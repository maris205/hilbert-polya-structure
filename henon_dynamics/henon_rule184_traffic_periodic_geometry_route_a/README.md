# HCS-C175: cyclic Rule-184 traffic periodic geometry

This package proves, simultaneously for every ring size `N>=1` and every particle sector `0<=k<=N`, the complete periodic core of cyclic Rule 184, finite attraction by a gap Lyapunov argument, every-iterate fixed counts, primitive-cycle and Artin--Mazur products, and the exact whole-sector versus periodic-core Koopman boundary.

The explicit progress is a full all-parameter classification for an irreversible traffic cellular automaton. The conservative Route-A verdict is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`; Route B remains false. The package makes no external novelty or priority claim.

中文摘要：本包对任意环长与固定粒子数扇区证明 Rule 184 的完整周期核、有限时间吸引、全迭代不动点闭式、本原周期与动力 zeta 乘积，并精确区分含瞬态的全状态空间和可酉化的周期核。该结果是动力系统定理进展，不是算术或 Hilbert--Pólya 匹配。

Run:

```bash
python code/c175_rule184_producer.py
python code/c175_rule184_checker.py
python code/c175_sympy_crosscheck.py
python code/c175_replay.py
python code/c175_mutation.py
python code/c175_release_manifest.py
```

The manuscript is `paper/main.pdf`. The finite JSON ledger is a regression sentinel; the infinite quantifiers are discharged by `THEOREM_PACKAGE.md` and the manuscript proof.
