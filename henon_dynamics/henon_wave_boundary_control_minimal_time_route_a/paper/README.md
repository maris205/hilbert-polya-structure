# Paper build

Compile one conditional source with `CRevisionRound=0,1,2` using LuaLaTeX,
`SOURCE_DATE_EPOCH=1788307200`, and the fixed trailer ID.  Retain two
substantive revisions and compare two fresh builds of every round byte for
byte.  `main.pdf` is the final Round 2 PDF.
The release manifest also scans every settled log and checks pages, extracted
text, and embedded/subset fonts for all three rounds.
