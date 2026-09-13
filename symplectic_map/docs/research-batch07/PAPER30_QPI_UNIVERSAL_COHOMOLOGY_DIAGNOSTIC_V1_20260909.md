# Paper30 qPI：全部反典范幂的通用整系数上同调诊断 V1

日期：2026-09-09。作者：主控 `/root`，可用 Codex AI。
类型：新的作者证明；不是独立接受、正式候选、论文稿或新意判定。

## Claim

置 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$，其中两个参数不满足任何根单位关系。
在 $\mathbb P^1_R\times_R\mathbb P^1_R$ 上实施
[G §1](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)
指定的八次截面吹起，参数对应为 $s=q,t=\tau$，得到 $S/R$。
令 $D$ 为相同的八环边界，$L_n=\mathcal O_S(nD)$，$\mathscr N=\mathcal O_D(D)$。
固定原矩阵与乘积顺序，不重定义原积分。

**U1（全部整系数上同调）。** 对每个整数 $n\geq0$，有
$$
H^0(S,L_n)=R\langle1\rangle,\qquad
H^1(S,L_n)\simeq\bigoplus_{j=1}^{n}R/(1-q^j),\qquad
H^i(S,L_n)=0\quad(i\geq2). \tag{U1}
$$
边界递增给出的 $H^1$ 短正合列逐级分裂。这里的同构不是额外的典范结构。

**U2（任意基变换的一个共同复形）。** 对每个固定 $n$，存在 $D(R)$ 中的同构
$$
R\Gamma(S,L_n)\simeq
R[0]\oplus\bigoplus_{j=1}^{n}K_j,
\qquad K_j=[R\xrightarrow{\,1-q^j\,}R], \tag{U2}
$$
$K_j$ 位于上同调次数 $0,1$。可以选取该同构使常数截面对应第一个 $R[0]$。
固定一次这样的选择后，对每个交换 $R$-代数 $A$，包括非约化、非平坦或非 Noetherian 的 $A$，
导出基变换得到关于 $A$ 自然的同构
$$
R\Gamma(S_A,L_{n,A})\simeq
A[0]\oplus\bigoplus_{j=1}^{n}[A\xrightarrow{\,1-q_A^j\,}A]. \tag{U2A}
$$
因此
$$
\begin{aligned}
H^0(S_A,L_{n,A})&\simeq A\oplus\bigoplus_{j=1}^{n}\operatorname{Ann}_A(1-q_A^j),\\
H^1(S_A,L_{n,A})&\simeq\bigoplus_{j=1}^{n}A/(1-q_A^j),\\
H^i(S_A,L_{n,A})&=0\quad(i\geq2).
\end{aligned} \tag{U3}
$$
第一式中的 $A$ 是真实常数子模。不声称通常的 $H^0$ 非平坦基变换可交换。

**U3（通用 Fitting 除子）。** 原通用有限呈示模满足
$$
\operatorname{Fitt}_0 H^1(S,L_n)
=\left(\prod_{j=1}^{n}(1-q^j)\right)
=\left(\prod_{d=1}^{n}\Phi_d(q)^{\lfloor n/d\rfloor}\right). \tag{U4}
$$
其中 $n=0$ 时空积生成单位理想，$\Phi_d$ 是整数圆分多项式。
这是指定上同调模的 Fitting 理想，不另定义任意跳跃概形或将不同模的 Fitting 理想混用。

## Status

**PROVABLE AS STATED（作者判断，等待针对本件的新非作者检查）。**
U1 的实质增量是无关系 $R$ 上的全部边界扩张；
U2–U4 是其经明确同调代数与基变换得到的推论，不分别计作三种新方法。
[DVR 分裂探针 S](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md)
已给通用根单位环上的截面引理；本件不由 DVR 特化反推通用结论。

## Assumptions

1. $q,\tau$ 始终为单位；不包括非单位参数。基变换 $A$ 继承此要求。
2. 相对模型的实际坐标为 G 的 $1+2+3+2$ 吹起：最后四点在不同边界分量，
   其坐标为 $1,\tau,\tau,q$。不得合并因不同分量坐标相等而看似相同的中心。
3. 消费已接受域上 T1 的精确阶 $d$ 原积分截面与极除子结论，
   以及 JR 的原矩阵迹、行列式恒等式；只在特征零域分支使用它们以建立下述引理。
4. [N 的节点帧](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)
   给八个传播比，其中非平凡者是 $-1/\tau,-1,-1/q,-\tau$。
   本件使用这些单位公式本身，而不是把域上线丛分类默认为任意基环上的分类。

## Notation

令 $a_j=1-q^j$，$B_j=R/(a_j)$。注意 $a_j\ne0$ 是无关系整环 $R$ 中的断言。
以 $T_n=H^1(S,L_n)$ 记通用上同调模；它不是 G 的固定 DVR 扭子记号。
原矩阵记为 $A(z)$，把原时间参数写作 $\tau$。
定义
$$
C_j=[z^j]\operatorname{tr}\bigl(A(q^{j-1}z)\cdots A(qz)A(z)\bigr)
\in B_j[x^{\pm1},y^{\pm1}]. \tag{U5}
$$
在非本原分支它不是把 $\operatorname{tr}M_j(1)-(\tau^j+1)$ 改名为积分。
令 $E$ 为完整环面补集，含 $D$ 及四条末端例外曲线。

## Proof Strategy

先直接计算通用曲面及节点环的上同调，产生扩张而不预设它们分裂。
再在每个 $B_j$ 上构造真实单位边界截面，以 Bockstein 自然性逐级分裂扩张。
最后用商模的长度一自由分解消除派生分解的二阶扩张障碍，
并只在复形层面应用任意基变换。

## Dependency Map

1. 实际八截面模型及局部吹起计算给 $R\Gamma(S,\mathcal O_S)=R[0]$。
2. 节点帧给 $R\Gamma(D,\mathscr N^j)=[R\xrightarrow{1-q^{-j}}R]$。
   边界短正合列因此给 $H^0$、高次消失及 $T_n$ 的扩张。
3. $B_j$ 截面引理给 $a_j$-扭的商生成元提升，证明每个扩张分裂，得到 U1。
4. $R/(a_j)$ 的投射维数至多一给 $\operatorname{Ext}^2_R(T_n,R)=0$，得到 U2。
5. proper、$R$-flat 可逆层的导出基变换给 U2A–U3；对角呈示给 U4。

## Proof

### Step 1. 通用模型及常数上同调

八个中心与边界的构造仅需求逆 $q,\tau$。
每个中心有两个相对参数，吹起图仍是两个参数的相对光滑图。
四个最终中心坐标为单位，故不落在节点；$S/R$ 光滑射影，$D$ 是相对 SNC 八环。
$E$ 也为相对 SNC Cartier 除子：在一个边界光滑点吹起时，
保留最后例外的完整总边界局部成为一个坐标超平面或两个坐标超平面之并。
因此 $E/R$ 平坦，且 $S\setminus E=(\mathbb G_m)^2_R$。

这里还需实际证明常数上同调，不从任意基变换的逐点维数猜出自由模。
仿射平面 $\mathbb A^2_R$ 在零截面的吹起是 $\mathbb P^1_R$ 上
$\mathcal O(-1)$ 的总空间。其到 $\mathbb P^1_R$ 的投影为 affine，
结构层的推前是 $\bigoplus_{k\geq0}\mathcal O(k)$。
两张标准仿射图的 Čech 计算给各 $\mathcal O(k)$ 高次上同调为零；
同一有限覆盖使此结论与该直和交换，次数零部分是 $R[u,v]$。
故吹起 $b$ 满足 $b_*\mathcal O=\mathcal O$ 及 $R^ib_*\mathcal O=0$（$i>0$）。
中心附近的实际图是这种模型的坐标变换及局部化，中心之外 $b$ 是同构，
所以该推前等式适用于每次实际吹起。
由 Leray，八次吹起保留 $R\Gamma(\mathcal O)$。
$\mathbb P^1_R\times_R\mathbb P^1_R$ 的标准四图计算给
$$R\Gamma(S,\mathcal O_S)=R[0]. \tag{U6}$$

### Step 2. 节点复形及不预设分裂的过滤

N 的实际帧在 $R$ 上给每个分量上的平凡线丛和单位节点粘合。
对相对节点 $R[u,v]/(uv)$，两分支正规化差值序列逐项正合。
张量 $\mathscr N^j$，八分量上的 $\mathbb P^1_R$ 只有常数上同调，
因此其全局上同调由 $[R^8\to R^8]$ 给出。
用节点单位消去七个可逆对后得到
$$
R\Gamma(D,\mathscr N^j)\simeq[R\xrightarrow{1-q^{-j}}R]. \tag{U7}
$$
此处 $1-q^{-j}=-q^{-j}a_j$ 为 $a_j$ 乘单位。
$R$ 是整环，故当 $j\geq1$ 时
$$H^0(D,\mathscr N^j)=0,\quad H^1(D,\mathscr N^j)=B_j,\quad H^{\geq2}=0.$$

对 $0\to L_{j-1}\to L_j\to\mathscr N^j\to0$ 取上同调，
由 (U6) 从 $j=1$ 开始归纳，得到
$$
H^0(S,L_j)=R\langle1\rangle,\quad H^{\geq2}(S,L_j)=0,
\quad 0\to T_{j-1}\to T_j\xrightarrow{\rho_j}B_j\to0. \tag{U8}
$$
这个消失论证只使用节点环的高次消失和边界序列，
没有在非局部基环上误用一次 Nakayama，也不需要先计算所有闭纤维。

### Step 3. 根单位整数基环上的截面引理

需要以下已经在 S 的 Steps 1–5 完整给出的具体引理：
$$
C_j\in H^0(S_{B_j},L_{j,B_j}),\qquad
C_j|_{D_{B_j}}\text{ 生成 }\mathscr N^j_{B_j}. \tag{U9}
$$
为标清此处真实依赖，记录其完整逻辑，不将分裂结论本身当作输入。
$B_j$ 作为 $\mathbb Z[\tau^{\pm1}]$-模自由，且有单射
$$B_j\hookrightarrow\prod_{d\mid j}\mathbb Q(\zeta_d)(\tau).$$
在精确阶 $d$ 分支，令 $k=j/d$，原矩阵块重复给 $M_j=M_d^k$。
二阶 Cayley–Hamilton 递推对 $[z^j]\operatorname{tr}M_d^k$ 给
$C_j=I_d^k$ 加关于 $I_d$ 的低次整数系数多项式。
域上 T1 因此使其在每一个分支都是 $L_j$ 截面。

这还不是 $B_j$ 上的整性证明。$C_j$ 在环面正则，故对于足够大的 $h$，
它是 $L_j(hE)$ 截面。商 $L_j(hE)/L_j$ 有有限过滤，
逐商为 $L_j(\ell E)|_E$（$1\leq\ell\leq h$）。
每个逐商在 $E$ 上可逆，且 $E/B_j$ 平坦，所以整个商对 $B_j$ 平坦。
张量上述单射保持商模的单射；$C_j$ 的商像在每个分支消失，因而原本消失。
于是 $C_j$ 已是整个 $B_j$ 上的 $L_j$ 截面；这不是非正规基环上的 Hartogs。

原 $A_1$ 的唯一负 $x$ 次项是
$-\tau x^{-1}\begin{pmatrix}1&0\\1&0\end{pmatrix}$，括号矩阵幂等且迹为一。
因此
$$[x^{-j}]C_j=(-\tau)^jq^{j(j-1)/2}\in B_j^*.$$
在 $x=0$ 边界分量的真实帧 $x^{-j}$ 中，它是单位。
各分量上的全局系数属于 $B_j$；沿节点的传播比为单位，乘积为 $q^{-j}=1$。
单位遂传播到整个八环，证明 (U9)。
此引理的下降与边界单位部分还在新的非作者检查中，本件不会把作者判断冒充接受。

### Step 4. 在无关系 $R$ 上逐级分裂

$S$ 与 $D$ 均对 $R$ 平坦，$a_j$ 是 $R$ 的非零因子。
分别对 $L_j$ 和 $\mathscr N^j$ 使用乘 $a_j$ 的层短正合列。
由边界序列 (U7)，其 Bockstein 给同构
$$
\beta_D:H^0(D_{B_j},\mathscr N^j_{B_j})\xrightarrow{\sim}H^1(D,\mathscr N^j)=B_j.
$$
在两项复形中该同态由 $(1-q^{-j})/a_j=-q^{-j}$ 实现，是一个单位。
曲面 Bockstein 给
$$v_j=\beta_S(C_j)\in T_j,\qquad a_jv_j=0.$$
连接同态关于边界限制的自然性保证
$$\rho_j(v_j)=\beta_D(C_j|_{D_{B_j}})\in B_j^*.$$
记此单位为 $b_j$。因为 $v_j$ 被 $a_j$ 杀死，其生成子模自然是 $B_j$-模，
可直接令 $\sigma_j(1)=b_j^{-1}v_j$，得到 $R$-线性截面 $\sigma_j:B_j\to T_j$。
这里不要求 $b_j$ 在 $R$ 中有单位提升；在非局部 $R$ 上这种要求并不必要。
由 $\rho_j\sigma_j=\operatorname{id}$，(U8) 逐级分裂，得到 U1。

### Step 5. 派生分解不能仅由上同调同构宣布

令 $C=R\Gamma(S,L_n)$。由 U1，它只有次数 $0,1$ 上同调。
常数映射 $R[0]\to C$ 在 $H^0$ 上同构，故截断三角为
$$R[0]\longrightarrow C\longrightarrow T_n[-1]\longrightarrow R[1].$$
每个 $B_j$ 有长度一自由分解
$$0\to R\xrightarrow{a_j}R\to B_j\to0.$$
U1 给 $\operatorname{Ext}^2_R(T_n,R)=0$。
于是上述三角的末箭头为零，三角分裂；可选取一个分裂保留原常数映射。
另一方面 $K_j$ 只有 $H^1(K_j)=B_j$，故 $K_j\simeq B_j[-1]$。
两者合成给 U2。此处确实检查了二阶扩张障碍，而不是认为任意复形都由其上同调决定。

### Step 6. 全部基变换与 Fitting 理想

$R$ Noetherian，$S/R$ proper，$L_n$ 相干且对 $R$ 平坦。
[Stacks Lemma 30.22.1](https://stacks.math.columbia.edu/tag/07VJ)
的两项条件因此适用：$R\Gamma(S,L_n)$ perfect，并对任意 $R\to A$ 满足导出基变换。
本轮主控实读该命题和完整证明；只引用这项通用工具，不把它计为本模型的新结果。
U2 的各项为有限自由模，所以导出张量可由逐项普通张量计算，得到 U2A。
取 kernel、cokernel 即得 U3，含 $A$ 非约化或非平坦时的 annihilator 项。

U1 的有限呈示矩阵为对角阵 $\operatorname{diag}(a_1,\ldots,a_n)$，
零阶 Fitting 理想由其行列式生成。
整数恒等式 $q^j-1=\prod_{d\mid j}\Phi_d(q)$ 中每个 $d$ 在 $1\leq j\leq n$
出现 $\lfloor n/d\rfloor$ 次，单位符号不影响理想，因此得到 U4。证毕。

## Remarks and Boundaries

在 G 的圆分 DVR 上令 $q=s,\tau=t,n=r$，U3 给
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j).$$
其中自由项来自 $j=r$。这与 S 的另一路 DVR 作者证明相符，却不是本件证明 U1 的前提。
全部初等因子可按 S 的 (S15) 读取；$n=r-1$ 的 Fitting 理想特化为 $(r)$。

U2 不声称选择在不同 $n$ 之间自动给出兼容的派生过滤同构。
它也不是截面环乘法、cup product、动力作用或相对对偶的同构。
尚未由这些模结构构造与 D 的整除微分之间的典范同构，
其数值相等不替代这种结构。
不研究非单位 $q,\tau$、稳定／半稳定约化或新能级规范。

## Corrections or Missing Assumptions

作者未发现需要缩小原 U1–U3 量词的步骤。
通用模型、非正规根单位环上的截面下降、边界 Bockstein 与派生二阶扩张消失
均是明确义务；不得用域上 $h^0$ 计数或圆分 DVR 的长度反推本件。

## Open Risks and Actual Reading

本件尚未独立接受。拟交非作者核查原 $R$ 上的扩张、常数推前与任意基变换接口，
不因此重开已接受 G1–G3 或旧 T1–T7。
来源查新另行进行；节点复形、Bockstein、Ext 消失、derived base change 和 Fitting 算术均为标准工具，
不能以这些工具的数量或公式数量宣称新意。

主控全文实读 G 254 行、G 独立报告 286 行、S 原 412 行及最终补充记号段，
当前 S 最终 SHA-256 为 `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac`。
N 在前阶段已全文实读，本件定向重读节点帧、$x=0$ 帧与单位传播段；
原矩阵消费 D 与 S 的准确式子。
按 proof-writer 写出准确命题、依赖和所有证明步骤；未改既有作者件、票、锁、入口或 PDF。
