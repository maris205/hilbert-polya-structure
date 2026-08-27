# P28 code status

## Round 4

`build_round4_bolza_owner_ledger.py` transcribes the published genus-two
opposite-side-pairing matrices, replays their determinants, common trace, and
polygon relator at 120-decimal precision, and emits the first target-free
Bolza magnetic-owner seed ledger.  Its declared scope is four systolic
inverse-paired primitive axis owners per field, equation-(19) signed branches
`k=+-1,+-2,+-3`, and fields `b=+1/2,-1/2` under the frozen Round-3 even
subtype: 24 branches per field and 48 rows total.  The negative-`k` branch may
store `f_j^-1`, but it shares the same `primitive_axis_owner_id` and receives no
second owner credit.

`test_round4_bolza_owner_ledger.py` has twelve tests covering the group source
lock, inverse-paired primitive certificate, four-owner-per-field grid, absence
of orientation owner credit, signed-`k` laws, `(b,k)->(-b,-k)` field reversal,
action, both clocks, signed/absolute stability, Maslov index, target-data
absence, and route firewalls.  Canonical reproduction is:

```bash
./experiments/reproduce_round4.sh
```

The matrix residuals validate the source transcription; they do not replace
the source's Poincare-polygon theorem.  The generator list is not promoted to a
complete primitive spectrum.

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
