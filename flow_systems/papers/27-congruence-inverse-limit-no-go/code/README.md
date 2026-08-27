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
