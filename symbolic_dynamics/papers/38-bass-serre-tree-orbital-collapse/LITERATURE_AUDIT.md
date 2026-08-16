# Paper 38 literature audit — SD-C40

Research cutoff: 2026-08-15.

## 1. Question and source policy

The audit asks whether primary literature already supplies the frozen
combination of a presentation-canonical `BS(1,r)` Bass--Serre full-tree
geodesic ledger, a same-object ordinary Fredholm determinant, and a
source-selective modular primitive sector.

Claims are attributed only to publisher, journal, DOI, official author, or
arXiv records.  Search snippets guide discovery but do not own theorem
statements.  Published versions are preferred when available.  The audit
separates five neighboring categories: Bass--Serre geometry, discrete
tree-lattice zeta, infinite weighted/measure-graph determinants, group
conjugacy growth, and newer graph-of-groups or double-coset zetas.

## 2. Closest primary sources

| Primary source | Established content used or compared | Boundary to SD-C40 |
|---|---|---|
| Serre, *Trees* (1980), DOI `10.1007/978-3-642-61856-7` | Bass--Serre theory for amalgams and HNN extensions | Owns the geometric language; a tree itself has no positive reduced closed path. |
| Bass, *The Ihara--Selberg zeta function of a tree lattice* (1992), DOI `10.1142/S0129167X92000357` | Primitive hyperbolic classes and determinant formulas for tree lattices | For `r>=2` the faithful image is non-discrete.  For `r=1` the image is a discrete translation `Z`, but the frozen `Z^2` action has kernel `<u>`, is non-proper, and fails finite-stabilizer hypotheses unless the acting group is quotiented. |
| Clair and Mokhtari-Sharghi, *Zeta Functions of Discrete Groups Acting on Trees* (2001), DOI `10.1006/jabr.2000.8600` | Von Neumann determinants for discrete tree actions under edge/end finiteness hypotheses | Gives the decisive image-discreteness, finite-stabilizer, end-kernel, and determinant-category boundary; its subgroup criterion must be applied to the faithful image, and it is not an ordinary full-tree Fredholm result. |
| Deitmar, *Ihara Zeta Functions of Infinite Weighted Graphs* (2015), DOI `10.1137/140957925` | Fredholm formulas for infinite graphs of finite total weight | A canonical invariant weight on the transitive full tree has infinite total mass; a radial summable weight chooses a basepoint and changes the object. |
| Lenz, Pogorzelski, and Schmidt, *The Ihara Zeta Function for Infinite Graphs* (2019), DOI `10.1090/tran/7508` | Measure graphs, groupoid action, noncommutative integration, and determinant formula | Supplies a different trace and determinant category, not the ordinary full-tree Fredholm determinant. |
| Fima, Le Maître, Moon, and Stalder, *A Characterization of High Transitivity for Groups Acting on Trees* (2022), DOI `10.19086/da.37645` | HNN Bass--Serre models and action-type geometry, including ascending common-end behavior | Supports the quasi-parabolic/common-end classification; it does not create full-tree periodic cycles. |
| Abbott, Balasubramanya, and Rasmussen, *Valuations, Completions, and Hyperbolic Actions of Metabelian Groups* (2024), DOI `10.1112/jlms.12916` | Explicit valuation-tree representatives for `BS(1,n)` and alternative divisor splittings | Confirms the main tree and makes the composite-`r` alternative-tree temptation explicit; the source lock forbids switching splittings. |
| Ciobanu, Evetts, and Ho, *The Conjugacy Growth of the Soluble Baumslag--Solitar Groups* (2020), NYJM 26, 473--495 | Geodesic conjugacy representatives and word-length conjugacy growth for `BS(1,k)` | Direct prior art for conjugacy, but its word-metric growth series differs from the height-only orbital product. |
| Guo, *The Conjugacy Ratio of Abelian-by-Cyclic Groups* (2026 issue), DOI `10.1017/S0013091525100977` | Explicit fixed-height congruence criterion in `BS(1,k)`: multiplication by powers of `k` modulo `k^n-1` | Directly anticipates the residue-orbit classification; that classification is not claimed as novel here. |
| Hong and Kwon, *Zeta Functions of Geometrically Finite Graphs of Groups* (2023), arXiv:2302.08850 | Zetas of quotient graphs of groups arising from cuspidal tree lattices | A quotient/tree-lattice category with different state space and hypotheses. |
| Marchionna, *Double-Coset Zeta Functions for Groups Acting on Trees* (2026), DOI `10.1016/j.jalgebra.2026.02.014`, arXiv:2409.01860 | Double-coset Dirichlet series and determinant formulas from local action data | The closest current alternative invariant, but not a primitive full-tree geodesic Fredholm determinant. |

## 3. Literature synthesis by object category

### Bass--Serre tree versus quotient geometry

Serre supplies the canonical tree attached to the original presentation.
Abbott and coauthors show that the same metabelian group can admit several
tree actions when composite parameters allow different divisor splittings.
That richness does not help the frozen question: changing to another tree
would violate source lock.  The main theorem uses only the original HNN
incidence indices `1` and `r`.

### Tree-lattice zeta and determinant ownership

Bass and Clair--Mokhtari-Sharghi count hyperbolic/orbital data for discrete
tree lattices.  Their theory is not evidence that the raw full-tree
Hashimoto operator is trace class.  For `r>=2`, the Bass--Serre action is
faithful and its image in the automorphism group is non-discrete because its
vertex stabilizer is infinite.  The balanced case is different:
`G_1=Z^2` acts on a line with kernel `<u>` and discrete translation image
`Z`.  The original `G_1` action still has infinite vertex and edge
stabilizers and is non-proper, so it fails the finite-stabilizer tree-lattice
action hypotheses.  Passing to the discrete image quotients the acting group
and changes the orbital ledger.  This two-case boundary, rather than a
blanket non-discreteness claim, is what an object-safe comparison must
preserve.

### Infinite graph determinant alternatives

Deitmar obtains ordinary Fredholm formulas by imposing finite total weight.
Lenz, Pogorzelski, and Schmidt instead use invariant measures and
noncommutative integration.  Both lines demonstrate that infinite graphs can
carry rigorous zetas, but only after specifying an appropriate summability or
trace framework.  Neither licenses an undamped ordinary determinant on the
full regular tree.  A source-invariant modular step weight is bounded away
from zero on an infinite orbit and fails the needed summability.

### Conjugacy and the necklace substitute

Ciobanu, Evetts, and Ho already analyze conjugacy growth for the same soluble
Baumslag--Solitar groups in the standard word metric.  Guo's current paper
states the fixed-height congruence used here.  Once this congruence is known,
Burnside's lemma and necklace enumeration yield the rational height-only
product routinely.  The scoped addition is not the congruence or necklace
identity, but the demonstration that this attractive product is a different,
generic object and cannot rescue the failed full-tree Fredholm obligation.

### Current graph-of-groups and double-coset work

Hong--Kwon and Marchionna show active interest in zetas derived from quotient
graphs of groups, local action data, and double cosets.  Those constructions
reinforce the need to type the counted objects.  They do not collide with the
negative same-object theorem; importing them would replace the candidate.

## 4. Claim-level novelty boundary

| Claim ID | Assessment | Source-locked interpretation |
|---|---|---|
| `SD-C40-C1` full tree has no periodic geodesic | Classical / elementary | Used as a decisive object test, not claimed as new graph theory. |
| `SD-C40-C2` full-tree Hashimoto noncompactness | Elementary analytic consequence | The explicit orthogonal-column proof closes ordinary Fredholm ownership on the frozen object. |
| `SD-C40-C3` action/tree-lattice hypotheses fail | Established hypothesis boundary | Clair--Mokhtari-Sharghi tie subgroup discreteness to stabilizers in the faithful image: the image is non-discrete for `r>=2`; at `r=1` it is discrete, but the frozen action has infinite kernel, is non-proper, and fails the finite-stabilizer hypotheses. |
| `SD-C40-C4` fixed-height residues and necklace product | Low positive novelty | Guo supplies the congruence; Burnside/Möbius produce a generic rational collapse. |
| `SD-C40-C5` integrated object/marker/determinant no-go | Narrow negative synthesis | The defensible contribution is the typed terminal theorem and branch decision, not a new zeta construction. |
| Arithmetic recognition mechanism | None | Prime/composite controls obey one index law; balanced control diverges. |

Novelty-safe sentence:

> For the original ascending-HNN Bass--Serre object of `BS(1,r)`, the literal
> full-tree primitive ledger is empty and its Hashimoto operator is not an
> ordinary Fredholm object; replacing recurrence by group conjugacy yields
> only a generic necklace product (or balanced divergence) under an
> incompatible tree-edge clock.

## 5. Attribution and language firewall

Do not claim a new Bass--Serre theory, tree-lattice zeta, infinite-graph
Fredholm theory, conjugacy criterion, necklace identity, or double-coset zeta.
Do not call a quotient/von Neumann/groupoid determinant the ordinary
full-tree determinant.  Do not describe a path that closes modulo the group
as a periodic point of the raw edge shift.

Forbidden claims include prime selection, an arithmetic Euler product,
functional equation, analytic continuation beyond the displayed rational
substitute, target-zero alignment, a self-adjoint carrier, critical-line
localization, RH consequences, or a universal no-go for every invariant of
Baumslag--Solitar groups.

## 6. Assessment

The candidate should proceed only as a negative branch-closure theorem.
Every positive component is either classical, directly anticipated, or a
routine necklace consequence.  The useful result is the disciplined
separation of full-tree periodicity, group-orbital recurrence, determinant
categories, and markers.  Route A is rejected, Route B stays locked, and no
new affine representation should follow.

No external review or LLM review loop was run, by explicit instruction.  The
audit is limited to source verification, claim attribution, mathematical
proof, and reproducible artifact checks.
