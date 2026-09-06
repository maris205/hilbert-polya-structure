# 当前研究状态与恢复入口

核对日期：2026-09-06。主线：`henon_dynamics`，C 系列。
长期规则见 [AGENTS.md](AGENTS.md)；本文件只保存当前状态和证据入口。

## 最新授权与恢复动作

用户在下述四项候选检查点交付并核实实际远端
`f29d79392498ac8cf6b9b72f8df07b95448c20d6` 后明确“继续”。
现在从 [第二轮缺额续接计划](continuation_c409_c413_round2/SCOUT_PLAN.md)
继续同一 C409–C413 批次。第五项现由
[独立迹映射审查](continuation_c409_c413_round2/REVIEW_TRACE_ROOT.md)
准入，状态 `FIVE_SUBSTANTIAL_CONTRACTS_ADMITTED`，见
[五项合同与写作计划](continuation_c409_c413_round2/BATCH_PLAN.md)。
新增合同为全整数 Fibonacci 迹映射的周期穷尽分类；已知周期族
和一般逃逸理论全部扣除，来源比较有界，不声明全球优先权。
四项旧合同与 48 个封存文件保持原字节，不重审通过的旧证明。
用户在并行写作中再次明确“继续”；现已完成五篇真实全文和
最终 PDF，**59 页（11/13/11/14/10）**，见
[五篇交付入口](continuation_c409_c413_round2/README.md)。
五篇非作者内部全文／来源审查均通过，C409/C410/C413 的实际
精度修订均经原审者确认，见
[稿审裁决](continuation_c409_c413_round2/REVIEW_ADJUDICATION.md)。
协调者已在十个全新目录完成每篇两次构建，五对 PDF 均同字节，
50 个最终 TeX/Bib 输入与两个构建副本一致，全部 59 页已实际
逐页查看；见 [终构建记录](continuation_c409_c413_round2/FINAL_BUILD_REPORT.md)。
五份正式评价的只读结构检查 5/5 及限定语义审查均通过；严格
目标边界与输入路由见 [评价范围](continuation_c409_c413_round2/EVALUATION_SCOPE.md)。
目标 A2/A3 仍 FAIL，45 格指标 NOT_TESTABLE，A0 三类控制门
INCOMPLETE，全部 target/Route-B flags 为 false，不称目标突破。
当前状态 `FIVE_PAPERS_SEALED_AND_RELEASE_COMMIT_SYNCED`；
科研提交的实际 Git 同步收据见下文。C409–C413 五篇批次完成，
停在用户检查点，不开始第六篇、不进入 C414。历史作者报告和
初审摘要保留当时状态，不能用其旧 PDF 哈希替代最终输出。

### 本批实际封存与同步收据

本续接树精确封存为 **207 个 payload、208 项 manifest、209 个
实际文件**；payload 合计 7,754,143 字节。所有实际文件都纳入，
包括默认忽略的历史日志和编译辅助文件。ledger 排除自身和
manifest，manifest 包含 ledger 而自排除。协调者实际执行
`sha256sum -c MANIFEST.sha256`，退出 0，208 项全部 OK；随后
以另一路只读目录遍历和清单解析核对三份精确集合、大小和摘要
对应，退出 0，无重复、额外／遗漏、符号链接或特殊文件。
ledger SHA256：`03a02f5bacbb11d6d00b6401af11ecf523723dcc677371b37909b7ec6aad2034`；
manifest SHA256：`5c8085ad3e62310774212a6dada4918f044044ec934f64f66cac230fc2b08c4d`。
这证明载荷成员和字节一致，不替代数学证明或目标算术结论；
未新增发布程序或声称通用篡改防护。此后不修改封存树。

[独立发布链接／范围审计](continuation_c409_c413_round2/nonlinear_geometry/RELEASE_LINK_SCOPE_AUDIT.md)
最终 139 行报告已实际读完并封存。它覆盖指定总览、终构建、
裁决全文及本状态／两注册表的新节；另一次自动存在性扫描覆盖
46 份 Markdown、143 处本地链接，零意外断链，两份清单为当时
明确预留。协调者现已实际确认这两个目标生成且符合上面的成员
规则；没有把前一次扫描冒称为封存后全树内容复审。五 PDF 的
实际页数／大小／摘要和五份 tuple 均获独立一致性核对。

整合前实际 fetch 核对 `HEAD` 与 `origin/main` 都为
`f29d79392498ac8cf6b9b72f8df07b95448c20d6`，无远端增量要整合。
本批只暂存该 209 文件树、当前状态入口和两份 Hénon 注册表。
八个继承未跟踪文件目录及其他流／空目录原样保留，不纳入提交。
本次已用只读 Git 差异确认原 48 文件研究快照及前批 179/93 文件
封存包未变，没有重跑其数学检查。常规提交／推送已实际成功，
真实同步收据如下；没有预填尚未产生的提交号。

暂存只读核验确认 **212 个路径 = 209 个封存文件 + 3 个许可
索引**，所有 index blob 与当前文件字节相同，没有夹带无关路径。
未过滤的 `git diff --cached --check` 退出 2：228 项均已逐项
分类，226 项来自保留的原始 log/aux/pdfinfo 输出，另两项是
C410 第 4、6 节源文件的末尾空行，无源码行尾空格或冲突标记。
这些无语义空白保留原始／已核源字节，不重写封存文件。对所有
作者文本允许末尾空行后单独执行检查，退出 0；不把未过滤检查
写成全部通过，也不将它误当作最终 TeX 日志的警告。

科研提交 **`bda265d66a26552cf9a1ece84cedc6efe33f95bd`**，主题
`Complete and seal five reviewed C409-C413 manuscripts`，已常规
推送至已配置 `origin/main`。随后 fetch、两次本地 ref 解析和
`git ls-remote origin refs/heads/main` 的实际结果均为该完整
提交号；运行时钟核对点为 2026-09-06 16:29:19 UTC。当时无
受跟踪未提交改动，状态只余八个继承未跟踪文件目录。
本段是推送成功后补记的状态收据，单独提交本状态文件，不回写
209 文件封存树或重新计算清单。其自身提交与最后同步状态以
真实 Git refs／交付消息核对为准，不嵌入自指的未来提交号。

## 本批选题历史（以下保留当时状态，由上文当前成果覆盖）

用户在 C404–C408 五篇、58 页封存交付，并核实
`b9eb720eeb5aa590d784b08ef20ffbac896165b5` 与实际远端一致后，
于 2026-09-06 明确“确认，下一轮”。**当前新授权为 C409–C413**，
从 [新批次选题计划](research_c409_c413/SCOUT_PLAN.md) 开始，状态
`SCOUT_CHECKPOINT_FOUR_READY_FIFTH_OPEN`；当前 0 项正式编号准入、0 篇新稿/PDF。
已有四项未编号 research-ready 候选通过非作者数学／实质性核查；
谱转移与后续有理野塔两项证明虽数学成立，因剩余增量不足被拒绝
独立计篇，见
[当前实质判定](research_c409_c413/PROVISIONAL_ADJUDICATION.md)。
仍缺一个独立合同；有理野塔数学及来源审查已结束，明确保留为
配套札记，不把它填入完成数。当前实际产物、限制与续接入口见
[四项研究候选检查点](research_c409_c413/README.md)。C409–C413
五篇任务尚未完成；下一次续接仍补这一批，不跳 C414。
上一批 round2/round3 的 179/93 个封存文件保持原字节，不重跑。
只在五个实质合同成立后冻结论文计划，不将旧札记直接改号计篇。
以下 C404–C408 记录是已完成的历史批次，不是当前授权的空缺。

本次研究检查点已精确封存为 **46 个 payload、47 项 manifest、
48 个实际文件**。ledger 排除自身与 manifest，manifest 包含 ledger
而自排除。协调者实际运行 `sha256sum -c MANIFEST.sha256`，退出 0，
47 项全部 OK；另用只读成员遍历独立比较磁盘、ledger 和 manifest
的精确集合，退出 0，无重复、额外/遗漏、符号链接或特殊文件。
ledger SHA256：`75cca9760bae2f0fbe2047b8e96ec703a9abe067b697130353537a201bb8d76a`；
manifest SHA256：`880947f4c7bdce49f1e2921f79e098201639e58e887e57f4c8258320d63eccaf`。
此为研究快照保存核验，不是论文完成或数学正确性证明；封存后
不再修改本目录，续接应另起未冻结目录并链接四份已核合同。

[独立检查点链接／状态审查](research_c409_c413/nonlinear_geometry/CHECKPOINT_LINK_SCOPE_AUDIT.md)
覆盖五个指定文档范围、335 行、44 处本地链接，零意外断链；
另作 38 份新树 Markdown 的纯链接扫描，78 处本地链接、114 处
外部链接跳过。全部四处当时缺失均指向明确预留的两清单；协调者
现已实际确认两者生成，且纳入上述精确成员核验。该审查没有
重新审查 38 份文档的数学或外部引用，本段关闭收据也不冒称
已包含于其先前固定的 current-state 节选。

整合前实际逐项分类远端的 2,771 个变更路径：1 个 symbolic 状态
文件、1,306 个 `docs/papers204_208_sequence/` 文件和 1,464 个
P208 文件；无本批、旧冻结包、AGENTS/工作流、参考路由或
evaluator 重叠，已安全快进至
`8e4e21d0c41da865bd12081879a09fd6eaa70de6`。本研究提交由主题
`Preserve C409-C413 four-contract research checkpoint` 的 Git 对象
绑定；同步以真实本地／远端 refs 及交付时的实际核对为准，不在
自哈希载荷中循环写入自身提交号。本次只暂存新检查点及本状态
入口，不改 C 注册表，也不纳入八个继承未跟踪目录。

关闭时再次 fetch 发现 symbolic 的新提交
`b8bf6c52f0a1a7c2075e86fd3bd950222acf5be1`。另外 4,475 个变更
路径已逐项分类为 1 个 symbolic 状态、3,758 个其批次文件、716
个 P208 文件；上述本流及指令路径仍无重叠。只将本轮尚未推送的
单个研究提交重放到该新基线，成功且无冲突；重放前后本研究树及
状态文件的字节差比较为空。冻结证明和清单未变，不因此重跑数学
检查。随后本段仅补记 Git 整合事实，位于封存载荷之外。

用户在 C399–C403 完成封存、同步及五篇 PDF 交付后，于 2026-09-06 再次
明确“确认，下一轮”。本次新授权范围为 **C404–C408**；起点 Git 为
`5b2a654c4f0b82b0e2d5158146b377ee6bf4e804`，不是续补旧批次。
首轮保留 [新批次选题检查点](research_c404_c408/README.md)：四条线共九个
候选组，**0 份录取合同、0 篇新论文/PDF，C404–C408 未完成**。
Hénon 算术三组、非仿射正特征三组、非线性几何两组、算术/谱迭代一组，
各自保存明确的经典所有权、增量不足或证明未闭合理由；没有冻结五篇计划。
本次有共振计数外推反例（378≠486、176≠192）及 Hietarinta–Viallet
三周期普通点数 9 与理想长度 18 的区别，均不另算论文。协调者用 F5B
独立复核两项共振反例，见 [实际收据](research_c404_c408/ROOT_INDEPENDENT_CHECK.md)。
最具体的未解入口是非加性共振在任意周期、尤其 p 整除周期时的无穷远
抵消/交数理论；没有把“未证明”称为全族 no-go。独立交叉核查与最终
同步状态见检查点总览。不得从此处跳到 C409 或重复计入旧批次。

用户在该检查点交付后再次明确“确认，下一轮”。现从已同步的
`ae2fdc72c865a61369ef74d03d5b266a94ace86d` 续接
[第二轮研究计划](continuation_c404_c408_round2/SCOUT_PLAN.md)，状态为
`PARTIAL_THREE_PAPERS_SEALED`；用户随后“继续”续接
收尾，仍是 C404–C408，不重启已通过的研究门槛。当前三篇完整正文与
PDF 已完成，共 **33 页（10/10/13）**，见
[三个 PDF 与实际缺额](continuation_c404_c408_round2/README.md) 及
[准入决定与部分合同计划](continuation_c404_c408_round2/ADMISSION_AND_BATCH_PLAN.md)：
C404 非线性 Hénon–Frobenius 共振全周期计数、C405 临界整除 Gram
奇异型/强预解式二分、C406 调和 δ 链临界第二 Weyl 系数。三份正文均
通过非作者内部全文与实际引文审查，未留下必须修订的数学/引用问题；
每稿两次新空目录构建及与经审查初稿的 PDF 比较均同字节，全部 33 页
已实际逐页查看，详见 [终构建记录](continuation_c404_c408_round2/FINAL_BUILD_REPORT.md)。
野性动力学加权公式数学成立但不够独立成篇，只保留札记；几何候选
被经典归属或新边界重数反例淘汰。尚未凑齐五个合同，C407/C408 保持空缺。
新工作写入独立续接目录，不回写第一轮筛选记录。

三份 [正式评价及范围](continuation_c404_c408_round2/EVALUATION_SCOPE.md)
均保留目标 A2/A3 FAIL、三类算术对照 INCOMPLETE、27 项 false scope flags
及 27 项 NOT_TESTABLE 目标指标。C404/C405 为源机制 EXPLORATORY，C406
为 REJECTED；源 A1/A4 标签没有提升为目标结论，另有独立一致性核对。
不将这个三篇检查点表述为 C404–C408 五篇已完成，也不进入 C409。

本轮精确封存及最终只读核验已完成：177 个 payload，ledger 排除
自身与 manifest；manifest 包含 ledger 而自排除，共 178 项，树内
实际文件 179 个。`sha256sum -c MANIFEST.sha256` 退出 0、178 项全部
OK；另用独立集合比较核对实际文件等于 ledger 加两清单、也等于
manifest 加自身，无重复、额外/遗漏、符号链接或其他特殊文件，退出 0。
这只证明成员与字节一致，不替代数学正确性。未新增发布程序或篡改测试。
manifest SHA256：`30a886cb0103ff0a0d5f6dae09c7902aca9d794fb14de25571716da9429d59ef`；
ledger SHA256：`1a708210edc404f5a9083c7b8f2f89ac389167229ac70bafec6d6e849f6bdc28`。
封存后不再修改本轮 payload，也不回写首轮或其他旧冻结包。

[独立本地链接审计](continuation_c404_c408_round2/reviews/RELEASE_LINK_AUDIT.md)
覆盖 39 份 Markdown、59 处本地链接：审计时 57 处存在、两清单为
明确预留、0 意外断链。根协调者封存后已实际确认这唯二预留目标生成
并存在。三个主 PDF 的页数/大小/摘要均与终构建收据一致；未复查外部 URL。

Git 整合先后核对远端新变动仅限 symbolic 的 state、P207 与相关记录，
无本批写入路径或 evaluator 重叠，已安全快进至
`eee9dcc3b89e1b822ad4f711aa57be5d7bd1bfd4`。本轮科研提交由 Git 中
`Complete C404-C406 partial batch and seal three reviewed papers` 主题的
对象绑定；同步以真实 refs 为准，不在封存载荷中循环写入自身提交号。
精确暂存范围仅本续接目录、当前入口和两份 Hénon 注册表；八个继承
未跟踪目录保留，不进入本次提交。

三篇终稿交付并核实 `ec024cadfbb728cc66aa0dcaca88a6d2f4dbd4d0` 与
远端一致后，用户再次明确“继续”。当前从
[C407/C408 缺额续接计划](continuation_c407_c408_round3/SCOUT_PLAN.md)
进入新一轮有范围的证明与选题，现已通过两个实质合同准入，状态
`FIVE_PAPERS_SEALED`，见
[续接冻结五项合同](continuation_c407_c408_round3/BATCH_PLAN.md)。
只补未完成的两项；round2 的三篇及其 179 个封存文件不回写、不重跑。
新增 C407 为 hyperbolic FAD 聚点集的全有限素数／野性 Cantor 与
零上盒维定理；C408 为全奇 k、全 m 交替零点的未饱和循环关系局部
厚度分类。两篇实际完整正文分别为 13、12 页，均通过非作者全文
与引文内部审查及定点修订；各两次新空目录终构建逐对同字节，
全部 25 页已实际查看，见 [终构建证据](continuation_c407_c408_round3/FINAL_BUILD_REPORT.md)。
连同原三篇，**C404–C408 五篇已完成，共 58 页**，见
[五个 PDF](continuation_c407_c408_round3/README.md)。新包精确封存与
只读核验已完成；Git 同步以以下提交主题及真实 refs 为准。
未把加权札记或低期反例补编 C 号，未开始 C409。

C407 正式 tuple 为 `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`，
源机制 EXPLORATORY；C408 为全 FAIL、REJECTED。新两项的三类算术
对照 INCOMPLETE、18 个目标指标 NOT_TESTABLE、18 个 scope flags false，
见 [正式评价范围与边界](continuation_c407_c408_round3/EVALUATION_SCOPE.md)。
五篇目标 A2/A3 均无提升。C407 的优先权比较只及已核读公开版本，
EMS 最终书稿未取得；C408 不作普通周期点或光滑曲面固定概形断言。

本次新包封存 **91 个 payload、92 项 manifest、93 个实际文件**。
ledger 排除自身与 manifest，manifest 包含 ledger 而自排除。
实际 `sha256sum -c MANIFEST.sha256` 退出 0、92 项全 OK；另从磁盘
重读两清单并独立比较集合，实际树等于 ledger 加两清单，也等于
manifest 加自身，无重复、额外/遗漏、符号链接或特殊文件。成员
核查通过，不把文件一致性当作证明正确性；封存后不再编辑新载荷。
ledger SHA256：`6cdc3f7cae99906fc80fbe482b59023725829710ae94c555d4a1f18cfb4c0ee8`；
manifest SHA256：`4e014721b21b6af032b7f70aaddca74fee697b56be46e8a28c3aab85eb4d98f5`。

[独立交付审计](continuation_c407_c408_round3/reviews/RELEASE_LINK_AUDIT.md)
实际覆盖 29 份新树 Markdown 与当时三份共享新增段，共 32 份文档；
82 处本地链接、51 个唯一目标，78 处存在，四处指向唯二预留清单，
0 意外断链。协调者封存后实际确认唯二清单均已生成并包含在精确
成员核验内。审计还只读核对五个 PDF 的页数、大小与摘要；不声称
复查外部 URL、旧证明或全历史索引。当前完成状态的扩展段由协调者
在封存后更新，不伪称已纳入先前审计的固定行范围。

整合前实际遍历远端 658 个变更路径：1 个 symbolic 状态文件、
469 个 `docs/papers204_208_sequence/` 文件、188 个 P207 文件，
没有本批、旧封存包、AGENTS/工作流或 evaluator 的重叠；安全快进到
`cb93dcab58009f6e70cff56b527ecf565f4313d6`，随后再次 fetch 仍一致。
新科研提交由主题 `Complete C407-C408 and seal five-paper batch` 的
Git 对象绑定；最终同步核对本地 HEAD、origin/main 与真实远端 main，
不为写入自身提交号而循环改写载荷。暂存范围仅新续接目录与当前
入口、两份 Hénon 注册表；八个继承未跟踪目录保留且不暂存。
五篇批次止于 C408；下一批须等待用户明确授权。

## 最近完成：C399–C403

该批最初要求：先按最新官方指导审计优化仓库 AGENTS、skills 与 workflow，
“然后再继续”。前一批 C394–C398 已交付；研究续接范围为 C399–C403 五篇。
仓库 Astra 指令优化及独立场景检查已完成并推送：`b0cdadb9`。
[指令审计](../docs/agent_workflows/ASTRA_AUDIT_2026-09-05.md) 保存来源、范围和验证。
用户随后要求“继续”，并在两份研究稿交付后“确认，下一轮”。续接仍是未完成的
C399–C403，不跳到 C404。当前已冻结
[五篇合同计划](continuation_c399_c403_round2/BATCH_PLAN.md)：C399 Boole 有限实
稳定性乘积、C400 有限正耦合 harmonic delta-comb、C401 非共振 Hénon–Frobenius
双时钟交数、C402 多项式坐标权重全周期留数边矩阵、C403 非乘性慢变整除 Gram
的精确 Schatten 收敛。五篇完整研究稿及 PDF 均已完成，共 **59 页**；
[本轮交付总览与五个 PDF](continuation_c399_c403_round2/README.md) 为当前入口。
三份新正文均有完整非作者内部审查：C401 一句非共振条件澄清已定点闭合，
C402/C403 无需修订；全部书目与实际引用语境逐项核对，无未关闭数学问题。
Boole 9 页与 δ 梳 14 页的 [前轮研究快照](research_c399_c403/README.md) 保留原字节，
合计 23 页及既有正文审查、定点修订、双新目录同字节构建、全页 QA 收据均复用。
它原有“未编号/缺三合同”等状态仅描述该冻结时点，不回写旧 manifest。
本轮 [五份正式评估及范围记录](continuation_c399_c403_round2/EVALUATION_SCOPE.md)
已写：C401/C403 仅源机制 EXPLORATORY，其余 REJECTED；目标 A2/A3 全未通过，
三类算术对照门槛均如实记 INCOMPLETE；另经独立跨产物一致性审计，未发现
源结论被提升为目标结论。三篇新终稿各做两次新空目录构建，PDF 逐对同字节，
最终日志无警告、字体全嵌入、文本及全部 36 页目视通过，见
[最终构建收据](continuation_c399_c403_round2/FINAL_BUILD_REPORT.md)。
用户 2026-09-06 的“继续”续接最后的封存和同步，不重启已验收的数学/
编译门槛。批次封存与最终只读核验已完成：232 个 payload（173 个新载荷、
59 个原快照文件），manifest 233 项；`sha256sum -c MANIFEST.sha256` 退出 0，
全部 233 项 OK。另只读核对实际文件集合与 ledger/manifest 成员完全相等、
无重复/额外文件/符号链接，退出 0；原快照同一命令仍 58 项 OK、退出 0。
新 manifest SHA256：`7ea58a3d8f25ee7079084c3af06d57bc5334a2e242abf3b627a452a2bec213b2`；
ledger SHA256：`95364ffa81ca05d81a8bf71031aaf437370efa5ff6f8f974b0ee0ae42bc7caf9`。
该核验只证明字节和成员一致，不替代科学审查；没有新增发布程序或伪造
篡改测试。核验后未改封存 payload。原快照 manifest 自身仍为
`e1b707ed43cd04fc3f9daf142618f1364b42c51e85ac1cba4860b20520fe0750`。
独立只读链接核对覆盖本批及复用目录共 56 份 Markdown、136 处本地链接
（77 个唯一目标），全部存在；五个 PDF 实测页数 9/14/13/12/11，三个
新 PDF 的摘要和大小与终构建收据一致。未重查外部 URL 或重做数学。

Git 整合已逐次只读确认远端变动限于 symbolic 研究流的 state、P204–P206
及相关记录，与本批无重叠；已安全快进到 `bad9dff9f11155a8ee8fd8ea7f40bdf5eb5f183d`。
本批科研提交由 Git 中 `Complete C399-C403 five-paper batch and seal reviewed artifacts`
主题的对象绑定；同步状态以实际 refs 为准，不为在 payload 内写入自身提交号
循环改写 manifest。五篇检查点停在 C403，未开始 C404。

发现并独立确认了 [C108 二周期源码缺陷](continuation_c399_c403_round2/nonlinear_return/BUG_FINDING_C108.md)：
producer 的方程并非其字面 Hénon 映射的二周期方程。旧 τ₂ 与直接依赖的
determinant 前缀停止作为通过证据使用；正确 τ₂=0。旧冻结文件原样保留，
不自动否定该包其他命题，也不将纠错另算新论文。
源文件的 Git 空白检查通过；原始编译日志自带的尾空白与末尾空行原样保留，
因此包含日志的全量空白检查会报告这些已知提示，未为消除提示改写原始证据。

正确仓库：`/root/autodl-tmp/hilbert-polya-structure`，分支 `main`。
环境初始 cwd `/root/autodl-tmp/henon_zeta` 不代表本主线工作目录。
恢复时查 Git、真实进程和当前产物，不根据聊天摘要虚构已完成步骤。

## 最近完成：C394–C398

提交并推送：`34c3781c7ad7231048ed01cc6ff174f3ded99433`。
交付时已实际核实本地 HEAD、origin/main 和远端 refs/heads/main 一致。
五篇终稿共 22 页；233 个载荷文件、5 份 manifest；最终发布复验均通过。
这些是该批实测结果，不是下一批必须达到的文件数或页数。

- [冻结计划与五篇合同](BATCH_PLAN_C394_C398.md)
- [选题、碰撞检索与经典所有权](IDEA_REPORT_C394_C398.md)
- [完整结果、修复、审查、PDF 与哈希](BATCH_REVIEW_C394_C398.md)

C394 仅局部 EXPLORATORY，其余四项 REJECTED；全部目标 A2/A3 未通过。
C398 的排除范围是固定正频率缩放及固定能量平移，不包括任意非线性重参数化。
此前 C389–C393 已交付 `697518b6db90458f86f7916fbf397b8ad5ef2372`，
见 [历史审查](BATCH_REVIEW_C389_C393.md)。不重做这些结果冒充新进展。

## 不变量与遗留材料

新 C 系列沿用 [Route A v0.2.0](../flow_systems/skills/route-a-evaluator.md)；
SHA256：`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
保持 `NO_BAD_EULER_OR_ROOT_NUMBER`，没有目标算术晋级或 Route B 授权。
已冻结论文、evaluator、评估 YAML 和发布清单不因指令优化而改写。

八个既存未跟踪目录必须保留且排除本任务暂存：本目录下五个
`henon_mu3_yukawa_mark_*` 包，以及仓库根的
`henon_ermakov_pinney_isotonic_action_route_a/`、
`henon_flat_magnetic_torus_landau_route_a/`、
`henon_hysteretic_relay_oscillator_route_a/`。
精确旧清单在上一版 Git 状态和 C394–C398 批次记录；不要宽泛清理。
其他研究流只在用户本次仓库指令审计范围内审查，不推进其科研批次。
