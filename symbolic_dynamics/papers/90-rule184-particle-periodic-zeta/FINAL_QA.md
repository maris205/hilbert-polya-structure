# Final QA — P90

Final decision: **internal GO / external HOLD**.
Audit completed: 2026-08-28 UTC.

## Mathematical QA

- [x] Rule-184 orientation and conservation checked directly.
- [x] Particle–hole/reflection conjugacy derived and exhaustively tested.
- [x] Min-plus indexing rederived for arbitrary time.
- [x] Sharp upper bound and every-layer witness verified.
- [x] Alternating two-cycle overlap handled at even half filling.
- [x] Fixed points, exact-period points, and temporal orbits kept distinct.
- [x] Möbius parity correction and particle refinement rederived.
- [x] Zeta identified explicitly as the finite temporal-map zeta.
- [x] Microcanonical limit specifies `n->infinity` and `m/n->rho`.

## Reproducibility QA

- [x] `python3 code/verify_rule184.py` passes **298,283 exact assertions**.
- [x] No random sampling, floating point, or third-party Python package.
- [x] Four-stage LaTeX/BibTeX build succeeds.
- [x] No undefined citation/reference, rerun request, box warning, or other
  LaTeX/package warning remains in `main.log`/`main.blg`.
- [x] All fonts are embedded and subsetted.
- [x] PDF text extraction contains the anonymous Stage 2 marker, scope hold,
  and complete references.
- [x] All five A4 pages were rendered and visually inspected; no clipping,
  collision, missing glyph, or stranded heading was found.

## Artifact QA

- `main.pdf`: 5 pages, 329,610 bytes, PDF 1.5.
- SHA-256:
  `7db799503da50d23f747c1a6f7e1483e7a0316b36e52dd4d91cb9615ca55b964`.
- `SHA256SUMS` covers the manuscript, bibliography, exact control, audit
  documents, README/build record, and PDF.

## Release gate

The proofs and registered controls support internal use. External release is
blocked only by ownership/novelty risk, chiefly the proximity of recent
Rule-184 jam-relaxation work. A broader literature audit and human author
review are required before any posting, submission, or priority claim.
