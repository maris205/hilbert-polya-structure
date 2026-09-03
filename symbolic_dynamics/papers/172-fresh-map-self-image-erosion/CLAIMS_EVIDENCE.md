# Claims and evidence — P172

**Status:** `ROUND2 DUAL-REVIEW CLOSED / HOLD_EXTERNAL`

| ID | Exact claim | Proof route | Independent verifier attack |
|---|---|---|---|
| C1 | `H_n(a,b;k)=binom(n-a,k-b) k! S(a,k)` for every fixed endpoint and total image size | choose the exterior part of the image and count surjections | enumerate every map `A->[n]`, grouped by labelled endpoint and image size |
| C2 | `P^t(A,B)=(Q^t)_(a,b)/binom(a,b)` for `B subseteq A` | permutation equivariance within a size layer and monotone nesting | construct the full subset matrix and compare exact rational powers |
| C3 | algebraic spectrum `a!/n^a` with binomial layer multiplicities `binom(n,a)` | order subsets by size and read the triangular diagonal | compare every state self-loop and quotient diagonal |
| C4 | one `J_2` occurs in the size quotient at `lambda_(n-1)=lambda_n` | strict preceding diagonal ratios plus nonzero adjacent coupling | exact nullities of `Q-lambda I` and its square |
| C5 | absorption CDF and mean follow from `Q` | finite monotone-chain absorption and first-step recursion | exact quotient powers and rational linear recurrence |
| C6 | the fixed-target subprobability polynomial is `1_(B subset A)[Q(z_1)...Q(z_t)]_(a,b)/binom(a,b)` | marked Chapman--Kolmogorov multiplication for the aggregate, then a coefficientwise stabilizer bijection preserving every epoch mark | author one-step mark enumeration plus Review-B complete-history coefficient checks through `t=3`, `n<=4` |

The verifier proves no novelty statement.  Its role is to attack boundary,
normalization, labelling, and Jordan claims independently of the manuscript.

Review A additionally forced two scope repairs: the theorem now states
`n>=1` explicitly, and the source boundary subtracts the complementary
zero-indegree successive-elimination game rather than relying only on
random-mapping terminology.

Review B independently passed 20,317 exact assertions, including full-matrix
characteristic polynomials, `P L=L Q`, labelled powers, exact-domain Jordan
ranks, absorption means, and three-epoch coefficientwise marked histories.
It forced three owner/formalization repairs: the exact extended-occupancy
specialization `Q_ab=Occ(b|a,a,a/n)` is now zero credit; the fixed-target
marked polynomial and coefficientwise lift are formally stated; and
P158/P162/P170/P173 plus the shared quotient/Jordan/absorption shell are
explicitly subtracted.  These controls are falsification evidence, not
proofs, novelty evidence, or release authority.
