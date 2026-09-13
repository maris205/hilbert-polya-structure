# Proof Package：负端有限系统的参数化交叉伴随

日期：2026-09-08。作者：主控。
使用 `formula-derivation` 固定同一完整二次端点，再用 `proof-writer` 证明。
本件是新作者证明；非作者审查与采用处置另记，不修改任何旧稿或接受记录。

## Claim

固定任意素数 $p\ge5$，令 $m=(p-1)/2$，工作环为
$R=\mathbb F_p[H]/(H^2)$。保持实际最高参数提取所用坐标 $u=Lx^2/4$。
以本文低方程定义有限 $w,a$，并令

$$
\Theta=u\partial_u,\qquad \mathcal Q=2\Theta+1,
\qquad f_1=e^w,\quad f_2=e^{2w},
$$
$$
\mathcal L_e=\mathcal D_e+8uf_2,\qquad
\mathcal L_o=\mathcal D_o+8uf_2,\qquad
\mathcal K=f_1/2+16uf_2a.
$$

对任意 $X\in uR[u]/(u^{m+1})$、$Y\in R[u]/(u^m)$，记
$P=\mathcal L_eX$、$Q=\mathcal L_oY+\mathcal KX$，各在相应有限范围解释。
则完整端点具有参数化恒等式

$$
\boxed{
\begin{aligned}
\mathcal C_H(X,Y)
&=-[u^m]f_1X-16[u^{m-1}]f_2(Y+2aX)\\
&=2[u^m](\mathcal Qa)P+4[u^m](\Theta w)Q
\qquad\text{于 }R.
\end{aligned}}
\tag{1}
$$

式 (1) 同时保留低带、伴随权重和端点乘积的 $H$ 一次变化。
应用于原实际二次响应系统时，它允许在不求 $X_0,Y_0,X_1,Y_1$ 显式解的情况下
计算两个二次端点系数；本件只证明这个通用恒等式与实际系统的接口，
不在此预设端点值 $0,-1/2$。

## Status

`PROVABLE AS STATED`，作者证明完成，等待真正非作者审查。
式 (1) 是有限域参数商环身份，不是特征零恒等式，也不声称模 $H^3$ 成立。
最终科学量词、实际模型与目标精度没有削弱；模 $H^2$ 只是乘 $H^{2m}$ 的内部接口。

## Assumptions and notation

整数 Chebyshev 多项式由 $C_n=z^n+z^{-n}$、$H=2-z-z^{-1}$ 定义，
取 $d_n(H)=(C_n(H)-2)/H$，特别地 $d_0=0$；
另记 $S_n(H)=(z^n-z^{-n})/(z-z^{-1})$，这是整数 Chebyshev 多项式。
有限对角算子为

$$
\mathcal D_eu^j=d_{2j}(H)u^j\quad(1\le j\le m),
\qquad
\mathcal D_ou^j=d_{2j+1}(H)u^j\quad(0\le j<m).
\tag{2}
$$

低带由单位三角方程准确确定：

$$
w(0)=0,\quad \mathcal D_ew=-4ue^{2w}\pmod{u^{m+1}},
\qquad
\mathcal D_oa+8ue^{2w}a=-e^w/2\pmod{u^m}.
\tag{3}
$$

这里 $(0)$ 指 $u$ 常数项，不是 $H=0$。
因为 $d_{2j}(0)=-4j^2$、$d_{2j+1}(0)=-(2j+1)^2$，所列全部对角元为单位。
偶常数项固定为零，绝不求 $d_0^{-1}$；奇下标 $j=m$ 不属于定义范围。
指数只需次数至多 $m<p$，其阶乘都是单位。
式 (3) 正是实际低带在本范围的约化，不把内部模态设为零。

实际接口继承下列已接受源的指定部分，而不重用它们的旧二次显式解或六核结论：

- [A19 最高项 Ward 稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)
  Steps 1–3、式 (9)–(24)：同一低带、基导数解、完整 Ward 及第一 forcing 关系。
- [A21 有限参照 ghost 稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md)
  Steps 1–5：先整性、再比较、两高带共同缩放与完整端点净贡献为零。
- [A22 原下一层响应稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md)
  Steps 1–3 至式 (12) 及 Step 8：实际移位、完整二次驱动与误差范围。
  其式 (16) 之后的旧解展开及 Steps 4–6 不作式 (1) 的输入。

## Proof Strategy and dependency map

1. Chebyshev 的二阶低展开使偶、奇有限对角算子在反向配对下互为伴随。
2. 对低方程作 $u$ 的 Euler 微分，直接构造两个参数化伴随权重。
3. 有限配对和乘法交换把未知响应从端点转移到其已知右端。
4. 在原实际模 $h^{p+1}$ 系统中，二次因子 $H^{2m}$ 只需要此模 $H^2$ 身份。

所有步骤都是准确有限身份或有明确阶数的约化，不使用近似模型、无限响应解或数值外推。

## Proof

### Step 1. 有限反向配对与真实传播子

由 $C_{n+1}=(2-H)C_n-C_{n-1}$、$C_0=2$、$C_1=2-H$，逐项比较到 $H^2$ 得

$$
d_n=-n^2+\frac{n^2(n^2-1)}{12}H\pmod{H^2}.
\tag{4}
$$

具体地，$C_n$ 的 $H$ 系数为 $-n^2$，$H^2$ 系数为 $n^2(n^2-1)/12$；
两多项式分别满足上述递推在对应次数的差分式并符合 $n=0,1$ 初值，因而对所有整数 $n\ge0$ 成立。
先取得这个有理系数的准确整数多项式系数身份，再约化模 $p$；固定分母 $12$ 对 $p\ge5$ 合法。
由于右侧是 $n$ 的偶多项式，

$$d_{2j}=d_{p-2j}=d_{2(m-j)+1}\quad\text{于 }R,
\qquad 1\le j\le m.\tag{5}$$

对奇型 $A\in R[u]/(u^m)$ 和偶型 $X\in uR[u]/(u^{m+1})$，定义
$\langle A,X\rangle=[u^m]AX$。
按 $X_j$ 展开并用式 (5)，有

$$
\langle A,\mathcal D_eX\rangle
=\sum_{j=1}^m A_{m-j}d_{2j}X_j
=\langle\mathcal D_oA,X\rangle.
\tag{6}
$$

对偶型 $B$ 和奇型 $Y$，同样逐项使用同一个式 (5)，得到
$[u^m]B\mathcal D_oY=[u^m](\mathcal D_eB)Y$。
乘子 $8uf_2$ 在配对中直接交换。因此

$$
[u^m]A\mathcal L_eX=[u^m](\mathcal L_oA)X,
\qquad
[u^m]B\mathcal L_oY=[u^m](\mathcal L_eB)Y.
\tag{7}
$$

这些等式没有丢弃端点项：第一式里 $X$ 的常数为零，
所以从不需要 $\mathcal L_oA$ 的 $u^m$ 系数；
第二式里 $B$ 的常数为零，所以从不需要 $\mathcal L_oY$ 的 $u^m$ 系数。
乘法保留到相应有限次数即可，缺失的奇共振下标不会被配对重新引入。

### Step 2. 直接构造参数化伴随权重

令

$$\alpha=2\mathcal Qa\pmod{u^m},\qquad
\beta=4\Theta w\pmod{u^{m+1}}.\tag{8}$$

$\beta(0)=0$。对第一条低方程取 $\Theta$，对角算子与 $\Theta$ 交换，
而 $\Theta f_2=2f_2\Theta w$，所以

$$
\mathcal D_e\Theta w=-4uf_2(1+2\Theta w),
\qquad \mathcal L_e\Theta w=-4uf_2.
\tag{9}
$$

于是 $\mathcal L_e\beta=-16uf_2$，在次数 $1,\ldots,m$ 成立。
对第二条低方程取 $\Theta$，得到

$$
\mathcal L_o\Theta a
=-\frac{f_1}{2}\Theta w-8uf_2a(1+2\Theta w).
\tag{10}
$$

将式 (10) 乘 $2$，再加 $\mathcal L_oa=-f_1/2$，按 $\mathcal K$ 定义合并，得到

$$
\mathcal L_o(\mathcal Qa)=-\mathcal K(1+2\Theta w),
\qquad
\mathcal L_o\alpha+\mathcal K\beta=-2\mathcal K.
\tag{11}
$$

这里只用次数 $0,\ldots,m-1$ 的奇方程。
$\Theta$ 保持次数，因此求导不会把未知的 $u^m$ 奇系数带入。

### Step 3. 将完整端点转到已知驱动

把 $P=\mathcal L_eX$、$Q=\mathcal L_oY+\mathcal KX$ 代入，依次用式 (7)、(9)、(11)：

$$
\begin{aligned}
[u^m](\alpha P+\beta Q)
&=[u^m]\{(\mathcal L_o\alpha+\mathcal K\beta)X
 +(\mathcal L_e\beta)Y\}\\
&=-[u^m](2\mathcal KX+16uf_2Y)\\
&=-[u^m]f_1X-16[u^{m-1}]f_2(Y+2aX).
\end{aligned}
\tag{12}
$$

式 (8) 使左端正是式 (1) 第二行，命题得证。$\square$
特别地，$P(0)=0$；乘 $Q$ 的 $\beta(0)=0$。
这再次说明右端所需奇下标严格小于 $m$。

### Step 4. 与原零层伴随的关系

在 $H=0$ 时，有限低解为 $w_0=\sum_{r=1}^{m}u^r/r$、
$a_0=\tfrac12\sum_{r=0}^{m-1}u^r$。
于是 $\alpha_{m-j}=2(m-j)+1=p-2j=-2j$ 对 $1\le j\le m$，
$\beta_{m-j}=4$ 对 $0\le j<m$。式 (1) 专化为

$$\mathcal C_0(X,Y)=-2\sum_{j=1}^m jP_j+4\sum_{j=0}^{m-1}Q_j.\tag{13}$$

这与旧零层有限伴随一致，但本证明不是对式 (13) 的模 $p$ 结论再除以 $p$，
而是先在 $R$ 中证明了包括参数一次变化的式 (1)。

### Step 5. 同一实际二次系统的精度接口

现在固定任意整数 $a_{\rm den}\ge2$，令 $M=p^{a_{\rm den}-1}m$、
$D=p+m$、$\chi=(-1)^{m+1}$，$h=2-\zeta-\zeta^{-1}$，其中 $\zeta$ 为本原 $p^{a_{\rm den}}$ 次根。
实际圆分整环 $\mathcal O^+=\mathbb Z_p[h]$ 满足 $v_h(p)=M$。
以下较大工作环为
$\mathscr R=\mathbb F_p[H]/(H^{p+1})\cong\mathcal O^+/(h^{p+1})$，$H\mapsto h$。
低系数先在形式整环内取 $\mathcal E=H\partial_H$，再约化；不对已取值的 $h$ 求导。

由所列 A19、A21、A22 的实际输入，令

$$
\tau^{\rm b}=-2\Theta w,\quad\sigma^{\rm b}=-\mathcal Qa,
\quad Z=(\mathcal E-\Theta)w,\quad T=(\mathcal E-\Theta-1)a,
$$
$$
\lambda_H=\chi H^m(4-H)^{m+1},\qquad c(H)=16-4H.
$$

在本段，$w,a$ 及 Ward 量按较大环所需精度使用，其模 $H^2$ 约化就是式 (3) 的同一低带。
保留实际移位
$\Delta_n=\lambda_HS_n-4H^{2m}-2H^pd_n\pmod{H^{p+1}}$。
从单位三角性可定义唯一 $X\in uR[u]/(u^{m+1})$、$Y\in R[u]/(u^m)$，使

$$
\widehat\tau=\tau^{\rm b}+\lambda_HZ+H^{2m}X,
\qquad
\widehat\sigma=\sigma^{\rm b}+\lambda_HT+H^{2m}Y
\quad\text{于 }\mathscr R.
\tag{14}
$$

它们满足的准确驱动就是 A22 式 (12)：

$$
\begin{aligned}
P&=(4+2H\mathcal D_e)\tau^{\rm b}-c(H)S_eZ,\\
Q&=(4+2H\mathcal D_o)\sigma^{\rm b}-c(H)S_oT.
\end{aligned}
\tag{15}
$$

这里 $S_eu^j=S_{2j}u^j$、$S_ou^j=S_{2j+1}u^j$。
式 (15) 全部在 $R$ 内，只需低带的 $H^0,H^1$ 系数。
无需先求二次零阶 $X_0,Y_0$ 来定义或求解它；偶入口由 $X(0)=0$ 固定，奇入口由单位对角元确定。
把式 (14) 代入同一个完整端点、使用保留的 Ward 乘积身份及 A21 净 ghost 结论，得到

$$
4^DpC_D=-\lambda_H(\mathcal E-m)B_{\rm low}
+H^{2m}\mathcal C_H(X,Y)\pmod{H^{p+1}},
\tag{16}
$$

其中 $C_D=[L^D]\mathcal B_3$、
$B_{\rm low}=[u^m]f_1+16[u^{m-1}]f_2a=-4^m[L^m]\mathcal B_1$。
由式 (1)，二次项仅需式 (15) 的驱动和低带，不含二次显式基解或六核。
这个接口不单独计算式 (16) 的数值，也不删 A21 的真实共同缩放证明。

精度是充分且有限的：$2m+2=p+1$；故模 $H^2$ 的二次计算乘 $H^{2m}$ 后覆盖所需全部层。
三次反馈至少为 $H^{3m}$，实际中间污染高度至少 $M-2m\ge3m$，
而 $3m\ge2m+2=p+1$；在 $p=5,m=2$ 是等号，恰在排除阶。
因此未扩大 $p,a_{\rm den}$ 限制，也没有获得再下一层的许可。

## Corrections or Missing Assumptions

无新增科学假设。式 (1) 只要求已列有限低方程和真实 Chebyshev 符号。
必须同时更新伴随权重与端点，不能把式 (13) 的常数权重直接用到 $H$ 一次层。
不能在奇下标 $m$ 处反演 $p$，也不能将有限交叉伴随理解为特征零或全阶自伴性。

## Open Risks and boundaries

- 新恒等式及实际接口须独立数学检查；作者证明不计非作者 PASS。
- 二次系数的具体值由另份同源有限计算处理；未核清前不能宣布旧显式基解可从当前完整证明链删除。
- 只有在新端点计算与消费者接口均闭合后，才可在当前证明中替换 A19 二次显式解、A22 六核及相应求和；旧接受稿永久保留。
- A17 原始整性／支撑、A18 有限参照与一次低解、A19 Ward、A21 ghost、A14–A16 三个参数窗口仍是必要输入。
- 本件不是新完整候选票、自然容量估计、稿件、PDF 或 Route 评价；不据此预支页数收益。
