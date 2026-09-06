# C407 author-side draft build

2026-09-06. This records a private draft check, not the final release QA,
human peer review, or a publication-priority certificate.

## Result

- Complete anonymous manuscript: `paper/main.tex`, `paper/math_commands.tex`,
  and `paper/sections/0_abstract.tex` through `7_scope.tex`.
- All new theorem proofs are in the body. Classical detector and counting
  inputs are cited where used. Four inline bibliography entries are present;
  no separate `.bib` is required by this build.
- The accepted outline is `PAPER_PLAN.md`; `paper/ABSTRACT_ZH.md` is a
  separate Chinese summary and is intentionally not a LaTeX input.
- Draft PDF: `/tmp/c407-author-draft-sNicvd/main.pdf`.
- Build log: `/tmp/c407-author-draft-sNicvd/main.log`; retained rerun output:
  `/tmp/c407-author-draft-sNicvd/compile.log`.
- PDF: 13 A4 pages, 411,706 bytes. Body and bibliography share page 13.
  No venue page cap was supplied for this pure-mathematics internal article.
- PDF SHA256:
  `12cecce888926bcce1b89999c043eeff5c182253dedcba0e7827d387e0d849be`.

## Build and checks

The source directory was used only for input. All generated output was
sent to a unique directory created by `mktemp -d` under `/tmp`.
The environment was:

```text
SOURCE_DATE_EPOCH=1788652800
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

The build used `latexmk -pdf -interaction=nonstopmode -halt-on-error`,
with its output directory set to the path above. The first fresh build
settled cross-references automatically. A subsequent `latexmk -g` rerun
was retained in `compile.log` and exited successfully. This rerun reused
the same directory and is **not** a second independent fresh build.
The preamble has explicit A4 geometry and guarded PDF date/trailer/PTEX
suppression settings.

Checks on the settled build:

- LaTeX warnings: zero.
- Undefined references/citations: zero.
- Overfull boxes: zero; underfull boxes: zero.
- All reported fonts embedded.
- Extracted PDF text contained no `??`, `[?]`, `VERIFY`, `TODO`, `TBD`,
  or `PLACEHOLDER` marker.
- Every section file is included by `main.tex`; all four bibliography keys
  are actually cited. No orphan `.tex` section or generated build artifact
  remains in the manuscript directory.
- Representative pages 1, 2, 7, and 13 were rasterized and visually
  inspected: title/abstract, the scope table, Fourier proof, and final
  provenance/bibliography were readable without apparent clipping.
  This sample inspection is not represented as a full-page visual audit.

No source edit was required by compilation. The source snapshot announced
to the independent manuscript reviewer therefore remained unchanged.
The prior-work qualifier requested by that reviewer was incorporated
before this snapshot: the BC2018 description now explicitly specifies
the unique-dominant-root and not-very-inseparable branch.

## Remaining release boundary

The root agent owns independent review consolidation, two final builds
from fresh directories, the complete final PDF/visual QA, and any release
copy. The author did not create `paper/main.pdf`, modify global evaluation
records, or perform a Git operation. The mathematical scope remains the
hyperbolic regimes left open in the checked BCH 2024 public version;
comparison with the unavailable final EMS book text remains unresolved.
