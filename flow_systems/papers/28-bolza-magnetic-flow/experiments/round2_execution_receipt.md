# P28 Round-2 execution receipt

Date: **2026-08-27**
Mode: deterministic target-free owner bookkeeping
Status: **COMPLETED / REPLAY PASS**

## Commands

```bash
python3 code/test_owner_ledger.py
python3 code/build_owner_ledger.py \
  --tensor-powers 1,2,4,8 \
  --output results/bolza_tensor_family_owner_ledger.csv \
  --validation-output results/round2_owner_ledger_validation.json
```

The build was repeated into an isolated temporary directory and both outputs
were byte-compared with `cmp`.

## Verification

```text
UNIT_TESTS=7/7_PASS
BUILD_EXIT_CODE=0
REPLAY_EXIT_CODE=0
CSV_BYTE_MATCH=PASS
JSON_BYTE_MATCH=PASS
CSV_ROWS_INCLUDING_HEADER=13
```

SHA-256 after the replay:

```text
build_owner_ledger.py                  941987764ad6a76e4d389e57182e2449c86af2b8eb0b94ed7c19622b49bfbe06
test_owner_ledger.py                   37a037a2757559d9756b2e4f209d039d13256b3127ccfbd3605cf6da716b4b0f
bolza_tensor_family_owner_ledger.csv   0432d1430ddeea910af5d26415e8b553efdd2af70ca7cce74f0f799f675e0339
round2_owner_ledger_validation.json    b365cc482baf7799ba0ee76a79a2b3b47ac3ed9f72e8e2f633d1dcacc109d6e0
```

## Scope boundary

This execution generated no magnetic closed orbit, eigenvalue, trace,
prime-table, or zero-table data. `h=1/N` is recorded as a
`MODELING_CHOICE`; the rescaled operator, energy window, and trace regime stay
unassigned/open. All 12 rows retain
`magnetic_orbit_trace_ownership=NOT_ESTABLISHED` and forbid transfer to the
fixed operator.
