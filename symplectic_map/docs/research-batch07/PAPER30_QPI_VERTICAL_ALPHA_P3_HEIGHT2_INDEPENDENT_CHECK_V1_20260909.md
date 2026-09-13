# Paper30 qPI：$p=3,a=2$ 第一末端有限 probe 独立核查 V1

日期：2026-09-09。类型：非作者独立数学／有限精确计算核查。
本件只接受下列明确边界内的 H2.1–H2.3，不替代全图接口证明，也不启动一般高度或完整初始理想研究。

## Claim

固定 $p=3,a=2,m=1,N=9$，
$q=\zeta_9=1+\pi$，$t=t_\delta=1+\delta\pi$，$\delta\in\{0,1\}$。
仅使用第一末端图
$$x=u^{-1},\quad y=W=1+uv,\quad J_t=W-v/W-tu,$$
以及原点 $P_0:(u,v)=(0,0)$ 的完成局部环
$$R=\widehat{\mathbb Z[\zeta_9]_{(\pi)}}[[u,v]],\qquad
\mathfrak m=(\pi,u,v).$$
记实际规范化的一形式与切向楔积系数为
$$\alpha_9=\frac19d_{\rm state}I_9=A_u\,du+A_v\,dv,\qquad
T=A_u(J_t)_v-A_v(J_t)_u,\qquad S=u+v.$$
这里状态微分固定 $q,t$，且始终保留 $du,dv$ 两个分量。

所核查的结论逐项为：

1. 作者式 (12)–(13) 的完整点多项式、式 (1) 的四个精确点值、式 (14) 的两个精确 $T(P_0)$ 都正确。
   四个系数的 $\pi$ 赋值都是二，两个 $T(P_0)$ 的赋值都是四。
2. 作者式 (15) 给出 $A_u,A_v$ 至四阶的完整双状态 jet。
   两系数零、一次齐次项为零，二次项均为 $\pi^2$。
   $T$ 的零至三次项为零，且
   $$T_4=(1+\delta)\pi^4+2\pi^3u+\pi^3v+2\pi S^3.$$
3. 对实际系数理想 $I=(A_u,A_v)\subset R$，令
   $$L_\delta=(1+\delta)\pi^2+2\pi u+\pi v,\qquad
   F=A_u,\qquad G=T-L_\delta A_u.$$
   则确有 $I=(F,G)$，其首式分别为 $\pi^2,2\pi S^3$，且仅在明确范围内有
   $$\bigl(\operatorname{in}_{\mathfrak m}I\bigr)_d
   =(\pi^2,\pi S^3)_d,\qquad 0\leq d\leq4.$$

## Status

**PROVABLE AS STATED / PASS（仅上述有限 Claim）。**

原 H2.1–H2.3 无须改弱，也未发现阻断其成立的硬缺口。
接受依赖于作者已明确列出的第一末端正则矩阵与原模型接口；本轮重新核查了实际九插入归一化，
但没有重开此前全图 gauge 接口证明。
脚本运行成功只是执行证据；接受还依赖下文的精确递推、独立实现、精度证明和理想论证。

## Assumptions and Read Boundary

全文读取并核查的本轮两个冻结输入仅为：

| 输入 | 全文范围 | SHA-256 |
|---|---:|---|
| [作者 probe](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.md) | 1–214 行；13,175 字节 | ef8e53646e2b5b702d5ae3e130a5fd14e8bcfd73d0e0a61db861a82730706a97 |
| [作者有限精确脚本](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.py) | 1–171 行；7,071 字节 | 26096c03b278415573564d6ff3aed945f4691c07d9b9df8a3c9b0b97e5597693 |

核查角色是曾参与本方向查新和此前有限审查的非作者代理，不是 fresh-eyes 审查者；
没有参与本轮作者 probe 或脚本的编写。
本轮没有读取新 global-firstjet、一般 $m$ 或更高迭代文件及其审查，
也未把已接受的 height-one 理想作为本高度的证明输入。
使用 proof-writer 的 Claim／输入／依赖／证明／未完成范围结构；未做 Route A/B 评分。
除本报告外不新增持久化脚本；作者件及此前冻结检查均未修改。

输入矩阵固定为作者式 (6)：
$$\widehat A(Z)=M_0+ZM_1+Z^2M_2,$$
$$M_0=\begin{pmatrix}t-v&-1\\-v(t-v)&v\end{pmatrix},\qquad
M_1=\begin{pmatrix}J_t-1&u\\v-t+v^2/W&1\end{pmatrix},\qquad
M_2=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$
所有分母均为 $W$ 的幂，故在 $R$ 内为单位。
使用作者给定的原谱乘积／gauge 接口，不另换矩阵、谱顺序、系数抽取或归一化。

## Notation

$\mathcal O=\mathbb Z[\zeta_9]_{(\pi)}$，$\widehat{\mathcal O}$ 为其 $\pi$-进完成。
$\operatorname{ord}_{\mathfrak m}$ 指局部环的 $\mathfrak m$ 阶；
$v_\pi$ 指点上离散赋值环的赋值，二者不可在保留状态变量时互换。
下文齐次式的系数属于 $\mathbb F_3$，并以相同符号 $\pi,u,v$ 表示关联分次变量。
精确点多项式则始终在混合特征环中解释，不把其整数系数先取模三。
$O(\mathfrak m^r)$ 是真实局部余项。
状态一形式使用相对 $\widehat{\mathcal O}$ 的连续微分，即自由模 $R\,du\oplus R\,dv$；
不以未完成的绝对 Kähler 微分模块替换它。

## Proof Strategy

先证明可用的混合特征精度和归一化，再把有限卷积拆成两个不同表示的独立计算：
点上采用整系数九因子及其两个状态导数的同步传播；
状态 jet 则先对精确有理矩阵微分，采用额外缩放变量记录总次数，再从另一乘法方向形成同一个有序八因子积。
最后直接证明低阶初始理想结论，不从计算软件输出推断完整 Gröbner 基。

## Dependency Map

1. 圆分展开与局部正则性给 $v_\pi(3)=6$ 和 $\operatorname{gr}_{\mathfrak m}R=\mathbb F_3[\pi,u,v]$。
2. 原谱乘积的九个插入项通过循环迹及 $q^9=1$ 相等，给准确的 $1/9$ 归一化。
3. 有序有限卷积及两完整插入矩阵给式 (12)–(14)，赋值判断依赖第 1 项。
4. 有理矩阵先微分、总阶精度控制与有限卷积给式 (15)；实际 $dJ_t$ 给 $T_4$。
5. $(J_t)_u$ 为单位给实际二生成元变换；关联分次环为整环排除四阶以下的隐藏消去。

## Proof

### Step 1. 混合特征与微分前后精度

直接展开可得
$$\Phi_9(1+\pi)=
\pi^6+6\pi^5+15\pi^4+21\pi^3+18\pi^2+9\pi+3
=\pi^6+3U,$$
$$U=1+3\pi+6\pi^2+7\pi^3+5\pi^4+2\pi^5.$$
$U$ 的剩余类是一，故为单位，因而 $3=-\pi^6/U$ 及 $v_\pi(3)=6$。
$\Phi_9(1+\pi)$ 对素数三是 Eisenstein 多项式；本地圆分环为以 $\pi$ 为参数、
剩余域为 $\mathbb F_3$ 的离散赋值环。
因此 $R$ 是三维正则局部环，以 $\pi,u,v$ 为正则参数，
$$\operatorname{gr}_{\mathfrak m}R\cong\mathbb F_3[\pi,u,v].$$
所用一般事实的条件正是此处的正则局部性，见
[Stacks Project, Lemma 10.106.1](https://stacks.math.columbia.edu/tag/00NN)。
这里的关联分次环没有全局关系 $\pi^6=0$；
该关系仅在本轮使用的有限商中出现：
$$R/\mathfrak m^6\cong
\mathbb F_3[\pi,u,v]/(\pi,u,v)^6.$$
所以输出总阶零至五可在此特征三商内计算，不能据此在六阶或更高继续照抄同一算术。

微分精度要单独检查。为确定一次状态导数的总阶至五，
矩阵须先保留总阶至六；被丢掉的 $\mathfrak m^7$ 项在一次状态微分后属于 $\mathfrak m^6$。
作者脚本确实先用次数六构造 $W^{-1}$ 和矩阵，再微分、截到五。
此外，先取系数模三不会把被丢弃的三倍项通过状态微分重新带入五阶：
对每个状态导数 $D$ 都有 $D(3f)=3D(f)$，理想 $(3)$ 被 $D$ 保持，
故导数仍属于 $(3)\subset\mathfrak m^6$。
这一点依赖“状态微分不作用于三或 $\pi$”，不能仅以总阶通常下降一阶来代替论证。
在辅助特征三六阶表示中，单独的 $\pi^6$ 项状态导数为零；
含 $\pi^6$ 且含状态变量的项总阶至少七，微分后仍不影响五阶。

独立实现采用更直接的检查路线：先对原有理矩阵在特征零符号层面求状态导数，
然后令 $(\pi,u,v)=(\varepsilon P,\varepsilon U,\varepsilon V)$，展开至 $\varepsilon^5$ 并取模三。
因此它不复用作者“先作有限多项式再微分”的实现步骤。
两条路线所需的精度均在本节已证明的范围内。

### Step 2. 规范化、次序与两个插入矩阵

对原九因子乘积作状态微分，每个因子各产生一次插入。
把任一项作迹的循环移位，再整体缩放谱变量以令插入点位于 $Z$，
只对所抽取系数 $[Z^9]$ 产生因子 $q^{9j}=1$。
循环后剩余因子的顺序仍是 $q^8,q^7,\ldots,q$。
故九个系数在特征零中相同，先求和除以九恰得到
$$\alpha_9=[Z^9]\operatorname{tr}
\left(d\widehat A(Z)\widehat A(q^8Z)\cdots\widehat A(qZ)\right).$$
这既不是特征三中的除法，也未使用不相邻矩阵交换。

点上直接对原矩阵求导得到
$$\widehat A(P_0;Z)=
\begin{pmatrix}t+Z^2&-1\\-tZ&Z\end{pmatrix},$$
$$D_u(Z)=Z\begin{pmatrix}-t&1\\0&0\end{pmatrix},\qquad
D_v(Z)=\begin{pmatrix}-1&0\\-t&1\end{pmatrix}
+Z\begin{pmatrix}-1&0\\1&0\end{pmatrix}.$$
其中 $D_v$ 的常数矩阵不可遗漏；$(J_t)_u(P_0)=-t$，
$(J_t)_v(P_0)=-1$ 同时已核。

作者循环 $k=8,7,\ldots,1$ 时把新因子乘在当前乘积右侧，
对应其式 (10) 的有序卷积。每个因子的谱次数非负，
所以丢弃 $Z^{10}$ 及以上不可能影响 $[Z^9]$。
独立点实现则传播完整九因子乘积在点上的值 $B$ 及两个一阶状态导数 $C_u,C_v$：
对 $k=8,7,\ldots,0$ 依次更新
$$B'=B F_k,\qquad C_j'=C_jF_k+B\,D_j(q^kZ),\qquad
F_k=\widehat A(P_0;q^kZ),\quad j\in\{u,v\},$$
右端全部使用旧值，初值为 $B=I_2,C_u=C_v=0$。
该实现把九个插入项全部累加后读取 $[Z^9]\operatorname{tr}(C_j)$，
检查其每个整系数可被九整除，再除以九。
它不是调用作者的八因子插入函数，因而同时独立检查了规范化。
只传播点值及一阶导数，没有展开含完整状态变量的 $I_9$。

### Step 3. 完整点多项式和准确赋值

独立点计算使用整数稀疏多项式，单项式由谱次数、$q$ 次数、$t$ 次数组成，
在每次乘法中通过 $q^6=-q^3-1$ 精确约化。
九插入和除以九后，得到
$$\begin{aligned}
A_u(P_0)={}&-4q^5t^4+q^5t^3+2q^4t^4-2q^3t^4+3q^3t^3\\
&+q^2t^4-6q^2t^3-5qt^4+7qt^3-6qt^2\\
&-t^5+3t^4-2t^3+t^2-t,
\end{aligned}$$
$$\begin{aligned}
A_v(P_0)={}&q^5t^3-2q^5t^2-5q^4t^3+7q^4t^2+7q^3t^3-6q^3t^2+q^3t\\
&-4q^2t^3+3q^2t^2-6q^2t-3qt^3-q-t^4+5t^3+t^2.
\end{aligned}$$
与作者式 (12)–(13) 的每个 $q,t$ 系数一致，不仅是检查 $t=1,q$ 两个代入点。
随后分别代入 $t=1,q$，再次圆分约化，再令 $q=1+\pi$，独立恢复：
$$\begin{aligned}
A_u(P_0;1)&=-3\pi^5-13\pi^4-21\pi^3-20\pi^2-18\pi-9,\\
A_v(P_0;1)&=-\pi^5-3\pi^4+\pi^2-9\pi-3,\\
A_u(P_0;q)&=-15\pi^5-63\pi^4-114\pi^3-116\pi^2-66\pi-24,\\
A_v(P_0;q)&=-11\pi^5-48\pi^4-97\pi^3-113\pi^2-66\pi-27.
\end{aligned}$$
再由 $T(P_0)=tA_v(P_0)-A_u(P_0)$，在同一圆分环内约化，得到
$$\begin{aligned}
T(P_0;1)&=2\pi^5+10\pi^4+21\pi^3+21\pi^2+9\pi+6,\\
T(P_0;q)&=22\pi^5+83\pi^4+135\pi^3+135\pi^2+72\pi+30.
\end{aligned}$$
这两个多项式的全部整数系数也与作者式 (14) 一致。

整数 $n\ne0$ 满足 $v_\pi(n\pi^k)=6v_3(n)+k$。
上述标准表示的 $\pi$ 次数均在零至五之间，不同次幂项的赋值模六不同，
因此最低赋值项若唯一就不能被其他项抵消。实际逐项结果如下：

| 点上系数 | 唯一最低赋值项 | 准确赋值 | 首单位剩余类 |
|---|---|---:|---:|
| $A_u(P_0;1)$ | $-20\pi^2$ | 2 | 1 |
| $A_v(P_0;1)$ | $\pi^2$ | 2 | 1 |
| $A_u(P_0;q)$ | $-116\pi^2$ | 2 | 1 |
| $A_v(P_0;q)$ | $-113\pi^2$ | 2 | 1 |
| $T(P_0;1)$ | $10\pi^4$ | 4 | 1 |
| $T(P_0;q)$ | $83\pi^4$ | 4 | 2 |

由离散赋值环的理想分类，两提升在指定零截面评价后的系数理想均为 $(\pi^2)$。
这一步不提供 $R$ 中的完整双状态系数理想。

### Step 4. 双状态 jet 和实际切向首式

独立状态计算在 $\mathbb F_3[\varepsilon,P,U,V,Z]$ 中使用总次数缩放，
每次乘法只保留 $\varepsilon$ 次数至五、谱次数至九。
这里用完整有理矩阵的导数 $\mathcal D_j(Z)=\partial_j\widehat A(Z)$，$j\in\{u,v\}$，
不使用 Step 2 已评价到点上的 $D_j(Z)$ 代替状态导数。
已精确微分的 $\mathcal D_u,\mathcal D_v$ 与原矩阵分别展开；
独立实现对 $k=1,\ldots,8$ 把 $\widehat A(q^kZ)$ 左乘到当前乘积，
最终顺序仍是 $\widehat A(q^8Z)\cdots\widehat A(qZ)$。
这与作者从八降到一、右乘的写法方向不同而数学目标相同。
最后收缩两个完整插入矩阵，抽取 $[Z^9]$，分别比较每个零至四阶系数。

两种 $\delta$ 的全部断言通过，结果统一为
$$\begin{aligned}
A_u={}&\pi^2+\pi^2u+
2(1-\delta)\pi^4+\pi^3u+\pi^2vS+\delta\pi S^3+2S^4
+O(\mathfrak m^5),\\
A_v={}&\pi^2+\pi^2v+2\delta\pi^3+
(1+\delta)\pi^3v+2\pi^2uS+2(1-\delta)\pi S^3+2S^4
+O(\mathfrak m^5).
\end{aligned}$$
这就是作者式 (15)，不是在 $u=0$ 或 $v=0$ 上的限制式。
零至一次项均为零、二次项均为 $\pi^2$，于是
$$\alpha_9\in\mathfrak m^2(R\,du\oplus R\,dv)
\setminus\mathfrak m^3(R\,du\oplus R\,dv),\qquad
\operatorname{in}_2(\alpha_9)=\pi^2(du+dv).$$
独立实现还输出五阶项供余项一致性核对；本报告不据此扩大初始理想的接受范围。

从精确 $J_t$ 微分而不是用点上导数代替整个状态邻域，得到
$$ (J_t)_u=-1-\delta\pi+v+v^2+O(\mathfrak m^3),\qquad
(J_t)_v=-1+u+2uv+O(\mathfrak m^3).$$
由于 $A_u,A_v\in\mathfrak m^2$，这些二阶导数 jet 已足够计算 $T$ 至四阶。
代入后分别核得 $T_0=T_1=T_2=T_3=0$，并得到
$$T_4=(1+\delta)\pi^4+2\pi^3u+\pi^3v+2\pi(u+v)^3.$$
其点上四阶项分别为 $\pi^4$ 与 $2\pi^4$，与 Step 3 的混合特征精确赋值一致。
纯状态四阶项 $2S^4$ 在两个系数中均非零：
若完整系数可被 $\pi^2$ 整除，其四阶齐次式也必须被 $\pi^2$ 整除，和该项矛盾。
因此点上的公共因子不能提升成完整邻域内的 $\pi^2$ 整除性。

### Step 5. 实际二生成元和只到四阶的初始理想

$J_u=(J_t)_u\equiv-1\pmod{\mathfrak m}$ 为单位。设 $J_v=(J_t)_v$，
则在实际局部环中有准确的矩阵关系
$$\begin{pmatrix}F\\G\end{pmatrix}
=
\begin{pmatrix}1&0\\J_v-L_\delta&-J_u\end{pmatrix}
\begin{pmatrix}A_u\\A_v\end{pmatrix}.$$
该矩阵行列式为 $-J_u$，是单位，故 $I=(F,G)$ 是真实的理想等式，
不是仅对首式或楔积的替换。
$L_\delta$ 是二阶齐次多项式，Step 4 给出
$$\operatorname{ord}_{\mathfrak m}F=2,\quad F_2=\pi^2,\qquad
\operatorname{ord}_{\mathfrak m}G=4,\quad G_4=2\pi S^3.$$
在两个 $\delta$ 值下，独立计算也直接检查了 $G_0,\ldots,G_3$ 为零及此四阶式。

现取任意 $h=aF+bG\in I$。
关联分次环为整环，所以对非零 $a$ 有
$\operatorname{ord}_{\mathfrak m}(aF)=\operatorname{ord}_{\mathfrak m}(a)+2$；
而 $bG$ 若非零，其阶至少四。
若 $a$ 的阶为零或一，$aF$ 的二或三阶首式不可能被 $bG$ 取消，
所得首式分别为 $\pi^2$ 乘以相应次数的齐次式。
特别地，若 $h\in\mathfrak m^4$，必有 $a\in\mathfrak m^2$，
从而其四阶齐次项为
$$h_4=\pi^2a_2+2b_0\pi S^3.$$
这证明初始理想零至四阶各部分都包含于 $(\pi^2,\pi S^3)$ 的对应部分。
反向包含由 $F$ 的常数、一次、二次倍数以及 $G$ 的常数倍数给出。
这些项的任意非零齐次组合也是相应乘积之和的首式，故得
$$\bigl(\operatorname{in}_{\mathfrak m}I\bigr)_d
=(\pi^2,\pi S^3)_d\quad(0\leq d\leq4).$$
零、一次部分均为零；二、三、四次部分分别为
$$\mathbb F_3\pi^2,\qquad
\pi^2\mathbb F_3[\pi,u,v]_1,\qquad
\pi^2\mathbb F_3[\pi,u,v]_2+\mathbb F_3\pi S^3.$$
该证明没有排除更高阶首式之间发生消去后产生新的初始生成元。
因此既不推出完整初始理想等式，也不推出 $I=(\pi^2,\pi S^3)$。有限 Claim 证毕。

## Actual Verification

1. 实际执行冻结脚本：
   <code>python -B docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.py</code>。
   退出码为零；输出六个精确点多项式、两个提升的 $A_u,A_v,T$ 零至五阶，
   并通过脚本自身的精确点表示／状态 jet 表示一致性断言。
2. 另外实际执行一份内存中的整系数九因子值／导数传播实现。
   退出码为零；验证九插入和的每个标准整系数可被九整除，
   与作者式 (12)–(13) 的全部系数相等，恢复式 (1)、(14) 的全部系数，
   并逐项断言上述六个准确赋值。没有导入作者脚本的计算函数。
3. 另外实际执行精确有理求导／缩放变量／左乘积的内存实现。
   退出码为零；两个 $\delta$ 的式 (15) 每个零至四阶系数、
   $T$ 的零至三阶消失与四阶式、变换后 $G$ 的首四阶均通过精确断言。
   五阶输出与作者逐项输出也作了一致性核对，但未把它包装成更广理想结论。
4. 手工检查圆分等式、局部环适用条件、微分前多留一阶、两个插入矩阵、
   次序保持、单位行列式及低阶取消论证；不是只复述脚本打印的 PASS。
5. 所有计算均为整数／有理函数符号计算或有限域精确运算；未使用浮点拟合、GPU、外部求解器或第二持久化脚本。

## Corrections or Missing Assumptions

无须修改本轮作者 Claim，也没有发现必须补入的科学假设。
本报告把两个容易误读之处展开为明确论证：
状态微分保持理想 $(3)$，以及实际生成元变换的单位行列式。
这是对既有有限证明的核实与解释，不是授权修改冻结作者件。
完成环上的微分按连续相对状态微分解释，与作者所用的 $du,dv$ 一致。

## Open Risks and Explicit Nonclaims

- 全图 gauge／原模型接口是明确输入，本轮没有重审；结论没有超出给定第一末端矩阵。
- 点理想 $(\pi^2)$、完整双状态理想 $I$、低阶初始理想信息是三个不同对象。
- 未计算完整初始理想、完整形式正规形、完整零概形、局部长度或高阶 syzygy。
- 不推断整条末端仿射线、全局曲线、其他末端点、其他状态、其他 Hasse 根或奇异能级。
- 不推广到 $a>2$、其他素数、$m>1$、全部时间提升或任何一般高度迭代。
- 不把有限精确算术证书等同于数值观察，也不把本轮 PASS 等同于 Route 评价、论文完成或投稿验收。

## Artifact State

本轮唯一新增持久化产物为本报告。
两个冻结输入在交付前再次核对，SHA-256 均与上表一致；未修改作者件和旧审查件。
报告自身的最终行数、字节数和 SHA-256 在最终交接中列出，避免在文件内自指式记录自身哈希。
最终结论：接受准确限定的 H2.1–H2.3；本轮有限核查完成，无待修硬缺口。
