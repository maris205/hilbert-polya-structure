# P190 Review A — replay receipt

Checked: 2026-09-04 UTC.

Command, from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers187_191_sequence/reviews/p190_a/verify_p190_review_a.py
```

| item | result |
|---|---|
| verifier SHA-256 | `37cb9f0aa6ba41a9f2dfb337ecbd73e16ca341abf1b7a11288b5a5f7f626f538` |
| canonical SHA-256 | `0a81802b457a69fca9b02a51b12820a7cc0bb5a53bc971f637aa7d5053adc54a` |
| canonical lines / bytes | `51 / 5618` |
| fresh process 1 versus canonical | byte-identical (`cmp` status 0) |
| fresh process 2 versus canonical | byte-identical (`cmp` status 0) |
| parameter boxes | `28` |
| exact assertions | `2,615,881` |
| formal counterexamples | `0` |
| open findings | `Critical 0 / Major 0 / Minor 0` |
| historical deltas | `P190-A-MI-01 ACCEPTED; P190-A-MI-02 ACCEPTED` |
| verdict | `PASS_DELTA_ACCEPTED` |
| lifecycle | `OWNER_AMBER / HOLD_EXTERNAL` |

The verifier reads the seven pinned author inputs only to validate their hashes
and to freeze the observed source tokens.  It does not import or execute the
author implementation.  Its dynamical, fibre, image, and spectral routines
are reviewer-owned.
