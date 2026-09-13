# Paper 30：偶数分母半阶消元与两倍奇素数的首项约化

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
本轮完整读取 `proof-writer` 技能后撰写的新结构证明；不是独立核查票。

## Claim

本件证明两项准确的结构命题。

第一项适用于全部偶数分母 $s=2M\ge4$：
首项可以用严格低于半阶的分支、一个中央模式平方项及两项有限指数系数精确表示，
见式 (4)。这不是自动闭合在低分母 $C_{r,M}$ 上的递推。

第二项针对真实无限合数族 $s=2p$。
固定任意奇素数 $p$ 和任意 $\gcd(r,2p)=1$，
令

$$
\zeta=e^{2\pi ir/(2p)},\qquad
h=D_2=2-\zeta^2-\zeta^{-2},\qquad
m=\frac{p-1}{2},\qquad \kappa=\lambda-\frac1{16}.
$$

在完成实圆分局部整数环 $\mathcal O^+=\mathbb Z_p[h]$ 中，实际首项满足

$$
\boxed{
S_{2p}(\lambda):=\frac{h^{p-1}}p C_{r,2p}(\lambda)\in\mathcal O^+[\lambda],
\qquad
\overline{S_{2p}}(\lambda)=2\kappa^p+\frac14\kappa^m
=2\kappa^m\left(\kappa^{m+1}+\frac18\right).}
\tag{1}
$$

这里的上横线是 $\mathcal O^+/(h)=\mathbb F_p$ 中的系数约化；
$h$ 在本件明确是 $D_2$，不是此前奇素数分母稿的 $D_1$。
式 (1) 在 $\kappa=0$ 同样是多项式身份，没有除以 $\kappa$。

由此 $\deg C_{r,2p}=p$。
在局部代数闭包中，恰有 $m$ 个根按重数计落在
$\lambda\equiv1/16$ 的剩余类中；
其余 $m+1=(p+1)/2$ 个根全部简单，分别对应
$\kappa^{m+1}=-1/8$ 的互异非零剩余根。
此外，在特征零系数域中

$$
\boxed{\deg\gcd(C_{r,2p},C'_{r,2p})\le m-1=\frac{p-3}{2}.}
\tag{2}
$$

非零剩余根在 $\overline{\mathbb F}_p$ 中理解，不声称它们全部属于 $\mathbb F_p$。
本结论不是全部根实性或全部两倍素数首项平方自由性定理。

## Status

上述半阶消元、式 (1) 和部分简单性命题：`PROVABLE AS STATED`。

对所有合数分母的完全平方自由性、全部根实性及
$\gcd(C_{r,s},Q_{r,s})=1$：本件 `NOT CURRENTLY JUSTIFIED`。
在 $s=2p$ 中仍未解决的重根只可能位于式 (1) 的 $\kappa=0$ 根簇；
本件没有用更高阶 $Q$ 计算代替这一边界。

## Assumptions and Notation

沿用同一双谐波映射、固定 $\lambda$、正 kick 和不除以分母的 SUM action。
真实传播子及物理正频支为

$$
D_n=2-\zeta^n-\zeta^{-n},\qquad
v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n}\quad(1\le n<s),
$$
$$
E=e^v,\qquad F=e^{2v},\qquad
C_{r,s}=-E_{s-1}-2\lambda F_{s-2}.
\tag{3}
$$

负下标系数为零，不在 $D_s=0$ 处作除法。
首项只需 $v_1,\ldots,v_{s-1}$。
相关递推、有限 action 身份及作用量规范见
[首项结构稿](PAPER30_TWIST_LEADING_STRUCTURE_PROBE_V1_20260907.md)
和[已接受的系数变分处置](PAPER30_TWIST_SINGLE_INSERTION_VARIATIONAL_GERM_DISPOSITION_20260907.md)。
两文的历史 OPEN 记录不覆盖后续已接受定理。

已全文读取
[全奇素数非消失处置](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)；
其中已接受的奇素数首项简单性及 $C,Q$ 互素性在本件不重审。

全部局部缩放仅分析同一个固定参数多项式，不把 $\lambda$ 改为随振幅调整。
$1/16$ 的来源是下文真实传播子的局部消元，不来自某个可积截断的移植。

## Proof Strategy and Dependency Map

1. 对全部偶数 $s$，用有限 action 的反射对称消去高半部，保留中央平方项。
2. 对 $s=2p$，取 $\xi=-\zeta$、$\pi=\xi-1$；
   奇模式传播子为单位，偶模式传播子恰含 $\pi^2$。
3. 缩放 $t=\pi x$，严格低于 $p$ 阶的偶部整、奇部是 $\pi$ 的倍数；
   它们的一层约化有显式平方传播子解。
4. 半阶 action 仍取到 $2p-1$ 阶的指数系数。
   显式保留其中的 $p!$ 层，证明整性并得到额外 Frobenius 项。
5. 一个有限截断指数恒等式给出全部素数一致的式 (1)。
6. 次数保持、约化 gcd 和简单根 Hensel 提升给出式 (2) 及根簇计数。

第 4 步不能省略：低阶分支只用 $p$-单位阶乘，不意味着其高阶指数系数也如此。

## Proof

### Step 1. 全偶数分母的精确半阶消元

先令 $s=2M$。真实半周期关系是

$$
D_{2M-n}=D_n,\qquad D_M=4,\qquad D_{n+M}=4-D_n.
$$

这是因为 $\gcd(r,2M)=1$ 使 $r$ 为奇数，从而 $\zeta^M=-1$。
定义严格低于半阶的截断

$$
P(t)=\sum_{n=1}^{M-1}v_nt^n,\qquad
T_M=\frac12[t^{M-1}]e^P+\lambda[t^{M-2}]e^{2P}.
$$

则有精确恒等式

$$
\boxed{
C_{r,2M}
=-2M[t^{2M-1}]e^P
-2M\lambda[t^{2M-2}]e^{2P}
+\frac{2M}{D_M}T_M^2,\qquad D_M=4.}
\tag{4}
$$

证明使用物理有限泛函

$$
\Phi_{2M}(v)=[t^{2M}]
\left(\frac12v\mathcal Dv+\frac12te^v
+\frac\lambda2t^2e^{2v}\right),\qquad
\mathcal D(t^n)=D_nt^n.
$$

反射 $D_{2M-n}=D_n$ 保证其临界方程恰为式 (3)。
临界值记为 $G$。临时把一步幅度写为 $b$，
对权重 $1,2$ 的 $(b,\lambda)$ 应用有限加权 Euler 身份，
有 $2MG=E_{2M-1}/2+\lambda F_{2M-2}=-C_{r,2M}/2$，
所以 $C_{r,2M}=-4MG$。

把分支写为 $P+v_Mt^M+\sum_{j>M}v_jt^j$。
每个高半部变量 $v_j$ 只线性出现：
它的系数等于相应低阶驻值方程
$D_{2M-j}v_{2M-j}+E_{2M-j-1}/2+\lambda F_{2M-j-2}=0$，
故高半部全部消去。
中央变量的贡献是
$D_Mv_M^2/2+T_Mv_M$，
取 $v_M=-T_M/D_M$ 后变为 $-T_M^2/(2D_M)$。
低部的动能最高次数为 $2M-2$，不贡献所需系数。
因此

$$
G=\frac12[t^{2M-1}]e^P+\frac\lambda2[t^{2M-2}]e^{2P}
-\frac{T_M^2}{2D_M},
$$

这证明式 (4)。
该式不要求把 $D_{n+M}=4-D_n$ 转化成未经证明的非线性对称性。
也不能将其中的 $T_M$ 称为低分母 $C_{r,M}$：
一般 $D_n(2M)\ne D_n(M)$，两者的低阶分支不同。

### Step 2. 两倍奇素数的两个传播子层

以下令 $M=p$、$p$ 为奇素数，并定义

$$
\xi=-\zeta,\qquad \pi=\xi-1,\qquad
\mathcal O=\mathbb Z_p[\xi].
$$

$\xi$ 是原始 $p$ 次单位根；
$\mathcal O$ 是完成局部整数环，剩余域为 $\mathbb F_p$，
$v_\pi(p)=p-1$。
当 $1\le n<p$ 时，

$$
D_n=
\begin{cases}
2-\xi^n-\xi^{-n},&n\text{ 为偶数},\\
2+\xi^n+\xi^{-n},&n\text{ 为奇数}.
\end{cases}
$$

因此

$$
\frac{D_n}{\pi^2}\equiv-n^2\pmod\pi
\quad(n\text{ 为偶数}),\qquad
D_n\equiv4\pmod\pi
\quad(n\text{ 为奇数}).
\tag{5}
$$

在所用范围内，偶数 $n$ 不被 $p$ 整除，所以两式的右端都是单位。
中央值 $D_p=4$ 保持精确，不将它误当成内部小除数。

取实参数

$$
h=D_2=2-\xi^2-\xi^{-2}.
$$

因 $\xi^2$ 同样原始，$h$ 是完成实子环
$\mathcal O^+=\mathbb Z_p[h]$ 的均匀化元，
$v_h(p)=m$、$v_\pi(h)=2$，并且

$$
h/\pi^2\equiv-4\pmod\pi.
\tag{6}
$$

这些身份与 $r$ 的选择无关；$r$ 只改变所取原始根及局部嵌入。
两实剩余域的正确关系是
$\mathcal O^+/(h)=\mathbb F_p$ 与 $\mathcal O/(\pi)=\mathbb F_p$，
不把 $\mathcal O/(h)$ 当作域。

### Step 3. 低半部的整性和显式约化

缩放 $t=\pi x$，记

$$
\widehat P(x)=\sum_{n=1}^{p-1}\pi^n v_nx^n=A(x)+\pi B(x),
$$

其中 $A$ 仅含偶数次幂，$B$ 仅含奇数次幂。
由式 (3)、(5) 三角归纳得到

$$
A,B\in\mathcal O[\lambda][x].
\tag{7}
$$

详细的估值归纳是：所有已求低阶系数整，
奇部已知含 $\pi$，而此范围的指数系数只使用 $k!$、$k<p$。
偶模式方程的第一驱动项是 $\pi$ 乘指数奇部，至少含 $\pi^2$；
第二驱动项本来含 $\pi^2$。
除以偶模式的 $D_n$ 后仍整。
奇模式方程的两项至少分别含 $\pi,\pi^3$，
除以奇模式单位传播子后仍是 $\pi$ 的倍数。
从 $n=1$ 开始，这就完成归纳。

令 $w=x^2$，上横线在本节表示模 $\pi$。
奇模式约化先给出

$$
\bar B=-\frac x8e^{\bar A}\pmod{x^p}.
$$

再代入偶模式方程，得到

$$
(x\partial_x)^2\bar A
=\kappa x^2e^{2\bar A}\pmod{x^p},\qquad
\kappa=\lambda-\frac1{16}.
$$

这里 $1/16$ 正是奇模式消去产生的项。
设 $q=\kappa/4$。直接代入及三角唯一性给出

$$
\boxed{
\bar A=\sum_{j=1}^{m}\frac{q^j w^j}{j},\qquad
\bar B=-\frac x8\sum_{j=0}^{m-1}q^j w^j.}
\tag{8}
$$

第一式是 $-\log(1-qw)$ 低于 $x^p$ 的有限截断；
所有分母 $j$ 都是 $p$-单位。
若记 $\mathcal E(w)=e^{\bar A}$，
则 $\mathcal E_j=q^j$ 对 $0\le j\le m$ 成立。
较高的 $\mathcal E_j$ 仍由有限截断 $\bar A$ 定义，
不可直接替换成完整有理函数的系数。

### Step 4. 精确保留 $p!$ 层

缩放后的半阶临界值为

$$
\widehat G:=\pi^{2p}G
=\frac\pi2[x^{2p-1}]e^{\widehat P}
+\frac{\lambda\pi^2}2[x^{2p-2}]e^{2\widehat P}
-\frac{\widehat T^2}{8},
$$
$$
\widehat T=\frac\pi2[x^{p-1}]e^{\widehat P}
+\lambda\pi^2[x^{p-2}]e^{2\widehat P}.
\tag{9}
$$

在式 (9) 中 $e^A$ 及 $e^{2A}$ 所需偶数系数最多为 $2p-2$ 阶。
由于 $A$ 始于二次，它们只使用小于 $p$ 的阶乘，因此整。
但 $e^{\pi B}$ 的奇部必须展开到 $2p-1$ 阶，
其中不能删去 $k=p$ 的项。

对 $1\le k\le2p-1$，

$$
v_\pi(\pi^k/k!)=
\begin{cases}
k,&k<p,\\
k-(p-1),&p\le k\le2p-1.
\end{cases}
$$

在奇数 $k$ 中，恰有 $k=1,p$ 具有赋值 $1$；
其余奇数 $k$ 的赋值至少为 $3$。
此外，

$$
\tau:=\frac{\pi^{p-1}}{p!}\equiv1\pmod\pi.
\tag{10}
$$

为核对符号，用
$p=\prod_{j=1}^{p-1}(1-\xi^j)$ 得
$p/\pi^{p-1}\equiv(p-1)!\equiv-1$；
后一个等式由有限域非零元素与逆元配对得到。
于是 $\pi^{p-1}/p\equiv-1$ 与 $1/(p-1)!\equiv-1$ 相乘给出式 (10)。

所以在所需奇系数范围，

$$
\frac{(e^{\widehat P})_{\rm odd}}{\pi}
\equiv e^{\bar A}(\bar B+\bar B^p)\pmod\pi,
\tag{11}
$$

而所需 $e^{2\widehat P}$ 偶系数整且模 $\pi$ 等于 $e^{2\bar A}$。
式 (11) 的 $\bar B^p$ 是真实阶乘贡献，不是自由添加的经验修正。
结合式 (9)，这已经证明
$\widehat G/\pi^2\in\mathcal O[\lambda]$。

### Step 5. 计算局部 primitive

记 $\mathcal F=e^{2\bar A}=\mathcal E^2$，
下标表示 $w$ 系数。
由式 (8)、(9)，

$$
\overline{\widehat T/\pi}=\frac12q^m.
$$

式 (11) 中普通奇部的贡献为

$$
\frac12[x^{2p-1}]\mathcal E\,\bar B
=-\frac1{16}\sum_{j=0}^{m-1}q^j\mathcal E_{2m-j}.
$$

而中央平方项的约化为 $-q^{2m}/32$。
有限卷积精确给出

$$
\mathcal F_{2m}
=2\sum_{j=0}^{m-1}q^j\mathcal E_{2m-j}+q^{2m},
$$

所以这两项之和等于 $-\mathcal F_{2m}/32$。

Frobenius 项只保留 $\bar B$ 的一次系数：
在模 $x^{2p}$ 的范围，
$\bar B^p=-x^p/8$，
因为其他奇幂经 $p$ 次方至少为 $x^{3p}$。
因此

$$
\frac12[x^{2p-1}]\mathcal E\,\bar B^p=-\frac{q^m}{16}.
$$

合并第二谐波势项后，得到

$$
\overline{\widehat G/\pi^2}
=\frac\kappa2\mathcal F_{p-1}-\frac{q^m}{16}.
\tag{12}
$$

现在只需一个有限截断身份：

$$
\boxed{\mathcal F_{p-1}=-q^{p-1}\quad\text{于 }\mathbb F_p[q].}
\tag{13}
$$

证明时将完整低于 $w^p$ 的对数分为前半与后半，
全部指数均只取低于 $p$ 阶的合法系数。由于后半最低次数为 $m+1$，
其平方最低次数为 $p+1$，故

$$
e^{2\bar A}\equiv
(1-qw)^{-2}
\left(1-2\sum_{j=m+1}^{p-1}\frac{q^jw^j}{j}\right)
\pmod{w^p}.
$$

右侧前一因子的 $w^{p-1}$ 系数为 $p q^{p-1}=0$。
相乘后的修正系数为

$$
-2q^{p-1}\sum_{j=m+1}^{p-1}\frac{p-j}{j}
=2m q^{p-1}=-q^{p-1},
$$

得到式 (13)。

由 $\kappa=4q$，式 (12) 化为

$$
\overline{\widehat G/\pi^2}
=-2q^p-\frac{q^m}{16}.
$$

另一方面，$C_{r,2p}=-4pG$ 给出

$$
S^\pi_{2p}:=\frac{\pi^{2p-2}}p C_{r,2p}
=-4\frac{\widehat G}{\pi^2}\in\mathcal O[\lambda],
$$
$$
\overline{S^\pi_{2p}}=8q^p+\frac14q^m
=2\kappa^p+\frac14\kappa^m.
\tag{14}
$$

最后 $S_{2p}=(h/\pi^2)^{p-1}S^\pi_{2p}$。
该倍因子为单位，且由式 (6) 与
$(-4)^{p-1}=1$，其约化等于 $1$。
$S_{2p}$ 的系数属于实子域，在 $\mathcal O$ 中整就属于 $\mathcal O^+$，
所以式 (14) 正是式 (1)。证明覆盖全部奇素数及全部互素分子。

### Step 6. 根簇与部分简单性

权重归纳先给出 $\deg C_{r,2p}\le p$；
式 (1) 的最高次系数为单位 $2$，
所以次数恰为 $p$，约化没有丢失次数。

在 $\overline{\mathbb F}_p$ 中，
$\kappa^{m+1}+1/8$ 有 $m+1$ 个互异非零根：
其导数是 $(m+1)\kappa^m$，且 $m+1=(p+1)/2$ 在特征 $p$ 非零。
这些根都与 $\kappa=0$ 分离。
在使这些剩余根分裂的有限非分歧局部扩域中应用简单根 Hensel 引理，
每个非零剩余根提升为一个唯一的简单特征零根。
互素因子版 Hensel 提升同时给出次数为 $m$ 的剩余根簇因子。
因此按重数计恰有 $m$ 个根位于 $\kappa\equiv0$，
外部 $m+1$ 个根全部简单。

也可直接核对

$$
\overline{S'_{2p}}=\frac m4\kappa^{m-1},\qquad
\gcd(\overline{S_{2p}},\overline{S'_{2p}})
=\kappa^{m-1}.
$$

约化 gcd 次数界或上述互素 Hensel 分解均给出式 (2)。
这些结论在局部域中证明后，仍约束原特征零数域中的 gcd；
扩域不会改变 gcd 的次数。
当 $p=3$ 时 $m=1$，式 (2) 已给出两倍三分母的完全平方自由性，
这只是一般公式的边界后果，不是由单例推断一般式。$\square$

### 窄推论：外部剩余根及局部因子的次数

以下推论由主控独立提出，作者在本稿中逐项复核。
若 $\alpha^{m+1}=-1/8$，则

$$
\alpha^{p+1}=\frac1{64},\qquad
\alpha^p=\frac1{64\alpha},\qquad
\alpha^{p^2}=\alpha.
$$

所以全部外部剩余根属于 $\mathbb F_{p^2}$，
Frobenius 在它们上作用为 $\alpha\mapsto1/(64\alpha)$。
其轨道长度只能为 $1$ 或 $2$。
因此外部因子在完成局部域 $\mathbb Q_p(h)$ 上的不可约因子次数只能为 $1$ 或 $2$；
这是剩余域因子唯一 Hensel 提升的局部结论，
不声称原全局数域中已有相同次数的因式分解。

固定点必须满足 $\alpha^2=1/64$，故只可能是 $\alpha=\pm1/8$。
令 $\chi_p(a)=(a/p)$ 表示 Legendre 符号。
直接代入 $m=(p-1)/2$，得到

$$
+1/8\text{ 是外部剩余根}\iff\chi_p(2)=-1,\qquad
-1/8\text{ 是外部剩余根}\iff\chi_p(-2)=1.
$$

这里用到的只是 $a^m=\chi_p(a)$，不需二次互反律。
这些数是 $\kappa$ 的剩余值，不是实际复嵌入下的 $\lambda$ 根坐标或实根证明。

## Exact Verification Actually Run

本件运行两项与新增身份直接相关的精确检查：

1. 令 $s=6$ 的反射传播子为自由符号
   $(D_1,D_2,D_3,D_4,D_5)=(A,B,H,B,A)$。
   用式 (3) 独立计算完整首项，与式 (4) 的半阶表达式相减，
   在 $\mathbb Q(A,B,H,\lambda)$ 中残差严格为零。
   $A,B,H$ 未代成具体三角值，此项检查的是新的普遍消元身份。
2. 只复用已有、未重算递推的
   [六分母精确首项](PAPER30_TWIST_ONE_INSERTION_INDEPENDENT_CHECK_20260907.md)
   $C_{1,6}=-4\lambda^3/3+39\lambda^2/8-127\lambda/96+99/2560$，
   检验本次新约化式。
   此时 $h=D_2=3$，精确得到
   $3C_{1,6}\bmod3=-\lambda^3+\lambda$，
   与 $2(\lambda-1/16)^3+(\lambda-1/16)/4$ 完全相同。

输出分别为
`GENERAL_REFLECTION_s6_HALF_ACTION_IDENTITY_PASS`
和 `EXISTING_C6_NEW_PRIMITIVE_RESIDUE_PASS`。
没有浮点根、素数列表、根扫描或旧诊断重跑；
一般证明由 Step 1–6 承担，有限检查不承担外推。

## Corrections or Missing Assumptions

一个自然但错误的首层猜测是只有 $2\kappa^p$，从而全部根聚在
$\lambda\equiv1/16$。
它漏掉了式 (11) 的 $p!$ 项。
正确结果多出 $\kappa^m/4$，因此只有 $m$ 个根按重数计留在该簇，
并非全部 $p$ 个根。
即使半阶分支只含低于 $p$ 的模式，也不能删除这一高阶指数贡献。

式 (4) 同样不证明
$C_{r,2M}$ 是低分母首项的平方或简单乘积。
半周期传播子身份是线性谱身份；非线性指数递推经消元后仍有两项独立的有限系数，
不能只保留中央平方项。

## Open Risks and Delivery Boundary

- 对 $p\ge5$，$\kappa=0$ 根簇的 $m$ 个特征零根仍需更精细分析；
  本件不声称它们重合，也不声称它们全部简单。
- 一般偶数但非两倍奇素数的分母，目前只得到式 (4)，
  没有将式 (1) 不加条件地推广。
- 本件未分析 $Q$ 的更高指数层，不推出偶数分母的 $C,Q$ 互素性。
- 全部根实性仍是另一个问题；局部算术分裂不等于复嵌入下实根。
- 作者证明须由非作者独立核查。仅新增本文件，
  不改旧稿、锁、状态入口、脚本、已接受结论或论文验收状态。
- 不进行 Route 评价、试写测页、论文立项、对外上传或其他系统族拼接。
