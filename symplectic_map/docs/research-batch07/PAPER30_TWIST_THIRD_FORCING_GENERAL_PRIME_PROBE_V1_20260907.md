# Paper 30：一般奇素数幂第三内部 forcing 的准确首层

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
本轮全文读取并使用 `proof-writer`。主控与本作者共同推导本链；
作者交叉核算及有界协作检查不算非作者独审。

## Claim

令 $p\ge5$ 为任意素数、$a\ge2$，$s=p^a$，$\zeta$ 为任意本原 $s$ 次根。
保持同一物理正 kick、固定参数及 SUM action，取

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad m=(p-1)/2,\qquad M=p^{a-1}m,\qquad \chi=(-1)^{m+1}.
\tag{1}
$$

在 $K^+=\mathbb Q_p(h)$ 的整数环 $\mathcal O^+=\mathbb Z_p[h]$ 中，
使用 $v_h(h)=1$、$v_h(p)=M\ge5m$。实际分支为

$$
V_n=\rho^nv_n(L/\rho),\qquad
d_n(h)=\frac{\zeta^n+\zeta^{-n}-2}{h}=-\frac{D_n}{h},
\qquad D_n=2-\zeta^n-\zeta^{-n},
$$
$$
d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
\tag{2}
$$

只用 $n<3p$ 的实际分支定义第三 forcing

$$
\mathcal B_3(L)=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.
\tag{3}
$$

则有完整参数多项式身份

$$
\boxed{h^{-(3m+1)}p^2\mathcal B_3\in\mathcal O^+[L],\qquad
\overline{h^{-(3m+1)}p^2\mathcal B_3}
=-\frac{3\chi}{64}L^m.}
\tag{4}
$$

因此 $p^2\mathcal B_3$ 的系数最小赋值恰为 $q_3=3m+1$。
这不是先假定该层非零：证明将排除所有更低层，包括整个 $3m$ 层。

因为 $3p<p^a$，此处仍是内部非共振模态。其实际值满足

$$
\boxed{h^{-(m+1)}p^2V_{3p}\in\mathcal O^+[L],\qquad
\overline{h^{-(m+1)}p^2V_{3p}}=\frac{\chi}{384}L^m.}
\tag{5}
$$

对任何有限局部扩域中的代数整数参数 $L$，若 $\bar L\ne0$，则

$$
v_h(\mathcal B_3(L))=3m+1-2M,\qquad
v_h(V_{3p}(L))=m+1-2M.
\tag{6}
$$

若 $\bar L=0$，两者分别严格大于式 (6) 的右侧；
这里不把分歧扩域的严格不等式写成整数“加一”下界。
式 (4)—(5) 对全部参数的整性不受这项点值区分影响。

令 $\mathcal B_1$ 为同一实际分支、同一 $L$ 坐标中的第一内部 forcing，另有

$$
\boxed{\gcd_{K^+[L]}(\mathcal B_1,\mathcal B_3)=1.}
\tag{7}
$$

不声明 $\mathcal B_2,\mathcal B_3$ 互素，也不把式 (7) 解释为完整 $C_{r,s},Q_{r,s}$ 的结论。

## Status

式 (4)—(7) 及其精度、点值边界：`PROVABLE AS STATED`。

主范围严格为 $p\ge5$。三的幂及 $p=3,a=2$ 的真正共振不属于本件。
本件的作者证明状态与待完成的联合非作者核查状态分开记录。

## Assumptions and Exact Inputs

本轮全文读取并绑定以下输入：

| 输入 | SHA256 |
| --- | --- |
| [第二阶乘带响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，同轮作者稿 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| [首层内部结构 V1](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)，已接受 | `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616` |
| [第二阶乘带处置](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md)，已接受 | `e3f46a7725f7f6354695c30613219a9df67f526ab559a832f0f2e9bbfe21c213` |

只调用与本件相关的已证输入：低块 $V_i$ 整、$V_1=1/2$；
$Y_j^{\rm act}=pV_{p+j}$ 和 $Z_j^{\rm act}=p^2V_{2p+j}$ 对 $0\le j<p$ 整；
$Y_0^{\rm act}\in h^{M-m}\mathcal O^+[L]$、$Z_0^{\rm act}\in h^M\mathcal O^+[L]$；
所有严格低于 $3p$ 的所需指数系数乘 $p^2$ 后整。
还调用第一 forcing 的精确首层、其所有 $L$ 根局部整，以及

$$
\overline{h^{-m}\mathcal B_1}=\chi(2-L^m),\qquad
\frac{d_p(h)}{h^{2m}}\equiv-1\pmod h.
\tag{8}
$$

响应桥提供下文的真实／形式比较及准确耦合模型；
它不提供第三 forcing 的准确层，后者由本稿另行完成数学推导。
两稿共同派生的公式不重复记为独立贡献或非作者审查。

## Notation

令 $\mathcal N=x\partial_x$。沿用真实 Chebyshev 多项式

$$
C_0(H)=2,\quad C_1(H)=2-H,\quad C_{n+1}(H)=(2-H)C_n(H)-C_{n-1}(H),
\quad d_n(H)=\frac{C_n(H)-2}{H}.
$$

$C_n(H)$ 在此只是辅助记号，不是系统首项。低块形式分支为
$P(H,x)=\sum_{i=1}^{p-1}P_i(H,L)x^i\in\mathbb Z_{(p)}[L][[H]][x]$，
$P_i(h,L)=V_i(L)$。所用有限 $x$ 次数具有统一有限的参数次数界。
记

$$
\mathcal D x^j=d_j(H)x^j,\quad
\mathcal D_kx^j=d_{kp+j}(H)x^j,\quad \Delta_k=\mathcal D_k-\mathcal D,
$$
$$
F=\frac x2e^P+Lx^2e^{2P},\qquad
J=\frac x2e^P+2Lx^2e^{2P},\qquad
K=\frac x4e^P+2Lx^2e^{2P}\pmod{x^p}.
\tag{9}
$$

算子用于 $1\le j<p$ 的正次数。响应桥的零常数模型满足

$$
(\mathcal D_1+J)Y=J/2,\qquad
(\mathcal D_2+J)Z=-K(Y-1/2)^2\pmod{x^p},
\tag{10}
$$
$$
Y^{\rm act}-Y(h),\quad Z^{\rm act}-Z(h)\in h^{M-m}\mathcal O^+[L][x]/(x^p).
\tag{11}
$$

这些零常数是证明工具，不是把实际内部模态置零。令

$$
y=Y+\tfrac12\mathcal NP,\qquad
Q=Z-\tfrac18\mathcal N^2P+\tfrac12\mathcal Ny.
\tag{12}
$$

桥稿的准确形式身份为

$$
(\mathcal D_1+J)y=\tfrac12\Delta_1\mathcal NP,
$$
$$
(\mathcal D_2+J)Q
=(2\Delta_1-\Delta_2)\frac{\mathcal N^2P}{8}
+\frac12(\Delta_2-\Delta_1)\mathcal Ny-Ky^2.
\tag{13}
$$

从 Step 2 起，未注明的形式计算先在 $\mathbb F_p[L][[H]]$ 中进行。
实际误差仍使用 $v_h$；$O(H^r)$ 指形式整除，绝不等同于未经说明的实际误差。

## Proof Strategy and Dependency Map

1. 从同一 SUM action 的非驻值 Euler 身份得到第三端点，并把所有舍弃项界到 $h^M$。
2. 用响应桥替换两个实际块，重组为四个有准确配对缺陷的形式项。
3. 用反演不变的有限对数参数计算真实移位，保留到足够的 $H$ 精度。
4. 从准确耦合模型求移位的一阶响应及组合二阶响应的下一 $H$ 修正。
5. 用低块 $H$ 导数的首积分计算两个有限矩，避免遗漏对数在第 $p$ 项的边界贡献。
6. 证明整个 $3m$ 层取消，再求 $3m+1$ 层；最后转回实际赋值、内部模态与互素推论。

## Proof

### Step 1. 同一有限 action 与全部实际误差

取 $N_0=3p$，将实际 $V$ 截断至 $N_0-1$，定义

$$
\Phi=[x^{N_0}]\left(\frac12V\mathcal D_hV
+\frac b2xe^V+\frac L2x^2e^{2V}\right)\bigg|_{b=1}.
\tag{14}
$$

这里只把 $b$ 用作 Euler 身份中的辅助幅度；实际规范仍为 $b=1$。
在作偏导时先把 $V_i$ 看作独立变量。真实递推给出

$$
\frac{\partial\Phi}{\partial V_i}
=\frac{d_i+d_{N_0-i}}2V_{N_0-i}
+\frac12[x^{N_0-i-1}]e^V+L[x^{N_0-i-2}]e^{2V}
=\frac{d_i-d_{N_0-i}}2V_{N_0-i}.
$$

所以真实分支不是该有限泛函的驻点。
赋予 $V_i,b,L$ 权重 $i,1,2$，$\Phi$ 权重为 $N_0$；
显含的 $b,L$ 导数之和为 $-\mathcal B_3/2$。
准确加权 Euler 身份因此给出

$$
\mathcal B_3=-6p\Phi+
\sum_{i=1}^{3p-1}i(d_i-d_{3p-i})V_iV_{3p-i}.
\tag{15}
$$

动能中的非内部配对或者是低块乘第二块，或者是第一块乘第一块，
赋值均至少为 $-2M$。内部配对 $V_pV_{2p}$ 的界为 $-m-M\ge-2M$。
传播子整，势能指数次数严格低于 $3p$，乘 $p^2$ 后整。
故 $v_h(\Phi)\ge-2M$，于是 $v_h(p^3\Phi)\ge M$。

式 (15) 乘 $p^2$。$i=p,2p$ 的权重还含一个 $p$，
其贡献赋值至少为 $2M-m>M$，可模 $h^M$ 舍去。
对低／第二块配对，成对权重为 $2i-3p$，可用 $2i$ 代替；
对第一块中的权重 $p+i$ 可用 $i$ 代替。所丢项均含一个 $p$ 乘整的正规化块。
令

$$
\delta_i^{\rm low}=d_i-d_{3p-i},\qquad
\delta_i^{\rm mid}=d_{p+i}-d_{2p-i},\qquad 1\le i<p.
\tag{16}
$$

得到准确实际同余

$$
p^2\mathcal B_3\equiv
\sum_{i=1}^{p-1}\left(2i\delta_i^{\rm low}V_iZ^{\rm act}_{p-i}
+i\delta_i^{\rm mid}Y^{\rm act}_iY^{\rm act}_{p-i}\right)
\pmod{h^M\mathcal O^+[L]}.
\tag{17}
$$

两种缺陷的模 $p$ 首项都是 $6\chi iH^m$，可由 Step 3 的准确式直接读出。
它们代入实际 $h$ 后的赋值至少为 $m$，因为额外的 $p$ 倍误差高度为 $M>m$。
由式 (11)，在式 (17) 中替换实际块的每个误差至少达到
$(M-m)+m=M$；乘积之差用整因子逐个抽出该误差。
因此后续形式模型计算可决定所有严格低于 $M$ 的实际端点层。

### Step 2. 四项准确重组

令 $C_i=\delta_i^{\rm low}-\delta_i^{\rm mid}$。
把式 (12) 的

$$
Y_i=-\frac i2P_i+y_i,\qquad
Z_i=\frac{i^2}{8}P_i-\frac i2y_i+Q_i
$$

代入式 (17) 的形式版本。模 $p$ 时 $p-i=-i$，
且 $\delta_{p-i}^{\rm mid}=-\delta_i^{\rm mid}$ 精确成立。
旧块两个交叉项在 $i\leftrightarrow p-i$ 后合并，得到

$$
\begin{aligned}
\mathcal E(H,L)={}&\frac14\sum_{i=1}^{p-1}i^3 C_iP_iP_{p-i}
+\sum_{i=1}^{p-1}i^2 C_iP_i y_{p-i}\\
&+2\sum_{i=1}^{p-1}i\delta_i^{\rm low}P_iQ_{p-i}
+\sum_{i=1}^{p-1}i\delta_i^{\rm mid}y_i y_{p-i}.
\end{aligned}
\tag{18}
$$

这里是完整参数多项式身份，不是参数点上的简化。
式 (17) 与式 (18) 的关系是：若形式结果
$\mathcal E=H^q c(L)+O(H^{q+1})$ 且 $q<M$，
则实际 $p^2\mathcal B_3=h^q\widetilde c(L)+O(h^{q+1})$，
其中还需 $M\ge q+1$。本稿最后将逐项核定这一条件。

### Step 3. 准确配对缺陷与合法的有限移位参数

在 $\mathbb F_p[[\eta]]$ 中置

$$
z=1+\eta,\quad H=2-z-z^{-1}=-\eta^2/z,\quad T=z^p=1+\eta^p,
\quad u=z^i.
$$

由真实 Chebyshev 身份直接相减，得

$$
C_i=-\frac{(T-1)^2(T^2+T+1)}{T^3H}\left(u+\frac{T^2}{u}\right),
\tag{19}
$$
$$
C_i-C_{p-i}
=\frac{(T-1)^3(T^2+T+1)}{T^3H}\left(u-\frac T u\right).
\tag{20}
$$

式 (20) 的分子从 $\eta^{3p+1}$ 起，除以 $H$ 后从
$\eta^{3p-1}=\eta^{2(3m+1)}$ 起。
所以式 (18) 的第一项整个低于 $H^{3m+1}$ 的部分消失，
不是只消去一个最低系数。

为精确计算其余项，定义有限表达式

$$
\tau(T)=(T-1)-\frac{(T-1)^2}{2}+\frac{(T-1)^3}{3},\qquad
\ell(T)=\frac{\tau(T)-\tau(T^{-1})}{2},\qquad
r=\ell(T)\frac{z-z^{-1}}H.
\tag{21}
$$

没有使用特征 $p$ 下的无限对数。若 $v=T-1$，则
$\ell(1+v)=v-v^2/2+v^3/3+O(v^4)$。
有限多项式 $E_3(t)=1+t+t^2/2+t^3/6$ 满足
$T^{\pm k}=E_3(\pm k\ell(T))+O(v^4)$，$k=1,2,3$，
所用分母在 $p\ge5$ 时全为单位。

还需说明 $r$ 真正在 $H$ 的形式环中。
反演 $\sigma(z)=z^{-1}$ 同时使 $\ell(T)$ 与 $z-z^{-1}$ 变号，故 $r$ 不变。
它在 $\eta$ 中从 $-2\eta^{p-1}$ 起，没有负次数。
取 $w_0=(z-1)/(z+1)$，则 $\sigma(w_0)=-w_0$ 且

$$
H=-\frac{4w_0^2}{1-w_0^2},\qquad w_0^2=\frac{H}{H-4}.
$$

因此固定环为 $\mathbb F_p[[w_0^2]]=\mathbb F_p[[H]]$，并有

$$
r=2\chi H^m+O(H^{m+1}).
\tag{22}
$$

令以下均为正次数上的对角算子：

$$
\mathsf S_j=\frac{z^j-z^{-j}}{z-z^{-1}},\qquad
\mathsf T_j=\frac{2+Hd_j(H)}{2(H-4)},\qquad
\mathsf U_j=\frac{H\mathsf S_j}{6(H-4)}.
\tag{23}
$$

有限展开及 $(z-z^{-1})^2=H(H-4)$ 给出

$$
\Delta_k(j)=kr\mathsf S_j+k^2r^2\mathsf T_j+k^3r^3\mathsf U_j
+O(H^{4m+1}),\qquad k=1,2,3.
\tag{24}
$$

其余项先在 $\eta$ 环中属于 $\eta^{4p-2}$，来自 $(T-1)^4/H$。
准确式与保留项均反演不变，因此该余项也在固定环内；
$4p-2=2(4m+1)$，故确为式 (24) 所写的 $H$ 高度。
负的 $j$ 也可使用同式，此时 $\mathsf S,\mathsf U$ 变号而 $\mathsf T$ 不变。

Chebyshev 递推的前两项给出

$$
\mathcal D=-\mathcal N^2+H\mathsf A+O(H^2),\qquad
\mathsf A=\frac{\mathcal N^4-\mathcal N^2}{12},
\tag{25}
$$
$$
\mathsf S=\mathcal N-H\frac{\mathcal N^3-\mathcal N}{6}+O(H^2),\quad
\mathsf T=-\frac14I+H\frac{2\mathcal N^2-I}{16}+O(H^2),\quad
\mathsf U=-\frac H{24}\mathcal N+O(H^2).
\tag{26}
$$

例如 $\mathsf S_{j+1}=(2-H)\mathsf S_j-\mathsf S_{j-1}$、$\mathsf S_0=0,\mathsf S_1=1$
逐阶给出 $\mathsf S_j=j-Hj(j^2-1)/6+O(H^2)$；$d_j$ 的递推给
$d_j=-j^2+Hj^2(j^2-1)/12+O(H^2)$，其余两式由式 (23) 代入得到。

### Step 4. 独立移位参数下的单位响应

先以独立变量 $\nu$ 代替 $r$，在式 (10)—(13) 中采用对角族
$\mathcal D_k=\mathcal D+k\nu\mathsf S+k^2\nu^2\mathsf T+k^3\nu^3\mathsf U$。
正次数传播子在 $H=\nu=0$ 都是单位，故模型在
$\mathbb F_p[L][[H,\nu]][x]/(x^p)$ 中唯一。
随后代入 $\nu=r(H)$；式 (24) 的模型误差经单位三角比较仍至少为 $H^{4m+1}$，
不会影响本稿目标层。准确耦合式的右侧从 $\nu^2$ 起，所以

$$
y=\nu t(H,x)+O(\nu^2),\qquad Q=\nu^2 q(H,x)+O(\nu^3).
\tag{27}
$$

令 $\mathscr L=\mathcal D+J$。取式 (13) 的相应系数，得到

$$
\mathscr Lt=\tfrac12\mathsf S\mathcal NP,
\tag{28}
$$
$$
\mathscr Lq=-\tfrac14\mathsf T\mathcal N^2P
+\tfrac12\mathsf S\mathcal Nt-Kt^2.
\tag{29}
$$

为了求它们到一次 $H$，定义低块的辅助幅度族 $P(H,b,L,x)$，其 forcing 为
$bxe^P/2+Lx^2e^{2P}$。只对该族作参数导数，最后总取 $b=1$；
这不改变实际参数或把阶乘桥错误外推到任意 $b$。
令

$$
\mathcal T=b\partial_b+L\partial_L,\qquad
f=\mathcal TP|_{b=1},\qquad g=\mathcal T^2P|_{b=1},
\qquad w=\partial_HP|_{H=0,b=1}.
\tag{30}
$$

记 $U=P|_{H=0,b=1}$、$f_0=\mathcal TU|_{b=1}$、$g_0=\mathcal T^2U|_{b=1}$，
其中对 $U$ 的参数导数使用对应的幅度族。
低块方程及其参数导数给出准确身份

$$
\mathscr Lf=\mathcal DP,\qquad
\mathscr Lg=(\mathcal D-J)f-2Kf^2.
\tag{31}
$$

以下下标 $0$ 表示取 $H=0$；设 $\mathscr L_0=-\mathcal N^2+J_0$，则

$$
\mathscr L_0w=-\mathsf A U,\qquad
\mathscr L_0(\mathcal Tw)
=-\mathsf A f_0-(J_0+2K_0f_0)w.
\tag{32}
$$

由式 (25)—(26)，$\mathsf S\mathcal N=\mathcal N^2-2H\mathsf A+O(H^2)$。
把 $-f/2$ 代入式 (28)，它与驱动的差为
$-H\mathsf A U/2+O(H^2)=H\mathscr L_0w/2+O(H^2)$。
有限单位解唯一，所以

$$
\boxed{t=-\frac12 f+\frac H2w+O(H^2).}
\tag{33}
$$

再将式 (33) 代入式 (29)，减去 $\mathscr L(g/8+f/16)$，
使用式 (31)—(32)，差准确化为

$$
H\left(-\frac{\mathcal N^4+2\mathcal N^2}{192}U
-\frac14\mathscr L_0(\mathcal Tw)\right)+O(H^2).
$$

由于 $\mathscr L_0f_0=-\mathcal N^2U$，括号等于
$\mathscr L_0(w/16+f_0/64-\mathcal Tw/4)$。
由相同的有限唯一性，得到

$$
\boxed{q=\frac18g+\frac1{16}f
+H\left(\frac1{16}w+\frac1{64}f_0-\frac14\mathcal Tw\right)+O(H^2).}
\tag{34}
$$

等价地，若 $t=t_0+Ht_1+O(H^2)$、$q=q_0+Hq_1+O(H^2)$，则

$$
t_0=-f_0/2,\quad t_1=(w-\mathcal Tw)/2,\quad
q_0=g_0/8+f_0/16,\quad
q_1=\mathcal T^2w/8-3\mathcal Tw/16+w/16+f_0/64.
\tag{35}
$$

这些是全参数的单位方程解，不是只检验若干素数后的外推。

### Step 5. 端点在三次移位阶的完整表达式

对正次数有限级数定义双线性矩

$$
\langle f,g\rangle_2=\sum_{i=1}^{p-1}i^2 f_i g_{p-i},\qquad
\langle f,g\rangle_4=\sum_{i=1}^{p-1}i^4 f_i g_{p-i}.
\tag{36}
$$

因为 $p-i=-i$，这两个矩在模 $p$ 中均对称。
记 $B_0=\langle U,U\rangle_4$。
式 (20) 和有限参数给出

$$
C_i-C_{p-i}
=\frac{3r^3H}{H-4}\mathsf S_i+O(H^{4m+1}).
$$

式 (18) 的第一项以 $i\leftrightarrow p-i$ 配对后因此为

$$
-\frac{3}{32}r^3H B_0+O(H^{3m+2})+O(H^{4m+1}).
\tag{37}
$$

其余三项只需 $C_i=-6r^2\mathsf T_i+O(r^3)$、
$\delta_i^{\rm low}=3r\mathsf S_i+O(r^2)$、
$\delta_i^{\rm mid}=3r\mathsf S_i+O(r^2)$；这些来自式 (24) 对 $j=i,-i$ 的应用。
用式 (26)—(27) 展开，得到

$$
\mathcal E=r^3(E_0+HE_1+O(H^2))+O(H^{4m}),
\tag{38}
$$

其中取到一次 $H$ 的完整括号是

$$
\begin{aligned}
E_0+HE_1={}&\frac32\langle P,t\rangle_2
+6\langle P,q\rangle_2+3\langle t,t\rangle_2\\
&+H\left\{-\frac3{32}B_0
-\frac38\bigl(2\langle U,t_0\rangle_4-\langle U,t_0\rangle_2\bigr)\right.\\
&\hspace{18mm}-\bigl(\langle U,q_0\rangle_4-\langle U,q_0\rangle_2\bigr)\\
&\hspace{18mm}\left.-\frac12\bigl(\langle t_0,t_0\rangle_4-\langle t_0,t_0\rangle_2\bigr)\right\}
\pmod{H^2}.
\end{aligned}
\tag{39}
$$

例如第二项使用 $-6\mathsf T_i=3/2-3H(2i^2-1)/8+O(H^2)$，
第三项使用 $6i\mathsf S_i=6i^2-H(i^4-i^2)+O(H^2)$，
第四项使用 $3i\mathsf S_i=3i^2-H(i^4-i^2)/2+O(H^2)$。
这逐项解释了式 (39) 的全部传播子修正。
$O(r^4)$ 在 $r=O(H^m)$ 后至少为 $H^{4m}$；
因 $m\ge2$，它严格高于目标 $3m+1$。

### Step 6. 低块一次 $H$ 响应的准确首积分

令

$$
\theta=(1-4L)/16,\quad A(x)=1-x/2+\theta x^2,
\quad U=-\log A,\quad v=x/A,\quad G=1+\mathcal NU=\frac{1-\theta x^2}{A}.
$$

此节先在特征零使用完整形式表达式；只在说明整性后约化所需系数。
有

$$
F_0=\mathcal N^2U=v/2+Lv^2,\qquad
J_0=v/2+2Lv^2,\qquad
G^2=1+v+Lv^2,
\tag{40}
$$
$$
\mathcal NG=F_0,\quad \mathcal Nv=Gv,\quad
\mathcal NF_0=J_0G.
$$

令 $I_A(x)=\int_0^x A(t)^{-1}\,dt$，并定义

$$
\boxed{
w=-\frac{(\theta x^2-1)(x-4\theta x^2)}{16A^2}
+\frac{x^2-8x}{192A}-\frac{G I_A}{48}.}
\tag{41}
$$

它的常数项和一次项均为零：一次项为
$1/16-1/24-1/48=0$。设

$$
R=J_0G^2-F_0^2/2-(G^2-1)/2.
$$

式 (40) 给出准确多项式展开

$$
\boxed{R=(3/8+3L/2)v^2+2Lv^3+\frac32L^2v^4.}
\tag{42}
$$

记式 (41) 的前两项为 $w_{\rm rat}$。用 $\mathcal NI_A=v$ 与 $\mathcal NG=F_0$，
直接乘积求导给出

$$
G\mathcal Nw-F_0w
=G\mathcal Nw_{\rm rat}-F_0w_{\rm rat}-G^2v/48=R/12.
\tag{43}
$$

该有理身份可不借助积分约分核对：把后一等式两边乘以 $192A^4$，
共同的分子是

$$
(6+24L)x^2A^2+32Lx^3A+24L^2x^4.
$$

对式 (43) 再作用 $\mathcal N$。由式 (40)，左边成为
$G(\mathcal N^2-J_0)w$；而

$$
\mathcal NR=G(\mathcal N^4-\mathcal N^2)U.
$$

因 $G(0)=1$，可除以这个形式单位，得到
$(\mathcal N^2-J_0)w=(\mathcal N^4-\mathcal N^2)U/12$。
所以式 (41) 满足式 (32) 的低块响应方程。
它的次数小于 $p$ 的系数整，因为积分所用分母严格小于 $p$，
而其他分母仅含 $2,3$。有限单位递推的唯一性说明它正是实际形式低块的 $\partial_HP|_0$。

只有 $I_A$ 的第 $p$ 个系数可能在本次所需范围内出现一个 $p$ 分母。
其余有理项及所有更低积分系数均整，故

$$
p[x^p]w\equiv-\frac1{48}[x^{p-1}]A^{-1}\pmod p.
\tag{44}
$$

不能把这一第 $p$ 阶边界项当成零；它是下一个矩计算的必要贡献。

### Step 7. 两个所需有限矩的通用求值

记

$$
\mathcal A(H,L)=\langle P,P\rangle_2=A_0+HA_1+O(H^2).
$$

已有接受输入 $A_0=(2-L^m)/2$。因为 $A_1=2\langle U,w\rangle_2$，
在式 (43) 取第 $p$ 阶系数并约化时，
$[x^p]\mathcal NU\mathcal Nw=-\langle U,w\rangle_2$，
$[x^p]F_0w=\langle U,w\rangle_2$。
于是

$$
\boxed{A_1=\overline{p[x^p]w}-\frac1{12}[x^p]R.}
\tag{45}
$$

为准确求这些系数，先以独立变量 $a_0$ 替换 $A$ 的线性系数：
$A_{a_0}=1-a_0x+\theta x^2$。在完整多项式环中有

$$
[x^{p-1}]A_{a_0}^{-1}=(a_0^2-4\theta)^m\quad\text{于 }\mathbb F_p[a_0,\theta].
\tag{46}
$$

证明可在形式二次扩张写 $A_{a_0}=(1-r_1x)(1-r_2x)$：
左边为 $(r_1^p-r_2^p)/(r_1-r_2)=(r_1-r_2)^{p-1}$，即右边。
先在 $r_1-r_2\ne0$ 的局部化证明，再由多项式环单射延伸，
故也包括重根与退化参数，没有参数排除。

由参数导数，令 $c_k=[x^p]v^k$，则

$$
c_k=\left.
\frac{\partial_{a_0}^{k-1}(a_0^2-4\theta)^m}{(k-1)!}
\right|_{a_0=1/2,\,\theta=(1-4L)/16},\qquad 1\le k\le4.
\tag{47}
$$

分母最多为 $3!$，在全部 $p\ge5$ 时可逆。
又 $B_0=\langle U,U\rangle_4=[x^p]F_0^2$，所以

$$
B_0=c_2/4+Lc_3+L^2c_4
=\frac14L^m-\frac1{16}L^{m-1},
\tag{48}
$$
$$
[x^p]R=(3/8+3L/2)c_2+2Lc_3+\tfrac32L^2c_4
=-\frac58L^m+\frac3{32}L^{m-1}.
\tag{49}
$$

为说明式 (48)—(49) 对最小 $p=5$ 也合法，计算时先在式 (47) 的导数多项式中合并，
再使用 $2m=-1$；不写含 $0\cdot L^{-1}$ 的表达式。
具体地，式 (48) 合并前的两个系数分别为
$m^2$ 和 $m/4+m(m-1)/2+m(m-1)(m-2)/6$，
约化后为 $1/4,-1/16$。
式 (49) 的两个系数为 $3m^2/2+2m$ 和
$3m/8+m(m-1)+m(m-1)(m-2)/4$，约化后为 $-5/8,3/32$。
所有幂在合并后均为 $L^m,L^{m-1}$，指数非负。

式 (44)、式 (46) 给 $\overline{p[x^p]w}=-L^m/48$。
代入式 (45)、式 (49)，最终得到

$$
\boxed{A_1=\frac1{32}L^m-\frac1{128}L^{m-1}=B_0/8.}
\tag{50}
$$

这不是用普通剩余 $U$ 替换全部低块；式 (50) 正是其下一 $H$ 层的真实响应矩。

### Step 8. 整个 $3m$ 层取消与下一层的非零系数

低块幅度族有准确权重身份

$$
P_i(H,b,L)=b^iP_i(H,1,L/b^2).
\tag{51}
$$

先在 $b\ne0$ 处由递推证明，再以有限多项式身份延伸到全部参数。
因此每个总 $x$ 次数为 $p$ 的矩具有 $b,L$ 权重 $p$，
$\mathcal T=b\partial_b+L\partial_L$ 在它上面等于 $p-L\partial_L$。
模 $p$ 后记该作用为 $\mathfrak d=-L\partial_L$。
矩的参数导数服从双线性乘积法则，例如

$$
\mathcal T\langle U,U\rangle_2=2\langle U,f_0\rangle_2,
\quad
\mathcal T^2\langle U,U\rangle_2
=2\langle f_0,f_0\rangle_2+2\langle U,g_0\rangle_2.
\tag{52}
$$

将式 (35) 代入式 (39) 的常数层，得到

$$
E_0=\left(\frac38\mathfrak d^2-\frac3{16}\mathfrak d\right)A_0=0.
\tag{53}
$$

最后等号使用 $A_0=1-L^m/2$：$\mathfrak d$ 在常数上为零，
在 $L^m$ 上的特征值为 $-m=1/2$，所以两个部分都被消去。
因此整个 $3m$ 层取消；$r$ 自身的更高 $H$ 修正也不会在下一层乘出未控制的 $E_0$ 项。

一次 $H$ 层的完整合并为

$$
\begin{aligned}
E_1={}&\left(\frac38\mathfrak d^2-\frac{15}{16}\mathfrak d+\frac9{16}\right)A_1\\
&+\left(-\frac1{16}\mathfrak d^2+\frac5{32}\mathfrak d-\frac3{32}\right)B_0
+\left(\frac1{16}\mathfrak d^2-\frac1{64}\mathfrak d\right)A_0.
\end{aligned}
\tag{54}
$$

为明确检查式 (54) 的来源，式 (39) 第一行的响应项给出
$(3\mathfrak d^2/8-15\mathfrak d/16+9/16)A_1+3\mathfrak dA_0/64$；
花括号中的传播子修正及基线给出
$(-\mathfrak d^2/16+5\mathfrak d/32-3/32)B_0
+(\mathfrak d^2/16-\mathfrak d/16)A_0$。
相加即式 (54)，保留了低块导数、两个响应及配对缺陷的全部同阶项。

代入式 (50)，$B_0$ 的总算子化为
$-(2\mathfrak d-3)(\mathfrak d-1)/128$，
$A_0$ 的算子是 $\mathfrak d(4\mathfrak d-1)/64$。
在 $L^{m-1}$ 上 $\mathfrak d$ 的特征值为 $3/2$，该项被准确消去。
在 $L^m$ 上特征值为 $1/2$；式 (48) 的贡献为 $-L^m/512$，
$A_0$ 的贡献为 $-L^m/256$。
所以

$$
\boxed{E_1=-\frac3{512}L^m.}
\tag{55}
$$

式 (22)、式 (38)、式 (53) 遂给出

$$
\mathcal E=-\frac{3\chi}{64}H^{3m+1}L^m+O(H^{3m+2})+O(H^{4m}).
\tag{56}
$$

全部余项界为至少
$\min(3m+2,4m,M)\ge3m+2$，因为 $m\ge2$、$M\ge5m$。
形式模型与实际分支间的误差已经由 Step 1 界到 $h^M$。
把式 (56) 从形式模 $p$ 环代入 $H=h$，任何 $p$ 倍系数误差亦至少为 $h^M$。
因此实际有

$$
p^2\mathcal B_3=-\frac{3\chi}{64}h^{3m+1}L^m
+O(h^{3m+2})\quad\text{逐系数于 }\mathcal O^+[L].
\tag{57}
$$

系数 $-3\chi/64$ 在每个 $p\ge5$ 下为单位；故这既证明整性，
又证明准确最小系数赋值为 $3m+1$，完成式 (4)。

### Step 9. 实际第三内部模态、点值边界与互素性

$3p<p^2\le s$，所以 $V_{3p}=\mathcal B_3/(2d_{3p})$ 是同一真实非共振分支。
三倍频身份准确给出

$$
d_{3p}=d_p(3+hd_p)^2,\qquad
\frac{d_{3p}}{h^{2m}}\equiv-9\pmod h.
\tag{58}
$$

第二式来自输入 (8)，且 $p\ge5$ 保证 $9$ 为单位。
以式 (58) 除式 (4)，得到式 (5) 的剩余
$(-3\chi/64)/(-18)=\chi/384$。

将整多项式先代入任意有限局部扩域的代数整数参数。
若 $\bar L\ne0$，式 (4)—(5) 的剩余均非零，所以正规化值为单位，给出式 (6)。
若 $\bar L=0$，正规化值位于该扩域的极大理想，故只可普遍断言

$$
v_h(\mathcal B_3(L))>3m+1-2M,\qquad
v_h(V_{3p}(L))>m+1-2M.
\tag{59}
$$

该扩域的值群可为 $e^{-1}\mathbb Z$；因此不能由剩余消失推出整数加一界。
也不能由此推断 $\bar L=0$ 类中的全部实际零点或准确更高赋值。

最后，输入 (8) 的第一 forcing 归一化后最高系数为单位，
其所有代数 $L$ 根局部整，且每个根的剩余满足 $\bar L^m=2$。
这在 $p\ge5$ 中非零，故式 (4) 在每个这些根处都是单位剩余，
$\mathcal B_3$ 不可能同时为零。两个多项式在代数闭包中无共同根，证明式 (7)。
证明完成。$\square$

## Exact Verification Actually Run

只核对本稿新自由符号身份，没有素数或参数样本。

1. 对自由 $x,\theta$，以 $I$ 为形式原函数并在求导中使用 $I'=1/A$，
   本作者实际计算式 (41) 的二阶方程、式 (43) 的首积分、式 (42) 的正确展开，
   以及 $w_1=0$。四个约分残差全部为零。输出：
   `EXACT_PASS low-H w ODE, first integral, corrected energy polynomial, and zero first coefficient; residuals = [0, 0, 0, 0]`。
2. 对自由 $T,u,H$，实际核对式 (19)—(20) 的两个准确因式分解；残差为零。
   同时对式 (54) 的算子多项式作符号合并，$L^m,L^{m-1}$ 系数分别为 $-3/512,0$。
   输出：`EXACT_PASS paired defect factorizations; E1 monomial coefficients = -3/512 0`。
3. 主控此前独立作过同链自由符号核算；本作者另外逐项重算了响应方程及式 (39)—(54)
   的双线性系数。有界协作检查还核对了有限对数的固定环与 $H^{4m+1}$ 误差。
   这些都是作者协作，不计入正式非作者审查。

上述核对不代替一般阶乘／实际桥、有限单位唯一性、误差高度或全部参数量词的证明。

## Corrections or Missing Assumptions

- 固定 SUM action 使用式 (14) 的正动能及正势能定义；传递草式中的负系数写法是笔误，
  未用于本稿的 Euler 身份或任何端点计算。
- 能量多项式式 (42) 的末项必须是 $3L^2v^4/2$；传递草式漏写的因子 $1/2$ 已按定义纠正。
  该正确系数与 $A_1=B_0/8$、最终首层一致。
- 有限对数采用反演对称化，明确留在 $\mathbb F_p[[H]]$；没有定义特征 $p$ 的无限对数。
- $L^{m-1}$ 项的取消在完整多项式环完成，不使用 $L^p=L$ 或根方程。
- 未把组合响应的低阶公式当作全部实际高块；新一次 $H$ 修正与全部同阶项均保留。
- 对分歧扩域的零剩余参数只给严格不等式，不给未经证明的整数加一界。

## Open Risks and Delivery Boundary

- 第三 forcing 的完整 Newton 多边形、全部实际根与 $\bar L=0$ 根类的更高层仍未确定。
- 不声明 $\mathcal B_2,\mathcal B_3$ 互素，不把内部 forcing 互素替换为完整 $C_{r,s},Q_{r,s}$ 结论。
- $p=3$ 的第三内部传播子尺度及 $a=2$ 的真共振必须另行处理，不能代入本件的 $1/384$。
- 本件与响应桥仍需绑定冻结版本的联合非作者核查；作者同推、交叉计算和符号运行不是独审。
- 只新增此作者稿；已冻结响应桥、旧接受稿、入口、锁及他人文件均未改。
  无正文估页、立项、PDF、Route、外部写入或付费资源操作。
