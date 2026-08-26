# Source and ownership audit / 来源与归属审计

## Frozen source / 冻结来源

- Repository source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`.
- Route-A evaluator: `flow_systems/skills/route-a-evaluator.md`, version 0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
- No target data or fitted parameter is used.

源提交、评估器路径与哈希、范围字面量都已冻结；没有使用目标零点、除子、素数表或拟合参数。

## Verified prior-work boundary / 已核验的先验归属

1. D. J. Bernstein and J. C. Lagarias, “The 3x+1 Conjugacy Map,” *Canadian Journal of Mathematics* 48 (1996), 1154–1169, DOI [10.4153/CJM-1996-060-x](https://doi.org/10.4153/CJM-1996-060-x). The paper studies the 2-adic parity conjugacy and explicitly includes odd \(ax+b\) generalizations. C174 therefore does **not** claim novelty for the parity map, its homeomorphism property, or the inverse parity series.
2. J. Leventides and C. Poulios, “Koopman operators and the 3x+1-dynamical system,” [arXiv:2010.12987](https://arxiv.org/abs/2010.12987), 2020. This studies Koopman/operator questions for the discrete positive-integer 3x+1 system and sequence spaces. It is cited to prevent an overbroad “first Koopman treatment” claim. C174's phase space and Haar \(L^2(\mathbb Z_2)\) theorem are stated narrowly, without a global priority claim.

Bernstein–Lagarias 的 parity 共轭及其奇 \(ax+b\) 扩张明确归属于经典工作；Leventides–Poulios 的正整数 Collatz Koopman 研究用于限制算子新颖性措辞。C174 不声称“首次研究 Collatz Koopman”，也不把经典共轭包装成新结果。

## Repository collision audit / 仓库碰撞审计

The nearest local packages concern finite dyadic Pascal maps, dyadic solenoids, a uniform affine horseshoe, finite-field multipliers, and non-dyadic Route-A obstructions. None freezes the full odd \((a,b)\) family on \(\mathbb Z_2\) and proves the combined first-return renewal, original-clock roof recovery, and reciprocal-stability parameter-blindness package. The binary-shift fixed-count formula alone is not treated as a new contribution.

仓库中邻近工作覆盖有限二进 Pascal 映射、二进 solenoid、均匀仿射马蹄与有限域乘子，但未覆盖本包的完整“首返 renewal + 原时钟恢复 + 稳定性参数盲性”组合。单独的二元移位不动点计数不作为新颖贡献。

## Evidence and novelty boundary / 证据与新颖性边界

The release establishes internal mathematical correctness and deterministic artifact closure. It does not perform a comprehensive literature review and therefore makes no universal priority claim for the renewal identity. “Main progress” means progress relative to this repository's frozen candidate evaluation, not a claim of first discovery in the literature.

发布包证明内部数学正确性和确定性工件闭合，但没有进行穷尽性文献综述，因此不声称 renewal 恒等式在全球文献中的首创性。“主进展”仅指相对本仓库冻结候选的明确推进。

## Citation integrity / 引用完整性

Both registered citations were checked against primary records (DOI landing record and arXiv record). Citation contexts are limited to ownership and scope. No numerical or theorem claim in C174 depends on an unverified secondary source.

两条登记引用均按 DOI/arXiv 主记录核验；引用只承担归属与范围功能。C174 的数值和定理结论均不依赖未经核验的二手来源。
