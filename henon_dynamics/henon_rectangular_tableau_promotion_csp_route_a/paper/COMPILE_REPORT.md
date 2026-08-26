# C187 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Source epoch: `1787702400`; `FORCE_SOURCE_DATE=1`; `TZ=UTC`.
- Build: two successful LuaLaTeX passes per revision artifact.
- Page geometry: A4, 595.276 by 841.89 points.

## Content-distinct revision ledger

| artifact | pages | bytes | SHA-256 | distinguishing paragraph |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 171,811 | `9cde82b4142018eff14e6ce4ab13758ed9cf870da8a8543815aafe0f0a62093c` | convention, unshifted CSP, order boundary, cycle recovery |
| `main_round1.pdf` | 2 | 171,766 | `6bc413378ca4752fd27c710badcf4387eb3440e75cbf6978e342da1f5a459264` | zeta, determinant, traces and root multiplicities |
| `main_round2.pdf` | 2 | 171,759 | `eace7ed5e6e5d0233eddeda5653ae389c9d8e5df1708c7242fc72aa971e533cc` | evacuation, evidence boundary and adversarial stop |
| `main.pdf` | 2 | 171,759 | `eace7ed5e6e5d0233eddeda5653ae389c9d8e5df1708c7242fc72aa971e533cc` | byte-identical release copy of round 2 |

Extracted text confirms that the three revision-focus paragraphs differ, and
the three revision hashes are pairwise distinct.

## Independent deterministic rebuilds

Two fresh temporary directories, each seeded only with `main.tex`, were built
twice at the frozen epoch.  Both output hashes were
`eace7ed5e6e5d0233eddeda5653ae389c9d8e5df1708c7242fc72aa971e533cc`;
both files were byte-identical to `paper/main.pdf`.

## Release checks

- Final and fresh-build logs contain no warnings, undefined references,
  missing characters, overfull or underfull boxes, fatal messages, or errors.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves the English theorem, Chinese abstract, equations,
  Route-A verdict and both references.
- Both rendered pages were inspected at 130 dpi: no clipping, collision,
  blank page, broken glyph, or illegible table was found.
