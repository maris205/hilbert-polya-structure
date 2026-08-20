# C78 compile report

Two isolated clean `latexmk -pdf -gg` builds were run with
`SOURCE_DATE_EPOCH=0` and `FORCE_SOURCE_DATE=1`.

```text
build 1 SHA-256: 2d0e0e553f3a2a6335822916505e0bde14eb225b0172dfc3522a64cb96ed0571
build 2 SHA-256: 2d0e0e553f3a2a6335822916505e0bde14eb225b0172dfc3522a64cb96ed0571
byte-identical:  yes
pages:           2
PDF size:        361752 bytes
final-log undefined references/citations: none
final-log overfull/underfull boxes: none
font embedding:  all fonts embedded
visual inspection: pages 1 and 2 passed
```

The extracted PDF text contains no `??`, `[VERIFY]`, `TODO`, or `FIXME`
markers.  The canonical C78 evidence SHA-256 is
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.

The C78 prefreeze manifest is generated after this final file set is sealed;
it excludes itself and transient build files.
