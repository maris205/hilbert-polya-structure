# Control results

Final hostile-audit execution (2026-08-28 UTC):

```bash
python3 code/verify_periodic_alphabet.py
```

Result:

```text
PASS: 5,242 exact assertions across 340 schedules
schedule=(2, 6): (p,Q)=(2,12), fixed=[0, 24, 0, 288]
schedule=(3, 4): (p,Q)=(2,12), fixed=[0, 24, 0, 288]
schedule=(1, 2, 3): (p,Q)=(3,6), fixed=[0, 0, 18, 0, 0, 108]
schedule=(2, 2, 2): (p,Q)=(3,8), fixed=[0, 0, 24, 0, 0, 192]
normal-form periodic ledgers and characteristic polynomials verified
```

In addition to traces, characteristic polynomials, and class ledgers, the
script directly checks the non-wrap and wrap coordinate identities in the
block conjugacy.
