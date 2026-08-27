# P27 Stage-1 theorem brief

## Research question

Can a residual principal-congruence inverse limit of modular geodesic flows own
a primitive/repetition ledger, or does compatibility across all finite covers
erase every periodic orbit?

## Object freeze

- Tower: `Gamma_n=Gamma(3 n!)`, a nested normal residual tower in
  `PSL_2(Z)`.
- Level spaces: noncompact finite-area modular surfaces `Y_n`.
- Limit phase space: inverse limit of `T^1Y_n` under finite coverings.
- Flow: coordinatewise unit-speed geodesic flow.
- Clock: common hyperbolic arclength.
- Candidate primitive object: a point periodic under one common real time at
  every level, not merely a sequence of unrelated finite-level closed orbits.

## Proposition — total-space periodic-orbit erasure

**Claim.** The inverse-limit flow has no periodic point.

**Proof.** Put `G=PSL_2(R)` and identify
`T^1Y_n=Gamma_n\G`, with geodesic flow given by right multiplication by
`a_t`.  Let `x=(x_n)` and suppose `g^T x=x` for `T>0`.  Choose representatives
`x_n=Gamma_n h_n`.  Compatibility under the covering to level 1 means
`Gamma_1 h_n=Gamma_1 h_1`, hence

```text
h_n=eta_n h_1 for some eta_n in Gamma_1.
```

At level 1 the orbit is a closed geodesic.  Choose its primitive hyperbolic
representative `gamma in Gamma_1` and orient it so that
`h_1 a_ell(gamma) h_1^{-1}=gamma`.  Then `T=m ell(gamma)` for some integer
`m>=1`.  The level-`n` lift returns after this same time precisely when

```text
h_n a_T h_n^{-1}
  = eta_n gamma^m eta_n^{-1}
  lies in Gamma_n.
```

Each `Gamma_n=Gamma(3 n!)` is the kernel of a reduction homomorphism from
`PSL_2(Z)` and is therefore normal in `PSL_2(Z)`, hence in `Gamma_1`.
Consequently

```text
eta_n gamma^m eta_n^{-1} in Gamma_n
if and only if gamma^m in Gamma_n.
```

Thus compatibility of the single inverse-limit point, together with one common
flow time `T`, forces `gamma^m` to lie in `intersection_n Gamma_n`.

It remains to verify the intersection inside `PSL_2(Z)`, where signs matter.
Let `[A]` lie in every `Gamma(3 n!)` and choose `A in SL_2(Z)`.  Membership
means that for every `n` there is `epsilon_n in {+1,-1}` such that

```text
A is congruent to epsilon_n I modulo 3 n!.
```

Because `3 n!` divides `3 (n+1)!`, reducing the `(n+1)`st congruence modulo
`3 n!` gives `(epsilon_{n+1}-epsilon_n)I=0 mod 3 n!`.  Since `3 n!>=3` cannot
divide `2`, the signs are constant.  Every integer entry of
`A-epsilon I` is then divisible by the unbounded sequence `3 n!`, so
`A=epsilon I`.  Therefore `[A]=1` and

```text
intersection_n Gamma(3 n!) = {1} in PSL_2(Z).
```

It follows that `gamma^m=1`, impossible for a hyperbolic element.  Hence the
inverse-limit flow has no periodic point.  QED.

## Consequence and ownership boundary

- `[PROVED]`: `Per(M_infinity)=empty`.
- Local theorem-progress tag: `[PROVED] PROVED_A1_OBSTRUCTION`.
- Informal A0 mapping: `[PROVED]` the frozen tower has principal-congruence
  arithmetic provenance; `[OPEN]` whether it supplies the required intrinsic
  rational-prime or prime-power link.
- Informal Route-A mapping: the inverse-limit flow has no primitive periodic
  objects from which to build its own A1 ledger.  This is not yet a formal A1
  evaluator verdict.
- Finite-level closed orbits and reduction orders exist, but their normalized
  projective statistic is not a periodic-orbit zeta owned by the limit flow.
- Noncompactness prevents importing compact inverse-limit conclusions without
  a separate proof.

## Residual hypothesis

`[HEURISTIC]`: a renormalized finite-level distribution could retain local
congruence splitting.  Its owner would be the tower plus normalization, not the
limit flow's nonexistent primitive orbit set.

## Target-free controls

1. Compare the real tower with a trivial product flow carrying the same Haar
   fiber.
2. Keep finite-level reduction orders separate from total-space periods.
3. Repeat the no-go argument for a cocompact residual arithmetic tower to test
   whether cusps are irrelevant to periodic-orbit erasure.
4. Prohibit inherited Route credit from the Deninger packet or base modular
   Selberg zeta.

## Route mapping

```text
PROPOSAL_STAGE=1
A0_INFORMAL_MAPPING=ARITHMETIC_PROVENANCE_PRESENT_PRIME_LINK_OPEN
A0_ARITHMETIC_PROVENANCE_EVIDENCE=PROVED
A0_PRIME_LINK_EVIDENCE=OPEN
A1_LOCAL_PROGRESS_EVIDENCE=PROVED
A1_LOCAL_PROGRESS_TAG=PROVED_A1_OBSTRUCTION
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2=NOT_EVALUATED
A3=NOT_EVALUATED
A4=NOT_EVALUATED
OVERALL_ROUTE_A_STATUS=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The bracketed evidence tokens in this brief are restricted to `PROVED`,
`HEURISTIC`, `MODELING_CHOICE`, and `OPEN`, as defined by
`skills/route-a-evaluator.md`.  `PROVED_A1_OBSTRUCTION` is a local progress tag;
`UNASSIGNED` and `NOT_EVALUATED` are stage states.

## Primary sources checked on 2026-08-26

- McCord, *Inverse limit sequences with covering maps*,
  https://doi.org/10.1090/S0002-9947-1965-0173237-0.  Supports the classical
  inverse-limit covering framework; its compact-manifold conclusions are not
  silently applied to the noncompact modular tower.
- Odden, *The baseleaf preserving mapping class group of the universal
  hyperbolic solenoid*, https://doi.org/10.1090/S0002-9947-04-03472-5.
  Supports the inverse-limit hyperbolic-solenoid comparison for closed surfaces.
- Martinez, Matsumoto, and Verjovsky, *Horocycle flows for laminations by
  hyperbolic Riemann surfaces and Hedlund's theorem*,
  https://doi.org/10.3934/jmd.2016.10.113 and
  https://arxiv.org/abs/0711.2307.  Supports unit-tangent flows on hyperbolic
  laminations and the need to track the leaf/limit-space topology.

The proposition above is derived in this brief; the sources validate the
framework, not the claimed novelty.

## Round-2 addendum — finite reduction orders (2026-08-27)

The previously registered eight-level table has been executed for three
pre-frozen hyperbolic `Gamma(3)` matrices.  The projective order convention is
`A ~ -A` in `PSL_2(Z/qZ)`.  Direct sequential multiplication and a separate
group-order-bound factor reduction agree in all 24 matrix/modulus cases.  The
order sequences are

```text
G3-A = [1,3,3,6,6,36,72,288]
G3-B = [1,1,3,12,60,360,360,2880]
G3-C = [1,2,6,12,12,72,72,576].
```

This gives `[NUMERICALLY_CERTIFIED]` finite-quotient order and period-scaling
data.  It is not evidence for a periodic point of `M_infinity`: each finite
order supplies a level-dependent closing multiple, while a periodic point of
the inverse limit would require one fixed positive time at every level.  The
owner field in all 24 rows is therefore
`FINITE_CONGRUENCE_TOWER_REDUCTION_DIAGNOSTIC`, and the corresponding
inverse-limit-flow credit is explicitly `FORBIDDEN`.

The matrices are exact `Gamma(3)` members and their positive words are
primitive necklaces.  Full conjugacy-class primitivity in `Gamma(3)` remains
`[OPEN]`; no claim in the finite-order table needs that stronger statement.
No prime table, Riemann-zero data, fitted clock, or target statistic was used.
The formal Route-A tuple remains `UNASSIGNED`: the Round-2 table closes a
finite-level diagnostic, not the missing rational-prime A0 link or a
determinant convention for A2.  A2--A4 remain `NOT_EVALUATED`, Route B remains
not run, and Gates A--E remain not reached.

## Round-3 prior-work positioning addendum — 2026-08-27

The search-bounded closest-prior audit found direct structural overlap.  In
particular, prior primary work supplies examples of hyperbolic laminated
geodesic flows without periodic orbits, describes universal and punctured
solenoids with simply connected disk leaves, and treats noncompact finite-area
inverse limits of regular surface coverings as hyperbolic McCord solenoidal
surfaces of finite type.  Those results do not state the exact
`Gamma(3 n!)` proposition verbatim, but they make the broad aperiodicity
phenomenon and its simply-connected-leaf mechanism prior.

Accordingly, this brief does **not** claim that
`Per(M_infinity)=empty` is a standalone novel general theorem.  Its proposed
paper role is an explicit, sign-sensitive principal-congruence specialization
paired with a reproducible finite-level ledger and a same-owner firewall.  The
full search protocol, exact links, source locators, include/exclude record, and
bounded novelty judgment are in
`notes/round3_closest_prior_audit.md`.  The non-prose Stage-1 manuscript plan
is in `paper/stage1_research_spine.md`.  ARS Stage 2 remains not started.
