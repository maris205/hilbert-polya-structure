# Paper30：一般第三 forcing 的完整第二正规化层

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`；
主控共同推导 $B_1,C_0$ 的有理系数提取与层的合并，
`p30_third_forcing_general_independent` 参与有限移位和实际误差的作者核算。
这些作者交叉核算均不算本件的非作者独审。
本轮完整读取 `proof-writer`、WORKFLOW 和当前 BATCH 首段，按新输入推进；
已接受的旧首层、五的幂边界和根簇分离不重审、不修改。

## Claim

令 $p\ge7$ 为任意素数、$a\ge2$、$\zeta$ 为任意本原 $p^a$ 次根。
保持同一双谐波模型、固定参数、物理正 kick 与 SUM action，取

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1}.
\tag{1}
$$

在 $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$ 中使用
$v_h(h)=1$、$v_h(p)=M$。实际分支保持

$$
d_nV_n=-\tfrac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad
d_n=-\frac{2-\zeta^n-\zeta^{-n}}h.
$$

由全部 $n<3p$ 实际模态定义

$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},\qquad
S=h^{-(3m+1)}p^2\mathcal B_3\in\mathcal O^+[L].
\tag{2}
$$

则完整参数多项式满足

$$
\boxed{S=-\frac{3\chi}{64}L^m
+h\frac{\chi}{8192}(684L-41)L^{m-1}+O(h^2).}
\tag{3}
$$

$O(h^2)$ 表示 $h^2\mathcal O^+[L]$ 中的逐系数误差；
式 (3) 对全部 $p\ge7,a\ge2$ 成立，包含 $p=7$。
当 $p=41$ 时，下一层的 $L^{m-1}$ 系数自身约化为零；
本件不由此声称更深准确赋值、特殊根展开或简单性。

证明还给出下述全参数有限矩身份。令 $P(H,x)$ 为已接受的形式低块，
$U=P(0,x)$，并定义

$$
\langle f,g\rangle_k=\sum_{i=1}^{p-1}i^kf_i g_{p-i},\qquad
A(H)=\langle P,P\rangle_2=A_0+HA_1+H^2A_2+O(H^3),
$$
$$
B(H)=\langle P,P\rangle_4=B_0+HB_1+O(H^2),\qquad
C_0=\langle U,U\rangle_6.
\tag{4}
$$

在 $\mathbb F_p[L]$ 中有

$$
\boxed{A_2=-\frac{1488L^2-1992L+373}{294912}L^{m-2},}
\tag{5}
$$
$$
\boxed{B_1=-\frac{816L^2-504L+67}{6144}L^{m-2},\qquad
C_0=-\frac{(4L-1)(8L-3)}{64}L^{m-2}.}
\tag{6}
$$

这些指数均非负，分母均为 $p$-单位。本件闭合下一正规化层，
不以式 (3) 代替全部正根 Newton 边、根簇分裂或简单性证明。

## Status

式 (3)、(5)、(6)：`PROVABLE AS STATED`，作者证明完成，待本轮非作者核查。
此前未求值的 $A_2$ 在本件由两个明确有理恒等式消去积分并求值；
所需响应和四项端点也完整保留至二次 $H$，没有只补入单个矩。

## Assumptions and Exact Inputs

| 已接受输入 | 调用范围 | SHA256 |
| --- | --- | --- |
| [一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，843 行 | 实际模 $h^M$ 端点、准确配对、有限移位、低块 $U,w$ 与旧 $A_0,A_1,B_0,E_1$ | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| [第二阶乘带响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，640 行 | 完整形式耦合模型及实际块 $h^{M-m}$ 比较误差 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |

调用上述接受事实，不重开其证明或重跑旧证书。本轮新增的
精确 $\mathcal R$ 响应、二阶配对表达式及三个新矩均在下文另行证明。
五的幂下一层不是本件输入，也不用于一般素数的外推。

## Notation

令 $\mathcal N=x\partial_x$。Chebyshev 辅助多项式为

$$
C_0(H)=2,\quad C_1(H)=2-H,\quad
C_{n+1}(H)=(2-H)C_n(H)-C_{n-1}(H),\quad
d_n(H)=\frac{C_n(H)-2}{H}.
$$

此处 $C_n(H)$ 不是式 (4) 的有限矩 $C_0$，两者由自变量和上下文区分。
低块 $P=\sum_{i=1}^{p-1}P_i(H,b,L)x^i$ 只取正次数，使用辅助幅度 $b$；
实际参数仍取 $b=1$。在模 $x^p$ 下令

$$
\mathcal D x^i=d_i(H)x^i,\quad
J=\frac{bx}2e^P+2Lx^2e^{2P},\quad
K=\frac{bx}4e^P+2Lx^2e^{2P},\quad \mathscr L=\mathcal D+J.
\tag{7}
$$

正次数 $i<p$ 的对角元在 $H=0$ 为 $-i^2$，所以单位三角方程唯一可解。
定义参数与 $H$ 微分算子

$$
\mathcal T=b\partial_b+L\partial_L,\qquad
\mathcal H=H\partial_H,\qquad \mathcal R=\mathcal T-\mathcal H.
\tag{8}
$$

没有将实际阶乘桥扩张到任意 $b$；该幅度只用于低块与其参数导数。
未注明处最终取 $b=1$。形式端点的计算先在 $\mathbb F_p[L][[H]]$ 中进行；
实际误差在最后以 $v_h$ 单独核定。

## Proof Strategy and Dependency Map

1. 从准确 Chebyshev 微分身份推导全 $H$ 的单位响应，再还原完整三次移位端点。
2. 用全部传播子、低块与响应的二阶项写出 $E_2$，不丢弃旧稿目标层中的配对修正。
3. 用有限 $x^p$ 偶次导数配对消去未知二阶低块解，把 $A_2$ 化为仅含 $U,w$ 的身份。
4. 以两个有理证书消去积分平方和积分，逐项检查没有 $p[x^p]w$ 型边界遗漏。
5. 用 Frobenius 二次分母系数求值，得到三个矩并合并所有幂。
6. 保留 $r^3$ 自身修正并检查 $p=7$ 的 $r^4$ 余项；最后由原桥回到实际 $S$。

## Proof

### Step 1. 全 $H$ 的精确单位响应

沿用接受的有限移位参数 $r(H)$ 以及算子

$$
\mathsf S_i=\frac{z^i-z^{-i}}{z-z^{-1}},\qquad
\mathsf T_i=\frac{2+Hd_i(H)}{2(H-4)},\qquad H=2-z-z^{-1}.
$$

独立移位 $\nu$ 的响应 $y=\nu t+O(\nu^2)$、$Q=\nu^2q+O(\nu^3)$ 满足接受的

$$
\mathscr Lt=\tfrac12\mathsf S\mathcal NP,\qquad
\mathscr Lq=-\tfrac14\mathsf T\mathcal N^2P
+\tfrac12\mathsf S\mathcal Nt-Kt^2.
\tag{9}
$$

我们在本轮证明精确身份

$$
\boxed{t=-\tfrac12\mathcal RP,\qquad
q=\tfrac18\mathcal R^2P-\frac{\mathcal RP}{4(H-4)}.}
\tag{10}
$$

对 Chebyshev 多项式求导给 $C_i'=-i\mathsf S_i$，因此

$$
\mathsf S\mathcal N=-\mathcal D-H\mathcal D'.
\tag{11}
$$

该身份也可由 Chebyshev 递推和其导数逐项验证，初值 $i=0,1$ 一致。
记 $f=\mathcal TP$、$g=\mathcal T^2P$、$u=H\partial_HP$。
低块方程及其导数给

$$
\mathscr Lf=\mathcal DP,\qquad
\mathscr Lg=(\mathcal D-J)f-2Kf^2,\qquad
\mathscr Lu=-H\mathcal D'P.
\tag{12}
$$

由式 (11)、(12)，$(u-f)/2$ 满足 $t$ 方程，唯一性给出第一式。
再有

$$
\mathscr L(\mathcal Tu)=-H\mathcal D'f-Ju-2Kfu,
$$
$$
\mathscr L(H^2\partial_H^2P)
=-H^2\mathcal D''P-2H\mathcal D'u-2Ku^2.
\tag{13}
$$

这里 $\partial_PJ=2K$；式 (13) 分别由 $\mathcal T$、二次 $H$ 求导得到。
Chebyshev 微分方程
$H(4-H)C_i''+(2-H)C_i'+i^2C_i=0$ 给出

$$
(2+H\mathcal D)\mathcal N^2
=-H^2(4-H)\mathcal D''-H(10-3H)\mathcal D'-(2-H)\mathcal D.
\tag{14}
$$

把 $t=(u-f)/2$ 代入式 (9)，再用式 (12)—(14)，其 $q$ 方程的右侧恰为

$$
\mathscr L\left(
\frac g8-\frac{\mathcal Tu}4+\frac{H^2\partial_H^2P}8
-\frac f{4(H-4)}+\frac{H-2}{8(H-4)}u\right).
$$

括号等于式 (10) 的第二式，因为
$\mathcal H^2P=u+H^2\partial_H^2P$，且 $\mathcal H,\mathcal T$ 交换。
单位三角唯一性完成式 (10) 的证明；所有新增除数在 $H=0$ 都是单位。

### Step 2. 完整二阶端点算子

回到接受的四项端点。第一项先使用准确 $i\leftrightarrow p-i$ 配对，
不能丢弃旧稿低精度表达式的 $O(H^{3m+2})$ 部分。
完整三次移位系数为

$$
\begin{aligned}
\mathcal F_3(H)={}&\frac{3H}{8(H-4)}\sum_i i^3\mathsf S_iP_iP_{p-i}
-6\sum_i i^2\mathsf T_iP_it_{p-i}\\
&+6\sum_i i\mathsf S_iP_iq_{p-i}
+3\sum_i i\mathsf S_it_it_{p-i}.
\end{aligned}
\tag{15}
$$

接受的准确配对余项是 $O(H^{4m+1})$，其他四次及更高移位贡献为 $O(H^{4m})$。
所以在本轮所需范围内

$$
\mathcal E=r^3\mathcal F_3(H)+O(H^{4m}),\qquad
\mathcal F_3=E_0+HE_1+H^2E_2+O(H^3).
\tag{16}
$$

对 $p\ge7$，真实 Chebyshev 递推给出合法展开

$$
\mathsf S_i=i-\frac H6(i^3-i)+\frac{H^2}{120}(i^5-5i^3+4i)+O(H^3),
$$
$$
\mathsf T_i=-\frac14+\frac H{16}(2i^2-1)
+\frac{H^2}{192}(-2i^4+8i^2-3)+O(H^3).
\tag{17}
$$

所有分母仅含 $2,3,5$，包括 $p=7$ 时均为单位。
至二次 $H$ 的偶次权重在 $i\leftrightarrow p-i$ 下对称。
低块幅度权重使总 $x^p$ 矩上的 $\mathcal T$ 作用等于
$\mathfrak d=-L\partial_L$，这是已接受的全参数权重身份。

为明确保留全部乘积与权重导数，设
$\Omega_i=i\mathsf S_i$、$\Psi_i=i^2\mathsf T_i$，
$\mathcal M[a]=\sum_i a_iP_iP_{p-i}$。
令 $\delta a=H\partial_Ha$ 只作用权重，
$\mathfrak R=\mathfrak d-H\partial_H$ 作用整个矩。
对称性和乘积法则给

$$
\sum_i a_iP_i(\mathcal RP)_{p-i}
=\tfrac12\{\mathfrak R\mathcal M[a]+\mathcal M[\delta a]\},
$$
$$
\sum_i a_i\{P_i(\mathcal R^2P)_{p-i}+(\mathcal RP)_i(\mathcal RP)_{p-i}\}
=\tfrac12\{\mathfrak R^2\mathcal M[a]
+2\mathfrak R\mathcal M[\delta a]+\mathcal M[\delta^2a]\}.
\tag{18}
$$

这些等式用于本段均模 $H^3$。将式 (10) 代入式 (15)，得到

$$
\begin{aligned}
\mathcal F_3={}&\frac{3H}{8(H-4)}\mathcal M[i^2\Omega]
+\frac32\{\mathfrak R\mathcal M[\Psi]+\mathcal M[\delta\Psi]\}\\
&+\frac38\{\mathfrak R^2\mathcal M[\Omega]
+2\mathfrak R\mathcal M[\delta\Omega]+\mathcal M[\delta^2\Omega]\}\\
&-\frac3{4(H-4)}\{\mathfrak R\mathcal M[\Omega]+\mathcal M[\delta\Omega]\}
\pmod{H^3}.
\end{aligned}
\tag{19}
$$

式 (17) 具体给出

$$
\mathcal M[\Omega]=A-\frac H6(B-A)+\frac{H^2}{120}(C_0-5B_0+4A_0)+O(H^3),
$$
$$
\mathcal M[\Psi]=-\frac A4+\frac H{16}(2B-A)
+\frac{H^2}{192}(-2C_0+8B_0-3A_0)+O(H^3).
\tag{20}
$$

取式 (19) 的 $H^2$ 系数，全部六个矩的算子如下：

| 矩 | 在 $E_2$ 中的算子 |
| --- | --- |
| $A_0$ | $\mathfrak d(16\mathfrak d+3)/1280$ |
| $A_1$ | $(\mathfrak d-1)(4\mathfrak d-5)/64$ |
| $A_2$ | $3(\mathfrak d-2)(2\mathfrak d-5)/16$ |
| $B_0$ | $-(2\mathfrak d^2-6\mathfrak d+5)/128$ |
| $B_1$ | $-(\mathfrak d-2)(2\mathfrak d-5)/32$ |
| $C_0$ | $(\mathfrak d-2)(2\mathfrak d-5)/640$ |

等价地，精确组合为

$$
\begin{aligned}
E_2={}&(\mathfrak d-2)(2\mathfrak d-5)
\left(\frac{3A_2}{16}-\frac{B_1}{32}+\frac{C_0}{640}\right)\\
&+\frac{(\mathfrak d-1)(4\mathfrak d-5)}{64}A_1
+\frac{\mathfrak d(16\mathfrak d+3)}{1280}A_0
-\frac{2\mathfrak d^2-6\mathfrak d+5}{128}B_0.
\end{aligned}
\tag{21}
$$

这一步未预设任何矩的参数支撑；所有 $H$ 导数、交叉项和第一项配对均在式 (19) 中保留。

### Step 3. $A_2$ 中的未知二阶低块解可以消去

以下先沿用接受的完整特征零表达式

$$
\theta=(1-4L)/16,\quad A_x=1-x/2+\theta x^2,\quad U=-\log A_x,
\quad v=x/A_x,\quad G=1+\mathcal NU=(1-\theta x^2)/A_x,
$$
$$
F=v/2+Lv^2,\quad J_0=v/2+2Lv^2,\quad K_0=v/4+2Lv^2,
\quad G^2=1+v+Lv^2.
\tag{22}
$$

$A_x$ 不同于矩函数 $A(H)$。有
$\mathcal Nv=Gv$、$\mathcal NG=F$、$\mathcal NF=J_0G$。
令 $I=\int_0^x A_t^{-1}\,dt$；接受的一次响应为

$$
w=W-GI/48,\qquad
W=\frac{G^2-G}{8}-\frac v{24}+\frac{xv}{192}.
\tag{23}
$$

这与接受稿的有理加积分表达式相同；所用系数低于 $p$ 时均整。
令

$$
\mathscr A=(\mathcal N^4-\mathcal N^2)/12,\qquad
\mathscr B=-(\mathcal N^6-5\mathcal N^4+4\mathcal N^2)/360,
\quad f=\mathcal TU|_{b=1}=G-1-Lxv/4.
\tag{24}
$$

写有限低块 $P=U+Hw+H^2\xi+O(H^3)$。
Chebyshev 的二阶展开和低块方程给

$$
\mathscr L_0\xi=-K_0w^2-\mathscr Aw-\mathscr BU,
\quad \mathscr L_0=-\mathcal N^2+J_0,
\quad \mathscr L_0f=-F,
\quad \mathcal N^2w=J_0w+\mathscr AU.
\tag{25}
$$

所有式 (25) 仅需次数严格小于 $p$ 的单位解；未定义或使用第 $p$ 阶的 $\xi$。
在有限正次数配对 $[x^p]ab$ 中，偶次 $\mathcal N$ 自伴，
因为 $(p-i)^{2k}=i^{2k}$ 于 $\mathbb F_p$。
乘法算子 $J_0$ 也自伴。于是

$$
\langle U,\xi\rangle_2=[x^p]F\xi
=[x^p]f(K_0w^2+\mathscr Aw+\mathscr BU),
$$
$$
\langle w,w\rangle_2=[x^p]w(J_0w+\mathscr AU).
$$

由于 $A_2=2\langle U,\xi\rangle_2+\langle w,w\rangle_2$，得到精确有限身份

$$
\boxed{A_2=[x^p]\{(J_0+2K_0f)w^2
+w\mathscr A(2f+U)+2f\mathscr BU\}.}
\tag{26}
$$

该式消去了未知 $\xi$。每个乘积都有正次数伴随因子，
所以只调用 $U,w,f$ 的 $<p$ 系数，不会引入它们的第 $p$ 阶分母。

### Step 4. 两个可逐系数验证的有理证书

本段先在 $\mathbb Q(L)$ 中计算，记 $\omega=4L-1$。
用 $xv=4(v-2G+2)/(1-4L)$，可把全部对象写在

$$
\mathbb Q(L)[v,G]/(G^2-1-v-Lv^2)
$$

中。特别地

$$
f=\frac{(1-2L)(G-1)-Lv}{1-4L},\qquad
W=\frac{G^2-G}{8}-\frac v{24}+\frac{v-2G+2}{48(1-4L)}.
\tag{27}
$$

定义以下明确有理函数，其中 $U$ 只出现在正次数导数内：

$$
M_1=J_0+2K_0f,\quad N_1=\mathscr A(2f+U),\quad
H_c=G\mathcal N^2f-F\mathcal Nf,
$$
$$
R_a=M_1W^2+N_1W+2f\mathscr BU,
\qquad B_a=-\frac{M_1WG}{24}-\frac{N_1G}{48}-\frac{vH_c}{1152}.
\tag{28}
$$

从 $\mathcal N^2f=J_0f+F$、$\mathcal NJ_0=2K_0G$ 直接求导，得到

$$
\mathcal NH_c=M_1G^2.
\tag{29}
$$

以下证书将本段所有消元化为有理多项式恒等式。令

$$
g_1=\sum_{k=0}^5a_kv^k+G\sum_{k=0}^4b_kv^k.
$$

未列系数为零；其系数表为

| $k$ | $a_k$ | $b_k$ |
| --- | --- | --- |
| 0 | $0$ | $0$ |
| 1 | $-(3L-1)/(288\omega^2)$ | $(3L-1)/(288\omega^2)$ |
| 2 | $(192L^3-576L^2+136L+5)/(4608\omega^2)$ | $-(12L-7)(32L^2-6L-1)/(2304\omega^2)$ |
| 3 | $-L(256L^2+92L-45)/(2304\omega^2)$ | $-L(184L^2-150L+27)/(1152\omega^2)$ |
| 4 | $-L^2(42L-11)/(288\omega^2)$ | $-L^2(2L-1)/(48\omega)$ |
| 5 | $-L^3/(48\omega)$ | $0$ |

再记

$$
\Lambda=466944L^4-602944L^3+304592L^2-67180L+5595,
$$
$$
g_2=\sum_{k=0}^6a'_kv^k+G\sum_{k=0}^5b'_kv^k,
\qquad
\kappa=-\frac{1488L^2-1992L+373}{294912L^2}.
\tag{30}
$$

其系数表为

| $k$ | $a'_k$ | $b'_k$ |
| --- | --- | --- |
| 0 | $-\Lambda/(2211840L^2\omega^2)$ | $\Lambda/(2211840L^2\omega^2)$ |
| 1 | $-(3L-1)^2/(36\omega^3)$ | $-(109824L^4-250240L^3+124608L^2-11688L-1865)/(1105920L\omega^3)$ |
| 2 | $(3L-1)(576L^3-752L^2+100L+19)/(576\omega^3)$ | $-(946176L^4-1559872L^3+648432L^2-68316L-3251)/(276480\omega^3)$ |
| 3 | $(384L^4-14592L^3+8624L^2-1190L-21)/(4608\omega^3)$ | $L(107584L^3-7280L^2-25892L+5327)/(46080\omega^3)$ |
| 4 | $L(864L^4-3224L^3+1672L^2-204L-7)/(576\omega^3)$ | $L^2(1536L^2+524L-467)/(5760\omega^2)$ |
| 5 | $-L^2(1512L^2-654L+29)/(1920\omega^2)$ | $-5L^3/(288\omega)$ |
| 6 | $-5L^3(2L-1)/(288\omega)$ | $0$ |

两张表满足

$$
\boxed{\mathcal Ng_1=B_a,\qquad
\mathcal Ng_2=R_a-vg_1-\kappa v,\qquad g_1(0)=g_2(0)=0.}
\tag{31}
$$

为明确证书如何直接核定，而非以黑箱积分代替证明，所需规则只有

$$
\mathcal N(v^k)=kGv^k,
$$
$$
\mathcal N(Gv^k)=kv^k+(k+\tfrac12)v^{k+1}+(k+1)Lv^{k+2},
\qquad \mathcal NU=G-1.
\tag{32}
$$

式 (32) 来自式 (22) 的乘积求导。
按式 (32) 展开式 (28) 的右侧并约化 $G^2$，分别比较 $v^k,Gv^k$ 的系数，
第一张表给 $\mathcal Ng_1-B_a=0$，第二张表给
$\mathcal Ng_2-R_a+vg_1+\kappa v=0$；每项仅为表中给定的有理数与 $L$ 多项式运算。
常数值使用 $v(0)=0,G(0)=1$，由 $a_0+b_0=a'_0+b'_0=0$ 得到。
这提供全部中间函数与逐系数验证规则，不需要选择素数或参数点。

所有表项的数值分母仅含 $2,3,5$。
因此这两个特征零身份可在每个 $p\ge7$ 的
$\mathbb F_p[L,L^{-1},\omega^{-1}]$ 中约化；$p=7$ 没有新增非单位除法。

### Step 5. 积分边界与 $A_2$ 的准确值

将式 (23) 代入式 (26)，得

$$
A_2=[x^p]\left\{R_a
+I\left(-\frac{M_1WG}{24}-\frac{N_1G}{48}\right)
+\frac{I^2M_1G^2}{2304}\right\}.
\tag{33}
$$

右侧用特征零的有理加积分表达式提取系数；式 (33) 及本段以下系数等式
均在所需系数证明 $p$-整后约化至 $\mathbb F_p$ 解释，
不把有限偶次配对的模 $p$ 身份误称为特征零的 $A_2$ 身份。
由式 (29) 和 $\mathcal NI=v$，在第 $p$ 阶分部积分有

$$
[x^p]I^2\mathcal NH_c=-2[x^p]IvH_c.
\tag{34}
$$

式 (34) 模 $p$ 合法的原因是 $H_c(0)=0$、$I(0)=0$：
$[x^p]H_cI^2$ 涉及的每个积分下标都严格小于 $p$，故其系数 $p$-整。
所以 $[x^p]\mathcal N(H_cI^2)=p[x^p]H_cI^2$ 的约化为零。
未把可能含 $p$ 分母的 $[x^p]I$ 先行置零。

式 (33)、(34) 及第一个证书于是给

$$
A_2=[x^p](R_a+IB_a)
=[x^p](R_a+I\mathcal Ng_1)
=[x^p](R_a-vg_1).
\tag{35}
$$

最后一个分部积分也合法：$g_1(0)=0$，所以
$[x^p]Ig_1$ 不涉及 $[x^p]I$；其系数在局部化系数环中 $p$-整。
再由第二个证书，$g_2$ 是数值分母均为 $p$-单位的纯有理函数，
在 $x=0$ 展开不产生新的整数分母。因此

$$
A_2=[x^p](\mathcal Ng_2+\kappa v)
=\kappa[x^p]v.
\tag{36}
$$

这里 $[x^p]\mathcal Ng_2=p[x^p]g_2$ 的约化为零，不依赖 $g_2$ 的第 $p$ 项消失。
接受的 Frobenius 二次分母身份给

$$
[x^p]v=[x^{p-1}]A_x^{-1}=L^m.
$$

故式 (36) 正是式 (5)。它的两侧都是 $\mathbb F_p[L]$ 中的多项式，
右侧只含非负幂 $L^m,L^{m-1},L^{m-2}$。
先在 $\mathbb F_p[L,L^{-1},(4L-1)^{-1}]$ 证明后，利用多项式环到此局部化的单射，
身份延伸到全部参数，包括 $L=0$、$4L=1$；没有参数排除。

### Step 6. $B_1,C_0$ 的自由有理系数提取

因为 $B_1=2\langle U,w\rangle_4=2[x^p]F\mathcal N^2w$，式 (25) 给

$$
B_1=[x^p]\left\{2FJ_0W+\frac{F^2v}{48}
+\frac{F(\mathcal N^2F-F)}6\right\}.
\tag{37}
$$

这里积分项使用 $\mathcal N(F^2)=2FJ_0G$，因此
$[x^p]FJ_0GI=-[x^p]F^2v/2$。
$F^2$ 的阶至少为二，故 $[x^p]F^2I$ 只用积分的 $<p$ 系数，分部积分合法。
另外 $[x^p]FJ_0G=[x^p]\mathcal N(F^2)/2=0$，所有系数均整。

利用式 (23) 及
$\mathcal N^2F=(v/2+4Lv^2)G^2+J_0F$，式 (37) 化为

$$
B_1=[x^p]\{P_B(v)+xP_X(v)\},
$$
$$
\begin{aligned}
P_B(v)={}&\tfrac32L^3v^6+\tfrac{107}{48}L^2v^5
+L^2v^4+\tfrac{23}{24}Lv^4+\tfrac58Lv^3
+\tfrac7{64}v^3+\tfrac1{16}v^2,\\
P_X(v)={}&L^2v^5/48+Lv^4/64+v^3/384.
\end{aligned}
\tag{38}
$$

而偶次配对、$\mathcal N^3U=J_0G$ 给

$$
C_0=-[x^p](\mathcal N^3U)^2=-[x^p]J_0^2G^2.
\tag{39}
$$

令 $A_{a_0}=1-a_0x+\theta x^2$、$\Delta=a_0^2-4\theta$。
接受的全参数身份 $[x^{p-1}]A_{a_0}^{-1}=\Delta^m$ 经参数导数给

$$
c_k=[x^p]v^k
=\left.\frac{\partial_{a_0}^{k-1}\Delta^m}{(k-1)!}
\right|_{a_0=1/2,\theta=(1-4L)/16},\qquad 1\le k\le6.
\tag{40}
$$

所用最大阶乘为 $5!$，在全部 $p\ge7$ 时可逆。
在 $\mathbb F_p(L)$ 中把 $c_k$ 除以 $L^m$，可写成

$$
\begin{array}{c|c}
k&c_k/L^m\\ \hline
1&1\\
2&-1/(2L)\\
3&-(4L-3)/(8L^2)\\
4&(12L-5)/(16L^3)\\
5&(48L^2-120L+35)/(128L^4)\\
6&-(240L^2-280L+63)/(256L^5)
\end{array}
\tag{41}
$$

这些表达式是先取式 (40) 的多项式导数、再用 $2m=-1$ 合并所得。
又 $\partial_\theta v^{k-1}=-(k-1)xv^k$，而固定 $a_0=1/2$ 后
$\partial_\theta=-4\partial_L$，所以

$$
d_k=[x^p]xv^k=\frac4{k-1}\partial_Lc_{k-1}.
$$

对式 (38) 只需

$$
d_3=\tfrac32L^{m-2},\qquad
d_4=\tfrac14(4L-5)L^{m-3},\qquad
d_5=-\tfrac5{32}(12L-7)L^{m-4}.
\tag{42}
$$

式 (42) 暂在 $\mathbb F_p(L)$ 中解释；例如 $p=7$ 时中间负幂会与分子约分，
不把 $0\cdot L^{-1}$ 当作在零参数处的计算。
代入式 (38)、(39)，所有项合并为

$$
B_1=-\tfrac{17}{128}L^m+\tfrac{21}{256}L^{m-1}-\tfrac{67}{6144}L^{m-2},
$$
$$
C_0=-\tfrac12L^m+\tfrac5{16}L^{m-1}-\tfrac3{64}L^{m-2}.
\tag{43}
$$

这即式 (6)。最终幂均非负，故与 Step 5 相同，
局部化中证明的身份由单射延伸到整个 $\mathbb F_p[L]$。

### Step 7. 整个二阶响应的合并

接受的旧矩为

$$
A_0=1-L^m/2,\quad A_1=L^m/32-L^{m-1}/128,
\quad B_0=L^m/4-L^{m-1}/16.
\tag{44}
$$

将式 (5)、(43)、(44) 代入式 (21)。对 $L^{m-j}$，
$\mathfrak d$ 的特征值为 $j+1/2$；$A_0$ 的额外常数被其算子的 $\mathfrak d$ 因子消去。
逐项贡献为

| 矩来源 | $L^m$ 系数 | $L^{m-1}$ 系数 | $L^{m-2}$ 系数 |
| --- | --- | --- | --- |
| $A_0$ | $-11/5120$ | $0$ | $0$ |
| $A_1$ | $3/4096$ | $-1/16384$ | $0$ |
| $A_2$ | $-93/16384$ | $83/65536$ | $0$ |
| $B_0$ | $-5/1024$ | $1/4096$ | $0$ |
| $B_1$ | $51/2048$ | $-21/8192$ | $0$ |
| $C_0$ | $-3/640$ | $1/2048$ | $0$ |
| 合计 | $135/16384$ | $-41/65536$ | $0$ |

这里 $L^{m-2}$ 的消失不是预设支撑：三个新矩已经完整求值，
其唯一该次幂再由 $(2\mathfrak d-5)$ 消去。得到

$$
\boxed{E_2=\frac{540L-41}{65536}L^{m-1}.}
\tag{45}
$$

### Step 8. 有限移位自身修正与实际高度

接受的有限参数以 $T=z^p$、$H=2-z-z^{-1}$ 定义为
$r=\ell(T)(z-z^{-1})/H$，其中

$$
\ell(T)=\tfrac12(\tau(T)-\tau(T^{-1})),\qquad
\tau(T)=(T-1)-(T-1)^2/2+(T-1)^3/3.
$$

不使用特征 $p$ 的无限对数。
有限展开给 $\ell(T)^2-(T+T^{-1}-2)=O((T-1)^4)$。
因 $T+T^{-1}-2=-H^p$ 且 $(z-z^{-1})^2=H(H-4)$，有

$$
r^2=4H^{2m}-H^{2m+1}+O(H^{4m+1}).
$$

接受的首系数为 $r=2\chi H^m+O(H^{m+1})$。
在除以 $4H^{2m}$ 后比较平方的一次 $H$ 项，因 $2$ 可逆，得到

$$
r=2\chi H^m(1-H/8+O(H^2)),\qquad
r^3=8\chi H^{3m}(1-3H/8+O(H^2)).
\tag{46}
$$

这里 $E_0=0$、$E_1=-3L^m/512$ 是已接受的完整低阶结论。
结合式 (16)、(45)、(46)，形式端点为

$$
\mathcal E=-\frac{3\chi}{64}H^{3m+1}L^m
+H^{3m+2}\left(8\chi E_2+\frac{9\chi}{512}L^m\right)
+O(H^{3m+3})+O(H^{4m}),
$$
$$
\boxed{\mathcal E=-\frac{3\chi}{64}H^{3m+1}L^m
+\frac{\chi}{8192}H^{3m+2}(684L-41)L^{m-1}
+O(H^{3m+3}).}
\tag{47}
$$

最后一个误差确实合法：$m\ge3$ 给 $4m\ge3m+3$。
在 $p=7,m=3$ 时恰为等号；四次移位从 $H^{12}$ 起，
不影响目标 $H^{11}$，但不能因此声称该误差从 $H^{13}$ 起。
准确传播子移位误差 $H^{4m+1}$ 和配对误差也高于目标。

实际两块原始比较误差为 $h^{M-m}$，乘入接受的缺陷高度至少 $m$ 后才为 $h^M$。
由于 $M\ge pm\ge7m\ge3m+3$，原桥误差和所有模 $p$ 系数提升误差
均可并入 $h^{3m+3}\mathcal O^+[L]$。
Step 5、6 的局部化仅用于证明完整多项式的模 $p$ 身份；
实际代入时使用其已经延伸回 $\mathbb F_p[L]$ 的形式，不在实际参数处除以 $L$ 或 $4L-1$。
于是式 (47) 可令 $H=h$ 转回实际 $p^2\mathcal B_3$，再除以 $h^{3m+1}$ 得式 (3)。
证明完成。$\square$

## Corrections or Missing Assumptions

- 全部有限配对只用次数 $<p$ 的低块；没有虚构第 $p$ 阶的单位逆。
- 两次积分分部均说明第 $p$ 阶乘积系数整性，没有重复旧稿中已排除的边界项遗漏。
- 有理证书只在证明中局部化参数；最终三个矩与端点均是全参数多项式身份。
- $p=7$ 的四次移位恰在目标余项阶，不漏项，也不宣称更强精度。
- $p=41$ 的系数消失由通式直接给出；不随之推断未证明的根或更深层性质。

## Open Risks and Delivery Boundary

- 本件完成一般 $p\ge7$ 的 $S\bmod h^2$；仅此有限层不足以确定全部正根 Newton 多边形、
  细分簇、简单性或分裂域。低次数系数仍有尚未求出的 $h^2$ 及更高项。
- 从本层和已接受分离引理可推出的有限根界另由本轮根界稿处理，不在本件重复推导。
- 五的幂已接受结果保持不变；全部负赋值 $p$ 次因子的精细结构仍未完成。
- 没有新增 $\mathcal B_2,\mathcal B_3$ 互素、完整素数幂 $C,Q$ 或实参数全实性结论。
- 本轮仅作自由有理恒等式和有限系数计算；无素数、参数、本原根或根扫描，无拟合。
- 仅新增此本地作者证明；不修改入口、旧冻结稿或锁，不估页、不立项、不作 PDF、Route 或外部操作。
