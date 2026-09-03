# P169 paper plan

**Working title:** Successor Transfer on Canonically Ordered Set Partitions  
**Format:** anonymous `amsart` 10pt short theory note  
**Lifecycle:** internal Round 0; `HOLD_EXTERNAL`  
**Date:** 2026-09-03 UTC  
**Target length:** 6--8 A4 pages including the verified bibliography

## One-sentence theorem package

For the simultaneous rule that sends each nonsingleton block maximum to the
cyclic successor block, determine the sharp transient clock and every
recurrent stratum, and independently compute every target fibre by an
explicit interlacing-sensitive five-state trace.

## Theorem ceiling

The complete note is restricted to the conjunction below.

1. Canonical order is preserved, and the restricted-growth form increments
   the last occurrence of every repeated letter simultaneously.
2. In every nontrivial `(n,k)` stratum, the exact maximum tail is
   `min(n-2,2k-2)`; the global maximum is `n-2` for `n>=2`.
3. Recurrent states have the dense/sparse prefix-suffix forms, counts
   `k!S(n-k,k)` or `(k)_(n-k)`, and exact nontrivial period `k`.
4. Every target fibre is the trace of an explicitly evaluable product of
   five-state local matrices.
5. The targets `025|134` and `035|124` have the same coarse endpoint data but
   fibres two and one.

The RGF carrier, whirling, directed-cycle chip firing, Bulgarian solitaire,
promotion/jeu-de-taquin/rowmotion, box-ball systems, set-partition stack
sorting, Stirling numbers, and generic transfer matrices are background.
Source-search non-hits provide no external permission.

## Claims--evidence matrix

| Claim | Uniform proof | Frozen exact control | Main location |
|---|---|---|---|
| literal equivalence and invariant `k` | adjacent retained-minimum argument and first-occurrence check | all partitions through `n=10` | Section 1 |
| queue smoothing | max-plus height formula and cone inequalities | 532,467 cases | Section 2 |
| sharp stratum/global clocks | smoothing plus labelled window; explicit sharp family | every stratum through `n=10`, witnesses through `n=50` | Section 3 |
| recurrent forms, periods, counts | invariant window forms and suffix cyclic increment | every state through `n=10` | Section 3 |
| every-target fibre trace | selected-maximum reconstruction and local-state bijection | 26,442 targets through `n=9` | Section 4 |
| interlacing sensitivity | printed matrices and predecessor lists | exact fibres 2 and 1 | Section 4 |
| all requested boundaries | separate theorem clauses and matrix boundary semantics | exhaustive finite sweeps | Sections 1, 3, 4 |

## Section plan

### Abstract

- Define the literal map without relying on the RGF shorthand.
- State the stratum clock, recurrent forms/counts/periods, and fibre trace.
- Name the interlacing counterexample and `HOLD_EXTERNAL` scope.
- Use no citations or ownership language beyond the lifecycle boundary.

### 1. Literal rule, coordinates, and theorem

- Canonically order blocks by minimum and prove that the update keeps this
  order, including the `k-1 -> 0` donation.
- Translate exactly to simultaneous last-occurrence increment.
- Give the owner-subtraction paragraph.
- State a complete theorem with all nontrivial and boundary strata visible.

### 2. Directed-cycle load factor

- Define `z_i`, `m`, and the threshold-one update.
- Give the periodic height lift, closed max-plus solution, and the two cone
  implications.
- Derive both finite smoothing times and note forward invariance.
- Explicitly assign this factor no residual theorem credit.

### 3. Labelled windows, sharpness, and recurrence

- Prove the dense suffix and sparse prefix window lemmas.
- Combine them with load smoothing for the upper clock.
- Display the sharp family and both sparse/dense intermediate forms.
- Prove the recurrent normal forms, exact periods, and counts.
- Preserve `n=1`, `k=1`, `k=n`, and `n=2k` in the theorem and prose.

### 4. Explicit target fibres

- Reconstruct each source from cyclic selected maxima.
- Print the five candidate sets and the retained-size/extrema table.
- Print the closed entry formula for every matrix entry.
- Explain that the final matrix omits the linear minimum comparison while the
  trace still closes the cyclic token state.
- Print all four matrices and predecessors for the interlacing pair.
- Prove the trace bijection and image test.

### 5. Controls and scope

- Record the independent standard-library verifier and exact assertion count.
- Treat finite checks as falsification only.
- Close with anonymous Round-0 `HOLD_EXTERNAL` status.

## Figure and table plan

No figure is needed.  The literal rule, two word trajectories, retained-state
table, and numerical matrices are more precise than a diagram.  There is no
prior-bound comparison table because all cited neighbours are subtraction
owners, not baselines for the combined literal theorem.

## Citation plan

- Restricted-growth encoding and whirling: `Wachs1994`,
  `JosephProppRoby2025`.
- Directed-cycle parallel chip firing: `JiLiWang2025` (formal publication;
  arXiv `2407.15889` retained as auxiliary metadata).
- Bulgarian solitaire: `Brandt1982`.
- Jeu de taquin, promotion, and rowmotion: `Schutzenberger1972`,
  `StrikerWilliams2012`.
- Box-ball system: `TakahashiSatsuma1990`.
- Set-partition stack sorting: `ChoiEtAl2024`.

Every record is checked against a primary publisher/DOI or arXiv metadata
surface.  The bibliography contains exactly the cited entries.

## Review boundary

No manuscript review belongs to this author Round 0.  The prior independent
candidate gate supplied the frozen contract and is not relabelled as a paper
review.

## Completion checklist

- [x] theorem and owner ceiling frozen
- [x] complete anonymous source
- [x] standalone verifier and frozen transcript
- [x] minimal verified bibliography
- [x] settled canonical PDF and preserved Round-0 copy
- [x] two source-only cold-build matches
- [x] visual, font, metadata, and anonymity QA
