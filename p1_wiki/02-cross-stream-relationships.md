# 六条路线之间的关系：概念谱系不等于证明依赖

[P1 Wiki 首页](README.md) · [方向总览](directions/index.md) · [claim 词汇](01-status-and-claim-vocabulary.md)

## 总览图

```text
早期自由探索
  zeta_mvp0 ── 原生 programme（与导入 RH 档案严格隔离）

路线图驱动的五个 Session
  Logistic (S1) ──概念谱系──> Hénon (S2) ──概念谱系──> Symplectic (S3)
       │
       └── 历史 breadth pivots（不等于顶层 Session 归属）

  Symbolic (S4) ──共享“符号 / 周期轨道 / 行列式”问题域── Flow (S5)
       │                                                    │
       └──── 不是 theorem/Route credit transfer ────────────┘
```

箭头只表示来源明确写出的研究动机、概念问题或历史序列。它们**不**表示一个方向的结论、证明、源锁、Route 状态、A0--A4 credit 或授权自动进入另一个方向。

## 关系表

| 两端 | 可安全说的关系 | 不可安全推出的关系 | 首选入口 |
|---|---|---|---|
| zeta_mvp0 原生 programme ↔ 导入 RH 语料 | 同置于早期自由探索目录，但被明确隔离；导入件保持 source-preserving 身份 | 导入件是原生 programme 的新结果，或提升其 `P0` / Z / RH 状态 | [zeta 方向页](directions/zeta_mvp0/index.md) |
| Logistic ↔ Hénon | 可比较的动力学探索历史；Logistic 档案含 Hénon breadth pivot | Logistic 的历史 pivot 等于 Hénon 顶层 Session 的正式证据 | [Logistic](directions/logistic_dynamics/index.md) / [Hénon](directions/henon_dynamics/index.md) |
| Hénon ↔ Symplectic | Symplectic 源材料叙述了 Logistic → Hénon → symplectic/Hamiltonian chaos 的概念谱系 | Hénon 结果为 Symplectic 的定理前提，或二者共享 Route verdict | [Symplectic 路线图](directions/symplectic_map/roadmap.md) |
| Symbolic ↔ Flow | 都处理符号编码、周期轨道、动力学 zeta / trace 的相关难题 | Symbolic 的有限自治系统完成了 Flow 的经典--量子义务，反之亦然 | [Symbolic](directions/symbolic_dynamics/index.md) / [Flow](directions/flow_systems/index.md) |
| Flow P24--P28 ↔ Flow Session | 五种连续时间机制由同一冻结计划组织，属于 Session 5 的内部专题 | 五篇 final package 交付完成就是 Route A/B 或 RH 成功 | [P24--P28 专题](collections/flow-p24-p28-five-planned-forms.md) |

## 为什么需要这种分隔

不同路线可能复用同一组高层词语：周期轨道、zeta、Fredholm determinant、量子化、Weil 型结构、算术来源或 trace formula。相同词语不保证对象、归一化、roof、所有权关系、源锁、解析域或审计标准相同。

尤其要防止三类错误迁移：

1. **对象迁移**：把 unit-roof symbolic object 的结论套到 physical-roof flow，或把 finite-level data 套到 inverse-limit flow。
2. **证据迁移**：把一个局部 finite calculation、control 或 proxy 解释为另外一个候选的全局 Owner / A2 / Route B 证据。
3. **流程迁移**：把某个 batch 的 format/build/acceptance 状态理解为数学的 Gate closure，或理解为其他 Session 的授权。

处理跨方向问题时，先打开两端的 `sources.md` 和 `conclusions.md`，确认对象和状态是否真可比；若原始材料没有建立正式依赖，就在笔记中标为“概念关联”，而非“使用了 / 证明了 / 传递了”。
