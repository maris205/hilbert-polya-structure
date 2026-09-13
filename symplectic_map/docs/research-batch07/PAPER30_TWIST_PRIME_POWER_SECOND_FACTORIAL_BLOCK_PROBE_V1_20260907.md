# Paper 30：奇素数幂的第二条阶乘带与下一非内部模态块

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
本轮全文读取并使用 `proof-writer`。本件是作者证明，不是非作者独审票。

## Claim

固定任意奇素数 $p$、整数 $a\ge2$，令 $s=p^a$，$\zeta$ 为任意本原 $s$ 次单位根。
使用同一物理正 kick、固定参数与 SUM action，取

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad m=(p-1)/2,\qquad M=p^{a-1}m.
\tag{1}
$$

在实分圆局部域 $K^+=\mathbb Q_p(h)$ 的整数环 $\mathcal O^+=\mathbb Z_p[h]$ 中，
归一化 $v_h(h)=1$，故 $v_h(p)=M>2m$，剩余域为 $\mathbb F_p$。
对实际分支

$$
V_n(L)=\rho^nv_n(L/\rho),\qquad
d_n=\frac{D_n}{\rho}=-\frac{D_n}{h},\qquad D_n=2-\zeta^n-\zeta^{-n},
$$

本件证明以下完整参数多项式结论：

1. 下一入口满足

$$
\boxed{p^2V_{2p+1}\in\mathcal O^+[L],\qquad
\overline{p^2V_{2p+1}}=\frac1{16}.}
\tag{2}
$$

2. 整个有界非内部块 $1\le j<p$ 满足

$$
\boxed{p^2V_{2p+j}\in\mathcal O^+[L],\qquad
\sum_{j=1}^{p-1}\overline{p^2V_{2p+j}}x^j
=\frac{x}{16A(x)}+\frac{Lx^2}{8A(x)^2}\pmod{x^p},}
\tag{3}
$$

其中 $q=(1-4L)/16$、$A(x)=1-x/2+qx^2$。等价地，令

$$
T_0=2,\quad T_1=1/2,\quad
T_j=\frac12T_{j-1}-qT_{j-2}\quad(j\ge2),
$$

则

$$
\boxed{\overline{p^2V_{2p+j}}=\frac{jT_j}{8}
=-\frac j4\overline{pV_{p+j}}\quad(1\le j<p).}
\tag{4}
$$

3. 每个剩余多项式的 $L$ 次数为 $\lfloor j/2\rfloor$；每个实际 $V_{2p+j}$
的系数最小 $h$ 赋值恰为 $-2M$。这不是任意参数处所有模态都有同一极点阶的声明。
在有限局部扩域的任意代数整数参数 $L$ 处，若 $T_j(\bar L)\ne0$，
则 $v_h(V_{2p+j}(L))=-2M$；入口 $j=1$ 对全部这些参数均成立。

另记录只用本块指数系数的有限推论：令

$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},
\tag{5}
$$

其中只使用 $n<3p$ 的实际分支，则 $p^2\mathcal B_3\in h\mathcal O^+[L]$。
这只是普通首层取消，不确定其准确非零层，不构造或求解 $V_{3p}$。

## Status

式 (2)—(4)、限定赋值推论及式 (5) 的普通首层取消：`PROVABLE AS STATED`。

原入口结论没有缩弱，块扩展仍严格限定 $n<3p$。
没有宣称第三内部模态或完整共振的准确 forcing、完整 $C_{r,p^a}$、简单性、
全实根或 $C,Q$ 互素已经解决。

## Assumptions and Inputs

以已接受的
[第二内部层处置](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)
为范围记录，实际调用其绑定的
[上一非内部块作者稿](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md)
和[第二内部 forcing 作者稿](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md)。
本轮全文读取相关输入及其既有联合核查；旧接受结论不作为待重审任务。

| 输入 | SHA256 |
| --- | --- |
| SECOND_INTERNAL_DISPOSITION | `77069ed7697b42887d794871ecd0a2d51647d54527ce8c90bc4432cceee7debe` |
| POST_POLE_BLOCK V1 | `0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34` |
| SECOND_INTERNAL_FORCING V1 | `278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15` |

具体调用以下已接受事实：

$$
V_n\in\mathcal O^+[L]\ (1\le n<p),\qquad V_1=1/2,\qquad
h^mV_p\in\mathcal O^+[L],\qquad pV_p\in h^{M-m}\mathcal O^+[L],
\tag{6}
$$
$$
pV_n\in\mathcal O^+[L]\quad(p<n\le2p),\qquad
\overline{pV_{2p}}=-1/4,\qquad
\bar d_n=-n^2\quad(p\nmid n).
\tag{7}
$$

始终使用实际递推

$$
d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
\tag{8}
$$

还调用上一块完整剩余式

$$
Y(x):=\sum_{j=0}^{p-1}\overline{pV_{p+j}}x^j
=\frac{xA'}{2A}=-\frac12N_xU\pmod{x^p},\qquad Y(0)=0,
\tag{9}
$$

其中 $N_x=x\partial_x$、$U=-\log A$，以及低块在 $n<p$ 的系数上满足
$\bar P=U\pmod{x^p}$。对数先在特征零定义；没有在特征 $p$ 中使用越过 $p!$ 的无限指数。

## Notation

在特征零形式幂级数环中写

$$
P=\sum_{n=1}^{p-1}V_nx^n,\qquad
R_1=\sum_{n=p}^{2p-1}V_nx^n,\qquad
R_2=\sum_{n=2p}^{3p-1}V_nx^n.
\tag{10}
$$

递推时 $R_2$ 只取已经求出的前缀。指数的所有使用均限定到 $x^{3p}$ 以下。
设 $E_N=[x^N]e^P$；负下标系数定义为零。
横线只作用于已经证明逐系数整的表达式。
赋值下界用于多项式时是所有系数的共同下界。

## Proof Strategy and Dependency Map

1. 用旧内部模态的实际高度及两条阶乘带，先证明入口式 (2)，逐项保留 $V_p^2/2$。
2. 以次数恒等式保留旧高块的全部二次项，沿单位传播子三角递推证明式 (3) 的整性。
3. 分别计算低块第二阶乘带、旧高块乘第一阶乘带、新高块线性项、旧高块二次项的剩余。
4. 由完整有限指数桥得到唯一的有限 Jacobi 方程，用参数平移族的二阶变化求出有理解。
5. 从完整幂和多项式读取准确系数尺度；在不除以 $d_{3p}$ 的条件下记录 forcing 普通首层取消。

主控与本作者分别导出同一块候选式，并交换了有理身份核对；这属于共同推导，
不作为独立审查。以下一般阶乘论证与实际整性不依赖素数样本或参数根扫描。

## Proof

### Step 1. 先单独证明下一入口

因 $p\ge3$，有 $3p-1<p^2\le s$，包括 $p=3$ 时的严格边界 $3p-1=8<9$。
因此本块全部模态均严格低于完整共振次数。
对整数 $k<3p$，$v_p(k!)=\lfloor k/p\rfloor\le2$。
由 $P$ 整，低指数系数在次数小于 $p$ 时整，小于 $2p$ 时乘 $p$ 后整，
小于 $3p$ 时乘 $p^2$ 后整。

先看 $E_{2p}$。指数项 $k<2p$ 的阶乘至多含一个 $p$ 因子，
故其乘 $p^2$ 后的赋值至少为 $M$。
唯一尚可贡献普通剩余的 $k=2p$ 项使用
$[x^{2p}]P^{2p}=V_1^{2p}=2^{-2p}$。把 $(2p)!$ 的两个 $p$ 因子明确拆开，得

$$
\overline{\frac{p^2}{(2p)!}}
=\frac{1}{2\,((p-1)!)^2}=\frac12,
\qquad \overline{p^2E_{2p}}=\frac18.
\tag{11}
$$

这里 $(p-1)!=-1$ 在 $\mathbb F_p$ 中由非零元的逆元配对成立。
没有把仍有负赋值的 $E_{2p}$ 本身直接约化。

所有高模从 $x^p$ 起，所以在入口所需次数精确有

$$
[x^{2p}]e^V=E_{2p}+\sum_{r=p}^{2p}V_rE_{2p-r}+\frac12V_p^2.
\tag{12}
$$

各项乘 $p^2$ 后的系数赋值下界如下；第二 forcing 项也列在表中。

| 项 | 乘 $p^2$ 后的赋值下界或剩余 | 理由 |
| --- | --- | --- |
| $E_{2p}$ 中 $k=2p$ 的指数项 | 剩余 $1/8$ | 式 (11) 与 $V_1=1/2$ |
| $E_{2p}$ 中 $k<2p$ 的指数项 | 至少 $M$ | 阶乘至多含一个 $p$ |
| $V_pE_p$ | 至少 $M-m$ | $V_p$ 至少 $-m$，$E_p$ 至少 $-M$ |
| $V_rE_{2p-r}$，$p<r\le2p$ | 至少 $M$ | $V_r$ 至少 $-M$，另一系数次数小于 $p$ |
| $V_p^2/2$ | 至少 $2(M-m)$ | 两个实际 $V_p$ 均保留，且 $2$ 为单位 |
| $L[x^{2p-1}]e^{2V}$ | 至少 $M$ | 低块至多一条阶乘带，高块只线性出现并乘低于 $p$ 阶的系数 |

最后一行的线性项包含 $V_p$，其乘 $p^2$ 后高度至少 $2M-m>M$；
其他已知高模贡献至少 $M$。因此这行没有假定内部模式消失。
所有正下界都严格大于零，包括最小情形 $p=3,a=2$。

式 (8) 在 $n=2p+1$ 的传播子剩余是 $-1$，为单位。
右边乘 $p^2$ 后整，剩余为 $-(1/2)(1/8)=-1/16$，
故 $p^2V_{2p+1}$ 整且剩余 $1/16$，证明式 (2)。

### Step 2. 全块的三角整性与准确次数展开

在任意已求前缀中，特征零的准确有限次数身份为

$$
e^{\alpha(P+R_1+R_2)}
=e^{\alpha P}\left(1+\alpha R_1+\alpha R_2+\frac{\alpha^2}{2}R_1^2\right)
\pmod{x^{3p}},\qquad \alpha=1,2.
\tag{13}
$$

因为 $R_1R_2$、$R_1^3$ 均从次数 $3p$ 起，$R_2^2$ 从次数 $4p$ 起。
舍去这些项首先是特征零的次数操作；即使 $p=3$ 时 $3!$ 非单位，
它们仍不影响任何次数严格小于 $3p$ 的系数。
相反，$R_1^2$ 不能在一般块中舍去。

对 $N<3p$，把式 (13) 乘 $p^2$ 后分四类检查：

1. 低块 $p^2[x^N]e^{\alpha P}$ 整，来自 Step 1 的阶乘界。
2. 旧高块线性项中 $pR_1$ 整，余下次数 $N-r<2p$ 的指数系数乘 $p$ 后整。
3. 新高块线性项中已求的 $p^2R_2$ 整，余下指数次数 $N-r<p$，故无需乘 $p$ 即整。
4. 旧高块二次项是 $(pR_1)^2/2$ 乘以次数低于 $p$ 的整指数系数，因而整。

归纳初值 $p^2V_{2p}=p(pV_{2p})$ 由式 (7) 整，且普通剩余为零。
假设 $2p\le r<n=2p+j$ 的整性已证，则原递推只用指数次数 $n-1,n-2$，
不依赖未求的 $V_n$ 或更高模。上面四类检查使右边乘 $p^2$ 后整。
对 $1\le j<p$，$\bar d_n=-j^2\ne0$，除以单位即得 $p^2V_n$ 整。
归纳完成整个块；入口和已接受的 $V_{2p}$ 均没有被置零。

### Step 3. 第二条阶乘带的完整剩余

对 $k=2p+r$、$0\le r<p$，拆掉两个 $p$ 因子后得到

$$
\overline{\frac{p^2}{(2p+r)!}}
=\frac{1}{2\,((p-1)!)^2r!}=\frac1{2r!}.
\tag{14}
$$

对 $k<2p$，乘 $p^2$ 的指数项剩余为零。因此

$$
\overline{p^2e^{\alpha P}}
=\frac{\alpha^2}{2}\bar P^{2p}
\sum_{r=0}^{p-1}\frac{(\alpha\bar P)^r}{r!}
\pmod{x^{3p}}.
$$

Frobenius 给出 $\bar P^p=x^p/2+O(x^{2p})$，所以
$\bar P^{2p}=x^{2p}/4+O(x^{3p})$。
这里的 $\alpha^{2p}=\alpha^2$ 只用于整数 $\alpha=1,2$；
没有在参数多项式环中使用错误的 $L^p=L$。
乘去 $x^{2p}$ 后仅需小于 $p$ 的指数系数，由式 (9) 的低块输入得

$$
\boxed{\overline{p^2e^{\alpha P}}
=\frac{\alpha^2}{8}x^{2p}A^{-\alpha}\pmod{x^{3p}}.}
\tag{15}
$$

还需旧的第一条阶乘带。对 $k=p+r$、$0\le r<p$，
$\overline{p/(p+r)!}=-1/r!$，而 $\bar P^p=x^p/2\pmod{x^{2p}}$，故

$$
\overline{pe^{\alpha P}}
=-\frac\alpha2x^pA^{-\alpha}\pmod{x^{2p}}.
\tag{16}
$$

式 (16) 是已接受的旧带身份；写出它是为准确计算本轮的旧高模乘低阶乘带项，
并非把第一条带的整性外推到更高次数。

### Step 4. 四项合并的有限指数桥

整性完成后定义

$$
pR_1=x^p\mathcal Y(x),\qquad Y=\overline{\mathcal Y},\qquad
p^2R_2=x^{2p}\mathcal Z(x),\qquad Z=\overline{\mathcal Z},\qquad Z(0)=0.
\tag{17}
$$

$Y(0)=0$ 来自实际 $pV_p$ 的高度 $M-m>0$，
$Z(0)=0$ 来自 $pV_{2p}$ 整再乘一次 $p$。
它们只是这些已整表达式的剩余初值，不是删去真实内部模态。

在式 (13) 的四项中，低块由式 (15) 贡献
$x^{2p}A^{-\alpha}\alpha^2/8$。
旧高块线性项先写为 $\alpha(pR_1)(pe^{\alpha P})$，
因余下次数低于 $2p$，式 (16) 给出贡献
$-x^{2p}A^{-\alpha}\alpha^2Y/2$。
新高块线性项贡献 $x^{2p}A^{-\alpha}\alpha Z$；
旧高块二次项贡献 $x^{2p}A^{-\alpha}\alpha^2Y^2/2$。
后两项所需低指数次数均低于 $p$，所以它们的约化合法。
合并得对 $0\le N<3p$ 的完整系数身份

$$
\boxed{
\overline{p^2[x^N]e^{\alpha V}}
=[x^{N-2p}]A^{-\alpha}
\left(\alpha Z+\frac{\alpha^2}{2}(Y-1/2)^2\right),\qquad \alpha=1,2.}
\tag{18}
$$

虽然入口的 $V_p^2/2$ 剩余为零，整个旧高块的平方却不能删去：
$Y^2$ 从 $x^2$ 起，在式 (18) 覆盖的次数中产生同尺度贡献。
对 $p=3$，它首次作用于本块之后式 (5) 所用的指数系数；对 $p\ge5$，
它也已作用于本块自身的后续 forcing。
常数 $1/8$、交叉项 $-Y/2$、二次项 $Y^2/2$ 来自三种不同项，
必须一起保留才形成式 (18) 中的平方。

### Step 5. 有限 Jacobi 方程及其有理解

令

$$
\mathcal J=\frac{x}{2A}+\frac{2Lx^2}{A^2},\qquad
\mathcal K=\frac{x}{4A}+\frac{2Lx^2}{A^2},\qquad B=Y-1/2.
$$

式 (8) 对 $n=2p+j$ 乘 $p^2$ 后取模，$\bar d_n=-j^2$ 与右侧总负号相消。
代入式 (18) 即得

$$
\boxed{N_x^2Z=\mathcal JZ+\mathcal K B^2\pmod{x^p},\qquad Z(0)=0.}
\tag{19}
$$

这里 $\mathcal J(0)=\mathcal K(0)=0$，且 $j^2$ 在 $1\le j<p$ 可逆；
第 $j$ 个系数只使用此前的 $Z$ 系数，故所需有限解唯一。
没有把这一唯一性延伸到不可逆的 $j=p$。

为求解，先在特征零中使用 $U=-\log A$ 的准确身份

$$
N_x^2U=\frac{x}{2}e^U+Lx^2e^{2U}
=\frac{x}{2A}+\frac{Lx^2}{A^2}.
\tag{20}
$$

此式代入 $A=1-x/2+qx^2$ 与 $16q=1-4L$ 即可直接验证。
令 $\varepsilon$ 为独立特征零形式变量，取平移缩放族
$U_\varepsilon(x)=\varepsilon+U(e^\varepsilon x)$。
式 (20) 对该族仍成立，因为每个 $x^ke^{kU}$ 都变成
$(e^\varepsilon x)^ke^{kU(e^\varepsilon x)}$。
设

$$
G=\left.\partial_\varepsilon U_\varepsilon\right|_0=1+N_xU,
\qquad H=\left.\partial_\varepsilon^2U_\varepsilon\right|_0=N_x^2U.
$$

对方程求两次 $\varepsilon$ 导数，链式法则分别给出
$\partial_\varepsilon^2e^{U_\varepsilon}|_0=e^U(H+G^2)$ 和
$\partial_\varepsilon^2e^{2U_\varepsilon}|_0=e^{2U}(2H+4G^2)$，因此

$$
(N_x^2-\mathcal J)H
=\left(\frac{x}{2A}+\frac{4Lx^2}{A^2}\right)G^2.
\tag{21}
$$

式 (9) 给 $B=-G/2\pmod{x^p}$。将式 (21) 除以 $8$，右边恰为
$\mathcal K B^2$，所以候选解为

$$
Z_*:=\frac18N_x^2U
=\frac{x}{16A}+\frac{Lx^2}{8A^2}
=-\frac14N_x\left(\frac{xA'}{2A}\right).
\tag{22}
$$

式 (21)—(22) 是未截断的有理身份；所涉 $G,H,Z_*$ 的分母只是
$2$ 的幂与常数项为 $1$ 的 $A$ 的幂。因此这些有理级数在所有奇素数下逐系数整，
可以约化后取任意有限次数，不需要把特征零的无限对数或 $e^\varepsilon$ 在模 $p$ 中定义。
$Z_*(0)=0$；由式 (19) 的有限唯一性，$Z=Z_*\pmod{x^p}$。
这证明式 (3)，且其一次系数重新给出 $1/16$。

### Step 6. 完整参数多项式、准确尺度与参数边界

上一块的幂和身份为 $[x^j]Y=-T_j/2$。式 (22) 给
$[x^j]Z=-j[x^j]Y/4=jT_j/8$，证明式 (4)。
这在 $\mathbb F_p[L]$ 内成立，不需要选择二次根、不除以参数多项式，
故 $L=0$、$q=0$ 以及旧内部 forcing 的根类都无需排除。

上一块已接受的最高系数是
$[L^k]\overline{pV_{p+2k}}=-4^{-k}$ 和
$[L^k]\overline{pV_{p+2k+1}}=-(2k+1)4^{-k-1}$。
乘以式 (4) 的 $-j/4$ 得本轮最高系数

$$
[L^k]\overline{p^2V_{2p+2k}}=\frac{2k}{4^{k+1}},\qquad
[L^k]\overline{p^2V_{2p+2k+1}}=\frac{(2k+1)^2}{4^{k+2}}.
\tag{23}
$$

在相应的 $1\le j<p$ 范围，分子非零且分母为单位，
所以每个剩余多项式次数恰为 $\lfloor j/2\rfloor$。
$p^2V_{2p+j}$ 至少有一个单位系数且全部系数整，
从而实际 $V_{2p+j}$ 的系数最小赋值恰为 $-2M$。
这里只确定剩余多项式的次数；实际多项式允许有更高次但被 $h$ 整除的系数。

对有限局部扩域中的整参数，把整多项式代入后仍整，
剩余不为零时是单位，故得到 Claim 中的条件赋值结论。
如果 $T_j(\bar L)=0$，本稿不把该参数处的赋值也写成 $-2M$。
$j=1$ 的剩余为常数单位 $1/16$，所以入口没有这项限制。
全块主张证明完成。$\square$

### Step 7. 不求解端点的有限 forcing 推论

式 (18) 已覆盖 $N=3p-1,3p-2$，所以式 (5) 乘 $p^2$ 后整，且

$$
\overline{p^2\mathcal B_3}
=-2[x^p]\left(\mathcal JZ+\mathcal K B^2\right).
\tag{24}
$$

由于 $\mathcal J$ 无常数项且 $\mathcal K$ 无常数项，
右边只用 $Z,Y$ 的次数小于 $p$ 的已知系数。
故可将它们替换成完整的有理式 $Z_*$ 与 $xA'/(2A)$。
式 (21)—(22) 的有理身份使右边等于 $-2[x^p]N_x^2Z_*$。
$Z_*$ 的第 $p$ 个系数在 $\mathbb Z_{(p)}[L]$ 中整，而 $N_x^2$ 在该次数乘 $p^2$，
所以其模 $p$ 剩余为零。因此

$$
\boxed{p^2\mathcal B_3\in h\mathcal O^+[L].}
\tag{25}
$$

此证明不除以 $d_{3p}$，不定义 $V_{3p}$，也不证明式 (25) 中 $h$ 的准确次数。
特别是 $p=3,a=2$ 时 $3p=s=9$ 已是全系统共振，
forcing 仍由前缀定义而该共振模态不能按非共振单位递推求解。

## Exact Verification Actually Run

使用自由符号 $x,L$，设 $q=(1-4L)/16$、$A=1-x/2+qx^2$，
$Y_*=xA'/(2A)$，$Z_*=x/(16A)+Lx^2/(8A^2)$。
实际运行的精确符号检查计算了

$$
N_x^2Z_*-\mathcal JZ_*-\mathcal K(Y_*-1/2)^2,\qquad
Z_*+N_xY_*/4,\qquad Z_*'(0)-1/16.
$$

通分后的三个残差均严格为零。实际输出：
`EXACT_PASS second-factorial Jacobi / derivative / first-entry identities; residuals = [0, 0, 0]`。
这只核对自由有理身份，不代替一般素数阶乘带、三角整性或实际赋值证明。
没有输入素数列表、原始分母列表、本原根列表或参数根列表。

## Corrections or Missing Assumptions

- 无需附加一般位置参数假设；本件整性和首层是完整参数多项式身份。
- 两条阶乘带分别负责 $1/8$ 和 $-Y/2$，旧高块二次项负责 $Y^2/2$，均未遗漏。
- $pV_p$ 和 $pV_{2p}$ 的真实高度只在整性和约化后用于剩余消失，没有修改实际分支。
- $p=3$ 时 $3p=p^2$，故所有阶乘界均坚持严格次数 $N<3p$；没有处理 $(3p)!$。
- 传播子始终使用 $d_n=-D_n/h$，单位方程的总符号与入口 $1/16$ 一致。

## Open Risks and Delivery Boundary

- 式 (25) 只证明第三 forcing 的普通首层取消，不给出准确非零层或可用的端点正规化。
  要研究该层，必须重新控制实际传播子修正及旧内部模式的有限高度，
  不能把本稿剩余方程当作实际等式使用。
- $3p$ 不属于本稿的非共振模态定理；对 $p=3,a=2$，它是完整共振而不是第三个普通内部模态。
- 不据此推出更高块、完整 $C_{r,p^a}$、其与 $Q$ 的关系、简单性或全部参数根全实。
- 新旧共享的候选推导、主控交叉计算与本作者符号核对均不算独立审查，仍待绑定本稿的非作者核查。
- 本轮只新写此作者稿；旧稿、既有处置、冻结输入、锁和脚本均未改。
  未作正文估页、立项、PDF、Route 评价、外部写入或付费资源操作。
