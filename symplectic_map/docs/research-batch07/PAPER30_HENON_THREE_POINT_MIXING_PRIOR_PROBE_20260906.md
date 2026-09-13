# 固定 Hénon 生成元的三点同步混合：有界一手先例核查

日期：2026-09-06。状态：`BOUNDED_PRIMARY_PRIOR_PROBE`。
实际执行者为 secondary xhigh 代理；没有调用 GPT-5.4 MCP 或人类评审。
只核查先例，不审查主控数学证明，不打候选分、不估计页数。

## 结论

本次未找到直接涵盖以下全部量词的已知定理：二维、两个固定整数 Hénon 生成元、
所有充分大奇素数、三个互异有序点接受同一个随机词、统一正谱隙。
这是有限检索的未命中，不是世界首次或完整查新 PASS。

最重要的非线性强先例是 Caprace–Kassabov 2023：他们确实用显式低次数多项式
置换构造了整个交错群的统一扩张，不能以“非线性、多项式、有限域、显式生成元”
这几个词宣称新意。然而其维数、空间和具体生成元不同，未发现向本题的直接转移桥。

最贴近“三点同词”这个表述的近期先例是 Cassidy 2024/2025 的多元组 Schreier
图定理；但其生成元在大对称群中随机选取，不覆盖指定的 Hénon 两元组。

可保留的精确增量仅是：在已知仿射扩张之上，为这些固定非线性生成元证明
面积/共线比值轨道之间的统一混合，并将其转回原四个动作的 lazy walk。
主控提出的两个三次表达式是否充分完成这一步，由作者证明及后续数学审查决定。

## 1. 比较合同

令 `H_j(x,y)=(x^2+j-y,x)`，`j=0,1`，在
`X_p=Conf_3(F_p^2)` 上逐点同时作用。可固定算子规范为

\[
P_p=\tfrac12 I+\tfrac18\sum_{j=0}^1
\bigl(\rho_3(H_j)+\rho_3(H_j^{-1})\bigr).
\]

目标是存在与 `p` 无关的 `epsilon>0,p_0`，使所有奇素数 `p>p_0` 上，
`P_p` 在均匀测度的零均值空间的算子范数至多 `1-epsilon`。
本报告不因写出这个合同而声称它已证明。

| 容易混淆的结论 | 为什么不等于当前目标 |
| --- | --- |
| 单点作用的谱隙 | 不控制张量表示中新出现的不变量 |
| 两点作用的谱隙 | 仿射面积/共线比值障碍在三点才出现 |
| 三份独立随机词分别作用 | 转移算子是独立乘积，不是同一个生成元的对角作用 |
| 已知生成整个 Alt 的事实 | 连通性不提供与 p 无关的谱隙 |
| 某组 Alt 生成元的 Cayley 谱隙 | 必须有与 p 无关的词长比较，才能转到当前生成元 |
| 当前三点谱隙 | 不反向推出整个置换群的 Cayley 谱隙 |

若同一生成集的整个交错群 Cayley 图有统一谱隙，则其三点商作用也有；
这是表示限制的标准推论，不能把这个单向蕴含倒用。

主控给出的研究机制是：先在 `ASL_2(F_p)` 轨道内平均，再利用 Hénon 动作混合
轨道标签。非共线轨道按有向面积 `Delta` 分类，共线轨道按比值 `a` 分类；
所述变换为 `Delta'=Delta+uv(u-v)`，共线情形为 `a(1-a)u^3`。
这些是本次查新的输入，不是本报告独立核查的定理。

## 2. 最接近的强非线性先例

### Caprace–Kassabov，2023

Pierre-Emmanuel Caprace、Martin Kassabov，*Tame automorphism groups of polynomial
rings with property (T) and infinitely many alternating group quotients*，
Transactions of the AMS 376 (2023), 7983–8021。
直接在线读取 [作者 v3 PDF](https://arxiv.org/pdf/2210.00730v3) 的引言、定理
1.1、1.2、1.5 及其设置；未下载到本地。

定理 1.5(i) 对每个奇素数，用
`sigma(x,y,z)=(y,z,x)`、`alpha=(x+y,y,z)`、`beta=(x+y^2,y,z)`
在 `F_p^3 \ {0}` 上生成 `Alt(p^3-1)`，其六度 Cayley 图组成扩张族。
1.5(ii) 还给出七维、两生成元的四度版本。

分类：`STRONG_CLOSE_PRIOR, NOT_DIRECT_COVER`。
它比仅三点作用的结论强，但基集合不是 `F_p^2`，动作也不是两个指定 Hénon。
尚未看到用当前生成元的统一有界长词模拟其动作的桥；不能只比较状态集大小。
定理 1.1 的 property (T) 构造要求秩至少三，不能直接把维数改成二。

## 3. 多点同词扩张的近期先例

### Ewan Cassidy，2024 首投、2025 v3

*Random permutations acting on k-tuples have near-optimal spectral gap for
k=poly(n)*，arXiv:2412.13941。
直接读取 [2025-10-24 v3](https://arxiv.org/pdf/2412.13941v3) 引言、定理 1.3、
定义和 Remark 1.4。定理对固定 `r>1` 个独立均匀随机置换的对角 k 元组作用
给出高概率近最优谱隙；本题所需的固定 `k=3` 在其范围内。

分类：`SAME_ACTION_TYPE, DIFFERENT_GENERATOR_QUANTIFIER`。
“同一个词作用所有点”不是新定义；但高概率随机置换结论不蕴含一个给定低次数
整数生成集对所有大素数成立。论文也明确区分多元组 Schreier gap 与全群 Cayley gap。
Remark 1.4 指回 Friedman–Joux–Roichman–Stern–Tillich 1998 的固定 k 一致扩张；
本次未另读该旧文，不将其详细定理冒称直接原文核查。

版本提醒：搜索缓存仍返回 `1/12` 指数，实际 v3 是 `1/20`；本报告按实际 v3
绑定，且不依赖这个增长指数来论证 `k=3`。

### Chen 等，2024

Chi-Fang Chen、Jeongwan Haah、Jonas Haferkamp、Yunchao Liu、Tony Metger、Xinyu Tan，
*Incompressibility and spectral gaps of random circuits*。
直接读取 [作者 v3](https://arxiv.org/html/2406.07478v3) 的可逆电路设置、定理
1.1/1.2 及局部门分解说明。
其同一个可逆电路在 t 份上的矩算子确实有统一于 t 的谱隙界，但界随比特数 n
退化（定理 1.1 为 `Omega(n^-3)`），采样的是局部可逆门，不是当前四个动作。

分类：`STRONG_METHOD_PRIOR, NOT_DIRECT_COVER`。
尤其不能把“独立于 t”误写成独立于底层空间规模，或拿其门模拟长度当成常数。

## 4. 必须扣除的仿射工具

Jean Bourgain、Alex Gamburd，*Uniform expansion bounds for Cayley graphs of
SL_2(F_p)*，Annals of Mathematics 167 (2008), 625–642。
[官方原文与摘要](https://annals.math.princeton.edu/2008/167-2/p07) 处理固定整数
矩阵生成非初等子群后的模 p 扩张；这足以构成 `U_2,L_2` 部分的强标准工具。

Elon Lindenstrauss、Péter P. Varjú，*Spectral gap in the group of affine
transformations over prime fields*，Annales de la Faculté des Sciences de Toulouse
25 (2016), 969–993。
直接读取 [出版 PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1518.pdf)
定理 1、定理 2 和引言设置。定理 2 对 `F_p^d ⋊ SL_d(F_p)` 的概率测度，把
全群谱隙从下方控制为线性投影谱隙及单点一步最大集中概率缺口的最小值乘常数。

分类：`STRONG_TOOL`。这些结论可控制仿射群及其每个轨道内的作用，不会消除
仿射群本身保留的面积和共线比值标签。因此一/二点扩张、仿射轨道内平均，以及
固定有界词比较本身，均不应作为当前三点非线性工作的主要新结论。

本报告没有声称整个 `ASL_2(Z)` 具有 property (T)；不能把 relative (T)、
有限商 property tau 与整个群的 property (T) 混写。

## 5. 两尺度拼接不是新的通用定理

Neal Madras、Dana Randall，*Markov Chain Decomposition for Convergence Rate Analysis*，
Annals of Applied Probability 12 (2002), 581–606。
在线读取 [作者稿](https://randall.math.gatech.edu/r-factor.pdf) 的设置与定理 1.1：
总谱隙由块内限制链、块间链及覆盖参数控制。其具体假设不能省略。

Sarah Miracle、Amanda Pascoe Streib、Noah Streib，*Iterated Decomposition of Biased
Permutations Via New Bounds on the Spectral Gap of Markov Chains*，
Theory of Computing 21(3), 2025。
读取 [正式出版页及原文](https://www.theoryofcomputing.org/articles/v021a003/)
的摘要、引言及 complementary decomposition 的定位。

分类：`STRONG_METHOD_TOOL`，不是对本题的直接覆盖。把已知轨道内 gap 与某个
已证明的商链 gap 拼接，是成熟方法；真正需要作者新证据的部分是本题商链的
具体转移核、各轨道权重、退化共线层及与原生成元的统一比较。
本报告不替主控决定采用哪个分解定理，也不作这些假设已满足的数学判断。

## 6. 近期同名或近名结果的排除

- [Bays–Zou，arXiv:2506.23015](https://arxiv.org/abs/2506.23015)：已核对作者摘要。
  研究复二维多项式自同构的组合非扩张/Elekes–Szabó 问题，不是有限域 Markov 谱隙。
- [Hiroki Sumi，arXiv:2408.03577](https://arxiv.org/abs/2408.03577)：作者摘要中的
  random Hénon/spectral gap 是复相空间 mean stability 与 Hölder 转移算子结论，
  不是模素数三点置换链。
- [Oren Becker、Emmanuel Breuillard，arXiv:2512.15364](https://arxiv.org/abs/2512.15364)：
  2025 年作者摘要处理线性/半单代数群反集中；其中有限有界秩群、几乎所有素数
  的扩张被列为续作方向，不能读作当前二维非线性、所有大素数目标的现成定理。

置换多项式的生成性、差分谱、群像为 Alt/Sym 等材料只解决不同问题；
本次不从这些事实推导统一 gap，也不因为词中有 polynomial 就套用线性群超逼近。

## 7. 检索范围与剩余不确定性

全文读取 `research-lit` 和 `novelty-check` 技能，采用四个断言：固定生成集三点 gap、
仿射工具、非线性轨道间混合、两尺度方法。分别用 Hénon/有限域、polynomial
permutations、k-tuples/Schreier、affine groups、nonlinear expanders、Feistel、
Markov decomposition 等不同表述检索，并加入 2024–2026 及最近 180 天限定。
搜索引擎可能返回旧论文的新抓取页，发表/版本时间按作者或出版页核对。

本地仅按相关文件名定向检索；没有发现匹配的本地外部文献，`literature/`、
`tools/` 不存在，未扫旧构建树。没有找到可用的指定 arXiv 抓取脚本，故使用
直接 arXiv 页面与公开在线 PDF 回退。Zotero/Obsidian 及指定 Codex reviewer
接口不可用；没有虚构调用。技能建议的 ML 会议表和评分按本任务明确范围跳过。

未找到直接覆盖的置信度仅为中等：有限域非线性置换、显式交错群生成集和
伪随机置换构造之间仍可能有未命中的专门结论。尤其如果存在统一有界词模拟桥，
上述 `NOT_DIRECT_COVER` 需要随新证据修订；本报告既未证明也未排除这种桥。

本轮没有声称目标定理成立，没有查看主控尚在推导的证明，不授予科学或候选 PASS。
没有实验、PDF 本地下载、外部写入、额外代理或新项目；只新增本报告。
到此结束有界查新，不增加八项清单，也不继续生成研究后备。
