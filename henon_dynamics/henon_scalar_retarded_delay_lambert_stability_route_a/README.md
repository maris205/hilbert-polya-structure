# HCS-C210 — scalar retarded delay stability atlas

This package freezes the real retarded equation

\[
  x'(t)=-a x(t)-b x(t-\tau),\qquad a,b,\tau\geq0,
\]

on the history space \(C([-\tau,0];\mathbb C)\).  It closes one complete
source theorem: the Lambert--\(W\) characteristic spectrum, an exact
method-of-steps fundamental solution, eventual compactness of the history
semigroup, root multiplicities, and the full nonnegative-parameter
stability/Hopf boundary.  Zero delay, absent delayed feedback, zero equation,
equal-rate and branch-point boundaries are retained explicitly.

The result is a source-local functional-differential theorem.  It is not a
prime model and does not reinterpret the characteristic determinant as a
target determinant.

## Reproduce

```text
python3 code/c210_delay_producer.py
python3 code/c210_delay_checker.py
python3 code/c210_delay_sympy_crosscheck.py
python3 code/c210_delay_replay.py
python3 code/c210_delay_mutation.py
python3 code/c210_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf), with the exact receipt at
`results/c210_delay_evidence.json`.

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;
overall `ROUTE_A_REJECTED`; Route B is false.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
