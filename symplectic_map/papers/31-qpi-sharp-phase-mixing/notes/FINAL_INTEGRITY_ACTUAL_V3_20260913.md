# Paper31：V3 独立终局完整性实际审查

日期：2026-09-13 UTC，实际 clock 已核至 02:29:34。审查者：`/root/p31_final_integrity_v1`。
角色：另一位 fresh 非作者；未参与本稿证明、写作、构建、首轮 source 或 actual PDF 内容审查。
本门只核接受对象、构建、已有实际审查链及锁的一致性，不重做数学、正式四门或查新。
`route_applicability: NOT_APPLICABLE`；实际为 secondary Codex，不冒称外部真人、指定不可用端点或跨模型审稿。

## 1. 结论

- `final_integrity_verdict: PASS`
- `accepted_source_identity: MATCH`；完整 V3 的12件源与两根实际工作副本逐件同一。
- `two_root_pdf_identity: MATCH`；r2/r3 PDF 字节相同。
- `locked_body_window: PASS`；30正文＋1参考文献，原22–30正文合同保持。
- `source_and_actual_pdf_review_chain: COMPLETE_AND_CONSISTENT`；唯一 M1 已关闭，两行 V3 制作修复已实际复查。
- `critical: []`；`major: []`；`minor: []`；`required_fixes: []`。

本门未发现阻止 Paper31 本地接受的完整性问题。主控实际 FULL 接收本报告后，可以依制作锁写本地接受记录、更新成品计数。
本报告不自行改索引、宣布五篇跨论文审查完成或关闭 goal；本次读取的当前入口仍为4/5，整批统一审计须在第五篇接受后另行执行。

## 2. 实际输入、角色与读取边界

本人 FULL 读工作区 `AGENTS.md` 28行、`docs/WORKFLOW.md` 39行，及 paper-compile `SKILL.md` 全251行。
该技能仅用于实际页界、字体、日志与匿名性核验；明确的只读任务和项目锁覆盖其默认清理、latexmk、重编译、会议页数、附录移证及投稿建议。
没有执行这些不适用步骤。项目 README 本次 FULL 读26行；BATCH_07_CONTEXT 仅 PARTIAL 1–65，未读整份历史。

以下记录均由本人本轮 FULL 读至 EOF，并对实际整件核 SHA；未把父代理摘要当作原件阅读。

| 输入（notes 下，另注明者除外） | 行 / bytes | SHA-256 |
|---|---:|---|
| [科学锁 V1](SOURCE_SCOPE_LOCK_V1_20260913.md) | 104 / 8906 | `b056a664863e41cf778225118ea719a3e43b4a78c451d302703f423c931dd584` |
| [制作锁 V1](PUBLICATION_LOCK_V1_20260913.md) | 72 / 6208 | `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c` |
| [首次完整源审查 V1](COMPLETE_SOURCE_ACTUAL_REVIEW_V1_20260913.md) | 177 / 18603 | `c2f15cd1dbe8ee2ccb3dfe85dfd2ea408b608f3403a38dcb4417063835fa990b` |
| [M1 实际续查 V2](SOURCE_M1_SUCCESSOR_REVIEW_V2_20260913.md) | 93 / 9156 | `1360aa0267dc69f76ecd3f58c2d56d27fda84b5410cd6edf3c60ef48edc23bfb` |
| [完整源处置 V2](COMPLETE_SOURCE_DISPOSITION_V2_20260913.md) | 51 / 3994 | `738a2a3422c3321d67fff185898770b03de365b121a8fd0054c94b94b84d6b92` |
| [首次构建协议 V1](NATURAL_BUILD_PROTOCOL_V1_20260913.md) | 42 / 4303 | `436d1fe42cc1e29fabf4fe16f60921462c710ea33c39a5d4de6d53aa8c668bb4` |
| [r0 诊断与 V3 恢复协议](R0_DIAGNOSIS_AND_V3_RECOVERY_PROTOCOL_20260913.md) | 61 / 4707 | `32b8f727e4284af0b3427380f3c74daad95111f212bfc097661e860094b469b9` |
| [主控制作及全页记录 V3](NATURAL_BUILD_AND_ROOT_PDF_CHECK_V3_20260913.md) | 69 / 5865 | `3b4ed9f70a1b07194b803ecdf9d87e6b4febdd163cf47546ead79621587ebb3a` |
| [独立 actual 稿件/PDF 审查 V3](ACTUAL_SOURCE_PDF_REVIEW_V3_20260913.md) | 146 / 16104 | `d91d59eb7e591f0b2f5b47e65b8931f7789aad07d54a1cfb96a55ba9e72d1be8` |
| [主控 actual PDF 门处置 V3](PDF_ACCEPTANCE_DISPOSITION_V3_20260913.md) | 41 / 2898 | `305c5489393517638e3bb5dbb3d926428fd2246eeabb52b36bbea0bd3fb9c13e` |
| [工具链清单 V1](BUILD_TOOLCHAIN_INVENTORY_V1_20260913.md) | 102 / 7484 | `d705e5cf18670c497291f1fc94e8b4b8c2c99c8968b9adc359e2db7c9cbf4e9b` |
| [scripts/build_natural_v2.sh](../scripts/build_natural_v2.sh) | 64 / 2656 | `016eb9530c36ec27b3c6bc17b1988b4ddbab1bd426009e282a785efd861b297f` |
| [正式双席处置](../../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md) | 126 / 10187 | `8693108fec4c8aa35310d40fd86c19e36429f79a1f46f225b2415e97f93e5ef7` |

本人另 FULL 读 V3 `main.tex` 41行、`math_commands.tex` 17行、`references.bib` 70行、V3 源清单12行，
以及完整 V2→V3 目录差分。其余九个章节本轮只作身份/定向命令检索，不冒称再次 FULL 阅读数学正文。
实际 PDF 本人亲看第1、19、25、30、31页完整页图，并读第30–31页全部提取文字；这是选页终验，不冒称本人又读全部31页。
全部31页的先前独立实际内容阅读，由上表146行报告及其准确输入身份承担；该席逐页图像、逐页全文及31页独立重渲染比对的范围陈述没有被扩大。

辅助只读席 `/root/p31_final_integrity_v1/p31_final_identity_readonly` 复核12件源、双根 PDF/清单和差分；其下另有一席只核 v2/v3 文件集合/差分。
辅助席均未写文件或审数学/PDF内容；关键清单校验、差分、PDF cmp、报告读取及页面判断也由本人亲自执行。
本报告的独立终局判断由本人承担，不把辅助结果伪报为另一张正式数学或完整内容票。

## 3. 接受源与审查链的实际对应

完整 V3 实测12件、2454行／108359 bytes；[SOURCE_V3_20260913.sha256](SOURCE_V3_20260913.sha256) 为12行／1164 bytes，
SHA `4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8`。
本人对 `paper/v3/`、`r2/work/`、`r3/work/` 分别执行 `sha256sum --strict -c`，各12/12 OK；两根 source.sha256 与原清单身份相同。
另按首次177行报告的实际12行源身份表读取 V1 文件并计算 SHA，12/12 MATCH；原 V2 对其冻结清单校核亦12/12 OK。
V2 清单 SHA 仍为 `9f61d249df26d8997690be71d2d24f5d0f3727e07c4159bc4a78aa66a91cd89f`。

本人 FULL 读实际 `diff -ru paper/v2 paper/v3`：只有 §5:248 一行措辞缩短、§6:276 一行 texorpdfstring 书签包装，另外10件字节不变。
具体是 “They commute and have bounded...” → “They commute, with bounded...”，以及保持数学显示的 `T=3/16` 纯文本书签。
main 和 §3 未改；引言、§2 的全实 lift 修正和七项书目未改；没有删正文证明、改量词/定义域、挪附录或变更版式。

源审查责任接续真实：首轮 FULL V1 是 `SCOPED_SOURCE_CORRECTION_REQUIRED`，不能追记成无条件 PASS；唯一 M1 是 lift 来源归属。
93行 V2 续查只对真实变动及原局部式核验，明确 M1 CLOSED；其余源未变，故可与首次 FULL 读合成源门通过。
146行 V3 报告再核两处真实制作变更和实际全部31页，没有冒称局部复查等于第二次 FULL 源。
主控41行处置只接受 actual source/PDF 门，并保留本终局门待审，不抢记第五篇。

正式准入两席身份本轮只核 SHA：R1 `ec9a0b743ca404d5e0c6dcde8a66252f3fd4df4c03f5a61df22818e25ceb74d3`、
R2 `318e71b4a3d97dc48c3dc19d3d2ad52a6defd737bf7e5529b8e82e14645edf76`，均与126行正式处置一致。
本轮未重读两席全文或38件数学祖先，不重投新意/价值/证明/容量票；它们与英文源门、制作门、实际PDF门、本门是不同阶段。
原六项引用记录 SHA `85be5a08f81484538fce6190d79901726a288a09060fb83dc528766732dd7947`、lift补充 SHA `680f1016a6caa1b220591e41507b31c4637415202057f700b0adb5d8a024c6cb` 本轮仅核身份；未重新联网读七篇外文。

## 4. 双根、命令、依赖与失败保留

[r2 PDF](../build/natural-20260913-r2/work/main.pdf) 与 [r3 PDF](../build/natural-20260913-r3/work/main.pdf) 各528155 bytes，
本人 `cmp` 退出0，两者 SHA 均为 `fc5d4419b6ddd2d9faf9ebb08b5319a3e249432c332944eb506f645857257640`。
两根最后一遍 `logs/04-pdflatex.main.pdf` 与各自 work/main.pdf 也分别 cmp 同一，接受对象不是另行替换的一份 PDF。

本人实际读取两根全部八个单行命令、八个退出码及两份8行 environment；命令序列各为：

```text
/usr/bin/pdflatex -fmt=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
/usr/bin/bibtex main
同一 pdfLaTeX 命令
同一 pdfLaTeX 命令
```

八个退出码全0。环境固定 SOURCE_DATE_EPOCH=0、FORCE_SOURCE_DATE=1、TZ=UTC、LC_ALL=C、
TEXINPUTS/BIBINPUTS/BSTINPUTS 为 `.:`、TEXFORMATS 为 `/var/lib/texmf/web2c/pdftex`。
64行脚本先拒绝已存在根、校验源，再复制完整源；只包含四次 run_pass，无 retry/clean 或复制旧 aux 的分支。
两根第一遍日志各在389行记 `No file main.aux.`、1093行记 `No file main.bbl.`；保存的正常首遍未定义引用未被抹除。
实际 logs 文件集合、八条命令及逐遍快照支持所记四遍收敛；未发现额外重跑或旧辅助文件混入的证据，不把这些本地记录夸大为全系统操作追踪。

两根 final recorder 的绝对 INPUT 以 `awk` 提取、C locale排序去重后，分别与保存 absolute-inputs.txt cmp 一致，各144项。
两份 absolute-inputs.sha256 字节相同，SHA `b463baff29948284177c09370c2e0d93aade3745f487d57c95b2a7578b69978b`。
本轮没有再次扫描这144个外部依赖的内容；既有主控/actual报告的逐项核验保留。清单边界是实际TeX绝对输入，不是OS动态库或BibTeX全部输入胶囊。
本人亲读 r2 main.blg 全部记录：plainnat.bst、references.bib、7 entries，warning$=0；TeX相对输入记录覆盖main、宏、九节及当根生成的aux/out/bbl。
另实核格式 SHA `5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0`、plainnat.bst SHA `21eefa76f1c967f5074776fcef096c0f8f2b9e42347e84b62e1dbb121dcae486`，仍与冻结inventory一致；bib由12源身份链覆盖。

r0 后处理失败没有被删除或冒作接受根：原 PDF SHA 仍 `fda521e298843de060c3582df46ce9541ea61d31ef7067203377f87ca1808c4f`。
本人逐件 cmp 三份 diagnostics/pdflatex.fmt39469/39483/39497.fls 与原格式目录同名文件，全部相同；三份PWD均指向r0/work。
其SHA依次为 `809be83ba75dbd49c05e7cc15f9b214e79b9809b780a9f5a0e5201451d4ac364`、`f103a65cf53805d2d7d7da6917fb7316d7103864b584b5d7a221fdf6cfd78756`、同前。
EXDEV原因在61行诊断中明确为基于跨设备/rename逻辑的推定，本轮不冒称运行追踪验证errno；恢复只改格式名路径，仍用原格式。
旧脚本V1实存且SHA仍 `e2fc648804d39c61a0dd5d6f43f8692d1685a1da5bce8894faed89faefb7e116`；V1/V2原稿与两锁均保持。
本人实际 `test ! -e .../natural-20260913-r1` 为真：r1未执行，不是通过；被接受的独立新根明确为r2/r3。

## 5. 本人实际页界、字体与选页终验

重新执行 pdfinfo/pdffonts 得31页、letter 612×792pt、PDF1.5、无加密、Author空且无CreationDate/ModDate；26项字体全为Type1，emb/sub/uni全yes。
源 main 明定11pt article、单栏、四边1inch；实际geometry日志为左右/上下72.26999 TeX pt，吻合1inch，没有隐改边距。
全源定向搜索只命中结论后的唯一 clearpage；未见 appendix、新正文分页、缩字/缩行距或填页指令。
两根 aux 中 LastBodyPage均30，bibcite均七项；实际第30页只有非空结论，第31页以References开始且包含七条完整书目。
自然结论页较短不是空白页或隐藏分页，仍按合同计正文30页；不把P30的40页例外迁移给P31。

本人亲看第1、19、25、30、31页130dpi完整单页图：匿名标题及摘要/表1正常，§5已修行在正文框内，§6数学标题显示正确，结论和参考文献没有裁切或重叠。
每张图均另从实际r2 PDF执行 `pdftoppm -f N -l N -singlefile -r 130 -png` 输出至stdout，与已有对应PNG逐页cmp，5/5字节相同；未生成或覆盖新图文件。
这验证本人所看的选页确出自接受PDF；并不冒称又重渲染或亲读另外26页。完整31页视觉与必要证明落点由此前fresh actual报告承担。

本人对两根 final main.log/main.blg 定向检索 Warning/Error/Overfull/Underfull/Missing/undefined，无命中；对实际PDF全文提取定向检索 `??`、`[?]`、`[VERIFY]`、TODO、/root/、PASS/FAIL，亦无命中。
日志和全文这里只是指定风险扫描，不记为逐行FULL内容阅读。书目原本的真实作者名不违背本稿匿名；本地P30条目清楚写Anonymous/unpublished/version4。
没有未处置制作问题或需要改变原科学量词、完整必要证明、22–30页合同的新证据。

## 6. 交付效力与停止

本次唯一新增文件为本报告；没有编辑源、锁、脚本、旧报告、日志、索引或已接受产物，没有编译、清理、安装、联网、CAS、数值/参数阶数枚举或外部操作。
所核直接记录与产物均真实存在、身份相符；没有重扫P27–30旧构建树、加载38件祖先包或新建通用基建。
已按实际任务区分FULL/PARTIAL/身份核验/搜索/选页显示；没有为了凑项新增finding或验收门。
本报告交付前由本人FULL读回至EOF，最终行数/bytes/SHA在交付消息绑定，避免自指哈希。
主控接受本门后可完成Paper31本地交付；之后的五篇统一审计仍是独立下一项，当前不预授完成。
交付后停止编辑，除非收到针对真实后续变化的明确任务。
