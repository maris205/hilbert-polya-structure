# Paper30 qPI：非单位时间三阶混合块的有界原始文献预筛 V1

日期：2026-09-09。执行者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
类型：新增、非正式、有界 primary 预筛；不是证明复核、正式查新分数、立项或论文接受。
`route_applicability: NOT_APPLICABLE`。
本轮亲读 `research-lit`，限定五个定向查询、四件最接近原始文献的必要段。
未调用外部模型，未委派新代理；仅写本件。旧先例报告和两件非作者核查报告均冻结不改。

## 1. 结论先行

**孤立混合块是标准二项式/平移代数；具体 qPI 几何实现尚有窄残余，但本轮不支持据此直接立独立长文。**

最直接的扣除不是一般性的“混合特征会出问题”，而是如下准确对应：
在 $R=\mathbb Z[\tau]$ 上，令 $T_\tau f(z)=f(z+\tau)$，则

$$ (T_\tau-1)z^2=\tau^2+2\tau z. \tag{P1} $$

把源限制为 $Rz^2$、靶取 $R\cdot1\oplus Rz$，其矩阵正是
$(\tau^2,2\tau)^t$。这是二项式恒等式，也可直接放进 Callan §5 的带权 Pascal 矩阵族；
本报告给出该对应作为读后推导，**不冒称 Callan 写出了 qPI 的上同调模块**。
因此 $\mathcal M$ 的非主 Fitting 理想、不分裂扩张及模 $2$ 厚度差异，不宜包装成新的普遍机制。
[Callan，§§1–5](https://arxiv.org/html/math/0209356v1)

四件所读原文没有直接给出：固定八次吹起、精确 $q=1$ 切片、$L_3=-3K$ 的实际派生截面，
经整数可逆变换产生作者给出的整个分解及其首次次数。这里保留的是**具体实现的候选残余**，
不是“全球无先例”，也不是已确认的独立研究价值。

Kleiman–Piene–Tyomkin 的工作明确覆盖正/混合特征的近点簇框架及正特征不可分现象；
Evain 提供碰撞/极限线性系统的通用方法；Zahariuc 已有反典范及 fat-point 线性系统的特征差异。
这些都需要实质扣除，不能因本文使用 $\mathbb Z[\tau]$ 就忽略。
[Kleiman–Piene–Tyomkin，§1](https://arxiv.org/html/0905.2169v3#S1)，
[Evain，§§1–2](https://arxiv.org/html/math/0407143v1#S1)，
[Zahariuc，§2.1](https://arxiv.org/html/1711.09323v2#S2.SS1)

## 2. 固定输入与被筛查的声明

仅以下两件是本轮 actual 作者输入；哈希在读取时核对一致。

| 输入 | 身份 | 本轮读取范围 |
|---|---|---|
| [ALL_DEGREE_JET_COMPLEX_V1](PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md) | 358 行，19,874 字节；SHA-256 `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` | Claim、Assumptions、原八中心、$J_n$ 公式及其构造叙述至 Step 5 入口；不是全文证明核查 |
| [DEGREE3_MIXED_OBSTRUCTION_PROOF_V1](PAPER30_QPI_NONUNIT_TAU_DEGREE3_MIXED_OBSTRUCTION_PROOF_V1_20260909.md) | 252 行，12,395 字节；SHA-256 `fe9f9f1c70b20eea4d587d57959eafd9dd8ab42cc128119c32ac6714c77470e8` | 全文读取以绑定准确 claim；包括原 $48\times49$ 矩阵身份、42 个单位 pivot、残余块及不外推项；未重算、未作证明投票 |

本轮把数学结论作为作者声明消费，不替代另行承担的独立证明责任。抽取四项：

1. **C1：全次数 actual jet 复形。** $B=\mathbb Z[q^{\pm1},\tau]$ 上，
   $R\Gamma(S,L_n)\simeq[B^{d_n+1}\xrightarrow{J_n}B^{d_n}]$，$d_n=2n(n+1)$，
   $J_n$ 是原四簇 $1+2+3+2$ 吹起的具体整数二项式矩阵，且任意基变换相容。
2. **C2：三阶具体几何实现。** 精确取 $q=1$、$R=\mathbb Z[\tau]$，作者声明

   $$R\Gamma(S,L_3)\simeq(R^{[0]})^4\oplus(R^{[1]})^2
   \oplus[R\xrightarrow{\tau^2}R]^2
   \oplus[R\xrightarrow{(\tau^2,2\tau)^t}R^2].$$

3. **C3：由 C2 得到的标准代数后果。** 记末块余核为 $\mathcal M$，则
   $\operatorname{Fitt}_1\mathcal M=(\tau^2,2\tau)$，
   $\operatorname{Fitt}_3H^1=\tau^5(\tau,2)$，并有不分裂
   $0\to R/(\tau)\to\mathcal M\to(2,\tau)\to0$。
   两个标量 $\tau^2$ 块及一个混合块，在 $k[\tau]$ 上分别产生
   非 $2$ 特征指数 $(1,2,2)$ 与特征 $2$ 指数 $(2,2,2)$。
4. **C4：次数范围。** $q=1$ 切片中 $n\le2$ 已有标量分解，$n=3$ 首次出现该非主障碍。
   尚未证明全部 $q$、全部次数的规范形，或“每个素数 $p$ 都在 $n=p+1$ 首次出现”的全称模式。

厚度指数比较不是 $\tau=0$ 单个域纤维维数比较：作者声明两种特征在那里均为
$h^0=7,h^1=6$。本轮不会把维数不变误报成无算术差异。

## 3. 实际检索边界与停止条件

五个外部查询已经用尽，没有再扩展新关键词或追逐所有参考文献：

| 编号 | 实际查询字符串 | 返回结果中的有效分支 |
|---|---|---|
| Q1 | `"fat points" collisions "characteristic"` | Evain 碰撞方法入口；Zahariuc 特征依赖的 fat-point 线性系统 |
| Q2 | `"Enriques" "clusters" "characteristic"` | 近点簇/Enriques 文献入口；不少结果中的 characteristic 指 Puiseux 特征而非底域特征，已排除 |
| Q3 | `"Pascal matrix" "Smith" polynomial` | Callan 的整数 Smith、模素数 Jordan 与带权 Pascal 矩阵 |
| Q4 | `"anticanonical" "Fitting" cohomology` | 主要是 Poisson sheaf、其他维数/其他对象或普通单词 fitting；未获得直接相关的实际 $R^1\pi_*\omega^{-n}$ 非主层结论 |
| Q5 | `site:arxiv.org "Enriques diagrams" "Hilbert"` | Kleiman–Piene–Tyomkin 0905.2169；随后打开最终 v3 |

Q4 的噪声结果不能作为不存在先例的证据。Jantzen 格子方向没有在本轮另做专门检索；
Q3 获得更直接的平移/Pascal 对应后按预算收束，不宣称已排尽所有表示论或格子先例。

来源与访问说明：

- 当前可调用工具列表没有 Zotero/Obsidian 文献检索工具；本轮不伪称使用了它们。
- 检查本地 `papers/`、`literature/` 的相关 PDF 文件名及指定脚本路径，
  未找到命名匹配的 collision/Pascal/Enriques/fat-point/Jantzen 文献，亦未找到 `arxiv_fetch.py`。
  本地目录大量是已有批次论文产物，未重扫其 PDF 内容；这不是完整本地全文排查。
- 按技能 fallback 使用 arXiv 定向网页查询与公开原文 HTML，未下载 PDF、未创建文献副本。
- ResearchGate 的 Evain 发现页返回 HTTP 429，未重试；后改读对应 arXiv 原始预印本。
  ResearchGate 搜索摘录不承担任何数学结论。
- 本轮没有新增 Google Scholar/Semantic Scholar 直接查询；旧轮访问限制不在此重试，
  也不计作本轮成功检索。未使用二手综述替代下面的原文。
- arXiv 实验 HTML 页有自动生成的 2026 日期，文献年份取 arXiv 版本记录/刊本元数据，
  不把 HTML 渲染日期冒充发表时间。

停止点：四件 primary 必要段已读，已能区分通用框架、准确孤立块及尚未获得直接覆盖的具体实现。
无需为本预筛重开 Harbourne/TVV 的旧完成段，也无需扩展成完整查新评分。

## 4. 四件最接近原始来源

| 原文、版本与出版身份 | 本轮实际核读的必要内容 | 对本模型的作用 |
|---|---|---|
| Steven Kleiman、Ragni Piene；Appendix B by Ilya Tyomkin，*Enriques diagrams, arbitrarily near points, and Hilbert schemes*，2009；[2011 v3](https://arxiv.org/abs/0905.2169v3)。arXiv 说明为 Rendiconti Lincei 终稿，本轮未另核卷页 | §1 混合特征范围；Definition 3.5、Theorem 3.10；Proposition 5.4 的推前/基变换构造；Theorem 5.7；Proposition 5.9；Appendix B 的 Example B.3、Proposition B.4 与 Lemma B.5 的一阶计算段 | 最接近的相对近点簇框架；明确扣除“正/混合特征近点簇”及“素数导致不可分”本身的新意 |
| Laurent Evain，*Computing limit linear series with infinitesimal methods*，[2004 v1](https://arxiv.org/abs/math/0407143v1)。本轮使用原始预印本，未另核刊本 | §§1–2 的 staircase、域上形式参数设置、Theorem 1 与 Corollary 3；§5 的 successive collision 定义、Proposition 17、Theorem 19 的假设与结论 | 通用 collision/infinitesimal-Horace 方法先例；不是本八中心实际相对 $H^1$ 模的分类 |
| David Callan，*Jordan and Smith forms of Pascal-related matrices*，[2002 v1](https://arxiv.org/abs/math/0209356v1)。本轮使用原始预印本，未核刊本 | §§1–5，尤其 Theorem 1、Theorem 3 与带权 $P_n(\mathbf c)$ 的定义和乘积恒等式 | 最直接的代数先例：参数平移的二项式矩阵；准确孤立混合列已在这个初等机制内 |
| Adrian Zahariuc，*Elliptic surfaces and linear systems with fat points*，Math. Z. 293, 647–660 (2019)；本轮读 [2024 v2](https://arxiv.org/abs/1711.09323v2) | Introduction/Theorem–Example 0.1；§1 Lemma 1.1；§2.1 的 $K=-2E_\infty$ 与 Proposition 2.2 | 反典范截面及 fat-point 线性系统的特征依赖已有具体几何先例；不等同于本 $\mathbb Z[\tau]$ 上的非主 Fitting 厚度 |

### 4.1 近点簇定理：覆盖基础构造，但不能混同为本矩阵的答案

Kleiman–Piene–Tyomkin 的 Definition 3.5 要求：截面相对已有例外严格变换，要么整段包含，
要么整段不交；Theorem 3.10 固定这种 diagram。Proposition 5.4 构造完整理想的平坦族和基变换，
Theorem 5.7 给到 Hilbert 概形的普遍单射。Appendix B 另给特征 $p$ 中切向一阶信息消失的例子。
这些不是仅在复数域上的理论。
[原文 §3](https://arxiv.org/html/0905.2169v3#S3)，
[原文 §5 与 Appendix B](https://arxiv.org/html/0905.2169v3#S5)

与作者输入比对所得的限制是：原簇 3 的末中心 $(u,\xi)=(0,\tau)$，
在 $\tau=0$ 时也碰到前一次例外的严格变换 $\xi=0$；作为原八次序列，不应直接当成一条固定
strict-diagram stratum 内的路径。这只是源假设的对照，不是对作者证明的复核。

反过来，也不能据此声称该通用框架完全不适用：作者先完成四次 toric 吹起后，在 $Y$ 上留下
四个始终互不相交的末截面。它们作为 $Y$ 上四个根点，其 fattening 正在 Proposition 5.9
（全顶点为根）的标准范围内，该命题在任意特征给 embedding。因此四个 fat 商及其相对族
本身没有新机制。仍需要具体极化 $M_n$、全局 monomial 子空间及评价映射，才能得到 $H^1$ 的余核；
上述定理不直接输出本 $J_n$ 的整系数分解或 $\tau^5(\tau,2)$。
[Proposition 5.9](https://arxiv.org/html/0905.2169v3#S5)

### 4.2 碰撞公式：对象、路径和输出都需严格区分

Evain Theorem 1 在域上的形式参数族中，由 staircase、速度和残余条件控制极限线性系统；
Theorem 19 处理四个等重 fat points 依不同切向依次汇到一个支撑点的碰撞。
当前四簇在原曲面上的支撑始终分离，非单位参数改变的是两处末中心与边界的相交情形。
因此“四点”“碰撞”“Enriques diagram”三词重合不构成定理可直接代入。
而域上极限子空间/特殊 subscheme 的结论，也不自动识别 $\mathbb Z[\tau]$ 上完整余核及扩张。
[Evain，Theorem 1 与 §5](https://arxiv.org/html/math/0407143v1)

没有证明 Evain 方法不能被进一步适配；本轮只确认所读结论没有直接给出本 actual 块。
也未把 §4 明示的特征零应用限制，误外推成整篇每个定理都只能用于特征零。

### 4.3 Pascal 先例：准确扣除孤立块，不能偷换整个余核

Callan §5 定义 $P_m(\mathbf c)_{ij}=c_{i-j}\binom{i-1}{j-1}$。
取 $c_j=\tau^j$，其转置就是以单项式为基的平移矩阵。
由此得到 (P1)，是现成二项式族中的准确列，不只是形状类似。
该列一旦给定，余核、Fitting 理想及特征 $2$ 的变化都属于标准交换代数后果。
作者输入已经声明不将这些形式工具另算新方法；这一自限应保留。
[Callan，§5](https://arxiv.org/html/math/0209356v1)

但必须同时保留反方向限制：Callan Theorem 3 的整数对角化对象是 $(P_m-I_m)^r$，
不是任意带参数的截断子矩阵；对整个 Pascal 矩阵合法的变换，也不自动保持几何选定的源子模。
甚至在二次平移差分中，若把源 $Rz$ 也一并加入，就多出列 $(\tau,0)^t$，
这与仅保留源 $Rz^2$ 的表示不是同一个对象。这里不从全矩阵的 Smith 结果，
跨环或跨子模推导作者的 $\mathcal M$ 是否分裂。

因此准确分界为：**“该列及其模的代数机制”已标准；“实际几何为什么恰留下该列而未留下
能改变余核的其他方向”仍要靠作者实际复形及整数消元。**
这给具体实现留出窄残余，并没有使计算本身升格为新的 Pascal/Jantzen 理论。

### 4.4 反典范/特征跳变：已有几何现象，不是本算术模的直接先例

Zahariuc 在 Atiyah ruled surface 上有 $K=-2E_\infty$；Proposition 2.2 给
$|nE_\infty|$ 在特征零和特征 $p$ 中的不同维数。因此反典范倍数截面的特征依赖已有先例。
其 Theorem–Example 0.1 又给 fat-point 线性系统在特征零空、特征 $p$ 非空的明确例子。
这里使用该版本已经证明的结论，不把该版本的 conjecture 转述成截至 2026 年仍未解决。
[Zahariuc，Introduction 与 §2.1](https://arxiv.org/html/1711.09323v2)

这些是其他曲面及域上线性系统的结果；不是当前有理八次吹起族的余核，也没有直接识别
$\operatorname{Fitt}_3H^1=\tau^5(\tau,2)$。本例的单纤维维数相同而厚度不同，确实比单纯
“维数随特征变”更具体；但该厚度差异在孤立列层面已被 (P1) 完整解释，不能重复计算新意。

## 5. 按声明扣除后的残余

| 声明 | 必须扣除 | 本轮剩余，不等于已确认创新 |
|---|---|---|
| C1 全次数 actual complex | 相对 fat-point 族、吹起推前、评价复形及整数二项式 jet 是标准构造路线 | 这八个中心与该极化对应的准确 $J_n$、任意基变换及原八组矩阵身份；属于具体实现 |
| C2 三阶 actual 分解 | 单位消元和从二项式矩阵取块不是新方法 | 该具体 $R\Gamma$ 确实留下两个 $\tau^2$ 块及一个受限平移列的准确几何实现 |
| C3 非主 Fitting、扩张、特征指数 | 给定 $\mathcal M$ 后均为标准代数；孤立列本身即 (P1) | 仅保留这些量作为 C2 的内在诊断，不能另列为三项独立创新 |
| C4 首次次数 | 二项式系数的素数整除现象早已存在 | 只对已比较的 $q=1,n\le3$ 范围成立；所有素数/所有次数模式不是当前结果 |

这是一件可作为精确算术几何例子保存的材料，或未来更强族内结构定理的基准例子。
现有有界证据不足以支持“只靠这个三阶块就有独立长文”的定位；即使具体块未在所读原文逐字出现，
也不等于重要性门槛已过。全次数实际矩阵提供继续研究的对象，不等于全次数结构定理已经建立。

## 6. 保留的科学与授权边界

1. 原 $F_{\tau=0}$ 的非主导塌缩 caveat 保持：光滑曲面族及反典范层的延拓，
   不自动使原离散映射在 $\tau=0$ 延续为双有理动力系统。不得借用另一个周期三极限映射替换原模型。
2. 不重新计入 Harbourne 维数/固定部或 TVV 有限生成等旧已完成部分；旧 unit-family C1 的结论域也不扩大。
3. 有限素数样本不证明 $n=p+1$ 首现规律；Pascal 类比也不证明这个规律在全次数 actual $J_n$ 中成立。
4. 本轮未输出正式分数、PASS/FAIL 数学审查票或“全球无先例”；没有建立 Paper30 项目或稿件。
5. 本报告依照有界查新停止条件收束。输入科学正确性由其专门核查承担，
   进一步独立长文定位需更强的族内结果及对该新增结果的相应查新，不能用本预筛提前代签。
