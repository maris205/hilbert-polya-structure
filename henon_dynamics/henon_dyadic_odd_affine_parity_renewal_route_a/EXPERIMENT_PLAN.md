# Exact-validation plan / 精确验证计划

## Objective / 目标

Validate the all-odd-parameter theorem independently of the producer, stress its semantic evidence carrier, and separate formal proof from finite regression sentinels.

对全体奇参数定理进行独立验证，攻击证据载体的语义完整性，并明确区分符号证明与有限回归哨兵。

## Frozen matrix / 冻结矩阵

- Parameters: \(a,b\in\{-5,-3,-1,1,3,5\}\), 36 pairs.
- Fixed words: every word for \(1\le n\le8\), 18,360 cases.
- Finite-tail inverse parity prefixes: all 256 prefixes for every pair, 9,216 cases.
- Return fixed points: \(1\le k\le12\), 432 rows.
- Primitive-period ledger: \(1\le n\le16\).
- Roof recovery coefficients: \(1\le n\le32\).
- Arithmetic: exact only; no floating point, training split, or target data.

参数、词长、首返和屋顶截断均在运行前冻结；它们只用于回归，不能替代“对任意奇 \(a,b\)”的证明。

## Six release commands / 六条发布命令

1. Producer: builds the canonical evidence JSON.
2. Independent checker: reimplements all formulas without importing producer code.
3. SymPy cross-check: derives branch iterates, fixed points, derivatives, Möbius reconstruction, and formal-series identities.
4. Replay: rebuilds evidence in a temporary directory and requires byte identity.
5. Mutation: requires rejection of 25 repaired-hash semantic changes and one stale-hash change.
6. Manifest: requires exactly 27 payload files plus the self-excluded manifest.

## Paper verification / 论文验证

- Compile baseline, internal round 1, and internal round 2/final snapshots with LuaLaTeX.
- Rebuild the final PDF twice under frozen `SOURCE_DATE_EPOCH` and require identical SHA-256.
- Require embedded fonts, zero undefined references/citations, zero missing glyphs, and zero overfull boxes.
- Render every page to PNG and inspect page snapshots.

## Failure rule / 失败规则

Any producer/checker disagreement, non-rejected semantic mutation, non-deterministic final PDF, manifest count mismatch, or forbidden-claim leakage blocks release. Route-A rejection is not a validation failure; it is the required scientific verdict when A0 fails.

生产器与检查器不一致、语义变异未被拒绝、PDF 非确定、清单不闭合或禁区主张泄漏，任一项都阻断发布。Route-A 拒绝本身不是验证失败，而是 A0 失败时应有的科学结论。
