# Paper30 qPI：整除状态一形式垂直厚化的有界原始文献预筛 V1

日期：2026-09-09。执行者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
类型：P03 新问题的有界 primary 包含预筛；不是作者证明、数学核查票、正式新意分数或立项。
`route_applicability: NOT_APPLICABLE`。
本轮亲读 `research-lit`；五个定向查询后，只核四组最接近原始来源的必要段。
旧报告全部冻结。本轮只新写本件，不改作者输入，不计算原三因子矩阵，不调用外部模型。

## 1. 结论与当前适用层级

**标准临界理想、闭一形式、形式群或有限平坦 torsor 理论，均不能仅凭旧 C3 的模 $\pi$ 信息，
直接宣布本原状态理想为统一的 $(\pi^\kappa,z^{\nu\sigma})$。但“厚度/提升依赖”本身也不是新机制。**

当前可以确定的扣除有四层：

1. 系数理想就是向量丛截面的标准零概形，并可写成余核的 Fitting 理想；
   先除公共 $p^a$ 因子，不等于做 $\pi$-饱和。
2. higher Hasse–Witt 的旧模 $p$ 乘子已被直接包含，不重开；
   Vlasenko 同文的 Theorem 2 还提供不要求 ordinary 的整形式群构造，
   不能说超奇异层只有模 $p$ 理论。
3. Lubin–Tate 已分类固定有限高度剩余形式群的提升；高度二的提升有一个形式参数，
   “同一剩余超奇异对象可以有不同提升”属于标准变形现象。
4. Henrio 的 Kummer/有限平坦退化已经把厚度、different 和特殊微分纳入同一框架；
   但它要求实际有限覆盖及相应约化假设，不直接识别当前曲面上两方向的 $p^{-a}dI_r$。

尚未由所读原文直接给出的，是**原固定 $I_r$、完整 $\mathcal U$、两状态方向以及实际 $t$ 提升**
共同决定的完成局部理想。未取得直接包含，不等于全球无先例或独立长文门槛已过。

任务进行中，主控报告了 $p=3,a=m=1$ 的原对象首诊断正向信号：光滑 Hasse 根处，
torus 上首个切向 $\pi$-jet 非零，作者据此预期局部理想为 $(\pi,J-h)$。
这是**尚未绑定作者证明文件、尚未独立接受的作者通信**；本报告不核算、不投票，
也不把一般反例套到这个 actual 结果上。若该信号及末端图身份最终成立，
“简单零点 + 切向首阶单位 $\Rightarrow(\pi,z)$”是标准局部消元；
残余工作是原对象中这个非零单位及其全图覆盖的准确识别。

## 2. 输入身份、对象和声明边界

| 冻结输入 | 本轮实际读取 | SHA-256 |
|---|---|---|
| [POST_INTEGRAL_IDEATION_PROPOSALS_V1](PAPER30_QPI_POST_INTEGRAL_IDEATION_PROPOSALS_V1_20260909.md) | §2 共同对象、P03 全条；用索引确认其与 P09 的区别，不消费其他提案 | `3b41f2fb34ac6652c2e452493308dd85f934512e4ef87f7204d2225e209e16d9` |
| [INTEGRAL_CANDIDATE_BRIEF_V1](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | §2 原中心、末端图、矩阵与积分规范；§3 C2/C3 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| [DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md) | 全文读取，复用已完成的 Hasse/Cartier/Dwork/Witt 扣除 | `8d24144c5e49ba30402a2749536ec0b66ca6170d6dcf9a85273330829c22a88f` |
| [INTEGRAL_NOVELTY_PHASE_B_V1](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md) | 针对问题检索来源索引，并读取 §5.3 的 C3 对照；不重载整个旧研究账本 | `44f628fbc07cad422f83c136cf1dd3fb2bae9d7a7782db3798a073b5ab1bdf41` |

保留原单位时间族；不引入此前 $\tau=0$ 非单位时间构造。沿用
$r=mp^a$、$p\nmid m$、$N=p^a$、$q=s=\zeta_r$、圆分 DVR $\mathcal O$、参数 $\pi$、
$e=v_\pi(p)$ 及任意 $t\in\mathcal O^*$。$d$ 固定 $s,t$，只微分原状态。

$$\alpha=p^{-a}dI_r,\qquad
\bar\alpha=H_p(T,J;\varepsilon)^\sigma dJ,\qquad
\sigma=1+p+\cdots+p^{a-1},\quad T=\bar t^m.$$

研究位置是小阶完整纤维 $X_h=(J=h)$ **光滑**且 $H_p(T,h;\varepsilon)=0$ 的点，
包括四条完整末端线。$\mathcal U$ 的完成局部自由微分模秩为二。
写成 $\alpha=A\,dz+B\,dw$ 后，待识别对象是

$$\mathfrak a=\mathfrak c(\alpha)=(A,B),$$

而不是单个分量的赋值、特殊纤维的根集、谱曲线形式群的一个系数，或被饱和后的不同理想。
在光滑能级，$dJ$ 不消失，所以旧 C3 只给
$\mathfrak a\bmod\pi=(z^{\nu\sigma})$，相差局部单位；它没有给 $B/\pi$ 的首项。

本轮分开筛查三项，均不预置数学结论：

- **V1：统一模型是否成立。** 原完整完成局部理想是否统一同型于
  $(\pi^\kappa,z^{\nu\sigma})$？$\kappa$ 是否沿光滑 $X_h$ 恒定？
- **V2：若不统一，真正首个差额是什么。** 共同高阶理想如何依赖纤维状态、单位 $t$ 的提升、
  坐标/微分标架；哪些差异在合法形式坐标变化后仍存在？
- **V3：先诊断的实际范围。** $p=3,a=m=1,q=\zeta_3,\bar t=1,h=1$，
  比较 $t=1$ 和 $1+\pi$；$J=y+x/y-x-1/x$、$H_3(T,h)=h^2-T$。
  光滑性及该 Hasse 式来自提案输入，不在本预筛重新证明。

这里的 $\kappa$ 是提案中的厚度指数，勿与 brief 用作剩余域符号的 $\kappa$ 混淆。
圆分参数 $\pi$ 保持实际规范；更换其单位倍不应被误记为几何厚度变化。

## 3. 有界检索记录与访问缺口

| 编号 | 实际 query | 有效发现或局限 |
|---|---|---|
| Q1 | `"mixed characteristic" "critical locus" differential ideal` | 未取得直接分类原两方向理想的可用命中；后用 Stacks 原定义核标准对象身份 |
| Q2 | `"Hurwitz" "differential" "thickness" Henrio` | 命中 Hurwitz differential/thickness 的相邻学位论文入口，也有无关噪声；随后直接按已知 Henrio 原文标识定位核验，不冒称搜索已直接命中原文 |
| Q3 | `"finite flat" "torsors" "differential" "mixed characteristic"` | Saïdi 度 $p$ 混合特征覆盖入口；搜索摘要不承担结论。有限平坦模型最终由 Henrio 原文承担 |
| Q4 | `"higher Hasse" "formal group" supersingular deformation` | Vlasenko 正式刊本、Ditters 1989 原文元数据，以及许多二手形式群页面 |
| Q5 | `site:arxiv.org Henrio Saidi "mixed" "torsors"` | 返回其他 motivic/reductive torsor 结果，未得到目标新命中；按五 query 上限收束 |

之后只打开准确原文/官方元数据和必要段，未继续同义搜索。Lubin–Tate 的经典原论文
按明确题名与官方 Numdam 标识直接定位，核验作者、年份、卷页和 Theorem 3.1。

可调用工具没有 Zotero/Obsidian 文献检索接口。检查相关本地 PDF 文件名及脚本路径，
未找到命名匹配的 Cartier/Hasse/Hurwitz/Lubin/形式群文献或 `arxiv_fetch.py`，
故使用 arXiv 网页 fallback；未重新通扫已有批次 PDF。未作新的 Google Scholar/
Semantic Scholar 直接查询，也不把旧轮拒绝访问计作本轮成功检索。

Ditters, *On the classification of commutative formal group laws over p-Hilbert domains and a finiteness
theorem for higher Hasse-Witt matrices*, Math. Z. 202 (1989)，本轮只得到
[出版社预览/元数据](https://doi.org/10.1007/BF01180685)；EuDML 打开失败，未读定理。
因此它是明确未补齐的近邻，不用于宣布 higher-Hasse 全部理论已经排尽。
Saïdi 搜索发现页未作原文精读，亦不进入数学判据。

Lubin–Tate 最初猜测的 `item/BSMF...pdf` 路径失败；随后官方原 PDF 成功打开并获得页码文本，
没有本地下载。截图接口未能解析该 PDF，故本轮以原 PDF 抽取正文核必要陈述，
不声称完成图像级或全文证明核验。Henrio 原 HTML 及 PDF 均可读。

## 4. 四组已读原始来源与准确包含边界

| 来源、状态与必要 read range | 已有结果/工具 | 本题尚需的实际识别 |
|---|---|---|
| The Stacks Project，在线原始证明参考；[Differentials, 00RM](https://stacks.math.columbia.edu/tag/00RM) 的 Lemma 10.131.7、10.131.12；[Fitting ideals, 07Z6](https://stacks.math.columbia.edu/tag/07Z6) 的 Lemma 15.8.2–4 与定义。访问日 2026-09-09 | 微分正合列、Fitting 的表示独立性及任意基变换 | 不能从理想的标准身份推断它在本原函数处的生成元或正规形 |
| Masha Vlasenko，*Higher Hasse–Witt matrices*，Indag. Math. 29 (2018), 1411–1424；[v3](https://arxiv.org/html/1605.06440v3)。**新增读取** §1 Theorem 2 前后及 §4 完整证明段；Theorem 1(i) 的旧模 $p$ 段只复用旧扣除 | Laurent 多项式系数序列构造整形式群；Theorem 2 不以 Hasse 可逆为假设 | 谱系数形式群与原曲面两方向 $p^{-a}dI_r$ 的完成局部理想并未自动相等 |
| Jonathan Lubin–John Tate，*Formal moduli for one-parameter formal Lie groups*，Bull. Soc. Math. France 94 (1966), 49–59；[官方原 PDF](https://www.numdam.org/article/BSMF_1966__94__49_0.pdf)。读 p.49 的问题/等价定义，p.50 Proposition 1.1 陈述，p.56 Theorem 3.1 陈述 | 固定高度 $h<\infty$ 剩余形式群的带标记提升由 $h-1$ 个参数分类；提升依赖是既有一般结构 | 高度二仅说明有一个变形参数，不说明原 $t$ 是该参数，也不把这个参数等同于 $\mathfrak c(\alpha)$ 的厚度 |
| Yannick Henrio，*Arbres de Hurwitz et automorphismes d'ordre p des disques et des couronnes p-adiques formels*，[2000 v1](https://arxiv.org/abs/math/0011098v1)。arXiv 标注待刊 Compositio，本轮不另核刊本卷页。读引言、§§1.1–1.4 至 Proposition 1.6、Definition 1.9，§2 Definitions 2.1–2.3 | 度 $p$ Kummer 退化、有限平坦 $\mathcal H_n$ 模型、different 及 exact/logarithmic differential 数据、Hurwitz 厚度条件 | 当前 $f_r:\mathcal S\to\mathbb P^1_{\mathcal O}$ 是相对一维纤维的 fibration，不是已识别的度 $p$ 有限 torsor；无原两方向理想的直接比较态射 |

### 4.1 系数理想属于标准临界/Fitting 构造

在一个光滑局部图上，把 $\alpha$ 视为 $\mathcal O_{\mathcal U}\to\Omega^1_{\mathcal U/\mathcal O}$
的截面映射；其余核有两生成元一关系列向量表示，所以

$$\mathfrak c(\alpha)=\operatorname{Fitt}_1(\operatorname{coker}\alpha).$$

对 $f_r=I_r$，相对微分正合列给 $dI_r$ 的同类表示，故在原局部环上

$$\operatorname{Fitt}_1\Omega^1_{\mathcal U/\mathbb A^1_{\mathcal O}}
=(p^a)\,\mathfrak c(\alpha).$$

这是按 Stacks 原定义对现有输入作的透明识别，不是新 qPI 定理。
在完成环上使用完成的有限微分模/连续微分，不能偷换成不受连续性约束的所有抽象微分。
扣掉已知公共因子保留了残余垂直结构，而 $\pi$-饱和可能把这些结构删除；两者不可混同。
[微分正合列](https://stacks.math.columbia.edu/tag/00RM)，
[Fitting 的表示独立及基变换](https://stacks.math.columbia.edu/tag/07Z6)

### 4.2 形式群并非只有 ordinary 理论，但对象比较不能省略

Vlasenko Theorem 2 用 $l(\theta)=\sum_{j\ge1}\beta_j\theta^j/j$ 定义形式群，
在适当 Frobenius lift 条件下证明其整性；§4 使用函数方程方法。
其 ordinary 假设属于旧 unit-root 逆矩阵部分，不能搬来排除 Theorem 2。
而且可以先在 $\mathbb Z[T,h]$ 的通用参数环构造整形式群，再特化到分歧圆分 DVR；
不能仅以 DVR 本身缺少指定 Frobenius lift 就否定这条基变换路线。
[Theorem 2 与 §4](https://arxiv.org/html/1605.06440v3#S4)

不过，形式群参数 $\theta$ 是其单位截面附近的群坐标，不是原状态能级坐标 $z$ 或纤维坐标 $w$。
即使另行完成谱形式群与实际 Jacobian 的识别，仍须给出把其具体态射/微分运输到原 $\alpha$
的箭头，且保持两系数理想与 $\pi$ 厚化。当前所读定理没有提供这个箭头。
旧 C3 识别实际 Jacobian 的 Hasse 值，也不是该更强的整局部识别。

Lubin–Tate Theorem 3.1 对固定剩余形式群给出提升参数及带标记等价的唯一性。
所以同一剩余对象有多个提升并不新，且改变坐标与改变提升需区分；高度二不意味着唯一提升。
反过来，它也不说任意一个从该曲面写出的状态一形式的零理想都只由这一个参数决定。
当前 $t=1$、$1+\pi$ 是否改变原理想，不能只用“变形空间维数一”代答。
[Lubin–Tate，p.49 与 Theorem 3.1](https://www.numdam.org/article/BSMF_1966__94__49_0.pdf)

### 4.3 有限平坦退化已有厚度与函数数据，仍须原覆盖身份

Henrio 的基环是完备混合特征 DVR，含本原 $p$ 次单位根，剩余域在所读设置中代数闭。
其 Proposition 1.6 处理相对曲线上的非平凡 étale $\mu_p$ 泛纤维 torsor，
并要求指定正规化的特殊纤维整等条件。退化参数与 different 满足
$\delta=v_K(p)-n(p-1)$；模型还包含函数 $u$，不是仅一个厚度整数。
Definition 1.9 从模型提取 $d\bar u$ 或 $d\bar u/\bar u$，
§2 再组合微分阶、残数与边厚度。不能把这些已有结构包装成新的“微分看见厚度”。
[Henrio，§§1–2](https://arxiv.org/html/math/0011098v1)

当前没有构造这样的有限覆盖及与 $\alpha$ 的比较；$f_r$ 的维数已经不同。
即使选择横截曲线后得到有限映射，也必须证明所选覆盖、群作用、different 和微分数据来自原对象，
并且不会丢掉纤维方向 $w$。一次任意切片的结果不足以识别曲面上的完整理想。
同样，“闭”比上述指定 exact/logarithmic 微分条件弱，不自动提供 torsor。
原任务只允许有限无分歧扩张以定义几何点；不得未经说明把更强基变换中的正规形当作原 DVR 结论。

## 5. 一个仅用于排除形式推理的局部对照

以下是本报告的初等比较例，不是 qPI 作者结果、不是新研究发现，也不反驳主控的 actual 正向消息。
在剩余特征 $3$ 的 $\mathcal O[[z,w]]$ 中令 $J_0=1+z$，取任意 $g(w)$，并置

$$I_g=J_0^3-3J_0+3\pi g(w).$$

于是同时有

$$\bar I_g=\bar J_0^3,\qquad
\alpha_g=\tfrac13dI_g=(J_0^2-1)\,dz+\pi g'(w)\,dw,\qquad
\bar\alpha_g=(\bar J_0^2-1)d\bar J_0.$$

这些形式均闭，且准确具有首诊断 C3 的约化。因为 $J_0^2-1=z(2+z)$，在所研究局部点

- $g=w$ 给 $\mathfrak c(\alpha_g)=(z,\pi)$；
- $g=\pi^{k-1}w$ 给 $(z,\pi^k)$，任意 $k\ge1$；
- $g=w^2/2$ 给 $(z,\pi w)$。

最后一个理想有水平分支，不能同型于任何有限纯垂直厚化 $(\pi^k,z)$。
这个例子只说明：**约化、整除与闭性自身不决定厚度，也不强制纯垂直支持。**
原 qPI 的完整光滑曲面/能级几何、实际积分及全局约束可能排除这些抽象例子；
尤其不以此声称原模型存在水平分支或状态依赖。

在首诊断的简单 Hasse 根处，若作者证明原 $B=\pi b$ 且 $b$ 在该点为单位，
并有 $\bar A$ 为 $z$ 的单位倍，则 $(A,B)=(\pi,z)$。
这一步是标准局部理想消元，既不需要新的 Cartier 定理，也不凭空证明 $b$ 的实际非零性。
一般重根/高 $a$ 情况不在这个简单根观察的量词内。

## 6. 作者进行中消息与差额定位

主控在本轮执行中报告：原 $p=3,a=m=1$ 的 $\alpha$ 可分解为
$(J_t^2-t)dJ_t$ 加首阶 $\pi$ 精确微分及更高项；在其所用参数/辛形式规范下，
光滑根 $h^2=\bar t$ 上首切向 jet 是 $h^3\Omega$。
因 $t$ 为单位，作者称其非零，且两个 $t$ 提升只改变法向项；完整末端图尚在作者工作中。

本预筛只记录这条**非文件化、未经本轮核查的作者状态消息**。不把上述恒等式视为已接受定理，
不覆盖四条末端线，更不外推所有素数、$a,m,t$。
若最终成立，其局部正规形是 §5 的标准单位消元消费者；值得核准的实际残余是：
原三因子矩阵的精确整除 jet、非零切向系数的内在身份，以及完整空间上的一致性。
这可以形成一个有用的低阶实例识别，但本轮不支持仅凭它升级为独立长文。

## 7. 有界处置与停止点

| 候选说法 | 本轮处置 |
|---|---|
| 高 Hasse 次幂或模 $\pi$ 零理想带来新机制 | 旧来源直接扣除；不重开 |
| 已有形式群/Cartier 理论强制当前原理想统一为 $(\pi^\kappa,z^{\nu\sigma})$ | 所读定理未直接提供；抽象约化/闭性不足；仍须实际对象比较 |
| 同一剩余对象的不同提升、厚度依赖本身是新现象 | 一般变形/有限平坦理论已有，必须扣除 |
| 首诊断切向单位一旦出现，$(\pi,z)$ 正规形是新分类定理 | 否；正规形是标准局部消元，原 jet 身份才是待核的具体内容 |
| 已发现全参数状态依赖或已建立全参数统一模型 | 均未建立；本报告不代作者宣布 |

五个 query 与四组必要 primary 已形成所需包含边界，停止继续查新。
没有定位到逐字的 qPI 两方向厚化定理，不构成全球无先例结论；Ditters、专门 Cartier
高维闭形式文献及其他有限平坦高阶分类仍有明确未读覆盖面。
本轮没有建立新的正式候选、分数、数学票、论文或外部发布；只保存这份针对尚未证明 P03 的来源边界。
