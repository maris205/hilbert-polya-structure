# P205 manuscript Review B — source-only build and actual page inspection

Build/render/visual inspection performed 2026-09-05 UTC by the B reviewer.
Receipt completed 2026-09-06 UTC. The service interruption did not change
the scientific inputs or invalidate this physical build/view dependency.
This is one actual reviewer build, not either of the two terminal builds
that root must later perform on accepted final inputs.

## Input and executed build

Reviewed freeze:
`/root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/frozen_round1/`.
All 22 nonself files and the freeze's own manifest are pinned in
[INPUT_PINS.sha256](INPUT_PINS.sha256). `sha256sum -c` actually passed all
23 entries. Frozen `SHA256SUMS` has SHA256
`f6e2115a024fa8b95e80a2362ea65f8a4223e83ea4ebb3c66a825add225d5135`.

The following source-only helper was read in full and actually executed
from `/root/autodl-tmp/symbolic_dynamics`, with child exit **0**:

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/frozen_round1 /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p205_b/cold_build /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/frozen_round1/main.pdf
```

The destination did not exist. The helper created a new `mktemp` build
stage and copied **only** `main.tex`, `math_commands.tex`,
`references.bib`, and the five `sections/*.tex`. It did not seed any PDF,
auxiliary, bibliography output or log. The eight copied inputs are pinned
in [cold_build/SOURCE_INPUTS.sha256](cold_build/SOURCE_INPUTS.sha256), and
all eight were subsequently checked with `sha256sum -c`, exit zero.

Within that new stage the actual engine sequence was:

```sh
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
```

All four children exited zero under the helper's `set -euo pipefail`.
Complete pass stdout, BibTeX stdout, final `.log`, `.blg`, `.fls`, `.bbl`
and auxiliary products remain under [cold_build/](cold_build/). No initial
or intermediate warning is erased; the final diagnostic scan, including
undefined references/citations, warnings, over/underfull boxes and fatal
errors, found none. `DIAGNOSTICS.txt` is genuinely empty, not a template.

Actual engines and settings:

- pdfTeX `3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian);
  full version output is [ENGINE.txt](cold_build/ENGINE.txt).
- BibTeX `0.99d` (TeX Live 2022/dev/Debian);
  full version output is [BIBTEX_ENGINE.txt](cold_build/BIBTEX_ENGINE.txt).
- `SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
  `LC_ALL=C`; actual [environment record](cold_build/BUILD_ENVIRONMENT.txt).

## Output and raw comparison

The fresh [PDF](cold_build/main.pdf) is 306,286 bytes, **3 A4 pages**,
PDF 1.5, unencrypted. Author/title/creator/producer/date metadata are
empty. [PDFINFO.txt](cold_build/PDFINFO.txt) records the actual output.
[FONTS.txt](cold_build/FONTS.txt) lists 25 font rows, all Type 1 and all
embedded; no unembedded or Type 3 font occurs.

The fresh and frozen PDFs have the same SHA256:

`f4aec5af74f6ab4a78e1120270e818f20b412694d9d7938145564b9b447e41cc`.

The helper's raw comparison passed, and the following explicit subsequent
comparison also actually ran with no output and exit **0**:

```sh
cmp docs/papers204_208_sequence/reviews/p205_b/cold_build/main.pdf papers/205-conflict-triggered-cyclic-increments/frozen_round1/main.pdf
```

This is actual byte identity, not visual similarity or normalized text.

## All three pages were actually viewed

The fresh PDF was rendered with `pdftoppm -png -r 120` into `views/`,
exit zero. I then opened and visually inspected **each** of the three PNGs;
the receipt is not inferred from existence, hashes, `pdfinfo` or text
extraction. The following page-specific checks describe the inspected
images on 2026-09-05:

| Actual page | Inspection result | PNG SHA256 |
|---|---|---|
| [1](views/page-1.png) | Title/abstract, literal setup, all initial citation contexts, distance definition and beginning of temporal theorem readable; no clipping, overlap or missing glyph. | `b27999f90c0ffaa1f6ae6d546e13227c064f905d19aef792006e59218f2cac56` |
| [2](views/page-2.png) | Temporal theorem continues correctly over the page boundary, its proof is readable, then all three inverse conditions and proof; beginning of static lemma is intact. | `ed02cee6de6672f66866a8b792b082a05b531e8e753b14c1983a28bc4896010c` |
| [3](views/page-3.png) | Static lemma/proof continuation, all six boundary counts, maximum-fibre theorem/proof, scope and all four bibliography entries present; no overflow, clipped equations or broken end matter. | `da67d08174acaf77b523556fc95c7f698ccec6ea244feb49637c559b401c8acd` |

Verdict for this build/view obligation: **PASS**. Page-break continuations
are ordinary readable layout, not missing proof text. No typography or
build repair is requested. These records and all retained build products
are included in the review package's complete nonself manifest.
