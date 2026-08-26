# Paper 28 — Semiclassical Tensor-Power Trace

Working title: *Semiclassical Tensor-Power Trace*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0--A1**, with a
  non-credit semiclassical tensor-power architecture note.
- Concrete progress: the magnetic field and flux are normalized; the nonexistent
  global magnetic potential has been removed; classical phases are owned by a
  degree-one line-bundle connection and its holonomy; the operator family
  `H_N=Δ^{L^N}` on `L²(Σ_B,L^N)`, `N→∞`, is frozen; and the
  `b=0,+1/2,-1/2` controls are assigned base-bundle degrees `0,+1,-1`.
- Formal Route-A tuple: **unassigned**.  Route-B evaluation is not run and
  invocation is disallowed.

## Evidence-token contract

Mathematical and computational statements in this project use only the following
evidence tokens:

```text
PROVED
HEURISTIC
MODELING_CHOICE
OPEN
```

`FROZEN`, `NOT_RUN`, and the exact ownership state `NOT_ESTABLISHED` are
pipeline/design markers, not evidence tokens and not evidence that a theorem or
same-owner trace correspondence has been proved.

## Frozen dynamical system and semiclassical family

Let `(Sigma_B,g)` be the Bolza genus-2 surface with curvature `-1`.  Its area is
`4 pi`.  On `T*Sigma_B`, take

```text
F = b Omega_g,       b = 1/2,
omega_b = omega_0 + pi^*F,
H(x,p) = |p|^2/2,
energy shell H = 1/2.
```

With the frozen sign convention, unit-speed trajectories satisfy
`nabla_t dot(gamma)=b J dot(gamma)`.  The flux is

```text
(1/(2 pi)) integral_Sigma F = 2b = 1,
```

so `[PROVED]`: the positive-field base bundle `L` has degree `+1`.  Fix a
Hermitian connection on `L` compatible with the stated sign convention, and
freeze the semiclassical tensor-power family

```text
H_N = Δ^{L^N},
Hilbert_N = L²(Σ_B,L^N),
N = 1,2,...,       N→∞.
```

The operator and its Hilbert space change with `N`; this is not the high-energy
limit of one fixed operator.  The connection on `L` induces the connection on
`L^N`, and its orbit holonomy is raised to the `N`th power, but whether those
orbits own a selected trace of `H_N` remains `[OPEN]`; its exact pipeline state
is `NOT_ESTABLISHED` until a trace regime and energy-window scaling are fixed
and verified.

Since the flux is nonzero, `F` is not exact and no global one-form `A` with
`dA=F` exists.  Closed-orbit phases must therefore be written as connection
holonomy (or action modulo `2 pi`), not as one global
`integral_gamma A` for all orbits.

The degree-one operator `Δ^L` on `L²(Σ_B,L)` is retained only as a
separate fixed-operator candidate:

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
```

No conclusion for the `N→∞` tensor-power family is transferred to
this fixed candidate.

## Research question and bold hypothesis

Can a source-verified trace regime for the changing family
`H_N=Δ^{L^N}`, `N→∞`, bind primitive magnetic-orbit holonomy and
Maslov data strongly enough to distinguish the arithmetic Bolza metric from
topology-, flux-, and degree-matched controls?

`[HEURISTIC]`: the minimal nonzero flux may break zero-field time-reversal pairing
and expose phase structure tied to the arithmetic Bolza surface.  Arithmetic
provenance plus a natural quantum host does not establish a rational-prime
correspondence or a same-owner trace formula.

## First kill gate

Compare the following controls at common `N`, energy-window convention,
trace regime, normalization, and orbit-selection rule:

```text
b=0       -> degree  0, trivial base bundle and trivial connection;
b=+1/2    -> degree +1, base bundle L;
b=-1/2    -> degree -1, dual base bundle L^*.
```

For tensor power `N`, the corresponding operator bundles have degrees
`0,+N,-N`; the negative-field operator is
`Δ^{(L^*)^N}`.  Also compare a non-arithmetic genus-2 metric perturbation
with the same area, field, base-bundle degree, tensor power, and trace regime.
If phase cancellation is controlled only by topology or flux, A0 fails and the
result remains a magnetic trace calibration.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned owner/phase ledger](results/README.md)

No prime-orbit claim, fixed-spectrum match, same-owner trace correspondence, or
Route-B credit is claimed.
