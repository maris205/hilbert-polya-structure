# Proof Package：JR 原泛纤维与循环谱商的准确 Jacobian／torsor 桥

日期：2026-09-08。作者证明入口，非独立审查票。
仅新增本文件；不修改基础证明、其他作者文件、项目、锁、稿件、PDF 或实验。
科学状态：`PROVABLE AS STATED`，限于下述泛纤维命题；尚需真正非作者核查。

## Claim

设 $k$ 是域，$s,t\in k^*$，$s$ 的精确有限阶为 $r\geq1$。
正特征 $p$ 自动满足 $p\nmid r$。令 $K=k(c)$，其中 $c$ 是超越元，记

$$
T=t^r,\qquad \varepsilon=(-1)^{r+1},\qquad n=2r.
$$

令 $X/K$ 是实际 JR Laurent 方程 $I_r(x,y;t,s)=c$ 的光滑射影模型。
其光滑、几何整、亏格一身份采用已接受的原始泛纤维证明；在非代数闭 $k$ 上，
这些性质由基变换到代数闭包后的同一结论下降。
令 $E/K$ 是下述方程的自然光滑射影完备化，并选择 $O=(Z,\lambda)=(0,0)$ 为零元：

$$
E:\quad \lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0.
\tag{1}
$$

则有一个在原参数 $t,s,c$ 上定义的 $E$-torsor 结构于 $X$，并有 $K$-同构

$$
\boxed{\operatorname{Jac}(X)\simeq E.}
\tag{2}
$$

准确的桥由原单周期 Lax 矩阵的谱线丛给出：若 $C/K$ 是原 $z$ 谱曲线，
$\pi:C\to E$ 是 $Z=z^r$ 的循环商，则存在 $K$-态射

$$
\alpha:X\longrightarrow\operatorname{Pic}^{n}(C)
\tag{3}
$$

使 $\alpha$ 将 $X$ 同构到 $\pi^*\operatorname{Pic}^0(E)$ 的一个几何平移陪集。
群同态 $\pi^*:\operatorname{Pic}^0(E)\to\operatorname{Pic}^0(C)$ 本身是闭浸入，
不是仅仅一个未知核的同源。因此，对任意几何点 $P_*\in X(\bar K)$，有同构

$$
X_{\bar K}\xrightarrow{\ \sim\ }E_{\bar K},\qquad
P\longmapsto(\pi^*)^{-1}\bigl(\alpha(P)\otimes\alpha(P_*)^{-1}\bigr),
\tag{4}
$$

右边再用 $Q\mapsto\mathcal O_E(Q-O)$ 识别 $E$ 与其 $\operatorname{Pic}^0$。
若 $P_*$ 在 $K$ 上有理，则 (4) 在 $K$ 上定义；否则不把 torsor 擅自平凡化。

此命题覆盖特征 $2,3$，对每个非零固定 $t$ 成立。
它不声称所有特殊有限纤维光滑，不由谱判别式直接给出动力坏纤维，
不确定回返平移点、坏纤维分量作用或全部有限域轨道结论。

## Status

`PROVABLE AS STATED`，原 Jacobian／torsor 泛纤维目标无需缩小到奇特征。
证明不把同亏格当作同构，也不把 $g(C)=2r-1$ 混为实际 $g(X)=1$。
下面的逆重建证明给出有理逆，特意排除正特征下“几何点泛单射但纯不可分次数大于一”的漏洞。

## Assumptions and accepted inputs

本件已读取以下指定文件；其已接受且未变部分只作输入，不重审。

| 输入 | 使用范围 |
|---|---|
| [入口接受处置](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) | 原始模型、四份证明的实际接受状态及当前开放边界 |
| [谱商入口 S](PAPER30_QPI_SPECTRAL_QUOTIENT_ENTRY_V1_20260908.md) | 原谱方程、循环商、非二特征非退化光滑模型；不预设 Jacobian 桥 |
| [原始亏格一桥 G](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 实际 $I_r=c$ 几何泛纤维光滑、几何整、射影、亏格一；每个 $t\ne0$、全部特征 |

S 的 SHA256 为 `049941aad912cabc3788d8063ba3cec20d3f7a863a2ef50e3d29e1747d3e3738`；
G 的 SHA256 为 `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace`。
其基础 P、N 的接受由入口处置给出；本件不依赖任何本轮尚未证的坏纤维或回返结果。

## Source scope and prior-art deduction

实际读取 [Joshi–Roffelsen 作者 v2](https://arxiv.org/html/2508.18578v2)，
§3.1 的 $A(z)$、$M(z)$、积分定义与循环 intertwining 恒等式，以及 §3.2 全节。
原积分、单周期特征多项式和谱奇点四次式均来自 JR，不计作本件新发现。
JR §3.2 没有给出本件所需的谱线丛逆重建和循环商 Jacobian 识别；
本件不把该节关于谱奇点产生动力奇点的叙述当成已证输入。

另外实际读取 [Beauville, Acta Math. 164 (1990), 211–235](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6443-11511_2006_Article_BF02392754.pdf)
的引言、§1.1–1.4、§1.7–1.12，特别是 Theorem 1.4 的谱模／常数共轭对应。
“多项式矩阵固定特征多项式对应谱曲线 Picard 开集”是既有标准理论，不能算本件的新理论。
该文按复数域陈述；为不暗中外推其特征条件，下面只使用并直接证明本题需要的秩二模构造、
常数共轭重建及其族版本。本件自己的模型对接是实际 $M$ 的两条端点系数恢复 $x,y$，
以及循环差的固定除子与无核下降。

有限检索还核对到 BNR 1989 的原出版元数据与作者文献入口；未将其更一般模空间结论
另作本证明的假设。没有在本地发现题名相关的 qPI／Beauville PDF，
未配置可用的 Zotero／Obsidian 来源；arXiv 查询采用公开检索回退，没有下载文件。
以上是有界一手来源核对与标准理论扣除，不是全球查新、价值或篇幅评分。

## Notation

- $\tau:C\to\mathbb P^1_z$ 是原谱曲线的次数二投影；$\pi:C\to E$ 是次数 $r$ 的商。
- $\sigma:C\to C$ 为 $(z,\lambda)\mapsto(sz,\lambda)$；$G=\langle\sigma\rangle$。
- $P_0,P_T$ 是 $C$ 上 $z=0$、$\lambda=0,T$ 的点。
- $Q_2,Q_1$ 是 $z=\infty$ 上 $\mu=\lambda z^{-n}$ 分别为 $1,0$ 的点。
  下标表示 $\lambda$ 的极阶分别为 $2r,r$，不是分歧指数。
- $J_C=\operatorname{Pic}^0(C)$，$J_E=\operatorname{Pic}^0(E)$。
- $M_j=[z^j]M(z)$；固定投影矩阵记为 $P=\operatorname{diag}(1,0)$。

## Proof Strategy and Dependency Map

1. 在所有特征建立本题所需的光滑谱模型；非二特征采用 S，特征二用原二次方程补证。
2. 给原 $M$ 定义 $\tau_*L=\mathcal O^{\oplus2}$ 的谱线丛，从而得到 (3)。
3. 从谱线丛恢复 $M$ 的常数共轭类，再由 $M_n,M_{n-1},M_0$ 恢复原 $x,y$，得到有理逆。
4. 用 $A:L\dashrightarrow\sigma^*L$ 的固定除子证明所有谱线丛差落在循环不变 Picard 群。
5. 用全群固定点排除 $\pi^*$ 的核；用 tame 平均算出不变群的单位分支恰为 $\pi^*J_E$。
6. 几何连通的 $X$ 像为一个完整陪集；有理逆使其为同构，随后下降 torsor 作用及 Jacobian。

## Proof

### Step 1. 原 Lax 数据及两个谱模型

保留 JR 的辅助规范参数 $w\ne0$，写

$$
A(z)=A_0+zA_1+z^2P,
$$

$$
A_0=\begin{pmatrix}
t+x-xy&-wx\\
w^{-1}(t+x-ty-2xy+xy^2)&x(y-1)
\end{pmatrix},
$$

$$
A_1=\begin{pmatrix}
y-x+x/y-1-t/x&w\\
w^{-1}(y-2x-1+xy+x/y-t/x)&1
\end{pmatrix}.
\tag{5}
$$

不同 $w$ 由常数对角共轭相连，故谱线丛的同构类与 $w$ 无关；构造族时可固定 $w=1$。
原积分与单周期矩阵为

$$
M(z)=A(s^{r-1}z)\cdots A(sz)A(z),\qquad
I_r=\operatorname{tr}M(1)-(T+1).
\tag{6}
$$

JR 的实际恒等式为

$$
\det A(z)=z^3,\qquad
\operatorname{tr}M(z)=T+I_rz^r+z^{2r},\qquad
\det M(z)=\varepsilon z^{3r},
\tag{7}
$$

$$
M(sz)A(z)=A(z)M(z).
\tag{8}
$$

于 $I_r=c$，原谱曲线是

$$
C:\quad\lambda^2-(T+cz^r+z^{2r})\lambda+\varepsilon z^{3r}=0.
\tag{9}
$$

其无穷远图令 $v=z^{-1},\mu=\lambda z^{-2r}$，则

$$
\mu^2-(1+cv^r+Tv^{2r})\mu+\varepsilon v^r=0.
\tag{10}
$$

在 $v=0$ 的两点 $\mu=0,1$，对 $\mu$ 的偏导分别为 $-1,1$，所有特征均非零。
在 $z=0$ 的两点 $\lambda=0,T$，相应偏导为 $-T,T$。
因此这四点光滑，$z$ 或 $v$ 各为其局部参数。
把 $z^r$ 换为 $Z$、$v^r$ 换为 $Z^{-1}$，并保持 $T,\varepsilon$ 不变，得到 $E$ 的同类两图。

非二特征的泛参数光滑性由 S 给出：其参数多项式

$$
\delta(c,T)=c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27T
\tag{11}
$$

关于超越元 $c$ 单首，故不为零。

现补本命题所需的特征二情形，不使用配平方。
此时 $r$ 为奇数、$\varepsilon=1$。令

$$
F(Z,\lambda)=\lambda^2+(Z^2+cZ+T)\lambda+Z^3.
$$

仿射奇点必须满足

$$
Z^2+cZ+T=0,\qquad c\lambda+Z^2=0,\qquad F=0.
\tag{12}
$$

若 $c=0$，第一个方程给 $Z^2=T\ne0$，与第二个矛盾。
若 $c\ne0$，则 $Z\ne0$、$\lambda=Z^2/c$；代回 $F=0$ 得
$Z^3(Z+c^2)=0$，故 $Z=c^2$。此时首式等价于

$$c^4+c^3+T=0.\tag{13}$$

反向代入也成立。因此特征二的原二次模型在 (13) 不成立时光滑，特别是泛 $c$ 时光滑。
无穷远已单独检查。$C\to E$ 在 $z\ne0,\infty$ 上由 $z^r=Z$ 给出有限 étale 基变换，
因为 $rz^{r-1}\ne0$；结合四个端点图，得到所有允许特征下 $C$ 的泛参数光滑性。

这些两图定义有限平坦次数二覆盖，且

$$
\tau_*\mathcal O_C=\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-n),
\qquad
(E\to\mathbb P^1_Z)_*\mathcal O_E=\mathcal O\oplus\mathcal O(-2).
\tag{14}
$$

这直接来自关于 $\lambda$ 单首二次关系的基 $1,\lambda$ 及 (10) 的转移。
故两曲线射影，并在代数闭包上有 $h^0(\mathcal O)=1$；光滑性使其几何整。
由 (14) 的 Euler 特征得到

$$g(E)=1,\qquad g(C)=n-1=2r-1.\tag{15}$$

商 $\pi:C\to E$ 为 $Z=z^r$；S 的不变量环证明在所有特征成立，
上述图使它延伸至射影模型。$P_0,P_T,Q_2,Q_1$ 均被整个 $G$ 固定。
这里不需要再次作 Riemann–Hurwitz，也不把特征二的二次覆盖误称为 tame。

### Step 2. 从实际 $M$ 到谱线丛族

先在 $X$ 的非空环面开集 $U$ 上工作，固定 $w=1$。
在 $\mathbb P^1_z\times U$ 上取向量丛 $V=\mathcal O^{\oplus2}$，
令谱代数的生成元 $\lambda$ 通过 $M(z)$ 作用。
(7) 与 Cayley–Hamilton 保证关系 (9) 成立；无穷远使用 $v^nM(v^{-1})$，
所以它是 (14) 的全局代数模。有限态射的仿射模对应给出 $C\times U$ 上层 $\mathcal L$，
满足

$$\tau_*\mathcal L=V.\tag{16}$$

必须核实这确为线丛，而不只是秩一无挠层。
在任一几何参数 $u\in U$、有限 $z=a$，若 $M_u(a)=bI$ 为标量，
则 $\det(\lambda I-M_u(z))$ 在 $(a,b)$ 的两个偏导都为零：
行列式一阶导数由伴随矩阵给出，而此处的伴随矩阵为零。
这与 Step 1 的 $C$ 光滑性矛盾。
无穷远的矩阵为 $P$，其特征值 $0,1$ 不同，亦非标量。

任意域上非标量的 $2\times2$ 矩阵有循环向量；在代数闭几何纤维上可选
$e$ 使 $e,M_u(a)e$ 线性无关。其行列式在邻域中为单位，
故 $e$ 将上述谱代数模局部生成成自由秩一模。
这是局部 Nakayama／基判据，适用于参数族；因此 $\mathcal L$ 是线丛。
记其在参数 $u$ 的限制为 $L_u$。

由 (16)，$\chi(L_u)=2$；结合 $g(C)=n-1$，Riemann–Roch 给

$$\deg L_u=n.\tag{17}$$

所以该族定义 $\alpha_U:U\to\operatorname{Pic}^{n}(C)$。
Picard 分支是 proper；$X$ 是光滑射影曲线，故逐点用 DVR 的 proper 赋值判据，
$\alpha_U$ 唯一延伸成 (3)。此步不是随意选取一条特征向量的零点集合；
线丛的整体模定义避免了特征向量规范的附加极点歧义。

### Step 3. 谱线丛恢复常数共轭类

对任意满足 (16) 的 $L$，谱坐标的乘法是

$$\lambda:\tau_*L\longrightarrow(\tau_*L)(n).\tag{18}$$

选取 $\tau_*L\simeq\mathcal O^{\oplus2}$ 后，(18) 恢复一个次数至多 $n$ 的矩阵多项式。
更换此同构仅由 $\operatorname{Aut}(\mathcal O^{\oplus2})=\operatorname{GL}_2(K)$
常数共轭改变矩阵；没有允许任意 $z$-有理 gauge。
反之，线丛同构推下后是常数矩阵，且与 $\lambda$ 作用相容，因而正给这种共轭。

此对应在族中同样成立：在 $\tau_*L$ 平凡的开层上，
$H^0(C,L)$ 为秩二向量丛，评价同构
$H^0(C,L)\otimes\mathcal O_{\mathbb P^1}\simeq\tau_*L$ 恢复 (18)。
可用 $H^0(C,L(-1))=H^1(C,L(-1))=0$ 表述该开条件；
其在 $L_u$ 上成立，因为推下是 $\mathcal O(-1)^{\oplus2}$。
因此后面的系数不变量确实给 Picard 像上的有理函数，而不只是几何点集合上的算法。
需要通用线丛时，$C$ 的有理点 $P_0$ 提供 Picard 的刚化，排除通用线丛的 Brauer 歧义。

这就是本题所需的 Beauville／谱模机制；上述模与向量丛论证不使用特征零假设。

### Step 4. 原坐标的准确逆重建，包含不可分次数检查

从实际 (5)–(6) 得到三条全阶恒等式：

$$
\boxed{M_n=P,\qquad (M_{n-1})_{12}=w,\qquad M_0=t^{r-1}A_0.}
\tag{19}
$$

第一条：最高项乘积为 $s^{2\sum_{j=0}^{r-1}j}P^r=P$，
因为 $s^{r(r-1)}=1$。
第二条：总次数 $2r-1$ 恰取一个 $A_1$、其余取 $P$。
要对 $(1,2)$ 项有贡献，$A_1$ 必在最右边；若它右边有 $P$，乘积第二列为零。
最右边项给 $s^{2\sum_{j=1}^{r-1}j}(A_1)_{12}=w$。
$r=1$ 时空乘积按 $1$ 解释，结论仍成立。
第三条：$\operatorname{tr}A_0=t,\det A_0=0$，
故 Cayley–Hamilton 给 $A_0^2=tA_0$，从而 $M_0=A_0^r=t^{r-1}A_0$。

在 $M_n=P$ 的规范中，(19) 给出

$$
\boxed{
x=-\frac{(M_0)_{12}}{t^{r-1}(M_{n-1})_{12}},\qquad
y=1+\frac{(M_0)_{22}}{t^{r-1}x}.}
\tag{20}
$$

该式分母在 $U$ 上非零。常数共轭若保持最高系数 $P$，
必须保持其两个不同特征值的特征线，因而是对角共轭；
两个 $(1,2)$ 元同时缩放，而 $(2,2)$ 元不变。因此 (20) 不依赖该剩余规范。

还可无基写出其代数性。令 $V=H^0(C,L)$，以恢复出的最高系数 $P$ 分解
$V=\operatorname{im}P\oplus\ker P$。
$PM_{n-1}(1-P)$ 是两个一维空间间的非零映射；
$PM_0(1-P)$ 与它的标量比等于 $-t^{r-1}x$。
而 $\operatorname{tr}((1-P)M_0)=t^{r-1}x(y-1)$。
这两条比值／迹是在 Picard 像上定义的有理函数，不需选择特征向量或开平方。

于是 $\alpha$ 在其像上有原坐标有理逆 (20)。因为 $x,y$ 生成 $K(X)$，
恢复式在函数域上给

$$K(\alpha(X))\xrightarrow{\alpha^*}K(X)\quad\text{为同构}.\tag{21}$$

特别地，$\alpha$ 非恒定且双有理到其像；其次数恰为一，包括全部不可分次数。
这里只看几何点泛单射会不足以推出 (21)，因此必须保留上述族版本与有理恢复式。

### Step 5. 循环作用给出固定的谱线丛差

由 (8)，$A(z)$ 给出谱代数模的有理同态

$$a_u:L_u\dashrightarrow\sigma^*L_u.\tag{22}$$

它在 $z\ne0,\infty$ 上为同构，因为 $\det A(z)=z^3$ 是单位。
沿循环复合 (22)，得到

$$
(\sigma^{r-1})^*a_u\circ\cdots\circ\sigma^*a_u\circ a_u
=M(z)|_{L_u}=\lambda.
\tag{23}
$$

注意 (23) 是乘以 $\lambda$，不是恒等；故 (22) 本身并非普通 $G$-线性化，
不能直接说 $L_u$ 下降为 $E$ 上线丛。

由谱方程及 Step 1 的局部参数，$\lambda$ 的除子为

$$\operatorname{div}_C(\lambda)=3rP_0-2rQ_2-rQ_1.\tag{24}$$

具体地，在 $P_0$ 上另一根趋于 $T\ne0$，根的乘积为 $\varepsilon z^{3r}$，
所以 $\operatorname{ord}_{P_0}\lambda=3r$；在 $P_T$ 上赋值为零。
在无穷远，大根 $\mu$ 趋于 $1$，故 $\lambda$ 极阶为 $2r$；
小根 $\mu$ 由两根乘积 $\varepsilon v^r$ 有零阶 $r$，故 $\lambda$ 极阶为 $r$。

记 $D(a_u)$ 为 (22) 作为 $\sigma^*L_u\otimes L_u^{-1}$ 的有理截面的除子。
其支集只可能位于上述四个点，且这些点均被 $\sigma$ 固定。
取 (23) 的局部赋值，得到 $rD(a_u)=\operatorname{div}(\lambda)$。
这是整数除子等式，故

$$
D(a_u)=D_A:=3P_0-2Q_2-Q_1,
\qquad
\sigma^*L_u\otimes L_u^{-1}\simeq\mathcal O_C(D_A).
\tag{25}
$$

固定除子 $D_A$ 与动力参数点 $u$ 无关。
由 $\alpha$ 的延伸及 Picard 的分离性，(25) 在所有 $P\in X$ 上成立。
因此对任意几何基点 $P_*$，有

$$
\alpha(P)\otimes\alpha(P_*)^{-1}\in\ker(\sigma^*-1:J_C\to J_C).
\tag{26}
$$

这一步是谱商下降的准确入口；没有假设个别 $L_P$ 本身来自 $E$。

### Step 6. 不变 Picard 单位分支恰为 $\pi^*J_E$，且无同源核

先证明 $\pi^*:J_E\to J_C$ 是闭浸入。
范数满足 $\operatorname{Nm}_\pi\circ\pi^*=[r]$，所以其核是 $r$-挠有限群概形的子群。
因为 $r\in k^*$，该核为 étale，故只需排除非平凡几何点。

在 $\bar K$ 上，假设 $N\in J_E$ 且 $\pi^*N\simeq\mathcal O_C$。
拉回线丛有来自商的自然 $G$-作用。选一个平凡化后，每个群元的作用与函数拉回
相差一个常数，因为 $C$ 射影几何整而全局单位只有 $\bar K^*$。
在全群固定点 $P_0$，来自 $\pi^*N$ 的自然纤维作用是恒等，
因此这些常数全部为 $1$。所得无零截面为 $G$-不变。
有限商、投影公式及 $(\pi_*\mathcal O_C)^G=\mathcal O_E$ 给

$$H^0(C,\pi^*N)^G=H^0(E,N).\tag{27}$$

其下降截面不能有零点，否则拉回也有零点；故 $N\simeq\mathcal O_E$。
这排除了整个核，而不只是核的某些点。
proper 群同态的平凡核使其为闭浸入，记像为 $H=\pi^*J_E$。

再令 $B=\ker(\sigma^*-1:J_C\to J_C)$。
$H\subset B$ 且 $\dim H=1$。在单位点处，

$$
\operatorname{Lie}(B)=H^1(C,\mathcal O_C)^G
\simeq H^1(E,\mathcal O_E),
\qquad \dim\operatorname{Lie}(B)=1.
\tag{28}
$$

这里的等式由有限态射的上同调以及 $r^{-1}\sum_{g\in G}g$ 平均投影得到：
取不变量是正合直和因子，故与上同调相容。
于是 $B$ 的单位点局部维数至少为一、切空间维数为一，局部环正则；
群平移给出单位分支光滑。其包含同维闭连通子群 $H$，从而

$$\boxed{B^0=H\simeq J_E.}\tag{29}$$

$r=1$ 时这些证明仍有效：$\pi$ 为恒等、$C=E$、$B=J_C$。
对 $r>1$，全群固定点是排除非平凡拉回核的关键；仅凭商的亏格为一不能替代它。

### Step 7. 陪集、同构与 $K$ 上 torsor 的下降

在 $\bar K$ 上任选 $P_*\in X(\bar K)$。
由 (26)，态射

$$P\longmapsto\alpha(P)\otimes\alpha(P_*)^{-1}$$

的像包含零元并连通，故落在 $B^0=H$。
由 (21) 非恒定，其射影像是 $H$ 中的一维闭子集，只能等于整个 $H$。
因此 $\alpha(X_{\bar K})$ 是 $H_{\bar K}$ 的完整平移陪集，尤其光滑。
又由 (21)，$\alpha$ 双有理到此陪集；光滑射影曲线间的双有理态射为同构。
这证明 (4)，也证明 (3) 是到其像的闭浸入。

记这个 $K$ 上闭像为 $Y$。
$J_E$ 在 $\operatorname{Pic}^n(C)$ 上通过张量乘以 $\pi^*N$ 作用；
该作用及 $Y$ 都在 $K$ 上定义，且几何基变换后 $Y$ 是陪集，
所以作用保持 $Y$ 的性质可忠实平坦下降。
几何基变换后，映射

$$J_E\times Y\longrightarrow Y\times Y,\qquad (N,L)\longmapsto(L,L\otimes\pi^*N)$$

是同构，因此它在 $K$ 上也是同构。
这给出 $Y$ 的 $J_E$-torsor 结构；用 $\alpha:X\simeq Y$ 拉回，再用
$E\simeq J_E$ 的有理零点规范，得到所声明的 $E$-torsor。

最后，光滑亏格一曲线的 torsor 群与其 Jacobian 规范同构：
在几何基点下均为 $P\mapsto\mathcal O_X(P-P_*)$ 的群，
更换基点只改变平移而不改变这个群同态；故这些同构下降到 $K$。
于是得到 (2)。这里确立的是同构，不是一个尚未确定次数的同源。$\square$

## Corrections or Missing Assumptions

本 Claim 没有剩余数学条件，也没有缩小 $r$、排除 $t$ 的特殊非零值或删去特征二、三。
仍需区分以下不能从本件擅自推出的陈述。

1. 若选择 $K$-有理基点才有 $X\simeq E$ 的带原点同构；本件没有声称此基点总存在。
   Jacobian 同构与 torsor 平凡化是两个不同问题。
2. 本件只在超越 $c$ 的真实泛纤维作全局结论。
   可在另已证光滑的有限纤维上复用相同证明，但不能据此自动断言所有 $\delta\ne0$ 的
   动力纤维都光滑，更不能由 Jacobian 泛同构直接分类特殊纤维。
3. 特征二的 (13) 是本件实际补证的谱奇点条件；它不是未经桥接就宣布的动力纤维条件。
4. 个别谱线丛 $L$ 的循环复合为 $\lambda$，没有普通线性化。
   使用固定除子后的线丛差和 Picard 单位分支，才是准确的商 Jacobian 识别。
5. 逆重建仅需恢复原 $x,y$，不需证明任意多项式矩阵都能唯一因式分解成原 $A$ 的循环乘积。
   把后一项额外提升为必要条件会制造本任务并不需要的缺口。

## Open Risks and handoff boundary

- 新作者证明的关键独立核查对象是 Steps 2–7，尤其谱模族的线丛性、(20) 的族有理逆、
  (25) 的方向与整数除子、(29) 的群概形核、torsor 下降。
  本件的作者状态不代替非作者 PASS。
- 坏纤维的精确集合、类型、重数及小特征特殊退化仍需实际模型分析，未在本件关闭。
- 本件没有计算 $F_{st,s}\circ\cdots\circ F_{t,s}$ 在 $E$-torsor 上的具体平移点，
  没有处理奇异层轨道，也没有预支 JR Conjecture 1.2 的所有结论。
- 标准谱对应、tame 不变量上同调、Picard／torsor 理论均须扣除已有理论；
  本件不作正式新意、价值、自然页数或 Route 评分，不因此自动立项。

## Verification record

1. 原 A、M、积分与 §3.2 已从 JR 作者全文实际读取，未只依据二手摘要。
2. 新恒等式 (19) 有上面的全 $r$ 手工证明。
   另用 SymPy 对 $\det A=z^3$、$A_0^2=tA_0$，及 $r=1,2,4$ 的
   $M_n$、$(M_{n-1})_{12}$、$M_0$ 和 (20) 作有限符号夹具核对，全部通过。
   该核对不替代全阶证明，不是数值实验或穷举认证。
3. 特征二 (12)–(13) 在原二次方程中直接消元，无除以二，也无 $c=0$ 漏支。
4. proof-writer 约束了精确量词、证明状态及不可分次数检查；research-lit 用于原公式核对
   和明确扣除 Beauville 的标准谱对应。没有修改任何已经接受的输入。
5. 本件仅本地交付；没有项目、稿、锁、PDF、测试页、正式评分或外部写操作。
