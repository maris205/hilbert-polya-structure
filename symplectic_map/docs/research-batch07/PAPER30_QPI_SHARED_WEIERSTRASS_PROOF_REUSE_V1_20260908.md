# Proof Package：qPI 共享 Weierstrass 计算的无循环证明复用 V1

日期：2026-09-08。作者：主控。只核定新的依赖顺序，不添加新的科学结论。

## Claim

保持候选 T1–T4 的全部对象与量词，已有 B 的纯谱模型计算可以在 J 的 Jacobian 识别之前使用，
同时提供 J 所需的泛谱光滑性，以及准确坏值结论中的四维临界代数。
实际临界长度四可以在局部模型比较之后得到，无需预先消费 F 的 Chern 长度计算。
因此下面的当前证明顺序不需要 S 的四次判别式长求值、J 的单独特征二消元、
F 的 Chern 长度求值或 F 的自治校验来闭合相同 T1–T4。

这些旧证明仍正确、冻结和保留；本件不是撤销其科学结论。
本件没有宣称全体必要证明因此能落入任何特定页数；容量仍由完整正式评审判断。

## Status

PROVABLE AS STATED；新依赖消费者待真正非作者核查。
本件不是数学独立接受、候选评分、正文页数通过或论文稿。

## Assumptions and frozen inputs

设 $k$ 为任意特征代数闭域，$s,t\in k^*$，$\operatorname{ord}(s)=r\ge1$，
$T=t^r$、$\varepsilon=(-1)^{r+1}$、$K=k(c)$。正特征自动有 $p\nmid r$。
只消费以下已写明推导的实际输入，不以整份稿的较强结论反向论证其基础：

| 输入 | 本件所需部分 | SHA256 |
|---|---|---|
| [P 原曲面](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 全部原模型、原积分、精确极除子 | 61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3 |
| [N 法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 实际精确阶 | 8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469 |
| [G 原 pencil](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 完整最小 pencil、几何泛光滑、有限坏值 | 0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace |
| [F 有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | Step1–3 及 Step4 的零维性论证；暂不使用长度数值 | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 |
| [J 原谱模](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | Step1 原矩阵／两图／端点／有限平坦结构；之后 Step2–7 | a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f |
| [B 准确坏值](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | Step1 代数恒等式；Step2–3；Step6；其后才用 Step4–5、7 | 1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1 |

J 作者稿 Step1 曾从 S 引入非二特征谱光滑；本件用以下完整消费者替换这一依赖，
不是在引用 J 的整项结论时偷偷删除其前提。J 的两图公式本身来自原矩阵恒等式，
并不以谱光滑或 Jacobian 身份为前提。
B 原稿称原谱方程“由 J 给出”；以下只用原方程这一代数输入，不先用 Jac$(X)=E$。

## Notation

为避免把 B 整包当成不可分节点，拆为：

- $W_0$：原谱方程到 $W$ 的代数变换，$W$ 总空间／纤维性质及完整临界代数计算。
- $J_0$：J 的原矩阵、两图与四端点数据。
- $J_1$：在泛谱曲线光滑后实施谱模、有理逆、固定差、无核和下降。
- $F_0$：实际有限纤维整约化、唯一奇点，以及实际临界概形有限；没有预设长度。
- $B_1$：真实局部截面、同基底最小正则模型比较、Fitting 与 Artin 块比较。

## Proof Strategy and Dependency Map

$$
P,N\longrightarrow G\longrightarrow F_0,\qquad
J_0\longrightarrow W_0\longrightarrow\text{泛谱光滑及亏格}
\longrightarrow J_1,
$$

$$
(G,F_0,J_1,W_0)\longrightarrow B_1
\longrightarrow\bigl(\operatorname{length}Z_{\rm act}=4,\ R_{\rm act}=\delta\bigr).
$$

R、O 的原 $P,G\to R$ 与 $F_0,R\to O$ 链保持；O 不消费临界长度、J 或 B。
该图没有从 $B_1$ 返回到 $W_0$ 或泛谱光滑的边。

## Proof

### Step 1. 纯代数的 $W_0$ 不使用实际 Jacobian

先只把

$$\Phi(Z,\lambda)=\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3$$

视为原谱二次方程。在 $Z\lambda\ne0$ 的开集采用 B Step1：

$$u=\varepsilon TZ/\lambda,\quad v=\varepsilon T^2/\lambda,\qquad
Z=Tu/v,\quad\lambda=\varepsilon T^2/v.$$

这是两个仿射开集的互逆代数变换；清分母恒等式为

$$\frac{v^3}{T^3}\Phi(Tu/v,\varepsilon T^2/v)
=-\varepsilon(v^2+cuv-\varepsilon Tv-u^3+Tu^2).$$

这一阶段不引用“已知两曲线光滑所以双有理对应延伸为同构”。
以右边定义 $W$ 的射影三次族。B Step3 的无穷远点、所有有限纤维整约化及总空间正则性
全部由这个方程的偏导和分量论证证明，不依赖原动力曲线 $X$。

B Step5 中对 $W$ 的相对微分表示是纯 hypersurface 计算：
临界理想在仿射图为 $(F_u,F_v)$，无穷远为单位理想。
再直接使用 B Step6 的完整概形级消元，得到

$$
Z_W=\operatorname{Spec} k[z]/q(z),\qquad
q(z)=(T-z^2)^2-\varepsilon Tz,\qquad c=\varepsilon-z-z^3/T.
$$

$q$ 首一四次，故这个代数在所有特征均为四维，包括重根情形。
消元过程中的可逆性只用 $T\ne0$、$\varepsilon^2=1$、
$q(0)=T^2$ 和 $(T-z^2)^2=\varepsilon Tz$；没有除以 $2$ 或 $3$。
B Step6 的乘 $c$ 矩阵与特征多项式计算也只使用这些关系。
因此 $Z_W$ 是有限概形，$W_K$ 的相对临界概形为空，且 $W_K$ 几何光滑。
这里应用 hypersurface Jacobian 判据到 $K$ 上的方程；不是由“总曲面光滑”推“所有纤维光滑”。

### Step 2. 从 $W_0$ 到全特征泛谱光滑、亏格与循环商

用 J Step1 的两张图定义 $E/K$。当 $Z\ne0,\infty$ 时，方程迫使 $\lambda\ne0$，
故此部分正是 Step1 的开集，因 $W_K$ 光滑而光滑。
剩下 $Z=0$ 的两点为 $\lambda=0,T$，相应偏导是 $-T,T$。
在 $V=Z^{-1}$、$\mu=\lambda Z^{-2}$ 的无穷远图，

$$\mu^2-(1+cV+TV^2)\mu+\varepsilon V=0,$$

两点为 $\mu=0,1$，相应偏导是 $-1,1$。
这穷尽 $E$ 的所有点，且所有非零偏导在任意允许特征下仍为单位。
故 $E/K$ 几何光滑，不需要 S 的非二特征判别式或 J 的特征二单独消元。

$C/K$ 使用 J 原 $z$ 两图定义。$z\ne0,\infty$ 上是 $E$ 的 $Z=z^r$ 基变换，
由于 $rz^{r-1}\ne0$，覆盖在此为 étale，故该开集几何光滑。
四端点仍分别有偏导 $-T,T,-1,1$，因此整个 $C$ 几何光滑。
由单首二次关系和原两图转移，直接复用 J 的有限平坦等式

$$
(\tau_C)_*\mathcal O_C=\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2r),
\qquad
(\tau_E)_*\mathcal O_E=\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2).
$$

两者有限于 $\mathbb P^1$，故射影；同样计算在代数闭包上给 $h^0=1$。
几何光滑且几何连通的一维曲线几何整；Euler 特征遂给
$g(C)=2r-1$、$g(E)=1$。这些计算不使用 Riemann–Hurwitz 或二次覆盖 tame 性。

循环作用为 $z\mapsto sz$，保持 $\lambda$；在无穷远也保持 $\mu$。
每张图的坐标环由单首二次关系自由分为基 $1,\lambda$（或 $1,\mu$）；
逐个单项式取循环不变量，只保留 $z^r$（或 $z^{-r}$）的幂，给出 $E$ 的原两图。
这是 S Step1 的相同代数论证，在此已完整说明；不需要 S 其余判别式求值。
若 $r>1$，端点局部参数映射为 $z\mapsto Z=z^r$ 或 $z^{-1}\mapsto V=z^{-r}$，
故四点完全分歧、被整个循环群固定；其余处 étale。$r=1$ 为恒等覆盖。

于是 J Step2–7 的泛谱几何前提全部满足。
其谱模族／有理逆／循环除子差／无核／下降证明照原文消费，
得到原 $K$ 上的 $E$-torsor 与 $\operatorname{Jac}(X)\simeq E$。
本件没有把这些必要推导缩成“两个亏格相同”。
带原点的 $E\simeq W_K$ 此时才由 Step1 开集同构在光滑射影曲线上延伸；
原 $Z=\lambda=0$ 的阶为 $1,3$，故映到 $W$ 的零点，正是 B Step1 原端点检查。

### Step 3. $F_0$ 不预设实际临界长度

P、N、G 的证明完全不依赖谱输入。F Step1–3 的整数格、最小 pencil 和伴随论证
给每个有限纤维几何整约化；不光滑时只有一个奇点、正规化有理。
G 给非空光滑基底开集，因此只有有限个坏值。
每条有限纤维整约化，在代数闭域上有非空光滑开集，奇点集有限。
于是所有实际有限奇点的并是有限集。

在光滑曲面 $U$ 上，$Z_{\rm act}=Z(df)$ 的支集正是这些点；
局部方程 $f-c=0$ 的 Jacobian 判据给此身份。因此 $Z_{\rm act}$ 零维且有限型，
是有限 $k$-概形。这个论证正是 F Step4 最后部分，不需要预设其长度为四，
也不需要将微分延至边界、计算八节点或应用 Chern／GRR。
此时定义 $A_{\rm act}$ 和乘 $c$ 的特征多项式合法，但尚未声明其次数。

### Step 4. $B_1$ 比较后得到原长度与准确特征多项式

对任意有限 $c_0$，F$_0$ 给实际特殊纤维几何整约化、有光滑 $k$-点。
G、P 给原 proper flat 正则模型；Step2 已给原泛 Jacobian／torsor 身份。
这些正是 B Step4 光滑点提升截面、局部 torsor 平凡化、
双方最小正则模型唯一性所需的全部实际前提。
该段不使用 $\operatorname{length}Z_{\rm act}=4$ 或 F 的 Chern 数。

再使用 B Step5 的同基底 Fitting 比较。
两个临界概形现在都已分别证明有限：实际者由 Step3，$W$ 者由 Step1。
henselization 的有限阶商不变，因此每个 $c_0$ 的 Artin 块及乘 $c$ 算子同构。
对有限多个块取直积，得到原临界代数的 $k$-长度为四，并且

$$
\det(C_0\operatorname{id}-m_{I_r}\mid A_{\rm act})
=\det(C_0\operatorname{id}-m_c\mid \Gamma(Z_W,\mathcal O))
=\delta(C_0,T).
$$

第二个等式由 Step1 已复用的 B Step6 四维矩阵给出，故没有循环预设四次次数。
非光滑点与 $Z_{\rm act}$ 支集相同，所有有限坏值与重数的 T3 结论随之成立。
B 的最小整 Weierstrass 判别式计算仍在原 Step2 中，不因这次复用被删除；
它与 $W$ 的最小正则模型性质保持明确区分。

## Corrections or Missing Assumptions

没有增加参数排除、改 $c$、删有限坏点、删特征 $2,3$ 或假设原 $X(K)$ 有点。
S 的谱结论、F 的实际长度四和全部 T1–T4 结论均保留；改变的是证明依赖选择。
本件只复用已接受的实际计算，新增须审对象是 Step1–4 的先后顺序及消费者前提闭合。

## Open Risks

须由新非作者确认 $W_0$ 不暗用 J$_1$、谱两图确已覆盖全部端点、
F$_0$ 的有限性不借长度，以及 B$_1$ 真正不消费旧 Chern 数值。
未完成这项针对性核查前，不能以本件自动替换正式评审的当前证明选择图。
本件不证明更高新意、更多科学价值或自然页数通过，不授权写稿或外部操作。
