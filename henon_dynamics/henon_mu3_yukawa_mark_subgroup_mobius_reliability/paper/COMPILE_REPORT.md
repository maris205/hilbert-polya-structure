# C77 compile report

Two isolated clean `latexmk -pdf` builds were run with
`SOURCE_DATE_EPOCH=0` and `FORCE_SOURCE_DATE=1`.

```text
build 1 SHA-256: 0ef4a3a7ef318a85f80bc12351e7e234c452a6c8a3beb3f4e3427dcb153e7e61
build 2 SHA-256: 0ef4a3a7ef318a85f80bc12351e7e234c452a6c8a3beb3f4e3427dcb153e7e61
byte-identical:  yes
pages:           2
PDF size:        345951 bytes
undefined references/citations: none
overfull/underfull boxes: none
font embedding:  all fonts embedded
visual inspection: pages 1 and 2 passed
```

The auxiliary files and compile logs are excluded from the prefreeze
manifest; the source, PDF, report, and metadata are included.
