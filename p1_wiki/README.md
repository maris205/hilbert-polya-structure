# P1 RH 探索知识库

这是 `hilbert-polya-structure` 第一阶段 Riemann Hypothesis / Hilbert--Pólya 探索的**导航型知识库**。它为下一位 agent 提供六条研究线、论文包、结论边界、路线图和原始材料之间的稳定入口；它不替代原始论文、冻结输入、评估记录、收据或授权。

> **先读边界。** 这里的页面是源绑定的导览与派生阅读副本，不是新的数学证明、Route 评估或研究授权。任何关于 RH、零点识别、素数迹公式、全局行列式或自伴算子的声称，都必须回到相应方向的原始来源、台账和正式评估。

## 整体路线图

![Hilbert--Pólya 动力学研究整体路线图：Route A（A0--A4）与 Route B（B1--B5）。](rh_roadmap0.png)

这张图是本知识库的总体导航图：Route A 从算术相关性、轨道和动力学 zeta 层逐步走向可提升性；Route B 则把候选对象推进到算子定义、自伴性、谱型、素数幂迹与完成的 \(\Xi\)/行列式恒等式。图中的完整性边界也与本库的既有原则一致：只有 B1--B5 全部闭合，才构成完整的 Hilbert--Pólya realization。

它用于定位探索方向与证据义务，不覆盖任何方向原始材料中的 source lock、当前状态、停止条件或 claim boundary，也不表示任一 Gate 已闭合。实际进展请先读[状态与 claim 词汇](01-status-and-claim-vocabulary.md)，再进入相应方向的 `conclusions.md` 和 `roadmap.md`。

## 六条顶层研究线

| 时段 / Session | 方向 | 核心张力 | 从哪里开始 |
|---|---|---|---|
| 早期自由探索 | [zeta_mvp0](directions/zeta_mvp0/index.md) | 原生结构 programme；另有不可提升的 RH 参考档案 | [原生 programme 与导入档案](directions/zeta_mvp0/index.md) |
| Session 1 | [Logistic Dynamics](directions/logistic_dynamics/index.md) | 离散 vs 连续 | [结论与边界](directions/logistic_dynamics/conclusions.md) |
| Session 2 | [Hénon Dynamics](directions/henon_dynamics/index.md) | 低维 vs 高维 | [结论与边界](directions/henon_dynamics/conclusions.md) |
| Session 3 | [Symplectic Map](directions/symplectic_map/index.md) | Hamiltonian chaos；耗散 vs 保守 | [结论与边界](directions/symplectic_map/conclusions.md) |
| Session 4 | [Symbolic Dynamics](directions/symbolic_dynamics/index.md) | 符号 vs 几何 | [结论与边界](directions/symbolic_dynamics/conclusions.md) |
| Session 5 | [Flow Systems](directions/flow_systems/index.md) | 经典 vs 量子 | [结论与边界](directions/flow_systems/conclusions.md) |

Flow Systems 内部另有一组受统一冻结计划组织的五种连续时间形式；它们属于 Session 5，而不是第七条顶层路线。见[专题：P24--P28 五种计划形式](collections/flow-p24-p28-five-planned-forms.md)。

## 阶段性工作论文

[《AI-Guided Exploration of Arithmetic Dynamical Systems》](phase1_ai_guided_exploration/README.md)（[正式 PDF](phase1_ai_guided_exploration/latex/manuscript.pdf)）以本页路线图为证据义务图，整理第一阶段的人机协作探索、局部结果、负对照与下一阶段的候选准入条件。它是固定材料窗口上的内部工作论文，不是 RH 证明、Route 评估替代品或外部同行评审结论。

## 推荐的 agent 阅读顺序

1. [Agent 起始页](00-agent-start.md)：先确定任务是导航、阅读、复现审计还是另需授权的研究动作。
2. [状态与 claim 词汇](01-status-and-claim-vocabulary.md)：不要把“流程完成”“有 PDF”或“局部定理”读成 Route 推进或 RH 结论。
3. [六线关系图](02-cross-stream-relationships.md)：识别概念谱系与正式依赖之间的区别。
4. 进入一个方向的 `conclusions.md`、`roadmap.md` 和 `sources.md`，再按其 `paper-index.md` 定位逻辑论文包。
5. 在需要连续阅读时才打开该包的 `fulltext.md`；它是由原始 TeX 派生的阅读副本，源 TeX/PDF 仍为权威文本。

## 内容布局

| 位置 | 用途 |
|---|---|
| [directions/](directions/index.md) | 六条顶层方向的摘要、边界、路线图、来源和论文索引 |
| `directions/<direction>/papers/` | 每个逻辑论文/项目包的一张来源卡和（可用时）TeX 派生全文 Markdown |
| [collections/](collections/flow-p24-p28-five-planned-forms.md) | 跨页面但不改变方向归属的专题集合 |
| [meta/](meta/README.md) | 生成清单、来源哈希和转换记录 |
| [tools/](tools/build_paper_corpus.py) | 可重复运行的论文 Markdown 生成器 |

## 生成与可复现性

`tools/build_paper_corpus.py` 选择每个逻辑包的规范 TeX 候选，生成 `paper-index.md`、来源卡、全文阅读副本和 source-hash manifest。它不会改动原始研究目录；无规范正文的项目也保留一张明确标记为 `no-canonical-fulltext` 的卡，而不会虚构论文内容。

从仓库根运行：

```bash
python3 p1_wiki/tools/build_paper_corpus.py
python3 p1_wiki/tools/build_paper_corpus.py --check
```

关于本知识库的定位、术语和停止条件，以[状态与 claim 词汇](01-status-and-claim-vocabulary.md)为准。
