# Paper 30：奇素数幂的首层内部共振局部结构

日期：2026-09-07。作者探针 V1；本轮完整读取 proof-writer 技能。
只写本新稿，不重审已接受的奇素数结论，不产生 Route 或论文验收状态。

## Claim

令 $p$ 为任意奇素数、$a\ge2$、$s=p^a$，$\zeta$ 为任意本原 $s$ 次单位根。
设

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad
m=\frac{p-1}{2},\quad M=\frac{\varphi(p^a)}2=p^{a-1}m,\quad L=\rho\lambda,
$$

并令 $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$，
以 $v_h(h)=1$ 归一化赋值。

本件的多项式对象不是完整的周期 $s$ 首项 $C_s$。
用真实阶数 $s$ 的传播子 $D_n=2-\zeta^n-\zeta^{-n}$，只计算
$1\le n<p$ 的物理分支，并定义第一个内部 $p$ 模态的 forcing 多项式

$$
\mathcal B_{p\mid s}(\lambda)
=-[t^{p-1}]e^v-2\lambda[t^{p-2}]e^{2v}.
\tag{1}
$$

因为 $p<s$，这里不是全系统的首项共振；实际 $v_p$ 不被设为零。
定义其缩放

$$
\mathcal B(h,L)=\rho^{p-1}\mathcal B_{p\mid s}(L/\rho).
$$

则对所有上述 $p,a,\zeta$ 有以下结论。

1. $\deg_L\mathcal B=m$，且

$$
\boxed{
h^{-m}\mathcal B(h,L)\in\mathcal O^+[L],\qquad
\overline{h^{-m}\mathcal B}(L)=(-1)^{m+1}(2-L^m).
}
\tag{2}
$$

2. $\mathcal B(h,L)$ 的 Newton 多边形是一段从 $(0,m)$ 到 $(m,m)$ 的
水平边；原 $\lambda$ 坐标下 $\mathcal B_{p\mid s}$ 的 Newton 边从
$(0,-m)$ 到 $(m,0)$。所有根均简单，且所有根满足 $v_h(\lambda)=-1$。

3. 令 $f=\operatorname{ord}_{\mathbb F_p^\times}(4)$。
在完成局部域 $K^+$ 上，$\mathcal B_{p\mid s}$ 的不可约因子恰有
$m/f$ 个，每个次数为 $f$。尤其当 $p\ge5$ 时没有 $K^+$ 中的根；
当 $f=m$ 时，该内部 forcing 多项式在 $K^+$ 上不可约。

4. 对真实非共振模态 $V_p=\rho^p v_p(L/\rho)$，有

$$
\boxed{
h^mV_p(L)\in\mathcal O^+[L],\qquad
\overline{h^mV_p}(L)=\frac{(-1)^m}{2}(2-L^m).
}
\tag{3}
$$

所以在任何整参数 $L$ 满足 $\overline L^{\,m}\ne2$ 时，
$v_h(V_p(L))=-m$。特别是 $p\ge5$ 时，对每个 $L\in\mathcal O^+$，
这个首层极点都不可避免。

以上是第一层内部 forcing 的无限族定理及精确剩余障碍。
它**不证明**完整 $C_s$ 的 Newton 多边形、平方自由性或与 $Q_s$ 互素。

## Status

内部首层定理 (2)--(3) 及所列 Newton、局部因子型推论：
PROVABLE AS STATED。

完整 $C_{p^a}$ 的 Newton 多边形、平方自由性及 $C_{p^a},Q_{p^a}$
共同根排除：NOT CURRENTLY JUSTIFIED。
本件不以改换多项式对象来宣称这些原目标已经完成。

## Assumptions

- 同一物理正 kick、SUM action、零均值正频规范和固定 $\lambda$。
- 实际递推是
  $v_n=-(E_{n-1}/2+\lambda F_{n-2})/D_n$，$E=e^v,F=e^{2v}$，
  对所有 $1\le n<s$ 成立；本件只需 $n\le p$。
- $s=p^a$、$a\ge2$，不把内部 $p$ 模态误认为真正共振 $s$ 模态。
- 所有模 $h$ 的实系数约化都在 $\mathcal O^+/(h)=\mathbb F_p$ 中；
  不把大环 $\mathbb Z_p[\zeta]/(h)$ 当作该剩余域。

## Notation

用独立形式变量 $H$，定义整数多项式

$$
B_0(H)=2,\quad B_1(H)=2-H,\quad
B_{n+1}(H)=(2-H)B_n(H)-B_{n-1}(H),\quad
d_n(H)=\frac{B_n(H)-2}{H}.
\tag{4}
$$

则 $d_n(H)\in\mathbb Z[H]$、$d_n(0)=-n^2$，
且 $d_n(h)=-D_n/h=D_n/\rho$。令

$$
V_n(H,L)=-\frac{E_{n-1}/2+LF_{n-2}}{d_n(H)},\quad 1\le n<p,
\qquad E=e^V,\quad F=e^{2V},
$$
$$
\mathcal B(H,L)=-E_{p-1}-2LF_{p-2}.
\tag{5}
$$

指数只取所需有限系数，至多除以 $(p-1)!$。
这里不构造越过 $p!$ 的特征 $p$ 指数级数。
写 $\kappa=(-1)^{m+1}$。

## Proof Strategy

关键不是先强行归一化整个 $p^a$ 系统，而是计算首个非单位传播子
$d_p$ 出现前的有限整块。这个块不具备特征零的 $p$ 周期反射对称性。
保留有限 action 的反射缺陷，计算它在 $H^m$ 的第一个非零项，
便得到式 (2) 的新常数 $2$。随后把这一真实局部余式转成 Newton
和因子型结论，再精确除以内部传播子得到式 (3)。

## Dependency Map

1. 圆分分歧给出 $v_h(p)=M$ 和 $d_p$ 的阶数 $2m$。
2. 小于 $p$ 的递推整性使有限 action 及反射缺陷可安全约化。
3. 形式参数中的首个反射缺陷位于 $H^m$，而非 $p$。
4. 平方传播子低阶解计算该缺陷的系数，得到 $2-L^m$。
5. $M>2m$ 把形式模 $p$ 身份转成真实局部整除和极点。
6. 剩余多项式可分及 Frobenius 轨道给出 Newton 和局部因子型。

## Proof

### Step 1. 分层传播子与分歧高度

圆分整性与完全分歧给出
$v_\pi(p)=\varphi(p^a)$，其中 $\pi=\zeta-1$。
又有 $h=-\pi^2/\zeta$，所以 $v_\pi(h)=2$、
$v_h(p)=M$，$\mathcal O^+/(h)=\mathbb F_p$。
这些标准事实在作者官网的
[Milne，命题 6.2](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=98)
对一般素数幂成立，本轮已核对。

若 $n=p^bj$、$p\nmid j$、$0\le b<a$，则
$\zeta^{p^b}$ 的阶数是 $p^{a-b}$，塔中的分歧指数为 $p^b$。
因而

$$
v_\pi(D_n)=2p^b,\qquad
v_h(d_n(h))=p^b-1.
\tag{6}
$$

这已经说明素数证明中的“全部低阶传播子为单位”不能延用。
更精确地，式 (4) 在特征 $p$ 中满足

$$
B_p(H)=(2-H)^p=2-H^p,\qquad
d_p(H)\equiv-H^{p-1}\pmod p .
\tag{7}
$$

因为 $M=p^{a-1}m>2m=p-1$，把 $H=h$ 代入式 (7) 后可除以
$h^{2m}$，得到

$$
\boxed{d_p(h)/h^{2m}\equiv-1\pmod h.}
\tag{8}
$$

### Step 2. 低阶整块与有限 action 的精确缺陷

对 $1\le n<p$，$d_n(0)=-n^2$ 是 $p$-单位，所以三角归纳给出

$$
V_n(H,L)\in\mathbb Z_p[L][[H]],\qquad
\mathcal B(H,L)\in\mathbb Z_p[L][[H]].
\tag{9}
$$

权重计数给出 $\deg_L\mathcal B\le m$。引入临时一步幅度 $b$，
定义有限 action

$$
\Phi(v;H,b,L)=[x^p]\left(
\frac12v\mathcal D_Hv+\frac b2xe^v+\frac L2x^2e^{2v}
\right),\qquad \mathcal D_Hx^n=d_n(H)x^n.
\tag{10}
$$

它只涉及 $v_1,\ldots,v_{p-1}$。在式 (5) 的分支、$b=1$ 处，

$$
\frac{\partial\Phi}{\partial v_i}
=\frac{d_i(H)+d_{p-i}(H)}2V_{p-i}
+\frac12E_{p-i-1}+LF_{p-i-2}
=\frac{d_i(H)-d_{p-i}(H)}2V_{p-i}.
$$

故不能将分支当作此 off-$H$ 泛函的临界点。给 $v_i,b,L$ 分别赋权
$i,1,2$，$\Phi$ 的加权次数为 $p$。精确 Euler 身份给出

$$
\boxed{
\mathcal B(H,L)
=-2p\Phi(V;H,1,L)+
\sum_{i=1}^{p-1}i\bigl(d_i(H)-d_{p-i}(H)\bigr)V_iV_{p-i}.
}
\tag{11}
$$

这里保留了全部非驻值项。式 (9)--(10) 都整，因此随后模 $p$ 合法。

### Step 3. 首个反射缺陷的通用系数

在 $\mathbb F_p[[\eta]]$ 中置 $z=1+\eta$、
$H=2-z-z^{-1}=-\eta^2/(1+\eta)$。
代入给出从 $\mathbb F_p[[H]]$ 到该环的单射，并且

$$
d_i-d_{p-i}
=\frac{z^i+z^{-i}-z^{p-i}-z^{-p+i}}H
=\frac{(z^p-1)(z^{i-p}-z^{-i})}{H}.
$$

由 Frobenius，$z^p-1=\eta^p$；
第二个因子的线性项是 $2i\eta$。所以首项为
$-2i\eta^{p-1}$。又 $H^m$ 的首项为 $(-1)^m\eta^{p-1}$，
而表达式本身是 $H$ 的多项式，故余项必须至少为 $H^{m+1}$。得到

$$
\boxed{d_i(H)-d_{p-i}(H)
=2\kappa\,i\,H^m+O(H^{m+1})\quad\text{于 }\mathbb F_p[H].}
\tag{12}
$$

即使写成 $\eta$ 后下一候选阶为奇数，也不会产生半整数次 $H$；
原多项式性质排除了这种项。

### Step 4. 缺陷系数的有限求值

由式 (11)--(12)，只需取 $V_i(0,L)$。令

$$
A(x)=1-x/2+(1-4L)x^2/16=(1-r_1x)(1-r_2x).
$$

平方传播子的特征零解是 $W=-\log A$，所以对 $i<p$，

$$
V_i(0,L)=W_i=\frac{r_1^i+r_2^i}{i},\qquad
r_1+r_2=1/2,\quad (r_1-r_2)^2=L.
\tag{13}
$$

这些系数均整。模 $p$ 后，

$$
\sum_{i=1}^{p-1}i^2W_iW_{p-i}
=-\sum_{i=1}^{p-1}
(r_1^i+r_2^i)(r_1^{p-i}+r_2^{p-i}).
$$

记 $\delta=r_1-r_2$。在形式二次扩张中，

$$
r_1^p+r_2^p=1/2,\qquad
r_1^p=1/4+\delta L^m/2,\qquad
r_2^p=1/4-\delta L^m/2.
$$

交叉和为

$$
\sum_{i=1}^{p-1}r_1^ir_2^{p-i}
=\frac{r_1^pr_2-r_1r_2^p}{r_1-r_2}
=\frac{L^m-1}{4}.
$$

因此

$$
\sum_{i=1}^{p-1}i^2W_iW_{p-i}
=\frac12-\frac{L^m-1}{2}=\frac{2-L^m}{2}.
\tag{14}
$$

虽然计算使用 $\delta^{-1}$，结果是多项式恒等式；
先在 $\delta\ne0$ 的形式局部化证明，再由多项式环单射延伸，
所以它也覆盖 $L=0$，没有删除特殊参数。

代回式 (11)，得到真正的形式剩余式

$$
\boxed{
\mathcal B(H,L)=
\kappa H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
\quad R,T\in\mathbb Z_p[L][[H]].
}
\tag{15}
$$

$L$ 次数有统一有限界。注意常数是 $2$，不能替换成素数分母闭合时的 $1$。

### Step 5. 从形式身份转到实际内部极点

在式 (15) 代入 $H=h$。由于 $M>m$，
$p/h^m$ 可整除 $h$；所以

$$
h^{-m}\mathcal B(h,L)\in\mathcal O^+[L],\qquad
\overline{h^{-m}\mathcal B}=\kappa(2-L^m).
$$

这证明式 (2)，并由非零最高次项推出次数恰为 $m$。
实际 $p$ 模态不是共振，故式 (4) 在 $n=p$ 给出

$$
V_p=\frac{\mathcal B(h,L)}{2d_p(h)}.
$$

结合式 (8) 得到

$$
\overline{h^mV_p}
=-\frac{\kappa}{2}(2-L^m)=\frac{(-1)^m}{2}(2-L^m),
$$

即式 (3)。如果 $\overline L^m\ne2$，右端为单位，极点阶恰为 $m$。
对于物理 $\lambda\in\mathcal O^+$，有 $L=\rho\lambda\equiv0$，所以还得到

$$
v_h\bigl(v_p(\lambda)\bigr)=-m-p
\quad\text{对每个 }\lambda\in\mathcal O^+.
\tag{16}
$$

这是一条真实系数赋值，不是对完整 $C_s$ 根位置的断言。

### Step 6. Newton 单边与平方自由性

式 (2) 说明 $\mathcal B(h,L)$ 的所有系数赋值至少为 $m$，
常数项与最高次项的赋值恰为 $m$，中间系数至少为 $m+1$。
因此其 Newton 下凸包恰为所述水平边。

若 $\mathcal B_{p\mid s}(\lambda)=\sum_{j=0}^m b_j\lambda^j$，则

$$
[L^j]\mathcal B(h,L)=\rho^{p-1-j}b_j,\qquad
v_h(b_j)\ge j-m,
$$

两个端点取等号。所以原坐标的 Newton 边为 $(0,-m)$ 至 $(m,0)$。
也可不用 Newton 根定理，直接验证根的赋值：对
$h^{-m}\mathcal B$，常数项和最高次项都是单位。
根的 $L$ 赋值若正，常数项是唯一最小赋值项；若负，最高次项是唯一
最小赋值项，均不可能相消。因此所有根的 $v_h(L)=0$，
即 $v_h(\lambda)=-1$。

剩余多项式 $\kappa(2-L^m)$ 与其导数互素，因为 $m$ 在特征 $p$ 非零，
而其根非零。故归一化多项式的判别式为单位，特征零中所有根互异。
这只证明内部 $\mathcal B_{p\mid s}$ 平方自由。

### Step 7. 明确的局部因子次数

若 $\alpha^m=2$，则

$$
\alpha^p=\alpha^{2m+1}=4\alpha.
$$

Frobenius 每次作用都是乘以 $4$，所以每个根轨道长度恰为
$f=\operatorname{ord}_{\mathbb F_p^\times}(4)$。又 $4^m=1$，故 $f\mid m$；
剩余多项式由 $m/f$ 个互异的 $f$ 次不可约因子组成。

把 $h^{-m}\mathcal B$ 除以其单位最高次系数使其首一。
$\mathcal O^+$ 是完成离散赋值环，剩余因子互素，所以
[Milne，Hensel 因子提升定理 7.33](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=123)
逐个唯一提升这些因子。提升后的每个因子不可约：若有非平凡分解，
其根的整性使首一因子仍整，约化将给出对应不可约剩余因子的非平凡分解。
于是局部因子个数及次数与剩余多项式相同。

当 $p\ge5$，$4\ne1\pmod p$，所以 $f>1$，没有 $K^+$ 中的根。
等价地，对 $L\in\mathcal O^+$，$\overline L^m$ 只能为 $0,1,-1$，
不能等于 $2$。当 $p=3$，$f=1,m=1$，剩余根为 $L=2$；
式 (2)--(3) 仍成立，但“所有整数 $L$ 都出现极点”不适用于这个剩余类。
证明完毕。$\square$

## Corrections or Missing Assumptions

本件无需额外科学假设，但必须区分三个对象：

| 对象 | 本件状态 |
|---|---|
| 第一个内部 forcing $\mathcal B_{p\mid p^a}$ | Newton 单边、平方自由、局部因子次数已给出证明 |
| 真正完整首项 $C_{p^a}$ | 尚未得到 Newton 多边形或平方自由证明 |
| 更高内部模态 $V_{2p},V_{3p},\ldots$ | 未从本件首层公式外推其最低阶或主项 |

常数 $2$ 的来源不是归一化错误。在平方传播子常数层，
$\mathcal B(0,L)=-2p^2W_p$，故

$$
\mathcal B(0,L)/p\equiv-1\pmod p.
$$

素数分母中 $p$ 与 $h^m$ 同阶，这个常数层参与首层闭合；
在当前 $p^a$、$a\ge2$ 中它被推至 $h^M$，高于 $h^m$，
因此真实内部余式保留 $2-L^m$。
这是新尺度差异的解释，不是重开已接受素数证明的审查。

## Open Risks and Next Exact Obligation

- 首个内部极点已明确，所以不能把低阶素数单位递推沿用到 $s-1$；
  从这里起，指数系数会遇到非整 $V_p$ 与非单位 $p!$。
- 若要得到完整 $C_s$，需构造并证明一个消去非 $p$ 倍频后的有限
  Schur 补或等价分层递推，保留每个内部层的整性、参数多项式和取消。
  仅把 $d_p$ 替换成一个“有效传播子”、或只保留单独 $V_p$ 链，
  尚不能控制同阶的其他模态贡献。
- 特别不能把 $\mathcal B_{p\mid s}$ 的根当作 $C_s$ 的根，不能从其
  平方自由性推出 $C_s$ 平方自由，也不能推出 $C_s,Q_s$ 互素。
- 作者和主控分别得到同一 Frobenius 轨道公式，属于协作交叉计算，
  不重复计为非作者验收。本件尚待独立核查。
- 本轮没有新增素数清单、根搜索、实验脚本或状态入口变更；
  仅新建本稿并核对公开作者官网的两个标准数论依据。

