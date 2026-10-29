"""Ambient Beauty product image processor (approved "Reef 19" standard).

Any source photo, any size -> 2048x2048 JPG, white background, product centred
with 8% padding and the Reef 19 wall shadow (light from upper right).

Cut-out:
  * plain white / near-white backgrounds -> precise flood cut-out (keeps glass + labels)
  * anything else (coloured, lifestyle, props) -> AI background removal (rembg)
Small sources are upscaled with Lanczos + light sharpening (owner's rule: always process).
"""
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy import ndimage

SIZE = 2048
PAD = 0.08
BG = (255, 255, 255)
TOL = 18
_SESSION = None


def _session():
    global _SESSION
    if _SESSION is None:
        from rembg import new_session
        for model in ("birefnet-general", "isnet-general-use", "u2net"):
            try:
                _SESSION = new_session(model)
                _SESSION.model_name_used = model
                break
            except Exception as e:  # model download / load failure -> next model
                print(f"model {model} unavailable: {e}")
    return _SESSION


def load(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        if img.getextrema()[3][0] < 250:      # real transparency: use it as the cut-out
            return img, True
    return img.convert("RGB"), False


def white_background(img):
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    b = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    return ((255 - b).max(axis=1) <= TOL).mean() >= 0.85


def trim_reflection(a, fg):
    rows = np.where(fg.any(axis=1))[0]
    top, bot = rows[0], rows[-1]
    dark = (255 - a).max(axis=2)
    mean = np.array([dark[y][fg[y]].mean() if fg[y].any() else 0 for y in range(fg.shape[0])])
    y = bot
    while y > top and mean[y] < 110:
        y -= 1
    band = bot - y
    if band >= 0.015 * (bot - top) and mean[max(top, y - 5):y + 1].max() >= 1.6 * np.median(mean[y + 1:bot + 1]):
        fg = fg.copy()
        fg[y + 1:] = False
    return fg


def cutout_white(img):
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    nearwhite = (255 - a).max(axis=2) <= TOL
    lab, _ = ndimage.label(nearwhite)
    border = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    bg = np.isin(lab, border[border > 0])
    fg = ndimage.binary_fill_holes(~bg)
    fg = ndimage.binary_opening(fg, iterations=1)
    fg = trim_reflection(a, fg)
    alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = img.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba


def cutout_ai(img):
    from rembg import remove
    return remove(img.convert("RGB"), session=_session(), post_process_mask=True).convert("RGBA")


def crop_to_product(rgba):
    alpha = rgba.split()[3]
    solid = alpha.point(lambda v: 255 if v > 24 else 0)
    box = solid.getbbox()
    if not box:
        raise ValueError("no product found in the photo")
    return rgba.crop(box)


def compose(product):
    box = int(SIZE * (1 - 2 * PAD))
    s = min(box / product.width, box / product.height)
    while (SIZE - product.width * s) / 2 - 0.121 * product.height * s < 0.03 * SIZE:
        s *= 0.98
    p = product.resize((round(product.width * s), round(product.height * s)), Image.LANCZOS)
    if s > 1.15:  # upscaled: restore crispness lost in enlargement
        rgb, a = p.convert("RGB"), p.split()[3]
        rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
        p = rgb.convert("RGBA")
        p.putalpha(a)
    x, y = (SIZE - p.width) // 2, (SIZE - p.height) // 2
    canvas = Image.new("RGBA", (SIZE, SIZE), BG + (255,))
    alpha = p.split()[3]
    H = p.height
    dx, dy = round(-0.121 * H), round(0.056 * H)
    sil = Image.new("L", (SIZE, SIZE), 0)
    sil.paste(alpha, (x + dx, y + dy))
    sil = sil.filter(ImageFilter.GaussianBlur(max(4, 0.007 * H)))
    xs = np.arange(SIZE, dtype=np.float32)
    near, far = x + p.width + dx, x + dx
    t = np.clip((near - xs) / max(1, near - far), 0, 1)
    strength = 0.30 - 0.09 * t
    shadow = np.asarray(sil, dtype=np.float32) * strength[None, :]
    shadow = Image.fromarray(np.clip(shadow, 0, 255).astype(np.uint8))
    canvas.paste(Image.new("RGBA", (SIZE, SIZE), (30, 20, 10, 255)), (0, 0), shadow)
    canvas.alpha_composite(p, (x, y))
    return canvas.convert("RGB"), s


def process(src, dst):
    img, has_alpha = load(src)
    if has_alpha:
        rgba, method = img, "transparent source"
    elif white_background(img):
        rgba, method = cutout_white(img), "white-background cut-out"
    else:
        rgba, method = cutout_ai(img), f"AI cut-out ({getattr(_session(), 'model_name_used', '?')})"
    product = crop_to_product(rgba)
    out, scale = compose(product)
    out.save(dst, "JPEG", quality=84, optimize=True, progressive=True)
    cover = product.width * product.height / (img.width * img.height)
    return {"source_px": f"{img.width}x{img.height}", "method": method,
            "upscale": round(scale, 2), "product_share_of_source": round(cover, 2)}


if __name__ == "__main__":
    import sys
    print(process(sys.argv[1], sys.argv[2]))
