# P32 内部研究：层留数的可识别性与四次轮廓的对称核

记录日期：2026-09-09 UTC。第五次 P29–P33 五篇整轮内部论证。
承接[三次对数阈值与亚纯正则部分][analytic]及[调和有限部分][harmonic]。
本篇回答：整个辅助二阶轮廓保留了四次压力项的哪些信息？

结论是：在固定二次型下，完整轮廓恰检测每个格点二次型值层上的
四次权重总和。全部层留数消失当且仅当整个轮廓恒零；但不一定迫使
四次多项式为零。格点对称性可以造成不可见方向，而一个明确的
非共振条件足以排除这些方向。本篇不给真实 D、P 添加该条件。

## 1. 固定模型与用于分析的线性空间

保持项目的 \(\mathsf Q=2\pi^2D>0\)、
\(q(x)=x^{\mathsf T}\mathsf Qx\)、
\(P(x)=s_4(2\pi x)\)、时间缩放和原产品归一化不变。为描述线性
映射的核，考虑四变量实齐次四次多项式空间 \(\mathcal P_4\)，
其维数为 \(\binom74=35\)。以下可对这个空间的任一元素作代数
测试，不表示另选真实压力函数或改动曲面。

对任意 \(P\in\mathcal P_4\)，沿用

\[
p_0(P)=\int_{\mathbb R^4}P(x)e^{-q(x)}dx,\qquad
\Theta_P(u)=\sum_{k\in\mathbb Z^4}P(k)e^{-uq(k)},\qquad
G_P(u)=\Theta_P(u)-p_0(P)u^{-4}.
\tag{1}
\]

前两轮的 Gaussian／Poisson 推导对一般四次齐次 P 线性成立，给出
\(G_P(u)=O(u^{-6}e^{-b/u})\)（\(u\downarrow0\)、某个 b>0），
而大端 \(\Theta_P(u)=O(e^{-q_*u})\)，
\(q_*=\min_{k\ne0}q(k)>0\)。因此

\[
\mathcal L_P(a)=\int_0^\infty e^{-au}G_P(u)du,
\quad \operatorname{Re}a>0,
\qquad
\mathcal L_P(a)=-\frac{p_0(P)}6a^3\operatorname{Log}a+\mathscr A_P(a).
\tag{2}
\]

\(\mathscr A_P\) 在零点解析，并有整个复平面上的亚纯延拓。
原积分只在其已经证明的域内使用；延拓不是在左半平面继续积分。

令

\[
\mathcal E=\{q(k):k\in\mathbb Z^4\setminus\{0\}\},\qquad
W_P(\lambda)=\sum_{q(k)=\lambda}P(k)\quad(\lambda\in\mathcal E).
\tag{3}
\]

每个层及每个有界 \(\mathcal E\) 子集有限。每个固定 u>0 上的
Gaussian 绝对收敛允许按层重排，给

\[
\Theta_P(u)=\sum_{\lambda\in\mathcal E}W_P(\lambda)e^{-u\lambda},
\qquad
\operatorname*{Res}_{a=-\lambda}\mathscr A_P(a)=W_P(\lambda).
\tag{4}
\]

第二式是前轮已证的至多简单极点公式。本篇的新工作是把这些层
总和接到完整核判准、对称性及有限重建，不能把 (4) 本身再算新结果。

## 2. 全部留数消失的充要条件

**命题 1。** 以下条件等价：

1. \(\mathcal L_P\equiv0\) 在开右半平面成立；
2. 对每个 \(\lambda\in\mathcal E\)，\(W_P(\lambda)=0\)；
3. \(\Theta_P(u)=0\) 对每个 u>0 成立；
4. \(\mathscr A_P\) 的全部候选极点可消，即其延拓是整函数。

这些条件还都蕴含

\[
p_0(P)=0,\qquad G_P\equiv0,\qquad \mathscr A_P\equiv0.
\tag{5}
\]

证明分开处理，以免把“没有极点”误当作一般函数的唯一性条件。

若 1 成立，由前轮在正实 a 向零时的精确三阶导数式
\(\mathcal L_P'''(a)=-p_0(P)\log a+O(1)\)，可知 p_0(P)=0。
于是 (2) 在右半平面给 \(\mathscr A_P=0\)。恒等定理沿该单值
亚纯延拓成立，故所有极点的留数为零，即 2。

2 由绝对收敛的层重排直接推出 3。若 3 成立，(1) 的零端估计给

\[
p_0(P)=\lim_{u\downarrow0}u^4\Theta_P(u)=0,
\tag{6}
\]

因为 \(u^4G_P(u)\to0\)。于是 G_P=0，积分式给 1，并由 (2) 得
\(\mathscr A_P=0\)。最后，前轮证明所有候选极点都至多简单，
且没有其他有限奇点，所以由 (4)，4 与 2 等价。□

在 1 中，只需轮廓在任一非空正实开区间为零，就可先用右半平面
全纯性与恒等定理得出 1。类似地，两个四次方向 P、R 的轮廓在该
区间相同，当且仅当所有 \(W_P(\lambda)=W_R(\lambda)\)。

这里“留数决定完整函数”仅指 (1)–(2) 这个固定 theta 族；对一般
亚纯函数，当然可以添加任意整函数而保留留数。本案不能自由添加，
因为全部留数还固定了 theta、其零 Fourier 系数 p_0 和指定积分。

因此可见信息可准确写成

\[
\mathcal P_4/\mathcal N_q,\qquad
\mathcal N_q=\{P:W_P(\lambda)=0\text{ 对全部 }\lambda\in\mathcal E\}.
\tag{7}
\]

这不提供稳定的数值反演：从近似的局部解析数据继续到全部极点，
一般需要另外的误差／稳定性论证。本篇只有精确函数的唯一性结论。

## 3. 格点等距对称造成的不可见方向

定义固定格点二次型的整数等距群

\[
\mathcal H_q=\{S\in GL_4(\mathbb Z):S^{\mathsf T}\mathsf QS=\mathsf Q\}.
\tag{8}
\]

该群有限：S 的第 j 列是满足 \(q(v)=q(e_j)\) 的整数向量，
每列只有有限种可能，故所有矩阵只有有限种可能。不需要预先算出
群列表即可得此存在性；真正使用平均的数值实现仍需其完整清单。

置

\[
\Pi_qP(x)=\frac1{|\mathcal H_q|}\sum_{S\in\mathcal H_q}P(Sx).
\tag{9}
\]

逐个 S 换元 k↦Sk 是每个格点层的双射，因此
\(W_{P\circ S}(\lambda)=W_P(\lambda)\)。Gaussian 积分中换元
y=Sx，因 \(|\det S|=1\) 且 q 不变，也有
\(p_0(P\circ S)=p_0(P)\)。于是

\[
\boxed{W_{\Pi_qP}=W_P,\qquad
\mathcal L_{\Pi_qP}=\mathcal L_P,
\qquad K_{\Pi_qP}=K_P.}
\tag{10}
\]

平均算子满足 \(\Pi_q^2=\Pi_q\)，其像正是等距群不变四次多项式。
所以

\[
\ker\Pi_q\subseteq\mathcal N_q.
\tag{11}
\]

特别地，若某个 S 使 \(P\circ S=-P\)，所有层总和及完整轮廓都
为零。这个消失机制是有限层上的精确配对，不是积分尾项的偶然抵消。

本篇没有对一般 q 证明 (11) 是等号：一个不变多项式仍可能在每个
层上抵消。只知道对称群很小，也不能推出可识别性；下一节使用更强
且明确的层非共振条件。

## 4. 一个充分的非共振条件与有限重建公式

考虑条件

\[
q(k)=q(l),\quad k,l\in\mathbb Z^4\setminus\{0\}
\quad\Longrightarrow\quad l=\pm k.
\tag{12}
\]

一个足够条件是 \(\mathsf Q\) 的十个独立上三角实系数在 Q 上线性
无关。因为二次型值相等给它们的一个整系数线性关系，所以
\(k_i^2=l_i^2\)、\(k_ik_j=l_il_j\)，即
\(kk^{\mathsf T}=ll^{\mathsf T}\)。选 \(k_j\ne0\)，先得
\(l_j=\varepsilon k_j\)，再由第 j 列得每个
\(l_i=\varepsilon k_i\)，其中 \(\varepsilon\in\{1,-1\}\)。

没有为实际压力 Hessian 或真实 \(\mathsf Q\) 认证这种系数关系。
它是一个数学上的充分条件，不是由“看起来非对称”或浮点小误差
得到的诊断。

在 (12) 下，四次齐次性给 P(-k)=P(k)，因而

\[
W_P(q(k))=2P(k).
\tag{13}
\]

所有层总和为零时，P 在每个整数点为零，已可由逐变量的无限根
论证推出 P=0。还可给更明确的有限重建：取

\[
\mathcal V=\{k\in\mathbb Z_{\ge0}^4:1\le k_1+k_2+k_3+k_4\le4\},
\qquad |\mathcal V|=\binom84-1=69.
\tag{14}
\]

设 B 是 P 对应的对称四线性形式，\(P(x)=B(x,x,x,x)\)。多项式
展开给以下有限差分恒等式：

\[
24B(v_1,v_2,v_3,v_4)
=\sum_{S\subseteq\{1,2,3,4\}}
 (-1)^{4-|S|}P\left(\sum_{j\in S}v_j\right).
\tag{15}
\]

证明：把 \(P(t_1v_1+\cdots+t_4v_4)\) 展开并对每个 t_j 取
0、1 的差分。任何未含某个 t_j 的项都消去；总次数为四，唯一留下
的多次数是 (1,1,1,1)，其系数为 \(24B(v_1,v_2,v_3,v_4)\)。

让四个 v_j 分别取各基向量（允许重复），右侧的非零自变量均在
\(\mathcal V\) 中，空集项 P(0)=0。若多重指标 \(|\alpha|=4\)，
对应四个基向量组成列表 \(v_1,\ldots,v_4\)，则 P 中
\(x^\alpha\) 的系数是

\[
c_\alpha=\frac1{\alpha!}
\sum_{S\subseteq\{1,2,3,4\}}
 (-1)^{4-|S|}P\left(\sum_{j\in S}v_j\right).
\tag{16}
\]

由 (13)，所有这些评价值等于相应留数的一半。因此在 (12) 下，
固定至多 69 个已知层的精确留数就能重建 P 的全部 35 个系数。
该评价矩阵秩为 35，故其中存在一个 35 行子集仍可重建；本篇不
选择最优子集，也不提供条件数或扰动误差。

**推论。** 若 (12) 成立，\(\mathcal N_q=\{0\}\)，且
\(\mathcal L_P\equiv0\iff P=0\)。证明是 (13)–(16)，不是单纯
由亚纯延拓名称推断。

## 5. 对称测试二次型：可见维数恰为二

下面仅作明确的代数测试，取 \(q_\circ(x)=x_1^2+\cdots+x_4^2\)，
不声称它等于实际 \(2\pi^2D\)。整数等距矩阵的每列为长度一的
整数向量，故恰为带符号的置换矩阵。

先按各坐标符号平均，只有偶次单项式留下；再按坐标置换平均，
不变四次多项式恰为

\[
\Pi_\circ P=A\sum_i x_i^4+B\sum_{i<j}x_i^2x_j^2.
\tag{17}
\]

半径平方为 1 的层只有八个 \(\pm e_i\)，每个评价值为 A；半径
平方为 2 的层有 \(\binom42\cdot4=24\) 个两坐标为 ±1 的点，
每个评价值为 2A+B。因此

\[
W_P(1)=8A,\qquad W_P(2)=48A+24B.
\tag{18}
\]

两个层总和为零就迫使 A=B=0，而由 (10)，这时所有层都为零。
故在这个测试型中确有

\[
\mathcal N_{q_\circ}=\ker\Pi_\circ,\qquad
\dim\mathcal N_{q_\circ}=33,
\qquad \dim(\mathcal P_4/\mathcal N_{q_\circ})=2.
\tag{19}
\]

非零而完全不可见的一个调和例子是

\[
P_\circ(x)=(x_1^2-x_2^2)(x_3^2-x_4^2).
\tag{20}
\]

交换第 1、2 坐标使它变号而不变 q，因此全部 W、p_0、K 和
\(\mathcal L\) 都为零。直接求二阶导数，前两坐标的贡献相消，
后两坐标的贡献也相消，故 \(\Delta P_\circ=0\)。这给出了
“调和四次项非零仍不足以推出整个轮廓非零”的具体模型例子。
不能把这项测试压力或对称性移植到真实曲面。

## 6. 与前轮系数及原覆盖产品的关系

已有 \(K_P=\mathcal L_P(0)\) 只是一项线性泛函；此前径向例子
\(P=\alpha q^2\) 在 \(\alpha\ne0\) 时有 K=0，却有 p_0≠0 与
非零对数项。本轮的 (20) 则是非零调和 P 但整个轮廓恒零。
相反，若实际 q 另证 (12)，完整轮廓恒零就能推出真实 P=0。
这三种逻辑方向应分别记录。

| 子论证 | 支持 | 主要限制 |
| --- | --- | --- |
| 完整轮廓恰检测层总权重 | 既有简单留数式与本篇命题 1 | 精确唯一性不是稳定数值恢复 |
| 有限等距平均保留全部可见量 | 逐层整数换元及 Gaussian 换元 | 一般情形只证核包含，不宣称等号 |
| 非共振层可有限重建四次项 | ± 层判准、69 点差分公式 | 未为真实 Q 认证该条件或算留数 |
| 对称测试型可见维数为二 | 两个有限层的纸面完整分类 | 不是实际 D 或实际压力项的观测 |

没有提高 N 展开的速率，没有为原产品精确临界点赋有限值，没有
完成 deck action／primitive lift 的新实例检查，也没有构造算子或
证明全局行列式相等。这里的可识别对象是已定义辅助 theta 轮廓，
不是原 owner 数据或 Hilbert–Pólya 谱。

## 7. 来源、实际动作与保全

ARS 的有界 argument-builder 用于区分继承的解析结构、新核判准、
条件重建及非实际测试例。普通浏览复核 [DLMF §1.8(iv)][poisson]
的 Poisson 公式背景；四维加权式仍依据[前轮自含推导][harmonic]，
不将其或本篇的核／维数结果归给 DLMF。其余恒等式均在文内证明，
没有新颖性检索或原创优先权声称。

实际只新增本笔记，主线程追加总记录。所有 35／69／8／24／33／2
均为组合、线性代数或有限层的纸面计数，没有运行格点程序、符号
代数、积分、压力估计、实验、fixture、producer 或历史 writer。
未构建论文或改写旧稿、书目、冻结输入、协议、正式回执和失败记录。
FAIL / BLOCK、D06 Recovery 3、Route 与 Stage 5／6 边界保持。

[analytic]: internal_cubic_log_threshold_and_analytic_remainder_20260909.md
[harmonic]: internal_harmonic_quartic_finite_part_and_dual_lattice_series_20260908.md
[poisson]: https://dlmf.nist.gov/1.8#E14
