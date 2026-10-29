# Ambient Beauty image robot

Turns supplier/web product photos into the store's standard image:
2048×2048 JPG, white background, product centred with 8% padding, "Reef 19" wall shadow.

**How it runs**
1. Photos go in Google Drive → `Product Images/<barcode>/main.*` and `box.*`.
2. Claude adds a job file in `jobs/` listing barcodes and SEO file names.
3. This repository's workflow reads Drive with a read-only robot account (key stored as the
   encrypted secret `GDRIVE_SA_KEY`, never in the code), processes the photos and saves them in
   `images/<barcode>/` with a report in `results/`.
4. Claude checks each image, then attaches it to the Shopify **draft** by its public address.
   Shopify keeps its own copy.

Code: `robot/processor.py` (image standard), `robot/run_job.py` (Drive + jobs).
