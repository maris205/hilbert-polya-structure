# P27 code status

Round-2 code is now landed:

- `round2_reduction_orders.py` freezes three `Gamma(3)` matrices, computes
  their projective reduction orders at all eight registered moduli, writes the
  CSV/JSON/manifest artifacts, and verifies exact artifact and source-binding
  bytes and hashes;
- `test_round2_reduction_orders.py` checks the matrix owners, all 24 independent
  order cross-checks, the frozen order sequences, deterministic serialization,
  and the finite-owner firewall.

The two order algorithms are deliberately different: one multiplies until the
first `+I` or `-I`; the other starts from the exact order of
`SL_2(Z/qZ)` and removes factors by binary powering.  The factorization is only
of the already frozen congruence moduli/group orders; no rational-prime target
table or Riemann-zero data enters the candidate.

Run from the paper directory:

```bash
bash experiments/reproduce.sh
```

The analytic `[PROVED] PROVED_A1_OBSTRUCTION` does not depend on this code.
Every generated row marks the finite-level statistic as not owned by the
inverse-limit flow.

Round 4 adds `round4_period_escape.py` and
`test_round4_period_escape.py`.  The generator reads the frozen Round-2 ledger
by exact SHA-256, checks the nested-modulus and order-divisibility contracts,
and emits a 24-row period-escape ledger plus validation JSON.  It explicitly
marks the asymptotic result as proved in the human-readable theorem rather than
inferred from the finite prefix.

```bash
bash experiments/reproduce_round4.sh
```

Eight tests and two byte-identical builds must pass.  No prime/zero target data,
formal Route tuple, or inverse-limit orbit credit enters the computation.

Round 5 adds `round5_cocompact_owner_escape.py` and
`test_round5_cocompact_owner_escape.py`.  The generator freezes a closed
genus-2 surface-group presentation, three primitive-homology words, and the
eight moduli `n!` for `1<=n<=8`.  It computes exact additive homology orders
and records them only as certified lower bounds for the unenumerated full
quotient orders.

```bash
bash experiments/reproduce_round5.sh
```

Ten tests and two byte-identical builds must pass.  The code does not enumerate
the residual cores, numerically choose a hyperbolic metric, or import any
prime/zero target.  Residual finiteness, tower residuality, and the minimal
geodesic-period argument remain human-readable proofs in the Round-5 note.
