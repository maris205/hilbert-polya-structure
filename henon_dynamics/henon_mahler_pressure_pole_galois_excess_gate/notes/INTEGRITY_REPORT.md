# Final integrity report

Date: 2026-08-14

Mode: final verification

Verdict: **PASS**

## Artifact and reproducibility gates

- required `README.md`, `paper/`, `code/`, `experiments/`, `results/` and
  `notes/`: PASS;
- final LaTeX PDF: PASS, 8 pages, author metadata `Liang Wang`;
- final PDF equals the round-two manuscript: PASS;
- exact producer, independent checker and 10 unit tests: PASS;
- dependency locks: 8/8; exact orbit rows: 3/3; mutations: 12/12;
- Route-A evaluation: PASS with physical-subsystem A2 scope firewall;
- Route B: correctly refused because no operator, domain or completed
  determinant exists.

## High-impact claim verification

| Claim | Evidence | Verdict |
|---|---|---|
| canonical Mahler split and nonnegative excess | reciprocal-pair embedding identity | VERIFIED |
| physical primitive pressure pole | Parry--Pollicott source theorem plus independently checked repetition tail | VERIFIED |
| certified residue interval | frozen pressure interval and monotonic endpoint computation | VERIFIED |
| scalar pressure retuning is impossible | exact period-four and period-one rows | VERIFIED |
| excess-abscissa trichotomy | positive generalized Dirichlet-series argument | VERIFIED |
| full pole under Hölder realization | source-normalized two-parameter theorem, explicitly conditional | VERIFIED AS CONDITIONAL_THEOREM |
| determinant/operator claims remain open | paper firewall, evaluator and hostile reviews | VERIFIED |

## Reference and citation audit

All five bibliography entries are cited and every citation key resolves.
The Parry--Pollicott metadata and exact theorem contexts were checked against
the official NUMDAM PDF.  Hénon's metadata were checked through the DOI
record.  The three internal Wang packages are present locally, and all eight
consumed source artifacts are hash-locked.  Ghost citations: 0/5.

## Data and internal-consistency audit

- every displayed finite value is recoverable from
  `results/c54_certificate.json` and independently checked;
- the producer and checker agree on the three exact Galois-excess rows, the
  residue interval and the finite logarithmic-derivative identities;
- manuscript, README, proof package, results and Route-A record use the same
  \(h_*\) interval, residue, trichotomy and conditional hypothesis;
- the all-period pole comes from the source theorem, not finite-orbit
  extrapolation;
- PDF metadata, embedded fonts, text extraction and rasterized pages 1, 5
  and 8 pass; no undefined references, box warnings, clipping or blank pages
  remain.

## Originality screen

Eight distinctive claim-level phrases spanning the abstract and every major
section were searched on the public web on 2026-08-14.  No substantive close
match to this manuscript was found.  P31, P45 and P53 are cited wherever
their results are reused.  This is a heuristic public-web screen, not a
substitute for a commercial plagiarism database.

## AI research failure modes

All seven protocol modes are `CLEAR` at the stated scope.  The detailed
justification is in `FAILURE_MODE_AUDIT.md`.  In particular, one bad source
hash and one multiprecision-initialization bug were caught, corrected and
retested rather than recast as mathematical evidence.

## Claim firewall

P54 proves a physical pressure-pole germ, a nonnegative Galois-excess
splitting, a scalar-roof obstruction and an excess-abscissa trichotomy.  The
full pole is conditional on an unproved Hölder periodic-sum realization.  No
rational-prime trace, completed Riemann determinant, self-adjoint operator,
Hilbert--Pólya realization or proof of the Riemann hypothesis is claimed.
