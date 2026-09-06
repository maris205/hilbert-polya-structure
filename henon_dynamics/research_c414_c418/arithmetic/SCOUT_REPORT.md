# C414–C418 arithmetic scouting report

Status: **one complete author-stage candidate; zero admissions**.
Two other precise contracts were screened out before proof work. Session date:
2026-09-07. No C-number, manuscript, PDF, formal evaluation or target fit is
created by this lane.

## Main outcome

The strongest result is a complete inverse theorem for the native return
observation of **every** matrix in SL(2,Z), not just hyperbolic matrices.
Two full labelled modulus rows, at periods one and two, determine one
congruence-compatible nonlinear conjugacy on the profinite plane. They also
determine the unitary-equivalence class of its Koopman operator **together
with every congruence conditional expectation**. This joint source information
still loses exactly the already identified exceptional 2-adic linear-class bit.

The proof closes scalar, elliptic, parabolic and both hyperbolic trace signs.
Its actual increment over the old finite census is the compatible nonlinear
lift and filtered-operator equivalence, not the old centered-content invariant,
trace-18 pair or two-class arithmetic fibre. General orbit-tree conjugacy,
linear local conjugacy and matrix LTE are credited to their owners.

The author-stage proof is ready for an independent mathematical and substantive
decision. **Do not admit it just because it is proved:** after the classical
inputs and old notes are deducted, its main new calculation is short. The
old BF recurrence texts remain unavailable, so their priority gate is not
silently cleared.

## Three frozen contracts and screening decisions

### 1. Congruence-compatible inverse and joint source-spectrum information loss

- **Object/family:** all matrices A in SL(2,Z); no restriction on trace.
- **Clock/domain:** forward iteration n on X=Zhat² and every labelled quotient
  (Z/qZ)². Modulus q is resolution, not time.
- **Observable:** F_A(q,n)=#Fix(A^n mod q), and equivalently the Koopman
  operator with all projections E_q onto congruence-measurable functions.
- **Arithmetic mechanism:** Smith reconstruction, trace and centered content;
  the exceptional ambiguity consists of two local linear classes at prime 2.
- **Classical ownership:** BRW 2008 linear classification, GNS 2001 labelled
  orbit-tree criterion, standard matrix LTE, and the previous unadmitted
  hyperbolic census quotient. These are deductions from the novelty claim.
- **Proposed increment:** exact compatible nonlinear conjugacy classification
  for the whole family, its filtered unitary equivalence, and the necessarily
  nondifferentiable local conjugacy in the two-class case.
- **Decisive check:** full labelled orbit-tree signatures for trace ±18 and
  ±66 through 2^8, odd-prime cases, boundary types and hostile different-depth
  controls. Full all-height proof is supplied; the finite check is only a
  diagnostic. Runtime is under one second on the local CPU; no GPU cost.
- **Replacement boundary:** not the real torus, not an additive/module
  conjugacy and not a target Riemann operator. Adding an observable sensitive
  to the missing additive structure changes the declared observation.
- **Disposition:** `AUTHOR_PROOF_COMPLETE; INDEPENDENT_VALUE_AND_SOURCE_REVIEW_REQUIRED`.
  This is one result with corollaries, not several candidate papers.

### 2. Polynomial-clock simultaneous returns

- **Object/family:** multiplication by a and b on R/Z, all integers a,b≥2.
- **Clock/domain:** one declared sampling index n, with two return times
  n and n² on the circle; this is not claimed to be iteration of one map.
- **Observable:** the ordinary series sum_{n≥1} gcd(a^n−1,b^(n²)−1) z^n.
- **Arithmetic mechanism:** uneven-height S-unit gcd, with multiplicative
  dependence as the expected dividing line.
- **Proposed increment:** a complete convergence/rationality or boundary
  classification for this genuinely nonlinear sampling clock.
- **Classical subtraction:** C411 already handles independent two-index
  rectangular returns; Miles/current synchronization and diagonal results
  do not by themselves establish the resampled contract. The existing
  S-unit estimate controls the larger height of order n², not the smaller
  normalization n needed for the proposed radius-one conclusion.
- **Cheap decisive check:** write the required inequality before computing.
  The available bound log gcd≤epsilon·max(n log a,n² log b) does not imply
  log gcd=o(n). This is a precise missing arithmetic lemma, not numerical
  evidence of a natural boundary. In the dependent subfamily a=c^r,b=c^s,
  gcd=c^[n gcd(r,sn)]−1, a periodic mixture of exponentials; that alone would
  be an insufficient residual theorem.
- **Replacement boundary/disposition:** `REJECT_FOR_CURRENT_BATCH_UNCLOSED`.
  Retain as a question only. No broad claim that the problem is open worldwide,
  no source theorem inferred from an abstract, and no speculative census.

### 3. Invariant-sublattice index zeta of the arithmetic return matrix

- **Object/family:** hyperbolic A in SL(2,Z), with its rank-two integral module.
- **Clock/domain:** finite-index A-invariant sublattices Λ≤Z²; the weight is
  [Z²:Λ]^(−s), not forward iteration time.
- **Observable:** sum_{AΛ=Λ}[Z²:Λ]^(−s), retaining its exact local factors.
- **Arithmetic mechanism:** lattices over Z[A] in the quadratic algebra Q[A],
  maximal-order comparison and conductor corrections.
- **Proposed increment:** an explicit complete family formula and a recovery
  theorem for the local order from those factors.
- **Cheap decisive check/classical owner:** the series is directly Solomon's
  lattice zeta. Lynch's July 2026 Theorem 1.1 gives an effective finite-module
  expression in the much broader arithmetic-order setting; classical
  quadratic-order factor formulas are also explicit. Merely translating
  these to an A-invariant lattice count supplies no separated new theorem.
- **Replacement boundary/disposition:** `REJECT_CLASSICAL_RECONSTRUCTION` at
  this proposed scope. Index/norm weighting does not become a Hénon period
  clock or a target Euler product. No separate inverse theorem beyond the
  established framework was identified, so no pilot or proof is commissioned.

## Deliverables and next gate

- [Full author proof](CONGRUENCE_CONJUGACY_PROOF.md).
- [Primary-source access and residual audit](SOURCE_AUDIT.md).
- [Bounded exact orbit-tree diagnostic](orbit_tree_check.py), run with
  `python -B orbit_tree_check.py`; it writes no files.

The diagnostic constructs parent/child cycle incidence, rather than comparing
only cycle histograms. Fifteen paired finite towers pass, including nine
nonhyperbolic/scalar boundary cases, plus three hostile/obstruction controls.
No old source tree was modified or promoted, and no global/Git write was made.

The main agent should independently review the theorem and decide whether the
compatible inverse question supplies sufficient post-classical value. If it
does not, preserve the shortfall instead of filling a paper slot. Target
arithmetic progress is absent: the joint source-spectral obstruction is not an
A2 match, and missing target controls/metrics remain unrun, not positive.

Skills used: repository batch routing; research-lit/idea-creator for screening;
ARS fact-check role for exact access/claim boundaries; proof-writer for the
complete statement, edge cases and explicit dependency map. No external model,
resolver API, GPU, human peer review or paper-writing pipeline was invoked.
