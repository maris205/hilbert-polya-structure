# Paper artifacts

`main.tex` contains three conditional, substantive revisions selected by
`\CRevisionRound`:

- `0`: exact flow, stable actions, and core regime theorem;
- `1`: adds the complete critical/zero-field/zero-axial/free/sign-reversal
  boundary audit;
- `2`: adds active-mode closure, minimal periods, strobe fixed spaces,
  quantitative evidence, the quantization nonclaim, and claim-local formal
  source citations with an explicit no-proof-outsourcing boundary.

The archived outputs are `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; `main.pdf` is byte-identical to round 2.

Each round was built twice in a fresh temporary directory, with two LuaLaTeX
passes per build and environment

```text
SOURCE_DATE_EPOCH=1788220800
FORCE_SOURCE_DATE=1
TZ=UTC
```

The paired PDFs are byte-identical for every round.  All settled logs are
warning-free, and every final-PDF font is embedded and subset.  Exact hashes,
page counts, sizes, and audit commands appear in `COMPILE_REPORT.md`.
