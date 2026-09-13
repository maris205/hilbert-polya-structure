# 有界阶 Hénon 同步混合：先例增量补充

日期：2026-09-06。状态：`BOUNDED_PRIMARY_PRIOR_SUPPLEMENT`。
本报告只对三点加强为 `3≤m≤d+1` 的新合同做有界增量查新。
它不是证明审查、Route 评价或候选评分；不估计论文容量。
实际执行者为独立 secondary 代理，没有调用指定 GPT-5.4 MCP 或人类评审。

前两份报告冻结：
[三点基线](PAPER30_HENON_THREE_POINT_MIXING_PRIOR_PROBE_20260906.md)；
[全次数三点补充](PAPER30_ALL_DEGREE_THREE_POINT_MIXING_PRIOR_SUPPLEMENT_20260906.md)。
本轮不重读其中未变的 BG/LV、Caprace–Kassabov 等来源。

## 1. 结论先行

在本次有限检索中，未找到直接覆盖完整合同的先例：对每个固定 `d≥2`，同一对
指定 Hénon 生成元及其逆，在所有素数 `p≥16d²`、所有 monic 次数 d 的 P 上，
对整个范围 `3≤m≤d+1` 的互异有序 m 点同词作用，具有只依赖 d 的统一正谱隙。
这只是未命中，不是“世界首次”，也不是数学或新颖性 PASS。

但是新辅助核的先例比“广义 Feistel 类似”强得多：Naor–Reingold 1999 已有
首尾低碰撞随机化、两轮函数、无碰撞条件下的精确联合质量论证，并明确推广到
k-wise independent 函数。该辅助核的核心原理应整体扣除，不能把“总变差先例，
本次 Doeblin”当作新的机制差异。逐点下界已经可从其证明直接读出。

剩余需要认真区分的贡献，是把这类已知随机置换机制定量实现在**固定同一对**
Hénon 动作中：相对整个仿射群的系数一致、次数受控短词实现，加上原始双生成元
上的仿射能量控制，最后得到完整有界阶合同。未找到直接覆盖这座桥的定理；
但“未找到”不为其中任何标准代数或比较步骤单独授予新颖性。

## 2. 本轮比较输入

令 `H_{P,j}(x,y)=(P(x)+j-y,x)`，`j=0,1`，且 P monic、次数恰为 d。
令 `X_{p,m}=Conf_m(F_p²)`，其大小为 `N_{p,m}=(p²)_m`。
目标算子及量词为

\[
\mathsf P_{p,P,m}=\tfrac12I+\tfrac18\sum_{j=0}^1
\bigl(\rho_m(H_{P,j})+\rho_m(H_{P,j}^{-1})\bigr),
\qquad
\inf_{\substack{p\ge16d^2\ \mathrm{prime}\\
P\ \mathrm{monic},\ \deg P=d\\3\le m\le d+1}}
\operatorname{gap}(\mathsf P_{p,P,m})\ge\delta_d>0.
\]

输入中的新机制：在 `ASL₂(F_p)∪{H_{P,0}^{±1}}` 的字度量内，反复有限差分、
对角缩放及 Cauchy–Davenport 幂值求和，拟以只依赖 d 的长度实现任意
`T_R(x,y)=(x+R(y),y)`、`deg R≤d`，及相应竖直剪切 V_S。
辅助核是独立随机因子的乘积 `A₁ V_S T_R A₀`，其中 A₀/A₁ 均匀于 ASL₂，
R/S 均匀于次数至多 d 的全部多项式。

主控提供的概率输入是：首端 y 投影和末端 x 投影各有至少
`1−binom(m,2)/(p+1)` 的无碰撞概率；在好事件内，两次插值给出精确质量
`p^(−2m)`，最终可取 `K(z,w)≥1/(2N_{p,m})`。
随后利用既有仿射扩张与字能量比较返回原始算子。
以上是本轮查新的比较对象，不是本报告对公式、常数或谱隙转移的验算。

尤其不能将“在整个 ASL₂ 被当作一个字母时字长只依赖 d”改写成
“每个仿射元素在原始两个生成元中都有独立于 p 的短词”。两者不是同一命题。
原来的三点面积／Weil 商链保留为独立结构旁证，不因新证明出现而重复计贡献。

## 3. 最接近先例：Naor–Reingold 1999

Moni Naor、Omer Reingold，*On the Construction of Pseudorandom Permutations:
Luby–Rackoff Revisited*，Journal of Cryptology 12 (1999), 29–66，
[DOI 与正式全文](https://link.springer.com/content/pdf/10.1007/PL00003817.pdf)。
在线读取正式版 §2.3、§3.2–3.3 的核心引理、§4、§5.2 及 §8 的 Corollary 8.1。
作者稿先可读取，后续抓取超时；正式版成功，不混用页码。

最相关定位如下：Definition 3.1 是 `h₂⁻¹ D_f₂ D_f₁ h₁`；Definition 3.5
（正式页 41）的坏事件正是首端右坐标或末端左坐标碰撞；Proposition 3.4
（正式页 42）控制其概率；
Lemma 3.5（正式页 42）给出好事件内精确质量 `2^(−2nm)`。
§5.2 / Theorem 5.2（正式页 49）只要求投影碰撞界。Corollary 8.1
（正式页 60）允许轮函数为
k-wise δ₀-dependent，所得置换误差为 `k²/2^n+k²/2^(2n)+2δ₀`。

分类：`DIRECT_AUXILIARY_METHOD_PRIOR, NOT_FIXED_HENON_SPECTRAL_THEOREM`。
以下取原文半块大小 `q=2^n`。映射是本报告基于原文的比较推断，
不声称原文已写出奇素数 Hénon 定理：

| 原文结构 | 本轮辅助核中的对应物 |
| --- | --- |
| 初始 h₁、终端 h₂⁻¹ | A₀、A₁ |
| 两轮 Feistel | 横向 T_R、竖向 V_S；交换坐标后的相同两轮结构 |
| 首端右投影／末端左投影无碰撞 | 初始 y／目标 x 互异 |
| 在互异输入上独立均匀的轮函数值 | 随机次数至多 d 多项式的 m 点插值，m≤d+1 |
| 好事件内联合质量为 q^(−2m) | 输入的 p^(−2m) |
| 对坏事件取并集上界 | 两端各 binom(m,2)/(p+1) |

把 XOR 换为有限域加减并保持可逆剪切，不改变“指定输入输出强制指定两轮
函数值”的逻辑。ASL₂ 的仿射随机化是一种适合本题面积保持约束的实例；
不能仅凭奇特征或 determinant-one 就把整个两轮论证标为新机制。

同样，虽然 Corollary 8.1 的陈述用总变差，Lemma 3.5 的精确条件质量配合
好事件概率已经给逐点下界。因此本文可以用 Doeblin 语言组织证明，但不宜声称
它克服了该先例只有 TV、没有逐点控制的本质障碍。
将有限域全函数改为低次随机多项式，使有限次求值精确独立，也是标准插值应用。
这只给出完整置换的近似 m-wise independence，不能据此宣称它 exact；
轮函数求值精确独立与最终置换带碰撞误差的保证必须在摘要、定理中分开。

## 4. 同步多点作用与谱隙的既有联系

Eyal Kaplan、Moni Naor、Omer Reingold，*Derandomized Constructions of k-Wise
(Almost) Independent Permutations*，Algorithmica 55(1) (2009), 113–133，
[作者单位出版记录](https://weizmann.elsevierpure.com/en/publications/derandomized-constructions-of-k-wise-almost-independent-permutati-3/)，
DOI `10.1007/s00453-008-9267-y`；[作者全文](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/kwise.pdf)。
读取作者稿 §2、§3.3、§4.1 和 §5.1–5.3 的相关陈述，不以预印本编号冒充期刊编号。

作者稿 Definition 3.9 的 companion graph 就是对互异 k 元组同时作用的图；
§3.3 通过重复复合放大混合；§5 用其谱隙构造短描述伪随机置换族。
§4.1 把 Feistel 的 k-wise 近似独立构造作为既有方法，并指出有效参数范围。
分类：`DIRECT_TUPLE_MIXING_FRAMEWORK_PRIOR`。

因此，“同词多点作用”“由 k 元组图谱隙得到近似独立置换”“组合若干轮放大混合”
都不是新问题定义或新抽象桥。该文没有指定当前两个 Hénon 动作，也没有声称
对全部 monic P、全部允许素数提供本题 δ_d。应扣除通用框架，保留具体生成集差别。

## 5. 换域及近期别名排查

Hector Bjoljahn Hougaard，*How to Generate Pseudorandom Permutations Over Other
Groups: Even-Mansour and Feistel Revisited*，
[arXiv:1707.01699v2](https://arxiv.org/abs/1707.01699)，2017-10-04。
本次核查作者摘要，确认已有把 Feistel 推广到一般群的研究；不据摘要猜测全文
定理对本题的覆盖。分类：`DOMAIN_GENERALIZATION_PRIOR_ONLY`。
它强化“从二元字符串到奇素域本身不应单列主要贡献”的判断，不提供当前谱隙。

William Gay、William He、Nicholas Kocurek、Ryan O'Donnell，
*Pseudorandomness Properties of Random Reversible Circuits*，
[arXiv:2502.07159v1](https://arxiv.org/abs/2502.07159)，2025-02-11。
本次只核查作者摘要：随机局部三比特可逆门的 k 元组链有定量谱隙，并导出
近似 k-wise independent 置换。其位串、局部门和维数参数不同，
不是固定平面 Hénon 对的直接定理，分类为 `RECENT_DIFFERENT_GENERATOR_PRIOR`。

重要版本警示：旧编号 [2404.14648](https://arxiv.org/abs/2404.14648) 已在
2025-02-12 撤回并指向合并稿；撤回说明特别指出其基于单向函数的某个计算安全
候选证明有误。这里不采用被撤回的计算安全结论，也不把该错误扩大成否定
合并稿仍保留的统计混合结果。

## 6. 有界字长实现的扣除边界

本轮对 `polynomial shear + word length`、`polynomial automorphisms +
Cauchy–Davenport`、`finite field + bounded generation` 等增量检索未找到直接
包含输入中“g=gcd(r+1,p−1) 个幂值求和＋逐次消系数＋系数统一长度”的同题定理。
这是有限检索未命中，不是该引理独立原创的证明。

已知归属沿用上一补充：有限差分交换子及降次已有 Edo–Lewis、
Bardakov–Neshchadim–Sosnovsky 的直接方法先例；有限域群生成／模拟已有
Maubach–Willems 等来源。它们不自动给出本题需要的统一字长。
Lagrange/Vandermonde 求值独立、Cauchy–Davenport 以及对角共轭对单项式的
缩放是标准工具，不能逐项计作新定理。

真正待核对的具体桥是：给定任意 P 和 R，是否确实能在**这一相对字度量**中
统一实现 R；所需的全部仿射元素，是否都有由原始双生成元能量统一控制的方式；
上述常数能否同时独立于 p、P 的系数和整个允许 m 范围。
这些是剩余证明义务／定位差别，本报告不替另一数学审查给结论。

## 7. 最小结论台账与停止边界

| 断言 | 查新后归属 |
| --- | --- |
| 两轮＋首尾随机化＋无碰撞精确质量 | 直接强方法先例，必须扣除 |
| 度数 d 给 m≤d+1 的精确函数值独立 | 标准插值，不等于置换精确独立 |
| 同步 m 点图、混合、谱隙及伪随机置换联系 | 既有框架 |
| 相对 ASL₂ 的有界字实现及原始双生成元统一能量桥 | 未找到直接覆盖；不授予单独新颖性 |
| 全 p、全 monic P、全部 m≤d+1 的同一 δ_d | 未找到直接完整先例；须独立数学验证 |

本次按 `research-lit`、`novelty-check` 执行，完整读取技能；使用公开一手来源，
没有可用的指定 reviewer MCP，也未虚报调用。检索覆盖 polynomial Feistel、
k-wise independent round functions、affine randomization/interpolation、
two-round permutation、Hénon/Henon、bounded-order/synchronous mixing、
uniform spectral gap、bounded word realization 等同义表述，并补近期 2024–2026
及最近 180 天别名。第三方索引仅用于定位，外部科学断言只依赖上述一手来源。

只新增本文件；没有外部写入、实验、本地 PDF 下载或新增代理。
遵循明确范围，不做技能中的通用会议扫描、评分或容量估计；没有重启旧构建验证。
未命中置信度为中等：密码学、群生成和有限域动力学之间可能仍有术语差异漏检。
到此停止有界增量查新。建议候选叙述明确承认 Naor–Reingold 型辅助机制，
将潜在贡献限定为上述固定 Hénon 双生成元的系数一致有界阶扩张合同。
