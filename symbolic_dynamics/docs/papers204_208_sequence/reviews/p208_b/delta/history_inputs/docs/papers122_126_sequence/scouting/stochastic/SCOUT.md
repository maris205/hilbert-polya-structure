# 随机秩下降、局部重写与半群作用宽搜

日期：2026-08-30。状态：scouting only；未分配论文编号，未写论文。本文件中的 `A/W/G/M/P/S/D` 只是候选标签。

## 1. 边界与判定口径

本轮先按现有 collision map、firewall 与 kill ledger 做了字面碰撞筛查。主动避开了 P1--P121 已使用的 Yule、队列、随机等待包装、普通随机游走、`BA->AB, AA->A`、竞争 `CB/BA` 重写、区间随机像、Rees sandwich motif、0-Hecke 排序、Tamari/Ferrers matching、Karger cycle contraction、Rémy、Apollonian、递归树、urn、greedy dimer、已有算术 affine/Euclid/Stern--Brocot 等载体。尤其不把“给旧过程加独立等待时间”算作新动力学。

本轮优先级是：字面新载体 > 每步真实状态变化 > 有限时间全分布/吸收时钟/终态纤维或历史计数 > 可形成无限族定理。有限枚举只算 theorem discovery/control，不算证明；搜索无命中只记为 bounded non-hit，不作 novelty certificate。

## 2. 二十个字面候选

| 标签 | 过程的字面定义 | 观测量 | 当前处置 |
|---|---|---|---|
| A01 | **Proper-residue gcd descent**：状态 `n>1` 时，从 `1,...,n-1` 均匀取 `a`，令 `n<-gcd(n,a)`；`1` 吸收。 | 吸收时间全 PGF、历史纤维、素幂分解 | **PROCEED_TO_PROOF_OWNER_GATE** |
| A02 | **Factor-sum descent**：对合数 `n`，从无序非平凡因子对 `ab=n, 2<=a<=b` 中均匀选择，令 `n<-a+b-1`；无因子对时吸收。 | `(终点,时间)` 联合律 | **RESERVE / theorem spike needed** |
| A03 | **Factor-gap descent**：同一因子对采样，但令 `n<-b-a`。 | `(终点,时间)` 联合律 | **RESERVE_SAME_CARRIER**，排在 A02 后 |
| A04 | **Cyclic non-generator order descent**：状态为循环群阶 `n>1`；从所有非生成元均匀取 `x`，令 `n<-ord(x)`；`1` 吸收。即对真因子 `d|n` 的一步质量正比于 `phi(d)`。 | 吸收时钟、素幂/平方自由分解 | RESERVE；先查群生成随机过程 owner |
| W01 | **Oriented ternary fusion**：在线性词 `w in {0,1,2}*` 中，从当前所有 `01,12,20` 出现位置均匀选一个，并分别改写为 `2,0,1`；无红式时吸收。 | 完整终态律、可达终态数、带重数历史数 | **CONDITIONAL PROCEED** |
| W02 | **Sandwich-center collapse**：从三字母词当前所有 `aba`（允许 `a=b`）中均匀选一个，以中心字母 `b` 代替整个三元组。 | 终态集合/概率、历史 DAG | RESERVE_LOW |
| W03 | **Bicyclic cancellation**：词上从所有 `pq` 均匀选一处作 `pq->epsilon`。 | 正规形、规约历史数 | KILL_THEOREM_THIN；随机性只剩历史计数 |
| W04 | **Colored polycyclic cancellation**：字母 `p_i,q_i`；均匀选相邻 `p_iq_j`，若 `i=j` 则删去，若 `i!=j` 则整词送入 cemetery `dagger`。 | 命中 cemetery 的有限时间律、幸存纤维 | RESERVE_HIGH_OWNER_RISK |
| W05 | **Braid-shortlex descent**：Coxeter 生成词上，随机选择 `s_i s_i->epsilon`，或仅当 shortlex 严格下降时选择 `s_i s_{i+1}s_i -> s_{i+1}s_i s_{i+1}`。 | 吸收正规形与规约历史 | KILL_OWNER/COLLISION_RISK；Coxeter/Hecke 太拥挤 |
| G01 | **Uniform reverse-delete**：连通图上均匀删除一个删后仍连通的边，直到生成树。 | 树的精确质量、形状质量 | **KILL_DIRECT_OWNER**；保留作负对照 |
| G02 | **Chordal simplicial deletion**：弦图上均匀删除当前 simplicial vertex，直到空图。 | PEO 的概率与纤维数 | RESERVE；PEO owner 风险高，时钟本身平凡 |
| G03 | **Non-cut survivor deletion**：连通图上均匀删除一个删后仍连通的顶点，直到剩一个顶点。 | 最终幸存点律、删除历史数 | RESERVE；需找图族闭式 |
| M01 | **Redundant-column deletion**：有限域矩阵中均匀删除一个删除后不改变列空间的列，直到剩一组基。 | 输出基的精确质量 | KILL_NEAR_MATROID_REVERSE_DELETE |
| P01 | **Fence maximal deletion**：fence poset `1<2>3<4>...` 中均匀删除当前极大元，直到剩一元，记录最后元素。 | 最后元素律、线性扩张加权 | KILL_THEOREM_THIN |
| P02 | **Ferrers corner deletion**：Young/Ferrers 图中均匀删除当前 removable corner，直到空图。 | tableau/history 权重 | KILL_INTERNAL_COLLISION；虽非 matching，仍回到既有 Ferrers 邻域 |
| P03 | **Dyck peak deletion**：Dyck 词中均匀选相邻 `UD` 并删除，直到空词。 | 删除历史数与高度过程 | KILL_DIRECT_CLASSICAL_RISK；标准树/括号递归邻域太近 |
| S01 | **Oriented adjacent-fold action**：在 `I subseteq [m]` 上从所有满足 `i,i+1 in I` 的幂等映射 `e_i:i+1->i` 中均匀选择并作用，即删去 `i+1`；无相邻对时停。 | 终态独立集律、作用词纤维 | RESERVE；需先做闭式 pilot |
| S02 | **Bidirectional adjacent-fold action**：有相邻对时，从所有有向合法折叠中均匀选择，删除该对任一端点；无相邻对时停。 | 极大独立集律 | KILL_OWNER_RISK；本质邻接随机 greedy MIS/RSA |
| S03 | **Finite abelian p-group quotient descent**：非平凡有限 Abelian `p`-群 `G` 中均匀取 `g!=0`，令 `G<-G/<g>`，按同构型继续，平凡群吸收。 | 分拆型吸收时钟、商链历史数 | RESERVE_STRONG；Hall-polynomial owner gate 后再 pilot |
| D01 | **Dominated-vertex deletion**：图上均匀选择满足 `N[v] subseteq N[w]`（某 `w!=v`）的顶点 `v` 删除，直到无 dominated vertex。 | stiff core 与删除历史 | KILL_INTERNAL_FIREWALL；落回 strong-collapse/dismantling 旧通道 |

上述 20 个过程分别覆盖算术秩下降、长度下降重写、图/拟阵逆删、偏序删除、幂等半群作用、有限群商与拓扑式折叠；没有把同一过程的等待时间变体另计为候选。

## 3. Exact pilots 与规范输出

四个脚本都只用 Python 标准库和 `fractions.Fraction`；递归方向严格降秩，因此没有截断或 Monte Carlo。重新运行后，stdout 与同名 `.out` 逐字一致。

| 脚本 | 覆盖 | exact assertions | 关键结果 |
|---|---:|---:|---|
| `gcd_split_chain.py` | 所有 `1<=n<=240`；素数 `p<=19,k<=8` | 3,064 | 字面 residue 与 totient-divisor 递归一致；素幂 PGF 乘积分解 |
| `cyclic_fusion_rewrite.py` | 全部长度 `<=7` 的三元词；`(012)^k,k<=9` | 33,718 | 完整概率递归=前向质量；XOR 守恒；支持数递推继续过 `k=9` |
| `reverse_delete_mst.py` | `K3,K4,K5` 全律；`K4` 的 `6!` 边序；星到 `n=7` | 591 | 重现 MST 形状质量与固定星公式；随后被直接 owner kill |
| `secondary_pilots.py` | 两个因子链到 `n=400`；fence 到 12；三元 sandwich 全词到长度 10 | 185,439 | 联合吸收律、fence 对称控制、sandwich 多终态信号 |
| **总计** |  | **222,812** | 所有规范输出 PASS |

复现命令（在本目录）：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 gcd_split_chain.py
PYTHONDONTWRITEBYTECODE=1 python3 cyclic_fusion_rewrite.py
PYTHONDONTWRITEBYTECODE=1 python3 reverse_delete_mst.py
PYTHONDONTWRITEBYTECODE=1 python3 secondary_pilots.py
```

对应规范输出为 `gcd_split_chain.out`、`cyclic_fusion_rewrite.out`、`reverse_delete_mst.out`、`secondary_pilots.out`。

## 4. 最强正信号

### 4.1 A01 proper-residue gcd descent

一步纤维计数为

\[
 \Pr(n\to d)=\frac{\varphi(n/d)}{n-1},\qquad d\mid n,\ d<n.
\]

若 `T_n` 是到 `1` 的步数，`G_n(z)=E[z^{T_n}]`，则有限全分布满足

\[
G_1(z)=1,\qquad
G_n(z)=\frac{z}{n-1}\sum_{d\mid n,\ d<n}\varphi(n/d)G_d(z).
\]

pilot 发现并精确验证了可直接争取证明的素幂闭式：

\[
G_{p^k}(z)=z\prod_{j=1}^{k-1}
 \frac{z+c_{p,j}}{1+c_{p,j}},
\qquad
c_{p,j}=p\frac{p^j-1}{p-1}=p+\cdots+p^j.
\]

等价地，

\[
T_{p^k}\overset d=1+\sum_{j=1}^{k-1}B_j,
\quad B_j\ \text{independent},\quad
\Pr(B_j=1)=\frac1{1+c_{p,j}}.
\]

因而均值、方差立即是相应 Bernoulli 和；这不是等待时间包装，而是原链吸收时钟本身的有限精确分解。

两条实质证明路线：**有**。

1. 由 totient 纤维递归对 `k` 归纳，并将相邻 `G_{p^k}` 的差分因子化；同时给出均值/方差 corollary。
2. 对整条严格下降历史按 `p`-进赋值序列计数，把历史和识别为基本对称多项式，直接得到乘积 PGF；再尝试 CRT 推进到平方自由或一般 `n`。

Kill 条件：素幂乘积已被直接文献陈述；历史计数无法给出独立于递归的证明；或一般 `n` 没有任何超过机械 divisor-DP 的无限族结构。当前建议：先做 proof spike，再查平方自由族。

### 4.2 W01 oriented ternary fusion

把 `0,1,2` 分别映到 `F_2^2` 的三个非零向量，三条规则都把相邻两向量替换为其 XOR，所以全词 XOR 严格守恒。长度每步减一，故完整终态分布由有限 DAG 精确给出。对起点 `(012)^k`，可达不可约终态数为

```text
k:     1  2  3  4  5   6   7   8    9
a_k:   2  4  9 21 49 114 265 616 1432
```

这些精确值在所有已算项满足

\[
a_k=3a_{k-1}-2a_{k-2}+a_{k-3}.
\]

对应的无权红式选择历史数为

```text
2, 12, 144, 2640, 66240, 2172240, 88583040,
4387582080, 256987987200.
```

两条实质证明路线：**条件性有**。

1. rewrite DAG 上的 exact mass recursion，证明终态律/历史计数递推。
2. 不可约词的有限自动机 + `F_2^2` 守恒 + 从 `(012)^k` 的可达性 grammar；若 grammar 可闭合，则由 transfer matrix 证明支持数有理生成函数。

必须强调：三阶递推目前只是 `k<=9` 的 theorem-discovery conjecture，不是定理。Kill 条件：`k=10` 失败；无法证明“满足自动机条件”与“实际可达”等价；或检索到字面三规则及该支持递推的 owner。当前建议：做 grammar/proof spike，成功才进入任何论文流程。

### 4.3 A02 factor-sum descent

严格下降性来自 `a+b-1<ab`（`a,b>=2`，等号情形也严格一单位），因此任意 `n` 的 `(终点,时间)` 联合律是有限有理数。到 `n<=400`，终点支持最大者是 `n=324`，有 12 个终点；例如

```text
n=36: ((3,4),1/8), ((5,3),1/4), ((7,2),1/8),
      ((11,1),1/4), ((19,1),1/4)
```

这证明载体确有分支与非平凡吸收时钟，但目前只有 acyclic DP 一条证明引擎，没有无限族闭式。Kill 条件：在素幂、半素数或固定因子型上找不到显式联合 PGF；或无法建立第二条历史/Dirichlet-convolution 路线。处置：reserve，不应仅凭有限表写论文。

### 4.4 W02 sandwich-center collapse

全体三元词到长度 10 的精确搜索中，`010102020` 可达 10 个不同不可约终态，说明非合流纤维不是空信号。当前没有稳定递推或概率闭式，且一般概率重写框架 owner 很强。Kill 条件：找不到参数化起点族与可证明 grammar，或只剩机械 DAG。处置：reserve-low。

### 4.5 G01 reverse-delete：强数值信号但必须 kill

pilot 得到

\[
K_4:\ (P_{star},P_{path})=(4/15,11/15),
\]

\[
K_5:\ (P_{star},P_T,P_{path})=(1/21,127/252,113/252),
\]

并验证固定标号星的概率 `1/(2n-3)!!` 到 `n=7`。这些都不是 residual contribution：直接 owner 已给 reverse-delete induction、任意树的全局公式、星公式及星/路径极值。因此此候选 **KILL_DIRECT_OWNER**，只作为 owner gate 有效性的负对照。

## 5. Owner subtraction（仅原始论文/官方页面）

### A01

1. Boris Alexeev, Kevin Barreto, Yanyang Li, Jared Duker Lichtman, Liam Price, Jibran Iqbal Shah, Quanyu Tang, Terence Tao, *Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*, arXiv:2605.00301 (2026), [官方 arXiv](https://arxiv.org/abs/2605.00301)。其 Definition 2.1 已系统定义向下 divisibility Markov chain，Examples 2.2--2.4 给随机除素数、Mertens 与 von Mangoldt 链。**扣除**：divisibility-poset downward-chain 语言、一般链/流框架不是本轮贡献。**保留**：proper-residue gcd 的具体 kernel、其完整吸收 PGF、上述素幂 Bernoulli 乘积以及尚待证明的更一般族。
2. Norihiko Minami, *On the random variable ... gcd(n,k1...kr)*, Journal of Number Theory 133 (2013), 2635--2647, DOI [10.1016/j.jnt.2013.01.012](https://doi.org/10.1016/j.jnt.2013.01.012)（[出版社页面](https://www.sciencedirect.com/science/article/pii/S0022314X13000620)）。该文研究一次性均匀 `k_i in {1,...,n}` 下 `gcd(n,k_1...k_r)` 的矩/卷积。**扣除**：一次 gcd 随机变量、totient/divisor 计数及矩方法不算新。**保留**：排除零剩余类后的逐步迭代吸收过程和它的时间分布；两模型不能混称。

截至 2026-08-30，对 exact kernel 词组、`proper residue gcd Markov chain`、素幂乘积式做的定向搜索未发现字面 owner；这只是 bounded non-hit，proof 阶段仍须扩大 MathSciNet/zbMATH/Google Scholar/全文引文链。

### W01/W02

Claudia Faggian, *Probabilistic Rewriting and Asymptotic Behaviour: on Termination and Unique Normal Forms*, Logical Methods in Computer Science 18(2), 2022, DOI [10.46298/lmcs-18(2:5)2022](https://doi.org/10.46298/lmcs-18%282%3A5%292022)（[期刊官方页](https://lmcs.episciences.org/9386)）。**扣除**：概率重写、normalization/termination、unique limit distribution 与策略比较的一般框架。**保留候选**：W01 的字面三规则、完整有限终态律、`(012)^k` 可达支持 grammar/递推；W02 的特定 sandwich 终态纤维。XOR 守恒本身按 elementary/zero-credit 处理。

对 `"01 -> 2" "12 -> 0" "20 -> 1"`、Unicode 箭头版本、规则+rewriting/semigroup 的定向检索没有发现同一规则系统；搜索命中了别的 cyclic-qutrit 三字母关系，但规则不同，不能据此声称 novelty。2026 年 cycle-rewriting 论文也不是本候选，因为 W01 是**线性词上的字母循环定向融合**，不是 cyclic-word rewriting。

### G01

Eric Babson, Moon Duchin, Annina Iseli, Pietro Poggi-Corradini, Dylan Thurston, Jamie Tucker-Foltz, *Models of Random Spanning Trees*, Random Structures & Algorithms 68(3), 2026, e70063, DOI [10.1002/rsa.70063](https://doi.org/10.1002/rsa.70063)；[官方 arXiv 全文](https://arxiv.org/abs/2407.20226)。Theorem 3.2 是 reverse-delete induction，Theorems 3.4/3.5 是外部/内部全局公式，Corollary 3.7 是 `1/(2n-3)!!` 星概率，Theorem 3.13 给 complete graph 上星最大、路径最小。**扣除后 residual 为零**，故直接 kill。

## 6. 排名、风险与下一道门

| 排名 | 候选 | 可证明闭式/主命题 | 两条路线 | 最大风险 |
|---:|---|---|---|---|
| 1 | A01 proper-residue gcd | 素幂吸收 PGF 的 Bernoulli 乘积；再争取平方自由/一般历史式 | 是 | 2026 downward-chain 框架很新；one-step gcd 文献深，owner 检索必须继续 |
| 2 | W01 ternary fusion | `(012)^k` 可达终态数的三阶递推/有理 GF；完整终态律 | 条件性是 | 当前递推仍为有限证据；reachability grammar 可能不闭合 |
| 3 | A02 factor-sum | 参数化整数族的 `(终点,时间)` 联合 PGF | 否 | 可能永远只剩机械 divisor-DP |
| 4 | S03 Abelian p-group quotient | 按分拆型的转移/吸收时钟 | 潜在是 | Hall polynomial 与随机生成/商群 owner 极强；尚无 pilot |
| 5 | W02 sandwich collapse | 参数化起点的终态纤维 GF | 否 | 一般重写 owner 强、当前信号不够形成定理 |

G01 的原始数值信号本可排前列，但 owner subtraction 后是零，故不进入正候选排名。

下一步只建议两个短 proof spike，不建议立刻分配论文：

1. A01：写出素幂乘积的两种完整证明，并计算平方自由 `n` 的历史多项式，检查是否有第二个真正无限族。
2. W01：先证明不可约语言自动机，再证明/否证从 `(012)^k` 的可达性 grammar；将 `a_k` 推到 `k=10` 仅作 falsification，不拿更多拟合作证明。

若二者任一过不了各自 kill 条件，就切换到 S03/A02，而不是在单一系统上继续堆有限枚举。
