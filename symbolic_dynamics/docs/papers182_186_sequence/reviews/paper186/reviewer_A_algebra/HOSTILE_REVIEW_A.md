# Hostile Review A — P186

## Round1 delta disposition

**ACCEPTED.**  The process-separated delta review found that Round1 repairs
P186-A-MI-01 and P186-A-MI-02 and introduces no new Critical, Major, or Minor
finding.  The current reviewer-owned verifier and `CANONICAL.txt` bind
Round1 `main.tex` SHA-256
`e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394`
and `main_round1.pdf` SHA-256
`449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48`.
Two clean-process runs reproduced the same 12,106,438-assertion transcript
byte for byte.  The original finding register below is retained as the
historical Round0 review record; its resolution is documented in
`DELTA_ACCEPTANCE_TEMPLATE.md`.

## Round0 frozen object and reviewer status

This is a **process-separated**, reviewer-owned audit.  It is not described
as an independent replication.  The reviewer read the frozen Round0 source,
PDF, author control, canonical transcript, proof package, claims ledger,
source-verification record, and QA documents.  No file under
`papers/186-rank-compression-support/` was edited.

- Reviewed `main.tex` SHA-256:
  `f44a1fa0119ff853991d737b72a345e0a60266bf7438c947bf5b61bb61a525aa`.
- Reviewed `main_round0_original.pdf` SHA-256:
  `6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431`.
- Control representation: the empty state, or a minimum followed by a
  positive ordered gap composition.
- Inverse control: weak-sequence reconstruction in `r+1` labelled short-gap
  slots around `r` forced surviving gaps.
- Exhaustive range: all gap states for `1 <= n <= 18`; literal gap erosion
  through `t=n+3`; target-local fibre and total mass at every tested time.
- Result: 12,106,436 exact assertions; zero formal counterexamples.

This route does not enumerate bit masks or call the author's subset-loop
verifier.  The gap representation is bijective and reaches all `2^n` states;
the inverse count is reconstructed from exact short-word spans in labelled
slots.

## Round0 decision (historical)

**Minor revision required.**  Every formal theorem, including its `t=0` and
post-height cases, survived.  Two abstract sentences need their formal
quantifiers restored.

## Finding register

### Critical — 0

No critical finding.

### Major — 0

No major finding.

### Minor — 2

#### P186-A-MI-01 — Ambiguous positivity antecedent in the abstract

The abstract says that each original positive gap `g` becomes `g-t “if
positive”` (lines 44–45).  Read grammatically, `g` is always positive, so the
sentence can prescribe a nonpositive gap when `t>=g`.  The formal theorem is
correct: retain `g-t` exactly when `g>t` (lines 92–104).  Replace the abstract
phrase by, for example, “becomes `g-t` when `g>t`, and otherwise disappears.”

#### P186-A-MI-02 — Unique deepest-state sentence omits `n>=2`

The abstract advertises “the unique state of depth `n-1`” without restricting
`n` (lines 46–47).  At `n=1`, both states, the empty set and `{0}`, are fixed
and hence both have depth `0=n-1`.  The formal theorem correctly begins the
uniqueness assertion with `n>=2` (lines 106–117).  Add the same qualifier to
the abstract or state the `n=1` boundary there.

Neither minor finding is a counterexample to the formally quantified results.

## Quantifier and boundary attack matrix

| Claim surface | Hostile control | Outcome |
|---|---|---|
| Gap normal form, all `t>=0` | Repeated one-step erosion versus `E_t`, through `n+3` | Pass |
| Minimum invariant/empty state | Checked for every gap state | Pass |
| `t=0` image and fibres | Entire `2^n` carrier; every fibre exactly one | Pass |
| Time-`t` image condition | Exact set equality with `max(B)+t(|B|-1)<n` | Pass |
| Image-size sum | Exact count for every tested `n,t` | Pass |
| Every-target fibres | Gap-slot inverse reconstruction, target by target | Pass |
| Negative budget | Exactly zero; no impossible target enters the image | Pass |
| Fibre mass | Sum equals `2^n` at every tested time | Pass |
| One-step specialization | Every nonempty fibre equals `C(n-max(B),|B|)` | Pass |
| Fibonacci first image | `2,3,5,...,6765` through `n=18` | Pass |
| Fixed/recurrent and basins | Empty basin one; singleton-minimum basin `2^(n-m-1)` | Pass |
| Clock CDF/depth shells | Bounded-gap-word reconstruction for every `h` through `n+1` | Pass |
| Small size `n=1` | Height zero; two deepest/fixed states | Pass; abstract needs qualifier |
| Sharp extremal `n>=2` | Unique gap word `(n-1)` at minimum zero | Pass |
| `t>=height` | Image has exactly the `n+1` fixed states; singleton fibre equals its basin | Pass |

## Proof-index audit

For a target with `r+1` elements there are exactly `r` target gaps and hence
`r` forced source gaps `h_i+t`.  There are exactly `r+1` insertion slots:
before, between, and after those forced gaps.  Their forced span is
`b_r-b_0+tr`; subtracting it from `n-1-b_0` gives the manuscript's upper
coefficient limit.  The reviewer control reconstructs those slots by exact
total span rather than using the author's subset traversal.  It confirms the
`r+1` exponent, the inclusive coefficient sum, the negative-limit convention,
and the empty-target exception.  No indexing defect was found.

## Manuscript/control agreement

The author's image sizes, maximum-fibre examples, basin sizes, depth
histograms, and assertion-scale canonical record agree with the
process-separated gap control on their common range.  The exact source and
Round0 PDF hashes match the frozen artifacts.  No displayed theorem or proof
formula contradicted the reviewer transcript.  Only the two abstract-level
scope issues above remain.

## Source and contribution boundary

The manuscript explicitly subtracts strict/weak sequence shifts, stars and
bars, beta sets, bounded compositions, Fibonacci identities, and generic
functional-graph bookkeeping.  It labels the retained conjunction
`OWNER_AMBER`, states that a bounded non-hit is neither novelty nor priority
evidence, and retains `HOLD_EXTERNAL`.  That language is appropriately
bounded.  This review makes no new owner or novelty determination.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/reviews/paper186/reviewer_A_algebra/verify_review_A_p186.py
```

The byte-for-byte expected transcript is `CANONICAL.txt`.  `SHA256SUMS`
binds the report, delta template, verifier, and canonical transcript while
deliberately excluding itself.
