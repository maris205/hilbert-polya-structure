# P31 Goal01：同一物理时钟的余切 Hamiltonian、作用量与平移边界

日期：2026-09-09 UTC。主代理在持续授权内新增的内部纸面推导。
它只识别现有 P31 流的经典 Hamiltonian，不选择量子化、算子域、
边界条件或 Route；不修改旧文件、锁定输入或正式状态。

## 1. 固定对象与结论

采用[同钟接触／Randers 笔记][contact]的全部定义：
\[
Y=Y_0(11),\quad M=S_gY,\quad
\alpha=\operatorname{Re}(2\pi i f(z)\,dz),\quad
\beta=\varepsilon\alpha,\quad d\beta=0,
\]
\[
\rho(x,u)=1+\beta_x(u)\ge c_0>0\quad((x,u)\in M),\qquad
X_\varepsilon=X_{\rm geo}/\rho,\qquad
F(x,v)=|v|_g+\beta_x(v).
\tag{1}
\]
这里 \(\varepsilon\) 是原正密度区间中的固定实数。
上游已从全方向正性证明
\[
0<c_0\le1,\qquad |\beta_x|_{g^*}\le1-c_0<1,\qquad
c_0|v|_g\le F(x,v)\le(2-c_0)|v|_g,
\tag{2}
\]
以及 F 的强凸性、同一物理时间的完备测地流与接触形式
\[
\lambda_\varepsilon=\lambda_{\rm geo}+\pi^*\beta,\qquad
d\lambda_\varepsilon=d\lambda_{\rm geo},\qquad
\lambda_\varepsilon(X_\varepsilon)=1.
\tag{3}
\]

本页在 \(T^*Y\setminus0\) 上显式构造同一个 F 的对偶正齐次
Hamiltonian H。对每个能量 E>0，都有一个自然微分同胚
\[
\Phi_E:M\longrightarrow\Sigma_E:=\{H=E\}
\]
把 \(X_\varepsilon\) 按**同一物理时间**送到 \(X_H|_{\Sigma_E}\)。
每条原有向本原闭轨道的作用量为
\[
\boxed{\mathcal A_E(P)=E T_\varepsilon(P)
=E\bigl(\ell_g(P)+\varepsilon I(P)\bigr).}
\tag{4}
\]
E 不是另选时钟比例；H 的正一次齐次性使不同正能量上的基底运动
具有相同时间。若改成二次 Hamiltonian，则必须重新计算时间。

ARS 的有限论证组织在此用于区分 dual norm、能层、特征方向、
Reeb 归一化、全局 exactness 和尚未作出的量子声明。
下文公式是直接证明，不依赖将周期乘积命名为“自然谱行列式”。

## 2. 对偶球与显式 H

记余切投影为 \(\pi_*:T^*Y\to Y\)。对每个 x，定义
\[
H(x,p)=F_x^*(p)
:=\sup_{v\ne0}\frac{p(v)}{F(x,v)},\qquad H(x,0)=0.
\tag{5}
\]
分母严格正；p≠0 时选取使 p(v)>0 的方向可知 H>0。
F 单位球的紧性与 (2) 保证 supremum 有限。

对偶闭单位球有直接描述：
\[
\begin{aligned}
\{p:H(x,p)\le1\}
&=\{p:p(v)\le |v|_g+\beta_x(v)\ \hbox{对全部 }v\}\\
&=\{p:|p-\beta_x|_{g^*}\le1\}
=\beta_x+\overline B_{g^*,x}.
\end{aligned}
\tag{6}
\]
第二步是 Riemann 对偶范数的定义。由于 \(|\beta_x|_{g^*}<1\)，
这个平移球包含零于内部，其 gauge 正是 H；没有将
F 的切单位球误认为平移的 Riemann 切单位球。

对 E>0，正齐次性因而给
\[
\{H\le E\}=\{p:|p-E\beta_x|_{g^*}\le E\},\qquad
\Sigma_E=\{p:|p-E\beta_x|_{g^*}=E\}.
\tag{7}
\]
为写出 H，置
\[
A(x)=1-|\beta_x|_{g^*}^2>0,\qquad
B(x,p)=\langle p,\beta_x\rangle_{g^*},\qquad C(x,p)=|p|_{g^*}^2.
\]
方程 \(|p-H\beta_x|=H\) 等价于
\[
A H^2+2BH-C=0.
\]
对 p≠0，\(\sqrt{B^2+AC}>|B|\)，唯一正根为
\[
\boxed{
H(x,p)=\frac{\sqrt{B(x,p)^2+A(x)C(x,p)}-B(x,p)}{A(x)}.
}
\tag{8}
\]
因此 H 在 slit cotangent bundle 上光滑，严格正、正一次齐次；
它在零截面连续，不声称在那里光滑。
由 (2) 或 (5) 得到一致的纤维比较
\[
\boxed{\frac{|p|_{g^*}}{2-c_0}\le H(x,p)
\le\frac{|p|_{g^*}}{c_0}.}
\tag{9}
\]
这是纤维中的增长界，不自动构成某个非紧全局伪微分演算的全部
symbol-seminorm 界；本页没有选择这种演算。

## 3. 能层与 canonical one-form 的精确拉回

采用 canonical one-form 和辛形式约定
\[
(\lambda_{\rm can})_{(x,p)}(\zeta)=p(d\pi_*\zeta),\qquad
\omega_{\rm can}=-d\lambda_{\rm can},\qquad
\iota_{X_H}\omega_{\rm can}=dH.
\tag{10}
\]
在局部坐标中这给通常的
\(\dot x=\partial_pH,\ \dot p=-\partial_xH\)。
注意 (10) 中的 \(\omega_{\rm can}\) 不等于
\(d\lambda_{\rm can}\)；以下符号全部与 (10) 一致。

对 E>0 定义
\[
\boxed{\Phi_E(x,u)=\bigl(x,E(u^\flat+\beta_x)\bigr),\qquad |u|_g=1.}
\tag{11}
\]
(7) 表明其像恰为 \(\Sigma_E\)，逆映射是
\[
(x,p)\longmapsto
\left(x,\bigl(p/E-\beta_x\bigr)^\sharp\right).
\tag{12}
\]
两者光滑，故是全局微分同胚。由 canonical form 的定义，
\[
\boxed{\Phi_E^*\lambda_{\rm can}
=E(\lambda_{\rm geo}+\pi^*\beta)=E\lambda_\varepsilon,\qquad
\Phi_E^*d\lambda_{\rm can}=E\,d\lambda_{\rm geo}.}
\tag{13}
\]

Euler 齐次公式给
\[
\lambda_{\rm can}(X_H)
=p(\partial_pH)=H.
\tag{14}
\]
此外 \(dH(X_H)=\omega_{\rm can}(X_H,X_H)=0\)，所以 X_H
切于各个正能层。对 \(\zeta\in T\Sigma_E\)，
\[
d\lambda_{\rm can}(X_H,\zeta)=-dH(\zeta)=0.
\tag{15}
\]
把 (15) 拉回，利用 \(d\lambda_{\rm geo}\) 在三维 M 上的
一维核是 \(\mathbb R X_{\rm geo}\)，可写
\[
(\Phi_E^{-1})_*X_H=\kappa X_{\rm geo}.
\]
将 (13)--(14) 代入此式，得到
\[
E=\lambda_{\rm can}(X_H)
=E\kappa\,\lambda_\varepsilon(X_{\rm geo})
=E\kappa\rho.
\]
E>0 可消去，因此
\[
\boxed{(\Phi_E^{-1})_*X_H=X_{\rm geo}/\rho=X_\varepsilon.}
\tag{16}
\]

这里一个容易混淆的 E 因子确实不存在。但
\(\lambda_{\rm can}|_{\Sigma_E}\) 本身的 Reeb 向量场是
\(X_H/E\)，拉回为 \(X_\varepsilon/E\)。
若使用归一化接触形式 \(E^{-1}\lambda_{\rm can}|_{\Sigma_E}\)，
其 Reeb 场才是 \(X_H\)。本页的同时间结论指 (16)，不把这两种
接触形式的 Reeb 归一化混同。

上游已证 \(X_\varepsilon\) 完备；由 (11)、(16) 得每个
\(X_H|_{\Sigma_E}\) 完备。任意 slit 点位于一个 E>0 的能层，
故 H 的流在整个 slit cotangent bundle 上对全部实时间存在。
这里不是由“流形非紧但形式光滑”推断完备性。

## 4. 周期、本原性与作用量

设 P 是原有向本原 geodesic，物理周期为
\[
T_\varepsilon(P)=\ell_g(P)+\int_P\beta
=\ell_g(P)+\varepsilon I(P)>0.
\tag{17}
\]
同时间微分同胚 (16) 保持返回时刻和本原性。
沿其能量 E 的闭轨道 \(P_E\)，(14) 恒为 E，故
\[
\begin{aligned}
\mathcal A_E(P)
&:=\oint_{P_E}\lambda_{\rm can}
=\int_0^{T_\varepsilon(P)}
  \lambda_{\rm can}(X_H)\,dt\\
&=E T_\varepsilon(P).
\end{aligned}
\tag{18}
\]
由 (13) 沿同一基底 geodesic 直接积分，也得到
\(E\ell_g(P)+E\int_P\beta\)，两种计算一致。
r 重轨道的作用量和周期各乘 r。

逆向的有向 geodesic 具有
\[
T_\varepsilon(P^{-1})=\ell_g(P)-\varepsilon I(P),\qquad
\mathcal A_E(P^{-1})=E\bigl(\ell_g(P)-\varepsilon I(P)\bigr).
\tag{19}
\]
两者一般不同，不能因原 g 可逆便按无向轨道合并。
本页没有 Maslov 指数、稳定性振幅、量子迹分布或 Bohr--Sommerfeld
条件；(18) 只是已定义经典作用量的精确值。

## 5. 固定能量平移是辛的，但不是 H 的同时间共轭

对固定 E>0，考虑全部 \(T^*Y\) 上的纤维平移
\[
T_E(x,p)=(x,p+E\beta_x).
\tag{20}
\]
因为 \(d\beta=0\)，
\[
T_E^*\lambda_{\rm can}
=\lambda_{\rm can}+E\pi_*^*\beta,\qquad
T_E^*\omega_{\rm can}=\omega_{\rm can}.
\tag{21}
\]
所以 \(T_E\) 是 symplectomorphism。
但这只把原 \(H_0(x,p)=|p|_{g^*}\) 的 E 能层送到 \(\Sigma_E\)。

更具体地，\(T_E\) 将 \(H_0\) 共轭为
\[
K_E:=H_0\circ T_E^{-1}=|p-E\beta_x|_{g^*},
\tag{22}
\]
它在 \(p\ne E\beta_x\) 处光滑，包含整个 \(\Sigma_E\) 的邻域；
不是 (8) 中同时控制所有能量的 H。
在 \(\Sigma_E\) 的点 \(p=E(u^\flat+\beta_x)\)，对
\[
|p-H(x,p)\beta_x|_{g^*}-H(x,p)=0
\]
作全微分。将 H 暂作独立标量参数时，其偏导是
\(-1-\beta_x(u)=-\rho(x,u)\)；对 (x,p) 的偏导是 \(dK_E\)。
因此在该点的**整个余切切空间**上有
\[
\boxed{dH=\rho^{-1}dK_E,\qquad
X_H=\rho^{-1}X_{K_E}\quad\hbox{于 }\Sigma_E.}
\tag{23}
\]
于是 \(T_E\) 保持的是 \(H_0\) 与 \(K_E\) 的 Hamiltonian 时间，
而 H 再作原来的 \(\rho\) 换时。
仅仅说“能层平移是辛的”不足以消去物理时钟。

## 6. Exactness 与把各能层拼成一个映射的失败

按通常约定，symplectomorphism exact 指
\(T^*\lambda_{\rm can}-\lambda_{\rm can}\) 是 exact one-form。
[非零周期笔记][nonzero]已证明实际 \(\alpha\) 有某个
hyperbolic 周期 \(I(\gamma)\ne0\)。
若 \(\varepsilon\ne0\)，则 \(\beta\) 非 exact，由 (21)
\[
\oint_{\widetilde\gamma}
(T_E^*\lambda_{\rm can}-\lambda_{\rm can})
=E\varepsilon I(\gamma)\ne0
\tag{24}
\]
可见 \(T_E\) 不是 exact symplectomorphism。
\(\widetilde\gamma\) 可取原闭 geodesic 的任意光滑余切提升；
故无需假设零截面在 slit domain 内。
若在整个 \(T^*Y\) 工作，也可由零截面拉回证明
\(\pi_*^*\beta\) 的非 exactness。
\(\varepsilon=0\) 时以上平移为恒等映射，没有该障碍。

因此非 exact 辛平移不必保持 canonical 闭作用量；
(24) 正是 (18) 中额外 \(E\varepsilon I(P)\) 的来源。
这一结论与辛形式保持完全相容。

若试图令 E 随原能量变化，拼出
\[
\mathcal T(x,p)=\bigl(x,p+|p|_{g^*}\beta_x\bigr),
\qquad p\ne0,
\tag{25}
\]
则它确实是一个正一次齐次微分同胚，满足
\[
H\circ\mathcal T=H_0,\qquad
\mathcal T^{-1}(x,p)=\bigl(x,p-H(x,p)\beta_x\bigr).
\tag{26}
\]
但 Hamiltonian 函数的这种坐标身份不够；其辛性失败：
\[
\mathcal T^*\lambda_{\rm can}
=\lambda_{\rm can}+H_0\pi_*^*\beta,\qquad
d(\mathcal T^*\lambda_{\rm can}-\lambda_{\rm can})
=dH_0\wedge\pi_*^*\beta.
\tag{27}
\]
在任何 \(\beta_x\ne0\) 的点，选径向竖直向量 V 使
\(dH_0(V)\ne0\)，再选某个余切总空间切向量 W，
使 \(\beta_x(d\pi_*W)\ne0\)。因 \(\pi_*^*\beta(V)=0\)，
(27) 在 (V,W) 上非零。
所以对实际 \(\varepsilon\ne0\)，\(\mathcal T\) 不是
symplectomorphism，不能由 (26) 宣布两个流同时间辛共轭。

这里排除的是 (20)、(25) 这两个**指定构造**的误用；
没有证明不存在任何其他辛映射、接触映射或量子模型。

## 7. 既有 coefficient family 的纯相位一致性，仅作代数检查

保留原平坦 character
\[
\kappa_w(\gamma)=e^{-w\varepsilon I(\gamma)}.
\]
对任意固定实 \(\hbar>0\)，(18) 的形式相位满足
\[
e^{i\mathcal A_E(P)/\hbar}
=e^{iE\ell_g(P)/\hbar}\,
 \kappa_{-iE/\hbar}(P).
\tag{28}
\]
\(-iE/\hbar\) 位于虚轴，正与[可酉化边界][nonzero]一致。
此处 \(\hbar\) 只是该代数相位中的正参数，未宣称构造了
一个依赖它的量子算子；(28) 不是已证明的 semiclassical trace formula。
Laplace 右域中的非酉 \(\kappa_s\) 与此虚轴酉 character
属于同一个解析族的不同参数，不需要把右域表示强行称为酉。

## 8. 来源支持、未解义务与操作记录

对偶范数与 Legendre 几何的标准定义参见 Zhongmin Shen，
*Landsberg, S- and Riemann Curvatures*，§2，特别是对偶范数、
式 (2)--(12) 附近的局部接口：
[MSRI/SLMath 原章节](https://library.slmath.org/books/Book50/files/08Sh.pdf)。
主代理实际核读该节相关段落；(6)--(9) 的特定公式在本页直接推导，
没有套用切／余切角色不同的 navigation 公式。

Álvarez Paiva--Balacheff--Tzanev 的
*Isosystolic inequalities for optical hypersurfaces*，
[arXiv:1308.5522v2 §4.1](https://arxiv.org/pdf/1308.5522v2)
给光学超曲面与 Finsler 对偶、canonical contact Reeb 和闭作用量
等于 Finsler 长度的标准局部对应。主代理实际读到相关节；
本页不把该文在紧基底上的 isosystolic 全局结果移植到非紧 Y。
(13)--(18) 自行处理本案能量归一化、完备性和同时间声明。

本页建立一个自然、正齐次的**经典** H，但尚未指定：
量子化规则、Hilbert 空间、算子域、cusp 处理、self-adjointness、
trace-class／正则化方案、量子 spectrum 与现有 classical
Selberg/Ruelle determinant 的身份或零点重数等式。
已有经典 determinant 的延拓也不补足这些量子义务。
不得由本页启动新的 Route 或把本页当作 Stage 5／6 授权。

保存只使用 apply_patch 新增本文件。主代理逐式构造，另由同模型
有界只读席检查能量 E 因子、(23) 和 exactness；该分工不是外部
独立科学再现。本页没有运行科学／符号程序、计算轨道、
数值估计、实验、producer 或稿件构建。
后继实际文本检查和读回状态由持续工作索引记录。

[contact]: internal_goal01_same_clock_contact_and_randers_realization_20260909.md
[nonzero]: internal_goal01_nonzero_period_and_exact_unitarizability_boundary_20260909.md
