# C278 paper build

`main.tex` defaults to revision round 2.  Archived revisions are selected by
defining `\CRevisionRound` to 0 or 1 before input.  Each retained PDF is built
twice in two fresh directories, with two LuaLaTeX passes per build, fixed
epoch `1788220800`, UTC, and the fixed trailer ID embedded in the source.
