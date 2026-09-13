# Paper30 V4：独立终局完整性检查 V1

日期：2026-09-09。结论：`READY_FOR_LOCAL_ACCEPTANCE`。
检查者：`/root/p30_qpi_result_interface_inventory_v1`；对象仅为下列冻结 V4 与 r4/r5 同字节 PDF。
本结论表示当前 Paper30 本地接受所需的源、合同、产物、构建及独立审查链已一致闭合；不是整批 PASS、候选重评分或对外发布许可。

## 1. 角色独立性与实际范围

本人未参与 Paper30 证明作者、正式候选投票、此前完整稿静审、排版或完整稿/PDF 审查。
此前在本轮承担过 V3 既有接口盘点：全文读 S1/S5/S6/S7/S8、局部读 S2/S4，并全文读当前证明图；该接触明确披露，不称盲审。
此前[接口盘点](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_EXISTING_QPI_INTERFACE_INVENTORY_V1_20260909.md)已冻结，SHA-256 为 `e5033d678872970d5018f007fa18c15e4cf0085980f26eb0ba0a616fdab4036d`，本轮未改动。
完整稿/PDF 席是另一代理 `p29_p30_existing_interface_limits_v1`；其既有接口接触也已披露，但未参与本文作者、候选票、旧全稿静审或排版。
本轮检查在该席 184 行终态报告完成以后启动；没有拿布局作者的窄检查替代非作者全文席。

本轮是终局完整性检查，不重开未变的数学证明、69 件来源投票或已闭的旧转写审查。
本人使用 paper-compile 技能的产物诊断／页界／字体规范；最新任务将执行限定为只读验收，未执行技能中的清理、编译、安装、修源或压页建议。
唯一新增文件为本报告；未改正文、旧报告、锁、构建、索引，未联网、上传或对外操作。

## 2. 本人实际阅读覆盖

下表“全文”指本轮亲自从首行读至末行；字节检查与内容阅读分别陈述。

| 项目，路径相对本 notes 目录 | 实读范围／用途 |
|---|---|
| PUBLICATION_LOCK_20260909.md | 全文 72 行；原版式、页数、双根、完整 PDF 与后续独立验收要求 |
| PUBLICATION_PAGE_ADDENDUM_V2_20260909.md | 全文 53 行；用户仅对 Paper30 批准的 22–40 页窗口及 V4 successor |
| SOURCE_SCOPE_LOCK_V2_20260909.md | 全文 99 行；完整科学对象、量词、证明消费者与不得扩大的出口 |
| V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md | 全文 87 行；十一源、控制输入、四过程、双新根与元数据协议 |
| V4_TWO_ROOT_AND_ROOT_PDF_RESULT_V1_20260909.md | 全文 116 行；实际构建记录、根全部 41 页阅读覆盖、完整产物哈希表 |
| V4_LAYOUT_CONTRACT_DELTA_CHECK_V1_20260909.md | 全文 82 行；作者关系、两处真实排版变更及合同增补范围 |
| V4_COMPLETE_MANUSCRIPT_PDF_REVIEW_V1_20260909.md | 全文 184 行；非作者十一源全文、41 页逐页实读、全部必要证明及引用限制 |
| COMPLETE_DRAFT_STATIC_DISPOSITION_V1_20260909.md | 全文 39 行；已闭 V1 完整静审及 V1→V2 修订链 |
| BUILD_FIX_DELTA_RECHECK_V1_20260909.md | 全文 59 行；已闭 V2→V3 两处实际编译修复 |
| FIRST_NATURAL_BUILD_INPUT_PROTOCOL_V1_20260909.md | 全文 138 行；V4 继续使用的本地工具、14 项选定依赖及固定环境 |
| FIRST_COMPLETE_NATURAL_BUILD_RESULT_V1_20260909.md | 全文 122 行；保留的 r0 失败、r2 成功但正文超原窗记录 |
| COMPLETE_DRAFT_INPUT_SNAPSHOT_V1_20260909.md | 全文 37 行；核验保留 V1 十一源的原字节身份 |
| V4 main.tex、macros.tex、SOURCE_V4_20260909.sha256 | 分别全文 62、9、11 行；目录输入、全局版式、页界标记与冻结列表 |
| V3→V4 实际目录 diff | 全部输出；仅 §3 与 §6 各一个 hunk，另九文件同字节，无增删源 |

当前十一源均作实际字节校验及机械结构检查，总行数实算为 3486；不把这说成本席重新全文逐段审完 V4 数学证明。
两根 main.fls 各 825 行的全部记录由程序逐项解析并比较；最终日志全文作诊断扫描，r4 main.blg 46 行另全文亲读。
本人直接提取当前 PDF 全文作页数／未解标记检查，并亲读页 39–41 提取文本。
本人打开 r4/inspection 的实际单页图像 1、39、40、41，核标题匿名和正文／参考文献边界；本席不冒称重新观看全部 41 页。
完整 41 页的两次实读分别来自根和上述 fresh 非作者席已完成且同字节绑定的记录；保留的 page-01.png 至 page-41.png 共 41 件。

## 3. 有效合同及源版本

有效 Paper30 合同是原 publication lock 加用户批准的 V2 页数增补：正文 **22–40 物理页**，参考文献另页另计。
仅最大页数 30→40 改变；下限、匿名英文、article 11pt、letter、单栏、一英寸边距、正常行距及全部必要证明在正文等条件继续有效。
此例外不能继承到 Paper31；原 39>30 的失败保留，既不回写为通过，也不以本次判断修改旧候选票。
本席核验主控传入的明确授权与增补记录一致，不以旧记录“待用户决定”撤销后续已确认的决定。

V4 实际 main/macros 保持 V3 字节：无字号、边距、行距、数学编号或章节选择变化。
目录完整 diff 只有两处把相同数学内容移到正常无编号陈列式：§3 的循环矩阵等式、§6 的两个常数上同调等式；后随假设原样保留。
这与已终态布局检查一致；无科学范围删减、附录迁移或按页数择稿证据。

## 4. 当前源／PDF／日志的本人实测

| 核验对象 | 实际结果 |
|---|---|
| paper/v4/ 与 r4/work/、r5/work/ 的十一源 | 同一冻结列表逐项校验，共 33 项全部吻合；冻结表与生产 protocol 的源哈希一致 |
| 源结构 | 9 个 input 目标全部存在；8 个正文节齐备；135 个 label 无重复、无缺引用目标 |
| 文献／占位 | 17 个实际 cited key 与 17 个 bibliography key 一一对应，无缺项／未用条目；无 TODO/TBD/VERIFY/PLACEHOLDER |
| 页式源控制 | 唯一 clearpage 是正文末标记后的参考文献换页；未匹配正文 newpage、appendix、includeonly、全局 linespread/setstretch |
| r4 PDF | 546617 bytes；SHA-256 `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |
| r5 PDF | 同上大小与 SHA；本人直接 cmp 返回 **0**，不是视觉相似 |
| 两根实际 pdfinfo | 均 41 页、612×792 pt letter、PDF 1.5；Author 空，无加密、表单或 JavaScript，无创建／修改日期字段 |
| 两根实际 main.aux | LastBodyPage=39；绝对末页=41 |
| 当前 r4 实际全文 pdftotext | 41 个非空物理页；References 唯一开始于第 40 页；无 ?? 或 [?] 未解标记 |
| 本人实际边界图／文本 | 第 1 页为 Anonymous；第 39 页结束完整状态阶证明及限制，第 40–41 页只有参考文献；末页短尾是自然参考文献结束 |
| 两根最终 main.log | 诊断无 Warning、overfull/underfull、缺字、未定义引用、fatal 或实际 rerun 要求；日志终项均为 41 页、546617 bytes |
| 两根 main.blg | 17 entries，warning 调用数 0；plainnat.bst 与 references.bib 与协议一致 |
| 两根实际 pdffonts | 各 23 个 Type 1 字体资源，均 embedded/subset/Unicode=yes |

因此本次实测为 **39 页正文 + 2 页参考文献**，在当前 22–40 页正文窗口内；未扣除任何正文页或假定存在空白封面，参考文献按实际分界另计。
两处 V4 对应旧 overfull 在最终日志已消失；其全页实际可读性由同源全文/PDF 席在 p14、p22–23 分别明确检查。

## 5. 构建与依赖一致性

本人校验双根结果表中的全部 23 个当前产物／控制文件的大小和 SHA，并核验 protocol 中六个控制哈希；均无不一致。
每根仅有约定的四件 stdout：pdfLaTeX 1、BibTeX、pdfLaTeX 2、pdfLaTeX 3；对应两根各件哈希相同且与冻结终态结果表一致。
三个实际 pdfLaTeX 输出依次为 39 页／504596 bytes、41 页／546265 bytes、41 页／546617 bytes；正常引用收敛不被误报为最终缺项。
四 stdout/根、最终日志及 BibTeX 记录无致命失败，与主控记录的八个退出码 0 一致。
“新根执行前缺席、冻结前输入、恰好四过程及无额外重跑”的时间过程证据来自实际执行者已冻结的 protocol／结果；本席不伪称在事后重新观察了历史缺席或再次执行过程。

两份 main.fls 的 PWD 分别准确指向 r4/work 与 r5/work；仅将各自根名规范化后，**全文字节相同**。
每根 153 个唯一 INPUT：13 个本根输入（10 个 TeX 源及本根 main.aux/main.out/main.bbl）和 140 个系统 TeX／字体／配置依赖。
所有所列输入当前均存在；未发现从另一构建根、其他论文或未列入冻结源的工作区文件读取内容。
references.bib 由 BibTeX 日志单独绑定，不假称它必须出现于 pdfLaTeX recorder 的 INPUT 表。
首协议预锁的 14 项选定 class/package/style 逐件重算哈希均一致；其中 13 项由两根 fls 确认加载，plainnat.bst 由两根 blg 确认。
两根日志引擎版本均为预定 pdfTeX 1.40.22／TeX Live 2022/dev/Debian，固定时间呈 1 JAN 1970 00:00；main.tex 的去日期／标识控制仍在。
fls 是实际输入路径记录，不是所有传递依赖的历史字节快照；本结论不扩大为跨机器或不同 TeX 发行版的可复现性。

## 6. 既有审查链与保存证据

| 阶段 | 同对象绑定及独立性判断 |
|---|---|
| V1 完整静审 → V2 文字／引用修订 | 已全文读静态 disposition；原 293 行静审和 95 行 delta 报告的终态 SHA 均核准，作为一个非作者席及其复核，不计两个独立票 |
| V2→V3 编译语法／溢出修复 | 全文读 59 行终态复核，SHA 吻合；未重开未变数学 |
| V3→V4 两处排版／合同 | 82 行终态报告同 SHA 且与本人完整 diff 相符；检查者是 §7–8 转写作者，只核未参与的 §3/§6，不当作 fresh 全稿席 |
| V4 完整实际稿件／PDF | 184 行终态报告 SHA 精确吻合；明确全部十一源 3486 行、逐页 1–41，含末端图、实际 Jacobian、闭 Hasse、Bockstein、两种高层、两次整除和文献页 |
| 本次终局完整性 | 本席与全稿/PDF 席、布局作者、原全稿静审席均不同；核验的是同一 V4、同一 PDF 与完整过程／控制链，不生成新的数学票 |

上述 V4 全文/PDF 报告明确指向当前 source manifest、r4/r5 PDF 大小与 SHA；其检查范围与原锁要求匹配，未把 root 阅读或布局检查冒充本人完整阅读。
必要完整证明、全部量词和来源限制的覆盖来自已闭完整静审＋真实 successor 检查＋本次已终态 V4 全文/PDF 审查；不是从构建成功推出科学正确。

本人只对需确认的旧对象作定向保存检查，没有重扫旧 build 树：

- V1 原十一源全部符合原 snapshot；V2/V3 的十一源各自符合保留 manifest，共 33 项旧源字节吻合。
- 原 publication lock 与原 source-scope lock 均保持记录哈希；科学锁所绑定 brief、证明图、69 项清单本身及正式准入 disposition 的哈希均吻合，未重读／重投 69 件。
- r0/work/main.log 的原 SHA `c65328c029f3d14dc2134c3f16ef7a46bd7b3eecf6298c5ed388455be4d8cef8` 保持；实际仍有第 338 行 Illegal unit 与 fatal 记录，r0 仍无 PDF。
- r2 原 PDF 仍为 546638 bytes、SHA `06a4e848e177b6b69a6593b7894286f55babb1ba09d64b29a1263d926c075d91`；原日志 SHA `1424a5b431c99cc0c303f06d7496320ca4fddb3a01c37f23c2b8352f132f2c8f` 及两条 overfull 保持。
- 首次失败恢复、首次成功但 39>30 的结果、旧独立边界检查及修复复核记录均在，指定 SHA 符合后来冻结记录；没有将旧 r2 PDF 静默改称本次产物。

## 7. 未关闭的限制与最终判断

全文/PDF 席已披露技能附带 pdf_read_preflight.py 因缺 pypdf 返回 `UNAVAILABLE`；其 exit 0 不是结构 PASS。
该可选方法不可用不等于实际 PDF 未读：现有 pdfinfo、aux、pdftotext、字体核验及两次全部 41 页实读共同覆盖所需产物检查。
本席没有重新安装或重跑该脚本，也没有把脚本状态改写为通过。
Vlasenko 勘误内容仍为 `CORRECTION_IMPACT_UNKNOWN`，Beauville 及其他旧来源阅读限制不由本轮关闭；全文席已核其未被转写为本稿必要而未自证的黑箱。
本次不授全球优先权、新意无条件证明、全高层厚度、奇异能级理想、额外分歧态结论或 Route A/B。

未发现需要修源、重编译、撤回终态审查或重新读取不变来源的新硬不一致；结论为 **READY_FOR_LOCAL_ACCEPTANCE**。
主控可据此完成 Paper30 本地接受记录与相应索引处置；本报告自身不改批次计数、不作整批 PASS、不选择或启动 Paper31。
只有当前指定源与 PDF 被覆盖；若它们发生变更，须按实际变化处理，不自动继承此结论。

## 8. 核心终态输入身份

| 文件（相对 notes） | SHA-256 |
|---|---|
| SOURCE_V4_20260909.sha256 | `f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9` |
| PUBLICATION_LOCK_20260909.md | `e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa` |
| PUBLICATION_PAGE_ADDENDUM_V2_20260909.md | `9cc96e76d8bd22dc7b76a4bb35791279c06fd1b83e24c3a74fe136f895a76380` |
| SOURCE_SCOPE_LOCK_V2_20260909.md | `66afedb5efe87a29250d24aa2ba275fe79b1ec6eee727e362b0fc7b2c48df5b2` |
| V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md | `8be634dc8011462a04a247f9ef8d8d76d5a42ebfbcaece35883b010555cb069b` |
| V4_TWO_ROOT_AND_ROOT_PDF_RESULT_V1_20260909.md | `fa993268714b53dcc23751e4bd5c18a90d2a3da80a391cede9fd4dc047627a19` |
| V4_LAYOUT_CONTRACT_DELTA_CHECK_V1_20260909.md | `c4c5a93ffb87242774fa65be1549993245823403d902ed1635ebf0407ac00cb8` |
| V4_COMPLETE_MANUSCRIPT_PDF_REVIEW_V1_20260909.md | `36ae070fe3afb9bfff6b60097d30b66eb381fe2af333fc4d75c2710467730f07` |
| COMPLETE_DRAFT_STATIC_DISPOSITION_V1_20260909.md | `ed7f8d9b04d7aa7516a9b0f6af4a924ab16064fd5b5869d93962adadd0bba95a` |
| BUILD_FIX_DELTA_RECHECK_V1_20260909.md | `ac60f1a3bb9f2909cb09deab6d4bc463e9cc049903e144f376a4e2b3050f890b` |

报告完成后由本人全文读回、核对终态 SHA 后交付并停写；本次无编译、无外部模型、无旧文件改写。
