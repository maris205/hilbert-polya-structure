# Compile and PDF audit

The manuscript was compiled with LuaHBTeX/LuaLaTeX at fixed
'SOURCE_DATE_EPOCH=1787875200' and 'FORCE_SOURCE_DATE=1'.  Each revision was
compiled twice in independent output directories; byte comparison passed for
all three pairs.

text:
lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main_round0_original '\def\CRevisionRound{0}\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main_round1 '\def\CRevisionRound{1}\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main_round2 '\def\CRevisionRound{2}\input{main.tex}'


| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| main_round0_original.pdf | 1 | 112441 | 6b2a70d3ecc166c787a1124e4b2689e619dd6363c1f63430e8d180453344d23b |
| main_round1.pdf | 2 | 118710 | d4d9883869f02f4a45b275a5c8d92722054ccf7b3d1ffbf2462fea79368696a5 |
| main_round2.pdf | 2 | 141332 | 10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05 |
| main.pdf (release = round 2) | 2 | 141332 | 10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05 |

cmp reports identical bytes for the two builds of each round, and the three
release-round hashes are pairwise distinct.  `pdffonts` reports 21 font
instances, all embedded and subsetted.  `pdftotext` contains the
Runge–Lenz, radial-action, Levi–Civita, integer-strobe, Artin–Mazur, scope, and
Route-A boundary phrases.  The LaTeX logs contain no overfull/underfull box,
undefined-reference, rerun, or fatal-error diagnostics.
