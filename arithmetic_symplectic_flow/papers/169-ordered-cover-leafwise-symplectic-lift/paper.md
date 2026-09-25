# A full leafwise symplectic lift of the ordered cover-scale flow

**Paper ID:** 169-ordered-cover-leafwise-symplectic-lift  
**Candidate ID:** ALF-20260915-OHL01  
**Date:** 2026-09-15  
**Status:** ADVANCE — COMPLETE LEAFWISE SYMPLECTIC PRIME-LOG LIFT; DECLARED DESIGN; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The full weakly ordered divisibility-cover carrier admits a positive-dimensional
leafwise symplectic lift with exactly one primitive logarithmic-time orbit
per prime. The carrier retains its actual nondiscrete transverse topology and
every transverse plane, including planes over mixed nonperiodic chains. A
single integer action controls symbolic shift, reciprocal plane dilation and
scale identification. Its complete quotient flow has a genuine global section
and a roof derived from uniform scale evolution. A global coordinate change
identifies the entire quotient with the original scale quotient times a plane,
with uniform hyperbolic time evolution in that plane. Complete periodic
equations force the transverse origin; no centres or periodic subsystem are
selected. All repetitions and return monodromies follow, and the lift's own
ordinary unweighted orbit product equals the integer Dirichlet series for
Re s>1. The transverse space is nowhere locally compact: this is a topological
transverse / smooth-leaf construction, not a classical symplectic manifold or
an asserted standard locally compact lamination. The admissibility and scale
laws remain explicit engineering choices; natural arithmetic selection,
operator traces and formal Route passage are not established.

## 1. Frozen object and precise question

The [version-1 card](candidate-card.md) precedes this proof. Write x <=_D z
for z/x a positive integer, and x prec_cov z for a strict cover in that order.
Set

\[
X=\{y\in(\mathbb Q_{>0})^{\mathbb Z}:y_0=1,\quad
y_j\prec_{\rm cov}y_{j+1}\ \forall j\},\qquad a_j=y_{j+1}/y_j,
\]

\[
Y=\{y\in X:a_j\le a_{j+1}\ \forall j\},\qquad
F(y)_j=y_{j+1}/y_1.
\tag{1}
\]

Rational coordinates are discrete; whole chains are not. The inequality is
ordinary numerical order. The full new base and scale action are

\[
\widetilde M=Y\times\mathbb R^2,\qquad \omega_y=dq\wedge dp,\qquad
\widetilde F(y,q,p)=(Fy,a_0q,p/a_0),
\tag{2}
\]

\[
K(y,q,p,r)=(Fy,a_0q,p/a_0,r/a_0),\qquad
\widetilde Q=(Y\times\mathbb R^2\times\mathbb R_{>0})/\langle K\rangle,
\]

\[
\widetilde\Phi^t[y,q,p,r]=[y,q,p,e^t r].
\tag{3}
\]

The question is whether this entire object realizes the source, plane
geometry, clock and finite primitive multiplicity together. Let Q_0 be the
quotient of Y times positive scale by G(y,r)=(Fy,r/a_0), and Phi_0 its scale
flow. These definitions agree with [163](../163-ordered-cover-scale-suspension/paper.md),
but all owner relations needed for the new lift are proved below.

| Ledger item | Owner in ALF-20260915-OHL01 | Limit |
| --- | --- | --- |
| Arithmetic source and admissibility | Exactly (1) | Covers and weak order are declared source design |
| Positive-dimensional geometry | All of (2), one symplectic plane per actual transverse chain | Leafwise, not classical manifold-wide symplecticity |
| Time and quotient | Exactly (3), all integer iterates and all real times | One universal scale normalization |
| Source projection | [y,q,p,r] -> [y,r] in Q_0 | Proved on the entire lift, not a selected subsystem |
| Primitive and repeat data | All positive closed times of (3) | Complete equations, not selected centres |
| Analytic owner | Ordinary unweighted product in Section 6 | No stability weight, transfer operator or trace is assumed |
| Measure | Leafwise area only | No transverse probability or Hilbert-space measure supplied |
| Further geometric owner | Hamiltonian/contact/quantum DEFERRED | Three-dimensional suspension leaves are not symplectic manifolds |

## 2. Lineage and exact comparison boundary

The [prior-work guide](../../docs/prior_work/README.md) motivates a geometric
lift that retains prime-symbolic structure. Here the explicit arrow is

~~~text
prime/composite exclusion by intermediate divisors
  -> multiplicative cover atoms
  -> weakly ordered full symbolic carrier
  -> reciprocal-dilation symplectic planes and an owned scale suspension.
~~~

This is a conservative geometric realization of a declared symbolic source,
not a realization of the original Logistic or Henon map. F shifts an admissible
chain; it does not execute chronological sieve tests. No such execution is
needed for the construction theorem, but its absence remains relevant to
stronger natural-source claims.

[052](../052-hyperbolic-wheel-packet-lift/paper.md) already proves the positive
principle that full hyperbolic planes can preserve finite packet multiplicity.
We do not claim to discover that principle or first resolve the continuum
objection. The present differences are the full nondiscrete ordered source,
its ratio-dependent geometric cocycle, and its simultaneous scale quotient.
Each is defined and audited in this new candidate. The identity thickening
failure in [033](../033-wheel-packet-symplectic-thickening-screen/paper.md)
and zero-dimensional loophole in
[034](../034-zero-dimensional-symplectic-loophole/paper.md) remain valid
controls; they do not prohibit every positive-dimensional lift.

This comparison covers the named local records, not an exhaustive literature
or novelty claim. No earlier theorem credit, 153 flat trace, sibling operator,
or Route status is incorporated. The question and owner limits are those of
the [175 batch scope](../175-six-lane-geometric-source-frontier/candidate-card.md).

## 3. The full transverse carrier and leafwise base

### Proposition 1 — Source, topology and symplectic cocycle

The allowed cover ratios are exactly the positive integer primes. Ratio
coordinates identify Y with all weakly nondecreasing bilateral sequences of
these derived atoms, with their product-subspace topology. F and tilde F are
homeomorphisms. The latter is smooth and symplectic between its entire
two-dimensional leaves. For every integer m,

\[
F^m(y)_j=y_{j+m}/y_m,\qquad
\widetilde F^m(y,q,p)=(F^m y,y_mq,p/y_m),
\]

\[
K^m(y,q,p,r)=(F^m y,y_mq,p/y_m,r/y_m).
\tag{4}
\]

Y is totally disconnected and nowhere locally compact. In particular the
construction cannot be reclassified as a finite-dimensional manifold.

**Proof.** A strict divisible ratio n>=2 has an intermediate point if and
only if n=ab with integers a,b>=2: use ax between x and nx, or read the two
integer ratios from any intermediate point. Thus covers derive primality,
without a supplied alphabet. Given any bilateral ratio sequence, its unique
normalized chain is y_j=product_{i=0}^{j-1}a_i for j>0 and
y_j=(product_{i=j}^{-1}a_i)^(-1) for j<0. Each coordinate and inverse ratio
depends on finitely many discrete coordinates, so these maps are mutually
continuous. F shifts ratios left; its inverse shifts them right. Both
preserve every weak inequality. Multiplication telescopes to (4), also for
negative m. All multipliers are positive continuous functions of finitely
many coordinates. Therefore the two maps in (2) are continuous inverses;
on each plane, d(a_0q) wedge d(p/a_0)=dq wedge dp.

Discrete product coordinates separate any two distinct chains by a clopen
set, proving total disconnectedness. For local compactness, a neighborhood
of any y contains a cylinder fixing ratios on some interval [-N,N]. Keep
the given chain through index N, then let a_{N+1} be any sufficiently large
prime and keep that value forever to the right. All such chains remain in
the cylinder and in Y. Their coordinate a_{N+1} takes infinitely many
values. Any compact set containing the cylinder would have finite image
under this continuous map into a discrete space, a contradiction. Thus no
point has a compact neighborhood. This also shows the actual transverse
space is not discrete. QED.

For example a_j=2 for j<0 and a_j=3 for j>=0 is an allowed nonperiodic
chain. Every plane over every shift phase of this chain is part of (2).
The argument did not collapse Y to its constant chains.

The word *leafwise* has a precise elementary meaning here: the base charts
are V times R^2 for transverse open V in Y, with planes {y} times R^2 as
smooth leaves; tilde F maps whole planes by (2). No transverse derivatives,
finite-dimensional transverse tangent bundle or transverse integration
measure are defined.

## 4. Complete scale quotient, section and geometric projection

### Proposition 2 — Full quotient and its actual timing

The space tilde Q is Hausdorff. Formula (3) defines a jointly continuous
complete flow. The embedded section r=1 is all of tilde M, has first-return
map tilde F, and has actual first-return roof

\[
\tau(y,q,p)=\log a_0(y)\ge\log2.
\tag{5}
\]

The entire quotient is the topological positive-roof suspension of (2).
It has charts with topological transverse Y directions and smooth
three-dimensional plaques, not a claimed locally compact lamination.

**Proof.** In u=log r coordinates, (4) subtracts log y_m from u. Since every
ratio is at least 2, log y_m>=m log2 for m>0 and log y_m<=m log2 for m<0.
Thus the action is free, and for any two bounded u-neighborhoods only
finitely many translates can intersect. Given two nonequivalent points,
first choose bounded u-neighborhoods. For each of the finitely many possible
translates, separate the two distinct points in the Hausdorff product space
and shrink neighborhoods to remove that intersection. Finite intersection
and open saturation produce disjoint neighborhoods in the quotient. This
proves Hausdorffness without local compactness.

The quotient projection is open, because saturations are unions of open
translates. Multiplication r -> exp(t)r commutes with K; the product of its
open quotient projection with the time line is again an open quotient map.
Consequently the descended action is jointly continuous and obeys the full
real group law. It is defined at every finite t and every state.

For each y, y_k increases from zero to infinity as k increases over Z.
There is a unique k with y_k<=r<y_{k+1}. Applying K^k in (4) places the
state in the semi-open strip 1<=r<a_0(y), with its transverse plane still
entire. The actual closed-strip gluing is

\[
(y,q,p,a_0(y))\sim(Fy,a_0q,p/a_0,1).
\tag{6}
\]

Taking logarithms gives the roof strip 0<=u<=tau. Section points cannot
be identified with different section points, since y_m=1 forces m=0.
An open u-strip of width less than log2 has no overlap with any nonzero
translate. Its quotient restriction is an open embedding and supplies
local charts as well as an embedding of the section.

Starting at r=1, a positive section crossing occurs exactly when e^t=y_m,
with m>0. The first value is m=1, yielding (5) and (2). All forward and
backward return gaps are at least log2, so infinitely many crossings cannot
accumulate in finite time. This agrees with the all-time formula already
established. Chart changes are restrictions of (4); y_m is locally constant
in transverse coordinates and the plane/u changes are smooth. Therefore
three-dimensional plaques have a well-defined smooth leaf structure.
No positive-dimensional symplectic form on an odd-dimensional plaque is
asserted. QED.

The same argument without q,p proves the corresponding properties of Q_0.
These local product charts retain the non-locally-compact transverse space;
neither the base nor suspension becomes a classical manifold.

### Proposition 3 — A full geometric trivialization, not a subsystem

There is a homeomorphism and a surjective flow factor

\[
\mathcal H:\widetilde Q\longrightarrow Q_0\times\mathbb R^2,\qquad
\mathcal H[y,q,p,r]=([y,r],qr,p/r),
\tag{7}
\]

\[
\mathcal H\widetilde\Phi^t\mathcal H^{-1}(z,Q,P)
=(\Phi_0^t z,e^tQ,e^{-t}P).
\tag{8}
\]

Projection onto Q_0 is exactly [y,q,p,r] -> [y,r]. All fibers are entire
planes; the invariant zero section is not the definition of the carrier.

**Proof.** Under K, the two quantities qr and p/r are unchanged, and the
first coordinate in (7) changes by G. Thus (7) is well defined and continuous
by the quotient property. Conversely represent z by (y,r) and set
q=Q/r and p=Pr. Replacing the representative by G^m changes these coordinates
exactly by K^m in (4). Hence this inverse is well defined. It is continuous
because the map from Y times positive scale times R^2 into tilde Q is
continuous and the quotient onto Q_0 times R^2 is open. The two formulas
are inverse on all states. Direct substitution of r -> exp(t)r proves
(8), including its single uniform time normalization. QED.

This is an explicit owned hyperbolic plane evolution. It is not obtained
by giving each periodic base point a separately chosen physical clock.
It is globally a product construction, not an irreducible source--geometry
feedback coupling: the source evolution receives no feedback from the plane.
Nor does the existence of (8) turn the transverse topological carrier into
a smooth Anosov manifold or a Hamiltonian realization.

## 5. Complete primitive ledger and monodromy

### Proposition 4 — All and only the prime zero-section circles close

There is exactly one primitive oriented closed tilde Phi orbit gamma_l for
each prime l. Its primitive time, every repeated time, and transverse
return monodromy are

\[
T_{\gamma_l}=\log l,\qquad T_{\gamma_l^k}=k\log l,\qquad
P_{l,k}=\begin{pmatrix}l^k&0\\0&l^{-k}\end{pmatrix}\quad(k\ge1).
\tag{9}
\]

There are no other periodic points or additional primitive packets arising
from planes, scale representatives, or mixed chains.

**Proof.** A positive time t closes a point if and only if, for some integer
m, K^m(y,q,p,e^t r)=(y,q,p,r). By (4) this is equivalent to all four equations

\[
F^m y=y,\qquad y_mq=q,\qquad p/y_m=p,\qquad e^t=y_m.
\tag{10}
\]

The final equation forces m>0 and y_m>1, so the middle two force q=p=0.
This is a consequence of the equations on every plane, not a restriction
to chosen centres. The first equation makes the ratios m-periodic; weak
ordering gives a_j<=a_{j+1}<=...<=a_{j+m}=a_j. Every inequality is therefore
an equality. The chain is y_j=l^j for a single prime l. Conversely each
such chain and the transverse origin satisfy (10) exactly for
t in (log l)Z. This proves least positive time and all repetitions.

For fixed l all scale values are phases of the same orbit; the quotient
is R/(log l)Z. It is genuinely an embedded circle: the continuous injective
map from that compact circle to the Hausdorff quotient is an embedding.
Distinct l are never identified by K or by the flow. No mixed chain can
close, and every quotient point meets the section, so (10) is exhaustive.
Orientation is increasing t; no reversal equivalence is imposed.

At this fixed base chain the kth return on its whole plane is
(q,p) -> (l^kq,l^{-k}p), so differentiation yields (9). In particular

\[
\det(I-P_{l,k})=(1-l^k)(1-l^{-k})=2-l^k-l^{-k}<0.
\tag{11}
\]

Thus there is no neutral transverse plane eigenvalue and no transverse
periodic continuum. The three-dimensional smooth suspension leaf still
has its usual time-direction eigenvalue 1; nothing here removes that
flow-neutral direction or defines derivatives transverse to Y. QED.

For every finite T, primitives with time <=T have l<=exp(T). Counting all
positive repeats with time <=T remains finite since k<=T/log2. This exact
bound proves coverage without any sampled orbit table. Formula (8) also
shows uniform hyperbolic rates e^t and e^(-t) in its plane coordinates;
this is leafwise hyperbolicity, not a global smooth-manifold claim.

## 6. The lift's ordinary orbit product

### Proposition 5 — Ordinary Euler identity in its defining half-plane

Using all primitive orbits of the lifted object with weight one, set

\[
L_{\rm lift}(s)=\sum_{\gamma\ {\rm primitive}}\sum_{k\ge1}
\frac{e^{-skT_\gamma}}k,\qquad Z_{\rm lift}(s)=\exp L_{\rm lift}(s).
\tag{12}
\]

The logarithm converges absolutely exactly for Re s>1. In that region,

\[
Z_{\rm lift}(s)=\prod_{l\ {\rm prime}}(1-l^{-s})^{-1}
=\sum_{n\ge1}n^{-s}.
\tag{13}
\]

**Proof.** Proposition 4 identifies every term of (12) as l^(-ks)/k,
with no extra packets or weights. For sigma=Re s>1 the absolute inner
sum is at most l^(-sigma)/(1-2^(-sigma)); summing over primes is bounded
by the convergent integer series. The same estimate locally uniformly
away from sigma=1 proves holomorphy of L and of its nonzero exponential.
Finite prime products expand by unique factorization with coefficient
one for each supported integer; absolute convergence then gives (13).
At sigma=1 the finite product over l<=N is at least sum_{n<=N}1/n.
Taking logarithms shows divergence of the absolute logarithmic series.
For sigma<=1 its positive terms are termwise at least those at 1, proving
the exact boundary. QED.

This proof starts with the new flow's full ledger. The answer agrees with
163 because Proposition 4 proves a full primitive-orbit bijection preserving
times. It is not a borrowed analytic assertion. Monodromy (11) has not been
inserted as a trace weight; no ordinary operator trace, flat trace,
Fredholm determinant, continuation or completed target identity is implied.

## 7. Controls, adverse findings and naturalness limits

| Control | Exact outcome | Meaning |
| --- | --- | --- |
| Composite ratio 4 | 2x lies strictly between x and 4x in the divisibility order | Covers, not hyperbolicity, supply integer irreducibility |
| Mixed 2-to-3 single-transition chain, all planes | Retained, complete, nonperiodic by (10) | The full carrier is not a chosen periodic subsystem |
| Nonzero q or p over any chain | Cannot solve a positive-time equation (10) | Finite multiplicity follows from dynamics on every plane |
| Replace transverse dilation by identity in both base and quotient | For each constant prime chain every (q,p) is a distinct periodic circle of the same log-prime time | Different-owner continuum control reproduces the mechanism of 033 |
| Remove weak ordering, retain covers and the lift | The mixed primitive ratio word (2,3) closes at the origin at time log6 with monodromy diag(6,1/6) | Hyperbolic lifting does not eliminate mixed source packets |
| Remove covers but retain strict integer divisibility and weak order | Constant composite ratio 4 now produces a primitive log4 circle | Ordering alone does not select primes |
| Change uniform time law to exp(c t), c>0 | Return times become (log l)/c | Declared normalization is not uniquely forced by arithmetic |
| Replace cover atoms by any numerically ordered alphabet bounded below by 2 | Periodicity still forces constant symbols and plane equations still force the origin | PROVES_TOO_MUCH for geometry and monotone recurrence alone |
| Inspect transverse topology | Y has no compact neighborhoods | No classical symplectic manifold or standard locally compact lamination obtained |
| Inspect (11) versus (12) | Ordinary orbit weights remain one, not inverse monodromy determinants | A geometric stability calculation is not a constructed trace formula |

The strongest naturalness objection is accepted and delimited: the order rule,
reciprocal-dilation cocycle and exponential scale law are design choices,
even though one ratio and one time action own all their consequences. This
does not invalidate the construction, but it leaves canonical arithmetic
selection and chronological prime generation OPEN. The geometric improvement
does not turn an engineered source into a natural A0 pass.

All real plane coordinates are included, without compactification, phase
selection, fitted prime parameters, Riemann-zero data or von Mangoldt weights.
No numerical experiment or cutoff extrapolation is used.

## 8. Owner-level assessment and decision

| Audit | Evidence | Status and boundary |
| --- | --- | --- |
| T0 full carrier / geometry | Propositions 1--3 | ESTABLISHED for topological transverse / smooth-leaf category; classical symplectic fields NOT APPLICABLE |
| T1 arithmetic source | Cover argument in Proposition 1 and exact factor (7) | SCOPED ESTABLISHED as the declared symbolic deformation; not sieve execution |
| T1 clock ownership | Same action (3), section (5), all-state conjugacy (8) | ESTABLISHED under declared scale design; naturalness OPEN |
| T2 primitive packets / repeats / stability | Full equations (10), (9)--(11) | ESTABLISHED on all states, each prime exactly one packet |
| T3 ordinary orbit product | Proposition 5 | ESTABLISHED for Re s>1 only; no transfer/trace/Fredholm owner supplied |
| Classical A0--A2 / formal Route | No classical global symplectic manifold or formal evaluation | NOT APPLICABLE / UNASSIGNED |
| Route B | Not invoked | NOT INVOKED |

**Decision: advance this scoped geometric construction, retaining naturalness
OPEN; fork before changing carrier, time law or analytic owner.** The same
object owns the source projection, full planes, complete time evolution,
primitive multiplicities, all repetitions, monodromy and ordinary product.
No such result transfers automatically to a classical manifold or to another
paper's trace representation. Further research is not authorized by this
conclusion alone.

## Reproducibility and research integrity

Inputs are exactly (1)--(3), all integers/rationals permitted there, full real
planes, and the exponential time normalization. The exact proofs are the
mathematical method and output. There are no sampled data, numerical precision
choices or downloaded sources. See the [card](candidate-card.md),
[claim ledger](claim-ledger.md), [evidence index](evidence/README.md), and
[summary](README.md). A separate invocation's risk-focused model review is
recorded independently and is not human peer review or an error-independence
certificate.

ARS is used only for bounded claim/evidence/counterargument discipline, not
its full publication workflow. This Markdown research record has no
human-subject data. Authorship is AI-assisted construction and model checking;
no human contribution, funding or conflict-of-interest facts are inferred.
