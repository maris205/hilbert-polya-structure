# Nonlinear geometry first-pass report and primary-source audit

2026-09-08 UTC. Scope: the three questions in [FROZEN_SCOUTS.md](FROZEN_SCOUTS.md).
Coordinator-authored analytic/source screening, not independent review.
**Zero admissions, zero manuscripts, zero new mathematical programs.**

## Dispositions

| Question | First-pass disposition | Exact reason |
| --- | --- | --- |
| NL424-1 | REJECT_AS_CURRENT_PAPER_PROPOSAL | Closest sources already supply the hard global/ray classification. No substantial new residual theorem has been established after their subtraction. This is not a proof that every explicit integer atlas has already been printed. |
| NL424-2 | NOT_CURRENTLY_JUSTIFIED | All-dimensional, all-parameter exhaustion is unproved; unbounded zero channels defeat a naive uniform height box. C421 covers only `n=3`. |
| NL424-3 | NOT_CURRENTLY_JUSTIFIED | The transfer and integrability are classical. A complete rational classification on the stated two-sided domain, including singular fibres, is missing. |

No disposition is a universal impossibility theorem or a claim that the
full frozen question was solved. None fills one of the five paper slots.

## Analytic feasibility checks

### 1. Global order and individual periodic points are not interchangeable

The two-slope map is an invertible integer map; its inverse is
`(x,y)->(y,f_(a,b)(y)-x)`. It is positively homogeneous, not generally odd.
Thus rational periodic rays and radial multipliers must be distinguished
from actual point returns.

The checked sources below already contain the finite-order/ray mechanism.
One must still distinguish nonglobal neutral cases: for example at `a=2`
every `(t,t)` with positive integer `t` is fixed regardless of `b`. This
follows by substitution, not from claiming global finite order. Conversely,
simply listing the familiar finite orders does not answer the frozen atlas.
No new full atlas proof or sufficient residual increment was obtained.

### 2. A precise obstruction to the proposed finite-box shortcut

The polynomial invariant follows by treating `K` as a quadratic in `x_1`:
its two roots sum to `product_(j=2)^n x_j+a`. Applying that root interchange
and then cyclically permuting coordinates preserves `K`. The inverse is
`(y_1,...,y_n)->(product_(j=1)^(n-1)y_j+a-y_n,y_1,...,y_(n-1))`.

At `a=0`, let the starting point have at least two zero coordinates.
At every step the product of the `n-1` coordinates other than the first
is zero: if the first is zero, at least one other zero remains; if it is
nonzero, both zeros remain. Hence the map on this locus is exactly the
signed rotation

`J(x_1,...,x_n)=(x_2,...,x_n,-x_1)`.

It preserves the number of zero coordinates, so the argument iterates.
Since `J^n=-I` and `J^(2n)=I`, the entire unbounded locus is periodic with
least periods dividing `2n`. For `n=4`, `(0,u,0,v)` has the scalar word
`(0,u,0,v,0,-u,0,-v)`; if `(u,v)!=(0,0)`, comparison with periods 1,2,4
shows that its least period is exactly 8. Its unrestricted heights are
arbitrarily large. This exact elementary check refutes a global fixed-box
claim, but neither solves the complement nor is claimed as a new paper:
Hu–Tan–Zhang explicitly identify the unforced dihedral locus.

The local `n=3` proof uses the special parameter-free second-order equation
`d_(i+1)+d_(i-1)=(x_(i+1)+1)d_i`, with `d_i=x_(i+2)-x_i`.
Its reduction to a finite extremal core cannot be asserted for all `n`
without a new argument. Neither an all-dimensional exceptional-channel
classification nor an exhaustive finite residual core was established here.

### 3. Adler regularity and source clock checks

Each `R_(b,c)` preserves `u+v` directly. Its inverse is
`(U,V)->(V-(b-c)/(U+V),U+(b-c)/(U+V))`, with the same cancellation
convention for equal parameters. Consequently the three-site transfer has
a well-defined inverse on its declared two-sided regular domain and
preserves `x_1+x_2+x_3`.

The first freeze named fibrewise classification but wrote only the sum
invariant. Nonauthor review correctly required a full invariant map before
any elliptic-fibre argument: sum fibres alone are affine planes. The contract
now specifies `I_beta=(S,H_beta)` with the polynomial `H_beta` written there.
Here is a direct invariance check, not an assertion of a new integrability
theorem. For a two-site operation write `s=u+v`, `d=b-c` and let `w,e`
be the third coordinate and parameter. Then

`H=s(uv+ws+w²)+b*v+c*u+(b+c)*w+e*s`.

For `s!=0`, the updated product differs by
`u'v'-uv=d(v-u)/s-d²/s²`, whereas
`b(v'-v)+c(u'-u)=d(u-v)+d²/s`. Their contributions cancel after multiplying
the product difference by `s`. If `b=c`, the operation is a regular swap
and the same invariant is symmetric in those coordinates, including `s=0`.
Thus each two-site operation, and hence the native transfer, preserves
both specified polynomial invariants for every parameter triple. No level
is removed or presumed smooth. This clarification fixes the fibre object;
it does not supply the missing rational periodic-point atlas.

When all parameters agree, the two maps are swaps and the native transfer
is the coordinate 3-cycle `(x_1,x_2,x_3)->(x_3,x_1,x_2)`. Its equal-coordinate
points are fixed; all others have least period 3. This degenerate subfamily
is immediate and is not the general rational classification.

The checked Kassotakis reduction distinguishes the ordinary transfer from
an extended transfer whose power gives it. Changing to that root map would
change least periods. Smooth-fibre elliptic torsion alone also omits the
singular and excluded-pole analysis. No such omission is accepted as an
all-parameter theorem; no numerical rational-height atlas was run.

## Primary-source verification, exact access scope

All remote accesses below used ordinary browsing on 2026-09-08 UTC.
Primary full-text access means the cited sections were actually inspected,
not that every page of the paper was read. No downloaded local-PDF page
anchor is used in this lane, so no local structural preflight is asserted.
The ARS source-verification role was used only for this bounded fact check;
the analytic conclusions above are separately identified coordinator work.

1. **Cairns, Nikolayevsky and Rossiter, _Piecewise Linear Periodic Maps
   of the Plane with Integer Coefficients_**, [arXiv 1407.3364v1](https://arxiv.org/pdf/1407.3364v1).
   Actual access: 13-page full text, introduction, explicit examples and
   Section 4/Theorem 1 and its proof (PDF pages 1–7), not all later tree
   constructions. The theorem bounds the global orders of continuous
   half-plane integer-linear periodic maps by `1,2,3,4,5,6,7,8,9,12`.
   The broader theorem is not an individual-point classification of every
   nonglobally periodic two-slope map. Used as a source-ownership collision.

2. **Lagarias and Rains, _Dynamics of a Family of Piecewise-Linear
   Area-Preserving Plane Maps I. Rational Rotation Numbers_**,
   [arXiv math/0301294v4](https://arxiv.org/pdf/math/0301294v4).
   Actual access: 20-page full text; definitions/introduction, Theorems
   2.1–2.4, and selected Section 4 proofs of 2.3 and 2.4. They characterize
   finite order through the orbit of `(0,1)` and classify the rational
   ray-rotation alternatives. Their introduction explicitly credits the
   overlap with Beardon–Bullett–Rippon. Native point returns are distinguished
   from periodic ray directions. No claim that the entire paper was read.

3. **Beardon, Bullett and Rippon, _Periodic orbits of difference equations_**,
   [publisher DOI](https://doi.org/10.1017/S0308210500030286).
   Actual access: publisher metadata/abstract and the explicit attribution
   in Lagarias–Rains, not its full proof. Publication year is 1995; later
   electronic availability is not treated as the research date. It supplies
   a closest-source pointer, not an unseen theorem silently imported here.

4. **Hu, Tan and Zhang, _Polynomial automorphisms of C^n preserving the
   Markoff–Hurwitz polynomial_**,
   [arXiv 1501.06955v2](https://arxiv.org/pdf/1501.06955v2),
   [publisher](https://link.springer.com/article/10.1007/s10711-017-0235-z).
   Actual access: the 36-page v2 PDF (6 May 2015), introduction through the
   initial group questions, Section 2.6 dihedral maps and nearby fork
   estimates; metadata checked against the primary publisher, online
   29 March 2017, volume 192 (2018), pages 207–243. These are unforced
   Markoff–Hurwitz group/geometric results, not an all-forced-parameter
   classification of the single cyclic map. No full Appendix proof or full
   discontinuity-domain theorem is claimed read or imported.

5. **Gamburd, Magee and Ronan, _An asymptotic formula for integer points
   on Markoff–Hurwitz varieties_**,
   [Annals 190 (2019), 751–809](https://annals.math.princeton.edu/2019/190-3/p02).
   Actual access: primary metadata and abstract. The linked official PDF
   request failed (timeout/access error); it is not marked full-text read.
   Its integer-point counting object does not itself answer this scout's
   native cyclic periodicity question. No unseen estimate is used.

6. **Veselov, _Yang–Baxter maps and integrable dynamics_**,
   [arXiv math/0205335v2](https://arxiv.org/pdf/math/0205335v2),
   [publisher DOI](https://doi.org/10.1016/S0375-9601(03)00915-0).
   Actual access: 11-page preprint; introduction, transfer definitions and
   theorem, factorization/isospectral discussion, and Adler formula (11),
   especially PDF pages 4–7. The map/sign convention and transfer order were
   read directly. The generic Jacobian linearization is source-owned; it is
   not an all-rational-points atlas. The 2002 preprint and 2003 publication
   dates are not replaced by the PDF rendering date.

7. **Kassotakis, _Invariants in Separated Variables: Yang–Baxter,
   Entwining and Transfer Maps_**,
   [SIGMA 15 (2019), 048](https://sigma-journal.com/2019/048/),
   [official PDF](https://sigma-journal.com/2019/048/sigma19-048.pdf),
   [arXiv 1901.01609v2](https://arxiv.org/abs/1901.01609v2).
   Actual access: 36-page full text; introduction and selected Sections 5.1
   and 5.2, Proposition 5.3, Corollary 5.7 and the three-site `H_V` example.
   These relate native and extended transfers and a discrete-Painlevé
   reduction. They must not be conflated with the local C422 `H_III^B`
   q-Painlevé contract. No complete rational periodic-point theorem was
   inferred from these reductions, and no full-paper-read claim is made.

8. **Adler, _Recuttings of polygons_**,
   [primary publisher](https://link.springer.com/article/10.1007/BF01085984).
   Actual access: Springer/MathNet metadata, not full 1993 text. Russian
   pages 79–82 and translated pages 141–143 refer to distinct editions.
   Retained as a historical origin pointer, not a proof dependency.

Prescreen-only sources included Weinreich's pentagram work (2104.06211;
generic integrability and characteristic restrictions inspected) and search
hits on Somos-4/Hirota–Kimura systems. Those envelopes collided with local
AR2/HK7/PG7 and were abandoned, so these are not supporting references for
any theorem above. A Gamburd ICM survey was also a lead, not a proof input.

## Reproducible search record

Queries were issued in the following successive groups; all on 2026-09-08.
These are actual search strings, not a claim to exhaustive worldwide search.
Subsequent direct opens/finds targeted the primary URLs and sections above.

```text
finite field pentagram map periodic orbits spectral curve singular fibres
Somos 4 periodic integer sequences classification parameters
Hirota Kimura Euler top rational periodic points classification

Lagarias Rains piecewise linear area preserving plane maps integer parameters periodic points finite order
Markoff Hurwitz cyclic recurrence integer periodic points x n product previous generalized trace map
Adler dressing chain rational periodic transfer maps complete classification

"Markoff Hurwitz" "periodic points" Coxeter
"Markoff" "linear terms" "Hurwitz" dynamics
"Adler map" "transfer maps" "periodic" rational

"piecewise linear" "integer" "periodic points" "Lagarias"
"periodic orbits" "Beardon" "Rippon" 1995 plane maps
"Adler map" "rational periodic"
"Markoff-Hurwitz" "cyclic" "periodic"

"Polynomial automorphisms" "Markoff-Hurwitz"
"Dynamics on Markoff-Hurwitz varieties"
"Adler" "Recuttings of polygons" 1993
"Adler map" "periodic points" elliptic
```

Local routing used `rg` for `pentagram|dressing chain|Somos|Hirota|McMillan|
cluster|Veselov|Adler|tropical|Yang.Baxter`, then more focused
`Lagarias|Rains|Brown|Markoff.Hurwitz` in the Hénon registries and relevant
C419–C423 scouts. Search output was a locator, not a claim of full-register
reading. Actual local reads included the old nonlinear scout's first 180
lines, `IR1_CLASSIFICATION.md` through its complete classification and count
rules, and the first 160 lines of `IR1_PROOF.md` for the changed-dimension
risk. No old core program, PDF build or numerical result was rerun.

## Next boundary

Do not write manuscripts for these three proposals. NL424-2 would need a
new all-dimensional exhaustion argument; NL424-3 would need a complete
native-domain fibre/torsion/singularity classification. NL424-1 needs a
demonstrably substantial residual question before revival. An independent
reader may dispute a screening judgment, but no supportive judgment can
replace the missing proof. Target arithmetic remains unestablished.
