# Pre-Review Integrity Verification

## Disposition

**PASS WITH ADVISORIES.**  On the frozen manuscript snapshot below, no
integrity blocker, fabricated result, unsupported citation context, missing
figure trace, dangling experiment pointer, or scope-changing inference was
found.  The remaining advisories are provenance or maintenance limitations;
none changes a scientific claim in the current manuscript.

| Item | Frozen value |
|---|---|
| Manuscript | `paper/manuscript.tex` |
| Manuscript SHA-256 | `f0923046d4af14dc4373f4698781770bd3545f1a28a5c08d15558421c2903f4a` |
| Source-lock SHA-256 | `20473ff34b1f9258281483f47b9db915eb2680d2a71e9e1e6e9f3cf3d6fc07c8` |
| Frozen code-tree SHA-256 | `ad7f6637a90e6f5cfc4933b89adc70c543c0d0f259f295ea84da10c6fa5f0b11` |
| Verification-manifest SHA-256 | `e3e79e94e1e7ec684cd66748498c7aba238eb25bbef629c778a069b755640c54` |
| Final-result-manifest SHA-256 | `f0bf05b8fddeac66b341bffc91eae3c20d65909bf9d1ce8b7d30d269f7dc9792` |
| Citation audit | `notes/CITATION_VERIFICATION.md`, 13 records |
| Claim registry | `paper/CLAIM_MANIFEST.json`, 17 claims |
| Experiment passport | `paper/EXPERIMENT_PASSPORT.json`, 8 experiment records |
| Figure package | `paper/FIGURE_PACKAGE.json`, 3 complete traces |

This report is a pre-review integrity gate, not peer review and not an
independent rerun of the sealed experiment.

## Executive gate table

| Gate | Coverage | Result |
|---|---:|---|
| References and citation contexts | 13/13 bibliography keys used; 21 citation-key occurrences checked | **PASS** |
| Quantitative and data claims | All manuscript result values and hashes checked against frozen artifacts | **PASS** |
| High-impact theoretical claims | Finite-rank theorem, carrier proposition, candidate corollary, and formal decision checked | **PASS** |
| Claim-to-experiment alignment | 15 explicit alignment rows; no dangling claim or experiment ID | **PASS** |
| Figure/table trace | 3/3 figures; source, transformation, output, caption, reverse link, and limitation present | **PASS WITH ADVISORIES** |
| Originality screen | 24/54 substantive prose paragraphs sampled (44.4%; requirement 30%) plus full local duplicate scan | **CLEAR WITH METHOD LIMITS** |
| Scope and narrative consistency | Research question, source lock, paper plan, results, and conclusion compared | **PASS** |
| Seven AI-research failure modes | 7/7 assessed below | **CLEAR** |
| Clean LaTeX/BibTeX build | Isolated `pdflatex -> bibtex -> pdflatex x3` | **PASS**, 16 pages, no unresolved citations/references |

## 1. Citation and prior-art integrity

The bibliography contains 13 entries and the manuscript uses all 13.  The
manuscript has 21 citation-key occurrences, no missing key, no unused key, no
duplicate label, and no unresolved reference on a clean build.  Each citation
context was compared with the claim boundary in
`notes/CITATION_VERIFICATION.md`.

Particular high-risk contexts are correctly limited:

- `alseda2025realteapot` supports the broader kneading context only.  The
  worked determinant is derived in this manuscript and is not attributed to
  an unverified exact page/formula.
- `hofbauer1985periodic` and `rugh2015kneading` support historical
  boundary-sensitive coding and weighted kneading context; neither is said to
  prove this project's specific quotient.
- `bruin2014natural`, `bose1989generalized`, `balazs1989quantized`, and
  `saraceno1990classical` establish classical carrier/quantization precedent
  without implying a canonical quantization of this candidate.
- `ji2026space` is explicitly restricted to non-exceptional rational maps of
  degree at least two and period-normalized characteristic exponents.  The
  manuscript does not transfer that theorem to arbitrary smooth or
  symplectic maps.
- `wang2026prime` now records the candidate genealogy: the Logistic
  band-merging parameter and prime-symbolic motivation are inherited.  The
  manuscript explicitly says it does not revalidate that study's prime-sieve
  claims, import its prime data, or reuse its non-autonomous construction as
  the autonomous carrier.

The Wang content check used the archived article PDF with SHA-256
`78a65db26110ef8173c3d7dc50caf2b598e59b854e7b5afa3983891008cb953e`.
PDF page-anchor preflight was unavailable because `pypdf` was not installed;
the audit therefore used full-text extraction and does not claim trusted page
anchors or verbatim quotation verification.  This limitation does not affect
the narrow genealogy claim.

**Citation verdict: PASS.**  No ghost citation, unsafe attribution, citation
laundering, or absolute priority claim was found.  The novelty audit remains
properly described as targeted rather than systematic.

## 2. Data, computation, and formal-decision integrity

All numerical statements in the abstract, main text, captions, tables, and
reproducibility appendix were traced to raw frozen files.

| Manuscript claim | Frozen evidence | Result |
|---|---|---|
| Primitive vector through period 20 and total 226; two exact methods agree | `results/ledger.json#/primitive_counts`, `#/independent_direct_counts`, `#/ledger_agreement`, `#/primitive_total`; redundant `results/exact_preflight.json#/cycle_audit` | **PASS** |
| Sole parent-boundary replacement, delta `(1,-1,0,...)`, parent counts and zeta | `results/ledger.json#/parent_boundary_quotient`; `results/exact_preflight.json#/boundary_quotient`; `results/parent_audit.json#/periodic_factor` | **PASS** |
| `W^3=0`, unsigned/orientation/parent/Lefschetz conventions remain separate | `results/exact_preflight.json#/zeta`; `results/ledger.json#/determinant_conventions` | **PASS** |
| Rank-one multiplier clock and only `p=2` | exact proof at manuscript lines 633--645; `results/ledger.json#/cycle_rows`; `results/analysis_test.json#/gates` | **PASS** |
| Independent parent audit: 100 digits, period 20, max residual `9.706e-98`, target `1e-75`, max 293 iterations | `results/parent_audit.json` | **PASS** |
| Each split: `65,536 x 256 = 16,777,216`, max error `1.3877787807814457e-16`, zero edge/boundary failures | three `results/float_stress_*.json` files | **PASS** |
| Six matched controls and dyadic total 747 | `results/exact_preflight.json#/controls`; source-lock prediction; named passing pytest assertion | **PASS WITH GRANULARITY NOTE** |
| 89 tests, zero failure/error/skip | `results/pytest_development.xml`; final manifest integrity flag | **PASS** |
| No external prime/zero data | source lock, exact/ledger/parent/float/analysis/final artifacts all declare false; static isolation passes with zero violation | **PASS** |
| Formal outcome | `results/final_result_manifest.json#/classification`; `results/analysis_test.json` | **PASS** |
| Source/code/verification hashes, split seeds, amendment, environment | source lock, markers, final manifest, amendment, checksum report | **PASS** |

The formal outcome is reported consistently as
`PRE_A0_STRUCTURAL_PASS`, `A0_FAIL / STRUCTURAL_ONLY`, `A1_WEAK`, A2--A4
`STOP_SCOPED`, Route B `FORBIDDEN`, and overall `ROUTE_A_REJECTED`.  The
frozen analysis JSON field `a1_status=PASS_PIECEWISE_EXACT_SYMPLECTIC_INTERIORS`
is a carrier-geometry label, not `A1_PASS`; the final manifest records that
post-test label clarification and the manuscript follows it.

The frozen pytest XML records 89 tests with zero errors, failures, and skips.
`sha256sum -c results/REPORT.sha256` returned **25/25 OK**, and every hash in
the final manifest was re-resolved to its source artifact/report.  Validation
and test markers carry the correct source lock, code tree, analysis hash, and
prior-stage artifact chain.  The verification manifest predates the logged
test access.  The sealed test was not rerun during this audit.

The 747-control value has one non-blocking evidence-granularity limitation:
the raw exact-preflight JSON stores `dyadic_ledger_total=true`, not a separate
numeric `747` field.  The number is predeclared in the source lock, asserted by
the named passing pytest case, and repeated in frozen reports.  The claim is
supported, but a future schema could freeze the numeric value directly.

**Data and computation verdict: PASS WITH ONE NON-BLOCKING GRANULARITY
ADVISORY.**  No invented, inconsistent, or selectively reported number was
found.

## 3. Claim-to-experiment passport alignment

`CLAIM_MANIFEST.json` registers 17 substantive claims, their exact manuscript
locations, evidence kind, citation links, result pointers, scope constraints,
and forbidden inferences.  `EXPERIMENT_PASSPORT.json` records eight evidence
units: exact preflight, ledger, independent parent audit, three split-specific
floating stresses, formal analysis, and the frozen test suite.  Its 15
claim--experiment joins resolve without a dangling ID.

The passport includes both negative results and known limitations.  In
particular it preserves the candidate's negative arithmetic outcome, the
matched dissipative/anti-symplectic/label-erasure/sign-null failures, the
one-step nature of the floating stress, the non-interval parent audit, the
finite period-20 ledger scope, and the unopened downstream gates.

This check verifies disclosure and claim-to-provenance fidelity. It does not
judge whether the experiment was correctly designed, run, statistically
adequate, or reproducible by ARS.

**Experiment-alignment verdict: ALIGNED.**  The passport is explicitly a
retrospective pre-review registry; it is not misrepresented as a pre-draft
precommitment.  The contemporaneous design commitment is
`experiments/source_lock.json`.

## 4. Figure-package integrity

`FIGURE_PACKAGE.json` contains a complete record for all three manuscript
figures.  Each record includes `artifact_id`, `source_data`, `transformation`,
hashed PDF/PNG outputs, atomic `caption_claim` verdicts,
`supported_manuscript_claims`, reverse-link counts, and nonempty
`limitations`.

| Figure | Caption atomic claims | Definition / substantive references | Trace verdict |
|---|---:|---:|---|
| `fig:carrier-obstruction` | 5/5 supported | 1 / 1 | **PASS** |
| `fig:orbit-lattice` | 5/5 supported | 1 / 1 | **PASS WITH ASSERTION-COVERAGE ADVISORY** |
| `fig:computational-audit` | 5/5 supported | 1 / 1 | **PASS** |

An isolated rerender left the workspace untouched.  All three PNGs were
byte-identical.  Raw PDF hashes changed because Matplotlib writes a
`CreationDate`; after neutralizing that single metadata field, all three PDFs
were byte-identical.  This matches the manuscript's explicit limitation and
is not a scientific-rendering difference.

The current manuscript's Figure 3 caption and the synchronized fallback
caption both correctly say the dyadic control tests
`enumeration/symplecticity`.  Figure 2's generator plots the frozen
primitive vector but does not itself assert total 226, method agreement, or
equality with the independent direct counts; those claims were separately
checked against the complete input JSON.

**Figure verdict: PASS WITH ADVISORIES; zero current-manuscript failure.**

## 5. Originality and duplicate-text screen

The paragraph population was defined mechanically from manuscript lines
57--1008: split on blank lines, remove LaTeX commands/citation/reference
markup, normalize to lowercase alphanumeric words, retain blocks of at least
15 words, and exclude eight caption/table blocks.  This produced 54
substantive prose paragraphs; the 30% integrity threshold is 17 paragraphs.
Twenty-four distributed paragraphs were sampled (44.4%):

`57--78, 83--90, 101--106, 108--115, 128--141, 185--200, 202--211,
254--263, 268--286, 323--329, 366--375, 382--416, 470--493, 544--566,
633--645, 669--677, 681--688, 690--702, 743--754, 780--790, 801--807,
826--838, 863--881, 990--1008`.

The archived Wang article was extracted in default, layout, and raw modes.
No 12-word normalized run matched.  The longest meaningful match was the
four-word phrase `non autonomous logistic map`, occurring in the newly
attributed genealogy context.  Paragraph-level stopword-filtered 1--2 gram
TF--IDF had maximum cosine similarity 0.086, not a substantial duplicate.

A full local scan covered 98 other `.tex`/`.md` files (1,896,922 bytes).
Twelve 12-word-or-longer matches all came from this project's own planning,
source-lock, proof, result, validation, or frozen-candidate records.  After
excluding those provenance sources, the longest repository match was nine
words.  No old paper or external manuscript produced a 12-word run.

Targeted exact-phrase Web searches through 2026-08-13 were also distributed
across the abstract, introduction, theorem, carrier construction, ledger,
audit, controls, and conclusion.  They did not reveal an unattributed exact
source.  This is a heuristic screen, not a professional plagiarism-database
certificate.  It cannot exclude translation, heavy paraphrase, private or
unindexed text, and the local PDF page divisions were not trusted page
anchors.

**Originality verdict: CLEAR WITH METHOD LIMITS.**  Internal reuse from the
project's own plan/proof/result provenance is visible and expected; no
substantial unattributed reuse from the author's prior paper was detected.

## 6. Scope, proof, narrative, and research-question consistency

The manuscript answers the frozen evaluative question: the carrier succeeds
geometrically but fails the arithmetic clock gate.  Its main theorem is stated
and proved with the required assumptions: one fixed finite graph, finite
memory, locally constant nonzero scalar weights, modulus-based additive
length, and exact termwise prime-log containment.  The proof correctly uses
higher-block recoding, finite spanning, rational independence of distinct
prime logarithms by unique factorization, and the closed-walk span bound.  The
finite-loop sharpness example is disclosed as explicitly inserting a finite
prime list.

The carrier proposition separately proves branchwise exact symplecticity from
the affine derivative and Liouville primitive.  It is limited to branch
interiors/almost everywhere and does not become a global smooth
symplectomorphism, a smooth submersion, or a full inverse-limit
homeomorphism.  The constant-slope baker cocycle is never substituted for the
nonlinear parent derivative.  Factor orientation, symplectic orientation,
Lefschetz convention, and quantum/Maslov phase remain distinct.

The negative result is not narratively inverted into success.  The manuscript
contains no `surprisingly`, `unexpectedly`, `counterintuitively`, `state of
the art`, or absolute `first-to-prove` rhetoric.  A valid carrier is consistently
described as a structural positive control and an arithmetic negative control.
The Wang genealogy paragraph and prior-art table now close the only identified
research-lineage gap.

**Scope/narrative verdict: PASS.**  No research-question deviation or
post-result scope expansion was found.

## 7. Seven AI-research failure modes

The failure-mode classifications use fail-closed evidence.  `CLEAR` means no
indicator was found in the audited snapshot; it does not claim philosophical
impossibility.

### Mode 1 — Confirmation without genuine execution: CLEAR

Evidence includes raw exact, ledger, independent parent, three split, and
analysis artifacts; 89-case pytest XML; source/code/artifact hash chains;
split access markers and access log; independent direct enumeration; matched
controls; and a byte-identical development rerun recorded in the final
manifest.  The manuscript does not pretend a literal historical shell log was
retained and does not claim that integrity hashing proves the theorem.

### Mode 2 — Fabricated or misused citations: CLEAR

All 13 bibliography entries were metadata-audited from DOI/publisher or
authoritative repository records, all are used, and all 21 citation-key
occurrences fall inside recorded safe-claim boundaries.  The high-risk
Teapot, Ji--Xie--Zhang, and Wang contexts are explicitly limited.  No ghost
key or citation-as-proof substitution was found.

### Mode 3 — Fabricated or inconsistent numerical results: CLEAR

Every reported value was found in a frozen raw artifact or in a transparent
exact calculation from such values.  The full report checksum and final
manifest index resolve without mismatch.  Rounding in the prose is correct,
and limitations on deterministic stress, precision, and period range are
retained.

### Mode 4 — Weak or misleading baselines: CLEAR

The controls change identified features: dyadic enumeration/symplecticity,
folded paired reversal, matched dissipation, label erasure, single-coordinate
anti-symplectic reversal, and all-positive sign null.  These distinguish code,
invertibility, symplecticity, and sign convention.  The paper does not turn
them into arithmetic baselines or A2--A4 evidence.

### Mode 5 — Narrative overfitting after seeing results: CLEAR

The source lock predeclares a negative answer as complete, freezes the
finite-rank clock prediction and stopping rule, and forbids reopening
downstream paths after A0 failure.  The final narrative preserves that
negative outcome and avoids surprise/primacy rhetoric.  Scope qualifications
are stronger, not weaker, in the conclusion.

### Mode 6 — Methods not matching executed work: CLEAR

The manuscript's reconstructed command order, seed derivation, correction
timing, scales, thresholds, split gates, immediate roundtrip definition,
independent parent method, and environment match the code-facing artifacts.
It explicitly says the command list is a reconstruction, that PDF raw hashes
are timestamp-sensitive, that the parent audit is not interval arithmetic,
and that floating operations are not independent observations.

### Mode 7 — Research-question drift / frame lock: CLEAR

The selected question permits rejection of the candidate; the paper reports
that rejection.  Classical construction components and the inherited Wang
genealogy are attributed, and the remaining claim is restricted to the
finite-locally-constant certificate.  Broader variable-roof, smooth,
countable-state, coupled, and higher-dimensional models are declared new
candidates requiring new source locks rather than post-hoc repairs.

## 8. Build and machine-readability checks

- `CLAIM_MANIFEST.json`, `EXPERIMENT_PASSPORT.json`, and
  `FIGURE_PACKAGE.json` parse as strict JSON.
- Every registered result/source/output path exists, every listed SHA-256 was
  recomputed, and every JSON pointer used for claim alignment resolves.
- Every experiment ID referenced by a claim exists in the passport; every
  alignment claim ID exists in the claim manifest.
- The manuscript compiled in an isolated temporary directory with the three
  frozen PDF figures using `pdflatex`, `bibtex`, and three final `pdflatex`
  passes.  The output is 16 pages, with no unresolved citation, reference, or
  duplicate-label warning.
- No validation or test execution was performed during this audit.

## 9. Non-blocking actions before submission

1. If the exact-preflight schema is revised in a new frozen run, record the
   numeric dyadic total `747` alongside its boolean gate.
2. Preserve the current paragraph around `wang2026prime`; removing it would
   reopen the candidate-genealogy integrity finding.
3. Preserve the manuscript distinctions between immediate one-step
   roundtrips and long-trajectory reversal, between high precision and
   interval proof, and between carrier geometry and the formal `A1_WEAK`
   verdict.
4. Re-run this gate if `manuscript.tex`, any cited raw artifact, any figure
   generator/input, or `references.bib` changes after the recorded hashes.

## Final verdict

The current 16-page manuscript is **eligible for external review**.  It has a
closed citation chain, a closed quantitative evidence chain, a complete
figure package, a claim-aligned experiment passport, and no suspected instance
of the seven screened AI-research failure modes.  The two remaining
advisories—the dyadic numeric-field granularity and PDF `CreationDate`
nondeterminism—are disclosed and do not undermine the
current manuscript's claims.
