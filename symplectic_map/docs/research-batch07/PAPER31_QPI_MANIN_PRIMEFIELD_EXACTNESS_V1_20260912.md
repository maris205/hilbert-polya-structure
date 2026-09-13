# Proof Package：原 qPI 的素域 Manin 充要判据 V1

日期：2026-09-12 UTC。作者：主控 `/root`。
标签：`AUTHOR_PROOF / PRIME_FIELD_ONLY`；`route_applicability: NOT_APPLICABLE`。
本件是新的有界证明，不是独立审查、正式候选、长文容量判断或 Paper31 完成。

## Claim

令 $p>3$ 为素数，$T\in\mathbf F_p^\times$，保持原带标记对象

$$
W_h:\quad v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad O=[0:1:0].
$$

对每个 $h_*\in\mathbf F_p$ 满足 $\delta(h_*)\ne0$，令
$d=\operatorname{ord}(P(h_*))$，并令 $i_n(h_*)=(nP.O)_{h_*}$，不相交时取零。
交数在原基方向 $z=h-h_*$ 上计算，可把常数域扩至 $\overline{\mathbf F}_p$，不作分歧底变换。
采用 [M] 已接受的同一多项式 $N_p$，本件证明

$$
\boxed{N_p(h_*)=0
\quad\Longleftrightarrow\quad
p\nmid d\ \text{且}\ i_d(h_*)>1
\quad\Longleftrightarrow\quad
\exists n\ge1,\ p\nmid n:\ i_n(h_*)>1.}
\tag{PF}
$$

若两边成立，对每个 $p\nmid n$，相交当且仅当 $d\mid n$，且相交时 $i_n=i_d$。
本件不求 $d$ 的闭式或 $i_d$ 的准确数值，也不将 (PF) 扩张为
$T,h_*\in\overline{\mathbf F}_p$、任意有限扩域、坏纤维、无穷远或 $p\mid n$ 的分类。
“素域”是本次新命题的显式范围，不是将此前全代数闭域必要条件静默缩小；[M] 的旧范围保持。

## Status

`PROVABLE AS STATED`，仅针对 (PF) 的上述全部量词；当前仍为作者证明，待 fresh 非作者审查。

## Assumptions and notation

所有微分仅对基变量 $h$，时间 $T$ 固定。沿用

$$
\begin{aligned}
s&=h^2-4T,& q&=8h-9,& b&=2h^2-3h-8T,\\
\delta&=h^4-h^3-8Th^2+36Th+16T^2-27T,\\
c_4&=s^2+24hT,& c_6&=-s^3-36hTs-216T^2,\\
a_4&=-c_4/48,&a_6&=-c_6/864,&\Delta&=T^3\delta.
\end{aligned}
$$

短模型为 $Y^2=X^3+a_4X+a_6$，其中
$X=u+s/12$、$Y=v+(hu-T)/2$，原 $P$ 送至 $(s/12,T/2)$。
定义 $A,M,L$ 为准确多项式分解

$$
(Z^3+a_4Z+a_6)^{(p-1)/2}=Z^pM(Z)+AZ^{p-1}+L(Z),\qquad\deg L<p-1.
$$

$M$ 是首一、次数 $(p-3)/2$ 的多项式；$A$ 是本短模型的 Hasse 系数。
$q$ 是线性多项式，不是域大小。记 $A_*=A(h_*)$。
[M] 的实际接口为

$$
\lambda=-\frac q\delta\,dh,\quad B=\frac b{2q},\quad
\mu(P)=\frac T2M(s/12)+\wp_A(B),\quad
\wp_A(c)=c^p-Ac,
$$

$$
N_p=q^p\mu(P)=\frac12\bigl(Tq^pM(s/12)+b^p-Abq^{p-1}\bigr).
$$

[M] 已证明 $N_p\ne0$、$\deg N_p\le2p$、$j\notin\overline{\mathbf F}_p(h)^p$，
以及全部 $p\nmid n$ 在任意有限好点切触必有 $N_p=0$。
还消费已接受的泛 $P$ 非挠性，使 $nP$ 与 $O$ 不泛重合，交数是有限整数。
上述旧结论不在本件重新审查或重复计功。

## Proof strategy

在 $q(h_*)\ne0$ 的好点，将源 Manin 公式准确取到一阶。
当 $A_*\ne1$，素域点数同余使全部有理点为 prime-to-$p$ 阶；一阶公式给充分性。
当 $A_*=1$，同一公式下降为有限群上的同态，极零次数和 Hasse 界给小核；
原点不可能为一、二、三阶，从而排除这一支的 $N_p$ 零值。
最后处理唯一 $q=0$ 的好点并用形式群把 $d$ 传给所有允许的 $n$。

## Dependency map

1. 一阶公式依赖 [UV] §2 的加法性／坐标公式、好模型整形式展开及本文 Step 1 的准确消去。
2. $\mathbf F_p$ 上的点数模 $p$ 同余在 Step 2 用有限和证明，不预先把 Hasse 系数当作整数迹。
3. $A_*=1$ 时的同态在 Step 3 由代数局部提升构造；不直接假设源公式对任意超越形式点已定义。
4. 非零同态的证明依赖非零有理函数的极零次数相等及经典椭圆曲线 Hasse 界。
5. 排除小阶依赖本原曲线 $-P=(0,0)$、$2P=(T,0)$，不是一般椭圆族性质。
6. $q=0$ 分支及必要性直接消费 [M]；prime-to-$p$ 倍数保持交数使用形式群线性项。

## Proof

### Step 1. 好点的一阶 Manin 值

本步先假设 $q(h_*)\ne0$。在 $R=\mathbf F_p[[z]]$ 上写
$\lambda=\ell(z)dz$，其中 $\ell_0=\ell(0)=-q(h_*)/\delta(h_*)\in\mathbf F_p^\times$。
令 $Q$ 是以代数幂级数为坐标的局部截面，其闭点为 $O$；设

$$
w=-X/Y,\qquad w(Q)=\gamma z+O(z^2),\qquad\gamma\in\mathbf F_p.
$$

若 $Q$ 不是恒零截面，其局部交数是 $\operatorname{ord}_z w(Q)$；
所以 $\gamma=0$ 当且仅当这个交数大于一。恒零截面单独定义 $\mu(O)=0$。

源 [UV] 式 (2.3) 可重排为

$$
\mu(Q)=R_Q+\wp_A\left(\frac{dX(Q)/(2Y(Q))}{\lambda}\right)
-\wp_A\left(\frac{(d\Delta/\Delta)X(Q)}{12\lambda Y(Q)}\right),
\tag{1}
$$

其中，省略 $Q$ 后的坐标记号，

$$
\begin{aligned}
R_Q&=Y M(X)-\wp_A\left(\frac{X^2}{Y}+\frac{2a_4}{3Y}\right)\\
&=\wp_A\left(\frac{a_4X+3a_6}{3XY}\right)-\frac{YL(X)}{X^p}.
\end{aligned}
\tag{2}
$$

第二个等式由定义分解除以 $X^p$、用 $Y^2=X^3+a_4X+a_6$ 得到；
它正是 [M] Step 6 已核定的源消去。若 $i=\operatorname{ord}_z w(Q)\ge1$，
$\operatorname{ord}_zX=-2i$、$\operatorname{ord}_zY=-3i$。
式 (2) 右侧两项的阶分别至少为 $3i$、$i$，故 $R_Q(0)=0$。
式 (1) 最后一项的内部参数阶至少为 $i$，亦在闭点为零。

整短模型的形式展开具有
$X=w^{-2}(1+O(w))$、$Y=-w^{-3}(1+O(w))$。
对系数也随 $z$ 变化的此展开取全导数，$dX/(2Y)$ 的常数项仍是 $dw$ 的常数项：
首项 $w^{-2}$ 的系数是常数 $1$，其余系数的基微分除以 $Y$ 后阶至少为 $2i$，
对 $w$ 的微分项则为 $(1+O(w))dw$。因此

$$
\left.\frac{dX(Q)/(2Y(Q))}{\lambda}\right|_{z=0}=\frac\gamma{\ell_0}.
$$

在素域中 $c^p=c$，所以 (1) 给准确等式

$$
\boxed{\mu(Q)(h_*)=(1-A_*)\frac\gamma{\ell_0}.}
\tag{3}
$$

这里不仅是赋值下界；横截 $i=1$ 时的非零可能性也保留。
所有坐标代数提升均可放入有限可分函数域扩张，$
j\notin K^p$ 在可分扩张下保持，故源加法同态适用。
更明确地，可以先取代数闭常数域，取包含有限多个提升坐标的有限可分函数域，
再取其光滑射影基曲线及对应赋值处使用 [UV] 的同一公式；
局部嵌入保持参数 $z$ 且分歧指数为一，所得值仍在 $\mathbf F_p$。
这避免将来源的函数域陈述未经说明扩大到所有形式点。

我们还需要 $\mu$ 对所有这种好模型局部截面正则。
闭点为 $O$ 时由 (1)–(2)；闭点仿射且 $Y\ne0$ 时由源式所有分母为单位；
若闭点是二挠点，则 $2Q$ 闭点为 $O$，且 $\mu(Q)=\mu(2Q)/2$，故同样正则。
泛恒为二挠点的情形由同态的 $2\mu(Q)=0$ 给 $\mu(Q)=0$。

### Step 2. 素域点数与 Hasse 系数的准确同余

令 $f_*(X)=X^3+a_4(h_*)X+a_6(h_*)$。Euler 判据（零值也包含）给

$$
\#E_{h_*}(\mathbf F_p)\equiv1+\sum_{x\in\mathbf F_p} f_*(x)^{(p-1)/2}\pmod p.
$$

被求和多项式次数是 $3(p-1)/2<2(p-1)$。
对正指数 $e$，$\sum_{x\in\mathbf F_p}x^e$ 在 $p-1\mid e$ 时为 $-1$，否则为零；
常数项之和为 $p=0$。故唯一贡献是 $X^{p-1}$ 的系数，得到

$$
\boxed{\#E_{h_*}(\mathbf F_p)\equiv1-A_*\pmod p.}
\tag{4}
$$

若 $A_*\ne1$，群阶不被 $p$ 整除，因此 $p\nmid d$。
对原代数截面 $Q=dP$ 应用 (3) 和加法性，得到

$$
d\mu(P)(h_*)=(1-A_*)\gamma_d/\ell_0,
\qquad w(dP)=\gamma_d z+O(z^2).
\tag{5}
$$

$d,1-A_*,\ell_0$ 都可逆，且 $q(h_*)\ne0$，故
$N_p(h_*)=0$ 当且仅当 $\gamma_d=0$，也就是 $i_d>1$。
这已证明 $A_*\ne1$ 分支的全部充分性和必要性。

### Step 3. 在 A=1 的闭纤维上构造小核同态

本步仍取 $q(h_*)\ne0$，并设 $A_*=1$。
每个 $R_0\in E_{h_*}(\mathbf F_p)$ 都有一个坐标为 $\mathbf F_p[[z]]$ 中代数幂级数的提升：
若 $Y(R_0)\ne0$，固定 $X=X(R_0)$，用 $2Y(R_0)\ne0$ 的 Hensel 提升取得 $Y(z)$；
若 $Y(R_0)=0$，固定 $Y=0$，由好纤维 $f_*'(X(R_0))\ne0$ 提升 $X(z)$；
$O$ 取零截面。所解方程导数为单位，这些提升为可分代数幂级数。

定义

$$
\chi(R_0)=\mu(\widetilde R_0)(h_*)\in\mathbf F_p.
$$

若 $\widetilde R_1,\widetilde R_2$ 提升同一点，其差在闭点为 $O$；
在同时包含两组代数坐标的有限可分函数域上，(3) 与 $A_*=1$ 给
$\mu(\widetilde R_1-\widetilde R_2)(h_*)=0$。
因此 $\chi$ 与提升选择无关。对两点取同一有限扩张，其和仍为代数提升；
源加法性于是证明 $\chi:E_{h_*}(\mathbf F_p)\to(\mathbf F_p,+)$ 为群同态。

在非二挠仿射点，源式的内部参数在 $z=0$ 属于 $\mathbf F_p$，
其 $\wp_1$ 值是零；二挠点的 $\chi$ 值为零。因此准确有

$$
\chi(O)=0,\qquad \chi(X,Y)=Y M_{h_*}(X)
\quad\text{for every affine }(X,Y)\in E_{h_*}(\mathbf F_p).
\tag{6}
$$

该显式同态不是本件的新构造来源：[V] p.3 已明确给出同样的
$Y M(X)$ 下降表达式，并转引 Voloch 1990 Proposition 1.3。
本步以已接受的源 $\mu$ 接口作局部重证，目的是闭合本原族论证的所有假设，不重复申报先例。

下面不用该转引的未读证明来断言核，直接论证 $\chi\ne0$。
记整数 $H=\#E_{h_*}(\mathbf F_p)$。由 (4)，$p\mid H$。
经典 Hasse 界 $|H-(p+1)|\le2\sqrt p$ 适用于本光滑射影几何整亏格一曲线及其有理零点。
当 $p\ge7$，$p+1+2\sqrt p<2p$，且下界为正，故 $H=p$；
当 $p=5$，同一界允许的正 $5$ 倍数仅为 $5,10$。

有理函数 $g=Y M_{h_*}(X)$ 在几何椭圆曲线上只在 $O$ 有极点，
因为 $M$ 首一且次数 $(p-3)/2$，极点阶准确为 $3+2(p-3)/2=p$。
它在三个不同的几何非零二挠点都为零，因为这些点的 $Y=0$，而好纤维使三根互异。
若 $H=p$ 且 $\chi$ 恒零，$g$ 还在 $p-1$ 个非零有理点全部为零；
这 $p-1$ 个点与三个几何二挠点不交，因为有理点群阶为奇数 $p$。
于是非零有理函数 $g$ 至少有 $p+2$ 个不同零点，却只有次数 $p$ 的极除子，矛盾。
若 $H=2p=10$ 且 $\chi$ 恒零，仅 $2p-1=9>p$ 个非零有理点已经给同样矛盾。
因此 $\chi$ 非零、像为整个加法群 $\mathbf F_p$，且

$$
|\ker\chi|=H/p\in\{1,2\}.
\tag{7}
$$

原点 $P=(0,T)$ 不是 $O$，且 $-P=(0,0)\ne P$，所以不是二阶。
在原三次上，$P$ 的切线斜率为 $-h$，第三交点为 $(T,T-hT)$，取逆得到
$2P=(T,0)$。因为 $T\ne0$，这不等于 $-P$，所以也不是三阶。
故 $d>3$，尤其原点不在阶至多二的核中。
由提升无关性，可以用原截面 $P$ 计算 $\chi(P(h_*))$，所以

$$
\mu(P)(h_*)=\chi(P(h_*))\ne0.
\tag{8}
$$

同时 $d\mid H$ 且 $d>3$，而 $H=p$ 或 $2p=10$，故 $p\mid d$。
本支既没有 $N_p$ 零值，也没有任何 prime-to-$p$ 的非空回返。

### Step 4. 唯一的 q=0 好点及全部允许倍数

若 $q(h_*)=0$，则 $h_*=9/8$。
好纤维条件及 [M] 的恒等式
$\delta(9/8)=(256T+27)^2/4096$ 强制 $256T+27\ne0$。
此时 $N_p(9/8)=b(9/8)^p/2\ne0$，且 [M] Step 6 已证明没有任何 $p\nmid n$ 的切触。
故 (PF) 两边均为假。若 $T=-27/256$，这个能级是坏点，不在本命题中；
该特殊时间的其他全部好点仍已由 Steps 1–3 覆盖，没有整体删去该时间。

最后，有限群中 $nP(h_*)=O$ 当且仅当 $d\mid n$。
若 $p\mid d$，所有 prime-to-$p$ 的 $n$ 都不相交。
若 $p\nmid d$ 且 $p\nmid n$、$n=md$，形式群乘法满足
$[m](w)=mw+O(w^2)$；$m$ 在 $R$ 为单位，所以代入非零 $w(dP)$ 保持其阶。
因此 $i_n=i_d$。结合前三步和 $q=0$ 分支，证明 (PF)。∎

## Corrections or missing assumptions

- 一阶系数 $\gamma$ 及 $\ell_0$ 必须在素域，才能把 $\wp_{A_*}$ 准确改写为乘以 $1-A_*$。
  在扩域中 $\gamma^p-A_*\gamma=0$ 可以有非零解，本文没有消除这项障碍。
- $A_*=1$ 不直接意味着原点有 $p$ 阶；本证明先算整个群的可能大小，再用原点小阶排除。
- 形式提升只用可分代数幂级数，源同态的使用通过实际有限函数域完成，不声称任意形式点自然在源 $E(K)$ 内。
- $\mu(P)(h_*)=0$ 是有理函数的单点值，不等于 $\mu(P)$ 恒零，也不推出原泛 $P$ 可被 $p$ 除。
- $N_p$ 根的重数没有被证明等于 $i_d-1$；特征 $p$ 对高阶项导数的消失尤其禁止这种自动推断。
- 坏纤维、$p$ 倍回返及原边界固定理想未由本件处理。

## Open risks and prior-art deduction

作者认为上述素域命题闭合；实际接受须等待 fresh 非作者核查，尤其是 Step 1 全导数常数项、
Step 3 有限可分提升的加法一致性、$p=5,H=10$ 与 $q=0$ 分支。
本件不预授独立数学 PASS 或候选四门任何分数。

本证明的主机制为 Manin 同态的一阶特化、有限群点数及 $p$-下降。
[V] 的准确 $Y M(X)$ 先例必须扣除；Hasse 界、极零次数、Hensel 提升和形式群亦均为标准工具。
新书面增量仅为将这些机制在本原 $T,h_*\in\mathbf F_p$ 上合成无幽灵零值的充要判据。
不能凭“充要”二字把这个短证明或与固定概形的标准消费者之和视为足够新的22–30页中心。

独立的作者有限排错 [F5] 已覆盖全部20组 $p=5$ 参数并给三处二阶证书，
但本证明不依赖其表格、样例或代码；也没有因该有限范围未见反例而扩大筛查范围。
本件没有运行新的质数／扩域采样，没有事后换阈值。

## Actual reading and verification boundary

主控本人 FULL 阅读 [M] 446行、其接受处置 [D] 148行，以及 [F5] 457行；
上述已接受模型识别只消费 [M]/[D] 的明确依赖，不借本件重开旧全文数学审查。
[UV] 本人实读 §2 的设置、定义、(2.2)–(2.3)、Proposition 2.3 陈述及完整证明；
本件只用好约化局部部分和同态公式，不使用其全局处处半稳定结论。
其官方HTML页头 v1日期2025-08-08、正文日期2026-08-24的差异保持原记录，不自行宣称另一个新版本。
[V] 作者托管PDF共7页，主控本人读完全文及参考文献，特别是p.2–3的下降同态及明确 $YM(X)$ 公式。
该PDF的最终期刊版本／年份本轮未锁定，因此本件只绑定作者托管原件，不凭文件名补造刊物元数据。
Voloch 1990 Proposition 1.3 仅从 [V] 看到准确转引，未据此冒称读过1990全文或原证明。

另本人打开 Broumas, *Effective p-descent*, Compositio Mathematica 107 (1997), 125–141 的官方PDF，
读到§4.2前段；它明载可分闭包上的等变同态，但首页适用素数的文本提取为 $p>5$。
本件的 $p>3$ 接口仍以 [UV] 的明确陈述和 [M] 已接受输入为准，没有用OCR猜测扩大Broumas范围。
此项来源旁证不是本件新增未经核对的证明依赖。

proof-writer 技能使本件保留准确素域量词、显式依赖和未闭合边界；没有因技能新增实验或暂停。
本文件使用 `apply_patch` 新增，不改冻结原件、接受处置、候选评分或源锁。
终态哈希在冻结交付时另报，不在文件内递归自载。

[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[D]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[F5]: PAPER31_QPI_MANIN_F5_EXACT_SCREEN_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S2
[V]: https://web.ma.utexas.edu/users/voloch/Preprints/disclog3.pdf
