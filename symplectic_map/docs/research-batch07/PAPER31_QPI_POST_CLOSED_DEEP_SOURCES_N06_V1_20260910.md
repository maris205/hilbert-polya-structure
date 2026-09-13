# Paper31：N06完整能量像的逐主张来源核对（Phase B，V1）

日期：2026-09-10（项目日期）；执行席：主控。
状态：`SOURCE_CHECK_ONLY / NO_NEW_MATHEMATICS / NO_NOVELTY_SCORE / NO_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。仅处理N06-C1/C2/C3，不替代独立C/D或固定曲线诊断。

## 1. 输入身份与准确待判问题

本人FULL读[Phase A][PA]92行、[基线][BASE]210行、[生成][GEN]233行、[首筛汇合][FILTER]63行及[局部来源增量][LS]55行。
本件只消费基线已接受对象，不重新审计其证明。输入SHA：

| 输入 | SHA-256 |
|---|---|
| PA | `8a8b9ba44f5e98e9ea6c31820c299dc69b81fe76b4f0ff8f67850f09a048a0a3` |
| BASE | `6c24c6cab58c899ef90f2369cb1bd83c8ff3de8668b77119351b684ac3df115e` |
| GEN | `b18e8cea87cb85355628f738eaf2fe69e44b0c5b4e1f564bcaf08228c071999f` |
| FILTER | `aae3b87f97289c36510f1f459055131d85d04aaf5239d5196bbe9518f4e17f2c` |
| LS | `bbabf1cf5d65cd80a192ba326e73aea50f883b1b4a57fa442e4212bfb70c3696` |

C1只问固定 $K=\mathbb Q_3(\zeta_3),t=1,h=0,c_1=-3+\pi^2$ 的**完整**原曲线有无点；$c_0=-3$已有点不再计功。
C2问原proper pencil在事先核准的光滑紧能量圆盘上的准确整数点能量像。
C3问相对原能量标签／固定圆盘的最小决定精度，及原临界数据是否足够；不把算法树深、Tamagawa距离或某个充分精度直接叫 $N_{\rm sol}$。
当前未核出原plane cubic呈示、全图能量像、共同光滑紧盘、固定 $c_1$ 可解性或锐界，不允许末端无根代签完整无点。

## 2. 实际查询与渠道限界

以下九条均为本件新执行，按主张归档；每项三种表述，不挪用首筛次数。

| 主张 | 三条实际查询 |
|---|---|
| C1 | `"q-Painlevé" "local solubility"`；`"genus one" "local solubility" algorithms ternary cubic p-adic`；`"local solubility" "genus one" 2024 2025 2026 site:arxiv.org` |
| C2 | `"p-adic" "image" polynomial "Jacobian" cell decomposition`；`"genus one" "pencil" "local solubility" energy`；`"p-adic families" "local solubility" 2024 2025 2026 site:arxiv.org` |
| C3 | `"local solubility" "precision" "discriminant" genus one`；`"p-adic" "optimal" "Hensel" "Jacobian ideal"`；`"local constancy" "curves" "precision" 2024 2025 2026 site:arxiv.org` |

另执行最新半年 `"p-adic" "local solubility" after:2026-03-10 before:2026-09-11 site:arxiv.org`，以及 `site:arxiv.org "local solubility" "2026" "genus one"`。
公开目录查询为 `"q-Painlevé" "local" site:scholar.google.com`、`"genus one" "local solubility" site:semanticscholar.org`，后各加Fisher–Sills确切题名查询；本轮未返回可用于排除先例的Scholar／S2正文。
旧阶段直接Scholar403／S2 429不重试或绕过；现有工具无独立学术数据库接口。本轮渠道是Web公开索引＋arXiv／作者／出版方原文，不能声称三大库已完整检索。
补充技术查询三条：`"Greenberg" "approximation" "Jacobian ideal" discrete valuation`；`"local solubility" "mod" "discriminant" cubic Fisher`；`"p-adic" "image" "critical values" polynomial local solubility`。
版本定位另查Hensel minimality II arXiv、Fisher–Sills刊名／页码／DOI、Schrettner2026；一次Fisher页码猜测未命中，最终只用AMS原元数据1635–1662。
ML会议目录与此纯数学对象无关，未机械列作覆盖。商站／ResearchGate／二手综述及无关软件日志未作技术结论依据。

## 3. 一手来源及其准确压力

### S1. Fisher–Sills：完整局部可解性算法与终止深度早已存在

T. A. Fisher、G. F. Sills，*Local solubility and height bounds for coverings of elliptic curves*，Math. Comp.81(2012),1635–1662；电子发表2012-02-21，[AMS元数据](https://www.ams.org/journals/mcom/2012-81-279/S0025-5718-2012-02587-7/)，[arXiv v1](https://arxiv.org/abs/1103.4944v1)提交2011-03-25。
本人读[作者40页长稿](https://www.dpmms.cam.ac.uk/~taf1000/papers/htbounds.pdf)，稿面日期2010-10-12；AMS参考文献将arXiv列为较长版，本件定理号按亲读作者长稿，不冒称刊本同号。

§2对任意有限 $K/\mathbb Q_p$ 的非奇异属一degree2/3/4模型给判定法；§2.1先清分母再遍历标准射影图，Algorithm2.3递归处理三次模型非正则剩余点。Lemma2.1给到最大无分歧扩张的WC限制核阶为Tamagawa数；不能据此略掉原模型识别。[作者长稿§2](https://www.dpmms.cam.ac.uk/~taf1000/papers/htbounds.pdf)

Th4.13的Tamagawa距离上界分别为 $\tfrac12v(\Delta),v(\Delta),2v(\Delta)$；Cor4.14证明算法终止，层数稳定后递归次数有 $\tfrac12v(\Delta)$ 界。Remark4.15区别树深与宽。它们不等于原能量圆盘的最小 $N_{\rm sol}$。[同稿§4.4](https://www.dpmms.cam.ac.uk/~taf1000/papers/htbounds.pdf)

亲读范围：摘要、完整§1/1.1、§2开头及Lemma2.1与证明、§2.1前言和Algorithms2.2/2.3；完整§4.4及其可见证明。整篇PARTIAL；§2.2/2.3与§3未完整审计，未运行Magma，也没有把原 $X_{c_1}$ 化成其输入。
**主控推断：** C1若只做到“全图递归判定”或一次具体计算，方法层新意很低；原族结构识别仍可未供给，但不能把算法存在或终止当作新机制。

### S2. Hensel minimality II：混合特征像的分片与导数控制是一般理论

R. Cluckers、I. Halupczok、S. Rideau-Kikuchi、F. Vermeulen，*Hensel minimality II: Mixed characteristic and a diophantine application*，[arXiv v2](https://arxiv.org/abs/2104.09475v2)，2023-09-07；Forum Math. Sigma11(2023),e89的原作者索引／刊本搜索元数据可见，正文使用[官方arXiv HTML](https://arxiv.org/html/2104.09475v2)。

在1-h-minimal假设下，Cor3.1.3/3.1.4给适当小球上的精确导数距离关系及像球；Th3.3.3在另加 $\mathrm{acl}=\mathrm{dcl}$ 时给有限cell分解，Addendum3给一维定义域／像相容准备。Th3.3.8给高维sup-Jacobian分片。[§3](https://arxiv.org/html/2104.09475v2#S3)

这里cell不等于有限个固定半径球，RV数据可承载无限族；其一般存在性不是原能量球清单。适用语言／参数、原模型图及compact光滑盘仍要核准，不能从一个临界理想的阶直接恢复全部像。[§3.3](https://arxiv.org/html/2104.09475v2#S3.SS3)

亲读摘要、完整引言、Def2.1.1及相邻记号、Remark2.2.3、从Prop3.1.1到§3.3末的全部可见文本（含定理及其证明，未补读转引Part I）；整篇PARTIAL。某些合并输出在无关后续§4处截断，不影响上述指定段可见完整性。
**主控推断：** C2“能量像可分片”和C3“导数控制局部像球”均须先扣除；真正剩余是原整体像的确定与锐性，不能通过把通用分片改称“临界数据控制”提高新意。

### S3. Schrettner2026：当前局部恒定性和充分精度的强先例保持

J. Schrettner，*Local constancy of reduction type and related invariants for curves in p-adic families*，QJM在线2026-08-06，[刊本](https://doi.org/10.1093/qmath/haag026)、[v2](https://arxiv.org/html/2508.12329v2)；v2提交2026-08-21、稿面2026-08-24。
主控此前已本人读摘要／引言／Def2.1及完整§5，本件消费[LS][LS]的准确记录，并新核当前元数据，不重开同一未变证明。
Th5.3的excellent DVR与regular closed embedding假设、Th5.7的Henselian有点性恒定及Remark5.4的有效充分精度均保留。未声称它给原最小精度；LS关于Hensel必须用相对光滑轨道的警告保持。[§5](https://arxiv.org/html/2508.12329v2#S5)
**主控推断：** C2的局部常值／C3的某个有效充分界不能再作为新中心；在固定光滑紧盘上加紧致性的有限覆盖亦是标准消费者，不是本轮已做出的原精确像。

### S4. 原动力文献与最新半年排除范围

Joshi–Roffelsen的2026刊本及其有限阶Lax新说明按[LS][LS]保持：只消费此前实际可见段，没有重查整刊，也不宣称全文完全排除局部可解性。[刊本](https://doi.org/10.1088/1751-8121/ae67bf)
最新半年查询命中Arango-Piñeros、Keyes、Kobin，*On p-adic solubility of Ax^\ell+By^m+Cz^n=0*，[arXiv2608.18525v1](https://arxiv.org/abs/2608.18525v1)，2026-08-19。本人仅元数据／摘要：主题是广义Fermat方程及局部概率，未见与固定原qPI pencil一致的对象；HTML正文超时，因此不据它排除隐藏的算法相关内容。
补充查询出现Greenberg／Artin函数综述、全系数平面三次局部密度、equicritical quartic等。前者仅作标准包含线索、后两者对象不同，本轮未全文读，不给“先例完全排除”标签，也不跨族吸收成P31。

## 4. 逐主张差额：方法已知，原发现尚待检验

| 主张 | 最近直接压力 | 本轮没有找到或供给的准确原增量 | 给C/D的判断材料 |
|---|---|---|---|
| C1 | S1的全图判定与终止；普通Hensel机制 | 固定 $c_1$ 的完整原点或全图排除仍未做；degree3正常模型及与原图的比较未供应 | 固定例子是诊断，不是独立长文承诺；算法存在没有新意 |
| C2 | S2的定义性／分片；S3局部恒定；原proper延拓 | 原 $\Sigma_{t,h}$ 的精确球清单和必要充分性 | “可描述”已弱；若只是标准算法输出几个球，应停长文 |
| C3 | S1判别式树深、S2导数像球、S3显式充分精度 | 相对固定原标签／盘的严格最小 $N_{\rm sol}$；临界数据决定能力或实际不足性 | 锐性不能用上界代签；最优值本身亦须科学消费者，不能仅称更尖锐 |

N06是旧I09的carry-forward，不把proper像路线另算新题。本件没有证明标准来源直接包含所有原族结论，也没有由未命中推断新颖。
目前最有意义的有界问题仍是固定 $c_1$ 全曲线诊断；是否值得选择它，应与另三项完整Phase B和独立批评合并决定，而非本来源件单独推荐。

## 5. 实际访问和交付限界

AMS全文直开internal error但出版方搜索返回元数据／摘要；作者PDF可读。未取视觉截图，不把PDF提取文本称视觉审查。
Hensel minimality II刊本直开internal error、旧ENS作者PDF404；一次尚未核版本时猜v3失败，随后由官方abs确认最新v2并成功读HTML。不是读取v3后回填v2。
最新Fermat HTML两次访问均超时，未换非一手镜像或宣称全文排除。旧Schrettner截图／刊本局部失败仍按LS，不因本轮索引可见而擦除。
本轮无数学计算、CAS、Magma、GPU、proof/pilot、评分、Route评价或完整候选准入。只有本文与先前Phase A为主控新增；不改冻结旧件、不建P31项目／锁／稿件／PDF，不上传／投稿。
本文写后本人全文读回，检查五个直接本地引用和输入SHA；终态行数／哈希另交接。Papers27–30接受、Batch07为4/5及P31正文22–30页保持。

[PA]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[BASE]: PAPER31_QPI_POST_CLOSED_BASELINE_GAPS_V1_20260910.md
[GEN]: PAPER31_QPI_POST_CLOSED_IDEA_GENERATION_V1_20260910.md
[FILTER]: PAPER31_QPI_POST_CLOSED_FIRST_FILTER_DISPOSITION_V1_20260910.md
[LS]: PAPER31_QPI_POST_CLOSED_LOCAL_SOLUBILITY_SOURCE_ADDENDUM_V1_20260910.md
