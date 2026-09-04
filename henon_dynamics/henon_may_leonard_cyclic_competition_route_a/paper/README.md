# Paper build: HCS-C358

`main.tex` is one conditional source with revision selector
`\CRevisionRound`.  The retained products are:

- `main_round0_original.pdf`: invariant and subcritical coexistence;
- `main_round1.pdf`: critical normalization, foliation, phase and period;
- `main_round2.pdf`: supercritical diagonal exception, full heteroclinic
  exhaustion, evidence and Route-A boundary;
- `main.pdf`: byte-identical copy of Round 2.

The release gate builds every round twice in fresh temporary directories with
two LuaLaTeX passes, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`,
and `TZ=UTC`.  It rejects unsettled warnings, stale or nondeterministic bytes,
unembedded fonts, dirty extracted text, failed page rasterization, and an
implausibly small manuscript.
