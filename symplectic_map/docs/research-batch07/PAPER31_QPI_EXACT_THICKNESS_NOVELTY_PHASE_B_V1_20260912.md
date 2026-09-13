# Paper31：原固定 T 准确厚度逐项查新 Phase B V1

日期：2026-09-12 UTC；来源席：`/root/p31_exact_thickness_phase_b_v1`。
状态：`CLAIMWISE_PHASE_B_COMPLETE_WITH_READING_GAPS`；route_applicability: NOT_APPLICABLE。
本件只执行冻结[Phase A][A]的V1–V3来源对照，不授新意分、数学PASS、正式候选准入或正文容量票。
novelty-check与research-lit均本人完整读取并使用；Phase C/D另由主控组织，不在本文件自评。

## 1. 结论先行：可扣除的机制与仍需评价的发现

在本轮列明的实际阅读范围内，未找到直接陈述原固定 $T$ 切片三组准确数值的文献；这不是无先例证明。
最强反向证据是：相同有标点Tate正常形已有，固定阶挠条件可以算法化计算，
一般Manin精确读阶、Igusa下降、Tate乘法传播和全倍数赋值公式也已有。
因此“从支持到重数”“出现二／三阶”“全部迭代”三个描述本身均不构成新方法。

| 核心断言 | 一手先例的直接包含部分 | 本轮仍未在实读处找到的原族输出 | 评价时的主要风险 |
|---|---|---|---|
| V1 | [UV]准确complex-Betti读阶与端点公式；[B97]/[V90]/[U91]正特征下降；[GMX]/[CCRS]同一正常形 | $H=32T+3h$ 的forcing及 $N_p'$ 分解；原好点Hasse准确阶；正特征消除导数盲区后的实际接触界 | 特征零2/3在forcing已知后是标准精确读阶的直接后果，不能独立算新结构定理 |
| V2 | [N16] Lemma8.2精确全倍数传播；[UV]式(3.1)兼容Igusa速度；[CCRS]固定阶挠多项式；旧[PF]/[FIX] | 所列全部素域好点上 $c_*=i_d$ 的实际分支求值，尤以 $p\mid d$、$q=0$ 与超奇异边界为准 | 全倍数公式与固定理想是消费者；新意不能由“任意n”字样累加 |
| V3 | [Tate]整数级数及乘法同态；[GMX]奇异Lyness纤维的Möbius动力学；旧节点正规化／固定理想 | 原固定T的首项、唯一 $(3/16,-2)$ 二阶例外、原h无分歧匹配 | 是特定一参数切片的二阶消去问题；普遍正常形和已知Taylor工具必须充分扣除 |

三项仍是同一原截面初始交数问题，不能拆成三篇或把标准消费者另立创新项。
本文件没有判定这些剩余具体发现是否足够达到Paper31原完整门槛；留给独立C/D及后继正式候选评价。

## 2. 实际冻结输入与阅读身份

下列前五件本席均FULL读取；原数学接受作为来源比较的固定输入，不重新审查其证明。
路径均相对 `docs/research-batch07/`。

| 输入 | 行／字节 | SHA-256 |
|---|---:|---|
| [A] `PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md` | 157／9522 | `171e8aa602d6431e76672c79cf6962c9269f73a6f91993ef7c131a697a4ac917` |
| [SYN] `PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md` | 245／10241 | `5400ed2775b3a91f85c814d9c8c8fb252dc91cf8577579f63da0cee87e7539d1` |
| [D] `PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md` | 234／13710 | `5340f77faa1354b1239240e3d7ba7068ae32e752e6d4550e32b2f243ea08bc99` |
| [SA] `PAPER31_QPI_MANIN_CONTACT_ORDER_SOURCE_AUDIT_V1_20260912.md` | 192／12549 | `17b7f3175ce52b53c03a3c0540cadb00b59b5067205818a822a1c8d15b2502ed` |
| [SI] `PAPER31_QPI_EXACT_THICKNESS_SOURCE_INCREMENT_V1_20260912.md` | 169／14016 | `762643a7bed0a1d54fa074a823d28054811c26373441fc9d7e49e04cb508ded1` |
| 旧[M] `PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md` | 446／17913；仅60–78、349–368行 | `48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2` |

AGENTS.md、WORKFLOW.md本人FULL；BATCH仅当前入口前22行。
旧[M]的定向原文已经写明好点 $q=0$ 无prime-to-p切触；因此该排除必须再从V1增量扣除。
旧[PF]的素域支持充要性与旧[FIX]完整equalizer理想按[A]/[D]所固定的基线扣除，未另声称本席重读其全文。
没有读取本轮fresh组合报告、后续C/D报告、fresh数学报告，也没有接触其分数。

## 3. V1：准确读阶已有，原forcing和正特征局部输入分开比较

[UV] Proposition4.7在其例外集 $S$ 外给 $J=I-2$，$I$ 是与complex-Betti叶的最大接触阶；
Proposition4.11给完整移动端点修正。实际挠叶已经相切、且周期参数无分歧时，
它就是匹配该点及切向的唯一complex-Betti叶，故不能借“最大接触”与“指定挠叶”用词差别规避此包含。
本族forcing一旦已算出，特征零2/3结论在这一开集正是其标准局部后果。[UV]

该文§4.12.4还在Legendre的双二次基变换上取 $Q=3P_3-P_2$，实得一处三阶complex-Betti接触。
这不是原指定挠截面或固定T的实例，但足以排除“高阶现象本身首次出现”的定位。
§2 Remark2.4及§3 Proposition3.3在正特征给含交数的局部下界，不能直接替换为本族准确等式。
文献也明确其最优局部p可除接触量与指定挠截面交数只先有不等关系。[UV]

本族待评价的具体剩余是 $-H/(q\delta)$、$N_p'=-q^{p-2}AH$ 的显式原切片分解，
以及由原系数真正排除不可见高阶分支后得到的接触首项与Hasse零阶。
它们不是把特征零方程简单模p所得；一般正特征工具由[B97]§4.2–4.6、
[V90] Theorem3.1／§6、[U91]§5供应，必须扣除。
这些原文在本次实读范围没有给出原 $q=8h-9,H=32T+3h$ 的分类。

[UU22] Theorem1.7已有very general带点Weierstrass族的prime-to-characteristic横截性；
其参数全称不能替换为每条固定T切片，也不能忽略文中对小可数常数域的提醒。
本轮仍不声称定位特征零全部真实好切触，也不把 $H=0$ 条件当成三阶挠接触存在性证明。[UU22]

## 4. V2：一般传播与有限阶算法不等于已经求值初始交数

[N16] Lemma8.2的低Hasse阶分支直接给
$i_n=p^a i_d+h_v(p^a-1)/(p-1)$；不整除首次指标时为零。
所需ordinary是泛曲线形式群高度条件，不等于每个闭纤维都普通；
使用某地方 $h_v\le p-1$ 的分支，也不要求先证明全曲面处处tame。
本族已给 $e_*\in\{0,1,2\}$ 后，全n传播属标准代入，不能另申报一项新方法。[N16]

[UV]式(3.1)直接以兼容Hasse根和Igusa标点规范给下降同态的速度表达；
[B97]已有闭式一阶下降，[U91]§5有Cartier像与局部Selmer描述，[V90]核为p倍点的机制已在先。
这些来源均不因本族需要p-primary分支而失去先例地位。
本次未在其实际读取的陈述里找到指定素域截面 $p\mid d$ 时 $i_d=1+\mathbf1_{q=0}$ 的求值。

更强的算法基线是[CCRS]§§2.1–2.2：同一Kubert–Tate $E(b,c)$、指定 $(0,0)$，
用倍点有理式构造 $f_N(b,c)$，并说明通过Möbius分解抽取原始挠曲线。
所以固定N计算返回条件、将 $b=T,c=1-h$ 代入并分析重根，已有标准计算入口；
“可以计算”本身不是新发现。该文相关引理在特征零挠参数框架陈述，
没有在所读处给全部p、全部素域参数的统一初始1/2/3阶公式。[CCRS]

原V2剩余是消去未知 $i_d$ 后准确给出 $c_*$：
$p\mid d$ 时为 $1+\mathbf1_{q=0}$；$p\nmid d$ 时由同一旧 $N_p$ 及 $H$ 判为1／2／3。
其中旧[PF]支持充要性、有限群点阶d、已知Hasse／Frobenius事实与旧[FIX]理想都不算增量。
需要评价的是这个统一低阶取值是否超出常规特定切片计算，而不是是否重述一个未知交数。
量词只到全部素域好点；不扩为任意有限扩域、全部几何闭点或统一闭式点阶。

## 5. V3：强Tate／Lyness正常形基线与原固定切片

[GMX] Theorem3和§2.2确实使用
$E(b,c):Y^2+(1-c)XY-bY=X^3-bX^2$，带点 $R=(0,0)$。
原族是 $b=T,c=1-h,P=-R$；文中变换在适用开集给
$h_L=-T/(1-h)^2$、$a_L=((1-h)^2+1-h-T)/(1-h)^2$。
所以这是同一有标点正常形，不是远亲；但固定T同时移动两Lyness参数，
不是固定 $a_L$ 的同一动力学切片。文中的被除参数及小阶正常形边界不能删去。[GMX]

该文§3.1还实际把奇异有理Lyness纤维变为线性分式动力学，研究根单位与可能周期；
因此节点乘法群／根单位判据不能当新结构。[Hone]§§4–6、Theorem1又给有标点Weierstrass、
Somos和Lyness之间的变换及倍点算法；它们不是原基方向的交数定理。[GMX][Hone]

[Tate]所读整数系数 $x,y$ 与曲线系数展开以及Theorem1的群同态证明，
已包含用乘法参数计算倍点的工具；形式隐函数及特征p的p次幂传播也应扣除。
新V3实际多做的是沿 $T$ 常数方向求解标点、保持原h的无分歧性，
并把一阶消去准确化为唯一 $(3/16,-2)$ 例外与非零二阶首项。
这些原切片系数未在本席实读Tate／GMX／Hone段落出现，不由普遍正常形自动变成已发表定理。[Tate]

旧节点坐标、乘法阶、完整 $z^{i_n}(\xi,\eta)$ 理想及长度一嵌入部分仍是既有输入。
特征5例外为尖点，不在命题域；一般代数闭 $k$ 上非根单位时交数全为零。
V3不因V2仅素域而被缩窄；节点上同一H因子的恒等式只说明凝聚性，不另计创新。

## 6. 本席一手阅读范围、近期线索和缺口

以下FULL只修饰列明的页／节，不修饰整篇；主控或旧代理的额外阅读未继承。
公开PDF通过内存管道解析，未建立下载库存。扫描文献缺式不报逐式视觉FULL。

| 来源及身份 | 本席本阶段实际阅读 | 用途／未覆盖 |
|---|---|---|
| [UV] arXiv2508.06680v1，2025提交 | 官方摘要／引言；HTML§2；PDF pp.8–18（§3、§4及参考文献）FULL；§2相关陈述证明已直接读 | 精确读阶、下降、例子；不宣称已读全部文件 |
| [V90] Compositio74(1990)247–258 | PDF pp.1–7、11–13：原文247–252、256–258及封面；Theorem3.1陈述证明及§6文本 | 扫描若干展示公式缺失，仅消费可核文本与UV明确复述，不报逐式FULL |
| [U91] Duke62(1991)237–265对应作者重排版 | 作者PDF pp.1–3，§5 pp.18–25 FULL（含Theorem5.5全部证明） | 页码非期刊页码；不继承旧代理的其它章节或勘误阅读 |
| [B97] Compositio107(1997)125–141 | pp.125–127、131–136全部可提取文字；§4.2–4.6及§5开头 | 公式提取有缺号；不称全篇／全部符号视觉FULL；兼容生成元精确式另由UV实读 |
| [N16] NYJM22(2016)989–1020 | 原文989–990与1003–1005 FULL | 摘要／引言；Lemma8.2全部条件证明及tame定义 |
| [Tate] 作者托管历史稿 | PDF pp.1–7 FULL | 读到同态／核证明，未读后续满射证明；未补造最终刊物年份 |
| [GMX] arXiv1004.5511v1(2010) | 官方摘要；PDF pp.1–9 FULL | 含Theorem3、§2.2全部、Lemma5节点分式与根单位机制；Lemma5后半未全读 |
| [Hone] arXiv2001.09076v3(2020) | 官方摘要；PDF pp.1–2、7–10 FULL | §§4–6及Theorem1；不称整篇FULL |
| [CCRS] LMS J.Comput.Math.17(2014)509–535 | pp.509–514可提取正文；§1、§§2.1–2.2 FULL | 同一Tate标点与固定阶算法；p.514图形未视觉核准、不消费图像结论 |
| [UU22] Selecta Math.28(2022)25 | 作者托管出版PDF pp.1–5 FULL | 摘要、引言、Theorems1.1/1.4/1.7/1.8；未读全部证明 |
| [Ottolini] arXiv2506.15344v2(2025) | 官方题录；PDF pp.1–4 FULL | 摘要、相关工作及Theorems1.3–1.5：一般特征零相切有限性，不是原族厚度 |
| [Greene] arXiv2606.01571v1(2026-06-01) | 官方题录、HTML摘要／§1及§2到Theorem2.2证明 | 近期intrinsic torsion pairing／isogeny分类，筛查线索；未借题名声称完整排除 |

时间核对：UV官方abs目前只列2025-08-08的v1，而当前HTML内部写2026-08-24；
本文件保持两个事实，不造v2或出版日期。[UVabs]
Ottolini最新v2为2025-09-10，不属于近六个月新预印本；2026期刊搜索显示未用于版本判断。[Ottolini]
Greene的2026-06-01提交在近六个月内；并非所有近期Tate／torsion关键词都属于本交数问题。[Greene]

Duistermaat书籍及官方chapter7入口本阶段均未取得正文，返回内部／不可重试安全访问错误。
因此相关周期纤维和Lyness章节的直接先例仍是覆盖缺口，不能以目录或访问失败排除。[Duistermaat]
Google Scholar、Semantic Scholar逐项入口均失败；已配套执行限域Web查询，但不宣称这些数据库已穷尽。
Zotero／Obsidian工具未配置；定向查找arxiv_fetch.py未得，按技能使用arXiv主站和限域搜索回退。
只定位本地PDF文件名以找相关一手来源，未找到上述作者／题名匹配，未重扫旧构建PDF内容。
ICLR／NeurIPS／ICML数据库对本纯数学断言不适用，未造会议检索。

## 7. 本阶段精确查询账

旧[SA]/[SI]次数不挪算。本席18条实际Web查询；每项各6条，前三为不同表述，后三为来源入口。
空结果或无关命中仅记覆盖状态；搜索引擎公式分词有明显失真，不作排除证据。

| ID | 命题 | 实际查询字符串 | 主要返回 |
|---|---|---|---|
| B01 | V1 | `"Tate normal form" "fixed b" tangency Picard Fuchs` | 无可核固定切片直接命中 |
| B02 | V1 | `"Lyness" "torsion" "intersection multiplicity"` | 无可核准确原交数命中 |
| B03 | V1 | `"Manin" "elliptic surfaces" "zero" "order" tangencies 2024 2025 2026` | UV镜像／作者讲座；另见Ottolini期刊线索，后转一手 |
| B04 | V2 | `"elliptic" "prime field" "initial" "intersection multiplicity" torsion` | 普通教材及异义结果，无原族命中 |
| B05 | V2 | `"elliptic divisibility" "Hasse" "Lemma 8.2"` | Naskręcki镜像，转NYJM一手 |
| B06 | V2 | `"Igusa" "p-primary" "tangencies" 2024 2025 2026` | 无固定初始交数命中 |
| B07 | V3 | `"Tate normal form" "nodal" "contact"` | 无固定切片直接命中 |
| B08 | V3 | `"Lyness" "3/16" elliptic` | 大量Lyness人名／日期歧义；Hone相关题名线索 |
| B09 | V3 | `"QRT" "fixed" "multiplicity" "nodal" 2024 2025 2026` | 无原节点厚度命中；QRT／qRT异义 |
| B10 | V1 | `site:scholar.google.com "elliptic surfaces" "tangencies" Manin` | 该三查询批返回Empty search results |
| B11 | V1 | `site:semanticscholar.org "elliptic surfaces" "Manin"` | 同上 |
| B12 | V1 | `site:arxiv.org "Tate normal form" "tangencies"` | 同上 |
| B13 | V2 | `site:scholar.google.com "elliptic divisibility" "Hasse"` | 该三查询批返回Empty search results |
| B14 | V2 | `site:semanticscholar.org "Divisibility sequences of polynomials and heights estimates"` | 同上 |
| B15 | V2 | `site:arxiv.org "prime field" "torsion" "multiplicity"` | 同上 |
| B16 | V3 | `site:scholar.google.com "Lyness" "singular" "Tate"` | 无相关数学命中 |
| B17 | V3 | `site:semanticscholar.org "Lyness" "Tate"` | 该批返回医学作者同名文献，未消费 |
| B18 | V3 | `site:arxiv.org "Lyness" "nodal" "multiplicity"` | 无相关数学命中 |

另直接打开下列六个入口，均返回Internal Error；它们是访问检查，不另充成功数据库检索。

- `https://scholar.google.com/scholar?q=elliptic+surfaces+Manin+tangencies`
- `https://www.semanticscholar.org/search?q=elliptic%20surfaces%20Manin%20tangencies&sort=relevance`
- `https://scholar.google.com/scholar?q=elliptic+divisibility+Hasse+valuation`
- `https://www.semanticscholar.org/search?q=elliptic%20divisibility%20Hasse%20valuation&sort=relevance`
- `https://scholar.google.com/scholar?q=Lyness+Tate+nodal`
- `https://www.semanticscholar.org/search?q=Lyness%20Tate%20nodal&sort=relevance`

只读辅助 `/root/p31_exact_thickness_phase_b_v1/recent_search_only` 独立执行以下17条，无文件所有权。
其阅读仅题录／摘要／提交历史，不冒充本席阅读全文；UV与Ottolini关键内容本席已另读。
时间窗口明确为2024-01-01至2026-09-12，近六个月为2026-03-12至2026-09-12。
日期限定并未被引擎严格遵守，归类按主站提交／官方事件日期，不按抓取日期。

| ID | 命题 | 辅助实际查询字符串 | 主要返回 |
|---|---|---|---|
| R01 | V1 | `"elliptic" "32T+3h" after:2024-01-01 before:2026-09-13` | 无相关数学命中 |
| R02 | V1 | `"y^2+hxy-Ty" "x^3-Tx^2" after:2024-01-01 before:2026-09-13` | 公式分词失真，无可识别原族命中 |
| R03 | V1 | `"elliptic" "Picard-Fuchs" "torsion" "tangency" after:2024-01-01 before:2026-09-13` | UV及不相关Calabi–Yau题名 |
| R04 | V1／6月 | `site:arxiv.org "elliptic" "torsion" "tangency" after:2026-03-11 before:2026-09-13` | Empty search results |
| R05 | V2 | `site:arxiv.org "elliptic" "Hasse" "intersection multiplicity" after:2024-01-01 before:2026-09-13` | Empty search results |
| R06 | V2 | `"elliptic" "p-primary" "intersection" "Hasse" after:2024-01-01 before:2026-09-13` | BSD／Hasse principle异义，非原厚度 |
| R07 | V2 | `"elliptic surfaces" "tangencies" "characteristic" after:2024-01-01 before:2026-09-13` | UV、作者讲座及窗口外UU |
| R08 | V2／6月 | `site:arxiv.org "elliptic divisibility" "characteristic" after:2026-03-11 before:2026-09-13` | Empty search results |
| R09 | V2／6月 | `"elliptic" "formal group" "multiplicity" "finite field" after:2026-03-11 before:2026-09-13` | 教材／不同对象，非初始厚度 |
| R10 | V3 | `"elliptic" "3/16" "nodal" after:2024-01-01 before:2026-09-13` | PDE／谱隙异义 |
| R11 | V3 | `"nodal" "torsion" "contact" "elliptic surfaces" after:2024-01-01 before:2026-09-13` | 旧曲面／contact-conic工作，无原例外 |
| R12 | V3／6月 | `site:arxiv.org "elliptic" "nodal" "tangency" after:2026-03-11 before:2026-09-13` | Empty search results |
| R13 | V3／6月 | `"elliptic curve" "3/16" "tangency" after:2026-03-11 before:2026-09-13` | 教材／旧Poncelet，无原例外 |
| R14 | 总补查／6月 | `"elliptic surfaces" "unlikely intersections" after:2026-03-11 before:2026-09-13` | 旧文及2024／2025讲座 |
| R15 | UV／6月 | `"Ulmer" "Voloch" "New unlikely intersections" after:2026-03-11 before:2026-09-13` | v1镜像、作者CV；不证明新版 |
| R16 | 邻近 | `"Singular intersections in families of abelian varieties" arxiv` | Ottolini主站v2 |
| R17 | 邻近／6月 | `"Singular intersections" "Ballini" "Capuano" "Ottolini" after:2026-03-11 before:2026-09-13` | 2026-04-23罗马大学官方讲座[Talk] |

辅助确认[Talk]是近六个月真实事件而非新预印本；本席没有继承为本人全文阅读。
辅助ScienceDirect打开Ottolini页面得403，未绕过；本席使用arXiv原文。
主控另提供CCRS与Greene一手URL作为来源线索，本席自行读取列明范围；不把主控查询充作本席次数。
本阶段合计35条真实search-query，外加6项直接数据库入口检查；没有借这些次数断言穷尽。

## 8. 交接边界

Phase B可供独立C/D使用的结论是：原具体数值未在列明实读范围直接命中，但一般机制和固定阶计算基线很强，
必须判断剩余统一分类是否非例行、是否有独立价值；不能只看显式公式数量或数学接受。
Duistermaat正文与Scholar／Semantic Scholar访问缺口应进入后续不确定性评估，不作加分或伪装排除。
冻结[A]不改；本件不新增主张、不缩量词、不重开数学、不运行采样、不建项目／锁／稿件／PDF。
唯一新增工作区文件为本件；未修改BATCH、README、原作者稿、旧失败或Papers27–30接受产物。
无投稿、上传、托管、push、发信、付费资源或其他外部效力。

[A]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
[D]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md
[SA]: PAPER31_QPI_MANIN_CONTACT_ORDER_SOURCE_AUDIT_V1_20260912.md
[SI]: PAPER31_QPI_EXACT_THICKNESS_SOURCE_INCREMENT_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1
[UVabs]: https://arxiv.org/abs/2508.06680
[V90]: https://www.numdam.org/article/CM_1990__74_3_247_0.pdf
[U91]: https://dlulmer.github.io/research/papers/1991.pdf
[B97]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf
[N16]: https://nyjm.albany.edu/j/2016/22-46v.pdf
[Tate]: https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf
[GMX]: https://arxiv.org/pdf/1004.5511
[Hone]: https://arxiv.org/pdf/2001.09076
[CCRS]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/66737ACC99BC2D4F70EE3A2D38FF1EB6/S1461157014000072a.pdf/computation-on-elliptic-curves-with-complex-multiplication.pdf
[UU22]: https://dlulmer.github.io/research/papers/2022.pdf
[Ottolini]: https://arxiv.org/abs/2506.15344
[Greene]: https://arxiv.org/abs/2606.01571
[Duistermaat]: https://link.springer.com/book/10.1007/978-0-387-72923-7
[Talk]: https://www.mat.uniroma1.it/it/singular-intersections-families-split-semiabelian-varieties
