# Paper30：第三 forcing 的完整四次移位剩余

日期：2026-09-07。作者：主控；`p30_third_forcing_general_independent`
核对了消去响应和常数项的作者推导。这些交叉核算不计非作者独审。
本件按 `proof-writer` 写出准确形式组成量，不把它单独称为实际 forcing 的下一层。

## Claim

对任意素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
沿用已接受的第三 forcing 形式端点 $\mathcal E(H,L)$、
合法有限移位参数 $r(H)=2\chi H^m+O(H^{m+1})$，以及完整三次响应 $\mathcal F_3(H,L)$。
存在全参数多项式 $E_4(L)\in\mathbb F_p[L]$，满足逐系数身份

$$
\mathcal E=r^3\mathcal F_3(H,L)+r^4E_4(L)+O(H^{4m+1}),
\tag{1}
$$
$$
\boxed{E_4(L)=-\frac3{32}
+\frac3{64}\sum_{k=1}^{m-1}(2k-1)(4L)^k.}
\tag{2}
$$

特别地，$E_4(0)=-3/32\ne0$，且 $\deg E_4=m-1$。
本件的 $E_4$ 只是四次移位在 $H=0$ 的系数；
在实际端点的 $H^{4m}$ 层还必须同时保留 $r^3\mathcal F_3$。
本件不独自确定该实际层，更不独自证明一般正根的准确赋值或简单性。

## Status

式 (1)、(2)：`PROVABLE AS STATED`，作者证明完成，待本轮真正非作者核查。
没有从五的幂有限表外推一般素数；下文从全素数单位耦合方程直接推导。

## Assumptions and Exact Inputs

| 已接受输入 | 有限调用 | SHA256 |
| --- | --- | --- |
| [一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，843行 | 式 (13)、(18)、(24) 的耦合、端点、有限移位；准确配对及 $A_0$ | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| [第二阶乘响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，640行 | 零常数单位模型的定义；实际内部常数仍在原误差中 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |

本件不调用尚待独审的新一般二阶矩或下一层来证明式 (2)，
也不重开上述旧接受证明。五的幂旧式仅可作结果的一致性观察，不是本件的证明输入。

## Notation

形式低块 $P(H,b,L,x)$ 在模 $x^p$ 的正次数上满足

$$
\mathcal DP=-\frac{bx}{2}e^P-Lx^2e^{2P},\qquad
\mathcal D x^i=d_i(H)x^i,\quad 1\le i<p.
$$

$d_i(H)$ 为真实 Chebyshev 传播子，$d_i(0)=-i^2$。
下文在取 $H=0,b=1$ 后写

$$
U=P(0),\quad \mathcal N=x\partial_x,\quad
\mathcal T=b\partial_b+L\partial_L,\quad
f=\mathcal TU,\quad g=\mathcal T^2U,
$$
$$
F=\mathcal N^2U,\quad J=\frac x2e^U+2Lx^2e^{2U},\quad
K=\frac x4e^U+2Lx^2e^{2U},\quad
\mathscr L=-\mathcal N^2+J.
\tag{3}
$$

参数导数在取 $b=1$ 前作用；不将该辅助幅度当成实际参数的改变。
由低块方程及参数导数，得到

$$
\mathscr Lf=-F,\qquad
\mathscr Lg=-F-2Jf-2Kf^2,\qquad
\mathcal N^2f=Jf+F.
\tag{4}
$$

所有单位响应均取零常数，正次数范围为 $1,\ldots,p-1$。
对正次数有限级数定义

$$
\langle u,v\rangle_j=\sum_{i=1}^{p-1}i^j u_i v_{p-i}.
\tag{5}
$$

偶权矩对称，奇权矩反对称。以下 $[x^p]$ 只用于至少含两个正次数因子的乘积，
或明确给出的有理级数；不对可能有 $p$ 分母的 $[x^p]U$ 本身取模。

## Proof Strategy and Dependency Map

1. 保留第一端点项的准确配对，在其余三项中提取四次移位系数。
2. 用同一单位耦合方程求四次系数所需响应的方程，而不直接求响应本身。
3. 两次偶导数配对消去新响应，留下一个可直接求值的奇权矩。
4. 以有理低块及二次分母的 Frobenius 身份求该矩，再用有限几何和去掉表面分母。
5. 核对所有有限边界和误差，区分形式组成量与实际总层。

## Proof

### Step 1. 四次系数的合法提取

沿用接受的 $\Delta_k=\mathcal D_k-\mathcal D$，其有限移位展开为

$$
\Delta_k=k r\mathsf S+k^2r^2\mathsf T+k^3r^3\mathsf U+O(H^{4m+1}).
$$

在独立移位变量 $\nu$ 下，$H=0$ 时
$\mathsf S=\mathcal N,\mathsf T=-I/4,\mathsf U=0$，所以

$$
\Delta_k=k\nu\mathcal N-k^2\nu^2/4.
\tag{6}
$$

有限正次数上的对角元 $-i^2$ 均为单位。
将 $\nu=r(H)$ 代回后，单位模型比较的余项仍在 $H^{4m+1}$。
准确配对使端点第一项等于

$$
\frac{3r^3H}{8(H-4)}\sum_{i=1}^{p-1}i^3\mathsf S_i P_iP_{p-i}
+O(H^{4m+1}).
\tag{7}
$$

这一项纳入 $r^3\mathcal F_3$，在四次移位的 $H^0$ 系数中无贡献。
不能把未经配对的独立 $\nu$ 多项式用来替换式 (7)。
其他三项在 $H=0$ 所需缺陷为

$$
C_i^*=\frac32\nu^2,\qquad
\delta_i^{\rm low}=3i\nu+\frac94\nu^2,\qquad
\delta_i^{\rm mid}=3i\nu+\frac34\nu^2.
\tag{8}
$$

它们直接由式 (6) 在 $i,-i$ 处作差得到。
写

$$
y=\nu t+\nu^2a+O(\nu^3),\qquad
Q=\nu^2q+\nu^3b+O(\nu^4).
\tag{9}
$$

将式 (8)、(9) 代入已接受的端点后三项
$\sum i^2C_i^*U_i y_{p-i}$、
$2\sum i\delta_i^{\rm low}U_iQ_{p-i}$、
$\sum i\delta_i^{\rm mid}y_i y_{p-i}$，取 $\nu^4$ 得

$$
E_4=\frac32\langle U,a\rangle_2+6\langle U,b\rangle_2
+\frac92\langle U,q\rangle_1+6\langle t,a\rangle_2.
\tag{10}
$$

其中 $\langle t,t\rangle_1=0$；两个混合二次矩因偶权对称而合并。
五次移位及四次移位的一次 $H$ 修正分别至少在 $H^{5m}$、$H^{4m+1}$。
因 $m\ge2$，$5m\ge4m+1$，故式 (1) 的精度成立。

### Step 2. 新响应的准确驱动

接受的耦合方程是

$$
(\mathcal D_1+J)y=\tfrac12\Delta_1\mathcal NP,
$$
$$
(\mathcal D_2+J)Q
=(2\Delta_1-\Delta_2)\frac{\mathcal N^2P}{8}
+\frac12(\Delta_2-\Delta_1)\mathcal Ny-Ky^2.
\tag{11}
$$

把式 (6)、(9) 代入式 (11) 的一至三次 $\nu$ 系数，依次得到

$$
t=-f/2,\qquad q=g/8+f/16,
\tag{12}
$$
$$
\mathscr La=-\frac18\mathcal NU+\frac12\mathcal Nf,
\tag{13}
$$
$$
\mathscr Lb=\frac12\mathcal N^2a+\frac1{16}\mathcal Nf
+Kfa-\frac14\mathcal Ng.
\tag{14}
$$

例如 $2\Delta_1-\Delta_2=\nu^2/2$，
$\Delta_2-\Delta_1=\nu\mathcal N-3\nu^2/4$。
三次 $\nu$ 项先给
$\mathscr Lb=\mathcal N^2a/2-3\mathcal Nt/8-2Kta-2\mathcal Nq$，
再代入式 (12) 就是式 (14)。
式 (12) 则由式 (4) 直接代入二次驱动和有限单位解唯一性验证。
本步没有除以 $p$ 或求解第 $p$ 个模态。

### Step 3. 消去两个新响应

对正次数因子 $u,v$，$[x^p]\mathcal N(uv)=0$，且
$[x^p]u\mathcal N^2v=[x^p](\mathcal N^2u)v$。
乘法算子 $J$ 亦对称，所以 $\mathscr L$ 在此有限配对中自伴。
由式 (4)、(14)，$[x^p]Fb=-[x^p]f\mathscr Lb$。
将它与式 (12) 一起代入式 (10)，得到

$$
\begin{aligned}
E_4=[x^p]\{& (3F/2-6\mathcal N^2f-6Kf^2)a
-3f\mathcal Nf/8+3f\mathcal Ng/2\\
&+9(\mathcal NU)g/16+9(\mathcal NU)f/32\}.
\end{aligned}
\tag{15}
$$

式 (4) 进一步给出准确消元身份

$$
3F/2-6\mathcal N^2f-6Kf^2=\mathscr L(3g+3f/2).
\tag{16}
$$

将式 (16) 与式 (13) 配对，剩余导数交叉项为
$3\mathcal N(fg)/2+3\mathcal N(f^2)/16$，其第 $p$ 项为零。
其余项恰为

$$
\boxed{E_4=\frac3{16}\langle U,g\rangle_1
+\frac3{32}\langle U,f\rangle_1.}
\tag{17}
$$

每次配对的两因子均零常数；乘法驱动含第三个正次数因子时更不涉及模态 $p$。
因此这里只使用次数严格小于 $p$ 的整响应，没有遗漏对数的第 $p$ 阶边界。

### Step 4. 一个奇权矩的全参数求值

记 $J_1(L)=\langle U,f\rangle_1$。
辅助幅度的总 $x^p$ 权重给出 $\mathcal T=-L\partial_L$ 在这些矩上的作用。
又 $\langle f,f\rangle_1=0$，因此

$$
\langle U,g\rangle_1=-L\partial_LJ_1,\qquad
E_4=\frac3{16}(-L\partial_L+1/2)J_1.
\tag{18}
$$

低块的已接受有理表示为

$$
\theta=(1-4L)/16,\quad A=1-x/2+\theta x^2,\quad
U=-\log A,\quad v=x/A,\quad G=1+\mathcal NU.
$$

这里只取 $U$ 的次数小于 $p$ 的系数及其无对数导数。
幅度权重和直接参数微分给
$f=\mathcal NU-L\partial_LU$、$\partial_LU=xv/4$，并有 $\mathcal Nv=Gv$。
使用接受的 $A_0=\langle U,U\rangle_2=1-L^m/2$ 以及
$[x^p](\mathcal NU)^2=-A_0$，得到

$$
J_1=-A_0-\frac L4[x^p]xv(G-1)
=-A_0+\frac L2[x^p]xv.
\tag{19}
$$

第二步使用 $\mathcal N(xv)=xv+xGv$，故 $[x^p]xGv=-[x^p]xv$。
这两个有理级数的分母只含 $2$ 及常数项为一的 $A$，可以直接约化。

以独立 $a_0$ 写 $A_{a_0}=1-a_0x+\theta x^2$、$\Delta=a_0^2-4\theta$。
在 $\mathbb F_p(a_0,\theta)$ 中，二次分母的系数满足

$$
[x^{p-2}]A_{a_0}^{-1}=
\frac{a_0\Delta^m-a_0^p}{2\theta}.
\tag{20}
$$

证明：在二次分裂域写 $A_{a_0}=(1-r_1x)(1-r_2x)$。
已有 $[x^{p-1}]A_{a_0}^{-1}=(r_1^p-r_2^p)/(r_1-r_2)=\Delta^m$。
直接展开还给
$a_0\Delta^m-(r_1^p+r_2^p)
=2r_1r_2(r_1^{p-1}-r_2^{p-1})/(r_1-r_2)$；
用 $r_1^p+r_2^p=a_0^p$、$r_1r_2=\theta$ 即得式 (20)。
在局部化中证明后，交叉相乘是多项式身份，所以不排除重根或 $\theta=0$ 参数。

令 $a_0=1/2,\theta=(1-4L)/16$，式 (20) 给

$$
[x^p]xv=\frac{4(L^m-1)}{1-4L},\qquad
J_1=\frac{L^m/2+2L-1}{1-4L}.
\tag{21}
$$

式 (21) 先在 $\mathbb F_p(L)$ 中计算；原矩本身是参数多项式。
因 $4^m=2^{p-1}=1$ 于 $\mathbb F_p$，令 $z_0=4L$ 后直接约分，得到

$$
\boxed{J_1=-1-\frac12\sum_{k=1}^{m-1}(4L)^k.}
\tag{22}
$$

这是完整多项式身份，包含 $L=0$ 和 $4L=1$，没有参数排除。
式 (22) 代入式 (18) 即为所求式 (2)。
最高项的系数为
$3(2m-3)4^{m-1}/64=-3/64\ne0$，故次数恰为 $m-1$。证毕。

## Corrections or Missing Assumptions

没有增加素数、指数或参数排除。所有数值分母仅含 $2$，
有限对数移位和模型只调用已接受的 $p\ge5$ 单位条件。
公式的推导不使用未定义的第 $p$ 个低模态，也不将实际内部模态设为零。

## Open Risks and Scope

式 (1) 是形式组成量分解，不是所有 $p$ 的实际 $H^{4m}$ 总系数。
三次响应的更高 $H$ 层可能与它同阶，不能略去；例如七的幂边界须另算
$[H^3]\mathcal F_3(H,0)$，再与式 (2) 的常数合并。
一般正根簇的完整 Newton 结构、负根簇、完整周期多项式及全实性均不由本件完成。
没有根、素数或参数扫描，没有作者代码运行被计作独审，没有估页、Route、PDF或对外操作。
本件冻结后交真正非作者审查；旧接受稿及失败记录全部保留。
