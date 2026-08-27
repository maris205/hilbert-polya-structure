# Build C199 paper

LuaLaTeX builds rounds 0, 1 and 2 by defining `\CRevisionRound`.  A fixed
`SOURCE_DATE_EPOCH` and two fresh final builds must give identical bytes.
`main.pdf` is byte-identical to round 2.  Release checks fonts, text, clean logs
and every rendered page; build sidecars are excluded from the manifest.
