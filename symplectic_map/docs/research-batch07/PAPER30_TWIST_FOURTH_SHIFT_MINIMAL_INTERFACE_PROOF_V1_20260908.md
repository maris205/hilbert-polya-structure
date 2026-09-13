# Paper30：四次移位的最小全参数接口 V1

日期：2026-09-08。作者：主控。性质：同对象替代证明，尚待针对本件变更的非作者数学检查。
不改写原完整四次多项式，不改变当前 C1–C3 或全部 $p\ge5,a\ge2$ 的科学范围。
本件只检验该中心真正需要的四次接口；不是容量票、正文草稿或测页。

## Claim

对每个素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
同一实际低块、有限单位耦合模型及已配对第三端点保持。
存在一个**全参数多项式** $E_4\in\mathbb F_p[L]$，使逐系数地

$$
\mathcal E(H,L)=r(H)^3\mathcal F_3(H,L)+r(H)^4E_4(L)
                         +O(H^{4m+1}),\qquad E_4(0)=-\frac3{32},
\tag{1}
$$

其中 $r=2\chi H^m+O(H^{m+1})$，$\mathcal F_3$ 为同一个完整三次端点。
本件直接证明 (1)，不求 $E_4$ 正 $L$ 系数的闭式，不调用原 A10 的奇矩 $J_1(L)$ 全参数求值。
因此它没有重证或撤销原 A10 的更强显式多项式结果。

结合已接受完整三次项的逐系数输入，(1) 给出原正簇所需的全部低参数系数界和实际常数；
这个组合仍对所有参数系数成立，不能把本件称为仅有 $L=0$ 的第三 forcing 定理。
它是否足以替代当前全部 A10 消费者，另由限定依赖检查回答；本件不自授组合审查。

## Status and Target

式 (1) 及§5列出的实际正簇接口：`PROVABLE AS STATED`，作者证明如下，未授非作者 PASS。
推导目标为一个精确的有限形式身份与其同精度实际转移，不是近似模型或新科学主张。
固定对象始终是原 $h=D_1,\rho=-h,L=\rho\lambda$、SUM action 下的第三内部 forcing。
临时令 $H=0,L=0$ 只用于求四次多项式的常数；全参数存在／整性先在§1证明。

## Assumptions and Exact Inputs

1. [A07 一般第三端点](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)
   Steps 1–4、式 (18)、(21)–(24)：真实 action及其误差、准确四项端点、合法有限移位，
   正次数模型在 $1\le i<p$ 具有单位三角唯一性。
2. [A06 完整耦合桥](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)
   的准确两条耦合方程；未乘端点缺陷的实际块误差仍只有 $h^{M-m}$。
3. [A09 全 $H$ 响应](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md)
   Step 1及Step 2开头：$\mathcal F_3$ 是完整三次系数，而不是丢掉第一配对项的版本。

本件重新推导四次响应所需有限方程及其常数配对，不将 A10 式 (17) 或式 (22) 当输入。
原 [A10 完整证明](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md)
已全文读取以定位可替代义务，原文件与接受状态保留。
实际转移的首层单位 $a_m=-3\chi/64+O(h)$、首一分离及原三次接口仅在§5调用，
不用于倒证本件 $E_4(0)$。

## Notation and Dependency Map

低块 $P(H,L,x)$ 为正次数有限多项式，$P_1=1/2$，
在 $\mathbb F_p[L][[H]][x]/(x^p)$ 满足

$$
\mathcal DP=-\frac{x}{2}e^P-Lx^2e^{2P},\qquad
\mathcal D x^i=d_i(H)x^i,\quad d_i(0)=-i^2\quad(1\le i<p).
$$

低块／单位响应的指数只提取次数小于 $p$ 的系数，分母皆为单位。
在独立移位变量 $\nu$ 中使用原 $\Delta_k=\mathcal D_k-\mathcal D$；
最终才令 $\nu=r(H)$。此为已证明的有限形式代入，不改变实际初值或参数。
依赖顺序：全参数单位性与有限展开 → 四次多项式存在 → 常数截面响应 → 有限配对 → 实际接口。

## Proof

### 1. 先证明全参数多项式存在及其误差

A07 的对角移位在实际代入后具有

$$
\Delta_k=k r\mathsf S+k^2r^2\mathsf T+k^3r^3\mathsf U
                   +O(H^{4m+1}),
\quad \mathsf S|_{H=0}=\mathcal N,\quad
\mathsf T|_{H=0}=-I/4,\quad\mathsf U|_{H=0}=0,
\tag{2}
$$

其中 $\mathcal N=x\partial_x$。对独立 $\nu$ 的有限三角模型，
对角元在 $H=\nu=0$ 为 $-i^2\ne0$，$1\le i<p$；逐阶求解只除这些
与参数 $L$ 无关的单位。故每个所需 $H,\nu$ 系数均为 $L$ 的多项式。
没有将实际 $L$ 设为幂零，也没有排除任何参数点。

准确配对后的第一端点项为

$$
\frac{3r^3H}{8(H-4)}\sum_{i=1}^{p-1}i^3\mathsf S_iP_iP_{p-i}
                      +O(H^{4m+1}).
\tag{3}
$$

此项归入完整 $r^3\mathcal F_3$，在四次系数的 $H^0$ 截面没有贡献。
不能用未经实际配对的独立 $\nu$ 第一项代替 (3)。
其余三项由 $y=O(\nu),Q=O(\nu^2)$、$C_i=O(\nu^2)$ 和
$\delta_i^{\rm low},\delta_i^{\rm mid}=O(\nu)$ 得到最低次数为三，
因而其四次系数 $E_4(H,L)$ 属于 $\mathbb F_p[L][[H]]$。
定义 $E_4(L)=E_4(0,L)$。四次系数的正 $H$ 修正代入后至少为 $H^{4m+1}$，
五次以上移位至少为 $H^{5m}$，而 $5m\ge4m+1$，包含最小 $m=2$。
(2) 的模型误差也经单位三角比较保持在 $H^{4m+1}$。
这证明 (1) 的全参数存在、整性与误差，只剩常数待算。

### 2. 常数截面的有限低块与两条驱动

现在仅为计算 $E_4(0)$ 取 $H=0,L=0$。记 $U=P(0,0,x)$，
$z=x/4$，并取下式的 $1\le n<p$ 系数：

$$
U=-2\log(1-z),\qquad f=\mathcal NU=\frac{2z}{1-z},\qquad
g=\mathcal N^2U=\frac{2z}{(1-z)^2},\qquad F=g.
\tag{4}
$$

有理式只表示所需有限系数。因为 $\mathcal N^2U=xe^U/2$，
(4) 满足同一低块方程及 $U_1=1/2$；单位三角唯一性说明它是实际低块的截面，
不是另一模型。这里没有取可能含 $1/p$ 的 $[x^p]U$。

记 $J=xe^U/2=F$、$K=xe^U/4=F/2$，$\mathscr L=-\mathcal N^2+F$。
对 (4) 求有限系数导数，得到

$$
\mathscr Lf=-F,\qquad
\mathscr Lg=-F-2Ff-Ff^2,\qquad \mathcal Nf=g.
\tag{5}
$$

例如 $\mathcal NF=F(1+f)$、$\mathcal N^2F=F(1+2f+f^2)+F^2$，
立即逐项给出 (5) 的第二式，无须能量积分或第$p$模态。

写零常数响应

$$
y=\nu t+\nu^2a+O(\nu^3),\qquad
Q=\nu^2q+\nu^3b+O(\nu^4).
$$

在此截面 $\Delta_k=k\nu\mathcal N-k^2\nu^2/4$。
将它代入准确耦合式

$$
(\mathcal D_1+J)y=\frac12\Delta_1\mathcal NU,
$$
$$
(\mathcal D_2+J)Q=(2\Delta_1-\Delta_2)\frac{\mathcal N^2U}{8}
       +\frac12(\Delta_2-\Delta_1)\mathcal Ny-Ky^2,
\tag{6}
$$

用 (5) 验证前两解，并取后两驱动，得

$$
t=-\frac f2,\qquad q=\frac g8+\frac f{16},\qquad
\mathscr La=-\frac f8+\frac g2,
\tag{7}
$$
$$
\mathscr Lb=\frac12\mathcal N^2a+\frac1{16}\mathcal Nf
                         +Kfa-\frac14\mathcal Ng.
\tag{8}
$$

这些等式均只在正次数 $i<p$ 求解；正对角元仍为单位。
本件不求 $a,b$ 的闭式。

### 3. 直接算标量端点，不建立全参数奇矩

对零常数有限级数置 $B(v,w)=[x^p]vw$。
因两因子均正次数，只涉及各自小于$p$的系数，并有

$$
B(\mathcal Nv,w)=-B(v,\mathcal Nw),\qquad
B(\mathscr Lv,w)=B(v,\mathscr Lw).
\tag{9}
$$

第一式由 $[x^p]\mathcal N(vw)=p[x^p]vw=0$；第二式用两次第一式及乘法算子 $F$ 的对称性。
即使有限方程的第$p$系数未定义，残差也只能与另一因子的零常数相乘，故不进入 (9)。

在当前截面，后三项真实端点的缺陷为

$$
C_i^*=3\nu^2/2,\qquad
\delta_i^{\rm low}=3i\nu+9\nu^2/4,\qquad
\delta_i^{\rm mid}=3i\nu+3\nu^2/4.
$$

代入四项端点中除 (3) 外的部分并取 $\nu^4$，得到

$$
E_4(0)=\frac32B(F,a)+6B(F,b)+\frac92B(f,q)
                                      +6B(\mathcal N^2t,a).
\tag{10}
$$

二次混合项用偶权对称合并；同一个 $t$ 的奇权矩为零。
由 $\mathscr Lf=-F$，以 (8) 消去 $b$；由 (7) 代入 $t,q$，
(10) 化为

$$
\begin{aligned}
E_4(0)={}&B(3F/2-6\mathcal N^2f-6Kf^2,a)
+\frac32 B(f,\mathcal Ng)\\
&-\frac38 B(f,\mathcal Nf)+\frac9{16}B(f,g)+\frac9{32}B(f,f).
\end{aligned}
\tag{11}
$$

(5) 给出准确恒等式

$$
3F/2-6\mathcal N^2f-6Kf^2=\mathscr L(3g+3f/2).
\tag{12}
$$

以 (9)、(7) 消去 $a$，第一项成为
$B(3g+3f/2,-f/8+g/2)$。
又 $B(f,g)=B(f,\mathcal Nf)=0$，
$B(f,\mathcal Ng)=-B(g,g)$，所以所有 $B(g,g)$ 项取消，
留下

$$
E_4(0)=\left(-\frac3{16}+\frac9{32}\right)B(f,f)
       =\frac3{32}B(f,f).
\tag{13}
$$

由 (4)，$f_i=2/4^i$，$1\le i<p$，故

$$
B(f,f)=\sum_{i=1}^{p-1}\frac{4}{4^p}
       =\frac{4(p-1)}{4^p}=-1\quad\text{于 }\mathbb F_p.
$$

最后一步用 $4^p=4$，所有数值分母均为2的幂。
因此 $E_4(0)=-3/32$，证明 (1)。
这个标量证明没有引入 $J_1(L)$、独立二次分母的分裂根、Frobenius系数身份或有限几何和。

### 4. 保留全参数接口而非改成单参数点结果

§1已证明同一 $E_4(L)$ 是参数多项式；§2–3只是求其常数。
因此对每个 $j\ge0$，$[L^j]E_4$ 是合法有限域系数，没有参数排除或极点。
并未从仅在 $L=0$ 成立的解推出全参数响应方程，也不将实际 $L$ 设为零。
完整三次项、所有四次组成量的定义及其统一误差均留在 (1)；
省去的是原 A10 的正 $L$ **显式求值**，不是删掉它们或假设它们为零。

### 5. 对实际正簇所需的全部系数有足够精度

在此步令 $\zeta$ 为任一本原 $p^{a_{\rm den}}$ 次根，$a_{\rm den}\ge2$；
另记下标 $a_{\rm den}$ 以免与响应 $a$ 混淆。
置 $h=2-\zeta-\zeta^{-1}$、$K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$，
$D=3m+1$、$M=p^{a_{\rm den}-1}m=v_h(p)$、$S=h^{-D}p^2\mathcal B_3$。
首一正因子沿用既有分离 $S=P_{\rm cl}U_{\rm cl}$，
$P_{\rm cl}=L^m+\sum_{j<m}b_jL^j$、$a_m=[L^m]S$。

仅在此步调用已接受的三次接口

$$
[L^j]\mathcal F_3\in H^{m-j+1}\mathbb F_p[[H]]\ (1\le j<m),\qquad
\mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}),
$$

以及实际端点模 $h^M$ 桥、$M\ge pm\ge4m+1$。
由 (1)，四次项除以 $H^{D}$ 后对任意参数系数都从 $H^{m-1}$ 开始；
当 $1\le j<m$ 时 $m-1\ge m-j$，所以不需要知道 $[L^j]E_4$ 的具体值。
三次项及余项分别从 $H^{m-j}$、$H^m$ 开始，得到

$$
[L^j]S\in h^{m-j}\mathcal O^+\quad(1\le j<m).
$$

纯常数仍保留全部同阶项：

$$
(2\chi)^3\frac{3\chi}{32}+(2\chi)^4\left(-\frac3{32}\right)=-\frac34,
\qquad S(0)=-\frac34h^{m-1}+O(h^m).
$$

有限域系数作任意整提升的差为 $p$ 倍，落入同一实际误差以上。
再调用原首层单位 $a_m$ 与 $e_*=M-D\ge m$ 的首一商转移，
即可原样得到正因子 $b_0=16\chi h^{m-1}+O(h^m)$、$b_j\in h^{m-j}$。
这一段不使用 $E_4$ 的正参数闭式，且在 $p=5,a=2$ 仍成立。$\square$

## Replacement Boundary and Open Risks

本件实质移除了当前正簇接口对 A10 Step 4 全参数奇矩／二次分母求值的依赖，
并将其 Steps 2–3 的一般参数消元限制为一个直接标量配对。
全参数单位性、真实三次与四次组成量、有限配对合法性和实际误差仍保留。
它不取代 A07 的实际 action、两种真实缺陷、合法移位、首层单位或 A06 的实际桥。

尚须两项不同检查：本件新数学的非作者核查；其他当前消费者是否也只需 (1) 的依赖检查。
在完成之前，不宣称 A10 已从当前必要证明链整体删除，不更新容量，不创建稿件。
原完整显式 $E_4(L)$、旧作者源、独审与失败记录全部保持。
没有缩小当前科学量词，没有证明负分裂域、下一阶根平移、最终共振或实根结论。
作者另直接构造 $p=5,7,11,13,17,19$ 的有限三角响应，核对 (7) 与原始端点 (10)，
均匹配 $-3/32$；这只作有界公式一致性检查，不承担普遍量词或非作者审查。
没有根扫描、测页、Route或外部操作。
