# HCS-C22: chronology separation and signed-trace collapse in a two-letter Hénon skew product

**Date:** 2026-08-09
**Status:** **lineage closed** after the audited conditional C22G blueprint
**Candidate:** HCS-C22, promoted from HCS-C01; final continuation HCS-C22G
**Parent candidates:** HCS-C01 and `henon_h6_instability_roof_v1`
**Evidence ceiling:** exact theorem plus computer-assisted interval theorem;
Route-A exploratory

> **Final lineage update.** The graded continuation is audited and closed in
> [`../henon_graded_ruelle_complex/`](../henon_graded_ruelle_complex/).
> After correcting the BPS mixed-pinning direction and odd-unstable residue
> parity, the one-step domains and finite residue/exterior algebra are exact.
> The all-word vector-kernel trace, order-zero nuclearity, approximation
> property, and joint meromorphic continuation remain open, so
> \(D_{\rm inst}=D_1D_3/(D_0D_2)\) is conditional. The blueprint is retained
> as classical analytic infrastructure, not promoted as a new
> Hilbert--Pólya mechanism.

## Certified outcome

The completed C22 program produced five positive items and two exact
collapse/obstruction layers.

1. The two rational Hénon letters share one exactly certified local four-box
   survivor.  Every admissible bi-infinite joint parameter--state itinerary
   has exactly one complete orbit in the survivor, with uniform contraction
   and fibre hyperbolicity.
2. For the certified period-seven and period-eight protocol pairs, the
   complete local coefficient \(Q_w(1)\) distinguishes schedules having,
   respectively, identical cyclic parameter-bigram and parameter-trigram
   ledgers.  All 29 and 49 marked state branches are included.  This proves
   that parameter-only cyclic statistics through word length three do not
   determine these tested coefficients; it does not prove infinite memory
   or exclude every higher finite-memory cohomology.
3. With scheme multiplicity and the stated local-residue convention, the
   unit-numerator all-complex signed construction collapses to one, while the
   formal bare scheme zeta is \((1-4z)^{-1}\).
4. The pure instability Euler determinant has the exact repetition law,
   fixed-point logarithmic trace identity, and an explicit nonzero normal-
   convergence domain.  Its certified multiplier bases are
   \(E=3.0269439\ldots\) and \(U=7.7573085\ldots\); at \(s=1\) the theorem
   guarantees \(|z|<0.9353771\ldots\).
5. Both parameter letters share the same strict complex pinning disks, with
   minimum coordinate clearance \(7/5490\).
6. The normalized projective lift shares the disk \(|m|\le1/2\), maps it
   into \(|m|<125440/466211\), and admits one common right-half-plane
   logarithm for the oriented instability factor.  Each periodic base orbit
   has exactly one lifted unstable orbit in this domain.
7. A standard scalar pinning cocycle cannot reproduce the pure instability
   trace **orbit by orbit**: cancelling its fixed-point denominator on a
   primitive orbit is incompatible with its double repetition because
   \(|\det(I-M^2)|\ne|\det(I-M)|^2\) for every area-preserving saddle.

Thus the local instability determinant itself is now rigorous in its
pressure-side domain, but the frozen orbitwise geometric scalar construction
is closed.  This does not exclude an aggregate scalar trace identity based
on cancellations among different same-period orbits.  The authorized
large-step continuation is a genuinely different projective,
exterior-degree Ruelle--Lefschetz complex.  No scalar finite section or
longer orbit catalogue is authorized.

The T1--T3 proofs are in [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md).
The T4 theorem, common complex/projective domains, and orbitwise scalar T5 obstruction
are in [`T4_T5_DERIVATION.md`](T4_T5_DERIVATION.md).  The next-form gate is
frozen in [`GRADED_PIVOT_ROADMAP.md`](GRADED_PIVOT_ROADMAP.md).

## Frozen object

This project asks a deliberately narrower question than a general
nonautonomous-Hénon or random-zeta program.  It fixes the Paper-5 convention

\[
H_a(q,p)=(1-aq^2-p,q)
\]

and studies the autonomous skew product

\[
F(\omega,z)=(\sigma\omega,H_{a_{\omega_0}}z),
\qquad
a_-=\frac{59}{10},\quad a_+=\frac{61}{10},
\]

over the full two-shift.  The fibre return attached to a word
\(w=w_0\cdots w_{n-1}\) is always the chronological product

\[
F_w=H_{a_{w_{n-1}}}\circ\cdots\circ H_{a_{w_0}}.
\]

It is never replaced by a symbol-frequency average, an averaged transition
matrix, or an unordered product.

The selected research question is:

> For the autonomous two-letter Hénon skew product at
> \(a_-=59/10\) and \(a_+=61/10\), what chronological information survives
> after joint parameter--state primitive orbits are passed to an intrinsic
> stability-weighted dynamical determinant?

The intended result is a chronology **classification**, not a claim that the
system detects a physical time arrow.  The common reversor
\(R(q,p)=(p,q)\) forces reversal-related protocols to have the same pure
instability data.  Therefore the first nontrivial comparison is between
words that are neither cyclic rotations nor reversals of one another.

## Why this form was selected

Three dynamical forms were screened.

1. A periodically forced Floquet block is useful as a finite diagnostic, but
   its block determinant collapses to the monodromy determinant.  It is not
   the primary object.
2. A substitution or genuinely aperiodic base has no ordinary periodic-orbit
   zeta on the base; periodic approximants would mix two different clocks.
   This form is rejected for C22.
3. The full-shift skew product is autonomous and retains every ordered
   schedule word as an actual base periodic orbit.  This is the selected
   form.

This is the theorem-stage/operator-gate continuation of the already
registered HCS-C01 idea.  It is not a new claim that nonautonomous Hénon maps
can be chaotic; that question already has direct prior art.

## Falsifiable theorem program

The project advances only through the following large gates.

- **T1 -- common survivor:** certify one real four-rectangle survivor and
  one uniform hyperbolicity/contraction package for every
  \(a\in[59/10,61/10]\).
- **T2 -- chronology quotient:** enumerate joint parameter--state primitive
  necklaces and prove exactly which weights are invariant under cyclic
  rotation and reversal.  Exhibit a certified non-dihedral chronology
  witness or stop.
- **T3 -- collapse controls:** prove the bare and signed/global trace
  identities that are independent of protocol chronology.  These controls
  must be removed before interpreting any signal.
- **T4 -- intrinsic weighted determinant: PASS.** Define the instability-weighted
  cycle expansion with a fixed repetition rule and show convergence in a
  nonzero domain.
- **T5 -- analytic operator gate: SPLIT.** Construct a common complex pinning domain
  and a nuclear/trace-class ordered branch operator with a proved trace
  formula.  The common base and projective/log domains pass.  The ordinary
  orbitwise scalar denominator cancellation fails by an exact repetition
  obstruction.  C22 is now a scoped theorem/obstruction project and the
  authorized search has changed to a graded operator complex.

No numerical Ulam matrix, finite-memory truncation, or visually stable root
is allowed to substitute for T5.

## Stage-1 pilot signals, now superseded

These observations selected the formal targets.  Their current certified
status is recorded above and in the result artifacts.

- The signed-root recurrence

  \[
  (T_{\omega,\varepsilon}q)_i
  =\varepsilon_i
   \sqrt{\frac{1-q_{i-1}-q_{i+1}}{a_{\omega_i}}}
  \]

  is uniformly contractive on the inherited real sequence box with the
  now-proved bound
  \(\theta=\sqrt{240/1003}<0.49\).
- Exact rational covering arithmetic proves that the inherited four-box
  covering graph persists on
  \(289/50<a<99/16\), which contains both frozen parameters.  The tight
  candidate margins at the frozen endpoints are \(7/720\) and \(3/64\).
- The smallest primitive same-bigram, non-dihedral protocol pair is

  \[
  0000101,\qquad 0001001.
  \]

  The originally selected branch \(++--+--\) remains a numerical pilot and
  is not used as the theorem.  The released theorem instead certifies the
  complete 29-branch aggregate by rational intervals.  Its branch-level
  instability-length difference, approximately
  \(1.7210945\times10^{-2}\), is retained only as the historical target
  selection; no separate branch-level theorem is claimed.
- At the actual rational parameters, reduction modulo \(43\) gives an exact
  chronology witness: one fixed point of the first protocol has monodromy
  trace \(15\), while one fixed point of the second has trace \(18\).
  The finite-field witness remains a control; the real local survivor and
  aggregate zeta-coefficient difference are now independently certified.

All pilot labels and their limitations are recorded in
[`notes/PILOT_LEDGER.md`](notes/PILOT_LEDGER.md).

## Route-A expectation

The honest current ceiling is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall status `ROUTE_A_EXPLORATORY`.  Even a rigorous internal nuclear
dynamical determinant would not by itself pass Route-A A2: no target divisor,
arithmetic normalization, or sealed target comparison has been supplied.
Route B is not authorized by this project.

## Project map

- [`RESEARCH_QUESTION.md`](RESEARCH_QUESTION.md): scope, FINER audit, and
  frozen definitions.
- [`EXPERIMENT_PLAN.md`](EXPERIMENT_PLAN.md): theorem/experiment gates,
  controls, kill rules, and reproducibility contract.
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md): Paper-5 lock, repository novelty
  boundary, and external prior art.
- [`DEVILS_ADVOCATE_CHECKPOINT1.md`](DEVILS_ADVOCATE_CHECKPOINT1.md): first
  adversarial review.
- [`DEVILS_ADVOCATE_CHECKPOINT2.md`](DEVILS_ADVOCATE_CHECKPOINT2.md):
  post-certificate adversarial decision.
- [`DEVILS_ADVOCATE_CHECKPOINT3.md`](DEVILS_ADVOCATE_CHECKPOINT3.md):
  post-T4/orbitwise-scalar-T5 closure and final graded kill rule.
- [`notes/PILOT_LEDGER.md`](notes/PILOT_LEDGER.md): exact and numerical pilot
  evidence with explicit status labels.
- [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md): T1--T3 theorem proofs.
- [`T4_T5_DERIVATION.md`](T4_T5_DERIVATION.md): T4 convergence theorem,
  complex/projective certificates, and orbitwise scalar T5 no-go theorem.
- [`GRADED_PIVOT_ROADMAP.md`](GRADED_PIVOT_ROADMAP.md): audited graded-form
  closure and its unresolved nuclear/supertrace gates.
- [`RESEARCH_SYNTHESIS.md`](RESEARCH_SYNTHESIS.md): interpretation and pivot
  decision.
- [`evaluations/route_a/hcs_c22/20260809T081750Z.yaml`](evaluations/route_a/hcs_c22/20260809T081750Z.yaml):
  current post-T4 conservative Route-A record; the earlier YAML remains a
  historical pre-T4 evaluation.
- [`REPOSITORY_UPDATE.md`](REPOSITORY_UPDATE.md): source commit, release tag,
  and verification handoff.
- [`results/RESULTS.md`](results/RESULTS.md): compact T1--T3 statement.
- [`results/T4_T5_RESULTS.md`](results/T4_T5_RESULTS.md): compact T4/T5 gate
  result and artifact map.
- [`code/README.md`](code/README.md), [`results/README.md`](results/README.md),
  and [`paper/README.md`](paper/README.md): implementation, evidence, and
  manuscript contracts.

## Stop/pivot rule

The orbitwise geometric scalar project has stopped at its predeclared T5 kill
rule.
The graded pivot did not spend a long round polishing finite sections. Its
predeclared stop conditions included:

- no common real survivor for the frozen parameter interval;
- no non-dihedral difference after complete local orbit aggregation;
- no common lifted branch domain or no trace-compatible graded nuclear
  operator;
- an extra stable projective fixed point enters the certified slope domain;
- the alternating construction is only a routine, non-effective
  specialization of the primary literature;
- the only surviving claim is already a standard consequence of an existing
  nonautonomous horseshoe theorem.

The theorem audit found that the all-word and nuclear gates had not actually
been proved, and the eventual mechanism was in any case classical. The C22G
operator lineage is therefore closed rather than silently changing its
determinant or returning to Ulam/cycle-section numerics. The scalar no-go
retains its exact orbitwise scope and still leaves aggregate scalar
representations unexcluded.
