# Paper30 qPI 非单位 tau 诊断：有界先例筛查 V1

日期：2026-09-09。执行者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
状态：`BOUNDED_PRIOR_ART_SCREEN_COMPLETE`；不是候选评分、独立证明接受或立项意见。
唯一写入为本文件；旧报告、冻结候选与双票失败处置不变。

## 1. 结论先行

允许参数 $\tau=0$ 确实提出了不同于旧单位基的几何问题，但目前已经识别出的
**特殊纤维全次维数、固定部分和有限生成性，均受到已有一般定理直接吸收**。
给定本轮主控核出的十环及相邻两条 $(-3)$ 曲线配置，
$$h^0(S_{q,0},-nK)=1+\frac{n(n+1)}2$$
是固定部分剥离、Harbourne 消失定理和 Riemann–Roch 的短推论；
反典范类 big 后，Cox 环乃至该反典范截面环的有限生成也是既有结果的应用。
这些不应作为尚未发现的新结构主张，也不因为“所有 $n$／所有特征”就重新计新意。

在本轮实读文献中，尚未找到把指定八截面整数族的首层推送
识别为 $R'[0]\oplus[R'\xrightarrow{\tau(q-1)}R']$ 的定理。
**这只是准确包含关系未建立，不是无先例证明，也不表示该猜想正确或足够成文。**
一般派生基变换、秩跳跃与固定部分工具仍须扣除；首层连接元和整个非单位基上的
高次推送／乘法尚需实际证明，不能由旧单位 C1 或域纤维维数猜出。

另有直接主题近邻 Joshi–Lobb：qPI 的参数趋零与两基点合并早已被研究。
其坐标中的极限是周期三 QRT 映射；本次原 $F_\tau$ 在 $\tau=0$ 却发生像维数下降。
没有给出延拓到零参数的曲面同构之前，既不能说两者完全相同，亦不能说互不相关。
以下将这一模型识别保留为明确限制，而不凭同名或不同坐标作全局首创结论。

## 2. 对象、证据与四项准确比较单位

实际读取[整数 brief §2.1](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)，
保持四簇 $1+2+3+2=8$ 个有序中心，仅把基改为
$$R'=\mathbb Z[q^{\pm1},\tau],\qquad L=\omega^{-1}_{S/R'}.$$
第二簇的末中心为 $xy=\tau$，第三簇为 $x^2/y=\tau$；
另两末中心仍为单位坐标 $1,q$。两个 $\tau$ 中心位于不同簇，
不是把原来不同的截面误并为一个中心。旧定义的八分量 $D$ 不能不加论证地
继续充当特殊纤维的完整反典范除子；本轮用 $L=-K$ 标定线丛。

已读取[旧正式处置](PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md)的失败结论和合同；
不重新评分、不恢复旧项目准入。复用[Phase B](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md)
中已核的单位族和标准工具扣除，只补非单位 $\tau$ 空白。
三个本地输入本轮所核 SHA256 分别为：

| 输入 | SHA256 |
|---|---|
| 整数 brief | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| 旧正式处置 | `0452b7aa8f28107ae65f3fa840647806b50eab2502340d1c609a0ca6c545ce90` |
| Phase B | `44f628fbc07cad422f83c136cf1dd3fb2bae9d7a7782db3798a073b5ab1bdf41` |

本轮主控另提供特殊纤维的几何诊断：$D_0=-K$ 是十分量约化环，
两条相邻分量 $A,B$ 满足 $A^2=B^2=-3,\ A\cdot B=1$；
$F=A+B$，$P=D_0-F/2$ 为 nef 且 $P^2=1$。
本报告核先例如何吸收这些诊断的后果，**不代替八中心到该配置的独立证明审查**。
数值 $n\leq8$ 的吻合没有用于下面的文献包含判断。

| ID | 精确比较单位 | 当前证据身份／先例结论 |
|---|---|---|
| T0 | 指定有序吹起在 $R'$ 上仍光滑射影，而 $\tau=0$ 的反典范类非 nef，$D_0=P+F/2$、$P^2=1$ | 几何配置由主控提供；有序吹起族和邻近图退化是已有机制，准确模型仍须核 |
| T1 | 对代数闭域的每个该特殊纤维及 $n\geq0$，$h^0(nD_0)=1+n(n+1)/2$，$h^1(nD_0)=n(n+1)/2$；$|nD_0|$ 的固定部分为 $\lceil n/2\rceil F$（$n>0$） | 给定 T0 和下述 nef 检查，是 Harbourne 的直接应用，不保留为未占据 finding |
| T2 | 该特殊纤维的 Cox 环及 $\bigoplus_{n\geq0}H^0(nD_0)$ 有限生成 | $-K$ big 后由 TVV Theorem 2.9 与分次子环的标准有限生成推得；不是新有限生成定理 |
| T3 | 保留真实基准截面的 $R\Gamma(S,L)\simeq R'[0]\oplus[R'\xrightarrow{\tau(q-1)}R']$，两项在次数 $0,1$ | 派发时明确为未证猜想；本轮没有找到准确包含，也没有证明它；非约化厚度不能从 T1 判断 |

“整个相对反典范环的生成元、关系、乘法及非平坦特化像”目前只是后续问题，
没有给定可检验的完整公式，故不虚构为第五条已成熟主张。

## 3. 实際检索范围与停止边界

亲读 `research-lit` 全文后执行；没有调用正式 Route A/B、novelty 打分或研究评审。
可用并发槽均在执行本轮其他有界任务，未额外创建重叠子任务。
本地 `papers/` 文件名筛查返回项目既有论文／构建 PDF，未发现题名相关外部文献；
未重读无关项目 PDF，也未保存外部 PDF。本地两个 arxiv 技能目录及 `tools/`
没有检得 `arxiv_fetch.py`，按技能退回网页域限定检索。
未配置 Zotero／Obsidian。Google Scholar 与 Semantic Scholar 的直接检索页
在前轮已有不可重试访问拒绝，本轮未再尝试；不能宣称完成两数据库新增扫描。
Consensus 虽有可用入口，本轮未调用；没有冒报 API 检索或引用数量覆盖。

实际执行 24 条 web 查询，前 16 条覆盖五种主要路径，最后八条为元数据核对及
主控给出 big 诊断后新增的有限生成直接先例。以下保留准确字符串：

| 路径 | ID 与实际 query | 结果用途 |
|---|---|---|
| 原 qPI 零参数 | Q01 `"q-Painlevé I" "zero" "blow"`；Q02 `"q-Painleve" "t=0" surface` | 初始结果噪声较多；不以无匹配为无先例 |
| Okamoto／Sakai 退化 | Q03 `"Okamoto" "degeneration" "anticanonical"`；Q04 `"anticanonical ring" "non-nef" rational surface` | Sakai／一般反典范背景入口 |
| 改用规范与作者 | Q05 `q first Painleve initial values space qPI Joshi blowup singularity t zero`；Q06 `"q-Painlevé I" geometry surface` | 定位 Joshi–Lobb |
| 非 nef 与点簇 | Q07 `"clusters" "fat points" "deformation" "rational surface"`；Q08 `"rational surfaces" "anticanonical" "fixed" Harbourne` | Harbourne、固定部分近邻 |
| 无穷近点特化 | Q09 `"clusters" "infinitely near" "specialization" Roé`；Q10 `"fat points" "collision" "flat" "surface" Evain` | Roé 原文及 Evain 发现入口 |
| 近期补查 | Q11 `"q-Painlevé I" "degeneration" after:2024-01-01 before:2026-09-10` | 返回 confluence／其他 qPI 系统；未视为本族精确结果 |
| 准确原文定位 | Q12 `"Varieties of clusters and Enriques diagrams" arxiv`；Q13 `"collisions" "fat points" "Evain" arxiv`；Q14 `"Rational surfaces associated with affine root systems" Sakai pdf` | Roé、Sakai 官方预印本入口；Evain未纳入精读五件 |
| 整数变形空白 | Q15 `site:arxiv.org "anticanonical" "deformation" "cluster"`；Q16 `"fat point" "mixed characteristic" degeneration after:2024-01-01 before:2026-09-10` | 未取得准确整数族定理；这是网页查询，不是 arXiv API |
| 元数据 | Q17 `"Singular dynamics" "Lobb" "2016" "Painlevé"`；Q18 `"Varieties of clusters and Enriques diagrams" "2004"`；Q19 `"Anticanonical Rational Surfaces" "1997" "903"` | 核版本与出版年；Q19带入的页码猜值不作引文依据 |
| 元数据 | Q20 `"Fixed loci" "Cerda" "2015" "17"`；Q21 `"Varieties of clusters and Enriques diagrams" site:cambridge.org/core/journals`；Q22 `"Anticanonical rational surfaces" site:ams.org 349` | 固定部分论文实际为2012；核 Roé 出版 DOI |
| big 直接先例 | Q23 `"Big rational surfaces" "Testa" "Velasco"`；Q24 `"rational surface" "big anticanonical" "Cox" finite generated` | 定位并精读 TVV；发现2025 nef Cox论文但不混用于非nef特殊纤维 |

搜索引擎日期提示不等于精确数据库过滤；本轮是经典直接先例为主、近期补查为辅。
已达到五条检索路径、五件相关一手的指定段精读，按有界任务停止。
不声称通查所有未发表工作、所有近六个月更新或全部术语变体。

## 4. 五件一手的实际阅读与准确边界

本表“精读”均指列明段落，而非整篇通读；不把摘要、作者网页或参考文献列表
升级成正文证明。数学判断只依据一手论文，发现入口中的自动摘要不作依据。

| ID | 论文／出版与原文 | 本轮实际 read range | 对本对象的作用与限制 |
|---|---|---|---|
| N1 | N. Joshi、S. B. Lobb，*Singular dynamics of a q-difference Painlevé equation in its initial-value space*，J. Phys. A 49 (2016), 014002；[arXiv:1407.1961v3](https://arxiv.org/html/1407.1961v3)，2015-08-01；[作者机构出版目录](https://extern.maths.usyd.edu.au/u/pubs/publist/pubs2016.html) | 摘要、§1开头与§§1.1–1.3、§§2.1–2.2、§4、Appendix A.1–A.2 | 明确研究趋零及两基点合并；复数、渐近动力与其给定初值模型，不是 $R'$ 的相干推送公式 |
| N2 | B. Harbourne，*Anticanonical Rational Surfaces*，Trans. Amer. Math. Soc. 349 (1997)，DOI 10.1090/S0002-9947-97-01722-4；[arXiv:alg-geom/9509001v2](https://arxiv.org/pdf/alg-geom/9509001)，1996-01-24 | 引言与 Theorem I.1、Lemma II.1；Theorem III.1(a)–(c)完整陈述；Remark III.13及其论证 | 任意特征代数闭域；T1直接吸收。非nef类先扣固定部分，不能直接对 $nD_0$ 套nef消失 |
| N3 | J. Roé，*Varieties of clusters and Enriques diagrams*，Math. Proc. Cambridge Philos. Soc. 137 (2004), 69–94，[出版 DOI](https://doi.org/10.1017/S0305004103007515)；[arXiv:math/0108023v1](https://arxiv.org/pdf/math/0108023) | 引言、§1关于相对吹起及 Props1.4–1.5陈述/1.4证明；§2.2/Prop2.24陈述；§4 Props4.1–4.2及证明 | 有序点簇、邻近图变化和光滑吹起族已有；基为代数闭域上有限型对象，4.2专指P2，不直接给整数相干模 |
| N4 | J. A. Cerda Rodríguez、G. Failla、M. Lahyane、O. Osuna Castro，*Fixed Loci of the Anticanonical Complete Linear Systems of Anticanonical Rational Surfaces*，Balkan J. Geom. Appl. 17(1) (2012), 1–8；[arXiv:1201.4881v1](https://arxiv.org/html/1201.4881v1)，2012-01-23 | 引言、§2指定nef/固定分量段、Prop3.2/Cor3.3及证明、Theorem4.1及证明、Cors4.2–4.3 | $K^2\geq0$且$-K$非nef时出现固定$(-n)$曲线($n\geq3$)已有；不提供本族准确 $A+B$ 系数或整数上同调 |
| N5 | D. Testa、A. Várilly-Alvarado、M. Velasco，*Big rational surfaces*，Math. Ann. 351 (2011), 95–107；[arXiv:0901.1094v2](https://arxiv.org/html/0901.1094v2)，2009-04-18；[作者出版表](https://mauricio-velasco.github.io/webpage/Research.html) | §§1.1–1.3、§2开头基域条件、Theorem2.9及短证明；未逐证依赖的所有引理 | smooth rational、$-K$ big即Cox有限生成，不要求nef；直接吸收T2，但不是整个 $R'$ 的相对环表示 |

N3 PDF扉页另出现重排日期2021-07-17；arXiv仍标v1、2001提交，出版为2004，
本报告按实际版本身份引用，不把重排日期当新增定理。
N4出版入口本轮返回错误或非PDF页面，数学读取来自其arXiv作者原文；
年份／页码由作者共同署名后续论文的参考文献及作者履历交叉核对。
Sakai京都官方1999目录可读，PS链接在web入口失败；流式转文本存在顺序／编码和大量空白，
未取得可靠的目标定义段，故**不计为第六件精读或直接包含证据**。
Harbourne作者个人页面出现不可重试拒绝，未再访问；其arXiv全文可读。
两次Roé的标题过滤返回空文本未算阅读，随后按PDF页5–6及26–27实际回读。
所有外部PDF均仅流式阅读，未写入本地库；未绕过登录、付费或权限限制。

## 5. 为什么单纤维公式已被吸收

以下是对主控给定几何配置的条件性推导，说明先例的**准确消费者**，
不是用文献替代该配置本身的证明。
令 $n>0$，$c=\lceil n/2\rceil$，$F=A+B$。
任取 $C\in|nD_0|$，写 $C=aA+bB+R$，$R$不含$A,B$。
因 $D_0\cdot A=D_0\cdot B=-1$ 且不同有效曲线相交非负，
$$3a-b\geq n,\qquad 3b-a\geq n.$$
取 $a,b$ 的较小者即得 $a,b\geq c$。故每个截面都含 $cF$，
$$H^0(nD_0)=s_{cF}\,H^0(M_n),\qquad M_n=nD_0-cF.$$

本轮几何诊断给出 $M_n$ 有效，且它与 $D_0$ 各分量相交非负；
其支持在 $D_0$ 中，因此与支持之外的曲线相交也非负，故 $M_n$ nef。
从 $D_0^2=0,D_0\cdot F=-2,F^2=-4$ 得
$$M_n^2=4nc-4c^2,\qquad -K\cdot M_n=2c\geq2.$$
于是 [Harbourne Theorem III.1(a)](https://arxiv.org/pdf/alg-geom/9509001)
直接给 $H^1(M_n)=0$ 且 $|M_n|$ 无基点；再由Serre对偶、Riemann–Roch得
$$h^0(nD_0)=1+\frac{M_n^2+D_0\cdot M_n}{2}
=1+2nc-2c^2+c=1+\frac{n(n+1)}2.$$
无基点也说明上述固定部分**恰为**$cF$，不只是一个下界。
$n=0$为有理曲面的常数项；对$nD_0$本身有$\chi=1,H^2=0$，故$h^1=h^0-1$。
这里对N2的应用是一般定理的实例化，没有新的消失方法。

此外 $P=D_0-F/2$ nef、$P^2=1$ 使 $D_0$ big；
[TVV Theorem 2.9](https://arxiv.org/html/0901.1094v2#S2)已给Cox环有限生成。
沿 $\mathbb N[D_0]$ 取分次子环的有限生成是标准半群／分次代数后果，
所以“非nef而反典范环仍有限生成”也已吸收。
这不等于已写出该环的最小生成元和关系，更不等于混合特征族的统一表示。

## 6. 尚未被当前实读来源决定的准确问题

### 6.1 首层连接元与厚度

若T3被真正证明，则记$f=\tau(q-1)$，任意$R'$-代数$A$上的形式后果为
$$H^0(S_A,L_A)\simeq A\oplus\operatorname{Ann}_A(f),\qquad
H^1(S_A,L_A)\simeq A/(f).$$
这些是两项自由复形加标准派生基变换的后果，不另外计为方法发现。
其闭集支撑是 $V(\tau)\cup V(q-1)$；两支相交不自动增加到两个独立$H^1$方向。

但 $[R'\xrightarrow{\tau^2(q-1)}R']$ 给出完全相同的所有域纤维上同调维数，
并且在$\tau$可逆处与T3等价，却有不同的非约化厚度。
所以旧单位C1、T1及上半连续性不足以证明T3的准确因子。
当前仍需实际追踪有序吹起的积分连接映射／插值矩阵与真实基准截面。
这一剩余是明确的证明任务，不因本轮没有搜到答案而自动具有论文级新意。

### 6.2 不可把旧对角模型乘一个 tau 后推广到所有 n

旧Phase B已经识别单位C1与既有$q$-Hodge单项式差分的形式近邻。
若直接猜
$$R'[0]\oplus\bigoplus_{j=1}^{n}[R'\xrightarrow{\tau(1-q^j)}R'],$$
则在$\tau=0$会预测$h^0=n+1$；T1的$n=2$已经给$h^0=4$而非3。
因此这个未经证明的全次推广与已给定几何后果不相容，不能通过换标题保留旧模型。
本报告没有把首层T3错误地扩充成这一全次公式。

### 6.3 相对环与特殊纤维环不是同一个对象

应区分
$$\mathcal R=\bigoplus_{n\geq0}H^0(S,L^n),\qquad
\mathcal R_0=\bigoplus_{n\geq0}H^0(S_{\tau=0},L_0^n),$$
以及自然映射$\mathcal R\otimes_{R'}R'/(\tau)\to\mathcal R_0$的像。
T1只是内在特殊纤维的Hilbert函数；T2只是有限生成存在性；
两者都没有决定上式的像、整数生成元或乘法关系。
相同Hilbert函数也不识别分次环。若继续此方向，应先给出这些对象的准确计算，
再与现有固定部分／Cox环方法作包含比较，不能把尚未算出的部分先登记成新发现。

## 7. 原 qPI 动力及其他已知框架的边界

[Joshi–Lobb](https://arxiv.org/html/1407.1961v3#S2)的两基点是$(u,v)=(t,0),(0,qt)$，
在$t\to0$合到同一原点；其时间规范是$t=1/\xi$及二步$t\mapsto t/q^2$。
本次则在不同簇的末端坐标同时碰各自边界节点，且原图为
$$F_\tau(x,y)=\left(\frac{q\tau}{qx-y},\frac{qx}{y}\right),\qquad\tau\mapsto q\tau.$$
在$\tau=0$且分母非零的稠密开集，第一坐标恒为零，像至多一维。
因此这个原特化图不是双有理辛映射；同一图的吹起提升不能恢复其稠密开集上的支配性。
这与N1的周期三支配极限不同；若以重标度或不同相对模型接上N1，必须明确给出
零参数处有效的映射，不能用仅在$\tau\ne0$成立的变换偷换特殊纤维。

Phase B既有GHK八环周期族、Friedman反典范对、Stacks perfectness／派生基变换、
Wagner差分模型等扣除继续有效，本轮不重新声称亲读它们的全部正文。
普通内部吹起中心在边界光滑部分的假设，不能未经检查延用到本轮两个节点中心。
同样，Sakai分类标签或“退化”一词不能代替canonical-type／nef条件核对；
本轮未成功取得Sakai准确原定义段，故不作其分类是否逐项包含T0的强断言。

## 8. 有界处置

本件只提供先例映射：T1与T2应明确扣为直接应用；T0属既有退化机制下的模型计算；
T3未证且准确包含未定。高次相对环还没有可评分的完整主张。
没有新意分数、价值分数、证明信心、自然页数预测、Route评分或准入建议。
旧两轮失败不变；本报告不为过门而补叙述，也不把未解决任务改写为成果。

本轮完成后全文回读本文件并停止；不继续无界追引、不修改既有报告、不生成论文或PDF。
