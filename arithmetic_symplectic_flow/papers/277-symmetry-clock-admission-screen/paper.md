# Full graph symmetry does not determine the witness-scan clock

**Paper ID:** `277-symmetry-clock-admission-screen`  
**Screen ID:** `ASFS-SCOUT-20260919-SYM01`  
**Date:** 2026-09-19; exact methodological control.  
**Status:** `SYMMETRY-ONLY CLOCK UNIQUENESS REFUTED; NO NEW OWNER — STOP / FORK`.  
**Route state:** no A0/A1/A2 or T0–T3 evaluation; formal `UNASSIGNED`; B `NOT INVOKED`.

## Abstract

We test a specific proposed justification for the uniform clock of the
complete witness-scan graph: invariance under all of its directed graph
automorphisms. Even allowing permutations of numeric labels and parallel
edge identities, every such automorphism fixes each hub and its scan port.
Both the uniform measure and the previously frozen nonuniform comparator
are invariant, including their induced groupoid and time actions. They
give different least times on the same prime packets. Thus this symmetry
requirement alone cannot determine the clock. The result is a bounded
admission control, not a new dynamical candidate or a universal refutation
of arithmetic naturalness. Three parallel architecture lanes produced no
new complete owner. The positive engineering theorem of 276 is preserved.

## 1. Scope, identity and lineage

The [version-1 screen card](candidate-card.md) freezes this question before
the proof. The only dynamical definitions used are the unchanged main
owner U=`ANG-20260919-WSI01` and its separately declared WEIGHT comparator
W in [276](../276-witness-scan-index-flow/candidate-card.md). SYM01 denotes
this comparison screen, not a newly claimed arithmetic flow.

| Item | Exact scope |
| --- | --- |
| Source and paths | 276's entire all-integer graph; all roots, marks, scans, escape ray and infinite paths |
| Symmetry being tested | All directed incidence automorphisms, with vertex and edge bijections; numeric labels need not be preserved |
| U measure | Root mass 1; H_n edge probabilities 1/n; deterministic probabilities 1 |
| W measure | Root mass 1; H_n port 0 probability 1/2, other ports 1/[2(n−1)]; deterministic probabilities 1 |
| Arrows, clocks and time | Same full prefix-arrow definition for each owner; each uses its OWN image derivative and real extension |
| Not introduced | No new symmetry arrows, quotient, state restriction, roof, geometric lift or analytic owner |

The lineage remains prime/composite tests -> arithmetic source updates ->
marked paths -> clock-ownership control. The actual source updates and
complete prime-only packet ledger are not being replaced or re-scored.
Classical symplectic and later analytic fields are NOT APPLICABLE / NOT
SUPPLIED for this screen. The question is only whether FULL GRAPH
SYMMETRY supplies the missing clock-uniqueness justification.

## 2. Definitions and exact graph invariants

For self-containment, the vertices are H_n (n>=2), S_(n,d) (n>=3,
2<=d<=n−1) and E_k (k>=0). H_n has n distinct marked edges. Port 0
goes to S_(n,2), except at H_2 it returns to H_2. Nonzero j goes
to H_gcd(n,j) when the gcd is at least 2, otherwise to E_0. A scan
goes to H_d on a divisor hit, otherwise advances d, returning to H_n
after its last nondivisor test. E_k goes to E_(k+1). Incoming and
outgoing degrees count edge identities, not just different neighbors.

An automorphism a is a pair of bijections on vertices and edges such
that a preserves both ends of every edge. No preservation of an
integer name, root label or port value is assumed.

### Proposition 1 — the scan port is fixed by every automorphism

Every a fixes every H_n and its port-0 edge. It may permute some
other edges or scan roots; no full automorphism-group classification
is required.

**Proof.** H_n is the UNIQUE vertex of outgoing degree n, for each
n>=2. All scan and escape vertices have outgoing degree 1. Thus
a(H_n)=H_n without any label-preservation assumption.

For n>=3, the target S_(n,2) of port 0 has outgoing degree 1 and
incoming degree exactly 1: its only incoming edge is H_n's port 0.
Every nonzero port has a different target type. A target H_g has
outgoing degree g>=2; E_0 has outgoing degree 1 but infinite incoming
degree, since mark 1 at every H_m enters E_0. Therefore port 0 is
the unique outgoing H_n edge whose target has both degrees equal
to 1, and a fixes that edge. At H_2, port 0 is instead the unique
edge from H_2 to itself; the other edge goes to E_0. It too is fixed.
All these statements include composite hubs and every retained root.
QED.

This is stronger than the observation that a fixed port label has
a different probability: the graph itself distinguishes this port,
even after every numeric label is allowed to move.

## 3. Two invariant measures and two different clocks

Let X be all rooted infinite marked paths and sigma the edge shift,
as in 276. A graph automorphism acts edgewise on X, mapping X_v to
X_(av), taking finite cylinders to finite cylinders, and commuting
with sigma. This action is a homeomorphism in the rooted cylinder
topology; it does not require sigma to be onto.

### Proposition 2 — both measured owners preserve the full symmetry

Every a in Aut(E) preserves both U and W measures. It induces an
automorphism of each owner's prefix groupoid and real extension,
preserves that owner's continuous image clock, and commutes with
physical time. No new groupoid equivalence is imposed by this fact.

**Proof.** For U, every edge weight is reciprocal outgoing degree,
an incidence invariant. For W, Proposition 1 fixes each H_n and its
port 0; its remaining edges may permute, but all have the same weight
1/[2(n−1)]. Every other vertex has a single edge of weight 1. Thus
in either owner every edge and its image have equal probability.
The root masses are all 1. A finite cylinder's mass is the product
of these edge probabilities, so a preserves cylinders and then the
whole Borel measure. The countable rooted coproduct causes no change
to this measure-uniqueness argument.

The groupoid map is (xi,l,eta) -> (a xi,l,a eta). It preserves the
tail-equality condition, composition, inversion and prefix topology.
For an owner's prefix probabilities P_alpha and P_beta, the Borel
IMAGE ratio on beta zeta -> alpha zeta is

    J = P_alpha/P_beta,       c = −log P_alpha + log P_beta.

This follows by prefix insertion in the root measure, first on
cylinders then on Borel sets; common tail refinements cancel. The
probability products are preserved by a, hence so is c, including
its continuous values on null paths. Consequently (xi,u)->(a xi,u)
and (g,u)->(ag,u) preserve the extension arrow from (eta,u) to
(xi,u+c(g)). They commute with all real translations. QED.

### Corollary 3 — symmetry-only uniqueness fails

U and W satisfy the SAME complete graph-symmetry requirement but
are distinct measures. On the same prime-scan packet their least
positive times are, respectively,

    T_U(p)=log p,             T_W(p)=log 2.

**Proof.** Already the port-0 cylinder at H_3 has U mass 1/3 and W
mass 1/2. The entire path and base-isotropy classification in
[276, Propositions 1–3 and Theorem 5](../276-witness-scan-index-flow/paper.md)
applies to this identical graph, not a new or selected source: every
path eventually escapes or repeats one prime scan C_p, of least edge
length p−1, and there is one packet per prime. A complete turn meets
one hub port 0 and otherwise deterministic edges. Its probability is
1/p under U and 1/2 under W. The positive-lag isotropy generator
therefore has the stated positive clock; its multiples give all
returns and rth repetitions. Finite prefixes cancel. All phases,
parallel marks and null periodic paths remain. QED.

At p=2 the times coincide, a useful control; p=3 already distinguishes
them. For W, equal times at different primes do not merge packets:
their marked tails still cannot agree. Neither measure is being
substituted into the other owner's conclusion.

## 4. A general admission test for port-transitivity arguments

For any directed graph and vertex v, let R_v be the outgoing edges
e for which some finite directed path after e ends at v. An empty
continuation is permitted when e is already a self-loop. Every
automorphism fixing v preserves R_v, since it transports a return
path to a return path and its inverse gives the converse.

Therefore an automorphism stabilizer cannot act transitively on
the outgoing edges if R_v is a nonempty proper subset. At a prime
hub of 276, port 0 returns whereas all nonzero ports enter the
nonrecurrent escape ray. A regular action on the abstract residue
labels thus cannot be assumed to extend to a v-fixing automorphism
of the complete source graph. Proposition 1 gives the stronger
all-hub obstruction actually needed here.

This is a necessary condition for one symmetry argument, not a
classification of arithmetic actions. It does not rule out a
specified stronger category, covering correspondence or external
normalization principle. Such a proposal must state its actual
state/edge action, compatibility and clock consequence; it cannot
be supplied by the word canonical alone.

## 5. Breadth dispositions and limitations

The [scout record](evidence/scout-record.md) preserves three bounded
lanes: finite-quotient/deck symmetry; saturated flags and local
factor exchanges; and one source-backed reversible-computation
geometric realization. Each collided with an existing owner or
lacked a complete new arithmetic source/time definition. No new
main candidate was admitted. These are bounded search findings,
not a proof that the architecture classes are impossible.

The decisive result here is **failure of graph-symmetry-only clock
uniqueness**. It is not failure of 276's engineered clock, not a
general theorem that natural clocks cannot exist, and not evidence
for an alternative preferred weight. Root-mass normalization and
all source/arrow data were held fixed. No new parameter family,
automorphism census, coarse topology claim or T3 rescue was pursued.

Portfolio: **stop the symmetry-only uniqueness argument / fork**.
Future admission needs a genuinely stronger arithmetic compatibility
condition that distinguishes the declared weights, or a different
full source/time mechanism. Merely adjoining automorphism arrows or
quotienting paths would change the owner and requires a new card.
The global research objective remains open; this screen is not a
replacement success criterion for it. 241/242 remain paused.

## Evidence, gates and disclosure

This is an exact incidence/cylinder proof with no numerical input,
cutoff, orbit search, fitting or empirical generalization. Its two
measured-owner ledgers remain separate and intact. The methodological
screen receives no A0/A1/A2 or T0–T3 coordinates. Formal coordinates
remain UNASSIGNED and Route B NOT INVOKED.

AI assistance was used for construction of the argument, comparison
and writing. ARS freeze-first and three-checkpoint internal model
review organize the work; they are not external peer review, formal
verification or guarantees of independent errors.

- [Frozen screen and appended decision](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Inputs, hashes and document verification](evidence/README.md)
- [Parallel scouts and primary-source boundary](evidence/scout-record.md)
- [Raw-card, manuscript and adverse review](evidence/independent-review.md)
