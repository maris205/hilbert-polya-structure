# Experiment Plan

**Problem**: certify prime-order exact-period torsion capacity for a frozen
cat map, then test whether the torsion-order observable has arithmetic
specificity and local regularity.

**Method thesis**: primitive determinant divisors give exact-period
prime-order carriers, but the natural order clock over-generates all integers
and is not a regular local observable.

**Date**: 2026-08-14.

## Evidentiary hierarchy

The all-period carrier statements and the clock obstruction are proofs.  The
registered computation, if independently authorized, is an exact
proof-contract audit and a reproduction of a fixed determinant ledger.  It
cannot establish the imported primitive-divisor theorem, prove a new
all-period statement from a cutoff, or supply a Route-A A2--A4 result.

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1: hyperbolic toral automorphisms in \(\mathrm{SL}_2(\mathbb Z)\) have prime-order exact-period carriers for all \(n>12\), and the frozen cat has them exactly for \(n\notin\{1,6,12\}\) | Distinguishes exact torsion capacity from mere determinant divisibility | Flatters applicability; kernel least-period lemma; negative-trace parity lemma; exact \(n\le12\) ledger; complete modulo \(2,3,5\) boundary proof | B1, B2, B3 |
| C2: the invariant order clock is non-specific and nonregular, while native monodromy cannot recover the carrier prime | Prevents a carrier theorem from being promoted to a prime clock | Exact all-order range; coprime perturbation proof; Birkhoff-sum identity; constant-derivative calculation | B4, B5 |

Anti-claims to rule out:

- absence of a primitive divisor means absence of an exact-period carrier;
- a finite determinant ledger proves the \(n>12\) result;
- internally occurring prime orders imply a prime-specific range or a
  prime-orbit bijection;
- cat-map monodromy, transfer, or quantization automatically reads the
  torsion-order prime.

## Paper Storyline

- Main paper must prove C1 and C2 and preserve their logical separation.
- Appendix may contain the exact recurrence ledger, kernel dimensions, and
  machine-readable proof contract.
- Experiments intentionally cut: random parameter scans, large period
  searches, prime-density statistics, zero matching, transfer/Fredholm
  construction, quantum cat-map numerics, and any post-null period extension.

## Experiment Blocks

### Block B1: Norm/determinant and primitive-period bridge

- Claim tested: C1 general theorem.
- Why this block exists: checks every hypothesis and implication in the
  Flatters-to-torus reduction.
- Task: symbolically verify the characteristic polynomial, norm-one unit,
  determinant/norm identity, finite-field kernel least-period lemma, and the
  three negative-trace parity cases for \(B=-M\).
- Compared systems: generic symbolic \(t>2\), generic symbolic \(t<-2\),
  and frozen trace \(t=3\).
- Metrics: Boolean proof-contract gates; exact symbolic identity residuals.
- Setup details: exact integer/polynomial arithmetic only; no prime values or
  orbit search.
- Success criterion: every assumption is explicit, the lemma distinguishes
  determinant primitivity from point-period primitivity, and the
  \(n\equiv2\pmod4\) branch uses index \(n/2\), not index \(n\).
- Failure interpretation: weaken or reject the general carrier claim; no
  finite experiment may repair it.
- Table/figure target: main theorem dependency diagram.
- Priority: MUST-RUN.

### Block B2: Frozen determinant and primitive-divisor ledger

- Claim tested: C1 small positive cases and exception set.
- Why this block exists: reproduces the fixed \(n=1,\ldots,12\) arithmetic
  ledger without selecting primes after inspection.
- Task: generate \(s_0=2,s_1=3,s_{n+2}=3s_{n+1}-s_n\), set
  \(\Delta_n=2-s_n\), and exactly factor only the twelve predeclared
  integers in the source lock.  For every factor, record its first determinant
  appearance.
- Compared systems: recurrence engine and direct exact matrix-power engine.
- Metrics: exact agreement of determinants, factorizations, supports, first
  appearances, and selected primitive divisors.
- Setup details: internally generated exact factoring of these fixed integers
  only; no external prime table and no periods beyond twelve.
- Success criterion: byte-stable ledger matches the source-locked values and
  the two engines agree.
- Failure interpretation: halt; do not alter the ledger, cutoff, or selected
  factors.
- Table/figure target: main classification table.
- Priority: MUST-RUN.

### Block B3: Jordan repair and exhaustive exclusions

- Claim tested: C1 exact classification at \(n=1,6,10,12\).
- Why this block exists: primitive-divisor absence is not a carrier
  exclusion, as \(n=10\) demonstrates.
- Task: exact arithmetic in \(\mathbb F_2^2,\mathbb F_3^2,\mathbb F_5^2\);
  verify \(A^3=I\) modulo two, \(A^2=-I\) modulo three, and
  \(A=-I+N,N^2=0,\operatorname{rank}N=1\) modulo five.  Enumerate the at most
  24 nonzero vectors only as a control and cross-check the analytic period
  classification.
- Metrics: exact vector-period multiset; analytic/enumerative agreement;
  period-ten count \(20\) points and \(2\) cycles; zero carriers at six and
  twelve.
- Success criterion: all prime supports of \(\Delta_6\) and
  \(\Delta_{12}\) are exhausted, and the nonkernel modulo-five vectors have
  exact period ten.
- Failure interpretation: halt and reject the exact classification.
- Table/figure target: boundary-case table.
- Priority: MUST-RUN.

### Block B4: Order-clock capacity and regularity

- Claim tested: C2.
- Why this block exists: distinguishes prime availability from arithmetic
  specificity.
- Task: encode proof contracts for order preservation, the exact-order point
  \((1/m,0)\), the coprime perturbation
  \(x+(1/N,0)\), and the formula
  \(\operatorname{ord}(x+(1/N,0))=mN\).
- Compared systems: symbolic arbitrary \(m,N\) with \(\gcd(m,N)=1\); tiny
  formal controls may instantiate fixed composite labels but never query a
  prime list.
- Metrics: Boolean identity gates and exact gcd conditions.
- Success criterion: full integer range and neighborhood unboundedness are
  certified by proof, not sampling.
- Failure interpretation: narrow the specificity obstruction while retaining
  any independently valid carrier theorem.
- Table/figure target: capacity-versus-specificity schematic.
- Priority: MUST-RUN.

### Block B5: Orbit sum and native monodromy

- Claim tested: C2.
- Why this block exists: prevents the global order label from being confused
  with an additive local clock or derivative multiplier.
- Task: verify \(S_nL=nL\), \(D(T_A^n)=A^n\), and the spectrum
  \(\{\alpha^n,\alpha^{-n}\}\) symbolically.
- Metrics: exact identity gates; dependence signature
  `orbit_sum=(n,order)`, `monodromy=(n only)`.
- Success criterion: no code or prose path identifies \(n\log p\) with
  \(\log p\), or \(n\log\alpha\) with a torsion-order readout.
- Failure interpretation: halt the Route-A classification and repair the
  semantic layer.
- Table/figure target: comparison table in the main paper.
- Priority: MUST-RUN.

## Frozen controls

| Control | Exact prediction | Role |
|---|---|---|
| K001 determinant convention | \(\Delta_n=\det(A^n-I)=2-s_n<0\) for \(n\ge1\) | catches sign and fixed-point-count confusion |
| K002 primitive transfer | a primitive factor at \(n\) forces every nonzero kernel vector to exact period \(n\) | positive bridge control |
| K003 nonprimitive carrier | modulo-five nonkernel vectors have exact period ten although \(\Delta_{10}\) has no primitive divisor | prevents converse error |
| K004 exception completeness | supports \(\{2,5\}\) at six and \(\{2,3,5\}\) at twelve yield no exact periods six/twelve | negative classification control |
| K005 all-integer overgeneration | \((1/m,0)\) has order \(m\) for arbitrary symbolic \(m\) | composite/specificity control |
| K006 discontinuity | for \(N=km+1\), \(x+(1/N,0)\to x\) and has order \(mN\) | regularity boundary |
| K007 monodromy blindness | all period-\(n\) points have derivative \(A^n\) | prime-label independence control |
| K008 negative-trace parity | odd \(n\) uses primitive index \(2n\), \(4\mid n\) uses \(n\), and \(n\equiv2\pmod4\) uses \(n/2\) | rejects the half-period shortcut |

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | immutable preflight | R000--R003 | source/proof hashes, forbidden-data scan, and schema all pass | seconds, CPU | mutable or unsafe input |
| M1 | proof contract | R010--R012 | B1, imported-theorem hypotheses, and parity conversion pass | seconds, CPU | invalid negative-trace index selection |
| M2 | frozen ledger | R020--R022 | B2 dual-engine and exact factor ledger agree | seconds, CPU | sign or first-appearance error |
| M3 | decisive boundaries | R030--R033 | B3 analytic/enumerative engines agree | seconds, CPU | missing prime support or Jordan-period error |
| M4 | specificity | R040--R043 | B4--B5 exact identities pass | seconds, CPU | vague “nonlocal” prose exceeds proved discontinuity |
| M5 | closure | R090--R100 | strict manifest and independent review pass | minutes, CPU | result overclaim |

## Stop/go policy

- No registered audit before an independent code-review
  `DEPLOYMENT_PASS` bound to the current source-lock and code-tree hashes.
- Any source hash, determinant, factorization, first-appearance, finite-field
  period, kernel count, proof-contract, or dual-engine disagreement halts.
- A new carrier at period six or twelve is a theorem-level contradiction and
  halts immediately; no continuation or cutoff repair is allowed.
- Periods beyond twelve may not be scanned.  Their conclusion comes only from
  the imported primitive-divisor theorem and Lemma 1.
- The twelve fixed factorizations may be recomputed internally only after
  lock.  No external prime table or generated target array may be loaded.
- A passing carrier audit does not open prime/zero matching, zeta/Fredholm,
  transfer, quantization, Route-A A2--A4, or Route B.
- The intended terminal label after a full pass is
  `INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`.

## Compute and Data Budget

- GPU-hours: zero.
- CPU: deterministic single-process exact arithmetic; expected registered
  runtime below one minute.
- Memory: below 1 GiB.
- External data: none during registered execution.
- Bibliographic sources: allowed for theorem attribution before lock; never
  parsed as candidate targets.
- Stochastic seeds and human evaluation: not applicable.

## Risks and Mitigations

- Risk: treating no primitive divisor as no exact carrier.
  Mitigation: mandatory modulo-five period-ten counter-control.
- Risk: attributing negative trace directly to Flatters or using
  \(\Delta_n(-M)\) when \(n\equiv2\pmod4\).
  Mitigation: freeze the three parity branches and require the
  \(n/2\) index plus Theorem 3.1 at \(n/2\in\{7,9,11\}\).
- Risk: calling a finite ledger an all-period proof.
  Mitigation: result schema records proof provenance separately from audited
  periods.
- Risk: claiming an order label is a regular point potential.
  Mitigation: neighborhood-unboundedness proof and no-extension nonclaim.
- Risk: cat-map quantization literature being read as a quantization of this
  clock.
  Mitigation: explicit no-transfer/no-quantization boundary.

## Final Checklist

- [x] Main theorem claims are frozen.
- [x] Positive- and negative-trace proof paths are explicit and separate.
- [x] Exact-period and primitive-divisor semantics are separated.
- [x] The full small determinant ledger is predeclared.
- [x] Nonprimitive period ten and exclusion periods six/twelve are mandatory.
- [x] Composite overgeneration and local regularity are tested by theorem.
- [x] Transfer, zeta, zero, and quantization experiments are intentionally cut.
- [x] Independent proof and novelty inputs have been incorporated, including
  an independent PASS on the repaired negative-trace parity lemma.
- [ ] Independent pre-execution code review has authorized a registered audit.
