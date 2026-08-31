# Theorem package

Let `H` be the self-adjoint operator on the natural domain of multiplication by `n` in `ell^2(Z)`,
`(Hψ)_n=Fnψ_n-J(ψ_{n+1}+ψ_{n-1})`, where `F != 0` and `F,J` are real.

## Main theorem

With `(Fcal ψ)(k)=sum_n ψ_n exp(ink)` and `G(k)=exp[-i(2J/F)sin k]`,
`Fcal H Fcal^{-1}=G^{-1}(-iF d/dk)G`.  Hence `H` has simple pure-point spectrum `F Z` and the complete
orthonormal eigenbasis `phi_m(n)=J_{n-m}(2J/F)`, with eigenvalue `Fm`.  Its propagator is

`U_nm(t)=i^(n-m) exp[-iFt(n+m)/2] J_{n-m}((4J/F)sin(Ft/2))`.

The least positive time with `U(t)=I` is `2pi/|F|`.  From a delta source at zero,
`P(X_t=n)=J_n(z(t))^2`, `E X_t=0`, and
`E X_t^2=z(t)^2/2=8J^2 F^{-2} sin^2(Ft/2)`.

For every `t`, `U(t)` is noncompact and belongs to no finite Schatten class.  For every
`lambda` outside `F Z`, `(H-lambda)^{-1}` belongs to `S_p` exactly when `p>1`; in particular it is compact
and Hilbert–Schmidt but not trace class.

## Proof locks

- Gauge differentiation fixes the sign and gives unitary equivalence to the circle momentum operator.
- Jacobi–Anger plus the Bessel recurrence gives the indexed eigenbasis; gauge unitarity gives completeness.
- Characteristics (equivalently the spectral Bessel addition formula) gives the kernel; its `n=m+1` derivative
  at zero is `+iJ`, fixing the remaining phase convention.
- `U(t)=I` forces `exp(-iFt)=1` by the simple ladder, proving minimality.
- The Bessel characteristic function `J_0(2z sin(q/2))` gives normalization and both moments.
- A unitary maps an orthonormal sequence to an orthonormal sequence, so it is not compact.  Resolvent singular
  values are `|Fm-lambda|^{-1}`, reducing `S_p` membership to the two-sided p-series.

## Boundary atlas

At `J=0`, the basis becomes the site basis and all ladder/return statements remain valid; the delta shell is
frozen.  At `F=0`, `J != 0`, the owner changes to the free lattice: spectrum is the absolutely continuous band
`[-2|J|,2|J|]`, the kernel is `i^(n-m)J_{n-m}(2Jt)`, and no positive full-space identity return exists.
