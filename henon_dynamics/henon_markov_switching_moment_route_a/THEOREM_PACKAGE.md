# Theorem and boundary package — C117

## Proposition 1 — exact finite moment owners

Let `P_ij` be the probability of `i -> j`, and apply `F_j` after that
transition.  With `B_j=DF_j(0,0)`, the block rule

```text
(A_1)_[j,i] = P_ij B_j
```

defines the exact evolution of unnormalised environment-conditioned tangent
first moments.  Replacing `B_j` by its action `S_j` on `(x^2,xy,y^2)` gives
the exact symmetric second-moment operator `A_2`.  Their dimensions are four
and six, respectively.  The evidence receipt records their matrices, traces
through power six, and full `det(I-zA_k)` polynomials.

## Proposition 2 — stationary intermittency control

The stationary law is `(3/7,4/7)`.  If `Bbar` is the stationary average of the
Jacobians and `Sbar` the stationary average of their symmetric squares, then

```text
Sbar - Sym^2(Bbar) =
[[27/49, 6/49, 1/147], [0,0,0], [0,0,0]],
```

which has rank one.  Thus averaging before and after the quadratic moment lift
are exactly different in this frozen model.

## Boundary

The propositions concern a common-fixed-point tangent cocycle.  They do not
construct a global nonlinear Markov transfer operator, establish compactness
or nuclearity, enumerate nonlinear random periodic orbits, or support Route B.
