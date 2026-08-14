# HCS-C52 compilation report

Status: **PASS; final PDF frozen**

## Build

- Command: `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Engine: pdfTeX via `latexmk` 4.76.
- Final exit status: 0.
- PDF: `main.pdf`.
- Page size: A4.
- Pages: 10.
- Bytes: 365781.
- SHA-256:
  `eb999119a0e2291bbd027fb7c70a69297d3421962b1353b83ddeaa9b5b28179d`.

The final `main.log` and `main.blg` contain no LaTeX/package warnings,
undefined citations or references, overfull or underfull boxes, or rerun
requests.  All fonts are embedded and subsetted; no Type 3 font occurs.
`pdftotext` completed successfully.

## Frozen manuscript-source hashes

| Artifact | SHA-256 |
|---|---|
| `main.tex` | `3525df6a6281b76a3d24602c22ad50f9a8addf2104dccc1e69e25692edb493d0` |
| `math_commands.tex` | `78e61b7dd77b038380cf600cde62779fb618c2584be2fc651a882c3bcdef3585` |
| `references.bib` | `77ecd82f2fe4978eb26655941627eb29f1b38bcaaf0f5b45ae0d995950c2f14c` |
| `sections/0_abstract.tex` | `4899977d2c972b91577600b232ebcdd55f6309279b6364ab94d4a5b22ba3251a` |
| `sections/1_introduction.tex` | `e23217e96236311cb2935c4c52912bac87de7e0b497ead8fd1df16e082204c41` |
| `sections/2_source_main.tex` | `eeb54f73e599a4ebcef5890c342ca971d8d44f08bb4064c867166a988cf5afb5` |
| `sections/3_monomial_group.tex` | `b02dbd0d4a4237350bec3906dc2d1529cc154d76fe43cf49a3295384c9a82711` |
| `sections/4_chow_projectors.tex` | `613e1a2c9064c4453d935fcc4ffe2bac5e729393c0548ab18d931c0342ebb99c` |
| `sections/5_cayley_character.tex` | `805685fa67d5d91c30cbb9e80238baef42489e95af8b096ad0ddab2e70c7bf5a` |
| `sections/6_graph_optimum.tex` | `2eaf4be8a56a0129d11b18a9a5092e4fddb28106dd8a573a1bbf98db623a4447` |
| `sections/7_route_scope.tex` | `378e027a2ad09ff4cccddbda50a3df15866746504aab711b5cb50145bd15ceb7` |
| `sections/8_declarations.tex` | `b2054ffda457fc2c483e748d6a6318f2c636de1b0b0579528cb4df355be6448b` |
| `sections/A_exact_tables.tex` | `c161bb1482931fc35eb5e6685f2d6baf80c4c55caaca358d8b4f40160829a2a7` |

## Visual audit

Rendered pages 1, 6, and 10 were inspected.  The title and abstract,
character table/equations, references, margins, page numbers, and line
breaks render cleanly with no clipping or unresolved markers.
