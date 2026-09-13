# qPI 垂直首 jet：原矩阵次数约束下的数字分解 V1

日期：2026-09-09。执行者：`/root/p30_qpi_post_integral_ideas_v1`。
类型：有界作者引理；不是 P03 完整作者件的独立验收或正式评分。
`route_applicability: NOT_APPLICABLE`。0 GPU；仅新增本报告，既有矩阵引理与其他报告冻结不改。

## Claim

令 $p$ 为奇素数，$a\ge1$，$N=p^a$，
$$\sigma=1+p+\cdots+p^{a-1}=\frac{p^a-1}{p-1}.$$
取状态系数环与相对一形式模
$$R_p=\mathbb F_p[t^{\pm1},x^{\pm1},y^{\pm1}],\qquad
\Omega=\Omega^1_{R_p/\mathbb F_p[t^{\pm1}]}=R_p\,dx\oplus R_p\,dy.$$
使用原 qPI 矩阵 $A(z)$，固定时间参数 $t$，置
$$
J=y-x+x/y-t/x,\qquad S=t+Jz+z^2,\qquad
\Delta=S^2-4z^3,
$$
$$
\Gamma(z)=\operatorname{tr}\bigl(dA(z)[A(z),z\partial_zA(z)]\bigr)\in\Omega[z],
$$
$$
\beta_N=[z^N]\Gamma(z)\Delta(z)^{(N-3)/2},\qquad
H_p(t,J)=[z^{p-1}]\Delta(z)^{(p-1)/2}.
$$
则有一形式恒等式
$$\boxed{\quad\beta_{p^a}=H_p(t,J)^{\sigma-1}\beta_p.\quad} \tag{1}$$
它是同一固定时间、同一谱缩放规范下的首阶项迭代式。
这里 $a$ 改变原圆分阶 $p^a$，不表示已经计算到 $\pi^a$ 或任何高于首阶的厚度。

条件性几何后果：若在原光滑能级开集上，$\beta_p$ 已被识别为正则切向一形式类，
则 (1) 给出的 $\beta_{p^a}$ 正则切向类在 $a>1$、$H_p=0$ 的层上为零。
本件不证明该原几何正则性接口，也不据此确定实际更高 $\pi$ 阶的首非零项。

## Status

**PROVABLE AS STATED。**

主恒等式 (1) 无新增几何假设；切向消失结论严格带有 Claim 中的正则类条件。
证明使用原矩阵的特定次数界，不对任意矩阵多项式 $A(z)$ 作同式断言。

## Assumptions、依赖与输入身份

前置固定输入是已全文读取并保持冻结的
[首 jet 矩阵引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md)，
283 行、14,146 字节，SHA-256：
`f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd`。
消费它的式 (4)、(5)、(10)–(13)：原矩阵规范、首谱缩放项、实际先除以 $N$ 的圆分接口和时间提升边界。

原矩阵来自该件亲读绑定的
[整数候选 brief §2.2](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)；
本件不重开其几何或旧候选状态。
所有微分均固定 $t,z$，只作用于状态 $x,y$；交换子为 $[X,Y]=XY-YX$。
没有把 $\beta_N$ 改成完整 $\alpha_N$，也没有改动前置已固定的降序乘积次序。

## Notation 与 Proof Strategy

仅为把原矩阵写紧凑，记 $v=y-1$、$u=x(y-1)$；它们不是新的独立状态变量。
原矩阵逐项等于
$$
A(z)=A_0+zA_1+z^2E,\qquad E=\begin{pmatrix}1&0\\0&0\end{pmatrix},
$$
$$
A_0=\begin{pmatrix}t-u&-x\\v(u-t)&u\end{pmatrix},\qquad
A_1=\begin{pmatrix}J-1&1\\J+u-1&1\end{pmatrix}. \tag{2}
$$
例如 $v(u-t)=t+x-ty-2xy+xy^2$，所以 (2) 没有替换原构造。

令
$$f(z)=\Delta(z)^{(p-1)/2}\in R_p[z],\qquad
G(z)=\Gamma(z)\Delta(z)^{(p-3)/2}\in\Omega[z].$$
使用 `proof-writer` 的分层证明结构，责任链为：

1. 用 (2) 的真实二次结构与 $dE=0$ 证明 $\Gamma$ 只支持次数 $1$ 至 $4$。
2. 得出 $\operatorname{supp}_zG\subset[1,2p-2]$ 和 $\operatorname{supp}_zf\subset[0,2p-2]$。
3. 先提取最低位的唯一次数 $p$，再逐位提取唯一次数 $p-1$。
4. 把得到的标量乘积识别为 $H_p^{\sigma-1}$；最后单列正则类与时间提升边界。

## Proof

### Step 1. 原 $\Gamma$ 的次数界

因为原 $E$ 与状态无关，$dA=dA_0+z\,dA_1$，而
$$z\partial_zA=zA_1+2z^2E.$$
不交换非交换因子，直接展开可得
$$
\begin{aligned}
[A,z\partial_zA]
&=z[A_0,A_1]+2z^2[A_0,E]
  +2z^3[A_1,E]+z^3[E,A_1]\\
&=z[A_0,A_1]+2z^2[A_0,E]+z^3[A_1,E].
\end{aligned} \tag{3}
$$
$[A_1,A_1]=[E,E]=0$ 消去了其他项；两个三次项的系数相加为 $2-1=1$。
因此
$$\Gamma(z)=\gamma_1z+\gamma_2z^2+\gamma_3z^3+\gamma_4z^4, \tag{4}$$
其中全部系数明确为
$$
\begin{aligned}
\gamma_1&=\operatorname{tr}(dA_0[A_0,A_1]),\\
\gamma_2&=\operatorname{tr}(dA_1[A_0,A_1])+2\operatorname{tr}(dA_0[A_0,E]),\\
\gamma_3&=2\operatorname{tr}(dA_1[A_0,E])+\operatorname{tr}(dA_0[A_1,E]),\\
\gamma_4&=\operatorname{tr}(dA_1[A_1,E]).
\end{aligned} \tag{5}
$$
这给出全部可能谱次数，既无常数项，也无五次及以上项。
作为对原矩阵的额外核准，由 (2) 的右上条目为常数 $1$ 可直接得到
$$\gamma_4=-d(J+u-1).$$
次数界的真正前提是原 $A$ 二次且最高次矩阵 $E$ 对状态微分为常数。
对一般更高次 $A$，或最高次矩阵有状态依赖的其他族，本证明不给相同范围。

### Step 2. 低位与高位多项式的准确范围

原判别式展开为
$$\Delta=t^2+2tJz+(J^2+2t)z^2+(2J-4)z^3+z^4.$$ 
因此 $f=\Delta^{(p-1)/2}$ 没有负次数，最高次数为 $2p-2$。
结合 (4)，$G=\Gamma\Delta^{(p-3)/2}$ 没有低于一次的项，且
$$\deg_zG\le4+4\frac{p-3}{2}=2p-2.$$
所以可严格写作
$$
f(z)=\sum_{r=0}^{2p-2}h_rz^r,\qquad
G(z)=\sum_{r=1}^{2p-2}g_rz^r, \tag{6}
$$
其中 $h_r\in R_p$、$g_r\in\Omega$，允许某些系数为零。
尤其 $h_{p-1}=H_p(t,J)$，$g_p=\beta_p$。
$p=3$ 时 $G=\Gamma$，范围仍是 $[1,4]=[1,2p-2]$，没有遗漏小特征边界。

### Step 3. Frobenius 因子与唯一数字分解

$a=1$ 时 (1) 是恒等式 $\beta_p=H_p^0\beta_p$。
以下设 $a\ge2$。
整数指数满足
$$\frac{p^a-3}{2}=\frac{p-3}{2}+\frac{p-1}{2}\sum_{i=1}^{a-1}p^i.$$
从而
$$\beta_{p^a}=[z^{p^a}]G(z)\prod_{i=1}^{a-1}f(z)^{p^i}. \tag{7}$$
在特征 $p$ 的标量环上，Frobenius 给
$$f(z)^{p^i}=\sum_{r=0}^{2p-2}h_r^{p^i}z^{rp^i}.$$
这里取幂的只有标量多项式 $f$，不对 $G$ 或一形式 $\beta_p$ 取 Frobenius 幂。

由 (6)–(7)，任何贡献到 $z^{p^a}$ 的项，其谱次数必须满足
$$r_0+pr_1+p^2r_2+\cdots+p^{a-1}r_{a-1}=p^a,$$
$$1\le r_0\le2p-2,\qquad0\le r_i\le2p-2\quad(1\le i\le a-1). \tag{8}$$
模 $p$ 后，$r_0\equiv0$。区间 $[1,2p-2]$ 中唯一的 $p$ 倍数是 $p$，故 $r_0=p$。
从 (8) 减去 $p$ 再除以 $p$，得到
$$r_1+pr_2+\cdots+p^{a-2}r_{a-1}=p^{a-1}-1.$$
再模 $p$，$r_1\equiv p-1$；区间 $[0,2p-2]$ 中唯一满足它的整数是 $p-1$，
因为下一候选 $2p-1$ 已越过上界。
减去 $p-1$、除以 $p$ 后，右端成为 $p^{a-2}-1$。
逐次重复这一已明确的同余和区间论证，最终得到唯一解
$$r_0=p,\qquad r_1=\cdots=r_{a-1}=p-1.$$
它确实满足 (8)，因为
$$p+(p-1)(p+p^2+\cdots+p^{a-1})=p^a.$$
因此不是忽略进位，而是给出了所有允许次数中唯一可能的数字选择。

### Step 4. 系数重组与条件性消失

由唯一解直接读取 (7) 的系数：
$$
\begin{aligned}
\beta_{p^a}
&=g_p\prod_{i=1}^{a-1}h_{p-1}^{p^i}\\
&=H_p(t,J)^{p+p^2+\cdots+p^{a-1}}\beta_p
=H_p(t,J)^{\sigma-1}\beta_p.
\end{aligned}
$$
这证明了 (1)，不需要系数域完美，也没有选取 Frobenius 根。

现在只陈述条件性几何接口。设 $W$ 是原光滑能级开集，切向一形式线丛为
$$\mathcal T=\Omega^1_{W/\mathbb F_p[t^{\pm1}]}/\mathcal O_W\,dJ,$$
在实际所用基域或时间特化后按相同相对定义解释。
假设原环面上的 $[\beta_p]$ 已经识别并正则延拓为 $b_p\in\Gamma(W,\mathcal T)$。
则 (1) 给出匹配环面公式的正则切向延拓
$$b_{p^a}=H_p^{\sigma-1}b_p.$$
在光滑能级开集上 $\mathcal T$ 局部自由，故与稠密环面相容的该延拓唯一。
当 $a>1$ 时 $\sigma-1>0$，所以将它限制到 $H_p=0$ 的层，得到 $b_{p^a}=0$。
在已接受的原 Hasse 解释下，这包含光滑超奇异能级。

本段不证明 $b_p$ 的原几何正则延拓；也不声称 $b_p$ 非零或准确的 $H_p$ 消失重数。
它更不决定原整除微分在该层下一项的 $\pi$ 赋值或更高厚度。∎

## 完整首 jet 与时间提升的边界

前置矩阵引理的实际圆分对象是先在特征零归一化的
$$\alpha_N=N^{-1}dI_N.$$
在 $\pi=\zeta_N-1$ 下，它只给到
$$\alpha_N\equiv F_N(A(t))+\pi\beta_N(A(t))\pmod{\pi^2},$$
其中零阶项在特征 $p$ 为
$$F_N(A(t))=H_p(t,J(t))^\sigma\,dJ(t).$$
其系数等式也由 (6) 的范围直接给出：在
$[z^{N-1}]\prod_{i=0}^{a-1}f(z)^{p^i}$ 中，每一位都只能取 $p-1$，
故系数是 $\prod_{i=0}^{a-1}h_{p-1}^{p^i}=H_p^\sigma$。
若同时令 $t=t_0+\pi t_1$、$t_1$ 对状态微分为常数，完整一阶系数是
$$\beta_N(A(t_0))+
t_1\left.\partial_t\bigl(H_p(t,J(t))^\sigma dJ(t)\bigr)\right|_{t=t_0}.$$
后项包括 $J(t)$ 与 $dJ(t)$ 的变化，不能丢弃。
因此 (1) 仅分解固定时间的谱缩放项；不能将其改写成未经证明的完整 $\alpha_N$ 迭代式。
本件的条件性切向消失也不等于完整两方向理想已经得到或非切向更高阶项已经计算。

## 实际有限核验

本次两段只读内存 `python -B` 计算均正常 exit 0，没有写脚本或数据文件：

1. 将原完整 $A_0,A_1,E$ 代入，分别检查 $dx,dy$ 系数：
   $[A,zA_z]$ 与 (3) 完全相等；$\Gamma$ 的非零谱次数均落在 $1,2,3,4$，
   四个系数分别与 (5) 完全相等。
2. 取独立标量变量 $t,h$、$\Delta=(t+hz+z^2)^2-4z^3$，
   对 $(p,a)=(3,2),(5,2)$ 以及每个 $r=1,2,3,4$ 精确核验
   $$[z^{p^a-r}]\Delta^{(p^a-3)/2}
   =H_p(t,h)^{\sigma-1}[z^{p-r}]\Delta^{(p-3)/2}.$$
   负次数系数取零，全部断言通过。这等价于独立核对四个形式 $\gamma_r$ 方向，
   不依赖原一形式各系数之间可能存在的关系。

有限核验仅排查符号、次数界和小实例；全部 $p,a$ 的证明由 Steps 1–4 承担。
没有展开任何高于首阶的 $\pi$ 项，也没有作原超奇异点的数值非消失测试。

## Corrections or Missing Assumptions

- 主控提出的迭代式原样成立，无需改指数或附加数值因子。
- 原 $A$ 的二次结构、状态无关的 $E$、四次 $\Delta$ 及 $\Gamma$ 无常数项不可省略为任意矩阵假设。
- Frobenius 乘积只作用于标量 $f$；右端是一形式 $\beta_p$ 乘标量，不是 $\beta_p$ 的幂。
- 超奇异层上的几何切向消失仅在原正则类接口成立后消费；本件不代签该接口。
- $p=2$ 不在本公式范围；$a>1$ 的一阶消失不是实际更高厚度已经确定。

## Open Risks 与机制定位

此迭代来自原低次数谱结构与唯一数字分解，没有新增一般 Cartier 理论或全厚度理论。
后续真正未闭合的责任仍是原 $\beta_p$ 的正则切向识别、首项非消失及
$a>1$ 首阶项消失后的实际下一阶信息；它们不因本件而自动接受。
原曲面全部两方向理想、不同时间提升的比较、正式新意／价值和正文容量均不在本件范围。
仅新增本报告；未创建候选、稿件、锁、PDF 或对外发布。
