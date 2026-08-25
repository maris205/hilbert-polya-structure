# C166 source audit

Date: 2026-08-25

Source commit: `4342893ce5e2516924181744bfacc01c12e4959d`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The frozen source is the finite affine map

```text
q=2^r, r>=1, d>=2,
T(x_1,...,x_d)=(x_1+x_2,...,x_(d-1)+x_d,x_d+1) mod q.
```

The exact clock is the iterate `n`.  Fixed points are counted without weights,
the Artin--Mazur convention is
`zeta_T(z)=exp(sum_(n>=1) #Fix(T^n) z^n/n)`, and `U_T` is the finite Koopman
permutation on `ell^2((Z/qZ)^d)` with the same clock.

The initially proposed standalone two-dimensional affine shear was stopped.
For odd modulus it is conjugate to a product rotation; for even dyadic modulus
it is exactly the `d=2` row of the present tower.  C166 therefore freezes the
whole family `d>=2` and claims no dynamical or computational complexity.

Allowed inputs are source integers, binomial coefficients, residues modulo a
power of two, truncated-polynomial identities, and finite permutation data.
No target zero or prime table, target divisor/counting law, arithmetic local
datum, Euler factor, root number, automorphy input, or target operator enters
the package.  The finite ledgers are regression sentinels and do not prove the
all-parameter theorem.

The package is source-locked and uses no training or external dataset.
`route_b_invocation_allowed=false`.
