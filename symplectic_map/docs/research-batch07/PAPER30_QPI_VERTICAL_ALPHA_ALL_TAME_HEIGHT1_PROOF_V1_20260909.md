# qPI：全部剩余阶的首层垂直理想与实际提升障碍

日期：2026-09-09。作者：主控 `/root`。
类型：新的有界作者证明；`route_applicability: NOT_APPLICABLE`。
本件只处理圆分高度 $a=1$；既有 $m=1$ 数学接受不自动代签本件的全 $m$ 接口。

## Claim

固定素数 $p$、整数 $m\ge1$、$p\nmid m$。令 $\mathcal O_0$ 为含精确 $m$ 阶单位根
$\widetilde\eta$ 的无分歧 $p$-进 DVR，其剩余域 $k$ 完美，置
$$\mathcal O=\mathcal O_0[\zeta_p],\qquad
\pi=\zeta_p-1,\qquad s=\widetilde\eta\zeta_p,\qquad t\in\mathcal O^\times.$$
$s$ 的准确阶为 $mp$，剩余 $\eta$ 的准确阶为 $m$。
可在原圆分局部环作这一无分歧／完成基变换后证明；理想等式再由忠实平坦性下降。
不容许任意额外分歧扩张后仍沿用下述准确阶数。

在 [G §1 的原八截面模型](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) 上，
取 $\mathcal U=\mathcal S\setminus\mathcal D$、$L_n=\mathcal O_{\mathcal S}(n\mathcal D)$，
保留原矩阵、降序乘积和原迹系数 $I=I_{mp}$，定义
$$\alpha=p^{-1}d_{\rm state}I,\qquad
J=I_{m,\eta}(x,y;\bar t),\qquad T=\bar t^m,\qquad \varepsilon_m=(-1)^{m+1}.$$
时间、根单位和底环系数不参与微分。
所有能级均为原 $J$ 的完整有限纤维，不替换为另一谱曲线或稠密开子曲线。
置
$$H=H_p(T,J;\varepsilon_m),$$
其中奇 $p$ 时
$$H_p(T,h;\varepsilon)=[Z^{p-1}]\bigl((T+hZ+Z^2)^2-4\varepsilon Z^3\bigr)^{(p-1)/2},$$
而 $p=2$ 时 $H_2(T,h;\varepsilon)=h$。

**TH.1（准确的实际障碍）。** 对每个光滑有限几何能级 $X=(J=h)$，
原函数 $J$ 在 $\mathcal U/(\pi^2)$ 的局部提升给出非零类
$$\kappa_J=\left[\overline{(j_j-j_i)/\pi}\big|_X\right]
\ne0\quad\text{in }H^1(X,\mathcal O_X). \tag{TH1}$$
这里 $j_i$ 是覆盖 $X$ 的实际正则局部函数，不假设存在全局提升。
非零性来自实际 $L_m$ 的一阶 Bockstein，且在每一个这样的完整 $X$ 上保持非零。

**TH.2（原首层理想）。** 对每个上述 $X$ 上的点 $P$，在实际局部环中
$$\boxed{\mathfrak c(\alpha)_P=(\pi,\widetilde H)_P.} \tag{TH2}$$
$\mathfrak c$ 是原相对秩二余切模的两个系数所生成的理想；波浪号为任意局部提升。
若 $H_p(T,h;\varepsilon_m)=0$，由下面固定的整数多项式 $F$ 构造首切向形式 $\nu$，则
$$\boxed{\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0
\quad\text{in }H^1(X,\mathcal O_X^p).} \tag{TH3}$$
因而 $\nu$ 在完整 $X$ 上处处非零，含原模型四条末端线上的所有点。
此处 $\operatorname{Fr}:\mathcal O_X\to\mathcal O_X^p$ 是到其像层的加法层同构，
不是随后映入 $H^1(X,\mathcal O_X)$ 的超奇异 Frobenius 算子。

**TH.3（完成式和状态提升）。** 若 $h$ 是上述 Hasse 多项式的 $e_h$ 重根，
在任一 $P\in X$ 作剩余域无分歧扩张并完成后，可取横向参数 $z$，$\bar z=J-h$，使
$$\mathfrak c(\alpha)\widehat{\mathcal O}_{\mathcal U,P}=(\pi,z^{e_h}). \tag{TH4}$$
沿任意无分歧状态提升，$\alpha$ 的两状态系数公共 $\pi$-阶在光滑超奇异层准确为 $1$，
在光滑普通层准确为 $0$；原 $dI$ 的相应阶为 $p$ 与 $p-1$。
不涵盖奇异能级、全高度 $a>1$ 的厚度，或额外分歧提升后的准确阶。

## Status、依赖与策略

**PROVABLE AS STATED（作者证明；新的接口及依赖仍待非作者合取检查）。**
证明责任分为三段，不能相互替代：

1. 已接受的 [U2A](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)
   用于实际 $L_m$ 的二阶底变换，再由完整能级的限制正合列证明 (TH1)。
2. 新 [prime trace 引理](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md)
   的环面 $p\pi$ 同余，经本件的局部提升和实际末端图延到整个 $X$。
3. 新 [Čech—Cartier 引理 OC](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md)
   在前两项实际前提核准后才用于原 $\alpha$。

第二、三项是新作者件，未由旧 $m=1$ 接受或消息结论替代独审。
本证明不需要尚未证明的一般 $m$ 配对常数 $m^2$，也不使用奇素数全高度的首 jet 因子分解。
Čech、Bockstein、Cartier 及亏格一典范次数均为标准工具；本件不据此宣称一般理论首创。

## Proof

### Step 1. 同一个 $L_m$ 的实际 Bockstein

记 $A_2=\mathcal O/(\pi^2)$，$S_0=\mathcal S\otimes k$。
已接受 U2A 对所有基变换自然，保留真实常数截面，故对 $n=m$ 给出同一个有限自由复形
$$C_A=A[0]\oplus\bigoplus_{j=1}^m[A\xrightarrow{1-s^j}A] \tag{1}$$
计算 $R\Gamma(S_A,L_{m,A})$，分别取 $A=\mathcal O,A_2,k$。
“同一个”意为先固定通用复形的选择再基变换；不为两个底环分别挑选不兼容的分裂。

当 $1\le j<m$ 时，$1-\eta^j$ 非零，故相应箭头为单位。
当 $j=m$ 时，由 $\widetilde\eta^m=1$，准确有
$$1-s^m=1-(1+\pi)^m\equiv-m\pi\pmod{\pi^2}. \tag{2}$$
$m$ 在 $k$ 中为单位。
对短正合列 $0\to k\xrightarrow{\pi}A_2\to k\to0$，
用 (1) 逐项计算连接同态：$j=m$ 的次数零生成元先提升、求微分再除 $\pi$，
其像为 $-\bar m$ 倍的次数一生成元；常数项的像为零。
因此实际层序列的 Bockstein
$$\beta:H^0(S_0,L_{m,0})\longrightarrow H^1(S_0,L_{m,0}) \tag{3}$$
秩为一，且核准确为真实常数截面 $k\langle1\rangle$。
连接同态关于导出同构及基变换的自然性将这个复形计算识别为实际层序列的 (3)。
此处没有把一个抽象同构的基向量默认为原 $J$。

原最小完整 $m$ 阶 pencil 给
$$H^0(S_0,L_{m,0})=k\langle1,J\rangle.$$
原 $J$ 非常数，于是它不在上述核中，故 $\beta(J)\ne0$。
对 $p=2$，$\pi=-2$ 且 $A_2$ 一般特征四；(1)–(3) 仍直接在该混合特征短正合列中成立。
这里从未使用 $A_2\simeq k[\epsilon]/\epsilon^2$。

### Step 2. 非零类限制到每个完整有限能级

先将剩余域扩张到包含 $h$ 的完美域，必要时使用相应无分歧底变换。
有限几何能级 $X=(J=h)$ 与 $D_0$ 不相交，其除子类为 $mD_0$。
在 $S_0$ 上，原截面 $J-h\cdot1$ 给准确正合列
$$0\longrightarrow\mathcal O_{S_0}
\xrightarrow{\ J-h\cdot1\ }L_{m,0}
\longrightarrow L_{m,0}|_X\longrightarrow0. \tag{4}$$
原有限纤维是有效 Cartier 除子，故首箭头单射；此处将 $J$ 理解为 $L_m$ 截面。
因为 $1$ 的零除子是 $mD_0$，它在 $X$ 上处处非零，给指定平凡化
$$L_{m,0}|_X\simeq\mathcal O_X.$$
已接受 U 的 $n=0$ 部分给 $H^1(S_0,\mathcal O)=H^2(S_0,\mathcal O)=0$。
由 (4) 的长正合列，实际限制同态因此为同构
$$\rho_X:H^1(S_0,L_{m,0})\xrightarrow{\sim}H^1(X,\mathcal O_X). \tag{5}$$
这是对每一个 $X$ 的同构，不是只对泛纤维的维数比较。

在 $\mathcal U$ 上，实际截面 $1$ 同样平凡化 $L_m$。
以该平凡化表示 $J$ 的任意局部提升为正则函数 $j_i$，
则按 Čech 余边界 $c_j-c_i$ 的约定，(3) 的局部代表正是
$\overline{(j_j-j_i)/\pi}$。
进一步限制到 $X$，(5) 将 $\beta(J)$ 准确送到 Claim 中的 $\kappa_J$。
改变局部提升只加 Čech 余边界。
由 Step 1 非零性和 (5) 单射性，取得 (TH1)。
这还证明该障碍在开曲面上不会因去掉边界而变零：若先在开曲面变零，再限制到 $X$ 也必为零。

### Step 3. 原环面的整数同余与正确的局部提升

使用 prime trace 引理的固定记号
$$B_s(z)=A(s^{m-1}z)\cdots A(z),\quad j_t=[z^m]\operatorname{tr}B_s(z),$$
$$C=s^{m(m-1)},\quad d=s^{3m(m-1)/2},\quad
\lambda=1\ (p\ne2),\quad\lambda=-1\ (p=2),$$
以及整数迹递推 $L_0=2,L_1=S,L_n=SL_{n-1}-DL_{n-2}$，定义
$$F(H_0)=\lambda[Z^p]L_p(t^m+H_0Z+CZ^2,dZ^3). \tag{6}$$
这里 $H_0$ 仅为多项式自变量，与 Hasse 函数 $H$ 区分。
该引理 §2–6 证明，先在整系数 Laurent 环中，
$$I-F(j_t)\in p\pi\mathcal O[x^{\pm1},y^{\pm1}],\qquad
F(H_0)=\lambda H_0^p+pQ(H_0), \tag{7}$$
$$\overline{F'(H_0)/p}=H_p(T,H_0;\varepsilon_m),\qquad
\overline{\lambda\pi^{p-1}/p}=-1. \tag{8}$$
模 $\pi$ 后，$j_t$ 正是原小阶 $J$；这是原 $m$ 块迹系数的定义，不作能级重规范。

取覆盖 $X$ 的实际仿射开集，选任意正则局部提升 $j_i$。
在它与环面的交上，$j_i-j_t=\pi f$，其中 $f$ 正则。
prime trace 引理的通用整数 Taylor 商给
$$F(j_i)-F(j_t)\in p\pi\mathcal O(U_i\cap(\mathbb G_m)^2). \tag{9}$$
商先在通用多项式环中定义再代入，故没有在剩余特征中约去零元素。
合并 (7)、(9)，$I-F(j_i)$ 在上述交上可被 $p\pi$ 整除。
不能据此假定 $j_t$ 已是完整曲面的全局正则提升；Step 2 事实上排除了这样的提升。

### Step 4. 整数同余跨过全部末端线

$I$ 由已接受 G1 在 $\mathcal U$ 正则，$F(j_i)$ 也正则。
需要检验它们之差模 $p\pi$ 的消失，不只检查约化点集。
原环面以外的 $\mathcal U$ 由 G §1 的四张末端图覆盖，其坐标为
$$\begin{array}{ll}
x=u^{-1},\ y=1+uv;&x=u(t+uv),\ y=u^{-1};\\
x=u(t+uv),\ y=u^2(t+uv);&x=[u(s+uv)]^{-1},\ y=u^{-1}.
\end{array} \tag{10}$$
在每条末端线的实际点附近，除 $u$ 外所列分母及 $t+uv$、$s+uv$、$1+uv$
按对应图均为单位；图的坐标环是 $\mathcal O[u,v]$ 的相应局部化。
即使底环换成 $\mathcal O/(p\pi)$，$u$ 仍为非零因子：
多项式模按 $u$ 的幂逐项自由，乘 $u$ 单射，随后局部化保持单射。
环面交由再求逆 $u$ 得到，故
$$\mathcal O(U_i)/(p\pi)\hookrightarrow
\mathcal O(U_i\cap(\mathbb G_m)^2)/(p\pi) \tag{11}$$
单射；对进一步局部化也成立。
由 Step 3，差的右侧像为零，故左侧已为零。
于是对全部这些原图，包括所有末端点，都有
$$I-F(j_i)\in p\pi\mathcal O(U_i). \tag{12}$$
这是非约化底环上的函数单射论证，不是用 Zariski 点稠密性冒充模 $p\pi$ 的单射。

### Step 5. 实际比较、全点理想与完成式

对光滑超奇异 $X$，(8)、(12) 与 (TH1) 分别核准 OC 引理的 A1–A4；
$\mathcal U/\mathcal O$ 光滑、$X$ 完整光滑几何整亏格一由同一原模型及所选光滑能级保证。
因此取实际正则函数
$$G_i=(I-F(j_i))/(p\pi),\qquad
\alpha=(F'(j_i)/p)dj_i+\pi dG_i.$$
OC 的完整证明给 $\nu=d(\bar G_i|_X)$，并给准确比较
$$\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0.$$
故 $\nu$ 是完整 $X$ 上的非零正则微分，亏格一使其无零点。
在每个点将 $dj_i$ 补为实际相对余切基，切向系数因此是 $\pi$ 乘单位；
消去法向中的 $\pi$ 倍数，得到 (TH2)。
这证明非零性的来源是原函数提升障碍，不是任意选择的辛补基。

对普通光滑 $X$，已接受 G3 的 $\bar\alpha=H\,dJ$ 且 $dJ$ 处处非零，
故至少一个系数是单位，$\mathfrak c(\alpha)_P=(1)=(\pi,\widetilde H)_P$。
这一分支不使用超奇异 OC 的前提。

对 $e_h$ 重根，模 $\pi$ 有
$H_p(T,J;\varepsilon_m)=(J-h)^{e_h}V(J)$，其中 $V(h)\ne0$。
光滑性使 $dJ$ 是非零法向，可在无分歧剩余域扩张后的完成局部环中
取 $z$ 提升 $J-h$，再补一个沿曲线参数；其相对形式光滑坐标存在于原光滑模型。
$V(J)$ 的提升为单位，所以 (TH2) 完成后准确化为 (TH4)。
沿无分歧状态提升，超奇异点的 $z$ 落入 $(\pi)$，故 $(\pi,z^{e_h})$ 的像准确为 $(\pi)$；
普通层像为单位理想。再乘 $p$，利用 $v_\pi(p)=p-1$，得 TH.3 所述状态阶数。证毕。

## Corrections or Missing Assumptions

- TH1 的非零性在每个完整 $X$ 的 $H^1(\mathcal O_X)$ 中实际证明；不能只引用全曲面的非零类。
- $p=2$ 的 Bockstein 使用特征四二阶商，迹同余使用 $\lambda=-1$；两处不能套奇素数双数计算。
- TH2 保留两个相对状态方向；单个末端点评值或一个切向系数不替代整个理想。
- 首层同余、实际障碍和 OC 比较三段缺一不可；全高度的首 jet 作者件不承担这些责任。
- 若扩大为奇异能级、全高度厚度、全初始理想或任意分歧状态阶数，当前结论不足。

## Open Risks、实际输入与交付边界

本件为新的作者证明，待对新接口及 prime trace 的非作者检查，并与 OC 的单独检查合取。
尚未授予新意、独立长文价值、自然容量或正式候选资格，不改变既有失败票。
未声称完整上同调复形与微分模的典范同构、晶体比较或一般 $m$ 的配对数值 $m^2$。

实际使用输入身份：

| 输入 | 使用范围 | SHA-256 |
|---|---|---|
| U 作者件 | 全文 255 行；尤其 U2A 关于底变换自然性、常数项，及 $n=0$ 消失 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| G 作者件 | §1 原四图、G1/G3 与证明 Steps 1–2、5–6；已接受内容只作接口消费 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| prime trace 引理 | 终态全文 269 行；本件准确消费 (3)–(6) 的整系数同余与 $p=2$ 符号 | `07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9` |
| OC 引理 | 全文 177 行；本件验证全部 A1–A4 后消费 OC1–OC2 | `81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa` |

仅新增本文件；不创建 Paper30 项目、稿件、source/publication locks、PDF、GPU 任务或外部效力。
