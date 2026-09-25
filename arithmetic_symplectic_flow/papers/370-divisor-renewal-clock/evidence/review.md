# 370 — CP2 manuscript comparison and CP3 final-surface review

Candidate: **ANG-20260922-DRE01**.
Candidate status: **OWNED RENEWAL CLOCK; NONPRIME GAP PRIMITIVES — STOP / FORK**.
Review verdict: **CP2 PASS; CP3 PASS within the frozen contract. No mandatory amendment.**
This is internal inherited-model/shared-history review, **NOT_CALIBRATED**, not external peer review.

## 1. Exact inputs and observable chronology

Before manuscript access I read the original card plus CP1 clarification, lines 1–112 through its then EOF:
`f4a1a914d117365671d88e946d75061d525b2065cf6080b88be22a3cc0cc7e8c`.
The original 100-line prefix is `46e18a3aa59d3eebfc744cf858c4b5ca516327d93124281bf47e4cfa2b5a3b08`.
I derived MAIN and all controls, sent findings, wrote and personally read independent-proof.md to EOF,
and froze its 182 lines at `5eff7798106460e6afb4f83e86e261c5c68fde3fb829049bad23a7f5a7f603e1`.
Root then acknowledged reading that proof and separately issued PAPER UNLOCK for this review.

After that unlock I personally read these files completely through their current EOF:

- paper.md, 269 lines: `da4c9a90a23a03395eb182c0deea08939c0489789a52a412b5e727af7f899d17`;
- candidate-card.md, 123 lines: `c959e53667c1a03c66a2b4819f2212ad041801fb4727c39352d9f63fdc20efc1`;
- claim-ledger.md, 42 lines: `2fd9b4230e21d724bd1d662710d506a8d7cf3ce2bc99bdc402827d50d85aa0ef`;
- README.md, 20 lines: `8ff4103abb553c38802b38cd8504610dbd9326d30505299e57510fe2ccb60047`.

All hashes are SHA-256. Manuscript lines 1–150 and 151–269 were read consecutively, followed by the
complete current card, ledger and README. Appended card outcome lines 113–123 were not raw inputs.
The original 112-line prefix and frozen independent-proof hash were rechecked unchanged.
Independent derivation preceded my manuscript access; this does not establish author-draft blindness,
cross-model execution or independent errors. The card itself disclosed root's prior expectations.
The author-read declarations in the manuscript are provenance statements, not verified private histories.

Applicable ARS instructions were retained. This file supplies CP2 and CP3 after the accepted CP1;
it does not claim that I reread the separate scope report. No peer/scout report, external source,
old scientific file, numerical experiment or auxiliary was used. Only this new review file is written.

## 2. CP2 — source, probability and owner

**Arithmetic law (§2).** Intersecting all tested integer ideals gives L_r K; Haar indices yield
w_d=1/L_(d−1)−1/L_d, with positive support exactly at prime powers. The exceptional zero has Haar mass zero.
The argument uses ideals in the profinite ring, not cancellation of arbitrary zero divisors as in a field.
The tails telescope to S_r=1/L_r, including r=0,1. The manuscript's sharper mean bound is valid:
r and r−1 are coprime divisors of L_r, hence S_r<=1/[r(r−1)] for r>=2 and 2<M<=3.
This r(r−1) proof was checked at manuscript stage; the raw proof used the distinct 6/r^2 bound.
Both prove convergence exactly, without a numerical cutoff or an assumed finite mean.

**Complete source and coding (§3).** The product probability and normalized residual weights define
the declared law on all N_0×D^N. Every finite cylinder has positive mass; w_d<=1/2 proves singleton
nullness without deleting those states. Arbitrary residuals and unbounded sequences of finite gaps remain.
The bit coding recovers the first waiting time and every subsequent finite gap. Its exact image has
infinitely many ones with allowed successive distances; neither the all-zero point nor finite-one
boundary sequences are silently restored from a compact closure.

W exists at every target, E precisely when r+1 is allowed. Direct substitution and the positive/zero
residual partition prove exhaustiveness and surjectivity. There is no terminal or omitted predecessor.
The manuscript's Borel claims suffice; the raw proof's stronger continuity statements need not be added.

**Every-Borel IMAGE (§4).** Taking arbitrary Borel residual sections gives the W and E image integrals
with the actual conditional probabilities. This verifies more than cylinder masses or total branch weights.
The two derivatives are finite and positive on their full domains, including null periodic histories.
Their branch sum equals one, proving invariance of the source probability, not an invariant physical-flow measure.
The all-point versions are frozen prescriptions; a.e. derivative uniqueness alone is not being promoted
to a statement about the clock at null periodic states.

**History clock and all kernels (§4).** The step signs and the telescoping identity
A_m=V(T^m x)−V(x)−log P_m agree with the inverse IMAGE orientation c=−log J.
Common-tail extension cancels the same terminal contribution; witness alignment proves composition.
Every-Borel finite-history change of variables establishes the replacement law on its actual chart.
Identical retained-lag triples are identified, but integer lag is not discarded.
Equation (7) gives necessary and sufficient tests for the full clock kernel, lag kernel and intersection.
These are full arrow tests, not only tests on isotropy. The raw proof's examples showing that MAIN's
two kernels contain neither one another are consistent with (7), though not required as extra paper examples.

## 3. CP2 — complete returns, incoming and phases

**Full incoming (§5).** Two sources are related exactly when their gap sequences have equal shifted tails,
with arbitrary finite residuals. Advancing to an event proves both directions. The union of all inverse
generations and the finite-prefix description cover the entire source orbit, not merely the literal cycle.
The raw depth-by-depth predecessor formula is a more explicit equivalent description, not a missing owner.

**Isotropy versus literal periods (§5).** Eventual gap periodicity is the exact nonzero-isotropy criterion.
For a primitive gap word delta, the listed states 0<=r<d_(j−1) give the whole literal periodic core.
Event positions force the least source period P_delta=sum d_j, rather than the number of gaps.
Every ancestor has isotropy P_delta Z even if it has no literal point return. The core clock telescopes
to B_delta=−sum log w_(d_j)>0, so H=B_delta Z and the isotropy clock kernel is trivial.
Extension isotropy is consequently trivial; noneventually-periodic tails instead have both groups zero.
The manuscript's abbreviated references to aperiodic tails are read with this explicitly stated eventuality criterion.

The phase h+c(y->a), or h−A_n(y) when T^n y=a, has the correct sign. It includes all heights and
incoming histories. The orbit fiber is R/H as a SET; no Hausdorff quotient or embedded-circle theorem follows.
Distinct primitive gap necklaces cannot share an eventual tail, hence cannot merge even at equal clock values.
One packet per primitive necklace and repetitions on that same packet give the entire positive-return ledger.

**Frozen tests (§5).** All four words are legal, primitive and mutually distinct. Their least source periods
are 2,3,4,5 and least physical times log2, log3, log12, log6. The latter two are not repetitions
of a prime packet; each violates the clarified pre-analysis target on its whole source orbit.
No post-test rescaling, representative selection or null-state deletion is used.

## 4. CP2 — three own controls

**GEOMETRIC (§6).** Its own tails are 2^(−r), mean two and residual masses 2^(−r−1).
Both inverse charts are global and have IMAGE 1/2 on every point, giving invariance and c=lag·log2.
All three kernel sets in question equal the lag-zero tail relation, including nonidentity arrows.
Its binary carrier still requires infinitely many ones. Primitive positive-gap necklaces have source
isotropy P_delta Z and H=P_delta log2 Z, with trivial extension isotropy and complete incoming/phases.
The all-zero binary boundary contributes no extra fixed packet.

**DETERMINISTIC (§6).** The source has exactly two equally weighted states, exchanged by the map.
W and E each exist only on their specified singleton target, and the unique full inverse has IMAGE one.
All clocks vanish: source and extension isotropy are 2Z, H=0, the clock kernel is the whole groupoid,
and the lag kernel/intersection are units. The two-state source cycle gives a free physical line, not a period-two flow.

**REINDEX-OFF (§6).** The whole MAIN measure is retained but the evolution is identity, with IMAGE one.
All (x,k,x) remain as distinct arrows. Source and extension isotropy are Z, every H is zero,
the full clock kernel is the groupoid, and lag kernel/intersection are units. Each source orbit is
a singleton with all real height phases. Neither MAIN's return packets nor its clock is transferred.

## 5. CP3 — strongest alternatives and final surfaces

The strongest positive case is genuine: a complete stationary probability and its conditional clock exist,
and the first two tests have the intended prime times. Neither fact removes the other primitive packets.
Changing the law or null-path versions, taking selected histories or reclassifying mixed gap words as
repetitions would change the frozen problem. The negative result is not a universal no-go for renewal sources.

The residual graph has infinitely many outgoing choices at zero, stationary root masses S_r/M, and
freely concatenable event excursions. These intrinsic facts and the actual mixed packet were checked here.
The manuscript's description of 364's specific hypotheses is author-reported: I did not reopen that card.
No 370 proof imports its theorem, and no finite-outdegree theorem is applied to this infinite-outdegree graph.
Thus nonproduct bit observations are not offered as proof of escape from return-word splicing.

The four surfaces agree on candidate, STOP / FORK disposition and the precise positive/negative boundary.
The original OPEN card is preserved separately from its appended outcome. T0 and declared T1 ownership
do not establish strong naturalness, which remains OPEN. T2's frozen prime-time target fails; T3 is
NOT AUDITED, classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED and Route B NOT INVOKED.
No physical invariant measure, geometric quotient, prime coverage or novelty certificate is claimed.
Batch-link existence and package-wide mechanical QA remain root's task, not a mathematical premise.
No mandatory correction or unresolved obligation blocks this scoped conclusion. This report is complete and frozen.
