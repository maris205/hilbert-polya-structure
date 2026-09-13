# Paper30 qPI：整系数退化与通用上同调的数学合取处置 V1

日期：2026-09-09。主控 `/root`。
状态：**D/G/S/U 数学接受；新问题的完整查新与组合非碰撞未完成；Paper30 未立项。**
route_applicability: NOT_APPLICABLE（纯数学结构，不是 Route A/B 评价）。
Batch07 本地论文验收仍为 **3/5**；Paper31 与最终跨论文审计尚未开展。

## 1. 本次真实变化

在旧 qPI 完整 V2 新意双票合取 FAIL 之后，本轮检验了新的族内量词：
从单个域上的有限阶参数改为整个整数参数族、非平坦／非约化基变换，
以及原根单位阶在坏素位下降时同一个完整模型与原状态微分的变化。
现有四份作者证明和四份非作者报告已由主控全文读取并按下表实际哈希核准。
主控接受下列原命题，未添加一般时间参数、奇素数或 $a=1$ 等削弱条件。

| 数学模块 | 实际接受的原内容 | 非作者报告 |
|---|---|---|
| [D1–D3](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 原积分先除后约化的相对微分、准确公共阶、含重数系数理想及光滑层 Hasse 解释 | [D 独审：PASS](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md) |
| [G1–G3](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 同一个完整八截面模型、原 pencil 射影平坦退化、原基变换缺陷、过滤长度和全开放空间微分 | [G 独审：PASS](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) |
| [S](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 整个根单位整数基环上的原迹系数截面与边界单位；原 DVR 扭子过滤逐级分裂和全部初等因子 | [S 独审：PASS](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md) |
| [U](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 无关系整数环上所有反典范幂的实际对角复形，真实常数项、任意基变换与指定 Fitting 理想 | [U 新增步骤：PASS](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md)，S5/S7 依赖按 §2 合取关闭 |

这是数学接受，不是独立价值、新意、正文容量、PDF 或论文准入的 PASS。
四位非作者分别负责实际新增义务；是独立 AI 检查，不是人类或跨模型认证。

## 2. U 的接受依赖已经实际合取

U 独审全文 284 行，明确只接受 U 的新增证明及消费接口，
保留 `PENDING_CONJUNCTION_WITH_S5_S7_REVIEW`，没有据交流消息代签 S。
主控随后全文读 S 独审 413 行；其 Steps 1–5 实际核准了 S5/S7：

- 原 $C_j$ 在 $\mathbb Z[q^{\pm1},\tau^{\pm1}]/(q^j-1)$ 全模型上为 $L_j$ 截面。
  全部 $d\mid j$ 特征零分支均被检查；下降使用完整环面边界的平坦允许极点商，
  而非非正规基环上的 Hartogs 或只检查约化点集。
- 真实 $x^{-j}$ 帧中的首项是单位 $(-\tau)^jq^{j(j-1)/2}$，
  并沿实际节点单位帧传播到整个八环；包括非约化商环上的拉回。

S 与 U 两份独审引用的 S 作者输入同为
`2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac`。
U 中的基环、吹起模型、边界、原矩阵次序、系数提取与 S5/S7 完全对应，
其独审 Step 3 已检查这个消费接口。主控再核同哈希与实际内容，
因此此处关闭审查所有权依赖，接受 U 全部原命题；不修改 U 独审的历史提交状态。
不把这个合取说成新增科学假设或再一次对同一证明重审。

S 派发与最终记号补齐交错：初始消息引用未冻结 412 行，作者随后补六行记号为最终 418 行。
主控明确绑定最终版本后，S 独审实际全文检查该 418 行；并不存在一份被覆盖的已冻结 412 行稿。
此身份调整和实际阅读已经写入独审，未将一次任务伪记为两次独立检查。

## 3. 接受结论的准确范围

### 3.1 通用整系数上同调

在 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 的同一个八截面曲面上，
对每个 $n\geq0$，有保留真实常数项的非典范同构
$$
R\Gamma(S,\mathcal O(nD))\simeq
R[0]\oplus\bigoplus_{j=1}^{n}[R\xrightarrow{1-q^j}R],
$$
两项复形位于次数 $0,1$。固定一次选择后，对所有交换 $R$-代数 $A$，
包括非平坦、非约化和非 Noetherian 的基环，逐项张量得到完整上同调。
特别是
$$
H^0\simeq A\oplus\bigoplus_{j=1}^{n}\operatorname{Ann}_A(1-q_A^j),
\qquad H^1\simeq\bigoplus_{j=1}^{n}A/(1-q_A^j),\qquad H^{\geq2}=0.
$$
原 $R$ 上的零阶 Fitting 理想为 $\left(\prod_{j=1}^{n}(1-q^j)\right)$。
这没有宣称通常的 $H^0$ 非平坦基变换总是同构。

### 3.2 圆分原 pencil 与全部初等因子

令 $N=p^a,r=mN$，$p$ 任意素数、$a,m\geq1$、$p\nmid m$，
$\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$、$\mathfrak p\mid p$，$s=\zeta_r$，
$t\in\mathcal O^*$ 任意，$e=v_\pi(p)$。剩余 $\eta=\bar s$ 精确阶为 $m$。
原 $1,I_r$ 在完整模型上生成射影平坦 pencil，剩余态射为
$\operatorname{Pow}_{N}\circ f_m$。每个有限几何剩余纤维为小阶完整纤维的 $N$ 倍，
无穷纤维为 $r\bar D$；幂态射保持剩余域常数，不混同绝对 Frobenius。

设 $\mathcal T=H^1(\mathcal S,\mathcal O(r\mathcal D))_{\rm tors}$，则
$$
\mathcal T\simeq\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j)
\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})}.
$$
逐级分裂由 Bockstein 的有限阶商生成元证明，不由长度猜测。
因此长度为 $ae$、最少生成元数为 $N-1$、零阶 Fitting 理想为 $(r)$。
原线性系的实际剩余像为 $\kappa\langle1,J^N\rangle$，
而完整剩余空间为 $\kappa\langle1,J,\ldots,J^N\rangle$，其中 $J=I_{m,\eta}$。

### 3.3 完整开放模型上的相对微分

微分只作用于原状态 $x,y$，固定时间及根单位参数。
令 $H=H_p(\bar t^m,J;(-1)^{m+1})$ 为 D 的准确多项式，则
$$
\alpha=p^{-a}dI_r\in\Gamma(\mathcal U,\Omega^1_{\mathcal U/\mathcal O}),
\qquad\bar\alpha=H^{(N-1)/(p-1)}dJ.
$$
此式及系数理想等式覆盖 $\mathcal U$ 的四条完整末端线，含 $p=2,3$。
沿整个剩余曲面泛点的公共 $\pi$-阶准确为 $ae$。
该阶不等于每个闭点提升的实际赋值；D 独审给出的 $p=2,r=2,t=x=y=1$ 反例边界保留。
统一除公共因子不等于对理想作 $\pi$-饱和。

## 4. 新意扣除与尚未完成的评价

以下来源记录均经主控全文读取，不把有限查询量说成全球先例排除：

- [圆分／q-curvature 先例](PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md)：
  JR 的原圆分矩阵结构、成熟 q-curvature，以及 Koroteev–Smirnov 2026 的特定首非零分歧项均保留。
- [整除微分来源差分](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md)：
  谱多项式与 higher Hasse–Witt 系数准确对应后，Hasse 迭代乘子被 Vlasenko Theorem 1(i) 直接包含。
  主控已亲读其定义和定理并核准代数识别；该指数不再作为新一般结果。
- [G 上同调来源预筛](PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md)：
  STT 的复数 Okamoto–Painlevé 对变形结果是旧背景，非本题整数 $H^1(\mathcal O(nD))$ 模。
- [整系数上同调先例核查](PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md)：
  GHK 通用周期族、Example 5.6 的近邻八个 $(-2)$ 环几何与 Friedman 周期理论保留。
  Stacks 的 perfectness／任意派生基变换直接适用；它们及 Ext、Fitting 算术均为标准工具。

主控另亲读 GHK 作者 v5 的 §1 及 Lemma 2.1、Example 5.6、Construction 5.7、
Remarks 5.8–5.9、Lemma 5.10、Corollary 5.11；
Friedman 作者 v2 引言、Definitions 3.7/3.9、Theorem 3.11 的陈述与证明及检索带出的相关段。
这些实读结果支持对象／底环区别，不构成全文排除；尚未证明 GHK 近邻模型与原 qPI 的精确整数坐标同构。
旧 Ohyama、GRT11 真实全文缺口也不因本次新计算被关闭。

现在固定[新问题 Phase A 的 C1–C3](PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md)，
完整多来源 Phase B 与独立组合增量核查正在执行。后续 Phase C/D 及正式双份完整四门尚未执行。
一般机制与真正实例识别必须分开，不将正确性、未检出、工具数量或来源数量转换为新意分数。

## 5. 本轮其他筛选的有限处置

[族内新问题集](PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md)
及[泛 torsor 预筛](PAPER30_QPI_GENERIC_TORSOR_SCREEN_V1_20260909.md)
指出一般 period/index 结论可由原 Halphen 几何推出，不能独立拆成论文。
[真实多截面诊断](PAPER30_QPI_TORSOR_MULTISECTION_DIAGNOSTIC_V1_20260909.md)
给出了具体覆盖与低阶分歧分析，但没有完成全部最小覆盖分类或 Weil–Châtelet 余循环。
这些仅作为筛选记录保留，未在本件另颁新数学接受或将未完成内容并入新主张以增加价值。
当前选择继续查的是上述整系数 C1–C3，不是跨族新方向。

## 6. 输入身份与实际变更边界

| 输入 | 主控已读范围 | SHA-256 |
|---|---|---|
| D 作者 | 全文 268 行 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| D 独审 | 全文 306 行 | `7c0ecd10991f80f0614713f344ab600a4eb69fd7356135fcfc927ed71a95d0bb` |
| G 作者 | 全文 254 行 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| G 独审 | 全文 286 行 | `ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b` |
| S 作者 | 原 412 行全文及最终全部补充段，合计覆盖最终 418 行 | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` |
| S 独审 | 全文 413 行 | `ae768ae89301af115dc917e9a4b075b401258fb563628e1238b01844a30da941` |
| U 作者 | 全文 255 行 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| U 独审 | 全文 284 行 | `9f54da405b8a40f58e34dc372fad7200452871171a92a0e0063edf1742e3cd55` |
| 整系数上同调来源核查 | 全文 | `26e901d014f553773838f20b1b3ea46b607deffbcf9d73a503cab3ef24570450` |
| 新问题 Phase A | 全文 107 行 | `bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5` |

U/S 报告均停止改动后核对上述身份。全新 Phase B 和组合核查先前因额度报错终止；
用户明确“继续，额度重置了”后，主控确认终态并在原实例接续，未把已终止任务当作运行中等待。
这不影响已完成的四对数学输入，也不将尚未提交的检索计为完成。

proof-writer 使本轮分别核准下降、扩张与派生接口；research-lit 使来源按实际条件扣除；
novelty-check 目前完成的是准确 Phase A，余下步骤依实际报告继续。
旧完整 V2 双票 FAIL 不变，不重抽同一内容，不自动建立 V3。
每位新意及独立价值至少7.5、完整证明信心至少9、自然完整正文22–30页要求不变。
本次只新增研究证明／检查／来源／处置文件及更新当前入口；未修改旧票、旧接受产物或锁，
未建立 Paper30 项目、source/publication locks、论文稿、试排 PDF 或开展 Paper31。
全部效力限于本地，五篇目标与最终跨论文统一审查保持未完成。
