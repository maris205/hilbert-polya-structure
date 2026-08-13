# Final Integrity Record

Date: 2026-08-14  
Candidate: `pcf_quadratic_prime_multiplier_obstruction_v1`  
Status: **COMPLETE_LOCAL / PASS**

## Scientific outcome

The all-period theorem excludes every rational multiplier whose modulus is a
rational prime at the frozen PCF quadratic. It also excludes every odd
rational exponent-prime base. The exact target `|lambda|=2^n` remains open
for periods `n>=2`, and a nonrational complex multiplier with rational-prime
modulus remains outside the theorem. The cotangent bridge is exact only on
regular branches and opens no global symplectic, determinant, zero, or
quantization claim.

## Independent review chain

- Round 1: `MINOR`, 7.1/10. Required an in-paper exact PCF relation and repair
  of one stale research-manifest hash.
- Response: added
  `0 -> 1 -> -(u-1) -> (u-1) -> (u-1)` and stated that PCF is provenance,
  not a theorem hypothesis; deterministically rebuilt the manifest.
- Round 2: `PASS`, 8.8/10, with no scientific blocker.

## Final artifact checks

- Manuscript source SHA-256:
  `d434e52e797567f33e9e9aac230b120241aa7a4dc05ae19c978f2ee6d4e2bd25`
- Final PDF SHA-256:
  `160e9c6fa12c35f500fbae39d9316fc55e8c9b4f1b044ef3deda6037e0b5b1c3`
- Final independent review SHA-256:
  `bd1d453e4679ed6418b0d40c99885c003860005957a3cf1a4542ae5eeb7982b6`
- Research result manifest SHA-256:
  `85f356dfce1e2257e7482840f1125a279289ccc215d52e1498a9dd0d94f18789`
- Research manifest: 45/45 hashes independently matched in Round 2.
- Tests: 37 passed; zero failures, errors, or skips.
- Build: 11 pages; `pdflatex -> bibtex -> pdflatex -> pdflatex`; no warning,
  undefined citation/reference, overfull, or underfull box; fonts embedded.
- Figures: three vector PDF figures and three 300-dpi review PNGs; all
  caption/data links and visible layouts passed two review rounds.
- Forbidden data: no external prime table, Riemann-zero data, target fit, or
  conditional high-period real-orbit ledger was used.

The historical pre-review PDF and the Round-1 PDF remain preserved. GitHub
synchronization is intentionally deferred to the five-paper batch close so
the existing nested-repository exclusion rule is applied once.
