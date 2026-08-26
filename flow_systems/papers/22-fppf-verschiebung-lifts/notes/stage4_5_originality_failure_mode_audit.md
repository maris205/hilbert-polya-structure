# Stage 4.5 independent originality, AI research failure-mode, and RAISE audit

Audit time: 2026-08-25T11:51:03Z  
Operating mode: Phase D Mode 2 (final check), seven-mode AI research failure checklist, and RAISE `primary_research / principles_only / Stage 4.5`  
Author supplied for D2: Liang Wang  
Audited manuscript: `paper/manuscript.tex`, SHA-256 `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2`

## Independent disposition

- Phase D: **PASS WITH LIMITATIONS**. The sampled public-Web screen found no `CLOSE_MATCH` or `VERBATIM` body paragraph and no actionable self-reuse signal. This is not a professional plagiarism determination and is deliberately not labelled `CLEAN`, because the public author corpus could not be made complete or exhaustively disambiguated.
- Seven AI research failure modes: **WARN, not block**. Modes 1, 3, 4, 5, and 6 are `CLEAR` on explicit non-applicability to the observed theoretical-paper surface; Modes 2 and 7 are `INSUFFICIENT EVIDENCE`; no mode is `SUSPECTED`. These statuses do not imply that the mathematical proof is correct.
- RAISE principle extension: **WARN**. All four principle checks are `fail` under the bundled criteria, but this is primary research, so the compliance contribution is warn-only and is not a claim of official RAISE compliance.
- No conclusion from the earlier Stage 2.5 audit was imported. Every disposition below was formed from the current manuscript, the current Material Passport, the Stage 4 patch/bundle, and a fresh public-Web screen.

## Input and provenance bindings

| Input | SHA-256 | Use in this audit |
|---|---|---|
| `paper/manuscript.tex` | `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2` | Current body, declarations, AI disclosure, and failure-mode surface |
| `notes/stage4_revision_patch_round1.json` | `e9c1debbb21a0b209847004de16fd76c9e1489844c4209417dd7fdb6b2ca5a6a` | Identification of every Stage 4 addition/substantial replacement |
| `notes/stage4_revision_evidence_bundle.json` | `763f9e3cc12a8115f02a0d315dc9c74415448676c341a20e80cc0d292006f0ff` | Revision-chain binding; not treated as originality evidence by itself |
| `notes/material_passport.json` | `f395557fe703fbbd62af60e7b5c2afcb63ff1c3db1c2299d0e7dbd73ef86b52c` | `repro_lock=null`, `slr_lineage=false`, `no_experiments_declared`, and empty experiment provenance |

The Stage 4 patch contains thirteen operations: eight body replacements, one body deletion, one title/byline replacement, and three declaration replacements. The replacement blocks map to twelve current body paragraphs and three current declaration paragraphs. All of those prose paragraphs were screened; the title/byline/date block was also checked as metadata.

## Phase D verification parameters and sampling ledger

The body denominator begins with the first numbered section (`Introduction and main results`) and ends before `Declarations`. Abstracts, the Chinese summary, keywords, MSC metadata, section-heading-only blocks, display-only blocks, declarations, and bibliography commands are excluded. Blank-line-delimited prose blocks with at least eight natural-language words are counted; theorem, proposition, remark, and proof prose is included. This deterministic rule yields 74 body paragraphs, assigned stable IDs `P001`–`P074` in manuscript order.

Sampling was performed as follows:

1. Include all twelve Stage 4 newly added or substantially replaced body paragraphs: `P005, P008, P009, P011, P012, P013, P014, P015, P055, P059, P073, P074`.
2. Add high-risk and section-coverage paragraphs, producing a 29-paragraph priority set: `P001, P002, P005, P008, P009, P010, P011, P012, P013, P014, P015, P017, P020, P024, P034, P039, P041, P055, P059, P061, P063, P065, P066, P069, P070, P071, P072, P073, P074`.
3. Supplement without replacement from the remaining eligible body paragraphs using a deterministic PRNG seeded by the first 16 hexadecimal characters of the manuscript hash, `2e8a6872eabb512d`. The eight random supplements were `P003, P019, P036, P037, P046, P053, P060, P062`.

Final body sample: 37/74 paragraphs, exactly **50.0%**.

| Major section | Denominator | Sampled | Sample IDs |
|---|---:|---:|---|
| 1. Introduction and main results | 16 | 12 | P001, P002, P003, P005, P008–P015 |
| 2. Rational Witt sheaves and the extension | 7 | 3 | P017, P019, P020 |
| 3. Three descent lemmas | 15 | 4 | P024, P034, P036, P037 |
| 4. The all-index descent obstruction | 16 | 4 | P039, P041, P046, P053 |
| 5. The extension-theoretic formulation | 8 | 5 | P055, P059–P062 |
| 6. The finite-flat site and the Dedekind-section assertion | 7 | 4 | P063, P065, P066, P069 |
| 7. Scope, controls, and conclusion | 5 | 5 | P070–P074 |
| **Total** | **74** | **37** | **50.0%** |

Stage 4 coverage is therefore 12/12 modified body paragraphs, 3/3 modified declaration paragraphs, and 1/1 modified title/byline metadata block. The three declarations and metadata are supplemental checks outside the 74-paragraph body denominator.

## D1 paragraph-level public-Web comparison

For every sampled paragraph, one normalized 8–12-word quoted fragment and one unquoted supplementary query were submitted. The returned top-ranked public result set was reviewed, up to ten results where the service returned that many; some queries returned fewer. Mathematical notation was normalized to words for search. No quoted query reproduced a complete sampled body fragment.

Result-set codes used in the table:

- `WITT`: thematic results led by Christopher Deninger's *Rational Witt vectors and associated sheaves* (`https://arxiv.org/abs/2508.05329`) and standard Witt-vector resources; none reproduced the sampled wording.
- `SHEAF`: standard sheaf/descent results, principally the Stacks Project (`https://stacks.math.columbia.edu/tag/007X`, `https://stacks.math.columbia.edu/tag/00WL`, and `https://stacks.math.columbia.edu/tag/007T`); concept overlap only.
- `ALG`: standard finiteness/finite-flat material, including `https://stacks.math.columbia.edu/tag/0GSE` and `https://stacks.math.columbia.edu/tag/02K9`; concept overlap only.
- `ROOT`: standard roots-of-unity material, including `https://stacks.math.columbia.edu/tag/0EXP`; concept overlap only.
- `EXT`: standard pushout/Ext explanations, including `https://math.stackexchange.com/questions/4824663/show-e-cong-e-as-r-modules-given-h-n-to-n-isomorphism-mathscr-e`; concept overlap only.
- `CECH`: standard Cech-versus-derived caveats, including `https://mathoverflow.net/questions/4214/equivalence-of-grothendieck-style-versus-cech-style-sheaf-cohomology`; concept overlap only.
- `CAT`: generic functoriality/pullback results, not the manuscript wording.
- `REV`: revision-guidance results, unrelated to the mathematical claim.
- `NONE`: returned results were absent or unrelated to the queried proposition.

`S4` marks a paragraph newly added or substantially replaced by the Stage 4 patch.

| ID | Location | S4 | Quoted characteristic fragment | Supplementary query | Reviewed result set | Grade and rationale |
|---|---|:---:|---|---|---|---|
| P001 | L119–130, §1 |  | “the chosen factors must satisfy descent on the double overlap” | `chosen factors descent double overlap rational Witt sheaf` | WITT/SHEAF | `ORIGINAL`: thematic descent sources only; no matching expression |
| P002 | L132–150, §1 |  | “treating an arbitrary skeleton as though it were automatically closed” | `arbitrary skeleton automatically closed algebraic geometry proof` | NONE | `ORIGINAL`: unrelated skeleton/closure results only |
| P003 | L152–158, §1 |  | “The word additive refers to the Witt addition, represented by multiplication” | `Witt addition represented by multiplication rational Witt vectors` | WITT | `COMMON_KNOWLEDGE`: standard big-Witt convention expressed in multiple forms |
| P005 | L169–178, §1 | yes | “a finite-flat covering family of an affine scheme means a” | `finite flat covering family affine scheme jointly surjective` | SHEAF/ALG | `COMMON_KNOWLEDGE`: standard site definition; no copied sentence |
| P008 | L206–219, §1 | yes | “When one topology is fixed below, the unadorned symbols” | `unadorned symbols topology sheafification affine sites notation` | SHEAF | `ORIGINAL`: notation sentence not found |
| P009 | L221–232, §1 | yes | “In particular e tau is nonzero and V N pullback” | `rational Witt extension class Verschiebung pullback nonzero` | WITT/EXT | `ORIGINAL`: result-specific formulation not found |
| P010 | L234–244, §1 |  | “Read in this sectionwise sense, that assertion therefore requires correction” | `sectionwise assertion requires correction sheaf Verschiebung` | WITT | `ORIGINAL`: source paper surfaced, not the correction wording |
| P011 | L246–261, §1 | yes | “The exact source is Deninger's version-1 preprint Proposition 4.3” | `Deninger version 1 Proposition 4.3 rational Witt Verschiebung` | WITT | `ORIGINAL`: bibliographic synthesis, no matching sentence |
| P012 | L263–280, §1 | yes | “This bounded negative result is not a claim of global priority” | `bounded negative result global priority rational Witt lifts` | WITT | `ORIGINAL`: no matching expression |
| P013 | L282–286, §1 | yes | “Our contribution is correspondingly narrow we answer the additive lifting question” | `additive lifting question rational Witt Verschiebung finite flat site` | WITT | `ORIGINAL`: manuscript-specific contribution statement |
| P014 | L288–306, §1 | yes | “failure of an unrelated target section to have a global preimage” | `target section global preimage epimorphism sheaves local preimages` | SHEAF/EXT | `ORIGINAL`: underlying sheaf principle is standard, but expression and implication are distinct |
| P015 | L308–316, §1 | yes | “These are the arithmetic and site-specific inputs the preceding conditional implication” | `arithmetic site-specific inputs rational Witt finite flat` | WITT | `ORIGINAL`: proof-package synthesis not found |
| P017 | L331–350, §2 |  | “The target Wrat A is viewed as an additive group under multiplication” | `Wrat A additive group under multiplication rational functions Witt` | WITT | `COMMON_KNOWLEDGE`: standard rational-Witt convention; wording differs |
| P019 | L365–374, §2 |  | “We do not silently extend that assertion to a larger affine site” | `extend assertion larger affine site sheaf finite flat` | SHEAF | `ORIGINAL`: scope sentence not found |
| P020 | L376–386, §2 |  | “It is essential that omega is an epimorphism in the category” | `omega epimorphism category of sheaves rational Witt` | SHEAF/WITT | `ORIGINAL`: standard principle applied in a manuscript-specific way |
| P024 | L434–436, §3 |  | “We collect the ingredients that make the overlap calculation survive sheafification” | `overlap calculation survive sheafification descent lemma` | SHEAF | `ORIGINAL`: no matching wording |
| P034 | L499–503, §3 |  | “Deninger's Proposition 4.5 gives injectivity when the relevant covers admit refinements” | `Deninger Proposition 4.5 injectivity normalization refinements covers rational Witt` | WITT | `ORIGINAL`: source attribution surfaced without matching prose |
| P036 | L519–528, §3 |  | “the finite-presentation assertion uses no hidden excellence hypothesis” | `finite presentation normalization no excellence hypothesis finite flat algebra` | ALG | `ORIGINAL`: standard finiteness results only |
| P037 | L530–534, §3 |  | “They give a finite-flat domain refinement Proposition 4.5 now applies separately” | `finite flat domain refinement Proposition 4.5 normalization rational Witt` | WITT/ALG | `ORIGINAL`: manuscript-specific inference not found |
| P039 | L546–549, §4 |  | “for every nontrivial index it produces a rational Witt section” | `every nontrivial index rational Witt section Verschiebung obstruction` | WITT | `ORIGINAL`: no matching result narrative |
| P041 | L568–583, §4 |  | “There is a finite extension containing all d-th roots of unity” | `finite extension containing all d-th roots of unity polynomial splits` | ROOT | `COMMON_KNOWLEDGE`: elementary finite-field fact appears in varied standard wording |
| P046 | L676–684, §4 |  | “Each part of the decomposition has a distinct role” | `decomposition distinct role rational Witt Verschiebung root factorization` | NONE | `ORIGINAL`: unrelated decompositions only |
| P053 | L739–756, §4 |  | “the same calculation therefore proves the finite-flat theorem without transferring” | `same calculation finite-flat theorem change of topology rational Witt` | WITT | `ORIGINAL`: site-specific proof sentence not found |
| P055 | L780–784, §5 | yes | “making the two functorial directions explicit prevents a common ambiguity” | `two functorial directions pullback transfer extension class ambiguity` | CAT/EXT | `ORIGINAL`: generic functoriality results only |
| P059 | L825–836, §5 | yes | “would produce an additive middle-object morphism lifting V N contrary” | `additive middle object morphism lifting Verschiebung extension class pushout` | EXT/WITT | `ORIGINAL`: theorem-specific contradiction not found |
| P060 | L838–844, §5 |  | “Taking u equal to zero the pushout is the zero extension class” | `pushout along zero morphism zero extension class Ext` | EXT | `COMMON_KNOWLEDGE`: standard Ext functoriality; no long copied sequence |
| P061 | L846–852, §5 |  | “We do not claim that the associated Cech complex computes the full” | `Cech complex does not compute full derived Ext sheaves` | CECH | `COMMON_KNOWLEDGE`: standard limitation stated in manuscript-specific context |
| P062 | L857–880, §5 |  | “There is a second way to state the nonvanishing that remains below” | `second way state nonvanishing extension class sheaf epimorphism` | SHEAF/EXT | `ORIGINAL`: no matching expression |
| P063 | L885–894, §6 |  | “These checks rather than a change-of-site implication justify the theorem” | `change of site implication finite flat theorem sheafification check` | SHEAF | `ORIGINAL`: manuscript-specific justification not found |
| P065 | L915–925, §6 |  | “an epimorphism supplies local preimages it does not ensure that” | `epimorphism sheaves supplies local preimages not global preimage` | SHEAF | `COMMON_KNOWLEDGE`: standard sheaf-epimorphism distinction in varied wording |
| P066 | L927–932, §6 |  | “The calculation is also independent of any response or future revision” | `calculation independent response future revision manuscript` | REV | `ORIGINAL`: only unrelated revision guidance surfaced |
| P069 | L956–963, §6 |  | “The source inputs consequently have distinct logical roles” | `source inputs distinct logical roles theorem proof literature` | NONE | `ORIGINAL`: no relevant result |
| P070 | L967–972, §7 |  | “The index N equal one is a sharp elementary control” | `N equals one control Verschiebung rational Witt identity` | WITT | `COMMON_KNOWLEDGE`: elementary identity/control, no copied wording |
| P071 | L974–980, §7 |  | “A change to a non-subcanonical topology can annihilate exactly the nilpotent information” | `non-subcanonical topology annihilate nilpotent information sheafification` | SHEAF/WITT | `ORIGINAL`: thematic topology sources only |
| P072 | L982–990, §7 |  | “the bounded source search underlying this draft supports owner subtraction” | `bounded source search owner subtraction provenance manuscript` | NONE | `ORIGINAL`: no relevant match |
| P073 | L992–997, §7 | yes | “The conclusion is therefore exact and modest Local root factorization” | `local root factorization exact modest conclusion rational Witt` | NONE/WITT | `ORIGINAL`: no matching conclusion wording |
| P074 | L999–1011, §7 | yes | “The reusable mechanism is the conditional implication from a selected cover-local preimage” | `selected cover local preimage overlap descent injective sheafification mechanism` | SHEAF | `ORIGINAL`: standard descent material only; no matching synthesis |

### D1 grade summary

| Grade | Body count | Proportion |
|---|---:|---:|
| `ORIGINAL` | 29 | 78.4% |
| `COMMON_KNOWLEDGE` | 8 | 21.6% |
| `PARAPHRASE` | 0 | 0.0% |
| `CLOSE_MATCH` | 0 | 0.0% |
| `VERBATIM` | 0 | 0.0% |

### Supplemental Stage 4 non-body checks

| ID | Stage 4 surface | Search | Result | Grade |
|---|---|---|---|---|
| S4-META-B0005 | Title, byline, affiliation, contact, date | Quoted title “A Descent Obstruction to Verschiebung Lifts” plus unquoted title keywords | No exact title hit; thematic fppf/descent results only. Factual identifiers were identity-checked, not prose-graded. | Metadata inspected; no collision identified |
| S4-NB01 | Author-contributions paragraph | “Liang Wang conceived the study, developed and verified the proofs” plus unquoted terms | No matching statement | `ORIGINAL` |
| S4-NB02 | Funding paragraph | “The author received no specific funding for this work” plus unquoted terms | Numerous exact short boilerplate instances and publisher templates | `COMMON_KNOWLEDGE`; nine-word standard disclosure, below the protocol's 20-word verbatim threshold |
| S4-NB03 | Competing-interests paragraph | “The author declares no competing interests” plus unquoted terms | Numerous exact short journal declarations | `COMMON_KNOWLEDGE`; standard declaration, below the 20-word threshold |

## D2 author self-reuse screen and same-name disambiguation

The author's name alone is not a safe identity key. Public results for “Liang Wang” include many distinct researchers, including multiple HUST affiliations and multiple ORCIDs. The DBLP disambiguation page (`https://dblp.org/pid/56/4499`) itself lists many same-name identities. Generic name-only or HUST-only hits were therefore excluded unless linked by the manuscript contact email `wangliang.f@gmail.com` or, for newer records, ORCID `0000-0001-9006-6924` together with that email/affiliation.

Strongly linked public works reviewed included:

| Work | Identity linkage | Public record |
|---|---|---|
| *How to Build a DNA Search Engine like Google?* (2011) | Exact contact email and HUST/Tencent affiliation | `https://www.hilarispublisher.com/open-access/how-to-build-a-dna-search-engine-like-google-jcsb.1000081.pdf` |
| *Translate gene sequence into gene ontology terms based on statistical machine translation* (2013) | Exact contact email | DOI `10.12688/f1000research.2-231.v1` |
| *Human Genome Book: Words, Sentences and Paragraphs* | Exact contact email and HUST | `https://www.qeios.com/read/CK8QUT` |
| *The Emergence of Prime Distribution from Low-Dimensional Deterministic Chaos* | Exact email, HUST, and ORCID | DOI `10.21203/rs.3.rs-8394349/v1` |
| *Emergence of Biological Structural Discovery in General-Purpose Language Models* | Exact email, HUST, and ORCID | DOI `10.21203/rs.3.rs-8507849/v1` |
| *Spectral Analysis of the Transfer Operator in the Period-3 Logistic Sandbox* | Exact email and exact manuscript school/affiliation | DOI `10.20944/preprints202603.1652.v1` |
| *Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking* | Exact email, HUST, and linked ORCID | `https://www.biorxiv.org/content/10.64898/2026.05.06.722404v1` |

Fresh exact-email/ORCID queries with `Witt`, `Verschiebung`, `fppf`, and the current title did not surface a reliably linked prior rational-Witt or fppf manuscript. The 37 D1 characteristic-fragment searches also did not match text from the linked works. The linked works are predominantly bioinformatics, language-model, or dynamical-systems papers and are topically distinct from the present sheaf-theoretic proof.

**D2 determination: `INSUFFICIENT EVIDENCE FOR CLEAN`; no actionable self-reuse signal identified in the reliably linked public subset.** The reason for withholding `CLEAN` is corpus completeness, not a detected overlap: no authoritative complete publication list or reliably verified Google Scholar profile was available through the public result set, name-only records cannot safely be assigned, paywalled/non-indexed works may be absent, and identity links for older works rely primarily on the reused email address. A professional database search or an author-supplied ORCID/complete CV would be required for a stronger conclusion.

## D3 AI-writing characteristic checklist

This is an informational style screen, not an AI-authorship detector. The manuscript already discloses AI assistance; that disclosure is not used as evidence that any particular sentence was machine-generated.

| Indicator | Observation | Triggered? |
|---|---|:---:|
| Excessive smoothness | Prose is polished, but theorem/proof, exposition, and declarations have visibly different rhythms. | no |
| Lack of specificity | Explicit rings, covers, maps, equations, proposition locators, and scope limits are pervasive. | no |
| Formulaic transitions | `therefore` 14, `thus` 8, `hence` 8, `consequently` 3, `moreover` 1. Repetition is noticeable even though causal transitions are normal in proof writing. | yes |
| Excessive parallelism | Paragraph structures vary across definitions, proofs, controls, and source discussion. | no |
| Hedging overload | Only `may` 2, `could` 1, and `perhaps` 1 were found; own results are not systematically hedged. | no |
| Citation-argument gap | Not established by this Phase D screen; no stylistic gap was apparent from the sampled paragraphs, but citation entailment belongs to a separate phase. | no trigger recorded |

Indicators triggered: **1/6**, below the two-indicator alert threshold. No AI-authorship determination is made.

## Phase D issue list and limitations

No `CRITICAL`, `SERIOUS`, or `MODERATE` originality issue was identified. The repeated causal-transition vocabulary is a non-blocking style observation below the D3 alert threshold. The D2 corpus-completeness limitation prevents a `CLEAN` label.

This screen uses public Web search, not Turnitin, iThenticate, or a publisher similarity database. It cannot calculate a reliable overlap percentage. Coverage is limited to publicly indexed pages, snippets, and accessible full text; paywalled, unindexed, removed, private, and newly posted material may be absent. Cross-language or translated reuse is difficult to detect. Search results are time-sensitive and were observed on 25 August 2026. The body check is a 50.0% sample rather than an exhaustive comparison, although all Stage 4 added/substantially modified prose was screened. D2 is further limited by common-name disambiguation and the absence of a complete authoritative author bibliography. Professional similarity screening remains appropriate before formal submission.

## Seven AI research failure modes

The checklist was applied afresh to the current manuscript and current passport. The passport records `no_experiments_declared`, `experiment_provenance=[]`, and `repro_lock=null`; the manuscript states that no empirical data were generated or analyzed. “Clear by non-applicability” below means only that the named experiment/implementation failure has no observed surface in this theoretical paper. It does **not** validate the mathematics or exclude ordinary proof errors.

| Mode | Status | Current evidence and bounded rationale |
|---|---|---|
| 1. Implementation bug passing AI self-review | `CLEAR` | No implementation, analysis code, empirical numerical result, benchmark, or code-derived claim is presented or listed in experiment provenance. This excludes the code-bug failure mode from the observed surface, not errors in the proof. |
| 2. Hallucinated citation | `INSUFFICIENT EVIDENCE` | Phase D checked text similarity, not reference existence, metadata, or citation entailment. No earlier Stage 2.5 conclusion was imported, and a fresh Phase A/A0 citation audit was outside the supplied task. This status does not allege that a citation is false. |
| 3. Hallucinated experimental result | `CLEAR` | The paper contains no experimental tables, percentages, seeds, run counts, or empirical-result narrative; the manuscript and passport independently state no experiments/data. This does not validate theorem statements. |
| 4. Shortcut reliance | `CLEAR` | There is no learned model, dataset, performance task, ablation, or generalization claim to which a shortcut feature could apply. The status is explicit non-applicability. |
| 5. Implementation bug reframed as novel insight | `CLEAR` | Mode 1's implementation surface is absent, and a case-insensitive manuscript scan found no “surprisingly”, “unexpectedly”, “counterintuitively”, or “contrary to our hypothesis” narrative. This does not rule out conceptual overinterpretation unrelated to code. |
| 6. Methodology fabrication | `CLEAR` | There is no experimental Methods section, hyperparameter set, preprocessing pipeline, dataset split, or run configuration to drift from. The proof exposition remains subject to mathematical review; this status addresses only the checklist's fabricated-experiment-methodology mode. |
| 7. Frame-lock at an early pipeline stage | `INSUFFICIENT EVIDENCE` | The current manuscript, Stage 4 patch, and bundle show internal alignment between the stated question, descent construction, and conclusion, but they do not reconstruct the initial Stage 1/2 framing alternatives or the author's counterfactual choice. Current coherence cannot prove the absence of an earlier frame lock. |

Failure-mode routing decision: **WARN**. There is no `SUSPECTED` mode. The only insufficient-evidence outcomes are Modes 2 and 7, which the bundled protocol permits to proceed with warning; Modes 1, 3, 5, and 6 are not left insufficient.

## RAISE principles-only audit

RAISE's official scope is evidence synthesis. This primary-research check is an ARS **principle extension**, not official RAISE compliance. `prisma_trAIce` is not applicable and is `null`; the eight-role matrix is omitted. Under the Stage 4.5 primary-research rule, the compliance contribution is capped at `warn` even when individual principle criteria fail.

| Principle | Status | Evidence | Gap |
|---|---|---|---|
| Human oversight | `fail` | The named sole author claims proof verification and manuscript responsibility in the contributions statement; the AI disclosure says every claim/reference/wording choice requires final verification by the named human author and excludes AI authorship. | `[MATERIAL GAP]` No reviewer count, reviewer qualifications, or adjudication procedure is reported; two or more required elements are missing. |
| Transparency | `fail` | The AI disclosure identifies three stages—literature triage, proof-audit support, and drafting—and assigns responsibility to the human author. | `[MATERIAL GAP]` It does not list the AI tools/models, versions, prompts, parameters/settings, or a tool-by-stage mapping; the passport has no corresponding `user_metadata.ai_tools_used` ledger. The omission is systematic. |
| Reproducibility | `fail` | The manuscript names the broad AI-assisted stages, and the materials paragraph points to a working repository. | `[MATERIAL GAP]` `repro_lock` is null; no equivalent model/version, prompt, seed/stochasticity, parameter, or data-access record appears; repository public access is explicitly unconfirmed. Both required supports are missing. |
| Fit for purpose | `fail` | The disclosure at least identifies the tasks in which AI assistance occurred. | `[MATERIAL GAP]` It gives no per-tool selection rationale, pilot evidence, validation reference, limitations, or task-specific performance check. Task names alone are not a fit-for-purpose justification. |

CA-4 self-check: no principle is marked `pass`; each non-pass status has explicit manuscript/passport evidence and a concrete gap. There is therefore no evidence-free pass to downgrade. The schema-valid companion report records `raise.block_decision="warn"`, `overall_decision="warn"`, and `user_action_required=true`.

Recommended non-destructive remediation before dissemination:

1. Replace the generic AI disclosure with a complete tool/model/version and tool-by-stage ledger; summarize or archive prompts and material parameters/settings, including stochasticity.
2. Describe the human verification procedure actually applied, including who checked which AI-assisted outputs and how disagreements or uncertain outputs were adjudicated.
3. Create a reproducibility lock or equivalent immutable archive and resolve the manuscript's still-unconfirmed public-access statement.
4. State why each tool was fit for its assigned task and provide a pilot check, validation reference, or clearly bounded limitation.

These recommendations are audit outputs only; this audit did not modify the manuscript, PDF, bibliography, revision patch/bundle, roadmap, Material Passport, or pipeline state.
