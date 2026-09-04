# Hostile Review B — P186 rank-compression support dynamics

**Reviewer process:** `/root/reviewer_b_p185_p186`, process-separated from the
P186 author and P186 Review A  
**Review date:** 2026-09-03 UTC  
**Frozen input:** immutable Round 1  
**Decision:** `ACCEPT_ROUND1_FOR_COORDINATOR_GATE`  
**External lifecycle:** `HOLD_EXTERNAL`

## Bottom line

The Round-1 theorem package is provable as stated.  I found zero Critical,
Major, and Minor defects after reopening ordered gap erosion at every time,
the clock and basins, every image and every carrier target fibre, coefficient
indices and negative budgets, the one-step binomial and Fibonacci
specializations, every depth CDF, `n=1,2` boundaries, the unique extremal,
the repaired abstract, sources, owner language, and artifact state.

This review authorizes only the next internal coordinator gate.  It does not
authorize circulation or submission and does not convert a bounded search
non-hit into novelty, priority, completeness, freedom-to-operate, or
validated-subclass evidence.  P186 remains `OWNER_AMBER / HOLD_EXTERNAL`.

This is process separation, not a claim of statistically independent error
processes.  The three controls share the theorem contract and runtime even
though they encode the carrier and reconstruct fibres differently.

## Frozen binding and read-only discipline

No file under `papers/186-rank-compression-support/` was edited.  This review
binds:

| frozen object | SHA-256 |
|---|---|
| `main.tex` | `e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394` |
| `main_round1.pdf` | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` |

The live `main.pdf` is byte-identical to Round 1.  The immutable Round-0 PDF
still has SHA-256
`6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431`.
The four-row Review-A manifest passes and its delta record closes both
historical abstract findings against the same Round-1 hashes.

The paper-local fifteen-row manifest is still deliberately Round-0-bound at
this intermediate stage: thirteen rows pass, and only the repaired `main.tex`
and rebuilt live `main.pdf` rows retain old hashes.  This is not a mathematical
finding against the immutable Round-1 input, but it is a terminal-QA
obligation.  The coordinator must regenerate the final paper manifest after
Round 2; external release remains blocked if that does not occur.

## Reviewer-owned representation

The verifier imports neither earlier control and excludes both earlier state
spaces:

- the author traverses subset bit masks;
- Review A stores a minimum followed by a positive gap composition and counts
  inverse slots recursively;
- Review B stores a `k`-set as the weakly increasing rank profile
  `b_j=a_j-j`, equivalently a partition in a `k` by `n-k` rectangle.

The disjoint union of these rectangle profiles has
`sum_k binom(n,k)=2^n` elements.  If `c_0<...<c_s` are the distinct values in
the weak profile, one step in profile coordinates is

\[
 (b_j)_j\longmapsto(c_i-i)_i.
\]

Thus the literal dynamics can be iterated without constructing a subset mask
or a positive-gap word.  Actual target points are decoded only at the audit
boundary by adding rank back.

For the inverse formula, Review B does not use Review A's slot recurrence.
Writing `r=|B|-1` and

\[
 D=n-1-b_r-tr,
\]

it expands by the total number `ell` of optional short gaps:

\[
 (1-S_t(z))^{-(r+1)}
   =\sum_{\ell\ge0}\binom{\ell+r}{r}S_t(z)^\ell.
\]

The number of length-`ell` words over `{1,...,t}` with sum at most `D` is
recomputed by the signed inclusion-exclusion identity

\[
 \sum_{j=0}^{\ell}(-1)^j\binom{\ell}{j}
                  \binom{D-jt}{\ell}.
\]

Summing their product over `ell` yields the manuscript's inclusive coefficient
sum through a route distinct from direct predecessor traversal, polynomial
multiplication, and weak-slot recursion.

## Exact audit coverage

The control exhausts every weak rank profile for `1<=n<=17`, every time
`0<=t<=n+3`, and **every carrier target**, including targets whose coefficient
budget is negative and whose observed fibre must be zero.  It makes
**16,766,548 exact assertions**.  A separate full traversal of all 262,144
rank profiles at `n=18` checks the paper's displayed orientation numbers:
6,765 first-image targets, 19 fixed states, maximum first fibre 2,002, and the
unique depth-17 state `{0,17}`.  Symbolic boundary identities are additionally
checked through `n=64`.

Two fresh processes reproduced `CANONICAL.txt` byte for byte.  Each transcript
has SHA-256
`b8d4d9a233be1fe64f121d85f83f77f06a798b49a9b14dc69cf3688fbf2e199a`.

## Hostile theorem audit

### 1. Ordered erosion and all-time pointwise law

In rank-profile coordinates, an original consecutive point gap is

\[
 g_j=(b_j+j)-(b_{j-1}+j-1)=b_j-b_{j-1}+1.
\]

At time `t>=1`, a rank jump `delta=b_j-b_{j-1}` survives exactly when
`delta>=t`, equivalently `g_j>t`, and contributes
`delta+1-t=g_j-t`.  Profile iteration and this closed reconstruction agree
for every state and time in the exhaustive boxes.  Order is preserved because
the surviving jumps are processed in their original index order; no hidden
sorting or merger occurs.

The empty profile stays empty and the leading value `b_0=a_0` remains the
minimum.  The repaired abstract now says “exactly when `g>t`” and cannot be
read as retaining a zero or negative gap.

**Verdict:** survives.

### 2. Clock, recurrent set, basins, and unique extremal

The last surviving original point gap vanishes at its own value, so the least
entrance time is the maximum `b_j-b_{j-1}+1`.  Every nonempty state retains its
minimum and reaches that singleton; the empty state remains in its own basin.
The profile census gives basin size `2^(n-m-1)` for every minimum `m`, exactly
one empty-basin state, and precisely `n+1` fixed/recurrent states.

For `n>=2`, depth `n-1` requires a rank jump `n-2`.  The rectangle bounds then
force the unique profile `(0,n-2)`, which decodes to `{0,n-1}`.  At `n=1`, both
the empty profile and `(0)` are fixed at depth zero; the abstract's repaired
`n>=2` qualifier is therefore necessary and now correct.  At `n=2`, the
unique depth-one profile decodes to `{0,1}`.

**Verdict:** survives.

### 3. All-time images and coefficient indices

For `B={b_0<...<b_r}`, the `r` surviving source gaps consume
`(b_r-b_0)+tr` span beyond the invariant minimum.  The remaining budget is

\[
 (n-1-b_0)-(b_r-b_0)-tr=n-1-b_r-tr=D.
\]

Therefore feasibility is exactly `D>=0`, or `b_r+tr<n`.  The control obtains
literal image-set equality at every tested time.  Counting `(r+1)`-element
targets from `{0,...,n-1-tr}` gives the displayed binomial image sum.

For every one of the `2^n` carrier targets, the observed predecessor count is
compared with the signed inclusion-exclusion evaluation above.  This checks:

- exponent `r+1`, matching the number of before/between/after slots;
- exactly `r` forced long gaps and the additive term `tr`;
- the inclusive coefficient range `0<=s<=D`;
- zero for every negative budget;
- the separately stated unique empty-target predecessor.

At `t=0`, `S_0=0`, only the `ell=0` term remains, and all `2^n` targets have
fibre one.  At `t>=n-1`, only the empty target and `n` singletons remain, with
their exact basin fibres.  Fibre mass is `2^n` at every tested time.

**Verdict:** survives.

### 4. One-step binomial and Fibonacci specializations

At `t=1`, every optional short gap equals one.  The inclusion-exclusion
calculation reduces target-by-target to

\[
 |T_n^{-1}(B)|=\binom{n-\max B}{|B|}.
\]

The image sum gives `2,3,5,...,4181` through `n=17` and 6,765 at `n=18`,
matching `F_{n+2}` including the empty target.  Every nonempty one-step target
is checked individually, rather than only checking the total image size.

**Verdict:** survives.

### 5. Bounded-gap depth CDF

Review B evaluates bounded positive words of a fixed length and exact span by
inclusion-exclusion, weights each span `s` by its `n-s` possible minima, then
adds the empty state.  This agrees with the literal profile clock census for
every `0<=h<=n+1`.  It gives `C_n(0)=n+1`, full mass at `h=n-1`, and every
positive shell as the difference of consecutive CDFs.  No asymptotic or
average-fibre inference is used.

**Verdict:** survives.

## Source and owner-language audit

Both cited sources resolve and are used only for background that the paper
assigns no contribution credit.  The
[Cambridge University Press record for Stanley, Volume 1, second edition](https://www.cambridge.org/core/books/enumerative-combinatorics/3155CDE1D973D49F873BDE2EAF8D7651)
matches the book DOI and enumerative-combinatorics scope.  The
[Springer record for Fayers](https://link.springer.com/article/10.1007/s00026-022-00577-4)
confirms the 2023 volume/pages, 2022 online publication, and explicit beta-set
background.  Neither source is represented as proving the autonomous support
iteration.

Review B reran four bounded exact-phrase/structural web queries:

1. `"rank-compression support" dynamics subset`;
2. `"a_j-j" support iteration subset`;
3. `"support" "a_j-j" subset map`;
4. `"gap erosion" subset dynamics finite`.

The results were unrelated rank compression, physical erosion, and uses of
similar symbols; no literal or equivalent owner was identified.  This is only
a bounded public-web non-hit.  It is not a professional database or
citation-chain search and provides no novelty, priority, completeness, or
freedom-to-operate conclusion.

The manuscript explicitly subtracts strict/weak sequence shifts, stars and
bars, beta sets, bounded compositions, Fibonacci summation, and generic
functional-graph bookkeeping.  It retains `OWNER_AMBER`, states that its
search is bounded, and denies novelty and priority consequences.

**Verdict:** sources and lifecycle wording survive; `HOLD_EXTERNAL` retained.

## Artifact and declaration audit

The frozen Round-1 PDF is 306,590 bytes, three A4 pages, unencrypted, and has
no JavaScript.  All 24 font rows are embedded and subset.  Its metadata title
and author fields are blank.  Text extraction finds both owner/hold notices,
data availability, ethics, and AI-use declarations.  Current LaTeX and BibTeX
logs contain no undefined references/citations, warning diagnostics, or bad
boxes.

The source is anonymous, contains both repaired abstract phrases, handles the
empty target before introducing `b_0,...,b_r`, and expressly interprets a
negative coefficient upper limit as zero.  It calls finite verification
falsification pressure rather than proof.

## Findings ledger

### Critical findings (0)

None.

### Major findings (0)

None.

### Minor findings (0)

None.

No manuscript repair is requested.  A byte-identical Round-2 receipt is
acceptable.  Any content change for another reason reopens every proof,
source, artifact, and reproducibility gate.

## Residual risks that are not findings

1. Finite rank-profile checks are bounded falsification pressure, not a proof
   of the all-`n,t` claims; the written gap argument carries those quantifiers.
2. Process separation and coordinate diversity do not establish statistically
   independent errors.
3. The paper-local manifest must be regenerated at terminal QA after the
   staged Round-1 repair.
4. Ownership remains amber pending a deeper database and citation-chain
   search.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/reviews/paper186/reviewer_B_rootspawn/verify_review_b_p186.py
```

The byte-for-byte expected transcript is `CANONICAL.txt`.  `SHA256SUMS`
binds the report, delta template, verifier, and canonical transcript while
deliberately excluding itself.

