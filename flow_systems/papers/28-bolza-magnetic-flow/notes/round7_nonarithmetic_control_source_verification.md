# P28 Round-7 source-verified non-arithmetic control

Date: **2026-08-28**

ARS scope: **Stage 1 RESEARCH, Phase-2 source verification / Route A A0--A1**.

## Result

The Round-6 `0/6` fail-closed gate is replaced by one real **`6/6` source
package**:

```text
surface_id=NAZARENKO-EXP-OCTAGON-G2
stable_name=Nazarenko exponential octagon genus-two control
(a,alpha)=(exp(-1/10),pi/4)
curvature=-1
matrix_count=4
source_package_gate=PASS_READY_6_OF_6
nonarithmeticity=PROVED
primitive_side_pairing_owners=4
systole=NOT_CLAIMED
common_geometric_cutoff=NOT_FROZEN
control_census=NOT_RUN
magnetic_comparison=NOT_RUN
```

The stable surface name is project-local and denotes exactly this parameter
specialization.  It is not attributed to the cited authors as a historical
name.

## Search strategy

Search date: **2026-08-28**.

Search surfaces:

- general web index, restricted in follow-up to arXiv, DOI/publisher pages,
  J-STAGE, EPFL Infoscience, Dagstuhl/DROPS, HAL, and the CGAL manual;
- Crossref official work records for every included published DOI; and
- original arXiv source bytes or publisher PDF when available.

Representative exact queries were:

```text
explicit non-arithmetic genus 2 hyperbolic surface Fuchsian group matrices systole
non arithmetic genus two surface explicit matrices octagon side pairing
genus 2 nonarithmetic Fuchsian group explicit generators systole
"Hyperbolic octagons and Teichmüller space in genus 2" pdf
Takeuchi arithmetic Fuchsian group invariant trace field criterion pdf
Lindemann Weierstrass exp nonzero algebraic transcendental authoritative source
```

Inclusion criteria:

1. an exact closed curvature-`-1` genus-two representation or a theorem needed
   to certify it;
2. a primary source, peer-reviewed paper/chapter, or official publisher record;
3. sufficient claim-level detail to bind a displayed formula, theorem, or
   metadata-only corroboration; and
4. a stable locator plus an explicit claim boundary.

Exclusion criteria:

1. arithmetic rather than non-arithmetic surfaces;
2. Teichmüller-curve monodromy or a variable-curvature surface instead of a
   closed Fuchsian genus-two surface group;
3. random-domain software without a frozen instance and non-arithmeticity or
   primitivity certificate;
4. matrices without a checked relation/source locator; or
5. a named surface without an independent arithmeticity test.

The web index does not expose a stable total-hit count, so no pseudo-PRISMA
universe is claimed.  The reproducible screening log retained eight candidate
records: eight title/abstract or official-metadata screens, four original/full
or author-source inspections, four claim-bearing inclusions, and four
exclusions.  Search-engine ranking outside this retained log is a limitation.

## Screening log

| Record | Decision | Reason |
|---|---|---|
| [Nazarenko, arXiv:1301.5446v1](https://arxiv.org/abs/1301.5446v1) | Include | Primary author source; equations (10)--(16) give the admissible octagon, quotient, presentation, and explicit generators. |
| [Aigon-Dupuy et al., DOI 10.1063/1.1850177](https://doi.org/10.1063/1.1850177) | Include with metadata boundary | Peer-reviewed family-level corroboration; exact Round-7 formulas are not inferred from metadata. |
| [Takeuchi, DOI 10.2969/jmsj/02740600](https://doi.org/10.2969/jmsj/02740600) | Include | Primary peer-reviewed arithmeticity criterion; publisher PDF inspected. |
| [Popescu, DOI 10.1007/978-3-031-51959-8_16](https://doi.org/10.1007/978-3-031-51959-8_16) | Include with review-status caveat | Published chapter and [author-source v2](https://arxiv.org/abs/2306.14352v2) supply the inspected Corollary 3.2; chapter peer review was not independently verified. |
| [Macasieb, arXiv:0803.1519](https://arxiv.org/abs/0803.1519) | Exclude | Explicit genus-two groups, but the paper classifies derived **arithmetic** examples and cannot be the requested negative control. |
| [Bouw--Möller, arXiv:0710.5277](https://arxiv.org/abs/0710.5277) | Exclude | Non-arithmetic Fuchsian monodromy for Teichmüller curves; not the required closed genus-two constant-curvature surface package with systole/primitivity. |
| [CGAL hyperbolic-surface manual](https://cgal.geometryfactory.com/CGAL/doc/main/Triangulation_on_hyperbolic_surface_2/index.html) | Exclude from gate; discovery only | Generates random rational-vertex genus-two domains, but supplies no frozen named instance, independent non-arithmeticity certificate, or per-owner primitivity certificate. |
| [Despré--Schlenker--Teillaud, DOI 10.4230/LIPIcs.SoCG.2020.35](https://doi.org/10.4230/LIPIcs.SoCG.2020.35) | Exclude from gate | Rigorous triangulation/flip result, not a six-item source package for one non-arithmetic control. |

## Source quality and claim ownership

The ARS Level-I--VII design labels are not naturally ordered for pure
mathematics.  Each theorem/construction is recorded as Level VI on the
field-neutral design ladder, then graded by fitness for its exact mathematical
claim.

| Source | Venue / verification | Claim owned | Grade | Boundary |
|---|---|---|---|---|
| Nazarenko 2013 | Official arXiv v1 record and TeX source; source-tar SHA-256 `9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b` | Exact two-parameter representation and relation | B | Primary preprint; no non-arithmeticity or systole claim. |
| Aigon-Dupuy et al. 2005 | AIP DOI, Crossref, and [official EPFL metadata](https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d); peer-reviewed | Representation-family corroboration | A for existence/family claim | Metadata/abstract surface only; not used for the exact specialization. |
| Takeuchi 1975 | DOI and [J-STAGE publisher PDF](https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_pdf/-char/en), SHA-256 `6fe5afdf2c02846ee8113ea2cb6f125d6807d2fce07c77feae4d71d6d3b8c048` | Necessary trace-field condition for arithmeticity | A | Does not supply the octagon or transcendence step. |
| Popescu 2024 | Springer/Birkhäuser DOI and author-source v2, source-gzip SHA-256 `f002fe96c0f4e80ce7ed7fd23a69b88536df831883cbb9152904b85c6e62289d` | `exp(alpha)` transcendental for nonzero algebraic `alpha` | B | Published primary proof; chapter review status not independently confirmed. Does not supply the surface, trace algebra, or Takeuchi implication. |

No predatory-venue signal was observed.  No financial conflict declaration was
located for these mathematical sources; the representation authors have the
ordinary intellectual interest of authors in their own construction.  This is
not equivalent to a comprehensive historical conflict or retraction-registry
audit.  No retraction notice was observed in the official records inspected.

## Exact geometry and matrix package

Let

```text
a=exp(-1/10),  x=a^2=exp(-1/5),  alpha=pi/4,
N=-1/sqrt((1-x)(2x-1)),
R=diag(exp(i*pi/4),exp(-i*pi/4)).
```

The source admissibility inequality is strict:

```text
1/sqrt(2) < a < 1,
b=1/(sqrt(2)a) < 1.
```

The exact matrices are

```text
g0=N[[a,x+i(1-x)],[x-i(1-x),a]],
g1=N[[a,(1-x)+i*x],[(1-x)-i*x,a]],
g2=R g0 R^-1,
g3=R g1 R^-1.
```

The 140-decimal replay verifies determinant one and the `SU(1,1)` constraints
for all four matrices.  The source relator

```text
g0 g1^-1 g2 g3^-1 g0^-1 g1 g2^-1 g3=I
```

has maximum entry residual below `1e-138`.  These residuals validate the
transcription.  They do not replace the source's admissible fundamental-octagon
construction as the discreteness/faithfulness theorem.

## Independent non-arithmeticity certificate

All four generators have the same squared trace, and the exact specialization
gives

```text
t^2=tr(g0)^2=4x/((1-x)(2x-1)),  x=exp(-1/5).
```

By Popescu Corollary 3.2, `x` is transcendental.  If `t^2` were algebraic,
then `x` would satisfy

```text
-2 t^2 x^2+(3 t^2-4)x-t^2=0
```

over the algebraic numbers, a contradiction.  Thus `t^2` and
`tr(g0^2)=t^2-2` are transcendental.  The displayed polynomial is genuinely
nonzero for every algebraic `t^2`: if `t^2` is nonzero, its constant
coefficient is nonzero, while for `t^2=0` it reduces to `-4x`.

Let `Gamma^(2)=<gamma^2:gamma in Gamma>`.  Since the surface group `Gamma` is
finitely generated, `Gamma/Gamma^(2)` is a finitely generated elementary
abelian `2`-group and hence finite.  Thus `Gamma^(2)` is a finite-index
cofinite subgroup.  Arithmeticity of Fuchsian groups is invariant under
commensurability, so if `Gamma` were arithmetic then `Gamma^(2)` would be
arithmetic as well.  After Cayley-conjugating the displayed `SU(1,1)` model
to `SL_2(R)`, Takeuchi Theorem 1 applies to `Gamma^(2)` and requires its trace
field to be an algebraic number field.  But `tr(g0^2)` is a transcendental
element of that field.  Therefore this source-locked surface group is
non-arithmetic.

This is an exact obstruction, not a genericity argument and not a floating-point
classification.

## Four rigorous primitive owners

The single surface relator has exponent sum zero in each generator, so the
abelianization is `Z^4` with `[g_j]=e_j`.  If `g_j=h^n` for `n>=2`, then
`e_j=n[h]`, impossible because `e_j` is primitive in `Z^4`.  Hence
each generator is primitive.  Moreover, if `g_i` were conjugate to `g_j` or
`g_j^-1`, abelianization would give `e_i=e_j` or `e_i=-e_j`; for `i!=j` both
are impossible.  Therefore `g0,g1,g2,g3` define four pairwise distinct
inverse-paired primitive side-pairing owners.

This is deliberately not called a systole theorem.  It gives no primitivity
credit to any other word and no short-spectrum completeness.

## Gate matrix

| Requirement | Verdict | Evidence |
|---|---|---|
| Named closed curvature-`-1` genus-two surface | PASS | Exact stable name and admissible Nazarenko specialization. |
| Explicit torsion-free cocompact Fuchsian matrices | PASS | Source fundamental-octagon theorem plus exact analytic matrices and independent replay. |
| Presentation / checked relation | PASS | Source equation (12), residual `<1e-138`. |
| Primary or peer-reviewed locator | PASS | arXiv primary source plus peer-reviewed AIP family paper. |
| Independent non-arithmeticity | PASS | Popescu transcendence theorem + exact trace algebra + Takeuchi criterion. |
| Systole or per-owner primitivity | PASS | Four generator classes primitive in `Z^4`; no systole claimed. |

```text
SOURCE_PACKAGE_GATE=PASS_READY_6_OF_6
```

## Paper-facing advance and limitations

Round 7 removes a concrete Stage-1 blocker: Paper 28 now has a named,
source-locked, exactly non-arithmetic, topology/curvature/area-compatible
genus-two control with four primitive owners.  This is a usable Methods and
Controls theorem package rather than a design placeholder.

It does **not** yet answer whether Bolza phase cancellation is
arithmetic-specific.  A fair comparison still lacks a rigorous control
systole/lower bound or another finite word-to-length completeness certificate
that can support one target-blind geometric cutoff `Lambda`.  Until that object
exists, no common-cutoff census, branch outcome, control margin, A0 promotion,
A2 experiment, or Route-B entry is authorized.

## Reproducibility

Run:

```bash
./experiments/reproduce_round7.sh
```

Results:

```text
UNIT_TESTS=22/22
ISOLATED_BUILDS=2
BYTE_IDENTICAL=true
ARTIFACT_TREE_SHA256=a11917f6e9eab3bc48f1920b9727b0ec96a9c43c1f7ac13ab69984c005cfccef
```

The canonical artifacts are the source matrix, exact/decimal matrix package,
six-item gate, validation record, and reproducibility receipt.  The default
command verifies them with `cmp`; `--refresh` is maintainer-only.
