import json
# id, title, handle, barcode for today's 30 drafts (all mediaCount 0, all folders renamed to barcode)
rows = json.load(open('runs/2026-11-21-b4/photo_targets.json'))
job = {"job_id": "2026-11-21-b4-photos", "drive_root": "18basmN8GWnhplngT_Sb5gIvNp4v3lfCJ",
       "items": [{"barcode": r["bc"], "slug": r["handle"]} for r in rows]}
json.dump(job, open('jobs/2026-11-21-b4-photos.json', 'w'), indent=1)
print(len(job["items"]))
