# C74 compile report

Two isolated clean `latexmk -pdf` builds were run with
`SOURCE_DATE_EPOCH=0` and `FORCE_SOURCE_DATE=1`.

```text
build 1 SHA-256: 60c80b5c82b93d1acd2957e7eb25589b521d5f1a9b9de1a4396d396d8c391e15
build 2 SHA-256: 60c80b5c82b93d1acd2957e7eb25589b521d5f1a9b9de1a4396d396d8c391e15
byte-identical:  yes
pages:           2
PDF size:        299362 bytes
final-log undefined references/citations: none
final-log overfull/underfull boxes: none
font embedding:  all fonts embedded
visual inspection: pages 1 and 2 passed
```

First-pass cross-references were resolved by `latexmk`; the final `main.log`
contains no unresolved-reference, citation, or box warning.
