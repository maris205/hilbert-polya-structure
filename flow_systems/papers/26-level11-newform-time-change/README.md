# Paper 26 — level-11 newform time change

Working title: *Level-11 Newform Periods as an Intrinsic Time Change of a Geodesic Flow*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0--A1**.
- Concrete progress: the arithmetic one-form, positive time-density/slowness
  factor, reciprocal speed multiplier, generator, and exact period-variation
  formula are frozen.  The earlier “modular-symbol time change” wording was
  narrowed because closed-geodesic periods are homology pairings, not
  automatically standard Manin cusp-to-cusp symbols.
- Formal Route-A tuple: **unassigned**.
- Route B: `EVALUATION=NOT_RUN`; `INVOCATION_ALLOWED=false`.

## Frozen dynamical system

Let `Y_0(11)=Gamma_0(11)\H`, let `X_geo` be its unit-speed geodesic vector
field, and take the normalized weight-2 newform

```text
f(z) = eta(z)^2 eta(11z)^2 = q - 2q^2 - q^3 + ... .
```

Define `omega_f=2 pi i f(z) dz`, `alpha_f=Re(omega_f)`, and on `T^1Y_0(11)`
put `a(v)=alpha_f(v)`.  For

```text
rho_epsilon(v) = 1 + epsilon a(v),
X_epsilon = X_geo / rho_epsilon,
```

Here `rho_epsilon` is the time-density/slowness factor, not the speed.  The
speed multiplier relative to `X_geo` is `1/rho_epsilon`.  The cusp-form decay
makes `a` bounded.  The frozen positivity interval is
`|epsilon| < ||a||_infinity^(-1)`.  For an original closed geodesic `gamma`,

```text
T_epsilon(gamma) = ell(gamma) + epsilon integral_gamma alpha_f,
T_epsilon(gamma^r) = r T_epsilon(gamma).
```

Writing `rho X` instead would change the period law and is not this candidate.

## Research question and bold hypothesis

Can the first derivative of the time-changed dynamical zeta be decomposed into
Hecke/Euler factors using only the same primitive-geodesic ledger?

`HEURISTIC`: newform periods along primitive closed geodesics may satisfy a
useful Hecke recurrence.  They are not known to equal Hecke eigenvalues `a_p`,
and no primitive orbit-to-prime correspondence is assumed.

## First kill gate

Replace `alpha_f` by a norm-matched generic smooth bounded observable and, in a
separate control, permute the newform periods among primitive orbits.  If an
Euler-factor score survives or no exact Hecke recurrence can be derived without
prime labels, stop the arithmetic interpretation.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned variation ledger](results/README.md)

No automorphic-`L` identity, Riemann target match, or Route-B entry is claimed.
