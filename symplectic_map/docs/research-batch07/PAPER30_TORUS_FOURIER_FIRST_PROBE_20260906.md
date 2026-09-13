# Paper30 T 分支：有限 Fourier 拉回分类与一次小支撑周期检验

日期：2026-09-06。性质：有界作者证明预筛；不是正式候选、独立审查、Route 评价或论文项目。
本次只新增本文件，不修改旧证据，不运行数值实验，不扩写已停止结果。

## Claim

在实二维环面 $\mathbb T^2=\mathbb R^2/\mathbb Z^2$ 上固定
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad F_\kappa=A\circ S_\kappa.
$$
原问题是：固定非零且足够小、使 $F_\kappa$ 为 Anosov 的实参数 $\kappa$，
若复系数有限三角多项式 $g$ 满足
$$
\sum_{j=0}^{n-1}g(F_\kappa^j x)=0
\quad\text{对所有 }n\geq1\text{ 与 }F_\kappa^n x=x,
\tag{P}
$$
是否必存在有限三角多项式 $h$，使 $g=h\circ F_\kappa-h$？
若是否定答案，需要真正满足全部条件 (P) 的严格反例。

本报告只完成首个拉回分类引理，以及下文预先固定七维支撑内的一次周期检验。
任意有限支撑的原问题没有被替换为这两个弱命题。

## Status

原问题：`NOT CURRENTLY JUSTIFIED`，科学状态 `OPEN`；未证明原命题，也未构造反例。

两个明确的弱结论：`PROVABLE AS STATED`，下文给出完整作者证明：

1. 对每个实 $\kappa\neq0$，有限三角多项式 $h$ 的拉回仍有限，当且仅当
   $h=f(q-p)$，其中 $f$ 是一元有限三角多项式。
2. 在固定支撑 $\{0,\pm(1,0),\pm(1,-1),\pm(0,1)\}$ 上，存在一个统一的
   参数邻域，使全部非零实参数的周期核恰好是下述显然两维余边界空间。

主问题在短引理及这一次有限支撑检验后仍未闭合，本分支按短作者结果停止。

## Assumptions

- 所有有限 Fourier 支撑都是 $\mathbb Z^2$ 的有限子集；系数允许为复数。
- 原问题的参数取在给定的 Anosov 小邻域内；不猜测数值双曲阈值。
- 第一项弱结论不需要双曲性或参数小性，只需要 $\kappa\neq0$。
- 第二项弱结论允许将参数邻域进一步缩小；缩小取决于固定的七维空间和五条轨道，
  不依赖该空间内 $g$ 的系数。没有声称此邻域对所有有限支撑统一有效。
- 只进行解析证明，不把线性参数处的检查或有限周期检查本身称为主问题的证明。

## Notation

令 $e_{r,s}(q,p)=\exp(2\pi i(rq+sp))$，$\mathcal T$ 为这些特征标的有限复线性组合空间，
并记 $\sigma_\kappa h=h\circ F_\kappa$。令 $\mathcal T_1$ 为一元有限三角多项式空间。
全部有限原函数所产生的有限余边界记为
$$
\mathcal B_\kappa=\{g\in\mathcal T:\exists h\in\mathcal T,
\ g=\sigma_\kappa h-h\}.
$$
周期核记为 $\mathcal P_\kappa=\{g\in\mathcal T:g\text{ 满足 (P)}\}$。
本文的差分符号固定为 $\sigma_\kappa-1$。

## Proof Strategy

第一步按纵向频率分组。每组恰是一个 Laurent 多项式乘以一个指数因子；
非零纵向频率产生的指数增长不可能被非零 Laurent 多项式消除。
第二步直接确定 $\mathcal B_\kappa$。
第三步只在一个固定七维空间中，写出五个周期泛函的商空间矩阵，利用显式基点计算
和实际周期点的解析延拓，证明该矩阵在一个非零参数邻域内仍可逆。

## Dependency Map

1. 拉回分类依赖 Fourier 系数唯一性、复解析恒等定理和 Laurent 多项式的增长界。
2. 有限余边界分类依赖拉回分类，以及精确恒等式 $(q-p)\circ F_\kappa=q$（模 $1$）。
3. 七维周期结论依赖实解析隐函数定理、一个显式五阶矩阵的可逆性和行列式连续性。
4. 原问题还需要任意有限支撑的周期检测或无限原函数尾部刚性；这一依赖没有证明。

## Proof

### Step 1. 有限拉回的完整分类

**引理 1。** 对实 $\kappa\neq0$ 及 $h\in\mathcal T$，
$$
\sigma_\kappa h\in\mathcal T\quad\Longleftrightarrow\quad
h(q,p)=f(q-p)\text{，某个 }f\in\mathcal T_1.
\tag{1}
$$

写 $h=\sum_{r,s}h_{r,s}e_{r,s}$，其中只有有限项非零。直接代入得到
$$
\sigma_\kappa e_{r,s}
=e_{2r+s,r+s}\exp\!\bigl(2\pi i\kappa(r+s)\sin(2\pi q)\bigr).
\tag{2}
$$
令 $z=\exp(2\pi iq)$、$w=\exp(2\pi ip)$，按 $b=r+s$ 分组：
$$
\sigma_\kappa h
=\sum_b w^b P_b(z)\exp\!\bigl(\pi\kappa b(z-z^{-1})\bigr),\qquad
P_b(z)=\sum_{r+s=b}h_{r,s}z^{2r+s}.
\tag{3}
$$
每个 $P_b$ 都是 Laurent 多项式。固定 $b$ 后，指数 $2r+s=r+b$ 随 $r$ 单射变化，
所以 $P_b=0$ 等价于这一整组原始 Fourier 系数全为零。

若 $\sigma_\kappa h$ 有限，则由沿 $p$ 变量的 Fourier 系数唯一性，对每个 $b$
存在 Laurent 多项式 $Q_b$，在 $|z|=1$ 上满足
$$
P_b(z)\exp\!\bigl(\pi\kappa b(z-z^{-1})\bigr)=Q_b(z).
\tag{4}
$$
两边在 $\mathbb C^*$ 上全纯，因此恒等定理将 (4) 延伸至整个 $\mathbb C^*$。

现在固定 $b\neq0$，设 $c=\pi\kappa b\neq0$，并反设 $P_b\neq0$。
这一论证也容许任意复 $c\neq0$。令 $z=t\overline c/|c|$，其中 $t\to+\infty$；
则 $cz=|c|t$ 且 $|c/z|=|c|/t$。若 $d$ 是 $P_b$ 的最大 Laurent 指数，
其最高项系数非零，故存在常数 $C>0$ 和 $t_0$，使 $t\geq t_0$ 时
$$
|P_b(z)|\geq Ct^d,\qquad
|P_b(z)e^{c(z-z^{-1})}|\geq Ct^d e^{|c|t-|c|/t}.
$$
任意 Laurent 多项式 $Q_b$ 在同一射线上至多按某个非负整数次幂增长；
上式与 (4) 矛盾，包括 $Q_b=0$ 的情形。因此所有 $b\neq0$ 的 $P_b$ 均为零。
剩余频率满足 $r+s=0$，恰得 $h=f(q-p)$。

反向由
$$
F_\kappa(q,p)=(2q+p+\kappa\sin(2\pi q),\ q+p+\kappa\sin(2\pi q))
$$
给出 $(q-p)\circ F_\kappa=q$（模 $1$），所以 $\sigma_\kappa h=f(q)\in\mathcal T$。
这证明 (1)。$\square$

**边界。** 复系数不会改变证明；没有用到系数正性或实值性。
对复 $\kappa\neq0$，若将拉回理解为 Laurent 表达式在复化空间 $(\mathbb C^*)^2$ 上的全纯复合，
同一结论仍成立；此时不声称 $F_\kappa$ 是实环面的 Anosov 映射。
在 $\kappa=0$ 时所有有限三角多项式的线性拉回均有限，故非零假设不可删除。

### Step 2. 全部有限 Fourier 原函数的像

**推论 2。** 对每个实 $\kappa\neq0$，
$$
\mathcal B_\kappa
=\mathcal B:=\{f(q)-f(q-p):f\in\mathcal T_1\}.
\tag{5}
$$
事实上，若 $g=\sigma_\kappa h-h\in\mathcal T$ 且 $h\in\mathcal T$，则
$\sigma_\kappa h=g+h\in\mathcal T$，引理 1 强迫 $h=f(q-p)$，从而得到 (5) 的必要性。
充分性由 Step 1 的精确坐标恒等式给出。$f$ 的常数项不产生余边界；
其余每个非零频率在 $f(q)$ 与 $f(q-p)$ 中位于不同格点，所以原函数在有限类中模常数唯一。

对任意周期点，余边界轨道和望远镜相消，故 $\mathcal B\subseteq\mathcal P_\kappa$。
原问题现在精确化为反向包含 $\mathcal P_\kappa\subseteq\mathcal B$；(5) 本身没有证明它。

### Step 3. 唯一一次固定小支撑周期检验

预先固定本次检验空间
$$
V=\operatorname{span}_{\mathbb C}
\{1,e_{1,0},e_{-1,0},e_{1,-1},e_{-1,1},e_{0,1},e_{0,-1}\}.
\tag{6}
$$
这是唯一检查的支撑，不再增列其他支撑以补充内容。

**命题 3。** 存在 $\varepsilon>0$，使对所有实 $|\kappa|<\varepsilon$ 及 $g\in V$，
下面三项等价：

1. $g$ 满足全部周期条件 (P)。
2. $g$ 在下文明确构造的一条固定轨道和四条三周期轨道上的和均为零。
3. 存在 $a,b\in\mathbb C$，使
   $$g=a(e_{1,0}-e_{1,-1})+b(e_{-1,0}-e_{-1,1}).\tag{7}$$

因此对于这个 $V$，全部足够小的非零实参数均不存在“无限原函数才能产生”的反例。
参数邻域可以与给定 Anosov 邻域相交；命题本身不依赖一般 Livšic 定理。

**3.1 实际周期轨道。** 原点在所有参数下都固定。在 $\kappa=0$ 时，
取 $u=(1/4,0)$、$v=(0,1/4)$ 及其负点，得到四条互不相交的最小三周期轨道：
$$
\begin{aligned}
\mathcal O_u&=\{(1/4,0),(1/2,1/4),(1/4,3/4)\},\\
\mathcal O_v&=\{(0,1/4),(1/4,1/4),(3/4,1/2)\},\\
\mathcal O_{-u}&=-\mathcal O_u,\qquad
\mathcal O_{-v}=-\mathcal O_v.
\end{aligned}
\tag{8}
$$
令 $\widetilde F_\kappa$ 是公式所定义的实平面提升。对 $z\in\{u,-u,v,-v\}$，
记 $\ell_z=(A^3-I)z\in\mathbb Z^2$，并考察
$$
\widetilde F_\kappa^3(x)-x-\ell_z=0.
\tag{9}
$$
在 $(\kappa,x)=(0,z)$ 处，该式对 $x$ 的导数是
$$
A^3-I=\begin{pmatrix}12&8\\8&4\end{pmatrix},\qquad\det(A^3-I)=-16\neq0.
$$
实解析隐函数定理给出真实解 $x_z(\kappa)$，满足 $x_z(0)=z$，且在某个共同参数邻域内
$F_\kappa^3x_z(\kappa)=x_z(\kappa)$（模 $\mathbb Z^2$）。
缩小邻域后，(8) 中十二个不同点的延拓仍然互不相同，故四条轨道仍互不相交且最小周期为三。
这不是将线性轨道坐标直接代入非线性映射；使用的是 (9) 的实际解析解。

**3.2 周期泛函降到五维商。** 写
$$
g=C+a e_{1,0}+b e_{-1,0}+c e_{1,-1}+d e_{-1,1}+u_0e_{0,1}+v_0e_{0,-1},
\qquad \alpha=a+c,\quad\beta=b+d.
$$
由 $e_{1,-1}\circ F_\kappa=e_{1,0}$ 和负频率的同一恒等式，
每条实际周期轨道上这两对函数分别有相同的轨道和。
五个轨道条件因此是向量 $(C,\alpha,\beta,u_0,v_0)$ 的五个线性条件，
形成一个实解析参数矩阵 $M(\kappa)$。

按原点、$u$、$-u$、$v$、$-v$ 的顺序，(8) 给出精确矩阵
$$
M(0)=\begin{pmatrix}
1&1&1&1&1\\
3&-1+2i&-1-2i&1&1\\
3&-1-2i&-1+2i&1&1\\
3&1&1&-1+2i&-1-2i\\
3&1&1&-1-2i&-1+2i
\end{pmatrix}.
\tag{10}
$$
此矩阵可逆，证明如下。齐次方程的第二行减第三行给出 $\alpha=\beta$；
第四行减第五行给出 $u_0=v_0$。第二行和第四行于是变成
$$
3C-2\alpha+2u_0=0,\qquad3C+2\alpha-2u_0=0.
$$
相加得 $C=0$，再得 $\alpha=u_0$；第一行给出 $4\alpha=0$。
故五个未知量全为零。

由于 $M(\kappa)$ 使用实际延拓轨道而且依赖参数连续，$\det M(0)\neq0$ 保证存在
$\varepsilon>0$，使整个实区间 $|\kappa|<\varepsilon$ 上 $M(\kappa)$ 均可逆。
因此第二项强迫 $C=u_0=v_0=0$、$c=-a$、$d=-b$，即 (7)。
第三项由精确坐标恒等式给出有限原函数 $h=a e_{1,-1}+b e_{-1,1}$，
这一恒等式也适用于 $\kappa=0$，所以望远镜相消证明第一项。
第一项包含第二项，三项等价全部证明。$\square$

**实值情形。** 如果要求 $g$ 实值，(7) 中需且只需 $b=\overline a$；
相应 $h$ 也实值。复系数证明先给出较完整的线性空间结论，不依赖这一附加对称性。

## Corrections or Missing Assumptions

没有修改原命题的量词来宣称成功。精确缺失义务是：对一个固定的足够小非零实参数，
证明
$$
\mathcal T\cap\bigcap_{n\geq1}\bigcap_{x\in\operatorname{Fix}(F_\kappa^n)}
\ker\!\left[g\longmapsto\sum_{j=0}^{n-1}g(F_\kappa^j x)\right]
\subseteq\{f(q)-f(q-p):f\in\mathcal T_1\}.
\tag{11}
$$
或者，给出 (11) 的严格反例，即一个不在右侧、但满足全部真实周期条件的有限 $g$。
两项均未完成。

若尝试从连续或解析原函数出发，所需的新步骤是控制该原函数可能存在的无限 Fourier 尾部，
证明其差分有限会强迫原函数有限（至多差一个不变函数）。引理 1 不能应用于无限 Fourier
原函数，因为 (3) 的 $P_b$ 那时未必是 Laurent 多项式；本报告的增长矛盾不再成立。

## Open Risks

- 命题 3 只处理 (6) 这一固定空间，不能对所有有限支撑取交后声称参数邻域仍非空。
- 五条轨道在 $V$ 上足够，不意味着它们或任何固定有限组轨道检测整个 $\mathcal T$。
- $\kappa=0$ 的满秩计算在这里仅是实际非线性延拓定理的基点；
  没有把线性 cat map 的一般 Fourier 余边界结构当作非线性结论。
- 一般 Livšic 存在性或连续、光滑、解析正则性不能替代有限 Fourier 支撑性。
  本证明未调用这些定理，也未作其解析适用条件的额外断言。
- 本次未新增公开文献检索，不声称完整查新或世界首次；标准 Fourier 分组、隐函数定理及
  固定有限秩的稳定性不应被包装成新的主要研究贡献。

## 有界预筛处置与核验记录

已读取工作区 `AGENTS.md`、`docs/WORKFLOW.md`、`BATCH_07_CONTEXT.md`、
`proof-writer/SKILL.md` 全文及 portfolio 第 8 节。证明技能要求使本报告显式保留原问题 `OPEN`，
而将确实证明的拉回分类及七维检验单列；不把弱结论冒充主命题。

核验为上述逐式解析计算：拉回频率、指数系数、分组单射、射线增长、四条实际周期延拓、
矩阵 (10) 的齐次消元、全部量词及实值边界。未进行数值采样或计算实验。

实际新增内容属于短作者结果：首个引理闭合，一次固定支撑周期检验闭合，
但关键的任意支撑刚性尚缺。至此停止；不增加支撑表，不接其他候选结果，不创建正式项目，
不触发容量评分、Route 评分或论文计数。
