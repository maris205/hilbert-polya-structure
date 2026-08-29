# Claims and evidence — P114

| Manuscript claim | Symbolic evidence | Exact finite evidence |
|---|---|---|
| peeling clock equals component height, with empty height zero | Lemma 2.1, induction on descendant height plus empty case | every orbit for `0<=n<=6` |
| basin formula `B_(n,r)` | all-minors matrix-tree determinant | every fixed endpoint and basin |
| bounded-depth EGF | labelled-set decomposition | exact `Fraction` series for every endpoint/height cell |
| local-fibre formula | attachment characterization plus inclusion–exclusion | every target in all seven lanes |
| only fixed recurrence and zeta exponent `2^n` | strict loss outside edgeless forests | complete functional graphs |
| for `n>=2`, maximum depth and `n!` deepest shell; explicit `n=0,1` exceptions | height extremality forces a rooted Hamilton path | literal depth histograms |

Canonical evidence files are `code/verify.py` and
`code/verification_output.txt`.  Computation is a hostile finite control, not
a substitute for the arbitrary-`n` proofs.

Parallel `RAKE`/height pruning, Cayley and all-minors tools, height
enumerations and nested EGF, generic inclusion–exclusion, absorption/zeta
conversion, and elementary Hamilton-path extremality receive zero
novelty/priority credit.  Only the endpoint-indexed assembly and elementary
`(m,s)` fibre calculation are retained as residual internal scope, still
without a priority determination.
