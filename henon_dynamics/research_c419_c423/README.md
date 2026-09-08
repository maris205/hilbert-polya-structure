# C419–C423 五篇完整论文

最新授权：用户收到第八轮 4/5 检查点后明确 **“确认，下一轮”**。
同批[第九轮研究](continuation_round9/PLAN.md)已新增准入 CP9，
现已完成 **M1／AS2／IR1／P7／CP9 五项独立合同的完整正文与最终 PDF**，
共 **67 页（11／18／18／14／6）**。
CP9 的全特征三域／全起点对同时预周期参数分类通过非作者全文
审查及协调者来源／实质增量核查，见
[第五项准入裁决](continuation_round9/CP9_ADMISSION_REVIEW.md)。
[第九轮协调裁决](continuation_round9/COORDINATOR_REVIEW.md)已收束；
AS1 与 AY 辅助结果通过范围内审查，原完整问题仍未闭合，不另计
论文。[五篇大纲](BATCH_PLAN.md)经[独立审查](REVIEW_OUTLINE.md)
通过、零必改项。五篇各有两轮真实非作者全文稿件审查及实际修订，
现均无剩余必改项；每篇两个全新最终构建的 PDF 逐字节一致，
全部最终页已实际查看。这是五篇成稿，不是五个提纲或研究合同。

## 五篇最终 PDF 与各自增量

| 论文 | 完整成果及严格边界 | PDF／源码与证据 |
| --- | --- | --- |
| C419 正字迹映射的整数周期分类 | 对所有含两种生成元的正字，完整周期点并集恰为 39 条仿射直线加四点；每个整数层化为至多 40 个候选的精确逐点分类，所有其他整数点双向趋于无穷。40 不是已实现最小周期的声明。 | [11 页 PDF](papers/C419_positive_trace_words/main.pdf) · [源码／证据入口](papers/C419_positive_trace_words/README.md) |
| C420 全层数 cusp 散射矩阵交换分类 | 对所有正整数层数、完整固定宽一 cusp 坐标，给出必要充分条件；完整处理非实字符平方、奇偶指数与张量非抵消，解释层数 50 不交换而 100 交换。经典散射重构明确归来源。 | [18 页 PDF](papers/C420_scattering_commutativity/main.pdf) · [源码／证据入口](papers/C420_scattering_commutativity/README.md) |
| C421 三项三次递推的全整数周期分类 | 对每个整数参数 a，完整分类 T_a(x,y,z)=(y,z,yz+a−x) 的所有普通整数周期，八个参数族加两例外，并给出最小周期及逐层有向计数。精确有限核心来自证明归约，不是猜定搜索截断。 | [18 页 PDF](papers/C421_integral_return/main.pdf) · [源码／证据入口](papers/C421_integral_return/README.md) |
| C422 有限域 q-Painlevé I 的统一周期界 | 对每个有限域及全部允许非零参数、完整七分支原生状态，证明 r 整除 ℓ 且 ℓ/r≤q+1+2√q；边界格与极点整除排除所有可约／多重有限纤维，包含例外线、奇异纤维及特征二／三。未证明分箱分布猜想。 | [14 页 PDF](papers/C422_painleve_bound/main.pdf) · [源码／证据入口](papers/C422_painleve_bound/README.md) |
| C423 特征三同时预周期参数分类 | 对 f=X⁴+X⁶、任意特征三域和任意标记点对，无穷多个参数同时预周期当且仅当两点均为常数或 f(a)=f(b)；统一二周期／逃逸参数解决来源留下的两个非零差值。不是全等权二项式族的分类。 | [6 页 PDF](papers/C423_two_cycle_preperiodicity/main.pdf) · [源码／证据入口](papers/C423_two_cycle_preperiodicity/README.md) |

## 正式评价、审查与发布证据

- [两轮稿件审查裁决](REVIEW_ADJUDICATION.md)保留十份完整原始报告及五份实际回复。
- [最终构建总报告](FINAL_BUILD_REPORT.md)记录五组逐字节一致 PDF、全部 67 页检查及真实失败历史；C421 首对构建的 trailer-ID 差异已用纯构建设置消除，失败对仍保留。
- [正式评价对象／时钟锁定](EVALUATION_SCOPE.md)与[非作者一致性审查](REVIEW_EVALUATION.md)单独记录科学等级，不以构建通过代替评价。
- [发布工具与精确成员政策](release/README.md)说明原字节复用已审工具及历史失败路径测试；本页在封存前写成，实际封存、批准摘要及 Git 状态以包外[最终发布收据](../RELEASE_C419_C423.md)为准。

评价权威固定为 Route A v0.2.0，SHA256
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c。
五篇均为 **ROUTE_A_EXPLORATORY**：

| 范围 | A0 | A1 | A2 | A3 | A4 |
| --- | --- | --- | --- | --- | --- |
| C419、C421、C422、C423 | A0_WEAK_ARITHMETIC_RELATION | A1_WEAK | A2_FAIL | A3_FAIL | A4_FAIL |
| C420 | A0_WEAK_ARITHMETIC_RELATION | A1_FAIL | A2_FAIL | A3_FAIL | A4_FORMAL_HINT |

五份最终记录见 evaluations/route_a/ 下的 HCS-C419 至 HCS-C423。
全部 **45 项 A2 指标是 NOT_TESTABLE，不是数值零或通过**；A0
必需对照面板仍 INCOMPLETE。C420 的 A4 形式线索仅承认已有的
真实经典散射结构，不是新量子提升、A2 进展或 Route B 准入。
所有目标 Euler 因子／根数／自守／零点／谱实现及 Route-B 标志均为 false。

来源访问按真实正文、指定段落、元数据和失败分别记录；未取得的
文献内容仍未知。AI 辅助内部审查不是人类同行评审或全球优先权
证明。原数学收据不冒称为本次新执行，有限样本不替代全称证明。

本批完成后停在 **C423 五篇检查点**。AY 与 AS1 的原完整问题仍
未闭合，不拆辅助定理作第六篇，不开始 C424、不进入 Route B，
不进行外部投稿、稿件上传或公告。NO_BAD_EULER_OR_ROOT_NUMBER 持续有效。

## 历史研究检查点

以下历轮“当前”“缺几项”“零稿件”等文字均指当时快照；
不覆盖上面的五篇最终成稿状态，也不把历轮重复问题累计成新论文。

第八轮历史授权：用户收到第七轮交接后再次 **“继续”**。同批
[第八轮定向研究已完成](continuation_round8/README.md)，**P7 新增
准入；当前 M1／AS2／IR1／P7 共 4/5 项完整合同，仍缺 1 项**。
P7 原全有限域、全参数、七分支周期界经过完整证明、非作者内部
数学审查与协调者来源／实质增量核查；见
[本轮裁决](continuation_round8/COORDINATOR_REVIEW.md)。AY 全有理周期
界、TR 两个有效参数区间及定性归约、FC 精确相关与对数界均
只保留辅助结果，不拆成第五项。四条是旧完整问题续接，不计
成新候选。仍为 0 新稿／PDF／正式评价，没有分配论文编号。

第七轮历史授权：用户收到第六轮交接后再次 **“继续下一步”**。同批
[第七轮有界研究已完成](continuation_round7/README.md)，**零新增准入，
仍为 M1／AS2／IR1 3/5、缺两项、0 新稿／PDF／正式评价**。
AS1 的全深度外围谱和全和精确径向留数已证明并通过非作者内部
审查；非零留数仅在两个实方向，旧“稠密非零留数”方案已排除，
但原整圆问题仍未闭合。AY／PG 辅助证明和 N7 完整否定证书已
复核，仍不满足独立论文准入。十一条筛查含十个新问题和一个旧
AS1 续接；本轮数学程序执行 0 次。见[第七轮裁决](continuation_round7/COORDINATOR_REVIEW.md)。
AF5-C 仍作为已闭合短有效推论退役，不重开其旧有效性缺口。

第六轮历史授权：用户收到第五轮检查点后再次 **“继续”**。同批
[第六轮有界研究已完成](continuation_round6/README.md)，保留 M1/AS2/IR1
**3/5 合同、缺 2 项、0 新稿／PDF／正式评价**。集中尝试 Lyness
整数穷尽和分圆域有效算法两个原问题。后者原全参数终止算法已
证明并通过非作者全文数学审查，但扣除既有扭点对应／有效闭包
机制后为短有效推论，不准入；Lyness 的全周期穷尽仍缺。见
[第六轮裁决](continuation_round6/COORDINATOR_REVIEW.md)。辅助证明不
另计候选，本轮数学程序执行 0 次，旧证明与有限字母表不重跑。

第五轮历史授权：用户收到第四轮检查点后再次 **“继续”**。同批
[第五轮有界研究已完成](continuation_round5/README.md)，保留 M1/AS2/IR1
**3/5 合同、缺 2 项、0 新稿／PDF／正式评价**；不重跑已有准入。
七个筛选条目、五个深入尝试零新增准入，见
[第五轮裁决](continuation_round5/COORDINATOR_REVIEW.md)。Lyness 的完整
低周期／$a=1$ 图谱和避开 $0,-1$ 的普通有理周期全纤维上界分别通过非作者内部审查，
但整数全周期穷尽仍缺。算术反例与有限性保留原全族／有效性缺口；
CF1 全计数及自然边界虽已证明并复核，仍为经典／既有机制短重构。
三个来源账本记录 79 条检索式；本轮数学程序执行为 0，未重跑旧
数学与构建，也未将辅助证明拆成第四、第五项。

第四轮历史授权：用户于 2026-09-08 再次 **“继续”**，同批
[第四轮有界研究已完成](continuation_round4/README.md)。**零新增准入，
仍为 3/5 合同、缺 2 项、0 新稿／PDF／正式评价**。
Hénon 两项短证明完整闭合；Lyness 的整数不变量与 $-1$ 层辅助
结论通过独立内部检查，但全周期仍未穷尽。正特征及全有理迹问题
保留精确反例与全族缺口，见[第四轮裁决](continuation_round4/COORDINATOR_REVIEW.md)。
七个筛选条目不是七个新独立问题；仅有一次新数学程序执行，旧
证明和第三轮有限诊断不重跑。以下各轮为已完成的历史检查点。

第三轮历史续接：用户 **“good，继续”** 后的
[第三轮有界研究已完成](continuation_round3/README.md)，**零新增准入，
仍为 3/5 项独立合同，仍缺两项**。九个筛选条目的
[完整裁决](continuation_round3/COORDINATOR_REVIEW.md)保留来源扣除和
全族证明缺口；其中 AS1 是旧问题续接、B3 仅浅筛，不按九个新问题计数。
本轮新增 McMillan 的无穷有理三周期纤维、迹返回的精确平方分母引理、
Bedford–Kim 无界三周期族及六层实际标量分母等证据；均未替代
原完整合同来凑名额。仍为 0 新稿／PDF／正式评价，未分配 C 编号。
以下第二轮结果是已完成的历史检查点，三项通过的证明/认证不重跑。

用户明确“继续”后，同一 C419–C423 批次已完成
[第二轮有界研究](continuation_round2/README.md)。目前 **3/5 独立合同已准入，
0 新稿、0 新 PDF、0 新正式评价**；仍缺两项完整合同，尚未分配 C 编号。
这是研究检查点，不是五篇论文交付。M1、AS2 不重新计数，IR1
晋升原来的 NG1 问题，不同时算作另一个新候选。

第二轮实质进展：整数全参数问题已形成
[完整普通周期分类和逐层计数](continuation_round2/integral_return/IR1_CLASSIFICATION.md)，
经解析与独立有限核心审查、协调者全文/来源/实质增量审查后
[准入一项](continuation_round2/integral_return_review/COORDINATOR_REVIEW.md)。
两份非作者审查均已闭环，没有剩余必改项。
[算术两候选](continuation_round2/elliptic_dynamics/SCOUT_REPORT.md)、
[正特征两候选](continuation_round2/new_charp/SCOUT_REPORT.md)、
[同余塔重构](continuation_round2/congruence_towers/PROOF_PACKAGE.md) 与
[第二圆周新诊断](continuation_round2/solenoid_boundary/DIAGNOSTIC_RECEIPT.md)
均未增加准入数。下述十二项计数专指首轮，不把复查同一问题
重复算作新候选或新论文。

## 历史研究与准入入口

- [第九轮计划](continuation_round9/PLAN.md)：AY 全族与 AS1 整圆定向续接，加一条有界正特征替代来源筛查，保留 4/5 基线。
- [第八轮交接](continuation_round8/README.md)：P7 完整准入、三条辅助证明、当前 4/5 状态及实际来源／执行边界；[冻结计划](continuation_round8/PLAN.md)保留当时四条尝试的原问题门槛。
- [第七轮交接](continuation_round7/README.md)：全深度辅助定理、来源修正、独立审查与未闭合原问题；[冻结计划](continuation_round7/SCOUT_PLAN.md)保留当时的未证明尝试。
- [准入裁决](ADMISSION_DECISIONS.md)：最终五项准入及历轮各问题的实际去向；原八轮四项基线已由 CP9 补齐。
- [P7 完整证明](continuation_round8/painleve/PROOF_PACKAGE.md)、[非作者全文审查](continuation_round8/painleve_review/REVIEW.md)与[来源／增量决定](continuation_round8/P7_SOURCE_CHECK.md)：第四项完整合同，非第四篇已交付论文；原猜想与积分仍归来源。
- [第六轮交接](continuation_round6/README.md)：原全参数有效算法闭合但未清除独立增量门槛，Lyness 全周期仍缺；数学和文档审查分列。
- [第五轮交接](continuation_round5/README.md)：完整辅助图谱、全纤维上界、精确反例、来源重构与剩余全族缺口。
- [第四轮交接](continuation_round4/README.md)：两项短闭合、辅助证明、反例、精确缺口与当前检查入口。
- [第三轮交接](continuation_round3/README.md)：新证明、有限诊断、具体缺口与审查入口。
- [选题与完成合同](SCOUT_PLAN.md)：五项独立实质合同成立后才启动
  五篇稿件计划；不拆短推论填补名额。
- [正字迹映射分类审查](mapping_class_review/REVIEW_PROOF_AND_INCREMENT.md)：
  已准入。全体含两种生成元的正字、所有整数不变量层上的统一
  周期点分类、有限算法与双向逃逸是一项完整合同。
- [全层数散射证明入口](arithmetic_spectral/AS2_PROOF_INDEX.md)：
  已准入。[非作者证明／来源／实质审查](arithmetic_spectral/non_author_review/REVIEW.md)
  通过，协调者已读完两份审查并关闭全部必改项。
  层数 50 和 100 推翻的两版猜想均保留，不与最终奇偶性条件混淆。
- [切换 solenoid 的准确证明边界](arithmetic_spectral/solenoid_review/PROOF_STATUS.md)：
  两个实边界点不可亚纯延拓已证明，整圆自然边界未闭合，不准入。
- 三条首轮报告：[正特征](positive_characteristic/SCOUT_REPORT.md)、
  [算术动力学](arithmetic/SCOUT_REPORT.md)、
  [非线性几何](nonlinear_geometry/SCOUT_REPORT.md)。九项在首轮均不准入；
  其中 NG1 现已晋升 IR1，其余保留原有来源扣除、短诊断和证明缺口。

源文献核查区分实际全文／指定段落访问、仅有元数据及访问失败。
当前团队的审查是 AI 辅助内部审查，不是人类同行评审或全球
优先权证明。没有外部投稿、稿件上传或公告。

## 证据与工作边界

第八轮的[P7 非作者全文审查](continuation_round8/painleve_review/REVIEW.md)
与[FC 非作者辅助审查](continuation_round8/orbit_sums/INDEPENDENT_HELPER_REVIEW.md)
均被协调者完整读完；协调者另行完成
[AY 辅助审查](continuation_round8/adler_yamilov/COORDINATOR_HELPER_REVIEW.md)
及[TR 辅助审查](continuation_round8/totally_real/COORDINATOR_HELPER_REVIEW.md)。
四个实际证明范围无剩余必改数学问题，只有 P7 清除了完整合同
及实质增量门槛。[文档静态审查](continuation_round8/CHECKPOINT_DOCUMENTATION_REVIEW.md)
另列范围。本轮仅一次 AY 冻结数学诊断，旧证明和构建不重跑；
54 次成功检索提交另加三条 TR 投递未知尝试，不称全球查新。
作者审查前 pending 文字保留为历史快照，以最终审查／裁决为准。

第七轮的[AS1 非作者数学审查](continuation_round7/spectral_review/INDEPENDENT_REVIEW.md)
逐条复核所有深度、短长度、字符判据和全加权极限；
[AY／PG 独立辅助审查](continuation_round7/nonlinear_review/INDEPENDENT_HELPER_REVIEW.md)
覆盖原生图表、零坐标界、逆映射和 AY 不变量修正。协调者完整
读完两份审查，并在[裁决](continuation_round7/COORDINATOR_REVIEW.md)中
给出 N7 的非作者手推复核。范围内无必改数学问题，原完整问题
的未闭合标签不变。另列[文档与状态审查](continuation_round7/CHECKPOINT_DOCUMENTATION_REVIEW.md)，
不作为新增数学执行或全局查新证明。

第五轮的[Lyness 分支非作者复核](continuation_round5/lyness_closure/INDEPENDENT_STRATA_REVIEW.md)、
[有理周期界独立复核](continuation_round5/lyness_sources/INDEPENDENT_PERIOD_BOUND_REVIEW.md)、
[算术辅助证明审查](continuation_round5/arithmetic_frontier/INDEPENDENT_HELPER_REVIEW.md)
与[完整 CF1／辅助 CF3 复核](continuation_round5/charp_frontier/INDEPENDENT_HELPER_REVIEW.md)
均保留各自实际范围且无必改数学问题。协调者完整阅读两份委派
审查以及三支线实际证明／报告／来源，不将来源访问或哈希算作
数学复算。下述各轮检查是历史收据，不冒算为本轮新执行。
第五轮[文档／静态审查](continuation_round5/CHECKPOINT_DOCUMENTATION_REVIEW.md)
亦已闭环，24 个范围、145 处真实本地链接均无缺失；摘要适用域
遗漏已修正，收据明确不覆盖随后新增的报告入口链接。

第四轮的[Hénon 短证明审查](continuation_round4/dissipative_henon/INDEPENDENT_SHORT_PROOF_REVIEW.md)
和[Lyness 辅助审查](continuation_round4/third_order_lyness/INDEPENDENT_HELPER_REVIEW.md)
均无范围内必改数学问题；[文档／静态审查](continuation_round4/CHECKPOINT_DOCUMENTATION_REVIEW.md)
单列实际文件、链接和内存语法检查，不是再次数学执行。
唯一新程序覆盖 65,536 个有限字母表状态及 363 个周期，无周期截断；
后续无界六周期手推族才是常高度假设的全族反证。查询收据合计
63 个实际检索式，不表示全球查新通过。下述历史收据不与之冒算
独立数学认证或新论文。

第三轮的[辅助证明审查](continuation_round3/INDEPENDENT_HELPER_REVIEW.md)
只读核对新 RT3 与 AS1-R3 帮助引理；
[文档/静态审查](continuation_round3/CHECKPOINT_DOCUMENTATION_REVIEW.md)
单列最终范围和限制，不声称重新执行数学程序。下述第二轮和首轮
收据是历史检查，不与第三轮累计为独立数学认证。

第二轮另有已完成的
[文档/静态代码审查](continuation_round2/CHECKPOINT_DOCUMENTATION_REVIEW.md)：
当前 3/5 状态一致，27 个范围的 117 处简单本地链接均存在，五个
新脚本静态编译通过。下述 32 份/115 处及七范围/56 处是首轮
历史收据，不与第二轮重复累计，也不代表数学重跑或封存。

各证明依赖其真实推导及列明的经典输入，有限诊断不证明无限族。
已有通过的旧封存数学检查和 PDF 构建没有重跑。主字符的 40 格
散射检查与单个层数 50 检查均有原收据；全层数结论不是扩大
数值表后外推得到的。

[文档／静态代码审查](checkpoint_review/REVIEW_DOCUMENTATION_CODE.md)
记录当时 32 份 Markdown 的 115 处本地链接均存在、五个新 Python
脚本的语法与静态编译通过。三个纯文档问题已修正并由原审者
定向复核关闭。该扫描没有预先覆盖后来添加的本入口或非作者
审查文件，也不是重新运行数学代码；脚本的正常模式／JSON
结果读取限制在报告中保留。

协调者随后仅检查新增／改动的链接范围：本入口、准入裁决、
AS2 证明入口与算术条件、两份非作者审查，以及总状态的本批
前缀，共七个范围、56 处本地链接，缺失为零；七处 HTTPS 链接
明确排除。实际使用 Python 3.12.3 的无字节码、只读标准库检查，
退出码 0，没有执行研究脚本。这是简单行内 Markdown 目标的
路径存在性检查，不是完整渲染、数学复算或封存保证。

科研起点为 2974f8ea5f9e7cb0f8146cae017add38a6939da0。
该起点不被伪称为已包含新稿件；最终载荷与 Git 对象另由发布收据
绑定。旧封存树和八个继承的未跟踪目录不改动。历轮各问题的具体
排除原因继续保留，不把参数表或短推论改名填补名额；上方五篇
成稿对应各自完整、已审的独立合同。来源系统的算术分类不建立
目标 Euler 因子、根数、零点对应或 Hilbert–Pólya 实现。
