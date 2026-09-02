# Compilation report — HCS-C285

## Deterministic build contract

- Engine: LuaLaTeX
- Passes per build: 2
- Fresh builds per revision: 2
- `SOURCE_DATE_EPOCH=1788307200`
- `FORCE_SOURCE_DATE=1`
- `TZ=UTC`
- Optional metadata suppressed and trailer ID fixed in `main.tex`

Each of the six fresh builds was byte-identical to its partner and to the
corresponding archived PDF.

| revision | pages | bytes | embedded/subset font rows | SHA-256 |
|---|---:|---:|---:|---|
| round 0 | 2 | 163,153 | 22/22 | `281d88d391a2ca9fdf79ba30ac840959150bf9081954571e7c9543c0ea798fe5` |
| round 1 | 3 | 185,026 | 23/23 | `ab2bf74aa9be4ab4a1a33b1b584755ab505e807134514b40e9bdb781ea13052d` |
| round 2 | 4 | 194,169 | 24/24 | `088d2ca85d86d1e1fc797071bef5aa8c4a4364178f0ab61f454d77df14e6000e` |

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf`.

## Log audit

Every final-pass log was scanned for:

- `LaTeX Warning` and package warnings;
- `Overfull`, `Underfull`, and bad-box/layout warnings;
- undefined or rerun-needed references;
- missing characters;
- citation warnings.

All counts are zero. The bibliography is internal, contains only the three
cited verified sources, and has no unresolved citation. All PDF fonts are
embedded and subset.

## Text and visual audit

Extracted text from every round contains its revision identity and common
theorem/ownership/nonclaim contract. The final round contains the finite theorem, exact reversal, complete
bottleneck limit, `Dirichlet(1,...,1)`, the boundary atlas, Gordon–Newell
ownership DOI, checker/SymPy/replay/mutation counts, literal scope, the exact
all-fail tuple, `ROUTE_A_REJECTED`, Route-B false, and no-formal-quantization
language. Positive/negative sentinels also confirm the corrected state-space
glyph and the intended `case. Zero population` abstract sentence boundary.

All 2+3+4 rendered pages were visually inspected. Titles, abstracts,
equations (1)–(15), proof boxes, the boundary table, hyperlinks, references,
page numbers, margins, and line breaks are legible; no clipping, collision,
blank page, missing glyph, or malformed rule is visible.

Status: **SUCCESS — warning-free, font-embedded, visually inspected,
deterministic three-round PDF closure.**
