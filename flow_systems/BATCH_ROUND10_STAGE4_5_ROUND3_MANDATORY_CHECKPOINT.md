# Round10 · Stage 4.5 Round 3 — 已完成审查，停在强制检查点

本轮完整审查已完成。**五篇均为 FAIL，没有获得进入下一阶段的完整性许可。** 这是证据支持、表述一致性及作者声明依据的审查结果，不是对故意不端的认定；也没有改变任何 Route 结论。

## 当前结果

| 稿件 | 通过的限定范围声明 / 登记总数 | 证据元组 | E6 条目 | 当前主要问题 |
|---|---:|---:|---:|---|
| [P29](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round3_final_integrity_report.md) | 385 / 389 | 389 | 1 | B0042 对源算法作范围否定缺少支持；整段作者/地址和资金、利益声明依据不足。 |
| [P30](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round3_final_integrity_report.md) | 421 / 438 | 438 | 2 | 参考文献 S02 的更正 DOI 注记错误；旧 reader 仍被当作当前可恢复清单；Gate6 状态及控制名称不一致。 |
| [P31](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round3_final_integrity_report.md) | 402 / 408 | 413 | 1 | “完整的八条声明”“最严格检查”缺少当前依据；I 与 I_diag 指代冲突。 |
| [P32](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round3_final_integrity_report.md) | 459 / 465 | 486 | 1 | 定义与项目实现依赖的措辞需区分；远程字节复核未完成；资金、利益声明待原始确认。 |
| [P33](papers/33-bolza-control-matched-census/notes/stage4_5_round3_final_integrity_report.md) | 395 / 403 | 480 | 0 | 结论把方案称为文献支持的架构，超过现有材料；夹具标识/类型及个人贡献声明有问题。 |

合计 2,103 条当前登记声明、2,206 个证据元组，所有登记条目均已审查。普通修正项 42 条（SERIOUS 25、MEDIUM 9、MINOR 8），按声明项而非独立根因计数；同一根因可能出现在不同句子。E6 的 5 条记录另计，不把它们混入普通完整性问题数。

## 已通过的验证，及其边界

- 五篇官方 bundle、覆盖构建/重放、证据行构建/重放、报告内证据行重放、Schema 12 合规格式及首屏分页渲染均通过。
- 另一实现独立重放了 20 个连续修订轮的全部 354 项操作；结果是字节链一致，不是独立科学验证。
- 有限词法候选共 54 个，未登记候选为 0；语义提取完整性仍为 `not_machine_detectable`。
- 最终复核 375 项锁定文件绑定和 15 个科学目录，未发现新增变化。现有 87 页预览保留，没有重新编译。

文献身份、引用的段落支持、数学正确性和可重复性始终分开。原文不可得时，仅有元数据或阅读任务用途的引用没有被升级为定理支持。合规结果均为理论研究下的 RAISE 原则扩展 WARN，不覆盖完整性 FAIL。

A0 API 是本轮 A1 之后的补充，顺序差异未隐去。实际对 9 条文献进行了 12 次 HTTP 调用，持续限流后停止，其余 117 条未调用；本轮主来源核查覆盖全部 126 条。两个自动标题警报有出版社材料解释，原始警报保留。P32 远程读取在 TLS 阶段失败，未获得响应正文，不声称完成了新的远程 hash 比较。

## P30 已知 reader 问题仍未解决

原 reader 的 `/entries/7` 对同一 matrix 路径预期 SHA-256 `583ce6…`、15,820 bytes；当前文件是 `f2e24d…`、23,869 bytes。此次授权只豁免针对这一已知不一致重复停工，**没有修复它，也没有将其视为 PASS**。旧 reader、旧 STOP、matrix 再生成记录保持原样。

后续若修复，应另建版本化 reader，明确历史/当前血缘并同步获得批准的正文消费者；不应在原 reader 或旧证据上就地抹掉问题。

## E6：需要区分历史已纠正与当前限定

- P29：1 条历史“程序分离 → 独立评估”漂移，后续正文已明确收窄。
- P30：2 条历史漂移，涉及评审独立性和 shuffle 的 placement-breaking 属性，后续正文已有明确收窄。
- P31：1 条 `any claim → every claim` 的免责声明削弱，当前仍保留。
- P32：1 条精确段落核验免责声明删除；当前另一处保留保护性说明，必须同时记录这个缓解因素。
- P33：0 条，**无需 E6 逐项处置**；仍须处理普通完整性问题。

历史操作记录不等于当前论文整体失去限定。已纠正的历史条目也不自动要求再次修改正文。本轮没有代作者创建任何 E6 处置；若要继续，需要对实际存在的条目作明确逐项选择，通用“继续”不能替代它。

## 建议的后续范围，尚未授权执行

1. 补充作者对完整作者/地址信息、资金、利益和所声称个人贡献的原始明确确认；没有确认的条目应提出收窄措辞，不拿生成的配置替代人类声明。
2. 仅针对列出的文献范围否定、比较性最高级、状态/名称和夹具描述，准备精确修正提案；P30 的更正 DOI 注记和版本化 reader 单独处理。
3. 对 5 条 E6 记录逐项处置，明确哪些历史条目已经由后续修订纠正，以及当前限定的处理。
4. 只有新的精确修正范围获授权并实施后，再绑定新输入做相应验证。本轮不启动该阶段。

## 控制文件

- [结构化完成报告](BATCH_ROUND10_STAGE4_5_ROUND3_COMPLETION_REPORT.json)
- [全部修正提案及 E6 记录](BATCH_ROUND10_STAGE4_5_ROUND3_CORRECTION_PROPOSALS.json)
- [报告交接核对](BATCH_ROUND10_STAGE4_5_ROUND3_REPORT_HANDOFF_VALIDATION.json)
- [官方报告证据行重放](BATCH_ROUND10_STAGE4_5_ROUND3_REPORT_OFFICIAL_EVR_VALIDATION.json)
- [受保护边界检查](BATCH_ROUND10_STAGE4_5_ROUND3_CLOSEOUT_BOUNDARY_CHECK.json)

P30 当前控制报告为 `stage4_5_round3_integrity_report_v2.json`，P33 当前控制声明登记为 `claim_registry_v2.json`；旧版保留但不作为当前计数。P32 使用 `A_B_semantic_final.json`，初步说明文字错误也保留了更正说明。

按 ARS academic-research-suite 的 final-check 强制检查点及本轮授权边界，现在停止。未修改正文、参考文献、source matrix、reader、历史 passport、科学代码/实验/结果、canonical、README/状态或 Git；未进入 Stage 5/6。

