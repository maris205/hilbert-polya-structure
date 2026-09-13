# P30 Goal01：屋顶输入误差与固定空间 resolvent 的定量稳定性

日期：2026-09-09 UTC。持续内部研究下经主线明确批准的唯一后继项；
只新增本文件，不改旧稿、锁定输入、程序或正式 Gate 状态。

## 1. 结论范围与固定输入

本页补[原路线图][roadmap] §2.4、§4.4 所要求的一个必要通道：
固定真实屋顶的输入误差如何传到同一 Banach 空间中的 transfer
operator，再传到已经存在的 resolvent。它不是完整五通道总误差、
determinant conditioning、谱／零点身份或科学计算证书。

始终固定[一侧屋顶笔记][roof]的原等边三盘：
半径 a>0、盘心间距 6a、单位速率、原盘标记、标准过去、有限平均、
一侧编码和端点指数 beta。记

\[
\begin{aligned}
\Sigma^+&=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},\\
d_\theta(x,y)&=\theta^{N(x,y)},\qquad
N(x,y)=\min\{j\ge0:x_j\ne y_j\},\\
\mathcal B_\beta&=C^\beta(\Sigma^+,d_\theta;\mathbb C),\qquad
q=\theta^\beta\in(0,1),\\
[u]_\beta&=\sup_{x\ne y}\frac{|u(x)-u(y)|}{q^{N(x,y)}},
\qquad \|u\|_\beta=\|u\|_\infty+[u]_\beta.
\end{aligned}
\tag{1}
\]

相同序列距离为零。真实正屋顶及原算子为

\[
g\in\mathcal B_\beta(\mathbb R),\quad
2a\le g\le10a,\quad G=[g]_\beta<\infty,\qquad
\mathcal L_su(x)=\sum_{j\ne x_0}e^{-sg(jx)}u(jx).
\tag{2}
\]

由[压力身份][entropy]及[固定空间条带笔记][strip]，
对实 t 有连续的 \(\lambda_t=r(\mathcal L_t)>0\)，并且
\(h=h_T>0\)、\(\lambda_h=1\)。

令 e 为一个固定的实值 \(\mathcal B_\beta\) 函数，定义

\[
\widetilde g=g+e,\qquad
\varepsilon_0=\|e\|_\infty\le a,\qquad
\varepsilon_\beta=[e]_\beta<\infty,\qquad
\widetilde{\mathcal L}_su(x)
 =\sum_{j\ne x_0}e^{-s\widetilde g(jx)}u(jx).
\tag{3}
\]

于是 \(a\le\widetilde g\le11a\)。这里只把 \(\widetilde g\) 解释为同一
输入的近似／enclosure 代表；不声称它来自另一个几何系统，也不声称
它的周期和等于真实 g 的周期和。它的定义不从轨道总量反拟合。

对实紧区间 I，设

\[
A=\max_{t\in I}|t|,\qquad
\lambda_-=\min_{t\in I}\lambda_t>0,\qquad
s=t+ib,\quad B=B(b):=\max\{1,|b|\},
\]
\[
N_B(u)=\|u\|_\infty+B^{-1}[u]_\beta,\qquad
\|Q\|_B=\|Q\|_{N_B\to N_B}.
\tag{4}
\]

以下高频区 B 就是 \(|b|\)。使用最大值的目的是同时包括 b=0
与有限频段，不在 b=0 定义一个含 \(1/|b|\) 的范数。对所有 B≥1，

\[
N_B(u)\le\|u\|_\beta\le B N_B(u).
\tag{5}
\]

所有空间的集合仍是原 \(\mathcal B_\beta\)。参数全纯性如需使用，
仍指固定 \(\|\cdot\|_\beta\) 算子范数，不指随 b 变化的范数。

本页的另一对算子始终共用原屋顶的精确 normalizer：

\[
T_s=\lambda_t^{-1}\mathcal L_s,\qquad
\widetilde T_s=\lambda_t^{-1}\widetilde{\mathcal L}_s.
\tag{6}
\]

\(\widetilde T_s\) 不是按 \(\widetilde g\) 自身压力重新归一化的算子。
选择或估计近似 normalizer 不在本页范围。由于 \(\lambda_t\)
依赖 \(\operatorname{Re}s\)，也不声称 (6) 是复 s 的全纯族。

## 2. 一步算子界：可固定的全部常数

先直接给出原算子在 (4) 中的统一一步界，不用“所有实 RPF
常数自动一致”或未写明的范数等价因子。设

\[
E_A=e^{10aA},\qquad
C_L=2E_A\bigl(3+(A+1)qG\bigr),\qquad
C_T=\lambda_-^{-1}C_L.
\tag{7}
\]

我们证明对所有 t∈I、b∈R，

\[
\|\mathcal L_s\|_B\le C_L,\qquad
\|T_s\|_B\le C_T.
\tag{8}
\]

首先 \(|e^{-sg}|\le E_A\)，每个点有两个前驱，因此
\(\|\mathcal L_su\|_\infty\le2E_A\|u\|_\infty\)。
若 \(x_0=y_0\)，相同前驱 j 可逐项配对，
\(N(jx,jy)=N(x,y)+1\)。实数 r 上的函数 \(e^{-sr}\)
在 \(r\in[2a,10a]\) 上导数模至多 \(|s|E_A\)，故

\[
\frac{|\mathcal L_su(x)-\mathcal L_su(y)|}
     {q^{N(x,y)}}
\le2E_Aq\bigl([u]_\beta+|s|G\|u\|_\infty\bigr).
\tag{9}
\]

若 \(x_0\ne y_0\)，分母为 1，直接用两个 sup 界得到
\(4E_A\|u\|_\infty\)。这同时控制了前驱集合改变的边界。因此

\[
[\mathcal L_su]_\beta
\le2E_A\bigl(q[u]_\beta+(|s|qG+2)\|u\|_\infty\bigr).
\tag{10}
\]

又因 \(|s|\le A+B\le(A+1)B\)，

\[
N_B(\mathcal L_su)
\le2E_A\left[
 \left(1+\frac{|s|qG+2}{B}\right)\|u\|_\infty
 +qB^{-1}[u]_\beta\right]
\le C_LN_B(u).
\tag{11}
\]

除以 \(\lambda_t\ge\lambda_-\) 得到 (8)。常数 (7) 只依赖固定
a、q、G、I 及其原 \(\lambda_-\)，与 b、e、输入函数无关。

## 3. 实屋顶误差的乘子估计

对任意 f、u∈\(\mathcal B_\beta\)，乘积差商给

\[
[fu]_\beta\le\|f\|_\infty[u]_\beta+[f]_\beta\|u\|_\infty,
\qquad
\|M_f\|_B\le\|f\|_\infty+B^{-1}[f]_\beta.
\tag{12}
\]

令 \(F_s=e^{-se}-1\)。对实 r∈\([-\varepsilon_0,\varepsilon_0]\)，
\[
\left|\frac{d}{dr}e^{-sr}\right|
=|s|e^{-tr}\le |s|e^{A\varepsilon_0}.
\]
分别在 0 与 e(x) 之间、e(x) 与 e(y) 之间积分，得到

\[
\|F_s\|_\infty\le |s|\varepsilon_0e^{A\varepsilon_0},
\qquad
[F_s]_\beta\le |s|\varepsilon_\beta e^{A\varepsilon_0}.
\tag{13}
\]

这里关键前提是 e 实值：沿实线段控制的是 \(e^{|t|\varepsilon_0}\)，
不是未经证明删掉的 \(e^{|s|\varepsilon_0}\)。本页不将 (13)
原样推广到复值输入误差。

从逐项定义可以核实乘法次序：

\[
\widetilde{\mathcal L}_s
 =\mathcal L_s M_{e^{-se}},\qquad
\Delta_s^L:=\widetilde{\mathcal L}_s-\mathcal L_s
 =\mathcal L_sM_{F_s},
\]
\[
\Delta_s^T:=\widetilde T_s-T_s
 =T_sM_{F_s}=\lambda_t^{-1}\Delta_s^L.
\tag{14}
\]

一般不能把右侧乘子移到 \(\mathcal L_s\) 左侧。结合 (8)、(12)、
(13)，定义可直接代入的误差上界

\[
d_L(s,e):=C_L|s|e^{A\varepsilon_0}
 \left(\varepsilon_0+\frac{\varepsilon_\beta}{B}\right),
\quad
d_T(s,e):=C_T|s|e^{A\varepsilon_0}
 \left(\varepsilon_0+\frac{\varepsilon_\beta}{B}\right).
\tag{15}
\]

于是

\[
\boxed{\|\Delta_s^L\|_B\le d_L(s,e),\qquad
       \|\Delta_s^T\|_B\le d_T(s,e).}
\tag{16}
\]

(15) 保留指数因子，尚未把 e 的大小藏进一个“统一常数”。在本页
预先固定的 \(\varepsilon_0\le a\) 条件下，另设

\[
D_L=C_L(A+1)e^{Aa},\qquad
D_T=C_T(A+1)e^{Aa},\qquad
\delta_B=B\varepsilon_0+\varepsilon_\beta.
\tag{17}
\]

由 \(|s|/B\le A+1\) 得到较简洁但可能较保守的结论

\[
\boxed{\|\Delta_s^L\|_B\le D_L\delta_B,\qquad
       \|\Delta_s^T\|_B\le D_T\delta_B.}
\tag{18}
\]

如果要以另一个上界 \(\varepsilon_0\le E_0<\infty\) 代替 a，
必须相应把 (17) 的 \(e^{Aa}\) 改成 \(e^{AE_0}\)，并另行保证所需
屋顶正性。没有任何无上界、e-无关的指数吸收断言。

## 4. 两侧因式分解、Neumann 门槛与 resolvent identity

以下引理是一般 Banach 空间上的直接证明；对每个固定 s 使用同一
\(N_B\) 范数即可。设 Q、\(\widetilde Q=Q+\Delta\) 有界，
\(R=(I-Q)^{-1}\) 已存在，并有

\[
\|R\|_B\le M,\qquad \|\Delta\|_B\le d,\qquad Md<1.
\tag{19}
\]

写 \(A_Q=I-Q\)，则乘法次序明确的两个因式分解为

\[
I-\widetilde Q
=A_Q(I-R\Delta)
=(I-\Delta R)A_Q.
\tag{20}
\]

由 (19)，\(\sum_{k\ge0}(R\Delta)^k\) 与
\(\sum_{k\ge0}(\Delta R)^k\) 都在算子范数下绝对收敛。
它们的有限部分和与对应 \(I-R\Delta\)、\(I-\Delta R\)
左右相乘均给恒等算子减去趋零的尾冪，所以各自是双侧逆。
因此

\[
\widetilde R:=(I-\widetilde Q)^{-1}
=(I-R\Delta)^{-1}R
=R(I-\Delta R)^{-1},
\]
\[
\|\widetilde R\|_B\le\frac{M}{1-Md}.
\tag{21}
\]

再利用两个逆的左右恒等式，直接计算

\[
\begin{aligned}
R\Delta\widetilde R
 &=R\bigl((I-Q)-(I-\widetilde Q)\bigr)\widetilde R
  =\widetilde R-R,\\
\widetilde R\Delta R
 &=\widetilde R\bigl((I-Q)-(I-\widetilde Q)\bigr)R
  =\widetilde R-R.
\end{aligned}
\tag{22}
\]

这给出两个合法但不能任意交换因子的 resolvent identity，以及

\[
\boxed{
\|\widetilde R-R\|_B
\le\frac{M^2d}{1-Md}.}
\tag{23}
\]

特别地，预先要求 \(Md<1/2\) 时，

\[
\|\widetilde R\|_B\le2M,\qquad
\|\widetilde R-R\|_B\le2M^2d.
\tag{24}
\]

这是围绕已存在的 R 展开的扰动 Neumann 级数；不要求
\(\|Q\|<1\)，也不要求整个谱位于单位圆内。对 (14) 分别取
\(Q=\mathcal L_s\)、\(Q=T_s\)，并用对应 d，才得到下面两类结论。

## 5. 有限频率：紧集必须避开相应不可逆点

### 5.1 共用精确 normalizer 的有限中频

固定任意实紧区间 I 及 \(0<\delta\le B_f<\infty\)，令

\[
\mathcal K_T=\{t+ib:t\in I,\ \delta\le|b|\le B_f\},
\qquad B_*=\max\{1,B_f\}.
\tag{25}
\]

[固定频率笔记][finite]给每个 s∈\(\mathcal K_T\) 的
\(r(T_s)<1\)，故 \(R_T(s)=(I-T_s)^{-1}\) 存在。
原算子范数整性和 \(\lambda_t>0\) 的连续性使 \(T_s\) 在固定范数中
连续；(20)–(21) 的局部 Neumann 公式又使 \(R_T(s)\) 连续。
紧性因此保证下式是一个有限常数：

\[
M_{T,f}
=B_*\max\left\{1,\sup_{s\in\mathcal K_T}
                  \|R_T(s)\|_{\beta\to\beta}\right\}<\infty.
\tag{26}
\]

这里的 \(B_*\) 明列了 (5) 的算子范数代价，所以
\(\|R_T(s)\|_B\le M_{T,f}\)。又由 (15)，在 \(\mathcal K_T\) 上

\[
d_T(s,e)\le
d_{T,f}:=C_T(A+B_f)e^{Aa}
                  (\varepsilon_0+\varepsilon_\beta).
\tag{27}
\]

若 \(M_{T,f}d_{T,f}<1/2\)，则整个 \(\mathcal K_T\) 上
\(I-\widetilde T_s\) 都可逆，并有

\[
\|\widetilde R_T(s)\|_B\le2M_{T,f},\qquad
\|\widetilde R_T(s)-R_T(s)\|_B
\le2M_{T,f}^2d_{T,f}.
\tag{28}
\]

也可以逐点使用更小的 (15)，无须一定采用 (27)。
条件 \(\delta>0\) 不能删掉：对每个实 t，\(T_t\) 都有本征值 1，
所以 \(I-T_t\) 不可逆。本页没有在整个实轴上构造它的逆。

### 5.2 原非归一化算子的有限频率

令 \(\mathcal S_\eta=\{s:|\operatorname{Re}s-h|<\eta\}\)
为[条带笔记][strip] §4 已证的条带。取任意非空紧集

\[
\mathcal K_L\Subset\mathcal S_\eta\setminus\{h\},
\qquad |\operatorname{Im}s|\le B_f,\quad
\operatorname{Re}s\in I\quad(s\in\mathcal K_L).
\tag{29}
\]

这里可允许 b=0，但必须避开 h。已有
\(R_L(s)=(I-\mathcal L_s)^{-1}\) 在该集合的邻域全纯，故

\[
M_{L,f}
=B_*\max\left\{1,\sup_{s\in\mathcal K_L}
                  \|R_L(s)\|_{\beta\to\beta}\right\}<\infty,
\qquad
d_{L,f}=C_L(A+B_f)e^{Aa}
                  (\varepsilon_0+\varepsilon_\beta).
\tag{30}
\]

若 \(M_{L,f}d_{L,f}<1/2\)，则整个 \(\mathcal K_L\) 上
\(I-\widetilde{\mathcal L}_s\) 可逆，而且

\[
\|\widetilde R_L(s)\|_B\le2M_{L,f},\qquad
\|\widetilde R_L(s)-R_L(s)\|_B
\le2M_{L,f}^2d_{L,f}.
\tag{31}
\]

(29) 不要求 \(r(\mathcal L_s)<1\)：t<h、b 很小时该条件一般不是
条带证明使用的条件。此处合法使用的是已有逆和 §4，而不是
\(\sum_n\mathcal L_s^n\) 在整个低频区的未经证明收敛。

不能令 (30) 的常数无条件穿过 h。确切地，[strip] §3 给

\[
R_L(s)=\frac{\Pi_h}{m_h(s-h)}+\mathscr H(s),
\qquad
m_h=\mu_h(g)\in[2a,10a],\qquad \Pi_h\ne0.
\tag{32}
\]

在充分小的闭圆盘内，取半径小于 1，则 B=1，且可逐点使用
\[
M(s)=\frac{\|\Pi_h\|_{\beta\to\beta}}{m_h|s-h|}
       +\sup\|\mathscr H\|_{\beta\to\beta}
\quad(s\ne h)
\]
作为 (19) 中的上界。安全门槛随接近 h 而收紧；(32) 不给跨越
h 的统一逆界，也不证明近似屋顶的压力极点位置不变。

对固定 e，\(\widetilde{\mathcal L}_s
=\mathcal L_0M_{\exp(-s(g+e))}\) 仍在固定 Banach 范数中整：
(12) 在 B=1 给 Banach 代数估计，指数幂级数在每个有界 s 集上
按算子范数一致绝对收敛。于是上述可逆点附近的
\(\widetilde R_L\) 全纯。这不赋予 (6) 归一化族复全纯性。

## 6. 高频归一化逆：明确的对数门槛

现在把 I 限制在[全 Hölder 高频笔记][high]所给的固定实紧窗口
\(I_0\) 内，h 是 \(I_0\) 的内点。使用该输入的常数
\(B_0\ge e^2\)、\(C_H\ge1\)、\(K_H>0\)、\(c_H>0\)，满足

\[
\|T_{t+ib}^{\,n}\|_B
\le C_H\min\{1,B^{K_H}e^{-c_Hn}\},
\quad t\in I_0,\ B=|b|\ge B_0,\ n\ge0.
\tag{33}
\]

[high] §11.3 按
\(n_0=\lceil(K_H/c_H)\log B\rceil\) 拆分级数，给真正的双侧逆及

\[
\begin{aligned}
\|R_T(t+ib)\|_B
&\le C_H\left(
 \left\lceil\frac{K_H}{c_H}\log B\right\rceil
 +\frac1{1-e^{-c_H}}\right)\\
&\le M_T(B):=C_R(1+\log B).
\end{aligned}
\tag{34}
\]

\(C_R\) 是由 (33) 固定的有限常数，与 e、B、t 无关。
定义本频段的无量纲安全量

\[
\Gamma_T(B,e)
:=D_TC_R(B\varepsilon_0+\varepsilon_\beta)(1+\log B).
\tag{35}
\]

在 t∈I、B≥B_0 的每一点，如果
\(\Gamma_T(B,e)<1/2\)，则

\[
\boxed{
\begin{aligned}
\|\widetilde R_T(t+ib)\|_B
&\le2C_R(1+\log B),\\
\|\widetilde R_T(t+ib)-R_T(t+ib)\|_B
&\le2D_TC_R^2(B\varepsilon_0+\varepsilon_\beta)
                          (1+\log B)^2.
\end{aligned}}
\tag{36}
\]

证明就是在 (24) 中取 \(M=M_T(B)\)、\(d=D_T\delta_B\)。
如使用实际的 (15)，还可把 (35) 换成较弱的
\(M_T(B)d_T(s,e)<1/2\)。并未对 \(\widetilde g\) 重新应用几何
高频定理，也未假设近似屋顶本身具有同一组 Dolgopyat 常数。

## 7. 高频原逆：保留实压力增长损失

原 \(R_L\) 的高频输入不同。取含 h 的闭实区间
\(I'\subset[h-\eta,h+\eta]\cap I_0\)，按 [strip] §5 选到

\[
\mathfrak a_{I'}
:=\max\{0,\sup_{t\in I'}\log\lambda_t\}<c_H/2,\qquad
\kappa_{I'}=\frac{K_H\mathfrak a_{I'}}{c_H}\ge0.
\tag{37}
\]

\(\mathfrak a_{I'}\) 不是几何圆盘半径 a。重新以 I=I' 固定
(4)、(7)、(17) 的常数。条带证明中保留了每一项
\(\lambda_t^n\)，得到

\[
\|R_L(t+ib)\|_B
\le M_L(B):=C_S(1+\log B)B^{\kappa_{I'}},
\qquad t\in I',\quad B=|b|\ge B_0.
\tag{38}
\]

因此正确的充分门槛是

\[
\Gamma_L(B,e)
:=D_LC_S(B\varepsilon_0+\varepsilon_\beta)
          (1+\log B)B^{\kappa_{I'}}<\frac12.
\tag{39}
\]

在 (39) 成立的每一点，\(\widetilde R_L=(I-\widetilde{\mathcal L}_s)^{-1}\)
存在，并由 (24) 得

\[
\boxed{
\begin{aligned}
\|\widetilde R_L(t+ib)\|_B
&\le2C_S(1+\log B)B^{\kappa_{I'}},\\
\|\widetilde R_L(t+ib)-R_L(t+ib)\|_B
&\le2D_LC_S^2(B\varepsilon_0+\varepsilon_\beta)
       (1+\log B)^2B^{2\kappa_{I'}}.
\end{aligned}}
\tag{40}
\]

逐点的较弱条件同样是 \(M_L(B)d_L(s,e)<1/2\)。
不能将整个既定条带的 (38) 偷换成纯 \(O(1+\log B)\)：
只有在实际可取 \(\mathfrak a_{I'}=0\) 的参数集合，例如
\(I'=\{h\}\)，才从本式得到 \(\kappa_{I'}=0\)。
若预先缩窄条带以减小指数，宽度及常数也随之改变。

(36)、(40) 都是频率加权范数结论。若需要固定强算子范数，
由 (5) 有
\(\|Q\|_{\beta\to\beta}\le B\|Q\|_B\)，须对最后输出界再乘 B；
不能把同一个加权界不加因子地改名为固定强范数界。

门槛 (35)、(39) 是关于 (s,e) 的条件，不是对任意固定非零 e
保证全部无限高频的断言。给定输入精度通常只能据此认证某个
频率范围；若让频率上限增长，必须同步检查输入误差是否满足门槛。

## 8. 有限记忆屋顶：sup 小不自动满足强扰动门槛

### 8.1 当前真实 g 的已知输入，仅到哪里

[有限记忆笔记][memory] §1 对每个深度 m 的 cylinder 预选代表，
定义 \(P_mf\) 在该柱上等于代表处函数值。它给

\[
\|P_mf-f\|_\infty\le q^m[f]_\beta,\qquad
[P_mf]_\beta\le[f]_\beta.
\tag{41}
\]

对实际 \(g_m=P_mg\)、\(e_m=g_m-g\)，因此只能直接得出

\[
\varepsilon_{0,m}\le Gq^m,\qquad
\varepsilon_{\beta,m}\le2G,\qquad 2a\le g_m\le10a.
\tag{42}
\]

当 \(Gq^m\le a\) 时可套用本页的统一上界。将目前 (42) 代入
(18) 得到 \(D_LG(Bq^m+2)\) 或 \(D_TG(Bq^m+2)\)；
在 G>0 时，这个已知上界本身并不随 m 趋零。它既不证明实际
\([g_m-g]_\beta\) 必有正下界，也不证明实际算子误差不收敛，
但明确显示现有 sup 证书不能独自认证本页的小扰动条件。

### 8.2 同一符号空间中的一般 big Hölder 反例

下面的反例解释缺失的逻辑步骤，不把一般函数冒充真实物理 g。
在 (1) 的同一无自环三符号 shift 上，取

\[
f(x)=\sum_{j=0}^\infty q^j\,1_{\{x_j=1\}}.
\tag{43}
\]

级数一致收敛，\(\|f\|_\infty\le(1-q)^{-1}\)。若首次不同坐标为 N，
前 N 项抵消，故
\[
|f(x)-f(y)|\le\sum_{j=N}^\infty q^j
             =\frac{q^N}{1-q},\qquad
[f]_\beta\le\frac1{1-q}.
\tag{44}
\]

任意每柱代表投影因而满足
\(\|P_mf-f\|_\infty\le q^m/(1-q)\to0\)，同时由 (41) 其
Hölder seminorm 不失控。

对每个 m≥1，取一个长 m、由 1、2 交替且最后一位为 2 的合法字
\(w^{(m)}\)，并定义
\[
x^{(m)}=(w^{(m)},1,2,1,2,\ldots),\qquad
y^{(m)}=(w^{(m)},3,2,3,2,\ldots).
\tag{45}
\]
这样的前缀对每个 m 都存在：从末位 2 向前交替即可。
前缀内部、前缀到尾段、尾段内部均无相邻重复，故两序列确实属于
\(\Sigma^+\)。它们首次不同坐标恰为 m，且在同一深度 m 柱内。
因此，不论该柱代表如何选择，
\[
P_mf(x^{(m)})=P_mf(y^{(m)}),\qquad
f(x^{(m)})-f(y^{(m)})
=\sum_{k\ge0}q^{m+2k}=\frac{q^m}{1-q^2}.
\]
从而

\[
\boxed{[P_mf-f]_\beta\ge\frac1{1-q^2}\quad(m\ge1).}
\tag{46}
\]

所以即使在完全相同的 shift 和端点范数上，sup 收敛也不推出
big Hölder 强范数收敛；反例对所有每柱代表选择都成立。
它只反驳这条一般推理，绝不是实际 \(g\) 的不收敛证书。
若要对实际 g 获得更强结论，需要另有更强正则性／强范数误差证书，
或另证可只使用弱误差的 weak–strong 稳定接口。本页没有悄悄更换
beta、完成该接口或把它当作既有结果。

## 9. 常数、证据与尚未获得的结论

(7)、(15)、(17) 明列了本页新增的一步与输入传播常数。
有限频段的 \(M_{T,f}\)、\(M_{L,f}\) 还依赖所选紧集，特别是其避开
相应不可逆集合的程度；紧性证明其有限，不是一个已算出的数值
enclosure。高频 \(C_H,K_H,c_H,B_0,C_R\) 继承固定真实几何、
source family、标准过去、有限平均、g、theta、beta 与实部窗口；
\(C_S,\kappa_{I'}\) 还依赖所选未归一化条带。
在这些选择固定后，它们不依赖输入函数、e、频率符号或 B≥B_0。
输入 e 的允许大小、频率增长和离极点距离则由各式显式控制。

本页严格只建立条件性的 roof norm → operator norm →
resolvent output norm 通道。它没有：

- 给 \(\widetilde g\) 另一个物理几何解释，或保持其周期时间不变；
- 为近似屋顶重新选择 normalizer，或计算其压力极点位移；
- 把有限记忆右域 determinant 收敛提升为条带内零点／重数收敛；
- 建立 determinant conditioning、普通 trace 或核 Fredholm 身份；
- 合成 orbit tail、rank、quadrature、roundoff 与 roof-input 五通道，
  或给出具体算法、精度、cutoff 和共同输出误差证书；
- 改变任何 Gate、Route、Stage、历史失败记录或执行停止线。

尤其，[非紧性笔记][noncompact]已排除原全 \(\mathcal B_\beta\) 上的
普通 nuclear 算子路线；本页的 resolvent 稳定性不会把原算子变成
核算子，也不替另一个 determinant 定义提供授权。

这是 AI 辅助内部纸面推导。ARS 的同阶段论证整合用于明确已有
输入、逐式推导、反例适用范围与未获结论。本页的指数因子、
乘法次序、范数等价因子及两类逆的门槛均有直接证明；一般反例经
同模型家族有界只读分工提供并由写者逐式核对，同伴同意不算外部
独立科学证据。没有新增外部文献断言或新颖性宣称。

本轮仅通过 apply_patch 新增本文件，并对这个新文件作一次静态
文本检查；不运行科学、符号、谱数值、轨道枚举、producer、
稿件 build 或正式研究 checker。实际检查结果随交接报告，不以
排版检查通过作为数学有效性或完整 Gate 通过的证据。

[roadmap]: stage1_phase6_final_report.md
[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[entropy]: internal_goal01_pressure_equals_physical_entropy_20260909.md
[strip]: internal_goal01_fixed_space_resolvent_strip_and_simple_pressure_pole_20260909.md
[finite]: internal_goal01_fixed_frequency_spectral_gap_20260909.md
[high]: internal_goal01_full_holder_high_frequency_from_cylinder_approximation_20260909.md
[memory]: internal_goal01_cylinder_trace_and_finite_memory_determinants_20260909.md
[noncompact]: internal_goal01_noncompact_transfer_and_positive_essential_radius_20260909.md
