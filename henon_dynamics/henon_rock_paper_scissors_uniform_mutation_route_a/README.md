# HCS-C235 — rock–paper–scissors with uniform mutation

This package closes one narrowly frozen three-strategy flow on the simplex,
not a general evolutionary-game family:

\[
 \dot x=a x(y-z)+\mu(1/3-x),\qquad\text{cyclically in }(x,y,z),
 \quad a,\mu\geq0,\quad x+y+z=1.
\]

The positive-rate conservative face has the exact product first integral
\(H=xyz\), a single periodic orbit on each regular interior level, a boundary
heteroclinic network, and the stated turning-point period quadrature.  Positive uniform
mutation gives immediate entrance to the interior, a strict product
Lyapunov function, global convergence to \((1/3,1/3,1/3)\), and tangent rates
\(-\mu\pm ia/\sqrt3\).  The \(a=0\) contraction and \(a=\mu=0\) identity
faces are recorded separately.

The release contains 28 physical files (27 payload files plus the
self-excluded manifest).  The evidence and paper are source-local and carry
the literal `NO_BAD_EULER_OR_ROOT_NUMBER`; no prime/zero table, Euler factor,
target determinant, automorphy statement, or Hilbert–Pólya claim is made.

Run the deterministic audit from this directory with:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_rps_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_rps_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_rps_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_rps_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_rps_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c235_release_manifest.py
```

The Route-A tuple is `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and
`route_b_invocation_allowed` is false.  “NEW” in the surrounding registry is
workspace-local only; this package does not certify literature priority.
