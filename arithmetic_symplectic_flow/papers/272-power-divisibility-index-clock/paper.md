# Arithmetic returns with a vanishing index clock

**Paper ID:** `272-power-divisibility-index-clock`  
**Candidate ID:** `ANG-20260919-PDI01`  
**Date:** 2026-09-19.  
**Status:** `REVERSIBLE ARITHMETIC SOURCE; EXACT-COBOUNDARY CLOCK — STOP / FORK`.  
**Type:** bounded exact source/clock audit, not main-candidate admission.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

On every pair of positive integers, alternate an involution governed
by power-divisibility parity with coordinate exchange. This gives a
global reversible arithmetic action that changes its source state,
without a prime list or static prime-labelled fiber. It nevertheless
has the same least-three-step cycle for every integer n>=2. The full
atomic measure with mass 1/(ab) produces nonzero logarithmic Jacobians
on many individual arrows, but their cocycle is exactly
log(product at target) minus log(product at source). Every closed
arithmetic return therefore has zero accumulated clock. A global
coordinate change proves that the real-cocycle extension has no
positive time return at any state, while retaining nontrivial discrete
isotropy. The same pointwise obstruction holds for all full-support
finite-positive atomic weights on countable partial-bijection owners.
This narrowly delimited control closes a source-to-clock design lane;
it does not rule out non-atomic geometry or independently derived
index characters. No operator or formal Route evaluation follows.

## 1. Identity, lineage and question

The [version-1 card](candidate-card.md) freezes the exact arithmetic
action, measure, groupoid arrows, clock and return convention before
this proof. This is not a variant of 270/271, and it is not promoted
as a promising main candidate after the pre-P0 scouts found a missing
source-owned return clock. The bounded audit replaces that missing
field by one exact testable prescription and evaluates its failure.

| Field | Same-object definition and scope |
| --- | --- |
| Source | X=N_(>=1)^2, discrete, all states retained |
| Arithmetic observable | k_a(b)=max{k>=0:a^k divides b} for a>=2; its parity governs the next update |
| Evolution | F=S composed with J, the power-divisibility involution and coordinate exchange defined below |
| Measure | mu({(a,b)})=1/(ab), full-support sigma-finite weighted counting measure |
| Clock | Negative logarithm of the pointwise image Jacobian for the entire Z-action |
| Flow owner | Cocycle-extension groupoid on X×R; physical time translates R |
| Return convention | All H_x={c(m,x):F^m x=x}; no selected cycles or collapsed isotropy |
| Classical symplectic map, positive roof, Hamiltonian/contact lift | NOT APPLICABLE / NOT SUPPLIED |
| Operator, trace, determinant | NOT SUPPLIED; T3 not pursued after the stop |

The precise [prior-work arrow](../../docs/prior_work/README.md) is
divisibility-based prime/composite observation -> power-divisibility
symbols of the current state -> reversible multiplicative feedback.
For each a>=2, the exact predicates a^j|b are re-evaluated at the
current pair; their truth set determines k_a(b). No prime valuation
alphabet is inserted: a may be composite. This is a discrete arithmetic
deformation of the source interface, not a Logistic/Hénon semiconjugacy
or a geometric lift. It does not establish prime selectivity merely
because divisibility enters the rule.

The question is whether genuine arithmetic state returns and local
logarithmic Jacobians give a nonzero physical return in this SAME
extension. We distinguish that question from whether F is bijective,
whether it has cycles, or whether one could choose a positive roof.
No parameter, roof fit, prime table, zero data, selected recurrent core
or prescribed prime time is used.

## 2. Definitions and complete reversibility

For a>=2, finiteness of k_a(b) follows from a^k<=b whenever a^k|b.
Put

    J(a,b)=(a,ab)    when k_a(b) is even,
    J(a,b)=(a,b/a)   when k_a(b) is odd,
    J(1,b)=(1,b),
    S(a,b)=(b,a),    F=S composed with J.

The odd branch always has k_a(b)>=1, so its division is integral and
positive. The a=1 rule is part of the full owner, not an omitted limit.

### Proposition 1 — full bijection and exact source execution

J and S are involutions on X. Hence F is a homeomorphism with inverse
J composed with S. It reads and updates its arithmetic source at every
step; it is not an action within a fixed all-integer label fiber.

**Proof.** Integer cancellation, valid also for composite a, gives

    k_a(ab)=k_a(b)+1,
    k_a(b/a)=k_a(b)−1 when a divides b.

If k_a(b) is even, multiplication moves it to odd and the next J
divides by a. If it is odd, division moves it to even and the next J
multiplies. On a=1, J is the identity. Thus J²=id on every state.
Coordinate exchange has S²=id. Their composition is bijective with
the stated inverse; every map and inverse is continuous in the discrete
topology. Explicitly, F(a,b)=(ab,a) on the even branch and (b/a,a) on
the odd branch, whereas F(1,b)=(b,1). These formulas show the actual
changing source coordinates. ∎

### Proposition 2 — a full all-integer return control

For every n>=2 the three distinct states

    (1,n) -> (n,1) -> (n,n) -> (1,n)

form a least-period-three F-cycle. These cycles are different for
different n. The state (1,1) is fixed.

**Proof.** The first arrow uses the a=1 boundary. In the second,
k_n(1)=0 is even, so J multiplies before S exchanges. In the third,
k_n(n)=1 is odd, so J divides before the exchange. The states are
pairwise distinct for n>=2, giving least period exactly three. The
pair with first coordinate 1 recovers n, so different n yield different
cycles. The remaining assertion follows from the boundary rule. ∎

This proof applies equally to prime n, prime powers and all other
composites. It is a PROVES_TOO_MUCH control, not a full classification
of F-cycles. No larger-period search is needed to show that this
primitive source subledger is not prime-selective.

## 3. Exact image Jacobian and all-iterate clock

Every singleton has finite positive mass w(a,b)=1/(ab); countability
therefore gives sigma-finiteness and full support. The total mass is
infinite already on a=1, so no probability normalization is claimed.
For every integer m define the image derivative by

    mu(F^m E)=sum_(x in E) J_m(x) w(x)

for all subsets E of X, allowing either side to be infinite.

### Proposition 3 — nonzero local logarithms but zero loop accumulation

Let L(a,b)=log(ab). The unique pointwise image derivative and cocycle
are

    J_m(x)=w(F^m x)/w(x),
    c(m,x)=−log J_m(x)=L(F^m x)−L(x),        m in Z.

For one step, c is log a on the even branch, −log a on the odd branch,
and 0 on a=1. On every full discrete return F^m x=x, c(m,x)=0.

**Proof.** Setting E={x} forces J_m(x)w(x)=w(F^m x), with no null-point
ambiguity because w(x)>0. Conversely F^m is a bijection, so summing
these equalities over any subset E proves the defining identity.
The formula for w gives the displayed difference of L. For one step,
coordinate exchange preserves ab, whereas J multiplies or divides
that product by a; at a=1 it does not change it. Finally,

    c(m+n,x)=c(n,F^m x)+c(m,x)

by subtraction of the intermediate L-value. This holds for negative
as well as positive iterates. If the source returns, its L-value
returns too, proving zero accumulated clock. ∎

For the explicit three-cycle, the local values are respectively
0, log n and −log n. Even for a prime n=p, a visible log p on one
arrow is canceled by the return arrow. Discarding that arrow, taking
absolute values, omitting zero steps or appending a reset time would
define another clock, not interpret this one.

## 4. The full extension and all physical returns

The base groupoid retains every iterate label m, including different
labels with the same endpoints. The extension arrows are

    (m,x,u): (x,u) -> (F^m x,u+c(m,x)).

Each m-chart is X×R; the disjoint-union arrow topology and object
topology are locally compact Hausdorff. Source and range are local
homeomorphisms. Composition follows the cocycle identity. Physical
time Phi_t(x,u)=(x,u+t), on objects and arrows, is a jointly continuous
groupoid automorphism for every t in R and is two-sided complete.
Nothing here requires c to be a positive suspension roof.

### Proposition 4 — global coordinate removal and empty positive-return ledger

The homeomorphism

    (x,u) -> (x,v),        v=u−L(x),

sends every extension arrow to (m,x,v):(x,v)→(F^m x,v), preserving
its iterate label. It commutes with physical time translation. Thus

    H_x={c(m,x):F^m x=x}={0}                 for every x.

There is no positive time return anywhere in the frozen extension,
and hence no primitive time-return packet.

**Proof.** At the arrow target,

    (u+c(m,x))−L(F^m x)=u−L(x).

L is continuous on the discrete X and finite at every point, so the
coordinate map and inverse v↦v+L(x) are global homeomorphisms. The
iterate labels have not been collapsed. In this coordinate every
groupoid arrow leaves v unchanged, whereas Phi_t changes it by t.
An isomorphism between a state and its time translate can therefore
exist only when t=0. The identity arrow supplies t=0. ∎

The distinction among three notions is essential:

| Notion | At the cycle through (1,n), n>=2 | At (1,1) |
| --- | --- | --- |
| Base iterate isotropy {m:F^m x=x} | 3Z | Z |
| Extension fixed-object isotropy | 3Z, not erased | Z, not erased |
| Physical-time stabilizer H_x | {0} | {0} |

For any other state, the first two groups are again equal, though its
base period is not classified here. Every physical-time stabilizer is
already classified by Proposition 4. Nontrivial discrete isotropy is
not a positive-time return and is not removed to obtain this result.

Unlike 270/271, the coarse quotient here is Hausdorff. More precisely,
the coordinate change identifies it with (X/F)×R, where X/F is the
discrete set of full F-orbits. The map X×R→(X/F)×R is an open continuous
surjection with precisely the groupoid orbits as fibers, hence is the
coarse quotient map. Physical time is translation on each R-component.
The failure is a vanishing return clock, not a hidden non-Hausdorff
topology or an incomplete time action.

## 5. Bounded general control: positive atomic masses

### Proposition 5 — full-support atomic image clocks are exact state differences

Let Z be any countable discrete state space with masses
0<m_z<infinity at every point. Let a discrete groupoid be presented
by partial bijections between subsets of Z, retaining all its arrows.
For each such map g define its image derivative by

    mu(gE)=sum_(z in E) J_g(z)m_z.

Then, at every admissible z,

    J_g(z)=m_(gz)/m_z,
    −log J_g(z)=h(gz)−h(z),       h(z)=−log m_z.

Every isotropy arrow has zero clock, and the corresponding real
cocycle extension has no positive physical-time return.

**Proof.** Apply the identity to {z}. Strict positivity and finiteness
allow division and logarithms. The converse identity on arbitrary
subsets follows by countable additivity and injectivity of g. The
formula telescopes under all composable arrows, independent of whether
several different arrows share endpoints. The same change v=u−h(z)
used in Proposition 4 fixes the real coordinate under every arrow;
time translation remains free. ∎

This excludes a precisely defined clock prescription, not all clocks
on countable sources. In particular it does NOT apply to non-atomic
unstable-volume Jacobians, points of zero measure, branching maps
without a partial-bijection image identity, or separately specified
algebraic index characters. It also does not rule out a positive
suspension roof justified by different geometry. Reweighting the
positive atoms alone cannot evade this proposition.

The cocycle-extension language is standard. Danilenko and Silva give
the Radon–Nikodym cocycle convention and the logarithmic extension
commuting with real translation in Sections 2.1 and 5.2 of
[Ergodic Theory: Nonsingular Transformations](https://arxiv.org/pdf/0803.2424v3).
Our elementary atomic proofs fix the image-measure sign explicitly.
We do not invoke their non-atomic ergodic type classification, identify
our full-state coarse quotient with a measurable associated flow, or
claim a new general coboundary theorem.

## 6. Controls, gates and decision

| Control | Finding | Limit or consequence |
| --- | --- | --- |
| Composite base a in k_a(b) | Cancellation proof still holds | No hidden prime-valuation input |
| a=1 and (1,1) | Defined boundary; one fixed point and full three-cycle families | No boundary deletion |
| Prime/composite n | Same least-three-step family for every n>=2 | Source primitive subledger is not prime-selective |
| Local log n versus entire cycle | 0+log n−log n=0 | Local arithmetic scale does not imply closed time |
| Arbitrary strictly positive atomic weights | Exact state-difference formula persists | Reweighting is not a repair within this class |
| Constant counting weights | Derivative 1 and clock 0 already on each arrow | Simpler comparator; no source return time |
| Different unit-roof suspension over F | Three-step source cycles give time 3, including composites; fixed point gives time 1 | A different clock, with no credit transferred to this extension |
| Full topology and isotropy | Complete time, Hausdorff coarse quotient, discrete isotropy retained | None rescues the zero physical-return ledger |

T0 is established for the discrete arithmetic groupoid and complete
real extension. T1 has a genuine state-dependent divisibility source
and an exactly owned image cocycle, but fails the proposed prime-return
clock mechanism; its design naturalness is still OPEN. T2 has no
positive physical returns on any state. This global statement does
not require or assert a full classification of F's discrete cycles.
T3 is NOT SUPPLIED / NOT PURSUED after the stop. Classical A0/A1/A2
are NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.

Portfolio: **stop this mechanism / fork search**. The decisive reason
is that its entire clock is a state difference and vanishes on every
return. The all-integer three-cycles independently refute prime
selectivity of that base subledger. This is a finite, reusable search
restriction, not successful main-candidate admission or a global
impossibility theorem. Future discrete source proposals need an
independently justified nonzero return cocycle or actual geometry,
not another choice of full-support atomic masses.

## 7. Reproducibility and integrity

All inputs are exact frozen definitions. Proofs use integer cancellation,
singleton measure identities, countable additivity and a global explicit
coordinate change. There is no numerical census, cutoff, floating-point
precision, fitting, data export, PDF generation or scientific run.
Previous cards, 241/242 and all other streams remain unchanged.

See the [claim ledger](claim-ledger.md), [evidence/source record](evidence/README.md),
[three-lane scout dispositions](evidence/scout-record.md), and
[separate internal review](evidence/independent-review.md).
AI-assisted authorship and separate model review were used; shared
context and model lineage mean this is not external peer review,
formal proof verification or a guarantee of independent errors.
The open programme goal remains active.
