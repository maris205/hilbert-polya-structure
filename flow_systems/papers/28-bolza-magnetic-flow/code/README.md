# P28 code status

`EXECUTION_STATUS=ROUND2_OWNER_LEDGER_COMPLETED`. The owner lemma now freezes
the connection/dual connection, sign convention, named Hilbert spaces,
operators, domains, bundle degrees, field-reversal partners, and holonomy
repetition. `build_owner_ledger.py` generated a 12-row target-free ledger for
`N=1,2,4,8`; `test_owner_ledger.py` passed 7/7 tests and replayed
byte-identically.

The code deliberately leaves the rescaled operator `UNASSIGNED`, energy window
`OPEN`, trace regime `UNASSIGNED`, and orbit ownership `NOT_ESTABLISHED`.

The implementation must key all spectral outputs by `tensor_power_N` and must
reject pooling with the separate fixed candidate `Δ^L`.  It must not emit a
same-owner evidence token stronger than `[OPEN]`, or change the exact pipeline
state from `NOT_ESTABLISHED`, without a separately verified trace theorem.
