# Experiment Plan

**Problem:** Determine exactly which source-period, orbit-type, twist, and
stabilizer information survives standard equivariant refinements of the
Paper-10 full-centralizer quotient, and whether any surviving datum supplies
an intrinsic modulus/prime clock.

**Method thesis:** A definition-separated exact audit should certify a strict
information-loss hierarchy: point-order Burnside data retain source order,
orbit-order data retain only quotient orbit type, $G$-permutation/enhanced
carriers retain the translating element only inside a labelled local group,
and orbifold/Morita quotient outputs are static.

**Date:** 2026-08-15 UTC.

**Authorization state:** `DESIGN_ONLY / NO_CODE / NO_REGISTERED_EXECUTION`.
A fresh independent source-lock PASS and a later independent code-tree-bound
`DEPLOYMENT_PASS` are required before one registered exact audit.

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1: standard equivariant carriers form a strict information-loss hierarchy on the centralizer torsor | prevents three inequivalent definitions from being conflated and identifies the strongest positive boundary | exact fixed-point, fixed-orbit, twisted, enhanced, mark, inertia, and groupoid records agree with the proof at every frozen modulus | B1--B4 |
| C2: none of the audited standard outputs supplies a one-factor intrinsic prime/modulus clock | decides Route A without claiming a universal no-go theorem | four scalar reductions have the frozen support/exponent pairs; period collisions and composites pass; every unit-factor quotient output has period one; all stronger carriers stay in varying labelled groups/rings | B2--B5 |

Anti-claims to rule out:

- the 2008 point-order rational zeta (revisited in 2015) and the distinct
  2015 orbit-order integral zeta are one invariant;
- the untwisted point-order series remembers the exact generator $A$;
- the 2013 $G$-permutation triple is $(1,1,A)$ rather than the convention-
  locked $(1,1,A^{-1})$;
- a labelled $G_q$-element is already a common cross-modulus return clock;
- nonempty inertia sectors necessarily carry nontrivial dynamics;
- an effective action containing an element of order $r$ must exhibit a
  period-$r$ point orbit;
- the finite audit proves an all-$q$ theorem;
- Miles's infinite acting-group zeta or Walton's finite-field variety theorem
  has been implemented or extended; and
- a passing audit opens transfer, Fredholm, Hecke, quantization, Ruelle/Fried,
  prime/zero, RH, or Route-B work.

## Frozen object and data policy

The arithmetic object is inherited exactly:

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
\mathcal Q_{\rm frozen}=(2,3,5,7,11,4,6,9,10).
$$

No tenth modulus may be generated, scanned, substituted, or used as a
fallback.  The abstract group-theoretic control

$$
C_6/C_2\sqcup C_6/C_3
$$

is frozen as a symbolic proof/development control.  It is not a modulus, an
arithmetic candidate, or an additional registered row.

Allowed operations are exact integer and modular arithmetic, finite matrix
and group operations, finite set construction, exact orbit partitions,
exact fixed-set tables, exact rational numerator/denominator arithmetic,
canonical JSON, hashing, and schema validation.

Forbidden operations include network access during execution, external prime
or zero data, a generated prime list, a new modulus, numerical evaluation of
$s$, $\log q$, $q^{-s}$, floating-point fitting, matrix or group search,
randomness, a new zeta convention, analytic continuation, transfer/Fredholm
operators, Hecke/quantum data, and post-result retuning.

## Paper Storyline

Main paper must prove:

1. the general finite-abelian-$C$-set information-loss hierarchy;
2. its regular-torsor specialization and four scalar reductions;
3. the stronger twisted invariant and its action-kernel qualification;
4. the static orbifold/inertia/quotient-stack boundary;
5. the abstract effective no-full-period counterexample; and
6. the composite and period-collision A0 controls.

The appendix may contain complete nine-row fixed tables, every matrix-group
fingerprint, exact subgroup/stabilizer evidence, and provenance manifests.

Experiments intentionally cut:

- new primes or composites;
- the full noncyclic shell $E_q$ (Paper 10 already audited it);
- symplectic-centralizer, reversing-group, or Hecke alternatives;
- numerical formal-variable specializations;
- an implementation of Miles, Walton, Ruelle, Fried, transfer, Fredholm, or
  representation-valued theories; and
- any global Euler product.

## Experiment Blocks

### Block 1: Upstream binding and regular-torsor reconstruction

- **Claim tested:** C1.
- **Why this block exists:** every later invariant assumes the exact
  Paper-10 $G_q$-torsor; hash drift or a different local group invalidates
  the comparison.
- **Dataset / split / task:** the nine frozen moduli only; bind all named
  Paper-10 terminal hashes; independently reconstruct $R_q[A]^\times$,
  $X_q=\mathrm{CV}_q$, the action $G_q\curvearrowright X_q$, and the exact
  matrix $a_q=A\bmod q$.
- **Compared systems:** algebra-unit and matrix-commutant definitions;
  torsor map and direct cyclic determinant definition.
- **Metrics:** exact set equality; action closure; freeness; transitivity;
  action kernel; $n_q$; $r_q$; $m_q$; uniform cycle lengths.
- **Setup details:** all elements are canonical matrix tuples; no abstract
  group relabelling replaces the bound matrix group.
- **Success criterion:** exact tuples
  $(n_q,r_q,m_q)$ are
  $(3,3,1),(8,4,2),(20,10,2),(48,8,6),(100,5,20),
  (12,3,4),(24,12,2),(72,12,6),(60,30,2)$ in frozen order; every action is
  regular and effective.
- **Failure interpretation:** source object mismatch; no equivariant result
  is reportable.
- **Table / figure target:** upstream/torsor passport.
- **Priority:** MUST-RUN.

### Block 2: Point-order versus orbit-order Burnside audit

- **Claim tested:** C1 and C2.
- **Why this block exists:** these are the two definitions most likely to be
  conflated.
- **Dataset / split / task:** for each frozen $q$, compute
  $L^{G_q}(\phi_q^k)$ and $\widetilde L^{G_q}(\phi_q^k)$ for
  $1\le k\le2r_q$ as exact $G_q$-set basis records; perform exact divisor
  inversion.
- **Compared systems:** fixed-point class versus fixed-$G_q$-orbit class.
- **Metrics:** support; Burnside basis coefficient; integrality/rationality
  flag; every element-fixed count; regular marks; cardinality and additive
  exact-period orbifold reduction support/exponent pairs.  No reduction is
  tested as a homomorphism of Burnside multiplication or power structures.
- **Setup details:** store factors symbolically as
  `(support, exponent_numerator, exponent_denominator, coefficient_basis)`;
  do not evaluate a power series numerically.
- **Success criterion:** point data have sole support $r_q$ and coefficient
  $[G_q/1]$; orbit data have sole support $1$ and the same coefficient.  The
  four scalar signatures are
  $(r_q,m_q)$, $(r_q,1/r_q)$, $(1,n_q)$, and $(1,1)$.
- **Failure interpretation:** the information-loss theorem or implementation
  is false; no alternative convention may be substituted.
- **Table / figure target:** main four-reduction table.
- **Priority:** MUST-RUN.

### Block 3: Twisted $G$-permutation and enhanced-carrier audit

- **Claim tested:** C1.
- **Why this block exists:** the stronger invariant can retain the
  translating element, contradicting any blanket claim that all equivariant
  data forget the clock.
- **Dataset / split / task:** for every frozen $q$, enumerate all
  $g\in G_q$ and $0\le k<r_q$; compute fixed sets of $g\phi_q^k$; compute the
  $(\mathbb Z\times G_q)$ stabilizer relation and enhanced tuple.
- **Compared systems:** untwisted point-order sequence, full twisted table,
  and enhanced class.
- **Metrics:** unique fixed translation $g=a_q^{-k}$; inverse-convention
  check; triple $(1,1,a_q^{-1})$; action kernel; recovered coset; enhanced
  tuple $(1,1,a_q,1)$; twist order.
- **Setup details:** matrix inversion is exact modulo $q$; `A` and `A^-1`
  are separate fields.
- **Success criterion:** all twisted rows have exactly one fixing $g$; the
  effective regular action recovers exact $a_q$; no output identifies
  coefficient rings across different $q$.
- **Failure interpretation:** the positive retention boundary is not
  certified.
- **Table / figure target:** information hierarchy diagram.
- **Priority:** MUST-RUN.

### Block 4: Orbifold sectors and action-groupoid audit

- **Claim tested:** C1 and C2.
- **Why this block exists:** stabilizer/inertia data and dynamical period are
  distinct.
- **Dataset / split / task:** enumerate $X_q^g$ for every $g\in G_q$;
  construct the action-groupoid incidence data; verify the natural
  transformation with component $a_q$ from identity to $F_{a_q}$.
- **Compared systems:** enhanced carrier before reduction, enhanced
  orbifold fixed-sector output, and Morita quotient.
- **Metrics:** nonempty sector count; nonidentity sector count; quotient
  object count; automorphism count; naturality equalities; induced period.
- **Setup details:** for the regular torsor only the identity sector may be
  nonempty.  No general-purpose stack package or external category service
  is permitted.
- **Success criterion:** one nonempty identity sector, zero nonidentity
  sectors, quotient groupoid equivalent to a point, all naturality squares
  commute, and every reduced period is $1$.
- **Failure interpretation:** the free-stack collapse is not certified.
- **Table / figure target:** carrier-to-reduction flow.
- **Priority:** MUST-RUN.

### Block 5: General hierarchy controls and terminal A0 gate

- **Claim tested:** C2.
- **Why this block exists:** the final decision needs a direct
  proves-too-much control and an explicit counterexample to “effective action
  plus order-$r$ element implies a period-$r$ factor.”
- **Dataset / split / task:** apply the symbolic orbit-type formulas to the
  frozen abstract $C_6/C_2\sqcup C_6/C_3$ control; compare prime and
  composite rows; check exact period collisions.
- **Compared systems:** source, coarse quotient, point/orbit Burnside,
  orbifold, $C$-permutation kernel/twists, and inertia counts.
- **Metrics:** $d_K$; $[C:HK]$; action kernel; source factors; quotient
  factors; orbifold rational exponents; inertia sectors; period-collision
  pairs; composite pass count; external-operation counters.
- **Setup details:** the abstract control is hard-coded by the theorem as
  group order $6$ with subgroup orders $2,3$; it cannot seed a modulus or
  candidate search.
- **Success criterion:** effective kernel $1$; source factors exactly
  $(1-t^3)^{-1}(1-t^2)^{-1}$ with no support $6$; quotient factor
  $(1-t)^{-2}$; point-orbifold exponents $2/3$ and $3/2$; five static inertia
  sectors; $r_2=r_4=3$ and $r_6=r_9=12$; all four composite rows satisfy the
  same hierarchy; all forbidden counters are zero.
- **Failure interpretation:** the A0 certificate is not established.  A
  mismatch is terminal, not a tuning signal.
- **Table / figure target:** terminal decision table.
- **Priority:** MUST-RUN.

## Frozen Expected Results

| $q$ | $n_q$ | $r_q$ | $m_q$ | point support | orbit support | $\kappa$(point) exponent | $\Phi$(point) exponent | $\kappa$(orbit) exponent | $\Phi$(orbit) exponent | twisted triple | enhanced tuple | nonidentity sectors | stack period |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
| 2 | 3 | 3 | 1 | 3 | 1 | 1 | $1/3$ | 3 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 3 | 8 | 4 | 2 | 4 | 1 | 2 | $1/4$ | 8 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 5 | 20 | 10 | 2 | 10 | 1 | 2 | $1/10$ | 20 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 7 | 48 | 8 | 6 | 8 | 1 | 6 | $1/8$ | 48 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 11 | 100 | 5 | 20 | 5 | 1 | 20 | $1/5$ | 100 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 4 | 12 | 3 | 4 | 3 | 1 | 4 | $1/3$ | 12 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 6 | 24 | 12 | 2 | 12 | 1 | 2 | $1/12$ | 24 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 9 | 72 | 12 | 6 | 12 | 1 | 6 | $1/12$ | 72 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |
| 10 | 60 | 30 | 2 | 30 | 1 | 2 | $1/30$ | 60 | 1 | $(1,1,A^{-1})$ | $(1,1,A,1)$ | 0 | 1 |

The result must keep rational values as reduced integer pairs, e.g.
`{"numerator":1,"denominator":12}`.  No floating-point field is allowed.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision Gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | source package integrity | R000--R004 | fresh independent `SOURCE_LOCK_PASS` bound to all final hashes | CPU seconds | definition or hash drift |
| M1 | implementation and development controls | R010--R029 | all tests pass; abstract control cannot enter modulus tuple | under one CPU minute | conflating schemas or inverse convention |
| M2 | independent deployment audit | R030--R039 | reviewed execution tree and tests receive `DEPLOYMENT_PASS` | CPU minutes | hollow validators or shared implementation paths |
| M3 | sole registered exact audit | R100 | exactly one deterministic execution over the fixed nine moduli | under one CPU minute | any mismatch is terminal |
| M4 | independent result integrity | R110--R119 | read-only recomputation returns `RESULT_PASS` | CPU minutes | accidental rerun or unbound output |
| M5 | manuscript handoff | R120 | only after result pass and strict manifest closure | no new run | novelty/claim expansion |

The registered candidate is seedless.  Development tests may exercise the
abstract group control and malformed inputs, but cannot add an arithmetic
modulus.  No registered scientific rerun is allowed after a mismatch.

## Compute and Data Budget

- Total accelerator hours: **0**.
- Expected registered CPU time: **under one minute**.
- Largest fixed group: $|G_{11}|=100$.
- Largest twisted table: at most $100\times30$ exact translation checks.
- External data preparation: **none**.
- Human evaluation: independent source, code, result, asset, and manuscript
  reviews only.
- Biggest bottleneck: definition/provenance discipline, not compute.

## Result Artifact Contract

One later raw result must contain:

1. source-lock, code-tree, deployment-review, claim, and upstream hashes;
2. the unique matrix and exact ordered nine-modulus tuple;
3. separate namespaces for `point_burnside`, `orbit_burnside`,
   `g_permutation`, `enhanced`, `orbifold`, and `action_groupoid`;
4. every frozen integer/rational field in the expected table;
5. complete twisted fixing and sector summaries with independently verifiable
   witnesses;
6. the abstract $C_6$ control under `structural_unit_control`, never under
   `modulus_records`;
7. exact period-collision and composite controls;
8. `ambient_ring_varies_with_q=true`,
   `intrinsic_prime_selector=false`, and
   `external_modulus_specialization_required=true`;
9. zero forbidden-operation counters; and
10. the exact terminal certificate.

## Risks and Mitigations

- **Risk: the 2008 point-order and 2015 orbit-order zetas are conflated.**
  **Mitigation:** distinct data models, divisor inversions, and support gates.
- **Risk: the stronger 2013 invariant is omitted or reduced to order.**
  **Mitigation:** full $g\phi^k$ table and exact stabilizer triple.
- **Risk: $A$ versus $A^{-1}$ is swapped.**
  **Mitigation:** freeze the left action convention and require direct
  fixed-point witnesses.
- **Risk: inertia-sector count is called a clock.**
  **Mitigation:** every sector record contains induced period and identity
  transition; the trivial-action $BC$ boundary remains a nonclaim.
- **Risk: the abstract $C_6$ group becomes a tenth modulus.**
  **Mitigation:** separate schema namespace, no residue ring or matrix field,
  and a hard gate that `modulus_records` has length nine.
- **Risk: varying Burnside rings are silently identified.**
  **Mitigation:** group fingerprints and coefficient-ring IDs are mandatory;
  no cross-$q$ equality operator exists.
- **Risk: finite checks are treated as proof.**
  **Mitigation:** every all-$q$/general-$C$ claim is tagged `proof_only`.

## Final Checklist

- [ ] Main hierarchy table is covered.
- [ ] Point/order/permutation/enhanced definitions are separated.
- [ ] The $C_6$ effective no-full-period counterexample is exact.
- [ ] Orbifold and Morita boundaries retain stabilizer data without a clock.
- [ ] Prime and composite controls are fixed in advance.
- [ ] No numerical analytic variable is evaluated.
- [ ] Nice-to-have experiments are absent from the registered path.
- [ ] A pass cannot increase novelty or open Route B.
