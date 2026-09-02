# P165 Review B — fresh owner and internal-collision audit

**Date:** 2026-09-03  
**Result:** `OWNER_THIN NON-HIT / NO INTERNAL COLLISION FOUND`  
**Lifecycle:** `HOLD_EXTERNAL`

This is a fresh bounded search performed for Review B.  It does not convert
a search non-hit into a novelty, priority, or publication claim.

## 1. Search envelope

The search used combinations of the following terms, including exact-phrase
variants:

```text
low-weight codewords hitting set shortening minimum distance
union supports codewords weight less than twice minimum distance
support 2d shortening linear code
iterated shortening linear codes minimum distance
repeatedly shorten support low-weight words
autonomous dynamical system linear codes shortening
residual code support minimum weight word
all-time image target preimage shortening linear code
```

The search also inspected the current P1--P165 directory inventory, the
P157--P161 historical-occupancy and collision ledgers, current P162--P165
review collision records, and the closest papers at source level.

## 2. Primary/background records and subtraction

### Direct nearest owner

M. Jibril, M. Tomlinson, C. J. Tjhai, M. Z. Ahmed, and S. Bezzateev,
*Some new codes from binary Goppa codes and a method of shortening linear
codes*, IET Communications 7 (2013), 270--277,
[DOI 10.1049/iet-com.2011.0693](https://doi.org/10.1049/iet-com.2011.0693).
The article develops low-weight-codeword hitting sets and generalized
distance-increasing shortening.  Taking the protected range through
`2d-1` supplies the one-step principle used by P165.  Therefore Review B
assigns zero contribution credit to selecting/hitting the entire support of
sub-double-weight words and to the resulting one-step lower bound
`d(T(C))>=2d(C)`.

### Nearby operations

M. Grassl and G. White, *New good linear codes by special puncturings*, ISIT
2004, p. 454,
[DOI 10.1109/ISIT.2004.1365491](https://doi.org/10.1109/ISIT.2004.1365491),
owns the neighboring use of low-weight support information for special
puncturing.  P165 correctly distinguishes its padded shortening from
puncturing.

Y. Liu, C. Ding, and C. Tang, *Shortened linear codes over finite fields*,
[arXiv:2007.05901](https://arxiv.org/abs/2007.05901), develops general
shortening theory and families over finite fields.  It reinforces that
ordinary finite-field shortening is background.  The inspected record did
not state P165's autonomous union-support self-map, its iterated image
criterion, or its extremal inverse classification.

A. Vardy, *The intractability of computing the minimum distance of a code*,
IEEE Transactions on Information Theory 43 (1997), 1757--1766,
[DOI 10.1109/18.641542](https://doi.org/10.1109/18.641542), supports the
manuscript's explicit disclaimer that no efficient general-code algorithm is
claimed.

### Mandatory zero-credit list

- Hamming weight, support, minimum distance, direct sums, repetition lines,
  puncturing, and shortening;
- hitting low-weight codewords through selected coordinates;
- removing every word below a distance threshold so that a surviving code
  has at least that threshold as its minimum distance;
- specifically, the entire one-step `d -> at least 2d` route;
- Gaussian enumeration of finite subspaces, elementary geometric sums, and
  generic termination of strict descent on a finite lattice.

## 3. Residual owner gate

After the subtraction above, the bounded search did not find a source for
the conjunction of:

1. the literal autonomous map that recomputes the union of all current words
   with weight strictly below twice the current distance;
2. the sharp global height `floor(log_2(n+1))` from disjoint dyadic purge
   layers;
3. the all-time, every-nonzero-target image equivalence
   `d(D)>=2^t` and `z(D)>=2^t-1`; and
4. the iff classification and prime-power count of sources simultaneously
   minimizing added dimension and added support.

No direct owner of the literal iteration, item 3, or item 4 was located.
This is an `OWNER_THIN` bounded non-hit only.  A later direct owner would
reopen the gate and could be Critical.

## 4. Internal P1--P165 collision attack

The audit treated shared phrases such as “finite dynamics,” “sharp clock,”
“subspace,” and “exact fibre” as zero separation evidence.  The closest
literal/proof-engine comparisons are:

| occupied paper | genuine overlap | why its theorem does not transfer |
|---|---|---|
| P98, equal-block-sum torsion shifts | linear constraints and finite cyclic modules | reversible block-sum torsion has no adaptive support kernel, descending code lattice, or dyadic extension atlas |
| P100, least-valuation digit erasure | state loss governed by a numerical threshold | digit deletion uses a fixed valuation selector; no minimum-distance recomputation or code-valued target condition |
| P102, cyclic group-algebra involution norm | finite algebra/code-adjacent carrier | a fixed norm-like group-algebra operator and recurrent algebra, not shortening on the current weight spectrum |
| P109, nilpotent-image subspace dynamics | full finite-field subspace lattice, absorption, every-target fibres | `U -> N(U)` iterates one fixed linear map and is solved by kernel flags/Gaussian incidence; P165 changes the coordinate kernel with the entire current code and uses distance plus zero-coordinate capacity |
| P115, bounded Cartier dynamics | finite-field linear coordinate selection and image flags | a fixed Cartier decimation with a Frobenius recurrent core; no support-union feedback or dyadic line extensions |
| P137, rank-feedback p-group splitting | strongest clock silhouette: a state parameter grows resource costs, plus target fibres | additive triangular part splitting on isomorphism types differs from multiplicative distance growth on labelled code subspaces; its inverse grammar cannot yield P165's target distance/zero-capacity iff or full-support-line rigidity |
| P143, Boolean row-inclusion residual | support/incidence data and exact inverse language | relation self-residuation has a depth-one preorder image and Boolean-lattice embeddings; it is neither a subspace restriction nor a weight threshold |
| P157/P161, finite-ring/finite-field collapse | arithmetic finite carriers and sharp boundaries | cubic Hensel branches and affine orthocenter windows do not act on code lattices and share no inverse engine |
| P162, random translation intersection | subspaces and target-resolved histories | stochastic erosion is indexed by the span of translations and target stabilizers; P165 is deterministic adaptive shortening |
| P163, complemented shadows | rank resources and all-time inverse formulas | Boolean-rank shadow/complement recurrence has a periodic core and product kernels, not descending code support layers |
| P164, cyclic equality feedback | q-ary words, affine-code fibre enumerators, sharp height | its tail is a fixed Rule-102 operator on individual words; P165 evolves whole subspaces with a nonlinear current-distance selector |

The killed Schur-power and code-hull candidates were also checked.  P165 is
neither a code product/power nor an orthogonality retraction.  The historical
occupancy ranges covering P1--P156 and the current P157--P165 sources show no
literal duplicate.  The generic silhouette “strict descent plus a growing
resource budget” receives no credit, but it does not transfer the targetwise
iff or simultaneous-equality theorem.

## 5. Adjudication

The paper's source boundary at `main.tex:73--82` is accurate and
conservative: it expressly credits Jibril et al. and assigns the whole
one-step mechanism zero contribution credit.  The paper makes no claim of
absolute novelty and visibly retains `HOLD_EXTERNAL`.  No provenance repair
is requested in Review B.
