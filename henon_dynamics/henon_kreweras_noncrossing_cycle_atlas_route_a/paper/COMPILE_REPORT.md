# C209 compilation report

Engine: LuaLaTeX (`lualatex -interaction=nonstopmode -halt-on-error`).
`SOURCE_DATE_EPOCH=1787875200` was fixed for every pass.  Each round used two
fresh passes so references and page anchors settle before the PDF was copied.
The source sets `\pdfvariable suppressoptionalinfo 611`, making the final PDF
ID independent of the build directory as well as the fixed epoch.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 4 | `42f8cac5839c41340bb98fd08605485c665fb686b131979a8170340b6d61b55c` |
| `main_round1.pdf` | 4 | `1bd292ce2c1eee0eeb2216b86498464fb2f957fa61629bca022ecb4f88b0b253` |
| `main_round2.pdf` | 4 | `79318d957ab3fdd8560d232e195dcdb0eb4febe7c312bd75a6f7a8c1011105cb` |
| `main.pdf` (round 2) | 4 | `79318d957ab3fdd8560d232e195dcdb0eb4febe7c312bd75a6f7a8c1011105cb` |

The three round hashes are distinct, and `main.pdf` is byte-identical to round
2.  The final stabilized two-pass log contains no warning, overfull, underfull, or undefined-reference
messages.  `pdfinfo` confirms four pages and embedded Latin Modern Type 1
fonts.  A second two-pass build with the same fixed epoch reproduced the final
hash exactly.
