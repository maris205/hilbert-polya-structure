# Algebra/arithmetic breadth scout and kill ledger

Date: 2026-09-03.  Scope: finite exact algebraic, arithmetic, finite-field,
matrix, module, and code dynamics outside the systems already used or killed
in P1--P166.

## Entry firewall

The most relevant occupied engines are P97 sumset squaring, P98 repeated-root
shift, P99 Hermite-normal-form shear, P100 least-valuation digit erasure, P102
norm/squaring, P103 adjugation, P107 annihilator-power ideals, P109 images of a
fixed nilpotent, P115 Cartier iteration, P119 Engel iteration, P124 cross-colon
ideals, P125 quadratic shear, P128 translation--GCD, P137 rank-feedback groups,
P142 valuation--GCD tents, P153 triangular factorial collapse, P154 subgroup
normalizers, P157 Newton--Hensel lifting, P165 support shortening, and P166
weight translation.  The permanent kill ledgers also exclude generic finite
linear/power maps, Jordan-power variants, derivative--GCD/radical stripping,
subspace products and Schur squares, normal closures/cores, matrix
Möbius--Drazin--Newton variants, and Euclidean/Hurwitz repackagings.

Two tempting systems were rejected **before** the count below.  The map
`x -> x + gcd(x,p^e)` is literally the AA03/GIO family and is conjugate to
P100's valuation-digit erasure.  Subspace Schur closure was already a permanent
subspace-product kill.  Neither is reported as new breadth.

## Exact breadth result

All signatures below are reproduced by `verify_scout.py`.  A small box is a
falsification probe, not a theorem.

| ID | Literal carrier and update | Exact pilot | Decision | Reason |
|---|---|---:|---|---|
| **QIS** | All `F_p`-subspaces of `F_{p^4}`; span the inverses of nonzero members | `p=2`: 67 states, depths `22/15/30`, cycles `1^4 2^9`, height 2 | **GREEN_OWNER_THIN** | Binary-only extra transient layer; exact all-prime theorem, zeta, full component shape, and all-time fibres.  Direct geometry/classification owners force explicit subtraction. |
| CIS | All codes `C <= F_5^3`; span the coordinatewise zero-totalized inverses of codewords | 64 states, 48 recurrent, height 1, 24 fixed and 12 two-cycles | KILL--NO_SHARP_SPINE | Dimension is monotone and equality gives a 1/2-cycle, but larger lengths already develop nonuniform tails; no exact all-length height or fibre atlas.  Strongly adjacent to inversion/subspace owners. |
| HSS | Binary length-6 codes; shorten on the support of `Hull(C)=C cap C^perp` | 2,825 states, height 2, 1,378 fixed, maximum fibre 443 | KILL--P165/NO_ATLAS | A hull diagnostic feeding support shortening is a P165 proof-engine reuse; pilots give no clean all-length law. |
| HSP | Binary length-6 codes; project every word away from the support of its hull | Same depth and fixed histograms as HSS, but maximum fibre 218 | KILL--SAME_CLOCK/NO_THEOREM | The literal update differs from HSS and its fibres differ, yet the clock repeats the same weak hull-support signal and has no independent formula. |
| EAF | Abelian `p`-group invariant-factor types of exponent at most 6 and rank at most 3; apply exterior square | 84 types, height 2, seven fixed | KILL--FUNCTOR-TAUTOLOGY | Iteration is a direct invariant-factor calculation; the bounded-rank clock has no separate inverse/fibre axis. |
| SQS | Symmetric inverse monoid `I_4`; square a partial bijection | 209 states, height 2, cycles `1^16 2^8` | KILL--GENERIC-POWER | This is a generic powering/root-count problem on a standard finite semigroup and reuses P102/P108-style exponent engines. |
| DFR | Subgroups of `D_16`; replace `H` by its Frattini subgroup `Phi(H)` | 19 states, height 3, only the trivial recurrent state | KILL--STANDARD-SERIES | The clock is the standard Frattini series; no new dynamical invariant or fibre theory. |
| DRS | Subgroups of `D_16`; replace `H` by `[H,H]` | 19 states, height 2, only the trivial recurrent state | KILL--STANDARD-SERIES | Direct derived-length repackaging, with thinner data than the original group invariant. |
| PLS | Subspaces of `F_2^5`; intersect with a fixed hyperplane and apply a nilpotent shift | 374 states, height 5, one recurrent state | KILL--P109/P160 | Fixed-flag truncation followed by a linear image is precisely the nilpotent-image/flag engine already occupied. |
| ARI | Subspaces of `F_2^5`; apply `N^{dim U}` to `U` | 374 states, height 5, image 23, maximum fibre 128 | KILL--P109+P137 | Literal hybrid, but its proof would only compose fixed nilpotent images with rank feedback. |
| DFM | `M_2(F_3)`; `A -> det(A) A` | 81 states, height 1, cycles `1^25 2^12` | KILL--RADIAL-POWER | Projective direction is frozen and only a scalar power recurrence remains; this is P102's scalar engine. |
| LFM | `F_5^3`; `v -> (sum_i v_i)v` | 125 states, height 2, 26 fixed | KILL--RADIAL-POWER | Again every orbit is a one-dimensional scalar recurrence; no genuinely matrix/module-level dynamics survives. |
| CSM | `GL_2(F_3)`; `A -> A^{-T}A` | 48 states, height 3, one fixed point and two 4-cycles | KILL--IRREGULAR/DIRECT-OWNER | Cross-prime pilots have irregular heights and periods; cosquares and congruence canonical forms are a mature direct owner area. |
| SAI | Ideals of `Z/p^12`; `I -> I^2 cap Ann(I)` | 13 states, height 2, image 5 | KILL--P107/P142 | On exponents the map is `a -> max(min(2a,e),e-a)`, a direct collision with annihilator-power and valuation tent engines. |
| DFF | A squarefree polynomial with one fixed irreducible factor of each degree `1,...,12`; keep factors whose degree divides the total degree | 4,096 states, height 4, 25 fixed | KILL--IRREGULAR-NO-SPINE | Heights for degree cutoff `m` jump irregularly (new records occur sparsely); no credible sharp parameter theorem, while Frobenius factor filters are direct. |
| PAF | Weight-4 binary abacus words of length 8; simultaneously move every available bead one step | 70 states, sharp pilot height 7 | KILL--RULE-184 | Strong clock but literally parallel TASEP/Rule 184 in abacus language, so it is a terminology change rather than a new system. |
| MFP | Pairs in `M_2(F_2)^2`; `(A,B)->(AB,A)` | 256 states, height 5, periods 1,2,3,6,8 | KILL--SEMIGROUP-WORD-IRREGULAR | Rich small graph, but no stable parameter signal; it is a semigroup word recurrence/product-exchange variant adjacent to P108. |

Count: **17 exact literal systems; one provisional survivor; 16 recorded
kills.**  Even deleting either of the closely related hull rows leaves at least
16 distinct literal updates.

## Why QIS alone crossed the gate

QIS gave all three requested axes at once.

1. **Sharp temporal/recurrent axis.**  The height is exactly two only at the
   binary base field and exactly one at every odd prime.  Every recurrent orbit
   has period at most two, with explicit counts and zeta function.
2. **Independent inverse/fibre axis.**  Every target has a closed `t`-step
   fibre formula.  In the binary case every hyperplane has exactly two plane
   predecessors at time one, an effect not determined merely by the height.
3. **Structural axis.**  The complete graph is a disjoint collection of bare
   fixed points/two-cycles plus one basin rooted at the full field.  Twisted
   Singer symmetry, `J(lambda A)=lambda^{-1}J(A)`, explains uniform binary
   hyperplane fibres.

The owner penalty is why the status is not a clean green light.  The dynamic
claims must be sold as a finite-graph synthesis built on explicitly credited
inverse-subspace geometry, not as a discovery of that geometry.
