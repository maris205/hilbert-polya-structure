# Paper30：第三 forcing 正根簇的统一 Newton 边与循环分裂域

日期：2026-09-07。主控作者稿；`p30_twist_leading_structure_probe`
与 `p30_third_forcing_general_independent` 交叉核算压缩算子，前者另核算
局部域推论。这些作者交叉检查不算本件的非作者独审。
使用 `proof-writer`，区分完整证明、待独立核查状态与未解决的负根分支。
不由五、七的幂外推，不扫描素数或拟合根。

## Claim

对任意素数 $p\ge5$、整数 $a\ge2$ 及任意本原 $p^a$ 次根 $\zeta$，保持
同一双谐波模型、物理正 kick、固定参数和 SUM action。令

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1},
$$
$$
K^+=\mathbb Q_p(h),\quad v_h(h)=1,\quad v_h(p)=M,
\quad q_3=3m+1,\quad e_*=M-q_3.
\tag{1}
$$

实际低模态满足

$$
d_nV_n=-\tfrac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},
\quad d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,
$$
$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},
\qquad S=h^{-q_3}p^2\mathcal B_3.
\tag{2}
$$

调用已接受的唯一分解 $S=P_{\rm cl}U_{\rm cl}$，其中 $P_{\rm cl}$
首一次数为 $m$、剩余为 $L^m$；$U_{\rm cl}$ 次数为 $p$，且
$U_{\rm cl}\equiv a_m=[L^m]S\pmod{h^{e_*}}$。
本件证明以下统一结论。

1. 若 $P_{\rm cl}=L^m+\sum_{j=0}^{m-1}b_jL^j$，则
   $$
   \boxed{b_0=16\chi h^{m-1}+O(h^m),\qquad
   b_j\in h^{m-j}\mathcal O^+\quad(1\le j<m).}
   \tag{3}
   $$
   $P_{\rm cl}$ 的 Newton 多边形只有连接 $(0,m-1)$ 与 $(m,0)$ 的一条边。
2. 该因子不可约、可分。其全部 $m$ 个根 $\alpha_j$ 及任意两个不同根之差满足
   $$
   \boxed{v_h(\alpha_j)=v_h(\alpha_i-\alpha_j)=t_*:=\frac{m-1}{m}
   \quad(i\ne j).}
   \tag{4}
   $$
3. 取 $\kappa^m=-16\chi h^{m-1}$，则每个单根生成域与这个 $m$ 次因子的
   分裂域均为
   $$
   \boxed{E=K^+(\kappa),\qquad [E:K^+]=e(E/K^+)=m,\quad f(E/K^+)=1.}
   \tag{5}
   $$
   这是全分歧循环扩张。按 $\mu_m\subset K^+$ 标签，可取
   $$\alpha_j=\omega_j\kappa+O(h),\qquad \omega_j\in\mu_m.\tag{6}$$
   这里 $O(h^r)$ 对有理 $r$ 表示相应扩域中赋值至少 $r$，不假设其为
   $K^+$ 内的整次幂理想。
4. 对任何有限扩域中的非零 $\ell$，若 $t=v_h(\ell)>-e_*/p$，则
   $$
   v_h(S(\ell))=
   \begin{cases}
   mt,&-e_*/p<t<t_*,\\
   (m-1)t_*+\max_jv_h(\ell-\alpha_j),&t=t_*,\\
   m-1,&t>t_*.
   \end{cases}
   \tag{7}
   $$
   在共同有限扩域中理解中间一行，允许在根处取 $+\infty$；对 $\ell=0$
   则直接有 $v_h(S(0))=m-1$。实际 forcing 和响应为
   $$
   v_h(\mathcal B_3(\ell))=q_3-2M+v_h(S(\ell)),\qquad
   v_h(V_{3p}(\ell))=m+1-2M+v_h(S(\ell)).
   \tag{8}
   $$

此外，对全部 $p\ge7$，已接受的下一层给出更精细的标签展开

$$
\boxed{\alpha_j=\omega_j\kappa-\frac{41}{384m}h
+O\bigl(h^{1+1/m}\bigr).}
\tag{9}
$$

式 (5) 只涉及正赋值 $m$ 次因子，不是整个次数 $3m+1$ forcing 的分裂域。
式 (7) 不包含负根界 $t=-e_*/p$；没有在该端点排除负因子的抵消。

## Status

上述统一正簇结论：`PROVABLE AS STATED`，本轮作者证明完成，待真正非作者联合核查。
一般负赋值 $p$ 次因子的准确 Newton 边、因子型和简单性不在本件结论中。

## Assumptions and Exact Inputs

本件调用以下明确的证明输入，不重开其未变部分。

| 输入 | 本件调用范围 |
| --- | --- |
| [已接受根簇分离](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | 实际唯一 $P_{\rm cl}U_{\rm cl}$、$U_{\rm cl}$ 误差和原次数 |
| [已接受一般下一层](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | 完整四项 $\mathcal F_3$、精确 $\mathcal R$ 响应、实际首系数；$p\ge7$ 的次首系数 |
| [已接受四次移位](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | 完整 $r^3\mathcal F_3+r^4E_4$ 端点和 $E_4$ 多项式 |
| [本轮高阶响应结构](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | 393 行冻结稿的全阶有理性、$n\le m$ 整性和全部预临界 $W$ 支撑 |
| [本轮临界投影](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | $\mathcal F_3(H,0)$ 的全部低层消失、临界系数及实际 $S(0)$ |

两个本轮作者稿与本件一起接受独立检查。本件没有以旧检查覆盖这些新引理。
全参数的高阶支撑、从支撑到准备因子的转移、局部域结论在下文另行证明。

## Notation

在形式特征 $p$ 层，使用真实 Chebyshev 低块 $P(H,b,L,x)$，最终取 $b=1$。
它在模 $x^p$ 下解

$$
\mathcal D_HP=-\frac{bx}{2}e^P-Lx^2e^{2P},\qquad
\mathcal D_Hx^i=d_i(H)x^i.
$$

令 $\mathcal N=x\partial_x$、$\delta=H\partial_H$，并定义

$$
\mathcal T=b\partial_b+L\partial_L,\quad
\mathcal R=\mathcal T-\delta,\quad
\mathscr E=H\partial_H+L\partial_L.
\tag{10}
$$

$\mathscr E$ 是形式参数的总次数算子，不是端点 $\mathcal E$。
权重与有限配对为

$$
\Omega_i=i\mathsf S_i=-d_i-Hd_i',\quad
\Psi_i=i^2\mathsf T_i,\quad
\mathsf T_i=\frac{2+Hd_i}{2(H-4)},\quad
\mathcal M[w]=\sum_{i=1}^{p-1}w_iP_iP_{p-i},\quad W=\mathcal M[\Omega].
\tag{11}
$$

记 $A=\mathcal M[\Omega']$、$B=\mathcal M[\Omega'']$、$Y=\mathcal M[\Psi]$、
$X=\mathcal M[i^2\Omega]$。这里只在相应前置 $H$ 因子所需的精度使用导数。
特别地 $HA,H^2B$ 在模 $H^m$ 下不需要未知的第 $m$ 阶权重。

## Proof Strategy and Dependency Map

1. 在 $H<m$ 的合法反射偶性层，把完整四项端点压缩为一个作用于 $W$ 的算子。
2. 用新有理性引理提供的预临界矩支撑，以及总次数 $m$ 处的算子零特征值，
   消去全部所需临界混合项；不假设临界 $W$ 自身为零。
3. 与独立计算的纯 $H$ 临界常数、四次移位项和实际误差桥合并，得到逐系数估值。
4. 转移到唯一首一正簇因子，显式缩放后应用简单根 Hensel 提升，确定全部根域。
5. 由两两根距离和单位负因子给出点值公式，并用已接受次首层求第一平移修正。

## Proof

### Step 1. 合法反射层与幅度齐次性

真实 Chebyshev 系数在 $0\le k<m$ 满足

$$
[H^k]\Omega_i=
\frac{(-1)^ki^2\prod_{s=1}^k(i^2-s^2)}{(2k+1)!}.
\tag{12}
$$

分母是 $p$-单位，故它是 $i$ 的偶多项式，并在 $i,p-i$ 上取相同值。
$\Psi_i$ 的同层系数也是 $p$-整偶多项式，由式 (11) 和 $d_i$ 的真实展开得到。
于是下文配对恒等式严格成立于 $\mathbb F_p[L][[H]]/(H^m)$。
不把这个偶性扩张到临界纯 $H^m$；该层由另稿处理真实奇偶缺陷。

低块的三角唯一性给出准确幅度齐次式

$$
P(H,b,L,x)=P(H,1,L/b^2,bx).
$$

它可在 $b$ 可逆环中推导，再取 $b=1$；两侧的原系数均为 $b,L$ 多项式。
因此 $\mathcal T P=(\mathcal N-L\partial_L)P$。
有限配对总 $x$ 次数为 $p$，在特征 $p$ 中其幅度导数为 $-L\partial_L$，
故配对上的 $\mathcal R$ 为 $-\mathscr E$。

### Step 2. 完整三次端点的压缩恒等式

调用已证明的精确响应

$$
t=-\tfrac12\mathcal RP,\qquad
q=\tfrac18\mathcal R^2P-\frac{\mathcal RP}{4(H-4)}
\tag{13}
$$

及完整四项端点

$$
\mathcal F_3=\frac{3H}{8(H-4)}X
-6\sum_i\Psi_iP_it_{p-i}
+6\sum_i\Omega_iP_iq_{p-i}
+3\sum_i\Omega_it_it_{p-i}.
\tag{14}
$$

对任一合法偶权 $w$，乘积求导与反射对称给

$$
2\sum_iw_iP_i(\mathcal RP)_{p-i}
=-\mathscr E\mathcal M[w]+\mathcal M[\delta w],
$$
$$
\sum_iw_i\{P_i(\mathcal R^2P)_{p-i}
+(\mathcal RP)_i(\mathcal RP)_{p-i}\}
=\tfrac12\{\mathscr E^2\mathcal M[w]
-2\mathscr E\mathcal M[\delta w]+\mathcal M[\delta^2w]\}.
\tag{15}
$$

第二式可直接对第一式再求一次导数：导数作用于权重贡献
$\mathcal Rw=-\delta w$，两个 $P$ 因子各产生一项。
所有求和仍限于 $1\le i<p$，没有第 $p$ 个低块系数的边界项。
代入式 (13)—(15) 得

$$
\begin{aligned}
\mathcal F_3={}&\frac{3H}{8(H-4)}X
+\frac32\{-\mathscr EY+\mathcal M[\delta\Psi]\}\\
&+\frac38\{\mathscr E^2W-2\mathscr E(HA)+HA+H^2B\}
-\frac3{4(H-4)}\{-\mathscr EW+HA\}.
\end{aligned}
\tag{16}
$$

两个真实 Chebyshev 微分身份为

$$
\Psi+\frac H2\Omega'=-\frac{H-2}{2(H-4)}\Omega=:g\Omega,
\qquad
i^2\Omega=\Omega+H(H-4)\Omega''+3(H-2)\Omega'.
\tag{17}
$$

第一式由 $d_i$ 的 Chebyshev 方程和 $\Omega=-d_i-Hd_i'$ 代入得到；
第二式为 $\mathsf S_i$ 的微分方程
$H(4-H)\mathsf S_i''+(6-3H)\mathsf S_i'+(i^2-1)\mathsf S_i=0$ 乘以 $i$。
这些也是整数 Chebyshev 多项式的恒等式，$H-4$ 在所用形式环中可逆。

为显示全部取消而不是只给目标算子，式 (17) 依次给

$$
Y=gW-HA/2,\quad
\mathcal M[\delta\Psi]=Hg'W+H(g-1/2)A-H^2B/2,\quad
X=W+H(H-4)B+3(H-2)A.
$$

把前两式代入式 (16)，在保留首项 $3HX/[8(H-4)]$ 时，其余部分是

$$
\frac38\left\{\mathscr E^2W+\frac{2(H-1)}{H-4}\mathscr EW
-\frac{3H(H-2)}{H-4}A-H^2B\right\}.
$$

最后代入 $X$ 的表达式，$A,B$ 两项分别准确取消，得到

$$
\boxed{\mathcal F_3=\frac38
\left\{\mathscr E^2+\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}\right\}W
\pmod{H^m}.}
\tag{18}
$$

算子中的有理系数均在左边乘法，不把 $\mathscr E$ 移过它们。
式 (18) 保留第一配对项；丢掉该项就不会取消 $A,B$。

### Step 3. 全部所需混合支撑

新高阶响应稿给出

$$
[H^kL^j]W=\delta_{j0}\beta_k,
\quad \beta_k=\frac{(k!)^2}{(2k+1)!},\qquad k+j<m.
\tag{19}
$$

对 $k+j=m$、$j>0$，该稿没有把 $W$ 系数设成零，而是证明它具有合法的
$p$-整有理核。以下消失来自式 (18) 的算子，非未经证明的临界核最高主部取消。

展开左乘系数的常数项：

$$
\frac{2(H-1)}{H-4}=\frac12+O(H),\qquad
\frac H{H-4}=O(H).
$$

固定 $j>0$、$k+j=n\le m$。此时 $k<m$，所以可用式 (18)。
不含额外 $H$ 的部分在 $H^kL^j$ 上乘以
$n(n+1/2)$。若 $n<m$，它所乘的 $W$ 系数由式 (19) 为零；
若 $n=m$，则 $2m+1=p=0$ 于 $\mathbb F_p$，故该乘子本身为零。
其余各项至少带一个额外 $H$，只能调用总阶严格小于 $n\le m$ 且仍有
正 $L$ 次数的 $W$ 系数，全部由式 (19) 消失。于是

$$
\boxed{[H^kL^j]\mathcal F_3=0\qquad(j>0,\ k+j\le m).}
\tag{20}
$$

所有系数已经在有限特征 $p$ 低块中定义并且 $p$-整，不存在把
$0$ 乘以一个隐藏 $p^{-1}$ 的步骤。
纯 $L^0$ 的临界系数不在式 (20) 的范围；本轮独立投影稿证明

$$
\mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}).
\tag{21}
$$

该证明使用真实临界 Chebyshev 系数及有限和，而不是将式 (18) 擅自延至 $H^m$。

### Step 4. 实际逐系数桥与首一因子

已接受完整端点和四次组成量为

$$
\mathcal E=r^3\mathcal F_3(H,L)+r^4E_4(L)+O(H^{4m+1}),
\quad r=2\chi H^m(1+O(H)),
$$
$$
E_4(L)=-\frac3{32}+\frac3{64}\sum_{j=1}^{m-1}(2j-1)(4L)^j.
\tag{22}
$$

误差为逐系数误差。对 $1\le j<m$，式 (20) 给
$[L^j]\mathcal F_3\in H^{m-j+1}\mathbb F_p[[H]]$。
所以三次项除以 $H^{q_3}$ 后属于 $H^{m-j}$；四次项除后从
$H^{m-1}$ 起，对 $j\ge1$ 满足 $m-1\ge m-j$；余项除后从 $H^m$ 起。

纯常数结合式 (21)、(22) 得到同阶相撞的准确总系数

$$
[H^{4m}]\mathcal E(H,0)
=(2\chi)^3\frac{3\chi}{32}+(2\chi)^4\left(-\frac3{32}\right)
=\frac34-\frac32=-\frac34.
\tag{23}
$$

响应桥将实际 $p^2\mathcal B_3$ 与 $H=h$ 的形式端点比较到模 $h^M$。
本轮所需的 $4m+1$ 精度合法，因为

$$
M\ge pm=(2m+1)m\ge4m+1\qquad(m\ge2).
\tag{24}
$$

最后一个不等式之差是 $2m^2-3m-1$，在 $m=2$ 为一，之后递增。
形式系数的不同整提升相差 $p$ 倍，也落入所用实际误差以上。
因此在原规范中

$$
S(0)=-\frac34h^{m-1}+O(h^m),\quad
[L^j]S\in h^{m-j}\mathcal O^+\ (1\le j<m),\quad
a_m=-\frac{3\chi}{64}+O(h).
\tag{25}
$$

这里 $p\ge5$ 使 $3,4,64$ 全为单位，特别地首常数均非零。

由已接受 $U_{\rm cl}\equiv a_m\pmod{h^{e_*}}$ 及
$S=P_{\rm cl}U_{\rm cl}$，得到逐系数同余
$S\equiv a_mP_{\rm cl}\pmod{h^{e_*}}$。
所需精度不超过 $m$，而

$$
e_*=M-3m-1\ge(2m-2)m-1\ge m\qquad(m\ge2).
\tag{26}
$$

故式 (25) 除以单位 $a_m$ 给出式 (3)，其中
$(-3/4)/(-3\chi/64)=16\chi$。

### Step 5. 单边、全部根和循环分裂域

连接 $(0,m-1)$ 与 $(m,0)$ 的线在整数 $1\le j<m$ 处高为
$(m-1)(m-j)/m$。式 (3) 给出的下界与它的差是

$$
(m-j)-\frac{(m-1)(m-j)}m=\frac{m-j}m>0.
$$

两端系数非零，所有中点严格在线上方，故 Newton 多边形恰为上述单边。
下面再用显式局部域证明简单性、全部根的位置和不可约性，
不以单边本身替代这些结论。

在固定代数闭包中取 $\kappa^m=-16\chi h^{m-1}$。
则 $v_h(\kappa)=(m-1)/m$，此分数分母为 $m$。
有限扩域的赋值群为 $\frac1e\mathbb Z$，故
$m\mid e(K^+(\kappa)/K^+)$；而 $\kappa$ 满足次数 $m$ 方程，
所以该扩张的次数和分歧指数都恰为 $m$、剩余次数为一。

因为 $m\mid p-1$ 且 $p\nmid m$，$\mathbb F_p$ 中的全部 $m$ 次单位根
通过简单根 Hensel 提升位于 $\mathbb Q_p\subset K^+$。
于是 $X^m+16\chi h^{m-1}$ 的全部根是 $\omega_j\kappa\in E$。
它在特征零可分，因此 $E/K^+$ 是 Galois 扩张；
$\sigma\mapsto\sigma(\kappa)/\kappa$ 把其 Galois 群嵌入循环群 $\mu_m$，
两群阶数均为 $m$，故扩张循环。

在 $E$ 的赋值环中，考虑

$$
Q(y)=\frac{P_{\rm cl}(\kappa y)}{\kappa^m}.
\tag{27}
$$

首系数是一，常数项为 $-1+O(h)$；第 $j$ 个中项的系数赋值至少
$(m-j)/m>0$。所以 $\overline Q=y^m-1$ 于剩余域 $\mathbb F_p$。
其 $m$ 个不同根均为简单根，Hensel 引理给出 $Q$ 的全部 $m$ 个根
$y_j\in E$，且 $y_j\equiv\omega_j$ 模极大理想。
所有误差系数至少有赋值 $1/m$，且导数为单位，故
$v_h(y_j-\omega_j)\ge1/m$。令 $\alpha_j=\kappa y_j$，得式 (4)、(6)：
不同 $y_j$ 的剩余不同，故 $v_h(y_i-y_j)=0$。

每个 $\alpha_j$ 的赋值分母为 $m$，故 $[K^+(\alpha_j):K^+]\ge m$；
而 $\alpha_j$ 满足首一次数 $m$ 的 $P_{\rm cl}$，所以等号成立。
因此 $P_{\rm cl}$ 不可约，各单根域均等于 $E$，且 $E$ 为该因子的分裂域。
不同剩余标签也证明全部实际根简单。式 (5) 得证。

### Step 6. 点值、临界距离和第一平移修正

若 $t>-e_*/p$，$U_{\rm cl}(\ell)$ 的常数是单位，各非恒定系数赋值至少
$e_*$。当 $t\ge0$ 时每个非恒定项赋值为正；当 $-e_*/p<t<0$ 时，
次数 $i\le p$ 给 $e_*+it\ge e_*+pt>0$。
因此 $v_h(U_{\rm cl}(\ell))=0$，并有

$$
v_h(S(\ell))=\sum_{j=1}^m v_h(\ell-\alpha_j).
\tag{28}
$$

当 $t<t_*$ 时每项为 $t$；当 $t>t_*$ 时每项为 $t_*$。
当 $t=t_*$ 时每项至少为 $t_*$。若其中一项严格大于 $t_*$，
由 $v_h(\alpha_i-\alpha_j)=t_*$ 和非阿基米德三角关系，其余全部等于 $t_*$；
若无严格大于者，所有项都等于 $t_*$。
这证明式 (7)，包括根处的无穷值。式 (8) 由原实际规范及已接受
$d_{3p}$ 的赋值直接得到，不改变参数归一化。

最后设 $p\ge7$，令 $c=41/384$。已接受下一层给
$b_{m-1}=ch+O(h^2)$，其中 $m,384$ 都是 $p$-单位。
在 $L=z-ch/m$ 中，$L^m+chL^{m-1}$ 的 $hz^{m-1}$ 项准确取消。
代入 $z=\omega_j\kappa$ 时，未取消的二次及更高平移项赋值至少
$(m-1)+2/m$；式 (3) 的 $j\le m-2$ 项具有同一下界。
$b_0-16\chi h^{m-1}$ 的赋值至少为 $m\ge(m-1)+2/m$，
$b_{m-1}-ch$ 的贡献也不低于此界。
因而

$$
v_h\bigl(P_{\rm cl}(\omega_j\kappa-ch/m)/\kappa^m\bigr)\ge2/m.
$$

缩放多项式的导数仍为单位，简单根提升使 $y$ 的修正赋值至少为 $2/m$；
再乘 $\kappa$ 得原根的误差至少为 $(m-1)/m+2/m=1+1/m$。
这证明式 (9)。当 $p=41$ 时平移系数自身更高赋值，证明和误差界仍有效；
没有把该零剩余误称为特殊因子分裂。全部结论得证。∎

## Corrections or Missing Assumptions

- 临界混合矩 $[H^kL^j]W$、$k+j=m,j>0$ 不需要为零；消失来自
  $\mathscr E^2+\mathscr E/2$ 的零特征值。这避免了一个不必要且未证明的最高主部假设。
- 纯临界 $H^m$ 不享有前置偶性，必须保留另稿的真实 Chebyshev 缺陷和四次移位碰撞。
- 每次取分裂域都指 $P_{\rm cl}$，不包括仍未解决的负赋值次数 $p$ 因子。

## Open Risks and Scope Boundary

1. 本件及两个新输入尚须本轮真正非作者检查；作者交叉推导不是独立接受。
2. 一般负根的准确斜率、因子型和简单性，第二／第三 forcing 的一般互素，
   完整素数幂 $C,Q$ 及实际参数根全实性，均未由本件解决。
3. 本件是同一模型族内的数学证明，不是新意认证、篇幅认证、正式 Paper30 立项或 Route 评价。
4. 全部旧冻结稿、原失败和已接受特殊素数结论保留；统一结论取代的是当前开放边界，
   不是对旧稿内容进行覆盖或改写。
