---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--31-level11-conjugacy-owner-ledger"
canonical_tex: "flow_systems/papers/31-level11-conjugacy-owner-ledger/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/31-level11-conjugacy-owner-ledger/paper/paper.pdf"
source_sha256: "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Canonicalization Before Quadratic Audit: A Certificate-Methods Architecture for an Oriented Level-11 Owner Ledger

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/31-level11-conjugacy-owner-ledger>)
- [规范 TeX](<../../../../../flow_systems/papers/31-level11-conjugacy-owner-ledger/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/31-level11-conjugacy-owner-ledger/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/31-level11-conjugacy-owner-ledger/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/31-level11-conjugacy-owner-ledger/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This article revises the research architecture for a finite ownership problem associated with a positive time change of the `Gamma_0(11)` geodesic flow. The frozen population contains 138 Hecke-output instances in 55 source-word/prime groups, with oriented primitive `Gamma_0(11)` conjugacy classes as the proposed owners. The earlier design made 9,453 terminal pair dispositions appear to be the foundational certificate. Adversarial review identified that requirement as an unjustified architectural lock. Revision 1 instead makes a deterministic canonicalization map and its biconditional the primary target: two rooted, oriented inputs must receive the same canonical owner bytes exactly when they represent the same oriented primitive owner. The 9,453-row table is retained, but only as a derived adversarial audit of the canonical partition. Aggregate class counts remain weaker post-closure controls. The article also defines the distinct roles of a global owner table `G`, the 138-row incidence relation `I`, and the cell-local no-double-credit quotient `C`. The executed work is limited to closed-corpus evidence synthesis and review-informed method design. No canonicalization theorem, owner partition, all-pairs audit, or `G/I/C` table has been produced. All 22 inherited citations retain `anchor:none`; source identities and metadata close, but claim-to-passage faithfulness remains `INCONCLUSIVE`. The contribution is therefore a reproducible, fail-closed certificate architecture rather than a scientific ownership result. P31 remains A1-only, with no formal Route-A tuple, positive arithmetic A2 credit, or Route-B invocation.
author:
- |
  Liang Wang^1^\
  ^1^School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology,\
  Luoyu Road 1037, 430070, Hubei, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 2 September 2026
title: |
  Canonicalization Before Quadratic Audit:\
  A Certificate-Methods Architecture for an Oriented Level-11 Owner Ledger
```

## Markdown 正文

> **繁體中文摘要**
>
> 本文針對固定的 $\Gamma_0(11)$ 測地流正時間變換， 提出一套失敗即關閉的 所有權憑證方法架構。 凍結輸入包含 一百三十八個 Hecke 輸出實例、 五十五個來源字與質數群組； 預定所有者是 保持方向的本原 $\Gamma_0(11)$ 共軛類。 核心目標不是先製作 九千四百五十三筆 彼此獨立的成對判定， 而是建立可重播的 決定性規範化映射及其雙條件： 兩個已取本原根 且保留方向的輸入 具有相同規範位元， 當且僅當它們代表 同一所有者。 只有在此定理、 證據格式與獨立驗證器完成後， 全部成對表格 才可作為派生的 對抗式回歸稽核。 本文並嚴格區分 全域所有者表 $G$、 一百三十八列的關聯表 $I$ 與儲存格內去重商 $C$。 本階段僅執行 封閉語料的文獻綜合 與審查後方法設計， 未實作規範化器、 共軛判定、 本原根證書、 所有者分割 或任何 $G/I/C$ 結果。 所有引文均無段落定位， 逐主張的來源支持仍屬未定； 本文不宣稱新定理、 普查結果、 新穎性或路線晉級。

**Keywords:** canonical forms; modular geodesic flow; $\Gamma_0(11)$; oriented conjugacy; primitive owners; certificate methods; adversarial audit

# Introduction, Research Question, and Contribution {#1-introduction-research-question-and-contribution}

Finite orbit ledgers require an equivalence rule before they can support a dynamical interpretation. A repeated row may represent the same primitive owner, a traversal power, an inverse-oriented owner, or a recurrence of one owner in another correspondence cell. P31 freezes those possibilities rather than allowing an outcome-dependent merge. Its inherited dynamical object is the positive time-changed flow `X_geo/rho_epsilon` on `T^1Y_0(11)`. The real level-11 newform differential, positivity interval, Hecke normalization, reciprocal log-zeta convention, and period coordinate `k=2y+z` remain unchanged.

The finite input is also unchanged: 138 instances are distributed over 55 source-word/prime groups. The inherited `2/2/134` split and the three 55-group diagnostic summaries are instance- or group-level controls, not owner counts. The proposed owner is an oriented primitive conjugacy class in `Gamma_0(11)` represented by a positive-trace determinant-one lift. Inversion is kept as a separate oriented owner and connected by an inverse-link field. A primitive traversal exponent is not a Hecke branch-cycle degree. Equality of trace, length, homology, or any other filter cannot by itself certify subgroup conjugacy.

The revised research question is:

**Can a deterministic, independently replayable canonicalization contract certify the complete oriented primitive-owner partition of the frozen 138-instance population, and, conditional on that closure, induce the distinct global, incidence, and cell-local estimands `G`, `I`, and `C`?**

This formulation changes the method priority without changing the object or scientific state. The primary target is a canonicalization biconditional, not 9,453 independently foundational negative certificates. The all-pairs expansion remains valuable because it can expose inconsistencies, nontransitive implementation defects, inverse-policy mistakes, and compensating merges or splits. It is nevertheless derived from the partition certificate unless a later theorem proves that bespoke pairwise evidence is necessary for a particular disposition.

The article's contribution is a certificate-methods architecture with three separated surfaces: a canonical proof object, a full-population adversarial audit, and downstream estimands. It is not positioned as a new conjugacy theorem, an implemented solver, or a novelty claim. No novelty search was authorized in the frozen research program. The article type is therefore deliberately narrower than a mathematical-results paper.

Three distinctions govern the exposition. First, the dynamical owner is not an input row: ownership is assigned only after subgroup conjugacy, orientation, and maximal-root status are resolved. Second, a proof object is not an estimand: canonical bytes and their witnesses justify a partition, whereas `G`, `I`, and `C` summarize different consequences of that partition. Third, an audit is not its own truth source: the all-pairs expansion can challenge a canonicalizer, but it cannot define correctness when the canonicalizer's biconditional is still open. Keeping these levels separate makes a negative or not-evaluable outcome reportable without silently changing the owner definition.

This architecture also fixes the temporal order of evidence. The owner contract, theorem versions, serialization, and failure states must be registered before the 138 rows are classified. The pair table may be generated only after those inputs have independently replayed certificates. Downstream counts may be read only after the pair audit agrees with the canonical partition or records a typed discrepancy. Nothing in this order presumes that the required canonicalizer exists; the lawful endpoint may remain `NOT_EVALUABLE`.

# Frozen Literature and Theoretical Boundary {#2-frozen-literature-and-theoretical-boundary}

::: {#21-exact-subgroup-representations}
## Exact subgroup representations {#21-exact-subgroup-representations}
:::

The frozen literature describes modular-subgroup structure through several exact mathematical interfaces. Subgroup classification, arithmetic-geometric descriptions, special polygons, and two congruence-recognition routes supply foundational finite-index and finite-data contexts [@P31-S01; @P31-S02; @P31-S03; @P31-S04; @P31-S05]. A later computational fundamental-domain framework supplies a potential exact Fuchsian-domain interface [@P31-S06].

These sources support only a bounded synthesis finding: finite, replayable subgroup data are plausible ingredients. They do not bind the exact P31 representation, prove the required canonicalization biconditional, decide any frozen pair, or define owner bytes. Representation, decision, and certification remain distinct obligations.

For the present article, this is a negative-boundary finding rather than a claim of literature absence. The corpus was frozen by a bounded search and has no passage-level locators. We can say that no retained source was admitted as the complete project solver; we cannot say that no such theorem or method exists anywhere. A later implementation would need a source- finalization step that records the exact representation hypotheses and the passages licensing each subroutine. Until then, even a mathematically promising route is an unbound component rather than an available certificate engine.

::: {#22-ambient-and-arithmetic-conjugacy-components}
## Ambient and arithmetic conjugacy components {#22-ambient-and-arithmetic-conjugacy-components}
:::

The second source group gives candidate components for matrix and arithmetic conjugacy. Ideal-class/matrix correspondences and their later refinements supply ambient integral structure, including a relation between hyperbolic integral matrices and ideal classes [@P31-S07; @P31-S08; @P31-S09]. Continued-fraction, arithmetic-group, and modern integral-matrix methods enlarge the possible ambient decision toolkit [@P31-S10; @P31-S11; @P31-S12; @P31-S13].

No source in this group may be promoted into the required oriented `Gamma_0(11)` solver. A valid specialization would still have to preserve determinant one, positive-trace lifting, the congruence condition, orientation, primitive roots, inverse linkage, termination, and independently replayable evidence. Failure of a bounded ambient search would not constitute a negative subgroup-conjugacy certificate.

Ambient-to-subgroup transfer is a particularly important stop surface. Two matrices may be related under an ambient group while the required conjugator fails the $\Gamma_0(11)$ condition, or an ambient procedure may omit the orientation and root policies needed by the ledger. The future dossier must therefore identify the decision group at every step, prove that normalizations remain within it, and serialize the conjugating or obstructing evidence. Merely reporting that a general algorithm terminated would not show that the project-specific owner predicate was evaluated.

::: {#23-canonical-reduction-roots-inversion-and-replay}
## Canonical reduction, roots, inversion, and replay {#23-canonical-reduction-roots-inversion-and-replay}
:::

Canonicalization requires more than an ambient yes/no decision. Modular-geodesic reduction provides relevant coding context [@P31-S15]. Word-hyperbolic conjugacy algorithms supply individual and batch decision precedents [@P31-S16; @P31-S17]. Centralizers and reversing symmetries clarify why ordinary symmetry and inversion must be typed separately [@P31-S18]. Pell equations, unit methods, and computational algebraic number theory provide potential arithmetic subroutines and implementation background [@P31-S19; @P31-S20].

The synthesis does not choose among polygon, arithmetic, or hyperbolic-group implementations. It instead specifies the acceptance condition that any route must meet. A route is admissible only if its hypotheses are proved for the frozen marked object, its output is canonical under the orientation policy, its primitive-root and inverse fields are exact, and an independent verifier can replay success and failure evidence. The literature does not supply the project serialization or prove that this combined contract terminates.

::: {#24-aggregate-counts-as-post-closure-controls}
## Aggregate counts as post-closure controls {#24-aggregate-counts-as-post-closure-controls}
:::

Class-number structure supplies useful aggregate context [@P31-S14]. A direct formula for primitive hyperbolic class counts in `Gamma_0(N)` is the closest frozen census precedent, and modular conjugacy has also been related to real-quadratic class numbers [@P31-S21; @P31-S22].

The information content of an aggregate count is lower than that of a labeled partition. Compensating false merges and false splits can preserve a total. Class counts can therefore test a closed owner table for consistency, but they cannot choose canonical representatives, certify an individual owner identity, or establish that every input has been resolved.

# Executed Methodology {#3-executed-methodology}

::: {#31-closed-corpus-literature-synthesis}
## Closed-corpus literature synthesis {#31-closed-corpus-literature-synthesis}
:::

The only executed research method in this phase is literature synthesis over frozen artifacts. The upstream corpus process captured 44 records, removed nine duplicate manifestations, screened 35 unique records, excluded 13, and retained 22 sources. The inclusion frame covered modular-subgroup descriptions, integral and subgroup conjugacy, reduction and centralizers, primitive roots, and direct class-count precedents. Nineteen inventory rows are classified as peer-reviewed. The authorized metadata correction fixed the P31-S16 page range to 287--305.

The source-verification layer closed identity and metadata for 22 of 22 rows within its recorded scope. That layer mainly used DOI, publisher, journal, institutional, metadata, abstract, and limited authoritative-record surfaces. It did not inspect every theorem passage, produce claim-level page or section locators, or perform a general current retraction or source-conflict screen. The evidence matrix then assigned each source an admitted contribution, an excluded stronger claim, and an applicability warning. Phase 3 grouped the sources into representation, conjugacy, canonicalization, and census themes without converting proximity into theorem transfer.

The synthesis used source-effect discipline rather than vote counting. A source could support a subgroup representation or an ambient decision method while being explicitly excluded from proving the composite P31 owner contract. Publication status and venue recognition did not erase that applicability boundary. Similarly, several adjacent algorithms do not become a complete solver merely because their advertised tasks can be listed in the same paragraph. The missing theorem-to-certificate links remain visible as method obligations.

Citation closure was checked structurally: every source identifier used by the manuscript belongs to the frozen inventory and resolves to one bibliography entry. That check does not validate a theorem passage. All citations retain `anchor:none`, no direct quotation is used, and claim-to-passage status remains `INCONCLUSIVE`. The wording is therefore deliberately limited to component context, prospective use, and recorded exclusions.

::: {#32-review-adjudicated-revision-procedure}
## Review-adjudicated revision procedure {#32-review-adjudicated-revision-procedure}
:::

Phase 5 supplied four procedurally separated, single-model-family review records: editorial, ethics, citation-integrity, and Devil's Advocate. Their integrated decision was `MAJOR_REVISION`, with no Critical finding and no ethics `BLOCKED` result. Revision 1 applies the author-adjudicated branch recorded in the Phase-6 contract. It changes study design only: canonicalization becomes primary, the all-pairs ledger becomes a derived audit, `G/I/C` receive self-contained conditional definitions, and the AI disclosure is narrowed to the actual verification surface.

No new retrieval occurred during Revision 1. No source field, reference, passage locator, direct quotation, experiment, code result, proof result, or canonical manuscript byte was introduced. The Phase-6 ClaimIntent manifest was frozen before this prose and supplies the complete set of eight substantive article claims. Every finding below is either a closed-corpus evidence-synthesis statement, a project definition, or a prospective method obligation.

# Review-Adjudicated Certificate Architecture {#4-review-adjudicated-certificate-architecture}

::: {#41-primary-target-a-canonicalization-biconditional}
## Primary target: a canonicalization biconditional {#41-primary-target-a-canonicalization-biconditional}
:::

Let `X` denote the frozen set of 138 instances after exact input validation. The future method should define a partial operation `root(x)` that either returns an oriented primitive `Gamma_0(11)` representative together with a traversal exponent and proof payload, or returns a typed not-evaluable state. It should then define a deterministic byte map

    kappa: X -> OwnerBytes

on every successfully resolved input. The primary theorem target is the biconditional

    kappa(x)=kappa(y)
    if and only if
    root(x) and root(y) represent the same oriented primitive Gamma_0(11) owner.

This is a target, not a proved statement. Its forward direction must prevent accidental byte collisions. Its reverse direction must show that all representatives of one oriented owner reduce to identical bytes. Both directions must be established in the exact subgroup and presentation used by P31. The map must not identify an owner with its inverse; instead, an `inverse_owner_bytes` field should connect the two oriented objects when that relation is defined.

The biconditional identifies the mathematical certificate invariant: a total, sound, complete, deterministic owner map. If such a theorem and its per-instance witnesses are independently replayable, the partition follows from byte equality. A separate bespoke negative proof for every unequal pair is then not logically foundational merely because the population is finite.

The two implications have different failure modes. Soundness fails if two distinct oriented owners can collide in one byte string. Completeness fails if two representatives of one owner can survive with different bytes. Determinism fails if the same input can produce different bytes under permitted executions. Totality fails if any validated instance lacks either a certificate or a typed unresolved disposition. A future theorem statement should name these obligations individually; a single headline such as "canonical reduction works" would be too coarse for the ledger contract.

The primitive-root layer must precede canonical owner serialization. If an input is a traversal power, serializing the unreduced input could mint a false owner. Conversely, root extraction must not erase the traversal exponent needed by the incidence relation. The proposed certificate therefore carries both the primitive owner bytes and the exact repetition field. Hecke degree remains an input coordinate and is never substituted for that repetition field.

::: {#42-prospective-certificate-and-verifier-contract}
## Prospective certificate and verifier contract {#42-prospective-certificate-and-verifier-contract}
:::

Each future per-instance certificate should bind at least: the immutable input identifier and hash; the subgroup representation and theorem version; exact membership evidence; the normalized matrix or word; the maximal primitive root and traversal exponent; the orientation convention; canonical owner bytes; inverse linkage; and the complete proof or reduction trace needed by a read-only verifier. A failure certificate should identify the exact failed precondition or unresolved theorem obligation rather than silently convert a timeout into nonconjugacy.

The verifier acceptance predicates are also prospective. It should recheck input binding, determinant and subgroup membership, root powering, primitiveness under the chosen theorem, orientation preservation, deterministic serialization, and any inverse relation. It should reject unknown fields, stale theorem versions, noncanonical encodings, missing proof data, or an unresolved subroutine. Independent replay means an implementation separate from the producer can evaluate the frozen mathematical predicates; it does not mean that two AI reviews have statistically independent errors.

No such schema, theorem binding, fixture set, producer, or verifier was implemented in the recorded research or writing stages. The specification above partially addresses reproducibility at the article level while leaving scientific and implementation closure explicitly open.

The producer and verifier should communicate through a versioned, closed schema. Required fields should have fixed encodings, and unknown fields should cause rejection rather than permissive parsing. Each proof payload should state which theorem and representation version it uses, so that a change in a normal-form convention cannot silently reuse old bytes. A manifest should bind the accepted input hashes, fixture hashes, producer build, verifier build, and output hashes. These requirements describe a prospective reproducibility contract; no such manifest or build exists in the present article.

Positive and negative evidence also require asymmetric handling. A positive conjugacy certificate can carry an explicit conjugator whose membership and action are replayed. A negative disposition needs a theorem-backed exhaustive argument appropriate to the frozen group and representation; failure to find a conjugator is insufficient. Root certificates face the same distinction: displaying a power relation is positive evidence, while claiming no proper root requires an exhaustive licensed method. The verifier must preserve these differences instead of reducing every result to one Boolean field.

Target-blind fixtures should exercise the contract before population execution. At minimum they should include identical inputs, distinct representatives of one owner, inverse-related owners, proper powers, coarse-invariant collisions, malformed membership data, and deliberately unresolved theorem bindings. Expected outputs must be registered before the producer sees them. A fixture suite can reveal implementation defects, but passing it cannot replace the global biconditional or the complete 138-instance replay.

::: {#43-the-9453-row-table-as-a-derived-adversarial-audit}
## The 9,453-row table as a derived adversarial audit {#43-the-9453-row-table-as-a-derived-adversarial-audit}
:::

For `X=138`, the unordered-pair expansion has `binom(138,2)=9,453` rows. Once `kappa` is total, each row can carry the two input IDs, their owner bytes, the derived equality disposition, inverse relationship, and any optional direct-solver cross-check. The expected same-owner relation is equality of canonical bytes; inequality supplies the derived different-owner relation under the proved biconditional.

This table remains useful. It can test symmetry, transitivity consequences, deterministic sorting, collision handling, inverse-policy consistency, and agreement between canonical and direct routes. Adversarial fixtures can target pairs that share trace, length, homology, or other coarse invariants while differing in exact ownership. Aggregate-count controls can then operate on the completed partition without replacing any row-level audit.

The table is not described as a uniquely necessary proof architecture. If a future scientific requirement needs a separately replayable negative obstruction for particular cross-class pairs, that need must be justified and bound. Until then, the full table is a regression expansion of the canonical certificate rather than 9,453 independent foundations.

The audit should retain discrepancies rather than overwrite them. If a direct pair solver and canonical-byte equality disagree, the row should record both results, their proof payloads, and a fail-closed batch state. Neither route should be selected after inspecting which one preserves a preferred aggregate count. This makes the table an adversarial consumer of the canonical partition rather than a mechanism for repairing the partition post hoc.

Pair rows can also test equivalence-relation consequences globally. A same-owner relation derived from canonical bytes is automatically reflexive, symmetric, and transitive at the byte level, but producer or serialization defects may still appear as inconsistent input bindings, inverse labels, or traversal metadata. The 9,453-row expansion exposes all unordered cross-input comparisons and therefore remains the most demanding finite regression surface even though it is not the primary proof object.

::: {#44-distinct-g-i-and-c-estimands}
## Distinct `G`, `I`, and `C` estimands {#44-distinct-g-i-and-c-estimands}
:::

The downstream objects can be defined conditionally once `kappa` is total and the biconditional is proved. Define the global owner table

    G = {kappa(x): x in X},

with exactly one row per distinct oriented owner byte string. Define the incidence relation `I` with one row for every input instance, carrying its input fields, cell coordinates, owner bytes, traversal exponent, inverse link, and all frozen Hecke coordinates. Thus `I=138` even when `G<138`.

Let a cell key be the frozen tuple `(source_word, prime, hecke_degree)`. Define `C` as the set of distinct `(cell_key, owner_bytes)` pairs induced by `I`. Raw multiplicity remains visible in `I`, while `C` awards one unit to an owner within a cell. The same owner may appear once in each of several cells without being duplicated in `G`.

Conditional well-definedness is straightforward but important. If `kappa` is total and satisfies the biconditional, changing an input representative within the same oriented owner cannot change its `G` row or its cell-level owner key. Deduplication inside a cell is therefore invariant under representative choice. Conversely, two different canonical owner bytes cannot be merged in `C` without violating the definition. This set-theoretic argument does not prove that `kappa` exists or that the frozen inputs are resolved; it states what follows if the primary certificate closes.

The three estimands answer noninterchangeable questions. The cardinality of `G` concerns distinct global oriented owners represented in the population. The rows of `I` retain provenance and allow one owner to be traced back to every input occurrence. The rows of `C` enforce no-double-credit within a frozen correspondence cell while allowing the same owner to occur in several cells. Publishing only `G` or only `C` would destroy occurrence-level information needed to reconstruct `I`; conversely, a complete `I` can induce `G` and `C` by the stated projections, but separate materializations make the transformations independently auditable. For that reason their schemas, validation rules, and summary statistics should be declared independently.

Materialization must remain conditional on zero unresolved owner rows. If even one input cannot be rooted or canonicalized, `I` may retain a diagnostic record but `G` and `C` cannot be reported as complete estimands. A partial table may be useful for method development only if it is labeled incomplete and does not award owner counts. This stop rule prevents missing inputs from being silently treated as new, different, or irrelevant owners.

# Evidence-Synthesis Findings {#5-evidence-synthesis-findings}

Eight precommitted positions control this manuscript. First, the frozen corpus supplies complementary subgroup, ambient-conjugacy, arithmetic, reduction, and hyperbolic-group components, but no executed complete oriented `Gamma_0(11)` owner solver. Second, the primary certificate target is the deterministic canonicalization biconditional. Third, the 9,453-row table is a derived adversarial audit, and aggregate counts remain post-closure controls. Fourth, `G`, `I`, and `C` are distinct estimands populated only after owner closure.

Fifth, a complete prospective certificate preserves subgroup membership, orientation, primitive-root status, inverse linkage, traversal exponent, deterministic serialization, and replayable failure evidence while keeping Hecke degree separate. Sixth, the article's methodological contribution is the separation of canonical proof object, audit expansion, and estimands. Seventh, metadata and source-identity closure do not clear theorem passages, retraction status, source conflicts, or the theorem-to-certificate bridge. Eighth, the manuscript remains A1-only and changes no scientific result or Route state.

These are evidence-synthesis and design findings. They do not imply feasibility, novelty, theorem correctness, or implementation readiness. The central scientific state remains `NOT_EXECUTED`.

# Reproducibility and Prospective Interface {#6-reproducibility-and-prospective-interface}

Reproducibility in the present article means that another reader can recover the frozen corpus, Phase-4 report, Phase-5 reviews, Phase-6 manifest, and revision log from named hash-bound artifacts. The literature selection and source ledger are inspectable, and the citation/reference/source-ID sets close. Generative prose is not promised to be byte-reproducible, and source-passage judgments cannot be replayed because the locators were never finalized.

A later scientific package should freeze four layers before reading owner outcomes. Layer one binds the exact `Gamma_0(11)` representation and proves every input conversion. Layer two binds the canonicalization and root theorem, including both directions of the biconditional. Layer three freezes producer and verifier schemas, adversarial fixtures, and typed failure states. Layer four defines the derived all-pairs audit and the conditional `G/I/C` materialization. Hashes, theorem versions, serialization versions, and fixture manifests should be immutable across execution.

The smallest valid next test is not the census. It is a theorem-to-certificate dossier evaluated against deliberately small, target-blind fixtures. Scientific population execution requires separate authorization after the primary biconditional, root policy, inverse policy, and independent verifier have closed. A missing theorem or unresolved fixture should terminate as `NOT_EVALUABLE_CONJUGACY_INCOMPLETE`, not as a negative owner result.

# Discussion and Implications {#7-discussion-and-implications}

The revised architecture improves the match between the mathematical object and its evidence. A partition is naturally represented by a total equivalence invariant. Expanding that invariant to every pair can be an excellent audit, but expansion size should not be confused with proof content. This distinction reduces a false quadratic necessity while preserving the most demanding adversarial check available for the fixed population.

The change does not make P31 easy. The canonicalization theorem must simultaneously handle exact subgroup membership, oriented conjugacy, primitive roots, inverse linkage, and deterministic bytes. A compact certificate that lacks either direction of the biconditional would be weaker than the all-pairs design it replaces. The revision therefore narrows the foundational object without lowering the exactness standard.

The `G/I/C` separation also clarifies what a future result would mean. `G` answers how many global oriented primitive owners occur. `I` records how the 138 frozen instances map to those owners. `C` answers how owner identity contributes within each frozen correspondence cell. None of the inherited instance summaries can substitute for these estimands, and no cell-local recurrence can multiply the number of global owners.

The architecture is intentionally compatible with more than one future mathematical implementation. A polygonal reducer, an arithmetic route, or a word-hyperbolic route could be considered, provided its exact hypotheses and evidence are bound to the same owner semantics. This interoperability is conditional: different producers cannot be compared until they preserve orientation, root status, inverse linkage, and serialization under one independently checked contract. The article therefore standardizes the meaning of a prospective result without claiming that any implementation route is presently adequate.

For Route A, this remains primitive-owner infrastructure at A1. No primitive Euler product, dynamical determinant, zero comparison, analytic continuation, or arithmetic specificity test is produced. Editorial improvement cannot promote a Route coordinate. Route B remains closed because there is no Route-A readiness, Hilbert space, operator, domain, self-adjointness result, trace formula, or divisor identity.

# Acknowledged Limitations {#8-acknowledged-limitations}

The dominant limitation is citation resolution. All 22 prose citation pairs retain `anchor:none`. The source ledger supports identity, metadata, and bounded claim-fitness accounting, but the exact passages and theorem hypotheses were not frozen. Claim-to-passage faithfulness is therefore `INCONCLUSIVE`. Revision 1 narrows language rather than inventing locators.

The corpus has no general current retraction or source-conflict clearance. Those checks remain unrun and their status remains unknown. The P31-S16 page correction is preserved, but one corrected field does not constitute a clean integrity screen. The corpus is historically weighted and no new contribution or novelty comparison was authorized.

The method architecture is uninstantiated. There is no bound canonicalization theorem, no producer or independent verifier, no completed fixture suite, no owner decision, and no `G/I/C` output. The conditional definitions show how outputs would relate after closure; they do not close the primary mathematical obligation.

Finally, AI-assisted review and drafting used one Codex model family with procedural role separation. This supplies multiple documented perspectives, not statistically independent validation. Liang Wang's gate confirmations establish author decisions and workflow authority only; they are not evidence of personal full-text checking.

# Future Work {#9-future-work}

Future work should proceed in this order:

1.  perform a separately authorized source-finalization pass that freezes exact theorem passages, hypotheses, correction status, and any required source-conflict or retraction checks;

2.  bind one exact subgroup representation and prove the conversion from every frozen input;

3.  state and prove the canonicalization biconditional, maximal-root contract, orientation convention, and inverse-link rule;

4.  freeze certificate schemas, producer/verifier roles, typed failures, and target-blind adversarial fixtures;

5.  execute the 138 per-instance certifications only after the interface recheck passes;

6.  derive the 9,453-row audit and compare it with optional direct pair checks without treating aggregate counts as pair evidence; and

7.  materialize and independently validate `G`, `I`, and `C` only after zero unresolved owner inputs.

Each step requires a new gate when it extends beyond literature-only manuscript composition. Nothing in this article authorizes retrieval or scientific execution.

# Conclusion {#10-conclusion}

P31 now has a more defensible certificate architecture. The foundational target is a total deterministic canonical owner map with a proved biconditional for oriented primitive `Gamma_0(11)` ownership. The 9,453-row table remains a full-population adversarial audit derived from that certificate, not a presumed uniquely necessary collection of bespoke proofs. Aggregate class counts remain weaker controls, and the global owner table `G`, incidence relation `I`, and cell-local quotient `C` remain distinct conditional outputs.

This is concrete design-level progress, but it is not a scientific result. No canonical form, owner partition, pair audit, theorem, computation, or estimand table has been executed. The source corpus remains passage-unresolved. A bounded Stage 2.5 textual-originality screen found no exact match within its declared samples and corpora, but scientific contribution novelty remains unassessed; the formal Route-A tuple remains `UNASSIGNED`, positive arithmetic A2 remains absent, and Route B remains closed.

# Declarations {#declarations .unnumbered}

#### Author contribution and accountability.

Liang Wang specified the mathematical object and restrictions, supplied the conceptual direction, approved the recorded stage gates, adjudicated the certificate-first design, and is responsible for the manuscript's scholarly content. AI assistance is disclosed below and is not credited with authorship. Stage-gate approval does not attest that the author personally performed full-text or exact source-passage verification.

#### Funding.

No funding was received for this work.

#### Competing interests.

The author declares no competing interests.

#### Ethics statement.

Human-subjects and animal-research review is not applicable. The work concerns theoretical mathematics, published-source records, and project-owned workflow artifacts; it involves no participants, identifiable personal data, animals, recruitment, or intervention.

#### Data and materials availability.

The materials are the frozen 22-row source inventory and the hash-bound project artifacts recorded for Round 10. No owner ledger, scientific dataset, solver output, pair-decision table, or `G/I/C` result was generated during manuscript preparation.

# AI Disclosure and Verification Limitation {#ai-disclosure-and-verification-limitation .unnumbered}

OpenAI Codex, using the GPT-5 model family, assisted during the session dated 2026-09-02 UTC; the exact backend snapshot/build was not exposed. AI-assisted work in the recorded pipeline included literature-search support, source-identity and metadata checking, evidence-matrix construction, evidence synthesis, report drafting, four role-based Phase-5 reviews, review synthesis, ClaimIntent-constrained Revision-1 drafting, citation-ID/reference closure checks, and revision-log accounting. No AI system executed a P31 solver, proof, pair decision, owner census, experiment, or canonical-results refresh.

Liang Wang is the responsible human author. He approved the project restrictions, stage gates, and the Phase-6 author-adjudicated design choice. Those approvals must not be interpreted as a statement that he personally read every source in full or verified any claim at the exact source-passage level. The recorded verification was bounded mainly to source identity, metadata, abstracts, authoritative landing pages, and project-local claim-fitness records. All 22 citations lack passage locators, so claim-to-passage faithfulness remains `INCONCLUSIVE`; the article does not claim theorem-level source verification, novelty clearance, or a clean retraction/conflict screen.
