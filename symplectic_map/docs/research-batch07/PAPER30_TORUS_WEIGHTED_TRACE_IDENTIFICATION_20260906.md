# Paper30 T 分支：参数加权空间的固定点迹与真实 Ruelle 谱识别

日期：2026-09-06。性质：新的有界作者证明。
只补足已证明核性的加权算子与实际面积动力学的谱识别；
不复查核性、不做实验，也不评价候选分数或论文容量。

## Claim

令 $\mathbb T^2=\mathbb R^2/\mathbb Z^2$，面积 $dx$ 归一为一，并令
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad
F_\kappa=A\circ S_\kappa,\qquad t=\pi\kappa.
\tag{1}
$$
对 $m=(r,s)\in\mathbb Z^2$，定义
$$
E_m(x)=e^{2\pi i m\cdot x},\qquad
\omega(m)=|s|-|r+s|.
\tag{2}
$$
固定非零实数 $t$ 时，令 $H_t$ 为三角多项式在以下范数下的完备化：
$$
\left\|\sum_m h_mE_m\right\|_{H_t}^2
=\sum_m |h_m|^2|t|^{-2\omega(m)}.
\tag{3}
$$
于是 $f_m=t^{\omega(m)}E_m$ 为正交归一基，$f_0=1$。

**定理。** 存在 $t_A>0$，使对每个实数 $t$ 满足 $0<|t|<t_A$，
三角多项式上的实际拉回 $h\mapsto h\circ F_{t/\pi}$ 延拓为
$H_t$ 上的迹类算子 $C_t$，并对每个整数 $n\ge1$ 满足
$$
\operatorname{Tr}_{H_t}(C_t^n)
=\sum_{x\in\operatorname{Fix}(F_{t/\pi}^n)}
\frac1{|\det(D_xF_{t/\pi}^n-I)|}.
\tag{4}
$$
其非零谱连同代数重数，恰等于 Faure–Roy 实现中的面积
Ruelle–Pollicott 共振。更精确地，若 $R_t$ 是下文定义的
Faure–Roy 迹类实现，则整个 Fredholm 行列式满足
$$
\det_{H_t}(I-zC_t)=\det(I-zR_t)
=(1-z)\det_{\ell^2(\mathbb Z^2\setminus\{0\})}(I-ztB(t)),
\qquad z\in\mathbb C.
\tag{5}
$$
这里 $B(t)$ 是已另证核性的矩阵，具体定义见 Assumptions。
因此 $tB(t)$ 的非零特征值，按代数重数计，是剔除常数块的一份
特征值 $1$ 后的真实共振。还可选取 $0<t_*\le t_A$，使
$0<|t|<t_*$ 时常数共振 $1$ 为代数单根，余下共振严格位于单位圆内。

## Status

`PROVABLE AS STATED`，其中“真实谱识别”明确指充分小的非零**实参数**。
原命题在这个量词范围内成立，不需要把形式对角变换当作
$L^2$ 上的有界相似。$t=0$ 的 $B(0)$ 属于另一个解析延拓问题，
不是本定理中 $H_t$ 的一个已定义参数值。

## Assumptions

- 接受已完成的局部输入
  [重加权核性证明](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md)，
  不在本文件重新证明：对 $\Lambda=\mathbb Z^2\setminus\{0\}$，
  $B(t)$ 在固定 $\ell^2(\Lambda)$ 上按迹范数全纯，半径
  $r_0=1/256$；在 $|t|\le r_0$ 上有 $\|B(t)\|_1<M$，其中 $M=23041$。
  其矩阵为
  $$
  B(t)_{n,m}=t^{\omega(m)-\omega(n)-1}
  [z^k]\exp\{t(r+s)(z-z^{-1})\},\qquad
  n=(2r+s+k,r+s),
  \tag{6}
  $$
  其他项为零，且只使用 $m,n\in\Lambda$。
- 使用 Faure–Roy 对 $C^1$ 足够小的实解析双曲环面扰动的迹类实现与固定点迹公式。
  定理的具体适用与页码列于 Step 1，不假设本空间与其空间间存在有界相似。
- $t$ 固定为非零实数；涉及热极限时，先固定这个 $t$ 和一个整数 $n\ge1$。
  本证明不交换热参数、动力学时间和耦合参数的三个极限。

## Notation

- $H_t^0$ 为零频率系数为零的闭子空间，$H_t=\mathbb C1\oplus H_t^0$。
- $\|m\|_1=|r|+|s|$，$|m|^2=r^2+s^2$。
- $\mathcal E$ 为在 $\mathbb C^2$ 上整解析且对 $\mathbb Z^2$ 周期的函数，
  视其在实环面上的限制；这是证明复合关系所用的核心，而非对任意 $H_t$ 元素作逐点解释。
- $\|T\|_1$ 表示迹范数；$\det(I-zT)$ 表示迹类算子的 Fredholm 行列式。
- $\mathcal R(F)$ 表示 Faure–Roy 拉回约定下的非零共振多重集。

## Proof Strategy

先在整解析周期核心上证明加权矩阵的全部整数次幂就是实际迭代拉回。
再用在 $H_t$ 中有界自伴的热对角算子作右正则化，
把算子迹写成实环面上的正核积分；逆函数定理将其极限定位到有限个非退化固定点。
最后与另一个已识别共振的迹类实现比较所有幂迹，得到整个行列式恒等。

## Dependency Map

1. 已接受的核性输入及单步 Fourier 展开给出 $C_t=1\oplus tB(t)$。
2. 整解析 Fourier 衰减、系数泛函连续性及实环面上的一致收敛，给出整数次迭代识别。
3. 热对角自伴性、强收敛及有限秩逼近，给出右乘正则化的迹范数收敛。
4. Poisson 求和、Anosov 非退化固定点及局部换元，给出本空间的固定点迹公式。
5. Faure–Roy 命题 9 与 Fredholm 行列式的幂迹展开，给出谱与代数重数识别。

## Proof

### Step 1. 实动力学范围与所用的 Faure–Roy 结果

$F_\kappa$ 是面积保持的实解析微分同胚，其提升为
$$
F_\kappa(q,p)=
(2q+p+\kappa\sin(2\pi q),\ q+p+\kappa\sin(2\pi q)).
\tag{7}
$$
$S_\kappa^{-1}=S_{-\kappa}$，$\det DS_\kappa=1$，$\det A=1$，
验证了上述微分同胚性和面积保持性。
矩阵 $A$ 的特征值是 $(3\pm\sqrt5)/2$，故其双曲。
(7) 中相对 $A$ 的周期解析扰动在 $C^1$ 范数下随 $\kappa\to0$ 趋零。
由 Anosov 结构稳定性和 Faure–Roy 定理 6，存在 $\kappa_{\mathrm{FR}}>0$，
使对每个实 $|\kappa|<\kappa_{\mathrm{FR}}$，$F_\kappa$ 是 Anosov，
且存在其拉回的 Faure–Roy 迹类实现 $R_{\pi\kappa}$。
其非零谱就是他们定义的 RP 共振，命题 9 对所有正整数给出 (4) 的右侧作为幂迹。
本文取
$$
t_A=\min\{r_0,\pi\kappa_{\mathrm{FR}}\}.
\tag{8}
$$

准确原始来源为 F. Faure and N. Roy,
*Ruelle–Pollicott resonances for real analytic hyperbolic maps*,
Nonlinearity **19** (2006), 1233–1252：
§2.2 的模型在印刷页 1238；定理 6 及相关性解释在页 1239
（PDF 第 7 页）；定理 7 在同页明确把非零谱称为 RP 共振；
定理 8 的零噪声谱极限及命题 9 的固定点迹在页 1240
（PDF 第 8 页）。本文直接使用定理 6 和命题 9；
定理 8 确认其噪声谱含义，但不承担下文两个空间之间的证明桥梁。
[作者全文及所述页码](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf)

约定也一致：原文的算子为 $h\mapsto h\circ F$。
本文的 $dx$ 是不变面积，故这是针对同一面积相关函数的谱，
不发生以逆映射约定替换特征值的问题。
还可直接核对原文式 (10)：其例子是
$S_\kappa A$，参数 $\delta=2\pi\kappa$，且
$A^{-1}F_\kappa A=S_\kappa A$。
不过这里适用的是一般定理，不需要由该共轭搬运本空间。

### Step 2. 构造加权延拓，并说明它不是已证明的 $L^2$ 相似

对 $m=(r,s)$，把 (7) 代入 $E_m$，并用 $t=\pi\kappa$，得到
$$
E_m\circ F_\kappa
=E_{(2r+s,r+s)}
\exp\{t(r+s)(e^{2\pi iq}-e^{-2\pi iq})\}.
\tag{9}
$$
它的 Fourier 系数正是 (6) 中的 Laurent 系数。
在正交基 $f_m=t^{\omega(m)}E_m$ 中，输入与输出的权重比例给出
$tB(t)$。常数固定；又因面积不变，对每个 $m\ne0$，
$$
\int_{\mathbb T^2}E_m(F_\kappa x)\,dx
=\int_{\mathbb T^2}E_m(x)\,dx=0.
\tag{10}
$$
所以不存在常数与零均值块之间的耦合。
由已接受的核性，(9) 在三角多项式上的作用唯一延拓为
$$
C_t=1\oplus tB(t):H_t\longrightarrow H_t,
\tag{11}
$$
它是迹类，且每个正整数次幂亦为迹类。

(11) 是从正交基与矩阵的迹范数收敛构造出的算子。
尽管形式上可写 $E_m\mapsto t^{\omega(m)}E_m$，
该对角变换在 $L^2$ 上一般不有界；此处和后续证明均不由其推断等谱。

### Step 3. 整解析核心确保全部幂等于实际迭代

先证 $\mathcal E\subset H_t$。
对 $h\in\mathcal E$ 与任意 $\rho>0$，令
$$
M_\rho(h)=\sup\{|h(x+iy)|:
x\in[0,1]^2,\ |y_j|\le\rho\ (j=1,2)\}<\infty.
$$
逐坐标平移 Fourier 系数的积分路径到
$y_j=-\rho\operatorname{sgn}(m_j)$，利用整解析性与周期边界抵消，得到
$$
|h_m|\le M_\rho(h)e^{-2\pi\rho\|m\|_1}.
\tag{12}
$$
反三角不等式给出
$$
|\omega(m)|=\big||s|-|r+s|\big|\le|r|\le\|m\|_1.
\tag{13}
$$
固定 $L=|\log|t||$，选择 $2\pi\rho>L$，则
$$
|h_m|^2|t|^{-2\omega(m)}
\le M_\rho(h)^2e^{-2(2\pi\rho-L)\|m\|_1},
\tag{14}
$$
右侧在 $\mathbb Z^2$ 上可和。因此 Fourier 截断
$h^{(N)}=\sum_{\|m\|_1\le N}h_mE_m$ 同时在 $H_t$ 中和实环面上一致收敛到 $h$。
三角多项式属于 $\mathcal E$ 且在 $H_t$ 中稠密。

提升 (7) 在 $\mathbb C^2$ 上整解析，并满足
$F_\kappa(z+\ell)=F_\kappa(z)+A\ell$，$\ell\in\mathbb Z^2$。
因为 $A\ell\in\mathbb Z^2$，对每个 $h\in\mathcal E$，
$h\circ F_\kappa$ 仍属于 $\mathcal E$，从而也属于 $H_t$。
这里即使复方向上的增长很快，也不影响任意固定条带上的有限常数 $M_\rho$。

对固定 $j\in\mathbb Z^2$，在 $H_t$ 的 Fourier 系数解释下有
$$
|g_j|\le |t|^{\omega(j)}\|g\|_{H_t}.
\tag{15}
$$
所以每个系数泛函连续。由 $C_t$ 的有界性，
$C_th^{(N)}\to C_th$ 于 $H_t$，其各 Fourier 系数收敛。
另一方面，因 $F_\kappa$ 把实环面映到实环面，
$h^{(N)}\circ F_\kappa\to h\circ F_\kappa$ 在实环面上一致收敛，
故其 Fourier 系数收敛到实际复合的系数。
对每个 $N$，Step 2 已将这两个有限输入所产生的输出识别为同一个 Fourier 序列。
取极限后得到
$$
C_th=h\circ F_\kappa\quad(h\in\mathcal E),
\tag{16}
$$
等式是在 $H_t$ 中、亦在整函数的 Fourier 序列意义下成立。
由于 $\mathcal E$ 在实际复合下保持，归纳得到
$$
C_t^nE_m=E_m\circ F_\kappa^n
\quad(m\in\mathbb Z^2,\ n\ge1).
\tag{17}
$$
这一步没有把任意 $H_t$ 元素视为可逐点评价的函数；
它只在足够大的不变整解析核心上建立迭代恒等式。

### Step 4. 热对角右正则化在本空间中的迹极限

对 $\varepsilon>0$ 定义
$$
P_\varepsilon f_m=e^{-\varepsilon|m|^2}f_m.
\tag{18}
$$
在正交基 $f_m$ 下，$P_\varepsilon$ 是自伴收缩，且逐坐标趋于一；
由 $\ell^2$ 支配收敛，$P_\varepsilon\to I$ 强收敛。

对任意迹类 $T$，有
$$
\|T(P_\varepsilon-I)\|_1\longrightarrow0.
\tag{19}
$$
完整理由如下。先以有限秩 $K$ 在迹范数中逼近 $T$；
$\|(T-K)(P_\varepsilon-I)\|_1\le2\|T-K\|_1$。
将 $K$ 写成有限个秩一项 $u\otimes v^*$ 之和。
自伴性给出
$(u\otimes v^*)(P_\varepsilon-I)
=u\otimes((P_\varepsilon-I)v)^*$，其迹范数等于
$\|u\|\,\|(P_\varepsilon-I)v\|\to0$。
先固定逼近误差再令 $\varepsilon\downarrow0$，最后令误差趋零，即得 (19)。
特别地，对固定 $n\ge1$，
$$
\operatorname{Tr}(C_t^nP_\varepsilon)
\longrightarrow\operatorname{Tr}(C_t^n).
\tag{20}
$$
此处右乘需要上面的自伴性论证；没有单从强收敛直接推断迹范数收敛。

### Step 5. 对角权重消去与 Poisson 核表示

由 (17)，$C_t^nf_m=t^{\omega(m)}E_m\circ F_\kappa^n$。
计算 $f_m$ 方向的坐标时输出权重恰为同一个 $t^{\omega(m)}$，故对角项为
$$
\langle f_m,C_t^nf_m\rangle_{H_t}
=\int_{\mathbb T^2}e^{2\pi i m\cdot(F_\kappa^n x-x)}\,dx.
\tag{21}
$$
内积在第二个变量线性；指数与积分不依赖提升的选择。
对实 $\kappa$，积分的模至多为一。因此迹的正交基展开与绝对可和性给出
$$
\operatorname{Tr}(C_t^nP_\varepsilon)
=\sum_{m\in\mathbb Z^2}e^{-\varepsilon|m|^2}
\int_{\mathbb T^2}e^{2\pi i m\cdot(F_\kappa^n x-x)}\,dx
=\int_{\mathbb T^2}K_\varepsilon(G_n(x))\,dx,
\tag{22}
$$
其中 $G_n(x)=F_\kappa^n x-x$ 是取值于 $\mathbb T^2$ 的光滑映射，且
$$
K_\varepsilon(y)=\sum_{m\in\mathbb Z^2}
e^{-\varepsilon|m|^2}e^{2\pi i m\cdot y}
=\frac\pi\varepsilon\sum_{\ell\in\mathbb Z^2}
\exp\!\left(-\frac{\pi^2|y-\ell|^2}{\varepsilon}\right).
\tag{23}
$$
第一个级数由 $\sum_me^{-\varepsilon|m|^2}<\infty$ 一致绝对收敛，
故 (22) 的求和与积分可以交换；第二个等号是二维 Gaussian 的 Poisson 求和式。
因此 $K_\varepsilon\ge0$、$\int_{\mathbb T^2}K_\varepsilon=1$，
且当 $\varepsilon\downarrow0$ 时它在离开零点的任意紧集上一致趋零。
后者也可从 (23) 看出：若到 $\mathbb Z^2$ 的距离至少为 $d>0$，
把指数衰减的一半提出，余下格点 Gaussian 和在 $0<\varepsilon\le1$ 时一致有界，
得到 $O(\varepsilon^{-1}e^{-\pi^2d^2/(2\varepsilon)})$。
故 $K_\varepsilon$ 是集中于零点的正近似恒等核。

### Step 6. 固定点处的局部换元与迹公式

固定 $n\ge1$。Anosov 性使每个 $p\in\operatorname{Fix}(F_\kappa^n)$
的 $D_pF_\kappa^n$ 在稳定和不稳定方向上的特征值模分别小于与大于一，
所以
$$
\det DG_n(p)=\det(D_pF_\kappa^n-I)\ne0.
\tag{24}
$$
逆函数定理说明每个这样的零点孤立。零点集闭且环面紧，故它有限：
若无限，则有聚点；该聚点仍是零点，违背其孤立性。

若零点集为空，紧性给出 $G_n(\mathbb T^2)$ 与零点的正距离，
(22)—(23) 的极限为零，正是空和 (4)。
否则记零点为 $p_1,\ldots,p_J$。
由逆函数定理及补集紧性，可以选择零点附近一个小球 $V\subset\mathbb T^2$，
使 $G_n^{-1}(V)$ 恰为互不相交的 $U_1,\ldots,U_J$ 之并，
各 $G_n:U_j\to V$ 都是微分同胚，且闭球包含在每个局部逆映射的定义域内。
具体地，先为每个 $p_j$ 取互不相交的局部逆邻域，
它们补集的像到零点有正距离，再将共同像球缩到该距离之内。

记逆分支为 $x_j:V\to U_j$，定义连续且可延至 $\overline V$ 的函数
$$
a_j(y)=\frac1{|\det DG_n(x_j(y))|}.
$$
实变量换元给出
$$
\int_{U_j}K_\varepsilon(G_n(x))\,dx
=\int_V K_\varepsilon(y)a_j(y)\,dy
\longrightarrow a_j(0)
=\frac1{|\det(D_{p_j}F_\kappa^n-I)|}.
\tag{25}
$$
这里极限来自 $a_j$ 在零点连续、$K_\varepsilon$ 非负且总质量为一，
以及 $V$ 外的质量趋零。
在 $\mathbb T^2\setminus G_n^{-1}(V)$ 上，$G_n(x)$ 离零点有统一正距离，
故剩余积分由 (23) 一致趋零。
将 (25) 相加，结合 (20) 与 (22)，得到 (4)。

### Step 7. 相同幂迹推出整个行列式及重数相同

现在仍固定一个实 $0<|t|<t_A$。
Step 6 与 Faure–Roy 命题 9 给出
$$
\operatorname{Tr}_{H_t}(C_t^n)=\operatorname{Tr}(R_t^n)
\quad\text{对所有整数 }n\ge1.
\tag{26}
$$
两侧算子都是迹类。迹类 Fredholm 行列式在 $z\in\mathbb C$ 上为整函数，
且在 $|z|$ 充分小时满足
$$
\det(I-zT)=
\exp\!\left(-\sum_{n=1}^{\infty}\frac{z^n}{n}\operatorname{Tr}(T^n)\right).
\tag{27}
$$
可取 $|z|<1/\max\{1,\|C_t\|,\|R_t\|\}$，
使两套幂迹展开都收敛。(26) 因而给出两行列式在零点邻域相同，
整函数恒等定理将等式延伸到全部复平面。
再由正交直和 (11) 的 Fredholm 行列式乘法得到完整的 (5)。

迹类算子的非零谱由孤立有限代数重数的特征值组成，
且 $\lambda\ne0$ 的代数重数等于
$\det(I-zT)$ 在 $z=\lambda^{-1}$ 的零点阶数。
所以 (5) 精确识别非零谱及其全部代数重数，而非仅识别谱半径或若干有限层系数。
零特征值本身不由此行列式识别，本定理也没有这样的主张。

最后若要在不另外调用混合性定理的情况下保证常数谱独立为单根，取
$$
t_*=\min\{t_A,1/(2M)\},\qquad M=23041.
\tag{28}
$$
则 $0<|t|<t_*$ 时，$\|tB(t)\|\le|t|\|B(t)\|_1<1/2$。
因此零均值块没有特征值 $1$，常数块提供唯一的一份代数单根 $1$。
其余非零共振正是 $tB(t)$ 的非零特征值，且模小于 $1/2$。
所选半径只是方便的充分界，不宣称最优。至此定理得证。$\square$

## Corrections or Missing Assumptions

- 不能以在 $L^2$ 上未经证明有界的对角变换直接宣告等谱；
  本证明由实际迭代、固定点迹及行列式完成替代桥梁，没有增加这种假设。
- “充分小”包含 FR 的真实 Anosov/迹类适用邻域和已接受的核性半径，
  具体量词是 (8)。若还要直接用粗范数保证常数谱单根，则用 (28)。
- 负实 $t$ 的所有 $t^{\omega(m)}$ 都是无歧义的非零整数幂，
  正交归一性由 $|t|$ 范数保证，对角权重仍精确消去。因此证明覆盖两侧实参数。

## Open Risks

- 在所述输入定理成立的前提下，本文件范围内没有未闭合的证明步骤。
- 复参数虽在 $B(t)$ 的解析核性范围内，但 $F_{t/\pi}$ 不再是这里所用的实面积映射；
  本文件不向复参数声称固定点正核证明或物理 Ruelle 谱识别。
- $t=0$ 时权重空间 (3) 未定义；不能把 (5) 当作关于该物理空间的零参数恒等式。
  使用 $B(0)$ 做后续解析扰动是另一项已经明确分离的研究任务。
- 本文只完成谱多重集的识别，没有声称两个 Hilbert 实现之间存在有界共轭，
  也没有声称任意加权空间元素都可作为普通函数逐点评价。
