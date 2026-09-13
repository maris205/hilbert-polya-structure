# Logistic Dynamics：来源、阶段与证据入口

[P1 Wiki](../../index.md) · [方向总览](../index.md) · [首页](index.md) · [结论](conclusions.md) · [路线图](roadmap.md) · [本页](sources.md)

## 源绑定身份

| 项 | 值 |
|---|---|
| 源研究库 | `git@github.com:maris205/riemann_dyna.git` |
| 冻结源提交 | `68a7ca23ebfede30c1a19b22c8de6d7173d99740` |
| 镜像库 | `git@github.com:maris205/hilbert-polya-structure.git` |
| 同步记录 | `HPD-MIRROR-20260811-A2E021F`，时间 `2026-08-11T21:30:00Z` |
| 本地镜像入口 | [`logistic_dynamics/`](../../../logistic_dynamics/README.md) |

这些值来自 [sync_manifest.yaml](../../../logistic_dynamics/sync_manifest.yaml)。该清单是阶段到源路径、项目映射、状态、论文边界和源提交的权威索引；本页的中文摘要不覆盖它。

## 首选阅读材料

| 文档 | 用途 |
|---|---|
| [README](../../../logistic_dynamics/README.md) | 流的范围、31 个项目记录的处理规则、同步与全局 claim boundary。 |
| [STAGE_INDEX](../../../logistic_dynamics/STAGE_INDEX.md) | 每个同步阶段的组别、状态、Route-A 状态与论文状态。 |
| [LOG0001_STABLE_RESULTS](../../../logistic_dynamics/LOG0001_STABLE_RESULTS.md) | 精确 `U_c` 主线、同一对象的解析结果、Route-A/Riemann 目标元组与停放要求。 |
| [EXPLORATION_CLOSEOUT](../../../logistic_dynamics/EXPLORATION_CLOSEOUT.md) | 可复用线索、受范围限定的障碍、最小重新开启门与 Route-B 边界。 |
| [sync_manifest](../../../logistic_dynamics/sync_manifest.yaml) | 源锁、项目路径、`failure`、`next_task`、测试与产物的机器可读来源。 |

## 论文与主线阶段入口

镜像说明将 7 个阶段标为已有论文、19 个标为计划论文、2 个并入 `LOG-0001` 的前提阶段，另有 3 个档案/控制/诊断阶段不打开论文。论文状态不等同于 Riemann 目标的完成状态。

### `LOG-0001` 稳定解析链

| 阶段 | 镜像项目 | 清单状态 |
|---|---|---|
| Nuclear Fredholm | [LOG-0001-NUCLEAR-FREDHOLM](../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/README.md) | `ANALYTIC_REVIEW` / published |
| Growth order | [LOG-0001-GROWTH-ORDER](../../../logistic_dynamics/projects/exact_uc_polar_growth_order/README.md) | `ANALYTIC_REVIEW` / published |
| Conformal ratio | [LOG-0001-CONFORMAL-RATIO](../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio/README.md) | `ANALYTIC_REVIEW` / published |
| Lower growth | [LOG-0001-LOWER-GROWTH](../../../logistic_dynamics/projects/exact_uc_polar_lower_growth/README.md) | `ANALYTIC_REVIEW` / published |
| Order lower | [LOG-0001-ORDER-LOWER](../../../logistic_dynamics/projects/exact_uc_polar_order_lower/README.md) | `ANALYTIC_REVIEW` / planned |

其必要的物理与极坐标前提可从 [阶段索引](../../../logistic_dynamics/STAGE_INDEX.md) 中的 Logistic structure / Logistic polar 条目回溯；其中 partition 与 boundary trace 被标为 `HISTORICAL_PREREQUISITE`，已并入 `LOG-0001`，不应再当作独立全局行列式结论。

### 其他已发布记录（只作源内历史入口）

| 阶段 | 镜像项目 | 清单状态与范围 |
|---|---|---|
| TH-0001 real caustic | [TH-0001-PHASE-CAUSTIC-REAL](../../../logistic_dynamics/projects/th_0001_phase_caustic_real/README.md) | `GO_WITH_LIMITATIONS` / published；属于源档案的 Hénon breadth pivot，并不合并入顶层 Hénon Session。 |
| COPRIME countable trace | [COPRIME-0001-COUNTABLE-TRACE](../../../logistic_dynamics/projects/coprime_0001_countable_trace/README.md) | `ANALYTIC_REVIEW` / published；需与其算子边界一同阅读。 |
| COPRIME scalar boundary | [COPRIME-0001-SCALAR-BOUNDARY](../../../logistic_dynamics/projects/coprime_0001_scalar_boundary/README.md) | `STOP_SCOPED` / published；端点障碍是该冻结对象的关闭边界。 |

## 再现与来源限制

- 每个项目目录的 `SOURCE_PROVENANCE.yaml` 与 `results/SOURCE_HASHES.sha256`（如该阶段具备）给出复制文件身份；详见其 README 与清单。
- 源仓库中的再现命令、测试和证书才是相应结果的证据入口；[稳定结果页](../../../logistic_dynamics/LOG0001_STABLE_RESULTS.md) 列出 `LOG-0001` 的再现命令。
- 旧数值 notebook 保留为历史诊断，不能用于重新定义候选或提升有限零点匹配。
- `LEGACY-ANNULAR-RESIDUAL-001` 依赖未镜像的独立 `prime_dynamics_theory` RH-371 checkpoint；它被标为 `NOT_TESTABLE`，不能把该外部依赖当作本方向的已纳入证据。

需要完整项目清单、文件路径和当前状态时，优先使用 [同步清单](../../../logistic_dynamics/sync_manifest.yaml) 与 [阶段索引](../../../logistic_dynamics/STAGE_INDEX.md)，再返回 [首页](index.md) 或 [路线图](roadmap.md)。
