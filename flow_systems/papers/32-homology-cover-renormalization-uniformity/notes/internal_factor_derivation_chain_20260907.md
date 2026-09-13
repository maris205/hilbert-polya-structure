# P32 内部笔记：候选覆盖因子到条件比较的推导链

记录日期：2026-09-07 UTC。用途：整理已有推导及其缺失前提，供内部研究接续；不是新定理报告、论文修订或完整性重审。

依据：[当前 R6 稿件][draft]，由 [Round-4 Recovery3 五篇输入索引][index] 指定。标量引理与形式载体的旧记录分别为 [条件标量引理记录][scalar]、[形式定义记录][formal]。下文沿用它们原有的限定范围，不把旧记录中的 `PASS` 当成本轮的新审查或科学结果。

按现稿的依赖关系，关键缺口是“这些候选表达式是否确实来自指定覆盖及指定 owner”，不是再次计算候选函数之间的不等式。已有标量引理和代数载体可以登记为现成文本；项目因子推导与实际 owner 比较仍未完成。

## 1. 保持固定的研究对象

- 覆盖塔为 `H_N = ker(Gamma -> H_1(Sigma; Z/NZ))`，基底为固定带标记的亏格二曲面；不换成前一分支的 residual inverse-limit 系统。
- owner 为有向本原共轭类，逆方向仍分开；同调向量位于 `Z^4`，正 content `d` 为绝对坐标的最大公因数，零向量另作零 content 分支。
- 物理提升时间乘以 `1/N`；原始提升分量乘积的对数乘以 `1/N³`。两项作用在不同层次，不能随 content 或结果调参。
- 高 content 的控制模数序列是 `N_k = k!`。不能换成任意挑选的模数子列，再把得到的行为归给原问题。

对应现稿 [B0013–B0014 定位入口][frame]、[B0064][schedule]。以上是固定定义／安排，不是已经验证某个具体 owner 的证明。

## 2. 候选因子字段对照

令 `ell = ell(g) > 0`。正 content 分支令 `q_N(g) = gcd(N,d)`。以下字段均摘自现稿的待证明目标；表中数值不是新增观察或新完成的覆盖论推导。

| 字段 | 正 content `d > 0` 的候选值 | 零 content 的候选值 |
| --- | --- | --- |
| deck-image order | `N/q_N(g)` | `1` |
| 本原提升分量数 | `N³ q_N(g)` | `N⁴` |
| 乘以 `1/N` 后的周期 | `ell(g)/q_N(g)` | `ell(g)/N` |
| 原始乘积经 `1/N³` 对数归一化后的指数 | `q_N(g)` | `N` |
| 归一化局部因子 | `F_N,g(s) = (1-exp(-s ell(g)/q_N(g)))^(-q_N(g))` | `F_N,g^(0)(s) = (1-exp(-s ell(g)/N))^(-N)` |

来源：[B0053–B0057 候选式及限制][candidates]、[B0061–B0062 中间字段与归一化顺序][fields]、[B0071 零 content][zero]. 比较基准是现稿定义的 `B_g(s) = (1-exp(-s ell(g)))^(-1)`，不是已由本次材料恢复出的乘积。

现稿要求先导出原始提升乘积，再分别应用两项固定归一化。仅把表中的阶数、分量数和指数代入并整理成同一表达式，不能替代各字段的几何／覆盖证明。

## 3. 项目因子与标量引理之间缺什么

以下编号只用于内部笔记定位，不是新增审查编号、正式证书 schema 或已执行测试。

| 衔接项 | 需要给出的内容 | 当前可记录的状态 |
| --- | --- | --- |
| L1：实际 owner 绑定 | 精确有向本原代表、同调向量、content、长度及输入表示 | 已有字段要求；本笔记未新增 owner 或其证明 |
| L2：覆盖作用与阶 | 从固定带标记表示给出 deck action，并证明相应阶数 | 候选值已写出，项目推导仍缺 |
| L3：提升分量 | 证明分量计数和覆盖次数，并说明每个被计入分量确为本原提升 | 不能仅从候选指数倒推计数或本原性 |
| L4：物理时间 | 给出未缩放周期及其依据，再明确乘以 `1/N` | 现稿要求绑定两种周期；未在此补做几何推导 |
| L5：原始乘积与对数归一化 | 先明确原始分量乘积及重数，再应用 `1/N³` | 不能把时间归一化与指数归一化混为一步 |
| L6：表达式进入有限定义域 | 识别对应形式元素、定义域、比较映射与假设 | 有限映射已定义；项目因子进入映射的连接未完成 |
| L7：比较与结果命名 | 前提齐备后才判断相等、不等或不可评估 | 本次无实际 owner 比较；不写成 mismatch、障碍或恢复结果 |

这张表重排了 [B0057、B0061–B0062][fields] 与 [B0084][projection] 的既有义务。某一步的缺口不能由后续标量不等式或通过的格式检查补足。

## 4. 已有条件标量引理及三条使用边界

已有引理在 `ell > 0`、实数 `s > 0`、整数 `m >= 2` 下比较

\[
\Phi_m(s)=(1-e^{-s\ell/m})^{-m},\qquad
B(s)=(1-e^{-s\ell})^{-1},\qquad
\Phi_m(s)>B(s).
\]

现稿及旧标量记录已有短证明：取 `x = exp(-s ell/m)`，利用 `(1-x)^m < 1-x < 1-x^m`，再对正数取倒数。[B0060][lemma]。本轮没有重新运行证明审查。

| 分支 | 何时可调用已有引理 | 不能省略的限制 |
| --- | --- | --- |
| 高 content `d >= 2` | 在固定阶乘序列已达到 `d` 整除 `N`，相应覆盖因子已导出、`q_N(g)=d`，且比较定义域已绑定之后，令 `m=d` | `Phi_d > B` 此前只是条件蕴涵，不是已观察到的 ownerwise mismatch |
| 零 content | 单独完成零 content 的 deck／分量／本原提升／归一化推导，并进入同一 owner 的合法有限标量域之后，对固定 `N >= 2` 令 `m=N` | 不能由正 content 公式非正式代入 `d=0` 得到项目结论 |
| content one | 现稿候选式中 `q_N=1`，但不属于该引理的 `m >= 2` 假设 | 候选式简化不等于覆盖因子已推导、全局乘积已定义或恢复已成立 |

对应 [B0066][higher-use]、[B0072][zero-use]、[B0076][one]. 本笔记不扩大到复数 `s` 上的大小关系，也不从有限模数前缀推断无限序列行为。

## 5. 有限标量化不等于无限对象求值

正 content 对有限 `F ⊂ O_+` 使用

\[
A_F=\mathbb Q[u_g:g\in F]
[(1-u_g^r)^{-1}:g\in F,\ r\in\mathbb N],
\]

以及 `Re(s)>0` 下的 `sigma_(s,F): A_F -> C`，其变量赋值为 `u_g -> exp(-s ell(g)/d(g))`。`j_F: A_F -> R_+` 是另一映射；并未声明整个 `R_+` 上的标量求值。[B0082][positive-domain]。

零 content 对固定 `g,N` 使用同一个带标签的 Hahn 纤维 `H_g` 内的

\[
A^0_{g,N}=\mathbb Q[z_g^{1/N}]
[(1-z_g^{1/N})^{-1},(1-z_g)^{-1}],
\]

以及 `tau_(s,g,N): A^0_(g,N) -> C`，`z_g^q -> exp(-s ell(g)q)`，同样要求 `Re(s)>0`。没有整个 `H_g` 的标量求值，也没有不同零 content owner 之间的乘积或向 `R_+` 的类型转换。[B0134][zero-domain]。

现稿的单 owner 投影 `pi_g: R_+ -> Q[[u_g]]` 只提供单向检验接口：两个已经定义的元素若相等，其投影必相等；一个合法坐标上的不等可以反驳这两个元素相等。反向不成立，混合项 `u_g u_h` 会被所有单 owner 投影消去。[B0084][projection]。

所以，“有限标量域已经定义”“候选函数已知不等”“全局项目对象不相等”是三个不同层次。不能跳过 L1–L6，也不能凭投影相等推出全局恢复。

## 6. 解析义务仍单列

仅在前面的局部研究支持继续 content-one 分支时，才进入现稿列出的解析工作。固定紧集为

\[
K(\delta,T,R)=\{s:1+\delta\leq\operatorname{Re}s\leq R,
\ |\operatorname{Im}s|\leq T\},
\]

其中 `delta>0`、有限 `T>=0`、有限 `R>=1+delta`。分别处理两个模数序列 `S_k=k!`、`S_k=2(k!)`，对角截断 `m_k=2^k`，不能互相替换。[B0087–B0089 定位入口][analytic-frame]。

| 现有项目 | 所列义务，均非本轮完成结果 |
| --- | --- |
| AN-1 | 固定序列与 `k`，使 owner 截断 `m -> infinity`，建立紧集上一致的可求和控制 |
| AN-2 | 固定有限 `m`，分别沿两个序列令 `k -> infinity` |
| AN-3 | 先 `m -> infinity` 再 `k -> infinity`，需要不依赖 `k` 的可求和控制函数 |
| AN-4 | 证明反向迭代次序与 AN-3 相同，并对应同一 owner 求和 |
| AN-5 | 沿 `m_k=2^k, N=S_k` 识别对角极限与共同迭代极限，并控制消失尾项 |

来源：[B0136–B0091 定位入口][analytic]. 现有有限前缀／panel 仍未执行，即使以后有限诊断一致，也不自动满足这些无限极限义务。

## 7. 本次记录结果

已把现稿分散的候选字段、条件引理、有限标量域和解析前提整理成可回指的衔接表。没有新增覆盖因子证明、owner 样本、数值比较、实验脚本、来源核验或 Route 判断；没有修改现稿、旧审查、锁和回执。正式未决状态保持原样。

下一项实质研究应从 L1–L3 的精确输入／覆盖作用／本原提升依据着手，而不是把已有标量比较再次包装为科学发现。本句标明现有依赖顺序，不表示相关推导或计算已经启动。

[draft]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex
[index]: /root/autodl-tmp/flow_systems/BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_REPORT_INPUTS.json
[scalar]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_conditional_scalar_lemma_audit_round2.json
[formal]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_formal_definition_audit_round2.json
[frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:102
[schedule]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:585
[candidates]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:493
[fields]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:556
[zero]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:637
[lemma]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:531
[higher-use]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:598
[zero-use]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:647
[one]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:681
[positive-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:764
[zero-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778
[projection]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:833
[analytic-frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:858
[analytic]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:904

## 追加进展：覆盖局部因子的条件证明（2026-09-07）

后续[内部条件推导笔记](internal_conditional_cover_factor_derivation_20260907.md)在明确的标记、正规局部等距覆盖、基轨道最小周期与 Euler 因子计数假设下，给出了 L2–L6 的条件论证，并衔接到 L7 的有限条件比较。它分别证明正／零 content 的阶数、分量数、最小提升周期及两项归一化，未认证具体 owner 或全局产品。上文是此前整理时的状态快照，原文保留；新证明及其范围以该后续笔记为准，不由此更新正式稿件或审查状态。
