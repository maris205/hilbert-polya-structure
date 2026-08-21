# C86 compile report

Two isolated `latexmk -pdf` builds were run with fixed
`SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`.  Their PDFs were byte-identical to each other and to the package
copy.

```text
PDF SHA-256: 544418e44bdf5a22a7a1f416fc4f6367aff6f9320c24986e9de626d0511e4423
pages: 2
paper size: US letter
embedded fonts: PASS (all listed fonts embedded)
undefined references/citations: 0
overfull boxes: 0
first-page visual inspection: PASS
second-page visual inspection: PASS
```
