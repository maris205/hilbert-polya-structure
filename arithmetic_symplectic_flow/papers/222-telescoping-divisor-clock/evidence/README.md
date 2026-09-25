# Evidence record — ASFS-20260918-TDC01

**Status:** STOP — TELESCOPING ROOF HAS THE OFFSET log 2; NO PRIME-LOG CLOCK.

## Scope and correction provenance

The exact object was frozen before proof writing. The first audit draft
incorrectly stated
\(\sum_{d=2}^{p-1}\log((d+1)/d)=\log p\).
Readback audit identified the missing factor 2 in the denominator. The
mathematical definition was not altered: \(D_n=\{2,\ldots,n-1\}\) for
\(n\ge3\), \(D_2=\{1\}\), and the same roof remain intact. The corrected
result is \(\log(p/2)\) for odd primes; all downstream positive Euler-product
or exact-clock language was withdrawn.

This correction is a same-thread model audit, not peer review or a certified
computer proof. It is recorded because the original hypothesis failed.

## Exact audit methods

1. Global inverse and symplectic pullback on every component plane.
2. Positive fixed-\(n\) minimum roof in both time directions; no finite-time
   accumulation despite global roof infimum zero.
3. Sum the exact recurrence around an arbitrary possible period. Every square
   and witness must vanish, giving the entire prime-only periodic ledger.
4. Multiply every adjacent ratio from \(d=2\) through \(n-1\): the product is
   \(n/2\), with no \(d=1\) interval added. The \(n=2\) sentinel is checked
   separately.
5. Derive the same map's monodromy \(A=I+N,\ N^2=0\); retain every repeated
   degeneracy.
6. Record only the actual-clock ordinary product and reset-edge cohomology;
   do not import 160's clock or operator credit.

## Inputs, limits, and controls

No prime table, zero data, numerical cutoff, GPU calculation or fitted
parameter is used. The claims are exact full-state proofs. Zero-witness,
shifted-test, unit-roof, phase-boundary, noncentral-state and monodromy
controls are listed in the paper. The comparison with
[160](../../160-source-geometric-return-clock/README.md) was read directly;
its engineered timing and source-clock naturalness limit remain distinct.

## Mechanical verification

The five package files are checked for local links, one candidate ID, and
consistent stop status. These checks concern artifact consistency only; they
do not strengthen the mathematical or Route verdict.
