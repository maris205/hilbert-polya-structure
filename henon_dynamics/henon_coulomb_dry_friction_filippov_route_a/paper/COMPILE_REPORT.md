# Compilation report

The three content-distinct revisions were each built twice in independent
fresh temporary directory trees with LuaLaTeX and
`SOURCE_DATE_EPOCH=1787875200`.  The settled bytes matched within each fresh
pair.  Build sidecars stayed in the temporary trees and are excluded from the
release; `paper/main.pdf` is byte-identical to `main_round2.pdf`.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `60787bfb50fbfc245225e2fa019550711cf437340f135ddabeaf33b0c78fbca1` | 2 |
| `main_round1.pdf` | `54ff4f5dd119f6186d1407cd6f255aded468b856064994a8c9cf592deb0220c9` | 2 |
| `main_round2.pdf` | `604965d87e02c4f6cb22750d214b0ea402ec743f1c8ca2bdc3e0a6da1a5602f2` | 2 |
| `main.pdf` | `604965d87e02c4f6cb22750d214b0ea402ec743f1c8ca2bdc3e0a6da1a5602f2` | 2 |

`pdfinfo` reports a two-page A4 PDF.  `pdffonts` reports embedded subset
fonts for every face.  The settled second-pass logs have no errors,
overfull/underfull boxes, undefined references, or missing characters (the
first pass has only the normal rerunfilecheck notice).  Text and visual audits
were performed; the paper explicitly retains the Route-A rejection and scope
firewall.
