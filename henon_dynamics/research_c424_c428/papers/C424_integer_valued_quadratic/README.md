# C424 — integer-valued quadratic Hénon maps

2026-09-09 UTC. **Two manuscript reviews accepted; final deterministic
build pair and all-page inspection complete; paper-local writes frozen.
NOT SEALED.**

[Read the complete article](main.pdf): 21 pages, 463423 bytes.
SHA-256: `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b`.
The selected output is the actual second new final build
`build/final_frozen_02/main.pdf`, copied to `main.pdf` after verification.
It is byte-identical to the first new final build and the reviewed PDF.

The article classifies rational periodic points of every degree-two
integer-valued polynomial in the native conservative map `(y,P(y)-x)`.
The complete finite computer-assisted input and the precisely attributed
internal C412 predecessor remain substantive dependencies; the source
cycle counts do not supply target Euler factors or root numbers.

## Current receipts and reproducibility

- [Final build and every-page inspection report](FINAL_BUILD_REPORT.md):
  exactly two new builds, both exit 0, each with 3 pdfLaTeX and 2 BibTeX
  passes; identical bytes, clean converged diagnostics and 22 embedded
  font resources. All 21 freshly rendered pages and all 1107 text lines
  were inspected.
- [Complete 29-input inventory](INPUT_MANIFEST.sha256): unchanged from
  both manuscript reviews and verified against `baseline/round0_layout1/`.
- [Manuscript improvement record](PAPER_IMPROVEMENT_LOG.md) and
  [state](PAPER_IMPROVEMENT_STATE.json): both real nonauthor passes were
  adjudicated PASS/no-change by the coordinator; zero revisions required.
- [First actual review](../../manuscript_reviews/round1/C424_REVIEW.md)
  and [second actual review](../../manuscript_reviews/round2/C424_REVIEW.md).
- [Citation and dependency audit](CITATION_AUDIT.md), complete
  [C412 predecessor](evidence/C412_main.pdf), all original proof/code/JSON
  evidence in `evidence/`, and [initial build history](BUILD_HISTORY.md).

`scripts/build.sh` is the presentation-only entry; the final invocations
used `build/final_frozen_01` and `build/final_frozen_02`, both previously
absent, with `SOURCE_DATE_EPOCH=1788912000`. Do not overwrite the preserved
logs or rerun mathematical evidence merely to rebuild the article.
The two final build directories and the original baseline directories
are retained. The no-change `main_round0_original.pdf`, `main_round1.pdf`
and `main_round2.pdf` aliases record review stages, not extra builds.

The older AUTHOR_REPORT and initial BUILD_HISTORY are historical
pre-review receipts; the current state is recorded above and in the
final report. Formal Route-A evaluation, global release membership and
manifest verification, sealing, and Git integration are coordinator-
owned and are not certified by this paper-local build completion.
