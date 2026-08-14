# Final integrity report

Date: 2026-08-14

Mode: final verification after two hostile-review rounds

Verdict: **PASS**

## Artifact and reproducibility gates

- required `README.md`, `paper/`, `code/`, `experiments/`, `results/` and
  `notes/`: PASS;
- final LaTeX PDF: PASS, 8 pages, author metadata `Liang Wang`;
- deterministic final PDF equals the round-two manuscript: PASS;
- exact producer, independent checker and 14 unit tests: PASS;
- dependency locks: 8/8; hostile mutations: 17/17 rejected;
- producer core SHA-256:
  `b62e9d6b7c24f19b86762310a3d1ef6c29784b16e71e7d0751ce19c79b11add1`;
- Route-A evaluation: PASS with the inherited physical-subsystem-only A2
  scope firewall;
- Route B: correctly refused because no operator, domain or completed full
  Galois-weighted determinant exists.

## High-impact claim verification

| Claim | Evidence | Verdict |
|---|---|---|
| primitive H6 cycles through period five | independent DFS and producer product enumeration | VERIFIED |
| width-three incidence relation | exact integer block vectors | VERIFIED |
| period-four-a trace and excess | radical calculation and reciprocal multiplier polynomial | VERIFIED |
| physical period-five branch | Sturm root count, derivative monotonicity and exact sign word | VERIFIED |
| period-five Galois excess is strictly larger than the period-four-a excess | six rational trace isolators and exact monotone bounds | VERIFIED |
| no width-at-most-three local excess potential | failed periodic-sum identity on the exact incidence relation | VERIFIED |
| finite witness is sharp at width four | unimodular selected minor and nonnegative interpolation | VERIFIED |
| one-sided Hölder necessary condition | cylinder approximation plus periodic incidence cancellation | VERIFIED |
| unrestricted/two-sided Hölder realization remains open | explicit scope firewall and missing future-dependent reduction | VERIFIED |

## Reference and citation audit

All seven bibliography entries are cited and every citation key resolves.
The external records were checked against the official
[MathNet Livshits record](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=2373&wshow=paper),
[Springer Bowen record](https://doi.org/10.1007/BFb0081279),
[NUMDAM Parry--Pollicott volume](https://numdam.org/issues/AST_1990__187-188__1_0/)
and [H\'enon DOI record](https://doi.org/10.1007/BF01608556).
The three internal Wang packages are present locally, and all eight consumed
artifacts are hash-locked.  Ghost citations: 0/7.

## Data and internal-consistency audit

- every displayed finite value is recoverable from
  `results/c55_certificate.json` and independently reconstructed;
- the producer and checker agree on the symbolic relation, exact trace and
  multiplier polynomials, physical root, excess inequality and interpolation
  determinant;
- manuscript, README, proof package, results and evaluators use the same five
  cycles and forward-block convention;
- the computation is a proof certificate, not an empirical extrapolation to
  all periods;
- PDF metadata, embedded fonts, text extraction and rasterized pages 1, 4, 7
  and 8 pass; no undefined references, box warnings, clipping or blank pages
  remain.

## Originality screen

Twenty characteristic claim-level phrases, with at least one from every
major manuscript section, were searched on the public web on 2026-08-14.
No substantive close or verbatim match to the new incidence obstruction,
period-five certificate or finite-sharpness result was found.  P31, P48 and
P54 are cited wherever their objects are reused.  This is a heuristic
public-web screen, not a substitute for a commercial plagiarism database.

## AI research failure modes

All seven protocol modes are `CLEAR` at the stated scope; the detailed
justification is in `FAILURE_MODE_AUDIT.md`.  In particular, hostile review
caught and repaired an under-certified physical period-five branch and an
invalid transfer from a one-sided block metric to arbitrary two-sided Hölder
data.  Neither issue was recast as positive evidence.

## Claim firewall

P55 proves an exact obstruction to locally constant excess potentials of
width at most three, plus a one-sided quantitative necessary condition for
Hölder realizability.  The five-orbit witness is interpolable at width four,
so no general Hölder no-go follows.  No rational-prime trace, completed
Galois-weighted determinant, self-adjoint operator, Hilbert--Polya
realization or proof of the Riemann hypothesis is claimed.
