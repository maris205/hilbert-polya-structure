# C134 research question

Can C129's finite-quotient translation sensitivity be upgraded to exact
translation recovery without changing its graph-directed Hénon dynamics,
Hardy space owner, or all-period Fredholm theorem?

## Certified answer

Yes, inside the frozen integer affine family.  Use the labelled universal
character `chi_X(m)=X^m` in `Q[X,X^(-1)]`.  The first three normalized log
jets of the Hardy determinant recover the Laurent monomials

```text
X^t0,  X^(t0+t1),  X^(t0+t1+t2),
```

and their exponent differences recover `(t0,t1,t2)`.  The same injectivity
holds at any known faithful character.  The exact anchor
`q=(3+4i)/5` has infinite order and is computable in Gaussian rationals.

The positive control compares `k=1` with `k=6`.  Their translations are
componentwise equal modulo five, so every C129-style `Z/5` twisted trace and
determinant aliases.  The Laurent and faithful-`q` receipts distinguish them.

The theorem requires a labelled character parameter, exact arithmetic, fixed
`A,B,c`, branch labels, and integer x-translations.  It does not establish
stable inversion from finite precision, arbitrary geometry recovery, target
divisor matching, or Route-B readiness.
