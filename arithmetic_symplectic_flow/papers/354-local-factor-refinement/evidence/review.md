# LFR01 — internal ARS analysis review

## Checkpoint 2: mathematical/adversarial review

Verdict: **PASS**, within the frozen local-source refinement contract.
Calibration: **NOT_CALIBRATED**. This is internal model-assisted review, not external peer review.

### Actual access and independence limits

- Candidate: `ANG-20260921-LFR01`; authorized batch round 5/5.
- Scientific input: `candidate-card.md`, original lines 1–146, read completely.
  SHA-256: `df82f1b6ba5562606b8aac1a2177783c4e29f5fda5d01ace0eae529462411e3a`.
- Scientific input: `paper.md`, lines 1–304, read completely.
  SHA-256: `36ce410c9b58773a73828a08fc1b9245939bbed86220c25b14c0d6c0807352bc`.
- These input hashes were measured, not merely copied from the assignment.
- Retained familiarity with prior 348–353 author inputs is disclosed; no additional older scientific file was opened.
- Applicable stream guidance and the ARS router, deep-research workflow, DA role,
  logical-fallacies reference and runtime policy had been read completely and remain applicable.
- No 354 peer, independent-proof, scope-review, outcome, README, ledger or card-append content was read.
- No external source, auxiliary reviewer, numerical experiment, Git operation or PDF was used.
- Shared conversation/model history prevents a blind-review claim. Served model identifier and
  effective reasoning configuration were not independently observable and remain `UNKNOWN`.
- Checks below are direct symbolic deductions and adversarial case checks, not an empirical census.

### 1. Every typed state and every eventual core

- For arbitrary `T(d,r,a)`, including malformed/unreachable accumulators, division strictly lowers
  positive integer `r`, while nondividing increments satisfy `d² ≤ r ≤ r_initial` before exit.
  Thus neither kind of step can occur infinitely often. Every work state exits to a finite normal word.
- This argument does not assume sortedness, primality, reachability, or a valid accumulator product.
  The `r=1` rule has priority; large initial `d` is handled by the immediate square-bound exit.
- Only a proper launch `T(2,n,empty)` uses the factorization invariant: the residual has no divisor
  below the current trial divisor. A successful trial divisor is therefore prime, and the terminal
  residual is prime. The product invariant and nondecreasing factors give the complete factor word.
- An arbitrary exited normal word is gcd-collapsed before a proper launch. Mixed-prime/unit cases
  terminate; the remaining cases enter a unique prime microcycle. No malformed accumulator
  creates a separate composite cycle, and no infinite transient state family was omitted.
- For prime `p`, trial states run from `2` through `b_p=floor(sqrt(p))+1`.
  The least discrete cycle length is exactly `ell_p=b_p`; its single normal launch translates
  `u` by `-log p`. Trial steps supply no additional geometric holonomy.
- Disposition: PASS; the all-state claim is stronger than a proper-launch-only factorization claim
  and is justified separately rather than silently inferred from it.

### 2. Inverses, branch measure, and non-surjectivity

- Normal targets have precisely the gcd predecessors, the `r=1` work exits, and the square-bound
  work exits. Their source types and predicates distinguish the three families.
- Work targets have precisely the normal launch, nondividing increment and successful division
  predecessors listed in the paper. The division predecessor requires the accumulator to end in
  `d` and `r≥d`; this is exactly the old square-bound condition `d²≤d r`.
- All stated inverse geometric domains are full target charts; normal inverses are `(aQ,X/a,Z)`
  or `(rQ,X/r,Z)` and work inverses are identity. No division by a vanishing transverse coordinate occurs.
- `T(2,1,(1))` has no predecessor under these exhaustive lists, but remains in the source and exits.
  Consequently local branch invertibility has not been confused with surjectivity of the full map.
- Each inverse/forward branch has Jacobian one, including the null axes, hence preserves the
  assigned chart measure on all Borel sets. This is not a claim that the full many-to-one map preserves
  the counting-sheet measure. Its IMAGE logarithmic cocycle is zero and is not the physical clock.
- Disposition: PASS.

### 3. Actual arrows, all lags, topology, and the full quotient

- Let `N_s,A_s` denote first-anchor time and accumulated normal-head log, and set `theta=u-A_s`.
  Terminal arrows have `theta_y=theta_x`, `k=N_y-N_x`; prime arrows have
  `theta_y-theta_x=j log p`, `k=N_y-N_x+j ell_p`, with equal `v,z` and integer `j`.
- Necessity follows by extending any common future equally to an anchor. Sufficiency uses
  nonnegative anchor-turn counts `a,b` with `a-b=j`; thus negative and positive lags are both realized.
- For a normal launch out of the prime anchor, `N_y=ell_p-1` and `j=-1` give actual lag `-1`,
  a useful sign check. At the same full point, `j log p=0` forces `j=0`, so main-source isotropy is trivial.
- Fixed state-pair/lag pieces are translation graphs with the claimed congruence restrictions.
  Discrete indices and the inherited topology give countable, Hausdorff, locally compact étale charts;
  inversion and composition respect the displayed lags. Equal triples are not duplicated histories.
- The continuous open phase map is onto and its fibers are exactly these orbits. Its quotient is
  the terminal `R³` plus one full `(R/(log p)Z)×R²` per prime, including every work-state basin.
- Disposition: PASS; no core-only quotient or compressed lag convention was substituted.

### 4. Contact owner, physical packets, and conjugacy boundary

- Constant `u` translations preserve beta. Direct differentiation gives
  `d beta=(dv-v du) wedge (dz+z du)` and `beta wedge d beta=du wedge dv wedge dz`.
  The claimed field satisfies `beta(R)=1`, `i_R d beta=0`, including the locus `1+vz=0`.
- The complete physical flow commutes with all arrows, descends to the full quotient, and preserves
  contact volume. The quotient volume is locally descended; infinite sheet multiplicity is not pushed forward.
- Terminal points have no nonzero return. In a prime component, the full return group is
  `(log p)Z` exactly at `v=z=0`, and is `{0}` elsewhere. There is one primitive circle per prime,
  with all repetitions and no phase/work-state multiplicity. Volume preservation does not imply recurrence.
- The anchor-coordinate identification gives a full strict contact-flow conjugacy to the prior physical
  owner, not equality of source groupoids: a named anchor turn now has lag `ell_p`, not lag one.
  The paper claims neither a lag-preserving anchor identification nor a universal nonisomorphism theorem.
- Disposition: PASS; `ell_p`, source lag, IMAGE cocycle and physical time remain distinct.

### 5. Three full controls and the bounded conclusion

- FACTOR-OFF retains every work state and work rule, removes launch predecessors into work charts,
  and adds singleton normal predecessors. All work exits still feed normal gcd reduction.
  Its full quotient has separate empty and unit `R³` basins plus all integer cylinders `n≥2`.
  The unit basin has actual `Z` source isotropy but no physical circle; the empty basin has none.
  Every integer cylinder has one zero-transverse primitive circle; composite/repetition coincidences
  do not identify different circles. Incoming empty-accumulator work states are retained.
- UNIT-HOLONOMY keeps the microcycles but makes all source geometry identity. Its prime-basin
  isotropy is the actual subgroup `ell_p Z`, at every transverse point, not a relabeled lag-one group.
  The full quotient has an `R³` per basin, so the stated physical flow has no nonzero returns.
- DRIFT-ONLY keeps the main source/groupoid/quotient and changes only the physical flow.
  It preserves beta and volume but is not the global Reeb flow: `beta(partial_u)=1+vz` and
  `i_partial_u d beta=-z dv-v dz`. Each prime component has the full `R²` family of circles.
- No control discards malformed charts, divides out an isotropy kernel without declaration,
  or selects a transverse center before reporting its physical ledger.
- The positive result is an autonomous local trial-division source realization with a conjugate
  physical owner, not a new physical architecture, canonical arithmetic clock, or naturalness theorem.
  Trial-division rules and launch scaling remain designed; gcd remains a macro operation.
- T0–T2 are owner-level only; T3 is not audited, formal Route A is unassigned and Route B not invoked.
  No trace, spectrum, RH conclusion, or cross-owner credit follows from this review.
- Disposition: PASS. No correction is required on the frozen 146/304-line inputs.
- Round 5 closes the authorized batch. The next action is a batch handoff and user confirmation,
  not a sixth candidate or an unapproved coupled source/clock construction.

Checkpoint 2 is frozen at EOF. Final-surface checkpoint 3 requires a separate release.

## Checkpoint 3: released final surfaces and five-round synthesis

Verdict: **PASS after one narrow wording clarification**, verified below.
The internal/shared-history and `NOT_CALIBRATED` limitations above remain unchanged.
This ARS final-surface checkpoint checks claim boundaries, not a fresh mathematical proof or external review.

### Actual added access and preservation

- Read only card lines 147–164; full file has 164 lines, measured SHA-256
  `a3c5d5f455476e4c0ec70f4a2487f838586e1b37af8776f0a4ca3af05cb4b4e2`.
- Read the full 31-line `README.md`, measured SHA-256
  `9bbc8f598b71716ae4d0434fab6c2b81834fd0ad0c63185f49d5e48d274c5b77`.
- Read the full 29-line `claim-ledger.md`, measured SHA-256
  `905e7735b5f13d9db27573c56ca842b8031ef9078d72a68c34566c7a70879c6b`.
- Read the full 62-line `../350-transverse-graded-trace/batch-summary.md`, initial measured SHA-256
  `2de475319e9366c5984b4fbec17b38292ffdf244e18768b5242fd440d2d51d6f`.
- After the author's one-line clarification, reread summary lines 21–25 only; still 62 lines,
  final measured SHA-256 `163adaa6abf973e8ef6a5c9a5c7249a43005e2976e18c16564fc0a836a9d49a3`.
- Rechecked original card 146-line prefix and unchanged 304-line paper hashes against CP2.
  No unchanged proof was reread. The prior review's 116-line prefix remains byte-preserved at
  `7f26c4e1f97aaff33a178acc1d5f26176d5ecfc35898328dd56afdd49d686104`.
- Linked local targets were checked for existence only, without opening peer reports or batch logs.
  No new scientific source, peer evidence, independent-proof report, external source or future card was read.

### Consistency and adversarial disposition

- The three 354 surfaces agree on candidate, status, all-state termination versus proper-launch
  factorization, complete physical prime ledger, and retained work-state/control multiplicities.
- Main source isotropy zero, unit-control `ell_p Z`, and discrete length versus physical `log p`
  are not conflated. The complete quotient contact-flow conjugacy is not promoted to source-groupoid
  identity, a new physical architecture, or a canonical-clock theorem. Disposition: PASS.
- The five-round table preserves the distinctions among transverse flat traces, a genuine contact
  complex, contact-order weights and cohomology. The unnormalized factor two and infinite-dimensional
  non-trace-class obstruction remain visible; no ad hoc halving or subtraction of infinite traces is endorsed.
- The altered clock in 353 is a separately owned control, not a result inherited by RCF01.
  Its conditional additive/monotone rigidity does not erase the counterexample to weaker hypotheses.
  The 354 source refinement is likewise separately owned and explicitly physically conjugate.
- N1, minor wording: the initial summary's unqualified statement that the batch constructed no
  ordinary trace-class operator was broader than the retained finite-dimensional comparisons warrant.
  The author now says no ordinary trace-class operator realizing the displayed orbit functions was
  constructed. The actual changed line and new hash were inspected. Disposition: RESOLVED.
- The synthesis states convergence before continuation and does not promote orbit functions to
  Fredholm/spectral/cohomological determinants. No Hilbert–Pólya operator, RH/zero-location result,
  formal Route-A success, Route-B readiness, or cross-owner credit is claimed. Disposition: PASS.
- All surfaces retain strong naturalness OPEN and the fifth-round stop. The suggested coupled
  arithmetic/clock direction is a proposal for user confirmation, not a frozen sixth object or authorization.
- Summary line 6 still says final review and preservation QA are pending. That is an accurate
  workflow snapshot, not a completed-QA claim; this report does not certify later mechanical checks.

Final checkpoint frozen at EOF; no mathematical correction or further research is required by this review.
