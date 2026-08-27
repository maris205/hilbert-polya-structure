# P27 Round-2 reproducibility receipt

Date: **2026-08-27**

Command:

```bash
bash experiments/reproduce.sh
```

Result:

```text
canonical generation: PASS
canonical manifest verification: PASS
unit tests: 5/5 PASS
second generation: PASS
second manifest verification: PASS
two-run byte identity: 4/4 PASS
```

Canonical SHA-256:

```text
congruence_reduction_order_ledger.csv  811c53a24e34def2b7fbb9353ccd568dd638a9c57706443626091bc4c23e09de
round2_metrics.json                    623b5f05ff63acfa76d3a4d8cb75d86adb4fc6911409083953c28d0938355277
experiment_receipt.json                7b94522eab84d69dbe95b439cd32955040e14c80424343a86b9d595d4eb7fafc
manifest.json                          ef57dd62868b9185b319af124df958a2a21f51e6d34d1380a5acacb8dea9bff1
```

Determinism scope: exact integer matrix arithmetic, fixed-order iteration,
sorted JSON keys, fixed CSV column order, and deterministic binary64 geodesic
length formatting.  The receipt does not certify external novelty, full
`Gamma(3)` conjugacy-class primitivity, or any periodic orbit of the
inverse-limit flow.
