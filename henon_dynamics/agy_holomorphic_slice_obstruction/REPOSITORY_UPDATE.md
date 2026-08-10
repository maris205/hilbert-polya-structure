# HCS-C26 repository update

## Release scope

HCS-C26 takes the holomorphic/no-localizer gate left by HCS-C25 and closes
it at theorem level.  It preserves the published countable AGY return map,
the raw chronological Rauzy matrices, and the unsmoothed oscillator fibre.
No finite transition average, Hermite truncation, or fitted arithmetic data
is used.

## Main additions

1. A self-contained complex-cone argument constructs one bounded domain
   `Omega` in complex projective dimension three with a common relatively
   compact image for every AGY inverse branch.
2. The raw scalar weights use one principal logarithm and are summable in
   sup norm locally uniformly on `Re(s)>-sigma_0`.
3. The scalar Bergman transfer operator is trace class and

   \[
   D(s,u)=\det(I-uL_s)
   \]

   is jointly holomorphic on the source half-plane times the full Fredholm
   variable plane.
4. For every genuine ordered return word,

   \[
   \operatorname{tr}T_{s,w}
   =\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
   \]

   The raw integer word matrix is formed before taking its characteristic
   polynomial, so chronology and word multiplicity are retained.
5. On the same domain, the literal oscillator-valued Bergman operator is
   bounded but noncompact.  Constants and one point evaluation expose the
   full `ell^1` family of distinct metaplectic atoms and yield an explicit
   positive essential-norm lower bound.

## Reproducibility

Run:

```bash
cd henon_dynamics/agy_holomorphic_slice_obstruction
./code/run_c26.sh
```

The deterministic suite rebuilds the exact length-128 source witness,
checks contravariant two-return bookkeeping and a spectrally
chronology-sensitive three-return noncyclic reversal, runs an implementation-
independent checker, executes 21 regression/mutation tests, replays a
13,528-return finite non-proof sentinel, and verifies a SHA-256 artifact
manifest.

## Route-A decision

The target infinite-oscillator candidate is classified as

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

The scalar determinant and Perron-characteristic trace formula remain
reusable positive infrastructure.  They do not establish a self-adjoint
Hilbert--Polya operator, a prime law, a functional equation, or a Riemann
divisor.

## Authorized next large door

The next experiment should reduce the exact chronological genus-two cocycle
modulo odd primes and attach the finite Weil representation

\[
\rho_p:\operatorname{Sp}(4,\mathbb F_p)\longrightarrow U(p^2).
\]

This changes the fibre rather than trying another small variation of the
base norm.  It preserves chronological arithmetic information and supplies
ordinary finite Gauss-sum characters, but it is a new model rather than a
limit formula for the ordinary infinite oscillator trace.
