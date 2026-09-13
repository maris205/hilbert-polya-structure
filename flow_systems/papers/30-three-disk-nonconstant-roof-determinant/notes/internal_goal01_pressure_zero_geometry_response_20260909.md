# P30 goal01：较小 Hölder 空间中的压力零点、几何响应与紧频带开放性

日期：2026-09-09 UTC。唯一新增授权为本文件；不改其他新旧文件、原稿、程序、数据、锁定输入或正式状态。

**主整合审读尚未完成。** 本页是内部分步论证与已核读定理的具体应用，不是形式化验证、外部独立认证或研究新颖性声明。本文 h 只定义为 RPF 谱压力的零点；没有在本单元核读并应用悬挂熵定理，因此不将它标为真实物理流的拓扑熵。

## 1. 新对象、固定空间与本页结论

继承[共同几何全纯笔记][geometry]的真实三盘参数邻域 \(\Omega\subset\mathbb C^9\)、原单位速率飞行时间 \(\tau_\zeta\)，以及其中明确构造的正一侧代表 \(\widehat g_\zeta\)。以下固定

\[
0<\theta<1,\quad \rho=\frac3{2\sqrt6-1},\quad
\alpha=\frac{\log\rho}{\log\theta},\quad
0<\beta<\alpha/2,\quad q=\theta^\beta\in(0,1),
\tag{1}
\]

\[
\mathcal B=C^\beta(\Sigma^+,d_\theta^+;\mathbb C),\qquad
\|u\|_\beta=\|u\|_\infty+[u]_\beta.
\tag{2}
\]

这里 \(\Sigma^+\) 是三字母、相邻字母不等的一侧移位，距离由首个分歧位置决定。\(\sigma^+\) 为左移；双向空间及其左移记为 \(\Sigma,\sigma\)，\(\pi\) 遗忘过去。基准半径记为 \(a_0>0\)，避免与 §7 的变化尺度 a 混淆。

上游已给出 Banach 值全纯族及一个同样全纯的双向共边界函数 \(V_\zeta\)：

\[
\widehat g_\zeta\circ\pi=\tau_\zeta-V_\zeta+V_\zeta\circ\sigma,
\qquad 2a_0\le\widehat g_\zeta\le10a_0
\quad(\zeta\in\Omega\cap\mathbb R^9).
\tag{3}
\]

该规范固定了标准过去 R 与同一个平均长度 \(N_*\)，不随谱参数或几何参数重选。[旧一侧笔记][one-sided]使用端点指数 \(\alpha/2\) 及可能不同的平均长度；本页不能把那份空间上的谱结论直接搬来，亦不声称新旧正代表逐点相同。

本页证明：

- 在当前较小 beta 的空间上重新应用实 RPF，得到简单正本征值 \(\lambda(t,\zeta)\)、正左右本征对象及不变概率。
- \(P=\log\lambda\) 在实参数上定义，其简单本征值分支在每个实基点附近全纯；存在唯一实压力零点 h，且它有局部复全纯延拓。
- \(P_s=-\mu(\widehat g)\)、\(D_\zeta P=-s\mu(D_\zeta\widehat g)\)，故 \(Dh=-h\mu(D\widehat g)/\mu(\widehat g)\)。整体尺度满足 \(h(a)=h(1)/a\)。
- 基准的严格逐频率下降可在当前新空间重建；对任意固定紧实参数区间与有限非零频带，该下降对充分小的实几何扰动保持统一幂界。

## 2. 同一 Banach 空间上的联合全纯算子

定义

\[
(\mathcal L_{s,\zeta}u)(x)=\sum_{j\ne x_0}
 e^{-s\widehat g_\zeta(jx)}u(jx).
\tag{4}
\]

两点首字母相同时可以配对相同的前置字母，前缀使 beta 次方距离缩为 q 倍；首字母不同时距离为 1，直接用两个上确界。于是对不含权重的 \(\mathcal L_0\)，

\[
\|\mathcal L_0u\|_\infty\le2\|u\|_\infty,\qquad
[\mathcal L_0u]_\beta\le2q[u]_\beta+4\|u\|_\infty,
\quad\|\mathcal L_0\|\le6.
\tag{5}
\]

乘积差商使 \(\mathcal B\) 成为含单位元 Banach 代数。因此指数级数在固定范数中正常收敛，并给

\[
\mathcal L_{s,\zeta}=\mathcal L_0M_{e^{-s\widehat g_\zeta}},\qquad
\|\mathcal L_{s,\zeta}\|\le6e^{|s|\|\widehat g_\zeta\|_\beta},
\tag{6}
\]

\[
\partial_s\mathcal L_{s,\zeta}
 =-\mathcal L_{s,\zeta}M_{\widehat g_\zeta},\qquad
D_\zeta\mathcal L_{s,\zeta}[\delta]
 =-s\mathcal L_{s,\zeta}M_{D\widehat g_\zeta[\delta]}.
\tag{7}
\]

这在 \(\mathbb C\times\Omega\) 上是算子范数联合全纯族。空间、距离、beta、分支标签及 roof 规范均已固定；复几何参数不再有有序正性的含义。

## 3. 在新 beta 上重新核对实 RPF 的全部输入

允许矩阵 \(A=J-I\) 满足 \(A^2=J+I>0\)，故是混合有限型移位。对每个实 \(t\) 与实 \(\zeta\in\Omega\)，势 \(f=-t\widehat g_\zeta\) 实值且属于当前 \(\mathcal B\)。

本次实际核读 [Stoyanov 作者稿，Theorem 2.1(a)–(d)][rpf] 及其 §1 的 \(\mathcal F_\vartheta\) 定义。该定理在非周期性允许矩阵、实 \(\mathcal F_\vartheta\) 势的前提下提供正本征函数、对偶测度、简单最大正本征值及其余谱的严格分离。这里重新取 \(\vartheta=q=\theta^\beta\)，不是旧空间的 \(\sqrt\rho\)。

准确的范数对应如下。来源定义 \(\operatorname{var}_k u\) 为在坐标 \(0,\ldots,k\) 一致的两字上的最大变差，\(|u|_q=\sup_{k\ge0}\operatorname{var}_k u/q^k\)。则

\[
|u|_q\le q[u]_\beta,\qquad
[u]_\beta\le\max\{2\|u\|_\infty,q^{-1}|u|_q\}.
\tag{8}
\]

第二式分别处理首分歧 N=0 与 N>=1。这证明当前空间与来源 \(\mathcal F_q\) 相同且范数等价，不仅是两个模糊的“Hölder 类”。故 RPF 在本空间上重新给

\[
\mathcal L_{t,\zeta}v=\lambda v,\quad
\mathcal L_{t,\zeta}^*\nu=\lambda\nu,\quad
\lambda>0,\quad \min v>0,\quad \nu(v)=1,
\tag{9}
\]

其中可先取 \(\nu\) 为概率再归一化 v。\(\lambda\) 代数单重且隔离，其余谱位于严格较小的圆盘内。RPF 概率 \(\mu(F)=\nu(vF)\) 满足 \(\mu(1)=1\)，并且

\[
\mathcal L_{t,\zeta}\bigl(v(F\circ\sigma^+)\bigr)
 =F\mathcal L_{t,\zeta}v=\lambda Fv
\quad\Longrightarrow\quad
\mu(F\circ\sigma^+)=\mu(F).
\tag{10}
\]

若 \(0<m\le v\le M\)，正性还给

\[
\frac mM\lambda^n\le\mathcal L_{t,\zeta}^n1(x)
\le\frac Mm\lambda^n.
\tag{11}
\]

因此本页的 \(\lambda\) 等于 \(\lim_n\|\mathcal L_{t,\zeta}^n1\|_\infty^{1/n}\)。这些都是新 beta、新代表上满足定理前提后的结论，不是用范数连续性从旧端点空间追认 RPF。

## 4. 简单谱分支与局部全纯压力

取任意实基点 \((t_0,\zeta_0)\)，令 \(L_*\) 和 \(\lambda_*>0\) 为 (9) 的算子与简单本征值。选以 \(\lambda_*\) 为中心的小圆 \(\Gamma\)，内部只有这个谱点且不含零。沿 \(\Gamma\) 的基准 resolvent 有统一界。由 (6)，参数足够接近基点时有范数收敛的 Neumann 展开

\[
(zI-L)^{-1}=(zI-L_*)^{-1}
\sum_{k\ge0}\bigl[(L-L_*)(zI-L_*)^{-1}\bigr]^k.
\tag{12}
\]

故 Riesz 投影

\[
\Pi(s,\zeta)=\frac1{2\pi i}\int_\Gamma(zI-\mathcal L_{s,\zeta})^{-1}\,dz
\tag{13}
\]

联合全纯。缩域使 \(\|\Pi-\Pi_*\|<1\)，投影的像与基准一维像同构，故秩仍为一。固定基准左右本征对象 \(v_*,\nu_*\)，\(\nu_*(v_*)=1\)，定义

\[
v(s,\zeta)=\frac{\Pi(s,\zeta)v_*}{\nu_*(\Pi(s,\zeta)v_*)},
\qquad \lambda(s,\zeta)=\nu_*(\mathcal L_{s,\zeta}v(s,\zeta)).
\tag{14}
\]

分母在基点为 1；该式构造全纯本征向量及本征值，而非仅说“存在谱扰动定理”。令 \(\nu(s,\zeta)=\nu_*\Pi(s,\zeta)\)，则 \(\nu(v)=1\)、\(\nu L=\lambda\nu\)。实参数附近 v 仍严格正，且共轭对称性使其为实函数，所以该 \(\lambda\) 与实 RPF 的唯一正主值相同，\(\nu\) 也为正 RPF 对偶对象的正倍数；它不必继续满足 \(\nu(1)=1\)，但 \(\nu(v)=1\) 已使 \(\mu(F)=\nu(vF)\) 成为概率。

因为 \(\lambda\) 不为零，可选唯一与基准实对数相容的局部支

\[
P(s,\zeta)=\operatorname{Log}\lambda(s,\zeta),\qquad
P(t_0,\zeta_0)=\log\lambda_*.
\tag{15}
\]

它是局部联合全纯函数。沿实参数重叠邻域，它们都是正主值的实对数，因此一致。**复参数处的 \(\lambda\) 是简单本征值的续延分支，不称为谱半径；(15) 更不是复函数 \(\log r(L)\)。** 本页也不声称存在整个复参数域的单值 Log。

## 5. 压力导数与唯一零点的局部全纯性

对任何参数方向 p，微分 \(Lv=\lambda v\)，再用当前点的 \(\nu\) 作用，利用 \(\nu L=\lambda\nu\) 和 \(\nu(v)=1\) 消去 v 的导数，得

\[
\partial_p\lambda=\nu((\partial_pL)v).
\tag{16}
\]

代入 (7)，得到本页关键符号：

\[
\boxed{\partial_sP(s,\zeta)=-\mu_{s,\zeta}(\widehat g_\zeta),\qquad
D_\zeta P(s,\zeta)[\delta]=-s\,\mu_{s,\zeta}(D\widehat g_\zeta[\delta]).}
\tag{17}
\]

复参数处 \(\mu\) 只是按 (14) 构造的复线性泛函；实参数处才使用其概率与正性。特别地，对所有实 t、实几何参数，

\[
-10a_0\le\partial_tP(t,\zeta)\le-2a_0<0.
\tag{18}
\]

由于 \(\mathcal L_{0,\zeta}1=2\)，\(P(0,\zeta)=\log2\)。对 \(t\ge0\)，从每点两前像、(3) 和正对偶测度得到

\[
2e^{-10a_0t}\le\lambda(t,\zeta)\le2e^{-2a_0t},\qquad
\log2-10a_0t\le P(t,\zeta)\le\log2-2a_0t.
\tag{19}
\]

结合局部解析性给出的连续性及 (18)，每个实几何参数恰有一个实零点，且

\[
P(h(\zeta),\zeta)=0,\qquad
\frac{\log2}{10a_0}\le h(\zeta)\le\frac{\log2}{2a_0}.
\tag{20}
\]

负 t 不可能有额外零点，因为 P 严格递减且 \(P(0)>0\)。

固定 \(h_0=h(\zeta_0)\)。由 (18)，\(P_s(h_0,\zeta_0)\ne0\)。在已选全纯支内取一个以 \(h_0\) 为中心的小 s 圆盘，使基准 P 在其中只有这个简单零点且边界不为零。缩小复几何邻域，边界上的统一微小变化与 Rouché 定理使每个 P 都恰有一个零点；它由

\[
h(\zeta)=\frac1{2\pi i}\int_{\partial D}
 s\,\frac{P_s(s,\zeta)}{P(s,\zeta)}\,ds
\tag{21}
\]

给出，因而全纯。这也是解析隐函数结论的一个明确构造。复零点仅在所选小圆盘内唯一；实切片与 (20) 的唯一实零点一致，所以 h 实解析。

## 6. 几何导数符号及非循环的形状接口

微分 \(P(h(\zeta),\zeta)=0\)，再使用 (17)，得

\[
\boxed{Dh(\zeta)[\delta]
=-h(\zeta)\,
\frac{\mu_{h(\zeta),\zeta}(D\widehat g_\zeta[\delta])}
     {\mu_{h(\zeta),\zeta}(\widehat g_\zeta)}.}
\tag{22}
\]

注意前面是负号，并且有因子 h。分母至少 \(2a_0\)。这里没有漏掉测度导数；(16) 已由谱微分给出一阶导数公式，而不是把 \(P=\mu(-s\widehat g)\) 这个错误等式拿去微分。

对实参数，把一侧不变概率 \(\mu\) 提升为双向不变概率 \(\overline\mu\)：任意双向区间 \([j,k]\) 的柱集概率定义为对应长度 \(k-j+1\) 的一侧柱集概率；\(\sigma^+\)-不变性保证这些有限分布相容。有限字母柱集由此给唯一双向不变扩张，且 \(\pi_*\overline\mu=\mu\)。由 (3) 及其 Banach 值可微性，

\[
\mu(\widehat g_\zeta)=\int\tau_\zeta\,d\overline\mu,\qquad
\mu(D\widehat g_\zeta[\delta])=\int D\tau_\zeta[\delta]\,d\overline\mu.
\tag{23}
\]

右侧测度取当前基点，积分共边界及其参数导数均为零。这不是对参数变动的积分错误地冻结测度，而是把 (22) 已经得到的积分量改写为物理 roof 的量。

**条件式伴随接口，不构成主证明依赖。** [真实形状首变分笔记][shape]由另一分支负责；仅当采用其逐点命题

\[
D\tau_\zeta[\delta]=-2\chi_0K_\delta+H_\delta\circ\sigma-H_\delta,
\quad K_\delta=n_0\cdot\delta C_{x_0}+\delta a_{x_0},
\tag{24}
\]

其中 n 为盘外法向、\(\chi_0=-v_0^-\cdot n_0=v_0^+\cdot n_0>0\)、\(H_\delta=v_0^-\cdot\delta q_0\)，才将 (17)、(22)–(23) 合成为

\[
D_\zeta P(s,\zeta)[\delta]=2s\int\chi_0K_\delta\,d\overline\mu_{s,\zeta},
\qquad
Dh[\delta]=2h\,
\frac{\int\chi_0K_\delta\,d\overline\mu_{h,\zeta}}
     {\int\tau_\zeta\,d\overline\mu_{h,\zeta}}.
\tag{25}
\]

该符号已与该分支直接对齐；本页不重复或冒称独立认证其形状证明。特别地，条件 (24) 下固定圆心共同增大半径给 \(Dh>0\)。主压力零点论证 (1)–(23) 不依赖 (24)，所以两份笔记互引不是证明循环。

## 7. 整体尺度律：由真实几何与固定规范直接证明

现在专取等边三盘整体缩放子族 \(C_i(a)=aC_i(1)\)、所有半径为 a，单位飞行速率不变。此处 a 是变量，不再是 §1 的固定 \(a_0\)。正实缩放保持反射、首次飞行和 code，唯一配置给

\[
Q_j(a,x)=aQ_j(1,x),\qquad \tau_a(x)=a\tau_1(x).
\tag{26}
\]

这也可直接由几何同步更新 \(\mathscr P_a(aq)=a\mathscr P_1(q)\) 核对。固定相同 R、相同 \(N_*\) 和符号度量；稳定纤维求和及有限平均都是关于 tau 的线性操作，因此

\[
\widehat g_a=a\widehat g_1,\qquad
\mathcal L_{s,a}=\mathcal L_{as,1}.
\tag{27}
\]

即便尺度 1 不在原局部复邻域内，也可沿这条精确缩放子族用同一固定构造定义它；\(\widehat g_1=\widehat g_{a_0}/a_0>0\)，所有正 a 仍可在同一符号空间应用实 RPF。不需要将一般复几何邻域无限延拓，也不把 \(N_*\) 随 a 重新取整。

由相同算子和唯一正主值，实压力满足 \(P(s,a)=P(as,1)\)，因此

\[
\boxed{h(a)=h(1)/a=a_0h(a_0)/a,\qquad h'(a)=-h(a)/a.}
\tag{28}
\]

代入 (22) 的 \(\partial_a\widehat g_a=\widehat g_a/a\) 得到同一负号。这个尺度律不需要先把 h 识别为流熵。

## 8. 在新空间重建基准严格下降

本节只为 §9 的开放性提供当前 \(\mathcal B\) 上的基准，不能援引旧 beta 空间的严格谱下降作为结论。令 \(\zeta=0\)，以下 g 均指 \(\widehat g_0\)，并重取

\[
D=[g]_\beta q/(1-q),\quad K_s=3+2|s|D,\quad
B_n(t)=\|\mathcal L_{t,0}^n1\|_\infty.
\tag{29}
\]

同一长度 n 共同前缀上的 Birkhoff 权重差逐项求和给 \(|S_ng(wx)-S_ng(wy)|\le D(1-q^n)d_\theta^+(x,y)^\beta\)。用实线段积分估计两个复指数的差，配对相同首字母的分支，异首字母用上确界，便在新 q、新 D 下得到

\[
\|\mathcal L_{s,0}^nu\|_\infty\le B_n(\operatorname{Re}s)\|u\|_\infty,
\quad
\|\mathcal L_{s,0}^nu\|_\beta
\le B_n(\operatorname{Re}s)(q^n[u]_\beta+K_s\|u\|_\infty).
\tag{30}
\]

令 \(P_m\) 在每个长度 m 柱集上取固定代表点的值。它有限秩，且 \(\|u-P_mu\|_\infty\le q^m[u]_\beta\)、\([P_mu]_\beta\le[u]_\beta\)、\([(I-P_m)u]_\beta\le2[u]_\beta\)。代入 (30)，

\[
\|\mathcal L_{s,0}^n-\mathcal L_{s,0}^nP_m\|
\le B_n(\operatorname{Re}s)(2q^n+K_sq^m).
\tag{31}
\]

先令 m 趋无穷，再取 n 次根；由 (11) 及 [Hennion Corollaire 5.3(ii)][hennion] 的紧算子距离公式，得到

\[
r(\mathcal L_{t+ib,0})\le\lambda(t,0),\qquad
r_{\rm ess}(\mathcal L_{t+ib,0})\le q\lambda(t,0).
\tag{32}
\]

若第一式对 b 非零取等，因为 \(q<1\)，此反设下存在外围本征函数；使用的是 [Hennion Proposition 3.1][hennion] 的有限维外围谱结论，并非预先宣称所有复参数都有 \(r_{\rm ess}<r\)。除以本页 §3 在新空间得到的正本征函数 v，方程变成正概率的复加权平均。

具体地，令 \(p(y\mid x)=e^{-tg(y)}v(y)/(\lambda v(x))>0\)，其对两前像求和为 1。归一化本征函数的模达到最大值时，每个前像都须达到同一最大值；全部有限前像稠密，因为任意柱词末字母与目标尾首字母之间都能插入一个同时不同于二者的第三字母。连续性给模处处为正常数，再由三角等号条件得到逐点关系

\[
e^{ibg}=e^{i\phi}\frac{F}{F\circ\sigma^+},\qquad |F|=1,
\tag{33}
\]

其中常相位 \(\phi\) 任意。由 (3)，新 g 的周期和仍是[真实第三周期笔记][periods]的

\[
T_2=8a_0,\quad T_3=(18-3\sqrt3)a_0,\quad
T_4=4a_0(\sqrt{37-6\sqrt3}-1).
\tag{34}
\]

该笔记 §3–4 已用精确代数证明 \((T_4-2T_2)/(2T_3-3T_2)\notin\mathbb Q\)。沿三周期相乘 (33) 后消去常相位，必得

\[
b(2T_3-3T_2)=2\pi(2m_3-3m_2),\qquad
b(T_4-2T_2)=2\pi(m_4-2m_2).
\tag{35}
\]

第一式左端非零，两个等式的比值与上述无理性矛盾。于是现在是在**当前较小 beta、新正代表的算子**上证明

\[
\boxed{r(\lambda(t,0)^{-1}\mathcal L_{t+ib,0})<1
\quad(t\in\mathbb R,\ b\ne0).}
\tag{36}
\]

这里复用了实际周期的几何事实，而没有复用另一个 Banach 空间的谱判断。

## 9. 任意固定紧频带对小实几何扰动开放

本节 \(|\zeta|\) 取参数空间中固定的 Euclidean 范数。固定紧区间 \(I\subset\mathbb R\) 及 \(0<\delta_b\le B_b<\infty\)，置

\[
K_0=I\times\{b:\delta_b\le|b|\le B_b\},\qquad
A_{t,b,\zeta}=\lambda(t,\zeta)^{-1}\mathcal L_{t+ib,\zeta}.
\tag{37}
\]

实 RPF 正主值由 §4 的局部支和唯一性在重叠处相容，故 \(\lambda(t,\zeta)>0\) 对实 \((t,\zeta)\) 连续；结合 (6)，A 在同一算子范数中连续。对任意有界算子，\(r(A)=\inf_{n\ge1}\|A^n\|^{1/n}\)，故谱半径上半连续。紧性与 (36) 给 \(r_*:=\max_{(t,b)\in K_0}r(A_{t,b,0})<1\)。

选 \(r_*<\kappa<1\)。对每个基准 \(p=(t,b)\in K_0\)，存在整数 \(n_p\ge1\) 使 \(\|A_{p,0}^{n_p}\|<\kappa^{n_p}\)。这项有限幂严格不等式在 p 的邻域及一个实几何邻域内保持。取覆盖 \(K_0\) 的有限子集，将这些几何邻域取交，得到共同 \(\varepsilon>0\) 及有限块长 \(n_1,\ldots,n_J\)。

进一步缩小 epsilon，使闭实几何球仍在上述邻域中。令 \(N=\max_j n_j\)、\(D_*=\max(1,\sup_{K_0,|\zeta|\le\varepsilon}\|A_{t,b,\zeta}\|)<\infty\)。对每个**固定参数算子**选其覆盖块长 \(n_j\)，写 \(n=kn_j+r\)、\(0\le r<n_j\)，则

\[
\|A_{t,b,\zeta}^n\|\le\kappa^{kn_j}D_*^r
\le(D_*/\kappa)^{N-1}\kappa^n.
\tag{38}
\]

因此存在 C 有限，

\[
\boxed{\sup_{t\in I,\ \delta_b\le|b|\le B_b,\ |\zeta|\le\varepsilon,\ \zeta\ \mathrm{real}}
\|\lambda(t,\zeta)^{-n}\mathcal L_{t+ib,\zeta}^n\|
\le C\kappa^n.}
\tag{39}
\]

它也给归一化逆 \(\|(I-A_{t,b,\zeta})^{-1}\|\le C/(1-\kappa)\)。取 I 包含 (20) 的区间，便可代入 \(t=h(\zeta)\)，此时 \(\lambda=1\)，得到压力零点线上同一有限频带的幂界。

这里没有交换 n 极限与参数上确界，也没有断言变化参数算子任意乘积满足 (39)。\(\varepsilon,C,\kappa\) 依赖 I、\(\delta_b,B_b\)，不能延拓为全部非零频率共用一个邻域与常数。特别地，**没有假设扰动后三周期比仍无理**：无理性本身不是开放条件；固定频带的结论来自新空间中的算子范数连续性和有限幂开覆盖。

## 10. 结论层级、来源与实际操作

本页闭合的是新空间 RPF、局部全纯谱压力及其零点、符号核准的几何一阶响应、精确尺度律，以及任意预选有限非零频带的小几何开放性。它不提供高频统一估计、零频方差、完整 zeta 延拓、物理散射 resolvent、核性、跡公式、Fredholm／quantum determinant 或 Hilbert–Pólya 身份。

若后续要把 h 称为真实流熵，须另外核读适用的正连续 roof 悬挂压力—熵定理，核对所用压力的标准识别、双／单侧关系及真实时间保持编码。这些不是将“pressure zero”换个名字就自动完成；本页不使用该身份。

本次实际普通浏览成功核读 Stoyanov arXiv:1703.04276v1 的 §1 和 Theorem 2.1(a)–(d)，以及 Hennion 的 Proposition 3.1、Corollaire 5.3(ii)；只将这些定理所述内容作为外部输入。Cambridge 同文 PDF 的本次直接打开超时，随后使用作者 arXiv 稿成功读取，未把失败访问冒称成功。没有重试受限全文或上传私人材料。

本地读取了共同几何全纯笔记、新旧一侧／固定频带笔记及实际第三周期相位论证。形状公式通过与负责分支直接对齐外法向、入／出射角和共边界符号后，仅以 (24) 的条件接口纳入；伴随文件落盘后又读取其 §5–6 的逐点式及条件接口，未据此宣称独立复核整份几何证明。主压力证明不依赖伴随文件的完成状态。ARS 的有限理论分析要求用于保持这些证据层级、参数量词与未识别熵的边界。

写前 `test ! -e` 确认本目标不存在，以 `apply_patch` 仅新建本文件；不运行科学、符号或数值程序、实验、枚举、artifact writer、构建或正式验证器，不改 Route／Stage 或历史失败记录。写后只做文本、行数、公式分隔与本地链接检查；其通过不认证数学成立性。

[geometry]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_joint_geometry_holomorphy_20260909.md
[one-sided]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[periods]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_third_period_and_phase_obstruction_20260909.md
[shape]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_physical_period_shape_derivative_20260909.md
[rpf]: https://arxiv.org/pdf/1703.04276
[hennion]: https://www.numdam.org/item/PSMIR_1995___2_A6_0.pdf
