# Claims–Evidence Map

| Claim | Proof location | Deterministic control |
|---|---|---|
| `Soc(R)=m^a`, `|V_i|=(q-1)q^(a-i)`, and the edge rule is exactly `v(x)+v(y)=a` | Lemma 2.1 | Abstract layer counts plus concrete product valuations in both ring models |
| Complete-bipartite blocks and the even central full-shift block | Theorem 3.1 | Valuation component involution `i -> a-i` for all 20 controlled parameter pairs |
| Adjacency rank is exactly `a+1` | Theorem 3.1 and quotient (7) | Exact rational row reduction of the nonsingular `(a+1) x (a+1)` quotient |
| Every SCC has Perron value `rho=(q-1)q^(a/2)` and entropy `log rho` | Theorem 3.1 | Exact identities `w_i w_(a-i)=rho^2`, including the even central square |
| `floor(a/2)+1` ergodic MMEs and the full MME simplex | Theorem 4.1 | Component count and equal-Perron checks; Parry uniqueness is cited input |
| Odd/even transition: no mixing maximal component for odd `a`, exactly one for even `a` | Theorem 4.1 | Exact component sizes: two-layer blocks have period two; the singleton valuation block has loops |
| Every `F_n` and the complete characteristic polynomial | Theorems 3.1 and 5.1 | Exact quotient traces through period 10 for every controlled `(q,a)` |
| Rational Artin--Mazur zeta formula | Theorem 5.1 | Exact polynomial computation of `det(I-zQ)` against the closed factorization |
| Every least-period point and temporal orbit count | Equation (12) | Möbius inversion of the controlled fixed-count sequence |
| `F_1,...,F_4` recover `(q,a)` | Theorem 6.1 | Exact branchwise recovery on all 20 pairs; no controlled four-period collision |
| Same `(q,a)` implies one-block conjugacy; finer ring structure collapses | Theorem 6.1 | Explicit layerwise pairing of `Z/p^(a+1)Z` and `F_p[t]/(t^(a+1))` for `p=2,3,5`, `a=1,...,5` |
| The displayed collapse can identify nonisomorphic rings | End of Section 6 | Characteristic witnesses `p^(a+1)` versus `p` in every dual-model control |

The control program is a regression guard, not a replacement for the proofs.
All-parameter scope follows from the valuation argument for arbitrary finite
commutative chain rings.  The finite controls intentionally include the
nonprime residue field `q=4`.

## Owner subtraction

Anderson--Livingston own the zero-divisor graph framework, and
Rattanakangwanwong--Meemark own spectral and rank calculations for the
zero-product graph over finite chain and principal ideal rings.  P87 does not
claim those results.  Its adjacency boundary is `v(x)+v(y)=a`; the classical
zero-product relation is at or beyond `v(x)+v(y)=a+1`, on a different vertex
set and convention for loops.  The external release status is `HOLD` pending
specialist priority clearance.

Dolžan (2026) owns the still closer fixed-product matrices
`A_u=(1_(xy=u))` and characteristic-polynomial calculations for finite local
rings.  P87's matrix is the sum of `A_u` over the nonzero socle, with the
isolated zero state removed.  The owner-subtracted claim is therefore the
symbolic theorem package for that union, not the invention or general spectral
theory of product matrices.
