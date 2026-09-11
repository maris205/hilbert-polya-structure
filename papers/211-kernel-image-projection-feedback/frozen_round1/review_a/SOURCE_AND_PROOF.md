# Review A: deductive attacks, source ownership and preparation boundary

2026-09-08 UTC. This is a completed pre-execution mathematical/source
assessment of the accepted P211 Round0, not a final manuscript verdict.
No mathematical correction is proposed and no scientific execution,
canonical adoption, strict replay pair or same-reviewer delta acceptance
has yet occurred. `OWNER_AMBER / HOLD_EXTERNAL`.

The reviewer nonauthorship and prior infrastructure familiarity are stated
in `PREPARATION.md`. I read all nine frozen TeX/Bib files, the complete
235-line proof package, source audit, claims/evidence, narrative, paper
plan and current frozen README. Author scientific code and canonical were
hashed as required input files, not read as the independent implementation
template. The independent capsule was written from the literal operation
and mathematical claims; it imports no author or historical program.

## 1. Hypothesis and convention audit

The carrier is every nondecreasing tuple of length n over [n], for n >= 1.
It is not restricted to extensive or top-fixing functions. Kernel ends X
always contain n; the distinct-value set Y need not contain n. The second
projection uses A = Y union {n}. Both supports are recomputed after every
whole-function step, and in T = e_X composed with e_A the right factor acts
first. Time zero is permitted and reserved for already fixed states.

The image test is genuinely stronger than extensivity and top-fixing.
For example, at n=4 the whole tuple (2,3,4,4) is extensive and fixes 4,
but W=(1,2,4), Z=(2,3,4) violates z_1 < w_2. It has zero predecessors
under the manuscript's image theorem. The proposed verifier does not use
extensivity as a replacement image predicate or omit these zero fibres.

The support notation f_{Y,X} is value set first, endpoint set second.
On an image target f_{Z,W}, the next kernel projection therefore uses W,
not Z. This reversal matters for the endpoint peeling formula. The image
inequalities also imply w_i > z_{i-1}, so every claimed free-gap length
w_i-z_{i-1}-1 is nonnegative, including the first gap with z_0=0.

## 2. Direct product and exact first image

For arbitrary n-containing X,A, partition A by the value z of e_X(a).
In each nonempty part B_z, the consecutive e_A blocks form one output
block with right endpoint max B_z. Thus Z=e_X(A) and W consists of those
maxima in increasing z order. This proves the asserted product formula
without assuming that the original source is extensive or top-fixing.

For its i-th pair, w_i <= z_i. If an A-site belonging to a later output
block were <= z_i, its X-ceiling would be <= z_i, a contradiction.
In particular z_i < w_{i+1}. The final pair is (n,n).

The containments W subset A and Z subset X are immediate. Conversely,
every c in X intersection A maps to itself, is the last A-site mapping
to c, and therefore appears as the equal pair (c,c). This proves the
exact common-support identity W intersection Z = X intersection A,
not just preservation of a subset of anchors.

For sufficiency, reverse the two target supports: source f_{W,Z} is
valid because W,Z have the same cardinality and contain n. The image
inequalities give e_Z(w_i)=z_i, with distinct outputs and right endpoints
w_i. This is an explicit predecessor, so the image criterion is iff.
The source ranks in this construction require no extra assumption.

## 3. Endpoint update, full time and sharpness attacks

On the first image, equal pairs are precisely the common anchors. Between
anchors, all unequal pairs form the strict list

    w_1 < z_1 < w_2 < z_2 < ... < w_r < z_r < c.

The X-ceiling of z_i is w_{i+1} for i<r; z_r and c both have ceiling c.
Recomputing the rightmost block ends gives exactly (z_i,w_{i+1}) for
i<r and the final anchor (c,c). The outer labels w_1,z_r disappear.
This is two-label deletion with alternating roles, not one-ended erasure.
Common anchors separate the ceiling intervals, so no cross-anchor merger
is silently assumed away. The same calculation covers r=0 and r=1.

After t updates the strict portion is its middle 2 max(r-t,0) labels.
While any such portion survives, its two outside distinct labels are lost
on the next step; thus stabilization cannot occur early. The exact
image-state entrance time is the largest r, and an anchor-only state is
the fixed projection e_C. Every whole-function orbit enters this image
after one step, ruling out every nontrivial cycle. The original source's
terminal support is exactly X intersection (Y union {n}).

For a nonfixed source the first normalization step must be counted:
tau(f)=1+R(Tf). A fixed source has time zero, not one. At n=3,
(1,1,3) -> (2,3,3) -> (3,3,3) is a hand-derived example with two full
steps but one remaining image step. At n=2, (1,1) -> (2,2) takes one,
while (1,2) is already fixed. At n=1 the unique state is fixed.
These are deductions from the displayed operation, not reported runs.

A strict interval with r pairs needs 2r labels below its ending anchor.
Therefore R <= floor((n-1)/2); with the normalization this gives the
stated upper bound ceil(n/2), for n>=2. This generic label-budget argument
is not by itself credited as the contribution. The sharp result also
requires the literal normalization, exact interval update and full-carrier
witnesses below.

For n=2m+1, X=(2,4,...,2m,n) and Y=(1,3,...,2m-1,n) yield exactly m
strict pairs in the first image. For n=2m, X=(2,4,...,2m) and
Y=(1,3,...,2m-1) require the actual completion by n; their first image
has m-1 strict pairs. In both cases f(1)=1 while Tf(1)=2, so the
initial step is not gratuitous. These give m+1 and m respectively,
including the even boundary n=2. No all-maximizer classification is
claimed by the manuscript or inferred from a later finite census.

## 4. Full labelled-target inverse, including orientation

For a target satisfying the image criterion, every source must contain
the forced z_i in X and w_i in A. On a strict interval [w_i,z_i],
X cannot meet [w_i,z_i), because e_X(w_i) would be too small; A cannot
meet (w_i,z_i], because w_i would cease to be the final A-site producing
z_i. Equal pairs force the same site into both sets. These intervals,
forced sites and open free gaps D_i partition the chain.

A free-gap site cannot belong to both supports: it would give an extra
anchor by the exact intersection identity. If a chosen A-site preceded
a chosen X-site in the same gap, its X-ceiling would create a target value
strictly between z_{i-1} and z_i. Consequently all extra X-sites must
precede all extra A-sites, with unused sites allowed anywhere. This order
is not interchangeable and is not a binomial count of arbitrary colours.

Conversely, with precisely those restrictions each A-site in
(z_{i-1},w_i] has X-ceiling z_i; its last site is w_i. This constructs
the exact specified whole target, not merely a target of the same rank
or the same unlabelled shape. The source supports are recovered uniquely
from any source, so the decoder is bijective rather than an overcount.

For a_i extra X-sites and b_i extra A-sites in d_i available positions,
one chooses their union in binom(d_i,a_i+b_i) ways; its first a_i sites
must be X. The forced supports have equal size, hence their independent
gap weights record delta=|A|-|X| as the exponent sum of b_i-a_i. The
published completed-support condition admits only delta=0,1, recovering
Y=A and Y=A minus {n}. In the second branch |A|=|X|+1>=2, so Y cannot
be empty. There is no additional rank multiplicity factor.

This proves the target-gap Laurent product and the extraction of its
zero and one coefficients. It uses neither the peeling theorem nor the
clock bound. It is not an implicit equation involving an unknown source.
P_0=1 handles empty gaps and adjacent anchors. At n=1 the product is 1
and gives the only predecessor. Targets failing the image criterion have
zero sources and must remain in the finite test carrier.

As a hand-derived inverse attack, for the constant target (3,3,3),
D_1={1,2} and P_2=u^-2+2u^-1+2+2u+u^2. The formula gives four sources:
(1,1,1), (2,2,2), (3,3,3), (2,3,3). The wrongly reversed free pattern
A at 1 followed by X at 2 instead reconstructs (1,1,3), whose image is
(2,3,3), not the constant target. This explicitly tests the easy-to-swap
gap orientation. No mathematical program was executed for this example.

## 5. Direct primary-source inspection and ownership

Fresh browser returns are preserved verbatim as structured tool returns
in `sources/web01.json` through `sources/web04.json`. Older source bodies
were JSON-decoded from the immutable source-addendum records before
reading. These saved objects are browser returns, not claimed raw HTTP
captures or native execution streams. The exact external input pins are
separate from the 33 frozen workspace input pins.

Stein's version of record is *The algebra of the monoid of order-preserving
functions on an n-set and other reduced E-Fountain semigroups*, Semigroup
Forum 111, 798--819, published 20 November 2025. Section 5.1 supplies the
kernel/image coordinates and ceiling supports. Its paragraph following
Lemma 5.12 explicitly supplies completed-image reconstruction and rank
differences zero or one. These are established primitives and receive zero
new contribution credit. I read the publisher's definition/support body
and full reconstruction/category paragraph, including the relevant
Section 5.1 interval, and checked the bibliographic metadata directly.
[Publisher primary source](https://link.springer.com/article/10.1007/s00233-025-10595-2).

Andrenšek v1 is *Endomorphisms of Hecke-Kiselman Monoids Associated to
Simple Oriented Graphs*, submitted 16 April 2026. I read Section 4's full
mathematical prose/formulas, including the Catalan floor-retraction
representation, Proposition 4.1, Theorem 4.4 and Lemma 4.6 with their
proofs; the damaged opening drawing was not visually inspected or credited.
Its graph-generator subset encoding is not literally the paper's endpoint
supports. Floor/ceiling order duality and the fixed-idempotent-product
criteria are known mechanisms, not contributions of P211.
[Version 1 primary source](https://arxiv.org/html/2604.15497v1#S4).

Version 3, dated 4 August 2026, is separately titled *Homomorphisms of
Hecke-Kiselman Monoids Associated to Simple Oriented Graphs*. I read the
content/idempotent background, Definition 3.1, Lemma 3.3, both complete
Proposition 3.4/3.5 proofs, Theorem 3.6 and the sandwich/corollary
neighborhood through Corollary 3.9. The directed-path product criterion
is subtracted as static background. Later displayed Sections 4--5 were
not relied upon as completely read. Separate version-specific abstract
metadata confirms both titles and dates; v1 theorem numbers are not
silently assigned to v3.
[Version 3 primary source](https://arxiv.org/html/2604.15497v3#S3),
[version metadata](https://arxiv.org/abs/2604.15497v3).

The v1 inspected prose span is browser lines 615--906 across the archived
body02/body03/body04 records. The v3 pertinent definition/proof neighborhood
is lines 185--254 and 269--429 from archived and fresh targeted returns.
The publisher spans include 403--428 and 525--586. Line numbers identify
each particular returned body, not equivalence between different versions.
A truncated combined display and one empty locator supplied no reading
credit; separate complete narrow reads supplied the missing coverage.
`evidence/NAVIGATION_FAILURES.json` records these limitations and the actual
missing-jq navigation failure. No failed scientific invocation is hidden.

The actual frozen introduction explicitly deducts all Stein primitives and
distinguishes the two Andrenšek versions. The inverse proof credits the
known rank branches at their use. Thus both candidate-gate carry-forwards
m01/m02 are materially implemented in the reviewed text; they are not new
open manuscript defects. The inherited gate itself is not being counted
as this actual manuscript review.

## 6. Repository mechanism subtraction and actual extent

The accepted candidate gate supplies its historical search boundary through
P210 and prior killed candidates. I read its full correctness/value and
source/read-scope records plus original historical pins, and then inspected
the selected nearest mathematical originals below. This is targeted
collision pressure, not a new semantic reading of every historical paper
or a proof that no conjugacy/factor can exist.

| Original actually inspected | Deduction and remaining boundary |
| --- | --- |
| P167 `main.tex`, all 385 lines | Minimum-inverse-position selection, root paths/cycles, its 2n-2 clock and Bell-type inverse organization are already owned. P211 neither selects a minimum inverse arrow nor inherits this whole-function rule merely because both act on maps. No no-factor theorem is asserted. |
| P190 `main.tex`, all 376 lines | Cyclic Brandt sandwich erosion, one-sided run loss, its parity clock and gap transfer are already owned. Mere erosion/parity language earns no credit. The inspected Brandt state/update is not the recomputed pair of chain supports, and it does not itself give P211's full normalization or labelled inverse decoder. |
| P209 complete setup, recurrence and inverse sections | Ordered-fibre threading, feeding rotation, selected-arrow paths and its target inverse mechanism are already owned. Rewriting a tuple as fibres alone is not an advance. Its rule is not identified with the present ceiling product. |
| P193 `main.tex` lines 35--310 | Mutual-best block refinement, its normal form and depth-layer clock subtract generic rank/partition stabilization. The later inverse section was not claimed as read or used. |
| P187 algebra replacement `CANDIDATES.md` and `KILL_LEDGER.md`, complete | The ten-entry ledger, including generic R01/P190 erosion, remains negative prior art; relabelled erosion is not promoted as a new axis. |
| P132 nondivisor algebra `SCOUT.md`, lines 142--170 and 452--552 | The actual SR1--SR6 and TM1--TM5 entries were inspected; transformation/inverse/sandwich templates are deducted within this extent. No complete read of the entire long scout is claimed. |
| P204 algebra-second `SCOUT_REPORT.md`, complete | Inverse and twisted-power conjugator mechanisms are already spent. They supply no free credit for semigroup vocabulary. |
| Current nonlinear `PROOF_AND_SUBTRACTION.md`, complete | PXE/TP and conjugator/coset mechanisms remain killed; coordinate changes of those schemes are not new results. |
| Current rational-coupling `PROOF_AND_SUBTRACTION.md`, lines 150--335 | CAC's four-step nilpotent clock and AB/BA/coset inverse mechanisms remain killed. A short semigroup clock does not automatically establish independent value. |
| Current SCRF complete 359-line `PROOF_PACKAGE.md` and root reception | Its support-count remainder rule, sharp support budget and quotient/cross-modulus inverse arguments are subtracted. It is NO_PROMOTION_VALUE, not a retained paper or an exact identity with KIP. This post-gate fortieth closed attempt does not alter Round0 or add a P211 science run. |

After these deductions the bounded retained objects are the exact
recomputed endpoint normal form with sharp full-carrier time, and the
specified-target forced/free/forbidden atlas with its independent ordered
gap factorization. The static projection product, support rank branches,
plain deletion budget and coefficient multiplication alone receive zero
credit. I found no demonstrated whole-carrier transfer in the inspected
originals that removes both retained objects. This is a bounded assessment,
not global originality, specialist endorsement or owner clearance.

## 7. Independent finite pressure and unresolved lifecycle

The standalone A verifier first enumerates the complete original carriers
and computes literal edges from ceiling tables. It then transposes the
whole graph, prunes indegree-zero vertices, traces every cycle and uses
reverse BFS for depths. Complete forward orbits check those graph-derived
results. Only afterward are theorem predictions compared. The inverse
route is target-only ordered ternary gap words, with binomial Laurent
convolution independently compared to full incoming lists, including zero
fibres. No temporal theorem computes a graph edge or graph distance.

All 2,353 states for n=1,...,7, all targets, each edge, full incoming list,
orbit, cycle, depth, target description and coefficient table are retained
in the future JSON contract. The counts and successful finite verdict have
not been invented in advance. `CANONICAL_SCHEMA.md` gives every field and
array order. The old author pilot prelock defect is preserved and not
used as a strict A replay; fresh A production/pair bindings are mandatory.

No Critical, Major or Minor mathematical/typesetting/source defect is
identified at this preparation stage. That statement is not a final
scientific or artifact PASS: root must first receive the entire preparation,
inspect an exact initial binding, receive real complete stdout, exclusively
adopt previously absent canonical bytes and separately bind/receive the
strict pair. A complete final report, finding census and actual same-reviewer
delta acceptance remain to follow. The later B, terminal physical builds
and five-paper completion gates cannot be replaced by this preparation.

Historical proof/planning documents retain their contemporary pending
execution language. The frozen current README and author execution receipt
explicitly record the later author-run lifecycle, so I do not require
rewriting immutable historical preparation merely to homogenize tense.
Source discovery and build provenance limitations remain disclosed, and
any concrete new source transfer or changed scientific dependency can
reopen the affected conclusion. No external action or Git write occurred.
