# Narrative report — fresh-map self-image erosion

**Lifecycle:** `HOLD_EXTERNAL`  
**Internal gate:** `PROVISIONAL_GREEN_OWNER_THIN`

## One-sentence result

For a labelled subset repeatedly intersected with its image under a freshly
resampled uniform endomap, the complete labelled transition kernel reduces to
a fixed-target Stirling-surjection refinement, while the top two size layers
force a genuine Jordan block and an endpoint-conditioned total-image mark
retains information that the subset process alone discards.  The aggregated
one-step size row itself is a direct extended-occupancy specialization and is
not counted as new progress.

## Literal process

Fix `n`.  Given the current `A subseteq [n]`, sample an independent uniform
map `f:[n]->[n]` and set

```text
A' = A intersect f(A).
```

Only `f|A` affects the update.  This is not the ordinary random-image chain
`A -> f(A)` and not intersection with an independent random mask.

## Claim spine

1. For fixed `B subseteq A` and `k=|f(A)|`, the exact restriction count is
   `binom(n-a,k-b) k! S(a,k)`.  Summing over `k` gives every labelled
   one-step endpoint.
2. Relabelling symmetry and nesting give every-time/every-labelled-target
   probabilities from an `(n+1)`-state cardinality quotient.
3. The full transition matrix has algebraic eigenvalues
   `lambda_a=a!/n^a` with multiplicity `binom(n,a)`.  The equality
   `lambda_(n-1)=lambda_n` and the positive `n -> n-1` coupling force a
   `J_2` block for every `n>=2`.
4. Marking `|f(A)|` before intersection gives a fixed-target subprobability
   polynomial.  Polynomial-kernel multiplication gives the aggregate, and a
   stabilizer bijection preserving every mark lifts it coefficientwise to
   each terminal target.  The generic product device earns zero credit.
5. For `n>=2`, every nonempty start except the separate `n=1` boundary is
   absorbed at the empty set almost surely; the CDF and mean are exact finite
   quotient formulas.

## Evidence and limitations

The standalone verifier enumerates every restriction on every subset through
the declared small boxes, compares the target-and-image-size counts to the
closed formula, checks full labelled powers against quotient powers, and
checks Jordan nullities with exact rational elimination.  These computations
are falsification evidence; the all-parameter proof is algebraic.

The exact row identity `Q_ab=Occ(b|a,a,a/n)`, specified-cell and
required-box occupancy, classical surjection counts, random mappings,
marked-kernel products, finite Markov-chain algebra, and lower-triangular
spectra receive zero contribution credit.  The shared shells of P158, P162,
P170, and P173 are likewise subtracted.  The bounded owner search found no
source for the remaining literal conjunction above, but a search non-hit is
not novelty, priority, or permission to circulate.
