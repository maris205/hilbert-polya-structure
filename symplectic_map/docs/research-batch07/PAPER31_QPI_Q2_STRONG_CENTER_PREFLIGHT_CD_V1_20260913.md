# Paper31 Q2-P：最强全曲面中心的独立条件性预核 C/D V1

日期：2026-09-13 UTC。独立审查者：`/root/p31_q2_strong_center_preflight`；非 Q2 作者。
状态：`CONDITIONAL_CENTER_PREFLIGHT / NOT_FORMAL_ADMISSION`。
结论：`STOP_AS_INDEPENDENT_CENTER`；这是本候选的研究定位建议，不是命题已被反驳或逐字包含的判决。
假定 [S] 的完整强定理最终成立：条件新意 **7.6/10**，条件价值 **8.2/10**，内生容量 **MID**。
不授 proof 分、正式双票、Route 票、稿件/PDF票；原22–30页与批次4/5保持。

## 1. 权限、技能与输入身份

FULL 读取 novelty-check 与 skills-codex/research-review 两份 SKILL.md，以及工作区 WORKFLOW。
本代理就是主控委派的独立 secondary reviewer；工具发现未找到可调用的 Codex review MCP。
因此不虚构指定 gpt-5.4 的外部执行、跨模型一致性或第二张独立票。
按用户有界要求执行技能的 claims→一手查新→反驳测试→结论结构，不开展无关 ML 会场检索。
唯一写入本文件；未改 S/M/TW/B/N、锁、作者输入、项目登记或任何已接受产物。

| 输入 | 实际阅读 | SHA-256 |
|---|---|---|
| [S] 最强目标与来源筛查 | FULL，167行 | `dcee3c53f319f2ecc5b3b65fd021661bfd3d8ee0a7818ff4f5a44f176d5b0465` |
| [M] 原测度/terminal/投影 | FULL，128行 | `cdf173e47f86f4558ad125c5894f825441449bf4ea6c4c8801d31507e8c53700` |
| [TW] 旧全实 twist 合成 | FULL，133行 | `63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24` |
| [B] 旧 acnode 锚定 | FULL，144行 | `9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d` |
| [N] 本轮节点短证，后补输入 | FULL，238行 | `f50d3291694a6156cac21edfd47af7288ab4fef2b8615c82afe1778471b3d686` |

消费 TW/B 已接受数学身份，不因冻结文件旧 pending 重开它们；旧全实 twist 新意7.2双FAIL不撤销。
N/M 在本审查中仍是作者输入，数学接受由主控另委派的 actual fresh 审查负责。
N 后补阅读没有把本预核换成短引理价值评价；即使 N 全部正确，也不等于 Q2-P 已证。

## 2. 被审对象：不弱化的四项强主张

固定任意 \(T>0\)，原完整 \(U\)、原映射 \(F_T\)、原测度 \(\mu=|dx/x\wedge dy/y|\) 不变。
对任意原 \(f,g\in C_c^\infty(U)\)，研究 \(C_n=\langle (f-\Pi f)\circ F_T^n,g-\Pi g\rangle\)。
\(\Pi\) 必须是逐连通圆均值；允许观测跨两个节点、全部terminal、临界能量的持续圆。

1. 完整原空间的有限阶范数控制与无限 Fourier 求和，不删节点、不只证regular紧窗。
2. 使用原 \(+P\) 的能量依赖位移，并给原 F 换圆时的奇偶主项，不改成固定时间摆流。
3. 每个固定 \(T\ne1\) 的最优 \(n^{-1/2}\) 主项、明确更快余项与非零 limsup 下界。
4. \(T=3/16\) 的持续圆驻点与消失小圆并存；\(T=1\) 的泛型 \(n^{-2}\) 端点主项及消失阶细化。

本预核一律假定这些最强结论终能证明，再评估学术增量；不以当前未证直接压低其潜在新意。
上界要求覆盖全部观测；最优性用合适光滑观测构造即可，不要求每对观测或每个 n 都有正下界。

## 3. 独立检索：实际 query 与阅读边界

以下18条是本代理实际执行的 query，不是把 S 的检索算作自己的检索，也不是18篇全文。

1. `"phase mixing" "integrable maps" 2026`
2. `"phase mixing" "separatrix" 2025 2026`
3. `"correlation decay" "QRT"`
4. `"phase mixing" Hamiltonian hyperbolic elliptic 2026 site:arxiv.org`
5. `"phase mixing" separatrix Hamiltonian 2025 site:arxiv.org`
6. `"phase mixing" "discrete" "integrable"`
7. `"Mixing in an anharmonic potential well" stationary points`
8. `"phase mixing" "frequency" "critical points" 2024 2025 2026`
9. `"phase mixing" "twistless" "map"`
10. `"On Absence of Embedded Eigenvalues and Stability of BGK Waves"`
11. `"Weak Convergence to Equilibrium for Statistical Ensembles in Discrete Integrable Hamiltonian Systems with Markov Perturbations"`
12. `"phase mixing" "elliptic" "optimal" 2026`
13. `"Weak Convergence to Equilibrium" "Markov Perturbations"`
14. `"phase mixing" "elliptic" "2025" "2026" arxiv`
15. `"correlation" "stationary phase" "integrable maps"`
16. `"phase mixing" "energy dependent" "map"`
17. `"The LLN and CLT for the statistical ensembles of discrete integrable Hamiltonian systems"`
18. `Liu Zhang Li 109460 discrete integrable Hamiltonian 2025`

1–6、11、13、15–18覆盖原离散目标；2、4、5、10覆盖双曲节点；7–9覆盖驻点；12、14覆盖椭圆端点。
最近六月窗口为2026-03-13至2026-09-13；实际确认下述2026-04-03、05-18及07-10一手日期。
部分 query 噪声很大；未把 QRT=quantum regression、MHD phase mixing 或抓取日期当同题先例。
检索并非穷尽所有数据库；无 Scholar/Semantic 专用调用记录，不据有限无命中宣称世界首创。

| 一手来源 | 本代理 actual reading，均非整篇 FULL |
|---|---|
| [FHR](https://arxiv.org/pdf/2105.02484)，v1，2021-05-06 | PDF1–6、25–32、34–40全部页；含Th2.2、Props7.4/7.6/7.7/7.11/7.13/7.14及这些命题正文证明；Lemma7.15证明未读；其余21页未整读 |
| [MRVB](https://arxiv.org/pdf/2201.07019)，v2，2022-03-10 | PDF1–4全部页，含Th1.1–1.3完整陈述；主定理证明未读 |
| [HRSS](https://arxiv.org/pdf/2405.17153)，v2，2024-06-04 | PDF1–4、6–8全部页；含假设、Remark1.2、Th1.3；Lemma2.1与后部证明本代理未读 |
| [Hadžić–Moreno](https://link.springer.com/article/10.1007/s00023-026-01692-1) | 官方网页11–158，摘要、日期、引言前段；未读其证明 |
| [Liu Markov](https://link.springer.com/article/10.1007/s44198-026-00424-7) | 官方网页11–128，另805–909的结论/引用/日期；未完整读其定理证明 |
| [Liu–Zhang–Li](https://arxiv.org/pdf/2509.20690) | arXiv v1 PDF1–4全部页，含§2、Th3.1及完整证明；另官方HTML入口；后文未读 |

PDF只经公开下载流与 pdftotext 读指定页，无外部PDF落盘、上传本地稿或付费访问。
[Liu–Zhang–Li出版社](https://www.sciencedirect.com/science/article/pii/S100757042500869X)搜索结果给摘要/章节摘录；直接open为403。
因此不声称读过正式版正文，不将其正式版与arXiv的编号/假设自动混用。

## 4. 最强先例实际压到哪里

FHR Th2.2已有摆流跨separatrix、原光滑观测、逐轨道均值与完整Fourier的 \(t^{-2-(p+q)/2}\) 上界。
Props7.7/7.14以能量振荡积分处理：双曲端的逆频率导数抵消坐标奇性；椭圆端由观测消失阶决定速率。
它未给原qPI映射、twist驻点、换圆奇偶或本题完整振荡主项/最优下界，故不是Q2-P的直接包含定理。[FHR](https://arxiv.org/pdf/2105.02484)
MRVB Th1.2已有有限简单频率驻点的框架，但其C¹结论是 \(t^{-1/3}\)，不是 \(t^{-1/2}\)。
Th1.1/1.3的光滑角—作用域假设不负责把原曲面跨节点范数变为一致可控量。[MRVB](https://arxiv.org/pdf/2201.07019)
HRSS的相关主定理要求非退化椭圆trapping及严格单调周期，观测对象为密度/引力场等宏观量。
不能以其慢率反驳任意两光滑观测的 \(n^{-2}\)，也不能当作已覆盖本题双曲节点。[HRSS](https://arxiv.org/pdf/2405.17153)

新近来源没有改变上述直接包含边界：Hadžić–Moreno是带椭圆/双曲trapping的谱分析与非定量damping，2026-04-03发表。[官方](https://link.springer.com/article/10.1007/s00023-026-01692-1)
Liu Markov依靠非零twisted Markov模的衰减；去掉随机项后不能保留其指数阻尼结论。
其官方发表日为2026-05-18，version of record为2026-07-10；非搜索抓取日期。[官方](https://link.springer.com/article/10.1007/s44198-026-00424-7)

Liu–Zhang–Li Th3.1明确研究 \(N^{-1}\sum_{j\le N}\langle G\rangle_j\) 的Cesàro极限，并有非共振条件。
这不是未平均 \(C_n\) 的sharp渐近；原qPI的实能带也不能直接满足其逐I全非共振条件。
其一维非恒定连续旋转数在连通能窗必取有理值；原文证明的a.e.版本不能由本轮擅自替它补成新定理。
Q3后备下一步应先核精确概率对象、非共振与随机CLT假设，不把确定性Cesàro和随机结论混合。[原文](https://arxiv.org/pdf/2509.20690)
检索还浮出2026 weighted Hamiltonian题名，但没有完成一手核验；仅留未核线索，不计证据或分数。

## 5. 三层包含判断：不得把“能迁移”写成“已证明”

| 强组成 | 直接包含层 | 标准组合层：本审查的条件性推断 | 本题未证层 |
|---|---|---|---|
| 原测度、terminal、逐圆投影 | 非qPI原文；一般条件期望/流盒标准 | M的原对象核对 | M须独立数学接受，不产生衰减率 |
| 跨saddle、原光滑、无限模 | FHR在摆系统确已完成 | Morse符号估计＋真实\(\tau/L\)相位可复制机制 | 原能量/角度混合导数与求和闭合 |
| 驻点\(n^{-1/2}\)及振荡项 | 所读源无Q2同一定理 | TW/B分类＋二次驻相＋可求和Fourier幅度 | 原相位系数、余项、下界 |
| \(T=1\)端点\(n^{-2}\) | FHR已有相同端点率机制 | 原中心Taylor jet＋非零离散twist | 精确首项与泛型非消失 |
| \(T=3/16\)同能持续/收缩两圆 | 所读源无本对象结论 | 持续圆普通驻相＋收缩圆单侧端点展开 | 不同振幅阶的共同完整余项 |
| 原F换圆与奇偶 | 无该原对象表述 | 偶数迭代＋对\(f\circ F\)应用同一结论 | 两列准确系数，不误认全局单步角 |

对核心问题的回答是：**FHR定理本身不足以直接套出Q2-P；其证明机制加本对象核验很可能足够。**
这不是用短引理代替强目标；它是在假定强目标成立后扣除其主要已知分析机制。

## 6. 为什么原离散时间不是自动的新分析机制

以下是迁移充分条件的独立解释，不是替作者交付完成的Q2证明。
取 \(e=h-h_+\)、\(\ell=1+|\log|e||\)，圆周期 \(L=A(e)\log(1/|e|)+B(e)\)。
若原 \(F^2\) 有非零解析短时间 \(\tau(e)\)，其局部相位可取 \(\alpha=\tau/L\)，于是
\(|\alpha'(e)|\asymp(|e|\ell^2)^{-1}\)，逆导数为 \(O(|e|\ell^2)\)，并需全部所用阶的可微符号界。
这正是使原观测坐标的能量导数奇性在分部积分中可积的结构；不需要把 \(\tau\) 设为常数。
N §2–3供应这一原对象接口的作者证明；它若被数学接受，标准迁移压力明显加强，而非出现新阻尼机制。
但 N §4的纯角向Fourier界不能自动给 \(\partial_e^r\widehat f_k\)；这一混合估计仍需实际写出。
应证明各阶振幅经 \(a\mapsto-\partial_e[a/(2\pi i k\alpha')]\) 后可积、边界消失且能对k求和。
不能从未经控制的 \(O(1)\) 或 \(O(\ell^b)\) 直接求导；也不能把 \(O(\delta)\) 薄层尾单独改成时间率。
另一等价看法是用 \(u=\alpha(e)\) 将节点附近能量密度化为端点指数小的振幅，仍须验证有限阶符号界。
正则窗驻相和非驻相分部积分在已接受TW提供的分类上进行；这里无需Diophantine小分母假设。
奇偶可用 \(C_{2j+1}(f,g)=C_{2j}(f\circ F,g)\)，由M的投影对易及紧支撑范数转换保证合法。
原F的奇偶处理因此可以复用同一估计，但不允许把上区间 \(\rho_+\) 叫作F单步角。

## 7. 特殊层与最优性：真正需要写清的细节

T=3/16时，持续圆跨 \(h_-=-2\) 是双侧光滑圆管；即使整纤维奇异，其驻相首项也不能删除。
在另一收缩圆，令 \(\varepsilon=h_--h\)，原光滑非零模通常是 \(O(\sqrt\varepsilon)\)，相关振幅为 \(O(\varepsilon)\)。
结合B给出的非零二阶相位jet，单侧模型为 \(\int_0^c\varepsilon b(\varepsilon)e^{in(c_0+c_2\varepsilon^2+\cdots)}d\varepsilon\)。
故应核可能的 \(n^{-1}\) 次层；这是条件性端点推断，尚非原qPI的已证系数或必非零结论。
它不否定 \(n^{-1/2}\) 最优首阶；但若承诺更快于 \(n^{-1}\) 的余项，就必须显式扣除或证明该层消失。
持续圆的两侧人工截断边界也必须相消；不能把两段各自的边界项当成新物理贡献。
T=1时，有限正则能级无驻点不等于全相关任意快；中心消失振幅与非零一阶twist留下端点项。
紧支撑能窗排除无穷能量尾，不包含任何额外的 \(T\to1\)、\(T\to0\) 或 \(T\to\infty\) 一致渐近承诺。
驻点下界可在其光滑圆管内选一个谐波再拉回原观测；T=1中心则须用合法原一阶jet配光滑截断。
两者均应证明归一化相关的非零limsup，不能在中心任意指定一个不满足光滑兼容性的角函数。
这是下界构造，不是把全观测上界弱化为有限Fourier定理；实观测的模态配对/奇偶取消仍须核。

## 8. 条件性新意、价值与22–30页容量

条件新意7.6：原qPI的完整sharp率相图、特殊同能两圆与离散主项是实在增量，不能归零。
但“有相混合”“跨separatrix”“全Fourier”“中心消失阶控制率”已有强先例；驻相本身亦标准。
T=3/16、1的相位几何主要消费旧TW/B；新率分层是其分析后果，不能再把旧twist发现完整计一遍。
因此整体更像一个完成度可很高的具体系统sharp应用，不足以确认新的独立强分析中心。
条件价值8.2：若完整成立，可把代数可积性、原测度与可测的长时相关连接，且清楚纠正错误整纤维中心化。
此价值评价不声称非线性稳定、Hamilton嵌入、谱统计、算术/Riemann结论或别的系统族结果。

容量MID：22–30页在诚实呈现完整证明时**可能真实支撑，但不稳健，不能先给HIGH容量票**。
合理条件预算：问题/先例/主定理3–4页；原测度与分支接口2–3页；节点混合导数与求和5–7页；
驻相、两特殊参数及准确主项5–7页；最优性/奇偶/统一结论2–3页；必要引用说明1–2页。
总量约18–26页，22页落在可行范围内；这不是已经写成稿的页数，也不保证达到下限。
若充分使用FHR技术并引用旧TW/B，实际增量可能落到18–21页；不得重抄旧twist长证明来填22页。
反过来，若原范数到全Fourier的完整符号估计确有必需长证，约22–26页是可信数学容量，不是纯凑页。
有限范数阶数、sharp系数和合法余项是主定理内生工作；重复terminal图表、薄尾独立命名、泛泛背景不增加中心容量。
FHR整篇42页或HRSS60页包含不同任务，不能成为本候选需要22–30页的证据。

## 9. 建议、required fixes与结束条件

建议 `STOP_AS_INDEPENDENT_CENTER`：即使完整强定理最终成立，现有证据仍把主要机制定位为标准组合。
不是正式拒稿票，也不撤销已授权节点短证及其数学审查；不能据此自动删文件或改冻结输入。
若用户另行决定为数学价值完成Q2，以下是强定理必须补的科学项，不是通过预核的承诺：

1. 固定有限原范数阶数与能窗依赖；证明每侧混合导数、边界消失、全Fourier余项求和。
2. 从原F/F²准确写主项系数，保留换圆奇偶与持续圆；不给虚假的全局单步角。
3. 分开T=3/16两种振幅，核 \(n^{-1}\) 次层；对T=1给端点非消失条件与余项。
4. 给光滑观测下界构造及非零limsup，不将n=0薄层尖锐性当长时最优性。
5. 定位为具体qPI的sharp全曲面相混合，清楚承认FHR/MRVB及旧TW/B；不以“首次跨节点”包装。

真正足以改变本定位的证据应是当前强目标内一个已知迁移无法处理且具有新解释力的必要机制。
“补完原计划证明”“技术更长”“没有同名qPI论文”本身不会提升为高新意；也不要求扩大系统族来救题。
若没有这种新证据，保留Q2为同对象数学资产/后续应用；Q3只保存上述来源压力，不自动开新候选。
旧FAIL/HOLD/STOP、P31未准入、原22–30页及批次4/5均保持；本件不更新goal状态。

[S]: PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
