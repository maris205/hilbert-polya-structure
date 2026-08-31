# P136 hostile review — Round A

**Manuscript:** *Recorded-Transversal Laws on Rate-Weighted Sunflower Forests*  
**Review date:** 2026-08-31 UTC  
**Reviewer role:** independent hostile reviewer; no participation in the round-0 draft  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`REPAIR`** — no critical formula failure, but one major terminology/claim-boundary defect must be repaired before Round B.

## 1. Scope and frozen-artifact checks

I reviewed `main.tex`, `references.bib`, all narrative/evidence/build files,
`code/verify.py`, the frozen verifier output, the LaTeX log, and all four PDF
pages. I did not modify the manuscript, verifier, bibliography, or PDFs.

Fresh checks gave:

- `cmp` of fresh verifier stdout against `code/verification_output.txt`: exit 0;
- 5,812 parameter-labelled inputs and 174,170 exact assertions: `PASS`;
- `main.pdf` and `main_round0_original.pdf`: byte-identical, SHA-256
  `0668f9b434aad2747a3d887d0a8fa6f6e36885a41b9f27f6182ee2d6a15192ef`;
- four A4 pages, blank title/author/subject/keyword metadata, unencrypted;
- all 18 font entries embedded, subsetted, and Unicode-mapped;
- searchable text and no actual undefined-reference, overfull-box, underfull-box,
  or build warning;
- every page visually inspected: no clipping, overlap, bad glyph, margin
  excursion, or anonymous-author leak.

The public-facing artifact says `Anonymous`; project files consistently retain
`HOLD_EXTERNAL`. This gate does not authorize external circulation.

## 2. Mathematical attack results

### 2.1 Weighted endpoint integral — survives

For a proper mask `A ⊊ [m]`, conditioning on the first core-marked clock at
time `t` requires:

- a petal mark and `X_i < t` for every `i ∈ A`;
- no clock before `t` for every edge outside `A`, other than the unique
  terminal edge at `t`;
- a core mark on that terminal edge.

This gives exactly

\[
 \Bigl(\prod_{i\in A}r_i\Bigr)
 \Bigl(\sum_{j\notin A}q_j\lambda_j\Bigr)
 \int_0^\infty e^{-\Lambda([m]\setminus A)t}
       \prod_{i\in A}(1-e^{-\lambda_i t})\,dt.
\]

Expansion gives the stated alternating sum. The edge cases survive:

- `A = ∅`: the formula is the competing-risk probability that the
  first selected edge has a core mark;
- `|A| = m - 1`: the complement rate is still positive, so there is no zero
  denominator;
- `m = 1`: the two endpoint masses are `q_1` and `r_1`, summing to one.

No missing condition on the marks of late outside edges was found: only their
clock times must exceed the stopping time, and their unobserved marks integrate
to one.

### 2.2 Actual-vertex law — survives

The aggregate event depends on clock ranks and on core-versus-petal categories,
not on the identity of a vertex within its core or petal. Conditional vertex
identities therefore remain uniform. Mixing over the possible terminal edge
does not spoil the factor `1/c`, because every terminal edge uses the same
core `C`. Thus division by `c ∏_(i∈A) p_i` is correct, and the all-petal mass
for a specified vertex tuple is `∏_i (c+p_i)^(-1)`, independently of the edge
rates.

The verifier separately resolves vertices only at unit rates. The manuscript
correctly says that the unequal-rate resolved law is carried by the proof, not
by exhaustive computation.

### 2.3 Unit-rate stopping-count distribution — survives

At unit rates the edge order is uniform and independent of the marks. Hence

\[
 \Pr(T>t)=\binom mt^{-1}e_t(r_1,\ldots,r_m).
\]

Tail differencing gives every mass below the upper endpoint. The manuscript's
repair of the upper endpoint is essential and correct:

\[
 \Pr(T=m)=\prod_i r_i+
 \frac1m\sum_j q_j\prod_{i\ne j}r_i
 =\frac{e_{m-1}(r)}m.
\]

The two terms are disjoint: all marks are petals, or the last edge has a core
mark after `m - 1` petal marks. This also works at `m = 1`, where the two terms
are `r_1` and `q_1`. The finite tail identities for `E[T]` and `E[T^2]`, and
therefore the variance formula, are correct.

### 2.4 Forest factorization — survives for endpoints and choice counts

With vertex-disjoint components and independent edge clocks/marks, every local
pair `(R_a,T_a)` is a function of only its component's randomness. Global
interleaving preserves every within-component exponential order. Therefore the
endpoint laws tensorize, the **numbers of selected vertices/choices** add, and
their PGFs multiply. Unequal positive fixed rates do not break this argument.

This conclusion would fail if components shared vertices or if a rate/mark in
one component depended on another component's history; both cases are properly
outside the contract.

## 3. Critical findings

**None.** I found no counterexample to the weighted endpoint law, actual-vertex
refinement, unit-rate mass/PGF/moment formulas, or the forest product for the
discrete choice count under the stated hypotheses.

## 4. Major findings

### `P136-A-M1` — “stopping clocks convolve” conflates choice count with elapsed time

The random variable `T` is explicitly defined as the number of recorded
vertices/choices. The verifier likewise increments an integer step count. But
the abstract says “the stopping clocks convolve,” and the same wording recurs
through `README.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
`CONTROL_RESULTS.md`, and `PAPER_PLAN.md`. This is especially dangerous because
the preceding construction has just introduced genuine exponential clocks.

Under the natural continuous-time reading, the claim is false. Take a forest
of two one-edge sunflowers with unit clock rates. Each local elapsed completion
time is `S_a ~ Exp(1)`, independently, but the elapsed time for the
whole forest is

\[
 S=\max(S_1,S_2),\qquad
 \Pr(S\le t)=(1-e^{-t})^2,
\]

not `S_1 + S_2` and not a convolution. In contrast, the discrete choice count
is deterministically `T = 1 + 1 = 2`, exactly as Theorem 5.1 intends.

**Required repair:**

1. Replace the abstract phrase by “component choice counts add, hence their
   probability generating functions multiply.”
2. At the first definition of `T`, state explicitly that `T` is a discrete
   choice/record count, **not** elapsed exponential time.
3. Replace exposed uses of “clock law,” “stopping clocks,” and “clock
   convolution” by “step-count law,” “choice count,” and “step-count
   convolution” throughout the manuscript and evidence files. Internal code
   identifiers may remain only if the user-facing labels are unambiguous.
4. Add one limitation sentence: continuous elapsed absorption times are not
   analyzed; for a disjoint forest, its completion time is the maximum of the
   component completion times.
5. Rebuild, replay the verifier, and search the final extracted text and
   evidence files for any remaining misleading “clock-law” claim.

This is a claim-boundary failure, not a failure of equations (8)--(15), but it
is major because the high-level statement is false under the most immediate
meaning of “clock” in this manuscript.

## 5. Minor findings

### `P136-A-m1` — the weighted verifier range hides integrality of tested rates

The control table writes `p_i, λ_i ≤ 3`, while the model allows arbitrary
positive real `λ_i`. The verifier actually tests only
`p_i, λ_i ∈ {1,2,3}`. The current inequality can be misread as an
exhaustive continuum check.

**Required repair:** write the exact finite grids in `main.tex` and all evidence
files, for example
“`p_i, λ_i ∈ {1,2,3}`” for the weighted lane and analogous set notation
for the other lanes. Preserve the existing statement that all-real-rate claims
come from proof rather than enumeration.

### `P136-A-m2` — make the conditioning step in the actual-vertex proof explicit

The proof is correct, but one additional sentence would eliminate a plausible
conditioning objection: the event fixing `A` and the terminal edge is
measurable with respect to clocks and category indicators only, so conditioning
does not bias identities within `C` or `P_i`.

**Required repair:** add that sentence immediately before division by
`c ∏_(i∈A) p_i`. This is explanatory and does not alter the formula.

## 6. Owner subtraction and contribution boundary

The central owner subtraction is accurate on the primary sources checked:

- [Bar-Yehuda, Section 5.1 and Theorem 6](https://doi.org/10.1007/s004530010009)
  gives Pitt's hypergraph vertex-cover rule; with unit vertex weights, the
  selected vertex in the chosen hyperedge is uniform. Zero credit for the
  process and approximation guarantee is therefore appropriate.
- [Gnedin, Proposition 2(i)](https://doi.org/10.1007/s11083-026-09743-2)
  explicitly gives the independent-exponential representation and independence
  of restrictions to disjoint item sets. Zero credit for the size-biased order
  and generic dissociation is appropriate.
- [Plackett's permutation model](https://doi.org/10.2307/2346567) has the stated
  1975 metadata and is an appropriate owner citation for the ranking device.

The residual contribution is consequently modest: a closed special-carrier
calculation assembling a weighted mask integral, vertex refinement, unit-rate
choice-count law, and the induced forest product. The manuscript already avoids
claiming a new algorithm or general independence theorem. A targeted bounded
search did not locate the whole displayed package, but that non-hit is not a
novelty certificate. `HOLD_EXTERNAL` must remain in force unless a wider direct-
package literature audit and an external novelty assessment are completed.

## 7. Round-A acceptance checklist

- [ ] Repair `P136-A-M1` everywhere visible to a reader.
- [ ] State explicitly that elapsed exponential absorption time is outside the
  paper.
- [ ] Correct the exact finite rate grid in the control table and ledgers.
- [ ] Strengthen the conditional-uniformity sentence in Corollary 3.2's proof.
- [ ] Fresh verifier byte replay remains exit 0.
- [ ] Four-stage LaTeX build, text extraction, metadata/font checks, and
  all-page visual QA pass after the repair.
- [ ] Preserve `Anonymous` and `HOLD_EXTERNAL`.

**Round-A disposition:** the theorem formulas survive, but the manuscript is
not ready for Round B until the stopping-**count** versus elapsed-**time**
boundary is made impossible to misread.
