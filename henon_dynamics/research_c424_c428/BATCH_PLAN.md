# C424–C428: five admitted contracts and manuscript plan

2026-09-09 UTC. Research state: **FIVE_SUBSTANTIAL_CONTRACTS_ADMITTED**,
by the coordinator's [actual decisions](ADMISSION_DECISIONS.md).
Outline state: **APPROVED_FOR_MANUSCRIPT_DRAFTING**.
The coordinator read the complete 255-line [independent outline review](REVIEW_OUTLINE.md)
and closes the gate on 2026-09-09 UTC. Its sole required correction,
O1 (C425's explicit Shin ownership deduction), was implemented and
read back by the reviewer; zero mandatory items remain. Report hash:
`52885c212b4a47de96344f8dae30bb2ee8517a1ebd46eeec6ae0c3350150528b`.
Only this administrative gate/numbering header changed after that review;
the five reviewed contracts and body plans are unchanged. Numbering below
is now the active five-paper assignment, not completed-paper status.
No sixth paper, C429, Route B or external submission is authorized.

## Shared format, evidence and completion gates

Use anonymous English mathematical articles, as in the preceding
authorized C-series batch: 11pt, approximately one-inch margins,
modular LaTeX, explicit theorem hypotheses and source attribution.
No journal, ML conference, artificial page limit, minimum section
quota, synthetic experiment or decorative illustration is selected.
Do not invent author identities, funding, human review or ethics
approval. Report AI-assisted preparation and current-team internal review.

The selected `paper-writing` workflow uses `paper-plan`, `paper-figure`
for substantive exact tables, `paper-write`, `paper-compile` and
`auto-paper-improvement-loop`. All relevant entry instructions and
required writing, venue and citation references were read by the
coordinator before planning. Legacy GPT-5.4/MCP/GPU examples do not
replace the current-team contract; no paid model, model switch or
external manuscript upload is performed. Preserve **two actual
manuscript review/revision passes** from that selected improvement
workflow, without fabricating edits or rising scores when none occur.
This is not a reason to repeat unchanged mathematical executions.

ARS is used only for bounded source/citation checks, not its full
research-to-paper pipeline, venue disclosure certification, Socratic
interview or generator-evaluator passport. Its citation-compliance
instructions and format reference have been read. Use the established
numbered mathematical bibliography, match every citation to an actual
reference and retain verified DOI/URL metadata. Missing DOI metadata,
unperformed retraction/venue/interest checks and local unpublished
sources must be identified, not silently marked verified. Internal
working notes are cited as such, without invented human authors.

Every central new argument belongs in the article or its included,
typeset appendix. A local Markdown link is not a substitute for that
argument. Previously proved results may be imported as precisely
stated, attributed theorems with complete accessible references and
their actual evidence status. Tables and pseudocode must be faithful
to accepted proof inputs; do not turn finite evidence into an
infinite-parameter numerical claim.

After the outline gate: draft and make actual PDFs; obtain the two
real nonauthor manuscript reviews, adjudicate and repair blocking
issues, and verify affected reasoning. Formal Route-A evaluation uses
unchanged v0.2.0, with the coordinator's completed
[reference routing](EVALUATION_REFERENCE_ROUTING.md). This plan assigns
no grades. Missing target tests remain NOT_TESTABLE/INCOMPLETE;
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.

The final release requires two fresh deterministic builds per paper,
byte comparison, font/text/warning checks and visual inspection of
every final page. Preserve actual baseline/revision files and failed
attempts if any. Seal the exact payload only after writers stop;
verify the final ledger and self-excluding manifest read-only, obtain
independent membership verification, then integrate exact authorized
paths and synchronize after inspecting any remote changes. Stop at C428.

## Assignments and ownership

All paths in this table are relative to this batch directory.

| Paper / working title | Complete object | Manuscript owner and path |
| --- | --- | --- |
| C424 — Rational periodic points of integer-valued quadratic Hénon maps | Every degree-two `P in Int(Z)`; `(y,P(y)-x)` on all `Q²`; exact rational cycles, least periods and sharp point bound | `round6_positive_characteristic`, after outline review; `papers/C424_integer_valued_quadratic/` |
| C425 — Integral periodic orbits of a general Fricke return word | All ordered integer `(A,B,C)`, native `T=s_z s_y s_x`, all integer points and all invariant levels | completed IH6 nonauthor reviewer, after outline review; `papers/C425_fricke_return/` |
| C426 — Affine good models of single-factor Hénon maps | Every number field, all `a!=0`, all polynomials of degree at least two, all local/global two-dimensional affine changes | `lyness_round5`; `papers/C426_affine_good_models/` |
| C427 — A semilinear atlas for integral Vieta recurrence cycles | `F=(x_2,...,x_n,x_2...x_n+a-x_1)`, all `n>=3`, all integer forcing, the entire integer lattice across all levels | coordinator; `papers/C427_vieta_semilinear/` |
| C428 — Integer periods of single-factor Hénon maps of arbitrary degree | Every `p in Z[t]`, `deg p>=2`, both `a=+1,-1`; exact union of native integer least periods of `(y,p(y)-a*x)` | `lyness_round5`; `papers/C428_integer_period_spectrum/` |

Authors own only their assigned manuscript directories. The coordinator
owns shared state, this plan, evaluations, final build integration,
release and Git. Reviewers write disjoint review paths and do not
self-admit their own manuscripts. Authors may read proof/source inputs
during outline review, but no draft is produced until the gate closes.
Completed proof packages retain their historical author-status wording;
the coordinator's admission decisions determine the latest state.

## C424: the whole integer-valued quadratic rational atlas

One-sentence contribution: the missing half-integral normal form is
completely classified, giving all rational cycles of every quadratic
integer-valued polynomial, sharp bound 17, and its full equality locus.

| Claim | Accepted inputs | Planned location |
| --- | --- | --- |
| Odd/even Newton-basis affine normalization on all rational points | `arithmetic_maps/PROOF_PACKAGE.md`, Step 7; `CLASSIFICATION.md` | §§2–3 |
| Normal-form integrality and all large negative parameters | Full analytic proof and C412's explicitly deducted local-word input | §§3–5 |
| Complete finite residual, without period cutoff | `FINITE_CORE_CONTRACT.md`, author code/result and `arithmetic_spectral/AM1_REVIEW/` independent code/result | §6 and typeset appendix |
| All cycles, least periods, coexistence, sharp point bound and equality locus | Full `CLASSIFICATION.md` and completed review/closure | §§7–8 |

Write `P(t)=m*t*(t-1)/2+n*t+r`, `m!=0`. For odd `m`, use
`q=n-(m+1)/2`, `A=mr+(3q-q²)/2`, and the bijection
`(x,y)->(mx+q,my+q)` to `F_A=(y,y(y+1)/2+A-x)`.
Even `m` imports the exact C412 monic integral quadratic result via
the stated scaling. Original rational coordinates need not be integral.

Include all four parametric cycle rows and eleven exceptional cycles,
the ordinary cycle-count formulas and the equality condition `A=-1`
for odd `m`. Least periods are exactly `1,2,3,4,5,6,7,9,10`.
The proof threshold is `a<=-146`; the actual 147-map certificate
covers `-145<=a<=1`, with `a=1` a separately proved control.
The independent original-coordinate reconstruction matched every cycle
and point, not only 306 total states and 113 cycles across the family.
Those totals are not one map's point bound. Retain the finite
computer-assisted dependency and do not rerun unchanged certificates.

Credit C412's annulus, six-symbol and finite-graph mechanisms. The
normalization is elementary, and method novelty is low. The complete
natural coefficient-class extension is the one admitted increment;
the exceptional table, nine periods and zeta are not separate results
for paper counting. No arbitrary rational-coefficient classification
or target Euler interpretation is asserted.

## C425: all ordered Fricke coefficients and all integer levels

One-sentence contribution: a forced maximum-height argument exhausts
all unbounded integral cycles into at most 27 affine lines and gives
a terminating exact finite residual rule for every ordered coefficient
triple, including exact least periods and level counts.

The central new proof is the complete
`continuation_round3/nonlinear_geometry/PROOF_PACKAGE.md`, with
`continuation_round3/nonlinear_geometry_review/REVIEW.md` and the
nearest-source comparisons in the original nonlinear-geometry scout.
Include the whole proof, not only the classification algorithm.

Structure: full theorem and source ownership; the native word and
invariant; the three-phase auxiliary lift; maximum-height entry;
the complete Type I/II 27-state graph; forcing 27 transitions above
`R=100(1+max(|A|,|B|,|C|))`; affine cycle-return test; finite residual,
line intersections and exact least-period exceptions; ordinary level
counts and limitations. A whole `T` is the clock: three lift steps
are one native iteration, and the intermediate phases cannot be dropped.

Tables: the two exact edge formulas and their parameter conditions,
retained/nonretained affine returns, and the source/new-scope comparison.
Every retained line has a proved native return time at most 54; it
does not follow that this is its generic or every point's least period.
Use polynomial gcd/integer roots for all exceptional line parameters,
and remove duplicates before counting. Each level intersects a line
in at most two points; no whole-lattice finite-count zeta is asserted.

The Fricke surface, Vieta involutions and finite-graph bookkeeping are
classical. Deduct C421's equal-forcing scalar classification, Shin's
independent-coefficient scope and height-graph/low-coordinate mechanisms
(`Character varieties on a four-holed sphere`, arXiv:2308.16614v3,
Theorems 1.1–1.3 and Remark 3.1), and Cantat's fixed-fibre input.
Independent Fricke coefficients alone are not a new extension of Shin.
The new theorem is unequal-forcing global
exhaustion with an explicit uniform residual rule. No finite core was
actually enumerated in this proof-only branch; neither a sharp bound
nor a practical complexity guarantee is claimed.

## C426: all affine good models and the ideal-square obstruction

One-sentence contribution: the dynamical good-reduction conditions
force every possible affine lattice to be one unique disc square,
leading to an all-coefficient local test and the exact global
obstruction `[I]^2=1`, including nonprincipal ideals and wild centres.

Read the full `continuation_round5/arithmetic/FROZEN_CONTRACTS.md`,
`PROOF_PACKAGE.md`, `SOURCE_AUDIT.md`, `DISPOSITION.md`, and
`continuation_round5/GR5_REVIEW/REVIEW.md`. Preserve its closed
left-coset/right-composition wording correction.

Structure: main classification and regular good-reduction definition;
all-affine highest-term/indeterminacy rigidity; one-dimensional
auxiliary `q=f-aY` and unique good disc; every residue characteristic
and the finite centre test; finiteness of exceptional places and
global centre patching; `I⊕I` and the exact Steinitz obstruction;
all global coordinate maps, representative independence, two examples
and precise limitations. Include all necessity arguments: it is not
enough to display a successful common scalar change.

For each finite place the scale exponent is `-v(b)/(d-1)` and must be
integral, while `v(a)=0`. With `r0=-q_(d-1)/(d*b)`, all centre classes
are tested among `r0+(s/d)*beta`, `beta in O/dO`; do not omit wild
branches. Once all local tests pass, `(b)I^(d-1)=O_K`, and global
models exist exactly when `I²` is principal, not when `I` is principal.
Include both the nonprincipal two-torsion repair and three-torsion
failure examples, with their actual field/ideal calculations.

Deduct Kawaguchi's definition and height input, Bruin–Molnar/Petsche–
Stout's adjacent model theory and classical disc/lattice/Steinitz
facts. Local/global formulas and examples are one integrated result.
No field extension, nonaffine conjugacy or multiple-factor Hénon
classification is included. The observable is good models, not native
orbit counts; `q` is not a replacement dynamical clock. Pure proof,
zero mathematical program runs and no target bad-Euler/root-number claim.

## C427: the original all-dimensional cross-level question

One-sentence contribution: mixed nonzero-block rigidity makes the
whole high-dimensional integer periodic recurrence piecewise linear,
yielding finitely many freely parameterized semilinear channels with
exact native least periods and a finite remainder uniform across levels.

Read the full `continuation_round6/nonlinear_geometry/PROOF_PACKAGE.md`
and `continuation_round6/NG2V_REVIEW/REVIEW.md`, including the original
R4/R5 contracts and the completed V4-H, V4-Z, V5-NZ inputs they route.
C421 owns the full `n=3` theorem and its inherited computer-assisted
certificate; quote it precisely as a prior result, not as new hand proof.

Structure: complete algorithmic theorem and semilinear output semantics;
native recurrence and invariant; classical integral-period input;
short and long nonzero blocks, including every mixed-zero boundary;
unique large factor and unit companions; finite small-coordinate/
large-sign tagging; necessary and sufficient linear systems and least-
period exclusions; constructive integer-cone parametrization; removal
of zero projected directions and finite remainder; inherited `n=3`,
per-level finite counts and limitations.

For `n>=4`, a nonzero update product involving a coordinate greater
than `|a|+4` in absolute value contains exactly one such factor and
only unit companions. This local fact, not the earlier overly strong
single-family guess, is the new global entry. All tag constraints
must be both necessary and sufficient. Output sets have the form
`b + N*v1 + ... + N*vr`, with free nonnegative parameters and exact
least-period labels. Overlaps/redundancy are allowed; do not imply
injective parametrization, independent direction vectors or a minimal
channel normal form. No polynomial constraint may remain on parameters.

Credit Pezda/Whang for uniform integral periods, Ginsburg–Spanier and
integer-cone theory for semilinear machinery, Hu–Tan–Zhang for adjacent
unforced full-group geometry, and C421 for the three-dimensional slice.
The proof-only `n>=4` result does not rely on the round-six exploratory
probe. A period bound alone is not enough for semilinearity, as the
review's polynomial-shear counterexample shows. Neither all-input
atlas computation nor target arithmetic has been performed.

## C428: arbitrary-degree, double-sign integer period spectrum

One-sentence contribution: integer congruences for an arbitrary-degree
secant remainder reduce the complete single-factor Hénon integer
period problem to finite restrictions and symbolic endpoint graphs,
giving the exact two sign-dependent spectra.

Read all six files in `continuation_round6/arithmetic/` and all actual
review/evidence inputs in `continuation_round6/IH6_REVIEW/`.
The main proof must include the full all-diameter reduction, not just
the two lists or a reference to a Python script.

Structure: exact union-of-least-periods theorem and closest-source
subtraction; native recurrence, integer translation and support;
secant remainder and all-degree congruences; three exhaustive large-
diameter templates; affine branch; integer interpolation and complete
small-diameter graph certificate; identity/exception-root large graphs;
all eleven realization witnesses; execution dependencies and limits.
Include pseudocode sufficient to reproduce both finite reductions,
all ten `D=0,...,9` restriction rows and the six large-template rows.

The positive set is `{1,2,3,4,6}`; the negative set is
`{1,2,3,4,6,8}`. The eight-cycle uses `p=t³-3t` and the native
negative-Jacobian recurrence. Do not assert a per-polynomial atlas,
sharp point count, arbitrary rational integer-valued coefficients,
nonunit Jacobian, number-field extension or multiple-factor result.

Deduct C417's positive list, witnesses and endpoint framework, C412's
quadratic case, classical interpolation/linear algebra and Pezda's
general planar period list. Kim et al.'s long cycles and Ingram's
rational quadratic conjecture have different coefficient/domain
quantifiers. No claim to solving that conjecture or to a new general
endpoint method is allowed. The two author executions and one
independent reconstruction are explicit computer-assisted dependencies;
do not rerun unchanged code only because it is typeset in a new article.

## Outline review request and handoff

The independent outline reviewer must check all five admitted contracts
against the actual source proof/admission boundaries, central proof
coverage, evidence semantics, nonduplication, author/reviewer separation
and the stated manuscript/release gates. Do not award scientific grades
or count this review as either of the two future manuscript passes.
Write the full report in `REVIEW_OUTLINE.md`; the coordinator will read
it completely and adjudicate before any manuscript drafting begins.
