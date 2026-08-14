# SD-C16 Experiment Plan

**Candidate:** reduced tensor bar-code one-vertex signed edge shift

**Date:** 2026-08-14

**System family:** Symbolic Dynamics only

**Compute:** deterministic CPU; no GPU

**Target-zero data:** forbidden and unused

## Claim map

| Claim | Evidence required | Block |
|---|---|---|
| C1: finite-local positive-cone cocycles cannot be arithmetic-selective | exact first-mode certificates plus planted-block shuffles | B1 |
| C2: tensor incidence recovers the Mangoldt profile | exact formal entropy-basis coefficients and cutoff stability | B2 |
| C3: the reduced bar grammar has a canonical scalar determinant | raw geometric convergence, endpoint coefficient completion, and independent reciprocal coefficients | B3–B4 |
| C4: the trace-log has the declared repetition semantics | high-precision repetition reconstruction only where `abs(z F)<1` | B5 |
| C5: reciprocal inversion is not arithmetic-selective | exact composite, random, shuffled, signed, and scalar controls | B6 |

## Frozen blocks

### B1 — Local cocycle falsification

- Exact point: `s=2`, `z=1/3`.
- Inventory cutoffs: `16,32,64,128`.
- Seeds: shuffled `14000..14015`; random-increasing `14100..14115`.
- Named rules: 18.
- Exhaustive rules: all 256 radius-one Boolean tables and all 260 labelled
  one-/two-state binary Mealy machines.
- Stop: any nontrivial shuffled control retaining the first Fourier mode is
  `PROVES_TOO_MUCH` for that local selector.

### B2 — Global tensor incidence

- Principal-ideal cutoffs: `64,128,256,512`.
- Compute `mu_tensor` recursively from divisibility, then
  `Lambda_tensor=mu_tensor*h` in the formal tensor-prime entropy basis.
- Entropy-relabel seeds: `14200..14207`.
- Success: exact `Lambda_tensor(p^r)=log p`, exact zero on mixed-prime
  endpoints, and exact overlap stability.
- Boundary: inventory subsets that are not divisor closed cannot redefine the
  incidence function; they are ambient evaluation subsets only.

### B3 — Raw bar-word determinant

Let `B(s)=zeta(s)-1` and

```text
F_L(s) = sum_(ell=1)^L (-1)^(ell+1) B(s)^ell.
```

- Word lengths: `1,2,4,8,16,32,64`.
- Points: `1.75`, `1.8`, `2`, `1.9+0.6i`.
- Precision: 80 decimal digits.
- The raw domain is predeclared as `Re(s)>sigma_bar`, where
  `zeta(sigma_bar)=2`.
- Check the exact geometric remainder and
  `D_bar(s,1)=1-F_bar(s)=1/zeta(s)`.
- An exact rational finite-alphabet certificate is run at `s=2`, endpoint
  cutoff 32, independently of floating arithmetic.

### B4 — Endpoint-first completion

- Formal endpoint cutoff: 512.
- Enumerate every ordered factorization word through its maximum possible
  length and verify the grouped coefficient is `-mu_tensor(n)`.
- Independently compute the Dirichlet inverse of the constant-one sequence.
- Numerical points in `Re(s)>1`: `1.1`, `1.25`, `1.5`, `1.7`,
  `1.25+0.75i`.
- Möbius partial-sum cutoffs: `100,1000,10000,100000` at 80 digits.
- These finite residuals are `NUMERICAL_OBSERVATION`; the analytic identity
  comes from the exact coefficient theorem, not from numerical convergence.

### B5 — Trace-log repetitions

- Points: raw `1.75,2`; endpoint-grouped `1.25`.
- `z=0.25,0.5,1`.
- Repetitions: `1,2,4,8,16,32,64,128,256`.
- Only points satisfying `abs(z F)<1` are admitted.

### B6 — Universal inversion controls

At coefficient cutoff 128, independently compare alternating bar words with
the Dirichlet inverse for:

- all objects;
- composite-only and prime-only inventories;
- seeded random positive weights;
- seeded random-increasing support;
- synthetic signed weights;
- shuffled ramp weights;
- three exact scalar partition sums.

If all controls invert exactly, record
`STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`; do not weaken or hide the
control because the arithmetic inventory also succeeds.

## Run order

| Milestone | Command / output | Decision gate |
|---|---|---|
| M0 sanity | selected exact coefficient and rational-tail tests | all exact identities pass |
| M1 local/global | local rules and tensor incidence ledgers | no fitted selector; incidence exact |
| M2 bar formal/raw | formal coefficients and geometric convergence | domains kept separate |
| M3 endpoint/trace | 80-digit partial sums and repetitions | residuals reported without zero claims |
| M4 controls | generic inversion matrix | mandatory `PROVES_TOO_MUCH` verdict |

## Target-zero fields

Every train/validation/test zero error, missing/extra-zero count, root-count
discrepancy, and root-fit metric is `not_applicable`. No root search or target
zero table is part of SD-C16.
