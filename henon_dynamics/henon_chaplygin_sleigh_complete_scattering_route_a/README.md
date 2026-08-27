# HCS-C199 — complete Chaplygin-sleigh scattering atlas

C199 gives a complete signed-offset, all-parameter theorem for the classical
Chaplygin sleigh: explicit reduced flow, heteroclinic scattering, physical
reconstruction and two asymptotic lines, stability, Poisson form, invariant
measure, reversibility and the recurrent zero-offset boundary.

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

Route B is false under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python code/c199_chaplygin_producer.py
python code/c199_chaplygin_checker.py
python code/c199_chaplygin_sympy_crosscheck.py
python code/c199_chaplygin_replay.py
python code/c199_chaplygin_mutation.py
python code/c199_release_manifest.py
```

The final independent paper is `paper/main.pdf`; three content-distinct rounds
preserve both substantive revisions.
