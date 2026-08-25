# C165 paper build

The released manuscript is `main.pdf`; `main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` preserve the three content-distinct
internal stages described in `../PAPER_IMPROVEMENT_LOG.md`.

Canonical final build command:

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

The final PDF is built twice from fresh auxiliary state and must be
byte-identical.  `main.pdf` is byte-identical to `main_round2.pdf`.  See
`COMPILE_REPORT.md` for hashes, font, log, page, and visual audits.  Build
auxiliaries are not release artifacts.
