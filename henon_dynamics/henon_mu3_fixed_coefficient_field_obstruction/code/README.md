# HCS-C44 exact computation

The producer enumerates the exact phase histogram

\[
N_p(r)=\#\{(x,y)\in\mathbf F_p^2:
2x^3+2y^3+(1+\rho_p)xy=r\}
\]

for every split prime through 499.  It then records the paired histogram,
the two nonzero power-moment witnesses used by the all-prime proof, the exact
scaling stabilizer, the resulting real-cyclotomic field degree, and the
degree-three anchor at \(p=7\).

`c44_checker.py` does not import the producer.  It uses a separately written
counter, a brute-force multiplicative-order calculation, independent moment
formulas, and an exact reduction in
\(\mathbf Q[z]/(1+z+\cdots+z^6)\) for the `p=7` polynomial.

Run the frozen release from the project directory with:

```bash
./code/run_c44.sh
```

The runner regenerates both JSON artifacts in a temporary directory, checks
them byte for byte, runs 25 mutation/regression tests, and verifies the
release hash manifest.  `--refresh-manifest` writes a new manifest only after
all preceding gates pass.
