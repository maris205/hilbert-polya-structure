# Assumptions and conventions

- The polynomial is fixed as `f=x^4-x-1` over `Z`; no coefficients are fit.
- For a good prime, `X_p` means the four roots over an algebraic closure of
  `F_p`, with scheme multiplicity absent because the fiber is étale.
- `F_p(alpha)=alpha^p` is called arithmetic Frobenius.  Geometric
  Frobenius is its inverse.  They have the same cycle partition, so every
  partition and determinant statement is convention-independent.
- The permutation operator sends the basis vector at `alpha` to the basis
  vector at `F_p(alpha)`.  Its inverse is the pullback convention; the two
  have the same determinant.
- Chebotarev and Dedekind factorization are invoked in their classical
  unconditional forms.  GRH and effective error bounds are not assumed.
- Formal power-series identities are interpreted at `u=0`; because the
  determinant is polynomial, they also identify the corresponding rational
  function wherever defined.
