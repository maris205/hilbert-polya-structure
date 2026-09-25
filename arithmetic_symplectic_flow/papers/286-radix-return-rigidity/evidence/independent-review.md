# 286 独立内部复核：固定-owner 类定理与准入边界

**Screen ID:** ASFS-SCREEN-20260920-RRR01  
**Main candidate:** NONE — SEPARATE-OWNER FAMILY SCREEN  
**Status:** EXACT ENDPOINT PACKET REDUCTION — STOP BLIND ROUTING SEARCH / FORK  
**Verdict:** 三检查点审查完成，无待解决的数学阻断或修改项。正时间包分类成立，unit-index 例外保留；一处不改变数学的用词精度项已修正并定点回读，见 §5。

## 1. 输入与实际顺序

| 输入 | SHA-256 |
|---|---|
| 286 原始冻结卡 | e69f918ca2b2fe13759cd85ea20ebffe6945bcd089611aaeb8a6c3ee946fd345 |
| 首次完整比较的 286 主文 | 7be90daef64ecdaaa5d33b1b25e0c1012e780ebced438923cd7953eed0c10818 |
| 单句术语修正后最终主文 | 846a1b5ead2cf344238e357e73a1b3c138e3392826b476d9a251e45d54454bcf |
| 282 既有引理所在主文 | a640a3aee9a3fb9003b42f5b4aa3d5c6c53388692109521714fc902e54a3aa93 |

检查点 1 先完整读冻结卡及获准的 282 Lemma 5 依赖段，独立推导本类 full owner、mixed-radix、正返回包、basin 与预列控制；向主控发送 raw 结果后，才完整读取 286 主文。

282 的实际读取范围为 Lemma 5 及工具返回的邻接证明上下文，不是重新审计整个旧包；本报告不重新赋予其信用。基本端点论证已经存在，新增审查对象是统一的完整 packet/routing 结论与准入范围。

检查点 2 全文比较主文，检查点 3 再尝试 unit-only、同根不同端点、非端点前像与重复律反例。原卡如事后追加行政 outcome，仍以表中原始冻结字节为 raw 输入。

审查者仅写本文件。无科学计算、周期 census、参数搜索、外部文献扩展、旧包修改或新架构证明。

## 2. 检查点 1：每个固定对象的完整时钟

结论对每个分别固定的非空可数离散 \(R\)、\(n(r)\ge1\) 与 total \(f\) 成立。不同选择不组成一个合并的 groupoid；任意 \(f\) 也不会自动获得算术来源或自然性。

每个 residue 分支是从 clopen coset 到完整目标根 \(K\) 的同胚。\(n=1\) 时仍是合法的唯一分支，只保持 seed。T 为 local homeomorphism；onto 与否取决于是否每个根都在 \(f\) 的像中，不能默认 onto。

有限逆前缀满足

\[
\theta_\alpha(t)=b_\alpha+D_\alpha t,\quad
D_\alpha=\prod_i n_i,\quad
b_\alpha=\sum_i j_i\prod_{h<i}n_h,\quad
0\le b_\alpha\le D_\alpha-1.
\]

上界由 \(j_i\le n_i-1\) 后 telescoping 得出，包含 unit steps 与空前缀。整数倍的 Haar 缩放给出 \(\mu(\theta_\alpha B)=h(B)/D_\alpha\)，对全部 Borel terminal sets 成立。

完整 retained-lag branch-pair topology 有可数 compact-open 基。相同箭头的不同表示同步延长两前缀，追加同一个实际 tail；公共 index product 在比值中抵消。因此

\[
J(g)=D_\beta/D_\alpha,\qquad
c(g)=\log D_\alpha-\log D_\beta
\]

表示无关、可乘／可加且在每个 bisection 局部常值。全支撑使连续 IMAGE-density 版本在 null points 也唯一；没有额外 a.e. retiming 或新加仿射箭头。

端点与保留的离散 lag 分离不同箭头；由实际 bisections 得到 Hausdorff、局部紧、第二可数、étale owner。实扩张保留全部对象，平移是完整联合连续作用；不由此声称 coarse quotient Hausdorff 或已有嵌入圆。

## 3. 既有端点引理及 unit-only 例外

对完整周期，逆前缀给出 \(x=b+Dx\)。当 \(D>1\)，模 \(D-1\) 强迫普通整数 \(b\) 被 \(D-1\) 整除；结合范围仅有 \(b=0,D-1\)。非零整数乘法在 \(K\) 上单射，故 \(x=0,-1\)。

这里明确复用 282 Lemma 5 的基本论证，不把 \(K\) 当整环，不以多项式根数代替证明；\(D=2\) 时模 1 虽无额外限制，范围仍只有两个端点。

当 \(D=1\)，所有 index 都是 1、所有 digit 都是 0，方程为 \(x=x\)。同一个 unit-only root cycle 上每个 \(x\in K\) 都周期，包括非端点和非整数种子。这是完整类别的必要例外，不得删去。

两端点不变律为 \(T(r,0)=(f_0(r),0)\)、\(T(r,-1)=(f_-(r),-1)\)，也包含 \(n(r)=1\)。它们的完整共同尾不可能相等，因为 seed 始终分别为 0、−1。

## 4. 正包、全部有限前像与固定控制

非零 lag isotropy 等价于 eventual full-state periodicity。若周期核心的 index product 大于 1，它只能是某个带端点标签的 \(f_0\) 或 \(f_-\) 循环。最小完整周期恰为该 root cycle 的最小周期 \(\ell_C\)。

对扩张循环 \(C\) 及其所有有限前像 \(B_C\)，实际前缀共轭给出

\[
G_z^z\text{ 的 lags}=\ell_C\mathbb Z,\qquad
c(z,k\ell_C,z)=k\log D_C,\qquad
H_z=(\log D_C)\mathbb Z.
\]

所有整数 \(k\) 均实现，故最小正值确为 \(\log D_C\)，不是仅发现一个返回值。clock 在这个 isotropy 上单射，固定对象的 extension isotropy 因而平凡。

每个 \(B_C\) 是一个完整实际 \(G\)-轨道，连同所有实坐标给出一个 time packet。不同 root cycles 不共享周期尾；同一个 root list 在两个端点中也仍不同。因此分类是两个 endpoint maps 的扩张循环集合的 **disjoint union**，各自按 cyclic rotation 计数。

unit-only 核心则保留 \(\ell_C\mathbb Z\) source isotropy，clock image 为 \(\{0\}\)，fixed-object extension isotropy 仍是整个 \(\ell_C\mathbb Z\)。前缀的瞬时 clock 在共轭中抵消，不能把这个零返回时间变成正包。

非 eventually periodic 状态无非零-lag isotropy。故扩张循环 basins 外的 \(H_z\) 全为 \(\{0\}\)，但不能一律称 source isotropy 平凡。

若初态属于正返回 basin，有限逆前缀从 seed 0 给出 \(x=b\ge0\)，从 −1 给出 \(x=b-D\le-1\)。初态 seed 必为嵌入整数；这只是必要条件，不是所有整数种子都会返回。

所有 basins 和 nonendpoint digits 仍在全 owner 中。它们可以改变 transient trajectories、前像、测度、拓扑与非闭箭头 clock；定理不声称完整群胚化为两个离散图。

最小正时间为 \(\log p\) 当且仅当 \(D_C=p\)。因为每个 index 是正整数，这等价于最小循环恰一次 index 为 \(p\)，其余全为 1。若最小 root cycle 的 product 是 \(p^a,\ a>1\)，它有自己的 primitive time \(a\log p\)，不是另一个包的第 \(a\) 次遍历。

由此“每素数恰一个包且无额外正包”的精确 ledger 条件是：每个 \(p\) 恰有一个 expanding tagged cycle 满足 \(D_C=p\)，且没有其他 expanding tagged cycles。这个条件不证明算术自然性。

两个预列固定控制吻合：

- 单根、\(n=2\)、两 digit 都回该根：恰两个正包，分别来自 0、−1，最小时间都为 \(\log2\)，不能按等时或相同 root list 合并。
- 单根、\(n=1\)：全部 \(K\) seeds 固定；source 与 fixed-object extension isotropy 均为 \(\mathbb Z\)，clock image 为零，没有正 cyclic-time packet。

## 5. 检查点 2：完整主稿比较

主文 Lemmas 1/3、Proposition 2、Theorem 4 与 Corollaries 5/6 均与 raw 推导相符。clock 的 inverse-prefix 正号、全部有限前像的共轭、最小 root period 与 primitive time 的关系均已核对。

未发现需修改的数学命题。唯一请求是 Corollary 5 proof 的 “Integer roots can also escape ...” 改为 “Integer-seed states can also ...”：\(R\) 是任意可数集合，整数属性在此属于 seed，而非 root。这是非阻断术语精度项，不改变证明。

主控已采纳这一处修正，主审已定点读回最终句。将该措辞还原后的全文字节 SHA 恢复为首次完整比较的主文哈希，确认没有其他正文改动；最终绑定如 §1，无需新证明回合。

## 6. 检查点 3：最强反方与范围

- **unit steps 会推翻端点结论吗？** 会推翻无条件版本；稿件仅对 \(D>1\) 应用端点引理，并完整保留 \(D=1\) continuum、source isotropy 与零 clock。
- **周期 root word 已经足够吗？** 不足够。实际 seed return equation 是必要步骤；其极值限制才把正核心约束到端点。
- **相同根列表或整数倍时间能否消掉 multiplicity？** 不能。实际共同尾与带标签的最小循环决定包，不能借 product 因式分解改写 primitive convention。
- **非整数无正返回是否意味着可删除？** 不能。它们仍参与 source、measure、topology，且可有 unit-only 周期状态；此处只有正时间账本被约化。
- **是否普遍否定素数选择？** 没有。两个 endpoint graphs 仍可有算术机制；本定理只要求这种机制在准入前被明确证明，不使每个类成员都失败。
- **是否把旧引理包装成新发现？** 没有。282 基本端点论证明确作为依赖，新审查范围是每个固定 owner 的 clock／packet／unit／basin 统一结论。
- **是否跨 owner 拼接？** 没有。每个 \(R,n,f\) 单独应用；278/285 只作范围控制，未供给本定理的证明，未转移其拓扑或 Route 结果。

## 7. 方法披露与交付范围

采用 ARS academic-research-suite 三检查点。主审 raw 推导先于主稿读取；同模型辅助 branch_return_controls 只读 raw 卡和许可依赖，核对 endpoint/unit sectors、最小周期、multiplicity、prime-product 与两个控制，未审 full clock、mixed-radix 或其他-seed basin 证明。

辅助未读主稿／他人答案，未写文件、外部检索或数值运行；主审完成全 owner、basins 与主文比较。共享模型与上下文仍可能共享错误；这不是外部同行评审、独立误差保证或形式验证。

支持本 screen 的 **STOP BLIND ROUTING SEARCH / FORK**：不再把未改变 endpoint mechanism 的 nonendpoint digit 丰富性当作新的正周期来源。无新 main candidate、无通用 no-go、无 T3，formal coordinates UNASSIGNED、Route B NOT INVOKED；旧包未改，241/242 未触碰。
