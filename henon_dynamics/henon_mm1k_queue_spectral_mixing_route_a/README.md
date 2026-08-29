# HCS-C225 — finite-capacity M/M/1/K spectral–mixing atlas

This package makes one theorem-scale advance for the Route-A dynamical-systems
program: a finite-capacity birth–death queue is treated as a complete reversible
semigroup rather than as a single stationary formula.  For states
`0,…,K` (with `K` including the customer in service), it records the exact
stationary law, symmetric Jacobi conjugation, every eigenmode and eigenvalue,
the spectral transient kernel, a quantitative TV/L2 mixing certificate, and
the four singular rate/capacity faces.  The `K→∞` atlas distinguishes the
positive-recurrent (`rho<1`), null-recurrent (`rho=1`) and mass-escape
(`rho>1`) regimes without asserting an unproved continuous-spectrum theorem.

The canonical evidence is
`results/c225_mm1k_evidence.json`.  `code/c225_mm1k_checker.py` is
producer-independent; `code/c225_mm1k_sympy_crosscheck.py` supplies exact
symbolic identities, `code/c225_mm1k_replay.py` performs clean-process byte
replay, and `code/c225_mm1k_mutation.py` rejects repaired-hash, nested-schema
and stale-hash attacks.  The release manifest seals exactly 27 payload files
and excludes itself.

## Reproduce

From this directory:

```bash
python -B code/c225_mm1k_producer.py
python -B code/c225_mm1k_checker.py
python -B code/c225_mm1k_sympy_crosscheck.py
python -B code/c225_mm1k_replay.py
python -B code/c225_mm1k_mutation.py
python -B code/c225_release_manifest.py
```

The source/evaluator lock is commit
`489672bd36abd3a4f6da92d1446a0af575917959` and
`flow_systems/skills/route-a-evaluator.md` SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`; all scope flags are false,
the Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and Route B is not invoked.

The finite queue is deliberately separated from C208's branching PGF and C220's
open-TASEP matrix-ansatz phase diagram.  No queue eigenvalue is identified with
a target zero, prime, Euler factor, or Hilbert–Pólya operator.
