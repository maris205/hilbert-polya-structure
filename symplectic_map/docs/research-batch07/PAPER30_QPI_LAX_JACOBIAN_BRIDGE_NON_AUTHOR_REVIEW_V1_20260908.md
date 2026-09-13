# Paper30 qPI Lax–Jacobian 桥：全新非作者数学核查 V1

日期：2026-09-08。
审查者：独立 Codex 代理 `/root/p30_qpi_jacobian_non_author_check`。
审查方式：按 research-review 技能，以已配置的 xhigh 独立 Codex fallback 核查；没有冒称调用指定 GPT-5.4 MCP。
文件所有权：仅本报告；未修改作者稿、S/G 输入、任何其他作者包、锁、项目、稿件或 PDF。

## 结论

**PASS：指定作者稿的实际泛纤维 Jacobian／torsor Claim 成立。**

在所提供且哈希一致的 S/G 已接受输入合同下，新 Steps 1–7 补齐了本 Claim 所需的数学链条。
结论是原参数上的 $K$-同构 $\operatorname{Jac}(X)\simeq E$ 和 $X$ 的 $E$-torsor 结构，
不是同亏格推断、未知次数同源，也不是只在几何点集合上建立的泛单射。
没有发现必须新增假设、排除特征 $2,3$、删去特殊非零 $t$，或进一步限制 $r$ 的硬缺口。
本报告没有 CONDITIONAL 或 FAIL 的实际 Claim 项；下文两处可选说明均不构成通过条件。

通过严格限于 $K=k(c)$、$c$ 超越的真实泛纤维；不顺带接受全部有限坏纤维分类、
具体回返平移点、torsor 总能平凡化或 JR 全部有限域轨道猜想。
这是数学入口审查，不是 Route 评价，不含正式新意、价值、稿件页数或 PDF 评分。

## 1. 输入、独立性与定位约定

完整逐行读取的唯一新作者稿为
[Jacobian 桥入口](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md)，共 492 行，SHA256：

`a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f`。

下文“作者 Lx–Ly”均指该冻结稿的行号，不指本报告。
作者稿中的 `PROVABLE AS STATED` 没有作为独立通过证据。
未读取本轮其他作者包、其他审查或接受处置投票；S/G 的已接受状态由任务提供。

外部合同仅为：

| 输入 | 实际采用的合同 | 核对的 SHA256 |
|---|---|---|
| [S 谱商入口](PAPER30_QPI_SPECTRAL_QUOTIENT_ENTRY_V1_20260908.md) | 原二次谱方程、全特征仿射循环商、非二特征光滑参数条件及其模型；局部读取 Claim、记号与不变量环公式 | `049941aad912cabc3788d8063ba3cec20d3f7a863a2ef50e3d29e1747d3e3738` |
| [G 原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 每个非零固定 $t$、所有允许特征下，实际 $I_r=c$ 的几何泛纤维光滑、几何整、射影且亏格一，以及原 Laurent 方程身份；仅采用其 Claim 合同 | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |

这两项基础结果没有重审；G 的代数闭底域结论在此经域扩张与忠实平坦下降用于任意 $k$。
没有借用坏纤维包或尚未证明的动力回返结果来闭合本桥。

## 2. 实际 Claim 矩阵

| 项目 | 作者定位 | 判定 | 决定性理由 |
|---|---|---|---|
| 原 $A,M,I_r$ 及参数规范相符 | L121–169，式 (5)–(9) | PASS | 与 JR 原公式一致；最高系数、零次项和循环顺序均一致 |
| 所有允许特征的 $C,E$ 光滑射影几何整模型及亏格 | L172–234 | PASS | 非二特征使用 S；特征二直接求偏导；双覆盖推下分裂给连通性与 Euler 特征 |
| $\mathcal L$ 为参数族上的线丛、$\deg L=n$、$\alpha$ 延伸 | L236–267 | PASS | 标量值将迫使固定谱曲线奇异；循环向量给谱代数自由秩一模；proper 延伸合法 |
| 谱线丛恢复常数共轭类及其族意义 | L269–288 | PASS | 推下评价同构恢复 $\lambda$ 乘法；有理点刚化消除通用线丛障碍 |
| 从 $M_n,M_{n-1},M_0$ 恢复原 $x,y$，含不可分次数 | L290–334 | PASS | 两个无基系数不变量是 Picard 开集上的有理函数；拉回恰为 $x,y$ |
| $A:L\dashrightarrow\sigma^*L$ 方向与循环复合 | L336–352 | PASS | 目标的 $\lambda$ 矩阵是 $M(sz)$；intertwining 给该方向；循环积正为 $M$ |
| 固定除子 $3P_0-2Q_2-Q_1$ 与谱线丛差不变 | L354–384 | PASS | 四点局部参数给 $\operatorname{div}(\lambda)$；支集固定后可在整数除子群除以 $r$ |
| $\pi^*$ 为闭浸入，排除整个群概形核 | L388–403 | PASS | 范数把核置于 étale $r$-挠；全群固定点消除所有几何核点 |
| 不变 Picard 群的单位分支恰为 $\pi^*J_E$ | L405–423 | PASS | tame 平均使不变量上同调为 $H^1(E,\mathcal O_E)$；维数和切维均为一 |
| 完整陪集与 $\alpha$ 同构到像 | L425–436 | PASS | 几何连通像落入单位分支；proper 非恒定像充满椭圆曲线；函数域次数一 |
| $K$ 上 torsor 作用及 $\operatorname{Jac}(X)\simeq E$ | L438–453 | PASS | 张量作用与像均在 $K$ 上，几何同构忠实平坦下降；换基点只改变平移 |
| 每个非零 $t$、全部允许 $r$、特征 $2,3$ 与不假设 $K$ 点 | L9–18、L26–56、L455–469 | PASS | 分母仅使用已知非零量；没有要求 $2$ 或 $3$ 普遍可逆；基点只在几何层选择 |

## 3. 模型与特征二：独立复核

作者 L193–215 的新证明确实补足 S 未覆盖的特征二部分。
写 $H=Z^2+cZ+T$、$F=\lambda^2+H\lambda+Z^3$，在特征二有

$$F_\lambda=H,\qquad F_Z=c\lambda+Z^2.$$

若 $c=0$，$F_\lambda=0$ 给 $Z^2=T\ne0$，而 $F_Z=0$ 要求 $Z=0$，无解。
若 $c\ne0$，奇点必须满足 $Z\ne0$、$\lambda=Z^2/c$；在 $H=0$ 上

$$c^2F=Z^4+c^2Z^3=Z^3(Z+c^2).$$

所以 $Z=c^2$，再代入 $H=0$ 得 $c^4+c^3+T=0$，反向代入也成立。
在本任务的 $K=k(c)$ 中，该单首多项式非零；这里没有把 $c$ 超越误换成“一般 $t$”。

无穷远图的 $\mu$ 偏导在 $\mu=0,1$ 为 $-1,1$，特征二时仍是非零单位。
$z=0$ 的两个点同样由 $T\ne0$ 保证光滑。
$C$ 在 $z\ne0,\infty$ 上是 $E$ 沿 $z^r=Z$ 的 étale 基变换，因 $r$ 与特征互素；
这不是声称特征二的次数二谱投影是 tame。

式 (14) 的分裂来自基 $1,\lambda$ 与 $\mu=\lambda z^{-n}$ 的直接转移，所有特征有效。
基变换到代数闭包后 $H^0(\mathcal O_C)=H^0(\mathcal O_E)=\bar K$；
光滑曲线各不可约分量互不相交，因此连通性给几何整性。
由 $\chi(\mathcal O_C)=2-n$、$\chi(\mathcal O_E)=0$ 得 $g(C)=n-1$、$g(E)=1$。
四个端点是 $K$-有理的全群固定点；这是后面核证明实际使用的几何信息。

## 4. Step 2：线丛族不是只在单条几何纤维上存在

作者 L238–245 先构造的是固定谱代数在 $\mathcal O^{\oplus2}$ 上的作用。
其有限图由 $\lambda\mapsto M(z)$ 给出，无穷远图由 $\mu\mapsto v^nM(v^{-1})$ 给出，
Cayley–Hamilton 与转移关系使这确实是全局谱代数模。

若某几何参数、某有限 $z=a$ 有 $M(a)=bI$，则
$\operatorname{adj}(bI-M(a))=0$；行列式对 $z$ 和 $\lambda$ 的两个一阶偏导同时为零。
该点又在固定特征多项式上，故会产生谱曲线奇点，与 Step 1 矛盾。
无穷远值为 $P=\operatorname{diag}(1,0)$，无论特征如何均非标量。

在任一底点的剩余域上，非标量的二阶矩阵有循环向量 $e$。
将其提升到局部环后，$e,Me$ 的行列式为单位；映射

$$\mathcal O[\lambda]/(\chi_M)\longrightarrow\mathcal O^{\oplus2},\qquad f\longmapsto f(M)e$$

在该邻域是底模同构，且与谱代数作用相容，因而是谱代数模的自由秩一表示。
也可先在几何基变换后检查再用忠实平坦下降；两种解释都覆盖参数族，非仅点集。
由有限推下的 Euler 特征得 $\deg L=2+(n-1)-1=n$。
Picard 分支 proper 且 $X$ 光滑一维，故 L265–267 的逐 DVR 延伸没有缺口。

## 5. Steps 3–4：真正有理逆与不可分次数

谱线丛同构推下必须与 $\lambda$ 乘法相容。
推下均为 $\mathcal O_{\mathbb P^1}^{\oplus2}$ 时，其自同构是常数 $\operatorname{GL}_2$，
因此只丢失常数共轭规范，不丢失一个任意 $z$-有理 gauge。

作者 L280–286 的族机制足够，具体可在 Picard 开集 $W$ 上表述如下。
以 $P_0\in C(K)$ 刚化通用线丛 $\mathscr P$，取开条件
$H^0(C,L\otimes\tau^*\mathcal O(-1))=H^1(C,L\otimes\tau^*\mathcal O(-1))=0$。
该开集包含 $\alpha(U)$。令 $q:C\times W\to W$；在 $W$ 上，$V=q_*\mathscr P$ 是秩二向量丛，评价给
$\tau_*\mathscr P\simeq\operatorname{pr}_W^*V$，故乘以 $\lambda$ 恢复
$M_j\in\operatorname{End}(V)$，可在局部框架中读出系数。
有理点所给刚化与 Picard 通用线丛的标准关系，可参见
[Stacks：有理点刚化的 Picard 函子](https://stacks.math.columbia.edu/tag/0B9R)。

最高系数的特征关系是 $M_n^2-M_n=0$，特征多项式为 $u(u-1)$。
因此族上的 $P=M_n$ 给出秩一分解 $V=V_1\oplus V_0$；不需要开平方、分离扩域或选特征向量。
令

$$F=P M_{n-1}(1-P),\qquad G=P M_0(1-P).$$

它们属于同一个可逆层 $\operatorname{Hom}(V_0,V_1)$。
在包含 $\alpha(U)$ 的 $F\ne0$ 开集，$F$ 是两条线丛间的同构，故 $G/F$ 是普通正则标量函数。
另一个量 $h=\operatorname{tr}((1-P)M_0)$ 也不依赖框架。
于是作者式 (20) 等价于实际定义在 Picard 开集上的

$$\widehat x=-\frac{G/F}{t^{r-1}},\qquad
\widehat y=1+\frac{h}{t^{r-1}\widehat x}.$$

所用全 $r$ 系数计算正确：最高项相位是 $s^{r(r-1)}=1$；
对 $(M_{2r-1})_{12}$，唯一有贡献的 $A_1$ 位于最右侧，其余相位乘积仍为一；
零次项由 $A_0^2=tA_0$ 得 $M_0=t^{r-1}A_0$。
因此 $\alpha^*\widehat x=x$、$\alpha^*\widehat y=y$，而不是 $x^p,y^p$。

设 $Y$ 是 $\alpha$ 的概形闭像；它是整的，此处不预设它正规。恢复出的函数可限制到 $Y$ 的非空开集。
由于原坐标生成 $K(X)$，域嵌入 $K(Y)\hookrightarrow K(X)$ 的像含 $x,y$，故是满射。
这直接证明总函数域次数为一，包括不可分次数。
不需要证明所有固定特征多项式矩阵都来自原循环因子分解；该额外满射命题不是本 Claim 的消费者。

## 6. Step 5：方向、循环积与固定除子

在 $L$ 的模框架中，$\lambda$ 作用为 $M(z)$；在 $\sigma^*L$ 中为 $M(sz)$。
因此 $A$ 成为 $L\to\sigma^*L$ 的谱模同态所需的等式正是
$M(sz)A=A M(z)$。作者方向没有写反，也没有把列特征向量束与本谱模构造混用。

下一次拉回同态的矩阵是 $A(sz)$，故整个循环复合的矩阵为
$A(s^{r-1}z)\cdots A(z)=M(z)$，在谱模上等于乘以 $\lambda$。
这验证式 (23)；它不是单位同态，所以个别 $L$ 没有由此获得普通 $G$-线性化。

局部赋值独立核对为

$$\operatorname{ord}_{P_0}(\lambda)=3r,\quad
\operatorname{ord}_{P_T}(\lambda)=0,\quad
\operatorname{ord}_{Q_2}(\lambda)=-2r,\quad
\operatorname{ord}_{Q_1}(\lambda)=-r.$$

在 $z\ne0,\infty$ 上 $A$ 的逆由 $z^{-3}\operatorname{adj}(A)$ 给出，故没有其他零点或极点。
四个可能支点均被 $\sigma$ 固定；因而循环复合的除子是 $rD(a)$，不是仅总次数乘以 $r$。
整数除子群无挠，故可得

$$D(a)=3P_0-2Q_2-Q_1,\qquad
\sigma^*L\otimes L^{-1}\simeq\mathcal O_C(D(a)).$$

符号和线丛比值方向一致；除子与动力参数点无关。
这给出 Picard 态射上的恒等式，延伸到整个 $X$ 后，任意两条谱线丛之差落入
$B=\ker(\sigma^*-1)$。只对线丛差使用不变量群是正确且必要的处理。

## 7. Step 6：群概形核与单位分支

首先 $\operatorname{Nm}_\pi\pi^*=[r]$，故 $\ker\pi^*\subset J_E[r]$。
因为 $r$ 可逆，$J_E[r]$ 有限 étale，其闭子群概形也有限 étale。
所以此处排除几何核点确实排除了整个群概形核；不存在残留纯不可分核。

设 $N\in J_E(\bar K)$ 的拉回平凡。其商拉回具有自然 $G$-作用。
任取全局无零截面后，各群元只乘一个全局单位，后者必为常数。
在全群固定点 $P_0$，自然拉回作用在 $N_{\pi(P_0)}$ 上是恒等，迫使每个常数为一。
于是该截面不变，借助有限商不变量与投影公式下降为 $N$ 的无零截面。
$N$ 必平凡。这一论证用的是全群固定点，不是只知道某处有部分分歧。

平凡群概形核使群同态在所有测试概形上单射，即为 monomorphism；其 proper 性再给闭浸入。
最后一步的标准判据见
[Stacks Lemma 41.7.2：proper monomorphism 等价于闭浸入](https://stacks.math.columbia.edu/tag/04XV)。
故 $H=\pi^*J_E$ 是一个真正的嵌入椭圆子群，而非仅同源像。

对单位分支，$\operatorname{Lie}(J_C)=H^1(C,\mathcal O_C)$，微分核为 $G$-不变量。
有限 $\pi$ 使 $H^1(C,\mathcal O_C)=H^1(E,\pi_*\mathcal O_C)$；
$r^{-1}\sum_g g$ 将不变量分裂为直和因子，其像是 $\mathcal O_E$。
故 $\dim\operatorname{Lie}(B)=h^1(E,\mathcal O_E)=1$。

可在 $\bar K$ 上进行下一步：$B$ 包含一维光滑闭连通子群 $H$，
单位点局部维数至少为一，而切空间维数恰为一，故局部环正则。
在代数闭底域上得到光滑性，群平移推广至单位分支；同维闭子群只能是整个 $B^0$。
于是 $B^0=H$ 为群概形等式，并可下降到 $K$。
这没有从点集维数跳过非约化结构，也没有在特征二错误使用二次覆盖的平均。
$r=1$ 时 $\pi=\mathrm{id}$、$B=J_C=J_E$，论证与结论均相容。

## 8. Step 7：完整陪集、下降及 Jacobian

在 $\bar K$ 选取 $P_*$ 仅用于描述几何陪集。
差映射的像连通且包含零元，故落在 $B^0=H$。
Step 4 已证明非恒定，故其 proper 一维像是整个 $H$，不是陪集的真开子集。
原态射双有理到该光滑射影陪集；光滑射影曲线的双有理态射为同构。
因此 $\alpha$ 几何基变换后是闭浸入，该性质下降，得到 $X\simeq Y$ 于 $K$。

张量乘以 $\pi^*N$ 的 $J_E$ 作用与闭像 $Y$ 本来就在 $K$ 上定义。
作用保持 $Y$，以及

$$J_E\times Y\longrightarrow Y\times Y,\qquad (N,L)\longmapsto(L,L\otimes\pi^*N)$$

为同构，均可在忠实平坦扩张 $\bar K/K$ 后检验。
$Y\to\operatorname{Spec}K$ 非空、光滑且满射，因此这确给 fppf torsor，不只是几何点上的简单传递作用。
经 $X\simeq Y$ 与 $E\simeq J_E$ 传回原曲线，完全不需要 $X(K)\ne\varnothing$。

最后，任选几何基点识别 $X$ 与其 torsor 群，再以 Abel 映射识别 $\operatorname{Pic}^0(X)$；
换基点只施加平移，平移在 $\operatorname{Pic}^0$ 上的作用为恒等，故诱导群同构可下降。
因此确为 $\operatorname{Jac}(X)\simeq E$，没有留下同源次数或底域扭曲未定的问题。

## 9. 有界来源与检查记录

公开一手核对限于原公式和这里实际使用的标准几何事实。
重新核对了 [JR 作者 v2 §3.1](https://arxiv.org/html/2508.18578v2#S3.SS1) 的 $A_0,A_1$、
$M$ 乘积顺序、积分定义、行列式及循环恒等式，与作者式 (5)–(8) 一致。
没有把 JR 的谱奇点叙述当作动力坏纤维已证明，也没有借用 Beauville 复数域定理向小特征直接外推。
标准 Picard 刚化与 proper monomorphism 来源已在对应步骤给出；新桥的通过依据是上面的具体数学核查。

本审查另执行一次无文件写入的 SymPy 精确代数夹具，结果如下：

| 独立代数核对 | 结果 |
|---|---|
| $\det(A_0+zA_1+z^2P)=z^3$ | PASS |
| $\operatorname{tr}A_0=t$ | PASS |
| $\det A_0=0$ | PASS |
| $A_0^2=tA_0$ 的四个矩阵元 | PASS |

这些是形式有理函数恒等式核对；全 $r$ 端点系数、模族、除子与群概形结论由正文论证承担。
未做有限域穷举、数值拟合、页数测试、PDF 验收或任何外部写操作。
未运行与本次变更无关的历史测试，也未扩大为新项目。

## 10. 修复要求与最终交接边界

强制修复：无。没有需要先退回作者处理的硬缺口。

仅有两处可选的记号／表述清晰化，不影响本票 PASS：

1. 作者 L283 的 $L(-1)$ 可显式记为 $L\otimes\tau^*\mathcal O_{\mathbb P^1}(-1)$，避免误认作减去一个点。
2. 作者 L417–420 可补“在 $\bar K$ 上检验光滑性和单位分支等式，再下降”，方便非完美底域读者核对群概形层面的论证。

未代作者实施以上可选编辑；冻结作者稿与输入哈希保持不变。
允许交接的结论仅为该稿 Claim 的泛纤维 Jacobian／torsor 识别及其谱线丛桥。
有限坏参数、特殊纤维类型和重数、回返平移点及轨道结论仍不在本票内。
最终审查判定：**PASS，原量词不变；无新增科学锁，无 Route／价值／页数评分。**
