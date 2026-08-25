# C141 narrative report

## What changed

C141 opens a new gate in the series: a single nonlinear complex polynomial now owns the inverse branches, all periodic points, a nuclear Hardy operator, and stability-weighted traces. Earlier finite polynomial matrices supplied only truncations; real Chebyshev models supplied counts; Möbius--Bergman packages supplied word-matrix traces. Here the exact all-period theorem is intrinsic to \(F(z)=z^2-6\).

The key design choice is the weight ladder. At \(m=0\), every trace is only \(2^n\). At \(m=1\), every trace vanishes. The first nontrivial member is \(m=2\), whose trace contains \(1/[\Lambda(\Lambda-1)]\). This makes the progress mathematically explicit without importing any target data.

## Exact progress

- two globally holomorphic, strongly separated inverse branches on \(\mathbb D_4\);
- an explicit trace-norm bound \(1/(4-\sqrt{10})\);
- all-period exhaustion and exact primitive counts;
- an all-order weighted trace formula;
- exact traces and determinant coefficients through period/degree six;
- a primitive product whose inner index begins at \(k=2\), with absolute convergence proved for \(|u|<4\).

## Boundary

The determinant is entire because the operator is trace class. That fact does not extend the displayed raw primitive product beyond its proved disk. C141 provides no target divisor, no arithmetic/local factor, no global target comparison, and no natural quantization. The result is therefore deliberately graded `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.
