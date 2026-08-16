# Batch review: HCS-P73--HCS-P77

Date: 2026-08-16

System family: frozen area-preserving H\'enon horseshoe only

Recommendation: **PIVOT**

## Completed papers

1. **HCS-P73 — Relative Lind full-ladder counterterm.** Exact partial
   fractions and level-dependent Taylor subtraction turn the nonabsolute raw
   pole family into a normally and unconditionally convergent all-channel
   counterterm on compact punctured subsets.
2. **HCS-P74 — All-channel counterterm gauge rigidity.** Singularity
   cancellation forces every channel coefficient; requiring a holomorphic
   nowhere-zero source extension forces \((a,\beta)=(3/4,1/2)\), but leaves
   a complete \(\mathcal O(\mathbb D)^\times\) holomorphic-gauge torsor.
3. **HCS-P75 — Weighted reflection scalar-channel divisor.** The full
   positive-weight orbit product regroups into exact scalar channels whose
   joint polar hypersurfaces are the smooth, locally finite family
   \(z^{2m}+w^{2m}=1\) in the bidisk.
4. **HCS-P76 — Weighted reflection natural-boundary circle.** On every
   fixed \(q>0\) fiber, all channel roots are exponential essential
   singularities and accumulate densely on
   \(|z|=\min(1,q^{-1})\), the natural boundary of the exact unrenormalized
   punctured continuation.
5. **HCS-P77 — Tautological Fredholm ownership firewall.** A post-hoc
   channel diagonal gives an exact local trace-class determinant, while a
   universal rank-one construction proves that bare representability earns
   no dynamical ownership. The independently specified orbit-block direct
   sum is noncompact.

Every project contains README.md, paper/, code/, experiments/, results/,
notes/, Route-A and Route-B evaluations, and paper/paper.pdf. The final batch
regression ran all five executable packages in normal and optimized modes:
118/118 unit tests passed, every independent reconstruction passed, and all
artifact manifests verified.

## Current strongest Route-A status

For this counterterm/divisor/operator chain, the evaluator tuple is

    (A0_NOT_ADDRESSED,
     A1_WEAK,
     A2_CERTIFIED_PREFIX,
     A3_PARTIAL_ANALYTIC_STRUCTURE,
     A4_FAIL)

with overall status ROUTE_A_EXPLORATORY. The batch supplies an exact
all-channel continuation and a sharp ownership firewall, but no
self-adjoint source operator, rational-prime semantics, prime-power
amplitudes, or explicit formula. Route B is not authorized.

## Strongest positive result

The weighted orbit product now has the exact two-variable continuation

\[
 \log\mathcal Z_{\rm orb}(z,q)
 =\sum_{m\ge1}c_m
 \frac{2(qz)^m}{1-(1+q^{2m})z^{2m}},\qquad
 c_m=\frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}(1-p),
\]

with every \(c_m\ne0\). Introduce an independent fugacity \(w\). The
bidisk lift has channels \(2w^m/(1-z^{2m}-w^{2m})\) and the locally finite
singular divisor

\[
 H_m:\quad z^{2m}+w^{2m}=1.
\]

The physical family is recovered by restriction to \(w=qz\). At \(q=1\),
P73 gives an order-independent primary-factor cancellation of
every complex component of this ledger. P74 then classifies exactly what is
and is not canonical: the singular data are coefficientwise rigid, but the
regularized function remains free up to a nowhere-zero holomorphic gauge.

## Strongest obstruction

Two complementary facts close the naive determinant road.

First, for each fixed \(q>0\), the unrenormalized weighted continuation on
\(\Omega_q=\{|z|<\min(1,q^{-1})\}\setminus\Sigma_q\) has dense exponential
essential singularities approaching the limiting circle, which is a natural
boundary for that exact punctured object. Second, Fredholm
representability by itself is universal:

\[
 F=\det_F\!\left(I+(F-1)P\right)
\]

for every nonvanishing holomorphic \(F\) and rank-one projection \(P\).
Each source-specified cyclic block owns the primitive Euler denominator
\(D_\omega(z)=\det(I-zB_\omega)\), while the P70 factor is
\(D_\omega(z)^{-1}\).  The block singular values stay in \(\{1,q\}\),
and their infinite direct sum is
noncompact and belongs to no Schatten class. Thus neither a reverse-engineered
determinant nor the bare orbit-block sum is the missing transfer owner.

## Reusable structure

The reusable compiler is now

    primitive/repetition ledger
      -> scalar channel index m
      -> smooth two-variable divisor H_m
      -> fiberwise essential-singularity mesh
      -> primary-factor counterterm plus holomorphic gauge
      -> operator-ownership firewall.

It cleanly distinguishes three logically different statements: analytic
continuation of a scalar function, Fredholm representation of that function,
and independent source-native ownership by an operator.

## Most important ROUND2 clue

The next operator candidate must be declared before matching the scalar
coefficients. Freeze its space, action, parameter dependence, and trace law,
then derive the orbit factors from that action. The useful test is not
whether its determinant equals a known function---rank one makes that
automatic---but whether its traces reconstruct primitive and repeated source
orbits without importing the completed scalar ledger.

## Current largest blocker

No compact or nuclear source-native operator owning the exact weighted
primitive Euler denominators and their reciprocal factors has yet been
constructed. P77 proves only that the literal orbit-block direct sum is
noncompact, while the available trace-class diagonal is post hoc and
abelian. Independently, the channel index still has no intrinsic
rational-prime or von-Mangoldt semantics. Operator provenance must be solved
before arithmetic labeling can be assessed.

## Next batch priorities

1. **Source-first operator gate:** predeclare a transfer space and action
   derived from the reflection dynamics, and require its trace powers to
   recover the exact primitive/repetition ledger before comparing
   determinants.
2. **Compactification or no-go:** determine whether a source-native
   normalization of the cyclic orbit blocks can become compact/nuclear while
   preserving every finite Euler denominator polynomial; otherwise prove a scoped
   impossibility theorem.
3. **Arithmetic gate only after ownership:** if a genuine owner survives,
   test its trace labels and amplitudes against rational prime powers. Do not
   generate further genus schedules or post-hoc diagonal/rank-one
   determinants without a new source axiom.

## Decision

**PIVOT.** The batch completed the all-channel renormalization and weighted
singularity geometry requested by P68--P72, then showed why those analytic
successes do not establish transfer ownership. Remain within the frozen
H\'enon family, but pivot from scalar counterterm engineering to a
source-first compact/nuclear operator construction or a precise no-go for
one. Arithmetic promotion remains premature.
