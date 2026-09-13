# Paper 30 文献预筛：几何周期检测、全局辛变形与 Weyl 周期迹

日期：2026-09-06（UTC）  
状态：有界一手文献 landscape；不是候选评分、正式立项、证明验收或 Route A/B 评价。  
范围：Paper 29 已接受稿之后、同一多项式离散辛映射族内的问题。本轮唯一新建文件为本报告。

## 1. 结论先行

值得继续数学预筛的是三个区别明确的问题：

1. 非线性 Weyl–Hénon 自同构的周期扭曲 Hochschild 商，能否与该映射自己的离散作用量 Brieskorn 模建立显式、全参数、包含退化周期点的同构，并保留足以做有限周期检测的结构？
2. Paper 29 的概形值检测如何、在什么额外条件及定量代价下，降到真正几何周期点的轨道和检测？逐点迭代重数有界不足以完成这一步。
3. 一阶标量 Hamiltonian 余边界已知之后，全局多项式辛共轭的高阶障碍、次数增长及形式可积性是否存在不能由逐阶套用旧结果短证的内容？

必须扣除的强先例：一般 tame Brieskorn 模的有限自由性/经典 Jacobian 纤维已有成熟理论；线性辛 Weyl 扭曲 Hochschild 计算已有明确结果；局部辛形式正常形与完整乘子谱刚性亦已有直接理论。未在本轮命中某个非线性桥接定理，只表示定向检索未命中，不表示世界新颖。

本轮使用 research-lit 的“先本地背景、再一手来源、区分实际阅读深度”流程。按限定范围没有另存论文 PDF、批量语料或外部记录，没有重开 Paper 29 已通过的阶段。

## 2. 本地边界与证据标签

已读 Paper 29 本地验收记录、接受稿引言与 8_symplectic_lift.tex；旧多项式余上同调查新只定向读取几何点、有限 Livšic 与 Bousch 段。沿用既有价值扣除，不将经典 Livšic 或已有局部函数算法重新包装为本次新发现。

- PROVED_PRIOR：原文明确陈述、且本轮读到相关段落的已有定理，不是本项目新证明。
- INFERENCE：根据原文假设与项目对象作出的适用性、量词或短推论判断。
- OPEN_NOT_ESTABLISHED：本轮没有建立、所列已读来源也未直接给出；不是对整个文献世界的开放性证明。
- NOT_SEARCHED：未覆盖的专门文献分支，不应据此作新颖性结论。

Paper 29 的一阶 Hamiltonian lift、标量多项式余边界和概形检测是本地已知输入。Weyl PBW 轨道基若仅复用其三角化，不足以支撑新的 22–30 实质页论文。C 因而转向真正的扭曲 Hochschild 商，而非改名后的同一个线性差分商。

## 3. 查询与时间覆盖

使用 Hénon/Henon 两种拼写；按命中转入作者页、出版社原文或 arXiv 正文。下表是实际执行查询的代表记录；搜索摘要不作为已读定理。

| 查询组 | 实际查询举例 | 作用/边界 |
|---|---|---|
| A 重数 | Hénon polynomial automorphism periodic point multiplicity uniformly bounded Shub Sullivan；"Hénon" "multiplicities" periodic points | 定位 Friedland–Milnor、Shub–Sullivan，辨别逐点与统一界。 |
| A 余边界 | "polynomial automorphism" "periodic" "coboundary"；"Hénon" "cohomological" polynomial | 未找到直接消除几何点值与概形值差距的一手定理。 |
| B 变形 | "symplectic maps" "formal" "deformations" "normal"；"area-preserving maps" "unique normal" | 命中局部正常形；不当作全局多项式辛共轭。 |
| B 谱 | "Multiplier rigidity for complex Hénon maps" | 定向核查 2026 Cantat–Dujardin，不重做旧完整谱查新。 |
| C 非交换 | "Weyl algebra" "Hénon" -Heiles -Hénon–Heiles；"Weyl algebra" "Henon" automorphism fixed | 排除 Hénon–Heiles 连续系统等假朋友。 |
| C 同调 | "Hochschild" "Weyl algebra" "arbitrary automorphism"；"twisted Hochschild" "nonlinear" symplectic；"Hochschild" "Hénon" | 核查线性扭曲理论的适用边界。 |
| C 作用量桥 | "twisted traces" "oscillatory"；"Weyl algebra" "generating function" "trace"；"Hochschild" "generating function" "symplectic"；"Hénon" "Brieskorn" | 未命中第 5 节具体非线性桥；不据此宣称首创。 |
| 2024–2026 | "Hénon" "formal" "symplectic" after:2024-01-01 before:2026-09-07；"Hénon" "periodic points" "multiplicity" "2025" | 新近结果核原始版本，不按网页抓取日期判断年份。 |
| 最近六个月 | "Hénon" "polynomial" "cohomological" after:2026-03-06 before:2026-09-07；"Weyl algebra" "automorphism" "fixed" after:2026-03-06 before:2026-09-07 | 窗口为 2026-03-06 至 2026-09-06。Cantat–Dujardin v1（2026-03-10）在窗口内；没有新增精确命中足以宣布本题新颖或已被完全覆盖。 |

## 4. 核心一手来源：11 篇

“正文相关节”不意味着全文精读。除明确标为摘要外，适用性判断基于定位阅读的原文。

| 文献、状态与来源 | Read level / 定位 | 直接覆盖：PROVED_PRIOR | 尚不能直接推出：INFERENCE |
|---|---|---|---|
| **A1** Shmuel Friedland, John Milnor, *Dynamical properties of plane polynomial automorphisms*, ETDS **9** (1989), 67–99。正式发表；[原文](https://deserti.perso.math.cnrs.fr/biblio/FriedlandMilnor_dynamicalpropertiesofplanepolynomialautomorphisms.pdf)。 | §3 Theorem 3.1；§8 Theorem 8.4、Corollary 8.6 与 Added in Proof。 | 约化 Hénon 复合固定点代数计数为次数，迭代为 \(D^n\)，计重数。Theorem 8.4 对 Jacobian \(\delta\ne1\) 且 \(\delta^n\ne1\) 给同一局部固定点重数保持。 | 计重数不等于约化；Theorem 8.4 不能直接用于辛情形 \(\delta=1\)。补注调用 Shub–Sullivan 仍是同一点迭代界，不是全周期点统一界。 |
| **A2** Michael Shub, Dennis Sullivan, *A remark on the Lefschetz fixed point formula for differentiable maps*, Topology **13** (1974), 189–191。正式发表；[作者机构原文](https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0015.pdf)。 | 全文 3 页；开头 Proposition 及证明。 | 给定 \(C^1\) 映射的给定固定点若对所有迭代均孤立，其局部指标随迭代有界；按导数中单位根的有限组合约化。 | 常数依赖给定映射芽/点，不能交换量词为对所有 \(n,x\) 的统一重数界，亦不直接控制整个多项式参数族。 |
| **A3** Katsunori Iwasaki, Takato Uehara, *Area-Preserving Surface Dynamics and S. Saito's Fixed Point Formula*, arXiv:0710.0706v1 (2007)。本轮使用作者预印本；[原文](https://arxiv.org/html/0710.0706v1)。 | §§1–2、§7，尤其 Theorems 2.1、7.5。 | 以 Saito 公式处理保面积曲面周期曲线，区分 type I/II；局部指标稳定性及孤立周期点增长。Theorem 7.5 是 Shub–Sullivan 型局部界。 | Theorem 2.1 的 type II 曲线条件不能删去；曲面计数不证明 Hénon 固定概形约化，也不消去幂零轨道和。 |
| **B1** Serge Cantat, Romain Dujardin, *Multiplier rigidity for complex Hénon maps*, arXiv:2603.09445v1 (2026-03-10)。预印本；[原文](https://arxiv.org/html/2603.09445v1)。 | 引言 Theorems A/B，参数空间与 §3 相关声明；重点 Theorem B。 | 固定 multidegree/multi-Jacobian 的 Hénon 复合中，完整迹谱给有限共轭歧义；文中亦有有限周期截断。 | 有限纤维不等于处处微分无核，也未将任意全局辛无穷小共轭积分成全阶、受控次数的多项式共轭。 |
| **B2** Vassili Gelfreich, Natalia Gelfreikh, *Unique normal forms for area preserving maps near a fixed point with neutral multipliers*, arXiv:0912.2922 (2009)；期刊 DOI 10.1134/S1560354710020164 (2010)。[原文](https://arxiv.org/html/0912.2922)。 | 主定理 Theorems 1–3 及正常形设定。 | 对中性乘子 \(+1/-1\) 的局部保面积映射族构造、简化并在相应非退化条件下唯一化形式正常形，给形式坐标不变量。 | 局部空间幂级数变换不等于全仿射平面上的多项式共轭，不提供逐参数阶的全局次数控制或全局周期多项式余边界判据。 |
| **C1** John Erik Fornæss, Brendan Weickert, *A quantized henon map*, DCDS **6** (2000), 723–740。正式发表；[出版社页面](https://www.aimsciences.org/article/doi/10.3934/dcds.2000.6.723)。 | 仅出版社摘要、书目信息；未读取正文。 | 已研究离散 Hénon 的量子化与 Hilbert 空间酉动力学，因此“首次量子 Hénon”不可主张。 | 摘要未给本题 Weyl 周期扭曲商—Brieskorn 同构或非约化周期纤维检测；未读正文仍待精查，不能视为已排除先例。 |
| **C2** Jacques Alev, Marco A. Farinati, Thierry Lambre, Andrea L. Solotar, *Homologie des invariants d'une algèbre de Weyl sous l'action d'un groupe fini*, J. Algebra **232** (2000), 564–577。正式发表；[作者机构原文](https://bibliotecadigital.exactas.uba.ar/download/paper/paper_00218693_v232_n2_p564_Alev.pdf)。 | 引言、Theorem 2.1 与 §5 扭曲系数计算相关部分；非全文证明核验。 | 经线性辛有限群与扭曲双模计算 Weyl 不变量代数的 Hochschild 同调/上同调，维数由群元素固定子空间数据决定。 | 非线性、无限阶、增加 Bernstein 次数的 Hénon 不满足其群作用假设；线性固定子空间公式不能直接套到非线性固定概形。 |
| **C3** Alexey A. Sharapov, Evgeny D. Skvortsov, *Hochschild cohomology of the Weyl algebra and Vasiliev's equations*, Lett. Math. Phys. (2017)，DOI 10.1007/s11005-017-0991-6；[期刊版作者原文](https://arxiv.org/html/1705.02958v2)。 | §4，特别 Theorem 4.1 及其线性辛 \(g\) 假设。 | Weyl Hochschild 复形的显式处理；线性、可对角化辛扭曲的非零上同调在 \(\mathrm{rank}(1-g)\) 次，相应类一维。 | 上同调不可不说明对偶性就改成任意扭曲 \(HH_0\)；其线性假设亦排除本题 Hénon 非线性迭代。 |
| **C4** Pavel Etingof, Douglas Stryker, *Short Star-Products for Filtered Quantizations, I*, SIGMA **16** (2020), 014；读取修订作者版 arXiv:1909.13588v6 (2021)。[原文](https://arxiv.org/html/1909.13588v6)。 | §§3.1–3.4；Lemma 3.1、Corollary 3.5、Example 3.9。 | 用 \(g\)-twisted traces / \(HH_0(A,Ag)^*\) 参数化相关结构；线性 Weyl 例在有特征值 1 时无扭曲迹，否则迹空间一维。 | 一般 twisted-trace 定义可用，但 short-star-product 与估计带保持过滤等前提；Hénon 不保持标准 Bernstein 过滤，不能由此得到周期维数及桥接同构。 |
| **C5** Antoine Douai, Claude Sabbah, *Gauss–Manin systems, Brieskorn lattices and Frobenius structures (I)*, Ann. Inst. Fourier **53** (2003)，DOI 10.5802/aif.1974。[正式原文](https://archive.numdam.org/item/10.5802/aif.1974.pdf)。 | §2.d Proposition 2.13；定向读 §4 Newton 过滤、Proposition 4.7 / Corollary 4.8。 | 在 tameness 等假设下 Brieskorn 格有限自由/局部自由，秩为 Milnor 数；零参数纤维为 Jacobian 商且特殊化受控；有 Newton 基理论。 | tame 作用量 Brieskorn 模平坦不可单列为新主定理；原文未直接识别非线性 Weyl–Hénon 的周期 \(HH_0\)，也不提供 Paper 29 支撑长度意义的单周期检测。 |
| **C6** Sergei Yakovenko, *Bounded decomposition in the Brieskorn lattice and Pfaffian Picard–Fuchs systems for Abelian integrals*, Bull. Sci. Math. **126** (2002), 535–554。[作者原文](https://www.wisdom.weizmann.ac.il/~yakov/ftpapers/log-poles.pdf)；[书目](https://arxiv.org/abs/math/0201114)。 | Theorems 1–2 与半拟齐次分解设定。 | 用有效 Brieskorn 分解除法构造 Picard–Fuchs 系统并控制多项式系数范数，覆盖半拟齐次 Hamiltonian 的代数约化。 | 除法算法与次数界本身已有强先例；新价值应来自 Hénon 周期结构或随周期统一的特殊估计，而非只把变量数换成轨道长度。 |

### 未作为核心证据的邻近命中

Guo–Zheglov 的 [arXiv:2203.13343v3](https://arxiv.org/html/2203.13343v3) Theorem 4.1 针对特定单项式型、非自同构 Weyl 端同态的固定元素，不是 Hénon 自同构直接结果。Belov–Kontsevich 的 [arXiv:math/0512169](https://arxiv.org/html/math/0512169) 中 tame 量子化、Weyl 导子内性是背景，不会自行形成新的量子共轭论文。仅作假朋友排除/价值扣除，不为凑数扩大核心表。

另查到 Weickert 2004 的 *Spectral properties and dynamics of quantized Henon maps* 书目信息（TAMS 356, 4951–4968），但未取得足以核验目标桥的一手正文，未将其视为已排除先例。选定 C 后应定向补读；没有取得正文不是新颖证据。

## 5. 精确覆盖边界

### A. 几何周期和与非约化固定概形

令 \(T_ng=\sum_{j=0}^{n-1}g\circ F^j\)、\(I_n=(F^n-\mathrm{id})\)。几何点值条件与概形条件分别为
\[
T_ng\in\sqrt{I_n},
\qquad
T_ng\in I_n.
\]
几何值只看到约化商，不能看到幂零部分。局部代数长度有限、或同一周期点在倍周期下重数有界，均不能直接将前一条件提升为后一条件，也不直接保留 Paper 29 的有限支撑长度阈值。这是依据 A1–A3 假设作出的量词判断（INFERENCE）。

同时进行的本地数学预筛已报告非约化有限周期假阳性机制；该机制不是“对所有周期均点值为零”的反例。本报告没有新增实验，也不把有限失败升级成全周期失败。必须区分固定映射的所有周期、固定次数族的所有参数、某一周期、预定有限点集。若仅加“选定周期概形约化”即可套用 Paper 29，通常是短推论；实质问题在退化参数的定量几何分离或真正全周期论证。

### B. 高阶全局辛共轭，而非一阶 lift 重述

Paper 29 已有标量 Hamiltonian 一阶余边界。B2 研究局部空间变量的无穷形式级数。与之不同，B 候选只有研究
\[
F_\varepsilon=C_\varepsilon^{-1}\circ F\circ C_\varepsilon,
\qquad
C_\varepsilon=\mathrm{id}+\varepsilon V_1+\varepsilon^2V_2+\cdots
\]
的全局多项式多阶兼容、非线性障碍、次数增长或可积性，才有清楚增量。“形式参数级数且每个系数多项式”既不等于有限次数多项式映射，也不等于解析收敛。

B1 的完整谱有限纤维不能排除特殊点分歧，故不能跳过高阶 obstruction。反过来，若只是每阶重新使用 Paper 29 线性判据，没有新的障碍结构或次数定理，也不足以独立长文。本轮未找到直接覆盖该受控全局问题的一手结果，但尚未确认新颖性。

### C. 真正的周期扭曲迹—作用量桥

令 \(\mathcal A_\hbar=\mathbb C[\hbar]\langle x,y\rangle/([x,y]-\hbar)\)，由原 Hénon 剪切/交换字诱导自同构 \(\sigma\)。其周期对象是
\[
HH_0(\mathcal A_\hbar,(\mathcal A_\hbar)_{\sigma^n})
\simeq
\mathcal A_\hbar/
\operatorname{span}_{\mathbb C[\hbar]}\{ab-b\sigma^n(a)\}.
\]
另一双模约定可能产生逆扭曲，必须统一。这里是线性模商，不是双边理想商代数。

对 \(N\) 个微步的周期作用量
\[
S_N(z)=\sum_{i=0}^{N-1}P_i(z_i)-\sum_{i=0}^{N-1}z_iz_{i+1},
\quad P_i'=p_i,\quad z_N=z_0,
\]
自然的 Brieskorn 型模为
\[
Q_N=
\mathbb C[\hbar,z_0,\ldots,z_{N-1}]
\bigg/\sum_i
(\partial_iS_N-\hbar\partial_i)
\mathbb C[\hbar,z_0,\ldots,z_{N-1}].
\]
分母是微分算子像之和，仍为 \(\mathbb C[\hbar]\)-子模而非多项式理想。短周期 \(N=1,2\) 的重复边须实际求导，不可机械套用互异邻居证明。

若 \(d_i=\deg p_i\ge2\)，取 \(w_i=1/(d_i+1)\)。纯最高项 \(P_i\) 权重 1，耦合项权重至多 \(2/3<1\)，纯最高部分有孤立临界点。验证半拟齐次/tameness 后，C5–C6 构成 Brieskorn 侧有限自由性及经典 Jacobian 纤维的强标准适用链（INFERENCE），不能主打一般平坦性。复数域到一般基域的下降、参数底局部自由到全局自由仍须单独说明。

本地候选提出按轨道顺序的乘法
\[
\prod_i z_i^{e_i}\longmapsto
\left[\prod_i X_i^{e_i}\right]_{\sigma^n},
\]
由相邻 Weyl 换序及扭曲循环性处理边界，连接 \(Q_N\) 与周期 \(HH_0\)。它不是一句抽象“形式驻相”。C2–C4 未直接覆盖此非线性同构，C5–C6 不提供 Weyl/Hénon 识别。本报告不验收该候选：仍须证明良定义、满射之外的单射、边界/短周期、基环与特殊化兼容，再判断是否只是短代数引理。

## 6. 四个可继续预筛的缺口与停止条件

### G1. 非线性周期 Hochschild—Brieskorn 显式比较

- 问题：证明上述自然同构，最好延伸到可控制高次同调/退化参数的复形比较，并与周期旋转、迭代或经典纤维兼容。
- 最强 prior：C2–C4 线性扭曲计算、C5 Brieskorn 自由性、C1 量子 Hénon 历史。
- 门槛：新增必须是映射自身的非线性周期结构、明确兼容性或退化信息，不是既有 Brieskorn 定理改记号。
- 状态：OPEN_NOT_ESTABLISHED。具体桥查询未命中；Fourier-integral-kernel、D-module trace、deformation-quantization fixed-point 的完整文献链为 NOT_SEARCHED，选定后应专项精查。
- 停止条件：若同构及全部推论由标准核复合/积分分部短证，不能靠一般背景填满篇幅。

### G2. 量子有限周期检测与幂零信息

- 问题：不只算各周期迹空间维数，还要证明 Weyl 观测量的 \(\sigma-\mathrm{id}\) 余边界类如何被有限、显式周期扭曲迹分离，给支撑/过滤依赖并与经典概形检测比较。
- 最强 prior：C4 扭曲迹解释与 Paper 29；C5 平坦性不能保证检测图交换或统一阈值。
- 门槛：定义观测量送入周期商的正确映射及其核，不能混同 \(HH_0(\mathcal A,\mathcal A_{\sigma^n})\) 与 \(\mathcal A/(\sigma-\mathrm{id})\mathcal A\)。
- 状态：OPEN_NOT_ESTABLISHED；这是 G1 后的真实数学风险，尚未查新/证明验收。
- 停止条件：若只是 \(\hbar\)-进逐阶套用 Paper 29，没有非形式或统一控制增量，应判短推论。

### G3. 退化周期几何检测：统一重数或替代机制

- 问题：在明确固定的辛 Hénon 族中，给足以从几何周期和恢复概形信息的估计，或绕过幂零结构证明真正全周期几何 Livšic。
- 最强 prior：A1–A3 与本地旧 Bousch/Livšic 查新。
- 门槛：不得把“对每个 \(x\) 存在 \(C_x\)”改成“存在 \(C\) 对所有 \(x,n\)”；点值零不天然控制 jets。
- 状态：OPEN_NOT_ESTABLISHED。没有证明所需统一界，也未找到给出该界的直接原始定理。
- 停止条件：有限阈值有非约化假阳性就应修正对象，不隐藏失败；只加约化假设后套 Paper 29 不单独立长文。

### G4. 全局多项式辛共轭的高阶障碍与次数代价

- 问题：明确二阶以上障碍、不变量性质及全局多项式次数控制，区分形式存在、逐阶多项式性与收敛。
- 最强 prior：B2 局部正常形、B1 完整谱刚性、Paper 29 一阶 lift。
- 门槛：需要不能被简单递归重述的结构定理或反例；始终属于当前离散辛映射，不另起独立算子族。
- 状态：OPEN_NOT_ESTABLISHED。若产生固定全局变形复形，应再查该复形；一般变形理论全景本轮 NOT_SEARCHED。
- 停止条件：只有 Hamiltonian 导子内性、一阶可解性或局部 Birkhoff/Takens 正常形时停止。

## 7. 使用限制

本报告支持继续严格数学预筛，不等于已选定 Paper 30。C 的具体非线性桥与有限检测有最清楚的对象差异；A 有实质量词缺口；B 必须越过一阶 lift。没有评分，也没有声称任何方向已能达到篇幅要求。

11 篇核心文献中 C1 仅读摘要，其余为注明的正文相关节，A2 全文。未用网页抓取日期冒充论文日期；近六个月以版本日期核验。引用链未穷尽，尤其一般量子化迹公式尚未专项精查。本报告适合排除明显重复、确定下一步精确命题，不可直接写成论文的“首次”“已穷尽文献”或正式新颖性结论。

收口时的本地状态更新：根任务已完成并封存 [量子周期迹作者证明探针](PAPER30_QUANTUM_PERIOD_TRACE_PROBE_20260906.md)，报告其中已给出内部消元、端点相对 Weyl–Koszul 比较、完整同调及精确有限量子检测的证明链。此为作者证明状态，不由本 landscape 验收；仍须结合独立数学检查与专门新意评价。上文“尚须证明/未建立”记录本轮文献预筛所负责的证据边界，不否定该并行新稿，也不因其出现重新开启全部查新。
