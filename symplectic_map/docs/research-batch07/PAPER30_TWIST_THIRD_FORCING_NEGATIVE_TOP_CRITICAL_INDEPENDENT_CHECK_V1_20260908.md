# Proof Package：负端最高参数临界层的独立核查 V1

日期：2026-09-08。核查者：`/root/negative_top_review`，不是临界作者稿作者。
本轮使用 `proof-writer`，全文读取冻结的 539 行临界作者稿。
本件只写独立报告；未修改作者稿、旧失败稿、预临界接受记录、批次入口或出版锁。

## Claim

核查对象是
[临界层作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_PROBE_V1_20260908.md)
式 (1)—(3)，以及主控指定的直接根界应用。
对所有素数 $p\ge5$、$a\ge2$，保持原实际分支，令

$$
m=(p-1)/2,\quad M=p^{a-1}m,\quad D=p+m=3m+1,\quad
e_*=M-D,\quad \chi=(-1)^{m+1},\quad C_D=[L^D]\mathcal B_3.
$$

作者的新主张为

$$
\overline{h^{-m}pC_D}=0,\qquad
pC_D\in h^{m+1}\mathcal O^+,\qquad
v_h([L^p]U_{\rm cl})\ge M-2m.
\tag{C}
$$

指定应用为：设

$$
\delta_+=\min\left\{\frac{e_*}{p-1},\frac{M-2m}{p}\right\}.
\tag{A0}
$$

则全部负根按代数重数计，都满足 $v_h(\beta)\le-\delta_+$；
在任何有限局部扩域中，非零参数 $\ell$ 若
$-\delta_+<t=v_h(\ell)\le0$，则

$$
v_h(S(\ell))=mt.
\tag{A1}
$$

不要求下一层非零，不审查其他商系数的新高度，不推出准确 Newton 斜率或根因子型。

## Status

**独立结论：PASS；`PROVABLE AS STATED`。**

作者主张 (C) 与指定应用 (A0)—(A1) 均通过；无需修订冻结的临界作者稿，
无需额外素数排除、改变规范或增加科学假设。
本报告中的 22 项范围核查全部通过；另对五个新增自由符号恒等式作精确核算，残差均为零。

临界 $h^m$ 系数确为零。形式端点标量中的 $p^2$ 只证明本层剩余为零，
不产生未受控制的更高实际赋值。
本次 PASS 不追认旧模 $h$ 作者稿中共振后整体约化的错误；该稿字面 FAIL 保留。

预临界证明及其 23 项独审作为已接受输入使用，没有重跑或重开。
本件是有界数学审查，`route_applicability: NOT_APPLICABLE`，
不等同于 Paper30 正式候选接受、篇幅认证、PDF 验收或任何 Route 通过。

## Assumptions and exact inputs

1. 使用同一 $h=2-\zeta-\zeta^{-1}$、本原 $p^a$ 次根 $\zeta$，
   $v_h(h)=1$、$v_h(p)=M\ge5m$，整数环为 $\mathcal O^+$，剩余域为 $\mathbb F_p$。
2. 使用实际 Chebyshev 传播子与实际递推，所有所用原指标满足 $n<3p<p^a$；
   $p\nmid n$ 时传播子为单位，$v_h(d_p)=v_h(d_{2p})=2m$。
3. 预临界稿的实际最高权重提取、低带整性、正规化高带整性、基带导数身份，
   以及 $pC_D\in h^m\mathcal O^+$ 已通过独审。
   新精度 $h^{m+1}$ 的所有调用在下文重新核界，但不重证未变化的预临界理论。
4. 单谐波正阶有理核的已接受范围是 $1\le k+j\le m$；
   本次只新增使用其中的边界 $k=m,j=0$。
5. 商与根的应用仅使用已接受分解
   $S=P_{\rm cl}U_{\rm cl}$，$P_{\rm cl}$ 首一次数 $m$、全部根正赋值，
   $U_{\rm cl}=u_0+\sum_{j=1}^p u_jL^j$，$u_0$ 为单位，
   $v_h(u_j)\ge e_*$；不把 $u_0$ 与某个同余模型常数认作准确相等。

| 直接输入 | 读取范围与用途 | SHA256 |
| --- | --- | --- |
| [临界层作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_PROBE_V1_20260908.md) | 全文 539 行；唯一新增作者证明 | `b621699d75512e0d762e7e7ac84218f43d80305a0ea6fdac61d236e72e8ebb0a` |
| [预临界证明 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md) | 前一接续任务已全文读取 306 行；本轮重用已接受基线和 Step 8 | `033a05a8bc6f9d34125696366bf0ee23f84682049df1d7edd8dd80c702929502` |
| [预临界独审 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | Claim、Status、准确输入；确认 23 项 PASS 范围 | `0793aa675cd71c7123c7efe7f782bc219de4cdd671d63f0781d46a901439653f` |
| [高阶低块结构 V1](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | Claim 1—2、Step 4；核对临界 $k=m$ 确在量词内 | `af5cd169e101948d9732cf9f913181ba2697e9fa9b4a848eebd1ffda841f21d1` |

定向读取的既有审查依据还包括：
[统一正簇独审 §5.2](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_INDEPENDENT_CHECK_20260907.md)
的临界整性论证，以及
[第二阶乘响应桥 Step 5、式 (34)—(35)](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)
与
[联合独审的实际移位核查](PAPER30_TWIST_THIRD_FORCING_GENERAL_AND_BRIDGE_INDEPENDENT_CHECK_20260907.md)。
只检查本次调用是否落在接受范围，没有重开旧证明链或扫描旧构建树。

## Notation

沿用 $u=Lx^2/4$、$\Theta=u\partial_u$，
$V|_{b=0}=W(u)$、$\partial_bV|_{b=0}=xA(u)$。
工作环为

$$
R_*=\mathcal O^+/h^{m+1}\mathcal O^+.
$$

该环具有特征 $p$，因为 $M\ge m+1$。
记 $w=W_{<p}\bmod h^{m+1}$、$a=A_{<m}\bmod h^{m+1}$，
$f_1=e^w$、$f_2=e^{2w}$ 只取次数小于 $p$ 的合法系数。
$\tau$、$\sigma$ 分别是 $pW_{p+j}$、$pA_{p+j}$ 的正规化高带剩余，
截断次数分别为 $m$、$m-1$。
带下标零的函数表示模 $h$ 的基带：

$$
f_{10}=(1-u)^{-1},\quad f_{20}=(1-u)^{-2},\quad
a_0=\frac1{2(1-u)}.
$$

它们不代表未正规化奇共振后的 $A_m,\ldots,A_{p-1}$。

## Proof Strategy and dependency map

只核查由模 $h^m$ 提高到模 $h^{m+1}$ 所需的新义务：

1. 临界有理核整性是否覆盖第 $p$ 个 ghost 系数；
2. 参照级数与实际递推的误差是否仍在 $h^{m+1}$；
3. 临界 Chebyshev 移位的常数、符号和 $p$ 分母是否正确；
4. 偶、奇响应以及奇响应常数项是否完整；
5. 端点提取是否使用全部修正，并只得出本层结论；
6. 将新最高项下界代回已接受的最低赋值项论证，核查指定应用。

## Scope checklist

以下行号均指绑定哈希的临界作者稿；每项 PASS 的实质理由见随后独立推导。

| 项 | 对象与定位 | 结论 |
| --- | --- | --- |
| C01 | Step 1，式 (8)—(9)：同一目标、权重与系数 $16$ 未改变 | PASS |
| C02 | 假设及 Step 3，第 245—252 行：$k=m,j=0$ 在已接受整性范围内 | PASS |
| C03 | Step 3：正阶 ghost 的全局有限分子恢复，不漏 $u^p$ | PASS |
| C04 | 第 226—243 行：倍角、变量 $16u/(4-H)$ 和未知量 $2G$ 的因子 | PASS |
| C05 | 第 255—264 行：$pG$ 唯一对数 ghost 与 $c^p=1$ | PASS |
| C06 | 第 266—272 行：指数 $Q^q/q!$ 的两类实际高度 | PASS |
| C07 | 第 257—259 行：实际低带高 $H$ 余项整性独立于未知 $R_{m+1,0}$ | PASS |
| C08 | 第 292—296 行：低带误差与正规化高带相乘仍保留目标高度 | PASS |
| C09 | Step 2，式 (11)：$M-2m\ge3m\ge m+1$ | PASS |
| C10 | 第 199—209 行：奇共振与非整指数最早相遇于 $u^{p+m}$，不在目标中 | PASS |
| C11 | 式 (6)、(16)：临界差分先消去 $p$ 分母后为 $4\chi n$ | PASS |
| C12 | 第 303—305 行：形式模 $p$ 移位转回实际 $R_*$ 的精度 | PASS |
| C13 | Step 5，式 (20)—(22)：偶响应 $t$、零常数和单位唯一性 | PASS |
| C14 | Step 6，式 (25)—(27)：保留奇移位中的常数项，$s_0=-2\chi$ | PASS |
| C15 | 式 (26)—(27)：奇响应驱动及解的完整有理身份 | PASS |
| C16 | Step 7，式 (28)—(31)：完整修正核、端点组合与临界消失 | PASS |
| C17 | 式 (3)：首一最高项的高度为至少 $M-2m$ | PASS |
| C18 | Corrections/Open Risks：不把形式 $p^2$ 因子兑换成下一层实际精度 | PASS |
| A01 | 指定应用：$\delta_+>e_*/p>0$ | PASS |
| A02 | 指定应用：全部负根满足闭下界 $v_h(\beta)\le-\delta_+$ | PASS |
| A03 | 指定应用：$-\delta_+<t\le0$ 上 $v_h(S(\ell))=mt$ | PASS |
| A04 | 端点和改进幅度：新左端开放，旧 $-e_*/p$ 包含，不声称对预临界界总是严格改善 | PASS |

## Proof

### Step 1. 临界有理核确实消除了正阶 ghost 风险

高阶结构输入不是只证明了 $k<m$。它明确包括 $k=m,j=0$，并给出

$$
R_{m,0}(z)=\frac{B(z)}{(1-z)^{2m}},\qquad \deg B\le2m=p-1.
$$

真实单谐波有限低块在 $z^0,\ldots,z^{p-1}$ 的系数均为 $p$-整。
将这 $p$ 个 Taylor 系数乘以整数多项式 $(1-z)^{p-1}$，
已恢复 $B$ 的所有系数；因此 $B\in\mathbb Z_{(p)}[z]$。
于是整个有理核的每个 Taylor 系数都为 $p$-整，**包括第 $p$ 个及后续 ghost 系数**。
这里没有假定第 $p$ 个实际单谐波递推的传播子是单位，也没有通过那个传播子求解。
这只是已接受有理结构与有限分子恢复在临界边界的准确应用。

准确倍角变换给出作者式 (13)：

$$
G(H,u)=\frac12P\left(H(4-H),0,\frac{16u}{4-H}\right).
$$

单谐波未知量为 $2G$；其右侧是 $-8u e^{2G}/(4-H)$，
除以二后乘回 $4-H$，确实是纯偶方程 $\mathcal D_eG=-4u e^{2G}$。
对已知 $R_{1,0},\ldots,R_{m,0}$ 作有限代换，保持 $p$-整性，得到

$$
G=-\log(1-cu)+Q,
\qquad c=(1-h/4)^{-1},\quad Q\in h\mathcal O^+[[u]],\quad Q(0)=0,
\tag{P1}
$$

其中 $Q$ 只保留 $H$ 次数至 $m$ 的有理核。对 $r<p$，
真实 $W_r(H)$ 的整个 $H$-Taylor 展开由常数为 $-4r^2$ 的单位三角递推保证 $p$-整，
故 $W_r-G_r\in h^{m+1}\mathcal O^+$。

本次使用的是有限参照 (P1)，没有声称真实高带 $W_{\ge p}$ 与这个参照逐项接近；
真实高带仍保留为未知的 $\tau$。因此没有借未接受的 $R_{m+1,0}$ 控制实际高带。

### Step 2. 唯一对数 ghost、指数误差与奇共振污染

在 $N<2p$ 内，$pG_N$ 的可能非零剩余仅来自零阶对数的 $N=p$ 项，
其值为 $c^p$。正阶有理核的相应系数均整，乘 $p$ 后消失。
又因 $R_*$ 为特征 $p$ 且 $h^p=0$，

$$
c^p=(1-h^p/4^p)^{-1}=1\quad\text{在 }R_*\text{ 中}.
\tag{P2}
$$

指数不能直接由形式整性推断。对 $c_0=1,2$ 使用准确的有限身份

$$
e^{c_0G}=(1-cu)^{-c_0}e^{c_0Q}.
$$

$[u^N]e^{c_0Q}$ 只出现 $q\le N<2p$ 个 $Q$ 因子。
$q<p$ 时 $v_h(p/q!)=M$；$p\le q<2p$ 时 $v_h(p/q!)=0$，
但 $Q^q$ 的每项高度至少为 $q\ge p=2m+1\ge m+1$。
两个范围都使 $p[u^N]e^{c_0G}$ 属于 $h^{m+1}\mathcal O^+$。

实际与参照低带的差属于 $h^{m+1}$。低带指数在总次数小于 $2p$ 时
至多有一个阶乘 $p$ 分母，正规化后误差仍在 $h^{m+1}$。
如有一个真实高带因子，其 $p$ 倍整，余下低指数次数小于 $p$，
所以低带误差乘高带也不会损失高度。两个高带同时出现的次数至少为 $2p$。
这独立核实了作者式 (15) 在新精度的合法性：

$$
E_1=f_1(\tau-1),\qquad E_2=2f_2(\tau-1).
\tag{P3}
$$

另一方面，已接受粗界 $v_h(W_p),v_h(A_s)\ge-2m$、$m\le s<p$
提高到新目标仍足够，因为

$$
M-2m\ge3m\ge m+1\qquad(m\ge2).
\tag{P4}
$$

在总次数 $N\le p+m-1$ 的指数响应积中，若 $s\ge m$ 且 $s<p$，
则指数下标 $N-s\le p-1$，对应指数系数整。
于是这些项乘 $p$ 后的高度至少为 $M-2m$，可模 $h^{m+1}$ 舍去。
这里仅将原先已证的支撑与粗界对照新精度，没有把奇共振后的 $A_s$ 本身约化。

### Step 3. 独立复算临界移位的符号、倍数及分母

使用预临界稿的真实系数公式

$$
[H^k]d_n(H)=D_k(n),\qquad
D_k(X)=\frac{(-1)^{k+1}X^2\prod_{r=1}^k(X^2-r^2)}{(k+1)(2k+1)!}.
$$

在 $k<m$ 时分母为 $p$ 单位，所以 $D_k(n+2p)-D_k(n)\equiv0\pmod p$。
临界 $k=m$ 的分母含一个 $p$，必须先在整数差分中消去这个因子。
令

$$
N(X)=X^2\prod_{r=1}^m(X^2-r^2)\in\mathbb Z[X].
$$

整数 Taylor 差分满足

$$
\frac{N(n+2p)-N(n)}p\equiv2N'(n)\pmod p.
\tag{P5}
$$

由于 $\{\pm1,\ldots,\pm m\}=\mathbb F_p^\times$，

$$
N(X)\equiv X^{p+1}-X^2\pmod p,
\qquad N'(n)\equiv n^p-2n=-n\pmod p.
$$

再用 $(m+1)\equiv1/2$ 和 $(p-1)!\equiv-1\pmod p$，得到

$$
\begin{aligned}
D_m(n+2p)-D_m(n)
&\equiv\frac{2\chi N'(n)}{(m+1)(p-1)!}
=4\chi n\pmod p.
\end{aligned}
\tag{P6}
$$

这与已接受的桥式 (34)—(35) 一致，并独立排除了常见的符号或因子二错误。
因为实际 $d_n(H)$ 为整系数多项式，未显示的低系数误差是 $p$ 倍，
代入 $h$ 后高度至少 $M$；高 $H$ 次数误差至少为 $m+1$。
故实际移位在 $R_*$ 中是

$$
\Delta_e=8\chi h^m\Theta,\qquad
\Delta_o=4\chi h^m(2\Theta+1),
\tag{P7}
$$

分别用于偶下标 $1\le j\le m$ 与奇下标 $0\le j<m$。
未在除以 $p$ 之前把临界分子粗略约化；也未把普通模 $p$ 同余乘以非整高带。
参与 (P7) 方程的是已经证明整的正规化高带。

### Step 4. 偶、奇临界响应均唯一，奇常数项不可遗漏

令 $\mathcal L_e=\mathcal D_e+8uf_2$、
$\mathcal L_o=\mathcal D_o+8uf_2$。
已接受的基带导数身份给出

$$
\tau^{\rm b}=-2\Theta w,\qquad
\sigma^{\rm b}=-(1+2\Theta)a.
$$

应用新移位 (P7)，作者的实际高带方程 (17)—(18) 正确。
构造候选

$$
\tau=\tau^{\rm b}+h^m t,\qquad
\sigma=\sigma^{\rm b}+h^m s.
$$

乘 $h^m$ 的系数只需模 $h$，交叉临界项在 $h^{2m}\subseteq h^{m+1}$ 中。
不是在含零因子的 $R_*$ 中非法约去 $h^m$：下列有限 $\mathbb F_p$ 响应解
给出一个满足实际方程的候选，随后由实际单位三角唯一性识别它与真实高带相同。

偶响应算子为

$$
\mathcal L_{e0}=-4\Theta^2+\frac{8u}{(1-u)^2}.
$$

其驱动为 $16\chi u/(1-u)^2$，而

$$
\mathcal L_{e0}\left(\frac{u}{1-u}\right)
=-\frac{4u}{(1-u)^2}.
$$

因此 $t=-4\chi u/(1-u)$。它的常数项为零；
所用对角元 $-4j^2$、$1\le j\le m<p$ 都是单位。

奇响应算子为

$$
\mathcal L_{o0}=-(2\Theta+1)^2+\frac{8u}{(1-u)^2}.
$$

其完整驱动为

$$
-\tfrac12f_{10}t-16uf_{20}a_0t
-4\chi(2\Theta+1)\sigma^{\rm b}_0
=\frac{2\chi(1+3u)^2}{(1-u)^4}.
$$

对 $s=-2\chi/(1-u)^2$ 应用 $\mathcal L_{o0}$，结果正是这一驱动。
全部对角元 $-(2j+1)^2$、$0\le j<m$ 是单位，故响应唯一。
特别是常数项满足

$$
\sigma_0=\frac{1}{2(-1+4\chi h^m)}
=-\frac12-2\chi h^m\quad\text{在 }R_*\text{ 中}.
\tag{P8}
$$

所以 $s_0=-2\chi$。作者保留了奇移位的常数部分，没有擅自设置零常数规范。

### Step 5. 完整临界端点的确为零，只得到这一层

由已接受的基带导数身份及本轮两个响应，

$$
E_1=-(1+2\Theta)f_1+h^mf_{10}t,
$$
$$
f_2\sigma+E_2a=-(3+2\Theta)(f_2a)+h^mK,
\qquad K=f_{20}(s+2a_0t)=-\frac{2\chi(1+2u)}{(1-u)^4}.
\tag{P9}
$$

实际最高权重身份仍为
$4^DpC_D=-[u^m]E_1-16[u^{m-1}](f_2\sigma+E_2a)$。
代入 (P9)，基带两项分别带系数 $2m+1=p$，在 $R_*$ 中为零。
留下的临界标量为

$$
\begin{aligned}
\mathfrak c_m
&=-[u^m]f_{10}t-16[u^{m-1}]K\\
&=4\chi m+32\chi\left\{\binom{m+2}{3}+2\binom{m+1}{3}\right\}\\
&=4\chi m+16\chi m^2(m+1)
=4\chi m(2m+1)^2.
\end{aligned}
\tag{P10}
$$

这里偶修正、奇修正和 $2a_0t$ 全部参与，没有只保留偶响应。
有限系数身份的分母仅含 $2,3$，对所有 $p\ge5$ 为单位。
因此 $\mathfrak c_m=0$ 在 $\mathbb F_p$ 中成立，
从而 $pC_D\in h^{m+1}\mathcal O^+$。

由首一性，$[L^p]U_{\rm cl}=h^{-D}p^2C_D$，于是

$$
v_h([L^p]U_{\rm cl})
\ge M-D+m+1=M-2m.
$$

这证明 (C)。式 (P10) 的形式 $p^2$ 因子不影响实际误差仍仅受控于
$h^{m+1}$ 这一事实，故本轮不能增加第二个临界层结论。

### Step 6. 指定根界与点值应用

令 $U_{\rm cl}=u_0+\sum_{j=1}^p u_jL^j$。
重用预临界 Step 8 的论证，只把最高系数下界换成 $M-2m$：

$$
v_h(u_0)=0,\qquad v_h(u_j)\ge e_*\ (1\le j<p),
\qquad v_h(u_p)\ge M-2m.
$$

$e_*>0$，且 $M-2m=e_*+m+1$，所以

$$
\delta_+>e_*/p>0.
$$

若 $-\delta_+<t=v_h(\ell)\le0$，则对 $1\le j<p$，

$$
v_h(u_j\ell^j)\ge e_*+jt
\ge e_*+(p-1)t>0,
$$

而

$$
v_h(u_p\ell^p)\ge M-2m+pt>0.
$$

两处严格不等式分别使用
$\delta_+\le e_*/(p-1)$、$\delta_+\le(M-2m)/p$ 及左端开放。
常数项因此是唯一最低赋值项，$U_{\rm cl}(\ell)$ 为单位。
已接受的全部根负赋值结论随即给出
$v_h(\beta)\le-\delta_+$，根重数不改变该推理。

若 $\alpha$ 是 $P_{\rm cl}$ 的根，则 $v_h(\alpha)>0\ge t$，故
$v_h(\ell-\alpha)=t$。$P_{\rm cl}$ 首一次数 $m$，按重数乘积得到
$v_h(P_{\rm cl}(\ell))=mt$，因此 $v_h(S(\ell))=mt$。
这在任意有限局部扩域中成立，不要求扩域值群为整数，也没有包括 $\ell=0$。

新左端 $-\delta_+$ 仍开放；最初的端点 $-e_*/p$ 严格位于区间中。
与预临界的
$\delta=\min\{e_*/(p-1),(e_*+m)/p\}$ 比较，只有 $\delta_+\ge\delta$，
不保证严格。事实上 $a=2$ 时 $M=pm$，

$$
\frac{e_*}{p-1}=m-1-\frac1{2m},\qquad
\frac{e_*+m}{p}=m-1,\qquad
\frac{M-2m}{p}=m-1+\frac1p,
$$

因此 $\delta_+=\delta=e_*/(p-1)$。
最高项下界提高一阶与每个参数下统一根界严格改善是两个不同的陈述；
本报告只通过前者及 (A0)—(A1)。$\square$

## Actual error closure and verification record

| 新精度下必须核验的来源 | 实际最低高度／支撑 | 处理 |
| --- | --- | --- |
| 正阶临界有理核，包括 ghost 系数 | 核本身 $p$-整；参照 $Q$ 至少含 $h$ | 合法保留至 $H^m$ |
| 实际整低带与有限参照之差 | $m+1$，先乘 $p$ 清除唯一阶乘分母 | 可舍 |
| 上述低带误差乘一个高带 | 高带的 $p$ 倍整，剩余低指数次数 $<p$ | 高度仍为 $m+1$ |
| $W_p$ 或中间奇层乘整指数 | $M-2m\ge3m\ge m+1$ | 可舍 |
| 参照指数的 $q<p$ 项 | 至少 $M$ | 可舍 |
| 参照指数的 $p\le q<2p$ 项 | 至少 $q\ge p>m$ | 可舍 |
| Chebyshev 差分的剩余低系数误差 | 至少 $M$；只乘正规化整高带 | 可舍 |
| 下一 $H$ 阶及两个临界修正相乘 | 分别为 $m+1$、$2m\ge m+1$ | 可舍 |
| 非整偶指数与奇共振相遇 | 最低 $u$ 次数为 $p+m$，所需乘积至多 $p+m-1$ | 不出现 |

本轮另用自由符号 $u,\chi,m$ 运行了五个即时精确有理核算，输出如下：

```text
even_response: 0
odd_forcing: 0
odd_response: 0
complete_endpoint_kernel: 0
endpoint_integer_identity: 0
```

这些是本文 Step 4—5 的新临界有理身份；没有给任何符号代入素数样本，
没有根扫描或拟合，也没有执行旧 39 项测试或重跑预临界 23 项核查。
程序残差仅防止代数笔误；整性、误差、量词与应用由上文证明负责。

## Corrections or Missing Assumptions

本轮未发现必须修正的临界作者稿证明错误，冻结 V1 保持原样。
最终处置应保持以下已核清区别：

- $k=m$ 正阶有理核确在旧接受范围内，$k=m+1$ 不在；
  不能将本次 PASS 自动外推。
- 奇响应常数项与完整端点组合不可删去；只算偶响应不足以证明本层消失。
- $\delta_+>e_*/p$，但相对预临界 $\delta$ 不总是严格增大。
- 本轮只证明临界层为零和相应下界；不报告准确最高项赋值或非零负端锚点。

## Open Risks

- $h^{m+1}$ 层的系数仍未计算；本报告没有审查下一层的有理核整性、移位或共振残量。
- 其他商系数的新准确高度、完整负 Newton 图、简单性、因子型和野分裂域仍开放。
- (A1) 不包含新左端 $t=-\delta_+$，也不包含零参数；本轮没有排除边界最低项并列。
- 本报告只新增本地独审票；不修改任何接受登记、旧失败证据或论文产物状态。
