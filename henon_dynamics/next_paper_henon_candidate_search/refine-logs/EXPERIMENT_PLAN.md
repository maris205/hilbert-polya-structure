# First-round experiment plan

Date: 2026-08-05
Generation: HCS-2026-08-05
Status: FROZEN FOR SANITY-FIRST EXECUTION

## 1. Scope

Run three independent, target-blind micro-pilots:

1. P1 / HCS-C03: exact finite-field local zeta census;
2. P2 / HCS-C02: intrinsic derivative-projective domain gate;
3. P3 / HCS-C05: phase-bearing action--instability determinant gate.

No Riemann zero ordinate, target prime weight, fitted spectral scale, or
post-hoc functional completion is available to these runs. The pilots test
BF0--BF3 only; none can by itself pass formal Route-A A2 or A3.

## 2. Common requirements

- Reuse existing certified artifacts where possible.
- Run the smallest sanity case before the full command.
- Freeze seeds and all conventions in the result JSON.
- Save machine-readable JSON and CSV plus a human-readable RESULTS.md.
- Preserve signed and complex weights.
- Include a self-check or test command.
- Report a positive result, a hard kill, or NOT_TESTABLE with equal prominence.
- Do not modify target-dependent legacy artifacts.

## 3. P1 -- HCS-C03 finite-field local zeta

### Object

\[
H_6(q,p)=(1-6q^2-p,q)\pmod{\mathfrak p}
\]

as a permutation of \(\mathbb F_{\mathfrak p}^2\), with exact cycle counts
\(c_{\ell,\mathfrak p}\) and

\[
Z_{\mathfrak p}(u)=\prod_\ell(1-u^\ell)^{-c_{\ell,\mathfrak p}}.
\]

### Sanity

- primes at most 11;
- verify bijectivity and total cycle mass
  \(\sum_\ell \ell c_{\ell,\mathfrak p}=\mathfrak p^2\);
- reconstruct fixed-point counts from cycle data for a frozen small range.

### Full run

- every prime at most 251;
- exact cycle-factor representation;
- deterministic random-permutation controls of the same cardinality;
- only predeclared bulk diagnostics, with no fitted normalization.

### Metrics

- cycle number, fixed points, maximum cycle length, number and mass of fixed
  and short cycles;
- exact self-check failures;
- deviations from random-permutation controls with seed uncertainty;
- whether a canonical local normalization exists before any global product.

### Decision

- BF2 pass: all exact ledger identities pass.
- BF3 candidate: a cross-prime invariant survives controls and has a
  predeclared interpretation.
- Hard kill for the proposed global mechanism: only universal finite
  permutation structure remains or normalization is noncanonical.

## 4. P2 -- HCS-C02 derivative-projective gate

### Object

For \(H_6\), the true derivative sends tangent slope \(m\) to

\[
\Phi_q(m)=\frac{1}{-12q-m}.
\]

The pilot asks whether certified branch/cylinder geometry supplies canonical
real or complex domains on which ordered true-Hénon projective maps are
separated, invariant, and contracting. It may not fit independent Möbius
generators.

### Sanity

- inventory every available h-set, cone, cylinder, inverse-branch, and complex
  domain artifact;
- reproduce one real slope/cone image directly from frozen source data;
- explicitly label any missing complex-domain premise.

### Full run

- memories 1 through 8 when the artifact interface supports them;
- interval or complex-disk images under ordered true branch maps;
- separation, strict containment, contraction, and distortion diagnostics.

### Metrics

- minimum containment margin and inter-domain gap;
- maximum projective derivative modulus;
- image diameter/width by memory;
- distortion decay, or the smallest explicit overlap/counterexample;
- provenance of every domain choice.

### Decision

- BF1 pass only if domains/generators are intrinsic to Hénon geometry.
- BF3 candidate only if a canonical contracting holomorphic cocycle and a
  credible error theorem target survive.
- NOT_TESTABLE is required if existing certificates do not define the complex
  objects; a heuristic plot cannot repair the missing premise.

## 5. P3 -- HCS-C05 phase-bearing determinant

### Object

Use the positive clock

\[
\ell_\gamma=\log|\Lambda_{u,\gamma}|
\]

and the exact discrete action \(A_\gamma\) from Paper 5's generating function.
The phase character must be derived before evaluation from monodromy,
orientation, reversor, or a proved Maslov rule.

### Sanity

- verify all required fields for all 2,170 catalogue records;
- verify action and orientation repetition laws on explicit repeats;
- reproduce the exact zero-action period-four obstruction;
- determine whether the stored data are sufficient to define a canonical
  Maslov index.

### Full run

- cutoffs 8, 12, 16, and 20;
- one frozen complex determinant/coefficient convention;
- orientation/reversor phase if canonical; Maslov only if derivable;
- shuffled-action, random-phase, constant-roof, and inherited scalar controls;
- fixed random seeds.

### Metrics

- product/trace or independent coefficient discrepancy;
- cutoff drift at frozen probes and/or coefficient norms;
- exact conjugation/reversal/repetition residuals;
- deterministic-versus-control margin;
- Maslov canonicality verdict.

### Decision

- BF2 pass: the complete signed/phase ledger and repetition identities pass.
- BF3 candidate: a deterministic phase/factorization anomaly survives every
  prespecified control and cutoff.
- Hard kill or downgrade: phase is noncanonical, only a forced conjugate
  completion creates symmetry, or controls explain the observation.

## 6. Compute budget and run order

All runs are CPU-only.

| Run | Priority | Cap | Order |
|---|---|---:|---:|
| P1 sanity/full | MUST | 2 CPU-hours | 1 |
| P2 sanity/full | MUST | 2 CPU-hours | 1 |
| P3 sanity/full | MUST | 2 CPU-hours | 1 |
| independent rerun | CONDITIONAL | 2 CPU-hours per anomaly | 2 |

The three sanity runs may execute in parallel. Any run exceeding twice its cap
is stopped and reported rather than silently enlarged.

## 7. Handoff

After completion:

1. review code independently;
2. rerun tests and decisive commands;
3. write refine-logs/EXPERIMENT_RESULTS.md;
4. append candidate-specific Route-A YAML only for pilots that reach BF3;
5. update docs/obstruction_registry.md for every reusable negative result.
