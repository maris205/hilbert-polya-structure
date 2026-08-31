# Compile report

## Frozen build

- engine: LuaLaTeX 1.14.0;
- `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`;
- two LuaLaTeX passes in each fresh directory;
- two independent fresh directories per round;
- result: each same-round pair was byte-identical.

## Revision artifacts

| artifact | pages | SHA-256 | substantive content |
|---|---:|---|---|
| `main_round0_original.pdf` | 2 | `b030f6146a351a7b1bfc735e752ab30f24dc60d90135a87e9600ad2255db603e` | affine transform, stationary Laplace law, all moments |
| `main_round1.pdf` | 2 | `3f08ebc6287720f72655c6628ae13111ea212ff3286d57cd52c8fd3a9a05b4c8` | adds three-covariance separation, Bartlett convention, window variance |
| `main_round2.pdf` | 3 | `3c0283170bb6cf7d807e53fbcd814b268c59670649726200e0dcc9d44a98bc24` | adds Borel genealogy, boundary atlas, executable/collision audit, Route A |
| `main.pdf` | 3 | `3c0283170bb6cf7d807e53fbcd814b268c59670649726200e0dcc9d44a98bc24` | byte-identical final copy of round 2 |

The three revision hashes are distinct.  Round 2 and `main.pdf` are
byte-identical.

## Release audit

- all 21 reported fonts are embedded and subset;
- the final PDF has three US-letter pages and no encryption;
- second-pass logs have no LaTeX/package warnings, overfull or underfull
  boxes, undefined references, or rerun requests;
- PDF text contains the affine transform, Dirac atom, Bartlett convention,
  Borel law, Hawkes DOI, strict Route-A tuple, and scope literal;
- visual inspection of all three final pages found no clipping, overlap,
  broken formula, blank page, or unreadable table.
