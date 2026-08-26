# Paper 19 Phase-2 source and routine-reduction screen

Date: **2026-08-24**

Status: **MERGE INTO PAPER 12**

This is a bounded Phase-2 source and feasibility audit.  It is not a proof
lock, manuscript, Route evaluation, or novelty theorem.

## 1. Search protocol

Search date: **2026-08-24**.

Search surfaces included Cambridge Core, EMS Press, Springer, the Stacks
Project, arXiv, publisher/author book records, and the complete local Paper-12
owner.  Query families included:

```text
topological groupoid cohomology transitive vertex group
Mackenzie rigid cohomology Theorem 3
Morita differentiable cohomology cup product
continuous unnormalized nerve cochain complex
unnormalized normalized cosimplicial cochain Dold Kan
infinite cyclic group cohomology higher degrees
arbitrary products exact cohomology modules
```

Inclusion required a primary paper, authoritative monograph, or maintained
mathematical reference with a theorem/page locator matching at least one of
the frozen owners: the continuous unnormalized nerve complex, transitive
groupoid reduction, the infinite cyclic stabilizer, or arbitrary products.
Search snippets, encyclopedias, and theories with mismatched coefficient or
cochain categories were excluded as theorem evidence.

## 2. Source matrix

| Source | Exact use | Verification |
|---|---|---|
| K. A. Mackenzie, *Rigid cohomology of topological groupoids*, J. Austral. Math. Soc. A 26 (1978), 277--301, DOI `10.1017/S1446788700011794` | printed pp. 289--291 define the continuous nonhomogeneous unnormalized complex; printed pp. 297--299, Theorem 3, reduce locally trivial locally compact transitive groupoids to a vertex stabilizer | **VERIFIED** |
| M. Crainic, *Differentiable and algebroid cohomology...*, Comment. Math. Helv. 78 (2003), 681--721, DOI `10.1007/S00014-001-0766-9` | pp. 686--688 give all-degree Morita invariance and product compatibility in the differentiable category | **VERIFIED AS COMPARATOR** |
| J. Blanco, B. Uribe, K. Waldorf, *Pontrjagin duality on multiplicative gerbes*, JNCG 17 (2023), 1469--1520, DOI `10.4171/JNCG/528` | pp. 1473--1475 give continuous simplicial cochains and the nonhomogeneous differential | **VERIFIED AS CONVENTION COMPARATOR** |
| M. Fuchssteiner, C. Wockel, *Topological Group Cohomology with Loop Contractible Coefficients*, Topology Appl. 159 (2012), 2627--2634, arXiv `1110.2977` | globally versus locally continuous cochains for loop-contractible coefficients | **VERIFIED AS ONE-OBJECT COMPARATOR** |
| C. Weibel, *An Introduction to Homological Algebra* (1994), Example 6.1.4, p. 161 | the infinite cyclic group has cohomological dimension one; with trivial real coefficients, `H^0=R`, `H^1=R`, and `H^n=0` for `n>=2` | **VERIFIED** |
| Stacks Project, Tag `019H`, Lemma 14.25.1 | the unnormalized cosimplicial complex splits into its normalized part and an acyclic degenerate part | **VERIFIED** |
| Stacks Project, Tag `060J`, Lemma 12.32.1 | arbitrary products of modules are exact, so componentwise cohomology commutes with the product used for a bare orbit set | **VERIFIED** |

Primary links:

- <https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/rigid-cohomology-of-topological-groupoids/E6F26A7B330EB996D3D8AF982BA18DA5>
- <https://ems.press/journals/cmh/articles/410>
- <https://ems.press/journals/jncg/articles/12586094>
- <https://arxiv.org/abs/1110.2977>
- <https://www.cambridge.org/core/books/an-introduction-to-homological-algebra/AAA3F16482097015CD12D4376D505282>
- <https://stacks.math.columbia.edu/tag/019H>
- <https://stacks.math.columbia.edu/tag/060J>

## 3. Conditional routine-reduction theorem shape

The Paper-12 standardized groupoid is the topological coproduct

```text
G_std = coproduct_(q in Q) ((R/LZ) rtimes R).
```

Each component is transitive with vertex stabilizer `LZ ~= Z`.  Conditional
on the still-required exact comparison between the author-defined Paper-12
complex and the cited continuous groupoid complex, transitive reduction, the
cyclic-group computation, and exactness of arbitrary products give the
theorem shape

```text
H_cnv^n(G_std;R) ~= product_(q in Q) H^n(Z;R),

H_cnv^0(G_std;R) ~= R^Q,
H_cnv^1(G_std;R) ~= R^Q,
H_cnv^n(G_std;R) = 0                    for n>=2.
```

The unnormalized convention does not create extra higher classes: its
degenerate summand is acyclic.  Algebraically, the cup product is
componentwise.  `H^0` acts coordinatewise on `H^1`, while every product of
two positive-degree classes is zero.  This must not be rewritten as the
ordinary exterior algebra on the full vector space `R^Q`, because classes on
different coproduct components do not multiply across components.

## 4. What remains to check locally

The source screen is sufficient to decide publication disposition, but a
Paper-12 amendment should still contain direct owner-matching checks:

1. write the comparison from the exact author-defined unnormalized complex
   to Mackenzie's complex, including signs and continuity;
2. verify the Alexander--Whitney cup convention and multiplicativity of the
   selected comparison;
3. derive the actual-owner higher cohomology from Paper 12's all-degree time
   factorization before stating the higher-degree value of `J*`;
4. avoid any topology on cohomology unless closed-image and quotient-topology
   questions are separately proved.

These are proof-completion tasks, not a credible standalone novelty delta.

## 5. Maximum-prior and disposition

Paper 12 explicitly left higher standardized cohomology uncomputed, so the
calculation is useful as closure.  However, Mackenzie's transitive reduction,
the classical cohomological dimension of `Z`, and exactness of products
already determine the answer almost entirely.  A new independent paper would
therefore overstate the increment.

```text
HIGHER_STANDARDIZED_GROUPS=CONDITIONAL_ROUTINE_ZERO_IN_DEGREES_GE_2
EXACT_AUTHOR_COMPLEX_THEOREM=PARTIAL_OWNER_MATCH_REQUIRED
ARBITRARY_Q_ASSEMBLY=PASS
UNNORMALIZED_EXTRA_CLASSES=REFUTED
STANDALONE_NOVELTY=FAIL
DISPOSITION=MERGE_INTO_PAPER_12
MANUSCRIPT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```

If a future draft requires nonzero standardized cohomology in degree at least
two, that branch is stopped by this audit.
