# HCS-C134: faithful character torus

This package replaces C129's single mod-five phase by the labelled character
torus of the integer translation lattice.  In the scaled, strictly separated
family with radius `3k` and branch permutations of `(-2k,0,2k)`, the first
three normalized Fredholm log jets recover every branch-labelled integer
translation exactly.

## Reproduce

```bash
python3 code/c134_character_producer.py
python3 code/c134_character_checker.py
python3 code/c134_sympy_crosscheck.py
python3 code/c134_replay.py
python3 code/c134_mutation.py
```

The exact receipt is `results/c134_character_evidence.json`, the manuscript is
`paper/main.pdf`, and the Route-A evaluation is
`evaluations/route_a/HCS-C134/2026-08-24.yaml`.

Strict verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_EXPLORATORY
route_b_invocation_allowed: false
```

Recovery is limited to the frozen branch-labelled integer affine family.  It
is not a finite-precision stability theorem or arbitrary-geometry theorem.
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
