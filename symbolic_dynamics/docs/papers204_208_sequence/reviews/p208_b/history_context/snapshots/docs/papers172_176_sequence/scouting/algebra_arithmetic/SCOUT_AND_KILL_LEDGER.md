# Algebra/arithmetic breadth scout and kill ledger

Date: 2026-09-03.  Scope: finite exact algebraic, arithmetic, finite-field,
finite-group, matrix, module, and code dynamics.  Status:
`EMPTY_GREEN_POOL / HOLD_EXTERNAL`.

The entry audit used the P1--P171 paper names, the P167--P171 historical
collision seed, and the current proof-silhouette firewall.  Fixed points,
tails, zeta functions, or the mere existence of a fibre formula do not earn
separation credit.  The decisive comparison is whether the literal update or
both proof engines transfer from an occupied system.

## Breadth count

The verifier contains 20 literal carriers and updates.  To avoid inflating the
count with disguises, this ledger identifies `A02/A19` as one generic
subspace-square class and `A07/A11` as one generic cyclic-power class.  The
remaining rows do not arise from changing only a parameter in another row.
The conservative total is therefore **18 distinct finite-dynamical-system
classes**, represented by 20 literal maps.

## Exact systems

| ID | Literal carrier and update | Early exact signal | Inverse/enumerative axis | Decision and reason |
|---|---|---|---|---|
| `A01` | all `F_q`-subspaces `U <= F_{q^m}`; `U -> U cap F(U)`, where `F(x)=x^q` | sharp height `m-1`; only fixed cycles; fixed count is the divisor count of `x^m-1`; e.g. `q=2,m=6`: 2,825 states, 9 fixed, depth histogram `9/1382/1062/300/48/24` | every target and time has an exact subspace-lattice Möbius formula; checked targetwise for binary `m<=5` and odd-prime controls | `KILL_INTERNAL_P110_P128`: this is the meet-dual of the semilattice orbit fold; the sliding intersection, invariant core, and Möbius inversion transfer from P110/P128 |
| `A02` | `F_2`-subspaces of `F_{2^m}` containing `1`; `U -> span(UU)` | fixed states are the subfields; pilot maximum tails for `m=2,...,6` are `0,1,2,2,3` | terminal-subfield basin counts, e.g. dimensions `1,2,3,6` receive `1,1,4,368` states at `m=6` | `KILL_INTERNAL_P97`: permanent subspace-product/Schur-square closure kill; shares class with `A19` |
| `A03` | monic `f in F_q[x]`, `deg f<=n`; `f -> gcd(f,f')` | factor exponent `e` maps to `e-1` unless `p|e`, when it freezes; exact height `min(n,p-1)` | factor-degree Euler products give every depth CDF and every target's time-`t` fibre | `KILL_DIRECT_OWNER_REPEAT`: exact prior rows in P127, P152, P157, and P162; derivative--GCD is the classical square-free-decomposition primitive |
| `A04` | the additive group of `F_{p^m}` in a normal basis; `x -> x^p-x` | `p=2,m=8` is nilpotent of height 8, whereas `p=2,m=5` has a 15-cycle; all behavior follows the rational form of `F-I` | every nonempty fibre of an iterate of this linear map is a kernel coset | `KILL_GENERIC_LINEAR`: Artin--Schreier linear algebra, with the same Jordan/kernel-coset engine excluded around P109/P115 |
| `A05` | polynomials of degree at most `d` over `F_p`; `f -> f(x+1)-f(x)` | `Delta^p=0`; the pilot heights are 2, 3, and 4 in `(p,d)=(2,7),(3,5),(5,3)` | all nonempty iterate fibres are uniform affine kernel cosets | `KILL_GENERIC_LINEAR`: a nilpotent linear operator and finite-difference/Jordan calculation, not an independent inverse system |
| `A06` | `F_p^m`; `x -> ell(x)x` for the normal-basis trace functional `ell` | radial direction freezes and the scalar follows a one-variable power recurrence; `p=5,m=3` has 26 fixed states and height 2 | fibres split into trace hyperplanes and one-dimensional scalar equations | `KILL_DIRECT_REPEAT`: this is the `LFM` literal map already killed in the P167--P171 algebra scout, and its scalar engine is P102-like |
| `A07` | `F_{q^m}`; `x -> N_{F_{q^m}/F_q}(x)x` | exactly the power map `x -> x^(1+(q^m-1)/(q-1))`; examples are bijective, idempotent, or mixed according to one gcd | cyclic congruence counts give all iterated fibres | `KILL_GENERIC_POWER`: no norm geometry remains after exponent reduction; counted with `A11` as one class |
| `A08` | additive cyclic group `Z/NZ`; `j -> rad(ord(j))j` | every active prime-adic valuation rises by one; unique fixed state and sharp height `max_p v_p(N)` | primewise product formulas give depth layers and predecessors | `KILL_INTERNAL_P100_P142`: coordinate valuation erosion/raising is the occupied digit-erasure and valuation-atlas engine |
| `A09` | ideals of `Z/NZ`, in CRT exponent coordinates `0<=a_i<=e_i`; `I -> I+Ann(I)`, i.e. `a_i -> min(a_i,e_i-a_i)` | idempotent; for exponent box `(3,4,2)`, 60 states collapse onto 12 fixed states | fibres are independent two-branch coordinate choices | `KILL_INTERNAL_P107_P142`: a one-step annihilator/valuation projection with no temporal residual |
| `A10` | residue ring `Z/p^kZ`; `x -> x^2` | combines valuation doubling on nonunits with group powering on units; e.g. modulo `3^5`, 82 recurrent states and height 3 | CRT and cyclic-unit root counts determine predecessors | `KILL_GENERIC_POWER_P102`: classical ring-power functional graph; neither axis escapes the occupied power/valuation engines |
| `A11` | `F_{q^m}`; Lang power `x -> x^(q-1)` with zero fixed | a cyclic multiplication map on exponents; `q=3,m=4` has height 4 and one nontrivial 4-cycle | linear congruences modulo `q^m-1` give every iterate fibre | `KILL_GENERIC_POWER`: same generic class as `A07`, with no separate Lang residual |
| `A12` | monic polynomials with nonzero constant term; `f -> gcd(f,f*)`, with monic reciprocal `f*` | idempotent reciprocal-core projection; `p=3,n=5` has 243 states and 43 fixed images | factor-orbit choices give static fibres | `KILL_SHALLOW_DUALITY`: mature reciprocal-factor pairing plus a one-step projection; no clock |
| `A13` | all subsets `A` of `C_n`; `A -> Stab_{C_n}(A)`, returned as a subset | idempotent; only 4 images among 1,024 states at `n=10` | exact-stabilizer subset counts are divisor Möbius/necklace counts | `KILL_SHALLOW_STABILIZER`: a static group-action invariant, not a two-axis dynamical system |
| `A14` | all subsets `A` of `C_n`; `A -> <A>` | idempotent; at `n=16`, 65,536 states have only 5 images | generating-subset fibres follow subgroup-lattice Möbius inversion | `KILL_SHALLOW_GENERATION`: static subgroup generation with no temporal axis; literal update differs from `A13` |
| `A15` | strict upper-triangular matrices over `F_2`; `A -> A^2` | unique absorber and sharp logarithmic nilpotence clock; `n=5` gives height 3 | matrix-root fibres already become rank/Jordan counting | `KILL_GENERIC_MATRIX_POWER`: a matrix-power/Jordan specialization of the P102 power engine and an earlier permanent kill |
| `A16` | `S_n`; `g -> g^{-1}(12)g(12)` | image has `C(n,2)` states, exactly `2n-3` fixed points, no other cycles, and sharp height 2 | every image fibre has size `2(n-2)!`; a closed fixed-point-marked fibre polynomial depends only on support overlap `r=0,1,2` | `KILL_INTERNAL_P119_TRANSFER`: same fixed-element commutator and centralizer-coset fibre engine; the support mark is real but paper-thin, and Fulman 2024 is close externally |
| `A17` | all subspaces of the Lie algebra of strict `4x4` upper-triangular binary matrices; `U -> U+[U,U]` | 2,825 states, 369 Lie-subalgebra fixed states, sharp pilot height 2 | maximum one-step fibre is 761, but no stable all-rank atlas emerges | `KILL_INTERNAL_P97`: binary-operation subspace closure is the same closure engine as subspace/Schur squaring, without an independent fibre theorem |
| `A18` | all subspaces of a symplectic `F_2`-space; `U -> rad(U)=U cap U^perp` | idempotent; dimension 6 has 2,825 states and 514 totally isotropic fixed images | fibres reduce to formed-space incidence enumeration | `KILL_SHALLOW_POLAR`: a one-step radical projection in a mature finite-polar-space setting |
| `A19` | binary codes containing the all-one word; `C -> span{u*v:u,v in C}` | expansive Schur-square closure; lengths 5 and 6 already have 52 and 203 fixed codes | code-power predecessor enumeration is the only second question | `KILL_DIRECT_OWNER_P97`: permanent Schur-power-code kill; counted with `A02` as one generic class |
| `A20` | all subspaces of `F_2^m`, with `N` one nilpotent Jordan block; `U -> U+N(U)` | `T^t(U)=U+NU+...+N^tU`; sharp height `m-1`; at `m=6`, depth histogram `7/1363/1146/225/52/32` | terminal invariant-subspace basins invite lattice Möbius inversion | `KILL_DIRECT_SCOUT_REPEAT`: this literal map was already pressure-tested and killed in P107--P111; it also transfers the P109/P110 flag-orbit closure engine |

## Why the three clean formulas still fail the gate

`A03` and `A16` demonstrate why mathematical cleanliness is not enough.
`A03` closes both axes perfectly, but is a literal and theorem-package repeat.
`A16` adds a new marking variable, but conditioning a centralizer coset by
ordinary fixed points reduces to a two-piece partial-rencontres calculation;
it does not replace either occupied proof engine.  `A01` is the best fresh
literal carrier in this lane, yet its complete formula is obtained by the
generic semilattice iterate identity followed by the same Möbius inversion
used in P110/P128.

## Recommendation

There is no green or owner-thin recommendation.  If a later coordinator wants
one negative control to revisit under a changed collision policy, `A01` is the
only one worth reopening.  Under the present P1--P171 firewall it should not
receive a paper number.

The exact transcript ends with 419,496 assertions and `RESULT=PASS`.  Those
bounded checks are reproducibility and falsification evidence only.
