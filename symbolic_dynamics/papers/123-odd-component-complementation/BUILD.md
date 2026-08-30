# Build record

## Final round-two support freeze

- Build date: 2026-08-30 UTC.
- Pipeline: isolated pdflatex -> bibtex -> pdflatex -> pdflatex.
- Result: **PASS**.
- Final-log warning hits: **0**.
- Errors: **0**.
- Undefined references/citations in final log: **0**.
- Overfull/underfull boxes in final log: **0**.
- Bibliography: **8/8** cited primary/classical sources.
- Review-A repaired PDF: **4 pages**, **281,582 bytes**, A4.
- Current PDF SHA-256: 6c78410d7689a7e5f057413ef5256a26885a86a2b9653e3b2581ede30b46c9c1.
- Round copies: `main_round0_original.pdf` retains SHA-256
  `e7a5138e142ef89402668e4eca4e86ea804672b080bfdcce3fe33f7fa074f68d`;
  `main_round1.pdf` is byte-identical to current `main.pdf`.
- Fonts: all listed fonts embedded; all have Unicode maps.
- Metadata: author/title/subject fields blank; no creation/modification dates; no JavaScript or encryption.
- Visual inspection: all four pages inspected at raster resolution; no clipping, collisions, malformed equations, orphaned headings, or unreadable table entries.

The first LaTeX pass produced the ordinary unresolved-reference diagnostics of a clean auxiliary directory; BibTeX and the two resolving passes discharged them. The final main.log has zero warning hits.

## Verifier freeze

- Command: python3 code/verify_odd_component_complementation.py.
- Canonical comparison: byte-identical.
- Assertions after Review-A strengthening: **203,244**.
- Verifier SHA-256: 952f277e2f6955d51365e670888a1b706af82aedf064cb0c2a57f9063c64890c.
- Canonical-output SHA-256: 735c28b8c8b48c3308741840f1a6f92868a59076f276131ad59a3bfcccdb5c7e.

## Source freeze

- main.tex SHA-256: 15e8193ad8568199aa3b08c13df1e2c61231b6b3ef13ef33fe804c4eb1d3ddb7.
- references.bib SHA-256: 144eb3aacf799c9b9cefc10357cadc9ff3e5e4aa7056d58b3965d94eafdc6804.
- Round-two changes are support-only. `main_round2.pdf`, `main_round1.pdf`,
  and current `main.pdf` are byte-identical at SHA-256
  `6c78410d7689a7e5f057413ef5256a26885a86a2b9653e3b2581ede30b46c9c1`.
- Status: anonymous internal round-2 freeze, `GO_INTERNAL`; novelty, priority,
  and external release **HOLD**.
