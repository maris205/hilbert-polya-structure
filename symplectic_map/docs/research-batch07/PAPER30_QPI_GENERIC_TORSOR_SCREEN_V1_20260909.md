# Paper30 泛 torsor 有界证明预筛 V1

日期：2026-09-09。类型：T1 的直接后果核查；非正式票、非旧证明重审、非新候选立项。
唯一科学输入：[完整候选简报 V2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md) §§2–3；T1 按已接受前提使用。
使用 proof-writer 技能：显式列出依赖，分别处置已证推论与未计算的上同调代表。

## Claim

在下述原假设下，每条整多截面的次数都被 $r$ 整除，末端例外曲线给出次数恰为 $r$ 的多截面，而且
$$
\operatorname{ind}(X)=\operatorname{per}(X)=r.
$$
因此，若 $r>1$，则 $X(k(c))=\varnothing$，且不存在保能级的曲面双有理共轭到带截面的自治 Tate 族。
这里“保能级”指保持原基底，或仅作可逆能级改名 $h=\phi(c)$，其中 $\phi\in\operatorname{PGL}_2(k)$。

## Status

PROVABLE AS STATED，按上述保能级含义。结论是既有 T1 加标准曲面／曲线／下降理论的推论。
“显式确定 Weil–Châtelet 类的代表”不包含在该结论中，其状态为 NOT CURRENTLY JUSTIFIED。

## Assumptions

- $k$ 是代数闭域，特征任意；$s,t\in k^*$，$s$ 的精确阶为 $r\ge1$，正特征 $p$ 时 $p\nmid r$。
- $S=S_{t,s}$ 是 §2 的光滑射影八次吹起曲面；$D=-K_S$ 是有效整系数反典范除子。
- $L\subset S$ 是一条完整末端例外曲线，$L\simeq\mathbb P^1_k$，$L^2=-1$。
  此处取 §2 的仿射状态线 $L_i$ 在 $S$ 内的闭包，不能把仿射线直接当作完整交数对象。
- 采用 T1：$f=I_r:S\to\mathbb P^1_k$ 为无基点完整 pencil，概形纤维 $f^{-1}(\infty)=rD$。
- 采用 T1：泛纤维 $X=S\times_{\mathbb P^1}\operatorname{Spec}k(c)$ 光滑、射影、几何整，亏格一。
  不增加一般位置、特征不为 $2,3$、有限纤维互异或已有截面等假设。

## Notation

- $K=k(c)$，$F$ 表示纤维除子类；故 $F\sim rD$。
- 整多截面为支配基底的整曲线 $C\subset S$；其次数为 $[k(C):K]$，包含不可分次数。
- $\operatorname{ind}(X)=\gcd\{[\kappa(P):K]:P\text{ 是 }X\text{ 的闭点}\}$。
- $E=\operatorname{Jac}(X)$，$\xi=[X]\in H^1(K,E)$ 是亏格一曲线的规范 torsor 类；
  $\operatorname{per}(X)$ 为 $\xi$ 的阶，零类的阶约定为 $1$。
  此处无需调用 T2 的具体谱商识别，更无需调用指定回返点。

## Proof Strategy

先用纤维交数求全部闭点的次数理想，再用 Tsen 消去有理 Picard 类的下降障碍，最后限制双有理映射到泛纤维。

## Dependency Map

1. 多截面整除性：仅依赖 $F\sim rD$、$S$ 光滑及除子交数／曲线有限映射次数公式。
2. 次数 $r$ 的多截面：再用 $L\simeq\mathbb P^1$、$L^2=-1$、伴随公式和 $D=-K_S$。
3. period 等式：再用亏格一 Picard torsor、Tsen–Brauer 消失及线丛的 Galois 下降。
4. 无点与保能级非共轭：只需第 1–2 步的 index 结论与光滑射影曲线的双有理不变性；不依赖 period 证明。

## Proof

### Step 1. 多截面与闭点次数

设 $C\subset S$ 是整水平曲线，$\nu:\widetilde C\to C$ 是正规化。映射 $g=f\circ\nu$ 非常数，
且为射影曲线到 $\mathbb P^1$ 的有限映射。拉回次数及投影公式给出
$$
[k(C):K]=\deg g=\deg g^*\mathcal O_{\mathbb P^1}(1)=F\cdot C=r(D\cdot C)\in r\mathbb Z.
$$
这里 $D\cdot C$ 是整数；公式采用有限映射的总次数，不假设 $g$ 可分。
每个闭点 $P\in X$ 在 $S$ 中的约化闭包是整水平曲线 $C_P$，且 $k(C_P)=\kappa(P)$。
反过来，整水平曲线的泛纤维是相应闭点。因此所有闭点次数被 $r$ 整除，$r\mid\operatorname{ind}(X)$。

### Step 2. 末端例外曲线实现次数 $r$

由光滑曲面的伴随公式，$(K_S+L)\cdot L=2g(L)-2=-2$，所以 $K_S\cdot L=-1$，$D\cdot L=1$。
因此 $F\cdot L=r>0$。若 $L$ 竖直，则 $f^*\mathcal O(1)|_L$ 的次数为零，与此矛盾；故 $L$ 水平。
第 1 步给出 $\deg(f|_L)=r$，即 $L$ 的泛纤维是一个次数恰为 $r$ 的闭点 $P_L\in X$。
故 $\operatorname{ind}(X)\mid r$；结合反向整除性得到 $\operatorname{ind}(X)=r$。
正特征下，该次数 $r$ 的扩张还可分，因为有限扩张的不可分次数为 $p$ 的幂而 $p\nmid r$。

### Step 3. period 与 index 相等所需的精确下降

取可分闭包 $K^s$ 与 $q\in X(K^s)$；这样的点存在，因为 $X/K$ 光滑非空。
亏格一曲线的 Jacobian 作用将 $X_{K^s}$ 以 $q$ 为原点识别为 $E_{K^s}$。
以 $a_\sigma=\sigma q-q$ 表示其 Galois $1$-余循环。
对任意整数 $d$，度 $d$ 的 Picard torsor 以 $\mathcal O(dq)$ 为原点时，余循环为 $d a_\sigma$；因此
$$
[\operatorname{Pic}^d_{X/K}]=d\xi,\qquad
\operatorname{Pic}^d_{X/K}(K)\ne\varnothing\ \Longleftrightarrow\ d\xi=0.
$$
次数 $r$ 的闭点 $P_L$ 给出实际线丛 $\mathcal O_X(P_L)$，所以 $r\xi=0$。
令 $n=\operatorname{per}(X)$，则 $n\mid r$ 且 $\operatorname{Pic}^n_{X/K}(K)\ne\varnothing$。

此处必须区分有理 Picard 类与实际线丛。Tsen 适用于代数闭域上任意特征的一元函数域，故
$\operatorname{Br}(K)=0$；这是引用的标准定理，不是本件重新证明的结论。
精确来源是 [Stacks Theorem 59.67.10（Tsen，03RD）](https://stacks.math.columbia.edu/tag/03RD)
及其直接推论 [Lemma 59.67.11（03RF）](https://stacks.math.columbia.edu/tag/03RF)。

为说明该消失如何使用：一个有理 Picard 类可在 $X_{K^s}$ 上取线丛代表 $\mathcal M$，
它的共轭同构未必满足余循环条件；两种复合之比属于 $(K^s)^*$，因为 $H^0(X_{K^s},\mathcal O)=K^s$。
这些标量给出 $H^2(\operatorname{Gal}(K^s/K),(K^s)^*)$ 中的下降障碍。
该群等于 $\operatorname{Br}(K)$，由 [Stacks Theorem 59.61.6（03R7）](https://stacks.math.columbia.edu/tag/03R7)。
障碍为零后，可调整共轭同构使之满足余循环条件；全部数据在某有限 Galois 扩张上定义，
由 [Galois 下降 Lemma 35.6.1（0CDR）](https://stacks.math.columbia.edu/tag/0CDR) 得到 $X$ 上实际线丛。
这是本件对标准下降机制的应用说明；没有先假定 $X(K)$ 非空来完成下降。

故上述度 $n$ 的有理 Picard 类下降为实际线丛 $\mathcal N\in\operatorname{Pic}(X)$。
在光滑整曲线 $X$ 上取 $\mathcal N$ 的非零有理截面，其除子 $A=\sum_P m_P P$ 满足
$$
n=\deg\mathcal N=\deg A=\sum_P m_P[\kappa(P):K]\in r\mathbb Z.
$$
允许 $m_P$ 为负数，所以此处不需要另行证明除子有效。于是 $r\mid n$，结合 $n\mid r$ 得 $n=r$。

### Step 4. 无点及保能级非共轭

若 $r>1$ 而 $X(K)$ 有点，该点度数为 $1$，与第 1 步矛盾。
若存在保能级曲面双有理映射 $\Phi:S\dashrightarrow Y$，且 $Y$ 的泛纤维为带 $K$-点的光滑射影亏格一曲线 $Y_K$，
则 $\Phi$ 诱导 $X\dashrightarrow Y_K$ 的 $K$-双有理映射；可逆改名 $h=\phi(c)$ 时先识别相应基域。
光滑射影曲线之间的双有理映射延拓为同构，见 [Stacks Theorem 53.2.6（0BY1）](https://stacks.math.columbia.edu/tag/0BY1)。
截面的泛点因而拉回为 $X(K)$ 中的点，矛盾。这已排除曲面映射本身，故也排除附加动力共轭条件的映射。∎

## Corrections or Missing Assumptions

- 原有界结论不需加强假设。$r=1$ 时 $L$ 的次数为 $1$，它给出截面，且 $\operatorname{per}(X)=\operatorname{ind}(X)=1$；非共轭障碍仅声称于 $r>1$。
- 不能把 $\operatorname{Br}(K)=0$ 错写成 $H^1(K,E)=0$；当 $r>1$ 时，本例恰有阶为 $r$ 的非平凡亏格一 torsor。
- 不主张对非代数闭常数域仍有相同 period 论证，也不排除非平凡有限基变换后出现截面。
- 逐条闭纤维上的同构或有限域点集的动力约化，不自动拼成 $K$ 上同构；本结论与这种逐纤维结果不冲突。

## Open Risks：显式类仍缺什么

本件只给出 $\xi$ 的阶及 $r>1$ 时的非平凡性，没有计算它在指定 Tate Jacobian 坐标下的上同调代表。
若进一步要求显式 Weil–Châtelet 类，至少需固定与原 $X$ 的实际 Jacobian 识别，给出可计算的分裂域与平凡化，
计算共轭平凡化之间的平移余循环，并验证其下降曲线就是原 $I_r=c$、而非另一个同阶 torsor。
仅写 $a_\sigma=\sigma q-q$ 是一般定义；没有原坐标的 $q$ 与 Galois 作用计算就不是显式答案。
仅知无穷远多重纤维、正规丛阶数和 $\operatorname{per}=\operatorname{ind}=r$，也没有给出上述代表或唯一性证明。
本件不推断具体循环覆盖形式、局部不变量或全局唯一性；这些需要另外的实质输入。

## 为什么不能单独包装为新 idea

多截面整除性、index 与无截面／非共轭是 T1 和已给吹起几何的短推论；period 只再调用任意特征通用的 Tsen–下降事实。
它们不需要新的 qPI 计算，不使用 T3 的临界代数或指定回返点，也没有越过已接受 T1 的实质几何内容。
适合把它们作为既有结果的澄清性推论，说明“闭纤维自治约化”不等于“泛 torsor 全局平凡化”。
显式 Weil–Châtelet 代表可能是尚未完成的更强任务，但本预筛既未证明它，也未判定其新意或独立价值。
网页核对日期：2026-09-09；仅使用以上公开 Stacks 官方定理页面，未调用程序 API 或下载本地 PDF。
