# Narrative report / 叙事报告

## Outcome first / 结论先行

C174 obtains a complete theorem package but rejects the candidate as a primary Route-A model. The exact positive result is the renewal decomposition and original-clock recovery. The exact negative result is stronger for evaluation: every unweighted periodic count and every reciprocal 2-adic derivative stability sum is independent of both odd parameters.

C174 得到完整定理包，但拒绝该候选作为 Route-A 主模型。正面进展是首返 renewal 与原时钟恢复；对路线评估更关键的负面进展是：所有无权周期计数与二进稳定性总和都与奇参数 \(a,b\) 无关。

## Why acceleration is subtle / 为什么加速并不平凡

On the odd coset, the return time is \(v_2(ax+b)\), with a geometric conditional Haar law. Encoding only the accelerated return map produces a countable-alphabet full shift with infinitely many time-one fixed points, so its ordinary Artin–Mazur zeta does not exist. The lost clock is not cosmetic: symbol \(k\) represents exactly \(k\) applications of the original map.

奇数截面上的返回时间服从精确几何分布。若只看加速映射，就得到可数字母满移位，时间一已有无限多个不动点，因此普通 Artin–Mazur zeta 不存在。符号 \(k\) 实际代表原映射的 \(k\) 个时钟步，不能丢失。

## Main reconstruction / 主要重构

The roof series is \(F(z)=\sum_{k\ge1}z^k=z/(1-z)\). Its renewal zeta is \((1-z)/(1-2z)\), counting exactly the original periodic points whose parity words contain a one. The missing all-zero orbit contributes \((1-z)^{-1}\), recovering the original \((1-2z)^{-1}\). The recovery is exact at every coefficient, not an asymptotic fit.

屋顶级数与零轨道因子逐系数恢复原系统 zeta；这是严格恒等式，而不是渐近拟合。

## Why Route A still fails / 为什么 Route A 仍失败

- A0: dyadic local arithmetic is intrinsic, but no rational-prime or prime-power correspondence emerges.
- A1: the primitive orbit ledger is exact, yet it is only weak because it carries no arithmetic labels.
- A2: all exact source zetas are elementary and parameter-blind.
- A3: rational continuation supplies no target functional equation or Weil compression.
- A4: the Koopman lift is a proper non-Schatten isometry; unitarization changes phase space.

Thus the tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, and A0 forces overall rejection.

## Boundary discipline / 边界纪律

The \((3,1)\) specialization lives on all of \(\mathbb Z_2\), not only on positive integers. The legal cycle \(1/5\to4/5\to2/5\to1/5\) demonstrates the difference. No claim about positive-integer Collatz trajectories follows. Likewise, the classical parity conjugacy is cited as prior work and not counted as the package's novelty.

\((3,1)\) 的二进系统远大于正整数 Collatz 系统；非整数三周期明确展示这一边界。本包不推出任何正整数 Collatz 结论，也不把经典共轭算作新颖贡献。

## Reproducibility / 可复现性

The producer, independent checker, symbolic cross-check, byte replay, mutation test, and release manifest form six separate release commands. The exact evidence contains no floating-point field. The paper is compiled in three content snapshots; the final snapshot is rebuilt twice deterministically and checked for fonts, warnings, and visual layout.

六条发布命令分别覆盖生成、独立验证、符号交叉验证、逐字节回放、语义变异与清单闭合；论文保留三版内容快照并对最终版做双次确定性编译。
