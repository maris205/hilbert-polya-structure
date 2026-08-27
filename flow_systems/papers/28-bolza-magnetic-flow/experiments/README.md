# P28 experiment status

## Round 3

`EXECUTION_STATUS=ROUND3_SOURCE_CONTRACT_COMPLETED`. Run:

```bash
./experiments/reproduce_round3.sh
```

Eight tests pass; two isolated contract builds are byte-identical.  The
artifact tree SHA-256 is
`a28bf68d0da5c34350224031428f18f325af0d11619df95f2509741475275f3d`.
The run validates the deterministic schema/status contract and exact rational
scaling identities.  It does not independently prove or re-check every
hypothesis of the cited trace theorem, and it generates no eigenvalue or orbit
data.

## Round 2

`EXECUTION_STATUS=ROUND2_OWNER_BOOKKEEPING_COMPLETED`. The deterministic
owner-bookkeeping run and its byte-identical replay are recorded in
`round2_execution_receipt.md`. This is not a magnetic-orbit, spectral, or trace
experiment. Frozen controls are

- zero field `b=0` on a degree-zero trivial bundle with trivial connection;
- positive field `b=+1/2` on the degree-one bundle `L`;
- negative field `b=-1/2` on the degree-minus-one dual bundle `L^*`;
- symmetry-resolved versus unsymmetrized ledgers; and
- an area-, field-, base-degree-, tensor-power-, energy-window-, and
  trace-regime-matched non-arithmetic metric.

Every tensor-family comparison must use a common `N`.  A fixed-operator
high-energy control is a separate regime and cannot be used as evidence for the
`N→∞` family.

The non-arithmetic genus-2 metric is still not instantiated.  Round 3 has bound
the signed-field even-subsequence operator, window, trace distribution, and
owner.  The next experiment is its primitive-orbit ledger followed by the
matched non-arithmetic metric; other regimes remain open.
