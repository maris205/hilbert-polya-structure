# P122 exact-control results

Status: **FRESH PAPER-LOCAL PASS / NONCOMPUTATIONAL CLAIMS BOUNDED**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The standard-library verifier makes no network call, random draw, or
floating-point comparison.  Its canonical transcript is
`code/verification_output.txt`.

## Stored result

```text
record-block reversal fibre verifier: PASS
assertions=1636476
record-block image automaton: PASS
assertions=551
combined_assertions=1637027
```

The literal lane exhausts every source and target for `0<=n<=9`, checks
fixed points, all fibres, maximum fibres, admissible-cut reconstruction,
the DP, image membership, and total fibre mass.  The aggregate lane derives
the same image counts independently from record indicators through `n=9`,
checks factorial mass, and continues the transfer through `n=30`.

The first image values for `0<=n<=9` are

```text
1, 1, 1, 4, 12, 60, 320, 2160, 15960, 138880.
```

The controls do not prove the all-size theorem, ownership, novelty, priority,
or external safety.
