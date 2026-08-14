# Test report

Command:

```bash
bash code/run_c56.sh
```

Results:

- primary exact producer: PASS;
- independent DFS/algebra checker: PASS;
- unit tests: 15/15 PASS;
- hostile claim mutations: 20/20 rejected;
- dependency locks: 7/7 matched;
- normal and optimized (`python -O`) producer output: byte-identical;
- primitive-cycle counts through period six: independently matched;
- incidence ladder: direct check for every width 3 through 64;
- period-six recurrence residuals: 6/6 exactly zero;
- multiplier irreducibility: independent modulo-13 check matched;
- exact integer obstruction margin: 96,873;
- width-five selected determinant: \(+1\);
- no rational-prime or zeta-zero table consumed;
- no Python cache required (`-B` and `PYTHONDONTWRITEBYTECODE=1`).

The executable certificate verifies the finite-memory obstruction and the
algebraic/symbolic inputs to the all-width theorem.  The all-\(m\) statement
itself is proved in the manuscript; the finite range is an implementation
guard, not an extrapolation.  The tests do not claim a general Hölder no-go.
