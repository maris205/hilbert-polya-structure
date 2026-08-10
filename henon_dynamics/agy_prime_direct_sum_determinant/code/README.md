# HCS-C28 code

The producer source-locks C24--C27 and emits the exact prime-assembly
certificate.  The independent checker does not import it: matrix replay,
determinants, minors, factorization, Jacobi symbols, and the C24 census use a
separate list-arithmetic implementation.

Run the full release:

```bash
bash code/run_c28.sh
```

The default command is a read-only manifest verification.  After an
intentional release update, refresh the frozen manifest explicitly and then
verify it:

```bash
bash code/run_c28.sh --refresh-manifest
bash code/run_c28.sh
```

No program expands the previous bounded prime window.  The all-prime
statements use exact integral minors, Thomas's character formula, and
classical convergence theorems.
