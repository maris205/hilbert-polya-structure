# Control results

Final hostile-audit execution (2026-08-28 UTC):

```bash
python3 code/verify_unitary_cayley.py
```

Result:

```text
PASS: 19,901 exact assertions
n=5: phi=4, period=1, P2=20
n=8: phi=4, period=2, P2=32
n=12: phi=4, period=2, P2=48
n=15: phi=8, period=1, P2=120
Ramanujan trace formula, parity dichotomy, and rigidity registry verified
```

The script uses integer matrices and exact rational arithmetic.  It now also
checks every Ramanujan multiplicity in the tested range directly.
