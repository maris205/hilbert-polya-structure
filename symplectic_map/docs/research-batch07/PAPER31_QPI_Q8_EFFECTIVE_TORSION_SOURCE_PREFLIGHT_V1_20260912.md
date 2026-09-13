# Paper31 Q8：有效同时扭的来源与强问题预筛 V1

日期：2026-09-12 UTC；会话环境日期09-13不用于虚报未来检索。性质：作者来源／证明可行性记录，非正式候选票。
Papers27–30 已接受4/5；Paper31 原22–30页、两位fresh各自完整四门及既有失败全部保持。
只核原正参数族中不同固定正代数 \(T_1\ne T_2\) 的同 \(h\) 问题，不做阶数扫描、实现停止算法或全prime工程。

## 1. 最强拟议中心与当前已证内容分开

沿用 [I 文件](PAPER31_QPI_Q8_DISTINCT_FACTORS_INTERFACE_V1_20260912.md) 的 \(S(T_1,T_2)\)、\(E_{T,h}\) 与 \(P_T\)。
设
\[
 d=[\mathbb Q(T_1,T_2):\mathbb Q],\qquad
 H=1+\mathrm h(T_1)+\mathrm h(T_2),
\]
其中 \(\mathrm h\) 是绝对对数 Weil 高度。

**Q8-E（未证）。** 给定正代数输入的有限编码，可有效计算一个上界 \(B(T_1,T_2)\)，
使每个 \(a\in S(T_1,T_2)\) 的两个扭阶均不超过此界。
这比定性有限性强；仅逐个寻找扭点而没有终止证书不算回答。

**Q8-P（更强、未证）。** 存在有效可计算的绝对常数 \(C,A>0\)，使对所有上述输入及所有 \(a\in S\)，
\[
 \max\{\operatorname{ord}(P_{T_1,a}),\operatorname{ord}(P_{T_2,a}),
 [\mathbb Q(a):\mathbb Q],\,\mathrm h(a)\}\le C(dH)^A.
\]
常数必须独立于 \(T_1,T_2,a\)，不得暗中使用未知最小间距或未控制的覆叠高度。
近对角 \(T_1\to T_2\) 也在量词内；高度与次数可控制非零代数差的分离，但本轮未推导最终指数。
阶数界才是主要有效增量；高度有界已有单因子强先例，次数可能是阶数界后的标准消元消费者，不分别冒记为三项创新。

I 的短证明和 [L 的乘积叶纸测](PAPER31_QPI_Q8_PRODUCT_LEAF_BLOCK_PAPER_TEST_V1_20260912.md) 已实际写出，尚待fresh数学复核：
两个因子几何非同源、非等常、迹零、两截面泛非扭；BC定理给同时扭有限；
已有强日志独立性给所有叶的投影有限germ及固定底点代数块，紧片近叶实交至多一点。
上述均不宣告 Q8-E 或 Q8-P 已证，也不把未证强问题压缩为已证短接口后再判其不足。

## 2. 方法与取证边界

按 research-lit 做定向检索，novelty-check 分开来源包含与剩余增量，proof-writer 组织实际纸证。
ARS 仅取 scoped fact-check／一手来源验证与质量分层；不启动完整深研、13角色流水线或实验。
无配置的 Zotero／Obsidian／指定 Codex MCP，使用公开一手网页及公开PDF流式文本；没有PDF落盘。
下面的 FULL 表示所列页段或摘要完整读到，不表示整篇论文全文通读。
数学定理的质量依据是准确命题／假设／证明接口及一手出版来源，临床研究设计层级不适用；未审查的全部正文、利益冲突等不虚填“无问题”。
聚合页只用于发现／身份交叉确认；科学结论以列明的一手来源为准。来源提到未发表工作，只记线索而不当可用定理。

## 3. 实际检索：22条query

前轮八问景观的31条不计入本轮；本轮以下22条均实际发出。结果有无关医学／材料／扭转梁等，已按数学对象排除。

1. effective simultaneous torsion two non isogenous elliptic schemes Binyamini Barroero Capuano 2025 2026
2. Binyamini effective relative Manin Mumford products elliptic curves distinct factors
3. site:arxiv.org simultaneous torsion elliptic curves effective 2024 2025 2026
4. "effective" "torsion" "non-isogenous" "Binyamini"
5. "effective" "simultaneous torsion" elliptic
6. "torsion points on families of products of elliptic curves"
7. "effective" "non-isogenous" "torsion" "2024"
8. "effective" "relative Manin" "2026"
9. "Unlikely intersections in products of families" arxiv
10. "Six unlikely intersection problems in search of effectivity"
11. Binyamini "non-isogenous" elliptic curves
12. "effective" "simultaneous torsion" after:2026-03-12 before:2026-09-13 elliptic
13. "relative Manin-Mumford" "effective" "2025"
14. "Binyamini" "torsion" "families" "2026"
15. "Barroero" "Capuano" "effective" elliptic 2024 2025 2026
16. "Unlikely intersections in products of families of elliptic curves" "2017" "Quarterly"
17. "The relative Manin–Mumford conjecture" "August" "2026"
18. "effective" "torsion" "non-isogenous families"
19. site:arxiv.org "Buium" "Coleman" "Pandit"
20. site:arxiv.org "Isogeny relations in products of families of elliptic curves"
21. site:arxiv.org "Relative monodromy of ramified sections"
22. "Monodromy of elliptic logarithms: some topological methods and effective results" arxiv

这是有界多表述筛查，不是穷尽数据库／PRISMA；未检得与强目标逐字同一的定理不等于全球新意。

## 4. 一手来源、实际阅读及准确包含

| ID／来源 | 本轮实际主控阅读 | 对本题的意义与限制 |
|---|---|---|
| BC：Barroero–Capuano, *Unlikely intersections in products of families of elliptic curves and the multiplicative group*, QJM 2017, DOI 10.1093/qmath/hax014；[作者v2](https://arxiv.org/abs/1606.02063)、[PDF](https://arxiv.org/pdf/1606.02063) | 官方摘要／元数据FULL；PDF pp.1–7 FULL，含Theorem1.1、Lemma2.1、Cor2.5及其证明 | n=m=1直接包含定性同时扭有限性；该特例还指向Masser–Zannier。坏支撑非同源论证及强日志独立性均已有；有限阶的有效上界不是这里读到的结论。 |
| BIN：Binyamini, *Point counting for foliations over number fields*, FoMPi 10 (2022), e6, DOI 10.1017/fmp.2021.20；[官方页](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/point-counting-for-foliations-over-number-fields/D8B743946064FC7DDE59131375AF9465)、[PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D8B743946064FC7DDE59131375AF9465/S2050508621000202a.pdf/point-counting-for-foliations-over-number-fields.pdf) | PDF pp.1–5、20–28 FULL；含Definition4、Theorem3、Theorem6和§§8.1–8.6的完整应用证明；非整篇39页FULL | Theorem6明写同一Legendre族的平方，不可直接写成不同因子的定理。其一般近叶计数Theorem3与整个方法已提供强有效化框架；p.21明确说其它MZ／BC变体似可处理、本文未逐项展开。 |
| TR：Tropeano, *Monodromy of double elliptic logarithms*, RSMUP154 (2025),45–75, DOI10.4171/RSMUP/156；[出版PDF](https://ems.press/content/serial-article-files/51210) | PDF pp.1–4 FULL，含引言所列Theorem4.11(2)，不是全部31页证明 | 不同非同源因子的相对日志单值化群为满秩Z⁴；为强结构先例，不自动提供输入高度控制的扭阶界。本纸测用BC的强AI，不借未读的TR完整证明替代。 |
| GH：Gao–Habegger, *The relative Manin–Mumford conjecture*, Invent.Math.2026, DOI10.1007/s00222-026-01443-3；[官方全文页](https://link.springer.com/article/10.1007/s00222-026-01443-3) | 官方摘要、引言Theorem1及Corollary2／Theorem3所在段落；其余全文未通读 | 官方出版日期2026-08-26，是真正近期更新；广义相对定性结论与统一计数不能自动改成有效常数或扭阶界。本题较早BC已足够，不以GH另造新意。 |
| TE：Tropeano, *Monodromy of elliptic logarithms: Some topological methods and effective results*, JNT280 (2026),49–87, DOI10.1016/j.jnt.2025.08.008；[官方预览](https://www.sciencedirect.com/science/article/abs/pii/S0022314X2500229X)、[作者版](https://arxiv.org/abs/2402.07741) | arXiv官方摘要FULL；出版检索正文的摘要、引言及节概览，非39页全文 | 有效构造对周期作用平凡而对日志非平凡的回路／满秩子群，并处理分歧。不能仅据“effective”标题当作有效共同扭阶定理。作者首页标2025；以官方卷期2026-03区分online/卷期，不把2024预印本变成2026新首发。 |
| DT：Dolce–Tropeano, *Relative monodromy of ramified sections on abelian schemes*, IMRN2026, DOI10.1093/imrn/rnag025；[作者版](https://arxiv.org/abs/2407.19476) | 官方摘要、版本历史FULL；未读完整证明 | 最新所核arXiv v4为2025-05-28；一般阿贝尔概形相对日志单值化强先例。不是从期刊年份推出最近六个月新证明或有效扭阶界。 |
| HJM：Habegger–Jones–Masser, *Six unlikely intersection problems in search of effectivity*, Math.Proc.Camb.Phil.Soc.162 (2017),447–477；[作者版](https://arxiv.org/abs/1509.06573) | 官方摘要／元数据；未读31页全文 | 特定CM、Legendre指定点扭与单位根条件组合的有效问题，不能当作任意两个非同源因子同时扭的直接定理。2015讲座网页2025更新时间不是新定理时间。 |
| LF：Ferrigno, *Isogeny relations in products of families of elliptic curves*, DOI10.1515/forum-2025-0128；[作者v3](https://arxiv.org/abs/2409.01408) | 官方摘要／版本历史FULL；未读证明 | v3为2025-10-23，有特定次数假设及纤维同源关系条件；不同于这里不附加纤维同源条件的同时扭集合。不能把摘要涵盖误作强Q8包含。 |
| DP：Dogra–Pandit, *A Buium–Coleman bound for the Zilber–Pink conjecture for curves inside abelian varieties*；[预印本](https://arxiv.org/abs/2608.24474) | 官方摘要／历史FULL；未读30页证明 | v1为2026-08-25，是近期预印本而非已刊定理；对象在固定阿贝尔簇，包含模大素数约化像的显式界与附加结构结果，不自动给本相对族扭阶界。 |

另外只作发现线索：DeMarco–Mavraki JEMS2024 的椭圆曲面／adelic实除子文章仅读摘要片段与关键词段落；
共同projective torsion的2024预印本仅读摘要片段，固定两椭圆曲线向 \(\mathbb P^1\) 的投影问题不等于本基变族；
Tropeano作者页所列BC–Ge–Tropeano Northcott工作仍标 work in progress，无可核正文，不消费其潜在结论。
这些碎片不是核心证明来源，不能由未读部分推断不存在更强包含。

## 5. BIN 逐接口适配账本：已闭合与 OPEN

| 依赖 | 同平方原文位置 | 本题现状 |
|---|---|---|
| 非同源、非等常、泛非扭与真子群排除 | BC Theorem1.1／Lemma2.1所需假设 | I1–I4实际短证；未记新理论。 |
| 进入有限Legendre覆盖 | BC曲线模型；BIN §8.1 | I5定性覆盖已写；统一覆盖次数／系数高度／例外点复杂度尚未逐项给算术界。 |
| 有理向量场与全叶参数化 | BIN §8.1 | L各因子分别拉回并给 \(G=(\mathbb C^2\rtimes GL_2)^2\)；没有把主丛传递性当微分Galois满群。具体算术模型大小尚待控制。 |
| 日志独立、投影有限germ、块分类 | BIN Lemmas36–37 | L实际纸证，使用BC函数域强形式；实交至多一点，不声称复代数部分为空。 |
| 截面专化高度与阶数—域次数关系 | BIN Lemmas30–31 | 原文使用已有椭圆高度／扭点理论；本题尚未给对两输入一致的常数链。不能把单因子已有高度界另记为创新。 |
| 多数共轭留在紧集、覆盖disc选择 | BIN Lemmas32–33 | 两因子的坏值并集／有限覆盖能否以同样多项式复杂度控制，须写实际估计，不以“类似”宣告完成。 |
| 周期、日志及导数增长、反角度 | BIN Lemma35与§8.4，引用AppendixA | 本轮读完整§8.4，但未读AppendixA完整证明；L仅给紧片上定性m>0，不是有效的 \(\exp[-\operatorname{poly}(d,H)]\) 下界。 |
| 近叶尺度、实有理块数、投影重数 | BIN §8.6、Theorem3与Corollary2 | 原机制已明确；本题还未给算术尺度 \(\epsilon\)、\(\delta_\xi,\delta_V,\delta_\Phi\) 的统一界，不能直接调用无代数曲线的Corollary6。 |
| 最终power对polylog不等式 | BIN式(112) | 若前链齐备即标准闭合；目前并非独立的新难点或已证强Q8。 |

对不同因子，L消除了“必须先发明新的双日志超越定理／高维块理论”的猜测。
但是适配短不等于最终统一有效化已经被逐字发表，也不等于常数工程在这里已经做完。
作者当前判断：Q8-P 有明确的强标准框架压力；需要fresh非作者判断其剩余实质能否支持独立中心，再决定是否值得继续完整常数链。

## 6. 留给独立预核的具体问题

请分别判断三个层级，不混写：

1. I／L当前纸证是否成立（另委派fresh数学任务），及哪些结论已经是直接消费者。
2. 若Q8-P最终严格成立，其扣除BC、BIN全部近叶方法后是否仍有足够新意／独立价值；不要仅给弱有限性评分，也不因题名不同就认为高新意。
3. 单一有效同时扭中心能否自然支撑22–30页完整证明；详述可迁移新机制还是重复已有方法。容量预测不是试排，也不要求事后改页数。

这不是正式ALL4申请：强目标未证、source/publication locks未建，故不能取得正式证明门或正式准入。
没有要求评审给7.5，也不重投旧b7.4或twist7.2失败包。新的预核只根据本轮实际新输入。
若不足，保留短数学、明确停止该独立中心，不把未证说成反证；若仍有实质存活，则下一项才是具体有效化链的纸证。
不通过反复抽审或不断加短推论制造准入；Q2／Q3仍为未核备选，当前不展开并行批次论文。
