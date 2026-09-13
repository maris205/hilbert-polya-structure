# Paper30：Ohyama 来源缺口核查 V1

日期：2026-09-09。范围：单篇公开一手来源的有界核查；不是查新评分、候选评价或数学证明审查。
交付状态：本轮访问结果已自查后冻结；全文缺口仍开放。旧执行的阅读经历不作为本实例已读证据。

## 1. 结论与版本身份

目标为 Yousuke Ohyama, *Expansions on special solutions of the first q-Painlevé equation around the infinity*，
待核出版引文为 *Proc. Japan Acad. Ser. A Math. Sci.* **86** (2010), no. 5, 91–92，
[DOI 10.3792/pjaa.86.91](https://doi.org/10.3792/pjaa.86.91)。

本轮确认了同题、同作者作品的存在，但没有取得出版全文或机构预印本的实际完整正文。
因此没有可新报的“亲读定理编号／证明页”或逐式排除结果。
书目中的卷号也不能报告为已经出版页眉独立核定：
[作者英文成果页第 [6] 项](https://math0.pm.tokushima-u.ac.jp/~ohyama/papers_e.html)实际写 **89**、no. 5、91–92、May 2010；
目标 DOI 字符串及若干检索索引指向 **86**，但 DOI 正文直达失败。
两种记录是待消解的书目冲突，不能凭作者网页自动把目标引文改成 89，也不能称本轮已用期刊页眉纠正了它。

[Newton 机构预印本入口 NI09061](https://api.newton.ac.uk/website/v0/events/preprints/NI09061)
的检索结果确实含同题、作者和首面内容；编号不在本件中转换成未经核实的提交日期或版本号。
未取得其完整正文、版本史或与出版版的逐字比较，故不能称 NI09061 与出版版等同。

本轮新增的明确访问证据是：
[日本学士院 Series A 官网](https://www.japan-acad.go.jp/en/publishing/pja_a.html)把正式档案链接至 Project Euclid；
其公开档案及本文 PDF 形式入口实际落到安全检查页面，而不只是笼统的“全文未找到”。
没有发现授权内可读全文，遂完成有限结果；这既不降低也不提高当前数学候选的科学结论。

## 2. 实际入口、来源层级与失败边界

| 来源与实际动作 | 本轮读到的内容／结果 | 可支持的范围 |
|---|---|---|
| 上述作者成果页，直接打开成功 | 第 [6] 项书目，含题名、作者、年份、期号、页码及冲突卷号 89 | 作者确有该作品；不是论文正文 |
| 上述 Newton 指定入口，直接打开 | 工具返回 Internal Error | 没有因这个动作取得全文 |
| 同一 Newton 地址的公开检索结果 | 题名、作者、摘要及印刷首面 §1 Introduction；首面下方可见页码 1 | 机构一手原文的搜索索引片段，不升级为实际打开的首面或全文 |
| Newton 搜索结果的截图请求，零基页 0、1、2 一批提交 | 三项均因内容未识别为 application/pdf 且网页截图未启用而失败 | 没有看到任何页面图像；请求页 2 不证明文档有第三页 |
| DOI 直达 | Internal Error | 未核正式出版页、摘要、页眉或全文 |
| 日本学士院 Series A 官网，直接打开并点击 Archives／Current and back issues | 确认正式档案链接为 `https://projecteuclid.org/pja` | 一手确认托管关系，未确认本文具体书目 |
| Project Euclid 卷 86 期 5 目录入口 | Internal Error | 未读取目录条目 |
| 按题名／DOI 构成的 Project Euclid `.full`、`.pdf` 形式入口 | 前者只返回空的一行 HTML，后者返回 iframe；不能据猜构 URL 认定文章已成功解析 | 未取得出版正文或 PDF |
| 对本文 `.pdf` 入口及官网档案页返回的 iframe 分别点击 | 两项均为 Website Unavailable，正文明确显示 “Additional security check is required” | 已确定这两次访问存在安全检查；立即停止 Project Euclid 路径 |
| J-STAGE 猜构的本文条目地址 | non-retryable safe-open 错误 | 不是经核实的正式条目；不据此断言 J-STAGE 有／没有本文 |
| 日本学士院猜构的旧目录地址、Newton 猜构的预印本网页地址 | Internal Error 或 non-retryable safe-open | 没有形成新的有效入口或版本证据 |

失败地址的精确目标（不把它们包装成可用来源）：

- `https://www.jstage.jst.go.jp/article/pjaa/86/5/86_5_91/_article`
- `https://www.japan-acad.go.jp/en/publishing/pja_a/contents/86/86_5.html`
- `https://www.japan-acad.go.jp/en/publishing/pja_a/issues.html`
- `https://www.newton.ac.uk/preprint/ni09061/`
- `https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-86/issue-5`
- 上项目录下的 `Expansions-on-special-solutions-of-the-first-q-Painlev%C3%A9-equation/10.3792/pjaa.86.91.full`
- 上项文章路径的 `.pdf` 形式。

安全检查地址中的运行时参数不复制进本件；没有解挑战、调整身份、代理换路、速率规避或权限绕过。
未把工具 Internal Error 解释为出版社拒绝开放，也未把一次可读搜索摘要解释为完整 PDF 已可访问。

## 3. 实际可见数学内容与精确比较边界

唯一可见的论文内容是 Newton **搜索索引首面**：摘要称无穷远的特定形式解唯一，
收敛与复参数的单位模条件相关，根单位时给代数函数，整数系数情形可用广义超几何级数表示。
同一首面 §1 的式 (1) 为

\[
\bar f\,f^2\,\underline f=t(1-f),\qquad
\bar f=f(tq),\quad\underline f=f(t/q),\quad q\in\mathbb C^*.
\]

这是对索引所呈现数学信息的转录与中文概括；没有把它算作亲读定理或证明。
尤其没有取得形式级数的具体规范、收敛半径、一般根单位的消元条件、逐个特殊参数公式或证明步骤。
“只在单位模条件下收敛”的摘要级说法在本件中不补成额外的充分性定理。

比较对象按本任务及当前简报固定为
\(F_t(x,y)=(st/(sx-y),sx/y)\)、\(t\mapsto st\)、\(\operatorname{ord}(s)=r\)、\(T=t^r\)，
以及原回返在完整有限闭纤维上的指定模型
\(W_\varepsilon(c,T):v^2+cuv-\varepsilon Tv=u^3-Tu^2\)、指定点 \(P=(0,\varepsilon T)\)。
以下“未核得”仅描述本轮来源证据，不等于断言 Ohyama 全文中不存在该结果。

| 比较项 | 可直接确认的重合 | 尚未核得的证明／不可排除之处 |
|---|---|---|
| 方程与参数 | 同属第一 q-Painlevé 的特殊解问题；索引式 (1) 采用复数非零参数 q | 未核从该规范到当前二维 F 的精确坐标／时间变换，不把 q=s 当成已验证身份；未取得任意特征或有限域版本 |
| 根单位与特殊代数解 | 摘要明确包含根单位下特殊形式解的代数性主题 | 未读一般根单位的定理量词、分支选择及证明；不能以“某个特殊解代数”替代“全纤维动力可约化” |
| s=1、−1 的特殊轨道 | 允许读取的旧定位段称 JR 引用 Ohyama 给出这两个小阶例子 | 本轮未读到 Ohyama 对应公式；此项只保留为继承的定位线索，不登记为亲自核实的 Ohyama 结论 |
| 退化纤维与奇点 | 首面提及初值空间无穷远除子的 A 型背景，不是有限坏纤维分类 | 未核有限坏值四次式、全部临界重数、节点／尖点分类；未取得足以排除它们的全文。特殊解也不能直接等同于整条退化纤维 |
| W 模型与指定回返点 | 实际可见索引未呈现本题 W、P 或谱模除子公式 | 未核 \(P_T-P_0\)、完整 r 步回返加 \(P\)、指定符号或整闭纤维延拓；不能由索引没有出现而排除全文覆盖 |
| 奇异群的标记元素与循环 | 实际可见片段没有提供节点乘法元素、尖点加法元素或有限点集循环公式 | 未核分裂／非分裂节点、小特征、奇点固定循环及全状态点阶；不能把特殊解公式当成完整光滑群上动力公式 |
| 同一原自治族约化 | 根单位话题与本题相关，但“根单位”本身不是自治共轭结论 | 未核 \(\mathcal R_{s,t}\sim\mathcal A_{t^r}\) 的逐闭纤维有限点集双射、全部合法状态及时间悬挂；该论文是否包含这些结论仍不能由本轮排除 |

当前简报的自治比较本来只主张逐纤维曲线同构在有限点集上的并合，不是随能级有理变化的全局曲面共轭。
本件保留这个准确层级，不把未取得的 Ohyama 结论与更强或更弱的不同命题混作直接查重。
本轮没有需要新读 V/C/Q/I 作者证明的具体全文公式，因此未打开那些作者件，也未审查当前候选的证明。

## 4. 实际检索账本

以下 19 式均实际提交公开网页检索；同批结果不强行分摊成每条 query 的独立零结果。
题名精确检索找到作者页、Newton 首面索引及多条二手书目；后续域限定检索多为无关项或空结果。
二手 ResearchGate、CiNii、Numdam 等检索片段只作为入口线索，没有充当论文定理证据。
未定位 arXiv 同题条目不意味着已证明 arXiv 不收录该文。

1. `"Expansions on special solutions of the first q-Painlevé equation around the infinity"`
2. `site:arxiv.org Ohyama "first q-Painlevé"`
3. `"10.3792/pjaa.86.91" site:jstage.jst.go.jp`
4. `"Expansions on special solutions" site:projecteuclid.org`
5. `"NI09061" Ohyama`
6. `site:arxiv.org "Ohyama" "Expansions"`
7. `Ohyama 2010 86 91 92 expansions Painleve Japan Academy`
8. `"pjaa.86.91"`
9. `"Expansions on special solutions" "Theorem"`
10. `"Expansions on special solutions" "projecteuclid"`
11. `"Expansions" "Ohyama" site:jstage.jst.go.jp/article/pjaa`
12. `"Expansions" "Ohyama" site:projecteuclid.org/journals`
13. `"Expansions" "Ohyama" site:japan-acad.go.jp`
14. `Proceedings Japan Academy Series A 86 5 2010 Ohyama`
15. `"Japan Academy" "May 2010" "91" Ohyama`
16. `"Expansions on special solutions" "pdf"`
17. `site:newton.ac.uk "Expansions on special solutions" "Theorem"`
18. `site:ir.library.osaka-u.ac.jp "Expansions on special solutions"`
19. `site:repo.lib.tokushima-u.ac.jp "Expansions on special solutions"`

## 5. 执行披露、未作检查与交接

使用可用 Codex AI 实例完成检索、比较与记录，不是作者确认、人类文献认证或跨模型复审。
亲自完整读取 research-lit 技能；按其来源降级原则使用公开网页检索与阅读工具。
工具发现中没有 Zotero、Obsidian 或 arXiv 专用工具；遵守本任务的本地输入白名单，未扫描本地论文库或安装服务。
用户限定不调用未请求的程序化书目 API，因此未运行技能默认 arXiv API 路径，也没有声称脚本调用成功；使用官方域网页检索 fallback。

本地科学输入仅为允许的当前候选简报可见内容（科学比较只消费对象／T1–T7）及旧来源报告中 Ohyama／GRT 定位搜索返回，
另读工作流和技能。简报自身的历史摘要不作本件判断依据；未另读新旧正式评分票、其他独立报告、README／BATCH、跨论文原稿或额外证明输入。
没有委派，没有下载或保存任何 PDF，没有付费访问、外发消息、上传、投稿或改变项目状态。
唯一新增工作区文件是本件；没有修改输入、论文目录或旧冻结记录。

尚未完成：出版页眉消解卷号冲突；NI09061 的完整正文／版本身份；正式出版全文；预印本与出版版差异；
特殊参数公式及根单位定理的准确页节；退化纤维、标记点及有限域自治约化的逐式包含／排除；完整前向引文图。
GRT11 不在本任务的全文核查目标中，没有另行检索、读取或作结论。

本轮没有新全文数学证据，不能消除旧记录中的 Ohyama 来源缺口；也没有新证据推翻当前候选。
新增可复核事实限于作者页独立重读、正式档案托管链及实际安全检查原因的定位。
交接后以本件全文回读、行数和 SHA256 绑定本次有限结果；不在文件内写自指哈希。
