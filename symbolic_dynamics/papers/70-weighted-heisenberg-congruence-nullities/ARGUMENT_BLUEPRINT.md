# Argument blueprint

```text
normal congruence kernel
    -> fixed configurations are functions on Q_ell
    -> weighted local rule is right convolution T
    -> extend scalars without changing nullity

finite Heisenberg representation theory
    -> construct every module over algebraic closure of F_p
    -> distinct clock eigenlines plus cyclic shift prove irreducibility
    -> squared-degree ledger proves cross-characteristic completeness
    -> ell^2 one-dimensional blocks
    -> ell-1 nonlinear degree-ell blocks, each repeated ell times

one-dimensional block alpha+beta*u+gamma*v
    -> eliminate v
    -> torsion intersection
    -> D = deg gcd(t^ell-1,(alpha+beta*t)^ell+gamma^ell)

nonlinear block alpha I+beta U+gamma V
    -> only diagonal and full-cycle determinant terms survive
    -> determinant = product_j(alpha+beta*zeta^j)+gamma^ell
    -> determinant = alpha^ell+beta^ell+gamma^ell
    -> cyclic recurrence gives nullity at most one
    -> determinant zero gives nullity exactly one

regular multiplicities
    -> total nullity D + ell(ell-1) * 1_Fermat
    -> projective coefficient phase diagram
    -> unit coefficients give the characteristic-three jump
```

## Convention firewall

The manuscript uses `(Tx)(q)=alpha*x(q)+beta*x(qa)+gamma*x(qb)`. For matrix
coefficients `phi_(lambda,v)(q)=lambda(pi(q)v)`, right translation satisfies
`R_h phi_(lambda,v)=phi_(lambda,pi(h)v)`, so the selected block is exactly
`alpha I+beta pi(a)+gamma pi(b)`. Replacing this by the dual convention sends
each irreducible to its contragredient, permutes the `ell`-torsion character
pairs by inversion, and inverts the nonzero central characters. Both the gcd
count and the common nonlinear nullity are unchanged.

## Failure conditions

- If `p=ell`, the semisimple decomposition is unavailable and the formula is
  not asserted.
- If a coefficient is zero, the recurrence proof needs a separate degenerate
  case split; the selected theorem requires all three coefficients nonzero.
- If an exact published finite-quotient formula is located, the residual claim
  must be narrowed or the paper replaced before external circulation.
