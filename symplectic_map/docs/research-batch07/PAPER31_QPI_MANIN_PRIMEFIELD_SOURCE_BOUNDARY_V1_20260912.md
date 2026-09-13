# Paper31：素域充要性与固定概形接口的来源边界 V1

日期：2026-09-12 UTC。主控：`/root`。
标签：`BOUNDED_SOURCE_AUDIT / STRONG_STANDARD_PRIOR_ART`。
本件不是全球新意保证、正式四门评分、source lock 或论文；旧来源记录不回写。

## 1. 检索对象与实际来源

本轮从已接受原 Manin 必要多项式接续，只问两件新事：素域根能否获得充分切触意义，以及
原完整固定概形能否合法消费准确截面交除子。research-lit 用于具体来源与读取层级的核对，不启动完整选题流水线。
本地定向 PDF 文件名筛选未见新增相关库文件；Zotero／Obsidian 工具未配置，arxiv_fetch.py 未找到，使用公开网页回退。
没有重扫旧构建树、下载 arXiv PDF 集或写外部文献库。

| 来源 | 身份与渠道 | 主控本人实际读取 | 本轮影响及限制 |
|---|---|---|---|
| [Ulmer–Voloch][UV]，*New unlikely intersections on elliptic surfaces* | 官方 arXiv:2508.06680v1；已有来源 | §2设置、定义、Manin公式、Proposition2.3陈述及完整证明；本轮又核对所消费部分 | 同态与好约化局部估计是旧机制；源§3的Igusa普遍族问题不自动成为原qPI问题 |
| [Voloch，DLP与下降][VD] | 作者托管7页PDF；作者预印本索引第64项亦确认题名，未核定最终刊物版本 | 全7页正文和参考文献；尤其p.2–3下降及明确的 $YM(X)$ 公式 | $A=1$ 的素域同态有准确先例，不能重新申报；论文同时讨论更一般下降，不据此代替本原族全部异常谱 |
| [Voloch 1990][V90]，*Explicit p-descent for elliptic curves in characteristic p* | Compositio Mathematica74(3),247–258；Numdam原期刊扫描及书目页 | 印刷pp.247–252的文本提取，含§1的Lemma1.1／Proposition1.3和§3Theorem3.1；若干扫描陈列式未被文本提取，故不报这些页的完整逐式原PDF验读 | Proposition1.3明确下降同态的核及 $yV(x)/c^p$；这是强上游先例。主控作者证明写成后才补读，作者稿的先前读取快照不回写 |
| [Broumas 1997][B]，*Effective p-descent* | Compositio Mathematica107,125–141；Cambridge合法官方PDF，DOI10.1023/A:1000170513383 | 首页至§4.2前段，未读全篇；明载可分闭包上等变同态 | 首页提取为 $p>5$，不猜测改成其他符号；本原 $p>3$ 的直接证明输入仍是UV明确接口，不由此升级 |
| [Conrad 2006作者稿][CON]，*Arithmetic moduli of generalized elliptic curves* | Stanford作者PDF，首页日期2006-07-18；49页 | printed pp.4–6：Definition2.1.2、标准多边形作用、Definition2.1.4、Fitting奇点概形及Remark2.1.13 | 几何整的DR半稳定亏格一族加光滑截面供应完整广义作用；不只光滑点群。DR上游原证明未读，不声称全49页或Tate形式一致化已验 |
| [Miranda–Persson 1989][MP]，*Torsion groups of elliptic surfaces* | Compositio Mathematica72(3),249–267；Numdam | 前段至§3初部；关键printedp.252§2Lemma2.1及proof转引 | 此处是全局挠截面的半稳定节点作用，不能直接套非挠截面的单点特化；其转引[M-P1]未读。仍扣除节点乘法切表示机制 |
| [Duistermaat 2010目录][DU]，*Discrete Integrable Systems: QRT Maps and Elliptic Surfaces* | Springer书籍的ETH馆藏目录 | 3页目录FULL；§7.4“Number of periodic fibers”p.342、§7.5p.346、§7.7p.355；未读这些正文 | 加权周期纤维已有直接书目线索；搜索摘要不充完整定理。官方书页访问失败后未绕过或用来源不明镜像 |
| [Voloch 2026讲义][SL]，*Unlikely tangencies on elliptic surfaces* | Algebra at Akaroa，2026年1月官方会议站11页slides | 全文本提取；不是逐页视觉验收 | 切触与Manin接口是近期明确研究主题；slides无完整证明，部分公式提取不稳定，不作为新充要性定理或char0桥的证明 |
| [Stacks 0C9Y][MIN]、[0CBY][NODE] | 官方网页标准条目 | 55.10.1–2陈述证明；53.21.1陈述及第一证明 | 最小正则模型唯一性与节点平滑化的标准输入；不是原族新意 |
| [Milne，AG11][WEIL] | 作者2024-11-04版讲义Chapter11，38页 | §d末尾printedpp.37–38，对应、亏格及有限域点数界的推导 | 经典Hasse–Weil界的可直接核对来源，仅消费本好椭圆纤维 $g=1$ 情形；不引入Route主张 |

UV页面页头v1日期2025-08-08与正文日期2026-08-24的差异继续保留；不因本次重新打开就称为新版本发现。
Voloch预印本索引说“New version”而未给该项刊物信息；不能将网页抓取日期误充论文发表日期。
这里主控的阅读范围和各作者／独查者分别计量，不把代理读取自动升级为主控FULL。

## 2. 真正竞争关系

Manin必要筛选来自UV及其上游。新素域证明中 $A\ne1$ 支只需一阶常数值和有限群阶同余；
$A=1$ 支所用 $YM(X)$ 并不是新微分同态，Voloch有直接表达式及更一般下降背景。
本轮额外写出的极零次数小核证明是标准工具重证；它与原点的小阶排除一起闭合原族的充分方向，但不增加理论来源的原创性。

原固定概形方面，torsor的equalizer恒等式、最小模型延拓、广义椭圆作用及节点UFD理想计算都属标准消费者。
新显式原自治坐标及其符号核定有对象识别价值，但旧henselian模型式本来已经是相对同构，不能继续声称相对识别全缺。
把准确 $i_n$ 保留为输入后写出固定理想，不等于算出全部周期除子。

Duistermaat的目录线索足以禁止“前人未研究带重数周期纤维”的叙事，但不足以断言该书已证明本稿的所有正特征公式。
Miranda–Persson的全局挠截面假设同样必须保留。
这两条先例不能随意合并成一个不存在的全形式非挠截面定理；新节点理想仍应由实际相对作用证明接受。

因此，本轮来源证据支持“可建立有界数学接口”，不支持“已发现一个标准机制之外的长文中心”。
没有对旧FAIL重抽分数；没有把未读全文当作高新意证据，也没有据此宣布家族耗尽。

## 3. 主控实际18条查询

以下是本逻辑研究轮实际发出的查询，不把打开已知URL或代理查询并入数量。

1. `elliptic surface translation automorphism fixed point scheme tangency sections QRT`
2. `"QRT" "periodic" "multiplicity"`
3. `"elliptic" "Manin map" "tangencies" torsion strict`
4. `"Tate normal form" "ramification" modular unit b`
5. `Duistermaat QRT maps elliptic surfaces periodic curves multiplicities tangencies pdf`
6. `"Discrete Integrable Systems" "QRT" "periodic" Duistermaat PDF`
7. `"Tate normal form" "b" "critical points"`
8. `"Manin map" "tangencies" "characteristic" 2026`
9. `"Broumas" "anomalous" elliptic curves`
10. `"Semaev" "Hasse invariant" elliptic curve`
11. `"elliptic" "p-descent" "finite field" "Broumas"`
12. `"Manin" "dual numbers" "elliptic" characteristic p`
13. `"Effective p-descent" Broumas 1997`
14. `"Evaluation of discrete logarithms" "p" Semaev elliptic curves 1998`
15. `"anomalous elliptic" "y" "Hasse"`
16. `"elliptic" "YM" "Semaev"`
17. `"The discrete logarithm problem on elliptic curves and descents" Voloch`
18. `"Explicit p-descent for elliptic curves in characteristic p" "247"`

arXiv检索脚本缺失时按技能回退浏览；既有UV官网由查询和直接URL复读定位，不另生成API成功记录。
Springer书页、Fields旧摘要入口、PDF截图的访问／工具失败没有被算作全文阅读；公开合法可读源足以推进本次有界证明。
仅保存本地本件，未新增源锁、PDF库、永久实验、项目或外部效力。

[UV]: https://arxiv.org/html/2508.06680v1#S2
[VD]: https://web.ma.utexas.edu/users/voloch/Preprints/disclog3.pdf
[V90]: https://www.numdam.org/item/CM_1990__74_3_247_0/
[B]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf
[CON]: https://math.stanford.edu/~conrad/papers/kmpaper.pdf
[MP]: https://www.numdam.org/article/CM_1989__72_3_249_0.pdf
[DU]: https://toc.library.ethz.ch/objects/pdf/e01_978-1-4419-7116-6_01.pdf
[SL]: https://www.math.auckland.ac.nz/~hekmati/Akaroa2026/Voloch.pdf
[MIN]: https://stacks.math.columbia.edu/tag/0C9Y
[NODE]: https://stacks.math.columbia.edu/tag/0CBY
[WEIL]: https://www.jmilne.org/math/CourseNotes/AG11.pdf
