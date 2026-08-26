# Paper 24 — Bianchi holonomy flow

Working title: *Complex Lengths and Holonomy-Twisted Orbit Traces on a Bianchi Flow*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0--A1**.
- Concrete progress: the phase space is frozen to a torsion-free, finite-volume
  cusped Bianchi 3-manifold; level-`(3)` neatness and torsion-freeness now have a
  self-contained proof; the complex-length and zeta conventions are fixed;
  cusp/scattering terms and the first falsification control are explicit.
- Primary arithmetic target: **Dedekind-zeta calibration for `Q(i)`**.  This does
  not confer Riemann-`zeta` A0 credit.
- Formal Route-A tuple: **unassigned**.
- Route B: `EVALUATION=NOT_RUN`; `INVOCATION_ALLOWED=false`.

## Frozen dynamical system

Let `Gamma((3))` be the principal congruence subgroup of
`SL_2(Z[i])` at the ideal `(3)`, projected to `PSL_2(C)`, and set

```text
X = Gamma((3)) \ H^3,
M = T^1 X,
flow = unit-speed geodesic flow,
clock = hyperbolic arclength.
```

Primitive objects are primitive loxodromic conjugacy classes.  Their intrinsic
data are the complex lengths `L_p = ell_p + i theta_p`, with orientation and
repetition recorded.  The level choice avoids silently applying manifold
formulae to the elliptic-torsion Bianchi orbifold, but `X` remains noncompact
with cusps.

The background scalar Selberg convention to be tested is

```text
Z(s) = product_p product_{m,n>=0}
       (1 - exp(-(s+1+m+n) ell_p) exp(i(m-n) theta_p)).
```

The `s+1` shift is convention-dependent and is frozen here; any reparameterized
formula must document the change.  A cusp-aware analytic formula must include
continuous-spectrum/scattering contributions.

## Frozen arithmetic owner

The primary calibration target is

```text
zeta_{Q(i)}(s) = product_{prime ideals pfrak}
                 (1 - Norm(pfrak)^(-s))^(-1).
```

Primitive arithmetic owners are Gaussian prime ideals, and repetitions are
their powers before any rational-norm push-forward.  Consequently, even an
exact primary calibration would concern `zeta_{Q(i)}`, not automatically the
Riemann zeta function.

A rational-prime push-forward is a separate secondary target with the following
rules frozen in advance:

```text
p = 2:          ramified, (2) = unit * (1+i)^2, one owner of norm 2;
p = 1 mod 4:    split, two distinct owners of norm p;
p = 3 mod 4:    inert, one owner of norm p^2.
```

The corresponding Dedekind local factors are respectively
`(1-2^(-s))^(-1)`, `(1-p^(-s))^(-2)`, and `(1-p^(-2s))^(-1)`.  The two split
owners, inert norm, ramification index, and prime-ideal repetitions may not be
silently collapsed.  A canonical orbit-to-rational-prime map with the correct
multiplicities remains `OPEN`.

## Research question and bold hypothesis

Can the holonomy-twisted primitive-orbit distribution of this arithmetic
geodesic flow generate a `Q(i)` prime-ideal Euler ledger without attaching
prime-ideal labels to closed geodesics?

`HEURISTIC`: the Bianchi arithmetic substrate and complex holonomy may support
a Hecke-equivariant prime-ideal factorization.  No canonical orbit-to-prime-ideal
map is currently proved.  The secondary rational-prime push-forward has the
additional split/inert/ramified ownership obligation above, so neither target is
an A0 or A1 pass.

## First kill gate

Keep every `ell_p` and repetition relation fixed but shuffle the holonomy angles
`theta_p`; also compare a matched non-arithmetic Kleinian ledger.  If the same
phase/correlation margin survives, holonomy is only a generic phase compiler
and the arithmetic hypothesis stops.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned ledger](results/README.md)

No manuscript, numerical result, Route advancement, or quantum claim is made
at this checkpoint.
