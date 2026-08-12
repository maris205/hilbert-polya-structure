# Claim-Driven Experiment Plan

## 1. Objective and decision target

Test one narrow Stage-1 claim:

> Does the weak mod-2 symbolic shadow attributed to the frozen quadratic map at
> \(a=u_c=1.5436890126920763\) remain a measurable, adequately exposed property of
> the matched Hénon dynamics as \(\rho\) becomes positive and reaches the symplectic
> endpoint \(\rho=1\)?

The plan is designed to return one of four outcomes:

```text
ROBUST_WEAK_SHADOW
A0_FAIL
NOT_TESTABLE_AS_TRANSPORT
UPSTREAM_FAIL
```

`ROBUST_WEAK_SHADOW` is still only a mod-2 result. It is not a rational-prime
correspondence and does not authorize a Riemann-zeta or quantization claim.

No new numerical result is reported in this document.

## 2. Candidate and exact identities

Use

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),
\qquad 0\leq\rho\leq1.
\]

The following invariants are unit-test oracles:

\[
DH_{a,\rho}=
\begin{pmatrix}-2ax&-\rho\\1&0\end{pmatrix},
\qquad
DH^T\Omega DH=\rho\Omega,
\qquad
\det M_\gamma=\rho^n.
\]

At \(\rho=1\), the type-1 generating function

\[
S_a(q,Q)=qQ-q+\frac a3q^3
\]

must recover the map through \(p=-\partial_qS_a\) and
\(P=\partial_QS_a\).

## 3. Source lock and data discipline

The machine-readable file `experiments/source_lock.json` is authoritative. Version 2,
`henon_homotopy_v2_shadow_transport`, was amended after development-only smoke tests
and before the validation or test split was inspected. It declares:

- primary \(a=u_c=1.5436890126920763\), the positive real root of
  \(a^3-2a^2+2a-2=0\);
- neighboring controls \(a\in\{1.50,1.52,1.56,1.58\}\);
- high-\(a\) positive control \((a,\rho)=(6,1)\);
- tainted legacy negative control \(a=1.02\);
- singular reference \(\rho=0\) and primary regular grid
  \(\rho\in\{0.02,0.05,0.1,0.2,0.5,1\}\);
- a separate geometry-only grid
  \(\rho\in\{0.25,0.5,0.75,0.9,0.95,0.99,1\}\);
- primary certification target through period 6, exploratory primary ledger through
  period 8, and high-\(a\) control through period 10;
- root tolerance \(10^{-11}\), deduplication tolerance \(10^{-8}\), and
  80-digit validation;
- the unique endpoint statistic, availability gate, splits, and confirmatory rule
  stated in Sections 7--8 below.

After this v2 lock, any change to parameters, statistic, threshold, or correction
family creates a new experiment rather than silently modifying this one.

Forbidden throughout candidate construction:

- Riemann zeros;
- parameters fitted to zeros;
- prime labels before a ledger is frozen;
- tuning \(a\) to make a multiplier near an integer or prime;
- manually inserted \(\log p\) or von Mangoldt weights.

The historical \(a=1.02\) choice is a tainted legacy negative control because earlier
work associated it with zero-oriented heuristics. It must not be pooled with clean
neighbors or used as evidence for the primary candidate.

## 4. Claims and work packages

| Work package | Claim IDs | Purpose | Gate to pass |
|---|---|---|---|
| WP-A | G1--G3, C3 | Verify map geometry, Jacobians, monodromy, and action code | All exact invariant tests pass |
| WP-B | C1 | Validate orbit enumeration in a high-\(a\) binary-symbolic regime | Expected primitive counts and precision checks pass |
| WP-C | P1 | Independently reproduce the parent mod-2 shadow | Parent statistic and temporal controls are distinguishable |
| WP-D | E1 | Run the conformal/symplectic symbolic-transport test | Exposure gate plus predeclared primary statistic |
| WP-E | E2, C2 | Track low-period branches and quantify ambiguity | No unreported collision, collapse, or completeness claim |
| WP-F | A1, Z1--Z2 | Conditional multiplier-prime exploration | Closed unless WP-C/D justify an A0 continuation |

## 5. WP-A: deterministic geometry validation

### Tests

1. Compare the analytic Jacobian with centered finite differences at fixed test points.
2. Verify \(DH^T\Omega DH-\rho\Omega\) to floating-point tolerance.
3. For every returned period-\(n\) orbit, verify:
   - cyclic residual;
   - minimal period;
   - \(|\det M_\gamma-\rho^n|\);
   - agreement between independent eigenvalue calculations.
4. At \(\rho=1\), verify reciprocal multiplier pairing.
5. Differentiate the generating function numerically and symbolically.
6. Verify the periodic action is invariant under cyclic rotation of the orbit.

### Failure rule

Any invariant failure blocks all interpretation of the affected ledger. Tolerances may
not be loosened after seeing arithmetic labels.

## 6. WP-B: high-\(a\) positive control

Use the clean high-\(a\) control declared in the source lock. Generate one seed per
primitive binary necklace, solve the cyclic orbit equations

\[
x_{i+1}+\rho x_{i-1}-1+a x_i^2=0,
\qquad i\pmod n,
\]

canonicalize under cyclic rotation, and reject solutions of smaller minimal period.

The expected number of primitive binary necklaces is

\[
N_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d}.
\]

For \(n=1,\ldots,10\), the count sequence is

```text
2, 1, 2, 3, 6, 9, 18, 30, 56, 99.
```

### Required validations and present status

- every symbolic seed has a converged representative or an explicit failure record;
- every representative passes the float residual and 80-digit residual check;
- no two representatives agree up to cyclic rotation at the deduplication tolerance;
- minimal periods agree with word primitivity;
- the count agrees with \(N_n\) through the claimed cutoff;
- monodromy determinant checks pass.

The current implementation has passed this gate: it recovered the exact primitive
count sequence through period 10 with no missing necklace class, and the maximum
reported cyclic residual was \(1.42\times10^{-13}\). The geometry/cycle audit suite
also passes. This is `NUMERICALLY_CERTIFIED` for the declared \(a=6\) calibration
regime; it is not a proof of completeness at \(u_c\).

### Interpretation

This work package validates implementation and completeness accounting only in the
calibration regime. Failure returns `ORBIT_FINDER_INVALID`. Success does not certify
the mixed \(u_c\) ledger.

## 7. WP-C: reproduce the upstream parity shadow

### Fixed symbolic convention

For the parent map \(x_{t+1}=1-a x_t^2\), define

\[
s_t=L\quad\Longleftrightarrow\quad x_t<0,
\qquad
s_t=R\quad\Longleftrightarrow\quad x_t\geq0.
\]

Let \(\tau_k\) be successive times with \(s_{\tau_k}=L\), and define the return gap
\(g_k=\tau_{k+1}-\tau_k\). The target parent feature is suppression of odd \(g_k\).
The boundary convention \(x_t=0\mapsto R\) is frozen even if it is rarely encountered.

### Required controls

1. Temporal shuffles preserving the empirical symbol count.
2. A fitted first-order two-state Markov chain preserving one-step transitions.
3. Neighboring \(a\)-parameters declared in the source lock.
4. Independent initial-condition splits.

### Parent failure rule

If the parent effect is not independently reproducible, or is no stronger than the
matched temporal controls, return `UPSTREAM_FAIL`. Do not run or interpret a
multiplier-prime experiment.

## 8. WP-D: unique primary transport statistic

### Locked trajectory manifest

Source-lock v2 fixes:

```yaml
development_seed: 20260812
validation_seed: 20260813
confirmatory_seed: 20260814
trajectories_per_split: 2048
parent_burn_in: 4096
trajectory_horizon: 1024
escape_threshold: 100
bootstrap_unit: trajectory
bootstrap_replicates: 2000
confidence_level: 0.95
```

For each split, PCG64 draws the pre-burn value uniformly from \([-1,1]\) for every
ensemble member. Burn the \(\rho=0\) parent for 4096 steps, then initialize
\((x_0,x_{-1})\) from consecutive parent states. Apply the same split protocol to every
\(\rho\) and clean neighboring \(a\) control. A trajectory is censored at its first
nonfinite coordinate or first coordinate magnitude exceeding 100. No gap crossing the
censoring time is counted.

Development and validation splits may be used to debug implementation, but not to
change the primary definition after the confirmatory manifest is frozen. The
confirmatory split is read once.

### Primary statistic

For pooled pre-censoring return gaps, with uncertainty clustered by trajectory, define

\[
P(\rho)=
\frac{N_{\mathrm{even}}(\rho)-N_{\mathrm{odd}}(\rho)}
     {N_{\mathrm{even}}(\rho)+N_{\mathrm{odd}}(\rho)},
\]

where all counts use only complete gaps before escape. The parent prediction is
\(P(0)=1\).

The **single confirmatory endpoint statistic** is
\(P(1)\). The full response on the singular reference plus
\(\rho\in\{0.02,0.05,0.1,0.2,0.5,1\}\) is secondary and may be
used to localize loss, not to choose a favorable endpoint.

### Exposure eligibility gate

The primary statistic is interpretable as transport only if both conditions hold at
the endpoint:

1. finite-step exposure fraction at \(\rho=1\) is at least 0.80;
2. at least 10,000 eligible return gaps are observed.

If either condition fails, report `NOT_TESTABLE_AS_TRANSPORT`. The conditional
survivor statistic may still be plotted, prominently labeled as descriptive.

### Locked endpoint and specificity rule

The confirmatory endpoint passes only if all of the following hold:

1. the availability gate passes;
2. the trajectory-cluster bootstrap 95% lower confidence bound for \(P(1)\) is at
   least 0.98;
3. \(u_c\) is significantly more specific than **each** clean neighboring-\(a\)
   control, using the predeclared one-sided trajectory-level contrasts and Holm's
   family-wise correction at \(\alpha=0.05\).

Temporal shuffle and first-order Markov nulls remain mechanism diagnostics. They may
demonstrate that parity is a generic consequence of marginal/one-step statistics and
therefore trigger `PROVES_TOO_MUCH`; they are not substituted for the locked neighbor
panel after inspection.

If the endpoint lower-bound criterion fails with adequate exposure, return `A0_FAIL`.
If neighbor parameters or temporal nulls reproduce the effect, return
`PROVES_TOO_MUCH`, which maps to `A0_FAIL` for the arithmetic candidate. If all locked
criteria pass, return `ROBUST_WEAK_SHADOW` only.

### Secondary diagnostics

- exposure and escape-time distributions versus \(\rho\);
- return-gap histogram and tail with cluster-bootstrap intervals;
- symbol marginal and transition matrix;
- change-point sensitivity across the fixed \(\rho\)-grid;
- neighbor-parameter panel;
- development/validation/confirmation consistency.

No secondary diagnostic can overturn a failed primary gate.

## 9. WP-E: periodic-orbit continuation and ambiguity audit

### Scope

- Treat periods \(n\leq6\) as the certification target.
- Treat \(n=7,8\) as exploratory at \(u_c\).
- Use \(n=9,10\) only in the high-\(a\) positive control unless a completeness method
  is supplied.

### Continuation rule

Do not describe \(\rho=0\) to \(\rho>0\) as a regular continuation. Record the
one-dimensional cycle as a singular reference, initialize at a declared positive
\(\rho\), and use predictor--corrector or pseudo-arclength continuation with adaptive
step size. For each accepted node record:

- coordinates and residual;
- minimal period;
- monodromy and multipliers;
- smallest singular value of the cyclic Newton matrix;
- symbolic word;
- branch event label;
- action at \(\rho=1\), when reached.

### Branch identity stop rule

A period collapse, collision, bifurcation, symbol change under the fixed partition,
or nonunique corrector terminates the statement that "the same orbit survives." The
branches may still be described as a bifurcation graph. Failed tracking may not be
silently repaired by choosing another root with a favorable multiplier.

### Completeness language

At \(u_c\), an enumerated ledger is exploratory unless an independent certificate is
available. Multi-start saturation is evidence about search stability, not proof of
completeness. Every table must include a missed-orbit-risk field.

## 10. WP-F: closed arithmetic extension

Do not run an arithmetic multiplier test unless all of the following are true:

1. WP-B validates the orbit code.
2. WP-C reproduces the parent feature.
3. WP-D returns `ROBUST_WEAK_SHADOW` with adequate exposure.
4. The relevant \(u_c\) primitive ledger has a credible completeness statement.
5. The orbit-to-number statistic is frozen before prime/composite labels are opened.

If opened, the test must include prime, composite, shuffled-label, matched-density,
neighbor-parameter, and cat-map controls. A single multiplier close to 5, or an exact
match obtained at a nearby tuned \(a\), is not evidence. No dynamical zeta is evaluated
after an A0 failure.

## 11. Reproducibility artifacts

Each run must write:

```text
results/<run_id>/
├── manifest.json
├── source_lock_snapshot.json
├── environment.txt
├── orbit_ledger.csv
├── branch_events.csv
├── symbolic_summary.csv
├── bootstrap_summary.json
├── invariant_checks.json
├── run.log
└── figures/
```

The manifest must include code hash, configuration hash, date, platform, precision,
random seeds, split label, and forbidden-data check. Raw arrays may be stored in a
documented binary format alongside these summaries.

## 12. Decision table

| Observation | Formal outcome | Next action |
|---|---|---|
| Parent parity does not reproduce | `UPSTREAM_FAIL` | End arithmetic inheritance claim; retain methods/obstruction result |
| High-\(a\) control misses expected cycles | `ORBIT_FINDER_INVALID` | Fix implementation; no \(u_c\) ledger interpretation |
| Symplectic endpoint lacks exposure | `NOT_TESTABLE_AS_TRANSPORT` | Report escape/branch obstruction; no zeta |
| Adequate exposure but parity equivalence fails | `A0_FAIL` | Publish controlled loss if robust; no zeta/quantization |
| Controls reproduce the effect | `PROVES_TOO_MUCH` / `A0_FAIL` | Interpret as generic symbolic dynamics |
| Parity survives all gates | `ROBUST_WEAK_SHADOW` | Design a new, independently locked A0 experiment; do not claim primes yet |
| Branch identity is lost | `BRANCH_AMBIGUOUS` | Report bifurcation graph; forbid "same orbit" wording |
| Ledger completeness is uncertain | `NOT_TESTABLE` for zeta | Stop before determinant evaluation |

## 13. Minimum paper-ready output

A Stage-1 paper is ready for internal review when it contains:

1. the exact geometric identities and correctly scoped elementary obstruction;
2. direct comparison with Fogedby--Jensen and Demaeyer--Gaspard;
3. a passing high-\(a\) software/completeness control;
4. one confirmatory transport outcome with exposure visible;
5. a branch/completeness uncertainty table at \(u_c\);
6. all negative controls and stop-rule decisions;
7. no arithmetic zeta or quantization claim unless separately authorized by a passed
   gate.
