# C194 compile report

Status: PASS.

## Frozen build

- Engine: XeTeX 3.141592653-2.6-0.999993, XeLaTeX format (TeX Live
  2022/dev/Debian).
- Fixed source epoch: `1787788800`; `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
  `LC_ALL=C`.
- Build: two successful XeLaTeX passes for each frozen artifact.
- Page geometry: A4, 595.28 by 841.89 points.

## Actual revision ledger

| artifact | pages | bytes | SHA-256 | substantive increment |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 59,446 | `fc82f08bef150d20de466ee8092b738da02b69d28590688c95724187a7d888d0` | transition window, mixed-radix semigroup, simple spectrum, Eulerian stationarity and initial Route-A verdict |
| `main_round1.pdf` | 2 | 63,345 | `48b078942789c3654b92c5a8112ec85225c652eb16860ee5a2254b014c1afd43` | common spectral projectors, exact convergence identity, sourced TV bound and explicit small-`n` boundary |
| `main_round2.pdf` | 2 | 69,281 | `9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7` | classical ownership table, prime/composite controls, exact certificate metrics, exact frozen Route-A tokens, scope literal and strengthened nonclaims |
| `main.pdf` | 2 | 69,281 | `9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7` | byte-identical release copy of round 2 |

The three round hashes are pairwise distinct, and `main.pdf` is byte-identical
to round 2.

## Independent deterministic rebuilds

Two fresh temporary directories were each seeded only with final `main.tex`
and compiled twice under the frozen environment.  Both hashes were
`9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7`,
byte-identical to the released final PDF.

## Release checks

- The final release pass-2 log examined at build time and both fresh pass-2
  logs contain no warnings,
  undefined references, missing characters, overfull or underfull boxes,
  badness diagnostics, fatal messages or errors.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves the abstract, all eight numbered equations, both
  DOI references, exact metrics, Route tuple and forbidden-claim boundary.
- Both pages were rendered at 144 dpi and visually inspected.  There is no
  clipping, overlap, collision, broken glyph, illegible equation or anomalous
  whitespace.

No warning or unresolved publication issue remains.  XeLaTeX sidecars and
Python caches are excluded from the release manifest.
