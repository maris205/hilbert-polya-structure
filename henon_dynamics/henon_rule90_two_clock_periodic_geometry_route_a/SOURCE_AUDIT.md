# C145 source audit

## Source lock

The only mathematical input is the Rule-90 update

```text
u_i -> u_(i-1)+u_(i+1) mod 2
```

on a labeled cyclic lattice.  The polynomial formula, kernel dimension,
Möbius inversion, torus interpretation, and all finite witnesses are derived
inside the package.  The manuscript has no external bibliography and makes no
priority claim.

## Independent paths

- Producer: integer-bit representation of polynomials over `F_2` and Euclidean
  gcd arithmetic.
- Checker: binary matrices, exponentiation, Gaussian rank, and selected direct
  state enumeration; it imports no producer code.
- SymPy: `Poly(..., modulus=2)` gcds for all 576 table cells and a separate
  squarefreeness audit.

## Evidence boundary

The formula is proved for all positive `L,n`.  The search statements are
explicitly bounded: the full positive and nondegenerate minima are within
`1<=L,n<=24` and `2<=L,n<=24`, respectively.  No infinite-volume or
thermodynamic limit is asserted.

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No external prime or target-zero
table, arithmetic/local factor, root number, automorphy claim, Hilbert--Polya
operator, or Route-B input is used.
