# Paper31：闭合非单位时间算术链的独立查新 C/D V1

日期：2026-09-10 UTC；执行席：`/root/p31_qpi_novelty_cd_i08_v1`。
`NOVELTY_PHASE_C_D / CLOSED_CHAIN_REVIEW / CAUTION / NO_FORMAL_ADMISSION_VOTE`。
`route_applicability: NOT_APPLICABLE`；纯数学新意与价值判断，不是 Route A/B、数学复审或完整双份四门票。

## 1. 结论先行

对[Phase A][PA]的完整 C1–C3 同一链，本席给**整体新意 7.0/10、独立研究价值 7.0/10，建议 CAUTION**。
这是新闭合包的独立判断，不回写[旧 I05 6.5/CAUTION][OLD]，也不是把旧分数机械增加0.5。
当前已经得到有实质内容的原对象结构结果，不能再用“连接未闭合”“只有有限 Smith 样本”概括它。
但扣除 Taylor/Pascal、留数、Ext、双对偶、Fitting 和 Lucas 的机制后，主要剩余是一个固定算术曲面族的精确识别与计算；
尚不足以支持“新的一般理论”或“仅凭本次查新即可进入高新意长文”的强定位。

最有价值的差额是：原受限四簇的标记整数扩张，与原无扭商的完整整数格识别，在同一上同调对象上相接，
从而把旧呈示／低阶例子提升为所有次数、所有素数的实际理想和长度规律。
方法新意弱于发现新意；不能将 C3 的首现、消失、递推分成三种独立方法，也不能将 C1 在 D05 与 G 两阶段重复计功。

CAUTION 的具体含义是：保留这份完整结构结果，采用克制的原对象定位；不建议凭改题、重排消费者或新抽一张局部票直接启动写稿。
若按既有流程继续提交完整候选，必须仍由完整材料和正式门票承担判断，本件既不替代也不预授它们。
本轮没有新增数学实验需求，也不要求反复重审已接受且输入未变的证明；全文先例缺口被保留，不被转化为新颖性。

## 2. 审查身份、方法与范围

本席不是 D05、G、C、D 或 A 的作者；此前检查过 D05、固定 M4、C/D 工具及 A 应用，并本人全文读过 G。
本席还是[Fitting 来源增补][FS]的作者，故不是零接触或对该来源记录的外部盲审；本次不把自己的来源增补计为另一张独立新意票。
[C1/C3 来源][S13]由主控作者收集，[C2 来源][S2]由 G 作者收集，[组合差额][PD]由 D05/D 作者核查；这些是证据输入，不是三张非作者评分。

本人 FULL 阅读 novelty-check 与 research-review 技能，按任务执行 C/D 的逐主张比较、方法／发现分拆及最强反对意见。
指定 GPT-5.4 MCP 当前未配置，本轮定向工具元数据查找也没有找到该审查端点；按已授权的 Codex xhigh 审查要求使用可用非作者席。
没有调用 GPT-5.4、执行模型切换或取得其 threadId，不称跨模型验证或人类审稿。
本件按明确分工消费已完成 Phase A/B，不重新运行其全部搜索，也不另开代理递归审查；所有评分只来自本席本次判断。

[数学合取][MATH]确认原链已经接受，本件消费该状态，不再次签数学正确性。
FULL 读取七份新阶段／来源／组合文件；原 D05/G/C/D/A 消费本人此前同 SHA 的全文阅读，另定向刷新 D05/G 的主张与前提。
旧 C/D 本轮实际读取1–110、160–210行，包含 I05、6.5、最强反对意见及 D05 停止准则；没有冒称重读 I09 全部正文。
组合基线与必要接受源的本席实读范围见第8节，不继承其他席的全文阅读标签。

## 3. 精确对象与三项主张

固定 $q=1,R=\mathbb Z[\tau]$、原八截面曲面及其反典范层 $\mathscr L$，
$M_n=H^1(S,\mathscr L^n)=\operatorname{coker}J_n$，$T_n=\operatorname{tors}_{\tau}M_n$，$L_n=M_n/T_n$，$E_n=L_n^{**}/L_n$。
研究的是整族层上同调；$\tau=0$ 不获得可逆动力。对 $n\ge1$，置
$$I_{n,a}=\left(\binom{n-1-b}{a}\tau^b:0\le b\le n-1-a\right),\quad 0\le a<n,\qquad B_n=\sum_{j=1}^{n-1}j^2.$$

| 核心 | 已闭合、可比较的主张 | METHOD 新意 | FINDING 新意 |
|---|---|---|---|
| C1：[D05][EXT] 的原相邻扩张 | $0\to M_n\to M_{n+1}\to R\oplus2\bigoplus_{j=1}^{n}R/(\tau^j)\to0$；全部标记 Ext 类、严格降次数的整数恢复、$n\ge1$ 非分裂 | MEDIUM：有对象适配和完整连接，但基本操作标准 | MEDIUM：确切整模连接超出旧呈示；仍非规范块分类 |
| C2：[G][G] 的原格识别 | 原留数像 $\tau^{-n}\bigoplus_a I_{n,a}$；原连接在理想坐标中为 $\tau$ 倍右移；自然缺陷 $E_n=\bigoplus_aR/I_{n,a}$ | MEDIUM：核心是原余核与整数 Taylor 像的识别，不是新留数或格理论 | MEDIUM：本包最强的结构发现，统一全部原格；抽象像本身是短计算 |
| C3：[A][A] 的统一算术消费者 | 全局 $\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_a I_{n,a}$、特征扭长 $B_n+D_n(p)$、首现和全部数字规则 | LOW：标准行列式／格指数／Lucas 消费者 | MEDIUM：对同一原模的新全称结论，不分别为四个公式加分 |

这里的 MEDIUM 不是“只有猜测”；三项按当前接受范围均已有证明。HIGH 不因量词是“全次数”而自动授予。
$D_n(p)=\sum_{a=0}^{n-1}\min\{b:0\le b\le n-1-a,\ p\nmid\binom{n-1-b}{a}\}$，不是底层纤维维数，也不是完整有限群的 $p$-对数阶。
其首现是 $n=p+1$、增量 $p-1$，首次局部理想为 $\tau^{B_{p+1}}(p,\tau)^{p-1}$；
无缺陷当且仅当 $n/p^{v_p(n)}<p$，A 的 (Digit) 给全部后续次数的终止递推。零次数采用原空和／空积约定。
这些是同一格识别的统一算术输出，不以多个名称放大方法数量。

## 4. 最近先例、阅读层级与包含边界

下表同时列真正近邻与必须扣除的工具；“未供应原对象识别”不是“已排除该论文全部潜在包含”。
R/T/P 表示相关正文／定理声明／指定证明；本轮亲读外文全文的数量为零。

| 最近先例 | 年份／出处 | 本席本轮证据层级 | 已有内容及准确剩余 |
|---|---|---|---|
| Callan, *Jordan and Smith forms of Pascal-related matrices* | 2002，arXiv | 消费 S13 的 §§1–5 定理／证明记录；未本轮重读原文 | 完整 Pascal 整等价、模素数机制扣除；未见对原受限共享列的完整适配定理。[原文][CALLAN] |
| Maakestad, *Principal parts on the projective line over arbitrary rings* | 2008，Manuscripta Math.126；所读预印 v4=2020 | 本人 R/T/P：§3 Th3.1全声明与(3.1.1)证明，§4 Th4.1的系统／单位条件及证明 | 整数二项式过渡和有条件分裂已知；不是任意整数像格的无条件自由化。[原文][MAAK] |
| Kyomuhangi–Marangone–Raicu–Reed, *Cohomology on the incidence correspondence and related questions* | 2024，arXiv:2411.13450v1 | 本人 R/T/P：§2相关接口、§3定义、Th3.2全声明、Cor3.3和Lemma3.4指定证明；未读Th3.2完整证明 | 全次数正特征主部丛分裂递推是强先例；没有从所读定理构造原四簇整数比较。[原文][K24] |
| 同四作者, *Computing the cohomology of line bundles on the incidence correspondence and related invariants* | 2025，arXiv:2503.17522v1 | 消费 S2 的 §3 实读记录，未本人重读原文 | 有分裂／上同调计算接口；算法名称不能替代原 $M_n$ 的输入识别。[原文][K25] |
| Griffiths, *Variations on a theorem of Abel*；Cattani–Cox–Dickenstein, *Residues in Toric Varieties* | 1976，Invent. Math.；1997，Compositio Math. | 消费 MATH、S2 明示的相关定理／证明范围，不继承全文标签 | 全局留数和、局部留数接口全扣除；实际四中心、标架及整数像仍需计算。[Griffiths][GR]、[CCD][CCD] |
| Galuppi, *Collisions of fat points and applications to interpolation theory* | 2019，J. Algebra534 | 消费 S13/S2 的设置、Construction10及相关命题／证明记录 | 碰撞、平坦极限和限制序列已知；一般复数碰撞的结论不直接是此整数受限源的标记 Ext 类。[原文][GAL] |
| Rowland, *The number of nonzero binomial coefficients modulo $p^\alpha$* | 2011，J. Combinatorics and Number Theory3 | 消费 S13 的 §1与§2相关定理／证明记录 | Lucas/Fine、数字递推机制扣除；本题将一个具体数字差和绑定到原上同调，不是新的数字理论。[原文][ROW] |
| Stacks §15.8；Ohm, *On the first nonzero Fitting ideal of a module* | 官方数学条目；2008，J. Algebra320 | Stacks消费S13；Ohm为本席此前官方摘要层，见FS | Fitting 基变换、主／可逆首理想与去扭商的联系均属先例；不能用主理想结论替换当前非主理想。[Stacks][STACKS]、[Ohm][OHM] |
| Hadjirezaei, *First nonzero Fitting ideals, reflexive defect, and local cohomology* | 2026，JPAA230(8),108300 | 本席此前官方索引摘要、引言、Th1.3声明及预览；本轮FULL重读FS，仍无正文全文 | 双对偶缺陷不是新概念；通用 D 因子机制继续扣除，全文对其精确包含未排除。[官方页][HAD] |

Perkinson 的关键交换图、Guardo 等后段、2013 UFD 首 Fitting 文的读取限制继续按 S2/S13 保留；本件不暗中将其状态清空。
本轮新增字符串查询为0；沿既给一手链接定向读上述两篇强先例，不声称重做 Phase B 的近期 arXiv／Scholar／S2 检索。
2024–2026及最近六个月的覆盖消费 S13/S2 的实际查询与失败记录；索引覆盖不等于穷尽，正文 HTML 生成日期不改写发表／版本日期。

## 5. 最强包含压力：明确能压缩什么、还不能压缩什么

### 5.1 抽象格与右移确实被一个短 Taylor 计算吸收

本人逐式核对了 S2 §2 的比较推导。令 $N=n-1$、$A_N=R[U,V]/(U,V)^{N+1}$，
$$\mathcal T_N(U^aV^b)=(-1)^{N-a-b}\binom{N-b}{a}\tau^b e_a\qquad(a+b\le N).$$
不同 $a$ 的源单项式独立，故其像恰是 $\bigoplus_a I_{n,a}$；不是从一般矩阵的逐行内容理想猜其完整像。
乘 $F=U(\tau+V)$ 后截断，则 Pascal 恒等式直接给
$$\mathcal T_{N+1}\circ m_F=\tau\,\operatorname{sh}\circ\mathcal T_N.$$
边界 $a+b=N$ 的被截断项，其二项式系数亦为零；没有遗漏一个额外边界修正。
各理想含非零整数常数和一个纯 $\tau$ 幂，指定嵌入下的双对偶为 $R$ 也是 UFD 的短推论。
这条**实际对象映射及其前提**充分否定“抽象二项式格＋右移＋双对偶是三种新机制”的说法。
这是 S2 的比较计算，不谎称这些记号／理想原样出现在 Maakestad 的论文中。

若要用这条计算直接包含原对象，还须构造原 jet 与该 Taylor 像的整数比较，并匹配原留数映射，
证明完整四中心消去原 $J_n$，在逆 $\tau$ 后识别整个余核，并保留全部 fat-jet 系数、Jacobian 单位、好图像包含及原 $s_0$。
G 已为本原几何写出了这些步骤；它们是本包留下的主要识别工作，不能在比较时省略。
反过来，四个核对步骤的数量并不自动产生四种创新；它们仍可能是一个标准留数实现的有技巧具体应用。

### 5.2 2024 主部丛定理的压力不能被简化为“底环不同”

该文的对象包含 $\mathcal F_r^d$、局部上同调双分次片及由双线性形式乘法给出的映射，不只是向量丛分裂表。
Th3.2 的递推及 Lemma3.4 的负二项式单位三角基，明确否定“正特征全部次数异常／负二项式整基此前没有统一办法”的叙事。[必要正文][K24]

当前没有给出把原 $J_n$ 对应到它的指定双分次乘法映射、同时把 $\tau$ 作用及 $s_0$ 连接对应过去的参数选择与同构。
不能只令 $r=n$ 或把局部坐标改名 $\tau$：必须核对真实源、商、截断和整数嵌入。
域上比较即使成立，也不能仅凭纤维分裂恢复混合特征厚度和自然整数格；但它可能直接简化 C3，故仍是强包含压力。
本席没有完成该映射，也没有证成不存在该映射；这限制“直接包含”的断言，不为原包自动授予 HIGH。

### 5.3 Fitting 全文缺口保留，但不重复给通用工具新意

2026 可见 Th1.3 另要求首 Fitting 理想为高度一准素；本题首次 $Q=\tau^B(p,\tau)^{p-1}$ 不满足该条件。
确切理由是 $p^{p-1}\tau^B\in Q$，$\tau^B\notin Q$，而 $p\notin\sqrt Q=(\tau)$，见 FS §4.1 的原题推论。
这只排除该条声明的直接代入，不能排除整篇其他定理，也不能排除 Ohm 全文。
因此 D 的一般行列式因子工具不给独立方法分；当前保留的是原 $M_n$ 所产生的含高度二信息的具体整数理想，不是缺陷概念本身。

### 5.4 对完整链的最强反对意见与回答

**反对意见：** 在已知原 jet 呈示之后，只用标准四边插值、一个留数正规形、Taylor 行内容及 Lucas/Fitting 记账，
便算出同一组理想；除了识别这个固定几何算例，是否还有足够独立的数学发现？

**有证据的回答：** 当前确实保留原整数连接而未除掉坏素，且给出闭式格和保留高度二信息的完整理想；
旧“只得到等规模矩阵／无控制连接／有限首现样本”的具体失败条件已不适用。
C1 的完整标记 Ext 信息也不能由 C2 的去扭商或 C3 的理想／长度反推，故并非所有结构都被一个行内容公式取代。

**回答的限度：** 这说明结果具有实质，尚不说明方法普适或发现高度意外。
C3 的现有证明主要消费真实相邻列及格连接，不是每一个标记 Ext 值都有新的独立用途；
不能把 C1 的所有恢复细节、通用工具证明的长度或未用的低阶锚点当作额外研究价值。
我认为本包超过孤立计算例子的层次，但最强反对意见只得到部分回答，这正是 CAUTION 而非高新意通过的原因。

## 6. 相对旧 6.5 与组合的准确差额

| 基线／旧压力 | 当前状态 | 新意处理 |
|---|---|---|
| 旧 I05：实际连接与可闭合消费者尚未展示 | D05 已给全部标记扩张和整数恢复，G/A 闭合原格及算术输出 | 是真正新增的同一链，不用旧 OPEN 否认当前证明 |
| 最近两诊断接受之后的 G 阶段 | C1 此时已接受，G 补其此前缺的格桥 | C1 在完整 I05 包中计一次；不在阶段推进中再记一次 |
| 原全次数 JET、零时间全次数固定部／维数、二阶 | 均为接受基线 | 全扣除；原呈示在逻辑上决定不变量，不等于旧文已完成闭式求解 |
| 三阶混合块与 $\tau^5(2,\tau)$；固定 M4 | 非自由去扭商、双对偶缺陷、长度跳跃已有低阶见证 | 所有低阶锚点扣除；不得重新宣称这些现象首次出现 |
| P18 的实际 Fitting 定理 | 复数标记 Hénon 相对微分的 $\operatorname{Fitt}_0$、完成／基变换／泛长度 | 通用操作扣除；没有当前整数无扭商识别或秩$n$理想乘积 |
| P29 的数字基与累计原函数 | 特征零动力向量空间余核、轨道支持及混合进位 | 工具扣除，不伪造它给出原四簇上同调或 Lucas 系数的证明箭头 |
| P30 单位时间上同调及迹／Hasse | 单位时间复形已反演 $\tau$；逐位选择有明确谱系数与支持界 | 给逆 $\tau$ 后的基线，不恢复原格；无到非零零时间环的“把单位送零”基变换 |

本席在列明的实际接受源中确认上述对象和前提，未发现旧组合提供新 C1/C2 的全部直接代入前提。
这不等于“已有矩阵不能推出结果”，也不等于全球不存在更短理论；比较的是已经给出的统一识别与输出，而非形式可计算性。
来源中一般 fat-point、主部丛与差分工具仍全扣；不能为使组合不碰撞而把公有工具变成本项目独有理论。

## 7. 分数理由、定位与不借用的未来价值

新意7.0的正面依据是原对象统一性、整数信息保留和从逐阶呈示到全称结构的实际跨越。
没有更高分的原因是抽象机制已经高度标准化，识别主要针对固定 $q=1$ 族，C3 在前提闭合后推导成本较低，且强来源全文包含尚未排除。
分数不是各表格标签的算术平均，不由证明通过次数、文件数量、是否还缺第五篇或锁定阈值反推。

独立价值7.0的依据是：它具体回答原整数无扭商何时不自由、缺陷是什么、坏素如何改变扭长，
并且保留比各域上长度更强的原扩张资料；这些答案不由 P18/P29/P30 的已用消费者供应。
限制是这些量仍集中于同一指定退化族，尚未展示一个超出该原计算的新一般分类或其他独立数学问题的必要应用。
没有这类应用不使现有定理失效，但不应借未实现的用途提高本次价值分。

建议定位为“非单位时间 qPI 反典范上同调的整数扩张、留数格及算术缺陷”，
主陈述以原 $M_n$ 的格／理想和实际次数连接为中心，将 Taylor、留数和数字工具明确归入标准机制。
不建议宣传“新的 Pascal 理论”“新的全素数现象”“一般 Hilbert–Pólya/动力谱结论”或“原整模已完整分类”。
这是一条结构计算型研究线的价值判断，不是对论文页数或录用的预测。

仍 OPEN 且本次不给潜在价值分：原整个 $M_n$ 的强直和 (P)、全部 Smith 指数、其他高于秩的 Fitting、一般 $q$、非加法结构或零时间可逆动力。
指定拉回／推出的 $P_m$ 仍不是原 $M_{n+1}$ 的直和因子；同理想、同长度也不推出同扩张。
无需为了改变本分数追加低阶样本；若以后发现真正的短包含，应按准确对象映射扣减；若出现新数学差额，应作为新输入另评。
本件不要求立即拓展范围，也不以未解决的目标把当前已闭合任务无限续期。

## 8. 本人实际读取、身份与终态验证

整文件 SHA 只绑定版本，不把 PARTIAL 变为 FULL。以下为本轮指定输入及直接比较源；未扫描旧 build 树或重核整份历史账本。

| ID | 本席实际读取覆盖 | SHA-256 |
|---|---|---|
| [PA][PA] | 本轮FULL，83行 | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` |
| [MATH][MATH] | 本轮FULL，117行 | `a0d1c880f45462721f78366234d0d5796d04f95c46428c05caacdb90ce75fdd3` |
| [PB][PB] | 本轮FULL，64行 | `5bfb95183689687b53fd1656896b64847605c362d260b1b68e999d7cee4b28ee` |
| [S13][S13] | 本轮FULL，181行 | `afc7c9b54044c25df82cfcaad62563e4d53f6c810be2eb785beb51f9eb7f294a` |
| [S2][S2] | 本轮FULL，228行；§2比较式逐式核对 | `01bc654082a21736c7af0e7494382d7f321d1c1b2b23492f6782d27c305b3d94` |
| [FS][FS] | 本轮FULL，102行；本人此前来源增补 | `60e972d287f5cf3d234826acd3caa4532f62e50a6578415c6942f4c0a19c2f36` |
| [PD][PD] | 本轮FULL，221行 | `766bbefd7df8918759101a543ff9f0635289cc77e24c5a18364ed065770eec7f` |
| [EXT][EXT] | 此前本人FULL318行；本轮1–110主张／前提刷新 | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` |
| [G][G] | 此前本人FULL429行；本轮1–115主张／前提刷新 | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` |
| [C][C] | 此前本人FULL176行；同哈希消费，不重签数学 | `25bb87a365eaf5a9d37c192a47f99d454007aa14e265668c34465cc3e2154e10` |
| [D][D] | 此前本人FULL297行；同哈希消费，保留其归一化修正史 | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` |
| [A][A] | 此前本人FULL180行；同哈希消费，不重签数学 | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` |
| [OLD][OLD] | 本轮PARTIAL1–110、160–210 | `4b1d3fdbb51f7b1e1250dfea393133ff3b409bc2bc5e130f7d8b55f703ef7fd4` |
| [PORT][PORT] | 本轮FULL121行；一次合并显示截断后另行全文补读 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [LIMIT][LIMIT] | 本轮FULL121行；保留该报告只读P30 V3的身份 | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |
| [UNIT][UNIT] | 本轮PARTIAL1–108，U1–U3及单位底环前提 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| [P18][P18] | 本轮PARTIAL525–618、1053–1149、1260–1295；主定理及Fitting／泛长度必要段 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| [P29-I][P29I] | 本轮PARTIAL19–39，对象及特征零 | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| [P29-3][P293] | 本轮PARTIAL1–244，数字基／轨道障碍／有界原函数的声明及证明 | `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1` |
| [P29-4][P294] | 本轮PARTIAL53–100，原相位数字重编码 | `e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884` |
| [P30-2][P302] | 本轮PARTIAL228–338，constants声明及完整证明 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [P30-5][P305] | 本轮PARTIAL84–161，rank-two及residue multiplier必要声明／证明 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |

本人新增外文定向实读范围：Maakestad PDF文本§3所需设置至Th3.1证明（192–505），§4 Th4.1所需系统和证明（711–1188）；
2024文 HTML §2相关设置／(2.7)–(2.9)与§3至Lemma3.4证明（239–467）。这些是文本相关段阅读，非视觉PDF全文或全部定理证明审计。
Maakestad 其余三条过渡式的证明由原文留作练习，本席不声称读到了不存在的完整证明；2024 Th3.2 case4完整证明未读。
FS 的官方索引预览阅读属于本席紧邻来源任务，本轮没有重新发起两篇全文查找；原≤6查询上限和访问失败记录保持原样。

终态只新增本报告；本人全文自读并核对直接本地链接、上表输入 SHA 与输出身份。
没有数学CPU/GPU实验、CAS、编译、试排页、项目／锁／稿件建立、旧记录改写、付费或对外上传；当前4/5批次及22–30页合同未改变。
技能的实际影响是方法／发现分拆、强先例逐前提比较和明确 CAUTION 边界，不是新增实验或自动准入。

[PA]: PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md
[MATH]: PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md
[PB]: PAPER31_QPI_NONUNIT_CLOSED_PHASE_B_DISPOSITION_V1_20260910.md
[S13]: PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C1_C3_V1_20260909.md
[S2]: PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C2_V1_20260909.md
[FS]: PAPER31_QPI_NONUNIT_FITTING_SOURCE_SUPPLEMENT_V1_20260909.md
[PD]: PAPER31_QPI_NONUNIT_CLOSED_PORTFOLIO_DELTA_V1_20260909.md
[EXT]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[C]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[D]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[A]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[OLD]: PAPER31_QPI_NOVELTY_CD_I05_I09_V1_20260909.md
[PORT]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[LIMIT]: PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md
[UNIT]: PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md
[P18]: ../../papers/18-marked-henon-scalar-boundary/paper/main.tex
[P29I]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex
[P293]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex
[P294]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/4_hilbert_series.tex
[P302]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[P305]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex
[CALLAN]: https://arxiv.org/html/math/0209356v1
[MAAK]: https://arxiv.org/pdf/math/0402279v4
[K24]: https://arxiv.org/html/2411.13450v1
[K25]: https://arxiv.org/html/2503.17522v1
[GR]: https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf
[CCD]: https://arxiv.org/pdf/alg-geom/9506024v1
[GAL]: https://arxiv.org/html/1803.02746v2
[ROW]: https://arxiv.org/html/1001.1783v3
[STACKS]: https://stacks.math.columbia.edu/tag/07Z6
[OHM]: https://www.sciencedirect.com/science/article/pii/S0021869308001452
[HAD]: https://www.sciencedirect.com/science/article/pii/S0022404926001313
