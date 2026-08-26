# C175 narrative report

Rule 184 supplies a genuinely different dynamical subtype: a synchronous, particle-conserving, irreversible cellular automaton with a density-dependent asymptotic geometry. The main progress is not another finite permutation classification. The paper solves the transient-to-periodic transition for every ring size and every particle number. Below half density, particles become isolated and translate right; above half density, holes become isolated and translate left. At half density only the two alternating states survive periodically.

The gap variables expose the mechanism. Zero gaps propagate backward and disappear when they meet an excess gap, giving a monotone defect count and a uniform finite attraction bound. Once the periodic core is identified, every iterate count reduces to a cyclic independent-set problem on `gcd(N,n)` sites. Möbius inversion then gives exact primitive geometric cycles and the full sector Artin--Mazur product.

The operator conclusion is deliberately split. Sectors with at most one minority symbol are rotations on the whole state space. Every sector with at least two minority symbols contains transients and is nonbijective, while its canonical periodic core remains a reversible finite rotation. That distinction is the reason for `A4_FORMAL_HINT`, not natural quantization of the entire all-sector system.

路线结论：本论文提供完整的动力学分类和可复验闭式，但周期轨道没有内生素数语义，也没有目标除子或全局解析比较。因此 A1 仅为 `A1_WEAK`，总体仍是 `ROUTE_A_REJECTED`。论文不声明外部新颖性、优先权或外部同行评审。
