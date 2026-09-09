# E4 nonauthor review: finite equivariant covers and bounded transfer graphs

2026-09-09 UTC. Independent **current-team internal** mathematical/source
review, not human peer review. This reviewer did not author either lane.
Scope: A2's three auxiliary claims and D1-FC's finite-cover classification,
its finite-stage/tower boundary, and its explicit sharpness examples.

## Outcome and disposition

**The reviewed mathematical interfaces survive. One genuine D1 finite-field
hypothesis omission was found, corrected by the author, and independently
read back; no mathematical must-fix remains open.** A2 has not proved
PC424-L: the missing uniform total-degree bound/global compatibility identity
remains missing. D1 has answered its finite normal equivariant-cover question,
but its principal mechanism is source-owned and the extensions are short
classical consequences. Neither lane establishes an independent-paper
increment or a target-arithmetic spectral bridge.

The exact surviving outputs are:

| Interface | Allowed claim | Non-claim |
| --- | --- | --- |
| A2 connected finite étale cover | Over an algebraically closed field of odd characteristic, a connected nonempty finite étale cover of the full affine line admitting a morphism over `x²+c` has degree one. | There are no nontrivial étale covers of the affine line; orbit sums automatically construct a transfer. |
| A2 Artin–Schreier certificate | `Δb=h^p−h`, with rational `b`, exists exactly when `h=ΔQ+β`, with polynomial `Q` and `β∈F_p`. A fixed-point sum kills `β`. | Split fibers over geometric periodic points imply this global identity; a split algebra with a lift has a one-step stable field component. |
| A2 finite-graph extraction | A degree-`D` total-degree equation containing more than `2^D d_T D^4` compatible graph points forces `h=ΔQ+β`, now with `β∈k`. | A bound only on degree in `Y` suffices; ordinary sums have supplied a uniform total-degree bound. |
| D1-FC | All specified finite normal equivariant covers over a number field are `A²_K×Spec A`, with lift `H^m×τ` and finite étale `K`-algebra `A`; in particular they cannot be ramified. | This excludes nonfinite constructions, covers lacking the stipulated equivariance/normality, arbitrary characteristic-`p` covers, or all arithmetic labels. |
| D1 finite-stage tower | Cofinal finite dynamically invariant levels, including levels invariant under a positive iterate, are geometrically constant. | Every infinite algebraic extension with a lift has such finite invariant levels. |
| D1 infinite witness | A marked orbit-divisor multiquadratic extension escapes the finite-stage hypothesis and has an exact periodic fixed-fiber quadratic-character line. | A global trace-class operator, limiting determinant, canonical unmarked divisor, target Euler factors, or prime-owner correspondence has been constructed. |

## Artifacts and actual read scope

- [A2 supplement](../../lanes/a2_transfer_bridge/PROOF_SUPPLEMENT.md): complete
  proof, including the subsequently added complexity-growth contrapositive.
  Main locators: assumptions/claims, Section 1, Sections 2.1–2.3, and
  Sections 3–4. [A2 report](../../lanes/a2_transfer_bridge/REPORT.md): complete.
- [D1 supplement](../../lanes/d1_arithmetic_spectral/FINITE_COVER_PROOF.md):
  complete, including the corrected `F_q` passage in Section 7 and the
  explicit negative Frobenius exponent for the sheet equalizer in Section 5.
  [D1 report](../../lanes/d1_arithmetic_spectral/REPORT.md): frozen question
  and completed output/source-disposition sections read.
- Imported [R6 algebraic descent](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md):
  exact theorem and complete Sections 1–7 read, with its wild-degree boundary
  also inspected. R6 remains an imported proved result, not a new A2 claim.
- Targeted old-source checks included the R5 split-algebra example, the R6
  arithmetic source audit's Cantat–Dujardin entry, and the C374
  [Kummer–Frobenius theorem package](../../../henon_kummer_arboreal_frobenius_route_a/THEOREM_PACKAGE.md).
  Registry searches were discovery pointers, not an exhaustive reread of
  unrelated packages or a re-verification of their numerical certificates.

## Must-fixes and closure record

### M1 — D1 Frobenius coefficient field: CLOSED

**Locator:** D1 supplement Section 7, originally the paragraph beginning
“Work in odd characteristic at a reduction”, followed by `P∈F_p²` and
`χ_p(f_j(P))`; D1 report, output 4.

For an arbitrary number field, the reduced coefficients of `H` and marked
`f` need not lie in `F_p`. An `F_p`-rational starting point alone does not
make its entire native orbit `F_p`-rational. The original formulation could
therefore apply `χ_p` to elements outside its domain and assert commutation
with a Frobenius that did not fix the dynamical coefficients.

The author now chooses an odd finite field `F_q` containing **all** reduced
coefficients of `H,f`, takes `P∈F_q²`, and uses `q`-power Frobenius and
`χ_q`. Independent readback confirms the same change in the report. The
orbit values then lie in `F_q`, and Frobenius preserves the quadratic
relations and commutes with the shift. The explicit example over `F_7`
is unchanged and correct. This was a real hypothesis repair, not an
objection to FC or the infinite-extension construction.

### Required claim boundaries — already satisfied

1. A2 must retain **OPEN / NOT CURRENTLY JUSTIFIED** for the implication
   from all ordinary orbit sums to a polynomial/algebraic transfer. Its
   Section 4 currently does so explicitly.
2. D1 must retain the cofinal **finite invariant stage** requirement in its
   tower conclusion. Theorem FC and Sections 4/7 currently retain it.
3. The normal-source extension and permutation formulas cannot be advertised
   as an unowned new finite-semiconjugacy mechanism: the Cantat–Dujardin
   collision is explicit in both D1 artifacts.
4. The Kummer witness depends on a declared marked coordinate/divisor and
   a finite field of definition; it is not intrinsic to an unmarked
   conjugacy class or independent of arithmetic base extension.

Minor notation: A2's newly added Section 4 contrapositive used `K_c` without
defining it locally. The author was asked to spell out the all-ordinary-
orbit-sum kernel there. Its mathematical content is already correct;
this is a self-containment clarification, not an additional theorem gap.

## A2 proof audit

### A2.1 Finite étale obstruction

All operative hypotheses are present: `k` algebraically closed, `p` odd,
the cover nonempty/connected/finite/étale over the **whole** `A¹`, and an
actual morphism `g:Y→Y` satisfying `πg=fπ`. No Galois assumption is needed.
Connected smooth `Y` is integral; compactification gives a smooth projective
curve `C` and extensions of both maps. The normal finite model identifies
`Y` with the complement of the full fiber over infinity, not an arbitrary
punctured model. The relevant extension principle is standard and was
checked in [Stacks 53.2](https://stacks.math.columbia.edu/tag/0BXX).

Degree multiplicativity gives `deg ḡ=2`; odd characteristic makes this
map separable. The `m=deg π` distinct points over the critical point `0`
each contribute at least one to its different. Total invariance of the
`b≥1` points at infinity gives a further contribution at least `b`, since
the sum of their ramification indices is `2b`. Thus

`2−2g(C) = deg Diff(ḡ) ≥ m+b ≥ 2`.

This forces `g(C)=0`, `m=b=1`. The different formulation correctly handles
ramification rather than assuming a tame formula for `π`. The required
inequality and separable genus formula were checked against
[Stacks 53.12](https://stacks.math.columbia.edu/tag/0C1B).

The theorem does not make `A¹` étale simply connected in characteristic
`p`; it obstructs an additional tame-quadratic equivariance condition.
It cannot be transported to D1's characteristic-`p` plane example by
ignoring either dimension or the wild base degree.

### A2.2 Artin–Schreier certificate and disconnected algebra

The quotient is correctly an `F_p`-vector space, not a `k`-vector space.
Removing constants and reducing exponents divisible by `p` yields a
unique finite sum of positive prime-to-`p` exponents. Pullback by `x²+c`
doubles its leading exponent, still prime to `p`; lower-term reductions
cannot cancel that term. Hence no nonzero class is periodic under pullback.
The cohomological identification uses precisely the
[Artin–Schreier sequence and affine vanishing](https://stacks.math.columbia.edu/tag/0A3J).

R6's finite-pole lemma first makes rational `b` polynomial. Invariance of
its AS class then yields `b=Q^p−Q`; the exact identity gives
`(h−ΔQ)^p−(h−ΔQ)=0`, hence `β∈F_p`. Conversely `b=Q^p−Q` constructs
the certificate. Since `f−x` has a root in `k`, just one valid fixed-point
condition removes `β`, including when the fixed-point scheme is nonreduced.

The split cover `y^p−y=0` with `h=1` has a component permutation but no
one-step stable component giving an algebraic transfer. This is a genuine
algebra-versus-field warning and **not** a PC424-L counterexample, because
the fixed-point orbit sum is nonzero. Likewise every cover splits over a
finite set of algebraically closed geometric points; this cannot detect
the global dynamical compatibility identity.

### A2.3 Heavy components, constants, and return to the native tick

The Bézout bookkeeping is valid with the displayed, nonoptimal constant:

- There are at most `D` reduced irreducible components; some contains at
  least `N/D` graph points.
- If a component has `M>d_T D³` graph points, at least one target component
  receives more than `d_T D²` **input** points. Counting input points here
  avoids an erroneous additional factor of two.
- `P_j∘T` is nonzero by dominance and has degree at most `d_T D`.
  If it does not contain the input component, the distinct affine
  intersection count is at most `d_T D²`. This is the applicable
  consequence of [Milne, Theorem 6.37](https://www.jmilne.org/math/CourseNotes/AG.pdf).
- Image-count propagation then loses at most a factor of two, since every
  geometric fiber of `T` has at most two points. After `D` propagations,
  `N/(D2^D)>d_T D³` still holds. Repetition among `D+1` components produces
  a dominant `T^r` self-map, `1≤r≤D`.
- A heavy component is not vertical: a vertical line contains at most
  one point of a graph. Its function field is finite over `k(x)` and
  carries the actual injective pullback, including possible inseparability.

R6 applies with polynomial base `f^r`, degree `2^r` prime to `p`, and
right side `S_rh`, yielding `y=Q(x)` and `Q∘f^r−Q=S_rh`.
Commuting the two difference operators makes `h−ΔQ` invariant under
`f^r`; degree growth makes it constant. There is no division by `r`, so
the argument remains valid when `p` divides the extracted return period.
Here the constant is only asserted to be in `k`, correctly distinct from
the `F_p` constant in the AS certificate. The all-orbit hypothesis, via
a fixed point, removes it and restores the **one-step** equation.

The threshold implication is proved. Its application to PC424-L is
conditional on a uniform bound on **total algebraic degree** for some
finite transfer graphs of arbitrarily large size. Choosing different
graphs/equations at different field sizes is allowed; compatibility among
those choices is unnecessary. Ordinary interpolation supplies `deg_Y=1`
but can have unbounded `deg_X`, so it does not close the gap. The added
contrapositive `q^n≤2^D d_T D^4` for any hypothetical non-coboundary defect
is the same valid threshold read backward, not a contradiction or a
constructed defect.

## D1 proof audit

### D1.1 No periodic affine curves: all factors, iterates, and conjugates

The phase-marked normalization argument handles all quantified compositions.
For a finite invariant union of curves, record all `sm` factor phases,
normalize each irreducible component, and complete it. The factor
isomorphisms extend to isomorphisms of complete normal curves and biject
their finite boundary sets. At a boundary point at least one coordinate
has a pole; otherwise properness of the finite normalization would place
it in the affine normalization.

Because the first output coordinate is the preceding `y`, the multisets
of all phase-marked `x` and `y` pole orders coincide. Their common maximum
`M` is positive. At a point realizing the maximum for `y`, the next
polynomial term has pole order `d_i M>M`, while `a_i x` has pole order at
most `M`. Cancellation is impossible, contradicting maximality. Component
permutations and repeated curves cause no problem because phase copies
are retained. A polynomial conjugacy transports the entire assertion.

This proof actually works in any algebraically closed characteristic. It
reconstructs a known result, not a new all-composition theorem. The accessible
[Dujardin–Favre preprint](https://arxiv.org/pdf/1405.1377), Proposition 1.7
in the served version, explicitly credits Bedford–Smillie Proposition 4.2
and notes its any-field proof. D1's published Proposition 1.9 locator must
not be substituted for the preprint's numbering.

### D1.2 Finite branch purity and arithmetic descent

The cover is a finite **morphism**, with normal finite-type source and all
nonempty components dominating the regular plane. Each component is
surjective because its finite image is closed and dense. Characteristic
zero supplies generic separability; a Galois or smooth-source assumption
is unnecessary. Normal source components are disjoint, so they can be
treated separately. The lift is a `K`-automorphism, not just pointwise
maps between unrelated fibers.

The non-étale locus is closed; its finite image `B` is a proper closed
branch support. Equivariance by **two isomorphisms** gives equality
`H^m(B)=B`, not merely a one-way inclusion. Its geometric divisorial
components are excluded by the preceding no-curve argument. Source and
target codimensions agree for the finite dominant surfaces. Normal source,
regular target, quasi-finiteness, equality of local dimensions, and
codimension-one unramifiedness match
[Stacks purity, Lemma 58.21.4](https://stacks.math.columbia.edu/tag/0BMB).
Thus isolated branching cannot survive; it is not dismissed without purity.

The now finite étale cover is geometrically split in characteristic zero.
This standard affine-space assertion is explicitly recorded in
[Chernousov–Gille–Reichstein, Section 8](https://www.math.uni-bielefeld.de/lag/man/274.pdf);
the arithmetic descent is also consistent with the
[geometric/arithmetic fundamental-group exact sequence](https://stacks.math.columbia.edu/tag/0BTX).
The sheet Galois set descends to a finite étale `K`-scheme. A lift above
`H^m` has a constant permutation of the connected geometric sheets;
`K`-definition says precisely that it commutes with the Galois action.
This gives `τ`, and the identical argument handles transition morphisms.
Geometric connectedness, not mere connectedness over `K`, forces degree one.

The finite-field-extension variant is legitimate: normalization of
`K[x,y]` in a finite extension is finite, and applying both `σ` and its
inverse to integral equations preserves that normalization. It is not an
unresolved birational-versus-regular lift issue. Even if “field lift” is
read as an injective embedding over the base automorphism, finite degree
forces surjectivity: `[L:σ(L)]=1`. No such automatic surjectivity argument
is available for A2's degree-two base embedding, where R6 deliberately
uses injective embeddings instead.

### D1.3 Native holonomy and finite-stage towers

For `m=1`, the return over every geometric primitive length-`n` orbit is
`τ^n`, independent of its location. A sheet cycle of length `r` yields
`gcd(n,r)` lifted cycles of length `lcm(n,r)`. The fixed-point formula
`F̃_n=F_n Σ_{r|n} r b_r` and formal zeta product
`ζ_G(z)=Π_r ζ_{H^r}(z^r)^{b_r}` follow exactly. Counts are reduced geometric
points, not scheme lengths. The no-curve theorem makes every fixed locus
finite, so no hidden positive-dimensional count appears.

For an `m`-tick lift, a primitive length-`n` orbit splits into `gcd(n,m)`
block cycles, with holonomy `τ^{n/gcd(n,m)}`. This does not create a one-tick
lift. The product Koopman formula is correctly conditional on a chosen
invariant measure/space; it does not assert an arbitrary trace exists.
The mixed equalizer uses `τ^n=φ_v^r`, so its sheet permutation trace is
`Tr(U_τ^n U_{φ_v}^{−r})`, as now explicitly stated.

Every genuinely equivariant finite level is constant, and full faithfulness
makes every transition constant. This remains valid if individual finite
field levels are stable under possibly different positive iterates.
It says nothing about an infinite extension whose nontrivial finite levels
are **all moved out of themselves** by every positive iterate.

### D1.4 Sharpness: characteristic p and an infinite orbit-divisor tower

The characteristic-`p` control is exact. For
`π(u,v)=(u^p−u,v^p−v)` and `H(u,v)=(v,v^p−u)`, monic AS equations give
degree `p²`, the derivative of `π` is `−I`, and the source is the connected
smooth normal affine plane. Directly,

`πH=Hπ=(v^p−v, v^(p²)−v^p−u^p+u)`.

The deck action `(a,b)↦(b,b−a)` is also correct, including `p=2`.
This falsifies the characteristic-zero **constancy** conclusion in positive
characteristic. It does not falsify the no-periodic-curve input or A2's
odd-characteristic tame-quadratic one-variable obstruction.

For the infinite example, the prime divisors of `f_j=f∘H^j`, `j∈Z`,
are distinct and irreducible; otherwise one would be periodic. Their odd
valuations prove square-class independence. Finite subsets give degrees
`2^|J|`; their union has geometric Galois group `Π_Z C_2`. The declared
shift on independent root generators defines an invertible lift.

A nontrivial finite intermediate extension of this abelian exponent-two
extension corresponds to a nonzero finite-dimensional subspace of the
finite-support character module. Stability under any shift power would
keep all translates of a nonzero finite-support vector in one fixed finite
support union, impossible by its translating extreme index. Thus **no**
nontrivial finite invariant geometric stage exists. Calling this merely
a tower of finite covers while suppressing equivariance would change FC's
hypothesis.

After the M1 correction, at an `F_q`-rational native orbit of length `n`
avoiding the marked divisor, the shift-`n` fixed fiber consists of exactly
`2^n` periodic root sequences. The product-of-signs line is independent of
reference roots as a line; Frobenius acts by

`ε(c)=χ_q(Π_{j=0}^{n−1} f(H^jP))`.

Cyclic re-rooting leaves this product unchanged. For
`H=(y,y²+3−3x)` over `F_7`, `(1,1)` and `(3,3)` are fixed points and
give `χ_7(1)=+1`, `χ_7(3)=−1`; all claimed avoidances hold. This is a real
same-native-length arithmetic distinction in the **infinite marked**
construction. It is not claimed for every parameter or every pair of orbits.
Its character can change on extending the finite coefficient field; fixing
the Frobenius field is part of the observable.

## Closest-source collision and retained research increment

The most important public collision is
[Cantat–Dujardin (2024), Section 3(a), Theorem B](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164).
The publisher's full displayed theorem/proof was independently read. For
proper holomorphic semiconjugacies between loxodromic plane automorphisms,
it proves polynomiality and then excludes the invariant Jacobian-zero
curve before concluding that the covering is an automorphism. In D1,
polynomial/finite algebraicity is already assumed; the remaining geometric
engine is the same. Arbitrary normal source surfaces require purity, and
arithmetic constant descent adds a useful formulation, but these do not
establish a substantial independent new mechanism.

For A2, compactification/Riemann–Hurwitz, AS reduction, and Bézout are
classical. The substantial finite-extension descent is already R6-owned.
The explicit heavy-component threshold is a valid new interface in this
batch; it still only reduces the unchanged open question to the unproved
uniform-complexity input. It is not a second paper beside A1.

C374's old all-level radical–cyclotomic/Frobenius representation concerns
a different tower with existing ownership. D1's orbit-divisor shift is
not that arithmetic number-field classification, nor do old finite
permutation determinants supply the absent global trace for it. Conversely
the fresh witness is ordinary multiquadratic theory plus a multiplicative
quadratic cocycle; this review found no basis to promote it to a new
global arithmetic-spectral theorem.

## Source-access and execution limitations

Primary bodies actually used: Stacks 53.2 curve extension/category theorem;
Stacks 53.12 genus/different formula; Stacks 59.63 AS exact sequence and
affine vanishing; Milne Section 6n/Theorem 6.37 and surrounding proof;
Stacks 58.21.4 purity hypotheses; Stacks 58.14.3 exact sequence;
Chernousov–Gille–Reichstein Section 8 opening; Cantat–Dujardin Theorem B
and full displayed proof; Dujardin–Favre preprint no-curve statement and
Bedford–Smillie attribution. Relevant PDF material was browser-extracted;
no local PDF page anchor or visual PDF audit is claimed.

The Dujardin–Favre publisher PDF request/find did not return usable text
in this review; the accessible arXiv version was used with its own
Proposition 1.7 numbering. The original Bedford–Smillie proof body was not
newly read. Its ownership is corroborated by the two author/publication
sources, while D1's supplied elementary proof was checked directly.
Bounded search non-hits do not certify global novelty or absence of a
stronger theorem.

Only this review file was written by E4. Mathematical program executions,
old-program reruns, builds, Git writes, shared-index/evaluator edits,
external-model calls/uploads, and extra agents: **0**. The repository
workflow and research-review checklist enforced proof/source subtraction,
actual-author repair/readback, and exact allowed claims. The ARS router
was inspected but no ARS pipeline or external-review workflow was run,
consistent with the bounded batch instruction.

**Recommendation to coordinator:** retain A2's three auxiliary interfaces
with PC424-L explicitly open; retain D1-FC and the sharpness witnesses as
`AUXILIARY_INTERFACE_ONLY`. No independent paper admission is recommended
from these formulations after source subtraction. No target Euler factor,
root number, automorphy, target divisor, or Hilbert–Pólya claim is supported.
