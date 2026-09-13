# Paper 30：两倍五素数临界根簇的精确二次域证书

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
按本轮完整读取的 `proof-writer` 撰写。本件是作者证明稿，不是独立审查票。
只处理一般平方根主面在 $p=5$ 真正退化的必要边界，不扩大分母或根扫描。

## Claim

保持既定物理正 kick、固定参数 $\lambda$ 与 SUM action。
对每个 $\gcd(r,10)=1$，令

$$
\zeta=e^{2\pi ir/10},\quad h=D_2=2-\zeta^2-\zeta^{-2},\quad
L=\mathbb Q_5(h),\quad \kappa=\lambda-1/16,
\qquad S(\kappa)=\frac{h^4}{5}C_{r,10}(1/16+\kappa).
\tag{1}
$$

规范 $v_h(h)=1$。已接受的 $\kappa=0$ 剩余类中恰有两个实际根。
本件证明这两个根均满足 $v_h(\kappa)=1$，均简单，且经
$K=\kappa/h$ 改标后的单首二次根簇因子剩余式为

$$
\boxed{K^2+2\in\mathbb F_5[K].}
\tag{2}
$$

它在 $\mathbb F_5$ 上不可约且可分。因此原二次根簇因子在 $L$ 上不可约，
两个根在 $L$ 的非分歧二次扩张中分裂。结合已接受的三个外部简单根，
完整 $C_{r,10}$ 无重根。
本件不声称全部根实性，也不声称这些根处更高作用量系数 $Q$ 非零。

## Status

上述精确边界结论：`PROVABLE AS STATED`。

一般 $p\ge7$ 所用 $\gamma=5/3072$ 在 $p=5$ 不再是单位，
其平方根改标的剩余式仅为 $K^2$，不能据此推出本件。
本件采用同一个实际 $C_{r,10}$ 的完整精确六系数证书，
没有替换构造，也没有选择或拟合目标根。

## Assumptions and Inputs

唯一既有结构输入是已接受的
[偶数半阶与两倍素数稿](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)，
SHA256 `2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a`。
使用其准确半阶 action 身份、$S$ 的整性、五次次数及三个外部根简单性。
不重新计算已通过且输入未变的普通剩余层，也不重审已接受的 $p=3$ 边界。

本件不以本轮一般权重稿或 Newton 稿为前提。
下面从旧半阶恒等式直接计算所需的六个新精确系数，
因而 $p=5$ 的结论不会循环依赖一般非退化证明。

## Notation

$\mathcal O=\mathbb Z_5[h]$ 是 $L$ 的整数环，剩余域为 $\mathbb F_5$。
记 $v_5(5)=1$。所有赋值延拓到局部代数闭包，$v_h(0)=+\infty$。
$\operatorname{red}$ 表示在 $\mathbb Q(h)$ 中利用
$h^2-5h+5=0$ 将每个系数唯一化为 $a+bh$，其中 $a,b\in\mathbb Q$。
这只是同一个二次数域的精确运算，不取数值近似。

## Proof Strategy

先将全部实际低半部传播子写入同一个二次域，精确计算
$v_1,\ldots,v_4$。然后用已接受的半阶 action 恒等式保留全部所需的
指数系数至第九阶，得到五次多项式的六个整数二次域系数。
这些系数直接确定 Newton 边与可分剩余式，再对已隔离的二次根簇提升。

## Dependency Map

1. 本原十次圆分关系给出 $h$ 的 Eisenstein 方程及四个低传播子。
2. 真实三角递推给出四个低半部系数；半阶 action 给出准确六系数身份。
3. 二次域赋值公式给出 Newton 边；整的整数尺度改标给出式 (2)。
4. 互素因子 Hensel 引理隔离原二次根簇，单根 Hensel 引理闭合简单性。
5. 已接受的三个外部简单根补齐完整五次多项式。

## Proof

### Step 1. 对全部允许 $r$ 的二次域和传播子

因为 $\zeta$ 为本原十次根，$\Phi_{10}(\zeta)=0$。
将该式除以 $\zeta^2$ 得

$$
(\zeta^2+\zeta^{-2})-(\zeta+\zeta^{-1})+1=0.
$$

代入 $h=2-\zeta^2-\zeta^{-2}$，得到 $D_1=h-1$。
又有 $D_2=D_1(4-D_1)$，从而

$$
h^2-5h+5=0.
\tag{3}
$$

这是在 $5$ 处的 Eisenstein 二次式，因此 $h$ 是 $\mathcal O$ 的素元，
$v_h(5)=2$，剩余域为 $\mathbb F_5$。
半周期和反射关系 $D_{n+5}=4-D_n$、$D_{10-n}=D_n$ 给出

$$
(D_1,D_2,D_3,D_4,D_5)=(h-1,h,4-h,5-h,4).
\tag{4}
$$

这些都是关于任意本原 $\zeta$ 的身份，所以同时覆盖全部允许的 $r$。
两个实嵌入只是式 (3) 中 $h$ 的共轭，不产生另一个构造。

### Step 2. 实际低半部和准确 action

令 $P(t)=\sum_{n=1}^4v_nt^n$，$E(t)=e^{P(t)}$，$F(t)=e^{2P(t)}$，
且 $E_n=[t^n]E$、$F_n=[t^n]F$，负下标系数定义为零。
真实递推只在 $1\le n\le4$ 使用

$$
v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n}.
\tag{5}
$$

第 $n$ 阶右侧仅依赖低于 $n$ 的分支系数，故可递归计算。
在式 (3) 的二次域中化简，得到

$$
\begin{aligned}
v_1&=h/2-2,\\
v_2&=(h/5-1)\lambda-h/5+3/4,\\
v_3&=(h/10+1)\lambda+7h/80-3/8,\\
v_4&=2\lambda^2/5+(2h/5-41/20)\lambda-h/15+127/480.
\end{aligned}
\tag{6}
$$

式 (6) 是特征零的准确有理系数，不在含 $5$ 的分母尚未抵消时约化。
在这里只需要这四个系数，但指数展开仍须取至第九阶。
由已接受的半阶 action 恒等式，令

$$
T=E_4/2+\lambda F_3,
$$

则完整实际首项恰为

$$
\boxed{C_{r,10}=-10E_9-10\lambda F_8+\frac52T^2.}
\tag{7}
$$

为使证书无需无限级数操作，全部所需指数系数可用以下有限递推定义：

$$
E_0=F_0=1,\qquad
E_n=\frac1n\sum_{j=1}^{\min(4,n)}jv_jE_{n-j},\qquad
F_n=\frac2n\sum_{j=1}^{\min(4,n)}jv_jF_{n-j},
\quad 1\le n\le9.
\tag{8}
$$

式 (8) 直接来自 $E'=P'E$、$F'=2P'F$，是特征零恒等式。
尤其其 $n=5$ 项没有被删除；全部含 $5$ 的贡献在式 (7) 中精确保留。

### Step 3. 六个精确系数的有限证书

取一个 $5$ 进单位整数

$$
N=1189085184,\qquad N\equiv4\pmod5,
\qquad f(\kappa)=N S(\kappa).
\tag{9}
$$

把式 (6)、式 (8) 代入式 (7)，再令 $\lambda=1/16+\kappa$，
以式 (3) 化简。完整结果是

$$
f(\kappa)=\sum_{b=0}^5 f_b\kappa^b,
\tag{10}
$$

其中六个系数为

$$
\begin{aligned}
f_0&=678596180h-2464668785,\\
f_1&=14291942400h-53359905600,\\
f_2&=849180842496-257421588480h,\\
f_3&=-103508213760h-781271285760,\\
f_4&=1086278860800h-1171310837760,\\
f_5&=93541367808-76101451776h.
\end{aligned}
\tag{11}
$$

式 (6)、式 (8)、式 (7) 与式 (11) 给出一个封闭的有限有理代数证书。
其每个身份都可在 $\mathbb Q[h,\lambda]/(h^2-5h+5)$ 中用多项式运算核验。
附录的复现代码逐个断言六个差严格等于零，不用容差或根近似。

### Step 4. 从整数系数读取准确赋值与 Newton 边

对非零 $a+bh$，其中 $a,b\in\mathbb Q$，有

$$
v_h(a+bh)=\min\{2v_5(a),\ 1+2v_5(b)\}.
\tag{12}
$$

若一个系数为零，对应项赋值取 $+\infty$。
该公式成立，因为两项有限赋值分别为偶数和奇数，不相等，
故非阿基米德赋值和的等号条件排除抵消。

对式 (11) 写 $f_b=a_b+b_bh$，各整数的赋值是

| 幂次 $b$ | $v_5(a_b)$ | $v_5(b_b)$ | $v_h(f_b)$ |
| --- | --- | --- | --- |
| $0$ | $1$ | $1$ | $2$ |
| $1$ | $2$ | $2$ | $4$ |
| $2$ | $0$ | $1$ | $0$ |
| $3$ | $1$ | $1$ | $2$ |
| $4$ | $1$ | $2$ | $2$ |
| $5$ | $0$ | $0$ | $0$ |

因此 $f$（亦即 $S$，因为 $N$ 为单位）的 Newton 下凸包恰为

$$
\boxed{(0,2)\longrightarrow(2,0)\longrightarrow(5,0).}
\tag{13}
$$

第一条边斜率为 $-1$、水平长度为 $2$，给出两个赋值为 $1$ 的根。
第二条边为外部水平边。这不是从一般平方根尺度强行推出来的边。

### Step 5. 整数尺度剩余式与实际因子

定义完整多项式的辅助改标

$$
U(K)=h^{-2}f(hK).
\tag{14}
$$

由上表，每项系数的赋值 $v_h(f_b)+b-2$ 均非负，
所以 $U\in\mathcal O[K]$。除 $b=0,2$ 外其余均严格为正。
对常数项，用

$$
f_0=5(135719236h-492933757),\qquad h^2=5(h-1)
$$

得到

$$
\overline{h^{-2}f_0}
=\overline{\frac{135719236h-492933757}{h-1}}
=\frac{-2}{-1}=2\quad\text{于 }\mathbb F_5.
$$

又有 $\bar f_2=1$，故

$$
\boxed{\bar U(K)=K^2+2.}
\tag{15}
$$

等价地，原来未乘 $N$ 的尺度满足
$\overline{h^{-2}S(hK)}=4K^2+3$。

为了只提升实际二次根簇，令 $a=f_5\in\mathcal O^\times$。
由式 (11)，$\bar f=\kappa^2(3\kappa^3+1)$，$\bar a=3$。
因此单首多项式 $f/a$ 的剩余分解是
$\kappa^2(\kappa^3+2)$，两因子互素。
由完备环上的互素因子 Hensel 引理，有唯一单首分解

$$
f=aAB,\quad A,B\in\mathcal O[\kappa],\quad
\deg A=2,\quad\deg B=3,\quad
\bar A=\kappa^2,\quad\bar B=\kappa^3+2.
\tag{16}
$$

这里 $A$ 为全部正赋值根的因子；$B(0)$ 为单位，所以不会混入该根簇。
令 $\widetilde A(K)=h^{-2}A(hK)$。从式 (14)、式 (16) 得

$$
\widetilde A(K)=\frac{U(K)}{aB(hK)}.
$$

分母的常数项为单位，其形式倒数属于 $\mathcal O[[K]]$；
而左侧为一个单首二次多项式，所以 $\widetilde A\in\mathcal O[K]$。
由于 $\overline{aB(hK)}=3\cdot2=1$，式 (15) 给出

$$
\overline{\widetilde A}=K^2+2.
\tag{17}
$$

这同时验证尺度改变后的整性和单首根簇的准确剩余式。

### Step 6. 可分提升、不可约性与完整无重根

在 $\mathbb F_5$ 中，平方只有 $0,1,4$，所以 $3=-2$ 不是平方。
$K^2+2$ 不可约，其两个根非零；导数 $2K$ 在两个根处均非零。
令 $L'/L$ 为剩余域 $\mathbb F_{25}$ 的非分歧二次扩张。
其整数环完备，素元仍为 $h$。由单根形式的 Hensel 引理，
式 (17) 的两个不同根分别唯一提升成 $\widetilde A$ 的两个根
$K_+,K_-\in\mathcal O_{L'}^\times$。
它们都是简单根，故 $\kappa_\pm=hK_\pm$ 是 $A$ 的两个简单根，
且 $v_h(\kappa_\pm)=1$。

剩余不可约性还使 $\widetilde A$ 在 $L$ 上不可约：
若它分裂，则因单首整性其根属于 $\mathcal O$，约化将产生
$K^2+2$ 的 $\mathbb F_5$ 根，矛盾。对单首二次式不可约性已经穷尽。
线性变量替换和非零标量乘法保持不可约性，所以 $A$ 也不可约。
根已在二次扩张 $L'$ 中，故其根域恰为该非分歧二次扩张。
剩余 Frobenius 对两个根的作用是 $\alpha\mapsto\alpha^5=-\alpha$。

作为纯导数附带结论，由 $U'(K_\pm)$ 为单位及式 (14)，
有 $v_h(f'(\kappa_\pm))=1$；$N$ 为单位，又得

$$
v_h(S'(\kappa_\pm))=1.
\tag{18}
$$

因子 $B$ 的三个外部根为已接受的简单根，赋值为零，与 $A$ 不相交。
所以 $f$、$S$ 以及原来完整的 $C_{r,10}$ 都无重根。
这证明 Claim。$\square$

## Exact Verification Actually Run

下面代码仅使用式 (3)—(8) 的实际 $s=10$ 恒等式，
生成式 (11) 并核对式 (15)。本次精确运行输出两项 `PASS`。
它不是遍历新的素数、分母或参数列表；没有调用数值求根、resultant 或拟合。

```python
import sympy as s

h, lam, k = s.symbols('h lam k')
M = h*h - 5*h + 5

def red(e):
    num, den = s.fraction(s.cancel(e))
    assert not den.has(lam, k)
    return s.expand(s.rem(num * s.invert(den, M, h), M, h))

D = [0, h-1, h, 4-h, 5-h]
v = [s.S(0)] * 5
E = [s.S(0)] * 10
F = [s.S(0)] * 10
E[0] = F[0] = s.S(1)
for n in range(1, 10):
    if n < 5:
        prev_f = F[n-2] if n >= 2 else 0
        v[n] = red(-(E[n-1]/2 + lam*prev_f) / D[n])
    E[n] = red(sum(j*v[j]*E[n-j]
                   for j in range(1, min(4, n)+1)) / n)
    F[n] = red(2*sum(j*v[j]*F[n-j]
                     for j in range(1, min(4, n)+1)) / n)

T = E[4]/2 + lam*F[3]
C = -10*E[9] - 10*lam*F[8] + s.Rational(5, 2)*T*T
S = red(h**4*C/5)
N = 1189085184
f = red(N*S.subs(lam, k+s.Rational(1, 16)))
expected = [
    678596180*h - 2464668785,
    14291942400*h - 53359905600,
    849180842496 - 257421588480*h,
    -103508213760*h - 781271285760,
    1086278860800*h - 1171310837760,
    93541367808 - 76101451776*h,
]
assert s.Poly(f, k).degree() == 5
for b, value in enumerate(expected):
    assert red(f.coeff(k, b) - value) == 0
print('PASS six exact coefficients')

def mod_h(e):
    value = red(e).subs(h, 0)
    num, den = map(int, s.fraction(value))
    assert den % 5
    return num * pow(den, -1, 5) % 5

residue = [mod_h(value*h**(b-2))
           for b, value in enumerate(expected)]
assert residue == [2, 0, 1, 0, 0, 0]
print('PASS residual h^-2 f(hK)=K^2+2; coefficients', residue)
```

`mod_h` 仅用于已经由赋值表证明整的系数；它先在二次域中约分，
再确认有理分母为 $5$ 进单位，最后取剩余。
不能用“先设 $h=0$”代替含 $h^{-2}$ 表达式的这一步合法化。

## Corrections or Missing Assumptions

无须额外参数假设。本件的 $h=D_2$、中心 $1/16$ 和标量规范始终固定。
一般非退化主面的 $p=5$ 例外由这里独立的准确证书处理，
不是将一般定理的适用条件事后删除。

## Open Risks and Delivery Boundary

- 六系数身份及其尺度推论须由非作者针对本稿准确哈希独立核验，
  本作者的再次精确运行不替代该票。
- 仅证明此必要边界的完整 $C$ 无重根；没有推出全实根或 $\gcd(C,Q)=1$。
- 只新增本稿，保留已接受输入及失败的一般 $p=5$ 主面记录；
  不修改入口、批次状态、冻结原稿或论文构建。
