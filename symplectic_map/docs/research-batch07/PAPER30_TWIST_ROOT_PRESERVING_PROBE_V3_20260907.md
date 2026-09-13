# Root-preserving probe V3：根单位差分与反函数的精确规约

日期：2026-09-07。本轮选择的唯一路径是根单位差分 $\to$ 反函数／Lagrange
系数 $\to$ 有限阶循环芽的射流条件。未重新检查旧直接线性路径、Green
Hermitian 捷径或 Jacobi–Schur 接口；未做新的根扫描。
已完整读取本轮 `proof-writer` 技能及
[上轮处置](PAPER30_TWIST_POST_CANCELLATION_AND_BRIDGE_DISPOSITION_20260907.md)。
该技能要求把实际新规约、失败的具体表示与未证明的全实根命题分开。

## Claim

原问题仍为：所有互素 $0<r<s$、$s\ge3$ 的真实双谐波共振首项
$C_{r,s}(\lambda)$ 是否有 $\lfloor s/2\rfloor$ 个正实单根？

本轮具体目标是把其正频首项改写成反函数指数系数，并检验该改写能否
落入一个参数仅仿射出现的指数族；同时准确识别相应的根单位共振障碍。
没有把有限实例替代全分母验收目标。

## Status

- 原全分母实根／简单性：`NOT CURRENTLY JUSTIFIED`。
- 以下反函数系数式及循环芽的有限射流等价：`PROVABLE AS STATED`。
- 具体候选表示 $w(y,a)=w_0(y)+a w_1(y)$ 在实际五分母已被精确排除。
  这不是实际 $C$ 的非实根反例，也不否定更深的保根表示。

## Assumptions and notation

固定互素 $r,s$。设

$$
\zeta=e^{2\pi ir/s},\qquad
D_n=2-\zeta^n-\zeta^{-n}=4\sin^2(\pi rn/s),\qquad a=-4\lambda.
$$

本稿使用正树权规范；形式变量为物理正相位变量 $X=\epsilon e^{i\theta}$
的缩放 $t=-X/2$，格点 $j$ 处乘 $\zeta^j$。定义唯一截断多项式

$$
v(t,a)=\sum_{n=1}^{s-1}v_n(a)t^n,
\quad E=e^v,\quad F=e^{2v},
\quad v_n=\frac{E_{n-1}+aF_{n-2}}{D_n}.
$$

取 $E_0=F_0=1,F_{-1}=0$。首项为

$$
R_s(a)=[t^s](t e^v+a t^2e^{2v}),\qquad
C_{r,s}(\lambda)=2(-1/2)^sR_s(-4\lambda).
$$

置

$$
Y(t)=t e^{v(t)},\qquad T(y)=Y^{-1}(y),\qquad
w(y)=\log\frac{y}{T(y)},\qquad H_a(y)=y+ay^2.
$$

这里 $Y^{-1}$ 是复合反函数，不是逐点倒数；$Y'(0)=T'(0)=1$。
所有对数均用于常数项为 $1$ 的单位级数，因而无分支歧义。
只需有限射流时使用形式级数；固定 $a\in\mathbb C$ 时，截断 $v$ 为多项式，
上述 $Y,T$ 也确实定义原点附近的解析芽。

本稿没有把这里的 $t$ 或 $T$ 与未缩放的物理次项变量混用，亦不重推 $Q$。

## Proof strategy and dependency map

1. 真实 $D_n$ 使线性算子成为根单位差分 $2-S_\zeta-S_{\zeta^{-1}}$。
2. 指数换元 $Y=t e^v$ 把差分变成乘法对数恒等式。
3. 形式留数换元严格给出反函数系数式，不要求未证明的保根性质。
4. 有限群平均给出循环芽的反向线性化，控制规范自由度及相关射流。
5. 用反函数的四阶系数检验“参数仿射指数”这个具体候选身份。

## Proof

### Step 1. 真实根单位差分的首个障碍

记 $(S_\zeta f)(t)=f(\zeta t)$、
$\mathcal D_\zeta=2-S_\zeta-S_{\zeta^{-1}}$。
因为 $\mathcal D_\zeta t^n=D_nt^n$，原有限三角递推等价于

$$
\mathcal D_\zeta v
=H_a(Y(t))-R_s(a)t^s+O(t^{s+1}).\tag{1}
$$

理由是低于 $s$ 阶的系数逐项相等，而 $D_s=0$，故 $s$ 阶左边为零。
由于 $Y(\zeta t)Y(\zeta^{-1}t)/Y(t)^2$ 的常数项为 $1$，式 (1)亦即

$$
\log\frac{Y(t)^2}{Y(\zeta t)Y(\zeta^{-1}t)}
=Y(t)+aY(t)^2-R_s(a)t^s+O(t^{s+1}).\tag{2}
$$

这不是只依赖传播子正性或反射对称的重写；它使用完整的根单位差分身份。

### Step 2. 反函数的准确 Bell／Lagrange 系数式

有

$$
\boxed{\displaystyle
R_s(a)=\frac1s[y^{s-1}](1+2ay)e^{s w(y,a)}.}\tag{3}
$$

为明确其规范，直接作留数推导：

$$
\begin{aligned}
R_s
&=\operatorname{Res}_{t=0}H_a(Y(t))t^{-s-1}\,dt\\
&=\operatorname{Res}_{y=0}H_a(y)T'(y)T(y)^{-s-1}\,dy\\
&=\frac1s\operatorname{Res}_{y=0}H_a'(y)T(y)^{-s}\,dy\\
&=\frac1s[y^{s-1}](1+2ay)e^{s w(y)}.
\end{aligned}
$$

第三步使用一个 Laurent 级数导数的留数为零：对
$H_a(y)T(y)^{-s}$ 求导并移项即可。形式换元因 $T'(0)=1$ 可逆而合法。
式 (3)只用 $w$ 至 $y^{s-1}$，等价于 $Y$ 至 $t^s$，所以原先只求
$v_1,\ldots,v_{s-1}$ 足够，不需要假定或反演共振的 $D_s$。

这给出了全分母的非递归提取形式，但其中 $w$ 仍由非线性消元决定。
单凭“写成指数系数”不产生实根定理。

### Step 3. 与有限阶循环芽的严格等价

定义解析芽

$$
\mathcal F(y)=Y(\zeta T(y)).
$$

其 $\mathcal F'(0)=\zeta$，并且
$\mathcal F^{\circ s}=\operatorname{id}$；因为 $\zeta$ 本原，它的复合阶
恰为 $s$。复合逆为 $\mathcal F^{-1}(y)=Y(\zeta^{-1}T(y))$。
在式 (2)中代入 $t=T(y)=y+O(y^2)$ 后得到

$$
\boxed{\displaystyle
\log\frac{\mathcal F(y)\mathcal F^{-1}(y)}{y^2}
=-y-ay^2+R_s(a)y^s+O(y^{s+1}).}\tag{4}
$$

分子表示两个值的普通乘积，不是复合；$T(y)^s=y^s+O(y^{s+1})$ 保证
障碍项的系数没有改变。于是 $R_s(a)=0$ 蕴含存在上述循环芽，满足

$$
\log\frac{\mathcal F(y)\mathcal F^{-1}(y)}{y^2}
=-y-ay^2+O(y^{s+1}).\tag{5}
$$

反向亦成立。设某解析芽（形式芽亦可）$\mathcal G$ 满足
$\mathcal G'(0)=\zeta$、$\mathcal G^{\circ s}=\operatorname{id}$ 及式 (5)。
用有限群平均定义

$$
\widetilde T(y)=\frac1s\sum_{j=0}^{s-1}\zeta^{-j}\mathcal G^{\circ j}(y).
$$

其导数为 $1$，且重新编号求和给出
$\widetilde T(\mathcal G(y))=\zeta\widetilde T(y)$。
置 $\widetilde Y=\widetilde T^{-1}$、
$\widetilde v=\log(\widetilde Y/t)$。则
$\mathcal G=\widetilde Y\circ(\zeta\,\cdot)\circ\widetilde T$。
将式 (5)变回 $t$，得到

$$
\mathcal D_\zeta\widetilde v
=\widetilde Y+a\widetilde Y^2+O(t^{s+1}).
$$

在 $1\le n<s$ 上，非零的 $D_n$ 逐阶强制
$\widetilde v_n=v_n$。在 $n=s$，左边为零，右边恰为同一个 $R_s(a)$，
因为 $[t^s](t e^{\widetilde v}+at^2e^{2\widetilde v})$ 只依赖
$\widetilde v_1,\ldots,\widetilde v_{s-1}$。故 $R_s(a)=0$。

因此，对每个固定复参数 $a$，**首项消失等价于存在复合阶为 $s$、线性部为
$\zeta$ 的解析循环芽，满足有限射流条件 (5)**。

规范自由度不会改变这个结论。若 $c=\widetilde v_s$，则
$h(t)=t e^{-ct^s}$ 满足 $h(\zeta t)=\zeta h(t)$。
将 $\widetilde Y$ 换成 $\widetilde Y\circ h$ 完全不改变 $\mathcal G$，
而把 $\widetilde v_s$ 置零、保持所有较低系数不变。
因此共振位置的可选规范不影响 $R_s$ 或 (5)。对数条件到 $y^s$ 涉及芽到
$y^{s+1}$ 的射流；上述共轭与规范操作是完整芽恒等式，并未遗漏这一阶。

这是首个有限射流障碍的等价表述，**不是**原辛映射的可积性或实际不变曲线定理。

### Step 4. 参数仿射指数这个候选身份在真实族失败

为把 (3)进一步化成一个固定的、参数只线性进入指数的 Bell 族，最直接的
候选是假定 $w(y,a)=w_0(y)+a w_1(y)$ 至所需阶。
实际逆函数已经在 $y^4$ 排除该身份。

由 $T=Y^{-1}$ 的直接四阶消元，或再次作上述留数换元，有

$$
[y^4]w
=v_4-4v_1v_3-2v_2^2+8v_1^2v_2-\frac83v_1^4.
$$

在共振前 $s\ge5$，$v_1$ 不含 $a$，$v_2,v_3$ 至多一次，且

$$
[a]v_2=\frac1{D_2},\qquad
[a^2]v_4=\frac2{D_2D_4}.
$$

因而

$$
\boxed{\displaystyle
[a^2y^4]w(y,a)=\frac{2(D_2-D_4)}{D_2^2D_4}.}\tag{6}
$$

在真实五分母中，两个互素代表分别给出

$$
r=1:\quad [a^2y^4]w=\frac{\sqrt5-1}{5}>0,
\qquad
r=2:\quad [a^2y^4]w=-\frac{\sqrt5+1}{5}<0.
$$

两值来自 $D_1D_2=5$、$D_4=D_1$，无需浮点求根。
因此 $w$ 不仅不是参数仿射，连这个高次参数系数的符号也不能对真实互素代表
统一取正。该系数位于首个共振之前；Step 3 的共振规范自由度不能把它消去。

式 (6)否定的是明确的候选身份。它不否定式 (3)，也不证明 $R_s$ 出现非实根。
非线性参数指数仍可能存在其他保根机制，但本轮没有获得其证明。

## Exact executable check

下面的精确片段先对抽象四阶 $v$ 直接反演 $Y$，再核对 Lagrange 式和
真实五分母的两个系数。没有根表或新增分母扫描。

```python
import sympy as S
t, y, a = S.symbols("t y a")
p1, p2, p3, p4 = S.symbols("p1 p2 p3 p4")
def cut(expr, var, n):
    return S.Add(*[c*var**p[0] for p,c in S.Poly(S.expand(expr),var).terms()
                   if p[0] <= n])
def expcut(v, var, n):
    return cut(sum(cut(v**j,var,n)/S.factorial(j)
                   for j in range(n+1)),var,n)
V = p1*t+p2*t**2+p3*t**3+p4*t**4
Y = cut(t*expcut(V,t,4),t,5)
T = y
for n in range(2,6):
    residual = cut(Y.subs(t,T),y,n)-y
    T = cut(T-S.expand(residual).coeff(y,n)*y**n,y,5)
z = cut(T/y-1,y,4)
w = -cut(sum((-1)**(j+1)*cut(z**j,y,4)/j for j in range(1,5)),y,4)
w4 = p4-4*p1*p3-2*p2**2+8*p1**2*p2-S.Rational(8,3)*p1**4
assert S.expand(w).coeff(y,4) == w4
left = S.expand(cut(Y+a*Y*Y,t,5)).coeff(t,5)
right = S.expand(cut((1+2*a*y)*expcut(5*w,y,4),y,4)).coeff(y,4)/5
assert S.expand(left-right) == 0
D1, D2, D3, D4 = S.symbols("D1 D2 D3 D4", nonzero=True)
v1 = 1/D1
v2 = (v1+a)/D2
v3 = (v2+v1*v1/2+2*a*v1)/D3
v4 = (v3+v1*v2+v1**3/6+a*(2*v2+2*v1*v1))/D4
lead = S.factor(S.expand(w4.subs({p1:v1,p2:v2,p3:v3,p4:v4})).coeff(a,2))
assert S.simplify(lead-2*(D2-D4)/(D2**2*D4)) == 0
lo, hi = (5-S.sqrt(5))/2, (5+S.sqrt(5))/2
assert S.simplify(lead.subs({D2:hi,D4:lo})-(S.sqrt(5)-1)/5) == 0
assert S.simplify(lead.subs({D2:lo,D4:hi})+(S.sqrt(5)+1)/5) == 0
print("EXACT_PASS: inverse identity and genuine sine affine-parameter obstruction")
```

## Corrections or missing assumptions

本轮没有发现原实际根命题的反例，也没有补出全实单根定理所缺的正性／
振荡引理。循环芽条件 (5)仍是一个非线性的有限射流可解性条件；它不自动
给出参数 $a$ 的实解数、重数或交错性。反函数表示中的参数非线性是实际
可核验的障碍，不能通过将系数同号改称“指数保根”略去。

## Open risks and handoff

原 $C$ 全分母根及重数分类保持 OPEN。全分母固定消失点后的非零 $Q$
亦不在本报告中解决。主控和其他作者的导数／次项留数身份若与 (3)共享
同一换元机制，不应作为彼此独立的新主结果重复计算。

本稿的新内容是一个规范完整的全分母循环芽／反函数规约，以及实际族对
指定参数仿射身份的精确否定；不是又一份旧 OPEN 的复述，也不是全问题完成。
没有修改冻结文件、批次 3/5、论文范围或科学验收要求。
