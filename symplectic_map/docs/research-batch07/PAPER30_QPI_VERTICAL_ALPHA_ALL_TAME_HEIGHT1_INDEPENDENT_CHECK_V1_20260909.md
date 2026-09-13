# Paper30 qPI：全部剩余阶首层垂直理想及 prime trace 的独立核查 V1

日期：2026-09-09。核查者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
类型：两个冻结作者件的非作者数学检查；不是新意、Route、长文容量或候选资格评价。
`route_applicability: NOT_APPLICABLE`。0 GPU。唯一新增文件为本报告。

## Claim Under Review

对任意素数 $p$、$m\geq1$、$p\nmid m$，固定实际圆分高度 $a=1$，
$\pi=\zeta_p-1$、$s=\widetilde\eta\zeta_p$ 及任意单位时间 $t$。
保留原矩阵、原降序乘积、原积分 $I_{mp}$、原八截面模型，以及原小阶积分 $J=I_{m,\eta}$。
以下 $R=\mathcal O[x^{\pm1},y^{\pm1}]$，$T=\bar t^m$，$\varepsilon_m=(-1)^{m+1}$，
$H=H_p(T,J;\varepsilon_m)$；$\lambda=1$（奇 $p$）或 $-1$（$p=2$）。
$H_p$ 保留目标稿的 Hasse 多项式定义，奇 $p$ 为所给四次式的系数，$H_2(T,h;\varepsilon_m)=h$。
本次完整核查以下两段：

1. **Prime trace：** 作者定义的整数多项式 $F$ 满足
   $$I_{mp}-F(j_t)\in p\pi R,\qquad F(h)=\lambda h^p+pQ(h),$$
   $$\overline{F'(h)/p}=H_p(T,h;\varepsilon_m),\qquad
   \overline{\frac{F(a+\pi f)-F(a)}{p\pi}}
   =H_p(T,\bar a;\varepsilon_m)\bar f-\bar f^p.$$
2. **实际首层结论 TH1–TH4：** 每个完整光滑有限几何能级 $X=(J=h)$ 的实际提升障碍
   $$\kappa_J\ne0\quad\text{in }H^1(X,\mathcal O_X)$$
   被准确识别；原两状态系数理想在每个 $P\in X$ 满足
   $$\mathfrak c(p^{-1}dI_{mp})_P=(\pi,\widetilde H)_P.$$
   在超奇异分支，原首切向形式满足
   $$\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0
   \quad\text{in }H^1(X,\mathcal O_X^p).$$
   重根处的完成式为 $(\pi,z^{e_h})$；无分歧状态提升上的准确阶数由此推出。

## Status

**PASS / PROVABLE AS STATED。**

两份冻结作者稿的本次完整检查未发现硬数学缺口，也没有要求修改作者件。
此结论按作者明确列出的同哈希 U/G 已接受输入及 OC 已独审条件引理理解；
本报告完整承担新 prime trace 证明，以及将实际 qPI 资料接入 OC 的全部新接口。
它不是以旧接受代签新接口，也不需要再添加一般 $m$ 配对常数之类的未证假设。

原量词保留所有素数，包括 $p=2$，以及全部 $p\nmid m$；
不增加奇异能级、圆分高度 $a>1$、任意额外分歧或全初始理想的结论。

## Identity Disclosure and Actual Read Scope

本核查者不是本次两份目标稿的作者。核查前已知主控的 Čech 思路，
并已单独检查过抽象 OC 引理，因此本次不是未接触方向的盲审。
本核查者曾编写旧配对引理、有限端点诊断和 tame 配对探针；
这些旧作者结果均未用于填补本次 prime trace 或实际 A3/A4 的证明责任。
未读取此次新的 tame-block first-jet 独立审查，也未将其他代理的消息当作数学检查。

| 输入 | 本次实际阅读／使用范围 | SHA-256 |
|---|---|---|
| [ALL_TAME_HEIGHT1_PROOF_V1](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md) | 冻结全文 219 行；TH1–TH4、全部五步证明、参数与依赖边界 | `43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75` |
| [PRIME_TRACE_CONGRUENCE_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md) | 冻结全文 269 行；包括原矩阵、全部一般证明、特征二及有限检查边界 | `07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9` |
| [U：通用上同调](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 全文 255 行；仅消费 U2A 的同一自然复形、真实常数项及 $n=0$ 消失，不重开旧整系数分裂的独立接受 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| [G：完整模型](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 第 1–150、170–254 行；仅消费原四图、实际完整纤维、$I$ 正则、G3 及原模型几何接口 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [Integral brief](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 第 25–95 行；核对原矩阵、八截面及原积分规范 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| [OC 作者引理](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md) | 本次重读第 1–90 行核对 A1–A4 接口；其冻结全文 177 行已由下项先前完整独审，不重复开展同一检查 | `81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa` |
| [OC 独立报告](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md) | 本核查者先前交付的同哈希条件引理检查；本次重读第 1–75 行核准其责任边界 | `cb5ec4eda57c74584a03c1aca4d78fa43ee898b8b6d73619f417d0d2bdd3083e` |

以上身份均在本次实际核对；不是从文件名推定版本。
完整读取 `proof-writer` 技能，并按其要求分离准确命题、依赖、推理与有限排错。
没有新增外部文献检索、论文或查新主张。

## Normalized Assumptions and Dependency Map

$\mathcal O_0$ 是无分歧 $p$-进 DVR，剩余域完美，并含准确 $m$ 阶单位根；
$\mathcal O=\mathcal O_0[\zeta_p]$，故 $v_\pi(p)=p-1$。
$t$、根单位及一切底环系数在状态微分下固定。
若需到几何能级，可作相应无分歧／完美剩余域扩张；理想等式使用忠实平坦下降。
准确赋值不向额外分歧扩张直接搬用。

证明责任链为：

1. 原 $p$ 块词轨道与整数迹递推给环面的 $p\pi$ 同余和通用 Taylor 商。
2. U2A 的同一个复形给实际 $L_m$ 的 Bockstein，且其核准确为真实常数。
3. 每个完整 $X$ 的限制正合列把该非零类送到实际函数提升障碍。
4. 原四图在非约化底环上的限制单射将环面同余提升为实际局部 A3。
5. 经逐项核准 A1–A4 后消费 OC，得到首切向非零及原秩二系数理想。

步骤 2–4 是新的实际比较责任，不能由抽象 OC、有限端点评值或旧纯四次配对承担。

## Proof Audit

### 1. 原块、词轨道与 $p=2$ 常值词

记 $r=s^m$，$B_s(z)=A(s^{m-1}z)\cdots A(z)$，
$j_t=[z^m]\operatorname{tr}B_s(z)$，$C=s^{m(m-1)}$，$\delta=s^{3m(m-1)/2}$。
原 $B_s(r^{p-1}z)\cdots B_s(z)$ 展开后，第 $\ell$ 块内部的参数为
$s^{\ell m+m-1},\ldots,s^{\ell m}$，因而准确恢复长度 $mp$ 的原降序乘积。
矩阵恒等式 $\det A(z)=z^3$、$\operatorname{tr}A_0=t$、$\det A_0=0$ 与 brief 一致；
本次另作了保留 $x,y,t,z$ 的精确符号核对。

$A_0^m=t^{m-1}A_0$ 和最高项的幂等矩阵给块迹首尾系数 $t^m,C$，
逐因子取行列式给 $\delta z^{3m}$。
模 $\pi$ 后仅用循环迹即可取得谱旋转不变性。
剩余根单位准确阶为 $m$，所以每个非 $m$ 倍谱次数的系数都在 $(\pi)$ 中。
这里包括 $m=1$ 的空剩余积和 $p=2$，不借用只限奇素数的 first-jet 公式。

对总次数 $mp$ 的指数词，循环移位使权重之差为
$$mp-pi_{p-1}.$$
它被 $p$ 整除，所以 $r$ 相位与矩阵循环迹均在轨道内不变。
素数长度的轨道只有大小 $1$ 与 $p$：常值词的全部指数准确为 $m$，
其相位是奇 $p$ 时的 $1$，以及 $p=2$、$m$ 奇时的 $-1$。
这正是 $\lambda$，不是可以随意略去的整体符号。
其余轨道的差贡献准确为
$$p(r^w-\lambda)\tau\in p\pi R.$$
这一论证不交换矩阵因子，也不在剩余特征中约去 $p$。式 (11) 成立。

### 2. 非共振投影不被当作环同态

整数恒等式 $L_p(S,D)=S^p+pV_p(S,D)$ 来自通用对称多项式，
不需要矩阵可对角化或谱判别式可逆。
$pV_p$ 的输入变化含非共振余项 $E_s\in\pi R[z]$，因此差在 $p\pi R[z]$ 中。

对 $S_s^p$ 必须另审纯次项：贡献 $z^{mp}$ 的纯 $p$ 次单项只能来自次数 $m$，
且两边该系数同为 $j_t$，所以准确抵消。
其余多项式混合项的系数可被 $p$ 整除；未抵消项又必须使用至少一个非共振系数，
因而再带 $\pi$。多个非共振次数回到共振次数的情形已包含其中。
故原式 (13) 成立，与词轨道同余合成得到实际 $I_{mp}-F(j_t)\in p\pi R$。

### 3. 整数导数、Hasse 系数与 Taylor 符号

通用伴随矩阵的迹微分给准确整数恒等式
$$\partial_S L_p=pU_{p-1}.$$
$h$ 在 $S=t^m+hZ+CZ^2$ 中的导数为 $Z$，因此取系数时从 $[Z^p]$ 降为 $[Z^{p-1}]$，
没有多余的 $m$ 或 $p$ 归一化。
模 $p$ 的通用恒等式
$$U_{p-1}(u+v,uv)=(u-v)^{p-1}$$
含 $u=v$，故仍不用可分性假设。
结合 $\bar C=1$、$\bar\delta=(-1)^{m+1}$，得到作者的准确 Hasse 多项式。
$p=2$ 时使用 $U_1=S$，最终系数就是 $h$。

圆分等式给
$$\rho=\pi^{p-1}/p\in\mathcal O^\times,\qquad\bar\rho=-1.$$
当 $p=2$ 时 $\pi=-2$、$\lambda=-1$，故 $\lambda\rho=+1$ 在特征零中成立，
而其剩余值仍为特征二中的 $-1$。作者没有把两种等式混为一谈。
把 $F=\lambda h^p+pQ$ 先在通用多项式环中展开，除以 $p\pi$ 后的中间项
带 $\pi^{j-1}$，$2\leq j<p$；首项与 $Q'$ 给 $H\bar f$，末项给 $-\bar f^p$。
特征二时中间和为空，整数商仍成立。
含挠代数中的商按通用多项式取值解释这一限定也正确。

### 4. 同一个自然复形给实际 Bockstein，而非抽象基向量

固定 U2 的一次导出同构并保留常数映射后，再作所有基变换。
由于其表示复形的项有限自由，短正合列
$$0\longrightarrow k\xrightarrow{\pi}\mathcal O/(\pi^2)\longrightarrow k\longrightarrow0$$
逐项张量仍正合；连接映射可以在这个同一复形中计算。
这来自同一个导出张量三角，而不是只在两个上同调群之间分别选基。

对 $1\leq j<m$，箭头 $1-s^j$ 为单位，对应两项复形可缩。
唯一剩余箭头满足
$$1-s^m=1-(1+\pi)^m\equiv-m\pi\pmod{\pi^2}.$$
提升次数零生成元、求微分并除以 $\pi$ 后，连接映射为 $-\bar m$，是单位。
真实常数直和项的连接映射为零。
所以实际 Bockstein 的核准确为 $k\langle1\rangle$，像为一维非零群。
原 $J$ 是非恒定截面，且 $H^0(S_0,L_{m,0})=k\langle1,J\rangle$，
故 $\beta(J)\ne0$。这里不必也未把 $J$ 强行识别为所选分解中的某个固定基向量。

$p=2$ 时 $\mathcal O/(\pi^2)$ 是混合特征二阶商，以上加法短正合列和复形计算仍有效。
没有要求把它识别为 $k[\epsilon]/\epsilon^2$。

### 5. 非零性准确限制到每个完整有限 $X$

原完整小阶 pencil 给 $X\sim mD_0$，且 $X\cap D_0=\varnothing$。
截面 $J-h\cdot1$ 因此给实际层正合列
$$0\longrightarrow\mathcal O_{S_0}\longrightarrow L_{m,0}
\longrightarrow L_{m,0}|_X\longrightarrow0.$$
有限纤维是有效 Cartier 除子，首箭头单射。
真实截面 $1$ 的零除子为 $mD_0$，故在 $X$ 上给指定平凡化 $L_{m,0}|_X\simeq\mathcal O_X$。
U 的 $n=0$ 消失使长正合列中的两端
$H^1(S_0,\mathcal O)$ 和 $H^2(S_0,\mathcal O)$ 都为零，因而
$$H^1(S_0,L_{m,0})\xrightarrow{\sim}H^1(X,\mathcal O_X)$$
是实际限制同构。这一证明逐个适用于每个完整 $X$，不只比较维数或泛纤维。

在 $\mathcal U$ 上仍以同一个截面 $1$ 平凡化 $L_m$。
局部截面提升变成真正正则函数 $j_i$，连接同态的 Čech 代表正是
$$\overline{(j_j-j_i)/\pi}.$$
其在 $X$ 上的限制因而就是 Claim 的 $\kappa_J$，不是另造的上同调类。
相对光滑性保证除 $\pi$ 后商正则；改选提升只加余边界。
上述限制同构送非零 $\beta(J)$ 到非零 $\kappa_J$，故 TH1 成立。
也排除了原 $J$ 在整个二阶开曲面上的全局提升。

### 6. 全部末端图上的非约化整除性

可以细化覆盖，使各 $j_i$ 所在开集包含于环面或一张实际末端坐标图。
模 $\pi$ 后 $j_t$ 与 $j_i$ 均是同一个 $J$，故在环面交上
$j_i-j_t=\pi f$。通用 Taylor 商与第 1–3 节合成给该交上的 $p\pi$ 整除性。

必须审查模 $p\pi$，而不仅是模 $\pi$。
原四张末端图分别有单位因子
$$1+uv,\qquad t+uv,\qquad t+uv,\qquad s+uv,$$
且局部去掉末端线就是再求逆 $u$。
即使 $B=\mathcal O/(p\pi)$ 非约化，乘 $u$ 在 $B[u,v]$ 上仍单射：
按 $u$ 的幂比较每个系数即可；此性质经所需局部化保留。
因此图函数模 $p\pi$ 到其环面交的限制确实单射。
$I$ 已由 G 正则，$F(j_i)$ 也正则，两者差在交上为零便在实际图上为零。
故每张图都有
$$I-F(j_i)\in p\pi\mathcal O(U_i).$$
这没有使用约化点集稠密性，也没有假装环面 $j_t$ 是全局正则提升。
四条末端线、包括其任意有限点均被覆盖。

### 7. OC 的实际 A1–A4 全部核准

| OC 接口 | 原模型中的实际来源 |
|---|---|
| A1：$v_\pi(p)=p-1$ 及 $\overline{\lambda\pi^{p-1}/p}=-1$ | 高度一圆分 DVR 与 prime trace 的整数圆分等式，含特征二 |
| A2：常数系数 $F=\lambda h^p+pQ$ | 原迹递推的固定整数多项式；全部状态微分固定 $t,s$ |
| A3：实际局部 $I-F(j_i)\in(p\pi)$ | 原环面词轨道同余、任意提升的 Taylor 商及非约化四图单射 |
| A4：原函数提升类 $\kappa_J\ne0$ | 同一自然复形的真实常数核及每个完整纤维上的实际限制同构 |

几何前提也匹配：原模型相对光滑二维，有限完整纤维几何整；所选概形纤维光滑。
由 $D_0=-K_{S_0}$、八次吹起后的 $D_0^2=0$ 和 $X\sim mD_0$，
伴随公式给 $2g(X)-2=X\cdot(X+K_{S_0})=0$，故光滑 $X$ 的亏格为一。
光滑概形纤维还保证 $dJ$ 是环境余切模的非零法向。

对 $H_p(T,h;\varepsilon_m)=0$ 的分支，现在才能消费已单独独审的 OC。
它给原函数 $G_i=(I-F(j_i))/(p\pi)$、原首切向形式 $\nu=d(\bar G_i|_X)$，
以及准确的正号比较 $\partial\nu=\operatorname{Fr}_*\kappa_J$。
$\operatorname{Fr}:\mathcal O_X\to\mathcal O_X^p$ 是加法层同构；
随后到 $H^1(X,\mathcal O_X)$ 的包含映射可能杀掉该类，二者不能合并。
因此超奇异情形没有“Frobenius 为零故障碍为零”的矛盾。
这次实际接口检查与先前抽象 OC 检查共同承担 TH3，不靠任何一般 $m$ 配对数值猜测。

### 8. 原两状态理想、重根与状态赋值

完整光滑亏格一曲线上的非零正则微分无零点。
在每个 $P\in X$ 将 $dj_i$ 补为相对余切基 $(dj_i,\theta)$，可写
$$\alpha=(F'(j_i)/p+\pi A)dj_i+\pi B\theta,$$
其中 $B$ 在该点是单位，由原 $\nu$ 的非零切向值保证。
故原两个系数生成 $(\pi,F'(j_i)/p)$，其第二生成元模 $\pi$ 准确为 $H$。
任意两个 $H$ 的提升之差在 $(\pi)$ 中，所以 TH2 的任意提升表述成立。
这不是只求一个切向系数或某个状态点的公共赋值。

普通光滑层上 $H$ 为单位，G3 给 $\bar\alpha=H\,dJ$；
$dJ$ 非零使原系数理想为单位理想。该分支不套用超奇异 OC 前提。

若 $h$ 为 $e_h$ 重根，剩余局部环中有
$$H=(J-h)^{e_h}V(J),\qquad V(h)\ne0.$$
无分歧剩余域扩张后的光滑形式坐标可令 $\bar z=J-h$，
故完成理想准确为 $(\pi,z^{e_h})$，不要求简单根。
沿任意给定无分歧状态提升，$z$ 的像在 $(\pi)$ 中；
因此超奇异层的系数理想像准确为 $(\pi)$，普通层为 $(1)$。
再乘 $p$，利用 $v_\pi(p)=p-1$，得到原 $dI_{mp}$ 的准确阶分别为 $p$ 和 $p-1$。
这些是实际两系数理想的推论，不是从下界误升为等式。

## Independent Finite Exact Checks

另运行一次内存 `python -B` 精确代数检查，退出码为 0；没有写脚本、数据或缓存文件。
实现直接按原次序累乘原矩阵，使用有理系数圆分商环，不调用作者的诊断脚本。
以下有限检查用于排错，不代替上面的一般证明：

| 检查对象 | 结果 |
|---|---|
| 保留符号 $x,y,t,z$ 的原矩阵 | $\det A(z)=z^3$、$\operatorname{tr}A_0=t$、$\det A_0=0$ 全部准确成立 |
| 通用 $p=2,3,5,7$ | $L_p-S^p\in p\mathbb Z[S,D]$、$\partial_SL_p=pU_{p-1}$、Hasse 系数及整数 Taylor 剩余式全部通过 |
| $(p,m,t,x,y)=(2,3,3,5,7)$ | 原差除以 $p\pi$ 的圆分幂基系数分母均与 $p$ 互素，商非零，乘回恢复原差 |
| $(2,5,5,3,7)$ | 同上，通过 |
| $(3,2,1,2,4)$ | 同上，通过 |
| $(3,4,2,4,5)$ | 同上，通过 |
| $(5,2,3,2,4)$ | 同上，通过 |

这些状态和时间在对应 $p$ 处均为单位。
取准确 $mp$ 阶生成元 $s$，按
$\zeta_p=s^{m(m^{-1}\bmod p)}$ 定义本次检查的 $\pi$，与作者参数分解一致。
通用 Taylor 检查先在特征零中除法并按 $\Phi_p(1+\pi)$ 约化，
检验系数 $p$-整性后才取剩余常数项；没有在特征 $p$ 中数值除以 $p$。

## Corrections or Missing Assumptions

未发现需修改作者件或缩小所声明量词的硬问题。
未要求补充任何一般 $m$ 配对、谱四次可分性、简单 Hasse 根或全局 $J$ 提升假设。
复形选择只须对固定 $n=m$ 一次固定，故不需要 U 未声明的跨 $n$ 兼容乘法或过滤同构。

本报告使用的“完整光滑能级”始终为概形意义上的原有限纤维；
若只取约化支撑光滑而实际纤维有重数，非零法向和上述论证不自动适用。
作者已经明确使用原完整光滑 $X$，本项只是防止后续扩大解释。

## Open Risks and Delivery Boundary

在两份冻结目标稿及上述同哈希依赖范围内，本次新数学检查无未关闭硬风险。
已通过且输入不变的 U/G 和 OC 不由本报告重复评票；若相关输入更改，需定位改变的消费接口。
本次 PASS 不证明一般 $m$ 的先前配对猜想，也不接受全高度厚度、奇异层、稳定约化或整个初始理想。
数学通过不产生来源新意、独立长文价值、自然容量或正式候选资格。
未读取或修改 source/publication locks、既有失败票、索引、稿件、PDF 或任何外部状态。
仅新增本报告；作者稿和原模型输入保持冻结。
