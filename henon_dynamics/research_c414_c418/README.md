# C414–C418：研究合同检查点，尚未完成五篇交付

本目录保存用户在 C409–C413 完成交付后，以“确认，下一轮”授权的
新批次研究。它不是五篇论文包，不是新的 Route A 正式评价，也不进入
C419。当前准入以 [协调者裁决](ADMISSION_DECISIONS.md) 为准；作者
选题报告和证明中的“待审”字样保留其交接时状态，不覆盖后来的审查。

## 当前成果与缺口

当前有 **3 项已准入合同**，其非作者全证明／来源审查、实际修订的
复核及所需证书收据均已闭合。四条研究线最初共筛选 12 个合同，
最终只有 3/5 达到准入门槛，仍缺 2 项独立且有实质分量的合同。
目前 **0 篇 LaTeX 新稿、0 个论文 PDF、0 份新正式评价**。

| 研究合同 | 完整结果与精确边界 | 证据入口 |
|---|---|---|
| 常系数 Hénon 的多项式点高度分布 | 所有有限域、所有次数至少二的常系数多项式和非零行列式参数；在 `F_q[t]^2` 上穷尽高度分布、完整聚合极点及自然边界。不是全部 `F_q(t)^2`，不是普通周期 zeta。 | [证明](spectral/HEIGHT_PROOF_PACKAGE.md)、[独立全审](arithmetic/REVIEW_HEIGHT_PROOF.md)、[来源](spectral/HEIGHT_SOURCE_AUDIT.md) |
| 正特征次数 `2p` 共振族 | 所有奇素数 `p`、`q=p^e, e>=3` 及完整次数 `2p` 系数空间；完备化环中的混合尾项不变量闭合全部迭代的普通几何点计数。固定时钟是 `H^(-1)Phi_q`。 | [证明](positive_characteristic/FULL_DEGREE_2P_PROOF.md)、[独立全审](arithmetic/REVIEW_CHARP_PROOF.md)、[来源](positive_characteristic/SOURCE_AUDIT.md) |
| 离散正弦 Hénon 全奇数度周期图 | 原文精确定义的全部奇数次数、全 `Q^2`、普通时钟；全边界首次返回、穷尽逃逸分支和全部本原周期数。正相位内部表与增长周期存在均扣除原文已有结果。 | [证明](nonlinear_geometry/PROOF_PACKAGE.md)、[协调者全审](REVIEW_GEOMETRY_ROOT.md)、[证书独立审查](positive_characteristic/REVIEW_GEOMETRY_CERTIFICATE.md)、[来源](nonlinear_geometry/SOURCE_AUDIT.md) |

上述结果来自 AI 辅助推导与当前团队非作者内部审查，不是人类同行评议
或全球新颖性保证。来源访问限制逐项保留；正确性不由文件哈希证明。

## 为什么不把其余材料补成第四、第五篇

全 `SL_2(Z)` 返回观测的兼容共轭结果通过数学核查，但扣除已有 census、
局部线性分类和一般 orbit-tree 输入后，其剩余短论证及直接算子推论
不足以单独计篇，保留为 [伴随札记](arithmetic/CONGRUENCE_CONJUGACY_PROOF.md)
及 [实质性裁决](REVIEW_ARITHMETIC_ROOT.md)。正特征的严格间隔引理、
次数六前驱、纯 Frobenius 分支和自然边界推论也不拆分计篇。

其余候选分别受精确反例、未闭合的全周期/全参数引理，或已有机制
碰撞限制；见四份 [算术](arithmetic/SCOUT_REPORT.md)、
[正特征](positive_characteristic/SCOUT_REPORT.md)、
[非线性几何](nonlinear_geometry/SCOUT_REPORT.md)、
[谱与解析](spectral/SCOUT_REPORT.md) 记录。未证明的问题并未被宣称为
不可能问题；本轮有界搜索也不是“以后再无可做方向”的结论。

[独立缺额复核](arithmetic/REVIEW_BATCH_SHORTFALL.md) 逐项检查了全部
12 个候选及可能重复计篇的入口，没有发现现成却被遗漏的第四或
第五项。该报告写成时几何项尚待裁决；其后唯一变化是几何项通过，
最终准入为 3 项，而不是把剩余两个缺额也宣称补齐。

## 验证范围与下一步

典范高度的 77,974 个多项式点诊断、精确正特征反例，以及全自由参数
几何证书分别针对其具体风险；有限诊断不代替无限参数证明，几何
证书的自动核验范围也不扩写为自动证明全部逃逸路线。最终实际收据
和保存核验见 [检查点记录](CHECKPOINT_RECORD.md)。

`henon-route-a-batch` 的选五项合同门槛尚未满足，故暂停在选题检查点，
没有为凑数进入五篇写作、正式评价、PDF 构建或 C 编号注册。
三个源系统结果均不建立目标 Euler 因子、根数、自守性、零点/除子对应
或 Hilbert–Pólya 实现。没有目标 A1/A2 突破，也不伪造未测指标。

续接应仍补 **同一 C414–C418 批次**的实质合同缺额，保留已核通过的
结果和来源限制；在五项合同成立后，再冻结正式论文计划并完成写作、
逐篇审查、严格评价及可复现 PDF 交付。未经新的相关证据，不重跑旧
证明或改号复活已经扣除的伴随札记。

本检查点封存后不修改目录内原文件；续接在新的未封存目录记录增量，
链接这里的已核输入。精确 payload 成员清单和自排除校验清单将在
所有最终审查归档后生成；实际完成情况以检查点记录和 Git 对象为准。
