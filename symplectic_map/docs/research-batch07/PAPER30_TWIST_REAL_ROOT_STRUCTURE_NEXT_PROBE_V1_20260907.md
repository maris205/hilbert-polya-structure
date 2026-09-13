# Proof Package：真实正弦传播子的双向有限保根分类

日期：2026-09-07。作者探针 V1；本轮完整读取并使用 `proof-writer` 技能。
本件含主控协作补充的前向必要性及五分母逆向充分性，经本作者逐项核实后纳入。
因此这是协作作者稿，不是独立验收票，也不作新意或论文容量声明。

## Claim

固定互素整数 $0<r<s$、$s\ge3$，令

$$
D_n=4\sin^2\frac{\pi rn}{s}>0\quad(1\le n<s),\qquad N=s-2.
$$

在实多项式空间 $\mathbb R_N[t]$ 上定义两个对角算子

$$
T^+_{r,s}\!\left(\sum_{k=0}^N c_kt^k\right)
=\sum_{k=0}^N D_{k+1}c_kt^k,
\qquad
T^-_{r,s}\!\left(\sum_{k=0}^N c_kt^k\right)
=\sum_{k=0}^N\frac{c_k}{D_{k+1}}t^k.
\tag{1}
$$

“保实根”指对整个 $\mathbb R_N[t]$ 中的实根多项式保持全实根。
允许重复根与零根；非零常数按无根计。零多项式单独映到零。
因为所有对角权严格为正，非零输入不会变成零，次数也保持。

本件证明完整分类

$$
\boxed{T^+_{r,s}\text{ 保实根}\iff r\equiv\pm1\pmod s,}
\tag{2}
$$
$$
\boxed{T^-_{r,s}\text{ 保实根}\iff
s=3\quad\text{或}\quad(s=5,\ r\equiv\pm2\pmod5).}
\tag{3}
$$

若把“保实根”换成“保全部非正实根”，分类仍相同：充分情形有正权，
必要性反例本身已只有非正实根。这里始终是完整次数上界 $N=s-2$ 的分类，
不是声称每个较低次数都失败；尤其次数 $0,1$ 时正对角算子当然保实根。
确切地，将全非正实根输入的首系数取正后，其系数全部非负；正权保持这个性质。
若输出已知全实根，它便不可能在正实轴上为零。

## Status

式 (2)、(3)：`PROVABLE AS STATED`。

实际首项参数多项式 $C_{r,s}(\lambda)$ 的全部根实性：
`NOT CURRENTLY JUSTIFIED`。上述分类作用于形式相位变量 $t$，
并没有建立首项在参数 $a=-4\lambda$ 中的稳定性。
它提供了真实正弦族上的明确正向结构和逆向障碍，不是原首项的非实根反例。

## Assumptions and source

采用[已核正的原递推](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md)，
在正树权规范中写为

$$
V(t,a)=\sum_{n=1}^{s-1}V_n(a)t^n,\quad E=e^V,\quad F=e^{2V},\quad
V_n=\frac{E_{n-1}+aF_{n-2}}{D_n},
$$
$$
R_s(a)=E_{s-1}+aF_{s-2},\qquad
C_{r,s}(\lambda)=2(-1/2)^sR_s(-4\lambda).
\tag{4}
$$

实际逆传播步骤作用于无常数项的有限多项式 $tP(t)$，对应于
$tP\mapsto tT^-P$，所以式 (1) 的次数和指标没有平移遗漏。
本件不重审[已接受的奇素数无重根及完整非消失](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)。

仅使用一项新外部标准工具：Borcea–Brändén 的有限次数保实根判据。
已亲读作者官方预印本中的稳定性定义及 Theorem 2(b)：对实线性算子
$T:\mathbb R_N[z]\to\mathbb R[z]$，若 $T[(z+w)^N]$ 为双变量实稳定多项式，
则 $T$ 保实根。本文的符号都是正系数实线性因子的乘积，直接验证其稳定性。
[Borcea–Brändén，*Pólya–Schur master theorems for circular domains and their boundaries*，Theorem 2，PDF 第 5 页](https://arxiv.org/pdf/math/0607416#page=5)。
这项标准定理仅支持有限线性算子的分类；它不提供 $R_s$ 的模型身份证明。

## Proof Strategy

先用实际三角恒等式把二次测试的判别式压成一个传播子大小比较。
前向充分性来自一次正弦系数乘子的辐角单调性；
前向必要性选取内部最小谱值，逆向必要性选取内部大谱值。
剩下的五分母例外用完全显式的稳定符号处理。

## Dependency Map

1. 所有必要性反例只依赖真实三角关系、互素指标置换及二次判别式。
2. $r=\pm1$ 的正向充分性由射线辐角直接证明负实根性质，再用标准有限符号判据。
3. $s=3$ 的逆向是常数倍恒等算子；五分母例外由三个正线性因子给出稳定符号。
4. 原参数根问题仍缺少实际非线性递推的不变保根类或另一个精确表示。

## Proof

### Step 1. 两个方向的精确二次测试

真实传播子满足

$$
D_{n-1}D_{n+1}=(D_n-D_1)^2.
\tag{5}
$$

它由 $\sin(x+y)\sin(x-y)=\sin^2x-\sin^2y$ 平方直接得到，
并非只由 $D_n>0$ 或反射对称推出。
对 $2\le n\le s-2$，取

$$
P_n(t)=t^{n-2}(1+t)^2\in\mathbb R_N[t].
\tag{6}
$$

两个输出的非零二次因子分别为

$$
D_{n-1}+2D_nt+D_{n+1}t^2,
\qquad
\frac1{D_{n-1}}+\frac2{D_n}t+\frac1{D_{n+1}}t^2.
$$

其判别式精确等于

$$
\boxed{\Delta_+=4D_1(2D_n-D_1),\qquad
\Delta_-=
\frac{4D_1(D_1-2D_n)}{D_n^2D_{n-1}D_{n+1}}.}
\tag{7}
$$

所有分母严格为正。故 $D_n<D_1/2$ 排除前向保根，
$D_n>D_1/2$ 排除逆向保根。每个负判别式给出一对真正的非实单根；
输入 (6) 只有零根和负实根。

即使要求除必留原点外的输入根严格为负，这种失败也不会消失：
在原无常数项表示中，可将 $t^{n-1}(1+t)^2$ 换成
$t\prod_{j=1}^{n-2}(t+\delta_j)(1+e^{\eta}t)(1+e^{-\eta}t)$，
取互异的小正数 $\delta_j$ 和足够小的非零 $\eta$。
输入的非零根可取为互异负根；输出系数连续依赖这些参数，原先那对非实单根
由简单根的局部连续性仍留在实轴外。这不需要新根扫描。

### Step 2. 正弦系数乘子的正向保根引理

给定 $0<\theta$、整数 $N\ge1$，假定 $(N+1)\theta<\pi$。
定义实系数线性算子

$$
\mathcal S_\theta P(t)
=\operatorname{Im}_{\rm coeff}\!\left(e^{i\theta}P(e^{i\theta}t)\right),
\qquad \mathcal S_\theta(t^k)=\sin((k+1)\theta)t^k.
\tag{8}
$$

下标表示逐系数取虚部；当 $t$ 为实数时，它也是通常的函数虚部。
若 $P=c\prod_{j=1}^d(t+x_j)$、$x_j>0$、$1\le d\le N$，可取 $c>0$。
在 $t=-x$、$x\ge0$ 上考察连续辐角

$$
\Phi(x)=\theta+\sum_{j=1}^d\arg(x_j-xe^{i\theta}),\qquad \Phi(0)=\theta.
$$

每个因子的辐角从 $0$ 连续下降到 $\theta-\pi$，且

$$
\Phi'(x)=-\sin\theta\sum_{j=1}^d
\frac{x_j}{x_j^2-2xx_j\cos\theta+x^2}<0.
\tag{9}
$$

因而
$\Phi(\infty)=(d+1)\theta-d\pi\in(-d\pi,-(d-1)\pi)$。
它恰好穿过 $0,-\pi,\ldots,-(d-1)\pi$ 各一次，且穿越导数非零。
$\mathcal S_\theta P$ 的次数仍为 $d$，因为最高系数乘以正数
$\sin((d+1)\theta)$；所以它恰有 $d$ 个负实单根。
输入的 $x_j$ 可以重复，式 (9) 仍严格成立。

若输入含零根，先提出 $t^b$；剩余辐角的起点改为 $(b+1)\theta$，
终点仍由总次数加一乘 $\theta$ 决定。同一计数证明零根重数保持，
其余根仍为负实单根。非零常数则直接乘以 $\sin\theta$。

特别将该引理用于 $P=(1+t)^N$，得到所有根严格为负的符号切片。
其齐次化
$\mathcal S_\theta[(z+w)^N]$ 是正数乘以
$\prod_{j=1}^N(z+\alpha_jw)$，$\alpha_j>0$。
当 $\operatorname{Im}z,\operatorname{Im}w>0$，每个因子都非零。
由上述有限符号判据，$\mathcal S_\theta$ 因此保持整个
$\mathbb R_N[t]$ 上的全实根，不仅保持同号根。

### Step 3. 前向充分性与必要性

当 $r=1$，取 $\theta=\pi/s$。由于 $N=s-2$，
$(N+1)\theta=(s-1)\pi/s<\pi$。
由逐系数身份

$$
\boxed{T^+_{1,s}=4\mathcal S_\theta\circ\mathcal S_\theta,}
\tag{10}
$$

得到前向保实根。这里是算子复合，不是函数值的平方。
$D_n(s-1,s)=D_n(1,s)$，故 $r=s-1$ 亦成立。

反之，若 $r\not\equiv\pm1\pmod s$，则必有 $s\ge5$。
选取 $n$ 使 $rn\equiv1\pmod s$。它不可能为 $1$ 或 $s-1$，
所以 $2\le n\le s-2$。此时

$$
D_n=d_{\min}=4\sin^2\frac\pi s.
$$

令 $r_0=\min(r,s-r)\ge2$。正弦在 $[0,\pi/2]$ 上递增，因而

$$
D_1\ge4\sin^2\frac{2\pi}s
=4\cos^2\frac\pi s\,d_{\min}>2d_{\min},
\tag{11}
$$

最后一步使用 $s\ge5$。式 (7) 的 $\Delta_+$ 因此严格为负。
这证明式 (2) 的两个方向。

### Step 4. 几乎所有逆向情形的统一反例

若 $s\ge4$ 为偶数，互素性使 $r$ 为奇数。
取内部指标 $n=s/2$，则 $D_n=4>D_1/2$，由式 (7) 得逆向失败。

若 $s\ge7$ 为奇数，考虑四个不同的非零谱指标

$$
k=\pm\frac{s-1}{2},\quad \pm\frac{s-3}{2}\pmod s.
$$

对应的两种传播子值为
$4\cos^2(\pi/(2s))$ 和 $4\cos^2(3\pi/(2s))$，均严格大于 $2$。
乘以 $r$ 在非零剩余类上作置换，故这四个值对应四个不同的 $n$。
删除两个端点 $n=1,s-1$ 后，至少还有一个内部 $n$ 满足
$D_n>2\ge D_1/2$。由式 (7) 得逆向失败。

这些是全部分母、全部互素分子的代数判定，没有枚举或拟合根。

### Step 5. 三分母及五分母边界的完整判定

当 $s=3$，两个互素分子均有 $D_1=D_2=3$，
$T^-P=P/3$，故保实根。这也处理了次数上界 $N=1$ 的边界。

当 $s=5$，记

$$
d_-=(5-\sqrt5)/2,\qquad d_+=(5+\sqrt5)/2.
$$

对 $r=\pm1$，$D_1=d_-$、$D_2=D_3=d_+$，且
$D_1-2D_2=(-5-3\sqrt5)/2<0$，所以逆向失败。

对 $r=\pm2$，序列为 $(D_1,D_2,D_3,D_4)=(d_+,d_-,d_-,d_+)$。
这里二次测试的 $D_1-2D_2=(-5+3\sqrt5)/2>0$，
但仅这个事实并不证明保根；还须检查完整三次空间。
置

$$
\alpha=1/d_+>0,\qquad \beta=1/d_->0,\qquad
\eta=\beta/\alpha=(3+\sqrt5)/2.
$$

其完整符号精确分解为

$$
\begin{aligned}
T^-[(z+w)^3]
&=\alpha w^3+3\beta zw^2+3\beta z^2w+\alpha z^3\\
&=\alpha(z+w)\bigl(z^2+(3\eta-1)zw+w^2\bigr).
\end{aligned}
\tag{12}
$$

因为 $c=3\eta-1=(7+3\sqrt5)/2>2$，存在 $\kappa>0$ 使
$\kappa+\kappa^{-1}=c$。故式 (12) 为
$\alpha(z+w)(z+\kappa w)(z+\kappa^{-1}w)$，
每个正线性因子在双上半平面非零，完整符号实稳定。
有限符号判据保证该 $T^-$ 在 $\mathbb R_3[t]$ 上真正保实根。
结合 Step 4 及三分母情形，式 (3) 的两个方向全部证明。$\square$

## Reproducible exact checks

已实际运行以下精确代数检查；抽象的 $x,h$ 在这里只表示 $D_n,D_1$，
不是对共振参数作 off-$H$ 连续变形。没有输入数值根或新增分母清单。

```python
import sympy as S
x,h,z,w = S.symbols("x h z w", positive=True)
y = (x-h)**2
assert S.factor(4*x*x-4*y-4*h*(2*x-h)) == 0
assert S.cancel(4/x**2-4/y-4*h*(h-2*x)/(x*x*y)) == 0
lo,hi = (5-S.sqrt(5))/2,(5+S.sqrt(5))/2
alpha,beta,eta = 1/hi,1/lo,(3+S.sqrt(5))/2
assert S.simplify(beta/alpha-eta) == 0
symbol = alpha*w**3+3*beta*z*w**2+3*beta*z*z*w+alpha*z**3
assert S.simplify(symbol-alpha*(z+w)*(z*z+(3*eta-1)*z*w+w*w)) == 0
assert S.simplify(lo-2*hi-(-5-3*S.sqrt(5))/2) == 0
assert S.simplify(hi-2*lo-(-5+3*S.sqrt(5))/2) == 0
print("EXACT_PASS: trigonometric discriminant identities and fifth-denominator symbol")
```

## Corrections or Missing Assumptions

本件没有修正已接受的素数简单性或 $C,Q$ 互素定理。
新分类指出，“传播子来自真实三角函数”并不能让实际所需的逆传播子自动
成为通常的保实根线性算子；事实上它在除式 (3) 外的全部分母上失败。
另一方面，前向确有强保根性质，但只在 $r=\pm1$，且方向与递推使用的相反。

这仍不能决定 $R_s(a)$ 的根，原因具体为：

1. 式 (1) 作用于相位级数变量 $t$，而目标根位于参数 $a$；两者尚无已证明的保根转换。
2. 实际 forcing 由 $e^V,e^{2V}$ 非线性生成，不是任意实根多项式。
   上面的失败反例排除无条件算子法，却不否定真实 forcing 落在更小的不变类中。
3. 没有证明该更小类在指数、乘法、终端提取及逆传播下封闭；
   也没有建立一个不依赖事后根的稳定符号来代表 $R_s$。

全文没有把 off-$H$ 处默认成反射对称的共振模型，没有重试旧路径、
Hermitian 收缩、参数仿射指数或三常数导数闭包。

## Open Risks and Delivery Boundary

- 原实际全实根命题仍 OPEN；本件既没有给出实际 $C$ 的非实根，也没有证明其全实。
- 经典有限稳定性工具不计为原创贡献；针对这套传播子的分类也未进行全球新意认证。
- 主控补充的两条必要／充分性已纳入协作作者证明，仍须非作者独立核查。
- 本轮仅新建本文件；旧作者稿、接受处置、入口、冻结锁及旧根扫描结果均未修改。
- 未做新根扫描、浮点拟合、跨系统构造、论文立项、PDF 或对外操作。
