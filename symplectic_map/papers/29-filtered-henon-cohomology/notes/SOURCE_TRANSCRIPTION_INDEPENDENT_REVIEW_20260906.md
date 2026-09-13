# Paper29 完整源稿：独立忠实转写审查

日期：2026-09-06。审查员：`/root/p29_source_transcription_review`。

**结论：SOURCE_TRANSCRIPTION_PASS_WITH_MINOR。** 实际完整源稿没有发现
CRITICAL 或 MAJOR 问题；有一项不阻断主证明的 MINOR 摘要范围遗漏，见第3节。
本结论只针对下述封存源的忠实转写、证明叙述、跨节一致性和既有锁契合。
它不是新的候选资格评分，不改变原R2容量FAIL及原合取结果，也不是
编译、22–30页门、渲染版面或PDF验收PASS。

## 1. 审查方式、独立性与输入身份

本审查员未参与源稿写作。先完整读取准备材料，未对当时尚未完成的
局部正文给结论；收到主控的 `COMPLETE_SOURCE_READY` 和源清单SHA后，
才开始读取实际源稿。此后从头到尾读完12个文件，共2124行。
读取前与读完后的12项SHA校验均全部一致。

源目录：`papers/29-filtered-henon-cohomology/paper/`。
文件身份清单位于项目的
`notes/SOURCE_DRAFT_MANIFEST_20260906.sha256`，条目路径相对上述源目录。
清单本身SHA256为
`37bfe5b105c19b42a97f1446318a838e467827424dc8015ca83d98a5eac2ed8d`。
本报告下文的源行号均指这份清单绑定的版本。

| 完整读取的源文件（相对paper/） | 行数 |
| --- | ---: |
| `main.tex` | 49 |
| `math_commands.tex` | 15 |
| `references.bib` | 60 |
| `sections/0_abstract.tex` | 19 |
| `sections/1_introduction.tex` | 160 |
| `sections/2_orbit_algebras.tex` | 236 |
| `sections/3_filtered_primitives.tex` | 315 |
| `sections/4_hilbert_series.tex` | 256 |
| `sections/5_periodic_detection.tex` | 166 |
| `sections/6_effective_periods.tex` | 353 |
| `sections/7_univariate_rigidity.tex` | 163 |
| `sections/8_symplectic_lift.tex` | 332 |

完整读取 `paper-write`、原 `research-review` 和
`skills-codex/research-review` 三份技能。采用完整稿交叉审查和按严重性、
位置、最小修正记录问题的结构。实际工具清单没有指定的Codex MCP
reviewer endpoint，因此采用当前实际运行的独立代理fallback；没有调用
或冒称调用gpt-5.4，没有外部review threadId。会议模板、9页默认值和
重开新意/容量评分不适用于用户已锁定的本次纯数学窄范围任务。

准备输入包括工作流、当前批次接续、`PAPER_PLAN.md`、
`SCOPE_AMENDMENT_20260906.md`、`SOURCE_SCOPE_LOCK_20260906.md`、
`PUBLICATION_LOCK_20260906.md`、`PLAN_ACCEPTANCE_20260906.md`，以及以下
完整科学与引用对照材料。其SHA均与锁/接收记录一致：

| 输入简记 | 文件 | SHA256 |
| --- | --- | --- |
| Plan | `PAPER_PLAN.md` | `8283fdd364d216f5208b3cadd2c6a6219fc02c432f345baaf1f57680c5ae9406` |
| Brief | `PAPER29_FILTERED_COHOMOLOGY_BRIEF_20260906.md` | `046cb40117c6c77f6fb61e5caf93f7ab52cbc8d219827dd731547663a83c1248` |
| M | `PAPER29_CYCLIC_COHOMOLOGY_FINITE_PERIOD_PROBE_20260906.md` | `0f3ce169e3c62bcde926f3d0f5661dad80dab534394dddaab5f3d24bf8e767b6` |
| S | `PAPER29_HENON_COHOMOLOGY_PROBE_20260906.md` | `3f9a1be49ff07bbadd4636f55745d1e31572f2a8988a1402828429edd9ea92d0` |
| IM | `PAPER29_COHOMOLOGY_MULTIPHASE_INDEPENDENT_CHECK_20260906.md` | `af20049ae1cdf6163a78b24a4a4a66f8f9f3ffe09e73274b6d5d21dc0ac85c39` |
| IS | `PAPER29_COHOMOLOGY_SCALAR_INDEPENDENT_CHECK_20260906.md` | `f87d3a19aee0bbc363c588e44e7a90e7a7ba853c314fc8ef18e13f0ce3096abd` |
| Citations | `PAPER29_COHOMOLOGY_CITATION_RECORDS_20260906.md` | `7a4f27383c07cd50b8e31ad92d3547e3a75d787fa76e9d74ffcfea30f8987b69` |

除Plan位于本项目外，上表科学文件均位于
`docs/research-batch07/`。原数学检查的PASS标签没有用来代替实际源中的
证明步骤；本轮检查的是这些步骤是否在新的英文叙述中正确保留。

## 2. 必列转写义务的实际核查

下表位置均相对 `paper/sections/`。PASS表示该项转写义务完整，
不表示本表之外的产物验收。

| 义务 | 实际位置 | 判定与核查要点 |
| --- | --- | --- |
| 无限基终止、合流、独立性与真实环双向同构 | `2_orbit_algebras.tex:59–130` | PASS。有限输入可引入新指标，但每项降次数；固定有限次数计数元组的字典序良基性明确。相邻规则仍保留另一原纯幂因子，共同乘积消歧；正规形湮灭关系理想，从而不只证明张成。两个环同态逐生成元互逆。 |
| 宏平移与同一个有限基证明 | `2_orbit_algebras.tex:138–236` | PASS。两个初值和相位周期性给出shift-k，而非shift-1。有限情形引用同一消歧证明；周期二生成理想给出双向环同构，长度δ^n是带重数的概形长度，且保留N=kn≥3。 |
| 普通最高项与混合进位制双射 | `3_filtered_primitives.tex:28–94` | PASS。两射线各自最高项为纯x或纯y幂；逐位整除给有限唯一数字。不同最高x^Ay^B项排除隐藏抵消，因此过滤确为原坐标普通次数。 |
| 全部障碍、有限累计原函数及常数核 | `3_filtered_primitives.tex:96–159` | PASS。非恒定基轨道无限；差分系数方向为u_(r−1)−u_r，负前缀和符号和两端截断正确。正常形常数与原坐标常数明确区分。 |
| 宏步离散凸性与保次数原函数 | `3_filtered_primitives.tex:166–238` | PASS。两尾之外的两处中部二阶差a+(δ−2)b、b+(δ−2)a均明写；下水平整数区间控制全部累计支撑。y^D达界只宣称scalar子族。 |
| 一次统一的仿射极点归约 | `3_filtered_primitives.tex:240–315` | PASS。所有扩域及正迭代的多项式半不变量先由无限基轨道排除；周期素曲线与有限极除子置换相连，再用UFD分母论证。有理固定域和所有原函数次数随之推出，不误消除射影无穷远极点。§7只调用此结论。 |
| strict filtered image、常数核、ρ方向 | `4_hilbert_series.tex:23–90` | PASS。W_D两度数限制排除取消；(σ−1)W_D等于V_D内全部余边界且核为K。负向低k位到正向位的两个显式编码式正确，ρ是置换但不假定对合；两宏次数表达式方向正确。 |
| 三域精确计数与scalar短特化 | `4_hilbert_series.tex:117–256` | PASS。α=Q、α>Q、Q>α互斥计数，比较最大值允许等号但不重复计数；关联分次与累计生成函数分开，常数核只在最终级数常数项补1。scalar只化简一般公式并推累计主项，没有复制独立scalar计数。相同宏次数比较限定为指定坐标滤过。 |
| long-gap提升与保宏相位无混叠 | `5_periodic_detection.tex:9–139` | PASS。L是每个词直径最大值而非支撑并集。唯一外间隙按循环距离计算；提升差jk+qN明确成为k倍数。满长n轨道、彼此不交的范数支撑和nc_0共同给iff；有理等价使用既有统一归约。 |
| scheme零与点值/幂零边界 | `5_periodic_detection.tex:142–166`；`8_symplectic_lift.tex:322–332` | PASS。精确理想成员与根理想成员分开；几何点在代数闭扩域上理解。约化有限特征零代数才可转为点值判据，period-one双数例未冒充长周期反例；结语保留未证边界。 |
| 精确端点费用、统一周期和quartic长度 | `6_effective_periods.tex:12–168` | PASS。端点词达到L_ph；balanced距离费用三个门槛给精确scalar式。n_eff保留全部n≥阈值；相位块定位及δ^4D^4仅对D≥1使用，D=0另说明。代数长度不冒充位复杂度。 |
| eventual-uniform尖锐量词与small-period边界 | `6_effective_periods.tex:170–339` | PASS。先定义固定scalar map的T_p(D)，明确每个n≥T和每个g∈V_D；g_r不同最高项给D_r=3d^r，包括d=3。binary等号情形稳定子只贡献非零倍数2；反例L≥2、n=2L−1≥3完整。k=2,N=6反例明确阻止macro-phase误推广。 |
| §7反射、导数最高项锥和完整刚性 | `7_univariate_rigidity.tex:16–163` | PASS。K[x,Q]的最高项锥所需证明完整；f及f_xy的交换反对称关系，C_D对x导数非零，两侧锥强迫对角再被反对称消去。无次数Ansatz，保留d、特征和Jacobian范围。没有复制旧scalar无曲线/反不变环基础。 |
| 加性扩张首项系数比和全固定域 | `8_symplectic_lift.tex:60–182` | PASS。互素分子分母具有同一个半不变量倍数；分别首一化后，首项系数比也属于K明写于103–104行。固定z后所有首一系数及该比均落K，覆盖整个L(r)固定域，非仅展示一个积分。 |
| 精确平移例外、全局辛坐标与所有Poisson对 | `8_symplectic_lift.tex:184–320` | PASS。最高两项比较强迫v_m常数和c=A′，A为多项式；势不能任加C(a)。全局多项式逆与辛形式取消明写。例外固定域内任意代数独立I,J借有限可分扩张的微分独立性得括号非零，而不只检验a、ρ一对。 |

## 3. 实际发现及最小修复

### MINOR-01：摘要代数长度上界遗漏D≥1限定

位置：`paper/sections/0_abstract.tex:11–13`，尤其第12行。
该句称testing algebra的长度至多δ^4D^4，但摘要没有明确限定D≥1。
正文 `6_effective_periods.tex:123–126` 正确限定D≥1，并在160–161行
明确排除quartic估计的D=0。正文又确实允许V_0及其检测，因此摘要的
无条件表述与全文范围存在一个可直接检查的边界不一致：D=0时右端为0，
而所选有限代数的长度δ^n为正。

最小修复：仅在摘要的上界句加上 `for $D\ge1$`。例如把
`the testing algebra has length at most $\delta^4D^4$` 改成
`for $D\ge1$ the testing algebra has length at most $\delta^4D^4$`。
不需要更改任何定理、证明、例子、结构或排版参数。

该项是摘要的范围限定遗漏，不是正文定理失败，故判MINOR而非MAJOR。
主控已明确会保留本次封存 `paper/`，在直接后继源版本中处理这个限定；
本报告没有改动源文件。后继仅需定向核对这处措辞与新源身份，不需要
重开本轮已核对且未变的数学链。

CRITICAL：0。MAJOR：0。MINOR：1。没有其他必要修复或新实验建议。

## 4. 跨节、引用和锁契合

- 主入口采用11pt、letterpaper、单栏article和1英寸边距；无行距或文字
  尺寸调整。源中唯一显式分页为 `main.tex:45` 的参考文献前clearpage。
  这只是源级协议检查，不是实际物理页数或实质页面判定。
- 恰有八个编号section、一个摘要和参考文献；结语位于§8。全部九个
  section文件均由main输入；源目录实际只有封存的12文件。没有附录、
  图像依赖、旧候选拼接、数值实验章或研究审计状态充正文。
- 基础证明按依赖只出现一次。§4的scalar结果是一般公式短特化；§7
  没有重写旧scalar无曲线论证；§5没有重证有限正规形。短例子都承担
  原计划中具体区别或反例义务，未发现基于页数目标的内容增补。
- 同名变量的局部变化有明确交代：§4改用α表示A(e)，§8的r不是§7
  反射，§8的ρ不是§4有限数字置换。F、σ、k、N=kn与scalar特化前后
  一致，§8另用带帽符号区分四维映射及其pullback。
- 五个BibTeX条目均在正文实际使用，元数据与已经验证的引用记录一致。
  Bousch仍为1992未发表稿；Schneider使用2016正式卷年；文中不混用
  作者稿与正式版定理编号。Bousch基础、Karr判据及Cerveau–Déserti邻近
  系数机制明确归属，finite approximate Livšic未被误写为同一精确代数
  命题或过时的“当前最佳率”。本轮没有另行重搜文献或重判优先权。
- 摘要、引言四项主张与正文结论逐项对应，唯一应修精确限定为MINOR-01。
  没有把滤过向量空间改称商环/共轭不变量，也没有把D^4长度改称
  最优复杂度；固定域结论不擅自扩大到全部参数纤维或isotrivial底族。
- 匿名署名和空PDF author字段均与出版锁一致。针对当前12文件的
  定向源检查未发现TODO/FIXME/XXX/VERIFY、正文页数目标语句或旧R2
  评分正文。静态检查不代替实际编译、引用解析和PDF阅读。

## 5. 本轮边界与下一步

已执行：完整准备材料读取、源身份前后校验、完整实际源读取、必要
证明步骤的转写核对、跨节与引用记录对照及当前源范围的静态检查。
唯一新增工作区文件为本报告。没有改源、运行TeX/BibTeX、生成PDF、
测量或预测页数、重跑实验、发起新文献检索或外部操作。

在上述一处小限定修复后，源转写审查没有阻断进入已授权首次构建的
内容问题。22–30实质正文页要求及独立实际PDF终审仍完全保留；首次
完整正确构建若不足22页，应依既有锁停止，不能把本审查当成补页
依据。原R2容量FAIL、旧合取结果与旧源均不因本报告而改变。
