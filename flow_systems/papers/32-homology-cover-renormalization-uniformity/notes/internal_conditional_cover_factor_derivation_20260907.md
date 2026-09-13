# P32 内部研究：纯同调覆盖局部因子的条件推导

记录日期：2026-09-07 UTC。用途：接续[上一份推导链笔记][chain]，新增一条自包含的条件证明；仅作内部研究记录，不改写当前 R6 稿件、正式审查状态或锁定材料。

本次结果：在下列明确的覆盖、基轨道最小周期与因子计数假设下，导出 deck 阶、提升分量数、最小提升周期、两项固定归一化及有限形式代表。正 content 与零 content 分开证明。这里证明条件命题，不声称已经为 P32 的具体 owner 提供输入表示、群本原证据或长度认证。

定义与目标沿用[当前 R6 对象及归一化][frame]、[候选因子与中间字段][targets]、[有限定义域][domains]。这些链接支持“研究对象如何规定”，不充当下面新证明的外部正确性证书。

## 1. 假设与计数约定

以下假设逐项列明；本笔记不以“genuine cover”一词替代它们。

- **H0（固定基底与标记）**：基底为闭双曲亏格二曲面 `Sigma`，使用单位速度测地流；给定标记
  \[
  \Gamma=\langle a_1,b_1,a_2,b_2\mid[a_1,b_1][a_2,b_2]=1\rangle.
  \]
  同调向量按此标记的四个坐标记录，两个方向不合并。
- **H1（规定的覆盖）**：对所讨论的正整数 `N`，给定连通、正规、无分歧、局部等距覆盖 `p_N: Sigma_N -> Sigma`，且在 H0 标记下确实对应 `H_N = ker(Gamma -> (Z/NZ)^4)`。覆盖使用拉回度量，未缩放的提升流保持原来的物理时间参数。本笔记把该几何覆盖及其与 `H_N` 的对应作为假设，不另给具体矩阵模型或覆盖构造认证。
- **H2（实际轨道条件）**：给定一条有向周期流轨道 `gamma`，其最小正周期确为 `ell > 0`；其曲面投影的定向环路类在 H0 标记下具有同调向量 `v=(v_1,...,v_4) in Z^4`。若用项目 owner 标签 `g` 指代它，还假设该标签确实绑定这条轨道和这个 `ell`。以下证明不从任意群字、任意正参数或未核验的矩阵反推这项条件。
- **H3（局部因子与归一化约定）**：周期为 `T` 的一条本原有向流轨道贡献 `(1-exp(-sT))^(-1)`；对固定基轨道之上的每条不同提升轨道恰计一次。不再按 deck 对称或反向取商。先把提升周期乘 `1/N`，再把这个有限分量乘积的对数乘 `1/N^3`。本笔记取实数 `s>0`，使用实对数。该 Euler 因子是这里定义的局部乘积约定，不是由谱算子、迹恒等式或无限行列式新推得的结论。

H2 的“本原”在本证明中仅指流的最小周期；它不自动提供项目所需的群共轭类非真幂证书，更不意味着同调向量的 content 等于一。零向量与可整除的非零同调向量均须保留。

## 2. 从标记到纤维返回平移

H0 的 relator 是交换子的乘积，在阿贝尔化后不施加任何额外关系。因此四个生成元的指数和给出 `Gamma_ab = Z^4`：一方面任意到阿贝尔群的映射只由四个像决定，另一方面四个任意阿贝尔群元素自动满足该 relator。这也给出正反向的生成元映射，故不是只宣称一个商映射。

模 `N` 约化满射到

\[
D_N=(\mathbb Z/N\mathbb Z)^4,\qquad
\Gamma/H_N\cong D_N,\qquad |D_N|=N^4.
\]

由 H1，覆盖的 deck 群与此商群相识别。考察诱导的单位切丛覆盖

\[
P_N=T^1p_N:T^1\Sigma_N\longrightarrow T^1\Sigma.
\]

每个基底单位切向量在每一张 sheet 上有唯一提升，故纤维有 `N^4` 个点。局部等距使提升测地流 `tilde_phi_t` 与基流 `phi_t` 满足 `P_N tilde_phi_t = phi_t P_N`，deck 变换也与提升流交换。

固定轨道上的点 `x`，令 `E=P_N^(-1)(x)`。连通正规覆盖使 `E` 成为 `D_N` 的自由且传递的作用集。选一个提升 `tilde_x_0` 后以 `a in D_N` 标记 `a tilde_x_0`。按 H1 的商群覆盖对应，沿 H2 的定向环路提升一次，其端点标签增加 `bar_v = v mod N`；单位切向量的提升由同一个局部等距唯一决定，因此诱导切丛覆盖的返回也具有这个标签变化。这里按该方向选择加法标记；没有另作方向商。

记一次基周期的返回为 `R=tilde_phi_ell|_E`。于是

\[
R(\widetilde x_0)=\bar v\widetilde x_0,\qquad
R(a\widetilde x_0)=aR(\widetilde x_0)
=(a+\bar v)\widetilde x_0.
\]

所以返回置换正是 `a -> a+bar_v`。这一步来自规定的覆盖、环路类与流提升，不是从目标因子指数倒推 deck action。

## 3. 平移阶、循环数与本原提升周期

### 3.1 正 content：整数最小阶

设 `v != 0`，定义

\[
d=\gcd(|v_1|,\ldots,|v_4|)>0,\quad
q=\gcd(N,d),\quad n=N/q,\quad w_i=v_i/q.
\]

这些都是整数，且 `gcd(n,w_1,...,w_4)=1`。对正整数 `k`，

\[
k\bar v=0
\ \Longleftrightarrow\ N\mid kv_i\quad(\forall i)
\ \Longleftrightarrow\ n\mid kw_i\quad(\forall i).
\]

由整数 Bézout 恒等式，存在整数 `A,B_i` 使 `An+sum_i B_i w_i=1`。若右侧整除条件成立，两边乘 `k` 即得 `n|k`；反之 `k=n` 满足全部条件。因此最小正返回倍数为

\[
h=\operatorname{ord}_{D_N}(\bar v)=N/q.
\]

所有平移循环的长度均为 `h`：`a+k bar_v=a` 的条件与起点 `a` 无关。因此循环数为

\[
c=|D_N|/h=N^4/(N/q)=N^3q.
\]

部分坐标为零不影响此证明；也没有把“流本原”偷换为 `d=1`。

### 3.2 零 content：单独的恒等返回

设 `v=0`。一次返回平移就是恒等映射，因此每个纤维点自成一个循环，直接得到

\[
h=1,\qquad c=N^4.
\]

这里没有使用含 `ell/d` 的正 content 表达式，也没有把 `d=0` 塞进其形式定义域。

### 3.3 循环与提升轨道一一对应

任取一个纤维点 `tilde_x`。若它位于长度为 `h` 的返回循环中，则 `tilde_phi_(h ell)(tilde_x)=tilde_x`。同一循环的点由整数倍 `ell` 的流动连接，因而位于同一条提升轨道。

反过来，如果两个纤维点 `tilde_x,tilde_y` 位于同一提升轨道，写成 `tilde_y=tilde_phi_t(tilde_x)`。投影后有 `phi_t(x)=x`。H2 的最小周期条件推出 `t in ell Z`：用 `t` 除以 `ell` 所余的 `r in [0,ell)` 也是返回时间，最小性迫使 `r=0`。故这两个点位于同一个返回循环。

此外，任何正提升返回时间 `T` 投影后都必须等于 `k ell`，其中 `k` 是正整数；返回条件再迫使 `h|k`。所以每条提升轨道的最小正周期恰为

\[
T_{\mathrm{lift}}=h\ell.
\]

因此第 3.1、3.2 节的循环数确实是不同本原有向提升流轨道的数目，而不是对重遍历的重复计数。证明在单位切丛中工作，基测地线在曲面上的自交不影响该对应：位置重复而方向不同并不是相同的单位切丛点。

Deck 在点上的自由作用不意味着每条轨道的集合稳定子平凡。平移模型下，该稳定子恰为 `<bar_v>`，阶为 `h`，其作用对应整数倍 `ell` 的时间平移。故不能因 deck 作用自由就把所有情形都计成 `N^4` 条轨道，也不能额外对这些轨道取 deck 商。

## 4. 原始乘积与两项固定归一化

对固定基轨道 `g`，先写出完全未归一化的有限提升乘积。第 3 节给出 `c` 条轨道，所有最小周期都是 `h ell`，所以按 H3

\[
U_{N,g}(s)
=\prod_{j=1}^{c}(1-e^{-sT_j})^{-1}
=(1-e^{-sh\ell})^{-c}.
\]

第一步只缩放物理时间，得到

\[
V_{N,g}(s)=U_{N,g}(s/N)
=(1-e^{-sh\ell/N})^{-c}.
\]

第二步只缩放这个乘积的对数，定义

\[
F_{N,g}(s)
=\exp\!\left(N^{-3}\log V_{N,g}(s)\right)
=(1-e^{-sh\ell/N})^{-c/N^3}.
\]

对 `s>0, ell>0`，相关底数在 `(0,1)` 内，以上实对数与指数运算均有定义。第二步不是计算 `N^(-3) V`，也不是再次缩放周期。

| 分支 | 未缩放最小周期 | 时间缩放后周期 | 原始分量指数 `c` | 对数归一化后指数 |
| --- | --- | --- | --- | --- |
| `v != 0` | `(N/q) ell` | `ell/q` | `N^3 q` | `q` |
| `v = 0` | `ell` | `ell/N` | `N^4` | `N` |

分别代入已证明的字段，得到两个条件结论：

\[
\boxed{F_{N,g}(s)=(1-e^{-s\ell/q})^{-q}\quad(v\ne0),}
\]

\[
\boxed{F^0_{N,g}(s)=(1-e^{-s\ell/N})^{-N}\quad(v=0).}
\]

这是固定基轨道之上有限条提升轨道的局部乘积计算；没有把所有 owner 的无限乘积当作已定义，也没有作任何极限交换。

## 5. 按覆盖配方构造有限形式代表

使用 R6 的[正 content 有限域及映射][positive-domain]。若 `d>0`，由 `q|d`，`d/q` 是正整数；第 4 节的时间单位与整数重数允许直接构造

\[
f_{N,g}=(1-u_g^{d/q})^{-q},\qquad
b_g=(1-u_g^d)^{-1},\qquad f_{N,g},b_g\in A_{\{g\}}.
\]

两个分母都属于可倒置的 `1-u_g^r`（正整数 `r`）。原始时间缩放后乘积的形式代表为 `(1-u_g^(d/q))^(-c)`；归一化后的重数已经证明是整数 `q`，所以此处无需给形式环另加任意 `1/N^3` 次方运算。

保持既有映射 `sigma_(s,{g})(u_g)=exp(-s ell/d)`，直接计算

\[
\sigma_{s,\{g\}}(f_{N,g})=F_{N,g}(s),\qquad
\sigma_{s,\{g\}}(b_g)=(1-e^{-s\ell})^{-1}=:B_g(s).
\]

其中变量映射仍是 `ell/d`，不能改成 `ell/q`。

零 content 则使用[固定 `g,N` 的同标签有限子代数][zero-domain]，单独构造

\[
f^0_{N,g}=(1-z_g^{1/N})^{-N},\qquad
b^0_g=(1-z_g)^{-1},\qquad f^0_{N,g},b^0_g\in A^0_{g,N}.
\]

对既有 `tau_(s,g,N)(z_g^a)=exp(-s ell a)`（这里 `a` 是相应有理指数），有

\[
\tau_{s,g,N}(f^0_{N,g})=F^0_{N,g}(s),\qquad
\tau_{s,g,N}(b^0_g)=B_g(s).
\]

此处也只有证明所得的整数重数 `N`，没有跨 owner 的零 content 乘积或向 `R_+` 的类型转换。

这两项是“从配方构造形式代表，再核对标量像”，不是“由固定 `s` 的标量值反推出唯一形式因子”。固定 `s` 的求值一般不单射：例如正分支取 `s=d log(2)/ell`，非零形式元素 `2u_g-1` 的像为零；零分支取 `s=N log(2)/ell`，非零元素 `2z_g^(1/N)-1` 的像为零。形式嵌入 `j_F` 的单射性是另一件事。

## 6. 有限条件比较及边界情形

结合[既有标量引理][scalar]，在 H0–H3 与上面的有限域绑定条件下可进一步得到：

- 正分支 `q>=2` 时 `F_(N,g)(s)>B_g(s)`，因此上述两个已构造的形式元素不同；这只用“不同标量像蕴含原元素不同”，无需假设求值单射。`q=1` 时则直接有 `f_(N,g)=b_g`，不能套用严格不等式。
- 零分支 `N>=2` 时同样有 `F^0_(N,g)(s)>B_g(s)`，且两个同标签形式元素不同；`N=1` 时二者相等。
- 沿固定的 `N_k=k!`，对固定 `d>=2`，只在 `d|N_k` 后取 `q=d` 并调用上述条件比较。这没有更换控制序列，也没有建立全局或一致极限结论。

作为通用边界检查，`N=1` 时两个分支都给出 `h=c=1`、最小周期 `ell` 和基底因子 `B_g`。若 `v!=0` 但 `N|d`，模 `N` 的返回仍可为恒等映射；此时正分支 `q=N` 与 `c=N^4` 一致，但其 owner 类型并不变成零 content。

以上比较是针对满足假设的局部数据所作的演绎结论；本笔记未提交任何具体 owner 的表示、证书或观测，不能将其记成已执行的项目 mismatch、全 owner 障碍、恢复成功或 Route 结论。这里只比较实数 `s>0`，不把大小关系推广到复数。

## 7. 相对上一份笔记的进展与剩余义务

逻辑链为：H0–H2 → 商群与纤维返回 → 最小阶及循环／轨道对应 → H3 的原始有限乘积 → 两项归一化 → 有限形式代表与条件比较。它不是从目标公式出发反推前提。

| 上一份笔记的衔接项 | 本次新增的精确范围 |
| --- | --- |
| L1：实际 owner 绑定 | 未完成；H2 明列其所需条件，没有新增具体群字、本原证书、向量或长度认证 |
| L2：覆盖作用与阶 | 在 H0–H2 下由商群覆盖的纤维返回及 Bézout 论证导出 |
| L3：分量及本原性 | 在 H2 最小流周期假设下证明循环／轨道对应与最小提升周期；未新增群非真幂证书 |
| L4：物理时间 | 条件推得未缩放 `h ell`，再按固定规则乘 `1/N` |
| L5：原始乘积及对数归一化 | 按 H3 的因子计数约定先写 `U`、再 `V`、最后 `F`，分别导出正／零分支 |
| L6：有限定义域连接 | 按证明得到的时间单位与整数重数构造代表，并直接核对有限标量像 |
| L7：比较与结果命名 | 得到有限条件比较；没有实际 owner 运行或项目结论认证 |

最直接的下一项实质工作是给出一个与固定标记一致的精确 owner，并分别落实非真幂、本原流轨道、同调向量和物理长度的绑定；不能用任意正参数 `ell` 替代这项工作。覆盖模型的具体输入实现、证书载荷和验证也未产生。

整个 `R_+` 或 `H_g` 上的标量求值、零 content 跨 owner 乘积、全局产品、尾界及 [AN-1–AN-5][analytic] 均不在本证明范围内。旧稿与旧笔记中的未完成状态按其当时范围原样保留；本次新增条件证明不自动改变正式流程状态。

本次核对方式：主线程整合了整数计数、覆盖返回／最小周期、有限域映射三项只读推敲，并直接写出论证；同系助手的核对不算独立科学证据。文件检查只验证引用定位、固定公式／条件是否写明及追加前的文本是否保留，不认证数学正确性。没有运行科学实验、枚举、旧审查脚本、论文构建或外部来源查询。

[chain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_factor_derivation_chain_20260907.md
[frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:90
[targets]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:493
[domains]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:720
[positive-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:764
[zero-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778
[scalar]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:531
[analytic]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:904

## 追加进展：精确代表族与符号周期（2026-09-08）

后续[显式非真幂代表族笔记](internal_explicit_nonpower_owner_family_20260908.md)给出 `g_d=a_1^d[a_1,b_1]`（整数 `d>=0`），证明其非平凡、非真幂且同调为 `(d,0,0,0)`，并连接到固定双曲度量下的本原流轨道与符号最小周期。在本笔记 H1、H3 条件下，后续笔记进一步给出 `g_2`、`g_0` 的局部因子及形式系数比较。它未完成规范 owner 枚举、数值长度、覆盖实现或全局比较对象；此前状态快照及正式稿件保持原样。
