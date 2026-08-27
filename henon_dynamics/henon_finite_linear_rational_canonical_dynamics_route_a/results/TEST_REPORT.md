# Test report

Commands and expected outcomes:

```text
python3 code/c204_finite_linear_producer.py             PASS: 8 cases, 144 cells
python3 code/c204_finite_linear_checker.py              PASS: independent ranks/graphs
python3 code/c204_finite_linear_sympy_crosscheck.py     PASS: 198 gcd, 6 charpolys
python3 code/c204_finite_linear_replay.py               PASS: byte-identical evidence
python3 code/c204_finite_linear_mutation.py             PASS: 18/18 rejected
```

The checker imports no producer module.  Exact arithmetic is used throughout;
there are no floating-point tolerances.

The fixed-epoch PDF audit closes at 2 pages and 261852 bytes with SHA-256
`336d039d320202a36f7c3c64af1c6bc7a058431575b8ce4e78336d2e5016a38a`;
round 2 and `main.pdf` are byte-identical.
