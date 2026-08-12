# Symbolic Dynamics Research Program

本目录是 Hilbert–Pólya 研究计划的 Symbolic Dynamics 路线入口。唯一主系统族是
**Symbolic Dynamics**；几何、Hamiltonian、quantum graph、scattering 或外部
operator-algebra 想法只记为 `ROUND2_CLUE`，不在当前路线展开。

## 当前项目

[**Ra-1-arithmetic-symbolic-dynamics**](Ra-1-arithmetic-symbolic-dynamics/README.md)

命名规则为 `R<route>-<roadmap-phase>-<project-name>`：`Ra-1` 表示当前的
Route-A roadmap 阶段，`arithmetic-symbolic-dynamics` 是本项目的实际名称，不再
使用 `project` 作为字面目录名。

## 论文与简明结论

| 论文项目 | 可共享论文 | 简明结果 | 状态 |
|---|---|---|---|
| [01-falsification-first-audit](Ra-1-arithmetic-symbolic-dynamics/papers/01-falsification-first-audit/README.md) | [PDF](Ra-1-arithmetic-symbolic-dynamics/papers/01-falsification-first-audit/main.pdf) · [LaTeX/实验/材料](Ra-1-arithmetic-symbolic-dynamics/papers/01-falsification-first-audit/) | 独立审计六个 symbolic 候选；没有一个同一对象通过 A0–A4，六项 Route B 均关闭。有限状态、有限记忆、有限维 cocycle determinant 的 divisor 计数为 $O(R)$，与完成 Riemann 函数的 $R\log R$ 量级不相容。 | **COMPLETE / FROZEN** |
| [02-wheel-sieve-stationarization-obstructions](Ra-1-arithmetic-symbolic-dynamics/papers/02-wheel-sieve-stationarization-obstructions/README.md) | [PDF](Ra-1-arithmetic-symbolic-dynamics/papers/02-wheel-sieve-stationarization-obstructions/main.pdf) · [LaTeX/证明/材料](Ra-1-arithmetic-symbolic-dynamics/papers/02-wheel-sieve-stationarization-obstructions/) | 证明 strict extension 不能产生周期点；forward-well-founded strong-bisimulation quotient 仍无环；保留 state-class exact-$q$ 标签的 quotient 继承严格分层；finite-alphabet fixed-window decoder 不能恢复无界精确 prime clock。 | **THEOREM SCREENING COMPLETE** |

### 论文 1 的候选分离结论

- `SD-C05` 是最强 endogenous rational-prime generator，但其 level shift 无周期轨道。
- `SD-C04` 有最自然的 Fredholm determinant，但 primitive species 是 modular/
  quadratic-irrational orbit，不是 rational primes。
- `SD-C06` 有最强的精确 zeta-quotient 碰撞，但没有同一对象的 primitive-orbit
  Fredholm ledger；Liouville sign 仍是额外 arithmetic observable。
- 三者的优点不能 coordinatewise 拼接成一个候选。

### 论文 2 之后的下一步

在当前 wheel-sieve 分支中，仍开放的同族方向是一个真正的无限 factor 或
observational recoding。运行任何新实验前，必须先完成
[source lock](Ra-1-arithmetic-symbolic-dynamics/papers/02-wheel-sieve-stationarization-obstructions/OBSERVATIONAL_RECODING_SOURCE_LOCK.md)：
冻结 infinite phase space、level-blind map、alphabet/memory class、exact arithmetic/
clock decoder、path-lifting compatibility 和 cutoff consistency。完成前维持
`NOT_TESTABLE`，不分配 `SD-C07`，不定义 determinant，Route B 继续锁定。

## 根目录保留内容

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [完整项目包](Ra-1-arithmetic-symbolic-dynamics/)

项目完整性由
[`PROJECT_MANIFEST.sha256`](Ra-1-arithmetic-symbolic-dynamics/PROJECT_MANIFEST.sha256)
管理；两个论文项目各有独立 `PAPER_MANIFEST.sha256`。本地 PDF/legacy 输入语料和
运行缓存不进入 manifests。
