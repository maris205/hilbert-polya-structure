# R10 E2：全层湮灭理想的独立完整数学审查

2026-09-10 UTC。当前模型、proof-writer、非作者内部审查。
本文件只裁决指定辅助定理的数学正确性，不作论文准入判断。

## 1. Claim：实际稿件、参数与准确目标

已全文读取作者
[REPORT.md](../../a1_annihilator_ideal/REPORT.md)，共 $455$ 行。
本次审查绑定 SHA-256：

3e53c02f8315cfd957be1c235609b3f2fd3292103b7bd8b31aa98b81f69b835e

取任意奇素数 $p$、$k=\overline{\mathbb F}_p$、$c\in k$，
$f(x)=x^2+c$，及完整约分 norm-one 函数

$$
w=\eta A/B,\qquad
\eta\in\{1,-1\},\qquad B(X)=(-1)^mA(-X),
$$

其中 $A,B$ 首一、互素，次数为 $m\ge0$。
此处 $A(0)B(0)\ne0$ 自动成立：若其中一个为零，反射关系使
另一个也为零，从而与互素性矛盾。没有隐含删除任何根重数。

定义

$$
\begin{aligned}
F_n(x)&=f^{\circ n}(x)-x,\\
H_n(x)&=\eta^n\prod_{i=0}^{n-1}A(f^{\circ i}(x))
             -\prod_{i=0}^{n-1}B(f^{\circ i}(x)),\\
I_w&=\{S\in k[x]: F_n\mid S F_n'H_n
                    \text{ 对每个整数 }n\ge1\}.
\end{aligned}
\tag{R1}
$$

每个周期都是 $f$ 的普通原生周期，包括 $p$ 的倍数周期。
再记

$$
b=m+2,\qquad D=4b^2,\qquad N=5D+1,
$$

以及首一多项式

$$
S_*=\prod_{r=1}^{D}F_r,\qquad
q_n=\frac{F_n}{\gcd(F_n,F_n'H_n)},\qquad
L_N=\operatorname{lcm}(q_1,\ldots,q_N).
\tag{R2}
$$

准确目标是：若 $I_w\ne0$，其首一生成元的每个根的最小周期
至多为 $D$，故 $S_*\in I_w$，并且

$$
\deg S_*=2^{D+1}-2,\qquad
I_w=
\begin{cases}
(L_N),&L_N\mid S_*,\\
(0),&L_N\nmid S_*.
\end{cases}
\tag{R3}
$$

这里没有断言全部可见点的总数至多为 $D$。

## 2. Status

**PROVABLE AS STATED：作者 Theorem 1.1 全部三项及所述
有限测试、模解释均通过。**

开放数学必改项为零，开放 provenance 必改项为零。
本次没有要求作者改稿；以下重构验证的是原 $455$ 行版本，
不依赖尚未写出的修补或附加假设。

更强的非恒定 norm-one 全分离
$I_w=(0)$ 仍未证明。(CP) 的逆推、一般 MS6 和论文准入
均不属于这个 PASS 的结论。

## 3. Assumptions、Notation、Strategy 与依赖

根重数 $e_n(a)=\operatorname{ord}_aF_n$、次数、矩阵维数、
词长及同余参数均为普通整数。只有在 $e_n(a)H_n(a)$ 等
域元素表达式中，整数重数才映入 $k$。
记

$$
B_n=\{a\in k:F_n(a)=0,\ e_n(a)H_n(a)\ne0\text{ in }k\},
\qquad \mathcal B=\bigcup_{n\ge1}B_n.
\tag{R4}
$$

证明链为：

1. 局部根重数给出平方自由 $q_n$、理想和有限可见集的等价。
2. $F_n'/F_n$ 的精确对数导数给出带重数系数张量。
3. R9 的 $S=1$ 矩阵给出张量分割秩的统一上界 $D$。
4. 两侧完整二进制单项式基和插值给出足够长时的下界 $|B_n|$。
5. 每个已可见周期在任意长的某些返回层持续可见，故其原生
   长度不超过 $D$。
6. 得到明确的 $S_*$ 后，才能调用 R9 固定多项式有限词定理，
   消除未知次数并证明 (R3)。

R9 在这里提供两个已经证明的接口，而不是新的存在假设：
固定非零 $S$ 的检测界为

$$
k_S+16(m+2)^2=k_S+4D,\qquad
k_S=
\begin{cases}
0,&\deg S=0,\\
\lfloor\log_2\deg S\rfloor+1,&\deg S\ge1,
\end{cases}
\tag{R5}
$$

以及下面使用的四块系数矩阵。两者都适用于全部当前参数，
包括 $n=1,2$、$c=0$、$m=0$、常数 $S$ 和非约化返回代数。

## 4. Proof：完整数学重构

### Step 1. 局部除法精确给出 radical ideal

设 $a$ 是 $F_n$ 的根，写 $F_n=(x-a)^eG$，$G(a)\ne0$。
若 $p\nmid e$，则

$$
F_n'=e(x-a)^{e-1}G+(x-a)^eG'
$$

的首项不消失，所以其阶数恰为 $e-1$。
若 $p\mid e$，第一项消失，阶数至少为 $e$。
于是 $q_n$ 在 $a$ 处的指数是：

- 当 $p\nmid e$ 且 $H_n(a)\ne0$ 时为一；
- 当 $p\mid e$ 或 $H_n(a)=0$ 时为零。

这证明 $q_n$ 首一、平方自由，根集恰为 (R4) 的 $B_n$。
若 $H_n$ 为零多项式，按 $\gcd(F_n,0)=F_n$ 得到 $q_n=1$，
同样适用。局部指数还直接给出，对每个 $S$，

$$
F_n\mid S F_n'H_n\quad\Longleftrightarrow\quad q_n\mid S.
\tag{R6}
$$

因此

$$
I_w=\bigcap_{n\ge1}(q_n).
$$

若 $\mathcal B$ 无限，非零多项式不可能在全部这些不同点消失，
故 $I_w=(0)$。若 $\mathcal B$ 有限，令

$$
Q_{\mathcal B}=\prod_{a\in\mathcal B}(x-a),
$$

空乘积为一。(R6) 给出 $I_w=(Q_{\mathcal B})$。
这同时证明 $I_w\ne0$ 当且仅当 $\mathcal B$ 有限，且理想
是 radical 的；当 $I_w=(0)$ 时，$k[x]$ 为整环也给出 radical。
这里只使用有限点集上的多项式消失，不使用下降链稳定性。

### Step 2. $B_n$ 的整周期不变性

每个 $F_n$ 的根都是最小周期整除 $n$ 的普通周期点。
沿该周期移动起点只对 $n$ 个因子作循环置换，因此
$H_n(f(a))=H_n(a)$，即使因子取值为零也成立。

若这个周期经过 $0$，$f^{\circ n}$ 的导数在周期每一点都是零，
所以 $F_n'$ 在这些点均为 $-1$，各根重数均为一。
若周期不经过 $0$，每一点的 $f$ 局部次数都是一，
因为奇特征下 $2a\ne0$。由交换迭代和平方差得

$$
\begin{aligned}
F_n(f(x))
&=f(f^{\circ n}(x))-f(x)\\
&=F_n(x)\bigl(2x+F_n(x)\bigr).
\end{aligned}
\tag{R7}
$$

在 $a$ 处，左侧阶数为 $e_n(f(a))$，右侧阶数为 $e_n(a)$，
因为第二因子取值为 $2a\ne0$。所以根重数也沿周期相同。
由此 $B_n$ 是完整周期的并，$f$ 及每个 $f^{\circ h}$
在该有限点集上都是置换。没有把二次多项式在整个 $k$
上误当成单射。

### Step 3. 顶系数恒等式保留正确的重数

在 R9 的同构

$$
\mathcal A_n\simeq k[x]/(F_n),\qquad X_i\mapsto f^{\circ i}(x)
$$

下，$L_n$ 是次数低于 $2^n$ 的余式的顶次系数。
对任意多项式 $J$，若 $J=QF_n+T$、$\deg T<2^n$，则

$$
[x^{-1}]_\infty\,J/F_n=[x^{2^n-1}]T=L_n(J).
\tag{R8}
$$

这里 $[x^{-1}]_\infty$ 只是按 $x$ 的负幂展开的系数，
不是取带额外负号的微分留数。因为 $F_n$ 首一，其倒数以
$x^{-2^n}$ 起首，只有 $T$ 的顶项能产生 $x^{-1}$。

精确因式分解的微分给出

$$
\frac{F_n'}{F_n}
=\sum_{F_n(a)=0}\frac{e_n(a)}{x-a},
\tag{R9}
$$

求和取不同根；式中 $e_n(a)$ 是它在 $k$ 中的像。
对任意多项式 $R$，把 $H_nR$ 除以 $x-a$，余数为
$H_n(a)R(a)$。结合 (R8)–(R9) 得

$$
L_n(F_n'H_nR)
=\sum_{F_n(a)=0}e_n(a)H_n(a)R(a).
\tag{R10}
$$

所以二进制词张量

$$
\mathcal T_n(\epsilon)
=L_n\left(F_n'H_n\prod_iX_i^{\epsilon_i}\right)
$$

确实满足

$$
\mathcal T_n(\epsilon)
=\sum_{a\in B_n}\gamma_n(a)
  \prod_{i=0}^{n-1}f^{\circ i}(a)^{\epsilon_i},
\qquad \gamma_n(a)=e_n(a)H_n(a)\ne0.
\tag{R11}
$$

所有 $p\mid e_n(a)$ 的点权重为零。这是代数恒等式本身，
不是删去某类原生周期，也不是把 Jacobian 在局部代数中求逆。

### Step 4. 四块张量的上界不含未知湮灭子

对 $h(X)=\sum_jh_jX^j$，R9 给出

$$
T_h(r,s)=\sum_{q\ge s}
\binom qs(-c)^{q-s}h_{2q+1-r},\qquad 0\le r,s\le m+1.
\tag{R12}
$$

超出次数范围及负下标的系数定义为零。这里输入多项式是
$X^{j+\epsilon}A$ 或 $X^{j+\epsilon}B$，$j,\epsilon\in\{0,1\}$。
次数至多为 $m+2$，所以每个条目的 $q\le m+1$；
所有矩阵都是固定有限矩阵。$c=0$ 时公式直接变为
$T_h(r,s)=h_{2s+1-r}$，不存在负次幂或除以 $c$。

取作者定义的

$$
M_\epsilon=\operatorname{diag}
\left(2\eta T_{X^{1+\epsilon}A},
      \eta T_{X^\epsilon A},
      2T_{X^{1+\epsilon}B},
      T_{X^\epsilon B}\right),
$$

及

$$
E=\operatorname{diag}(I_b,-I_b,-I_b,I_b).
$$

R9 的特殊矩阵在 $S=1$ 时恰为 $EM_\epsilon$，故

$$
\mathcal T_n(\epsilon)
=\operatorname{tr}(EM_{\epsilon_0}\cdots M_{\epsilon_{n-1}}).
\tag{R13}
$$

四项整体标量分别是 $(2\eta)^n,-\eta^n,-2^n,1$，
与 $F_n'H_n$ 的展开一致。该调用仅把 $S=1$ 作为张量构造参数，
**没有假设 $1\in I_w$**。未知非零湮灭子完全不进入矩阵的大小。

全部词矩阵落在

$$
\mathcal D=\bigoplus_{j=1}^{4}\operatorname{Mat}_b(k),
\qquad \dim_k\mathcal D=4b^2=D.
\tag{R14}
$$

对 $n\ge2$、$1\le h\le n-1$，令 $\mathcal F_{n,h}$ 的行、列
分别索引长度为 $h,n-h$ 的二进制词 $u,v$，条目为
$\mathcal T_n(uv)=\operatorname{tr}(EM_uM_v)$。
在 $\mathcal D$ 中选基后，这个矩阵通过其 $D$ 维坐标空间分解，
所以

$$
\operatorname{rank}\mathcal F_{n,h}\le D.
\tag{R15}
$$

使用的是四块代数的维数 $4b^2$，不是全部 $4b$ 阶矩阵空间
的维数 $16b^2$。这里不需要迹配对非退化，也不需要迹能
唯一确定表示；特征中的迹抵消只会降低上界。

### Step 5. 两半插值给出恰等于 $|B_n|$ 的秩

设 $t_n=|B_n|$，先假设 $t_n\ge1$ 且
$2^h\ge t_n$、$2^{n-h}\ge t_n$。
长度为 $h$ 的词 $u$ 对应多项式

$$
P_u(x)=\prod_{i=0}^{h-1}f^{\circ i}(x)^{u_i}.
$$

它首一，次数为 $\sum_i u_i2^i$；这些次数恰好各取
$0,\ldots,2^h-1$ 一次。按次数排列的转换矩阵对角元为一，
所以这些 $P_u$ 是次数低于 $2^h$ 的全部多项式空间的基。

在 $B_n$ 的 $t_n$ 个不同点上，次数低于 $t_n$ 的 Lagrange
插值多项式给出所有点值。其分母是不同点之差，均为 $k$
中非零元素，不要求 $t_n<p$。所以左评估矩阵
$V_{u,a}=P_u(a)$ 有满列秩 $t_n$。

右评估矩阵的条目是

$$
W_{v,a}=
\prod_{j=0}^{n-h-1}
f^{\circ j}(f^{\circ h}(a))^{v_j}.
$$

由 Step 2，$f^{\circ h}(a)$ 遍历的是同一组不同点。
在变量 $y=f^{\circ h}(a)$ 上使用次数低于 $2^{n-h}$ 的
完整二进制基，得到 $W$ 也有满列秩 $t_n$。
没有仅根据 $f^{\circ h}$ 的多项式次数来假设其单射。

由 (R11)，

$$
\mathcal F_{n,h}
=V\operatorname{diag}(\gamma_n(a):a\in B_n)W^{\mathsf T}.
\tag{R16}
$$

满列秩给出 $V,W$ 的左逆；分别从左、右乘这些逆及其转置，
恢复可逆对角矩阵 $\operatorname{diag}(\gamma_n(a))$。
因此乘积的秩至少为 $t_n$，而 (R16) 又给出至多为 $t_n$。
故在这两个半词长度条件下，

$$
\operatorname{rank}\mathcal F_{n,h}=|B_n|\le D.
\tag{R17}
$$

$B_n=\varnothing$ 时是零张量，结论也成立。
没有声称所有短返回层都满足两个半词条件。

### Step 6. 每个指定可见周期确实可保持可见

取 $a\in B_{n_0}$，令 $g=f^{\circ n_0}$，$\mu=g'(a)$。
因为 $g(a)=a$，有以下三个完整分支：

- $\mu=0$：任意正整数 $q$ 的迭代乘子仍为零，
  $g^{\circ q}-x$ 在 $a$ 处重数恒为一。
- $\mu\ne0,1$：令 $t_\mu$ 为其有限乘法阶；
  $q\equiv1\pmod{t_\mu}$ 保证 $\mu^q=\mu\ne1$，
  重数仍为一。
- $\mu=1$：令 $e=e_{n_0}(a)\ge2$。由于 $g-x$ 是非零
  多项式，其局部首个非线性项存在，写为
  $g(a+z)=a+z+u z^e+O(z^{e+1})$，$u\ne0$。
  在复合中该项系数相加，归纳得到
  $g^{\circ q}(a+z)=a+z+quz^e+O(z^{e+1})$。
  所以 $q\equiv1\pmod p$ 保持原整数重数 $e$。

最后一分支中 $a\in B_{n_0}$ 已保证 $p\nmid e$；
论证没有把这个整数重数替换为其剩余类。若点不满足可见性，
则不把它纳入本引理的前提。

再设

$$
\alpha=\eta^{n_0}\prod_{i=0}^{n_0-1}A(f^{\circ i}(a)),
\qquad
\beta=\prod_{i=0}^{n_0-1}B(f^{\circ i}(a)).
$$

分成 $q$ 个重复返回块后，精确有

$$
H_{qn_0}(a)=\alpha^q-\beta^q.
\tag{R18}
$$

在 $\overline{\mathbb F}_p$ 中，每个非零的 $\alpha,\beta,\mu$
都属于某个有限域，故有有限乘法阶。取正整数 $M$ 同时被
$p$ 和这些非零元素的阶整除，令 $q=1+jM$，$j\ge0$。
这些正整数任意大，且同时满足全部所需同余。

非零的 $\alpha,\beta$ 被 $q$ 次幂保持；零值因 $q>0$
仍为零。所以 (R18) 等于 $\alpha-\beta=H_{n_0}(a)$。
单侧为零的两种情形均保留；双侧为零与原可见性矛盾。
上述同一个 $q$ 选择还使

$$
e_{qn_0}(a)=e_{n_0}(a),\qquad
H_{qn_0}(a)=H_{n_0}(a),
$$

因此 $a\in B_{qn_0}$。这是精确的无限同余序列，
不需要 $q$ 为素数，也不需要 $M$ 对所有点统一。
域为 $\overline{\mathbb F}_p$ 的假设在这里实质使用；
未推广到包含超越元的一般代数闭特征 $p$ 域。

### Step 7. 有限可见集只用于选择足够长的返回

假设 $I_w\ne0$。Step 1 给出 $\mathcal B$ 有限。
若为空，则 $I_w=(1)$，周期断言为空，后续结论立即适用。
否则记 $t=|\mathcal B|\ge1$。

固定任意 $a\in\mathcal B$，选 $n_0$ 使其在 $B_{n_0}$
可见，记其原生最小周期为 $r$。
Step 6 给出任意大的 $n=qn_0$ 使其仍在 $B_n$。
选一个这样的 $n$，使 $h=\lfloor n/2\rfloor\ge1$ 且

$$
2^h\ge t,\qquad 2^{n-h}\ge t.
$$

因为 $|B_n|\le t$，Step 5 的两个长度条件满足。
Step 2 又保证 $a$ 的完整 $r$ 周期全包含在 $B_n$ 中。
所以

$$
r\le |B_n|\le D.
\tag{R19}
$$

$t$ 和同余模数可以未知且非常大；只需存在一个足够长的
所选返回层，不必先给出这些量的显式界。
矩阵维数 $D$ 自始至终只由 $m$ 决定。
对每个可见周期分别重复这一逻辑即可，不要求所有可见周期
在同一个返回层同时可见。因此不能把 (R19) 改写为
$|\mathcal B|\le D$。

每个 $a\in\mathcal B$ 都是某个 $F_r$ 的根，$1\le r\le D$。
由于 $Q_{\mathcal B}$ 是不同线性因子的乘积，
$Q_{\mathcal B}\mid S_*$。从 $I_w=(Q_{\mathcal B})$ 得到
$S_*\in I_w$。各 $F_r$ 首一、次数为 $2^r$，故

$$
\deg S_*=\sum_{r=1}^{D}2^r=2^{D+1}-2.
\tag{R20}
$$

这证明全部原生周期和次数结论，且没有额外的 $p,c$
或系数依赖。多项式 $S_*$ 本身依赖 $c$，次数界不依赖。

### Step 8. $N=5D+1$ 和完整理想的有限判据

每个 $q_n$ 非零且首一，因此 $L_N$ 始终是非零首一多项式，
允许 $L_N=1$。由 (R6)，

$$
\bigcap_{1\le n\le N}(q_n)=(L_N),\qquad I_w\subseteq(L_N).
\tag{R21}
$$

如果 $I_w\ne0$，Step 7 给出 $S_*\in I_w$，所以
$L_N\mid S_*$。取逆否命题便得到
$L_N\nmid S_*\Rightarrow I_w=(0)$。

反过来，假设 $L_N\mid S_*$。于是
$\deg L_N\le2^{D+1}-2$，并且

$$
k_{L_N}\le D+1,
\tag{R22}
$$

当 $L_N=1$ 时用 $k_{L_N}=0$，不能写 $\log_2 0$。
按 lcm 的定义，$L_N$ 已满足每个 $1\le n\le N$ 的湮灭
条件。R9 固定 $S$ 定理可应用于这个已构造的非零 $L_N$，
需要的范围不超过

$$
k_{L_N}+16(m+2)^2
\le D+1+4D=5D+1=N.
\tag{R23}
$$

所以 $L_N\in I_w$。理想性给出 $(L_N)\subseteq I_w$，
与 (R21) 合起来证明 $I_w=(L_N)$，即 (R3)。

因为 $D=4(m+2)^2\ge16$，有
$2^D\le2^{D+1}-2<2^{D+1}$，故 $k_{S_*}=D+1$。
同一个 R9 定理恰需检测 $1\le n\le N$，从而还得到

$$
I_w\ne0
\Longleftrightarrow
F_n\mid S_*F_n'H_n\quad(1\le n\le N).
\tag{R24}
$$

这一调用位于显式次数界证明之后，不以 R9 的固定 $S$ 结论
循环论证未知 $S$ 的次数。

## 5. 模解释、边界检查与未证明的结论

作者的模解释可以完全代数化。取直积中的单个元素

$$
v=(F_n'H_n\bmod F_n)_{n\ge1}
\in\prod_{n\ge1}k[x]/(F_n).
$$

映射 $k[x]\to k[x]v$，$S\mapsto Sv$ 的核正是 $I_w$。
所以当 $I_w\ne0$ 时，

$$
k[x]v\simeq k[x]/(L_N),\qquad
\dim_k k[x]v=\deg L_N\le2^{D+1}-2.
$$

这里“family”是该直积中的一个元素，不是另行取无数个
独立生成元。$L_N=1$ 时模为零，维数为零。
这个结论来自已经证明的理想式，不来自 Noetherian 下降链论断。

| 检查点 | 结论 |
| --- | --- |
| $n=1$ | 局部理想、带重数系数恒等式和 R9 矩阵仍适用；张量分割只在选定的长层 $n\ge2$ 使用。 |
| $n=2$ | 可取 $h=1$；仅在实际满足两半长度条件时使用秩等式。 |
| $c=0$ | (R12) 无除法地退化；关键恒等式 (R7) 仍成立。 |
| $m=0$ | $A=B=1$，$b=2,D=16,N=81$；维数和截止不退化。$\eta=1$ 时 $H_n=0,q_n=L_N=1,I_w=(1)$。 |
| $p\mid n$ 或 $p\mid e_n(a)$ | 所有返回层仍定义并检测；权重忠实保留重数在域中的像。 |
| $\mu=0,1$ 或其他值 | Step 6 三分支穷尽，选同一个同余序列，整数重数不变。 |
| $\alpha,\beta$ 单侧零 | 正次幂保持零，另一侧按有限阶保持；没有使用 $\alpha/\beta$。 |
| $\mathcal B=\varnothing$ | 空乘积为一，理想是全环，不是零理想。 |
| $\mathcal B$ 有限但未知大小 | 只用于选任意长返回；未用于矩阵维数或冒充 $|\mathcal B|\le D$。 |
| $L_N=1$ | 固定 $S$ 定理用常数分支 $k_{L_N}=0$，空根集和零模均一致。 |

$A,B$ 的全部根重数和完整系数都保留；$F_n$ 的根重数则按
(R10) 明确映入 $k$。没有从某个原子幂的
周期条件逆推指数一原子，也没有对多个因子逐个施加 (CP)。
本文所证的全层理想有限判据不自动识别普通周期乘积条件：
$F_n'$ 的乘法可能在野性局部因子中损失点值信息。

尤其没有证明非恒定 norm-one 函数总使 $L_N\nmid S_*$。
因此优先目标 $I_w=(0)$ 的全分离、逆向 (CP) 和一般 MS6
仍保持原未证状态。有限理想公式本身不构成这些箭头的证明。

## 6. Corrections、来源范围与最终冻结

本次没有发现需要作者修补的数学或身份记录缺陷，未要求改稿，
也没有替作者修改任何内容。协调者曾先行核查并提示作者注意
秩／持续可见性的接口，这一事实已由作者 Section 9 记录。
本次是全文读取后的非作者独立重构，不称为未见作者稿的盲审。

实际重新核读了
[R9 作者稿 Sections 3、5](../../../continuation_round9/a1_general_quadratic_normone/REPORT.md)
的固定 $S$ 定理、完整矩阵公式及相关参数、截止说明；
实际文件仍为 $437$ 行对应的 SHA-256：

6c7a21d2ceaecf585f7c37f8c57dcce79ce1243d2ec9926059f826adc9e15d40

这与本线程先前 R9 全数学审查所绑定的作者版本一致。
R9 的一般 $c$、全部 $n$、常数 $S$ 和非约化配对接口按原范围
导入；未重新标成 R10 新结论。R10 新桥是 Step 4–7 的秩、
持续可见性和原生周期界，继而才消除未知湮灭子的次数。

**最终裁决：Theorem 1.1 完整数学 PASS，零开放 must-fix。**
原三项结论、全部参数和常数均保持不变。
不作新合同、论文准入、独立优先权或目标算术升级判断。
没有数学程序、数学查询、新 agent、外部模型/API、GPU、
Git 或 PDF 操作；只有本独占评审文件被写入，
作者文件、R9、R8、旧轮与共享文件均保持只读。
