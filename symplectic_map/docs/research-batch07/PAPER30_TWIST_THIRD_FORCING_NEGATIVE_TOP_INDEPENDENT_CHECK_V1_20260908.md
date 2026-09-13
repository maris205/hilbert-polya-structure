# Proof Package：第三 forcing 负端最高参数系数独立检查 V1

日期：2026-09-08。检查者：`negative_top_review`，不是被审稿作者。
本件完整读取并遵循 `proof-writer`；仅写此独立报告，不修改作者稿、接受状态、批次入口或出版锁。

## Claim

审查对象为
[负端最高系数作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_COEFFICIENT_PROBE_V1_20260907.md)
的式 (1)—(2)。沿用实际第三 forcing 与实际分支，令

$$
p\ge5\text{ 为素数},\quad a\ge2,\quad m=(p-1)/2,\quad
M=p^{a-1}m,\quad D=p+m=3m+1,\quad e_*=M-D.
$$

要证的是

$$
p[L^D]\mathcal B_3\in h\mathcal O^+,
\qquad
v_h([L^D]S)\ge e_*+1,
\qquad
v_h([L^p]U_{\rm cl})\ge e_*+1,
\tag{C}
$$

其中 $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，
$P_{\rm cl}$ 首一且次数为 $m$。不审查下一非零层、完整 Newton 图或根斜率。

## Status

**数学主张 (C)：PASS；`PROVABLE AS STATED`。原主张无需削弱或增加科学假设。**

**作者稿 V1 按字面无修正逐行通过：FAIL。** Step 2 的约化范围写得过大，
而 Step 4 中“高度至多为 $-2m$”的赋值方向错误。必须作下文列出的局部修订。
本报告给出不使用非法约化的完整独立证明，故这些问题不构成主张 (C) 的反例。

关键答案是：奇共振后的 $A_m,\ldots,A_{p-1}$ 不能当作
$1/[2(1-u)]$ 的系数；但是本证明只在次数不超过 $p+m-1$ 的乘积中使用它们。
在此范围，与其相乘的偶指数系数必处于整的低带。因此这些乘积乘 $p$ 后确实消失。
若把范围推进到 $p+m$，同一理由即不再成立。

## Assumptions

1. 使用实际圆分域 $K^+=\mathbb Q_p(h)$，$\mathcal O^+$ 为其整数环，
   $v_h(h)=1$、$v_h(p)=M$，剩余域为 $\mathbb F_p$。
2. 使用实际 Chebyshev 传播子和实际有限递推：

   $$
   d_n(h)=\frac{\zeta^n+\zeta^{-n}-2}{h},\qquad
   d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}-L[x^{n-2}]e^{2V(b)}.
   $$

   当 $p\nmid n$ 时 $d_n$ 是单位，$\bar d_n=-n^2$；
   $v_h(d_p)=v_h(d_{2p})=2m$。这里只使用 $n<3p<p^a$，不存在真正的零传播子。
3. 第三 forcing 按作者稿定义，实际分支为 $b=1$。
4. 转回首一商时调用已接受的 $D=\deg S$ 与首一分解。
   已接受高系数桥 $p^2[L^j]\mathcal B_3\in h^M\mathcal O^+$、$j>m$ 可沿用；
   本报告也直接证明所需的单个最高系数乘 $p$ 后整。

不把“共振后 $A$ 可约化为有理低层”作为假设。所需粗界在本报告中从实际递推推导，
不把作者稿笼统引用的“阶乘桥低精度后果”当成未经检查的证据。

### Inputs and exact scope

| 文件 | 本次读取、使用范围 | SHA256 |
| --- | --- | --- |
| [负端最高系数 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_COEFFICIENT_PROBE_V1_20260907.md) | 全文 250 行；全部新主张与证明 | `9a32bb855d524c2ab00d2f84cf54026537f093c6d4f003c50087b950473d863d` |
| [一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | 实际递推、forcing、传播子规范、已接受输入和式 (17)；不重开既有首层证明 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| [根簇分离 V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | Claim、假设、分离引理及 Steps 6—7 的高系数桥与首一商 | `da834676ba00aa72e292acee6281b1a4ee4cd4dc8ebfab964a7fd28b503b7f2f` |
| [首层内部结构 V1](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | Claim、Step 1 的实际传播子高度、Step 5 的实际 $V_p$ 首层 | `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616` |

以上哈希仅绑定直接相关文件。没有运行素数扫描、根拟合、旧不变 39 项测试、PDF 构建或外部上传。
本件为纯数学局部核验，`route_applicability: NOT_APPLICABLE`；这不是 Route A/B 或论文产物验收。

## Notation

为避免把系数 $A_0$ 与整段低层函数混同，统一记

$$
V|_{b=0}=W(Lx^2),\qquad
\left.\partial_bV\right|_{b=0}=xA(Lx^2),\qquad u=Lx^2/4,
$$
$$
\widehat W(u)=W(4u)=\sum_{r\ge1}w_ru^r,
\qquad \widehat A(u)=A(4u)=\sum_{r\ge0}a_ru^r.
$$

所有级数只取递推实际存在的有限次数。
令 $e_{c,r}=[u^r]e^{c\widehat W}$，其中 $c=1,2$。
上横线只施于已证明为整的量。
后文有理生成函数恒等式表示所注明次数以内的系数身份，不把有限多项式与无限有理级数等同。

## Proof Strategy

先隔开三个真正不同的范围：$a_{<m}$ 的可约化低层、
$a_m,\ldots,a_{p-1}$ 的负赋值中间层，以及 $a_{\ge p}$ 的正规化 $p$-带。
用有限次数的指数多项式证明单个 $p$ 分母的公式，再按卷积指标分类处理奇次响应。
整个过程不对负赋值的 $a_r$ 取模 $h$。

## Dependency Map

1. 加权齐次性与实际递推给出 $w_r,a_r$ 的精确方程及最高系数提取。
2. 低于各自第一个共振的单位三角递推给出 $w_{<p}$、$a_{<m}$ 的有理剩余。
3. 实际 $d_p,d_{2p}$ 的高度给出 $w_p$、$a_m,\ldots,a_{p-1}$ 的粗界。
4. 单 $p$ 分母引理及三角归纳给出 $p w_{p+j}$ 整性与 $\tau$。
5. 卷积指标分区给出中间奇共振项乘 $p$ 后消失，以及 $p a_{p+j}$ 整性与 $\sigma$。
6. 最高系数提取与两个有限系数计算给出 (C) 第一式。
7. 正规化和首一性给出 (C) 其余两式。

## Proof

### Step 1. 精确递推和加权最高项

给 $b,L$ 分别赋权 $1,2$。对 $V_n$ 作三角归纳可知其中每个单项式
$b^kL^j$ 满足 $k+2j=n$，且 $k,j\ge0$。
令 $b=0$ 后只剩偶次项；对 $b$ 在零处求导后只剩 $xA(Lx^2)$。
逐项代入实际递推得到

$$
d_{2r}w_r=-4e_{2,r-1},\qquad
d_{2r+1}a_r=-\tfrac12e_{1,r}-8[u^{r-1}]e^{2\widehat W}\widehat A.
\tag{R}
$$

第一 forcing 项的目标次数 $3p-1=2D$ 对应 $b$ 次数零。
第二项去掉显含的 $L$ 后，所需 $L^{D-1}$ 的加权余量恰为一，
必须取 $e^{2V}$ 的 $b$-线性部分；准确地，

$$
\left.\partial_be^{2V}\right|_{b=0}=2xe^{2W}A.
$$

因此

$$
[L^D]\mathcal B_3
=-4^{-D}\bigl(e_{1,p+m}+16[u^{p+m-1}]e^{2\widehat W}\widehat A\bigr).
\tag{T}
$$

作者稿式 (5)、(6)、(14) 的常数因子均正确。其第 195 行写的是
$\partial_be^V$，应改写为本处真正用到的 $\partial_be^{2V}$，但式 (14) 没有少因子二。

### Step 2. 正确的低层范围与中间共振粗界

对 $1\le r<p$，偶传播子 $d_{2r}$ 均为单位。
若此前的 $w_i$ 整，则 $e_{2,r-1}$ 只含指数阶乘 $k!$、$k\le r-1<p$，故整。
归纳得到 $w_r\in\mathcal O^+$。约化 (R)，比较

$$
W_{\rm low}(u)=-\log(1-u),\qquad
r^2[u^r]W_{\rm low}=[u^{r-1}](1-u)^{-2}=r,
$$

可由单位三角唯一性得到

$$
\bar w_r=1/r\quad(1\le r<p).
\tag{L1}
$$

对 $0\le r<m$，奇传播子 $d_{2r+1}$ 均为单位，指数系数所需次数小于 $p$。
同一整性归纳及 (R) 给出

$$
a_r\in\mathcal O^+,\qquad \bar a_r=1/2\quad(0\le r<m).
\tag{L2}
$$

确切核算为：若 $A_{\rm low}=1/[2(1-u)]$，则其方程右侧取负号后的第 $r$ 项为

$$
\tfrac12+4\binom{r+1}{2}
=\frac{(2r+1)^2}{2},
$$

等于约化左侧。因此 (L2) 在单位范围内由唯一性成立。
**本证明从不将 (L2) 延伸到 $r\ge m$。**

在 $r=p$ 的偶递推中，$e_{2,p-1}$ 仍整，而 $v_h(d_{2p})=2m$，所以

$$
v_h(w_p)\ge-2m,\qquad p w_p\in h\mathcal O^+.
\tag{B1}
$$

在 $r=m$ 的奇递推中，右侧仅用整的 $e_{1,m}$、$e_{2,k}$ 和 $a_s$、$s<m$，
所以 $v_h(a_m)\ge-2m$。对 $m<r<p$，$d_{2r+1}$ 为单位，
$e_{1,r}$ 与所有所用的 $e_{2,k}$、$k\le r-1<p$ 都整。
由 (R) 对 $r$ 归纳得到

$$
v_h(a_r)\ge-2m\quad(m\le r<p).
\tag{B2}
$$

于是 $p a_r\in h\mathcal O^+$，因为 $M-2m\ge3m>0$。
这是实际递推上的下界，不是把共振置零，也不是声称这些 $a_r$ 本身整。

### Step 3. 为什么原稿 Step 2 的宽泛写法确实不成立

此处只是定位原文错误，不是下面证明的额外前提。
已接受首层内部结构给出

$$
\overline{h^mV_p}(L)=\frac{(-1)^m}{2}(2-L^m).
$$

加权齐次性使 $[L^m]V_p(b)=b[L^m]V_p(1)$，故
$a_m=4^m[L^m]V_p(1)$。令 $\chi=(-1)^{m+1}$，则

$$
\overline{h^ma_m}=4^m\chi/2\ne0,
\qquad v_h(a_m)=-m.
\tag{N1}
$$

再看 (R) 中 $r=m+1$ 的方程。
$e_{1,m+1}$ 整，$[u^m]e^{2\widehat W}\widehat A$ 除常数项乘 $a_m$ 外均整，
而 $\bar d_{p+2}=-4$。乘 $h^m$ 后约化得

$$
\overline{h^ma_{m+1}}=2\overline{h^ma_m}\ne0.
\tag{N2}
$$

这里 $m+1<p$ 且 $2(m+1)+1=p+2\ne p$。
所以即使排除 $r=m$，仍存在原稿第 105 行所列范围内的系数 $a_{m+1}$ 不整。
不能在该范围内以 $\widehat A_0=1/[2(1-u)]$ 解释真实约化。
原稿“在后续所需的低次数内”若仅指 $r<m$，方向可成立，但必须明确写出这个范围。

### Step 4. 单个 $p$ 分母引理与偶次正规化带

令 $Q(u)=\sum_{1\le r<p}w_ru^r$，$T_0(u)=\sum_{1\le r<p}u^r/r$。
由 (L1)，$Q-T_0\in h\mathcal O^+[u]$。
当 $N<2p$ 时，$p[u^N]e^{cQ}$ 是 $w_1,\ldots,w_{p-1}$ 的
$\mathbb Z_{(p)}$ 系数多项式：指数展开中只出现 $k!$、$k\le N<2p$，
每个阶乘至多含一个因子 $p$。因此该量整，且其约化只依赖 $\bar Q$。

在次数小于 $2p$ 的范围内，

$$
-\log(1-u)=T_0(u)+u^p/p+R(u),
$$

其中 $R$ 从次数 $p+1$ 开始，且所需系数均 $p$-整。
展开 $e^{cT_0}=(1-u)^{-c}\exp(-cu^p/p-cR)$ 时，
所有两个尾项相乘的次数至少 $2p$。因为 $(1-u)^{-c}$ 整，得到

$$
\overline{p[u^{p+j}]e^{cQ}}
=-c[u^j](1-u)^{-c}\quad(0\le j\le m).
\tag{E0}
$$

若 $p w_{p},\ldots,p w_{p+j}$ 已整，令
$\tau_i=\overline{p w_{p+i}}$。由于两个高带 $w_{\ge p}$ 的乘积从次数 $2p$ 才开始，
在目标次数内指数对高带严格线性；(E0) 给出

$$
\overline{p e_{c,p+j}}
=[u^j]\frac{c(\tau(u)-1)}{(1-u)^c},
\qquad \tau(u)=\sum_{i=0}^{m}\tau_i u^i.
\tag{E}
$$

这里所需的 $e^{cQ}$ 低系数次数不超过 $m<p$，均整，
故没有把两个分别不整的量直接约化相乘。

正规化整性不是先验假设：由 (B1) 从 $j=0$ 起步，
对 $1\le j\le m$，方程 (R) 的 $w_{p+j}$ 右侧只用已经正规化整的高带。
将该方程乘 $p$，使用上面的有限线性展开和单位 $d_{2p+2j}$，
逐项证明 $p w_{p+j}\in\mathcal O^+$，随后才定义其剩余。
约化给出

$$
\tau_0=0,\qquad
j^2\tau_j=[u^{j-1}]\frac{2(\tau-1)}{(1-u)^2}\quad(1\le j\le m).
$$

因 $j<p$，递推唯一。将 $\tau=-2u/(1-u)$ 代入，右侧等于
$-2[u^{j-1}](1+u)/(1-u)^3=-2j^2$，故

$$
\tau(u)\equiv-\frac{2u}{1-u}\pmod{u^{m+1}}.
\tag{PW}
$$

因此在所需范围内

$$
E_1(u):=\sum_{j=0}^{m}\overline{p e_{1,p+j}}u^j
\equiv-\frac{1+u}{(1-u)^2}\pmod{u^{m+1}},
$$
$$
E_2(u):=\sum_{j=0}^{m}\overline{p e_{2,p+j}}u^j
\equiv-\frac{2(1+u)}{(1-u)^3}\pmod{u^{m+1}}.
\tag{PE}
$$

### Step 5. 含负赋值中间项的乘积为什么可丢弃

固定目标卷积次数 $N=p+j$、$0\le j\le m-1$，写

$$
[u^N]e^{2\widehat W}\widehat A=\sum_{s=0}^{N}e_{2,N-s}a_s.
$$

将项按 $s$ 分类：

| 响应下标 $s$ | 偶指数下标 $k=N-s$ | 乘 $p$ 后的合法处理 |
| --- | --- | --- |
| $0\le s<m$ | 可在低带或 $p$-带 | $a_s$ 整；若 $k<p$，全项乘 $p$ 后的剩余为零；若 $k\ge p$，用 (PE) 和 (L2) |
| $m\le s<p$ | $k\le p+j-m\le p-1$ | $e_{2,k}$ 整，故 $v_h(p e_{2,k}a_s)\ge M-2m>0$ |
| $p\le s\le N$ | $0\le k\le j<m$ | $e_{2,k}$ 整；只需先证明 $p a_s$ 整后再约化 |

这给出了原稿 Step 4 第 157—160 行所需的具体次数及赋值证明。
中间层并非因为自身乘 $p$ 消失就能在任意乘积里删除；这里合法的原因是
**其配对因子仍整**。中间层与新的偶 $p$-带的最低相遇次数是 $m+p$，
不在本表范围中。

现在对 $a_{p+j}$、$0\le j<m$ 作三角归纳。
方程 (R) 乘 $p$ 后，第一个右侧项由 (PE) 整；卷积次数是 $p+j-1$，
应用上述分类时，第三类只包含已经处理的 $a_p,\ldots,a_{p+j-1}$。
第 $j=0$ 步的卷积次数为 $p-1$，所有项为低层或中间层，乘 $p$ 后的剩余为零。
因为 $d_{2p+2j+1}$ 是单位，由归纳得到

$$
p a_{p+j}\in\mathcal O^+\quad(0\le j<m).
$$

定义 $\sigma_j=\overline{p a_{p+j}}$ 和
$\sigma(u)=\sum_{j=0}^{m-1}\sigma_ju^j$。
前述分区现在也严格证明全部所需卷积身份

$$
\overline{p[u^{p+j}]e^{2\widehat W}\widehat A}
=[u^j]\left(\frac{\sigma(u)}{(1-u)^2}
+E_2(u)\frac1{2(1-u)}\right),\quad 0\le j<m.
\tag{PA}
$$

此处 $1/[2(1-u)]$ 仅提供下标 $s\le j<m$ 的系数，
没有使用 $a_m$ 或任何共振后的虚假剩余。

约化 (R) 得

$$
(2j+1)^2\sigma_j=\tfrac12[u^j]E_1
+8[u^{j-1}]\left(\frac{\sigma}{(1-u)^2}+
E_2\frac1{2(1-u)}\right),\quad 0\le j<m,
\tag{SA}
$$

其中 $j=0$ 的第二项为零。所有 $2j+1<p$，所以递推唯一。
候选 $\sigma=-(1+u)/(2(1-u)^2)$ 的第 $j$ 项为 $-(2j+1)/2$。
代入后括号内等于 $-3(1+u)/(2(1-u)^4)$，其第 $j-1$ 项为
$-j(j+1)(2j+1)/4$。于是右侧等于

$$
-\frac{2j+1}{2}-2j(j+1)(2j+1)=-\frac{(2j+1)^3}{2},
$$

与左侧相同，包括 $j=0$。故

$$
\sigma(u)\equiv-\frac{1+u}{2(1-u)^2}\pmod{u^m}.
\tag{PS}
$$

### Step 6. 目标最高系数消失与首一商高度

由 (T)、(PE)、(PA) 可知目标最高系数乘 $p$ 后整，而且

$$
4^D\overline{p[L^D]\mathcal B_3}
=-[u^m]E_1
-16[u^{m-1}]\left(\frac{\sigma}{(1-u)^2}
+E_2\frac1{2(1-u)}\right).
$$

第一项为 $2m+1=p$。括号内的第 $m-1$ 项为

$$
-\frac32\left\{\binom{m+2}{3}+\binom{m+1}{3}\right\}
=-\frac{m(m+1)(2m+1)}4
=-\frac{m(m+1)p}{4}.
$$

因 $p\ge5$，所用分母均为单位；两个贡献分别在剩余域中为零。
这并不依赖两项之间的额外抵消。因此
$p[L^D]\mathcal B_3\in h\mathcal O^+$。

由 $v_h(p)=M$，

$$
v_h([L^D]S)=v_h(p[L^D]\mathcal B_3)+M-D\ge e_*+1.
$$

已接受分解中 $P_{\rm cl}$ 首一，且次数为 $m$、$U_{\rm cl}$ 次数为 $p$，
所以 $[L^D]S=[L^p]U_{\rm cl}$。这证明 (C) 全部结论。$\square$

## Corrections or Missing Assumptions

以下为作者稿 V1 的最小局部修复，不需要改变定理：

1. **第 103—115 行，Step 2：必须改范围。**
   明写 $\bar w_r=1/r$ 仅用于 $1\le r<p$，
   $\bar a_r=1/2$ 仅用于 $0\le r<m$。
   不能把“$r<p$ 且 $2r+1\ne p$”作为整段 $A$ 的合法约化范围；
   上面的 (N2) 给出实际反证，而非纯措辞偏好。
2. **第 157 行，Step 4：必须改赋值方向。**
   “高度至多为 $-2m$”应改为“赋值至少为 $-2m$”，
   即 $v_h(a_s)\ge-2m$。在解释中加入本报告 Step 2 的三角粗界。
3. **第 124—139、154—179 行：补全约化存在性与乘积界。**
   先通过单位三角归纳证明 $p w_{p+j}$、$p a_{p+j}$ 整，再对其取剩余。
   Step 4 至少写出
   $s\ge m$、$N\le p+m-1\Rightarrow N-s\le p-1$，
   并说明 $v_h(p e_{2,N-s}a_s)\ge M-2m>0$。
   这足以排除被重点质疑的 singular 中间项，不需另开实验。
4. **第 125—135 行，Step 3：澄清单分母的两层含义。**
   低块指数的阶乘分母在次数 $<2p$ 仅含一个 $p$；
   已经不整的实际高带也在该次数范围内只线性出现。
   本报告 Step 4 证明此说法对实际递推成立，而不只是形式对数模型中的直觉。
5. **第 144、184、195 行：记号局部修正。**
   $\tau,\sigma$ 的有理表达分别注明模 $u^{m+1}$、模 $u^m$；
   Step 5 的导数改成 $\partial_be^{2V}|_{b=0}=2xe^{2W}A$。
   这些修正不改变已核对正确的式 (14) 常数 $16$。

因此应保留数学主张，修订证明的截断范围和整性说明；
不应因 Step 2 的文字错误直接宣布最高系数消失被反驳，
也不应将未修订的 Step 2 作为“共振后整体可约化”的一般引理继续使用。

## Open Risks

- 本报告的 PASS 只覆盖 (C) 和上述有限递推推导。
  不把 $e_*+1$ 认定为准确高度，不判断其他高参数系数的最小非零层。
- 在卷积次数达到 $p+m$ 时，$e_{2,p}a_m$ 首次可能出现。
  $p e_{2,p}$ 的剩余为 $E_2(0)=-2\ne0$，而 $v_h(a_m)=-m$；
  这个单项乘 $p$ 后赋值为 $-m$，不整，更不能单独删去。
  因而这里的截断边界具有实质内容，不能向更高次无证明外推。
- 已接受首一分解、高参数桥和实际次数仅作为指定依赖使用；
  本报告没有重开它们的既有审查，也不创造新的接受登记。
- 原稿保留原样。本件提供主张的独立证书及原文最小修订清单，
  不等同于已经完成作者稿修订或出版交付。
