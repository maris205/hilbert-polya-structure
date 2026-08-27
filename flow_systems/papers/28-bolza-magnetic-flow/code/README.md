# P28 code status

## Round 3

`build_round3_trace_contract.py` generates and validates the 12-row
source-bound contract for `N=2,4,8,16` and fields `0,+1/2,-1/2`.
`test_round3_trace_contract.py` has eight independent standard-library tests,
including the fixed-`k` positive/negative action-sign pairing.
Canonical reproduction is:

```bash
./experiments/reproduce_round3.sh
```

The generated contract does not contain eigenvalue or orbit samples.  It
authorizes the source-compatible signed-field even-subsequence owner theorem,
while retaining an open zero-field owner and all fixed-operator firewalls.

## Round 2

`EXECUTION_STATUS=ROUND2_OWNER_LEDGER_COMPLETED`. The owner lemma now freezes
the connection/dual connection, sign convention, named Hilbert spaces,
operators, domains, bundle degrees, field-reversal partners, and holonomy
repetition. `build_owner_ledger.py` generated a 12-row target-free ledger for
`N=1,2,4,8`; `test_owner_ledger.py` passed 7/7 tests and replayed
byte-identically.

Those `UNASSIGNED`/`OPEN` fields are the immutable Round-2 state.  Round 3 adds
a separate, narrower source-compatible even-subsequence contract rather than
rewriting historical artifacts.

The implementation must key all spectral outputs by `tensor_power_N` and must
reject pooling with the separate fixed candidate `Δ^L`.  A `PROVED` same-owner
token is permitted only for the verified source-compatible signed-field even
subsequence.  All other regimes remain `[OPEN]` / `NOT_ESTABLISHED` until a
separate trace theorem is verified.
