# Integrity report

## Scope

Project: `HCS-P57`, one-paper continuation of the H6 pressure/orbit lane.
No other dynamical-system family is introduced.

## Mathematical checks

| Claim | Independent control | Status |
|---|---|---|
| primitive cycles through period seven | direct four-state DFS/rotation quotient | VERIFIED |
| `A6` reflection orbit | six exact recurrence remainders | VERIFIED |
| `A6` cubic trace field | independent chronological resultant, mod-5 witness, three Sturm intervals | VERIFIED |
| `A7/B7` shared field | independent degree-14 resultant, mod-37 witness, fourteen Sturm intervals | VERIFIED |
| physical embeddings | rational coordinate boxes, zero-free coordinate rows, trace-derivative zero counts and trace images | VERIFIED |
| `Delta_5>0` | exact log bracket and integer margin | VERIFIED |
| diagnostic `Delta_5` | two 90-digit implementations | VERIFIED |
| width-five relation | direct cyclic block counters | VERIFIED |
| width-six sharpness | determinants `-1` and `+1` | VERIFIED |
| finite-memory scope | explicit width-six interpolation | VERIFIED |

## Software checks

- primary certificate: PASS;
- independent certificate: PASS;
- unit tests: 15/15;
- mutations rejected: 22/22;
- dependency hashes: 8/8;
- no network, subprocess or external target-data dependency in the
  mathematical scripts;
- `PYTHONDONTWRITEBYTECODE=1` in the runner;
- `git diff --check`: PASS.

## Manuscript checks

- complete author/affiliation metadata;
- 8-page PDF generated;
- references resolved;
- no overfull or underfull boxes;
- no undefined labels or citations;
- first and densest appendix pages visually inspected;
- exact claims distinguish `PROVED`, numerical diagnostics and `OPEN` gates.

## Claim firewall

The maximum claim is a width-at-most-five locally constant obstruction plus
exact period-six/seven trace algebra.  The artifact does not assert failure
of every H\"older potential, a full Galois-weighted determinant, a
rational-prime orbit law, a self-adjoint operator, the Riemann hypothesis or
the Hilbert--P\'olya conjecture.

Route A is `ROUTE_A_EXPLORATORY`; Route B is `ROUTE_B_NOT_TESTABLE`.
