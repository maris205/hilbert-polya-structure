# Exact theorem package — HCS-C282

## 1. Frozen model

Let

`U_t=u+c t-sum_{i=1}^{N_t}Y_i`,

where `u>=0`, `c>0`, `N` is Poisson with rate `nu>=0`, and the independent
claims are iid `Exp(beta)` with `beta>0`.  Ruin and deficit are

`tau=inf{t>=0:U_t<0}`, `D=-U_tau` on `{tau<infinity}`.

Strict passage matters at `u=0`: the initial state is not ruined.  The owner
used for Route A is the killed Markov process

`X_t=U_t` for `t<tau`, and `X_t=Delta` for `t>=tau`.

The transform below remains a first-passage functional of the underlying
surplus `U`.  The owner does not include `c=0`, investment, diffusion, claim
dependence, control, finite-horizon inversion, or empirical solvency
calibration.

## 2. Joint transform theorem

For `q,s>=0`, define

`Phi_{q,s}(u)=E_u[e^{-q tau-sD};tau<infinity]`.

Let

`r_q=(c beta-nu-q+sqrt((c beta-nu-q)^2+4c beta q))/(2c)`.

Then `0<=r_q<=beta` and

`Phi_{q,s}(u)=(beta-r_q)/(beta+s) exp(-r_q u)`.

When `nu=0`, the selected root is `beta` and the transform is zero, as it must
be.  For `nu>0`, it is strictly below `beta`.

### Proof

The generator/first-jump equation on `u>0` is

`c Phi'(u)-(nu+q)Phi(u)
 +nu int_0^u Phi(u-y) beta e^{-beta y}dy
 +nu int_u^infinity e^{-s(y-u)} beta e^{-beta y}dy=0`.

The last term is `nu beta e^{-beta u}/(beta+s)`.  Set

`J(u)=int_0^u Phi(u-y) beta e^{-beta y}dy`.

Then the renewal equation is equivalent to

`c Phi'=(nu+q)Phi-nu J-nu beta e^{-beta u}/(beta+s)`,

`J'=beta(Phi-J)`, `J(0)=0`.

This is a two-dimensional inhomogeneous linear system.  Its homogeneous
mode `e^{-r u}` exists exactly when

`c r^2-(c beta-nu-q)r-q beta=0`.

Thus the two quadratic-root modes exhaust its homogeneous solution space,
with a generalized mode at the critical double root.  The forcing particular
solution is `(Phi,J)=(0,-beta e^{-beta u}/(beta+s))`.  For `q>0`, the two
roots have opposite signs, so boundedness removes the growing mode and
retains the positive root displayed above.  At `q=0` with `0<nu<c beta`,
however, both
`0` and `R=beta-nu/c` give bounded nonnegative local solutions.  The required
probability boundary selects `R`: for
`Z_t=sum_{i<=N_t}Y_i-c t`, the strong law gives
`Z_t/t -> nu/beta-c<0`, hence `M=sup_{t>=0}Z_t<infinity` almost surely and
`Phi_{0,s}(u)<=P(M>u)->0` as `u->infinity`; this removes the constant mode.
When `nu>c beta`, boundedness removes the negative-root mode and retains zero.
At equality it removes the linearly growing generalized mode.  For the
surviving mode,

`J=A beta e^{-r u}/(beta-r)-beta e^{-beta u}/(beta+s)`,

so `J(0)=0` forces `A=(beta-r_q)/(beta+s)`.  Mode exhaustion, this initial
condition, and the chamber boundary together prove uniqueness.

If `nu=0`, there are no claims and the transform is identically zero; this is
the displayed formula with `r_q=beta`.  Coupling all reserves to the same
compound-Poisson path and using continuity of the exponential claim law
extends the `u>0` derivation to `u=0` without changing strict passage.

## 3. Overshoot theorem

The transform factors as

`Phi_{q,s}(u)=[beta/(beta+s)] Phi_{q,0}(u)`.

Therefore, when `nu>0`, conditional on ruin, `D~Exp(beta)` and `D` is
independent of `tau`.
This also follows pathwise: conditional on a claim exceeding the pre-ruin
reserve, its excess is fresh exponential by memorylessness.  In every
nontrivial ruin chamber, `E[D|ruin]=1/beta`.

## 4. Complete loading atlas

Put `rho=nu/(c beta)`.

### Profitable chamber: `0<rho<1`

The zero-discount root is

`R=beta-nu/c>0`,

and

`P_u(tau<infinity)=rho e^{-Ru}`.

Differentiating `Phi_{q,0}` at `q=0` gives

`E_u[tau | tau<infinity]=(1+nu u/c)/(c beta-nu)`.

### Critical chamber: `rho=1`

The zero-discount root is zero, so ruin is certain.  Moreover

`r_q~sqrt(beta q/c)` as `q downarrow 0`.

The right derivative of the ruin-time Laplace transform is therefore
`-infinity`, and `E_u[tau]=infinity` for every `u>=0`.

### Adverse chamber: `rho>1`

Again the zero-discount root is zero and ruin is certain.  This time the root
is differentiable, yielding

`E_u[tau]=(beta u+1)/(nu-c beta)`.

### No-claim face

If `nu=0`, the reserve increases deterministically and ruin is impossible.
Conditional ruin quantities are undefined, not zero.  The `u=0` face is
already covered by all formulas.

## 5. Adjustment martingale and supremum

In the profitable chamber let `Z_t=sum Y_i-c t`.  Since

`nu(beta/(beta-R)-1)-cR=0`,

`exp(R Z_t)` is a mean-one martingale.  Let `M=sup_{t>=0}Z_t`.  Ruin from
reserve `u` is exactly `{M>u}`, hence

`P(M>u)=rho e^{-Ru}`, `u>=0`.

Thus `M` has atom `1-rho` at zero and density `rho R e^{-Rx}` for `x>0`.
This dual workload statement is an exact source corollary, not a target
spectral bridge.

## 6. Executable certificate

The canonical receipt has 36 exact regime rows, 448 high-precision joint
transform rows, 144 conditional-first-mean rows, 12 adjustment-martingale
rows, and six boundary rows.  The producer-independent checker passes
**4,487** assertions, SymPy passes 15 identities, replay is
byte-exact, and 26/26 hostile mutations
are rejected.  These are regression gates, not a finite proof of the theorem.

## 7. Route-A verdict

The tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

The process has no arithmetic origin.  The killed PDMP/Markov semigroup has no
intrinsic deterministic, enumerable primitive-periodic-orbit owner.  Neither
Poisson claim times nor the adjustment root supplies rational-prime labels, a
logarithmic prime clock, a target determinant, or a target divisor.
The source result is therefore `ROUTE_A_REJECTED`; Route B is not authorized.
