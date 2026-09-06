# 全复周期 Hénon 一元坐标多项式权重：有限状态闭合合同

日期：2026-09-05。只写本目录；不分配新编号，不写 TeX、不改旧包、
共享索引、已封存研究快照或 Git。本次实际深入 **一个** 非线性子类型，
未为满足上限而追加另外两个条目。

## 选择结论与实际级别

**建议保留一个合同，交独立准入审查；不是已完成论文或新颖性认证。**
对象是任意次数的复多项式 Hénon 映射，逐步权重限定为任意固定的一元
多项式坐标权重 $q(\pi_1P)$；问题是其全复周期、带符号稳定性迹，是否在所有周期上由同一有限矩阵
精确闭合。这里的剩余增量不是低次数留数消去，也不是有限周期表，
而是 **矩阵大小只依赖映射次数和权重次数、不依赖周期长度** 的构造定理。

下文给出完整作者证明。`proof-writer` 状态为 **PROVABLE AS STATED**，
其中“全参数”使用明确的全局留数延伸；在抛物等退化参数上，普通的
简单固定点分母和式本来没有定义，绝不把它标成有限的普通和式。
这个状态是作者的证明判断，最终准入与独立审查由协调者裁定。

廉价决定性检验已执行：

- 七个具体映射／权重，$d=2,3,4$、$n\le5$，27 个有限矩阵迹与循环方程
  Gröbner 正规形留数比较一致；包含一个抛物固定点参数。
- 两个非退化例用商代数乘法矩阵的 $\operatorname{Tr}(m_gm_J^{-1})$
  重建加权根和，并与正规形留数比较。
- 以导数和 Jacobian 参数为不定元，核对 $n=1,\ldots,6$ 的 Hill 符号恒等式。
- 六个自由系数的二次映射／二次权重矩阵给出四次行列式的显式因式分解；
  是从矩阵直接算出，不是根据短迹序列拟合。
- 从字面映射重建一个历史二周期反例；旧包未修改，见末节。

执行脚本：[exact_check.py](exact_check.py)。有限证据不证明全周期定理；
全周期量词由下述有界流量引理承担。没有 GPU、外部模型或论文构建。

## 1. 冻结对象、量词与成功／淘汰边界

令 $d\ge2$，$m\ge0$，取任意首一多项式

$$
p(X)=X^d+\sum_{j=0}^{d-1}p_jX^j,\qquad
q(X)=\sum_{j=0}^{m}q_jX^j,\qquad a\in\mathbb C^*.
$$

允许 $q$ 的实际次数小于 $m$，也允许 $q=0$。固定真正非线性的可逆映射

$$H_{p,a}(x,y)=(p(x)-ay,x)\quad\hbox{on }\mathbb C^2.$$

时钟始终是原始整数迭代。没有选取实 repeller、换时钟、选取部分周期、
取绝对稳定性权重或把不同时间的映射串成非自治系统。

对 $n\ge1$，令所有下标模 $n$，定义循环方程

$$F_{n,i}(\mathbf x)=p(x_i)-x_{i+1}-a x_{i-1},\quad 0\le i<n.$$

重复的邻项必须相加：$n=1$ 时是 $p(x_0)-(1+a)x_0$，$n=2$ 时是
$p(x_0)-(1+a)x_1$ 和 $p(x_1)-(1+a)x_0$。
循环方程的一个解对应固定点 $(x_0,x_{n-1})\in\operatorname{Fix}(H^n)$；
固定点按带起点的集合计数，不把本原周期商当作固定点集合。

在 $\operatorname{Fix}(H^n)$ 全部非退化时，定义

$$
\tau_n(p,a,q)=\sum_{P\in\operatorname{Fix}(H^n)}
\frac{\prod_{i=0}^{n-1}q(\pi_1H^iP)}{\det(I-DH^n(P))}.
\tag{1}
$$

在任意参数处，采用同一式的全局留数延伸，作为全参数对象的定义：

$$
\tau_n(p,a,q):=-\operatorname{Res}_{F_n}
\left(\prod_{i=0}^{n-1}q(x_i)\right).
\tag{2}
$$

这里 $\operatorname{Res}_{F_n}$ 是所有有限共同零点的 Grothendieck 局部
留数之和，分母次序固定为 $F_{n,0},\ldots,F_{n,n-1}$，分子微分形式次序
为 $dx_0\wedge\cdots\wedge dx_{n-1}$。退化点并非被删除；它们使用高阶
局部留数。式 (2) 不宣称是一个自然 Banach 空间 Perron 算子的迹。

冻结生成函数约定为

$$D_{p,a,q}(z)=\exp\left(-\sum_{n\ge1}\frac{\tau_n(p,a,q)}n z^n\right).\tag{3}$$

这是原点的形式幂级数，结论将同时给出一个实际解析 germ。
定义

$$
M=\max(0,m-d+1),\quad
B=\left\lfloor\frac{M(d+1)}{(d-1)^2}\right\rfloor,
\qquad\mathcal E=\{0,\ldots,B\}^2.
\tag{4}
$$

**成功门槛。** 构造一个仅依赖 $p,a,q,d,m$、大小 $(B+1)^2$ 的矩阵 $W$，
证明每个 $n\ge1$ 都有 $\tau_n=-\operatorname{Tr}W^n$，包括式 (2) 的全参数
延伸，因而 $D=\det(I-zW)^{-1}$。给出不是低阶 vanishing 的显式例，
同时准确说明其物理／算术边界。

**决定性淘汰条件。** 若周期无关界不能成立、循环张量在 $n=1,2$ 失配、
退化点只靠删去处理，或直接先前定理已覆盖这个周期无关有限矩阵合同，
则不准入。若最后只剩 Euler–Jacobi 消去或历史程序纠错，也不计作新论文。

## 2. 定理：任意次数／任意一元坐标多项式权重的有限闭合

对 $k,e\ge0$，定义纯代数系数

$$c_{k,e}(p,q)=[X^{-1}]\frac{q(X)X^k}{p(X)^{e+1}},\tag{5}$$

其中 $[X^{-1}]$ 指在无穷远的 Laurent 展开中取系数；它不是在 $0$ 展开。
对边状态 $(r,\ell),(s,v)\in\mathcal E$，置

$$
W_{(r,\ell),(s,v)}=
\binom{\ell+s}{\ell}a^{\ell}\,c_{r+v,\ell+s}(p,q).
\tag{6}
$$

**定理。** 对上述全部参数与每个 $n\ge1$，式 (2) 有定义，且

$$
\boxed{\tau_n(p,a,q)=-\operatorname{Tr}W^n,\qquad
D_{p,a,q}(z)=\frac1{\det(I-zW)}.}
\tag{7}
$$

$W$ 的系数属于 $\mathbb Z[p_0,\ldots,p_{d-1},a,q_0,\ldots,q_m]$。
式 (7) 与任意参数专门化相容；固定权重实际次数下降时不必重新证明。

### 假设与依赖图

1. $F_{n,i}$ 的最高齐次项为 $x_i^d$：无无穷远共同零点、有限完全交、
   全局留数正规形和系数抽取采用经典定理 [S1]。
2. 字面 Hénon 线性化与循环 Jacobian 的负号采用标量循环 Hill 恒等式
   [S2]；小周期单独展开，不能忽略邻项重合。
3. 同一大圆上的几何级数把留数写为邻接整数指数流的循环配分和。
4. **本合同新增的核心引理**：所有非零贡献的指数流有式 (4) 的逐点界，
   而不只是随 $n$ 增长的总次数界。
5. 有限边状态的闭合乘积就是同一个 $W$ 的矩阵迹，最后使用有限矩阵的
   形式恒等式 $-\log\det(I-zW)=\sum\operatorname{Tr}(W^n)z^n/n$。

### 证明第 1 步：有限零点、退化参数与经典留数输入

按总次数排序，$\operatorname{in}(F_{n,i})=x_i^d$，这些首项两两互素，
所以 $F_{n,i}$ 构成 Gröbner 基；标准单项式为
$\prod_i x_i^{j_i}$，$0\le j_i<d$。商代数维数为 $d^n$。
特别地，每个参数都有有限零维完全交，可能带非约化重数，但没有共同
无穷远零点，因为全部最高齐次项消失只可能 $x_0=\cdots=x_{n-1}=0$。

经典全局留数正规形定理 [S1, Lemma 4.2] 在这里给出

$$
\operatorname{Res}_{F_n}(g)=
[x_0^{d-1}\cdots x_{n-1}^{d-1}]\operatorname{NF}_{F_n}(g).
\tag{8}
$$

首一正规形的约化不除以任何参数，因此式 (8) 是参数的多项式，
在退化参数上仍有定义。等价的系数抽取／全局留数展开是
[S1, Theorem 2.3] 的已有输入，不主张为新结果。

### 证明第 2 步：循环 Jacobian 与返回稳定性分母

在循环点设 $v_i=p'(x_i)$，并写

$$A_i=\begin{pmatrix}v_i&-a\\1&0\end{pmatrix},\qquad
\mathcal M_n=A_{n-1}\cdots A_0=DH^n(x_0,x_{n-1}).$$

循环 Jacobian $J_n=DF_n$ 具有对角元 $v_i$、向右邻项 $-1$ 和向左邻项
$-a$。$n\ge3$ 时，标量循环三对角行列式公式
[S2, equation (1)] 代入这些邻项得

$$
\det J_n=\operatorname{Tr}\mathcal M_n-1-a^n
=-\det(I-\mathcal M_n),
\tag{9}
$$

末步使用 $\det\mathcal M_n=a^n$ 和二阶行列式恒等式。
两个短周期直接给出

$$
\det J_1=v_0-1-a,
\qquad
\det J_2=v_0v_1-(1+a)^2,
$$

而 $\operatorname{Tr}\mathcal M_1=v_0$、
$\operatorname{Tr}\mathcal M_2=v_0v_1-2a$，所以式 (9) 也成立。
因此在简单根处，$-g/\det J_n=g/\det(I-DH^n)$，逐点证明 (1) 与 (2)
一致。这个负号与 $n$ 无关。

### 证明第 3 步：准确的邻接指数展开

取 $R$ 充分大，使当 $|X|=R$ 时
$|p(X)|>(1+|a|)R$。同一个 $R$ 对任意 $n$ 的乘积圆环都适用。
经典全局留数系数公式可以在此圈上积分；对每个 $i$ 有一致绝对收敛的展开

$$
\frac1{F_{n,i}}=
\sum_{L_i,R_i\ge0}
\binom{L_i+R_i}{L_i}
\frac{a^{L_i}x_{i-1}^{L_i}x_{i+1}^{R_i}}
     {p(x_i)^{L_i+R_i+1}}.
\tag{10}
$$

这里大写 $R_i$ 是整数指数，与积分半径 $R$ 不同。
有限个一致绝对收敛级数的乘积可以逐项积分。每个配置的局部贡献为

$$
\prod_{i=0}^{n-1}
\binom{L_i+R_i}{L_i}a^{L_i}
c_{R_{i-1}+L_{i+1},L_i+R_i}(p,q).
\tag{11}
$$

$n=1$ 时两个邻因子落在同一变量，二项式系数会正确重组为
$(1+a)^{L_i+R_i}$；$n=2$ 时左、右邻变量相同，但指数相加，式 (11)
仍保持原样。没有把短周期当成三条不同顶点的图。

### 证明第 4 步：周期无关的有界流量引理

若 $c_{k,e}\ne0$，无穷远的最高幂次必须至少为 $-1$，从而

$$m+k-d(e+1)\ge-1.$$

对式 (11) 的非零配置令 $e_i=L_i+R_i$。先用未截断的
$M_0=m-d+1$，得到

$$d e_i\le M_0+R_{i-1}+L_{i+1}.\tag{12}$$

若 $M_0<0$，对全部 $i$ 求和会得到
$(d-1)\sum_i e_i\le nM_0<0$，矛盾；所以所有贡献为零。
若 $M_0=0$，同一求和迫使全部 $e_i=0$。
以后设 $M_0=M>0$。

对这个固定配置构造实非负矩阵 $P$：当 $e_j>0$ 时，从列 $j$ 向行
$j-1$ 放入 $L_j/e_j$，向行 $j+1$ 放入 $R_j/e_j$；重合行的贡献相加。
当 $e_j=0$ 时，在 $j+1$ 行放入 $1$。每列之和为 $1$，且

$$ (P\mathbf e)_i=R_{i-1}+L_{i+1}.$$

式 (12) 因而为 $d\mathbf e\le M\mathbf1+P\mathbf e$。反复代入 $K$ 次，

$$
\mathbf e\le\frac Md\sum_{k=0}^{K-1}d^{-k}P^k\mathbf1
                  +d^{-K}P^K\mathbf e.
\tag{13}
$$

每个 $P^k$ 也列随机，所以对非负 $\mathbf e$ 有
$\|P^K\mathbf e\|_\infty\le\|\mathbf e\|_1$；固定 $n$ 与配置后，
式 (13) 的余项随 $K\to\infty$ 消失。

关键是 $P$ 只沿圆周的相邻位置移动。从某列 $j$ 出发，经过 $k$ 步能到达
行 $i$，必有圆周距离 $\operatorname{dist}(i,j)\le k$。
给定行 $i$，这样的初始列最多为 $\min(n,2k+1)$。
每个 $(P^k)_{ij}\le1$，因此

$$ (P^k\mathbf1)_i\le2k+1.$$

这对 $n=1,2$ 也成立。代入式 (13) 并求和得

$$
e_i\le\frac Md\sum_{k\ge0}\frac{2k+1}{d^k}
=\frac{M(d+1)}{(d-1)^2}.
\tag{14}
$$

由于 $e_i$ 是整数，$L_i,R_i\le e_i\le B$。
这个论证不要求参数实、不要求权重正，也不把 $P$ 解释成实际 Hénon
动力学的 Markov 算子；$P$ 只是对单个整数指数配置的证明工具。
特别地，$d=2$ 没有使用不成立的 $d-2$ 分母最大值估计。

### 证明第 5 步：有限边状态与全部周期同时闭合

第 4 步证明式 (11) 中任意非零贡献都满足 $0\le L_i,R_i\le B$。
取周期边状态

$$E_i=(R_{i-1},L_i),\qquad E_{i+1}=(R_i,L_{i+1}).$$

则式 (11) 的第 $i$ 个因子正是 $W_{E_i,E_{i+1}}$。
整数配置与闭合边状态序列一一对应，所以完整留数之和为

$$\operatorname{Res}_{F_n}\prod_iq(x_i)
=\sum_{E_0,\ldots,E_{n-1}\in\mathcal E}
W_{E_0,E_1}\cdots W_{E_{n-1},E_0}
=\operatorname{Tr}W^n.$$

对于 $M_0\le0$，同样公式由前一步的消去或单一零状态成立。
这一步不是将 $n$ 个不同维度商代数的矩阵混作同一个算子：同一个边状态
矩阵 $W$ 从一开始就只依赖 $d,m,p,a,q$。

取 $T=1/X$，$T^dp(1/T)=1+p_{d-1}T+\cdots+p_0T^d$，其负整数次幂的
每个 Taylor 系数是 $p_j$ 的整系数多项式。因此式 (5)、(6) 的每个矩阵元
具有定理所说的系数性质。式 (2)、(3) 及有限矩阵 log-det 恒等式给出
式 (7)。由于 $\det(I-zW)|_{z=0}=1$，右端在原点解析。证明完毕。

## 3. 非平凡全参数例与完整的普通迹边界

### 3.1 二次映射、全部二次权重的闭式

取

$$p(X)=X^2+bX+c,\qquad q(X)=uX^2+vX+w.$$

在通用边矩阵中反复删除无入边／无出边的状态，所得保留全部迹的
五状态块采用次序 $(0,0),(0,1),(1,0),(1,1),(2,2)$。它仍保留一个不参与
闭合路径的桥状态 $(2,2)$，该状态不影响任何幂迹或 $\det(I-zW)$。令

$$A=v-bu,\quad C=b^2u-bv-cu+w,\quad
E=-b^3u+b^2v+2bcu-bw-cv,$$

该块为

$$
W_*=
\begin{pmatrix}
A&C&0&u&0\\
0&au&0&0&0\\
C&E&u&v-2bu&u\\
au&a(v-2bu)&0&0&0\\
0&a^2u&0&0&0
\end{pmatrix}.
$$

这是直接由式 (6) 得到的通用多项式块。一般系数先按上述无入边／无出边规则裁剪，
所得迹恒等式是多项式恒等式，因而在所有系数专门化后仍成立。
有限行列式计算给出

$$
\boxed{
D(z)^{-1}=(1-uz)(1-auz)
\bigl(1-(v-bu)z-au^2z^2\bigr).}
\tag{15}
$$

常数 $c,w$ 不进入这个结果；这说明该带符号全复周期观测并非保留全部
动力学信息。式 (15) 是主定理的例子，不另算一篇论文。
取 $b=-1,c=2,a=2/3,u=v=w=1$ 时，留数前五项为
$11/3,61/9,359/27,2329/81,15611/243$，式 (1) 的迹是其负数。

### 3.2 完整的普通 trace-class 代表判据

对这个冻结的迹序列，存在某个复 Hilbert 空间上的 trace-class 算子 $T$
满足 $\operatorname{Tr}T^n=\tau_n$ 对全部 $n\ge1$ 成立，当且仅当 $W$ 幂零。

证明：若存在这样的 $T$，其普通 Fredholm determinant 是整函数，且在
原点等于 $D(z)=1/\det(I-zW)$。若 $\det(I-zW)$ 非常数，它至少有一个复根，
而分子为 $1$，极点不能消去，矛盾。反之若 $W$ 幂零，全部迹为 $0$，
取 $T=0$ 即可。有限矩阵 $\det(I-zW)=1$ 与幂零等价，故条件完整。

这只是冻结迹序列的普通迹类代表判据，不排除 supertrace、分布迹、
不同周期观测或物理绝对权重算子。Fredholm 极点反证是经典机制，
与仓库 P25／本轮普通迹备选存在机制重叠，不作为主创新。

## 4. 碰撞、原始来源与有边界的查新

### 4.1 仓库读取边界

读取根与 Hénon 指导、本流当前状态、批次 skill 和其完整 WORKFLOW；
定向查看当前初筛、封存备用报告以及命中本问题的批次计划。
没有读取数百个包。本问题的一个直接近邻是
[旧 holomorphic Hénon pilot](../../henon_holomorphic_complex_transfer/THEOREM_PACKAGE.md)，
它只声明一／二周期前缀及 inverse-pullback 次数增长，并没有周期无关
有限状态构造。其二周期实测缺陷见 §5，不把纠错本身当作本合同增量。

独立审阅另指出同一基础层的直接近邻
[time-ordered Hénon 推导包](../../henon_time_ordered_ruelle_cocycle/DERIVATION_PACKAGE.md)。
作者已定向核对其第 515–675 行：Lemma 4／Theorem 5 已给出该参数族的
循环 Hill 关系、全周期单位权重留数消去、返回导数迹分子公式，以及退化
固定点的 signed scheme-residue 约定。这些全部扣为既有输入，不作为
本合同的新结果；该处没有任意一元坐标多项式权重的周期无关有限边矩阵。

Boole 全实周期权重稿使用一维射影 fixed-point index／无穷远临界结构；
其本次封存文件未改动。新合同不是其额外参数，也不使用 Cayley、椭圆
action-angle、Lattès 或既有 Blaschke 谱共轭配方。

### 4.2 原始来源扣除表

| 来源 | WHY／HOW／WHAT 及与本合同的关系 | 实际访问与证据级别 |
|---|---|---|
| **[S1]** Cattani, E., Dickenstein, A., & Sturmfels, B. (1996). *Computing multidimensional residues*. In *Algorithms in Algebraic Geometry and Applications*, Progress in Mathematics 143, 135–164. [作者 arXiv 1994 稿](https://arxiv.org/pdf/alg-geom/9404011) | 计算固定个数多项式方程的全局留数；以初始形式／Gröbner 正规形求系数。Theorem 2.3、Lemma 4.2、§4 的代数迹公式全部属于既有输入。 | 原文相关完整定理和证明已通过网页 PDF 文本访问；出版元数据又由[作者发表清单](https://mate.dm.uba.ar/~alidick/PubsDickensteinApril2020.pdf)交叉确认。不是本轮人工阅读声明。 |
| **[S2]** Molinari, L. G. (2008). *Determinants of block tridiagonal matrices*. *Linear Algebra and its Applications, 429*, 2221–2226. [arXiv v3](https://arxiv.org/pdf/0712.0681v3)；[作者机构元数据](https://air.unimi.it/handle/2434/43334) | 把循环三对角行列式化为二阶 transfer-product 行列式。标量 equation (1) 给出式 (9) 的经典 Hill 符号。 | 原文公式／相应假设及机构书目信息已访问。作者站 PDF 一次返回 502，改用 arXiv v3，不冒称失败请求成功。 |
| **[S3]** D'Andrea, C., & Dickenstein, A. (2026). *Toric Euler-Jacobi vanishing theorem and zeros at infinity*. [arXiv:2601.13977v1](https://arxiv.org/html/2601.13977v1) | 检查消去与无穷远零点条件的逆向关系。其 Theorem 1.4 需要 indecomposable 支持等条件；不能把它无条件移植给本循环族。它进一步表明“找到全局留数消去”不是新颖性依据。 | 原文引言、例子、Theorem 1.1／1.4 已访问；作为预印本标识，未宣称同行评审发表。 |
| **[S4]** Soprunov, I. (2007). *Global residues for sparse polynomial systems*. [作者 arXiv 稿](https://arxiv.org/abs/math/0511684) | 稀疏系统的全局留数和插值。直接相关 primitive 是固定周期下已有的留数计算，不能据此把每个周期的有限商代数说成一个周期无关算子。 | arXiv 官方元数据／摘要已访问；本合同证明不依赖尚未逐节阅读的全文。 |

数学原始定理的适配性按“已核对假设与命题”判断；医学实验七级金字塔
对纯证明不适用，未用一个虚假的 RCT／meta-analysis 等级给它们评级。
来源均为实名作者、原稿／机构出版记录；未执行 Cabell、Scopus 订阅审计
或作者利益冲突调查，因此不声称这些检查全通过。没有发现来源指向的
具体冲突不等于认证无冲突。

### 4.3 实际检索、遗漏与新颖性边界

2026-09-05 通过网页检索定向查询这些问题，并访问上表主来源：

1. `Hénon map periodic orbit sum holomorphic residue Euler Jacobi polynomial observables trace formula`
2. `Hénon map trace formula polynomial weights finite matrix residue periodic points`
3. `polynomial automorphism dynamical zeta holomorphic fixed point index sum Hénon maps`
4. `Hénon Grothendieck`、`Hénon Euler-Jacobi`、`polynomial weighted periodic points residue`
5. `weighted Lefschetz polynomial dynamical`、`Hénon rational weighted zeta`
6. `global residue transfer matrix`、`periodic points polynomial weights`
7. `Hénon holomorphic weights zeta 2024 2025 2026`
8. `Hénon residue 2026 weighted`、`Hénon trace identities`
9. `Molinari determinants block tridiagonal matrices transfer matrices arxiv Hill formula 2008`

纳入与具体权重、返回分母、留数或周期无关压缩相关的原始数学来源；
排除蛋白质“residue”、Hénon–Heiles ODE、PDE Hénon 权重和二手结果页。
本地定向碰撞查询采用 `rg`；本环境没有 Zotero／Obsidian 工具，未伪造
数据库结果。只读官方 arXiv 页面，不运行会启动专用 bibliographic resolver
或传送未公开证明的程序。

**检索有界判断：** 本次没有找到直接包含式 (4)、(6)、(7) 的全次数／
全多项式权重／全周期构造的来源；这只能支持继续独立准入审查，不能
证明全球首创。最强可见新量词是从 $d^n$ 维循环商代数转为 $(B+1)^2$
维同一个矩阵。若已有一般代数 correspondence／weighted Lefschetz
定理直接蕴含这一压缩，必须重新评估论文增量，而不能只改题名。
这个源集合在方法上完全偏向理论数学；这是请求范围造成的分布集中，
不扩充无关经验论文来做比例装饰。

## 5. 历史二周期精确反例：记录而不改写

旧包声明
$F(z,w)=(w,w^2-z/4)$。对 $F^2(z,w)=(z,w)$，正确方程应为

$$w^2=\tfrac54z,\qquad z^2=\tfrac54w,$$

从而消去多项式为 $z^4-125z/64$。设
$\omega=(-1+i\sqrt3)/2$，四点为

$$
(0,0),\quad(\tfrac54,\tfrac54),\quad
(\tfrac54\omega,\tfrac54\omega^2),\quad
(\tfrac54\omega^2,\tfrac54\omega).
$$

它们的返回稳定性倒数分别是
$16/25,-16/75,-16/75,-16/75$，总和为 $0$。
旧 producer 实际使用了 $y=x^2-x/4$、$x=y^2-y/4$，把当前步和上一步
变量的系数放错位置。它列出的非实点

$$P_*=((-3-i\sqrt{39})/8,(-3+i\sqrt{39})/8)$$

满足

$$
F^2(P_*)-P_*=
\left(i\sqrt{39}/16,\,117/256-7i\sqrt{39}/64\right)\ne0.
$$

旧 `c108_sympy_crosscheck.py` 核对的是同一错误 resultant，并直接断言
已有数值与 payload 相等，没有从字面 $F^2-I$ 独立重建。
因此旧文档的 $\tau_2=-1664/1725$ 不成立，其相应 determinant 前缀也不成立。
本次没有运行旧 producer、改旧证据、改旧清单或把新输出放入旧路径。
该具体缺陷已送协调者；任何修复／历史状态更改属于另外明确范围。

## 6. 复现、未做事项与交接

在仓库根运行：

```text
python henon_dynamics/continuation_c399_c403_round2/nonlinear_return/exact_check.py
```

脚本只向 stdout 输出 JSON，不读历史证据，也不写它们。
本轮实际环境为 Python 3.12.3、SymPy 1.14.0，退出状态 0。
最终 stdout 保存为 [EXACT_CHECK_OUTPUT.json](EXACT_CHECK_OUTPUT.json)；
两种有限留数算法的匹配不是外部评审，也不是全周期定理的替代。

实施了 `henon-route-a-batch` 的先合同／再决定性检验、ARS 三段式来源核查、
`research-lit`／`novelty-check` 的直接所有权扣除和 `proof-writer` 的完整
量词与退化边界。按当前明确指令，不采用旧 `idea-creator` 示例要求的
8–12 个条目、GPT-5.4 外部接口或 GPU 试验；不声称这些调用已执行。
这份文档和代码使用 AI 辅助研究工具编制，独立团队审查仍须单独记录。

尚未做正式 Route-A 评估、实际论文写作、PDF 构建、发表／上传、
共享索引／Git 更新。**全局留数、源有理行列式和源系数域不建立目标
Euler factors、root number、automorphy、零除子对应或 Hilbert–Pólya 实现。**
保持 `NO_BAD_EULER_OR_ROOT_NUMBER`，没有目标 A2/A3 晋级。

下一门槛是从本文件原始证明开始的独立内部审查：重点攻击式 (14) 的
全周期界、短周期邻项重合、全局留数与 (1) 的负号、退化参数定义，以及
相对经典固定维数留数算法是否确有足够独立增量。审查未通过前，不进入
论文编写或占据已完成论文席位。
