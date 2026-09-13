# All-period resonance boundary: bounded mathematical preflight

日期：2026-09-06。仅新增本文件；不改已停止第五候选及其有效数学文件，不重新评价旧门槛。

## 结论、Claim 与 Status

**数学状态：PROVABLE AS STATED（以下精确公式）。选题处置：短推论 STOP。**

推广并非把旧柱面的系数整体乘上占用因子：一般周期占用还引入一个斜投影的秩一修正，使 leading determinant 通常依赖四个 Fourier 坐标。但这个修正可由一个行列式为一的左剪切和一个 $2\times2$ 行列式完整计算，不需要新的轨道构造、谱估计或高阶奇点理论。去掉已接受的父证明后，实质增量约为 2–4 页推论级代数，不应自动用于补足第五候选的正文长度。

本轮使用 `proof-writer`，区分下列完整证明与没有开展的高阶研究。没有浏览综述，没有重审旧文件，没有启动论文项目或给 PASS。

## 输入、假设与记号

已核读以下实际输入；哈希与指定值一致：

- [Main V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md)：`f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0`。
- [固定宏周期一的 boundary 补充](PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md)：`c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9`。
- [该补充的独立数学检查](PAPER29_CYCLIC_HENON_BOUNDARY_INDEPENDENT_CHECK_20260906.md)：`9e1c22e0182d79398ce50ee840b56b62cb6823a69e5cdba3473af88645a8150c`。

固定 $6\mid k$，相位指标为 $j\in\mathbb Z/k\mathbb Z$，映射保持为
$$
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\qquad
H_c(x,y)=(x^2+c-y,x),\qquad c_j=\epsilon^{-2}(u_j-1).
$$
任意指定正宏周期向量 $\boldsymbol n=(n_i)$，仍选 main 的原字：第 $i$ 行在 $n_i\ge2$ 时有唯一全正块，其余块只在相位 $i$ 为负；$n_i=1$ 时选唯一单负块。置
$$
a_i=\begin{cases}1,&n_i=1,\\1-1/n_i,&n_i\ge2,\end{cases}
\quad D_a=\operatorname{diag}(a_i),\quad
w=D_a^{-1}\mathbf1,\quad W=\mathbf1^Tw,
$$
$$
P(a)=\left(\prod_i a_i\right)W
=\sum_i\prod_{j\ne i}a_j.
$$
这些是实际宏周期字的占用数；$1/2\le a_i\le1$、$1\le w_i\le2$。定义
$$
K_{ij}=\frac1{n_i\rho_i}\partial_{u_j}\rho_i,
\qquad
D_{\boldsymbol n}(\epsilon,v)
=\epsilon^{-(k+1)}\det K(\epsilon,\epsilon v).
\tag{1}
$$
先在 $u$ 中求导，再代入 $u=\epsilon v$。本文件不将 $K$ 改成 $v$-微分。

用以下 Fourier 坐标区分基本共振频率与倍频：
$$
V_\pm=\frac1k\sum_jv_j e^{\mp i\pi j/3},\qquad
Z_\pm=\frac1k\sum_jv_j e^{\mp2\pi i j/3},
\qquad
\omega_\pm=\frac1W\sum_jw_j e^{\mp i\pi j/3}.
\tag{2}
$$
因 $w$ 为实正向量，$\omega_-=\overline{\omega_+}$；但 $v$ 是复参数，不对 $V_\pm,Z_\pm$ 施加共轭限制。

**精确结论。** 对每个固定 $k$ 和所有上述周期向量，(1) 在每个有界 $v$-集上联合全纯延拓到 $\epsilon=0$，并有
$$
\boxed{
D_{\boldsymbol n}(0,v)
=-\frac{3k^2}{32}P(a)\,\mathcal P_a(v),}
\tag{3}
$$
其中
$$
\boxed{
\begin{aligned}
\mathcal P_a(v)={}&1-4Z_+Z_-
 +2(\omega_+V_-+\omega_-V_+)\\
&+4(Z_+\omega_-V_-+Z_-\omega_+V_+).
\end{aligned}}
\tag{4}
$$
对较小紧集，余项 $D_{\boldsymbol n}(\epsilon,v)-D_{\boldsymbol n}(0,v)=O_k(\epsilon)$ 可取周期一致的界。常数允许依赖该紧集及 $k$。

## 证明策略与依赖

父证明已给实际周期分支、谱的联合全纯性及周期一致的二阶 $C^1$ jet。本轮只做三步：保留移动零阶行的 $Q(u)$ 修正；将 $w$ 方向用一个显式左剪切移回常数方向；计算所得两模块的行列式。最后的实际零曲线仍使用同一个全纯隐函数论证。

## Proof

### 1. 占用线性与继承的 jet

令 $J=\mathbf1\mathbf1^T$、$G(u)_{i,\cdot}=d_uh_i$，其中
$$
h_i=\frac{\sqrt{1-u_i}}2
\bigl((1-u_{i-1})^{-1}+(1-u_{i+1})^{-1}\bigr).
$$
父证明给出
$$
K=\mathbf1g_0(u)+\epsilon(J-2D_a)G(u)
 +\epsilon^2T_a(u)+O(\epsilon^3),
\tag{5}
$$
$$
g_0(u)_j=-\frac1{2(1-u_j)},\quad
G(0)=C=\frac12(S+S^{-1}-I),\quad
T_a(0)=-\frac14J+D_aB,
$$
$$
B=-\frac32I+\frac54(S+S^{-1})-(S^2+S^{-2}).
$$
二阶占用线性在宏块边界也成立：当 $k\ge3$，每个相邻或距离二符号对最多有一个端点处于负号相位 $i$。故第 $i$ 行相对于全正字的一、二阶偏差分别为
$$
-2a_i h_i,\qquad
-2a_i(E_{i-1}+E_i+D_{i-1}+D_{i+1}),
$$
这里 $E,D$ 是 main 的相关系数函数，不是本文件的矩阵 $D_a$。这解释了 (5) 的 $a_i$ 依赖，没有把长周期字当成常值字。余项继承 main 的周期一致估计。

### 2. 必须使用斜投影：保留 $Q(u)$ 项

令 $q_0=\mathbf1/\sqrt k$，$R$ 为频率 $\pm\pi/3$ 的两模空间，$\Pi_R$ 为其 Fourier 投影。先提出 $D_a$：
$$
D_a^{-1}K=w g_0(u)+\epsilon(w\mathbf1^T-2I)G(u)
 +\epsilon^2\left(-\tfrac14w\mathbf1^T+B\right)+O(\epsilon^3)
\tag{6}
$$
是在 $u=\epsilon v$ 下足够精确的展开。

使用 boundary 中同一列变换
$$
\widetilde q(u)=q-q_0\frac{g_0(u)q}{g_0(u)q_0},\qquad
\widetilde q(\epsilon v)=q-\epsilon r_q q_0+O(\epsilon^2),
\quad r_q=\frac{v^Tq}{\sqrt k}.
$$
它精确消去 $g_0(u)$，且不改变 Fourier 列矩阵的行列式。记 $H=G'(0)[v]$。对 $q\in R$，除去 $\epsilon^2$ 的完整列极限为
$$
Y(q)=\tfrac34q+(w\mathbf1^T-2I)Hq
 -r_q\left(\tfrac{\sqrt k}{2}w-q_0\right).
\tag{7}
$$
最后一项来自移动零阶行，不能省略。

常数输入列的输出极限现在沿 $w$ 而不是沿 $q_0$。取
$$
L_a=I-\frac{(w-(W/k)\mathbf1)\mathbf1^T}{W}.
\tag{8}
$$
则 $L_aw=(W/k)\mathbf1$，$L_a$ 在 $\mathbf1^\perp$ 上是恒等，且 $\det L_a=1$；后者由 $\mathbf1^T(w-(W/k)\mathbf1)=0$ 得到。其逆把 (8) 中的负号换为正号，故在 $w_i\in[1,2]$ 上一致有界。

因此正确的两模商投影是
$$
\Pi_RL_a=\Pi_R-\frac{(\Pi_Rw)\mathbf1^T}{W},
\tag{9}
$$
它消去 $w$ 和所有非共振的零和 Fourier 模，不能替换成旧的 $\Pi_R$。

由 boundary 的 Hessian 恒等式，对每个 $q\in R$ 有
$$
(Hq)_i=v_{i-1}q_{i-1}+v_{i+1}q_{i+1}
-\tfrac14(v_{i-1}+v_{i+1})q_i-\tfrac12v_iq_i,
$$
从而在求和并使用 $q_{i-1}+q_{i+1}=q_i$ 后，
$$\mathbf1^THq=\tfrac54v^Tq.\tag{10}$$
将 (7) 代入 (9)，得到实际有效两模块
$$
\boxed{R_a(v)q=R_0(v)q+
\frac{3}{2W}(\Pi_Rw)(v^Tq),}
\tag{11}
$$
其中 $R_0=\tfrac34I_R-2\Pi_RH|_R$ 是旧全周期一的块。
具体地，额外系数是
$2\mathbf1^THq-v^Tq=\frac32v^Tq$。
若错误地删去 $Q(u)$ 项，会得到错误系数 $5/2$；若错误地用正交投影，则会漏掉整个修正。

### 3. 显式两模块与完整行列式

在单位 Fourier 基 $(q_+,q_-)$ 中，(11) 变成
$$
\boxed{R_a(v)=\frac34
\begin{pmatrix}
1+2\omega_+V_-&-2Z_++2\omega_+V_+\\
-2Z_-+2\omega_-V_-&1+2\omega_-V_+
\end{pmatrix}.}
\tag{12}
$$
其行列式为 $\frac9{16}\mathcal P_a(v)$；两个占用修正的二次乘积相消，直接展开即得 (4)。

将 $L_aD_a^{-1}K$ 乘以 $Q(\epsilon v)$，再将非共振非常数列除以 $\epsilon$、两共振列除以 $\epsilon^2$。父证明的联合全纯 jet 保证该矩阵全纯延拓，余项在有界 $v$-集上周期一致。其 Fourier 极限是上三角分块：补空间对角元为
$$
-W/2,\qquad
\ell_\nu=1-2\cos(2\pi\nu/k)
\quad(\nu\ne0,k/6,5k/6),
$$
右下块为 (12)。非零右上耦合可以存在，但左下块为零；有限 $\epsilon$ 时左下块是 $O(\epsilon)$，补空间逆一致有界。因此正确 Schur 补为 $R_a(v)+O(\epsilon)$，不需要逆掉可能奇异的 $R_a$。

利用已证乘积 $\prod\ell_\nu=k^2/3$，再恢复行因子 $\det D_a=\prod a_i$，得到
$$
\left(\prod a_i\right)
\left(-\frac W2\right)\frac{k^2}{3}
\frac9{16}\mathcal P_a(v)
=-\frac{3k^2}{32}P(a)\mathcal P_a(v).
$$
这证明 (3)，包括归一化、符号、全纯延拓和统一余项。证毕。

## 实际含义与最小反例

只有当 $\omega_+=\omega_-=0$ 时，leading 函数才退回原来的两 Fourier 坐标柱面。这个条件比“全部周期相同”更一般，是 $w$ 的基本共振 Fourier 分量消失；不能将任意非恒定占用都视为不平衡。

一般不平衡占用下，leading 函数已经依赖 $V_\pm,Z_\pm$ 四个坐标。例如取 $n_0=2$、其余 $n_i=1$，则 $w_0=2$、其余 $w_i=1$，所以
$$
\omega_+=\omega_-=\frac1{k+1}.
$$
沿 $v_j=t\cos(\pi j/3)$，有 $Z_\pm=0$、$V_\pm=t/2$，于是
$$\mathcal P_a(v)=1+\frac{2t}{k+1}.\tag{13}$$
其简单零点 $t=-(k+1)/2$ 是额外耦合的直接见证：旧的两坐标公式在此会错误地给出常数一。

当 $\omega_\pm\ne0$ 时，(12) 从四个 Fourier 参数到四个矩阵条目是可逆仿射变换。因此完整 leading 零集是一个平移后的标准 $2\times2$ 行列式二次锥，再乘其余自由坐标；这仍是有限维代数的直接后果。本轮不分析锥顶在高阶项下的实际奇点或解消。

在任何满足 $\mathcal P_a(v_*)=0$、$d_v\mathcal P_a(v_*)\ne0$ 的有限点，(3) 的全纯延拓与隐函数定理给出实际局部退化超曲面。这里不声称实际有限 $\epsilon$ 的函数完整地只依赖四个 Fourier 坐标；更高阶项可依赖其余参数和完整周期字。旧全周期一结果同样只把两坐标结论用于 leading 函数。

特别地，沿原曲线 $v_j=t\cos(2\pi j/3)$，有 $V_\pm=0$、$Z_\pm=t/2$，所以对**每个**周期向量都仍有
$$\mathcal P_a(v)=1-t^2.\tag{14}$$
由周期一致余项及 $P(a)\ge k/2^{k-1}$，在 $t=\pm1$ 两个固定小圆上可统一应用 Rouché 定理及简单零点的隐函数定理，得到
$$
t_{\boldsymbol n,\pm}(\epsilon)=\pm1+O_k(\epsilon)
$$
的实际全纯零曲线，半径和误差可取周期一致。简单零点的行列式导数非零，故曲线上选定矩阵秩恰为 $k-1$；原宏周期轨道仍然 exact、disjoint、simple，且迹非零。这仍只否定该周期向量的同一组选词在固定 $u$-邻域内处处满秩，不否定换词，也不证明最优域。

## 新义务、证据等级与停止点

本轮真正新增的义务是处理 (9) 的斜投影，并保留 (7) 的移动零阶修正。其余证明全部使用已通过的二阶 jet、紧占用区间、一个 $2\times2$ 行列式及简单零点的全纯延拓。

额外四坐标依赖是正确的结构差分，但不是新的分析机制。实际高阶奇点、全部选词的内在谱秩、一般次数等问题均未展开，也不能把未做的问题计为本结果内容。

只读 CAS 曾在 $k=6$、$w=(2,1,1,1,1,1)$、
$v_j=x\cos(\pi j/3)+y\cos(2\pi j/3)$ 检查过符号：有效块为
$\operatorname{diag}(3/4+3x/14-3y/4,\,3/4+3y/4)$，与 (12) 一致。
全部一般量词由上面的代数证明承担，而不是由这项排错承担。

**最终处置：短推论 STOP。** 可以保留这份正确公式供后续工作避免误用正交 Schur，但不升级旧候选、不重新打开其篇幅门槛，也不自动启动正式写作。仅本文件被新增。
