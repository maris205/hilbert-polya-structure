# Proof Package：第三 forcing 负商次高系数的首层消失

日期：2026-09-08。作者：`/root/negative_subtop_author`。
按 `proof-writer` 编写；本件为新作者稿，不是非作者独立验收。
只处理同一实际构造的负商次高系数，不改写最高项、正簇或旧失败稿。

## Claim

固定任意素数 $p\ge5$、整数 $a\ge2$，令
$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=p+m,\qquad e_*=M-D.
$$
在既有实际分解
$$
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
P_{\rm cl}=L^m+\sum_{i<m}b_iL^i,\quad
U_{\rm cl}=\sum_{j=0}^{p}u_jL^j
$$
中，证明
$$
\boxed{p[L^{D-1}]\mathcal B_3\in h\mathcal O^+,\qquad
\gamma_{p-1}:=\overline{h^{-e_*}u_{p-1}}=0.}                 \tag{1}
$$
特别地 $v_h(u_{p-1})\ge e_*+1$。这是下界，不是准确赋值。
次高项的下一层、负因子的完整下凸包、准确斜率、因子型和简单性均不由本件确定。

## Status

`PROVABLE AS STATED`：以下给出一般素数的作者证明。
没有预设目标非零，没有素数或参数扫描，也不从最高项的消失直接推断次高项。
二次、三次辅助幅度响应和第二次偶共振均保留在证明内。

## Assumptions and accepted inputs

保持实际圆分规范
$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad K^+=\mathbb Q_p(h),\quad \mathcal O^+=\mathbb Z_p[h],
$$
其中 $\zeta$ 为本原 $p^a$ 次根，$v_h(h)=1$、$v_h(p)=M\ge5m$。
实际有限递推及 forcing 是
$$
d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}
             -L[x^{n-2}]e^{2V(b)},\qquad 1\le n<3p,
\quad d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,                    \tag{2}
$$
$$
\mathcal B_3=-[x^{3p-1}]e^{V(1)}-2L[x^{3p-2}]e^{2V(1)}.    \tag{3}
$$
辅助幅度 $b$ 只用于提取齐次系数，实际仍取 $b=1$。
由于 $3p<p^a$，本件的所有实际传播子均非零；
$p\nmid n$ 时 $d_n$ 为单位且 $d_n\equiv-n^2\pmod h$，
$v_h(d_p)=v_h(d_{2p})=2m$。

只调用以下已接受输入，不重新审查其未变证明：

- [首层内部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
  式 (3)：$h^mV_p(L)\in\mathcal O^+[L]$。
  齐次性使它逐系数适用于 $V_p(b,L)$；本件只需要整性，不需要其准确剩余。
- [本轮负端最高项处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)：
  分解的次数、$u_j\in h^{e_*}\mathcal O^+$（$j\ge1$）、
  $b_i\in h\mathcal O^+$（$i<m$），以及已接受的
  $v_h(u_p)\ge e_*+m+1=M-2m$。
- [负端替代证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_ALTERNATIVE_V1_20260908.md)
  中同一纯偶变量与有限递推的规范。下文重新给出本件需要的响应递推及整性证明，
  不使用其只针对一次响应的乘积支撑作为二、三次响应的黑箱。

## Notation

置 $t=bx$、$u=Lx^2/4$。权重为 $\deg_x(t)=1$、$\deg_x(u)=2$。
对辅助幅度只保留 $b$ 次数至三，即在 $t^4=0$ 下写
$$
V=W(u)+tA(u)+t^2C(u)+t^3E(u)\pmod{t^4}.                   \tag{4}
$$
$C,E$ 是在 $b^2,b^3$ 泰勒系数中提出 $x^2,x^3$ 后的响应，
不是未经除以 $2!,3!$ 的导数。
所有运算同时截断到权重严格小于 $3p$；这是真正的下降封闭有限系数区域。
定义
$$
\Theta=u\partial_u,\qquad \mathscr N=t\partial_t+2\Theta,
\qquad F_\alpha=e^{\alpha W}\quad(\alpha=1,2).
$$
指数只代表所需的有限系数运算，不宣称 $p$-进解析收敛。
横线只作用于已证明整的系数；剩余域为 $\mathbb F_p$。

## Proof Strategy

先把次高项化为二、三次响应。将四个实际内部响应值保留为独立初值，
并建立零初值的辅助分支。通过权重证明实际／辅助差只含一次内部值，
或两个第一内部值，其系数为整数；乘 $p$ 后误差消失。
对辅助分支的完整 $u^p$ 阶乘带先证明整性再约化，得
正规化高带 $\tau=-\mathscr Nw$。最后两个端点的缩放乘子恰均为 $p$。

## Dependency Map

1. 齐次性和指数的完整三阶展开给出端点式 (8)。
2. 第一次内部整性及实际传播子高度给出四个初值的界 (10)。
3. 有限权重和零共振初值的辅助分支给出实际／辅助误差 (13)。
4. 单个阶乘带及单位三角递推给出高带恒等式 (19)、(22)。
5. 两个准确端点乘子和首一商的唯一交叉项给出式 (1)。

## Proof

### Step 1. 完整二、三次响应与准确端点

按 $n$ 在 (2) 中归纳：$[L^j]V_n(b)$ 是 $b^{n-2j}$ 的常数倍。
这是因为 $b,L$ 的权重分别为 $1,2$，两项 forcing 恰将指数系数的权重补至 $n$。
故 (4) 中的四个响应唯一确定本件需要的最高四条参数带。
在特征零将指数展开至三阶，得到
$$
\begin{aligned}
e^{V}&=F_1\left(1+tA+t^2(C+A^2/2)
                       +t^3(E+AC+A^3/6)\right),\\
e^{2V}&=F_2\left(1+2tA+t^2(2C+2A^2)
                       +t^3(2E+4AC+4A^3/3)\right)
\pmod{t^4}.                                                \tag{5}
\end{aligned}
$$
提取实际递推给
$$
\begin{aligned}
d_{2r}W_r&=-4[u^{r-1}]F_2,\\
d_{2r+1}A_r&=-\tfrac12[u^r]F_1-8[u^{r-1}]F_2A,\\
d_{2r+2}C_r&=-\tfrac12[u^r]F_1A-8[u^{r-1}]F_2(C+A^2),\\
d_{2r+3}E_r&=-\tfrac12[u^r]F_1(C+A^2/2)
             -8[u^{r-1}]F_2(E+2AC+2A^3/3).
                                                               \tag{6}
\end{aligned}
$$
负下标系数按零处理。仅在 $W$ 的第一式中要求 $r\ge1$。
可将 (6) 写成
$$
\mathscr D V=-\frac t2e^V-4u e^{2V},\qquad
\mathscr D(t^ku^r)=d_{k+2r}t^ku^r.                          \tag{7}
$$

第一 forcing 的 $L^{D-1}=L^{3m}$ 项需要 $b^2$ 响应；
第二 forcing 在提出外部 $L$ 后需要 $b^3L^{3m-1}$。
因此准确公式是
$$
\boxed{
[L^{D-1}]\mathcal B_3=-4^{-(D-1)}\left(
[u^{3m}]F_1(C+A^2/2)
 +16[u^{3m-1}]F_2(E+2AC+2A^3/3)\right).}                  \tag{8}
$$
第二项的 $16$ 同时包含外部 $-2L$、三阶指数系数的因子 $2$
和变量 $u=Lx^2/4$ 的一个缩放因子 $4$。这里没有只保留线性响应。

### Step 2. 四个实际共振初值及新增偶共振的界

在 $t^4=0$、权重小于 $3p$ 的区域，非单位传播子恰对应四个单项式：
$$
t u^m,\quad t^3u^{m-1}\qquad(n=p),\qquad
u^p,\quad t^2u^{p-1}\qquad(n=2p).
$$
记它们的实际系数为
$$
q_A=A_m,\quad q_E=E_{m-1},\quad q_W=W_p,\quad q_C=C_{p-1}.
                                                               \tag{9}
$$
既有 $h^mV_p(L)$ 的逐参数整性和 $4$ 为单位给
$v_h(q_A),v_h(q_E)\ge-m$。
纯偶递推对 $r<p$ 只涉及单位传播子和次数小于 $p$ 的指数，故 $W_r$ 整；
$r=p$ 时右端仍整，所以 $v_h(q_W)\ge-2m$。

为估计新增的 $q_C$，先看 $r<p$ 的奇响应。
在 $A_m$ 前它整，其后至 $r=p-1$，递推是单位三角系统，
只含低于 $u^p$ 的整偶指数；故 $v_h(A_r)\ge-m$。
在 $C_r$ 的 $r<p-1=2m$ 区间，$A^2$ 的所需次数为
$r-1\le2m-2$，不可能同时使用两个下标至少为 $m$ 的奇响应。
因此在此区间 $v_h(C_r)\ge-m$。
到 $r=p-1=2m$，$F_1A$ 仍只用整偶指数乘一个这样的奇响应，
$F_2A^2$ 的次数是 $2m-1$，依旧排除两个 $A_m$ 后的因子。
故 (6) 的第三式右端赋值至少 $-m$；除以高度 $2m$ 的 $d_{2p}$ 后得到
$$
\boxed{v_h(q_A),v_h(q_E)\ge-m,\qquad
v_h(q_W)\ge-2m,\qquad v_h(q_C)\ge-3m.}                    \tag{10}
$$
这是实际初值的界，没有对它们作未经正规化的模 $h$ 约化。

### Step 3. 零初值辅助分支与严格共振误差控制

定义辅助分支 $\widetilde V$：在 (9) 的四个位置把系数指定为零，
其余位置仍按同一实际递推 (7) 求解。
这些零值是有限证明装置，不改变实际分支。
所有未被指定的位置，其 $d_n$ 都是单位，故辅助分支唯一存在。

首先，$\widetilde V$ 的全部 $u$ 次数小于 $p$ 的系数整。
其证明是按权重归纳：在 $t^4=0$ 下先将指数展开成
$e^{\widetilde W}$ 乘一个 $t$ 次数至三的多项式；
后者的分母只含 $2,3$，而前者的 $u^r$ 系数在 $r<p$ 时只含单位阶乘。
四个指定零初值不引入除法，其余传播子均为单位。
同一论证给出
$$
[t^ku^r]e^{\alpha\widetilde V}\in\mathcal O^+
\quad\text{若 }k+2r<2p,\quad k\le3,\quad\alpha=1,2.       \tag{11}
$$

现在暂将四个 $q$ 看成独立形式变量，在共振位置指定这些值，并在其余位置
按单位三角递推得到 $V(q)$。零值给 $\widetilde V$，实际四元组给 $V$。
令 $\Delta=V(q)-\widetilde V$。给 $q_A,q_E$ 标记最低权重 $p$，
给 $q_W,q_C$ 标记最低权重 $2p$；递推中的 $t,u$ 因子及指数乘积不降低权重。
因而 $\Delta$ 始于权重 $p$，且在权重小于 $3p$ 时
$$
e^{\alpha V(q)}-e^{\alpha\widetilde V}
=e^{\alpha\widetilde V}
\left(\alpha\Delta+\frac{\alpha^2}{2}\Delta^2\right).      \tag{12}
$$
三次项始于权重 $3p$，已经在本件区域之外。

按权重归纳，$\Delta$ 以及 (12) 的每个系数都是 $q$ 的整系数多项式。
具体地，(12) 中任何含 $\Delta$ 的乘积，其背景指数只能使用权重小于 $2p$
的系数；这些系数由 (11) 整。其余步骤仅为加乘和单位传播子除法，
所以归纳封闭。每个出现的 $q$ 单项式只能是一次项，或两个来自
$\{q_A,q_E\}$ 的因子；含 $q_W,q_C$ 的任何二次项权重至少为 $3p$。

将实际初值代入并用 (10)，一次项最低高度至少为 $-3m$，
两个第一次内部值的乘积高度至少为 $-2m$。因此得到本件需要的逐系数界
$$
\boxed{V-\widetilde V,\quad
e^{\alpha V}-e^{\alpha\widetilde V}
\in h^{-3m}\mathcal O^+
\quad(t^4=0,\;\deg_x<3p),\quad \alpha=1,2.}               \tag{13}
$$
由于 $M-3m\ge2m\ge4$，这些差先乘 $p$ 后都属于 $h\mathcal O^+$。
这同时处理新增偶共振、两个第一次内部值的乘积、二次和三次幅度响应。
它不是只利用 $pA_m\equiv0$ 的单因子论证。

### Step 4. 辅助分支的完整单阶乘带

在本件有限区域写
$$
\widetilde V=T+R,\qquad
T=\sum_{r<p,\;k\le3}[t^ku^r]\widetilde V\,t^ku^r,
\quad R\in u^pK^+[t,u]/(t^4).
$$
$T$ 的系数由 Step 3 全整，且无常数项；$R^2$ 的权重至少 $4p$，
不出现于本件窗口。对窗口内的单项式 $t^ku^r$，指数中所需因子数至多
$k+r\le3m+2<2p$。故低部分指数的阶乘至多含一个 $p$，
并且 $p e^{\alpha T}$ 的全部所需系数整。

在先清除该一个 $p$ 后，Wilson 身份给
$$
\frac p{(p+s)!}\equiv-\frac1{s!}\pmod p
\quad(0\le s<p).                                          \tag{14}
$$
约化 $T$ 后，Frobenius 与 $t^p=0$ 给
$$
\overline T^{p}=u^p\pmod{u^{2p},t^4}.                     \tag{15}
$$
这里纯偶线性系数是
$W_1=-4/d_2=4/(4-h)\equiv1\pmod h$；
纯偶更高项的 $p$ 次幂从 $u^{2p}$ 起，所有正 $t$ 次项的 $p$ 次幂都为零。
式 (14) 的 $p$ 倍系数、(15) 以及 $\alpha^p=\alpha$ 给出
$$
\overline{p[t^ku^{p+j}]e^{\alpha T}}
=-\alpha[t^ku^j]e^{\alpha w},                              \tag{16}
$$
其中 $w$ 是 $T$ 在权重小于 $p$ 区域的约化，
右端只在 $k+2j<p$ 时使用，故指数的所有阶乘均为单位。
这里不将未整的高阶指数直接放入特征 $p$ 中。

从 $\widetilde W_p=0$ 开始，按高节点的权重递推，
(7) 和 $e^{\alpha\widetilde V}=e^{\alpha T}(1+\alpha R)$
证明 $pR$ 在本件区域整：在 $e^{\alpha T}R$ 中，背景指数的所需权重
小于 $p$，其系数整，且只涉及更早的高节点；所有相应除数都是单位。
令
$$
\tau(t,u)=\sum_{k+2j<p}\overline{p[t^ku^{p+j}]\widetilde V}\;t^ku^j,
\qquad [1]\tau=0.                                         \tag{17}
$$
式 (16) 与线性高带项给出完整而合法的身份
$$
\boxed{\overline{p[t^ku^{p+j}]e^{\alpha\widetilde V}}
=[t^ku^j]\alpha e^{\alpha w}(\tau-1),
\quad k\le3,\quad k+2j<p.}                                \tag{18}
$$
常数缺陷 $-1$ 来自完整阶乘带，不是把实际 $W_p$ 设为形式对数的 $1/p$。

### Step 5. 全部三次幅度响应的高带是同一缩放导数

低节点及高节点分别用
$d_{k+2j}\equiv-(k+2j)^2$ 和
$d_{2p+k+2j}\equiv-(k+2j)^2\pmod h$。
式 (7)、(18) 给
$$
\mathscr N^2 w=\frac t2e^w+4u e^{2w},\qquad
\mathscr N^2\tau=J(\tau-1),\qquad
J=\frac t2e^w+8u e^{2w},                                   \tag{19}
$$
在 $t^4=0$、权重小于 $p$ 的区域成立。
在零节点单独指定 $w(0,0)=\tau(0,0)=0$；没有除以 $d_0$。
对第一式作用 $\mathscr N$，逐项求导得到
$$
\mathscr N^3w=J(1+\mathscr Nw).                            \tag{20}
$$
所以 $-\mathscr Nw$ 满足第二式。除零节点外，每个对角元
$(k+2j)^2$ 的指标都在 $1,\ldots,p-1$，可逆；$J$ 无常数项。
单位三角唯一性遂给
$$
\boxed{\tau=-\mathscr Nw.}                                \tag{21}
$$
它包含 $W,A,C,E$ 的高带，而不只是奇一次响应。
将它代回 (18)，并使用
$\mathscr N e^{\alpha w}=\alpha e^{\alpha w}\mathscr Nw$，得
$$
\boxed{\overline{p[t^ku^{p+j}]e^{\alpha\widetilde V}}
=-[t^ku^j](\alpha+\mathscr N)e^{\alpha w}
=-(\alpha+k+2j)[t^ku^j]e^{\alpha w}.}                     \tag{22}
$$
上述求导只用于低于 $p$ 权重的指数，全部有限阶乘合法。

### Step 6. 两个次高端点均具有零缩放乘子

由 (13)，在以下端点可将 $\widetilde V$ 换回实际 $V$ 而不改变 $p$ 倍剩余。
第一端点在 (22) 中取
$$
\alpha=1,\quad k=2,\quad j=m-1,
\qquad \alpha+k+2j=1+2+2m-2=p.
$$
第二端点取
$$
\alpha=2,\quad k=3,\quad j=m-2,
\qquad \alpha+k+2j=2+3+2m-4=p.
$$
两个低权重分别为 $p-1,p-2$，都严格小于 $p$，完全落在 (22) 的合法区域。
由于 $m\ge2$，第二个 $j$ 非负；$p=5$ 时它恰为零，
相应低三次响应的对角元是 $3^2$，仍为单位，不需特殊素数扫描。
因此
$$
\overline{p[t^2u^{3m}]e^V}=0,\qquad
\overline{p[t^3u^{3m-1}]e^{2V}}=0.                         \tag{23}
$$
先前已证明这两个 $p$ 倍系数整。结合 (5)、(8) 与 $2,4$ 为单位，
得到
$$
p[L^{D-1}]\mathcal B_3\in h\mathcal O^+.
$$

### Step 7. 规范化单位及商转移的交叉项

由于 $v_h(p)=M$，记 $\epsilon=p/h^M\in(\mathcal O^+)^\times$。
因此由 Step 6 有
$$
\overline{h^{-M}p^2[L^{D-1}]\mathcal B_3}
=\overline{\epsilon\,p[L^{D-1}]\mathcal B_3}=0.             \tag{24}
$$
不能在非零问题中将 $\epsilon$ 擅自设为 $1$；本件因其所乘的剩余为零，
无需计算该单位的准确剩余。

首一分解在 $L^{D-1}=L^{m+p-1}$ 处只有两个配对：
$$
[L^{D-1}]S=u_{p-1}+b_{m-1}u_p.                            \tag{25}
$$
由 $b_{m-1}\in h\mathcal O^+$ 及已接受的最高项下界，交叉项满足
$$
v_h(b_{m-1}u_p)\ge e_*+m+2\ge e_*+1.                     \tag{26}
$$
故将 (25) 除以 $h^{e_*}$ 后约化，不保留任何交叉项；
又因 $D+e_*=M$，(24) 给出
$$
\gamma_{p-1}=\overline{h^{-e_*}u_{p-1}}
=\overline{h^{-M}p^2[L^{D-1}]\mathcal B_3}=0.
$$
于是式 (1) 全部成立。$\square$

## Corrections or Missing Assumptions

- 没有缩小一般量词或追加关于非零性的假设。
- $C,E$ 的规范在式 (4)—(6) 明示，避免把二、三阶导数和泰勒系数混用。
- 实际奇共振后响应不直接约化；式 (10)—(13) 先完成共振多项式的真实估值。
- 四个零共振初值只定义辅助分支；它们与实际分支的差以 $M-3m>0$ 明确控制。

## Open Risks and Scope

- 本件是作者证明，尚需针对本冻结新稿的非作者核查；作者间推导相合不计独审。
- $v_h(u_{p-1})\ge e_*+1$ 不代表该层非零，也不单独确定任何负 Newton 边。
- 本件只推次高首层，不宣称其余中间高系数具有相同消失，也不提高已接受最高项精度。
- 没有重开正簇、建立 Paper30 项目、编译论文、作 Route 评价或执行外部操作。
