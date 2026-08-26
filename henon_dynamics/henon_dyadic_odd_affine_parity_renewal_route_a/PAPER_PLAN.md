# Paper plan / 论文计划

## Proposed title / 拟定标题

**Exact Renewal and Clock Recovery for Odd-Affine Parity Maps on the 2-Adic Integers**

## Story / 叙事主线

The paper begins from the classical parity conjugacy, explicitly assigns it to prior work, and asks a narrower source-side question: what does first-return acceleration preserve? The main theorem derives the geometric renewal law, isolates the countable exceptional set, restores the original clock through the roof, and then proves that both unweighted and stability-weighted invariants erase every odd parameter. This exact success therefore becomes a Route-A obstruction rather than a target claim.

论文从经典 parity 共轭出发但不主张其新颖性；核心问题是首返加速保留了什么。正文依次给出几何 renewal、异常集、原时钟恢复与参数盲性，最终把“精确可解”转化为 Route-A 反例性结论。

## Section structure / 章节结构

1. Introduction and ownership boundary.
2. Frozen family and classical parity foundation.
3. Fixed-word and reciprocal-stability theorems.
4. First-return renewal and exceptional set.
5. Original-clock roof recovery.
6. Koopman boundary, 3x+1 boundary, and Route-A verdict.
7. Reproducibility and limitations.

## Claims–evidence matrix / 主张—证据矩阵

| Claim | Proof | Machine evidence |
|---|---|---|
| one fixed point per binary word | iterate formula + unit denominator | producer/checker word ledger; SymPy |
| stability sum equals one | exact derivative and \(v_2\) identity | independent checker |
| geometric first-return law | Haar valuation layers | 432 exact return rows |
| roof recovery restores \((1-2z)^{-1}\) | renewal determinant + zero orbit | 32 exact series coefficients; SymPy |
| parameter blindness | all-parameter formulas | 36-pair hostile control grid |
| operator is only a formal hint | Wold decomposition | proof audit; no finite spectral fit |

## Visual decision / 图表决策

No figure is materially useful: every dependency is a short exact equation. One compact Route-A table is retained because it compares five distinct gates and their blocking reasons. This is an equation-first paper, not a data-visualization paper.

无需生成图：关键关系均由短公式直接表达。仅保留一张 Route-A 五层结论表，因为它能清晰对应五个关卡与失败原因。

## Citation scaffold / 引用框架

- Bernstein–Lagarias (1996): ownership of parity conjugacy and odd \(ax+b\) extension.
- Leventides–Poulios (2020): adjacent positive-integer Koopman literature and priority boundary.

No citation is used as a substitute for a proof in this paper.

## Improvement rounds / 改进轮次

- Round 1: attack clock ambiguity, exceptional-set completeness, and classical-prior ownership.
- Round 2: attack operator overclaim, 3x+1 leakage, Route-A consistency, and release reproducibility.

Both rounds are internal adversarial improvement passes. No external reviewer, score, or acceptance probability is simulated.
