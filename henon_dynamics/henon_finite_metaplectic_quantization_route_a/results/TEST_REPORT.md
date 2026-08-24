# Test report

```text
python3 code/c128_metaplectic_producer.py  PASS (exact cyclotomic field)
python3 code/c128_metaplectic_checker.py   PASS (independent complex matrices)
python3 code/c128_sympy_crosscheck.py      PASS (22 checks)
python3 code/c128_replay.py                PASS
python3 code/c128_mutation.py              PASS (32/32 rejected)
```

The exact producer and numerical checker use independent representations and
do not import one another.  The checker validates every headline ledger field,
including phase conventions, action, spectrum, determinant, exact-check
counts, and the even-modulus control.
