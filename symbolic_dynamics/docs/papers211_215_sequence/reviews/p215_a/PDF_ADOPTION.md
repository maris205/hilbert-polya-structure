# P215 Review A PDF adoption

2026-09-11 UTC. Before adoption, live `main.pdf` and physical Round0 PDF were
whole-raw equal: 200,910 bytes, SHA256
`68b00073dda65e211dfb1ff518729df81b5631b0a75301b37cf6d7465e9f6784`.
The absent preservation target was created with `cp --no-clobber` as
`reviews/p215_a/original_main.pdf` and compared whole-raw to Round0.

Only the accepted A build01 PDF was then copied to the live PDF path and
compared whole-raw. Current live PDF is 200,921 bytes, SHA256
`ff04cdb46b6072398119a962a9038303d3665222da048c8eb14a103105d55f85`.
All six pages were actually viewed and complete artifact DATA was accepted.

No TeX/Bib/scientific source changed. Frozen Round0 and old live PDF remain
preserved. This is artifact adoption, not Round1, Review B or paper completion.
