# Paper31 Q2：完整原相关衰减的组合内增量检查 V1

日期标签：2026-09-13。作者：`/root/p31_q2_portfolio_delta`，未参与 M／N／K／E／G 的证明写作。
状态：LOCAL_PORTFOLIO_DELTA_IDENTIFIED / NO_FORMAL_ADMISSION。
仅执行 novelty-check 的 Phase A 及本地组合内子检查；不是外部查新、数学审查或正式四门票。
不授新意／价值分数，不授容量 PASS，不以本件改写旧 FAIL、STOP 或接受状态。

## 1. 有界结论

相对下文实际读取的 P27–30 接受源，以及已扣除的旧全实 twist 基线，[G] 有可辨认的单一分析增量：
在同一个完整原实 qPI 曲面、原离散映射和辛面积上，对允许跨 saddle、椭圆中心及 terminal 的原光滑紧支撑观测，
证明逐连通圆中心化相关的完整 Fourier 渐近、有限原范数控制、原单步奇偶系数及真正光滑观测的最优率。
已读 P27–29 的对象与结论不包含该命题；P30 则提供必须大幅扣除的原模型，而非提供这些时间衰减结论。

这不是“没有任何先例”或“足够独立成篇”的结论。
最强重新包装反对仍成立为待判问题：旧频率图加上既有奇异作用角／振荡积分机制，是否只剩一项原族上的完整应用？
本件只能说明该新命题不是已读组合结论的同义改写，不能凭此排除外部定理覆盖、标准迁移或切分成篇风险。
检查时 G／K／E 为完整作者证明、fresh actual review 尚待；M／N 的数学接受由[D]明确消费，不在此重审。

## 2. 实际输入与阅读层级

本人 FULL 读取 `/root/autodl-tmp/.codex/skills/novelty-check/SKILL.md` 至 EOF。
依主任务限定，省略技能中的外部检索、跨模型评分与全流程总分，未把本地阴性核对代称为这些阶段完成。

| 对象 | 本人实际读取范围 | 用途 |
|---|---|---|
| [G] 完整相关合成 | FULL，1–358 | 准确提取当前完整作者结论、量词、证明组成和非数学边界 |
| [D] Q2 处置 | FULL，1–118 | M／N 已接受范围、旧 twist 双 FAIL、强 Q2 有界接续及独立后续门 |
| [M] 测度／terminal／投影 | FULL，1–128 | 核原域、逐圆投影及非混合零模反例，不重新给数学票 |
| [K] 节点混合导数 | PARTIAL，1–108、218–292 | 全阶原范数／全模声明、符号接口及其证明边界；未读中段隐函数完整证明 |
| [E] 椭圆 jets | PARTIAL，1–110、250–377 | 原光滑 jets 的声明、两端点主项、奇偶及合法最优性观测；未读中段完整角度构造 |
| [N] 节点范数／尾 | PARTIAL，146–238 | 已接受的角向范数、投影损失、截断尾与尚缺时间率的旧边界 |
| [W] 旧 twist portfolio | FULL，实际为1–137 | 定位已锁组合基线及旧输入扣除；不继承其全文读取或外部判断身份 |
| [P27] 接受布局源 | PARTIAL，40–220 | 摘要后段、引言五项结论、定位及对象定义 |
| [P28] 接受 successor | PARTIAL，40–230 | 完整摘要、主定理八项、周期对象的明示限定及定位开头 |
| [P29I] 接受 successor 引言 | FULL，1–160 | 多项式 Hénon 余边界、过滤、周期概形测试的完整主张 |
| [P29P] 同源周期检测节 | FULL，1–166 | 循环指标、完整 scheme identity 与非标量平均边界 |
| [P30I] V4 引言 | FULL，1–300 | 原矩阵输入、三个算术临界理想／jet 定理及排除范围 |
| [P30U] V4 原曲面节 | PARTIAL，1–270 | 原八中心、terminal 辛形式、原 proper pencil 及边界复形开头；一次输出遗漏80–125已补读 |
| [P30J] V4 谱 Jacobian 节 | PARTIAL，1–270 | 原 Weierstrass 族、临界代数、谱曲线商、Jacobian 定理及证明前段 |

以下只绑定本次新论断与已接受处置的实际输入身份；对 K／E 的哈希不意味着本人 FULL 阅读其证明。

| 件 | 行数／bytes | SHA256 |
|---|---:|---|
| G | 358／18193 | `48fff63450138a788e4442c7b94c90e454eeebee2c1960afd895d15577c0cf6f` |
| K | 292／15637 | `f01797fdfaf8bcff40881cac199ff9e06fc1484bc578a2fad2f3c599b129cb79` |
| E | 377／17873 | `adaa676ad6fd049d65f2137eb52ee158a98604a652bcd7505c62f4ddf9aebfe6` |
| D | 118／9712 | `647f9ff04a023ce6dd889558cfd8834b7a1f7adf451e7fa356543e20bfe4d4ec` |

未读本轮外部 S／CD 全文，未重跑其查询；外部机制压力仅按[D]的既有记录保留，不冒充本人的独立外部查新。
P1–26 未重新搜索或全文读取；P11 的有限阿贝尔群周期消费者沿[W]已核边界扣除，本人未重读 P11。

## 3. Phase A：一个中心的四个必要技术部分

固定任意 $T>0$，原映射 $F(x,y)=(T/(x-y),x/y)$，原完整曲面 $U$，
$h=-x+y+x/y-T/x$、$\mu=|\Omega|$、$\Omega=dx\wedge dy/(xy)$。
对 $f,g\in C_c^\infty(U)$，$\Pi$ 是逐连通圆均值，目标为

$$C_n(f,g)=\langle ((I-\Pi)f)\circ F^n,(I-\Pi)g\rangle_{L^2(\mu)}.$$

这些符号固定同一个确定性系统；不替换成删临界能区的正则环带、有限模、随机扰动或全局常数时间流。

| 必要部分 | 当前实际作者命题 | 相对旧输入的定位 |
|---|---|---|
| Q2-a 原对象与观测接口 | 原测度、proper 紧能窗、terminal 范数、逐圆投影；只减整纤维均值会留下 $+1/-1$ 模 | M／N 已接受的短接口；原辛形式与曲面大部来自 P30，不是独立新方法 |
| Q2-b 跨 saddle 的全模分析 | 原 $C^r$ 观测混合能量／角度导数、原 $F^2$ 相位倒导数符号；完整局部能量积分对任意指定 $N$ 为 $O(n^{-N})$ | K 和 G 关闭 N 明确未证的能量微分、接缝、可积性、所有边界及全部 Fourier 求和；不把旧 $O(\delta)$ 截断尾改名为时间率 |
| Q2-c 原椭圆 jets 与端点项 | 非零模振幅 $\varepsilon A_k+\varepsilon^2R_k$，一阶主系数仅 $k=\pm1$；普通端点 $n^{-2}$，$T=3/16$ 二次端点 $n^{-1}$ | E 把旧中心范数尾推进为实际振荡主项与可求和余项；参数阈值和相位 jet 仍来自旧 twist |
| Q2-d 完整原映射的统一渐近 | 所有区域拼合，给原单步奇偶主系数、全局最优率与原光滑观测的非零 limsup | G 的主结论；前三项是它的定义／证明部分，不另计三篇或三项一般机制 |

准确主张是：写 $n=2m+r$、$r\in\{0,1\}$，固定参数及有限原紧能窗，作者给有限 $C^{20}$ 范数控制，

$$\begin{array}{ll}
T\notin\{3/16,1\}:& C_{2m+r}=m^{-1/2}\mathcal A_r(m)+O(m^{-3/2}),\\
T=3/16:& C_{2m+r}=m^{-1/2}\mathcal A_r(m)+m^{-1}\mathcal D_r(m)+O(m^{-3/2}),\\
T=1:& C_{2m+r}=m^{-2}\mathcal B_r(m)+O(m^{-3}).
\end{array}$$

$\mathcal A_r$ 是各实际持续正则驻点圆上的绝对收敛振荡级数；$\mathcal B_r,\mathcal D_r$ 来自原一阶 jets。
在 $T=3/16$，整条纤维虽然临界，持续圆仍是正则驻相圆；消失圆的 $m^{-1}$ 项另计，不能互相替代。
上区间换圆使奇数振幅是两圆 Fourier 系数的交叉配对，并非将偶数振幅机械复制。
最优性为存在原光滑观测使归一化相关绝对值 limsup 正；不是所有观测、所有时刻的正下界。
这是作者完整证明的待独查结果，不由本件升级为数学接受。

## 4. 与 P27–30 的实际断言对照

| 已读接受源的断言 | 不能混同的词义／对象 | 与 Q2 的包含及扣除关系 |
|---|---|---|
| P27 五部分 typed-arrow 加权次数、对角平移、selector-pair 有限变化及互反证书 | “平移”是次数向量沿全一方向；“尾”是稳定 selector 后的仿射公式 | 不是能量系综或相关尾；其特征零、维数 $r\ge3$ 正支撑多项式剪切结论不提供当前二维实积分族的相关估计 |
| P28 主定理的 primitive word 实现、quotient period、rank-one monodromy 和解码 | 正文明确两个最小周期都不使 polynomial state 周期；cyclic rotation class 是字的标记相位 | 无实圆时间角、辛测度条件期望或 $n\to\infty$ 的相关衰减；不能因有“周期／旋转”就算先有 Q2 |
| P29 引言的 $(F^*-1)$ 多项式余边界、degree filtration 和 bounded primitive | observable 是多项式，$F$ 是有限复合 Hénon，cohomology 是向量空间商 | 与原 $L^2(\mu)$ 逐圆中心化不同；形式上同有 Koopman pullback 不会将代数测试变成分析衰减 |
| P29 `thm:periodic-test` 的 $S_ng=0$ in $K[\operatorname{Fix}(F^n)]$ | “circle”是整数词压成循环指标；测试不是全周期点标量平均，更不是一个实状态圆上的均值 | 已读完整证明检测 scheme-valued 周期和的零性，没有给本题原光滑类的 Fourier 频率或相关渐近 |
| P30 `geom:surface`、`geom:poles` | 原 torus 加四 terminal、无退化辛形式、原 pencil 到 $\mathbb P^1$、无穷 scheme fiber | 这些是当前 $U,\Omega$ 与能窗 proper 紧性的现成几何基础，必须引用／扣除；取 $|\Omega|$ 为不变测度也不是新一般机制 |
| P30 `spec:weierstrass`、`spec:finite-critical`、`spec:jacobian` | “谱”指实际矩阵谱曲线与 Jacobian；“临界”在此先指代数族及相应概形 | 原实际椭圆曲线和临界结构是大量共享输入；不是 Koopman 算子的相关衰减谱定理 |
| P30 `main:first`、`main:odd`、`main:two` | $p,\pi_a,H$ 及第一 cyclotomic 层／高层 first jet，保留两状态方向 | 这些是算术临界理想的等式，不是实能量导数 $\sigma'(h)$ 或原离散时间渐近；其完整 terminal 范围不能重复宣传为 Q2 新建域 |

上述非包含有实际对象、函数类和结论量词依据，不是“题名不同所以不同”。
同时，“已读范围未陈述 Q2”不等于本人已逐定理排除这些论文所有未读章节，更不是 P1–30 全文无碰撞证明。

## 5. 必须清零计功的旧模型与旧 twist 输入

P30 原几何、原积分、实际谱曲线及四 terminal 已在组合中存在；本轮没有新造一张 qPI 曲面。
旧 twist 包已有真实回返组件、$F$ 保圆／换圆、$F^2$ 相位、全 $T$ 驻点分类、六端点及相位可微控制。
旧 forcing、Wronskian 一阶关系和节点参数亦不重计；两个数 $3/16$、$1$ 都不是 Q2 新发现的参数阈值。
它们现在获得相关渐近的分析后果，但新后果不能反向改写旧 twist 的新意 7.2 双 FAIL。[D]

同样必须扣除 Parseval／Fubini、相位共同 gauge 消去、能量分部积分、二次驻相、光滑 Morse 坐标及有限迭代的奇偶归约。
G 将这些步骤直接证明出来是数学可核查性，不自动构成新一般方法。
M 的逐圆投影、N 的投影非 Hölder 例子、K 的混合符号和 E 的偶半径构造都是同一全局相关定理的必要技术内容。
它们可承担真实证明负载，但不可仅以“独立文件数／行数多”替代创新计功或正文容量。

## 6. 最强重新包装／切分反对及可答到哪里

反对一：已知整条频率图后，$n^{-1/2}$ 是二次驻相，$n^{-2}$ 是一次消失振幅的普通端点；
$3/16$ 的 $n^{-1}$ 也只是二次端点的标准指数。所谓“新相图”是否只是旧 twist 表的读数？
本地回应仅为：旧表没有处理原光滑类在节点的混合导数、投影正则性损失、无限模余项、完整原曲面拼合或合法最优性。
G 确实声称并写出这些新义务；但这些义务可能仍属于成熟机制的对象化迁移，不能从“必须做”推出“足够新”。

反对二：P30 已给原族，旧 twist 已给全部相位，现稿会不会以反复铺陈同一原模型和奇异几何填出第五篇？
边界回应是严格引用和扣除：只补相关估计真正消费的域、范数与相位接口；不重抄旧曲面／twist 证明计作新增正文。
如果引用既有跨 separatrix 技术后真实增量不足独立长文，就应据实际容量处理；本件不预判，也不新增第五个硬门。

反对三：测度、saddle、中心、驻点、奇偶和最优性被分列后，是否只是把一个消费者拆成多个“贡献”？
应保持 §3 的一个中心：完整原系统上可达的最优相关渐近及机制竞争。
逐圆投影是正确定义，saddle 快衰减解释何者不主导，中心与持续圆决定主项，奇偶还原原映射，最优性确认率不可统一改进。
任何一项都不能独自被包装成额外 long-paper 中心，旧周期计数消费者也不添作新结论。

反对四：已有跨节点相混合先例是否已经直接包含强目标？
[D]已明确保留 FHR 等的标准迁移压力；本次没有重读其原文，因此不作独立 containment 结论。
区分旧频率表与新分析命题，只回答组合内部的增量；全球新意和独立价值仍必须在实际完整证明输入上另行判断。

## 7. 状态与执行边界

本件不改变 M／N 的既有数学接受，不先给 G／K／E 数学票，不把旧条件预核转成正式票。
旧 twist 7.2 双 FAIL 与其它 FAIL／STOP／HOLD 原样保留；P31 仍未正式准入，批次仍4/5。
两位 fresh 非作者各自完成四门、22–30页真实内生容量、最终稿件／PDF验收及其后跨论文终审都是独立后续义务。
P30 的22–40页例外不迁移，本件也没有估页、试排或以技术行数推算容量。

初次路径定位误列了旧 build 文件名，已立即向主控说明并停止该路线；未读其内容、未消费为证据，后续仅使用上表明确源路径。
无网络、CAS、数值、枚举、扫描实验、构建、PDF读取、外部写入或再委派；未改动旧源码、报告、锁及入口。
唯一新文件为本件。冻结前 FULL 读回，最终行数、字节和 SHA256 在交付消息给出；冻结后停止编辑。
结论强度仅为有界 LOCAL_PORTFOLIO_DELTA_IDENTIFIED，不是全球新意保证或正式准入建议。

[G]: PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md
[D]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[K]: PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[W]: PAPER31_QPI_REAL_GLOBAL_TWIST_PORTFOLIO_DELTA_V1_20260912.md
[P27]: ../../papers/27-positive-newton-translation-reciprocity/paper-layout-20260905/main.tex
[P28]: ../../papers/28-primitive-selector-cycle-monodromy/paper-successor-20260905/main.tex
[P29I]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex
[P29P]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/5_periodic_detection.tex
[P30I]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex
[P30U]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[P30J]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
