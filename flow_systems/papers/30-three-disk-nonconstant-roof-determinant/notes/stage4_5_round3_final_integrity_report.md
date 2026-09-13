# P30 — Stage 4.5 Round 3 最终完整性报告

结论：**FAIL，停在强制检查点**。本报告针对 [当前审查稿](stage4_prime_revision_round4.tex)，没有修改正文、参考文献或科学材料。FAIL 表示存在未解决的证据支持、表述或作者声明依据缺口，不是对故意不端的认定，也不是新的 Route 判定。

## 范围与结果

| 核查 | 当前结果 | 边界 |
|---|---|---|
| A 文献字段 | 27/28 条通过，1 条错误 | 不等于全文、定理适用性或撤稿全筛查 |
| B 引用语境 | 30/30 个当前源使用语境有相应层级支持 | 包含明确的元数据/阅读任务用途，不升级为定理支持 |
| C 数据与记录 | 9/15 个核查分组与所述范围一致 | 分组不是实验样本 |
| D 原创性筛查 | 90/90 个声明的正文段落单元 | 引号检索加非引号补充；非专业查重或全网保证 |
| E 当前登记声明 | 421/438 条在限定范围获验证 | 所有登记声明均审查；语义提取完整性不可由机器证明 |
| E 证据行 | 438 个所选元组 | 官方构建、重放及报告内重放均通过 |
| E6 连续修订 | 80 项操作，2 条漂移记录 | 单独列示，不混入普通问题数 |

E 分类：VERIFIED 421；MINOR_DISTORTION 3；MAJOR_DISTORTION 3；UNVERIFIABLE 5；UNVERIFIABLE_ACCESS 6。

有限词法覆盖检查未登记候选为 0，但不能据此声称机器穷尽了所有实质声明。原创性审查覆盖声明范围内所有当前已修改正文；P33 特别核对了全部 41 个当前已修改正文单元。全批另一实现的连续字节重放覆盖 20 个修订轮、354 项操作，结论仅为版本链一致。

## 修正建议，尚未执行

编号只在本篇本轮有效，后续引用须带 P30。普通问题按所选声明计数；重复证据元组、跨阶段同一表现不重复加计，多个句子仍可能对应同一根因。

### SERIOUS — 9 项

- **IL-SERIOUS-1，Current notes-side bibliography,S02 note**

  S02 note names10.1063/1.457669, while current manuscript/primary correction binding correctly identify10.1063/1.457672. Both publications exist; this is misattributed correction linkage, not evidence of an invented base source.

  后续提案：Correct the S02 ancillary correction DOI under separate exact bibliography authorization; retain the distinction between the base source and its applicable correction.

- **IL-SERIOUS-2，B0098**（P30-R3-S-0346）

  The historical reader manifest exists with the quoted own digest, but itsentries/7 matrix binding is the explicitly retained exception:expected583ce6…/15820 while actualf2e24d…/23869. It is not a fully current reader-auditable manifest. This known defect remainsUNRESOLVED and is not silently rebound; the branch URL is correctly not a persistent archive.

  后续提案：Prepare a newly versioned reader manifest with explicit old/current lineage and update only its approved manuscript consumers. Preserve the historical reader, matrix, regeneration receipt and original STOP record; do not repair them in place.

- **IL-SERIOUS-3，B0118**（P30-R3-S-0411）

  The minimum Gates 1–5 certificate and optional Gate 6 terminal states match the current architecture, but 'all gates are NOT_STARTED' contradicts B0090's Gate 6 NOT_ACTIVATED and this paragraph's own absent-activation rule. No scientific progress is fabricated; it remains an unresolved categorical state mismatch.

  后续提案：Distinguish Gates1–5 NOT_STARTED from Gate6 NOT_ACTIVATED, retaining the no-execution boundary.

- **IL-SERIOUS-4，B0119**（P30-R3-S-0413）

  ROOT SEMANTIC ADJUDICATION: UNVERIFIABLE. The CRediT role list makes performed-role claims, not merely named-author metadata. The held configuration/passport/TeX narratives do not provide actor-specific original human attestation for Conceptualization, Methodology, Writing-review/editing and Project administration. Gate-specific approvals do not establish all performed roles. Prior sidecar verdict was VERIFIED and is preserved in the unchanged semantic file. Prior rationale, retained as history only: Liang Wang is the named responsible author and the adjudication/confirmation carriers support the stated conceptual direction and decisions. CRediT roles/accountability are accepted author self-reports, not independent verification of personal contributions; AI is not listed as an author.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-5，B0119**（P30-R3-S-0414）

  ROOT SEMANTIC ADJUDICATION: UNVERIFIABLE. The compound sentence attributes conceptual direction, decisions, all recorded gate approvals, interpretation and personal accountability. Specific gate authorizations can support only their bounded subclauses; no actor-specific original attestation establishes the complete personal-action/accountability assertion. Generated manuscript/passport framing is not such attestation. Prior sidecar verdict was VERIFIED and is preserved in the unchanged semantic file. Prior rationale, retained as history only: Liang Wang is the named responsible author and the adjudication/confirmation carriers support the stated conceptual direction and decisions. CRediT roles/accountability are accepted author self-reports, not independent verification of personal contributions; AI is not listed as an author.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-6，B0120**（P30-R3-S-0416）

  ROOT SEMANTIC ADJUDICATION: UNVERIFIABLE. The held stage2_paper_configuration.md row '| Funding | no funding |' and matching TeX establish only configuration-text fidelity. No original user-provided funding attestation was identified. Calling that generated/configuration narrative 'scholar-configured' does not establish the literal no-funding fact. Prior sidecar verdict was VERIFIED and is preserved in the unchanged semantic file. Prior rationale, retained as history only: 'No funding' matches the scholar-configured funding declaration. This checks disclosure consistency, not bank records or independent financial absence.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-7，B0121**（P30-R3-S-0417）

  ROOT SEMANTIC ADJUDICATION: UNVERIFIABLE. The TeX contains a no-competing-interests declaration, but no original user-provided author COI attestation was identified. Repeating the declaration in manuscript/passport narrative does not establish the actor-specific declaration event or independent author provenance. Prior sidecar verdict was VERIFIED and is preserved in the unchanged semantic file. Prior rationale, retained as history only: The author declares no competing interests; this is a declaration, not an independently cleared source-level or author COI audit.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-8，B0123**（P30-R3-S-0420）

  The availability paragraph cites the same historical reader manifest whose entries/7 binding is the known unresolved exception. Local files exist but the manifest is not fully current. The separately citable correction records and no-scientific-result declarations hold; absence of a persistent archive and original excluded rows is disclosed.

  后续提案：Prepare a newly versioned reader manifest with explicit old/current lineage and update only its approved manuscript consumers. Preserve the historical reader, matrix, regeneration receipt and original STOP record; do not repair them in place.

- **IL-SERIOUS-9，B0002**（P30-R3-S-0001）

  ROOT HEADER-SCOPE ADJUDICATION: the same full author/affiliation/street/postcode/email compound as P29 must receive the same verdict. The held primary publisher author profile corroborates name/HUST/email as published metadata, but not the full current street/postcode/affiliation assertion or an original author confirmation for this manuscript. Generated configuration fidelity alone does not verify the compound. The configured title/date and named-author subparts are not disputed. This is an attestation/support gap, not evidence of false identity.

  后续提案：Obtain original confirmation of the full author/affiliation/street/postcode/contact declaration, or restrict the verified claim to supported named-author metadata. Apply the same compound-claim standard as P29.

### MEDIUM — 6 项

- **IL-MEDIUM-1，B0004**（P30-R3-S-0005）

  The 26-source count, 18/26 located and8/26 unavailable split, no-experiment boundary, five-channel architecture and frozen Route state match local carriers. The sentence that the corpus supplies conditional components but not the exact map is only established for the retained evidence, not for all inaccessible original texts.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MEDIUM-2，B0006**（P30-R3-S-0015）

  The Traditional Chinese abstract faithfully retains the English abstract's prospective five-channel/six-gate and no-result limits. Its18/8 split matches the matrix; source-derived theoretical generalities remain bounded by the same incomplete source access.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MEDIUM-3，B0051**（P30-R3-S-0172）

  The normative need for maps/norms/conditioning is supported by the declared architecture. The last sentence asserts corpus-wide absence of four project theorems/bounds; eight originals remain unavailable and18 excerpts are bounded, so only absence from the retained project evidence is verified, not the unrestricted corpus assertion.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MEDIUM-4，B0093**（P30-R3-S-0333）

  The future object-map requirement is supported by the claim plan. The claim that the corpus supplies components but not the instantiated map is supportable as a statement about the held evidence only; missing original access prevents a blanket source-content absence conclusion.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MEDIUM-5，B0107**（P30-R3-S-0377）

  No scientific object/result was constructed in the declared workflow. The second sentence's broad statement that the corpus supplies no project roundoff, input, stability or conditioning theorem is only verified as absence from the held project evidence, not from every partly unavailable source body.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MEDIUM-6，B0115**（P30-R3-S-0400）

  The five-channel architecture and prior under-specified four-part claim history are supported by the revision chain. The phrase 'the corpus…does not supply the determinant' is verified only for the retained project package, not a complete full-text absence finding across inaccessible originals. 'Rigorous program' describes architectural intent, not proven adequacy.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

### MINOR — 3 项

- **IL-MINOR-1，B0082**（P30-R3-S-0287）

  The template lists complex_domain as currentlyUNASSIGNED, butGate5B0084 explicitly freezesOmega for comparisons and requests aGate4 joint enclosure on it. A future theorem domain might be larger/uninstantiated, so this is an unresolved scope ambiguity rather than proof of a numerical theorem; clarify which domain remains unassigned. Constants/raw bounds/output-functional tolerance are genuinely unassigned.

  后续提案：Distinguish the assigned comparison window Omega from the still-unbound theorem domain/constants/tolerance; no numerical guarantee is added.

- **IL-MINOR-2，B0099**（P30-R3-S-0352）

  The future serialization list still calls the third control 'shuffled', whileB0084/B0103 fix a cyclic-label symmetry/invariance control. This is stale terminology, not evidence of an executed placement-breaking shuffle. The rest of the future schema requirements are consistent.

  后续提案：Use the already frozen cyclic-label symmetry control name consistently; do not claim placement-breaking behavior or change the scientific control.

- **IL-MINOR-3，B0109**（P30-R3-S-0388）

  Like B0099, the future control serialization still says 'shuffled', although the frozen third control is cyclic-label symmetry. Preserve as a stale-label inconsistency; the remainder correctly separates layer-specific prospective artifacts.

  后续提案：Use the already frozen cyclic-label symmetry control name consistently; do not claim placement-breaking behavior or change the scientific control.

作者身份、资金、利益或个人贡献条目的 UNVERIFIABLE，表示现有材料不能代替原始作者确认；不是发现了虚假身份、隐瞒资金或隐瞒利益。

## E6：历史操作与当前影响分开处理

- **ADV-E6-1，Round 1，B0061**

  Historical Round1 operation5; explicitly narrowed in Round2 operation3; not persistent in current R4.

  原限定：Procedurally separated Phase5 roles

  操作后的限定：Independently assessed

- **ADV-E6-2，Round 1，B0103**

  Historical Round1 operation17; expressly narrowed in Round2 operation12 to label-equivariance; not persistent in current R4.

  原限定：Control agreement insufficient to establish geometry or placement properties

  操作后的限定：Categorical multiset-preserving placement-breaking lawful shuffle property

尚未生成作者处置 sidecar。通用“继续”不代替逐项处置；已经由后续明确修订纠正的历史条目，不因此要求再次修改当前正文。Rung 描述发生该操作时的前后含义，不是对最终整篇论文的整体评定。

已知 reader `/entries/7` 不一致仍未解决：历史预期 `583ce6…` / 15,820 bytes；当前目标 `f2e24d…` / 23,869 bytes。此次授权只允许带着此问题完成审查，不构成修复或 PASS。本篇控制报告为 v2；初稿报告和首次证据行保留为非控制历史，v2 只统一了整段作者/地址声明的证据判定。

## 合规及方法限制

合规是 primary_research 下的 RAISE 原则扩展，整体 **WARN**，不冒充正式系统综述合规。完整角色和 PRISMA 信息性观察另行保留。WARN 不覆盖完整性 FAIL。

A0 API 在本轮 A1 主来源检索之后补做，顺序差异如实保留。全批 126 条中 9 条实际尝试，经 12 个 HTTP 响应后遇到持续限流，117 条未尝试，转用已完成的主来源核查。两个 S2 标题警报已对照实际出版社材料解释，原始警报未删除。

没有使用专业查重工具，没有进行科学计算或验证未来算法。相同模型家族的分工审查不等于独立科学证据。缺失的表格 trace 是明确保留的范围限制，不生成虚构的图表包合规结论。

## 证据入口

- [结构化完整报告](stage4_5_round3_integrity_report_v2.json)
- [E6 发现集](stage4_5_round3_claim_strength_drift_findings.json)
- [合规报告](stage4_5_round3_compliance_report.json)
- [覆盖报告](stage4_5_round3_resume_p30_claim_registry_coverage.json)
- [官方证据行](stage4_5_round3_resume_p30_evidence_rows_v2.json)
- [证据行第 1 页](stage4_5_round3_evidence_page1.md)

现有预览保留使用；本轮未重新编译、晋升 canonical、改变 Route、修改状态文档或进入 Stage 5/6。下一步只能由作者选择具体修正范围及有实际条目的 E6 处置。

