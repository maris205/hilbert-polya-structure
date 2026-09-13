# Paper30：素数幂后极点模态块与第二内部 forcing 联合独审

日期：2026-09-07。核查者：late_nonnenmacher_source。
本轮完整读取并使用 proof-writer；本票仅审查本轮两份新作者稿。

## Claim

固定任意奇素数 $p$、$a\ge2$、$s=p^a$ 及任意本原 $s$ 次根 $\zeta$。
保持原物理正 kick、固定参数和 SUM action，令

$$
h=D_1,\quad \rho=-h,\quad L=\rho\lambda,\quad
m=(p-1)/2,\quad M=p^{a-1}m,
$$
$$
d_n=-D_n/h=D_n/\rho,\qquad V_n(L)=\rho^n v_n(L/\rho).
$$

本票联合核查实际 $p+1\le n\le2p$ 模态块及第二内部 forcing，
包括如下准确结论：

1. 对 $1\le j<p$，$pV_{p+j}\in\mathcal O^+[L]$，其剩余生成函数为

   $$\sum_{j=1}^{p-1}\overline{pV_{p+j}}x^j
   =\frac{xA'}{2A}\pmod{x^p},
   \qquad A=1-x/2+(1-4L)x^2/16.$$

2. 该剩余多项式的参数次数、最高系数以及系数意义下准确 $p$ 尺度均如作者所述；
   参数代入后的准确赋值只在规定的非零剩余条件下断言。
3. 对由同一实际分支至 $2p-1$ 定义的

   $$\mathcal B_2=-[x^{2p-1}]e^V-2L[x^{2p-2}]e^{2V},$$

   有

   $$h^{-2m}p\mathcal B_2\in\mathcal O^+[L],
   \qquad \overline{h^{-2m}p\mathcal B_2}=2,$$
   $$pV_{2p}\in\mathcal O^+[L],
   \qquad \overline{pV_{2p}}=-1/4.$$

4. 所有局部代数整数参数均有
   $v_h(\mathcal B_2)=2m-M$、$v_h(V_{2p})=-M$，
   包括旧的 $\bar L^m=2$ 代数剩余类；
   已接受第一内部 forcing $\mathcal B_1$ 与 $\mathcal B_2$ 互素。

这里 $2p<s$，没有任何本轮模态被设为零；
$\mathcal B_2$ 不是周期 $2p$ 系统的首项。

## Status

**PROVABLE AS STATED。下列 25 项限定核查全部 PASS。**

未发现阻断性数学缺口，不要求修改两份冻结作者稿。
没有缩小其全部奇素数、全部 $a\ge2$、全部允许 $\zeta$ 的量词范围。
结论不涉及完整 $C_{p^a}$ 的根分类、平方自由性或完整 $C,Q$ 互素。

## Exact inputs and independence

已全文读取并实际核对以下两份新输入：

| 输入 | 行数 | SHA256 |
| --- | --- | --- |
| [POST_POLE_BLOCK V1](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md) | 391 | 0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34 |
| [SECOND_INTERNAL_FORCING V1](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md) | 640 | 278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15 |

还按要求完整重读了 430 行已接受
[第一内部局部结构输入](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)，
其 SHA256 为：

    f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616

核查者是该旧首层输入的原作者；它在本票仅作为已经接受的规范和结论使用，
不重新授予“非作者独审”。核查者未参与本轮两份新稿的模态块、端点缺陷或
第二层取消推导，本票也不将主控与两位作者的协作同式当作独立证据。

## Assumptions and notation

$\mathcal O^+$ 是 $K^+=\mathbb Q_p(h)$ 的完成整数环，
$v_h(h)=1$、$v_h(p)=M>2m$，剩余域为 $\mathbb F_p$。
只按已接受范围使用

$$
V_i\in\mathcal O^+[L]\ (i<p),\qquad
h^mV_p\in\mathcal O^+[L],\qquad
\overline{h^mV_p}=\frac{(-1)^m}{2}(2-L^m),
$$
$$
d_p/h^{2m}\equiv-1\pmod h,\qquad
\sum_{i=1}^{p-1}i^2u_i u_{p-i}=\frac{2-L^m}{2},
$$

其中 $u_i$ 是平方传播子 $U=-\log A$ 的低于 $p$ 次系数。
本票不重审这些旧结论。

$H$ 为独立形式变量，
$\mathscr R=\mathbb Z_{(p)}[L][[H]]$；
低块为 $P(H,x)=\sum_{i=1}^{p-1}P_i(H,L)x^i$，且 $P_i(h,L)=V_i(L)$。
记 $\mathcal N=x\partial_x$、$\chi=(-1)^{m+1}$。
实际高块系数记为 $Y_j=pV_{p+j}$，形式比较模型记为 $\mathscr Y_j$。
多项式赋值均指系数赋值的最小值；参数代入的赋值另作说明。

## Proof strategy and dependency map

先独立核查新块的完整阶乘桥与三角整性，才允许使用它们进入端点证明。
端点按如下链条审查：

1. 实际块与形式单位三角模型的准确误差；
2. 实际 Chebyshev 移位缺陷及整段配对缺陷；
3. Jacobi 修正回到实际系数；
4. 非驻值有限 action 的精确 Euler 身份及所有误差高度；
5. 两个同阶贡献的完整参数多项式相消；
6. 第二传播子除法、参数单位值及两个内部 forcing 的互素推论。

形式 $H$ 同余、实际 $h$ 同余和特征 $p$ 参数多项式身份不混用。
不以有限样本、普通剩余首层或有理辅助式单独代替这条实际链。

## Independent proof audit

### 1. 低块形式环及精确第一系数：PASS

对 $1\le n<p$，$d_n(H)$ 的常数项 $-n^2$ 是 $p$ 单位，
所以原三角递推给出 $P_n\in\mathscr R$。
由于 $d_1(H)=-1$ 精确，$P_1=1/2$ 与 $H,L$ 无关。
所有使用的 $x$ 次数有限，参数 $L$ 的次数有统一有限界，
因此 $H=h$ 的代入可逐参数系数收敛，不会产生未控制的负赋值。

### 2. 小于 $2p$ 的完整阶乘带：PASS

$N<2p$ 时 $[x^N]e^{\alpha P}$ 只用 $k!\ (k\le N)$。
对每个奇素数都有 $2p-1<p^2$，故至多出现一个 $p$。
所以乘 $p$ 后所有这些系数整；$N<p$ 时原系数已经整。
对 $k=p+r$、$0\le r<p$，

$$
\frac p{(p+r)!}\equiv-\frac1{r!}\pmod p.
$$

这是实际清分母后的同余，不能对原非整指数系数先取剩余。
第 $p$ 到第 $2p-1$ 个指数项均被此式覆盖。

### 3. 形式 $H$ 桥的误差确为 $pR$：PASS

在 $\mathscr R/p\mathscr R$ 中，
$P(H,x)^p\equiv x^p/2\pmod{x^{2p}}$，
因为其余 $P_i^p x^{pi}$ 从 $x^{2p}$ 才开始。
与第 2 项合并，对 $\alpha=1,2$、$0\le j<p$ 得

$$
p[x^{p+j}]e^{\alpha P(H,x)}
+\frac\alpha2[x^j]e^{\alpha P(H,x)}
\in p\mathscr R.
$$

因此作者 (10a) 的误差确为 $pR_{\alpha,j}(H,L)$，
而非仅在 $H=0$ 成立或另有未控制的 $H$ 误差。
这里只使用整数 $\alpha^p=\alpha$ 于剩余域；
没有使用错误的参数多项式身份 $L^p=L$。

### 4. 高模式线性展开与真实 $pV_p$：PASS

若 $R_{\rm high}$ 从 $x^p$ 开始，
则 $R_{\rm high}^2$ 从 $x^{2p}$ 开始，
所以在特征零中精确有

$$
e^{\alpha(P+R_{\rm high})}
=e^{\alpha P}(1+\alpha R_{\rm high})\pmod{x^{2p}}.
$$

这不依赖高模式系数是否整，因而没有把其极点当作“小量”忽略。
实际 $V_p$ 包含在 $R_{\rm high}$ 内，且
$Y_0=pV_p\in h^{M-m}\mathcal O^+[L]$。
其普通剩余为零是赋值结论，不是投影或共振规范。

### 5. 后极点块的逐阶整性：PASS

乘 $p$ 后，高模式线性项只含
$pV_n$ 乘 $[x^{N-n}]e^{\alpha P}$；
其中 $N-n<p$，后因子已经整。
从第 4 项的真实 $Y_0$ 出发，
$d_{p+j}\equiv-j^2\ne0$ 对 $1\le j<p$ 给出每一步的单位除法。
因此 $pV_{p+1},\ldots,pV_{2p-1}$ 全部逐系数整。
该证明没有对下一内部指标 $2p$ 偷用单位传播子。

### 6. 完整指数剩余与有限 Jacobi 方程：PASS

低块阶乘项给出 $-\alpha x^pA^{-\alpha}/2$，
高块线性项给出 $\alpha x^pA^{-\alpha}Z$，
其中 $Z=\sum_{j=0}^{p-1}\bar Y_jx^j$、$Z(0)=0$。
因此新块稿 (13) 的两式及其因子二正确。
再由实际递推的负号与 $d_{p+j}\equiv-j^2$ 相消，得到

$$
\mathcal N^2Z=
\left(\frac{x}{2A}+\frac{2Lx^2}{A^2}\right)(Z-1/2)\pmod{x^p}.
$$

右端无常数驱动算子，每个 $j^2$ 对 $1\le j<p$ 可逆，
所以零常数项的有限解唯一。

### 7. 有理首层的完整参数身份：PASS

核查者独立计算
$U=-\log A$ 的平方传播子式和
$\mathcal N^3U=J_0(1+\mathcal NU)$，
其中 $J_0=x/(2A)+2Lx^2/A^2$。
于是
$Z=-\mathcal NU/2=xA'/(2A)$ 满足第 6 项；
自由 $x,L$ 的通分残差严格为零。
该有理式 $A(0)=1$，系数只含 $2$ 的分母，
所以包括 $p=3$ 在内都可取所需剩余。
它不扩张 $j=p$ 处的有限唯一性范围。

### 8. 剩余多项式的次数与最高系数：PASS

对 $A=(1-r_1x)(1-r_2x)$，
对称幂和 $T_j=r_1^j+r_2^j$ 无需除以 $r_1-r_2$，
故 $L=0$ 和 $q=0$ 的退化参数也被覆盖。
从有限对数系数可独立得到作者的 $T_j$ 展开。
最高 $q$ 次项在 $j=2k$ 时为 $2(-1)^k$，
在 $j=2k+1$ 时为 $(2k+1)(-1)^k/2$。
乘以 $-1/2$ 并代入 $q=(1-4L)/16$ 后，准确得到

$$
[L^k]\bar Y_{2k}=-4^{-k},\qquad
[L^k]\bar Y_{2k+1}=-(2k+1)4^{-k-1}.
$$

$j<p$ 使奇数公式中的 $j$ 非零，最高次确不丢失。

### 9. 系数准确尺度与参数准确尺度：PASS

第 5、8 项说明每个 $pV_{p+j}$ 系数整且至少一个系数为单位，
所以原 $V_{p+j}$ 的系数最小赋值恰为 $-M$。
这并不证明每个参数点都取得该赋值。
作者只在 $T_j(\bar L)\ne0$ 时作点值断言；
$j=1$ 的剩余为常数 $-1/4$，才对所有局部代数整数参数都准确。
作者也仅把 $\lfloor j/2\rfloor$ 称为剩余次数，
没有误称实际多项式不能有更高次数。

### 10. 实际块与形式单位模型的误差：PASS

用第 3 项的形式桥和精确高块线性式重新代入，
得到端点稿 (15)：

$$
d_{p+j}(h)Y_j+[x^j]J(h,x)Y
=\tfrac12[x^j]J(h,x)+p\varepsilon_j(h,L).
$$

最低阶的负下标按零处理，剩下的低指数整数项可收入
$p\varepsilon_j$，故不破坏该式。
形式模型使用同一 $d_{p+j}(H)$ 与 $J(H,x)$，只是取模型常数项为零；
其所有三角除数仍为 $p$ 单位。
逐阶相减，初始误差为 $Y_0$ 的 $h^{M-m}$，
额外驱动为 $h^M$，从而
$Y_j-\mathscr Y_j(h)\in h^{M-m}\mathcal O^+[L]$。
这清楚地区分模型初值与真实模态，没有改变后者。

### 11. 移位及反射缺陷的精确公式：PASS

置 $z=1+\eta$、$T=z^p$、$H=2-z-z^{-1}$。
直接从 Chebyshev 定义相减，独立得到

$$
H\Delta_j=(T-1)(z^j-T^{-1}z^{-j}),\qquad
H\delta_i=(T^2-1)(T^{-2}z^i-z^{-i}).
$$

在特征 $p$ 中 $T=1+\eta^p$；
分子首项分别为 $2j\eta^{p+1}$、$4i\eta^{p+1}$。
除以 $H\sim-\eta^2$ 并与 $H^m\sim(-1)^m\eta^{p-1}$ 比较，
得到 $\Delta_j\sim2\chi jH^m$、$\delta_i\sim4\chi iH^m$，符号正确。
$H$ 级数嵌入 $\eta$ 级数环是单射，
而各缺陷原本为 $H$ 多项式，所以下一项不会出现半整数次 $H$。

### 12. 整段配对缺陷及第二首层：PASS

核查者以自由 $T,u$ 直接构造 $i$ 与 $p-i$ 的两项，
其中 $u=z^i$，核得精确因式分解

$$
H(\delta_i+\delta_{p-i})
=-\frac{(T-1)^2(T+1)}{T^2}(u+T/u).
$$

其首项为 $-4\eta^{2p}$；
再除以 $H$ 后为 $4\eta^{2p-2}=4H^{2m}$ 的首项。
所以配对和是 $4H^{2m}+O(H^{2m+1})$，
不只是 $H^m$ 的单个系数相消。
将形式模 $p$ 式代入 $H=h$，
所有额外 $p$ 倍项高度至少 $M>2m$，故所需实际同余成立。

### 13. 未移位模型与 Jacobi 修正方程：PASS

对实际低块方程作 $\mathcal N$ 微分，
因为对角算子与 $\mathcal N$ 交换，
得到
$(\mathcal D_H+J)\mathcal NP=-J$。
因此未移位有限解准确为 $\mathscr Y^{(0)}=-\mathcal NP/2$。
从移位方程相减，其驱动是
$-(\mathcal D_H^{\rm sh}-\mathcal D_H)\mathscr Y^{(0)}$。
取第 11 项的 $H^m$ 层，负号及两个因子二合成

$$
(-\mathcal N^2+J_0)Y^{(1)}=\chi\mathcal N^2U.
$$

这对 $1\le j<p$ 仍是单位三角方程，零常数项解唯一。

### 14. 参数导数给出的修正：PASS

对自由 $b,L,x$ 的
$U(b,L,x)=-\log(1-bx/2+(b^2-4L)x^2/16)$，
核查者独立验证
$\mathcal NU=bU_b+2LU_L$ 和平方传播子式。
在 $b=1$ 处，对驱动的两个参数导数分别给出
$-x/(2A)$ 与 $-x^2/A^2$。
所以

$$
Y^{(1)}=-\chi(U_b+LU_L)|_{b=1}
=-\chi(\mathcal NU-LU_L)
$$

正好解第 13 项；通分符号残差为零。
此参数导数只是系数身份，未改变实际固定参数要求；
只需低于 $p$ 的系数，所以没有越过 $p!$ 取特征 $p$ 指数。

### 15. 修正回到实际块的误差阶：PASS

形式同余可写为
$\mathscr Y-\mathscr Y^{(0)}
=H^m\widetilde Y^{(1)}+H^{m+1}R+pT$，
其中各有限系数整。
代入 $H=h$ 并加入第 10 项的真实／形式误差，
由于 $M-m>m$ 且各高度为整数，得到

$$Y_j=-\frac j2V_j+h^m\widetilde Y^{(1)}_j+O(h^{m+1}).$$

取任意剩余系数的整提升只改变所列余项。
这里保留的是实际 $V_j$，不是把平方传播子低首层替换成完整实际低块。

### 16. 非驻值有限 action 的精确 Euler 身份：PASS

取 $[x^{2p}]$ 的有限泛函并先把 $V_i$ 视为独立变量。
其梯度在真实分支上为
$(d_i-d_{2p-i})V_{2p-i}/2$，一般不为零。
按 $V_i,b,L$ 的权重 $i,1,2$ 作 Euler 恒等式，
参数项合为 $-\mathcal B_2/2$，
所以准确得到

$$
\mathcal B_2=-4p\Phi+
\sum_{i=1}^{2p-1}i(d_i-d_{2p-i})V_iV_{2p-i}.
$$

该推导不要求周期 $2p$ 的反射对称性，
也没有把真实分支当作这个人工截断泛函的临界点。

### 17. $p^2\Phi$ 的赋值控制含中央项：PASS

动能非中央配对至多为一个整低模乘一个赋值至少 $-M$ 的高模，
传播子整，故下界为 $-M$。
中央 $V_p^2$ 单独保留；即使不利用 $d_p$ 的正赋值，
其保守下界 $-2m$ 也严格大于 $-M$。
两项势能分别只需指数 $2p-1$、$2p-2$ 的系数，
乘 $p$ 后整，由此同样有下界 $-M$。
所以 $\Phi$ 的系数赋值至少 $-M$，
$p^2\Phi$ 至少为 $M>2m$。
没有将取 $2p$ 阶动能中真实存在的 $V_p^2$ 因指数线性展开而漏掉。

### 18. 端点配对及最小边界 $p=3,a=2$：PASS

将第 16 项乘 $p$ 后按 $i$ 与 $2p-i$ 配对，
准确系数为 $2i-2p$；中央缺陷精确为零。
$-2p$ 部分至少含 $p\delta_i$，高度为 $M+m$。
结合第 17 项，端点同余为

$$
p\mathcal B_2\equiv
\sum_{i=1}^{p-1}2i\delta_iV_iY_{p-i}
\pmod{h^{2m+1}\mathcal O^+[L]}.
$$

第 10 项误差在这个实际公式中再乘 $\delta_i\in h^m\mathcal O^+$，
故总高度至少 $(M-m)+m=M>2m$。
特别在 $p=3,a=2$，$M=3,m=1$：
原 $Y_0$ 的高度是 $2$，并不能直接忽略；
进入端点后才提高至 $3$，严格越过目标层 $2$。
这一步实际处理了边界，不是只写“初值为高阶”。

### 19. 未修正块的贡献及全部较低层取消：PASS

代入 $Y_{p-i}=-(p-i)V_{p-i}/2+\cdots$，
零阶贡献是
$-\sum_i i(p-i)\delta_iV_iV_{p-i}$。
将 $-i(p-i)$ 换为 $i^2$ 丢掉的项含 $p\delta_i$，
高度至少 $M+m$。
再用 $i\leftrightarrow p-i$，平方权重的差同样被 $p$ 整除，
所以可用 $\frac12(\delta_i+\delta_{p-i})$ 配对。
第 12 项因此给出完整贡献

$$2h^{2m}\sum_i i^2u_i u_{p-i}
=h^{2m}(2-L^m).$$

这同时消去所有低于 $2m$ 的层，而不是从普通剩余为零猜测下一阶。

### 20. $h^m$ 修正的第二个同阶贡献：PASS

第 11、14 项给出修正的归一化贡献

$$
-8\sum_{i=1}^{p-1}i^2u_i
\bigl((p-i)u_{p-i}-L\partial_Lu_{p-i}\bigr).
$$

三次权重和在配对下变号，故为零；
二次权重的对称性使
$\mathcal A'(L)=2\sum_i i^2u_i\partial_Lu_{p-i}$。
于是余下的贡献是

$$4L\mathcal A'(L)=-2mL^m=L^m\quad\text{于 }\mathbb F_p[L].$$

这里使用的是已接受的完整多项式身份
$\mathcal A=(2-L^m)/2$ 及其形式导数；
不假设 $L$ 为剩余基域中的点，不除以 $2-L^m$。

### 21. 误差汇总与准确常数 $2$：PASS

主要余项的实际下界如下：

| 来源 | 进入端点后的高度下界 |
| --- | --- |
| $p^2\Phi$ | $M$ |
| 配对系数中的 $-2p$ | $M+m$ |
| 实际／形式模型差 | $(M-m)+m=M$ |
| 模型 $h^m$ 修正后的余项 | $m+(m+1)=2m+1$ |
| 用模 $p$ 配对替换整数权重 | $M+m$ |
| 配对缺陷的下一阶 | $2m+1$ |
| 在 $h^{2m}$ 层把低模换为其剩余 | $2m+1$ |

全部严格高于 $2m$，包括最小边界。
第 19、20 项合成为
$p\mathcal B_2\equiv h^{2m}((2-L^m)+L^m)=2h^{2m}$。
因奇剩余特征中 $2\ne0$，整性、准确最小系数赋值 $q_2=2m$
和常数剩余同时成立，不是仅有一个非尖锐下界。

### 22. 真实第二传播子除法：PASS

由实际倍频恒等式可直接算得
$d_{2p}=d_p(4+hd_p)$，其符号也经自由符号检查。
所以已接受的 $d_p/h^{2m}\equiv-1$ 给出
$d_{2p}/h^{2m}\equiv-4$。
此归一化传播子是与 $L$ 无关的单位，
因此

$$
pV_{2p}=
\frac{h^{-2m}p\mathcal B_2}{2h^{-2m}d_{2p}}
$$

为整多项式，剩余准确为 $2/(-8)=-1/4$。
不能把这里的负传播子换成 $D_n/h$。

### 23. 所有局部代数整数参数及旧消失类：PASS

第 21、22 项的约化都是非零常数。
在任意相应有限局部扩张中代入整数 $L$，仍得到单位；
所以点值赋值分别精确为 $2m-M$、$-M$。
这覆盖 $\bar L^m=2$ 的全部代数剩余根类，
而不仅是 $\mathbb F_p$ 的参数点，也包含 $p=3$ 的边界类。
此处和第 9 项的“有条件点值尖锐性”是不同结论，作者没有混写。

### 24. 两个内部 forcing 互素及原变量：PASS

先对已接受的 $h^{-m}\mathcal B_1$ 使用其单位最高系数，
首一化后所有代数根均为局部整数。
第 23 项使 $\mathcal B_2$ 在每个这样的根上非零，
所以 $\gcd_{K^+[L]}(\mathcal B_1,\mathcal B_2)=1$。
这里使用单位最高系数的是归一化后的第一 forcing，
并不声称未除去 $h^m$ 的原多项式最高系数为单位。

两者回到原 $\lambda$ 分别乘非零常数
$\rho^{kp-1}$ 并作同一可逆线性变量替换 $L=\rho\lambda$，
互素性保持。这只是同一个 $p^a$ 系统的两个内部 forcing，
没有比较来自不同周期构造的首项。

### 25. 全量词、内部层边界与科学范围：PASS

所有实际身份来自任意本原 $\zeta$ 的 Chebyshev 表达式；
没有对 $p$、$a$、$r$ 或参数做样本外推。
对全部奇 $p$、$a\ge2$ 都有
$2p<s$、$2p-1<p^2$、$M>2m$，
每个本轮除法的单位条件和误差高度均满足。
精确高模式线性展开只用于严格小于 $2p$ 的指数系数，
没有被延伸到会出现 $R_{\rm high}^2$ 的下一层。
完整 $C_{p^a}$、$Q_{p^a}$、全实根或完整内部塔均未被本票宣告解决。

## Exact verification actually run

核查者独立启动了两组自由符号运算，只检查本轮新身份，
没有输入素数、$r$、参数点或数值根列表。

第一组对自由 $x,L$ 核对平方 forcing、有理 $Z=-\mathcal NU/2$
和后极点 Jacobi 方程，残差均为零，且一次系数为 $-1/4$。
实际输出：

    REVIEWER_RATIONAL_IDENTITY_PASS: square forcing, Y=-NU/2, post-pole Jacobi equation
    Y_first_coefficient -1/4

第二组从自由 $T,u,H$ 的传播子表达式直接构造移位、反射、配对和倍频，
并以自由 $b,L,x,\chi$ 核对参数导数和 Jacobi 修正。
另外独立核对
$(p-i)^2-i^2=p(p-2i)$ 与
$i^3+(p-i)^3=p(p^2-3pi+3i^2)$，
作为配对取模的精确整除身份。
实际输出：

    REVIEWER_ENDPOINT_GENERIC_IDENTITIES_PASS
    Jacobi_correction_residual 0
    shift_reflection_pair_and_double_mode_residuals 0 0 0 0
    quadratic_and_cubic_pairing_divisibility_residuals 0 0
    no prime, r, parameter-point, or root samples

这些计算不承担一般整性或误差高度的证明；
其余部分由上述逐项论证核查，不由作者 stdout 或运行成功替代。

## Corrections or missing assumptions

没有阻断性缺口，没有作者修改要求。
两份稿中的以下限制和次序必须保留：

- 先清去阶乘的唯一 $p$ 分母，再在形式 $H$ 环中取模；
- 真实 $pV_p$ 初值只在明确误差估计中进入，不能置零；
- 第二端点先使用非驻值 Euler 身份，再利用缺陷提高真实／形式误差高度；
- 配对缺陷必须控制到整个 $2m$ 层，不能只核第一个 $m$ 层取消；
- 先得到整系数常数约化，再断言全部整数参数的非消失。

旧首层输入只按既有接受范围调用，没有重开其作者或独审状态。

## Open risks and delivery boundary

- 本票仅接受新非内部块及第二内部 forcing 的限定无限族结论。
- 后续指数达到或越过 $2p$ 的新高模乘积、更多阶乘层及完整内部塔尚未证明。
- 两个内部 forcing 互素不等于完整 $C_{p^a},Q_{p^a}$ 互素。
- 只新增本联合报告；两份作者稿、旧接受稿、入口、脚本及冻结记录均未修改。
- 未运行素数／根扫描、旧分母复跑、论文立项、正文/PDF 构建、Route 评价或对外操作。

