# Paper 8 manuscript release

**Title:** *Isotropy Averaging Erases Returns: Character Traces and a Fixed-Map Normality Obstruction on Deninger Prime Orbits*

**Author:** Liang Wang, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology (HUST), `wangliang.f@gmail.com`

## Claim boundary

The locked verdict hierarchy is:

- packet completion/bridge: `NOT_TESTABLE`;
- fixed chosen one-orbit analogue: `REFUTED`;
- positive-time scalar Radon ledger: `PASS`.

The manuscript makes no determinant, A3, A4, Route B, global all-prime operator, or Hilbert--Pólya claim.

## Release contents

- `paper.pdf` — release PDF;
- `manuscript.tex` — XeLaTeX source;
- `references.bib` — cited bibliography (14 entries, with manifestation-specific locator notes);
- `figures/owner_map.tex` — native TikZ owner/stop map;
- `figures/character_filter.tex` — native TikZ character-filter diagram.

Both figures are native TikZ. No external raster or vector figure is imported into the manuscript.

## Build

From this directory, run:

```sh
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The audited build used XeTeX/TeX Live 2022-dev and the TeX Gyre Termes, TeX Gyre Termes Math, TeX Gyre Cursor, Noto Serif CJK SC, and Noto Sans Mono CJK SC font families.

## Verification record

The release lock was audited on 2026-08-14 (CST):

- 19 A4 pages, PDF 1.5;
- no unresolved citation or cross-reference;
- no overfull box, missing glyph, undefined control sequence, or BibTeX warning;
- two harmless underfull boxes remain: badness 10000 in the English abstract (source lines 93--95) and badness 1038 in the prior-mathematics paragraph (source lines 148--149);
- every PDF font reported `emb=yes`, `sub=yes`, and `uni=yes` under `pdffonts`;
- `pdftotext`, `pdfinfo`, and `pdffonts` checks passed;
- representative raster pages 1, 7, 9, 15, 16, 18, and 19 were visually inspected for clipping, collisions, tables, figures, equations, declarations, and references.

The deterministic control suite was also reproduced from the project directory with `./experiments/reproduce.sh`: 18/18 tests passed, nine CSV artifacts contained 129 rows, two fresh generations were byte-identical, and `results/isotropy_trace_manifest.json` had SHA-256 `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`.

## Release hashes

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` |
| `references.bib` | `a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e` |
| `figures/owner_map.tex` | `b1978bcd5f37cb470096f36b3f05c7a5bc4abf30001b417d8eda5094bd54a34d` |
| `figures/character_filter.tex` | `6405ba10b414dfebc5d25811d26b71f3cccccd07f554ce56ee83af55061e72a7` |
| `paper.pdf` | `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a` |

## Source-PDF distribution boundary

Citation reproducibility and redistribution permission are separate questions. A public GitHub sync must exclude `../notes/sources/*.pdf` unless a redistribution licence has been documented for that exact manifestation. The local research copies are not deleted by this packaging step. Source manifests, SHA-256 inventories, URLs, exact locators, and preflight sidecars remain available for audit and may be synchronized.

