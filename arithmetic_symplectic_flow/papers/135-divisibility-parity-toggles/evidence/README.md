# Evidence — ASFS-SCOUT-20260914-98

**Status:** `PRE-P0 STOP — PRODUCT-TOPOLOGY DISCONTINUITY; EMPTY-SEED RANK ESCAPE`  
**Route:** A0/A1/A2 `UNASSIGNED`; formal coordinates `NOT EVALUATED`;
Route B `NOT INVOKED`.

## Exact inputs and method

The inputs are the [frozen card](../candidate-card.md): all downsets of integer
divisibility, vertex-count intrinsic rank, odd then even simultaneous toggles,
and the product topology. The rank convention was explicitly disambiguated
before the audit. There is no cutoff, parameter search, prime file, fitted
arithmetic word, or floating-point computation.

Reproduction consists of the following exact checks in the [paper](../paper.md):

1. Express toggle eligibility using immediate lower and upper covers. Check
   that opposite cover parities leave these tests unchanged in a half-step.
2. Check the two possible dangerous changes on a cover edge to prove downset
   preservation, then apply the unchanged eligibility tests twice.
3. Compare downarrow(2q_j) with {2} as distinct odd primes q_j tend to infinity.
   Read the coordinate 2 after each half-step. Repeat with downarrow(4q_j)
   and downarrow(4), reading coordinate 4 for the inverse.
4. Enumerate only eligible ranks for the exact ideals I_k={rank<=k}; compose
   their two scalar boundary changes and use 2^{k+1} to prove distinctness.

No finite truncation is used as evidence for the infinite claims. Finite
graded-poset permutations and the full fixed ideal are explicit controls.
This audit stops before general periodic classification or a topology change.

## Sources and ownership

The [prior-work guide](../../../docs/prior_work/README.md) supplies the
prime-symbolic admissibility lineage. [132](../../132-divisibility-rowmotion/paper.md)
supplies the immediate comparison object and its different non-surjectivity
obstruction. All mathematical assertions needed for the new action are proved
directly here; no primary literature theorem, finite-toggle period, geometric
map, roof, or determinant is imported. No literature-wide novelty claim is
made.

Local link and status checks verify package consistency only. They do not
prove the mathematical propositions, which are established by the displayed
arguments. Any independent model check is not external peer review.

The [separate-context 135--137 check](../../137-sieve-mask-translation/evidence/review-three-screens.md)
found no blocking defect in the scoped proofs; its input identities and
review limitations are recorded there.
