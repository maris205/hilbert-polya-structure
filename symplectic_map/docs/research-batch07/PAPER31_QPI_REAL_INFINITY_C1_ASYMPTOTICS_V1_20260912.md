# Paper31 Q4: two real infinity ends with controlled first derivatives

日期：2026-09-12 UTC。作者：`/root/p31_real_components_and_return`。
状态：AUTHOR_PROOF_FROZEN / INDEPENDENT_REVIEW_PENDING；只补原 Q4 的无穷端，不自授查新或准入。
本件保持全部固定 $T>0$ 的量词；没有 CAS、采样、枚举、数值拟合、外部查询或再委派。

## 1. Claim, assumptions and notation

原完整有限纤维及标点为
$$
W_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad T>0,\quad P=(0,T),\quad O=[0:1:0].
$$
采用 [GEO] 已证的实际实曲面同构、分支定位与正向微分 $\omega=du/(2v+hu-T)$。
令 $Y=v+(hu-T)/2$，则
$$
Y^2=f_h(u)=u^3+(h^2/4-T)u^2-hTu/2+T^2/4,\qquad \omega=du/(2Y).
$$
在下外区间研究实际 $F_T=+P$，在上外区间研究实际分支回返 $F_T^2=+2P$。
分别取正向旋转数唯一提升 $0<\rho_-<1$ 与 $0<\rho_+<1$。
$P=(0,T/2)$，而 $2P=(T,T(h-1)/2)$，这里坐标已是 $(u,Y)$。
设 $\Omega_\pm>0$ 为 identity 实圆的一个完整周期；另一实圆的同一回返角度相同。
写
$$
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T,\quad q=8h-9,\quad
J_\pm=\frac{\delta}{q}\Omega_\pm^2\frac{d\rho_\pm}{dh}.
$$
此处 $q$ 仅为这个线性式，不是 elliptic modulus 或时间参数。

**定理（PROVABLE AS STATED）。** 对每个固定 $T>0$，令 $L=|h|\to\infty$，则
$$
\begin{aligned}
\rho_-&\longrightarrow 5/8,& J_-&\longrightarrow (\log T)/8 &&(h\to-\infty),\\
\rho_+&\longrightarrow 3/4,& J_+&\longrightarrow -(\log T)/4 &&(h\to+\infty).
\end{aligned}\tag{1}
$$
两个 $J$ 的误差均为 $O_T((\log L)/L)$；特别地 $T=1$ 时二者极限准确为零。
证明将给出 $\Omega$ 和短弧积分的带一阶导数余项，不能将未控制的 $o(1)$ 直接求导。
上端的 $J_+$ 使用二次回返；若消费 [ACNODE] 的 forcing 方法，右端必须乘二。
本件的 (1) 直接由实积分证明，不需要预先使用那个微分方程。

固定 $\sigma\in\{-1,+1\}$，令 $h=\sigma/\varepsilon$、$\varepsilon=L^{-1}>0$、$\ell=\log(1/\varepsilon)$、$c=\log T$。
记 $R=O_{C^1,T}(\varepsilon^a\ell^b)$ 表示对充分小 $\varepsilon>0$，
$|R(\varepsilon)|+|\varepsilon R'(\varepsilon)|\le C_T\varepsilon^a\ell^b$。
阈值和常数可以依赖固定 $T$；不声称在 $T\to0$ 或 $T\to\infty$ 一致。
该记号中的导数始终是 $\varepsilon$ 导数；原 $h$ 导数准确为 $\partial_h=-\sigma\varepsilon^2\partial_\varepsilon$。

## 2. Strategy and dependencies

1. 解析隐函数定理产生全部三个根及其带导数尺度，不依赖有限根表。
2. 对完整实周期的 elementary integral 自证对数常数和一阶余项。
3. 对不完整短弧积分提取一个 $\operatorname{arsinh}$，同时控制参数导数。
4. 先对得到的 $C^1$ 展开求导，再消去主导对数项，最后计算 $J$。

除 [GEO] 的原对象与真实回返外，渐近证明只用解析隐函数定理、积分变量代换及下述显式估计。
完整椭圆积分可以作为记号，但不援引未实读的渐近定理或文献常数。

## 3. Three roots and exact positive real integrals

代入 $u=\sigma T\varepsilon+\varepsilon^2 z$ 后，$\varepsilon^{-2}f_{\sigma/\varepsilon}(u)$ 等于
$$
\Phi_\sigma(\varepsilon,z)=z^2/4-T^3+\sigma\varepsilon(T^3-2T^2z)
+\varepsilon^2(3T^2z-Tz^2)+3\sigma T\varepsilon^3z^2+\varepsilon^4z^3.
$$
在 $\varepsilon=0$ 有两个简单实根 $z_\pm(0)=\pm2T^{3/2}$，其 $z$ 偏导为 $z_\pm(0)/2\ne0$。
故有实解析的 $z_\pm(\varepsilon)$；对小正 $\varepsilon$，小根与余下大负根为
$$
\begin{aligned}
r_2&=\sigma T\varepsilon+\varepsilon^2z_-(\varepsilon),&
r_3&=\sigma T\varepsilon+\varepsilon^2z_+(\varepsilon),\\
r_1&=T-1/(4\varepsilon^2)-r_2-r_3.
\end{aligned}
$$
根严格满足 $r_1<r_2<r_3$；前两根为不同解析实根，第三根由 Vieta 公式也是实根。
以解析 Taylor 余项记号写出
$$
D:=r_3-r_1=\frac1{4\varepsilon^2}\bigl(1+O_{C^1,T}(\varepsilon^2)\bigr),\quad
d:=r_3-r_2=4T^{3/2}\varepsilon^2\bigl(1+O_{C^1,T}(\varepsilon)\bigr).
\tag{2}
$$
因此 $\kappa:=\sqrt{d/D}=4T^{3/4}\varepsilon^2(1+O_{C^1,T}(\varepsilon))$，且
$\varepsilon\kappa'/\kappa=2+O_T(\varepsilon)$。
这些是根方程的解析结论，不是仅知道连续根后形式求导。

在 identity 圆令 $u=r_3+s^2$，$Y=s\sqrt{(s^2+D)(s^2+d)}$，$s\in\mathbb R\mathbf P^1$。
正向一次遍历为 $s$ 从负无穷到正无穷；它与 $\omega$ 的正方向一致。
令 $U_-=0$、$U_+=T$；由根展开，对相应两端 $B_\sigma:=U_\sigma-r_3>0$。
在两端足够远时，实际回返点均有正 $Y$；上端用到了 $h>1$，没有将此假设用于整个上区间。
所以真实正向积分准确为
$$
\Omega=\int_{r_3}^{\infty}\frac{du}{\sqrt{f_h(u)}},\quad
A_\sigma=\frac12\int_{r_3}^{U_\sigma}\frac{du}{\sqrt{f_h(u)}},\quad
\rho_\sigma=\frac12+\frac{A_\sigma}{\Omega}.
\tag{3}
$$
$0<A_\sigma<\Omega/2$ 保证式 (3) 就是指定的 $(0,1)$ 提升，不存在未知整数常数。

## 4. Complete logarithmic integral with derivative control

令
$$K_c(\kappa)=\int_0^\infty\frac{dt}{\sqrt{(1+t^2)(\kappa^2+t^2)}}.$$
代换 $u=r_3+Dt^2$ 给 $\Omega=2K_c(\kappa)/\sqrt D$。
下面直接证明在 $\kappa\downarrow0$ 时
$$
K_c(\kappa)=\log(4/\kappa)+E(\kappa),\qquad
|E|+|\kappa E'|\le C\kappa^2\log(1/\kappa).
\tag{4}
$$
从积分减去 $\int_0^1dt/\sqrt{\kappa^2+t^2}=\operatorname{arsinh}(1/\kappa)$，余下为
$$
R(\kappa)=\int_0^1\frac{a(t)\,dt}{\sqrt{t^2+\kappa^2}}
+\int_1^\infty\frac{dt}{\sqrt{1+t^2}\sqrt{t^2+\kappa^2}},\quad
a(t)=(1+t^2)^{-1/2}-1.
$$
因为 $|a(t)|\le Ct^2$，可令 $\kappa=0$ 得到有限积分。
取 $F(t)=\log(t/(1+\sqrt{1+t^2}))$，则 $F'(t)=1/(t\sqrt{1+t^2})$。
代入两段原函数并用 $F(t)-\log t\to-\log2$、$F(t)\to0$（分别 $t\to0,\infty$），得到 $R(0)=\log2$。
在 $0<t<\kappa$ 用 $|(t^2+\kappa^2)^{-1/2}-t^{-1}|\le t^{-1}$，在 $\kappa<t<1$ 用上界 $\kappa^2/(2t^3)$；
乘以 $|a(t)|\le Ct^2$ 并积分，得到 $|R(\kappa)-R(0)|\le C\kappa^2\log(1/\kappa)$。
在 $t\ge1$ 的差值积分为 $O(\kappa^2)$。
对每个 $\kappa>0$ 可在积分号下求导；其绝对值由这些可积核控制。
再乘 $\kappa$ 后，第一段核的绝对值为 $\kappa^2|a(t)|/(t^2+\kappa^2)^{3/2}$。
在 $t<\kappa$ 与 $t>\kappa$ 分段积分分别是 $O(\kappa^2)$ 与 $O(\kappa^2\log(1/\kappa))$；尾段仍是 $O(\kappa^2)$。
最后 $\operatorname{arsinh}(1/\kappa)-\log(2/\kappa)$ 及其 $\kappa\partial_\kappa$ 导数均为 $O(\kappa^2)$，证明 (4)。

由 (2)、(4) 及链式法则，
$$
K_c(\kappa(\varepsilon))=2\ell-3c/4+O_{C^1,T}(\varepsilon),\qquad
\Omega=\varepsilon\bigl(8\ell-3c+R_\Omega(\varepsilon)\bigr),\quad
R_\Omega=O_{C^1,T}(\varepsilon).
\tag{5}
$$
这里 $D$ 的相对 $O_{C^1}(\varepsilon^2)$ 误差乘对数后仍为 $O_{C^1}(\varepsilon)$，未丢掉导数控制。

## 5. Incomplete integral with two moving scales

式 (3) 令 $t=u-r_3$，得到
$$
A_\sigma=\frac1{2\sqrt D}\int_0^{B_\sigma}
\frac{(1+t/D)^{-1/2}}{\sqrt{t(t+d)}}\,dt.
$$
其不带 $D$ 修正的积分准确是 $2\operatorname{arsinh}\sqrt{B_\sigma/d}$。
令 $\eta=d/B_\sigma$、$\zeta=B_\sigma/D$；作 $t=B_\sigma x$ 后误差为
$$
\mathcal E(\eta,\zeta)=\int_0^1
\frac{(1+\zeta x)^{-1/2}-1}{\sqrt{x(x+\eta)}}\,dx.
$$
对小正 $\eta,\zeta$，由 $|(1+\zeta x)^{-1/2}-1|\le C\zeta x$ 得
$$
|\mathcal E|+|\eta\partial_\eta\mathcal E|+|\zeta\partial_\zeta\mathcal E|\le C\zeta.
\tag{6}
$$
导数积分合法，因为固定正参数时核可积；$\eta$ 导数再用 $\eta/(x+\eta)\le1$，$\zeta$ 导数直接用同一 $C\zeta x$ 上界。
这一步控制了两个移动尺度，而非只给固定参数的积分误差。

根展开分别给
$$
B_-=T\varepsilon(1+O_{C^1,T}(\varepsilon)),\qquad
B_+=T(1+O_{C^1,T}(\varepsilon)).
$$
因而 $\eta_-=4\sqrt T\varepsilon(1+O_{C^1,T}(\varepsilon))$，
$\eta_+=4\sqrt T\varepsilon^2(1+O_{C^1,T}(\varepsilon))$，而 $\zeta_-=O_{C^1,T}(\varepsilon^3)$、$\zeta_+=O_{C^1,T}(\varepsilon^2)$。
各正参数的 $\varepsilon$ 对数导数有界，故 (6) 给沿下、上路径分别为 $O_{C^1,T}(\varepsilon^3)$、$O_{C^1,T}(\varepsilon^2)$ 的误差。
使用准确恒等式
$$
\operatorname{arsinh}(\eta^{-1/2})=
\log2-\tfrac12\log\eta+\log\frac{1+\sqrt{1+\eta}}2,
$$
最后一项及其 $\eta\partial_\eta$ 导数均为 $O(\eta)$，得到
$$
A_- =\varepsilon\bigl(\ell-c/2+R_-(\varepsilon)\bigr),\qquad
A_+ =\varepsilon\bigl(2\ell-c/2+R_+(\varepsilon)\bigr),\quad
R_\pm=O_{C^1,T}(\varepsilon).
\tag{7}
$$
这同时证明两端短弧的常数和一阶余项，不用不完整椭圆积分的外部渐近公式。

## 6. Differentiate first, then take the weighted limit

令 $a_-=1$、$a_+=2$，$B=8\ell-3c$、$C_\sigma=a_\sigma\ell-c/2$，以及 $r=R_\Omega$、$s=R_\sigma$。
则 $\Omega=\varepsilon(B+r)$、$A=\varepsilon(C_\sigma+s)$，其中 $|r|+|s|\le C_T\varepsilon$、$|r'|+|s'|\le C_T$。
因此真正求导并相消得
$$
\Omega A_\varepsilon'-A\Omega_\varepsilon'
=\varepsilon(3a_\sigma-4)c+O_T(\varepsilon^2\ell).
\tag{8}
$$
其主项来自 $\varepsilon^2(BC_\sigma'-C_\sigma B')=\varepsilon(-a_\sigma B+8C_\sigma)$；
各含 $r,s$ 的项由已证一阶界至多为 $O_T(\varepsilon^2\ell)$。
利用准确的 $\partial_h=-\sigma\varepsilon^2\partial_\varepsilon$，式 (8) 给
$$
\Omega^2\rho_h'=-\sigma(3a_\sigma-4)c\varepsilon^3+O_T(\varepsilon^4\ell),\qquad
\rho_h'=-\frac{\sigma\varepsilon\bigl((3a_\sigma-4)c+O_T(\varepsilon\ell)\bigr)}{(8\ell-3c+r)^2}.
\tag{9}
$$
原多项式还直接给 $\delta/q=\sigma(1+O_T(\varepsilon))/(8\varepsilon^3)$，所以
$$J_\sigma=-(3a_\sigma-4)c/8+O_T(\varepsilon\ell).$$
这就是 (1) 中两个加权极限；$T=1$ 时 $c=0$，同一估计仍给 $J_\pm\to0$，无需除以 $c$。
式 (5)、(7) 的比值同时给 $\rho_\sigma\to1/2+a_\sigma/8$，即 $5/8$ 与 $3/4$。
更准确地，$\rho_\sigma=1/2+a_\sigma/8+(3a_\sigma-4)c/[8(8\ell-3c)]+O_T(\varepsilon/\ell)$。
这里最后的比值余项不承担求导义务；求导已由 (8)–(9) 的独立 $C^1$ 控制完成。∎

## 7. Remaining scope and actual verification

本件证明两个无穷端及所需一阶余项；没有替主控证明上区间全部符号、$q=0$ 桥或全局 twist 个数。
不声称两无穷极限本身具有足够新意，不改变原 Q4 的全参数目标或 Paper31 页数／准入门槛。
实际公开查询为零，故无检索账本条目；未下载或引用未经核准的椭圆积分渐近来源。
本人本轮 FULL 读 proof-writer、[ACNODE] 与 [MIDDLE]；[GEO] 是本人上一任务 FULL 读回冻结稿，当前哈希已复核未变。
输入 SHA256：[GEO] `f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196`；
[ACNODE] `9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d`；
[MIDDLE] `4b07925048eb416d431d1e924c7d54a46c90c1a9b08708b6647c4430a79860a3`。
只新建本件，未改已冻结几何、旧 twist 稿、BATCH、README、锁、失败或已接受产物。

[GEO]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[ACNODE]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[MIDDLE]: PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
