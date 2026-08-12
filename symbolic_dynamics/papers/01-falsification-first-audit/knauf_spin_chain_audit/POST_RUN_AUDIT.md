# SD-C06 Post-Run Semantic Audit

Date: 2026-08-12

Status: **PROVED** protocol/code semantics; **NUMERICAL_OBSERVATION** values

This note corrects two interpretations without altering the locked protocol,
raw rows, seeds, cutoffs, or numerical values.

## 1. Random-sign cross-level differences are not cutoff drift

The protocol defines the random sign by the complete key
\((\text{base seed},k,\text{state index})\).  Hence a fixed base seed at
depths \(k=20\) and \(k=22\) produces two distinct deterministic sign fields.
The raw column named `successive_k_drift` is the absolute difference of their
finite sums, but for `random_state_sign` it is **not** the truncation drift of
one fixed observable.

Consequences:

- the reported median 2.09591 is retained as a descriptive cross-level
  re-keyed difference only;
- it is not used as an A2 stability margin;
- a future stability control would need a preregistered sign field whose
  restriction is consistent across all depths.

The symbolic-parity control is depth-coherent.  Its final median
successive-cutoff drift, 0.00130302, is below the Liouville value 0.00436081.
Therefore small finite-depth drift is not selective evidence for Liouville or
for the open signed-convergence statement.

## 2. No compact symbolic limit dynamics is claimed

The computation uses the finite layers \(\{0,1\}^k\) and the recursive
refinement between them.  The natural aggregate state set for this audit is
the finite-support direct union of those layers.  Neither the primary object
nor the experiment defines an autonomous shift on a compact one-sided phase
space, a periodic-orbit map, or a limiting transfer-operator function space.

This reinforces the existing Route-A decision:

- `A0_ANALYTIC_ARITHMETIC_ORIGIN` for the source-proved unsigned arithmetic
  identity;
- `A1_FAIL` because there is no intrinsic primitive-cycle ledger;
- `A2_FAIL / NOT_TESTABLE` because no periodic-orbit Fredholm determinant is
  defined;
- `route_b_invocation_allowed: false`.

No Riemann-zero table was used, and none of these corrections changes a raw
numeric result.
