# P174 claims and evidence ledger

**Status:** `PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Logical rule:** proofs establish the all-parameter statements; computation
is independent counterexample pressure.

## Formal claims

Let `p` be prime, `2<=k<=p`, `X=C(P^1(F_p),k)`, and let `M` be the
minimum-pivot Möbius feedback map.

| ID | Claim | Proof dependency | Verifier contract | Status |
|---|---|---|---|---|
| C1 | The literal projectivity is a bijection for each proposed pivot and preserves the carrier. | elementary projective conventions | target size, distinctness, closure, forced inverse | proved |
| C2 | `im M=Z={S:infinity in S}`. | pivot maps to infinity; pivot-zero inverse for surjectivity | exact first image in all boxes | proved |
| C3 | `im M^2=Y={S:{0,infinity} subset S}` and `Y` is precisely recurrent. | infinity maps to zero; pivot zero on `Y`; inversion is involutive | exact second image, pointwise tails/periods | proved |
| C4 | `M^4=M^2` pointwise. | `M^2(X)=Y` and `M^2=id` on `Y` | every state in 69 complete boxes | proved |
| C5 | Depths `0,1,2` contain `C(p-1,k-2)`, `C(p-1,k-1)`, `C(p,k)` states. | membership in `Y`, `Z\Y`, `X\Z` | exact tail histogram | proved |
| C6 | For odd `p`, fixed count is `[u^(k-2)](1+u)^2(1+u^2)^((p-3)/2)`; the other recurrent states form 2-cycles. | two singleton and `(p-3)/2` paired inversion orbits in `F_p^*` | fixed and exact periods | proved |
| C7 | For `p=2,k=2`, the graph is one depth-two chain into a fixed state. | direct evaluation of all three states | three explicit boundary edges | proved |
| C8 | A target outside `Z` has zero fibre; for `R in Z`, valid pivots are exactly `0,...,h(R)-1`. | forced projective inverse and modular no-wrap equivalence | every target, every actual and predicted pivot | proved |
| C9 | The pivot-marked inverse is `1+z+...+z^(h(R)-1)`. | C8 plus one forced source per pivot | bit-exact pivot support and uniqueness | proved |
| C10 | Positive fibre-size distribution is `C(p-h,k-2)` and the maximum is `p-k+2`. | inversion relabels nonzero target points; largest-label census | all histograms and mass identity | proved |

## Exact verification boundary

`verify_p174.py` exhausts every state and target for every allowed `k` at

```text
p = 2,3,5,7,11,13,17,19.
```

This is 69 complete `(p,k)` boxes.  The frozen run performs 131,018,555
assertions and records an edge SHA-256 for every box.  Checks include:

- all literal edges and their proposed-pivot inverses;
- complete first and second images;
- every tail, eventual period, and the identity `M^4=M^2`;
- every fixed state and every two-cycle;
- every target fibre, including zero targets;
- uniqueness and exact initial-interval support of pivot marks;
- the full fibre-size distribution and total-mass identity;
- the complete smallest boundary graph.

## Zero-credit facts and engines

- the definition and elementary algebra of fractional-linear maps;
- dynamics of a fixed Möbius transformation;
- `PGL(2,q)` actions and projective-line subset or configuration orbits;
- inversion as an involution on `F_p^*`;
- binomial subset counts;
- ordered minimal/canonical images and canonizing elements for subsets under
  permutation-group actions;
- P96 fixed-base-map finite-subset machinery;
- P168 inverse-span/subspace machinery;
- AQN's generic adaptive-normalization/section/group-action architecture.

The residual under consideration is only the literal two-stage containment
tower together with the target-varying modular pivot interval.  The current
evidence does not upgrade this residual beyond amber.

## Statements excluded

- no novelty, priority, ownership, or freedom-to-operate conclusion;
- no claim that a bounded search non-hit is positive evidence;
- no projective-naturalness claim: the ordered prime-field representatives
  are part of the rule;
- no extension to prime powers, multisets, `k=1`, or `k=p+1`;
- no assertion that exhaustive computation replaces a proof;
- no public-circulation or submission authorization.
