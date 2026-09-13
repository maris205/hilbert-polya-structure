# Proof Package：有限参照的首个 $h^p$ ghost 及其完整端点贡献

日期：2026-09-08。作者：`/root/negative_hp_ghost_author`。
本件只处理有限参照在新精度的首个误差及其引发的高带源响应；
不计算其他 $h^p$ 响应，不改旧稿、入口、接受处置或发布状态。
使用 proof-writer；本件为作者证明包，尚不构成非作者独审。

## Claim

固定任意素数 $p\ge5$、$a\ge2$，保持同一实际双谐波分支及规范

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m=3m+1,
\qquad C_D=[L^D]\mathcal B_3.
$$

设 $W$ 是下述实际偶低带，定义准确有限参照

$$
T(u)=\sum_{r=1}^{p-1}W_ru^r,\qquad
Q_{\rm ref}(u)=T(u)-\sum_{r=1}^{p-1}\frac{u^r}{r},\qquad
G(u)=-\log(1-u)+Q_{\rm ref}(u).
\tag{1}
$$

则对 $c=1,2$，先在特征零解释左侧指数，再逐系数乘 $p$，有

$$
\boxed{
p e^{cG}\equiv -\frac c4 h^p u^p(1-u)^{-c}
\pmod{(h^{p+1},u^{2p})}.}
\tag{2}
$$

这个同余包含所用系数乘 $p$ 后的整性，不声称 $e^{cG}$ 本身整。
令

$$
\delta=h^p/4,\qquad \eta=1+\delta,
\qquad \tau_j=pW_{p+j},\quad \sigma_j=pA_{p+j}.
$$

在 $\mathcal O^+/(h^{p+1})$ 中，所需实际正规化指数高带准确成为

$$
\boxed{E_c=c f_c(\tau-\eta),\qquad c=1,2.}
\tag{3}
$$

在与实际对象使用相同传播子、相同低带的有限高带方程中，
把 $\eta$ 改成 $1$ 所得唯一辅助解记为 $(\widehat\tau,\widehat\sigma)$。
则真实解及其完整端点满足

$$
\boxed{(\tau,\sigma)=\eta(\widehat\tau,\widehat\sigma),
\qquad 4^DpC_D=\eta\widehat{\mathfrak C},
\qquad \eta\widehat{\mathfrak C}=\widehat{\mathfrak C}.}
\tag{4}
$$

最后一个等式仅在模 $h^{p+1}$ 的工作环中成立：
首个有限参照 ghost 对完整最高端点的 $h^p$ 系数贡献为零。
这不判断 $h^{-p}pC_D$ 的实际剩余是否为零；
传播子非恒定二次移位、低带变化及其他新响应仍须另算。

## Status

**PROVABLE AS STATED。** 证明先计算乘 $p$ 后指数展开的唯一存活项，
再用实际支撑还原高带方程，最后利用单位三角性证明整体缩放。
不依赖任何未证明的全局有理核整性。

## Assumptions

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为本原 $p^a$ 次根，
  $K^+=\mathbb Q_p(h)$，$\mathcal O^+=\mathbb Z_p[h]$，
  $v_h(h)=1$，$v_h(p)=M$，剩余域为 $\mathbb F_p$。
- 实际传播子为 $d_n=-(2-\zeta^n-\zeta^{-n})/h$。
  对所需 $1\le n<3p<p^a$，非共振 $d_n$ 为单位；
  $v_h(d_p)=v_h(d_{2p})=2m$。
- 实际权重低带由 $u=Lx^2/4$、$V|_{b=0}=W(u)$、
  $\partial_bV|_{b=0}=xA(u)$ 定义，且满足

  $$
  d_{2r}W_r=-4[u^{r-1}]e^{2W},\qquad
  d_{2r+1}A_r=-\frac12[u^r]e^W-8[u^{r-1}]e^{2W}A,
  \tag{5}
  $$

  $$
  4^DC_D=-[u^{p+m}]e^W-16[u^{p+m-1}]e^{2W}A.
  \tag{6}
  $$
- 已接受的有限整性与支撑如下：$W_r\in\mathcal O^+$、
  $W_r\equiv1/r\pmod h$ 对 $1\le r<p$；
  $A_r\in\mathcal O^+$ 对 $0\le r<m$；
  $pW_{p+j}$ 对 $0\le j\le m$、$pA_{p+j}$ 对 $0\le j<m$ 均整；
  $v_h(W_p)\ge-2m$，$v_h(A_r)\ge-2m$ 对 $m\le r<p$。
  零阶低奇带为 $A_r\equiv1/2\pmod h$ 对 $r<m$。

这些有限实际身份和整性使用
[已接受后临界稿 Step 1—2](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md)
及 [完整二次边界稿 Step 1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)。
本件不把此前参照误差 $O(h^p)$ 直接用于新精度；式 (2) 是新计算。

## Notation

置

$$
\mathscr R=\mathcal O^+/(h^{p+1}),\qquad
w=T\text{（仅在所需低次数使用）},\qquad
a=A_{<m},\qquad f_c=e^{cw}\ (c=1,2).
$$

$f_c$ 只提取次数小于 $p$ 的系数，因此指数阶乘均为单位。
因为 $m\ge2$，有

$$
M\ge5m\ge p+1,\qquad
M-2m\ge3m\ge p+1.
\tag{7}
$$

故 $\mathscr R$ 的特征为 $p$。式 (2) 的同余按 $u^N$、$N<2p$
逐系数解释；不对无限高指数系数作整性断言。
有限高带及正规化指数定义为

$$
\tau=\sum_{j=0}^{m}\tau_ju^j\pmod{u^{m+1}},\qquad
\sigma=\sum_{j=0}^{m-1}\sigma_ju^j\pmod{u^m},
\qquad [u^j]E_c=p[u^{p+j}]e^{cW}.
\tag{8}
$$

所需 $E_c$ 下标为 $0\le j\le m$；
含 $E_2a$ 的端点只提取 $u^{m-1}$。
记 $\Theta=u\partial_u$、$\mathcal Q=2\Theta+1$，并定义有限对角算子

$$
\mathcal D_eu^j=d_{2j}u^j,\quad
\mathcal D_ou^j=d_{2j+1}u^j,\quad
\Delta_eu^j=(d_{2p+2j}-d_{2j})u^j,\quad
\Delta_ou^j=(d_{2p+2j+1}-d_{2j+1})u^j,
$$

$$
\mathcal L_e=\mathcal D_e+8uf_2,\qquad
\mathcal L_o=\mathcal D_o+8uf_2,\qquad
\mathcal K=\frac{f_1}{2}+16uf_2a.
\tag{9}
$$

偶常数项固定为 $\tau_0=0$，不用 $d_0^{-1}$。
其余偶下标为 $1\le j\le m$，奇下标为 $0\le j<m$。

## Proof Strategy

先在特征零有限指数展开中做 $h$-高度审计。
唯一可能留下的项是 $Q_{\rm ref}^p/p!$，其剩余由有限域 Frobenius 和
实际 $W_1=4/(4-h)$ 决定。随后以 $G_{<p}=W_{<p}$ 的准确匹配
转回实际高带。新的缺陷常数 $\eta$ 同时出现于两条高带方程，
线性齐次结构使其成为共同缩放。最后只需零阶完整端点含 $p$ 因子的身份，
而不需重算此前各个已消失的 $h$ 层。

## Dependency Map

1. 式 (2) 使用 $Q_{\rm ref}\in h\mathcal O^+[u]$、
   $M\ge p+1$、$N<2p$ 及准确 $W_1$。
2. 式 (3) 使用式 (2)、$W-G$ 从 $u^p$ 开始和已接受正规化高带整性。
3. 真实高带方程与端点使用式 (5)—(6)、式 (7) 及有限乘积支撑。
4. 整体缩放使用非共振对角元为单位与偶常数项固定为零。
5. 端点贡献消失只使用零阶低解和 $2m+1=p$；
   不使用最高系数下一层已经非零或已经为零的假设。

## Proof

### Step 1. 有限参照误差的整性、唯一存活项和常数

由假设，$Q_{\rm ref}\in h\mathcal O^+[u]$，没有常数项，次数小于 $p$。
准确特征零身份为

$$
e^{cG}=(1-u)^{-c}\sum_{q\ge0}\frac{c^q Q_{\rm ref}^q}{q!}.
\tag{10}
$$

因为 $c=1,2$，$(1-u)^{-c}$ 的全部系数是整数。
固定 $N<2p$。无常数项条件使 $u^N$ 内只出现 $0\le q\le N$：

- 当 $q<p$，$q!$ 是 $p$ 单位，乘 $p$ 后的高度至少为
  $M+q\ge p+1$。
- 当 $p<q<2p$，$v_p(q!)=1$，故 $p/q!$ 为 $p$ 单位，
  乘 $Q_{\rm ref}^q$ 后高度至少为 $q\ge p+1$。
- 当 $q=p$，$p/p!=1/(p-1)!$ 为单位，可能留下高度 $p$ 的系数。

因此全部所需 $p[u^N]e^{cG}$ 均整，且模 $h^{p+1}$ 只余

$$
(1-u)^{-c}\frac{c^p}{(p-1)!}Q_{\rm ref}^p.
\tag{11}
$$

写 $Q_{\rm ref}=hR$，$R\in\mathcal O^+[u]$，并在剩余域中约化。
非零有限域元素与其逆元配对后只剩 $1,-1$，故
$(p-1)!\equiv-1\pmod p$。又 $c^p=c$ 于 $\mathbb F_p$，所以

$$
\frac{c^p}{(p-1)!}\overline R^{,p}=-c\overline R^{,p}.
\tag{12}
$$

有限域 Frobenius 给
$\overline R^{,p}=\sum_{r=1}^{p-1}\overline{R_r}^{,p}u^{rp}$。
在次数小于 $2p$ 的范围内只有 $r=1$ 保留。
式 (5) 的 $r=1$ 偶方程与准确 $d_2=h-4$ 给

$$
W_1=\frac4{4-h},\qquad
R_1=\frac{W_1-1}{h}=\frac1{4-h},\qquad
\overline{R_1}=\frac14.
\tag{13}
$$

于是 $\overline R^{,p}=u^p/4\pmod{u^{2p}}$。
将此代回 (11)—(12)，得到式 (2)。这个推导从未对含 $1/p!$
的单独非整指数先行约化；约化发生在乘 $p$ 并证明整性之后。

### Step 2. 从参照转回实际指数高带

由定义，$G_{<p}=W_{<p}$ 准确，而 $G_r=1/r$ 对 $r\ge p$。
因此 $W-G$ 从 $u^p$ 开始，模 $u^{2p}$ 的特征零身份为

$$
e^{cW}=e^{cG}\{1+c(W-G)\}.
\tag{14}
$$

对 $0\le j\le m<p$，有

$$
pG_{p+j}=\begin{cases}1,&j=0,\\p/(p+j),&j>0,\end{cases}
\qquad pG_{p+j}\equiv\mathbf1_{j=0}\pmod{h^{p+1}}.
\tag{15}
$$

第二式使用 $p+j$ 在 $j>0$ 时为单位及 $M\ge p+1$。
式 (14) 的乘积在所需系数中只用 $e^{cG}$ 的下标小于 $p$ 的低系数，
它们整且与 $f_c$ 准确相同；$p(W-G)$ 的所需系数也整。
故式 (2)、(14)—(15) 合并为

$$
E_c=c f_c(\tau-1)-\frac c4h^p(1-u)^{-c}.
\tag{16}
$$

所用低范围有 $f_c\equiv(1-u)^{-c}\pmod h$，
因为 $W_r\equiv1/r$ 且低指数阶乘为单位。
在乘 $h^p$ 后可将 (16) 的最后一个低核换为 $f_c$，得到式 (3)。
至此两个符号已经固定：参照指数首误差为负号，
实际缺陷常数从 $1$ 变为 $1+h^p/4$。

### Step 3. 在新精度核对实际乘积支撑

由 $v_h(W_p)\ge-2m$ 与 (7)，在 $\mathscr R$ 中 $\tau_0=pW_p=0$。
对实际 $p[u^N]e^{2W}A$，其中 $N\le p+m-1$，按 $A$ 的下标分类：

1. 若 $A$ 下标 $r<m$，则它是整低系数。指数高带的贡献正是 $E_2a$；
   指数下标小于 $p$ 的部分乘 $p$ 后高度至少 $M\ge p+1$。
2. 若 $m\le r<p$，指数下标 $N-r\le p-1$，仍是整低系数；
   此类乘积乘 $p$ 后高度至少 $M-2m\ge p+1$，故消失。
3. 若 $r\ge p$，所需 $r=p+j$，$0\le j<m$；
   相乘指数下标小于 $m<p$，贡献正是 $f_2\sigma$。

此外，非整指数与中间奇响应的最短相遇次数为 $p+m$，
严格超过目标 $p+m-1$；两个高带相乘最短次数为 $2p$，也不出现。
所以在全部所需次数内准确有

$$
p[u^{p+j}]e^{2W}A=[u^j](f_2\sigma+E_2a),\qquad 0\le j<m.
\tag{17}
$$

同一分类还给 $p[u^N]e^{2W}A=0$ 于 $\mathscr R$ 对 $N<p$ 成立，
因为这时没有指数或响应的 $p$ 高带；特别是奇入口所需 $N=p-1$ 为零。

这也说明最小情形 $p=5,m=2,a=2$ 没有遗漏污染：
其最坏高度 $M-2m=6=p+1$，在本工作环中恰好消失。

### Step 4. 实际方程与精确共同缩放

将式 (3)、(17) 代回实际递推 (5)，得到

$$
(\mathcal L_e+\Delta_e)\tau=8\eta uf_2\pmod{u^{m+1}},
\qquad \tau_0=0,
\tag{18}
$$

$$
(\mathcal L_o+\Delta_o)\sigma
=-\mathcal K(\tau-\eta)\pmod{u^m}.
\tag{19}
$$

式 (6) 的完整端点同时成为

$$
4^DpC_D=-[u^m]f_1(\tau-\eta)
-16[u^{m-1}]f_2\{\sigma+2a(\tau-\eta)\}.
\tag{20}
$$

在同一环中定义辅助有限解

$$
(\mathcal L_e+\Delta_e)\widehat\tau=8uf_2,
\quad\widehat\tau_0=0,\qquad
(\mathcal L_o+\Delta_o)\widehat\sigma
=-\mathcal K(\widehat\tau-1),
\tag{21}
$$

并定义 $\widehat{\mathfrak C}$ 为 (20) 右侧中
$(\tau,\sigma,\eta)$ 被 $(\widehat\tau,\widehat\sigma,1)$ 取代后的量。
这只是有限线性辅助系统，不声称它是另一个真实 forcing。

偶正下标对角元为 $d_{2p+2j}$，$1\le j\le m$；
奇对角元为 $d_{2p+2j+1}$，$0\le j<m$。
这些下标均不被 $p$ 整除，因此全为单位。
乘子 $8uf_2$ 严格增加 $u$ 次数，所以 (21) 可按次数唯一求解。

标量 $\eta$ 与全部算子及低核交换。
把 $\eta\widehat\tau$ 代入 (18)，再把
$\eta\widehat\sigma$ 代入 (19)，分别得到相同右端，
且偶常数项仍为零。由单位三角唯一性得到

$$
\tau=\eta\widehat\tau,\qquad\sigma=\eta\widehat\sigma.
\tag{22}
$$

式 (20) 每一项遂共同乘 $\eta$，给
$4^DpC_D=\eta\widehat{\mathfrak C}$。
这里没有丢弃 $h^p$ 对高带源的反馈，也未将任何传播子移位设为零。

### Step 5. 完整 ghost 端点为什么消失

只需计算 $\widehat{\mathfrak C}\pmod h$。
此时真实传播子为 $d_n=-n^2$，平移 $n\mapsto n+2p$ 不改变其剩余，
故 $\Delta_e=\Delta_o=0$。低函数是

$$
w_0=-\log(1-u),\qquad a_0=\frac1{2(1-u)},\qquad
f=\frac1{1-u},\quad g=f^2.
\tag{23}
$$

由低方程对 $u$ 求导或直接代入 (21)，再用单位三角唯一性，得到

$$
\widehat\tau_0^{\rm series}=-2\Theta w_0=-\frac{2u}{1-u},
\qquad
\widehat\sigma_0^{\rm series}=-\mathcal Q a_0
=-\frac{1+u}{2(1-u)^2}.
\tag{24}
$$

下标 $0$ 在 (24) 表示 $h$ 的零阶级数，不是 $u$ 常数项。
两个完整乘积具有身份

$$
f(\widehat\tau_0^{\rm series}-1)=-(1+2\Theta)f,
$$

$$
g\{\widehat\sigma_0^{\rm series}
+2a_0(\widehat\tau_0^{\rm series}-1)\}
=-(3+2\Theta)(ga_0).
\tag{25}
$$

例如第二式由 $\Theta g=2g\Theta w_0$ 与乘积法则展开即得。
提取两个目标系数，式 (25) 给

$$
\overline{\widehat{\mathfrak C}}
=(1+2m)[u^m]f+16\{3+2(m-1)\}[u^{m-1}]ga_0
=p\left([u^m]f+16[u^{m-1}]ga_0\right)=0.
\tag{26}
$$

所有参与系数都整；式 (26) 不含可抵消这个 $p$ 的 $1/p$ 分母。
因而 $\widehat{\mathfrak C}\in h\mathscr R$，从而

$$
(\eta-1)\widehat{\mathfrak C}
=\frac{h^p}{4}\widehat{\mathfrak C}=0\quad\text{于 }\mathscr R.
\tag{27}
$$

这完成式 (4)，且不借用此前已经接受的更强端点消失层。证毕。$\square$

### Step 6. 直接指数项与其源响应的符号复核

这一分拆用于防止只保留式 (16) 的直接 ghost 而遗漏响应。
若暂时固定 $\widehat\tau,\widehat\sigma$，只把端点中的缺陷 $1$
改成 $\eta$，直接增量为

$$
\delta\left([u^m]f+32[u^{m-1}]ga_0\right)
=\delta\{1+8m(m+1)\}=-\delta\quad\text{于 }\mathscr R,
\tag{28}
$$

其中 $m(m+1)=-1/4$ 于 $\mathbb F_p$。
由式 (22)，高带还增加
$\delta\widehat\tau_0^{\rm series}$ 和
$\delta\widehat\sigma_0^{\rm series}$；将 (24) 代入其端点增量给

$$
\delta\{2m+4m(m+1)(2m-1)\}=+\delta\quad\text{于 }\mathscr R.
\tag{29}
$$

式 (29) 的有限系数使用
$[u^n](1-u)^{-k}=\binom{n+k-1}{k-1}$；
化简后仅是所示整数多项式，故 $p=5$ 也无分母例外。
两式相加为零，分别确认了直接项的负号与源响应的正号。

### 定向作者核验记录

本件使用自由符号准确计算核对了七个残差：零阶偶方程、零阶奇方程、
式 (25) 的两个乘积身份、式 (28)—(29) 之和等于
$\delta(2m+1)^3$ 的多项式身份，以及直接项与响应项对 $2m+1$
分别约化为 $-\delta,+\delta$ 的两个多项式余式。
七个残差均为零。没有通过扫描特殊素数外推一般量词，
也没有把作者符号核验记为非作者独审。

## Corrections or Missing Assumptions

- 此前有限参照只有 $O(h^p)$ 误差；新精度不能把它直接设零。
  式 (2) 给出准确首误差，式 (18)—(27) 才证明完整端点贡献消失。
- 式 (2) 的 $N<2p$ 是实质范围：到 $N=2p$ 时
  $\overline R_2^{,p}u^{2p}$ 已进入，且实际高带乘积也可能出现。
- 共同缩放使用两条实际方程同时改变同一个缺陷常数；
  只改变端点指数会错误留下式 (28) 的非零项。
- $\widehat\tau,\widehat\sigma$ 是同一传播子下的辅助有限解，
  不是把原模型替换成理想传播子或换成另一构造。

## Open Risks

- 本件只排除了有限参照 ghost 对最高端点的净 $h^p$ 贡献。
  其他 $h^p$ 贡献及完整剩余 $\overline{h^{-p}pC_D}$ 不在结论内。
- 所用中间污染在 $p=5,a=2$ 时从 $h^{p+1}$ 开始；
  若再提高精度，不能继续沿用本件的舍去。
- 本件不推断其他商系数、完整负 Newton 图、准确根赋值或分裂域。
- 这是新的作者证明包；仍需真正非作者独立审查，
  不以本件的符号复核替代独审。
