# HCS-C129: graph-directed phase holonomy

This package adds a frozen fifth-root translation-lattice character to the
C124 graph-directed affine Hénon Hardy owner. It proves an all-period twisted
trace/Fredholm/primitive identity and an exact control: the twist distinguishes
two branch assignments whose untwisted determinant is identical.

## Reproduce

```bash
python3 code/c129_phase_producer.py
python3 code/c129_phase_checker.py
python3 code/c129_sympy_crosscheck.py
python3 code/c129_replay.py
python3 code/c129_mutation.py
```

The manuscript is `paper/main.pdf`; exact claims are bound to
`results/c129_phase_evidence.json`; the content ledger is
`C129_RELEASE_MANIFEST.json`.
The package-local Route-A evaluation is retained at
`evaluations/route_a/HCS-C129/2026-08-24.yaml` under the evaluator's v0.1.0
accumulation contract.

Strict verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_EXPLORATORY
route_b_invocation_allowed: false
```

The character supplies finite-quotient position sensitivity, not complete
geometry recovery or a target-divisor match. Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
