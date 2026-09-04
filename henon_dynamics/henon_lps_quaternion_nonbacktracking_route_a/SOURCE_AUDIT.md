# Source audit

## Verified external inputs

The LPS article and DOI metadata were verified against the publisher record.
The Hashimoto chapter metadata and DOI were verified against the publisher
record.  The Bass DOI was checked against its journal record.  The
Kotani--Sunada article was checked on the University of Tokyo journal site,
which supplies the full article and its pages.  The Davenport book and DOI
were checked against the Springer record; it is the source used for the
prime number theorem in arithmetic progressions.

Three substantial external inputs enter the proof:

1. LPS connectedness plus the Ramanujan bound for the explicit quaternionic
   congruence graph.
2. The Bass--Hashimoto determinant/Euler-product identity for finite graphs.
3. The prime number theorem for arithmetic progressions, used only for the
   natural density of the four reduced residue classes modulo 20.

Quadratic reciprocity, finite group orders, and the simplicity of
`PSL2(F_q)` are used in their standard classical forms.

## Package-owned derivation

C375 explicitly derives the norm/determinant and inverse-pair identities,
the square-root gauge conjugacy, exact chamber sizes, determinant-character
bipartition, `PSL2` nonbipartiteness, complete quadratic spectral mapping,
Ramanujan-circle consequence, all-iterate trace convention, Möbius primitive
cycle formula, and conditional half--half chamber density.

The executable evidence builds all five finite groups without a group
database, checks every right translation, independently rebuilds them with
a different projective normalization and left action, and cross-checks the
trace polynomial symbolically.

## Evidence boundary

The five finite graphs and 1,124-prime chamber ledger are implementation
receipts.  They do not prove the cited LPS theorem, its all-prime scope, or
the prime-number-theorem density.  No finite eigenvalue fit is used to infer
the Ramanujan bound.

The exact primitive-cycle ledger is likewise source-local.  It does not
transport `q` or primality onto individual cycles, produce an intrinsic
`log p`/von Mangoldt weight, or execute the mandatory shuffled-period,
random-weight, random-phase, same-density-length, neighboring-parameter, and
simpler-parent controls at the A1 orbit-correspondence layer.  Exact
wrong-residue-prime, matched-composite, and cyclic chamber-label-shuffle
controls are executed at A0; they do not fill those A1 gaps.  This is why the
strict evaluator records `A1_WEAK` and `ROUTE_A_EXPLORATORY`.

## Collision audit

The nearest owner is HCS-C329.  It already owns the generic
Bass/Ihara/Hashimoto identity, so C375 does not count that identity by itself
as a new result.  The distinct owner is the joint theorem for the norm-five
LPS congruence family: explicit quaternion generators, arithmetic
`PSL2/PGL2` split, bipartite wall, exact finite sizes, LPS-to-Hashimoto
spectral circle, every-iterate dynamics, and gauge-locked evidence.

A repository-wide collision scan found no prior `LPS` package.  This is a
bounded workspace statement, not a claim of global scholarly novelty.
