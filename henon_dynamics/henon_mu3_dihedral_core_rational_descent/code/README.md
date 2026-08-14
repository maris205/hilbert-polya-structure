# HCS-C53 exact code lane

This directory produces and independently checks the exact certificate for the
all-\(n\) quadratic-descent theorem and the \(n=4\) rational dihedral-core
descent.  The checker uses a custom exact \(\mathbf Q(\rho)\) pair algebra; it
does not import the producer or trust stored boolean claims.

Run the frozen artifacts without changing them:

```bash
./code/run_c53.sh
```

Refresh the certificate, independent check, and full-project manifest as one
rollback-safe transaction:

```bash
./code/run_c53.sh --refresh-results --refresh-manifest
```

`--refresh-results` is rejected unless `--refresh-manifest` is also present.
Set `C53_INJECT_PROMOTION_FAILURE_AFTER=1`, `=2`, or `=3` to exercise
transaction rollback.  The targeted suite covers all three failure positions
and a transaction with a missing initial target.  It independently rehashes
each altered certificate and requires both the frozen-payload gate and the
named semantic gate to fail without checker errors.

The manifest inventories the complete frozen project: root documentation,
the manuscript and compiled PDF, the byte-identical root and archived Route-A
records, code, and results.  LaTeX build intermediates, extracted `main.txt`,
Python caches, and the manifest itself are excluded.  The default runner
reconstructs the two JSON artifacts in a temporary directory, checks the
Route-A byte identity, and verifies the full inventory without modifying
stable bytes.
