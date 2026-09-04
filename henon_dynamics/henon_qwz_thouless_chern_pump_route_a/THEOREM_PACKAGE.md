# Theorem package

**Status:** PROVABLE AS STATED. **Scope:** `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Theorem

Let `m` be real and orient the parameter torus by `dk wedge dτ`. Put
\[
d=(\sin k,\sin\tau,m+\cos k+\cos\tau),\qquad H_m=d\cdot\sigma.
\]

1. The eigenvalues are `±|d|`. The family is gapped exactly when `m` is not `-2,0,2`, and its direct gap is
\[
G(m)=2\min\{|m+2|,|m|,|m-2|\}.
\]
2. In a gapped chamber the lower projector
\[
P_-=(I-\widehat d\cdot\sigma)/2
\]
is a smooth rank-one complex line bundle. With
\[
c_1={1\over2\pi i}\int_{\mathbb T^2}
 \operatorname{Tr}\!\left(P_-[\partial_kP_-,\partial_\tau P_-]\right)dk\,d\tau,
\]
its Chern number is
\[
c_1=-\tfrac12\{\operatorname{sgn}(m+2)-2\operatorname{sgn}(m)+\operatorname{sgn}(m-2)\}.
\]
Thus it is `0,-1,+1,0` as `m` crosses the four open chambers from left to right.
3. At increasing `m`, the wall data `(mass,point,chirality,jump)` are
`(-2,(0,0),+1,-1)`, `(0,(pi,0),-1,+1)`, `(0,(0,pi),-1,+1)`, `(2,(pi,pi),+1,-1)`.
4. Let `τ` increase from `0` to `2 pi`, take unit positive particle charge,
   and define positive current by `J=partial_k H`. If the lower band is
   filled, the cycle is traversed adiabatically, and the gap remains open,
   the transported positive-particle charge equals `c1`. With
   `Omega_kτ=i Tr P[partial_k P,partial_τ P]`, the filled-band response is
   `Q=-(2 pi)^-1 integral Omega_kτ=c1` in the frozen orientation. Electron
   charge would add the factor `-e`. This statement is an adiabatic limit; it
   does not claim exact finite-driving-rate quantization.

At `m=-2,0,2` the projector is undefined at the listed zeroes. Reversing the torus orientation or replacing `τ` by `-τ` flips `c1`. Complex conjugation obeys `K H(k,τ)K=H(k,-τ)`. For `|m|>2`, the normalized vector is homotopic through a nonzero field to the appropriate constant pole.

## Proof

Writing `x=cos k`, `y=cos τ` gives
\[
|d|^2=m^2+2+2m(x+y)+2xy.
\]
This is affine in each of `x,y`, so its minimum on the square `[-1,1]^2` occurs at a corner. The four values are `(m+2)^2,m^2,m^2,(m-2)^2`, proving the spectral and gap statements.

Pauli multiplication gives
\[
\operatorname{Tr}(P_-[\partial_kP_-,\partial_\tau P_-])
=-{i\over2}\widehat d\cdot(\partial_k\widehat d\times\partial_\tau\widehat d).
\]
Hence `c1` is minus the degree of `d-hat`. Take the north pole as a regular value. Its possible preimages are the four points with `sin k=sin τ=0`; a point contributes precisely when its Dirac mass `M=m+cos k+cos τ` is positive, and its local degree is `chi=cos k cos τ`. Therefore `deg(d-hat)=sum chi 1_{M>0}`. Using `1_{M>0}=(1+sgn M)/2` and `sum chi=0` gives the displayed signed-mass formula. Equivalently, increasing a Dirac mass through zero changes the lower-band Chern number by `-chi`; summing the four cones gives the chamber atlas. Direct differentiation supplies the audit identity
\[
d\cdot(\partial_kd\times\partial_\tau d)
=\cos k+\cos\tau+m\cos k\cos\tau.
\]
The last assertion is precisely the standard gapped filled-band adiabatic transport theorem in the fixed convention.

## Evidence boundary and Route A

Exact corner, Pauli, degree, and Dirac receipts prove the analytic identities. A separate lattice-gauge calculation is only a regression witness and never upgrades a numerical value into topology. The Chern integer is source-local natural quantization, not a prime carrier. Therefore the tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, and Route B is false.
