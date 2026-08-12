# Paper Plan

**Title**: Exact Clock Decoding and Periodic Factors of a Graded Wheel-Sieve
Shift

**Short title**: Periodic-Clock Obstructions for Wheel-Sieve Recodings

**One-sentence contribution**: We turn the endogenous prime multiplier of a
graded wheel-sieve shift into a precise inheritance test and prove that exact
single-valued decoding excludes periodic semiconjugate images and, under an
explicit lag-pair condition, periodic points newly created in orbit closures.

**Format**: anonymous, shareable theorem note; not yet targeted to a specific
venue

**Date**: 2026-08-12

**Primary family**: Symbolic Dynamics only

**Evidence policy**: complete proofs and explicit mathematical controls; no
numerical experiment

**Target length**: 8--11 pages including references and appendices

**Route status**: Route-A theorem obstruction; Route B locked; no determinant

## Claims--evidence matrix

| ID | Manuscript claim | Evidence to include | Scope sentence required | Main location |
|---|---|---|---|---|
| C0 | The wheel recurrence produces the rational primes and hence an injectively drifting exact clock. | Restate the recurrence; cite and summarize the prime-enumeration lemma from Paper 01. | This is an upstream theorem for the frozen source, not a new result on prime distribution. | Section 2 |
| C1 | A decoder \(d:\pi(X)\to C\) with \(d\circ\pi=\kappa\) exists iff \(\kappa\) is constant on \(\pi\)-fibers. | Two-line necessity and sufficiency proof. | Single-valued exact decoding is stronger than choosing a clock separately for each lift. | Section 3.1 |
| C2 | An exact-clock shift-compatible image has no periodic point; a surjective exact-clock factor is aperiodic. | Fiber-collision proof and coboundary telescoping restatement. | No topology or locality is assumed; exact decoding and semiconjugacy are essential. | Section 3.2 |
| C3 | A continuous total decoder excludes periodic points in \(Y_0=\overline{\pi(X)}\) when every lag-pair closure avoids the diagonal. | Define \(E_m\) and \(F_m=(d,d\circ S^m)\); use density and continuity. | Continuity alone is not enough in a compactified clock codomain. | Section 4.1 |
| C4 | A compact phase space cannot continuously decode the unbounded exact clock into \(\mathbb N_{\rm disc}\). | Compact-image and finite-discrete-subset proof. | Distinguish compact target phase space from compactification of the clock codomain. | Section 4.2 |
| C5 | Every major hypothesis has an explicit deletion control, and nonrecurrence is sharp. | One-point factor, level-mod-\(m\) cycle, partial or discontinuous boundary decoder, one-point clock compactification, periodic control clock. | The controls regain cycles by losing a frozen inheritance hypothesis; none rescues the original mechanism. | Section 5 |
| C6 | \(\tau=\log\kappa\) is obstructed as an inherited absolute label, whereas an ordinary positive suspension roof can coexist with a periodic base. | Distinguish absolute labels, differences, and accumulated roof sums; cite Parry–Pollicott for the standard roof framework. | No general no-go theorem for roofs or suspension flows is claimed. | Section 6.1 |
| C7 | The frozen exact-clock stationarization class receives **THEOREM_STOP**, while determinant gates remain unavailable. | Route-A status table tied to C2--C5. | The stop is not transferred to independently defined symbolic grammars. | Section 6.2 |

## Core theorem statements

### Theorem A: direct exact-clock image obstruction

Let \((X,\sigma)\) carry a clock \(\kappa:X\to C\) such that

\[
\kappa(\sigma^m x)\ne\kappa(x)
\qquad
(x\in X,\ m\ge1).
\]

Let \(\pi:X\to Y\) and \(S:Y\to Y\) satisfy
\(\pi\circ\sigma=S\circ\pi\). If a function
\(d:\pi(X)\to C\) satisfies \(d\circ\pi=\kappa\), then

\[
\pi(X)\cap\operatorname{Per}_m(S)=\varnothing
\qquad
(m\ge1).
\]

No topology is part of this statement. The wheel corollary substitutes
\(\kappa(x)=q_{\ell(x)+1}\).

### Theorem B: continuous closure obstruction

Let \(Y_0=\overline{\pi(X)}\). Let \(S:Y_0\to Y_0\) and
\(d:Y_0\to C\) be continuous, and retain semiconjugacy and exactness on the
image. For every \(m\ge1\), assume

\[
\overline{
  \{(\kappa(x),\kappa(\sigma^m x)):x\in X\}
}
\cap\Delta_C
=\varnothing.
\]

Then

\[
Y_0\cap\operatorname{Per}_m(S)=\varnothing
\qquad
(m\ge1).
\]

The proof must use general neighborhoods and density, not sequences, so no
hidden first-countability assumption enters.

### Corollary: wheel integer and logarithmic clocks

Theorem B applies to:

- \(C=\mathbb N\) with the discrete topology and clock \(q_{k+1}\);
- \(C=\mathbb R\) with the usual topology and clock \(q_{k+1}\); and
- \(C=\mathbb R\) with the usual topology and clock \(\log q_{k+1}\).

For the real cases, state that the lag-pair set is locally finite and both
coordinates escape to \(+\infty\). Do not rely on a false uniform-gap claim
for \(\log q_{k+m+1}-\log q_{k+1}\).

### Proposition: compact phase-space obstruction

If \(Y_0\) is compact and \(d:Y_0\to\mathbb N_{\rm disc}\) is continuous,
then \(d(Y_0)\) is finite. Thus \(d\circ\pi=\kappa\) is impossible for the
unbounded wheel clock. Present this as a feasibility corollary, not as a
periodic-point theorem.

## Manuscript structure

### Abstract (170--220 words)

- Name the source: the graded wheel-sieve tail-path system with endogenous
  prime multiplier clock.
- State Theorems A and B in plain language.
- State the compact phase-space corollary.
- Name the sharpness control: compactifying the clock at infinity permits a
  continuous decoder and boundary fixed point because lag-pair separation
  fails.
- Include one provenance sentence: the periodic-coboundary mechanism is
  classical; the contribution is the wheel-specific stationarization package.
- End with the scoped decision: **THEOREM_STOP** for exact-clock inheritance,
  no determinant, Route B locked.

### Section 1: Introduction and positioning (1--1.25 pages)

- Motivate the exact question: whether the source's endogenous prime clock can
  survive passage from strict grading to periodic symbolic dynamics.
- State the contribution before historical context.
- List Theorems A and B, the compactness corollary, and the control suite.
- Place the hero hypothesis map after the contribution list.
- Give the novelty disclaimer prominently:
  - telescoping of coboundaries on periodic orbits is classical;
  - no universal Livšic theorem is claimed;
  - the contribution is the source-specific obstruction package.
- Position Heeren (2026) as direct prior art and remove all “first symbolic
  prime sieve” language.
- State that there is no numerical experiment and no determinant.

### Section 2: Frozen wheel source and admissible inheritance (1 page)

- Restate \(Q_k,q_k\), the prime-enumeration theorem from Paper 01, the graded
  path space, and strict level advance.
- Define \(\ell\), \(\kappa=q_{\ell+1}\), and
  \(\tau=\log\kappa\).
- Define semiconjugacy, semiconjugate image, factor, orbit closure, exact
  decoder, and total decoder.
- State the autonomous single-valued rule: one target state cannot select a
  different value based on an unrecorded source lift.
- Include a scope table for direct images, closures, and arbitrary or post-hoc
  observations.

### Section 3: Direct images, fibers, and periodic coboundaries (1--1.25 pages)

#### Section 3.1: Fiber-consistency lemma

- Prove \(d\circ\pi=\kappa\) iff \(\kappa\) is constant on
  \(\pi\)-fibers.
- Explain that any path-window implementation is covered once it defines one
  function of the target path state.

#### Section 3.2: Theorem A

- Give the one-line fiber proof.
- Derive the surjective-factor corollary.
- Add the reformulation \(a=d\circ S-d\), whose cycle sum telescopes.
- Cite Livšic only for the classical cohomological framework and
  Boyle–Handelman only for ordered cohomology and finite-orbit traces.
- Say explicitly that no converse theorem or hyperbolicity is used.

### Section 4: Orbit closures and clock topology (1.5 pages)

#### Section 4.1: Theorem B

- Define \(E_m\) and \(\Delta_C\).
- Prove
  \(F_m(Y_0)\subseteq\overline{E_m}\) using continuity and density.
- Derive the contradiction at a periodic point.
- Verify the hypotheses separately for discrete \(q\), real \(q\), and real
  \(\log q\).

#### Section 4.2: Compact target phase spaces

- Prove the finite-image corollary for a compact phase space and a discrete
  clock codomain.
- Explain that this is an impossibility of exact continuous decoding, not
  merely an exclusion of periodic points.

#### Section 4.3: Why compactifying the clock changes the answer

- Give
  \(Y=\{0\}\cup\{(k+1)^{-1}:k\ge0\}\), its continuous shift, and fixed point.
- First show that the \(\mathbb N_{\rm disc}\)-decoder cannot extend
  continuously.
- Then compactify to \(\mathbb N\cup\{\infty\}\), extend continuously, and
  show that \(\overline{E_m}\) meets the diagonal at
  \((\infty,\infty)\).
- State that continuity is not a substitute for diagonal separation.

### Section 5: Adversarial controls and sharpness (1--1.25 pages)

Present one assumption-deletion table followed by the constructions.

1. Clock erasure: a constant factor with a fixed point.
2. Level wrapping: the \(\ell\bmod m\) factor with an \(m\)-cycle and no
   exact prime decoder.
3. Partial decoder: exact on the dense image, undefined at the boundary fixed
   point.
4. Discontinuous extension: an arbitrary finite boundary label.
5. Clock compactification: a continuous \(\infty\)-valued boundary label for
   which diagonal separation fails.
6. Periodic control clock: \(c_{k+m}=c_k\) admits an exact decoder on the
   level-mod-\(m\) factor.
7. Broken semiconjugacy and independent orbit labels: classify these as new
   mechanisms, not counterexamples.

End with the sharpness sentence: the abstract lemma depends on clock
nonrecurrence, not primality; wheel arithmetic proves that the endogenous
source clock has that property.

### Section 6: Interpretation and route decision (1 page)

#### Section 6.1: Roof versus absolute clock

- Cite Parry–Pollicott for the standard suspension and periodic-orbit
  framework.
- Distinguish:
  - an absolute label \(\tau(y)\), which exact decoding forces to agree when a
    state repeats;
  - an increment \(d\circ S-d\), whose cycle sum is zero; and
  - a positive roof \(r(y)\), whose cycle sum is the nonzero closed-orbit
    length.
- State that a periodic base with a roof is allowed.
- Classify an independently assigned \(\log p\) target roof as a new A0
  mechanism.

#### Section 6.2: Route A and Route B

- Give the A0--A4 table from the narrative report.
- Record **THEOREM_STOP** only for the frozen inheritance mechanism.
- Record: determinant convention not defined; A2 not testable; Route-B
  invocation not allowed.
- Do not create a candidate identifier or candidate YAML.

### Section 7: Conclusion and limitations (0.5 page)

- Reprise the direct-image, closure, and compact-target conclusions.
- State the classical-mechanism/source-specific-contribution distinction one
  final time.
- Name the open boundary: independently defined symbolic arithmetic grammars
  that do not inherit this clock.
- Reaffirm that crossing this boundary requires a new source lock and A0
  proof, not reuse of the present result.

### Appendix A: Proof-dependency audit

- Map each conclusion to semiconjugacy, exactness, totality, continuity, and
  diagonal separation.
- Record which hypotheses are absent from Theorem A.
- Include the nonmetrizable-density justification for Theorem B.

### Appendix B: Literature and priority statement

- Give the five-source ledger in compact form.
- State that the elementary coboundary obstruction is not claimed as novel.
- State the Heeren direct-prior collision and revised novelty language.

## Figure plan

| ID | Type | Description | Source | Priority |
|---|---|---|---|---|
| Fig. 1 | Parallel hypothesis map | From the graded wheel source, show: exact image \(\rightarrow\) fiber collision; continuous closure plus lag separation \(\rightarrow\) no boundary cycle; assumption deletion \(\rightarrow\) cycles without inherited clock. Add an inset distinguishing phase-space compactness from clock compactification. | Pure TikZ; no data | High |

### Figure 1 caption draft

“The obstruction is an inheritance theorem, not a blanket prohibition of
periodic factors. An exact semiconjugate image cannot close because a
revisited target state would have to decode two distinct wheel primes. The
same conclusion extends to an orbit closure only when continuous decoded lag
pairs remain separated from the diagonal. Deleting exactness or compactifying
the clock restores cycles but does not preserve the frozen prime clock under
the theorem's hypotheses.”

## Table plan

| ID | Content | Purpose |
|---|---|---|
| Table 1 | Theorem scope: image, closure, compact target | Prevent assumptions from leaking between results |
| Table 2 | Hypothesis-deletion controls | Make sharpness and counterexamples auditable |
| Table 3 | Route-A gate outcomes | Separate the theorem stop from analytic claims |

## Citation plan

Use only verified metadata and give every citation one limited job.

- Hedlund 1969: continuous shift-commuting local coding context only.
- Livšic 1972: cohomological framework and periodic-orbit obstruction; only
  the necessary telescoping direction is used.
- Parry–Pollicott 1990: suspension roofs, periodic-orbit sums, and zeta
  context; no determinant is imported.
- Boyle–Handelman 1996: ordered cohomology and finite-orbit evaluation for
  zero-dimensional dynamics.
- Heeren 2026 SSRN: direct topical prior for an endogenous non-stationary
  symbolic sieve; identify it as a working paper and avoid priority claims.

No source is cited as proving the wheel-specific theorem. Its proofs are
self-contained apart from the upstream prime-enumeration result.

## Style and sharing checks

- Author block: Anonymous Authors.
- No affiliation, repository URL, internal filesystem path, or private data.
- Define project labels before using them, or put them in a separate
  research-status subsection.
- Put mathematical conclusions before project governance in the abstract and
  introduction.
- Use “semiconjugate image” for the non-surjective case and “factor” only when
  surjectivity is present.
- Never write that factors preserve aperiodicity without the exact-decoder
  qualifier.
- Never call \(\tau=\log\kappa\) a suspension roof without explaining that it
  is frozen as an absolute inherited label.
- Identify Heeren 2026 as non-peer-reviewed working-paper prior art.
- Do not include an empirical-results section.

## Phase checkpoints

- [x] Source lock and proof package.
- [x] Literature audit and novelty boundary.
- [x] Narrative report and claims--evidence matrix.
- [x] Structural paper plan.
- [x] Pure TikZ hypothesis map.
- [x] Modular LaTeX manuscript and verified bibliography.
- [x] PDF compilation and static checks.
- [x] Independent improvement Round 1.
- [x] Independent improvement Round 2.
- [x] Root README summary and per-paper manifest.

Repository commit, push, and workspace synchronization are release-handoff
operations outside the paper build and are reported with the final delivery.

## ROUND2_CLUE

A genuinely new periodic arithmetic grammar that does not decode the wheel
clock requires its own symbolic source lock and A0 proof. It is not developed,
tested, or used as evidence in this paper.
