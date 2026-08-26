# HCS-C173: positive Lyness five-cycle obstruction

This package gives a complete obstruction/progress paper for

\[
F(x,y)=\left(y,\frac{1+y}{x}\right)
\quad\text{on}\quad (0,\infty)^2.
\]

The global identity (F^5=I) yields one fixed point and exact period five
everywhere else.  Therefore (\operatorname{Fix}(F^5)) is the whole
positive quadrant, so the classical Artin--Mazur zeta is not defined.  The
natural invariant-measure Koopman operator is unitary of order five, but all
five eigenspaces are infinite-dimensional; it is noncompact, not in any
finite Schatten class, not self-adjoint, and has no ordinary trace-class
Fredholm determinant.

Route-A verdict:

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`;
overall `ROUTE_A_REJECTED`; Route B remains unauthorized.

## Reproduce

```bash
python3 code/c173_lyness_producer.py
python3 code/c173_lyness_checker.py
python3 code/c173_sympy_crosscheck.py
python3 code/c173_replay.py
python3 code/c173_mutation.py
python3 code/c173_release_manifest.py
```

The paper is `paper/main.pdf`.  The package contains 27 payload files plus
the self-excluded content-addressed release manifest.  The scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
