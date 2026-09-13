# Paper29 加性辛映射的 wild 固定 scheme：有界预筛

日期：2026-09-06。审查对象：新方向，不是正式论文。

**处置建议：STOP_SCOPED / 不建议作为当前 Paper29 立项。**

最小对象与一般矩阵对象均可严谨成立；下文给出完整证明。停止原因不是数学失败，而是已有文献已经覆盖决定性的 Smith 正规形、总次数、不可分次数及周期点计数机制。局部 scheme 型别比点数更细，但目前实际新增内容是这一已有机制的短显式展开，未发现可支撑 22–30 页实质正文的新核心。

- 科学状态：下文命题为 `PROVED`，不等于新意或论文验收通过。
- 新意门：现有核心覆盖强；精确局部例子的“未搜到逐字相同陈述”不构成新意证明。
- 价值门：适合作为已有理论的有用例子或短注；尚不构成当前长文问题。
- 自然篇幅预估：完整介绍、证明、scheme 与几何周期层边界，约 8–14 页实质正文；此为预筛判断，不是排版验收或独立评审分数。
- 产物状态：仅本报告；没有创建 `papers/29`，没有修改旧候选或已接受论文。
- `route_applicability: NOT_APPLICABLE`。这里没有 Riemann 动力行列式、RH、prime-clock 或谱算子主张。

## 1. 范围、入口与实际方法

本报告只拥有这个新文件。按任务要求全文读取 `AGENTS.md`、`docs/WORKFLOW.md`、当前批次接续文件，以及 idea-creator、research-lit、proof-writer 的 `SKILL.md`。最新任务明确保留 22–30 页正文与新意/价值/完整证明门，且停止旧 Hénon trace-chart 候选；批次接续文件中旧的页数变更提请不覆盖这一最新要求。本报告不在旧候选周边加推论。

使用 idea-creator 的先查新、先验价值、失败即淘汰原则；使用 research-lit 的本地优先与一手来源核对；使用 proof-writer 的精确命题、依赖与完整证明格式。未使用技能所列指定外部模型通道；这里是普通独立代理的有界 fallback，不能冒称指定模型复核。纯证明任务不造 GPU 实验。

本地 PDF 先按名称和已有源码关键词定向筛选，读取 Paper4 与 Paper5 已有 PDF 的前三页：它们分别处理数域上的周期乘子好约化、归一化代数作用量，没有提供本方向的正特征加性固定 scheme 结果。没有找到本地相关外部文献 PDF。没有找到可用的 `arxiv_fetch.py`，按技能允许的方式以 arXiv 官方页面检索替代 API 脚本。没有下载外部 PDF 到工作区。

## 2. 一手查新与覆盖结论

### 2.1 关键来源

| 来源 | 已核证据 | 对候选的覆盖判断 |
| --- | --- | --- |
| Byszewski–Cornelissen–Houben, *Dynamics of endomorphisms of algebraic groups*, arXiv:2209.00085v2，2024 修订，176 页；当前核到的版本按研究专著预印本记录 | §5.2；Lemma 5.2.2；Proposition 5.2.14；Theorem 5.2.17 | 直接覆盖向量群的 Smith 方法、总/不可分次数及固定点序列；不是仅有相似 zeta 名称的邻近工作 |
| Byszewski–Cornelissen, *Multiband linear cellular automata and endomorphisms of algebraic vector groups*, arXiv:2211.02866v2，2024 | Theorem F，Proposition G；一手院系记录称 2024 年已接受于 *Algebraic Geometry and Physics* | 向量群矩阵与线性元胞自动机的对应、周期点群及计数已经系统化；不宜另造该对应为创新 |
| Byszewski–Cornelissen–Houben，附录与 van der Meijden 合作，*Dynamically affine maps in positive characteristic*, Contemp. Math. 744 (2020), 125–156；arXiv:1904.04942 | 定义与导言、主结果适用对象 | 提供动态仿射框架和 tame/full 计数背景；不声称其一维或 Kummer 主定理直接证明本报告的局部 scheme 分类 |
| Byszewski–Cornelissen，附录 Royals–Ward，*Dynamics on abelian varieties in positive characteristic*, Algebra Number Theory 12 (2018)；arXiv:1802.07662 | 官方摘要 | 已区分固定点数与次数计数；对象是 abelian varieties，不能直接当作向量群定理 |
| Bell–Miles–Ward, *Towards a Pólya–Carlson dichotomy for algebraic dynamics*, Indag. Math. 25 (2014), 652–668；arXiv:1307.2369 | 作者稿与一手机构出版记录 | 紧邻的群动力系统 zeta 二分传统；不将本方向的 zeta 加工视为新增数学问题 |
| Cornelissen–Park, *Orbit decomposition statistics for discrete dynamical systems: the Cesàro mean and a large deviation principle*, arXiv:2605.24504 (2026) | 官方摘要 | 新近轨道统计仍覆盖代数群与线性元胞自动机背景；未发现本报告局部 scheme 型别在此被研究 |

来源链接：[BCH 专著 v2](https://arxiv.org/pdf/2209.00085v2)，[向量群与元胞自动机 v2](https://arxiv.org/pdf/2211.02866v2)，[该文接受记录](https://apacz.matinf.uj.edu.pl/publikacje/9858-multiband_linear_cellular_automata_and_endomorphisms_of_algebraic_vector_groups)，[动态仿射论文](https://arxiv.org/pdf/1904.04942)，[动态仿射出版记录](https://research-portal.uu.nl/en/publications/dynamically-affine-maps-in-positive-characteristic/)，[abelian varieties 官方记录](https://arxiv.org/abs/1802.07662)，[Bell–Miles–Ward 作者稿](https://eprints.whiterose.ac.uk/104959/1/PolyaCarsonFinal.pdf)，[其出版记录](https://eprints.whiterose.ac.uk/id/eprint/104959/)，[2026 轨道统计](https://arxiv.org/abs/2605.24504)。

最关键的定向核对是 BCH 的以下位置：印刷页 55–58（PDF 页 65–68）建立向量群的 twisted-polynomial 矩阵与 Smith 方法；Lemma 5.2.2 给总次数和不可分次数；印刷页 62–63（PDF 页 72–73）Proposition 5.2.14 与 Theorem 5.2.17 给迭代规律。其 §4.1（印刷页 37–38）还明确区分几何固定点与重数，并讨论核的 étale/local 分解。因此不能说该文“完全忽略 scheme，只数点”。

该来源并未在已核章节中逐项列出下面 $H_q$ 的两条局部 Smith 指数，也未找到 Hénon 名称。**这是精确公式的显式呈现差异，不是已确认的理论缺口。** 下文独立推导表明，得到这些公式所需的新计算非常短。

### 2.2 检索覆盖与限度

实际使用超过五种定向问法，包括：Byszewski/Cornelissen 与 additive/positive characteristic；Miles/Ward 与 inseparable periodic counts；Hénon + additive + positive characteristic；fixed point scheme + additive automorphism；Smith normal form + group schemes；linearized polynomial kernel；Smith forms of powers；2024–2026 的向量群与元胞自动机跟进。

没有试图用大量不相关摘要凑足 10–15 篇。主对象在一份直接匹配的专著中已有强覆盖时，有界预筛应及时收束。未找到精确 Hénon 局部型别的既有逐字陈述，并不支持全球“首次”结论；特别是加性多项式、有限群概形及矩阵幂 Smith 型别存在大量经典基础文献。

## 3. 证明包：矩阵核的全部局部 scheme

### Claim

令 $p$ 为素数，$r\geq1$，$q=p^r$，$k=\overline{\mathbf F_q}$，$R=\mathbf F_q[T]$。记 $F:\mathbf G_a\to\mathbf G_a$ 为坐标上的 $q$ 次幂映射。对 $f(T)=\sum_i f_iT^i\in R$，定义加性多项式

$$L_f(X)=\sum_i f_iX^{q^i}.$$

若 $M\in M_2(R)$ 且 $\det M\ne0$，令 $d_1\mid d_2$ 为其非零 Smith 因子，$e_i=v_T(d_i)$，$D=\deg\det M$，$E=e_1+e_2$。则 $M(F)$ 的核是有限 $k$-scheme，满足：

$$\operatorname{length}\ker M(F)=q^D,\qquad
\#\ker M(F)(k)=q^{D-E}.$$

每个几何点处的局部环同构于

$$k[u,v]/(u^{q^{e_1}},v^{q^{e_2}}).\tag{3.1}$$

其中 $e_i=0$ 的因子意指该变量被一次方消去。作为局部群概形，单位连通分支为

$$\alpha_{q^{e_1}}\times\alpha_{q^{e_2}},\qquad
\alpha_{q^a}=\ker(F^a:\mathbf G_a\to\mathbf G_a),$$

并约定 $\alpha_1$ 为平凡群概形。

### Status

`PROVABLE AS STATED`。这是基础 Smith/加性核机制的自含展开，不主张其本身为新定理。

### Assumptions and notation

系数限制在 $\mathbf F_q$，因此 $F$ 与系数乘法交换，$L_{fg}=L_f\circ L_g$。不能把本证明的交换行列式无条件用于任意 $k$ 系数的 $p$-加性矩阵；后者需要 skew-polynomial 工具。这里的 $F$ 是基变换后的坐标 $q$ 次幂 $k$-态射，不混同于对所有基域元素取幂的绝对 Frobenius。

### Proof strategy and dependency map

1. $R$ 是 PID，故 Smith 分解可把矩阵核化为两个一元加性核。
2. 一元加性多项式的最低 Frobenius 指数决定每个根的局部重数。
3. 最高指数决定总长度，平移保证各点局部型别一致。

### Proof

**Step 1: 矩阵正规形对应实际多项式自同构。** Smith 正规形给 $U,V\in\operatorname{GL}_2(R)$ 使

$$UMV=\operatorname{diag}(d_1,d_2).$$

$U^{-1},V^{-1}$ 仍在 $M_2(R)$，故 $U(F),V(F)$ 都是实际加性多项式自同构。源上的 $V(F)$ 因而给矩阵核与 $\ker L_{d_1}\times\ker L_{d_2}$ 的 scheme 同构；靶上的 $U(F)$ 不改变零纤维。这里没有把纯不可分映射误称自同构。

**Step 2: 一元长度与根。** 写 $d=T^e h$，$h(0)\ne0$，$m=\deg h$。因系数在 $\mathbf F_q$，

$$L_d(X)=L_h(X)^{q^e}.$$

$L_h$ 的通常次数为 $q^m$，导数恒为非零的 $h(0)$。在代数闭域上，它恰有 $q^m$ 个不同根。$L_d$ 的商环维数为其次数 $q^{m+e}$，每个根的重数为 $q^e$。

**Step 3: 局部环而不只是重数。** 对根 $a$，令 $u=X-a$。加性给 $L_h(a+u)=L_h(u)$。在 $u=0$ 的局部环中，$L_h(u)/u$ 是单位，故方程 $L_h(u)^{q^e}=0$ 与 $u^{q^e}=0$ 生成相同理想。于是该根处的局部环是 $k[u]/(u^{q^e})$。坐标 $L_h(u)$ 是加性局部坐标；其有限截断逆可由 $h(T)$ 与 $T^e$ 的 Bezout 恒等式取得，因此单位连通分支作为群概形亦同构于 $\alpha_{q^e}$。

**Step 4: 两因子相乘。** 总长度与几何点数分别相乘。由 $\deg d_1+\deg d_2=D$、$v_T(d_1)+v_T(d_2)=E$ 得两个公式及 (3.1)。由于核是群概形，任意核点的平移也是 scheme 自同构，这也直接确认全部局部型别一致。证毕。

## 4. 一般 $\operatorname{SL}_2(R)$ 对象：可行，但并非未开发空白

### Claim

取 $A(T)\in\operatorname{SL}_2(R)$，且 $s(T)=\operatorname{tr}A(T)$ 非常数，$d=\deg s\geq1$。令 $\Phi=A(F)$。则 $\Phi$ 是加性多项式自同构，保持 $dx\wedge dy$，且对所有 $n\geq1$，

$$\operatorname{length}\operatorname{Fix}(\Phi^n)=q^{nd}.$$

若 $e_1(n),e_2(n)$ 是 $A(T)^n-I$ 的两条 $T$-局部 Smith 指数，则

$$\#\operatorname{Fix}(\Phi^n)(k)=q^{nd-e_1(n)-e_2(n)},$$

而全部局部环由 (3.1) 给出。

### Status

`PROVABLE AS STATED`。必须保留“非常数迹”；例如 $A=I$ 时固定 scheme 不有限。不能从多项式矩阵的单步通常次数直接猜测固定核长度。

### Proof

**Step 1.** $A^{-1}$ 仍是 $R$ 系数矩阵，因此 $A(F)$ 可逆。其 Jacobian 为常矩阵 $A(0)$，因为 $d(X^{q^i})=0$ 对 $i\geq1$。又 $\det A(0)=1$，故保持标准二形式。本报告只主张辛二形式保持，不额外主张某个锁定 Liouville 原始量的 exactness。

**Step 2.** Cayley–Hamilton 给 $A^2-sA+I=0$。定义 $D_0(S)=2$、$D_1(S)=S$、

$$D_{n+1}(S)=S D_n(S)-D_{n-1}(S).$$

取迹和归纳得到 $\operatorname{tr}(A^n)=D_n(s)$。对每个 $n\geq1$，$D_n$ 是次数为 $n$ 的首一多项式：$D_2=S^2-2$；其后递推的首项来自 $S D_n$，不会被次数 $n-1$ 的 $D_{n-1}$ 抵消。此论证在特征 $2$ 也有效。

**Step 3.** 对任意二阶行列式一矩阵，

$$\det(A^n-I)=2-\operatorname{tr}(A^n)=2-D_n(s).$$

右侧次数为 $nd$ 且非零。第 3 节引理适用，给出有限性、总长度、几何点数与局部环。证毕。

### Known deductions / novelty boundary

这已置于 BCH §5.2 的向量群框架内。特别是它不是一个困难的一般 $k$ 系数分类：选取 $\mathbf F_q[T]$ 恰好使整个计算退化到交换 PID。将此结论写成“全体加性辛映射的新固定点理论”会同时夸大对象范围与新意。

## 5. 最小对象 $H_q$ 的完整局部公式

令

$$H_q(x,y)=(x^q-y,x),\qquad
B(T)=\begin{pmatrix}T&-1\\1&0\end{pmatrix}.$$

则 $H_q=B(F)$，$H_q^{-1}(x,y)=(y,y^q-x)$，且逐坐标相加得到

$$H_q+H_q^{-1}=(x^q,y^q).$$

其 Jacobian 为 $J=B(0)$。令 $v=v_p(n)$。

### Claim

每个 $n\geq1$，$\operatorname{Fix}(H_q^n)$ 总长度为 $q^n$。全部局部 Smith 指数如下：

| 条件 | $(e_1,e_2)$ | 几何固定点数 | 每点局部长度 |
| --- | --- | --- | --- |
| $p$ 奇，$4\nmid n$ | $(0,0)$ | $q^n$ | $1$ |
| $p$ 奇，$4\mid n$ | $(p^v,p^v)$ | $q^{n-2p^v}$ | $q^{2p^v}$ |
| $p=2$，$n$ 奇 | $(0,1)$ | $q^{n-1}$ | $q$ |
| $p=2$，$n$ 偶 | $(2^{v-1},2^{v-1})$ | $q^{n-2^v}$ | $q^{2^v}$ |

因此奇特征时约化当且仅当 $4\nmid n$；特征 $2$ 时没有任何迭代的固定 scheme 约化。

### Status

`PROVABLE AS STATED`。任务中的初推总长度、几何点数和奇特征重数全部正确；特征 $2$ 的“odd $(1,F)$ / even 等幂”须精确定义成表中局部 Smith 因子，而非全局 Smith 多项式等式。

### Proof strategy / dependency map

总长度来自第 4 节的 $s(T)=T$。局部型别只需在 DVR $\mathbf F_q[[T]]$ 中计算矩阵 $B^n-I$ 的 Smith 指数，再用第 3 节。

### Proof

**Step 1: 奇特征的非共振周期。** $J^2=-I$、$J^4=I$。当 $n$ 为奇数，$\det(J^n-I)=2\ne0$；当 $n\equiv2\pmod4$，该行列式为 $4\ne0$。故 $B^n-I$ 在 $T=0$ 已可逆，两条局部指数都是零。

**Step 2: 奇特征的 $4\mid n$。** 直接乘法给

$$B^2=-I+TJ+T^2E_{11},\qquad B^4=I-2TJ+O(T^2).$$

写 $n=p^v m$、$p\nmid m$；因 $p$ 奇且 $4\mid n$，可写 $m=4h$，$p\nmid h$。有限乘法展开给

$$B^m-I=-2hTJ+O(T^2)=T U,$$

其中 $U(0)=-2hJ$ 可逆。矩阵 $B^m$ 与 $I$ 交换，故特征 $p$ 的二项式恒等式允许写

$$B^n-I=(B^m-I)^{p^v}=T^{p^v}U^{p^v}.$$

$U^{p^v}$ 可逆，两条指数均为 $p^v$。

**Step 3: 特征 $2$ 的奇数周期。** $B-I$ 有一个单位条目且行列式为 $T$，所以其局部指数为 $(0,1)$。对奇数 $n$，

$$B^n-I=(B-I)S_n(B),\qquad S_n(B)=I+B+\cdots+B^{n-1}.$$

在 $T=0$，写 $J=I+N$，$N^2=0$。于是

$$S_n(J)=nI+\frac{n(n-1)}2N=I+cN$$

对某个 $c\in\mathbf F_2$ 成立；整数二项式系数先取整再约化。$I+cN$ 的逆为自身，故 $S_n(B)$ 局部可逆，两条指数保持 $(0,1)$。

**Step 4: 特征 $2$ 的偶数周期。** 精确恒等式为

$$B^2-I=TB.$$

对 $v\geq1$，二项式恒等式给

$$B^{2^v}-I=(B^2-I)^{2^{v-1}}
=T^{2^{v-1}}B^{2^{v-1}}.$$

右侧后因子可逆。若 $n=2^v m$、$m$ 奇，则

$$B^n-I=(B^{2^v}-I)S_m(B^{2^v}).$$

由于 $J^{2^v}=I$，最后一因子在 $T=0$ 为 $mI=I$，仍可逆。因此两条指数均为 $2^{v-1}$。由第 3 节得到表中局部环、几何点数和局部长度。证毕。

## 6. 一个真实的 scheme 级区别，以及它为什么仍然偏短

下面给出点数不能检测局部结构的实际完整引理。它是本次最有用的补充，但不声称解决了文献中的开放问题。

### Claim: 全周期同计数但不同局部型别

取

$$A_1=\begin{pmatrix}1&T\\T&1+T^2\end{pmatrix},\qquad
A_2=\begin{pmatrix}1&1\\T^2&1+T^2\end{pmatrix}.$$

二者属于 $\operatorname{SL}_2(R)$，迹均为 $2+T^2$。记 $\Phi_i=A_i(F)$。则对所有 $n\geq1$，$\Phi_1^n$ 与 $\Phi_2^n$ 的固定 scheme 有相同总长度与相同几何点数：

$$\operatorname{length}\operatorname{Fix}(\Phi_i^n)=q^{2n},\qquad
\#\operatorname{Fix}(\Phi_i^n)(k)=q^{2n-2p^{v_p(n)}}.$$

但在 $n=1$，两个固定 scheme 都仅支撑在原点，且分别为

$$\operatorname{Fix}(\Phi_1)\simeq\alpha_q\times\alpha_q,
\qquad \operatorname{Fix}(\Phi_2)\simeq\alpha_{q^2}.$$

它们的 Zariski 切空间维数分别为 $2$ 与 $1$，故不作为 $k$-scheme 同构。

更精确地，令 $P=p^{v_p(n)}$，则 $A_1^n-I$ 的局部指数始终为 $(P,P)$。$A_2^n-I$ 的指数在 $p$ 奇时为 $(P-1,P+1)$；在 $p=2,n$ 奇时为 $(0,2)$；在 $p=2,n$ 偶时为 $(P,P)$。

### Status

`PROVABLE AS STATED`。这是显式 scheme 区分例，不是已确认的新理论。

### Proof

**Step 1.** 两矩阵行列式与迹逐项可算。故第 4 节给总长度 $q^{2n}$，且两矩阵所有 $n$ 的固定核行列式相同。

**Step 2.** 写 $C_i=A_i-I$。则

$$C_1=\begin{pmatrix}0&T\\T&T^2\end{pmatrix},\qquad
C_2=\begin{pmatrix}0&1\\T^2&T^2\end{pmatrix}.$$

二者行列式均为 $-T^2$。第一矩阵是 $T$ 乘以可逆矩阵，故指数为 $(1,1)$；第二矩阵有单位条目，故指数为 $(0,2)$。

**Step 3.** 写 $n=Pm$、$p\nmid m$。分解

$$A_i^m-I=C_iS_m(A_i).$$

$A_1(0)=I$，故 $S_m(A_1)(0)=mI$ 可逆。$A_2(0)=I+N$、$N^2=0$，故

$$S_m(A_2)(0)=mI+\binom m2N$$

也可逆，其行列式为 $m^2\ne0$。这两个 $S_m(A_i)$ 与 $C_i$ 交换。因此

$$A_i^n-I=C_i^P S_m(A_i)^P,$$

且右侧最后一因子局部可逆。

**Step 4.** $C_1=T U$ 且 $U$ 可逆，给 $C_1^P$ 指数 $(P,P)$。Cayley–Hamilton 对 $A_2$ 给精确恒等式

$$C_2^2=(A_2-I)^2=T^2A_2.$$

当 $P$ 为奇数，

$$C_2^P=T^{P-1}A_2^{(P-1)/2}C_2,$$

故两指数是 $(P-1,P+1)$。当 $P$ 为偶数，

$$C_2^P=T^P A_2^{P/2},$$

故两指数是 $(P,P)$。全部情形的指数和均为 $2P$，第 3 节给点数公式。$n=1$ 时局部长度已等于总长度，原点是唯一几何点；局部环分别是 $k[u,v]/(u^q,v^q)$ 与 $k[v]/(v^{q^2})$，其极大理想模平方维数为 $2$ 与 $1$。证毕。

### 解读边界

点数及 determinant 的确不能决定两条局部 Smith 指数。但本例的差别已经由最基本的单位条目与 $T$ 公因子检测出来，完整全周期证明仅需上述恒等式。它没有引入新的分类不变量或新方法，也没有识别出一个文献明确未解决的问题。把它命名为“scheme 谱刚性反例”之类不会增加数学量。

## 7. 周期层：可以直接得到什么，不能偷换什么

记 $g_n=\#\operatorname{Fix}(\Phi^n)(k)$。几何 exact-period 点数与轨道数当然可由有限集分解得到

$$P_n^{\mathrm{geom}}=\sum_{d\mid n}\mu(n/d)g_d,
\qquad O_n=P_n^{\mathrm{geom}}/n.$$

这是集合上周期分解的直接推论，不是新的周期计数定理。

固定 scheme 的总长度不能用同一个 Möbius 公式解释成“实际 exact-period 几何点的重数”。例如特征 $2$ 的 $H_q$：$\operatorname{Fix}(H_q)$ 和 $\operatorname{Fix}(H_q^2)$ 都只有原点一个几何点，但长度分别是 $q$ 与 $q^2$。因此 $q^2-q>0$ 是重复支撑的 wild 增厚，不是新出现的二周期点。

若把 exact-period scheme 明确定义为 $\operatorname{Fix}(\Phi^n)$ 中支撑在几何 exact-period $n$ 点上的开闭分量之并，那么第 3 节给其长度为

$$q^{e_1(n)+e_2(n)}P_n^{\mathrm{geom}}.$$

这个定义只是选择现有有限 scheme 的若干分量；它不等同于 dynatomic cycle、残余交、形式周期或其他可能的 scheme-theoretic exact-period 定义。任何进一步主张须先锁定其中一种概念。当前没有证据表明采用这一简单定义会产生长文规模的新机制。

## 8. 精确小例核错记录

实际运行只读 SymPy 有限特征多项式运算，无文件写入。对 $p\in\{2,3,5,7\}$，$1\leq n\leq48$，分别计算 $B^n-I$、$A_1^n-I$、$A_2^n-I$：共 $576$ 个案例，每例核对 determinant 次数与两条局部 Smith 指数，共 $1152$ 个断言，全数通过。

计算局部指数的方法为：对非零二阶矩阵 $C$，$e_1$ 是全部条目最低 $T$ 次数的最小值，$e_2=v_T(\det C)-e_1$。这是 DVR 的一阶、二阶行列式理想定义，与任意浮点阈值无关。

代表输出 $(p,n;e_1,e_2;\deg\det)$：

- $H$：$(2,1;0,1;1)$，$(2,2;1,1;2)$，$(2,3;0,1;3)$，$(2,4;2,2;4)$。
- $H$：$(3,4;1,1;4)$，$(3,12;3,3;12)$。

本记录只用于定位公式和边界错误，不能代替第 3–6 节证明，也不计作数值研究成果。$q=p^r$ 的一般性已由证明中的 Frobenius 指数建立，不从这些素域例子外推。

## 9. Claims / evidence / risks / decision

| 主张或候选贡献 | 证据状态 | 评价 |
| --- | --- | --- |
| $H_q$ 的固定 scheme 总长 $q^n$ | `PROVED`，第 4–5 节 | 正确；短特例 |
| 奇特征 $4\mid n$ 时一致 wild 局部长度 | `PROVED`，第 5 节 | 初推正确；局部矩阵一次展开即闭合 |
| 特征 $2$ 的奇/偶局部型别 | `PROVED`，第 5 节 | 正确；关键是 $B^2-I=TB$ |
| 一般 $A(T)\in\operatorname{SL}_2(R)$ 的固定核长度 | `PROVED`，第 4 节 | 交换 PID 子类，受已有向量群机制强覆盖 |
| 全局点数相同而局部 scheme 不同 | `PROVED`，第 6 节 | 有用，但是 elementary Smith 型别例子 |
| 完整新意或文献未覆盖的 scheme 分类 | `OPEN / NOT ESTABLISHED` | 搜索未找到相同措辞不能升级为新意 PASS |
| 新的 zeta rational/natural-boundary 理论 | 未提出 | 既有研究覆盖强；禁止以 zeta 延展凑当前篇幅 |
| 22–30 页实质正文 | 未达到可行性门 | 当前已证明材料自然偏短，不能通过教程化扩写改变这一点 |

尚未解决但不能装作既得贡献的方向包括：非交换系数环中的完整局部型别随迭代分类；带嵌入或兼容过渡映射的整个固定群概形塔，而非单个核的抽象型别；与真正非加性辛映射的 wild 周期局部环之间的结构差异。这些都需要新的明确问题、新的查新和真实非平凡命题。目前仅是研究线索，不据此启动正式论文，也不把跨对象拼接作为已授权候选核心。

**最终建议：STOP。** 保留这个正确的证明与强 prior 命中记录，避免下一轮再次发现同一短特例。原 Hénon trace-chart 候选继续停止，不降低页数或新意门，不创建正式 Paper29。若后续有人提出真正超出已有 Smith 核机制的明确 scheme 问题，应把它作为全新候选重新说明其对象、科学价值和证明障碍；当前报告不授予这种尚未提出问题任何预先通过状态。
