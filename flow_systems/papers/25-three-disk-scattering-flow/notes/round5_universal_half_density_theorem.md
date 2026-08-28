# P25 Round-5 universal half-density theorem and negative-control closure

Date: **2026-08-27**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow: Stage-1 research plus reproducibility validation
- Frozen inputs:
  - Round-2 orbit ledger SHA-256
    `25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736`;
  - Round-3 direct-return-map ledger SHA-256
    `1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e`.
- Target data: none
- Route scope: Stage 1 / A0--A1 negative control

## The theorem

Let `M` be a real `2 x 2` symplectic hyperbolic return matrix.  Its eigenvalues
can be written

```text
sigma Lambda, sigma Lambda^(-1),
Lambda > 1, sigma in {+1,-1}.
```

For every repetition `r >= 1`, `[PROVED]`

```text
|det(I-M^r)|^(-1/2)
  = Lambda^(-r/2) / |1-sigma^r Lambda^(-r)|.
```

Consequently the project statistic

```text
H_r = Lambda^(-r/2)
```

is the universal leading magnitude of the two-dimensional hyperbolic
stability amplitude.  Its relative error against the exact amplitude is
exactly `Lambda^(-r)`:

```text
abs(A_r-H_r)/A_r = Lambda^(-r).
```

### Proof

Since `det(M)=1`, the two eigenvalues are reciprocal and have one common real
sign.  The eigenvalues of `M^r` are `sigma^r Lambda^r` and
`sigma^r Lambda^(-r)`.  Therefore

```text
det(I-M^r)
 = (1-sigma^r Lambda^r)(1-sigma^r Lambda^(-r)).
```

Taking the absolute square root, extracting `Lambda^(r/2)`, and inverting
gives the displayed identity.  Comparing it with `H_r` gives the exact
relative-error formula.  No billiard-specific, arithmetic, prime, or target
assumption enters the proof.

The `sigma=-1` branch matters: odd-collision physical Birkhoff sections in the
frozen ledger have negative trace.  The earlier positive-reflection paraxial
convention and the physical signed convention therefore have different exact
correction factors, while sharing the same leading half-density.  Round 5
stores both rather than replacing a signed amplitude by its leading absolute
envelope.

## Frozen finite-ledger replay

The deterministic audit applies the theorem to all 2,241 certified primitive
owners and repetitions `r=1,2,3`, producing 6,723 rows:

```text
primitive branches                 = 2,241
repetition branches                = 4,482
negative primitive-sign owners     =   804
total theorem-ledger rows          = 6,723
```

The maximum source-half-density replay residual is
`3.954949477893865e-15`.  The maximum formula residual at 100 decimal digits
is about `2.083e-101`.  The largest exact relative correction to the leading
factor is

```text
r=1: 1.1092757866871041e-2
r=2: 1.2304927709302936e-4
r=3: 1.3649558364864960e-6.
```

These are `[NUMERICALLY_CERTIFIED]` facts about the frozen finite ledger.  The
algebraic theorem does not depend on the ledger or its cutoff.

## Paper-level consequence

The project is retained as a methods/negative-control paper.  The theorem
explains why the tested `Lambda^(-r/2)` envelope can persist in a completely
non-arithmetic hyperbolic system: it is forced by the local symplectic
hyperbolic eigenvalue pair before any arithmetic owner is supplied.  Thus
half-density persistence alone cannot establish arithmetic specificity.

This strengthens, but does not overstate, the executed control result:

- the universal leading-factor mechanism is `[PROVED]`;
- the 6,723-row replay is `[NUMERICALLY_CERTIFIED]`;
- the neighboring-geometry and shuffled/composite outcomes remain
  `[NUMERICAL_OBSERVATION]`; and
- using half-density persistence as arithmetic evidence remains
  `[STOP_SCOPED] / PROVES_TOO_MUCH`.

The result does not say that every phase-sensitive or source-derived
observable is non-discriminative.  It stops this magnitude-only statistic.
The next scientifically lawful branch is either to draft the authorized
negative-control manuscript later or to introduce a genuinely source-owned,
phase-sensitive observable with a predeclared falsification contract.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_NEGATIVE_CONTROL
UNIVERSAL_HALF_DENSITY_THEOREM=PROVED
FINITE_REPETITION_LEDGER=NUMERICALLY_CERTIFIED_6723_OF_6723
PAPER_DISPOSITION=RETAIN_AS_METHODS_NEGATIVE_CONTROL_PAPER
A0_SOURCE_STATUS=ABSENT_BY_CONSTRUCTION
HALF_DENSITY_CONTROL_VERDICT=STOP_SCOPED / PROVES_TOO_MUCH
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2_EVALUATION=NOT_RUN
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
ARS_STAGE_2_MANUSCRIPT_AUTHORIZED=false
```

## Primary source boundary

The semiclassical three-disk orbit surface is source-locked to Gaspard and
Rice, *Semiclassical quantization of the scattering from a classically chaotic
repellor*, https://doi.org/10.1063/1.456018, and to Wirzba,
*Quantum Mechanics and Semiclassics of Hyperbolic n-Disk Scattering Systems*,
https://arxiv.org/abs/chao-dyn/9712015.  The exact two-eigenvalue identity above
is proved locally and is not attributed to those papers as a novelty claim.
