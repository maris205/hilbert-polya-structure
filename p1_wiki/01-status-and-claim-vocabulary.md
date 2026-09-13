# 状态与 claim 词汇：避免把文档流程当作数学结论

[P1 Wiki 首页](README.md) · [Agent 起始页](00-agent-start.md) · [六条方向](directions/index.md)

## 四个必须分开的层次

| 层次 | 它回答什么 | 不等于什么 |
|---|---|---|
| **来源身份** | 文件来自哪个项目、提交、锁定输入或导入档案？ | 数学正确性或独立复核 |
| **文档 / 流程状态** | 是否完成构建、冻结、审计、交付或私有同步？ | Route 通过、可发表性或 RH 证明 |
| **局部数学结论** | 一个具体对象上究竟证明或反驳了什么？ | 全局 zeta / Riemann-zero 结论 |
| **路线评估** | 针对受类型约束的候选对象，哪些 Gate / Route obligation 被检查？ | 另一对象、另一方向或整个计划的通行证 |

“PDF 存在”“测试通过”“pipeline completed”“最终稿已发出”只在各自层次内有意义。它们不会自行建立 prime-power trace、完成 ξ 行列式、自伴算子、Riemann-zero 对应或 RH。

## 本库使用的状态词

| 词汇 | 在本库中的保守读法 |
|---|---|
| `PROVED` / `PASS` | 只指来源中明确命名的对象、命题和适用范围；需回到原文检查。 |
| `ROUTE_A_EXPLORATORY` | 探索性 Route-A 记录；不是 Hilbert--Pólya 成功。 |
| `GO_WITH_LIMITATIONS` | 仅在记录的限制和下一步门槛下可继续理解；不是全局肯定。 |
| `ROUTE_A_REJECTED` / `FAIL` | 该受类型对象或代理对象未通过所列义务；不自动否定不同对象。 |
| `UNASSIGNED` | 没有为完整候选分配可比较的 Route tuple；不可偷借 proxy 的 credit。 |
| `NOT_APPLICABLE` | 该材料不是用对应 Route-A/B schema 评价的对象；不是 PASS，也不是科学失败。 |
| `NOT_TESTABLE` | 证据或对象不足以对该条件作出测试性裁决；不是未知的正证据。 |
| `HOLD_EXTERNAL` / `STOP_SCOPED` | 流程或范围受到明确停止限制；不能据此启动下一论文、对外发布或拓展声明。 |
| `completed` | 指记录的流水线阶段已结束；需区分“实验、文档、构建”与“科学 Gate”。 |

## Route A / Route B 的准确使用

Flow Systems 的正式方案把 Route A 的问题分为：算术相关性（A0）、原始/可复现周期轨道所有权（A1）、稳定动力学 zeta 或 Fredholm 行列式（A2）、全局解析 / Weil 压缩结构（A3）、自然的经典到量子提升（A4）。只有满足该方向源材料规定的进入条件，Route B 才讨论完整算子、自伴性、谱型、精确 prime-power trace / Weil 相容性和全局 completed-ξ determinant/divisor equality。

这是一套**对象和证据依赖的评价协议**，不是六条路线可自由借用的勋章。特别是：

- Flow P24--P28 的 Stage 5 交付完成不产生新的 A--E credit；该批次正向算术 A2 为 `0/5`，Route B invocation 为 `0/5`。
- Symplectic Batch07 的 `route_applicability: NOT_APPLICABLE` 不能写成 Route PASS。
- Symbolic P211--P215 的内部完成也不会自动转换为旧 Hilbert--Pólya A0--A4 或 Route B 进展。
- zeta_mvp0 的局部 `P^*_{loc}` 不是开放的 `P0`，更不是 Z 或 RH 许可。

各方向的具体适用词义以自己的[结论页](directions/index.md)和原始评估为准。

## 原始文本与派生阅读副本

`p1_wiki` 的 `fulltext.md` 是对受选 TeX 主文稿的机器派生 Markdown，用于检索和快速阅读。它可能无法无损表达所有 LaTeX 宏、交叉引用、图、表、证明环境或参考文献格式。因此：

1. 源卡中的路径、哈希和转换状态是阅读副本的 provenance；
2. 需要精确数学陈述、页码、图表、引用或构建复现时，应回到原始 `.tex`、PDF、`.bib` 和包内 README；
3. 导入档案、冻结 source lock、receipt、ledger 和评估 YAML 不因转换而改变字节、身份或证据等级。

## 一条全局非主张

截至本知识库所编排的材料，不能把任一 Session 或它们的并列阅读解释成已证明 Riemann Hypothesis、已构造满足要求的自伴 Hilbert--Pólya 算子、已得到内生 von Mangoldt prime-power trace、已完成 completed-ξ determinant equality，或已建立 Riemann zeros 的谱识别。每一方向可能有有价值的局部定理、否定性校准、构造性接口或流程证据；它们的精确范围只在原始材料中成立。
