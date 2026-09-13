# Paper30：首三内部 forcing 算术结构的有界查新

日期／最后检索：2026-09-08。作者：主控，合并独立只读检索代理的来源核对。
使用 `novelty-check` 与 ARS `three-way-scan`：先按主张检索，再按 WHY／HOW／WHAT 对照一手来源。
这是查新预核，不是正式候选四门评价、正文容量结论或论文立项。

## 1. 结论与三个待评价主张

结论：`NO_DIRECT_MATCH_IN_READ_SCOPE; GLOBAL_NOVELTY_UNCERTAIN`。
建议：`PROCEED_WITH_CAUTION`，进入已闭合定理包的去重价值判断，不立即成稿。
本次未找到直接给出同一加权双谐波、素数幂内部 forcing 算术结构的一手先例；
“未找到”不是世界范围的不存在证明，也不是新意 PASS。

本轮科学输入是[已接受完整结构](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_COMPLETE_STRUCTURE_DISPOSITION_20260908.md)，
不是原来尚未解决的全分母实根猜想。对所有 $p\ge5,a\ge2$，
$m=(p-1)/2$、$M=p^{a-1}m$、$D=3m+1$，研究固定
$V_{\epsilon,\lambda}=\epsilon\cos q+\lambda\epsilon^2\cos2q$ 的实际 SUM/Lindstedt 内部项。

| 核心主张 | 潜在新意（暂定、非正式票） | 最强已知扣除及剩余差距 |
| --- | --- | --- |
| C1：第三内部项的准确图 $(0,m-1)\to(m,0)\to(D,M-m)$，不可约因子次数 $m,p$，正簇驯分歧／负单根域野分歧 | MEDIUM | Newton 边到不可约性和分歧指标是标准；新增只能是实际递推的精确边高度、不同根簇及规范化常数，不能声称新的一般 Newton 方法。 |
| C2：完整实际最高端点的首次非零剩余 $\overline{h^{-p}p[L^D]\mathcal B_3}=-3/16$ | MEDIUM | Fourier 递推、树和、零动量消去及加权共振正规形均有先例；本轮差距是统一素数参数下的有限参照首误差、二次响应与真实同阶污染的合并计算。 |
| C3：首三个实际内部 forcing 两两互素，特别是同次数的第二项与负因子首常比不同 | MEDIUM | “首项消失后继续递推”不是新概念；新的内容只能是具体三项的公共零点排除，不等于所有内部层或最终周期 forcing 均已分类。 |

上述暂定等级仅描述候选发现相对于本次已读来源的差距；没有给出正式数值新意票。
C3 依赖 C1/C2 等输入，不应包装成另一套独立方法或另拆一篇。
证明较长不能自行证明研究价值；尚需判断该内部算术对象是否形成独立、非例行的数学问题。

## 2. WHY／HOW／WHAT 对照及实际阅读范围

| 一手来源 | WHY：问题 | HOW：方法 | WHAT：已给结果与本题区别；实际阅读 |
| --- | --- | --- | --- |
| Berretti–Gentile (2000), *Scaling properties for the radius of convergence of Lindstedt series: generalized standard maps*, JMPA 79(7),691–713；DOI `10.1016/S0021-7824(00)00167-7` | 广义 standard map 在有理旋转数附近的共轭收敛半径缩放 | Fourier–Taylor 递推、树展开、零动量共振消去、最小树系数 | 本轮代理重读保留的[官方作者TeX](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.tex.gz) §1–4、§6关键定义；主控沿用此前已亲读段落并复核[机构书目](https://iris.uniroma3.it/handle/11590/143062)。固定 $f$、普通节点阶与复旋转数极限不是本题完整内部算术结构。出版社定稿未逐项核验。 |
| Berretti–Gentile (2001), *Non-universal behaviour of scaling properties for generalized semistandard and standard maps*, Nonlinearity 14(5),1029–1039；DOI `10.1088/0951-7715/14/5/307` | 支撑如何改变缩放指数与非普适性 | 正 Fourier 支撑、同相位树值及 Diophantine 最小阶 | [作者公开版](https://ipparco.roma1.infn.it/pagine/deposito/2000/bg4.ps.gz)摘要、§1、§4式(4.5)、§5由代理定点重读；主控此前亲读§1–5，本轮重核[机构书目](https://iris.uniroma3.it/handle/11590/139305)。同号无抵消下界不覆盖任意参数的本题系数两条边。 |
| Olvera (2001), *Estimation of the Amplitude of Resonance in the General Standard Map*, Experimental Mathematics 10(3),401–418；DOI `10.1080/10586458.2001.10504459` | 估计一般 Fourier 扰动的共振幅度与塌缩 | 可带不同 $\epsilon$ 权重的同调递推、共振正规形、组合首出现阶与渐近直线比较 | [作者上传的原刊扫描/OCR](https://www.researchgate.net/publication/38338476_Estimation_of_the_Amplitude_of_Resonance_in_the_General_Standard_Map)：代理读§2 pp403–405、§3 p406、§6 pp411–412；主控读摘要及§2–3交界相关段落。明确允许首共振系数消失后继续；复杂公式OCR损坏，未逐式核验。未在这些段落见 C1–C3。 |
| Djakov–Mityagin (2005预印), *Asymptotics of instability zones of the Hill operator with a two term potential*, arXiv:math-ph/0509034 | 双谐波线性 Hill 算子的谱隙渐近 | Fourier正路径、指数规范变换和谱重数 | 主控此前亲读[作者HTML §3–4](https://arxiv.org/html/math-ph/0509034#S3)，本轮复核[官方摘要](https://arxiv.org/abs/math-ph/0509034)。已有全阶小振幅首系数乘积；传播子为 $n^2-j^2$，不是本题非线性指数递推。未建立保参数根的对象身份。 |
| Guàrdia–Montes–Nart (2012；预印2008), *Newton polygons of higher order in algebraic number theory*, Trans. AMS 364(1),361–416；DOI `10.1090/S0002-9947-2011-05442-5` | 在局部域分解多项式并计算算术指标 | Newton多边形、剩余多项式和高阶分解 | 主控亲读[作者HTML](https://arxiv.org/html/0807.2620v2)引言、§1.3–1.4，特别Theorem1.15、Corollary1.16及其证明；[机构元数据](https://upcommons.upc.edu/handle/2117/14810)核期刊年与DOI。互素长高单边带来的不可约／分歧推论必须扣除，真正输入仍需本题系数计算。 |
| Mugnaine等 (2025), *Isochronous islands in the two-harmonic standard map*；DOI `10.1140/epjs/s11734-025-01867-7` | 同频多岛链如何随两个模式竞争出现 | 固定点与相图分岔分析 | 代理完整读[arXiv HTML §1–4](https://arxiv.org/html/2504.20177v1)；主控核[作者原刊版](https://web.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Mugnaine%20EPJST%202025.pdf)首页与§2模型。模型及一般岛链竞争已知，不是内部forcing的算术因子定理。 |
| Mugnaine等 (2025), *Dependence of isochronous bifurcations on the driving-mode phase shift in two-harmonic standard maps*, PRE112,034216；DOI `10.1103/6v36-6h3s` | 非零相移怎样改变竞争、固定点与shearless曲线 | period-one方程、稳定性及分岔图 | 代理读[arXiv HTML](https://arxiv.org/html/2505.00179v1)§I–III、V–VI及附录；主控读[作者原刊版](https://portal.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Mugnaine%20PRE%202025.pdf)首页、引言和§II模型。mode整数不是轨道分母；不据其分岔表排除或证明 C1–C3。 |
| Leal等 (2025), *Secondary shearless bifurcations for two isochronous resonant perturbations*, Chaos35,043136；DOI `10.1063/5.0233732` | twist系统内局部shearless曲线的生成 | 比较双谐波map、Ullmann map与Walker–Ford流的局部分岔 | 主控和代理读[作者原刊版](https://web.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Leal%20Chaos%20PDF%202025.pdf)首页、引言和§II式(1)及附近段落。明确 $m_1=1,m_2=2$ 为extended standard map；未在所读部分见内部算术结论，不冒称全文排除。 |

以上8项中7项有经核书目的期刊发表记录，但实际阅读版本和证明／数值／经验猜想性质分别如表。
这是理论数学的对象与定理适配检查，不用临床证据等级评判数学证明。
来源集中于英文数学物理论文；五项经典文献超过五年，因其确属方法近邻而保留。
该语言、主题与经典来源集中限制了覆盖面，不以“较老”否定仍适用的数学先例。
没有生成系统综述式PRISMA总量、撤稿核验结果或人工阅读认证。

额外定位但不作为核心排除依据的两项：

- Berretti–Marmi, *Scaling near resonances and complex rotation numbers for the standard map*, Nonlinearity7 (1994),603–621，DOI `10.1088/0951-7715/7/2/014`；代理仅读[机构摘要](https://ricerca.sns.it/handle/11384/4178)及[作者PDF首页抽取](https://homepage.sns.it/marmi/papers/Berretti_Marmi_nonlinearity_94.pdf)，不据摘要排除正文其他结果。
- Mugnaine等, *Isochronous bifurcations in a two-parameter twist map*, PRE110 (2024),024206，DOI `10.1103/PhysRevE.110.024206`；代理仅读[机构原刊PDF](https://repositorio.usp.br/directbitstream/74206ab1-9134-415d-a5fa-371f3704b853/PhysRevE.110.024206.pdf)搜索抽取的摘要及§II式(1)，用于确认模型背景，不声称全文核验。

## 3. 必须扣除什么，尚有何种可能贡献

共同 WHY 是理解共振／小除数／多项式结构；既有 HOW 已涵盖通用递推、树和、
加权正规形、同号无抵消和局部 Newton 工具。最强相邻 WHAT 分属共振幅度、
收敛半径、线性谱隙乘积、局部分岔与一般局部域分解。

Olvera 的加权 Fourier 设置比“BG固定 $f$ 与本题加权 $f$ 不同”更近。
因此不能仅靠不同 $\epsilon$ 权重、首项消失后的继续计算来宣称新意。
同样，现成 Newton 理论并不直接算出本题消去后的实际高度；
它扣除的是从准确边到因子和分歧的通用推理，不抹掉待评价的系数定理。

本轮潜在发现是：同一个实际内部递推在所有允许素数幂下，
呈现可准确描述的正／负赋值簇、驯／野单根域差别，并阻止首三内部项共享参数根。
“算术结果已证明”“与所读先例有差距”“足够构成独立论文”必须分开。
本轮没有证明它自动控制最终 $C_{r,p^a},Q$ 或实周期轨道的完整分裂机制。
与旧 Hill、Suris 或异宿作用差的精确桥接仍未建立，不拼接那些构造的最好结果。

## 4. 检索范围、时效与工具限制

主控执行24条公开网页查询及1条Consensus检索；独立代理另执行36条网页查询。
下节保存主控完整查询与代理完整查询，打开准确链接、文内查找及本地原文读取另计。
每个 C1–C3 均有至少三种措辞；另查2024–2026及最近六个月
2026-03-08至2026-09-08的arXiv相关记录。没有将不相关的ML会议当作本数学问题的必要语料。

Scholar和Semantic Scholar完成的是入口／域名索引查询，不是完整数据库导出。
代理访问Scholar遇验证码、S2论文入口抓取失败；不尝试绕过。
Consensus给出GMN等候选书目，主控对采用的GMN先fetch记录再回到官方原文。
其2008预印年份没有误记为2012期刊年份；未采用其自动结论或订阅推销作为证据。

最近窗口没有找到直接相关的新发论文；这不保证该窗口不存在漏检文献。
Mugnaine两篇arXiv首发分别为2025-04-28与2025-04-30；对应期刊发表为2025-08-26、
2025-09-26。Leal原刊首页注明2025-04-18。
2505.00179的HTML页眉出现2026日期，但官方提交历史仅列2025年v1，故不计作最近新发／修订。
抓取日期、机器评论和搜索引擎的“几个月前”不替代原刊或官方提交日期。

BG出版社定稿未逐项核验，公开版差异保留；本轮Gentile站证书／超时问题未通过关闭验证处理，
使用先前正常取得的官方公开源做定点阅读。Olvera内容取自作者上传扫描，OCR公式限制保留。
GMN机构PDF入口403即停止该入口，正常使用另有公开的官方arXiv HTML；没有绕过访问控制。
没有完整前向／后向引文穷举，没有查到的词组不能支持世界范围排除。

`novelty-check` 指定的GPT-5.4 Codex MCP接口当前未配置，未调用或冒称跨模型验证。
本轮只读代理检索不是该阶段的替代完成；另行的同模型独立主张边界复核也只记其真实范围。
所有查询使用公开主题词，没有上传本地未发表稿、发信、付费或创建外部项目。

## 5. 可复查查询日志

主控网页查询（24条）：

```text
01 "Lindstedt" "Newton polygon"
02 "standard map" "p-adic" resonance
03 "Lindstedt" cyclotomic "prime"
04 "standard map" cyclotomic resonance polynomial
05 "Lindstedt series" "p-adic"
06 "resonance polynomial" irreducible "prime" 2024 2025 2026
07 "Lindstedt series" resonance cancellation "prime power"
08 "standard map" "harmonic sums" resonance
09 "double harmonic" "standard map" Chebyshev 2024 2025 2026
10 "generalized standard map" "common zeros"
11 "Lindstedt" "coprime" resonance
12 "two-harmonic" resonance polynomial cancellation 2024 2025 2026
13 site:arxiv.org "Lindstedt" "resonance" after:2026-03-08
14 site:arxiv.org "standard map" "prime powers"
15 site:scholar.google.com "Lindstedt" "polynomial"
16 site:semanticscholar.org "Lindstedt" "resonance"
17 "Newton polygons of higher order in algebraic number theory" Guardia Montes Nart
18 "Lindstedt" "prime" "resonances"
19 "standard map" resonance polynomial factorization
20 "Lindstedt" "p-adic" 2024 2025 2026 [domains:arxiv.org,semanticscholar.org]
21 "standard map" "Newton polygon" 2024 2025 2026 [same domains]
22 "resonance" "Lindstedt" "coprime" after:2026-03-08 [domain:arxiv.org]
23 "Dependence of isochronous bifurcations" "034216" doi
24 "Non-universal behaviour of scaling properties" "10.1088"
```

Consensus查询：`Lindstedt standard map resonance cyclotomic polynomial p-adic factorization`。
多数精确算术组合没有直接命中，宽查询出现无关同名“standard map”；没有引用这些噪声条目。

独立代理查询（36条；15、25另设recency184天）：

```text
01 Berretti Gentile generalized standard map Lindstedt resonance 2000 2001
02 Arturo Olvera Estimation Amplitude Resonance General Standard Map 2001
03 site:arxiv.org "two-harmonic standard map" 2024 2025 2026
04 "Berretti" "Gentile" "Non-universal" standard maps
05 "Scaling properties" "generalized standard maps" 2000 pdf
06 "Estimation of the Amplitude of Resonance" pdf Olvera
07 "two-harmonic standard map" 2026 after:2026-03-08 before:2026-09-09
08 site:scholar.google.com "standard map" "Lindstedt" resonance
09 site:semanticscholar.org "two-harmonic standard map"
10 "Estimation of the amplitude of resonance" euclid
11 "Estimation" "Olvera" "1069786347" pdf
12 "Berretti" "Gentile" "generalized standard maps" "cancellation"
13 "Non-universal behaviour" "semistandard" pdf -site:researchgate.net
14 "standard map" Lindstedt cyclotomic Newton polygon factorization
15 site:arxiv.org ("two-harmonic" OR "double harmonic") "standard" 2026
16 "two-harmonic standard map" 2024 2025 2026 cyclotomic
17 "Lindstedt" "prime power" forcing
18 "standard map" "resonance polynomial" arithmetic
19 "Arturo Olvera" "amplitude" "pdf" standard
20 "generalized standard maps" "Lindstedt" "beg" pdf
21 "standard map" "Lindstedt" "coprime"
22 "Lindstedt" "cyclotomic"
23 "Estimation of the Amplitude of Resonance" "6." collapse
24 "Scaling properties" "generalized standard maps" pdf Gentile 691 713
25 "two harmonic" "standard map" "2026" Lindstedt
26 "Scaling properties for the radius of convergence of Lindstedt series" "resonances" "generalized" "pdf"
27 "Dependence of isochronous bifurcations" "10.1103"
28 site:mat.uniroma3.it/users/gentile/ricerca/lavori/ "generalized standard maps" "cancellations"
29 "two-harmonic standard map" "Newton polygon"
30 "Scaling near resonances" "standard map" Marmi Berretti 1994 doi
31 "Non-universal behaviour" "Berretti" "Gentile" "mp_arc"
32 "Lindstedt" "cyclotomic" "forcing"
33 "standard map" "p-adic" factorization
34 site:arxiv.org "Lindstedt" "two-harmonic" after:2026-03-08 before:2026-09-09
35 site:semanticscholar.org "generalized standard maps" Lindstedt
36 site:scholar.google.com "two-harmonic standard map" 2026
```

## 6. 接续

下一项是对这个已闭合内部算术定理包作独立的去重与研究价值判断，
明确它相对于旧论文及上述先例的非例行内容；不要自动把原全分母实根目标缩写成已解。
若它有独立论文价值，再按现有顺序进行作者自然容量预筛、双独立候选评价与立项；
不以本预核跳过任何已锁门槛，不继承Paper29的特殊测页许可。
若价值不足，继续族内真正缺口，而非增加背景或拆分短推论凑篇。
当前仍未估页、未成稿，Batch07本地完成3/5。
