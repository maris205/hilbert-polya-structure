# C327 compilation report

## Status

SUCCESS.  All revisions were built with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Artifact | Pages | SHA-256 | Embedded/subset font rows |
|---|---:|---|---:|
| `main_round0_original.pdf` | 2 | `a403ce74dbf518c00d78b28ae15842ed394c50e89b559c0869310035c9af9d81` | 23 |
| `main_round1.pdf` | 4 | `975a2fadf2038b156ab19ebd3d4e6a05508a6dd2ee00f2c1b307202b05524cde` | 23 |
| `main_round2.pdf` | 4 | `d721bb570785d9af6cf96cede73ed55fb97316ce5a39b77ca57b10ac791a5208` | 25 |
| `main.pdf` | 4 | `d721bb570785d9af6cf96cede73ed55fb97316ce5a39b77ca57b10ac791a5208` | 25 |

`main.pdf` is byte-identical to round 2.  The three revision hashes are
distinct and their required content tokens are extractable.

## Gates

- Two independent fresh two-pass builds per revision match the checked-in PDF
  byte for byte.
- Logs contain zero LaTeX/package warnings, overfull or underfull boxes,
  undefined references/citations, rerun requests, or missing glyphs.
- `pdffonts` reports every font embedded and subset.
- `pdftotext -layout` extracts all theorem and revision tokens without
  replacement/control-character defects.
- Every page rasterizes successfully; visual inspection found no clipping,
  overlap, missing equation, or unreadable element.
- No auxiliary build file is retained in the package.
