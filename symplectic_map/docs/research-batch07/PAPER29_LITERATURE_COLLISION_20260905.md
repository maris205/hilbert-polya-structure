# Paper29 候选：一手文献碰撞与可保留差量

日期：2026-09-05。对象：当前 separated Hamiltonian product-shear 辛映射族。  
性质：有界、独立的文献审查；不是正式 candidate PASS，不是 Route A/B 评价，不是证明或 PDF 验收。  
route_applicability: NOT_APPLICABLE  
评估输入：主代理给出的原候选，以及本次审查期间补充的“每个动量碰撞分层的精确固定域”强化命题。没有审阅完成版论文。

## 1. 结论先行

1. **原拟无周期仿射代数曲线定理已有更一般的直接前例。** Abboud 的最新 arXiv:2311.18381v3（2026-06-17），Proposition 13.20，纸面页 149–150，覆盖任意 normal affine surface 的 loxodromic automorphism。对任意正迭代同样适用。不能把本候选的 repeated-root Danielewski 情形作为该结论的新推广。
2. **剪切公式、Danielewski 商、torus grading、Cox lifting 和齐次因子对应除子均已有成熟前例。** “将这些工具组合，推出泛动量纤维不存在额外有理积分”有证明价值，但单凭此不足以稳健地主张高新颖性。
3. **强化后的全纤维命题是当前可保留的主要差量：** 动量值相等关系若有 $s$ 个块，则该纤维每个 $F^N$ 的完整有理固定域恰由块内坐标比值生成，超越次数为 $r-s$。本次定向一手检索未找到同等完整分类，但这只是有限检索结果，不是优先权证明。
4. **最强异议仍成立：** 审稿人可以把全纤维结论视为“标准块消元 + 已知仿射曲面动力学 + 标准齐次除子论证”的具体应用。真正需要展示的是所有退化分层、primitive character/gcd、非自由商纤维都被统一处理，而不是给熟悉机制换名字。
5. 建议：原泛纤维版不应单独作为强新论文卖点；全分层完整固定域版可继续做有界证明审查。不得因本报告未找到精确前例而写“first”“全新方法”或授予任何评分门槛 PASS。

最近前例及原文：[Abboud v3](https://arxiv.org/pdf/2311.18381v3)、[Cox realization/lifting 原始论文](https://arxiv.org/html/0810.1148v1)、[2026 trinomial LND 分类](https://arxiv.org/html/2605.17670v2)。

## 2. 审查中的候选命题及版本区别

取 $r\ge3$，$Q=\prod_iq_i$，$P=\prod_ip_i$，$F=T_g\circ S_f$，其中剪切来自
$V=f(Q)$、$W=g(P)$，$f,g\in\mathbb C[t]$ 均非恒定。记
$c_i=q_ip_i-q_rp_r$，并约定 $c_r=0$。

### 2.1 原候选 A：全空间与简单动量纤维

对每个 $N\ge1$，

$$
\mathbb C(q,p)^{F^N}=\mathbb C(c_1,\ldots,c_{r-1}),\qquad
\mathbb C[q,p]^{F^N}=\mathbb C[c_1,\ldots,c_{r-1}].
$$

简单动量意为 $c_1,\ldots,c_r$ 两两不同；其纤维 $M_c$ 到
$D_h=\{QP=h(x)\}$，$h(x)=\prod_i(x+c_i)$ 的映射拟为全局
$(\mathbb C^*)^{r-1}$-torsor。还拟排除非平凡多项式特征函数。
无周期曲线、次数增长等属于证明输入，不应作为独立原创主张。

### 2.2 审查期间强化 B：所有动量纤维

把指标集按 $c_i=c_j$ 分为 $s$ 个块 $I_a$，每块选代表 $j_a$。
拟证明对每个 $c$ 及每个 $N\ge1$，

$$
\mathbb C(M_c)^{F^N}
=\mathbb C\!\left(q_i/q_{j_a}:i\in I_a\setminus\{j_a\},\ a=1,\ldots,s\right),
\qquad
\operatorname{trdeg}_{\mathbb C}=r-s.
$$

这不是 A 的自动特化：固定域一般不与退化特化交换。块内比值“确实不变”只给包含关系；
反向包含、所有正迭代，以及非简单纤维上的附加积分穷尽性才是实质内容。

据主代理的证明方案，固定上述比值、令 $K$ 为其有理函数域后，出现

$$
K[M_s]=K[x,u_1,v_1,\ldots,u_s,v_s]/(u_av_a-x-d_a),
\qquad d_a\ne d_b,
$$

以及 $Q=Z\prod_au_a^{n_a}$、$P=Z^{-1}\prod_av_a^{n_a}$，其中
$n_a=|I_a|$、$Z\in K^*$。若 $e=\gcd(n_1,\ldots,n_s)$，
primitive vector 为 $\alpha_a=n_a/e$。此时连接 torus
$H=\ker(\prod t_a^{\alpha_a})$ 的商拟为

$$
UV=\prod_a(x+d_a)^{\alpha_a}.
$$

这是新的待审证明输入，不是本报告已经验证的定理。该商可能有有限非平凡 stabilizer；
不得继续称它为每点自由的 torsor。

## 3. 最大碰撞：无周期曲线已经属于已有定理

Abboud v3 的 Proposition 13.20 只要求曲面 normal affine、映射 loxodromic，
不要求光滑或定义多项式无重根；Remark 13.21 将其定位为对 Bedford–Smillie
平面结论的推广。该论文初稿为 2023-11-30，2024-02-06 有 v2，
2026-06-17 的 v3 修正若干证明并增加中间结果；这里以 v3 为引用依据。
初稿相应编号为 Proposition 14.19。arXiv 页面没有核实到正式期刊卷页，
应标注为预印本，而非把“经历 review”写成已发表。[原文及版本](https://arxiv.org/abs/2311.18381)

与候选的对应是审查者的推论：

- $QP=h(x)$ 对非零非恒定 $h$ 是 normal affine surface；$h$ 有重根不破坏 normality。
- 如果已经证明候选商映射的第一动力次数
  $\lambda_1=(r\deg f-1)(r\deg g-1)>1$，它即为 loxodromic。
- 每个正迭代仍为 loxodromic，故无周期曲线。

normality 也可直接在 Liendo–Regeta–Urech 引言看到：其 $n=1$ 的
Danielewski 曲面始终 normal；该文不是无周期曲线定理的来源。
[Liendo–Regeta–Urech 引言与 Theorem 1](https://arxiv.org/html/1905.00423v2)

因此候选的无穷远极点阶数证明，可以作为自包含、便于辛映射读者验证的证明；
但应明确说其结论被上述一般定理覆盖。低技术证明的简化价值需要实际比较篇幅、
假设和可复用性，不等于结论优先权。

## 4. Cox/torsor 机制：已知多少，尚余多少

Arzhantsev–Gaifullin 的原始论文直接研究 factorially graded affine variety 的
quasitorus 商、齐次元与有效 Weil 除子的对应。Theorem 4.1 对不收缩除子的
商给出 Cox realization 的泛性质；Theorem 5.1 给出 automorphism lift 的正合列
$1\to N\to\widetilde{\mathrm{Aut}}(R(X))\to\mathrm{Aut}(X)\to1$。
这是本候选除子机制的近前例，不宜只引用泛泛的 torus quotient 背景。
其定理没有直接写出候选 $F^N$ 固定域。[原始论文 §§4–5](https://arxiv.org/html/0810.1148v1)

Bellamy–Craw–Schedler Theorem 1.1/3.2 在适当 linearisation 假设下识别
Cox ring 与 stable locus 的 semi-invariant ring，Example 4.4 包括 hypertoric
情形。它是几何结构定理，不是“任一具体循环自同构提升的固定域为空”的定理。
特别是 Example 1.2 说明不能随意把 stable locus 的函数环换成整个源的函数环。
[原文](https://arxiv.org/html/2404.12225v1)

### 4.1 最短的一般性反对论证

下述是审查者对候选证明结构的抽象化，不是声称已在某篇文献找到的原文定理：

设 $A$ 是有限生成 UFD，$A^*=K^*$，一个 split torus $H$ 正则作用于
$Y=\operatorname{Spec}A$；$\Phi$ 与其作用交换。若商 $\pi:Y\to X$
有足够好的几何轨道纤维，使每个非空真 $H$-齐次主除子都降到 $X$ 上的非零有效除子，
而 $\bar\Phi^N$ 没有周期除子，则：

1. $\Phi^N a=\lambda a$ 的齐次分量仍是同特征值的特征函数。
2. 任一非常数齐次分量的零除子降到一个周期有效除子，矛盾。
3. 所有多项式特征函数都是常数。
4. 对既约分式 $a/b$，$\Phi^N(a/b)=a/b$ 与 UFD/常数单位群使 $a,b$
   成为同特征值特征函数，故 $\operatorname{Frac}(A)^{\Phi^N}=K$。

这说明“weight decomposition + divisor descent”本身是一个短而标准的组合，
难以作为方法层面高新颖性支柱。候选 B 的实际差量在于：能否对每个碰撞分层
找到正确 $A,H,\pi$ 并完全核实这些条件，且最终明确回到原辛映射变量。

不能删掉关键假设。例如 $Y=\mathbb A^2\times\mathbb G_m$，
$\Phi=(\text{Hénon},\mathrm{id})$，底曲面没有周期曲线，但上面仍有不变量 $t$。
此例的单位群非恒定。单凭“底层无曲线”或“generic torus fiber”不能证明提升固定域。
非自由商还必须排除被商映射压缩到点的上层除子。

## 5. 一手来源表：15 个定向工作，不作大规模下载

表中“读到”表示实际核对的层级，不把只读摘要算作通篇审阅。来源均为作者原文、
arXiv 或正式出版页面；检索出现的二手摘要站、ResearchGate 自动摘要和会议摘要册
仅作为定位线索，不承担技术结论。

| 工作 | 年代／发表状态 | 实际读到 | 与候选重叠及精确差别 |
| --- | --- | --- | --- |
| Marc Abboud, On the dynamics of endomorphisms of affine surfaces | 2023 初稿；2026-06-17 v3，预印本 | 引言、主定理摘要、Prop.13.20 及证明 | 直接覆盖所有 normal affine loxodromic 商的无曲线结论；不写原辛映射全纤维固定域。[arXiv](https://arxiv.org/abs/2311.18381) |
| Matthias Leuenberger, Andriy Regeta, Automorphism Groups of Danielewski Surfaces；相关正式论文 Vector Fields and Automorphism Groups of Danielewski Surfaces | 2017 预印本；正式题名 IMRN 2022(6),4720–4752，online 2020 | 预印本引言、Thm.1–2、Prop.3；正式摘要与元数据 | 相反 triangular $\mathbb G_a$ 子群及 free-product 结构已知；研究群/Lie 代数识别，不给此 $F^N$ 固定域。正式版题名与初稿不可混写。[初稿](https://arxiv.org/html/1710.06045v1)、[正式版](https://doi.org/10.1093/imrn/rnaa189) |
| Rafael B. Andrist, Frank Kutzschebauch, Andreas Lind, Holomorphic automorphisms of Danielewski surfaces II—structure of the overshear group | 2011 预印本；J. Geom. Anal. 25 (2015),1859–1889 | 引言、Def.1.2、主 Thm.5.1 | 剪切/overshear 公式及 amalgam 先例；所读主定理要求 $\deg p\ge4$，不能误记成本文所有 $r\ge3$。不处理具体提升的完整不变量。[原文](https://arxiv.org/html/1106.4580v1)、[DOI](https://doi.org/10.1007/s12220-014-9496-z) |
| Adrien Dubouloz, Pierre-Marie Poloni, On a class of Danielewski surfaces in affine 3-space | 2006 预印本；J. Algebra 321(7) (2009),1797–1812 | 摘要、引言、主问题范围 | 更一般 $x^nz=Q(x,y)$ 的同构、自同构及嵌入；不是本文循环固定域结论。不可把所有 Danielewski 分类当作直接动力学结论。[原文](https://arxiv.org/html/math/0602549v1)、[正式版](https://doi.org/10.1016/j.jalgebra.2008.12.009) |
| Alvaro Liendo, Andriy Regeta, Christian Urech, On the characterization of Danielewski surfaces by their automorphism group(s) | 2019 初稿、2022 v2；Transformation Groups，online 2020 | 引言、Thm.1–2 | 明确 $xy=p(z)$ 始终 normal；群识别与 root subgroup 背景，不是周期曲线或积分完备性。[原文](https://arxiv.org/html/1905.00423v2)、[DOI](https://doi.org/10.1007/s00031-020-09606-z) |
| Matthew Arbo, Nicholas Proudfoot, Hypertoric varieties and zonotopal tilings | 2015 预印本；IMRN 2016(23),7268–7301 | 引言、定义、构造范围与脚注 | Hamiltonian torus quotient 是既有几何框架；非零复动量参数通常不再有文中 conical 定义所需的 $\mathbb G_m$ 作用，不应笼统称所有纤维 conical hypertoric。[作者稿](https://pages.uoregon.edu/njp/zt.pdf)、[正式版](https://doi.org/10.1093/imrn/rnw005) |
| Ivan V. Arzhantsev, Sergey A. Gaifullin, Cox rings, semigroups and automorphisms of affine algebraic varieties | 2008 预印本；Sb. Math. 201(1) (2010),1–21 | 引言、Thm.4.1、Thm.5.1、相关证明 | 对齐次除子和 lift 的最强机制前例；无“不变量场恰为所有碰撞比值”的具体结论。[原文](https://arxiv.org/html/0810.1148v1)、[出版记录](https://www.mathnet.ru/eng/sm7370) |
| Gwyn Bellamy, Alastair Craw, Travis Schedler, The semi-invariant ring as the Cox ring of a GIT quotient | 2024-04-18 预印本，未核实正式卷页 | 引言、Thm.1.1/3.2、Ex.1.2/4.4 | Cox/semi-invariant ring 识别和 hypertoric 范围；未宣称具体自同构固定域平凡。[原文](https://arxiv.org/html/2404.12225v1) |
| Veronika Kikteva, On the connectedness of the automorphism group of an affine toric variety | 2024；Sb. Math. 215(10),1351–1373 | 引言、Cox 章节及引用的正合列 | 说明 lifting/gradings 在当前文献仍是标准工具；其主问题是 connected component，不是积分穷尽性。[原文](https://arxiv.org/html/2409.10349v1)、[正式版](https://www.mathnet.ru/eng/sm10080) |
| Timofey Krasikov, Kirill Rassolov, $\mathbb T$-homogeneous locally nilpotent derivations of trinomial algebras | 2026-05-17 初稿、05-19 v2，预印本 | 引言、Type1 定义、Thm.2.2、Thm.4.1 范围 | $u_av_a-u_bv_b=d_a-d_b$ 属 Type1 表述；齐次 LND/replicas 不是新机制。它分类单个连续流，不给本候选固定复合字全部迭代的积分分类。[原文](https://arxiv.org/html/2605.17670v2) |
| Mikhail Ignatev, Timofey Vilkin, On flexibility of trinomial varieties | 2025 预印本；Mediterr. J. Math.23,70，2026-02-26 发表 | 引言、Thm.2.6、出版元数据 | 分类若干 trinomial flexible 族；全 $\mathrm{SAut}$ 的轨道/不变量不等于一个循环子群的不变量。[原文](https://arxiv.org/html/2506.20524v1)、[正式版](https://doi.org/10.1007/s00009-025-03037-4) |
| Sergey Gaifullin, Generically flexible affine varieties with invariant divisors | 2025 预印本；Indagationes Mathematicae online 2026-03-05，所见出版页标 In Press | 引言、FML/ML 定义、主构造范围 | 即使全群有开轨道，边界仍可含 invariant divisors；提醒不能把 flexibility 当某个映射无周期除子的证明。[原文](https://arxiv.org/html/2507.14745v1)、[出版页](https://doi.org/10.1016/j.indag.2026.03.002) |
| Neena Gupta, Sourav Sen, A note on double Danielewski surfaces | 2026-04-12 预印本 | 摘要、引言及修正定理范围 | 修正 2403.02876 的同构分类证明及相关自同构表述；不是本文 exact fixed field 的前例，但必须避免引用旧错证明作捷径。[原文](https://arxiv.org/html/2604.10644v1) |
| Polina Evdokimova, Isomorphism classes of multi Danielewski varieties | 2026-07-14 预印本 | 摘要、引言、定义及主问题范围 | 处理 multi Danielewski 的 Makar–Limanov invariant/同构类，不是给定 $T_gS_f$ 的循环固定域。[原文](https://arxiv.org/html/2607.12639v1) |
| Sergey A. Gaifullin, Automorphisms of Danielewski varieties | 2017 预印本；J. Algebra 573 (2021),364–392 | 摘要与出版元数据；未逐定理通读 | 高维 Danielewski 与 torus/LND 相关背景；不能凭摘要排除正文一切间接重叠，已由更近 Type1 文献优先承担机制核对。[arXiv](https://arxiv.org/abs/1709.09237)、[正式版](https://doi.org/10.1016/j.jalgebra.2020.12.032) |

## 6. 定向检索覆盖与失败边界

使用 research-lit 与 novelty-check 技能，按本任务的 web-only / 不扫描旧产物限制执行。
没有批量下载 PDF；只在线打开选中一手全文/HTML/PDF。没有 Zotero、Obsidian 或
所要求的 mcp__codex__codex 可调用工具，因此未执行 GPT-5.4 xhigh 跨模型复审；
本报告是当前独立代理的实际评估，绝不代称该模型意见。ML 会议数据库清单与本纯数学问题
无关，未为形式完整性检索 ICLR/NeurIPS/ICML。

每组至少三个实际检索表述，另加年代窗口。引号表示实际关键词组合，不表示全文引文。

| 核心问题 | 至少三个已执行表述 | 主要结果 |
| --- | --- | --- |
| 商上无周期曲线 | “Danielewski” “periodic curves” automorphism；“affine surface” “loxodromic” “invariant curve”；“Danielewski” “Hénon” invariant | 命中 Abboud 的直接覆盖；转读最新 v3 |
| 全空间/泛纤维完整固定域 | symplectic polynomial map product q_i p_i rational first integrals Hamiltonian shears；“symplectic” “rational invariants” “shears”；“symplectic maps” “complete” “invariant field”；“Danielewski” “fixed field” | 未找到等同完整固定域；大量泛 integrator 或不相关命中排除 |
| torsor/hypertoric/Cox 结构 | “hypertoric” automorphism “invariant” “torsor”；“hypertoric” “principal” “bundle” moment map；“Danielewski” “universal torsor”；“hypertoric” “Cox ring” | Cox 与 hypertoric 文献覆盖结构，不等同离散 fixed field |
| 提升后的 eigenpolynomial/除子完备性 | “Cox ring” automorphism “rational invariant”；“torus” “torsor” automorphism “invariant rational functions”；“Cox rings” “automorphisms” “invariant divisors”；“factorial” “torsor” “dynamics”；“universal torsor” “automorphism” “periodic” | 命中原始 lifting/不收缩除子机制；未找到具体循环 fixed-field 总定理 |
| 每个碰撞分层与块内比值穷尽性 | “symplectic” “momentum” “collision” “rational integrals”；“Danielewski” “ratios” automorphisms；“momentum fibers” “rational” “invariants”；“collision” “fixed field” polynomial automorphism；“trinomial” “shears” “invariants” | 未命中精确分类；转查 trinomial/齐次 LND 术语 |

2024–2026 的显式关键词检索包括 Danielewski automorphism rational invariant、
Hamiltonian shear invariant、symplectic map rational first integrals、trinomial varieties
automorphisms、invariant rational functions Cox。另执行截至 2026-09-05 最近约六个月的
recency=184 检索，以及 after:2026-03-05 before:2026-09-06 表述，搜索 arXiv 的
Danielewski、hypertoric automorphisms、trinomial automorphisms 和 Cox invariants。
由此补入 Abboud v3、Krasikov–Rassolov、Gupta–Sen、Evdokimova；Ignatev–Vilkin
正式发表日期为 2026-02-26，略早于六个月窗口，但属于 2024–2026 覆盖。

年代过滤依赖搜索引擎索引，结果中存在把旧文重新抓取日期显示为近期的情况，
因此以 arXiv submission/version history 或出版页为准。不能声称已经逐日检查最近六个月
全部 arXiv 投稿。Google Scholar / Semantic Scholar 的索引入口有被常规 web 搜索覆盖，
但没有它们的独立 API 或完整检索导出，故不宣称多数据库系统综述。

## 7. 候选 B 应当回答的证明问题

以下是决定它是否有独立内容的具体审查问题；不是要求扩张成抽象曲面自同构项目：

1. 每个 $M_c$ 的函数域合法性与整性。重根时不能把简单动量纤维的 UFD 证明原样复用。
2. 块内比值的代数独立性，以及固定比值后 $K[M_s]$ 的严格识别；不能只在
   $Q\ne0$ 的坐标图上证明，再默认所有有理不变量自动延拓。
3. $H$ 必须使用 primitive exponent vector；若直接用 $(n_a)$，$\gcd>1$
   时 kernel 不连接，丢失有限成分可能造成错误固定域结论。
4. 加权商每个几何纤维是否确为单个 $H$ 轨道、维数是否恒定；有限 stabilizer
   的存在不等于失败，但它排除了直接沿用 torsor 说法。
5. $H$-齐次主除子的商像必须是曲线而非点，且闭包和迭代不产生漏项。
   原始 Cox 文献的“uncontracting”条件正是这里的警示。
6. 当 $\sum_a\alpha_a$ 为 1 或 2 时，商多项式不再满足旧“次数至少3”的
   no-curve 初等引理假设；需要单独证明商 loxodromic，然后合法应用 Abboud，
   或给出覆盖这些指数端点的正确直接证明。
7. 对每个 $N$ 的 fixed field，必须处理不可约因子的有限置换；
   polynomial fixed ring 与 rational fixed field 的差别必须清楚。
8. 全空间结论仍需证明 $\mathbb C(c)\cap\mathbb C[q,p]=\mathbb C[c]$，
   而不是仅由“纤维一般”一句话结束。

全纤维比值可能提供“有理积分维数跳跃，而商的正熵动力学仍在”的清晰辛映射解释。
这项解释应紧贴原变量和分裂 Hamiltonian 的对称性，不靠另起抽象几何选题来填充正文。

## 8. 暂定价值评估与定位

下面是选题阶段的主观粗评，允许约 ±1 分误差；不是锁定 rubric、不是验收阈值，也不把
尚未验证的强化命题计为已证成果。

| 版本 | 文献差量新颖性 /10 | 问题价值 /10 | 证明问题状态 |
| --- | --- | --- | --- |
| A：全空间/泛简单纤维 fixed field，配 no-curve 与标准商结构 | 4.5 | 6.0 | 机制清楚，明显依赖已有一般结果；缺少足以支持独立长文的稳健差量 |
| B：所有碰撞分层、所有正迭代、明确全部比值生成元 | 6.5 | 7.0 | 有一个清晰完整分类问题；非自由加权商、gcd 与全分层穷尽性仍待独立证明审查 |

建议定位为：对于一个明确、任意维数和任意非恒定 $f,g$ 的 separated product-shear
辛映射族，完整分类全空间与所有动量纤维的有理积分，精确说明参数碰撞导致的积分增加。
“no hidden integrals”可作结果解释，但必须指明函数类是 rational、并给全纤维定理的
严格量词；不能等同于任意解析意义的非可积性。

建议最终文献段直接承认三层已有工作：
Danielewski triangular dynamics 的构造来源；Abboud 的一般无曲线定理；
Cox/graded divisor lifting 的机制来源。候选的差量只放在精确的辛映射积分分类与
碰撞分层上。若强化 B 的剩余证明失败或只能回退到 A，应重新判断是否值得独立成篇，
不能用重复根 no-curve、Noether 公式或已知动力次数补足新颖性。

最终建议：PROCEED WITH CAUTION（仅对 B 的有界证明继续有效）；没有授予 candidate PASS。
