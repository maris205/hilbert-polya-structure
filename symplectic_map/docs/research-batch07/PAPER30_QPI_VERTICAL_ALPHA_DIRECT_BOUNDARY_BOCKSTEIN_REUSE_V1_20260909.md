# Paper30 qPI：首层实际 Bockstein 的直接八环证明复用

日期：2026-09-09。作者：主控 `/root`。
类型：同一首层命题的有界替代证明；不是新的独立 finding 或新意票。
`route_applicability: NOT_APPLICABLE`。

## Claim

保持 [TH](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)
的全部首层量词。取素数 $p$、$m\ge1$、$p\nmid m$，无分歧 $p$-进 DVR
$\mathcal O_0$ 含精确 $m$ 阶单位根 $\widetilde\eta$，其剩余域 $k$ 完美。
置
$$\mathcal O=\mathcal O_0[\zeta_p],\quad \pi=\zeta_p-1,\quad
s=\widetilde\eta\zeta_p,\quad A_2=\mathcal O/(\pi^2),\quad t\in\mathcal O^\times.$$
原八截面光滑射影模型为 $S/\mathcal O$，相对反典范八环为 $D$，
$$L_n=\mathcal O_S(nD),\qquad \mathscr N=\mathcal O_D(D),\qquad U=S\setminus D.$$
保留原矩阵、原积分 $J=I_{m,\eta}(x,y;\bar t)$，不重定义能级。
上标或下标 $A$ 表示对 $A\in\{A_2,k\}$ 的实际基变换。

**DB.1（低层及真实边界）。** 对每个 $0\le n<m$ 及上述 $A$，
$$H^0(S_A,L_{n,A})=A\langle1\rangle,\qquad
H^i(S_A,L_{n,A})=0\quad(i>0). \tag{DB1}$$
这里 $1$ 是原常数截面，不是另选直和基向量。
在 $k$ 上，实际边界限制给正合列及同构
$$0\longrightarrow k\langle1\rangle\longrightarrow H^0(S_k,L_{m,k})
\xrightarrow{r_0}H^0(D_k,\mathscr N_k^m)\longrightarrow0,$$
$$r_1:H^1(S_k,L_{m,k})\xrightarrow{\sim}H^1(D_k,\mathscr N_k^m),
\qquad H^{\ge2}(S_k,L_{m,k})=0. \tag{DB2}$$
DB2 右侧两个群各为一维 $k$-空间。

**DB.2（实际首层连接）。** 用底环短正合列
$0\to k\xrightarrow{\pi}A_2\to k\to0$ 定义实际层的 Bockstein
$$\beta_L:H^0(S_k,L_{m,k})\longrightarrow H^1(S_k,L_{m,k}).$$
它与边界 Bockstein $\beta_D$ 满足
$$r_1\beta_L=\beta_D r_0. \tag{DB3}$$
在从原节点帧于 $\mathcal O$ 上固定、再同时约化的边界复形
$[\mathcal O\xrightarrow{1-s^m}\mathcal O]$ 的坐标中，
$\beta_D$ 准确为乘 $-\bar m$。因此
$$\ker\beta_L=k\langle1\rangle,\qquad \beta_L(J)\ne0. \tag{DB4}$$
这就是 TH Step 1 使用的实际 $\beta_{L_m}$，不是一个新定义的替代类。

**DB.3（同一完整纤维消费者）。** 对原每条完整光滑有限几何能级 $X=(J=h)$，
在允许的完美剩余域扩张后，以原 $1$ 平凡化 $L_m|_X$，有实际限制同构
$$\rho_X:H^1(S_k,L_{m,k})\xrightarrow{\sim}H^1(X,\mathcal O_X),$$
且局部正则提升 $j_i$ 给
$$\rho_X\beta_L(J)=\left[\overline{(j_j-j_i)/\pi}\big|_X\right]
=\kappa_J\ne0. \tag{DB5}$$
该等式适用于完整 $X$，不只对泛点或环面开集。

## Status

**PROVABLE AS STATED（新的作者复用证明，待非作者检查）。**
所替换的只是 TH Step 1 对 U2A 的使用，以及 Step 2 的同一常数消失供应。
TH 的原迹 $p\pi$ 同余、OC A1–A4、完整两方向理想及高层证明不由本件代签。
本件不证明或否定通用底环上的全部次数导出分裂，不修改已接受 Ucoh/Ssplit。

## Assumptions、依赖与策略

只消费以下旧证明的实际模型及局部公式，不消费其后部通用分裂出口：

1. [原模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)
   §1、Steps 1–2 的八截面、相对光滑、反典范八环及原截面身份。
2. [Nbd](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)
   的实际节点单位帧与传播比，及 [Ucoh](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)
   Steps 1–2 的整基环图计算。下文重述所需常数／节点计算，而不以 U2A 倒推。
3. [P](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)
   的原小阶 $J$ 非常数、极除子为 $mD_k$；
   [Gfield](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md)
   的原完整 pencil，供 DB.3 固定原有限纤维。

策略是先在 $A_2$ 和 $k$ 上直接计算边界，再用相同层序列的 Bockstein 自然性。
不把通常 $H^0$ 的非平坦基变换误作同构，不需要选择全 $L_m$ 的派生直和分裂。

## Proof

### Step 1. 实际常数上同调及基变换身份

每次截面吹起在中心附近有两个相对参数，局部是 $\mathbb A^2_A$ 零截面的吹起。
它是 $\mathbb P^1_A$ 上 $\mathcal O(-1)$ 的总空间；向 $\mathbb P^1_A$ 的 affine 投影
将结构层推到 $\bigoplus_{d\ge0}\mathcal O(d)$。
两张标准 affine 图的 Čech 复形给每个 $\mathcal O(d)$ 的高次上同调为零，
并与此直和交换；次数零部分为 $A[u,v]$。
故该吹起满足 $b_*\mathcal O=\mathcal O$、$R^i b_*\mathcal O=0$（$i>0$）。
坐标变换、局部化及中心外的同构将等式用于每个实际中心。
这些实际图在 $A_2,k$ 上仍为同样图式；没有假定任意非平坦吹起自动基变换可交换。

八次使用 Leray，再对 $\mathbb P^1_A\times\mathbb P^1_A$ 用标准四图，得到
$$H^0(S_A,\mathcal O)=A,\qquad H^i(S_A,\mathcal O)=0\quad(i>0). \tag{1}$$
同一坐标常数给这里的 $A$；这一身份与 $A_2\to k$ 及乘 $\pi$ 相容。

### Step 2. 从实际节点帧固定可同时约化的边界复形

$D_A$ 是八个 $\mathbb P^1_A$ 的节点环，$\mathscr N_A$ 在各分量平凡。
这是原 Nbd 单位帧的整系数公式；四个非平凡传播比为
$-1/t,-1,-1/s,-t$，其乘积是 $s^{-1}$。
相同公式在 $A_2,k$ 仍为单位，不从域上线丛分类推断此结论。

对节点 $A[u,v]/(uv)$，分支差值序列
$$0\longrightarrow A[u,v]/(uv)\longrightarrow A[u]\oplus A[v]
\xrightarrow{(f,g)\mapsto f(0)-g(0)}A\longrightarrow0$$
在任意上述 $A$ 上逐项正合。张量可逆层并沿八环取 Čech，
各分量无高次上同调，故 $R\Gamma(D_A,\mathscr N_A^j)$ 由 $[A^8\to A^8]$ 计算。
沿原单位帧消去前七个可逆对，余下箭头为 $1-s^{-j}$。
在 $\mathcal O$ 上将次数一坐标乘单位 $-s^j$，固定得到
$$K_{j,A}=[A\xrightarrow{1-s_A^j}A],\qquad\text{次数为 }0,1. \tag{2}$$
先固定这些消元和单位缩放、再取 $A_2,k$，所以 (2) 与乘 $\pi$、约化及相应连接同态相容。
本步骤只对边界固定模型，没有断言整张曲面的通用导出分裂。

### Step 3. 非共振低层与首个共振层

若 $1\le j<m$，则 $\eta^j\ne1$，所以 $1-s^j$ 在 $A_2$ 及 $k$ 中都为单位。
由 (2)，$H^i(D_A,\mathscr N_A^j)=0$ 对所有 $i$ 成立。
对原有效 Cartier 除子序列
$$0\longrightarrow L_{j-1,A}\longrightarrow L_{j,A}
\longrightarrow\mathscr N_A^j\longrightarrow0 \tag{3}$$
取长正合列，并由 (1) 归纳，即得 DB1，且各次数零同构保持实际常数。
当 $m=1$ 时该归纳区间为空，DB1 直接由 (1) 给出。

在 $k$ 上 $1-\eta^m=0$，故 (2) 给
$H^0(D_k,\mathscr N_k^m)=H^1(D_k,\mathscr N_k^m)=k$，高次为零。
将 DB1 的 $n=m-1$ 代入 (3) 的 $j=m$ 长正合列，准确得到 DB2。
特别原 $H^0(S_k,L_{m,k})$ 为二维，$r_0$ 的核正是真实常数。
原 $J$ 由 P 是这个空间中的非常数截面，故 $r_0(J)\ne0$。
此处不把 $J$ 预设为 (2) 的某个单位生成元；只使用实际限制和非核性质。

### Step 4. 实际层连接的自然性和准确斜率

$S/\mathcal O$、$D/\mathcal O$ 平坦，$L_m$ 和 $\mathscr N^m$ 可逆。
因此底环 $0\to k\xrightarrow{\pi}A_2\to k\to0$ 分别产生两个准确层短正合列。
原限制 $L_m\to i_*\mathscr N^m$（$i:D\hookrightarrow S$）给它们之间的交换图。
取上同调连接的自然性，就得 DB3；这里的限制是同一模型的实际态射。

在 (2) 的固定边界复形中，$\widetilde\eta^m=1$ 给
$$1-s^m=1-(1+\pi)^m\equiv-m\pi\pmod{\pi^2}. \tag{4}$$
以 $1$ 提升剩余次数零生成元，求微分后除 $\pi$，再约化，所得是 $-\bar m$。
这逐复形计算的是实际 $\beta_D$，因为 Step 2 已固定与系数短正合列相容的消元。
由 $p\nmid m$，$\beta_D$ 是同构。结合 $r_1$ 是同构及 $\ker r_0=k\langle1\rangle$，
便有 DB4；若 $r_0(J)=b_J$，其边界像准确为 $-\bar m b_J$，不把 $b_J$ 人工归一为一。

所有计算在 $A_2$ 中实施。当 $p=2$，$\pi=-2$、$A_2$ 通常特征四，
上述系数短正合列和 (4) 仍成立；没有将它误换为特征二双数环。
当 $m=1$，(4) 的斜率仍为 $-1$，无需额外例外。

### Step 5. 原完整纤维上的同一个 Čech 类

在允许的剩余域扩张上固定 $h$。原完整有限纤维 $X=(J=h)$ 与 $D_k$ 不相交，
对应于 $L_{m,k}$ 的有效 Cartier 截面 $J-h\cdot1$。
原 $1$ 在 $X$ 上处处非零，准确给 $L_{m,k}|_X\simeq\mathcal O_X$。
由
$$0\longrightarrow\mathcal O_{S_k}\xrightarrow{J-h\cdot1}L_{m,k}
\longrightarrow L_{m,k}|_X\longrightarrow0$$
及 (1) 的 $H^1,H^2$ 消失，得到实际 $\rho_X$ 同构。
这对每个所选完整 $X$ 成立，不由仅泛纤维维数推断。

在覆盖 $X$ 的原模型开集用 $1$ 平凡化 $L_m$，将 $J$ 的局部截面提升写成正则函数 $j_i$。
按 TH 的 Čech 约定 $c_j-c_i$，$\beta_L(J)$ 的局部代表是
$\overline{(j_j-j_i)/\pi}$；限制及上述指定平凡化就给 DB5。
改变提升只加余边界；这里的 $\beta_L$ 与旧 U2A 算出的层 Bockstein 是同一个实际连接，
所以更换计算证明没有更换 $\kappa_J$，也没有改变后续 OC 的符号或目标 $H^1(\mathcal O_X^p)$。
由 DB4 及 $\rho_X$ 单射性，$\kappa_J\ne0$。证毕。

## 替换边界、Corrections 与 Open Risks

- 若本件获非作者核准，TH Step 1 可改接 DB1–DB4，Step 2 的 $n=0$ 供应改接 (1)；
  TH Steps 2–5 的其余部分、prime trace、OC、实际 Jacobian／闭 Hasse、TB/P2/PI 均保持。
- Ucoh Steps 1–2 的实际常数与节点计算仍保留；其通用截面 Ssplit、全部扩张分裂和 U2A
  不再由这个特定 Bockstein 消费者调用。若其他消费者另用它们，仍须分别保留，不作整包删除。
- 本件不是 U2A 全量词的替代，不给任意高度、所有 $n$ 的上同调分裂或自然新一般理论。
  它证明同一个首层连接，不提高 V1–V3 的新意分数，也不授正文容量。
- 当前作者结论待非作者检查，尤其需核原节点帧的整基环身份、Bockstein 交换图、
  特征四、$m=1$ 和与原 $J$ 的非核识别。没有凭“只用一个特例”直接删除旧证明。
- skill proof-writer 的实际影响是固定准确替换出口、给出完整自然性证明并保留未审状态。
  旧冻结文件、查新7.2及全部正式失败不改；没有项目、稿件、锁、试排或外部效力。
