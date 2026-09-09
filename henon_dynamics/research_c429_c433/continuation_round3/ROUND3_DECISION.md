# Round 3 decision: one admitted full contract and uniform local inertia

2026-09-09 UTC. Coordinator adjudication of the frozen round-3 proofs,
eleven completed nonauthor mathematical/admission review records, and
the separate source audit. Research continues in round 4; this is a
saved result checkpoint, not a final handoff or a completed-paper claim.

## Outcome

**PC424-L is proved and admitted as one integrated contract.** The
original all-odd-prime/all-parameter polynomial ordinary-cycle equality
is not weakened. Both its independent mathematical checks and the
additional source/substantiality check pass. The finite-detection
corollary is part of that same result.

**All-level local small-cycle inertia is proved.** For every odd p and
every e≥1, the canonical degree-p^e factor for P_s=(1+s)z+z² over
k((s)) is irreducible with full cyclic inertia C_(p^e). Its oriented
first AS quotient stabilizes from level two, while the prime-level
field meets every higher field trivially. These results do not prove
the original global dynatomic component classification.

The remaining accepted round-3 results are auxiliary construction
boundaries and Fricke reductions. No other contract is admitted here.
Current batch totals are **1/5 admitted contracts; 0/5 completed papers**.
There were **zero round-3 mathematical executions**, zero manuscripts,
zero PDF builds and zero formal evaluations. The three actual round-2
executions remain three; theorem deductions from them are not new runs.

## 1. PC424-L: complete original closure, not a nilradical shortcut

The [complete proof](a1_periodic_normal_form/PROOF_PACKAGE.md) proves

    K_c = {Q∘(x²+c)−Q : Q∈k[x]}

for every odd p and every c∈k=algebraic closure of F_p, with K_c defined
using every ordinary primitive cycle and each distinct point once.
There is no restriction on degree, parameter, period or periodic-root
multiplicity. The equality branch fulfills the original contract.

The new coefficient is [P_E](P_all H_n(v)), not the previously proved
[P_E]H_n(v). Exact one-circuit carry reduction, localization of its
contributing sources and insertion/deletion of a forced weight-one
transition prove its stabilization for n≥3 floor(log₂D)+4. Combined
with the inherited leading coefficient and necessary Jacobian
annihilation at adjacent levels, it eliminates every positive normal
defect. Fixed points eliminate constants.

No single-level converse to Jacobian annihilation is used. In
particular, the old counterexample and all nonreduced return algebras
remain valid. The result bypasses, rather than proves, the earlier
unresolved algebraic-transfer and multiplicity-growth mechanisms.

For degree cap M≥1, return levels n=3 floor(log₂M)+4 and n+1 provide
an exact certificate. A failed test yields a detecting ordinary
primitive period dividing one of those integers. The bound 32 M³ is
on the two iterate polynomials, not an asserted optimized runtime.

E2's [436-line independent derivation](reviews/e2_carry_independent/REVIEW.md)
did not read A1's new proof or E8's review. E8's
[281-line full-author review](reviews/e8_carry_stabilization/REVIEW.md)
covers the entire proof and later finite corollary. Both report zero
mathematical must-fixes. The coordinator read all 444 author-proof
lines, both complete reviews, and the compact author report.

X2's [source report](reviews/x2_pc_l_sources/REPORT.md) and the
[coordinator synthesis](NOVELTY_CHECK_PC_L.md) explicitly subtract
classical residue/normal-form/Jacobian formulas, finite binomial matrices
and comparison of successive weighted traces. B1 independently checked
the original contract, proof and closest sources, then read back the
entire final source synthesis. Its
[337-line admission review](reviews/b1_pc_l_admission/REVIEW.md)
qualifies exactly one substantial result, with zero open required repairs.
The coordinator read that entire final review including its final delta.
The actual admission is recorded in
[ADMISSION_DECISIONS.md](../ADMISSION_DECISIONS.md).

The source gate is bounded and access-limited, not worldwide priority
certification. No first-ever finite-Livšic claim is made. The historical
external cross-model example in novelty-check was not run; the authorized
current-team fallback is recorded explicitly and is not called cross-model.

## 2. Uniform local inertia: three separately reviewed steps

The frozen [interlevel supplement](a3_interlevel_contacts/PROOF_SUPPLEMENT.md)
first proves a contact-degree criterion. Differentiating the prime-level
quotient identity then gives, for every e≥2,

    v(alpha_e−beta_1) = 2(p−1)²/p²,
    [K(alpha_e):K] ≥ p²,
    v(P_s^p(alpha_e)−alpha_e) = 2(p−1).

The contradiction uses a possibly noncyclic compositum and the first
upper break of its prime-level quotient. It does not infer extension
degree from native period alone. In particular, M_2 is irreducible for
every odd p, with no AS-computation or discriminant premise. The separate
discriminant-only pair control is correct but unnecessary for this
uniform theorem. The proposed higher exact-denominator shortcut is
actually false and remains recorded as such.

E6's [348-line interlevel review](reviews/e6_interlevel_contacts/REVIEW.md)
passes all those claims. The coordinator read the complete 319-line
supplement and the entire review.

The new [199-line all-level proof](a3_interlevel_contacts/FULL_LOCAL_INERTIA.md)
then compares every higher cycle with level two. Each has exactly p
top clusters at the threshold 2(p−1)/p. The level-two multiplier has
valuation 2(p−1)(2p−1); the derivative-ratio identity makes the average
cross contact exceed the threshold. One close pair and its native shifts
give a canonical matching of all p clusters. Galois equivariance and
the cyclic p-group embedding force the higher image to be full.

This uses existence of a deep contact, not equality of all cross
contacts, a guessed high-level ramification pattern, or full-field
nesting. E6's separately allocated
[308-line full-inertia review](reviews/e6_full_local_inertia/REVIEW.md)
passes with zero open repairs; the coordinator fully read both proof
and review and accepts the all-p/all-e local theorem.

The separate [oriented-quotient proof](a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md)
uses native equivariance as well as Galois equivariance. The designated
one-step +1 action fixes the scalar ambiguity, so [a_e]=[a_2] in
K/wp(K) and the degree-p subfields F_e=F_2 for all e≥2. A Hasse–Arf
congruence contradiction also proves L_1∩L_e=K. At p=3 only, the old
certified class 2s^(-4)+s^(-2) consequently holds for all e≥2.
Neither general-prime explicit coefficients nor full-field nesting
are asserted. E2's separate
[336-line corollary review](reviews/e2_oriented_quotients/REVIEW.md)
passes; the coordinator read the full corollary and entire final review.

All three local stages are now accepted at their exact scope. The
original global PC424-D still asks about all geometric components;
transitivity among global native cycles is not supplied by rotating
one local cycle. A4's next task retains that gap. An independent
source/substantiality scout for the all-level local theorem is allowed
to reject standalone admission; it cannot relabel the global contract.

## 3. Other reviewed auxiliary claims

| Lane / final nonauthor check | Accepted increment | Explicit remaining boundary |
| --- | --- | --- |
| A2 / [E1](reviews/e1_graph_complexity/REVIEW.md) | Linear degree obstruction for additive-separated transfer equations and generic finite-data incidence bounds, including cycle constants and vertical factors. | This package did not construct a transfer for a fixed globally admissible h. PC424-L is now closed by A1's different proof; the historical graph review remains unchanged. |
| A4 / [E4](reviews/e4_primitive_collision_budget/REVIEW.md) | Exact cut-support/discriminant identities and an infinite n=3^e collision-budget obstruction: primitive multiplicity M≥2n exceeds the complement-contracted graph's minimum cut; discriminant valuation ≥2n−1. | Excludes only an arbitrary-deletion-budget certificate. Does not show actual colliding labels contain a cut, or prove reducibility/CUT/GQ. |
| B4 / [E7](reviews/e7_branch_discriminant_bounds/REVIEW.md) | Exact branch-contact ledger, slope-forced normalization index and degree-p integral basis; the two specified scalar upper bounds stay above the accepted lower threshold. | Does not exclude interlevel information. A3's now-proved full-inertia route is compatible with this method-specific boundary. |
| C4 / [E5](reviews/e5_smooth_fold/REVIEW.md) | Irreducible finite-chart critical hypersurface/global fold, all-smooth-base fixed-scheme finite flatness, complete period-two-germ isolation and residual normalization criterion. | SF2 still needs to exclude normalized ramification at finite genuinely higher-period points. Neither constant length nor one colliding germ proves this. |
| D2 / [E3](reviews/e3_sign_slice/REVIEW.md) | Complete 1+2+4+4 cycle restriction; exact sign classes [D²−C²] and [C²+4D]; formal symmetry-line blindness; legitimate sufficient specialization; odd paired-cycle characters. | ST/SF2 and actual higher-image character independence remain unproved. Slice degeneracies are not automatically transverse generic-fold witnesses. |

All five final reviews report zero open required mathematical/source
repairs. The coordinator read all five completely. C4's determinant
column-order clarification and exact finiteness citation were the only
review-driven final wording repair here, independently read back by E5.
Accepted FG2 and NI are not reopened or enlarged.

X1's [multiplicity source report](x1_multiplicity_sources/REPORT.md)
does not identify an applicable all-parameter multiplicity theorem.
Its primary-source limits remain useful, but that missing input is no
longer required for A1's proof. No absence-of-theorem claim is inferred
from its bounded search.

## 4. Work receipt and continuation

Round 3 had eight actual author/source-lane allocations. Additional
proof-only supplements stayed in A3's exclusive path. Nine existing
nonauthor threads produced **eleven** final mathematical/admission
review records: E1; E2 twice; E3; E4; E5; E6 twice; E7; E8; and B1.
X2's separate primary-source audit is recorded separately, not padded
into that review count. These are actual tasks and files, not a claim
that every thread was continuously active or used a different model.

The coordinator's source synthesis, finite-certificate proposal, full
readbacks and admission are actual work. No round-3 mathematical code,
old mathematical rerun, PDF build, formal evaluation, external model
upload, new credential or target-arithmetic promotion occurred.

Round-2 records were already synced at
`9623efe900df6003664315099440fa0683930d9b`. This round's proofs/reviews
are frozen for exact-path research-record integration; it is not a
sealed final paper payload. Earlier reports keep their dispatch-time
status, while this decision records the now-closed dependencies.

Concrete round-4 work is already allocated: actual global primitive
collision incidence; remote Fricke parabolic divisors; slice quadratic
exclusion; a complementary Fricke source scout; general-prime first
quotient ramification through two distinct approaches; and local-theorem
source/substantiality assessment. New work has exclusive new paths.
Neither failed methods nor correct auxiliary lemmas automatically fill
the four missing contracts. No five-paper draft plan or manuscript is
claimed complete. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
