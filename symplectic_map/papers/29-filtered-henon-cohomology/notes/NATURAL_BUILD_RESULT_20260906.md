# Natural-draft measurement and two-root build: actual result

Date: 2026-09-06. Status: BUILD_AND_PHYSICAL_PAGE_GATE_PASS.
Independent actual-PDF review and final integrity acceptance remain pending.

## Bound source and first measurement

Selected source: paper-successor-20260906-transcription-v1/.
SOURCE_BUILD_MANIFEST_20260906.sha256 has SHA256
958dd5be31db838485feff5512ac675960ce7caa296f02c1f05b82b6b87e01ee.
The original paper/ remains frozen. The sole pre-build correction was the
abstract's D>=1 qualifier; the independent 30-line fix receipt has SHA256
cda53a4bb6c150c490958989ac96915c44dab5463c8e36b071538ed5ec329b30,
and closes the sole minor source-review finding. Root read that receipt fully.

The first complete successful build was build/natural-20260906-r0/.
It produced **26 body pages and 1 reference page**, 27 physical pages total.
The main-body-end auxiliary label records page26, references-start records
page27, and physical PDF text confirms that References starts on page27.
Page26 contains the planned potential examples and conclusion, including the
geometric-point boundary; it is not a blank or label-only page. No appendix,
acknowledgments, blank body page or externally sourced illustration is present.
The original 22--30-body-page criterion is satisfied by this measurement.
No source content or formatting was changed after this measurement.

## Actual independent build roots

Both commands used the unchanged scripts/build-local.sh from SOURCE_BUILD_LOCK:

```sh
bash scripts/build-local.sh paper-successor-20260906-transcription-v1 build/natural-20260906-r0
bash scripts/build-local.sh paper-successor-20260906-transcription-v1 build/natural-20260906-r1
```

The second command ran only after the first measured body passed the page gate.
Each command created a new root and copied the selected source to its work/.
The environment was SOURCE_DATE_EPOCH=0, FORCE_SOURCE_DATE=1, TZ=UTC, LC_ALL=C.
The recorded engine is pdfTeX 1.40.22 (TeX Live 2022/dev/Debian), using the
installed LaTeX article class and size11.clo. No installation was needed.

| Root | pass1 | BibTeX | pass2 | pass3 | Final PDF |
| --- | --- | --- | --- | --- | --- |
| natural-20260906-r0 | exit0 | exit0 | exit0 | exit0 | 438693 bytes |
| natural-20260906-r1 | exit0 | exit0 | exit0 | exit0 | 438693 bytes |

The PDFs compare byte-for-byte equal (cmp exit0). Each has SHA256
774865fa38e7d6f053daf57a48a03da3eb52edf940694f1fa6c116287bd966e0.
The twelve source files in each work/ independently pass the selected source
manifest. This is local same-environment deterministic reproduction, not a
claim of cross-platform byte identity or a hermetic dependency capsule.

Every TeX pass has its own stdout log, copied TeX log and input recorder in
the corresponding build root. BibTeX stdout and its .blg are retained;
stages.log records each actual exit code. Initial cross-reference resolution
passes are preserved; both final pass3 logs and BibTeX logs have no undefined
references/citations, multiply defined labels, overfull/underfull boxes or
warning/error matches. No failed build root was overwritten or erased.

## Actual document checks and remaining review

pdfinfo reports letterpaper, 612x792 points, PDF1.5, an empty Author field,
the correct title, no encryption and no JavaScript. pdffonts lists20 font
rows; all are Type1 and embedded. There are no unembedded or Type3 fonts.
All27 pages were rendered at100dpi under natural-20260906-r0/render/.
The root inspected every individual page image, covering1--27, and observed
no clipped equations, overlapping text, missing glyphs or rendering defect.
All displayed equations and theorem continuations are present; the ordinary
page breaks follow the source's standard article layout.

A separate independent reader is checking the actual complete source, PDF
text and each of the27 individual images. That report is not replaced by
the root's visual check or by successful compilation. Final independent
integrity review must also bind the actual artifacts and accepted evidence
before Paper29 is counted. Current batch acceptance therefore remains2/5.
The original candidate R2 capacity FAIL and original conjunction FAIL remain
unchanged; this build is evidence under the later authorized measurement
exception, not a retroactive rewrite of either old review.
