# Symbolic Dynamics Research Program

本目录是 Hilbert–Pólya 研究计划的 Symbolic Dynamics 路线入口。唯一主系统族是
**Symbolic Dynamics**；几何、Hamiltonian、quantum graph、scattering 或外部
operator-algebra 想法只记为 `ROUND2_CLUE`，不在当前路线展开。

## 当前子项目

[**Ra-1-project — Hilbert–Pólya Symbolic Dynamics**](Ra-1-project/README.md)

命名规则为 `R<route>-<roadmap-phase>-<project>`：`Ra-1` 表示当前的 Route A
roadmap 阶段，末段 `project` 表示子项目名称与容器。论文、证明、实验、数值结果、
评估与 manifests 全部位于该目录。

## 阶段论文与简明结论

| 阶段 | 可共享论文 | 简明结果 | 状态 |
|---|---|---|---|
| Stage 01 — Scope Screening | [PDF](Ra-1-project/stages/stage_01_scope_screening/paper/main.pdf) · [LaTeX/材料](Ra-1-project/stages/stage_01_scope_screening/paper/) | 独立审计六个 symbolic 候选；没有一个同一对象通过 A0–A4，六项 Route B 均关闭。有限状态、有限记忆、有限维 cocycle determinant 的 divisor 计数为 $O(R)$，与完成 Riemann 函数的 $R\log R$ 量级不相容。 | **COMPLETE / FROZEN** |
| Stage 02 — Wheel-Sieve Stationarization | [PDF](Ra-1-project/stages/stage_02_stationary_wheel_extension/paper/main.pdf) · [LaTeX/材料](Ra-1-project/stages/stage_02_stationary_wheel_extension/paper/) | 证明 strict extension 不能产生周期点、有限 DAG 的 strong-bisimulation quotient 仍无环、保留 state-class exact-$q$ 标签的 quotient 仍继承严格分层，且 finite-alphabet fixed-window decoder 不能恢复无界精确 prime clock。 | **THEOREM SCREENING COMPLETE** |

### Stage 01 的候选分离结论

- `SD-C05` 是最强 endogenous rational-prime generator，但其 level shift 无周期轨道。
- `SD-C04` 有最自然的 Fredholm determinant，但 primitive species 是 modular/
  quadratic-irrational orbit，不是 rational primes。
- `SD-C06` 有最强的精确 zeta-quotient 碰撞，但没有同一对象的 primitive-orbit
  Fredholm ledger；Liouville sign 仍是额外 arithmetic observable。
- 三者的优点不能 coordinatewise 拼接成一个候选。

### Stage 02 的下一步

在当前 wheel-sieve 分支中，仍开放的同族方向是一个真正的无限 factor 或
observational recoding。运行任何新实验前，必须先完成
[source lock](Ra-1-project/stages/stage_02_stationary_wheel_extension/OBSERVATIONAL_RECODING_SOURCE_LOCK.md)：
冻结 infinite phase space、level-blind map、alphabet/memory class、exact arithmetic/
clock decoder、path-lifting compatibility 和 cutoff consistency。完成前维持
`NOT_TESTABLE`，不分配 `SD-C07`，不定义 determinant，Route B 继续锁定。

## 根目录保留内容

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [Ra-1-project 完整研究包](Ra-1-project/)

子项目完整性由
[`PROJECT_MANIFEST.sha256`](Ra-1-project/PROJECT_MANIFEST.sha256) 管理；每个阶段另有
独立 `STAGE_MANIFEST.sha256`。本地 PDF/legacy 输入语料和运行缓存不进入 manifests。
