# Independent internal review — PDI01

**Candidate:** `ANG-20260919-PDI01`. **Date:** 2026-09-19.
**Scope:** bounded exact review of a lane not admitted as a promising main candidate.
**Verdict:** PASS for the proof/stop record; no blocking error or required change.
The proposed full-owner clock fails, rather than receiving candidate credit.

## Inputs, method and independence

| Input | SHA256 |
| --- | --- |
| Version-1 raw card read before the manuscript | `088e64e21d89034ba04e8e647d287520a7eff724bb2629bcf287f32ee05017fd` |
| Manuscript reviewed | `8f0a8d4843fe983a93441fde41db2c304435fc0def89957c98856333b9a81bc5` |

The reviewer derived the concrete inverse, unit controls, all-iterate
Jacobian, coordinate removal and atomic-scope limitation from the raw
card, and sent those conclusions before reading the manuscript. Later
comparison is explicitly a readback, not a claim of blind review at
every stage. No prior-package conclusion was used as a proof premise.

ARS academic-research-suite's deep-research devil's-advocate procedure
organized the three checkpoints below. A further bounded model audit
received only the abstract atomic partial-bijection assumptions, not the
root manuscript, and confirmed the reviewer's existing derivation and
scope exclusions. It is supplementary internal checking, not additional
independent mathematical authority. Agents share model lineage/context;
this is not external peer review, human certification, formal proof
checking or a guarantee of independent errors.

No scientific computation, orbit census, candidate expansion, operator,
trace construction or formal Route evaluation was performed. Document
hash checks are administrative, not scientific experiments.

## Checkpoint 1 — raw-card derivation and decisive gate: PASS

**Full action, including composite bases.** For a>=2, k_a(b) is finite.
Integer cancellation gives k_a(ab)=k_a(b)+1 and, whenever a divides b,
k_a(b/a)=k_a(b)−1. No prime factorization assumption about a is needed.
Odd k ensures integral division. Thus each non-unit J branch reverses
the other; J(1,b)=(1,b) supplies the necessary separate unit boundary.
One must not assign a parity to the unbounded powers of 1. Since S is
also an involution, F=SJ is a bijection and F^(-1)=JS on all X.

Explicitly, if b>=2, the inverse sends (a,b) to (b,ab) when k_b(a)
is even, and to (b,a/b) when it is odd; if b=1, it sends (a,1) to
(1,a). This checks the opposite unit boundary as well as the forward
formula. Discreteness makes the bijection and its inverse continuous.

**Source controls, not a selected carrier.** For every integer n>=2,
(1,n), (n,1), (n,n) form a three-cycle, and their pairwise distinctness
makes three its least period, not merely a return time. Different n
give different cycles. The control includes primes, prime powers and
other composites without distinction. The state (1,1) is fixed.
This refutes prime selectivity of that subledger without classifying
the remaining F-cycles. No higher-period enumeration is required.

**Full atomic image identity.** Put w(a,b)=1/(ab) and L=−log w=log(ab).
Each atom is positive and finite; countability gives sigma-finiteness,
not a normalized probability. For every integer m, singleton evaluation
uniquely forces J_m(x)=w(F^m x)/w(x). Bijectivity and countable additivity
prove the identity on every subset, including when the total is infinite.
The pointwise clock is therefore c(m,x)=L(F^m x)−L(x), for negative
as well as positive iterates. It satisfies the cocycle law by cancellation.
The three single-step cases are +log a, −log a and 0 at a=1.

**Complete time-return result.** Every base return has c=0. More strongly,
v=u−L(x) is a global homeomorphic coordinate change on X×R; all extension
arrows preserve v, while physical time still sends v to v+t. Thus every
isomorphism-class time stabilizer is {0}. This argument covers all states,
not only the exhibited cycles, and proves absence of primitive positive
time-return packets under the frozen convention.

The coordinate change retains each iterate label. At every x, extension
fixed-object isotropy is exactly {m:F^m x=x}, not necessarily trivial.
It is 3Z on the displayed three-cycles and Z at (1,1). The three-cycle
clock values 0,+log n,−log n cancel. Neither base cycles nor surviving
discrete isotropy supplies a nonzero physical return.

**Bounded atomic control.** For any allowed partial bijection g with
0<w(z)<infinity at every state, its singleton image identity forces
J_g(z)=w(gz)/w(z). With h(z)=−log w(z), c=h(gz)−h(z). This is also
valid when distinct arrows have the same endpoints: they have equal
clock, while their labels and isotropy need not coincide. The coordinate
v=u−h(z) removes this cocycle. All isotropy clocks vanish and all physical
time stabilizers are trivial. Arbitrary reweighting within this class
cannot repair the proposed mechanism.

This is not a result about non-atomic geometric Jacobians, zero/infinite
point masses, branching correspondences without the stated injective
image rule, independently specified algebraic index characters, or a
different positive roof. Those are outside the tested prescription.

The precommitted stop is already decisive. No full base-cycle ledger,
operator, zeta or T3 rescue follows from this review.

## Checkpoint 2 — manuscript, added topology and source: PASS

Propositions 1–5 agree with the raw derivation and keep all unit states,
inverse arrows, zero/negative increments and distinct iterate labels.
The manuscript separates source cycles, extension fixed-object isotropy
and actual time returns correctly. Its source predicates are re-evaluated
observables, not claimed F-invariants; arithmetic execution alone is not
promoted to prime selectivity or a Logistic/Hénon semiconjugacy.

The added coarse-quotient argument is correct. X/F has the discrete
quotient topology because X is discrete. After coordinate removal,
the groupoid orbit through (x,v) is the full F-orbit of x times {v}.
The projection to (X/F)×R is continuous and open: an open set is a union
of sets {x}×V_x, and its image on a base orbit is that orbit label times
the open union of the corresponding V_x. It is a surjection with exactly
these fibers, hence induces the claimed quotient homeomorphism.
Consequently the coarse space is Hausdorff and physical time translates
each R-component. This coarse description does not erase the isotropy
of the frozen groupoid, and Hausdorffness does not rescue its clock.

Direct source checking was limited to Danilenko–Silva,
[Ergodic Theory: Nonsingular Transformations, version 3, Sections 2.1 and 5.2](https://arxiv.org/pdf/0803.2424v3).
Section 2.1 states the Radon–Nikodym cocycle convention; Section 5.2
uses the negative-logarithm real extension and real translations that
commute with it. This supports the manuscript's terminology citation.
The sign and pointwise atomic result here are proved directly. No
non-atomic ergodic-type classification, measure-theoretic associated-flow
identification, or novel general coboundary theorem is imported.

## Checkpoint 3 — strongest counterarguments and final verdict: PASS

| Challenge | Resolution |
| --- | --- |
| A local log p might be a prime return time | The actual loop has increments 0,+log p,−log p; all closed clocks vanish globally. |
| Composite bases might invalidate the parity toggle | The cancellation identities use arbitrary integer a>=2, not prime valuations. |
| A source cycle might become a time circle | Its extension isotropy survives with zero clock; the actual time orbit remains a line. |
| The coordinate change might discard arrows or change physical time | It preserves iterate labels and commutes with u-translation; it is a full-owner conjugacy. |
| Other positive atom weights might repair the clock | Every such image Jacobian is the same kind of endpoint-weight ratio. |
| A general non-atomic/index-clock no-go might have been proved | It has not: Proposition 5 expressly excludes those distinct prescriptions and geometries. |
| The Hausdorff coarse quotient might count as target progress | It validates topology only; no positive time-return packet exists. |

Required changes: **none**. The correct disposition is **stop this
mechanism / fork search**, with this lane still not admitted as a
promising main candidate. Full ownership, source reversibility and
the owned cocycle are established; the proposed prime-return clock
fails and design naturalness remains OPEN. T2 has an empty positive
time-return ledger, not an unproved full classification of F-cycles.
T3 is not supplied; classical fields are NOT APPLICABLE, formal
coordinates UNASSIGNED, Route B NOT INVOKED. The report grants no new
claim about 241/242 or any other frozen owner.
