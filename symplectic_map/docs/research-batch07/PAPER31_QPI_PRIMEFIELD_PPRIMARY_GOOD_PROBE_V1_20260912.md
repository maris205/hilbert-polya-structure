# Proof Package：素域好纤维的 p-primary 初始交数 V1

日期：2026-09-12 UTC。作者：`/root/p31_qpi_primefield_pprimary_good_probe_v1`。
标签：`AUTHOR_PROOF / PRIME_FIELD_GOOD_FIBRES_ONLY`；`route_applicability: NOT_APPLICABLE`。
本件是有界作者证明，不是 fresh 数学票、正式候选或长文价值判定。

## Claim

保持原带标记对象

$$
W_h:\quad v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad O=[0:1:0].
$$

设 $p>3$ 为素数，$T\in\mathbf F_p^\times$，$h_*\in\mathbf F_p$，且

$$
\delta(h_*)\ne0,\qquad
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T.
$$

令 $d=\operatorname{ord}P(h_*)$，$i_n=(nP.O)_{h_*}$，不相交时取零；
交数沿原参数 $z=h-h_*$，不作分歧重标。只考虑 $p\mid d$ 分支。本件证明

$$
\boxed{i_d=1+\mathbf 1_{\{8h_*-9=0\}}.}\tag{P1}
$$

标准形式群传播随后给出，对每个整数 $n\ge1$，

$$
\boxed{i_n=
\begin{cases}
0,&d\nmid n,\\
p^{v_p(n/d)}\bigl(1+\mathbf 1_{\{8h_*-9=0\}}\bigr),&d\mid n.
\end{cases}}\tag{P2}
$$

这里 $v_p$ 是整数的 $p$-进赋值；(P2) 仍只针对 (P1) 的同一参数分支。
不分类 prime-to-$p$ 初始交数、扩域参数、坏纤维、无穷远或全局除子。

## Status

`PROVABLE AS STATED`。待核思路的数值结论保持不变；必须修正其中的微分表述：
相对微分不能未经说明沿截面拉回成基微分，本文使用 Frobenius 扭曲上的水平导数。
Igusa 前提通过真实有限 étale 邻域实现，不直接将 Igusa 除子公式套到原基。

## Assumptions and notation

消费已接受 [PF]/[D] 的原模型识别、泛 $P$ 非挠性、$j\notin k(h)^p$、点数同余、小阶排除及

$$
s=h^2-4T,\quad c_4=s^2+24hT,\quad c_6=-s^3-36hTs-216T^2,
$$

$$
a_4=-c_4/48,\quad a_6=-c_6/864,\quad
X=u+s/12,\quad Y=v+(hu-T)/2.
$$

因此短模型 $E$ 为 $Y^2=X^3+a_4X+a_6$，判别式为 $T^3\delta$。
其 Hasse 系数 $A$ 是 $(X^3+a_4X+a_6)^{(p-1)/2}$ 的 $X^{p-1}$ 系数。
令 $q=8h-9$；已接受的模型化微分为

$$
\lambda=-\frac q\delta\,dh.\tag{1}
$$

允许扩充常数至 $k=\overline{\mathbf F}_p$，取 $R=k[[z]]$。
所有导数均指连续 $k$-导数 $D=d/dz$，故 $D$ 在 $R^p=k[[z^p]]$ 上为零。
常数扩张不改变原有限长度。写 $E'=E^{(p)}$，坐标为 $X',Y'$，方程为

$$
Y'^2=X'^3+a_4^pX'+a_6^p,
$$

并令 $F:E\to E'$、$V:E'\to E$ 为相对 Frobenius 和 Verschiebung，$VF=[p]$。

## Proof strategy and dependency map

1. 已接受素域点数论把 $p\mid d$ 化为 $A(h_*)=1$ 和 $d=mp$，$m=1$ 或 $2$。
2. 好普通邻域上，以有限 étale 的 $\ker V$ 生成元及四阶标记实现实际 Igusa 提升。
3. 拉回 [UV] (3.1)，并检查短模型缩放，得到兼容生成元的水平速度阶等于 $\operatorname{ord}\lambda$。
4. $FQ$ 的坐标是 $p$ 次幂；群律的水平对数导数给差截面的准确速度。
5. 速度阶至多一，故导数不可见的 $z^p$ 项不影响初始交数；$V$ 的 étale 性保持交数。
6. (P2) 只用普通形式群，其一般先例 [N] Lemma 8.2 明确扣除。

## Proof

### Step 1. 将闭点降至非零 p 挠点

已接受点数同余是 $\#E_{h_*}(\mathbf F_p)\equiv1-A(h_*)\pmod p$，不要求 $q(h_*)\ne0$。
由于 $p\mid d$，有 $A(h_*)=1$，故闭纤维普通且 $A$ 在 $R$ 为单位。
Hasse 界给 $\#E_{h_*}(\mathbf F_p)=p$（$p\ge7$），
而 $p=5$ 时只可能为 $5$ 或 $10$。
原 $P$ 不是一、二、三阶：$-P=(0,0)\ne P$，$2P=(T,0)\ne-P$。
因此

$$
d=mp,\qquad m\in\{1,2\},\qquad m=2\Longrightarrow(p,d)=(5,10).
$$

设 $Q=mP$。闭点 $Q(h_*)$ 准确为非零 $p$ 挠点，且 $pQ=dP$。
其短坐标仿射且 $Y(Q(h_*))\ne0$，因为非零奇阶点不是二挠点。
同样 $FQ(h_*)$ 是 $E'_{h_*}$ 的非零 $p$ 挠点，且属于 $\ker V$。

### Step 2. 实现 Igusa 前提，而非任意选择两个不兼容数据

在原好普通开邻域上，$V$ 是有限 étale 同态，$\ker V$ 为秩 $p$ 的有限 étale 群概形。
因 $R$ 严格 henselian，$FQ(h_*)$ 唯一提升为 $Q_0\in\ker V(R)$。
其特殊点非零，故它是 $\ker V$ 的生成元；$Y'(Q_0)$ 在 $R$ 为单位。
这不是任意形式截面：它来自 $(\ker V)\setminus O$ 的有限 étale 邻域，坐标为可分代数幂级数。

为实际使用 [UV] §3，进一步在有限 étale 邻域选一准确四阶点。
由于 $p>3$，$E[4]$ 有限 étale，几何四阶点可作这种提升。
所得光滑代数邻域 $U$ 上的 $E$、四阶点与 $Q_0$ 给出到
$\operatorname{Ig}_1(4)$ 的模映射，并识别 $E_U$ 为其普适椭圆曲线的拉回。
这是 [UV] §3.1 的准确级结构；$U$ 到原基在所选点处 étale，完成环仍为 $R$，参数仍为 $z$。
原 $j$ 非常数，故此模映射非恒定，源有理微分恒等式可在泛点拉回。

[UV] §3.2 的生成元 $Q_0$ 决定兼容的 $\alpha$，满足 $\alpha^{p-1}=A$。
本文先选 $Q_0$ 再用其兼容 $\alpha$，不独立任取一个 $(p-1)$ 次方根来假定公式成立。
$A(h_*)=1$ 保证 $\alpha$ 为单位；该根也可由单位方程的 Hensel 提升取得。
[UV] (3.1) 的第一式拉回后为

$$
\lambda=\alpha^{p-2}\frac{dX'(Q_0)}{2Y'(Q_0)}.\tag{2}
$$

此式不使用 $\mu$ 的商表达式，因此不需除以可能在 $q=0$ 消失的 $\lambda$。
源式在泛点成立并作为有理微分恒等式延拓；右侧在本好普通邻域正则。

短模型兼容性不能省略。若两短模型满足
$X=u^2\widetilde X$、$Y=u^3\widetilde Y$，$u$ 在好邻域为单位，则

$$
\lambda=u^{-2}\widetilde\lambda,\qquad
\alpha=u\widetilde\alpha,\qquad
\frac{dX'(Q_0)}{2Y'(Q_0)}
=u^{-p}\frac{d\widetilde X'(Q_0)}{2\widetilde Y'(Q_0)}.
$$

最后一个等式使用 $d(u^p)=0$；总权重为 $u^{p-2-p}=u^{-2}$，与 (1) 一致。
因此 (2) 是原指定短模型的微分恒等式，不只是在另一个规范化模型中的赋值猜测。

### Step 3. 水平对数导数与移动平移

因为 $E'$ 的系数在 $R^p$，它连同群律与原点下降到 $R^p$。
该下降给出水平提升 $D_h$，在基环等于 $D$，并满足 $D_hX'=D_hY'=0$。
对任意 $S\in E'(R)$，差 $\theta_D(S)=D\circ S^*-S^*\circ D_h$
在基环为零，所以是 $S$ 处的相对切向量；用群平移移至原点，再与
$\omega'=dX'/(2Y')$ 配对，定义水平对数导数 $L_D(S)\in R$。
在仿射且 $Y'(S)$ 为单位处，定义准确成为

$$
L_D(S)=\frac{D X'(S)}{2Y'(S)}.
$$

这是利用 $D(R^p)=0$ 的定义，不把 $S^*\Omega^1_{E'/R}$ 误当作 $\Omega^1_{R/k}$。
群律定义于 $R^p$，故其系数导数为零；其切映射经平移识别为两个原点切向量之和。
从而 $L_D(S_1+S_2)=L_D(S_1)+L_D(S_2)$，且 $L_D(-S)=-L_D(S)$。
此处使用群律的两个变量求导，已包含移动平移点的导数。

令 $Z=FQ-Q_0$，则 $Z(h_*)=O$，且 $VZ=pQ=dP$。
$FQ$ 的坐标为 $X(Q)^p,Y(Q)^p$，所以 $L_D(FQ)=0$。因此

$$
L_D(Z)=-L_D(Q_0),\qquad
\operatorname{ord}_z L_D(Z)=\operatorname{ord}_{h_*}\lambda=:\ell.\tag{3}
$$

式 (1) 以及好点条件给

$$
\ell=\begin{cases}0,&q(h_*)\ne0,\\1,&q(h_*)=0.\end{cases}\tag{4}
$$

$q$ 的斜率为 $8\ne0$，且 $\delta$ 是单位，故第二行确实为一。

### Step 4. 原点处单位因子与低阶积分

固定水平短模型参数 $w'=-X'/Y'$，并令 $v'=-1/Y'$。
原点完成环满足

$$
v'=w'^3+a_4^p w'v'^2+a_6^p v'^3,
\qquad v'=w'^3 U(w'),\quad U\in R^p[[w']],\ U(0)=1.
$$

隐函数系数由该方程递归唯一决定，故确实在 $R^p$，不会产生基方向导数。
从 $X'=w'/v'$、$Y'=-1/v'$ 直接计算

$$
\omega'=H(w')\,dw',\qquad
H(w')=1+\frac{w'U'(w')}{2U(w')},\qquad H(0)=1.
$$

因此对 $Z$ 也有 $L_D(Z)=H(w'(Z))D(w'(Z))$，不需要在原点除以有极点的 $Y'$。
设 $f=w'(Z)\in zR$，则由 (3) 得 $\operatorname{ord}_z Df=\ell\in\{0,1\}$。
写 $f=\sum_{j\ge1}c_jz^j$。导数的首个非零项在 $z^\ell$，故
$(\ell+1)c_{\ell+1}\ne0$。
若 $1\le j<\ell+1$，则 $jc_j=0$，而 $j<\ell+1\le2<p$，所以 $c_j=0$。
故 $\operatorname{ord}_z f=\ell+1$。
导数不可见的正次 $p$ 倍指数至少为 $p>\ell+1$，不能产生更低首项。

$V$ 在原点 étale，故其形式参数展开为 $w(VS)=c\,w'(S)+O(w'(S)^2)$，$c\in R^\times$。
代入 $Z$ 得 $(VZ.O)_{h_*}=(Z.O)_{h_*}=\ell+1$。
由于 $VZ=dP$，(P1) 得证。
原广义模型参数与短模型参数都生成零截面的理想，所算交数也就是原 $i_d$。

### Step 5. 标准传播与边界核对

有限群中 $nP(h_*)=O$ 当且仅当 $d\mid n$；否则 $i_n=0$。
若 $n=drp^e$、$p\nmid r$，形式群的 $[r](w)=rw+O(w^2)$ 保持正赋值。
本好普通点的 $[p](w)$ 最低项为 $c_pw^p$，$c_p$ 是单位，其余项次数大于 $p$。
故对任意正赋值 $f$，$\operatorname{ord}[p](f)=p\operatorname{ord}f$；迭代即 (P2)。∎

$p=5,d=10$ 没有例外：取 $Q=2P$ 后闭点为非零五挠点，以上每步仍成立。
$q=0$ 也未删去：$h_*=9/8$ 时 $\delta=(256T+27)^2/4096$，
仅 $T=-27/256$ 使该点为坏点而被原假设排除；其他时间若同时 $p\mid d$，准确为 $i_d=2$。
普适 Igusa 普通点上的微分无零，不代表其在原基拉回无零：
$U\to\operatorname{Ig}_1(4)$ 可以分歧，而 $U\to\mathbb A^1_h$ 在所选点仍 étale。
这里的 $q=0$ 阶由 (1) 算出，没有误用 Igusa 上的除子阶。

## Corrections, open risks and prior-art deduction

本作者证明没有剩余未证环节；独立接受仍须由非作者核对实际新稿。
最易误用的三点是：生成元与 $\alpha$ 必须兼容；移动平移要用可加水平对数导数；
低阶积分依赖 $\ell+1<p$，不能把它推广为任意高阶接触公式。
证明中采用 $k=\overline{\mathbf F}_p$ 只是局部证明工具，不扩张本文参数量词。

[N] Lemma 8.2 已有一般交数传播；本处 $h_{E,v}=0$，其公式准确降为 (P2) 的 $p^e$ 因子。
本文给出该普通特例的自足短证明，仅为核对适用性，不将标准传播申报新理论。
Igusa 标记、UV/Broumas 微分机制、Hensel 提升、群律切映射与形式群亦全部扣除。
本件新增书面输出限于原素域 $p\mid d$ 分支的准确初始数值，不据此预授长文准入。

## Actual reading and execution boundary

作者本人 FULL 读 [PF] 325行、[D] 176行、工作区 AGENTS/WORKFLOW 与 proof-writer 技能；
批次接续仅消费最新入口。旧 F5 文本只定向检索相关行，不重算、不修改或扩采样。
[UV] 实读 §2 模型权重与 (2.2)、Remark 2.8、§3.1–3.2 全部至 Corollary 3.5；
本文只消费 (3.1) 第一式及级结构，不消费其超奇异局部不等式或全球计数。
[N] 实读官方 PDF 文本 pp.1003–1005，包括 Lemma 8.2 陈述和证明；
网页截图接口失败，未声称已作视觉 PDF 核验；普通传播另由 Step 5 自足证明。
Broumas 原件本轮未另读，所需 $p>3$ 公式以 [UV] 明确范围为准，不猜测旧 OCR 的素数限制。

只读作者辅助核对了 Step 3–4，未承担 fresh 数学票，且没有写文件。
proof-writer 促使本件显式修正微分类型及保留结论量词，没有导致采样或权限暂停。
本轮仅以 `apply_patch` 新增本件；没有修改冻结稿、建项目／锁／论文、编译、GPU或外部效力。

[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[D]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S3
[N]: https://nyjm.albany.edu/j/2016/22-46v.pdf
