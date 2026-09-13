# Paper30 有界证明入口：qPI 谱曲线的循环商、判别式与亏格

日期：2026-09-08。作者侧独立数学入口，不是正式候选审稿、查新票或 Route 评价。
仅新增本文件；不修改主控的辛形式／边界计算或另一作者的正规丛计算。

## Claim

设 $k$ 是域，$r\geq1$，$s\in k^\times$ 的乘法阶恰为 $r$，
$\operatorname{char}k\nmid r$，$t\in k^\times$，$c\in k$。记

$$
T=t^r\ne0,\qquad \varepsilon=(-1)^{r+1},\qquad
A(Z)=Z^2+cZ+T.
$$

考虑仿射谱曲线

$$
C_r^{\mathrm{aff}}:
\lambda^2-A(z^r)\lambda+\varepsilon z^{3r}=0.
$$

下列结论成立。

1. 作用 $\sigma(z,\lambda)=(sz,\lambda)$ 的仿射商为
   $$
   E^{\mathrm{aff}}:
   \lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0,
   \qquad Z=z^r.
   $$
   商映射是有限平坦的，秩为 $r$；此项不需排除特征二。
2. 若 $\operatorname{char}k\ne2$，置 $W=2\lambda-A(Z)$，则商曲线等价于
   $$
   W^2=f(Z),\qquad
   f(Z)=A(Z)^2-4\varepsilon Z^3
   =Z^4+(2c-4\varepsilon)Z^3+(c^2+2T)Z^2+2cTZ+T^2.
   $$
   采用单首多项式判别式 $\operatorname{Disc}f=\prod_{i<j}(\alpha_i-\alpha_j)^2$
   的约定，有精确恒等式
   $$
   \operatorname{Disc}_Z f=256\varepsilon^2T^3D_\varepsilon(c,T),
   $$
   其中
   $$
   D_\varepsilon(c,T)
   =c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27\varepsilon^2T.
   $$
   对本题 $\varepsilon^2=1$，这个 $D_\varepsilon$ 逐项等于 JR 的式 (3.13)。
3. 在 $T\ne0$、$\operatorname{char}k\ne2$ 下，
   $E^{\mathrm{aff}}$ 的几何奇点存在，当且仅当 $D_\varepsilon(c,T)=0$。
   在另有 $\operatorname{char}k\nmid r$ 时，原仿射谱曲线的奇点存在条件相同。
4. 在 $\operatorname{char}k\ne2$ 下，若 $D_\varepsilon(c,T)\ne0$，
   则下面明确构造的光滑射影完备化满足
   $$
   g(\overline E)=1,\qquad g(\overline C_r)=2r-1,
   \qquad \overline C_r/\mu_r\cong\overline E.
   $$
   商映射是次数 $r$ 的可分 Kummer 覆盖，仅在 $\overline E$ 上
   $Z=0$ 的两个点及 $Z=\infty$ 的两个点处全分歧。
   当 $r=1$ 时映射为恒等映射，这四点的分歧指数均为 $1$，不称为分歧点。

本命题没有涉及动力学纤维 $\{I_r(x,y)=c\}$ 与上述任一谱曲线之间的同构、
双有理对应或 Jacobian 同一性。

## Status

`PROVABLE AS STATED`，限于上述逐项列明的范围。
几何亏格结论的光滑参数条件是 $D_\varepsilon(c,T)\ne0$；
特征二的平方配方法及亏格延伸不在本证明的结论内。

## Assumptions and notation

- 几何不可约性、几何奇点、分歧点数及几何亏格均在代数闭包 $\bar k$ 上核对。
  方程、商映射和所列特殊点本身在 $k$ 上定义。
- $E^{\mathrm{aff}}$ 与 $C_r^{\mathrm{aff}}$ 是指定的仿射方程；
  $\overline E$ 与 $\overline C_r$ 是下文双覆盖坐标图给出的光滑射影曲线，
  不指任意未经解奇的平面射影闭包。
- $\mu_r=\langle s\rangle$ 在本题是分裂的循环群；特征不整除 $r$。
- 计算判别式时暂把 $\varepsilon$ 作为形式变量，所得整数系数恒等式随后代入
  $\varepsilon=(-1)^{r+1}$。这样不隐藏约去因子或小特征问题。
- $\operatorname{Res}(a,b)$ 表示多项式结式；当 $a$ 单首时等于对 $a$ 的全部根
  （含重数）取 $b$ 值之积。

## Source scope and prior deduction

实际读取 Joshi–Roffelsen，*Arithmetic dynamics of a discrete Painlevé equation*，
[arXiv:2508.18578v2，2026-01-16](https://arxiv.org/html/2508.18578v2)：
§3.2 全节，另定向读取 §3.1 Theorem 3.1、Remarks 3.2–3.5、式 (3.6)–(3.11)
及相应迹恒等式推导。谱方程和奇点参数四次式均已在 JR §3.2 提出。
本件的商曲线／分歧计算是为限定对象与检验桥接缺口，不能把已知谱判别式算作新突破。

Riemann–Hurwitz 使用
[Stacks Project §53.12](https://stacks.math.columbia.edu/tag/0C1B)
的可分公式及 tame 情形的不同指数 $e-1$；实际读取了该节公式推导及
Lemmas 53.12.1–53.12.4 的陈述和证明。下文逐次核对可分性、光滑性及 tame 条件。

## Proof Strategy

先直接计算不变量环，不先假定谱曲线不可约。随后配平方并手工分解结式，得到
精确判别式与奇点条件。对非判别式参数，用两个坐标图构造完备化并计算四次双覆盖
的亏格。最后由 $z^r=Z$ 的 Kummer 扩张逐点计算分歧，再作 Riemann–Hurwitz。

## Dependency Map

1. 仿射商：单首二次关系给出的唯一余式表示，以及 $s$ 的精确阶。
2. 奇点条件：$2$ 可逆、$T\ne0$、雅可比判据及结式恒等式。
3. 商的亏格：四次多项式平方自由、无穷远两个光滑点、次数二 tame 双覆盖。
4. 原谱曲线亏格与射影商：$Z$ 在四个点处的赋值为 $\pm1$、
   Eisenstein 不可约性、$r$ 可逆，以及 tame Riemann–Hurwitz。
5. 动力学纤维桥接：不属于上述依赖链，没有从本命题获得证明。

## Proof

### Step 1. 仿射不变量环与商映射

令

$$
B=k[Z,\lambda]/(\lambda^2-A(Z)\lambda+\varepsilon Z^3),
\quad
R_r=k[z,\lambda]/(\lambda^2-A(z^r)\lambda+\varepsilon z^{3r}).
$$

因为关系关于 $\lambda$ 单首二次，$R_r$ 的每个元素恰有一种表示
$a(z)+b(z)\lambda$，其中 $a,b\in k[z]$。若该元素被 $\sigma$ 固定，
唯一性迫使 $a(sz)=a(z)$ 与 $b(sz)=b(z)$。
比较 $z^j$ 的系数，而 $s^j=1$ 当且仅当 $r\mid j$，可知
$a,b\in k[z^r]$。反向包含由作用公式直接成立。因此

$$
R_r^{\mu_r}=B,\qquad Z\longmapsto z^r.
$$

这里的 $B\hookrightarrow R_r$ 是单射：两个关于 $\lambda$ 次数小于二的余式
若代入 $Z=z^r$ 后相同，其各个多项式系数已经相同。
此外

$$
R_r\cong B[z]/(z^r-Z)
$$

作为 $B$-代数，故 $1,z,\ldots,z^{r-1}$ 构成 $B$-基。
这证明不变量环意义的仿射商以及有限平坦、秩 $r$ 的结论。
本步没有使用 $2$ 可逆或光滑性。

### Step 2. 配平方与准确的奇点条件

从本步起假设 $\operatorname{char}k\ne2$。
代换 $W=2\lambda-A(Z)$ 的逆是 $\lambda=(W+A(Z))/2$，故为仿射坐标变换，
将商方程化为 $W^2=f(Z)$。
其几何奇点恰好满足

$$
W=0,\qquad f(Z)=0,\qquad f'(Z)=0.
\tag{2.1}
$$

$f(0)=T^2\ne0$，故这样的 $Z$ 不为零。又 $f(Z)=0$ 意味着
$A(Z)^2=4\varepsilon Z^3\ne0$，所以 $A(Z)\ne0$。
设

$$
Q(Z)=Z^2-cZ-3T.
$$

直接微分并消去三次项，得到恒等式

$$
Zf'(Z)-3f(Z)=A(Z)Q(Z).
\tag{2.2}
$$

由 $Z,A(Z)\ne0$ 可知，在 $f(Z)=0$ 上，$f'(Z)=0$ 等价于 $Q(Z)=0$。
所以几何奇点还可准确写为

$$
Z=\alpha\ne0,\quad
Q(\alpha)=f(\alpha)=0,\quad
\lambda=A(\alpha)/2.
\tag{2.3}
$$

此推导没有除以 $3$。

### Step 3. 手工结式分解与判别式

本步在整数系数形式变量环中计算。由于 $f$ 单首四次，
$\operatorname{Disc}_Z f=\operatorname{Res}(f,f')$。由 (2.2)、结式的乘法性及
在第二项中加 $f$ 的倍数不改变结式，有

$$
T^2\operatorname{Disc}_Z f
=\operatorname{Res}(f,Zf')
=\operatorname{Res}(f,AQ)
=\operatorname{Res}(f,A)\operatorname{Res}(f,Q).
\tag{3.1}
$$

若 $\beta_1,\beta_2$ 是 $A$ 的两个形式根，含重数，则
$f(\beta_i)=-4\varepsilon\beta_i^3$，且 $\beta_1\beta_2=T$。
交换两个结式参数的符号为 $(-1)^{4\cdot2}=1$，于是

$$
\operatorname{Res}(f,A)=16\varepsilon^2T^3.
\tag{3.2}
$$

模 $Q$ 有 $Z^2=cZ+3T$，从而 $A(Z)=2cZ+4T$。因此

$$
f(Z)\equiv4B_0(Z)\pmod Q,
\qquad B_0(Z)=(cZ+2T)^2-\varepsilon Z^3.
$$

再将 $B_0$ 除以 $Q$，其余式为 $aZ+b$，其中

$$
a=c(c^2+4T)-\varepsilon(c^2+3T),\qquad
b=T(3c^2+4T-3\varepsilon c).
$$

$Q$ 两根之和是 $c$、乘积是 $-3T$，故

$$
\operatorname{Res}(Q,B_0)=b^2+cab-3Ta^2.
$$

为明确核对展开常数，将右侧按 $\varepsilon$ 次数收集：

| 次数 | 系数 |
| --- | --- |
| $\varepsilon^0$ | $T^2(c^2-4T)^2$ |
| $\varepsilon^1$ | $T^2c(36T-c^2)$ |
| $\varepsilon^2$ | $-27T^3$ |

这些系数由上式的 $a,b$ 直接相乘得到，因而

$$
\operatorname{Res}(Q,B_0)=T^2D_\varepsilon(c,T),\qquad
\operatorname{Res}(f,Q)=16T^2D_\varepsilon(c,T).
\tag{3.3}
$$

把 (3.2)–(3.3) 代入 (3.1)，在整环中约去 $T^2$，得到整数多项式恒等式

$$
\boxed{\operatorname{Disc}_Z f
=256\varepsilon^2T^3
\bigl(c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27\varepsilon^2T\bigr).}
\tag{3.4}
$$

整数多项式恒等式可约化到任意特征；在本题的非二特征、$T\ne0$ 下，
前面的 $256\varepsilon^2T^3$ 是非零元。因此 $f$ 有重根当且仅当
$D_\varepsilon(c,T)=0$。结合 (2.1)，证明了商的准确奇点参数条件。

对于原谱曲线，令 $w=2\lambda-A(z^r)$，方程为

$$
w^2=f(z^r).
\tag{3.5}
$$

其在 $z=0$ 的两个点有 $w=\pm T\ne0$，故光滑。在 $z\ne0$ 上，

$$
\frac{d}{dz}f(z^r)=rz^{r-1}f'(z^r),
$$

其中 $rz^{r-1}\ne0$。所以一个原谱奇点等价于 $z^r$ 是 $f$ 的重根。
在 $\bar k$ 中，每个非零重根有恰好 $r$ 个不同的 $r$ 次根，给出其全部提升。

还可记录与原方程有关的精确判别式，而非仅记录其零点集：

$$
\operatorname{Disc}_z f(z^r)
=r^{4r}T^{2r-2}\bigl(\operatorname{Disc}_Z f\bigr)^r
=256^r r^{4r}\varepsilon^{2r}T^{5r-2}D_\varepsilon(c,T)^r.
\tag{3.6}
$$

证明是在 $f(z^r)$ 的 $4r$ 个形式根上取导数值之积：导数中常数 $r$ 贡献
$r^{4r}$，$z^{r-1}$ 贡献 $T^{2r-2}$，而每个 $f$ 的根出现 $r$ 次，
使 $f'$ 的贡献为 $(\operatorname{Disc}_Z f)^r$。
次数 $4r$ 的判别式符号 $(-1)^{4r(4r-1)/2}$ 等于 $1$。
这亦可先在泛参数平方自由情形求得，再由多项式恒等式延伸。

### Step 4. 与 JR 四次式的关系

代回 $\varepsilon=(-1)^{r+1}$，有 $-\varepsilon=(-1)^r$、$\varepsilon^2=1$。
故

$$
D_\varepsilon(c,t^r)
=c^4+(-1)^rc^3-8t^rc^2-(-1)^r36t^rc+16t^{2r}-27t^r.
\tag{4.1}
$$

这正是 [JR §3.2 式 (3.13)](https://arxiv.org/html/2508.18578v2#S3.SS2)。
JR 已将该式联系到谱方程奇点；本件补明结式因子、循环商和亏格对象，
不将式 (4.1) 或这个奇点参数集合声称为首次发现。

### Step 5. 商曲线的光滑完备化与亏格一

现在固定 $D_\varepsilon(c,T)\ne0$。
$f$ 的四个根在 $\bar k$ 中互异且均非零，故 $f$ 不是 $\bar k(Z)$ 中的平方，
$W^2=f(Z)$ 几何不可约。其仿射部分由 Step 2 光滑。

无穷远使用坐标

$$
u=Z^{-1},\qquad V=W/Z^2.
$$

对应方程是

$$
V^2=(1+cu+Tu^2)^2-4\varepsilon u.
\tag{5.1}
$$

在 $u=0$ 有两个不同的 $k$-点
$P_{\infty,+}=(0,1)$ 和 $P_{\infty,-}=(0,-1)$。
方程对 $V$ 的偏导分别为 $2$ 和 $-2$，均非零；所以这两个点光滑，
$u$ 各为一个局部参数。
在两个图的重叠部分按上述代换粘合，得到有限映射
$\overline E\to\mathbb P^1_Z$，故所得曲线射影且完备。

这个次数二覆盖可分，因为特征不为二。四个简单根是全部分歧点：
在一个简单根 $\alpha$ 处，方程形如 $W^2=(Z-\alpha)h(Z)$，
$h(\alpha)\ne0$，所以分歧指数为 $2$；在无穷远及其余点则不分歧。
在 $\bar k$ 上所有剩余域次数均为 $1$，四个分歧点均为 tame。
Riemann–Hurwitz 因而给出

$$
2g(\overline E)-2=2(-2)+4(2-1)=0.
$$

故 $g(\overline E)=1$。
例如 $Z=0$ 时的点 $(Z,\lambda)=(0,0)$ 是 $k$-有理点，
选择它为零元后，$\overline E$ 是 $k$ 上的椭圆曲线。
这个零元选择不来自或规定任何动力学纤维上的平移结构。

### Step 6. Kummer 覆盖：次数、全部分歧与射影商

$\overline E$ 在 $Z=0$ 上另有两个不同的点

$$
P_{0,+}=(Z,W)=(0,T),\qquad P_{0,-}=(0,-T).
$$

因为 $2W\ne0$，$Z$ 在两点处均为局部参数。结合 Step 5 的无穷远图，有

$$
\operatorname{div}_{\overline E}(Z)
=P_{0,+}+P_{0,-}-P_{\infty,+}-P_{\infty,-}.
\tag{6.1}
$$

不存在其他零点或极点，因为 $Z$ 是到 $\mathbb P^1_Z$ 的坐标函数。

在 $k(\overline E)$ 中添入满足 $z^r=Z$ 的元素 $z$。
当 $r>1$ 时，$X^r-Z$ 在点 $P_{0,+}$ 的离散赋值环上满足 Eisenstein 判据：
常数项赋值为 $1$，其余非首项系数为零。因此它在函数域中不可约，扩张次数恰为 $r$。
其导数是 $rX^{r-1}$，所以扩张可分。$r=1$ 时这些次数和可分性结论直接成立。

下面在 $\bar k$ 上逐点检查覆盖。

- 在 $P_{0,+}$、$P_{0,-}$，$Z$ 的赋值是 $1$。
  Eisenstein 扩张各只有一个上方点，分歧指数为 $r$。
- 在 $P_{\infty,+}$、$P_{\infty,-}$，改用 $z^{-1}$ 满足
  $(z^{-1})^r=Z^{-1}$；右端赋值为 $1$，故各有一个上方点，分歧指数为 $r$。
- 在其余点，$Z$ 是单位。有限代数 $\mathcal O[X]/(X^r-Z)$ 中 $X$ 是单位，
  导数 $rX^{r-1}$ 是单位，故此代数是有限 étale；取归一化不会增加分歧。
  等价地，在 $\bar k$ 的完备局部环中，其非零剩余值有 $r$ 个不同的根，
  分别由 Hensel 引理提升。

以上分歧全部 tame，因为特征不整除 $r$。
当 $r>1$ 时，这给出了全部四个分歧位置，而非只计算仿射部分的两个位置；
当 $r=1$ 时没有分歧。

为了明确此函数域的光滑射影模型，先使用 (3.5)，再在无穷远使用

$$
v=z^{-1},\qquad w_\infty=w/z^{2r},\qquad
w_\infty^2=(1+cv^r+Tv^{2r})^2-4\varepsilon v^r.
\tag{6.2}
$$

$f(z^r)$ 有 $4r$ 个不同的非零根：每个 $f$ 的根有 $r$ 个不同的提升，
提升后的导数不为零。故仿射图光滑且几何不可约。
在 $v=0$ 时 $w_\infty=\pm1$，对 $w_\infty$ 的偏导非零；这两个无穷远点也光滑。
粘合所得即 $\overline C_r$。

商映射在有限图上是 $(z,w)\mapsto(z^r,w)$，在无穷远图上是
$(v,w_\infty)\mapsto(v^r,w_\infty)$，故延伸为射影曲线的有限映射。
由于 $s$ 的精确阶为 $r$，变换 $z\mapsto sz$ 给出全部 $r$ 个不同的 Kummer
自同构，固定函数域恰为 $k(\overline E)$。
其射影曲线商因此为 $\overline E$；上面的两图也直接给出了这个商。

### Step 7. 原谱曲线的几何亏格

对 $\overline C_r\to\overline E$ 使用
[tame Riemann–Hurwitz](https://stacks.math.columbia.edu/tag/0C1B)：
两曲线光滑射影且几何不可约，映射可分、次数 $r$，四处不同指数为 $r-1$。
因此

$$
2g(\overline C_r)-2
=r\bigl(2g(\overline E)-2\bigr)+4(r-1)=4r-4,
$$

从而

$$
\boxed{g(\overline C_r)=2r-1.}
$$

作为同一计算的边界核对，(3.5) 到 $\mathbb P^1_z$ 的次数二映射恰有
$4r$ 个简单分歧点，两个无穷远点不分歧，亦给出
$2g-2=-4+4r$。当 $r=1$ 时原谱曲线就是商曲线，亏格为 $1$；
当 $r>1$ 时原谱曲线不是亏格一曲线。$\square$

## Corrections or Missing Assumptions

### 小特征与退化参数边界

1. 特征三不需要额外排除，只要 $3\nmid r$。
   前述证明没有除以 $3$，两个覆盖的分歧指数为 $2$ 和 $r$，仍为 tame。
   此时参数判别式简化为
   $$
   D_\varepsilon(c,T)=(T-c^2)^2-\varepsilon c^3.
   $$
   若它为零，(2.3) 中 $Q(Z)=Z(Z-c)$，故唯一可能的奇点横坐标是 $Z=c$；
   $T\ne0$ 迫使 $c\ne0$。这足以检查奇点判据，未开展退化纤维的全面分类。
2. 特征二下 Step 1 的仿射商仍有效，但 $W=2\lambda-A(Z)$ 不可逆，
   四次式成为平方，$256$ 也变成零。本文件不以四次判别式判断其光滑性或亏格；
   需要另用二次方程的 Artin–Schreier 型局部分析，未在此执行。
3. $T=0$ 明确排除；它会使 $Z=0$ 上两个点合并，破坏 (6.1) 与四点 Kummer 分歧计算。
4. $\operatorname{char}k\mid r$ 明确排除；在域中本就不存在该特征倍数精确阶的
   乘法根 $s$，也不能用可分 Kummer 或 tame Riemann–Hurwitz。
5. $D_\varepsilon=0$ 时，本文件已给出准确的仿射奇点条件，但不保留
   $g(\overline C_r)=2r-1$ 的光滑参数结论，也不在此分类其归一化分支或退化类型。
6. “奇点当且仅当判别式为零”针对所列仿射曲线及其自然双覆盖图。
   不应套用于未经处理的普通平面射影闭包；后者可因坐标嵌入在无穷远产生固定奇点。

## Open Risks and the dynamical-fibre gap

本件的谱曲线命题在明列假设下没有剩余证明步骤；但它没有关闭下列动力学问题。

- 参数相同的动力学纤维 $F_{c,t}=\{(x,y)\in X_{t,s}:I_r(x,y)=c\}$
  并未被构造出到 $\overline E$ 的有理映射，更没有证明次数为一。
- 迹和行列式固定只给出特征多项式；它们不自动证明矩阵模空间或等谱集合
  与某个 Jacobian 的同构。若引入谱线丛，还需证明其定义、下降、逆重建和泛单射性。
- $g(\overline C_r)=2r-1$ 说明不能把原 $z$-谱曲线直接叫作该动力纤维的椭圆曲线。
  取循环商得到亏格一，也不意味着动力纤维恰好等于这个商。
- 相同的坏参数四次式不能代替以上对应。即使另行证明动力纤维亏格一，
  也还需一个具体几何对应才能识别其 Jacobian；本文件不宣称它与 $\overline E$ 相同。
- 因此本件不证明 JR Conjecture 3.6 的全阶动力学纤维结论，不推出有限域轨道
  Hasse 上界或轨道平移定律，也不为 Paper30 预支新意、篇幅或立项资格。

## Verification record

完成有限符号恒等式核对：用 SymPy 对 $f(Z)$ 求判别式，
结果与 (3.4) 一致；又将 $b^2+cab-3Ta^2$ 按 $\varepsilon$ 收集，
得到 Step 3 表中的三个系数，并核对特征三的约化。
写入后另以断言核对 (2.2) 与 (3.4)，均通过。
这是对手工恒等式的附加检查，不替代上述结式证明；未作数值扫描或实验。

按 `proof-writer` 的要求，显式区分了原方程、商方程、完备化、几何亏格与待证桥接。
无稿件、页数测试、正式评分、Route 评价、项目创建或外部写操作。
