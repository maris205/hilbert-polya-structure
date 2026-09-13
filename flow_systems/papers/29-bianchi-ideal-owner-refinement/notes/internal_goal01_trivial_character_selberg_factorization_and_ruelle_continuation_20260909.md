# P29 Goal01：平凡角色的 Selberg 因式分解与经典 Ruelle 全平面延拓

日期：2026-09-09 UTC。主代理在持续授权内新增的内部纸面推论。
只处理现有单位速测地流与平凡 Γ 角色；不增加新流、不执行数学程序、
不选择量子化或更改任何 Route／Stage 状态。

## 1. 明确结论与来源责任

沿用[横向 supertrace 笔记][supertrace]：
\[
\Gamma=\{B\in SL_2(\mathbb Z[i]):B\equiv I\pmod3\},\qquad
X=\bar\Gamma\backslash\mathbb H^3.
\tag{1}
\]
曲率为 -1，流是 SX 上的完整单位速测地流。
\(\mathscr O\) 为有向本原流轨道，按时间平移取商；不是无向曲线集。
已定义的平凡角色 Ruelle 逆乘积为
\[
\zeta^{\rm cl}_0(s)
=\prod_{\gamma\in\mathscr O}(1-e^{-s\ell_\gamma})^{-1},
\qquad \operatorname{Re}s>2.
\tag{2}
\]
这里下标 0 表示平凡 Γ character，不是零能量或改变时钟。

本页证明：可取同一几何上的三个齐性束 Selberg 函数
\(Z_0,Z_+,Z_-\)，保持 Pfaff 的参数偏移约定，使
\[
\boxed{
\zeta^{\rm cl}_0(s)=
\frac{Z_+(s)Z_-(s)}{Z_0(s-1)Z_0(s+1)}.
}
\tag{3}
\]
右边在整个复平面亚纯，并与 (2) 的函数相容，因而 (2) 有唯一的
全平面亚纯延拓。没有声称全平面全纯、无零或只有单一极点。

外部输入是 Jonathan Pfaff，
*Selberg zeta functions on odd-dimensional hyperbolic manifolds of finite volume*，
[arXiv:1205.1754v1，Theorem 1.1][pfaff]。
本页直接核查该定理的实际 cusp 假设、三个 M 表示、
源式 (1.2)／(3.2) 的有向轨道与参数，再证明 (3)。
不是仅根据一篇论文的标题引用“Ruelle 可延拓”。

ARS 有界论证组织在此用于区分源定理、实际适用条件、乘积恒等式、
唯一延拓以及仍不成立的量子解释。

## 2. 实际群与 Spin 模型兼容

[实际有限周期包笔记][packets]已核对 \(\bar\Gamma\) 的离散、
无撓及有限体积；[自然振幅笔记][amplitude]给
\[
\operatorname{tr}B\in2+9\mathbb Z[i]\qquad(B\in\Gamma).
\tag{4}
\]
为说明 (4)，写 B=I+3D，由 det B=1 得
\(3\operatorname{tr}D+9\det D=0\)，故
\(\operatorname{tr}B=2-9\det D\)。

\(-I\notin\Gamma\)，所以 \(\Gamma\to\bar\Gamma\) 为群同构，
没有把 source 的 Spin lift 换成一个带中心扭结的不同群。
Pfaff §2.1 取 \(G=\operatorname{Spin}(3,1)\cong SL_2(\mathbb C)\)，
\(K=\operatorname{Spin}(3)\cong SU(2)\)，其标准双曲度量曲率也是 -1。
因此 source 的 \(\Gamma\backslash G/K\) 是 (1) 的同一流形。

也可直接再看无有限阶元这一点：若 B 有有限阶，其特征值是
\(\lambda,\lambda^{-1}\)，\(|\lambda|=1\)，故
\(\operatorname{tr}B=\lambda+\lambda^{-1}\in[-2,2]\)。
与 (4) 相交只剩 2，特征值均为 1；有限阶矩阵可对角化，故 B=I。
这项说明只用于 source 的无撓条件，不用一个未经定义的
“neat”标签代替下面更精确的 cusp 检查。

## 3. 直接验证 source 的 cusp 条件

Pfaff 式 (1.3) 要求：对每个 Γ-cuspidal parabolic subgroup
\(P=M_PA_PN_P\)，
\[
\boxed{\Gamma\cap P=\Gamma\cap N_P.}
\tag{5}
\]
本页直接证明此式，不需要为一个额外表示类证明更强的 neat 性。

固定这样的 cusp。其 unipotent cusp lattice 含非平凡元素
\(Q\in\Gamma\cap N_P\)，而 P 稳定其唯一边界点 z。
在 SL 模型中 Q 是非恒等 unipotent，故 Q-I 是秩一 Gaussian
矩阵，其核是一条 \(\mathbb Q(i)\)-直线。因此
\[
z\in\mathbb P^1(\mathbb Q(i)).
\tag{6}
\]
这里仅使用 Γ-cuspidal 的通常含义：\(\Gamma\cap N_P\) 是
正维 \(N_P\) 中的格，因而含非恒等 unipotent。
不需要列举全部 cusp 或选择实际 cusp representatives。

任取 \(B\in\Gamma\cap P\)。B 固定 z。
选非零 \(v\in\mathbb Q(i)^2\) 代表 (6)，则
\[
Bv=\lambda v,\qquad \lambda\in\mathbb Q(i).
\]
由于 B 是 determinant-one Gaussian 矩阵，
\(\lambda,\lambda^{-1}\) 都满足 monic Gaussian 特征多项式。
\(\mathbb Z[i]\) 在其分式域中整闭，所以
\(\lambda,\lambda^{-1}\in\mathbb Z[i]\)；于是
\[
\lambda\in\mathbb Z[i]^\times=\{1,-1,i,-i\}.
\tag{7}
\]
因此 \(\operatorname{tr}B=\lambda+\lambda^{-1}\in\{2,-2,0\}\)。
结合 (4)，只可能为 2，且 \(\lambda=1\)。

把 z 移到无穷远后，B 是对角元均为 1 的上三角矩阵，
正是 \(N_P\) 中的元素，包括恒等元。
故 \(\Gamma\cap P\subset\Gamma\cap N_P\)，反向包含显然，(5) 成立。

这是针对实际 level-(3) 群的 source 假设证明，
不是只从有限体积或 torsion-free 推出所有 cusp 都没有旋转部分。

## 4. 三个 M 表示、法向旋转与方向约定

在 \(G=SL_2(\mathbb C)\) 中，可取
\[
M=\left\{m_\varphi=
\begin{pmatrix}e^{i\varphi}&0\\0&e^{-i\varphi}\end{pmatrix}:
\varphi\in\mathbb R/(2\pi\mathbb Z)\right\}.
\]
定义三个有限维酉一维表示
\[
\sigma_0(m_\varphi)=1,\qquad
\sigma_+(m_\varphi)=e^{2i\varphi},\qquad
\sigma_-(m_\varphi)=e^{-2i\varphi}.
\tag{8}
\]
这些是 M 角色，不是任意 \(\Gamma\)-阿贝尔 character。
按 Pfaff §2.3 的最高权单位，它们是 \(k_2=0,+1,-1\)；
若直接用 \(\varphi\) 的整数指数，则是 \(0,+2,-2\)。
本页不用同一个下标偷换这两种索引。

[amplitude, §3] 直接解 Jacobi 方程，给稳定返回
\[
P_\gamma^s=e^{-\ell_\gamma}R_{\vartheta_\gamma},\qquad
\operatorname{spec}_{\mathbb C}P_\gamma^s
=\{e^{-\ell_\gamma+i\vartheta_\gamma},
   e^{-\ell_\gamma-i\vartheta_\gamma}\}.
\tag{9}
\]
若 SL 的旋转部分是 \(m_\varphi\)，则
\(\vartheta_\gamma=\pm2\varphi\pmod{2\pi}\)。
因此 source 束的返回标量满足无歧义的无序对身份
\[
\{\mu_{\sigma_+}(\gamma),\mu_{\sigma_-}(\gamma)\}
=\{e^{i\vartheta_\gamma},e^{-i\vartheta_\gamma}\},
\quad \mu_{\sigma_0}(\gamma)=1.
\tag{10}
\]
改变法向角或 source 左／右作用的符号只交换 + 与 -，
不改变 (3) 的分子。用 \(e^{\pm i\varphi}\) 则不是所需法向表示。

Pfaff §3 的 (3.2) 明确按全部 prime Γ-conjugacy classes 取乘积，
其源导言还把该集合与 geodesic-flow 闭轨道相对应；
没有再商 \([\gamma]\sim[\gamma^{-1}]\)。
这与 (2) 保留两种方向的约定相符。

实际群中二者也不共轭：若 \(h\gamma h^{-1}=\gamma^{-1}\)，
loxodromic γ 的两个不同特征线必须被 h 交换。
在相应特征基底，det h=1 的反对角矩阵满足 \(h^2=-I\)，
与 \(h\in\Gamma\) 矛盾。若起初只在 PSL 写等式，负号已由
双方的 \(I\bmod3\) 提升排除。
故本页不存在隐藏的平方根、二倍计数或逆向合并。

## 5. 保持 source 的 Selberg 参数归一化

令 \(j\in\{0,+,-\}\)，定义
\[
Z_j(z):=Z(z,\sigma_j)
=\prod_{\gamma\in\mathscr O}\prod_{k=0}^\infty
\det\!\left(
I-\mu_{\sigma_j}(\gamma)\,
\operatorname{Sym}^kP_\gamma^s\,
e^{-(z+1)\ell_\gamma}
\right).
\tag{11}
\]
这是 Pfaff 式 (1.2) 在 d=3、n=1 下的原约定。
这里的 +1 是 source 的半维数偏移，不是重设真实周期。
source 给充分的绝对收敛域 \(\operatorname{Re}z>2\)；
本页先使用此保守域，不需要求最优收敛边界。

对 \(T=r\ell_\gamma\)，置
\[
q_{\gamma,r}=e^{-T},\quad
w_{\gamma,r}=e^{ir\vartheta_\gamma},\quad
\Delta_{\gamma,r}
=(1-q_{\gamma,r}w_{\gamma,r})
 (1-q_{\gamma,r}w_{\gamma,r}^{-1}).
\tag{12}
\]
两因子互为共轭，故
\(\Delta_{\gamma,r}=1-2e^{-T}\cos(r\vartheta_\gamma)+e^{-2T}>0\)。
它是稳定二维返回的 determinant，
不是 scalar flat trace 的完整四维分母。

由 symmetric powers 的特征值生成级数，
\[
\sum_{k\ge0}\operatorname{tr}
  \operatorname{Sym}^k((P_\gamma^s)^r)
=\Delta_{\gamma,r}^{-1}.
\]
而在相同 eigenbasis 中，\(\operatorname{Sym}^k((P_\gamma^s)^r)\)
的 k+1 个特征值模均为 \(e^{-kT}\)，故还有绝对重排所需的
\[
\sum_{k\ge0}\left|\operatorname{tr}
 \operatorname{Sym}^k((P_\gamma^s)^r)\right|
\le\sum_{k\ge0}(k+1)e^{-kT}
=(1-e^{-T})^{-2}\le(1-e^{-\delta})^{-2}.
\]
对 (11) 展开有限维 log determinant 并按正常收敛重排，得到
\[
\boxed{
\log Z_j(z)
=-\sum_{\gamma\in\mathscr O}\sum_{r\ge1}
\frac{\mu_{\sigma_j}(\gamma)^r
      e^{-(z+1)r\ell_\gamma}}
     {r\Delta_{\gamma,r}}.
}
\tag{13}
\]
其中 log 分支由沿实正无穷趋于 0 固定。
这也与 source 式 (3.5) 中 \(n_\Gamma(\gamma^r)=r\) 一致。

绝对重排可直接核查：上述 k 求和的绝对上界与已有
\(\ell_\gamma\ge\delta>0\) 给共同常数
\((1-e^{-\delta})^{-2}\)；
\(|\mu_{\sigma_j}|=1\)，而全部重复计数
\(N(L)\le Ce^{2L}\)。用 (13) 的正数上界分壳求和即可；
在此 \(\operatorname{Re}z>2\) 足够。
因此不是从未控制的 infinite-product cancellation 猜出 (13)。

## 6. 四个 log 的逐轨道相消

先取 \(\operatorname{Re}s>3\)，使 (3) 中四个 source 参数
\(s,s,s-1,s+1\) 均处于上一节的充分收敛域。
由 (10)、(12)--(13)，
\[
\begin{aligned}
&\log Z_+(s)+\log Z_-(s)
 -\log Z_0(s-1)-\log Z_0(s+1)\\
&=\sum_{\gamma,r}\frac{e^{-sr\ell_\gamma}}{r}
 \frac{1-q_{\gamma,r}(w_{\gamma,r}+w_{\gamma,r}^{-1})
           +q_{\gamma,r}^2}
      {\Delta_{\gamma,r}}\\
&=\sum_{\gamma,r}\frac{e^{-sr\ell_\gamma}}{r}
=\log\zeta^{\rm cl}_0(s).
\end{aligned}
\tag{14}
\]
最后一步使用 (2) 已固定的正无穷归一化。
所以没有一个未定常数、额外 entire prefactor 或 branch factor；
指数化后正是 (3)。

本页的 \(\zeta^{\rm cl}_0\) 是 inverse Euler product。
Pfaff 式 (1.4) 的 \(R(s,\sigma_0)\) 用正次幂乘积，故
\[
\zeta^{\rm cl}_0(s)=R(s,\sigma_0)^{-1}
\tag{15}
\]
在右域成立。相应因式分解的分子／分母不能互换。
source Corollary 1.2 可作为另一种延拓入口，但 (14) 已明确给出
本案所需的三个齐性 Selberg 函数与四个参数位置。

## 7. 全平面亚纯延拓、常数钟与正时间迹的准确衔接

由 §§2--4，三个 \(\sigma_j\) 都满足 Theorem 1.1 的输入，
故每个 \(Z_j\) 都在 \(\mathbb C\) 亚纯，且不恒等于零，
因为其右域乘积非零。
因此 (3) 的右边定义一个全平面亚纯函数。

(14) 在非空开半平面成立。用亚纯函数身份定理，它与原先
\(\operatorname{Re}s>2\) 中的 (2) 完全一致；
右侧看似的零／极点若落在原非零右域中，必须在 quotient 中抵消。
这提供的是唯一亚纯延拓，不声称完整复平面上仍有绝对乘积。

[supertrace] 已在正时间构造合法的 \(\nu_0\) 并证明
\[
-\frac{(\zeta^{\rm cl}_0)'(s)}{\zeta^{\rm cl}_0(s)}
=\int_0^\infty e^{-st}\,d\nu_0(t)
\quad(\operatorname{Re}s>2).
\tag{16}
\]
现可延拓左边这个标量函数，并写为
\[
-\frac{Z_+'(s)}{Z_+(s)}-\frac{Z_-'(s)}{Z_-(s)}
+\frac{Z_0'(s-1)}{Z_0(s-1)}
+\frac{Z_0'(s+1)}{Z_0(s+1)}.
\tag{17}
\]
但 (17) 在右域外不表示原 Laplace 积分仍绝对收敛，
也不构成普通 \(L^2\) resolvent trace。
\(\nu_0\) 的正时间支撑障碍不会被解析延拓消除。

对一个固定常数钟 c>0，原 \(\ell\mapsto c\ell\) 给
\[
\zeta^{\rm cl}_{c,0}(s)=\zeta^{\rm cl}_0(cs)
=\frac{Z_+(cs)Z_-(cs)}{Z_0(cs-1)Z_0(cs+1)}.
\tag{18}
\]
这是同一固定 Z 的参数代入；不是把 source 的 +1 偏移也乘 c。
其对数导数产生 c，与
\(\nu_{c,0}=c(t\mapsto ct)_*\nu_0\) 一致。

## 8. 尚未取得的结论与实际操作

本页只覆盖平凡 Γ 角色。Theorem 1.1 的 M 齐性束、
以及 Corollary 1.2 中从 G 表示限制所得的 Γ 束，
都不自动覆盖此前任意 \(\chi_\theta:\Gamma\to U(1)\)。
全角色的 twisted Selberg 与 cusp 分析必须另有适用定理和证明。
本页亦不处理一般非恒定正换时。

来源描述其 Selberg 奇点与某些齐性 Laplace／Dirac 算子、
scattering matrix 及 cusp 项的关系；这不把本案自然 Koopman
\(A_\theta=-i\nabla_X\) 变成这些算子。
[自然 L2 生成元笔记][generator]的
\(\sigma_{\rm ess}(A_\theta)=\mathbb R\) 与 noncompact resolvent
结论仍然有效。
本页未定义该 A 的普通核 Fredholm determinant，
未建立量子 spectrum／zeta zeros 的一一对应、全局 quantum
determinant 身份或 Route 判定。

主代理实际核读 Pfaff arXiv v1 的 §1 相关定义／Theorem 1.1／
Corollary 1.2、§2.1／§2.3／§2.6 及 §3 的 (3.1)--(3.5)。
最初另一公开镜像请求 timeout 后，使用作者 arXiv 版本；
没有绕过权限或付费访问，也没有本地 PDF 下载。
本页不宣称复核 source 的整篇谱分析证明；
引用的是已明列、实际对齐假设的来源定理。

保存使用 apply_patch 只新增本文件。
有限分工提供 source 定位与旋转／因子校对，主代理直接推导 cusp
条件和 (14)，同模型 agreement 不是外部独立科学证据。
未运行科学、符号、census、producer、实验或 manuscript build；
未改变旧笔记、失败记录、锁定输入或正式阶段。
实际文本检查由持续工作记录另记。

[supertrace]: internal_goal01_transverse_supertrace_and_classical_ruelle_interface_20260909.md
[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[amplitude]: internal_goal01_geometric_return_amplitude_and_laplace_bound_20260909.md
[generator]: internal_goal01_natural_l2_generator_and_cusp_essential_spectrum_20260909.md
[pfaff]: https://arxiv.org/pdf/1205.1754v1
