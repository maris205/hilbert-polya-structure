# Proof Package：第三内部 forcing 的完整 Newton 图、因子次数与两两互素

日期：2026-09-08。作者：主控。
使用 `proof-writer`。本件合并同一实际分支的已接受系数区间与同轮新非零锚点，
并证明第二／第三 forcing 的新互素推论；没有拼接不同构造的最优结果。

## Claim

固定任意素数 $p\ge5$、整数 $a\ge2$，取任意本原 $p^a$ 次根 $\zeta$，令

$$h=2-\zeta-\zeta^{-1},\quad K^+=\mathbb Q_p(h),\quad
\mathcal O^+=\mathbb Z_p[h],\quad v_h(h)=1,$$
$$m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad
D=p+m=3m+1,\quad e_*=M-D,\quad \chi=(-1)^{m+1}.$$

保持实际双谐波递推、固定参数和 SUM action，定义

$$\mathcal B_k(L)=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V},\quad k=1,2,3,$$

其中各项只用相应下标以下的真实分支。令

$$S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
U_{\rm cl}=\sum_{r=0}^{p}u_rL^r.$$

则第三 forcing 的负因子有单条准确 Newton 边

$$\boxed{\operatorname{NP}(U_{\rm cl}):(0,0)\longrightarrow(p,M-m),
\qquad v_h(\beta)=-(M-m)/p\quad(U_{\rm cl}(\beta)=0).}\tag{1}$$

$U_{\rm cl}$ 在 $K^+[L]$ 上不可约且可分。合并已接受正因子，
$S$ 的完整 Newton 图恰为两条边

$$\boxed{(0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m).}\tag{2}$$

因此 $\mathcal B_3$ 在 $K^+$ 上恰有两个不可约因子，次数分别为 $m,p$，
且自身可分。三个内部 forcing 两两互素：

$$\boxed{\gcd(\mathcal B_i,\mathcal B_j)=1
\quad(1\le i<j\le3).}\tag{3}$$

每个负根生成一个次数 $p$、全分歧的野扩张 $F_\beta=K^+(\beta)$。
若 $E$ 为既有正因子的循环分裂域，则

$$[EF_\beta:K^+]=e(EF_\beta/K^+)=mp,\qquad f(EF_\beta/K^+)=1.\tag{4}$$

本件不声称不同负根生成同一个域，不识别负因子的完整分裂域或其 Galois 群。
任意参数的点值式另在 Step 5 精确列出，负临界圈保留完整距离和。

## Status

`PROVABLE AS STATED`：以下给出合并结构及新互素推论的完整作者证明。
新的最高系数计算及本稿仍须各自非作者独审后，由主控作本轮接受处置；
本件不会自行把同轮作者完成状态记作独审接受。

## Assumptions and exact inputs

1. [已接受上半段、分界及二次边界处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_BOUNDARY_AND_QUADRATIC_DISPOSITION_20260908.md)
   给唯一首一分解、$\deg P_{\rm cl}=m$、$\deg U_{\rm cl}=p$、$u_0$ 为单位，以及
   $$v_h(u_r)\ge M-p\ (1\le r\le m),\qquad
   v_h(u_r)\ge M-m-1\ (m+1\le r<p).\tag{5}$$
2. [同轮新最高系数证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md)
   合并第一 forcing 次层与有限参照首误差，给出
   $$pC_D=-\frac3{16}h^p+O(h^{p+1}),\qquad C_D=[L^D]\mathcal B_3.\tag{6}$$
   这是本件的新作者输入；其独审与两份输入的独审分开进行。
3. [已接受统一正簇稿](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md)
   式 (25) 及后续因子论证给
   $$u_0=-3\chi/64+O(h),\quad P_{\rm cl}(0)=16\chi h^{m-1}+O(h^m).\tag{7}$$
   其正因子不可约可分，全部根 $\alpha_j$ 及两不同根之差的赋值为
   $t_+=(m-1)/m$，分裂域 $E/K^+$ 为次数 $m$ 的全分歧循环扩张。
   这些已接受结论与正簇距离式不重开。
4. [已接受第二内部层处置](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)
   给逐系数整性与准确常数剩余
   $$h^{-2m}p\mathcal B_2\in\mathcal O^+[L],\qquad
   \overline{h^{-2m}p\mathcal B_2}=2,\qquad
   \gcd(\mathcal B_1,\mathcal B_2)=1.\tag{8}$$
5. [第一内部局部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
   的形式整除身份及根结构给
   $$\mathcal B_1(H,0)=2\chi H^m+O(H^{m+1})\quad\text{模 }p,$$
   且 $\mathcal B_1$ 的全部根在 $L$ 坐标的赋值为零。
   同一纯偶倍角身份可见[分界高系数稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md)
   的 Step 4；下面重新核对本件所需缩放。

以上皆为同一实际 $h=D_1$ 规范，不调用旧分母 $2p$ 的 $h=D_2$ 结果。

## Proof strategy and dependency map

准确最高高度与中间区间的严格弦上不等式给单边及全部根赋值；
分母 $p$ 强制不可约及全分歧。
第二／第三 forcing 互素不能只用次数小于 $p$：第二 forcing 的次数确可达 $p$。
本件计算其最高项，并以最高项／常数项之比排除与负因子成比例。
最后合并已接受正因子与单位圈结果，给完整因子型和点值公式。

## Proof

### Step 1. 准确最高高度与弦上不等式

因 $P_{\rm cl}$ 首一，准确有 $u_p=h^{-D}p^2C_D$。
式 (6) 因而给

$$u_p=-\frac3{16}p h^{-m}(1+O(h)),\qquad v_h(u_p)=M-m.\tag{9}$$

这里 $3,16$ 是单位，$O(h)$ 表示相对误差。令 $b=M-m$，$t_-=-b/p$。
有 $e_*=M-p-m>0$，且

$$\frac{M-p}{m}-\frac bp=\frac{(p-m)e_*}{mp}>0,\qquad
\frac{M-m-1}{p-1}-\frac bp=\frac{e_*}{p(p-1)}>0.\tag{10}$$

由式 (5)、(10)，每个 $0<r<p$ 的点满足 $v_h(u_r)>rb/p$。
端点高度分别为 $0,b$，故下凸包恰为式 (1) 的单条边。

也可直接验证根赋值，无须从系数下界猜测等号。
若 $t=v_h(\beta)>-b/p$，常数项是 $U_{\rm cl}(\beta)$ 唯一最低项。
若 $t<-b/p$，对 $0<r<p$ 有

$$v_h(u_r\beta^r)-(b+pt)
=\left(v_h(u_r)-\frac{rb}{p}\right)+(r-p)\left(t+\frac bp\right)>0,$$

常数与最高项之差也严格为正。因此最高项唯一最低。
两种情况都不能给根，所以全部根必须满足 $v_h(\beta)=-b/p$。

### Step 2. 不可约性、可分性及根生成域

由于 $p\mid M$ 且 $0<m<p$，$\gcd(p,b)=1$。
若 $U_{\rm cl}$ 有次数 $0<d<p$ 的 $K^+$ 因子，
将该因子的常数项除以首项，其赋值应为一个整数；
按其全部 $d$ 个根的乘积，这个赋值又是 $-db/p$，并非整数。
矛盾，故 $U_{\rm cl}$ 不可约。特征零保证不可约多项式可分。

任意 $F_\beta/K^+$ 的次数因此为 $p$。其值群含 $-b/p$，
而基域值群为 $\mathbb Z$，故分歧指数是 $p$ 的倍数。
分歧指数不超过扩张次数 $p$，所以 $e=p$；局部域次数公式再给剩余次数 $f=1$。
因剩余特征为 $p$，这是野全分歧扩张。

既有 $E/K^+$ 为 Galois 扩张、次数 $m$，与 $p$ 互素。
交域次数同时整除 $m,p$，所以交域为 $K^+$；Galois 性给线性无交，
从而 $[EF_\beta:K^+]=mp$。
合域的分歧指数同时被 $m$ 与 $p$ 整除，又不超过 $mp$，
故它为 $mp$，剩余次数为一，证明式 (4)。

### Step 3. 第二 forcing 的真实最高项

齐次性使 $\deg_L V_n\le\lfloor n/2\rfloor$，由实际递推按 $n$ 归纳即可。
因此 $\mathcal B_2$ 第一项的次数至多为 $p-1$，第二项因外乘 $L$，次数至多为 $p$。
不能把后者漏计。它的 $L^p$ 系数只取纯偶块，准确为

$$[L^p]\mathcal B_2=-2\,4^{-(p-1)}[u^{p-1}]e^{2W(H,u)}\big|_{H=h}.\tag{11}$$

这些 $W_r$ 只用 $r<p$，其实际原下标 $2r$ 不被 $p$ 整除，全部形式整。
设 $P_0(H,x)$ 为相同低递推在 $L=0$ 的解，$H_2=H(4-H)$、$c=16/(4-H)$。
Chebyshev 倍角准确给 $d_{2r}(H)=(4-H)d_r(H_2)$，所以

$$W(H,u)=\frac12P_0(H_2,cu)\pmod{u^p}.\tag{12}$$

核准常数的方法是将右端代入纯偶方程：左端变为
$-(4-H)c^r[x^{r-1}]e^{P_0}/4$，而右端要求
$-4c^{r-1}[x^{r-1}]e^{P_0}$；二者由 $(4-H)c=16$ 相等。
低单位三角唯一性保证式 (12) 是同一纯偶块，不是另一个构造。
由第一 forcing 在 $L=0$ 的定义，得到

$$[u^{p-1}]e^{2W}=-c^{p-1}\mathcal B_1(H_2,0).$$

将其代回式 (11)，有准确身份

$$[L^p]\mathcal B_2
=2\left(\frac4{4-h}\right)^{p-1}\mathcal B_1(h(4-h),0).\tag{13}$$

第一 forcing 的已接受形式首层、$M\ge m+1$ 及 $4^m=1$ 模 $p$ 给出

$$\boxed{[L^p]\mathcal B_2=4\chi h^m+O(h^{m+1}).}\tag{14}$$

特别地它非零，$\deg\mathcal B_2=p$。
这只是最高项及次数，不推出第二 forcing 的完整 Newton 图或简单性。

### Step 4. 两两互素与第三 forcing 的完整因子型

式 (8) 保证 $\mathcal B_2$ 在任意有限扩域中的整参数处均不为零，
而 $P_{\rm cl}$ 的全部根具有正赋值。因此它与正因子互素。
若它与 $U_{\rm cl}$ 有共同根，由 $U_{\rm cl}$ 不可约且两者次数均为 $p$，
必有 $\mathcal B_2=cU_{\rm cl}$ 对某个非零 $c\in K^+$。
于是两者的最高系数／常数系数比必须相等。

然而，由式 (8)、(14) 得

$$\frac{[L^p]\mathcal B_2}{\mathcal B_2(0)}
=2\chi p h^{-m}(1+O(h));$$

由式 (7)、(9) 得

$$\frac{u_p}{u_0}=4\chi p h^{-m}(1+O(h)).\tag{15}$$

将二式之差除以非零公共尺度 $\chi p h^{-m}$，剩余为 $2-4=-2\ne0$。
故不能成比例，证明 $\gcd(\mathcal B_2,U_{\rm cl})=1$，从而
$\gcd(\mathcal B_2,\mathcal B_3)=1$。

$\mathcal B_1$ 全部根的赋值为零，第三 forcing 的根赋值只为 $t_+>0$ 与 $t_-<0$，
所以第一／第三 forcing 也互素。第一／第二互素已由式 (8) 接受。
三项合并得到式 (3)。

正、负因子均不可约可分，且其根赋值不同。因此它们互素，
第三 forcing 恰有这两个不可约因子，次数 $m,p$，自身可分。
两个因子的 Newton 斜率分别为 $-(m-1)/m$ 与 $b/p$，
给完整 $S$ 图的式 (2)。这也可由下节在两临界赋值以外的唯一最低项直接读出。

### Step 5. 全参数点值式及负临界圈边界

记负根为 $\beta_1,\ldots,\beta_p$，正根为 $\alpha_1,\ldots,\alpha_m$。
对任意有限扩域中的非零参数 $\ell$，令 $t=v_h(\ell)$。
因 $P_{\rm cl}$ 首一且负因子首系数高度为 $b$，准确乘积身份给

$$v_h(U_{\rm cl}(\ell))=b+\sum_{k=1}^p v_h(\ell-\beta_k).\tag{16}$$

当 $t<t_-$ 时每个差的赋值为 $t$，故该式为 $b+pt$；
当 $t>t_-$ 时每个差的赋值为 $t_-$，故它为零。
合并既有正簇距离式，可得完整分段身份

$$\boxed{v_h(S(\ell))=
\begin{cases}
Dt+b,&t<t_-,\\
mt_-+b+\displaystyle\sum_{k=1}^p v_h(\ell-\beta_k),&t=t_-,\\
mt,&t_-<t<t_+,\\
(m-1)t_++\max_jv_h(\ell-\alpha_j),&t=t_+,\\
m-1,&t>t_+.
\end{cases}}\tag{17}$$

$\ell=0$ 时值为 $m-1$；根处允许 $+\infty$。
负临界圈不是单位值区间：这里保留完整距离和，未将其偷换为未经证明的单个最大距离。
所有负根两两距离的准确值及负分裂域仍未由式 (17) 决定。
实际换算保持

$$v_h(\mathcal B_3(\ell))=D-2M+v_h(S(\ell)),\qquad
v_h(V_{3p}(\ell))=m+1-2M+v_h(S(\ell)).$$

这证明全部主张。$\square$

## Corrections or Missing Assumptions

主控在写稿前曾向协作者提示“第二 forcing 次数小于 $p$”；
实际权重检查发现外部 $L$ 使次数可达 $p$，该草算不能用于互素证明。
本稿从式 (11)—(15) 正面处理真实次数 $p$，以不同的准确系数比排除成比例。
未将错误次数放入冻结稿或据此登记接受结论。

新非零锚点是 $h^{-p}pC_D=-3/16+O(h)$，不把 $4^D$ 误当作 $16$。
第二 forcing 的旧常数单位式与最高项精度都按实际 $h=D_1$ 规范使用。

## Open Risks and non-claims

新的最高项输入及本稿须完成各自非作者独审；此作者状态不替代验收。
本件闭合的是第三内部 forcing 的完整局部 Newton 图和因子次数，
不是完整周期 $p^a$ 的最终 forcing $C,Q$ 或全部合数的实根分类。
第二 forcing 的完整负 Newton 图、其简单性、负根间距与第三负因子的野分裂域仍未求出。
不声称负根生成的次数 $p$ 域为循环、Galois 或彼此相同。
本件没有 Paper30 立项、容量评分、稿件、PDF、Route 或对外效力。
