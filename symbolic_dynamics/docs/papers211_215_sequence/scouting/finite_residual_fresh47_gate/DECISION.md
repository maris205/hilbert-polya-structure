# Fresh47 独立候选准入裁决

2026-09-11 UTC。裁决人：`/root/p213_manuscript_review_b`。
这是一个有界 source/proof/evidence 候选 gate，不是稿审、全局查新或新定理研发。
本人不是 fresh47 / PRE / PFR 作者；根提出共轭疑问，由本人阅读原件和独审
论证后独立判断。`current_round_independent_scout` 已明确其 REVIEW.md 稳定。
本裁决不把根的疑问本身当作证据，也不构成外部或跨模型审查。

本 gate 的现稿 pin 是 `95db41c45ba16382b4bb843aea9c351ddeafd05a628124ff881559aa3c9023cd`。
独审保存的是更早所读现稿 pin `5871bf36...`；不声称二者全 raw 相等。
本人的演绎判断建立在此次完整读取的当前稿及完整 withdrawn diff 上。

## 裁决：NO_GO_CURRENT_BATCH_OCCUPIED_SCHEDULE

fresh47 **不能作为当前五篇批次的一张新系统席位准入**。阻断项是具体的
PFR 逐轮共轭，以及当前合同要求在已占用、已拒绝系统之外选取新系统；
不是时钟证明错误，不是“标准方法必然无价值”，也不是“两机制都必须新”。

同时保留一个明确正面数学结论：现稿点态时钟

\[
h(w)=\left\lceil\frac{\max_{0\le i\le j\le n}
 (|\operatorname{red}(w_{1:i})|+|\operatorname{red}(w_{j+1:n})|)
 -|\operatorname{red}(w)|}{2}\right\rceil
\]

及其 exposed-peak 精确递减论证，在本次演绎复核中无未决缺口。
相对于所读旧 PFR 原件，它是实质更强的点态结论；旧原件只给终态和长度预算。
“所读旧证据没有这条定理”不等于“全球首次”。候选系统不准入和定理有价值
可以同时成立，不应将本裁决改写成新时钟已被旧文献完全包含。

## 1. 当前合同怎样约束这个结论

当前 `docs/papers211_215_sequence/PROBLEM_ANCHOR.md` 的 anchored question
明确从 through P210 的 known/rejected/reserved 内部表面之外选择五个系统，
并明确继承 `docs/papers197_201_sequence/PROBLEM_ANCHOR.md`。当前条款还要求
扣除 known maps、conjugacies、factors、parameter restrictions 和 proof mechanisms，
以及 replace weak or duplicate systems。

继承 anchor 的 anchored question 要求 genuinely different finite autonomous
deterministic maps，覆盖 occupied/killed/reserved 全部内部表面；其 selection/
promotion 条款明确把 parameter variants、conjugates 排除在价值阈值外。
工作区 AGENTS 的 replace weak or duplicate systems 与此一致。

合同也确实只要求一条刚性时态结论和一条不同机制的 inverse/enumeration
结论，并未要求两个机制分别具有全球新颖性。因此，本 gate 的分项判断是：

| 检查项 | 判断 | 精确理由 |
| --- | --- | --- |
| 自然、确定、有限的 literal map | 满足 | 固定 q、N，旧最大常值 run 的奇偶压缩 |
| 刚性 all-parameter temporal theorem | 满足演绎审查 | 有序两端距离最大值和两条逐轮不等式 |
| 数学上分离的完整 inverse baseline | 满足修正后的演绎审查 | 唯一 run/gap 分解、完全图颜色矩阵、显式系数 |
| 两条机制都具有新颖性 | 不是合同要求 | 不以该虚构要求拒绝 |
| 超出内部已占/已kill map 的系统资格 | **不满足** | q=4 与 archived PFR 保长逐轮共轭 |

“每篇有清楚 theorem-level progress”不能独自撤销同一有效合同中的系统去重
条件。当前没有“可重开旧系统并作为新席位计数”的明确例外授权。

## 2. 核验具体碰撞，而非仅援引 free reduction 名字

旧 `algebra_lane/replacement/pilot.py:445–481` 给出的 PFR 是左至右扫描，
若相邻字母满足 INVERSE={0:1,1:0,2:3,3:2} 就删除这对并越过两字母，
否则保留当前字母。其旧 carrier 实例是四字母、长度至多六；literal 函数
本身不依赖 cutoff。旧 CANDIDATES 和 KILL_LEDGER 已将 R08/PFR 纳入已kill
内部表面，不是新发现未占用对象。

独审 §4 的共轭论证正确，现稿的 `aaa` 比较不足以反驳它：

1. q=4 自逆字母的 reduced-word 根树和两生成元自由群的 Cayley 根树都为
   4-正则树。固定一个保根的无标号树同构。
2. 每个词唯一编码从根开始的逐边 walk。经同构传输整条 walk，再读目标树
   的边标签，得到所有词的保长双射；它不是固定的逐字母替换。
3. 在无标号 walk 中分解最大连续单无向边往返段。自逆标签下它就是常值
   run；自由群标签下它是互逆字母交替段。旧 PFR 左扫描不能跨越不同边的
   段界配对，在每段中恰删除左起相邻对，保留该段的奇偶长度。
4. 因而同一个传输双射与一次更新交换，进而与全部迭代交换，也保持 cutoff。
   特别是 q=4、N=6 已与确切历史 carrier 共轭；改变 N 只是 cutoff 扩展。

这核验的是输入独审已经给出的碰撞论证，不是为 fresh47 新增 theorem axis。
同构也保留两端距离和顶点次序，因此新时钟直接成为同一旧 schedule 上的
新点态时钟，而不能证明 schedule 是新系统。旧 ledger 中“clock cannot
support a paper”的宽泛价值句不应被当作反驳新时钟的数学定理；本 gate
不依赖该句，只依赖确切旧 map 和仍有效的系统资格合同。

## 3. 为什么不能从 q 改名获得 GO_NARROW

偶数 q=2r 对应相同的 q-正则树传输与 rank-r 自由群 schedule；只有 rank-2
是本次实际读取的历史实例，不冒称所有 rank 都曾执行。也不声称奇数 q
的整棵正则树与偶度自由群树同构。

但只去掉 q=4、只取奇数 q、或增加 N，均不改变现稿使用的单边段 parity
更新，也不产生新的 q 特有时态机制：时钟证明仍仅用树的唯一 parent 和
有序 peak，逆像仍仅对同一颜色矩阵替换 q。现稿没有另一个已提出、已证明、
通过去重的受限系统合同。依现有 parameter-variant 排除条款，不能用这个
参数裁剪把已占 schedule 重新包装为新系统席位。

这不是普遍禁止在已知算法上证明新结论；只是本批明确要求系统广度和去重。
因此不存在可从现稿直接裁出的合规 GO_NARROW 新席位合同。

## 4. 数学复核及错误保存

时钟第一不等式的分段顶点映射在共享边界一致、保序且位移至多一。
第二不等式中 p<r 时两个最大值索引均为相应端点距离的内部严格 peak，
被擦除偶 run 的外伸 witness 有序；p=r 时离开端点 geodesic，两个 parent
方向相同，一个 witness 同时增加两距离。最后一步 excess 为一或二，
ceiling 正确降至零；空词、固定词、q=1 均无隐藏例外。

修正逆像的 off-diagonal gap 是
`1/((1-(q-1)e)(1+e))`。旧 PRE 全文中的 run/gap 矩阵计算经 retained
weight `z -> z/(1-z^2)`、erased weight `L -> z^2/(1-z^2)` 直接给出现稿
公式。因此 inverse 是完整独立基线，但该机制全部扣除新意。

withdrawn V1 错写 numerator `1-(q-2)e`，对应 q=3、target ab、length 4
给六而实际为七。该 Major 已被作者纠正并经独审演绎接受；本次检查确认。
`DRAFT_V1_WITHDRAWN_RECONSTRUCTED.md` 明示它是重建历史文本而非首版原始字节。
本 gate 读取其 preservation notice 及与完整现稿的全 diff，保留错误性质；
不冒称失败科学执行，也不将已修正错误继续当作否决原因。

独审报告真实 bounded temporal pressure 为 3800 词、32525 counted checks、
832 非空第二不等式检查且零反例，并明确未测试 inverse。本人读取其 review、
source-review 和完整短 stdout；没有重新运行或独立接收该运行的全 native
过程，不把这组有限结果当作 all-parameter 证明。准入裁决依上述演绎和合同。

## 5. 处理边界

保留 fresh47 证明和独审作为**旧 schedule 上有价值的未准入定理进展**；
保留 V1 错误及修正史，不重写旧 PFR/PRE disposition。若将来明确授权研究
“旧系统上的新定理”，它可在那个不同 scope 中重新评价，但不是本次自动
打开的工作，也不能作为当前 P214 席位计数。现行 scope 下应替换候选系统。

本 gate 不新增定理、不做科学执行或 build、不改编号/中央计数、不建 manuscript、
不做 Git/外部上传。只写本新 gate 目录。没有新增全局 owner 搜索；独审所读
外部文献的排除边界按其有限范围保留，不作全球 novelty 结论。
初次组合显示截断，随后完整读取现稿、独审、两 anchor、PRE 原证明和所需
PFR 原始函数/处置，并读取完整 withdrawn diff；截断显示不代替这些证据。
最终状态：**NO_GO_CURRENT_BATCH_OCCUPIED_SCHEDULE / HOLD_EXTERNAL**。
