# Paper30：新离散辛映射问题的动力／几何有界筛选

日期：2026-09-07。状态：`BOUNDED_SCREEN_COMPLETE_TWO_OPEN_LEADS`。
本文件是问题生成与定点查新，不是候选评分、证明接收或成稿许可。
Batch07 仍为 3/5；Paper30 未立项。22–30 页实质正文原约束不变，
本报告不预测页数、不打四门分数，也不以旧结果追加短推论。
Route applicability: `NOT_APPLICABLE`。

## 1. 结论和证据边界

生成九个具体问题，只对问题 1、2 使用共十二条外部搜索查询。
较值得进入一个新、有界作者证明的是问题 1 的**同局部 Floquet 数据、
不同高阶势函数项的共振缺陷稳定性**。问题 2 仍是实际数学 `OPEN`，
但末轮命中尚未全文核定的广义 standard-map Lindstedt 系列先例，
因此其文献非覆盖义务也未关闭。其余七题记录第一失败关口及最强旧覆盖，
没有扩展查新，不授予新意结论。

这里 `OPEN` 只表示精确定义的问题尚未由本轮论证解决，
不表示世界上已公认的开放问题，也不表示检索未命中就是原创。
“已有工具的直接应用”“有真实剩余义务”和“可以立即作为正式论文”是三件事。

本轮亲自读取了 `AGENTS.md`、`docs/WORKFLOW.md`、`README.md`、
`BATCH_07_CONTEXT.md`、`PAPER30_DISCOVERY_STATE_20260906.md` 的前 115 行、
以及 `PAPER30_TORUS_TWO_SCALE_CANDIDATE_DISPOSITION_20260907.md`。
本地 PDF 相关性筛选只阅读 Paper20 接受版本的前三页：其贡献是次数矩阵，
并不包括本文问题 1 的实稳定性结论；没有重审其证明或扫描旧构建。
没有独立 `literature/` 文献库，未下载论文。

使用了 `idea-creator` 和 `research-lit` 技能；最新有界任务覆盖技能模板的
全方向逐题多轮检索、默认 GPU pilot、根目录报告等步骤。
理论任务无需数值 pilot；本轮没有数值、GPU、实验或正式论文。
可调用工具列表没有 GPT-5.4 Codex MCP、Zotero 或 Obsidian 接口，
也未找到技能所述 `arxiv_fetch.py`，所以实际为本 secondary 研究代理生成问题、
公开网页与 arXiv 定点核对。未运行 GPT-5.4、未伪称跨模型或人类评审，
本文件不构成双盲独立候选评价。

以下方向全部排除：量子周期迹、几何周期点检测、形式 Hamiltonian gauge、
作用量逆谱、同随机 Hénon 词的多点混合、正弦 cat 的两级 Ruelle 共振、
已占据的 degree/Newton/selector 和 Paper29 多项式上同调。
主控另做代数／算术端筛选，本文件不重复该端工作。

## 2. 九个具体问题

### 1. 等局部 Floquet 数据的共振局域周期轨道：高阶势项能否决定耦合失稳？

**对象与量词。** 在长度为 N 的有限路径图上，L 为正图 Laplacian，取

\[
 p'=p-f_\kappa(q)-\epsilon Lq,\qquad q'=q+p',
 \quad q,p\in\mathbb R^N,
\]

其中 f 逐坐标作用，且

\[
 f_\kappa(x)=x+\frac{5x^2+155x^3-5x^4-83x^5}{24}
       +\kappa x^2(x^2-1)^2.
\]

这是势函数梯度 kick 与自由 drift 的真实全局辛多项式映射。
对每个 N≥2，在端点放置二周期 (q,p)=(1,2)↔(−1,−2)，
其余坐标置于固定点 0。问题不是该周期能否由隐函数定理继续，而是：
能否从完整一阶 N 维共振约化给出可核对的稳定／失稳区间，
说明固定局部 Floquet 数据时，κ 如何控制耦合后的谱类型？
第一阶段只要求有限链；任何 ε_N 与 N 无关的 ε_0 必须分别证明。
长链极限与全相图不作为即刻义务。

**已核对的输入代数，不是耦合定理。** 对所有 κ，

\[
 f(0)=0,\quad f'(0)=1,\quad f(\pm1)=\pm4,
 \quad f'(1)=8/3,\quad f'(-1)=7/2.
\]

例如原五次项的导数是
\(1+(10x+465x^2-20x^3-415x^4)/24\)，在 −1 的值是
\(1+60/24=7/2\)。若
\(M(c)=\left(\begin{smallmatrix}1-c&1\\-c&1\end{smallmatrix}\right)\)，
则背景与缺陷的两步矩阵分别为

\[
 P_0=M(1)^2=\begin{pmatrix}-1&1\\-1&0\end{pmatrix},\qquad
 P_*=M(7/2)M(8/3)
 =\begin{pmatrix}3/2&-3/2\\19/6&-5/2\end{pmatrix}.
\]

二者 trace=−1、det=1，特征值均为 \(e^{\pm2\pi i/3}\)。
上右元素异号说明对应同一上半圆特征值的 Krein 符号相反
（整体符号取决于约定，二者相反不依赖约定）。
κ 项在三个取值点上的函数值与一阶导数均为零，
而改变二阶导数，故这确是先验等 jet 参数族，不是事后改动局部谱目标。

**第一可失败证明关口。** 必须把周期轨道自身随 ε 的位移计入 monodromy；
不能只往冻结轨道 Hessian 加 εL。计算 λ_0=e^{2πi/3} 的完整简并约化，
检查跨缺陷边的符号、背景项和二阶 jet 的真实进入方式。
相反 Krein 符号只准许失稳，不保证给定耦合会产生四重组。
原 κ=0 多项式可能迅速失谐离开背景带，这一可能性不能删除。

**最强可能旧覆盖。** 反连续极限加隐函数定理覆盖周期继续；
MacKay–Sepulchre 的网络稳定性和 Aubry band 方法覆盖大量非共振／定号情况；
Howard–MacKay 及一般 Krein 理论覆盖“冲突是失稳必要机制”。
因此存在性、一般 Krein 图示、有限维特征多项式本身不能计作核心新贡献。
剩余目标必须是指定真映射的完整有效耦合矩阵与可证明谱结论。

**意义、可行性与风险。** 这能区分“未耦合周期谱相同”与“耦合响应相同”，
指出仅凭局部 Floquet 数据预测网络稳定性的不足。
有限周期和近邻图让第一次失败检查可由精确矩阵计算完成；
主要风险是约化后完全落入现成缺陷 Jacobi 矩阵分类，或所选区间只有稳定保护。
状态：`OPEN`，优先有界作者 probe，未证明、未立项。

### 2. 双谐波 twist map 的全分母共振消失集合

**对象与量词。** 在 \(\mathbb T\times\mathbb R\) 取

\[
 p'=p-V'_{\epsilon,\lambda}(q),\quad q'=q+p',\qquad
 V_{\epsilon,\lambda}(q)=\epsilon\cos q+\lambda\epsilon^2\cos2q.
\]

对每个互素 0<r<s、s≥3，写
\(q_j=\theta+2\pi rj/s+u_j\)、\(\sum_j u_j=0\)，
在 s 周期离散作用量中消去零均值变量，得约化势 \(W_{r,s}(\theta)\)。
问题是确定首个可能共振系数

\[
 W_{r,s}=\text{常数}+\epsilon^s C_{r,s}(\lambda)\cos(s\theta)
             +O(\epsilon^{s+1}),
\]

的真实消失集合：给出对所有 r,s 有效的递推／结构描述，
判定实零点及其重数，并在简单零点确定下一真实分裂阶。
“全部实根是否简单／是否存在统一实根结构”本身须接受反例，
不预设根数或符号。这里 s 是轨道分母，不是直接 forcing mode 编号。

**第一可失败证明关口。** 先严格定义约化和相位规范，证明到 ε^s−1
确无非恒定相位项；明确 C 的度数和余项量词只对固定 s，
不能把分母相关小除数界写成 s 一致。
随后用少数精确小分母检查所谓统一根结构；若很早反例出现，
必须停止该结构猜想，而不是仅罗列系数。

**最强可能旧覆盖。** Lyapunov–Schmidt、Poincaré–Birkhoff 和共振正规形
覆盖约化框架和非退化分支；单正弦的分母阶缩放亦有旧先例。
Berretti–Gentile 的广义 standard-map Lindstedt 系列可能已覆盖关键组合递推。
2024–2025 双谐波 map 文献直接覆盖模型和多种 fixed-point/island 分岔。
不能把 mode competition、首个 Fourier 消失或少量低周期系数宣称为新机制。

**意义、可行性与风险。** 目标是解释预先调谐的第二谐波何时真正抑制
给定有理旋转共振，及抵消后哪种周期几何接替。
与作用量逆谱不同，此处不从谱重构参数；与旧局部共振判别式不同，
对象是所有有理旋转分母的完整离散周期约化。
风险为经典 Lindstedt/tree 展开已给完整答案，或剩余只是例行高阶代数。
状态：数学 `OPEN`，且 `LITERATURE_COLLISION_UNRESOLVED`；不先行推荐证明扩张。

### 3. 可逆 Duffing kick 的双脉冲连接：相互作用符号是否由对称性决定？

**对象与量词。** 取
\(p'=p+\mu q-q^3,\ q'=q+p'\)，固定一个已有横截同宿轨道的 μ>0，
对每个充分大间距 L，比较由同符号与异符号两个主脉冲拼接得到的
可逆对称同宿轨道。问 Lin matching 量的首项符号能否由脉冲符号与 L 的奇偶
完全决定，还是包含独立、可变号的全局同宿系数；明确给出后者时的边界。

**第一关口。** 先在实际离散同宿上确定主相互作用系数不为零；
不能拿 Smale horseshoe 的轨道存在代替 matching 符号，
也不能以形式连续 Duffing separatrix 代替真离散轨道。

**最强可能旧覆盖。** 可逆映射的对称截面、Smale–Birkhoff、Lin 方法和
离散多脉冲稳定性已有强框架；固定 μ、单个非退化脉冲的渐近拼接很可能直接适用。
此项没有追加检索，以上只是必须核对的覆盖对象。

**意义与风险。** 区分时间反演对称和真实连接符号，能够约束同宿分岔；
但若没有超出一般 Lin 系数的显式真映射信息，剩余只是框架应用。
状态：`DEPRIORITIZED_STRONG_FRAMEWORK_COVERAGE`，不即时展开。

### 4. 小 kick 下首次共轭点的有限时间测度律

**对象与量词。** 对
\(p'=p-\epsilon\sin q,\ q'=q+p'\) 在 2π 周期二维环面上的投影，
定义 τ_ε(z) 为离散作用量 Dirichlet Hessian 首次非正定的时间。
其三对角对角元是 \(2-\epsilon\cos q_j\)，邻对角元 −1。
问对每个适当连续点 c>0，归一面积 m 是否满足

\[
 \epsilon^{-1/2}m\{z:\tau_\epsilon(z)\le c\epsilon^{-1/2}\}
       \longrightarrow A(c),
\]

且 A 可由真 pendulum 极限的 Jacobi 方程明确给出；
可先检验 c≤π 的零响应与 c>π 的首次正响应，而不讨论无限时全局最小集。

**第一关口。** 局部缩放 p=√ε y 只控制有界 y；
必须排除远离主共振的初值在该时间窗贡献同阶测度。
仅做轨道 averaging 不能自动通过 Hessian 最小特征值的零交叉极限。

**最强可能旧覆盖。** 离散 Hopf／无共轭点刚性、定量非最小集合估计和
共振 averaging 的现成组合可能已覆盖该极限。未追加定点检索。

**意义与风险。** 将无限时间的变分非最小性变成可观测时间尺度；
关口清楚且真／假都有解释力。但新成分可能仅是标准缩放的测度版本。
状态：`OPEN_UNSCREENED`，备存而不扩张。

### 5. 双曲轨道管的 Gromov width 是否含有非线性耦合信息？

**对象与量词。** 在 R⁴ 取
\(p'=p+\operatorname{diag}(\mu_1,\mu_2)q-\nabla U_\eta(q)\)，
\(q'=q+p'\)，其中 μ₁>μ₂>0，
\(U_\eta=(q_1^4+q_2^4)/4+\eta q_1^2q_2^2\)。
令 Ω_n(δ) 是包含原点的双向 Bowen 管分支
\(\bigcap_{|j|\le n}F^{-j}B_\delta(0)\)。
问固定充分小 δ 时
\(\Lambda_1^{2n}c_G(\Omega_n(\delta))\) 是否收敛，
若收敛，其首个小 δ 修正能否检测 η；Λ₁ 是原点最大不稳定乘子。

**第一关口。** 线性长方体／椭球上下界只给指数候选，
不证明真实容量前因子收敛；必须同时给辛嵌入下界和不挤压上界。

**最强可能旧覆盖。** 线性辛容量公式、辛双曲正规形以及已有容量／熵估计
可能覆盖指数，而未必覆盖固定 δ 的非线性前因子。这里没有文献通过判断。

**意义与风险。** 若成立，是几何辛不变量而非代数次数看见耦合的例子。
但四维真实容量计算远难于轨道范数估计，很容易只有夹界没有结论。
状态：`HIGH_RISK_GEOMETRIC_RESERVE`；不把它替换为简单指数推论。

### 6. 标准 nontwist map 的真重联边界与形式能量相等是否一致？

**对象与量词。** 固定
\(p'=p-h\beta\sin q,\ q'=q+h(1-(p')^2)\)，h>0 小。
连续近似在 β=2/3 出现两个指定双曲固定点间的能量匹配。
问对所有充分小 h，两个指定可逆对称截面上的连接条件是否由单一
β(h) 控制，还是存在不可合并的真连接／切触边界。

**第一关口。** 必须区分形式 modified Hamiltonian 的能量相等与真实稳定／
不稳定流形相交；如果分裂是指数小量，任何固定阶 h 展开都不关闭问题。

**最强可能旧覆盖。** Nontwist 重联、离散 Melnikov 和指数小分裂已有强先例。
主控提示的 Suris 破裂及其首阶 turnstile 工作也禁止将一般低阶 splitting 当新意，
但本问题不等于 Suris 族，不把那一结果直接当此模型定理。

**意义与风险。** 能辨别所谓“能量重联判据”的科学边界；
然而第一关就可能需要非零 Stokes 常数与全局流形匹配。
状态：`STOP_TOO_DEEP_FOR_IMMEDIATE_PROBE`，不借著名全局难题撑题。

### 7. 固定三周期 accelerator mode 的精确最早出生阈值

**对象与量词。** 对圆柱提升
\(p'=p+K\sin q,\ q'=q+p'\)，只研究
\(F_K^3(q,p)=(q+2\pi m,p+2\pi)\) 的最小三周期轨道，
区分 m mod 3。对这三个有限类别确定最早出现椭圆 accelerator 周期支的
K 阈值与退化类型，排除较低周期伪解。

**第一关口。** 求和仅给 K≥2π/3，不能证明界可达；
必须同时满足三个相位一致条件和 Floquet 判据，
阈值若是非代数定义不能伪装成整系数消元。

**最强可能旧覆盖。** 低周期 accelerator-mode 分类、对称周期求解与
普通 saddle-center 分岔很可能直接覆盖。未展开检索。

**意义与风险。** 是精确 transport mechanism 的有界模型，
但很可能仅为旧周期方程的有限求解。
不将问题改成所有周期阈值的下确界、last invariant circle 或全局扩散。
状态：`DEPRIORITIZED_LOW_PERIOD_CLASSIFICATION`。

### 8. 图耦合 Hénon 在反积分区间的完整有界轨道编码

**对象与量词。** 对每个最大度数≤D 的有限图 G，取
\(F(q,p)=(p,a\mathbf1-q-p^{\circ2}-\epsilon L_Gp)\)。
因后半块关于 p 的导数对称，这是 R^{2N} 上的辛映射。
问能否给出与 N 无关的显式 a₀(ε,D)，使 a>a₀ 时完整双向有界轨道集
而非预选子集，与 2^N 字母满移位共轭；并判定所给阈值是否真有尖锐新内容。

**第一关口。** 收缩构造所有 ±√a 代码只给一个 horseshoe；
必须证明没有遗漏其他有界轨道。即使做到，也要扣除反积分极限的通用结论。

**最强可能旧覆盖。** Aubry 式反积分编码、统一锥条件，
以及 Paper20 前三页明确提到的四维 coupled-Hénon horseshoe 文献。
显式保守常数通常只是这些定理的定量化，不自动成为新研究问题。

**意义与风险。** 能把空间维度一致的完整动力学与局部编码区分开；
但最强旧覆盖太直接，追最优阈值又可能变成难控的全局切触问题。
状态：`DEPRIORITIZED_ANTI_INTEGRABLE_APPLICATION`。

### 9. 交叉正弦剪切第一次倍周期处的 Floer bar 配对

**对象与量词。** 在二维 2π 环面取 Hamiltonian 同伦于恒等的
\(p'=p+K\sin q,\ q'=q-K\sin p'\)，研究 K=2 附近的 F_K²。
问在非退化的两侧，指定原点倍周期所产生局部轨道的作用量差是否确实组成
完整全局 Floer barcode 中的同一有限 bar，并给出该 bar 的真实首项。
这不是从周期作用量反演 map 参数，也不是 cat map 的 Ruelle 谱。

**第一关口。** 局部正规形和作用量差不决定全局 Floer differential 的配对；
必须排除其他固定点／轨道对该局部链复形的干扰。

**最强可能旧覆盖。** 局部 Floer birth/death 模型、barcode stability 与
continuation 已有完整基础，单个 bar 的缩放很可能只是局部标准模型的应用。

**意义与风险。** 真正引入辛拓扑可见的信息，但会把当前 kick–drift 主线
扩展到另一 Hamiltonian 环面词和 Floer 工具链。
状态：`ROUND2_CLUE`，只记录，不展开跨系统族工作。

## 3. 两题的一手定点核对

### 3.1 共振缺陷：哪些现成、哪些还没有被这轮证据覆盖

| 一手来源 | 实际读到的范围 | 必须扣除／尚不能推出 |
| --- | --- | --- |
| R. S. MacKay, J.-A. Sepulchre, *Stability of discrete breathers*, Physica D 119 (1998), 148–162，doi:10.1016/S0167-2789(98)00073-6 | 出版社摘要；全文链接工具返回错误，没有越过访问限制 | 一般非同质网络、一般耦合、用辛 signature 给弱耦合 ℓ² 稳定性条件已经存在；未逐条核定本文相反 signature 精确共振是否落在其假设之外 |
| S. Aubry, *Breathers in nonlinear lattices: Existence, linear stability and quantization*, Physica D 103 (1997), 201–250，doi:10.1016/S0167-2789(96)00261-8 | 出版社摘要；全文打开失败 | 反连续极限编码、Floquet 与 Newton band 的联系已存在；不能把这套方法的名称或使用本身算新 |
| J. E. Howard, R. S. MacKay, *Linear stability of symplectic maps*, J. Math. Phys. 28 (1987), 1036–1051，doi:10.1063/1.527544 | 作者机构书目与 WRAP 出版记录；出版社 DOI 打开失败 | 一般线性辛稳定性框架是直接先例；全文未取得，故不声称已经排尽其所有专门定理 |

一手链接：[MacKay–Sepulchre 出版记录](https://www.sciencedirect.com/science/article/pii/S0167278998000736)，
[Aubry 出版记录](https://www.sciencedirect.com/science/article/pii/S0167278996002618)，
[Howard–MacKay 机构记录](https://wrap.warwick.ac.uk/id/eprint/25081/)。

本轮能够作出的窄结论是：非共振／定号稳定性和普通 breather 存在性不是新问题。
本文显式 f_κ 在 ε=0 具有相反 signature 的同角共振，这是实际输入代数。
“指定耦合后的约化矩阵及谱区间未由已读来源直接给出”只是有限证据下的剩余义务，
不能升级为已证明原创。连续时间 Klein–Gordon 的相关结果只用作最强覆盖线索；
不将本任务转成该系统的延伸论文，跨族用途为 `ROUND2_CLUE`。

### 3.2 双谐波：模型、固定点竞争和分母阶缩放均有强先例

| 一手来源 | 实际读到的范围 | 与精确问题的距离 |
| --- | --- | --- |
| M. Mugnaine 等，*Isochronous islands in the two-harmonic standard map*，2025，arXiv:2504.20177；期刊 doi:10.1140/epjs/s11734-025-01867-7 | arXiv 模型、引言、固定点/island transitions；作者机构期刊 PDF 的结论可见 | 两个 harmonic mode 的竞争、saddle-node/pitchfork 与中间 islands 都不是新；其正文明确主要研究 y=0 的 period-one fixed points，不能直接等同于本文所有 r/s 的 ε^s 系数根结构 |
| M. Mugnaine 等，*Dependence of isochronous bifurcations on the driving-mode phase shift in two-harmonic standard maps*，Phys. Rev. E 112 (2025), 034216；arXiv:2505.00179 | arXiv 引言、模型、参数范围和第 III 节；作者机构已出版 PDF 首页 | 相位打破、固定点稳定性、intermediate modes、secondary shearless curves 已研究；本文不靠加一个相位自称新模型 |
| W. Wenzel, O. Biham, C. Jayaprakash, *Periodic orbits in the dissipative standard map*, Phys. Rev. A 43 (1991), 6550 | APS 摘要 | 单正弦的有理分母阶缩放有数值及解析论证；原文也讨论 Hamiltonian 极限，不能把 ε^s 本身当原创。其一般 dissipative 结论不无条件移植到辛映射 |
| A. Berretti, G. Gentile, *Scaling properties for the radius of convergence of Lindstedt series: generalized standard maps*, J. Math. Pures Appl. 79 (2000), 691–713 | 末轮搜索命中的参考文献项；未取得／阅读全文 | 最强未关闭碰撞项：可能包含广义 Fourier 支撑、共振树与 leading-order cancellation 所需核心结构。未核定前不授予查新通过 |

一手链接：[2504.20177 原文](https://arxiv.org/html/2504.20177v1)，
[2505.00179 原文](https://arxiv.org/html/2505.00179v1)，
[PRE 已出版作者版本](https://fisica.ufpr.br/viana/artigos/2025/paper25.pdf)，
[Wenzel–Biham–Jayaprakash APS 页面](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.43.6550)。
Berretti–Gentile 项只作为准确标题的待核对先例，不把二手参考文献命中当一手定理证据。
arXiv HTML 的渲染日期与论文发表日期不混用；PRE 的发表年份以作者期刊 PDF 为准。

另外，主控提供的 2026 Suris 局部刚性及 1996 Suris 分裂线索作为排除边界，
本报告不另行扩检或复述为已亲读定理，也不围绕它们产生第三条文献路线。

## 4. 查询账单：恰十二条，之后只打开已命中一手页面

1. `coupled standard maps discrete breathers spectral stability MacKay Aubry`
2. `standard map subharmonic bifurcation two harmonic potential resonant cancellation periodic orbit normal form`
3. `"coupled maps" "breathers" "resonance" symplectic`
4. `"discrete breathers" "Hamiltonian-Hopf" finite size resonance stability`
5. `"standard map" "resonant" "two harmonics" perturbation periodic`
6. `"standard map" "Arnold tongues" leading order coefficient rational resonance`
7. `MacKay Sepulchre 1998 stability discrete breathers pdf symplectic maps`
8. `site.arxiv.org "breather" "symplectic maps"`
9. `site.arxiv.org "standard map" "resonant" "Lindstedt"`
10. `"two-harmonic standard" isochronous 2025 periodic bifurcation`
11. `Howard MacKay "Linear stability of symplectic maps" 1987`
12. `"standard map" "subharmonic" "bifurcation" "coefficient"`

未用百科、AI 摘要或自动评审网站支持科学判断；搜索偶然返回这些页面时未采用。
具体 arXiv 限域查询没有理想命中不构成无先例证据。
出版社全文访问错误保留为阅读限制，没有付费、代请求或外部发信。

## 5. 接续

问题 1 的有界入口是端点单缺陷二周期继续和完整一阶矩阵，
不是整条无限晶格理论、全部 κ 相图或“相反 Krein 必然失稳”的空泛断言。
本报告完成后，主控新增指令授权另写独立作者 probe：
`PAPER30_RESONANT_LATTICE_MATRIX_PROBE_20260907.md`。
该后续将先使用 `proof-writer` 技能，仍无候选评分、稿件或数值实验，
且必须另有独立数学审查；本筛选不能替代它。

问题 2 保留文献碰撞和证明义务，不与问题 1 拼装。
其余题只保存为本轮淘汰／储备记录，不借筛选报告本身贡献论文篇幅。
没有修改旧论文、冻结结果、原审查和状态锁；没有创建正式 Paper30 项目。

### 完成后的先例补充边界

作者有限链 probe 写作期间，主控另行报告了更强的已定位先例：
DPW 2015/2016 的 index-one Jacobi／半圆律模型直接覆盖约化矩阵与闭式根，
Aubry 1998 亦已有 isolated defect 与 opposite-Krein band 的无限体积失稳现象。
这些来源不是本代理十二条查询内新亲读的材料，具体来源核定由主控保存。
因此问题 1 不能仅凭“显式矩阵、闭式根或相反 Krein 机制”获得新意额度；
必须进一步核定实际等局部一阶 jet 辛映射族中的非线性、链长一致谱响应
是否超出这些先例。本文的相对优先次序不是候选立项结论。
