# Independent model review — ANG-20260915-MNR01

**Date:** 2026-09-15  
**Candidate ID:** ANG-20260915-MNR01  
**Candidate status:** STOP — OWNED MULTIPLICATIVE RETURN CLOCK; MIXED PRIMITIVES REMAIN.  
**Review verdict:** NO MATHEMATICAL BLOCKER FOUND IN THE SPECIFIED CLAIMS.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Scope and review provenance

Reviewer: the separately dispatched scale_quotient_adversary agent, under
research_controller/multiplicative_norm_carrier. This agent first examined
the proposed scale quotient in a read-only pre-audit, then read the actual
[paper](../paper.md), [frozen card](../candidate-card.md),
[claim ledger](../claim-ledger.md), package summary and evidence index.
The present review is of Propositions 1--4 and the actual status boundaries,
including the author's subsequently added equivalent convergence threshold.

The pre-audit findings were sent to the author before the manuscript was
completed. Thus this is a separately executed technical review, not a
paper-blind test or an assertion of epistemic independence from all author
interaction. The reviewer retained the session's model settings and did not
use another external model, a new numerical experiment or a literature
novelty search. Model review is not human peer review.

ARS claim--evidence--counterargument discipline was used only for this
bounded proof and scope audit. No publication workflow, venue assessment,
operator construction or analytic continuation was invoked.

The reviewed core-file SHA-256 identities were:

| File | SHA-256 |
| --- | --- |
| paper.md | 3ca8ca887ab11a2a581ce5f3c770e5fc2422f69b9fd692fd3c38e0bbe615d4a9 |
| candidate-card.md | ddbcdbab1693dcd325f534d0a3292f6779f9f4eb1cb98b9f02e982e528d91496 |
| claim-ledger.md | 6c84114aed89b5f2bf358575be19c3754d23131eb3892c3a6c9c1d257a784367 |

These identify the reviewed bytes; they do not certify their correctness.
Later navigation-only or review-link edits do not erase this review's
specific proposition-level scope.

## Findings on the actual proofs

### R1 — Derived alphabet and two-sided action

**Finding: supported.** Proposition 1 derives prime ratios from the
absence of an intermediate divisor, rather than presupposing a selected
prime alphabet. The forward and negative-index reconstruction formulas
are mutually inverse with the ratio map, and each coordinate depends on
only finitely many discrete coordinates. This verifies the claimed
homeomorphism and normalized inverse.

The formula G^m(y,r)=(F^m y,r/y_m) is valid for every integer m.
In particular, the negative direction is not omitted when the quotient
is defined. No periodic subsystem is substituted for the complete X.

### R2 — Quotient sign, actual section and complete flow

**Finding: supported.** The sign in G is correct. Applying G to
(y,y_1) gives (Fy,1), so the forward scale flow reaches the next section
after log y_1, not after its negative. Since y_j increases strictly
from zero to infinity, the unique integer k with
y_k<=r<y_{k+1} gives the stated representative after G^k.

The residual positive-scale action commutes with G and therefore descends.
Continuity may be made explicit by observing that the orbit quotient map
is open: saturation is a union of images under homeomorphisms. Its product
with the time line is consequently a quotient map as well. This justifies
the manuscript's inherited continuity statement.

The lower bound log 2 gives non-Zeno crossing times in both directions.
The full product scale flow is already defined for every real time,
so the quotient does not lose an endpoint at infinity. This is distinct
from a roof that is merely positive but tends to zero along an escaping
trajectory.

The Hausdorff argument is valid: in logarithmic height, an m-step move
has displacement at least |m|log 2. Bounded height neighborhoods can
therefore interact through only finitely many group elements, which
can be separated by shrinking neighborhoods. No local compactness,
smooth manifold or classical symplectic conclusion follows from this.

### R3 — Full stabilizers, primitive times and repetitions

**Finding: supported.** The actual paper writes a closed return as
G^m(y,e^t r)=(y,r). With this convention the equations are
F^m y=y and e^t=y_m, correctly forcing m>0 when t>0.
The alternative convention G^m(y,r)=(y,e^t r) would reverse the
index sign; the paper does not mix these two conventions.

If the chain has least positive shift period d, its positive return
indices are precisely rd, and y_{rd}=N_w^r. The smallest elapsed
time is therefore log N_w, with full stabilizer
(log N_w) times the integers. A nonperiodic chain has trivial
flow stabilizer.

All section phases of one periodic chain belong to one closed flow
orbit. Conversely, an intersection with that section changes the
chain by an actual shift iterate. Hence cyclic word equivalence is
exactly the claimed orbit equivalence; scale does not supply an
additional parallel family of closed circles.

### R4 — Mixed words and equal-norm multiplicity

**Finding: supported; decisive negative target result.** The word
(2,3) has least shift period 2 and gives a genuine primitive flow
orbit of time log 6. Its doubled word is a repeated traversal,
not a new primitive orbit. This already triggers the card's
prime-exclusive stopping condition.

The words (2,3,5) and (2,5,3) are both primitive and are not cyclic
rotations. They produce distinct orbits of equal time log 30.
The paper correctly retains both instead of using norm as a complete
orbit identifier. The constant-prime circles at log p remain positive
controls, not the full orbit ledger.

### R5 — Finite time cutoffs

**Finding: supported.** Time at most T bounds the word product by e^T,
the number of letters by T/log 2, and every letter by e^T. Only
finitely many integer letters and finite words meet those bounds.
The reasoning covers repeated returns as well as primitive orbits;
cyclic identification cannot increase that count.

This is a direct all-cutoff finiteness proof, not an inference from
a numerical census. It does not claim a particular asymptotic orbit
count or identify words with equal norm.

### R6 — Ordinary zeta and its exact absolute region

**Finding: supported.** A primitive word of length d contributes
exactly d phase-marked points when counted at length rd. Division
by rd gives the required coefficient 1/r. The proof correctly
uses extended nonnegative sums before permitting complex
rearrangement. Thus absolute logarithmic convergence is exactly
P(Re s)<1, and the full product has Z=1/(1-P(s)) in that region.

The original P(Re s)<1 statement and sufficient region Re s>=2
were already correct. The added h in (1,2), P(h)=1 argument is an
equivalent refinement, not a correction of an earlier assertion
that the entire half-plane Re s>1 was valid.

The actual added paragraph is sufficient: comparison with
sum n^(-1-delta) gives continuity on compact real subintervals
of (1,infinity); P strictly decreases; the finite subsum
1/2+1/3+1/5=31/30 exceeds 1 near exponent 1; and P(2)<1.
For exponents at most 1 the same finite subsum excludes convergence.
The exact absolute-logarithmic abscissa is therefore h without
using prime harmonic divergence or a numerical estimate.

Nothing here supplies a Fredholm determinant, trace, continued
function, target divisor or spectral realization. The paper
expressly stops before those assertions.

## Record correction and disposition

| Item | Observation | Disposition |
| --- | --- | --- |
| E1: control count | An earlier evidence-index sentence said eleven controls, while Section 5 contains ten control rows. | ADDRESSED: the author changed the actual sentence to "All ten controls"; the reviewer reread that sentence. This did not affect any proof or gate decision. |
| E2: threshold formulation | The pre-audit proposed the equivalent threshold h in (1,2). | OPTIONAL REFINEMENT INCORPORATED AND CHECKED: no original convergence-domain error was found. |

No unresolved mathematical correction was identified in the reviewed
contract. This is a bounded review outcome, not a proof that every possible
future claim about the carrier is correct.

## Owner and portfolio assessment

The candidate card, paper and claim ledger preserve the same full X,
integer scale action, roof, primitive convention and ordinary product.
The paper does not import 148's unit clock, 146's arbitrary-unit
stabilizers or a prime-only projected product.

The status STOP is warranted by the intrinsic mixed primitive orbit.
The positive construction and analytic diagnostic are correctly scoped
owner-level T0--T3 results, with scale naturalness OPEN and classical
A0--A2 NOT APPLICABLE. Formal Route coordinates remain UNASSIGNED;
Route B remains NOT INVOKED.

**Recommended handoff:** stop this prime-exclusive architecture and retain
its complete scale-clock and full-word product as controls. Any changed
admissibility rule, constant-word sector, norm character, roof or analytic
owner requires a fresh frozen identity. No such next candidate is
created by this review.
