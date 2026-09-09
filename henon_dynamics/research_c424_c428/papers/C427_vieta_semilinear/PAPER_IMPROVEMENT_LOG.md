# C427 actual manuscript improvement record

2026-09-09 UTC. Current-team internal nonauthor review; no external
model or human peer-review claim. The selected improvement workflow
requires two actual passes; both are now complete and adjudicated.

## Round 1: complete review and adopted clarification

The complete unabridged reviewer report is retained at
[round1/C427_REVIEW.md](../../manuscript_reviews/round1/C427_REVIEW.md),
SHA256 `4c6389db5de39eedc9a35e0732f4d5427805e80c77a6a3db3bcc23d231fac812`.
The coordinator read its entirety and accepts the zero-must-fix
recommendation. No journal score is invented. Optional O1 is adopted:
the abstract now explicitly says that the absolute value of the
coordinate exceeds `|a|+4`. The full body already used exactly that
condition; no proof, theorem or table changed.

The genuine pre-review baseline is preserved as
`main_round0_original.pdf` and `builds/initial_03/main.pdf`, SHA256
`ff63cdac04d87d212e7c902ce61c56695587e3b12379e180bd6f9c3c3e4dd021`.
Its source archive remains in `builds/initial_03/source.tar`.
Only `sections/00_abstract.tex` changed among the ten TeX/Bib inputs;
the current input manifest records its new digest. No artificial
intermediate mathematical version was created.

One real revised build ran in the new `builds/round1_revised/` directory:

```sh
env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=builds/round1_revised main.tex
```

Exit 0; three engine passes and two BibTeX passes. Shell `pipefail`
was enabled and a full console transcript was captured in `compile.log`.
Engine/BibTeX final logs have no warning, over/underfull box, undefined
reference/citation or TeX error. All 19 font resources remain embedded
Type 1 with Unicode maps. The actual revised PDF has 13 pages,
346694 bytes. `main.pdf`, `main_round1.pdf` and the revised build PDF
have SHA256 `cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1`.
Revised source archive SHA256:
`654d12dad810676f83e801727a9e46434963cf76552da37f7d70c9cce7e9f933`.

All revised pages were rendered and text extracted. The coordinator
freshly viewed page 1. A comparison with the baseline showed page 2
is not byte-identical after reflow, so the old all-page visual receipt
is not claimed for this revision. Round-two inspection and final
all-page release inspection remain explicit next gates. No mathematical
execution or old certificate replay was performed.

## Round 2

The full report is [round2/C427_REVIEW.md](../../manuscript_reviews/round2/C427_REVIEW.md),
SHA256 `d0ea10ebf7d90e76dc4e262a23738de1ea626f72c102211c4c6e0361ac0f4bc8`.
The coordinator read the complete report and accepts PASS: O1 closed,
zero must-fix and zero new optional findings. The reviewer reread the
entire revised PDF and all 13 new page images, checked each rendering
against a fresh current-PDF stream, and confirmed the complete ten-input
source/archive identity and sole abstract hunk. Exact-period quantifiers,
free parameters, projection, zero directions and the level-independent
remainder were separately challenged without finding a regression.

No second source correction was needed. `main_round2.pdf` is explicitly
a no-change byte alias of the reviewed `main_round1.pdf`, not a new build.
Both have the revised PDF hash printed above. The actual sole source diff
is preserved in `reviews/round1/source_changes.diff`. No mathematical
execution was added. The final fresh-build pair, formal evaluation and
release sealing are not closed by this log.
