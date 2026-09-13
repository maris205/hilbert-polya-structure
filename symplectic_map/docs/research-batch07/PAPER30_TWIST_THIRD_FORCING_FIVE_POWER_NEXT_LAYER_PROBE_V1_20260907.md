# Paper30：五的幂第三 forcing 的下一层与二次根簇

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`，
`p5_fourth_shift_collision` 参与本轮有限移位与真实模型的作者核算；
主控共同确定本轮局部因子推论。上述参与者均不是本件的非作者独审。
本轮完整读取 `proof-writer`，按新输入与新结论建立本件；不修改或重审旧接受稿。

## Claim

固定 $p=5$、任意整数 $a\ge2$、任意本原 $5^a$ 次根 $\zeta$，保持同一系统、
物理正 kick、固定参数和 SUM action。取

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad K^+=\mathbb Q_5(h),\qquad \mathcal O^+=\mathbb Z_5[h],
$$
$$
v_h(h)=1,\qquad m=2,\qquad M=v_h(5)=2\cdot5^{a-1}\ge10.
\tag{1}
$$

以全部实际 $n<15$ 模态定义

$$
d_nV_n=-\tfrac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad
d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,
$$
$$
\mathcal B_3=-[x^{14}]e^V-2L[x^{13}]e^{2V},\qquad
S=h^{-7}\,25\mathcal B_3\in\mathcal O^+[L].
\tag{2}
$$

则完整参数多项式的下一层为

$$
\boxed{S(L)=2L^2+h(-2L^2-L-2)+O(h^2).}
\tag{3}
$$

这里 $O(h^2)$ 是 $h^2\mathcal O^+[L]$ 中的逐系数误差，不是固定参数点的误差。
式 (3) 对全部 $a\ge2$ 统一成立；不是只对 $a=2$ 的结果。

调用本轮根簇分离引理，写唯一分解 $S=P_{\rm cl}U_{\rm cl}$，其中
$P_{\rm cl}$ 首一次数二、$\bar P_{\rm cl}=L^2$，
$U_{\rm cl}$ 次数五且在所有有限扩域整参数处取单位值。
则

$$
\boxed{P_{\rm cl}(L)=L^2-\frac h2L-h+O(h^2).}
\tag{4}
$$

这个二次因子在 $K^+[L]$ 上不可约且可分；它的两个根 $\beta_+,\beta_-$ 满足

$$
\boxed{v_h(\beta_\pm)=\tfrac12,\qquad
K^+(\beta_+)=K^+(\beta_-)=K^+(\sqrt h).}
\tag{5}
$$

该二次分裂域相对 $K^+$ 的分歧指数为二、剩余次数为一；
这不是整个七次 $\mathcal B_3$ 的分裂域结论。
选定一个 $\sqrt h$ 后可标记根使

$$
\beta_\pm=\pm\sqrt h+\frac h4+O(h^{3/2}).
\tag{6}
$$

式 (6) 的误差用延拓的 $v_h$ 解释。
对任意有限局部扩域的整参数 $\ell$，有准确距离公式

$$
\boxed{v_h(\mathcal B_3(\ell))
=7-2M+v_h(\ell-\beta_+)+v_h(\ell-\beta_-),}
\tag{7}
$$
$$
\boxed{v_h(V_{15}(\ell))
=3-2M+v_h(\ell-\beta_+)+v_h(\ell-\beta_-).}
\tag{8}
$$

根参数处两侧均允许 $+\infty$。五个负赋值根仍由 $U_{\rm cl}$ 保留，
本件不声明它们简单、具有同一赋值或具有某一因子型。

## Status

式 (3)—(8)：`PROVABLE AS STATED`，作者证明完成，待本轮联合非作者核查。
本件明确保留 $r^3H^2$ 与 $r^4$ 在 $H^8$ 的碰撞；
不将 $p\ge7$ 的公式模五代入，也不由 $p=5$ 外推其他素数。

## Assumptions and Exact Inputs

| 输入 | 本轮用途与状态 | SHA256 |
| --- | --- | --- |
| [一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，843 行 | 已接受；调用式 (17)—(29) 的端点、配对、有限移位和单位响应，不重审 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| [第二阶乘带响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，640 行 | 已接受；调用两实际块与完整形式模型的误差，不重审 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| [本轮根簇分离作者 V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)，455 行 | 新输入，已全文读取；与本件联合待审，调用唯一分解及商的高精度常数性 | `da834676ba00aa72e292acee6281b1a4ee4cd4dc8ebfab964a7fd28b503b7f2f` |

接受的实际／形式误差在乘入端点缺陷后至少为 $h^M$。
本轮根簇稿给出 $e_*=M-7\ge3$ 及
$U_{\rm cl}\equiv a_2\pmod{h^{e_*}\mathcal O^+[L]}$，其中 $a_2=[L^2]S$。
本件的局部因子推论依赖这个新引理，不把它误记为上一轮已接受输入。

## Notation

形式计算先在 $\mathbb F_5[L][[H]]$ 中进行，$O(H^j)$ 表示逐系数形式整除。
最后单独用实际误差桥令 $H=h$。有限级数均模 $x^5$，正次数为 $1\le i\le4$。
记 $\mathcal N=x\partial_x$，真实 Chebyshev 多项式为

$$
C_0=2,\quad C_1=2-H,\quad C_{n+1}=(2-H)C_n-C_{n-1},
\quad d_n(H)=\frac{C_n(H)-2}{H}.
\tag{9}
$$

$P(H,x)$ 是接受的低块，$P_i(h)=V_i$ 对 $1\le i\le4$。
定义 $\mathcal D_kx^i=d_{5k+i}(H)x^i$、$\mathcal D=\mathcal D_0$、
$\Delta_k=\mathcal D_k-\mathcal D$，并记

$$
J=\frac x2e^P+2Lx^2e^{2P},\qquad
K=\frac x4e^P+2Lx^2e^{2P},\qquad \mathscr L=\mathcal D+J.
\tag{10}
$$

接受的零常数单位模型满足

$$
(\mathcal D_1+J)Y=J/2,\qquad
(\mathcal D_2+J)Z=-K(Y-1/2)^2,
$$
$$
y=Y+\tfrac12\mathcal NP,\qquad
Q=Z-\tfrac18\mathcal N^2P+\tfrac12\mathcal Ny.
\tag{11}
$$

这些模型常数是证明工具；实际内部常数已在接受的 $h^M$ 误差中处理。
为避免与 $P_{\rm cl}$ 混淆，下文的 $P$ 始终仅指有限 $x$ 低块。

## Proof Strategy and Dependency Map

1. 调用接受的四项端点与 $h^M$ 比较；不重开第二阶乘带。
2. 保留合法有限移位的三次项，并单列四次响应在 $H=0$ 的常数。
3. 对固定 $i=1,2,3,4$ 使用真实 Chebyshev 多项式，给出可逐项重建的有限解表。
4. 合并 $r$ 自身修正、$r^3H^2$ 和 $r^4$ 三个同阶贡献，再检查实际误差高度。
5. 用本轮唯一根簇与商的高度得到首一二次因子；以判别式证明根域和简单性。

## Proof

### Step 1. 完整四项端点及所需精度

令

$$
\delta_i^{\rm low}=d_i-d_{15-i},\qquad
\delta_i^{\rm mid}=d_{5+i}-d_{10-i},\qquad
C_i^*=\delta_i^{\rm low}-\delta_i^{\rm mid}.
$$

$C_i^*$ 不是式 (9) 的 Chebyshev $C_i$。
接受的模型替换和重组给出形式端点

$$
\begin{aligned}
\mathcal E={}&\frac14\sum_{i=1}^4i^3C_i^*P_iP_{5-i}
+\sum_{i=1}^4i^2C_i^*P_i y_{5-i}\\
&+2\sum_{i=1}^4i\delta_i^{\rm low}P_iQ_{5-i}
+\sum_{i=1}^4i\delta_i^{\rm mid}y_i y_{5-i}.
\end{aligned}
\tag{12}
$$

任一形式整提升与实际 $25\mathcal B_3$ 的比较误差至少为 $h^M$；
改变模五系数的提升也只增加高度至少为 $M$ 的误差。
因此求出式 (12) 模 $H^9$ 即足够，因为 $M\ge10>8$。

### Step 2. 合法移位与第一项的完整配对

沿用接受的有限参数：$z=1+\eta$、$H=2-z-z^{-1}$、$T=z^5$，

$$
\tau(T)=(T-1)-(T-1)^2/2+(T-1)^3/3,
\quad \ell(T)=\tfrac12(\tau(T)-\tau(T^{-1})),
\quad r=\ell(T)\frac{z-z^{-1}}H.
\tag{13}
$$

它属于 $\mathbb F_5[[H]]$。令

$$
\mathsf S_i=\frac{z^i-z^{-i}}{z-z^{-1}},\qquad
\mathsf T_i=\frac{2+Hd_i}{2(H-4)},\qquad
\mathsf U_i=\frac{H\mathsf S_i}{6(H-4)}.
$$

接受的精度在本情形为

$$
\Delta_k(i)=kr\mathsf S_i+k^2r^2\mathsf T_i+k^3r^3\mathsf U_i+O(H^9),\qquad k=1,2,3.
\tag{14}
$$

第一项必须先按 $i\leftrightarrow5-i$ 配对。接受的准确缺陷身份给出

$$
\frac14\sum_i i^3C_i^*P_iP_{5-i}
=\frac{3r^3H}{8(H-4)}\sum_i i^3\mathsf S_iP_iP_{5-i}+O(H^9).
\tag{15}
$$

故这一项在独立移位变量的四次项中没有 $H^0$ 贡献，
但它在式 (15) 的 $r^3H^2$ 层仍有贡献，不能删去。

先以独立 $\nu$ 代替 $r$。单位三角唯一性及式 (14) 保证代回 $\nu=r$
后的模型误差仍在 $H^9$；记
$y=\nu t+O(\nu^2)$、$Q=\nu^2q+O(\nu^3)$。
取接受的耦合方程相应系数，得

$$
\mathscr Lt=\tfrac12\mathsf S\mathcal NP,\qquad
\mathscr Lq=-\tfrac14\mathsf T\mathcal N^2P
+\tfrac12\mathsf S\mathcal Nt-Kt^2.
\tag{16}
$$

于是三次移位系数为

$$
\begin{aligned}
F(H)={}&\frac{3H}{8(H-4)}\sum_i i^3\mathsf S_iP_iP_{5-i}
-6\sum_i i^2\mathsf T_iP_it_{5-i}\\
&+6\sum_i i\mathsf S_iP_iq_{5-i}
+3\sum_i i\mathsf S_it_it_{5-i}.
\end{aligned}
\tag{17}
$$

由于 $v_H(r)=2$，四次项只需在 $H=0$ 求值，五次及更高移位项至少在 $H^{10}$。
式 (15) 已单独保证第一项的精度。因此存在 $E_4(L)$，使

$$
\mathcal E=r^3F(H)+r^4E_4(L)+O(H^9).
\tag{18}
$$

### Step 3. 固定四个低模态的三次响应证书

全部运算在 $\mathbb F_5[L][H]/(H^3)$ 中进行，不使用含 $1/120$ 的通用展开。
式 (9) 直接给出

$$
\begin{array}{c|c|c}
i&d_i(H)&\mathsf S_i(H)\\ \hline
1&-1&1\\
2&1+H&2-H\\
3&1+H-H^2&3-4H+H^2\\
4&-1+2H^2&4-10H+6H^2
\end{array}
\tag{19}
$$

表中整数均按模五解释；$\mathsf T_i$ 由其有单位分母的准确定义计算。
为了完整说明有限表的重建规则，若 $E^{(\alpha)}=e^{\alpha P}$，则

$$
E^{(\alpha)}_0=1,\qquad
E^{(\alpha)}_n=\frac1n\sum_{k=1}^n\alpha kP_kE^{(\alpha)}_{n-k}
\quad(1\le n\le4),
$$
$$
P_n=d_n^{-1}\left(-\tfrac12E^{(1)}_{n-1}-LE^{(2)}_{n-2}\right).
\tag{20}
$$

负下标系数为零；所有 $n$ 和 $d_n(0)$ 均为单位。
在式 (16) 中，$t_n,q_n$ 也按相同的正次数顺序唯一求出：

$$
t_n=d_n^{-1}\left(\tfrac12\mathsf S_n nP_n-
\sum_{k=1}^{n-1}J_kt_{n-k}\right),
$$
$$
q_n=d_n^{-1}\left(-\tfrac14\mathsf T_n n^2P_n+
\tfrac12\mathsf S_n\,n\,t_n-[x^n]Kt^2-
\sum_{k=1}^{n-1}J_kq_{n-k}\right).
\tag{21}
$$

这些有限递推给出以下完整表。每组三列分别为 $H^0,H^1,H^2$ 系数。

| 对象 | $i$ | $H^0$ | $H^1$ | $H^2$ |
| --- | --- | --- | --- | --- |
| $P_i$ | 1 | $-2$ | $0$ | $0$ |
| $P_i$ | 2 | $1-L$ | $L-1$ | $1-L$ |
| $P_i$ | 3 | $2L+1$ | $2$ | $1$ |
| $P_i$ | 4 | $-2L^2+2L-2$ | $2L^2+2L+2$ | $-L^2+2L-2$ |
| $t_i$ | 1 | $1$ | $0$ | $0$ |
| $t_i$ | 2 | $-2L-1$ | $-2$ | $2L$ |
| $t_i$ | 3 | $1-2L$ | $-2$ | $2$ |
| $t_i$ | 4 | $2L^2+2L-1$ | $-L^2-2L+2$ | $2-L$ |
| $q_i$ | 1 | $-1$ | $2$ | $-2$ |
| $q_i$ | 2 | $2L$ | $L$ | $-2L-2$ |
| $q_i$ | 3 | $1$ | $L+2$ | $2-L$ |
| $q_i$ | 4 | $2L-2$ | $-L$ | $-L^2-2L+1$ |

代入式 (17)，四项的逐阶系数为

| 式 (17) 项 | $H^0$ | $H^1$ | $H^2$ |
| --- | --- | --- | --- |
| 第一项 | $0$ | $-L^2-L$ | $-L^2+L-2$ |
| 第二项 | $-L^2$ | $L^2-L$ | $L^2-2L-1$ |
| 第三项 | $-2L^2-2L$ | $2L+1$ | $L^2$ |
| 第四项 | $-2L^2+2L$ | $L^2-1$ | $-L^2-L-1$ |
| 合计 | $0$ | $L^2$ | $1-2L$ |

每一项都是四个自由参数多项式乘积的有限求和，不是参数点的拟合。
因此

$$
\boxed{F(H)=HL^2+H^2(1-2L)+O(H^3).}
\tag{22}
$$

### Step 4. 完整四次移位项不能省略

在 $H=0$，写 $U=P(0)$、$t_0=t(0)$、$q_0=q(0)$、
$\mathscr L_0=-\mathcal N^2+J_0$。为避免同一字母兼用，记

$$
y=\nu t_0+\nu^2a_\nu+O(\nu^3),\qquad
Q=\nu^2q_0+\nu^3b_\nu+O(\nu^4).
$$

此时 $\mathsf S=\mathcal N$、$\mathsf T=-I/4$、$\mathsf U=0$，
故 $\mathcal D_k=-\mathcal N^2+k\nu\mathcal N-k^2\nu^2/4$。
准确耦合方程给出

$$
\mathscr L_0a_\nu=-\tfrac18\mathcal NU-\mathcal Nt_0,
$$
$$
\mathscr L_0b_\nu=\tfrac12\mathcal N^2a_\nu-\tfrac38\mathcal Nt_0
-2K_0t_0a_\nu-2\mathcal Nq_0.
\tag{23}
$$

用与式 (21) 相同的单位三角递推得到

| $i$ | $(a_\nu)_i$ | $(b_\nu)_i$ |
| --- | --- | --- |
| 1 | $2$ | $-2$ |
| 2 | $2-2L$ | $2L+2$ |
| 3 | $L+2$ | $L+1$ |
| 4 | $-2L^2+L+2$ | $-2L^2-2L$ |

式 (14) 给出本次所需的 $H=0$ 缺陷

$$
C_i^*=\tfrac32\nu^2,\quad
\delta_i^{\rm low}=3i\nu+\tfrac94\nu^2,\quad
\delta_i^{\rm mid}=3i\nu+\tfrac34\nu^2.
\tag{24}
$$

式 (24) 用于式 (12) 后三项；第一项已由式 (15) 完整配对，
不可把未经配对的独立 $\nu$ 多项式替换进去。
定义 $\langle f,g\rangle_k=\sum_{i=1}^4i^kf_ig_{5-i}$。
偶权二次矩对称，奇权一次矩反对称；特别地 $\langle t_0,t_0\rangle_1=0$。
故四次系数准确为

$$
E_4=\tfrac32\langle U,a_\nu\rangle_2
+6\langle U,b_\nu\rangle_2
+\tfrac92\langle U,q_0\rangle_1
+6\langle t_0,a_\nu\rangle_2.
\tag{25}
$$

前述完整表直接给出

$$
\langle U,a_\nu\rangle_2=L-2,\quad
\langle U,b_\nu\rangle_2=1-L,\quad
\langle U,q_0\rangle_1=2L-1,\quad
\langle t_0,a_\nu\rangle_2=L.
$$

式 (25) 的四个贡献依次为 $2-L$、$1-L$、$-L-2$、$L$，所以

$$
\boxed{E_4=1-2L\ne0\quad\text{于 }\mathbb F_5[L].}
\tag{26}
$$

### Step 5. 三个同阶贡献与实际误差

从式 (13) 的有限定义可得
$\ell(T)=(T-T^{-1})/2+O((T-1)^3)$。
特征五下 $T-T^{-1}=(z-z^{-1})^5$，并且
$(z-z^{-1})^2=H(H-4)$，因此

$$
r=\tfrac12H^2(H-4)^3+O(H^4)
=-2H^2-H^3+O(H^4).
\tag{27}
$$

这里有限对数差的更高项实际从更高于 $H^3$ 的高度起，不影响式 (27)。
故

$$
r^3=2H^6+3H^7+O(H^8),\qquad r^4=H^8+O(H^9).
$$

式 (18)、(22)、(26) 的 $H^8$ 层有三个来源，全部必须保留：

$$
\underbrace{3L^2}_{r^3\text{ 自身修正}}
+\underbrace{2(1-2L)}_{r^3H^2}
+\underbrace{(1-2L)}_{r^4}
=-2L^2-L-2.
$$

因此

$$
\boxed{\mathcal E=2H^7L^2+H^8(-2L^2-L-2)+O(H^9).}
\tag{28}
$$

本次作者另用式 (9) 生成至 $n=14$ 的真实传播子，直接在
$\mathbb F_5[L][H]/(H^9)$ 中求式 (11) 并代入原式 (12)，得到相同的逐项表：

| 式 (12) 项 | $H^6$ | $H^7$ | $H^8$ |
| --- | --- | --- | --- |
| 第一项 | $0$ | $-2L^2-2L$ | $1-L$ |
| 第二项 | $-2L^2$ | $-L^2-2L$ | $-2L^2+2L$ |
| 第三项 | $L^2+L$ | $-L^2-2L+2$ | $-2L^2+2$ |
| 第四项 | $L^2-L$ | $L^2+L-2$ | $2L^2-2L$ |
| 合计 | $0$ | $2L^2$ | $-2L^2-L-2$ |

每项低于 $H^6$ 的系数为零；总 $H^6$ 层消去。
这张表是同一有限代数身份的作者交叉核算，不是独审，也不替代式 (19)—(27) 的推导。

由 $M\ge10$，接受的实际误差及模五提升误差均高于 $h^8$。
故式 (28) 代入 $H=h$ 后给出

$$
25\mathcal B_3=2h^7L^2+h^8(-2L^2-L-2)+O(h^9)
\quad\text{于 }\mathcal O^+[L].
$$

除以 $h^7$ 即式 (3)。这里没有将实际 $a$ 固定，也没有在分歧扩域擅自取整阶界。

### Step 6. 唯一二次因子、Newton 边与根域

本轮根簇分离输入给出 $S=P_{\rm cl}U_{\rm cl}$，其中
$U_{\rm cl}\equiv a_2\pmod{h^{M-7}}$ 且 $M-7\ge3$。
从式 (3) 有 $a_2=2-2h+O(h^2)$，所以逐系数模 $h^2$ 可除以常数单位 $a_2$：

$$
P_{\rm cl}\equiv \frac{2L^2+h(-2L^2-L-2)}{2-2h}
\equiv L^2-\frac h2L-h\pmod{h^2\mathcal O^+[L]}.
$$

这证明式 (4)。特别地，二次因子的常数系数赋值恰为一，
一次系数赋值恰为一，最高系数为一。
其 Newton 下边连接 $(0,1)$ 与 $(2,0)$；$(1,1)$ 严格在边上方。
也可不引用 Newton 定理而直接判别：
若根的正赋值小于 $1/2$，二次项唯一最低；若大于 $1/2$，常数项唯一最低。
两者均不能相消，所以两个根都只能具有赋值 $1/2$。

写 $P_{\rm cl}=L^2+bL+c$，判别式为

$$
\Delta=b^2-4c=4h(1+O(h)).
\tag{29}
$$

在剩余特征五的完备 DVR 中，任意 $1+h\mathcal O^+$ 都有唯一属于
$1+h\mathcal O^+$ 的平方根：对 $X^2-u$ 从剩余根 $1$ 作 Hensel 提升，
其导数 $2$ 为单位。因此可写 $\Delta=4h\,u^2$，$u=1+O(h)$。
由于 $v_h(h)=1$ 而 $K^+$ 的值群为 $\mathbb Z$，$h$ 不是 $K^+$ 中的平方。
式 (29) 非零且不是平方，证明二次因子不可约、可分，且

$$
K^+(\beta_\pm)=K^+(\sqrt\Delta)=K^+(\sqrt h).
$$

二次根公式给 $\beta_\pm=-b/2\pm u\sqrt h$，再用
$b=-h/2+O(h^2)$、$u=1+O(h)$，得到式 (6)。
$X^2-h$ 为 Eisenstein 多项式，故这个二次扩张完全分歧、剩余次数为一。
这里已经证明两个簇内根简单，没有预先假定所有七个根简单。

### Step 7. 全部有限扩域整参数的点值

本轮分离引理保证 $U_{\rm cl}(\ell)$ 在任意有限扩域整参数处为单位。
又 $P_{\rm cl}=(L-\beta_+)(L-\beta_-)$，故

$$
v_h(S(\ell))=v_h(\ell-\beta_+)+v_h(\ell-\beta_-).
$$

乘回 $\mathcal B_3=h^7\,25^{-1}S$ 得式 (7)。
因 $15<5^a$，接受的实际非共振身份为 $V_{15}=\mathcal B_3/(2d_{15})$，
且 $v_h(d_{15})=4$，于是式 (8) 成立。

例如当 $0\le v_h(\ell)<1/2$ 时，两项距离之和为 $2v_h(\ell)$；
当 $v_h(\ell)>1/2$（包括 $\ell=0$）时，距离之和恰为一。
在 $v_h(\ell)=1/2$ 的边界保留准确距离公式，不强加统一点值。
整个证明适用于任意有限分歧扩域。证明完成。$\square$

## Corrections or Missing Assumptions

- 没有把 $r^4$ 视为高于目标的误差；在 $p=5$ 它恰好位于 $H^8$。
- 没有用分母含五的通用 $H^2$ Chebyshev 展开；有限表来自真实递推。
- 簇内二次根域不是整个第三 forcing 的分裂域；简单性只覆盖这两个正赋值根。
- 根簇因子的模 $h^2$ 确定使用商模 $h^{M-7}$ 的常数性，不能只由 $\bar U_{\rm cl}=2$ 推出。

## Open Risks and Delivery Boundary

- 一般 $p\ge7$ 的三次移位 $H^2$ 系数已有有界响应表达式，
  但所需二阶低块矩的充分系数尚未求值；其 $L^{m-1}$ 或更低项不由本件确定。
  本件不把那个尚未闭合的表达式冻结为一般 Newton 或简单性定理。
- 五的幂的五个负赋值根仍未获得准确 Newton 斜率、因子型或简单性结论。
- 没有新增 $\mathcal B_2,\mathcal B_3$ 互素、完整素数幂 $C,Q$ 或实参数全实性结论。
- 所有有限计算均固定 $p=5$ 且保持 $L$ 为自由符号；无素数、参数、本原根或根扫描。
- 仅新增此本地作者稿；旧接受稿、失败记录和锁不变。未估页、未立项、未构建 PDF、未作 Route 评价或外部操作。
