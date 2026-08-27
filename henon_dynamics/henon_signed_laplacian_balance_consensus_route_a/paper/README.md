# Build C203 paper

LuaLaTeX builds rounds 0, 1 and 2 by defining `\CRevisionRound`.  The final
fixed-epoch build is repeated from fresh sidecars and must be byte identical;
`main.pdf` equals round 2.  Release audits fonts, extracted text, clean logs and
every rendered page.
