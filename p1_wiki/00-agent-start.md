# Agent 起始页：安全阅读与下一步定位

[P1 Wiki 首页](README.md) · [方向总览](directions/index.md) · [状态与 claim 词汇](01-status-and-claim-vocabulary.md)

## 在开始前先分流

| 你的任务 | 首先打开 | 不应自动做什么 |
|---|---|---|
| 理解某一方向当前到了哪里 | 该方向的 `conclusions.md` | 把“完成”扩大为 RH 或 Route B 结论 |
| 理解为何这样设计 | 该方向的 `roadmap.md` | 把路线图中的候选步骤当作已执行结果 |
| 找论文、数据、收据、源锁 | `sources.md` → `paper-index.md` → 包卡 | 以派生 Markdown 取代源 TeX/PDF 或冻结记录 |
| 阅读一篇主文稿 | 包卡 `index.md` → `fulltext.md` | 忽略 `source_path`、哈希、状态或适用范围 |
| 复现实验/审计 | 原包 README、输入锁、receipt、项目 AGENTS/workflow | 因看到旧脚本而重跑或重写冻结产物 |
| 提出新研究动作 | 该方向的停点、重开门和授权材料 | 把知识库导航当作新的研究授权 |

## 最短可靠路径

1. 读[状态与 claim 词汇](01-status-and-claim-vocabulary.md)，尤其区分 `completed`、`PASS`、`EXPLORATORY`、`UNASSIGNED`、`NOT_APPLICABLE` 与 `HOLD_EXTERNAL`。
2. 在[方向总览](directions/index.md)选择唯一的主方向；不要因为名称相近就把历史 breadth pivot 归入另一顶层 Session。
3. 读该方向的 `index.md`、`conclusions.md` 和 `roadmap.md`。`conclusions.md` 优先于叙述性的历史 README。
4. 要引用具体结果时，沿 `sources.md` 回到受控上游材料；必要时同时看评价 YAML、source lock、receipt 和最终正文。
5. 只有在任务的明确授权覆盖该动作时，才遵循原目录的工作流运行脚本、修改文稿或扩展路线。

## 论文 Markdown 的阅读规则

每个逻辑包位于 `directions/<route>/papers/<route>--<package>/`：

- `index.md` 是来源卡：记录逻辑身份、选中的 TeX/PDF、辅助 Markdown、哈希及生成状态；
- `fulltext.md` 是从选中 TeX 派生的 Markdown 阅读副本；
- 原始 `source_path`、`.tex`、PDF、数据、锁定清单和评估仍具有优先级。

若卡片显示 `no-canonical-fulltext`，其意思是该逻辑包没有可确认的正式 TeX 正文；它不是“空白论文”，也不授权从项目笔记拼出一个新正文。

## 需要特别慢下来看的交叉边界

- `zeta_mvp0` 的原生 programme 与导入 `prime_dynamics_theory` RH 档案是两种不同身份；后者为 source-preserving reference corpus，不提升前者的 gate 或 claim。
- Logistic-origin 档案中的 Hénon/Symbolic/quantum graph 等 breadth pivot 是历史背景，不并入独立的 Session 2--5。
- Symplectic 的“Logistic → Hénon → Symplectic”是概念谱系，不自动传递定理、Route 状态或认证。
- Flow P24--P28 是 Flow 内部的五种连续时间形式；它们并非六条顶层线之外的一个新的统摄路线。

完整说明见[跨路线关系](02-cross-stream-relationships.md)。
