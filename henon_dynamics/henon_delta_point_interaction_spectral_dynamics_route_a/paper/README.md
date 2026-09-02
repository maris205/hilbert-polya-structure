# Paper build

`main.tex` is one conditional source.  `CRevisionRound=0,1,2` retains the
initial derivation and two substantive revisions.  Build with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788307200`; each retained round is compiled twice in two
fresh directories, with two passes per build, and compared byte for byte.
The release manifest performs these six builds itself and checks settled
warnings, every round's page count, embedded/subset fonts, extracted text,
and SHA256.  `main.pdf` is Round 2.
