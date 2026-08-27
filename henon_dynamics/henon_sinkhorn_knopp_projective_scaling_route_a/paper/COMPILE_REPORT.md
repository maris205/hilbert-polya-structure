# C191 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Fixed source epoch: `1787788800`; `FORCE_SOURCE_DATE=1`.
- Build: two successful LuaLaTeX passes per frozen artifact.
- Page geometry: A4, 595.276 by 841.89 points.

## Actual revision ledger

| artifact | pages | bytes | SHA-256 | substantive increment |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 146,876 | `0f03c7e80934a079889b62fa664bbfaadaee7ce93bcae01cedfa95d00822c127` | support, total-support and full-indecomposability classification with the support-not-total boundary |
| `main_round1.pdf` | 2 | 146,898 | `3f41001054f429d37994f2ecd16089cce92a5f533a92022f72f7da99213db770` | positive projective map, Hilbert contraction, exact `S^T S` Jacobian, local rate and four boundary witnesses |
| `main_round2.pdf` | 2 | 146,909 | `b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129` | complete source ownership, periodic-orbit stop, executable evidence ledger, nonclaims and exact Route-A rejection |
| `main.pdf` | 2 | 146,909 | `b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129` | byte-identical release copy of round 2 |

The three revision hashes are pairwise distinct.  The rounds contain actual
mathematical and audit increments rather than macro-only relabeling.

## Independent deterministic rebuilds

Two fresh temporary directories, each seeded only with final `main.tex`, were
compiled twice at the fixed epoch.  Both output hashes were
`b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129`;
both files were byte-identical to `paper/main.pdf`.

## Release checks

- The retained final and round logs contain no warnings, undefined references,
  missing characters, overfull or underfull boxes, fatal messages or errors.
- Both fresh-build logs satisfy the same clean-log test.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves both abstracts, all formulas, the strict Route-A
  tuple, declarations and all four DOI references.
- Both pages were rendered and visually inspected: no clipping, collision,
  overlap, broken glyph, anomalous whitespace or illegible equation was found.

No warning or unresolved publication issue remains.  Generated `.aux`, `.log`,
`.out` and Python cache files are build sidecars and are excluded from the
release manifest.
