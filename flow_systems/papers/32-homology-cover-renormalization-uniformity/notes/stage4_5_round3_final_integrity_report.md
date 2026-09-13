# P32 — Stage 4.5 Round 3 最终完整性报告

结论：**FAIL，停在强制检查点**。本报告针对 [当前审查稿](stage4_prime_revision_round4.tex)，没有修改正文、参考文献或科学材料。FAIL 表示存在未解决的证据支持、表述或作者声明依据缺口，不是对故意不端的认定，也不是新的 Route 判定。

## 范围与结果

| 核查 | 当前结果 | 边界 |
|---|---|---|
| A 文献字段 | 30/30 条通过，0 条错误 | 不等于全文、定理适用性或撤稿全筛查 |
| B 引用语境 | 30/30 个当前源使用语境有相应层级支持 | 包含明确的元数据/阅读任务用途，不升级为定理支持 |
| C 数据与记录 | 11/15 个核查分组与所述范围一致 | 分组不是实验样本 |
| D 原创性筛查 | 96/96 个声明的正文段落单元 | 引号检索加非引号补充；非专业查重或全网保证 |
| E 当前登记声明 | 459/465 条在限定范围获验证 | 所有登记声明均审查；语义提取完整性不可由机器证明 |
| E 证据行 | 486 个所选元组 | 官方构建、重放及报告内重放均通过 |
| E6 连续修订 | 52 项操作，1 条漂移记录 | 单独列示，不混入普通问题数 |

E 分类：VERIFIED 459；MINOR_DISTORTION 2；MAJOR_DISTORTION 0；UNVERIFIABLE 2；UNVERIFIABLE_ACCESS 2。

有限词法覆盖检查未登记候选为 0，但不能据此声称机器穷尽了所有实质声明。原创性审查覆盖声明范围内所有当前已修改正文；P33 特别核对了全部 41 个当前已修改正文单元。全批另一实现的连续字节重放覆盖 20 个修订轮、354 项操作，结论仅为版本链一致。

## 修正建议，尚未执行

编号只在本篇本轮有效，后续引用须带 P32。普通问题按所选声明计数；重复证据元组、跨阶段同一表现不重复加计，多个句子仍可能对应同一根因。

### SERIOUS — 2 项

- **IL-SERIOUS-1，B0122**（P32-R3-B0122-001）

  The wording is present in the author-configuration/declaration cargo. Fidelity to that declaration can be checked; no original financial/conflict attestation or independent fact audit is held. Register UNVERIFIABLE for the literal personal-world fact, not falsehood or misconduct.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-2，B0123**（P32-R3-B0123-001）

  The wording is present in the author-configuration/declaration cargo. Fidelity to that declaration can be checked; no original financial/conflict attestation or independent fact audit is held. Register UNVERIFIABLE for the literal personal-world fact, not falsehood or misconduct.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

### MEDIUM — 2 项

- **IL-MEDIUM-1，B0098**（P32-R3-B0098-004）

  All25 local files match this reader inventory;11 are historically marked public and14 local-only. This round made no successful remote byte comparison: the first exact pinned URL failed TLS before response/hash evaluation. The remote byte-identity assertion therefore has UNVERIFIABLE_ACCESS, not an invented mismatch or fresh remote PASS.

  后续提案：Keep remote verification as a dated historical receipt, or authorize a separate current retrieval. Current TLS failure is retained; do not assert a successful fresh byte comparison.

- **IL-MEDIUM-2，B0125**（P32-R3-B0125-003）

  All25 local files match this reader inventory;11 are historically marked public and14 local-only. This round made no successful remote byte comparison: the first exact pinned URL failed TLS before response/hash evaluation. The remote byte-identity assertion therefore has UNVERIFIABLE_ACCESS, not an invented mismatch or fresh remote PASS.

  后续提案：Keep remote verification as a dated historical receipt, or authorize a separate current retrieval. Current TLS failure is retained; do not assert a successful fresh byte comparison.

### MINOR — 2 项

- **IL-MINOR-1，B0034**（P32-R3-B0034-002）

  Narrow abstract/contents fragments do not certify source-wide absences. The transfer restriction is valid as no accepted P32 proof here, but wording about what the works do not establish should not be read as a verified exhaustive negative about their contents.

  后续提案：Narrow the source-wide claim to the actually held, explicitly bounded evidence, or provide the specific original support. Access unavailability is not proof that the full source lacks the result.

- **IL-MINOR-2，B0095**（P32-R3-B0095-002）

  B0134 explicitly says CP-P32-004 is not a definition premise, while this sentence ties unresolved constructions to that checkpoint. Under B0131 only project realization remains open, but the causal wording conflates defined carrier and unproved application; a localized clarification is warranted.

  后续提案：Separate established formal-carrier definitions from the unexecuted project realization/CP-P32-004 dependency.

作者身份、资金、利益或个人贡献条目的 UNVERIFIABLE，表示现有材料不能代替原始作者确认；不是发现了虚假身份、隐瞒资金或隐瞒利益。

## E6：历史操作与当前影响分开处理

- **ADV-E6-1，Round 3，B0128**

  Round3 operation14; current R4 retains the deletion, with protective exact-passage disclaimer elsewhere in B0121. Rungs describe the operation, not the final manuscript as a whole.

  原限定：Approval disclaims both personal full-text reading and any exact-passage claim verification.

  操作后的限定：Approval disclaimer narrowed to full-text reading; exact-passage disclaimer deleted.

尚未生成作者处置 sidecar。通用“继续”不代替逐项处置；已经由后续明确修订纠正的历史条目，不因此要求再次修改当前正文。Rung 描述发生该操作时的前后含义，不是对最终整篇论文的整体评定。

## 合规及方法限制

合规是 primary_research 下的 RAISE 原则扩展，整体 **WARN**，不冒充正式系统综述合规。完整角色和 PRISMA 信息性观察另行保留。WARN 不覆盖完整性 FAIL。

A0 API 在本轮 A1 主来源检索之后补做，顺序差异如实保留。全批 126 条中 9 条实际尝试，经 12 个 HTTP 响应后遇到持续限流，117 条未尝试，转用已完成的主来源核查。两个 S2 标题警报已对照实际出版社材料解释，原始警报未删除。

没有使用专业查重工具，没有进行科学计算或验证未来算法。相同模型家族的分工审查不等于独立科学证据。缺失的表格 trace 是明确保留的范围限制，不生成虚构的图表包合规结论。

## 证据入口

- [结构化完整报告](stage4_5_round3_integrity_report.json)
- [E6 发现集](stage4_5_round3_claim_strength_drift_findings.json)
- [合规报告](stage4_5_round3_compliance_report.json)
- [覆盖报告](stage4_5_round3_resume_p32_claim_registry_coverage.json)
- [官方证据行](stage4_5_round3_resume_p32_evidence_rows.json)
- [证据行第 1 页](stage4_5_round3_evidence_page1.md)

现有预览保留使用；本轮未重新编译、晋升 canonical、改变 Route、修改状态文档或进入 Stage 5/6。下一步只能由作者选择具体修正范围及有实际条目的 E6 处置。

