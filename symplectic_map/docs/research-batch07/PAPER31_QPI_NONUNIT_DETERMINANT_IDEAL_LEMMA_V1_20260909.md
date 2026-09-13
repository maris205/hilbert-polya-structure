# Proof Package — 高度一扭结因子与行列式理想的分离

日期：2026-09-09。新作者引理，等待非作者检查。本件是标准交换代数工具的自足证明，不是原 D05 的自审，也不把原格识别、任何具体 $M_n$ 的结构或新意视为已证。

## Claim

固定有理素数 $p$，令

$$
A=\mathbb Z[\tau]_{(p,\tau)},\qquad K=\operatorname{Frac}(A)=\mathbb Q(\tau).
$$

设 $n,r\ge0$，有限呈示 $A$-模 $M$ 有指定的长度一自由分辨率

$$
0\longrightarrow A^r\xrightarrow{\Phi}A^{n+r}\longrightarrow M\longrightarrow0,
\tag{1}
$$

且 $M[1/\tau]$ 是秩 $n$ 的自由 $A[1/\tau]$-模。记

$$
T=\{m\in M:\tau^s m=0\text{ 对某个 }s\ge0\},\qquad L=M/T.
$$

假设 $L^{**}$ 自由且秩为 $n$，自然嵌入的余核 $E=L^{**}/L$ 有限长。选择一个 $L^{**}\simeq A^n$ 的基，并定义

$$
\operatorname{detideal}(L)
=\operatorname{im}\left(\bigwedge^nL\longrightarrow\bigwedge^nL^{**}\simeq A\right).
\tag{2}
$$

令 $\widehat R=\mathbb Q[[\tau]]$，并令 $\operatorname{tors}_{\tau}$ 表示被某个 $\tau$ 幂杀死的元素子模，不是导出函子的 $\operatorname{Tor}$。定义

$$
B=\operatorname{length}_{\widehat R}
\operatorname{tors}_{\tau}(M\otimes_A\widehat R).
\tag{3}
$$

主引理的结论为准确的 $A$-理想等式

$$
\boxed{\operatorname{Fitt}_n(M)=\tau^B\operatorname{detideal}(L).}
\tag{4}
$$

条件性直和推论：若存在抽象 $A$-模同构

$$
L\simeq\bigoplus_{a=0}^{n-1} I_a
\tag{5}
$$

且每个非零理想 $I_a\subset A\subset K$ 在此指定分式域嵌入下满足 $I_a^{**}=A$，则

$$
\operatorname{detideal}(L)=\prod_{a=0}^{n-1}I_a,
\qquad
\operatorname{Fitt}_n(M)=\tau^B\prod_{a=0}^{n-1}I_a.
\tag{6}
$$

对于 $n\ge1$ 的具体候选

$$
I_a=\left(\binom{n-1-j}{a}\tau^j:0\le j\le n-1-a\right),
\qquad 0\le a\le n-1,
\tag{7}
$$

上述嵌入归一化条件自动满足。因此，若未来另行证明了 (5)，则 (6) 对 (7) 成立。本件不证明 (5) 对任何原研究模块成立，也不计算该乘积的组合形式或余长。

## Status

`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`，仅因原附带的“抽象理想直和即可取未归一化乘积”需要显式修正。

主等式 (4) 在原给定假设下原样成立，没有削弱。一般抽象直和必须保留 (6) 前的嵌入归一化条件；不加该条件的说法为假。具体理想 (7) 已满足此条件，故其条件性乘积不受影响。

## Assumptions

- $p$ 是素数，$A$ 是固定二维局部整环；分辨率 (1) 是实际正合序列，特别是 $\Phi$ 单射。不能用任意具有额外关系的呈示替代此假设而保留同一个最大子式论证。
- $M[1/\tau]$ 的自由性是在整个 $A[1/\tau]$ 上，而不只是再倒置 $p$ 后成立。
- $L^{**}$ 和 $E$ 指自然双对偶映射及其余核；不使用另行拟合的自由格替换自然双对偶。
- 直和推论中的 $I_a^{**}=A$ 指给定 $I_a\subset K$ 的双对偶分式理想确实为 $A$，不只是“它抽象同构于一个自由秩一模”。
- $n=0$ 时 $\bigwedge^0(0)=A$，行列式理想与空乘积均约定为 $A$。$r=0$ 时零阶子式理想约定为 $A$。

## Notation

对矩阵 $X$，$I_s(X)$ 表示其所有 $s\times s$ 子式生成的理想，$I_0(X)=A$。按 (1) 的生成元数约定，$\operatorname{Fitt}_n(M)=I_r(\Phi)$。设 $N=n+r$。对高度一素理想 $\mathfrak q$，$v_{\mathfrak q}$ 是离散赋值环 $A_{\mathfrak q}$ 的归一化赋值；在 $\mathfrak q=(\tau)$ 时取 $v_{(\tau)}(\tau)=1$。

式 (2) 不依赖自由基的选择：另一组基改变顶次外幂坐标时只乘以 $A$ 的单位，从而不改变作为 $A$ 子集的理想。

## Proof Strategy

将自由呈示映到自然双对偶，得到矩阵 $P:A^N\to A^n$，其像为 $L$。在分式域上，$\Phi$ 与 $P$ 给出互补子空间，全部互补最大子式相差同一个标量 $\delta\in K^\times$。有限长余核保证每个高度一局部化的 $P$ 都满射；其局部投影正规形将 $v_{\mathfrak q}(\delta)$ 识别为原模块的扭结长度。全部非零高度一赋值只可能位于 $(\tau)$，在 UFD 中因此得到 $\delta=\varepsilon\tau^B$。最后处理理想直和的自然双对偶及嵌入归一化。

## Dependency Map

1. $A$ 的 UFD 性、各高度一局部环的 DVR 性，用于控制分式标量而非仅控制理想的除子。
2. $M[1/\tau]$ 自由，用于保证 $T$ 是全部 $A$-扭结、$L$ 无扭结并排除其他高度一扭结支撑。
3. $E$ 有限长和 $L^{**}$ 自由，用于使每个高度一局部化的 $P$ 有单位最大子式。
4. (1) 与互补外幂恒等式，用于证明实际理想的统一标量关系，而非仅证明双对偶后的相等。
5. $(\tau)$ 处的 DVR 完成，用于把标量指数与题设的 $B$ 精确对应。
6. 自然双对偶的函子性和秩一理想公因子消除，用于区分抽象直和与指定分式嵌入的乘积。

## Proof

### Step 1. 环、扭结及自然双对偶

$\mathbb Z[\tau]$ 由 Gauss 引理是 UFD，局部化仍为 UFD；故 $A$ 为 UFD。其极大理想为 $(p,\tau)$，维数为 $2$。每个高度一素理想由一个不可约元生成，局部化后每个非零元素是该生成元的幂乘以单位，因此是 DVR。

$T$ 是有限生成子模：$A$ Noetherian，$M$ 有限生成。因此存在一个共同的 $s$ 使 $\tau^sT=0$。反过来，若 $m\in M$ 被某个非零 $c\in A$ 杀死，则 $m/1\in M[1/\tau]$ 也被非零的 $c/1$ 杀死。该局部化是整环上的自由模，故 $m/1=0$，也就是 $\tau^u m=0$ 对某个 $u$ 成立。因此 $T$ 正是 $M$ 的全部 $A$-扭结，$L$ 无扭结且秩为 $n$。

有限生成无扭结模 $L$ 的自然映射 $L\to L^{**}$ 是单射。为核对此处的自然性，可以把 $L$ 嵌入 $L\otimes_AK\simeq K^n$，并清除有限组生成元的坐标分母，得到一组 $A$-线性坐标泛函 $L\to A$；这些泛函能分离任意非零元素，故自然评价映射无核。

对高度一 $\mathfrak q$，有限长模 $E$ 的局部化为零：某个极大理想幂杀死 $E$，而极大理想有元素不属于 $\mathfrak q$，该元素局部化后可逆。于是自然嵌入给出

$$
L_{\mathfrak q}=(L^{**})_{\mathfrak q}\simeq A_{\mathfrak q}^n.
\tag{8}
$$

这里没有另取不同的双对偶格。若用局部双对偶的语言，有限呈示模的 $\operatorname{Hom}$ 与局部化交换，连续两次应用后也给出 $(L^{**})_{\mathfrak q}\simeq(L_{\mathfrak q})^{**}$。

### Step 2. 由自然映射构造互补矩阵

选择 $L^{**}\simeq A^n$，令 $P$ 为复合

$$
A^N\longrightarrow M\longrightarrow L\longrightarrow L^{**}\simeq A^n.
\tag{9}
$$

其像正是指定的 $L$，故由列向量外积生成顶次外幂的像得到

$$
I_n(P)=\operatorname{detideal}(L).
\tag{10}
$$

更具体地，$L$ 的任意 $n$ 个元素都可写为 $P$ 的列向量的 $A$-线性组合，故其行列式属于 $I_n(P)$；反向每个列子式本身就是这种外积的像。这也处理了外幂可能存在的附加扭结，因为只计算其映入自由秩一模的像。

$P\Phi=0$，且张量 $K$ 后的维数和正合性给出

$$
\ker P_K=\operatorname{im}\Phi_K.
\tag{11}
$$

只在 $K$ 上使用 (11)。在 $A$ 上实际有 $\ker P/\operatorname{im}\Phi\simeq T$，不能把这部分扭结抹去。

先设 $n,r>0$。令 $V=K^N$ 带标准体积形式，$\varphi_1,\ldots,\varphi_r$ 为 $\Phi_K$ 的列。交替 $n$-线性形式

$$
\omega(v_1,\ldots,v_n)=
\det[\varphi_1\ \cdots\ \varphi_r\ v_1\ \cdots\ v_n]
$$

在任一 $v_i\in\ker P_K$ 时为零，且自身非零。$P_K$ 的 $n$ 个行泛函的外积也是非零的、在同一核上消失的 $n$-形式。两者都属于一维空间 $\bigwedge^n(V/\ker P_K)^*$，因此存在唯一 $\delta\in K^\times$ 使前者等于后者的 $\delta$ 倍。

在标准坐标向量上逐个评价，对每个大小为 $r$ 的指标集 $I\subset\{1,\ldots,N\}$ 得

$$
\det\Phi_I=\pm\delta\det P_{I^c}.
\tag{12}
$$

符号由同一标准体积形式下的互补指标顺序决定，不影响理想。所有子式使用同一个 $\delta$；由于至少一个 $P$ 子式非零，标量确实唯一。式 (12) 因而给出分式域内的精确分式理想等式

$$
I_r(\Phi)=\delta I_n(P).
\tag{13}
$$

### Step 3. 每个高度一处的标量赋值

固定高度一 $\mathfrak q$，记 $R_{\mathfrak q}=A_{\mathfrak q}$。由 (8)–(9)，$P_{\mathfrak q}:R_{\mathfrak q}^N\to R_{\mathfrak q}^n$ 满射，因此 $I_n(P)R_{\mathfrak q}=R_{\mathfrak q}$。

选择该满射的一个截面，再选择其核的自由基。核是有限自由模的直和项，在局部环上自由，秩为 $r$。这样得到源自由模 $R_{\mathfrak q}^N$ 上的一个可逆换基，使矩阵分别成为

$$
P_{\mathfrak q}=[I_n\ 0],\qquad
\Phi_{\mathfrak q}=\begin{bmatrix}0\\ \Psi_{\mathfrak q}\end{bmatrix},
\tag{14}
$$

其中 $\Psi_{\mathfrak q}$ 是单射的 $r\times r$ 方阵。源自由模换基只在各子式理想中进行可逆线性组合。由 (1) 与 (14)，

$$
M_{\mathfrak q}\simeq R_{\mathfrak q}^{n}\oplus\operatorname{coker}\Psi_{\mathfrak q},
\qquad
T_{\mathfrak q}\simeq\operatorname{coker}\Psi_{\mathfrak q}.
$$

后一余核是 DVR 上的有限长扭结模。DVR 上的 Smith 正规形将 $\Psi_{\mathfrak q}$ 的不变量写为均匀化元的非负幂，因此

$$
I_r(\Phi)R_{\mathfrak q}=(\det\Psi_{\mathfrak q}),\qquad
v_{\mathfrak q}(\delta)=v_{\mathfrak q}(\det\Psi_{\mathfrak q})
=\operatorname{length}_{R_{\mathfrak q}}T_{\mathfrak q}.
\tag{15}
$$

若 $\mathfrak q\ne(\tau)$，则 $\tau$ 在 $R_{\mathfrak q}$ 中为单位，而 $\tau^sT=0$，所以 $T_{\mathfrak q}=0$。这包含 $(p)$ 及其他任何高度一素点，不只检查两个坐标轴。因而

$$
v_{\mathfrak q}(\delta)=0\quad(\mathfrak q\ne(\tau)),\qquad
v_{(\tau)}(\delta)=\operatorname{length}_{A_{(\tau)}}T_{(\tau)}\ge0.
\tag{16}
$$

### Step 4. 指数与 $\mathbb Q[[\tau]]$ 的准确对应

在高度一素点 $(\tau)$ 再局部化时，所有非零整数均变成单位；故

$$
R=A_{(\tau)}=\mathbb Q[\tau]_{(\tau)},\qquad \widehat R=\mathbb Q[[\tau]].
$$

把 (14) 在此处的 Smith 正规形写成 $\operatorname{diag}(\tau^{b_1},\ldots,\tau^{b_r})$，其中 $b_i\ge0$，省略的单位均可吸收。它给出

$$
M_R\simeq R^n\oplus\bigoplus_{i=1}^rR/(\tau^{b_i}).
$$

张量完成环后同一个分解成立；$b_i=0$ 的项为零模，其余项正是全部 $\tau$-扭结。因此

$$
B=\sum_i b_i=\operatorname{length}_{R}T_{(\tau)}=v_{(\tau)}(\delta).
\tag{17}
$$

这也证明了 (3) 中的长度有限，不需要假设任意基变都与取双对偶交换。

由 UFD 中分子分母的唯一分解，(16)–(17) 蕴含 $\delta=\varepsilon\tau^B$，其中 $\varepsilon\in A^\times$：所有不可约元的赋值已被检查，分母不能留下非单位因子，除 $\tau$ 外分子也不能留下非单位因子。将它代回 (10)、(13) 即得到 (4) 的实际理想相等。这里不仅比较了高度一除子；高度二信息仍保留在 (13) 的同一个 $I_n(P)$ 中。∎

### Step 5. 零秩与无关系边界

若 $r=0$，则 $M=A^n$，$T=0$、$L=L^{**}=A^n$、$E=0$，所以 $B=0$、$\operatorname{Fitt}_n(M)=I_0(\Phi)=A=\operatorname{detideal}(L)$。

若 $n=0$，则 $M[1/\tau]=0$。有限生成性给出 $M=T$，$L=L^{**}=0$、$E=0$，而 $\Phi$ 是单射方阵。于是 $\operatorname{Fitt}_0(M)=(\det\Phi)$。在每个高度一局部化用方阵 Smith 正规形，重复 (15)–(17) 的行列式赋值计算，得到 $\det\Phi=\varepsilon\tau^B$。按 $\operatorname{detideal}(0)=A$ 的约定，(4) 仍成立。$n=r=0$ 时 $M=0$、空行列式为 $1$、$B=0$，两种边界一致。

### Step 6. 抽象直和、自然双对偶与正确乘积

先给出不可省略的反例：秩一模 $L=A$ 抽象同构于理想 $(p)$，但其自然双对偶是它本身，故 $\operatorname{detideal}(L)=A\ne(p)$。不能把 $(p)^{**}=(p)\subset K$ 的基向量 $p$ 默换成不是该模基向量的 $1$，再据此声称未归一化乘积。

一般地，设非零理想 $I\subset A$ 的有限生成元的 UFD 最大公因子为 $g\ne0$，写 $I=gJ$。$J$ 的生成元没有共同不可约因子。每个 $A$-线性泛函 $I\to A$ 张量 $K$ 后是秩一 $K$-空间上的标量乘法，因此在分式域中对偶可识别为

$$
I^*=\{c\in K:cI\subset A\}.
$$

若 $cJ\subset A$，则对每个不可约元 $h$，由 $\min v_h(J)=0$ 得 $v_h(c)\ge0$，所以 $c\in A$。因此 $J^*=A$、$J^{**}=A$，进而 $I^*=g^{-1}A$，并且在原分式嵌入中

$$
I^{**}=gA.
\tag{18}
$$

现在给定抽象同构 $\theta:L\simeq\bigoplus_a I_a$。双对偶的函子性给出同构 $\theta^{**}:L^{**}\simeq\bigoplus_a I_a^{**}$，并且它与两侧自然评价映射组成交换方块。若 $I_a=g_aJ_a$，在目标双对偶上选择基 $g_ae_a$，则 $L$ 的像在这组基下正是 $\bigoplus_aJ_ae_a$，不是未归一化的 $\bigoplus_aI_ae_a$。

这个归一化后的像的行列式理想是 $\prod_aJ_a$：任意 $n$ 个列向量的行列式每一项都属于该乘积；反过来，分别取 $j_ae_a$ 的外积实现每个乘积生成元。这证明一般修正版

$$
\operatorname{detideal}(L)=\prod_a(g_a^{-1}I_a).
\tag{19}
$$

当每个指定嵌入的 $I_a^{**}=A$ 时，(18) 保证 $g_a$ 是单位，故 (19) 恰化为 (6)。抽象同构无须事先与某个给定双对偶基一致：自然交换方块允许选择兼容基，而随后任意改变双对偶基只乘单位，不改变理想。必要的是指定理想嵌入的归一化，而不是一个默许的非单位坐标缩放。

### Step 7. 具体二项式理想仅提供条件性乘积

对 (7) 中的每个 $a$，理想同时含有非零整数 $\binom{n-1}{a}$ 和纯幂 $\tau^{n-1-a}$。当指数为零时理想为 $A$。当指数为正时，任何公共不可约因子若整除此纯幂，就必须与 $\tau$ 相伴；但 $\tau$ 不整除这个非零整数。因此最大公因子是单位，(18) 给出指定分式嵌入下的 $I_a^{**}=A$。

所以 (5) 对这些具体理想若已由别处独立证明，就可以应用 (6)。此处没有证明任何原格映到 $\bigoplus I_a$ 的满射性、单射性或精确像；也没有证明 Lucas 型判别、乘积化简、余长求和或“首次出现”的组合消费者。

## Corrections or Missing Assumptions

- 主等式 (4) 无须增加假设；候选 Plücker 证明的核心正确。必须让所有子式共享同一个分式标量，并在完整 UFD 上检查全部高度一素点，才足以恢复实际理想，而非只恢复其除子。
- “抽象直和 $L\simeq\bigoplus I_a$ 即得到 $\prod I_a$”原说法不成立。上文保留反例、一般式 (19) 和归一化条件；没有把该条件默认为抽象模同构的一部分。
- $\ker P=\operatorname{im}\Phi$ 只在 $K$ 上使用；在 $A$ 上的余核是 $T$，正是 $\tau^B$ 因子的来源。
- 若只知道倒置 $p$ 后的自由性，不能据此排除其他高度一扭结；本证明使用题设在 $A[1/\tau]$ 上的自由性。若不再有长度一分辨率或 $E$ 的有限长条件，也不能直接复用本证明。

## Open Risks / Blocking

本件归一化后的条件性命题无剩余数学阻塞，仍待非作者针对实际新证明检查。它是标准代数工具，应在后续查新判断中扣除，不单独主张新意。

原模块的长度一自由分辨率、自然扭结商、双对偶自由性、有限长缺陷和 (5) 的实际原格识别，全部仍是未来应用必须提供的输入。本件不消费尚未完成的 residue 识别，也不把任何 $M_4$ 或一般 $M_n$ 的猜测提升成事实。主控另行编写的组合消费者不在本文件的依赖链中。

## Input / Ownership / Verification record

- 直接数学输入是主控本轮给出的完整一般假设、Plücker 候选证明、具体理想公式，以及随后明确要求保留归一化条件的补充。未读取或使用其他作者尚未完成的原格识别稿。
- 本人全文读取 proof-writer 技能 223 行，并据其结构给出原主命题、条件性推论、完整证明及反例。技能 SHA-256：`6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe`。
- 数学计算脚本运行 $0$ 次，GPU 使用 $0$；无 CAS、联网或新增文献检索。实际文件操作仅为读取技能、检索指定输出是否存在、用补丁新增本文以及读取/行数/哈希核对。
- 唯一新增文件是本文。D01 独立检查终态、原 D05 作者稿、原论文及其他冻结记录保持不动。本件是新作者证明包，不能自行兼任其非作者检查。
