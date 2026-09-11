# Route A — final QA report for P187–P191

terminal_status=PASS
papers=5
review_replays=10
cold_builds=10
visual_pages=20
pdf_manifest_rows=20
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL

Terminal QA bound the following final conditions:

- every live `main.pdf` equals the accepted `main_round2.pdf`;
- every paper reproduced its live PDF in two physical source-only cold builds;
- every paper produced one visual PNG per page at 220 dpi;
- every rendered page has a paper-local, page-numbered observation row recording
  the absence of clipping, overlap, broken glyphs, and unintended truncation;
- all ten review packages replayed byte-identically to their canonicals;
- all paper, review, QA, and sequence manifests close mechanically;
- the 21-row `PACKAGE_MANIFESTS.sha256` binds the five paper manifests, five
  cold-build manifests, ten authoritative review manifests, and QA manifest;
- one generating terminal-audit pass and two subsequent clean-process passes
  reproduced `qa/CANONICAL.txt` byte for byte via `cmp`.

This final QA report is an internal artifact-integrity receipt only. It does
not widen the owner boundary or authorize external release beyond
`HOLD_EXTERNAL`.
