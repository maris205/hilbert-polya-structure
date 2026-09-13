# 固定参数次项的单插入作用量恒等式 V1

日期：2026-09-07。主控作者证明，非作者核查另存。
本轮使用 `proof-writer`，把精确系数化简与尚未证明的共同根排除分开。
此前完整正负 Fourier 算法及低分母结论保留，不重开原证明或旧计算。

## Claim

对固定互素 $0<r<s$、$s\ge3$ 的原双谐波辛映射，
令 $v(t)$ 为下文定义的实际解析消元的纯正频支，$v_{ks}=0$。
总作用量中 $\epsilon^{s+2}\cos(s\theta)$ 的准确系数满足

$$\boxed{Q_{r,s}(\lambda)=-s[t^{s+1}]e^{-v(t)}.}\tag{1}$$

因此计算 $Q$ 只需正频支至 $s+1$ 阶，不必求负缺陷的位移响应。
这里不是把完整力中的负频项删去；负一次谐波作为显式插入保留，
消元驻值性质使位移响应对作用量的一阶变化消失。

进一步令 $y=Y(t)=te^{v(t)}$、$t=T(y)$ 为形式反函数，
$A_k=[y^k]T(y)^{-s}$。则

$$\boxed{Q_{r,s}=A_1,\qquad
C_{r,s}=-\frac{A_{-1}+4\lambda A_{-2}}s.}\tag{2}$$

## Status

恒等式 $(1)$、$(2)$ 及有限三角算法：`PROVABLE AS STATED`。

由此进一步断言 $C(\lambda_*)=0$、$C'(\lambda_*)\ne0$ 时
$Q(\lambda_*)\ne0$：`NOT CURRENTLY JUSTIFIED`。
本报告没有把原全分母命题改成“可以算法计算”这一较弱目标。

## Assumptions and notation

固定 $r,s$，置 $\omega=2\pi r/s$、$\zeta=e^{i\omega}$，
$D_n=4\sin^2(\pi rn/s)$。$D_n$ 按 $s$ 周期延拓；$s\nmid n$ 时为正。
$\lambda$ 保持固定，可在预定紧实区间中变化；所有解析邻域允许依赖这些固定数据。
映射及作用量规范不变：

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p',$$

$$\mathcal A=\sum_{j=0}^{s-1}
\left\{\tfrac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
-\lambda\epsilon^2\cos2q_j\right\}.$$

采用已接受的零均值小解消元，$q_j=\theta+\omega j+u_j$，
$\sum_j u_j=0$。其实际约化作用量为 $W$，相位平均为 $\overline W$。
首项 $C$ 和次项 $Q$ 的定义及解析余项沿用
[完整次项证明](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.md)。
下文将复参数记作 $x_+,x_-$，不将它们与零均值子空间或反函数 $Y,T$ 混用。
所有梯度、二次型及内积作复解析双线性延拓，不使用复共轭。

## Proof strategy and dependency map

1. 将正、负谐波幅度临时独立化，得到有限维全纯零均值消元。
2. 对负一次谐波幅度求导；驻值性质消除隐含位移导数。
3. 正支的循环协变性把格点求和转为一次精确系数筛选，证明 $(1)$。
4. 形式留数变元及分部积分给出 $(2)$；这些恒等式不需要假定 $C=0$。

## Proof

### Step 1. 独立幅度只是原作用量的解析计算装置

令 $Z=\{u\in\mathbb C^s:\sum_j u_j=0\}$，$\Pi$ 为复线性零均值投影。
在周期 $u$ 上定义

$$\begin{aligned}
\mathscr A(u;x_+,x_-)=&\ \tfrac12\sum_j(u_{j+1}-u_j)^2\\
&-\tfrac12\sum_j\left(x_+\zeta^je^{iu_j}+x_-\zeta^{-j}e^{-iu_j}\right)\\
&-\tfrac\lambda2\sum_j\left(x_+^2\zeta^{2j}e^{2iu_j}
+x_-^2\zeta^{-2j}e^{-2iu_j}\right).
\end{aligned}\tag{3}$$

在 $(u,x_+,x_-)=(0,0,0)$，$\Pi\nabla_u\mathscr A$ 对 $u\in Z$ 的导数
为可逆的 $L|_Z$，其中 $(Lu)_j=2u_j-u_{j-1}-u_{j+1}$。
有限维全纯隐函数定理给出唯一小全纯解 $U(x_+,x_-)\in Z$。
定义 $\Psi(x_+,x_-)=\mathscr A(U(x_+,x_-);x_+,x_-)$。

当 $x_+=\epsilon e^{i\theta}$、$x_-=\epsilon e^{-i\theta}$ 时，
$(3)$ 恢复原总作用量扣去常数 $s\omega^2/2$ 的表达。
解析解唯一性保证它恢复同一真实小解，而非另选模型。
单项式 $x_+^a x_-^b$ 对应 $\epsilon^{a+b}e^{i(a-b)\theta}$。
结合原反射对称性给出的实余弦规范，得到

$$C=2[x_+^s]\Psi(x_+,0),\qquad
Q=2[x_+^{s+1}x_-]\Psi(x_+,x_-).\tag{4}$$

此处辅助的独立幅度仅用于取原函数的精确 Taylor 系数，
不允许将最终 $\lambda$ 改成依赖 $\epsilon$ 的调谐曲线。

### Step 2. 负一次谐波插入的 envelope 恒等式

投影驻值使 $\nabla_u\mathscr A=c\boldsymbol1$，其中 $c$ 可非零。
$\partial_{x_-}U$ 的坐标和为零，因此链式法则严格给出

$$\partial_{x_-}\Psi=\left.\partial_{x_-}\mathscr A\right|_{u=U}.$$

对 $(3)$ 显式求导并令 $x_-=0$，负二次谐波项含一个 $x_-$ 因子，故消失。
余下精确身份为

$$\partial_{x_-}\Psi(x_+,0)
=-\tfrac12\sum_j\zeta^{-j}e^{-iU_j(x_+,0)}.\tag{5}$$

右边是一次显式负谐波插入。没有把响应位移假定为零；
它的贡献是因零均值投影驻值而与完整梯度配对为零。

### Step 3. 正支及模式筛选

对格点作循环平移并同时将 $x_+$ 乘以 $\zeta$，方程保持不变。
唯一性因此给出某个全纯 $v(t)$，使

$$iU_j(x_+,0)=v(x_+\zeta^j),\qquad v(0)=0.$$

零均值条件逐阶给出 $v_n=[t^n]v=0$ 当 $s\mid n$。
其余阶由投影驻值方程乘以 $i$ 得到

$$v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n},\quad s\nmid n,
\qquad E=e^v,\quad F=e^{2v},\tag{6}$$

其中负下标系数取零。$E_{n-1}$、$F_{n-2}$ 只涉及之前的 $v$ 系数，
所以这是实际正支的三角递推，包括超过首个共振阶后的各项。
$v_s=0$ 是零均值规范，不是声称 $E_{s-1}/2+\lambda F_{s-2}=0$。
特别是计算 $v_{s+1}$ 时仍用 $D_{s+1}=D_1>0$。

在 $(5)$ 中展开 $e^{-v(t)}=\sum_{n\ge0}h_nt^n$。
本原单位根求和给出
$\sum_j\zeta^{j(n-1)}=s$ 当 $n\equiv1\pmod s$，否则为零。
所以 $[x_+^{s+1}]\partial_{x_-}\Psi=-s h_{s+1}/2$。
由 $(4)$ 得到 $(1)$。整个论证对任意固定 $\lambda$ 成立，不要求 $C=0$。

### Step 4. 可直接实现的有限算法

在 $(6)$ 中算到 $n=s+1$，并使用指数微分递推

$$E_n=\frac1n\sum_{k=1}^nkv_kE_{n-k},\qquad
F_n=\sum_{k=0}^nE_kE_{n-k},\qquad
h_n=-\frac1n\sum_{k=1}^nkv_kh_{n-k},$$

初值为 $E_0=F_0=h_0=1$。最后输出 $Q=-s h_{s+1}$。
在共振阶必须先置 $v_s=0$，再照常更新 $E_s,F_s,h_s$；
这些指数系数本身不必为零。旧首项仅算到 $s-1$ 的正频表不能原样当作此算法。

这个有限算法没有负位移模式，却与先前完整正负模式算法计算同一实际系数；
证明靠 $(5)$ 的驻值消元，不靠有限算例相符。

### Step 5. 反函数 Laurent 系数

$Y(t)=te^{v(t)}$ 满足 $Y(0)=0,Y'(0)=1$，因此有唯一形式反函数 $T(y)$。
对任意形式 Laurent 级数，$\operatorname{Res}_t$ 表示 $t^{-1}$ 系数。
因为 $e^{-v}=t/Y$，作可逆形式变元 $y=Y(t)$ 得

$$\begin{aligned}
Q&=-s\operatorname{Res}_t\frac{dt}{Y(t)t^{s+1}}\\
 &=\operatorname{Res}_y\frac{(T(y)^{-s})'}y\,dy
 =[y^1]T(y)^{-s}=A_1.
\end{aligned}$$

最后等号只使用：$\operatorname{Res}_y(\sum_k kA_k y^{k-2})=A_1$。
另一方面，对 $k=1,2$，同一变元及形式导数留数为零给出

$$\begin{aligned}
[t^s]Y(t)^k
&=\operatorname{Res}_y y^kT^{-s-1}T'\,dy\\
&=-\tfrac1s\operatorname{Res}_y y^k(T^{-s})'\,dy
=\tfrac{k}{s}A_{-k}.
\end{aligned}$$

已接受的首项规范为
$C=-E_{s-1}-2\lambda F_{s-2}=-[t^s](Y+2\lambda Y^2)$，
代入上式得到 $(2)$ 的第二个恒等式。$\square$

## Corrections or missing assumptions

在同一个由真实传播子决定的反函数上，共同根问题精确化为

$$C(\lambda)=Q(\lambda)=0
\quad\Longleftrightarrow\quad
A_{-1}+4\lambda A_{-2}=0,\quad A_1=0.$$

这是必要且充分的系数条件，不是对其不可能性的证明。
反函数及其全部系数随 $\lambda$ 非线性变化；没有证据允许把其中一个
系数指定为独立正权或将双线性表达换成绝对值平方。
也不能用 $Q/C'$ 的事后定义把“某个因子非零”当成已证明结论。

## Open risks

原模型的全实根、根简单性和全部固定消失点的 $Q\ne0$ 仍是不同未完成义务。
本轮贡献是精确的单插入／反函数规约，不是全分母非消失定理。
与同轮反函数、系数变分报告重叠的公式只按一份数学内容计算；
没有论文立项、篇幅票、Route 评价、PDF或对外操作。
