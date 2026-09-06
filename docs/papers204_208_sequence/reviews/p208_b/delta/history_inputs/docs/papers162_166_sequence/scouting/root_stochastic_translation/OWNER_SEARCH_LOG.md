# RTI bounded owner and collision search

**Search date:** 2026-09-02 UTC  
**Disposition:** `NO_LITERAL_CONJUNCTION_HIT / FOCUSED_OWNER_GATE_REQUIRED`  
**Lifecycle:** `HOLD_EXTERNAL`

## 1. Search surface

Queries combined the literal update and its three coordinates:

- `A intersection (A+v) random translation finite vector space`;
- random binary erosion / random structuring element;
- iterated erosion by translated two-point structuring elements;
- random vectors span `F_2^d` / finite-field random matrix rank;
- translation stabilizer of a subset with erosion fibres; and
- every-target inverse enumeration for finite-group morphology.

The local P1--P161 corpus and all visible P162--P166 scout/kill ledgers were
searched for the literal map, translation intersections, random erosion,
history spans, and target translation stabilizers.  No literal match was
found.  A bounded non-hit is not novelty or priority evidence.

## 2. Direct inputs that receive zero credit

| Source | Material directly owned | RTI residual after subtraction |
|---|---|---|
| H. J. A. M. Heijmans and C. Ronse, *The algebraic basis of mathematical morphology I: Dilations and erosions*, DOI `10.1016/0734-189X(90)90148-O` | erosion as intersection of translates, group-invariant lattice framework, dilation/erosion algebra | no credit for naming the update an erosion or for the composition identity itself |
| H. J. A. M. Heijmans and J. Serra, *Convergence, continuity, and iteration in mathematical morphology*, DOI `10.1016/1047-3203(92)90032-O` | iteration and idempotent-limit questions for morphological operators | no generic iteration or convergence claim |
| G. V. Balakin, *The distribution of the rank of random matrices over a finite field*, DOI `10.1137/1113076` | finite-field random-matrix rank distribution | no credit for (2)--(4) as a standalone rank law |
| K. Sivakumar and J. Goutsias, *Binary random fields, random closed sets, and morphological sampling*, DOI `10.1109/83.503907` | stochastic/random-set setting for morphological sampling | no generic “random morphology” claim |

The bounded search did not locate a source combining random two-point
erosions on `F_2^d`, reduction of the whole history to its generated
subspace, the sharp `V\{0}` absorption law, and the target-stabilizer
polynomial (6).  This is only a scoped non-hit.

## 3. Internal collision subtraction

- **P109** studies deterministic image-subspace descent under a nilpotent
  linear operator.  RTI's state is an arbitrary subset, its randomness builds
  a subspace of translations, and its inverse statistic is `Stab(B)`.
- **P115** uses a deterministic Cartier operator and finite-linear rank data;
  no random erosion or coset-proper-subset inverse appears.
- **P158** intersects a graph with independent random cut graphs.  Its history
  object is a vertex signature/occupancy partition and its fibres use
  surjection counts.  RTI instead forms a linear span in the *translation
  group* and resolves arbitrary subset targets by their stabilizer subspace.
- **CNG**, killed in this same batch, is deterministic adjacent GCD/min erosion
  on a cyclic tuple and also has an exact earlier internal collision.  It has
  no random-span law or target-stabilizer inverse polynomial.
- Generic coordinate-death, coupon-collector, random-subspace intersection,
  and powerset direct-image systems do not transfer (6): membership events
  are coupled in whole affine `H`-cosets.

## 4. Honest owner gate

The erosion semigroup law and rank CDF are classical.  The claimed internal
increment is only their conjunction with:

1. the sharp worst-state witness `V\{0}`;
2. the full time/target/source-size polynomial indexed by translation
   stabilizers; and
3. exact recovery of stabilizer dimension from one-step inverse mass.

Promote only if an independent reviewer agrees that the coset inverse atlas
is not already a standard random-morphology theorem and that the P158
comparison is mechanism-level distinct.  Otherwise mark
`KILL_MORPHOLOGY_OR_INTERNAL`, not reserve.
