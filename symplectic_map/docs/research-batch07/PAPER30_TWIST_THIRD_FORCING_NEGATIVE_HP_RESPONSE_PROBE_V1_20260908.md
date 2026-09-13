# Proof Package：最高 forcing 的首个非零负端剩余及有限伴随压缩

日期：2026-09-08。作者：`/root/negative_hp_response_author`。
使用 proof-writer；本件只写这个新文件，不改旧稿、入口、锁或接受记录。
本件主证明是完整移位／响应部分；第一 forcing 新层与有限参照 ghost
分别引用同轮另两份作者证明，明确区分作者闭合和非作者独审接受。

## Claim

固定任意素数 $p\ge5$、整数 $a\ge2$，保持同一实际双谐波分支，令

$$m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m=3m+1,
\qquad \chi=(-1)^{m+1},\qquad C_D=[L^D]\mathcal B_3.$$

本件在已接受的最高项 Ward 和二次边界之后，证明新的完整二次响应系数

$$\boxed{\mathfrak c_{2,1}=-1/2\quad\text{于 }\mathbb F_p.}\tag{1}$$

其精确定义见式 (19)。它包括非恒定二次传播子、一次低带、
二次响应的一次变化和全部端点乘积变化，不是只保留其中一个源项。
连同本轮第一 forcing 新层和有限参照 ghost 两个输入，得到

$$\boxed{4^DpC_D=-\frac34h^p+O(h^{p+1}),\qquad
\overline{h^{-p}pC_D}=-\frac3{16}\ne0.}\tag{2}$$

因此原最高系数下界成为准确等式

$$\boxed{v_h(pC_D)=p,\qquad v_h([L^p]U_{\rm cl})=M-m.}\tag{3}$$

式 (2)—(3) 的作者证明使用下列同轮明确输入；它们尚须与本件分别完成
真正非作者独立审查后，才可由主控登记为新的接受结论。
本件不独自声称完整负 Newton 图、因子型或分裂域已经验收。

## Status

**PROVABLE AS STATED，作者证明完成，独立审查另记。**
原目标不需要削弱或增加科学假设。式 (1) 是本件的自含新计算；
式 (2) 合并同轮两个有明确证明文件的输入，而非先验假设其误差为零。

## Assumptions and inputs

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为本原 $p^a$ 次根；
  $K^+=\mathbb Q_p(h)$，$\mathcal O^+=\mathbb Z_p[h]$，
  $v_h(h)=1$，$v_h(p)=M$，剩余域是 $\mathbb F_p$。
- 真实传播子为 $d_n=-(2-\zeta^n-\zeta^{-n})/h$，
  实际辅助权重低带 $W,A$ 和端点满足

  $$d_{2r}W_r=-4[u^{r-1}]e^{2W},\qquad
  d_{2r+1}A_r=-\frac12[u^r]e^W-8[u^{r-1}]e^{2W}A,$$
  $$4^DC_D=-[u^{p+m}]e^W-16[u^{p+m-1}]e^{2W}A,$$

  其中 $u=Lx^2/4$，$V|_{b=0}=W(u)$、$\partial_bV|_{b=0}=xA(u)$。
- [已接受最高项二次边界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)
  提供完整 Ward 身份、二次零层解及其端点为零；
  本件已全文读取该稿，使用其 [独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md)
  所对应的已接受数学输入，不重开已消失的旧层。
- [已接受后一临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md)
  式 (17)—(19) 提供有限低带的一次系数 $w_1,a_1$，以及所需整性与支撑。
- 同轮 [第一 forcing 最高项新层稿](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md)
  式 (3)—(4) 提供

  $$[H^{m+1}]B_{\rm low}=\chi/16,\qquad
  [H^p]\{-\lambda_H(\mathcal E-m)B_{\rm low}\}=-1/4.\tag{4}$$

  本件已全文读取该稿；它是同轮作者输入，独审状态不由本件替代。
- 同轮 [有限参照 ghost 稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md)
  式 (2)—(4)、(18)—(27) 提供精确首误差、真实高带共同缩放和净端点零贡献。
  本件已全文读取该稿；不是将旧 $O(h^p)$ 误差直接设为零。
- 商系数的换算只用已接受首一分解
  $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，
  其中 $P_{\rm cl}$ 首一次数 $m$、$U_{\rm cl}$ 次数 $p$。

## Notation

形式变量 $H$ 与实际 $h$ 分开，工作环为

$$\mathscr R_H=\mathbb F_p[H]/(H^{p+1})
\cong\mathcal O^+/(h^{p+1}),\qquad H\longmapsto h.$$

因为 $M\ge5m\ge2m+2=p+1$，该比较环的特征为 $p$。
定义 $\Theta=u\partial_u$、$\mathcal Q=2\Theta+1$、$\mathcal E=H\partial_H$，
并在各自有限低范围写

$$w=W_{<p},\quad a=A_{<m},\quad f_1=e^w,\quad f_2=e^{2w},$$
$$\mathcal D_eu^j=d_{2j}(H)u^j,\quad
\mathcal D_ou^j=d_{2j+1}(H)u^j,\quad
\mathcal L_e=\mathcal D_e+8uf_2,\quad
\mathcal L_o=\mathcal D_o+8uf_2,$$
$$\mathcal K=\frac{f_1}{2}+16uf_2a.$$

指数只提取次数小于 $p$ 的系数；这里的指数阶乘均为单位。
偶范围为 $1\le j\le m$，奇范围为 $0\le j<m$；偶常数项单独固定为零。
记

$$f=(1-u)^{-1},\quad g=f^2,\quad G=(1+u)f,\quad
\ell=\log(1-u),\quad
\mathscr D=\sum_{k\ge1}\frac{u^k}{k^2},\quad
\mathscr H=\sum_{r\ge0}\frac{u^r}{2r+1}.$$

这些级数先在特征零解释，只使用 $\ell,\mathscr D$ 的次数至多 $m$、
$\mathscr H$ 的次数小于 $m$。故所用分母都是 $p$ 单位。
供逐项验证的导数身份是

$$\Theta\ell=-uf,\qquad \Theta\mathscr D=-\ell,\qquad
\Theta\mathscr H=(f-\mathscr H)/2.\tag{5}$$

## Proof Strategy

保留传播子到 $H^p$ 的非恒定二次项，把高带写为精确基带、精确线性 Ward 项
及二次响应。新层的两条有限三角方程由实际方程逐项确定。
然后建立有限伴随恒等式，用简单权重 $-2j$ 和 $4$ 消去未知响应本身。
得到的端点只含已接受低层函数，其单和、有限三角双和全部化为三次多项式和。
最终合并线性新层和独立计算的 ghost，得到实际非零剩余。

## Dependency Map

1. 实际有限高带、首个 ghost 和污染支撑确定新精度下的同一计算对象。
2. 准确 Chebyshev 移位与 Ward 身份确定式 (13)—(17) 的二次响应系统。
3. 有限伴随引理把式 (19) 化为式 (25) 的已知核。
4. 六个系数多项式及有限双和交换证明 $\mathfrak c_{2,1}=-1/2$。
5. 同轮第一 forcing 新层及 ghost 零净贡献给式 (2)，首一性给式 (3)。

## Proof

### Step 1. 实际 ghost 已计入，辅助系统没有更换模型

同轮 ghost 稿在本次环内证明

$$E_c=c f_c(\tau-\eta),\qquad \eta=1+H^p/4,\qquad c=1,2,$$

并证明实际高带为 $\tau=\eta\widehat\tau$、$\sigma=\eta\widehat\sigma$。
其中辅助量使用相同实际传播子和相同低带，满足

$$\begin{aligned}
(\mathcal L_e+\Delta_e)\widehat\tau&=8uf_2,\qquad\widehat\tau(0)=0,\\
(\mathcal L_o+\Delta_o)\widehat\sigma&=-\mathcal K(\widehat\tau-1),
\end{aligned}\tag{6}$$

这里 $\Delta_e$、$\Delta_o$ 的符号分别是
$d_{2p+2j}-d_{2j}$、$d_{2p+2j+1}-d_{2j+1}$。
实际完整端点在本环内准确等于

$$4^DpC_D=\widehat{\mathfrak C}
:=-[u^m]f_1(\widehat\tau-1)
-16[u^{m-1}]f_2\{\widehat\sigma+2a(\widehat\tau-1)\}.\tag{7}$$

这一步用了 ghost 稿证明的 $(\eta-1)\widehat{\mathfrak C}=0$；
直接 ghost 和由它引起的响应各自不为零，不能分别省略。
式 (6) 只是同一个实际有限系统的缩放辅助解，不是另一动力模型。

### Step 2. 准确传播子及下一二次项

定义整数 Chebyshev 多项式
$C_n=z^n+z^{-n}$、$S_n=(z^n-z^{-n})/(z-z^{-1})$、$H=2-z-z^{-1}$。
已接受的准确特征 $p$ 身份为

$$d_{2p+n}-d_n
=\lambda_H(1-H^p/2)S_n
+(-2H^{p-1}+H^{2p-1}/2)(2+Hd_n),$$
$$\lambda_H=\chi H^m(4-H)^{m+1}.$$

在本次环内，它给出

$$\boxed{d_{2p+n}-d_n
=\lambda_HS_n-4H^{2m}-2H^p d_n.}\tag{8}$$

因此必须保留 $-2H^p d_n$。被省去的首个第一类项高度为 $m+p$，
其余项更高；因为 $m\ge2$，这些高度均至少为 $p+1$。
记 $S_eu^j=S_{2j}u^j$、$S_ou^j=S_{2j+1}u^j$。
又在 $\mathbb F_p[H]$ 中有

$$\frac{\lambda_H^2}{H^{2m}}=(4-H)^{p+1}
=16-4H\pmod{H^2}.\tag{9}$$

式 (9) 用 $(4-H)^p=4-H^p$，而不是将 $\lambda_H^2/H^{2m}$
错误视为常数 $16$ 到下一层。
Chebyshev 初值和递推给

$$S_n=n-\frac{n(n^2-1)}6H+O(H^2),\qquad
d_n=-n^2+\frac{n^2(n^2-1)}{12}H+O(H^2).\tag{10}$$

### Step 3. 二次响应的有限方程

保留已接受的精确低带组合

$$\tau^{\rm b}=-2\Theta w,\quad \sigma^{\rm b}=-\mathcal Q a,\quad
Z=(\mathcal E-\Theta)w,\quad T=(\mathcal E-\Theta-1)a.$$

基带和线性 Ward 身份使辅助解可写为

$$\begin{aligned}
\widehat\tau&=\tau^{\rm b}+\lambda_HZ+H^{2m}(X_0+HX_1),\\
\widehat\sigma&=\sigma^{\rm b}+\lambda_HT+H^{2m}(Y_0+HY_1)
\end{aligned}\tag{11}$$

于本次环及各自有限 $u$ 范围中成立。
所有被排除的三次移位反馈高度至少为 $3m\ge2m+2=p+1$。
最小情形 $p=5,m=2$ 是等号，恰在本环中为零，不能用于再下一层。
由非共振三角对角元为单位，构造 (11) 等价于唯一的实际辅助解。

写 $X(H)=X_0+HX_1$、$Y(H)=Y_0+HY_1$、$c(H)=16-4H$。
将式 (8)—(11) 代入式 (6)，扣去基带和线性 Ward 方程，得到模 $H^2$ 的系统

$$\begin{aligned}
\mathcal L_eX&=(4+2H\mathcal D_e)\tau^{\rm b}-c(H)S_eZ,\\
\mathcal L_oY&=-\mathcal KX+(4+2H\mathcal D_o)\sigma^{\rm b}-c(H)S_oT.
\end{aligned}\tag{12}$$

其中 $X(0)=0$ 指 $u$ 常数项。这个系统同时保留移位的常数二次项、
非恒定二次项以及线性移位再次作用于线性响应的贡献。

所需低带为

$$w_0=-\log(1-u),\quad a_0=f/2,\quad
w_1=\frac{u(1+u)f^2}{4},\quad
a_1=\frac{(1+16u+7u^2)f^3-G\mathscr H}{48}.\tag{13}$$

定义

$$\begin{gathered}
\mathcal D_{e0}=-4\Theta^2,\quad \mathcal D_{o0}=-\mathcal Q^2,\quad
\mathcal D_{e1}=(4\Theta^4-\Theta^2)/3,\quad
\mathcal D_{o1}=(\mathcal Q^4-\mathcal Q^2)/12,\\
S_{e0}=2\Theta,\quad S_{o0}=\mathcal Q,\quad
S_{e1}=-(8\Theta^3-2\Theta)/6,\quad
S_{o1}=-(\mathcal Q^3-\mathcal Q)/6,\\
\mathcal L_{e0}=\mathcal D_{e0}+8ug,\quad
\mathcal L_{o0}=\mathcal D_{o0}+8ug,\quad
\mathcal L_{e1}=\mathcal D_{e1}+16ugw_1,\quad
\mathcal L_{o1}=\mathcal D_{o1}+16ugw_1,\\
K_0=f/2+8uf^3,\quad K_1=fw_1/2+16ug(a_1+2w_1a_0).
\end{gathered}\tag{14}$$

下标 $0,1$ 在本节表示 $H$ 系数，不是 $u$ 系数。于是

$$\begin{gathered}
Z_0=-uf,\quad Z_1=(1-\Theta)w_1,\quad
T_0=-g/2,\quad T_1=-\Theta a_1,\\
\tau^{\rm b}_0=-2uf,\quad\tau^{\rm b}_1=-2\Theta w_1,\quad
\sigma^{\rm b}_0=-\mathcal Q a_0,\quad\sigma^{\rm b}_1=-\mathcal Q a_1.
\end{gathered}\tag{15}$$

二次零层的已接受解是

$$X_0=4\ell-2G\mathscr D,\qquad
Y_0=-(1+u)f^2\mathscr D-2f\ell-2f-4G\mathscr H.\tag{16}$$

式 (12) 的一次系数给出本件的新方程

$$\boxed{\mathcal L_{e0}X_1=P_1,\qquad
\mathcal L_{o0}Y_1+K_0X_1=Q_1,}\tag{17}$$

其中全部右端已知，准确为

$$\begin{aligned}
P_1={}&4\tau^{\rm b}_1+2\mathcal D_{e0}\tau^{\rm b}_0
-16S_{e0}Z_1-(16S_{e1}-4S_{e0})Z_0-\mathcal L_{e1}X_0,\\
Q_1={}&-K_1X_0+4\sigma^{\rm b}_1+2\mathcal D_{o0}\sigma^{\rm b}_0
-16S_{o0}T_1-(16S_{o1}-4S_{o0})T_0-\mathcal L_{o1}Y_0.
\end{aligned}\tag{18}$$

这些式子定义唯一 $X_1,Y_1$；无需对 $\mathscr H$ 的共振后系数求逆。

### Step 4. 完整端点与有限伴随引理

基带端点为零，线性端点保持准确 Ward 身份
$-\lambda_H(\mathcal E-m)B_{\rm low}$。
二次零层端点 $\mathfrak c_{2,0}$ 已接受为零。
式 (7)、(11) 的新二次系数准确为

$$\begin{aligned}
\mathfrak c_{2,1}={}&-[u^m]f(X_1+w_1X_0)\\
&-16[u^{m-1}]g\{Y_1+2a_0X_1+2a_1X_0
+2w_1(Y_0+2a_0X_0)\}.
\end{aligned}\tag{19}$$

本式中的 $a_1X_0$ 和指数变化项均不能删除。

**有限伴随引理。** 对任何 $X(0)=0$ 的有限级数 $X$ 至次数 $m$、
任意 $Y$ 至次数 $m-1$，置 $P=\mathcal L_{e0}X$、
$Q=\mathcal L_{o0}Y+K_0X$。则在 $\mathbb F_p$ 中

$$\boxed{\begin{aligned}
\mathcal C(X,Y)&:=-[u^m]fX-16[u^{m-1}]g(Y+fX)\\
&=-2\sum_{j=1}^m jP_j+4\sum_{j=0}^{m-1}Q_j.
\end{aligned}}\tag{20}$$

**证明。** 将两侧展开为 $X_j,Y_j$ 的线性组合。
左端的 $X_j$ 系数为 $-1-8(m-j)(m-j+1)$，
$Y_j$ 系数为 $-16(m-j)$。
右端的 $Y_j$ 系数为

$$-4(2j+1)^2+16(m-j-1)(m-j).$$

它减去左端系数等于 $4p(p-2-4j)$。
对 $X_j$，令 $t=m-j$；利用
$[u^r]K_0=1/2+4r(r+1)$，右端系数是

$$8j^3-16\sum_{r=1}^{t}r(j+r)
+4\sum_{r=0}^{t-1}\{1/2+4r(r+1)\}
=8j^3-8jt(t+1)-8t^2-6t.$$

减去左端系数后得到

$$8j\{j^2-t(t+1)\}+2t+1
=p(8j^2-2pj+1).$$

这些精确差在模 $p$ 后均为零。所用有限和公式只有分母 $2,3$；
$X_0=0$ 排除未定义的偶常数反演。故 (20) 成立。$\square$

将式 (17) 代入引理，式 (19) 变为

$$\mathfrak c_{2,1}=[u^{m-1}]\mathcal N(u),\tag{21}$$

其中完全已知的核是

$$\mathcal N=-\frac{2f}{u}\Theta P_1-\frac{f}{u}w_1X_0+4fQ_1
-32g\{a_1X_0+w_1(Y_0+fX_0)\}.\tag{22}$$

前两个分子均无常数项，故除以 $u$ 不产生负次项。
最高被提取的原输入次数至多为 $m$，仍在已经说明的整性窗口内。

### Step 5. 已知核的六项分解

用式 (5) 对式 (13)—(18) 求导，再代入式 (22)，得到

$$\mathcal N=A_{\ell H}\ell\mathscr H+A_{DH}\mathscr D\mathscr H
+A_D\mathscr D+A_\ell\ell+A_H\mathscr H+A_0.\tag{23}$$

六个有理核为

$$\begin{aligned}
A_{\ell H}&=\frac{8(1+u)^2}{3(1-u)^4},&
A_{DH}&=-\frac{4(1+u)^3}{3(1-u)^5},\\
A_D&=-\frac{3u^4+494u^3+2168u^2+1138u+37}{6(1-u)^6},\\
A_\ell&=\frac{-7u^4-272u^3+686u^2+1392u+121}{3(1-u)^6},\\
A_H&=\frac{4u(41u^3+445u^2+427u+47)}{3(1-u)^6},\\
A_0&=-\frac{2(15u^3+236u^2+139u-6)}{3(1-u)^5}.
\end{aligned}\tag{24}$$

这一步仅为已定义有限微分表达式的代数化简。
例如式 (18) 的第一源明确展开为

$$P_1=\frac{4u(1+u)(3u^2+16u+1)}{(1-u)^5}\mathscr D
-\frac{8u(13u^2+40u+7)}{3(1-u)^4}\ell
-\frac{2u(u^3-80u^2-71u+6)}{3(1-u)^4}.$$

对第二源使用同一式 (5) 后，乘式 (22) 中的 $4f$；
分别收集 $\ell\mathscr H,\mathscr D\mathscr H,\mathscr D,\ell,\mathscr H,1$
即得到式 (24) 的六个分子。这六项可各自按式 (18)、(22) 原定义直接核验，
不依赖猜测 $X_1,Y_1$ 的全局有理性。

为后续有限和，令 $a_*(n)=[u^n]A_*$，则对全部整数 $n\ge0$，
式 (24) 等价于以下特征零多项式身份：

$$\begin{aligned}
a_{\ell H}(n)&=\frac{8(n+1)(2n^2+4n+3)}9,\\
a_{DH}(n)&=-\frac{4(n+1)^2(n^2+2n+3)}9,\\
a_D(n)&=-\frac{(n+1)(96n^4+473n^3+811n^2+549n+111)}{18},\\
a_\ell(n)&=\frac{(n+1)(48n^4+432n^3+1162n^2+1172n+363)}9,\\
a_H(n)&=\frac{2n(n+1)(48n^3+72n^2+16n+5)}9,\\
a_0(n)&=-\frac{(n+1)(96n^3+208n^2+59n-36)}9.
\end{aligned}\tag{25}$$

每一行均由 $[u^n](1-u)^{-d}=\binom{n+d-1}{d-1}$
按分子逐项展开、整体化简得到。
虽然未化简的二项式可能使用分母 $120$，式 (25) 的最终分母只有 $2,3$；
本件只在式 (25) 整体成立后约化，不在 $p=5$ 时对 $120$ 求逆。

### Step 6. 全部单和、双和的精确消去

由式 (23) 的卷积，式 (21) 在特征零可写为

$$\begin{aligned}
\mathfrak c_{2,1}={}&a_0(m-1)
+\sum_{r=0}^{m-1}\frac{a_H(m-1-r)}{2r+1}\\
&+\sum_{k=1}^{m-1}\left\{-\frac{a_\ell(m-1-k)}k
+\frac{a_D(m-1-k)}{k^2}\right\}\\
&+\sum_{k=1}^{m-1}\sum_{r=0}^{m-1-k}
\left\{-\frac{a_{\ell H}(m-1-k-r)}{k(2r+1)}
+\frac{a_{DH}(m-1-k-r)}{k^2(2r+1)}\right\}.
\end{aligned}\tag{26}$$

以下等式在 $\mathbb F_p$ 中使用 $m=-1/2$ 约化被加数的多项式系数，
但求和上限始终是原整数 $m$，不是替换求和区间。
所有 $k$ 和 $2r+1$ 均在 $1,\ldots,p-1$ 内，可以求逆。
由式 (25)，第一项变为 $13/12$，第三行的单和被加数为

$$U(k)=\frac{16}3k^4-8k^3-\frac{29}2k^2-\frac23k
+\frac74+\frac5{96k^2},\tag{27}$$

奇单和的被加数为

$$V(r)=-\frac{16}3r^4-24r^3-\frac{340}9r^2-\frac{205}9r-\frac{19}6.\tag{28}$$

双和被加数的准确部分分式分解为

$$\frac{4k^2}{3(2r+1)}+B(k,r),\tag{29}$$
$$B(k,r)=-\frac{2r^3}{9k^2}-\frac{r^2}{3k^2}
-\frac{r(11-24k^2)}{18k^2}
+\frac{64k^3+24k^2-16k-9}{36k^2}.$$

式 (27)—(29) 由式 (25) 直接多项式除法得到。
对多项式部分，先在特征零求和，准确有

$$\sum_{r=0}^{m-1-k}B(k,r)
=-\frac{(k-m)(42k^3+18k^2m+6km^2-9k-2m^3-7m)}{36k^2}.$$

再约化 $m=-1/2$ 得

$$\sum_{r=0}^{m-1-k}B(k,r)
=-\frac76k^2-\frac13k+\frac13-\frac5{96k^2}.\tag{30}$$

因此式 (27) 中的倒数平方项与式 (30) 恰消去，二者之和是

$$A(k)=\frac{(2k+1)(32k^3-64k^2-62k+25)}{12}.\tag{31}$$

对式 (29) 的奇倒数项交换有限求和，得到

$$\begin{aligned}
\frac43\sum_{k=1}^{m-1}k^2\sum_{r=0}^{m-1-k}\frac1{2r+1}
&=\frac29\sum_{r=0}^{m-1}
\frac{(m-r-1)(m-r)(2m-2r-1)}{2r+1}\\
&=-\sum_{r=0}^{m-1}\frac{(2r+3)(r+1)}9.
\end{aligned}\tag{32}$$

第一式使用有限平方和；新加的末端 $r=m-1$ 的分子为零。
第二式是在剩余域中将 $m=-1/2$ 代入被加数后，
用 $m-r=-(2r+1)/2$ 约掉合法单位 $2r+1$ 得到。
因此没有未受控制的奇调和和留下。
合并式 (28)、(32) 的被加数为

$$B_*(r)=-\frac{(2r+3)(16r^3+48r^2+42r+7)}6.\tag{33}$$

综上，式 (26) 化为

$$\mathfrak c_{2,1}=\frac{13}{12}
+\sum_{k=1}^{m-1}A(k)+\sum_{r=0}^{m-1}B_*(r).\tag{34}$$

为统一包含 $p=5$，在使用幂和公式之前先合并同下标项。
直接展开式 (31)、(33) 给

$$A(k)+B_*(k)=-32k^3-\frac{161}3k^2-\frac{73}3k-\frac{17}{12},$$
$$13/12+B_*(0)=-29/12.$$

所以式 (34) 只需次数至多三的幂和：

$$\begin{aligned}
\mathfrak c_{2,1}
&=-\frac{29}{12}+\sum_{k=1}^{m-1}
\left(-32k^3-\frac{161}3k^2-\frac{73}3k-\frac{17}{12}\right)\\
&=-\frac{288m^4+68m^3-240m^2-65m+36}{36}
=-\frac12\quad\text{于 }\mathbb F_p.
\end{aligned}\tag{35}$$

最后一步代入 $m=-1/2$，分子成为 $18$。
从式 (27) 到式 (35) 所用固定分母只含 $2,3$，
无需在 $p=5$ 时使用四次幂和的含 $1/5$ 表达式。
这证明式 (1)，包括最小素数边界。$\square$

### Step 7. 合并同轮输入并回到实际最高系数

式 (7)、(11)、完整 Ward 乘积身份和式 (19) 给

$$4^DpC_D=-\lambda_H(\mathcal E-m)B_{\rm low}
+H^{2m}\{\mathfrak c_{2,0}+H\mathfrak c_{2,1}\}
\pmod{H^{p+1}}.\tag{36}$$

已接受二次边界给 $\mathfrak c_{2,0}=0$，本件给 $\mathfrak c_{2,1}=-1/2$，
同轮第一 forcing 稿式 (4) 给线性项 $H^p$ 系数 $-1/4$。
首个有限参照误差已经通过式 (6)—(7) 的真实共同缩放计入；其净贡献为零。
故

$$4^DpC_D=-\frac34H^p\pmod{H^{p+1}}.$$

实际比较之前，所有所用正规化高带、指数和端点都已整。
在剩余域中 $4^m=2^{p-1}=1$，因此

$$4^D=4^{3m+1}=4,$$

不是 $16$。于是实际剩余为 $-3/16$。
因 $p\ge5$，$3$ 和 $16$ 都是单位，这个剩余非零。
这证明式 (2) 及 $v_h(pC_D)=p$。
首一性给

$$[L^p]U_{\rm cl}=h^{-D}p^2C_D,$$

其赋值为 $M-D+p=M-m$，式 (3) 得证。

### Step 8. 新精度的实际误差审计

| 来源 | 本层准确处理或排除界 |
| --- | --- |
| 有限参照首误差 | 同轮 ghost 稿准确计算为 $-cH^pu^p(1-u)^{-c}/4$，完整高带共同缩放后净端点贡献为零 |
| $pW_p$ 和中间奇响应乘整低指数 | $M-2m\ge3m\ge p+1$，包括 $p=5$ 时等号 |
| 非整指数与中间奇响应相遇 | 最短次数 $p+m$，严格超过端点目标 $p+m-1$ |
| 两个高带乘积 | 最短次数 $2p>D$，不出现 |
| 模 $p$ Chebyshev 系数代入实际 $h$ | 误差高度 $M\ge p+1$ |
| 新非恒定二次移位 | $-2H^pd_n$ 已在式 (8)、(12)、(18) 保留 |
| 线性移位平方系数的一次变化 | $\lambda_H^2/H^{2m}=16-4H+O(H^2)$ 已保留 |
| 低带一次变化及端点乘积变化 | 式 (13)—(19) 完整保留，包括 $a_1X_0$ |
| 二次修正之后的三次反馈 | 至少 $H^{3m}$，而 $3m\ge p+1$；$p=5$ 恰在排除边界 |
| 二次源中省去的低带二次变化 | 至少 $H^{2m+2}=H^{p+1}$ |
| 线性 Ward 项的任意高低带变化 | 完整形式身份保留，只按 $B_{\rm low}$ 的合法系数提取，不将实际数值直接求导 |

### 作者侧定向代数核验

使用自由符号的有理函数运算执行下列检查，没有素数扫描或根拟合：

1. 用式 (5) 的微分代数计算式 (18) 的两个右端；代入式 (22) 后，
   六个独立单项 $\ell\mathscr H,\mathscr D\mathscr H,\mathscr D,\ell,\mathscr H,1$
   的系数与式 (24) 全部一致。
2. 核对式 (24)—(25) 六个系数多项式身份，残差均为零。
3. 核对式 (27)—(30) 的部分分式与有限求和身份，残差均为零。
4. 核对式 (31)—(35) 的合并、三次有限和和 $m=-1/2$ 剩余，残差均为零。

这些核验是作者侧的可复算代数辅助，不替代本件及两个同轮输入的非作者独审。
本件没有新建脚本、数值实验、模型参数或拟合阈值。

## Corrections or Missing Assumptions

- 不能只沿用模 $H^p$ 的旧有限参照；本件依赖同轮 ghost 稿的新首误差及其真实反馈证明。
- 不能把 $\lambda_H^2/H^{2m}$ 在新层继续写成常数 $16$，也不能漏掉 $-2H^pd_n$。
- $X_1,Y_1$ 不需要全局闭式；有限伴随引理直接证明其完整端点，
  而非假设这些未知响应为零。
- 式 (35) 前必须先合并四次项，避免在 $p=5$ 时非法约化含 $1/5$ 的独立幂和表达式。
- 最高权重因子是 $4^D\equiv4$；因此实际剩余为 $-3/16$。

## Open Risks and handoff

- 本件与同轮第一 forcing／ghost 稿仍须真正非作者独立审查；作者计算成功不等于接受登记。
- 若这三份作者输入均通过独审，式 (3) 可作为此前条件负 Newton 图推论的非零锚点；
  相关统一因子结论和组合审计由主控另行完成，本件不代替那一步。
- 不在本件推断野分裂域、不同负根的全部距离，或一般第一／第二／第三 forcing 的互素性。
- 再提高精度时 $p=5$ 的 $H^{3m}=H^{p+1}$ 反馈和实际中间污染都会进入，
  不可把本件的误差表当作无限精度身份。
- 本件没有创建 Paper30 正式项目、稿件、PDF、Route 评分或外部效力。
