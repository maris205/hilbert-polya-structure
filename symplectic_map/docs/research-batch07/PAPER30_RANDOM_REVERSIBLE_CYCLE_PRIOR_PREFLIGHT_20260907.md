# Paper30 随机可逆周期统计：一手先例预检

日期：2026-09-07。状态：`BOUNDED_PRIOR_PREFLIGHT_COMPLETE`。
输入：[八题组合 V2 §2 N1](PAPER30_NONCOHOMOLOGICAL_PORTFOLIO_V2_20260907.md)。
本件只记录有界查新与适用性判断；不授予正式新意 PASS、数学 PASS 或容量票，
不创建 Paper30 项目，不改变批次/state。数学作者正在另行检验的结论不是本件的证明结果。

## 1. 结论

**通用可逆组合统计已强匹配；指定随机多项式系综尚未直接匹配。**
不能把“可逆周期不是普通随机置换周期”“对称轨道与非对称轨道对分别出现
Poisson 分量”或固定有限多个周期的常规联合推广当作新的统计机制。
最强一手来源是 Roberts–Vivaldi (2009) 和 Lugo (2009)。后者准确给出
固定单周期的复合律，并已有足以直接推出固定有限维联合律的生成函数方法。

在本次八条查询及所读一手全文中，**没有找到**同时满足下列条件的现成定理：
奇素数 p；均匀抽取一次单首次数 d(p) 的 P；d→∞ 且 d<p；之后始终迭代
同一张 H_P；联合统计全部 n≤L(p) 的 R-对称轨道及非对称轨道对；有显式
增长窗口全变差误差。这里 `NO_MATCHED_SOURCE_IN_BOUNDED_SEARCH` 只描述查得证据，
不是全球不存在或新颖性通过。

另有必须保留的引用风险：Roberts–Vivaldi Theorem B 的总周期措辞与其证明中
只计对称周期的步骤，在固定小周期尺度不能不经检查地互换。Lugo 的复合律
正说明非对称轨道对在这一尺度不可删除。

## 2. 来源与精确覆盖

| 一手来源 | 实际核读与定位 | 核心内容 | 对 N1 的匹配状态 |
| --- | --- | --- | --- |
| J. A. G. Roberts, F. Vivaldi, *Signature of time-reversal symmetry in polynomial automorphisms over finite fields*, Nonlinearity **18** (2005), 2171–2192 | [作者保存的正式版](https://web.maths.unsw.edu.au/~jagr/RV05p.pdf)，pp.2174–2176 Proposition 1/Corollary 1；p.2179 Conjecture 1；§3 | 对称/非对称周期分类与固定集计数恒等式；有限域多项式自同构的普适尺度分布是猜想/数值证据 | `MATCHED_BASELINE`；不是随机系数 P 的联合极限定理 |
| J. A. G. Roberts, F. Vivaldi, *A combinatorial model for reversible rational maps over finite fields*, Nonlinearity **22** (2009), 1965–1982, DOI 10.1088/0951-7715/22/8/011 | [正式版作者全文](https://web.maths.unsw.edu.au/~jagr/RV09.pdf)，pp.1967–1968 Theorems A/B；§2；pp.1974–1978 §3；[arXiv metadata](https://arxiv.org/abs/0905.4135) | 固定两对合的固定点数量，对所有此类对合对均匀抽样；宏观周期分布及重复周期统计 | `MATCHED_GENERIC_MODEL`；Theorem B 的固定周期总数解释有下述风险；不覆盖 P 系综 |
| Michael Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604v1 (2009), 17 pp.，本次未核得期刊发表信息 | [官方 HTML](https://arxiv.org/html/0911.3604v1)，§§4–6；[PDF 在线页码](https://arxiv.org/pdf/0911.3604)，pp.5–7 图分解、pp.7–8 Theorem 5.1/Lemma 5.2，pp.8–9 Propositions 6.1/6.2、Corollary 6.4 | 无固定点数条件的均匀随机对合乘积：固定 k 周期数趋于 A_k+2B_k，A_k、B_k 独立，均值分别 1、1/(2k)；另给指定固定点数的图分量一阶精确计数及平方根尺度均值 | `MATCHED_FIXED_PERIOD_MECHANISM`；固定有限维联合是其方法的直接推论，非原文明确列出的联合定理；未查得增长维数 TV |
| Michael T. Lugo, *Profiles of Large Combinatorial Structures*, University of Pennsylvania PhD thesis (2010) | [作者导师主页全文](https://www2.math.upenn.edu/~pemantle/papers/Student-theses/Lugo100407.pdf)，印刷 pp.149–153（PDF pp.161–165），§§5.3–5.4 | Theorem 5.3.1 及证明重现上述复合律；后续指定固定点数计数 | `DUPLICATE_SUPPORT`；不是另一条新增突破 |
| Charles Burnette, *Involution factorizations of Ewens random permutations*, DMTCS **27:2** (2025), DOI 10.46298/dmtcs.11602 | [正式期刊 metadata/摘要](https://dmtcs.episciences.org/16385)，只做主题排除，未冒称阅读全文 | 对 Ewens 随机置换，研究其可写成两个对合乘积的**分解方式数量**之对数正态律和速率 | `NO_MATCHED_TARGET_STATISTIC`；随机测度与待统计对象均不同 |

没有采用搜索引擎将旧作者 PDF 标为“几个月前”的抓取日期作为论文发表年份。
Lugo 博士论文是同一作者结果的补充定位，不与 2009 预印本重复计算先例数量。

## 3. 两个随机集合不能因固定点数量相同而认同

下面是本次对目标对象的直接代数核对，不是上述论文的随机多项式定理。
令

\[
T_P=R\circ H_P:(x,y)\mapsto(x,P(x)-y),\qquad H_P=R\circ T_P.
\]

R、T_P 均为对合，且奇特征下各有 p 个固定点：R 的固定集为对角线，
T_P 的固定集为图 y=P(x)/2。相空间大小 N=p²。所以形式参数确为 g=h=p=√N。

但 Roberts–Vivaldi 的随机空间是
\(\mathcal I(N,g)\times\mathcal I(N,h)\) 上的均匀测度；每个分量包含所有对应
固定点数的对合。Lugo Theorem 5.1 则在所有对合上均匀抽样，不先固定 g,h。
本题只有 p^d 张不同的 T_P，且每张都保留第一坐标、逐竖纤维作斜率 −1 的仿射反射。
多项式取值之间还受次数限制。它不是全体有 p 个固定点对合的均匀子样本。

真正缺口也**不只是“本题仅随机一个对合”**：对共轭不变量，通用随机对合模型
可以将一个对合固定为其共轭类代表，再让另一个在整个共轭类均匀变化。
不能消除的是 T_P 的纤维结构及单个函数 P 的复用。把全部函数 P 取为独立均匀值
仍只得到纤维反射子系综；有限次数插值只是进一步限制，不能自动完成通用模型转移。

因此 N1 若最后证明得到通用均值主体，新增工作的位置是**结构化随机系综中的实现与
误差控制**。主控转告的 n=1,2 例外（B₁=B₂=0，S₂ 的候选均值为 1/2）应单独核证，
不能归因于 Lugo 定理；本预检不以该转告替代证明，也不将两个低周期例外计作新机制。

## 4. 固定周期、平方根尺度与全变差须分开

### 4.1 宏观长度分布不是固定周期数分布

Roberts–Vivaldi Theorem A 在 g+h→∞、(g+h)/N→0 下，对**平均点占比**给出
尺度 z=2N/(g+h) 的分布 \(1-e^{-x}(1+x)\)。本题形式参数代入后 z=p=√N。
其 Theorem B 用
\(f=gh/N\)（奇周期）或 \((g²+h²)/(2N)\)（偶周期），区分固定 t 与固定
\(y=(t-1)(g+h)/(2N)-\log f\)；所以不能把这篇说成“仅有增长周期、没有固定周期讨论”。
也不能把一个周期 t≈p 的边缘结论称为 n≤L(p) 的增长维数联合 TV。
定位：[正式版 pp.1967–1968](https://web.maths.unsw.edu.au/~jagr/RV09.pdf)。

### 4.2 Lugo 固定有限维联合属于直接标准延伸

原文 Theorem 5.1 明述固定单 k；本次检查全文没有找到明确列出的 joint 或
total-variation 定理。以下是**本次从其图分解与系数慢变推出的直接推论**，不是
将其原文换名：设通用模型的 k-路径数为 A_k、2k-图圈数为 B_k，则固定 L 的多标记函数为

\[
Q(z)\exp\!\left\{\sum_{k=1}^{L}
  \left[(u_k-1)z^k+(v_k-1)\frac{z^{2k}}{2k}\right]\right\},
\quad Q(z)=\frac{e^{z/(1-z)}}{\sqrt{1-z^2}}.
\]

任意固定混合阶乘矩只将 [z^N]Q(z) 改为有限个固定移位的系数之和；
\([z^{N-j}]Q/[z^N]Q\to1\) 给出分解矩。因此固定有限多个 A_k、B_k 联合趋于
互相独立的 Poisson 分量，均值 1、1/(2k)。这一步沿用已有证明结构即可，不能因
原文定理只写单 k 就计为实质新意。依据：[Lugo §§4–5](https://arxiv.org/html/0911.3604v1#S4)。

但上述固定移位 argument 没有自动提供 L、矩阶都增长时的一致界，也没有处理
P 系综的坐标重复、有限域秩、受限插值。本次没有把这些尚需估计的部分宣称成现成结论。

### 4.3 已有增长尺度覆盖到哪里

Lugo §6 的 Corollary 6.4 已取 r=O(√N)、两个对合各有 √N 固定点：
r-路径平均数渐近 e^{-r/√N}，偶 r 的图圈平均数渐近 e^{-r/√N}/r。
其中图圈长度 r=2n 才对应一对 n-周期。它是**一阶期望**，不是增长窗口联合 TV。
因此“允许周期增长”本身不够新；反之，不能用它直接否决指定 P 系综的 TV 命题。
定位：[Lugo §6，PDF p.9](https://arxiv.org/html/0911.3604v1#S6)。

## 5. Roberts–Vivaldi Theorem B 的固定小周期引用警告

正式版 p.1975 的证明以 μ(t,i) 计总 t-周期，随后借 Theorem 7 转为只计对称周期。
Theorem 7 控制的是所有非对称周期占据的**相空间比例**。这不蕴含固定 t 的
非对称轨道对消失；后者只占 O(1/N) 的点比例，却可能有非零计数极限。

该区别可由文章自身公式 (33) 作有限计算核对：将其非对称点比例乘以 N/(2t)，
得到通用模型 \(\mathbb E B_t\to1/(2t)\)（固定 t，g=h=√N）。
这个一阶事实本身不是完整分布反证，但已经不能支持“丢掉 B_t 不影响 fixed-t
统计”的论证。Lugo 在另一种、未固定 g,h 的均匀对合模型中给出的
\(A_t+2B_t\) 则是明确的分布级警示。

故本件只将 RV Theorem B 记为**强先例但固定周期总数解释须审查**，
不直接引用为 N1 总周期或联合 Poisson 定理，不据此否定该文宏观尺度 Theorem A，
也不把这项引用审慎包装成项目的新定理。
定位：[RV 正式版 p.1974 式 (33)、p.1975 证明首段](https://web.maths.unsw.edu.au/~jagr/RV09.pdf)。

## 6. 有界搜索记录与未关闭边界

使用 research-lit 技能，先检本地相关题名；本地库未发现随机对合/该随机系综的
对应外部论文。没有配置可调用 Zotero/Obsidian 搜索；未找到技能指定位置的
arxiv_fetch.py，因此使用官方 arXiv metadata 搜索/读取回退。
八条查询已用完；arXiv PDF 只在线核页码，**没有下载到本地**。

1. `Roberts Vivaldi random involutions reversible maps cycle statistics finite fields period distribution`
2. `"random" "Hénon" "finite fields" cycles distribution`
3. `site:arxiv.org Roberts Vivaldi reversible maps random involutions`
4. `"A combinatorial model for reversible rational maps over finite fields" Roberts Vivaldi 2009`
5. `"random" "polynomial" "Hénon" "cycles" "finite"`
6. `"random involutions" "joint" "cycles" Poisson`
7. `"Hénon" "finite fields" "distribution" random polynomial`
8. `Lugo composition random involutions cycle counts Poisson 2009`

官方 HTML 精读范围为 Lugo §§4–6 的完整相关陈述和证明；RV2009 的 Theorems A/B、
§2 计数公式、§3 证明及 pp.1978–1979 的固定次数/Galois 警告；RV2005 的
Proposition 1、Corollary 1 和 §3 对应猜想/证据。RV2009 本身已提醒：固定代数映射
及固定周期的根数有界，不能直接得到无界支持的 Poisson 极限；本题 d→∞ 正是在改变
这个量词，但并非文献空白的证明。

另发现 de Faria–Hutz 的 Wehler K3 后续文献
（[arXiv:1309.6598 metadata](https://arxiv.org/abs/1309.6598)），属于不同代数空间，
本次未阅读全文，不能借其摘要扩大 RV 定理适用性。尚未穷尽密码学中同函数复用
Feistel 型置换的别名文献；仅记检索边界，不继续扩展本次八-query 预算。

**交给主控的扣除项：**通用反射/路径/图圈分类、固定周期复合 Poisson、固定有限维
多标记阶乘矩推广、平方根尺度一阶均值均已存在或为其直接标准推论。
剩余仅能按实际证明评价：P 系综的真实零秩碰撞机制、增长窗口一致误差是否有
非例行内容。没有直接检得相同命题，并不足以自动保留 N1 为长篇候选。
