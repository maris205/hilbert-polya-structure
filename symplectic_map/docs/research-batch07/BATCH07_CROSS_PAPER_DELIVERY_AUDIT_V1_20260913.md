# Batch07 五篇接受产物与合同一致性审计 V1

日期：2026-09-13 UTC。审计席：`/root/batch07_cross_delivery_v1`，独立于本轮主控索引／总处置及另一科学席。
对象：Papers27–31 各自最新本地接受记录指向的精确源、主 PDF、独立根 PDF 与终态审查链。
结论：`CROSS_PAPER_DELIVERY_AND_CONTRACT_PASS`；`required_fixes: []`（本交付／合同域）。
另有一组非阻断书目作者字段错误 BIB-01，见 §6；不是“全部书目零差异”，也不把原冻结接受记录改称无瑕疵证书。
本报告不是第三份科学评分、重新查新、全证明复验或新增全页 PDF 审查；不单独授予整批科学审计 PASS 或关闭 goal。

## 1. 实际范围与方法

本人 FULL 读取工作区 `AGENTS.md` 与 `docs/WORKFLOW.md`。批次入口仅 PARTIAL 读取当前首部和历史标记；没有整份加载历史账本。
根 README／BATCH 当前首部为 5/5、跨审进行中，旧 4/5／待验收已明确标作历史；P29／P30 README 本轮也已注明其 3/5／4/5 为原接受阶段。
索引最终完成状态由主控在接收两席后单独处置，本报告不要求改写冻结的旧阶段快照。

以下五份最新接受记录均亲自 FULL 读至 EOF，并重新计算整件 SHA；没有以父代理摘要代替阅读。

| 论文 | 接受记录（相对各项目 notes） | 行 / bytes | 本轮 SHA-256 |
|---|---|---:|---|
| P27 | [LOCAL_ACCEPTANCE_20260905.md](../../papers/27-positive-newton-translation-reciprocity/notes/LOCAL_ACCEPTANCE_20260905.md) | 41 / 6146 | `c74faa836e06b700b5b41ed40df50435100adb25226b034f4e2bf101db2828ce` |
| P28 | [LOCAL_ACCEPTANCE_SUCCESSOR_20260905.md](../../papers/28-primitive-selector-cycle-monodromy/notes/LOCAL_ACCEPTANCE_SUCCESSOR_20260905.md) | 80 / 4544 | `9f0bb26d43ed68e5d7732b31c784facd2186d6bc15d4527cfdef1a9fbcbad27c` |
| P29 | [LOCAL_ACCEPTANCE_20260906.md](../../papers/29-filtered-henon-cohomology/notes/LOCAL_ACCEPTANCE_20260906.md) | 66 / 4911 | `efb0f0058ae55ab1ffb681581838df1b652985ed2d647ad0a3fbda467245c017` |
| P30 | [LOCAL_ACCEPTANCE_20260909.md](../../papers/30-qpi-vertical-critical-ideals/notes/LOCAL_ACCEPTANCE_20260909.md) | 108 / 8513 | `cfb2f9e034716545fd22d9e7024d7b9b62d89350c3eecc97852870b17f094a52` |
| P31 | [LOCAL_ACCEPTANCE_V3_20260913.md](../../papers/31-qpi-sharp-phase-mixing/notes/LOCAL_ACCEPTANCE_V3_20260913.md) | 56 / 5044 | `179ed9984de2c3e020e690dac11f14b6ebf981a1ec9356e9f5006b8040baa618` |

实际检查是定向 `sha256sum`、`sha256sum -c`、源文件集合比较、`stat`、`wc`、主／双 PDF 的直接 `cmp`、`pdfinfo`、`pdffonts`，以及末正文页至文献末页的 `pdftotext -layout` 输出亲读。
所有命令只读；未执行 TeX/BibTeX、旧 builder／validator、重渲染、旧根全树或外部依赖扫描、网络检索、科学数值或 CAS。
整件 SHA 读取不记为数学内容 FULL；pdfinfo／字体检查和页界文字不记为全页视觉 FULL。
最初按后篇习惯推测的 P27 root 内 acceptance.json、P28 work 内源路径不存在；随后按实际终审／脚本路径定位，仅作定向读取完成绑定。
这两个定位失误不构成产物缺失；P27 acceptance 在 evidence/r0,r1，P28 原设计使用只读外部源而非 work 源副本。`jq` 不可用后用本地 Perl JSON::PP 只读选字段，未安装依赖。

## 2. 精确交付矩阵与实测页界

以下路径全部相对于所列项目目录；双根 PDF 均实际存在，大小、SHA 与接受记录相符，每组直接 `cmp` 退出 0。

| 论文 / 项目 | 接受主 PDF；独立根 PDF | bytes（各） | 正文＋文献＝总页 | 有效正文窗 | 结论 |
|---|---|---:|---|---|---|
| P27 `27-positive-newton-translation-reciprocity` | `build/final-20260905-r0/main.pdf`；`build/final-20260905-r1/main.pdf` | 336871 | 27＋2＝29 | **24–28** | MATCH / PASS |
| P28 `28-primitive-selector-cycle-monodromy` | `build-capsule-successor-20260905/r0/work/main.pdf`；`r1/work/main.pdf`（同 capsule） | 836405 | 23＋2＝25 | 22–30 | MATCH / PASS |
| P29 `29-filtered-henon-cohomology` | `build/natural-20260906-r0/work/main.pdf`；`build/natural-20260906-r1/work/main.pdf` | 438693 | 26＋1＝27 | 22–30 | MATCH / PASS |
| P30 `30-qpi-vertical-critical-ideals` | `build/natural-20260909-r4/work/main.pdf`；`build/natural-20260909-r5/work/main.pdf` | 546617 | 39＋2＝41 | **22–40，仅本篇** | MATCH / PASS |
| P31 `31-qpi-sharp-phase-mixing` | `build/natural-20260913-r2/work/main.pdf`；`build/natural-20260913-r3/work/main.pdf` | 528155 | 30＋1＝31 | 22–30 | MATCH / PASS |

| 论文 | 双 PDF 的共同实测 SHA-256 |
|---|---|
| P27 | `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4` |
| P28 | `ebbd943cba592de21658248779ea3fb4da2cbcbf9a297131df5a358e731b38ca` |
| P29 | `774865fa38e7d6f053daf57a48a03da3eb52edf940694f1fa6c116287bd966e0` |
| P30 | `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |
| P31 | `fc5d4419b6ddd2d9faf9ebb08b5319a3e249432c332944eb506f645857257640` |

本人读取 P27 页27–29、P28 页23–25、P29 页26–27、P30 页39–41、P31 页30–31 的全部提取文字。
五篇末正文页均实际含结论／证明／范围说明；References 分别从28、24、27、40、31起，后缀仅文献，没有把总页数当正文或藏后参考文献证明。
P31 第30页是非空结论自然短页，不是未读条件下推测的空白页；正文实质性与无填页的完整视觉证据仍由既有 actual 报告承担。
五篇主 PDF 均实际为 letter 612×792 pt、PDF1.5、未加密、无表单／JavaScript；字体资源分别22、22、20、23、26，全部 embedded。
这些输出没有被夸大为新一次所有公式可读性或每个 PDF 对象的安全解析。

## 3. 接受源的精确绑定

P27 以任一 final root 中的三件为自包含接受源；另核 layout main 与原宏／书目。原 paper/main.tex 仍为 `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`，不冒称它就是接受排版 main。

| P27 文件 | 行 / bytes | 两 final root 及相应源的实测 SHA-256 |
|---|---:|---|
| main.tex | 1690 / 55110 | `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8` |
| math_commands.tex | 17 / 601 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| references.bib | 217 / 6610 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

P28 精确源是 `paper-successor-20260905/` 的三件，实际目录恰为三件。
本人重算三件身份，并亲读双根已封存 acceptance.json 的 source_hashes；两份三键映射均与实源及正式接受表完全相符。
没有凭不存在的 work 源副本断言构建不一致；只读挂载和历史 before/after 输入图由已绑定153行终审记录承担，本轮不重扫6908项／约314MB资源树。

| P28 文件 | 行 / bytes | 实测 SHA-256 |
|---|---:|---|
| main.tex | 1855 / 84983 | `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9` |
| math_commands.tex | 14 / 444 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
| references.bib | 204 / 6104 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

P29–P31 各自实际源目录恰等于下面完整源清单，且原接受源与两个接受 work 副本均逐件 `sha256sum -c` 为 OK。
这些只读副本校验共36＋33＋36＝105项；不重新扫描其他构建根或系统依赖。

| 论文 | 接受完整源 | 文件 / 行 / bytes | 完整清单及其本轮 SHA-256 |
|---|---|---:|---|
| P29 | `paper-successor-20260906-transcription-v1/` | 12 / 2124 / 87260 | `SOURCE_BUILD_MANIFEST_20260906.sha256`：`958dd5be31db838485feff5512ac675960ce7caa296f02c1f05b82b6b87e01ee` |
| P30 | `paper/v4/` | 11 / 3486 / 145249 | `SOURCE_V4_20260909.sha256`：`f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9` |
| P31 | `paper/v3/` | 12 / 2454 / 108359 | `SOURCE_V3_20260913.sha256`：`4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8` |

本人另 FULL 读 P29/P30/P31 实际 main.tex（49/62/41行），PARTIAL 读 P27 main 1–38、P28 main 1–30。
P28–P31 明定 article11pt/letter/1inch；P27 保留其既有11pt article、原包及原间距设置，不追施后篇统一geometry／metadata规范。
正文数学文件除上述入口／局部以外仅作身份或清单核验，不能将本节称为本轮全文证明审查。

## 4. 实际内容门与独立终局门的终态绑定

下表报告均重算整件 SHA，匹配接受记录。FULL/PARTIAL 是**本席这次对报告文本的读取范围**；报告中记载的原审查员实际全文／全页覆盖仍按其原作用域使用。

| 论文 | 终态证据（相对各 notes） | 本席阅读 | SHA-256 |
|---|---|---|---|
| P27 | `LAYOUT_OUTPUT_20260905_DIAGNOSTIC_REVIEW.md` | FULL 62行 | `864ebc1a85860e6b7f269456410876ea80a1e3592528d6992996b9d38def4378` |
| P27 | `LAYOUT_VISUAL_20260905.md` | FULL 15行；未新看29图 | `0533677ed5bdfb5b6ec6c96f63dfb208c3b559d2bc40d8e19438435fbfd17c10` |
| P27 | `FINAL_ARTIFACT_AUDIT_20260905.md` | FULL 153行 | `007db977cf65444761b71e98a6d26123b3c335bc3585e7a88ebabcab05936ba3` |
| P28 | `FINAL_PDF_SUCCESSOR_REVIEW_20260905.md` | FULL 153行 | `8a27036539f0a967430eb01438c12b216d005829bff4a0899a8cf7220419f748` |
| P29 | `ACTUAL_PDF_INDEPENDENT_REVIEW_20260906.md` | PARTIAL 1–95、156–197 | `58ffb3387012441260413262035b8b5be183ab9896842b77223f4a2694e5a457` |
| P29 | `FINAL_INTEGRITY_REVIEW_20260906.md` | PARTIAL 1–95、213–281 | `293299c0022ea8cd50138ccb8ea50c91849fc9ced5b123d86bfeba5c3d01471b` |
| P30 | `V4_COMPLETE_MANUSCRIPT_PDF_REVIEW_V1_20260909.md` | PARTIAL 1–64、140–184 | `36ae070fe3afb9bfff6b60097d30b66eb381fe2af333fc4d75c2710467730f07` |
| P30 | `FINAL_INTEGRITY_REVIEW_V1_20260909.md` | FULL 142行 | `dec4223bd56ef139cd26d9d5467137c63f3227331c5924d2cd42cd30cfc82534` |
| P31 | `ACTUAL_SOURCE_PDF_REVIEW_V3_20260913.md` | PARTIAL 1–59、112–146 | `d91d59eb7e591f0b2f5b47e65b8931f7789aad07d54a1cfb96a55ba9e72d1be8` |
| P31 | `FINAL_INTEGRITY_ACTUAL_V3_20260913.md` | FULL 132行 | `0cf2b56814764351e763e6fcffea1656bf1543004d5b642443d527e79f380a03` |

- P27：独立内容／警告审查 PASS 与主控全部29页、72dpi视觉记录同一PDF SHA；最终独立技术审计按明确目录谓词条件 PASS，后续用户确认与rebind由本地接受记录消费。不存在未解决的该确认义务。原视觉不是fresh非作者全29页，不追溯改称后篇式角色合同。
- P28：终态报告把全部25页亲看和本地交付完整性合并在该独立席，给 `FINAL_PDF_SUCCESSOR_REVIEW_PASS / INDEPENDENT_LOCAL_ACCEPTANCE_READY`；原controller和validator的visual pending是其先前阶段快照，不是当前未闭门。
- P29：独立actual席亲读全12源及27页，随后不同非作者作终局完整性；两报告均无CRITICAL/MAJOR/MINOR。摘要D≥1唯一修复由 `SOURCE_TRANSCRIPTION_FIX_RECEIPT_20260906.md` FULL30行、SHA `cda53a4bb6c150c490958989ac96915c44dab5463c8e36b071538ed5ec329b30` 明确关闭。
- P30：fresh完整稿/PDF席亲读11源及41页；后续另一非作者最终报告为 `READY_FOR_LOCAL_ACCEPTANCE`，无必修源/PDF问题。曾任§7–8作者的局部布局检查者没有冒充fresh完整稿席；两独查原先有界接口盘点已披露，不称盲审或跨模型。
- P31：首次FULL V1源＋V2真实M1修正＋V3两行制作变化＋actual全部31页形成合成内容PASS；不冒称actual席又FULL读了一遍12源。另一fresh非作者的终局门PASS、required_fixes空。本人FULL读51行 `COMPLETE_SOURCE_DISPOSITION_V2_20260913.md`，SHA `738a2a3422c3321d67fff185898770b03de365b121a8fd0054c94b94b84d6b92`，明确原V1需修及M1已闭。

本轮定向核准的状态记录还包括：P27 evidence/r0、r1 的 acceptance.json 均SHA `8022e67263546aed1447119f16d80351080750a38e5862f82590b88efacff69f`；
P28 两 work/report/acceptance.json 均SHA `d191787beede459620fdc1b4192246a65e1dbe0d7120673bad6fcec2deeb99f3`，automated PASS、findings空；
P28 evidence/outcome.json SHA `ff4e9440a4b055a78135996bcd9ebd70ac1b492054af5277b218f9a4531faa5b`。
不回写这些先行记录的 pending，不以本轮只读检查声称重新运行了250项seal或全部stage验证。

## 5. 合同例外、失败真值与保留边界

| 论文 | 亲读的有效合同范围 | 必须保留的真实处置 |
|---|---|---|
| P27 | successor publication lock必要PARTIAL：1–57、234–262、354–392；local delivery supplement FULL39行；最新接受FULL | 正文24–28未改。用户只批准跨根显式dir行的自身st_size不比较；目录结构/模式/链接数/成员/空缓存及全部文件字段仍要求。只读技术PASS＋确认后rebind形成本地接受，非新builder PASS。 |
| P28 | publication lock必要PARTIAL：1–55、340–480；successor接受FULL；源增补独审PARTIAL195–239 | 原22–30不变，三处增补是已核实的证明/解码细节，不是新headline或改页式。原稿、旧失败、controller pending均保留，由后继终态消费。 |
| P29 | publication lock FULL48行；scope amendment FULL24行 | 用户允许在原容量双PASS不齐时一次自然完整成稿取证；实测26页通过，但原R2容量FAIL及候选合取FAIL不重评分，不把此例外传递P30/P31。 |
| P30 | publication lock FULL72行；page addendum V2 FULL53行 | 用户明确仅本篇30→40。原r0 fatal仍无PDF；原r2为39>30失败及两overflow，V4/r4,r5是后来合同下的新产物。 |
| P31 | publication lock V1 FULL72行；源V2处置FULL及实际终态链 | 原22–30不变。V1的M1不是追记PASS；r0四遍TeX成功但后处理失败，r1未执行不计通过；接受的是V3/r2,r3。 |

P27 supplement SHA `ceea8192167cdd7ca26c416b4067ac0e15f285879e88d1872706b2a26166df42` 与 successor publication SHA `779b8196c59aeed992016cbba855d99b83ba46d294aacb2e7242fa8089d24612` 均本轮核同。
P27 原 failure.json 实测SHA `178e3f2e49e05c17b21f24bcd041d94f9fffe6ea460414137c253a18d8ba8140` 未变；原builder仍 **exit1 / FAIL_PRESERVED_NO_RETRY / CROSS_MANIFEST:R009**，没有虚构clean end-to-end成功。
P30原publication SHA `e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa`、唯一页窗增补SHA `9cc96e76d8bd22dc7b76a4bb35791279c06fd1b83e24c3a74fe136f895a76380`，P31publication SHA `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c` 均本轮MATCH。

P27十八项、P28七项underfull分别已有逐项可读性处置，不能汇总成“五篇都无任何warning”。P29–31当前最终日志的无未处置诊断由同源既有actual／终审承担。
P30可选结构脚本缺pypdf的 `UNAVAILABLE` 未重标PASS；实际41页完整读与现有工具证据仍在。
P30 Vlasenko `CORRECTION_IMPACT_UNKNOWN` 及其他既有外文实读范围不由本次关闭；它们没有被偷换成新全局新意保证。
所有原稿、旧失败的总体保存判断限于既有终态审查证据和本次所列定向身份，不冒称本席重新取证整个历史文件系统。

## 6. 非阻断书目字段发现 BIB-01

页界及文献后缀检查实际读到三条跨篇同一来源的作者字段差异：

| P27接受PDF条目 | P27冻结文字 | P28对应条目文字 | 本席处置 |
|---|---|---|---|
| [14] Degree-growth of monomial maps，2007 | B. Hasselblatt and T. Propp | [9] Boris Hasselblatt and James Propp | 已由附属勘误提供正确字段；外部核验归主控 |
| [15] Polynomial symplectomorphisms，2008 | J. Janeczko and Z. Jelonek | [13] Stanisław Janeczko and Zbigniew Jelonek | 同上 |
| [19] 同一 arXiv:2509.14584 | Y. Shao and Y. Sun | [17] Enbo Shao and Xiaosong Sun | 同上 |

本席没有访问外网，不能把P28文字本身当作作者真值证明。主控的一次有界一手metadata检查确认这三项P27作者字段错误，并以另存书目勘误伴随记录处理。
本人随后 FULL 读 [P27书目勘误](../../papers/27-positive-newton-translation-reciprocity/notes/BIBLIOGRAPHIC_ERRATA_V1_20260913.md) 全36行／3705 bytes，实际SHA为 `065896f56ba8d41135fe99ebc04a3a2428f5730ac13be9b8610badd65062cf1f`。
勘误明确绑定本报告已实核的P27接受PDF、references.bib及原接受记录的三个SHA；表中对象与本席页界观察对应。其主控实际外部读取范围仅身份页作者行／作者学校目录与论文首页，不倒签为本席亲读或三文全文。
当前附属交付已经提供三条正确作者信息，不再留作待处理项；原PDF中的字母确实未修改。该记录不改接受PDF、源、锁或旧接受文档，亦不授权重编译。
这里保留发现的存在，不宣称五篇书目完全一致。它不是PDF身份漂移、页数合同违反、数学证明缺失或原目录恢复确认未完成，故不阻断本交付／合同域PASS。
若将来需要把勘误嵌回冻结P27论文，应另按其新版本／恢复边界处理，不能在本轮借勘误覆盖原稿或重跑受限构建。

## 7. 最终交付结论与停止

五篇接受对象与各自实测页窗、同源双根、actual报告和最终独立完整性终态相容，均有本地接受记录。当前成品计数确为5/5。
`delivery_identity_findings: []`；`contract_blockers: []`；`unresolved_required_acceptance_fixes: []`；`nonblocking_bibliographic_findings: [BIB-01（三项作者字段）]`。
P27恢复谓词确认、P29自然成稿例外、P30独有40页上限均按用户后来明确决定理解；没有新造重复许可请求，也不将特例外推。
本结论不改另一科学席的独立贡献／共享归属判断，不授Route A/B层级PASS；五篇为纯数学本地交付，Route适用性与产物状态分开。
没有投稿、上传、托管、push、外部发信或付费资源效力；本席只新增本报告，未改任何其他文件。
主控接收本报告和独立科学报告后作统一处置与索引更新，再按约定汇报并暂停；本席不代替该最终合取。
报告最终FULL读回及行数／bytes／SHA由交付消息记录，避免自指哈希；交付后停止编辑。
