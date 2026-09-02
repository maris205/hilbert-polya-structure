# Exact control results — P160 RCS Round 2

**Status:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

## Author verifier — double fresh replay

Both 2026-09-02 UTC fresh runs matched `verification_output.txt` byte for byte.

```text
RCS VERIFY parameters=((1, 1), (2, 1), (1, 3), (2, 2), (3, 2))
EXHAUSTIVE source_weight<=32 target_weight<=9 times=0..5
ASSERTIONS 3462895
STATUS PASS
```

- Assertions: **3,462,895**.
- Transcript SHA-256:
  `3e1b83ff586795fc80fc01882d545fff270f9106471145b39c0f0ca51bd3a778`.
- Standard-library only; exact integer arithmetic; no network, randomness,
  floating point, or third-party dependency.

## Independent Review-A verifier — double fresh replay

Both runs matched
`docs/papers157_161_sequence/reviews/p160_rcs_a/CANONICAL.txt` byte for byte.

```text
P160 RCS HOSTILE REVIEW A: PASS
assertions=7332616
source_weight_max=30
target_weight_max=10
parameter_pairs=16
times=0..5
author_code_imported=no
```

- Assertions: **7,332,616**.
- Canonical SHA-256:
  `971bcfccf205a590d08246f7266b73f38d088bfc79c571e92b209a936359ef9f`.
- The reviewer control imports no author code and includes asymmetric and
  zero-boundary windows.

## Independent Review-B verifier — accepted and replayed

Review B returned `ACCEPT — 0 Critical / 0 Major / 0 Minor`. Its independent
standard-library verifier was rerun after the lifecycle-only source change and
matched `VERIFIER_RUN_1.txt` byte for byte:

```text
assertions=11287366
result=PASS
```

- Output SHA-256:
  `b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a`.
- Verifier SHA-256:
  `589a737b8371e46aba51caabbb431fb00b4ab9531fc4bd48805eb2cc62adeea9`.
- It imports neither author code nor Review-A code.

## Audited interfaces

The three controls jointly pressure literal iteration, coordinate formula,
point clocks, cap heights, empty and nonempty fibres, exact support, mass
conservation, conjugation, and ordered recovery. The mathematical M1 repair is
symbolic: for excess `d`, `gamma=(d)` is a one-part admissible witness. No
verifier is proof, source ownership evidence, or external clearance.
