# C404–C408：五篇完成，新增 C407/C408

2026-09-06。用户“继续”所授权的两项缺额已补齐：**五篇完整研究稿，
共 58 页**。本次新增 25 页；C404–C406 的 179 个封存文件保持原字节，
不重写、不重跑、不重复计算为新成果。未开始 C409。

## 五个 PDF 与独立问题

| 编号 | 正文 PDF | 页数 | 完整源结果 |
|---|---|---:|---|
| C404 | [非线性 Hénon–Frobenius 共振计数](../continuation_c404_c408_round2/henon_resonance/paper/main.pdf) | 10 | 全周期、全 p-幂塔的普通点数与同一 zeta 的自然边界。 |
| C405 | [临界整除 Gram 的奇异型与极限](../continuation_c404_c408_round2/arithmetic_forms/paper/main.pdf) | 10 | 临界系数的可求和二分、最大可闭下界及正逼近的强预解式极限。 |
| C406 | [调和 δ 链的临界第二 Weyl 系数](../continuation_c404_c408_round2/critical_delta/paper/main.pdf) | 13 | 完整渐近耦合类的两项计数律、第二系数及硬／软端点。 |
| C407 | [有限 adelic 失真的 Cantor 聚点集](arithmetic_candidate/paper/main.pdf) | 13 | 正熵 hyperbolic FAD 系统：无 active prime 时有限；任意有限正数个 active primes（含野性项）时整个原生轨道计数聚点集为 Cantor 集，上盒维为零，并有多对数覆盖界。 |
| C408 | [循环交换关系的交替零点厚度](cluster_boundary/paper/main.pdf) | 12 | 所有奇 k>=3、全部 n=2m 的未饱和循环关系：交替零点局部交长的完整公式，含两类共振与显式有理重数生成函数。 |

[五项冻结合同](BATCH_PLAN.md) 给出精确对象、量词、observable、经典
输入和独立增量。生成函数、端点和三类实际算例均归所属主定理，
没有拆作额外论文。原三篇的证明、审查及 33 页构建证据见
[原交付包](../continuation_c404_c408_round2/README.md)，其历史缺额
陈述由本次完成记录续接，不回写历史。

## 新增两篇的实质与来源界线

C407 的新证明是自适应 valuation-tree 覆盖，以及正权有限类型径向
核的 Fourier 非消去，进而在每个 cylinder 排除局部常值。动力学
detector 渐近式、单素数先前结果、负整数切片技巧与固定点实现均
明确归于原来源。精确范围见 [合同](arithmetic_candidate/CONTRACT.md)、
[完整证明](arithmetic_candidate/PROOF_PACKAGE.md)、
[来源审计](arithmetic_candidate/SOURCE_AUDIT.md)。结果覆盖所核读
BCH 2024 公开 v2 明确留下的 hyperbolic 多素数／野性 regimes；
2026 引文所列 EMS 最终书稿未取得，**不作全球优先权保证**。
不包含一般 nonhyperbolic 情形、单射性或 Haar 推前无原子性。

C408 扣除已知 deep support 分类，新增的是所有 m、所有奇 k 的
非约化厚度及共振系数。它研究**未饱和有限循环关系代数**，不把
边界局部长度称为普通 torus 周期点数，也不把该局部概形等同于
光滑 cluster surface 的固定点概形。见 [完整证明](cluster_boundary/PROOF_PACKAGE.md)、
[来源审计](cluster_boundary/SOURCE_AUDIT.md) 与
[独立证明／范围核查](ROOT_CLUSTER_REVIEW.md)。偶 k、其它零模式
和完整 torus 总计数没有被悄悄纳入合同。

## 实际审查、构建与严格评价

两篇实际正文分别完成 [C407 非作者全文与引文审查](reviews/C407_MANUSCRIPT_REVIEW.md)
和 [C408 非作者全文与引文审查](reviews/C408_MANUSCRIPT_REVIEW.md)，
必须修订项已定点关闭。每稿在两个新空目录独立编译，两份 PDF
及经审查初稿逐对同字节；全部 25 页实际逐页查看，字体全部嵌入，
无未解析引用或最终排版告警。版本、原始日志、输入及 PDF 摘要见
[最终构建收据](FINAL_BUILD_REPORT.md)。

C407 保持源机制 `ROUTE_A_EXPLORATORY`，C408 为目标
`ROUTE_A_REJECTED`。加原三篇，五篇目标 A2/A3 **全部 FAIL**；新增
两份的 18 项目标指标为 NOT_TESTABLE、18 项 scope flags 为 false，
三类强制算术对照 INCOMPLETE。精确 tuple 和未做项见
[评价范围](EVALUATION_SCOPE.md) 与 [独立一致性审查](reviews/EVALUATION_BOUNDARY_REVIEW.md)。
这些是源问题论文，不是目标零点对应或 Hilbert–Pólya 实现，保持
`NO_BAD_EULER_OR_ROOT_NUMBER`，没有 Route-B 晋级。

当前 AI 团队审查是内部检查，不等于人类同行评审或期刊录用。
实际作者身份、贡献、资助与利益冲突须在投稿前由责任作者确认；
本轮没有向第三方上传稿件。`paper-plan`、`paper-write`、
`paper-compile` 的要求落实为完整论证、实际引文核验、定点修订及
可追溯构建。本地 `henon-route-a-batch` 的实质准入要求使下述短
札记不计篇；ARS 的相关来源／诚信规则用于归属与版本缺口，不
冒称完整十阶段认证，不套用旧 ML/GPU/固定模型配额。

## 未计篇材料

[野性普通计数札记](wild_ordinary/SCOUT_REPORT.md) 找到 p=3、最小
周期 12、首返重数 12 而非 3 的点；协调者用独立
[h-adic 精确计算](ROOT_WILD_CHECK.md) 核验。它反驳原始权重恒为一
的猜想，不是全部普通计数公式的 no-go；其有限域推广保留研究记录，
不编号、不补第六篇。另有 [双素数张量谱筛选](spectral_candidates/SCOUT_REPORT.md)，
因剩余增量仅是已知谱的短推论而未准入。

## 封存与同步范围

本目录全部实际文件构成新封存树。[payload ledger](PAYLOAD_FILES.txt)
只排除自身与 [manifest](MANIFEST.sha256)；manifest 包含 ledger、
只排除自身。最终只读核验要求摘要与精确成员集合都一致，无重复、
遗漏、额外文件、符号链接或特殊文件。未新增发布程序或虚构篡改测试。
[独立交付链接审计](reviews/RELEASE_LINK_AUDIT.md) 只核查本地链接
和实际 PDF 数据，不冒称外部 URL、数学或旧稿的重新审查。

共享 CURRENT、两份注册表、旧封存包、外部来源和固定 evaluator
不在此载荷树内，分别由 Git、原清单和来源记录约束。实际封存核验
及 Git 同步结果见 [当前入口](../CURRENT_RESEARCH_STATE.md)；不将
自身提交号循环写入载荷。八个继承未跟踪目录继续保留且不暂存。
本批完成于 C408，等待下一轮明确授权。
