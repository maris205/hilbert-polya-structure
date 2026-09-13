# Paper 30：两倍奇素数临界根簇的下一 Newton 边与可分提升

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
按本轮完整读取的 `proof-writer` 撰写；本件是作者证明稿，不是独立审查票。

## Claim

设 $p\ge7$ 为奇素数，$\gcd(r,2p)=1$，保持既定物理正 kick、参数
$\lambda$ 及 SUM action。令

$$
m=(p-1)/2,\quad h=D_2,\quad \kappa=\lambda-1/16,\qquad
S(\kappa)=\frac{h^{p-1}}p C_{r,2p}(1/16+\kappa).
\tag{1}
$$

在实圆分域的 $p$ 进完成 $L=\mathbb Q_p(h)$ 上，规范 $v_h(h)=1$。
对代数闭包中的根也使用该赋值的唯一延拓。以下结论成立。

1. 已知的 $\kappa=0$ 剩余根簇包含恰好 $m$ 个实际代数根，按重数计。
   取 $\tau^2=h$ 后，这个根簇的单首因子可合法改标为一个整的单首
   $m$ 次多项式，其剩余多项式是

$$
\boxed{(-1)^m G_m(K;\bar\gamma),\qquad
G_m(K;\bar\gamma)=[w^m]\bigl((1+Kw)^2+\bar\gamma w^2\bigr)^{-1/2},
\quad \gamma=5/3072.}
\tag{2}
$$

   这里 $K=\kappa/\tau$，$\bar\gamma$ 是 $\gamma$ 在 $\mathbb F_p$ 中的像。
   式 (2) 可分，故全部 $m$ 个实际簇内根均简单。
2. 若 $p\equiv1\pmod4$，簇内的下一条 Newton 边恰为
   $(0,m/2)\longrightarrow(m,0)$，所有 $m$ 个根满足 $v_h(\kappa)=1/2$。
3. 若 $p\equiv3\pmod4$，确定的下一条非水平边是
   $(1,(m-1)/2)\longrightarrow(m,0)$。其中 $m-1$ 个根满足
   $v_h(\kappa)=1/2$；余下一个根简单，且属于 $L$。
   该根或者恰为 $\kappa=0$，或者有正整数赋值，因而至少为 $1$。
   若 $s_0=S(0)\ne0$，余下的左边精确写成
   $(0,v_h(s_0))\longrightarrow(1,(m-1)/2)$，其根的赋值为
   $v_h(s_0)-(m-1)/2$。本件不进一步声称已计算一般 $p$ 的 $v_h(s_0)$。
4. 结合已接受的 $m+1$ 个外部简单根，完整 $p$ 次多项式 $C_{r,2p}$
   在特征零代数闭包中无重根。这里不声称全部根为实数，也不声称
   这些根处下一作用量系数 $Q$ 非零。

## Status

上述明确限定 $p\ge7$ 的结论：`PROVABLE AS STATED`。

本件解决实际低权重主面到根簇 Newton/Hensel 结论的桥接。
$p=5$ 的 $\bar\gamma=0$ 是真实例外，必须另用精确证书；
$p=3$ 不满足这里的局部整系数条件，沿用已接受的 $C_6$ 结果。
不能用本件的可分性证明覆盖这两个边界素数。

## Assumptions

- 使用已接受的实际有限作用量多项式及其 $2p$ 局部整性定理，
  不替换构造、参数或 action 规范。
- 引用下列两份本轮作者引理所证明的准确陈述；在本件形成时，
  它们尚待非作者统一审查。本件不将“作者证明完毕”记成“已独立接受”。
- $r$ 只要求与 $2p$ 互素；论证对每个相应实圆分嵌入成立，
  不从有限 $r$ 样本外推。

## Notation and Inputs

$\mathcal O$ 为 $L$ 的整数环，剩余域为 $\mathbb F_p$，且 $v_h(p)=m$。
写 $S=\sum_{b=0}^p s_b\kappa^b$。令 $E=L(\tau)$、$\tau^2=h$；
由 $X^2-h$ 的 Eisenstein 性，$E/L$ 为完全分歧二次扩张，
$\tau$ 是其整数环 $\mathcal O_E$ 的素元，剩余域仍为 $\mathbb F_p$。
在 $E$ 上，$v_\tau=2v_h$。

本件依赖以下精确版本。

1. [偶数半阶与两倍素数稿](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)，
   SHA256 `2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a`。
   这是已接受输入：$S\in\mathcal O[\kappa]$，次数为 $p$，最高次系数为单位，且

$$
\bar S=2\kappa^m(\kappa^{m+1}+1/8).
\tag{3}
$$

   非零的 $m+1$ 个剩余根已知简单；本件不重审该阶段。
2. [低半权重与唯一阶乘极点桥](PAPER30_TWIST_TWO_PRIME_CLUSTER_WEIGHT_PROBE_V1_20260907.md)，
   SHA256 `6af2251223c61eb255cbd35d62421374f6f2c339e97d1de6f5484b057b7b7cef`。
   已完整读取其作者证明。本件使用它的逐系数结论

$$
v_h(s_b)\ge\max\{0,\lceil(m-b)/2\rceil\},
\tag{4}
$$

   以及 $\operatorname{wt}(h)=2,\operatorname{wt}(\kappa)=1$ 下准确的首面

$$
\operatorname{in}_m S
=\frac14\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\binom m{2j}\binom{2j}j
\left(\frac\gamma4\right)^j H^jK^{m-2j}.
\tag{5}
$$

   $H,K$ 是关联分次环的初始符号。式 (4)—(5) 针对完整实际 $C$，
   已包括有限指数系数的 $p!$ 层，不能仅由退化辅助 ODE 替代。
3. [四次 jet 与有限系数多项式引理](PAPER30_TWIST_DEGENERATE_FLIP_QUARTIC_JET_LEMMA_V1_20260907.md)，
   SHA256 `58a65cc7ca2f646f3e40c7d558ca731df887991e0b3ef3bbc596a5b8712dcf97`。
   已完整读取其作者证明。使用其有限多项式公式和可分性身份；
   为明确本件的剩余根边界，下文保留所需的短证明，不重复记为独立贡献。

## Proof Strategy

先由旧的互素剩余分解隔离次数恰为 $m$ 的根簇，再用式 (4)—(5)
证明平方根改标后的因子仍整。随后对其可分剩余多项式作 Hensel 提升。
这一区分保证只从 $v_h(\kappa)>0$ 出发，而没有暗中假设
$v_h(\kappa)\ge1$。Newton 边由准确系数赋值读取，而非由预选尺度猜测。

## Dependency Map

1. 式 (3) 与完备离散赋值环上的互素因子 Hensel 引理给出根簇因子。
2. 式 (4)—(5) 给出整的平方根改标及其准确剩余式。
3. 有限二项式公式与微分身份排除式 (2) 的全部重根。
4. 单根 Hensel 引理给出实际简单根；系数赋值给出各条 Newton 边。
5. 唯一深根的 Galois 不变性给出其下降；旧外部根结果补齐完整 $C$。

## Proof

### Step 1. 先隔离实际根簇，不预设整数尺度

令 $a\in\mathcal O^\times$ 为 $S$ 的最高次系数。式 (3) 给出
$\bar a=2$，且单首多项式 $S/a$ 的剩余分解为

$$
\overline{S/a}=\kappa^m(\kappa^{m+1}+1/8).
$$

这两个单首因子互素，因为第二个因子的常数项 $1/8$ 非零。
$\mathcal O$ 完备，故互素因子形式的 Hensel 引理给出唯一分解

$$
S=aFJ,\qquad F,J\in\mathcal O[\kappa]\text{ 单首},qquad
\deg F=m,\quad\deg J=m+1,
\tag{6}
$$

其中 $\bar F=\kappa^m$、$\bar J=\kappa^{m+1}+1/8$。
单首整多项式的根均整；$F$ 的每个根约化为零，故其赋值严格大于零。
反之，$J(0)$ 为单位，所以 $J$ 没有赋值严格大于零的根。
因此 $F$ 恰是所需 $m$ 根簇的完整因子，按重数计数。
该阶段没有把正有理赋值替换成正整数赋值。

### Step 2. 平方根改标是整的，且不混入外部根

在 $E$ 中定义完整多项式的辅助改标

$$
R(K)=\tau^{-m}S(\tau K).
\tag{7}
$$

其第 $b$ 个系数的 $\tau$ 赋值为 $2v_h(s_b)+b-m$。
当 $b\le m$，式 (4) 使其非负；当 $b>m$，原整性使其严格为正。
所以 $R\in\mathcal O_E[K]$，且由式 (5) 得

$$
\bar R(K)=\frac14\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\binom m{2j}\binom{2j}j
\left(\frac{\bar\gamma}4\right)^j K^{m-2j}
=\frac{(-1)^m}{4}G_m(K;\bar\gamma).
\tag{8}
$$

虽然 $R$ 的特征零次数仍为 $p$，其剩余次数只是 $m$；
不能把 $R$ 当作已单首化的根簇因子。为此定义

$$
\widetilde F(K)=\tau^{-m}F(\tau K).
\tag{9}
$$

由式 (6)—(7)，在 $E[[K]]$ 中有

$$
\widetilde F(K)=\frac{R(K)}{aJ(\tau K)}.
$$

$aJ(\tau K)$ 属于 $\mathcal O_E[K]$，常数项为单位，
故其形式倒数属于 $\mathcal O_E[[K]]$。因此右侧的每个系数均整。
左侧本来就是 $m$ 次多项式，遂得
$\widetilde F\in\mathcal O_E[K]$，且其最高次系数恰为 $1$。
又因 $\overline{aJ(\tau K)}=2\cdot(1/8)=1/4$，式 (8) 给出

$$
\boxed{\overline{\widetilde F}=(-1)^mG_m(K;\bar\gamma).}
\tag{10}
$$

这证明对已隔离实际根簇作平方根改标的合法性。

### Step 3. 有限剩余多项式可分

因为 $p\ge7$，$\bar\gamma\ne0$。有限展开为

$$
G_m(K;\bar\gamma)=(-1)^m\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\frac{m!}{j!^2(m-2j)!}
\left(\frac{\bar\gamma}4\right)^jK^{m-2j}.
\tag{11}
$$

所有展示的非零系数都是 $\mathbb F_p$ 的单位，因为各阶乘的指标
小于 $p$。次数为 $m$。当 $m$ 偶时常数项非零；
当 $m$ 奇时常数项为零而一次项非零。

由输入 3 已直接验证的生成函数微分身份，

$$
(K^2+\bar\gamma)G_m''+(1-2m)KG_m'+m^2G_m=0.
\tag{12}
$$

若 $\alpha^2+\bar\gamma=0$，生成函数在 $K=\alpha$ 处化为
$(1+2\alpha w)^{-1/2}$。由于 $-1/2=m$ 在 $\mathbb F_p$ 中，
且 $m!$ 可逆，有

$$
G_m(\alpha;\bar\gamma)=\binom{-1/2}m(2\alpha)^m=(2\alpha)^m\ne0.
$$

若普通点 $\alpha^2+\bar\gamma\ne0$ 是重数 $k\ge2$ 的根，
则 $2\le k\le m<p$。在 $K-\alpha$ 的展开中，式 (12) 的
$(K-\alpha)^{k-2}$ 系数恰为
$(\alpha^2+\bar\gamma)k(k-1)c$，其中 $c\ne0$ 为首个非零展开系数。
该乘积非零，矛盾。因此 $G_m$ 的每个代数根均简单。

### Step 4. 每个剩余根提升为实际简单根

取 $\mathbb F_p$ 的有限扩域 $k'$，使式 (10) 的所有根都属于 $k'$，
再取 $E$ 的相应有限非分歧扩张 $E'$。该扩张的整数环仍完备，
剩余域为 $k'$，素元仍可取 $\tau$。
对式 (10) 的每个根 $\alpha$，有
$\overline{\widetilde F}'(\alpha)\ne0$，故单根形式的 Hensel 引理
给出唯一提升 $K_\alpha\in\mathcal O_{E'}$，且
$\widetilde F'(K_\alpha)$ 为单位。
不同 $\alpha$ 给出不同提升；共 $m$ 个，已经穷尽单首 $m$ 次因子。
故全部 $\kappa_\alpha=\tau K_\alpha$ 为 $F$ 的简单根。

还可读取一个有用但不涉及 $Q$ 的导数结论。由式 (8) 和简单剩余根，
$R'(K_\alpha)$ 为单位；对式 (7) 求导，得

$$
v_h\bigl(S'(\kappa_\alpha)\bigr)=\frac{m-1}{2}.
\tag{13}
$$

### Step 5. 实际 Newton 边及深根边界

式 (5) 与式 (11) 中各系数非零表明，对
$0\le j\le\lfloor m/2\rfloor$ 恰有

$$
v_h(s_{m-2j})=j.
\tag{14}
$$

结合式 (4)，全部其余系数点位于所述下凸包之上或边上。
式 (3) 又给出 $(m,0)$ 到 $(p,0)$ 的外部水平边。

若 $m$ 偶，式 (14) 包含 $(0,m/2)$ 与 $(m,0)$，
所以两点间的斜率 $-1/2$ 边是准确的完整簇内边。
式 (11) 无零根，亦使所有提升 $K_\alpha$ 为单位，
故所有簇内根的 $h$ 赋值等于 $1/2$。

若 $m$ 奇，式 (14) 的最左点为 $(1,(m-1)/2)$。
因此至 $(m,0)$ 的边斜率为 $-1/2$、水平长度为 $m-1$。
式 (11) 有恰一个零单根；其余 $m-1$ 个剩余根均非零。
故恰有 $m-1$ 个实际根赋值为 $1/2$，另一个根赋值严格大于 $1/2$，
或者恰为零。

该唯一深根的性质在 $L$ 的绝对 Galois 群下不变：
$F$ 定义于 $L$，且完备离散赋值的延拓唯一。
唯一性迫使该代数根被整个 Galois 群固定，因特征零可分而属于 $L$。
所以若它非零，其赋值为整数。
也可直接从 $s_0$ 看清未被计算的唯一位置：

- 若 $s_0\ne0$，式 (4) 给出 $v_h(s_0)\ge(m+1)/2$，
  最左边为 $(0,v_h(s_0))\to(1,(m-1)/2)$。
  该边的水平长度为 $1$，根赋值为
  $v_h(s_0)-(m-1)/2\ge1$。
- 若 $s_0=0$，$\kappa=0$ 就是根；式 (14) 的 $b=1$ 系数非零，
  故该根仍是单根，其余非零根的 Newton 多边形从 $b=1$ 开始。

这里未假定 $s_0\ne0$，也未把下界冒充它的精确赋值。

### Step 6. 补齐完整多项式并固定结论范围

因子 $F$ 的全部 $m$ 根已简单。因子 $J$ 的 $m+1$ 个根为已接受的
外部简单根；它们的赋值为零，与 $F$ 的正赋值根不相交。
故 $S=aFJ$ 无重根。式 (1) 仅作非零标量乘法和参数平移，
所以 $C_{r,2p}$ 同样无重根。所有步骤都对任意允许的 $r$ 成立。
这证明 Claim。$\square$

## Verification and Corrections

- 本稿没有运行新的素数扫描、浮点根扫描或经验拟合。
- 准确的初始面来自输入 2 的完整实际 action 权重证明，
  不是从辅助微分方程或有限样本推断。
- 输入 3 的四次 jet 和可分性身份已被本作者协作推导；
  这种交叉一致不充当本稿或输入稿的非作者独立审查。
- 平方根尺度是从已证明赋值界和非零主面推出的。
  原先“正赋值根必在 $\kappa=hK$ 尺度”不成立，未被用于证明。

## Open Risks and Delivery Boundary

- $p\equiv3\pmod4$ 时唯一深根的精确位置、以及 $S(0)$ 是否可能为零，
  本稿不计算；这不妨碍该根的单根性已经证明。
- $p=5$ 需要单独证书，因为式 (10) 在该素数退化为 $K^2$；
  不得把 $p\ge7$ 的非零系数论证照搬过去。
- 全部根实性、更高首项 $Q$ 非消失、完整 $\gcd(C,Q)$ 问题均未由本稿推出。
- 交付仅此新作者稿；输入、旧接受状态、冻结根、入口及批次状态均不修改。
  结论接受须等待针对准确版本的非作者审查。
