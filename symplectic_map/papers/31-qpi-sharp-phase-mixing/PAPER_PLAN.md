# Paper31 — Paper Plan V1

日期：2026-09-13。状态：`AUTHOR_OUTLINE_FROZEN / FORMALLY_ADMITTED_SCIENTIFIC_INPUT / OUTLINE_SCOPE_REVIEW_PENDING`。
题名固定：**Sharp phase mixing for the autonomous q-Painlevé I map**。
本件是中文作者大纲，拟正文为匿名英文；不是新科学票、source/publication lock、英文稿或 PDF 验收。
准入以[正式双席处置][ADMISSION]为准；[BRIEF] 与各原证明头部的历史 pending 不在本件回写。
本计划已定向对齐 root 冻结的 [source scope V1][SOURCELOCK]、[publication lock V1][PUBLOCK] 与[引用记录 V1][CITATIONS]；不编辑这些锁。

## 1. 一句话贡献与制作配置

一句话贡献：对任意固定正参数，证明原自治 q-Painlevé I 映射在完整实曲面上、对原光滑紧支撑观测逐连通圆中心化后的 sharp 未平均相关渐近，给出全参数的准确振荡主项、有限原范数余项、两节点贡献及原单步换圆奇偶。

全稿只有这个中心。下列三个从属主张是同一定理的可核验方面，不是三个新方法或三篇论文。
旧模型、forcing、频率图、两个阈值和标准相混合技术不重新计作本文的独立发现。

| 配置项 | 本稿采用的明确约束 |
|---|---|
| 项目与交付 | `papers/31-qpi-sharp-phase-mixing/`；仅本地，当前无目标期刊，不套 ICLR 或其他会议模板 |
| 外部评审标准绑定 | `criteria_binding_unavailable`：无目标期刊/track，因此不宣称 venue alignment 或 submission readiness；这是当前不适用的外部绑定，不是待用户确认或新的硬门 |
| 文种与匿名 | 英文纯数学 article；匿名作者块，不生成作者身份或单位 |
| 版式 | 单栏 article 11pt、letter、四边 1 inch、普通行距与段落 |
| 正文硬窗 | 22–30 页；标题、摘要、引言、完整主定理、全部题目特有必要证明及结论均计入 |
| 参考文献 | 结论后另起页，另计；不能将必要证明挪入参考文献前后的附录或补充材料 |
| 编辑目标 | 自然完整写法约 28–29 页；下表中心目标 28.5 页不是实测、保证或新的容量票 |
| 软文字预算 | 全稿英文正文约 8,000–10,000 词，含首尾但不含参考文献；公式不折算成词或页，完整性和真实 PDF 页数优先 |
| 文件结构 | **8 个编号 section 文件**；另有 1 个不编号的 abstract 文件，references 不计 section |
| 科学边界 | 保留原完整观测类、全部正参数、两节点、四 terminal、无限 Fourier、原单步奇偶；不作数值、CAS、参数/阶数枚举或试排短稿 |

不把 Paper30 的 22–40 页例外迁移到本稿。高端超窗风险真实存在；发生后先核实际重复和转录负担，不能缩字号、改边距、删量词或外移证明。

## 2. 三个从属主张—证据—正文矩阵

| 从属主张 | 已接受的实际证据 | 正文承担位置 | 状态及归属边界 |
|---|---|---|---|
| C1：原完整观测类上的全局强率，而非删节点的正则能窗结论 | [M] 原测度、proper 能窗与逐圆投影；[N] 原节点周期/解析时间；[K] 全圆混合导数；[E] 原 jets；[G] §§3–6 全模积分与拼合 | §2 定义及定理；§5 双曲端；§6 椭圆端；§7 全局合成 | 完整数学已接受；原 C²⁰ 范数不能换成不明的作用角无限光滑范数。标准 coarea、投影及 FHR 式分析不申报首创 |
| C2：两个特殊参数的准确主项及 sharpness | [PF]/[B]/[MID]/[UP]/[INF]/[TW] 必要频率链；[B] §5 中心相位 jets；[E] §§6–8 两种端点；[G] (1.2)–(1.6)、§8 | §2 给完整公式；§§3–4 证明频率输入；§6 端点系数；§7 原观测非零 limsup | 旧 twist 图和阈值完全扣除；新结论是同一原系统的相关渐近，不能把每行参数算一项独立创新 |
| C3：真实离散动力的相位与奇偶，不将它换成全局常数时间流 | [GEO] Step 4–5 原 +P 与换圆；[M] §4 对易及 ±1 障碍；[N] §3 原 F² 的解析能量时间；[G] §§3、7 原奇偶系数 | §2 固定对象与投影；§5 识别原局部时间；§7 写出两列准确振幅 | 分支回返、有限迭代和消零模不是新机制；其作用是保证完整原命题没有被替换 |

各证据都是纸面证明，不配置实验、拟合指标或数值验证。准入后的独立大纲核对只查这些责任与制作锁的一致性，不重抽已经通过的四门票。

## 3. 主定理必须在前部完整出现的内容

首屏在 Abstract/Introduction 中先用三行结果表给读者最重要的信息；精确量词、系数和全部余项随后在 §2 集中定义一次。
以 n=2m+r、m≥1、r∈{0,1} 表示原步数，表内 O 常数由固定 T、固定紧能窗及原 C²⁰ 范数乘积控制。

| 参数 | 逐圆中心化的完整相关 | 主项来源与最慢阶 |
|---|---|---|
| T∉{3/16,1} | m^(-1/2)𝒜ᵣ(m)+O(m^(-3/2)) | 全部非退化驻圆；最慢 n^(-1/2) |
| T=3/16 | m^(-1/2)𝒜ᵣ(m)+m^(-1)𝒟ᵣ(m)+O(m^(-3/2)) | 同一能级的持续驻圆与消失椭圆圆；最慢仍 n^(-1/2) |
| T=1 | m^(-2)ℬᵣ(m)+O(m^(-3)) | 原椭圆中心一阶 jets；最慢 n^(-2) |

§2 的完整声明不得只留下这张表。必须逐项陈述：

1. 原 torus 表达式 F_T(x,y)=(T/(x−y),x/y)、h=−x+y+x/y−T/x、Ω=dx∧dy/(xy)；实际定义域为原 U_T=S_T∖D 的完整实点，四条 terminal 全保留，h proper。
2. μ=|Ω|，Π 为逐连通圆的条件均值；内积第一槽线性，C_n(f,g)=⟨((I−Π)f)∘F_T^n,(I−Π)g⟩，f,g∈C_c^∞(U_T)。不假设 (I−Π)f 仍原光滑。
3. 固定闭有限能窗 J 包含支撑能量，可扩大覆盖两临界值与当前驻点能量；在稍大紧饱和能窗的有限原图册定义 C^a 范数。常数可依赖 T、J、阶数与图册，不承诺接近参数阈值的一致性。
4. 令 G_T=F_T²、f_r=f∘F_T^r；在正时间角中 σ=2ρ₋、2ρ₀、ρ₊，持续圆的 σ 跨 h₋ 解析延拓。ρ₊ 本来就是 F_T² 的圆回返角，不再乘二。
5. 驻圆集合 𝒮_T 按圆而非仅能级计数：中区间一圆 / T=3/16 时 h₋ 的持续一圆 / 下外同能两圆 / T=1 时空 / 上外同能两圆，依次对应五个参数区间；每圆 σ″<0。
6. 将 [G] (1.2) 的 𝒜ᵣ 写为对 c∈𝒮_T、k≠0 的**绝对收敛**级数，系数为 L(h_c) f̂_{r,c,k}(h_c) overline(ĝ_{c,k}(h_c))/√|kσ″(h_c)|，指数为 2πikmσ(h_c)+iπ sgn(kσ″(h_c))/4。不得漏 Fourier 求和、圆重数、相位符号或添一个多余 2π。
7. 以 ε=h₋−h、σ_E(ε)=2ρ₋(h₋−ε)、σ_c=2θ_T 定义 A_k^(r)=∂_ε[L f̂_{r,k} overline(ĝ_k)]|₀。A_k^(r) 仅在 k=±1 可非零，但原观测和余项仍保留全部模式。
8. β=σ_E′(0)=−2ρ₋′(h₋) 在 T≠3/16 非零；ℬᵣ=−Σ_{k=±1}A_k^(r)e^(2πikmσ_c)/(2πkβ)²。γ=σ_E″(0)=2ρ₋″(h₋)<0 在 T=3/16；𝒟ᵣ=Σ_{k=±1}iA_k^(r)e^(2πikmσ_c)/(2πkγ)。这两个符号与因子必须来自 §6 的实际端点积分。
9. 同一主定理附完整固定 saddle 截断的局部结论：对每个指定整数 N≥1 为 O(m^(−N))，原 C^(N+2) 足够；不把固定 C²⁰ 说成控制任意 N。
10. 对每个固定 T 有合法实/复原光滑紧支撑观测给相应归一化绝对相关的正 limsup。T=1 的非消失条件为一阶 jet 对中的开稠密条件；首 jet 消失至少 O(m^(−3))，不主张全部高阶 jet 的最优分类。

原单步的两列系数将在 §7 作为主定理的显式展开写出；§2 用 f_r 的定义已经准确覆盖所有 n，不延后原观测类或奇偶量词。

## 4. 统一术语与记号表

| 对象 | 拟正文统一写法及防冲突规则 |
|---|---|
| 参数、空间与算子 | T>0；U_T 表示实曲面，𝖴 表示 Koopman 算子；G_T=F_T²，不将几何输入文件别名 G 当数学符号 |
| 临界点与临界能量 | w₋<0、w₊>1；s₋、s₊ 为对应原坐标点 (w²,w)，h₋<h₊。全文称 elliptic centre/acnode 与 hyperbolic saddle/split node，说明曲线奇点和能量临界点的对应 |
| 辛形式与周期 | Ω 只留给原辛二形式；η 为正则纤维的相对时间形式，ω 为其 Weierstrass 表达；**所有旧稿 Ω(h) 周期统一转为 L(h)>0** |
| 时间方向与测度 | ι_XΩ=−dh，η(X)=1，dh∧ω=+Ω 在相对意义成立，dμ=L dh dθ；中心 ε 坐标取正测度 L dε dθ，不把有向微分负号带入绝对测度 |
| 角与频率 | θ∈ℝ/ℤ 为正 Hamilton 时间角；ρ₋、ρ₀ 为 F_T 的提升，ρ₊ 为 F_T² 的提升；σ 为统一的 G_T 相位，θ_T 为中心原单步极限角 |
| 模态与迭代 | Fourier 用 e^(−2πikθ)，k∈ℤ；n=2m+r 的 r 仅取 0、1。椭圆有符号半径改记 ϱ=√(2ε)，不与奇偶 r 重名 |
| 能量局部变量 | saddle e=h−h₊；elliptic ε=h₋−h；无穷端 ξ=1/|h|、ν=sgn(h)。不能把无穷端 ξ 与椭圆 ε 的导数混用 |
| 原坐标与归一化坐标 | terminal 用 (a,b)；Weierstrass 用 (u,v)，完成方后 (u,Y)，短式用 (X,Y)；Morse 局部用 (p,q)，其 q 不作全稿全局符号 |
| PF 及倒相位符号 | 将旧 q=8h−9 统一写 q₀(h)，H=32T+3h；PF exact primitive 写 Q_PF，倒相位导数写 Q_inv=1/α′，避免三种 q/Q 共名 |
| Wronskian 与截断 | W=L I′−I L′，J_ρ=(δ/q₀)L²ρ′；能窗固定记 J，若同节会混淆则写 J_energy。平滑能量 cutoff 写 χ，不把它用为组件指标 |
| 主项及 jets | 𝒜ᵣ、ℬᵣ、𝒟ᵣ 是序列；A_k^(r) 是原中心 jet 系数，R_k 是端点余项；d_{f,±1} 是原一阶角模，不使用“任意指定中心单模”措辞 |

上述重命名只消除冲突，不改变原证明的规范。写作前建立逐式转录对照，尤其检查 L/Ω、q₀/q、r/ϱ 和 ν/σ；不得把不同分支的有利提升拼接。

## 5. 章节与实质篇幅目标

以下是单一作者结构预算，不从 R1/R2 的最佳模块拼成新票，也不从源文件行数或 bytes 折页。
数字用于提醒证明负担，章节可在同一科学范围内互相借空间；它们不是必须逐节精确达成的页数或字数门。
表中的相对文件名属于 publication lock 选定的首个完整源 `paper/v1/`；本次尚不创建该源树或任何 TeX 文件。

| 文件（拟创建；本次不写 TeX） | 标题 | 编辑目标页数 | 主要证明负担 |
|---|---|---:|---|
| `sections/00-abstract.tex` | Abstract（不编号） | 0.50 | 约 180–230 词，完整观测对象和三行强结果 |
| `sections/01-introduction.tex` | 1. Introduction | 1.50 | 单一问题、最强先例扣除、结果预览和路线 |
| `sections/02-real-surface-main-theorem.tex` | 2. The real surface and main theorem | 4.00 | 原模型接口、实圆、terminal、投影及完整定理/系数 |
| `sections/03-picard-fuchs-forcing.tex` | 3. Picard–Fuchs forcing | 2.25 | 原非齐次方程完整特征零推导与 Wronskian |
| `sections/04-global-frequency-geometry.tex` | 4. The global frequency geometry | 6.50 | 有限端点、真实锚、表观奇点、可微无穷渐近和全参数分类 |
| `sections/05-hyperbolic-fibre-estimates.tex` | 5. Hyperbolic fibre estimates | 6.25 | 原周期次数与解析时间、混合符号、接缝、全模消边界 |
| `sections/06-elliptic-jets-endpoints.tex` | 6. Elliptic jets and endpoint asymptotics | 3.75 | 正向对称角、原 jets、偶函数下降和两个端点展开 |
| `sections/07-global-asymptotics-sharpness.tex` | 7. Global asymptotics and sharpness | 3.50 | Fourier/驻相求和、完整分割、原奇偶和真实下界 |
| `sections/08-conclusion.tex` | 8. Conclusion | 0.25 | 准确结果与适用边界，不另开研究主线 |
| **正文合计** | 标题及首尾包含于以上前部预算 | **28.50** | 全部必要证明在正文；参考文献另页 |

### Abstract：以具体定理开场

目的：不用背景套话，直接说明在完整原实曲面上得到了何种 projected correlation theorem。
五个信息单元依次为：原对象和结果；跨两种退化纤维与单步换圆的难点；频率几何/原符号/原 jets 的证明路径；全 Fourier 与有限原范数保证；T=1、T=3/16 的量化差异和 sharpness。
首屏三行表放在引言前部，不在摘要堆积符号。摘要不引文、不自称首次跨 separatrix、不宣称普适新阻尼机制。

### §1. Introduction

目的：读完引言即知道 What（完整未平均相关渐近）、Why（原观测跨退化圆与不变分量）和 So what（真实 qPI 的最慢相关尺度由参数和几何精确决定）。

- 开头说明原系统保留能量，有限分支回返在连通圆上旋转，上区间原单步会换圆；单圆旋转不是混合，研究问题是能量系综中消去逐圆零模后的相关。
- 首屏结果表即本计划第3节的三行摘要；紧邻解释 T=3/16 的 m^(−1) 来自消失圆，而同能级持续圆仍贡献 m^(−1/2)。只在正文 §2 定义全部系数，不在引言重复长公式。
- 用三个短贡献段对应 C1–C3。旧全实频率图只是必要输入，本文因其未成篇而给完整证明，不宣称重新发现它。
- Related work 整合为按问题组织的三至四段，不另设固定一页综述：原光滑/退化轨道相关（FHR，辅以 HRSS）；频率非退化与驻相（MRVB，标准方法）；确定性离散 Cesàro 与随机扰动（Liu–Zhang–Li、Liu2026）。每组说清对象/假设/时间平均/机制差异，不用题名缺席证明新意。
- 最强限制正面保留：这里是具体原系统上的新完整结论，方法上承受 FHR 与标准振荡积分的强先例压力；不称文献穷尽或世界首创。P30 原几何按其真实未发表本地稿件身份归属。
- 路线只用一小段：§§2–4 固定原系统及所有驻圆；§§5–6 控制退化端；§7 合成并证明最优性。

自然转场：准确的相关对象依赖完整曲面与正确条件均值，因此先固定这些接口，再陈述定理。

### §2. The real surface and main theorem

目的：使原分式之外的完整动力、所有定理量词与系数在同一位置可查；后文无需反复重建对象。

拟子节及实际证明位置：

1. **The original surface and finite fibres.** 给 P30 已接受曲面构造的精确接口命题：原八中心、D=(h)_∞、U_T 为有限基的原补集、F_T 的完整自同构。明确这一基础由 P30 本地 accepted unpublished manuscript 支持，不复写一般 r 法丛链。用 [GEO] Step 4 在实光滑射影纤维上证明实际 φ、逆式与 +P 延拓，而非直接援旧 p>3 概形 PASS。
2. **Real circles and terminal points.** 用 [GEO] Steps 1–3 的消元 T=w³(w−1)、h=w(3−2w)、δ′=w²(4w−3)³ 证明只有两个简单实坏值；完成方三次根型给 2/1/2 圆及 P 所在分支。保留 h=1 分解与原四阶点作为上区间定位锚；实 Lie 群商给准确最小分支回返。合成一个四 terminal 表，列原图、h|_{a=0}、Ω 密度和 −2P/−P/O/P 像，避免 [M] 与 [GEO] 重复两遍表。
3. **Measure, conditional means, and norms.** 直接代入证明 terminal 密度不退化、h_b≠0；原 F 保 h、Ω 的稠密开恒等式延到全 U_T。给 dh∧ω=+Ω、η(X)=1、dμ=L dh dθ 和双圆周期相等的证明。由 proper 基变换/紧实曲面证明闭能窗饱和紧，临界纤维 μ-零；说明 terminal 原图与 (h,a) 有限阶范数等价。定义 Π，证明正交性、支撑饱和紧及 Π𝖴=𝖴Π；给上圆 ±χ 产生 −1、下圆 ±χ 产生 +1 的短反例，排除整纤维均值替代。
4. **The sharp correlation theorem.** 集中写本计划第3节清单的全部定义和完整定理，含 𝒮_T、𝒜ᵣ/ℬᵣ/𝒟ᵣ、原 C²⁰ 余项、saddle 的逐 N 范数及 sharpness 量词。相位 gauge 同时作用于两个 Fourier 因子会相消；正则圆管上的能量/角度有限范数等价作为后续公共引理。引用后文命题编号解释每块来源，不在此重复证明。

不把持续圆的详细解析参数化在此及 §4 各证一次：本节说明 acnode 的孤立性与分离，实际双侧周期/相位的解析延拓统一放 §4.1。
不把 Π 的像误称原 F 的不变子空间。投影非 Hölder 的实际例子在 §5.2，仅在本节提示其存在。

自然转场：定理主项由 σ 的全部驻圆决定；要排除漏掉的圆，先推导控制其导数的原 forcing。

### §3. Picard–Fuchs forcing

目的：完整提供旧未成篇的原方程及真实边界项，给 §4 共享的唯一 Wronskian 工具。

1. **A marked reduction.** 按 [PF] Claim、Steps 1–2 固定短式坐标 X=u+(h²−4T)/12、Y=v+(hu−T)/2，以及截面 (X_P,Y_P)=((h²−4T)/12,T/2)。ω=dX/(2Y) 不带 h 依赖缩放；明确固定 X 微分与移动截面全导数的区别。给 a,b、α_PF、β_PF、γ_PF、r₀、r₁ 的可核公式，并实写两条 G0 多项式还原恒等式，由此得到 Gauss–Manin 两式，再消去第二类微分。
2. **The endpoint calculation.** 写组合 primitive Q_PF 的简式和 O 处局部参数展开；展示 R₀、R₁ 各有极部而组合恰消、Q_PF(O)=0。完整两次 Leibniz 项必须出现，特别 2X_P′f_h(P) 不能因 Y_P′=0 消去。实写 Q_PF(P) 与移动项的相消，得到 𝓛I=−H/(q₀δ)、𝓛L=0 和算子全部系数。
3. **One Wronskian identity.** 一次性推导 J_ρ=(δ/q₀)L²ρ′ 与 J_ρ′=−jHL/q₀²，其中 j=1 对 +P、j=2 对 +2P。对后者解释局部 log(2P)=2log(P) 模固定整周期，不能把跨分支复弧称为实圆单步角。§4 在真实弧上应用，不重新做第二遍 G0 或端点代数。

本节不含 [PF] Steps 3–5 的正特征导数、Hasse、μ(P) 或厚度消费者。不能以“见已接受本地 PF 笔记”代替以上证明。
标准还原背景如需加引文交 root 的 citation 核验；本题恒等式和端点计算已经明确自证，不靠未经核验的引用补证明。

自然转场：微分恒等式本身没有积分常数；实际持续圆与两无穷端将固定这些常数并闭合所有符号。

### §4. The global frequency geometry

目的：实写定理消费的全部旧 twist 证明，准确确定驻圆及椭圆相位 jets；不扩成旧值域论文。

1. **The persistent circle and its anchor.** 用 [GEO] Step 3 的简单根 r(h) 和 u=r(h)+s²、s∈ℝP¹ 参数化，核无穷图、ω 非零、P 截面与持续圆双侧解析；这也服务 §7 的跨 h₋ 驻相，不重复建图。由 [B] §§3–4 的真实 L、ρ 解析性得 J_ρ(h₋)=0 和锚定积分。实写 H(h₋)=w₋(2w₋+1)(4w₋−3)²、δ′(h₋)<0，以及 H 的一次过零如何给至多一个且非退化的极大。保留 [B] §5 的准确 ρ′(h₋)、特殊 ρ″(h₋) 公式，为 β/γ 服务。
2. **The middle interval and the upper return.** 先用 [MID] §§2–5 的真实正向弧证明 θ_T=1/2+π⁻¹ arctan(1/√(3−4w₋))；中间上端短弧有界、完整周期经 Fatou 发散给 ρ₀→1/2，从而把“至多一个”变为 T<3/16 的“恰一个”。再用 [UP] §§2–5 的有符号解析 s₂(h)=T(h−1)/(2√((T−r₁)(T−r₂))) 定义真实 2P 弧，核 h=1 的 1/2 与 h↓h₊ 的 0。利用 §3 的 j=2 Wronskian，令 K_tw=δL²ρ₊′，从 q₀K_tw′−8K_tw=−2HL 在 h=9/8 解析代值得 ρ₊′=H/(4δL)>0。原相位无奇点，只有 J_ρ 有单极；给两侧符号与至多一个非退化极大的完整论证。
3. **Differentiable infinity constants.** 将 [INF] §§3–6 两端合为一个 ξ=1/|h|、ν=±1 引理：实际解析根方程产生 D_r=r₃−r₁、d_r=r₃−r₂ 的带导数尺度；同一完整积分给 log(4/κ_mod) 及 κ_mod∂κ_mod 余项；实际短弧的 B₋∼Tξ、B₊∼T 是两个不同移动尺度，必须分别代回，并控制两参数偏导。写明 L、短弧的 C¹ 展开，先求导后相消，得到 J₋(−∞)=(log T)/8、J₊(+∞)=−(log T)/4 及 O_T(log|h|/|h|) 误差。不能对裸 O(1) 或 o(1) 求导，不能除以 log T 丢掉 T=1。
4. **Exactly the stationary circles used above.** 依 [TW] §§2、4–5 合成下/中/上的严格导数符号，逐参数说明不存在额外零点和水平拐点；T=1 的严格性来自 J 的严格单调及零无穷极限。五行 twist 表在此作为证明末尾的压缩结论，随即转为 §2 的按圆集合 𝒮_T。单独说明 T=3/16、h₋=−2 的持续光滑圆非退化驻点不属于“正则能级”计数，却必须属于相关驻圆集合。

共享去重：真实实圆参数化、端点弧和正方向只建一次；有限与无穷论证的公共 Wronskian 只引 §3。不消费完整七值域表、极大值积分方程、θ_T=5/8 的额外比较阈值、全有理角周期表或源桥，均不纳入正文篇幅。
两个无穷端虽不是紧支相关中的空间尾，仍是全参数“恰有这些驻点”的必要证明，不能借紧支性删除。

自然转场：驻圆已经全部找出，但正则角坐标在 saddle 退化；需要从原曲面范数直接控制这些角坐标，而不是删掉节点能带。

### §5. Hyperbolic fibre estimates

目的：以完整固定 saddle 邻域证明逐 N 的全 Fourier 衰减，保留原 F²、全部退化圆和真实消边界。

1. **The original passage time.** 按 [N] §§1–3 给临界 Hessian/线性化所需计算、κ=w₊√(4w₊−3)、𝔞=arcosh((2w₊−1)/(2(w₊−1)))。在 e=pq、Ω=−a₀dp∧dq 正向 Morse 图证明穿箱时间的解析对数展开；通过真实 split-node 归一化明确上侧每圆一次、下侧唯一圆两次。原横截面上的 F² 给同一个双侧解析 τ(e)，用流对易、局部解析恒等及完整圆传递延拓，核 τ(0)=2𝔞/κ>0；不是分别任意选周期提升。
2. **Why original regularity must be retained.** 用 [N] §4 的原 f−f(s₊) 时间积分界说明 Πf=f(s₊)+B_f/L；从原时间导数和圆上分部积分给全部非零 k 的 O(L⁻¹) 与 O(L^(j−1)|k|^(−j)) 双界，明确角向有权范数可增而不是所有 Fourier 范数都发散。给 [N] §5 的正则 separatrix bump 例子，解释中心化后沿节点路径为 1/log(1/radius)，不具任意正阶 Hölder。只对原 f、g 取导数；这些短说明不另立创新或空间尾章节。
3. **Mixed symbols on the full circle.** 完整实现 [K] Steps 1–5：固定正则解析横截面和有限箱/外弧；u_log=log|p|、D₀=e∂_e|u_log=q∂_q、∂u_log=p∂_p−q∂_q；明列各阶移动入口导数而非只微分大 O；由 S(e,u_log)=(θ+ν_loc)L、S_u≥c 归纳 Euler/θ 混合 jets，再恢复 p、q 的因子，防止额外 e^(−Ca) 损失。箱外用固定短时流图；入口、出口和 θ=0=1 接缝以开重叠核导数，允许角宽 O(1/L) 而不微分移动特征函数。最后用 e^a∂_e^a=D(D−1)…(D−a+1) 与周期分部积分得到全部 k 的 C1/C2 型估计。
4. **The inverse phase derivative and actual boundary terms.** 完整实现 [K] Step 6 和 [G] §4：α=τ/L，R_hyp=(Dτ)L−τDL→τ(0)A(0)>0，Q_inv=eL²/R_hyp；证明各阶 ∂_e^aQ_inv=O(|e|^(1−a)ℓ²)。对 χL f̂_{r,k} overline(ĝ_k) 证明 𝒯a=−∂_e(Q_inv a) 保持 conormal 类；每次真正消失的是 Q_inv𝒯^ja=O(eℓ^M)|k|^(−2s)，不是 𝒯^ja 自身。先截断后 N 次分部积分再取节点极限，给可积对数主控、Σ|k|^(−N−2) 求和及原 C^(N+2) 界。合计上侧两圆与下侧一圆；不选随 m 缩小的能带替代此证明。

此节用一套混合导数归纳覆盖有限所有象限/圆；不能逐象限复制，也不能只写一个箱后声称全圆。空间能带面积的精确 4/κ 常数及 n=0 尾尖锐性是 [N] 的已接受辅助结果，但 [G] 完整时间定理不消费它们，不作为本文额外命题或填页材料。

自然转场：saddle 在固定截断下比任意指定多项式都快；决定另一类端点的是消失圆上的原光滑 jets。

### §6. Elliptic jets and endpoint asymptotics

目的：同一原角构造服务普通与退化端点，得到 ℬᵣ、𝒟ᵣ 的准确符号、有限范数余项及全模结论。

1. **A positive symmetric time angle.** 依 [E] §4 取 h=h₋−(p²+q²)/2、Ω=−b dp∧dq、b>0；必要反射后 X=b⁻¹∂φ，b(0)=1/ω₋，L₀=2π/ω₋。用 b_ϱ 的唯一零均值周期原函数定义 Ψ_ϱ 和解析逆角，证明 z(−ϱ,θ)=z(ϱ,θ+1/2)，不是默认任意作用角都满足该对称性。
2. **Ambient jets and summable remainders.** 依 [E] §§5–6 证明 f̂_k(−ϱ)=(−1)^k f̂_k(ϱ)，同 k 振幅为偶函数且至少二阶消失；实写偶函数下降的积分恒等式与四阶 Taylor 除法，得到 L f̂_{r,k} overline(ĝ_k)=εA_k^(r)+ε²R_k(ε) 的真正闭半轴光滑性及 (1+|k|)^S C^J 余项界，原阶数为 2J+4+S。写 d_{f,±1}=(a_f∓ib_f)/2、A_{±1}=2L₀d_{f,±1}overline(d_{g,±1})，其余 A_k=0；不能把高模从观测类删除。
3. **The nonstationary endpoint.** 依 [E] §7 取 x=sgn(β)(σ_E−σ_c)，在整个固定 cutoff 支撑 σ_E′≠0；变换振幅 b_k(0)=0、b_k′(0)=A_k/β²，三次分部积分产生准确负号及 O(m^(−3))。J=3、S=2 已由原 C¹² 控制，因此共同 C²⁰ 足够，不主张最小正则性。
4. **The quadratic endpoint at T=3/16.** 依 [E] §8 取 x=√(2(σ_E−σ_c)/γ)，x=ε(1+O(ε))；振幅 xc_k，c_k(0)=A_k。用紧支积分实际分部积分得到 iA_k/(2πkmγ)，再以 |km|^(−1/2) 分割/积分估计余项，全部 k 绝对求和得 O(m^(−3/2))。不能调用不收敛的裸 ∫₀∞xe^(iωx²/2)dx 当普通广义积分。

本节只积分消失圆；T=3/16 同能级的持续圆不在此域，须留到 §7 作一次双侧驻相。相位 β/γ 取自 §4 且为 F² 的导数，因子二不能丢。
原一步的 jet 相位 e^(2πikrθ_T) 在 §7 统一写出，不在两种端点各重证一次；原光滑下界观测也统一放 §7。

自然转场：所有局部积分已有可求和界，最后在原完整曲面上进行一次统一分割和原步数还原。

### §7. Global asymptotics and sharpness

目的：关闭从局部引理到同一完整主定理的全部交换次序、圆重数、奇偶与最优性责任。

1. **The global Fourier formula.** 按 [G] §3 从 Π𝖴=𝖴Π 得 C_{2m+r}(f,g)=C_{2m}(f_r,g)，并由 F 的原光滑性在固定紧能窗控制 ||f_r||_{C^a}≤C_a||f||_{C^a}。逐圆 Parseval、层内和能量上两次 Cauchy–Schwarz 给绝对可积全模主控，再用 Tonelli/Fubini 写统一积分。一次 Fubini 不能自动许可后续导数/渐近交换，后者分别引用 §§5–6 的实际可求和界。
2. **Uniform stationary phase on regular tubes.** 按 [G] §5 给需要的一维 C_c⁴ 标量驻相及余项：Morse 坐标的 Jacobian 给 1/√|σ″|，高斯 Fourier 恒等式与四阶振幅控制给 (m|k|)^(−3/2)。正文保留这段短直接证明和当前全 k 振幅代入，不长抄一般多维驻相理论；如果使用标准定理作为补充来源，先核准确出处。非驻圆紧管用 §§5 的同一转置积分公式，不重推机制。
3. **One invariant partition of the complete surface.** 按 [G] §6：saddle 截断覆盖所有退化完整圆；acnode 小盘与持续紧圆取分离邻域，各 cutoff 在整圆常值，并在正则侧合成原能带权重。持续圆管跨 h₋ 完整保留；T=3/16 只作一次双侧驻相。其余有限紧圆管按驻/非驻分割，权重在振幅只乘一次；上圆只须被 G_T 保持，不额外要求每个局部权重被 F_T 保持。proper 饱和紧性排除新的空间无穷端，terminal 仍是正则图。取 saddle/非驻 N=3 归并余项：普通参数椭圆 m^(−2) 被 O(m^(−3/2)) 吸收，T=1 因无驻圆而显为全局主项。
4. **The original even and odd coefficients.** 按 [G] §7：下/中/持续圆 f̂_{r,c,k}=e^(2πikrρ)f̂_{c,k}；中心 A_k^(r)=e^(2πikrθ_T)A_k^(0)。上侧选 z₁=F_Tz₀，证明 F_Tz₁=z₀(θ+σ)。将偶振幅 L(f̂₀overline(ĝ₀)+f̂₁overline(ĝ₁)) 和奇振幅 L(f̂₁overline(ĝ₀)+e^(2πikσ)f̂₀overline(ĝ₁)) 完整写出，给主项中的具体代入。单圆支撑可使奇数相关恒零，所以不能要求所有步数正下界。由酉性给 C_{−n}(f,g)=overline(C_n(g,f))。
5. **Sharpness in the original class.** 按 [G] §8、[E] §9：T≠1 用分离紧正则驻圆管上的 χ(h)e^(2πiθ)，也覆盖 T=3/16 的持续圆；它在原 U_T 光滑，包括 terminal，并得偶列归一化模趋正。实部的余弦序列用相邻商矛盾证明正 limsup。T=1 用原 Morse 图的径向 bump 乘 p+iq，而不是任意指定中心单模；A₁=2L₀、A₋₁=0，实 p 亦有正 limsup。一般 jet 对在 A₁、A₋₁ 不同时零时，用两个不同单位频率的平方模 Cesàro 平均证明正 limsup，再说明该非消失集合开稠密。这里 Cesàro 仅是验证振荡主项不消失的辅助步骤，最终相关仍未经时间平均。

段末明确主定理各行与全部余项已经闭合。不得把空间薄层尖锐性当成长时间下界，或把合法存在观测扩大成每对观测必达最慢率。

### §8. Conclusion

目的：用约一短段重述完整原相关定理的区别性结论，不再重复长表或全部系数。
强调原不变分量已显式投影、T=1 无有限驻圆而由中心 jets 决定率、T=3/16 有同能双来源、原奇偶保持。
紧接适用边界：不涉及未投影混合、单圆混合、CLT、参数阈值的一致常数或全部高阶 jet 分类；不扩展为另一系统族的 future-work 主线。

## 6. 必要证明落点总账与明确不消费项

此表用于写完英文稿后的实际转录核对；不是用大纲检查代替完整证明审查。

| 责任 | 必须在正文实际出现的位置 | 不允许的替代 |
|---|---|---|
| 原完整 U_T、proper 有限基与真实 +P | §2.1 的 P30 精确接口＋GEO 实曲线延拓/弦切证明 | 只给 torus 两分式；将旧 p>3 结果外推实数 |
| 两实临界值、节点类型、2/1/2 圆与四 terminal | §2.2 的消元/根型/统一 chart 表，§5.1 与 §6.1 所需原 Hessian/方向 | 删除 terminal、将仿射弧当完整圆、只列数值根 |
| 正 coarea、Π 与 Koopman 对易、原范数 | §2.3；§5.2 另证明实际非 Hölder 损失 | 假设中心化仍原光滑，或改用整纤维均值 |
| PF G0/G1/G2、Q_PF(O)、移动端点和 j=2 | §3 全部三个子节 | 一行引内部笔记；省 f_h(P)；漏真实二倍 forcing |
| 持续圆锚、有限端点与 h=9/8 解析性 | §4.1–4.2 | 只有 J′ 符号而无积分常数；删除表观奇点 |
| C¹ 无穷常数及全部严格驻圆分类 | §4.3–4.4 | 对裸余项求导；T=1 因除 log T 丢失；仅“至多一个” |
| 原 F² 解析时间和上下穿箱次数 | §5.1 | 另造常数时间摆流；每个象限任选有利提升 |
| 全圆混合导数、移动入口和全部接缝 | §5.3 | 仅箱内或固定模估计；微分移动特征函数 |
| 倒相位符号、反复积分的真实边界及全模 | §5.4 | 声称迭代振幅自身趋零；用 δ(m) 薄层猜测 |
| 正向椭圆角、真实 ε 光滑 jets、带权范数 | §6.1–6.2 | 任意角 gauge；形式偶性而无下降范数；只留 ±1 模 |
| 两种端点的准确常数与余项 | §6.3–6.4 | 漏 β/γ 中的倍数，错负号，使用不收敛裸积分 |
| 全局可交换次序、驻相余项、完整分割 | §7.1–7.3 | 每模估计冒充全模；持续圆双计或删去 |
| 原奇偶、负时、原观测下界与 generic 限定 | §7.4–7.5 | 两圆当同圆单步；逐时刻下界；全高阶 jets 无证推广 |
| 原 C²⁰ 全局界与 C^(N+2) 局部界 | §2.4 声明；§§5–7 每块记录有限阶成本并在 §7.3 汇合 | 用无限光滑 seminorm 隐藏成本；固定 C²⁰ 控制所有 N |

不消费、不加入正文的旧内容：一般 r 法丛/谱 Jacobian/算术临界理想；正特征 Hasse 和节点厚度；旧 Q/Z 源桥全文；七值域表与极大值积分求值；全有理角周期表；空间薄层精确面积常数及其 n=0 尖锐性；任何目标零点、拟合或枚举产物。
其中已接受旧数学和旧 FAIL/STOP 记录全部保留，但记录本身不进入正文成为技术结论或篇幅。
对 [N] 的全量阅读不等于必须把其全部辅助推论发表：保留 [G] 实际消费的周期、原时间、范数/投影正则边界，未消费空间尾不增设为新的科学要求。

## 7. 表格、图和引用脚手架

### 7.1 最小视觉配置

| ID | 位置与内容 | 来源与用途 |
|---|---|---|
| Table 1 | 引言前部的三行参数/衰减/来源表 | [G] (1.6) 与 [E] 端点；让读者在首屏识别 T=1 和 T=3/16 的实际差异，不用数值图 |
| Table 2 | §2 原四 terminal 合并表 | [GEO] Step 4＋[M] §2；同一映射、测度与能量的四重精确对应，避免重复文字 |
| Table 3 | §4 证明末尾的五行严格频率分类 | [TW] §2 及本稿 §§3–4 证明；统一转成主定理的驻圆集合，不附旧值域表 |

不安排 raster/hero 图，不生成图片，不安排无数据的实验图。来源比较用机制分组文字即可，不额外制造泛泛的理论比较表。
三张表均由准确数学输入人工转录为正文表格，其 caption 必须区分回返 F_T 与 F_T²、持续圆与消失圆；不是观测或拟合证据。

### 7.2 已核来源绑定；不从记忆生成 BibTeX

下列是从[正式共同清单][MANIFEST]、[准入处置][ADMISSION]和已冻结[引用记录][CITATIONS]绑定的来源脚手架，不宣称本大纲作者本轮重新读了这些外文全文。
六项正式元数据已按引用记录核定；未来仅在实际正文消费和版本定位落实后冻结 BibTeX。FHR/MRVB 可用已核正式期刊书目，但具体定理比较仍标明已读 arXiv 版本，不能声称已核 VOR 正文一致。已拒绝正文不重试、不镜像绕取，固定 arXiv 版本不可静默替换成别版。

| 绑定来源 | 拟消费位置和准确关系 | 已核范围与不可扩大处 |
|---|---|---|
| Faou–Horsin–Rousset，*On Linear Damping Around Inhomogeneous Stationary States of the Vlasov-HMF Model*，[2105.02484v1](https://arxiv.org/pdf/2105.02484v1) | §1 最强近先例；§5 可注明相近节点/Fourier 技术，§6 可注明原中心 jets 的先例。明确扣除跨 separatrix、原光滑、全模和任意有限幂节点机制 | 固定 v1，PDF 1–6、25–32、34–40；非整篇 42 页，Lemma 7.15 证明未在共同范围。不说“首次跨节点” |
| Moreno–Rioseco–Van Den Bosch，正式题名 *Mixing in anharmonic potential well*；arXiv 题名保留 *Mixing in an anharmonic potential well*，[2201.07019v2](https://arxiv.org/pdf/2201.07019v2) | §1 频率非退化/有限驻点的框架定位；§7 的驻相本身不是新机制 | 固定 v2，PDF 1–4，Th1.1–1.3 声明；Th1.2 为 C¹ 的 t^(−1/3)，不误引成 sharp t^(−1/2)。正式书目为 JMP 63(7), 071502 (2022)，071502 是文章号 |
| Hadžić–Rein–Schrecker–Straub，*Quantitative phase mixing for Hamiltonians with trapping*，[2405.17153v2](https://arxiv.org/pdf/2405.17153v2) | §1、§6 原中心观测的 Fourier 消失阶与 trapping 定位 | 固定 v2，PDF 1–8、11–17，含 Lemma2.1 完整证明；不把单调周期/宏观核主定理写成本题任意双相关和 saddle 定理 |
| Liu–Zhang–Li，*The LLN and CLT for the statistical ensembles of discrete integrable Hamiltonian systems*，[2509.20690v1](https://arxiv.org/html/2509.20690v1) | §1 确定性离散统计对象的差别；需要时 §8 说明本文不宣称 CLT | 固定 v1，原对象、非共振及 Th3.1 声明/完整证明；Cesàro LLN 不是未平均相关，后文随机 CLT 不消费，出版社既有 403 保留 |
| Liu，*Weak Convergence to Equilibrium for Statistical Ensembles in Discrete Integrable Hamiltonian Systems with Markov Perturbations*，[官方 DOI 页面](https://link.springer.com/article/10.1007/s44198-026-00424-7) | §1 说明依赖 Markov 扰动的机制不同 | 官方摘要/完整 Conclusion/日期：Published 2026-05-18，VOR 2026-07-10；未核中间证明，不去随机化后保留指数阻尼 |
| P30，*Vertical critical ideals and cyclotomic first jets of q-Painlevé I*，2026，匿名 accepted local manuscript | §1 归属、§2.1 原曲面/完整 finite-fibre 接口；真实标为未发表本地稿件 | [P30 §2][P30S02]、[P30 finite-critical lemma][P30S03] 的约定输入；引用记录已核 `paper/v4/` 与 2026-09-09 本地接受，不捏造期刊、DOI 或公开 URL |
| 标准解析 Morse、coarea、实椭圆群、光滑射影延拓和驻相 | §2、§5、§6、§7 的标准背景；本题所需符号、端点、余项仍实际证明 | 如确需具名文献，准确书目/定理位置标为 `[VERIFY]` 后交 citation 核验；不从记忆编 BibTeX，不以未核书目代替必要证明 |

不扩大查新阶段。旧 CD 的 7.6/8.2/MID/STOP 定位建议、旧 twist 7.2 双 FAIL 及缺读边界不删除、不重评分；正文如实反映其最强来源压力，但不插入内部评分账。

## 8. 作者自检、独立接续与读取范围

本件使用 paper-plan 的单一叙事、主张—证据矩阵和章节责任方法；按项目合同不执行其默认 ICLR 页数、实验结构、强制 hero 图或附录移证建议。
技能的外部 outline review 不在本作者任务中模拟：本件未再委派、未自授 outline scope PASS；root 将对实际新大纲/锁作一次独立有界忠实性核对，而不是重开未变科学门。

写作接续：

1. root 对本作者大纲与已冻结 source/publication locks 作独立有界一致性核对；仅修真实冲突，不把编辑预算升级成科学门，也不把 `criteria_binding_unavailable` 当阻断。
2. 按上述准确 8 个编号 section 文件与单独 abstract 写完整英文稿；保留所有必要证明，不先建短稿试排测容量。先写逻辑依赖 §§2–7，再收束 Abstract/Introduction/Conclusion，但最终阅读顺序按本计划。
3. 全稿完整后实际检查符号、证明转录、引文和来源身份；原字节齐备后由主控按协议冻结，进入确定性构建、真实页数及 PDF 验收。
4. 只针对实际变更及新出现风险作独立 actual 稿件/PDF 审查。准入 PASS、作者大纲、运行成功和 PDF 完成仍是不同状态；P31 成品与批次第五篇未完成前不报交付。

本大纲作者本轮实际 FULL 读取：paper-plan/SKILL.md、shared-references/writing-principles.md；[ADMISSION] 126 行、[BRIEF] 160 行、[MANIFEST] 178 行、[OMAP] 265 行；[G] 358 行、[M] 128 行、[N] 238 行、[K] 292 行、[E] 377 行；[GEO] 208 行、[B] 144 行；本项目 README。
封稿前另 FULL 读 root 冻结 [SOURCELOCK] 104 行、[PUBLOCK] 72 行、[CITATIONS] 142 行并对齐本计划；未重新检索引文或修改两锁。
实际定向 PARTIAL： [PF] 1–165（只消费 Claim 与 Steps 1–2）；[MID] 28–115；[UP] 20–112；[INF] 1–205；[TW] 25–133；[R1] 176–198 与 [R2] 217–239 的容量章。未把定向范围标作全文，也未重读 38 祖先或外文全文。
正文责任来自亲读原证明和 OMAP 定位；容量章节只用于理解原独立风险，不拼其最好预算，不冒领其评分。
唯一新增/编辑文件为本件；无其它项目文件、锁、原证明或已接受产物改动。交付前全文读回，行数/bytes/SHA 另由交付消息绑定；不在正文内写自引用 SHA。

[ADMISSION]: ../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md
[SOURCELOCK]: notes/SOURCE_SCOPE_LOCK_V1_20260913.md
[PUBLOCK]: notes/PUBLICATION_LOCK_V1_20260913.md
[CITATIONS]: notes/CITATION_RECORDS_V1_20260913.md
[BRIEF]: ../../docs/research-batch07/PAPER31_QPI_Q2_COMPLETE_CANDIDATE_BRIEF_V1_20260913.md
[MANIFEST]: ../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_REVIEW_INPUT_MANIFEST_V1_20260913.md
[OMAP]: ../../docs/research-batch07/PAPER31_QPI_REAL_GLOBAL_TWIST_CURRENT_PROOF_MAP_V1_20260912.md
[M]: ../../docs/research-batch07/PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: ../../docs/research-batch07/PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[K]: ../../docs/research-batch07/PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: ../../docs/research-batch07/PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[G]: ../../docs/research-batch07/PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md
[GEO]: ../../docs/research-batch07/PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[PF]: ../../docs/research-batch07/PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[B]: ../../docs/research-batch07/PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[MID]: ../../docs/research-batch07/PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
[UP]: ../../docs/research-batch07/PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md
[INF]: ../../docs/research-batch07/PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md
[TW]: ../../docs/research-batch07/PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[R1]: ../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_REVIEW_R1_V1_20260913.md
[R2]: ../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_REVIEW_R2_V1_20260913.md
[P30S02]: ../30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[P30S03]: ../30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
