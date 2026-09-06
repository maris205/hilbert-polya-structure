# Symbolic Dynamics — 当前研究状态

更新：2026-09-06 UTC。跨会话恢复入口；本文件不代替证明或重审历史。

## 当前结论

- 当前执行批次：[P204 起的新五席研究](docs/papers204_208_sequence/PIPELINE_STATE.md)，状态 `P205_INTERNALLY_COMPLETE / P206_REJECTED_IN_A / FOUR_SEATS_OPEN`。P204、P206 稿审 A 淘汰，原稿、冻结和 critical open value finding 保留。P205 两份独立稿审及实际无修改 delta 已接受、三轮冻结完整；root B 双次各 12,023,630 断言及原始字节比较通过，两个终端冷构建、三页实际视读和单篇 artifact gate 完成。当前保留 1、完成 1、空缺 4，下一编号 P207，整批远未完成。
- 当前候选边界：LNR 原 HOLD_SOURCE 不变，直接相关 lower-rank 收敛旧文正文仍未核；数学重放不消除来源 finding。UGR 作者证明已闭合、独立候选 gate 进行中，全局时钟仅为非 sharp 上界。MNC 的实际非作者 gate 已判 `MATH_VALID / KILL_VALUE_TEMPORAL_BINARY_WRAPPER`；root 读完整 adapter、通过 29/17/3 pins，并双次各重放 293,461 断言和原始字节比较后接受淘汰，MNC-V1 Critical/open 保留。其正确全目标逆像极值不能补足被扣除的时间轴，未编号。第六线七个、第七线六个 literal 均 NO_PROMOTION；root 已读原件并核完整封印。新 CPRM 的初等完整结论不送准入，CSGD 非负 carrier 不封闭的失败原样保留。HVD 与第八线仍为 bounded scout。
- 最新范围推送 `6bd2d798` 已归档 LNR 逆像/gate、第六线、对比度 intake 及 root 距离解码证明，三份新候选 manifest 的 59 pins Git 对象检查通过。P205 完成证据仍在前推送 `ef9deb85`；后来闭合的 UGR/MNC 作者包、MNC adverse gate、第七线、新 root scout 与活跃工作尚未包含。未同步的工作变化不归到历史提交。
- 路线仍为 **Route A / Symbolic Dynamics**，当前子轨广泛探索有限自主确定性映射。短论文 Stage/Round 不是原始 HP 算术路线的 A0–A4；没有进入 Route B。
- 最新内部完成批次：**P197 / P199 / P200 / P202 / P203**。五篇各四页，十份实际论文审查、十次终端冷构建、二十页实际视读完成；整批终端审计 `PASS`。全部仍为 `OWNER_AMBER / HOLD_EXTERNAL`。
- 研究完成提交 `0236e3e7` 已随正常合并 `1b55fbda` 实际推送，远端 ref 已确认；见 [同步回执](docs/papers197_201_sequence/GIT_SYNC_RECEIPT.md)。[配置审计](docs/research_state/INSTRUCTION_AUDIT_2026-09-05.md) 和独立情境/修订测试完成。
- 上一批恢复记录见 [已完成批次状态](docs/papers197_201_sequence/PIPELINE_STATE.md)；完成证据见 [最终 QA](docs/papers197_201_sequence/FINAL_QA_REPORT.md)，逐篇进展见 [Round2 报告](docs/papers197_201_sequence/ROUND2_REPORT.md)。不因旧索引中的 pending 文字重做已完成审查。
- P198、P201 在论文审查中淘汰，原稿和编号保留；五篇完成不能读成 P197–P203 七篇通过。当前台账 **57 次候选尝试**（5 选中、3 reserve、49 淘汰），不是 57 个已验证独立子类。

## 持续约定与证据边界

每轮五篇、每篇明确数学进展；在当前类型内广泛寻找系统，弱信号或旧机制重复时换方向，普通阶段转换无需再确认，及时私有 Git 同步。科研执行见 [工作流](docs/research_state/WORKFLOW.md)。状态查询本身不启动新批次。

P200 的窄/方阵 sharp 时钟仍未证明。P203 的历史 Stage1 中间代码缺失仍是未修复归档限制：旧 pin-list 的 3 PASS / 1 FAIL 保留；当前独立论文证明和运行输入完整。当前论文零未决问题不抹去这一历史限制。详情均在最终 QA 及其链接的原件。

上一完成批次 P192–P196 的研究提交为 `76146ba17eb15beccfc38e625427f8da726db919`，见 [上一批最终 QA](docs/papers192_196_sequence/FINAL_QA_REPORT.md)。P192 全 n history-set/相关深度分布仍是猜想，P194 文献遗漏已修复；旧状态和外部 HOLD 原样保留。

## 路径、历史与维护

工作区 `/root/autodl-tmp/symbolic_dynamics` 本身没有 Git；镜像是 `/root/autodl-tmp/hilbert-polya-structure`。新论文 P187 起在镜像根 `papers/`，较早已跟踪材料多在 `symbolic_dynamics/` 下。实际完成提交与远端同步分别记录，不能把 WIP 备份当验收。

编号异常、P51–P56 缺失、P57–P66 历史同步缺口、双 96 和完整路径映射见 [历史与边界](docs/research_state/HISTORY_AND_CAVEATS.md)。该文及 [整理前快照](docs/research_state/ARTIFACT_SNAPSHOT_2026-09-05.json) 保持原基线，190 个不同编号材料包不是实时完成总数。

证据优先级：接受版本的证明/审查/实际输出与 Git 对象，高于恢复索引，高于聊天摘要。明确区分证明、有限实验、猜想、淘汰、reserve 和待完成；子代理消息须落到可检查原件。实质里程碑变化时先更新批次状态，再刷新本入口；模型切换不改变已证明结论。
