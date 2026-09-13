# Paper 30：唯一例外首项根的一阶 Hensel 位移

日期：2026-09-07。作者证明探针 V1；不是独立核查票、Route 评价或论文验收。

## Claim

固定奇素数 $p\ge5$ 和 $1\le r<p$，令

$$
\zeta=e^{2\pi ir/p},\qquad h=2-\zeta-\zeta^{-1},\qquad
m=\frac{p-1}{2},\qquad \rho=-h,\qquad L=\rho\lambda.
$$

在完成实圆分局部环 $\mathcal O^+=\mathbb Z_p[h]$ 中，采用已接受的物理正频支及首项归一化

$$
S(L)=\frac{\widetilde C(L)}p,\qquad
\widetilde C(L)=\rho^{p-1}C_{r,p}(L/\rho),\qquad
\overline S(L)=1-L^m.
$$

设 $L_*$ 是 $S$ 在剩余类 $L\equiv1/4\pmod h$ 中唯一的 Hensel 根。则

$$
\boxed{S(1/4)\equiv\frac h{24}\pmod{h^2},\qquad
L_*\equiv\frac14-\frac h{48}\pmod{h^2}.}
\tag{1}
$$

该结论对全部上述 $p,r$ 成立；不是有限素数或数值根扫描的外推。
这里的算术根坐标只重写同一个固定参数多项式，不把动力系统的 $\lambda$ 改为随振幅调整。

## Status

`PROVABLE AS STATED`，原一阶根位移命题保持不变。

本文只给出唯一例外首项根的位置，**不**据此宣告该根处 $Q\ne0$，也不证明全部根实性。
此前已接受的奇素数首项平方自由定理不重新打开。

## Assumptions

- 采用同一双谐波映射、SUM action 和物理正 kick 规范，不更换模型。
- 采用[首项平方自由作者证明](PAPER30_TWIST_PRIME_SQUAREFREE_PROBE_V1_20260907.md)
  和[第一曲率作者证明 V2，第 7 节](PAPER30_TWIST_PRIME_POST_CANCELLATION_PROBE_V2_20260907.md)
  已核正的归一化：$S\in\mathcal O^+[L]$、$\deg S=m$、$\overline S=1-L^m$。
- 采用[上轮处置](PAPER30_TWIST_PRIME_SQUAREFREE_CURVATURE_DISPOSITION_20260907.md)
  中已接受的局部环事实：$h$ 是 $\mathcal O^+$ 的均匀化元，
  $\mathcal O^+/(h)=\mathbb F_p$，且 $p=u h^m$，其中 $u\in(\mathcal O^+)^\times$。
- 本文始终假定 $p\ge5$。于是 $12,24,48$ 均为 $p$-进单位，且 $m\ge2$。
  不用本式处理 $p=3$，亦不重开该分母的既有恢复证明。

## Notation

真实归一化传播子及低于共振阶的有限分支为

$$
D_n=2-\zeta^n-\zeta^{-n},\qquad d_n=-D_n/h,
$$
$$
V(x;L)=\sum_{n=1}^{p-1}V_n(L)x^n,\qquad
V_n=-\frac{E_{n-1}/2+L F_{n-2}}{d_n},\qquad
E=e^V,\quad F=e^{2V}.
\tag{2}
$$

负下标系数按零处理。式 (2) 的指数只取所需有限系数，至多涉及 $(p-1)!$；
本文不需要定义跨越 $p!$ 的约化指数。
真实首项为 $\widetilde C=-E_{p-1}-2L F_{p-2}$。

用独立形式变量 $H$ 表示传播子的形式变形；$H$ 与实际均匀化元 $h$ 必须区分。
上横线对 $\mathcal O^+$ 系数指模 $h$，对 $\mathbb Z_p$ 系数指模 $p$，
两者都取值于 $\mathbb F_p$。$L_0=1/4$ 表示 $\mathbb Z_p$ 中这个确切有理数，
不是提前把实际根固定在该值。

## Proof Strategy

先构造一个无 $p$-分母的有限 action 整提升 $\mathscr S(H,L)$，
只要求它在实际圆分参数 $H=h$ 时等于 $S(L)$。
在 $H=0$ 的特征零模型中，传播子不具有所需的反射对称性，不能直接使用驻值 envelope。
但其模 $p$ 约化恢复反射对称性；由于被微分的有限分支本身整，
该模 $p$ 驻值已足以计算 $\partial_H\mathscr S(0,L_0)\bmod p$。
最后利用 $p\in(h^2)$，把这个形式一阶计算转回实际局部根位移。

## Dependency Map

1. Chebyshev 型整数递推给出 $d_n(H)$ 及其一阶系数；此步不使用离开 $H=h$ 的反射。
2. 低于 $p$ 阶的三角递推使 $V_n(H,L)$ 与有限 action 都整；因此无隐藏的 $H^2/p$。
3. 在实际 $H=h$，反射与加权 Euler 身份给出 $\mathscr S(h,L)=S(L)$。
4. 仅在 $H=0$ 模 $p$ 使用驻值，得到一阶系数的显式有限求和。
5. 已接受的 $\overline S=1-L^m$ 控制常数项和根处导数；$m\ge2$ 排除常数 $p$ 项污染。
6. 完成离散赋值环中的简单根 Hensel 唯一提升，把近似根转成式 (1)。

## Proof

### Step 1. 传播子的整数形式提升

定义整数多项式 $B_n(H)$：

$$
B_0(H)=2,\qquad B_1(H)=2-H,\qquad
B_n(H)=(2-H)B_{n-1}(H)-B_{n-2}(H).
\tag{3}
$$

由相同递推及初值，$B_n(h)=\zeta^n+\zeta^{-n}$。
每个 $B_n(0)=2$，故

$$
d_n(H)=\frac{B_n(H)-2}{H}\in\mathbb Z[H],\qquad d_n(h)=d_n.
\tag{4}
$$

写 $B_n(H)=2+a_n H+b_n H^2+O(H^3)$。
递推的线性项给出 $a_n-2a_{n-1}+a_{n-2}=-2$，
$a_0=0,a_1=-1$，所以 $a_n=-n^2$。
二次项满足

$$
b_n-2b_{n-1}+b_{n-2}=(n-1)^2,\qquad b_0=b_1=0.
$$

多项式 $n^2(n^2-1)/12$ 具有同样的二阶差分与初值；递推唯一性因此给出

$$
\boxed{d_n(H)=-n^2+c_n H+O(H^2),\qquad
c_n=\frac{n^2(n^2-1)}{12}.}
\tag{5}
$$

在 $H=h$ 有 $d_n(h)=d_{p-n}(h)$。
但在独立形式变量 $H$ 上不主张 $d_n(H)=d_{p-n}(H)$；
其常数项在特征零一般已不相等。
所需较弱事实是

$$
\overline{d_n(0)}=-n^2=-(p-n)^2=\overline{d_{p-n}(0)}
\quad\text{于 }\mathbb F_p.
\tag{6}
$$

### Step 2. 无 $p$-分母的有限整提升

用 $d_n(H)$ 替换式 (2) 的传播子，唯一三角地定义 $V_n(H,L)$，$1\le n<p$。
因为 $d_n(0)=-n^2\in\mathbb Z_p^\times$，每个 $d_n(H)$ 在 $\mathbb Z_p[[H]]$ 中可逆。
所需指数系数只除以 $k!$，$k<p$；归纳得到

$$
V_n(H,L)\in\mathbb Z_p[L][[H]].
\tag{7}
$$

令 $\mathcal D_H(x^n)=d_n(H)x^n$。对任意有限系数向量 $v=(v_1,\ldots,v_{p-1})$，
写 $v(x)=\sum_{n=1}^{p-1}v_nx^n$，定义

$$
\Phi(v;H,b,L)=[x^p]\left(
\frac12v\mathcal D_Hv+\frac b2 x e^v+\frac L2x^2e^{2v}\right).
\tag{8}
$$

这里 $b$ 是临时的一步幅度，实际取 $b=1$。定义本证明的整提升

$$
\mathscr S(H,L)=-2\Phi(V(H,L);H,1,L).
\tag{9}
$$

它是一个有限多项式表达式与式 (7) 的复合，所以属于 $\mathbb Z_p[L][[H]]$。
给 $b$ 权重 $1$、$L$ 权重 $2$ 时，第 $n$ 个三角解的权重为 $n$；
有限 action 的权重为 $p$，故式 (9) 的 $L$ 次数一致有界于 $m$。
因此可以写成

$$
\mathscr S(H,L)=S_0(L)+H S_1(L)+H^2R(H,L),
\quad S_0,S_1\in\mathbb Z_p[L],\quad R\in\mathbb Z_p[L][[H]],
\tag{10}
$$

且代入拓扑幂零元 $H=h$ 后，余项确实属于 $h^2\mathcal O^+[L]$。
这里没有先形成某个含 $1/p$ 的 off-$H$ 表达式再约化；
尤其不存在 $H^2/p$ 使阶数下降的问题。

### Step 3. 只在实际圆分点识别首项

对式 (8) 的 $v_i$ 求导得

$$
\frac{\partial\Phi}{\partial v_i}
=\frac{d_i(H)+d_{p-i}(H)}2v_{p-i}
+\frac b2[e^v]_{p-i-1}+L[e^{2v}]_{p-i-2}.
\tag{11}
$$

在 $H=h$，真实反射 $d_i=d_{p-i}$ 使这些驻值方程恰好等于式 (2)
及其含 $b$ 的版本。记此时的临界值为 $G(b,L)$。
有限多项式链式法则消去临界分支的隐含导数；结合权重 $p$ 的 Euler 身份，得

$$
pG=b\,\partial_bG+2L\,\partial_LG
=\frac b2E_{p-1}+L F_{p-2}.
\tag{12}
$$

在 $b=1$，右端等于 $-\widetilde C/2$。于特征零中除以非零整数 $p$，
得到

$$
\boxed{\mathscr S(h,L)=-2G(1,L)=\frac{\widetilde C(L)}p=S(L).}
\tag{13}
$$

该证明同时说明除 $p$ 后的表达式整。
本文不把式 (12) 延伸为独立形式变量 $H$ 上的驻值身份，
也不声称 $\mathscr S(H,L)$ 在 off-$H$ 处等于三角终端首项除 $p$。

### Step 4. 模 $p$ 驻值足以计算一阶项

在 $H=0$，把式 (11) 与三角解代入后模 $p$ 约化。
由式 (6)，右端全部为零。因此

$$
\left.\frac{\partial\Phi}{\partial v_i}\right|_{v=V(0,L),\ H=0,\ b=1}
\in p\mathbb Z_p[L],\qquad 1\le i<p.
\tag{14}
$$

另一方面，式 (7) 保证 $\partial_HV_i(0,L)$ 仍整。
对式 (9) 求导时，链式法则的隐含分支项由式 (14) 在模 $p$ 下消失。
只剩显式传播子导数，故

$$
\boxed{\overline{S_1}(L)=
-\sum_{n=1}^{p-1}\overline{c_n}\,
\overline{V_n(0,L)}\,\overline{V_{p-n}(0,L)}.}
\tag{15}
$$

这一步没有声称特征零 $H=0$ 的梯度为零。
它只使用梯度可整除 $p$ 及分支导数整，两者合在一起已经足够。

### Step 5. 在例外残类计算有限和

当 $H=0,L=L_0=1/4$ 时，低于 $p$ 阶的平方传播子分支满足

$$
V_n(0,L_0)=\frac1{n2^n},\qquad 1\le n<p.
\tag{16}
$$

为直接核验此式，在特征零令 $W=-\log(1-x/2)$，$E_W=(1-x/2)^{-1}$。
对每个 $n\ge1$，

$$
\frac12[E_W]_{n-1}+\frac14[E_W^2]_{n-2}
=\frac1{2^n}+\frac{n-1}{2^n}=\frac n{2^n}=n^2W_n,
$$

其中 $n=1$ 的第二项为零。故 $W_n$ 满足 $d_n(0)=-n^2$ 的三角递推，
低于 $p$ 阶的唯一性给出式 (16)。随后才对这些有限且整的系数取模。

在 $\mathbb F_p$ 中，式 (16) 给出

$$
\overline{V_n(0,L_0)}\,\overline{V_{p-n}(0,L_0)}
=\frac1{n(p-n)2^p}=-\frac1{n^2 2^p}.
$$

代入式 (15)，得

$$
\overline{S_1}(L_0)
=\frac1{12\,2^p}\sum_{n=1}^{p-1}(n^2-1).
\tag{17}
$$

因为 $p\ge5$，在 $\mathbb F_p$ 中
$\sum_{n=1}^{p-1}n^2=p(p-1)(2p-1)/6=0$，
而 $\sum_{n=1}^{p-1}1=-1$，故括号内有限和为 $1$。
再由 $2^p=2$，得到

$$
\boxed{\overline{S_1}(L_0)=\frac1{24}.}
\tag{18}
$$

### Step 6. 常数 $p$ 项不污染实际一阶系数

由式 (10)、(13) 及已接受的首项约化，

$$
\overline{S_0}(L)=\overline S(L)=1-L^m.
$$

因为 $(1/4)^m=2^{-(p-1)}=1$ 于 $\mathbb F_p$，
$S_0(L_0)\in p\mathbb Z_p$。
又因 $m\ge2$ 和 $p=u h^m$，

$$
S_0(L_0)\in h^2\mathcal O^+.
\tag{19}
$$

式 (18) 给出 $S_1(L_0)-1/24\in p\mathbb Z_p$，
故 $h(S_1(L_0)-1/24)\in h^{m+1}\mathcal O^+\subset h^2\mathcal O^+$。
结合式 (10) 的整余项，得到

$$
S(L_0)\equiv h/24\pmod{h^2}.
\tag{20}
$$

这也覆盖 $p=5$：此时 $m=2$，常数项可能恰有二阶贡献，
但仍不改变这里的一阶位移。本文没有据此丢弃将来二阶计算中的常数 $p$ 项。

### Step 7. 简单根唯一提升与位移

在剩余类 $L_0$，首项导数为

$$
\overline S'(L_0)=-mL_0^{m-1}=-4m=2\in\mathbb F_p^\times.
\tag{21}
$$

因此 $L_0$ 是剩余多项式的简单根。$\mathcal O^+$ 是完成离散赋值环，
$S\in\mathcal O^+[L]$，所以简单根版 Hensel 引理给出唯一
$L_*\equiv L_0\pmod h$ 满足 $S(L_*)=0$。
这里所用的存在唯一性正是
[Milne，Algebraic Number Theory，命题 7.31](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=122)
的完成离散赋值环情形。

对任意 $a\in\mathbb Z_p$，多项式 Taylor 展开结合式 (20)、(21) 给出

$$
S(L_0+ah)\equiv h\left(\frac1{24}+2a\right)\pmod{h^2}.
$$

取 $a=-1/48$，便有 $S(L_0-h/48)\in h^2\mathcal O^+$。
同一剩余类中的差商

$$
\frac{S(L_*)-S(L_0-h/48)}{L_*-(L_0-h/48)}
$$

按多项式差商解释，其模 $h$ 等于式 (21) 的单位 $2$。
因此 $L_*-(L_0-h/48)\in h^2\mathcal O^+$，得到式 (1)。证毕。$\square$

## 唯一既有有限检验：五分母精确 sanity

只复用[第一曲率作者稿 V2，式 (13)](PAPER30_TWIST_PRIME_POST_CANCELLATION_PROBE_V2_20260907.md)
已有的 $p=5$ 精确首项式，不增加素数列表或根搜索。该式给出

$$
S(L)=-\frac1{384}\bigl((1344h-1536)L^2+(528h-560)L+48h-59\bigr),
\qquad h^2-5h+5=0.
$$

其确切值为

$$
S(1/4)=\frac{295}{384}-\frac{11}{16}h,
\qquad -\frac{11}{16}\equiv\frac1{24}\pmod5.
$$

直接代入本文候选根后，尚未利用 $h$ 的最小多项式就有

$$
S\left(\frac14-\frac h{48}\right)
=\frac{295}{384}-\frac{875}{1152}h+\frac{77}{1152}h^2-\frac7{4608}h^3.
$$

前两个系数的分子均被 $5$ 整除，且 $5\in h^2\mathcal O^+$，
所以整个表达式属于 $h^2\mathcal O^+$，与一般证明一致。
这只是既有有限例的精确一致性检查，不充当无限族证明。

## Corrections or Missing Assumptions

无须额外科学假设。必须明确修正的潜在推理方式是：
不能声称 Chebyshev 形式变形在特征零任意 $H$ 上反射对称，
也不能以这种错误对称性把终端首项除 $p$ 当作全局 off-$H$ 整表达式。
本文用式 (9) 的有限整 action 提升替代该推理；
实际点身份和模 $p$ 的驻值各自在合法范围内使用。

## Open Risks and Delivery Boundary

- 数学结论限于式 (1)。它为后续 $Q$ 计算提供实际根的一阶位移，
  不决定更高阶组合是否取消；若分析至 $h^2$ 或更高阶，必须重新保留相应常数 $p$ 项。
- 与已接受第一曲率式组合时，应代入 $L_*(h)$，不得将它冻结成 $1/4$。
- 作者已检查符号、单位分母、两个不同的约化环、$p=5$ 边界及 off-$H$ 非反射问题；
  独立核查仍须由非作者另行完成，本件不自记为审查通过。
- 仅新建本证明文件；旧稿、冻结产物、状态入口与脚本均未改动。
- 不产生全根实性、合数分母简单性、全部固定消失点恢复或正式 Route 候选结论。
