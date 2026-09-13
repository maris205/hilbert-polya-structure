# Proof Package：两因子矩阵 holonomy 的首次有界作者预筛

日期：2026-09-06。性质：新的 AUTHOR 数学预筛，不是独立终审、候选选择、
正式论文、Route 评价或产物验收。`route_applicability: NOT_APPLICABLE`。
本报告与已冻结的形式 gauge 候选 R1 是不同问题、不同角色的工作；未改旧 R1。

## Claim

令 $p\in\mathbb C[t]$ 的确切次数为 $d\ge2$，
$H_p(x,y)=(p(x)-y,x)$，$A=\mathbb C[x,y]$，$\sigma=H_p^*$。
对 $f,g\in\mathbb C[t]$ 定义

$$
U(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
L(b)=\begin{pmatrix}1&0\\b&1\end{pmatrix},\qquad
C(x,y)=U(f(x))L(g(y)).
$$

矩阵 cocycle 的乘积顺序固定为

$$
C_n=\sigma^{n-1}(C)\cdots\sigma(C)C.
$$

“完整周期恒等”意为对每个 $n\ge1$，$C_n=I_2$ 在
$\operatorname{Fix}(H_p^n)$ 的完整坐标环中成立，包含其非约化结构。
大问题是不限制 $f,g$ 次数时，该条件是否强迫 $f=0$ 或 $g=0$，
或是否有两者非零的真实多项式 gauge。**本报告不解决这个无界大问题。**

本轮证明以下有界结论，它包含所允许的二次后备合同，且用同一短证明覆盖任意 $d$。

**定理。** 假设 $\deg f,\deg g\le d$，置 $q(t)=p(t)-2t$。
下列条件等价：

1. 对所有 $n\ge1$，$C_n=I_2$ 在完整 $\operatorname{Fix}(H_p^n)$ 上成立。
2. 上述恒等只对 $n=1,2$ 成立。
3. 存在 $a,b\in\mathbb C$，满足
   $f=a q$、$g=b q$、$ab=0$。
4. 存在 $B\in SL_2(A)$，使 $C=\sigma(B)B^{-1}$。

第三项的非平凡解有显式 gauge：

$$
\begin{array}{ll}
b=0:& B=U(a(x-y)),\\[2mm]
a=0:& B=L(b(x+y-p(y))).
\end{array}
$$

当 $a=b=0$ 时可取 $B=I_2$。本报告不声称 gauge 唯一。
对每一个固定 $p$，只检验 $n=1$ 都不足以代替上述两个周期：
$f=g=q$ 通过一周期，但在完整二周期 scheme 上失败。

特别地，对 $p=t^2+c$、全部 $c\in\mathbb C$、$\deg f,\deg g\le2$，
完整分类就是

$$
(f,g)=(a(t^2-2t+c),0)
\quad\text{或}\quad
(f,g)=(0,b(t^2-2t+c)).
$$

## Status

有界定理及全部显示的退化／边界证书：**PROVABLE AS STATED**。
无需删除任何复参数、增加约化性假设或改变 holonomy 乘积顺序。

无界 $f,g$ 的第一大问题、以及任意 $C\in SL_2(A)$ 的一般
polynomial Livšic 充要命题：**NOT CURRENTLY JUSTIFIED / OPEN**。
本报告没有构造 $f,g$ 都非零且全周期恒等的 gauge。
闭合的是一个短的三角分类结果；据此作者预筛按范围停止，不授予新颖性或容量 PASS。

## Assumptions

- 基域为 $\mathbb C$，$d\ge2$，$p$ 首系数非零；不要求 monic、centered 或 generic。
- 有界定理只限制一元多项式 $f,g$ 的次数为至多 $d$，不限制待求 $B$ 的次数。
- 固定点和二周期均使用定义理想本身，不替换成根理想，不仅在几何点代值。
- $\sigma$ 逐项作用于矩阵，$\sigma(B)B^{-1}$ 与 $C_n$ 采用上面的左乘顺序。
- 任意一般 $SL_2$ cocycle 不属于本定理；对完整矩阵问题没有从受限乘积形式作推广。

## Notation

令 $I_n\subset A$ 由 $H_p^n$ 的两个坐标减去 $x,y$ 生成，
$R_n=A/I_n$。定义 $p(t)=\alpha t^d+\cdots$，$\alpha\ne0$。
下面 $a,b$ 专指 cocycle 的标量系数，$\alpha$ 是映射多项式首系数。
在 $R_2$ 中用

$$
\delta=2(y-x).
$$

矩阵 $I_2$ 表示单位矩阵；理想 $I_n$ 的含义始终由下标和上下文区分。

## Proof Strategy

先在一周期商环中读出 $q\mid f,g$；次数界使两个商成为标量。
二周期短环的重邻项给出 $p(x)=2y$、$p(y)=2x$，使 $H_p$ 精确交换 $x,y$。
于是二周期 holonomy 化为一个显式非交换乘积，其一个对角项检测 $ab\delta^2$。
关键是证明 $\delta^2$ 在每个完整二周期环中都非零，包括几何二周期坍缩时。
最后由显式单三角 gauge 及矩阵望远镜乘积证明全周期充分性。

## Dependency Map

1. 固定点定义理想给出 $R_1\simeq\mathbb C[t]/(p(t)-2t)$。
2. 二周期定义理想与一元消去给出一个参数无例外的 $d^2$ 维环及基。
3. 直接 $2\times2$ 矩阵乘法加上 $\delta^2\ne0$ 排除 $ab\ne0$。
4. 加法三角群的差分恒等式给出 $B$；一般 coboundary 的望远镜乘积给全周期恒等。

这些步骤下面全部证明，不需要一般矩阵 Livšic 定理、差分 Galois 定理或数值实验。
三角群化为加法共边界是继承的一般机制，不能算作新非交换理论。

## Proof

### Step 1. 完整一周期环强迫整除，不只是根集消失

固定点定义理想为

$$
I_1=(p(x)-y-x,\ x-y)=(x-y,\ p(x)-2x).
$$

因此 $R_1\simeq\mathbb C[t]/(q(t))$，且 $x=y=t$。
矩阵在此环中为

$$
C=\begin{pmatrix}1+f(t)g(t)&f(t)\\g(t)&1\end{pmatrix}.
$$

所以 $C=I_2$ 当且仅当 $f,g\in(q)$，即 $q\mid f$ 和 $q\mid g$。
由于 $\deg q=d$，有界合同给出 $f=a q$、$g=b q$，其中 $a,b$ 是复标量。
若某个多项式为零，相应标量为零；这一步不除以 $a$ 或 $b$。
即使 $q$ 有重根，此整除结论仍成立，因为用的是商环而不是点集。

### Step 2. 二周期理想确实保留两个相同邻项

直接计算

$$
H_p^2=(p(p(x)-y)-x,\ p(x)-y).
$$

第二坐标的固定方程给 $p(x)-2y=0$。第一坐标的固定方程为
$p(p(x)-y)-2x=0$；它与 $p(y)-2x$ 的差可被 $p(x)-2y$ 整除。
这是多项式恒等式 $p(u)-p(v)\in(u-v)$ 的应用，故理想精确相等：

$$
I_2=(p(x)-2y,\ p(y)-2x).
$$

此处的 $2y,2x$ 不能改成一个邻项。
在 $R_2$ 中，$H_p(x,y)=(y,x)$，故 $\sigma$ 精确交换这两个变量。

还需一个含所有退化参数的基事实。消去 $y$ 得

$$
R_2\simeq\mathbb C[x]/(F_p(x)),\qquad
F_p(t)=p(p(t)/2)-2t.
$$

$F_p$ 的确切次数为 $d^2$，首系数为 $\alpha^{d+1}/2^d\ne0$。
对 $0\le i,j<d$，$x^iy^j$ 在此一元表示中成为
$x^i(p(x)/2)^j$，其次数为 $i+dj$，首系数为 $(\alpha/2)^j$。
这些次数恰各一次遍历 $0,\ldots,d^2-1$，且首系数均非零。
与一元商环的幂基作三角换基即得

$$
\{x^iy^j:0\le i,j<d\}
\quad\text{是 }R_2\text{ 的一组基}. \tag{1}
$$

没有使用 $F_p$ 可分、$R_2$ 约化或特殊参数外的假设。

### Step 3. 平方差在每个完整二周期环中均非零

若 $d\ge3$，则 $x^2,y^2,xy$ 都是 (1) 中不同基元。
表达式

$$
\delta^2=4x^2+4y^2-8xy
$$

的 $xy$ 系数为 $-8\ne0$，故不为零。

若 $d=2$，写 $p(t)=\alpha t^2+\beta t+\gamma$。
由二周期关系，

$$
x^2=\frac{2y-\beta x-\gamma}{\alpha},\qquad
y^2=\frac{2x-\beta y-\gamma}{\alpha}.
$$

所以

$$
\delta^2=\frac{4(2-\beta)}{\alpha}(x+y)
          -\frac{8\gamma}{\alpha}-8xy. \tag{2}
$$

这里 $1,x,y,xy$ 是基，$xy$ 系数仍为 $-8$。
因而对于每一个允许的 $p$ 都有 $\delta^2\ne0$ 于 $R_2$。
这不表示 $\delta$ 非零因子；下一节的退化例中它就是幂零元。

### Step 4. 两因子 holonomy 的一个对角项排除同时非零

已经由 Step 1 得 $f=a q$、$g=b q$。在 $R_2$ 中，

$$
f(x)=2a(y-x)=a\delta=:u,\qquad
g(y)=2b(x-y)=-b\delta=:v.
$$

由变量交换，$\sigma f=-u$、$\sigma g=-v$。因此按规定乘积顺序，

$$
C_2=U(-u)L(-v)U(u)L(v)
=\begin{pmatrix}
1+uv+(uv)^2&u^2v\\
-uv^2&1-uv
\end{pmatrix}. \tag{3}
$$

式 (3) 由乘开两个矩阵
$\bigl(\begin{smallmatrix}1+uv&-u\\-v&1\end{smallmatrix}\bigr)$ 和
$\bigl(\begin{smallmatrix}1+uv&u\\v&1\end{smallmatrix}\bigr)$ 得到，
不将 $U(-u)L(-v)$ 误认成 $C^{-1}=L(-v)U(-u)$。
其 $(2,2)$ 项减去 $1$ 恰为

$$
-uv=ab\delta^2.
$$

若 $C_2=I_2$，则 $ab\delta^2=0$。由于 $ab$ 是复标量且 $\delta^2\ne0$，
得到 $ab=0$。在有幂零元的环中也成立，因为非零复标量仍可逆。
故条件 2 推出条件 3。

### Step 5. 显式三角 gauge 与全周期 scheme 恒等

置 $s=x-y$，有

$$
\sigma s-s=p(x)-2x=q(x).
$$

如果 $b=0$，取 $B=U(as)$，利用 $U(r)U(t)=U(r+t)$ 得
$\sigma(B)B^{-1}=U(aq(x))=C$。

置 $r=x+y-p(y)=\sigma^{-1}s$，则

$$
\sigma r=x-y,\qquad \sigma r-r=p(y)-2y=q(y).
$$

如果 $a=0$，取 $B=L(br)$，利用下三角的同一加法恒等式得到
$\sigma(B)B^{-1}=L(bq(y))=C$。
两个构造都在 $SL_2(A)$ 内，逆矩阵只需把三角参数取负。
于是条件 3 推出条件 4。

对任意多项式 $B\in SL_2(A)$，若 $C=\sigma(B)B^{-1}$，则非交换乘积依序望远镜消去：

$$
C_n=\sigma^n(B)B^{-1}.
$$

在 $R_n$ 中，任何多项式在 $H_p^n(x,y)$ 与 $(x,y)$ 的代入相等，
所以 $\sigma^n(B)=B$，从而 $C_n=I_2$。此等式发生在完整坐标环而非仅在点上。
故条件 4 推出条件 1；条件 1 推出条件 2 由量词直接成立，所有等价均已证明。
取 $a=b=1$ 时一周期成立而 Step 4 排除二周期，证明对每个固定 $p$ 的周期界尖锐性。$\square$

## Degenerate scheme certificate：二次参数 $c=-3$

此例说明完整 scheme 条件在有界定理中不能省略。
取 $p(t)=t^2-3$，$q(t)=(t-3)(t+1)$。
Step 2 的一元环为

$$
R_2\simeq\mathbb C[x]/((x-3)(x+1)^3),\qquad
y=(x^2-3)/2.
$$

其两个几何点均为固定点：$(3,3)$、$(-1,-1)$，所以 $\delta=0$ 在所有几何点上。
但是在完整环中 $\delta=q(x)$，并且

$$
\delta^2\equiv-4(x-3)(x+1)^2\ne0,\qquad \delta^3=0. \tag{4}
$$

非零性来自 (4) 的代表多项式次数为三，小于商模多项式次数四。
模理想同余由
$q(x)^2-(x-3)(x+1)^3=-4(x-3)(x+1)^2$
直接验证；$q^3$ 则被模多项式整除。

对 $f=a q$、$g=b q$，式 (3) 在此环约化为

$$
C_2-I_2=ab\delta^2\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$

当 $ab\ne0$ 时，它在所有几何点上为零但在完整 scheme 上非零。
因此若只检验约化点，恰会漏掉这一参数；本报告没有将它删去。

## Unbounded-degree boundary：两周期不能无条件外推

任取允许的 $p$，设

$$
f(t)=g(t)=F_p(t)=p(p(t)/2)-2t.
$$

两者均非零且次数为 $d^2>d$。在 $R_2$ 中有
$F_p(x)=F_p(y)=0$，故 $C=I_2$、$C_2=I_2$。
在 $R_1$ 中也有 $F_p(t)=0$：模 $q$ 时 $p(t)/2=t$，从而 $F_p(t)=q(t)=0$。
所以这个两者非零的例子通过完整一、二周期 scheme 检验。

这里只证明前两个周期通过；**没有证明所有周期通过，也没有构造其 polynomial gauge**。
它不是无界主问题的反例，而是对错误外推的明确阻止：
离开 $\deg f,\deg g\le d$ 后，本报告的二周期判据不能直接继续强迫 $f=0$ 或 $g=0$。
无界情形中，一周期只给 $f=q r$、$g=q s$；商 $r,s$ 不再是标量，
Step 4 的简单标量可逆性论证也不再适用。

## Corrections or Missing Assumptions

- 原 lead 的一周期整除判断正确，且必须解释为完整 $q$ 整除，而非只除去其平方自由部分。
- 二周期的系数 $2$ 正确；在所指定的乘积顺序下，检测项为 $ab[2(y-x)]^2$。
- 上三角 gauge $U(x-y)$ 的方向正确；下三角对应的是 $L(x+y-p(y))$，不是未经检查的同一个势函数。
- 有界后备合同不需要数学修复；其全 $c$ 结论由更一般的确切次数 $d$ 证明直接包含。
- 不额外声称一般矩阵问题已解，不把幺幂加法化或过去的 companion／差分 Galois 结果当作本轮新机制。

## Actual Verification

本轮重新完整读取了 `AGENTS.md`、`docs/WORKFLOW.md` 与
`/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md`，按该技能核对精确主张、
假设、依赖、退化情况及未证范围。证明使用上文显示的理想恒等式、
一元三角换基、矩阵乘法和望远镜消去，没有执行符号脚本或数值实验。

本轮唯一写入为本文件，使用 `apply_patch`。未修改先前 R1、作者输入或已接受产物；
未子委派、未建项目／正文／构建、未编译、未外部写入、未查新评分。
这是一份作者论证，尚未经 fresh 独立数学终审；本文件不自行授予该状态。

## Open Risks and Author Stop

有界定理没有尚待修补的证明步骤；全参数及 scheme 边界已经显式处理。
无界两因子分类的剩余义务是控制任意多项式商 $r,s$ 的所有周期乘积，
或给出两者非零的全周期 gauge；本报告没有完成其中任一项。
任意 $SL_2(A)$ cocycle 的一般充要性还更强，不能从本分类推出。

本轮所得是短的三角分类及一个必要的非约化边界证书。
按授权范围在此诚实停止：**有界数学结论 PROVABLE AS STATED；
无界问题 OPEN；无新颖性 PASS、无长文容量 PASS、无候选立项。**
最终文件行数与 SHA256 在写入后的交付消息中另报，不在文件内作自引用哈希。
