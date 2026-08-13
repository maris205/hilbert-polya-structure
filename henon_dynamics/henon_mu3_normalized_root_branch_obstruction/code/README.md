# HCS-C46 exact computation

C46 certifies the first-prime divisor obstruction to the normalized Galois
root from C45.  At (p=7), it starts from the exact three sector
characteristic polynomials in
(mathbf Q(zeta_7)[z]), forms
(q_k=D_k\overline{D_k}), descends through
(	heta=zeta_7+zeta_7^{-1}), and computes exact cubic resultants.

The final reduced norm is

\[
N_7(z)=\frac{P_{18}(z)^2}{49P_{12}(z)^2}.
\]

Good reduction modulo five proves that (P_{18}) and (P_{12}) are
coprime and individually squarefree.  Thus every finite divisor order is
(pm2), not divisible by (d_7=3); the normalized cubic root has local
orders (pm2/3).

The independent checker does not import the producer or SymPy.  It implements
cyclotomic multiplication, conjugation, real-subfield reduction, a direct
three-dimensional multiplication determinant for the norm, and finite-field
Euclidean gcds from scratch.

Run the frozen release with:

```bash
./code/run_c46.sh
```

The runner regenerates both JSON artifacts, checks byte identity, runs 33
mutation/regression tests, and verifies the release manifest.
