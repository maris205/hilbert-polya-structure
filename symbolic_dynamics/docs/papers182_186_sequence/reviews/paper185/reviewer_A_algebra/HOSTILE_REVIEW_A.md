# Hostile Review A — P185

## Round1 delta disposition

**ACCEPTED.**  The process-separated delta review found that Round1 repairs
P185-A-MI-01 and introduces no new Critical, Major, or Minor finding.  The
current reviewer-owned verifier and `CANONICAL.txt` bind Round1 `main.tex`
SHA-256
`e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6`
and `main_round1.pdf` SHA-256
`fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3`.
Two clean-process runs reproduced the same 2,104,528-assertion transcript
byte for byte.  The original finding register below is retained as the
historical Round0 review record; its resolution is documented in
`DELTA_ACCEPTANCE_TEMPLATE.md`.

## Round0 frozen object and reviewer status

This is a **process-separated**, reviewer-owned audit.  It is not described
as an independent replication.  The reviewer read the frozen Round0 source,
PDF, author control, canonical transcript, proof package, claims ledger,
source-verification record, and QA documents.  No file under
`papers/185-prefix-diversity-delay/` was edited.

- Reviewed `main.tex` SHA-256:
  `a1fa39c5e83bba76af2100fdf27209414fdfb1c56bd7da36e6397c0a33657185`.
- Reviewed `main_round0_original.pdf` SHA-256:
  `45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129`.
- Control representation: equality partitions encoded by restricted-growth
  strings (RGSs), weighted by the number `(n)_k` of injections of their `k`
  blocks into the `n`-letter alphabet.
- Exhaustive control range: every RGS for `1 <= n <= 10`; literal iterates
  through `t=n+3`; exact weighted fibre mass on the full `n^n` carrier.
- Result: 2,104,525 exact assertions; zero formal counterexamples.

The control route is genuinely different from the author's labelled-word
loop.  In particular, at `n=10` it visits 115,975 equality partitions and
weights them to all `10^10` labelled words.  The all-distinct RGS class is
split into the identity word (clock zero) and the other `n!-1` permutations
(clock one), so aggregation does not erase the exceptional fixed point.

## Round0 decision (historical)

**Minor revision required.**  The formal theorems survived the hostile
control, including all endpoint products and all post-height iterates.  The
Round0 abstract and the “All-time every-target fibres” heading nevertheless
state a time scope broader than the displayed image/CDF/fibre theorems.

## Finding register

### Critical — 0

No critical finding.

### Major — 0

No major finding.

### Minor — 1

#### P185-A-MI-01 — “All-time” claim boundary is not stated piecewise

The abstract says without qualification that at time `t` the image has
`2^(n-t-1)` states and the clock CDF is `(n)_(n-t)n^t` (`main.tex`, lines
47–50).  Those formulas are formally stated only for `1 <= t <= n-1`
(lines 131–140 and 182–189).  At `t=0`, the image is the entire `n^n`-word
carrier and the clock CDF is one, so the unqualified abstract readings are
false.  For `t>=n`, the displayed exponents/falling-factorial indices are not
the intended stabilized formulas.  Likewise, the section headed “All-time
every-target fibres” (line 198) gives its product theorem only for
`1 <= t <= n-1` (lines 200–213), and the endpoint `t=n-1` silently uses the
empty-product convention.

This is not a counterexample to any formally quantified theorem.  It is a
localized scope defect in the paper's central branding and summary.  The
delta should either narrow “all-time” everywhere or add the missing trivial
pieces: at `t=0`, every target has one preimage; at `t>=n-1`, the sole image
target is `e`, with fibre `n^n`, and every other target has fibre zero.  The
abstract image/CDF formulas must carry their transient range, and the empty
product at `t=n-1` should be declared.

## Quantifier and boundary attack matrix

| Claim surface | Hostile control | Outcome |
|---|---|---|
| Carrier and totality, every `n>=1` | RGS weights sum exactly to `n^n` | Pass |
| Pointwise formula, every `t>=1` | Direct feedback on each partition output versus the delay formula, through `n+3` | Pass |
| Branch `r>=n` | Explicit checks at `t=n`, `n+1`, `n+2`, `n+3` | Pass |
| `t=0` | Identity map, `n^n` image targets, unit fibres, identity fibre one | Pass mathematically; omitted from the all-time inverse statement |
| Image for `1<=t<=n-1` | Exact target-set equality with all binary-rise paths | Pass |
| Stable image for `t>=n-1` | Singleton `{(0,1,...,n-1)}` at `n-1`, `n`, and `n+3` | Pass |
| Every-target fibres | Weighted partition fibres versus the local product, target by target | Pass |
| Fibre mass | Sum of all target fibres equals `n^n` at every tested time | Pass |
| Product endpoints | `t=n-1` empty product gives `n^n`; outside-image fibres vanish | Pass |
| Fixed/recurrent states | Exact fixed-word reconstruction inside each partition class; all classes reach `e` | Pass |
| Clock/CDF | Weighted clock census versus `(n)_(n-t)n^t`; identity fibre agrees | Pass on stated range |
| Small sizes | `n=1` height 0/deepest 1; `n=2` height 1/deepest 3 | Pass |
| Sharp extremal | For `n>=3`, depth `n-1` iff the first two positions share a block | Pass |

## Proof-index audit

The shift `r=t-1` is consistent.  A time-`t` target exposes
`d_0,...,d_(n-t)` by `d_j=y_(j+t-1)-(t-1)`.  Its genuinely constrained source
positions are `q=1,...,n-t-1`; the first source letter contributes `n`, and
the final `t` source coordinates contribute `n^t`.  Thus the front factor is
`n^(t+1)`, not `n^t`, and the product has exactly `n-t-1` factors.  The RGS
control found no off-by-one error.  It also checked the empty product at
`t=n-1` and the post-height full fibre.

## Manuscript/control agreement

The author's canonical histogram, image sizes, maximum-fibre examples,
carrier mass, and fixed/deepest counts agree with the process-separated RGS
control on their common range.  The source and Round0 PDF hashes above match
the frozen artifacts.  No manuscript number contradicted the reviewer
transcript.  The only disagreement is the scope language recorded as
P185-A-MI-01.

## Source and contribution boundary

The manuscript explicitly gives restricted-growth/set-partition encodings,
prefix statistics, falling factorials, and generic finite-map bookkeeping no
contribution credit.  It labels the retained conjunction `OWNER_AMBER`, says
that a bounded non-hit is neither novelty nor priority evidence, and retains
`HOLD_EXTERNAL`.  Those are appropriately limited statements.  This review
does not turn the bounded owner search into a novelty claim and makes no new
owner determination.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/reviews/paper185/reviewer_A_algebra/verify_review_A_p185.py
```

The byte-for-byte expected transcript is `CANONICAL.txt`.  `SHA256SUMS`
binds the report, delta template, verifier, and canonical transcript while
deliberately excluding itself.
