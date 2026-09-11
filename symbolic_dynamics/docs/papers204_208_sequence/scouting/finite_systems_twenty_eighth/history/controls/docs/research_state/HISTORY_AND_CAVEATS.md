# 历史整理与证据边界

日期：2026-09-05 UTC。入口：工作区根 `SYMBOLIC_DYNAMICS_STATE.md`。
本次对既有研究材料做只读盘点，新增恢复/索引文档并更新总览；没有重审全部论文，没有改变既有定理、论文编号或历史审查结论。

## 为什么需要文件化恢复

长会话包含临时猜想、后来撤回的方向、子代理未交付的任务，以及不同阶段的完成口径。
模型切换或上下文压缩后，先读当前状态，再按具体任务读取论文/审查/验证原件。
聊天中的“P1–P196 已完成”不能覆盖下面的缺号、旧稿审核状态与 Git 缺口。

OpenAI 官方模型指南列出 GPT-6 Astra 的长任务一致性及 compaction 支持；这不能推出本会话的记忆机制具体变化，也不能保证所有历史细节无损恢复。
参考：[model guidance](https://developers.openai.com/api/docs/guides/latest-model)、[compaction API](https://developers.openai.com/api/reference/java/resources/responses/methods/compact)。
本项目采用文件/Git交接是工程选择，不是对模型内部记忆实现的断言。

## 研究历史的阅读分段

这些分段用于导航，不把不同年代的验收门槛视为相同。

| 时段 | 研究内容与状态 | 阅读入口（工作区相对路径） |
|---|---|---|
| P1–P3 | 初始六候选反证优先审计；wheel-sieve 精确时钟继承受阻 | README 中对应历史段落；papers/01-* 至 03-* |
| P4–P18 | tensor-prime/Euler、分级行列式、Gamma 通道、谱运动、recurrent trace，以及相关闭路与消去障碍 | README 的 P4–P18 逐篇段落 |
| P19–P43 | 编译器、symbolic grammar、incidence、affine/Mayer 等算术选择与算子继承审计 | README；P39/P40 路线审计 |
| P44–P50 | q-adic 边界、weighted operators/Schatten、tree 与 Toeplitz 结果 | docs/papers44_48_sequence；P49/P50 HANDOFF.md |
| P51–P61 | 转向更广 symbolic 系统；P51–P56 仅有历史主题线索，P57–P61 有本地实物 | P177 批 TITLE_COLLISION_INVENTORY；papers/57-* 至 61-* |
| P62–P116 | 五篇一轮的跨系统探索：substitution、SFT/sofic、IET、trees、随机过程、有限代数等 | 各 docs/papers*_sequence 的阶段报告与碰撞账本 |
| P117–P151 | 明确 breadth-first、早期精确结构信号、持久淘汰记录和多条定理输出 | docs/papers117_121_sequence/PROBLEM_ANCHOR.md 起 |
| P152–P196 | 九轮、45 个论文包；各批记录六阶段完成和外部 HOLD | 九个批次 PIPELINE_STATE.md 与 FINAL_QA_REPORT.md |
| P197–P201 | 当前 Stage 1，未凑齐五席，未正式编号 | docs/papers197_201_sequence/PIPELINE_STATE.md |

## 三套“进度”不能互换

1. 原始 Hilbert–Pólya 路线用 A0–A4 衡量算术来源、轨道/算子和完成结构。
   P6/P7/P8 留下 Euler–Gamma、chiral motion、recurrent trace 的重要局部结果；
   尚无同一系统的统一 completed determinant/divisor 闭环。历史 README 的局部
   GO/A3 描述不能读成 A4 已通过或 Route B 已开启。
2. 后续短论文的 Stage/Round 标记是研究和写作流程，不是 A0–A4 数学层级。
   Stage 6 完成表示本批次协议闭合；不表示 Hilbert–Pólya 目标推进到“第六层”。
3. 文件存在、论文内部验收、来源界定、Git 备份是四种分别记录的状态。
   内部通过和大量有限断言都不证明新颖性，也不等于完成全部历史审核。

## 计数规则与盘点结果

整理前 Git 基线：`76146ba17eb15beccfc38e625427f8da726db919`。

| 量 | 结果 | 正确解释 |
|---|---:|---|
| 本地编号目录 | 191 | 包含一个空的旧 96 目录 |
| 本地不同编号 | 190 | P1–P50、P57–P196 |
| 有代表 PDF 的目录 | 190 | 存在性检查，未对全部稿件重新验收 |
| Git 已跟踪的不同论文编号 | 180 | P1–P50、P67–P196，跨两种布局 |
| 本地有、Git 历史未找到的论文编号 | 10 | P57–P66 |
| 当前批次整理前文件 | 50 | 全部为候选/控制/筛选材料，零篇论文 PDF |

P117–P196 是16轮、80个编号论文包；P152–P196 是9轮、45个记录了当前六阶段闭合的包。
这些都不是严格数学意义下的“独立子类数”。各批 breadth ledger 的单位、重复控制和 reserve 重入
规则并不完全相同，不能把其数字相加当作全历史去重系统数。没有建立同构/共轭/因子等价关系下的
统一子类总表，因此当前不提供“总共验证了 N 个子类”的伪精确数字。

## 异常账本

| 项目 | 经检查的事实 | 本次处理 / 尚未解决 |
|---|---|---|
| 根 README 过时 | 最新完成标题停在 P167–P171，69 是该批宽度语境 | 新增当前入口和 P192–P196 状态，旧段标为历史快照 |
| P51–P56 缺号 | 当前工作区与已检查 Git refs 无论文目录；后续记录提到从 /tmp 恢复主题 | 保留缺口，不补造论文，不重新编号 |
| P57–P66 同步缺口 | 本地有 TeX/PDF；Git 路径/内容历史审计未找到相应稿件，docs/papers62_66_sequence 亦未找到 | 登记为本地材料，历史回填仍待专门执行；本次不宣称已同步 |
| 双 96 | 正式 P96 是 finite-subset-circle-expansion；equal-window-sum-torsion-shifts 是空的未跟踪旧目录 | 快照保留两目录，正式论文只计一次；没有移动或删除 |
| P49/P50 | HANDOFF.md 明写 HOLD_FOR_INDEPENDENT_WRITER_AUDIT，STATUS.txt 另记 HOLD_FOR_FRESH_INDEPENDENT_PRE_RUN_REAUDIT，并引用历史 /tmp overlay | 两种层级均仍 HOLD；文件存在可确认，不自行关闭旧审计要求 |
| 论文 README 的旧阶段 | 例如 P192 仍强调 Review-A repair，而批次记录已完成 Review B 和终端 QA | 以已接受版本与批次终端证据判定；本次不改封存论文以免破坏 manifest |
| Git 路径分裂 | P187–P196 新增在仓库根，其余已跟踪流文件在 symbolic_dynamics 下 | 明确映射，不重排历史文件 |
| 当前批次未归档 | 整理前的50个文件尚未进入 Git | 以 WIP/history checkpoint 归档；不是完成五篇 |
| 当前 replacement algebra verifier | 只读运行报 negative shift count，缺 contract/canonical | 保留失败 WIP；不列为第五席，不计入 PASS |
| 聊天中的候选评价 | LZK/FOSP 被称为强候选，但没有独立候选 gate 文件 | 中央状态明确标为 gate pending |

## Git 路径映射

工作区为 `/root/autodl-tmp/symbolic_dynamics`；Git 镜像为 `/root/autodl-tmp/hilbert-polya-structure`。

| 内容 | 工作区相对位置 | Git 相对位置 |
|---|---|---|
| 已跟踪 P1–P50、P67–P186 | papers/<slug> | symbolic_dynamics/papers/<slug> |
| P57–P66 | papers/<slug> | 尚无已确认位置 |
| P187–P196 | papers/<slug> | papers/<slug> |
| 较早已跟踪批次 | docs/papers*_sequence | symbolic_dynamics/docs/papers*_sequence |
| P187–P196 两批 | docs/papers*_sequence | docs/papers*_sequence |
| 当前 P197–P201 WIP 及新历史索引 | docs/papers197_201_sequence、docs/research_state | 同路径，仓库根 docs 下 |
| 新恢复入口 | SYMBOLIC_DYNAMICS_STATE.md | 同名，仓库根 |
| 本流 README/AGENTS | README.md、AGENTS.md | symbolic_dynamics/README.md、symbolic_dynamics/AGENTS.md，入口链接调整一级 |

上述映射按实际路径记录；论文包内部文件与 manifest 不因本次索引工作重写。

## 可重复的盘点

`inventory.py` 只读目录、代表 PDF 哈希和 Git 跟踪路径，输出 JSON，不写研究文件：

```bash
python3 docs/research_state/inventory.py /root/autodl-tmp/symbolic_dynamics /root/autodl-tmp/hilbert-polya-structure
```

`ARTIFACT_SNAPSHOT_2026-09-05.json` 固定在整理前的 Git/候选文件基线，后续增加状态文件或
Git checkpoint 后当前输出自然会不同。`PAPER_ARTIFACT_INDEX.tsv` 是从同一快照提取的
代表 PDF 索引，列出工作区路径、Git路径和 SHA-256。它不取代论文内的 canonical manifest。

## 淘汰知识的读取方式

进入任何新系统前，检索全体已发表编号材料与历史 scouting/kill ledger；空缺号的主题线索
仍保留为碰撞警示，但不能假装已读过不存在的论文。优先检索 literal update 与 proof engine，
不要只搜新命名。当前的 CSL 因 `C=rho^{-1}D^2` 精确归约到 TCSD；LSPO、SCT 有直接历史
重复；GBE 是标准 Bellman closure；SDD/LFAS 仍为 reserve。完整证据见当前批次状态文件。

未落盘消息中的其他淘汰（例如代码 shortening 方向）只能当待查线索；落入正式中央结论前，
补上对应旧文/旧 scout 的具体路径与确切映射。
