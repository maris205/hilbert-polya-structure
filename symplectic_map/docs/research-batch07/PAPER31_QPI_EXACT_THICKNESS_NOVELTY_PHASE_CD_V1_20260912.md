# Paper31：原固定 T 准确厚度——独立查新 Phase C/D V1

日期：2026-09-12 UTC。独立评价席：`/root/p31_exact_thickness_phase_cd_v1`。
状态：`NOVELTY_REVIEW_COMPLETE_WITH_SOURCE_GAPS`；route_applicability: NOT_APPLICABLE。
本件是 novelty-check 的有界 C/D，不是正式候选四门、数学复审、容量票或论文准入。
技能指定的 GPT-5.4 MCP 未配置；按本次授权使用实际可用 Codex xhigh 独立席，不称跨模型验证。
先完成指定作者／旧边界和一手来源阅读，再接收冻结[B]及[PORT]，本人读完后才作评分；无评分助手。

## 1. 结论

**总体新意：6.8/10；建议：PROCEED_WITH_CAUTION。**

这是有可信净增量的、特定带点椭圆切片的准确交数发现，不是新的 Manin／Igusa／Tate 方法。
在实际读到的最强先例中，没有发现直接包含 V1–V3 全部原数值及量词的定理；
但这一有限检索事实本身不给分，也不构成全球无先例证明。

正面的依据是实际输出发生了变化：原来已知回返支持和含未知 $i_n$ 的完整理想，
现在在规定范围内得到初始交数 $c_*$、Hasse 阶 $e_*$ 和节点唯一二阶例外，因而真正去掉未知局部长度。
保留闭有限群点阶 $d$ 并不把未知交数藏回答案。
谨慎的依据是：对象本来就是经典有标点 Tate 正常形；计算固定阶挠条件已有算法；
大部分推理链由通用定理和低阶展开供应。它比“把旧理想再写一遍”实质得多，
却仍有被视为标准工具在一个固定切片上的精细计算的明显风险。

6.8 是对本次统一发现新意的综合判断，不是数学正确率，也不是三个单项分数相加。
未按作者稿行数、数学 PASS、页数要求、搜索空命中或主控预期调分。
此处 PROCEED_WITH_CAUTION 只支持继续把这一单中心准确定位、交给后续决策；
不授 Paper31 的新意门、价值门、证明门或正文容量门，更不授权建项目、锁、稿件或编译。

## 2. 评价对象与不变范围

保持原 $F_T(x,y)=(T/(x-y),x/y)$、完整 $\mathcal U$、
$W_h:v^2+huv-Tv=u^3-Tu^2$、$P=(0,T)$、$O$、$T\ne0$ 和原 $z=h-h_*$。
记 $q=8h-9,H=32T+3h,i_n=(nP.O)_{h_*}$；不改变回返点或用分歧参数重计长度。

| 主张 | 方法新意 | finding 新意 | 扣除先例后的评价对象 |
|---|---|---|---|
| V1：forcing、真实好切触与 Hasse／Manin 根阶 | LOW | MEDIUM | 原规范 $-H/(q\delta)$、$N_p'=-q^{p-2}AH$；实际素于特征好切触的准确 2／3 阶及首项；好点 Hasse 零阶的准确 1／2 分类 |
| V2：全部素域好点的初始交数及全部迭代 | LOW | MEDIUM | $c_*=i_d$ 三分支的统一求值，特别是 $p\mid d$ 时 $1+\mathbf1_{q=0}$，并确实包含超奇异、好点 $q=0$ 和 $p=5,d=10$ |
| V3：全部有限节点的唯一二阶例外 | LOW | MEDIUM，三项中最鲜明的具体现象 | 固定原 T 的首项、$p>5,(T,h_*)=(3/16,-2)$ 的唯一例外和非零二阶首项，及它们在原 h 上的无分歧识别 |

V1 的好切触断言是特征零，或代数闭特征 $p>3$ 且 $p\nmid n$ 时的**实际切触条件阶**；
它不定位所有真实发生处。一般正特征 $N_p$ 根不能反推真实切触，三阶好切触存在性也未证明。
V2 是所有 $p>3,T,h_*\in\mathbf F_p$ 的好点、所有 $n\ge1$，不是全部几何好点或所有扩域。
V3 保持一般代数闭 $k$、$p>3$ 的全部有限节点及全部 n；非根单位没有回返，不能缩成素域。
特征零有限阶节点全部横截是其已证边界；尖点、无穷、$T=0$ 及一般非自治相对作用均不在分类内。
这些边界是准确研究合同，不是本席为提高评分而删改或追加的要求。

## 3. 最接近先例与直接包含

| 一手来源 | 年份／身份 | 直接包含的部分 | 没有据此认定已包含的部分 |
|---|---|---|---|
| [Ulmer–Voloch][UV]，§§2–3、4.7、4.11–4.12 | arXiv v1 2025；当前正文另写 2026-08-24 | 正特征局部界、兼容 Igusa 速度；complex-Betti 准确读阶、修正端点及显式算例 | 原 H 因子、原切片的 $c_*,e_*$ 和节点例外 |
| [Voloch][V90]，Theorems 3.1、6.1 | Compositio 74 (1990) | 下降同态及其与特征零 Manin 映射模 p 的导数联系 | 原规范乘子、Hasse 消失处准确阶及原 forcing 求值 |
| [Broumas][B97]，Theorem 4.1、§4.1、式(30)–(31) | Compositio 107 (1997) | Frobenius 扭曲上的导数同态、兼容规范与显式下降 | 原固定切片的准确初始化 |
| [Naskręcki][N16]，Lemma 8.2 | NYJM 22 (2016) | 当局部 Hasse 阶不超过 $p-1$ 时的全部倍数交数公式 | 首次交数和本族 Hasse 阶的实际数值 |
| [Gasull–Mañosa–Xarles][GMX]，Theorem 3、§2.2、§3.1 | arXiv 1004.5511 (2010) | 同一有标点 Tate／Lyness 正常形；奇异纤维分式动力学与根单位机制 | 固定原 T 方向的一／二阶接触分类 |
| [Clark–Corn–Rice–Stankewicz][CCRS]，§§2.1–2.2 | LMS J. Comput. Math. 17 (2014) | 同一 Kubert–Tate 对象及固定 N 的挠条件多项式算法 | 本次全部 p、素域好点的统一低阶分类 |
| [Tate][TATE]，式(4)、(11)、(14)、Theorem 1 | 历史稿 1959，所用重排综述不臆定刊年 | 整数级数与乘法同态 | 保持 T 恒定后的唯一例外和原 h 首项 |
| [Hone][HONE]，§6、Theorem 6.1 | arXiv v3 (2020) | 带点曲线变换和 QRT 标量乘法算法 | 基方向局部交数 |
| [Ulmer–Urzúa][UU]，Theorems 1.1、1.7–1.8 | 所读 arXiv v4 (2020)；出版 2022 据[B] | 特征零相切有限性和有明确条件的 very general 横截性 | 每条固定 T 切片的全参数分类 |

最重要的对象识别不是“与 Lyness 相似”，而是原曲线本身为 $E(b,c)$，
$b=T,c=1-h,R=(0,0)=-P$。在 GMX 变换的共同图表上，

$$
a_L=\frac{(1-h)^2+1-h-T}{(1-h)^2},\qquad
h_L=-\frac{T}{(1-h)^2}.
$$

因此固定 T 通常同时改变两个 Lyness 参数；固定 $a_L$ 的结果不能不核方向就套来。
反过来，也不能把该参数方向差异夸张为一个新椭圆模型。小阶及被除参数的图表边界仍须保留。[GMX]

另补核了比 2026 讲义更早的明确导数先例：Voloch Theorem 6.1 的原图是
$M\equiv a\delta\mu\pmod p$，$a\in K^\times$；不是只到“作者猜测有联系”。
一般导数桥必须扣除，但函数域中的非零乘子不自动给原模型中每个闭点的准确首项，
特别不能代替对 Hasse 零点和原规范的核算。[V90]

## 4. 为什么还剩 finding，为什么仍只给中等新意

### V1

新[G]/[C]输出的是原截面的显式因子及正特征低阶无遗漏结论，而不只是套一个有限性界。
普通点与超奇异点在原局部展开中走不同阶数，最后得到一致的真实 2／3 阶，这是有内容的准确求值。
但特征零部分在 forcing 已知后已是通用准确读阶的特例，不能把“计算 forcing”与“读出 2／3”各算一次突破。
Hasse 零阶把旧未知 $e_h$ 变成 1 或 2，具有实际消费者，但仍属该切片模映射退化的具体控制，未建立新的通用机制。
正特征好点 $q=0$ 无素于 p 切触已在旧[M]71–72、354–365行，必须扣除；本轮互补的新结果不能掩盖此旧项。

### V2

这是统一结果最有用的部分：在规定全部素域好点，答案不再含未知 $i_d$。
尤其 $p\mid d$ 分支不被旧 $N_p$ 的 prime-to-p 支持判据直接覆盖，新[PP]给其准确初始值。
然而该分支从已有兼容 Igusa 速度和 $\operatorname{ord}\lambda\in\{0,1\}$，经低于 p 的局部积分得到；
方法的特殊技巧不能按“首次处理 p-primary”放大为新的下降理论。
合并后全部 n 的公式及好点固定理想只是标准传播和旧[FIX]的消费者，不构成额外创新。
所以 V2 具有真实统一 finding 增量，但方法和设置的新意显著弱于一个新的普遍交数定理。

### V3

唯一二阶节点例外是最清楚、可复述且确实发生的算术现象：$p>5$ 时相应乘法元素在有限域代数闭包中有有限阶，
而特征零该二阶候选不是根单位，不贡献有限阶回返。它不是三阶好切触未证存在性的另一种说法。
新[NODE]还算出非零二阶项，并保持原 h 和原 P 的符号，故不是只找到一阶可能消失的必要条件。
但其证明核心是普遍整数 Tate 展开、带点正常化、固定 T 的隐函数消去及二阶 Taylor 求值。
这是一项有特点的局部分类，尚未显示可独立移植的新理论；具体数字本身不保证高新意。

三项共用 $W_h,P,T,z$，并共同求原理想中的标量，凝聚性真实成立。
$H=w(2w+1)(4w-3)^2$ 对接好点 forcing 和节点例外，是有助理解的同源性证据，
不是第四个发现，也没有被升级为新的全退化定理。[A][SYN]

## 5. 本地非碰撞、风险和诚实定位

[PORT]给出的实际本地比较支持“原准确标量尚未被既有接受论文供应”。本席消费这份冻结独立报告，
没有继承其对 Papers 11／18／29／30 正文的实读身份。本人另完整读旧[OLD]，确认旧素域充要性和完整固定理想已经真实存在。
因此不把“从点集升级概形”“首次拥有固定理想”“首次提出旧 I03”当本轮卖点；
也不因此前已经提问就否定本轮确实求出的新数值。

最合适的定位是：**固定 Tate 参数切片上的准确算术接触阶及其原 qPI 固定厚度实现**。
主叙述应是初始交数的统一求值，之后简短给标准全倍数及旧理想消费者。
不宜声称“新的 Manin 方法”“首次联系特征零与正特征”“首次发现高阶相切”或“全部几何固定厚度已分类”。

主要风险依次为：

1. 审稿人将正常形、已有下降读阶和有限阶挠多项式算法合起来，认为剩余为例行的专门切片计算。
2. 未覆盖的 Duistermaat 正文或其它固定 b 文献直接包含同一初始分类；有限检索与访问失败均不能排除它。
3. 把三项相互依赖的结果和标准消费者重复计功，或把 2／3 条件阶包装成全部异常位置／三阶存在性。
4. 本地非碰撞只说明没有重复已读本地定理，不能替代外部新意；数学证明接受也不能替代新意。

上述风险没有把当前结论判作无价值或假定它永远不能成文。
本席也不追加“先关闭全部扩域、尖点、无穷或旧 I03 才可研究”的新合同。
按现在的证据，保留这一凝聚 finding 并谨慎定位比直接宣称高新意突破更准确；正式候选决策仍另行进行。

## 6. 本人实际输入阅读账

以下哈希由本席实际 `sha256sum` 核定，绑定整个文件；FULL／PARTIAL只修饰本席读到的范围。
首次合并读[B]/[PORT]有极短输出截断，已另读[B]195–241行补齐；两件现均本人FULL。
路径除技能外均相对工作区，研究文件均位于 `docs/research-batch07/`。

| 输入 | 本人范围／总行数 | SHA-256 |
|---|---|---|
| AGENTS.md | FULL 1–28 | `73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412` |
| docs/WORKFLOW.md | FULL 1–39 | `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2` |
| `/root/autodl-tmp/.codex/skills/novelty-check/SKILL.md` | FULL 1–86 | `bf82687716497fd301e828fd8eb835815eb16d3d9267c1f9dd0849b3a05948df` |
| [A] | FULL 1–157 | `171e8aa602d6431e76672c79cf6962c9269f73a6f91993ef7c131a697a4ac917` |
| [SYN] | FULL 1–245 | `5400ed2775b3a91f85c814d9c8c8fb252dc91cf8577579f63da0cee87e7539d1` |
| [G] | FULL 1–267 | `c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b` |
| [C] | FULL 1–281 | `7ec721bfac1d43f214dc9c8b3906c8bab131fe53b67fd6c48e06eeaa752f27aa` |
| [PP] | FULL 1–254 | `38805df5657731f6698b3fcc3356269cb02da2e2c952779b5750ec6fe8442449` |
| [NODE] | FULL 1–346 | `5b61cbc732fbd70d6edd1979d183d50081ea1cac3d849164422447c5c785cf27` |
| [OLD] | FULL 1–176 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [M] | PARTIAL 1–87、354–365／446 | `48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2` |
| [PF] | PARTIAL 1–87／325 | `de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef` |
| [FIX] | PARTIAL 1–84／348 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [B] | FULL 1–241 | `efa6763b9246b526a4b27fccc102afabcc382173b4fb0797de5a302410be1832` |
| [PORT] | FULL 1–180 | `3c15b22b2ea418c28fd35c3d205be48fec6332fa057991aae058c1829351b5ba` |

未读新数学独查、增量批评正文或[B]/[PORT]并发草稿；没有由其中转述升级本人阅读身份。
不重审已接受的数学，不运行新 CAS、F5 或其它采样。

## 7. 本人一手来源阅读与搜索边界

| 来源 | 本人实际范围；不声称整篇 FULL |
|---|---|
| [UV] | 官方 HTML 摘要／引言、§§2–3全文、§§4.4–4.12全文；另读§4.1–4.3部分。直接核对 Proposition4.7、4.11 和全部三个 Legendre 示例段落 |
| [GMX] | PDF Theorem3（p.4）、§2.1、§2.2全文（p.8）、§3.1节点部分至根单位排除；即相关 pp.4–10，不把其它章节当已读 |
| [N16] | PDF 印刷 pp.1003–1005 全文：定义、Lemma8.2全部陈述与证明及tame定义 |
| [TATE] | PDF pp.1–7全文，含整数级数和同态／核证明；未读后续满射证明及全部后半综述 |
| [HONE] | 官方 HTML 摘要、§§1–3全文、§6全文与Theorem6.1；未把全部其余章节计入 |
| [UU] | arXiv v4 PDF 引言及Theorems1.1、1.4、1.7、1.8，§§2.1–2.6；未读其横截性主证明 |
| [CCRS] | 出版 PDF pp.509–513，§1及§§2.1–2.2全文，特别是固定 N 的算法与Möbius分解；未消费p.514图形 |
| [V90] | 扫描PDF文本定向读§§1–3及§6相关陈述；展示公式有丢失，不称逐式全文。另下载到临时目录并实际视觉读印刷p.257整页，核准Theorem6.1展示式和完整短证明 |
| [B97] | PDF文本定向读取Theorem4.1及证明、§4.1式(12)–(13)、Theorem4.2／式(21)相关段落、式(30)–(31)及说明；提取存在缺号，未逐式视觉核准或读整篇 |
| [V26] | 作者讲义 PDF 11页／提取文本125行全部读完。January2026，不属于最近六个月；p.9述导数联系，只作已知方法的旁证，不代替[V90]正式陈述 |
| [OTT] | 官方摘要、题录及提交历史：v2为2025-09-10；只作特征零一般有限性的邻近线索，未读正文 |
| [GREENE] | 官方摘要、题录及提交历史：2026-06-01；只作近期相邻检索线索，主题为torsion pairing／intrinsic subgroup，不据摘要排除全文 |

[UV]页头为2025-08-08 v1，而正文Date为2026-08-24；本席保持该差异，不造新版或出版日期。
[V26]搜索结果的“六个月”标签不能覆盖正文January2026；[GREENE]确在2026-03-12至2026-09-12窗口内。
本席另打开 Ulmer1991 作者PDF得到 Internal Error，未取得原文；[B]对它的阅读不继承为本人阅读。
Duistermaat、Scholar／Semantic Scholar缺口按冻结[B]如实保留，本席没有重复尝试或绕过访问边界。

本席补做的实际三条 Web 查询如下；[B]的35条检索及6项数据库检查是该来源阶段工作，不充本席次数：

- `site.arxiv.org Lyness elliptic "tangencies" "2026"`
- `site.arxiv.org "Tate normal form" "intersection multiplicities"`
- `site.arxiv.org Ulmer Urzua transversality sections elliptic surfaces`

上述查询用于定位强先例／近期作者材料，不凭空命中排除原创。其余调用为打开已指明一手来源、定位和阅读。
[B]已完成逐主张及近期窗口检索；本席消费其覆盖账，同时本人重读最强相关来源，不宣称穷尽所有数据库。
技能使方法与 finding 分列、加入最强反向先例并保留访问缺口；没有因此暂停已授权工作或改变三项科学范围。

## 8. 交付边界

唯一新增工作区文件为本报告，使用 apply_patch；临时目录只存公开Voloch来源和阅读用渲染图。
没有修改冻结稿、[A]/[B]/[PORT]、旧失败、锁、BATCH、README或论文产物。
无项目／稿件／PDF／GPU／外部写入。本报告完整读回后的实际行数及输出SHA-256随交付消息报告，避免自哈希循环。

[A]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md
[B]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_B_V1_20260912.md
[PORT]: PAPER31_QPI_EXACT_THICKNESS_PORTFOLIO_DELTA_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[PP]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[NODE]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[OLD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1
[V90]: https://www.numdam.org/article/CM_1990__74_3_247_0.pdf
[B97]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf
[N16]: https://nyjm.albany.edu/j/2016/22-46v.pdf
[GMX]: https://arxiv.org/pdf/1004.5511
[CCRS]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/66737ACC99BC2D4F70EE3A2D38FF1EB6/S1461157014000072a.pdf/computation-on-elliptic-curves-with-complex-multiplication.pdf
[TATE]: https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf
[HONE]: https://arxiv.org/html/2001.09076
[UU]: https://arxiv.org/pdf/1908.02208
[V26]: https://www.math.auckland.ac.nz/~hekmati/Akaroa2026/Voloch.pdf
[OTT]: https://arxiv.org/abs/2506.15344
[GREENE]: https://arxiv.org/abs/2606.01571
