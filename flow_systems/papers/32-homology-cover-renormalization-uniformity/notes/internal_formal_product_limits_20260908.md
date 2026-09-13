# P32 内部研究：形式产品构造与阶乘序列的两类极限行为

记录日期：2026-09-08 UTC。接续[显式非真幂代表族及局部系数比较][owner-note]。本次在 R6 已定义的空间和拓扑中构造比较对象、证明极限行为；不修改论文、旧笔记正文、正式审查或锁定材料。

本次新增三个形式层结论：正 content 局部因子可以构成既有 `R_+` 中的明确产品；该产品沿固定 `N_k=k!` 收敛到不同于基准的形式极限；对一个零 content owner，相应序列在既有 Hahn 赋值拓扑中非柯西。它们是下述明确对象的数学结论，不是数值 Euler 产品、包含零 content 的全 owner 产品或正式 Route 判断。

## 1. 保持原有索引、类型与拓扑

`O_+` 指[原稿数学定义][owner-frame]中的全体有向本原曲面群共轭类里同调 content 为正者，而不是某次计算已经列出的有限名单。每个 `g in O_+` 有固定整数 `d(g)>=1`，不同 owner 使用独立变量 `u_g`。同调对共轭不变，所以 content 是该索引上的良定义函数。

沿用 [R6 的有限 owner／总次数双逆极限][carrier]：

\[
R_{F,D}=\mathbb Q[u_g:g\in F]/\mathfrak m_F^{D+1},\qquad
\mathfrak m_F=(u_g:g\in F),\qquad
R_+=\varprojlim_{(F,D)}R_{F,D}.
\]

这里 `F` 是 `O_+` 的任意有限子集，`D` 为非负整数。过渡映射先把被删除 owner 的变量置零，再截断总次数；各坐标取离散拓扑。以 `p_(F,D)` 表示坐标投影。相等要求所有坐标相等，收敛要求每个固定坐标最终精确稳定。

零 content 继续使用[另行定义的带标签纤维][zero-carrier] `H_g`，不与 `R_+` 合并。其系数为有理数，指数非负有理数、支撑良序；`v(a)` 为非零元素的最小支撑指数，约定 `v(0)=+infinity`。零邻域为 `U_r={a:v(a)>r}`。两种拓扑不是同一种收敛概念。

本笔记的正 content 比较 owner 记为

\[
g_{\mathrm{hc}}=[a_1^2[a_1,b_1]].
\]

它是上一份笔记族中的 `g_2`：非平凡、非真幂且 content 为 `2`，因此确实属于这里按数学定义取全体类的 `O_+`。这个标签不表示规范枚举的第二项，也不表示已生成其机器 owner 记录。零 content 例子记为 `g_zc=[[a_1,b_1]]`，外层括号表示有向共轭类；它对应上一笔记的 `g_0`。

## 2. 三个正 content 形式产品的构造

对整数 `N>=1`、`g in O_+`，令

\[
q_N(g)=\gcd(N,d(g)),\qquad
f_{N,g}=(1-u_g^{d(g)/q_N(g)})^{-q_N(g)},
\]

\[
b_g=(1-u_g^{d(g)})^{-1},\qquad
f_{*,g}=(1-u_g)^{-d(g)}.
\]

`d(g)/q_N(g)` 为正整数。以上元素均属于原有的单 owner 有限局部化 `A_{ {g} }`；它们各自只依赖自己的变量，且常数项为 `1`。

对每个 `(F,D)`，定义

\[
P^+_{N,F,D}=\left[\prod_{g\in F}f_{N,g}\right]_{\leq D},\qquad
B^+_{F,D}=\left[\prod_{g\in F}b_g\right]_{\leq D},\qquad
P^+_{*,F,D}=\left[\prod_{g\in F}f_{*,g}\right]_{\leq D}.
\]

`[ ]_(<=D)` 表示映入 `R_(F,D)`。因为每个 `u_g` 在此商环中幂零，所列分母都有有限几何逆，故这些有限乘积定义良好。`F` 为空时产品为 `1`。

若 `(F,D) <= (F',D')`，被删除变量的因子变成 `1`；剩余因子保持不变，进一步次数截断与乘法相容。因此

\[
\rho_{(F',D'),(F,D)}(P^+_{N,F',D'})=P^+_{N,F,D},
\]

另两族同理。由逆极限的定义，三族相容坐标分别确定明确元素

\[
\mathcal P_N^+,\quad\mathcal B^+,\quad\mathcal P_*^+\in R_+.
\]

这里已经指定了所有有限 `F,D` 的完整乘积，因而也指定了混合 owner 单项式的系数；不是仅由单变量投影倒推出一个“唯一全局对象”。

### 有限部分乘积网确实收敛

对有限 `E subset O_+`，用[既有有限嵌入][finite-domain]定义

\[
\mathcal P_{N,E}^+=j_E\!\left(\prod_{g\in E}f_{N,g}\right).
\]

有限子集按包含关系定向。其 `(F,D)` 坐标为

\[
p_{F,D}(\mathcal P_{N,E}^+)
=\left[\prod_{g\in E\cap F}f_{N,g}\right]_{\leq D}.
\]

一旦 `E` 包含 `F`，该坐标便精确等于 `P^+_(N,F,D)`，且以后不变。因此这个网收敛到 `mathcal P_N^+`。`mathcal B^+` 与 `mathcal P_*^+` 的部分乘积网同样收敛。这给出了“形式无限产品”记号在本拓扑下的明确含义。

证明使用“只依赖自身 owner 变量”与“常数项为一”两项条件。仅有常数项一并不足以推出任意无限乘积存在。每个 `(F,D)` 只包含有限多个单项式，不需要全体 owner 的解析可求和性；本构造也不要求所有 owner 在某个总次数层上具有全局有限支持。

有限子集网不依赖可数枚举或规范排序。这并没有给出冻结字长／字典序下的前缀完整性证书。也不能把这里的 `R_+` 无说明地替换为另一种无限变量完备化。

## 3. 沿整条固定阶乘序列的形式极限

仍取 `N_k=k!`，整数 `k>=1`。对每个固定有限 `F`，定义

\[
K_F=\max\bigl(\{1\}\cup\{d(g):g\in F\}\bigr).
\]

当 `k>=K_F` 时，对所有 `g in F` 同时有 `d(g)|k!`，因此 `q_(k!)(g)=d(g)`，从而在任何次数截断之前就有

\[
\prod_{g\in F}f_{k!,g}
=\prod_{g\in F}(1-u_g)^{-d(g)}.
\]

于是对每个固定 `(F,D)`，

\[
p_{F,D}(\mathcal P_{k!}^+)=p_{F,D}(\mathcal P_*^+)
\quad(k\geq K_F).
\]

按第 1 节的拓扑定义，得到

\[
\boxed{\mathcal P_{k!}^+\longrightarrow\mathcal P_*^+\quad\text{于 }R_+.}
\]

该阈值对固定 `F` 的所有 `D` 都适用，但不声称存在对所有有限 `F` 共同有效的阈值。`K_F` 只说明整条阶乘序列在该坐标何时稳定，没有另选控制序列；也没有把结论推广为任意趋于无穷的模数序列。

这里检验的是每个有限 `F` 上的全部混合项，不是只检验 singleton 投影。因此原稿关于 singleton 投影并不联合忠实的提醒仍然有效，并未被绕过。

## 4. 有限坐标见证极限不等于基准

取固定坐标 `(F,D)=({g_hc},1)`。因 `d(g_hc)=2`，对 `k>=2`，

\[
p_{\{g_{\mathrm{hc}}\},1}(\mathcal P_{k!}^+)
=p_{\{g_{\mathrm{hc}}\},1}(\mathcal P_*^+)
=1+2u_{g_{\mathrm{hc}}},
\]

\[
p_{\{g_{\mathrm{hc}}\},1}(\mathcal B^+)=1.
\]

该坐标环是 `Q[u_(g_hc)]/(u_(g_hc)^2)`，其中 `2u_(g_hc)!=0`。所以这不再是对未定义整体的猜测，而是两个已构造 `R_+` 元素在明确坐标上的差异：

\[
\boxed{\mathcal P_*^+\ne\mathcal B^+,\qquad
\mathcal P_{k!}^+\not\longrightarrow\mathcal B^+.}
\]

第二个结论也可直接从离散坐标看出：从 `k=2` 开始，该坐标一直为 `1+2u`，不可能最终等于基准坐标 `1`。其他 owner 的因子在这个坐标都变为 `1`，不能抵消该差异。这里使用的是有理数系数，特别是 `2!=0`。

这给出了正 content 形式产品的非基准极限结论；并未构造含零 content 的全 owner 乘法对象，也未宣称其有标量求值。

## 5. 零 content 单纤维中的非柯西序列

固定上面明确的零 content owner `g_zc`，简写同一纤维变量为 `z`。对整数 `N>=1`，把既有有限域中的

\[
a_N=(1-z^{1/N})^{-N}\in A^0_{g_{\mathrm{zc}},N}
\]

通过原有包含映射视为同一个 `H_(g_zc)` 的元素，然后比较不同 `N`。基底元素为 `b^0=(1-z)^(-1)=a_1`。这不是在不同 owner 的纤维间相减。

每一项都有合法展开

\[
a_N=\sum_{j\geq0}\binom{N+j-1}{j}z^{j/N}.
\]

其支撑为 `(1/N) Z_(>=0)`，是良序集；该展开可由有限个几何级数相乘得到。对固定 `N,M`，差的支撑包含于 `(1/lcm(N,M)) Z_(>=0)`，也合法。比较两项不要求所有 `N` 的支撑联合起来良序，本笔记也未据此定义无限和。

若 `N>M>=1`，两项的常数项都是 `1`，相减后抵消。`a_N` 的最小正指数是 `1/N`，系数为非零有理数 `N`；`a_M` 的最小正指数为 `1/M>1/N`。故

\[
\boxed{v(a_N-a_M)=1/N\qquad(N>M\geq1).}
\]

取固定零邻域 `U_(1/2)={a:v(a)>1/2}`。对任意尾端起点 `K`，选择 `k>=max(K,2)`，则 `k,k+1` 都在尾端内，而

\[
v(a_{(k+1)!}-a_{k!})=\frac1{(k+1)!}<\frac12.
\]

其差不在这个固定邻域里，否定了柯西条件。因此

\[
\boxed{(a_{k!})_{k\geq1}\text{ 在既定 }H_{g_{\mathrm{zc}}}
\text{ 的赋值拓扑中非柯西，因而不收敛。}}
\]

这里不需要假设该纤维完备；若一个序列收敛，则两个足够靠后的项之差必须落在任意给定零邻域中，与上述事实矛盾。对基底更有直接检验：`N>1` 时 `v(a_N-b^0)=1/N`，因此也不趋于基底。邻域要求严格大于 `1/2`，所以 `N=2` 时等于 `1/2` 仍不满足。

这是单 owner 的特定赋值拓扑结论，不是整个 `H_g` 的标量求值，不是本次证明的标量发散，也不构造跨零 owner 产品。

## 6. 形式结论怎样连接到项目问题

| 对象 | 本次已证明 | 仍不包含 |
| --- | --- | --- |
| 正 content 全体数学索引上的 `mathcal P_N^+`、`mathcal B^+` | 既有 `R_+` 中的相容坐标构造、有限部分乘积网收敛 | 数值 Euler 产品或已执行规范枚举 |
| `mathcal P_(k!)^+` | 收敛到 `mathcal P_*^+`，且明确一次项坐标排除基准极限 | 全局标量化、解析紧集上一致收敛或 AN-1–AN-5 |
| 固定零 owner 的 `a_(k!)` | 同标签 Hahn 赋值拓扑中非柯西 | 全零 owner 乘法对象或其他拓扑下的结论 |

这些形式产品的定义直接使用已经给出的局部表达式。把它们解释为规定几何覆盖的归一化产品，仍须保留[覆盖推导][cover-note]中的覆盖、物理时钟和因子计数前提；定义一个形式对象本身不认证具体几何输入。上轮显式族的群论与符号周期连接也不替代 `SG2OwnerCanonical-v1` 的一般接口、序列化和前缀证书。

对未来可能提出的全 owner 对象，存在一个有用但仍带前提的传递规则：若另行构造了拓扑对象 `A`、其中的序列 `X_k` 与基准 `X_base`，并证明连续映射 `Theta:A -> R_+` 满足

\[
\Theta(X_k)=\mathcal P_{k!}^+,\qquad
\Theta(X_{\mathrm{base}})=\mathcal B^+,
\]

则 `X_k` 不可能收敛到 `X_base`，否则连续性将与第 4 节矛盾。这里没有假设 `A` 或 `Theta` 已经存在；尤其，原有零 content 带标签的不交并本身没有提供这种全 owner 对象或删除零分支的映射。

因此，“正 content 形式产品已有不同极限”可以明确记录；“原项目任何全 owner 解析产品都已被否定”仍不能由此直接宣布。没有新增整个 `R_+` 或 `H_g` 上的标量映射，没有启动 content-one 解析阶段，也没有修改正式 Route／恢复／障碍状态。

## 7. 本次核对与保存范围

按 ARS 的论证流程，本笔记把对象构造、坐标兼容、阶乘稳定、有限反例和零纤维拓扑分开证明。三个只读推敲任务分别检查了正产品构造、阶乘极限及零纤维非柯西论证；主线程整合并写出证明，同系助手的一致意见不作为独立科学证据。

本次未新增外部定理或来源查询；索引、拓扑与局部表达式依据下列既有材料，新增结论由正文论证支持。文件检查只核对局部引用、关键条件及原有文本的追加保留，不认证数学正确性。没有运行科学实验、枚举、数值计算、既有审查脚本或论文构建；只新增此内部笔记，并在上轮笔记及总内部记录中追加入口。

[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[owner-frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:188
[carrier]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:720
[finite-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:764
[zero-carrier]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778

## 后续内部推导入口（2026-09-08）

后续见[辅助分量记录与连续读出下的恢复极限障碍](internal_componentwise_recovery_obstruction_20260908.md)：另行定义只并列记录既有正分量与各零纤维的辅助拓扑空间，证明固定阶乘序列在其中没有极限，并明确这种障碍向其他空间传递所需的固定、精确、连续读出条件。辅助空间不替代原 `R_0`，也不是全 owner Euler 乘法对象；原文、论文及正式审查状态保持不变。
