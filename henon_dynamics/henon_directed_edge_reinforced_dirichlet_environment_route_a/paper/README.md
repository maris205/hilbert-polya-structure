# Paper build

The single source selects revision rounds 0, 1 and 2 through
`\CRevisionRound`.  Each checked PDF is compiled twice in separate fresh
directories with LuaLaTeX, a fixed trailer ID and epoch.  `main.pdf` is the
exact final-round byte stream.
