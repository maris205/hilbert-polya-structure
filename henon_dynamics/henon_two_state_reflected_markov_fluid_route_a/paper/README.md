# Manuscript build

`main.tex` is the source for three conditional revisions.  The release script injects `\CRevisionRound=0,1,2`, performs two fresh LuaLaTeX builds per round under the fixed epoch, checks settled logs, fonts, text, rasterization, and stores round 2 byte-for-byte as `main.pdf`.
