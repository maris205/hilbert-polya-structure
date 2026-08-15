# Experiment Plan

**Problem:** Determine whether quotienting cat-map torsion cycles by their
finite centralizer yields an intrinsic multiplicity-one arithmetic dynamics,
or only a modulus-wise coarse quotient with an externally assigned clock.

**Method thesis:** Exact finite-module checks should reproduce the proved
cyclic-vector torsor and group strata while exposing two independent failure
modes: the induced quotient dynamics is trivial, and the symplectic
centralizer retains norm-class multiplicity.

**Date:** 2026-08-15 UTC.

**Authorization state:** `DESIGN_ONLY / NOT_AUTHORIZED_FOR_CODE_OR_EXECUTION`.
An independent source-lock PASS and a later code-tree-bound deployment review
are required before one registered audit may run.

## Frozen object and data policy

The only matrix is

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
$$

The complete authorized modulus list is

$$
\mathcal Q_{\rm frozen}=\{2,3,5,7,11,4,6,9,10\}.
$$

- Prime controls $2,3,5,7,11$ are inherited from Paper 9.
- Composite controls $4,6,9,10$ are fixed before implementation to represent
  a binary lift, squarefree inert CRT product, odd inert lift, and
  binary--ramified CRT product.
- No other prime or composite may be generated, scanned, sampled, or used as
  a fallback.

Allowed operations are exact integer arithmetic, modular arithmetic, finite
set construction, finite matrix multiplication, determinant/unit tests,
finite group/set orbit calculations, exact rational fractions, JSON
serialization, hashing, and schema validation.

Forbidden operations include network access during execution, a prime table
or primality search, Riemann-zero data, numerical evaluation of $s$,
$\log q$, or $q^{-s}$, floating-point fitting, matrix search, parameter
search, random seeds, Monte Carlo inference, new moduli, transfer/Fredholm
operators, quantization, and stacky/equivariant/twisted-sector construction.

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1: $\mathrm{CV}_q$ is a $C_q=R_q[A]^\times$ torsor for all frozen $q$ | validates the proposed multiplicity compression exactly | independent definitions of the commutant, algebra units, cyclic locus, action map, and all four torsor axioms agree at every fixed modulus | B1, B2 |
| C2: the one-class quotient is static and non-prime-specific | separates set multiplicity from an arithmetic clock | induced $A$ action is identity; all four composites also have one full-$C_q$ quotient class; no numerical clock field exists | B3, B5 |
| C3: the symplectic centralizer does not give one class in general | tests whether the escape remains inside the symplectic-map premise | exact $C_q^1$ orbits equal $\Delta_q$ fibers and norm image; frozen counts match $\varphi(q)$ or $\varphi(q)/2$ | B3 |
| C4: split/ramified full shells contain discarded strata | prevents a cyclic-stratum result from being sold as a full-shell result | exact $E_q$, $\mathrm{CV}_q$, discarded set, full-centralizer strata, and prime reversing-group strata match the proof | B4 |
| C5: the terminal outcome is an A0 failure, not a zeta or quantum pass | enforces the project gate | all relations pass, external-label and composite controls are true, forbidden counters are zero, and machine decision is exact | B5 |

Anti-claims to rule out:

- the one class is caused by a nontrivial quotient return time;
- the full centralizer is automatically symplectic;
- the cyclic locus equals the full exact-order shell at every prime;
- the construction singles out primes rather than arbitrary moduli;
- nine examples establish the all-$q$ theorem;
- a passing audit opens an equivariant, stacky, Hecke, transfer, quantum, or
  Route-B continuation.

## Paper Storyline

Main paper must prove:

1. cyclic basis $\Rightarrow$ commutant $R_q[A]$ $\Rightarrow$ torsor;
2. $A\in C_q$ $\Rightarrow$ one quotient class but identity induced
   dynamics;
3. $C_q^1$ quotient $\Rightarrow$ norm classes;
4. prime full-shell strata and discard fractions;
5. composite controls $\Rightarrow$ no prime specificity.

The exact audit is only a finite falsification and implementation control.
The paper must not use it as proof of an infinite statement.

Appendix support may include the nine-modulus ledger, exact formulas for
algebra units, orbit partitions, schema, and provenance counters.

Intentionally cut:

- additional primes, prime powers, or composite scans;
- empirical asymptotics or convergence;
- any numerical value of an analytic parameter;
- a transfer or Fredholm determinant;
- Hecke quantization or quantum spectra;
- Burnside-ring, orbifold, stack, groupoid, or twisted-sector zeta
  constructions;
- prime/zero comparison.

## Experiment Blocks

### Block 1: Schema and independent-definition preflight

- **Claim tested:** the later candidate encodes exactly the frozen object and
  does not hide a second modulus list or arithmetic target.
- **Why this block exists:** a torsor audit is meaningless if the centralizer,
  cyclic locus, or group ambient changes between modules.
- **Dataset / split / task:** no data split; parse the source lock and fixed
  nine-modulus ledger.
- **Compared systems:** direct matrix representation versus quadratic-algebra
  representation.
- **Metrics:** exact source-lock hashes; one matrix; one modulus tuple;
  duplicate-key rejection; forbidden-field absence; deterministic
  serialization.
- **Setup details:** exact arithmetic only; no candidate science run.
- **Success criterion:** all hashes and schema fields match, and every
  executable path reads the same frozen tuple.
- **Failure interpretation:** implementation is not authorized; repair code
  before any registered audit.
- **Table / figure target:** provenance table only.
- **Priority:** MUST-RUN.

### Block 2: Centralizer and torsor closure

- **Claim tested:** C1.
- **Why this block exists:** this is the sole positive algebraic mechanism.
- **Dataset / split / task:** for each fixed $q$, enumerate
  $\mathrm{Mat}_2(R_q)$ and independently construct
  $R_q[A]=\{aI+bA\}$; enumerate units and cyclic vectors.
- **Compared systems:**
  1. matrices satisfying $UA=AU$;
  2. polynomial matrices $aI+bA$;
  3. unit polynomial matrices;
  4. vectors with unit $\det[v,Av]$.
- **Metrics:** exact set equality; $|C_q|=|\mathrm{CV}_q|$; injective,
  surjective, free, and transitive action booleans; exact additive order of
  each cyclic vector.
- **Setup details:** the largest raw matrix space is $11^4=14641$ matrices;
  exhaustive exact enumeration is small and deterministic.
- **Success criterion:** every equality and torsor axiom is true at all nine
  moduli with no exception.
- **Failure interpretation:** either the implementation or frozen theorem is
  false; the registered audit fails and no replacement modulus is allowed.
- **Table / figure target:** main exact ledger, algebra/torsor columns.
- **Priority:** MUST-RUN.

### Block 3: Orbit quotient, norm fibers, and clock kill

- **Claim tested:** C2 and C3.
- **Why this block exists:** it separates multiplicity removal from a valid
  symplectic arithmetic clock.
- **Dataset / split / task:** compute $A$-orbits on $\mathrm{CV}_q$,
  $C_q$-orbits, $C_q^1$-orbits, determinant/norm images, and induced
  quotient transitions.
- **Compared systems:** full $\mathrm{GL}_2(R_q)$ centralizer versus
  symplectic $\mathrm{SL}_2(R_q)$ centralizer.
- **Metrics:**
  - $\operatorname{ord}_q(A)$;
  - uniform cyclic-vector orbit length;
  - $|\Gamma_q^{\rm cyc}|$;
  - one full-centralizer quotient class;
  - $C_q^1$ quotient count and exact $\Delta_q$-fiber equality;
  - norm-image set and cardinality;
  - induced $A$ transition on both quotient sets;
  - a required string `IDENTITY_NO_NATIVE_MODULUS_CLOCK`.
- **Setup details:** determinant is computed directly and as
  $a^2+3ab+b^2$; agreement is mandatory.
- **Success criterion:** full quotient count is one; symplectic quotient
  counts are $1,2,2,6,10,2,2,6,2$ in frozen order; every induced transition
  is identity; no numerical analytic field is emitted.
- **Failure interpretation:** the proposed A0 certificate is not established.
- **Table / figure target:** main GL-versus-Sp comparison table.
- **Priority:** MUST-RUN.

### Block 4: Full-shell strata, discard, and reversing boundary

- **Claim tested:** C4.
- **Why this block exists:** a one-class cyclic locus may conceal noncyclic
  vectors in the full additive-order shell.
- **Dataset / split / task:** enumerate $E_q$, $\mathrm{CV}_q$, their
  difference, and full-centralizer orbits.  For the five frozen primes only,
  construct the reversing group
  $\mathcal R_p(A)=\{G:GAG^{-1}=A^{\pm1}\}=C_p\cup JC_p$ and its shell
  orbits.
- **Compared systems:** binary/inert, split, ramified, and composite CRT
  controls.
- **Metrics:** exact shell, retained, and discarded counts; exact rational
  fractions; full-$C_q$ shell-orbit count; full-$C_q^1$ shell-orbit count;
  prime reversing-group orbit count; cyclic/noncyclic mixing boolean; local
  pseudo-symmetry scope flag.
- **Setup details:** no new prime or modulus; no factorization or primality
  service.
- **Success criterion:** the full ledger matches the source lock.  Prime
  reversing-group shell counts are $1,1,2,1,2$ at $2,3,5,7,11$ and no
  reversing orbit mixes $\mathrm{CV}_p$ with its complement.  The result
  identifies $C_q$ as a $q$-dependent local group and makes no global-lift
  assertion.
- **Failure interpretation:** the full-shell boundary or reversing statement
  must be rejected.
- **Table / figure target:** retained/discarded stratum table.
- **Priority:** MUST-RUN.

### Block 5: Proves-too-much and terminal-decision gate

- **Claim tested:** C2 and C5.
- **Why this block exists:** an algebraically exact repair is not an
  arithmetic mechanism if it applies equally to predeclared composites and
  needs an external label.
- **Dataset / split / task:** evaluate only the four composite controls and
  result-schema provenance counters.
- **Compared systems:** inherited primes versus structurally selected
  composites; full versus symplectic quotient.
- **Metrics:** composite full-quotient class count; quotient-map identity;
  external-label flag; prime-selector flag; numerical-clock counter;
  network/data-access counters; route status.
- **Success criterion:** every composite full quotient has one class; every
  quotient action is identity; `external_modulus_label_required=true`;
  `intrinsic_prime_selector=false`; all forbidden counters are zero; exact
  terminal status is
  `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
  `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
- **Failure interpretation:** if composites differ, the proves-too-much
  conclusion fails; if forbidden counters are nonzero, result integrity
  fails; neither outcome authorizes exploratory replacement runs.
- **Table / figure target:** mechanism-boundary summary.
- **Priority:** MUST-RUN.

## Frozen expected results

The implementation must reproduce this exact table, derived before code:

| $q$ | type | $|E_q|$ | $|\mathrm{CV}_q|$ | discarded | $|C_q^1|$ | $\operatorname{ord}_q(A)$ | cyclic $A$-orbits | $|\mathrm{CV}_q/C_q|$ | $|\mathrm{CV}_q/C_q^1|$ | $|E_q/C_q|$ | $|E_q/C_q^1|$ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | binary inert | 3 | 3 | 0 | 3 | 3 | 1 | 1 | 1 | 1 | 1 |
| 3 | inert | 8 | 8 | 0 | 4 | 4 | 2 | 1 | 2 | 1 | 2 |
| 5 | ramified | 24 | 20 | 4 | 10 | 10 | 2 | 1 | 2 | 2 | 4 |
| 7 | inert | 48 | 48 | 0 | 8 | 8 | 6 | 1 | 6 | 1 | 6 |
| 11 | split | 120 | 100 | 20 | 10 | 5 | 20 | 1 | 10 | 3 | 12 |
| 4 | binary inert lift | 12 | 12 | 0 | 6 | 3 | 4 | 1 | 2 | 1 | 2 |
| 6 | binary/inert CRT | 24 | 24 | 0 | 12 | 12 | 2 | 1 | 2 | 1 | 2 |
| 9 | inert lift | 72 | 72 | 0 | 12 | 12 | 6 | 1 | 6 | 1 | 6 |
| 10 | binary/ramified CRT | 72 | 60 | 12 | 30 | 30 | 2 | 1 | 2 | 2 | 4 |

Additional exact identities:

$$
|C_q|=|\mathrm{CV}_q|,
\qquad
|C_q^1|=\frac{|C_q|}{|\operatorname{im}N_q|},
\qquad
|\Gamma_q^{\rm cyc}|=\frac{|C_q|}{\operatorname{ord}_q(A)}.
$$

Prime reversing-group full-shell orbit counts at $2,3,5,7,11$ are frozen as
$1,1,2,1,2$.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | source-lock and schema readiness | R000--R003 | independent source PASS, then independent code `DEPLOYMENT_PASS` | CPU seconds; no science run | hash drift or duplicate schema |
| M1 | independent definitions and torsor unit tests | R010--R019 | all development tests pass without altering fixed object | CPU seconds | accidentally sharing one implementation between “independent” definitions |
| M2 | freeze implementation and registered claim | R020--R024 | code-tree/review/claim hashes bound; clean network-disabled environment | no science result yet | provenance mismatch |
| M3 | sole registered exact audit | R100 | exactly one execution over the fixed nine moduli | under one CPU minute | any mismatch is terminal FAIL, not a tuning signal |
| M4 | read-only result integrity | R110--R119 | independent reviewer recomputes hashes, tables, counters, and decision without rerun | CPU seconds | confusing finite verification with proof |
| M5 | paper handoff | R120 | only after result PASS | no additional run | claim expansion beyond source lock |

The sole registered audit must be deterministic and seedless.  Development
tests may exercise code structure before deployment freeze, but they may not
add moduli or inspect external arithmetic targets.  The registered candidate
may not be rerun to repair a scientific result.

## Compute and Data Budget

- Total estimated accelerator hours: **0**.
- Total estimated CPU time for the registered audit: **less than one minute**.
- Maximum enumerated ambient matrix space: $11^4=14641$ matrices.
- External data preparation: **none**.
- Human evaluation: independent proof/source review, code review, result
  integrity review, and later manuscript review only.
- Biggest bottleneck: semantic and provenance discipline, not compute.

## Result artifact contract

A later implementation should produce one raw machine-readable result with:

1. exact source-lock, code-tree, code-review, and claim hashes;
2. the unique matrix and ordered nine-modulus tuple;
3. one record per modulus containing every column in the frozen table;
4. independent-definition equality booleans;
5. torsor axiom booleans;
6. exact $A$-orbit, centralizer, symplectic-centralizer, and reversing-group
   profiles;
7. norm-image and $\Delta_q$-fiber equality records;
8. quotient-transition records explicitly equal to identity;
9. external-label and composite proves-too-much decisions;
10. zero-valued forbidden-operation counters; and
11. the exact terminal classification.

No result artifact may contain a floating-point approximation to $s$,
$\log q$, $q^{-s}$, a prime density, or a zero ordinate.

## Risks and Mitigations

- **Risk: full $\mathrm{GL}_2$ and symplectic centralizers are conflated.**
  **Mitigation:** construct them separately and require determinant-one
  membership plus different expected quotient counts.
- **Risk: coarse quotient class is mislabeled as a primitive arithmetic
  orbit.**  **Mitigation:** store induced transition, native period $1$, and
  `external_modulus_label_required=true` as mandatory fields.
- **Risk: split/ramified discarded vectors disappear from reporting.**
  **Mitigation:** enumerate $E_q$ independently and require exact complement
  and full-shell orbit profiles.
- **Risk: composite controls are chosen after results.**  **Mitigation:** bind
  the exact tuple and structural rationale in the source lock before code.
- **Risk: finite controls are treated as proof.**  **Mitigation:** mark every
  all-$q$ claim `proof_only`; result report must call the run a falsification
  control.
- **Risk: equivariant or Hecke mechanisms are falsely excluded.**
  **Mitigation:** machine and human reports list them as `OUTSIDE_SCOPE`, not
  `FAIL`.
- **Risk: a failed registered run is rerun after a patch.**
  **Mitigation:** one registered claim, one result; implementation defects
  must be closed during pre-execution review.

## Final Checklist

- [x] Main theorem claims are frozen before implementation.
- [x] Novelty is isolated as a scoped decision package.
- [x] The full/symplectic distinction is mandatory.
- [x] The coarse quotient/quotient-dynamics distinction is mandatory.
- [x] Composite proves-too-much controls are fixed.
- [x] Prime and zero data are forbidden.
- [x] Numerical analytic evaluation is forbidden.
- [x] All nine expected profiles are frozen.
- [x] Reversing-group scope is prime-only and fixed.
- [x] The local pseudo-symmetry versus global-centralizer cost is explicit.
- [x] Equivariant/stacky/Hecke mechanisms are outside scope.
- [x] Nice-to-have runs have been cut; every planned run defends a claim.
- [ ] Independent final source-lock review has passed.
- [ ] Code-tree-bound deployment review has passed.
- [ ] Sole registered audit has passed.
