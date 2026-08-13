# Experiment Plan

**Problem**: determine whether tensor-factorization supplies an intrinsic
grading and a genuine analytic dual determinant, rather than only a formal
Euler identity.

**Method thesis**: factorization topology fixes the Möbius grading exactly;
group-completion inversion fixes finite (s\leftrightarrow1-s) symmetry, but
only a nonempty relative trace-class domain would constitute A3 progress.

**Date**: 2026-08-13

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Blocks |
|---|---|---|---|
| C1: grading is intrinsic | prevents hand-assigned signs | exact chain complex, (\partial^2=0), Euler/homology parity (=\mu) at every cutoff | B1–B2 |
| C2: duality is analytic, not merely formal | required for A3 | common or relative trace-class theorem on a nonempty open set | B3–B4 |
| Anti-claim: any parity or UFD works | detects proves-too-much | parity-flip, random, shifted, additive and free-mixing controls | B2, B5 |

## Paper Storyline

- Main paper must establish the exact grading theorem and decide the nuclear
  overlap gate.
- Appendix may contain full chain ledgers and cutoff tables.
- Zero fitting, broad parameter searches, and cross-family models are cut.

## Experiment Blocks

### B1 — exact factorization complexes

- Claim tested: C1.
- Task: build divisor intervals for all (n\le N), enumerate simplices or an
  equivalent normalized chain basis, verify (\partial^2=0), Betti numbers,
  and reduced Euler characteristic.
- Cutoffs: (N=64,128,256,512), reduced only if exact enumeration exceeds
  the recorded CPU budget.
- Metrics: boundary failures, Euler–Möbius mismatches, homology mismatches,
  maximum chain dimension and chain count.
- Success: zero exact mismatches at every reported cutoff.
- Failure: factorization-poset grading is not the claimed canonical source.
- Priority: MUST-RUN.

### B2 — graded trace and parity controls

- Claim tested: C1 and anti-claim.
- Systems: canonical reduced degree, global parity flip, deterministic random
  parity, total prime-factor count with multiplicity, squarefree exterior
  degree, shifted monoid, additive monoid.
- Metrics: exact (\mu(n)) prefix accuracy; exact supertrace coefficients;
  invariance under atom relabeling; orientation ambiguity flag.
- Success: canonical topology uniquely recovers (mu) up to a reported
  global suspension; controls do not receive orientation credit.
- Failure: the mechanism proves too much or the source cannot select parity.
- Priority: MUST-RUN.

### B3 — finite dual determinant identities

- Claim tested: algebraic part of C2.
- Task: compute (R_P(s)) for nested atom cutoffs on a preregistered grid,
  verify (R_P(1-s)R_P(s)=1) and unit modulus on the critical line.
- Grid: rational/complex points chosen before any target comparison; no zeta
  zeros.
- Metrics: symmetry residual, modulus residual, cutoff phase drift.
- Success: exact/specified-precision finite identities; all drift reported.
- Failure: implementation error only; finite success is not A3 evidence.
- Priority: MUST-RUN.

### B4 — common and relative nuclear diagnostics

- Claim tested: decisive part of C2.
- Task: compute singular-value sums for the (s), (1-s), difference, and
  relative-ratio diagonal sectors across cutoffs; pair with an analytic
  convergence/divergence proof.
- Metrics: partial trace norms and fitted growth only as diagnostics; theorem
  status reported separately.
- Success: bounded trace norm on a predeclared open set plus proof.
- Failure: divergence or no open set gives `SCOPED THEOREM STOP` for the naive
  dual complex.
- Priority: MUST-RUN.

### B5 — positive mixing and shifted-law controls

- Claim tested: anti-claim.
- Task: repeat the Paper-04 semiprime check with canonical, random, and
  factor-count signs; report whether any sign is genuinely derived from a
  boundary complex.
- Success: only source-derived cancellations receive credit.
- Failure: arbitrary signs perform equally and no source selector exists.
- Priority: MUST-RUN.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | chain sanity | (n\le32), hand-check (p,p^2,pq,pqr) | (\partial^2=0) and correct empty-complex convention | minutes CPU | sign normalization |
| M1 | exact prefix | B1 at all feasible cutoffs | zero Euler/homology mismatch | minutes–hours CPU | chain explosion |
| M2 | controls | B2 and B5 | canonical source separates from arbitrary parity | minutes CPU | proves-too-much |
| M3 | duality | B3 | exact finite symmetry, full phase drift | minutes CPU | false convergence narrative |
| M4 | analytic stop/go | B4 plus theorem | nonempty relative nuclear domain or scoped stop | theorem-led | cancellation not trace class |

## Compute and Data Budget

- CPU only; no GPU.
- Standard library plus exact integer/rational linear algebra where feasible.
- No external datasets and no Riemann-zero data.
- Biggest bottleneck: explicit simplicial-chain enumeration for highly
  composite (n); an equivalent exact Möbius/homology certificate may be
  used only if its equivalence is proved and both implementations overlap at
  small cutoffs.

## Risks and Mitigations

- **Chain explosion:** preserve complete small-(N) chains and use a proved
  tensor-product/Boolean-lattice formula for large (N).
- **Parity orientation ambiguity:** report both global orientations and deny
  A3 credit unless a source rule selects one.
- **Finite-product seduction:** keep analytic-domain verdict independent of
  finite symmetry residuals.
- **Hidden target import:** prohibit Gamma/zeta continuation in the main
  computation; use them only after GO as sealed external diagnostics.

## Final Checklist

- [ ] Main exact chain table produced
- [ ] Canonical versus arbitrary parity isolated
- [ ] Nuclear overlap theorem decided
- [ ] No zero data read
- [ ] GO/STOP/NOT-TESTABLE mechanically assigned
