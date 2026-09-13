# Paper30 qPI：通用整系数上同调 U 的非作者数学核查 V1

日期：2026-09-09。核查者：`/root/p30_qpi_universal_cohomology_check_v1`。
类型：限定 U 新增命题及其消费接口的 fresh 非作者证明核查；不是 S 的独审、正式候选评价、来源查新或论文产物验收。

## Claim

唯一待核作者输入为 [U 诊断 V1](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)，全文 255 行，SHA-256：

`a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b`。

置 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$。$S/R$ 严格使用 G 的八截面吹起，参数对应为 $s=q,t=\tau$；$D$ 为指定八环，$L_n=\mathcal O_S(nD)$，$\mathscr N=\mathcal O_D(D)$。本核查保留以下原量词与结论：

1. 对每个整数 $n\geq0$，有
   $$
   H^0(S,L_n)=R\langle1\rangle,\qquad
   H^1(S,L_n)\simeq\bigoplus_{j=1}^nR/(1-q^j),\qquad
   H^{\geq2}(S,L_n)=0.
   $$
   边界递增所得每一级短正合列分裂，不宣称该分裂典范。
2. 对每个固定 $n$，存在保留真实常数映射的同构
   $$
   R\Gamma(S,L_n)\simeq P_n:=R[0]\oplus
   \bigoplus_{j=1}^n[R\xrightarrow{1-q^j}R],
   $$
   各两项复形的次数为 $0,1$。
3. 固定一次上述选择后，对每个交换 $R$-代数 $A$，有关于 $A$ 自然的导出基变换同构及上同调公式
   $$
   R\Gamma(S_A,L_{n,A})\simeq P_n\otimes_R A,
   $$
   $$
   H^0(S_A,L_{n,A})\simeq A\oplus\bigoplus_{j=1}^n\operatorname{Ann}_A(1-q_A^j),
   \qquad H^1(S_A,L_{n,A})\simeq\bigoplus_{j=1}^nA/(1-q_A^j),
   $$
   且高次上同调为零。第一式的 $A$ 是实际常数子模。$A$ 无需平坦、约化或 Noetherian。
4. 原通用有限呈示模的零阶 Fitting 理想为
   $$
   \operatorname{Fitt}_0H^1(S,L_n)
   =\left(\prod_{j=1}^n(1-q^j)\right)
   =\left(\prod_{d=1}^n\Phi_d(q)^{\lfloor n/d\rfloor}\right).
   $$

以下以作者公式编号 U1、U2、U2A、U3、U4 识别这些结论；作者小节标题与公式编号的不同不改变核查对象。

## Status

**PROVABLE AS STATED，相对于 U 明示消费的 S5/S7 截面引理。U 的新增证明步骤及消费接口：数学 PASS。**

未发现需要削弱 $n$ 或 $A$ 的量词、增加局部性或特征排除的数学缺口。这里的结论有一个必须显式保留的接受依赖：同 SHA 的 [S 作者件](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md)中的 S5/S7，须由本轮另一个非作者报告独立确认。本报告全文读取 S 以核对接口，但不代签该报告，也不把作者自评或交流消息当作其接受。

因此本件提交时的依赖状态为 **PENDING_CONJUNCTION_WITH_S5_S7_REVIEW**。主控只有读取同输入的实际 S 独审报告并确认 S5/S7 有效后，才可把这项依赖式 PASS 合取为 U 的完整数学接受。这不是对原数学命题添加新假设，而是划清本次独立审查的所有权。

| 新增义务 | 本次结论 | 检查到的关键条件 |
|---|---|---|
| 通用模型与 $R\Gamma(\mathcal O_S)$ | PASS | 实际相对坐标吹起；局部推前由两图计算，不用纤维维数猜测 |
| 节点复形与未分裂过滤 | PASS | 真实单位帧；整环上 $1-q^j$ 非零；逐级长正合列 |
| S5/S7 的 U 消费接口 | PASS，保留独审依赖 | $B_j$ 就是 S 的根单位基环；完整模型及迹系数完全相同 |
| 原非局部 $R$ 上 Bockstein 分裂 | PASS | 自然性给单位商像；只在 $B_j$ 内取逆 |
| 派生分裂与常数项 | PASS | $\operatorname{Ext}^2_R(T_n,R)=0$；保留原常数映射的分裂三角 |
| 全部 $A$ 的自然基变换 | PASS | 原基 Noetherian、proper、层对基平坦；同一复形逐项张量 |
| Fitting 乘积 | PASS | 指定模的对角有限呈示；$n=0$ 空积约定 |

## Assumptions

- $q,\tau$ 为单位；不涉及非单位参数的模型。$R$ 中未施加根单位关系。
- 中心按 G 的 $1+2+3+2$ 次截面吹起定义。先做四次节点吹起的等价描述中，最后四个中心在不同分量的坐标为 $1,\tau,\tau,q$。相同坐标值不表示同一中心。
- 消费已接受域上 T1 与原矩阵迹、行列式恒等式作为 S5/S7 的上游输入；本次不重审旧 T1 或其余旧接受件。
- N 的节点帧以其显式坐标公式相对化，不把域上多重次数为零的线丛分类直接套到任意基环。
- S5/S7 的准确内容是：对每个 $j\geq1$，原迹系数 $C_j$ 在整个 $B_j$ 模型上为 $L_j$ 截面，且其限制在整个 $D_{B_j}$ 上生成 $\mathscr N^j_{B_j}$。不能用仅泛纤维正则或仅几何点非零的弱版本替代。

## Notation

$$
a_j=1-q^j,\qquad B_j=R/(a_j),\qquad
T_j=H^1(S,L_j),\qquad T_0=0.
$$

$E$ 为完整环面补集，含 $D$ 与四条末端例外曲线；它不同于 $D$。原乘积次序与系数定义为

$$
C_j=[z^j]\operatorname{tr}\bigl(A(q^{j-1}z)\cdots A(qz)A(z)\bigr)
\in B_j[x^{\pm1},y^{\pm1}].
$$

使用上同调移位约定 $H^i(M[k])=H^{i+k}(M)$；故模 $M[-1]$ 仅在次数 $1$ 有上同调。支持于闭子概形的层，在曲面上取上同调时隐含其闭浸入推前。

## Proof Strategy

直接在无关系 $R$ 上计算常数层与节点环，先得到未分裂的扩张；只以 S5/S7 提供的真实模 $a_j$ 截面构造 Bockstein 分裂。随后检查派生扩张障碍及固定选择后的自然基变换，不由圆分 DVR 长度、域上维数或任意非平坦普通基变换反推通用结论。

## Dependency Map

1. G 的显式坐标、N 的帧公式 $\Rightarrow$ 通用模型与节点两项复形。
2. 局部吹起推前 $\Rightarrow R\Gamma(S,\mathcal O_S)=R[0]$；再由边界序列得到 $T_j$ 的扩张。
3. S5/S7 $\Rightarrow$ 单位边界截面；Bockstein 自然性 $\Rightarrow$ 扩张逐级分裂，即 U1。
4. U1 与每个 $B_j$ 的长度一自由分解 $\Rightarrow$ 二阶 Ext 消失；常数三角分裂给 U2。
5. 固定 U2 的选择后导出基变换给 U2A、U3；U1 的对角呈示给 U4。

## Proof

### Step 1. 模型与局部吹起的常数推前

所有中心在实际仿射图内由两个相对坐标 $(u,v)$ 的零截面定义；平移最后中心只使用 $q,\tau$ 及其逆。零截面吹起的两图为

$$\operatorname{Spec}R[u,w],\quad v=uw;
\qquad\operatorname{Spec}R[z,v],\quad u=zv.$$

这些图及交叠公式在任意 $R$-代数下保持同样的表达式。因此这里的相对吹起模型确实与所需任意基变换相容；没有援引一般吹起对任意非平坦基变换自动交换的错误命题。中心外为同构，八次操作给 $S/R$ 光滑射影。

最后四个中心在不同分量上且坐标为单位，所以不遇节点。节点局部边界为 $uv=0$，边界光滑点为 $u=0$；吹起后的严格变换及需要保留的例外由上述两图直接计算。由此得到 $D$ 的八环，以及完整 $E$ 的相对 SNC Cartier 结构。局部环 $R[u,v]/(u)$ 和 $R[u,v]/(uv)$ 具有相应单项式 $R$-基，所以 $D,E$ 对 $R$ 平坦，基变换后也平坦。

再核查结构层推前。设 $b:Y\to\mathbb A^2_R$ 为零截面吹起。它是 $\mathbb P^1_R$ 上 $\mathcal O(-1)$ 的总空间；相应仿射投影 $p$ 满足

$$p_*\mathcal O_Y=\bigoplus_{k\geq0}\mathcal O_{\mathbb P^1_R}(k).$$

标准两仿射图的 Čech 商对每个 $k\geq0$ 均无正次上同调，次数零为齐次 $k$ 次二元多项式。有限覆盖的 Čech 复形与直和交换，故

$$H^0(Y,\mathcal O_Y)=R[u,v],\qquad H^{>0}(Y,\mathcal O_Y)=0.$$

这不仅是全空间上的消失：对目标任一主仿射开集，上述两图 Čech 复形按其定义方程局部化；局部化正合，仍给对应结构环及正次消失。因此 $Rb_*\mathcal O_Y=\mathcal O_{\mathbb A^2_R}$。实际中心附近正是该模型的坐标变换及局部化，中心外为同构，所以每次实际吹起都有同一推前等式。

八次 Leray 复合不改变结构层的导出全局截面。$\mathbb P^1_R\times_R\mathbb P^1_R$ 的标准四图计算给结构层上同调只有常数 $R$，于是

$$R\Gamma(S,\mathcal O_S)=R[0]. \tag{C1}$$

这一步未使用任何局部基环假设、闭纤维计数或 Nakayama 引理。

### Step 2. 真实相对节点复形与边界过滤

N 的四个零次分量使用单项式帧；其余四个分量的线丛是实际 $\mathcal O(1)$ 减去指定单位坐标截面。局部一次因子在减点后的线丛中成为处处生成的截面，其两个端点系数均为单位。因此得到各分量上真实的平凡化，不仅是纤维上的次数判断。

按 N 的有向环，四个非平凡传播比为

$$-1/\tau,\quad-1,\quad-1/q,\quad-\tau,$$

其余四个为 $1$，乘积为 $q^{-1}$。张量 $j$ 次后乘积为 $q^{-j}$。

对节点的环，差值映射给准确序列

$$0\to R[u,v]/(uv)\to R[u]\oplus R[v]\to R\to0,$$

最后映射取两分支在零点的值之差。张量可逆层后仍正合。所有八个分量是 $\mathbb P^1_R$，其平凡线丛仅有常数上同调，因此

$$R\Gamma(D,\mathscr N^j)\simeq[R^8\to R^8].$$

利用单位粘合逐节点消去七个可逆对，余下

$$[R\xrightarrow{1-q^{-j}}R],\qquad1-q^{-j}=-q^{-j}a_j. \tag{C2}$$

$R$ 为整环且 $q$ 未满足根单位关系，所以每个 $j\geq1$ 的 $a_j$ 都是非零因子。故 (C2) 的零次上同调为零，一次上同调为 $B_j$，更高次为零。

因为 $D$ 是有效 Cartier 除子，有

$$0\to L_{j-1}\to L_j\to\mathscr N^j\to0.$$

从 (C1) 开始归纳：零次节点群为零使常数群每级不变；前级及节点的高次消失使本级高次消失；一次段准确给

$$0\to T_{j-1}\to T_j\xrightarrow{\rho_j}B_j\to0. \tag{C3}$$

此时尚未断言 (C3) 分裂。特别地，不需要在非局部 $R$ 上由一次模极大理想消失推出全局模消失。

### Step 3. S5/S7 消费接口的范围检查

S 的通用根单位环为 $\mathbb Z[q^{\pm1},\tau^{\pm1}]/(q^j-1)$，与 $B_j$ 完全相同，因为两个关系只差符号。S 的相对模型与 $S_{B_j}$ 的每步中心、图及边界均一致；Step 1 的显式图已核对任意基变换接口。原矩阵、乘积顺序及取 $[z^j]$ 的定义也一致。

因此 S5/S7 的准确输入就是

$$C_j\in H^0(S_{B_j},L_{j,B_j}),\qquad
C_j|_{D_{B_j}}\text{ 生成 }\mathscr N^j_{B_j}. \tag{C4}$$

U 没有使用 S 的 DVR 模分裂结论反推 (C4)。其 Step 3 的摘要保留了四项必要义务：所有 $d\mid j$ 的特征零分支、完整 $E$ 而非仅 $D$、允许极点商的基环平坦性、实际边界单位系数。其边界系数 $(-\tau)^jq^{j(j-1)/2}$ 与 S 的原矩阵计算相同，且是 $B_j$ 的单位。

尤其 U 没有把非本原分支上的 $C_j$ 换成 $\operatorname{tr}M_j(1)-(\tau^j+1)$，没有将仅泛纤维正则提升成整性，也没有声称普通 $H^0$ 对非平坦基变换可交换。其消费范围与 S5/S7 一致。

(C4) 的独立数学证明由另一个 fresh S 核查负责；本报告的以下证明精确以 (C4) 为输入，不把本段接口检查计为那份独审的替代。

### Step 4. 非局部通用环上的 Bockstein 分裂

$L_j$ 与 $\mathscr N^j$ 对 $R$ 平坦，$a_j$ 为非零因子，故分别有乘 $a_j$ 的短正合列，右端为对应模 $a_j$ 的层。限制映射 $L_j\to\mathscr N^j$ 与乘法交换，因而组成这两个短正合列之间的映射。

记连接同态为 $\beta_S,\beta_D$。由 (C2)，$H^0(D,\mathscr N^j)=0$ 且 $a_jH^1(D,\mathscr N^j)=0$，故长正合列给同构

$$\beta_D:H^0(D_{B_j},\mathscr N^j_{B_j})\xrightarrow{\sim}B_j.$$

在 (C2) 的两项模型中，对模 $a_j$ 的元素选择任意提升再除以 $a_j$ 计算微分，得到乘子 $-q^{-j}$。这在 $B_j$ 中为单位，改变连接同态符号也不影响生成元结论。

令

$$v_j=\beta_S(C_j)\in T_j.$$

曲面长正合列给 $a_jv_j=0$；连接同态的自然性给

$$\rho_j(v_j)=\beta_D(C_j|_{D_{B_j}})=:b_j\in B_j^\times. \tag{C5}$$

其中单位性用到了 (C4)，不是只用一个非零泛纤维限制。子模 $T_j[a_j]$ 本来就是 $B_j$-模，故定义

$$\sigma_j:B_j\to T_j,\qquad \overline c\longmapsto\overline c\,b_j^{-1}v_j.$$

该映射是 $R$-线性且良定义的。若改用 $R$ 中的代表计算，任意两个代表相差 $a_j$ 的倍数，作用于 $v_j$ 的差为零。完全不需要 $b_j^{-1}$ 在 $R$ 中有单位提升。(C5) 给 $\rho_j\sigma_j=\operatorname{id}$，从而 (C3) 分裂。

逐级采用这些分裂得到

$$T_n\simeq\bigoplus_{j=1}^nB_j.$$

它们确实分裂原边界短正合列，而非仅给出一个忽略过滤的抽象同构。结合 Step 2 的常数群与高次消失，U1 成立。

### Step 5. 二阶 Ext、移位与真实常数三角

置 $C=R\Gamma(S,L_n)$。U1 说明它仅在次数 $0,1$ 有上同调。常数截面给映射 $i:R[0]\to C$，其零次上同调为恒等识别，故其锥仅在次数 $1$ 有上同调 $T_n$。因此有三角

$$R[0]\xrightarrow{i}C\to T_n[-1]\xrightarrow{\delta}R[1]. \tag{C6}$$

对每个 $B_j$，非零因子 $a_j$ 给长度一自由分解

$$0\to R\xrightarrow{a_j}R\to B_j\to0.$$

因 $n$ 有限，U1 的直和给 $T_n$ 的长度一有限自由分解，故

$$\operatorname{Hom}_{D(R)}(T_n[-1],R[1])
=\operatorname{Ext}^2_R(T_n,R)=0.$$

所以 $\delta=0$，(C6) 是分裂三角。可选择 $C\simeq R[0]\oplus T_n[-1]$ 使 $i$ 成为第一直和项的包含；并非先任取一个可能混淆常数项的上同调分解。

复形 $K_j=[R\xrightarrow{a_j}R]$ 的次数是 $0,1$，它的唯一上同调为次数 $1$ 的 $B_j$，故 $K_j\simeq B_j[-1]$。代回得到 U2。这里的障碍确为二阶 Ext，而不是一阶 Ext，也不需要假设 $R$ 是 PID 或 hereditary 环。

### Step 6. 真正任意基变换与选择后的自然性

$R$ Noetherian，$S/R$ 射影因而 proper，$L_n$ 为相干可逆层且对 $R$ 平坦。[Stacks Lemma 30.22.1（精确 tag 07VK，所在节 07VJ）](https://stacks.math.columbia.edu/tag/07VK)的假设全部满足；该命题同时给 perfectness 与对任意目标环的导出基变换，不要求目标环 Noetherian、约化或平坦。本轮实读命题及完整证明。

固定 Step 5 的一个同构后，对所有 $A$ 使用同一个 $P_n$，不在每个 $A$ 上重新选择分裂。由于 $P_n$ 为有限自由复形，$P_n\otimes_R^{\mathbf L}A=P_n\otimes_R A$，由自然的基变换映射得到 U2A。

还可在本模型上明确核查所需自然性。选 $S$ 的有限仿射覆盖；分离性使有限交仍仿射。其有界交替 Čech 复形 $Q^\bullet$ 的各项对 $R$ 平坦，因为交集的坐标环对 $R$ 平坦且可逆层对应有限投射模。对任意 $A$，同一覆盖的基变换仍为仿射覆盖，$Q^\bullet\otimes_R A$ 就是 $L_{n,A}$ 的相应 Čech 复形。

$P_n$ 有界投射，故固定的派生同构可由链映射 $P_n\to Q^\bullet$ 表示，并可令第一 $R[0]$ 上的链映射就是常数截面。该映射的锥为有界无上同调的平坦复形；从最高次数向下归纳，其各短正合列的商与核均平坦，故张量任意 $A$ 后仍无上同调。于是同一个链映射张量后对每个 $A$ 都是拟同构。这也直接保证对环同态 $A\to A'$ 的自然性及常数映射的保持。

逐项取核与余核给

$$H^0([A\xrightarrow{a_{j,A}}A])=\operatorname{Ann}_A(a_{j,A}),
\qquad H^1([A\xrightarrow{a_{j,A}}A])=A/(a_{j,A}).$$

故 U3 包含完整 annihilator 项；在 $a_{j,A}=0$ 时该项是 $A$，在 $a_{j,A}$ 为单位时两项上同调均为零，零因子情形由实际核处理。没有把非零因子的通用假设错误地沿非平坦基变换保留。第一直和项仍是实际常数截面，所以普通 $H^0(S,L_n)\otimes_R A\to H^0(S_A,L_{n,A})$ 只对应这个常数子模，未被宣称总是同构。

### Step 7. 对角呈示、Fitting 理想与边界值

U1 给 $T_n$ 的有限呈示

$$R^n\xrightarrow{\operatorname{diag}(a_1,\ldots,a_n)}R^n\to T_n\to0.$$

零阶 Fitting 理想由此方阵的最大阶子式即行列式生成，所以

$$\operatorname{Fitt}_0T_n=\left(\prod_{j=1}^na_j\right).$$

利用整数多项式恒等式 $q^j-1=\prod_{d\mid j}\Phi_d(q)$，对每个 $d\leq n$ 统计其在 $j=1,\ldots,n$ 中出现 $\lfloor n/d\rfloor$ 次，得到 U4；总符号为单位，不影响理想。

$n=0$ 时 Step 1 给 $R[0]$，$T_0=0$，其零阶 Fitting 理想为单位理想，所有空和及空积公式一致。$n=1$ 无需特殊例外。任意 $A$ 的高次消失由两项复形给出，不需要在该基环上再做相干性或 Nakayama 论证。

作者所列圆分 DVR 专门化也符合公式：当 $n=r$ 且 $q=s$ 精确阶为 $r$ 时，第 $r$ 个微分为零，因此 $H^1$ 多出一个自由 $\mathcal O$ 项；当 $n=r-1$ 时，Fitting 乘积专门化为 $\prod_{j=1}^{r-1}(1-s^j)=r$。这些是已证通用复形的推论，不是本证明的输入。S15 的 elementary divisors 仍属 S 独审范围，本件不另行核发其接受。$\square$

## Corrections or Missing Assumptions

没有要求修改 U 作者件的数学错误，也未增加原命题外的科学假设。作者链接的 07VJ 是包含所引引理及证明的节，精确引理 tag 为 07VK；这是来源定位细化，不是引用失效。

后续消费者必须保留：完整 $E$ 与 $D$ 的区别、S5/S7 的整模型单位截面、商环内取逆、真实常数三角、固定一次派生分裂后再统一基变换。上述每项均与 U 原证明相容。

## Open Risks

- 本件的唯一待合取接受依赖是同哈希 S5/S7 的实际 fresh 非作者报告。即使有人已交流“未发现缺口”，本件也不据此提前代签。若该报告发现失效，本件对 U 的合取接受必须继续保持未闭合。
- 不声称不同 $n$ 的派生同构自动兼容，不声称保留截面环乘法、cup product、动力作用、相对对偶或与整除微分对象的典范识别。
- 不涉及非单位 $q,\tau$、稳定或半稳定约化、任意跳跃概形的定义。U4 仅为准确指定模的 Fitting 理想。
- 本核查不评价新意、论文容量、Route 或正式四门；没有数值抽样、CAS 实验或 PDF 验收。标准工具数量不计为独立新方法。

## 实际读取、输入身份与唯一输出

| 文件 | 本轮实际读取范围 | SHA-256 |
|---|---|---|
| [U 作者件](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 全文 1–255 行；定向回读 100–255 行 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| [S 作者件](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 全文 1–418 行；消费 S5/S7 接口，不替代其另行独审 | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` |
| [G 作者件](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 全文 1–254 行；使用实际中心与相对坐标 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [G 独立核查](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | 全文 1–286 行；接受范围与模型消费边界 | `ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b` |
| [N 帧文件](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 定向 68–247 行；实际中心、节点帧、$x=0$ 帧及四个传播比 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |

另全文亲读工作区 `AGENTS.md`、`docs/WORKFLOW.md` 与 proof-writer 技能；定向阅读批次接续首部 1–28 行。外部仅实读 Stacks 07VJ 的本节及 07VK 的引理命题、完整证明，用于核对基变换条件；未开展一般文献查新。

proof-writer 使本件分开准确命题、输入引理、逐项证明与未合取接受风险；未扩大为重审旧包。唯一新增文件是本核查报告，使用 `apply_patch` 写入并于交付前全文回读及计算 SHA-256。未修改 U、S、G、N、入口、冻结材料、旧接受件、票、锁或任何论文产物。
