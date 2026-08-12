# Symbolic Dynamics Research Program

本目录是 Hilbert–Pólya 研究计划的 Symbolic Dynamics 路线入口。唯一主系统族是
**Symbolic Dynamics**；几何、Hamiltonian、quantum graph、scattering 或外部
operator-algebra 想法只记为 `ROUND2_CLUE`，不在当前路线展开。

当前研究项目为 **Ra-1: Arithmetic Symbolic Dynamics**。`Ra-1` 表示
Route-A roadmap 的当前阶段；项目名称只在本 README 中维护，不再增加项目包装目录。
全部可共享论文直接位于根目录的 [`papers/`](papers/) 中。

## 论文与简明结论

| 论文项目 | 可共享论文 | 简明结果 | 状态 |
|---|---|---|---|
| [01-falsification-first-audit](papers/01-falsification-first-audit/README.md) | [PDF](papers/01-falsification-first-audit/main.pdf) · [LaTeX/实验/材料](papers/01-falsification-first-audit/) | 独立审计六个 symbolic 候选；没有一个同一对象通过 A0–A4，六项 Route B 均关闭。有限状态、有限记忆、有限维 cocycle determinant 的 divisor 计数为 $O(R)$，与完成 Riemann 函数的 $R\log R$ 量级不相容。 | **COMPLETE / FROZEN** |
| [02-wheel-sieve-stationarization-obstructions](papers/02-wheel-sieve-stationarization-obstructions/README.md) | [PDF](papers/02-wheel-sieve-stationarization-obstructions/main.pdf) · [LaTeX/证明/材料](papers/02-wheel-sieve-stationarization-obstructions/) | 证明 strict extension 不能产生周期点；forward-well-founded strong-bisimulation quotient 仍无环；保留 state-class exact-$q$ 标签的 quotient 继承严格分层；finite-alphabet fixed-window decoder 不能恢复无界精确 prime clock。 | **THEOREM SCREENING COMPLETE** |
| [03-wheel-sieve-periodic-clock-obstruction](papers/03-wheel-sieve-periodic-clock-obstruction/README.md) | [PDF](papers/03-wheel-sieve-periodic-clock-obstruction/main.pdf) · [LaTeX/证明/审稿](papers/03-wheel-sieve-periodic-clock-obstruction/) | 精确 autonomous clock decoder 强制 factor 纤维保持同一 level，因此 direct image 继承严格分层且无周期点；连续 closure decoder 在 lag-pair 与对角线分离时同样排除边界周期点。clock erasure 或 compactification 虽能制造周期点，却不能继承普通拓扑下的精确 $q/\log q$ clock。 | **COMPLETE / THEOREM STOP** |

### 论文 1 的候选分离结论

- `SD-C05` 是最强 endogenous rational-prime generator，但其 level shift 无周期轨道。
- `SD-C04` 有最自然的 Fredholm determinant，但 primitive species 是 modular/
  quadratic-irrational orbit，不是 rational primes。
- `SD-C06` 有最强的精确 zeta-quotient 碰撞，但没有同一对象的 primitive-orbit
  Fredholm ledger；Liouville sign 仍是额外 arithmetic observable。
- 三者的优点不能 coordinatewise 拼接成一个候选。

### 论文 3 的 theorem stop 与下一步

对“周期 target 逐点、单值、自治地继承 levelwise wheel prime clock”这一分支，
Paper 03 给出 `THEOREM_STOP`；继续增大 cutoff 或搜索 quotient cycle 已无意义。
仍开放的同族方向只能是一个**不同的、target-intrinsic arithmetic invariant**，
而不是对原 exact clock 的保真 factor。它必须重新 source-lock：冻结 phase space、
transition rule、arithmetic decoder、clock、primitive/repetition ledger 和 function
space，并从 A0 重新审计；不自动继承 `SD-C05` 的 arithmetic credit。当前仍不分配
`SD-C07`，不定义 determinant，Route B 继续锁定。

## 目录

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [三篇论文](papers/)

根目录不再设置项目包装层；每个论文项目各自使用 `PAPER_MANIFEST.sha256` 管理
完整性。本地 PDF/legacy 输入语料和运行缓存不进入 manifests。
