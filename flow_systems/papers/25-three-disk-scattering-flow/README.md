# Paper 25 — three-disk scattering flow

Working title: *Generic Half-Density Is Not Arithmetic: A Three-Disk Scattering Control*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0 kill control**.
- Concrete progress: the exact no-eclipse geometry is frozen; the exact quantum
  multiple-scattering determinant is separated from the semiclassical
  Gutzwiller--Voros orbit expansion; the project is internally prespecified as
  the batch's non-arithmetic control.
- A0-source status: **`[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION`**.  This status
  follows from the frozen control design and does not depend on the numerical
  half-density experiment.
- Half-density control status: **`[OPEN]`**.  The word-length-at-most-12 ledger
  has not been executed, so `PROVES_TOO_MUCH` is a possible future control
  verdict, not a current result.  The formal Route-A tuple remains unassigned;
  Route-B evaluation is not run and invocation is disallowed.

## Frozen dynamical system

Take three disks of radius `a`, with centers at the vertices of an equilateral
triangle of side `d=6a`.  The primary object is the unit-speed exterior billiard
flow with specular reflection.  Its primitive objects are primitive oriented
cyclic disk words; the clock is physical Euclidean flight length.

The third center lies at distance `(sqrt(3)/2)d` from the line joining the other
two.  Thus the no-eclipse condition follows from

```text
(sqrt(3)/2)d > 2a,
```

and `d=6a` is safely inside the open hyperbolic regime.

## Research question and bold hypothesis

Can any target-free statistic of the primitive-orbit half-density distinguish
rational primes from matched random/composite controls after stability and
escape rate are frozen?

`[HEURISTIC]`: instability factors can mimic an envelope such
as `p^(-r/2)` without any arithmetic origin.  If so, amplitude resemblance is a
generic hyperbolic effect and the tested statistic must be classified
`[STOP_SCOPED] / PROVES_TOO_MUCH`.

The exact spectral surface is the multiple-scattering matrix determinant (or
exact `S`-matrix factorization).  A Gutzwiller--Voros zeta is used only as a
semiclassical curvature-expanded object, never as an exact determinant
identity.

## First kill gate

The internally prespecified test enumerates primitive words through topological
word length 12 at `d/a=5.8, 6.0, 6.2`, then compares shuffled periods, random
phases, matched-density integers, and composites.  Its execution status is
`[OPEN]`.  If an alleged arithmetic score persists across these controls, the
statistic receives `[STOP_SCOPED] / PROVES_TOO_MUCH`; otherwise that verdict is
not assigned.  Either outcome leaves the independently frozen A0-source absence
unchanged and cannot manufacture an arithmetic owner for this geometry.

Evidence labels in this project use the vocabulary of
`skills/route-a-evaluator.md`; assignment states such as `UNASSIGNED` and
`NOT_EVALUATED` are stage bookkeeping, not evidence tokens.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned ledger](results/README.md)

No numerical result or manuscript is claimed yet.
