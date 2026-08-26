# 论文 9–13 创建、审查与完整性流程记录

日期：2026-08-16（Asia/Shanghai）  
范围：论文 9、10、11、12 与论文 13 技术说明  
阶段：ARS Stage 6 流程总结（待用户终止确认）  
批次技术结论：**PASS — C0/M0/m0**  
公开发布：**`PUBLIC_RELEASE_AUTHORIZED=false`**

## 1. 证据边界

本记录依据当前工作区的精确字节、追加式审查报告与批次审计编制。
早期原始对话已在长会话压缩中不可见，因此不能伪造最初提示词、轮次号或
用户逐次干预次数。当前唯一可安全逐字引用的用户原话是：

> “继续”

该指令发生在五篇论文的 Stage 5 交付与批次审计完成之后，作为进入 Stage 6
流程总结的明确同意。更早的任务范围只能从冻结工件推断，不能作为逐字引语。
本记录把“工件证据”“合理推断”和“评价建议”分开处理。

主上游收据：

- 批次审计：`papers/9-packet-separation/notes/papers9_13_batch_audit.md`
- SHA-256：`6aa915a9e85153957b269448ba23b56716c4f64d18e6b3c85f904d73b0001aea`
- 上游哈希图：65 个当前节点、255 条边、0 自环、0 环路。

## 2. 论文与最终交付物

| 论文 | 最终定位 | PDF 页数 | PDF SHA-256 |
|---|---|---:|---|
| P9 | 内部接受的论文包 | 21 | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |
| P10 | 内部接受的论文包 | 19 | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |
| P11 | 内部接受的论文包 | 16 | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |
| P12 | 内部接受；保留 `STANDALONE_PASS` | 18 | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |
| P13 | 内部接受的 **Technical Note** | 15 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |

每个 `paper/` 目录均恰有六个普通文件：README、TeX、BibTeX、两个原生
TikZ 图源和一个 PDF；没有符号链接、辅助文件、第二个 PDF 或研究源 PDF。

论文 13 的独立实质性判定仍为 `NOTE_OR_MERGE`、`STANDALONE_PASS=false`、
`C0/M1/m0`。该 Major 是采用技术说明定位的理由，而不是被本记录消除的缺陷。

## 3. 逐阶段流程

| 证据对齐阶段 | 主要输入 | 产出与关键决定 | 迭代／纠错 | 最终门禁 |
|---|---|---|---|---|
| 1. 批次接收与候选冻结 | P9–P13 协议、候选锁及前序论文边界 | 建立五个所有者类型明确的项目；在批次边界统一交付 | 原始提示词不可见；不得补写 | 历史 `pipeline_state.md` 仅作当时门禁快照 |
| 2. Phase 1 设计重锁 | 方法、devil/domain、source-feasibility 审查 | 五篇论文最终 Phase-1 均归零 | P9 两态；P10 两态；P11 两态；P12 初版/v1/v2；P13 初版/v1 | 全部最终 `C0/M0/m0` |
| 3. Phase 2 来源与先例 | 来源 PDF、所有者词典、有限先例搜索 | 来源、术语、所有权和新颖性上限 | 搜索结论始终保留 `SUPPORTED_WITHIN_SEARCH` 边界 | 不把有限搜索升级为绝对优先权主张 |
| 4. Phase 3 证明与控制设计 | 锁定主张和来源上限 | 稳定证明、反例、确定性控制设计 | P12 经 v2/v3/v4；P13 经初版和 v2 corona 强化 | 数学包通过；standalone 另行裁定 |
| 5. P13 控制修复 | 第一版实现与独立 mutation probes | 替换 manifest `26a41e…094c2` | 第一版因 lookup/self-comparison oracle 不独立而判 `C0/M1/m0`；修复后再运行与独立复核 | 176/176、12 CSV、2665 行、67/67 负控，PASS |
| 6. 发布形态裁定 | 证明、来源、控制与 standalone 审查 | P9–P12 保留论文定位；P13 进入 Technical Note | P12 v4 关闭 routine-reduction Major；P13 明确保留 Major | `PASS_TO_TECHNICAL_NOTE`，不虚称 standalone |
| 7. Route 评估 | 稳定证明和控制收据 | 40 份 Route-A YAML | 25 exploratory、15 rejected | 120 个 A2–A4 坐标全部 FAIL；Route B 为 0 |
| 8. 组合与引文预检 | proof/Route tuple、来源上限 | 五份 composition blueprint；英文正文和独立简体中文摘要 | 先冻结结构、主张顺序、图表追踪与声明边界 | blueprint 不增加数学证据 |
| 9. 稿件审查与重锁 | TeX、Bib、图源、PDF | 五个六文件稿件包 | P9 初稿 C1/M8 后接受；P12 Freeze 1→2→Correction→count relock；P13 Freeze 1 C0/M2/m1→Freeze 2→status relock | 当前稿件包全部技术 `C0/M0/m0` |
| 10. P12 有界纠错 | P12 Review Freeze 2 | 正确 Bib/PDF 与 citation→peer→release 追加链 | Stacks 题名改为 “Colimits of spaces”；中文计数改为 353 正文 + 32 关键词 = 385 | 两个历史 m1 均透明关闭 |
| 11. 引文、同行与发布审计 | 最终稿件 tuple | 每篇 citation、peer、release 报告 | P11–P13 有追加式状态重锁 | 所有当前引用图闭合、技术 PASS |
| 12. 五篇批次审计 | 五个当前学术 tuple 与状态文档 | 统一的精确字节、PDF、来源、Route、控制和哈希图收据 | 修复 P9 报告边、P11/P12/P13 状态表述；校正图方向术语 | `PASS — C0/M0/m0`，公开发布仍 false |

## 4. 最小可证迭代计数

这里统计的是工件中明确命名的状态，而不是推测对话轮次。

| 论文 | 设计状态 | 证明／定位状态 | 稿件／终局状态 |
|---|---:|---:|---:|
| P9 | 2 | 1 个稳定证明包 | 2：初稿与接受重审 |
| P10 | 2 | 1 个稳定证明／控制包 | 至少 2；含一次最终空格 Minor 重锁 |
| P11 | 2 | 1 个稳定证明／控制包 | 至少 2 个引文状态，另有一条状态重锁链 |
| P12 | 3 | 3：v2/v3/v4 | 4：Freeze 1、Freeze 2、Correction、count relock |
| P13 | 2 个 Phase-1 状态、3 个控制设计状态 | 2 个 standalone 状态、2 个控制实现 | 3：Freeze 1、Freeze 2、status relock |

## 5. 完整性统计

| 项目 | 汇总 |
|---|---:|
| 单元测试 | 399/399 |
| CSV | 53 |
| CSV 正文行 | 7,709 |
| 显式负控 | 86 |
| Route-A | 40 |
| exploratory / rejected | 25 / 15 |
| Route-B | 0 |
| 本地保留研究 PDF | 32 |
| 复用审计 manifestation | 3 |
| PDF/preflight 审计对 | 35 |
| 五个稿件 PDF 总页数 | 89 |
| 总字体数 | 39，全部 embedded/subset/Unicode |

五个保留的稿件 PDF 均为 A4 PDF 1.5、无加密、无附件、无光栅图；Ghostscript
解析通过。
研究源 PDF 仅保留于 `notes/sources/`，未进入任何 `paper/` 包。

## 6. 关键方向修正

1. **不能把标准材料的组合包装成 standalone。** P12 通过 v4 的同载体
   标准化/H1 对角不变量关闭了早期 routine-reduction Major；P13 的 corona
   结果经扣除前序贡献并独立复核后，仍是一般等距对角引理的实例，因此转入
   Technical Note。
2. **控制必须独立失败关闭。** P13 第一版 CSV 字节虽正确，但若 detector 只是
   查 token 或两边使用同一公式，不能证明 oracle 独立。修复后才以替换 manifest
   进入下游。
3. **所有者和类型优先于叙事。** P12 曾发现 packet 非 transitive、Route owner、
   态射方差与同载体标准化不一致等风险；每次均通过版本化锁而非文字掩盖处理。
4. **元数据也属于完整性。** P12 的 Stacks 题名错误和中文计数约定错误都在
   批次阶段作为 m1 公开保留并追加关闭。
5. **报告边也要无环。** P9 的临时 `paper.log` 只能作为历史收据；P13 最终
   README 由批次审计向下绑定，不制造自哈希或反向循环。

## 7. 用户关键决定与可归属贡献

压缩会话摘要（不是可逐字引用的原始 turn）记录了五篇批次范围、整体自动委派和
审计闭合前的 no-Git/no-public-sync 约束；冻结工件佐证了批次范围与发布 hold。
当前唯一可逐字归于用户的原话仍是“继续”。早期逐字指令已经不可见，因此不把
agent 发现的错误、数学修复或审查结论归功于用户。

可见的用户价值主要是工作范围、自治程度、继续执行和发布边界的选择。证明撰写、
来源核验、错误发现、重锁和技术闭合应归于 AI/审查流程，除非未来提供完整原始对话
证明另有人工贡献。

## 8. Collaboration Depth Trajectory（建议性）

该评价采用 Wang–Zhang rubric v1.0，非论文质量评价，永不阻断流程。因原始早期
对话缺失，分数为低至中等置信度的临时值。

| 维度 | 分数 | 观察 |
|---|---:|---|
| Delegation Intensity | 8/10 | 整类任务被批量委派，不是零散微调 |
| Cognitive Vigilance | 4/10 | 流程设置了强审计门禁，但可见对话没有用户主动质询证据 |
| Cognitive Reallocation | 3/10 | 可见记录没有用户原创综合、反论证或定理级判断 |

**Zone 2 — Mid, automation-dominant。** Zone 3 需要三个维度都至少为 7；当前
只支持高委派。Zone 1 也不成立，因为 AI 使用显然很强。未来若希望形成可审计的
Zone 3，可在每个主要门禁人工抽样挑战一个核心定理或引文，记录 article-type 与
release-boundary 的人工理由，并在每次纠错后写出一条原创综合。

## 9. AI 自我反思

### 9.1 行为摘要

AI 采用了高并行、强锁定、追加式审查策略。优点是独立 reviewer 能多次推翻过早
的 PASS；缺点是状态文档和哈希边发生了过多微小重锁，增加了协调成本。这个反思
由同一 AI 系统生成，不能被当作独立外部评价。

### 9.2 指标与 sycophancy 风险

| 指标 | 结果 |
|---|---|
| DA concession rate | `UNMEASURED`；压缩后的日志不足以重算分母 |
| 连续 concessions | `UNMEASURED` |
| skipped checkpoints | `UNMEASURED`；自动授权将多个非强制 checkpoint 合并到批次边界 |
| 可见 user overrides | 0 |
| 可见 health alerts | 0；完整历史总数 `UNMEASURED`，不是“无风险”证明 |
| Intent-mode transitions | `UNMEASURED`；可见的 Stage 5→6 是阶段迁移，不是 exploratory↔goal-oriented 模式变化的证据 |
| cross-model disagreements | 未启用 cross-model |

因此 sycophancy 风险评级为 **UNMEASURED / 需人工阅读**，不能因 health alert 为 0
就标为 LOW。独立审查多次阻止错误 PASS，说明防线实际工作；但这不替代原始对话
级的 concession 统计。

### 9.3 AI 做错了什么

- P12 初始 Bib 把 Stacks Tag 0B1W 写成 “Topological colimits”，且早期 citation
  PASS 未发现。
- P12 中文摘要曾用 `Script_Extensions=Han` 得到 370，把 17 个标点误计入正文。
- P13 Freeze 1 的六键 trace、父 README 状态和 Han 计数不一致。
- P13 第一版控制允许 tautological/detector-token oracle 通过，必须有界修复。
- P12 控制审计曾出现并行 reproduce 编排事故；最终虽清理且未污染结果，但暴露了
  runner 协调问题。
- P13 README 状态指针在终局阶段多次变动，造成不必要的重锁链。
- 批次报告曾把按“referrer→prerequisite”方向的新报告称为 sink；独立机器复核后
  改为 source。

### 9.4 七类失败模式审计日志

本批次没有统一、当时生成的 ARS v3.20 Stage 2.5/4.5 七项日志。P11--P13 的
最终引文审计包含逐篇七项表，P9--P10 没有对应表；下表只是 Stage 6 对五篇最终
证据的追溯综合，不替代缺失的正式记录。

| 模式 | 追溯评价 | 历史与解决 |
|---|---|---|
| 1. implementation bug passing self-review | CLEAR | P13 控制 oracle 曾被独立 mutation probe 判疑；替换实现和独立复跑后关闭 |
| 2. hallucinated citation | CLEAR | 引文图全部闭合；P12 题名属于真实来源的元数据 m1，已纠正并重锁 |
| 3. hallucinated experimental result | CLEAR | 所有有限结果均绑定 CSV/manifest；P13 第一 manifest 明确排除，不进入证据 |
| 4. shortcut reliance | CLEAR / 理论论文边界 | 有限控制明确声明仅诊断，不升级为连续或一般性定理 |
| 5. bug reframed as insight | CLEAR | oracle 缺陷没有被写成数学贡献；先修控制再允许下游 |
| 6. methodology fabrication | CLEAR | 测试数、行数、负控、构建命令和 PDF 收据均由稳定字节复核 |
| 7. early frame-lock | CLEAR at final scope | 多个 standalone 强化被反例/先例审查降级；P13 最终诚实采用 Technical Note |

无用户 override 记录。

## 10. 协作质量评价（临时、低至中等置信度）

| 维度 | 分数 |
|---|---:|
| Direction Setting | 88 |
| Intellectual Contribution | 45 |
| Quality Gatekeeping | 78 |
| Iteration Discipline | 80 |
| Delegation Efficiency | 92 |
| Meta-Learning | 47 |
| **等权总分** | **72/100 — Good** |

做得有效之处：批次范围明确、委派粒度高、发布前设置了 no-Git/no-public-sync
边界，并允许审查循环持续到精确字节闭合。可改进之处：在关键数学和来源门禁加入
可见的人工作证；对 P13 article type 给出人工裁定理由；在每次重大纠错后记录一条
用户自己的方法论反思。

## 11. 可复用经验

- 正确的工件字节不等于正确的控制 oracle；必须做 mutation probe。
- standalone 价值需要在扣除前序论文和标准引理后独立审查。
- `pipeline_state.md` 应解释为历史快照，当前状态由后续精确收据决定。
- README、citation、peer、release 和 batch 报告必须按无环方向绑定。
- 源 PDF 的本地存在与公开载荷排除是两项不同的门禁；没有真实 Git/archive/
  fresh-clone 检查就不能声称公开安全。
- 中文计数必须冻结 Unicode 属性、文本边界和关键词是否计入。

## 12. 外部发布门禁与终止状态

以下仍由人类或真实发布系统决定：作者顺序、单位、通讯作者、ORCID、CRediT、
经费、利益冲突、致谢、伦理/同意适用性、最终 AI/tool disclosure；未发表伴随论文
的不可变公开身份或获批自包含替代；期刊/文章类型、模板、引文风格、许可证、
可访问性和投稿日 DOI/撤稿/勘误/政策刷新；以及真实 Git/index/LFS/archive/upload/
attachment/hidden-path/fresh-clone 源 PDF 排除检查。

本流程记录不执行 Git、提交、推送、归档或上传。Stage 6 在交付本记录后保持
`in_progress`，直到用户用“完成”“确认”“结束”或等价明确表达接受交付物。
