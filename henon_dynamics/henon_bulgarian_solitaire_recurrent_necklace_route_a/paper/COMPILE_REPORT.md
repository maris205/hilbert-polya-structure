# C190 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Source epoch: `1787702400`; `FORCE_SOURCE_DATE=1`; `TZ=UTC`.
- Build: two successful LuaLaTeX passes per frozen artifact.
- Page geometry: A4, 595.276 by 841.89 points.

## Actual revision ledger

| artifact | pages | bytes | SHA-256 | substantive increment |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 181,882 | `5aeb6d8128631751374a0dbc710095c781334a8bc4681724b7894adae12819af` | Brandt coordinates, fixed/cycle ledger, zeta, triangular and evidence boundaries |
| `main_round1.pdf` | 2 | 189,864 | `85cc22910952e28904f73362d1b0d801aca7c6d55631edfaee7388fdb5cbb366` | full characteristic polynomial, transient zero multiplicity, root spectrum, N=8 spectral sentinel |
| `main_round2.pdf` | 2 | 211,683 | `aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d` | recurrent reflection, nonfaithful/global boundary, exact audit totals, Route-A stop, compact declarations and references |
| `main.pdf` | 2 | 211,683 | `aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d` | byte-identical release copy of round 2 |

The three revision hashes are pairwise distinct.  The source was revised and
recompiled between rounds; the PDFs are not macro-only relabelings.

## Independent deterministic rebuilds

Two fresh temporary directories, each seeded only with final `main.tex`, were
built twice at the frozen epoch.  Both output hashes were
`aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d`;
both files were byte-identical to `paper/main.pdf`.

## Release checks

- Final and both fresh-build logs contain no warnings, undefined references,
  missing characters, overfull or underfull boxes, fatal messages, or errors.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves both abstracts, all formulas, the strict Route-A
  tuple, declarations, and both verified DOI references.
- Both rendered pages were inspected at 140 dpi: no clipping, collision,
  overlap, broken glyph, or illegible equation was found.  Compact section
  spacing, declarations, and footnote-size references remain readable.
- A first round-2 render exposed a literal `qquad`; the missing backslash was
  repaired before the frozen final build and the page was reinspected.
