# C220 compilation report

Build contract: LuaLaTeX 1.14.0, A4 paper, fixed
`SOURCE_DATE_EPOCH=1787875200`, and two settled passes per revision.  Each
revision was compiled twice; the second pass was used as the settled artifact.
The final `main.pdf` is a byte copy of revision 2.  All three revision PDFs
are content-different.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `77ec4659b233d57ac6a518ce258b5ed5dcfb6905c416666c9ea4642c5847b13a` |
| `main_round1.pdf` | 3 | `cbf78443fb0f9465852d484770249981e8e9a1946f39a4b36d26a1003adabf69` |
| `main_round2.pdf` | 3 | `c68459c1d85934837d871cf1201c93923e5ac42b2aca784392c688030fe8f018` |
| `main.pdf` (equals round 2) | 3 | `c68459c1d85934837d871cf1201c93923e5ac42b2aca784392c688030fe8f018` |

The settled round-0, round-1, and round-2 logs contain no `Warning`,
`Overfull`, `Underfull`, `undefined`, or `Error` diagnostics.  `pdfinfo`
reports A4 pages and `pdffonts` reports 18 embedded, subset fonts.  A
`pdftotext` audit finds the required TASEP, matrix, current, phase,
`ROUTE_A_REJECTED`, `NO_BAD_EULER_OR_ROOT_NUMBER`, and Derrida anchors.
An independent two-directory clean rebuild reproduced the three hashes above
byte-for-byte for every revision.
Auxiliary LaTeX sidecars are removed before manifest closure.
