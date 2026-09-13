# Paper31：原实旋转数／twist 强来源审计 V1

日期：2026-09-12 UTC；执行者：/root/p31_real_twist_primary_sources。
状态：BOUNDED_SOURCE_AUDIT_TERMINAL / STRONG_TEXT_GAPS_REMAIN / NO_NOVELTY_SCORE。
归属：只写本文件；不修改 BATCH、README、候选、证明稿、锁或论文项目。

## 1. 结论与权限边界

本轮完成约定上限 16 条公开查询，并终止检索；没有找到可实际阅读全文的 Beukers–Cushman 合法入口。
其机构 PDF 与尝试的出版社文章入口本次均明确返回 403，未重试或绕过这些入口。
Duistermaat 原书的机构三页目录已 FULL 读取，相关章节和页码现在可精确定位；其定理正文仍未取得。
因此两项强来源缺口没有闭合，不能将访问失败、目录或他文转述变成“已排除包含关系”。
固定 T 不是固定 Lyness 参数 a，只能说明不能直接按该参数线套用，不能据此给原全局 twist 新意。
既不授 Q4 候选 PASS，也不判断原问题已被全部覆盖；无正式查新分数、容量票或四门票。
本地批次仍为 4/5，Paper31 未准入、未建项目；这些状态来自本轮实际读取的 BATCH 入口。

本人完整读取 research-lit/SKILL.md 后执行有界来源核对；未调用 ARS，故不声称其完整 fact-check 流程。
无 Zotero／Obsidian 工具元数据命中。定向本地文件查询未找到相关名称 PDF 或 arxiv_fetch.py。
该查询中的 literature/、tools/ 与 /root/autodl-tmp/.claude/skills/arxiv 路径不存在，记录为路径不存在而非权限错误。
使用公开浏览降级；任务禁止 API／resolver，本轮不另配 API，也不把公开站点定向搜索称作数据库原生检索。
ARXIV_DOWNLOAD=false；没有本地 PDF 下载、数学软件、CAS、参数采样、再委派、凭据提取、上传、发信或付费操作。

## 2. 输入实际读取范围

FULL：[原范围件](PAPER31_QPI_POST_EXACT_SOURCE_AND_SCOPE_V1_20260912.md)，全部 179 行。
PARTIAL：BATCH_07_CONTEXT.md 第 1–18 行，确认最新 b 机制处置和保留 Q4；没有加载整份历史账本。
接受原范围件作为任务输入，不冒充其旧来源与证明已经由本席重新核准。
本席没有参与原实分支几何证明；主控并行承担该数学任务，本文不预判其结果。

原族和标记为

$$v^2+huv-Tv=u^3-Tu^2,\qquad T>0,\qquad R=(0,0).$$

GMX 的参数记作 b=T、c=1-h；为避免和原 h 混淆，将其能量记作 k：

$$a(h)=1+\frac1{1-h}-\frac{T}{(1-h)^2},\qquad k(h)=-\frac{T}{(1-h)^2}.$$

这是原范围件输入且本轮另由 GMX Theorem 3 的证明原式核对；不是新增正常形定理。
c=0（h=1）对应四阶标记缺图，必须在原族另作匹配，不能删除后再声称全局。
原 h 导数与固定 a 能量导数不同；在合法光滑旋转分支上，链式法则同时涉及参数和能量两个偏导。
这只是适用性警示，未假定两偏导已存在于所有分支，也没有据此证明任何导数符号。

## 3. Beukers–Cushman：已核元数据、未核主定理

来源：[机构正式文章记录](https://research-portal.uu.nl/en/publications/zeemans-monotonicity-conjecture/)，
F. Beukers、R. H. Cushman，*Zeeman's monotonicity conjecture*，Journal of Differential Equations 143 (1998), 191–200。
DOI 为 10.1006/jdeq.1997.3359；本轮在已发表 GMX 的出版社参考文献搜索呈现中交叉核到该 DOI。
正式记录的期号栏误样显示“1998”；本文不据该栏锁期号，出版社作者检索呈现为 143(1)、1998-02-10。
旧 repository 搜索记录标 1997 preprint；与正式 1998 发表年分别保留，不把搜索抓取新近日期当出版年。

实际读取：机构记录正文／书目；作者 [Publications 页](https://www.uu.nl/staff/FBeukers/Publications)中 1998 条目。
机构 PDF 的搜索呈现只显示摘要和 §1 首段（含映射、正象限、不变量），没有取得后面的完整主定理。
可从该有限原文明确识别映射为 (x,y)↦(y,(y+a)/x)，不变量为 (x+1)(y+1)(x+y+a)/(xy)。
其研究对象为第一象限中的保不变量动力；此范围信息不等于确认正文中没有其它实域延拓结果。

未核准的四项必须保留：

1. 完整主定理中 a 的精确量词及所有例外；不能用常见转述替代。
2. 能量区间和端点是否纳入，尤其负能量和其它实连通分支是否另有处理。
3. 作者选定的旋转方向、数值提升及导数符号约定；本文不抄二手正负号表。
4. Picard–Fuchs／Abelian 积分证明的边界项与正性条件；本席没有读到其原证明。

CGM 引言确实转述 BC 用时间／周期比和 Picard–Fuchs 技术证明单调性。
这一句在本文只作“CGM 对先例的归属说明”，不充当 BC 的完整原文、符号核准或全实域排除证据。

## 4. Duistermaat：强章节定位，而非正文接受

来源：[Utrecht 机构书目和摘要](https://research-portal.uu.nl/en/publications/discrete-integrable-systems-qrt-maps-and-elliptic-surfaces/)。
J. J. Duistermaat，*Discrete integrable systems: QRT maps and elliptic surfaces*，Springer，2010；
机构条目给 649 页、印刷 ISBN 978-1-4419-7116-6；任务指定书 DOI 为 10.1007/978-1-4419-7117-4。
本轮未取得出版社书页正文来重新核 DOI；不得把机构目录当完整电子书 source lock。

[ETH 图书馆保存的原目录](https://toc.library.ethz.ch/objects/pdf/e01_978-1-4419-7116-6_01.pdf)
实际浏览为 3 页、73 行，全部读取；第一页为书名，后两页为原目录。
下面终止页由目录中下一节起始页减一推定，不是逐页看过的内容范围。

| 精确位置 | 目录起始页／推定区间 | 对 Q4 的作用与阅读边界 |
|---|---|---|
| §2.6，实点 | 74／74–84 | 实点基础；仅目录，不授实分支结论 |
| §8.1，实结构与实自同构 | 377／377–383 | 实结构及自同构；仅目录 |
| §8.2，奇异纤维附近的实周期 | 384／384–390 | 端点周期渐近的强先例定位；未读正文 |
| §8.4，实旋转函数的奇性 | 395／395–399 | 旋转函数奇性；未读定理／证明 |
| §8.5，实曲线束 | 400／400–404 | 全局实 pencil；未读正文 |
| §11.4，Lyness 映射 | 518／518–545 | 最直接的实 Lyness 强覆盖检查位置；未读正文 |

搜索意外出现非作者托管的整书镜像摘要片段，提及所有奇异值间区间的旋转行为及 a 的分岔。
该镜像未打开、未下载，片段不作为已验证科学证据，不从中抄定理、结论或给包含性判定。
合法目录本身已经足以要求认真核 §8 和 §11.4；无须消费上述镜像才能承认此覆盖风险。
[Google Books 可打开的条目](https://books.google.com/books/about/Discrete_Integrable_Systems.html?id=PXi5zwEACAAJ)只有介绍／目录外元数据，没有取得相关章节预览。
其 ISBN 9780387566238、627 页与机构记录不一致，且“Other editions”链接混入 *Quantum Groups*。
故该 Google Books 条目不用于本书版本锁、页数锁或定理归属；不擅自修正原机构书目。

## 5. 本人补核的可读一手工具来源

| 来源与版本 | 本人实际读取 | 可消费的有限作用 |
|---|---|---|
| [CGM, arXiv:math/0702121v2](https://arxiv.org/pdf/math/0702121)，JDE 244 (2008), 630–648 | 摘要、§1 全部、Theorems 1–2 完整陈述；另读 §2 的 Lemma 5、Proposition 6、Proposition 8 及证明；非整篇 | 作者自身的可积映射／不变向量场回返接口已有先例，不供应原固定 T 的 twist 符号 |
| [GMX, arXiv:1004.5511v1](https://arxiv.org/pdf/1004.5511)，DCDS 32 (2012), 587–604 | 摘要、引言定向段和 Theorem 3；§2.1 全部、§2.2 Theorem 3 全证明；非整篇 | 带点椭圆曲线的 Lyness 正常形和群平移识别已经存在，不得以参数换算本身计新意 |

CGM Theorem 1 要求一个向量场轨道被 F 保持，圆周上才给时间／周期比；直线轨道得到的是平移。
其 Theorem 2 在有限连通分支条件下允许某个迭代 F^m；不能把 F^m 的旋转直接当作 F 的旋转。
上述为本轮实际主陈述核对；Theorems 1–2 的完整证明未重新阅读，本文不报“全证明复核”。
CGM PDF 边栏标 arXiv v2、2007-02-05，正文首页另印 2018-11-03；两个日期如实并列，不归为 2026 新文。
GMX Theorem 3 在特征不为 2、3 的域上给阶至少 5（含无穷阶）标记的正常形。
其 §2.2 明写 k=−b/c²、a=(c²+c−b)/c² 和 c=0 四阶边界，支持本件的原路径换算。
其正象限能量描述与 k<0 不直接吻合，但该正常形定理本身并非只限正象限。
因此“负能量”不能被说成未见过 Lyness 或模椭圆曲线文献；本轮没有得到负能量 twist 分类先例的完整新正文。

## 6. 本轮 16 条实际公开检索账本

每条均实际调用；无关、空呈现和重复命中保留，不报去重文献数或数据库精确命中数。
基础先例不限制年份；Q12、Q15 含 2024–2026；Q13、Q16 指定 2026-03-12 至 2026-09-12。
站点定向结果仍是公开 web 索引，不是已成功进入 Scholar／Semantic Scholar 原生数据库。

1. "Beukers" "Cushman" "Zeeman" pdf
2. "Duistermaat" "Discrete integrable systems" "rotation" preview
3. "Lyness" "negative" "rotation number"
4. "Zeeman’s monotonicity conjecture" Beukers Utrecht filetype:pdf -site:dspace.library.uu.nl -site:researchgate.net -site:eurekamag.com
5. "Discrete integrable systems" "11.4" Springer
6. "Discrete integrable systems" "Front Matter" "7117"
7. "Duistermaat" "rotation function" Lyness
8. "Zeeman" "rotnum" Beukers
9. "Zeeman" "Beukers" site:webspace.science.uu.nl
10. "9781441971174" preview introduction Lyness
11. "Beukers Cushman" "monotonicity" pdf -site:researchgate.net -site:nzdr.ru -site:citeseerx.ist.psu.edu -site:dspace.library.uu.nl
12. Lyness rotation number negative energy variable parameter 2024 2025 2026
13. site:arxiv.org Lyness "rotation" after:2026-03-12 before:2026-09-13
14. "Discrete integrable systems" Duistermaat preview site:books.google.com
15. site:scholar.google.com Lyness "rotation" "negative" 2024 2025 2026
16. site:semanticscholar.org Lyness "rotation" "negative" after:2026-03-12 before:2026-09-13

Q8–Q10 同次调用给 Empty search results；不据此声称这些文献或作者网页不存在。
近期／negative 查询混入不相干医疗“rotation”、老文新抓取记录；没有消费为负能量新定理。
Q13 返回旧 GMX 等，不是 2026 新文；日期关键词／索引过滤并不保证返回结果都符合时间窗。
本轮没有找到可读的 2024–2026 原固定 T twist 定理；这只描述此次检索输出，不构成无先例证明。
两周期、三阶 Lyness 或其它 QRT 族若出现，最多列 ROUND2_CLUE；本轮不改变族或启动这些项目。

## 7. 访问失败的精确记录

| 入口／动作 | 本轮实际输出 | 处置 |
|---|---|---|
| [BC 机构 PDF](https://dspace.library.uu.nl/bitstream/handle/1874/2189/1020.pdf?isAllowed=y&sequence=1) | (403) Forbidden | 本次明确拒绝；停止该入口，不覆盖旧 unknown 记录 |
| [旧 dbc handle](https://dbc.library.uu.nl/handle/1874/2189) | (404) Not Found | 旧 handle 不可达，不称正文不存在 |
| [尝试的 BC 出版社文章入口](https://www.sciencedirect.com/science/article/pii/S0022039697933596) | (403) Forbidden | 停止；未取得足以核 PII／正文的页面 |
| [Springer 书页](https://link.springer.com/book/10.1007/978-1-4419-7117-4) | not safe to open (non-retryable error) | 不重试同入口；不是已确认 HTTP 403 或付费墙 |
| [Springer 前件入口](https://link.springer.com/content/pdf/bfm:978-1-4419-7117-4/1) | 一行 Internal Error，无码 | 原因未知；未当作目录／前言读取 |
| [ScienceDirect 作者页](https://www.sciencedirect.com/author/6602893363/frits-beukers) | 一行 Internal Error，无码 | 搜索呈现与实际正文访问分开 |
| 作者 Profile 首次 click | invalid arguments | 改用已返回页面 ref 后正常成功，非权限错误 |

旧范围件中的 unknown 失败是另一次观测，本次明确 403 仅描述本次；二者不冲突，也不能互相改写。
未使用换代理、缓存绕读、身份切换或第三方整书镜像来绕过访问限制。

## 8. 可执行的后续科学接口

先完成不依赖缺读的原实分支几何与严格回返识别；本文不阻止这些已授权本地数学工作。
BC 主定理完整原文与 Duistermaat §§8、11.4 是 source/publication admission 前仍应核清的强覆盖项。
若未来取得新的合法公开正文或用户提供文本，须实际逐定理比较实域、参数路径、方向、回返次数及端点。
在此之前，不以“原族路径不同”“已有来源进不去”或短 Wronskian 恒等式授新颖性。
本次有界工作已终态，不继续第 17 条查询，不对原全局 twist、论文容量或整批完成作推断。
