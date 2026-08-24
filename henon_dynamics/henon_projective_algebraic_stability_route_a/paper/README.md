# Paper build — C121

Run from this directory:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The fixed trailer ID, omitted PDF dates, fixed environment, and embedded
Latin Modern fonts make isolated builds deterministic.  The files
`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` retain the
standard release-snapshot names.  They are synchronized byte-for-byte with
`main.pdf` because the repository-native route-label correction superseded
obsolete labels in every PDF.  The prose revision trail remains in
`../PAPER_IMPROVEMENT_LOG.md`.
