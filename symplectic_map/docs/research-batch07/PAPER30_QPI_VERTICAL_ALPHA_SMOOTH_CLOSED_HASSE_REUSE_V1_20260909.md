# Paper30 qPI：完整光滑闭纤维的 Hasse 身份前提复用 V1

日期：2026-09-09。作者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
类型：仅替换一个旧消费者前提的有界作者证明；不是新独立发现、正式评价或论文稿。

## Claim

保持 [垂直微分 Phase A V1–V3](PAPER30_QPI_VERTICAL_ALPHA_SCOPE_PHASE_A_V1_20260909.md)
的原对象与光滑有限能级范围。设 $k$ 为其中允许的完美剩余域，
$\eta,t_0\in k^\times$，$\eta$ 的精确阶为 $m$，$p=\operatorname{char}k>0$ 且 $p\nmid m$。
在原八吹起曲面 $S=S_{t_0,\eta}$ 上取原小阶积分
$$f=J=I_{m,\eta}(x,y;t_0):S\longrightarrow\mathbb P^1_c,$$
保留原能级参数 $c$、反典范边界 $D$ 和 $U=S\setminus D$。
设 $h$ 是一个有限闭能级，在其有限剩余域扩张 $l/k$ 上视为 $h\in l$，
并假设完整概形纤维 $X_h=f_l^{-1}(h)$ 在 $l$ 上光滑。
原本直接给定 $h\in k$ 或有限几何能级的情形分别取 $l=k$ 或 $l=k(h)$。

**SH.1（选定纤维前提）。** $X_h$ 是射影、光滑、几何整约化的亏格一曲线，
它完整地位于原 $U_l$，包括与四条末端线的交点。
这一结论只需 Gfield 的原完整 pencil、Stein 几何连通性及已假定的该纤维光滑；
不需 Ffib 关于全部有限纤维几何整约化性的供应证明。

**SH.2（同能级的完整几何模型识别）。** 令 $\bar l$ 为 $l$ 的代数闭包，
$T=t_0^m$、$\varepsilon=(-1)^{m+1}$，取原射影 Weierstrass 三次族，其仿射式为
$$W_c:\quad v^2+cuv-\varepsilon Tv=u^3-Tu^2.$$
保留既有原泛谱模／Jacobian／torsor 全证明及 W0 的当前纯临界有限代数供应后，
Hloc 的 L(a) 在原参数 $c=h$ 可直接应用，给出完整曲线同构
$$X_h\otimes_l\bar l\simeq W_h\otimes_l\bar l.$$
该同构经几何光滑点的 henselian 提升取得，不声称在 $l$ 上已有指定点、全局泛截面或典范同构。

**SH.3（原闭纤维 Hasse）。** 对原谱商的完整光滑模型 $E_h$，
指定微分的 Cartier 系数为
$$H_p(T,h;\varepsilon)^{1/p},\qquad
H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases}$$
通过 SH.2 的实际完整曲线识别，这给出原 $X_h$ 的几何 Jacobian 的同一 Hasse 零性质：
$$X_h\text{ 的几何 Jacobian 超奇异}\quad\Longleftrightarrow\quad H_p(T,h;\varepsilon)=0\text{ 于 }l.$$
因此对 Phase A 已限定的完整光滑闭纤维消费者，可以用本件替换
Hloc 实际前提中的 Ffib 箭头，不改变 V1–V3、原泛 Jacobian 或闭纤维 Hasse 的责任。

## Status

`PROVABLE AS STATED / AUTHOR_PROOF`，待另一非作者检查。
证明没有新增光滑性假设：Claim 只使用 Phase A 原来已经限定的光滑概形纤维。
本件不宣称 Hloc 对所有有限纤维的旧版本从此无需 Ffib，也不修改旧作者稿或依赖报告。

## Assumptions 与既有输入

以下是已接受、当前不变的原对象证明；作者快照中的历史待审字样由相同哈希接受处置接续。

| 别名 | 原输入与本件消费的准确出口 |
|---|---|
| P、Nbd | [原辛／极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)、[边界法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)：原中心、$D=-K_S$、$D^2=0$、极除子与精确阶；作为 Gfield 的原供应保留 |
| Gfield | [原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) Steps 1–6：同一完整 pencil、所有几何纤维连通、几何泛光滑亏格一、有限纤维位于 $U$ |
| Jspec | [原 Lax Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) 原两图及 Steps 2–7：实际谱模族、有理逆、固定除子差、无核和原域 torsor 作用 |
| Wreuse | [共享 Weierstrass 复用 V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) 70–161：原两图与全特征泛谱前提、W0 纯临界有限性，以及任意原域 Step 2a |
| Bbad 的纯方程段 | [准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) 138–166、217–251、305–311、329–365：带原点泛变换、$W$ 的正则 proper flat 及几何整约化纤维、完整谱侧临界有限代数 |
| Hloc | [指定点／局部模型复用](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) L(a) 及 L.1–L.3；只改接其实际 $X$ 侧特殊纤维前提，其他前提与最小模型唯一性保留 |
| Ddiff | [圆分整除微分](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) 206–233：原谱微分的全图正则性与 Cartier 系数规范 |

本件不把相同谱方程、相同亏格或未知核同源当成 Jspec 的替代。
也不替换 Wreuse 用于泛光滑的 W0 纯临界代数证明。

## Notation 与 Proof Strategy

始终把 $S,f,D,X_h$ 视为原对象的明确基变换；参数 $c$ 不作仿射或分式线性重参数化。
上标或下标 $\bar l$ 表示到 $\bar l$ 的基变换。
局部模型的底环为
$$A_0=\bar l[c]_{(c-h)},\qquad A=A_0^h,\qquad L=\operatorname{Frac}(A),$$
其中 $A_0^h$ 是普通 henselization，剩余域仍是 $\bar l$。
这一步在剩余几何中完成，不是对原算术 DVR 作额外分歧状态提升。

依赖顺序是：

1. Gfield 的几何连通性加所选纤维光滑，验证 Hloc 的 $X$ 侧特殊纤维前提。
2. 原 Jspec／Wreuse 和 Bbad 纯方程段给 Hloc 其余泛数据与 $W$ 模型前提。
3. 几何点提升、局部 torsor 平凡化和最小正则模型唯一性给同一 $h$ 的完整同构。
4. 原谱微分的 Cartier 计算沿完整同构传递；仅 Hasse 零性质返回 $l$，不下降未经指定的点或同构。

## Proof

### Step 1. 原完整纤维与几何连通性

域扩张不改变 $\eta$ 的精确阶，且保持 $t_0$ 为单位。
原八个中心、原矩阵与原积分的公式基变换后仍是相同对象。
因此在代数闭域 $\bar l$ 上可对原 $f_{\bar l}$ 直接应用 Gfield，而不是另外选择一个 pencil。
Gfield Step 2 的齐次截面规范是 $1,J$，故保留原 $c=J$，并有
$$f_l^{-1}(\infty)=mD_l,\qquad f_{\bar l}^{-1}(\infty)=mD_{\bar l}.$$
这里关于 $l$ 的等式由原定义或其忠实平坦基变换验证；不从点集相同推出概形等式。

$f$ 非恒定且 $S$ 射影，故其像为整个 $\mathbb P^1$；每个闭纤维非空。
有限纤维是 $S_l$ 中的闭子概形，因而射影，不因其位于开曲面 $U_l$ 而失去完整性。
它不碰 $D_l$，因为后者是无穷纤维的完整支集。
本步没有把 $X_h$ 限制到原环面，也没有删除末端交点。

Gfield Step 3 对 $f_{\bar l}$ 的 Stein 分解用完整截面数排除包括不可分次数在内的全部复合次数，
给 $(f_{\bar l})_*\mathcal O=\mathcal O$ 及所有几何纤维连通。
因此特定 $X_{h,\bar l}$ 连通；并不要求 $h$ 落在 Gfield Step 4 选出的某个预定开集。
Step 4 的作用在本件是保留几何泛光滑，所选闭纤维的光滑性来自 Claim 原假设。

### Step 2. 光滑加几何连通给几何整约化与亏格一

$X_h/l$ 光滑，故 $X_{h,\bar l}$ 是光滑曲线，局部环正则，特别地约化且为局部整环。
若两个不同不可约分量相交，交点的局部环会有至少两个极小素理想，不可能为整环。
曲线为 Noetherian，只有有限个不可约分量；这些不相交的闭分量各自也是开集。
Step 1 的连通性遂迫使只有一个分量。因此 $X_{h,\bar l}$ 整且约化，
这正是 $X_h/l$ 的几何整约化性，不是把仅在 $l$ 上连通误读为几何连通。

Gfield 的原线性系给 $X_{h,\bar l}\sim mD_{\bar l}$。
由于 $S_{\bar l}$ 光滑、$J-h$ 非零，此纤维为有效 Cartier 除子。
原 $K_S=-D$、$D^2=0$ 与伴随公式给
$$p_a(X_{h,\bar l})=1+\frac{mD\cdot(mD+K_S)}2=1.$$
对光滑射影几何整曲线，算术亏格等于几何亏格，故其亏格为一。
这一论证对 $p=2,3$ 以及 $m=1$ 原样成立，没有除以剩余域中的 $2$ 或 $m$。
SH.1 得证。到此完全未使用 Ffib 的整数 Picard 格或全部有限纤维分量排除。

### Step 3. Hloc 的全部模型与泛数据前提

取
$$\mathscr X=S_{\bar l}\times_{\mathbb P^1_c}\operatorname{Spec}A,
\qquad \mathscr W=W_{\bar l}\times_{\mathbb A^1_c}\operatorname{Spec}A.$$
原 $S_{\bar l}$ 是实际八次光滑点吹起的光滑整曲面。
原 $f_{\bar l}$ 对光滑曲线平坦：在每个底 DVR 上，非零底函数在整曲面的局部环中不是零因子，
无挠 DVR 模平坦。射影性给 proper，原构造给有限表示。
先局部化到 $A_0$ 再作 ind-étale 的 henselization，得到 Noetherian 正则模型 $\mathscr X$；
此处正是 Hloc 的局部化／henselian 正则性接口，不宣称任意基变换都保持正则。
其特殊纤维为 Step 2 已证的同一个 $X_{h,\bar l}$，几何整约化；
泛纤维的光滑射影几何整亏格一来自 Gfield，且随域扩张到 $L$ 保持。

$\mathscr W$ 的所需前提仍由 Bbad 217–251 的完整纯方程证明供应。
记其仿射方程左侧为 $F_W=v^2+cuv-\varepsilon Tv-u^3+Tu^2$。
唯一无穷远点 $O=[0:1:0]$ 光滑，给实际截面；分量与该点相交的论证给每条几何纤维整约化；
三次 Hilbert 多项式给平坦，射影性给 proper；纤维奇点处 $uv\ne0$、$\partial_cF_W=uv\ne0$
给总空间正则。局部化和上述 henselization 后这些前提保持。
泛光滑仍用 Wreuse 的原 W0 证明，包括 Bbad 305–311、329–365 的完整同构
$$Z_W\simeq\operatorname{Spec}\bar l[z]/((T-z^2)^2-\varepsilon Tz).$$
该有限临界代数的泛化为空，给几何泛光滑；本件未新造更短替代引理。

Jspec 的实际谱模、原状态有理逆及不可分次数检查、循环固定除子差、无核和作用下降全保留。
Wreuse 原两图与任意原域 Step 2a 仍供应其谱几何前提。
因此在原泛域已有真实的谱商 $E$-torsor $X$，而非只有相同亏格或未知核同源；
基变换到 $L$ 得所需作用。Bbad 138–166 的原点检查给带原点 $\iota_L:E_L\simeq W_L$。
这逐项完成 Hloc L(a) 的其余前提，未从所求闭纤维同构倒推任何泛身份。

### Step 4. 几何点提升与指定泛同构的双向延伸

$X_{h,\bar l}$ 非空、有限型且光滑，因 $\bar l$ 代数闭，可取任意几何点 $q_0$。
这不调用有限域 Weil 选点，也不指定动力学平移点。
有限表示平坦态射在几何光滑纤维点处光滑，所以 $\mathscr X/A$ 在 $q_0$ 邻域光滑。
如 Hloc L.1，取该邻域到 $\mathbb A^1_A$ 的 étale 坐标，平移其剩余值为零，
沿零截面拉回后用 henselian 性提升指定剩余点，得到截面 $e_A$。
所取底环是 $A_0^h$，没有更改 $c$；截面仅在该局部底上存在。

真实 torsor 作用使 $N\mapsto e_L+N$ 为 $E_L\simeq X_L$。
与 $\iota_L$ 合成其逆，得到唯一满足 $\phi_L(e_L)=O_L$ 的指定等变泛同构。
对 $\mathscr X,\mathscr W$，特殊纤维都是唯一重数一竖直整分量，
又是参数 $c-h$ 的主 Cartier 除子；相应正规线丛次数为零。
因此没有作为特殊纤维分量的第一类例外曲线，两者是同一正亏格泛曲线的最小正则 proper 模型。
Hloc L.2–L.3 的最小模型唯一性将 $\phi_L$ 和其逆各自延伸。
两次复合在概形稠密泛纤维上恒等，目标分离，因而处处恒等。
遂得 $A$ 上完整同构 $\phi_A:\mathscr X\simeq\mathscr W$，限制到特殊纤维即 SH.2。
它严格位于同一 $c=h$；没有改能级，也没有先丢掉末端点再仅作双有理比较。

### Step 5. 同一闭能级的原完整谱商与正则微分

Step 4 已给 $W_{h,\bar l}$ 光滑。定义原谱商的两图为
$$\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0,$$
$$\mu^2-(1+hV+TV^2)\mu+\varepsilon V=0,\qquad V=Z^{-1},\ \mu=\lambda Z^{-2}.$$
在 $Z\ne0,\infty$ 处，方程使 $\lambda\ne0$；Bbad 的互逆变换
$u=\varepsilon TZ/\lambda$、$v=\varepsilon T^2/\lambda$
把这一开集接到同一 $W_h$ 的光滑开集。
剩余四端点的偏导仍为 $-T,T,-1,1$，在所有允许特征中都是单位。
故整个 $E_{h,\bar l}$ 光滑。
原两图的有限平坦推下为 $\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2)$，
从而射影、几何连通且亏格一；结合光滑性给几何整。
已有开集同构遂唯一延伸为完整光滑射影曲线同构 $E_{h,\bar l}\simeq W_{h,\bar l}$。
原两图在 $l$ 上的几何光滑性可沿 $\bar l/l$ 检测；本件使用的曲线同构仍只在 $\bar l$ 上选择。

原微分为
$$\omega=\frac{dZ}{2\lambda-(T+hZ+Z^2)}.$$
记原谱方程左侧为 $\Phi=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3$。
有限光滑点在分母为零时改用 $-d\lambda/(\partial_Z\Phi)$；光滑性保证相应偏导为单位。
无穷远图为 $-dV/(2\mu-(1+hV+TV^2))$，两端点分母是单位。
因此这是完整 $E_h$ 上的非零正则微分；不是仅环面的有理形式。
通过两个完整同构拉回，得到完整 $X_{h,\bar l}$ 的非零正则微分。

### Step 6. Cartier 系数及返回原域的准确责任

按 Ddiff 的同一规范，奇 $p$ 时置 $Y=2\lambda-(T+hZ+Z^2)$，则
$Y^2=(T+hZ+Z^2)^2-4\varepsilon Z^3$，$\omega=dZ/Y$。
Cartier 的 $p^{-1}$ 半线性与次数界 $2p-2$ 给
$$\mathcal C(\omega)=Y^{-1}\mathcal C(Y^{p-1}dZ)
=H_p(T,h;\varepsilon)^{1/p}\omega.$$
特征二时 $S(Z)=T+hZ+Z^2$，$\omega=dZ/S(Z)$，故
$$\mathcal C(\omega)=S(Z)^{-1}\mathcal C(S(Z)dZ)=h^{1/2}\omega.$$
两式只保留指数同余 $p-1$ 的唯一项，并使用 Step 5 的全曲线正则性。
Cartier 与曲线同构的拉回相容，因此对所选拉回微分，原 $X_{h,\bar l}$ 具有同一显示系数。
这不是对任意未指定原域微分宣称完全相同的数值规范。

改变局部截面、同构或微分基只会在一维正则微分空间中乘以非零标量 $a$，
而 $\mathcal C(a\omega)=a^{1/p}\mathcal C(\omega)$，不会改变 Cartier 是否为零。
亏格一曲线的几何 Jacobian 超奇异恰当且仅当该 Cartier 算子为零；
对于没有 $l$-点的 $X_h$，这一性质按其几何 Jacobian 定义，不要求先平凡化原域 torsor。
$H_p(T,h;\varepsilon)\in l$，且 $l\hookrightarrow\bar l$ 单射，
故几何计算中的零条件恰等价于它在 $l$ 中为零。
这是本件送回原域的责任，不是把所选几何点或 $\bar l$ 上同构未经下降数据就送回 $l$。
SH.3 得证。$\square$

## Corrections or Missing Assumptions

没有新增假设或未闭合数学步骤。改接只适用于已经光滑的完整概形纤维；
“约化支集光滑”“原环面光滑”或“曲线正则但未核几何光滑”均不能替代 Claim 的原前提。
本件不判定其他能级是否光滑，不扩展奇异层，也不改变 Hasse 根重数或 V1–V3 的理想精度。

## Open Risks 与验证边界

作者尚需非作者检查，尤其核对 Step 2 的实际纤维身份、Step 3 的全部 Hloc 前提和 Step 6 的下降范围。
Gfield、Jspec、Wreuse、W0、Hloc、Ddiff 未被本件重新宣告独立通过。
其中原泛 Jacobian 的完整证明和 W0 当前有限临界代数仍必须保留；
唯一被本有界消费者替换的是 Hloc 选定光滑纤维的 Ffib 特殊纤维前提供应。

本次全文读 proof-writer；它要求将原假设、几何基变换、局部点选择和可下降的零性质逐项分开。
本次重新实读 Gfield Claim 及 95–253、TH 的准确范围和 Phase A 对完整光滑能级／Hasse 的锁定段。
Hloc L(a) 与 L.1–L.3／实际前提、Wreuse 70–161、Bbad 指定纯方程段及 Ddiff 206–233
已在紧邻任务中亲读，本件继续使用这些未变实际文本，不引用旧依赖报告作数学证明。
未读取新非作者票，未执行数值实验、GPU、联网或外部写入。

| 冻结输入 | SHA-256 |
|---|---|
| Phase A | `ca6a8e6695709c2eaaff4707bcb94ccfd86367afb492d5ea87da6a1d90396f2f` |
| Gfield | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |
| Jspec | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| Wreuse V2 | `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2` |
| Bbad | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |
| Hloc | `0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e` |
| Ddiff | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |

只新增本文件，不改冻结作者件、249 行依赖报告、brief、manifest、锁或索引。
不授予独立新意、价值、容量或候选准入，不新建论文项目。
