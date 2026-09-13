# Proof Package：JR qPI 全阶实际临界四次与准确有限坏值

日期：2026-09-08。有界作者证明入口，非独立审查报告。
仅新增本文件；泛 Jacobian 稿、实际纤维稿及全部既有接受输入保持冻结。
不读取轨道消费者，不作轨道声明、评分、立项、稿件、PDF 或外部写操作。

## Claim

设 $k$ 是任意特征的代数闭域，$s,t\in k^*$，$s$ 的精确有限阶为 $r\geq1$。
正特征 $p$ 自动满足 $p\nmid r$。取实际八次吹起曲面 $S=S_{t,s}$，
原积分态射 $f=I_r:S\to\mathbb P^1_c$，及实际有限初值曲面
$U=S\setminus D=f^{-1}(\mathbb A^1_c)$。固定

$$
T=t^r,\qquad \varepsilon=(-1)^{r+1},\qquad
\delta(c,T)=c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27\varepsilon^2T.
$$

令 $Z_{\mathrm{act}}=Z(df)\subset U$，
$A_{\mathrm{act}}=\Gamma(Z_{\mathrm{act}},\mathcal O)$。
使用已接受的实际长度四结论定义首一四次

$$
R_{r,t,s}(C)=\det(C\operatorname{id}_{A_{\mathrm{act}}}-m_f),
$$

其中 $C$ 是写特征多项式时的形式变量，$m_f$ 是乘以原函数 $f$ 的算子。
则成立比所要求零集身份更强的全特征恒等式

$$
\boxed{R_{r,t,s}(C)=\delta(C,T).}
\tag{1}
$$

因此对每个有限 $c_0\in k$，

$$
\boxed{
f^{-1}(c_0)\text{ 不光滑}\quad\Longleftrightarrow\quad\delta(c_0,t^r)=0.}
\tag{2}
$$

由于已接受的有限纤维几何整、约化、算术亏格一，(2) 同时给出准确的几何亏格判据：
非根处为光滑亏格一；根处正规化亏格为零。无穷远重纤维不在本结论范围内。

另有明确的局部模型桥。令 $K=k(c)$，$E/K$ 为已接受的谱商 Jacobian。
它在原基底坐标 $c$ 上有 Weierstrass 方程

$$
W:\quad v^2+cuv-\varepsilon Tv=u^3-Tu^2.
\tag{3}
$$

对每个有限 $c_0$，在 $\mathcal R_0=k[c]_{(c-c_0)}$ 及其 henselization
$\mathcal R=\mathcal R_0^h$ 上，(3) 是最小整 Weierstrass 模型，判别式为

$$\Delta_W=T^3\delta(c,T).\tag{4}$$

实际模型 $S\times_{\mathbb P^1}\operatorname{Spec}\mathcal R$ 与
$W\times_{\mathbb A^1}\operatorname{Spec}\mathcal R$ 在选择一个局部截面后
同构为 $\mathcal R$-模型。这个同构保持原参数 $c$，且保留整个局部临界概形。

## Status

`PROVABLE AS STATED`。要求的 $V(R_{r,t,s})=V(\delta)$ 已闭合；
(1) 也有完整证明，而非由两个四次的相同次数或一般 $t$ 的比较推得。
无需排除特征 $2,3$、特殊非零 $t$，或缩小到小阶 $r$。
作者证明仍需真正非作者核查；本文状态不是非作者 PASS。

## Assumptions and frozen inputs

主控已明确传达 J、F 的真实独立接受；以下消费的是数学契约，不读取或复用审查投票。
源文件中旧“待独审／OPEN”文字作为冻结历史保留，不修改。

| ID | 输入 | SHA256 | 本件使用的契约 |
|---|---|---|---|
| J | [泛 Jacobian／torsor 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` | 原泛纤维 $X/K$ 是谱商 $E/K$ 的 torsor，$\operatorname{Jac}(X)\simeq E$；全部特征、每个 $t\ne0$ |
| F | [实际有限纤维与临界长度四](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` | Claim 1–5：所有有限纤维整约化、算术亏格一；坏纤维唯一奇点且正规化有理；实际临界长度四及 $R$ 的定义；$r=1$ 恒等式 |
| G | [原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` | 原 $f$ proper、flat、泛光滑；几何泛纤维光滑几何整、亏格一；实际有限模型是 $U$ |

本件不重审上述未变基础，不使用任何回返、轨道或未接受的坏值身份。
新关键是从泛 torsor 到逐个有限 DVR 模型的桥，而不是再次建立泛 Jacobian。

## Notation

- $c$ 始终是原 $I_r$ 的基底坐标；$C$ 只作特征多项式的形式变量。
- $x,y$ 保留为原动力坐标；$u,v$ 是 (3) 的 Weierstrass 坐标，避免混同。
- $W$ 是 (3) 在 $\mathbb P^2_{\mathbb A^1_c}$ 中的三次射影闭包，
  零截面为 $O_W=[0:1:0]$；不是仿射曲线本身。
- $g:W\to\mathbb A^1_c$ 是原参数投影。
- $\mathcal R_0,\mathcal R$ 如 Claim；$L=\operatorname{Frac}\mathcal R$，
  $\nu$ 是取值在 $\mathbb Z$ 的规范离散赋值，$\nu(c-c_0)=1$。
- $\operatorname{Fitt}_1$ 使用余核有两个生成元时的一阶子式理想规范。
- “好约化”指存在 proper smooth DVR 模型；不把可分扩张后的潜在好约化当作好约化。

## Sources actually read and prior-art deduction

本轮定向读取以下公开一手数学资料的指定陈述及证明；没有绕过访问限制。

| 来源 | 实际读取及适用范围 |
|---|---|
| [Stacks §55.8, tag 0C2R](https://stacks.math.columbia.edu/tag/0C2R) | 本章 $R$ 为任意 DVR；模型为 flat finite type；Definition 55.8.4 的最小正则 proper 模型排除第一类例外曲线；Lemmas 55.8.3、55.8.5 及 Proposition 55.8.6 |
| [Stacks §55.10, tag 0C9Y](https://stacks.math.columbia.edu/tag/0C9Y) | Lemmas 55.10.1–2 全部证明：光滑射影曲线、$H^0=K$、正亏格时最小正则模型唯一，任一正则 proper 模型向其有唯一收缩映射；无特征限制 |
| [Stacks Lemma 55.14.7, tag 0CDI](https://stacks.math.columbia.edu/tag/0CDI) | 全部证明：存在 proper smooth 模型等价于任意最小模型光滑；任意 DVR |
| [Conrad, Minimal Models for Elliptic Curves, 2015-11-21](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf) | §2 的任意 DVR 长 Weierstrass 定义、Theorem 2.8、Corollaries 2.9–2.10 及判别式变换；§3.10、§4.7 的模型关系作交叉核对。本文核心唯一性引用 Stacks，不用数域或短 Weierstrass 版 Tate 算法 |
| [Stacks Fitting ideals, tag 07ZA](https://stacks.math.columbia.edu/tag/07ZA) | Lemma 15.8.4，特别是 (3) 的任意基变换相容及其矩阵证明 |
| [Stacks henselization, tag 07QL](https://stacks.math.columbia.edu/tag/07QL) 及 [lifting, tag 07LW](https://stacks.math.columbia.edu/tag/07LW) | henselization 的 DVR／正则性保持、有限阶商不变；Lemma 15.9.14 的光滑点 étale 提升机制 |

另外定向查阅 Liu–Lu 的 [arXiv:1207.0569](https://arxiv.org/pdf/1207.0569)
§4.1–4.3，确认一般 DVR 的 Weierstrass 模型定义及最小性；未用其 Galois 同余主定理。
本地未发现相关最小模型文献 PDF，未配置新的文献工具或下载文件。

最小模型唯一性、Weierstrass 判别式变换及 Fitting 理想均是标准理论，必须扣除。
本件的实际对接是原参数上的 (3)–(4)、有限模型同构及四维临界代数求值，
不是新提出一般最小模型定理。没有作全球查新或正式价值评价。

## Proof Strategy

先求原谱商的长 Weierstrass 模型及其准确判别式。
用 $\nu(\Delta)\le4<12$ 的整数赋值论证核定整方程最小性。
进一步发现该模型的总曲面已经正则，且所有射影三次纤维整约化；
因此它本身就是每个有限 DVR 上的最小正则模型。
实际纤维有光滑点，henselian 局部提升给出截面，平凡化泛 torsor。
最小正则模型唯一性遂给真正的同基底模型同构，而非只比较泛曲线。
最后用内禀 Fitting 临界概形保留非约化长度，并直接计算 $W$ 的临界乘法矩阵。

## Dependency Map

1. (3)–(4)：已接受 J 的原谱商方程、可逆有理代换、长 Weierstrass 整系数不变量。
2. 有限 DVR 最小整方程：第 1 项、原 $c$ 的单首四次、判别式的十二次幂变换。
3. $W$ 为最小正则模型：实际总空间偏导、整三次纤维、纤维平方为零、Stacks 最小定义。
4. 实际局部模型与 $W$ 同构：F 的有限整约化输入、光滑点提升、J 的 torsor、正亏格模型唯一性。
5. 全阶 $R=\delta$：第 4 项的同基底同构、Fitting 临界概形基变换、下面的明确四维代数。
6. 好约化及坏值等价：第 3–5 项和 Stacks Lemma 55.14.7；不含任何轨道消费者。

## Proof

### Step 1. 原参数上的 Weierstrass 代换

J 给出 $E/K$ 的原方程

$$\Phi(Z,\lambda)=\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0.$$

在其函数域内置

$$u=\frac{\varepsilon TZ}{\lambda},\qquad v=\frac{\varepsilon T^2}{\lambda}.$$

逆式是

$$Z=\frac{Tu}{v},\qquad\lambda=\frac{\varepsilon T^2}{v}.\tag{5}$$

记 $F(u,v,c)=v^2+cuv-\varepsilon Tv-u^3+Tu^2$。
直接清分母得到

$$
\frac{v^3}{T^3}\Phi\left(\frac{Tu}{v},\frac{\varepsilon T^2}{v}\right)
=-\varepsilon F(u,v,c).
\tag{6}
$$

只使用 $\varepsilon^2=1$ 和 $T\ne0$，没有除以 $2,3$。
这给泛曲线双有理对应，延伸为光滑射影曲线同构。
原零点 $(Z,\lambda)=(0,0)$ 处 $\operatorname{ord}Z=1$、
$\operatorname{ord}\lambda=3$，故 $u,v$ 分别有极阶 $2,3$；
它映到 $O_W$。因此这是带原点的椭圆曲线同构。
整个代换只改变纤维坐标，$c$ 没有平移、缩放或分歧基变换。

### Step 2. 判别式与所有特征的十二次幂最小性

方程 (3) 的长 Weierstrass 系数为

$$a_1=c,\quad a_2=-T,\quad a_3=-\varepsilon T,\quad a_4=a_6=0.$$

因此

$$
b_2=c^2-4T,\quad b_4=-\varepsilon Tc,\quad
b_6=\varepsilon^2T^2,\quad b_8=-\varepsilon^2T^3.
$$

采用整系数公式

$$\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6,$$

逐项得到

$$
\begin{aligned}
\Delta
&=\varepsilon^2T^3(c^2-4T)^2
 +8\varepsilon^3T^3c^3-27\varepsilon^4T^4
 -9\varepsilon^3T^3c(c^2-4T)\\
&=\varepsilon^2T^3\bigl(c^4-\varepsilon c^3-8Tc^2
 +36\varepsilon Tc+16T^2-27\varepsilon^2T\bigr)
=T^3\delta(c,T).
\end{aligned}
\tag{7}
$$

在 $\mathcal R_0$ 或 $\mathcal R$ 上 $T$ 是单位，而 $\delta$ 是首一四次，故

$$0\le\nu(\Delta)=\operatorname{ord}_{c=c_0}\delta\le4<12.\tag{8}$$

任意两个定义同一带原点椭圆曲线的长 Weierstrass 方程，均由
$u=a^2u'+b$、$v=a^3v'+a^2du'+e$ 的可容许变换相连，
其中 $a\in L^*$；相应判别式满足 $\Delta=a^{12}\Delta'$。
这条长方程变换适用于所有特征；其整系数恒等式见上述 Conrad §2 的变换论证。

若存在判别式赋值更小的整方程，则 $\nu(\Delta')\ge0$，同时

$$0<\nu(\Delta)-\nu(\Delta')=12\nu(a)\le4,$$

与整数赋值矛盾。因此 (3) 在每个有限 DVR 上为最小整 Weierstrass 方程。
此处的 $12\nu(a)$ 是 $\mathbb Z$ 中的等式；特征 $2,3$ 下绝不把 $12$ 约成零。
也没有声称任意最小方程都必须满足赋值小于 $12$；这里只证明这一充分条件。

### Step 3. $W$ 的总曲面正则、全部有限纤维整约化

齐次式为

$$v^2w+cuvw-\varepsilon Tvw^2-u^3+Tu^2w=0.$$

无穷远 $w=0$ 只有 $O_W=[0:1:0]$，该处对 $w$ 的偏导为 $1$；
所以零截面在所有特征和所有 $c$ 上都相对光滑。
任意几何三次纤维若有两个分量，它们都必须与无穷远直线相交，
且交点只能是 $O_W$，这会使 $O_W$ 不光滑；重分量也会在该点破坏光滑性。
因而每个几何纤维只有一个不可约分量且其重数为一。
平面超曲面是 Cohen–Macaulay 的，没有嵌入分量，故整个纤维约化且几何整。
它是平面三次，算术亏格为一。
模型 projective；长 Weierstrass 关系给平坦性，也可由各纤维同一三次 Hilbert 多项式验证。

仿射图的相对偏导为

$$F_u=cv-3u^2+2Tu,\qquad F_v=2v+cu-\varepsilon T,\qquad F_c=uv.$$

纤维奇点不可能有 $u=0$：此时 $F=v(v-\varepsilon T)$，
在两个可能根处 $F_v$ 分别为 $-\varepsilon T,\varepsilon T$，均非零。
也不可能有 $v=0$：此时 $F=u^2(T-u)$；$u=0$ 已排除，
$u=T$ 则 $F_u=-T^2\ne0$。
因此每个纤维奇点都满足 $uv\ne0$，从而 $F_c\ne0$。
在这些点，绝对总空间由 Jacobian 判据光滑；在其余点，相对光滑也给绝对光滑。
所以

$$W\text{ 是光滑 }k\text{-曲面，特别是正则曲面。}\tag{9}$$

对每个有限 DVR 基变换，特殊纤维是唯一的竖直整曲线，
且作为完整重数一的主纤维有自交数 $0$。
它不能是自交数 $-1$ 的第一类例外曲线，因此没有可收缩的此类曲线。
由 Stacks Definition 55.8.4，$W_{\mathcal R_0}$ 和 $W_{\mathcal R}$
本身就是泛椭圆曲线的最小正则 proper 模型。
这比“最小 Weierstrass 方程”更具体；本件没有把两种最小性混为定义。

### Step 4. 实际模型的 henselian 截面与局部同构

固定一个任意有限 $c_0$，令

$$\mathscr X=S\times_{\mathbb P^1_c}\operatorname{Spec}\mathcal R.$$

$\mathcal R$ 是 DVR，剩余域仍为代数闭的 $k$，原参数 $c-c_0$ 仍为 uniformizer。
它由 $\mathcal R_0$ 作 ind-étale henselization 得到，没有分歧变换。
实际曲面的正则性在这里保持：有限层是 étale 基变换，
特殊闭点的完成局部环与原模型相同；泛纤维已经光滑。
等价地可用 henselization 的正则性保持性质。
proper、flat、finite type 由基变换保持，特殊纤维仍是原 $f^{-1}(c_0)$。

由 F，它是几何整且约化的曲线，因此有非空光滑开集。
选其中一点 $p\in f^{-1}(c_0)(k)$。因 flat 且该纤维在 $p$ 光滑，
$\mathscr X\to\operatorname{Spec}\mathcal R$ 在 $p$ 附近光滑。
光滑点具有到 $\mathbb A^1_{\mathcal R}$ 的局部 étale 坐标，可把 $p$ 的坐标取为零。
沿零截面拉回后得有 $k$-点的 étale $\mathcal R$-概形；
henselian 性给出提升截面。因此存在

$$e:\operatorname{Spec}\mathcal R\longrightarrow\mathscr X,\qquad e(k)=p.\tag{10}$$

这也可直接用 Stacks Lemma 15.9.14 的光滑点提升与 henselian 分裂性质。
我们只在 $\mathcal R$ 上选截面，不声称原 $k(c)$ 上有全局截面。

截面的泛点使原 torsor $X_L$ 平凡化。结合接受输入 J 和 (5)，有一个 $L$-同构

$$X_L\simeq E_L\simeq W_L.\tag{11}$$

实际 $\mathscr X$ 的特殊纤维只有一个重数一整分量，自交数为零，
所以它也不含第一类例外曲线，是最小正则 proper 模型。
(11) 的曲线光滑、射影、几何整，$H^0=L$，亏格为一。
这些恰满足 Stacks Lemmas 55.10.1–2 的全部假设，因而 (11) 唯一延伸为

$$\boxed{\mathscr X\simeq W_{\mathcal R}\quad\text{作为 }\mathcal R\text{-模型}.}\tag{12}$$

这里的 $\mathcal R$-线性尤其保持原 $c$。不同截面可给不同的泛平移，
但每次得到的模型同构都保持 $c$，故后续临界概形与长度的比较不依赖这种选择。
本件没有从泛 Jacobian 同构直接推断 (12)：(10)、双方正则性和相对最小性均不可缺少。

### Step 5. 同基底模型同构保留全部临界概形

对 $f:U\to\mathbb A^1$，定义

$$\mathcal I_{\mathrm{crit}}=\operatorname{Fitt}_1\Omega^1_{U/\mathbb A^1}.$$

在 $U$ 的光滑曲面坐标图中，相对微分有表示

$$\mathcal O\xrightarrow{df}\Omega^1_{U/k}\longrightarrow\Omega^1_{U/\mathbb A^1}\to0.$$

中间为秩二自由模，所以一阶 Fitting 理想正是 $df$ 两个坐标生成的理想。
它因而准确给出输入 F 的 $Z_{\mathrm{act}}$，不是重新定义另一种临界长度。
在 $W$ 的仿射 hypersurface 图上，

$$\Omega^1_{W/\mathbb A^1}
=\bigl(\mathcal O\,du\oplus\mathcal O\,dv\bigr)/(F_u\,du+F_v\,dv),$$

故其一阶 Fitting 理想为 $(F_u,F_v)$，无穷远零截面附近是单位理想。
记对应概形为 $Z_W$。

相对 Kähler 微分及 Fitting 理想与基变换相容；后者由表示矩阵子式即得，
也正是 Stacks Lemma 15.8.4(3)。因此 (12) 给出

$$Z_{\mathrm{act}}\times_{\mathbb A^1}\operatorname{Spec}\mathcal R
\simeq Z_W\times_{\mathbb A^1}\operatorname{Spec}\mathcal R.\tag{13}$$

这保留非约化结构，而非仅保留奇点集合。
对任何支撑于 $c_0$ 的有限长代数，其 $k[c]$-结构通过某个
$k[c]/(c-c_0)^N$ 因子化；henselization 满足

$$\mathcal R/(c-c_0)^N\mathcal R\simeq\mathcal R_0/(c-c_0)^N\mathcal R_0.$$

所以 (13) 保留相应 $k$-长度以及乘以 $c$ 的算子。
特别地，两个临界代数在每个有限 $c_0$ 的块具有同一特征多项式。
下一步直接证明 $Z_W$ 有限，并计算这些块的总乘积。

### Step 6. $W$ 的完整四维临界代数

由 Step 3，$Z_W$ 的全部支集在 $uv\ne0$ 的仿射开集中。
有限型概形的非空闭补集必有闭点，故这个开集包含整个临界概形，包括其非约化结构。
其代数由 $F=F_u=F_v=0$ 在 $u,v$ 可逆处给出。
从 $F_v=0$ 得

$$c=\frac{\varepsilon T-2v}{u}.$$

代入 $F=0$ 与 $uF_u=0$，分别得到

$$v^2=u^2(T-u),\qquad\varepsilon Tv=u^3.\tag{14}$$

这一步只除以单位 $u$；所有整数 $2,3$ 原样保留。
置 $z=v/u$，则 (14) 等价于

$$u=T-z^2,\qquad v=z(T-z^2),\qquad (T-z^2)^2=\varepsilon Tz.$$

因此令

$$q(z)=z^4-2Tz^2-\varepsilon Tz+T^2,\tag{15}$$

得到准确的概形同构

$$\boxed{Z_W\simeq\operatorname{Spec}k[z]/(q(z)).}\tag{16}$$

逆构造也合法：$q$ 的常数项 $T^2$ 非零，故商环中 $z$ 是单位；
又 $(T-z^2)^2=\varepsilon Tz$ 为单位，故 $u=T-z^2$ 及 $v=zu$ 也是单位。
以这些式子及上面的 $c$ 定义反向映射，代入 $F,F_u,F_v$ 全为零。
所以没有漏掉因消元除法排除的分支。

原基底函数在该商环中为

$$c=\frac{T}{z}-3z=\varepsilon-z-\frac{z^3}{T}.\tag{17}$$

最后一个等式直接来自 $q(z)=0$。
因为 $q$ 单首四次，(16) 是长度四的有限概形；不需要假设它约化或四根互异。
在基 $1,z,z^2,z^3$ 上，乘以 (17) 的矩阵为

$$
N_T=\begin{pmatrix}
\varepsilon&T&0&3T^2\\
-1&0&T&-3\varepsilon T\\
0&-3&0&-5T\\
-T^{-1}&0&-3&0
\end{pmatrix}.
\tag{18}
$$

四列分别由下列商环恒等式得到：

$$
\begin{aligned}
c\cdot1&=\varepsilon-z-T^{-1}z^3,\\
c\cdot z&=T-3z^2,\\
c\cdot z^2&=Tz-3z^3,\\
c\cdot z^3&=3T^2-3\varepsilon Tz-5Tz^2.
\end{aligned}
$$

为明确行列式核对，按 $CI-N_T$ 的第一行展开，三个非零项的余子式分别是

$$C^3-12TC+27\varepsilon T,\qquad C^2-3\varepsilon C-20T,
\qquad 12+C^2/T.$$

故

$$
\begin{aligned}
\det(CI-N_T)
&=(C-\varepsilon)(C^3-12TC+27\varepsilon T)
 +T(C^2-3\varepsilon C-20T)+3T^2(12+C^2/T)\\
&=C^4-\varepsilon C^3-8TC^2+36\varepsilon TC+16T^2-27\varepsilon^2T
=\delta(C,T).
\end{aligned}
\tag{19}
$$

这条恒等式在 $\mathbb Z[\varepsilon,T,T^{-1},C]$ 中成立，
因此在特征 $2,3$ 下仍包含全部非约化临界信息。

### Step 7. 原临界多项式、坏值及好约化的合取

输入 F 及 (16) 说明两边临界代数都有限。
有限维 $k[c]$-代数按有限支撑值分解成 Artin 块；
Step 5 在每个 $c_0$ 给这些块的同基底同构，故相应乘法算子的特征多项式逐块相等。
将全部块相乘，由 (19) 得

$$R_{r,t,s}(C)=\det(CI-N_T)=\delta(C,T),$$

即 (1)。这个论证保留每个实际局部长度；不是先证明零集再凭四次次数补上重数。
输入 F 的实际坏值判据立即给出 (2)。

还可把局部桥表为

$$
\begin{aligned}
f^{-1}(c_0)\text{ 光滑}
&\Longleftrightarrow W_{c_0}\text{ 光滑}
\Longleftrightarrow\delta(c_0,T)\ne0\\
&\Longleftrightarrow E_L\text{ 在 }\mathcal R\text{ 上有好约化}.
\end{aligned}
\tag{20}
$$

首项由 (12)；中项也可直接由 (16)–(19) 的临界支撑得到，
与长 Weierstrass 的判别式非零光滑判据吻合。
末项由 Step 3 的最小正则模型和 Stacks Lemma 55.14.7；
故不用额外假定 Tate 算法在特征 $2,3$ 的某张表。
对 $\mathcal R_0$ 本身，$W_{\mathcal R_0}$ 也是最小正则模型，
同一引理给原 DVR 上 $E$ 好约化当且仅当 $\delta(c_0,T)\ne0$。
这完成 Claim。$\square$

## Boundary checks

1. **$r=1$。** $s=1,T=t,\varepsilon=1$，(1) 恢复输入 F Claim 5 的原自治恒等式；
   本证明不靠该特例外推 $r>1$，所以没有循环。
2. **特征二。** $r$ 必为奇数，$\varepsilon=1$；
   $\delta=C^4+C^3+T$，$q=z^4+Tz+T^2$，
   全部单位条件仅用 $T\ne0$。步骤中没有除以二；十二次幂变换仍按整数赋值使用。
3. **特征三。** $3\nmid r$；$\delta=C^4-\varepsilon C^3+TC^2+T^2$。
   (14)–(19) 不除以三，允许临界重数；不会把实际 Jacobian 长度强定为特征零节点／尖点数。
4. **特殊非零 $t$ 与碰撞。** 每一步对固定任意 $T=t^r\ne0$ 成立，
   不需 $\delta$ 可分、无需把 $t$ 当超越元，也不经一般参数再延拓。
5. **原基底。** henselization 不改剩余点或 uniformizer 的赋值；
   (5)、(12)、(17) 均保持原 $c$，不存在未记录的基底重参数化。
6. **不平凡的全局 torsor。** 局部截面只是 (10)，不授予 $k(c)$ 上的全局截面；
   无穷远纤维 $rD$ 及其全局 torsor 障碍保持原状态。

## Corrections or Missing Assumptions

本 Claim 无待补的数学假设。更强结论 (1) 已明确证明，故本轮不把旧 F 的全阶接口
继续标作 OPEN；旧作者文件及其旧状态保留，不追改冻结内容。

必须保留的关键前提是：实际有限纤维几何整且约化、总模型正则、
泛 Jacobian 同构在原 $k(c)$ 上成立，以及 $t\ne0$。
如果删去有限约化性，光滑点可能不提升为当前重纤维的光滑截面，
且有限 torsor 可以有不同局部约化；本证明不能这样推广。

## Open Risks and scope

- 作者证明尚需新的非作者核查，重点为局部截面、双方最小正则模型、
  Fitting 临界概形身份和 (16) 的概形级双向消元。
- (1) 识别实际临界多项式，(4) 识别所列最小整 Weierstrass 判别式；
  两者相差固定单位 $T^3$，定义不同，不把它们无条件混称同一对象。
- 本件没有追加轨道、周期、回返平移点或奇异层分量作用的结论。
- 没有使用 $t$-族的临界有限平坦构造；无需为了本强等式另开该模块。
- 标准局部模型理论已扣除；没有新意／价值／页数／Route 评价或产物验收声明。

## Verification record

1. 全文读取指定 F 作者输入及必要 J 契约，验证两份冻结作者 SHA256 不变；未读审查票。
2. 自行读取上述 Stacks 模型定义、唯一性、好约化引理及完整证明，逐项核对任意 DVR、
   正亏格、$H^0=L$、正则 proper、无第一类例外曲线等条件。
3. 原谱方程代换、$b_i$ 判别式、四个乘法矩阵列及行列式 (19) 均用 SymPy 精确核对通过。
   正文保留全部消元、三余子式与整数恒等式；运行不替代证明。
4. 全文自查时区分动力 $x,y$ 与 Weierstrass $u,v$、基底 $c$ 与形式变量 $C$，
   检查特征 $2,3$、$r=1$、所有 $T\ne0$、非约化临界概形及无穷远排除。
5. proof-writer 约束精确量词和完整证明；research-lit 用于全特征模型定理与标准理论扣除。
   只新增本文件，未修改既有稿件、锁、PDF、实验或任何外部对象。
