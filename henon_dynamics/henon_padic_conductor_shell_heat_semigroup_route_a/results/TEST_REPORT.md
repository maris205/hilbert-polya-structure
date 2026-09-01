# Test report

Expected commands and pass sentinels:

```text
C283_PRODUCER_PASS cells=438 dft=36
C283 independent checker: PASS (1507 assertions; ...)
C283_SYMPY_PASS (102 exact checks; ...)
C283 byte replay: PASS
C283 hostile mutation: PASS 17/17
C283_MANIFEST_PASS
```

The release gate additionally requires an exact 27-file payload set, no build
sidecars, three distinct revision PDFs, `main.pdf` equal to round 2, two fresh
byte-identical builds per revision, embedded/subset fonts, expected extracted
text, an accepted page count, fixed provenance locks, and the exact Example
5.1/arXiv:1511.02146 direct-owner boundary.
