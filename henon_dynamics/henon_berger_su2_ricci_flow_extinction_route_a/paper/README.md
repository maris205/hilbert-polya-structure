# Paper artifacts: HCS-C360

`main.tex` is one conditional source.  Supplying `CRevisionRound=0,1,2`
produces the geometric-reduction original, the lifespan revision, and the
final normalized/Route-A revision.  `main.pdf` must be byte-identical to
`main_round2.pdf`.

The release gate performs two fresh LuaLaTeX passes twice per round at the
frozen epoch, then checks exact bytes, warnings, page count, embedded/subset
fonts, extracted text, and rasterization.  The manuscript uses native
equations rather than a redundant external figure.
