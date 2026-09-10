# C430 — actual manuscript review, pass 1

2026-09-09 UTC. Current-team, nonauthor mathematical manuscript review of
*Native Galois fields of small wild cycles*. This is the first review of
the actual typeset manuscript assigned to this reviewer, not a relabeling
of an earlier research-proof review. It is not external peer review,
publication acceptance, a formal route evaluation, or a release seal.

## Disposition and ranked findings

**PASS 1: no mathematical or source-applicability must-fix found.**
The all-odd-prime, all-level native cyclicity and oriented first-character
claims are supported by the typeset proofs. The actual second-layer
ramification calculation is complete. The eventual tower has its stated
additional companion dependency and the required order of quantifiers.
There is one optional editorial clarification below. No numerical score
is assigned. Coordinator adjudication and a second review of the actual
post-adjudication input remain separate prospective steps.

| Severity | Finding | Action |
| --- | --- | --- |
| Critical / major | None found in the reviewed statement, proof, or dependency chain. | No mathematical repair requested. |
| Minor, nonblocking — R1-E1 | Section 7 first uses `d_H` in Theorem 7.1 without explicitly defining it in C430. The intended ordinary metric Hausdorff distance is recoverable from the text and companion, so this is not a proof gap. It is useful to make the convention explicit because the distinction between full Hausdorff convergence and merely weak measure convergence is essential here. | Before Theorem 7.1, add a sentence that `d_H` denotes Hausdorff distance for `d(x,y)=|x-y|` on nonempty compact subsets of the completed algebraic closure; optionally give its two-directed-distance formula. Do not change the theorem or replace full-sequence convergence by a subsequence statement. |

R1-E1 is at `sections/07_eventual_tower.tex:15–26` in the reviewed source,
PDF page 14. Verification after any edit: both directed distance bounds
used in Section 7.3 must still refer to this same distance, and the
threshold must still be chosen independently of the Galois element.
No other stylistic change is required for this disposition.

## Exact reviewed input and coverage

The assigned applicable `AGENTS.md` files, complete `BATCH_PLAN.md`, and
complete `auto-paper-improvement-loop/SKILL.md` were read. The instruction
was applied as a current-team mathematics manuscript review. Its older
external-model/ML-venue defaults did not authorize an API call, venue
score, mathematical run, or a write outside this allocated report.

I read the complete current `main.tex`, `math_commands.tex`, all nine
included section files, and `references.bib`; the complete
`SOURCE_BUILD_RECORD.md`; and the extracted text of all 18 PDF pages.
An initially truncated full-PDF extraction was completed by a separate
page-6–12 extraction, including the entire once-p argument and all early
conductor cases. This was a fresh check of what is actually typeset.

The current source files compare identically with their `baseline/src/`
copies. The current PDF, `baseline/main.pdf`, `main_round0_original.pdf`,
and `qa/author_build_02/source/main.pdf` have identical bytes. The final
baseline log equals the second author-build source log. The reviewed PDF
has 18 pages and 404880 bytes, Letter pages, PDF version 1.5. The final
TeX log ends with that successful output and has no warning, undefined
reference/citation, or overfull/underfull-box diagnostic. I did not
recompile the paper.

I also viewed the already retained second-build page images for pages
1, 10, 11, 14, and 18. These cover the first theorem and field overbar,
the cancellation lemma, the equal-conductor exclusion, the imported
compact theorem, and the final bibliography entries. No clipping,
colliding equations, or missing symbol was seen in these inspected
images. This is a five-page visual spot check, not a new all-page visual
audit; the author's distinct all-page check remains identified as such
in the build record. PDF text extraction can lose overbars, so the
algebraically closed constant field was checked in source and image,
not inferred from flattened extracted text.

The exact current input fingerprints are:

| C430 file, relative to its paper directory | SHA256 |
| --- | --- |
| `main.pdf` = `baseline/main.pdf` = `main_round0_original.pdf` | `54bc61f0d9c89405047fdf116bbcaf38d9e658c6d401b70862b22659f2574c8e` |
| `baseline/main.log` | `7b2cc706dcf7bdbaca4d7c7389162484cf18d078162954edda2ba0dccb6bfc4f` |
| `SOURCE_BUILD_RECORD.md` | `5f022836036b81e2e79b2cf4bc3100e9ae8891ef1b53e4df3c9700ff652a0957` |
| `main.tex` | `64726ac4156c5f58f7012373b0e00497bf36ea3465c7f664d46292749ca39669` |
| `math_commands.tex` | `09ce6cb709b396eef06067e872ed648bc5f4f4295c2c80200e2f4ccc4b298cdd` |
| `references.bib` | `9bb44aae6ffbd524fd24c6567df1bc7ab671fd7f11ea5a62031c35496f1bfcaa` |
| `sections/00_abstract.tex` | `4190fecbf742de602c4a6a1f9add60df97350f4922fe77a0c0bce5e8a63c8189` |
| `sections/01_introduction.tex` | `83859269616b6fc2d58ab8b22729b862c1cb9bbe49ab87ece564567086d2eefb` |
| `sections/02_local_setup.tex` | `6072b59c61c9583e035b9363c63e7889858b9ba127a8fa33024c036672f57ff6` |
| `sections/03_second_layer.tex` | `f65985674292b57f6cbe52ea2c407394e785fb1d9224dbe8829d9990a811204f` |
| `sections/04_full_inertia.tex` | `9f40a4775383c07dd4a4ecc8733f9ffbb235f1215ab26f02be60a62099fd298c` |
| `sections/05_oriented_quotients.tex` | `8cc49232529207fcbec1ff90f73ef9fe5cd5ca8a9e7049785355f47e7034d284` |
| `sections/06_ramification.tex` | `28d77c6548a8e8780ed56750cdea277b536cd2bbb3147a3abc6ef8c0fe3ea77c` |
| `sections/07_eventual_tower.tex` | `4873ac52d5dedee20ec4443d480d86bfdaf306e2dbcbef3d365c5e88a4a19b43` |
| `sections/08_scope.tex` | `026bdee1dd9bc96e3835c6ec038495cbbd4854ed3e178b95f5ee31ba37e999f2` |

## Mathematical readback

### 1. Native fields: Sections 2–4, Theorem 1.1

The Hensel factor interface is explicit. Reduction of the return quotient
has Weierstrass order exactly p^e, the complementary factor evaluates to
a unit on the small disk, and the imported ordinary cycle consists of
p^e distinct roots. Every root is an iterate of one chosen root. Thus
the root field splits the separable factor, and its Galois group is a
subgroup of the native cyclic rotation group. This preliminary argument
does not silently assume the subgroup is full. The coefficient residue
field is algebraically closed, and total ramification is justified using
the complete discrete-valuation degree identity.

The native displacement lemma establishes the isometry and its stronger
residue-one difference quotient. It gives the exact unit-index
displacement 2r and the deeper p-divisible displacement needed before
full inertia is known. The prime-to-p leading-value lemma proves the
monomial formula and controls the infinite tail; it is applied only when
the integer-normalized leading valuation is prime to p.

The derivative-ratio evaluations at lower-period roots are taken after
differentiating a polynomial identity, with the denominator derivative
proved nonzero. They are not substitutions into 0/0. The exact contact
`2(p-1)^2/p^2` forces only the second-layer degree obstruction, uniformly
in higher e. Under the hypothetical degree-p root-field assumption, the
compositum has degree p^2 and the prime-value lemma would give first
break `2(p-1)`, incompatible with its L1 quotient
of break `p-1`. This closes the all-odd-prime second-layer argument,
including p=3, without relying on a finite characteristic-three
certificate.

Full degree at arbitrary e is proved by a different mechanism. The
second-cycle multiplier valuation is `2(p-1)(2p-1)`, and the resulting
mean contact is strictly larger than 2r for every p≥3. A deep pair,
isometry, and strict ultrametric separation produce a unique matching of
all p top clusters. Its native and Galois equivariance are both proved.
A proper subgroup of the native cyclic group would act trivially on
these clusters, whereas the transferred level-two action is transitive.
The resulting degree p^e and distinguished one-step generator have the
same quantifiers as the abstract and theorem.

### 2. Oriented quotients and disjointness: Section 5

Lagrange interpolation gives the trace-one element without division by
p^e. The negative weighted trace sum is correctly reindexed, including
the wrapped coefficient, to give native translation by +1. Its
stabilizer is precisely the p-step subgroup. Changes of trace-one element
or root preserve the oriented Artin–Schreier class.

The matched cluster labels differ only by a translation. This gives
`rho_e mod p = rho_2 mod p` on the entire absolute Galois group, not just
an abstract identification of cyclic groups. Consequently the two
resolvents differ by an element of K, and their AS representatives
differ by a coboundary. The manuscript consistently distinguishes class
equality from raw Laurent-series equality.

The supposition `L1 ⊂ L2` makes the contact element prime-valued in L2
and produces a second lower break whose difference from the hypothetical
first break is nonzero modulo p. This contradicts the abelian
Herbrand/Hasse–Arf congruence. Cyclicity and the common degree-p subfield
then propagate `L1 ∩ Le = K` to every e≥2. Section 5 explicitly warns
that the paired hypothetical breaks are not yet the actual filtration.

### 3. Actual first quotient and L2 different: Section 6

Lemma 6.1 is fully typeset, with `v_p(a)=1` and strict displacement
inequality for every nonidentity automorphism. Cancellation forces the
first prime-to-p exponent `n=a+(p-1)b0`. The first-grade coefficient
polynomial has nonzero degree-p leading term; its additive image has
exactly p elements. For a later break c, the n-th monomial is uniquely
lowest, giving the stated displacement `n+c`. No prime-value formula
is used on the once-p-valued contact element.

For `B=L2 L1`, the manuscript verifies the degree, valuation scaling,
lower bound A on all contact displacements, and the positivity and
prime-to-p nature of the first break before applying the lemma. The
p-step subgroup's persistence is proved by the two projections and
upper quotient compatibility, not by a generally false product rule
for compositum ramification.

The exclusion of `b≤p-1` includes the equal-conductor case. A single
rank-two drop is excluded by the first-grade lemma, while a lower first
drop and final break p−1 give a later displacement strictly below A.
After obtaining `b>p-1`, conductor comparison and the native generator's
displacement determine `b=2(p-1)`. The last p-step displacement then
determines the actual second upper break `2p(p-1)`.

The final formulas agree with the displayed filtration and the
integer-normalized Hilbert different sum:

- L2 upper breaks: `2(p-1), 2p(p-1)`;
- L2 lower breaks: `2(p-1), 2(p-1)(p^2-p+1)`;
- field different: `(p-1)(2p^3-2p^2+3p-1)`.

The compositum filtration and its different are consistent with these
steps. The root-order discriminant is expressly separated from the
field different. The p=3 values 144 and 88 have their correct different
meanings and are consequences of the proved formulas, not computational
evidence or an unrecorded experiment.

### 4. Eventual tower: Section 7, Theorem 1.3

I read the actual current C431 introduction/Theorem 1.1 and full
Sections 5–6. The imported theorem supplies the compact closure of the
entire cycle union, the full Hausdorff limit as the compact tail
intersection, and a homeomorphism conjugating one application of P to
addition by 1 on Z_p. C431's old-cycle separation proof excludes every
finite p-power cycle and the two possible fixed points. Thus the input
is genuinely the infinite adding machine, not an unjustified conclusion
from growing approximating periods or weak convergence alone. Its
cyclic-partition and separation proofs do not invoke C430 inertia or
AS stabilization. C430 Sections 2–6 do not use C431.

The Galois action extends isometrically to the completed algebraic
closure, and finite nets consisting of algebraic cycle points prove
joint continuity on the compact closure. This does not assume that all
limit coordinates are algebraic. The centralizer argument identifies
each conjugated Galois map as a translation, and native orientation
removes scalar/sign ambiguity of the character.

For each fixed j, the finite quotient is taken from the actual Z_p
conjugacy. Compact disjoint fibers have positive separation. Full
Hausdorff convergence supplies an E_j before g is chosen. Nearby-point
labels are choice-independent, onto, and equivariant both for P and for
every Galois element. This proves the exact quantifier order

`∀ j≥1 ∃ E_j≥j ∀ e≥E_j ∀ g∈G_K: rho_e(g) mod p^j = chi_infty(g) mod p^j`.

Surjectivity follows from closed image and a nonzero first reduction;
uniqueness follows by comparing both candidate characters with one late
cycle at each finite depth. All kernel fields are defined inside the
fixed separable closure. Their nesting is justified by nested kernels,
not by a false containment assertion for the original full fields.
The text explicitly declines `E_j=j`, `K_j=L_j`, arbitrary full-field
nesting, and Galois correspondence for transcendental completed
coordinates. The abstract, introduction, proof, and scope section agree.

## Source ownership and dependency boundaries

I read the complete three source-audit records listed below. Those
records, together with the bibliography and build record, retain the
bounded nature of the source comparisons. I also newly inspected the
primary LRL Theorem C, its q=1 discussion, the minimal-ramification
definition and Proposition 4.4 statement; and the primary Elder–Keating
perfect-residue-field scope, Lemmas 2.1–2.2 and Theorem 2.3 statement.

The geometric cycle count, uniqueness, radius and reduction-iteration
orders are properly credited to the
[LRL author version](https://arxiv.org/html/1311.4478v3). Its q=1
alternative applies here, and the common root denominator remains p,
not p^e. The imported cyclic ramification and AS conductor tools have
the needed arbitrary perfect-residue-field scope in
[Elder–Keating, Section 2](https://arxiv.org/html/2503.16830v1#S2).
The manuscript does not count these classical tools as new results.

The comparisons with Keating's two papers and Debaisieux match the fully
read bounded source audits: relevant periodic-field, tower, and
torsor-character mechanisms are credited, while the fixed unchanged
base and exact eventual native characters are distinguished. Their
full external proofs were not newly re-read in this manuscript-review
turn, and no new exhaustive priority, forward-citation, or retraction
search is claimed. The Conrad and Stacks interfaces are standard,
correctly bounded in the manuscript, and supported by the author's
documented primary checks; no fixed-field theorem in the completion is
silently imported.

C431 is accurately described as an unpublished companion, with an exact
theorem locator and local PDF/source links. Distribution must retain
that companion dependency; the present review does not turn it into a
published external theorem. The actual checked dependency bytes are:

| C431 file, relative to its paper directory | SHA256 |
| --- | --- |
| `main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `sections/1_introduction.tex` | `d9e36e1bb5239457a6a8e3c32a47217ce8b25b8f340505000718c191198f1c34` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |

## Fully read accepted-proof and source-audit ledger

Paths below are relative to the batch directory. Each of the six
arithmetic proof inputs was read completely and compared substantively
with its typeset destination; these were not accepted merely because
an earlier report labeled them passed.

| Input | SHA256 |
| --- | --- |
| `continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md` | `7e9494aa53bb96f5927b8a6ab8e27c5d318d35a9c0f1751663acb9b91f0c1bdb` |
| `continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md` | `0a4f4ff66b633de268d741142502c1b4244868b9eccd3eb040ae472e0b296250` |
| `continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md` | `18366e789a1cb693000a2a50d42452e7e7658091cd67ece1c715d38e2a4ae479` |
| `continuation_round4/a3_first_quotient_ramification/PROOF_PACKAGE.md` | `a7a2823857d4bfe05006171809e310df196316f9777bb315052e348094dc7154` |
| `continuation_round4/a3_first_quotient_ramification/SECOND_LAYER_BREAKS.md` | `a79c9fea9e9ee01f8888bd0f088b20bb18fb505b60ccdeab8f1516125192a4ed` |
| `continuation_round5/a3_eventual_quotient_tower/PROOF_PACKAGE.md` | `b20fc9dbfe32ca492a373bc86ced69738518f7cabd295f6903c3bd52d5b77c68` |
| `continuation_round4/NOVELTY_CHECK_UNIFORM_LOCAL.md` | `81b114bb30964c5b46ee077e090ac93cb16e03eec50c66fef3a33cded3ced2bb` |
| `continuation_round4/x2_uniform_local_source_admission/REPORT.md` | `80eedc560f717f1de0f55e4cbc1948e2ca59a42be395c023e622c2f6b68a5f9d` |
| `continuation_round5/x1_eventual_tower_sources/REPORT.md` | `aa34f7a393bfc69b7366653af49b131a16a3649aaca8f2d14c7e49a63419b027` |

## Handoff and execution boundary

This report is the only allocated task file written by this reviewer.
No source, bibliography, PDF, baseline, shared ledger, evaluation, Git
state, or prior proof/review artifact was modified. No mathematical
program, compiler, new agent, external model API, or manuscript upload
was used. Read-only public primary-source retrieval is distinguished
from an external-model call.

The auto-paper-improvement-loop instruction influenced the explicit
round-one input binding, the severity/action format, and the separation
of an actual manuscript read from historical proof checks. It did not
authorize performing the author's revision or the coordinator's gates.
The reviewed source and baseline remain frozen. After full report
readback, the next step is coordinator adjudication of R1-E1, followed
by a separately assigned pass 2 on the actual resulting source/PDF.

Final status: **C430_MANUSCRIPT_PASS1_NO_MUST_FIX;
ONE_OPTIONAL_EDITORIAL_CLARIFICATION; AWAIT_COORDINATOR_ADJUDICATION.**

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
