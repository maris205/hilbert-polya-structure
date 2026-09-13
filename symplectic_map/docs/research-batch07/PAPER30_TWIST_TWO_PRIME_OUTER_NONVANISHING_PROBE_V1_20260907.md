# Paper30：两倍奇素数分母的负指数正规化与次项非消失 V1

日期：2026-09-07。作者探针；独立核查尚待完成。

## Claim and scope

本件原任务是排除 $s=2p$ 首项的外层简单根与次项的共同根。
在同一实际递推中，所得首层正规化实际给出更强的全根排除。
固定奇素数 $p$、$s=2p$ 及互素 $0<r<2p$，保持已接受的物理规范

$$
v_n=-\frac{[t^{n-1}]e^v/2+\lambda[t^{n-2}]e^{2v}}{D_n},
\qquad v_{2p}=0,
\qquad Q_{r,2p}=-2p[t^{2p+1}]e^{-v},
$$

其中 $D_n=2-\zeta^n-\zeta^{-n}$、$\zeta=e^{2\pi ir/(2p)}$；
计算 $Q$ 时继续原递推到 $n=2p+1$，不删除指数的共振系数。

置

$$
\xi=-\zeta,\quad \pi=\xi-1,\quad
g=2-\xi-\xi^{-1}=D_{p+1},\quad
h=D_2=g(4-g),\quad m=(p-1)/2.
$$

在完成实分圆子域的整数环 $\mathcal O^+$ 中，有

$$\boxed{
\frac{g^p}{p}Q_{r,2p}\in\mathcal O^+[\lambda],
\qquad
\overline{\frac{g^p}{p}Q_{r,2p}}=\frac1{64}.}
\tag{1}
$$

等价地，

$$\boxed{
\frac{h^p}{p}Q_{r,2p}\in\mathcal O^+[\lambda],
\qquad
\overline{\frac{h^p}{p}Q_{r,2p}}=\frac1{16},
\qquad
\overline{h^{m+1}Q_{r,2p}}=\frac{(-1)^{m+1}}{16}.}
\tag{2}
$$

横线指 $\mathcal O^+/(h)=\mathbb F_p$ 上的多项式约化。
因此对任意代数整数参数 $\lambda$，在相应有限局部扩张中均有

$$
v_h\bigl(Q_{r,2p}(\lambda)\bigr)=-(m+1),
\qquad v_\pi\bigl(Q_{r,2p}(\lambda)\bigr)=-(p+1).
\tag{3}
$$

利用已接受的首项整数化及单位最高系数，所有 $C_{r,2p}$ 根均为局部代数整数。
故式 (1)–(3) 推出

$$\boxed{\gcd(C_{r,2p},Q_{r,2p})=1\qquad\text{对所有奇素数 }p.}
\tag{4}
$$

这包括原任务的 $m+1$ 个外层简单根，也包括尚待进一步分析的内层根簇。
本件不证明内层根简单，不证明全部根实；没有推广到其他偶数分母或素数幂分母。

## Status

- 本件作者证明：式 (1)–(4) 完成，等待非作者限定核查。
- 旧奇素数 $C,Q$ 结果不重开；已有 $2p$ 首项约化按接受范围引用。
- 不使用新增素数列表、浮点根搜索、有限例子外推或目标零点拟合。
- 不改变论文立项、Route 状态、正文页数或 PDF 验收状态。

## Assumptions and dependency map

1. $p\ge3$ 为奇素数；$\xi=-\zeta$ 是本原 $p$ 次单位根。
   令 $K=\mathbb Q_p(\xi)$、$\mathcal O=\mathbb Z_p[\xi]$，
   $v_\pi(\pi)=1$、$v_\pi(p)=p-1$。
   实子域 $K^+=\mathbb Q_p(g)=\mathbb Q_p(h)$ 的整数环为
   $\mathcal O^+=\mathcal O\cap K^+$，$g,h$ 均为其均匀化元，$v_h(p)=m$。
   注意 $\mathcal O/(h)$ 不被当作 $\mathbb F_p$；
   中间步骤使用 $\mathcal O/(\pi)=\mathbb F_p$，最后返回 $\mathcal O^+$。
2. $Q=-2p[t^{2p+1}]e^{-v}$ 来自已接受的
   [单插入规约](PAPER30_TWIST_SINGLE_INSERTION_VARIATIONAL_GERM_DISPOSITION_20260907.md)。
   本件证明的是该既定系数的非消失，不另换次项定义。
3. 最后一步只调用
   [偶分母结构作者稿](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)
   及其已接受核查中的

   $$
   S=\frac{h^{p-1}}pC_{r,2p}\in\mathcal O^+[\lambda],\quad
   \deg S=p,\quad
   \bar S=2\kappa^p+\frac{\kappa^m}{4},\qquad
   \kappa=\lambda-\frac1{16}.
   \tag{5}
   $$

   输入作者稿 SHA256：

   ```text
   2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a
   ```

   式 (1)–(3) 的证明不依赖 $C$ 根簇的进一步结构。

## Proof strategy

将原正支缩放为 $V(x)=v(\pi x)$，但保留全部低于 $2p$ 的非共振模式，
而非只保留此前半作用量中的低于 $p$ 的半支。
此时偶部分 $A(x^2)$ 的系数整数，奇部分为 $\pi B(x)$。

末端 $V_{2p+1}$ 与负指数中的两个 $p!$ 极点精确相消。
随后普通奇指数项由 $e^Ae^{-A}=1$ 消尽，只留下奇指数第 $p$ 项。
这个 Frobenius 项在偶模递推的 $p+1$ 阶产生一个确定缺陷，
最终给出与 $\lambda$ 无关的非零常数 $1/128$。

## Detailed proof

### Step 1：实际传播子、缩放与有限支的整性

对 $1\le n\le2p-1$，有

$$
D_n\equiv4\pmod{\pi^2}\quad(n\text{ 奇}),
\qquad
\frac{D_n}{\pi^2}\equiv-n^2\pmod\pi\quad(n\text{ 偶}).
\tag{6}
$$

第二式的右边非零，因为该范围内的偶数 $n$ 不是 $p$ 的倍数。
第一式包含中央模式 $n=p$，此时 $D_p=4$ 精确成立。
缩放递推为

$$
D_nV_n=-\frac\pi2[x^{n-1}]e^V
-\lambda\pi^2[x^{n-2}]e^{2V}.
\tag{7}
$$

由三角递推归纳得

$$
V_{2j}\in\mathcal O[\lambda],\qquad
V_{2j+1}\in\pi\mathcal O[\lambda]
\quad(1\le n<2p).
\tag{8}
$$

这里所需的指数整性可直接逐项检查：
若已有前缀为 $A(x^2)+\pi B(x)$，$B$ 为奇多项式，
则次数不超过 $2p-2$ 的偶指数系数整数，
次数不超过 $2p-1$ 的奇指数系数在 $\pi\mathcal O[\lambda]$ 中。
来自 $A$ 的阶乘至多为 $(p-1)!$；来自 $B$ 的第 $k$ 项具有赋值

$$
v_\pi\left(\frac{\pi^k}{k!}\right)
=k-(p-1)\lfloor k/p\rfloor
\qquad(0\le k\le2p+1<p^2).
\tag{9}
$$

偶数 $k>0$ 的赋值至少为二，奇数 $k$ 的赋值至少为一。
因此奇 $n$ 在式 (7) 中除以单位，偶 $n$ 在分子含 $\pi^2$ 后再除以
$D_n=\pi^2\cdot\text{单位}$，归纳成立。

写完整有限支

$$
P(x)=\sum_{n=1}^{2p-1}V_nx^n=A(w)+\pi B(x),\quad w=x^2,
$$
$$
A(w)=\sum_{j=1}^{p-1}a_jw^j,\qquad
B(x)=x b(w),\qquad b(w)=\sum_{j=0}^{p-1}b_jw^j.
\tag{10}
$$

定义

$$
E(w)=e^{A(w)},\qquad H(w)=e^{-A(w)},\qquad
E_j=[w^j]E,\quad H_j=[w^j]H,\quad
c=\frac1{2D_1}.
$$

对 $0\le j<p$，$E_j,H_j$ 都整数；$E_p,H_p$ 可以各自含 $1/p$。
然而因为 $p$ 为奇数，$E_p+H_p$ 中的第 $p$ 次指数项相消，故该和整数。
原递推的一阶给出精确式 $b_0=-c$。

### Step 2：必须保留的两个奇指数项

记

$$\tau=\frac{\pi^{p-1}}{p!}\in\mathcal O^\times.
\tag{11}
$$

由 $\prod_{j=1}^{p-1}(1-\xi^j)=p$，约去 $\pi^{p-1}$ 并取模，得到
$p/\pi^{p-1}\equiv(p-1)!\equiv-1$；
最后一个同余由非零剩余类按逆元配对，只有 $1,-1$ 自配对得到。
所以 $\bar\tau=1$。

式 (9) 进一步表明：在奇指数系数除以 $\pi$ 后，
恰好 $k=1,p$ 两项可能贡献模 $\pi^2$ 的首层；其余奇数 $k$ 的赋值至少为二。
这里也包含最大可能的 $k=2p+1$，其除以 $\pi$ 后赋值恰为二，不能误认为单位。
对偶指数，所有 $k>0$ 的贡献在 $\pi^2$ 中，包括 $k=2p$。

因而对本件使用的有限系数有

$$
[x^{2p}]e^P=E_p+\pi^2 R_0,
\qquad [x^{2p-1}]e^{2P}\in\pi\mathcal O[\lambda],
\tag{12}
$$

以及

$$
\frac1\pi[x^{2p+1}]e^{-P}
=-[x^{2p+1}]HB-\tau[x^{2p+1}]HB^p+\pi^2 R_1,
\tag{13}
$$

其中 $R_0,R_1\in\mathcal O[\lambda]$。
式 (13) 的 $k=1$ 项可能带有 $H_p$；该项被原样保留而没有先取模。
其余奇 $k\ge3$ 所剩 $A$ 次数至多 $p-1$，没有额外的 $p!$ 分母。
式 (12) 中 $k\ge2$ 的剩余 $A$ 次数也至多 $p-1$。
这说明式 (12)–(13) 的整系数余项没有隐藏的 $\pi^2/p$。

同时，由奇模式 $n=2j+1<2p$ 的实际递推及式 (6)，得

$$
b_j+cE_j\in\pi^2\mathcal O[\lambda]
\qquad(1\le j\le p-1).
\tag{14}
$$

确切地说，$e^P$ 的相应偶系数与 $E_j$ 相差 $\pi^2$ 倍整数，
$\lambda\pi[e^{2P}]_{2j-1}$ 也在 $\pi^2$ 中，
并且 $D_{2j+1}-D_1\in\pi^2\mathcal O$。
因此这里可保留同一个精确系数 $c$，而不是提前用 $1/8$ 替换极点前系数。

### Step 3：末端正规化使全部普通卷积相消

令

$$J=[x^{2p+1}]e^{-V(x)},\qquad V(x)=v(\pi x).
$$

由于 $V_{2p}=0$，末端只线性进入指数，故

$$
J=-V_{2p+1}+[x^{2p+1}]e^{-P}.
$$

而 $D_{2p+1}=D_1$，所以原递推给出精确式

$$
\frac J\pi
=c[x^{2p}]e^P+\frac{\lambda\pi}{D_1}[x^{2p-1}]e^{2P}
+\frac1\pi[x^{2p+1}]e^{-P}.
\tag{15}
$$

代入式 (12)–(13)，并使用 $b_0=-c$，得到

$$
\frac J\pi
=c(E_p+H_p)-\sum_{j=1}^{p-1}H_{p-j}b_j
-\tau[x^{2p+1}]HB^p+\pi^2R_2.
\tag{16}
$$

前两项均已整数；这一步先消除了 $E_p,H_p$ 的 $p!$ 极点。
之后才能使用式 (14)。因 $H_{p-j}$ 对 $1\le j\le p-1$ 都整数，

$$
\frac J\pi
=c\left(E_p+H_p+\sum_{j=1}^{p-1}H_{p-j}E_j\right)
-\tau[x^{2p+1}]HB^p+\pi^2R_3.
$$

括号是 $[w^p]HE=0$，严格为零而非只模零。因此

$$
\frac J\pi\in\mathcal O[\lambda],\qquad
\overline{\frac J\pi}=-[x^{2p+1}]\bar H\,\bar B^p.
\tag{17}
$$

Frobenius 及奇支最低次数给出

$$
\bar B^p=\bar b_0^{,p}x^p+O(x^{3p})
=-\frac{x^p}{8}+O(x^{3p}),
$$

而 $3p>2p+1$。因此

$$\boxed{
\overline{\frac J\pi}=\frac18\bar H_{m+1}.}
\tag{18}
$$

这里的 $A$ 是完整 $n<2p$ 分支的偶部分。
若误将它替换为旧半支中仅含 $n<p$ 的截断，则不能求得正确的 $H_{m+1}$。

### Step 4：偶模的首个 Frobenius 缺陷

以下只在已整数化的有限系数上取模，并记

$$\kappa=\lambda-\frac1{16},\qquad q=\frac\kappa4,
\qquad N_w=w\frac{d}{dw}.
$$

式 (14) 和 $b_0=-c$ 给出

$$
\bar B=-\frac{x}{8}\bar E\pmod{x^{2p}},
\qquad \bar B^p=-\frac{x^p}{8}\pmod{x^{2p+1}}.
\tag{19}
$$

偶模式 $2\le n\le2p-2$ 的式 (7) 除以 $\pi^2$。
利用式 (6) 以及正指数版的式 (13)，即保留 $B+\tau B^p$，得到

$$
N_x^2\bar A
=\frac{x}{2}e^{\bar A}(\bar B+\bar B^p)
+\lambda x^2e^{2\bar A}
=\kappa x^2e^{2\bar A}-\frac{x^{p+1}}{16}e^{\bar A}
\pmod{x^{2p}}.
$$

等价地，对 $w^1,\ldots,w^{p-1}$ 的系数有

$$\boxed{
N_w^2\bar A=qwe^{2\bar A}
-\frac{w^{m+1}}{64}e^{\bar A}\pmod{w^p}.}
\tag{20}
$$

式中的指数仅指这些次数的有限指数系数；它们用到的阶乘严格小于 $p$，
不在特征 $p$ 中定义一个无条件的无限指数。

对 $1\le j\le m$，第二项尚未出现，唯一三角解与

$$A^{(0)}(w)=-\log(1-qw)$$

的相应有限系数相同。基准满足
$N_w^2A^{(0)}=qwe^{2A^{(0)}}$。
在第一个受缺陷影响的 $j=m+1$ 阶，右边第一项只依赖此前系数，
第二项仅贡献 $-1/64$，所以

$$
\bar a_{m+1}-[w^{m+1}]A^{(0)}
=-\frac1{64(m+1)^2}=-\frac1{16}\quad\text{于 }\mathbb F_p.
\tag{21}
$$

最后等号使用 $m+1\equiv1/2\pmod p$。
因 $m+1\ge2$ 且 $e^{-A^{(0)}}=1-qw$，这给出

$$\boxed{\bar H_{m+1}=\frac1{16}.}\tag{22}
$$

特别地，该数与 $\lambda$ 无关。
把式 (22) 代入式 (18)，得到

$$\boxed{
\frac J\pi\in\mathcal O[\lambda],\qquad
\overline{\frac J\pi}=\frac1{128}.}
\tag{23}
$$

上述所有次数界和单位分母对 $p=3$ 同样成立；没有排除最小奇素数。

### Step 5：返回实子域与物理 $Q$

有精确关系

$$g=-\frac{\pi^2}{\xi},\qquad
\pi^{2p}=(-g\xi)^p=-g^p,
$$

所以由 $Q=-2p[t^{2p+1}]e^{-v}$ 得

$$
\frac J\pi=-\frac{\pi^{2p}}{2p}Q
=\frac{g^p}{2p}Q.
\tag{24}
$$

式 (24) 属于 $K^+[\lambda]$；与式 (23) 的 $\mathcal O[\lambda]$ 整性相交，
便得到 $\mathcal O^+[\lambda]$ 整性。
式 (23)–(24) 给出式 (1)。
因 $h/g=4-g$，乘以 $(4-g)^p$ 后约化为 $4^p=4$，得到式 (2) 的前两式。

此外

$$
\overline{p/h^m}
=\frac{-1}{(-4)^m}=(-1)^{m+1},
$$

这里 $4^m=2^{p-1}=1$。
于是

$$
h^{m+1}Q=\frac p{h^m}\frac{h^p}pQ
$$

具有式 (2) 的非零常数约化。
把一个系数整数、约化为非零常数的多项式代入任意局部代数整数，
所得必为单位；这证明式 (3)。

### Step 6：在全部首项根上非消失

式 (5) 的最高次系数约化为 $2\ne0$，因为 $\deg_\lambda\kappa^p=p$，
其余项次数小于 $p$。将 $S$ 除以其单位最高系数，得到
$\mathcal O^+[\lambda]$ 中的首一多项式。
所以它的每个代数根 $\lambda_*$ 均在相应有限局部扩张的整数环中。

式 (2) 在任意这样的扩张中仍约化为同一个非零常数，
故 $Q(\lambda_*)\ne0$，得到式 (4)。
这一推理不要求内层根简单，也不要求根落在 $K^+$ 本身。
外层与内层使用的是同一个 $Q$ 多项式和同一个正规化，没有拼接不同构造。

在局部代数闭包中没有共同根也排除了原实分圆数域中的非平凡 gcd，
并排除了其任意特征零扩张中的共同因子。

## Verification and error audit

本件没有用有限素数实验承担一般结论。以下为证明内的精确检查点：

1. 使用完整 $n<2p$ 分支，$V_{2p}=0$ 而指数共振系数不置零。
2. 末端传播子 $D_{2p+1}=D_1$ 精确，不使用其仅模意义的近似。
3. $E_p,H_p$ 各自可能非整数；先以精确 $c=1/(2D_1)$ 配对后才取模。
4. 奇指数除以 $\pi$ 后只留下 $k=1,p$；$k=2p+1$ 被赋值二的余项覆盖。
5. 偶指数 $k=2p$ 同样是赋值二的余项；剩余 $A$ 阶乘均小于 $p$。
6. $e^Ae^{-A}=1$ 消去的是精确有限卷积，不是未经正规化的特征 $p$ 指数乘法。
7. 偶递推在 $w^{m+1}$ 的新项来自同一个 $p!$ Frobenius 项，
   系数依次为 $-1/16$、除以 $N_x^2=4N_w^2$ 后 $-1/64$。
8. $\bar H_{m+1}=1/16$ 的符号由 $H=e^{-A}$ 再取负号得到。
9. $\pi^{2p}=-g^p$ 精确，保证最终正规化确实属于实子域。
10. 全部 $C$ 根的整数性仅用已接受首项的单位最高系数，
    不借用尚未证明的内层简单性或实根性。

## Corrections or missing assumptions

没有修改旧接受稿。本件特别排除三种会破坏证明的捷径：

- 不能把旧半支 $A_{\le m}$ 当作完整 $A$ 来求 $H_{m+1}$；
  新 Frobenius 缺陷恰好发生在被旧半支截去的下一阶。
- 不能在式 (15) 中先把 $c$ 换为 $1/8$ 后分别约化 $E_p,H_p$；
  单独的误差可能乘上 $1/p$。式 (16) 先精确消除该极点。
- 不能忽略奇指数第 $p$ 项；若只保留普通 $B$ 项，
  卷积相消后会错误得到零。

## Open risks and delivery boundary

- 本件作者证明仍须针对实际文本接受非作者核查；不自授 `PASS`。
- $s=2p$ 内层首项根的简单性和全部根实性没有由本件解决。
- 不推广到一般偶数、奇合数或素数幂分母。
- 仅新增本文件；不改旧稿、锁、脚本、失败记录或状态入口。
- 没有新根扫描、图像、论文试写、PDF 构建、Route 评价或对外操作。
