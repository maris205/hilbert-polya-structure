# Boxed plane-partition layer stripping — owner audit

**Audit date:** 2026-09-03 UTC  
**Scope:** bounded primary-source search, not a novelty or freedom-to-operate
opinion  
**External status:** `HOLD_EXTERNAL`

## Object searched

For an `a x b` weakly decreasing array `pi` with entries in
`{0,...,c}`, the proposed map is

```text
L(pi)_(i,j) = max(pi_(i,j)-1,0).
```

The proposed package combines the coordinatewise iterate and absorption
clock with bounded plane-partition counts, arbitrary-target fibres over a
skew complement, and a support-split convolution.  I also searched the
stronger formulation on all finite posets: a state is an order-reversing map
`f:P->{0,...,c}` and `L(f)=(f-1)_+`.

## Queries actually used

The search used combinations of the following literal and structural terms,
with separate searches for foundational and 2024--2026 material:

- `plane partitions remove bottom layer subtract 1 positive entries`;
- `plane partition layers level sets order ideals subtract one`;
- `skew plane partitions bounded height determinant`;
- `order polynomial support order ideals convolution bounded P-partitions`;
- `P-partitions chain of order ideals multichain zeta polynomial`;
- `plane partition dynamics order ideal erosion layers`;
- `reverse plane partitions dynamics bounded posets`;
- `Schur process plane partition slices`;
- `2025 2026 plane partition dynamics order ideal erosion`.

Searches were run against author pages, publisher/DOI pages, arXiv, and the
local P1--P163 portfolio.  A search non-hit is not treated as owner clearance.

## Primary and authoritative sources inspected

| Source | Inspected content | Allocation |
|---|---|---|
| R. P. Stanley, *Ordered Structures and Partitions*, Memoirs AMS 119 (1972), [DOI](https://doi.org/10.1090/memo/0119), [author PDF](https://math.mit.edu/~rstan/pubs/pubfiles/9.pdf) | bounded/order-reversing `P`-partitions, order polynomials, and their relation to order ideals | The finite-poset carrier and all order-polynomial notation are classical; zero credit. |
| R. P. Stanley, “Theory and Application of Plane Partitions: Part 1,” *Studies in Applied Mathematics* 50 (1971), 167--188, [DOI](https://doi.org/10.1002/sapm1971502167), [author PDF](https://math.mit.edu/~rstan/pubs/pubfiles/12-1.pdf) | ordinary plane partitions, row/column/part bounds, and the boxed product enumeration | The rectangle specialization and MacMahon product are classical; zero credit. |
| D. Brown, B. Elek, and I. Halacheva, “Cacti, Toggles, and Reverse Plane Partitions,” [arXiv:2412.02614](https://arxiv.org/abs/2412.02614), Definition 3.4 and Lemma 3.6 | a bounded RPP is an order-reversing labelling and is equivalently an increasing chain of order ideals | This makes the key owner collision explicit: `L` is just deletion/shift of the first level in that chain. |
| M. Plante and T. Roby, “Rowmotion on the Chain of V's Poset and Whirling Dynamics,” [arXiv:2405.07984](https://arxiv.org/abs/2405.07984), Definition 2.5 and Theorem 2.11 context | `k`-bounded `P`-partitions and the standard bijection with ideals of `P x [k]` | Confirms that the proposed generalization is the standard bounded-labelling carrier. Their whirling map is different; no direct-map claim is assigned to them. |
| C. Krattenthaler, “Enumeration of Lattice Paths and Generating Functions for Skew Plane Partitions,” *Manuscripta Math.* 63 (1989), 129--156, [DOI](https://doi.org/10.1007/BF01168868), [author PDF](https://www.mat.univie.ac.at/~kratt/artikel/skew.pdf) | definitions and determinantal generating functions for skew, reverse-skew, and column-strict variants | Skew-complement enumeration and determinant technology are owner-dense and receive zero credit. |
| S. Hopkins, “Order Polynomial Product Formulas and Poset Dynamics,” PSPM 110 (2024), 135--157, [DOI](https://doi.org/10.1090/pspum/110/02006), [author PDF](https://www.samuelfhopkins.com/OPAC/files/proceedings/hopkins.pdf) | current survey of order-polynomial products and genuine promotion/rowmotion dynamics on `P`-partitions | Confirms a crowded current interface. The proposed `L` is much thinner than the surveyed toggle dynamics. |
| A. Okounkov and N. Reshetikhin, “Correlation Function of Schur Process with Application to Local Geometry of a Random 3-dimensional Young Diagram,” *JAMS* 16 (2003), 581--603, [DOI](https://doi.org/10.1090/S0894-0347-03-00425-9), [arXiv](https://arxiv.org/abs/math/0107056) | plane partitions as partition-slice processes and determinantal background | Slice/Schur-process language and determinants receive zero credit. It does not directly study `L`. |
| R. Patrias and O. Pechenik, “Dynamics of Plane Partitions: Proof of the Cameron--Fon-Der-Flaass Conjecture,” *Forum Math. Sigma* 8 (2020), e62, [DOI](https://doi.org/10.1017/fms.2020.61) | boxed plane partitions as ideals in a product of three chains and nontrivial rowmotion dynamics | Separates the literal map: rowmotion is not `L`, but the plane-partition dynamics neighbourhood is established and dense. |

## Direct owner versus mechanism owner

The bounded search did not locate a paper whose headline map is exactly
`f -> (f-1)_+`.  That non-hit does not rescue the proposal.  The stronger
finite-poset translation shows that every claimed formula is a direct
restatement of classical multichain structure:

```text
I_r(f) = {x in P : f(x) >= r},       r=1,...,c,
I_1 superseteq ... superseteq I_c,
I_r(L^t f) = I_(r+t)(f).
```

Thus the proposed dynamics is a left shift of an order-ideal multichain.
The support-refined convolution is the decomposition of a multichain at its
`t`-th intermediate ideal, equivalently the ordinary convolution law for
powers of the zeta function of `J(P)`.  The target fibre is the lower segment
of that same multichain.  These are mechanism-owned, definition-level facts,
not a second theorem axis.

## Determinant decision

No explicit Gessel--Viennot/Krattenthaler determinant is promoted into the
candidate contract.  Determinantal enumerations for skew plane partitions
are classical, but a bounded, zero-based, weak/weak convention requires a
careful specialization or coefficient extraction.  The exact fibre is safely
and completely stated as the bounded order polynomial
`PP_(R/S)(t)`.  Adding a determinant would contribute no residual value and
would increase convention risk.

## Internal collision subtraction

| Internal item | Collision | Result |
|---|---|---|
| P113 principal-hook partition dynamics | integer-partition absorption plus transported fibres | Same broad clock/fibre format; not the literal map. Low-to-moderate subtraction. |
| P126 balanced composition refinement | cumulative depth census is a bounded-object count; all-time images and target fibres | Very close theorem silhouette. P126 still has a nontrivial canonical code and decoder; `L` has only scalar thresholding. Strong negative comparison. |
| P144 leftmost Dyck reassociation | exact iterate/clock plus target-resolved histories | Same package shape, but P144 has a nontrivial reassociation and unique inverse construction. `L` is strictly thinner. |
| P149 endpoint-peak extraction | all-rank images, right sections, clock, and target multiplicities | Rank-changing image/fibre template already occupied; different carrier and engine. Moderate subtraction. |
| P160 rectangular-corner stripping | coordinate iterate, unique zero, sharp clock, arbitrary-target forced core with free boundary objects, and image/support consequences | Closest collision. The proposed map replaces P160's two-dimensional crop and two-boundary inverse geometry by uniform scalar truncation. The principal proof and theorem interfaces transfer after replacing a rectangle crop with a height threshold. Decisive internal kill. |
| Historical PP1 scout (`docs/papers132_136_sequence/replacement_scout/combinatorial/SCOUT.md`) | simultaneous plane-partition corner removal killed as ordinary order-ideal Pop/peeling | Not the same literal update, but it is direct retained negative evidence against another elementary plane-partition erosion paper. |

## Owner verdict

```text
DIRECT_LITERAL_OWNER_FOUND  NO_IN_BOUNDED_SEARCH
MECHANISM_OWNER             YES
GENERAL_POSET_UPGRADE       KILL_DEFINITION_LEVEL
RECTANGLE_RESIDUAL          NONE_AFTER_MACMAHON_SKEW_RPP_SUBTRACTION
INTERNAL_CLOSEST            P160
FINAL                       KILL_DEFINITION_LEVEL_AND_INTERNAL_COLLISION
EXTERNAL                    HOLD_EXTERNAL
```

The failure is not mathematical.  It is a paper-threshold failure: after
classical bounded `P`-partitions, ideal multichains, order-polynomial/zeta
convolution, MacMahon, and skew-plane-partition enumeration are subtracted,
the dynamics contributes only the observation that subtracting one shifts a
height filtration.  There is no logically independent residual axis.
