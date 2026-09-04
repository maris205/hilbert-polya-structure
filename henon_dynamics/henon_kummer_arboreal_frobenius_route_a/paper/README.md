# Paper artifacts

`main_round0.tex`, `main_round1.tex`, and `main_round2.tex` are distinct wrappers around the auditable conditional source `main_body.tex`.  Each wrapper has its own deterministic trailer identifier and adds a substantive theorem layer.  Their PDFs are preserved beside them; `main.pdf` equals the final round byte for byte.

Every round contains an English abstract and an independently written Chinese abstract, each with 5--7 language-matched keywords.  The release gate rejects later-round conclusions or evidence in earlier artifacts and requires an embedded subset CJK font.

Run `python -B ../code/c374_release_manifest.py --write --build-pdfs` from this package directory to rebuild all paper artifacts and reports.
