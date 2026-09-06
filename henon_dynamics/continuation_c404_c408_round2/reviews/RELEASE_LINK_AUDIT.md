# 最终本地链接与发布索引一致性审计

日期：2026-09-06。审查者为独立分配的 nonlinear-return 团队代理，
不是 README 或 FINAL_BUILD_REPORT 的作者。

结论：**未发现意外断链、主 PDF 数据不一致或发布索引范围串用。**
两份封存清单在本审计时尚未生成，单列为待协调者封存后核验；
本报告不宣称载荷已经封存或 Git 已同步。

## 1. 实际检查范围与方法

工作树为 `henon_dynamics/continuation_c404_c408_round2/`。
用 `rg --files --hidden --no-ignore -g '*.md'` 枚举目录内全部
Markdown，而非只检查默认未忽略文件。对全部文件内容执行本地链接
提取和目标存在性检查，按各 Markdown 所在目录解析相对路径；
围栏代码和行内代码中的数学区间等不作为链接。另行检查引用式链接
定义及 HTML 链接标记，没有需要另行解析的本地目标。

人工完整核对了当前 README、FINAL_BUILD_REPORT、EVALUATION_SCOPE、
ADMISSION_AND_BATCH_PLAN、SCOUT_PLAN，以及三份共 297 行的 Route A
YAML；还核对两份独立范围审计中与标签、缺额及阶段性状态有关的段落。
对其他 Markdown 的读取仅用于链接检查，不冒称本次重新审查了其数学
或外部文献。三份实际主 PDF 分别用 `pdfinfo`、`stat` 和 `sha256sum`
读取页数、字节数和摘要；没有重新编译、渲染或运行数学程序。

检查使用现有 Node 标准库的只读内存脚本及文本字段提取，没有新增
发布程序、安装依赖或重新运行正式 evaluator。107 处外部链接目标
未访问，也未判定其在线可用性。

只新增本文件，未修改任何已有文件。协调者在审计期间为 README
补入本报告的链接后，明确停止修改 README；以下绑定采用该最终版本。
本文件落盘后再次检查时，总范围为 39 份 Markdown（原有 38 份加本报告）。

原有 38 份 Markdown 覆盖分组：批目录顶层 5；arithmetic_forms 及
其 paper 子目录 6；critical_delta 及其 paper 子目录 5；
henon_resonance 及其 paper 子目录 8；nonlinear_geometry 3；
reviews 5；wild_dynamics 6。本报告是末次扫描新增的第 39 份。

## 2. 链接结果与尚未生成的目标

最终扫描共识别 **59 处本地链接**：**57 处目标存在，2 处明确预留，
0 处意外缺失**。没有仅含页内锚点的链接。各现存目标本身不是符号
链接；这不是对全载荷所有文件或所有父目录的符号链接封存审计。

| 预留目标，相对本批目录 | 本次实测 | 后续责任 |
|---|---|---|
| `PAYLOAD_FILES.txt` | 不存在，未生成 | 协调者生成精确成员表后核验 |
| `MANIFEST.sha256` | 不存在，未生成 | 协调者生成摘要清单后核验 |

两项均由 README 链接，正是本次任务指定的唯二预留目标。没有将其
计入“存在”，也没有把预期的生成时序误报为意外断链。本报告本身
已经落盘，README 指向 `reviews/RELEASE_LINK_AUDIT.md` 的新链接
在末次检查时存在。

部分现存链接指向本批目录外的首轮记录、C399–C403 包、既有证明
或共享 CURRENT 入口。它们在当前仓库内存在；README 已明确这些
对象不属于本批载荷树。本检查不承诺仅复制本批子目录后这些跨包链接
仍可离线使用，也不验证树外文件的旧封存或 Git 状态。

## 3. 三份主 PDF 与最终构建表

以下为实际文件重新读取的值；逐项与 FINAL_BUILD_REPORT 两张表及
README 页数一致，页数合计 **33**。

| 稿件 / 主 PDF | 页数 | bytes | SHA-256 |
|---|---:|---:|---|
| C404 — `henon_resonance/paper/main.pdf` | 10 | 373654 | `99c58e5805bb4e5b70e5f86505dc60dd8f79df76ea0011ac901127456e10a3cc` |
| C405 — `arithmetic_forms/paper/main.pdf` | 10 | 355317 | `9b6801db5237ef523fded18797ec7508a06762bd79fd1c32f0074ddbfa9290c3` |
| C406 — `critical_delta/paper/main.pdf` | 13 | 403808 | `43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9` |

三个文件均为 A4、PDF 1.5。C405 的空 metadata 标题/作者字段与
FINAL_BUILD_REPORT 的明确披露一致，不是本次发现的摘要或文件错配。
本次没有重看页面图像；全部 33 页目视检查的执行者和证据仍以协调者
的最终构建报告为准。

## 4. 三篇／两空缺及 Route A 边界

README 只把 C404、C405、C406 列为完成稿件，分别对应唯一主 PDF、
证明包、来源审计和非作者正文审查。C407/C408 在标题、正文和结尾均
保持科学合同空缺，没有把野分歧札记、几何部分结果或重复生成函数
推论算成第四、第五篇，也没有分配 C409。当前准入计划和续接计划
与这个发布统计一致。

| 稿件 | README 总评 | YAML 总评 | 必须随标签保留的范围 |
|---|---|---|---|
| C404 | 源机制 EXPLORATORY | `ROUTE_A_EXPLORATORY` | `A1_PASS_ANALYTIC` 仅原生有限域 S 周期计数 |
| C405 | 源机制 EXPLORATORY | `ROUTE_A_EXPLORATORY` | `A4_FORMAL_HINT` 仅源正算子，不提供轨道至 Hamiltonian 传输 |
| C406 | REJECTED | `ROUTE_A_REJECTED` | `A4_NATURAL_QUANTIZATION` 仅源 Schrödinger 实现 |

三 YAML 的 tuple 均等于自身 a0–a4 的 verdict。每份都有 9 个明确
false 的 scope flags、9 个 `NOT_TESTABLE` 的 A2 指标，合计分别
为 27；每份 `route_b_invocation_allowed` 均为 false。三份 A0
对照状态均为 INCOMPLETE，A2/A3 均 FAIL。三份 `reference_routing`
按 YAML 所在目录解析后都指向实际存在的本批 EVALUATION_SCOPE。
README 没有把缺测解释成零误差，也没有把源证明提升成目标欧拉因子、
根数、零点对应、Hilbert–Pólya 实现或 Route B 晋级。

## 5. 历史记录与当前绑定

局部版本差异：PARTIAL_BATCH_BOUNDARY_REVIEW 仍记录两份计划在
其审计时的旧哈希／阶段性措辞；协调者后来加入收尾状态。旧哈希
不是对当前字节的声明。初稿收据中的等待状态同样属于历史时点，
FINAL_BUILD_REPORT 已明确这一点。均保留原记录，不误报为断链或
当前索引错误；本次没有发现必须修改已有文件的问题。

下列 SHA-256 在末次核对中保持一致。路径相对本批目录。

| 文件 | SHA-256 |
|---|---|
| `README.md` | `984ff3088e7ea2d5a4b0ead78da97425d5d442e1be6a0eaf5c4ea0ce999231cc` |
| `FINAL_BUILD_REPORT.md` | `26d919d8aa8b58f9413b68edc9b4ae0fb74ffd488c0c0d371df546b4e2dd9a45` |
| `EVALUATION_SCOPE.md` | `3f57c80303721af3652ade4574af275aa0c19054dde9f1159e53ea81e42016d8` |
| `ADMISSION_AND_BATCH_PLAN.md` | `69ac1307e26715d3d92a8846f0063e1228f3a0bdcec85b9d78f1f23cd44c4a99` |
| `SCOUT_PLAN.md` | `ff38389ffe4136752c5f3a69240cf23758d6356f58aabb4f25e2f4e612a08040` |
| `reviews/EVALUATION_BOUNDARY_REVIEW.md` | `18cb8662503dc5d9d8f15cab8c11dba2d523b0a4956ae52019648650b2aa2eba` |
| `reviews/PARTIAL_BATCH_BOUNDARY_REVIEW.md` | `5a2575b16c0cb3e433fe155e307b9690d7213a5bee25b9832a7055f0af338b9a` |
| `evaluations/route_a/HCS-C404/2026-09-06.yaml` | `d82f8c63d5b35b88f9d59ae09cb6c1af4a2dbfb18d37430151f9c3e86bd22a40` |
| `evaluations/route_a/HCS-C405/2026-09-06.yaml` | `d904350cf40ffe54e333ae5ee26fef012c242d9400b6c14ae4fb230e564e1941` |
| `evaluations/route_a/HCS-C406/2026-09-06.yaml` | `0e69a4cb7bc9a8a3995edb88fdaef7a89d799f86228f83747e0b18c6f8f78258` |

本报告不包含自身摘要，也不预填尚不存在的清单摘要，避免递归改写。
协调者可在读取本报告后将其纳入完整载荷，再生成唯二预留清单并做
真实成员／摘要核验。封存后的核验结果及 Git 同步状态应另在树外
CURRENT 入口记录；本次审计没有执行或替代那些后续步骤。
