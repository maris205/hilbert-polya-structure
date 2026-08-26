# HCS-C176: recurrent Abelian-sandpile translation spectrum

This package proves, for every finite connected undirected loopless multigraph with a designated sink and every nonnegative addition vector, that addition--stabilization on recurrent stable configurations is a critical-group translation. It derives two exact order formulas, every orbit and fixed count, the Artin--Mazur zeta, finite Koopman determinant and character spectrum, group-inversion reversal, and the self-adjoint boundary.

The explicit progress is an all-graph bridge from physical toppling dynamics to a finite abelian translation theorem, with a strict separation from all stable configurations. The conservative Route-A verdict is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`; Route B remains false. No external novelty or priority claim is made.

中文摘要：本包对任意有限连通无向无环多重图、指定汇点和非负加砂向量，证明复现稳定构型上的加砂--稳定化等同于临界群平移，并完整导出阶、轨道、谱、动力 zeta、Koopman 行列式和反演对称性。所有稳定构型上的映射可能非单射，绝不与复现子空间混同。

Run:

```bash
python code/c176_sandpile_producer.py
python code/c176_sandpile_checker.py
python code/c176_sympy_crosscheck.py
python code/c176_replay.py
python code/c176_mutation.py
python code/c176_release_manifest.py
```

The manuscript is `paper/main.pdf`. The finite simple-graph JSON ledger is a regression sentinel; the multigraph quantifiers are discharged by `THEOREM_PACKAGE.md` and the manuscript proof.
