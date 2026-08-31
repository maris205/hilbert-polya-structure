# Theorem package

Let `e_n(x)=exp(i n x)` and `D=-i*d/dx` on the circle.  The equation
`u_t+u_xxx=0` has the Fourier solution

\[
U(t)e_n=e^{i n^3t}e_n=e^{itD^3}e_n.
\]

Thus `D^3` is self-adjoint on its Sobolev domain and `U(t)` is a strongly
continuous unitary group on `L^2(T)`.

## Complete revival and sampled-fixed-space theorem

1. `U(t)=I` on all of `L^2(T)` exactly when `t` is in `2*pi*Z`; the mode
   `n=1` proves minimality.
2. If `gcd(p,q)=1`, then

   \[
   U(2\pi p/q)u=\sum_{r=0}^{q-1}A_r\,
   u(\,\cdot+2\pi r/q),\qquad
   A_r={1\over q}\sum_{s=0}^{q-1}
   e^{2\pi i(ps^3-sr)/q}.
   \]

   This follows because `(n+q)^3-n^3` is divisible by `q`, followed by
   finite Fourier inversion.  Parseval gives `sum |A_r|^2=1`.
3. The rational strobe has exact order `q`: an order must annihilate the
   phase of mode one, while the `q`th power annihilates every mode.
4. Its fixed space is the closed span of the modes satisfying `q|n^3`.  If
   `q=product ell^a`, this is equivalent to `L(q)|n`, where
   `L(q)=product ell^ceil(a/3)`.
5. A nonconstant state with finite Fourier support `S` has least continuous
   return `2*pi/gcd{|n|^3:n in S,n!=0}`.  Constants are fixed at every time.
6. If `t/(2*pi)` is irrational, no nonzero Fourier mode can be fixed, so the
   fixed space consists exactly of constants.

Every `U(t)` is noncompact: the images of the Fourier basis remain
orthonormal.  Hence it is not trace class and supplies no infinite-
dimensional Fredholm determinant.  The theorem concerns the periodic linear
Airy equation only, not nonlinear KdV or arbitrary third-order boundary
conditions.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
ROUTE_A_REJECTED; Route B false.
```

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
