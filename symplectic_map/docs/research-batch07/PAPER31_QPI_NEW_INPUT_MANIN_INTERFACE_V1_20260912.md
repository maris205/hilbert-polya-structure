# Proof Package：原 qPI 回返点的正特征 Manin 接口 V1

日期：2026-09-12 UTC。作者：`/root/p31_qpi_manin_interface_derivation_v1`。
数学标签：`AUTHOR_PROOF`；`route_applicability: NOT_APPLICABLE`。
本件仅为新实读来源在原对象上的有界接口推导，不是候选准入、fresh 独查、数学接受、实验或 PDF 验收。

## Claim

固定代数闭域 $k$，$\operatorname{char}k=p>3$，$T\in k^\times$，$K=k(h)$。
保留原自治同族曲线及原指定回返点

$$
W_h:\quad v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T).
$$

令

$$
\begin{aligned}
s&=h^2-4T, & q&=8h-9, & b&=2h^2-3h-8T,\\
\delta&=h^4-h^3-8Th^2+36Th+16T^2-27T,\\
c_4&=s^2+24hT, & c_6&=-s^3-36hTs-216T^2,\\
a_4&=-c_4/48, & a_6&=-c_6/864.
\end{aligned}
$$

用保留 $O$ 和原点标记的短 Weierstrass 坐标

$$
X=u+s/12,\qquad Y=v+(hu-T)/2,
\qquad X_P=s/12,\quad Y_P=T/2.
$$

对每个实际素数 $p>3$，在辅助不定元 $Z$ 中唯一分解

$$
(Z^3+a_4Z+a_6)^{(p-1)/2}
=Z^pM(Z)+AZ^{p-1}+L(Z),\qquad\deg_ZL<p-1.
$$

本件证明以下有界命题。

1. 原泛椭圆曲线满足 $j\notin K^p$。Ulmer–Voloch 所用的原模型接口准确为

   $$
   \boxed{\lambda=-\frac{q}{\delta}\,dh},\qquad
   \boxed{B=\frac{b}{2q}},\qquad
   \boxed{\mu(P)=\frac{T}{2}M(s/12)+B^p-AB}.
   $$

2. 对全部上述 $p,T$，$\mu(P)\ne0$，从而 $P\notin pW_h(K)$。
   该结论不由原点无限阶推断，而由本表达式的不可消极点或一个非零特殊值证明。

3. 实际多项式

   $$
   \boxed{N_p(h):=q^p\mu(P)
   =\frac12\left(Tq^pM(s/12)+b^p-Abq^{p-1}\right)}
   \tag{N}
   $$

   属于 $k[h]\setminus\{0\}$，且 $\deg_hN_p\le2p$。
   令 $\iota_n(h_*)=(nP.O)_{h_*}$ 为椭圆曲面上原两截面的局部交数。
   对每个正整数 $n$ 且 $p\nmid n$，在每个有限好纤维 $\delta(h_*)\ne0$，

   $$
   \iota_n(h_*)>1\ \Longrightarrow\ N_p(h_*)=0.
   \tag{F}
   $$

   若 $256T+27\ne0$，唯一有限好约化 $\lambda$ 零点 $h_*=9/8$
   实际不可能满足 $\iota_n(h_*)>1$。

4. 因此

   $$
   \mathcal C_{p,T}:=
   \{h_*\in k:N_p(h_*)=0\}\cup
   \{h_*\in k:\delta(h_*)=0\}\cup\{\infty\}
   \tag{C}
   $$

   是对所有 $p\nmid n$ 的原切触位置的共同有限必要候选集，
   $|\mathcal C_{p,T}|\le2p+5$；这里只给未优化上界。
   有限好纤维中的候选位置至多 $2p$ 个。
   该集合不是全部接触的精确分类，也不是全部非空交点 $nP\cap O$ 的有限列表。

## Status

`PROVABLE AS STATED`，仅针对上述明确的有界命题 1–4。
原曲线、底域、固定时间和指定回返点均未修改；未增加一般时间假设以删除特殊值。
“$\mu(P)=0$ 与切触充要”“所有 $n$ 包括 $p\mid n$”“坏纤维逐一分类”不在命题内，亦未证明。

## Assumptions

- $k$ 代数闭且 $p>3$；因此本文分母中的 $2,3$ 均可逆，整数 $8$ 不被 $p$ 整除。
- $T\in k^\times$ 固定；所有 $d$ 及撇号只对基变量 $h$ 微分，$dT=0$。
- 原曲线与原回返点身份沿用 [BASE] §1–2 及 [RETURN] §3.1–3.3 的已接受接口。
  本件不重新证明原完整曲面、torsor 作用、四末端线或全有限状态识别。
  原泛回返非挠亦沿用该基线，因此 $nP\ne O$ 于泛纤维；不从非挠性推出非 $p$ 可除性。
- 采用 [UV] §2 的 $(2.2),(2.3)$ 及 $\mu:E(K)/pE(K)\hookrightarrow K$ 的接口。
  本件先实际验证 $j\notin K^p$；不以“非恒定”替代该条件。
- 只使用 [UV] Proposition 2.3 的**好约化局部证明**；不全局套用其“处处半稳定”前提。
  尤其特殊 $T=-27/256$ 时，不把碰撞纤维未经核对就当作乘法约化或宣称处处半稳定。

## Notation

- $E=W_h/K$ 表示原曲线的泛纤维；$O$ 是原无穷远零点。
- $Z$ 是分解 $M,A,L$ 时的独立多项式变量，$X_P=s/12$ 是实际原点坐标，二者不混同。
- $\Delta=T^3\delta$，$j=c_4^3/\Delta$；$A,M,L$ 均依赖当前实际素数 $p$。
- $\wp_A(z)=z^p-Az$，$\mu(P)$ 是本短模型中源公式的有理函数值。
- $\eta=d_{\rm rel}X/(2Y)$ 是相对不变微分。
  $dX_P/(2Y_P)$ 是将点坐标对底 $h$ 微分所得的基微分，不是 $\eta$ 的混写。
- $\nu(Q)=\mu(Q)\lambda\eta^{p-2}$ 是源文的模型无关扭曲截面；
  在有限好纤维本模型中 $\eta$ 为局部基，故可用系数的赋值计算其阶。
- 局部交数 $\iota_n>1$ 才称本件中的切触；$\iota_n>0$ 只表示非空接触。

## Proof Strategy

先以整数多项式恒等式化简原短式和 $\lambda,B$，再将源式标准代入原点。
普通时间在一个有限好点发现 $B$ 的简单极点，直接排除 $\mu$ 恒零；
唯一例外时间先约消 $B$，再在其奇异参数处评价正则多项式来证明 $\mu\ne0$。
最后重述并核对源文好约化局部估计，得到原切触的必要多项式条件。

## Dependency Map

1. 原对象身份依赖 [BASE]、[RETURN] 的既有接受，不依赖本次新计算。
2. $j\notin K^p$ 依赖 $c_4,\delta$ 的首项与 $p\nmid8$。
3. $\lambda,B$ 依赖本文两条整数多项式恒等式与源公式；不依赖任何小 $p$ 样本。
4. $\mu\ne0$ 依赖 $A,M(X_P)\in k[h]$、特征 $p$ 的极阶，及特殊时间的准确评价。
5. $P\notin pE(K)$ 依赖源文的商群接口与已证 $\mu(P)\ne0$；不用高度、$I_8$ 分量或非挠性推断。
6. 有限筛选依赖第 4 项、$N_p$ 的次数界，以及 Proposition 2.3 好约化证明的局部结论。
7. 有限坏纤维和无穷远仅加入候选集，不以它们的未分类行为支持好纤维论证。

## Proof

### Step 1. 原短式、判别式及非 $p$ 次幂条件

完成平方后，原式成为

$$
Y^2=u^3+\frac{s}{4}u^2-\frac{hT}{2}u+\frac{T^2}{4}.
$$

代入 $u=X-s/12$，逐项展开给出 $Y^2=X^3+a_4X+a_6$，
且原 $P$ 准确送至 $(s/12,T/2)$。这是带标记的坐标变换，不是另选椭圆曲线或另一点。
直接展开还给出整数恒等式

$$
c_4^3-c_6^2=1728T^3\delta.
$$

故判别式为 $\Delta=T^3\delta\ne0$，因为 $\delta$ 对 $h$ 是首一四次式。
泛纤维因此光滑。$c_4$ 对 $h$ 首一且次数为 $4$，所以

$$
\operatorname{ord}_{\infty}(j)=-(12-4)=-8.
$$

若 $j=f^p$ 且 $f\in K$，则每个离散赋值下 $\operatorname{ord}(j)=p\operatorname{ord}(f)$；
这与 $p>3$ 且 $p\nmid8$ 矛盾。因此 $j\notin K^p$。
源文的非 $p$ 次幂前提已在原对象上核定。

### Step 2. 准确化简 $\lambda$

由于 $T$ 为常数，$d\Delta/\Delta=(\delta'/\delta)dh$。
源式中的 $a_4/(18a_6)=c_4/c_6$，而

$$
\frac{dj}{j}
=\left(\frac{3c_4'}{c_4}-\frac{\delta'}{\delta}\right)dh.
$$

以下恒等式在 $\mathbb Z[T,h]$ 成立，可由所列多项式逐项展开验证：

$$
3c_4'\delta-c_4\delta'=-q c_6.
\tag{I1}
$$

它给出 $\lambda=-q\,dh/\delta$。
这在 $K\,dh$ 中是恒等式，所以 $c_4=0$ 或 $c_6=0$ 的有限值并不自动成为真实例外；
未约消原式中的表面分母不得误记为 $\lambda$ 的极点。
在有限好开集 $\delta\ne0$ 上，$\lambda$ 正则，唯一可能的零点是 $h_0=9/8$。

### Step 3. 准确化简 $B$ 并得到原 $\mu(P)$

源式 $(2.3)$ 在原点上的内部参数为

$$
B=\frac{dX_P/(2Y_P)}{\lambda}
-\frac{12X_P^2+((d\Delta/\Delta)/\lambda)X_P+8a_4}{12Y_P}.
$$

这里

$$
\frac{dX_P}{2Y_P}=\frac{h}{6T}dh,
\qquad
\frac{d\Delta/\Delta}{\lambda}=-\frac{\delta'}q.
$$

由此将 $B$ 通分为

$$
B=\frac{-12h\delta+s\delta'+q(2c_4-s^2)}{72Tq}.
$$

第二条整数多项式恒等式为

$$
-12h\delta+s\delta'+q(2c_4-s^2)=36T(2h^2-3h-8T).
\tag{I2}
$$

故 $B=b/(2q)$。源 $(2.3)$ 给出 Claim 1 中的 $\mu(P)$，并且

$$
B=\frac h8-\frac3{64}-\frac{256T+27}{64(8h-9)}.
\tag{Bsplit}
$$

所有上述有理恒等式仅以 $2,3,T$ 和明确的多项式作分母，
故在每个 $p>3,T\ne0$ 下成立；没有通过小素数模式外推。

### Step 4. 全部时间的非零性及真正的 $p$ 可除性结论

首先，$a_4,a_6,X_P\in k[h]$，所以多项式展开定义保证 $A,M(X_P)\in k[h]$。
令 $c=256T+27$。直接代入得

$$
\delta(h_0)=\frac{c^2}{4096},\qquad b(h_0)=-\frac c{32}.
$$

**分支一：$c\ne0$。** 此时 $h_0$ 为好纤维。
由 (Bsplit)，以 $z=h-h_0$ 为局部参数，$B$ 的主部为 $-c/(512z)$。
$B^p$ 因而有准确 $p$ 阶极点；$-AB$ 的极阶至多为 $1$，$Y_PM(X_P)$ 正则。
因为 $p>1$，后两项不可能消去第一项的最高极部，故

$$
\operatorname{ord}_{h_0}\mu(P)=-p,\qquad\mu(P)\ne0.
\tag{NZ1}
$$

**分支二：$c=0$，即 $T=-27/256$。** 此值仍非零，因为 $p>3$。
先在 $k(h)$ 中约消得

$$
B=\frac{8h-3}{64},\qquad
\delta=\frac{(8h-9)^2(64h^2+80h+153)}{4096}.
$$

因此 $\mu(P)\in k[h]$。
在 $h=h_0$ 处，准确数值为

$$
a_4=a_6=0,\qquad X_P=(3/8)^2,\qquad
Y_P=-(3/8)^3,\qquad B=3/32.
$$

在此参数下辅助多项式为 $Z^{3(p-1)/2}$；因 $p>3$，其唯一项次数不等于 $p-1$，
且 $3(p-1)/2\ge p$。所以

$$
A(h_0)=0,\qquad M_{h_0}(Z)=Z^{(p-3)/2}.
$$

利用特征 $p$ 的 $(a-b)^p=a^p-b^p$，得到

$$
\mu(P)(h_0)
=-(3/8)^p+(3/32)^p
=(-9/32)^p\ne0.
\tag{NZ2}
$$

这里仅评价已经正则的多项式，目的是证明它不恒零；
**没有**在 $h_0$ 的奇异纤维上另定义椭圆 Manin 映射或调用好约化命题。
两分支覆盖全部 $T\in k^\times$。
由于源接口使 $\mu$ 在商 $E(K)/pE(K)$ 上定义，$P\in pE(K)$ 会强制 $\mu(P)=0$；
(NZ1)–(NZ2) 排除该可能。这是实际非 $p$ 可除性证明，不是“无限阶”的同义改写。

### Step 5. 多项式清分母及统一有限次数界

在特征 $p$ 中 $2^p=2$，将 Claim 1 的表达乘以 $q^p$ 就得到 (N)。
第 4 步证明 $\mu(P)\ne0$，且 $q\ne0$，所以 $N_p\ne0$。

对次数界，给 $Z,a_4,a_6$ 权分别为 $2,4,6$。
$(Z^3+a_4Z+a_6)^{(p-1)/2}$ 每项总权为 $3(p-1)$。
于是 $A$ 的总权为 $p-1$，$M(Z)$ 的总权为 $p-3$。
由于 $\deg_ha_4\le4$、$\deg_ha_6\le6$、$\deg_hX_P=2$，逐单项式得到

$$
\deg_hA\le p-1,\qquad\deg_hM(X_P)\le p-3.
$$

因此 (N) 的三项次数分别至多 $2p-3,2p,2p$，故 $\deg_hN_p\le2p$。
特殊时间可先消去 $q^p$，此时 $\deg_h\mu(P)\le p$；不需要此改进来证明统一上界。
对每个实际 $p$，按给定的有限多项式展开计算 $A,M$ 即可构造 $N_p$；
这是精确代数算法，不声称存在与 $p$ 无关的固定次数多项式。

### Step 6. 只在好约化处使用源文的局部切触估计

取有限好点 $h_*$，以 $z=h-h_*$ 为局部参数，令 $\ell=\operatorname{ord}_{h_*}\lambda\ge0$。
假设 $p\nmid n$ 且 $\iota=(nP.O)_{h_*}>1$，置 $Q=nP$。
源映射是加法群同态，故 $\nu(Q)=n\nu(P)$；$n$ 在 $k$ 中非零，二者赋值相同。

在本好约化短模型中，$\eta$ 为局部基，$Q$ 的坐标 $x,y$ 满足
$\operatorname{ord}(x)=-2\iota$、$\operatorname{ord}(y)=-3\iota$。
具体地，$O$ 附近的参数 $w=-x/y$ 具有 $x=w^{-2}(1+O(w))$、
$y=-w^{-3}(1+O(w))$ 的整形式展开，而 $\operatorname{ord}(w(Q))=\iota$。
源证明使用的代数消去可直接写成

$$
\begin{aligned}
R&:=yM(x)-\wp_A\left(\frac{x^2}{y}+\frac{2a_4}{3y}\right)\\
&=\wp_A\left(\frac{a_4x+3a_6}{3xy}\right)-\frac{yL(x)}{x^p}.
\end{aligned}
$$

其理由是 $yM(x)=\wp_A(y/x)-yL(x)/x^p$，再用 $y^2=x^3+a_4x+a_6$ 相减。
因 $a_4,a_6,A$ 在此整，右侧第一项赋值至少 $3\iota$；
$\deg L\le p-2$ 使第二项赋值至少 $\iota$，从而 $\operatorname{ord}(R)\ge\iota$。
此外

$$
\operatorname{ord}\left(\frac{dx}{2y}\right)\ge\iota-1,
\qquad\operatorname{ord}\left(\frac{d\Delta}{\Delta}\right)\ge0.
$$

将 $(2.3)$ 分解成 $R$ 与其余两个 $\wp_A$ 项，再乘以 $\lambda$，
相应赋值下界分别为

$$
\iota+\ell,\quad
\min\{p(\iota-1)-(p-1)\ell,\ \iota-1\},\quad
\min\{p\iota-(p-1)\ell,\ \iota\}.
$$

使用 $\iota\ge2$、$\ell\ge0$，三者均至少为

$$
\operatorname{ord}_{h_*}\nu(P)\ \ge\
\begin{cases}
1,&\ell=0,\\
p-(p-1)\ell,&\ell>0.
\end{cases}
\tag{G}
$$

这给出了 [UV] Proposition 2.3 所需的好约化局部蕴含，
也说明本步没有使用曲面其他位置的半稳定性。

若 $\delta(h_*)q(h_*)\ne0$，则 $\ell=0$，$\lambda$ 为单位乘 $dh$，
(G) 迫使 $\mu(P)$ 在该点为零，即 $N_p(h_*)=0$。
若 $q(h_*)=0$ 且仍为好纤维，则 $c\ne0$、$h_*=h_0$、$\ell=1$。
但 (NZ1) 给出

$$
\operatorname{ord}_{h_0}\nu(P)=-p+1,
$$

而切触的 (G) 要求其至少为 $1$，矛盾。
同时 $N_p(h_0)=b(h_0)^p/2\ne0$，故该排除与统一筛选式完全一致。
若 $c=0$，$h_0$ 本身是坏点，未落在本步的好开集中。
由此证明 (F)。

### Step 7. 有限候选集及其不可倒置性

非零 $N_p$ 至多有 $2p$ 个不同根，$\delta$ 至多有 $4$ 个不同根。
每个不在 (C) 中的基点都是有限好点且 $N_p$ 非零，因而由 (F) 不存在任何 $p\nmid n$ 的切触。
加入无穷远仅再加一个点，所以 (C) 与 $2p+5$ 的上界成立。

本件未在有限坏纤维或无穷远计算局部交数，故它们保留为候选，不能报成已分类。
$N_p(h_*)=0$ 只通过必要方向得到；本证明既不保证该点存在 $n$ 使 $nP=O$，
也不保证接触阶大于 $1$。当 $p\mid n$ 时 $\mu(nP)=0$，
第 6 步“乘以 $n$ 不改变赋值”的论证失效；因此不扩张到这种 $n$。
Claim 1–4 在所列范围内成立。∎

## Corrections or Missing Assumptions

- 原有限回返身份未变；短式只是保留原 $P$ 的计算坐标，不是替换系统。
- 特殊时间 $T=-27/256$ 已单独证明 $\mu\ne0$，没有暗加 $256T+27\ne0$。
- $j\notin K^p$ 与 $P\notin pE(K)$ 均实际验证；原已知非挠性不充作后者前提。
- 源 Proposition 2.3 的全局半稳定前提未擅自删除；本件明确重证仅依赖好约化的局部部分。
- 此处 $\lambda$ 的有限好点零阶由本整模型计算。
  非最小全局短坐标中裸 $\lambda$ 在无穷远的阶不能直接当作扭曲截面 $\lambda\eta^{-2}$ 的阶；
  本件将无穷远保留为候选，不用这种混淆作推理。

## Open Risks

- 尚无本文件的 fresh 非作者检查；作者辅助核算不改 `AUTHOR_PROOF` 标签。
- 未证明 $N_p$ 根的精确切触意义、全部接触阶、$p$ 倍截面行为、坏纤维分类或点阶闭式。
- 全 $p$ 统一表达、非零性和有限必要筛选来自源接口的实际标准代入及短局部计算。
  它们不自动形成新长文中心，不给新意、独立价值、自然页数或正式候选任何预通过。
- 未打开原 §2 引用的上游文献 [1]/[7]/[9] 原文；本件实际依赖所读 [UV] 明载接口。
  这项读取范围不能改写成已逐一审查所有上游定理。

## 实读来源、验证与 SHA-256

### 实读来源身份

[UV] 为 [Ulmer–Voloch 官方 HTML：New unlikely intersections on elliptic surfaces](https://arxiv.org/html/2508.06680v1#S2)，
本次于 2026-09-12 实读 §2 的设置、$M,A,L$ 定义、$(2.2)$、Lemma 2.1、
$\mu$ 接口及 $(2.3)$、Proposition 2.3 陈述与完整证明，重点使用其中好约化局部证明。
工具文本定位为 §2 开始至 Proposition 2.3 证明结束（页面归一化行 79–174）；
另核对页面页头（行 36）与正文 Date（行 43），不冒称全文实读。
页面页头标 `arXiv:2508.06680v1 [math.AG] 08 Aug 2025`，正文却标 `August 24, 2026`。
本记录绑定“2026-09-12 实读的官方 HTML 指定范围”，不自行解释日期差，也不称其为已锁定的新版本。
同日 11:33 UTC 成功获取的完整 HTML 字节流 SHA-256 为
`9ddffdf28e3e042c7c02ab00f2a4b40c09b11a4ded4bde1e3da94a86c0753f58`。
该流只作身份哈希、未保存为新增源文件；哈希覆盖整响应不代表本人全文读取。

| 本次本人输入 | 实读范围 | SHA-256 |
|---|---|---|
| [BASE] | FULL，121 行 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [RETURN] | FULL，167 行 | `9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce` |
| [工作流](../WORKFLOW.md) | FULL，39 行 | `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2` |
| [批次入口](../../BATCH_07_CONTEXT.md) | PARTIAL，1–100 行，仅状态 | `ff4b3185421c0da70262ee1396dd7889600eb0f4f64ce22f323bd220cdb32348` |
| `proof-writer/SKILL.md` | FULL，223 行 | `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe` |

技能完整路径为 `/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md`。
该技能使本件固定准确量词、依赖图、两个特殊分支和不成立的逆命题；未触发停止或额外科学约束。

### 实际有限代数校验

本次用 SymPy 对 $\mathbb Q[T,h]$ 中的五个有限表达作精确通分/展开：
判别式恒等式、(I1)、(I2)、$\delta(9/8)$ 及 (Bsplit)，差值均准确为零。
另准确核对特殊时间的 $a_4,a_6,X_P,Y_P,B$ 五个值及 $\delta$ 因式分解。
这些只是已写整数恒等式的转录校验；证明的全特征结论来自公式，未运行任何小 $p$ 样本归纳。
未创建实验项目、脚本、输出集、候选阈值、论文源或 PDF。

并行作者辅助 `/auxiliary_algebra_check` 只回传消息，未写文件；
它另行核对同样两条恒等式与特殊时间评价，并委派了一项仅回消息的特殊值辅助核算。
所有这类贡献均计入作者侧核算，不称 fresh 独查、正式数学票或跨模型证据。

## 终态边界

本任务唯一写入本文件；其他工作区文件只读。
未改任何旧接受、失败、来源锁、候选评分、索引或批次状态，未重开已通过阶段。
未扫描旧构建树，未运行新实验、编译、投稿、上传、推送、外发消息或付费服务。
交付文件的终态 SHA-256 由写入后实际哈希单独回报，避免自包含哈希循环。

[BASE]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[RETURN]: PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md
[UV]: https://arxiv.org/html/2508.06680v1#S2
