# Symbolic Dynamics — 当前研究状态

更新：2026-09-05 UTC。用途：跨会话、上下文压缩和模型切换时的恢复入口。
这是经文件/Git盘点后的状态摘要，不是所有历史证明的重新认证。

## 先读结论

- 路线仍为 **Route A / Symbolic Dynamics**。当前批次寻找不同的有限自主确定性映射，重在系统广度和每篇明确的定理进展。
- 最新完成批次是 **P192–P196**，研究提交为 `76146ba17eb15beccfc38e625427f8da726db919`。五篇完成两轮独立审查和终端 QA，仍为 `HOLD_EXTERNAL`。
- 当前批次原编号为 **P197–P201**，五篇 Round0 均已落盘，但论文审查重新淘汰了 **P198、P201**。原三席 P197/P199/P200 保留，替补 OR 已通过独立候选审查并按新编号 **P202** 写稿；仍缺一席，不能称本轮五篇已完成。
- P197/P199/P200 已各自完成：两轮论文审查、Round2、共六次终端冷构建、十二页最终视读及两次终端整包审计通过。P202 四页稿的论文 Review A 已通过并冻结 Round1，正在 Review B；其候选审查不计作论文审查。
- 历史五席冻结 `FIVE_SEAT_FREEZE.md` 保持原样。后续裁决以 `P198_REOPEN_ADJUDICATION.md` 和 `P201_REOPEN_ADJUDICATION.md` 为准：CMM 完整逆像机制退化为受限删除加根转子；EPF 与旧的已淘汰 OCL 完全共轭。数学进展和合格新系统必须分开计数。
- 编号上限 196 不等于 196 篇已完成论文或 196 个动力学子类。实物盘点见下文。

## 用户长期要求

每轮五篇，中间常规转换无需再确认；每篇应有清楚的数学进展；在当前动力学类型内广泛找子系统，早期信号弱或与旧系统重复时及时换方向；阶段结果落实成论文并及时 Git 同步。用户允许较长研究时间。

当前批次的详细阈值与两轮审查要求在 `docs/papers197_201_sequence/PROBLEM_ANCHOR.md`、`STANDING_WORKFLOW_AUTHORIZATION.md`、`HOSTILE_REVIEW_PROTOCOL.md`。科研结论以证据为准，不能为凑五篇把 reserve 自动升格。

## 最新已完成批次

| 编号 | 系统 | 已审定进展概要 |
|---|---|---|
| P192 | first-collision Hurwitz | 严格调度时钟、sharp tail、fixed census、全目标一步逆像和唯一最大纤维 |
| P193 | mutual-best block refinement | 同时分块手术、递归/分层时钟、全目标分量乘积 |
| P194 | least-raising crystal words | 精确权重时钟、Schur 深度多项式、完整前驱颜色判据 |
| P195 | odd-side least-neighbor trees | 奇偶分类的 fixed/2-cycle 递归结构、sharp tail、EGF 和局部纤维 |
| P196 | cyclic Gödel implication | 一步 rotation core、trace/cycle 数据、精确 gap-product 纤维 |

证据：`docs/papers192_196_sequence/phase2/ROUND2_REPORT.md`、`FINAL_QA_REPORT.md`。
归档记录为 20 页、10 次 source-only 冷构建、10 份论文审查包；作者/A/B 计数共 56,517,656。
这些是归档计数，本次历史整理没有重跑这五篇的全部数学验证。

特别保留：P192 的全 n history-set 公式及其推导的深度分布仍是猜想；P194 的 Defant–Williams 近邻文献遗漏已修复。P192 为 `OWNER_RED_AMBER`，其余四篇为 `OWNER_AMBER`，全部 `HOLD_EXTERNAL`。

## 当前恢复点

详细状态：`docs/papers197_201_sequence/PIPELINE_STATE.md`。

| 候选 | 当前状态 | 尚需完成 |
|---|---|---|
| TCSD / P197 | 个体论文内部完成，终端整包 PASS | 等待本轮其余两篇；外部 HOLD |
| CMM / P198 | 论文 Review A 淘汰：受限删除/根改接贡献塌缩 | 保留四页原稿，席位重新搜索 |
| LZK | 独立审查淘汰：P100/HF1 的分量化旧机制 | 保留淘汰证据，不分配论文号 |
| FOSP / P199 | 个体论文内部完成，四页终端整包 PASS | 等待本轮其余两篇；外部 HOLD |
| LFAS / P200 | 个体论文内部完成，四页终端整包 PASS | 窄/方阵 sharp 仍猜想；外部 HOLD |
| EPF / P201 | 与已淘汰旧 OCL 完全共轭，退出新系统席位 | 保留五页原稿及新定理，不能包装成新子类 |
| OR / P202 | 四页 Round1 冻结，论文 A 与 root 重放通过 | 论文 B、Round2 和终端 QA |

原编号对应保持不变，不覆盖 P198/P201 旧身份。接续：P202 论文 B 与 QA；MCT 单色三角形新线索正在独立候选审查，尚未编号/计为选中。三篇终端证据见 RETAINED_FINAL_QA_REPORT.md。台账为57次当前候选尝试（4选中、3reserve、50淘汰），另17历史控制、8code-only；LGB 重入淘汰、ND1 仅reserve，D2G/CCW 为已知算子/特化淘汰。旧51、50、54快照保留。研究备份62bc2108已通过97d04aec合并同步；本次三篇最终清单、P202 Round1及新侦察记录待下一次备份，不是五篇完成提交。

## 历史计数与路径

截至整理前快照：191 个编号目录、190 个不同编号、190 个含主 PDF 候选的目录；P51–P56 无当前目录；编号 96 的一个旧目录为空。此处只是实物计数，不表示历史论文全部符合今天的完成标准。

工作区 `/root/autodl-tmp/symbolic_dynamics` 本身没有 Git。镜像为 `/root/autodl-tmp/hilbert-polya-structure`，存在历史布局分裂：已跟踪的较早文件通常在 `symbolic_dynamics/` 下，P187–P196 在根 `papers/` 与 `docs/` 下。P57–P66 的当前路径未在 Git 中找到；详见异常账本，勿据此声称所有旧稿已同步。

历史说明与恢复边界：`docs/research_state/HISTORY_AND_CAVEATS.md`。
逐目录/PDF 哈希/镜像位置和整理前 50 个当前批次文件的快照：`docs/research_state/ARTIFACT_SNAPSHOT_2026-09-05.json`。

## 证据优先级与维护

已接受版本的定理/证明、审查结论、验证输出和 Git 对象高于总览文字；总览高于聊天摘要；未落盘的子代理消息仅作为待查线索。区分“已证明”“有限实验支持”“猜想”“淘汰/保留”和“待完成”。检索未命中不表示新颖性已确认。

每次批次状态实质变化时，先更新批次状态文件，再刷新本入口的最新完成批次与下一动作。历史快照保留原基线，不把它改成实时状态。模型升级不自动改变已证明结论，也不自动证明旧猜想。
