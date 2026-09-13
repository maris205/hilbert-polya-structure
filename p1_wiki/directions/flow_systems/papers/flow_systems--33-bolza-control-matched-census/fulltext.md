---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--33-bolza-control-matched-census"
canonical_tex: "flow_systems/papers/33-bolza-control-matched-census/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/33-bolza-control-matched-census/paper/paper.pdf"
source_sha256: "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Interoperable Certificate Design for Primitive Geodesic Ownership on Two Frozen Genus-Two Surfaces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/33-bolza-control-matched-census>)
- [规范 TeX](<../../../../../flow_systems/papers/33-bolza-control-matched-census/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/33-bolza-control-matched-census/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/33-bolza-control-matched-census/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/33-bolza-control-matched-census/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This report asks what exact-certificate architecture could eventually support primitive-geodesic ownership decisions for a source-locked Bolza surface and one frozen nonarithmetic genus-two control at $\Lambda=21/10$. Stage 1 executed a closed-corpus literature synthesis, not a census or algorithm validation. The evidence supports object, candidate-generation, conjugacy, root-decision, owner-semantics, rigorous-predicate, and producer-checker components, but identifies no project owner. The review-adjudicated architecture permits two surface-specific exact proof producers, provided they emit one common semantic owner-certificate schema checked by an independent validator. The schema separates full-group conjugacy, maximal-root and primitivity evidence, external inversion pairing, self-reciprocity, repetitions, termination, completeness, and positive or negative replay payloads. It requires no common internal solver or input model. All implementation remains prospective. At the frozen cutoff, the target is largely an inherited systolic-empty replay, while nontrivial prospective closure lies on the control; this asymmetry prohibits a between-surface arithmetic inference. P33-RC-1 is reorganized into producer soundness, schema interoperability, and independent validation, with a fail-closed not-evaluable endpoint. The contribution is an interoperable certificate-methods design, not a census, novelty claim, magnetic or determinant result, formal Route-A tuple, or Route-B progress.
author:
- |
  Liang Wang^1^\
  ^1^School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Luoyu Road 1037, 430070, Hubei, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 2 September 2026
title: 'Interoperable Certificate Design for Primitive Geodesic Ownership on Two Frozen Genus-Two Surfaces'
```

## Markdown 正文

**Keywords:** genus-two surface; Bolza surface; primitive geodesic; conjugacy certificate; inversion-paired owner; evidence synthesis; independent validation

# 繁體中文摘要 {#繁體中文摘要 .unnumbered}

本研究探討：在兩個來源鎖定的緊緻虧格二雙曲曲面上，何種精確憑證架構可支援原始閉測地線的所有權判定。研究對象固定為 Bolza 目標曲面與一個非算術控制曲面，動力學子型固定為單位速率的物理基底測地時間、磁場參數 $b=1/2$ 及有號磁場的偶數子序列；共同截斷值維持為 $\Lambda=21/10$，且不得依已知方向重新調整。本研究實際執行的是封閉語料的文獻查核、證據整合及方法設計，並未執行測地線普查、共軛判定、原始根判定、數值實驗或路線圖評分。綜合結果支持一項受限架構：兩個曲面可採用各自專屬的精確證明產生器，但輸出必須進入共同的語義憑證綱要，再由獨立驗證器檢查。綱要須分離完整群共軛、最大根與原始性、外部反元素配對、自互反性、重複軌道、終止性、完備性，以及正面或負面的重播證據。共同語義不要求共同的內部演算法或數值表示。固定截斷值造成明顯不對稱：目標端主要是既有系統短線界限下的空集合重播，控制端才承擔非平凡的前瞻性封閉工作，因此兩端差異不能支持算術性推論。P33-RC-1 的七項義務仍為零項完成；產生器、綱要、驗證器與普查均未實作。本文的落地成果是可稽核的憑證方法設計，而不是已完成的科學普查、磁流或行列式結果，也不是 Route A 或 Route B 的正式結論。

# Introduction

::: {#problem-and-scope}
## Problem and scope
:::

A primitive closed-geodesic list is not automatically an ownership theorem. For this project, one unoriented primitive owner is the unit $$\{[g]_{\Gamma},[g^{-1}]_{\Gamma}\},$$ with admission under the frozen exact translation-length predicate $\ell(g)\leq 21/10$. A valid owner record therefore needs more than a word, trace, matrix, or approximate length. It needs a full surface-group conjugacy disposition, a maximal-root or no-proper-power disposition, an external inversion-pair assignment, a cutoff proof, and a completeness account for the candidate universe. Powers are repetitions rather than new primitive owners. A self-reciprocal class is a special internal relation and does not replace the external inverse-pair convention.

The two project objects originate in a substantial but heterogeneous literature. Nazarenko (2013) [@P33-S01] supplies the compact genus-two octagon-family and generator context from which the frozen control is drawn. Aigon-Dupuy et al. (2005) [@P33-S02] provide peer-reviewed family-level context for genus-two hyperbolic octagons and Fuchsian descriptions. For the target, Aurich et al. (1991) [@P33-S05] provide regular-octagon matrices, a length relation, and a periodic-orbit enumeration precedent, while Katz et al. (2016) [@P33-S08] provide arithmetic-Fuchsian and quaternion-order context for the Bolza surface. Grácio and Sousa Ramos (2010) [@P33-S09] connect symbolic dynamics and fundamental-group words to genus-two length-spectrum computation. These contributions support objects and candidate-generation contexts; they are not treated as completed P33 owner censuses.

::: {#research-question}
## Research question
:::

The frozen research question is:

**Research question.** Can exact full-conjugacy, inversion-pair, primitivity, and completeness certificates close both frozen owner censuses at the inherited cutoff $\Lambda=21/10$ beyond the already-known coarse support?

Stage 1 does not answer this question through execution. It addresses the prior methods question: what architecture is supported by the verified, frozen literature, what semantic contract must be shared across heterogeneous surface-specific proof routes, and which obligations remain open before computation may begin?

The inherited cutoff was historically target-blind, but its coarse support implication is now known. The source-locked target inequality places the Bolza side below its inherited systolic threshold, so successful replay there is expected to certify an empty below-cutoff universe. The source-locked control has an inherited witness below the same cutoff, so its successful replay must include at least one primitive owner. Neither direction is discovered here. The common cutoff straddles the two inherited systolic contexts; it is not a matched scientific comparison and must not be retuned after the outcome direction became known.

::: {#bounded-contribution}
## Bounded contribution
:::

The contribution is a review-adjudicated certificate-methods design based on semantic commonality without forced implementation identity. Bolza and control producers may use different representations, algorithms, and theorem routes, but must emit one semantic schema for independent checking. This prose architecture does not establish producer feasibility, theorem applicability, validator termination, owner admission, novelty, or priority.

# Literature and Theoretical Framework

::: {#frozen-geometry-arithmetic-context-and-candidate-generation}
## Frozen geometry, arithmetic context, and candidate generation
:::

The control is one source-locked specialization within a compact genus-two octagon family, not a representative of all nonarithmetic surfaces. Nazarenko (2013) [@P33-S01] supports the construction and generator layer, and Aigon-Dupuy et al. (2005) [@P33-S02] support a broader peer-reviewed octagon-family setting. Neither source, by itself, proves the project specialization's arithmetic status, exact systole, or primitive-owner census.

The control's nonarithmeticity remains a bounded multi-source and inherited-project input. Takeuchi (1975) [@P33-S03] supplies an arithmetic-Fuchsian trace-field criterion, with the frozen verification record preserving the associated 2006 correction. Popescu (2024) [@P33-S04] supplies a Lindemann-Weierstrass ingredient relevant to the inherited expression containing $\exp(-1/5)$. The project-specific inference would require those ingredients to be applied to the exact frozen trace formula; this Phase-6 revision neither reconstructs nor newly proves that chain.

The target is similarly treated through bounded complementary context. Aurich et al. (1991) [@P33-S05] provide regular-octagon periodic-orbit and matrix context, and Katz et al. (2016) [@P33-S08] provide exact arithmetic and quaternion-order context for Bolza. Jenni (1984) [@P33-S06] remains PLAUSIBLE, page-unpinned, and context-only in the frozen verifier; it is not used here to assert an exact systole theorem or formula. Schmutz (1993) [@P33-S07] supplies broader extremal and systolic context without independently validating the project replay inequality. Thus object identity, arithmetic characterization, systolic context, and below-cutoff owner closure remain separate evidence surfaces.

::: {#from-candidate-words-to-owner-semantics}
## From candidate words to owner semantics
:::

Candidate generation and ownership require different proof objects. Aurich et al. (1991) [@P33-S05] and Grácio and Sousa Ramos (2010) [@P33-S09] support pathways from exact or symbolic group data to length-spectrum candidates. Such candidates are not unique owners merely because they share a length, trace, homology class, literal word, or matrix representation. Under the frozen design, those quantities may filter or organize work, but none is a substitute for full-group conjugacy.

Primitive and reciprocal semantics must also remain distinct. Cherubini et al. (2022) [@P33-S14] connect primitive closed-geodesic counting to primitive root-conjugacy classes and distinguish primitive classes from repetitions. Erlandsson and Souto (2024) [@P33-S15] study reciprocal geodesics, including the special case in which a class is conjugate to its inverse. P33 applies external inversion pairing to every oriented class, including non-self-reciprocal classes. Consequently, full conjugacy, maximal-root status, self-reciprocity, external inversion pairing, and repetition accounting require independently tagged dispositions.

::: {#algorithmic-components-under-heterogeneous-inputs}
## Algorithmic components under heterogeneous inputs
:::

The frozen corpus contains strong component-level algorithmic precedents but no finished cross-surface implementation. Voight (2009) [@P33-S10] develops exact fundamental-domain, presentation, reduction, and word-problem methods for suitable cofinite Fuchsian input. Despré et al. (2023) [@P33-S11] give a terminating Dirichlet-domain method from a hyperbolic surface polygon with side pairings, under a different computational input setting. Their applicability cannot be silently unified for the frozen algebraic target and source-locked transcendental control.

Epstein and Holt (2006) [@P33-S12] establish a general conjugacy solution for word-hyperbolic groups and include a positive-conjugator pathway; the corrected frozen page range is 287--305. Lysenok (1990) [@P33-S13] provides root-extraction and related algorithmic solvability in hyperbolic groups. These results support feasibility classes. They do not instantiate project-specific constants, canonical negative evidence, exact generator encodings, hash-stable serialization, or proof that both frozen presentations satisfy every required hypothesis.

The design implication is narrower than a transferred theorem. Each surface-specific producer must eventually bind its own exact representation, theorem identifiers, implementation versions, and applicability proof. Interoperability need not force those internals to be the same. What must be common is the meaning of the claims that leave the producer.

::: {#rigorous-predicates-and-producer-validator-separation}
## Rigorous predicates and producer-validator separation
:::

Strohmaier and Uski (2013, corrected 2018) [@P33-S16] illustrate a separation among bounded computation, error control, and completeness reasoning for spectral objects on hyperbolic surfaces; their correction remains visible and their determinant endpoint is outside P33. Johansson (2017) [@P33-S17] presents arbitrary-precision midpoint-radius arithmetic with explicit error radii. Rump (2010) [@P33-S18] surveys rigorous verification using floating-point computation. These works support proof-bearing enclosure discipline for appropriate numerical predicates, but interval arithmetic does not decide group conjugacy or primitivity.

Hoffman et al. (2016) [@P33-S19] provide a nearby example of separating approximate hyperbolic-geometry candidates from rigorously validated outputs, although their objects are hyperbolic three-manifolds rather than the present closed surfaces. Hales et al. (2017) [@P33-S20] provide a large-scale precedent for production computation accompanied by independently checkable formal artifacts. P33 uses these as architectural precedents only. The literature does not validate an unbuilt P33 producer or require that P33 adopt any one proof-assistant or numerical library.

# Executed Methodology

::: {#closed-corpus-design}
## Closed-corpus design
:::

The executed method was a staged literature investigation. Phase 1 froze the research question, the two source-locked surfaces, unit-speed physical base-geodesic time, $b=1/2$, the signed-field even subsequence, the inverse-paired primitive-owner rule, $\Lambda=21/10$, the result taxonomy, and fail-closed states. Phase 2 screened the bounded search output, retained 20 sources, and recorded source identity, verification outcome, admissible use, exclusion boundary, and locator status. Phase 3 aligned retained sources to source-effect rows and thematic synthesis. Phase 4 produced the first research report. Phase 5 performed separately recorded editorial, ethics, citation-integrity, and Devil's Advocate reviews, followed by synthesis and checkpointing. Phase 6 froze eight revised claim intents before this report was written.

No retrieval, new source, locator, quotation, experiment, or scientific computation occurred during revision. No geodesic, conjugacy query, root query, systole proof, certificate, schema implementation, validator, or fixture was executed, and no canonical result was refreshed. The findings concern evidence support and open obligations, not newly computed dynamics.

::: {#source-verification-and-evidence-controls}
## Source verification and evidence controls
:::

The inventory contains 20 sources: nine S2\_VERIFIED, ten VERIFIED, and one PLAUSIBLE; 18 were conservatively counted as peer reviewed. S2\_VERIFIED establishes record identity and metadata, not theorem- or passage-level support. The evidence matrix separated admissible contributions from stronger excluded uses.

Correction and locator boundaries were carried forward exactly. The Takeuchi record retains its correction binding (Takeuchi, 1975) [@P33-S03] , and the Strohmaier-Uski record retains its 2018 correction binding (Strohmaier and Uski, 2013, corrected 2018) [@P33-S16] . Epstein and Holt (2006) [@P33-S12] retains pages 287--305. Jenni (1984) [@P33-S06] remains PLAUSIBLE, page-unpinned, and context-only.

Every literature statement has a visible frozen citation and anchor:none; no direct quotation is used. Exact passages were not supplied, so all 48 uses remain locator warnings and claim-to-passage faithfulness is INCONCLUSIVE. No systematic source-level retraction or conflict-of-interest audit was run, and correction records are not clearance findings.

::: {#synthesis-and-adjudication-method}
## Synthesis and adjudication method
:::

The synthesis was limited to eight manifest claims. Review comments informed architecture, article positioning, asymmetry, and AI provenance; requests requiring retrieval, source finalization, science, or implementation remain limitations. The design asks whether separate exact routes can share owner semantics and whether an independent validator can reject unsupported claims. A positive design answer is not an implementation answer.

# Review-Adjudicated Proof and Method Architecture

::: {#two-surface-specific-exact-proof-producer-contracts}
## Two surface-specific exact proof-producer contracts
:::

The architecture defines two prospective producer roles.

**Bolza proof producer (BP).** BP would consume the exact source-locked Bolza presentation and frozen semantic locks. A later freeze must identify exact generator encodings, theorem and algorithm versions for domain/reduction, conjugacy, roots, and completeness, and prove applicability. BP must emit proof payloads, not status labels.

**Control proof producer (CP).** CP would consume the source-locked control and the same semantic locks, but may use different number representations and proof routes. Its later freeze must likewise bind exact encodings, predicates, versions, and applicability. BP need not represent CP's input.

"Exact proof producer" requires checkable evidence under a declared proof type; it does not assert existing software. Producer proofs may differ, while their semantic conclusions remain comparable.

::: {#one-common-semantic-owner-certificate-schema}
## One common semantic owner-certificate schema
:::

The proposed common schema is a versioned semantic envelope around producer-specific evidence. It is a design specification, not a serialized artifact already frozen for execution. Its minimum record families are:

  Record family                  Required semantic fields                                                                                                                                                            Fail-closed purpose
  ------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  Run header                     schema version; surface ID; producer and proof-type IDs; input, theorem-version, implementation, and correction-provenance digests; frozen clock, subtype, owner rule, and cutoff   binds every claim to one exact prospective run and prevents silent input or correction drift
  Candidate                      stable candidate digest; producer-normalized representation; enumeration provenance; exact or proof-bearing cutoff disposition                                                      distinguishes candidate generation from owner admission
  Conjugacy                      ordered pair of oriented-class candidates; exactly one positive, negative, or unresolved disposition; positive conjugator or producer-specific negative/canonical proof payload     prevents filters, timeouts, or failed searches from becoming nonconjugacy proofs
  Root/primitivity               maximal-root representative and exponent, or independently checkable no-proper-power payload; primitive/repetition disposition                                                      prevents a power from minting a primitive owner
  Inversion and reciprocity      oriented class ID; inverse-class link; external owner-pair ID; separately proved self-reciprocal flag                                                                               applies inverse pairing universally while preserving the reciprocal special case
  Owner and repetition           deterministic owner ID; member oriented classes; primitive representative; all admitted repetitions mapped to that owner                                                            keeps multiplicity and repetition separate from owner credit
  Termination and completeness   theorem-bounded candidate-universe descriptor; termination witness; resolved/unresolved totals; coverage digest; resource-stop state                                                distinguishes complete, bounded-incomplete, and not-evaluable outcomes
  Validation                     validator version and digest; per-predicate decisions; rejected incompatibilities; accepted/rejected fixture-set digest                                                             prevents a producer from self-certifying its summary

Records would be ordered by surface, family, and stable semantic digest; owner membership by oriented-class digest. A future freeze must fix character normalization, line endings, number encoding, key order, proof tags, digest algorithm, and the exact versioned hash domain. No execution digest is emitted here.

Positive evidence requires a replayable producer-appropriate witness. Negative evidence requires a theorem-backed canonical or exhaustive payload; failed search, timeout, cap, or numerical nonmatch is not a certificate. The validator may dispatch tags to independent BP and CP adapters, so common semantics do not imply common solver code.

The schema has explicit incompatibility rules. A complete run cannot contain an unresolved conjugacy, root, cutoff, or owner disposition. A primitive record cannot simultaneously report an exponent greater than one. A repetition cannot create an owner ID distinct from its primitive root's owner. A self-reciprocal flag requires its own conjugacy-to-inverse evidence, while external inverse pairing is required regardless of that flag. A complete status is incompatible with a failed termination or coverage predicate, a missing correction binding, duplicate canonical owner IDs, hash drift, or an unrecognized proof type.

::: {#independent-validator-contract}
## Independent validator contract
:::

The validator is one semantic checker with independent proof adapters, not a copy of either census loop. It must derive status from predicates rather than trust producer labels. Checks include schema/bytes, provenance and hashes, cutoff replay, conjugacy, root evidence, inversion, reciprocity, repetition, uniqueness, termination, coverage, and zero unresolved records. Failure yields rejection, bounded-incomplete, or not-evaluable status under a later state table.

Fixtures must include accepted minimal records and rejected malformed schemas, unknown proof types, altered digests, unsupported negative decisions, primitive/power conflicts, missing inverse links, false reciprocity, duplicate owners, unresolved cutoffs, incomplete coverage, invalid termination, and hash mismatch. No fixture bytes or runs exist.

::: {#p33-rc-1-reorganized-as-a-three-package-fail-closed-gate}
## P33-RC-1 reorganized as a three-package fail-closed gate
:::

The seven original obligations remain unchanged and unimplemented. Revision-1 reorganizes them so that shared semantics are not confused with shared implementation.

  Package                             Original obligations retained                                                                                             Prospective closure evidence                                                                                                                                                                       Current status
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  A. Producer-specific soundness      representation applicability; 2 full conjugacy; 4 root and primitivity; producer side of 5 termination and completeness   for BP and CP separately: exact input encoding, named theorem/algorithm versions, applicability proof, positive and negative proof types, maximal-root logic, candidate bound, termination proof   unimplemented
  B. Common-schema interoperability   external inversion pairing; 6 deterministic artifacts; shared side of 5 completeness                                      versioned field schema, canonical ordering, proof-type registry, correction provenance, serialization and hash domain, repetition rules, coverage and unresolved ledgers                           unimplemented
  C. Independent validation           independent validation; checker side of 2, 4, 5, and 6                                                                    independent validator and proof adapters, predicate table, incompatibility checks, accepted/rejected fixtures, replay receipts                                                                     unimplemented

The underlying count remains zero of seven implemented obligations. This report supplies a more precise prospective contract, not closure evidence. If either producer lacks a sound exact conjugacy method, or if a negative disposition cannot be independently certified, the lawful fallback remains NOT\_EVALUABLE\_CONJUGACY\_METHOD\_UNAVAILABLE. If a resource stop prevents complete coverage while some valid records exist, the output must be bounded-incomplete rather than a negative theorem.

The literature supports the three-package architecture only at component and precedent level. Voight (2009) [@P33-S10] and Despré et al. (2023) [@P33-S11] support different domain or presentation pathways. Epstein and Holt (2006) [@P33-S12] and Lysenok (1990) [@P33-S13] support conjugacy and root-decision components. Cherubini et al. (2022) [@P33-S14] and Erlandsson and Souto (2024) [@P33-S15] motivate separate primitive, repetition, reciprocal, and inverse-pair semantics. Strohmaier and Uski (2013, corrected 2018) [@P33-S16] , Johansson (2017) [@P33-S17] , and Rump (2010) [@P33-S18] support rigorous predicate and enclosure discipline. Hoffman et al. (2016) [@P33-S19] and Hales et al. (2017) [@P33-S20] support the broader producer-validator pattern. None supplies the missing P33 implementation or scientific result.

## Audit interpretation of the prospective contract

The three-package organization is intended to make later evidence auditable without pretending that prose is executable. Package A is evaluated separately for BP and CP. For each producer, a future reviewer would need to identify the exact mathematical input, the representation of generators and words, the theorem or algorithm invoked for every decision, and the hypotheses that connect that theorem to the frozen surface. A producer label, a successful program exit, or an approximate numerical match would not meet this burden. Each positive decision would need a replayable witness appropriate to its proof type; each negative decision would need canonical, exhaustive, or otherwise theorem-backed evidence. If a producer can generate candidates but cannot justify a negative full-group conjugacy decision, it cannot report a complete owner set. The contract therefore treats implementation availability and mathematical soundness as distinct questions.

Package B concerns the meanings carried across that producer boundary. A common record must say which surface, run, candidate, oriented class, primitive root, inverse partner, and owner it concerns. It must also distinguish an assertion about a class from the payload offered to support that assertion. The schema cannot infer primitivity from a short word, infer ownership from equal length, or infer self-reciprocity from the external convention that pairs every class with its inverse. Repetitions must point back to the owner of their primitive root, while a self-reciprocal flag must carry separate conjugacy-to-inverse evidence. Likewise, a cutoff disposition must record the exact or proof-bearing comparison it uses rather than a rounded decimal. These are semantic constraints on any future serialization; the present manuscript neither fixes the bytes nor selects a universal proof language.

Interoperability also requires explicit treatment of incomplete information. Positive, negative, and unresolved dispositions are not interchangeable. A timeout, cap, failed search, missing adapter, unknown proof tag, or hash mismatch must remain visible and cannot be coerced to a negative answer. A run claiming completeness would have to account for every theorem-bounded candidate and every derived oriented class, with no unresolved conjugacy, root, cutoff, inversion, or owner relation. A bounded search that returns some valid records but lacks coverage may still be useful, yet its lawful status is bounded-incomplete. If an exact conjugacy method is unavailable for either frozen presentation, the contract preserves `NOT_EVALUABLE_CONJUGACY_METHOD_UNAVAILABLE`. This status is an execution limitation, not a theorem that the corresponding geodesic or owner does not exist.

Package C makes those rules checkable by a party that does not trust producer summaries. Independence here is architectural: the validator derives acceptance from schema fields and replayed predicates, and producer-specific adapters expose only the proof types they know how to check. A future test set would need both accepted records and deliberately rejected counterexamples. Rejection cases include altered provenance digests, unrecognized proof types, unsupported negative decisions, a primitive record carrying exponent greater than one, a repetition assigned a fresh owner, a missing inverse link, an asserted self-reciprocity relation without evidence, duplicate owner identifiers, unresolved cutoffs inside a complete run, and a coverage total inconsistent with the candidate universe. Passing such fixtures would test a frozen validator version; it would not by itself certify either surface census.

The contract also separates local record validity from population completeness. A conjugacy witness may be correct for one pair while the candidate universe is incomplete. A root witness may be correct while inverse pairing is absent. A collection of individually sound owner records may still omit an admissible owner. Conversely, a proof that no candidate lies below the cutoff must bind the candidate bound, length predicate, termination argument, and correction provenance; an empty output file is not an empty-universe certificate. This separation is especially important for the inherited Bolza-side emptiness, where the apparent scientific answer is coarse but the future replay burden still includes provenance, predicate, termination, and completeness evidence.

Finally, every prospective run would need a state transition that can be reconstructed from the evidence. Producer creation, schema serialization, validation, scientific interpretation, and roadmap interpretation are separate events. A validator acceptance could authorize reporting a per-surface certificate status only under a later gate; it could not automatically award Route-A credit or open Route B. Rejection or non-evaluability would report the failed obligation without strengthening a geometric conclusion. This manuscript provides the vocabulary and failure semantics for such an audit. It does not create schema bytes, fixtures, software, certificates, owners, completeness proofs, or a route verdict, and all seven P33-RC-1 obligations remain unimplemented.

# Evidence-Synthesis Findings

::: {#object-support-without-owner-identification}
## Object support without owner identification
:::

The frozen literature supports genus-two octagon objects, Bolza context, and candidate-generation precedents, but it does not itself identify unique primitive inverse-paired owners. Nazarenko (2013) [@P33-S01] and Aigon-Dupuy et al. (2005) [@P33-S02] bound the control-family context. Aurich et al. (1991) [@P33-S05] , Katz et al. (2016) [@P33-S08] , and Grácio and Sousa Ramos (2010) [@P33-S09] bound complementary target and candidate-generation contexts. No cited source is converted into a project-level full-conjugacy, maximal-root, inverse-pair, or completeness certificate.

::: {#heterogeneous-exact-producers-are-compatible-at-the-semantic-layer}
## Heterogeneous exact producers are compatible at the semantic layer
:::

The synthesis supports a conditional design: two sound surface-specific proof producers may be acceptable if they emit one common semantic owner-certificate schema that an independent validator checks. This conclusion removes a false necessity identified in review. It does not claim that either producer is available, that both exact input models have been selected, or that one validator has been implemented. The common layer standardizes meanings and admissible evidence states; it does not standardize the mathematics inside each producer.

::: {#the-frozen-cutoff-asymmetry-is-material}
## The frozen-cutoff asymmetry is material
:::

At $\Lambda=21/10$, the target side is largely constrained by the inherited systolic-empty replay, whereas the nontrivial prospective owner closure lies on the control side. This is a design fact inherited before the present revision, not a new census. It explains why a symmetric two-surface narrative would overstate what remains unknown on the target side. It also limits the scientific interpretation: an empty-versus-nonempty replay at a cutoff lying on opposite sides of the inherited systoles cannot distinguish arithmetic from nonarithmetic geometry.

The cutoff is therefore preserved without post-hoc normalization. The target still needs a valid completeness and empty-universe certificate under its producer contract, but that replay does not create a new comparative finding. The control still needs exact conjugacy, primitive-owner, inverse-pair, cutoff, and completeness closure, and its inherited witness does not establish the rest of the universe.

::: {#contribution-and-noncontribution}
## Contribution and noncontribution
:::

The achieved contribution is an interoperable exact-certificate methods design for one frozen target/control pair. It is not a completed owner census, validated software method, arithmetic comparison, magnetic comparison, determinant calculation, novelty assessment, exhaustive literature review, impossibility result, or owner no-go. Component nonclosure means that execution is not presently warranted under the frozen proof standard; it does not mean execution can never succeed.

# Reproducibility and Prospective Execution Interface

::: {#what-is-reproducible-now}
## What is reproducible now
:::

The present report can be audited against frozen project artifacts. Its Phase-6 claim manifest has identifier M-2026-09-02T11:37:06Z-33p6 and SHA-256 83500193f234eb5c2681ffd4c6bb3948f107adede9714fc1d1bc75ead2106191. The manifest binds the eight allowed claim surfaces and prohibits new retrieval, science, implementation, novelty assessment, or Route change. The Phase-4 report, four Phase-5 role reviews, synthesis, checkpoint, Phase-2 inventory, and source-verification tables are fixed inputs. The closed bibliography has 20 entries. This report preserves 48 adjacent citation/anchor pairs, covering all 20 source IDs, with every anchor set to none.

Reproducibility here means auditability of the frozen evidence trail, scope, citation closure, and manifest compliance. It is not computational reproducibility of the unimplemented method.

::: {#what-a-future-execution-freeze-must-add}
## What a future execution freeze must add
:::

A later, separately authorized phase would need to freeze BP and CP representations independently; exact theorem and implementation versions; applicability proofs; a byte-exact schema and proof-type registry; cutoff and length predicates; positive and negative evidence formats; canonical ordering and hash domain; correction provenance; resource limits and status transitions; an independent validator; and accepted/rejected fixtures. Only after those materials pass review could an execution produce a complete, bounded-incomplete, or not-evaluable census status.

Validated numerical methods may support cutoff or sign predicates where their hypotheses apply. Johansson (2017) [@P33-S17] and Rump (2010) [@P33-S18] support disciplined enclosure methods, but additional precision cannot prove nonconjugacy, maximal roots, or candidate completeness. The interface must keep numerical evidence subordinate to the exact group-theoretic proof type it is actually qualified to check.

::: {#state-separation}
## State separation
:::

Three axes must remain distinct in future reporting:

1.  **Execution status:** not run, rejected at freeze, bounded-incomplete, not evaluable, or completed under a frozen contract.

2.  **Scientific content:** per-surface owner and completeness outcomes, only if actually certified.

3.  **Roadmap interpretation:** Route-A or Route-B assessment, only under a separately authorized roadmap gate.

This separation prevents a well-designed schema from being misreported as a scientific result and prevents an execution failure from being misreported as a theorem about the surfaces.

# Discussion and Implications

::: {#methodological-implication}
## Methodological implication
:::

Interoperable evidence need not originate from identical machinery. A common semantic contract protects the meaning of conjugacy, primitivity, inversion, completeness, and failure while permitting producer-specific mathematics. Negative evidence is first-class: failed searches do not prove nonconjugacy, no-root status, or candidate completeness. The schema exposes these distinctions so validation can fail closed.

::: {#scientific-implication-of-the-cutoff}
## Scientific implication of the cutoff
:::

The frozen target-control pair remains useful as an interface stress test because its representations may demand different proof routes. It is not presently a clean arithmeticity experiment. The target's inherited empty replay and the control's nontrivial prospective closure are asymmetric, and the broader qualifying control panel is incomplete. Treating the two surfaces as interface cases preserves methodological value without converting the expected support direction into evidence for an arithmetic contrast.

::: {#route-and-dynamical-system-boundary}
## Route and dynamical-system boundary
:::

The dynamical subtype remains exactly as inherited: unit-speed physical base-geodesic time, $b=1/2$, and the signed-field even subsequence. The magnetic field remains a model lock rather than a compared outcome. No magnetic period, phase, stability, signed-$k$, field-sign, determinant, or spectral result is reported.

Within Route A, this report is preparation for a possible A1 ownership/completeness artifact only. It awards no A1 credit because no census or validator has run. The between-surface count contrast remains A0\_INCONCLUSIVE\_SYSTOLE\_CONFOUNDED, the panel remains A0\_CONTROL\_PANEL\_INCOMPLETE, and a formal A0 verdict is prohibited. A2--A4 are not run; positive arithmetic A2 remains absent. Route B is closed. The formal tuple remains UNASSIGNED.

# Acknowledged Limitations

First, the corpus is bounded, not exhaustive. Search interfaces did not yield auditable global hit totals, and the frozen search did not establish novelty, priority, impossibility, or complete disciplinary coverage. No new search was authorized for this revision.

Second, locator-level support remains materially incomplete. All 48 literature uses carry anchor:none. Exact page, section, paragraph, or quotation passages were not provided to the compiler, so claim-to-passage faithfulness remains INCONCLUSIVE. S06 is PLAUSIBLE, page-unpinned, and context-only. Nine S2\_VERIFIED records remain record-level matches rather than theorem validation.

Third, bibliographic source-status work remains open. The S03 and S16 corrections are preserved as bindings, and the corrected S12 pages are visible, but the frozen References list contains the base works only. This revision was required to preserve that closed list verbatim and therefore could not add correction entries. Systematic retraction and source-level conflict-of-interest screens were not performed.

Fourth, the architecture is unimplemented. Neither producer has a frozen exact representation or theorem-applicability proof. No schema bytes, proof registry, validator, proof adapter, fixture, candidate universe, conjugacy result, root result, owner record, termination proof, or completeness certificate exists. P33-RC-1 remains open with zero of seven obligations implemented.

Fifth, the frozen scientific design is asymmetric and limited. The target's below-cutoff emptiness is largely an inherited replay, while nontrivial closure lies on the control. The common cutoff is systole-confounded and the control panel is incomplete. The report cannot support a between-surface arithmetic conclusion or generalize to other genus-two surfaces.

Sixth, the review process used separately recorded roles within one AI model family. Procedural separation does not establish statistically independent errors or cross-model calibration. The responsible human author's authorization does not establish that he performed full-text or source-passage verification.

# Future Work

Future work requires separate gates. Source finalization could freeze exact passages, apply correction records, clarify S06, and screen retraction and source COI. Implementation design could specify BP and CP encodings, applicability, proof payloads, and termination. Schema and validator gates could freeze exact bytes, semantics, proof tags, status transitions, adapters, and fixtures.

Only after those gates pass should an execution gate replay the inherited locks and attempt the two censuses. Results would need per-surface completeness states and a zero-unresolved ledger before any complete status. A scientifically matched threshold or expanded control panel would be a different design and would require new authorization; it must not be retrofitted into this frozen cutoff.

# Conclusion

The frozen corpus supports an interoperable certificate-methods architecture, not an executed primitive-owner census. Two surface-specific exact proof producers may use different internal representations and theorem routes. Their outputs can be compared only through one common semantic schema that distinguishes conjugacy, roots and primitivity, external inversion, self-reciprocity, repetitions, cutoff evidence, termination, completeness, and positive or negative replay payloads. One independent validator must check that schema and dispatch producer-specific proof types without trusting producer status.

Revision-1 clarifies this architecture and reorganizes P33-RC-1 into producer-specific soundness, common-schema interoperability, and independent validation. It does not close any implementation or scientific obligation. The frozen-cutoff asymmetry remains explicit, every claim-to-passage binding remains inconclusive, and NOT\_EVALUABLE\_CONJUGACY\_METHOD\_UNAVAILABLE remains a lawful fail-closed endpoint.

Phase 6 therefore changes no census, Route tuple, A0 prohibition, positive arithmetic A2 status, Route-B status, formal project claim, canonical manuscript, or canonical result. The only achieved endpoint is a more precise, review-adjudicated methods and evidence-synthesis report.

# Declarations {#declarations .unnumbered}

#### Funding.

The author received no funding for this work.

#### Competing interests.

The author declares no competing financial or non-financial interests.

#### Author contributions.

Liang Wang is the sole responsible human author. He provided the research direction, conceptualization, methodological constraints, authorship information, declarations, and phase-gate authorizations; reviewed the bounded outputs; and accepts responsibility for the manuscript's scholarly content.

#### Ethics approval, consent to participate, and consent for publication.

Not applicable. This literature and certificate-design study involved no human participants, personal data, recruitment, intervention, or animal subjects.

#### Data, materials, and code availability.

The evidence used here is limited to the frozen project-local Stage-1 corpus, verification ledgers, synthesis artifacts, review records, and Stage-2 manifests identified in the associated repository. This manuscript produced no new scientific dataset, experimental output, owner census, validator implementation, or canonical-result refresh.

#### AI assistance and verification limitation.

OpenAI Codex from the GPT-5 model family assisted the recorded workflow with literature-search support, source-record and metadata checks, evidence extraction and synthesis, adversarial and role-based review, deterministic citation and hash checks, and manuscript drafting and restructuring on 2 September 2026 UTC. The exact backend snapshot was not exposed. Liang Wang supplied the project direction and remains the accountable author. The record does not establish that he personally performed full-text or source-passage verification. Exact passages were not supplied to the manuscript compiler: every literature use therefore retains `anchor=none` and `claim_to_passage=INCONCLUSIVE`. AI assistance and human authorization do not convert record-level evidence into verified passages, establish source cleanliness, or validate the prospective scientific method.
