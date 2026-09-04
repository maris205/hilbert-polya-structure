# Paper build

`main.tex` defaults to revision round 2. A fresh build may select a round with
`\def\CRevisionRound{0|1|2}\input{main.tex}`. Round 0 contains the core theorem and proof, round 1 adds the complete boundary atlas, and round 2 adds executable evidence, source ownership, and scope closure. `main.pdf` must be byte-identical to `main_round2.pdf`.
