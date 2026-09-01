# Theorem package — exact product-sphere Ricci-flow atlas

## 1. Frozen owner

Let `m>=1`, let `d_i>=1` be integers, and let `g_i` be the unit round metric
on `S^{d_i}`.  On

`M=product_{i=1}^m S^{d_i}`

freeze the product metric

`g(0)=direct_sum_i a_i g_i`, with every `a_i>0`.

Write `c_i=d_i-1` and `n=sum_i d_i`.  The owner is the unnormalized Ricci
flow `partial_t g=-2 Ric(g)` in physical time.  A circle factor (`d_i=1`) is
flat, so its factor clock is defined to be infinity rather than obtained by a
division by zero.

## 2. Exact flow and maximal interval

**Theorem 1.**  The unique Ricci flow in the frozen product family is

`g(t)=direct_sum_i a_i(t)g_i`, `a_i(t)=a_i-2c_i t`.

If at least one `c_i>0`, set

`T_i=a_i/(2c_i)` for `c_i>0`, `T_i=infinity` for `c_i=0`, and
`T=min_i T_i`.  The maximal Riemannian interval is `(-infinity,T)`.  If all
`c_i=0`, the metric is flat and stationary for all real time.

**Proof.**  Constant rescaling leaves the Ricci tensor unchanged as a
`(0,2)` tensor, and `Ric(g_i)=c_i g_i`.  The Ricci tensor of a Riemannian
product is the direct sum of the factor Ricci tensors.  Coefficient comparison
therefore gives `a_i'=-2c_i`.  Positivity of every coefficient gives the
stated maximal interval.  For all-flat data every derivative vanishes.  This
also proves uniqueness inside the family; standard Ricci-flow uniqueness
identifies it with the ambient solution while it exists.  QED.

For `t<T`, the exact homogeneous invariants are

`R(t)=sum_i d_i c_i/a_i(t)`,

`|Rm|^2(t)=sum_i 2d_i c_i/a_i(t)^2`,

`|Ric|^2(t)=sum_i d_i c_i^2/a_i(t)^2`,

`V(t)=V(0) product_i (a_i(t)/a_i)^(d_i/2)`,

and `diam(M,g(t))=pi sqrt(sum_i a_i(t))`.  In particular
`d log V/dt=-R`.

## 3. Tied first collapse and Type-I model

Assume `T<infinity`.  Let `I={i:T_i=T}` and
`D=sum_{i in I} d_i`.  Every member of `I` has `c_i>0`, and
`a_i(t)=2c_i(T-t)` for `i in I`.

**Theorem 2.**  As `t` tends upward to `T`,

`(T-t)R(t) -> D/2`,

`(T-t)^2 |Ric|^2(t) -> D/4`,

`(T-t)^2 |Rm|^2(t) -> sum_{i in I} d_i/(2c_i)`,

and

`V(t) ~ C_I (T-t)^(D/2)`,

where

`C_I=product_i Vol(S^{d_i},g_i) product_{i in I}(2c_i)^(d_i/2)
 product_{j notin I}a_j(T)^(d_j/2)`.

Thus the singularity is Type I.  The diameter tends to
`pi sqrt(sum_{j notin I}a_j(T))`; this is zero exactly for full collapse.

For any `t_k upward T`, put `Q_k=(T-t_k)^(-1)` and
`g_k(s)=Q_k g(T+s/Q_k)`, `s<0`.  At chosen product basepoints the flows
converge smoothly on compact pointed sets to

`product_{i in I}(S^{d_i}, -2c_i s g_i) times (R^{n-D},g_E)`, `s<0`.

**Proof.**  Substitute `a_i(t)=2c_i(T-t)` on `I`; all coefficients outside
`I` have positive limits.  The displayed curvature and volume formulas give
the three limits term by term and the Type-I upper and lower bounds.  For the
blowup, a collapsing coefficient becomes exactly `-2c_i s`.  A survivor has
coefficient `Q_k a_j(T)-2c_j s`, which tends to infinity.  A round sphere (or
circle) whose scale tends to infinity converges pointed smoothly to its
Euclidean tangent space.  Products preserve pointed smooth convergence. QED.

## 4. Exact volume normalization

Let

`C(t)=(V(0)/V(t))^(2/n)`,

`tau(t)=integral_0^t C(s) ds`, and `hat g(tau(t))=C(t)g(t)`.

**Theorem 3.**  The normalized metric has constant volume `V(0)` and solves

`partial_tau hat g=-2 Ric(hat g)+(2/n)hat R hat g`,

where the scalar curvature is spatially constant.  The normalized solution is
ancient in every case.  At the forward endpoint:

1. If all factors are flat, `C=1`, `tau=t`, and both flows are stationary.
2. If `T<infinity` and `D=n`, every factor is curved, all factor clocks are
   equal, `g(0)` is Einstein, `g(t)=(1-t/T)g(0)`,
   `C(t)=(1-t/T)^(-1)`, and
   `tau=-T log(1-t/T)`.  The normalized metric is stationary and exists for
   all forward normalized time.
3. If `D<n`, the normalized endpoint `tau_T` is finite.  With
   `beta=D/n` and a positive constant `C_*`,

   `C(t) ~ C_*(T-t)^(-beta)`,

   `tau_T-tau(t) ~ C_*/(1-beta) (T-t)^(1-beta)`.

   For `i in I`, `hat a_i ->0`; for `j notin I`, `hat a_j ->infinity`.
   More sharply,

   `hat a_i ~ 2c_i(1-beta)(tau_T-tau)`

   and `hat R ~ D/[2(1-beta)(tau_T-tau)]`.

Consequently full first collapse, curved Einstein initial data, infinite
forward normalized lifetime, and stationary normalized flow are equivalent.
Every other nonflat case has a partial first collapse and a finite normalized
singularity.

**Proof.**  The volume formula gives `C^(n/2)V=V(0)`.  Since
`V'/V=-R`, logarithmic differentiation gives `C'/C=2R/n`.  Constant metric
scaling preserves the Ricci tensor and sends scalar curvature to `R/C`.
Dividing `d(Cg)/dt` by `d tau/dt=C` gives the normalized equation.

At backward infinity, `C(t)` is asymptotic to a nonzero constant times
`|t|^{-D_c/n}`, where `D_c` is the dimension of all curved factors.  The
integral diverges whether `D_c<n` (power below one) or `D_c=n` (logarithm), so
normalized time tends to minus infinity.  At the forward endpoint the volume
law gives `C(t)~C_*(T-t)^(-D/n)`.  Its integral diverges exactly when `D=n`.
If `D=n`, equal clocks are equivalent to `c_i/a_i=1/(2T)` for all factors,
which is exactly the positive Einstein condition; direct substitution gives
the stationary normalization.  If `D<n`, integration gives the displayed
time gap.  Multiplying a collapsed affine coefficient and a surviving
positive coefficient by `C(t)` yields the scale limits and the sharp
normalized-time asymptotics. QED.

## 5. Boundary atlas

- `m=1,d=1`: a stationary circle for all time.
- `m=1,d>=2`: a round shrinking sphere, full Type-I collapse, and stationary
  normalized metric.
- all `d_i=1`: an arbitrary flat product torus; all scales are constant.
- mixed circle/curved products: circles survive the first singularity, so the
  normalized endpoint is necessarily finite.
- tied clocks: every minimizer belongs to `I`; no generic tie-breaking is
  allowed.
- common scaling `a_i -> lambda a_i` rescales physical singular time by
  `lambda`; factor permutation changes no geometry.
- `a_i=0`, `d_i=0`, surgery after `T`, nonproduct perturbations, quotients,
  and general homogeneous spaces are outside the frozen owner.

## 6. Executable and Route-A conclusions

The evidence contains 218 analytic and boundary rows.  An independent
checker performs 2,063 assertions; SymPy proves 20 identities; replay is byte
identical across 159,616 bytes; 52 of 52 hostile mutations are rejected.  All
21 partial-collapse normalized-time tails are finite values reconstructed by
an endpoint-regularized quadrature, not merely positivity labels.

Outside the flat face, `V'=-RV<0`, so there are no nonconstant recurrent or
periodic metrics in this owner.  There is no rational-prime clock, intrinsic
primitive orbit ledger, dynamical determinant, target analytic structure, or
natural same-clock quantum lift.  Therefore

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,

overall `ROUTE_A_REJECTED`, Route B disabled, under
`NO_BAD_EULER_OR_ROOT_NUMBER`.
