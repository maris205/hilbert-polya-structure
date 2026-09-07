# C414–C418：五篇完整论文与证据入口

本批完成五项独立、实质性的来源系统研究合同，现有 **五篇完整英文
论文、61 页最终 PDF**。完整证明／来源准入、非作者实际稿件审查、
修订闭环、每篇两次全新确定性构建与全部最终页面目视均已完成。
当前团队审查是 AI 辅助内部审查，不是人类同行评审或全球首创证明。

最终封存以本包 [精确成员账本](PAYLOAD_LEDGER.json)、
[自排除摘要清单](MANIFEST.sha256) 及包外
[当前状态中的实际核验／Git 收据](../CURRENT_RESEARCH_STATE.md) 为准。
该包外记录在真正封存与同步后更新，避免清单内自指摘要或预填提交号。
本文件的完成口径是五篇论文与已记录研究／构建门槛，不代替实际 Git refs。

## 五篇最终 PDF 与各自增量

| 论文 | 页数 | 完整问题与实际增量 |
|---|---:|---|
| [C414：常系数 Hénon 的典范高度分布](papers/C414_height_distribution/main.pdf) | 9 | 对任意有限常数域、任意次数至少二及全部允许系数，确定所有多项式点的系数无关高度分布、合并后的全部极点与重数、亚纯自然边界及保留实数高度取整振荡的计数主项。对象是高度 Dirichlet 级数，不是周期轨道 zeta。 |
| [C415：次数 2p 的 Hénon–Frobenius 共振](papers/C415_degree_2p/main.pdf) | 11 | 对所有奇素数 p、q=p^e 且 e≥3、全部次数 2p 修正多项式，给出高／低支撑两分支的完整普通几何不动点公式；低支撑的半线性完美化尾项与下降封闭了此前缺口，自然边界为该公式的推论。 |
| [C416：离散正弦族的全部有理周期](papers/C416_discrete_sine/main.pdf) | 15 | 对每个奇数度 d≥3，精确裁剪全部核心单元并穷尽带符号的边界返回与逃逸，确定所有普通周期、重数和总点数，包含最小半径与增长周期的唯一性。已知核心分类及增长周期存在性明确扣除。 |
| [C417：首一整系数保守三次族的有理周期](papers/C417_integral_cubic/main.pdf) | 17 | 对全部首一整系数三次多项式，给出七类周期模板、全局共存周期集的尖锐十一点上界及完整等号族；无界参数归约与有限补集证书均排入正文／附录。 |
| [C418：非恒定二次函数域参数的有理周期集](papers/C418_function_field/main.pdf) | 9 | 对特征非二的任意常数域、非零常数行列式和全部非恒定多项式参数，给出七行完整周期图谱、所有特征碰撞及尖锐十四点例外；特征非二、三时再区分 −1 为平方与否的八／六点界。 |

每个论文目录都保留可编辑 TeX／Bib、引文审计、作者交付历史、
非作者实际稿件审查、最终 PDF 和真实构建日志。完整证明位于论文中；
研究证明文件和精确检查用于补充追溯，不以只有提纲或代码的包充数。

## 准入、审查与复现

- [本轮准入裁决](ADMISSION_DECISIONS.md)、[冻结的五篇写作计划](BATCH_PLAN.md)
  和[独立大纲审查](REVIEW_OUTLINE.md) 区分五项问题，没有拆分推论计篇。
- [实际稿件审查裁决](REVIEW_ADJUDICATION.md) 汇总五篇闭合结果。
  C415 唯一必改项已将“有限环”的歧义改为“每次计算为有限表达式”，
  原审者核对了修订源码和更新 PDF；其余四篇无需稿件修订。
- [最终构建总报告](FINAL_BUILD_REPORT.md) 与各篇逐页收据记录十次
  全新构建、61 页实际目视及协调者对 55 个输入、110 份源副本和
  五组 PDF 的独立字节核对。[源摘要](FINAL_SOURCE_SHA256SUMS) 固定最终输入。
  C417 一次额外引用稳定化保留了原始警告日志，未改变 PDF 字节或源码。
- [发布工具说明](release/README.md)、[实际测试收据](release/TEST_REPORT.md)
  和[非作者代码审查](release/REVIEW_CODE.md) 说明精确成员、外部批准账本摘要、
  非覆盖封存及篡改测试的边界。摘要一致性不是数学正确性或真实性证明。

前三项研究输入沿用已封存的
[原研究快照](../research_c414_c418/README.md)，不改旧清单、不重跑已通过
检查以重复 PASS。新增三次族与函数域证明分别在
[三次证明／独立审查](cubic_arithmetic/REVIEW_CUBIC_ROOT.md) 和
[函数域证明／独立审查](function_field/REVIEW_SOURCE_AND_REDUCTION.md)。
三次有限补集另经协调者独立算法重建；函数域的精确检查保留其
[真实运行收据](function_field/EXACT_CHECK_RECEIPT.md)。有限诊断不代替无穷参数证明。

## 严格 Route A 结论

评价使用未修改的 v0.2.0，精确来源／时钟和阅读范围见
[EVALUATION_SCOPE.md](EVALUATION_SCOPE.md)，一致性审查见
[REVIEW_EVALUATION.md](REVIEW_EVALUATION.md)。

| 论文 | A0 | A1 | A2 / A3 / A4 | 完整评价 |
|---|---|---|---|---|
| C414 | WEAK_ARITHMETIC_RELATION | FAIL：所选高度观测不是周期分类 | FAIL / FAIL / FAIL | [YAML](evaluations/route_a/HCS-C414/2026-09-07.yaml) |
| C415 | WEAK_ARITHMETIC_RELATION | WEAK：来源计数完整，目标桥缺失 | FAIL / FAIL / FAIL | [YAML](evaluations/route_a/HCS-C415/2026-09-07.yaml) |
| C416 | WEAK_ARITHMETIC_RELATION | WEAK：来源周期完整，目标桥缺失 | FAIL / FAIL / FAIL | [YAML](evaluations/route_a/HCS-C416/2026-09-07.yaml) |
| C417 | WEAK_ARITHMETIC_RELATION | WEAK：来源周期完整，目标桥缺失 | FAIL / FAIL / FAIL | [YAML](evaluations/route_a/HCS-C417/2026-09-07.yaml) |
| C418 | WEAK_ARITHMETIC_RELATION | WEAK：来源周期完整，目标桥缺失 | FAIL / FAIL / FAIL | [YAML](evaluations/route_a/HCS-C418/2026-09-07.yaml) |

五篇均为来源范围内的 **ROUTE_A_EXPLORATORY**，不是目标 A1/A2 突破。
A0 必需对照面板仍 INCOMPLETE；全部 45 项 A2 指标为 NOT_TESTABLE，
不是数值零误差。未提供目标行列式／零点对照，不把相应资格 FAIL
误说为某个尚未定义模型的数值反证。所有目标局部数据、Euler 因子、
根数、自守性、函数方程、零点／除子、Hilbert–Pólya 与 Route B 标志均为 false。
`NO_BAD_EULER_OR_ROOT_NUMBER` 持续有效。

## 未入选五篇的工作与停止点

本续接还保存 [正字映射类研究储备](mapping_class/CHECK_RECEIPT.md)、
[前向正特征候选边界](forward_charp/SCOUT_REPORT.md) 和
[双 Frobenius 时钟候选边界](frobenius_clocks/SCOUT_REPORT.md)。
映射类储备未完成独立准入，其他候选不满足本批新增独立问题门槛；
它们都不编号、不计第六篇。作者检查日志中的历史 pending 状态
由明确链接的后续闭合记录承接，不篡改早期收据。

授权止于 **C414–C418 五篇检查点**。不开始 C419，不进入 Route B，
不投稿、不向第三方上传论文、不发布外部公告。下一批须等待用户确认。
