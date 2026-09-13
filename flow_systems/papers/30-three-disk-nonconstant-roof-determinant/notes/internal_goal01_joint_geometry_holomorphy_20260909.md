# P30 goal01：共同复几何邻域中的碰撞配置、物理 roof 与正一侧代表

日期：2026-09-09 UTC。唯一写入授权为本新增内部笔记；不改旧稿、既有笔记、程序、数据、锁定输入或正式状态。

**审读状态：主整合审读尚未完成。** 下文是可逐项检查的新纸面推导，不是形式化验证、实验或外部独立认证；同伴同意也不计作独立科学证据。不存在 Route／Stage 升级或数学新颖性认证。

## 1. 上游输入、固定空间与准确的局部命题

[双向配置笔记][coding] §1–2 给出等边三盘的全部闭盘配置收缩，§3 给出固定点与真实首次飞行的双向桥接，§4 给出有限块依赖与 roof 局部性。[一侧 roof 笔记][one-sided] §2–4 给出固定几何的一侧化、有限平均保正和固定空间整算子族；它未证明几何参数的联合全纯性。

固定单位欧氏速率、原盘标记和基准参数

\[
C_1^0=(0,0),\quad C_2^0=(6a,0),\quad C_3^0=(3a,3\sqrt3a),
\quad K_i=\overline B_{\mathbb R^2}(C_i^0,a),\quad a>0.
\tag{1}
\]

仍使用全部相邻字母不等的双向盘字空间 \(\Sigma\)、一侧空间 \(\Sigma^+\)、左移 \(\sigma,\sigma^+\) 和遗忘过去的 \(\pi\)。对双向字令 \(N(x,y)=\min\{|j|:x_j\ne y_j\}\)，并固定 \(0<\theta<1\)，取 \(d_\theta(x,y)=\theta^{N(x,y)}\)；相同字距离为零。一侧使用首个非负分歧位置定义 \(d_\theta^+\)。

复向量范数与双线性点积必须分开：

\[
|z|_{\mathbb C^2}=(|z_1|^2+|z_2|^2)^{1/2},\qquad
z\cdot w=z_1w_1+z_2w_2.
\tag{2}
\]

前者仅用于估计；后者用于构造全纯函数，**不含复共轭**。定义

\[
E=\ell^\infty(\Sigma\times\mathbb Z;\mathbb C^2),\qquad
\mathcal B_\gamma^-=C^\gamma(\Sigma,d_\theta;\mathbb C),\qquad
\mathcal B_\gamma^+=C^\gamma(\Sigma^+,d_\theta^+;\mathbb C),
\quad \|F\|_\gamma=\|F\|_\infty+[F]_\gamma.
\tag{3}
\]

上式 \(\mathcal B_\gamma^-\) 指双向空间、\(\mathcal B_\gamma^+\) 指一侧空间；向量值版本用 (2) 的范数。它们完备：范数 Cauchy 列先一致收敛，将差商取极限再取上确界即得原范数收敛。标量版本满足 \(\|FG\|_\gamma\le\|F\|_\gamma\|G\|_\gamma\)。

原几何常数及可选择的指数为

\[
\kappa_*=(2\sqrt6-1)/6>1/2,\quad
\rho=(2\kappa_*)^{-1}<1,\quad \alpha=\frac{\log\rho}{\log\theta},
\quad 0<\beta<\alpha/2,
\quad \rho<r<\theta^{2\beta},\quad t=\theta^\beta.
\tag{4}
\]

任意上述 \(\beta\) 均可选；例如先选 \(\beta=\alpha/4\)，再选 \(\rho<r<\sqrt\rho\)。这些选择一次固定，不依赖参数微分阶或 code。

**局部命题。** 存在基准圆心／半径的共同复参数邻域 \(\Omega\subset\mathbb C^9\)，使固定配置 \(\zeta\mapsto Q_\zeta\in E\)、第零碰撞点 \(\zeta\mapsto Q_{0,\zeta}\in C^\beta(\Sigma;\mathbb C^2)\)、物理 roof 的复延拓 \(\zeta\mapsto\tau_\zeta\in\mathcal B_\beta^-\) 均全纯。还有一个明确的一侧族 \(\widehat g_\zeta\in\mathcal B_\beta^+\)，全纯、与 \(\tau_\zeta\) 上同调，并在实参数切片满足 \(2a\le\widehat g_\zeta\le10a\)。所有紧参数域上的每个固定阶导数有同一 Banach 范数中的一致界。

这里证明的是 \(\beta<\alpha/2\) 的共同复邻域正常收敛。上游固定几何的物理 roof 具有指数 \(\alpha\)，其一侧化在实基准参数可达到 \(\alpha/2\)；本命题不声称共同复族仍保持这两个端点指数，也不声称损失最优。

## 2. 复管、平方根分支与有限组态紧致性

参数写成 \(\zeta=(\Delta C_i,\Delta a_i)_{i=1}^3\)，其中 \(\Delta C_i\in\mathbb C^2\)、\(\Delta a_i\in\mathbb C\)，令

\[
C_i(\zeta)=C_i^0+\Delta C_i,\quad a_i(\zeta)=a+\Delta a_i,
\quad \|\zeta\|_{\rm geom}=\max_i\{ |\Delta C_i|,|\Delta a_i|\}.
\tag{5}
\]

圆心和半径是仿射全纯参数，不在其复延拓中取绝对值。对 \(d>0\) 定义精确的闭复管及配置域

\[
T_i^d=K_i+\overline B_{\mathbb C^2}(0,d)
 =\{z:\operatorname{dist}_{\mathbb C^2}(z,K_i)\le d\},\quad
\mathcal X_x^d=\prod_{j\in\mathbb Z}T_{x_j}^d.
\tag{6}
\]

每个 \(T_i^d\) 是实凸紧集。\(\mathcal X_x^d\) 在 \(\ell^\infty(\mathbb Z;\mathbb C^2)\) 中是非空闭凸完备集。所有 codes 同时使用时，取 \(E\) 中逐坐标满足 (6) 的闭凸集；没有依赖 code 的管宽。

在 \(\operatorname{Re}(z\cdot z)>0\) 上取正实根对应的平方根，置

\[
\nu_{\mathbb C}(z)=z/\sqrt{z\cdot z},\qquad
S(p,q,w)=\nu_{\mathbb C}(p-q)+\nu_{\mathbb C}(w-q).
\tag{7}
\]

需要控制的实组态只有 12 个紧集 \(K_j\times K_i\times K_k\)，其中 \(j\ne i\)、\(k\ne i\)，允许 \(j=k\)。上游在这些**全部闭盘三点组态**上证明跨盘距离在 \([4a,8a]\)，且 \(|S|\ge2\kappa_*\)，并非仅在固定点处成立。

若 \(v\) 是上述实跨盘差向量，\(e\) 是其管内扰动，则 \(|e|\le2d\)，由双线性点积的 \(|z\cdot w|\le|z||w|\)，

\[
|(v+e)\cdot(v+e)-|v|^2|\le32ad+4d^2.
\tag{8}
\]

取 \(d\) 足够小使右端小于 \(8a^2\)，所有内层平方量便满足 \(\operatorname{Re}(z\cdot z)>8a^2\)。内层分支于是先被合法定义；它在这些有限紧组态上连续且有界。再缩小同一个 \(d\)，使外层也满足

\[
\operatorname{Re}\bigl(S(p,q,w)\cdot S(p,q,w)\bigr)>2\kappa_*^2.
\tag{9}
\]

理由是基准实值至少 \(4\kappa_*^2\)，有限紧集上的连续延拓一致。两层平方根由右半平面的同一分支控制；没有绕零改变分支或逐 code 选根。

## 3. 复方向导数、共同收缩及不变性

定义迭代的第 j 坐标

\[
(\mathscr P_{\zeta,x}q)_j=C_{x_j}(\zeta)+a_{x_j}(\zeta)
\nu_{\mathbb C}\bigl(S(q_{j-1},q_j,q_{j+1})\bigr).
\tag{10}
\]

在非零实向量 v 处，

\[
D\nu_{\mathbb C}(v)h=
\frac{(I-\nu(v)\nu(v)^{\mathsf T})h}{|v|}.
\tag{11}
\]

矩阵是实正交投影；作为作用于 Hermitian 范数复向量的复线性矩阵，它仍有算子范数 1。因此 (11) 的界对**复方向 h**也成立，不是将实 Lipschitz 界未经证明地复杂化。对基准的一个更新坐标，用三输入的最大范数，逐块估计得

\[
|D\mathscr P_{0,x,j}(h_-,h_0,h_+)|
\le\frac{|h_-|+2|h_0|+|h_+|}{8\kappa_*}
\le\rho\max\{|h_-|,|h_0|,|h_+|\}.
\tag{12}
\]

在 (8)–(9) 的全纯定义域内，三输入导数的有限维算子范数连续。12 个基准紧集和固定 \(r>\rho\) 因而给出 \(d_0>0,\eta_0>0\)：对 \(T^{d_0}\) 中全部相应三点及 \(\|\zeta\|_{\rm geom}\le\eta_0\)，两层分母满足严格裕量且该导数范数至多 r。半径因子 \(a_i(\zeta)\) 已包含在此连续性估计中。

这一步只需有限维紧致性：任何趋近基准紧集却破坏所需严格界的序列都有落在该紧集的收敛子列，与 (8)–(12) 矛盾。每个无限 code 的每个更新坐标都属于这 12 种局部情形，故常数同时控制所有无限 codes 与所有坐标。

现在选 \(\delta=d_0/2\)，实际迭代只用 \(\mathcal X_x^\delta\)，较大的管用于提供定义邻域。沿实际凸管中两配置的线段积分 (12) 的邻域版本，得到

\[
\|\mathscr P_{\zeta,x}q-\mathscr P_{\zeta,x}\widetilde q\|_\infty
\le r\|q-\widetilde q\|_\infty.
\tag{13}
\]

为证明映回同一管，逐坐标选择实基配置 \(b_j\in K_{x_j}\) 使 \(|q_j-b_j|\le\delta\)。对这样的实 b，S(b) 是非零实向量，\(\nu_{\mathbb C}(S(b))\) 正是实单位向量，Hermitian 范数为 1。方向 S 在固定 b 下不依赖几何参数，所以精确地

\[
(\mathscr P_{\zeta,x}b-\mathscr P_{0,x}b)_j
=\Delta C_{x_j}+\Delta a_{x_j}\nu_{\mathbb C}(S(b)),
\quad\|\mathscr P_{\zeta,x}b-\mathscr P_{0,x}b\|_\infty\le2\|\zeta\|_{\rm geom}.
\tag{14}
\]

一般复配置的 \(\nu_{\mathbb C}(S(q))\) 并非 Hermitian 单位向量；(14) **仅对所选实 b 使用**。由于 \(\mathscr P_{0,x}b\in\mathcal X_x^0\)，

\[
\operatorname{dist}(\mathscr P_{\zeta,x}q,\mathcal X_x^0)
\le r\delta+2\|\zeta\|_{\rm geom}.
\tag{15}
\]

按次序完成选择：在确定 \(r,d_0,\delta,\eta_0\) 后，固定

\[
0<\eta<\min\{\eta_0,(1-r)\delta/4,a/4,(3\sqrt3-2)a/8\},
\qquad\Omega=\{\zeta:\|\zeta\|_{\rm geom}<\eta\}.
\tag{16}
\]

于是 (15) 严格小于 \(\delta\)，实际管不变；且 \(2\eta<\delta\)。所有选择都在迭代及参数微分之前完成。

## 4. 固定迭代的正常收敛与真实几何识别

令 \(q^0_j(x)=C_{x_j}^0\)，\(q^{n+1}_\zeta=\mathscr P_{\zeta,x}q^n_\zeta\)。每个有限迭代的坐标关于参数全纯，由 (14) 得 \(\|q^1-q^0\|_\infty\le A:=a+2\eta\)，故

\[
\|q^{n+1}_\zeta-q^n_\zeta\|_E\le Ar^n,\qquad
\|Q_\zeta-q^n_\zeta\|_E\le\frac{A}{1-r}r^n.
\tag{17}
\]

完备性给极限；由 (13) 的连续性它是固定点，同一管中两个固定点的距离至多自身的 r 倍，故唯一。第 n 次迭代坐标只依赖 \(x_{j-n},\ldots,x_{j+n}\)，这是 (10) 的三点局部性归纳。每个有限 n 在 \((x,j)\) 上因此只使用有限种块函数，其参数全纯性实际发生在 E 的有限维子空间中。(17) 的一致正常收敛与 Cauchy 公式给 \(E\)-值全纯性，不只逐 code 全纯。

对实 \(\zeta\)，迭代从实配置开始，所选平方根始终为正实根。固定点位于新的真实圆周。新盘到旧盘的 Hausdorff 距离至多 \(2\eta\)，因而跨盘距离在 \([4a-4\eta,8a+4\eta]\)，no-eclipse 间隔至少 \((3\sqrt3-2)a-4\eta>0\)。

固定点方程给 \(-v^-+v^+=2\chi n\)，其中 \(\chi=|S|/2>0\)；故入射、出射法向符号及反射公式仍成立。出发盘、到达盘的平方距离公式与严格 no-eclipse 共同排除早撞第三盘，正飞行下界排除碰撞累积。反过来，任意真实双向被困轨道的碰撞配置落在本管内，反射公式与 S 的正下界迫使它满足 (10)，故等于唯一固定点。这里沿用的是上游 §3 的明确代数论证，其严格几何前提已在本段保持，并未假定“拓扑结构稳定定理”。

## 5. 碰撞点和物理 roof 的固定 Cβ 范数全纯性

第零坐标增量 \(D_n=q^{n+1}_{0,\zeta}-q^n_{0,\zeta}\) 只依赖中心半径 \(n+1\) 的块。如果两个增量值不同，其首分歧 N 至多 \(n+1\)；由 (17)，

\[
\|D_n\|_{C^\beta}\le Ar^n(1+2t^{-n-1})
\le A(1+2/t)(r/t)^n.
\tag{18}
\]

因为 \(r<t^2<t\)，此增量级数在共同复邻域内正常收敛。有限块函数及其参数导数属于有限维柱集函数空间，故各项本身是 \(C^\beta\)-值全纯函数；(18) 证明极限 \(Q_{0,\zeta}\) 的该意义全纯性。

令 \(\ell(z)=\sqrt{z\cdot z}\)，并取同一分支定义

\[
\tau^n_\zeta(x)=\ell(q^n_{1,\zeta}(x)-q^n_{0,\zeta}(x)),\quad
\tau_\zeta(x)=\ell(Q_{1,\zeta}(x)-Q_{0,\zeta}(x)).
\tag{19}
\]

相应跨盘差向量位于共同紧邻域，\(D\ell(z)h=(z\cdot h)/\sqrt{z\cdot z}\) 的范数有统一有限界 L。沿凸管线段积分，得

\[
\|\tau^{n+1}_\zeta-\tau^n_\zeta\|_\infty\le A_\tau r^n,
\quad A_\tau=2LA.
\tag{20}
\]

增量依赖块包含于 \([-n-1,n+2]\)，所以与 (18) 完全同样地

\[
\|\tau^{n+1}_\zeta-\tau^n_\zeta\|_{C^\beta}
\le A_\tau(1+2/t^2)(r/t)^n.
\tag{21}
\]

这给 \(\tau_\zeta\in\mathcal B_\beta^-\) 的正常收敛与全纯性。实参数切片上它就是实际单次飞行时间，且由 (16) 有 \(3a\le\tau_\zeta\le9a\)。

一侧化还需要保留比目标 beta 更强的统一局部性。若 \(N(x,y)\ge2\)，取 \(n=N-2\)，则 \(\tau^n(x)=\tau^n(y)\)，因为它只看 \([-n,n+1]\)。用 (20) 的两侧尾和，并增大常数覆盖 N=0、1，得到一个与参数、codes 无关的有限 \(C_0\)：

\[
|\tau_\zeta(x)-\tau_\zeta(y)|\le C_0r^{N(x,y)}
\quad(\zeta\in\Omega).
\tag{22}
\]

## 6. 固定过去的一侧化：逐项 Cβ 正常收敛

采用与[一侧笔记][one-sided] §2 完全相同的 R：\(b(1)=2\)、\(b(2)=b(3)=1\)；保留非负坐标，负坐标按 \(x_0,b(x_0)\) 交替。R 合法、不扩张双向距离，且只依赖未来。它一般不与移位交换，以下不使用这种错误交换。

置

\[
U_{n,\zeta}(x)=\tau_\zeta(\sigma^nx)-\tau_\zeta(\sigma^nRx),
\qquad h_\zeta=\sum_{n\ge0}U_{n,\zeta}.
\tag{23}
\]

两被比较字在全部 \(j\ge-n\) 一致，故

\[
\|U_{n,\zeta}\|_\infty\le C_0r^{n+1},\qquad
\|h_\zeta\|_\infty\le B:=C_0r/(1-r).
\tag{24}
\]

令 \(m=N(x,y)\)。当 \(m\ge n\)，移位后原字对及 R 字对的首分歧都至少为 \(m-n\)，由 (22) 有项差界 \(2C_0r^{m-n}\)。当 \(m<n\)，**不声称存在负长度的一致块**：直接用 (22) 的全局界得项差至多 \(2C_0\)，而 \(r^{m-n}>1\)，故同一较松上界仍成立。再结合 (24) 的两个上确界，得到对全部 m、n 有效的

\[
|U_{n,\zeta}(x)-U_{n,\zeta}(y)|
\le2C_0\min\{r^n,r^{m-n}\}.
\tag{25}
\]

当 \(m\le2n\) 时，除以 \(t^m\)，用第一项得至多 \(2C_0(r/t^2)^n\)；当 \(m\ge2n\) 时，用第二项得到该量再乘 \((r/t)^{m-2n}\le1\)。因此

\[
[U_{n,\zeta}]_\beta\le2C_0(r/t^2)^n,\qquad
\|U_{n,\zeta}\|_{C^\beta}\le3C_0(r/t^2)^n.
\tag{26}
\]

固定 n 时，组合 \(F\mapsto F\circ\sigma^n\) 与 \(F\mapsto F\circ R\) 都是固定空间上的有界线性算子；前者范数至多 \(t^{-n}\)，后者至多 1。所以每个 \(U_{n,\zeta}\) 已是 Banach 值全纯函数。(26) 与 \(r/t^2<1\) 才将级数提升为共同 \(C^\beta\) 范数中的正常收敛，而不仅仅是逐点或上确界收敛。

若 \(\pi x=\pi y\)，则 \(Rx=Ry\)，直接相减 (23) 得

\[
h_\zeta(x)-h_\zeta(y)=\sum_{n\ge0}
[\tau_\zeta(\sigma^nx)-\tau_\zeta(\sigma^ny)].
\tag{27}
\]

此级数绝对收敛；对 \(\sigma x,\sigma y\) 的同式删去首项。故

\[
f_\zeta=\tau_\zeta-h_\zeta+h_\zeta\circ\sigma=f_\zeta^+\circ\pi.
\tag{28}
\]

从一侧字补入标准过去的提升 J 是等距嵌入，\(f_\zeta^+=f_\zeta\circ J\)。因此它在同一 \(\mathcal B_\beta^+\) 中全纯。以上是对真实几何 roof 的推导，未借助抽象 toy 例子判定实际几何。

## 7. 固定 N 平均保正、保周期与规范区别

(28) 本身不保证正性。使用 (24) 的共同常数，固定与参数无关的整数

\[
N_*\ge\max\{1,\lceil2B/a\rceil\},\qquad
\widehat g_\zeta=\frac1{N_*}\sum_{j=0}^{N_*-1}f_\zeta^+\circ(\sigma^+)^j.
\tag{29}
\]

有限个固定有界组合保持 \(\mathcal B_\beta^+\)-值全纯性。望远镜求和给

\[
\widehat g_\zeta\circ\pi
=\frac{S_{N_*}\tau_\zeta-h_\zeta+h_\zeta\circ\sigma^{N_*}}{N_*},
\qquad 2a\le\widehat g_\zeta\le10a\quad(\zeta\text{ 实}).
\tag{30}
\]

最后一个不等式使用真实 \(\tau_\zeta\in[3a,9a]\) 和 \(2B/N_*\le a\)；不对复参数谈有序正性。再令

\[
v_\zeta=\frac1{N_*}\sum_{j=0}^{N_*-2}(N_*-1-j)
f_\zeta^+\circ(\sigma^+)^j,\qquad V_\zeta=h_\zeta+v_\zeta\circ\pi.
\tag{31}
\]

当 \(N_*=1\) 时此和为零。逐项比较系数得 \(\widehat g=f^+-v+v\circ\sigma^+\)，故

\[
\widehat g_\zeta\circ\pi=\tau_\zeta-V_\zeta+V_\zeta\circ\sigma.
\tag{32}
\]

全部周期和保持，不要求周期为 \(N_*\) 的倍数。实切片上，双向悬挂映射 \([x,u]_{\tau_\zeta}\mapsto[x,u-V_\zeta(x)]_{\widehat g_\zeta\circ\pi}\) 与边界识别相容并交换时间平移，逆映射加回 V；这没有缩放原物理时间。

这里明确构造的是共同规范代表 \(\widehat g_\zeta\)，而不是把实际逐飞行长度删去过去。基准参数处 R、h、f 与一侧笔记的选择一致，但其平均长度 \(m_*\) 与本处 \(N_*\) 可不同，因此不自动宣称两份笔记中的正一侧函数逐点相同；它们均与同一物理 roof 上同调。没有修改该旧笔记或原时钟。

## 8. 导数界、可用接口与停止边界

对任意紧集 \(K\Subset\Omega\)，取 \(\varepsilon_K>0\) 使每点周围坐标半径 \(\varepsilon_K\) 的九维闭多圆盘仍在 \(\Omega\)。前述正常收敛给各 Banach 值族 F 的共同有限界 \(M_F\)。多元 Cauchy 公式在 Banach 范数中成立，并给

\[
\sup_{\zeta\in K}\|\partial_\zeta^\mu F_\zeta\|
\le\mu!\,M_F\,\varepsilon_K^{-|\mu|}.
\tag{33}
\]

它可直接由有限块近似的 Cauchy 积分及范数一致极限得到；不需要未展开的隐函数定理。固定紧域不随导数阶改变，常数允许依赖阶数。实参数限制因此是 Banach 值实解析族，结论强于仅逐 code 实解析或 C1。

若只取基础转移接口，仍在固定 \(\mathcal B_\beta^+\) 上定义 \(\mathcal L_{s,\zeta}=\mathcal L_0M_{\exp(-s\widehat g_\zeta)}\)。一侧笔记 §4 的乘积与指数级数证明适用于当前较小 beta，给 \((s,\zeta)\in\mathbb C\times\Omega\) 的算子范数联合全纯性及 \(\|\mathcal L_{s,\zeta}\|\le6e^{|s|\|\widehat g_\zeta\|_\beta}\)。这里不调用该笔记其他节的谱论推导来扩大本页结论。

指数损失有两个明确位置：(18)、(21) 要求 \(r<t\)，(26) 要求更强的 \(r<t^2\)。原实收缩率 rho 不能直接当作整个复邻域的收缩率；本页先选择严格余量 \(\rho<r<t^2\)，因此只覆盖 \(\beta<\alpha/2\)。实几何“每点 Hölder”不是这项联合全纯性的理由；真正理由是共同复分母、复方向导数、code 一致收缩和 Banach 范数正常收敛。

未建立共同邻域的最优数值半径、端点指数保持、物理切向双曲分裂、谱隙、核性、trace-class、算子跡、dynamical／Fredholm／quantum determinant 身份或 Hilbert–Pólya 结论。同步更新始终只是几何实现的证明工具，不是物理碰撞映射的收缩证明。原 Route、Gate、Stage 5／6 边界和历史失败记录不变。

## 9. 实际操作与证据限制

本单元沿用已完整读过的工作区规则与 ARS router 的有限理论分析边界；重读双向配置笔记中实际使用的全盘组态、收缩及局部性段落，完整读取新一侧笔记以固定 R、符号与规范差异。上述新结论由本页公式承担，不倒写为上游已证，不声称文献穷尽或首创。

写前 `test ! -e` 确认本目标不存在；仅以 `apply_patch` 新建本文件。不运行科学或符号程序、数值迭代、字词／轨道枚举、实验、artifact writer、稿件构建或正式验证器，也不再派工。尝试的只读 `git status` 因当前目录不在 Git 工作树中而不可用；它没有改变文件，亦不影响本页明列的单文件写入边界。写后只做文件存在、行数与局部文字／链接检查；这些检查不认证数学成立性。主整合审读尚未完成。

[coding]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_biinfinite_coding_and_roof_locality_20260909.md
[one-sided]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
