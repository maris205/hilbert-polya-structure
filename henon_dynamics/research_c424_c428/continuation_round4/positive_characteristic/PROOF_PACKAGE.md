# ROUND4-PC424-L：全局正则性尝试与迹配对的精确盲区

2026-09-08 UTC（按实际执行时钟校正日期）。原问题见 [冻结合同](FROZEN_CONTRACTS.md)。
本轮为手证明和来源适用性核查，数学程序执行零次。

## Claim

对每个奇素数 $p$、$k=\overline{\mathbb F}_p$、每个 $c\in k$ 和
$h\in k[x]$，令 $f_c=x^2+c$。是否有

$$
\biggl[\sum_{a\in O}h(a)=0\text{ 对每个普通几何本原周期轨道 }O\biggr]
\quad\Longleftrightarrow\quad
h=Q\circ f_c-Q\text{，其中某个 }Q\in k[x]?
$$

若不成立，原合同需要完整统一的缺陷空间 $K_c/B_c$ 分类或完整障碍机制。
所有参数、次数、普通点、原生时钟及周期量词均未改变。

## Status

**NOT CURRENTLY JUSTIFIED：原完整问题仍未闭合。**

本轮未得到第三轮所需的新素周期高接触全局上界。进一步尝试用循环
完全交代数的 Jacobian、乘法迹或非退化留数对偶绕过最大重数，得到
下面的精确诊断：普通迹恰好遗漏所有局部长度被 $p$ 整除的整个因子；
在新的本原素周期块上，加入全部循环移位的扭曲迹也不消除这一盲区。
留数对偶虽然非退化，却不把“普通点处为零”送到零泛函。

这些是经典有限代数事实在当前缺口上的完整适配，**不是独立论文级
合同，不是完整族 no-go，也不证明原等式为假**。不以来源筛选或辅助
引理填补准入名额。第二个问题未开启。

## Assumptions and notation

除非某条辅助引理另有说明，始终采用原 $p,k,c$。令

$$
F_n=f_c^{\circ n}-x,\quad A_n=k[x]/(F_n),\quad
H_n(h)=\sum_{i=0}^{n-1}h(f_c^{\circ i}(x)),\quad
J_n=F_n'=(f_c^{\circ n})'-1.
$$

$m_W$ 表示有限维 $k$-代数中乘以 $W$ 的线性算子，
$\operatorname{tr}_k$ 表示其普通线性代数迹，不是本原轨道和。
局部长度和根重数 $e_a$ 是正整数；出现在 $k$-系数中时经自然映射
$\mathbb Z\to k$ 解释。两者不能混淆。

## Proof Strategy and dependency map

1. 继承第二轮完整二进制支撑检测与 nilradical 等价，不重新证明为新结果。
2. 继承第三轮新素周期定位；既有两界相容，不能宣称矛盾。
3. 直接分解任意一元有限代数，精确计算 Jacobian annihilator 与乘法迹核。
4. 在 exact-$n$ 周期块上计算所有乘法／循环移位组成的普通迹。
5. 分清非退化留数对偶与普通点取值，说明为什么它也不能自动填补缺口。
6. 核查两条全局来源候选的量词：PCF 刚性不等于特殊纤维横截性；
   固定中心、固定真子圆盘的 $p$-adic 离散性不等于移动新周期的重数上界。
7. 仍缺全参数 reduced detection 或新素周期控制；不在结论隐藏该依赖。

## Proof / exact deductions

### Step 1. 继承的必要条件，不作新增准入

由 [R2 主证明](../../continuation_round2/positive_characteristic/PROOF_PACKAGE.md)
及 [协调者跟进](../../continuation_round2/COORDINATOR_PC_L_FOLLOWUP.md)，
有唯一正规代表

$$
k[x]=B_c\oplus V,\qquad V=k\oplus xk[x^2].
$$

非零常数不能位于 $K_c$，因为 $f_c$ 在 $k$ 上有固定点。故若存在
正规缺陷，则某个 $0\ne v\in V\cap K_c$ 有正奇次数 $D$。旧输入给出

$$
[H_n(v)]\in\operatorname{Nil}(A_n)\quad(\forall n\geq1),
\qquad
[H_n(v)]\ne0\quad\bigl(n>2\lfloor\log_2D\rfloor\bigr),
$$

以及最大根重数的必要下界

$$
M_n>\frac{2^{\lceil n/2\rceil}}{pD}\quad(\forall n\geq1).
\tag{1}
$$

[R3 主证明](../../continuation_round3/positive_characteristic/PROOF_PACKAGE.md)
已排除有限个例外素数及固定点贡献，证明每个充分大的允许素数 $\ell$
上必须有 exact-$\ell$、multiplier-$1$ 的新周期，根重数满足

$$
\frac{2^{(\ell+1)/2}}{pD}<e_\ell\leq\frac{2^\ell-2}{\ell}.
\tag{2}
$$

后一上界除以 $2^{\ell/2}$ 后增长，故式 (2) 相容。本轮不重算低期，
不把单个旧 germ 的 $p$-次重复当作新周期的控制。

### Step 2. Jacobian 测试究竟检测哪些普通点

**辅助命题 1。** 设 $k$ 为特征 $p>0$ 的代数闭域，任取非常数首一
多项式

$$
F=\prod_{a\in Z}(x-a)^{e_a},\qquad A=k[x]/(F),\qquad
R_{\mathrm{vis}}=\prod_{\substack{a\in Z\\p\nmid e_a}}(x-a).
$$

空乘积为 $1$。对任意 $W\in k[x]$，以下三项等价：

$$
F'W=0\text{ in }A;\qquad
R_{\mathrm{vis}}\mid W;\qquad
W(a)=0\text{ 对每个满足 }p\nmid e_a\text{ 的 }a.
\tag{3}
$$

**证明。** 固定 $a$，写 $F=t^{e_a}U(t)$，其中 $t=x-a$、$U(0)\ne0$。
若 $p\nmid e_a$，则

$$
F'=e_a t^{e_a-1}U+t^{e_a}U'
$$

的首项次数恰为 $e_a-1$。于是 $t^{e_a}\mid F'W$ 当且仅当 $t\mid W$。
若 $p\mid e_a$，第一项为零，且 $t^{e_a}\mid F'$；此因子对 $W$ 没有
任何限制。对全部互素的局部因子合并，得到式 (3)。若 $F'=0$，所有
$e_a$ 均被 $p$ 整除，式 (3) 两边同为对任意 $W$ 成立，边界也包括在内。
$\square$

等价地，$F/\gcd(F,F')=R_{\mathrm{vis}}$。这里不是通常的完整 radical
$\prod_{a\in Z}(x-a)$。因此原轨道条件确实推出 $J_nH_n(v)=0$，但
Jacobian 测试仅留下局部长度在 $k$ 中非零的那些点。R2 的单个反例
已说明逆推失败；式 (3) 精确给出全部失败支撑，不宣称新算法或新源定理。

### Step 3. 全部乘法迹没有增加信息

**辅助命题 2。** 在辅助命题 1 的条件下，对任意 $W,U\in A$，

$$
\operatorname{tr}_k(m_{WU})
=\sum_{a\in Z}e_a W(a)U(a).
\tag{4}
$$

所以

$$
\operatorname{tr}_k(m_{WU})=0\quad(\forall U\in A)
\quad\Longleftrightarrow\quad R_{\mathrm{vis}}\mid W.
\tag{5}
$$

**证明。** 中国剩余定理给出
$A\simeq\prod_{a\in Z}k[t]/(t^{e_a})$。在因子 $a$ 的基底
$1,t,\ldots,t^{e_a-1}$ 中，乘以 $WU$ 的矩阵为三角矩阵，全部对角元
都等于 $W(a)U(a)$。其迹为 $e_aW(a)U(a)$，各因子相加得到式 (4)。
若 $W$ 在所有可见点为零，式 (4) 对任意 $U$ 为零。反之，对一个可见
点 $a$，可由中国剩余定理选 $U$ 在该因子上为 $1$、其他因子上为 $0$；
式 (4) 得到 $e_aW(a)=0$。由于 $e_a\ne0$ in $k$，有 $W(a)=0$。
$\square$

即便允许任意多项式测试权重 $U$，普通乘法迹配对的核也恰好是式 (3)
的同一个理想。用迹配对代替 Jacobian annihilator 并未获得丢失的
普通点信息。这不是一个关于“所有可能不变量”的不可能性定理；例如
特征多项式仍可能保留 $p$-次幂因子，不能一并称为完全失明。

### Step 4. 新素周期上的循环扭曲迹仍有同一盲区

回到 $A_n$。因 $F_n(f_c(x))=f_c(f_c^{\circ n}(x))-f_c(x)$ 被 $F_n(x)$
整除，代入 $x\mapsto f_c(x)$ 在 $A_n$ 上良定义。它给出 $k$-代数
自同构 $\sigma$，因为 $\sigma^n=1$。设 $O$ 为 exact-$n$ 的普通周期，全部点的根重数
为同一个 $e$；对本轮相关 multiplier-$1$ 周期，这由 R3 的局部共轭
引理保证。记对应的稳定块为

$$
A_{n,O}=\prod_{a\in O}k[t_a]/(t_a^e).
$$

**辅助命题 3。** 对任意 $U\in A_{n,O}$ 和整数 $j$，

$$
\operatorname{tr}_k(m_U\sigma^j\mid A_{n,O})=
\begin{cases}
0,&n\nmid j,\\
e\displaystyle\sum_{a\in O}U(a),&n\mid j.
\end{cases}
\tag{6}
$$

因此若 $p\mid e$，则由所有乘法算子及 $\sigma$ 生成的线性算子代数
在此块上的普通迹恒为零，包括先作循环平均的任何这类迹。

**证明。** $\sigma$ 在 $n$ 个局部因子上作一个长度恰为 $n$ 的循环置换。
若 $n\nmid j$，$\sigma^j$ 不保留任何一个因子；乘法 $m_U$ 保留每个
因子，故 $m_U\sigma^j$ 的所有对角块为零，其迹为零。若 $n\mid j$，
$\sigma^j=1$，辅助命题 2 给出第二行。并且

$$
(m_U\sigma^i)(m_V\sigma^j)=m_{U\sigma^i(V)}\sigma^{i+j}.
$$

于是该算子代数的每个元素都是 $m_U\sigma^j$ 型元素的有限和。
当 $p\mid e$ 时，式 (6) 的每一项均为零，结论成立。$\square$

对素数 $n=\ell\ne p$，$1/\ell$ 确实存在，Reynolds 平均
$\ell^{-1}\sum_{j=0}^{\ell-1}\sigma^j$ 也定义良好。然而它不能消除式
(6) 中的零因子 $e$。故“取与特征不同的素周期，再平均即可还原普通
轨道数据”的捷径没有依据。本命题不声称原二次族在每个素周期确实
出现 $p\mid e$ 的高接触块；那一全局存在／排除问题仍须单独证明。

### Step 5. 非退化留数配对为何不构成自动修复

局部代数 $L=k[t]/(t^e)$ 上，令
$\lambda(W)=[t^{e-1}]W$。配对 $(W,U)\mapsto\lambda(WU)$ 非退化：
若非零 $W$ 的最低非零项为 $b t^r$，取 $U=t^{e-1-r}$ 就得到
$\lambda(WU)=b\ne0$。

但当 $e\geq2$ 时，$W=t$ 在唯一普通点处为零，却有

$$
\lambda(t\,t^{e-2})=1.
\tag{7}
$$

因此普通点为零不会推出留数配对为零。完全交或 Gorenstein 性提供
完美的 jet 对偶，不提供“普通取值条件自动包含所有 jet 条件”的定理。
用这一完美配对检测旧二进制引理的非零 $H_n(v)$ 固然可行，但原合同
没有供给所得留数必须为零的前提。

这也区别于旧 C402 的全概形多项式加权留数；那个对象刻意保留重数
及 jet 数据，不能把其完整源公式替换成本合同的普通本原轨道和。

### Step 6. 两条全局来源候选没有关闭剩余量词

**PCF 刚性与横截性。** Levy 的实际正文明确区分固定临界 portrait 的
有限性与方程交点的约化性；后者在正特征可失败。其有限性结论没有给出
固定 $c$ 上、$\ell\to\infty$ 的新本原周期根重数界。故“有限临界
portrait $\Rightarrow$ 所有新周期接触有一致上界”仍是没有证明的额外
推理，而不是该来源的结论。具体访问入口见 [来源核查 S1](SOURCE_AUDIT.md#s1-刚性不等于横截性)。

**提升后的 $p$-adic 离散性。** 另核到的 Einsiedler–Everest–Ward
定理以特征零良约化曲线上的固定中心 $x$ 为量词起点；真子圆盘
$r<1$ 中的有限性不提供全部残差圆盘 $|y-x|<1$ 内的统一总数，
也没有让中心随新的周期移动后的统一常数。即便已有合适提升，
把一个特殊纤维根重数解释为同残差圆盘内提升根的总重数后，所需
统一上界仍没有来源支持。见 [来源核查 S2](SOURCE_AUDIT.md#s2-固定中心的-p-adic-离散性不是所需重数上界)。

两条都只是当前所选应用未成立，不是对来源本身的否定。

## Corrections or missing assumptions

要经重数路线证明原等式，一个足够的缺失引理仍是：对每个原允许的
$(p,c)$，若 $E_\ell^{\rm new}$ 为 exact-$\ell$ 点的最大根重数
（没有这种点时取 $0$），则在 R3 的有限例外集 $E_c$ 外有

$$
\liminf_{\substack{\ell\to\infty\\\ell\text{ prime},\ \ell\notin E_c}}
\frac{E_\ell^{\rm new}}{2^{\ell/2}}=0.
\tag{8}
$$

式 (2) 与式 (8) 会矛盾，但式 (8) **未获证明**。本轮没有把
Jacobian／迹配对盲区当作式 (8) 为假的证据。

若绕过重数，则仍需对每个非零正规 $v$ 证明存在某个 $n$，使
$H_n(v)$ 在 $F_n$ 的至少一个普通根处非零；或从全部普通轨道和
构造某个有理转移，再调用旧的无极点引理。式 (3)--(7) 不提供这些
额外数据。Hilbert 90 的有限循环字段转移也不是该统一多项式转移。

## Open risks and disposition

- 原命题可能真、可能假；没有全族反例或完整缺陷分类。
- 来源检索有界；“所读正文没有提供所需结论”不等于世界文献穷尽。
- 辅助命题为当前作者手推的经典代数适配；没有冒称独立非作者审查。
- 本轮一项原问题续接、零第二题、零完整合同、零数学执行。
- 无新稿／PDF、旧实验重跑、正式评价、封存、外部模型／上传／GPU，
  无共享状态或 Git 写入。

本轮最准确的结论为
`ORIGINAL_QUESTION_UNCLOSED / TRACE_SHORTCUT_BOUNDARY_EXACT / NOT_ADMITTED`。
`NO_BAD_EULER_OR_ROOT_NUMBER` 始终有效。
