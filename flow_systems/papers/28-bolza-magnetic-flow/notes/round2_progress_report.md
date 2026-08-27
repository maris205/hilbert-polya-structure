# P28 Round-2 progress report

Date: **2026-08-27**

## Result

Round 2 proves the tensor-family owner-separation lemma and materializes a
target-free `b=0,+1/2,-1/2` ownership ledger for common tensor powers
`N=1,2,4,8`.

```text
OWNER_LEDGER_ROWS=12
FIELD_VALUES=3
TENSOR_POWERS=4
UNIT_TESTS=7/7_PASS
DETERMINISTIC_REPLAY=PASS
OWNER_ROWS_PROVED=12/12
TRACE_BINDING_ROWS_OPEN=12/12
ORBIT_OWNERSHIP_NOT_ESTABLISHED=12/12
FIXED_OPERATOR_TRANSFER_ALLOWED=0/12
```

The exact positive/negative-field comparison is antiunitary conjugation at the
same `N`; the exact classical comparison is velocity reversal. The ledger
therefore records sign pairing as a control, not as an arithmetic signal.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
A0_SCREEN=ARITHMETIC_SUBSTRATE_PRESENT_PRIME_LINK_UNPROVED
A1_SCREEN=PRIMITIVE_MAGNETIC_LEDGER_NOT_EXECUTED
A4_ARCHITECTURE_NOTE=OWNER_SEPARATION_PROVED_NO_CREDIT
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

This is real theorem and reproducibility progress, but it is not a primitive
orbit experiment. No formal Route-A tuple is assigned because the trace
regime, energy window, primitive orbit ledger, arithmetic controls, and
non-arithmetic metric control remain incomplete.

## Artifacts

- `notes/round2_tensor_family_owner_lemma.md`
- `code/build_owner_ledger.py`
- `code/test_owner_ledger.py`
- `results/bolza_tensor_family_owner_ledger.csv`
- `results/round2_owner_ledger_validation.json`
- `experiments/round2_execution_receipt.md`
