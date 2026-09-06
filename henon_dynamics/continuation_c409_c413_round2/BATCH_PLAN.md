# C409–C413：五项独立合同与论文计划

2026-09-06。合同状态：`FIVE_SUBSTANTIAL_CONTRACTS_ADMITTED`。
写作大纲状态：`FROZEN_AFTER_INDEPENDENT_OUTLINE_REVIEW`。
这不是论文完成记录；大纲冻结时新论文/PDF 为零。写作进展见
批次外的当前状态入口。五篇上限不变，
不进入 C414，不将未选中的算术或谱候选作为第六篇。

## 准入依据与固定输入

前四项沿用 [封存实质裁决](../research_c409_c413/PROVISIONAL_ADJUDICATION.md)
及其四份非作者证明审查，不重新打开已通过的证明门槛。
第五项由本轮 [非作者完整数学与来源审查](REVIEW_TRACE_ROOT.md)
准入：全部整数 Fibonacci 迹映射的穷尽分类。两类已封存札记
仍不计篇，未选入的本轮有限格点、cocycle 与 cutoff-filter 研究
也不计篇。未取得的经典来源、公开版本差异及目标算术限制均
保留，不将五项合同解释成五项全球优先权证明。

所有新稿只写在本续接树 `papers/`；原 48 文件研究快照与前批
179/93 文件封存包不改字节、不重跑已通过且输入不变的检查。
最终文章是完整正文，不仅链接证明草稿或照搬工作流状态。

## 编号、对象与一篇一问题

| 编号与工作标题 | 对象、时钟及完整问题 | 拟写路径／作者 |
|---|---|---|
| C409 — Active fibres and natural boundaries in wild finite-adelic dynamics | 有限素数、非负周期径向指数和有限单位模复相位的级数；普通整数时间。精确判断抵消后何时有有理函数，何时有稠密实际 Fourier 原子及自然边界，并处理正熵非双曲 wild FAD 实现。 | `papers/C409_wild_fad/`；arithmetic |
| C410 — Wild cubic inverse-image towers in characteristic three | 任意特征三域、`a != 0`、`f=X^3+aX^2`；generic 逆像高度，不是周期。所有高度的算术/几何群、混合全局独立、局部秩一、分歧及亏格。 | `papers/C410_wild_cubic/`；positive_characteristic |
| C411 — Joint meromorphic boundaries of two-clock common returns | 所有整数底数 `a,b >= 2` 的圆乘法共同固定点；`n,m` 是两个独立时钟。双变量级数的全部开绝对收敛域、依赖分支极因子及完整联合亚纯边界。 | `papers/C411_two_clock/`；arithmetic |
| C412 — Rational periodic points of monic integral conservative Hénon maps | 所有 `a,b in Z` 的 `(y,y^2+by+a-x)`；普通迭代和有理点。两奇偶正规形合并，所有周期点、全部参数及尖锐八点界。 | `papers/C412_integer_henon/`；nonlinear_geometry |
| C413 — Integral periodic points of the Fibonacci trace map | 单一 `(y,z,yz-x)` 的全 `Z^3`、全部整数不变量层与普通迭代。完整周期集及每层返回律；其他整数点的双向 proper escape。 | `papers/C413_integral_trace/`；root |

共同格式：英文、匿名、独立可读的数学 `article`，11pt，约一英寸
页边距。没有已选投稿场所或强制页数，不采用 ICLR 模板、九页
硬限或为凑相关工作篇幅而扩写。以完整论证决定长度。按节保存
LaTeX，`main.tex` 只引用本篇实际节文件；不强制相同节数。

## C409：主张—证据及结构

一句话：有限 active-fibre 判据精确解决复相位抵消后的有理性／
自然边界二分，并给出非双曲野性动力学的实质应用。

证据：封存 `arithmetic/PROOF_PACKAGE.md`、`REALIZED_EXAMPLE.md`、
`POSTCLASSICAL_DELTA.md`、`arithmetic/SOURCE_AUDIT.md` 与
`REVIEW_ARITHMETIC_ROOT.md`。
各路径相对 `../research_c409_c413/`。

抽象判据限于有限素数集、有限个单位模相位、复周期权和非负
实数周期径向指数。FAD 推论另保留正熵及真实 FAD 数据假设；
不把一个实际系统的 wild 因子任意替换为未实现系数。

正文顺序：问题和主要二分；最近结果与 wild 差额；有限 adelic
群及 Fourier 展开；相位先聚合与全导子网格的完整证明；FAD
推论及 Salem×additive 真实实现；适用边界与结论。
主要数学步骤全部在正文或正文所含附录中，不只给 proof sketch。
摘要明示 AF 的两个分支，不把全部代数无野情形归为新结果。

引文计划：BCH 实际已读公开 v2、BHN 实际已读版本及可验证元数据；
引用范围由封存来源审计决定。最终书稿未取得的事实保留。
不引入未核实的“最新最终版仍未解决”断言。
表格仅在有助于区分 no-wild、dominant-root 与当前假设时使用。
不需要装饰性图或新数值实验。

## C410：主张—证据及结构

一句话：同一混合 Kummer/AS 归纳证明全局最大独立和局部秩一
可以并存，从而统一确定特征三三次 generic 野塔。

证据：封存 `positive_characteristic/WILD_CUBIC_PROOF.md`、
`SOURCE_SCREEN.md`、`EXACT_CHECK_REPORT.md` 及
`REVIEW_WILD_CUBIC_ROOT.md`。
正文必须保留任意基域 `k`、参数 `a`、树的兼容标号及常数域论证。

任意 `k` 上的 T1 与代数闭常数域上的 Kummer/AS 秩、惯性、
不同式及局部数据分开陈述。不声称一般 `k` 的分歧点剩余次数
为一；局部 AS 秩一不是全局秩一。逆像高度也不是有限域扩张度，
不增加特殊化满群断言。

正文顺序：完整定理和经典群 E 的归属；三次 Kummer/AS 正规形；
所有高度的 signature 上界；全局 square/AS 类秩证明；局部归纳
与惯性/不同式；群等号、正则性、亏格及限制。
`|E_n|=2^(3^(n-1))*3^((3^n-1)/2)` 和 `g_2=46` 可在摘要预览，
但数据表不构成贡献。标明源逆像深度不是前向周期计数。

引文计划：Benedetto 等、Bouw–Ejder–Karemaker/Ejder 的经典群，
以及实际必要的 Kummer/AS/分歧输入；元数据和适用域从已核源继承。
不借用有理 PSL 札记扩成第二篇，不宣传群 E 本身为新构造。
可用一个简短层数／群阶／亏格表，且由证明公式产生。

## C411：主张—证据及结构

一句话：两个独立时钟的共同回返有完整双变量延拓几何，不能由
同步、对角线或体积 zeta 的一变量结果替代。

证据：封存 `arithmetic/RECTANGULAR_RETURN_PROOF.md`、
`RECTANGULAR_SOURCE_AUDIT.md`、`RECTANGULAR_EXACT_CHECK_REPORT.md`、
`REVIEW_RECTANGULAR_ROOT.md` 及
`positive_characteristic/REVIEW_HARTOGS_PROPAGATION.md`。

独立底数初始开绝对收敛域为 `D²`。依赖底数 `a=c^r,b=c^s`、
`gcd(r,s)=1` 时初始域为 `D²` 内 `c^(rs)|x|^s|y|^r<1`；
两分支的联合亚纯边界均指 `∂(D²)`，不把依赖初始域的全部
边界误写成自然边界。

正文顺序：原生圆作用与精确定义；既有矩形/同步/体积问题比较；
两类底数的开绝对收敛域；primitive-ray 亚纯展开和真极因子；
径向奇性、Hartogs 传播及全联合边界证明；退化切片与限制。
强调零坐标轴的逐点收敛不是邻域收敛，整个联合边界也不等于
每个固定切片都有自然边界。Corvaja–Zannier 使用两个独立指数
的准确 S-unit 版本，不换成对角 BCZ 估计。

引文计划：Ward/Miles/Lind 相关原生定义，CZ 的确切公开版本，
已核 Hartogs 依据。一个问题／时钟／函数表即可说明差别。
如画收敛域示意，只表现公式确定的 log-radius 区域，不用仿真
声称联合延拓或目标 Euler 性。

## C412：主张—证据及结构

一句话：整个 monic 整系数 Jacobian `+1` 二次 Hénon 族的有理
周期点可精确列尽，普通周期仅 `1,2,3,4`，总点数至多八。

证据：封存 `nonlinear_geometry/PROOF_INTEGER_HENON.md`、
`ADDENDUM_INTEGER_HENON_ODD.md` 及 `REVIEW_INTEGER_HENON_ROOT.md`。
两个无限参数分支由六符号论证统一；13+17 个小参数的实际独立
全图重建收据继承，不能缩成只比较周期数。

固定 `b=2q+e`、`e in {0,1}`、`A=a-q²+(2-e)q`，
`T_q H_(a,b) T_q^(-1)=H_(A,e)`；正规坐标回译是减 `q`。
八点取等当且仅当 `e=1,A=-4`，即 `b=2q+1,a-q²+q=-4`。

正文顺序：全两参数主定理；整性和整数平移正规形；最大值与
六符号归约；局部符号方程的完整周期分类；偶/奇表及有限补集
证明证书；重叠、尖锐八点界与有理参数/相反 Jacobian 边界。
必须在可读正文中写完两分支，不把 odd addendum 当第二篇。

引文计划：已核来源中的 Hénon 高度及一般有理周期工作；1994
订阅全文未取得的限制不能消失。只比较实际读取范围，不把数学
自足性当成优先权证明。两张奇偶周期表是必要图表；不需外部
AI 画图或数值周期图。

## C413：主张—证据及结构

一句话：已知迹映射周期曲线恰好穷尽全部整数周期点；最大模法
排除所有其他周期而给出全部整数层的回返分类。

证据：本轮 `nonlinear_geometry/PROOF_PACKAGE.md`、
`SOURCE_LEDGER.md`、`VERIFICATION.md` 和 `REVIEW_TRACE_ROOT.md`。
固定 `K=x²+y²+z²-xyz`、`S_k=K^(-1)(k) intersect Z³`、`k in Z`；
与经典 half-trace 比较时 `I=K/4-1`。每层 zeta 使用全部普通
时间 `n>=1`，不要求整个 `S_k` 有限。双向 proper escape 仅指
无穷范数趋于无穷，不指每一坐标单调或新定量增长率。
正文顺序：全格分类定理与经典归属；精确周期词；最大模等号
及所有符号/零分支；单位立方体与双向 proper escape；每层
固定点／zeta／周期点数；有理反例、全群量词与目标边界。

两张紧凑表分别展示周期族和每层完整点数，不引入不必要图。
摘要给出周期集 `1,3,4,6,12`，注明只对整数；全格 `Fix(T^6)`
无限，因此 zeta 只定义在固定层。一般增长/逃逸理论及轨道族
存在均扣除，主张仅为穷尽性。

引文计划：Roberts–Baake 1994、Roberts 1996、Humphries 的实际
2016 v1；如为 Markoff 算术语境需要，再引 Ghosh–Sarnak 和
Vishkautsan 的已核版本。不存在“first ever”优先权声明。

## 审查、评价及真正完成条件

本大纲由当前团队非作者逐项审查主张覆盖、来源差额和边界后
冻结。论文写成后，每篇另交非作者实际全文、引文和证据审查；
不能用选题证明审查代替稿件审查。修复真正阻断点，仅重核受
影响推理，不按固定轮数机械重写。

根协调者负责五份正式 Route-A v0.2.0 评价及全部必要参考路由。
评价的科学标签与论文实质准入分开；三类算术对照未做则
`INCOMPLETE`，目标测试未定义则 `NOT_TESTABLE`，不补造实验。
所有目标 Euler 因子、根数、零点/除子对应和 Hilbert–Pólya
断言必须保持未建立；最终精确 tuple 由实际 evaluator 决定。

初稿可由作者自检编译。最后根协调者在两个新空目录构建每篇，
使用 `SOURCE_DATE_EPOCH=1788652800`、`FORCE_SOURCE_DATE=1`，
记录实际引擎和命令，比较 PDF 字节，核对字体/文本/警告，并
逐页视觉检查全部最终页。数学旧收据只在相关输入未变时复用。
页面数量和文件大小不得作为研究完成的替代。

每篇完整包包含正文源/PDF、证明来源入口、实际审稿/修订、
评价与构建收据。本轮最后作精确 payload ledger 和自排除
manifest，核磁盘成员集合及摘要；不改已封存快照。根独占全局
状态、两份注册表和 Git，暂存精确范围，审远端改动后常规同步。
完成后交付五个真实 PDF，停在 C413。无期刊投稿或外部上传授权。

## 技能适配与待完成大纲审查

使用 `paper-plan` 的一篇一主张、主张—证据及近邻来源组织；
使用 `paper-write` 的完整分节正文、真实引文和逆大纲检查；
使用 `paper-compile` 的实际构建/文本/字体检查。仓库前瞻合同
替代无关 ML 会议模板、固定页数与旧外部 reviewer 默认。
所有文件编辑使用 `apply_patch`，不使用技能中的 shell 写文件
回退。外部 MCP 模型不可用且未调用；团队审查明确为内部。

大纲独立审查已完成，见
[实际审查记录](positive_characteristic/REVIEW_BATCH_OUTLINE.md)。
该记录审读的初版摘要为
`eaabe15be1f84fde3f540f8887761c5705680c2558071ca853af6eaa75a18ce5`；
无结构性阻断。协调者逐项核对并在本版加入 R1–R5 的假设／
归一化／时钟限定和精确来源入口，没有变更已核定理。现在冻结
此五稿合同和大纲，开始正文；稿件全文的后续独立审查仍未完成。
除所列五篇外无新增稿件。
