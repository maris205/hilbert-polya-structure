# Test report

```text
python3 code/c205_dyck_shift_producer.py             PASS: 144 formula, 33 direct
python3 code/c205_dyck_shift_checker.py              PASS: 144 formal, 33 direct
python3 code/c205_dyck_shift_sympy_crosscheck.py     PASS: 72 series + 6 entropy + singularities
python3 code/c205_dyck_shift_replay.py               PASS: byte-identical evidence
python3 code/c205_dyck_shift_mutation.py             PASS: 19/19 rejected
```

The checker imports no producer module.  Formal power series use exact
fractions, while periodic-word counts and Möbius inversion use integers.

The fixed-epoch PDF audit closes at 3 pages and 244591 bytes with SHA-256
`203531a0984884266508021d163ed6a5d03b651919698f34b140495b939c4986`;
round 2 and `main.pdf` are byte-identical.
