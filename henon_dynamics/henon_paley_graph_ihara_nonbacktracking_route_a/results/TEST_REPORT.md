# Test report

- Producer: PASS, 13 fields and canonical payload
  `3e1af8f9bea8744e1611deef28f695b24f0454b1f0be7bce1ffd0a70fdcb861a`.
- Independent checker: PASS, 13,048 exact checks and 156 trace rows.
- SymPy lane: PASS, 692 symbolic/exact checks.
- Isolated byte replay: PASS, 38,668 bytes identical.
- Hostile mutation: PASS, 70/70 repaired-hash/parser mutations rejected;
  optimized producer and checker rejected.
- PDF: PASS, fresh two-build equality for rounds 0/1/2, pages 2/2/3,
  embedded/subset fonts, nonempty rasters, zero warning and extracted-text
  control markers.
- Evidence file SHA-256:
  `1e59fd2b2dafa17e2ee00c3ef20d82b38539e85e708ac8e73c087485cd545c7a`.
- Final PDF SHA-256:
  `286ba44628b8f27df7fd352f11d53514c6388f0bea2b3e4c0818b910c8bed502`.
