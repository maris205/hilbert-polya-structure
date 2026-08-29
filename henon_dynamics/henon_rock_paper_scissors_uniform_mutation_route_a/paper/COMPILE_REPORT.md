# Compilation report

The three content-distinct revisions were each built twice in independent
fresh temporary directory trees with LuaLaTeX and
`SOURCE_DATE_EPOCH=1787875200`.  The settled bytes matched within each fresh
pair, and all sidecars were removed before manifest closure.  The release
`paper/main.pdf` is byte-identical to `main_round2.pdf`.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `c477b433d432b6f5d98435ed87334ecc946c15e5a36f3351cf6185c163e605f2` | 2 |
| `main_round1.pdf` | `faf1d3f3e0a185b5d6939695addeca01a9332b65ea26c10d2cb6fad1f253e6a5` | 2 |
| `main_round2.pdf` | `bfc8e4d24257aad4c273e74b1f6363707ae9b1e3dc69dee8cd74c6b99d03b2e6` | 3 |
| `main.pdf` | `bfc8e4d24257aad4c273e74b1f6363707ae9b1e3dc69dee8cd74c6b99d03b2e6` | 3 |

`pdfinfo` reports a three-page A4 PDF.  `pdffonts` reports embedded subset
fonts for every face.  The settled logs contain no errors, overfull/underfull
boxes, undefined references, or missing characters.  Text and visual audits
were performed; the paper explicitly retains the Route-A rejection and scope
firewall.
