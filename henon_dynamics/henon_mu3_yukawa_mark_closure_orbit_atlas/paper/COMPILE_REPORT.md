# C76 compile report

Two isolated clean `latexmk -pdf` builds were run with
`SOURCE_DATE_EPOCH=0` and `FORCE_SOURCE_DATE=1`.

```text
build 1 SHA-256: 2bde79a1b6ac6ac0b7ffa3bf6c2a0af626fba8dc776bf969c49fe32ada82a9ea
build 2 SHA-256: 2bde79a1b6ac6ac0b7ffa3bf6c2a0af626fba8dc776bf969c49fe32ada82a9ea
byte-identical:  yes
pages:           2
PDF size:        316616 bytes
final-log undefined references/citations: none
final-log overfull/underfull boxes: none
font embedding:  all fonts embedded
visual inspection: pages 1 and 2 passed
```

The first draft exposed a duplicate `\Phi` macro definition; removing that
local macro fixed the only compilation error.  The final logs contain no
unresolved-reference, citation, or box warnings, and the extracted PDF text
contains no `[VERIFY]`, `TODO`, or `FIXME` markers.
