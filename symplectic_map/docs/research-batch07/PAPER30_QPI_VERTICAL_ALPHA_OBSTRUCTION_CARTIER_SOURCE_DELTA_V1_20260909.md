# P30 qPI：实际提升障碍—Cartier 比较的有界来源差分 V1

日期：2026-09-09。类型：primary 定理包含核查；不是正式 novelty 四门、数学接受或评分。
状态：SOURCE_DELTA_BOUNDED；route_applicability：NOT_APPLICABLE。

身份披露：本执行者是 prime trace 引理的作者，也写过首 jet 引理及上一份 height-one 来源报告；
并非 fresh／盲态创新审查席。本轮不以自己的 trace 证明给 TH 或 OC 投数学接受票。
按 research-lit 执行：6 条新 query、4 件正文来源的必要段；只新增本文件。

## 1. 结论先行

**新 TH/OC 的一般机制应大幅归入既有提升障碍、Čech 连接与 Cartier 理论；
但四件已读定理没有在不补实际识别箭头的情况下直接给出原 qPI 的全 $p,m$ 理想 $(\pi,H)$。**

“局部提升之差给障碍类”“除素数的 Frobenius 微分与局部同伦”“连接映射由扩张类计算”
均已有直接来源，不能因为本件重写了自足证明就算新理论。
OC 一旦给定其 A1–A4，核心比较就是整数 Taylor 展开后对一个标准短正合列计算连接类；
非零正则微分在完整亏格一曲线上无零点，以及最后的两方向理想消元，也不另算方法创新。

本轮未被来源定理直接代替的是**原对象实例识别**：
同一个实际 $L_m$ 的 Bockstein 确实作用于原 $J$，其非零类限制到每个完整 $X$；
原降序迹满足指定 $p\pi$ 同余，且跨过全部末端图；
由这个同余得到的局部原函数，确实产生原 $\alpha=p^{-1}dI$ 的首切向类。
这是一组待数学检查的具体责任，不是“已证明全球首创”或“值得独立长文”的结论。

另须避免相反的过度扣除：算术 Kodaira–Spencer／DI 文献的典型对象是
**整个 Frobenius 态射的提升障碍**，而当前 $\kappa_J$ 是**指定原函数／截面的提升障碍**。
同样出现差商，并不自动把二者识别为一个类。

## 2. 冻结 claim 与本轮输入

全文读取并核准下列两个准确版本；本报告不消费其他后来出现的数学检查票。

| 输入 | 范围与身份 | SHA-256 |
|---|---|---|
| [ALL_TAME_HEIGHT1_PROOF_V1](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md) | 全文 219 行；TH.1–TH.3、Steps 1–5，作者证明状态 | 43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75 |
| [OBSTRUCTION_CARTIER_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md) | 全文 177 行；A1–A4、OC.1–OC.2 及完整证明 | 81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa |
| [HEIGHT1_SOURCE_DELTA_V1](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_SOURCE_DELTA_V1_20260909.md) | 本轮重读 §§1–2、检索日志起首并按标题定位旧扣除；不重跑旧查询 | 6d7bbe36569a110c68c181d1ae70857760ac5b1d062ab10cba295f368e412990 |

准确新量词为：所有素数 $p$（含 $2$）、所有 $m\ge1$ 且 $p\nmid m$、圆分高度 $a=1$，
实际单位时间与完整光滑有限原能级 $X=(J=h)$。仍不涵盖奇异能级、更高 $a$ 的厚度、
任意额外分歧状态提升或晶体模比较。

TH 的实际链为
$$
[\,1-s^m\,]\equiv[-m\pi]\pmod{\pi^2}
\Longrightarrow \beta_{L_m}(J)\ne0
\Longrightarrow \kappa_J=\rho_X\beta_{L_m}(J)\ne0,
$$
其中 $\rho_X$ 是由原有效除子限制序列得到的实际同构。
在 Hasse 零能级，作者再由
$$
G_i=\frac{I-F(j_i)}{p\pi},\qquad
\bar G_j|_X-\bar G_i|_X=f_{ij}^{\,p},\qquad
f_{ij}=\overline{(j_j-j_i)/\pi}|_X
$$
取得
$$
\nu=d(\bar G_i|_X),\qquad
\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0
\ \text{in }H^1(X,\mathcal O_X^p).
$$
来源比较针对这条新链，不再要求旧配对路线中尚未证明的一般 $m$ 配对常数 $m^2$。
新作者证明已明确不用它，不能把过时责任继续记成 TH 的缺口。

## 3. 检索日志与四件正文来源

未发现可调用 Zotero／Obsidian 接口。本地相关 PDF 文件名筛选无命中；
未找到 arxiv_fetch.py，按技能使用 arXiv 网页 fallback。没有下载 PDF 到工作区。

| 编号 | 实际新 query | 用途 |
|---|---|---|
| Q1 | “2608.21772” Shimada arithmetic Kodaira Spencer | 核准 2026 新预印本 |
| Q2 | “Dupuy” “Katz” “Rabinoff” “Zureick-Brown” 2019 arithmetic Kodaira Spencer | 分离检索线索中混写的两篇 2019 来源 |
| Q3 | “Buium” “2006” “Kodaira-Spencer” | 核题名与出版方摘要，筛选与本接口的接近度 |
| Q4 | site:arxiv.org “arithmetic Kodaira” “Deligne” “Shimada” | arXiv fallback／相关元数据 |
| Q5 | “Deligne” “Illusie” “Relèvements modulo p2” 1987 pdf | 定位原始 DI 论文 |
| Q6 | “Deligne” “Illusie” “1987” “pdf” “247” “270” -site:scispace.com -site:scribd.com | 从作者 IAS 出版目录取得公开原论文 |

6 条后停止检索；随后仅打开已定位原文、原文链接、指定段落及元数据。
四件正文阅读对象如下。年代较早的三件是当前问题的直接基础来源，不以“最近两年”过滤掉。

| 来源 | 版本与出版状态 | 实际必要阅读范围 |
|---|---|---|
| Kanau Shimada，Arithmetic Kodaira–Spencer Class and Frobenius Liftings via Frobenius–Witt Cotangent Complex | [arXiv:2608.21772v1](https://arxiv.org/abs/2608.21772v1)，2026-08-22，13 页预印本；未核正式刊本 | [HTML](https://arxiv.org/html/2608.21772)：§2 的定义与纤维序列；§3 定义 3.1/3.7、定理 3.3/3.9 及证明；§4 定义 4.1、定理 4.2 及证明；§5 定义 5.1–5.2、定理 5.3 的证明、推论 5.6–5.7 |
| Taylor Dupuy、David Zureick-Brown，Deligne–Illusie Classes as Arithmetic Kodaira–Spencer Classes | [JTNB 31(2) (2019), 371–383](https://www.numdam.org/articles/10.5802/jtnb.1086/)，DOI 10.5802/jtnb.1086，正式论文 | [正式 PDF](https://www.numdam.org/item/10.5802/jtnb.1086.pdf)：Remark 1.1、Theorem 1.2；§§2.1–2.7 的底环、Frobenius、DI 类和 Theorem 2.2；§3 的局部兼容数据、Lemmas 3.2–3.3、Theorem 3.4 与证明，页 373–382 |
| Taylor Dupuy、Eric Katz、Joseph Rabinoff、David Zureick-Brown，Total p-differentials on schemes over Z/p² | 正式刊于 [J. Algebra 524 (2019), 110–123](https://doi.org/10.1016/j.jalgebra.2019.01.003)；本轮正文读 [arXiv:1712.09487v1](https://arxiv.org/abs/1712.09487v1)，2017-12-27，11 页 | [作者 HTML](https://arxiv.org/html/1712.09487)：§2.1 前提、§2.7–2.15 基本正合列与 Frobenius 提升；§3 Theorem 3.2 与证明；§4 Theorem 4.1 与证明；另核作者 PDF 的 $p>2$ 前提及在 HTML 缺失的正合列文字 |
| Pierre Deligne、Luc Illusie，Relèvements modulo p² et décomposition du complexe de de Rham | Invent. Math. 89 (1987), 247–270；[作者 IAS 目录](https://publications.ias.edu/node/403)，[公开原 PDF](https://publications.ias.edu/sites/default/files/Number57.pdf) | §1 Theorem 1.2；§2 Theorem 2.1 的 (a)–(d)、Remarks 2.2(i)–(iii)，页 249–254；§3.4 前提、Theorem 3.5、Corollary 3.6 与 3.5 的构造证明，页 262–264 |

书目区分：JTNB 那篇只有 Dupuy、Zureick-Brown 两位作者；四作者的是 J. Algebra 那篇。
这里纠正的是本轮检索线索的混写，不倒推为旧来源报告已发生错误。

## 4. 原文定理与当前 claim 的精确关系

### 4.1 Shimada：真正被统一的是 Frobenius 提升障碍

Shimada 的类位于
$$
\kappa_{\mathcal Y}\in
\operatorname{Ext}^1_{Y_0}(F_{Y_0}^*\mathbb L_{Y_0/\mathbb F_p},\mathcal O_{Y_0}),
\quad Y_0=\mathcal Y/(p).
$$
Theorem 3.3 将其消失与 $\mathcal Y/(p^2)$ 存在 Frobenius 提升等价；
3.9 加入底上指定 Frobenius 的兼容要求；4.2 在光滑情形把它与 DI 类按其符号约定识别。
5.3 则将类与平方零扩张的 $\xi\circ dF-F\circ\xi$ 比较。
这些是“新的算术 KS 类／新的提升障碍比较”表述必须扣除的近年一般定理。[Shimada §§3–5](https://arxiv.org/html/2608.21772)

**本件关系（推断）：** TH 的 $\kappa_J$ 是一个实际函数提升的连接类，而非上述 Ext 类本身。
当 $p>2$ 时，$\mathcal U/(p)=\mathcal U/(\pi^{p-1})$，不等于 TH 的约化曲面 $\mathcal U/(\pi)$。
Shimada 的 flat 版本仍可作用于这种 $\mathbb Z_{(p)}$-平坦对象，不能说其理论完全不允许分歧；
但作用后的基空间、余切复形和障碍对象都尚需运输。
$p=2$ 时两种底层厚度对齐，也仍须识别“提升指定函数”与“提升整个 Frobenius”的箭头。
Theorem 3.9 要求已经给定一个底上的态射，不能预先把不存在的全局 $j$ 当作该态射。

### 4.2 Dupuy–Zureick-Brown：分歧 $\pi$-形式情形已有，不能以底环排除

JTNB §2.2 明确用 $R_n=R/\pi^{n+1}$；§2.5 的 DI 类由局部 $\pi$-derivation 的差得到，
目标是 Frobenius 扭曲切层的 $H^1$。§2.7.1–2 把它解释为 Frobenius 提升 torsor 的类。
Theorem 2.2／3.4 给光滑态射的兼容，Theorem 2.2 还包括闭浸入；
其正式框架允许有限分歧扩张上的 $\pi$-形式模型，固定底上 $\pi$-derivation；§2.4 区分 $p$ 次与 $p^r$ 次 Frobenius，比较时须固定所用幂次。[JTNB §§2–3](https://www.numdam.org/item/10.5802/jtnb.1086.pdf)

**本件关系（推断）：** “\(\pi\)-方向局部提升之差及其函子性”已有，不能计为新框架。
但当地差作用于整个函数层、满足 Frobenius Leibniz 规则；TH 的 $f_{ij}$ 是局部提升一个函数的普通差。
要按该兼容定理直接包含 TH，必须给出实际形式态射、所选底 Frobenius、
由扭曲切层到本件目标的比较，以及与原 $j_i,I$ 的等式。
只有特殊纤维的 $X\hookrightarrow U_0$，不等于已提供整个光滑 $\pi$-形式提升的闭浸入；
也不能另选一条抽象椭圆曲线提升后，默认为原完整能级的指定提升。

### 4.3 四作者 total-p：扩张类与连接映射的机制已有，目标不能偷换

所读 v1 的 §2.1 假设 $R=W_2(k)$、$p>2$。基本正合列是
$$0\longrightarrow\mathcal O_{Y_0}\longrightarrow
\Omega^{1,\mathrm{tot}}_{\mathcal Y}\longrightarrow
F_{Y_0}^*\Omega^1_{Y_0}\longrightarrow0.$$
Proposition 2.15 将分裂与 Frobenius 提升对应；Theorem 3.2 给扩张类与 DI 类的符号比较。
Theorem 4.1 的 arithmetic Gauss–Manin 连接
$H^0(F^*\Omega^1)\to H^1(\mathcal O)$
是与扩张类的 cup product，证明直接计算局部提升的差。[作者 v1 §§2–4](https://arxiv.org/html/1712.09487)、[对应 PDF](https://arxiv.org/pdf/1712.09487)

**本件关系（推断）：** 连接类／扩张类的计算方法不是新比较原理。
但其 total-p 微分模不是当前原秩二相对余切模，连接映射也不是 OC 的
$H^0(B_X^1)\to H^1(\mathcal O_X^p)$。
不能只凭“Gauss–Manin”“Cartier”“rank two”等词，将这两个序列拼成未证明的模同构。
这里不将所读 v1 的 $p>2$ 前提擅自扩为 $p=2$；最终刊本正文的版本差异亦不作推定。

### 4.4 Deligne–Illusie：除 $p$、局部同伦及 Cartier 分解已是经典构造

DI Theorem 1.2 给 Cartier 同构。Theorem 2.1(b) 对局部 Frobenius 提升使用
$p^{-1}\widetilde F_i^*$；(c)–(d) 用两个提升的除 $p$ 差得到同伦，
满足 $f_j-f_i=dh_{ij}$ 及三重交的余循环条件。Remark 2.2(iii) 解释相应提升障碍。
Theorem 3.5／Corollary 3.6 进一步比较模 $p^2$ 的提升 gerbe 与
$\tau_{\le1}F_*\Omega^\bullet$ 的分裂，并非只陈述维数相等。[DI §§1–3](https://publications.ias.edu/sites/default/files/Number57.pdf)

**本件关系（推断）：** “局部除法—微分—余差—Cartier”不能作为新的一般结构宣传。
不过 DI 的输入是实际 Frobenius 提升／相应模型提升；OC 只有指定原迹函数 $I$ 和
$I-F(j_i)\in p\pi$。单变量 $F$ 与一个函数的同余，不等于已给整个模型的 Frobenius 提升，
也不等于已经识别 DI 的除 $p$ 微分映射。其一般分裂定理不单独给出 TH 的原迹或系数理想。

## 5. 哪些已可直接扣除，哪些仍须实际识别

下表是本地 claim 的责任分析；“仍须识别”不表示目前没有作者证明，更不表示已获新意。

| 当前环节 | 可以扣除的机制 | 仍属于原对象的识别责任 |
|---|---|---|
| TH Step 1：$\beta_{L_m}(J)$ | 已有实际底变换复形后，连接同态由提升、微分、除 $\pi$ 计算是基本同调代数 | 固定同一自然复形及真实常数项；原 $J$ 非常数，故不在核；$1-s^m\equiv-m\pi$ 的单位斜率 |
| TH Step 2：限制到每个 $X$ | Cartier 除子限制序列和长正合列 | 同一个原 $L_m$、完整有效纤维、指定平凡化及 $H^1/H^2(\mathcal O_{S_0})=0$，确使 $\rho_X$ 为同构 |
| prime trace／TH Steps 3–4 | 循环词轨道、多项式整除、局部化单射均是标准工具 | 原因子次序的 $p\pi$ 同余；全部末端图在非约化 $\mathcal O/(p\pi)$ 上的单射；$p=2$ 的准确符号 |
| OC Steps 1–4 | 整数 Taylor 与标准 Čech 连接计算；$\ker d=\mathcal O_X^p$ 是 Cartier 的基本内容 | 实际 $G_i$ 的差确为 $f_{ij}^p$，以及得到的 $\nu$ 正是原 $\alpha$ 的首切向类，而不是另选形式 |
| OC Step 5／TH 完成式 | 亏格一非零正则微分无零点；单位系数消元；重根理想和无分歧评价 | 同一 $\nu$ 在所有原完整点成立，且两个实际状态方向都保留 |

尤须保留两个 Frobenius 箭头：
$$
H^1(X,\mathcal O_X)
\xrightarrow[\text{加法群同构}]{\operatorname{Fr}_*}
H^1(X,\mathcal O_X^p)
\xrightarrow{\iota_*}
H^1(X,\mathcal O_X).
$$
OC 的非零结论位于中间目标。由短正合列的精确性，
$\iota_*\partial\nu=0$；不能把这个非零类直接送入末端目标后仍宣称非零。
因此“超奇异 Frobenius 为零”不反驳 OC，同时 total-p 文献中值于末端目标的连接映射
也不会因记号近似而自动等于 OC 的非零比较。
通过 Frobenius twist 可将半线性表述线性化，但仍须运输这两条不同的箭头。

从这里能作出的有限结论是：**OC 更适合表述为一个针对指定整数同余的自足实例引理，
不适合宣称新的 arithmetic Kodaira–Spencer／divided Frobenius 一般理论。**
TH 的来源差分进一步收缩到原 cohomology—trace—完整模型的实例识别与算术结论。
数学上自足、来源上未直接包含、研究上有足够新意，是三件不同的事。

## 6. 访问限制、未覆盖项与交付边界

- Shimada 已核到 2026-08-22 的 v1 及必要 §§3–5；这是一份预印本，不将其描述为已同行评审定理。
- total-p 的 NSF 托管入口本轮返回内部读取错误，正文改用作者 arXiv v1；正式刊本身份由出版方及 JTNB 参考文献核准。v1 的若干 HTML 图为空，已读对应作者 PDF 的文字层；没有以缺失图直接补出新比较。
- DI 的 Springer 页面只提供机构访问／订阅入口；通过作者 IAS 目录公开附件读到原文，没有使用付费或登录访问。PDF 文字层有 OCR 瑕疵；所记公式仅限可核必要段，未声称审计全文排印。
- [Buium 2006，J. Number Theory 119(2), 297–306](https://doi.org/10.1016/j.jnt.2005.11.002) 本轮只核出版方摘要及作者目录：主题是通用椭圆曲线算术 KS 类的模 $p$ 表达所满足的 PDE。未读其完整定理，不列作第五件正文来源，也不能排除它或其所引 Hurlburt 公式存在更具体的比较接口。
- 旧 KS 根单位曲率、Bai–Lee、Fonseca、Movasati 的已记录机制扣除沿用，不重查；本轮没有穷尽所有分歧变形／椭圆模空间文献。未命中不是不存在，未直接包含不是正式新意通过。

没有新增非零计算、GPU、论文项目、锁、索引或分数；仅新增本报告。
最终来源判断保持有界：标准机制已明确扣除；本轮所读定理尚未直接代替 TH 的原对象实例识别。
待对应数学检查完成后，可以引用这些来源重新压缩方法表述；本报告本身不授予验收或新的研究阶段。
