# HCS-C49 exact computation

This directory certifies the third chronological moment without replacing the
ordered six-step phase by an averaged transition matrix.  It separates three
logically different layers:

1. the exact radial identity
   `Z=1+#P5-#S-#Q+p#X` and the split-quadric count;
2. generic characteristic-zero smoothness of the `(2,3)` Fano threefold,
   together with an explicit finite-characteristic elimination firewall;
3. finite reproducibility controls, which do not assert all-split-prime
   smoothness.

The producer uses first-nonzero-coordinate charts on the split quadric and an
array-valued literal chronology DP.  The checker uses last-nonzero-coordinate
charts, sparse-dictionary Fermat convolutions, a dictionary chronology DP, and
the reversed normalized singular recurrence.  It also recomputes the exact
41-by-41 Sylvester determinant by fraction-free Bareiss elimination, verifying

`Res(R,H) = 2^21 * 3^12 * 23^3`.

The certificate distinguishes theorem-level arithmetic from finite data.  The
Fermat--Jacobi formula `alpha=20*p^2+p*a_p` is an all-split-prime theorem, and
Chevalley--Warning gives `p | beta` at good split primes.  The displayed values
of the quotient traces and any finer pattern among them remain a finite ledger.

The operator conclusion is a normalized semifinite `tau`-associated graded
`Det_8` on `Re(s)>1/4`.  It is not a classical Fredholm determinant.  The
certificate separately freezes

`X_s in L^q(M,tau) iff q*Re(s)>2`

and

`X_s in S^q(H) iff q*Re(s)>3`.

Run `./code/run_c49.sh` from the project directory.  It regenerates both JSON
artifacts in a temporary directory, requires byte identity with the frozen
results, runs 55 isolated gate-mutation tests, and verifies the manifest.  Use
`./code/run_c49.sh --refresh-manifest` only when intentionally freezing a
complete artifact set.
