# HCS-C45 exact computation

The C45 release has two exact ledgers.

1. For every split prime through 499 it counts the chronological first phase
   zero fibre, verifies (N_{p,1}(0)=p-3), reconstructs
   (C_{p,1}=-6), and records the ordinary Galois-norm virtual degree
   (2(p-1)) together with exact bounded-prefactor triangle inequalities.
2. For eleven frozen primes through 97 it counts the genuine ordered
   four-variable phase
   
   \[
   x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0
   +2\sum_{j=0}^3x_j^3
   \]
   
   and reconstructs both (C_{p,2}) and the normalized moment
   (c_{p,2}=C_{p,2}/d_p).  No averaged transition matrix is used.

The independent checker does not import the producer.  It uses separately
written zero counters, rebuilds all exact fractions and virtual-degree
bounds, and checks a frozen second-moment ledger.  The normalized object

\[
G_p(z)=\exp\!\left(d_p^{-1}\operatorname{Log}_0N_p(z)\right)
\]

is deliberately classified as a local analytic branch, not as an ordinary
rational or Fredholm determinant.

Run the frozen release from the project directory with:

```bash
./code/run_c45.sh
```

The runner regenerates both JSON artifacts in a temporary directory, compares
them byte for byte, runs 28 mutation/regression tests, and verifies the
release hash manifest.  `--refresh-manifest` writes a new manifest only after
all preceding gates pass.
