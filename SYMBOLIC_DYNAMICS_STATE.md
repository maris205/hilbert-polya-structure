# Symbolic Dynamics — 当前研究状态

更新：2026-09-06 UTC。跨会话恢复入口；本文件不代替证明或重审历史。

## 当前结论

- 当前执行批次：[P204 起的新五席研究](docs/papers204_208_sequence/PIPELINE_STATE.md)，状态 `P205_P207_COMPLETE / P208_A_ACCEPTED_ROUND1_FROZEN / TWO_SEATS_OPEN`。P204、P206 在稿审 A 淘汰，原稿、冻结及 critical open value finding 保留。P205、P207 已内部完成，接受 A/B、终端双构建/全页视读及实际制品验收均有原件。P208 已窄准入并有完整七页稿；root 完整原件审查、作者/A 严格双重放和实际全页视读完成。同一非贡献者 A 已接受仅澄清库路径计数的文档 delta，零当前 open finding；root 核完最终 764 payload、4,219 引用及初始 743 payload 保留，随后物理封存 487 输入 Round1，逐项及 raw 清单比较通过。新的非贡献者 p208_b_reviewer 已从 Round1 开始独立 B 审。原执行失败、报告限制与文档历史映射均保留；尚无 B 接受、Round2 或 P208 完成。保留 3、完成 2、空缺 2，下一编号 P209，整批未完成。
- 当前候选边界：LNR 原 HOLD_SOURCE 不变，直接相关 lower-rank 收敛旧文正文仍未核；数学重放不消除来源 finding。UGR 已按单一 rank-family 窄合同准入 P207，全局时钟仅为非 sharp、明确依赖有限证书的上界。MNC 的实际非作者 gate 已判 `MATH_VALID / KILL_VALUE_TEMPORAL_BINARY_WRAPPER`；root 读完整 adapter、通过 29/17/3 pins，并双次各重放 293,461 断言和原始字节比较后接受淘汰，MNC-V1 Critical/open 保留。其正确全目标逆像极值不能补足被扣除的时间轴，未编号。第六至第九线均已在原件与完整封印检查后关闭，无新增准入。CPRM 初等结果不送准入，CSGD carrier 失败保留；HVD/NCC 的局部证明不能代替缺失全局定理，CPC 原盒长周期亦不填席。第十线已通过 root 原件及 79/19、40/18+1+20 pins 核验：五条关闭 NO_PROMOTION，新非贡献者 `ofs_candidate_gate` 已实际给出 GO_NARROW_TWO_AXIS，旧 edge-labelled lift 与静态计数等全部扣除；root 读完整几何/逆像/K 时钟证明、来源边界及 452 行代码，双次各 628,980 检查和原始字节比较通过，87 条 gate 清单和 149 referents 前后不变，正式准入 P208；第十一线已通过 root 完整原件及 32/7 pins 核验，两个实际规则关闭 NO_PROMOTION。第十二线三条实测已通过 root 完整原件、22/12 pins 和实际 raw pair 比较后关闭 NO_PROMOTION；第十三线也已读完整证明/来源/代码，核完 55 条外封印、八份共 99 条清单、21 历史 pins 和 86 回执引用，并实际比较两类 raw pair 后关闭。其全参数 DAG 逆像极值不补足未证时间轴。第十四线也已完整原件/代码检查，39/11 pins、48 回执引用和两次 raw pair 比较通过后关闭；两个逆像极值证明不补足时间轴。第十五线亦已完整原件核查，六份 65 条清单、18 历史 pins、60/10 输入输出引用及两次 raw 比较通过后关闭；任意长周期的特定层构造不等于完整时间分类。第十六线完整原件/代码和 151 外封印、11/16 历史 pins、四次实际 raw 比较均核完后关闭 NO_PROMOTION；其局部尖锐定理不填席。第十七线完整案头原件及 6/10 pins 核完后关闭 NO_FRESH_SLATE，零新科学执行。第十八线完整原件及 7/13 pins 核完后也关闭 NO_FRESH_SLATE，零科学执行。第十九线已获不同新范围的有界侦察分配。
- 最新私有推送 `076cfbd4` 已实际确认远端：P208 准入、完整七页稿/作者及 root 双次证据/逐页视读、487 输入 Round0、第十二/十三线及所有已说明失败归档。八份显式清单的 1,135 条 Git 对象检查通过，正常 fast-forward 保留远端 `b9eb720e` 的 96 条不相交 Henon 路径。进行中的稿审 A、第十四/十五线明确排除；后来第十六线分配与同步回执不归入此提交。前推送 `cb93dcab` 保留 P207 完成及 OFS 候选 gate；`eee9dcc3` 保留 P207 接受 A，P205 完成仍在 `ef9deb85`。
- 路线仍为 **Route A / Symbolic Dynamics**，当前子轨广泛探索有限自主确定性映射。短论文 Stage/Round 不是原始 HP 算术路线的 A0–A4；没有进入 Route B。
- 最新内部完成批次：**P197 / P199 / P200 / P202 / P203**。五篇各四页，十份实际论文审查、十次终端冷构建、二十页实际视读完成；整批终端审计 `PASS`。全部仍为 `OWNER_AMBER / HOLD_EXTERNAL`。
- 研究完成提交 `0236e3e7` 已随正常合并 `1b55fbda` 实际推送，远端 ref 已确认；见 [同步回执](docs/papers197_201_sequence/GIT_SYNC_RECEIPT.md)。[配置审计](docs/research_state/INSTRUCTION_AUDIT_2026-09-05.md) 和独立情境/修订测试完成。
- 上一批恢复记录见 [已完成批次状态](docs/papers197_201_sequence/PIPELINE_STATE.md)；完成证据见 [最终 QA](docs/papers197_201_sequence/FINAL_QA_REPORT.md)，逐篇进展见 [Round2 报告](docs/papers197_201_sequence/ROUND2_REPORT.md)。不因旧索引中的 pending 文字重做已完成审查。
- P198、P201 在论文审查中淘汰，原稿和编号保留；五篇完成不能读成 P197–P203 七篇通过。当前台账 **57 次候选尝试**（5 选中、3 reserve、49 淘汰），不是 57 个已验证独立子类。

## 持续约定与证据边界

P208 稿审 A 已实际接受精确文档 delta，零当前 open finding。root 已读完整原件/代码，核验最终 764 封印、4,219 引用及 743 份初始 payload 保留，确认报告 Minor 所涉 35 种库路径写法对应 32 个已全部 pinned 文件，无数学或运行依赖变化。先前双次各 130,961 检查及 18,695 条全作者输出比较保留；两个已更新的文档引用按明确历史映射处理。root 随后物理冻结 487 输入 Round1，全部 live/Round0/Round1 副本及实际 raw 清单比较通过。见 [root 接受及冻结](docs/papers204_208_sequence/qa/P208_A_ROOT_DELTA_INSPECTION.md)。独立 B 已由新的非贡献者实际开始，尚无 Round2 或论文完成。第十六至十八线负结果交接已通过 root 完整原件/制品检查；第十九线只获有界新方向侦察授权，无新增准入。

P208 在稿审 A 的运行证据补检期间，另完成 [root 严格作者重放](docs/papers204_208_sequence/qa/P208_STRICT_AUTHOR_REPLAY.md)：两次各 62,101 检查，同一 2,055 状态，七条子命令及三次原始字节比较均通过；981 输入、918 运行文件、112 动态链接文件和 29 配置项前后核验，38 条完整封印复核通过。禁用 site 与旧缓存的此对运行补足重用证据，旧回执限制和原件不改；不代表稿审 A 已接受，也不新增席位。

新 NCC 邻域计数反馈的六个原始完整小盒已完成，固定点及全部常值目标逆像公式有完整证明和双次各 102,613 条断言的作者重放；全局时序/全目标极值未证明，关闭为 `HOLD_PROOF / NO_ADMISSION`。真实二周期与一般直方图逆像旧机制扣除均保留，未新增席位或扩大实验上限。

第八线六个候选已在 root 全原件、13 条清单及九条历史 pins 核验后关闭为 NO_PROMOTION；第九线六个候选也已在完整证明/来源/执行原件与 66/9 pins 核验后关闭。两者实际有限数据是作者证据，未标成 root 新数学重放。第九线 QEF 的尖锐静态五逆像界不能补足未证时序轴，原 old-LV 错误比较标签及更正保持不动。新 CPC 计数规则原盒已有 32/30 周期，亦不编号；第十线及独立 desk 已封存，OFS 已完成窄范围准入成为 P208，现稿审 A 接受及 Round1 已完成、B 在进行；第十一至十五线均已完整原件核验关闭；第十六、十七线已按各自实际范围核验关闭；第十八线完整原件及 7/13 pins 核完后也关闭 NO_FRESH_SLATE，零科学执行。第十九线已获不同新范围的有界侦察分配。

每轮五篇、每篇明确数学进展；在当前类型内广泛寻找系统，弱信号或旧机制重复时换方向，普通阶段转换无需再确认，及时私有 Git 同步。科研执行见 [工作流](docs/research_state/WORKFLOW.md)。状态查询本身不启动新批次。

P200 的窄/方阵 sharp 时钟仍未证明。P203 的历史 Stage1 中间代码缺失仍是未修复归档限制：旧 pin-list 的 3 PASS / 1 FAIL 保留；当前独立论文证明和运行输入完整。当前论文零未决问题不抹去这一历史限制。详情均在最终 QA 及其链接的原件。

上一完成批次 P192–P196 的研究提交为 `76146ba17eb15beccfc38e625427f8da726db919`，见 [上一批最终 QA](docs/papers192_196_sequence/FINAL_QA_REPORT.md)。P192 全 n history-set/相关深度分布仍是猜想，P194 文献遗漏已修复；旧状态和外部 HOLD 原样保留。

## 路径、历史与维护

工作区 `/root/autodl-tmp/symbolic_dynamics` 本身没有 Git；镜像是 `/root/autodl-tmp/hilbert-polya-structure`。新论文 P187 起在镜像根 `papers/`，较早已跟踪材料多在 `symbolic_dynamics/` 下。实际完成提交与远端同步分别记录，不能把 WIP 备份当验收。

编号异常、P51–P56 缺失、P57–P66 历史同步缺口、双 96 和完整路径映射见 [历史与边界](docs/research_state/HISTORY_AND_CAVEATS.md)。该文及 [整理前快照](docs/research_state/ARTIFACT_SNAPSHOT_2026-09-05.json) 保持原基线，190 个不同编号材料包不是实时完成总数。

证据优先级：接受版本的证明/审查/实际输出与 Git 对象，高于恢复索引，高于聊天摘要。明确区分证明、有限实验、猜想、淘汰、reserve 和待完成；子代理消息须落到可检查原件。实质里程碑变化时先更新批次状态，再刷新本入口；模型切换不改变已证明结论。
