# Round 2 Review

Manuscript reviewed: `papers/03-wheel-sieve-periodic-clock-obstruction/`

Objects checked in this round:

- current source (`main.tex`, `sections/`, `README.md`, `SOURCE_LOCK.md`, `references.bib`, `figures/obstruction_map.tex`)
- compiled review target `main_round1.pdf`
- prior review record `reviews/round1_review.md`

Review standard:

- theorem correctness first
- then verification of all Round 1 required fixes
- then a fresh scan for new counterexamples, topological loopholes, citation/shareability problems, scope drift, and same-object governance failures

## Overall verdict

Verdict: **WEAK ACCEPT**

Score: **8/10**

Bottom line: the Round 1 Major issues have been substantially and, in the manuscript itself, successfully repaired. I do **not** find a new theorem-breaking flaw in the direct-image obstruction, the closure obstruction, the compact-target proposition, or the boundary controls. I also do **not** find a new Route-B leak, cross-object credit transfer, or scope jump out of the Symbolic Dynamics family.

At this point, the paper reads like a narrow but mathematically coherent theorem note. The remaining issues are minor and mostly concern artifact synchronization and conservative public-facing citation hygiene rather than the core proofs.

## Round 1 fix verification

### 1. Overclaim / wording downgrade — verified

This was the biggest Round 1 issue, and it is now materially fixed.

What I checked:

- abstract now says the closure result is under an **explicit sufficient condition**
- the contribution is now described as an **assumption-explicit wheel-sieve stationarization audit**
- introduction explicitly says the periodic contradiction is **not** presented as a new universal theorem
- the novelty claim is narrowed to a wheel-source-specific obstruction package

Assessment:

- the earlier “minimal / assumption-complete / universal-sharpness” drift has been removed from the manuscript proper
- I did not find a remaining sentence in the paper text that would force a Major objection on overclaim grounds

### 2. Compactness proposition separated from periodicity obstruction — verified

This repair is also real, not cosmetic.

What I checked:

- Section 4 now separates the closure theorem from the compact-target proposition
- the proposition is explicitly presented as a **separate feasibility obstruction**
- the manuscript now states that this proposition uses only compactness of the target and continuity of the decoder, and uses neither equivariance, periodicity, nor the diagonal-separation theorem

Assessment:

- the logical hierarchy is now correct
- a fast reader is much less likely to confuse the compactness-of-range argument with the periodic-point theorem

### 3. Paper 02 directional contrast — verified

What I checked:

- introduction now says this note closes the residual branch left by the previous stationarization audit
- it explicitly contrasts the prior **strict-extension** direction with the present **source-to-target images and closures** direction

Assessment:

- this was exactly the clarification needed for project-sequence consistency
- the categorical reversal is now explicit on page 1 rather than implicit

### 4. Ordinary roof protection — verified

What I checked:

- Section 5.3 now explicitly says the paper is **not** proving any obstruction to ordinary positive suspension roofs on periodic base systems
- the obstruction is clearly limited to inherited pointwise absolute labels on revisited target states

Assessment:

- this successfully blocks the earlier likely misreading
- I no longer see a realistic risk that the note will be read as a false “no roofs on periodic systems” claim

### 5. Real lag-pair closure step made explicit — verified

What I checked:

- the proof of the real-clock corollary now explicitly says that the lag-pair set is locally finite in `R^2`, has no finite accumulation point, and hence is closed and misses the diagonal

Assessment:

- the final topological step is now stated, not merely implied
- this closes the readability gap noted in Round 1

### 6. Prior-art tightening — substantially verified

What I checked:

- introduction now explicitly disclaims priority for symbolic sieve encodings in general
- Heeren 2026 is cited as direct topical prior art rather than ignored
- the contribution is framed as a source-specific obstruction note, not as the first symbolic sieve or first periodic contradiction

Assessment:

- the novelty posture is now appropriately narrower
- the manuscript-level prior-art positioning is acceptable

## Fresh Round 2 mathematical review

I re-checked the principal theorem chain rather than only the prose edits.

### Direct-image theorem

I still find the logic correct:

- exact decoding implies fiber constancy
- fiber constancy plus pairwise distinct clock values forces level consistency
- level consistency induces a target grading
- a periodic target point would force `\bar\ell(y)=\bar\ell(y)+m`

No continuity, compactness, finite alphabet, or locality is smuggled into that proof. I do not see a counterexample under the stated hypotheses.

### Closure theorem

The closure argument is still correct as written:

- `F_m(y)=(d(y),d(S^m y))` is continuous
- `F_m(\pi(X))=P_m`
- density of `\pi(X)` in `Y_0=\overline{\pi(X)}` gives `F_m(Y_0)\subseteq \overline{P_m}`
- an `m`-periodic point would land on the diagonal

I do not see a topology bug here. In particular, the theorem does **not** rely on sequences or metrizability, and the paper now correctly avoids that trap.

### Compact-target proposition

This remains correct and correctly demoted:

- compact image in `N_disc` must be finite
- compact image in `R` must be bounded
- the full exact wheel clock range is infinite/unbounded

No periodicity input is needed, and the manuscript now says so.

### Countercontrols

The controls still do the right job:

- modulo-level factor: shows periodicity after clock erasure
- defect-shift closure: shows a boundary fixed point can appear when total continuous inheritance fails
- one-point compactification: shows continuity alone is not enough once the clock topology is changed
- roof discussion: correctly separates absolute point labels from accumulated suspension-roof data

I do not see a hidden theorem contradiction among these controls.

## Remaining issues

## Critical issues

None found.

I do not find a theorem-breaking flaw in the principal statements under the paper’s frozen hypotheses.

## Major issues

None found.

Relative to `reviews/round1_review.md`, the required Major repairs have been implemented successfully enough that I would not keep the manuscript at **REVISE** on mathematical or positioning grounds.

## Minor issues

### Minor 1 — `SOURCE_LOCK.md` is slightly narrower than the manuscript on the direct-image clock codomain

The manuscript’s direct-image theorem is formulated for a general frozen clock sequence `(a_k)` and is then specialized to both exact `q` and exact `log q`. By contrast, `SOURCE_LOCK.md` Section 2 still writes the image decoder only in the integer-clock form

- `d : π(X) -> N`
- `d ∘ π = κ`

and only later mentions the real-valued clocks.

This is not a mathematical error in the paper itself, but it is a small shared-artifact mismatch. If the source lock is meant to mirror the theorem class exactly, it would be cleaner either to:

- state the image theorem in the same generic `a_k in C` form as the paper, or
- add an explicit parallel direct-image clause for `τ = log κ`

### Minor 2 — Heeren 2026 metadata is now conservative, but the exact displayed SSRN version/date should still be manually rechecked before external circulation

The current citation posture is much better than before. However, SSRN landing-page metadata is mutable enough that the exact displayed version/date should still be manually confirmed at release time.

This is a shareability caution, not a theorem issue.

## Route and scope audit

I explicitly checked the governance constraints named in the task.

- Symbolic Dynamics remains the only primary family.
- Route B stays locked.
- No determinant, spectral operator, or zero-comparison claim is reintroduced.
- The “same target object” discipline is now repeated in both the figure and consequences.
- The note does not splice arithmetic evidence from one object into periodic data of another.

I therefore do **not** find a current shared-scope violation.

## Recommendation

For theorem correctness and scoped project use, this draft now clears the bar.

For external circulation, I would treat the manuscript as essentially ready after tiny hygiene cleanup of the remaining minor artifact/citation points above.

## Final score card

Mathematical correctness: **9/10**

Assumption discipline: **8/10**

Novelty calibration: **8/10**

Project-scope consistency: **9/10**

Shareable-paper readiness: **8/10**

Overall: **8/10**

Final verdict: **WEAK ACCEPT**

## One-line decision

Round 1’s substantive objections have been repaired; I find no remaining Critical or Major flaw, only minor artifact-synchronization and citation-hygiene points.
