# Fresh52 非贡献者候选 gate

2026-09-11 UTC。裁决人 `/root/p213_manuscript_review_b`。
接案前没有 fresh52 proof/verifier contribution；不属于 DESK 列明的三位
贡献者。本次只核验已有候选合同、证明、来源和内部碰撞，没有增加候选
theorem axis、编写/运行 SCI 代码、分配论文号或修改作者/中央文件。
这是独立候选 gate，不是 manuscript review、外部或跨模型认证。

## 裁决

**NO_GO_CURRENT_BATCH_OCCUPIED_FACTOR / HOLD_EXTERNAL**。

所提窄合同的数学演绎部分通过本次检查：通用半尺寸上界、线性 cascade、
H(8)=4、与同 carrier EQC 非共轭、全目标系数/有限 subset DP，以及 pair-target
闭式和该 stratum 的最大值均未发现证明缺口。它们值得保留为数学进展。

但源扣除遗漏了比 EQC 更直接的已占系统 **C19_ISE interval-span echo**：
fresh52 的整个分区动力学正是该已kill word map 的自然等值类满射因子。
这违反当前和继承 anchor 的旧系统/factor 排除条款；不因数学进展较强而
自动获得新系统席位。以下给出具体原件、carrier、满射和交换等式。

| Finding | 级别/状态 | 精确内容 |
| --- | --- | --- |
| F1 | Major，confirmed admission blocker，未修复 | DESK §6 遗漏已kill C19_ISE；D 是其 equality-pattern factor |
| 数学证明 finding | 0 open | 不把源资格阻断伪装成定理错误 |

不附加“两条机制都新”“同时必须有 exact H、pointwise clock、sharp leading
constant”的条件。拒绝原因也不是系数公式没有多项式时间算法。若只看数学
双轴，窄合同已超出原始 generic convergence；决定性失败在系统资格。

## 1. F1：完整的同规则 quotient 碰撞

### 1.1 历史 literal 和旧处置

原件 `docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md`
的 C19_ISE（248–256行）规定，对每个 n>=1，

\[
W_n=\{0,\ldots,n-1\}^n,
\qquad F_n(w)_i=\ell_w(w_i)-f_w(w_i),
\]

其中 f 和 ell 是字母出现的第一和最后位置。原 `pilot.py` 的完整
`interval_span_echo` 函数逐字实现该式：记录 first/last，再逐位置返回
last[value]-first[value]。0-based 或 1-based 位置约定不影响差值。
所有输出均在 0..n-1，所以这是 W_n 上的闭合自主更新。

旧 `KILL_LEDGER.md` 第28行明确将 C19_ISE 标为 KILL，并记载其通过
equality-class intervals 因子化。旧 n<=6 数值盒只作历史叙述，不被当作
全参数证明；这里使用的是原件所定义的任意 n literal 函数。
本批 `sequence_combinatorics_lane/PROOF_PACKAGE.md` §1 还已经拒绝了
inclusive-span +1 重命名：它与旧 F_n 逐字母平移共轭。
两处历史均未在本 gate 被改写或重新执行。

### 1.2 满射及一次更新交换

定义 E_n: W_n -> Pi_n，把词映为其位置等值类分区：

\[
i\sim_{E_n(w)}j\quad\Longleftrightarrow\quad w_i=w_j.
\]

它满射。任意 Pi_n 分区最多有 n 个非空块，给各块赋不同的 0..n-1
字母即可得到一个原像词。既不要求区间块，也不丢失任何位置标签。

设 pi=E_n(w)。对 pi 的任意块 B，其全部位置在 F_n(w) 中获得共同字母
max B-min B=delta(B)。因此两个旧块 B,C 在新词中成为同一等值类，
当且仅当 delta(B)=delta(C)。这正是 DESK 的同步 equality-diameter
合并，且没有在同轮继续处理新直径相等。故对每个 w，

\[
\boxed{E_n\circ F_n=D_n\circ E_n.}
\]

满射和交换等式给出整个 full-Bell-carrier 的 dynamical factor，迭代后仍
有 E_n F_n^t = D_n^t E_n。不是只在一个小轨道或特殊 stratum 上相似。
这一核验是对历史 literal 的 collision audit，不是给作者增添可准入定理。

不把 E_n 称为双射，也不声称两个完整 functional graphs 共轭。商映射会
忘掉字母名称，字母稳定可能有额外 transient；本裁决不需要给两个 map
的逐点稳定时间建立等号。它只用当前合同明确排除的确切 factor 关系。
n=0 的单状态边界不会使正整数全族摆脱此碰撞。

### 1.3 合同后果，而非回溯性否定新数学

候选作者 `current_round_independent_scout` 收到定位后确认没有不同 carrier
约定或反证，接受该遗漏由 gate 记录，并保持 DESK 不改。此回应与上面的
独立原件核验一致，不代替满射/交换论证本身。

当前 `PROBLEM_ANCHOR.md` 要求在 through P210 的 known/rejected/reserved
表面之外选择系统，明确扣除 factors，并要求 replace duplicates。继承
`docs/papers197_201_sequence/PROBLEM_ANCHOR.md` 的 anchored question 也
明确把 factored earlier map 列为 kill 情形。已kill C19_ISE 在该范围内。

旧 C19 没有给出 fresh52 的线性 all-size 时态定理或本次完整分区 inverse。
不能把“旧 schedule 已占”夸大为“旧证据已经证明了这些新结论”。不过当前
合同不是一个重开旧 map/factor 的 theorem-improvement 项目，因此这些
新进展不能自动解除 F1。仅证明与 EQC 非共轭不足以排除另一个已占对象。

## 2. 数学合同逐项复核

### 2.1 Causal spine 和半尺寸上界

严格合并减少块数，故无非平凡周期，固定当且仅当所有块直径互异。
若 t>=2 的合并所有输入块在 t-1 前已存在且未变，它们当时已同直径，
理应更早合并，矛盾。因此末轮合并可逐轮选出新形成父块，得到无空轮
的 nested spine。首轮输出至少含两点，直径为正。之后每轮至少并入一个
同正直径、故至少两点、且与父块不交的块。最终含至少 2h 点，推出
H(n)<=floor(n/2)。首轮 singleton 合并和离 spine 的并行合并均已覆盖。
空分区/单点的 h=0 及 n>=2 非单射例子也成立。

### 2.2 完整线性构造，不是未覆盖标签的端点示意图

challenge 原件的 I_m 有 5m+5 个整数。P 左端为 2 mod 3，Q 左端为负
3 的倍数，A 左端为零；右端分别为 >=6 的偶数、>=3 的奇数和四，且
左右端范围不交，所以所有端点互异。未使用点按阈值 2m+1 分配给末个
Q/P，均落在对应 hull 内，不改变端点并确实覆盖整个 I_m。

U_k 的 hull 为 [-3k,4+2k]。先与唯一同直径 P_k 合并后右端增二，
再与唯一同直径 Q_k 合并后左端减三。未消费伙伴的直径分属 mod 5
的四、一两类且各自严格递增，保证每轮只有预定一组碰撞。m>=1 的
边界与最终一个块均正确，因此 h=2m，而不是只证明至少 2m。
n-N 属于 0..4，若非零只添加一个直径 0..3 的块，与全部 >=4 cascade
直径不相交；这建立全部 n>=10 的 lower bound 和 Theta(n)。没有
反向推出未经证明的最优首项系数。

### 2.3 八点 witness 和 EQC 边界

指定分区依次将 2/5 singleton 合并成直径三，再匹配 {3,6}、{4,8}、
{1,7}，得到直径四、六、七，共四轮；半尺寸上界给 H(8)=4。
EQC 的同 cardinality causal spine 每轮至少倍增，故同 Pi_8 上高度
至多三。高度由共轭保持，因此该**同 carrier EQC 非共轭**结论正确。
它不排除 1.2 已证明的 ISE 满射因子；二者不矛盾。

### 2.4 全目标 endpoint 系数与有限算术求值

每个正直径块有唯一端点 (a,b)，其余元素是 Y 内严格介于端点间的
任意子集。一个 endpoint factor 恰选零或一个这样的块。提取 x_Y 的
squarefree 系数恰强制所选块互不交且覆盖 Y；唯一端点也排除 factorial
过计数。d=0 时唯一局部分拆为全 singleton，所以 C(Y,0)=1。

任何 predecessor 必须 refine 目标；一个目标块内部正好是同一直径
的全部前驱块，不同目标块必须取不同直径。反方向也成立，给出全目标
distinct-diameter coefficient，不是仅正纤维的必要条件。n=k=0 的
空乘积为一、无可覆盖情形系数为零，边界正确。

局部 nilpotent-variable subset DP 必须逐 factor 使用旧系数；按照文中
乘法 prescription，S 与新增 T 不交恰删除所有重复变量项。枚举不交
(S,T) 受 3^|Y| 控制，2^|Y| coefficient storage（可用新旧双数组）正确。
第二层显式使用 old array，每个直径至多供给一个目标块，故 O(nk2^k)
算术操作有效。这里不承诺 polynomial bit complexity，也不把该算法
称为已实现/运行的 verifier。

### 2.5 Pair-target 闭式和 stratum 最大

每个二点目标块只有 unsplit pair 或两 singleton 两种局部分拆，分别
用其正直径与零。零直径至多供给一个目标块。所以全直径互異时有 k+1
原像；唯一一对重复直径时必须拆其中一个，恰为二；其余重复模式都要
拆至少两个，故为零。反向 nested pairs {i,2k+1-i} 给出互異奇数直径，
对每个 k>=1 达到 k+1；k=0 fibre=1。最大及等号条件仅限 pair stratum，
未混称全 Pi_n 的最大纤维。

## 3. 机制扣除、直接主源和范围

Generic coarsening/终止、按 distinct statistic 分配目标块、squarefree
cover counting 均不给新机制信用。与 EQC 的 factorial splitting 相比，
endpoint 局部 cover 是不同的具体实现；线性两侧 cascade 也不是旧
equal-mass 倍增时钟的换标签。因此数学双轴并不因使用标准工具自动失败。
F1 是额外且决定性的 exact-map-factor 问题。

按项目技能使用了 research-lit 的 primary/source 分离规则，只做本任务
的限定来源读取，未启动通用文献流水线或下载/执行论文代码。
实际打开并完整读了 Alpert–Kahng (1997) 的 IBM abstract：其任务是把给定
ordering 切成区间 clusters 来优化 diameter，不能仅凭此摘要认定它拥有
这里的自主 equal-diameter update；也不能据此替未读全文作排除保证。
[IBM primary publication record](https://research.ibm.com/publications/splitting-an-ordering-into-a-partition-to-minimize-diameter)

旧 EQC owner audit 原件完整读过，其结论是 unresolved direct owner 而非
source clearance。本次尝试打开 Eliahou–Erickson 的
[publisher DOI](https://doi.org/10.1016/j.disc.2012.11.014) 返回 Internal Error，
未收到主文或摘要；不复述为本次成功读取，也不把旧 owner risk 迁移为 D
的直接文献所有权。

另两个限定查询为 `"partition" "equal diameter" merging dynamics` 及
arxiv.org 内 `"interval span" "iteration" words partitions`。返回的大量
几何/物理邻居未作证明输入，未找到正文级直接 owner 不等于 novelty。
内部 rg 覆盖 docs/papers 中 equal-diameter/span/coarsening 同义表达，
从本批旧 sequence source memo 定位 ISE，再读取具体旧函数/定义/kill。
这不是全库无遗漏保证；一个正的确切碰撞已足以裁决，无需扩大搜索救席。

## 4. 交付与停止边界

保留当前两作者证明包，保留早期 quadratic-span heuristic 被线性构造
反驳的来源史。此次不新增实验、代码/运行、build、manuscript、paper ID、
reserve、计数或中央更新。当前 scope 下替换候选，不把旧 factor 改名准入。

INPUT_PINS.sha256 固定本次关键原件；整文件 pin 不冒称读了历史 pilot
中不相关函数。完整读 DESK、challenge、EQC root/owner 和 ISE kill，
ISE CANDIDATES 读取具体248–256行，pilot 读取含完整 interval_span_echo
的230–295行，sequence proof/source memo 全读。无历史 SCI 程序被导入。
实际 web 返回的类型检查曾误打印字符串索引并截断；不影响先前完整 IBM
摘要读取，不被当作额外主源或证据。非自身 manifest 仅封本 gate 新文件。
最终：**NO_GO_CURRENT_BATCH_OCCUPIED_FACTOR；数学0 open，准入1 blocker；
HOLD_EXTERNAL 不变。**
