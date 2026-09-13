# Paper30 qPI：特征二块首 jet 与高层截断理想合并独立核查 V1

日期：2026-09-09。类型：两份冻结作者件的有界非作者数学检查。
唯一新增产物为本报告；没有修改作者件、旧检查、索引或锁。

## Claim

第一部分核查 P2 块引理的完整原量词。
取奇整数 $m\ge1$、完美特征二剩余域 $k$、无分歧二进 DVR $\mathcal O_0$，
含精确 $m$ 阶单位根 $\widetilde\eta$，剩余为 $\eta$。
对 $a\ge2$，令
$$N=2^a,\qquad \mathcal O_a=\mathcal O_0[\zeta_N],\qquad
\pi_a=\zeta_N-1,\qquad s_a=\widetilde\eta\zeta_N,\qquad t_a\in\mathcal O_a^\times.$$
保持原八截面模型、原谱乘积及原状态微分规范
$$\alpha_{mN}=N^{-1}d_{\rm state}I_{mN,s_a}.$$
将高度二和高度 $a$ 的二阶商按相同参数及相同时间 jet 识别为
$$B=k[\epsilon]/(\epsilon^2),\qquad \pi_2,\pi_a\mapsto\epsilon,$$
所得共同模型记为 $\mathcal U_B$。
在原环面定义
$$\mathsf B_s(z_s)=A(s^{m-1}z_s;t)\cdots A(z_s;t),\quad
s=\eta(1+\epsilon),\quad j_*=[z_s^m]\operatorname{tr}\mathsf B_s,$$
$$\mathsf B_0=\mathsf B_\eta(z_s;\bar t),\quad
T=\bar t^m,\quad J=I_{m,\eta}(x,y;\bar t),\quad S(Z)=T+JZ+Z^2,$$
$$\chi_m=J\,dJ+[z_s^{2m}]
\operatorname{tr}(d\mathsf B_0\,z_s\partial_{z_s}\mathsf B_0).$$
核查并接受 P2.1、P2.2：
$$\alpha_{mN}^{[2]}=j_*^{N-1}dj_*+\epsilon\beta_N,\qquad
\beta_N=J^{N-4}\beta_4,\qquad \beta_4=T\,dJ+J^2\chi_m,$$
以及原完整模型上的
$$\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}.$$
非零偶数幂的角括号表示任意局部提升的共同幂；零次幂为一。
这部分不假设光滑能级或 $J\ne0$，但不单独断言 $\chi_m$ 全图正则或切向非零。

第二部分按 PI 作者件的有限剩余域、原模型及允许的完成／无分歧范围，
另假设完整概形纤维 $X=(J=0)$ 光滑，因原几何输入它是完整几何整亏格一曲线。
对 $P\in X$，任意实际局部提升 $j$ 及常数单位提升 $\widetilde T$，接受 PI.1、PI.2：
$$\mathfrak c(\alpha_{4m})_P+(\pi_2^2)
=(\pi_2^2,j^3+\pi_2\widetilde T,\pi_2j^2)_P,$$
$$\mathfrak c(\alpha_{mN})_P+(\pi_a^2)
=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_aj^{N-2})_P.$$
在普通光滑能级，原系数理想为单位理想。
对高度二的闭点，按需无分歧扩张并完成后，接受 PI.3 的带底参数作用的同构
$$\widehat{\mathcal O}_{\mathcal U_2,P}/
\bigl(\mathfrak c(\alpha_{4m})+(\pi_2^2)\bigr)
\cong k(P)[[w,z]]/(z^5),\qquad \pi_2\mapsto z^3/T.$$
横向长度五只属于此截断商。
沿无分歧光滑超奇异状态提升，$a=2$ 时 $\alpha_{4m}$ 的公共阶准确为一、
$dI_{4m}$ 准确为五；$a\ge3$ 时只接受前者至少二阶及其对应的后者下界。

## Status

**PROVABLE AS STATED / PASS。**

两份新作者件的原结论均无需改弱，未发现硬缺口。
接受是以下全称证明和实际输入接口的合取，不是由作者自评、主控实读或有限点测试代签。
所有高层一形式比较及临界理想结论均严格限于已声明的模 $\pi_a^2$ 范围。

核查者非两份新作者，但此前已知特征二方向，
并在 PI 作者件冻结前给过一次仅消息的有界诊断；因此本轮不是盲审或 fresh-eyes 审查。
本轮重新全文读取两份冻结字节，没有用此前消息替代实际文件阅读。
proof-writer 用于组织 Claim、输入、全称证明、测试和边界；不承担新意、Route 评分或论文验收。

## Assumptions and Read Identity

本轮新作者输入：

| 文件 | 实际全文范围 | SHA-256 |
|---|---:|---|
| [P2_HIGHER_IDEAL_PROOF_V1](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md) | 1–227 行；13,625 字节 | 1d2ff70c69cb26ec2009055f3161cb44758338db8912b9654ab8c53b5d7c59d3 |
| [P2_BLOCK_FIRST_JET_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | 1–334 行；19,638 字节 | c5fc4192822733993f361363f194832aee872ab25ce598c39e76be3b1ae62897 |

紧邻的有界诊断已实际读取下列上游正文，本轮确认同哈希，仅消费已接受接口，不重开旧审查：

- [全 tame 首层 TH](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)：
  全文 1–219 行；实际 $G_i$、完整 $X$ 上的 $\nu$ 与处处非零结论。
  SHA-256：43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75。
- [OC 引理](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md)：
  全文 1–177 行；TH 已核准前提后的实际切向类与 Čech—Cartier 接口。
  SHA-256：81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa。
- [prime trace 引理](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md)：
  实读 9–70、158–230 行；原 $p=2$ 的 $F$、整数同余、Taylor 商及符号。
  SHA-256：07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9。

本轮继续消费此前已亲读且同身份的原几何／矩阵接口：

| 输入 | 已实读并用于本轮的段 | SHA-256 |
|---|---|---|
| [整数 brief](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 32–85、123–192 行中的原矩阵、八中心及整除微分规范 | 59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13 |
| [原整除诊断 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 8–53、101–193 行中的循环插入、迹及行列式、秩二递推 | e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652 |
| [原完整模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 7–63、83–149、222–234 行中的四图、正则函数与整除一形式延拓 | 59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0 |

不读取其他新独立检查或处置意见来取得本轮结论；未重开同哈希已接受阶段。
不以旧奇素数 TB、有限 N9 数据或一般 $m$ 的单位配对猜想证明特征二。
块引理允许完美 $k$ 的较广范围，其代数和系数域论证不需要 $k$ 有限；
PI 的几何结论则保留自身较窄的输入范围，不静默扩大。

## Notation and Proof Strategy

$z_s$ 为谱变量，$Z$ 是共振投影后对应 $z_s^m$ 的形式变量；
完成后的横向参数另记为 $z$。
状态微分固定时间、根单位、谱变量和底环。
原环面微分模为 $R\,dx\oplus R\,dy$，只出现一个一形式值矩阵，不对一形式取 Frobenius 幂。
记
$$\mathcal P_m\left(\sum c_i z_s^i\right)=\sum c_{mj}Z^j,\qquad
[M,X]=MX-XM.$$
投影仅满足
$$\mathcal P_m(Q(z_s^m)P(z_s))=Q(Z)\mathcal P_m(P(z_s)),$$
不把它当作一般乘法同态。

依赖链分成三段：

1. 新块代数：整数插入、全部块内变化、特征二递推和交换子、实际支持界、四块基准及全端分解。
2. 新几何桥：首层特征四中的 $\chi_m$ 识别、局部 $\beta_i$、泛点 $J^2$ 整除与 TH 的完整切向类。
3. 新局部代数：实际两生成元消元、全部高层截断理想、完成商和无分歧状态阶。

## Proof

### Step 1. 原规范、二阶商与实际块归一化

作者缩写 $b=x(y-1)$、$c=y-1$、$\mathcal J(t)=y-x+x/y-t/x$ 后的矩阵
逐项恢复 brief 的原矩阵；没有状态依赖共轭或新增独立的 $q$ 系数依赖。
保留原整数身份
$$\det A(z_s)=z_s^3,\qquad \operatorname{tr}A(0)=t,\qquad
\det A(0)=0,\qquad [z_s^2]A=E=\operatorname{diag}(1,0),\qquad dE=0.$$

$\Phi_{2^a}(1+X)=(1+X)^{2^{a-1}}+1$ 对二为 Eisenstein，
所以 $v_{\pi_a}(2)=2^{a-1}\ge2$。
$\mathcal O_0$ 的像经 $\mathcal O_0/(2)=k$ 嵌入二阶商，给系数域；
商长为二，每个元素唯一写成 $c_0+c_1\pi_a$。
因此高度二与高度 $a$ 的共同双数商成立，且不要求有限剩余域。
时间匹配由商映射满射保证。
自然嵌入 $i\mapsto\zeta_{2^a}^{2^{a-2}}$ 在 $a>2$ 时将 $\pi_2$ 送到零，
而不是共同的一阶参数；作者明确没有使用这一错误识别。

在特征零令 $r=s_a^m$。原第 $j$ 块的原因子指数是
$mj+m-1,\ldots,mj$，因此原 $mN$ 因子准确按降序分成 $N$ 块。
状态微分的第 $j$ 块经循环迹及 $w=r^jz_s$ 移到指定插入位置；
$r^N=1$ 保持循环次序，目标系数的缩放因子 $r^{jmN}=1$。
于是整系数一形式中已有
$$dI_{mN}=N[z_s^{mN}]
\operatorname{tr}\left(d\mathsf B_{s_a}(z_s)
\mathsf B_{s_a}(r^{N-1}z_s)\cdots\mathsf B_{s_a}(rz_s)\right).$$
先除 $N$ 后的右端仍整，随后才可约化。
$d\mathsf B_s$ 含全部 $m$ 个块内插入，不能再乘或除 $m$。
单原因子版本是 $m$ 倍的插入系数；独立特征零测试也核对了二者与完整微分除 $N$ 相等。

### Step 2. 实际块内谱变化与时间完整保留

在 $R=B[x^{\pm1},y^{\pm1}]$ 中保持实际时间 $t$。
逐因子展开给
$$\mathsf B_s=\mathsf B_\eta(z_s;t)+\epsilon\mathsf C,\qquad
\mathsf C=\sum_{j=0}^{m-1}j\,\mathsf A_{m-1}\cdots\mathsf A_{j+1}
(z_s\partial_{z_s}\mathsf A_j)\mathsf A_{j-1}\cdots\mathsf A_0.$$
$\mathsf A_j=A(\eta^jz_s;t)$；$\mathsf C$ 只需剩余值，而实际时间不被换成剩余时间。
循环迹与 $\eta$ 的精确阶在非约化环上仍给
$$\operatorname{tr}\mathsf B_\eta=t^m+j^\circ z_s^m+z_s^{2m}.$$
非共振次数的 $\eta^i-1$ 是单位，首尾系数由原 $A(0)$ 和 $E$ 的幂给出。
故可写
$$S_s=\operatorname{tr}\mathsf B_s
=S_*(z_s^m)+\epsilon V,\qquad
S_*(Z)=t^m+j_*Z+Z^2,\qquad \mathcal P_mV=0.$$
这里最高系数 $s^{m(m-1)}=1$ 是高层双数商中的等式，
不是对原特征零圆分环作相同断言。
实际行列式仍是 $s^{3m(m-1)/2}z_s^{3m}$，其标量首 jet 可能非零，
但状态导数始终为零。作者没有把这一点误当成行列式本身无变形。

### Step 3. 特征二内部项

整系数递推
$$U_{-1}=0,\quad U_0=1,\quad U_n=SU_{n-1}-DU_{n-2}$$
和 Cayley–Hamilton 给
$$\operatorname{tr}(dM\,M^{N-1})
=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD.$$
在通用对称变量中，特征二且 $N=2^a$ 给
$$U_{N-1}(u+v,uv)=\frac{u^N-v^N}{u-v}=(u+v)^{N-1}.$$
商表示多项式，再由对称多项式环单射下降；
不需要实际矩阵可对角化、迹非零或谱可分。
由 $dD_s=0$，内部项成为 $[z_s^{mN}]S_s^{N-1}dS_s$。

平方零展开只留下两个潜在误差
$$\epsilon(N-1)S_*^{N-2}V\,dS_*+
\epsilon S_*^{N-1}dV.$$
其余因子只含 $m$ 倍谱次数，且 $\mathcal P_mV=\mathcal P_m(dV)=0$，
故合法投影后两项消失；两个非共振误差相乘则因 $\epsilon^2=0$ 消失。
于是
$$F_N=[Z^{N-1}]S_*^{N-1}\,dj_*.$$
将 $S_*^{N-1}$ 写成 $\prod_{i=0}^{a-1}S_*^{2^i}$，
每位原次数在 $\{0,1,2\}$ 中。目标 $2^a-1$ 的最低位为奇数，只能选一；
逐次减一、除二，所有位都选一。
因此
$$F_N=j_*^{N-1}dj_*.$$
实际时间对 $j_*$ 及 $dj_*$ 的全部一阶影响仍保留。

### Step 4. 特征二加权交换子和外部项

对任意交换特征二系数环上的二阶矩阵，
$$\operatorname{ad}_M^2(X)=M^2X+XM^2
=(\operatorname{tr}M)[M,X].$$
标量几何级数的形式导数给
$$\sum_{j=1}^{N-1}jU^{N-1-j}V^{j-1}=(U+V)^{N-2}.$$
代入可交换的左右乘算子后，对 $N\ge4$ 得
$$\sum_{j=1}^{N-1}jM^{N-1-j}XM^{j-1}
=(\operatorname{tr}M)^{N-3}[M,X].$$
这没有除以迹；迹为零时仍成立。
$N=2$ 的左端是 $X$，不能使用负幂写法，因此以四块为基准是必要的。

因为 $m$ 奇，外部速度 $m$ 在双数商中为一：
$$r=s^m=1+\epsilon,\qquad
\mathsf B_s(r^jz_s)=\mathsf B_s(z_s)
+\epsilon j\,z_s\partial_{z_s}\mathsf B_0.$$
展开原降序插入积，外部项已带 $\epsilon$，其余因子只取剩余值。
于是
$$\alpha_{mN}^{[2]}=F_N+\epsilon\beta_N,\qquad
\beta_N=[Z^N]\gamma_m(Z)S(Z)^{N-3},$$
$$\Gamma_m=\operatorname{tr}\left(d\mathsf B_0
[\mathsf B_0,z_s\partial_{z_s}\mathsf B_0]\right),\qquad
\gamma_m=\mathcal P_m\Gamma_m.$$
外部速度为一与整数归一化中不再乘 $m$ 是两个不同理由，作者已正确区分。

### Step 5. 实际支持界、二进制选择与四块基准

剩余块最高系数为 $E$，故 $\deg d\mathsf B_0\le2m-1$。
特征二还使 $z_s\partial_{z_s}(z_s^{2m}E)=0$，所以谱导数次数也至多 $2m-1$。
因此
$$\operatorname{supp}\Gamma_m\subset[1,6m-2],\qquad
\operatorname{supp}\gamma_m\subset[1,5],$$
其中 $m=1$ 的后一界可改为四。
$\gamma_mS$ 的支持在 $[1,7]$。
在
$$\gamma_mS^{N-3}=(\gamma_mS)\prod_{i=2}^{a-1}S^{2^i}$$
中，第一因子要贡献目标 $2^a$，其次数必须是四的倍数，唯一候选是四。
剩余目标经减四、除四后为 $2^{a-2}-1$，后续各位仍只能选一。
故
$$\beta_N=J^{4+8+\cdots+2^{a-1}}\beta_4=J^{N-4}\beta_4.$$
$a=2$ 的空积给恒等边界；该论证保留标量系数的 Frobenius。

独立检查四块系数时，令 $M=\mathsf B_0$、$R_z=z_s\partial_{z_s}M$、
$\mathcal S=\operatorname{tr}M$、$\mathcal D=\det M=z_s^{3m}$。
对 Cayley–Hamilton 求状态微分，并使用实际 $d\mathcal D=0$，可得
$$M\,dM+dM\,M=(d\mathcal S)M+\mathcal S\,dM.$$
乘 $R_z$ 取迹，再用行列式谱微分，得到
$$\Gamma_m=(z_s\partial_{z_s}\mathcal D)d\mathcal S+\mathcal S K_m,$$
$$K_m=d\mathcal S(z_s\partial_{z_s}\mathcal S)
+\operatorname{tr}(dM\,R_z).$$
若行列式有状态变化，另有 $d\mathcal D\,(z_s\partial_{z_s}\mathcal S)$ 项；
作者的省略仅因原矩阵满足 $d\mathcal D=0$，不是无条件矩阵公式。

$m$、$3m$ 均为奇数，故
$$d\mathcal S=z_s^m dJ,\quad z_s\partial_{z_s}\mathcal S=Jz_s^m,\quad
z_s\partial_{z_s}\mathcal D=z_s^{3m}.$$
于是
$$\Gamma_m=z_s^{4m}dJ+S(z_s^m)K_m,\qquad
[Z^2]\mathcal P_mK_m=\chi_m.$$
$K_m$ 没有常数项，次数至多 $4m-2$，故 $\kappa_m=\mathcal P_mK_m$ 支持至多为一至三。
因为 $S^2=T^2+J^2Z^2+Z^4$，读取
$$[Z^4](\gamma_mS)=[Z^4](Z^4S\,dJ+S^2\kappa_m)$$
准确给出 $\beta_4=T\,dJ+J^2\chi_m$。
$m=1$ 时原 $A_1$ 直接给 $\operatorname{tr}(dA_1A_1)=JdJ+d[x(y-1)]$，
从而 $\chi_1=d[x(y-1)]$；该式本身不替代全曲线单位性。

### Step 6. 块因子分解的完整模型责任

$N-4>0$ 为偶数；任意两个局部提升相差 $\epsilon f$，其平方、从而 $(N-4)$ 次幂相同。
这些幂粘成全局正则函数，无需 $J$ 的全局整提升。
环面上的内部和外部式因此给
$$\alpha_{mN}^{[2]}
=j_*^{N-4}\bigl(j_*^3dj_*+\epsilon\beta_4\bigr).$$
两层时间的完整二阶像相同，故这是同一个原环面系数环中的比较。

原八中心使用四个不同边界分量的单位坐标 $1,t,t,s$。
它们及标准吹起次序在共同商中相同，逐图给同一 $\mathcal U_B$；
未援引任意非平坦基变换与吹起可交换的通则。
原 G 的整除一形式全局正则性提供比较两边的正则截面。
四个末端图是 $B[u,v]$ 关于 $1+uv,t+uv,t+uv,s+uv$ 的相应局部化，
环面交再反演 $u$。
乘 $u$ 在这些环及自由微分模中均单射，即使 $B$ 非约化也成立。
环面上为零的差遂在四图上为零，证明 P2.2。
这一延拓不假设 $\chi_m$ 或 $\beta_4$ 单独全图正则。

### Step 7. 特征四首层准确识别 $\chi_m$

取 $\pi_1=-2$、$s_1=-\widetilde\eta$，任选与高层剩余时间相同的首层单位时间。
这里不匹配两种二阶厚化，只比较共同的剩余曲面。
首层两块归一化准确为
$$\alpha_{2m}=[z_s^{2m}]\operatorname{tr}(d\mathsf B_s(z_s)\mathsf B_s(-z_s)).$$
在特征四商中，单项式系数满足 $(-1)^n-1\equiv-2n$，故
$$\mathsf B_s(-z_s)=\mathsf B_s(z_s)+\pi_1z_s\partial_{z_s}\mathsf B_s(z_s).$$
整系数公式 $\operatorname{tr}(dM\,M)=S\,dS-dD$ 不需要除二。
$dD_s=0$；块迹的非共振系数在 $(\pi_1)$，
其共振主项为 $t_1^m+j_*Z+Z^2$，其中此处最高系数一在首层特征零环中准确成立。
单个非共振误差不能贡献目标次数，两个误差的乘积被 $\pi_1^2$ 消去。
故
$$\alpha_{2m}\equiv j_*dj_*+\pi_1K_0\pmod{\pi_1^2},\qquad
K_0=[z_s^{2m}]\operatorname{tr}(d\mathsf B_0\,z_s\partial_{z_s}\mathsf B_0).$$

实际 prime trace 给 $F(h)=-h^2-2t_1^m$ 及正则
$G=(I_{2m}-F(j_*))/(2\pi_1)$，所以
$$\alpha_{2m}=-j_*dj_*+\pi_1dG.$$
比较时必须保留 $2j_*dj_*=-\pi_1j_*dj_*$，
经 $\pi_1\Omega/\pi_1^2\Omega\simeq\Omega\otimes k$ 得
$$d\bar G=K_0-JdJ=K_0+JdJ=\chi_m.$$
最后才使用特征二。
TH／OC 已接受的实际类于是给 $\chi_m$ 在 $X$ 环面交上的切向限制等于 $\nu$，
而 $\nu$ 在完整 $X$ 上正则且处处非零。
这不是只识别到未知标量，也不要求环境 $\chi_m$ 已跨端正则。

### Step 8. 局部 $\beta_i$、坐标变换及 $J^2$ 的全点整除

高度二的 $\Omega^1_{\mathcal U_B/B}$ 局部自由且 $B$-平坦，
所以乘 $\epsilon$ 给自然同构
$$\Omega^1_{U_0/k}\simeq\epsilon\Omega^1_{\mathcal U_B/B}.$$
由原全局约化 $\bar\alpha_{4m}=J^3dJ$，
对任意局部提升 $j_i$ 可唯一地定义正则剩余形式
$$\beta_i=(\alpha_{4m}^{[2]}-j_i^3dj_i)/\epsilon\bmod\epsilon.$$
只有剩余商唯一，不是在双数环中选择唯一数值除法。
在 $j_j=j_i+\epsilon f$ 下，直接展开给
$$\beta_j-\beta_i=-J^2\bar f\,dJ-J^3d\bar f.$$
这是内蕴差的变换；原图中 $q,t$ 依赖的坐标转换已包含在原一形式及 $dj_i$ 中，
不额外产生未计的一阶矩阵项。

环面特殊提升 $j_*$ 给 $\beta_*=T\,dJ+J^2\chi_m$；
故任意 $j_i$ 在环面交上仍满足 $J^2\mid(\beta_i-TdJ)$。
$X$ 的泛点属于环面：若完整整曲线包含于补集某条末端仿射线，
便与其完整亏格一性质矛盾。
在 $R_P=\mathcal O_{U_0,P}$ 中，$J$ 为素 Cartier 参数，因为 $X$ 是光滑整概形纤维，
而不是仅有光滑支撑的重数纤维。
对任一自由系数 $b$，泛点整除给
$$ub=J^2g,\qquad u\notin(J).$$
素性先给 $b=Jb_1$；在整环中约去 $J$ 后再用素性，得 $b_1\in(J)$。
所以 $b\in J^2R_P$，无需把 $u$ 当作 $P$ 处的单位，也无需额外 UFD 假设。

因此 $\rho_i=(\beta_i-TdJ)/J^2$ 在所有点附近正则。
其切向限制不因提升改变，因为商的改变量为
$-\bar f\,dJ-Jd\bar f$，在 $X$ 的切向商中为零。
在环面交上它等于 $\nu$；两者均已在完整整曲线上正则，故逐点相等。
TH 的处处非零性由此给每个点的切向单位，包括全部末端点。

### Step 9. 两方向实际消元、任意提升和全部高层

将 $dj_i$ 补成实际局部余切基 $(dj_i,\theta)$。
选 $\rho_i$ 的提升并写为 $A_i\,dj_i+B_i\theta$，其中 $B_i$ 为单位。
于是双数商中
$$\alpha_{4m}^{[2]}
=(j_i^3+\epsilon\widetilde T+\epsilon j_i^2A_i)dj_i
+\epsilon j_i^2B_i\theta,$$
故系数理想准确为
$$(j_i^3+\epsilon\widetilde T,\epsilon j_i^2).$$
取实际局部环的满射原像得到 PI.1。
改变 $j_i$ 的立方只添加 $\epsilon J^2f$，已被第二生成元吸收；
改变 $\widetilde T$ 只影响 $\epsilon^2$ 项。
因此任意提升量词成立，且混合项 $\pi_2\widetilde T$ 不能删去。

对任意标量 $g$，即使它是零因子，也有 $\mathfrak c(g\omega)=g\mathfrak c(\omega)$。
应用 P2.2，将两个生成元同时乘 $j_i^{N-4}$，再取原像，准确得到 PI.2。
这是二阶商中整个理想的乘法，不是只比较其零点或某个状态方向。
任意提升下 $j^{N-1}$ 的变化为 $\epsilon J^{N-2}f$，同样由第二生成元吸收；
$\epsilon j^{N-4}$ 的变化为零。
普通光滑层的 $J$ 非零且 $dJ$ 为非零法向，
原约化 $J^{N-1}dJ$ 因而有单位系数。

### Step 10. 完成商与状态赋值的准确边界

在高度二闭点，无分歧处理剩余域并完成后，模 $\pi_2^2$ 的环是
$$k(P)[[w,z,\epsilon]]/(\epsilon^2),$$
可令 $z=j_i$，因为 $dJ$ 非零；$w$ 沿 $X$。
PI.1 的商为
$$k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2).$$
$T$ 是单位，消去 $\epsilon=z^3/T$ 后，关系分别给 $z^6=0,z^5=0$，
前者已由后者包含。
因此 PI.3 的同构及底参数作用正确；
作为 $k(P)[[w]]$-模的五个基元为 $1,z,z^2,z^3,z^4$。
这是横向长度五，不是闭点商的总 Artin 长度，也不是原完整临界商的长度。

沿无分歧状态提升，$j$ 的值在 $(\pi_2)$ 中，
所以 $j^3+\pi_2\widetilde T$ 准确一阶，$\pi_2j^2$ 至少三阶。
原系数理想的像加 $(\pi_2^2)$ 既为 $(\pi_2)$，原像理想自身不可能只有二阶或更高；
故 $\alpha_{4m}$ 准确一阶。乘回四，因 $v_{\pi_2}(4)=4$，$dI_{4m}$ 准确五阶。
当 $a\ge3$，沿同类状态，PI.2 只保证原系数理想的评价像包含于 $(\pi_a^2)$；
不是说整个曲面上的原系数理想包含于该理想。
对应 $dI_{mN}$ 的下界为 $a2^{a-1}+2$；普通光滑层准确为 $a2^{a-1}$。
未推断高层准确首非零阶。两份原 Claim 证毕。

## Actual Independent Verification

所有下列检查均为本轮实际执行的内存代码，未调用作者测试实现，
未创建第二脚本或数据文件，全部退出码为零。
有限排错不替代以上全称代数及 TH／OC 的完整曲线证明。

### A. 特征零四块归一化

在 $\mathbb Z[\eta,i]/(\eta^2+\eta+1,i^2+1)$ 中取
$m=3,N=4,s=\eta i,x=y=1,t=3$。
独立传播原 12 因子的值及两个状态导数，检查目标导数的全部标准整系数可被四整除，
并验证
$$\text{完整微分}/4
=3\times\text{单原因子插入}
=\text{完整三因子块插入}.$$
在基 $(1,\eta,i,\eta i)$ 中，两个规范化系数为
$$(-24066,-12231,405,-7047),\qquad (2688,3726,-1314,-3516).$$
这里没有在特征二中反除四；也避免了双数商中奇数 $m$ 的剩余为一而掩盖归一化错误。

### B. 全 Laurent 的特征四桥

另在
$$\mathbb Z[\eta,x^{\pm1},y^{\pm1},t]/(\eta^2+\eta+1)$$
中取 $m=3,s_1=-\eta$，保留不定状态和时间。
以独立整数稀疏 Laurent 运算计算完整 $B_s,B_\eta,j_*,I_6$，
直接检查 $I_6+j_*^2+2t^3$ 的全部系数可被四整除并形成
$$G=-(I_6+j_*^2+2t^3)/4.$$
两状态方向都准确满足
$$2\alpha_{6}=dI_6,\qquad
[z_s^6]S_s\,dS_s\equiv j_*dj_*\pmod4,$$
$$\alpha_6\equiv j_*dj_*-2K_0\pmod4,\qquad
dG\bmod2=K_0+JdJ.$$
$j_*,I_6,G$ 的标准 Laurent 表示分别有 24、106、98 项；
$\chi_3$ 的两个模二系数分别有 29、20 项。
这些是该 $m=3$ 子情形的全 Laurent 恒等式检查，不是有限点代替全曲线。
一般 $m$ 的桥仍由 Step 7 证明。

### C. 原矩阵双数完整计算

独立实现有限域和双数运算，保留实际时间一阶变化及 $\epsilon\,dx,\epsilon\,dy$，
分别形成原单因子插入、完整块插入、内部项、$\Gamma_m,K_m,\chi_m$ 和 $\beta_N$。
检查全部谱系数的 $\Gamma_m$ 恒等式、$\gamma_m/\kappa_m$ 支持界、
四块基准式、内部幂式和完整层比较。

有限域使用二进制幂基标签：标签整数的二进制位表示 $\theta$ 的系数，
不是将标签当作素域整数。所有 $\eta$ 均另验精确阶。

| $k$ 及定义多项式 | $(m,\eta,a)$ | $(t_0,t_{\rm lin},x,y)$ | $(J,T,J^{N-4})$ | 结果 |
|---|---|---|---|---|
| $\mathbb F_4$，$\theta^2+\theta+1$ | $(1,1,3)$ | $(1,2,1,1)$ | $(0,1,0)$ | PASS；另核 $\chi_1=d[x(y-1)]$ |
| 同上 | $(3,2,2)$ | $(2,1,1,3)$ | $(0,1,1)$ | PASS |
| 同上 | $(3,2,4)$ | $(1,3,3,2)$ | $(0,1,0)$ | PASS |
| $\mathbb F_8$，$\theta^3+\theta+1$ | $(7,2,3)$ | $(3,5,6,4)$ | $(4,1,2)$ | PASS |
| $\mathbb F_{16}$，$\theta^4+\theta+1$ | $(5,8,3)$ | $(7,9,5,11)$ | $(13,6,11)$ | PASS |
| 同上 | $(15,2,3)$ | $(11,6,7,13)$ | $(2,1,3)$ | PASS |

全部非平凡 tame 块的样本均出现非零块内非共振一阶项；
实际五次投影项也出现，未误用单矩阵四次界。
表中包含非素域乘数和 $J=0$ 情形；
没有据这些点推断光滑能级、全端单位或几何非消失。

### D. 普适符号式、数字与截断商

- 对完全独立的通用二阶矩阵 $M,X,R_z$，符号模二验证
  $\operatorname{ad}_M^2(X)=(\operatorname{tr}M)[M,X]$。
- 对通用矩阵及独立状态／谱方向，符号核得完整 $\Gamma$ 式，
  包括一般情况下的 $d(\det M)\,z_s\partial_{z_s}(\operatorname{tr}M)$ 附加项；
  确认作者只在实际 $dD=0$ 后删除它。
- 对 $a=2,\ldots,8$ 穷举内部数字 $\{0,1,2\}$ 与外部首位 $[1,7]$，
  唯一组合分别为全一及首位四、后续全一。
- 在 $\mathbb F_2(T)[\pi,z,w]$ 中作双向符号理想约化，验证
  $$(\pi^2,z^3+\pi T,\pi z^2)=(\pi+z^3/T,z^5).$$
  一般单位 $T$ 的完成环同构仍由 Step 10 的直接消元证明。

## Corrections or Missing Assumptions

无须修改两份冻结作者件。
PI 已明确加入完整光滑概形纤维、闭点剩余域、特征四／特征二区别、
唯一剩余除法以及 $a=2$ 准确阶／$a\ge3$ 下界等必要边界。
本报告进一步明确：高层状态阶的包含关系只指评价后的理想像，
不能误读为整个曲面的一形式已被 $\pi_a^2$ 整除。
这不改变作者原有“沿该状态”的范围。

## Open Risks and Explicit Nonclaims

- P2 块引理的全模型分解不单独提供 $\chi_m$ 的全图正则性或首切向单位；PI 通过实际 TH 类完成所需桥。
- PI 仅覆盖假定光滑的完整 $X=(J=0)$；不把光滑支撑代替约化光滑概形纤维。
- 所有高层临界理想等式均已加 $(\pi_a^2)$；不声称完整理想、完整初始理想或全形式正规形。
- 横向长度五只属于高度二截断商；不是原临界商总长度，也不声称对双数底平坦。
- $a\ge3$ 的准确状态首非零阶仍未确定；禁止由截断结果外推。
- 不扩大到非单位时间、偶 $m$ 或额外有分歧状态扩张。
- 未读取其他新评审结论、修改旧冻结输入、评分、立项、写稿、建锁、编译或进行任何外部发布。

## Artifact State

本轮唯一新增持久化产物为本报告，无 GPU、第二脚本或数据文件。
两份新作者件及所消费的同哈希上游身份在交付前再次核对。
报告最终行数、字节数、SHA-256 与输入未变状态在交接中列出。
终态：P2.1–P2.2 与 PI.1–PI.3 合并接受，无待修硬缺口；不承诺超出上述范围的结论。
