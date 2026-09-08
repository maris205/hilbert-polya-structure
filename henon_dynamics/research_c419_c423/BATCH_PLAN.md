# C419–C423: five admitted contracts and manuscript plan

2026-09-08 UTC. Contract state: **FIVE_SUBSTANTIAL_CONTRACTS_ADMITTED**,
as recorded in [ADMISSION_DECISIONS.md](ADMISSION_DECISIONS.md).
Outline state: **APPROVED_FOR_MANUSCRIPT_DRAFTING**. The five exact
contracts below are admitted; their manuscript transcription and release
remain unfinished. No sixth paper or C424 is authorized.

The coordinator read the complete [independent outline review](REVIEW_OUTLINE.md)
and closes this gate on 2026-09-08 UTC: PASS, zero mandatory scientific
or workflow corrections. The ownership typo was removed; current status
now distinguishes active manuscript numbering from historical unnumbered
proof snapshots. Neither editorial change alters a contract. C419–C423
below are active manuscript assignments, not completed-paper claims.

## Shared format, skill use and completion criteria

Use the same anonymous English mathematical-article format as the
preceding authorized C-series batch: 11pt, approximately one-inch
margins, modular section files and explicit source attribution. No
journal or ML conference is selected; no artificial nine-page limit,
minimum related-work page count, section quota, experimental section
or decorative hero image is imposed. Length follows the complete
argument, including its proof tables. Do not invent author identities.
Disclose AI-assisted preparation and internal, not human, review.

The `paper-writing` workflow is applied through `paper-plan`,
`paper-figure` for substantive exact tables, `paper-write`,
`paper-compile`, and `auto-paper-improvement-loop`. Its named legacy
GPT-5.4/MCP examples are replaced by current-team internal review under
the batch's standing instruction; no paid model call, model switch or
external upload is performed. The ML-venue defaults do not replace the
user's mathematical contract. Main-agent selected skills and required
writing, venue and citation references were read in full before planning.

All pipeline phases are retained in their relevant scope. For proof-only
papers, the figure phase produces useful LaTeX classification/comparison
tables from established theorem data, not fabricated experiments.
One independently reviewed complete outline precedes drafting. After
the first real PDF, retain **two actual review/revision passes** for
the generated manuscripts under the improvement skill; preserve the
baseline and real resulting PDF versions and full review texts. Do not
manufacture revisions or rising scores when a review needs none.
This is distinct from repeating old mathematical programs.

Every article must contain complete proofs in its body or an included,
typeset appendix. An external local Markdown link alone is not a proof
supplement for a central assertion. Verified external theorems may be
used with exact hypotheses and precise ownership. The final package
also retains its proof/source notes and actual evidence.

Formal judgments use unchanged Route A v0.2.0 at
`flow_systems/skills/route-a-evaluator.md` with its exact hash and
prescribed references. They are not assigned by this plan. Missing
target tests remain NOT_TESTABLE/INCOMPLETE as appropriate.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.

## Numbering, objects and author ownership

| Paper / working title | Exact object and observable | Author and path |
| --- | --- | --- |
| C419 — Integer periodicity of positive trace-map words | A=(x,z,xz-y), B=(z,y,yz-x), every positive word using both letters, all integer points and invariant levels; one whole word is one ordinary time step | coordinator; `papers/C419_positive_trace_words/` |
| C420 — When do the cusp scattering matrices of Gamma_0(N) commute? | Every positive integer N, complete weight-zero/trivial-character scattering matrix in fixed width-one cusp coordinates; pairwise commutativity at all regular complex parameters | spectral-probe author after outline review; `papers/C420_scattering_commutativity/` |
| C421 — Integral periodic orbits of a cubic three-term recurrence | T_a(x,y,z)=(y,z,yz+a-x), every integer a and invariant level; all ordinary integer cycles, actual least periods and oriented per-level counts | lyness_round5; `papers/C421_integral_return/` |
| C422 — A uniform orbit bound for finite-field q-Painleve I | All finite fields F_q, nonzero s,t_0, the seven specified native branches on torus plus four accessible affine lines over phase cycle t_0<s>; ordinary branch iteration | char-p author; `papers/C422_painleve_bound/` |
| C423 — A two-cycle test for simultaneous preperiodicity in characteristic three | f=X^4+X^6 over every characteristic-three field and all marked pairs; infinitude of geometric parameters lambda for ordinary preperiodicity of both points under f+lambda | coordinator; `papers/C423_two_cycle_preperiodicity/` |

Authors own only their listed package directories. The coordinator owns
this plan, current state, round-nine adjudication, shared indexes,
evaluations, final builds and release/Git integration. Separate reviewers
write only their assigned review paths. During outline review authors
may read inputs and prepare per-paper plans/source material, but must
not pre-empt the outline gate by producing manuscripts.

## C419: exact all-positive-word arithmetic exhaustion

One-sentence contribution: the universal integer periodic locus for all
positive words containing both generators is an explicit 39-line-plus-
four-point set, reducing every fixed word and level to an exact finite
classifier and giving proper two-sided escape of every nonperiodic point.

| Claim | Accepted proof/evidence | Manuscript location |
| --- | --- | --- |
| Universal locus and exhaustive cone/descent proof | `../continuation_c414_c418_round2/mapping_class/PROOF_PACKAGE.md`, Steps 1–5; `mapping_class_review/REVIEW_PROOF_AND_INCREMENT.md` | §§2–4 |
| Every listed point is fixed by some positive word | Same proof, Step 6 | §4 |
| At most 40 level candidates; exact word-dependent ordinary cycles | Same proof, Steps 7–8 and `classify_word.py` | §§5–6 |
| Proper forward and backward escape outside the periodic set | Same proof, Steps 9–10 | §7 |

Structure: front-loaded theorem and source comparison; maps, chronological
convention and invariant; escape cone and complete descent; the 39 lines,
exceptional points and existential converse; exact level intersections;
partial-injection classifier and native zeta corollary; two-sided escape,
reproducibility and scope. Keep every intermediate letter phase in the
classifier. A union over words is not periodicity under every word.
Do not assert existence of a 40-cycle or treat the generic-line automaton
as a replacement for actual point dynamics.

Tables: the 27+6+6 line families, quadratic level forms and low-level
cardinalities, plus a concise source-versus-new-scope comparison. Their
contents are proof data, not new numerical samples. Sources come from
the verified mapping-class source audits; deduct C413's single Fibonacci
map, general escape theory and whole-group finite-orbit results. No
rational/all-group/complex-scheme extension is asserted.

## C420: full fixed-coordinate scattering classification

One-sentence contribution: a character/tensor analysis classifies all
levels at which the complete fixed-cusp scattering family commutes,
including the parity cancellation that distinguishes N=50 from N=100.

The exact arithmetic answer is
\(v_2(N)\le9,v_3(N)\le3,v_5(N)\le3,v_p(N)\le1\) for p>=7;
if \(v_5(N)\ge2\), all other odd-exponent primes are ±1 modulo 5;
if \(v_2(N)\ge8\), all odd odd-exponent primes are ±1 modulo 8.
No phase restriction is imposed at even unramified exponents.

| Claim | Accepted proof/evidence | Manuscript location |
| --- | --- | --- |
| Fixed cusp character decomposition and full paired blocks | `arithmetic_spectral/independent_review/REPAIRED_CLASSIFICATION.md` | §§2–3 |
| Principal oldforms and constant phase/parity reduction | `oldform_review/PROOF_PACKAGE.md` and `TWIST_PARITY_LEMMA.md`, under `arithmetic_spectral/` | §§4–5 |
| Nonreal-square and odd-phase necessity with no tensor cancellation | Repaired classification and its minimal-level scalar lemma | §§5–6 |
| Exact arithmetic equivalence at every level | `AS2_PARITY_CRITERION.md`, explicit group facts in `AS2_REPAIRED_CRITERION.md` | §7 |

Read every dependency routed by `arithmetic_spectral/AS2_PROOF_INDEX.md`
and the complete `non_author_review/REVIEW.md` and source/substance audit.
Structure: main level classification and normalization; verified classical
scattering formulas; fixed Fourier blocks; principal all-exponent
eigenbasis; real-square phases and odd central channels; nonreal-square
Dirichlet-coefficient necessity and tensor lemma; elementary congruence
classification, counterexamples, meromorphic extension and limitations.

The paper must include the key local matrix identities and both necessity
arguments, not merely quote the final arithmetic criterion. Incoming
oldform matrices depend on s and are not a fixed similarity. Preserve
imprimitive-square Euler factors and all regular exceptional parameters.
These are source scattering factors, not target Euler factors. The
spectral parameter is not an ordinary dynamical clock.

Tables: character square/phase parity cases and the exact prime-exponent
conditions; a small N=50/100 comparison illustrates the repaired logic.
Use actual Young/classical source metadata and retain Huxley/Keil access
limits. Do not turn the small counterexamples or principal lemma into
additional papers or a spectral realization claim.

## C421: all-parameter integer cycles and per-level counts

One-sentence contribution: a parameter-independent extremal-difference
reduction and a terminating exact finite certificate give every integer
cycle of T_a, its least period and its invariant-level multiplicity.

| Claim | Accepted proof/evidence | Manuscript location |
| --- | --- | --- |
| All-height, all-parameter residual core | `continuation_round2/integral_return/IR1_PROOF.md`, §§1–3; independent analytic review | §§2–4 |
| Exhaustion without any period cutoff | Same proof §4; author certificate and independently structured backward two-sign certificate | §5 and typeset appendix |
| Disjoint unbounded families and two exceptions | `IR1_CLASSIFICATION.md` and completed coordinator review | §6 |
| Exact per-level oriented counts and native zeta | Classification formulas and symbolic verification receipt | §7 |

Structure: complete theorem/table and source ownership; invariant and
ordinary recurrence; long-family extraction; maximum-difference bound
\(1\le D\le100, |x_i+1|\le3D\) for the residual; fully specified
finite seed certificate and stopping proof; least-period/disjointness
and reversal analysis; per-level square tests, native counts and limits.
Least periods are exactly {1,2,3,4,5,6,8,9,12}. Include all ten table
rows, parameter exclusions, the a=-13 five-cycle and a=-2 nine-cycle.

Finite evidence: 74,866 author seeds and 149,732 independently rebuilt
two-sign seeds, with 25,851 oriented cycles matched individually. These
are the already accepted executions, not fresh tests. Include algorithms,
exact ranges and preserved outputs in the release; do not rerun them
without changed inputs or a concrete unresolved risk. The proof table
also parametrizes unbounded families, not only this finite core.
No all-level finite-count zeta is asserted. Tables and pseudocode are
material; no fresh parameter scan or synthetic experiment is planned.

## C422: all-characteristic integral fibres and native periods

One-sentence contribution: boundary-lattice and minimal-pole arguments
show that every finite invariant fibre of the resolved native q-Painleve
space is integral and reduced, yielding the uniform orbit bound including
all exceptional lines and characteristics two and three.

| Claim | Accepted proof/evidence | Manuscript location |
| --- | --- | --- |
| Compactification of exactly the native seven-branch space | `continuation_round8/painleve/PROOF_PACKAGE.md`, §§2–3 | §§2–3 |
| Boundary lattice and minimal pole order r=ord(s) | Same proof §§3–5 | §§4–5 |
| Every finite fibre integral, reduced and genus one | Same proof §§5–6; complete `painleve_review/REVIEW.md` | §6 |
| Every native orbit has r dividing ell and ell/r<=q+1+2 sqrt(q) | Same proof final sections | §7 |

Structure: full native statement; exact torus/line charts and regular
invertible evolution; eight-blowup boundary cycle; orthogonal lattice and
pole-index obstruction; source integral and positive-characteristic
reduction; irreducible/reduced finite fibres; smooth and singular point
counts and phase-clock conversion; source/target scope and reproducibility.

The phase multiplier is s and the field cardinality q; do not silently
identify these. The proof must retain all t!=0, every accessible line
point, no unproved source discriminant formula and no assumption that
all finite fibres are smooth. Tables: eight blowup centres/classes,
seven native branches and a source-versus-proved-bound comparison.
Use Joshi–Roffelsen's actual checked version and credited integral/chart
construction, plus verified classical geometry/Hasse sources. Do not
claim the bin-distribution conjecture or full target arithmetic.

## C423: a concise complete residual example

One-sentence contribution: a universal two-cycle parameter excludes both
nonzero differences left for x^4+x^6 by the equal-weight reduction and
classifies simultaneous preperiodicity over every characteristic-three
field and every marked pair.

| Claim | Accepted proof/evidence | Manuscript location |
| --- | --- | --- |
| Three-value reduction and universal local-height bridge | Lee–Nam v2 Theorems 1.5/4.4 and 2.1, exact imports verified in `continuation_round9/CP9_ADMISSION_REVIEW.md` | §2 |
| Universal period-two/escape parameter and positive height | `continuation_round9/charp_alternatives/PROOF_DRAFT.md`, Lemma 2 | §3 |
| Arbitrary-field reduction, both signs and sufficiency | Same full proof and `charp_review/REVIEW.md` | §§3–4 |

Structure: main theorem and the precisely named source gap; local-height
input and constant-field conventions; explicit orbit identities and
escape at a pole; full arbitrary-field proof and elementary single-point
parameter infinitude; limitations/disclosure. All proof belongs in the
article. State exact least period two in the nonconstant case and apply
the one-point lemma to the fixed marked point a.

Tables: a small comparison of monomial/strict-weight/this fixed equal-
weight scope, with precise source qualifications. The two orbit segments
are displayed equations; no standalone diagram is needed. Cite verified
Lee–Nam v2 and Ghioca–Hsia metadata, with the height theorem expressly
accessed as stated in Lee–Nam. Do not imply the original height proof
was independently read or that the preprint is already a journal paper.
The note is allowed to be short: no padding, additional signs-as-papers
or unsupported all-binomial/colliding-orbits generalization.

## Review and release routing

The independent outline review checks exact claim/evidence coverage,
source ownership, proof placement, table choices and the completeness of
each distinct question. The reviewer may request minimal scope-preserving
repairs. After closure, authors write only their allocated manuscripts.

New manuscript reviews read actual complete TeX/Bib/PDF text and compare
them to the accepted proofs. An old proof PASS does not certify new
transcription. Two real improvement passes retain full review text and
affected revision closure; a clean first pass does not require invented
changes. Formal evaluations and all scope flags remain coordinator-owned.

For final PDFs use two fresh build directories per paper under recorded
deterministic settings. Compare bytes, inspect text/fonts/logs, and
visually inspect every final page. Record true command exits and hashes.
No repeated build of an old released paper is planned. Final release
uses an exact payload ledger, self-excluding manifest, failure-path-tested
release checker and a completed read-only verification after sealing.

Only after those gates may the coordinator stage exact authorized paths,
inspect remote advancement and synchronize using the existing standing
authorization. Do not stage the inherited eight unrelated untracked
directories, alter old frozen packages, create new remotes or publish to
a journal. Stop at the five-paper C423 handoff.
