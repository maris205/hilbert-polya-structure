# PSR01 independent source/mathematical review — DA checkpoints 1–3

## Material Passport and scope

Scope: `ASFS-SCOUT-20260919-PSR01`; date: 2026-09-19.
Reviewer: separately executed internal model reviewer `/root/cs09_form_review`.
Calibration: `NOT_CALIBRATED`; no venue-specific review criteria or human verification claimed.
ARS was used for bounded source checking, evidence-first derivation, checkpoint separation and severity calibration.
This is not a full journal-review panel, a new candidate admission, or a Route evaluation.
The caller's instruction against manufactured criticism governs: an empty current-issue list is legitimate.

Checkpoint 1 and the raw mathematical conclusions were returned before reading the root draft or source-audit narrative.
The reviewer directly read the complete original 078/079/081 cards and papers, the PSR01 scope,
and the publisher's primary PDF. The initial task identified the source and relevant seed-condition risk;
this was not a source-blind discovery. No other scout's proposed mathematical conclusions were used as evidence.
Checkpoint 2/3 then compared that committed derivation with the root-authored draft and audit.
Same model family/shared project context remain limitations; separate execution does not prove independent errors.

Inputs at the first checkpoint 2/3 draft review:

| Artifact | SHA-256 |
| --- | --- |
| [Scope card](../candidate-card.md) | `2846d6113903b37a14e182c429f3180e7960841d82a53b2c9ba3d560c6addfe7` |
| [Root draft](../paper.md) | `f2bbca32ae40269a01add71b1bfe5079206494ecdc8fee3c5a49dc293f5709d0` |
| [Source audit](source-audit.md) | `e1acfae57356c0cb0e6db2197e06149850e997f16d906b8d7941769c45cf8b47` |

The six original 078/079/081 card/paper hashes were independently captured before notices;
they match the corresponding six historical hashes in the source audit. This is not a claim that
the reviewer stripped every later notice or audited every downstream file. That preservation QA is separate.
No science run, numerical census, fit, target generation, new roof, deletion, or external upload was performed.
Only this reviewer file was written. Root owns all paper, card, ledger, notice and index edits.

## Checkpoint 1 — scope and method

**Verdict: PASS for the bounded correction audit.**
The question is answerable on the already frozen formulas: classify every periodic state of
G(x,y)=(y,gpf(x+y)) on all positive integer pairs, then retain each old full path carrier and roof.
Direct identities plus the correctly restricted source theorem suffice; a numerical search would not establish completeness.
No new dynamics or geometric admission is required to test the historical claims.

The primary source is Back–Caragiu, *The Greatest Prime Factor and Recurrent Sequences*,
Fibonacci Quarterly 48(4), 358–362, [publisher PDF](https://www.fq.math.ca/Papers1/48-4/Back_Caragiu.pdf).
The setting is a prime sequence; Theorem 3 on printed pages 359–360 requires unequal initial values.
Its broader abstract wording cannot erase that condition. The equal-prime case is idempotent.

The historical “unique cycle on all positive pairs” assertion has a decisive counterexample:
G(p,p)=(p,p) for every prime p, including 2. Nor is “unequal positive seeds” a valid repair:
G(6,2)=(2,2). This invalidates the old exhaustive ledger, not merely an incidental example.
The correction therefore must retain the prime diagonals; restricting the domain would change the owner.
This historical core error was reported at checkpoint 1, not concealed as a minor wording issue.

## Independent raw derivation retained for comparison

After two updates, both coordinates are prime. A periodic point is itself an image under G²
of another point on its orbit, so every periodic state has prime coordinates.
Equal prime coordinates give the fixed points above. For an unequal prime pair already on a
periodic orbit, Theorem 3 forces eventual entry into the four-cycle; periodicity then forces that very orbit.
Thus the full primitive ledger is one singleton per prime plus exactly one nonconstant four-cycle C.

On the full X_G={z:z_(j+1)=G(z_j), j∈Z}, evaluation at zero gives
Fix(σ^m)↔Fix(G^m): a periodic state has exactly one m-periodic extension by cycle repetition.
Additional nonperiodic prehistories cannot give an extra periodic extension with that zeroth state.
Consequently Fix(σ^m) consists of all prime constant paths and, when 4 divides m, the four phases of C.
Each fixed-point set is countably infinite. No claim that all of X_G is periodic is needed or established.
The product-discrete path topology makes X_G closed and the shift a homeomorphism.
Both frozen roofs are continuous and bounded below, so their suspensions have complete two-sided flows.
Closed suspension orbits correspond to shift cycles with the cycle sum as primitive time.

For 079, the full primitive times are 1 for every prime and 4 for C.
Every positive iterate has infinitely many fixed paths, so its ordinary Artin–Mazur coefficients are not finite.
The first-repetition terms already have infinitely many copies of |e^(−s)|, excluding absolute convergence at every finite s.
The old finite factor is only C's contribution. This does not rule out arbitrary separately defined regularizations;
none is supplied, selected or authorized here, and none may be silently called the ordinary full-orbit product.

For 081, the prime paths have primitive times log p; C has time log210 and is not a prime repetition.
The complete product is ζ(s)/(1−210^(−s)) on Re s>1. For σ=Re s>1,
Σ_p Σ_(r≥1) p^(−rσ)/r ≤ (1−2^(−σ))^(−1) Σ_(n≥2) n^(−σ)<∞.
Unique factorization then identifies the prime subproduct with the absolutely convergent Dirichlet series.
This establishes a full ordinary product, not an operator determinant, trace formula, or spectral divisor.
The old “per-prime time absent” statement is false for this chosen roof; the stronger natural-time claim remains unproved.

## Checkpoint 2 — synthesis against evidence

**Verdict: PASS.** No unresolved Critical, Major or Minor issue identified within this scope.

| Stress-tested claim | Draft anchor | Assessment |
| --- | --- | --- |
| Source conditions are narrower than the historical wording | §2; source audit, Primary source | Correct: unequal initial primes, with a separate composite-seed adverse test |
| Periodic classification is exhaustive on the frozen domain | §3, Proposition 1 | Correct two-step prime reduction; all diagonals and C retained |
| The full natural extension is not replaced by selected periodic points | §3 final paragraphs; §4 definition and bijection | Correct; possible nonperiodic pasts are neither classified nor discarded |
| The unit-roof full ordinary zeta is not the C factor | §4 final two paragraphs | Correct infinite fixed-point/repetition obstruction, explicitly limited to ordinary absolute convergence |
| The log-roof product includes every primitive | §5, Proposition 2 | Correct prime Euler product times the unavoidable C factor on Re s>1 |
| Actual log p circles do not establish natural timing | §6 first two paragraphs | Correct separation of chosen log-output readout from an independently derived physical clock |
| Correction is not a new candidate or a transfer of Route credit | §1 and §8 | Scope and owner boundaries preserved |

The synthesis does not cherry-pick the favorable prime factors: it retains the adverse mixed circle.
It also does not overcorrect by denying the genuine prime-indexed periods supplied by the frozen log roof.
The ordinary-product convention is explicit; conclusions do not depend on selecting an unannounced trace or regularization.
The draft uses the primary theorem only for nonconstant-cycle completeness, not as authority for the log clock.

## Checkpoint 3 — final-draft vulnerability review

**Verdict: PASS for the reviewed mathematical/source correction.**
Current Critical issues: none. Current Major issues: none. Current Minor issues: none identified.
The historical error remains consequential, but is resolved in this draft; it is not relabelled as an unresolved defect of266.

**Strongest counter-argument.** The recovered prime family could tempt the programme to announce an
arithmetic dynamical success after simply converting prime labels into prescribed logarithmic times.
It could also tempt an author to divide out C and then call the result the original flow's zeta.
Either move would defeat this correction's same-object purpose. The draft directly answers both objections:
§5 retains the extra factor and rejects deletion/division as an owner-preserving interpretation;
§6 explains that the diagonal roof is exactly a prime-label-to-log readout and does not establish natural timing.
Accordingly this is a genuine source/ledger correction, but not evidence that the main arithmetic-clock programme is solved.

| Final stress test | Result and limit |
| --- | --- |
| Remove the external theorem | Diagonal counterexamples survive, but completeness of the nonconstant ledger is no longer established by this proof; dependence is explicit |
| Replace prime initial conditions by arbitrary unequal positive seeds | False; the draft's (2,6)→(6,2)→(2,2) test prevents this generalization |
| Ignore nonperiodic histories | Unnecessary for periodic counts; the draft retains the full X_G instead of imposing such a deletion |
| Invoke a regularized product to rescue079 | Outside the stated ordinary product; no impossibility claim about every regularization is made |
| Drop C to obtain a pure Euler product | Rejected explicitly; C is primitive and belongs to the frozen full owner |
| Treat the correction as a new natural-clock or Route success | Rejected explicitly in §6 and §8 |
| Ask whether the correction matters | Yes: it reverses a false missing-prime claim and withdraws a false finite-unit-zeta claim without altering the maps or roofs |

## Unassessed surfaces and handoff

No assertion is made about the existence/cardinality of all nonperiodic two-sided histories, arbitrary
regularizations, analytic continuation, new operators, or a conservative realization. These are not needed for the reviewed claims.
The deferred proposal and geometry-screen dispositions in §7 were read as scope statements, not independently
admitted or proved here. No new architecture, theorem contract or computation is recommended by this report.
Comprehensive historical dependency correction and notice-byte preservation remain root's separate document QA.
The draft's explicit source attribution, limitations and AI-assistance disclosure fit this bounded internal review;
the report is not external peer review or independently verified human mathematics.

Handoff: retain the corrected full arithmetic/packet control; stop the invalid uniqueness and finite-unit-product
claims; leave further search to a separately frozen scope. Same-object bookkeeping is intact in the reviewed draft.
Formal Route coordinates remain UNASSIGNED; Route B remains NOT INVOKED.

## Final bounded readback and input rebinding

Root's concurrent updates were read back after the first report: paper status now says the correction is complete;
source-audit corrects its082 historical-hash transcription; the scope appends the bounded correction outcome.
The mathematical proofs, original owners, full ledgers, roofs and convergence/natural-clock limits are unchanged.
This readback introduces no new proof or admission; checkpoint 2/3 verdicts remain PASS.
Root separately reports18 successful stripped-original-text SHA checks; this reviewer does not claim to have rerun them.

| Final reviewed artifact | SHA-256 |
| --- | --- |
| Scope card | `afe3ed4d1b63979bc27f339f02ffd81cfdd38aa1e08a31051963ec1b97264506` |
| Root draft | `0842a064d7d61cc2e20bb11f13b016e6749b8faadcfab7e78027f88d9b7d4253` |
| Source audit | `719d3973bae02e529ca2dc684e591da1bdfcccab1251a1f044187729be6fd20c` |
