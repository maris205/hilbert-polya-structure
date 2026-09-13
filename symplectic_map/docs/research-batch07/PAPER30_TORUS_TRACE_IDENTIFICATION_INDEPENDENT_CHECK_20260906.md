# Paper30 环面：加权空间、固定点迹与 Ruelle 谱识别的独立核查

输入日期：2026-09-06。实际核查日期：2026-09-07。
性质：独立、有界、纯证明核查；仅新增本文件。

## Claim

核查作者文件
[参数加权空间的固定点迹与真实 Ruelle 谱识别](PAPER30_TORUS_WEIGHTED_TRACE_IDENTIFICATION_20260906.md)
的完整定理，而非只核其形式 Fourier 计算：对
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
F_\kappa=A\circ S_\kappa,\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad t=\pi\kappa,
$$
在充分小的每个非零实 $t$ 下，作者的 $H_t$ 确实承载实际拉回的迹类延拓
$C_t$，其每个正整数次幂满足固定点迹公式，且
$$
\det_{H_t}(I-zC_t)=\det(I-zR_t)
=(1-z)\det_{\ell^2(\mathbb Z^2\setminus\{0\})}(I-ztB(t))
\quad(z\in\mathbb C).
\tag{C1}
$$
这里 $R_t$ 是同一实映射、同一拉回方向的 Faure–Roy 迹类实现。
该等式须识别全部非零特征值及代数重数，并在进一步缩小的参数区间内证明
常数共振 $1$ 唯一且代数简单。它不包含复耦合参数、$t=0$ 的物理加权空间，
或两个实现之间的有界相似主张。

## Status

`PROVABLE AS STATED`。

在接受指定核性输入的前提下，作者原定理、公式、两侧实参数量词与结论边界全部成立。
未发现需要增加科学假设、削弱结论或改动作者文件的证明缺口。
下面补写的局部逆分支构造、周期点特征值估计及 Hilbert 空间认同，
均为原有假设的直接展开，不构成修订版定理。

## Inputs and Actual Review Method

- 作者输入共 $395$ 行，已分段全文读取并核对 SHA256：
  `ccdcb4bb0cd1ebaabfd65c6069cd47b1bcab7e94c2e524aa77c22dcdea209cd6`。
- 已接受核性输入为
  [重加权核性证明](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md)，
  SHA256：`c85dfa0ed29f1c6eb7d29d0898984bf9e2536da5ec89868c4582db9ea7381826`。
  本轮只核对其文件身份并使用给定定理，未重开该核性证明。
- 实际审查后端为独立协作代理直接数学核查，即 `secondary-agent fallback`。
  没有调用 GPT-5.4 MCP，没有将本报告标成该后端的运行结果。
- 本代理先独立核完完整证明；另有一个只读有界子任务核查作者第 $236$—$339$ 行的
  热极限与固定点换元，结果一致。该辅助核查未承担 FR 阅读或其余证明，未写文件。
- 使用 `proof-writer` 技能组织精确断言、依赖与证明边界；未做数值实验、
  参数拟合、候选评分、容量判断、稿件制作或外部写操作。
- 已完成的第二谱层代数核查报告未改动。

## Assumptions

只接受以下明示输入：

1. $B(t)$ 在固定 $\ell^2(\Lambda)$ 上按迹范数全纯，其中
   $\Lambda=\mathbb Z^2\setminus\{0\}$，半径 $r_0=1/256$；
   $|t|\le r_0$ 时 $\|B(t)\|_1<M$，$M=23041$，矩阵就是作者式 (6)。
2. FR 定理适用于足够小的实解析周期扰动，提供迹类实现及各幂固定点迹；
   其具体原文和本族适用性在第 1 步亲读核查，不以作者的转述作为唯一依据。
3. $t$ 固定为非零实数。涉及热极限时再固定任意 $n\ge1$，最后只令
   $\varepsilon\downarrow0$，不要求对 $t$ 或 $n$ 一致。

## Notation

沿用作者的
$$
E_m(x)=e^{2\pi i m\cdot x},\quad
m=(r,s),\quad \omega(m)=|s|-|r+s|,
$$
$$
\|h\|_{H_t}^2=\sum_m|h_m|^2|t|^{-2\omega(m)},\qquad
f_m=t^{\omega(m)}E_m.
\tag{N1}
$$
$H_t$ 首先是该加权序列范数的完备化，不预设所有元素是可逐点评价的函数。
$\mathcal E$ 表示在 $\mathbb C^2$ 上整解析、对 $\mathbb Z^2$ 周期的函数核心。
$U_t:\ell^2(\mathbb Z^2)\to H_t$ 是把标准基送到 $f_m$ 的酉同构。
$H_t^0$ 为零频率系数为零的闭子空间。
内积在第二变量线性；$\|\cdot\|_1$ 表示迹范数。

## Proof Strategy

逐一检查“实际拉回—全部实际迭代—热迹—固定点和—FR 幂迹—整个行列式”这条链。
通过 Fourier 系数的唯一性连接函数核心与加权完成空间；不尝试在两个空间上
直接使用未经证明有界的同一个对角变换。

## Dependency Map

1. 明确 FR 的实解析与小扰动条件，获得同一映射的 $R_t$。
2. 面积保持、完整 Fourier 核与正交归一基，给出块分解及迹类延拓。
3. 整解析核心的衰减、稠密性与复合不变性，识别全部实际迭代。
4. 自伴热收缩的强收敛，加有限秩逼近，推出右乘迹范数收敛。
5. 对角权重消去、Gaussian 核、Anosov 非退化性及全局补集控制，给出固定点迹。
6. 所有幂迹相等、迹类 Fredholm 行列式与整函数恒等定理，给出全部非零谱的重数。
7. 已接受的粗迹范数界独立排除零均值块中的额外特征值 $1$。

## Proof

### Step 1. 亲读 FR 原文与实际参数适用性

本轮实际读取了两份同一原始文献：

- [FR arXiv v2 原文](https://arxiv.org/pdf/nlin/0601010)：§2.2，预印本第 $8$—$11$ 页。
- [FR 印刷作者全文](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf)：
  印刷第 $1238$—$1240$ 页，即 PDF 第 $6$—$8$ 页。

访问记录：印刷 PDF 的浏览器读取首次返回 `Internal Error`；随后从同一作者官方 URL
作只读 HTTP 流式文本提取成功，亲读了上述三页，未保存下载副本。因此本轮既不是
只依赖检索摘要，也没有把第一次失败误记为成功。

原文位置与被用结论核对如下：

| 原文位置 | 实际核对内容 |
| --- | --- |
| §2.2；印刷 $1238$，预印本 $8$—$9$ | 模型为双曲整数矩阵加实解析周期扰动；式 (9) 是正向拉回。 |
| 定理 6；印刷 $1239$，预印本 $9$ | $C^1$ 充分小的扰动给出 Fourier 指数加权的迹类实现。 |
| 定理 7 及相邻相关性公式；印刷 $1239$，预印本 $10$ | 非零本征值按重数解释为 RP 共振。 |
| 定理 8、命题 9；印刷 $1240$，预印本 $10$—$11$ | 分别给出零噪声谱解释及各正整数次幂的绝对 Jacobian 固定点迹。 |

上述结论和位置均来自亲读原文；主证明只需要定理 6、命题 9及其共振约定，
不以定理 8 替代两个空间的迹比较桥梁。
[FR §2.2 与定理 6—命题 9](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf)

对当前族，提升可直接写成
$$
F_\kappa(q,p)=A(q,p)+g_\kappa(q,p),\qquad
g_\kappa(q,p)=\kappa\sin(2\pi q)(1,1).
\tag{1}
$$
$g_\kappa$ 实解析且周期，$\|g_\kappa\|_{C^1}\to0$；
$A\in SL(2,\mathbb Z)$、$\operatorname{Tr}A=3>2$。
这逐项满足所读一般模型，故存在同时满足 Anosov 性与 FR 实现的
$\kappa_{\mathrm{FR}}>0$。对每个符合条件的参数，可以选择 FR 允许的正加权常数
并定义其实现 $R_t$；本证明不需要该选择关于 $t$ 解析或两个空间的范数一致。

此外 $S_\kappa^{-1}=S_{-\kappa}$、$\det DS_\kappa=1$，因而
$F_\kappa$ 是保持归一面积 $dx$ 的实解析微分同胚。
FR 式 (10) 的示例顺序为 $S_\kappa A$，且
$$
A^{-1}F_\kappa A=S_\kappa A,\qquad \delta=2\pi\kappa=2t.
\tag{2}
$$
作者对此没有次序或参数归一化错误；实际适用一般模型 (1)，不需要依赖 (2) 搬运空间。
取
$$
t_A=\min\{r_0,\pi\kappa_{\mathrm{FR}}\}>0.
\tag{3}
$$
于是每个实 $0<|t|<t_A$ 同时落入两份输入定理的允许区域。

### Step 2. 参数权重、常数块与唯一迹类延拓

对每个非零实 $t$，$\omega(m)\in\mathbb Z$ 保证 $t^{\omega(m)}$ 有定义且非零。
其模为 $|t|^{\omega(m)}$，所以 (N1) 中 $f_m$ 恰为正交归一基；
负 $t$ 仅带来整数幂的符号，没有支路选择。

独立代入 (1) 得
$$
E_m(F_\kappa x)
=E_{(2r+s,r+s)}(x)
\exp\{t(r+s)(e^{2\pi iq}-e^{-2\pi iq})\}.
\tag{4}
$$
因此非零频率块在 $f_m$ 基中的矩阵元为
$t^{\omega(m)-\omega(n)}C_{r+s,k}(t)=tB(t)_{n,m}$。
常数输入恰映为常数。面积保持另给出非零频率输入的零频率输出为零，
这也可以从核直接排查：输出零频率迫使 $r+s=0$、$k=-r$，而此时
$C_{0,k}$ 只在 $k=0$ 非零，继而输入也只能为原点。

故严格的空间认同为
$$
U_t^{-1}C_tU_t=1\oplus tB(t).
\tag{5}
$$
右侧由给定输入为迹类，且在稠密的三角多项式上与实际拉回相同。
所以延拓存在且唯一，$H_t^0$ 闭且保持，两个方向的块耦合都为零。
迹类理想性质进一步给出
$$
\|C_t^n\|_1\le\|C_t\|^{n-1}\|C_t\|_1<\infty\quad(n\ge1).
\tag{6}
$$
这里的 $U_t$ 是两个已定义 Hilbert 空间之间的酉同构；没有断言其形式 Fourier
对角变换在同一个 $L^2$ 空间上有界。这正确解释了作者式 (11) 的基认同记法。

### Step 3. 整解析核心确实识别全部实际复合

对 $h\in\mathcal E$，任意闭复条带上的最大模 $M_\rho(h)$ 有限。
Fourier 积分沿各坐标向 $-\rho\operatorname{sgn}(m_j)$ 平移给出
$$
|h_m|\le M_\rho(h)e^{-2\pi\rho\|m\|_1}.
\tag{7}
$$
平移方向的符号正确，因为 Fourier 系数中的指数是 $e^{-2\pi i m\cdot z}$。
再由 $|\omega(m)|\le|r|\le\|m\|_1$，选
$2\pi\rho>|\log|t||$，即得到加权平方可和性。
同一估计也使 Fourier 截断在实环面上一致收敛。
因此 $\mathcal E\subset H_t$，其所含三角多项式保证稠密性。

提升 $F_\kappa$ 整解析，且 $F_\kappa(z+\ell)=F_\kappa(z)+A\ell$。
对 $h\in\mathcal E$，复合仍整解析并保持整数周期性，故
$h\circ F_\kappa\in\mathcal E$。任意固定复条带经提升的像可用紧性控制；
迭代增长很快不影响“每个固定函数、每个固定条带”这一结论。

每个 Fourier 系数泛函满足
$$
|g_j|\le |t|^{\omega(j)}\|g\|_{H_t}.
\tag{8}
$$
所以 $C_th^{(N)}\to C_th$ 于 $H_t$ 时，各系数收敛。
对同一截断列，因为 $F_\kappa$ 为实环面自映射，
$h^{(N)}\circ F_\kappa\to h\circ F_\kappa$ 一致，亦给出各 Fourier 系数收敛。
两个极限由 (4) 的有限输入识别相同，且 $H_t$ 的序列表示是单射，故
$$
C_th=h\circ F_\kappa\quad(h\in\mathcal E).
\tag{9}
$$
利用已经证明的核心不变性，(9) 可逐次归纳，得到
$$
C_t^nE_m=E_m\circ F_\kappa^n
\quad(m\in\mathbb Z^2,\ n\ge1).
\tag{10}
$$
这不是把单步矩阵的形式乘方直接当作真实复合，也没有对任意完成空间元素调用点值。

### Step 4. 自伴热收缩足以控制右乘迹范数

在 $f_m$ 基中定义 $P_\varepsilon f_m=e^{-\varepsilon|m|^2}f_m$。
这是范数不超过一的自伴算子，且由平方可和支配收敛强收敛到 $I$。

对迹类 $T$ 和有限秩逼近 $K$，
$$
\|T(P_\varepsilon-I)\|_1
\le2\|T-K\|_1+\|K(P_\varepsilon-I)\|_1.
\tag{11}
$$
对任一秩一项 $u\otimes v^*$，自伴性给出
$$
\|(u\otimes v^*)(P_\varepsilon-I)\|_1
=\|u\|\,\|(P_\varepsilon-I)v\|\longrightarrow0.
\tag{12}
$$
先固定 $K$，取极限，再使 $\|T-K\|_1$ 趋零，推出
$\|T(P_\varepsilon-I)\|_1\to0$。这也明确指出一般强收敛本身不够，
需要控制右因子的伴随；当前自伴性完全提供了该条件。
取 $T=C_t^n$ 并使用 (6)，得到作者的热迹极限。

### Step 5. 对角权重与 Gaussian 常数核对

记 $d_m^{(n)}$ 为实际函数 $E_m\circ F_\kappa^n$ 的第 $m$ 个 Fourier 系数。
按第二变量线性的内积约定，(10) 给出
$$
\langle f_m,C_t^nf_m\rangle_{H_t}
=\overline{t^{\omega(m)}}t^{\omega(m)}|t|^{-2\omega(m)}d_m^{(n)}
=d_m^{(n)}
=\int_{\mathbb T^2}e^{2\pi i m\cdot(F_\kappa^n x-x)}\,dx.
\tag{13}
$$
该消去对正、负实 $t$ 均精确成立。实映射保证右侧积分模不超过一。
因此乘上 Gaussian 后可以绝对交换求和与积分，得到
$$
\operatorname{Tr}(C_t^nP_\varepsilon)
=\int_{\mathbb T^2}K_\varepsilon(G_n(x))\,dx,
\qquad G_n(x)=F_\kappa^nx-x\in\mathbb T^2,
\tag{14}
$$
$$
K_\varepsilon(y)=\sum_{m\in\mathbb Z^2}e^{-\varepsilon|m|^2}e^{2\pi i m\cdot y}
=\frac\pi\varepsilon\sum_{\ell\in\mathbb Z^2}
e^{-\pi^2|y-\ell|^2/\varepsilon}.
\tag{15}
$$
二维 Fourier 变换的常数 $\pi/\varepsilon$ 正确，且
$$
\frac\pi\varepsilon\int_{\mathbb R^2}e^{-\pi^2|y|^2/\varepsilon}\,dy=1.
$$
故核非负、环面总质量为一。若 $d(y,0)\ge d>0$，将指数一半提出，
剩下的格点和在基本域及 $0<\varepsilon\le1$ 上一致有界，得到
$O(\varepsilon^{-1}e^{-\pi^2d^2/(2\varepsilon)})$。
这里先按周期性把 $y$ 放在一个紧基本域内，因而该一致有界性没有遗漏无界平移。

### Step 6. 固定点非退化、全部逆分支与补集控制

$G_n$ 用环面的群运算定义，是全局光滑映射。
提升 $\widetilde F_\kappa^n(x)-x$ 在 $x\mapsto x+\ell$ 下改变
$(A^n-I)\ell\in\mathbb Z^2$，所以该定义不依赖提升；局部导数是
$DG_n=D F_\kappa^n-I$。

在固定点 $p$，稳定和不稳定子空间被 $D_pF_\kappa^n$ 保持。
若稳定特征值为 $\alpha$，Anosov 估计对重复周期给出
$|\alpha|^k\le C\theta^{nk}$，其中 $C>0$、$0<\theta<1$。
取 $k$ 次根并令 $k\to\infty$，得 $|\alpha|\le\theta^n<1$；
在不稳定空间对逆映射作同样推导，得到特征值模大于一。
因此 $\det DG_n(p)\ne0$，不能把稳定方向的一次算子范数误当作必小于一，
而作者所用的周期点特征值结论本身正确。

固定点由逆函数定理孤立，固定点集又是紧集，所以有限。
若其为空，(15) 的离零一致估计直接使 (14) 趋于零。
若固定点为 $p_1,\ldots,p_J$，则可精确展开作者的共同像球构造：

1. 为各 $p_j$ 选两两不交的开邻域 $O_j$，使 $G_n:O_j\to W_j$ 微分同胚。
2. 令 $K=\mathbb T^2\setminus\bigcup_jO_j$。它紧且不含零点，因此
   $d(0,G_n(K))>0$。
3. 选以零点为中心的小球 $V$，使 $\overline V\subset\bigcap_jW_j$，
   且半径小于上述正距离。
4. 定义 $U_j=(G_n|_{O_j})^{-1}(V)$；此时
   $G_n^{-1}(V)=\bigsqcup_jU_j$，没有遗漏远处额外原像。

若 $x_j$ 为逆分支，函数
$$
a_j(y)=|\det DG_n(x_j(y))|^{-1}
$$
在 $\overline V$ 上连续且有界。实变量换元和 (15) 给出
$$
\int_{U_j}K_\varepsilon(G_n(x))\,dx
=\int_VK_\varepsilon(y)a_j(y)\,dy
\longrightarrow a_j(0).
\tag{16}
$$
绝对 Jacobian 必须保留，作者没有以有符号行列式替代。
在 $G_n^{-1}(V)$ 的补集，像到零点的距离至少为 $V$ 的半径，
故补集积分趋零。结合第 4 步，获得
$$
\operatorname{Tr}_{H_t}(C_t^n)
=\sum_{p\in\operatorname{Fix}(F_\kappa^n)}
\frac1{|\det(D_pF_\kappa^n-I)|}.
\tag{17}
$$
作者已保留闭球上的延拓条件，足以支持 (16) 的有界性；不存在只靠零点连续性
却未控制其余区域的缺口。

### Step 7. 全部幂迹、整个行列式与代数重数

对固定的同一个允许实参数，(17) 与亲读的 FR 命题 9 给出
$$
\operatorname{Tr}(C_t^n)=\operatorname{Tr}(R_t^n)\quad(n\ge1).
\tag{18}
$$
这里每个 $n$ 的热极限单独成立，已经足以得到这一组恒等式；不需要在
$n\to\infty$ 时交换热极限。

迹类 Fredholm 行列式的幂迹展开在 $|z|\|T\|<1$ 时收敛。
从 $|\operatorname{Tr}(T^n)|\le\|T\|_1\|T\|^{n-1}$ 也可直接检查
作者选择的共同 $z$ 邻域。因此 (18) 给出两行列式在零点附近完全相同。
二者作为 $z$ 的函数均整，整函数恒等定理把相等延至整个复平面。
由 (5) 的正交块分解，再得到 (C1) 的最后一个因子分解。

迹类谱—行列式对应定理适用于这两个迹类算子：每个 $\lambda\ne0$ 是孤立的
有限代数重数特征值，当且仅当 $z=\lambda^{-1}$ 是 Fredholm 行列式的零点，
且该零点阶数等于其代数重数。因此作者得到的是非零谱的完整多重集，
不是只比较几何重数或有限条渐近系数。$\lambda=0$ 不由行列式零点检测，
作者也没有提出该额外结论。

### Step 8. 常数共振唯一性与参数边界

令
$$
t_*=\min\{t_A,1/(2M)\}>0.
\tag{19}
$$
对实 $0<|t|<t_*$，核性输入直接给出
$$
\|tB(t)\|\le |t|\|B(t)\|_1<1/2.
\tag{20}
$$
所以 $1\notin\operatorname{Spec}(tB(t))$，且零均值块的全部谱都在
半径 $1/2$ 的圆盘内。由严格块分解 (5)，常数块中的 $1$ 在整个空间代数简单：
零均值块上 $tB(t)-I$ 可逆，既没有额外本征向量，也没有把该块接到常数方向的
广义本征链。借 (C1)，同一结论转移到 FR 共振多重集。

原定理的 $t_A$ 与额外的 $t_*$ 分工正确。前者给谱识别，后者用保守但明确的
范数界给常数唯一性；不能在不作额外论证的情况下把 (20) 的量词扩大到全部
$0<|t|<t_A$，作者没有如此扩大。

对负实 $t$，所有上述步骤仍成立；对复 $t$，虽然 $B(t)$ 有给定解析延拓，
实际映射不再是这里的实面积自映射，(13) 的实相位界、(14) 的正核定位及
FR 的实动力学适用条件不能直接沿用。$t=0$ 时 (N1) 的空间也没有被定义。
作者恰好排除了这两类越界。原定理在原量词内证毕。$\square$

## Corrections or Missing Assumptions

无需科学修正，也无需补加空间相似、任意元素点值、对时间一致的热极限或复参数假设。
作者列出的 FR 印刷页码已在本轮实际成功读取后核实，不是待验证的转引。

本报告明确展开了三处容易误读但原文已经有充分依据的细节：

- 酉同构 $U_t$ 是不同完成空间之间的基认同，不是同一个 $L^2$ 上的有界对角相似。
- 周期点稳定特征值估计通过重复周期消去 Anosov 常数，不要求一次导数范数小于一。
- 共同像球必须避开原局部邻域补集的像；紧性保证作者所需的全部逆分支覆盖。

这些均不是新增实验、修改定理或重新开启已通过输入的理由。

## Open Risks and Disposition

本次范围内无未闭合证明义务；结论依赖给定核性输入及已经核实适用的 FR 定理。
仍不包含以下范围外断言：零谱结构识别、任意完成空间元素的点值、两个实现的有界共轭、
复耦合的物理共振、$t=0$ 的物理空间，以及新意或篇幅可行性。

交付状态：指定独立核查完成；保留作者输入与既有代数报告，完成后停止。
