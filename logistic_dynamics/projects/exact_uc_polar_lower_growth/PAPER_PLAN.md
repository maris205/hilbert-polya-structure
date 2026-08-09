# Paper plan — cancellation-safe lower growth for LOG-0001

## One-sentence contribution

For the unchanged exact-\(U_c\) polar Fredholm determinant, positivity of the
exact signed trace ledger on the safe real axis and one pure-left orbit give a
certified nonzero derivative, an explicit linear maximum-modulus lower bound,
and a qualitative proof that the determinant is transcendental entire.

## Claim--evidence matrix

| Claim | Evidence | Boundary |
|---|---|---|
| \(D_{\rm pol}'(2)>0.0213\). | Absolute convergence of the same signed trace logarithm at \(s=2\), positivity of every real trace denominator, the absolute trace-log bound \(B_2\), and the exact pure-left length-one term. | No signed term is replaced by an absolute-value surrogate in the derivative identity. |
| \(M_D(R)>0.0213(R-2)\) for \(R>2\), hence \(M_D(R)>0.01065R\) for \(R\ge4\). | Cauchy's derivative estimate on the disk centered at \(2\) of radius \(R-2\). | The explicit bound is linear, not exponential. |
| \(D_{\rm pol}\) is transcendental entire. | The trace majorant gives \(D_{\rm pol}(\sigma)\to1\), while the derivative certificate proves nonconstancy. | This does not identify positive or exact order. |
| \(M_D(R)/R^A\to\infty\) for each fixed \(A>0\). | A transcendental entire function has nonzero Taylor coefficients of arbitrarily high degree; Cauchy's coefficient bound transfers each one to maximum modulus. | The argument supplies no uniform coefficient size, exponential rate, divisor lower bound, or \(T\log T\) law. |

## Fixed outline

1. Abstract
2. Frozen determinant and main theorem
3. Signed trace logarithm on the safe real axis
4. Pure-left derivative lower bound
5. Maximum modulus and transcendence
6. Outward interval certificate and reproducibility
7. Limitations and conclusion
8. Proof appendix

## Reproducibility boundary

The analytic proof uses only the inherited exact parameter equation, the
same matching-space determinant, the exact based-word trace formula, and
standard complex analysis.  The numerical certificate evaluates the frozen
algebraic constant and scalar elementary functions with outward Arb
intervals.  It does not evaluate the Fredholm determinant, search for its
zeros, or read prime, Riemann-zero, zeta, xi, or USTC data.
