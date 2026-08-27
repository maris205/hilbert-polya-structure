# P24 code status — Round 2 executed

`round2_bianchi_ledger.py` uses exact pairs of Python integers for Gaussian
arithmetic.  It enumerates the reduced word ball of
`U(3), U(3i), L(3), L(3i)` and their inverses through frozen word length 5,
deduplicates exact matrices, checks determinant and level membership, identifies
power relations visible inside the sample, reconstructs PSL complex lengths,
and emits a deterministic holonomy shuffle without consulting prime or zero
tables.

Commands:

```bash
python3 code/test_round2_bianchi_ledger.py -v
python3 code/round2_bianchi_ledger.py
python3 code/round2_bianchi_ledger.py --verify-existing
```

The test suite covers exact generator and row membership, inverse closure,
projective trace reconstruction, target-free controls, and byte determinism.
The code intentionally does not assert full `Gamma((3))` generation or full
conjugacy/primitivity completeness.
