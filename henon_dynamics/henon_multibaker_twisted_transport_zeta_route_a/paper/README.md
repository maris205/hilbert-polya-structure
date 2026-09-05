# Paper artifacts

`main.tex` defaults to Round 2. The three tiny round wrappers choose distinct
conditional theorem content. Round 0 contains the complete orbit atlas;
Round 1 adds determinant and correction; Round 2 adds diffusion, relaxation
and independent evidence. All rounds have bilingual abstracts and six
keywords in each language.

The release command builds each round twice in independent temporary
directories, with two LuaLaTeX passes and epoch 1788566400. The final PDF is
byte-identical to Round 2. Settled logs are retained in `compile_roundN.txt`.
`COMPILE_REPORT.md` records the actual output audit.
