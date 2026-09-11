# Owner and collision log — divisor-imbalance dynamics

**Date:** 2026-09-03 UTC  
**Status:** bounded search / no novelty claim / `HOLD_EXTERNAL`

## Exact-expression search

Searches included the literal strings
`lcm(d,n/d)/gcd(d,n/d)`, `lcm(d,n/d) gcd(d,n/d) divisor map`,
`divisor dynamics folded doubling prime exponents`, and the exact exponent
recurrence `|2a-e|`.  The strongest literal hit was
[OEIS A332618](https://oeis.org/A332618), which sums
\(\operatorname{lcm}(d,n/d)/\gcd(d,n/d)\) over all divisors.  It owns the
static arithmetic expression and a multiplicative sum formula; it does not
define or iterate the fixed-(N) divisor self-map in the inspected record.

This is a bounded non-hit, not evidence of novelty, priority, ownership, or
freedom to circulate.

## Mechanism owners receiving zero credit

- The standard full tent map and dyadic map literature owns the
  doubling/reflection semiconjugacy and general rational eventual
  periodicity.  A direct modern control is Scheicher,
  [*Dynamical properties of the tent map*](https://doi.org/10.1112/jlms/jdv071),
  *J. London Math. Soc.* 93 (2016), 319--340.
- Finite/digital tent maps have a substantial engineering and dynamical
  literature.  The candidate claims no invention of a tent map, its binary
  itinerary, or generic periodic-point machinery.
- The fundamental theorem of arithmetic and the coordinate identities
  \(\nu_p(\gcd)=\min\), \(\nu_p(\operatorname{lcm})=\max\) are background.

The residual being tested is narrower: the complete finite divisor-graph
package with exponent-sensitive tails and the arbitrary-time endpoint-correct
fibre atlas.  The owner search has not yet found that conjunction stated for
this arithmetic self-map.

## P1--P161 subtraction

- P97 sumset squaring is a nonlinear subset map and does not use divisor
  complements or folded exponent doubling.
- P100 least-valuation digit erasure and P142 valuation--GCD divisor dynamics
  use valuation strata, but their coordinate maps are erasure/GCD descent,
  not the reflected map \(a\mapsto|2a-e|\), and neither supplies the cycle
  census plus endpoint-split all-time fibres here.
- P107 iterates powers/annihilators of ideals; no tent quotient occurs.
- P108 and P115 own generic recurrence/finite-functional-graph tools.  Formula
  (8) alone earns no separation credit; the divisor-specific depth and fibre
  package must carry the note.
- P128 is translation--GCD factor erosion and P131 is a Euclidean quotient
  queue.  Both are absorbing, whereas this system retains an odd-modulus
  recurrent core with nontrivial cycles.
- P154 uses subgroup normalizers and an arithmetic binary inverse tree.  The
  carrier and literal operation are unrelated.

No same-batch collision exists with RTI's stochastic subset intersections or
CEF's equality-feedback word dynamics.  A later direct owner of the complete
divisor/tent/fibre conjunction triggers narrowing or kill.

## Preliminary verdict

`KILL_EXACT_INTERNAL_X01_DUPLICATE`.  The hostile gate also identified direct
Cobeli--Zaharescu and Cobeli--Prunescu--Zaharescu owner chains.  This correct
system is archive-only and cannot be resurrected.  External status remains
`HOLD_EXTERNAL`.
