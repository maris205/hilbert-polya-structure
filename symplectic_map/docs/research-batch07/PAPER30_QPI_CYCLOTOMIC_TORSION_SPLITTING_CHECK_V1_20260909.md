# Paper30 qPI：圆分扭子逐级分裂独立数学核查 V1

日期：2026-09-09。非作者核查者：`/root/p30_qpi_torsion_splitting_check_v1`。
类型：有界 fresh 数学证明核查；不是查新、正式票、Route 评价、立项或容量判断。

## Claim

核查[作者分裂探针 V1](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md)的原 (S1)、每一级边界扩张分裂，以及 (S14)–(S15) 的全部初等因子。
保持任意素数 $p$、整数 $a,m\geq1$、$p\nmid m$，并保持

$$
N=p^a,\qquad r=mN,\qquad s=\zeta_r,\qquad
\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p},\quad\mathfrak p\mid p,
\qquad t\in\mathcal O^\times.
$$

$\pi$ 是该 DVR 的任意参数，$e=v_\pi(p)$。在 G 指定的同一个相对八吹起曲面及边界上，令

$$
\mathcal L_j=\mathcal O_{\mathcal S}(j\mathcal D),\qquad
T_j=H^1(\mathcal S,\mathcal L_j)\quad(0\leq j<r),\qquad
\mathcal T=H^1(\mathcal S,\mathcal L_r)_{\rm tors}.
$$

准确待核结论是

$$
\mathcal T\simeq\bigoplus_{n=1}^{r-1}\mathcal O/(1-s^n),
$$

并且对每个 $1\leq n<r$，G 的原序列

$$
0\longrightarrow T_{n-1}\longrightarrow T_n
\xrightarrow{\rho_n}\mathcal O/(1-s^n)\longrightarrow0
$$

作为 $\mathcal O$-模序列分裂。零商包括在量词内。

## Status

**PROVABLE AS STATED；数学 PASS。**

原量词和原规范无需削弱。未发现必须修改作者稿的数学错误或未闭合引理。
本 PASS 消费已接受的 G 与域上 T1，不重做或重新颁发 G1–G3 的接受。
本报告不判断无关系通用环上同时计算全部相对上同调的其他主张。

| 实际核查对象 | 结论 | 决定性理由 |
|---|---|---|
| Step 1、4：完整环面补集 $E_n$ | PASS | 包含四条末端例外；局部方程为坐标或两个坐标之积，既是 Cartier 又相对平坦 |
| Step 2：非正规底环上的下降 | PASS | $L_n(kE_n)/L_n$ 是基环平坦层，故沿基环单射可检测其零截面 |
| Step 3：全部 $d\mid n$ 分支 | PASS | 准确系数是 $I_d^{n/d}$ 加低次多项式，非本原分支亦完整覆盖 |
| Step 5：边界单位及实际 N 帧 | PASS | 原矩阵唯一最高负 $x$ 次项给出单位；在 $x=0$ 分量确与 N 的 $x^{-n}$ 帧对齐 |
| Step 6–8：Bockstein 与分裂 | PASS | 提升被 $1-s^n$ 杀死，且边界像为循环商生成元，给出实际右逆 |
| (S14)–(S15)、小素数与任意单位 $t$ | PASS | 逐项赋值和重数计数；不由长度或 $h^0$ 跳跃猜分裂 |

## Assumptions

1. 相对中心、吹起次序、反典范边界、原矩阵及谱系数定义全部采用作者原规范。$t$ 必须为单位；不要求其一般，不排除 $p=2,3$，也不排除 $a=1$ 或 $m=1$。
2. [G 作者文件](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)及其[独立报告](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md)作为已接受依赖。本次实际消费的是边界两项复形、曲面上同调消失、原准确短正合列，以及 $T_{r-1}=\mathcal T$。
3. [brief V2 的 §2 与 T1](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)确实声称：每个特征零代数闭域、每个精确有限阶 $d\geq1$ 的 $q$ 和每个非零时间参数，都有同一八吹起模型上的 $I_d\in H^0(\mathcal O(dD))$，其极除子为 $dD$。该量词包括 $d=1$。这里只消费这个截面结论及 §2 的迹、行列式恒等式，不把 T1 升级为任意底环定理。
4. [N 的实际坐标、节点帧与传播计算](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)按原有向八环使用。其相对使用由显式单位坐标公式验证，不使用“各纤维次数零，所以任意底环上线丛平凡”的无效代替。

## Notation

$$
R_n=\mathbb Z[q^{\pm1},\tau^{\pm1}]/(q^n-1),\qquad
M_n(z)=A(q^{n-1}z)\cdots A(qz)A(z),\qquad
C_n=[z^n]\operatorname{tr}M_n(z).
$$

$X_n/R_n$ 是相同八截面吹起模型，$D_n$ 是八环反典范边界，$E_n$ 是完整环面补集的除子，包含 $D_n$ 和四条末端例外曲线。
记 $L_j=\mathcal O_{X_n}(jD_n)$、$\mathscr N=\mathcal O_{D_n}(D_n)$。
在 DVR 上令 $a_n=1-s^n$；对 $n<r$ 它非零。
边界或商底环上的层参与总曲面上同调时，均理解为相应闭浸入的推前。

## Proof Strategy

先独立核对 (S5)–(S7) 的整数截面和单位边界；再把这些实际截面送入 G 的原扩张，通过 Bockstein 的有限阶与自然性直接构造右逆。
最后在已经得到的直和上计算赋值。长度和最少生成元数只在最后作一致性推论。

## Dependency Map

1. 原模型坐标 $\Rightarrow$ $E_n$ 有效 Cartier、相对平坦且补集为原环面。
2. 全部特征零根单位分支上的 T1 与 Cayley–Hamilton $\Rightarrow$ $C_n$ 在各分支是 $L_n$ 截面。
3. 允许极点商平坦与基环单射 $\Rightarrow$ $C_n$ 在整个 $R_n$ 上是 $L_n$ 截面。
4. 原矩阵最高负 $x$ 次项与 N 的单位帧 $\Rightarrow$ 模 $a_n$ 截面的边界是单位生成元。
5. G 原扩张、乘 $a_n$ 的两个长正合列及自然性 $\Rightarrow$ 扩张右逆，归纳给 (S1)。
6. 已获直和与根单位赋值 $\Rightarrow$ (S14)–(S15)；不反向使用数值推断第 5 项。

## Proof

### Step 1. 完整 $E_n$ 的局部结构满足下降所需条件

四次节点吹起后，最后四中心位于四个不同分量的坐标 $1,\tau,\tau,q$ 处。
因 $q,\tau$ 可逆，中心不在任何节点；即使商底环上 $q=1$、$\tau=1$ 或 $q=\tau$，也不把不同分量上的截面合并。
每个吹起中心有相对坐标 $(u,v)$，理想为 $(u,v)$。两吹起图是多项式坐标图，且这些图及其粘合与任意底环特化相容。
因此这里不需要假设一般吹起与任意非平坦基变换无条件交换。

节点边界 $uv=0$ 吹起后，两图中的完整约化边界是两个坐标的乘积为零；
光滑边界 $u=0$ 吹起后，在 $(u,v/u)$ 图是 $u=0$，在 $(u/v,v)$ 图是 $(u/v)v=0$。
由此 $X_n/R_n$ 光滑，完整 $E_n$ 是相对 SNC 除子，没有遗漏末次例外，也没有三重交点。

即使底环有零因子，多项式环里的坐标 $u$ 和单项式 $uv$ 仍是非零因子，局部化保持这一性质。
故 $E_n$ 是有效 Cartier 除子。该判据对应 [Stacks 01WQ 的局部非零因子刻画](https://stacks.math.columbia.edu/tag/01WQ)。
另外 $R_n[u,v]/(u)$ 及 $R_n[u,v]/(uv)$ 有不含被禁止单项式的 $R_n$-基，所以相对平坦；局部化仍平坦。
全部中心均在原边界，故

$$
X_n\setminus E_n=(\mathbb G_m)^2_{R_n}.
$$

若改用 $D_n$，补集还含四条末端仿射直线，不能把初始 Laurent 正则性直接用于整个补集。
作者明确使用 $E_n$，该潜在缺口没有发生。

### Step 2. 允许极点商的平坦下降引理有效

在作者引理的任意基环 $B$ 上，设 $E/B$ 平坦且 $E$ 有效 Cartier，取 $k\geq0$。
置 $Q_j=L(jE)/L$。对 $j\geq1$ 有准确序列

$$
0\longrightarrow Q_{j-1}\longrightarrow Q_j
\longrightarrow L(jE)|_E\longrightarrow0.
$$

末项在 $E$ 上可逆且 $E/B$ 平坦，所以末项对 $B$ 平坦。平坦模的扩张仍平坦，归纳给 $Q_k$ 对 $B$ 平坦；所用代数事实的命题和证明已核对 [Stacks 00HM](https://stacks.math.columbia.edu/tag/00HM)。
局部取 $E=(f)$ 并平凡化 $L$，这个论证就是

$$
Q_k\simeq f^{-k}A/A\simeq A/(f^k),
$$

以 $A/(f)$ 为逐商的过滤；不需要 $B$ 或 $A$ 正规。

对单射 $B\hookrightarrow B'$，在每个仿射开集 $V$ 上令 $M=\Gamma(V,Q_k)$，其 $B$-平坦性给出 $M\hookrightarrow M\otimes_B B'$。
写 $g:X_{B'}\to X$，这就是层单射 $Q_k\hookrightarrow g_*g^*Q_k$，明确了单射两端所在的空间。
同时，$Q_k$ 平坦保证

$$
0\longrightarrow L\longrightarrow L(kE)\longrightarrow Q_k\longrightarrow0
$$

经基变换仍然正合；这使用的是平坦商保持张量后左端单射的事实，而不是要求 $B'$ 平坦，见 [Stacks 00HL](https://stacks.math.columbia.edu/tag/00HL)。
于是 $h$ 的商像在基变换后为零，就已在原层中为零。对该短正合列取全局截面的左正合性，得到 $h\in H^0(X,L)$。

此论证没有要求 $H^0$ 与非平坦基变换可交换。它只在局部平坦商中检测给定截面的零像，因而是对非正规 $R_n$ 的真实下降证明。

### Step 3. 全部除子分支的准确系数没有漏项

$R_n$ 在 $\mathbb Z[\tau^{\pm1}]$ 上以 $1,q,\ldots,q^{n-1}$ 为基自由。
张量 $\mathbb Q$ 后利用 $q^n-1=\prod_{d\mid n}\Phi_d(q)$ 的互素分解，再对每个 $\tau$ Laurent 环取分式域，得到单射

$$
R_n\hookrightarrow\prod_{d\mid n}\mathbb Q(\zeta_d)(\tau).
$$

这里不是声称不同圆分因子在整数环上互素；分支在剩余特征相交与此单射完全相容。

固定每个 $d\mid n$，令 $q=\zeta_d$、$k=n/d$。在原乘积顺序中，每长度 $d$ 的块完全相同，所以 $M_n=M_d^k$。
准确来源恒等式是

$$
\operatorname{tr}M_d=\tau^d+I_d w+w^2,\qquad
\det M_d=\varepsilon_d w^3,\qquad
w=z^d,\quad\varepsilon_d=(-1)^{d+1}.
$$

这些式子已与 brief V2 §2 的原矩阵和能级规范逐项对照。
二阶矩阵 Cayley–Hamilton 给整数递推 $P_k=XP_{k-1}-YP_{k-2}$，$P_0=2$、$P_1=X$。
对每个 $k\geq1$，$P_k$ 的 $Y$-零次项为 $X^k$，其余项的形式为整数倍 $Y^jX^{k-2j}$、$j\geq1$。
因此

$$
C_n=[w^k]P_k(\tau^d+I_dw+w^2,\varepsilon_dw^3)
=I_d^k+\sum_{\ell<k}b_{k,\ell}(\tau^d,\varepsilon_d)I_d^\ell.
$$

唯一的 $I_d^k w^k$ 来自 $X^k$ 的全部 $k$ 个因子选 $I_dw$；其他项的 $I_d$ 次数严格更小。
例如 $k=1,2,3$ 分别给 $I_d$、$I_d^2+2\tau^d$、$I_d^3+6\tau^dI_d-3\varepsilon_d\tau^d$，只作准确系数的低阶对照，证明本身由递推覆盖全部 $k$。
尤其非本原分支的 $C_n$ 不被误写为 $\operatorname{tr}M_n(1)-(\tau^n+1)$。

该分支的曲面就是参数 $(\tau,\zeta_d)$ 的原八吹起曲面。
T1 在特征零代数闭包给 $I_d\in H^0(\mathcal O(dD))$，并由域扩张的忠实平坦性下降到 $\mathbb Q(\zeta_d)(\tau)$。
每个幂 $I_d^\ell$ 都是 $\mathcal O(\ell dD)$ 截面，并通过有效 $D$ 的自然包含视作 $\mathcal O(nD)$ 截面。
故所有 $d\mid n$ 分支均通过，包含 $d=1$ 和 $d=n$。

### Step 4. 从 Laurent 环到全 $R_n$ 截面

在有限仿射覆盖上把 $E_n$ 写成非零因子 $f_i$ 的零集。
正则函数 $C_n$ 在各补集上属于 $A_i[f_i^{-1}]$，故各有有限分母幂；取最大幂得到某个 $k$。
各局部延拓在重叠上相等，因为有效 Cartier 补集是概形稠密的，局部自由层上的限制是单射；这一密性也见 [Stacks 01WQ](https://stacks.math.columbia.edu/tag/01WQ)。
于是 $C_n\in H^0(X_n,\mathcal O(kE_n))$，再由 $D_n$ 有效自然包含到 $H^0(X_n,L_n(kE_n))$。

Step 3 给其全部特征零分支属于 $H^0(L_n)$；Step 1、2 遂给

$$
C_n\in H^0(X_n,L_n).
$$

这是原作者 (S5)。一般非正规基环上并不允许仅凭泛纤维正则性下结论，但这里平坦商条件实际成立。
此后沿 $R_n\to\mathcal O/(a_n)$ 拉回这个已经构造的截面，只使用截面的自然拉回映射；不假设全部 $H^0$ 的基变换同构。

### Step 5. 最高负 $x$ 次项确为实际 N 帧中的单位

令

$$
E=\begin{pmatrix}1&0\\1&0\end{pmatrix}.
$$

原 $A_0$ 和 $P$ 没有负 $x$ 次项，原 $A_1$ 的全部 $x^{-1}$ 项准确为 $-\tau x^{-1}E$。
每个因子最低 $x$ 次数为 $-1$，所以乘积的 $x^{-n}$ 项只有一种选法。
由 $E^n=E$、$\operatorname{tr}E=1$ 得

$$
[x^{-n}]\operatorname{tr}M_n(z)
=(-\tau)^nq^{0+1+\cdots+(n-1)}z^n,
$$

因此 $C_n$ 在 $x=0$ 分量的最高极项系数为

$$
u_n=(-\tau)^nq^{n(n-1)/2}\in R_n^\times.
$$

不是仅有 $u_n\ne0$；它是单位，因为 $q,\tau$ 本来可逆，且没有整数分母。

N 的 Step 5 中，$B_1=\{x=0\}$ 在两个相邻节点都使用 $x^{-1}$，并在整个该分量上使用这一平凡化；$B_1$ 没有受到最后四次吹起的影响。
故上述系数准确属于所需 $x^{-n}$ 帧，不缺隐藏的 $y$ 或时间因子。
N 的其余四个非平凡分量使用坐标 $z$ 的一次消失因子 $z-\tau$、$y-1$、$z-q$、$z-\tau$；
把其指定中心除子减去后，得到实际平凡化，端点比为

$$
-1/\tau,\qquad-1,\qquad-1/q,\qquad-\tau.
$$

这些恒等式在 $R_n$ 上逐项成立，张量 $n$ 次后的总乘子是 $q^{-n}=1$。
不从零次多重次数推断任意基环上的平凡性，而是由这些具体帧构造 $\mathscr N^n\simeq\mathcal O_{D_n}$。

每个分量为 $\mathbb P^1_{R_n}$，其结构层全局截面为 $R_n$，故在该平凡化中的限制系数都是基环常数。
从 $B_1$ 上的单位 $u_n$ 沿环传播，每次只乘单位，得到每个分量上的单位系数。
节点也被这些帧覆盖，所以这给出整个 $D_n$ 上的生成元。
由可逆元拉回仍可逆，(S7) 包括任意非约化商底环上的截面生成性。

### Step 6. 原边界扩张与 Bockstein 自然性真正给出右逆

消费 G 的准确结论，对 $1\leq n<r$，

$$
R\Gamma(\mathcal D,\mathcal N^n)
\simeq[\mathcal O\xrightarrow{1-s^{-n}}\mathcal O],\qquad
1-s^{-n}=-s^{-n}a_n,
$$

故 $H^0(\mathcal D,\mathcal N^n)=0$、$H^1(\mathcal D,\mathcal N^n)=\mathcal O/(a_n)$，并有原序列

$$
0\longrightarrow T_{n-1}\longrightarrow T_n
\xrightarrow{\rho_n}H^1(\mathcal D,\mathcal N^n)\longrightarrow0.
$$

若 $a_n$ 为单位，商为零，该级分裂没有内容。
若它非单位，令 $\mathcal O_n=\mathcal O/(a_n)$。
$q\mapsto s\bmod a_n$、$\tau\mapsto t\bmod a_n$ 定义环同态 $R_n\to\mathcal O_n$。
Step 4、5 拉回给截面 $c_n\in H^0(\mathcal S_n,\mathcal L_{n,n})$，且其边界限制生成 $\mathcal N_n^n$。

由于 $\mathcal S$ 和 $\mathcal D$ 都对 DVR 平坦，乘 $a_n$ 的两个层序列均短正合。
其连接同态分别为 $\beta_{\mathcal S}$ 与 $\beta_{\mathcal D}$，于是

$$
v_n=\beta_{\mathcal S}(c_n)\in T_n,\qquad a_nv_n=0.
$$

边界序列的准确长正合列给

$$
0=H^0(\mathcal D,\mathcal N^n)
\longrightarrow H^0(\mathcal D_n,\mathcal N_n^n)
\xrightarrow{\beta_{\mathcal D}}H^1(\mathcal D,\mathcal N^n)
\xrightarrow{a_n}H^1(\mathcal D,\mathcal N^n).
$$

最后的乘法为零，因此 $\beta_{\mathcal D}$ 是同构。
同一节点复形模 $a_n$ 后微分为零，故左边非零项为 $\mathcal O_n$。
把全边界平凡化选成 $B_1$ 上系数为 $1$，则 $c_n$ 的边界系数为 $\bar u_n\in\mathcal O_n^\times$，所以它确实生成这个全局截面模。
在给定复形约定中，连接同态由提升后除以 $a_n$ 的微分给出，即乘 $-s^{-n}$，确为单位。

边界限制是 $\mathcal L_n\to i_*\mathcal N^n$ 的层态射，并与乘 $a_n$ 交换。
对这两个短正合列使用连接同态自然性，得到

$$
\rho_n(v_n)=\beta_{\mathcal D}(c_n|_{\mathcal D_n}).
$$

故 $\rho_n(v_n)$ 是循环商的生成元。
若其坐标为 $\overline b_n\in\mathcal O_n^\times$，因 $\mathcal O$ 局部且 $a_n$ 非单位，可取单位提升 $b_n\in\mathcal O^\times$。
定义

$$
\sigma_n:\mathcal O/(a_n)\longrightarrow T_n,\qquad
\overline1\longmapsto b_n^{-1}v_n.
$$

$a_nv_n=0$ 保证良定义，$\rho_n\sigma_n=\mathrm{id}$ 保证它是实际右逆。
因此该扩张在 $\operatorname{Ext}^1_{\mathcal O}(\mathcal O/(a_n),T_{n-1})$ 中的类为零。
这同时使用了“有限阶”和“商生成元”两个条件；没有用模 $a_n$ 截面存在本身替代分裂。

从 $T_0=0$ 归纳得到作者对所有 $j<r$ 的直和式。
再消费 G 已核闭的端点 $T_{r-1}=\mathcal T$，得到原 (S1)。
端点在 $n=r$ 时来自 $I_r$ 的单位边界限制和自由商，未被本报告重做或用于预设之前的扩张分裂。

### Step 7. 全部初等因子及边界参数

由 $\bar s$ 精确阶为 $m$，$1-s^n$ 非单位当且仅当 $m\mid n$。
取 $\xi=s^m$，$\xi$ 精确阶为 $N$，删除原直和中的零商即得

$$
\mathcal T\simeq\bigoplus_{j=1}^{N-1}\mathcal O/(1-\xi^j).
$$

令 $v_p(j)=b$，则 $\omega=\xi^j$ 精确阶为 $p^{a-b}$。
任意 $p$ 幂根单位在剩余域中都约化为 $1$；对 $p\nmid u$，

$$
\frac{1-\omega^u}{1-\omega}=1+\omega+\cdots+\omega^{u-1}
\equiv u\not\equiv0\pmod\pi
$$

（$u$ 取正整数代表），所以所有本原同阶根的 $1-\omega^u$ 具有同一赋值。
对 $h=a-b$ 使用

$$
\prod_{\substack{1\leq u\leq p^h\\p\nmid u}}(1-\omega^u)
=\Phi_{p^h}(1)=p
$$

得到 $v_\pi(1-\xi^j)=e/\varphi(p^{a-b})$。
在 $1\leq j<N$ 内，具有 $v_p(j)=b$ 的指标恰有 $\varphi(p^{a-b})$ 个，故

$$
\boxed{
\mathcal T\simeq
\bigoplus_{b=0}^{a-1}
\left(\mathcal O/\bigl(\pi^{e/\varphi(p^{a-b})}\bigr)\right)
^{\oplus\varphi(p^{a-b})}.
}
$$

各指数为实际赋值，因而为正整数；不需要添加某个特殊参数或额外分歧假设。
这就是 (S14)–(S15)，不是只计算乘积理想。

| 边界情形 | 准确结果与核查 |
|---|---|
| $p=2,a=1,m=1$ | $s=-1$、$\mathcal O=\mathbb Z_{(2)}$、$e=1$，唯一非零项为 $\mathcal O/(2)$；$C_1=y-x+x/y-\tau/x$ 的边界系数 $-\tau$ 为单位 |
| $p=3,a=1,m=1$ | $e=2$，$1-s$、$1-s^2$ 各赋值 $1$，故 $\mathcal T\simeq(\mathcal O/(\pi))^{\oplus2}$；这里 $3$ 与 $(1-s)^2$ 相差单位 |
| 任意 $p$、$a=1$、任意允许 $m$ | $\mathcal T\simeq(\mathcal O/(\pi^{e/(p-1)}))^{\oplus(p-1)}$，不排除 $m=1$ |
| 任意 $a$、$m=1$ | 所有 $1\leq n<r$ 都是非零循环商，按 $v_p(n)$ 分组正是上述全部 $a$ 层 |
| 任意 $t\in\mathcal O^\times$ | 证明只用 $t$ 的可逆性；即使其约化等于 $1$ 或 $\bar s$，中心仍分属不同分量，边界系数仍为单位 |

通用截面与分裂构造不需要在底环中求 $2$、$3$、$n$ 或 $d$ 的逆，且实际小素数的非约化商底环已由 Step 2、4、5 处理。
最后求和才得到

$$
\operatorname{length}_{\mathcal O}\mathcal T
=\sum_{b=0}^{a-1}e=ae,\qquad
\dim_\kappa(\mathcal T/\pi\mathcal T)
=\sum_{b=0}^{a-1}\varphi(p^{a-b})=N-1.
$$

它们与 G 一致，但不是分裂证明的输入。原全量词结论得证。$\square$

## Corrections or Missing Assumptions

没有必需的数学修正、量词削弱或额外假设。
以下条件是作者证明已具备、后续引用不得省略的真实接口：

1. 保留完整 $E_n$，而非只取 $D_n$；保留其有效 Cartier 和相对平坦性。
2. 分支下降必须覆盖每个 $d\mid n$，并使用给定 $C_n$ 的谱系数定义。
3. 对非正规 $R_n$ 必须使用平坦允许极点商的单射，不可以改写成仅凭稠密泛纤维或 Hartogs。
4. 边界必须是 N 的实际帧中的单位，而非只在特征零非零。
5. Bockstein 必须同时给被 $a_n$ 杀死的提升和商生成元；本证明两者均已核实。

## Open Risks

在本次原 (S1)、逐级分裂和 (S14)–(S15) 范围内没有未闭合证明义务。
分裂与动力、乘法、对偶或其他指定结构的相容性未在作者稿声称，本报告也未证明。
这里的非典范模分裂不自动产生任何上述结构的典范分裂。
无关系通用环上的全部相对上同调、其他稳定约化或微分高阶问题不在本次审查范围。

## 实际阅读与输入绑定

最初派发提到 412 行及 `8dbfd5a8…`；首次实际读到作者补齐记号后的 418 行。
主控随后明确将本任务绑定到下表所列最终 418 行版本；本报告全文核查的是这一最终版本，未声称读过不存在的冻结旧版。

| 文件 | 核查者实际阅读范围 | SHA-256 |
|---|---|---|
| [分裂探针 V1](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 全文 1–418 行，全部八步骤与 (S1)–(S15) | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` |
| [G 作者 V1](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 全文 1–254 行；消费已接受依赖，不重审 G1–G3 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [G 独立核查 V1](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | 全文 1–286 行；核对已接受接口和不声称旧扭子扩张分裂的边界 | `ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b` |
| [brief V2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md) | 定向实读 35–145 行；实际使用 §2 原矩阵/迹恒等式、T1；末端触及 T2 标题与开式但未审 T2 | `b8f1ca66927b977b05a2996e42d299390d6a895d1a3378119d1be5415d70a00f` |
| [N 作者入口](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 定向实读 65–284 行；实际核对中心、八环、Step 5–7 帧与传播 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |

治理与接续阅读：工作区 `AGENTS.md` 全文 28 行，SHA-256 `73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412`；
`docs/WORKFLOW.md` 全文 39 行，SHA-256 `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2`；
`proof-writer/SKILL.md` 全文 223 行，SHA-256 `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe`。
`BATCH_07_CONTEXT.md` 只作关键词定位及实读 1–110 行接续定位，读取时全文件 SHA-256 `4d11047ef4b883d78f34149981a1054e6fbc44555e61b1291c4754f9f115b7d5`；不将余下历史账本记作全文实读。

外部只核对 Stacks 的标准数学工具：00HM、00HL 的命题与证明及 01WQ 的 Cartier 局部刻画和补集密性；未做一般查新或来源新意评价。
未读取旧 47 件输入、未审主控其他新通用环命题、未数值抽样代替证明、未运行实验或改入口。
核查者亲读技能及上述全部声明范围，并独立完成主证明检查。
辅助代理 `/root/p30_qpi_torsion_splitting_check_v1/flat_bockstein_spotcheck` 只接收两个抽象论证，完成不写文件的纯代数反向点检，结论均为可证。
其指出须明确自然限制映射及单位截面对全局截面模的生成性；本报告 Step 5–6 已逐项核实。这项辅助不替代核查者对作者最终全文和实际模型的独立检查。
唯一新增文件是本报告；作者探针、G、N、brief、旧接受件、锁和产物均未修改。
