# Paper build — C125

Run from this directory:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The fixed trailer ID, omitted PDF dates, fixed environment, and embedded
Latin Modern fonts make isolated builds deterministic.  The files
`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` use the
standard release-snapshot names and are synchronized byte-for-byte with the
final source.  The evidence-led revision history is retained in
`../PAPER_IMPROVEMENT_LOG.md`; no snapshot preserves superseded claims.
