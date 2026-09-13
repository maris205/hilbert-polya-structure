# Paper30：正簇支撑与临界端点的同一有限算子

日期：2026-09-08。作者推导；使用 `formula-derivation` 与 `proof-writer`。
本件只新增有限恒等式替代证明，不修改冻结输入、原定理、候选评价或验收标准。
辅助代数核算属于作者工作，不计真正非作者独审。

## Claim / Target

取素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
对真实 Chebyshev 有限低块及完整四项三次移位响应，设

$$
\mathscr E=H\partial_H+L\partial_L,\qquad
W(H,L)=\sum_{i=1}^{p-1}\Omega_i(H)P_i(H,L)P_{p-i}(H,L).
$$

则在 $\mathbb F_p[[H,L]]/(H,L)^{m+1}$ 中有

$$
\boxed{\mathcal F_3=
\frac38\left\{\mathscr E^2+
\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}\right\}W
+\frac{3\chi}{16}H^m.}
\tag{U1}
$$

有理系数表示左乘；$\mathscr E$ 不越过它们。进一步，只调用已接受的
**严格预临界**矩输入

$$
W=\sum_{k=0}^{m-1}\beta_kH^k\pmod{(H,L)^m},
\qquad \beta_k=\frac{(k!)^2}{(2k+1)!},
\tag{U2}
$$

而不调用总阶 $m$ 的有理核、临界分子恢复或临界矩消失，便得到

$$
\boxed{\mathcal F_3=rac{3\chi}{32}H^m
\pmod{(H,L)^{m+1}}.}
\tag{U3}
$$

换言之，所有 $j>0$、$k+j\le m$ 的 $[H^kL^j]\mathcal F_3$ 及所有
$n<m$ 的 $[H^n]\mathcal F_3(H,0)$ 同时为零；纯临界系数为 $3\chi/32$。
这是原正簇支撑与常数结论的同对象替代证明，不改变完整第三 forcing
在 $p\ge5,a\ge2$ 下的原 $C1$–$C3$ 目标。

## Status

- 统一式 (U1)：`PROVABLE AS STATED`，下文给出完整有限证明。
- 由明确输入 (U2) 推出 (U3)：`PROVABLE AS STATED`；不把 (U2) 视为本件新证。
- 推导主线：`COHERENT AS STATED`。没有额外假设临界矩为零或有理。
- 新替代证明尚待针对实际变更的真正非作者检查；本件不自行登记为独立接受。

## Assumptions, Frozen Inputs, and Invariant Object

本件全文读取并有限调用以下原稿；不修改其历史状态文字。

| 输入 | 本件使用的准确内容 |
| --- | --- |
| [A12 临界投影](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | 真实 Chebyshev 定义、完整四项端点、精确响应的绑定；本件重证真实临界投影和有限和，不调用其单独的临界微分算子 |
| [A13 统一正簇](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | 实际有限低块、幅度齐次性和精确响应；式 (19) 中严格总阶小于 $m$ 的矩值，即 (U2) |

(U2) 的上游证明仍由
[A11 高阶响应结构](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md)
承担。本件未全文重开 A11，不宣称删去产生这些预临界矩值的有理性论证；
本件只把它们作为已接受且准确限定的输入使用。

不变量对象始终是同一个真实有限和 $W$，不是任意插值矩、无限第 $p$ 模态
或独立拼接的临界核。下文没有近似步骤：所有截断均为所指理想中的精确同余。

## Notation and Derivation Map

令 $i^*=p-i$、$I=i^2\in\mathbb F_p$，并定义

$$
C_0=2,\quad C_1=2-H,\quad C_{i+1}=(2-H)C_i-C_{i-1},
\qquad d_i=(C_i-2)/H,
$$
$$
\mathsf S_0=0,\quad\mathsf S_1=1,\quad
\mathsf S_{i+1}=(2-H)\mathsf S_i-\mathsf S_{i-1},
\qquad \Omega_i=i\mathsf S_i,
$$
$$
\Psi_i=\frac{i^2(2+Hd_i)}{2(H-4)},\qquad
\bar w_i=\frac{w_i+w_{i^*}}2,\qquad w_i^-=\frac{w_i-w_{i^*}}2.
\tag{1}
$$

$P_i=[x^i]P(H,1,L,x)$ 始终满足 $1\le i<p$。
设 $\mathcal N=x\partial_x$、$\delta=H\partial_H$、
$\mathcal T=b\partial_b+L\partial_L$、$\mathcal R=\mathcal T-\delta$，最后取 $b=1$。
对任一权重 $w_i(H)$，令

$$
f_i=P_iP_{i^*},\qquad \mathcal M[w]=\sum_{i=1}^{p-1}w_if_i.
$$

依赖链为：

1. 三角有限低块给出自身的 $p$ 整性及幅度齐次性；不使用有理延拓核。
2. 整数 Chebyshev 系数给出真实临界反射缺陷。
3. 平均权满足完整微分身份，使 A13 的权重导数消元在完整形式环中精确成立。
4. 未平均缺陷在目标总阶只产生 $3\chi H^m/16$，从而得到 (U1)。
5. (U2) 与总阶 $m$ 的零特征消去全部未知临界矩；低层递推与先消 $p$ 的有限和给出 (U3)。

## Proof

### Step 1. 有限低块自身整性及响应的齐次性

在 $\mathbb Z_{(p)}[b,L][[H]][x]/(x^p)$ 中，取 $P(0)=0$ 并解

$$
\mathcal D_HP=-\frac{bx}{2}e^P-Lx^2e^{2P},\qquad
\mathcal D_Hx^i=d_i(H)x^i.
\tag{2}
$$

这里 $P(0)=0$ 指 $x$ 常数项。第 $i$ 模态的右端只用先前模态，
且指数展开所需的阶乘指数至多 $i-1<p$。由于 $d_i(0)=-i^2$ 是
$\mathbb Z_{(p)}$ 的单位，第 $i$ 模态除以 $d_i(H)$ 合法。
逐个求解 $i=1,\ldots,p-1$ 便证明

$$
P_i\in\mathbb Z_{(p)}[b,L][[H]],\qquad 1\le i<p.
\tag{3}
$$

这已经保证本件所有临界有限矩能在 $\mathbb F_p[[H,L]]$ 中取值。
它不声称对应的无限有理表达式或单独第 $p$ 模态为 $p$ 整。

按式 (2) 的三角递推，每个 $P_i$ 的 $b,L$ 单项式具有形状
$b^{i-2j}L^j$，$0\le2j\le i$。因此

$$
\mathcal TP=(\mathcal N-L\partial_L)P,\qquad
\mathcal RP=(\mathcal N-\mathscr E)P.
\tag{4}
$$

也可由 $P(H,b,L,x)=P(H,1,L/b^2,bx)$ 得到同一身份；这里不需要保留
$b^{-1}$，因为原系数为上述多项式。式 (4) 对反复响应仍成立。
两因子有限配对的总 $x$ 次数是 $i+i^*=p=0$，故合并的响应算子为
$-\mathscr E$。

沿用原完整端点及已证明的精确响应：

$$
t=-\frac12\mathcal RP,\qquad
q=\frac18\mathcal R^2P-\frac{\mathcal RP}{4(H-4)},
\tag{5}
$$
$$
\mathcal F_3=
\frac{3H}{8(H-4)}\sum_i i^2\Omega_if_i
-6\sum_i\Psi_iP_it_{i^*}
+6\sum_i\Omega_iP_iq_{i^*}
+3\sum_i\Omega_it_it_{i^*}.
\tag{6}
$$

式 (5) 仅用单位分母，在 $p=5$ 仍合法；本件不调用另外需要 $p\ge7$
的次首矩数值。$H-4$ 可逆，所有有限响应系数均为 $p$ 整。

### Step 2. 真实 Chebyshev 临界投影不可省略

递推的生成函数是

$$
\sum_{i\ge0}C_i z^i=\frac{2-(2-H)z}{(1-z)^2+Hz},\qquad
\sum_{i\ge0}\mathsf S_i z^i=\frac{z}{(1-z)^2+Hz}.
\tag{7}
$$

按 $H$ 展开分母，再提取 $z^i$，先在整数中得到

$$
[H^k]\mathsf S_i=(-1)^k\binom{i+k}{2k+1},
$$
$$
[H^k]d_i=
(-1)^{k+1}\left\{\binom{i+k+1}{2k+2}+\binom{i+k}{2k+2}\right\}
=\frac{(-1)^{k+1}i}{k+1}\binom{i+k}{2k+1}.
\tag{8}
$$

超过上指标的二项式取零。对 $k<m$，

$$
[H^k]\Omega_i=
\frac{(-1)^ki^2\prod_{s=1}^k(i^2-s^2)}{(2k+1)!},
\tag{9}
$$

分母为 $p$ 单位，故权重同层在 $i,i^*$ 上相等。
由 $\Omega_i=-d_i-Hd_i'$，$d_i$ 的同层也相等。

临界 $k=m$ 时，不能把式 (9) 中含 $p$ 的分母直接约化。
这时 $2m+1=p$，$m+1$ 是单位。若 $i\le m$，则
$\binom{i+m}{p}=0$；若 $i>m$，写 $i+m=p+s$，$0\le s<p$，
由 $(1+z)^{p+s}=(1+z^p)(1+z)^s$ 得
$\binom{i+m}{p}=1\pmod p$。所以式 (8) 给出

$$
[H^m]d_i=2\chi i\,\mathbf1_{i>m},\qquad
[H^m]\mathsf S_i=-\chi\,\mathbf1_{i>m}.
\tag{10}
$$

$i>m$ 与 $i^*>m$ 恰有一个成立，且 $i^*=-i$ 于 $\mathbb F_p$。
因此

$$
\boxed{\Omega_i^-=-\frac\chi2 iH^m+O(H^{m+1}),\qquad
d_i-d_{i^*}=2\chi iH^m+O(H^{m+1}).}
\tag{11}
$$

又因 $i^{*2}=i^2$ 且 $\Psi$ 中的 $d$ 额外乘以 $H$，

$$
\Psi_i^-=rac{i^2H(d_i-d_{i^*})}{4(H-4)}=O(H^{m+1}).
\tag{12}
$$

式 (11) 是真实多项式的非偶缺陷，不是预临界偶多项式的外推。

### Step 3. 平均权的微分身份在完整形式环中成立

Chebyshev 整数多项式满足

$$
H(4-H)C_i''+(2-H)C_i'+i^2C_i=0,\qquad C_i'=-i\mathsf S_i.
\tag{13}
$$

具体地，令 $Q=z\partial_z$ 并代入 $H=2-z-z^{-1}$，则
$(QH)^2=H(H-4)$、$Q^2H=H-2$，而
$Q^2(z^i+z^{-i})=i^2(z^i+z^{-i})$。链式法则立即给出第一式；
该代入对 $\mathbb Z[H]$ 单射，故结果是整数多项式身份。
对第二式，记 $D_z=(1-z)^2+Hz$，式 (7) 直接给出

$$
\partial_H\sum_{i\ge0}C_iz^i
=-\frac{z(1-z^2)}{D_z^2}
=-z\partial_z\sum_{i\ge0}\mathsf S_iz^i.
$$

提取 $z^i$ 即得 $C_i'=-i\mathsf S_i$。

将 $C_i=2+Hd_i$ 代入第一式，得

$$
\mathscr J_i:=H^2(4-H)d_i''+H(10-3H)d_i'
+\{2+(i^2-1)H\}d_i+2i^2=0.
\tag{14}
$$

现在先在完整环 $\mathbb F_p[[H,L]]$ 中取
$d=\bar d_i$、$w=\bar\Omega_i$、$v=\bar\Psi_i$。
由于 $i^{*2}=i^2=I$，两个式 (14) 有相同参数和常数项，其平均仍满足
$\mathscr J=0$，并且

$$
w=-d-Hd',\qquad v=\frac{I(2+Hd)}{2(H-4)}.
$$

令 $g=-(H-2)/(2(H-4))$。代入上述两个表达式并展开，准确有

$$
2(H-4)\left(v+\frac H2w'-gw\right)=\mathscr J=0.
$$

另一方面，对式 (13) 第一式求导，再用 $w=-\bar C_i'$，得到
$H(4-H)w''+(6-3H)w'+(I-1)w=0$。于是

$$
\boxed{v+\frac H2w'=gw,\qquad
Iw=w+H(H-4)w''+3(H-2)w'.}
\tag{15}
$$

这些是平均权的**精确**身份，不只模 $H^m$ 成立。
特别是未知临界平均权也包含在内。所有微分先在完整形式环进行，再取
总阶商；不能直接对一个未经控制的截断代表元求 $\partial_H^2$。
最终的 Euler 算子则保持 $(H,L)^{m+1}$，所以 (U1) 在该商中定义良好。

### Step 4. 完整偶端点的精确消元：列出全部权重导数项

把式 (6) 中的 $\Omega,\Psi$ 分别替换为平均权，定义
$\mathcal F_3^{\rm ev}$。因 $f_i=f_{i^*}$，
$W=\mathcal M[\Omega]=\mathcal M[\bar\Omega]$ 精确成立。
以下 $A,B,Y,X$ 全部使用平均权：

$$
A=\mathcal M[w'],\quad B=\mathcal M[w''],\quad
Y=\mathcal M[v],\quad X=\mathcal M[Iw].
$$

偶配对与式 (4) 给

$$
2\sum_iw_iP_i(\mathcal RP)_{i^*}
=-\mathscr E\mathcal M[w]+\mathcal M[\delta w],
$$
$$
\sum_iw_i\{P_i(\mathcal R^2P)_{i^*}
+(\mathcal RP)_i(\mathcal RP)_{i^*}\}
=\frac12\{\mathscr E^2\mathcal M[w]
-2\mathscr E\mathcal M[\delta w]+\mathcal M[\delta^2w]\}.
\tag{16}
$$

第一式来自 $\sum w_i\mathscr Ef_i=
\mathscr E\mathcal M[w]-\mathcal M[\delta w]$。
第二式的左边由反射平均等于 $\frac12\sum w_i\mathscr E^2f_i$，
再把两次乘积导数全部展开即得右边。求和始终是 $1\le i<p$，无第 $p$ 模态边界。

代入完整四项端点后，精确得到

$$
\begin{aligned}
\mathcal F_3^{\rm ev}={}&\frac{3H}{8(H-4)}X
+\frac32\{-\mathscr EY+\mathcal M[\delta v]\}\\
&+\frac38\{\mathscr E^2W-2\mathscr E(HA)+HA+H^2B\}
-\frac3{4(H-4)}\{-\mathscr EW+HA\}.
\end{aligned}
\tag{17}
$$

式 (15) 给出

$$
Y=gW-\frac H2A,\qquad
\mathcal M[\delta v]=Hg'W+H(g-1/2)A-\frac{H^2}2B,
$$
$$
X=W+H(H-4)B+3(H-2)A.
\tag{18}
$$

这里 $\mathscr E(gW)=g\mathscr EW+Hg'W$。
所以式 (17) 中 $-\mathscr EY$ 和 $\mathcal M[\delta v]$ 的
$Hg'W$ 项准确相消；$\mathscr E(HA)$ 的两项也准确相消。
暂时扣除第一项 $3HX/[8(H-4)]$，余下表达式是

$$
\frac38\left\{\mathscr E^2W+
\frac{2(H-1)}{H-4}\mathscr EW
-\frac{3H(H-2)}{H-4}A-H^2B\right\}.
\tag{19}
$$

最后把式 (18) 的 $X$ 代回：它贡献
$3/8$ 乘以 $HW/(H-4)+3H(H-2)A/(H-4)+H^2B$。
因此 $A,B$ 两项分别相消，得到完整形式环中的精确身份

$$
\boxed{\mathcal F_3^{\rm ev}=\frac38\mathscr DW,\qquad
\mathscr D=\mathscr E^2+
\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}.}
\tag{20}
$$

这说明把 A13 的微分消元作用于平均权后没有额外的临界权重导数残项。
式 (6) 的第一项不能删除；删除后式 (19) 的 $A,B$ 不会相消。

### Step 5. 非偶端点在总阶 $m$ 只贡献纯标量

由式 (11)、(12)，$\mathcal F_3-\mathcal F_3^{\rm ev}$ 到总阶 $m$
只需要其余因子在 $H=L=0$ 的值。这个判断使用的是 $H^m$ 本身的总阶，
而非假设响应独立于 $L$。

在 $H=L=0$，式 (2) 的有限解为

$$
P(0,1,0,x)=-2\log(1-x/4)\pmod{x^p},\qquad
U_i:=P_i(0,0)=\frac{2}{i4^i}.
\tag{21}
$$

写 $u=x/4$，该级数满足
$\mathcal N^2P=2u/(1-u)^2=(x/2)e^P$，由有限三角唯一性即为所求解。
这里只取 $i<p$，没有调用含 $1/p$ 的第 $p$ 个对数系数。
式 (4)、(5) 因而给

$$
t_i(0,0)=-\frac i2U_i,\qquad
q_{i^*}(0,0)=\left(\frac{i^2}{8}-\frac i{16}\right)U_{i^*}.
\tag{22}
$$

第一端点的奇权和 $\sum I\Omega_i^-f_i$ 精确为零，因为 $If_i$ 对称；
第四端点的奇权和 $\sum\Omega_i^-t_it_{i^*}$ 也精确为零。
第二端点因式 (12) 高于目标阶。第三端点在目标总阶等于

$$
\sum_i\Omega_i^-\left(\frac{3i^2}{4}-\frac{3i}{8}\right)U_iU_{i^*}
=-\frac38\sum_i i\Omega_i^-U_iU_{i^*}.
\tag{23}
$$

$i^2$ 项为对称乘积乘奇权，故其和为零。再用

$$
i^2U_iU_{i^*}=-\frac4{4^p}=-1\quad\text{于 }\mathbb F_p,
\qquad \sum_{i=1}^{p-1}i^2U_iU_{i^*}=1,
$$

式 (11)、(23) 得

$$
\boxed{\mathcal F_3-\mathcal F_3^{\rm ev}
=\frac{3\chi}{16}H^m\pmod{(H,L)^{m+1}}.}
\tag{24}
$$

式 (20)、(24) 证明 (U1)。临界反射缺陷的修正是非零实项；
未经平均而直接把 A13 原模 $H^m$ 公式升阶，会漏掉它。

### Step 6. 同一算子一次消去所有未知临界矩与正参数项

令 $V(H)=\sum_{k=0}^{m-1}\beta_kH^k$。由输入 (U2) 及式 (3)，可写

$$
W=V+W_m+O((H,L)^{m+1}),
$$

其中 $W_m$ 是任意的、合法取值于 $\mathbb F_p$ 的总阶 $m$ 齐次多项式。
不要求它为零，也不要求它来自 $p$ 整的无限有理核。
由于

$$
\mathscr EW_m=mW_m,\qquad
\frac{2(H-1)}{H-4}=\frac12+O(H),\qquad
\frac H{H-4}=O(H),
$$

有

$$
\mathscr DW_m=m(m+1/2)W_m=0\pmod{(H,L)^{m+1}},
\tag{25}
$$

因为 $2m+1=p=0$。这不是以零乘一个未定义的 $p^{-1}$ 元素：式 (3)
已经在有限低块自身证明了需要的整性。
于是 $\mathscr DW\equiv\mathscr DV$，而右边只有 $H$。
结合式 (24)，所有目标范围的正 $L$ 项一次消失。

对纯标量低阶，取 $\delta=H\partial_H$。左乘 $H-4$ 后，同一算子成为

$$
(H-4)\mathscr D=(H-4)\delta^2+2(H-1)\delta+H.
$$

其作用在 $V$ 上的第 $n$ 个系数，$1\le n<m$，为

$$
n^2\beta_{n-1}-2n(2n+1)\beta_n=0,
\qquad \frac{\beta_n}{\beta_{n-1}}=\frac{n}{2(2n+1)}.
\tag{26}
$$

所有分母 $2n+1<p$，故此处的约化合法。常数系数也是零。
$H-4$ 为单位，从式 (26) 便得到所有严格预临界标量消失。
本步不重做 A12 的逐核极点及无穷远消失证明。

### Step 7. 仍保留临界有限和，末项必须先消去 $p$

这里只对同一算子 (20) 提取一个系数，不另建 Chebyshev 临界微分算子。
设 $a(H)=2(H-1)/(H-4)$、$b(H)=H/(H-4)$。
逐项卷积给出

$$
[H^m]a\delta V=[H^m](ma-Ha')V.
$$

因 $m=-1/2$ 于 $\mathbb F_p$，直接通分得

$$
m^2+ma-Ha'+b=\frac{H(H+20)}{4(H-4)^2}.
\tag{27}
$$

故式 (20)、(24) 中的临界系数为

$$
[H^m]\mathcal F_3(H,0)
=\frac{3\chi}{16}+\frac3{32}B_m,
\qquad
B_m=[H^m]\frac{H(H+20)}{(H-4)^2}V(H).
\tag{28}
$$

这仅使用预临界 $V$；式 (27) 前因子有一个 $H$，也显示未知 $W_m$
不能影响这个系数。几何展开给

$$
\frac{H(H+20)}{(H-4)^2}
=\sum_{r\ge1}\frac{6r-1}{4^r}H^r.
$$

令 $t_k=4^k(k!)^2/(2k+1)!$。由 $4^m=1$、$m=-1/2$ 得

$$
B_m=\sum_{k=0}^{m-1}\frac{6(m-k)-1}{4^{m-k}}\beta_k
=-2\sum_{k=0}^{m-1}(3k+2)t_k.
\tag{29}
$$

以下望远镜恒等式先在 $\mathbb Q$ 中使用。取 $g_k=k(2k+1)$，则

$$
\frac{t_{k+1}}{t_k}=\frac{2(k+1)}{2k+3},\qquad
g_{k+1}t_{k+1}-g_kt_k=(3k+2)t_k.
\tag{30}
$$

求和后仅剩 $g_mt_m$。不能把含单独 $p^{-1}$ 的 $t_m$ 先约化：必须先算

$$
g_mt_m=mp\frac{4^m(m!)^2}{p!}
=\frac{m4^m(m!)^2}{(p-1)!}\in\mathbb Z_{(p)}.
\tag{31}
$$

在 $\mathbb F_p^\times$ 中把互逆元素配对，只有 $1,-1$ 自逆，故
$(p-1)!=-1$。再将阶乘按 $r$ 与 $p-r$ 分半配对，得到

$$
(-1)^m(m!)^2=-1,\qquad (m!)^2=\chi.
$$

加上 $4^m=2^{p-1}=1$，式 (31) 的约化为 $-m\chi=\chi/2$。
因此式 (29)、(30) 给

$$
B_m=-\chi,\qquad
[H^m]\mathcal F_3(H,0)
=\frac{3\chi}{16}-\frac{3\chi}{32}
=\frac{3\chi}{32}.
\tag{32}
$$

结合 Step 6 的全部低阶与正参数消失，(U3) 得证。$\square$

## Precisely Replaced and Retained Dependencies

这里的“删除”只指本件作为**正簇部分替代证明**时不再调用的证明步骤，
不是删除文件，也不是断言完整第三 forcing 的其他分支不再使用这些结果。

| 原依赖或步骤 | 采用本件后的准确状态 |
| --- | --- |
| A11 中总阶 $n=m$ 的有理核及临界分子恢复，原用于保证 A13 的临界混合系数合法 | 正簇这条证明不再需要；Step 1 的实际有限三角块自身整性已经足够 |
| A11 提供的全部严格预临界矩支撑与数值 (U2) | **仍需保留**其上游证明；本件不证明如何以更弱工具取得这些值 |
| A12 Step 3 的预临界标量逐有理核消失 | 被同一算子加 $\beta$ 的有限递推 (26) 替代 |
| A12 Step 4 的另一个临界 Chebyshev 微分算子及 $\mathscr J,\mathscr J'$ 消元 | 不再调用；平均权的全阶精确消元已经在 Step 3–4 完成，(27) 只是同一算子的系数卷积 |
| A12 真实整数 Chebyshev 临界投影及奇权端点 | **仍需保留**；Step 2、5 在本件完整重证，产生必需的 $3\chi/16$ |
| A12 临界有限和、终项先消 $p$ | **仍需保留**；Step 7 完整重证，不用“同理”或零乘不整元素 |
| A13 原模 $H^m$ 的压缩及单独的临界混合层消失论证 | 由同一个全平均精确恒等式、真实奇权修正及总阶 $m$ 零特征统一替代 |
| 完整四次移位 $E_4$、实际模 $h^M$ 桥、唯一正簇因子及其单位商、局部域论证 | **全部仍保留**；它们不属于本件所替代的有限算子层 |

因此，确实少掉的是正簇证明对**临界有理延拓与第二套临界微分消元**的调用，
以及重复的预临界标量核消失证明。没有少掉对真实低块、预临界矩输入、
真实临界投影、完整端点或实际算术桥的依赖。

## Downstream Scope and Non-Claims

(U3) 恰提供原正簇证明需要的两个输入：

$$
[L^j]\mathcal F_3\in H^{m-j+1}\mathbb F_p[[H]]\quad(1\le j<m),
\qquad
\mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}).
$$

因此可以接回 A13 的原实际四次移位、系数转移、Newton 边及局部域证明，
不改任何规范或阈值。特别地，仍须保留同阶常数的完整合并

$$
(2\chi)^3\frac{3\chi}{32}+(2\chi)^4\left(-\frac3{32}\right)
=-\frac34,
$$

不能把形式三次系数当成实际最终常数。$p\ge5,a\ge2$ 下的桥精度检查及
后续局部域证明仍属于原输入；本件没有重新证明或改变它们。

本件不主张：

- 从三角低块自身整性推出 (U2)，或因取得 (U1) 就完全消除 A11。
- (U1) 无修正地成立于所有总阶，或非偶缺陷在更高含 $L$ 阶仍不贡献。
- 临界矩 $W_m$ 为零、有某个特定值，或有理核的最高主部消失。
- 负簇、完整互素、整个 forcing 分裂域或完整 $C1$–$C3$ 已被本件单独替代。
- 任何页数节省、容量通过、新候选通过、论文立项、Route、PDF 或外部交付。

## Open Risks and Verification Boundary

作者辅助核算对抽象函数 $W(H,L),A(H,L),B(H,L)$ 使用完整乘积导数，
将式 (18) 代入式 (17) 后与式 (20) 比较，符号残差为 $0$；
式 (27) 的独立通分残差也为 $0$。这些核算不依赖素数扫描或拟合，
但只核对所指定代数，不替代证明本身或真正非作者独审。

1. 新增的数学变更是平均权全阶身份、反射修正和总阶商的统一使用；应针对这些
   变更做真正非作者检查，不以作者辅助代数核算替代。
2. 采用本件后，A11 严格预临界矩输入的最小上游证明仍须另行确认；本件不掩盖此依赖。
3. 所有原稿、原失败、评价与已接受产物保持不变；本件只是新版本作者探测记录。
