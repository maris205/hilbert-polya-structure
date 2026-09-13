# Paper30 qPI：圆分上同调扭子的分裂探针 V1

日期：2026-09-09。作者：子代理 `/root/p30_qpi_cyclotomic_torsion_splitting_probe_v1`。
类型：有界作者理论诊断；不是 G 的独立审查、正式评分、立项或论文稿。
proof_status：PROVABLE AS STATED（本件作者证明，尚未独立接受）。

## Claim

保持 [G 的完整模型与全部原假设](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)：
任意素数 $p$，整数 $a,m\geq 1$，$p\nmid m$，
$$
N=p^a,\qquad r=mN,\qquad s=\zeta_r,\qquad
\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p},\quad \mathfrak p\mid p,
$$
且 $t\in\mathcal O^*$。令 $\pi$ 为 $\mathcal O$ 的参数，$e=v_\pi(p)$。
在 G 指定的相对八吹起曲面 $\mathcal S/\mathcal O$ 上，令
$$
\mathcal L_n=\mathcal O_{\mathcal S}(n\mathcal D),\qquad
\mathcal T=H^1(\mathcal S,\mathcal L_r)_{\mathrm{tors}}.
$$
本件检验并证明原先没有在 G2c 声称的加强：
$$
\boxed{\quad
\mathcal T\simeq\bigoplus_{n=1}^{r-1}\mathcal O/(1-s^n).
\quad} \tag{S1}
$$
更精确地，G2c 的每一级短正合列都作为 $\mathcal O$-模序列分裂。
这里不把“有过滤”当作“过滤已分裂”：额外输入是下文构造的有限阶 Bockstein 提升。
本件不声称分裂与任意未指定的动力、乘法或对偶结构相容。

## Status

**PROVABLE AS STATED。** 原目标没有缩小参数范围，没有加入 $t$ 一般、$p>3$、
额外 ramification 或基环正规等假设。证明依赖已接受的域上 T1，
以及 G 中同一相对模型的边界上同调序列；后者在此写出所需部分。
本件的作者判断不代替 G1–G3 的独立报告，也不意味着本件已获独立接受。

实质的新步骤是：先在
$$
R_n=\mathbb Z[q^{\pm1},\tau^{\pm1}]/(q^n-1)
$$
上证明通用迹系数是完整模型截面，再沿 $R_n\to\mathcal O/(1-s^n)$ 拉回。
这里 $\tau$ 是通用时间参数，避免与已固定的 $t\in\mathcal O^*$ 混淆。
$R_n$ 本身对整数无扭且约化，但一般不正规；其模素数纤维可以非约化。
证明没有把特征零分支的结论直接宣布为整性，也没有在 $R_n$ 上使用 Hartogs。

## Assumptions

1. 曲面、八个中心的次序、边界、矩阵顺序均保持 G 与
   [brief V2 §2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md) 的原规范。
2. 复用域上 T1：精确阶为 $d$ 的根单位参数给出
   $I_d\in H^0(S,\mathcal O(dD))$ 及 $(I_d)_\infty=dD$。
   这里只在特征零域上使用这一已接受输入；不把它直接升级成任意基环命题。
3. 复用 [N 的 Step 5–7](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)
   的显式节点帧和传播比。那些公式只含 $q,\tau$ 的求逆，因而可在本件基环上逐项实施。
4. 不变更 G、D、旧接受件、入口或任何锁。本件只处理原 $\mathcal O$-模分裂。

## Notation

- $A(z)$ 为原矩阵，在通用构造中把原时间参数写为 $\tau$：
  $$
  A(z)=A_0+zA_1+z^2P,\qquad P=\operatorname{diag}(1,0),
  $$
  $$
  A_0=\begin{pmatrix}
  \tau+x-xy&-x\\
  \tau+x-\tau y-2xy+xy^2&x(y-1)
  \end{pmatrix},
  $$
  $$
  A_1=\begin{pmatrix}
  y-x+x/y-1-\tau/x&1\\
  y-2x-1+xy+x/y-\tau/x&1
  \end{pmatrix}.
  $$
- 对每个整数 $n\geq1$，定义通用 Laurent 多项式
  $$
  M_n(z)=A(q^{n-1}z)\cdots A(qz)A(z),\qquad
  C_n(q,\tau;x,y)
  =[z^n]\operatorname{tr}M_n(z)
  \in R_n[x^{\pm1},y^{\pm1}]. \tag{S2}
  $$
  在 $q$ 非本原时，不把 $C_n$ 改定义为 $\operatorname{tr}M_n(1)-(\tau^n+1)$；
  后一个表达式通常还有其他谱次数的贡献。
- $X_n/R_n$ 是按 G 的相同八个相对截面吹起所得曲面，$D_n$ 是八分量反典范环；
  $E_n$ 是原环面补集的完整约化除子，故包括 $D_n$ 与四条末端例外曲线。
- $L_j=\mathcal O_{X_n}(jD_n)$，$\mathscr N=\mathcal O_{D_n}(D_n)$；
  圆分 DVR 模型上的对应线丛仍记为 $\mathcal L_j$、$\mathcal N$。
- 对 $0\leq j<r$，记 $T_j=H^1(\mathcal S,\mathcal L_j)$，其中 $T_0=0$。
  对 $1\leq j<r$，记 $a_j=1-s^j\ne0$。

## Proof Strategy

证明一个允许极点商的平坦下降引理。它使 $C_n$ 在所有特征零根单位分支上的完整正则性
下降到整个 $R_n$，包括之后的非约化特化。
再直接由原矩阵的 $x^{-1}$ 项计算边界单位。
最后用乘 $a_n$ 的 Bockstein 和边界限制的自然性，
在 $T_n$ 中构造一个被 $a_n$ 杀死且映向 $\mathcal O/(a_n)$ 生成元的元素。

## Dependency Map

1. (S1) 依赖每个 $0\to T_{n-1}\to T_n\to\mathcal O/(a_n)\to0$ 的分裂。
2. 每一步分裂依赖一个 $a_n$-扭的商生成元；由 Bockstein 及其边界自然性给出。
3. 这个生成元依赖模 $a_n$ 的完整截面及其单位边界限制。
4. 模 $a_n$ 截面来自 $R_n$ 上的 $C_n$；整性依赖允许极点商的基环平坦性，
   并以域上 T1 和二阶矩阵的 Cayley–Hamilton 递推检验特征零各分支。
5. 边界系数直接从原 $A_1$ 的秩一最高负 $x$ 次项计算，
   不由泛点非零推断整数单位。

## Proof

### Step 1. 通用模型与完整环面边界

G 的八次吹起同样可在 $R_n$ 上实施：四次节点吹起后，
四个最后中心位于四个不同边界分量上，其坐标为 $1,\tau,\tau,q$。
这些都是单位，故不会遇到边界节点。

节点处的局部模型是 $R_n[u,v]$ 中的 $uv=0$。
在一个边界光滑点吹起时，局部模型为边界 $u=0$、中心 $u=v=0$。
其两张图为 $(u,v/u)$ 与 $(u/v,v)$；约化总变换分别是一个坐标超平面或两个坐标超平面之并。
因此 $X_n/R_n$ 光滑，$E_n$ 是相对 SNC 除子。
由于全部中心都在环面之外，
$$
X_n\setminus E_n=(\mathbb G_m)^2_{R_n}.
$$
特别地 $E_n\to\operatorname{Spec}R_n$ 平坦。
在坐标模型中，该平坦性来自 $R_n[u,v]/(u)$ 或 $R_n[u,v]/(uv)$
作为 $R_n$-模的单项式基；局部化及相对坐标变换保持这一性质。
这里使用的是完整 $E_n$，不能用不含末端例外的 $D_n$ 代替环面补集。

### Step 2. 允许极点商的平坦下降引理

使用以下引理，其证明不要求基环正规或是整环。

**引理。** 设 $B\hookrightarrow B'$ 是单射环同态，$X/B$ 是拟紧概形，
$E\subset X$ 是有效 Cartier 除子且 $E/B$ 平坦，$L$ 是可逆层。
若 $h\in H^0(X,L(kE))$ 对某个 $k\geq0$ 成立，
且 $h_{B'}\in H^0(X_{B'},L_{B'})$，则 $h\in H^0(X,L)$。

**证明。** 对 $k=0$ 没有待证事项。对 $k\geq1$，商层
$$
Q=L(kE)/L
$$
有有限过滤，其逐商为
$$
L(jE)|_E,\qquad 1\leq j\leq k.
$$
这些层在 $E$ 上可逆，故对 $B$ 平坦。平坦模的扩张平坦，所以 $Q$ 对 $B$ 平坦。
局部在仿射开集上，张量 $B\hookrightarrow B'$ 保持单射，得到
$$
Q\hookrightarrow Q\otimes_B B'.
$$
由于 $Q$ 平坦，序列 $0\to L\to L(kE)\to Q\to0$ 在基变换后仍然正合。
$h$ 在 $Q$ 中的像于基变换后为零，由上述单射，该像本来就是零。
故 $h$ 来自 $H^0(X,L)$。证毕。

这一步给出的是实际模单射，不是“在稠密特征零点为零，故在奇异整数模型上正则”。
在本件取 $B=R_n$；也可以先以 $B'=R_n\otimes\mathbb Q$ 使用整数无扭的版本，
但下文一次嵌入到各分支的函数域更直接。

### Step 3. 在每个特征零分支上，$C_n$ 是低阶积分的首一多项式

$R_n$ 是 $\mathbb Z[\tau^{\pm1}]$ 上以 $1,q,\ldots,q^{n-1}$ 为基的自由模。
由于特征零的 $q^n-1$ 平方自由，有单射
$$
R_n\hookrightarrow B'
:=\prod_{d\mid n}\mathbb Q(\zeta_d)(\tau), \tag{S3}
$$
其中第 $d$ 个分支令 $q=\zeta_d$。这也直接证明 $R_n$ 约化。

固定一个分支，记其域为 $K_d=\mathbb Q(\zeta_d)(\tau)$，
对应基变换为 $(X_{n,d},D_{n,d})$；令 $d$ 为 $q$ 的精确阶，$k=n/d$。
按原矩阵顺序，长度为 $d$ 的块重复 $k$ 次，故
$$
M_n(z)=M_d(z)^k.
$$
记 $w=z^d$。原域上迹、行列式恒等式给出
$$
\operatorname{tr}M_d=\tau^d+I_dw+w^2,
\qquad \det M_d=\varepsilon_dw^3,
\qquad \varepsilon_d=(-1)^{d+1}.
$$
定义整数多项式
$$
P_0(X,Y)=2,\quad P_1(X,Y)=X,\quad
P_k(X,Y)=XP_{k-1}(X,Y)-YP_{k-2}(X,Y).
$$
对任意二阶矩阵，Cayley–Hamilton 等式乘矩阵幂并取迹给出
$\operatorname{tr}(M^k)=P_k(\operatorname{tr}M,\det M)$。
递推还给出 $P_k(X,Y)$ 的首项是 $X^k$，其余单项式均形如 $Y^jX^{k-2j}$，$j\geq1$。
因此
$$
\begin{aligned}
C_n
&=[w^k]P_k(\tau^d+I_dw+w^2,\varepsilon_dw^3)\\
&=I_d^k+\sum_{\ell=0}^{k-1}b_{k,\ell}(\tau^d,\varepsilon_d)I_d^\ell,
\end{aligned} \tag{S4}
$$
其中系数为整数多项式。
首项系数为 $1$ 的理由是：$X^k$ 中选取全部 $I_dw$ 给出唯一的 $I_d^kw^k$；
其余 $Y^jX^{k-2j}$ 的 $I_d$ 次数至多为 $k-2j<k$。

该分支的八个中心正是参数 $(\tau,\zeta_d)$ 的原中心。
域上 T1 给 $I_d\in H^0(X_{n,d},\mathcal O(dD_{n,d}))$，
所以 (S4) 是 $H^0(X_{n,d},\mathcal O(nD_{n,d}))$ 的截面。
这里对任意 $d\mid n$ 都进行了检验，不能只核对本原 $n$ 阶分支。
若从 T1 的代数闭域版本开始，先到该函数域的代数闭包应用，
再利用域扩张的忠实平坦性下降上述截面即可。

### Step 4. 下降到整个 $R_n$ 的完整整数截面

$C_n$ 起初是 $X_n\setminus E_n$ 上的 Laurent 多项式。
对于拟紧概形与有效 Cartier 除子，任何补集上的正则函数都允许某个有限阶的 $E_n$ 极点：
局部写为边界方程的有限次幂分母，再取有限仿射覆盖上的最大阶数。
所以对足够大的 $k$，
$$
C_n\in H^0(X_n,L_n(kE_n)).
$$
Step 3 说明其在 (S3) 的每个分支都属于 $H^0(L_n)$。
Step 1 的 $E_n/R_n$ 平坦性与 Step 2 的引理遂给出
$$
\boxed{\quad C_n\in H^0(X_n,L_n)\quad}\qquad(n\geq1). \tag{S5}
$$
整个下降使用 $L_n(kE_n)/L_n$ 的 $R_n$-平坦性，
并没有把非正规基环上的任意有理函数正则性仅靠泛纤维来判断。
此后沿任意 $R_n$ 的商环拉回 (S5) 都会给出真实截面；
不需要、也不声称该非平坦基变换使 $H^0$ 普遍可交换。

### Step 5. 边界限制是显式单位

仅仅在每个特征零分支边界上非零，不足以断言整数边界单位。
这里从原矩阵直接计算它。
取
$$
E=\begin{pmatrix}1&0\\1&0\end{pmatrix},
\qquad E^2=E,\qquad\operatorname{tr}E=1.
$$
在 $x=0$ 的 Laurent 展开中，$A_0$ 与 $P$ 没有负 $x$ 次项，
而 $A_1$ 的唯一负 $x$ 次项是 $-\tau x^{-1}E$。
长度 $n$ 的矩阵乘积中，取得 $x^{-n}$ 必须在每个因子选取这一项，故
$$
[x^{-n}]\operatorname{tr}M_n(z)
=(-\tau)^nq^{n(n-1)/2}z^n.
$$
于是
$$
C_n=u_nx^{-n}+O(x^{-n+1}),\qquad
u_n=(-\tau)^nq^{n(n-1)/2}\in R_n^*. \tag{S6}
$$
这里 $O$ 只表示较高的 Laurent 次数。

N 的显式有向帧传播给 $\lambda(\mathscr N)=q^{-1}$。
这项计算在 $R_n$ 上仍成立，因为四个传播比是
$-1/\tau,-1,-1/q,-\tau$，全部为单位。
因此 $\mathscr N^n$ 的全部粘合可归一，最后一项为 $q^{-n}=1$，
即 $\mathscr N^n\simeq\mathcal O_{D_n}$。
在 $x=0$ 分量上，N 指定的帧为 $x^{-1}$，其 $n$ 次幂为 $x^{-n}$。
(S6) 说明 $C_n|_{D_n}$ 在这一分量上的系数是单位 $u_n$；
各分量上的限制线丛都平凡，而 $H^0(\mathbb P^1_{R_n},\mathcal O)=R_n$，
所以截面在每个分量上的系数为基环常数。
沿八环的传播比全是单位，故在每个分量、节点及整个基环上均为单位。
得到
$$
\boxed{\quad C_n|_{D_n}\text{ 生成可逆层 }\mathscr N^n.\quad} \tag{S7}
$$
这包括非约化商环上的拉回，不是只在约化点集上非零。

### Step 6. 原 DVR 上的准确扩张

现在回到原 $\mathcal O$、$s$、$t$、$\mathcal S$。
G 的节点正规化计算在指定帧下给出
$$
R\Gamma(\mathcal D,\mathcal N^n)
\simeq[\mathcal O\xrightarrow{\,1-s^{-n}\,}\mathcal O]. \tag{S8}
$$
对 $1\leq n<r$，$a_n=1-s^n$ 非零，且
$$
1-s^{-n}=-s^{-n}a_n.
$$
因此
$$
H^0(\mathcal D,\mathcal N^n)=0,
\qquad H^1(\mathcal D,\mathcal N^n)\simeq\mathcal O/(a_n).
$$
由 G 的 $H^1(\mathcal S,\mathcal O)=0$、$H^2(\mathcal S,\mathcal L_j)=0$
及边界短正合列，得到所需的原扩张
$$
0\longrightarrow T_{n-1}\longrightarrow T_n
\xrightarrow{\rho_n}H^1(\mathcal D,\mathcal N^n)
\longrightarrow0. \tag{S9}
$$
其端点识别是 $T_{r-1}=\mathcal T$：在 $n=r$ 处，
原 $I_r$ 的单位边界限制消去连接同态，剩余商为自由秩一模。
这一步只重述 G2 所需的准确序列，不以任何方式预设 (S9) 分裂。

### Step 7. Bockstein 提升的自然性与有限阶

若 $a_n$ 是单位，则 (S9) 的商为零，本级没有扩张问题。
以下令 $a_n$ 非单位，并置 $\mathcal O_n=\mathcal O/(a_n)$。
存在环同态
$$
R_n\longrightarrow\mathcal O_n,\qquad q\longmapsto s\bmod a_n,
\quad\tau\longmapsto t\bmod a_n.
$$
八个中心及其坐标在这个特化下完全相同。
拉回 (S5)–(S7) 得到
$$
c_n\in H^0(\mathcal S_n,\mathcal L_{n,n}),\qquad
c_n|_{\mathcal D_n}\text{ 生成 }\mathcal N^n_n, \tag{S10}
$$
其中下标 $n$ 表示模 $a_n$ 基变换。
$\mathcal S$ 与 $\mathcal D$ 均对 $\mathcal O$ 平坦，故乘非零 $a_n$ 给出层短正合列
$$
0\to\mathcal L_n\xrightarrow{a_n}\mathcal L_n\to\mathcal L_{n,n}\to0,
\qquad
0\to\mathcal N^n\xrightarrow{a_n}\mathcal N^n\to\mathcal N^n_n\to0.
$$
右端层以对应闭浸入的推前理解。
分别记其连接同态为 $\beta_{\mathcal S}$ 与 $\beta_{\mathcal D}$。
由第一个序列，
$$
v_n:=\beta_{\mathcal S}(c_n)\in T_n,
\qquad a_nv_n=0. \tag{S11}
$$
对第二个序列，$H^0(\mathcal D,\mathcal N^n)=0$，
而 $a_n$ 杀死 $H^1(\mathcal D,\mathcal N^n)$，所以准确长正合列给出同构
$$
\beta_{\mathcal D}:
H^0(\mathcal D_n,\mathcal N^n_n)
\xrightarrow{\ \simeq\ }H^1(\mathcal D,\mathcal N^n). \tag{S12}
$$
按 (S8) 的约定，$\beta_{\mathcal D}$ 在两项复形上由
$(1-s^{-n})/a_n=-s^{-n}$ 给出，是一个单位；
即使改变节点定向使连接同态多一个符号，同构与生成元结论也不改变。

边界限制与乘 $a_n$ 组成交换图，连接同态的自然性给出
$$
\rho_n(v_n)=\beta_{\mathcal D}(c_n|_{\mathcal D_n}). \tag{S13}
$$
(S10) 是一个单位截面，(S12) 是同构，所以 (S13) 是
$H^1(\mathcal D,\mathcal N^n)\simeq\mathcal O/(a_n)$ 的生成元。
这准确核对了需要的 Bockstein，而非仅凭模 $a_n$ 有截面就宣布 (S9) 分裂。

### Step 8. 分裂及 elementary divisors

令 (S13) 在选定的 $\mathcal O/(a_n)$ 坐标中等于单位 $\overline b_n$。
选取一个提升 $b_n\in\mathcal O^*$，则
$$
\sigma_n:\mathcal O/(a_n)\longrightarrow T_n,
\qquad \overline1\longmapsto b_n^{-1}v_n
$$
由 (S11) 良定义，而且 $\rho_n\sigma_n=\operatorname{id}$。
所以每个 (S9) 分裂，归纳得到
$$
T_j\simeq\bigoplus_{n=1}^{j}\mathcal O/(1-s^n)
\quad(0\leq j<r).
$$
在 $j=r-1$ 代入 $T_{r-1}=\mathcal T$ 即得 (S1)。证毕。

还可不加入新的几何假设而读出全部非零 elementary divisors。
因为 $\bar s$ 的精确阶为 $m$，$1-s^n$ 非单位当且仅当 $m\mid n$。
令 $\xi=s^m$，则 $\xi$ 的精确阶为 $N$，且
$$
\mathcal T\simeq\bigoplus_{j=1}^{N-1}\mathcal O/(1-\xi^j). \tag{S14}
$$
若 $v_p(j)=b$，$0\leq b<a$，则 $\xi^j$ 是精确 $p^{a-b}$ 阶根单位。
对一个精确 $p^h$ 阶根单位 $\omega$，各 $p\nmid u$ 的
$(1-\omega^u)/(1-\omega)$ 的约化为非零 $u$，因而是单位。
结合 $\Phi_{p^h}(1)=p$，得到
$$
v_\pi(1-\xi^j)=\frac{e}{\varphi(p^{a-b})}.
$$
具有 $v_p(j)=b$ 的 $j\in\{1,\ldots,N-1\}$ 恰有 $\varphi(p^{a-b})$ 个，故
$$
\boxed{\quad
\mathcal T\simeq
\bigoplus_{b=0}^{a-1}
\left(\mathcal O/\bigl(\pi^{\,e/\varphi(p^{a-b})}\bigr)\right)^{\oplus\varphi(p^{a-b})}.
\quad} \tag{S15}
$$
式中各指数是整数，因为它们已被证明等于实际赋值；这里不需要另取特定参数或另用圆分 ramification 公式。
这给回
$$
\operatorname{length}_{\mathcal O}\mathcal T=ae,
\qquad\dim_\kappa\mathcal T/\pi\mathcal T=N-1,
$$
但本件的分裂论证不以这两个数值等式为依据。

## Corrections or Missing Assumptions

没有反例，也没有在本件目标 (S1) 中发现额外假设需求。
必须保留的论证条件如下。

1. 特征零测试必须覆盖每个 $d\mid n$；非本原分支上的 $C_n$ 不是直接换名为 $I_n$。
2. 必须证明允许极点商平坦，才可以从 (S3) 下降正则性。
   只说“特征零点稠密”或者对非正规基环使用余维一延拓均不够。
3. 必须取完整环面补集 $E_n$，并计算显式单位 (S6)；泛纤维非零不足以保证单位。
4. 必须使用 (S12)–(S13) 检查边界 Bockstein 的像。
   一个模 $a_n$ 截面本身并不自动分裂任意扩张。

## Open Risks

- 本件是新的作者证明，尚未经过针对 Step 2、Step 4 与 Step 7 的独立检查；
  不代签 G 的独审，也不把本文状态升格为独立接受。
- 域上 T1 及 G2 的准确上同调序列是本件明确依赖；若其实际输入发生改变，
  只需检查相应消费者，不由本件授权重开整个旧包。
- 这里只计算固定原模型的 $\mathcal O$-模结构。
  分裂与 cup product、动力作用、相对对偶或额外典范结构的相容性未研究。
- 在无关系通用环 $\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 上同时计算全部 $H^1(L_n)$，
  以及由其导出基变换重建 $n=r$ 的自由项，是自然的进一步命题；本件没有证明或采用它。
- 未做查新、评分、无限 CAS、稳定／半稳定模型分类或新的能级规范变换。

## 实际读取与变更边界

完整读取 G 作者文件、工作区 `AGENTS.md`、`docs/WORKFLOW.md` 及 `proof-writer` 技能。
定向读取 brief V2 §2 的原矩阵与域上 T1、N 的节点帧／传播段，以及 D 的原矩阵约定；
没有重新加载旧 47 件输入，没有把任何来源恒等式计为本件首创。
唯一新增文件是本件；未改 G、D、入口、冻结原稿或旧接受产物。
