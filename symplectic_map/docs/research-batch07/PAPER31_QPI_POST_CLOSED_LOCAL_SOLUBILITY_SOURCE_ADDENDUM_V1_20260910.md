# Paper31：关闭后新发现的局部有点性来源增量 V1

日期：2026-09-10（项目日期）。主控：`/root`。
状态：`BOUNDED_SOURCE_ADDENDUM / QUICK_FILTER_INPUT / NO_NEW_MATHEMATICS / NO_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。这是新问题 N06 的首筛来源输入；不回写已冻结的[Phase 1地形汇合][PHASE1]，不宣布首筛或深查新已完成。

## 1. 实际问题与本地边界

本人全文读取[基线盘点][BASE]210行。旧 I09 的原完整曲线整体有点性仍未由现有链给出；真实末端方程有根是充分条件，无根不是必要性证明。
固定旧诊断为 $K=\mathbb Q_3(\zeta_3)$、$t=1$、$h=0$、$c_0=-3$、$c_1=-3+\pi^2$；本轮未计算或判定 $X_{c_1}(K)$。
拟议新连接是原 proper pencil 的完整能量像与 P30 临界理想，而非给不同能量的 WC 类强加一个共同 Jacobian。
该连接只是问题；微分理想控制 Hensel 半径的标准机制和曲线有点性的局部恒定性必须先扣除。

## 2. 实际检索

首轮实际执行以下三个问题查询；后有一次相同查询复核，不增加独立查询数：

1. `"q-Painlevé" "p-adic" "rational points"`
2. `"genus one" "local solubility" "density" pencil`
3. `"p-adic" "image" "Jacobian ideal" Hensel polynomial`

版本定位另执行 `"Local constancy of reduction type" Schrettner arxiv` 与 `"Local constancy of reduction type" "5.4"`。
其余弱相关的有界高度／Yomdin–Gromov、一般 Hensel 教材及综述结果没有用作原 qPI 先例排除。未用非一手页面作结论依据。
本件仅为逐题首筛增量，不冒称完成 novelty-check 的逐主张多源深查；Phase 1 的 Scholar 403／Semantic Scholar 429 失败保持，没有绕过访问限制。

## 3. 两项核到的来源

### S1：局部恒定性已是强一般先例

Jakab Schrettner，*Local constancy of reduction type and related invariants for curves in p-adic families*，QJM，在线2026-08-06；[刊本](https://doi.org/10.1093/qmath/haag026)、[作者v2](https://arxiv.org/html/2508.12329v2)。v2提交2026-08-21，PDF稿面2026-08-24，日期分别保留。

Th5.3在excellent DVR、光滑射影曲线及模型正则闭嵌入正则ambient的条件下给充分近曲线的正则模型同特殊纤维。Th5.7给Henselian情形有点性恒定；完美剩余域下index恒定。Remark5.4已给可提取精度 $d=d'+n+2$，并在光滑ambient下保留无分歧扩张统一性。[v2 §5](https://arxiv.org/html/2508.12329v2#S5)

本人实读：刊本摘要、引言、Def2.1；v2摘要／引言、Def2.1及完整§5；另定向核PDF文本第15页。整篇PARTIAL，未审计上游§3–4全部证明。刊本后文定向访问曾失败；v2 PDF截图超时，不称视觉核对通过。

公式警告：Th5.7证明的HTML及PDF提取文本把还原目标写成全部 $\mathcal C_s(k)$，紧前却使用相对光滑轨道 $\mathcal C^0$。本件不照抄为“任意特殊纤维点都可提升”；Hensel消费者须保留光滑轨道。此处是主控公式适用性警告，不宣称已推翻局部恒定性定理，也不消费该段为新证明。

**首筛含义（主控推断）：** 单说“有限精度可判定”“有点性局部恒定”或“精度原则上有效”均不足为新贡献。若继续，应给原族实际能量像／严格最优精度或真正不同的统一性，并完整对齐模型与允许扩张；本件未得到这些结论。

### S2：JR刊本有新增说明，但本轮未见原局部分裂定理

Nalini Joshi、Pieter Roffelsen，*Arithmetic dynamics of a discrete Painlevé equation*，J. Phys. A 59(19),195201；在线2026-05-13、印刷2026-05-15。[刊本](https://doi.org/10.1088/1751-8121/ae67bf)、[Crossref](https://api.crossref.org/works/10.1088/1751-8121/ae67bf)

独立来源席 `/root/p31_post_closed_multiplicative_landscape_v1` 只读交付：刊本仍列Conj1.2与Conj3.7；v2后者为Conj3.6。定位到新增Remark3.6关于有限阶参数下形式Lax方程，不是整体局部分裂定理。已读范围的p-adic内容为既有almost-good-reduction背景，局部Artin–Mazur zeta在展望中。[刊本](https://doi.org/10.1088/1751-8121/ae67bf)、[v2](https://arxiv.org/html/2508.18578v2)

该席亲读官方搜索索引实际返回的元数据、摘要、§1/1.1–1.3、Th3.1、Remark3.6、§3.2及邻段、§4；另读v2对应HTML及PDF第1–2、12页文本。IOP直开robots拒绝、PDF截图超时、未做全篇差分。主控读取该席终态交付，不继承其外文亲读身份。本增量不是重新审查P30，也不说刊本整篇绝无局部结果。

## 4. 接续

S1比已冻结形变地形中的一般log lifting更直接；它降低仅“稳定性”版本的投入价值，不自动淘汰原能量像的准确识别。
新生成条目终态后，再合并其量词、其余逐题首筛及真正差异；不因查不到原族同题就授新意。
无数学诊断、GPU运行、新评分、锁、稿件或PDF；Batch07仍4/5，完整失败及已有接受均不变。仅写本地本文件。

[PHASE1]: PAPER31_QPI_POST_CLOSED_DISCOVERY_PHASE1_DISPOSITION_V1_20260910.md
[BASE]: PAPER31_QPI_POST_CLOSED_BASELINE_GAPS_V1_20260910.md
