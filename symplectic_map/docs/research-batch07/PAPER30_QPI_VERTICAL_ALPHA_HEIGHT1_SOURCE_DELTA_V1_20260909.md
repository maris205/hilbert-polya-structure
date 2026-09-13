# Paper30 qPI P03：全素数 height-one 识别的有界来源增量 V1

日期：2026-09-09。执行者：`/root/p30_qpi_post_integral_ideas_v1`。
类型：新增 claim 的定向来源扣除；不是数学接受、正式查新票、评分、候选合同或论文。
`route_applicability: NOT_APPLICABLE`。0 GPU；只新增本文件，所有旧件冻结。

身份披露：本执行者写过首 jet 矩阵引理及迭代引理，也写过前期想法报告；
因此不是 fresh／盲态独立创新审查席。本轮不以自己的引理给新证明投接受票。
使用 `research-lit`：五个定向 query，四件一手作者来源的必要段，保留访问缺口；
不把搜索未命中解释为无先例。两件新作者证明的数学核查由另一席承担。

## 1. 来源结论

**应扣除的标准机制比旧低素数预筛更明确，但尚不能据本轮来源把完整 actual 结论列作已定理的直接实例。**
给定原对象确实产生一个与正则微分配对为一的 de Rham 补基，
“Hasse 与补基 Cartier 系数不同时为零”就是标准秩二／秩一线性代数；
不应把可选择第二类补基、Cartier 半线性或最后的局部理想消元计作新方法。

剩余责任集中在一条准确的实例识别链：原整数循环除法、依赖状态的正则端点矩阵、
实际首 jet 给出的特定 $R$、其配对单位证书，以及由内在正则切向类覆盖完整原能级。
这些责任并不会因抽象补基可以选择而消失。这里的“剩余”指本轮未被所读定理直接代替的证明责任，
不等于已经证明其全球首创、困难程度或独立论文价值。

近期根单位量子差分文献给出很近的框架，但其对象与取层方式仍需比较：
由近单位量子联络提取的曲率层，不自动等于本原矩阵的 $p^{-1}d_{\rm state}I_p$。
因此，建议在两份作者证明通过数学核查后，继续一次有明确停止条件的全 $a$／$m$ 理论诊断；
不建议仅把 height-one 结论改名为新 Cartier 理论，或据此直接进入完整稿件。

## 2. 本轮准确绑定的作者 claim

本轮全文读下列两件，复查 hash 未变；正文状态仍为作者证明、待非作者核查。

| 输入 | 已读范围 | SHA-256 |
|---|---|---|
| [ALL_PRIME_HEIGHT1_PROOF_V1](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_HEIGHT1_PROOF_V1_20260909.md) | 全文 255 行，特别是 Claim、Steps 1–5 | `ffdcfc37860477e990f836721898fc654537bb3254b7335876581990c2da4f74` |
| [CARTIER_PAIRING_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_CARTIER_PAIRING_LEMMA_V1_20260909.md) | 全文 227 行，CP.1–CP.2 及各自实际前提 | `65dfd605af26e84b57289ef57380392c923b2b1c700b5a3c69731567f8a54e4c` |
| [PRIOR_ART_SCREEN_V1](PAPER30_QPI_VERTICAL_ALPHA_PRIOR_ART_SCREEN_V1_20260909.md) | 全文 222 行；旧查询和访问缺口复用，不重跑 | `9bc5bbbcc021588a0d9f60b0f70197924b58c729fe066e48e9d9c656c1466f2b` |

固定 $a=m=1$、$q=\zeta_p$、$\pi=q-1$，在原圆分 DVR 或其有限无分歧扩张上，
固定任意实际单位时间 $t$，只微分原两个状态方向。作者声称对所有素数 $p$、
所有光滑有限小阶能级 $X_h$ 上每个点 $P$，有
$$
\alpha_p=p^{-1}d_{\rm state}I_p,\qquad
\mathfrak c(\alpha_p)_P=(\pi,\widetilde H_p(t,j)).
$$
该陈述包含完整原能级与四条末端线，而不是仅环面或一个谱替代曲线。
光滑 Hasse 根重数为 $e_h$ 时，完成局部式为 $(\pi,z^{e_h})$；
不预设 Hasse 根简单。对约化到该光滑超奇异层的任一无分歧 DVR 状态提升，
两个实际系数的公共 $\pi$ 阶准确为一，故未整除 $dI_p$ 的公共阶准确为 $p$。

$p=2$ 由原两因子迹另证；奇素数的四次配对引理不能直接用于二。
没有加入奇异能级、任意有分歧再基变换、全圆分层数 $a$ 或一般剩余阶 $m$。
上述“所有状态提升”是系数沿环同态的评价，不是把一形式拉回 DVR 的零相对微分模。
本报告保留这些区别，不用旧 $p=3$ 信号替代新全素数量词。

## 3. 检索与实际阅读边界

### 3.1 五个 query

| 编号 | 实际 query | 用途／结果 |
|---|---|---|
| Q1 | `"q-difference" "roots of unity" "Poisson" curvature` | 定位根单位曲率近邻；筛掉二手摘要后读 KS 作者原文 |
| Q2 | `"elliptic" "symplectic-Hodge" "Kodaira-Spencer"` | 定位椭圆曲线补基与变形方向的标准几何接口 |
| Q3 | `"Cartier" "conjugate filtration" "de Rham" "elliptic"` | 定位 Cartier 在整个 de Rham 空间上的商映射，而不只查 Hodge 线 |
| Q4 | `"Fonseca" "Higher Ramanujan" "symplectic-Hodge"` | 确认 Fonseca 作者正文与出版元数据入口 |
| Q5 | `site:arxiv.org "Quantum Adams operations"` | arXiv fallback；新增 Bai–Lee 2025 原文，核根单位算子的对象和退化层 |

五 query 后只打开明确作者原文、其中已有链接与元数据，未再跑同义检索。
本轮可调用工具未发现 Zotero／Obsidian 接口；相关本地 PDF 文件名未命中，
也未找到 `arxiv_fetch.py`，故按技能用 arXiv 网页 fallback；没有下载 PDF 或重扫旧构建树。
没有直接查询 Google Scholar／Semantic Scholar，不冒称覆盖它们的独立索引。

### 3.2 四件必要来源

| 来源与状态 | 实际必要 read range | 与本题的关系 |
|---|---|---|
| Peter Koroteev、Andrey Smirnov，*On the Quantum K-theory of Quiver Varieties at Roots of Unity*；[arXiv:2412.19383v4](https://arxiv.org/abs/2412.19383v4)，v4 日期 2026-06-02；arXiv 记载刊本 IMRN 2026(14), rnag153 | [v4 正文](https://arxiv.org/html/2412.19383v4) §§5.3–5.6，重点 Lemma 5.1、(5.22)–(5.27)、Theorems 5.4–5.5；连读 §5.2 末尾的规范说明 | 原根单位迭代乘积与 $p$-曲率的紧邻；旧 Phase B 已有此源，本轮核首非零层的准确规范 |
| Shaoyun Bai、Jae Hee Lee，*Quantum Adams operations in quasimap K-theory*；[arXiv:2510.09335v1](https://arxiv.org/abs/2510.09335v1)，2025-10-10，预印本，本轮新增 | [作者正文](https://arxiv.org/html/2510.09335) §5.2 Definition 5.1、Theorem 5.5 及证明；§5.4 Proposition 5.12、Conjectures 5.13/5.15、Corollary 5.17、Remark 5.18；同时核 §5.3 的适用条件 | 根单位曲率与 quantum Adams 的直接识别；不能把后续退化猜想全写成无条件定理 |
| Tiago J. Fonseca，*Higher Ramanujan equations I: moduli stacks of abelian varieties and higher Ramanujan vector fields*；[arXiv:1612.05081v1](https://arxiv.org/abs/1612.05081v1)，2016-12-15，本次读作者预印本版本 | [正文](https://arxiv.org/html/1612.05081) §§2.1–2.3 的辛／Hodge 基；§5.1 全节；§6.1 Theorem 6.2 及证明 | 一般辛补基、其椭圆曲线显式规范与 Kodaira–Spencer 接口；不是本原 $R$ 的身份定理 |
| Hossein Movasati，*Leaf schemes and Hodge loci*；[作者 PDF](https://w3.impa.br/~hossein/myarticles/LeafScheme.pdf)，扉页日期 2026-08-10，研究／讲解混合作者稿，未核同行评审刊本 | 扉页与前言；§4.4，PDF 索引页 82–83、页脚 83–84，特别是共轭滤过及其 Cartier 商映射段；阅读前后条件以区分普通层后续命题 | 对标准 de Rham／Cartier 机制给出明确作者叙述；不把本书后续普通层或 $p\ne2,3$ 专门公式误套到所有超奇异层 |

版本说明：KS 刊本信息取自 arXiv 作者元数据，数学阅读对象是 v4，不声称另读出版排版全文。
Fonseca 相关 AMS 专著入口有检索元数据，但直接页返回 403；不据此声称已核其刊本定理编号。
Movasati 是作者维护稿而非本轮核实的正式刊本；其标准结构段不承担最早发现权判断。

## 4. 已经可以扣除的机制

### 4.1 选择配对为一的补基不是新构造

Fonseca 的 genus-one 显式模型给出辛 Hodge 双基，且固定第一微分后，第二基可加其倍数；
其 §5.1 用 Gauss–Manin 与辛配对表达 Kodaira–Spencer。
这是本轮扣除补基选择与变形语言的来源。[Fonseca，§§5.1、6.1](https://arxiv.org/html/1612.05081)

以下是对本题的透明推论，不是该文已写出的 qPI 断言。若 $\omega$ 已固定，
任选一个配对为一的补基 $\eta_0$，则实际给定的 de Rham 类可写成
$$[\eta_{\rm actual}]=c[\eta_0]+b[\omega],\qquad
c=\langle\omega,\eta_{\rm actual}\rangle.$$
可以另选 $\eta_0$ 并不保证固定 $\eta_{\rm actual}$ 的 $c$ 非零。
只有证明这个实际 $c$ 是单位，才可运输补基非消失结论。
若要进一步称实际 $\eta$ 为某方向 $\nabla_v\omega$，还须给出该变形方向及相应比较；
不能仅因为式子是第二类微分就把它叫作已识别的 Kodaira–Spencer 方向。

### 4.2 CP.2 的抽象不同时消失属于标准推论

Movasati §4.4 先给任意完美域上光滑椭圆曲线的共轭滤过，
再由 $H^1_{\rm dR}/G^0$ 的 Cartier 同构得到到 Hodge 线的满射；
其后的普通曲线分裂是额外情形，不能反过来限制这条商映射。
[Movasati，§4.4](https://w3.impa.br/~hossein/myarticles/LeafScheme.pdf)

因此，在代数闭剩余域上，若已知 $[\omega],[\eta]$ 配对为一，它们构成秩二 de Rham 空间的基。
秩一 Cartier 商映射不可能同时杀掉这两个基向量。
若实际系数已识别为
$$\mathcal C(\omega)=H^{1/p}\omega,\qquad
\mathcal C(\eta)=\Lambda^{1/p}\omega,$$
就有 $(H,\Lambda)\ne(0,0)$；这个推论不要求 $H\ne0$，反而正好处理超奇异情形。
在前款的写法中，超奇异点满足
$\mathcal C(\eta_{\rm actual})=c^{1/p}\mathcal C(\eta_0)$。
故“补基的 Cartier 像非零”本身应扣除，剩下的是本题固定类的 $c=1$ 证书。

这里仍须按 CP.1 固定的局部正则化来定义 $[\eta]$，并核 Cartier 与该代表的对应。
不把有理微分的恰当性直接等同于零 de Rham 类。
CP.2 作者证明自行处理 $p$ 次负主部，是证明接口的细节，不是另一个全新 Cartier 原理。

### 4.3 理想消元、重根和公共阶不另算方法

若实际全局首切向类已证明处处非零，在局部基 $(dj,\theta)$ 中写
$$\alpha=(\widetilde H+\pi A)dj+\pi B\theta,\qquad B\in\mathscr A^\times,$$
则 $(\widetilde H+\pi A,\pi B)=(\widetilde H,\pi)$ 是直接消元。
模 $\pi$ 的 Hasse 根有重数 $e$，便得到 $(\pi,z^e)$，不需新正规形理论。
沿所准许的 DVR 状态提升评价后得公共阶一，乘 $p$ 后加上 $p-1$ 阶，也都是此理想等式的推论。
标准系数理想／Fitting 身份和无分歧基变换的既有扣除沿用旧预筛 §4.1，未重开旧来源。

## 5. 最近根单位来源仍缺什么比较箭头

KS 在参数同时趋近单位、并把差分算子写成 $1+\pi\nabla+O(\pi^2)$ 后，
用 $p=-\pi^{p-1}$ 提取 $p$ 次迭代的 $\pi^p$ 层。
本句的 $\pi$ 是该文的 Dwork 参数；它与本题固定的 $q-1$ 只按其一阶关系比较，不直接等同。
其 (5.26) 是归一化逆乘积的 $p$-曲率，§5.6 的结论是指定量子联络的等谱。
[KS，§§5.3–5.6](https://arxiv.org/html/2412.19383v4)

Bai–Lee Theorem 5.5 识别指定 Kähler 差分联络的根单位 $k$-曲率与 quantum Adams；
§5.4 使用 $q-1=\beta t$，Proposition 5.12 抽取 $\beta^p$ 层。
更广的 Adams–Steenrod 退化仍列作猜想，并单列成立条件。
[Bai–Lee，§§5.2–5.4](https://arxiv.org/html/2510.09335)

本题不能只按术语相似应用这两文，至少还缺下列三个实际箭头：

1. 将原固定 $2\times2$ 的 $A(Z)$、其参数与整数格，识别到来源所需的具体量子差分对象，
   并证明所用规范不删端点、不引入不许可分母。
2. 将那个对象的曲率取层，与本题先在整数层除 $p$ 再取 $\pi$-jet 的
   $p^{-1}d_{\rm state}[Z^p]\operatorname{tr}\prod A(q^iZ)$ 比较；
   矩阵逆乘积、谱信息、标量迹系数的状态微分不能未经证明互换。
3. 将比较运输到原完整光滑能级和局部自由秩二微分模，保持实际两系数理想及固定的圆分参数。

这些箭头是本报告依据对象差异提出的必要检查，不是断言永远不存在这种识别。
反之，若以后确实构造出全部箭头，则相应内容应重新扣为直接实例；
目前仅有同类框架与一般机制，不足以替作者的完整 actual 链作来源包含证明。

## 6. 全素数新 claim 的责任划分

| 作者链上的环节 | 本轮可扣除的已有部分 | 尚须由 actual 证明承担的部分 |
|---|---|---|
| 原循环除法与首矩阵 jet | 矩阵有限和、Cayley–Hamilton 等为标准代数工具；根单位曲率有近邻框架 | 固定原因子次序、先除 $p$ 后降模的合法性，以及实际取层一致性 |
| 原第一末端 gauge | 正则延拓和迹共轭不变性是标准工具 | $G$ 依赖状态，$d\widehat A$ 必含其导数；特定正则矩阵确给同一原 $I_p$ |
| 四次曲线上的补基 | 配对为一的第二类补基可选择；不算新一般理论 | 原首 jet 算出的固定 $R$ 恰给该类，而非重新选择一个好用的 $R$ |
| CP.1 的单位配对 | 留数配对和可分根插值是标准工具 | 特定整数证书 $4(R/Z)=f'B-(4Z^2+2(h-2)Z)f$ 与首一三次 $B$ 的实际恒等式 |
| CP.2 的 $H,\Lambda$ 非共零 | 已给双基及 Cartier 系数后为标准直接推论 | 精确指数、半线性规范、所给有理代表与 de Rham 类的对应 |
| 一个端点到完整原 $X_h$ | 射影几何整曲线上正则函数为常数 | $\nu_h$ 来自原全局正则一形式、可粘合且在全部末端有效；不是只在谱曲线比较 |
| $(\pi,H)$、重根及公共阶 | 首切向单位给标准消元与理想评价 | 该单位对全部允许 $p,t,h,P$ 确实成立；$p=2$ 的实际另证不能遗漏 |

据此，适当的新结果表述若数学核查通过，应强调“固定 qPI 原模型上的统一实例识别／精确系数理想”，
不要扩大成“发现 Cartier 双性”“第二类微分的新构造”或“一般根单位曲率的新理论”。
从低素数数值信号推进到全素数、全光滑原能级，是量词和实际证明责任的增长；
它本身不自动判定研究新意高低，仍取决于能否被具体已有识别直接包含。

## 7. 是否值得继续全 $a$ 或 $m$

**值得一次有界、纯理论、原对象内的后续诊断；本来源报告不授权更大项目或预支其成功。**
优先问机制是否改变，而不是继续搜若干素数上的同一不等式。

- **全 $a$ 方向：** 冻结的[首 jet 迭代作者件](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_ITERATION_V1_20260909.md)
  声称对奇 $p$、$m=1$，$\beta_{p^a}=H_p^{\sigma-1}\beta_p$。
  若该接口通过核查，则 $a>1$ 时 Hasse 零层的首切向 $\pi$ 项已经消失。
  这排除直接复制 height-one 证明，却没有给更高实际理想。
  有价值的下一问是首个非零较高层是否仍来自可识别的 de Rham／晶体对象，
  而不是从该消失式猜一个统一厚度指数。
- **一般 $m$ 方向：** 必须保留块内 $q$ 变形及原状态规范，先明确其首项对应的实际微分或配对类。
  若它只是同一个单位补基机制经已证识别运输，应如实扣为推广实例；
  若配对系数出现真正零点或额外参数，才有理由继续研究新局部结构。
- **停止条件：** 仅重现抽象补基非消失、仅得到一般形式群“可能依赖提升”，或只有更多有限样本，
  都不足以推进全层理论目标。后续必须交付原对象的比较式、首非零层或明确反例之一。

本款是来源工作后的范围建议，不是新的数学证明。未计算高层 $\pi$ 展开，未新跑素数实验，
未补做独立 proof check，也未把迭代作者件自动升级为已接受输入。

## 8. 尚存访问和覆盖缺口

1. 四件作者原文的上述必要段均已实读，不声称四篇／部全文精读或其证明都经独立验算。
2. 通过 KS 原文所列 Katz 1972 DOI 链接尝试取得原始共轭滤过来源，
   [该入口](https://doi.org/10.1007/BF01389714) 未成功返回正文；未计作第五件已读来源。
   本轮 Cartier 商映射的明确阅读根据是 Movasati 作者稿，故不宣布已追溯到最早原始证明。
3. Fonseca 的 AMS 相关页直接访问为 403；这里只按实际已读 arXiv 版本引用。
   不把该访问失败当作不存在刊本，也不将未读刊本编号拼接到预印本。
4. 旧 Ditters 1989 全文缺口仍在；旧 Vlasenko、Lubin–Tate、Henrio 扣除按旧预筛复用，
   本轮没有重新读取其全文或宣称穷尽了所有非普通形式群及高层整结构结果。
5. 尚未系统追索所有 qPI／离散等单值原文是否已给“此特定矩阵到此配对类”的显式识别。
   五 query 的有界增量不能排除其存在；本报告不作全球无先例结论。

## 9. 交付边界

`research-lit` 使本轮按对象、取层、基与配对、适用素数、全局覆盖五项逐条核来源，
并把预印本、作者稿、刊本元数据和未访问正文分开记录。
唯一新增产物是本报告；无稿件、PDF、项目锁、Route 门分、容量估计或外部发送。
最后判定保持两层：**标准机制已明确扣除；完整 actual height-one 识别尚未被本轮所读定理直接代替。**
这既不预授作者数学证明，也不预授研究新意；数学状态以另席检查和主控实际验收为准。
