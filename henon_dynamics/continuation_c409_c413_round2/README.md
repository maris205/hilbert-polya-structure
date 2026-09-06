# C409–C413：五篇完整论文与交付记录

五篇全文及 PDF 已完成，共 **59 页（11/13/11/14/10）**。
五项非作者内部全文／来源审查、实际修订确认、每篇两次全新目录
同字节构建，以及全部 59 页视觉检查均已通过。
论文状态为 `FIVE_COMPLETE_PAPERS`。精确载荷封存与真实 Git
同步收据由批次外的 [当前状态入口](../CURRENT_RESEARCH_STATE.md)
记录，不在自哈希载荷里循环嵌入自身提交号。本轮止于 C413，
不启动第六篇。

本轮接续已冻结的 [四项研究合同检查点](../research_c409_c413/README.md)，
补入独立的整数迹映射合同后，按
[五项实质合同与写作计划](BATCH_PLAN.md) 写成五篇文章。
它们不是五份研究大纲，也没有把未准入札记重新编号凑数。

## 五篇正文及各自增量

| 论文 | 完整 PDF／源文件 | 已证明的独立问题与主要限制 |
|---|---|---|
| C409 — Active fibres and natural boundaries in wild finite-adelic dynamics | [PDF，11 页](papers/C409_wild_fad/main.pdf) · [LaTeX](papers/C409_wild_fad/main.tex) | 有限素数、有限单位模相位和非负周期径向指数下，先聚合抵消，再以有限 active-fibre 判据精确区分有理性与亚纯自然边界；包括真实非双曲 wild FAD 应用。无野分支的经典推论已扣除。 |
| C410 — Wild cubic inverse-image towers in characteristic three | [PDF，13 页](papers/C410_wild_cubic/main.pdf) · [LaTeX](papers/C410_wild_cubic/main.tex) | 任意特征三基域上 `X^3+aX^2`、`a != 0` 的所有 generic 逆像高度：算术／几何群、全局 Kummer/AS 独立、局部秩一、分歧与亏格。群 E 的定义为经典输入；逆像高度不是前向周期。 |
| C411 — Joint meromorphic boundaries of two-clock common returns | [PDF，11 页](papers/C411_two_clock/main.pdf) · [LaTeX](papers/C411_two_clock/main.tex) | 对所有整数底数 `a,b >= 2`，完整分类双时钟共同回返级数的开绝对收敛域、依赖分支真极因子及整个双圆盘的联合亚纯边界。经典 gcd 估计与既有矩形对象已扣除；联合边界不等于每条切片边界。 |
| C412 — Rational periodic points of monic integral conservative Hénon maps | [PDF，14 页](papers/C412_integer_henon/main.pdf) · [LaTeX](papers/C412_integer_henon/main.tex) | 全体整系数 `(y,y^2+by+a-x)` 的有理周期点穷尽分类，最小周期仅 `1,2,3,4`，尖锐总点数上界为八，并给出全部取等参数。限 monic、整系数、Jacobian `+1`；不推广到一般有理系数或另一符号。 |
| C413 — Integral periodic points of the Fibonacci trace map | [PDF，10 页](papers/C413_integral_trace/main.pdf) · [LaTeX](papers/C413_integral_trace/main.tex) | 固定映射 `(y,z,yz-x)` 在全 `Z^3` 的周期穷尽分类，最小周期恰为 `1,3,4,6,12`，非周期整数点双向 proper escape，并确定每个整数不变量层的返回律。已知周期族的存在不是新主张；不声称有理点分类。 |

两篇自然边界文章的问题不同：C409 解决一变量中复相位抵消后的
精确有限判据及 wild 实现；C411 解决两个独立迭代时间下的完整
双变量延拓几何。C412 是整个两参数 Hénon 族；C413 是单一三维
迹映射的所有整数层。C410 则是 generic 野性逆像塔，不与它们
混用时钟或点数。

## 数学证据、实际来源与审稿

[审查裁决总表](REVIEW_ADJUDICATION.md) 链接五份真正的非作者全文
审查和受影响段确认。所有审查来自当前内部团队，不称为人类／
外部同行评审。C409 的导子量词与经典命题定位、C410 的三根相异
说明、C413 的有限盒内周期限定均有真实修订记录；未制造固定
轮数的改写版本。C411 与 C412 没有必须修订项。

固定证明来源如下：前四篇沿用原研究快照，第五篇的证明在本树；
各篇稿件的引文记录均在本树。

- C409：[完整原证明](../research_c409_c413/arithmetic/PROOF_PACKAGE.md)、
  [真实 wild 例](../research_c409_c413/arithmetic/REALIZED_EXAMPLE.md)、
  [新增稿引文记录](papers/C409_wild_fad/CITATION_METADATA.md)。
- C410：[完整原证明](../research_c409_c413/positive_characteristic/WILD_CUBIC_PROOF.md)、
  [精确检查范围](../research_c409_c413/positive_characteristic/EXACT_CHECK_REPORT.md)、
  [稿件引文记录](papers/C410_wild_cubic/CITATION_AUDIT.md)。
- C411：[完整双时钟原证明](../research_c409_c413/arithmetic/RECTANGULAR_RETURN_PROOF.md)、
  [原精确检查](../research_c409_c413/arithmetic/RECTANGULAR_EXACT_CHECK_REPORT.md)、
  [稿件引文记录](papers/C411_two_clock/CITATION_METADATA.md)。
- C412：[偶支原证明](../research_c409_c413/nonlinear_geometry/PROOF_INTEGER_HENON.md)、
  [奇支原补充](../research_c409_c413/nonlinear_geometry/ADDENDUM_INTEGER_HENON_ODD.md)、
  [稿件引文记录](papers/C412_integer_henon/CITATION_AUDIT.md)。
- C413：[全整数原证明](nonlinear_geometry/PROOF_PACKAGE.md)、
  [独立精确验证收据](nonlinear_geometry/VERIFICATION.md)、
  [原来源范围](nonlinear_geometry/SOURCE_LEDGER.md)、
  [稿件引文记录](papers/C413_integral_trace/CITATION_AUDIT.md)。

这些有界来源检查不是全球优先权证明。未取得的最终书稿、订阅
全文，以及预印本／最终排印版之间未逐字核对的差异均明确保留。
有限检查不证明无限量词；相应一般定理的证明在实际正文中。
本轮未因排版、日期改变或归档而重跑输入未变的旧数学实验。
原 48 文件研究快照及前批 179/93 文件封存包不回写。

## Route A：源成果与目标门槛严格分开

采用完整读取并固定摘要的 Route A v0.2.0：
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
六篇参考 PDF 的实际导论读取、来源锁、目标缺项理由见
[评价范围](EVALUATION_SCOPE.md)；五份结构检查通过，另有
[限定语义一致性审查](arithmetic/REVIEW_EVALUATION_CONSISTENCY.md)。

| 对象 | 完整严格 tuple（A0,A1,A2,A3,A4） | 评价 |
|---|---|---|
| C409 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | [YAML](evaluations/route_a/HCS-C409/2026-09-06.yaml) |
| C410 | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | [YAML](evaluations/route_a/HCS-C410/2026-09-06.yaml) |
| C411 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | [YAML](evaluations/route_a/HCS-C411/2026-09-06.yaml) |
| C412 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | [YAML](evaluations/route_a/HCS-C412/2026-09-06.yaml) |
| C413 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | [YAML](evaluations/route_a/HCS-C413/2026-09-06.yaml) |

五项总体均为源限定 `ROUTE_A_EXPLORATORY`，不是目标通过。
三类强制算术对照门全部 `INCOMPLETE`；45 格 A2 指标均明确
`NOT_TESTABLE`，并非误差为零。全部目标／Route-B scope flags
为 false。保留 `NO_BAD_EULER_OR_ROOT_NUMBER`：没有建立目标
Euler 因子、根数、自守性、零点／除子对应或 Hilbert–Pólya 算子。
本批有完整源数学成果，但没有 A1/A2 目标突破。

## 构建、历史文件与封存

[终构建记录](FINAL_BUILD_REPORT.md) 固定五个最终 PDF 的真实字节
摘要、十次干净构建、源复制一致性、字体／文本检查及全部页的
实际视觉检查。[最终源摘要](FINAL_SOURCE_SHA256SUMS) 固定 50 个
TeX／BibTeX 输入。每篇的 `final_build/` 保存真实日志、字体列表、
PDF 元数据和已检查文本；根目录 `main.pdf` 是唯一交付入口。

`BUILD_REPORT`、作者局部图、`build_author/`／`author_build/` 中
的 PDF、初编辅助文件，以及初稿审查摘要保留为历史证据。它们
不代表最后修订后的 PDF。部分历史报告的 PENDING 是该检查时的
状态，由本页、终构建记录和实际确认追加段明确更新；不回写成
仿佛最初已完成。[只读载荷盘点](arithmetic/PAYLOAD_INVENTORY_REVIEW.md)
也明确是构建中的非原子快照，不冒充最终成员核验。

本树采用 [精确 payload ledger](ARTIFACT_LEDGER.md) 和
[自排除 manifest](MANIFEST.sha256)。ledger 排除两清单自身，
manifest 包含 ledger 但排除自身；所有实际载荷均列入，包括被
Git 默认忽略的历史日志与辅助文件，不只以可见文件列表为准。
最终摘要／成员集合核验结果记录在批次外的当前状态入口；这两份
清单是最后生成物，不能以本段规则声明替代实际运行收据。
未新增发布程序或通用安全保证。

## 未选研究与五篇检查点

[算术有限格点逆问题](arithmetic/SCOUT_REPORT.md) 数学上已得非作者
支持，但 1996/1999/2003 的确切历史归属仍未清，不编号、不计篇。
[正特征续接筛选](positive_characteristic/SCOUT_REPORT.md) 的一般
cocycle 引理未证，停止于已记录范围。
[谱滤波筛选](spectral/SCOUT_REPORT.md) 与旧两类札记同样不计篇。
五个实际论文合同来自上表，不来自这些备选记录的拆分。

最终同步只使用已配置仓库的常规提交／推送，先检查远端增量，
只纳入本树、当前状态入口和两份 Hénon 注册表；八个继承未跟踪
目录及其他研究流保留不动。封存与真实 refs 核对完成后即交付
本批五篇，等待用户下一次授权，不进入 C414，也不向期刊或
第三方平台上传稿件。
