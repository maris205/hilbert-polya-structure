# Paper 30：两倍奇素数临界根簇的低半权重与唯一阶乘极点桥

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
本轮完整读取并使用 `proof-writer` 技能。本件是新辅助证明，不是独审票。

## Claim

固定奇素数 $p\ge5$、$\gcd(r,2p)=1$，沿用同一物理正 kick、固定参数和
SUM action。令

$$
m=(p-1)/2,\qquad h=D_2,\qquad \kappa=\lambda-1/16,
\qquad S(\kappa)=h^{p-1}C_{r,2p}(1/16+\kappa)/p.
$$

这里 $h$ 是完成实圆分整数环 $\mathcal O^+$ 的素元，$v_h(p)=m$。
已接受的 $S\in\mathcal O^+[\kappa]$ 和其普通剩余多项式不在本件重审。
本件证明更细的两个事实。

**低半权重。** 取形式平方根 $\delta^2=h$，令 $t=\delta x$、$w=x^2$，写

$$
P(\delta x)=A(w)+\delta x B(w),\qquad
A=\sum_{j=1}^{m}h^jv_{2j}w^j,
\qquad B=\sum_{j=0}^{m-1}h^jv_{2j+1}w^j.
\tag{1}
$$

将真实传播子在独立形式变量 $H=0$ 处展开，再令 $H=h$。
$A,B$ 的每个非零形式单项 $H^a\kappa^bw^j$ 均满足 $2a+b\ge j$。
其中最低权重部分是

$$
\boxed{
A^{[0]}=-\frac12\log\bigl((1+\kappa w)^2+\gamma Hw^2\bigr)
\pmod{w^{m+1}},\qquad \gamma=\frac5{3072}.}
\tag{2}
$$

上标 $[0]$ 指权重 $2a+b-j=0$，不是只取 $H=0$。

**实际首项的初始权重。** 对 $\mathcal O^+[\kappa]$ 定义

$$
\operatorname{wt}(h)=2,\qquad \operatorname{wt}(\kappa)=1,
\qquad \operatorname{wt}(a\kappa^b)=2v_h(a)+b.
$$

设 $H,K$ 为相应关联分次环中的 $h,\kappa$ 初始符号。
$S$ 没有权重小于 $m$ 的项，权重恰为 $m$ 的部分是

$$
\boxed{
\operatorname{in}_m S
=\frac14\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\binom m{2j}\binom{2j}j
\left(\frac5{12288}\right)^jH^jK^{m-2j}.}
\tag{3}
$$

所有式 (3) 系数都在 $\mathbb F_p$ 中解释。特别地，若 $s_b=[\kappa^b]S$，则

$$
\boxed{
v_h(s_b)\ge\max\left\{0,\left\lceil\frac{m-b}{2}\right\rceil\right\},
\qquad 0\le b\le p.}
\tag{4}
$$

对 $b=m-2j$，式 (3) 还给出 $h^{-j}s_b$ 的准确剩余值。
特别地，这不是预设 $\kappa\asymp h$ 得到的估计；权重来自实际递推。
$p=5$ 时式 (1)—(4) 仍成立，但式 (3) 退化为 $K^2/4$，不能据此宣称
非零 $H$ 端点或一般素数的全部 Newton 结论。

## Status

上述低半权重、唯一 $p!$ 层桥和式 (2)—(4)：`PROVABLE AS STATED`。
本件不单独声明根簇全部简单、全部根的准确赋值或更高 $Q$ 非消失。
从本桥推导实际 Newton 分解由另件处理，避免把同一计算重复记为两项贡献。

## Assumptions and Notation

真实递推和严格低于半阶的 $P$ 为

$$
D_n=2-\zeta^n-\zeta^{-n},\quad \zeta=e^{2\pi ir/(2p)},\qquad
v_n=-\frac{[t^{n-1}]e^v/2+\lambda[t^{n-2}]e^{2v}}{D_n},
\qquad P=\sum_{n<p}v_nt^n.
\tag{5}
$$

本件只使用 $n<p$ 的分支，没有在内部共振或 $D_{2p}=0$ 处作除法。
输入是已接受的
[偶数半阶与两倍素数稿](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)，
SHA256：`2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a`。
该稿给出真实半阶消元、$h$ 的局部规范和 $S$ 的普通剩余多项式。

本文的 $B$ 是式 (1) 除去一个 $x$ 后的多项式；与先前将整段奇部称为
$B_{\rm odd}(x)$ 的记法相比，$B_{\rm odd}(x)=xB(x^2)$。
引入 $\delta$ 只为整数次幂记账；下文所有系数式仅含 $h$，不依赖平方根选择。

## Proof Strategy and Dependency Map

1. 将实际奇偶传播子写成 $\mathbb Z_{(p)}[[H]]$ 上的单位三角算子。
2. 以 $2a+b-j$ 过滤同时归纳偶分支、奇分支及奇分支消去余项。
3. 提取最低权重的偶方程，以显式二次式解它。
4. 把已接受的精确半阶 action 写为有限的奇、偶和中央三部分。
5. 在特征零先核每个阶乘的 $p$ 极点，识别唯一达到权重 $m$ 的项。
6. 对已整的该项使用 Frobenius，得到式 (3)，再读取逐系数界。

四次局部 jet 同时由主控独立推导，见已全文读取的
[四次 jet 与有限多项式辅助稿](PAPER30_TWIST_DEGENERATE_FLIP_QUARTIC_JET_LEMMA_V1_20260907.md)，
SHA256：`58a65cc7ca2f646f3e40c7d558ca731df887991e0b3ef3bbc596a5b8712dcf97`。
本件保留所需的短计算以使全低半权重证明自足，但不将该重叠 jet 另算贡献。
本件不调用外部命名定理；所用三角递推、二项式展开及 Frobenius 恒等式
均在下文直接使用并说明其适用阶数。

## Proof

### Step 1. 形式真实传播子与三角整性

令 $\xi=-\zeta$，则 $\xi$ 为本原 $p$ 次根且
$h=2-\xi^2-\xi^{-2}$。在 $\xi+\xi^{-1}$ 剩余为 $2$ 的分支上，

$$
\xi+\xi^{-1}=\sqrt{4-h}.
$$

把 $h$ 换成独立形式变量 $H$，偶传播子为整数 Chebyshev 多项式，奇传播子
则为 $\sqrt{4-H}$ 的整数多项式。因此它们都属于 $\mathbb Z_{(p)}[[H]]$。
这里平方根系数仅有 $2$ 的分母，可由其二项式展开直接验证。
准确的首阶是

$$
\frac{D_{2j}(H)}H=j^2+O(H),\qquad
D_{2j+1}(H)=4+O(H).
\tag{6}
$$

在所需范围 $1\le j\le m$，$j^2$ 为 $p$-单位；奇常数 $4$ 也为单位。
故缩放后的每个三角方程都在 $\mathbb Z_{(p)}[[H]][\kappa]$ 上唯一可解。
所需低分支的指数次数小于 $p$，使用的阶乘全为 $p$-单位。
得到的形式解在 $H=h$ 处收敛并等于式 (1) 的实际解。

记 $M=w\partial_w$，定义对角算子

$$
L_e(w^j)=\frac{D_{2j}(H)}H w^j,\qquad
L_o(w^j)=D_{2j+1}(H)w^j.
$$

于是 $L_e=M^2+H\mathcal R_e$、$L_o=4+H\mathcal R_o$；
$\mathcal R_e,\mathcal R_o$ 是系数整且不改变 $w$ 次数的对角算子。
只需它们在有限次空间上的定义，不要求一条无限阶导数展开。

设 $E=e^A$、$z^2=Hw$。真实递推 (5) 的奇偶部分精确写成

$$
L_oB=-\frac E2\cosh(zB)-\lambda zE^2\sinh(2zB)
\pmod{w^m},
\tag{7}
$$
$$
L_eA=-\frac w2E\frac{\sinh(zB)}z
-\lambda wE^2\cosh(2zB)
\pmod{w^{m+1}}.
\tag{8}
$$

式 (7)—(8) 中每个双曲函数组合都是 $z^2=Hw$ 的幂级数，因此没有引入
额外平方根分母。

### Step 2. 全低半部的权重闭合

定义 $\mathcal F_\ell$ 为支撑满足 $2a+b-j\ge\ell$ 的形式级数
$\sum c_{abj}H^a\kappa^bw^j$，其中 $a,b,j\ge0$，
$c_{abj}\in\mathbb Z_{(p)}$。有限 $w$ 截断下，乘法满足
$\mathcal F_i\mathcal F_j\subset\mathcal F_{i+j}$。
乘 $H,\kappa,w$ 分别改变过滤阶 $2,1,-1$。

需要同时证明

$$
A,B,E\in\mathcal F_0,\qquad R:=B+E/8\in\mathcal F_1.
\tag{9}
$$

式 (7) 减去常数项后是

$$
4R=-(L_o-4)B-\frac E2\bigl(\cosh(zB)-1\bigr)
-\lambda zE^2\sinh(2zB).
\tag{10}
$$

若已求系数满足 $A,B\in\mathcal F_0$，其指数 $E$ 也满足该界。
第一项因 $L_o-4$ 含 $H$，属于 $\mathcal F_2$；
后两项每一非零项含 $H^kw^k$、$k\ge1$，属于 $\mathcal F_1$。
这里 $\lambda=1/16+\kappa\in\mathcal F_0$。
因而式 (10) 给出相应已求范围内的 $R\in\mathcal F_1$。

再把 $B=-E/8+R$ 代入式 (8)。双曲函数的零次驱动合并为

$$
-\frac w2 EB-\lambda wE^2
=-\kappa wE^2-\frac w2ER.
\tag{11}
$$

这两项属于 $\mathcal F_0$。余下双曲函数项都含
$H^kw^{k+1}$、$k\ge1$，其过滤阶为 $k-1\ge0$。
除以式 (6) 的单位传播子不降低过滤阶，故新求的 $A$ 系数满足界。

该论证确实是三角归纳：从 $A_0=0$ 开始，先由奇方程求 $B_0$；
在第 $j$ 步，先用已知 $A_{j-1}$ 求 $B_{j-1}$ 及相同阶的 $R$，
然后偶方程才求 $A_j$。右端只用此前系数。
如此直到 $j=m$，得到式 (9)，没有假设尚未求得的高模式整性。

### Step 3. 最低权重偶解

以下等式取各自恰当的初始过滤阶。式 (10) 的第一项至少提高两级，
所以不影响 $R^{[1]}$。后两项只需取 $Hw$ 的一次项、
$B^{[0]}=-E^{[0]}/8$ 和 $\lambda_0=1/16$。
因此

$$
R^{[1]}=-\frac{Hw}{16}E^{[0]}(B^{[0]})^2
-\frac{\lambda_0Hw}{2}(E^{[0]})^2B^{[0]}
=\frac{3Hw}{1024}(E^{[0]})^3.
\tag{12}
$$

式 (8) 中恰为过滤阶零的项于是给出

$$
M^2A^{[0]}=-\kappa w e^{2A^{[0]}}
-\frac5{1536}Hw^2e^{4A^{[0]}}
\pmod{w^{m+1}}.
\tag{13}
$$

具体地，四次系数由三项相加：
$-3/2048+1/6144-1/512=-5/1536$。
传播子修正至少提高两级，不能在本层制造额外导数项。

设 $\beta=5/1536$、$\gamma=\beta/2$，直接微分验证

$$
A_*=-\frac12\log\bigl(1+2\kappa w+(\kappa^2+\gamma H)w^2\bigr)
$$

满足式 (13) 的未截断有理身份及 $A_*(0)=0$。
每一阶 $w^j$ 的未知量系数为 $j^2$，对 $1\le j\le m<p$ 可逆，
所以三角唯一性给出 $A^{[0]}=A_*$ 的所需截断，即式 (2)。
$p\ge5$ 保证 $\beta,\gamma$ 的分母为 $p$-单位；
$p=5$ 的分子消失并不破坏形式恒等式。

### Step 4. 半阶 action 的有限权重核算

现在令 $H=h$，使用实际 $A,B$，并仍记 $E=e^A$。
已接受的半阶 action 给出 $C=-4pG$ 及

$$
h^pG=\frac\delta2[x^{2p-1}]e^{A+\delta xB}
+\frac{\lambda h}2[x^{2p-2}]e^{2A+2\delta xB}
-\frac{\widehat T^2}{8},
$$
$$
\widehat T=\frac\delta2[x^{p-1}]e^{A+\delta xB}
+\lambda h[x^{p-2}]e^{2A+2\delta xB}.
$$

故 $S=-4h^pG/h$ 精确等于下列三个有限项：

$$
S_{\rm odd}=-2\sum_{\ell=1}^{p}
\frac{h^{\ell-1}}{(2\ell-1)!}
[w^{p-\ell}]EB^{2\ell-1},
\tag{14}
$$
$$
S_{\rm even}=-2\lambda\sum_{\ell=0}^{p-1}
\frac{4^\ell h^\ell}{(2\ell)!}
[w^{p-1-\ell}]E^2B^{2\ell},
\qquad S_{\rm central}=\frac12U^2,
\tag{15}
$$
$$
U:=\frac{\widehat T}\delta
=\frac12\sum_{\ell=0}^{m}\frac{h^\ell}{(2\ell)!}
[w^{m-\ell}]EB^{2\ell}
+\lambda\sum_{\ell=0}^{m-1}
\frac{2^{2\ell+1}h^{\ell+1}}{(2\ell+1)!}
[w^{m-\ell-1}]E^2B^{2\ell+1}.
\tag{16}
$$

所有 $E,E^2$ 都由有限 $A$ 定义，没有用式 (2) 的无限尾替换高系数。
所需最高 $w$ 次数为 $p-1$，而 $A$ 没有常数项，所以这些指数本身只用
小于 $p$ 的阶乘，系数仍整，且 $[w^d]E^aB^k$ 的权重至少为 $d$。

式 (14)—(16) 的显式阶乘则必须另外核算。
因为 $0\le k<2p$，$v_p(k!)$ 等于 $0$ 或 $1$；
除以一个 $p$ 将实际 $h$ 权重降低 $2m$。
得到如下准确的下界：

| 项 | 范围 | 权重下界 |
| --- | --- | --- |
| $S_{\rm odd}$ | $1\le\ell\le m$，无 $p$ 极点 | $p+\ell-2\ge2m$ |
| $S_{\rm odd}$ | $m+1\le\ell\le p$，一个 $p$ 极点 | $\ell-1\ge m$ |
| $S_{\rm even}$ | $0\le\ell\le m$，无 $p$ 极点 | $p-1+\ell\ge2m$ |
| $S_{\rm even}$ | $m+1\le\ell\le p-1$，一个 $p$ 极点 | $\ell\ge m+1$ |
| $U$ 第一和 | $0\le\ell\le m$ | $m+\ell\ge m$ |
| $U$ 第二和 | $0\le\ell\le m-1$ | $m+\ell+1\ge m+1$ |

因此中央平方的权重至少为 $2m$。含 $p$ 极点的每一项仍整：
奇和中的 $h^{\ell-1}$ 至少含 $h^m$，偶和中的 $h^\ell$ 至少含 $h^{m+1}$。
这也说明当前权重计算未在非整组合上提前取剩余值。

唯一能达到权重 $m$ 的项是式 (14) 的 $\ell=m+1$，即奇指数的 $k=p$ 层：

$$
S_{[m]}=-2\frac{h^m}{p!}[w^m]EB^p
\quad\text{加上权重大于 }m\text{ 的项}.
\tag{17}
$$

### Step 5. 实单位、Frobenius 与初始多项式

为核式 (17) 的单位，令 $\pi=\xi-1$。
已接受的实际尺度满足 $h/\pi^2\equiv-4\pmod\pi$。
由 $p=\prod_{j=1}^{p-1}(1-\xi^j)$ 和 Wilson 恒等式得到

$$
\frac p{\pi^{p-1}}\equiv-1,\qquad
\overline{\frac{h^m}{p!}}=(-1)^m.
\tag{18}
$$

后一个剩余值属于实剩余域 $\mathcal O^+/(h)=\mathbb F_p$。
没有把大环 $\mathcal O/(h)$ 当作域。

由于 $m<p$，形式 Frobenius 身份说明 $B(w)^p$ 在 $w^1,\ldots,w^m$ 的
系数全被 $p$ 整除。这样的项在本计算至少多出 $2m$ 权重。
常数项 $B_0=-1/(2D_1(h))$ 满足 $B_0=-1/8+O(h)$，
所以它的非恒定 $h$ 修正也至少提高两级。
因此式 (17) 的初始部分是

$$
\operatorname{in}_mS
=\frac{(-1)^m}{4}[w^m]
\bigl((1+Kw)^2+\gamma Hw^2\bigr)^{-1/2}.
\tag{19}
$$

式 (19) 的系数只依赖 $A$ 到 $w^m$ 阶，故这时使用式 (2) 合法。
它不同于在 Step 4 的高指数系数中直接补入无限低支尾项。

最后展开

$$
\bigl((1+Kw)^2+\gamma Hw^2\bigr)^{-1/2}
=\sum_{j\ge0}\binom{-1/2}{j}
(\gamma H)^jw^{2j}(1+Kw)^{-1-2j}.
$$

取 $w^m$ 系数，使用
$\binom{-1/2}{j}=(-1)^j\binom{2j}j/4^j$，
得到式 (3)。其 $K^m$ 系数为 $1/4$，所以初始部分不为零。
不存在权重低于 $m$ 的项等价于逐系数界 (4)，证明完成。$\square$

## Verification Actually Run

本轮运行两条一般纯符号身份核验，不代入素数或数值根：

- 对一般 $\kappa,H,\beta$，令
  $A=-\frac12\log(1+2\kappa w+(\kappa^2+\beta H/2)w^2)$，
  计算 $M^2A+\kappa we^{2A}+\beta Hw^2e^{4A}$，残差严格为零。
- 对一般 $\lambda,Y$，用 $b_0=-Y/8$、
  $b_1=-Yb_0^2/16-\lambda Y^2b_0/2$ 计算偶方程四次项，
  精确得到 $-(96\lambda-1)Y^4/1536$，临界值为 $-5Y^4/1536$。

实际输出：`INDEPENDENT_EXACT_PASS weighted differential identity and critical quartic coefficient`。
有限 action 的逐项界由上面的通用估值证明承担；未新增素数列表、
根扫描、目标拟合或旧分母复跑。

## Corrections or Missing Assumptions

- $p\ge5$ 是本件统一有理四次式的明确范围；$p=3$ 的簇只有一根，
  本件未为它重复构造一条四次权重引理。
- $p=5$ 的 $\gamma$ 不是单位。式 (3) 的退化必须保留，不能据此强外推
  $p\ge7$ 的非退化根簇结论。
- 独立形式变量 $H$ 用于证明支撑；实际赋值界须在 $H=h$ 后解释。
  系数中额外的 $p$ 因子只会提高实际权重，不会降低式 (4) 的下界。

## Open Risks and Delivery Boundary

- 本件给出实际初始权重而不自行授予全部簇根简单性；可分性及 Hensel
  论证由对应新引理和 Newton 稿承担。
- 本件不确定初始多项式零剩余根的下一层准确赋值，也不完成 $p=5$ 的退化边。
- 本件只控制严格低于半阶的分支和该次半阶 action，不推断更高 $Q$ 层的整性。
- 只新写本文件；已接受稿、独审票、冻结锁和入口均未改。
