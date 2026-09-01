# Theorem package: irreducible network SIS threshold and critical law

## Frozen owner

Let `A` be a nonnegative irreducible `n x n` matrix, `beta>0`, and
`D=diag(delta_1,...,delta_n)` with every `delta_i>0`.  On the cube
`Q=[0,1]^n`, set

\[
 f(x)=\beta\operatorname{diag}(1-x)Ax-Dx,
 \qquad M=\beta A-D.
\]

The clock is physical ODE time.  Reducible contact graphs, zero recovery,
time-dependent rates, stochastic finite-population chains, and reinfection
delays are different owners.

## Main theorem

1. `Q` is forward invariant.  Every solution starting at a nonzero point is
   strictly positive at every positive time.
2. If `s(M)<0`, the disease-free state is globally exponentially stable.  If
   `s(M)=0`, it is globally asymptotically stable.
3. Suppose `s(M)=0`.  Choose Perron vectors `Mv=0`, `w^T M=0`, `v,w>>0`,
   normalized by `w^T v=1`, and put

   \[
   \kappa=\beta w^T\operatorname{diag}(v)Av>0.
   \]

   Then every nonzero solution satisfies

   \[
   t x(t)\longrightarrow \frac{v}{\kappa}.
   \]

4. If `s(M)>0`, there is exactly one equilibrium `x*` in `(0,1)^n`; it
   attracts every nonzero point of `Q`.  Its Jacobian is irreducible Metzler
   Hurwitz.  With `A,D` fixed, every component of `x*` increases strictly as
   `beta` increases within the endemic chamber.

## Proof

At a face `x_i=0`, `f_i=beta(Ax)_i>=0`; at `x_i=1`, `f_i=-delta_i<0`.
This proves invariance.  Irreducibility and the cooperative variational system
propagate any nonzero coordinate to every vertex, proving strong positivity.

For `s=s(M)<=0`, Perron--Frobenius supplies `w>>0` with `w^T M=s w^T`.
For `V=w^T x`,

\[
 \dot V=sV-\beta w^T\operatorname{diag}(x)Ax.
\]

The first term gives exponential extinction when `s<0`.  At `s=0`, the second
term is nonpositive and, on a strictly positive orbit, vanishes only at zero;
LaSalle's argument closes global extinction.

At criticality, zero is a simple eigenvalue of the irreducible Metzler matrix
`M`, and all remaining spectral values lie in the open left half-plane.  Put
`P=vw^T`, `Q=I-P`, `E=ker(w^T)`, and write `x=av+y`, where `a=w^T x>0` and
`y=Qx in E`.  If `N(x)=-beta*diag(x)Ax`, then

\[
 \dot a=w^TN(x),\qquad
 \dot y=M|_E y+QN(x).
\]

On the positive cone, `a` and `||x||_1` are comparable because `w>>0`.
Consequently `||y||=O(a)` and `|a'|=O(a^2)`.  Set `z=y/a`; it is bounded and
satisfies

\[
 \dot z=M|_E z+\frac{QN(x)}a-\frac{\dot a}{a}z.
\]

Global critical extinction gives `a(t)->0`.  Both terms after `M|_E z` tend
to zero, while `M|_E` is exponentially stable.  Variation of constants
therefore gives `z(t)->0`, i.e. `y=o(a)`, for every nonzero critical orbit,
not merely for an orbit lying on a center manifold.  Exact projection of the
quadratic term now yields

\[
 -\frac{\dot a}{a^2}
 =\beta w^T\operatorname{diag}(x/a)A(x/a)\longrightarrow\kappa.
\]

Thus `(1/a)'->kappa`, so `ta(t)->1/kappa`; since `x/a=v+z->v`, the displayed
vector limit follows.  This also records the normalization that a bare `1/t`
claim would miss.

When `s(M)>0`, a small multiple of the positive Perron vector is a strict
subsolution and the all-ones vector is a strict supersolution.  Cooperative
monotone iteration produces an interior equilibrium.  The identity

\[
 f(\theta x)-\theta f(x)
 =\beta\theta(1-\theta)\operatorname{diag}(x)Ax\gg0,
 \quad 0<\theta<1,
\]

on positive states is strict subhomogeneity.  Comparing the largest and
smallest component ratios of two positive equilibria proves uniqueness;
the same order squeezing proves attraction of every nonzero orbit.

At `x*`, the Jacobian

\[
 J_*=\beta\operatorname{diag}(1-x_*)A
 -\beta\operatorname{diag}(Ax_*)-D
\]

is irreducible Metzler and satisfies
`J_*x_*=-beta diag(Ax_*)x_*<<0`, hence it is Hurwitz.  Differentiating
`f(x_*(beta),beta)=0` gives

\[
 \frac{dx_*}{d\beta}=-J_*^{-1}\operatorname{diag}(1-x_*)Ax_*\gg0,
\]

because `-J_*^{-1}` is strictly positive.

## Exact regression family

The executable receipt covers 20 irreducible regular graphs and 240 exact
parameter rows across subcritical, equality, and endemic chambers.  At
criticality the invariant diagonal solves `y'=-delta y^2`; 720 rational
time samples verify `y(t)=y0/(1+delta*y0*t)` and `t y(t)->1/delta`.  These
rows test conventions and boundary formulas; the proof above owns the
arbitrary-network theorem.

## Route-A boundary

The frozen tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_REJECTED`, with Route B disabled.  The epidemic threshold is not a
rational-prime clock, the equilibria are not primitive source cycles, and no
target determinant or Hilbert--Polya operator is claimed.
