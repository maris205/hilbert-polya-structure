# Paper30：有界次数多项式剪切的统一相对字长

日期：2026-09-06。性质：独立有界数学核查与完整作者证明。
只新增本文件；此前全部报告冻结，不开展整体混合或其他商空间任务。

## Claim

设 $d\geq2$，$p>d$ 为素数，$P\in\mathbb F_p[X]$ 为任意首一、次数恰为 $d$ 的多项式。
在 $\mathbb F_p^2$ 上令
$$
H_P(x,y)=(P(x)-y,x),\qquad
\mathcal S_P=\operatorname{ASL}_2(\mathbb F_p)\cup\{H_P,H_P^{-1}\}.
$$
每个任意选择的特殊仿射变换算一字，$H_P$ 和 $H_P^{-1}$ 各算一字。
证明存在仅依赖 $d$ 的 $B(d)$，使任意 $R\in\mathbb F_p[X]$、$\deg R\leq d$ 的水平剪切
$$
T_R(x,y)=(x+R(y),y)
$$
都可以写成至多 $B(d)$ 个 $\mathcal S_P$ 字母的乘积。
这里 $R$ 不要求首一，零多项式也包括在内。

## Status

`PROVABLE AS STATED`。完整证明给出一个显式但不声称最优的上界：
$$
B(d)=12\cdot2^d-4d-11.
\tag{1}
$$
字长界不依赖 $p$、$P$ 的任意低阶系数或 $R$ 的任意系数。
具体所选字母可以依赖这些数据；统一的是字母个数，而不是要求所有目标使用同一个词。

## Assumptions

- 底域是素域 $\mathbb F_p$，$p>d$；不将 Cauchy–Davenport 擅自推广到任意素数幂域。
- 群乘法为映射复合，右边的因子先作用。
- 字长使用整个 $\operatorname{ASL}_2(\mathbb F_p)$ 作为允许的一字集合。
  本命题不是某个固定小生成集合上的字长估计。
- 允许 $H_P$ 的正逆映射；构造中反转已有词不会改变词长上界。
- 所有多项式及变换恒等式均在 $\mathbb F_p$ 上成立；不使用数值近似或系数拟合。

## Notation

记 $|G|_{\mathcal S_P}$ 为相应最短字长，单位映射的长度取 $0$。
定义
$$
J(x,y)=(-y,x),\qquad Y(x,y)=(x,y+1),\qquad
D_t(x,y)=(tx,t^{-1}y)\quad(t\in\mathbb F_p^*).
$$
它们及逆映射均属于 $\operatorname{ASL}_2(\mathbb F_p)$。
令有限差分为 $\Delta Q(X)=Q(X+1)-Q(X)$，并记
$$
Q_r=\Delta^{d-r}P\quad(0\leq r\leq d).
$$
若 $A\subseteq\mathbb F_p$，$mA$ 始终表示允许重复加数的 $m$ 重和集
$A+\cdots+A$，不是标量乘法集合。

## Proof Strategy

先从 $H_P$ 提取 $T_P$，再用有限差分提取每个次数的一个非零首项模型剪切。
特殊线性对角共轭把该首项乘以 $(r+1)$ 次幂；
Cauchy–Davenport 保证至多 $r+1$ 个这样的幂值足以合成任意首项系数。
最后逐次消去低阶误差，并累计明确的词长上界。

## Dependency Map

1. 模型剪切的提取依赖三个直接复合恒等式及 $p>d$ 时有限差分的次数下降。
2. 任意首项系数的合成依赖乘法群循环性和素数模数的 Cauchy–Davenport 定理。
3. 全部目标系数的处理依赖次数归纳，允许每一阶的剩余多项式系数任意。
4. 最终上界来自构造词长的递推求和，不宣称最短词长。

## Proof

### Step 1. 提取 $T_P$ 并逐次作有限差分

因为 $J^{-1}(x,y)=(y,-x)$，直接代入给出
$$
H_PJ^{-1}(x,y)=(P(y)+x,y)=T_P(x,y).
\tag{2}
$$
所以 $|T_P|_{\mathcal S_P}\leq2$。
对任意多项式 $Q$，复合方向固定后有
$$
Y^{-1}T_QY=T_{Q(X+1)},\qquad
Y^{-1}T_QYT_Q^{-1}=T_{\Delta Q}.
\tag{3}
$$
这里 $T_{Q(X+1)}$ 表示剪切函数在纵坐标处取 $Q(y+1)$。
若已有 $T_Q$ 的一个长度至多 $\ell$ 的词，则 (3) 构造出 $T_{\Delta Q}$ 的词，
长度至多 $2\ell+2$。

定义构造上界
$$
\ell_0=2,\qquad\ell_{m+1}=2\ell_m+2,
\quad\text{因此}\quad\ell_m=4\cdot2^m-2.
\tag{4}
$$
归纳应用 (3) 得到
$$
|T_{Q_r}|_{\mathcal S_P}\leq\ell_{d-r}.
\tag{5}
$$
式 (4) 是构造词的上界；当模型剪切本身已经仿射时，它一般不是最短长度。

若 $Q$ 的次数为 $j$、首项系数为 $b$，且 $1\leq j\leq d<p$，
则 $\Delta Q$ 的次数为 $j-1$、首项系数为 $jb\neq0$。
因 $P$ 首一，故
$$
\deg Q_r=r,\qquad [X^r]Q_r=b_r:=\frac{d!}{r!}\in\mathbb F_p^*.
\tag{6}
$$
所有相关整数因子都在 $1,\ldots,d$ 内，因此 $p>d$ 正好保证这里没有次数塌缩。

### Step 2. 用有界多个幂值表示任意系数

这里使用的 Cauchy–Davenport 定理为：若 $p$ 是素数且 $A,B\subseteq\mathbb F_p$ 非空，
则
$$
|A+B|\geq\min\{p,|A|+|B|-1\}.
\tag{CD}
$$
已实际读取 Alon–Nathanson–Ruzsa 原作者公开论文的 Theorem 1.1（PDF 第 1 页），
并核对该文第 4 页从其多项式方法推出此定理的证明：
[N. Alon, M. B. Nathanson and I. Z. Ruzsa, *The polynomial method and restricted sums of congruence classes*,
J. Number Theory 56 (1996), 404–417](https://web.math.princeton.edu/~nalon/PDFS/anrf3.pdf)。
采用的是该文无加数互异限制的 Theorem 1.1，不是限制和集版本。

对固定 $1\leq r\leq d$，定义
$$
A_r=\{t^{r+1}:t\in\mathbb F_p\},\qquad
g_r=\gcd(r+1,p-1).
$$
乘法群 $\mathbb F_p^*$ 是 $p-1$ 阶循环群，因此幂映射的非零像大小为 $(p-1)/g_r$；
计入零值后，
$$
|A_r|=1+\frac{p-1}{g_r},\qquad1\leq g_r\leq r+1.
\tag{7}
$$
反复应用 (CD) 给出
$$
|mA_r|\geq\min\{p,m(|A_r|-1)+1\}\quad(m\geq1).
$$
特别地，
$$
|g_rA_r|\geq\min\{p,g_r(p-1)/g_r+1\}=p,
\qquad g_rA_r=\mathbb F_p.
\tag{8}
$$
因此每个 $c\in\mathbb F_p$ 都可写为至多 $g_r\leq r+1$ 个非零参数的幂值之和：
$$
c=\sum_{i=1}^s t_i^{r+1},\qquad
0\leq s\leq g_r,\quad t_i\in\mathbb F_p^*.
\tag{9}
$$
证明是先使用 (8) 得到恰好 $g_r$ 个来自 $A_r$ 的加数，再删除其中的零加数。
对 $c=0$ 也可直接取空和。参数可以重复，(CD) 没有要求它们互异。
这一步从不需要 $D_0$；它并不是一个可逆变换。

### Step 3. 对角共轭合成任意最高次系数

对每个 $t\neq0$，按定义依次复合得到
$$
D_tT_QD_t^{-1}(x,y)=(x+tQ(ty),y)=T_{tQ(tX)}(x,y).
\tag{10}
$$
所以当 $Q=Q_r$ 时，新的剪切多项式次数仍为 $r$，首项系数是 $b_rt^{r+1}$，
而该共轭的字长至多为 $\ell_{d-r}+2$。

给定任何希望实现的 $r$ 次项系数 $a\in\mathbb F_p$，
对 $c=a/b_r$ 应用 (9)，并令
$$
S(X)=\sum_{i=1}^s t_iQ_r(t_iX).
$$
由于所有水平剪切满足 $T_AT_B=T_{A+B}$，有
$$
T_S=\prod_{i=1}^sD_{t_i}T_{Q_r}D_{t_i}^{-1},\qquad
[X^r]S=b_r\sum_{i=1}^s t_i^{r+1}=a.
\tag{11}
$$
因此 $\deg S\leq r$，且
$$
|T_S|_{\mathcal S_P}\leq(r+1)(\ell_{d-r}+2).
\tag{12}
$$
如果 $a=0$，可以取空乘积 $T_S=I$，即 $S=0$；(12) 仍然成立。

### Step 4. 按次数消去全部低阶项

对固定的 $d$ 定义
$$
B_0=1,\qquad
B_r=B_{r-1}+(r+1)(\ell_{d-r}+2)\quad(1\leq r\leq d).
\tag{13}
$$
我们归纳证明：每个次数至多 $r$ 的多项式 $R$ 都满足
$|T_R|_{\mathcal S_P}\leq B_r$。

当 $r=0$，$T_R$ 是水平平移，属于特殊仿射群，所以长度至多 $1$。
零平移是单位映射，长度为 $0$。

现在设结论已对 $r-1$ 成立。给定 $\deg R\leq r$，令 $a=[X^r]R$，
由 Step 3 构造满足 $[X^r]S=a$ 的 $S$。
于是 $R-S$ 次数至多为 $r-1$。由于低阶归纳允许任意系数，得到
$$
|T_{R-S}|_{\mathcal S_P}\leq B_{r-1}.
$$
再用精确恒等式 $T_R=T_ST_{R-S}$ 和 (12)，
$$
|T_R|_{\mathcal S_P}\leq(r+1)(\ell_{d-r}+2)+B_{r-1}=B_r.
$$
归纳闭合，特别适用于所有 $\deg R\leq d$。
从始至终没有要求 $R$ 或任一低阶剩余多项式首一。

### Step 5. 显式统一字长

由 (4)、(13)，
$$
B_d=1+4\sum_{r=1}^d(r+1)2^{d-r}.
$$
有限几何级数求和给出
$$
\sum_{r=1}^d(r+1)2^{d-r}=3\cdot2^d-d-3,
$$
因此
$$
B_d=12\cdot2^d-4d-11.
$$
这正是 (1)，只依赖 $d$，证明原命题。$\square$

## Corrections or Missing Assumptions

主控推导无需定理级修正；以下细节已精确处理：

1. $H_PJ^{-1}=T_P$ 与 $Y^{-1}T_QYT_Q^{-1}=T_{\Delta Q}$ 按右因子先作用逐式核验。
2. 对角共轭产生的是 $tQ(tX)$，因此首项变化为 $t^{r+1}$，不是 $t^{r-1}$。
3. 覆盖用的幂值集合包括零，但构造词时删除零加数；从未使用 $D_0$。
4. 和集允许重复参数。只用非零幂值而忘记零补位，不能直接得到这里的 $g_rA_r=\mathbb F_p$。
5. 当 $d=p-1$、从而某一幂指数可能等于 $p$ 时，(7)、(8) 仍成立；
   $p>d$ 保证有限差分所需因子非零，边界不需要额外排除。
6. $\ell_m$、$B_r$ 是明确构造上界，不是声称无相邻字母抵消的最短词长。

## Open Risks

- 对上述生成集合和量词没有剩余证明缺口；不声称 (1) 最优或寻找表示的计算成本同样有界。
- 不将“任意特殊仿射变换算一字”偷换为某个固定小生成集合上的统一字长。
- 本报告只证明水平多项式剪切的表示，不开展同步点插值、整体混合或 Doeblin 比较。
- 不从二次剪切结论外推四点问题，不重新推导商空间能量，不作新意、容量或论文完成判断。

## 来源与交付边界

本轮完整读取 `proof-writer/SKILL.md`，并核验上述原作者公开论文的 Cauchy–Davenport
定理及其证明位置。经典和集定理是明确引用的输入，不作为新的研究贡献。
全部新增内容均为符号证明；没有实验、外部写入、代理派生或冻结文件修订。
只交付本报告，原命题按原始范围成立，至此完成本次有界任务。
