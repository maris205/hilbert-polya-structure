# 当前研究状态与恢复入口

核对日期：2026-09-05。适用主线：`henon_dynamics` 的五篇一轮研究。
本文件整理可见对话与仓库证据，服务模型切换、上下文压缩和中断恢复；
不是论文完成证明，也不覆盖仓库其他研究主线的最新状态。

## 先读这一段

- 实际研究仓库：`/root/autodl-tmp/hilbert-polya-structure`，分支 `main`。
  环境显示的 `/root/autodl-tmp/henon_zeta` 不是本轮工作目录。
- 本轮冻结证据基线为 `0596f9d680277288225062a6fdd7ad7ce116e01d`
  （`Add Route-A papers C374-C378`）。实施中实际 fetch 发现远端另有三次
  符号动力学主线提交，路径与本轮无重叠，已仅快进至
  `42725133cd3864d434fc0e6579263b1b0e944431`；本轮冻结基线不改。
- **C379–C383 已全部完成**，五包均通过 write 和随后完整 nonwrite 验收，
  独立总审通过。共 234 个材料文件、五份发布清单、24 页最终论文；全部
  最终页面的视觉检查已经闭合。当前处于五篇完成后的用户检查点，
  不得仅凭这份记录自行开启 C384–C388。
- 旧摘要中的“正在完成 C99–C103”已经过时。相关未跟踪目录是遗留材料，
  不应把当前编号退回，也不应因不属于本轮而删除。
- 模型切换后的“无活动构建代理”仅是恢复审计时的历史状态；用户批准继续后
  已重新启动 C379/C382/C383 代理，root 负责 C380。恢复时仍应重新查状态。
- 用户在整理历史后明确要求继续本轮，该授权已经执行完毕；模型切换没有
  重做已验收的旧批次。下一轮仍按五篇一轮原则等待用户确认。

## 用户长期原则

1. 优先走 skills 路线图中的 A 路线；关注 A1、A2 的实质证据。
2. 每轮五篇，每篇一个完整、独立且有明确进展的问题；用户明确反对把
   一篇文章拆成五个小步骤充数。
3. 可以大胆提出假设、扩大单篇步幅；发现模型难以形成明确增量时，
   可以更换动力学子类型。大胆假设仍须区分猜想、证明与数值观察。
4. 必须输出论文 PDF，并保留可复算材料。已通过验证的旧成果不因模型
   更换重做；失败和否证也应有具体数学结论。
5. 已授权批次内部持续推进；五篇完成后汇报并到用户检查点。用户关于
   额度重置的表述不等于要求无限新开批次。
6. 以中文交流，报告明确进展；不能把文件数量、篇数或测试数量当作
   已突破 A1/A2 或黎曼目标的替代证据。

## 路线图与证据规则

权威入口为 [Route-A evaluator](../flow_systems/skills/route-a-evaluator.md)，
版本 `0.2.0`，本次实测 SHA-256：
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。

- **A0**：内生算术起源；素数、素数幂、时钟与权重不能事后贴标签。
- **A1**：本原周期轨道、重复、方向、相位、重数、稳定性及完整性；
  严格评估还要求承载 A0 的算术信息并落实规定对照。
- **A2**：明确的动力学 zeta/Fredholm 对象及其目标零点/除子关系；
  必须锁定时钟、归一化、截断和验证域。
- **A3**：全局解析结构与算术算子关联。
- **A4**：自然量子化、幺正或散射结构，以及是否具备 Route B 条件。

原系统的周期账或行列式可以很完整，但其严格 A1/A2/A3 结论必须依照
同一目标重新评估。C379–C383 选题文档中的 expected tuple 不是最终结论；
实施中已经下调未经证据支持的 A1/A3 预期，具体以冻结评估 YAML 为准。

公共边界：`NO_BAD_EULER_OR_ROOT_NUMBER`，Route B 未获本轮授权。
不把原系统的曲线 zeta、谱公式或散射矩阵写成已经获得目标 Euler 因子、
根数、自守性、目标函数方程/零点或 Hilbert–Pólya 算子。

旧工作摘要记录使用 ARS `0.1.26`；当前技能目录提供的是 `0.1.28`。
恢复研究工作时按当前目录阅读适用技能，不能把旧技能内容当作现行内容；
这也不自动改变已经冻结的 evaluator 版本、用户授权或论文事实。

## 上一批已提交成果：C374–C378

主要依据为 [批次审查](BATCH_REVIEW_C374_C378.md)、五份发布清单及实际
文件。该报告记载三轮稿件、独立校验、符号复算、变异和确定性编译已完成。
本次恢复核对仅作静态文件/哈希审计，不冒充重新执行全部重型验收。
独立只读审计确认：五包共 200 个清单 payload 全部存在且 SHA-256 相符，
加五份清单共 205 个物理文件；清单自身哈希与批次报告一致。
报告记载的最终论文页数合计 23 页，本次未重新编译或逐页视觉验收。

| 编号 | 已提交论文主题 | 已记录严格路线结论 |
|---|---|---|
| C374 | Kummer 前像树的全层 Galois 图像与根素数密度 | A0 结构算术；A1 WEAK；A2/A3 FAIL；A4 FORMAL_HINT；EXPLORATORY |
| C375 | LPS 四元数图族的非回溯周期和谱 | A0 结构算术；A1 WEAK；A2/A3 FAIL；A4 FORMAL_HINT；EXPLORATORY |
| C376 | 平坦磁环面的 Landau 谱与磁平移 | A0 FAIL；A1 WEAK；A2/A3 FAIL；A4 NATURAL_QUANTIZATION；REJECTED |
| C377 | 周期 CLM 任意均值精确流与首极点 | A0–A4 全部 FAIL；REJECTED |
| C378 | beta-two Dyson–OU 特征值扩散的完整分拆谱 | A0–A3 FAIL；A4 FORMAL_HINT；REJECTED |

这些是最近批次的候选级判断，不是对整个仓库所有路线成果的总评级。

## 当前批次：C379–C383

规划入口：[选题报告](IDEA_REPORT_C379_C383.md) 与
[批次计划](BATCH_PLAN_C379_C383.md)。基线为上述 `0596f9d6…`，
计划日期 `2026-09-05`，确定性构建 epoch `1788566400`，
预留 obstruction 编号 `HEN-O363`–`HEN-O367`。

| 编号 | 当前选题与目标增量 | 已核对的落盘状态 |
|---|---|---|
| C379 | multibaker：绕数/重复/反演轨道账、扭曲输运行列式、扩散分支 | 完成：五页 PDF，write/nonwrite 验收与独立清单审计通过 |
| C380 | 有限 Blaschke 圆周映射：周期与乘子、解析转移谱、参数边界 | 完成：四页 PDF，write/nonwrite 验收与独立清单审计通过 |
| C381 | LSV alpha-one 间歇映射：中性点、首返分支、返回尾部及诱导算子 | 完成：六页 PDF；全分支核性与精确幂范数一结论，完整验收及独立总审通过 |
| C382 | CM 曲线 `y^2=x^3-x`：全好奇素数 Frobenius 相位、全次数闭点 | 完成：四页 PDF，write/nonwrite 验收与独立清单审计通过 |
| C383 | Friedrichs Aharonov–Bohm：连续谱、散射相位、热核与规范边界 | 完成：五页 PDF，write/nonwrite 验收与独立清单审计通过 |

“冻结”表示本轮当前工作选择；并不意味着定理已成立或其新颖性已获外部
确认。已授权在明确碰撞或无法闭合时更换模型，变更需留痕。

本轮五题最终均保留，定理、证据与论文的实际完成凭据见
[C379–C383 批次审查](BATCH_REVIEW_C379_C383.md)。选题阶段的 A1/A3
乐观预期已被正式评估下调：C379–C382 为 A1_WEAK，C383 为 A1_FAIL；
五篇 A2/A3 均为 FAIL。只有 C382 的 A0 为结构算术关系，C383 的 A4 为
幺正/散射候选。不能把这批源系统定理写成目标 A1/A2 已通过。

恢复实施时优先核验：

1. C379 的边界符号编码、`L=1,2`、绕数与 Bloch 相位是否同一约定。
2. C380 的精确函数空间、扩张范围、内外固定点谱通道与文献定理适用性。
3. C381 的复解析分支域、核性/收敛界、原时钟与首返时钟，尤其不能从
   有限截断推出无限维 Fredholm 定理。
4. C382 相对 flow papers 4/6 和现有 CM 论文的完整机制碰撞；Gaussian
   素元符号与 ordinary/supersingular 公式；native zeta 与目标 A2 的边界。
5. C383 的 Friedrichs 原点条件、散射符号、前向分布及时间反演定义。

## 纠正旧摘要和计划的读法

- C99–C103 摘要是更早的历史断点。当前恢复入口是 C379–C383。
- 曾建议的 multinacci、Bost–Connes、Hecke triangle 与 NLS 已非当前五题；
  不因中间代理报告再次把它们加入，导致超过五篇。
- PGL3 题是因缺乏已验证商复形材料而暂缓。没有找到实际执行构造预检的
  记录，因此不能称“已实验失败”或已证明不可行。
- 原代理名称和旧 session/process 编号不保证当前有效，重新查询活动状态。
- `HEAD == origin/main` 只说明当时检查的本地引用相等；发布前另行 fetch。
- 目录存在、代理收到任务、纸面 expected tuple 都不等于成果完成。

## 遗留未跟踪材料

以下内容在本次整理前已存在，保留并排除在 C379–C383 的发布暂存范围外：

- `henon_mu3_yukawa_mark_first_passage_generating_polynomial/`
- `henon_mu3_yukawa_mark_pair_dependence_geometry/`
- `henon_mu3_yukawa_mark_first_passage_triple_coupling/`
- `henon_mu3_yukawa_mark_first_passage_triple_orbit_quotient/`
- `henon_mu3_yukawa_mark_first_passage_minmax_aggregation/`
- 仓库根的 `henon_ermakov_pinney_isotonic_action_route_a/`
- 仓库根的 `henon_flat_magnetic_torus_landau_route_a/`
- 仓库根的 `henon_hysteretic_relay_oscillator_route_a/`

前五项相对本目录，后三项相对仓库根。不要执行宽泛清理或把根目录副本
与 `henon_dynamics` 下的已提交论文混为一谈。

## 下次恢复的最短流程

1. 读本文件并核对仓库、分支、`git status --short` 和最新提交；更新事实，
   不把本快照永久当作实时状态。
2. 只读当前五题的计划、相关技能与必要的既有论文；按需查
   [候选注册表](docs/candidate_registry.md)、
   [障碍注册表](docs/obstruction_registry.md) 和具体包的 `SOURCE_AUDIT.md`。
3. 查询活动代理与实际文件；按互不重叠的论文目录重新分配工作。
4. 先把每篇核心证明与证据做成可复核成果，再写作/编译/交叉审查；
   完成发布清单与总登记后按已授权工作流提交发布。
5. 每篇完成、题目更换或发生中断时更新本文件中的当前表与下一步。
   完成五篇后报告具体数学增量与严格路线结论，进入用户检查点。

## 模型切换与记忆：本次核查边界

OpenAI 官方文档把上下文压缩和跨会话 memories 分为不同配置/能力；
GPT-6 Astra 继续支持 compaction 与 persisted reasoning。
这不构成“换模型后历史全文逐字无损继承”或“此会话开启了某一记忆配置”
的证明。本次没有更改应用记忆设置、删除会话或触发手动压缩。
本文件是可阅读的项目交接记录，其可靠性来自随工作更新和仓库核对。

核查来源（2026-09-05）：
[GPT-6 模型说明](https://developers.openai.com/api/docs/guides/latest-model)、
[Codex 配置参考](https://learn.chatgpt.com/docs/config-file/config-reference)。
