# CP2 / CP3 final review — ANG-20260922-CEH01

2026-09-22; batch `FULL-TRANSPORT-20260922-G`, round 2/5.
Verdict: `CP2 PASS; CP3 PASS — BOUNDED STOP RECORD, NO REVISION REQUIRED`.
Internal shared-history review: `NOT_CALIBRATED`.

## 1. Authority, actual access and frozen receipts

Root accepted and froze the 257-line card-only raw proof before explicitly
unlocking these four final surfaces. I then read them fully, not merely their
headings or selected claims: paper.md lines 1–125 and 126–234; candidate-card.md
1–93; claim-ledger.md 1–70; README.md 1–37. The returned text reached each
file's final line; wc independently confirmed those EOF counts. No output was
truncated. All four measured hashes match the values supplied with the unlock.

paper.md — 234 lines — SHA256 e08c35648316d20bafe118af546597725caefeb79264e203cdccf63b6c7d6060
candidate-card.md — 93 lines — SHA256 808e494b4a985645c5e36693c99f7133a7d724c6c3e4b63c53b4fc97f705c03b
claim-ledger.md — 70 lines — SHA256 d82bfb5eefeba503135568dbc7bceecc073321ec5232aa4ae9bc36fa5313c059
README.md — 37 lines — SHA256 49bdc0c79bd6fb1507c5c116006ee7b8cf38366c4999fe291cfd58472d32eb9f

The original card prefix was recomputed with `head -n 61 | sha256sum` and
matches the scientific input used for CP1 and the independent raw derivation:

candidate-card.md (original lines 1–61) — SHA256 02da94469ed3289591c192ad93e7f5080ad67b843da9f7f1bc175c0562504136
scope-review.md — frozen 74 lines — SHA256 d7be72329d182920dcc3b39d212b31e10c36ce81b27cf29ad5ce29ff26e563cb
independent-proof.md — frozen 257 lines — SHA256 6987fb6756d95e6364fbc8398c6ddc7c2a322c94919578c5aac55ab8cef88cd7

Scope/raw hashes were rechecked; neither file was modified. Their authorship
and earlier full inputs are retained context, not newly claimed blind reads.
Only the four unlocked scientific surfaces were newly read for CP2/CP3.
No other package, peer/scout report, external source, numerical experiment,
auxiliary agent or model change was used. Root's and the main author's stated
private access histories are their disclosures, not independently verified facts.

I authored this package's scope/raw receipts, not its source definition or
main manuscript, and have prior shared-project authorship/review history.
The raw proof preceded main access. This establishes task-local separation of
derivations, not blind review, cross-model verification or external peer review.
ARS suite, deep-research workflow, runtime policy and Devil's Advocate role
instructions were fully read at CP1 and retained for the assigned CP2/CP3
stages. Evidence-based findings override a forced issue count or score; no
numeric calibration, novelty certification or review-quality claim is made.

## 2. CP2 mathematical checks

**Quotient ownership and cancellation — PASS (Sections 1–2).** The labelled
occurrence-poset proof establishes both directions of the exchange equivalence.
Moving the desired first vertex past incomparable vertices is justified in
both linear extensions. Equal-letter occurrences remain ordered, avoiding an
extra factorial. Minimal/maximal deletion gives the exact finite residual
sets; deleting a boundary node cannot create spurious surviving constraints.
The distinguished first/last a-occurrence proves letter cancellation and then
finite-word cancellation. Content vectors separate differing deleted labels
and growth letters; growth and deletion cannot coincide in length.

**Own laws, all points and inverses — PASS (Section 3).** Formula (4) is the
actual word-pushforward, not counting representatives as dynamical arrows.
The transition cases are disjoint, row sums are one, and all positive entries
are <=1/2. Cylinder positivity proves full support; decreasing cylinder bounds
prove every singleton null while retaining it. The explicit 1/8 versus 1/2
calculation proves nonstationarity. Formula (8) has both necessity and
sufficiency, including the empty heap. The inverse I_c on its full E_c maps
bijectively onto X_c; its first-state chart restrictions agree with the raw
proof's smaller atlas. No predecessor, finite initial heap or component is lost.

**Every-Borel IMAGE and continuous-version uniqueness — PASS (Section 4).**
Cylinder laws extend by finite-measure uniqueness, then sum over the countable
first-state partition. Each derivative is positive and finite at every point
and locally constant on E_c. The additional uniqueness argument is sound:
E_c is open, mu has full support there, and two unequal continuous versions
would differ on a nonempty relatively open set of positive mu measure, contrary
to equality a.e. This is uniqueness among continuous versions, not among all
measurable null-set modifications. No new source law or null boundary is chosen.

**Complete signed histories and kernels — PASS (Section 4).** Empty prefixes
are explicitly included. Formula (11) composes actual prefix IMAGE factors;
(13) cancels common tails. Equal lag permits aligning witnesses, and aligning
middle witnesses proves composition. The three sets in (14) range over all
legal finite prefix pairs and every infinite tail, not only isotropy. They
match the raw rational product criteria. The clock-zero lag-one edge [2]->[22]
correctly prevents equating the clock kernel with the lag kernel. Signed
local clocks are kept; no positive classical roof follows.

**Full periodic and physical ledger — PASS (Section 5).** Formula (15)
enumerates all incoming histories with the correct source height. Eventual
periodicity characterizes source isotropy, and the complete map dZ->tau_C Z
follows by cancelling the finite stem. Since tau_C>0, extension isotropy is
trivial but source isotropy is not removed. The full vertical stabilizer is
H_x; phases are R/H_x, with no representative selection. Primitive cyclic
state words classify packets, distinct equal-time necklaces remain distinct,
and repetitions have k tau_C. Graph connectivity is not confused with equality
of source tail orbits. Walks avoiding e and null periodic paths are included.

**Composite conclusion and prescribed tests — PASS (Sections 5–6).** Formula
(18) counts one factor 2 for each edge except an empty-heap departure, together
with every actual append denominator and distinct-target deletion count.
Each edge reciprocal is even. A nonempty closed walk has even length >=2,
so its multiplier is composite (indeed divisible by 2^d). The retained
length-zero unit has clock zero and is explicitly outside that assertion.
The root-2 packet has entire H=(log4)Z, so no hidden half-period rescues it.
The main exchange walk e,2,[23],2,e differs from the raw example e,2,[23],3,e;
both are legal in the same owner, primitive because e appears only once, and
have multiplier 192. The former additionally demonstrates deleting a formerly
later letter after an actual allowed exchange. This is not a changed candidate.
The e-avoiding [2],[22],[2] packet has multiplier 8, consistently retained.

**Three complete own controls — PASS (Section 7).** The uniform poset theorem
applies separately to each frozen relation. FREE-WORD has its own N=1 and
leftmost deletion; COMMUTATIVE has its own multinomial counts and uniform
distinct-label deletion, not occurrence-weighting; NONCOPRIME has its own
opposite arithmetic exchange posets. Their pi/P, every-Borel IMAGE, kernels,
incoming histories, isotropy, phases and entire packet ledgers follow from
those own data, not MAIN's counts. The stated 96, 192 and 384 exchange tests
agree with the raw calculations. All have the primitive root-2 obstruction.

## 3. CP3 four-surface consistency and bounded disposition

All four surfaces identify ANG-20260922-CEH01 and the same STOP / FORK outcome.
The card's original OPEN status is preserved historical contract text; its
explicit outcome appendix reports the proved stop without rewriting that input.
Claim-ledger CEH-1 through CEH-8 are supported by the indicated paper sections;
its paper count/hash and original-card hash match actual bytes. README stays
within those claims. All displayed local Markdown targets are present among
the four read files; the six linked Section 2–7 anchors match their headings.

The strongest possible overclaims were checked explicitly: continuous-version
uniqueness does not assert uniqueness of arbitrary measurable versions; the
composite theorem excludes the unit and is limited to the four frozen laws;
the Markov lift is not claimed to escape splicing; signed clocks do not give
a classical positive-roof flow. Strong naturalness remains OPEN. T3 is NOT
AUDITED, classical A0/A1/A2 NOT APPLICABLE, formal Route UNASSIGNED, and B NOT
INVOKED. No regular manifold quotient, invariant flow measure or novelty claim
is promoted. The same-object ledger is intact, with no hidden packet deletion.

No critical, major or minor correction is required on these frozen inputs.
This is acceptance of a complete negative owner-level record, not target
success: the first primitive log4 packet already forces STOP, and the full
ledger contains no primitive log-prime packet. ARS checkpoint separation and
claim-boundary checks informed this review; they are not mathematical evidence
independent of the proofs. This review is frozen after its final hash receipt;
any different architecture requires a fresh card, not edits to this stopped one.
