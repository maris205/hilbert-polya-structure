# Stage 4.5 Round 2 independent originality and seven-failure-mode audit

Audit time: 2026-08-25T15:13:08Z  
Operating mode: ARS Phase D Mode 2 (final originality check) plus the seven-mode AI research failure checklist  
Audited manuscript: `paper/manuscript.tex`, SHA-256 `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`  
Author identity supplied for the self-reuse screen: Liang Wang, `wangliang.f@gmail.com`

## Independent disposition

- **Phase D: `PASS WITH LIMITATIONS`.** A new public-Web search run found no `CLOSE_MATCH` or `VERBATIM` item in the 37/74 body sample, the full title, or the newly revised materials sentence. This is not a professional plagiarism determination and is deliberately not labelled `CLEAN`.
- **Author self-reuse: `INSUFFICIENT EVIDENCE FOR CLEAN`; no actionable self-reuse signal in the reliably email-linked public subset.** The evidence boundary is corpus completeness and identity disambiguation, not a detected overlap.
- **Seven failure modes: `WARN_NOT_BLOCK`.** Modes 1, 3, 4, 5, and 6 are `CLEAR_BY_NON_APPLICABILITY`; Modes 2 and 7 are `INSUFFICIENT_EVIDENCE`; no mode is `SUSPECTED`.
- **Route accounting:** Route A = `NOT_TESTABLE`; Route B = `NOT_TESTABLE`; gate credit = `NONE`. This Phase D carrier does not advance either route or any gate.

All quoted and supplementary searches described below were executed afresh for Round 2. The earlier audit supplied the required stable sample design only; its search results and grades were not imported as evidence or conclusions.

## Protocol and input bindings

This audit applied the ARS `plagiarism_detection_protocol.md`, the Phase D and Mode 2 instructions in `integrity_verification_agent.md`, `ai_research_failure_modes.md`, and the Stage 4.5 boundary in `integrity_review_protocol.md`.

| Input | SHA-256 | Bounded use |
|---|---|---|
| `paper/manuscript.tex` | `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed` | Sole manuscript target for Round 2 |
| `notes/stage4_5_integrity_revision_patch_round2.json` | `421e969a54bcd5a783faeab1485605533e4465bd8b7e4289cdf522de0770ebc0` | Identifies the two Round 2 correction operations |
| `notes/stage4_5_integrity_revision_round2.tex` | `a93b64f5ad41ede0ddaef8ad6fa46800092a9abd5d75fb099d357b54ea2058a2` | Anchored Round 2 draft |
| `notes/stage4_5_integrity_revision_round2.tex.apply-report.json` | `88c2becd2a644537d3ba356f2b97eb9d3eecca00fdbab93713d02226e1b51765` | Mechanical application record only |
| `notes/stage4_5_revision_evidence_bundle_round2.json` | `c665cee2e8c2288fb2c8e17a0e7e7e935b8062813a42d67cc8cea892ed6c10a9` | Revision-chain binding only; not originality evidence |
| `notes/material_passport.json` | `004f73185723d519d1c6ab22a4888324856d01554ed8c91efabb0354a4658d7b` | Historical corroboration only |

The Material Passport is stale for manuscript binding: its `content_hash` remains the prior manuscript hash `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2`, not the audited Round 2 hash. Its `no_experiments_declared`, empty `experiment_provenance`, and `repro_lock=null` fields were therefore not treated as fresh binding evidence. The current manuscript's own no-data/no-experiment surfaces are the primary evidence for the applicable failure-mode checks.

## Deterministic 37/74 sampling ledger

The body denominator starts at the first numbered section and ends before `Declarations`. Abstracts, the Chinese summary, keywords, MSC metadata, headings without prose, display-only blocks, declarations, and bibliography commands are excluded. Blank-line-delimited prose blocks with at least eight natural-language words are counted; theorem, proposition, remark, and proof prose is included. Re-executing this rule on the Round 2 manuscript yields 74 eligible paragraphs, `P001`–`P074`.

Per the Round 2 instruction, the prior deterministic 37-paragraph sample was replay-fixed before examining any new search result. It was not reseeded from the changed whole-file hash merely because Round 2 corrected title/date and materials metadata. The sample is:

`P001, P002, P003, P005, P008, P009, P010, P011, P012, P013, P014, P015, P017, P019, P020, P024, P034, P036, P037, P039, P041, P046, P053, P055, P059, P060, P061, P062, P063, P065, P066, P069, P070, P071, P072, P073, P074`.

| Major section | Denominator | Sampled | Sample IDs |
|---|---:|---:|---|
| 1. Introduction and main results | 16 | 12 | P001, P002, P003, P005, P008–P015 |
| 2. Rational Witt sheaves and the extension | 7 | 3 | P017, P019, P020 |
| 3. Three descent lemmas | 15 | 4 | P024, P034, P036, P037 |
| 4. The all-index descent obstruction | 16 | 4 | P039, P041, P046, P053 |
| 5. The extension-theoretic formulation | 8 | 5 | P055, P059–P062 |
| 6. The finite-flat site and Dedekind-section assertion | 7 | 4 | P063, P065, P066, P069 |
| 7. Scope, controls, and conclusion | 5 | 5 | P070–P074 |
| **Total** | **74** | **37** | **50.0%** |

The title and the revised materials paragraph were screened separately outside the body denominator, as were the other declaration surfaces and the author-email self-reuse queries.

## D1 fresh paragraph-level public-Web comparison

For each of the 37 paragraphs, a normalized quoted characteristic fragment and a distinct unquoted supplementary query were submitted on 25 August 2026. Returned public results were reviewed for exact wording, long-sequence overlap, and semantically close re-expression. No quoted query reproduced its complete manuscript fragment. Search-engine snippets were discovery aids only; technical judgments used primary or official sources: Deninger's current primary preprint (`https://arxiv.org/abs/2508.05329`) and the Stacks Project pages on sheafification (`https://stacks.math.columbia.edu/tag/007X`), epimorphisms (`https://stacks.math.columbia.edu/tag/007T`), finite locally free morphisms (`https://stacks.math.columbia.edu/tag/02K9`), and Cech constructions (`https://stacks.math.columbia.edu/tag/01ED`). Non-primary technical pages returned by the engine were not used to support a judgment.

Result-set codes: `WITT` = Deninger/standard Witt theme only; `STACKS` = official sheaf/descent/finite-flat topic only; `ROOT` = standard roots-of-unity topic only; `EXT/CECH` = standard categorical or Cech topic only; `CAT` = generic functoriality; `REV` = unrelated revision material; `NONE` = absent or irrelevant results. None of these codes denotes a wording match.

| ID | Quoted exact-phrase query | Fresh supplementary query | Result | Round 2 grade and rationale |
|---|---|---|---|---|
| P001 | “the chosen factors must satisfy descent on the double overlap” | `chosen factors descent double overlap rational Witt sheaf` | WITT/STACKS | `ORIGINAL`: thematic descent results only |
| P002 | “treating an arbitrary skeleton as though it were automatically closed” | `arbitrary skeleton automatically closed algebraic geometry proof` | NONE | `ORIGINAL`: no relevant phrasing |
| P003 | “The word additive refers to the Witt addition, represented by multiplication” | `Witt addition represented by multiplication rational Witt vectors` | WITT | `COMMON_KNOWLEDGE`: standard big-Witt convention, no long copied sequence |
| P005 | “a finite-flat covering family of an affine scheme means a” | `finite flat covering family affine scheme jointly surjective` | STACKS | `COMMON_KNOWLEDGE`: standard site definition |
| P008 | “When one topology is fixed below, the unadorned symbols” | `unadorned symbols topology sheafification affine sites notation` | STACKS | `ORIGINAL`: notation sentence not found |
| P009 | “In particular e tau is nonzero and V N pullback” | `rational Witt extension class Verschiebung pullback nonzero` | WITT/EXT | `ORIGINAL`: result-specific formulation not found |
| P010 | “Read in this sectionwise sense, that assertion therefore requires correction” | `sectionwise assertion requires correction sheaf Verschiebung` | WITT | `ORIGINAL`: source theme only |
| P011 | “The exact source is Deninger's version-1 preprint Proposition 4.3” | `Deninger version 1 Proposition 4.3 rational Witt Verschiebung` | WITT | `ORIGINAL`: bibliographic synthesis, no matching sentence |
| P012 | “This bounded negative result is not a claim of global priority” | `bounded negative result global priority rational Witt lifts` | WITT | `ORIGINAL`: no matching expression |
| P013 | “Our contribution is correspondingly narrow we answer the additive lifting question” | `additive lifting question rational Witt Verschiebung finite flat site` | WITT | `ORIGINAL`: manuscript-specific contribution statement |
| P014 | “failure of an unrelated target section to have a global preimage” | `target section global preimage epimorphism sheaves local preimages` | STACKS/EXT | `ORIGINAL`: standard principle, distinct application and wording |
| P015 | “These are the arithmetic and site-specific inputs the preceding conditional implication” | `arithmetic site-specific inputs rational Witt finite flat` | WITT | `ORIGINAL`: proof-package synthesis not found |
| P017 | “The target Wrat A is viewed as an additive group under multiplication” | `Wrat A additive group under multiplication rational functions Witt` | WITT | `COMMON_KNOWLEDGE`: standard rational-Witt convention |
| P019 | “We do not silently extend that assertion to a larger affine site” | `extend assertion larger affine site sheaf finite flat` | STACKS | `ORIGINAL`: scope sentence not found |
| P020 | “It is essential that omega is an epimorphism in the category” | `omega epimorphism category of sheaves rational Witt` | STACKS/WITT | `ORIGINAL`: standard principle in a manuscript-specific application |
| P024 | “We collect the ingredients that make the overlap calculation survive sheafification” | `overlap calculation survive sheafification descent lemma` | STACKS | `ORIGINAL`: no matching wording |
| P034 | “Deninger's Proposition 4.5 gives injectivity when the relevant covers admit refinements” | `Deninger Proposition 4.5 injectivity normalization refinements covers rational Witt` | WITT | `ORIGINAL`: primary source surfaced without matching prose |
| P036 | “the finite-presentation assertion uses no hidden excellence hypothesis” | `finite presentation normalization no excellence hypothesis finite flat algebra` | STACKS | `ORIGINAL`: standard finiteness topic only |
| P037 | “They give a finite-flat domain refinement Proposition 4.5 now applies separately” | `finite flat domain refinement Proposition 4.5 normalization rational Witt` | WITT/STACKS | `ORIGINAL`: manuscript-specific inference not found |
| P039 | “for every nontrivial index it produces a rational Witt section” | `every nontrivial index rational Witt section Verschiebung obstruction` | WITT | `ORIGINAL`: no matching result narrative |
| P041 | “There is a finite extension containing all d-th roots of unity” | `finite extension containing all d-th roots of unity polynomial splits` | ROOT | `COMMON_KNOWLEDGE`: elementary finite-extension fact in varied standard wording |
| P046 | “Each part of the decomposition has a distinct role” | `decomposition distinct role rational Witt Verschiebung root factorization` | NONE | `ORIGINAL`: unrelated decompositions only |
| P053 | “the same calculation therefore proves the finite-flat theorem without transferring” | `same calculation finite-flat theorem change of topology rational Witt` | WITT/STACKS | `ORIGINAL`: site-specific proof sentence not found |
| P055 | “making the two functorial directions explicit prevents a common ambiguity” | `two functorial directions pullback transfer extension class ambiguity` | CAT/EXT | `ORIGINAL`: generic functoriality only |
| P059 | “would produce an additive middle-object morphism lifting V N contrary” | `additive middle object morphism lifting Verschiebung extension class pushout` | EXT/WITT | `ORIGINAL`: theorem-specific contradiction not found |
| P060 | “Taking u equal to zero the pushout is the zero extension class” | `pushout along zero morphism zero extension class Ext` | EXT | `COMMON_KNOWLEDGE`: standard Ext functoriality |
| P061 | “We do not claim that the associated Cech complex computes the full” | `Cech complex does not compute full derived Ext sheaves` | CECH | `COMMON_KNOWLEDGE`: standard limitation, no copied long sequence |
| P062 | “There is a second way to state the nonvanishing that remains below” | `second way state nonvanishing extension class sheaf epimorphism` | STACKS/EXT | `ORIGINAL`: no matching expression |
| P063 | “These checks rather than a change-of-site implication justify the theorem” | `change of site implication finite flat theorem sheafification check` | STACKS | `ORIGINAL`: manuscript-specific justification not found |
| P065 | “an epimorphism supplies local preimages it does not ensure that” | `epimorphism sheaves supplies local preimages not global preimage` | STACKS | `COMMON_KNOWLEDGE`: standard local-versus-global distinction |
| P066 | “The calculation is also independent of any response or future revision” | `calculation independent response future revision manuscript` | REV | `ORIGINAL`: unrelated revision results only |
| P069 | “The source inputs consequently have distinct logical roles” | `source inputs distinct logical roles theorem proof literature` | NONE | `ORIGINAL`: no relevant result |
| P070 | “The index N equal one is a sharp elementary control” | `N equals one control Verschiebung rational Witt identity` | WITT | `COMMON_KNOWLEDGE`: elementary identity/control, no copied wording |
| P071 | “A change to a non-subcanonical topology can annihilate exactly the nilpotent information” | `non-subcanonical topology annihilate nilpotent information sheafification` | WITT/STACKS | `ORIGINAL`: thematic topology results only |
| P072 | “the bounded source search underlying this draft supports owner subtraction” | `bounded source search owner subtraction provenance manuscript` | NONE | `ORIGINAL`: no relevant result |
| P073 | “The conclusion is therefore exact and modest Local root factorization” | `local root factorization exact modest conclusion rational Witt` | NONE/WITT | `ORIGINAL`: no matching conclusion wording |
| P074 | “The reusable mechanism is the conditional implication from a selected cover-local preimage” | `selected cover local preimage overlap descent injective sheafification mechanism` | STACKS | `ORIGINAL`: standard descent theme, no matching synthesis |

### D1 grade summary

| Grade | Count | Proportion |
|---|---:|---:|
| `ORIGINAL` | 29 | 78.4% |
| `COMMON_KNOWLEDGE` | 8 | 21.6% |
| `PARAPHRASE` | 0 | 0.0% |
| `CLOSE_MATCH` | 0 | 0.0% |
| `VERBATIM` | 0 | 0.0% |

The independently reached distribution happens to equal the earlier screen's distribution; equality is an outcome of the fresh search run, not imported evidence.

## Fresh non-body and Round 2 changed-surface searches

| Surface | Exact query | Fresh result | Classification |
|---|---|---|---|
| Full title | “A Descent Obstruction to Verschiebung Lifts on fppf and Finite-Flat Sites” | No exact title hit; an unrelated paper combined the generic themes “descent obstruction”, “Verschiebung”, and “lifts” without the title or manuscript claim | No collision identified |
| Short title stem | “A Descent Obstruction to Verschiebung Lifts” | No exact title hit | No collision identified |
| New materials sentence | “The proof ledger, source locator audit, claim manifest, and compilation materials used to assemble this draft are available from the author upon reasonable request” | No exact full-sentence hit | `ORIGINAL`; the conventional tail does not create a long match |
| Contribution statement | “Liang Wang conceived the study, developed and verified the proofs” | No exact hit | `ORIGINAL` |
| Funding statement | “The author received no specific funding for this work” | Many exact boilerplate instances | `COMMON_KNOWLEDGE`; nine-word disclosure, below the protocol's 20-word verbatim threshold |
| Competing-interests statement | “The author declares no competing interests” | Many exact boilerplate instances | `COMMON_KNOWLEDGE`; standard short disclosure below the threshold |

The Round 2 materials sentence was searched in its full current form, not as the superseded repository-access sentence.

## D2 fresh author self-reuse screen

Five identity-constrained searches were freshly run: exact email alone; email plus `rational Witt`; email plus `Verschiebung`; email plus `fppf`; and email plus the exact title. The exact-email search returned a sizeable, topically heterogeneous corpus. Public records with the exact email included, among others:

- *The emergence of prime distribution from low-dimensional deterministic chaos*, on the publisher's article page (`https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2684334`);
- *Emergence of Biological Structural Discovery in General-Purpose Language Models*, on bioRxiv (`https://www.biorxiv.org/content/10.64898/2026.01.03.697478v1`);
- *Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking*, on bioRxiv (`https://www.biorxiv.org/content/10.64898/2026.05.06.722404v1`);
- *Human Genome Book: Words, Sentences and Paragraphs*, on Qeios (`https://www.qeios.com/read/CK8QUT`);
- *Spectral Analysis of the Transfer Operator in the Period-3 Logistic Sandbox*, on Preprints.org (`https://doi.org/10.20944/preprints202603.1652.v1`); and
- *Translate gene sequence into gene ontology terms based on statistical machine translation*, on F1000Research (`https://doi.org/10.12688/f1000research.2-231.v1`).

The topic/title-constrained searches did not surface an email-linked prior rational-Witt, Verschiebung, fppf, or same-title manuscript. None of the 37 fresh characteristic-fragment searches surfaced text from the reliably email-linked works. The linked subset is mainly bioinformatics, language-model, dynamical-systems, or other topically distinct work.

**D2 determination: `INSUFFICIENT EVIDENCE FOR CLEAN`; no actionable self-reuse signal in the reliably email-linked public subset.** A complete authoritative bibliography was not available; “Liang Wang” is highly ambiguous; email reuse is a strong link but not a complete publication ledger; indexing, paywall, removal, and coverage gaps remain; translated or unindexed reuse is not reliably detectable. These limitations forbid a `CLEAN` label even though no actionable signal appeared.

## D3 fresh AI-writing characteristic screen

This is a style screen, not an AI-authorship detector. Counts were recomputed on the current manuscript.

| Indicator | Fresh observation | Triggered? |
|---|---|:---:|
| Excessive smoothness | Proof, exposition, controls, and declarations have differing rhythms | no |
| Lack of specificity | Explicit rings, covers, maps, equations, locators, and scope limits are pervasive | no |
| Formulaic transitions | `therefore` 14; `thus` 8; `hence` 8; `consequently` 3; `moreover` 1 | yes |
| Excessive parallelism | Paragraph structures vary across definitions, proofs, and controls | no |
| Hedging overload | `may` 2; `could` 1; `might` 0; `perhaps` 1 | no |
| Citation-argument gap | Not established by a Phase D style screen; no style trigger recorded | no |

Surprise/reframing phrases were also checked: `surprisingly`, `unexpectedly`, `counterintuitively`, and `contrary to our hypothesis` each occur zero times. Result: **1/6**, below the two-indicator alert threshold. Repeated causal transitions remain a non-blocking style observation; no authorship inference is made.

## Seven AI research failure modes

`CLEAR_BY_NON_APPLICABILITY` means only that the named implementation/experiment failure has no observable surface in this theoretical manuscript. It does not validate the proof. `INSUFFICIENT_EVIDENCE` is not converted to `CLEAR`.

| Mode | Status | Round 2 evidence and boundary |
|---|---|---|
| 1. Implementation bug passing AI self-review | `CLEAR_BY_NON_APPLICABILITY` | No implementation, analysis code, numerical output, benchmark, or code-derived claim is presented. This says nothing about proof correctness. |
| 2. Hallucinated citation | `INSUFFICIENT_EVIDENCE` | Phase D tests originality and public-text overlap, not reference existence, metadata, locator correctness, or claim entailment. No conclusion from another phase is imported into this carrier. No fresh Phase D suspicion arose. |
| 3. Hallucinated experimental result | `CLEAR_BY_NON_APPLICABILITY` | The current manuscript explicitly says no empirical data were generated or analyzed and contains no experimental tables, seeds, run counts, percentages, or empirical result narrative. |
| 4. Shortcut reliance | `CLEAR_BY_NON_APPLICABILITY` | No learned model, dataset, task metric, ablation, or generalization claim exists on the paper's surface. |
| 5. Implementation bug reframed as novel insight | `CLEAR_BY_NON_APPLICABILITY` | The implementation surface is absent, and all four surprise/reframing phrase counts are zero. This does not exclude non-code conceptual overinterpretation. |
| 6. Methodology fabrication | `CLEAR_BY_NON_APPLICABILITY` | No experimental Methods section, hyperparameters, preprocessing, split, or run configuration is claimed. Mathematical exposition remains subject to mathematical review. |
| 7. Early frame-lock | `INSUFFICIENT_EVIDENCE` | The present manuscript and Round 2 revision artifacts show current internal alignment, but they cannot reconstruct the author's initial Stage 1/2 alternatives or the counterfactual framing that would have been chosen. Present coherence is not proof that early frame-lock did not occur. |

Failure-mode routing: **`WARN_NOT_BLOCK`**. No mode is `SUSPECTED`; Modes 2 and 7 preserve their evidentiary limits.

## Route and gate accounting

| Item | Status | Reason |
|---|---|---|
| Route A | `NOT_TESTABLE` | This originality carrier has no route-A test surface |
| Route B | `NOT_TESTABLE` | This originality carrier has no route-B test surface |
| Gate credit | `NONE` | Phase D originality/failure-mode screening does not itself satisfy either route gate |

## Query audit trail and limitations

The fresh Round 2 run comprised 37 quoted body queries, 37 unquoted body supplements, six exact non-body/changed-surface queries, and five distinct email/topic queries. The complete 74 body-query strings are recorded row by row above; the six non-body and five email queries are recorded in their respective sections.

No `CRITICAL`, `SERIOUS`, or `MODERATE` originality issue was identified. The D3 transition repetition is a below-threshold, non-blocking observation. This search cannot produce a reliable similarity percentage and does not substitute for Turnitin, iThenticate, a publisher database, or expert mathematical review. It covers public indexed results and accessible snippets/full text only; paywalled, private, removed, newly posted, translated, or unindexed material may be absent. The body comparison is a deterministic 50.0% sample rather than an exhaustive manuscript-to-corpus comparison. Author-corpus incompleteness and same-name ambiguity are material D2 limitations.

Accordingly, the bounded outcome is **`PASS WITH LIMITATIONS / WARN_NOT_BLOCK`**, never `CLEAN`, with Route A/B both `NOT_TESTABLE` and no gate credit.
