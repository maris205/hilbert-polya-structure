# 一般宏周期边界与余秩二临界集：独立数学检查

日期：2026-09-06。仅检查新增数学，不重开第五候选已经完成的 FAIL，不重新评分长文新意、价值或页数门。

## Claim：输入与所检查的精确命题

已完整读取 [一般周期边界 preflight](PAPER29_ALL_PERIOD_BOUNDARY_PREFLIGHT_20260906.md)，230 行，并实际核验 SHA-256：

    f39d735da4ba02802e3baa570c043260f4424898e186f9d671696e81b345ffc9

落定前另完整读取随后交付的实际作者稿 [余秩二临界集证明](PAPER29_CORANK_TWO_TRACE_BOUNDARY_PROOF_20260906.md)，217 行，并实际核验 SHA-256：

    f86ef7dd30e98f296abe7b1603dfd6a2e916e8d86382e9cb46dae0d6093b6e21

它将最初消息中的新推论写成实际证明，并明确补入平衡占用的有界尺度对照。本报告最终绑定以上两件实际作者输入，而非仅检查一个消息草图。

所用父输入为已独立通过的 [Main V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md) 与 [固定点边界](PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md)，本轮核验其 SHA-256 分别为：

    f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0
    c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9

两份已有独立数学检查是父依赖证据，不是本轮重新执行的项目：

- [Main 独立检查](PAPER29_CYCLIC_HENON_JET_INDEPENDENT_CHECK_20260905.md)，绑定 SHA-256 为 ff0144b1324cbdd25718ed017ea3a03611cd84882cd7c6d89abd3ce9b194d984。
- [固定点边界独立检查](PAPER29_CYCLIC_HENON_BOUNDARY_INDEPENDENT_CHECK_20260906.md)，绑定 SHA-256 为 9e1c22e0182d79398ce50ee840b56b62cb6823a69e5cdba3473af88645a8150c。

本轮需要判定：

1. 任意指定宏周期选字下，重标度行列式的四 Fourier 坐标公式是否正确。
2. 非常数占用的斜投影、移动公共行修正与有效块中 $3/2$ 系数是否完整。
3. 重标度余项以及原余弦线上的实际简单零曲线是否对周期一致，曲线上原矩阵是否恰有秩 $k-1$。
4. **另列的余秩二作者稿**：当占用基本频率不消失时，是否可从实际 Schur 条目得到真实余秩二流形与行列式临界超曲面的精确二次锥局部式；平衡占用时，是否排除固定有界重标度域内的余秩二点。这个推论不是输入 preflight 已经证明或已经过审的内容，本报告在后文独立给出其证明。

本人不是两份新输入的作者。完整读取 proof-writer 技能后，采用其“命题—假设—依赖—完整证明—边界”框架，仅新建本报告；不编辑作者稿、旧候选评价、锁、索引或其他检查。实际方法是独立代理手算有限维代数与全纯论证，无 CAS、数值实验或外部写入，也未读取另一项新选词证明。

## Status

**原 preflight 的数学结论：PROVABLE AS STATED。**

**新增余秩二作者稿：PROVABLE AS STATED。** 其原矩阵秩与原行列式单位表述已明确限于固定非零 $\epsilon$。对包含 $\epsilon=0$ 的联合全纯族，单位乘二次锥的对象必须是已除去 $\epsilon^{k+1}$ 的行列式；原行列式仍有这个额外因子。后文精确列出两种恒等式，不把它们混用。

没有发现需要修正 preflight 系数、符号或量词的实质错误。新增余秩二推论是实际 Schur 块加全纯逆/隐函数定理的短后果，不是新的普遍奇点理论或原迹映射的 fold 分类。

## Assumptions

- 工作于复数域，固定 $k\ge6$ 且 $6\mid k$；所有常数允许依赖 $k$。
- 固定的正整数宏周期向量为 $\boldsymbol n=(n_i)_{i=0}^{k-1}$。选字与 Main V2 相同：负号只在本行相位出现，长周期具有唯一全正 marker。
- $a_i=1$ 若 $n_i=1$，否则 $a_i=1-1/n_i$；因此 $a_i\in[1/2,1]$。
- 先在原 $u$ 坐标求导，再在 $u=\epsilon v$ 处取值。$\epsilon$ 在求导过程中固定。
- 父证明提供实际周期分支、归一化谱行及其联合全纯、周期一致的二阶展开。只使用这个已通过的输入，不重新证明轨道收缩。
- 一般周期公式及余弦零曲线在每个有界 $v$ 域上作周期一致估计。新增余秩二推论则先固定周期向量并假定 $\omega_+\omega_-\ne0$；不声称其邻域或逆坐标在 $\omega_\pm\to0$ 时一致。

## Notation

令
$$
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},
\qquad H_c(x,y)=(x^2+c-y,x),
\qquad c_j=\epsilon^{-2}(u_j-1).
$$
对所选周期的返回迹 $\rho_i$，写
$$
K_{ij}=\frac1{n_i\rho_i}\partial_{u_j}\rho_i,
\qquad
D_{\boldsymbol n}(\epsilon,v)
=\epsilon^{-(k+1)}\det K(\epsilon,\epsilon v).
$$
占用记号为
$$
D_a=\operatorname{diag}(a_i),\qquad
w=D_a^{-1}\mathbf1,\qquad W=\mathbf1^Tw,\qquad
P(a)=\left(\prod_i a_i\right)W.
$$
于是 $1\le w_i\le2$、$k\le W\le2k$，且 $P(a)\ge k/2^{k-1}$。

单位 Fourier 列为 $q_\nu(j)=k^{-1/2}e^{2\pi i\nu j/k}$，常数列为 $q_0=\mathbf1/\sqrt k$。令
$$
q_+=q_{k/6},\qquad q_-=q_{5k/6},\qquad
R=\operatorname{span}\{q_+,q_-\}.
$$
$\Pi_R$ 表示正交 Fourier 投影，但涉及 $v$ 的转置配对仍是双线性 $v^Tq$，不把 $v$ 共轭。定义
$$
V_\pm=\frac1k\sum_jv_je^{\mp i\pi j/3},\qquad
Z_\pm=\frac1k\sum_jv_je^{\mp2\pi i j/3},\qquad
\omega_\pm=\frac1W\sum_jw_je^{\mp i\pi j/3}.
$$
四个 $V_\pm,Z_\pm$ 是独立复线性坐标，因为相应四个 Fourier 频率在每个 $6\mid k$ 时互异。由于 $w$ 实正，$\omega_-=\overline{\omega_+}$，因此两个 $\omega$ 同时为零或同时非零；$v$ 无对应实限制。

## Proof Strategy

先使用父展开，左乘 $D_a^{-1}$ 后把移动公共输出方向 $w$ 用行列式一的剪切搬回常模。完整保留 $Q(u)$ 的列修正，计算正确商投影下的两模块；再把其嵌入完整重标度矩阵证明行列式及统一误差。实际简单零曲线由统一 Rouché 计数和全纯 IFT 得到。最后独立处理新增余秩二推论，以实际 Schur 四条目建立可逆坐标。

## Dependency Map

1. 父二阶谱 jet、占用线性与周期一致余项，给出本轮实际矩阵展开。
2. $Q(u)$ 精确消去共同零阶行，$L_a$ 精确消去输出方向 $w$，给出斜投影。
3. Hessian 求和恒等式与 Fourier 配对，给出 $3/2$ 修正和四坐标多项式。
4. 补块可逆、列可除性、父全纯余项，给出实际 Schur 块及统一行列式估计。
5. 余弦线上的 $1-t^2$、统一余项、Rouché 与简单零点 IFT，给出实际秩 $k-1$ 曲线。
6. 在 $\omega_+\omega_-\ne0$ 下，四条目参数化可逆；参数化逆函数定理给出新增余秩二流形与精确局部式。

## Proof

### Step 1. 继承展开及其占用依赖

设 $J=\mathbf1\mathbf1^T$，$G(u)$ 的第 $i$ 行为 $d_uh_i$，其中
$$
h_i(u)=\frac{\sqrt{1-u_i}}2
\bigl((1-u_{i-1})^{-1}+(1-u_{i+1})^{-1}\bigr).
$$
父证明给出实际谱行的展开
$$
K=\mathbf1g_0(u)+\epsilon(J-2D_a)G(u)
 +\epsilon^2T_a(u)+O(\epsilon^3),
$$
$$
g_0(u)_j=-\frac1{2(1-u_j)},\quad
G(0)=C=\tfrac12(S+S^{-1}-I),\quad
T_a(0)=-\tfrac14J+D_aB,
$$
$$
B=-\tfrac32I+\tfrac54(S+S^{-1})-(S^2+S^{-2}).
$$
负号只在相位 $i$ 出现时，一个相邻或距离二符号对至多有一个端点为负；$k\ge6$ 保证这两个端点是不同相位。其均值偏差等于单负块偏差乘 $a_i$，即使符号对穿过宏块边界也成立。故一阶、二阶占用线性并未要求周期词为常词。

取值 $u=\epsilon v$ 后，$T_a(u)=T_a(0)+O(\epsilon)$ 在有界 $v$ 域上一致成立。左乘有界的 $D_a^{-1}$，得到供本轮使用的式子
$$
D_a^{-1}K=w g_0(u)+\epsilon(w\mathbf1^T-2I)G(u)
+\epsilon^2(-\tfrac14w\mathbf1^T+B)+O(\epsilon^3).
$$
这里第二阶矩阵替换仅在 $u=\epsilon v$ 后使用；没有把该替换错误地称为整个固定 $u$ 域上的三阶余项。

### Step 2. 移动列变换与输出斜投影

父列变换为
$$
\widetilde q_\nu(u)=q_\nu
-q_0\frac{g_0(u)q_\nu}{g_0(u)q_0}\quad(\nu\ne0).
$$
它精确消去 $g_0(u)$；将这些列和 $q_0$ 组成 $Q(u)$，有 $\det Q(u)=\det P$，其中 $P$ 是同序 Fourier 矩阵。

对于 $q\in R$，令 $r_q=v^Tq/\sqrt k$、$H=G'(0)[v]$。由于 $Cq=0$，
$$
\widetilde q(\epsilon v)=q-\epsilon r_q q_0+O(\epsilon^2).
$$
代入 Step 1，并用 $Bq=3q/4$、$Cq_0=q_0/2$，得到完整列极限
$$
Y(q)=\frac34q+(w\mathbf1^T-2I)Hq
-r_q\left(\frac{\sqrt k}{2}w-q_0\right).
\tag{A}
$$

写 $\delta=w-(W/k)\mathbf1$，定义
$$
L_a=I-\frac{\delta\mathbf1^T}{W}.
$$
因 $\mathbf1^T\delta=0$，矩阵 $N=\delta\mathbf1^T/W$ 满足 $N^2=0$，从而 $L_a^{-1}=I+N$、$\det L_a=1$。又有
$$
L_aw=(W/k)\mathbf1,\qquad
L_aq=q\quad\text{若 }\mathbf1^Tq=0.
$$
$L_a$ 及逆在 $w_i\in[1,2]$ 上一致有界。于是作用于输出商空间的正确投影是
$$
\Pi_RL_a=\Pi_R-\frac{(\Pi_Rw)\mathbf1^T}{W}.
\tag{B}
$$
它消去 $w$，也消去非共振的非常数 Fourier 列。若仍直接使用 $\Pi_R$，会把 $w$ 的共振分量错误保留。

### Step 3. 独立核对 $3/2$ 系数与四坐标块

父 Hessian 恒等式在 $q\in R$ 上为
$$
(Hq)_i=v_{i-1}q_{i-1}+v_{i+1}q_{i+1}
-\tfrac14(v_{i-1}+v_{i+1})q_i-\tfrac12v_iq_i.
$$
求和时，前两项总和是 $2v^Tq$；第三项为
$$
-\tfrac14\sum_i v_i(q_{i-1}+q_{i+1})=-\tfrac14v^Tq,
$$
这里用了共振关系 $q_{i-1}+q_{i+1}=q_i$。故
$$
\mathbf1^THq=\tfrac54v^Tq.
\tag{C}
$$
将 (A) 代入 (B)，所有 $w$ 方向项消失，剩下
$$
\begin{aligned}
\Pi_RL_aY(q)
&=\tfrac34q-2\Pi_RHq
 +\frac{\Pi_Rw}{W}\left(2\mathbf1^THq-v^Tq\right)\\
&=R_0(v)q+\frac{3}{2W}(\Pi_Rw)(v^Tq).
\end{aligned}
$$
这直接核验修正系数是 $3/2$。其中减去的 $v^Tq$ 恰来自 $Q(u)$ 修正，删去它会错误得到 $5/2$。

四个配对的归一化为
$$
q_\pm^*w=\frac{W}{\sqrt k}\omega_\pm,\qquad
v^Tq_+=\sqrt k V_-,\qquad v^Tq_-=\sqrt k V_+.
$$
代入父块 $R_0(v)$，得到
$$
R_a(v)=\frac34
\begin{pmatrix}
1+2\omega_+V_-&-2Z_++2\omega_+V_+\\
-2Z_-+2\omega_-V_-&1+2\omega_-V_+
\end{pmatrix}.
\tag{D}
$$
单位 Fourier 列的 $\sqrt k$ 因子在此完全抵消。展开两阶行列式，两个 $\omega_+\omega_-V_+V_-$ 项相消：
$$
\det R_a=\frac9{16}\mathcal P_a(v),
$$
$$
\mathcal P_a=
1-4Z_+Z_-+2(\omega_+V_-+\omega_-V_+)
+4(Z_+\omega_-V_-+Z_-\omega_+V_+).
\tag{E}
$$
这与输入的四坐标公式完全一致。

若 $\omega_\pm=0$，式 (E) 回到旧两坐标柱面；这不要求所有 $a_i$ 相同。若 $\omega_\pm\ne0$，在 $v=0$ 的两个 $V$ 导数就非零，故不能把四坐标依赖删去。输入的 $n_0=2$、其他 $n_i=1$ 例子给出 $W=k+1$、$\omega_\pm=1/(k+1)$；沿基本频率余弦线，$\mathcal P_a=1+2t/(k+1)$，其反例计算正确。

### Step 4. 完整矩阵、Schur 块及周期一致误差

令
$$
\Delta_\epsilon=\operatorname{diag}
(1,\epsilon^{\times(k-3)},\epsilon^2,\epsilon^2)
$$
按常模、非共振非常数模、两共振模排序。定义
$$
\mathcal A(\epsilon,v)
=P^{-1}L_aD_a^{-1}K(\epsilon,\epsilon v)
Q(\epsilon v)\Delta_\epsilon^{-1}.
\tag{F}
$$
每个非常数列的共同零阶项被 $Q$ 精确消掉。每个共振列的一阶系数在 $u=0$ 为零，因此代入 $u=\epsilon v$ 后又有一因子 $\epsilon$。由父全纯余项可知 (F) 全纯延拓，并在固定有界 $v$ 域上有周期一致的 $O(\epsilon)$ 误差。其系数导数的对应界在较小紧集上由 Cauchy 估计得到。

记 $U=R^\perp$，则
$$
\mathcal A(0,v)=
\begin{pmatrix}D_U&Z_a(v)\\0&R_a(v)\end{pmatrix},
\qquad
D_U=\operatorname{diag}\left(-W/2,(\ell_\nu)_{\nu\in U\setminus\{0\}}\right),
$$
$$
\ell_\nu=1-2\cos(2\pi\nu/k).
$$
常模的系数为 $-W/2$，因为 $-\sqrt k\,w/2$ 经 $L_a$ 成为 $-Wq_0/2$。其余 $U$ 列的极限为 $\ell_\nu q_\nu$，因为 $L_a$ 在零和空间上恒等。这核验了左下块为零，而不是假定完整矩阵仍然循环。

$D_U$ 的逆由 $W\ge k$ 及固定 $k$ 的非零 $\ell_\nu$ 一致控制。因此在有界 $v$ 域及共同小 $\epsilon$ 域内，可定义实际 Schur 块
$$
\mathcal S(\epsilon,v)
=\mathcal A_{RR}
-\mathcal A_{RU}\mathcal A_{UU}^{-1}\mathcal A_{UR}
=R_a(v)+O_k(\epsilon).
\tag{G}
$$
上右块可以非零；这里仅使用 $\mathcal A_{RU}=O(\epsilon)$ 与其他块的一致界，未求逆 $R_a$。故 (G) 在两模块退化处同样有效。

由 $\det L_a=1$、$\det Q=\det P$，
$$
D_{\boldsymbol n}
=\left(\prod_i a_i\right)\det\mathcal A
=\left(\prod_i a_i\right)\det\mathcal A_{UU}\det\mathcal S.
\tag{H}
$$
父乘积公式给出 $\prod\ell_\nu=k^2/3$，于是
$$
D_{\boldsymbol n}(0,v)
=-\frac{3k^2}{32}P(a)\mathcal P_a(v).
$$
所有矩阵及逆的界在占用紧盒上统一，恢复的因子 $\prod_i a_i$ 也有统一上下界。因此 $D_{\boldsymbol n}(\epsilon,v)-D_{\boldsymbol n}(0,v)=O_k(\epsilon)$ 的周期一致性成立，常数允许依赖指定的紧集。这既核对了首系数，也核对了余项量词。

### Step 5. 周期一致的实际简单零曲线与秩

在 $v_j=t\cos(2\pi j/3)$ 上，Fourier 正交性给出 $V_\pm=0$、$Z_\pm=t/2$，因此对所有占用向量均有 $\mathcal P_a=1-t^2$。置
$$
c_a=-\frac{3k^2}{32}P(a),\qquad
f_{\boldsymbol n}(\epsilon,t)
=c_a^{-1}D_{\boldsymbol n}
\bigl(\epsilon,(t\cos(2\pi j/3))_j\bigr).
$$
$|c_a|$ 对周期有正下界；Step 4 给出共同复 $t$ 域上的
$$
f_{\boldsymbol n}(\epsilon,t)=1-t^2+\epsilon h_{\boldsymbol n}(\epsilon,t),
\qquad |h_{\boldsymbol n}|\le M_k.
$$
选固定 $\delta\in(0,1/2)$，在 $|t-s|=\delta$、$s=\pm1$ 上，
$$
|1-t^2|\ge\delta(2-\delta).
$$
统一缩小 $\epsilon$ 域，使 $|\epsilon|M_k<\delta(2-\delta)$。Rouché 定理在每个圆内给出恰好一个零点，按重数计；因此它是简单零点。局部全纯 IFT 与每圆唯一性将这些零点拼为整个共同 $\epsilon$ 小圆上的全纯函数 $t_{\boldsymbol n,s}(\epsilon)$，包括 $\epsilon=0$。

零点方程进一步给出
$$
|t_{\boldsymbol n,s}(\epsilon)-s|
\le \frac{M_k}{2-\delta}|\epsilon|.
$$
故其半径和 $O_k(\epsilon)$ 误差确为周期一致。对每个小非零 $\epsilon$，
$$
\partial_t\det K
=\epsilon^{k+1}c_a\,\partial_t f_{\boldsymbol n}\ne0.
$$
若 $K$ 的秩至多 $k-2$，其全部余子式为零，链式求导的每个行列式一阶导数都会为零，矛盾。因本身行列式为零，秩恰为 $k-1$。父轨道构造在 $u=O(\epsilon)$ 域内仍给 exact、disjoint、simple、nonzero trace，故这里不是状态周期点的分岔。

对任意固定 $u$ 邻域，曲线点随 $\epsilon\to0$ 进入其中；所以它排除的是该周期向量同一组选字的统一固定邻域非退化性，不是所有选字均失效。至此原 preflight 的全部数学主张成立。

## 新增余秩二作者稿的独立证明

以下内容在收到本轮任务时是待核查的新推论，随后由绑定 SHA 的实际作者稿交付。本报告已完整阅读该稿；以下检查与其陈述一致，不从父检查继承。

### Step 6. 四条目仿射可逆与唯一四坐标顶点

固定 $\boldsymbol n$ 且 $\omega_+\omega_-\ne0$。设 $r_{ij}$ 是 $R_a(v)$ 的条目。式 (D) 的逆显式为
$$
V_-=\frac{4r_{11}/3-1}{2\omega_+},\qquad
V_+=\frac{4r_{22}/3-1}{2\omega_-},
$$
$$
Z_+=\omega_+V_+-\frac23r_{12},\qquad
Z_-=\omega_-V_--\frac23r_{21}.
$$
故从 $(V_+,V_-,Z_+,Z_-)$ 到四条目的仿射映射可逆。令四条目为零，得到唯一的四坐标点
$$
V_+=-\frac1{2\omega_-},\quad
V_-=-\frac1{2\omega_+},\quad
Z_+=-\frac{\omega_+}{2\omega_-},\quad
Z_-=-\frac{\omega_-}{2\omega_+}.
\tag{I}
$$
其余 $k-4$ 个 Fourier 坐标自由。在这四维法向切片中，$\det R_a=0$ 是标准 $2\times2$ 行列式锥，(I) 是唯一顶点；在整个 $v$ 空间中则是锥顶乘自由坐标的余维四仿射集合，不能称为整个 $k$ 维参数空间中的唯一点。

### Step 7. 实际余秩二流形

任取一个有限的自由坐标值 $\zeta_*\in\mathbb C^{k-4}$，并以 (I) 及它确定 $v_*$。因周期向量已经固定，$v_*$ 有限；可在包含它的有界域上使用 Step 4。实际 $\mathcal S(\epsilon,v)$ 全纯，且
$$
\mathcal S(0,v)=R_a(v).
$$
记 $\xi=(V_+,V_-,Z_+,Z_-)$，$\zeta$ 为其余 Fourier 坐标。由 Step 6，四条目关于 $\xi$ 的 Jacobian 在 $(0,v_*)$ 可逆。复全纯隐函数定理因此给出
$$
\mathcal S(\epsilon,\xi,\zeta)=0
\quad\Longleftrightarrow\quad
\xi=\Xi(\epsilon,\zeta)
$$
的局部全纯图像。对每个充分小的固定 $\epsilon$，该集合在 $v$ 空间中光滑且余维四；在联合 $(\epsilon,v)$ 空间中也余维四。

由 Schur 分块消元，$\mathcal A$ 与
$$
\operatorname{diag}(\mathcal A_{UU},\mathcal S)
$$
左右等价，消元因子可逆。在 $\mathcal S=0$ 图像上，$\operatorname{rank}\mathcal A=k-2$。当 $\epsilon\ne0$，(F) 的所有左右因子都可逆，故
$$
\operatorname{rank}K(\epsilon,\epsilon v)=k-2.
$$
这也等于未归一化的所选迹 Jacobian 的秩，因为各 $n_i\rho_i$ 非零。父轨道仍简单、精确、互异、迹非零。

### Step 8. 精确行列式临界超曲面局部式

定义坐标变换
$$
(\epsilon,\xi,\zeta)\longmapsto
(\epsilon,x,y,z,t,\zeta)
=
(\epsilon,\mathcal S_{11},\mathcal S_{22},
\mathcal S_{12},\mathcal S_{21},\zeta).
$$
它在 $(0,v_*)$ 的 Jacobian 可逆：保留的 $\epsilon,\zeta$ 坐标形成恒等块，而 $\xi$ 到四个 Schur 条目的块由 Step 6 可逆。全纯逆函数定理给出真正的局部双全纯坐标，并且直接有
$$
\det\mathcal S=xy-zt.
$$
令 $\mathcal U=(\prod_i a_i)\det\mathcal A_{UU}$，它在该邻域内全纯且不消失。由 (H)，联合归一化行列式恰满足
$$
D_{\boldsymbol n}=\mathcal U(xy-zt).
\tag{J}
$$
对于固定非零 $\epsilon$，原行列式则恰满足
$$
\det K(\epsilon,\epsilon v)
=\epsilon^{k+1}\mathcal U(xy-zt),
\tag{K}
$$
此时 $\epsilon^{k+1}\mathcal U$ 是非零单位。在这些固定非零切片上，整个局部临界行列式超曲面确为四坐标行列式锥乘自由的 $k-4$ 个坐标，余秩二流形即其局部奇异集合 $x=y=z=t=0$。

若把 $\epsilon=0$ 也纳入原行列式的联合 germ，(K) 中 $\epsilon^{k+1}$ 不是单位，不能删去。此时应使用 (J) 的归一化对象讨论锥的精确局部式；原 $K$ 在 $\epsilon=0$ 的秩也不能由非零 $\epsilon$ 的缩放等价推断。这个区分是本推论必要的书写边界，不是新增证明障碍。

在零行列式集合中，若四个 Schur 条目并非全零，则这个 $2\times2$ 矩阵的秩为一。因此相应 $K$ 的秩为 $k-1$，完整核对作者稿“临界超曲面在余秩二集合以外均为余秩一”的局部断言。

以上坐标由实际 Schur 条目构成，故高阶项已被真正的局部坐标吸收，而非仅有二阶近似。然而这只描述行列式临界超曲面及选定矩阵的秩，不给出原迹映射 germ 的左右等价、fold/cusp 类型或其他映射奇点分类。新增作者稿按这些明确范围成立。

### Step 9. 平衡占用的有界尺度对照

若 $\omega_+=\omega_-=0$，式 (D) 的迹恒等于 $3/2$。在每个固定有界 $v$ 域上，由 (G) 有
$$
\operatorname{tr}\mathcal S(\epsilon,v)=\frac32+O_k(\epsilon).
$$
统一缩小该域所对应的 $\epsilon$ 半径，可令误差绝对值小于 $3/4$。于是实际 $\mathcal S$ 不可能为零矩阵。补块仍可逆，故对非零 $\epsilon$ 有 $\operatorname{rank}K\ge k-1$；这个有界重标度域内不存在余秩二或更高余秩点。这不排除 $v$ 随 $\epsilon$ 发散的别的尺度或其他选词。

实际占用给出 $\omega_-=\overline{\omega_+}$，当失衡趋于零时，(I) 中两个 $V_\pm$ 的模都趋于无穷。因此失衡余秩二中心离开每个有界 $v$ 域，与上述平衡结论相容；不需要也未建立全局紧化或一致过渡模型。

余秩二作者稿最后关于“另一个最小选取若独立通过，将表明这些点不是全体标记谱的共同微分缺陷”的段落是条件比较。该新选词证明不是本报告依赖，本轮没有读取或验证它，也不将其结论升级为已证。两份实际作者输入的本轮数学主张至此检查闭合。

## Corrections or Missing Assumptions

两份实际作者输入均无需数学修改。以下限定已在新增作者稿中得到尊重，任何后续表述都应保留：

1. (I) 是唯一的四坐标顶点；整个参数空间仍有 $k-4$ 个自由坐标。
2. 余秩二推论固定周期向量并要求 $\omega_+\omega_-\ne0$。在占用平衡时仿射四条目映射不再可逆，不能应用同一四维 IFT；式 (I) 在 $\omega_\pm\to0$ 时也可能逃向无穷。
3. 联合全纯族中单位乘二次锥的是 $D_{\boldsymbol n}$。原 $\det K$ 的单位版本与原 $K$ 秩 $k-2$ 仅对非零 $\epsilon$ 断言。
4. 所有现象仅对指定周期向量的原组选字成立，不说明任何其他选择的秩。

## 净新增证明负载

一般周期 preflight 的净负载是：占用输出方向造成的斜投影、保留 $Q$ 修正后得到 $3/2$、四坐标块与行列式、周期一致的实际零曲线。它复用全部轨道/Riccati 分析、二阶相关系数、Fourier 乘积与一般缩放框架；这些不能再次计为新增篇幅。

我的独立估计是：将 preflight 融入父数学文本后，净新增约 **2–4 页** 紧凑完整的英语数学推导。新增余秩二作者稿在复用该块之后另需约 **1–2 页**：写出仿射逆、参数化 IFT、Schur 行列式恒等式、平衡对照及归一化限制。两者都不是观测页数，也不是相加后重开旧候选的页数证书。本报告为核查而重复的记号与依赖说明不应按科学正文负载计算。

余秩二延拓确实增加了“实际临界锥顶而不仅是 leading 顶点”的结论，但证明机制是可逆补块、四个条目坐标以及全纯逆/隐函数定理的直接组合。不能把它包装成新奇点理论、额外独立长篇论文或原迹映射的完整奇点分类。

## Open Risks 与最终处置

在上述精确假设及解释下，没有剩余数学缺口。未开展 $\omega_\pm\to0$ 的一致奇点模型、其他选字的内在谱秩、全局临界集合或映射 germ 分类；这些不属于本报告已证明的内容。

**最终数学状态：绑定 SHA 的一般周期 preflight 与余秩二作者稿均为 PROVABLE AS STATED。** 两份实际输入的数学结论完整保留。本轮不推翻作者的短推论 STOP，不改变旧第五候选 FAIL、不授予候选 PASS，不创建正式 Paper29 或 PDF；批次状态仍为 2/5。
