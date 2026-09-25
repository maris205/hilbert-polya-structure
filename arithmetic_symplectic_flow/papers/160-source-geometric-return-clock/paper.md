# A complete divisor-scan flow with an engineered prime-log transit clock

**Paper ID:** 160-source-geometric-return-clock  
**Candidate ID:** ASFS-20260915-SGC01  
**Date:** 2026-09-15  
**Status:** ENGINEERED PRIME-LOG FLOW UNDER PRESPECIFIED DILATION/RESET TIMING — ESTABLISHED; SOURCE-CLOCK NATURALNESS OPEN; STOP PROMOTION.  
**Route:** Owner-level construction audit; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

Under prespecified dilation/reset timing, an explicitly frozen all-integer
divisor scanner is realized by a smooth symplectic cotangent map and a
complete suspension. Each local scan interval is traversed under the same
declared dilation law, with a precisely specified final reset seam. On the
full state space every composite fibre has no
periodic state, and every prime fibre has exactly one hyperbolic primitive
orbit of elapsed time log p. The ordinary orbit product therefore equals
the prime Euler product on its initial absolute-convergence half-plane.
This is a bounded engineered-clock result, not a proof of natural
arithmetic time. Indeed, the roof is cohomologous on each finite phase cycle
to placing the entire log n time at its reset edge. The chosen dilation
law, initialization interval and reset identification remain explicit
geometric design inputs. The construction stops promotion toward natural
A0 rather than treating geometric consistency as removal of that gap.

## 1. Frozen identity and design boundary

The [version-1 card](candidate-card.md) was written before this construction
audit. All results below concern that displayed map and roof, not the
dyadic unit-roof candidates [147](../147-saturated-drift-cotangent-sieve/paper.md)
or [153](../153-saturated-sieve-flat-trace/paper.md). Their traces and
ordinary products are not transferred.

For every integer n>=2 define L_n=n-1 and cyclic phases d=1,...,n-1.
Let

\[
w(n,d)=
\begin{cases}
1,&2\le d<n\ \text{and}\ d\mid n,\\
0,&\text{otherwise}.
\end{cases}
\qquad
a(n)=\sum_{d=1}^{n-1}w(n,d).
\tag{1}
\]

Thus a(n) is the number of proper nontrivial divisors. The phase d=1
is a neutral initialization interval, not an additional divisibility
test. All n-2 actual tests occur once per scan, including the empty scan
at n=2. No prime labels are used to define the carrier or the update.

Freeze

\[
M=\coprod_{n\ge2,\,1\le d<n}\mathbb R^2_{n,d},\qquad
\omega|_{\mathbb R^2_{n,d}}=dq\wedge dp,
\]
\[
f_{n,d}(q)=q+\tfrac12\tanh q+L_nw(n,d),
\qquad
F(n,d,q,p)=
\left(n,d^+,f_{n,d}(q),\frac{p}{f'_{n,d}(q)}\right).
\tag{2}
\]

On each scan interval r runs from d to d+1 under the same law dr/dt=r.
This fixes the roof

\[
\tau(n,d,q,p)=\int_d^{d+1}\frac{dr}{r}
=\log\frac{d+1}{d}>0.
\tag{3}
\]

The candidate is the endpoint-glued suspension

\[
X_\tau=\{(z,t):z\in M,\ 0\le t\le\tau(z)\}/
((z,\tau(z))\sim(Fz,0)),
\tag{4}
\]

with translation in t and the stated gluing. The variable r=d e^t gives
an equivalent interval description. Internal seams identify r=d+1
with the next interval's lower endpoint. The final seam identifies
(z,n) with (Fz,1); it is an explicit reset and is not a continuous
positive-time return path from n to 1.

| Item | Same owner in ASFS-20260915-SGC01 | Limit |
| --- | --- | --- |
| Arithmetic | All local tests (1) act inside (2) | No chronological evolution from n to n+1 |
| Geometry | Full countable union of real planes, all q and p | Disconnected and noncompact |
| Lineage | Divisor-exclusion symbol -> local finite scan -> bounded configuration drift -> canonical cotangent lift | A constraint deformation, not an infinite prime-word conjugacy |
| Clock | Exactly (3), with flow (4) and the specified reset | Dilation law and seam are declared design inputs |
| Periodic convention | All least-period full states, modulo cyclic phase | No centre, momentum or prime-domain restriction before proof |
| Repetitions | Repeated traversal of the same oriented flow orbit | Not a new orbit for each phase or repetition |
| Analytic owner | Ordinary unweighted orbit Z only | Operator, trace and Fredholm realization OPEN |
| Measure | Componentwise symplectic area | No finite normalization of canonical area or trace normalization is supplied |
| Later owner | Hamiltonian/contact/quantum DEFERRED | The three-dimensional suspension is not automatically symplectic |

The [prior-work lineage](../../docs/prior_work/README.md) is retained through
the explicit prime/composite admissibility witnesses, their sequential local
execution, and a positive-dimensional conservative lift. The geometric
clock hypothesis is a deformation added to that source; it is not claimed
to be an already proved feature of the original Logistic or Hénon work.

## 2. Two pre-P0 screens and the nearest controls

The earlier [108 bounded next-clock screen](../108-source-action-frontier-cycle-11/evidence/README.md#bounded-next-clock-hypothesis-screen)
already identified integer-boundary dilation/reset and telescoping
increments as potential rewritings of an installed log n roof. It admitted
no sufficiently specified source-owned candidate and expressly made no
general impossibility claim. This package does not claim that risk is
new or has been overcome: its addition is the explicit frozen construction
and complete-state audit under the timing assumption. The source-naturalness
obligation identified by 108 remains OPEN.

The first screened proposal treats elapsed time as the change of a globally
defined positive scale R. Its logarithmic increment is an exact difference,
log R(y)-log R(x), so its total is zero on a genuinely closed path.
If an excursion from scale 1 to n is closed by returning that same scale
to 1, the final increment is -log n. This is a finite-scan instance of the
existing [029 index-cocycle obstruction](../029-primorial-index-cocycle-screen/paper.md),
not a new general theorem or an achievement assigned to this candidate.

The second proposal, frozen in (2)--(4), has a quotient seam and positive
transit time. Here r is not a global real coordinate on a closed orbit.
Its difference from the first proposal is an explicit change of geometric
object, not the omission of a negative contribution from one fixed cocycle.

The historical [082 control](../082-gpf-fixed-point-euler-control/paper.md)
uses a global greatest-prime-factor map, prime fixed labels, and a direct
roof log p on those labels. The present map instead executes every proper
divisor test locally on every n, with a proved full positive-dimensional
periodic ledger and a phase-dependent transit roof. These are genuine
construction differences, not a proof that target-installation concerns
have disappeared. Section 6 makes their remaining clock similarity exact.

The [143 batching boundary](../143-dyadic-batched-divisor-counter/paper.md)
also remains relevant: a well-defined processing schedule is not by itself
a source-determined geometric time. Finally, the
[155 incompleteness result](../155-derivative-roof-completeness-test/paper.md)
concerns a different state-dependent roof and is not automatically inherited.

## 3. Full geometry and complete owned time

### Proposition 1 — Global symplectic base

F is a smooth symplectomorphism of the full two-dimensional M.

**Proof.** The countable disjoint union of planes is Hausdorff and
second-countable. On each component

\[
f'_{n,d}(q)=1+\tfrac12\operatorname{sech}^2q\in(1,3/2].
\tag{5}
\]

The difference f(q)-q is bounded as a function of q on that component,
so f tends to the corresponding infinity at both ends. It is an
increasing onto smooth diffeomorphism of the real line. Given the next
phase and (Q,P), take the preceding phase and recover
q=f^{-1}(Q), p=P f'(q). This defines the smooth global inverse.
Since P dQ=(p/f'(q))d(f(q))=p dq, the cotangent map preserves
dq wedge dp on every component. QED.

### Proposition 2 — Complete dilation-transit suspension

The frozen quotient (4) is a smooth three-dimensional suspension with
a flow defined for every real time and every full state. Its slab
description has the same time, including at the final seam.

**Proof.** The roof is a positive smooth function, constant on each
component. Standard crossing coordinates here can be written directly:
near an upper endpoint use (Fz,t-tau(z)); near a lower endpoint use
(z,t). Because tau is locally constant and F is a diffeomorphism, these
are smooth compatible coordinates and the vector field is partial_t.

The change r=d e^t gives r partial_r inside each interval. At an internal
seam the next r coordinate equals the old one. At the final seam the
overlap coordinate is r_new=r_old/n; therefore
r_old partial_(r_old)=r_new partial_(r_new). The reset is represented
by the quotient chart, not by a discontinuous global scalar observable.
All q and p are included through the same F gluing.

On any trajectory the integer n stays fixed and the phases cycle.
For that n every roof is at least

\[
\epsilon_n=\log\frac{n}{n-1}>0.
\tag{6}
\]

Thus any finite elapsed time crosses only finitely many section intervals,
in either direction. Equivalently, every L_n successive intervals sum to

\[
\sum_{d=1}^{n-1}\tau(n,d,q,p)=\log n\ge\log2.
\tag{7}
\]

All finite iterates and inverse iterates exist by Proposition 1.
Consequently neither unbounded configurations nor arbitrarily small
roofs across different n produce finite-time escape. QED.

The global infimum of tau is zero, attained only as an infimum over
different fibres. No trajectory travels through that sequence of fibres.
The contrast with 155 is that its shrinking roofs occur successively
along one permitted trajectory.

## 4. Full intrinsic periodic ledger

### Proposition 3 — Exactly one prime packet; no composite packet

The full periodic set of F is

\[
\operatorname{Per}(F)=
\{(p,d,0,0):p\ \text{prime},\ 1\le d<p\}.
\tag{8}
\]

For each prime p these p-1 points form one primitive orbit of least
period p-1.

**Proof.** A periodic full state of period m must return its phase, hence
m=rL_n for an integer r>=1. Sum the actual configuration increments
from (2) along that proposed full cycle:

\[
0=q_m-q_0
=\tfrac12\sum_{j=0}^{m-1}\tanh q_j+L_n r a(n).
\tag{9}
\]

If n is composite, the nonnegative integer a(n) is at least one.
Since every tanh q_j>-1, the right side is strictly greater than
-m/2+L_n r a(n)>=m/2>0, a contradiction. This excludes every real
configuration and momentum, not merely a chosen invariant subset.

If n is prime then a(n)=0 and all witnesses vanish. The remaining
configuration map q->q+(1/2)tanh q moves every positive q strictly
right and every negative q strictly left, preserving its sign.
No such nonzero configuration is periodic. At q=0 the full momentum
map is p->(2/3)p, so any positive return forces p=0. Conversely the
zero states traverse exactly the L_n cyclic phases, proving (8) and
their least period. QED.

The equivalence a(n)=0 iff n is prime follows directly from the
definition of prime as having no divisor strictly between 1 and n.
No factorization oracle or prime table is evaluated inside (2).

### Proposition 4 — Owned primitive times and nondegenerate repetitions

The complete flow has exactly one oriented primitive closed orbit
gamma_p for each prime p. Its actual elapsed times and monodromy obey

\[
T_{\gamma_p}=\log p,\qquad
T_{\gamma_p^r}=r\log p,\qquad
P_p=\operatorname{diag}((3/2)^{p-1},(2/3)^{p-1}).
\tag{10}
\]

Every positive repetition is nondegenerate.

**Proof.** A closed flow orbit must cross the section and give a
periodic F-state; conversely each primitive F-cycle produces one
oriented flow orbit. Positive local time and Proposition 2 preclude
hidden finite-time accumulation. Quotienting its p-1 section points
by cyclic phase leaves one orbit. The roof sum is exactly (7) with
n=p, and repeating that same cycle r times gives r times its time.

At the surviving q=p=0 state, the cross derivative
-p f''(q)/(f'(q))^2 vanishes. The full step derivative is
diag(3/2,2/3). Its actual p-1 step product gives (10), and

\[
\det(I-P_p^r)=
2-(3/2)^{r(p-1)}-(2/3)^{r(p-1)}<0.
\tag{11}
\]

Thus all repetitions are hyperbolic and nondegenerate. QED.

For n=2 there is one neutral phase, no proper-divisor tests, one derived
fixed state, and roof log2. It is neither a zero-length cycle nor an
exception requiring a prime-specific formula. For n=3 there are two
phases with times log2 and log(3/2), summing to log3.

## 5. Ordinary product only

### Proposition 5 — The full owned ordinary orbit product

The unweighted primitive product is

\[
Z(s)=\prod_{\gamma\ \mathrm{primitive}}(1-e^{-sT_\gamma})^{-1}
=\prod_{p\ \mathrm{prime}}(1-p^{-s})^{-1},
\qquad \Re s>1.
\tag{12}
\]

Its defining logarithmic series has exact absolute-convergence abscissa
1. On that same half-plane it equals the Dirichlet series
sum_(m>=1) m^(-s), with normalization tending to 1 as real s tends
to positive infinity.

**Proof.** Proposition 4 proves the full orbit and repetition ledger;
each orbit has weight one, so no arithmetic coefficient is added.
For sigma>1,

\[
\sum_p\sum_{r\ge1}\frac{p^{-\sigma r}}r
\le\frac{1}{1-2^{-\sigma}}\sum_{n\ge2}n^{-\sigma}<\infty.
\tag{13}
\]

This also gives locally uniform convergence on Re s>1 and a
holomorphic nonzero product there. The series sum_p 1/p diverges:
otherwise the finite products over p<=N of (1-1/p)^(-1) would
be uniformly bounded, using
-log(1-x)<=2x for 0<=x<=1/2. But their positive geometric expansions
contain every 1/m with m<=N, by integer prime factorization, and
therefore dominate the divergent harmonic sum. Thus already the
r=1 terms diverge at sigma=1, proving the exact absolute boundary.
Absolute convergence and uniqueness of prime factorization identify
the expanded product with sum_(m>=1) m^(-s) for Re s>1. QED.

Equation (12) is an equality on the original convergence domain,
not a newly constructed analytic continuation, operator determinant,
trace formula, target-zero result or formal Route-A divisor verdict.
No transfer operator or function space has been specified here.
In particular 153's flat traces do not acquire this changed clock.

## 6. Clock cohomology and adverse controls

### Proposition 6 — The positive transit roof concentrates at the reset

Let h(n,d,q,p)=log d. For the same finite phase cycle,

\[
\tau(z)=h(Fz)-h(z)+
\mathbf1_{\{d=n-1\}}\log n.
\tag{14}
\]

**Proof.** For d<n-1 the next phase is d+1, so the difference
is exactly log((d+1)/d). At d=n-1 the next phase is 1,
and -log(n-1)+log n is the last roof. This includes n=2.
The q and p updates do not enter h. QED.

This is the precise surviving warning in the main claim: all total
log n time can be concentrated on the scan's reset edge by adding a
coboundary. The positive roof (3) is not equal to an exact difference
on a closed cycle, because the reset term remains. Geometric
reparameterization alone does not establish why arithmetic should
privilege that reset time. Conversely (14) is not a theorem that every
cohomologous positive roof is illegitimate or that this flow fails
to exist.

| Control | Exact finding | Interpretation |
| --- | --- | --- |
| Remove all witnesses | The proof gives one zero-state packet for every integer n, still of time log n | Prime selectivity comes from executed witnesses; the clock separately tracks scan size |
| Replace witnesses by arbitrary nonnegative integer tests | Their total zero set controls recurrence by the same cycle-sum argument | PROVES_TOO_MUCH: generic constraint engineering remains possible |
| Keep every q and p | Propositions 2--4 apply to the entire carrier | No centre selection, nonzero-momentum omission or periodic-domain crop |
| Use dr/dt=1 in the same event skeleton | Each interval takes one unit; total time is n-1 | A different allowed positive velocity changes the clock without changing the event map |
| Shift all marks by a fixed a>-1 | Dilation from d+a to d+1+a totals log((n+a)/(1+a)) | The chosen initialization and multiplicative origin matter; this comparator is not the frozen roof |
| Compare global infimum with orbitwise sums | inf_M tau=0 but every trajectory repeats a fixed finite phase list of sum log n | The 155 mechanism is absent; pointwise positivity alone was not used as proof |
| Reset-edge identity | Equation (14) retains the log n boundary term | No claim that the transit formula by itself solves source-clock naturalness |

These comparator objects are not substitutes in (12). In particular,
using a constant velocity or shifted marks would require a new
candidate card before any result was assigned to those flows.
The arithmetic tests do not prove a continuous dilation symmetry of
the integer source, nor select the time form dr/r. No uniqueness
requirement is imposed: the narrower unproved obligation is a
source-based justification of the chosen clock mechanism.

## 7. Assessment and decision

| Obligation | Finding for the frozen object | Scope |
| --- | --- | --- |
| P0 geometric and clock consistency | Established globally | Explicit engineered assumption, full-state completeness |
| A0 operational source | Local divisor witnesses select prime periodic support | Source-determined or privileged clock naturalness OPEN |
| A1 geometric ledger | One complete intrinsic primitive packet per prime, exact owned log p times and repetitions | No inherited source-clock naturalness or formal Route credit |
| A2 ordinary product | Equation (12) on Re s>1 | Operator, trace, Fredholm and target-divisor evaluation NOT SUPPLIED |
| Formal Route / B | UNASSIGNED / NOT INVOKED | No formal evaluation or spectral conclusion |

**Portfolio: retain the bounded engineered-clock control under
prespecified dilation/reset timing; stop promotion and fork for a
genuinely justified source-clock mechanism.** There is a complete
same-object construction here, not a proof that the original
prime-symbolic source naturally produces its clock. Equation (14) must
remain beside every summary of the exact log p result. The explicit
velocity and reset seam are neither hidden nor erased by the positive
geometric audit. No further parameter adjustment, trace construction or
naturalness claim is undertaken in this package.

## Evidence and reproducibility

The inputs are the integer formulas (1)--(3), the fixed coefficient 1/2,
and all real q,p. Proofs cover all integers, phases, real states and
positive repetition orders; there is no numerical cutoff or target data.
The [evidence index](evidence/README.md) records the design screen,
independent model-audit provenance and local file checks. The
[claim ledger](claim-ledger.md) separates the exact construction from
its naturalness boundary. No external literature theorem is required
for these direct arguments; linked historical papers are scoped
comparators only. Bounded ARS claim/evidence/counterargument discipline
is used without a publication pipeline or a human-peer-review claim.
