# Paper 27 — congruence inverse-limit no-go

Working title: *No Periodic Orbits in a Residual Congruence-Limit Geodesic Flow*

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
arclength at every level.  Because the modular surfaces have cusps, the honest
name is a principal-congruence inverse-limit geodesic lamination, not a compact
McCord solenoid.

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
- [reproduction entry point](experiments/reproduce.sh)

The no-periodic-orbit theorem remains the Route-relevant landed result.  The
finite-level table is a reproducible diagnostic only; a full manuscript and
external novelty audit remain pending.
