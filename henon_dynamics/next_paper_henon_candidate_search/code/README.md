# Reproduction commands

All candidate-generation and validation code is target-blind: it does not read
Riemann-zero ordinates or tune against target prime weights.  Run commands from
the Hénon research root, namely the directory containing
`next_paper_henon_candidate_search/`.

## C02 — projective derivative cocycle

```bash
python next_paper_henon_candidate_search/code/c02_projective_pilot.py
python next_paper_henon_candidate_search/code/c02_projective_check.py
```

The producer writes exact disk constants, memory bounds, and primitive-cycle
monodromy checks to `results/c02_projective/`.  The checker independently
recomputes the exact constants and gate decision.

Frozen conventions: `c02_PROTOCOL.md`.

## C02B — complex signed-root polydisc

```bash
python next_paper_henon_candidate_search/code/c02b_complex_polydisc.py
python next_paper_henon_candidate_search/code/c02b_complex_polydisc_check.py
```

The producer proves exact/dyadic self-mapping margins and contraction bounds
and enumerates cyclic sign chronology through length 12.  The independent
checker recomputes every algebraic and cyclic assertion and samples each
boundary circle as a regression diagnostic; sampling is not used in the
proof.

Frozen conventions: `c02b_complex_polydisc_protocol.md`.

## C02C — effective finite-window pinning and trace identities

```bash
python next_paper_henon_candidate_search/code/c02c_finite_window.py
python next_paper_henon_candidate_search/code/c02c_finite_window_check.py
```

The producer writes complete open/cyclic ledgers, endpoint-boundary probes,
two-coordinate gluing controls, matching/Hill identities and exact
complex-base projective constants to `results/c02c_finite_window/`.  The
checker independently solves the recurrence by complex Newton iteration,
rechecks the worst binary64-conditioned cases at high precision, verifies
complete IDs and rejects truncated or tampered ledgers.  It does not import
the producer.

Frozen conventions: `C02C_FINITE_WINDOW_PROTOCOL.md`.  The first full run's
transparent conditioning erratum is recorded there; raw binary64 global
discrepancies remain in the output alongside high-precision identity checks.

## C03 — exact finite-field census

```bash
python next_paper_henon_candidate_search/code/c03_test_finite_field.py
python next_paper_henon_candidate_search/code/c03_finite_field.py
python next_paper_henon_candidate_search/code/c03_independent_check.py
```

The full deterministic run enumerates all phase points for 54 primes
\(p\le251\), applies both frozen random-control ensembles, and takes about one
minute on the recorded CPU.  The independent checker uses tuple states and
does not import the producer.

Frozen conventions: `c03_PROTOCOL.md`.

## C05 — action, Hill determinant, and Maslov ledger

```bash
python next_paper_henon_candidate_search/code/c05_maslov_pilot.py
python next_paper_henon_candidate_search/code/c05_selfcheck.py
```

The producer reads the immutable certified orbit catalogue, preserves
primitive/repeat order and complex phase, and writes the complete ledger and
finite-section controls to `results/c05_maslov/`.  The self-check verifies the
Hill identity, reversor pairing, gauge covariance, local-symbol Maslov
collapse, and exact zero-action period-four orbit.

## Fast validation without regenerating C03 controls

```bash
python -m py_compile next_paper_henon_candidate_search/code/*.py
python next_paper_henon_candidate_search/code/c02_projective_check.py
python next_paper_henon_candidate_search/code/c02b_complex_polydisc_check.py
python next_paper_henon_candidate_search/code/c02c_finite_window_check.py
python next_paper_henon_candidate_search/code/c03_test_finite_field.py
python next_paper_henon_candidate_search/code/c03_independent_check.py
python next_paper_henon_candidate_search/code/c05_selfcheck.py
```

## Implementation rules retained for the next round

- preserve ordered products and doubled chronological occurrences;
- separate primitive cycles from repetitions;
- use exact arithmetic or outward interval enclosures for theorem constants;
- freeze deterministic seeds and controls before full runs;
- keep producer and independent checker implementations separate;
- distinguish finite-section stability from Route-A A2;
- preserve the signed and absolute flat-trace conventions as distinct
  objects;
- keep the cylinder-memory index distinct from dynamical time;
- freeze C02D's function space, kernel, orientation, norm and target trace
  before any operator finite-section run;
- define \(\mathcal L^{[N]}\) only as a common-space one-step-clock
  finite-memory approximation, never as \(\mathcal L^N\) or an exact block
  recoding;
- require the signed aggregate cylinder error to remain contractive after
  admissible-word growth; single-branch decay is not a pass;
- write any C02D outputs into a new result directory rather than mutating
  C02C.
