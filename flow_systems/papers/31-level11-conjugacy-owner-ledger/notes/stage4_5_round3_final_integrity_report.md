# P31 — Stage 4.5 Round 3 最终完整性报告

结论：**FAIL，停在强制检查点**。本报告针对 [当前审查稿](stage4_prime_revision_round4.tex)，没有修改正文、参考文献或科学材料。FAIL 表示存在未解决的证据支持、表述或作者声明依据缺口，不是对故意不端的认定，也不是新的 Route 判定。

## 范围与结果

| 核查 | 当前结果 | 边界 |
|---|---|---|
| A 文献字段 | 24/24 条通过，0 条错误 | 不等于全文、定理适用性或撤稿全筛查 |
| B 引用语境 | 26/26 个当前源使用语境有相应层级支持 | 包含明确的元数据/阅读任务用途，不升级为定理支持 |
| C 数据与记录 | 6/8 个核查分组与所述范围一致 | 分组不是实验样本 |
| D 原创性筛查 | 84/84 个声明的正文段落单元 | 引号检索加非引号补充；非专业查重或全网保证 |
| E 当前登记声明 | 402/408 条在限定范围获验证 | 所有登记声明均审查；语义提取完整性不可由机器证明 |
| E 证据行 | 413 个所选元组 | 官方构建、重放及报告内重放均通过 |
| E6 连续修订 | 52 项操作，1 条漂移记录 | 单独列示，不混入普通问题数 |

E 分类：VERIFIED 402；MINOR_DISTORTION 1；MAJOR_DISTORTION 0；UNVERIFIABLE 5；UNVERIFIABLE_ACCESS 0。

有限词法覆盖检查未登记候选为 0，但不能据此声称机器穷尽了所有实质声明。原创性审查覆盖声明范围内所有当前已修改正文；P33 特别核对了全部 41 个当前已修改正文单元。全批另一实现的连续字节重放覆盖 20 个修订轮、354 项操作，结论仅为版本链一致。

## 修正建议，尚未执行

编号只在本篇本轮有效，后续引用须带 P31。普通问题按所选声明计数；重复证据元组、跨阶段同一表现不重复加计，多个句子仍可能对应同一根因。

### SERIOUS — 5 项

- **IL-SERIOUS-1，B0042**（P31-R3-B0042-003）

  Revision1 is a dated historical scope, and the Phase6 manifest has eight entries. Eight cannot establish completeness of current semantic extraction: source-status, metadata, workflow, and design-assertion sentences extend beyond that inventory.

  后续提案：Describe the eight-entry historical ClaimIntent inventory as historical, not the complete current semantic claim population.

- **IL-SERIOUS-2，B0065**（P31-R3-B0065-003）

  No comparison metric, complete alternative fixture inventory, or evidence proves the superlative; current B0061/B0062 explicitly omit self/reversal/triple/independent semantic coverage. The valid9453 arithmetic is unaffected.

  后续提案：Narrow the unsupported superlative to the declared 9453 unordered-distinct-pair regression audit, retaining omitted-case and no-independent-semantic-oracle limits.

- **IL-SERIOUS-3，B0083**（P31-R3-B0083-004）

  No comparison metric, complete alternative fixture inventory, or evidence proves the superlative; current B0061/B0062 explicitly omit self/reversal/triple/independent semantic coverage. The valid9453 arithmetic is unaffected.

  后续提案：Narrow the unsupported superlative to the declared 9453 unordered-distinct-pair regression audit, retaining omitted-case and no-independent-semantic-oracle limits.

- **IL-SERIOUS-4，B0102**（P31-R3-B0102-001）

  Funding and competing-interest statements are retained author declarations, not independently verified financial facts. No conflicting evidence was found in the allowed materials; no external clean screen is implied.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

- **IL-SERIOUS-5，B0103**（P31-R3-B0103-001）

  Funding and competing-interest statements are retained author declarations, not independently verified financial facts. No conflicting evidence was found in the allowed materials; no external clean screen is implied.

  后续提案：Obtain an original, explicit author confirmation for the exact declaration or personal-act scope; otherwise propose narrower wording. A generated configuration/passport or generic stage approval is not the missing attestation. No external financial or employment audit is implied.

### MINOR — 1 项

- **IL-MINOR-1，B0073**（P31-R3-B0073-002）

  First sentence preserves zero-unresolved closure. The following reference to I retaining unresolved diagnostics conflicts with the controlling B0067/B0113 I_diag-only rule. Schema precedence preserves the principal gate but does not remove the inconsistent referent.

  后续提案：Use I_diag for unresolved diagnostic retention; preserve the zero-unresolved closure requirement for I.

作者身份、资金、利益或个人贡献条目的 UNVERIFIABLE，表示现有材料不能代替原始作者确认；不是发现了虚假身份、隐瞒资金或隐瞒利益。

## E6：历史操作与当前影响分开处理

- **ADV-E6-1，Round 3，B0108**

  Round3 operation13; current Round4 B0108 retains any→every weakening; this is a disclaimer-scope change, not evidence that personal reading occurred.

  原限定：No implication of personal verification of any claim

  操作后的限定：No implication only of verification of every claim

尚未生成作者处置 sidecar。通用“继续”不代替逐项处置；已经由后续明确修订纠正的历史条目，不因此要求再次修改当前正文。Rung 描述发生该操作时的前后含义，不是对最终整篇论文的整体评定。

## 合规及方法限制

合规是 primary_research 下的 RAISE 原则扩展，整体 **WARN**，不冒充正式系统综述合规。完整角色和 PRISMA 信息性观察另行保留。WARN 不覆盖完整性 FAIL。

A0 API 在本轮 A1 主来源检索之后补做，顺序差异如实保留。全批 126 条中 9 条实际尝试，经 12 个 HTTP 响应后遇到持续限流，117 条未尝试，转用已完成的主来源核查。两个 S2 标题警报已对照实际出版社材料解释，原始警报未删除。

没有使用专业查重工具，没有进行科学计算或验证未来算法。相同模型家族的分工审查不等于独立科学证据。缺失的表格 trace 是明确保留的范围限制，不生成虚构的图表包合规结论。

## 证据入口

- [结构化完整报告](stage4_5_round3_integrity_report.json)
- [E6 发现集](stage4_5_round3_claim_strength_drift_findings.json)
- [合规报告](stage4_5_round3_compliance_report.json)
- [覆盖报告](stage4_5_round3_resume_p31_claim_registry_coverage.json)
- [官方证据行](stage4_5_round3_resume_p31_evidence_rows.json)
- [证据行第 1 页](stage4_5_round3_evidence_page1.md)

现有预览保留使用；本轮未重新编译、晋升 canonical、改变 Route、修改状态文档或进入 Stage 5/6。下一步只能由作者选择具体修正范围及有实际条目的 E6 处置。

