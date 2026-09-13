# Paper30 qPI P03：所有素数的一层圆分垂直理想

日期：2026-09-09。作者：主控 `/root`。类型：新的有界全素数作者证明。
`route_applicability: NOT_APPLICABLE`。不是正式候选、论文或独立接受。

## Claim

令 $p$ 为任意素数，$q=\zeta_p$、$\pi=q-1$，令 $\mathcal O$ 为
$\mathbb Z[\zeta_p]$ 在 $p$ 上的圆分 DVR，或它的有限无分歧扩张。
$p=2$ 时 $q=-1,\pi=-2$。允许完成该 DVR，不允许在本定理中另加有分歧基变换后仍把 $\pi$ 称为参数。
取任意 $t\in\mathcal O^\times$，保持原八截面模型及完整开放部分 $\mathcal U_t$，并定义
$$I_p=[Z^p]\operatorname{tr}(A(q^{p-1}Z)\cdots A(qZ)A(Z)),\qquad
\alpha_p=p^{-1}d_{\rm state}I_p.$$
这里固定实际时间 $t$ 与 $q$，只对原两个状态方向求微分。

记剩余域为 $k$、$T=\bar t$、
$$J=y+x/y-x-T/x\quad\text{on }U_0=\mathcal U_t\otimes k.$$
令
$$H_p(T,h)=
\begin{cases}
[Z^{p-1}]\bigl((T+hZ+Z^2)^2-4Z^3\bigr)^{(p-1)/2},&p>2,\\
h,&p=2.
\end{cases}$$
给定任一光滑有限小阶能级 $X_h=(J=h)$，在需要时作有限剩余域／无分歧扩张定义 $h$。
本件不将奇异能级叫作超奇异。

**V.1：实际两方向理想。** 对每个 $P\in X_h$，在原局部环
$\mathscr A=\mathcal O_{\mathcal U_t,P}$ 中，取 $j$ 为 $J$ 的任一局部提升，
取 $\widetilde H_p(t,j)$ 为 $H_p(T,J)$ 的任一局部提升，则
$$\boxed{\quad
\mathfrak c(\alpha_p)_P=(\pi,\widetilde H_p(t,j)).\quad} \tag{V1}$$
右端实际只依赖剩余函数 $H_p(T,J)$，不依赖这些提升的选择。
若 $H_p(T,h)\ne0$，两边均为单位理想。
若 $h$ 是 $H_p(T,h)$ 的重数为 $e_h$ 的根，完成后可以写成
$$\widehat{\mathfrak c(\alpha_p)}_P=(\pi,z^{e_h}),\qquad \bar z=J-h. \tag{V2}$$
此处 $e_h$ 是 Hasse 根重数，不是圆分分歧指数；不先验假定所有根简单。
结论覆盖完整光滑能级和全部四条末端线上的交点，不仅环面。

**V.2：状态评价与未整除微分。** 对约化到光滑超奇异能级的任一无分歧 DVR 状态提升，
两个实际 $\alpha_p$ 系数的公共 $\pi$ 赋值准确为一；约化到光滑普通能级时准确为零。
因为 $v_\pi(p)=p-1$，未整除原微分的局部理想为
$$\mathfrak c(dI_p)_P=(\pi^p,\pi^{p-1}\widetilde H_p(t,j)), \tag{V3}$$
其状态评价公共阶在上述两种情形分别准确为 $p$ 和 $p-1$。
这是系数沿环同态的评价，不是向 DVR 的零相对微分模拉回一形式。

## Status and Scope

PROVABLE AS STATED（以下三个实际作者证明接口合成；整体仍待非作者核查）。
本件把已完成的特征三诊断推进为**全部素数、任意单位时间提升、全部光滑有限状态**，
但严格固定圆分层数 $a=1$ 与剩余阶 $m=1$。
原发散 P03 的全部 $a,m$ 目标仍 OPEN，不能用本件的一层结论代替它。
本件没有宣布全 ramified jet、稳定约化、晶体同构或独立论文价值。

## Assumptions, Inputs and Notation

1. 原 $A$、矩阵次序与原八中心固定于[整数 brief §2](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)。
   同一个模型上的 $\alpha_p$ 全局正则及
   $$\bar\alpha_p=H_p(T,J)dJ$$
   消费已接受[整除证明 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)
   和[完整模型 G Step 6](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)。
2. 原小阶 $J$ 是完整无基点 pencil；其每条光滑有限纤维光滑、射影、几何整、亏格一，
   且 $dJ|_{X_h}\ne0$。原
   $$\Omega=dx\wedge dy/(xy)$$
   在整个 $U_0$ 正则非退化；不删四条末端仿射线。
   对奇 $p$，该光滑层的谱四次式 $(T+hZ+Z^2)^2-4Z^3$ 可分。
   这是已接受原小阶几何／谱接口，不是从首 jet 计算反推的前提。
3. 对奇 $p$，使用[首 jet 矩阵引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md)
   的 $N=p$ 部分；该件同时给出先除 $p$、后模 $\pi^2$ 的实际循环插入接口。
4. 对奇 $p$，使用[纯四次曲线配对引理](PAPER30_QPI_VERTICAL_ALPHA_CARTIER_PAIRING_LEMMA_V1_20260909.md)
   CP.1–CP.2。此纯引理不承担下文 $R$ 的实际 qPI 身份，后者在 Steps 2–3 完整给出。
5. 原 [p3 作者件](PAPER30_QPI_VERTICAL_ALPHA_P3_DIAGNOSTIC_V1_20260909.md)
   及其[非作者检查](PAPER30_QPI_VERTICAL_ALPHA_P3_INDEPENDENT_CHECK_V1_20260909.md)
   作为已核低阶对照保存，不用其有限量词代签这里的任意 $p,t,h$。

用大写 $Z$ 表示谱变量，$z$ 表示完成局部法向参数，避免混同。
$\mathfrak c$ 是原局部自由秩二相对微分模的系数理想；完成时使用该有限模的完成／连续微分。
没有把形式幂级数环的未完成抽象 Kähler 模冒称自由秩二。

## Proof Strategy and Dependency Map

1. 从原全局正则 $\alpha_p$ 及其准确约化，定义 Hasse 零曲线上的内在切向首 jet。
2. 它是完整射影亏格一曲线上的正则一形式；与 $dJ$ 楔积后除以原 $\Omega$ 得到常数。
3. 在原第一末端图给一个真正正则的矩阵 gauge，直接计算这个常数的统一系数公式 $\Lambda_p$。
4. 纯四次曲线上的配对值一证明 $H_p=0$ 时 $\Lambda_p\ne0$；不是从有限素数结果外推。
5. 特征二用原两因子迹的精确式另证；最终两方向局部消元给 V.1–V.2。

## Proof

### Step 1. 任意 Hasse 根的内在切向首 jet

先固定任一素数及一条光滑 $X_h$，且 $H_p(T,h)=0$。
在 $P\in X_h$ 附近选 $j$ 提升 $J$，并固定 $H_p$ 的任意系数提升多项式 $\widehat H$。
全局约化式及相对微分模的 $\mathcal O$-平坦性给唯一的一形式
$$\gamma_j=\frac{\alpha_p-\widehat H(j)\,dj}{\pi}.$$
此处唯一性针对已选 $j,\widehat H$；没有声称分解本身典范。
在环境余切模的限制中定义
$$\nu_h=[\bar\gamma_j|_{X_h}]
\in\Omega^1_{X_h/k}
=\Omega^1_{U_0/k}|_{X_h}/\mathcal O_{X_h}dJ. \tag{1}$$

如果 $j'=j+\pi f$，则模 $\pi^2$ 的差为
$$\widehat H(j')dj'-\widehat H(j)dj
\equiv\pi\bigl(f\widehat H'(j)dj+\widehat H(j)df\bigr).$$
限制到 $X_h$ 后，第二项为零，第一项是 $dJ$ 的倍数。
更换 $\widehat H$ 的系数提升又只增加一个 $\pi L(j)dj$，在 (1) 中也为零。
因此 $\nu_h$ 在所有图上粘成正则一形式；此构造不要求 Hasse 根简单。
它只使用实际 $\alpha_p$、剩余 $J$ 和固定 $\pi$，不需要任一全局 $J$ 或辅助函数的整提升。

定义环境线丛同构
$$\Phi_h:\Omega^1_{X_h/k}\longrightarrow\Omega^2_{U_0/k}|_{X_h},
\qquad[\eta]\longmapsto\eta\wedge dJ.$$
$dJ|_{X_h}$ 非零保证这是同构；目标不是一维曲线自身的 $\Omega^2_{X_h}$。
所以
$$c_h=\Phi_h(\nu_h)/\Omega|_{X_h}\in H^0(X_h,\mathcal O_{X_h})=k(h). \tag{2}$$
最后等号来自光滑射影几何整性；可先在代数闭包上证明，再下降。
要证明 $\nu_h$ 处处非零，只需在一个实际点准确算出这个常数并证明它非零。

### Step 2. 第一末端图上的正则原矩阵，而非谱替代模型

使用原第一末端图
$$x=u^{-1},\quad y=W=1+uv,\qquad
J_t=W-v/W-tu.$$
开放环 $\mathcal O[u,v,W^{-1}]$ 包含整条 $u=0$ 末端线。
在 $u\ne0$ 上取 $G=\operatorname{diag}(u,1)$；直接共轭原 $A$ 得到
$$\widehat A=GAG^{-1}=\widehat A_0+Z\widehat A_1+Z^2E,$$
$$\widehat A_0=
\begin{pmatrix}t-v&-1\\-v(t-v)&v\end{pmatrix},\qquad
\widehat A_1=
\begin{pmatrix}J_t-1&u\\v-t+v^2/W&1\end{pmatrix},\qquad E=\operatorname{diag}(1,0). \tag{3}$$
右端每个条目在整个图上正则；$G$ 不在 $u=0$ 可逆并不妨碍右端定义该正则矩阵。
且其迹、行列式准确为
$$\operatorname{tr}\widehat A=t+J_tZ+Z^2,\qquad \det\widehat A=Z^3. \tag{4}$$
$G$ 与 $Z,q$ 无关，故有序乘积的迹在 $u\ne0$ 与原迹相同，
两边正则后相等延到整个图；没有任意重排因子或更改 $I_p$ 常数规范。

虽然 $G$ 依赖状态，不能直接忽略 $dG$，但这里不这么做：
**直接对正则矩阵 $\widehat A$ 重新应用整数循环插入**。
它给同一个原函数的精确等式
$$\alpha_p=[Z^p]\operatorname{tr}
\bigl(d\widehat A(Z)\widehat A(q^{p-1}Z)\cdots\widehat A(qZ)\bigr). \tag{5}$$
因为首先在特征零有 $dI_p=p[Z^p](\cdots)$，然后在整图中唯一延拓；
$d\widehat A$ 已包含全部状态 gauge 导数。

### Step 3. 所有奇素数上的准确常数

设 $p>2$。$v_\pi(p)=p-1\ge2$，所以 $\mathcal O/(\pi^2)$ 的特征为 $p$。
在该商环对 (5) 应用首 jet 引理，置
$$\Delta=(t+J_tZ+Z^2)^2-4Z^3,$$
得到
$$\alpha_p\equiv
\widehat H_p(t,J_t)dJ_t+\pi\beta_p\pmod{\pi^2},$$
$$\beta_p=[Z^p]\Delta^{(p-3)/2}
\operatorname{tr}\bigl(d\widehat A[\widehat A,Z\partial_Z\widehat A]\bigr). \tag{6}$$
$\widehat H_p$ 可取显示的整数系数提取多项式。
零阶迹表达式与该 Hasse 形式之差是 $p$ 的倍数，在这里确实属于 $(\pi^2)$。
所有式子使用实际 $t$；因此 (6) 的首谱项只需 $T=\bar t$，
没有漏掉任意时间提升对零阶参照项的影响。

在剩余第一末端点
$$u=0,\quad v=1-h,$$
有 $J=h$、$dJ=(v+v^2-T)du-dv$，而 $\Omega=-du\wedge dv$。
令 $a_v=v+v^2-T$，在此点的矩阵与两个状态导数是
$$A_*=
\begin{pmatrix}T-v&-1\\-v(T-v)&v\end{pmatrix}
+Z\begin{pmatrix}-v&0\\v-T+v^2&1\end{pmatrix}+Z^2E,$$
$$A_u=Z\begin{pmatrix}a_v&1\\-v^3&0\end{pmatrix},\qquad
A_v=\partial_v A_*.$$
所以将 (6) 楔 $dJ$ 并除以 $\Omega$，得到
$$c_h=\Lambda_p(T,h):=[Z^p]R(T,h,Z)f(T,h,Z)^{(p-3)/2}, \tag{7}$$
其中 $f=(T+hZ+Z^2)^2-4Z^3$，而
$$R=\operatorname{tr}\bigl((A_u+a_vA_v)[A_*,Z\partial_ZA_*]\bigr)\big|_{v=1-h}. \tag{8}$$
式 (8) 的有限矩阵相乘准确给 $R=r_4Z^4+r_3Z^3+r_2Z^2+r_1Z$，
$$r_4=h^2-3h-T+2,$$
$$r_3=-2h^3+14h^2+6hT-24h-8T+12,$$
$$r_2=-h^4+3h^3-2h^2+5hT+3T^2-4T,$$
$$r_1=-h^3T+3h^2T+hT^2-2hT. \tag{9}$$
这正是纯配对引理固定的四个系数，至此完成它与原实际首 jet 的接口。
给定任一固定素数时 (7) 是有限系数提取；全素数的论证由 (5)–(8) 和矩阵引理承担，
不是对 $p=3,5,7,11$ 样本的插值。

光滑 $X_h$ 的 $f$ 可分。纯配对引理给 $H_p(T,h)$ 与 $\Lambda_p(T,h)$ 不同时为零；
其证书为 $4(R/Z)=f'B-(4Z^2+2(h-2)Z)f$，其中 $B$ 首一三次，
根上留数配对为一，两个 Cartier 像同时为零则该配对为零。
因此当前 $H_p(T,h)=0$ 时，(7) 的 $c_h$ 非零。
由 (2)，$\nu_h$ 在整个完整 $X_h$ 上处处非零，包括其余三个末端点。
这一延拓使用的是已正则的内在 $\nu_h$，不假设 (3) 的 gauge 覆盖其他图。

### Step 4. 特征二由原两因子迹另证

本步不把奇素数引理中的半整数指数代入二。
令 $b=x(y-1)$。原矩阵满足 $\operatorname{tr}A_1=J_t$、$\det A_1=-b$，
并且
$$I_2=\operatorname{tr}(A_0A_2+A_2A_0-A_1^2)
=2t-4b-J_t^2.$$
在特征零先除以二求状态微分，$\pi=-2$ 给
$$\alpha_2=-J_t\,dJ_t+\pi\,db. \tag{10}$$
取 $H_2(T,J)=J$，其唯一根 $h=0$。
在原环面上逐项求导，有整数 Laurent 证书
$$xy(b_x(J_t)_y-b_y(J_t)_x)-t-x(y+1)J_t
=2x(xy-x-y). \tag{11}$$
模二且在 $J=0$ 上，(11) 给
$$db\wedge dJ=T\Omega.$$
$T\ne0$，所以 Step 1 的内在 $\nu_0$ 在稠密环面非零；
双方全局正则且 $X_0$ 几何整，等式延到整个曲线，常数为 $c_0=T$。
本步也不要求 $b$ 在其他混合特征末端图正则。
于是所有素数的光滑超奇异层都已得到处处非零的首切向类。

### Step 5. 两状态理想、重根、时间提升与完成

在 $P\in X_h$ 的局部自由微分模中将 $dj$ 补为基 $(dj,\theta)$，写
$$\alpha_p=(\widehat H(j)+\pi A)dj+\pi B\theta.$$
首切向类处处非零给 $B(P)\ne0$，故 $B$ 是局部单位。
于是
$$\mathfrak c(\alpha_p)_P
=(\widehat H(j)+\pi A,\pi B)=(\pi,\widehat H(j)).$$
更换 $H_p(T,J)$ 的任何提升只增加 $\pi$ 倍数，不改变右端，证明 V1 的全部提升量词。
若 $H_p(T,h)\ne0$，已知约化 $H_p(T,J)dJ$ 在该点至少一个系数非零，
原系数理想就是单位理想，也符合 V1。

在 Hasse 根附近，底域扩张定义 $h$ 后可写
$$H_p(T,J)=(J-h)^{e_h}U(J),\qquad U(h)\ne0.$$
取任意 $z$ 提升 $J-h$；局部单位提升 $\widetilde U$ 后，
$\widehat H(j)-z^{e_h}\widetilde U\in(\pi)$，故
$$(\pi,\widehat H(j))=(\pi,z^{e_h}).$$
这先在实际局部环成立，随后张量完成环仍成立。
对闭点，有限无分歧扩张后可用光滑相对完成坐标，微分使用原有限模的连续完成；
对非闭点，前述局部自由模论证已经适用，不要求它由有限域扩张定义。
证明 V2。

由于 (7) 与 (10) 的切向常数仅依赖 $T,h$，任意两种具有相同剩余 $T$ 的时间提升
在相同剩余曲线上的内在首切向类相同；V1 的整个理想也只依赖剩余 Hasse 函数。
这不声称两个实际一形式或其法向首项相同，特征三端点已经展示二者可以不同。

最后将理想沿无分歧 DVR 状态提升评价：在超奇异层
$\widehat H(j)\in(\pi)$，所以 V1 的像准确为 $(\pi)$；普通层则为单位理想。
乘 $p$ 并用 $p=\text{unit}\cdot\pi^{p-1}$，得到 V3 及其准确公共赋值。证毕。

## Actual Verification, Sources and Open Risks

- 主控全文读首 jet 矩阵作者件（283 行）、纯曲线配对作者件（227 行）、
  p3 作者件（251 行）及其非作者报告（278 行），并实读旧 G Step 6 的全模型延拓接口。
- 新的[有限符号复核脚本](qpi_vertical_alpha_endpoint_algebra_v1_20260909.py)
  实际执行正常 exit 0：原迹／行列式、精确 $I_2$、模二切向恒等式、
  第一末端正则 gauge 及 $R$ 的全部四个系数均通过。
  该脚本不证明全素数矩阵引理、Cartier 非消失或全局几何延拓，也不生成数据文件。
- 原 C3、完整 pencil、辛形式和谱可分接口是已接受前置；标准局部理想消元不是新方法。
  纯配对中的 Cartier 规范另核 [Achter–Howe §§2.1–2.4](https://arxiv.org/html/1710.10726v5#S2.SS2)，
  本件不将一般 Cartier／de Rham 双性宣称为新理论。
- 实际新责任是：首 jet 公式在原正则 gauge 上使用正确、$R$ 与纯谱引理逐项一致、
  内在切向类覆盖完整原曲线，以及全素数／时间提升的准确量词。
  它们和两份新引理仍须合并非作者检查，不能由旧 p3 的 PASS 代签。
- 本件仅处理 $a=m=1$。$a>1$ 时首切向 $\pi$ 项可能已经消失；
  其更高局部理想尚未由 V1 给出。$m>1$ 的块内谱变形同样未在本件处理。
- 奇异能级、稳定约化、野导子、晶体比较、全迭代厚度及正式新意／容量保持未授予。
  不重投旧 C1–C3，不建项目、锁、稿件或 PDF，无外部效力。
