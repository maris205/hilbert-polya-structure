# C176 results / 结果

Status: all theorem-led symbolic and exhaustive regression gates pass.

- Every finite connected undirected loopless sink multigraph: recurrent stable configurations form the critical-group torsor (`PROVED`).
- Every nonnegative `b`: Smith and adjugate formulas give the same exact order `L` (`PROVED`).
- Recurrent dynamics: all orbits have length `L`, with `D/L` cycles and fixed count `D` iff `L|n` (`PROVED`).
- Zeta, determinant and characters: exact factors and every `L`-th root with multiplicity `D/L` (`PROVED`).
- Symmetry: group inversion is a reversor; the finite Koopman unitary is self-adjoint iff `L<=2` (`PROVED`).
- Boundary: full stable-state addition may be noninjective; no full-space permutation claim is made (`PROVED` by path counterexample).
- Finite sentinels: 30 graph types, 137 sinks, 780 translations, 8,704 fixed rows, 32,938 stable transitions, 13,764 recurrent transitions, and 212,504 fixed-state comparisons. Of the tested labelled sources, 610 full stable maps are noninjective.
- Independent checker: 135,049 assertions. SymPy: 5,248 checks. Mutation suite: 17/17 rejected.
- Citation and reference registries: 0 entries.

Route-A v0.2: `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, Route B false.

中文结论：正定理严格属于复现稳定构型；所有稳定构型不能自动视为临界群或酉置换。闭式谱与 zeta 没有赋予该模型素数语义。
