# Paper 27 — congruence inverse-limit no-go

Working title: *Finite-Level Closed Geodesics without Inverse-Limit Periodic
Orbits: an Explicit Congruence-Tower Ownership Audit*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0--A1**.
- Concrete mathematical result: for the frozen residual principal-congruence
  tower, the coordinatewise continuous-time geodesic flow on the inverse limit
  has **no periodic points**.
- Local progress tag: **`[PROVED] PROVED_A1_OBSTRUCTION`** for the inverse-limit
  flow itself.  This is an informal Route-A mapping, not a formal evaluator
  verdict.  Informally, the congruence-tower provenance is `[PROVED]`, while an
  intrinsic rational-prime link is `[OPEN]`.  The formal `(A0,A1,A2,A3,A4)`
  tuple and overall Route-A status are unassigned; A2--A4 are `NOT_EVALUATED`,
  Route-B evaluation is not run, invocation is disallowed, and Gates A--E are
  not reached.

- Round-3 closest-prior audit: **COMPLETE, SEARCH-BOUNDED**.  Direct structural
  prior work was found, so the theorem is not being positioned as a new general
  aperiodicity theorem.  The candidate contribution is narrowed to the explicit
  `Gamma(3 n!)` specialization, its sign-sensitive residual proof, the
  reproducible finite-level order ledger, and the finite-owner firewall.
- Round-4 theorem: **`[PROVED]` period escape**.  In any descending normal
  finite-index tower with trivial intersection, the finite-quotient orders of
  every infinite-order element divide forward and tend to infinity.  Hence the
  whole-`g`-loop closing times of every fixed hyperbolic owner escape to
  infinity.  This is the minimal time among whole traversals of the selected
  `g`-loop; without a conjugacy-primitivity proof it is not called the
  underlying flow orbit's minimal period.  The 24 frozen rows validate the
  finite prefix; they do not prove the asymptotic theorem.

### Round-4 period-escape result — 2026-08-27

For `o_n=ord(g Gamma_n)` in `Gamma_1/Gamma_n`, normal tower maps give
`o_n | o_(n+1)`.  If this sequence were bounded, it would be eventually
constant, forcing a positive power of the infinite-order element `g` into
`intersection_n Gamma_n={e}`.  This contradiction proves `o_n -> infinity`
and therefore the whole-`g`-loop closing time `o_n ell(g) -> infinity` for
hyperbolic lifts.

The exact specialization applies to `Gamma(3 n!)`.  The executable audit
rechecks all 21 divisibility transitions for the three frozen elements; their
last-to-first order growth factors are `288`, `2880`, and `576`.  The theorem
strengthens the finite-owner firewall without reviving a general novelty claim.
See the [Round-4 theorem](notes/round4_period_escape_theorem.md).

### Round-3 closest-prior result — 2026-08-27

The strongest prior-work overlap is substantive:

- Martínez--Matsumoto--Verjovsky (2016) give a compact hyperbolic lamination
  example without periodic geodesic orbits and separately describe the
  universal hyperbolic solenoid as an inverse limit with simply connected
  leaves.
- Penner--Šarić (2008) define the noncompact punctured solenoid as the inverse
  limit over finite-index subgroups of `PSL_2(Z)` and state that its leaves
  are unit disks.
- Alcalde Cuesta--Carballido Costas--Martínez--Verjovsky (2026) treat exactly
  the object class of noncompact finite-area surface-covering inverse limits,
  call the regular-cover case a hyperbolic McCord solenoidal surface of finite
  type, and define its leafwise geodesic flow.

No checked primary source stated the exact factorial-chain proposition
`Gamma(3 n!)` verbatim.  That negative search result is bounded by the
recorded strings and sources; it is not an absolute novelty claim.  In light of
the direct structural prior, the no-period theorem is treated as an explicit
specialization/case study rather than a standalone new general theorem.  See
the [Round-3 source audit](notes/round3_closest_prior_audit.md), [Round-3
conclusion](notes/round3_conclusion.md), and [Stage-1 research
spine](paper/stage1_research_spine.md).

### Round-2 finite-level diagnostic — 2026-08-27

The prespecified eight moduli `3,6,18,72,360,2160,15120,120960` have now
been executed for three frozen hyperbolic elements of `Gamma(3)`.  The landed
ledger has 24 rows.  Every projective reduction order was computed by both
sequential matrix multiplication and an independent finite-group-bound factor
reduction; all `24/24` pairs agree.  The observed order sequences are

```text
G3-A: 1,3,3,6,6,36,72,288
G3-B: 1,1,3,12,60,360,360,2880
G3-C: 1,2,6,12,12,72,72,576
```

These are `[NUMERICALLY_CERTIFIED]` finite-quotient diagnostics.  Their owner
is the frozen congruence tower plus the three matrices, not the inverse-limit
flow.  Consequently they do not weaken or compensate for the `[PROVED]`
identity `Per(M_infinity)=empty`, and they receive no formal A1/A2 credit for
that flow.  Positive-word primitivity is checked exactly, while primitivity as
a full `Gamma(3)` conjugacy class remains `[OPEN]` because it is unnecessary
for the reduction-order diagnostic.

## Frozen dynamical system

For `n>=1`, let

```text
Gamma_n = Gamma(3 n!) < PSL_2(Z),
Y_n = Gamma_n \ H,
M_infinity = inverse_limit_n T^1Y_n.
```

The bonding maps are the finite covering maps, and the flow is defined
coordinatewise by the unit-speed geodesic flows.  The clock is hyperbolic
arclength at every level.  In the terminology of Alcalde Cuesta et al. (2026),
this normal regular-cover tower is a noncompact hyperbolic McCord solenoidal
surface of finite type.  It is not the compact universal hyperbolic solenoid;
`principal-congruence inverse-limit geodesic lamination` remains an
unambiguous project-local description.

## Stage-1 no-go theorem

Write the level-`n` coordinate as `Gamma_n h_n`.  Compatibility with the first
coordinate gives `h_n=eta_n h_1` for some `eta_n in Gamma_1`.  If the first
projection has primitive hyperbolic representative `gamma` and primitive length
`ell(gamma)`, then a common period has `T=m ell(gamma)` and

```text
h_n a_T h_n^{-1} = eta_n gamma^m eta_n^{-1}.
```

The level-`n` lift returns after `T` exactly when this element lies in
`Gamma_n`.  Since every `Gamma_n=Gamma(3 n!)` is normal in `Gamma_1`, this is
equivalent to `gamma^m in Gamma_n`.  Hence a compatible periodic point would
force `gamma^m` into every level.

For completeness, if `[A] in PSL_2(Z)` belongs to every `Gamma(3 n!)`, choose
`A in SL_2(Z)`.  For each `n` there is a sign `epsilon_n` with
`A = epsilon_n I mod 3 n!`.  Reducing the level `n+1` congruence modulo `3 n!`
shows the signs agree, because `3 n!` never divides `2`.  All entries of
`A-epsilon I` are therefore divisible by the unbounded sequence `3 n!`, so
`A=epsilon I` and `[A]=1`.  Thus

```text
intersection_n Gamma(3 n!) = {1},
```

so `gamma^m=1`, contradicting hyperbolicity.  Therefore

```text
Per(M_infinity) = empty.
```

This proves `Per(M_infinity)=empty` and establishes the local progress tag
`[PROVED] PROVED_A1_OBSTRUCTION`.  It does not by itself assign a formal A1
verdict or overall Route-A status.  Finite-level zeta functions may still have a
renormalized projective limit, but that would be a different owner and must be
labeled separately.

## Bold residual hypothesis and kill gate

`[HEURISTIC]`: normalized finite-level trace/zeta data may retain local congruence
splitting information.  The kill gate is owner identity: if the proposed
analytic object is not defined by primitive orbits of `M_infinity`, it cannot
receive A1/A2 credit for the limit flow.

Evidence labels follow `skills/route-a-evaluator.md`.  `PROVED_A1_OBSTRUCTION`
is a local progress tag; `UNASSIGNED` and `NOT_EVALUATED` are stage states, not
formal evidence tokens.

## Files

- [Stage-1 theorem brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned finite-level diagnostic](results/README.md)
- [Round-2 conclusion and owner firewall](notes/round2_conclusion.md)
- [Round-3 closest-prior audit](notes/round3_closest_prior_audit.md)
- [Round-3 conclusion](notes/round3_conclusion.md)
- [Round-4 period-escape theorem](notes/round4_period_escape_theorem.md)
- [Round-4 reproducibility receipt](experiments/round4_reproducibility_receipt.json)
- [Stage-1 paper research spine](paper/stage1_research_spine.md)
- [reproduction entry point](experiments/reproduce.sh)

The no-periodic-orbit theorem remains the Route-relevant landed result.  The
finite-level table is a reproducible diagnostic only.  The external
closest-prior audit is complete and narrows the publishable claim; a manuscript
has not been started and ARS Stage 2 has not begun.
