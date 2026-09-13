# qPI：特征二高层首 jet 的准确临界理想与首层类接口

日期：2026-09-09。作者：主控 `/root`。
类型：新的有界作者证明；`route_applicability: NOT_APPLICABLE`。
本件区分圆分高度一的特征四二阶商与高度至少二的特征二二阶商，不把它们识别。

## Claim

固定奇整数 $m\ge1$，有限完美剩余域 $k$ 的精确 $m$ 阶元 $\eta$。
令 $\mathcal O_0$ 为具有剩余域 $k$ 的无分歧二进 DVR，含其唯一 $m$ 阶提升 $\widetilde\eta$。
对 $a\ge2$，置
$$N=2^a,\qquad\mathcal O_a=\mathcal O_0[\zeta_N],\qquad
\pi_a=\zeta_N-1,\qquad s_a=\widetilde\eta\zeta_N.$$
允许完成和有限无分歧扩张，不附加有分歧基变换。
在参数 $s_a,t_a\in\mathcal O_a^\times$ 的原八截面开放曲面 $\mathcal U_a$ 上，保持原规范
$$\alpha_{mN}=2^{-a}d_{\rm state}I_{mN,s_a}.$$
设 $T=\bar t_a^m$、$J=I_{m,\eta}(x,y;\bar t_a)$，假设完整有限能级
$$X=(J=0)\subset U_0$$
光滑；按原几何输入它是完整几何整亏格一曲线。
$H_2(T,h)=h$，故这里正是光滑超奇异能级，不包括奇异能级。

**PI.1（高度二的准确截断理想）。** 对 $a=2$ 和任意 $P\in X$，
在实际局部环中任取 $J$ 的提升 $j$、$T$ 的常数单位提升 $\widetilde T$，则
$$\boxed{\mathfrak c(\alpha_{4m})_P+(\pi_2^2)
=(\pi_2^2,j^3+\pi_2\widetilde T,\pi_2j^2)_P.} \tag{PI1}$$
所有两个状态系数都保留，覆盖四条完整末端线。
它不是 $(\pi_2^2,j^3,\pi_2j^2)$：首生成元的实际混合项不能删除。

**PI.2（全部更高层）。** 对所有 $a\ge2$，在同样的局部点与原模型上，
$$\boxed{\mathfrak c(\alpha_{mN})_P+(\pi_a^2)
=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_aj^{N-2})_P.} \tag{PI2}$$
这里 $a=2$ 与 (PI1) 相同。普通光滑层的原系数理想为单位理想。

**PI.3（高度二完成商与无分歧状态）。** 在 $a=2$ 时，对闭点作所需的有限无分歧扩张后，
可取 $\bar z=J$ 和沿 $X$ 的参数 $w$，使
$$\frac{\widehat{\mathcal O}_{\mathcal U_2,P}}
{\mathfrak c(\alpha_{4m})+(\pi_2^2)}
\simeq \frac{k(P)[[w,z]]}{(z^5)},\qquad \pi_2\longmapsto z^3/T. \tag{PI3}$$
这是带所示底参数作用的同构；常数域按该无分歧扩张解释。
因此此截断商沿 $X$ 的横向长度为五；不称原完整临界商长度五。
沿任何约化到 $X$ 的无分歧状态提升，$\alpha_{4m}$ 两系数公共 $\pi_2$ 阶准确为一，
原 $dI_{4m}$ 的公共阶准确为五，因为 $v_{\pi_2}(4)=4$。
对 $a\ge3$，(PI2) 只给 $\alpha_{mN}$ 的公共阶至少二，不给准确首非零阶。

## Status 与依赖

**PROVABLE AS STATED（作者证明；新的代数件与本接口仍待非作者检查）。**
本件不将已接受首层结论作为高层理想的自动推论。
依赖如下，每个使用箭头在正文中给出：

1. [全 tame 首层 TH](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)
   与[接受处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md)：
   特征二、高度一的实际局部 $G_i$ 在 $X$ 给处处非零首切向类 $\nu$。
2. [prime trace 引理](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md)：
   在高度一给实际 $F(h)=-h^2-2t^m$ 与 $G=(I_{2m}-F(j_*))/(2\pi_1)$。
3. 新 [P2 块首 jet 引理](PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md)：
   给原环面 $\alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m$，
   以及完整模型 $\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}$。
   它本身不证明 $\chi_m$ 在 $X$ 的非零性；该责任由本件 Step 1–3 承担。
4. 已接受 G 的原开放模型光滑、原整除微分全局正则、同一剩余小阶曲面。

新 P2 作者件仍需全文非作者检查；本稿不能由旧奇素数 TB 报告代签。
本证明不调用旧有限 N9 数据或一般 $m$ 配对猜想，不把有限 p2 点算例当作全曲线证据。

## Notation 与策略

小写 $z_s$ 暂为谱变量，$Z$ 为共振投影后代替 $z_s^m$ 的变量；完成参数在 Step 5 再记为 $z$。
令 $d$ 固定时间、根单位、底环与谱变量，只对原两个状态求微分。
记
$$B_\eta(z_s)=A(\eta^{m-1}z_s)\cdots A(z_s),\qquad
S=\operatorname{tr}B_\eta=T+Jz_s^m+z_s^{2m},$$
$$K_0=[z_s^{2m}]\operatorname{tr}(dB_\eta\,z_s\partial_{z_s}B_\eta),
\qquad\chi_m=K_0+JdJ.$$
这是 P2 块引理所用的同一原矩阵一形式。
策略：在特征四的高度一商中准确识别 $\chi_m|_X=\nu$；
随后在特征二的高度二商中，利用局部 lift 变换及 $J^2$ 整除性，
将这一非零切向类接入整个完整曲面的双系数理想。

## Proof

### Step 1. 高度一的实际展开识别同一个切向类

另取高度一系数环 $\mathcal O_1=\mathcal O_0$，
$$\zeta_2=-1,\qquad\pi_1=-2,\qquad s_1=-\widetilde\eta.$$
任取单位时间提升 $t_1$ 使剩余时间等于 $\bar t_a$。
这里只比较剩余 $X$ 上的微分类，不将此高度一二阶商与高层商识别，也不要求时间的二阶 jet 匹配。
置 $B_s=A(s_1^{m-1}z_s)\cdots A(z_s)$，$S_s=\operatorname{tr}B_s$，$j_*=[z_s^m]S_s$。
因为 $m$ 奇，$s_1^m=-1$；原两块循环插入在整数环中给
$$\alpha_{2m}=[z_s^{2m}]\operatorname{tr}\bigl(dB_s(z_s)B_s(-z_s)\bigr). \tag{1}$$
归一化为 $\frac12dI_{2m}$，不是 $\frac1{2m}dI_{2m}$。

在 $\mathcal O_1/(\pi_1^2)$ 中，$-1=1+\pi_1$，逐单项式二项展开给
$$B_s(-z_s)=B_s(z_s)+\pi_1z_s\partial_{z_s}B_s(z_s). \tag{2}$$
这是特征四二阶商上的多项式等式，不先取模二。
对任何二阶矩阵，整系数恒等式
$$\operatorname{tr}(dM\,M)=(\operatorname{tr}M)d(\operatorname{tr}M)-d(\det M)$$
可由行列式的伴随矩阵公式直接证明，不需要在该商中除二。
原 $\det B_s=s_1^{3m(m-1)/2}z_s^{3m}$ 对状态为常数，故 (1) 的内部项为
$[z_s^{2m}]S_s\,dS_s$。

模 $\pi_1$ 后，循环迹只保留谱次数 $0,m,2m$，所以所有非共振系数在 $(\pi_1)$ 中。
其最高系数 $s_1^{m(m-1)}=1$ 在高度一准确成立。
共振三项式是 $t_1^m+j_*Z+Z^2$；求 $S_s\,dS_s$ 的共振系数时，
使用一个非共振因子的项仍非共振，使用两个的项带 $\pi_1^2$ 而消失。
因此该内部系数准确为 $j_*dj_*$。
在 (2) 的外部项中已乘 $\pi_1$，其余因子只需剩余值，故 (1) 给
$$\alpha_{2m}\equiv j_*dj_*+\pi_1K_0\pmod{\pi_1^2}. \tag{3}$$

另一方面，prime trace 的 $p=2$ 多项式准确为
$$F(h)=-[Z^2]\bigl((t_1^m+hZ+Z^2)^2-2d_sZ^3\bigr)
=-h^2-2t_1^m.$$
原 $G=(I_{2m}-F(j_*))/(2\pi_1)$ 在环面正则，且准确满足
$$\alpha_{2m}=-j_*dj_*+\pi_1dG. \tag{4}$$
比较 (3)、(4)，先在二阶商中保留 $2j_*dj_*=-\pi_1j_*dj_*$，
再用 $\pi_1\Omega/\pi_1^2\Omega\simeq\Omega\otimes k$，得到
$$d\bar G=K_0-JdJ=K_0+JdJ=\chi_m. \tag{5}$$
最后一个等号才使用剩余特征二。
由 TH 已接受的实际 OC 接口，$d(\bar G|_X)$ 在整个 $X$ 粘为处处非零的 $\nu$。
故 (5) 准确识别
$$\chi_m|_{\Omega_X}=\nu \tag{6}$$
于环面与 $X$ 的交上；其完整正则延拓与非零性来自该实际首层类。
没有假设 $\chi_m$ 本身在整个剩余曲面上正则。

### Step 2. 高度二的局部首系数与 lift 变换

现在回到高度二，记 $\epsilon=\pi_2\bmod\pi_2^2$、$B=\mathcal O_2/(\pi_2^2)$。
因 $v_{\pi_2}(2)=2$，$B$ 特征为二，且其系数域给 $B\simeq k[\epsilon]/\epsilon^2$。
原 $\mathcal U_B/B$ 光滑，微分模局部自由。
在覆盖 $X$ 的各原局部开集任选 $J$ 的正则提升 $j_i$。
原约化公式为 $\bar\alpha_{4m}=J^3dJ$，所以
$\alpha_{4m}^{[2]}-j_i^3dj_i$ 属于 $\epsilon\Omega^1_{\mathcal U_B/B}$。
利用此模与剩余微分模的自然同构，唯一地定义正则剩余一形式
$$\beta_i=\frac{\alpha_{4m}^{[2]}-j_i^3dj_i}{\epsilon}\bmod\epsilon. \tag{7}$$
商在 $B$ 中的提升不唯一，但其剩余值唯一；这是局部自由模的准确核／像关系。

若 $j_j=j_i+\epsilon f$，在特征二双数环中准确展开
$$(j_i+\epsilon f)^3d(j_i+\epsilon f)
=j_i^3dj_i+\epsilon(j_i^2 f\,dj_i+j_i^3df).$$
因此
$$\beta_j-\beta_i=-J^2\bar f\,dJ-J^3d\bar f. \tag{8}$$
这给需要的完整两方向变化，不仅比较切向商。

### Step 3. J² 整除从原环面延到每个完整点

P2 块引理在原环面给
$$\alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m.$$
结合 (8)，在每个局部开集与环面的交上，$\beta_i-TdJ$ 被 $J^2$ 整除，
其商与 $\chi_m$ 相差 $\bar f\,dJ+Jd\bar f$ 型的项。

现在固定任一 $P\in X$。$X$ 是光滑几何整概形纤维，故 $J$ 在
$R_P=\mathcal O_{U_0,P}$ 中是定义约化素 Cartier 除子的元素，且 $dJ$ 非零。
$X$ 的泛点在原环面：若它在补集四条末端线上，则整条完整亏格一曲线会包含于其中一条仿射直线，
与原完整几何整曲线的性质矛盾。
所以 $\beta_i-TdJ$ 在该素除子泛点被 $J^2$ 整除。

逐个局部自由系数，设 $b\in R_P$ 在 $(R_P)_{(J)}$ 属于 $J^2(R_P)_{(J)}$。
存在 $u\notin(J)$ 及 $g\in R_P$ 使 $ub=J^2g$。
因 $(J)$ 是素理想，先得 $b=Jb_1$，在整环中约去 $J$ 后再用同一素理想得 $b_1\in(J)$。
因此 $b\in J^2R_P$。这直接证明需要的整除性，不靠只在一个有限点验证。
于是
$$\rho_i=(\beta_i-TdJ)/J^2 \tag{9}$$
在每个 $P$ 附近为正则一形式。
在环面上，$\rho_i$ 的切向限制按 (6)、(8) 等于 $\nu$。
两者现在都在完整 $X$ 正则，故在整曲线的每点相等；于是 $\rho_i$ 的切向系数处处为单位。
四条末端线不需要另作有利点选择或假设一个全局 $j_*$ 提升。

### Step 4. 两方向理想消元与全部高层

在 $P$ 的 $B$-局部微分模中，将 $dj_i$ 补为基 $(dj_i,\theta)$。
从 (7)、(9)，可取 $\rho_i$ 的一个提升使
$$\alpha_{4m}^{[2]}=(j_i^3+\epsilon\widetilde T)dj_i+
\epsilon j_i^2(A_i\,dj_i+B_i\theta),$$
其中 $B_i$ 在 $P$ 为单位，因其切向剩余正是 $\nu$。
所以系数理想准确等于
$$ (j_i^3+\epsilon\widetilde T+\epsilon j_i^2A_i,\epsilon j_i^2B_i)
=(j_i^3+\epsilon\widetilde T,\epsilon j_i^2). \tag{10}$$
取 $\mathcal O_2\to B$ 的局部满射原像，即得 (PI1)。
若改变 $j_i$ 的提升，立方只增加 $\epsilon J^2f$，已在第二生成元中；
改变 $T$ 的提升只改变 $\epsilon^2$ 项。所以 (PI1) 的任意提升量词正确。

对 $a\ge2$，P2 块引理将高度二和第 $a$ 层的二阶商按相同参数 $\pi_2\mapsto\pi_a$、相同时间 jet 识别，
并在同一原完整模型给
$$\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}.$$
当 $a>2$，$N-4$ 是二的正倍数，所以乘数幂与 $J$ 的局部提升无关；$a=2$ 时为一。
对任何标量 $g$ 都有 $\mathfrak c(g\omega)=g\mathfrak c(\omega)$，无须 $g$ 为单位。
将 (10) 两个生成元同时乘 $j_i^{N-4}$ 后取原像，得到 (PI2)。
其任意提升量词也可直接检查：$j^{N-1}$ 的改变是 $\epsilon J^{N-2}f$，已由另一生成元包含，
而 $\epsilon j^{N-4}$ 的改变为零。
普通光滑层由原约化 $\bar\alpha_{mN}=J^{N-1}dJ$ 得单位系数。

### Step 5. 完成商、横向长度及状态阶

高度二在闭点按需作有限无分歧扩张后，原相对光滑完成局部环的模 $\pi_2^2$ 可写为
$$k(P)[[w,z,\epsilon]]/(\epsilon^2),\qquad \bar z=J.$$
因为 $dJ$ 非零，$z$ 可选为上述 $j_i$ 的提升，另取 $w$ 为沿曲线的参数。
$\epsilon\widetilde T=\epsilon T$，故 (10) 给商环
$$k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2).$$
$T\ne0$，第二关系允许消去 $\epsilon=z^3/T$。
第三关系成为 $z^5=0$，第一关系成为 $z^6=0$，后者已被前者包含。
这给 (PI3)，并证明作为 $k(P)[[w]]$-模的基为 $1,z,z^2,z^3,z^4$。
这里只计算已加 $(\pi_2^2)$ 后的商；没有删除原临界理想尚未知的更高厚度。

沿任何无分歧状态提升，$j$ 的评价在 $(\pi_2)$ 中。
因此 $j^3+\pi_2\widetilde T$ 的评价准确阶为一，而 $\pi_2j^2$ 的评价阶至少三。
已知原理想加 $(\pi_2^2)$ 的像为 $(\pi_2)$，迫使原系数理想自身的像也有准确一阶，
否则加 $(\pi_2^2)$ 仍不可能产生一阶元素。
故 $\alpha_{4m}$ 公共阶准确一，乘回四后准确五。

当 $a\ge3$，$N\ge8$，(PI2) 的两个非 $\pi_a^2$ 生成元沿该状态的阶均至少二，
只给原系数理想包含于 $(\pi_a^2)$。不能由此推出准确二。
乘回 $2^a$ 后的对应下界为 $a2^{a-1}+2$；普通层准确 $a2^{a-1}$。证毕。

## Corrections or Missing Assumptions

- Step 1 必须在特征四保留 $2j_*dj_*=-\pi_1j_*dj_*$；若提前置二为零，会漏掉 $JdJ$。
- (7) 只通过局部自由模给唯一剩余商，不声称双数环内数值除 $\epsilon$ 唯一。
- (9) 的整除需要 $X$ 是光滑整概形纤维、$J$ 为素 Cartier 参数；不能只取重数纤维的光滑支撑。
- 首层和高层相同的是剩余 $X$ 与已识别微分类，不是两个不同特征的二阶商。
- (PI3) 和长度五只属于截断临界商；本件不声称完整临界理想或全形式正规形。

## Open Risks 与交付边界

新 P2 块作者件和本件全部新接口仍待按最终实际字节独审。
本件不提供一般 $a\ge3$ 的准确状态阶、不解决全厚度或奇异能级；
不重新评判旧正式失败，也不据完整公式的数量授予新意或自然长文容量。
采用 proof-writer 分离具体断言、实际依赖、整数计算与全曲面延拓。
仅新增本文件；没有新脚本、GPU、稿件、锁、PDF、投稿、上传或其他外部效力。
