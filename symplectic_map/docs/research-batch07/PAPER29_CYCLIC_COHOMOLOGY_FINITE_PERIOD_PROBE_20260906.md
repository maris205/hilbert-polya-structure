# 多相位 Hénon 多项式上同调：单个有限周期概形检测预筛

日期：2026-09-06。独立有界数学任务。只新增此报告；不改之前的 splitting-rigidity STOP 报告、scalar 报告或正式论文。

## Claim

设 $K$ 是特征零域，$k\ge1$，$p_0,\ldots,p_{k-1}\in K[T]$，且 $d_j=\deg p_j\ge2$。按周期 $k$ 延拓 $p_i,d_i$ 到所有 $i\in\mathbb Z$。令
$$H_j(x,y)=(p_j(x)-y,x),\qquad F=H_{k-1}\circ\cdots\circ H_0.$$

定义实际轨道多项式 $X_i\in K[x,y]$：
$$X_0=x,\qquad X_{-1}=y,\qquad p_i(X_i)=X_{i-1}+X_{i+1}.$$
对 $g\in K[x,y]$，使用§1的唯一正规形，令 $L(g)$ 是其中所有非恒定标准单项式的支撑直径的最大值；空集的最大值约定为零。

**主命题。** 对任意 $n\ge1$，若
$$N=kn\ge3,\qquad N>2L(g),$$
则以下条件等价：

1. 存在多项式 $f\in K[x,y]$，满足 $g=f\circ F-f$。
2. $g$ 的正规形中，常数项为零，且每个标准单项式的 shift-$k$ 轨道上的系数和均为零。
3. 在完整固定点概形 $\operatorname{Fix}(F^n)$ 的坐标环中，
   $$S_ng:=\sum_{j=0}^{n-1}g\circ F^j=0.$$

这里的周期数据是整个固定点**概形**上的元素，不只是所有几何周期点上的函数值，也不是某个双曲集合上的 Livšic 条件。$S_n$ 是沿迭代的和，不是乘法算子的矩阵迹。

若 $\deg_{x,y}g\le D$，§5给出由相位次数唯一确定的精确最坏跨度界 $L_{\mathrm{ph}}(D)$。因而一个有效选择为
$$n_{\mathrm{eff}}(D)=\left\lceil\frac{\max\{3,2L_{\mathrm{ph}}(D)+1\}}{k}\right\rceil.$$
设 $\delta=\prod_{j=0}^{k-1}d_j$。对 $D\ge1$，所选检测概形的代数长度满足
$$\dim_K K[\operatorname{Fix}(F^{n_{\mathrm{eff}}})]
=\delta^{n_{\mathrm{eff}}}\le\delta^4D^4.$$
这只是代数长度上界，不是位复杂度或所有检测算法的复杂度声明。

此外，§8证明任何次数至多 $D$ 的多项式 coboundary 都有次数至多 $D$ 的多项式 primitive，并由相位的混合进位制置换给出滤过上同调的精确 Hilbert 级数。该级数依赖给定坐标中的普通次数滤过，不宣称为任意多项式共轭下的不变量。

## Status

**`PROVABLE AS STATED`，但必须采用上述 scheme 条件与严格多相位阈值。**

原提案中的基础构造、上同调刻画及 $N>2L$ 检测闭合。原线性跨度估计可以正确解释为仅计邻居扩张步，因此不是需要反例否定的结论；不过§5的相位乘积权将主有效界改进为对数级，且给出精确最坏跨度。

一个实际被否定的推广是：“二次单相位的 $N=2L$ 改进自动适用于任意多相位。”§6.3 给出 $k=2,N=6,L=3$ 的确切相位混叠反例。

没有授予研究新颖性、自然篇幅或 Paper29 候选 PASS；没有建立正式项目。基础正规形机制有明确前人工作，见下节。

## Assumptions, scope and prior boundary

本任务使用已全文读取的 `proof-writer`；本次再次全文读取该技能，按其要求把精确命题、证明依赖、实际失败与边界分开。

Thierry Bousch 的作者稿 [*Algèbres de Hénon*](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf) 已经全文核对：§2 的 Théorème 1 给二次有限周期代数的 squarefree 基与唯一 fission 正规形；§5.1 引入 wrapping；Théorème 1 bis 给无限轨道代数的基；§7 将 Hénon 作用写成指标平移。§2 也明确区分非约化代数与仅取点值。该文 Théorème 3 是乘法迹所给平均值的最终稳定，并不是本报告 $S_ng=0$ 的上同调检测命题。

因此本报告**不把 orbit-algebra、无限基、有限基、wrapping 或 shift 本身包装为全新机制**。这里给出多次数、多相位的完整自足证明，真正待独立查新的增量是上同调检测、相位混叠边界与有效/锐跨度量化；没有完成外部优先权穷尽调查。

所有原始多项式 $p_j$ 的首项系数只要求非零，不要求 monic 或正系数。下文将首项系数除出只是书写正规化。$K$ 不必代数闭。

## Proof strategy and dependency map

1. 严格降普通总次数的重写系统，结合互素纯幂歧义的合流，建立无限与有限的标准单项式基。
2. 无限代数与真实 $K[x,y]$ 双向同构，将宏映射识别为 shift-$k$；由自由单项式轨道直接计算多项式 coboundary。
3. 有限周期代数与 $\operatorname{Fix}(F^n)$ 概形环同构；$N>2L$ 时唯一大循环间隙排除不同宏轨道混叠。
4. 两侧相位乘积权控制正规形支撑，实际轨道多项式的次数证明上界可达。
5. 构造临界周期反例，区分 scalar/binary 与多相位边界。
6. 证明平移轨道上的次数离散凸，构造不增次数的 primitive，再由混合进位制计数得到精确滤过 Hilbert 级数。

## 1. 无限代数的终止、合流和真实相空间同构

### 1.1 Rewrite system

写
$$p_i(T)=a_iT^{d_i}+q_i(T),\qquad a_i\in K^*,\qquad\deg q_i<d_i.$$
令
$$R_\infty=K[Z_i:i\in\mathbb Z],$$
其中每个元素只涉及有限多个变量。定义
$$r_i=a_i^{-1}\bigl(Z_{i-1}+Z_{i+1}-q_i(Z_i)\bigr),\qquad
I_\infty=(Z_i^{d_i}-r_i:i\in\mathbb Z).$$
重写规则为 $Z_i^{d_i}\longrightarrow r_i$。

若一个普通总次数为 $D$ 的单项式被重写，则每个所得单项式的次数都至多 $D-1$。因此递归重写树的深度至多 $D$，分支数有限。任意多项式重写顺序也终止：将当前单项式次数组成有限多重集，按由大到小的次数计数比较，每次以有限多个较小次数取代一个次数；等价地，序数 $\omega^Dc_D+\omega^{D-1}c_{D-1}+\cdots+c_0$ 严格下降，其中 $c_r$ 是当前次数为 $r$ 的非零单项式个数。系数相消只会减少该多重集。

这里不需要在以 $\mathbb Z$ 为指标的无限变量集上，未经说明地选择一个 shift-invariant well-order。

### 1.2 Confluence

对单项式次数作归纳。唯一歧义是同一单项式 $M$ 同时被两个不同规则 $i\ne j$ 整除；同一规则的两次选择没有不同的结果。

若 $Z_i^{d_i}Z_j^{d_j}\mid M$，先作 $i$ 规则，再在线性展开中将原有的 $Z_j^{d_j}$ 因子重写，得到
$$\frac{M}{Z_i^{d_i}Z_j^{d_j}}r_ir_j.$$
反过来先 $j$ 再 $i$ 得到同一个多项式。即便 $i,j$ 相邻，$r_i$ 含 $Z_j$ 也不妨碍此等式：原来保留的 $Z_j^{d_j}$ 因子仍可重写。所有中间单项式次数都低于 $\deg M$，所以归纳假设保证它们的完全正规形一致。

将正规形线性延拓到多项式，记为 $\operatorname{NF}_\infty$。上述归纳也证明它不依赖重写顺序。对每个单项式 $M$，
$$\operatorname{NF}_\infty\bigl(M(Z_i^{d_i}-r_i)\bigr)=0.$$
故它湮灭 $I_\infty$。反过来，重写保持模 $I_\infty$ 的同余类，而不可约单项式被正规形固定。因此
$$\mathcal B=\left\{\prod_{i\in\mathbb Z}Z_i^{e_i}:
e_i=0\text{ 除有限多项外},\ 0\le e_i<d_i\right\}$$
的像构成 $A_\infty=R_\infty/I_\infty$ 的 $K$-基。

这一步证明的是线性独立性，不仅是通过重写得到一个生成集。

### 1.3 Isomorphism with $K[x,y]$

在 $K[x,y]$ 中，从 $X_0=x,X_{-1}=y$ 向正、负两个方向使用递推，得到全部 $X_i$。代入 $Z_i\mapsto X_i$ 给出同态
$$\Psi:A_\infty\longrightarrow K[x,y].$$
反向同态 $\Theta:K[x,y]\to A_\infty$ 由 $x\mapsto[Z_0],y\mapsto[Z_{-1}]$ 定义。关系递推逐一给出 $[Z_i]=X_i([Z_0],[Z_{-1}])$，故 $\Theta\Psi$ 在所有生成元上恒等；$\Psi\Theta$ 在 $x,y$ 上恒等。于是两者互逆。

以下将 $Z_i$ 的标准单项式与相应真实轨道多项式 $X_i$ 的乘积识别。

### 1.4 Macro shift

逐个 $H_j$ 迭代给出 $F^*X_0=X_k$、$F^*X_{-1}=X_{k-1}$。序列 $F^*X_i$ 与 $X_{i+k}$ 满足同一递推，因为 $p_{i+k}=p_i$；由这两个相邻初值向正、负方向递推得
$$F^*X_i=X_{i+k}\qquad(i\in\mathbb Z).$$
记这个作用为 $\tau$。它保持基 $\mathcal B$，且正规形与 $\tau$ 交换。这里必须使用 shift-$k$，不能用 shift-$1$ 替代；即使所有 $p_j$ 相同，所研究的宏映射仍可能是一个真迭代。

## 2. 多项式 coboundary 的完整刻画

除常数单项式 $1$ 外，$\tau$ 在 $\mathcal B$ 上的每个轨道都自由：一个非空有限支撑集合不可能等于其非零平移。

将正规形写成有限和
$$\operatorname{NF}_\infty(g)=c_0+\sum_O\sum_{r\in\mathbb Z}c_{O,r}\,\tau^r b_O,$$
其中 $O$ 遍历出现的非恒定基轨道，$b_O$ 是任一代表，且每个内和仅有限项非零。定义轨道和
$$c_O=\sum_r c_{O,r}.$$

若 $g=(\tau-1)f$，则常数正规系数为零，且每个轨道系数按 $c_{O,r}=b_{O,r-1}-b_{O,r}$ 望远镜相消，故 $c_O=0$。

反之，若 $c_0=0$ 且所有 $c_O=0$，令
$$b_{O,r}=-\sum_{s\le r}c_{O,s}.$$
这些系数也有限支撑，因为总和为零。定义
$$f=\sum_O\sum_r b_{O,r}\tau^r b_O.$$
直接比较每个基元素的系数，得到 $(\tau-1)f=g$。因此 Claim 中的条件1与2等价；解 $f$ 唯一模常数，因为 $\ker(\tau-1)=K$。

注意“常数项”是**正规形**常数项，而不是原 $K[x,y]$ 表达式的常数项。例如 $p(x)=x^2+c$ 时，$F^*x-x=x^2-y-x+c$ 的原常数项可能非零，但正规形是 $X_1-X_0$，正规常数项为零。

## 3. 有限周期代数确实是固定点概形环

令 $N=kn\ge3$，并在 $\mathbb Z/N\mathbb Z$ 上定义
$$A_N=K[Z_i:i\bmod N]\big/
\bigl(p_i(Z_i)-Z_{i-1}-Z_{i+1}:i\bmod N\bigr).$$
因 $k\mid N$，$p_i$ 的下标在模 $N$ 后无歧义。

§1.1–1.2 的同一个严格降次数、纯幂合流证明适用，给出基
$$\mathcal B_N=\left\{\prod_{i=0}^{N-1}Z_i^{e_i}:0\le e_i<d_i\right\}.$$
所以
$$\dim_K A_N=\prod_{i=0}^{N-1}d_i=\delta^n.$$
该维数计算不要求概形约化。

映射 $Z_i\mapsto Z_{i\bmod N}$ 诱导 wrapping 同态 $W_N:A_\infty\to A_N$。在 $K[x,y]$ 的识别下，其核为
$$J_N=(X_N-X_0,\ X_{N-1}-X_{-1}).$$
理由是：这两个相邻周期关系与递推一起，向两个方向推出每个 $X_{i+N}=X_i$；反之全部周期关系包含这两个。于是有限代数与该二生成理想的商互相给出逆同态。

根据 $F^{n*}(x,y)=(X_N,X_{N-1})$，恰有
$$A_N\simeq K[x,y]/J_N=K[\operatorname{Fix}(F^n)].$$
同时，$F^*$ 对应 $A_N$ 中的循环 shift-$k$，记为 $\tau_N$，且 $\tau_N^n=1$。

## 4. 单个充分长周期的无混叠与检测证明

### 4.1 The exact no-alias lemma

非恒定标准单项式 $b=\prod X_i^{e_i}$ 的支撑为 $E=\{i:e_i>0\}$，直径为
$$\operatorname{diam}(b)=\max E-\min E.$$
若 $\operatorname{diam}(b)\le L<N/2$，则不同支撑指标模 $N$ 后仍不同，故 $W_Nb$ 本身就是 $\mathcal B_N$ 中的基元素，无需进一步重写。

将支撑放在长度 $N$ 的圆周上，考虑相邻占据指标之间的**循环距离**，而不是空位置的个数。从最大指标绕回最小指标的外间隙长度为
$$N-\operatorname{diam}(b)>L.$$
所有内部间隙长度都至多 $L$。因此有唯一一个大于 $L$ 的间隙。单点支撑的唯一间隙为 $N$，结论仍成立。

这个唯一间隙决定了把循环单项式切开并提升回整数直线的方法，唯一性只差整体平移一个 $N$ 的整数倍。由于 $N$ 是 $k$ 的倍数，以下两点成立：

- 若两个直径至多 $L$ 的无限标准单项式，wrapping 后落在同一个循环 shift-$k$ 轨道上，则它们原来已在同一个无限 shift-$k$ 轨道上。
- 每个这样的循环单项式的 shift-$k$ 轨道长度恰为 $n$。非平凡稳定平移会移动唯一大间隙的端点，与其唯一性矛盾。

这不是一般“有限字总能唯一解码”的断言，严格的 $N>2L$ 正是这里用于保证唯一切口的条件。

### 4.2 Trace detection

对§2的每个无限轨道 $O$，选一个在 $g$ 中出现的代表 $b_O$，使其直径至多 $L(g)$。wrapping 后
$$W_N(S_ng)
=n c_0+\sum_O c_O\sum_{j=0}^{n-1}\tau_N^j W_N(b_O).$$
这里同一无限轨道上的任意平移具有同一个循环轨道和，因此系数只通过 $c_O$ 出现。

由§4.1，不同 $O$ 的循环轨道互不相交，且每个内和包含 $n$ 个不同的基元素。常数基元素又与它们都不同。于是上式为零，当且仅当全部 $c_O$ 为零且 $nc_0=0$。特征零保证 $n\ne0$，故等价于 $c_0=0$。结合§2，得到条件3推出条件1。

另一个方向不需要长度界：若 $g=(F^*-1)f$，则
$$S_ng=F^{n*}f-f,$$
在 $\operatorname{Fix}(F^n)$ 概形环中为零。Claim 的三个条件因而完全等价。$\square$

## 5. 精确跨度、对数次数界与检测代数长度

### 5.1 Phase-product weights

定义正整数权重
$$w_0=w_{-1}=1,$$
$$w_i=\prod_{r=0}^{i-1}d_r\quad(i\ge1),\qquad
w_i=\prod_{r=i+1}^{-1}d_r\quad(i\le-2).$$
其规则是从初始两点 $\{-1,0\}$ 分别向外，每跨过一个指标 $i$ 就乘以 $d_i$。对所有 $i$，都有
$$w_{i-1}\le d_iw_i,\qquad w_{i+1}\le d_iw_i.$$
向外的一侧等号成立；向内的一侧严格小于。并且 $\deg q_i<d_i$，所以全部重写规则不增加单项式加权次数 $\sum_i e_iw_i$。

普通次数至多 $D$ 的原多项式 $g(X_0,X_{-1})$ 的每个单项式，加权次数也至多 $D$。正规形每一项因此仍满足
$$\sum_i e_iw_i\le D.$$

### 5.2 Exact worst-case support diameter

对整数 $D\ge0$，定义
$$L_{\mathrm{ph}}(D)
=\max\bigl(\{b-a:a<b,\ w_a+w_b\le D\}\cup\{0\}\bigr).$$
该最大值是有限且可计算的，因为权重在两端指数增长。每个具有至少两个支撑点的正规单项式，其两端权重之和不超过 $D$，所以
$$L(g)\le L_{\mathrm{ph}}(D).$$

这个界是**准确的最坏情形界**，不是只有数量级。递推直接证明
$$\deg_{x,y}X_i=w_i.$$
正向第一步 $X_1=p_0(x)-y$ 的次数是 $d_0$；以后 $p_i(X_i)$ 的次数 $d_iw_i$ 严格大于被减去的 $X_{i-1}$ 的次数。负向从 $X_{-2}=p_{-1}(y)-x$ 开始相同地逐步比较。首项系数始终非零，因此不存在最高次相消。

于是每个允许的端点对 $a<b$ 本身给出多项式 $X_aX_b$，其普通次数恰为 $w_a+w_b$；其正规形就是标准单项式 $X_aX_b$，因为两个指数均为 $1<d_i$。取实现最大值的端点对，即达到了 $L_{\mathrm{ph}}(D)$。$D\le1$ 时最大跨度为零。

### 5.3 A closed uniform bound

令 $d=\min_jd_j\ge2$。有
$$w_i\ge d^{\operatorname{dist}(i,\{-1,0\})}.$$
对 $D\ge2$，定义
$$h=\left\lfloor\log_d(D/2)\right\rfloor,$$
$$L_d(D)=1+2h+\mathbf 1_{\{D\ge(d+1)d^h\}}.$$
则
$$L_{\mathrm{ph}}(D)\le L_d(D)\le1+2\lfloor\log_dD\rfloor.$$
证明是将端点向两侧的距离写成 $r,s\ge0$：端点距离至多 $1+r+s$，而 $d^r+d^s\le D$。固定 $r+s=t$ 时，和最小恰在两个指数相差至多一时取得。最大可能的 $t$ 因而是 $2h$，或在所示门槛成立时为 $2h+1$。

当全部 $d_i=d$ 时，取两个端点在初始区间的相反两侧就达到这个上界，所以 $L_{\mathrm{ph}}(D)=L_d(D)$。这也明确处理 $D=2$ 的边界：$L_d(2)=1$。

原提案的线性粗界可救，但不作为主界：只有产生邻居 $X_{i\pm1}$ 的重写分支才可能扩支撑，该分支降低普通次数 $d_i-1\ge d-1$。下阶 $X_i^{d_i-1}$ 分支虽只降一次数，却不扩支撑。因此不能把全部重写步都按 $d-1$ 收费；若只数邻居步，原粗估计仍安全。上述加权证明不需要这个粗估计。

### 5.4 Effective period and quartic algebra-size bound

取
$$n_{\mathrm{eff}}(D)=\left\lceil\frac{\max\{3,2L_{\mathrm{ph}}(D)+1\}}{k}\right\rceil.$$
此时 $N=kn_{\mathrm{eff}}$ 满足主定理的两个条件，故一次完整概形周期检测就足够。

设 $\delta=\prod_{j=0}^{k-1}d_j$，且 $D\ge1$。将任一向外距离写成 $qk+r$，$0\le r<k$，相应权重至少为 $\delta^q$。令 $t=\lfloor\log_\delta D\rfloor$，所有可能出现的指标均在
$$[-kt-k,\ kt+k-1]$$
内，因此
$$L_{\mathrm{ph}}(D)\le2kt+2k-1,\qquad
n_{\mathrm{eff}}(D)\le4t+4.$$
利用§3的实际有限基长度，得到
$$\dim_K A_{kn_{\mathrm{eff}}}=\delta^{n_{\mathrm{eff}}}
\le\delta^{4t+4}\le\delta^4D^4.$$
没有由此推出正规形算法的位复杂度、稀疏复杂度或全部可能检测方法的计算下界。

## 6. 阈值反例、scalar 二次例外与相位误推广

### 6.1 General alphabets: $N=2L$ really can fail

先取 $k=1$、$d\ge3$ 和 $L\ge2$，令
$$g=X_0X_L^2-X_0^2X_L.$$
两个标准单项式不在同一无限平移轨道上，因为按从左到右读出的指数分别为 $(1,2)$ 与 $(2,1)$。由§2，$g$ 不是多项式 coboundary。

但在 $N=n=2L$ 的有限周期代数中，循环平移 $L$ 恰交换两项，故 $S_ng=0$。因此通用阈值不能把 $N>2L$ 简单弱化为 $N\ge2L$。

### 6.2 Sharp degree-scale examples

仍取 $k=1$、$d\ge3$。对 $r\ge1$，置 $a=-r-1,b=r,L=2r+1$，令
$$g_r=X_aX_b^2-X_a^2X_b.$$
两端轨道多项式的次数均为 $d^r$，并分别具有非零纯 $y^{d^r}$、纯 $x^{d^r}$ 最高项。上述差的两个最高单项式不同，不相消，所以
$$\deg g_r=D_r=3d^r.$$
它不是 coboundary，却在单个周期 $n=4r+2=2L$ 上通过 scheme 和为零的测试。

另一方面，§5.3 给出 $L_d(D_r)=2r+1$，故统一有效阈值为 $n_{\mathrm{eff}}(D_r)=4r+3$。因此在这串输入次数上，保证“**每个** $n\ge n_{\mathrm{eff}}(D)$ 都检测**全部**次数至多 $D$ 的输入”的最终统一阈值不能降低一单位；在这一精确量词下，主导尺度 $4\log_dD+O(1)$ 的系数 $4$ 也不能在一般 $d\ge3$ 情形降低。

这不排除特意选择某个更短的单一 $n(D)$，也不排除多周期联合检测；更不是所有 coboundary 算法的复杂度下界。

### 6.3 Binary scalar improvement, and why it is not automatically multiphase

若 $k=1,d=2$，在 $N=2L\ge3$ 时，不同无限单项式平移轨道仍不会混叠。若支撑直径小于 $L$，或支撑至少有三个点，循环外间隙仍唯一最大。唯一剩余情形是单项式 $X_aX_{a+L}$：两个间隙等长，但交换切口得到的无限单项式本来就是同一个全整数平移轨道。

这一情形的有限轨道可能只有 $n/2$ 个元素，不过周期和只多出非零因子 $2$，在特征零下不影响零检测。因此 scalar binary 可改用 $N\ge2L$。$N=2L-1$ 时，
$$g=X_0X_L-X_0X_{L-1}$$
则给出失败反例：无限支撑距离不同，有限圆周上却为同一平移轨道。

**实际多相位反例。** 取 $k=2$、全部 $d_i=2$、$L=3$、$N=6$，故宏周期 $n=3$。令
$$g=X_0X_3-X_3X_6.$$
这两个无限单项式虽相差 shift-$3$，却不相差 shift-$2$ 的整数次，因此由§2它不是 $F$ 的 coboundary。但 $W_6g=0$，从而 $S_3g=0$ 在 $\operatorname{Fix}(F^3)$ 的概形环中成立。

这反驳了“$N$ 为 $k$ 的倍数就足够处理临界等长切口”的推理。一般多相位定理保留 $N>2L$。若另外有 $k\mid L$，binary 临界切口也保持宏相位，可以作相应特例改进；本报告不为了最佳多相位例外分类继续扩展任务。

## 7. Scheme versus point values: strict delivery boundary

主定理已证明的是理想成员关系
$$S_ng\in(X_N-X_0,X_{N-1}-X_{-1}),$$
不是只证明 $S_ng$ 在其几何零点集合上消失。后者最多把它放进该理想的根理想；非约化固定点概形可能保留非零幂零类。

没有假设所有周期点横截、简单或双曲，也没有逐参数证明固定点理想为根理想。若另行满足约化假设，scheme 测试才可等价改写成所有几何周期点的周期和为零；没有该假设时不作此升级。

本报告也未将固定点概形上的轨道和 $S_ng$ 与 Bousch 的乘法迹平均混为一谈；两者的取值空间和消失条件不同。

## 8. 次数不增的 primitive 与多相位滤过上同调

### 8.1 A filtration-adapted mixed-radix basis

令 $V_D=\{g\in K[x,y]:\deg g\le D\}$，$V_{-1}=0$。对标准单项式 $b_e=\prod_iX_i^{e_i}$，定义
$$A(e)=\sum_{i\ge0}e_iw_i,\qquad B(e)=\sum_{i\le-1}e_iw_i.$$
正向 $X_i$ 的最高齐次项为非零常数乘 $x^{w_i}$，负向 $X_i$ 的最高齐次项为非零常数乘 $y^{w_i}$；这正是§5.2的严格次数比较所给。因此 $b_e$ 的最高齐次项为
$$c_e x^{A(e)}y^{B(e)},\qquad c_e\in K^*,$$
且
$$\mu(b_e):=\deg b_e=A(e)+B(e).$$

正、负两条射线上的指数分别是逐位基数 $d_0,d_1,\ldots$ 与 $d_{-1},d_{-2},\ldots$ 的有限混合进位制数字。反复取余和整除给出每个非负整数的唯一有限表示。因此
$$e\longleftrightarrow(A(e),B(e))\in\mathbb Z_{\ge0}^2$$
为双射，且不同标准单项式有不同的最高 $x^Ay^B$ 单项式。于是 $V_D$ 的基恰为 $\mu(b_e)\le D$ 的标准单项式；尤其
$$\dim_K V_D=\binom{D+2}{2}.$$
这既排除了不同最高项间的隐蔽取消，也说明这里确实是原始普通次数滤过，而非另造的形式字长滤过。

### 8.2 Discrete convexity and degree-preserving primitives

固定一个指标 $i$。沿宏平移 $i\mapsto i+k$，其权重序列在跨越初始区间前后具有形状
$$\ldots,\delta^2b,\delta b,b,a,\delta a,\delta^2a,\ldots,$$
其中 $a,b$ 是依赖于该指标余类的正整数。两条几何尾部的二阶差为正；中间两处二阶差分别为
$$a+(\delta-2)b,\qquad b+(\delta-2)a,$$
也为正，因为 $\delta\ge2$。因此 $r\mapsto w_{i+rk}$ 离散凸，不需要额外假设 $a/b$ 的大小。

对每个非恒定标准单项式 $b_e$，
$$r\longmapsto\mu(\tau^rb_e)=\sum_i e_iw_{i+rk}$$
也是离散凸函数。其次数至多 $D$ 的整数下水平集是一个区间。

若 $g\in V_D$ 是 coboundary，§2 在每个轨道上构造的 primitive 只在原有非零系数最小、最大平移指标之间填入累计系数。该区间两端的单项式都在 $V_D$ 中，故离散凸性保证所有填入的单项式也在 $V_D$ 中。于是得到
$$g\in V_D\cap(\tau-1)K[x,y]
\quad\Longrightarrow\quad
\exists f\in V_D:\ g=(\tau-1)f.$$
由于 $\tau f=f+g$，还自动有 $\tau f\in V_D$。这个结论对任意 $k$、任意所述相位次数与全部下阶系数成立。

### 8.3 The exact phase permutation

令
$$\mathcal H=K[x,y]/(\tau-1)K[x,y],\qquad
\mathcal H_D=\operatorname{image}(V_D\to\mathcal H).$$
定义 $\mathcal H_{-1}=0$。下面计算
$$\operatorname{Hilb}_{\mathrm{gr}\mathcal H}(t)
=\sum_{D\ge0}\dim_K(\mathcal H_D/\mathcal H_{D-1})t^D.$$

对标准单项式的负向数字写
$$B=\delta Q+R,\qquad Q\ge0,\quad0\le R<\delta.$$
令 $e_j=e_{-j}$，$1\le j\le k$；则 $0\le e_j<d_{k-j}$，且
$$R=\sum_{j=1}^{k}e_j\prod_{h=1}^{j-1}d_{k-h}.$$
定义混合进位制反向重编码
$$\rho(R)=\sum_{j=1}^{k}e_j\prod_{h=0}^{k-j-1}d_h,$$
空乘积均为一。这个定义是一个集合 $\{0,\ldots,\delta-1\}$ 上的置换：原数字按负向基数唯一编码 $R$，宏平移后它们恰好成为正向指标 $k-j$ 的合法数字，并唯一编码 $\rho(R)$。基数不等时不假设 $\rho$ 是对合。

宏平移将原正向块的权重乘 $\delta$，将负向深部块的权重除 $\delta$，并将低 $k$ 位重编码为 $\rho(R)$。于是对于唯一对应于 $(A,Q,R)$ 的标准单项式，
$$\mu(b)=A+\delta Q+R,\qquad
\mu(\tau b)=\delta A+Q+\rho(R).$$

### 8.4 Counting the filtered image

令
$$W_D=\{f\in V_D:\tau f\in V_D\},\qquad E_D=\dim_KW_D.$$
滤过适配基与 $\tau$ 的基置换性质给出
$$E_D=\#\{b\in\mathcal B:\max(\mu(b),\mu(\tau b))\le D\}.$$
§8.2 证明 $(\tau-1)W_D=V_D\cap(\tau-1)K[x,y]$；该映射的核为常数空间。所以
$$\dim_K\mathcal H_D=\binom{D+2}{2}-E_D+1.$$

记单项式精确权重计数级数为
$$E(t)=\sum_{b\in\mathcal B}t^{\max(\mu(b),\mu(\tau b))},\qquad
C_\rho(t)=\sum_{R=0}^{\delta-1}t^{\max(R,\rho(R))}.$$
固定 $R$ 后，分别按 $A=Q$、$A=Q+s$、$Q=A+s$（$s\ge1$）求和。后两种情况下，因 $R,\rho(R)\in[0,\delta-1]$，分别有
$$\max(\mu(b),\mu(\tau b))=(\delta+1)Q+\delta s+\rho(R),$$
$$\max(\mu(b),\mu(\tau b))=(\delta+1)A+\delta s+R.$$
因此固定 $R$ 的贡献为
$$\frac{1}{1-t^{\delta+1}}
\left[t^{\max(R,\rho(R))}
 +\frac{t^\delta}{1-t^\delta}\bigl(t^R+t^{\rho(R)}\bigr)\right].$$
利用 $\rho$ 是置换，汇总得到
$$E(t)=\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}}.$$
由上一维数恒等式逐级作差，最终得到完整公式
$$\boxed{
\operatorname{Hilb}_{\mathrm{gr}\mathcal H}(t)
=1+\frac{1}{(1-t)^2}
-\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}}.
}$$
常数项为 $1$，符合常数函数给出非零上同调类。该公式与全部首项非零系数、下阶系数无关；其输入仅是有序相位次数与指定的初始坐标/宏相位。

### 8.5 Scalar specialization and actual phase distinction

当 $k=1$、$\delta=d$ 时，$\rho$ 为恒等，故
$$C_\rho(t)=1+t+\cdots+t^{d-1},$$
并得到
$$\operatorname{Hilb}_{\mathrm{gr}\mathcal H}(t)
=1+\frac{t-t^d}{(1-t)^2(1-t^{d+1})}.
$$
这里只作为多相位公式的特例列出，不复制其它代理的 scalar 定义域分类或应用。

作为真正的多相位例子，取 $k=2,d_0=d_1=2$。此时 $\delta=4$，
$$\rho(0)=0,\quad\rho(1)=2,\quad\rho(2)=1,\quad\rho(3)=3,$$
所以
$$C_\rho(t)=1+2t^2+t^3.$$
单因子次数四的情形则有 $C_{\mathrm{id}}(t)=1+t+t^2+t^3$。两者普通宏映射次数同为四，但其上述 Hilbert 级数之差为
$$\operatorname{Hilb}_{(2,2)}(t)-\operatorname{Hilb}_{(4)}(t)
=\frac{t-t^2}{1-t^5}\ne0.$$
例如一次齐次滤过增量分别为 $2$ 与 $1$。这区分了同总次数、不同相位词的**指定坐标滤过**上同调；没有据此声称一个任意多项式共轭不变量。

## 9. Verification and open scope

已逐项核查：

- 每个无限变量重写分支严格降普通总次数；合流没有依赖不存在的无限 shift-compatible well-order。
- $A_\infty\cong K[x,y]$ 与 $A_N\cong K[\operatorname{Fix}(F^n)]$ 都给出双向映射，而不是仅靠维数猜测。
- 宏相位为 shift-$k$；有限长度 $N=kn$；式中所谓间隙是循环距离，不是少一的空位计数。
- 主定理中所有循环轨道长度为 $n$；scalar binary 临界例外另计稳定子倍数。
- $L_{\mathrm{ph}}(D)$ 不仅是上界，端点乘积给出可达证明；$D=0,1$ 与常数正规项分开。
- bounded-degree primitive 来自宏平移权重的离散凸性；Hilbert 计数使用 $\max(\mu(b),\mu(\tau b))$，不是只数原单项式次数。
- 混合进位制 $\rho$ 是明确的置换；并未在基数不等时误认为它是对合，或把普通次数滤过声明为共轭不变量。
- 几何点值版本、外部优先权与自然篇幅门均未擅自判定。

剩余范围只有两项：一是此单周期 scheme-effective coboundary 结论与定量锐性的一手外部查新；二是在何种明确系数/周期假设下可将 scheme 检测降为纯几何点值检测。它们不影响本文已给的精确代数命题，但不能用本报告自动给正式 Paper29 PASS。

本报告的 SHA256 在保存完成后的交付消息给出，避免自引用哈希。没有改动其它项目文件。
