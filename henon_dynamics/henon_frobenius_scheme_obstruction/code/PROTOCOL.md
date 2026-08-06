# Frozen code protocol

The implementation must follow `../EXPERIMENT_PLAN.md` exactly.

## Programs

- `c12a_producer.py`: exact symbolic identities, formula ledger, joint-action
  control, and period-five collision certificate.
- `c12a_checker.py`: independent finite-field arithmetic and artifact checks;
  it must not import the producer.  It validates the complete JSON/CSV schema,
  frozen input hashes, exact period-five constants, and enumerates the
  reversible control relations directly.
- `test_c12a.py`: unit tests for field laws, frozen irreducibles, equations,
  and expected-fail controls.

## Output schema

The producer writes `results/c12a_certificate.json` and the low-period table
`results/c12a_low_period_counts.csv`.  The checker writes
`results/c12a_independent_check.json`.

All integers are serialized as decimal JSON integers or strings when a
factored expression is intended.  Polynomial coefficient vectors are ordered
from highest to lowest degree.  Every cell records `a,p,r,n`, prime status,
ordinary support count, multiplicity-weighted count when defined, and the
scheme-length convention.

The local-zeta theorem field is explicitly scoped to finite zero-dimensional
fibers.  The positive-dimensional degree-drop cell is a control row, not an
input to that theorem.

## Decision rules

- any exact identity mismatch: `IMPLEMENTATION_FAILURE`;
- any producer/checker mismatch: `INDEPENDENT_CHECK_FAILURE`;
- all identities pass and local factors are finite-permutation factors:
  `C12A_NO_GO_ZERO_DIMENSIONAL_FROBENIUS_COLLAPSE`;
- the period-five polynomial matches the frozen published coefficient vector:
  `C12B_N5_PRIOR_WORK_COLLISION`.
