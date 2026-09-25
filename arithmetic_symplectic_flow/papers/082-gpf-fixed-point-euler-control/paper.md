<!-- PSR01 CORRECTION NOTICE START -->
> **2026-09-19 bounded dependency correction.** This control's own map and prohibited direct log-label readout boundary are unchanged. The comparison below describing 078 as a unique four-cycle and 081 as a single aggregate packet is false and WITHDRAWN. 081's full frozen owner includes prime log circles plus an extra log210 circle; its clock-naturalness promotion is not retained.
> See the [PSR01 source correction](../266-prime-source-return-rescreen/paper.md).
> This notice changes no frozen candidate definition or Route status.
>
> **Historical text retained below; the specified comparison is superseded.**
<!-- PSR01 CORRECTION NOTICE END -->

# A greatest-prime-factor fixed-point map can formally reproduce the Euler product only by a prohibited readout

**Paper ID:** 082-gpf-fixed-point-euler-control  
**Record ID:** ASFS-SCOUT-20260914-55  
**Date / status:** 2026-09-14; PROHIBITED EXTERNAL POSITIVE CONTROL  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## The tempting formal object

On integers n >= 2 define

\[
P(n)=\operatorname{gpf}(n).
\]

For a prime p, P(p)=p. For a composite n, its greatest prime factor is strictly
smaller than n. Thus all composite points strictly descend under P until a prime
is reached, and the complete periodic set is exactly the set of prime fixed
points.

If one then declares a roof on those fixed points by

\[
\tau(p)=\log p,
\]

the formal primitive-orbit product is

\[
\prod_{p\ \mathrm{prime}}(1-e^{-s\log p})^{-1}
=\prod_p(1-p^{-s})^{-1},
\qquad \operatorname{Re}s>1.
\]

This identity is not a discovery of a dynamical mechanism. It is the Euler
product written after the map has already returned the prime label and the roof
has explicitly converted that label to log p.

## Why this is a prohibited control

The map directly invokes global integer factorization and labels every prime as
a fixed point. The roof then assigns precisely the desired prime logarithm to
that label. This is the forbidden manual pattern T_p=log p in functional
notation. It has no named deformation from the prior Eratosthenes-symbolic
source, no Logistic/Hénon conservative lift, no positive-dimensional symplectic
base, and no independent derivation of an arithmetic clock.

It also proves too much: for any externally chosen set A one could define a
recognizer/retraction with A as its fixed set and attach a prescribed roof to
its labels. The algebraic orbit product would merely restate the supplied
weights. The present factorization oracle is more canonical than an arbitrary
program, but that does not repair the absent project lineage or the direct
prime-label-to-time insertion.

The GPF-Fibonacci source control in 078 differs materially: its gpf rule occurs
inside a second-order recurrence and its unique 4-cycle has a complete ledger.
081's aggregate roof is a single edge formula on that one packet. Neither result
licenses the pointwise fixed-label roof used here.

| Gate | Result |
| --- | --- |
| arithmetic recognition | exact but factorization-oracle control |
| periodic ledger | exact prime fixed points |
| clock | prohibited direct log-label readout |
| lineage | scoped FAIL |
| symplectic P0 / A1 / A2 | NOT EVALUATED |
| Route B | NOT INVOKED |

## Decision

**Portfolio position: stop/exclude.** 082 is a negative control against
mistaking a formal Euler product for a candidate. Do not refine its zeta,
quantize it, or attach a geometric lift. Future candidates must generate their
symbolic/arithmetic structure through the permitted lineage and derive any clock
without a pointwise prime-label-to-log assignment.

## Evidence index

- [047 sum-of-prime-factors fixed-point control](../047-sopfr-prime-fixed-point-control/paper.md)
- [078 GPF-Fibonacci A0/A1 control](../078-gpf-fibonacci-a0-a1-control/paper.md)
- [081 aggregate GPF log-roof path flow](../081-gpf-log-roof-path-flow/paper.md)
- [011 reversible sieve simulation control](../011-reversible-sieve-simulation-control/paper.md)
