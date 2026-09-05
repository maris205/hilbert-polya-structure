# 当前研究状态与恢复入口

核对日期：2026-09-05。主线：`henon_dynamics`，C 系列。
长期规则见 [AGENTS.md](AGENTS.md)；本文件只保存当前状态和证据入口。

## 最新授权与恢复动作

用户最新要求：先按最新官方指导审计优化仓库 AGENTS、skills 与 workflow，
“然后再继续”。前一批 C394–C398 已交付；研究续接范围为 C399–C403 五篇。
仓库 Astra 指令优化及独立场景检查已完成；尚未开始 C399–C403 论文。
[指令审计](../docs/agent_workflows/ASTRA_AUDIT_2026-09-05.md) 保存来源、范围和验证。
接下来按 [新工作流](../.agents/skills/henon-route-a-batch/references/WORKFLOW.md) 进入选题。
本次工作流维护不是一篇论文，不占五篇名额。

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
