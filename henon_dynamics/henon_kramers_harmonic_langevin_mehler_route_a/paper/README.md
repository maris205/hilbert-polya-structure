# C237 manuscript

`main.tex` is the two-round revised theorem paper.  `main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are built in clean directories with
two LuaLaTeX passes per round and fixed `SOURCE_DATE_EPOCH=1787875200`;
`main.pdf` is a byte copy of round 2.  `COMPILE_REPORT.md` records engines,
hashes, logs, font checks, and warning scans.  The critical-damping sentence
is intentionally phrased as a spectral-abscissa/asymptotic-exponent result
because of the explicit Jordan factor $t e^{-\omega t}$.
