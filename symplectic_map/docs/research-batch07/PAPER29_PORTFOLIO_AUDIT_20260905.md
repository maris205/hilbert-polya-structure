# Paper29 选题前组合内非碰撞审计

日期：2026-09-05。范围：本地 Papers1–28。性质：有界只读科学范围审计；不是证明终审、外部查新结论、Route A/B 评价或新论文立项。

## 结论先行

在本次所读的项目问题书、最终提案、摘要和必要边界段内，没有找到已经记录的如下完整结果：共正射线 Hamiltonian 剪切的相空间动量不变量分类、相应全局 Poisson/辛约化，以及通过约化曲面动力学排除额外有理第一积分的完备性定理。这个方向与 Papers20–28 的次数研究在映射族上相邻，但研究对象并不相同。

必须同时保留一个重要碰撞：共正射线上的正权支撑选择天然趋于最大射线倍数，其环境空间次数矩阵和增长率很可能只是既有 stationary-selector 机制的专例。因此，“直接检查若干守恒动量＋重新计算一个 Perron 根”不足以支持新论文。主代理目前正在验证的更强候选——约化面上无周期曲线及每个迭代幂的完整有理不变量域——才可能构成实质增量；本审计没有证明或验收这些待验证主张。

“本地未覆盖”仅表示下列已读语料没有同一结论，不等于世界文献中未解决。Papers23、24、26 的构建/权限阻断和 Paper19 的内部保留状态，也不使它们的既有科学内容重新变成可计数的新贡献。

## 输入、方法与证据等级

- 工作入口采用 [AGENTS.md](../../AGENTS.md)、[WORKFLOW.md](../WORKFLOW.md) 和 [Batch07 当前接续](../../BATCH_07_CONTEXT.md)。后者第3–4、48–53行规定当前完成2/5，下一项是 Paper29，论文仍串行开展。
- 项目定位采用 [README](../../README.md)、[原始研究背景](../../propose-symplectic-map.md) 和 [候选登记册](../candidate_registry.md)。不扫描 build、dependency-capture，不读取整份历史 Batch07 账本，不执行数学实验、编译或 Route 评分。
- Papers1–19 由独立只读子审计提取对象、结论、边界及精确来源；Papers20–28 由本审计直接核对问题书/提案，另核对 Paper27 当前论文摘要与 Paper28 已接受 successor 源的摘要、主定理及结论。
- 使用 `research-lit` 的“研究对象—贡献—边界—关联”整理框架；本次委派明确限制为本地语料，因此未进行外部检索、下载或外部写入。
- 下表的“结果”是相应项目已经记录的结论，不表示本次逐行重新核验了完整证明。数值证据、形式定理、Route 结论、产物终态分开描述。

## Papers1–19：对象与边界账本

表中行号用于精确定位所链接的文本源；一个项目可以同时有科学内容和交付限制。

| Paper | 已研究对象及最强记录结果 | 明确边界与碰撞提示 | 可核对来源 |
|---:|---|---|---|
| 1 | 冻结 Hénon 同伦 \(H_{a,\rho}=(1-ax^2-\rho y,x)\)。辛端点暴露率约1.17%，无完整视界存活轨道，邻参特异性门失败；另有光滑保投影辛提升的临界点障碍。 | 冻结载体失败，不是所有辛系统的算术不可能定理；轨道延续等属于数值证据。 | [README](../../papers/1-symp-vs-diss/README.md)，第8、20、31行。 |
| 2 | 三状态 PCF Markov–baker 和固定有限记忆局部常数乘子钟。周期长度只有有限有理秩，不能包含全部 \(\log p\)。 | 不排除点依赖屋顶、可数状态或增长系统族；精确 baker 仍是结构对照。 | [README](../../papers/2-branch-baker/README.md)，第5行；[RQ](../../papers/2-branch-baker/notes/RESEARCH_QUESTION.md)，第66行。 |
| 3 | 冻结 PCF 二次映射及一般单首整多项式 \(F'=mH\) 的周期乘子整除性：有理周期乘子属于 \(m^n\mathbf Z\)，从而排除冻结映射的原始有理素数乘子。 | \(\lvert\lambda\rvert=p^n\) 是另一问题；基素数2的高周期边界随后由 P7 收紧。仅知模长而不知乘子有理的情形不在此定理内。 | [RQ](../../papers/3-prime-multiplier-obstruction/notes/RESEARCH_QUESTION.md)，第7、45、64行。 |
| 4 | 整系数面积保持 Hénon，推广至固定 \(S\)-整数单首面积保持因子的有限复合。乘子为 \(S\)-单位；精确有理模长的素支撑限于固定坏素数集，整情形只能为1。 | 良约化条件必要；不限制无理代数模长大小，也不涉及近似素数或一般 Lyapunov 指数。 | [README](../../papers/4-integral-henon-multipliers/README.md)，第5行；[RQ](../../papers/4-integral-henon-multipliers/notes/RESEARCH_QUESTION.md)，第87、120、140行。 |
| 5 | 代数精确辛映射的已归一闭轨道作用量。代数性与 Hermite–Lindemann 排除其等于任何复支的 \(\log p\)，包括规定的倍数、平均和重复。 | 不覆盖 \(\log\lvert\mathcal A\rvert\)、多值生成函数、不当 Liouville 变更或超越归一化；作用量不是多模动量约化。 | [RQ](../../papers/5-algebraic-action-clocks/notes/RESEARCH_QUESTION.md)，第7、48、209行。 |
| 6 | 加法读出 \(L=v+\log q+\alpha\)：有限有理秩项、固定有理坏素数支撑和实代数项给出命中素数数目 \(\le\dim_{\mathbf Q}V+\lvert S_{\mathbf Q}\rvert\)。 | 仅此加法合同的容量界，不是所有动力学的完整逃逸分类；此处 selector 是读出选择，不是 Newton 选择。 | [RQ](../../papers/6-arithmetic-clock-escape-trichotomy/notes/RESEARCH_QUESTION.md)，第26、81、148、192行。 |
| 7 | 同一 PCF 二次映射的2-adic周期结构：周期至少2的点为单位，有理乘子为 \(2^n\) 乘奇整数；局部周期是 Frobenius 周期的唯一 Hensel 提升，归一乘子为非分歧范数。 | 精确排除 \(n=2,3\) 的 \(\pm2^n\)；任意 \(n\ge4\) 仍明确开放。至周期7的记录为 development-seen，不能升级成全周期或盲测证明。 | [README](../../papers/7-base2-exponent-clock/README.md)，第9行；[RQ](../../papers/7-base2-exponent-clock/notes/RESEARCH_QUESTION.md)，第75行；[登记册](../candidate_registry.md)，第10行。 |
| 8 | 双曲 \(SL_2(\mathbf Z)\) 环面自同构上的素数阶扭点。每个 \(n>12\) 有素数阶精确周期载体；标准 cat 的精确周期集合为 \(\mathbf N\setminus\{1,6,12\}\)。 | 阶数钟覆盖所有整数且不连续、非局部、非素数特异；导数返回只依赖周期，不内生编码载体素数。 | [README](../../papers/8-cat-torsion-capacity/README.md)，第18、26行。 |
| 9 | 标准 cat 的非零 \(p\)-扭点壳及 Euler 产品。仅 \(p=2\) 有一个原始轨道；奇素数 \(m_p\ge p-1\)。非零纯标量分母权不能把次数压成1，分数壳质量修复只是全壳归一化。 | 不排除矩阵、分子抵消、Fredholm 或富化商；外加一轨道 selector 不是 Newton 单项式 selector。 | [摘要源](../../papers/9-cat-prime-shell-multiplicity/paper/manuscript.tex)，第53行；[RQ](../../papers/9-cat-prime-shell-multiplicity/notes/RESEARCH_QUESTION.md)，第140行。 |
| 10 | 有限模数上的 cat 循环向量及中心化子商。循环向量集为 \(R_q[A]^\times\) 的 torsor；完整商压成一类并消掉动力学，辛中心化子商保留范数类。 | 随模数变化的有限群商，不是 Hamiltonian moment-map reduction；外贴 \(\log q\) 不是内生钟。 | [摘要源](../../papers/10-cat-centralizer-quotient/paper/manuscript.tex)，第53行；[RQ](../../papers/10-cat-centralizer-quotient/notes/RESEARCH_QUESTION.md)，第296行。 |
| 11 | 有限交换群平移作用的 Burnside、带标签、增强对象、orbifold/stack 信息保留层级。强带标签对象恢复平移元模核，有效作用时恢复精确带标签元。 | 标量/orbifold/Morita 像仍可能只剩静态动力学；没有统一内生模数钟，不是相空间辛约化或一般不可能定理。 | [摘要源](../../papers/11-cat-equivariant-clock/paper/manuscript.tex)，第54行；[RQ](../../papers/11-cat-equivariant-clock/notes/RESEARCH_QUESTION.md)，第233、563行。 |
| 12 | \(f_{m,a}=(y+(x^m-a)^2,x)\) 的形式周期迹矩：\(S_m=C_m+D_ma^{2m-1}\)，奇 \(m\) 时 \(C_m=0\)，并有有限系数证书；完整四次 \(0^4\) 纤维的三周期二阶矩给最小共轭分离量。 | 一般 \(D_m\ne0\) 和任意次数的三周期恢复仍开放；与 P15 重叠的四次结论已吸收，不作为平行新贡献。 | [RQ](../../papers/12-henon-period3-residue/notes/RESEARCH_QUESTION.md)，第196、285、287行；[P15 吸收约定](../../papers/15-henon-quartic-trace-fibers/notes/RESEARCH_QUESTION.md)，第239行。 |
| 13 | 退化 Hénon 族的实际精确周期覆盖、相对正规化、有限循环轨道商；有限局部自由且几何整，边界给约化 dynatomic 代数，稠密 étale 开集的轨道单值化为 \(S_r\)；轨道和/返回迹生成泛轨道函数域。 | 不声称所有纤维光滑约化或循环作用处处自由；primitive 指周期/域生成，monodromy 指覆盖，不是 Newton 字的有序矩阵乘积。 | [摘要源](../../papers/13-henon-primitive-cycle-cover/paper/main.tex)，第78行；[RQ](../../papers/13-henon-primitive-cycle-cover/notes/RESEARCH_QUESTION.md)，第326行。 |
| 14 | 单项式 Hénon 在有限秩乘法群平方中的存活窗口：显式系数一致四步有限界，且每个次数都有 rank-one 无限三步族。 | 特征零且三个系数均非零；窗口尖锐但常数不宣称最优。完整支撑一定理/证明已被 P16 吸收。 | [摘要源](../../papers/14-henon-four-step-torus-escape/paper/main.tex)，第52行；[RQ](../../papers/14-henon-four-step-torus-escape/notes/RESEARCH_QUESTION.md)，第198行；[P16 吸收约定](../../papers/16-henon-support-size-torus-escape/notes/RESEARCH_QUESTION.md)，第184行。 |
| 15 | 单因子单首中心四次 Hénon 的纯形式迹纤维：固定迹将 Jacobian 候选限于至多 \(d-1\) 个；周期一二唯一非拟有限 locus 是 \(E=\{a=1,p=(x^2-L)^2\}\)；周期一至三给拟有限截断，最小值为3。 | 不声称全局唯一恢复、单射、映射精确次数或多因子复合；单个三周期矩只分离异常纤维。 | [摘要源](../../papers/15-henon-quartic-trace-fibers/paper/main.tex)，第59行；[RQ](../../papers/15-henon-quartic-trace-fibers/notes/RESEARCH_QUESTION.md)，第239、250行。 |
| 16 | 具有非零常数的稀疏广义 Hénon，按合并后的实际非恒定支撑计数。支撑至少2时有显式系数一致两步有限界，每个预定支撑都有 rank-one 无限一步族；纳入支撑一四步/三步对照。 | 不覆盖零常数、零耦合或已删去项；不提供高度/枚举或所有自由链分类；支撑大小不是仿射共轭不变量。 | [摘要源](../../papers/16-henon-support-size-torus-escape/paper/main.tex)，第56行；[RQ](../../papers/16-henon-support-size-torus-escape/notes/RESEARCH_QUESTION.md)，第184、291行。 |
| 17 | type-\(\nu\) shift-like 递推生存簇中的连通环面平移。非零常数且至少两个非恒定项时，第 \(m\le k\) 窗维数至多 \(k-m\)，逐窗可取等，\(T_k\) 对每个有限秩群有限；另分类二维零常数共振边界。 | 不给有效基数或所有取等平移分类；不重包 P16 定量界。torus translate 是生存簇内乘法子族，不是相空间 torus action/moment quotient。 | [摘要源](../../papers/17-shiftlike-torus-coset-decay/paper/main.tex)，第48行；[RQ](../../papers/17-shiftlike-torus-coset-decay/notes/RESEARCH_QUESTION.md)，第293、338行。 |
| 18 | 广义 Hénon 参数空间唯一包含多项式边界的标记分支。\(-b\) 与任意 \(d-1\) 个规定的简单不交带标签周期迹给占优、泛 étale 坐标，临界/Fitting 方案在简单标量边界精确基变换。 | 不保证每个固定非零 \(b\)，特别不保证整个辛切片；不主张全 incidence 不可约、全局恢复或临界横截。有限标记商不等同辛约化。 | [摘要源](../../papers/18-marked-henon-scalar-boundary/paper/main.tex)，第69行；[RQ](../../papers/18-marked-henon-scalar-boundary/notes/RESEARCH_QUESTION.md)，第75、129行。 |
| 19 | 内部证明包：P17 锚定最大维平移的底层群刚性、全部归一平移参数及系数族几何；支撑一的 gcd 核障碍、无标量提升和进一步窗口关闭，含 \(q=2\) 精确例外。 | `COMPLETE_BOUNDED_INTERNAL_SCOPE`，15项外部来源声明仍阻断，没有 PDF 或出版候选；所给较长窗口不宣称最短，不分类所有低维/包含极大平移。内部内容仍占据组合内贡献范围。 | [摘要源](../../papers/19-shiftlike-translate-gcd-obstruction/paper/main.tex)，第52行；[RQ](../../papers/19-shiftlike-translate-gcd-obstruction/notes/RESEARCH_QUESTION.md)，第483、492、533行；[内部闭合](../../papers/19-shiftlike-translate-gcd-obstruction/notes/BOUNDED_INTERNAL_SCOPE_CLOSURE.md)，第10行。 |

## Papers20–28：Hamiltonian / Newton 最近邻账本

| Paper | 已研究对象及最强记录结果 | 明确边界与碰撞提示 | 可核对来源 |
|---:|---|---|---|
| 20 | 两模耦合梯度剪切，\(V=q_1^2q_2^2+q_1^g\)、\(W=p_1^2p_2^2+p_2^g\)，\(g\ge5\)。严格 selector/carry、最高项存活及坐标可见性给精确 \(2\times2\) 次数矩阵，\(\lambda_1=(\sqrt g+1)^2\)。 | 特定支撑、相序及系数；不分类任意支撑、环面、第一积分、非共轭或熵。显示耦合不是全局不可分解证明。 | [RQ](../../papers/20-coupled-shear-degree-matrix/notes/RESEARCH_QUESTION.md)，第9–42、61–66、78–82行。 |
| 21 | 三模全乘积加两端 spike，\(g\ge8\)。精确三阶矩阵递推、第三坐标可见性及无限不可约三次 Perron 子族（\(g\equiv2,3,4\bmod5\)）。 | 固定三模构造，不是一般三模分类；没有第一积分、全局约化、可积性或非共轭结论。 | [RQ](../../papers/21-three-mode-hamiltonian-cubic-degree/notes/RESEARCH_QUESTION.md)，第3–16、38–41行；[登记册](../candidate_registry.md)，第24行。 |
| 22 | 任意 \(r\ge4\)、\(g\ge2r+1\) 的两端 spike 全乘积剪切。精确次数矩阵，\(\chi_C=(t-1)^{r-3}P_3(t)\)，共同单位扇区与三维补空间解释谱坍缩。 | 三次 annihilator 不意味着每个参数都有精确三次最小递推/Perron 次数；矩阵 quotient 不是多项式相空间的 Hamiltonian quotient。 | [RQ](../../papers/22-hamiltonian-cubic-spectral-collapse/notes/RESEARCH_QUESTION.md)，第10–64、118–135行；[最终提案](../../papers/22-hamiltonian-cubic-spectral-collapse/refine-logs/FINAL_PROPOSAL.md)，第104行附近。 |
| 23 | 四模四 spike，\(g\ge10\)：严格固定 cone、精确可见四阶矩阵和 quartic recurrence；\(g\equiv3\bmod5\) 给无限四次 Perron 子族。 | 非泛支撑/泛系数结果，不主张“满秩必四次”、一般实现或可积性；共同核引理明确非新。交付阻断不抹去科学范围。 | [RQ](../../papers/23-hamiltonian-quartic-spectral-escape/notes/RESEARCH_QUESTION.md)，第10–60、99–134行；[终态索引](../../README.md)，第42行。 |
| 24 | 两模 crossed-binomial \(V_m=Aq_1^mq_2^2+Bq_1q_2^{2m}\) 配 diagonal pure-power \(W\)。普通次数从固定 seed 严格交替跨墙 \(u_1/u_2=2\)，任意非零系数下精确两步 monodromy、奇偶律，\(\lambda_1=sm(2m+1)\)。 | 不覆盖墙上、\(m=1\)、任意周期实现或逆次数；抽象 period-\(k\) selector-to-monodromy 只是条件技术，不是独立贡献。交付阻断仍保留该科学对象。 | [RQ](../../papers/24-hamiltonian-period-two-selector-exchange/notes/RESEARCH_QUESTION.md)，第9–59、100–133行；[终态索引](../../README.md)，第43行。 |
| 25 | 选定梯度矩阵的 support-row rank 约束：若 \(r\) 是堆叠支撑行的秩，则 \(\chi_C=(t-1)^{n-r}Q_r\)。显式各维正 Hamiltonian 族使 Perron 代数次数及可见标量最小递推阶任意大并达到秩界。 | 单位特征空间/特征多项式因子属于次数线性代数，不是守恒函数；不研究紧化、熵、可积性、第一积分、逆/高阶动力次数或全局分类。 | [最终提案](../../papers/25-hamiltonian-support-rank-unbounded-perron-degree/refine-logs/FINAL_PROPOSAL.md)，第79–101、103–162、203–212行。 |
| 26 | 两模任意有限 collected 正内部 \(V\) 支撑（指数均至少2），\(W\) 为两个分离纯幂。任意非零系数的 exposed-face Hessian 证书、墙上最高项存活、全局 projective log contraction、完整内部/墙 selector 尾部、精确正逆次数桥和统一二次 Perron 上界。 | 明确排除 mixed \(W\)、更高维、低于2的指数及高阶次数/熵/可积性。墙尾部 selector 交替不是数值 projective 二周期；逆标量递推另证，不能从向量桥直接搬运。交付阻断仍占据结论范围。 | [RQ](../../papers/26-hamiltonian-newton-envelope-contraction/notes/RESEARCH_QUESTION.md)，第9–170、176–195行；[终态索引](../../README.md)，第45行。 |
| 27 | \(r\ge3\) 的双侧正内部 collected 支撑。完整严格箭头证书下的真实 weighted-degree action 每步沿全1方向平移；无限认证分支的 selector-pair 更换至多 \(d_V+d_W-2\)，有等号判据及全局原点 stationary tail；非空严格整数域迫使 full spans 和逐边 literal reflected reciprocity，另有单步半裕量半径。 | 加权次数的状态平移/可观察空间，不是原始 \((q,p)\) 的守恒动量。无全局动力次数、分类、全局 reversor、多边稳健性或二维推广；结论依赖完整证书。 | [已接受论文源码](../../papers/27-positive-newton-translation-reciprocity/paper/main.tex)，第27–54、56–138行；[RQ](../../papers/27-positive-newton-translation-reciprocity/notes/RESEARCH_QUESTION.md)，第98–114行。 |
| 28 | 每个根定 primitive pair word \(\ell\ge3\) 构造一个固定自主辛映射，维数 \(2(\ell+1)\)。等总次数正支撑＋同步置换给 V-max/W-min normal-fan iff；独立精确动量权 carry chamber 提升为真实 weighted degrees；有两个分开的最小周期、rank-one 有序周期矩阵及三级字解码。 | 一字一映射且维数随字长增长；不是多项式状态周期，不是 ordinary-degree/entropy/可积性结果。此处 momentum 是初始次数权，不是 moment map；商是权空间模对角线。完整最大值递推从 \(n=1\) 起，不能把旧稿的较小 gate 或索引断言当当前定理。 | [已接受 successor 源](../../papers/28-primitive-selector-cycle-monodromy/paper-successor-20260905/main.tex)，第54–77、117–204、1792–1849行。 |

## 最近邻之间哪些内容已经被占据

| 机制或表述 | 已有覆盖 | Paper29 必须避免的重包装 |
|---|---|---|
| Hamiltonian 梯度剪切、辛性、显式逆 | P20–28 的基础定义与证明 | 仅换支撑或参数后再次验证 block-Hessian 辛性。 |
| 支撑比较 → 严格 carry → 最高项存活 → 精确次数矩阵 | P20–25 的固定构造，P26–28 的更一般面/证书机制 | 把形式 max-plus 轨迹当新真实次数定理；只更换可见坐标或矩阵大小。 |
| 单位扇区、支撑秩、低阶谱因子 | P22、23、25 | 将次数矩阵共同核改称“积分”或将特征空间 quotient 改称“辛约化”。 |
| selector 周期与 monodromy | P24 的真实二相交替；P28 的任意 primitive rooted word 家族实现 | 外加周期调度、条件矩阵乘积、rank-one 特征多项式本身不新增自主实现定理。 |
| 全1平移与 stationary tail | P27；P28 在等总次数及置换下扩展 residual 机制 | 共射线支撑的环境次数率若直接落入既有严格 stationary 分支，不再另计主要贡献。 |
| 环面/商/单值化术语 | P10–11 有限模群商；P13、18 周期标记覆盖；P16–19 生存簇 torus translates | 相同术语并不表示相同数学对象；反过来，也不能省略对这些对象的明确区分。 |

吸收关系同样属于非碰撞基线：P12 的重叠四次结论并入 P15；P14 的支撑一定理和证明并入 P16。P17 不能作为 P16 二维定量结论的第二次包装，P19 相对 P17 只把它明确新增的刚性、全参数和系数族几何等部分算作增量。参见表中各项目的吸收/边界段。

## 共正射线候选的逐层比较

主代理给出的工作设想是：两个 Hamiltonian 的单项式支撑都落在同一条正 primitive ray 上，寻找并分类形如 \(J_c=\sum_i c_iq_ip_i\) 的精确不变量；在全1 primitive vector 的情形，用 \(Q=\prod_iq_i\)、\(P=\prod_ip_i\)、\(x_i=q_ip_i\) 及动量差约化到候选曲面

\[
D_h:\quad QP=h(x),\qquad h(x)=\prod_i(x+c_i).
\]

上式在本节只是候选说明，不是本审计新增证明；符号 \(c_i\) 在动量差参数化中应与线性组合系数另作清晰区分，正式文稿不得混用。

| 候选层次 | 组合内判断 | 仍须真正验证的内容 |
|---|---|---|
| 若干 \(J_c\) 的直接守恒 | 未见同一相空间命题；与 P22/P25 的矩阵共同核不同 | 是整个复合映射的不变量空间分类，还是仅两个剪切分别守恒的充分条件；特征、常数项、零项及支撑合同必须固定。直接检查本身很可能只是短引理。 |
| 环面作用与全局 quotient | 未见相同构造；P10–11、13、18 的商及 P16–19 的 torus translates 均不是该对象 | 不只在所有坐标非零的图上写有理公式；需明确 invariant ring、纤维、光滑/奇异 locus、下降映射及 Poisson/辛结构的适用层。泛纤维论证不能自动推广至所有特殊纤维。 |
| 约化面的真实动力学 | 没有在既有项目中发现同一结果；P26 mixed-W 排除与 P27 的次数结论不能替代它 | 从 \(D_h\) 的自动同构结构或直接赋值论证给出真正新信息。只复制环境空间 Perron 值不够。 |
| 无周期曲线 → 第一积分完备性 | 在本次语料中未见覆盖，是当前最值得验证的核心 | 主代理正在验证“相应约化面无周期仿射曲线”、以及每个 \(F^N\) 的有理不变量域恰为动量参数域。需要独立证明核查无穷远赋值、有限分支置换、特殊 \(h\)、泛动量纤维 torsor/因子性、分子分母半不变量和权分解下降；不能从几条显式动量直接宣称全部第一积分已知。 |

特别要分清“有 \(r-1\) 个第一积分”和“Liouville 可积”：在 \(2r\) 维辛空间中，前者本身不提供足够的相互对合积分，也不说明剩余二维动力学可积。若候选的最终结论恰是排除剩余有理第一积分，摘要应正面表述这一完备性/非存在结论，而非仅以“降维”包装。

## 三个可继续验证的方向

以下是有界候选，不是三个已立项项目，也不是三条外部新颖性结论。方向1中的各层应当作为一篇紧密连接的论证，不按短引理拆成多篇。

1. **优先：共射线动量约化与有理第一积分完备性。** 将精确线性动量空间、全局 quotient、约化曲面无周期曲线和每个迭代幂的完整有理不变量域组织成一个命题链。组合内的实质区别清楚；关键风险是全球几何/赋值证明是否成立，以及外部相关的曲面自动同构和不变量域结果是否已直接推出同一结论。环境次数公式只能作为背景或校验。
2. **保留：同族具体剪切的高阶动力次数。** 从固定的已理解正支撑构造出发，研究中间维子簇的 degree growth 或相应紧化作用，而不是把已有坐标 degree matrix 的外幂当答案。P25/P26 明确把 higher dynamical degrees、紧化和熵排除；这提供本地未覆盖范围，但没有提供易证性或外部新颖性。只有存在可独立控制的几何机制时才值得推进。
3. **保留：低指数/边界支撑下的精确存活与失败分类。** 固定一个窄的 Hamiltonian 子族，研究正内部假设下降到指数1或坐标边界时，哪些 leading-form/carry 失败可以完整分类、哪些可由替代坐标或真实面证书修复。P26/P27/P28 已有这些边界的反例，所以单添反例不构成增量；需要必要充分分类或新的系数一致定理，不能只重述原假设的重要性。

当前建议先完成方向1的证明可行性及外部查新。方向2、3仅作族内后备，不借本审计提前建立 Paper30/31 或扩大当前科学锁。

## 哪些是明确开放，哪些只是没有研究

- 文档明确保留的问题包括 P7 的任意 \(n\ge4\) 精确 \(\pm2^n\) 乘子问题，以及 P12 的一般 \(D_m\ne0\)/任意次数恢复问题。它们属于各自原对象；本批不会因“开放”二字自动跨族切换。
- P20–28 对可积性、第一积分、全局约化、紧化或高阶次数的排除，一般是范围声明，不是已经证明的世界性开放问题。
- 本审计的 common-ray/quotient/no-periodic-curve no-hit 是局部非碰撞证据。是否可证、是否有足够研究价值、是否已被公开文献覆盖，仍是各自独立的后续关卡。

## 索引一致性与操作边界

- 当前 [README 第4行](../../README.md) 和 [Batch07 接续第3–4行](../../BATCH_07_CONTEXT.md) 均为 P27、P28 已接受、2/5。登记册第3行仍写 P28 恢复中，属于未更新的导语；本审计只记录这一差异，没有修改登记册。
- P7/P8 项目 README 保留较早 source-lock 快照，不能用来覆盖总索引中更晚的科学状态。定位时另见未列入成果索引的 `papers/3-s_integral_clock`；本次没有读取或另计该目录，Paper3 按当前索引采用 `3-prime-multiplier-obstruction`。
- P28 科学范围按已接受 `paper-successor-20260905/main.tex` 复核，未以原稿取代 successor，也未扫描或重审任何旧 build 根。
- 本次唯一新增文件就是本审计。未改冻结源码、锁、控制器、账本或已接受产物，未创建正式 Paper29 项目，未调用外部服务或执行实验。后续是否锁题由主流程根据证明与查新结果决定，本文件不产生额外权限。
