# Research question

For the bounded self-adjoint operator on
`ell2(Z) direct_sum C|d>` defined by

```text
(H u)_n = J(u_{n+1}+u_{n-1}) + g u_d delta_{n0},
(H u)_d = epsilon u_d + g u_0,
```

can one give, for all `J>0`, real `epsilon`, and real `g`, a single rigorous
atlas of the full spectral type, every bound state, the impurity spectral
measure, and the exact on-shell reflection/transmission probabilities?

The decisive subquestion is branch control.  Squaring the Schur equation gives
a quartic that can possess additional real roots.  Which roots are genuine
physical-sheet poles, and how can the proof prevent the others from being
promoted to eigenvalues?

A second rigor question is spectral-measure completeness: after computing an
almost-everywhere boundary density, can one use local-uniform Stone inversion,
off-band meromorphy, and explicit edge atom limits to exclude every possible
singular-continuous remainder rather than inferring that conclusion from the
density alone?

The package also asks for the exact degenerate limits `g=0` and `J=0`, the
band-edge cases `epsilon=plus_or_minus 2J`, and the unitary equivalence of the
two coupling signs.  It does not ask for arithmetic data, a target determinant,
target zeros, or a Hilbert--Polya operator.
