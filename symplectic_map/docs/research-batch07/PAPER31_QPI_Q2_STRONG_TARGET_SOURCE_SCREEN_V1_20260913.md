# Paper31 Q2：完整原曲面的强相混合目标与一手包含性筛查 V1

日期：2026-09-13 UTC。作者：/root。状态：AUTHOR_SCREEN_FROZEN / FRESH_CENTER_PREFLIGHT_PENDING。
这是 [八问筛查][S0] 后实际执行的 Q2，不是把普通正则紧能窗重新命名为新中心。
使用 research-lit、ARS 的有界来源核验、proof-writer、novelty-check；不运行泛化科研流水线，不建新系统族。
本件清楚区分既定旧数学、新作者短证、待证强目标及文献事实。尚无正式候选、锁、稿件、PDF或22–30页容量票。

## 1. 不弱化的 Q2-P 强目标

固定任意 \(T>0\)。在原完整实曲面 \(U\) 上，以 \(\mu=|dx/x\wedge dy/y|\) 为原测度，取任意 \(f,g\in C_c^\infty(U)\)。
允许观测跨孤立节点、分裂节点及全部四条 terminal；不预先删去临界能级，不要求投影后函数仍属于原光滑类。
采用 [M] 的逐连通圆条件期望 \(\Pi\)，研究原离散 \(F_T\) 的

$$C_n(f,g)=\langle (f-\Pi f)\circ F_T^n,\ g-\Pi g\rangle.$$

Q2-P 要求以原曲面有限阶光滑范数和紧支撑能窗控制完整相关，给最优衰减及准确振荡主项，
而不是仅对有限 Fourier 多项式、单一正则区间或固定离节点距离证明估计。
常数可依赖固定 \(T\) 和紧支撑；未添加 \(T\to0,\infty\) 的一致估计要求。
不得用单一 Hamiltonian 时间采样替换 \(F_T\)：能量依赖的离散位移必须由原 \(+P\) 导出，上区间必须处理双圆交换与奇偶。

待证的具体最优图景如下，不作为已证定理使用：

- \(T\ne1\)：完整相关应有 \(n^{-1/2}\) 量级的驻相主项及更快余项，并对主项非零的观测证明不能统一改进该阶。
- \(T=3/16\)：必须包含 \(h_-=-2\) 上持续光滑圆的二次驻点，以及同能量处另一分支小圆的消失；不能因整个纤维奇异而删掉主项。
- \(T=1\)：全部有限正则能级无驻点，孤立椭圆中心处一阶 twist 非零；待证泛型 \(n^{-2}\) 端点主项，观测消失阶可再加速。
- 分裂节点处的实际全 Fourier、能量导数与短时间位移配合，必须证明其没有比上述主项更慢的遗漏项。只知道薄能带尾小，尚不能推出这一点。

这里的 \(n^{-2}\)、完整余项和“泛型”非消失条件仍有明确证明义务。
最优性可以用存在光滑观测与归一化相关的非零 limsup 表述；不要求每对观测或每个整数 n 都有同号下界。
若强图景不成立，应先指出原命题哪一项失败，而非默默换成正则窗 \(n^{-1/2}\)。

## 2. 已接受输入与本轮纸测差量

旧 [全局合成][TW] 已获后续数学接受；文件头旧 pending 是冻结历史，不能当成新待审权限。
其全参数分类：\(T\notin\{3/16,1\}\) 恰有一个非退化驻点能级；
位置依次是 \(T<3/16\) 的中区间、\(3/16<T<1\) 的下区间、\(T>1\) 的上区间。
上区间相位是 \(F^2\) 的圆回返，不能与下／中区间的 \(F\) 相位混为单步提升。
[B] 的准确节点式为

$$\rho'(h_-)=-\frac{32T+3h_-}{(8h_--9)\delta'(h_-)L(h_-)},\qquad
\rho''(h_-)|_{T=3/16}=-\frac{3}{2(8h_--9)\delta'(h_-)L(h_-)}<0.$$

持续圆的相位与周期解析越过 \(h_-\)。新生小圆在存在侧有相同的群平移旋转相位，
但原光滑函数的 Fourier 幅度在收缩时消失，故不可用持续圆的非退化幅度代替。
这些是旧数学输入，不复活旧全实 twist 新意7.2双FAIL。

本轮 [M] 作者完整证明原 coarea 正号、proper 紧能窗、terminal 正则性、逐圆投影与 Koopman 对易，
并给整纤维均值的严格 \(+1/-1\) 非衰减反例。
另有节点纸测：中心化可把相关薄层尾从面积的 \(\delta\log(1/\delta)\) 改善到对 n 一致的 \(\delta\)；
均值投影可使原本离 saddle 的光滑 bump 在节点附近失去任意正阶 Hölder 正则性。
这些新短证另冻、另作 actual fresh 数学独查，本件不先给数学接受票。
即使全部短证成立，它们也没有完成 Q2-P 的全 Fourier 衰减或容量证明。

## 3. 实际检索范围与排除规则

日期截止2026-09-13。主控共18条 web query，分六批三条；不是18篇读过全文。

1. phase mixing integrable maps separatrix saddle critical points correlation decay
2. phase mixing trapping Hamiltonian systems Hadzic Rein Schrecker Straub 2025 2026
3. site:arxiv.org phase mixing action angle critical points separatrix discrete maps
4. Faou Horsin Rousset phase mixing pendulum separatrix linear damping
5. "integrable maps" "decay of correlations" action angle
6. "phase mixing" "hyperbolic" "elliptic" 2025 2026
7. "Quantitative phase mixing for Hamiltonians with trapping" journal 2026
8. "On Linear Damping Around Inhomogeneous Stationary States" journal
9. "phase mixing" "twistless"
10. "phase mixing" "critical points" "2026"
11. "phase mixing" "separatrix" "2025"
12. "mixing" "QRT" correlation elliptic
13. "BGK-type equilibria" "hyperbolic" 2026
14. Moreno Rioseco Van Den Bosch "mixing" Hamiltonian
15. "phase mixing" "integrable maps" correlations
16. "phase mixing" "discrete" "separatrix" 2026
17. "QRT" "phase mixing"
18. "correlation decay" "twist" integrable map stationary phase 2025 2026

1–3、5、12、15–18覆盖原离散／强相关目标，4、6、10、11、13覆盖节点与退化范数，9、14覆盖 twist 退化，
7、8补出版状态。普通 search snippet 不算 actual theorem read。
QRT-PCR、量子 twist fields、一般 hyperbolic linked-twist maps 等关键词噪声未作为同题先例。
最近六月由2026年查询、2026-04-03正式论文及2026-08-21预印本修订核实，不以抓取日期当发表日期。
没有可用 Zotero／Obsidian 工具或本地 arxiv_fetch 脚本，使用公开一手 arXiv／出版社。
未落盘外部 PDF；公开 PDF 流经 pdftotext 读取指定页。未扫旧构建树、未读取凭据、未上传任何本地稿。
ARS 仅作适用于本题的 scoped source verification，不扩展为全套深研或跨族项目。

## 4. 一手来源与实际阅读边界

### S1：摆系统已有跨分离曲线的强定理

Faou–Horsin–Rousset，*On Linear Damping Around Inhomogeneous Stationary States of the Vlasov-HMF Model*，
[arXiv:2105.02484](https://arxiv.org/abs/2105.02484)，[原PDF](https://arxiv.org/pdf/2105.02484)，
[出版社DOI](https://link.springer.com/article/10.1007/s10884-021-10044-y)。
实际 PDF 第1–6、28–32、38–40页 FULL；含 Theorem2.2、Propositions7.6/7.7/7.13/7.14 及其正文证明；
7.14末引Lemma7.15的证明未读，7.4／7.11的全部坐标估计证明未读，整篇42页不标 FULL。

Theorem2.2 对摆流的两光滑观测去逐轨道均值，允许穿分离曲线，给
\(\langle t\rangle^{-2-(p+q)/2}\)；p,q是椭圆中心处一阶及以上导数的连续消失阶，泛型为0。
有限正则性门槛为 \(m\ge5+p+(p+q)/2\)、\(M\ge\max\{7+q+(p+q)/2,m+2\}\)，另有速度衰减。
证明把椭圆中心与 separatrix 分开；后者在足够光滑下任意多项式衰减，频率导数无零。
因此“跨双曲节点、原光滑观测、完整 Fourier”不是未被处理过的机制。
但该定理不是原 qPI 的离散 \(+P\) 定理，也未处理本题驻点及双圆交换；不能直接逐字套用。

### S2：一般能量—角度框架及频率临界点

Moreno–Rioseco–Van Den Bosch，*Mixing in an anharmonic potential well*，
[arXiv:2201.07019v2](https://arxiv.org/abs/2201.07019)，修订2022-03-10，
[原PDF](https://arxiv.org/pdf/2201.07019)，[关联正式DOI](https://doi.org/10.1063/5.0091016)。
实际 PDF 第1–6页 FULL：全部主定理1.1–1.3、Corollary1.4、Proposition2.1陈述与其证明前段；
未读后6页，不把 Theorem1.2 的证明称 FULL。

Theorem1.1 在光滑角度坐标及非零频率 Jacobian 下给 \(t^{-1}\)；
Theorem1.2 在有限个简单频率驻点下给 \(t^{-1/3}\)，不是 \(t^{-1/2}\)；
Theorem1.3 在一维更光滑的非退化情形给任意有限幂次。
其紧支撑假设在角度—作用域中，故不能由原曲面紧支撑自动推出跨节点的一致坐标范数。
本题正则窗的 \(n^{-1/2}\) 可由标准二次驻相及 Fourier 求和改善，但这项改善本身不视为新中心。

### S3：trapping 的椭圆端点范数已有先例

Hadžić–Rein–Schrecker–Straub，*Quantitative phase mixing for Hamiltonians with trapping*，
[arXiv:2405.17153v2](https://arxiv.org/abs/2405.17153)，修订2024-06-04，
[原PDF](https://arxiv.org/pdf/2405.17153)。
实际 PDF 第1–8、11–17页 FULL：定理入口、假设、背景比较及Lemma2.1完整证明；其余不标已读。
官方摘要页标60页，本轮未确认新的正式发表状态，不据二手引用杜撰期刊。

对象是紧 trapping 轨道及非退化椭圆点；所用周期导数有严格符号。
Lemma2.1 控制光滑原数据的非零 Fourier 系数为
\(O(\sqrt{E-E_{\min}}\,|k|^{-r}\|g\|_{W^{r,\infty}})\)，此处 r=1,2。
宏观密度／场的观测核包含指示函数，不能把其慢率读成任意两原光滑函数相关的最优率。
该工作强化端点范数的标准技术压力，但未直接覆盖本题双曲节点与离散 twist 驻点。

### S4–S5：近期相关但不同对象，不作直接包含

Hadžić–Moreno，*On Absence of Embedded Eigenvalues and Stability of BGK Waves*，
[官方期刊正文](https://link.springer.com/article/10.1007/s00023-026-01692-1)，发表2026-04-03。
实际只读摘要与引言至Remark1.4（网页行11–223），未核其主定理证明。
其线性化 Vlasov–Poisson 算子处理椭圆／双曲 trapping，给无嵌入本征值及非定量 damping；
不能改写为本题原离散映射的定量率定理。

Frączek–Kanigowski–Ulcigrai，*Singularity of the spectrum of typical minimal smooth area-preserving flows in any genus*，
[官方摘要](https://arxiv.org/abs/2505.13193)，v2修订2026-08-21。
实际摘要与metadata FULL，正文未读。其紧曲面局部 Hamiltonian 流／IET 特殊流框架不是本题 proper 首积分的闭圆分叶。
记录近期景观，不借其奇异谱或不混合结论反驳本题逐圆投影后的能量系综相混合；跨族想法仅可另记 ROUND2_CLUE。

## 5. 机制扣除后仍待证明的接口

| 强主张 | 已有压力／输入 | 本题尚需完成 | 不可替代 |
|---|---|---|---|
| 原测度与逐圆中心化 | 条件期望、群平移均标准；[M]给原对象验算 | actual fresh数学检查 | 定义不等于率 |
| 跨双曲节点、无限Fourier | S1已有全局摆定理；本轮节点薄尾与局部离散时间纸测 | 原 \(F^2\) 相位下的混合能量／角度导数及求和 | \(O(\delta)\)不可直接换 \(O(n^{-1/2})\) |
| 最优率与振荡主项 | 旧全局 twist + 标准驻相；S2有频率驻点框架 | 原圆交换奇偶、每阶主项、余项与下界 | 只跑有限模态／regular窗不够 |
| \(T=3/16,1\) 特殊分层 | 旧[B]给节点相位jet；S1给椭圆消失阶方法 | 持续圆／收缩圆分离、完整主项和最优性 | 旧twist分岔不可再次当新发现 |

推断而非来源事实：当前看最有希望的证明路线仍是已知 separatrix 抵消技术、原离散时间接口、
标准驻相与椭圆端点展开的同对象组合。它可能有技术工作量，但工作量不自动形成高新意。
相反也不能仅因“Morse局部引理短”就判最强Q2-P被逐字发表。
需 fresh 非作者针对完整 Q2-P、假定其最优结论最终成立的条件性新意／价值／22–30页内生容量预核；
不是正式四门双票，不给不存在的 proof≥9，不因文献没有同名 qPI 标题就判空白。

## 6. 本轮边界

旧 Q8 强中心 STOP、b7.4 双FAIL、全实twist7.2双FAIL及其它FAIL/HOLD/STOP保持。
Q3 无限 Fourier／小分母问题仅后备，未启动新证明或实验。
Paper31 原22–30页不变，Paper30 的22–40例外不能迁移。批次仍4/5，goal active。

[S0]: PAPER31_QPI_POST_RAMIFICATION_IDEA_SCREEN_V1_20260912.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
