# Independent internal review — WSI01

**Candidate:** `ANG-20260919-WSI01`. **Date:** 2026-09-19.
**Reviewed status:** `OWNED PRIME PACKETS AND INDEX CLOCK; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.
**Verdict:** PASS for the scoped engineering theorem and its adverse controls.
No blocking error or required manuscript change was found. Natural A0,
classical geometry, coarse-circle embeddings and T3 are not established.

## Inputs, procedure and independence limits

| Input | SHA256 |
| --- | --- |
| Original version-1 card, read before the manuscript | `c2ed49305777d01985556bdc7eaef02945abd90f2895c05a6c31e31cefc654ed` |
| Manuscript reviewed | `c7ea7f73f05104f3b388b134b982a5de7c0c04bb470ac98f5c349bcb11e605ce` |

The reviewer read the raw card first, independently derived the complete
path/cycle, measure, image-clock, return and control results, and sent
them before reading the manuscript. Checkpoint 2 is a subsequent full
manuscript comparison, not claimed blind at every stage. A bounded
auxiliary model check received only the graph and comparator definitions,
not files or manuscript; it corroborated the reviewer's control and
missing-predecessor conclusions. No earlier candidate supplied a proof
premise or a clock for this new owner.

ARS academic-research-suite's deep-research devil's-advocate procedure
organized the three checkpoints. No numerical experiment, cutoff census,
new candidate, coarse-space classification, operator or T3 construction
was undertaken. Hash checks bind documents, not scientific runs. Shared
model lineage and context limit this internal review: it is not external
peer review, human certification, formal proof checking or evidence of
independent error processes. The raw-card hash binds the original
definition, not any later administrative outcome appended to that file.

## Checkpoint 1 — independent raw-card derivation: PASS

**All roots and all cycles.** Every scan takes finitely many steps to a
hub. Every nonzero hub port either enters the escape ray or reaches a
strictly smaller integer hub. A composite hub's port-0 full scan also
reaches a strictly smaller hub. At a prime p it returns along the unique
marked cycle C_p, whose least edge period is p−1, including H_2's
port-0 self-loop. There is only one occurrence of H_p in that word.

A retained late scan root may miss an earlier divisor and return once
to its composite H_n, but the next port-0 excursion restarts at 2 and
hits a divisor. Other ports descend or escape. Thus such roots create
no omitted composite cycle. Along an infinite nonescaping path there
can be only finitely many strict hub decreases; afterward it repeats
one C_p. Escaping paths instead have strictly increasing E indices.
These two alternatives exhaust all infinite marked paths. Parallel
nonzero ports cannot create cycles because they descend or escape.

The declared small controls obey this proof: H_4 and H_6 scan first
to H_2; S_(6,3) and H_6's mark 3 can reach H_3. Neither returns to
a composite cycle. Arbitrary roots beyond the first witness are not
deleted or identified with the root at H_n.

**Full topology and shift.** Finite nonempty branching gives compact
metrizable root spaces and compact-open prefix cylinders. Their
countable coproduct is locally compact Hausdorff and second countable.
The path classification also makes X countable: each path is a finite
prefix followed by a prime-cycle phase or an escape tail. Sigma is a
homeomorphism from each first-edge cylinder onto its target root space.
It is not onto. Its missing root components are precisely those at
S_(n,d), 3<=d<=n−1, with d−1 dividing n; the only possible predecessor
instead takes its witness edge. All paths from such roots are retained.
Other late scan roots can have a predecessor while remaining unreachable
from their own hub. The manuscript's S_(6,3) example correctly suffices
to establish non-surjectivity without confusing these two distinctions.

**Measure strata.** Consistency of equal child weights gives rooted
Borel probabilities. Their sum is sigma-finite, locally finite, Radon
and full-support; compact sets meet finitely many root components.
Let A be paths that eventually enter the escape ray. Their singleton
is a cylinder after that entry and has mass 1/D_alpha>0. A path
eventually repeating C_p has cylinder masses decreasing by p^(-r)
over r turns, hence zero singleton mass. Since X is countable, the
entire complement of A is null. A is open and dense: every prefix can
finish its scan to a hub and use mark 1 to escape, or is already on E.

Thus this full-support measure is purely atomic but not positive at
every point. The positive-atom obstruction applies on the invariant
discrete set A only. With L(xi)=−log mu({xi}), its restricted clock
is L(range)−L(source). This does not remove the retained null prime
tails or imply an everywhere-defined potential on the full owner.

**Groupoid and Borel image clock.** Prefix pairs with a common terminal
vertex give compact-open bisections. Equal-lag intersections refine
both prefixes by the same word; inversion swaps prefixes and matching
the middle prefixes gives composition. Source, range and lag separate
different triples, proving the asserted Hausdorff étale topology. No
onto shift or globally invertible shift is needed.

For any Borel tail set B at v, the cylinder rule extends to
mu(alpha B)=mu_v(B)/D_alpha. Therefore beta zeta -> alpha zeta has
J=D_beta/D_alpha and c=log D_alpha−log D_beta. Equal-lag presentations
differ by a common tail enlargement whose factors cancel. Refinement,
units, inverses and the cocycle law follow, with the frozen eta-to-xi
orientation. The clock is constant on each prefix bisection. Full
support makes its continuous image-density version unique, including
at periodic null points; no positive singleton mass is assumed there.

The real extension on G×R is locally compact Hausdorff and étale.
Physical translation is jointly continuous and defined at every real
time. Scan and escape edges have zero clock; completeness does not
mean a positive-edge roof or a theorem about elapsed scan runtime.

**Entire return and packet ledger.** On A, the escape tail is not
eventually periodic, so base isotropy and H are trivial. On a path
eventually following C_p, the isotropy lags are exactly (p−1)Z. The
finite transient cancels; one cycle has one degree-p hub and otherwise
degree-one vertices. Consequently its lag r(p−1) has clock r log p,
H=(log p)Z, and the least positive time is log p. The clock has
trivial kernel on this isotropy, so extension fixed-object isotropy
is trivial at every object, including the escape stratum.

Same-prime phases and finite prefixes are related by actual tail
arrows; physical time aligns their real coordinates. Different prime
cycles never have equal shifted marked tails. All escape tails do
agree after aligning their E indices. Hence there is exactly one
cyclic time packet per prime and one noncyclic time orbit. Transient
parallel marks remain different paths but not additional packets.
The full clock is not an endpoint difference: such a difference would
vanish on isotropy, whereas the C_p generator has value log p.

## Checkpoint 2 — manuscript comparison and comparators: PASS

The complete manuscript agrees with the preceding derivations. In
particular Theorem 5 uses minimal marked-edge periods, not periods of
the degree sequence; no shorter time is assigned by dividing scan length.
Its packet equivalence is actual arrow/time equivalence, not equality
of lengths. The stated abstract orbit set is one R orbit plus one
R/((log p)Z) orbit for each prime. The manuscript correctly does not
impose a disjoint-union topology on that set or claim that its packets
embed as Hausdorff circles in the coarse quotient. That geometry stays
OPEN; no further coarse-space result was needed for this review.

The three separately frozen comparators have the following exact scope:

| Comparator | Independent finding | Limit of the inference |
| --- | --- | --- |
| SOURCE-OFF | All scan tests false gives exactly C_n for every n>=2, least edge period n−1 and uniform-weight time log n. Nonzero ports still descend or escape. | Witness execution removes composite cycles in this design; the comparator does not replace WSI01. |
| WEIGHT | Let P_alpha be its own product of edge probabilities. Its image ratio is P_alpha/P_beta and clock −log P_alpha+log P_beta. Each C_p contains one port-0 choice of probability 1/2, so every distinct prime packet has least time log2. | The same graph does not force the main uniform measure's log-prime times. Equal times do not merge packets, and this is not a retiming credited to the main owner. |
| PREDICATE | With h(n,2)=1_(n not in K), all other h=0 and 2 in K, cycles are exactly C_n for n in K, with uniform-weight time log n. Excluded hubs descend to H_2; late scan roots cannot restore their cycles. | This is arbitrary-set encodability of a comparator family. A noncomputable K gives a mathematical graph, not a computable algorithm or endogenous generation of K. |

The main predicate remains ordinary computable divisibility, not a
supplied prime-indicator table. The controls do not invalidate the
exact main theorem, but they do prevent deriving natural arithmetic
necessity merely from its matching packet list. They do not prove that
every possible future justification of these choices is impossible.

The cited [Sims graph/local-homeomorphism examples](https://www.aidansims.com/papers/Sims2017.pdf)
were directly checked in the preceding source review and retain only
their terminology role here. Their opposite graph source/range naming
is noted correctly. The current proofs do not borrow an operator result
or an earlier candidate's measure, clock or cycle classification.
Historical comparison descriptions were not used as proof premises;
this review does not grant a literature-novelty claim.

## Checkpoint 3 — final adverse checks and verdict: PASS

| Strongest objection | Resolution |
| --- | --- |
| A scan root after a missed divisor might create a composite loop | It can return to H_n once, but restarting the full scan forces descent; no hub can increase to close a mixed cycle. |
| Parallel exits or transient prefixes might multiply prime packets | Marked paths remain distinct, but eventual equal tails give actual connecting arrows. |
| Pure atomicity might force zero clock on all states | Positive mass holds only on the conull escape set; periodic paths are retained null states. |
| Null clocks might be arbitrary | Full-support continuity fixes the image-density version on every bisection. |
| The non-onto shift might invalidate the groupoid or omit roots | Prefix maps are local homeomorphisms on the entire source; missing-predecessor roots are retained. |
| A cyclic stabilizer might prove an embedded classical circle | Only the abstract homogeneous R-set is established; coarse topology and embeddings remain OPEN. |
| Exact prime packets might close natural A0 | SOURCE-OFF, WEIGHT and PREDICATE separate executed selection from unproved necessity of the architecture and measure. |

Required changes: **none**. Retain a **scoped advance** for the complete
owned source, index clock and prime-packet theorem; **stop natural-A0
promotion and fork** the search for justification of the design choices.
The same-object ledger remains intact, including all roots and null
states. T0–T2 are owner-level labels only; T3 is NOT SUPPLIED / NOT
PURSUED. Classical fields are NOT APPLICABLE, formal coordinates
UNASSIGNED and Route B NOT INVOKED. No enlarged authorization follows
from this internal review.
