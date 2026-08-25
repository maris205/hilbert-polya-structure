# HCS-C157: square-billiard Abel half-wave trace

C157 derives an exact Poisson formula for the genuine Dirichlet Abel
half-wave trace of the unit square,

```text
W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2)),   Re(s)>0.
```

The dual formula separates the Weyl zero mode, dual axes, interior primitive
square-billiard directions with all repetitions, and the boundary
subtraction.  The interior terms give a source-derived bridge to clean-family
lengths `L_(a,b)=2*sqrt(a^2+b^2)`.  Exact shell ledgers through squared norm
500 and two high-precision, tail-bounded numerical sentinels close the result.

The construction is a source Dirichlet trace, not an isolated-orbit
determinant or a target trace identity.  Route B is disabled.

## Reproduce

```bash
python code/c157_abel_trace_producer.py
python code/c157_abel_trace_checker.py
python code/c157_sympy_crosscheck.py
python code/c157_replay.py
python code/c157_mutation.py
```

The final paper is `paper/main.pdf`; release closure is recorded in
`C157_RELEASE_MANIFEST.json`.
