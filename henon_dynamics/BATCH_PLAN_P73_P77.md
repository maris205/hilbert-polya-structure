# Batch plan: HCS-P73--HCS-P77

Date: 2026-08-16

System family: frozen area-preserving H\'enon horseshoe only

Starting point: HCS-P72 proves the exact channel expansion

\[
 \log \mathcal Z_{\rm orb}(t,1)
 =\sum_{m\ge 1}c_m\Phi(t^m),\qquad
 \Phi(x)=\frac{2x}{1-2x^2},\qquad
 c_m=\frac1m\prod_{\substack{p\mid m\\p\ \text{odd}}}(1-p),
\]

and shows that every channel is nonzero.  The P71 relative germ therefore
has an infinite essential-singularity ladder.  The present batch tests the
surviving all-channel, weighted, and punctured-operator directions without
promoting any of them to an arithmetic trace.

## P73: relative Lind full-ladder counterterm

Project slug: `henon_relative_lind_full_ladder_counterterm`

Primary gate: construct a pole-by-pole Weierstrass-type counterterm whose
logarithm converges normally and independently of channel ordering.

For

\[
 \alpha_{m,k}=2^{-1/(2m)}e^{\pi i k/m},\qquad
 b_{m,k}=\frac{c_m(-1)^k}{\sqrt2\,m},
\]

the channel has the partial-fraction expansion

\[
 c_m\Phi(t^m)=\sum_{k=0}^{2m-1}
 \frac{b_{m,k}}{1-t/\alpha_{m,k}}.
\]

The raw pole family is not absolutely summable.  Subtracting the first
`m` Taylor terms from each pole factor makes each factor vanish to order
`m`; the resulting double series is normally and unconditionally
convergent on compact subsets of the punctured unit disk and still sums to
the exact channel tail.  Together with the explicit remaining source factor
at `1+sqrt(2)t=0`, the normalized full counterterm makes the P71/P72 relative
germ identically one on every compatible branch.

Hard firewall: this is an exact renormalization of a known ledger, not an
independent determinant, transfer operator, or arithmetic construction.

## P74: all-channel counterterm rigidity modulo holomorphic gauge

Project slug: `henon_all_channel_counterterm_gauge_rigidity`

Primary gate: decide what the singularity divisor determines uniquely.

In the channel-log class

\[
 W(t)=\exp\!\left(\sum_{m\ge2}d_m\Phi(t^m)+G(t)\right),
\]

removability at the radius belonging to channel `m` forces `d_m=c_m`.
Requiring the remaining source-cancelled object to extend holomorphically and
nowhere zero forces the power and exponential coefficients
`(beta,a)=(1/2,3/4)`.  Nothing in the divisor
fixes the nowhere-zero holomorphic factor `exp(G)`, so the complete family is
a holomorphic-gauge torsor.

The genus schedules `m-1` and `m` provide two exact calibrations.  The first
cancels the channel sector, leaves `exp(-3/2)` after the forced source factor,
and gives complete trivialization only after the stated final scalar
normalization `exp(3/2)`.  Under the same final normalization, the second
preserves the first source monomial of each channel and leaves the explicit
analytic residual

\[
 \exp\!\left(-2\sum_{m\ge2}c_m t^m\right).
\]

Hard firewall: no finite jet normalization removes the holomorphic gauge;
absolute uniqueness may not be claimed.

## P75: weighted reflection scalar-channel divisor

Project slug: `henon_weighted_reflection_channel_divisor`

Primary gate: extend the scalar regrouping to the P70 weight family.

The target identity is

\[
 \log\mathcal Z_{\rm orb}(z,q)
 =\sum_{m\ge1}c_m\Psi_m(z,q),\qquad
 \Psi_m(z,q)=
 \frac{2(qz)^m}{1-(1+q^{2m})z^{2m}}.
\]

The arithmetic coefficient `c_m` is unchanged.  Introduce an independent
fugacity `w`; the bidisk channels have denominator
`1-z^(2m)-w^(2m)` and polar hypersurfaces

\[
 H_m:\ z^{2m}+w^{2m}=1.
\]

They are smooth and locally finite in the open bidisk, and the channel sum
converges normally on compact subsets of their complement.  Restriction to
the physical fiber `w=qz` recovers the positive-`q` family, where channel
`m` has radius

\[
 \rho_m(q)=(1+q^{2m})^{-1/(2m)}.
\]

Hard firewall: for `q != 1` there is no source-native weighted Lind factor
in the current evidence package.

## P76: weighted reflection natural-boundary circle

Project slug: `henon_weighted_reflection_natural_boundary`

Primary gate: classify the global accumulation geometry on every positive
weight fiber.

The radii `rho_m(q)` increase strictly to

\[
 L(q)=\min(1,q^{-1}).
\]

Every point

\[
 \rho_m(q)e^{\pi i k/m},\qquad 0\le k<2m,
\]

is an exponential essential singularity, because different channels have
different moduli and `c_m` never vanishes.  Their arguments become dense.
Consequently the circle `|z|=L(q)` is a natural boundary for this explicit
unrenormalized punctured continuation.

Hard firewall: an all-channel counterterm can remove the prescribed divisor;
the theorem is object-specific and does not prohibit separately renormalized
objects.

## P77: tautological Fredholm ownership firewall

Project slug: `henon_tautological_fredholm_ownership_firewall`

Primary gate: distinguish analytic determinant representation from
source-native transfer ownership.

For each fixed `q>0`, on
`Omega_q={|z|<min(1,q^(-1))} minus Sigma_q`, the diagonal channel operator

\[
 A(z,q)=\operatorname{diag}\bigl(c_m\Psi_m(z,q)\bigr)_{m\ge1}
\]

is holomorphic with values in the trace class.  Hence `K=exp(A)-I` is
trace class and

\[
 \det_F(I+K)=\exp(\operatorname{Tr}A)
\]

reproduces the channel continuation.  This representation is
parameter-dependent and reverse engineered.  Indeed every nonvanishing
holomorphic function has a rank-one determinant representation.

By contrast, each weighted cyclic orbit block owns the Euler denominator
`D_omega(z)=det(I-zB_omega)`, and the P70 Euler factor is its reciprocal.
The source-native direct sum is noncompact: every block
has singular values in `{1,q}`, bounded below by `min(1,q)>0`.  Therefore it
has no standard trace-class Fredholm determinant.

Hard firewall: bare Fredholm representability is universal and does not
establish transfer dynamics, self-adjointness, rational-prime semantics, or
Route B.

## Batch acceptance gates

Each paper must contain:

1. a proof package separating exact theorems from scope firewalls;
2. executable main and independent certificates;
3. unit tests run both normally and with optimization;
4. dependency hashes and mutation rejection;
5. a compiled LaTeX PDF with no unresolved citations or references;
6. Route-A and Route-B evaluations;
7. source, integrity, hostile-review, and failure-mode audits.

The batch review must rerun all five packages, verify the full complex
singularity and operator scopes, update both registries and programme
READMEs, and make an explicit `KEEP`, `PIVOT`, or `STOP` recommendation.
