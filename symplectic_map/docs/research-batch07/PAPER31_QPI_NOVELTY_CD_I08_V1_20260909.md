# Paper31：I08 独立新意 Phase C/D 与反方审查 V1

日期：2026-09-09 UTC；执行席：`/root/p31_qpi_novelty_cd_i08_v1`。
状态：`INDEPENDENT_NOVELTY_CD / CAUTION_DIAGNOSTIC_ONLY / NO_CANDIDATE_ADMISSION`。
总评：**4.0/10，CAUTION**；只建议一次有界纸面诊断，不建议现在启动独立22–30页统计论文。
本票不撤销已接受数学，不是正式四门票、跨模型验证、容量PASS或Paper31准入。
`route_applicability: NOT_APPLICABLE`；纯理论GPU必要预算与实际耗用均为0。

## 1. 独立性、实读输入与任务边界

本人是新意件的全新非作者席，未参与输入的想法生成、几何证明、数学独审或来源件撰写。
未读取其他I08或其他方向的C/D投票，未与其他评审席交换或校准意见，也不排名其他四个方向。
FULL读 `novelty-check/SKILL.md` 86行、`skills-codex/research-review/SKILL.md` 102行、`idea-creator/SKILL.md` 235行。
FULL读工作区 `AGENTS.md` 28行与 `docs/WORKFLOW.md` 39行；批次入口仅定向定位并读1–20行当前状态。
技能促使本件分开方法/发现、逐项核先例假设，并给最强反对意见和可停止的最小诊断；不开展完整idea流水线。
工具metadata未发现指定 `mcp__codex__codex` 接口；实际按派发采用独立Codex xhigh席，不冒称GPT-5.4或虚构threadId。
这是本次独立Phase C复核本身；没有再生成一个同源“外部模型”或将自问自答记作第二张票。

| 本人FULL读取的指定输入 | 行数 | 读取时SHA-256 |
|---|---:|---|
| [Phase A](PAPER31_QPI_SURVIVOR_CLAIMS_PHASE_A_V1_20260909.md) | 81 | `be4a8b04354b762dc43cb9b7947248005c7f2c8612970387a2ef588b477d0b33` |
| [I08深核来源](PAPER31_QPI_DEEP_SOURCES_I08_V1_20260909.md) | 162 | `0b509858575c5dcca41631d3137ea7433f8a22def571cb23b71de653f11069c4` |
| [几何数学处置](PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md) | 50 | `9db1f21b39b8e8df664fb27bd434fd02aed04b206ace4873de9834ff77d044e4` |
| [作者可行性件](PAPER31_QPI_KUMMER_FEASIBILITY_V1_20260909.md) | 138 | `d297f6219bbd0e17062cf6f20e245c96f37e0f54ba84cc834990e56ec3154b38` |
| [组合基线](PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md) | 121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [十项生成](PAPER31_QPI_IDEA_GENERATION_V1_20260909.md) | 164 | `385ee36d1788b4060d8371150e2d2db8a86484231999ce08b085328ea787e9dd` |

合并工具输出曾截断，组合基线与十项生成随后分别完整重读；FULL不依赖截断片段。
消费已接受处置，不重新审查未变证明；基线内上游正文/票的FULL身份不继承为本人FULL。
唯一允许新增为本报告；不改上述输入、旧稿/旧票/锁、README、批次入口或其他索引。

## 2. 固定对象与已经关闭的数学

对象为 $E_{T,h}:v^2+huv-Tv=u^3-Tu^2$、原指定点 $P=(0,T)$，固定 $T$、能级 $h$ 变化。
在 $p\ge5,T\ne0,-27/256,\ell\ge5,\ell\ne p$，全部有限层几何像
$W_n\rtimes\operatorname{SL}_2(\mathbb Z/\ell^n)$，$W_n=(\mathbb Z/\ell^n)^2$，已经接受。
算术Frobenius应在 $\det A=q$ 陪集；商类 $[b_n]\in W_n/(A_n-I)W_n$ 的有限层接口也已经接受。
若 $v_\ell\det(I-A)<n$，其阶恢复原点阶的 $\ell$ 部分；其他层保持截断，不能删掉此条件。
上述是实质数学进展，但仍未提供有效统计常数、全层覆盖控制、统一尾项或无截断统计定理。
不把排除的 $T,p,\ell$ 范围称为已分类例外；没有证明这些参数必失败，也不为扩大增量而主动打开它们。
P30的完整自治共轭、准确回返点和原周期权重，P11模型识别后的一般群论循环求和全部扣除。
特别地，$T=1,h=2$ 经 $x=u,y=v+u-1$，曲线及指定点恰为 [JR] Example5.4，不能重新发现该例。

## 3. 本人独立实读的一手先例

下面是本人新打开的原文，不仅复述来源报告；读取层级只列实际可见部分，不称任何一篇FULL全文。
公开网页读取与 `curl → pdftotext` 流式读取均未持久新增外部PDF；没有访问受限数据库或绕过403。

| 来源、年份 | 本人实际读取 | 决定包含关系的假设/结论 |
|---|---|---|
| [HV] Hall–Voloch，2006 | 引言、§2.1含Lemmas1–2及证明、§2.3、§4.2全部；§4.3起始 | 非等常数函数域、mod $\ell$ 像含SL₂、点非 $\ell$ 倍；中心余上同调给满仿射像。§2.3分 $\det=1/\ne1$，Theorem6对tame覆盖给常数Frobenius陪集的有效误差 |
| [CH] Cojocaru–Hall，2005 | 引言Theorem1.1及上下文；§3 Proposition3.1与相邻应用 | 基曲线亏格控制非等常数族的大素数几何SL₂；有理基阈值为15，故素数 $\ell\ge17$ 通用。Prop3.1明确固定det并要求tame |
| [JR] Jones–Rouse，2009v4/2010 | 摘要、引言起始；Theorem3.2及邻近证明；3.4完整证明、Lemmas3.5–3.7；3.8完整证明；Ex5.4与5.5声明 | global field不是仅数域；不可约模加挠点域不可除性给全Kummer塔，满平移时以 $\ell^{-v_\ell\det(A-I)}$ 积分检测点阶素于 $\ell$ |
| [AGM] Akbary–Ghioca–Murty，2010 | §3 Lemma3.3完整证明、3.4声明与其共轭不变性上下文 | 数域表述下，对好约化且 $\ell\ne p$，核大小和 $\ell^{n-c}b\in(A-I)W_n$ 精确检测 $\ell^n\mid[E(\mathbb F_p):\langle P\rangle]$；不是只检测一次可除性 |
| [G] Gekeler，2006 | 引言、§2设置、Theorem2.3表、Lemmas2.11–2.15及可见证明、2.3证明、Corollary2.18表 | 余核决定局部群结构；还已计算条件 $v_\ell(\det A-1)=r$ 下的余核型分布，证明使用定trace/det计数和提升，不只有全GL₂平均 |
| [LP] Lombardo–Perucca，v2/2021刊行 | v2 §4末Ex26及推导；§5 Theorem27、Lemmas28–29和证明；§6.1起始 | 数域满Kummer时，给定局部群的标记点均匀模型已明确；§5所用标量群不自动留在固定det陪集，不能照套本题 |

[HV] Theorem6的量词是tame有限Galois覆盖及degree-$d$闭点，误差含 $|C(q^d)|^{1/2}q^{d/2}/d$。
它的degree-one版本可在相应常数域上使用，但需重新标明覆盖/常数域，而非把不同采样问题直接等同。
[HV] rank $\ge6$ 属于无界素数的primitive-subgroup主定理，不是单个固定 $\ell$ 的幂次尾项门槛。
[JR] 的准确题名为《Galois theory of iterated endomorphisms》，不是输入旧件中另两种题名写法。
[AGM] 的指数判据结合群阶即可确定点阶；其后解析定理的GRH或高rank不转化为本局部群论接口的障碍。
[G] 条件表固定的是 $v_\ell(\det A-1)$，并非原字写成每个精确 $\det A=q$；下面保留这个需核的短比较。
[LP] v2可见文本确有Lemma29事件写 $\det(A-I)$、证明却计 $\det(\lambda A)\equiv1$ 的不一致。
最终刊版§5本席未读；上游所报403保留，不据此断言最终定理错误，也不从未核定版本进口任何尾界。

## 4. 最近六个月与检索覆盖限度

继承Phase B已披露的20条查询和2026-03-09至09-09的arXiv题名元数据检索，不冒称本人重做138篇全文审计。
本席另实际查询 `"fixed determinant" "point" elliptic order distribution Kummer 2026`、
`"cokernel" "fixed determinant" elliptic curve Gekeler`、`"elliptic" "point order" "2025" "2026" Kummer`。
新增查询噪声大，未增加可核强近邻；这种负检索不是“全球无人做过”的证据，判断主要依上述强原文。
本人新读 [Lee–Sheen](https://arxiv.org/abs/2606.25067v2) 官方摘要与版本日期：6月23日初稿、7月23日v2；研究群阶整除，不是指定点阶。
本人新读 [Fan 2608.24744v1](https://arxiv.org/abs/2608.24744v1) 摘要、HTML引言至Theorems1.3–1.4及邻近解释。
其对象是固定有限域椭圆等变同源映射的商线置换，几何像 $\mathcal N\rtimes\Lambda_{\mathcal N}$，并有分歧纤维权重；不是原非等常数SL₂标记点族。
本人新读 [Fan 2608.27255v1](https://arxiv.org/abs/2608.27255v1) 摘要、HTML引言TheoremsA–C及§1.3起始；非其64页正文审计。
其genus-one Galois closure含循环线性补群，故不直接包含本SL₂族；但“仿射几何/算术像+扩域支持+权重”这一包装不能算新机制。
这两篇首次日期分别8月25日、8月27日；无证据把六月份Lee–Sheen误署为Fan，亦不以近期稿不同对象提高本题新意分。

## 5. 三个核心的独立新意与反方判断

方法分评机制，发现分评拟得到的结论差额；C2/C3的MEDIUM仅是目标潜力，不表示已有定理或已获新发现。
下列分数为发现阶段判断，不对应任何正式四门阈值，也不按数学正确性PASS给新意加分。

| 核心 | 方法 | 发现 | 新意/10 | 当前建议 |
|---|---|---|---:|---|
| C1：原指定点全部有限层满仿射像 | LOW | LOW | 3.0 | ABANDON作为独立中心；保留为后续可复用输入 |
| C2：固定det的真正点阶律与有效误差 | LOW | MEDIUM（待证目标） | 4.5 | CAUTION，仅作标准包含诊断 |
| C3：统一幂次尾项、原周期消费者 | LOW | MEDIUM（待证目标） | 4.5 | CAUTION，先问统一控制是否产生非标准结论 |

### C1：正确、准确，但全球增量很薄

最近先例是 [HV] 的函数域Sah–Kummer，辅以 [JR] 全塔准则和 [CH] 有理基大素数定理。
真实delta是本族对每个允许 $T,p$ 的准确验证，并补齐 $\ell=5,7,11,13$ 及全层；不能抹掉这些量词贡献。
最强反对意见：所用同源/Hodge次数、局部Tate惯性、高度不可除性、中心元消余循环均是成熟机制；本族核验已有短证明。
对该反对意见的有效回应是“范围比通用大素数更明确”，不是“从GL₂换成SL₂首次解决函数域”。
失败风险：将科学正确性误当新机制，或者把允许范围之外尚未研究的参数称为完整例外分类。
新意风险HIGH、当前已接受证明的正确性不在本件重评；不足单独支撑锁定长文。

### C2：剩余是通用陪集律的准确实现，不是新的点阶机制

最近先例组合是 [G] 的余核/条件行列式表、[LP] 的均匀标记点、[AGM] 的精确指数判据，以及 [HV]/[CH] 的陪集计数。
真实delta是给定 $T,q$ 能级族的可计算 $v_\ell\operatorname{ord}(P_h)$ 分布，连同明确有限域误差；这尚未供给。
最强反对意见：全平移和SL₂一旦已满，有限层陪集主项只依 $q,\ell,n$，不依允许的 $T$；它不可能在该范围再出现qPI特有的首项偏差。
这里说的是由全像决定的主项，不是声称不同 $T$ 在有限 $q$ 下的真实计数完全相同；误差仍可不同。
回应边界：一个完整通用定理及本族验证可能是有用成果，但仅换坐标、添加一个均匀标记点或计算新常数不自动达到长文价值。
最可能失败是定理完成后发现仅为 [G] 表的短精化加已有Chebotarev；另一风险是直接把valuation条件表误作精确det表。
数学可行性风险MEDIUM、可发表独立增量风险HIGH；若短比较成立且无新消费者，发现评级应降LOW。

### C3：固定一个素数的尾项应独立判断，不等于完整循环长度分布

最近先例是 [HV] tame亏格/有效陪集框架、[G] 的局部提升计数，及已接受P30/P11的原权重。
真实delta最多是对层数增长可用的统一幂次尾控制、有效截断平衡及准确局部周期统计，而非再写 $d_h,N_h/d_h$。
最强反对意见：若固定det矩阵事件有普通指数衰减，覆盖规模又是显式指数增长，则截断平衡本身是标准方法。
但不能反向声称尾项不可能：无界素数primitive-root的rank困难与此固定 $\ell$ 问题不同，且 [LP] 版本缺口并不是不可能性证据。
实际风险是 $q\equiv1\pmod{\ell^j}$ 时近单位矩阵的退化、层依赖常数和tame性的未核义务；不因 $\ell\ne p$ 就断言整个有限群阶素于 $p$。
需要局部惯性/覆盖证明，而非仅引用“满像”授予全塔tame；本要求不重开满像结论。
单个 $\ell$ 的局部分布不能恢复完整 $d_h$ 或按 $N_h/d_h$ 加权的全部循环清单；不得以“真正周期”隐匿该边界。
正确完成局部统计仍有意义；尚无证据它需要或产生新的统计机制，数学/新意风险均HIGH。

## 6. 最小纸面诊断：只查精确det余核表与近单位元尾

建议一次1–2天、2–4页以内的诊断记录，CPU仅可选秒级转录核验，GPU0；本报告不启动它或大型枚举。
先固定一个 $\ell\ge5$，常数可以依 $\ell$，不得暗增为所有 $\ell$ 一致；保留允许的 $p,T$ 及增长的有限域 $q$。
令 $\mu_\delta$ 为 $\det A=\delta\in\mathbb Z_\ell^\times$ 陪集上的归一化SL₂平移测度，$C_A=\operatorname{coker}(A-I)$。
第一项短检查是：当 $\delta\ne1$、$r=v_\ell(\delta-1)<\infty$ 固定时，精确 $\mu_\delta(C_A\simeq H_{a,b})$ 是否就是 [G] Corollary2.18 的 $g_r(a,b)$。
实际 $\delta=q>1$ 满足该条件，但 $r$ 可任意大；若另研究 $\delta=1$ 的极限，必须单列而非代入有限 $r$ 表。
必须证明逐精确det的质量不变，不能用全GL₂中零测度事件的朴素条件化；优先复用 [G] 的定trace/det提升论证。
这里已有一个无需新机制的消费者：若 $C_A\simeq H_{a,b}=\mathbb Z/\ell^a\times\mathbb Z/\ell^b$，$a\le b$，平移满像给均匀 $z\in C_A$，则
$$\Pr(\ell^s z=0\mid C_A\simeq H_{a,b})=\frac{|H_{a,b}[\ell^s]|}{|H_{a,b}|}=\ell^{\min(s,a)+\min(s,b)-a-b},\qquad s\ge0.$$
这是两个循环因子各自数核的恒等式，不是本报告新统计定理；真正点阶的各档由相邻累积概率相减。
第二项只查 $\tau_n(\delta)=\mu_\delta\{v_\ell\det(I-A)\ge n\}$ 是否有对 $r$ 不恶化的可求和指数上界。
把 $A\not\equiv I\pmod\ell$ 的普通提升与 $A=I+\ell^aB$ 的近单位分支分开；后一分支满足
$$\delta-1=\ell^a\operatorname{tr}B+\ell^{2a}\det B.$$
这一步是识别剩余难度的位置，不在此宣称 $O(\ell^{-n})$、最优常数或某个最终 $q$ 误差指数已经成立。
若尾界可得，再只列出有限层误差 $E_n(q)$ 与 $\tau_n(q)$ 的实际依赖，检查存在 $n(q)\to\infty$ 使二者趋零。
已有 $|W_n\rtimes\mathrm{SL}_2(\mathbb Z/\ell^n)|=\ell^{5n}(1-\ell^{-2})$ 可提示规模，但不能代替覆盖亏格/tame与事件大小验证。
诊断输出必须是“旧表+短证明已包含”或“准确未闭合的新引理/障碍及消费者”，不交一个更长的待证清单。

## 7. 原动力消费者的价值扣除与停止准则

对光滑能级的任意有界指标 $0\le f_h\le1$，已知 $N_h=q+1+O(\sqrt q)$ 直接给
$$\left|\frac{\sum_{h\in U(\mathbb F_q)}N_hf_h}{\sum_{h\in U(\mathbb F_q)}N_h}-\frac{\sum_{h\in U(\mathbb F_q)}f_h}{|U(\mathbb F_q)|}\right|=O(q^{-1/2})$$
（$U(\mathbb F_q)$ 非空，按 $q\to\infty$ 理解）；有限个奇异能级的总状态质量相对 $(q+1)^2$ 是 $O(q^{-1})$。
因此把已得能级局部概率转为原状态局部概率大体是Hasse界的短推论，不应单列为新统计中心。
完整一步周期由旧式 $d_h\mapsto r_0d_h$ 得到，故局部指数只移位 $v_\ell(r_0)$；这里 $r_0=\operatorname{ord}(s)$，勿与上节det赋值 $r$ 混淆。
这不供应全部循环数的精确概率，也不把时间悬挂的新记号当新定理。

1. 若精确det表与 [G] 条件表仅差标准提升，尾界及误差平衡也无新机制：停止I08作为独立P31长文，保存短推论；不靠旧共轭链凑22页。
2. 若只完成固定 $n$ 而未能控制尾项：仅承认截断计数，不把未定质量删掉；固定层重复枚举不延长诊断。
3. 若发现真实的新参数依赖或异常，先区分它是有限域误差、被排除参数，还是与已接受全像矛盾；不能事后改原范围寻找漂亮结果。
4. 只有得到不能由上述先例短合成的统一定理/障碍，并明确改善原局部周期知识，才建议重新评估投入；“此前未写本坐标公式”不足。
5. 诊断到期仍只有标准方法预期和未证技术负担，则暂停该形式，不升级为完整统计工程，不借I10无界素数问题增加潜在影响。

## 8. 最终建议与交付状态

总新意 **4.0/10，CAUTION**：C1作为独立中心放弃；C2/C3仅保留一次低成本、具有明确淘汰结果的纸面诊断。
我实际会先做上节旧表比较；不会先写论文、枚举大量有限群、扩大例外参数或开展全素数primitive-point问题。
最强整体反对意见是：对象和几何输入已正确，统计主项却被通用满像机制固定，余下很可能是成熟理论的准确应用。
最有利但尚未获得的转机是：近单位分支的统一有效控制揭示具有独立消费者的新结构；不能提前把该可能性记为结果。
本件不授容量通过，也不按估计页数否认已接受数学；P31正文22–30页、全必要证明和未来完整独立双票全部保持。
未创建论文项目/锁、未编译或运行实验、未改变批次4/5，未外传、投稿、部署或联系外部作者。
终态保存后本人全文自读、复核六个指定输入哈希及本件直接本地链接；报告SHA另随交付回报，不自指写入正文。

[HV]: https://web.ma.utexas.edu/users/voloch/Preprints/lang-trotter.pdf
[CH]: https://www.alinacarmencojocaru.com/cojocaru-hall-IMRN-2005.pdf
[JR]: https://arxiv.org/pdf/0706.2384v4
[AGM]: https://personal.math.ubc.ca/~dghioca/papers/lt_revision.pdf
[G]: https://ems.press/content/serial-article-files/25986?nt=1
[LP]: https://arxiv.org/pdf/1612.02847v2
