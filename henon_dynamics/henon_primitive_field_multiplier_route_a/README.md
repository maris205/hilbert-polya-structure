# HCS-C172: primitive finite-field multiplier dynamics

For every prime power \(Q\geq2\) and every primitive
\(a\in\mathbb F_Q^\times\), this package proves the complete orbit inventory,
all fixed counts, Artin--Mazur zeta, Koopman spectrum and determinant, inversion
time reversal, and self-adjointness exactly when \(Q\leq3\).

## Explicit progress

- \(0\) fixed plus one nonzero cycle of length \(Q-1\).
- \(\#\mathrm{Fix}(T^n)=Q\) when \(Q-1\mid n\), and \(1\) otherwise.
- \(\zeta_T(z)=((1-z)(1-z^{Q-1}))^{-1}\).
- Natural same-clock unitary Koopman operator with reciprocal determinant.
- Exact inversion reversor and complete self-adjoint boundary.
- Four genericity controls that prevent an arithmetic or target overclaim.

Read the [proof package](THEOREM_PACKAGE.md), the exact
[results](results/RESULTS.md), and the [compiled paper](paper/main.pdf).

Route-A verdict:
`(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.
The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
