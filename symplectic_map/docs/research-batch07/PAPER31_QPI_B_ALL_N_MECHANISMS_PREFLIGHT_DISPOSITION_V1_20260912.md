# Paper31：指定 b 全阶机制、边界数学与查新预核处置 V1

日期：2026-09-12 UTC；主控 `/root`。全部规定新输入已终态并本人FULL核准。
状态：`SCOPED_MATHEMATICS_ACCEPTED / NOVELTY_PREFLIGHT_4_0_CAUTION / NO_CANDIDATE_ADMISSION`。
这是[前轮有界入口][MON]之后真正新增机制的处置，不重开准确厚度旧双FAIL或已接受Papers27–30。

## 1. 本轮结果与原目标

原目标不变：对全部 $N\ge4$，指定 $b=T:X_1(N)\to\mathbf P^1$ 的几何群是否为 $S_{d_N}$，或有哪些真实例外？
此原命题仍为 `NOT CURRENTLY JUSTIFIED`，本轮没有原构造反例，也不宣称已排除例外。
三份作者新推导、两份fresh非作者实际数学审查均已由主控本人FULL读回并核准，必要数学修正为空。
接受的是下面的限定数学，而不是完整全阶满群、正式候选、新意或容量PASS。

| 新输入 | 本轮实际证明 | 严格不推出什么 |
|---|---|---|
| [两端惯性机制][I] | 单支惯性循环子群含单二换位的完整阶分类；$N=2^k,k\ge6$两端惯性均偶 | 有限集合不是满群例外；不能断言整个群为偶群 |
| [全级标记分离][J] | 不同精确阶标记的 b 除子除±外不同；$\mathbf C(j,b)=\mathbf C(X_1(N))$ | 只排除含j中间域，不等于指定b覆盖不可分解 |
| [全部有限非零尖点][C] | 两类零阶尖点的 $b-b_*$ 均有非零一次项，故全都不分歧 | 不排除非尖点临界值碰撞，不供应全阶单二换位 |

Paper31仍非已准入项目，原正文22–30页及完整四门合同保持；未创建项目／锁／稿件／PDF或试排测页。
Papers27–30本地接受4/5不变；没有新的权限阻塞，不称原族耗尽、Batch07完成或跨论文终审已执行。

## 2. 全阶惯性路径的准确边界

有限置换的某幂为一枚二换位，当且仅当它恰有一个二循环、其它循环长度全奇。
原因是长度L的循环取幂若产生二循环，就同时产生L/2个；不能从四循环或多个二循环中任选一枚。
结合旧尖点公式的真实几何重数，[I]和[独立检查][MI]证明对全部 $N\ge4$：

$$\langle\sigma_0\rangle\text{含单二换位}\iff N\in\{7,9,11,18,22\},$$
$$\langle\sigma_\infty\rangle\text{含单二换位}\iff N\in\{6,8\}.$$

完整分类处理了 $N=4$ 不规则几何阶、$N=14$ 的两枚二循环、$4\mid N$ 第二段 $M\equiv14\pmod{16}$ 的剩余情形。
符号界留下的有限边界逐式手算不是精确阶方程或数值单值群扩阶扫描。
对 $N=2^k,k\ge5$，还准确得到

$$\operatorname{sgn}(\sigma_0)=(-1)^{2^{k-5}},\qquad\operatorname{sgn}(\sigma_\infty)=(-1)^{3\cdot2^{k-5}}.$$

所以 $k\ge6$ 时两者的任意共轭与乘积均偶，不能独自生成满对称群；$k=5$两者均奇，阈值不能擅自下移。
这严格结束了“继续找一个单端惯性幂就能全阶取得二换位”的拟议机制，不结束全阶满群问题。
一般N的两端混合乘积仍可能提供其它元素；二幂无限类必须另取有限非零分支的信息。

## 3. 双函数生成不是任意中间域排除

[J]在满级曲线上对所有原始标记向量给统一尖点阶，再用三个测试向量排除八分之一零阶候选。
余下非平凡倍点候选迫使 $N\equiv3\pmod8,N\ge11$，第二个阶比较又迫使N=7，矛盾。
由此全阶标记分离与稳定子闭合；[MI]独立核准行／列约定、短及长坐标分母、满级宽度和N4边界。
Galois对应给 $\mathbf C(j,b)=F_N:=\mathbf C(X_1(N))$。
任何真正 proper $\mathbf C(b)\subsetneq K\subsetneq F_N$ 因而必须满足 $j\notin K$，但仍有 $K(j)=F_N$。
这将未解决部分定位到不同j之间的b等值对应；同一椭圆曲线的标记稳定子再细化不能解决它。

抽象反例 $J=t^3,g=t^2+t,u=g(g-1)$ 满足 $\mathbf C(J,u)=\mathbf C(t)$，因为 $u-2J=t(J-1)$。
但 $\mathbf C(u)\subsetneq\mathbf C(g)\subsetneq\mathbf C(t)$ 是二乘二分解。
u是去掉四个简单零点和无穷点后的原始单位，所有有限分歧均为二阶，且5/16上恰有一枚二换位。
所以“双函数生成＋原始单位＋有限简单分歧＋单二换位”在一般函数域层面仍不足以证明不可分解。
此处J不是经典模j，该例不是指定原模曲线的反例；它只否定上述未经证明的代数升级。
Koo–Shin／Jung–Koo–Shin既有标记primitive-family和j扩张生成方法明确扣除，不包装成新的不可分解理论。

## 4. 有限非零尖点缺口已闭合

尖点阶公式的零点只有 $r=0$ 和存在时的 $r=3N/8$；主控新推导[C]逐一计算局部首项。
第一行用精确阶单位根 $\zeta$、$s=\zeta+\zeta^{-1}$ 和真实局部参数q，得到

$$b(q)=-\frac{(s+1)^3}{(s+2)^4}\left[1-(s-2)^2(3s+4)q+O(q^2)\right].$$

精确阶N≥4排除s=2,−2,−1；代数整数性排除s=−4/3，所以一次系数非零。
该行值互异，但非消失本质上就是旧节点式(11)的同一局部信息，不再记创新。
第二行写 $N=8m,q=z^8,u=\eta z^3$，$\eta=\zeta_N^a,\gcd(a,m)=1$，直接双级数展开给

$$b(z)=\eta^{-8}\left[1-3\eta^3z+O(z^2)\right].$$

真实宽度为八，所以z而非q是局部参数；一次系数 $-3\eta^{-5}$ 非零。
该行恰有φ(m)个几何尖点，其常数值为全部原始m次单位根，各一次；m=1的b=1也包括。
[fresh独立尖点检查][MC]逐式重证两展开、余项、宽度、符号计数及N4边界，主控FULL核准接受。
因此所有有限非零分支值的分歧点都必须为非尖点；不同行尖点值即使碰撞也不给惯性添非平凡循环。
未解决的是同一b值上非尖点的多个二阶／三阶分歧；旧局部e≤3依然不能保证它们分离。

## 5. 查新输入与C/D处置

[Phase A][A]在新推导之前冻结固定B1–B3：全阶群、任意中间覆盖、实际足够惯性，不是三个独立论文贡献。
[Phase B][B]201行由该文件作者执行36条实际查询；另有子定位者6条查询未并入作者计数，主控查询另列§6。
每面至少三类查询，基础不限年、2024–2026、2026-03-12至09-12窗口均实际执行。
十项去重一手来源含正常形／模单位／除子、j扩张生成、模中间曲线、不同投影的分歧和Baker2026模型对照。
结果仅为已读范围内未定位直接完成B1–B3的定理，不是无先例证明；数据库缺口与Fricke II缺式正文保留。
Scholar/Semantic Scholar搜索页不安全打开错误、arXiv搜索页超时及个别出版社403均按实际返回记录，不混写失败原因。
传统Tate级数、模单位自由基、全阶尖点除子、标记稳定子、传递／本原／二换位群论、旧C0和N4–9均扣除。

[fresh非作者C/D][CD]214行已冻结，主控本人FULL读回并核哈希；终态新意4.0/10，CAUTION / PROCEED WITH CAUTION。
B1–B3当前方法均LOW；未证全阶finding的潜在新意暂为MEDIUM，不能记入已完成贡献。
该席明确三短模块有实际用途，但扣除成熟除子、稳定子、Tate展开后，不支持当前包直接作22–30页论文中心。
其最强四项来源本人实际核读；另八条补查及全部十项来源／Fricke II和数据库缺口保留，不让缺读提高新意。
主控保留该分数和强反对，不补抽、平均、改题复投或将它称为正式双席四门FAIL。
指定GPT-5.4 MCP不存在可用审查接口；采用当前Codex xhigh fresh非作者fallback，不称跨模型验证。
该票只评固定未证问题和拟议机制的新意预核，不替代数学独查或完整候选的双席四门。

**合同表述澄清。** 冻结C/D §9末误写“四门各≥7.5”；主控初始委派的压缩措辞也不够精确，错误在此显式纠正。
原[正式处置][OLD]§1及共同manifest168–171行的合同始终是：新意≥7.5、独立价值≥7.5、完整证明信心≥9、可信完整正文22–30页容量PASS。
C/D作者已在无工具、无文件改动、无重评分的终态回复确认该更正不影响4.0/CAUTION；原票冻结保留，门槛没有改变。

## 6. 主控实际来源补充与检索账

本轮主控按 novelty-check、proof-writer 和 ARS有界来源角色工作；ARS仅为 three-way-scan 的来源检索／核对部分。
已本人FULL读所用技能、选定workflow与bibliography/source-verification角色及质量定义；不称完成整个ARS研究管线或PRISMA综述。
不运行来源resolver、Passport认证、人类已读标记或外部模型API；理论数学不套RCT等级。
本人另外的重点原文读取如下，不继承代理的原文阅读身份：

| 来源 | 主控本人实际范围 | 使用边界 |
|---|---|---|
| van Hoeij–Smith 2004.13644 | §2.1–2.3全文及前轮接受的指定b接口；当前尖点计数逐式读取 | 模单位除子为旧依赖，不声称新满群定理 |
| Koo–Shin2010，DOI10.4064/aa141-4-2 | 出版社PDF§1–2、Lemma3.1、Th3.2及证明、Lemma3.3、Th3.5及证明 | 标准q阶稳定子和含j生成；不覆盖任意C(b)子域 |
| Jung–Koo–Shin1506.06317v3 | 摘要、§1–2、Ex3.1；Prop4.1及证明、Th4.3及证明、Th4.4(i)及证明 | primitive标记族与b覆盖的置换本原性分开；未称全文17页 |
| Tate nonarch-ams | 引言、式(1)–(24)、Th1陈述及至同态证明的相关段，原印刷1–7页 | 经典乘法一致化和整数级数；不是新边界定理来源 |
| Baker2608.05299v1 | 摘要、§1.1–1.3含Th1.1/1.2；另看到§1.4作者AI声明 | 2026-08-05提交、内文08-07；模型同构β不是指定b投影，未核41页证明 |

Fricke families II（JMAA2019，DOI10.1016/j.jmaa.2018.11.033）主控只得搜索呈现，公式缺失；正常open为Internal Error。
不能把该缺读当作排除先例。Koo–Shin机构PDF主控返回明确Timeout fetching，随后取得出版社PDF；不冒称两版本等价。
另旁读Aoki2004出版社PDF§3式(3)–(5)，仅为Tate公式定位；不把抓取“数月前”当发表日期。
Baker的作者AI披露不构成本项目证明检查或高低质量票；本件只消费实际读到的定理陈述与适用对象。

下列12条主控query均实际于本轮执行；与Phase B可能重叠，不作独立去重命中数，不追加虚构数据库召回率。

| # | 原样 query |
|---|---|
| R01 | "Tate normal form" "symmetric group" |
| R02 | "modular unit" "indecomposable" |
| R03 | "modular curve" "monodromy" "b" Tate 2024 2025 2026 |
| R04 | "Tate normal form" "function field" j b |
| R05 | "modular function fields" "generators" "Siegel" j |
| R06 | "modular units" "primitive generator" |
| R07 | "modular curves" "indecomposable" "maps" |
| R08 | "Function fields of certain arithmetic curves and application" Koo Shin |
| R09 | "Primitive and totally primitive Fricke families" |
| R10 | "Primitive and totally primitive Fricke families with applications (II)" arxiv |
| R11 | "Function fields of certain arithmetic curves" "10.4064" |
| R12 | Tate curve X u q sum n qn u 1 qn u squared Silverman formula |

## 7. 已发生的范围偏差及隔离

全级标记作者的检查者自行委派 `/root/p31_b_indecomposability_mechanism/full_level_stabilizer_check/finite_residue_check`。
该子任务通过 `functions.exec`→`exec_command` 运行Bash内嵌Python3（`python - <<'PY'`），枚举N=4至64的原始候选与测试剩余向量。
它比较整数分段阶函数，断言正规化稳定子为±e1；任务退出码0、状态completed，只打印标准输出，无文件写入。
这超出本轮不扩阶枚举边界。获知后明确停止，不再索取新计算，只追回已有执行事实。
该结果没有被消费为全阶证明、补强证据或证书；fresh数学审查明确禁止并未运行任何枚举、CAS或再委派。
没有生成N≥10精确阶方程／单值群表，但不能因此声称本轮“从未运行任何N≥10有限算术检查”。
已冻结作者文件的简略披露不回写；本节给出完整终态事实，不让偏差自行形成后续权限。
另一尖点审查者补读旧稿145–168行是同一归一化依赖的紧邻定位，主控确认后实记145–205 PARTIAL，未重审旧证明。

## 8. 本轮输入身份与接续

下表八件对象均已终态，主控本人FULL读回。哈希绑定科学内容，不代替阅读或数学核查。

| 对象 | 行／字节 | SHA256 |
|---|---:|---|
| [Phase A][A] | 66／5494 | 6740c84a45ef60b5f86118837307380a7895c4f47be8ec860dfac9ab57f54f3d |
| [Phase B][B] | 201／18472 | f72db24a15663002b9e6d26f6008d522e97d7c41704cc2eeb67f00b79b77899f |
| [惯性作者][I] | 143／10699 | b166abe3c3de351ffb737f08b6faa8dcc300e11e4cc30e1e2dd1c8424090ff55 |
| [标记作者][J] | 154／12126 | c572a42de403a687aa469ad60869945238836c2c0457291d73f2768983b34e86 |
| [尖点作者][C] | 110／7488 | cc995a3e5232021349b03c59093a51a6c285f549ac52e238c493f75ee4d9d1b0 |
| [机制独查][MI] | 164／13162 | e1cd459aacfaed3369f89ad49ede748b0b3d13b832256e92eddc0af496fb32c7 |
| [尖点独查][MC] | 111／8533 | d01000462d03023091406386ab986d8a56355bbfdde4cc68149cdcf98f862e45 |
| [独立C/D][CD] | 214／17403 | 1e46709b142277a5af9e2e51821bf95905f8f32e60d9bc99926685ccba8ff8d1 |

旧[准确厚度正式双FAIL][OLD]、[前轮来源与十问范围][SCOPE]、已接受N4–9及全部原族证明保持。
下一项只可由当前实际结果进入新机制：不含j的指定b中间对应、非尖点临界值的完整惯性；不继续扩大已受阻的单端幂／标记稳定子路径。
Q4实旋转数／twist仍为另一母问题，其强来源缺读与全局分支义务不因本轮自动解除。
不把上述短推论拼成新候选，不扩N≥10扫描、不重投旧同包、不改正文合同；本件终态后更新一次当前入口。

[MON]: PAPER31_QPI_MODULAR_B_MONODROMY_FEASIBILITY_V1_20260912.md
[A]: PAPER31_QPI_B_MONODROMY_NOVELTY_PHASE_A_V1_20260912.md
[B]: PAPER31_QPI_B_MONODROMY_NOVELTY_PHASE_B_V1_20260912.md
[I]: PAPER31_QPI_B_GLOBAL_INERTIA_MECHANISM_V1_20260912.md
[J]: PAPER31_QPI_B_INDECOMPOSABILITY_MECHANISM_V1_20260912.md
[C]: PAPER31_QPI_B_FINITE_NONZERO_CUSP_RAMIFICATION_V1_20260912.md
[MI]: PAPER31_QPI_B_NEW_MECHANISMS_MATH_REVIEW_V1_20260912.md
[MC]: PAPER31_QPI_B_CUSP_RAMIFICATION_MATH_REVIEW_V1_20260912.md
[CD]: PAPER31_QPI_B_MONODROMY_NOVELTY_CD_V1_20260912.md
[OLD]: PAPER31_QPI_EXACT_THICKNESS_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md
[SCOPE]: PAPER31_QPI_POST_EXACT_SOURCE_AND_SCOPE_V1_20260912.md
