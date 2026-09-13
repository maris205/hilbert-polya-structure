# Paper31：I05／I09 深核一手来源与包含边界 V1

日期：2026-09-09 UTC；执行席：`/root/p31_qpi_quick_filter_covers_v1`。
阶段：`novelty-check / PHASE_B_ONLY / NO_CANDIDATE_ADMISSION`。
`route_applicability: NOT_APPLICABLE`；不出 Phase C／D 自票、正式新意分数、数学接受或长文容量 PASS。
本件只追加证据；保留冻结首筛、已接受数学、旧失败与锁，不建立论文、不改索引。

## 1. 本轮结论与范围

I05：完整 Pascal／Stirling 理论确为最强包含入口，但最直接的双变量变基不保持原源，已有二阶可检验见证。
这只排除一个快捷包含论证；尚未排除适配原四簇的联合变换，也没有供应全次数递推或全素数定理。
I09：新增 Zimmermann 与 Petrov–Skorobogatov 两项强先例，进一步扣除一般“野厚度—分歧”和“Bockstein—扭子”概念。
固定原完整提升到具体局部类的计算仍未找到现成公式，但这是未解决输入，不是已经证明的新机制。
两项仅可把下文精确差额交独立核对；任何一项若最终只剩一般理论代入，都应淘汰当前形式。

本人 FULL 读取 `novelty-check/SKILL.md`、`research-lit/SKILL.md`、本轮 Phase A 与代数首筛。
自身覆盖首筛已完成，本轮重新全文读取；此前首筛阅读身份保留，不扩展为本轮所有原文证明已全文核审。
本轮实际执行24条查询：每项每核心至少3条，共18条核心查询，另6条追索；打开／定位不重复计数。
实际 CAS／候选运行／GPU 均为0；没有把纯理论问题称为缺GPU，没有下载新增PDF到本地文献库。

| 本地输入 | 实际读取范围 | SHA-256 |
|---|---|---|
| [Phase A](PAPER31_QPI_SURVIVOR_CLAIMS_PHASE_A_V1_20260909.md) | FULL | `be4a8b04354b762dc43cb9b7947248005c7f2c8612970387a2ef588b477d0b33` |
| [代数首筛](PAPER31_QPI_QUICK_FILTER_ALGEBRA_V1_20260909.md) | FULL 1–170 | `28746a09feaa908b5e0a532cff311332936c4710580b5e2724d307f621cc5702` |
| [覆盖首筛](PAPER31_QPI_QUICK_FILTER_COVERS_V1_20260909.md) | FULL 1–178 | `72f5f4a806d32ffd28ab1cf6704532aec0eaf81fd89f5e5d8e5beed8bed58e39` |
| [原全次数 jet 复形](PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md) | 定向1–245；含完整指标、矩阵与四簇推导，非全篇 | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| [接受原稿 trace 节](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex) | 定向1–235 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| [接受原稿首层节](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex) | 定向13–115、272–346；另关键词定位 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| [接受P30 PDF](../../papers/30-qpi-vertical-critical-ideals/build/natural-20260909-r4/work/main.pdf) | 本地文献入口，实读前3页；不重扫构建树 | `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |

## 2. 六个核心及检索对象

| 核心 | 方法检索 | setting 检索与必须留下的原对象 |
|---|---|---|
| I05-C1 原源模 | 整数 Pascal／Stirling、平移、除幂 | $R=\mathbb Z[\tau],q=1$，原 $\Lambda_n$ 与四末次 fat jets；不能换为完整多项式空间 |
| I05-C2 真实扩张 | 整数模呈示、Smith、连接映射 | 非PID底环上的原余核；须容纳已接受的混合块，不能只比较逐域不变量 |
| I05-C3 首素数厚化 | 模$p$ Jordan、二项系数、进位 | 每个$p$在原受限系统的首现及后续；$n=p+1$仍是问题 |
| I09-C1 实际类 | 显式局部下降、WC、野torsor | 原$m=a=1$、完整$t,c$、$I_p=c$、有限剩余域、$\bar c=h^p$且$J=h$光滑 |
| I09-C2 过滤桥 | Bockstein、Picard–Néron、Herbrand | 明确原类到过滤的比较；不是把不同目标群中的同名算子直接相等 |
| I09-C3 分裂消费者 | period/index、可分闭点、最小分裂 | 允许扩张类型与赋值归一化明确；通常光滑模型不换为log光滑 |

## 3. 实际查询日志

以下字符串均在2026-09-09执行。日期筛选用于定位，稿件年代以官方版本记录为准，不用网页抓取日期充新文献。

| ID／核心 | 查询字符串 | 返回与消费 |
|---|---|---|
| Q01 I05-C1 | `Pascal matrix Stirling unimodular change basis invariant submodule fat point jet interpolation binomial` | 定位Callan及若干离题离散jet稿；正文依据S1 |
| Q02 I05-C1 | `Callan Smith forms Pascal related matrices weighted translation polynomial ring restricted columns` | S1与Stirling矩阵文献；未命中原四簇稳定性定理 |
| Q03 I05-C1 | `site:arxiv.org 2024 2025 2026 Pascal matrix Smith normal form fat points interpolation` | 命中S2（2026-05），核对底环而非凭标题包含 |
| Q04 I05-C2 | `"integer" "translation" "difference" "module" "divided powers" extension` | 多为无关表示论／教材；不算排除性证据 |
| Q05 I05-C2 | `"fat points" "infinitely near" "integer" cohomology Harbourne` | Harbourne、fat-point碰撞线索；追到S3 |
| Q06 I05-C2 | `site:semanticscholar.org Pascal matrix Smith form polynomial module extension` | 公开S2域PDF索引多是域上矩阵理论；不冒称S2 API完整检索 |
| Q07 I05-C3 | `"Pascal matrix" "Jordan" "prime" "polynomial" first degree` | Bayat–Teimoori／Callan线索；实际定理用S1 |
| Q08 I05-C3 | `"fat points" "characteristic" "p" "binomial" interpolation` | 域上Hilbert函数、插值矩阵；未供应整族首现 |
| Q09 I05-C3 | `site:arxiv.org after:2026-03-09 before:2026-09-10 "Smith" "Pascal" "binomial"` | 未返回更贴近原对象的新定理；不声称无近期先例 |
| Q10 I09-C1 | `"q-Painlevé" "Weil" "torsor" local reduction` | 未定位原固定提升公式；泛torsor材料不作证明依据 |
| Q11 I09-C1 | `"genus one" "torsor" "explicit" "local field" good reduction wild` | 显式下降、Brauer分裂等邻近材料；须分清局部／全局 |
| Q12 I09-C1 | `site:arxiv.org "torsors" "elliptic" "2024" "2025" "2026" ramification` | 无直接原qPI公式；结合Q20及主控新命中核S8、S9 |
| Q13 I09-C2 | `"Bockstein" "torsor" "elliptic" ramification` | 命中Petrov–Skorobogatov，追到S8正文 |
| Q14 I09-C2 | `"Bertapelle" "Tong" "filtration" "torsors"` | 定位S6；重开原PDF核过滤定理 |
| Q15 I09-C2 | `site:scholar.google.com "genus one" "wild" "conductor" "Picard"` | 未获得可核Scholar正文结果；不冒称登录／全库检索 |
| Q16 I09-C3 | `"Mitsui" "torsors" "index" separable closed points` | S4官方刊本／摘要 |
| Q17 I09-C3 | `"elliptic" "torsor" "minimal" "splitting" "wild" local field` | 新增Zimmermann S7强包含入口 |
| Q18 I09-C3 | `site:arxiv.org after:2026-03-09 before:2026-09-10 "elliptic" "torsor" "period" ramification` | 未检出直接本题；近六个月另核S8 v2及S9新稿 |
| Q19 I09追索 | `"The torsion in the cohomology of wild elliptic fibers" arxiv` | 获S7官方arXiv，与被拒刊商页面分开 |
| Q20 I09追索 | `"On spectral sequences for semiabelian varieties over non-closed fields" arxiv` | 获S8作者版与2026刊版元数据 |
| Q21 I09追索 | `"q-Painlevé" "torsor" "reduction" arithmetic local` | 无原完整提升代表；不据此判定新颖 |
| Q22 I05追索 | `"Anticanonical rational surfaces" Harbourne pdf` | 获S3，实读摘要／引言／Theorem I.1 |
| Q23 I05追索 | `"relative" "clusters" "infinitely near" "points" Kleiman Piene` | 相对cluster／Enriques图线索；未读其全篇，不作结构包含票 |
| Q24 I05追索 | `"integral" "Pascal" "Smith" "translation" site:scholar.google.com` | 无可核直接Scholar条目；核心矩阵结论仍限S1 |

公开网页、arXiv、作者／机构存档、Numdam／Mersenne刊本与本地接受PDF实际可用。
Zotero／Obsidian工具未配置；本轮未冒称使用。ML会议数据库与此纯算术／代数问题无主题适配，不以空跑充覆盖。
Google Scholar／Semantic Scholar仅作公开域定位，没有绕过登录、限额或权限；本件不冒称全部可见数据库被穷尽。
主控补送S9的arXiv元数据入口后，本人打开并定向实读其引言、主定理和§2.1；不是继承主控摘要当正文阅读。

## 4. 一手来源及实际阅读层次

### S1. Callan：完整 Pascal 的整数与模$p$规范形

[Jordan and Smith forms of Pascal-related matrices，arXiv:math/0209356v1](https://arxiv.org/html/math/0209356v1)，2002-09-25。
实读全部数学正文§§1–5（HTML34–113），含Theorems1–3及证明；原摘要由arXiv条目核对。
完整 $P_N$ 经Stirling整基变换得到模$p$ Jordan块；$(P_N-I)^r$整数等价于升阶乘系数对角矩阵。
§5给带权Pascal卷积恒等式，不是任意参数环／受限列的Smith分类。
HTML自动显示的2026-08日期不作新版本；正文矩阵 $J_N(\lambda;\ldots)$ 也不是本项目 $J_n$。
包含限度：完整空间的除幂／进位与Jordan机制已知；四簇共享的原源是否保留，必须另给实际变换。

### S2. Lu–Ruan–Wang–Xiao：近期多变量 Smith 等价

[Matrix equivalence to Smith normal form: new theoretical results for multivariate polynomial matrices，2605.09286v1](https://arxiv.org/html/2605.09286v1)，2026-05-10。
实读摘要、§1引言相关工作、Problem1与§2起始底环条件（HTML34–69）；未审全篇证明。
底环为域 $\mathbb K$ 上多变量多项式环；主类以特定三角形因式行列式和各阶约化子式生成单位理想刻画等价。
该文明确提醒一般约化子式判据并不充分。不能把 $\mathbb Z[\tau]$ 中整数素数当成域上的另一变量。
因此它加强“先核底环与理想”的审查要求，但不提供本原非标量扩张分类。

### S3. Harbourne：任意特征域上的反典范线性系

[Anticanonical Rational Surfaces，alg-geom/9509001v2](https://arxiv.org/pdf/alg-geom/9509001v2)，1996-01-24作者版，1997刊行。
实读摘要、完整引言、Theorem I.1及紧邻说明（PDF前2页），另读第3页基本引理；非全文。
取代数闭域任意特征，光滑射影有理反典范曲面；Theorem I.1针对nef除子，描述截面／$h^1$与固定部。
非nef类须另知有效锥并去固定部；不能直接把零时间整个 $-nK$ 当nef。
这扣除逐域线性系维数与几何呈示思想，不将这些域上数值自动提升为 $\mathbb Z[\tau]$ 扩张等价。

### S4. Mitsui：最小分裂次数不是新机制

[Models of torsors under elliptic curves，2017官方刊本](https://pmb.centre-mersenne.org/item/10.5802/pmb.16.pdf)。
本轮重读摘要、引言、Theorem1.1／Corollary1.2／Theorem1.6全部条件（PDF第2–3页）；分类表未重审。
完整DVR上亏格一扭子有次数等于index的可分闭点；有限剩余域时period=index，故最小分裂次数为period。
Theorem1.6对非有限剩余域有额外WC-trivial与扩张条件，不能无条件套到任意剩余域。
原能级的period值、具体分裂扩张及其最小分歧仍需输入；“存在最小度分裂域”不能单算贡献。

### S5. Mitsui–Smeets：log-unit／法丛／log光滑

[Logarithmic good reduction and the index，1711.11547v3](https://arxiv.org/pdf/1711.11547v3)，2023-06-15版本。
本轮重读引言Theorem1.2、§4设置／Lemma4.1／Proposition4.2及证明；§5／ordinary限制沿自身首筛已读范围消费。
§4先要求proper flat **log-regular** 模型；特殊纤维公重数$m$、约化纤维法丛阶$\mu$满足某处log光滑当且仅当$m=\mu$。
证明已经比较log-unit微分与法丛$p$-挠，不能把这种对应另起名称当新桥。
亏格一定理在代数闭剩余域下将log好约化与tame $H^1_\ell$及$p\mid m$时的好Jacobian／上同调平坦相连。
原特殊纤维写成$pX$不自动证明原总模型log-regular；log光滑不等于通常光滑。

### S6. Bertapelle–Tong：完整 Picard–Néron 过滤先例

[On torsors under elliptic curves and Serre’s pro-algebraic structures，1204.2805v2](https://arxiv.org/pdf/1204.2805v2)。
本轮重读摘要／引言前页、§2.1的加厚Picard正合列、Theorem3.4.3／Corollary3.4.4；§2.3范围沿首筛消费。
前提为完整DVR、代数闭正特征剩余域与原扭子的proper regular minimal模型；不要求ordinary。
$\psi(n)$组织加厚曲线，$q:\operatorname{Pic}^0\to J$将相应过滤映到Néron过滤，有限层核由法丛限制生成。
泛“以上同调厚度得到Herbrand型函数”已被包含；有限剩余域的下降与原$t,c$代入仍未供应。
版本标识为2013-11-21 v2，PDF内稿件日期2017-07-12；不伪称核过另一刊本或57页全部证明。

### S7. Zimmermann：更强的野上同调—分歧跳跃公式

[The torsion in the cohomology of wild elliptic fibers，1909.10891v2](https://arxiv.org/html/1909.10891v2)，2020-08-22版本。
新实读摘要／引言、Theorem2.4、Theorem3.3及其条件、§5 Theorem5.1与公式；非14页全文证明审计。
$M_{X/K}$是使正规化基变换向原总模型为étale覆盖的最大基域，不定义为任意选取的分裂域。
在相应正规化模型的$H^1$自由时，$\operatorname{tors}H^1(X,\mathcal O_X)\simeq H^1(G,R')$，$G=\operatorname{Gal}(M_{X/K}/K)$。
代数闭剩余域、ordinary好约化给所需自由性；supersingular不能静默套这一分支，需例如另证$X_K(M)$非空。
Theorem5.1在ordinary好约化或乘法约化下进一步给wild群循环及由下编号分歧跳跃决定的扭子指数公式。
所以连泛“分歧跳跃决定精确厚度”都不是剩余；原类如何确定该$M$以及有限剩余域下降仍是任务。
该刊商网页403保留；使用独立公开arXiv作者版，没有绕过原权限。HTML2026排版日期不改2020版本年份。

### S8. Petrov–Skorobogatov：同名 Bockstein 不同目标

[On spectral sequences for semiabelian varieties over non-closed fields，2411.15353v2](https://arxiv.org/html/2411.15353v2)，2026-06-12版本；初稿2024-11-22。
新实读摘要、引言相关工作与§5 Theorem5.1及证明（HTML约631–683）；未全文核审。
任意域$k$、$\operatorname{char}k\nmid n$、semiabelian torsor $X$：Hochschild–Serre首微分类为$\beta_n([X])\in H^2(k,A[n])$，相应$d_2$为cup乘。
此$\beta_n$来自乘$n$的Kummer序列；在I09特征零分式域$K$可取$n=p$，不能因剩余特征为$p$误排除。
但原$\beta_L$来自$0\to k\to\mathcal O/(\pi^2)\to k\to0$作用于反典范层，目标为$H^1(X_k,\mathcal O)$。
本先例不提供二者的比较，也不是从原几何Bockstein反求完整WC类；泛Bockstein叙事必须扣除。

### S9. Shang–Niu：最新全局反例并非局部反例

[Counterexamples to O'Neil's Period-Index Problem on Elliptic Curves，2608.29288v1](https://arxiv.org/html/2608.29288v1)，2026-08-29。
新实读摘要、引言Theorem1.1、§2.1到Hilbert配对设置（HTML40–192）；未核全篇或Magma证书。
主定理在数域$\mathbb Q(\zeta_8)$构造period8、index16而所有$E[8]$提升的障碍阶为8的族。
它反驳的是O'Neil全局提升障碍的最优阶问题；引言明确另述局部period=index，不推翻S4。
不能用该文反例包装原局部$p$层差额，也不能把有限平坦／Kummer提升本身当已识别的原$t,c$代表。

## 5. I05：对实际源的可检验比较

原源是$V_n=R\langle x^iy^j:(i,j)\in\Lambda_n\rangle$，不是$R[x,y]_{\le2n,\le2n}$。
除方框界外，原指标满足$n+i-j\ge0$、$i+j\ge n$、$i+2j\ge2n$、$i+j\le3n$。
四簇分别读取四个线性切片$2n-i$、$n+i-j$、$i+2j-2n$、$3n-i-j$；同一源列同时参与不同簇。
只对一个切片简化的Pascal基不能未经证明就成为全$V_n$的相容基；目标行变换也须同一复形内合法。

一个本轮直接代数见证是：$(2,2)\in\Lambda_2$，但普通张量下降阶乘变换给
$$x^2y^2\longmapsto x(x-1)y(y-1)=x^2y^2-x^2y-xy^2+xy.$$
其中$(1,1)\notin\Lambda_2$，因为$1+2\cdot1<4$，而其系数是整数单位1。
故这一完整多项式空间上的整可逆变换不限制为$V_2$的自同构；以$\tau$作步长同样出现非零$\tau^2xy$。
这是对具体快捷变基的反例，不是对所有适配变换的反例，更不是全次数新结构定理。

I05-C1的实际剩余：给一个保持四簇原评价的整数递推／过滤及明确比较矩阵；若S1型适配变换直接做到，应扣为推论。
I05-C2的实际剩余：恢复连接映射／扩张类，至少精确再现已接受$(\tau^2,2\tau)^t$；逐域Smith、Fitting一致不代替整模同构。
I05-C3的实际剩余：严格排除每个$p$的更早厚化并证明全部后续规律；完整$P_N$的首$p$-Jordan断点不自动给原$n$。
旧$\tau^5(\tau,2)$已否定全标量对角化；本轮没有重猜、绕开或把它误解释为非标量递推不可能。
仅再做$p=3,5$几个样本不填这三项差额；只重述除幂／进位机制的版本应直接淘汰。

## 6. I09：原提升、三种连接和真实消费者

先扣除原谱Jacobian的好约化：小阶光滑、$T=t^p,\bar c=h^p$使旧判别式约化为小阶判别式$p$次幂。
原接受$\kappa_J=[\overline{(j_j-j_i)/\pi}|_X]\ne0$是反典范层几何Bockstein的限制。
超奇异层的$\partial\nu=\operatorname{Fr}_*\kappa_J$位于$H^1(X,\mathcal O_X^p)$；到$H^1(X,\mathcal O_X)$的后续像为零。
这些目标群与S8的$H^2(K,E[p])$、原WC群$H^1(K,E)$不同；没有给比较映射就不能彼此替代。
又原$d_{\rm state}I_p$固定基参数、微分不显式含$c$；只持有旧有限jet不等于已经读取所有完整能量提升。
这不证明有限jet必然不够：也可能类在相关提升邻域内恒定，但这种恒定性和所需截断精度都必须实际证明。

I09-C1的实际剩余：在固定完整$t,c$下产生可计算代表／局部对偶泛函，证明代表就是原扭子，并给零类判定。
仅定义$\sigma Q-Q$未完成该任务；还需原$E$作用、分裂点、Galois作用与取值坐标的实际计算。
I09-C2的实际剩余：先固定所称过滤，识别原类与S6或S7的输入，再求层级；一般Herbrand函数或log-unit式已被包含。
S7的$M_{X/K}$、一个末端根域及全体最小度分裂域可能是不同对象；没有比较不能共用同一“分歧深度”。
有限剩余域到代数闭剩余域的扩张／下降须给出，ordinary／supersingular条件必须分别保留。
I09-C3的实际剩余：在上述类已知后计算原提升分层的分裂条件与必要扩张；S4的最小次数存在性预先扣除。
在有限剩余域且Jacobian好约化下，通常光滑proper模型给剩余域点并由Hensel提升；反向由分裂识别到好Jacobian模型。
所以“通常光滑模型存在”这一抽象等价本身也不算剩余；原类是否分裂才是具体消费者。
$b_p(w)=c$有原域根可给原曲线点，无根只排除该末端点；根域不同式不是所有分裂域的最小不同式。
若独立核对发现原全提升比较仅等于S5的已有log-unit构造，或唯一输出是标准Newton多边形例题，应淘汰此形式。

## 7. 未供给输入与交付边界

I05未供给适配全源的实际整数变换、全次数扩张递推与全素数首现证明；本件不把不稳定见证升级为全球新意。
I09未供给原完整WC代表、与S6／S7／S8的具体比较、有限域下降或分裂的必要充分计算；本件不把缺公式升级为价值证明。
最新范围确实覆盖2024–2026并检查2026-03-09至09-09：S2、S8 v2、S9有官方近期日期，相关性分别核定。
公开搜索没有穷尽有限平坦群概形和显式局部下降文献；未读的Kleiman–Piene／Sen原作不列作本人正文核审。
部分多工具合并显示被截断时，只把明确可见的指定段计入实读；本件的局部范围不冒充FULL。
唯一新增持久文件为本报告。未改冻结输入、未启动独立Phase C、未运行实验／构建、未对外写入或申请付费资源。
提交前全文自读、上述7件输入哈希核对及本件本地相对链接存在性核查；最终行数／SHA在交付消息提供。
