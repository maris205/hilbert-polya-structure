# HCS-C239 — multiway perfect-shuffle cycle atlas

This source-local Route-A package studies the exact finite permutation
\\[
  \\rho_{k,n}(i)=ki\\pmod{M},\\qquad M=kn+1,\\quad 1\\leq i<M.
\\]
It proves `Fix(r)=gcd(k^r-1,M)-1`, the position order
`ord_(M/gcd(i,M))(k)`, Möbius least-period and primitive-cycle formulas, and
the finite zeta/Koopman factorizations.  The receipt covers 50 parameter pairs
and independently exhausts every listed residue phase space.

The arithmetic firewall is literal `NO_BAD_EULER_OR_ROOT_NUMBER`.  Integer
moduli and multiplicative orders are source-local combinatorics, not prime
carriers, logarithmic lengths, or target data; consequently the strict tuple
is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and
Route B is disabled.

Reproduce the package with:

```text
python3 -B code/c239_shuffle_producer.py
python3 -B code/c239_shuffle_checker.py
python3 -B code/c239_shuffle_sympy_crosscheck.py
python3 -B code/c239_shuffle_replay.py
python3 -B code/c239_shuffle_mutation.py
python3 -B code/c239_release_manifest.py
```

The final paper is `paper/main.pdf`; round 0/1/2 PDFs document two substantive
revision steps.
