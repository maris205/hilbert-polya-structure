# HCS-C27 validation report

## Status

`PASS` for the declared fixed-prime and finite-scan claims.

The independent checker imports neither `c27_producer.py` nor its matrix
helpers. It replays the source matrices with a standard-library tuple engine,
Bareiss integer determinants, separate modular elimination, exact Thomas
invariants, and exact `(1,G_p)` arithmetic.

## Independent gates

All 8 gates pass:

1. source hashes;
2. chronology and symplectic forms;
3. small-prime Thomas invariants;
4. all six local-polynomial hashes and full coefficient arrays;
5. the 328/248 power census and the p=83/p=89 late-separation controls;
6. the complete p=43 finite-Weil fibre-polynomial collision;
7. the C24 integral symplectic conjugacy;
8. 150 distinct branch signatures.

## Theorem versus computation

- **Theorem:** fixed-p trace class and joint Fredholm holomorphy, by a finite
  tensor extension of the C26 scalar theorem.
- **Theorem:** Thomas character formula and good-prime Legendre reduction.
- **Theorem:** P076/P082 all-prime/all-power class-function collapse, by
  explicit integral symplectic conjugacy.
- **Theorem from a complete finite-group period:** p=43 equality of the
  finite-fibre polynomials for all repetitions.
- **Exact finite computation:** p ≤ 97, r ≤ 24 power census, first
  differences r=41 at p=83 and r=30 at p=89, and the
  bridge-length-at-most-12 arithmetic scan.

The p=43 result does not identify the full AGY periodic atom. The 150-branch
scan is not promoted to an all-length statement.

## Precision

All decisions are made by integer, rational, or finite-field arithmetic. No
tolerance, floating-point Gauss phase, numerical eigenvalue, prime fit, or
Riemann-zero data enters a gate.
