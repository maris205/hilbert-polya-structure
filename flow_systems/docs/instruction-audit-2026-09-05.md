# 仓库指令审计与优化 — 2026-09-05

本次范围是仓库内的代理指令、技能入口与研究 workflow。没有修改全局 Codex 配置、已安装插件、模型运行参数、科学代码或论文证据，也没有尝试把配置优化视作既有研究 STOP 的解除。

## 依据与判断

实际检索并打开了 OpenAI 当前的 [GPT-6 Astra 指导](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)、[模型页](https://developers.openai.com/api/docs/models/gpt-6-astra)、[AGENTS.md 文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[技能文档](https://learn.chatgpt.com/docs/build-skills) 与 [子代理文档](https://learn.chatgpt.com/docs/agent-configuration/subagents)。

Astra 指导明确建议审计技能和指令文件对行为的影响，并校准自主执行、并行委派和验证强度。本次将这些建议落实为按任务加载、在已授权范围内完成工作、独立任务并行，以及通过相关检查后不无理由扩大验证。没有把“最大化性能”解释为降低研究标准或强制最高 reasoning；也没有进行延迟、成本或模型能力基准测试。

官方发现规则使用 `AGENTS.md` 与 `.agents/skills/<name>/SKILL.md`。仓库原有的两份 evaluator 是科学规范引用，不是这种标准技能目录。新技能只提供有边界的入口，不复制判据正文。`AGENTS.md` 的自动加载通常在会话启动时完成；本轮已显式读取并按新规则执行，新会话的客户端自动发现尚未单独实测。

## 发现与处置

| 发现 | 处置 |
| --- | --- |
| 优化前完整路径盘点未发现标准 AGENTS、SKILL 或 workflow 文件；包括隐藏及忽略文件，共 5,815 个文件、407 个目录。 | 新建一个根入口、一份 workflow 和两个窄范围技能入口。 |
| `codex_prompt.md` 以 312 行重复批次流程，引用不存在的 `propose.md`，并直接要求启动批次、逐篇 commit/sync。 | 改为 14 行续接入口，使用实际 proposal 路径；新批次规则集中到 workflow，仅在对应授权下启用。 |
| 两份 evaluator 共 31,464 字节，存在真实的 SHA 绑定及调用者。 | 保留原始路径、字节、数学门槛和输出 schema；按需加载的新入口分别为 1,786 与 1,846 字节。 |
| README 和历史 BATCH 文档混有过往“当前状态”“下一次确认”等文字。 | 将其定位为导航和历史材料，执行依据回到对应用户授权、输入锁及结果记录；没有批量重写历史。 |
| `audit_*`、`reproduce.sh` 等名字不能说明是否写文件；不少工具固定轮次、旧时间、路径或 canonical 输出。 | workflow 要求检查实际输入和副作用，没有虚构统一测试命令，也没有试跑研究脚本。 |
| 完整 Route 评估、局部门槛说明、普通代码维护容易混用。 | 技能描述和正文明确分流；局部审查不得输出整体通过，审查请求不自动授权实验或登记写入。 |

`propose-flow-systems.md` 保留为完整科学方案，包含旧同步布局示例；其操作性文字必须在当前任务授权下解释。Jupyter checkpoints、历史 BATCH 文档、所有论文状态和外部 ARS 插件均未改写。未检查或改动全局自定义 fallback 配置。

## 修改清单

- [AGENTS.md](../AGENTS.md)：23 行，3,166 字节；保留常驻的仓库导航与关键约束。
- [workflow.md](workflow.md)：任务分类、阶段续接、执行、验证、交付及新批次政策的单一入口。
- [codex_prompt.md](../codex_prompt.md)：6,033 → 1,031 字节，减少约 82.9%；不再复制整套批次规则。
- [flow-route-a/SKILL.md](../.agents/skills/flow-route-a/SKILL.md) 与 [flow-route-b/SKILL.md](../.agents/skills/flow-route-b/SKILL.md)：可发现的窄范围技能入口。

减少的是默认与重复加载的指令负担；因为原始科学规范仍保留，以上不是仓库总字节减少或模型速度提升的测量。

## 验证

两个技能分别通过随 `skill-creator` 提供的 `quick_validate.py`，退出码均为 0。五份执行入口的 10 个 Markdown 本地链接均可解析到存在的目标。该检查只验证格式和路径，不证明模型行为或研究结论。

本次修改前后，proposal 与两份原始协议的 SHA-256 一致：

| 文件 | SHA-256 |
| --- | --- |
| `propose-flow-systems.md` | `c3fb9885b96b9182661e86b5def7cc7eaebb6ad9b847eced6b0c342427c9b88d` |
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |

一个未接收先前研究审计结论的独立子代理完成了四个只读决策场景：普通拼写修正、仅解释 Route-B 自伴性、继续已有 STOP 的审计、对零点拟合候选做局部 A0 审查。分别保持局部维护、概念解释、既有停止边界和有依据的单项失败判断，没有把这些请求扩展成研究执行或整体通过。拼写场景没有给出具体错字，代理正确保留了询问目标词句的可能性。

该检查暴露的两处措辞摩擦已修正：workflow 现在只要求检查受影响部分，拼写更正无需完整技能评估；Route-A 入口明确区分已知门槛失败与完整评估的可测试性。修改后的 Route-A metadata 再次通过验证，其他已通过且未受影响的检查没有重复执行。

这是一组决策演练，不是端到端客户端加载测试、正式研究评审或性能基准。未运行论文审计重播、科学测试、PDF 构建或 Git。

## 原研究任务的续接边界

此次优化前，P30 的 [STOP 记录](../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round3_p30_STOP_reader_manifest_mismatch.json) 已保存：历史 reader manifest 的 `/entries/7` 未通过联合字节数/SHA 检查，其余 10 项通过。失败目标是 `notes/stage4_prime_claim_passage_matrix_round2.json`。原诊断只打印布尔结果，不能由此断言究竟是字节数、SHA 还是两者不符。

这不是一个已完成的 Stage 4.5 Round 3 最终审计，也不等于最新五稿输入锁已经失配。相关未完成工作和原始检索记录继续保留；本次没有重试该检查或修复任何输入。

继续研究的最小待授权动作是：仅只读定位 P30 这一个历史描述符与目标的差异，区分历史快照问题与当前证据依赖，提出具体的最小处理方案。不得在定位过程中更新清单、覆盖证据、生成新的通过结论或推进 Stage 5/6。
