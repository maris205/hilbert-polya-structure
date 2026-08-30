# S01 oriented adjacent-fold：proof/value/owner spike

日期：2026-08-30 UTC。状态：proof spike only；未分配论文编号，不是论文，
未做 Git 操作。

## Verdict

最终处置：**KILL_AS_STANDALONE / DIRECT_COUNT_OWNER**。

过程本身与下面的逐终态公式都正确；kill 的原因不是反例，而是 headline
结果发生了精确 owner collision：若 $X_n$ 是最终存活点数，则

$$
X_n-1=\operatorname{MNA}(\pi) \qquad\text{pointwise}, \tag{1}
$$

其中 $\pi$ 是 $S_{n-1}$ 上的均匀随机置换，$\operatorname{MNA}$ 是相邻模式
$12$ 的最大互不重叠出现数。Kitaev (2005) 已给出任意连续模式最大互不
重叠出现数的全分布生成函数；Kitaev--Zhang (2024) 又明确写出普通置换上
MND（因补映射也即 MNA）的 EGF

$$
\sum_{m,k\geq0}D_{m,k}u^k\frac{z^m}{m!}
=\frac{e^z}{1-u\{1+(z-1)e^z\}}. \tag{2}
$$

因此 scout 得到的 survivor-count PGF、全部有限尺寸计数、矩、主奇点和
CLT 都是 (2) 经 (1) 换名后的直接推论，不能作为 S01 的新贡献。

本轮仍得到一个尚未在检索到的直接 owner 中出现的残差：每个终态独立集
$A$ 的优先级置换 fibre 是一个明确的 descent-set interval，见 Theorem 3。
但该公式只把动力学约束翻译成经典 exact-descent-set 计数；在总计数定理
已经被 owner 完整覆盖的情况下，不足以支撑一篇独立短论文。它可保留为
以后“有向森林/一般有向图折叠”的局部引理，不能为当前 path 系统立项。

## Literal process and conventions

固定 $n\geq1$，初态为 $[n]$。若 $i,i+1$ 都存活，则边
$e_i=(i,i+1)$ 合法；每一步从所有当前合法边中均匀选一条并删去右端
$i+1$。无合法边时停止。

- $A_n$ 表示随机终态；
- $X_n=|A_n|$；
- $P_n(u)=\mathbb E[u^{X_n}]$；
- 为生成函数方便，置 $P_0(u)=1$；实际过程从 $n\geq1$ 开始；
- fibre 一律指原始 $n-1$ 条边的均匀优先级置换 fibre，不把不同长度且
  非等概率的“合法事件词”混为均匀对象。

## Proof map

1. 用每条边的 iid 连续时钟将逐步均匀选择耦合为均匀优先级置换。
2. 由第一次响铃分裂路径，证明 root 给出的 PGF recurrence 和 OGF。
3. 写出逐点二状态 automaton，识别为最大互不重叠 ascent 数。
4. 由 automaton 证明终态支撑以及每个终态的 exact descent-set fibre。
5. 对 forgetting process 做最小有限反例，排除逐分布同一性。
6. 将新残差与 Kitaev 的总分布 owner、Alon--Elboim--Sly 的 forgetting
   渐近 owner、标准 path RSA 三者分别相减。

## Theorem 1: static priorities and first-event splitting

给每条原始边 $e_i$ 一个独立 $\operatorname{Exp}(1)$ 时钟 $T_i$。按时钟
从小到大扫描；若响铃时两个端点仍存活，就删去右端，否则忽略该边。
所得终态与字面 Markov chain 同分布。

### Proof

在任意当前状态，当前合法的边从未响铃：一条边一旦不合法，由于系统只
删除点，它永远不会重新合法。指数分布的无记忆性说明所有当前合法边的
剩余时钟仍 iid，因此下一条响铃的合法边在它们之中均匀。逐步归纳即得
字面过程。连续时钟的秩是 $S_{n-1}$ 上的均匀置换，故也可只保留优先级。
$\square$

若第一条边是 $e_i$，点 $i+1$ 被删，余下过程分裂成点数为 $i$ 和
$n-i-1$ 的两条独立子路径。因此

$$
P_0=1,\qquad P_1=u,\qquad
(n-1)P_n=\sum_{i=1}^{n-1}P_iP_{n-i-1}\quad(n\geq2). \tag{3}
$$

令 $F(z,u)=\sum_{n\geq0}P_n(u)z^n$。对 (3) 求和得

$$
zF_z-F+1=zF(F-1),\qquad F(0,u)=1,\quad [z]F=u. \tag{4}
$$

解 (4) 为

$$
F(z,u)=1+\frac{uz}{u(1-z)+(1-u)e^{-z}}. \tag{5}
$$

这是一个正确的动力学推导，但 Section “Direct owner collision” 说明
(5) 已由旧的置换模式公式拥有。

## Theorem 2: pointwise permutation automaton and MNA identity

令 $r_i$ 是边 $e_i$ 的响铃秩，所以
$\pi=r_1r_2\cdots r_{n-1}$ 是均匀置换。写 $s_j=1$ 当且仅当点 $j$ 最终
存活。则

$$
s_1=1,\qquad s_2=0,\qquad
s_j=(1-s_{j-1})\mathbf1\{r_{j-2}<r_{j-1}\}quad(3\leq j\leq n). \tag{6}
$$

特别地，若 $\pi$ 的某个 maximal ascent run 含 $L$ 个相邻上升，则该 run
贡献 $\lceil L/2\rceil$ 个除点 1 外的存活点，因而逐置换成立 (1)。

### Proof

点 1 没有可删除它的边，点 2 必被 $e_1$ 删除。对 $j\geq3$，点 $j$ 只
可能被 $e_{j-1}$ 删除。它存活恰当且仅当 $e_{j-1}$ 响铃前，点 $j-1$
已经被 $e_{j-2}$ 删除；这又等价于 $s_{j-1}=0$ 且
$r_{j-2}<r_{j-1}$，得到 (6)。

在一个连续 ascent run 上，(6) 从左到右选择第一、第三、第五、……个
上升位置，数目为 $\lceil L/2\rceil$。这也是路径上该组相邻 ascent
occurrences 的最大不相交选择数。对所有 run 求和即得 (1)。$\square$

### Immediate support corollary

终态支撑恰为

$$
\mathcal I_n^{(1)}=
\{A\subseteq[n]:1\in A,\ A\text{ is independent in the path}\}. \tag{7}
$$

必要性来自停止条件和点 1 永不删除。充分性也可由下一定理看出：任意
$A\in\mathcal I_n^{(1)}$ 给出的 required ascent/descent 集互不冲突，而
任意指定 descent set 都由至少一个置换实现。因此
$|\operatorname{supp}(A_n)|=F_n$（$F_1=F_2=1$）。注意终态不必是极大
独立集；例如 $n=3$ 可终止于 $\{1\}$。

## Theorem 3: exact pointwise terminal-set fibres

这是本轮唯一可能的真正 residual。令 $m=n-1$，对
$A\in\mathcal I_n^{(1)}$ 定义比较位置集合

$$
U_A=\{j-2:3\leq j\leq n,\ j\in A\}, \tag{8}
$$

$$
D_A=\{j-2:3\leq j\leq n,\ j\notin A,\ j-1\notin A\}. \tag{9}
$$

这里 $U_A$ 是 required ascents，$D_A$ 是 required descents。若
$B\subseteq[m-1]$，令

$$
\beta_m(B)=|\{\pi\in S_m:\operatorname{Des}(\pi)=B\}|. \tag{10}
$$

则优先级 fibre 与终态概率为

$$
f_n(A)=
\sum_{D_A\subseteq B\subseteq[m-1]\setminus U_A}\beta_m(B),
\qquad
\Pr(A_n=A)=\frac{f_n(A)}{(n-1)!}. \tag{11}
$$

此外 (11) 完全显式。对 $C=\{c_1<\cdots<c_t\}\subseteq[m-1]$，令
$\lambda(C)=(c_1,c_2-c_1,\ldots,m-c_t)$，空集时
$\lambda(\varnothing)=(m)$。经典 Möbius inversion 给出

$$
\beta_m(B)=
\sum_{C\subseteq B}(-1)^{|B|-|C|}
\frac{m!}{\prod_{a\in\lambda(C)}a!}. \tag{12}
$$

### Proof

由 (6)，若 $j\in A$，比较位置 $j-2$ 必须上升；若 $j\notin A$ 且
$j-1\notin A$，它必须下降；若 $j-1\in A$，则 $j$ 自动被排除而该比较
自由。因此产生 $A$ 的置换恰是下降集满足

$$
D_A\subseteq\operatorname{Des}(\pi)
\subseteq[m-1]\setminus U_A
$$

的置换，分拆 exact descent sets 即得 (11)。

最后，下降集包含于 $C$ 的置换必须在由 $C$ 切出的每个 block 内递增，
其数目为 $m!/\prod_{a\in\lambda(C)}a!$。在 Boolean lattice 上反演即得
(12)。$\square$

### Residual value ceiling

(11) 的优点是逐终态、任意 $n$、非递归且给出严格正概率判据；它比只给
$X_n$ 的边际分布更细。其不足同样明确：

- 动力学部分只是二状态局部 automaton；
- (12) 是经典 descent-set enumeration，不可计为新技术；
- 对所有 $A$ 求和后立即退化为 owner 已有的 MNA 分布；
- 当前没有额外的闭式相关函数、非平凡极值 fibre 或一般图推广。

所以允许的 claim ceiling 只能是“path dynamics 的 pointwise descent-set
encoding”，不能声称新 survivor-count law、moment theorem 或 CLT。

## Moments and asymptotics (correct, but not novelty)

由 (5) 对 $u$ 求导：

$$
\sum_{n\geq0}\mathbb E X_n z^n
=\frac{ze^{-z}}{(1-z)^2}, \tag{13}
$$

$$
\sum_{n\geq0}\mathbb E[X_n(X_n-1)]z^n
=\frac{2ze^{-z}\{e^{-z}-(1-z)\}}{(1-z)^3}. \tag{14}
$$

因此

$$
\mathbb E X_n=\frac{n+1}{e}+O((n-1)!^{-1}), \tag{15}
$$

$$
\operatorname{Var}(X_n)=
\left(\frac3{e^2}-\frac1e\right)n+O(1). \tag{16}
$$

在 $u=1$ 邻域，(5) 的主奇点是分母的唯一邻近简单零点 $\rho(u)$；标准
simple-pole quasi-powers 给出中心极限定理。这里不把该 CLT 列作 residual：
一方面它由 Kitaev 的已知 MNA EGF 直接推出；另一方面 forgetting paper
在另一个过程上已经明确拥有相同的中心、方差常数和更强的 functional
CLT。新稿若引用这些量，只能写成一致性校验。

## Hostile check: the forgetting process is not the same distribution

Alon--Elboim--Sly 的过程从 memory $\{0\}$ 开始，连续 iid 输入逐个进入；
若新值大于进入前的当前最小值，就删除该最小值。只有输入的相对秩重要。
令 $M_m$ 为 $m$ 个输入后的 memory size。

最小反例在 $m=3$：六个相对次序给出

$$
\#\{M_3=1,2,3\}=(1,4,1), \tag{17}
$$

而 S01 在 $n=4$ 的六个边优先级给出

$$
\#\{X_4=1,2,3\}=(1,5,0). \tag{18}
$$

特别地，严格递减的三个输入使 memory size 为 3，概率 $1/6$；路径 4 的
独立终态最多只有两个点。因此

$$
X_{m+1}\not\stackrel d=M_m\qquad(m=3), \tag{19}
$$

verifier 还穷举确认 $m=3,4,\ldots,8$ 全部不同。两者在 $m=1,2$ 的巧合和
相同的线性均值/方差常数不能升级为逐分布或逐对象同一性。

## Direct owner collision

### 1. Count distribution: fatal direct owner

Sergey Kitaev, “Partially ordered generalized patterns,” *Discrete
Mathematics* 298 (2005), 212--229,
[DOI](https://doi.org/10.1016/j.disc.2004.03.017), gives the generating
function for the entire distribution of the maximum number of non-overlapping
occurrences of an arbitrary dashless/consecutive pattern from its avoidance
EGF. The official [University of Strathclyde record](https://pureportal.strath.ac.uk/en/publications/partially-ordered-generalized-patterns/)
states this scope explicitly.

Sergey Kitaev and Philip B. Zhang, “Non-overlapping descents and ascents in
stack-sortable permutations,” *Discrete Applied Mathematics* 344 (2024),
112--119, [arXiv:2310.17236](https://arxiv.org/abs/2310.17236),
[DOI](https://doi.org/10.1016/j.dam.2023.11.020), explicitly record (2) for
ordinary permutations and attribute it to the 2005 general result.

Taking $m=n-1$ and using complement to exchange ascent and descent, (1)--(2)
give

$$
F(z,u)=1+uz
\frac{e^z}{1-u\{1+(z-1)e^z\}}, \tag{20}
$$

which is algebraically identical to (5). This is exact finite-distribution
ownership, not merely a nearby mechanism or matching asymptotic.

### 2. Forgetting: constants and FCLT owner, but no finite-law collision

Noga Alon, Dor Elboim, and Allan Sly, “On a random model of forgetting,”
*Annals of Applied Probability* 34 (2024), 2190--2207,
[arXiv:2203.02614](https://arxiv.org/abs/2203.02614),
[DOI](https://doi.org/10.1214/23-AAP2018), prove memory size $n/e+o(n)$ and a
functional CLT with variance coefficient $3e^{-2}-e^{-1}$, together with much
finer memory-set results. Equations (17)--(19) prove that this is not the same
finite distribution. It owns the surprising constants in its own process, but
Kitaev is the actual exact-law owner for S01 after (1).

### 3. Standard greedy MIS/RSA on a path: adjacent, not literal

Standard random greedy MIS orders vertices and accepts a vertex if no accepted
neighbor precedes it. Its path density is $(1-e^{-2})/2$, not $1/e$, and its
terminal set is maximal. For a modern primary account and historical routing,
see Krivelevich--Mészáros--Michaeli--Shikhelman,
“Greedy maximal independent sets via local limits,”
[arXiv:1907.07216](https://arxiv.org/abs/1907.07216). S01 can terminate at a
nonmaximal independent set, so this is not a direct owner. It does, however,
make a paper framed only as “random independent-set dynamics on a path” look
even less distinctive.

### Search log and limitations

Current-network searches on 2026-08-30 included exact formula searches for
`u(1-z)+(1-u)e^{-z}` and `e^z/[1-u(1+(z-1)e^z)]`, and mechanism searches for
`delete right endpoint adjacent pair`, `random permutation of edges path`,
`oriented random sequential deletion`, `maximum disjoint ascents`, and
`maximum non-overlapping consecutive pattern 12`. They found no paper naming
the literal adjacent-fold Markov chain and no direct pointwise terminal-set
fibre theorem. Absence from these searches is not a priority claim. More
importantly, the count-law collision is already exact enough to decide this
candidate without relying on an absence claim.

## Independent exact verification

Files:

- `verify_stoch_oriented_fold.py`
- `verify_stoch_oriented_fold.out`

Reproduction command:

```bash
python3 docs/papers122_126_sequence/proof_spikes/verify_stoch_oriented_fold.py
```

Canonical result:

```text
oriented adjacent-fold exact control: PASS
assertions=818566
exhaustive_edge_priority_permutations=409114; n=1..10
literal_Markov_vs_priority=n<=10; automaton_and_MNA=n<=10
pointwise_descent_interval_fibres=all_terminal_sets_n<=10
PGF_recurrence_and_closed_OGF=n<=40; factorial_moments=n<=40
support=all independent subsets containing vertex 1
fold_count_law_n4=Counter({2: 5, 1: 1})
forgetting_size_law_m3=Counter({2: 4, 1: 1, 3: 1})
forgetting_distribution_mismatch_m=[3, 4, 5, 6, 7, 8]
owner_collision=survivor_count_minus_one_is_MNA_on_S_(n-1)
```

The verifier SHA-256 at signoff is
`54775754f1988ade6e6e38bfbbe48611a449ba989ec9b6399e097a95d8e6ff78`.

The checks are independent of the symbolic derivation in the following sense:

- literal state-by-state rational Markov recursion is compared with all edge
  priority permutations for $n\leq10$;
- direct edge deletion is compared permutation-by-permutation with automaton
  (6) and with $1+\operatorname{MNA}$;
- every supported terminal set is compared with (11)--(12);
- recurrence (3), closed OGF (5), and factorial moment GFs (13)--(14) are
  checked coefficientwise through $n=40$;
- forgetting is enumerated from its own literal memory update, not inferred
  from asymptotics.

## Final recommendation

**KILL S01 as one of the five standalone papers.** Do not allocate a paper
number, and do not advertise (5), (13)--(16), or the CLT as new.

Keep only Theorem 3 as a reusable lemma. Re-entry would require a genuinely
larger theorem—e.g. an all-size classification on oriented forests or a graph
family where terminal-set fibres have a new structural factorization. Merely
adding correlations, numerical tables, or another derivation of the already
owned MNA EGF does not clear the owner/value gate.
