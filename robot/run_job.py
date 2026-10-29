"""Process every job in jobs/ that has no result yet.

Job file (written by Claude), e.g. jobs/2026-10-29-street-origins.json:
{
  "job_id": "2026-10-29-street-origins",
  "drive_root": "<Product Images folder id>",
  "items": [{"barcode": "6290360379876", "slug": "street-origins-bisous-bisous-paris-extrait-de-parfum-75ml"}]
}
For each item the robot looks in Drive folder <drive_root>/<barcode>/ for files named main.* and box.*,
processes them and writes images/<barcode>/<slug>.jpg and images/<barcode>/<slug>-with-box.jpg.
Results (sizes, method, public URLs, problems) go to results/<job_id>.json.
"""
import io, json, os, glob, sys, traceback
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
import processor

REPO = os.environ.get("GITHUB_REPOSITORY", "ambukecom/ambient-beauty-images")
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
IMG_TYPES = ("image/", "application/octet-stream")


def drive():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    info = json.loads(os.environ["GDRIVE_SA_KEY"])
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/drive.readonly"])
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def q(svc, query):
    out, token = [], None
    while True:
        r = svc.files().list(q=query, fields="nextPageToken, files(id,name,mimeType,size)",
                             pageSize=200, pageToken=token,
                             supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        out += r.get("files", [])
        token = r.get("nextPageToken")
        if not token:
            return out


def download(svc, fid, dst):
    from googleapiclient.http import MediaIoBaseDownload
    with io.FileIO(dst, "wb") as fh:
        dl = MediaIoBaseDownload(fh, svc.files().get_media(fileId=fid))
        done = False
        while not done:
            _, done = dl.next_chunk()


def selftest():
    """Synthetic bottle on a coloured background -> proves the AI cut-out + shadow work."""
    img = Image.new("RGB", (900, 1100), (196, 120, 150))
    d = ImageDraw.Draw(img)
    d.rectangle([330, 300, 570, 900], fill=(40, 40, 60))
    d.rectangle([410, 200, 490, 300], fill=(200, 170, 90))
    os.makedirs("images/_selftest", exist_ok=True)
    img.save("/tmp/selftest_src.jpg")
    info = processor.process("/tmp/selftest_src.jpg", "images/_selftest/selftest.jpg")
    info["url"] = RAW + "images/_selftest/selftest.jpg"
    return info


def run(job_path):
    job = json.load(open(job_path))
    jid = job["job_id"]
    res = {"job_id": jid, "items": []}
    if job.get("selftest"):
        res["selftest"] = selftest()
    svc = drive() if job.get("items") else None
    tmp = "/tmp/src"
    os.makedirs(tmp, exist_ok=True)
    for it in job.get("items", []):
        bc, slug = it["barcode"], it["slug"]
        r = {"barcode": bc, "slug": slug, "images": {}, "problems": []}
        try:
            folders = q(svc, f"'{job['drive_root']}' in parents and name = '{bc}' and "
                             "mimeType = 'application/vnd.google-apps.folder' and trashed = false")
            if not folders:
                r["problems"].append(f"no Drive folder named {bc}")
                res["items"].append(r)
                continue
            files = q(svc, f"'{folders[0]['id']}' in parents and trashed = false")
            for kind, suffix in (("main", ""), ("box", "-with-box")):
                cands = [f for f in files if f["name"].lower().startswith(kind)
                         and f["mimeType"].startswith(IMG_TYPES)]
                if not cands:
                    r["problems"].append(f"no {kind} photo in folder {bc}")
                    continue
                if len(cands) > 1:
                    r["problems"].append(f"{len(cands)} {kind} photos found, used {cands[0]['name']}")
                src = os.path.join(tmp, f"{bc}_{cands[0]['name']}")
                download(svc, cands[0]["id"], src)
                rel = f"images/{bc}/{slug}{suffix}.jpg"
                os.makedirs(os.path.dirname(rel), exist_ok=True)
                try:
                    info = processor.process(src, rel)
                    info.update(source_file=cands[0]["name"], url=RAW + rel, path=rel)
                    if info["product_share_of_source"] < 0.04:
                        r["problems"].append(f"{kind}: product is tiny in the source photo, check the result")
                    r["images"][kind] = info
                except Exception as e:
                    r["problems"].append(f"{kind}: processing failed: {e}")
        except Exception as e:
            r["problems"].append(f"error: {e}")
            traceback.print_exc()
        res["items"].append(r)
        print(json.dumps(r))
    os.makedirs("results", exist_ok=True)
    json.dump(res, open(f"results/{jid}.json", "w"), indent=2)


if __name__ == "__main__":
    for jp in sorted(glob.glob("jobs/*.json")):
        jid = json.load(open(jp))["job_id"]
        if not os.path.exists(f"results/{jid}.json"):
            print("running", jid)
            run(jp)
