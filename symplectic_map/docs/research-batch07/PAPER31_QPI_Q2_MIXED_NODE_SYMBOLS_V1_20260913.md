# Paper31 Q2：完整 saddle 圆的混合导数与可微符号 V1

日期标签：2026-09-13。作者：/root/p31_q2_mixed_node_proof。
状态：AUTHOR_PROOF_COMPLETE / FRESH_ACTUAL_REVIEW_PENDING。
本件使用 proof-writer；只读协作核对：node_implicit_bound_check，不充当独立数学验收或正式准入票。
固定原 qPI 的任意 $T>0$，保留完整圆、saddle 与四条 terminal；无 CAS、数值、扫描或 LaTeX。

## Claim

记 $e=h-h_+$，$\ell(e)=1+\log(1/|e|)$。充分缩小 $\delta\in(0,1)$ 后，
在每个单侧 $0<\pm e<\delta$ 的每条完整圆分支 $\Gamma_e$ 上，存在正向 Hamilton 角参数

$$z(e,\theta)=\phi_X^{\theta L(e)}z_0(e),\qquad \theta\in\mathbb R/\mathbb Z,$$

其中 $z_0(e)$ 是延至 $e=0$ 正则点的固定解析横截面，$L(e)$ 为完整正周期。
存在固定紧能窗 $K\subset U$，使对任意整数 $a,b\ge0$，有与 $e,\theta,f$ 无关的常数 $C_{a,b}$ 满足

$$\sup_\theta\left|\partial_e^a\partial_\theta^b(f\circ z)(e,\theta)\right|
\le C_{a,b}|e|^{-a}\ell(e)^{a+b}\|f\|_{C^{a+b}(K)}.\tag{C1}$$

有限阶情形只要求原曲面上的 $f$ 在 $K$ 邻域属于 $C^{a+b}$；不要求 $\Pi f$ 仍为原光滑函数。
以 $\widehat f_k(e)=\int_0^1 f(z(e,\theta))e^{-2\pi i k\theta}\,d\theta$ 定义 Fourier 系数，则对全部整数 $k\ne0$、$a,s\ge0$，

$$|\partial_e^a\widehat f_k(e)|
\le C_{a,s}\|f\|_{C^{a+s}(K)}|e|^{-a}\ell(e)^{a+s}|k|^{-s}.\tag{C2}$$

特别地，这不是固定 $k$ 或删去节点带后的估计。中心化不改变这些非零系数。
沿 [N] 的同一个有界解析时间提升 $\tau(e)$，置 $\alpha(e)=\tau(e)/L(e)$。
在上述缩小后的单侧区间有 $\alpha'(e)\ne0$，且 $Q(e)=1/\alpha'(e)$ 满足

$$|\partial_e^a Q(e)|\le C_a |e|^{1-a}\ell(e)^2,\qquad a\ge0.\tag{C3}$$

所有常数允许依赖固定 $T$、所选紧能窗、固定横截面与阶数；不宣称关于 $T$ 的一致性。

## Status

**PROVABLE AS STATED。** 原完整曲面与原观测类不变；相位起点是证明中主动构造的合法 gauge，
不是给任意剧烈依赖能量的相位 gauge 都赋予 (C1)。本件不单独声称完整相关衰减率、最优性或长文容量。

## Assumptions and notation

1. 消费 [D] 已数学接受的 [M]、[N]，不重开这些接受结果。$F$ 是原完整 $U$ 上的自同构，
   $h$ proper，$\iota_X\Omega=-dh$，$d\mu=L(e)\,de\,d\theta$。
2. [N, §2] 给 saddle 的解析 Morse 图 $e=pq$、$\Omega=-a_0(p,q)\,dp\wedge dq$，
   $a_0>0$，$X=(p\partial_p-q\partial_q)/a_0$。此处将其密度重命名为 $a_0$，避免与导数阶数 $a$ 混淆。
3. 完整圆由有限次穿过固定 Morse 箱和有限条箱外紧正则弧组成。
   上侧两圆每圆穿箱一次，下侧一圆穿箱两次；分支及轨道段的次序在各单侧固定。
4. [N, §§2–3] 给

   $$L(e)=A(e)\log(1/|e|)+B(e),\quad A(0)=m/\kappa>0,\quad
   F^2|_{\Gamma_e}=\phi_X^{\tau(e)}|_{\Gamma_e},\quad\tau(0)>0,$$

   其中 $A$ 解析，$B$ 在相应一侧解析延至零，$\tau$ 双侧解析；$m=1$ 或 $2$。
5. $D=e\partial_e$ 总是表示固定归一化角度时的 Euler 导数；$D_0=e\partial_e|_u$ 表示固定下述箱内变量 $u$ 时的导数。
   原 $C^r(K)$ 范数使用覆盖固定紧能窗的有限原光滑坐标图；所有相应固定坐标变换的有限阶导数有界。

## Proof strategy and dependency map

先在箱内使用 $u=\log|p|$，把危险的横向微分写成有界的 $q\partial_q$，
把穿箱时间变成长度为 $O(\ell)$、积分核所有混合导数有界的积分。
随后用时间方程的隐函数求导控制固定归一化角度的轨道位置。
箱外只用统一有限时间的正则流图；人工接缝在重叠图中核对，不微分移动的分段特征函数。

依赖顺序是：

1. [M] 的 proper 紧能窗与 terminal 正则性、[N] 的真实箱／弧分解，给有限图和固定横截起点。
2. 箱内移动端点引理，加 [N] 的周期可微展开，给归一化时间隐函数的混合导数。
3. 隐函数归纳及正则弧短时流图，给完整圆上的 (C1)。
4. (C1) 加周期分部积分，给全部非零模的 (C2)。
5. [N] 的同一 $L,\tau$ 的解析展开，直接给 (C3)。

## Proof

### Step 1. 固定起点和有限轨道段

固定一个单侧及一条圆分支。在其极限 separatrix 正则弧上取一点和固定解析横截面。
因 $dh\ne0$，解析隐函数定理给该截面上以 $e$ 为参数的 $z_0(e)$，并解析延至零。
用正向 Hamilton 流定义声明中的 $z(e,\theta)$。每个 $e\ne0$ 的圆上 $X$ 无零点且周期为 $L(e)$，
故这是周期角参数；有限时流对参数光滑，说明它在每个 $e\ne0$ 附近关于 $(e,\theta)$ 光滑。
此处只用这一局部光滑性，不从长时间流的粗糙变分估计推导统一界。

选定 $0<r<R$，使闭大箱 $|p|,|q|\le R$ 严格落在 Morse 图内，且 $a_0\ge c_*>0$。
以小箱 $|p|,|q|\le r$ 划分穿箱段和箱外弧，缩小 $\delta$ 使 $|e|<r^2/4$。
取 $K=h^{-1}([h_+-2\delta,h_++2\delta])$；[M] 的 proper 性保证它紧，且它包含全部当前轨道段及所需小延拓。
入口、出口远离箱角且对 $X$ 横截；箱外极限弧紧且无零点。
解析流的局部存在、对初值的解析依赖及入口／出口横截性，使各箱外穿越时间解析延至 $e=0$。
有限条段的总数量与次序由 [N] 的真实圆分解固定。

从 $z_0(e)$ 到任一段起点的累计正时间 $c_j(e)$ 是有限个完整穿箱时间与正则弧时间的和。
[N] 的逐箱展开于是给对每个整数 $j_1\ge0$ 的界

$$|D^{j_1}L(e)|+|D^{j_1}c_j(e)|\le C_{j_1}\ell(e).\tag{1.1}$$

可以在基点切开一条箱外弧；被切开的两段仍是解析有限时间段，故不改变 (1.1)。

### Step 2. 穿箱时间的所有移动端点导数

在某次穿箱中固定 $\sigma=\operatorname{sgn}p$，令

$$p=\sigma\exp(u),\qquad q=\sigma e\,\exp(-u),\qquad
u_0(e)=\log|e|-\log r,\quad u_1=\log r.$$

实际段的 $u$ 从 $u_0(e)$ 增至 $u_1$。
定义 $H(e,u)=a_0(\sigma\exp(u),\sigma e\,\exp(-u))$。作用在原坐标函数上有

$$D_0=q\partial_q,\qquad \partial_u=p\partial_p-q\partial_q.$$

两算子对易；在闭大箱上其任意有限复合的系数和作用于解析密度所得函数都一致有界。
因此对所有 $i,j\ge0$，在小箱段及稍许物理延拓上有

$$|D_0^i\partial_u^j H(e,u)|\le C_{i,j},\qquad H(e,u)\ge c_*.\tag{2.1}$$

从入口到当前点的时间为 $I(e,u)=\int_{u_0(e)}^u H(e,v)\,dv$。
其积分长度至多 $C\ell$。固定 $u$ 的一次 Euler 微分给

$$D_0I(e,u)=\int_{u_0(e)}^u D_0H(e,v)\,dv-H(e,u_0(e)).\tag{2.2}$$

高阶移动端点不能只靠微分一个裸 $O(\ell)$。
这里 $Du_0=1$，而沿入口的总导数作用在积分核上为
$D_0+\partial_u=p\partial_p$：入口的 $q=\sigma\operatorname{sgn}(e)r$ 固定，$p=\sigma|e|/r$。
更明确地，记 $\mathcal T_0 B=B(e,u_0(e))$、$E_0=D_0+\partial_u$，则
$D(\mathcal T_0 B)=\mathcal T_0(E_0B)$，逐阶微分 (2.2) 给对 $i\ge1$

$$D_0^i I=\int_{u_0}^uD_0^iH\,dv
-\mathcal T_0\!\left(\sum_{j=0}^{i-1}E_0^{i-1-j}D_0^jH\right).$$

所得入口项由 (2.1) 一致有界；公式也完整计入二阶及更高阶的移动端点项。
由此对所有 $i\ge0$，$|D_0^i I|\le C_i\ell$。
对上端变量至少微分一次，则基本积分公式给 $\partial_u I=H$，再由 (2.1) 得

$$|D_0^i I(e,u)|\le C_i\ell,\qquad
|D_0^i\partial_u^jI(e,u)|\le C_{i,j}\quad(j\ge1).\tag{2.3}$$

令 $S(e,u)=c_j(e)+I(e,u)$ 为从所选起点累计的时间。
结合 (1.1)，(2.3) 对 $S$ 仍成立，且 $S_u=H\ge c_*$。

### Step 3. 归一化时间隐函数的混合导数

在该轨道段上，以一个有界的局部角度 lift $\vartheta=\theta+\nu$ 写

$$S(e,u(e,\theta))=\vartheta L(e),\tag{3.1}$$

其中整数 $\nu$ 在当前重叠图上固定，可始终令 $|\vartheta|\le2$。
因为 $S_u\ge c_*$，隐函数定理适用。一次导数为

$$D u=\frac{\vartheta DL-D_0S}{S_u},\qquad
\partial_\theta u=\frac{L}{S_u},\tag{3.2}$$

故两者均为 $O(\ell)$，没有额外负幂的能量损失。
现在对总阶 $n=a+b\ge1$ 归纳证明

$$|D^a\partial_\theta^b u|\le C_{a,b}\ell^{a+b}.\tag{3.3}$$

将 $D^a\partial_\theta^b$ 作用于 (3.1)。链式法则中唯一包含最高阶未知导数的项是
$S_uD^a\partial_\theta^b u$。其余项有两类：
不含 $u$ 的导数的纯 $D_0^nS$ 项至多为 $O(\ell)$；
包含 $u$ 的导数时，系数至少带一次 $u$ 微分，故由 (2.3) 有界，
并乘有限个低于 $n$ 阶的 $u$ 导数，其总微分阶数不超过 $n$。
归纳假设将每个此类乘积控制为 $O(\ell^n)$。
右端 $D^a\partial_\theta^b(\vartheta L)$ 由 (1.1) 为 $O(\ell)$，或当 $b\ge2$ 时为零。
除以有正下界的 $S_u$ 后得到 (3.3)，完成所有有限阶的归纳。

恢复原坐标时，一次导数有

$$Dp=pDu,\quad \partial_\theta p=p\partial_\theta u,\qquad
Dq=q(1-Du),\quad \partial_\theta q=-q\partial_\theta u.$$

进一步的任意混合导数始终是 $p$ 或 $q$ 乘以 $u$ 的有限 jet 的多项式，
多项式各项的总微分阶数不超过所求阶数。
因为 $|p|,|q|\le R$，(3.3) 给全部原坐标导数的 $O(\ell^{a+b})$ 界。
这里没有除以趋零的 $p$ 或 $q$，也没有用 $e^{-Ca}$ 的长时间 ODE 界冒充 $e^{-a}$。
链式法则遂给箱内

$$|D^a\partial_\theta^b(f\circ z)|
\le C_{a,b}\ell^{a+b}\|f\|_{C^{a+b}(K)}.\tag{3.4}$$

### Step 4. 箱外正则弧、移动接缝和周期接缝

每条箱外极限正则弧都在有限 Hamilton 时间内运行。
从该弧入口定义 $Z_j(e,t)$；在 $e=0$ 时这条弧紧且远离临界点，
故有限流图覆盖和流的参数依赖给一个延至 $e=0$、$t$ 区间统一有界并向两端略延长的解析 $Z_j$。
其所需有限阶导数一致有界；途经 terminal 时使用 [M] 的原正则图，结论不变。
当前点可以写为

$$z(e,\theta)=Z_j(e,t(e,\theta)),\qquad
t(e,\theta)=\vartheta L(e)-c_j(e).$$

由 (1.1)，$t$ 的任意正阶 $D,\partial_\theta$ 混合导数是 $O(\ell)$，而 $t$ 本身在固定有界区间。
对 $Z_j$ 使用链式法则，每个总阶 $n$ 项至多含 $n$ 个此类因子，
得到与 (3.4) 相同的 $O(\ell^n)$ 原范数界。

上述分段只用于估计同一个已经定义的光滑参数 $z(e,\theta)$，没有乘分段特征函数。
在箱入口或出口附近，将箱坐标延入 $r<|p|<R$ 或 $r<|q|<R$ 的固定物理小条带；
相邻正则流图也作固定短时间延拓，两表达在非空开重叠上表示同一条轨道。
(2.1)–(2.3) 在这种延拓上继续成立：若 $u$ 稍低于入口，积分只增加固定长度的反向短段。
因此任一人工接缝点附近都有满足统一估计的开图。
重叠的角宽可以随能量缩成 $O(L^{-1})$；点态导数界不需要统一正的角宽，也不对这个宽度求倒数。
由相同光滑映射在开重叠上的相等，接缝两侧全部实际导数一致。

最后，$\theta=0=1$ 的接缝位于选择的正则基点图内。
在两侧分别用 $Z_0(e,\theta L)$ 与 $Z_0(e,(\theta-1)L)$，
其中 $Z_0(e,t)$ 允许基点附近的正、负短时间。
周期恒等式 $\phi_X^{L(e)}z_0(e)=z_0(e)$ 说明这两个局部表示是同一圆上参数；
采用圆的局部 lift 后其全部导数一致。改变 lift 只添加局部固定整数倍的 $L$，仍受 (1.1) 控制。
故 (3.4) 在整个圆成立，且没有因移动接缝丢失能量导数。

### Step 5. 普通能量导数与全部 Fourier 模

对 $a\ge1$，Euler 导数满足精确算子恒等式

$$e^a\partial_e^a=D(D-1)\cdots(D-a+1).\tag{5.1}$$

因 $D$ 与 $\partial_\theta$ 对易，(3.4)、$\ell\ge1$ 和 (5.1) 直接给 (C1)，
$a=0$ 情形已经包括在 (3.4) 中。
对每个 $e\ne0$，紧角圆上的有限阶参数微分允许交换积分与 $\partial_e^a$。
再在角圆上分部积分 $s$ 次，所有周期边界项都消失，得到

$$\partial_e^a\widehat f_k(e)
=(2\pi i k)^{-s}\int_0^1
\partial_e^a\partial_\theta^s(f\circ z)(e,\theta)e^{-2\pi i k\theta}\,d\theta.$$

代入 (C1) 即得 (C2)。常数不依赖 $k$，所以它确实控制全无限 Fourier 族。
[N] 在 $a=0$ 时另有较尖的 $L^{-1}$ 与 $L^{s-1}|k|^{-s}$ 双界；
这里不替换或否定那些界，只补齐任意能量微分所需的可微界。

为明确给后续相关积分的接口，若 $\chi$ 是固定单侧光滑能量截断且导数有界，置
$b_k(e)=\chi(e)L(e)\widehat f_k(e)\overline{\widehat g_k(e)}$。
Leibniz 公式、$|\partial_e^jL|\le C_j|e|^{-j}\ell$ 与 (C2) 给

$$|\partial_e^a b_k(e)|\le
C_{a,s,\chi}\|f\|_{C^{a+s}(K)}\|g\|_{C^{a+s}(K)}
|e|^{-a}\ell^{a+s+1}|k|^{-s}.\tag{5.2}$$

例如将 $|k|^{-s}$ 的界用于 $f$ 因子、$s=0$ 的界用于 $g$ 因子即可；
落到 $L$ 或 $\chi$ 上的导数不会增加右端对数指数。
这仍是符号估计，不把其后的能量分部积分或求和证明预先记为完成。

### Step 6. 原离散相位的倒导数符号

写 $l=\log(1/|e|)$。由已接受的解析展开，$L=Al+B$ 且
$DL=eA'l-A+eB'$。
定义

$$R(e)=(D\tau)L-\tau DL
=\tau A+e(\tau'A-\tau A')l+e(\tau'B-\tau B').\tag{6.1}$$

于是 $R(e)\to\tau(0)A(0)>0$。
任意有限阶 $D$ 作用于 $e$ 乘解析函数乘 $l$ 后仍是此种形式，且 $|e|l$ 在零附近有界；
所以 $|D^jR|\le C_j$，并可缩小 $\delta$ 使 $R\ge c_R>0$。
微分 $R\cdot R^{-1}=1$ 逐阶归纳，得到 $|D^j(R^{-1})|\le C_j$。
另一方面，(1.1) 给 $|D^j(L^2)|\le C_j\ell^2$，故
$|D^j(L^2/R)|\le C_j\ell^2$。

直接计算同一个原相位得

$$\alpha'(e)=\frac{R(e)}{eL(e)^2},\qquad
Q(e)=\frac{eL(e)^2}{R(e)}.\tag{6.2}$$

这同时证明 $\alpha'$ 非零及其符号等于 $e$ 的符号。
把 (5.1) 用于 $Q=e(L^2/R)$，或将 $D(eH)=e(D+1)H$ 逐次代入，得到

$$\partial_e^a Q
=e^{1-a}(D+1)D(D-1)\cdots(D-a+2)(L^2/R)\quad(a\ge1).$$

当 $a=1$ 时右端乘积仅为 $(D+1)$；更统一地它是
$e^{1-a}\prod_{j=0}^{a-1}(D+1-j)(L^2/R)$。
连同 $a=0$ 的 (6.2)，上述 $D$ 界给 (C3)。
该符号源自 [N] 的同一完整周期与同一有界提升；没有拼接不同圆的有利相位或另换常数时间流。
至此 (C1)–(C3) 全部成立。$\square$

## Corrections or missing assumptions

无新增科学假设或观测缩限。必须保留的相位选择条件已在 Claim 与 Step 1 明示：
任取在穿孔能区间光滑但旋转极快的 gauge 会使能量导数失控，故本命题量词是“存在固定正则横截面给出的角度”。
各单侧、各圆可分别选择这样的起点；Fourier 相关乘积的共同 gauge 因子相消。

## Open risks and boundary

- 本件是作者完整证明，仍待 fresh actual 数学检查；只读协作者不是正式准入席。
- 只证明节点混合导数、全模符号与 $1/\alpha'$ 符号；尚未在本件证明任意次能量分部积分的可积性、边界消失和完整相关渐近。
- 不把 $\Pi f$ 当原光滑函数；(C2) 直接对原 $f$ 证明，中心化只删除零模。
- 不声称 $z$ 或其角度延至节点光滑；对数增长允许且确实必要。
- 不作关于 $T\to0,1,\infty$ 的一致估计，不改变 P31 页数或任何旧 FAIL／STOP；本件不构成新意、容量或 Route A/B 票。

## Read scope

完整读取：proof-writer 的 SKILL.md（223 行）、[D]（118 行）、[N]（238 行）、[M]（128 行）。
本件只消费它们明确给出的已接受输入；未另称亲读其历史引用全文，也未作新的外部文献结论。

[D]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
