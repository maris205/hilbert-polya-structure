# CP2 / CP3 final review — ANG-20260922-DGH01

2026-09-22; batch `GEOMETRIC-FEEDBACK-20260922-J`, round 2/5.
Verdict: `CP2 PASS; CP3 PASS — OWNER PROOF WITH BOUNDED MAIN T2 OPEN`.
Outcome: `OWNED HENON CLOCK; FIXED/133 WINDOWS EMPTY — BOUNDED OPEN / STOP / FORK`.
Internal shared-history `NOT_CALIBRATED`; not external peer review or a T2 pass.

## 1. Actual unlock, complete reads and bindings

Root read and froze the 288-line raw proof before separately unlocking the
four finished surfaces. I read Paper lines 1–120 and 121–230, Card 1–115,
README 1–42 and Ledger 1–39 completely through their actual final lines.
`wc -l` confirmed the EOF counts; no output was truncated. The aliases below
bind each actual filename, full line count and measured current SHA256:

Paper = paper.md — 230 lines — SHA256 3be4440099fc070681e6ade525d70e87aec833937b5edf6ee39a7bff54429baf
Card = candidate-card.md — 115 lines — SHA256 b2df228032038f8f8f7966697a91cf39fdba017c4676db92d85c33f16cbb65ef
README = README.md — 42 lines — SHA256 583a6b34d9b62254a29caa09767c167f26b97382c8bbb760e09b36c26901bc5b
Ledger = claim-ledger.md — 39 lines — SHA256 c1ead7dbba59c8babcedb9084d09562fdc06eda3569d3a676b9756dfd74615b4

The original and clarified pre-proof prefixes were rehashed directly using
`head`; neither the definitions nor the pre-proof target was overwritten.

candidate-card.md (original lines 1–84) — SHA256 8b39da5a233453db3d50d1758df7833f7d7220ef56a858f1b09b33fac83a33f8
candidate-card.md (released lines 1–98) — SHA256 4f316c418c00484c41dae025aa1754ec678661ab05b911e391948ce7d26e6ccd
scope-review.md — 93 lines — SHA256 d50906c59bf039ffa85757941894519560426d0fdcb0dbf6bdea9bd1d594b255
independent-proof.md — 288 lines — SHA256 d14a3f111390a71442b08705deeb7d3c71ecec27a171433e182d7fdce8666337

Scope/raw hashes and counts were checked; their bytes were not changed.
I authored those evidence files, not the source definition or main manuscript.
Only these four scientific surfaces were newly read after unlock. No other
new output, helper/peer/scout artifact, old card, external source, experiment,
auxiliary agent or model change was used. Author/root private-access reports
are their disclosures, not independently verified access logs.
The declared design-feasibility exposure and shared prior history remain;
this is not blind preregistration, cross-model verification or external review.
The same-author helper is disclosed in Paper, not counted as this reviewer.
Previously fully read ARS instructions are retained, not falsely reported as
fresh reads during this phase. Raw separation preceded manuscript exposure.

## 2. CP2 mathematical comparison

**Full state, root closure and partial bijections — PASS (Paper Section 2).**
The half-open strips include every real sign and the exact floor cuts. Root
closure follows from coprimality with a+b. At a target, U uniquely fixes d;
positivity Ds>r and gcd(D,r)=1 are precisely the MAIN/A/Q source-root tests.
Each real inverse and the R gate give both identities and all incoming, not
just sufficient formulas. Domain and image are distinguished, so no-predecessor
points and terminals are not conflated or removed. No global onto, continuous,
conservative or symplectic conclusion is added.

**Every-Borel own IMAGE and cut versions — PASS (Section 2).** Substitution
in V and integration in U prove the inverse determinant law on every Borel
subset, with counting weight one on both root fibres. The unique predecessor
and U-recorded strip make image charts disjoint, so the whole-image summation
has no hidden multiplicity. MAIN/R/Q obtain 1/d and A obtains 1 from their
own inverse formulas. Constant polynomial extension values at cuts are the
frozen versions, not post-return modifications. No unrestricted measurable-
version uniqueness or differentiability of the global cut map is claimed.

**Full history cocycle and kernels — PASS (Section 3).** Same-lag witnesses
are aligned using already legal continuations; no terminal receives an invented
extra step. Finite IMAGE products give exp(-c) in the source-to-range direction.
Partial injectivity cancels the shorter history, yielding the whole lag kernel
as units. MAIN/R/Q clock-zero arrows are exactly actual all-unit connecting
segments; A's whole groupoid is clock-zero. Their intersections with the lag
kernel are units. These agree with the raw proof and are not loop-only tests.

**Entire isotropy, incoming and phases — PASS (Section 3).** Unique inverses
exclude transient trees entering cycles. Legal signed iterates give all source
chains and their endpoints; nonperiodic chains have zero isotropy. A least
q-cycle has source qZ and clock kq mapped to kL. Extension isotropy is qZ when
L=0 and zero when L>0, so ineffective loops are correctly retained. The root
sum excludes all-unit cycles only for MAIN/Q; it is not a claim that any cycle
exists there. A has H=0 globally without losing possible map cycles, and R's
unit cycles retain their isotropy. The phase sign is correct: the arrow from
index j to i has c=B(j)-B(i), making h+B(j) invariant, in R or R/LZ. This
accounts for all heights/incoming and same-packet repetitions, not a section.

**COMPLETE fixed sets — PASS (Section 4).** MAIN/A/Q fixed integer roots
force (1,1), d=2. Their respective quadratic/linear fixed solutions lie outside
both allowed d=2 strips. The emptiness is global over all roots, not sampled.
For R, the negative strip is impossible and monotonicity of t(t+D+1) on the
positive strip gives exactly 2D(D-1)<=b<D(2D+1), with the stated gcd/gate.
This is the same necessary-and-sufficient set as raw, including boundaries.
Every fixed point has only itself incoming; D=1 keeps Z extension isotropy
and real phases, whereas D>1 has the full primitive log D circle.
Paper's infinite family b=2D^2-1, a=1+jDb differs from raw's witness family
but satisfies the same exact set: the interval bounds, gcd=1 and D|(a+b)
all hold for D>=2. Distinct j give distinct singleton orbits. Countability
follows from the integer parametrization. Thus the stated excess prime and
composite fixed packets belong to R only; no control result transfers to MAIN.

**SINGLE 133 traversal — PASS (Section 5).** Formula (6) is the full real
three-step closure equation with the exact d=1 and d=3 strips. Its positive-z
case contradicts y>=0. In its negative-z case, negative x contradicts the
first equation, while positive x contradicts the second. The inequalities
include every retained endpoint. This agrees with raw under renaming of the
three real coordinates. The solution set for one three-step closure is empty;
the formal product 9 therefore has no H or primitive packet assigned here.
This test is NOT a census of six-step, nine-step or other repeated-133 returns,
period-two returns, other words, or all MAIN periodic states. No such result
is inferred from the empty window or from the generic conditional H formulas.

## 3. CP3 four-surface scope and final disposition

All four surfaces identify ANG-20260922-DGH01 and the same bounded OPEN /
STOP / FORK outcome. The Card preserves both the original OPEN input and its
pre-proof target clarification, then appends the result transparently. Paper
and Ledger's 98-line input lock matches the measured prefix. Ledger claims
and README agree with the proofs, especially SINGLE traversal and unclassified
repeated-133 itineraries. Local Markdown targets refer to these read package
or evidence files and are present; no unrelated science was opened for checks.

T0/specified IMAGE-clock T1 ownership is separate from strong naturalness OPEN
and MAIN T2 bounded OPEN. Empty windows neither prove nor refute the global
necessary prime-time/multiplicity target. R's adverse packets and A's zero
clock do not change that status. The frozen budget ends the local research;
no extra census, retuning, source deletion or automatic advancement is implied.
Classical NOT APPLICABLE, T3 NOT AUDITED, formal UNASSIGNED and B NOT INVOKED
remain consistent. There is no claimed operator, novelty or publication result.

No critical, major or minor correction is required on these bound inputs.
CP2/CP3 PASS accepts this exact owner proof and honestly inconclusive return
screen, not a MAIN target pass. ARS stage separation and claim-boundary checks
informed the review; they are not external mathematical validation. Freeze
this report after its final receipt; all science, scope and raw remain unchanged.
