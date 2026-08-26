# Frozen control receipt

Run date: 2026-08-25 UTC

Environment:

```text
Python 3.12.3
Linux x86_64
```

Command:

```sh
python3 code/verify_complete_bipartite.py
```

Receipt:

```text
globally extendible finite-shape counts (six shapes, two parameter pairs): PASS
global-phase versus local-admissibility counterexamples: PASS (13/25 and 12/25)
radius-one dimer bijection K_(2,6) <-> K_(3,4): PASS (288 torus points)
finite-index fixed-point formula: PASS
weighted 2x2 partition identity: PASS (sum=26450)
remote-phase independence equation p=p^2: PASS
ALL CHECKS PASS
```

- script SHA-256: updated after the two-round improvement loop in `SHA256SUMS`
- finite-shape checks: the empty set and five nonempty shapes at `(m,n)=(2,2)` and `(2,3)`, interpreted as restrictions of global configurations
- semantic counterexamples: for `(m,n)=(2,3)`, two remote even sites have 13 globally extendible restrictions versus 25 locally admissible patterns, while a remote even--odd pair has 12 versus 25
- dimer check: all 288 points of the `2 x 2` torus for `(2,6)`; injective images and exact inverse under `(3,4)`
- weighted count: independent integer weights on both target parts

The control is finite regression evidence only. The manuscript proves the translation-equivariant infinite-lattice code, inverse, entropy, subgroup dichotomy, pressure, and periodic formula without a finite cutoff.
