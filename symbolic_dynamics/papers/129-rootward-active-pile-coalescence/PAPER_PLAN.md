# Paper plan — P129

**Working title:** Rootward Active-Pile Coalescence on a Path: Interface
Additivity and Exact Jump Counts  
**Format:** anonymous `amsart`, BibTeX bibliography  
**Type:** finite stochastic dynamics / exact probability  
**Date:** 2026-08-31  
**Target length:** 5--6 A4 pages including references  
**External status:** `HOLD_EXTERNAL`

**Current internal snapshot:** round two frozen; both independent reviews
and paper-local final QA complete; `GO_INTERNAL / HOLD_EXTERNAL`.

## One-sentence contribution

For a path process that selects an occupied nonroot site uniformly, moves it
one step toward the root, and coalesces on contact, the expected number of
discrete updates from every rooted initial set is exactly the sum of the
meeting times of its consecutive pure-death interfaces.

## Claims–evidence matrix

| ID | Claim | Proof/evidence | Location |
|---|---|---|---|
| C1 | Absorption is certain and every hitting-time PGF satisfies a finite acyclic first-step recursion. | Strict descent of `Phi(S)=sum S`; direct conditioning; exact rational DP. | Model/results section |
| C2 | For `S={0=s_0<...<s_r}`, `E[T_S]=sum_i h(s_{i-1},s_i)`, where `h` is the two-path pure-death meeting mean. | Finite-site rate-one Poissonization and strong Markov; ordered consecutive-label blocks; predictable compensator, finite-time expectation, monotone convergence, Tonelli; first-event recurrence. Exact Bellman/interface comparison through `n=14`. | Main theorem section |
| C3 | `supp(T_S)={max S,...,sum S}` for every nonabsorbing rooted state. | Induction on `Phi`, split by occupancy of the predecessor of the maximum; exhaustive exact laws through `n=11`. | Exact-law section |
| C4 | From full occupancy, `E[T_n]=sum_{m=1}^{n-1}(2m-1)!!/(2m-2)!!`. | C2 plus Catalan/ballot decomposition, explicit finite telescoping and bounded optional stopping for `h(m-1,m)`; exact checks through `m=80`. | Full-start corollary |
| C5 | `E[T_n]=4/(3 sqrt(pi)) n^(3/2)+O(n^(1/2))`, and the minimum time has mass `1/(n-1)!`. | Central-binomial asymptotic; unique descending all-collision schedule. | Corollaries |

The experimentally observed maximum-endpoint probability is intentionally
excluded from the manuscript theorem contract. It remains pilot-only until a
separate proof is completed.

## Structure

### Abstract

- State the literal active-pile scheduler in the first sentence.
- State the arbitrary-initial-state interface theorem, not merely the
  full-start mean.
- Give the double-factorial sum and `n^(3/2)` leading term.
- Mention the exact PGF/support result and bounded owner status.

### 1. Model, question, and subtraction boundary

- Define path, occupied-set state, root, update, and discrete hitting time.
- Explain why uniform active-pile time differs from a uniform geometric-site
  lazy chain and from standard independently moving reversible walks.
- Subtract generic coalescing-walk, voter-duality, graphical-construction,
  first-passage, and exact one-dimensional coalescence machinery.
- State the P114/P117/P121/P126 internal firewall and `HOLD_EXTERNAL`.

### 2. Finite law and support

- Prove strict potential descent and PGF recursion.
- Prove the support interval for every rooted initial state.
- Derive the full-state minimum mass from the unique descending collision
  order.
- Do not mention the unproved maximum-endpoint formula as a theorem.

### 3. Poisson clocks and interface additivity

- Prove that rate-one clocks at occupied nonroot sites have the literal
  uniform-active embedded jump chain, using only the finite accessible site
  set and strong Markov at effective stopping times.
- Construct ordered coalescing pure-death graphical paths and inductively
  prove the consecutive-label-block invariant, including indirect mergers.
- Identify the active-pile count with the number of open initial interfaces.
- Apply the predictable compensator first at finite time, pass to infinity by
  monotone convergence, and then use Tonelli; explicitly state that interface
  lifetimes need not be independent.
- Derive the recurrence for `h(a,b)` including the root boundary.

### 4. Ballot evaluation and full occupancy

- Evaluate `h(m-1,m)` by the stopped fair event-type walk.
- State the Catalan/ballot last-exit decomposition and prove the resulting
  double-factorial ratio by explicit central-binomial telescoping and bounded
  optional stopping.
- Sum adjacent interfaces for the full state.
- Apply the central-binomial estimate for the leading asymptotic.

### 5. Exact control and limitations

- Describe the paper-local `Fraction` verifier and canonical transcript.
- Record the executed ranges exactly: transition/mean checks for every rooted
  subset through `n=14`, complete distributions through `n=11`, and the pair
  recurrence and independent adjacent ballot sum through 80.
- State that computation is corroboration, not proof.
- Fix carrier, scheduler, set-valued collision, and path-only boundaries.

### Conclusion

- Restate the interface theorem and full-state consequence without novelty
  inflation.
- Keep external owner/non-release hold explicit.

## Figure phase

No data plot or architecture figure is warranted. The contribution is an
exact theorem, and a decorative path diagram would not make the
Poissonization/interface proof easier to verify. The figure phase therefore
freezes **zero figures and zero tables**; equations and a short proof roadmap
carry the comparison. This is a deliberate no-figure outcome, not a skipped
pipeline phase.

## Citation plan

- Model/related work: Cox (1989), Cooper et al. (2013), Benjamini et al.
  (2016), Kanade et al. (2023).
- One-dimensional exact coalescence/first-passage boundary: Ermakov (1997).
- Birth--death coalescing-flow boundary: Assiotis (2018).
- Active-count/expected-jump bridge in TASEP: Hitczenko--Wesołowski
  (2025), Theorem 3.
- Exact nearest-neighbor coalescence patterns and interval labels:
  Śniady--Urbán (2026), arXiv v3.
- Every citation must use DOI/Crossref-verified metadata. Generic graphical,
  coalescence-time, and simple-walk tools receive zero contribution credit.

## Review gates

1. **Complete:** round 0 compiled and was preserved before hostile review.
2. **Complete:** independent nonauthor Review A audited every theorem, proof
   boundary, bibliography, verifier, PDF page, font, and metadata field.
3. **Complete:** all Review-A findings were repaired in source/support;
   `main_round0_original.pdf` is preserved and `main_round1.pdf` is frozen.
4. **Complete:** a different independent nonauthor performed Review B on
   round 1 and returned no blocking finding.
5. **Complete:** round 2 is the support-only sign-off; paper-local final QA
   and `SHA256SUMS` are complete.  External status remains HOLD.
