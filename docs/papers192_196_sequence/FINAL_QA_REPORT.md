# Route A — final QA report for P192–P196

terminal_status=PASS
papers=5
review_packages=10
author_replay_executions=10
review_replay_executions=20
cold_builds=10
visual_pages=20
pdf_manifest_rows=20
grand_evidence_assertions=56517656
open_findings=critical:0,major:0,minor:0
external_status=OWNER_RED_AMBER_P192;OWNER_AMBER_P193_P196;HOLD_EXTERNAL

Terminal QA bound the following final conditions:

- every live `main.pdf` equals the accepted `main_round2.pdf`;
- every paper reproduced its live PDF in two physical source-only cold builds;
- every paper produced one visual PNG per page at 180 dpi, and all 20 pages
  were inspected for clipping, overlap, broken glyphs, and unintended
  truncation;
- all five author controls and all ten process-separated hostile-review
  controls replayed twice byte-identically to their canonical transcripts;
- the canonical evidence counters total 15,387,752 author assertions,
  9,347,475 Review-A assertions/checks, and 31,782,429 Review-B assertions;
- all paper, review, QA, canonical-PDF, and aggregate package manifests close
  mechanically;
- the 21-row `PACKAGE_MANIFESTS.sha256` binds the five paper manifests, five
  cold-build/visual manifests, ten authoritative review manifests, and the
  central QA manifest;
- after one preflight receipt-label correction, two full clean-process audit
  passes reproduce `qa/CANONICAL.txt` byte for byte.

P194 is the only paper whose Round-2 PDF differs from Round 1. The difference
is the accepted Defant--Williams citation, zero-credit statement, and exact
map separation; the theorem statements, numbered formulas, proofs, example,
author verifier, and canonical transcript are unchanged. P192's all-`n`
history law and its consequences remain explicitly conjectural.

This final QA report is an internal artifact-integrity receipt only. It does
not widen the owner boundary, prove novelty or priority, certify freedom to
operate, or authorize external release beyond `HOLD_EXTERNAL`.
