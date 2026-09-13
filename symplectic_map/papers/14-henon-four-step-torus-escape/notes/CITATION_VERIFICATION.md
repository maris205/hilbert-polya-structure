# Citation Verification

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Verification policy

- Literature freeze date: 2026-08-16.
- Only author papers, journal pages, and author-posted/arXiv preprints are
  used as technical evidence.
- Search-engine summaries, encyclopedias, blogs, and secondary surveys are
  not evidence.
- Only Evertse--Schlickewei--Schmidt is imported as a proof theorem.
- Every other source is used only to delimit prior-art scope unless a later
  independent review explicitly promotes a precise theorem.
- No source below is treated as proving the proposed four-step theorem.

## V1. Evertse--Schlickewei--Schmidt

**Source.** J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt,
“Linear equations in variables which lie in a multiplicative group,”
Annals of Mathematics 155 (2002), 807--836.

- Journal: https://annals.math.princeton.edu/2002/155-3/p04
- Author manuscript/arXiv: https://arxiv.org/abs/math/0409604
- Exact imported result: published Theorem 1.1; the arXiv HTML conversion
  displays the main bound as Theorem 0.1.
- Verified scope: characteristic-zero field; subgroup of
  \((K^\ast)^n\) of finite rank \(R\); arbitrary fixed nonzero coefficients;
  nondegenerate solutions of a linear equation.
- Verified explicit bound:
  \[
  \exp\!\bigl((6n)^{3n}(R+1)\bigr).
  \]
- Specialization used here: \(n=3\), \(R=3r\), giving
  \[
  \exp\!\bigl(18^9(3r+1)\bigr).
  \]
- Critical applicability note: coefficients need not lie in the
  multiplicative group. The variables
  \((x_{i+1},x_i^d,x_{i-1})\) lie in \(\Gamma^3\), while
  \(c^{-1},-b/c,-a/c\) are fixed coefficients.
- Not supplied by this source: Hénon dynamics, the factor \(4d\), the
  degeneracy table, \(81d^2\), or the \(T_3\) example.
- Status: **THEOREM INPUT VERIFIED**.

## V2. Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve

**Source.** Holly Krieger, Aaron Levin, Zachary Scherr, Thomas J. Tucker,
Yu Yasufuku, and Michael Zieve, “Uniform Boundedness of S-Units in Arithmetic
Dynamics,” Pacific Journal of Mathematics 274 (2015), 97--106.

- Primary link: https://arxiv.org/abs/1406.1990
- Journal DOI: https://doi.org/10.2140/pjm.2015.274.97
- Range locked: Theorem 1.7 gives an image \(S\)-unit bound for the stated
  class of monic \(S\)-integral polynomials, while Theorem 1.8 is a special
  one-bad-coefficient orbit result over a number field.
- Boundary: one-dimensional image/orbit arithmetic; not a two-dimensional
  Hénon initial-state count and not the present arbitrary-characteristic-zero
  finite-rank theorem.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V3. Canci--Paladino

**Source.** Jung-Kyu Canci and Laura Paladino, “Preperiodic points for
rational functions defined over a global field in terms of good reductions.”

- Primary link: https://arxiv.org/abs/1403.2293
- Range locked: the main result bounds \(K\)-rational preperiodic points of
  an endomorphism of \(\mathbb P^1\) using the number of bad-reduction
  places; a two-variable \(S\)-unit theorem is an input.
- Boundary: \(\mathbb P^1\), global fields, and reduction data; no Hénon
  four-step survival set.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V4. Canci--Vishkautsan and Canci--Troncoso--Vishkautsan

**Sources.**

1. J. K. Canci and Solomon Vishkautsan, “Scarcity of cycles for rational
   functions over a number field.”
   https://arxiv.org/abs/1604.03965
2. J. K. Canci, Sebastian Troncoso, and Solomon Vishkautsan, “Scarcity of
   finite orbits for rational functions over a number field.”
   https://arxiv.org/abs/1711.04649

- Range locked: explicit periodic or preperiodic bounds for rational
  functions on \(\mathbb P^1\), depending on degree and bad-reduction data;
  the first paper also treats finitely generated semigroups of rational
  functions.
- Boundary: neither paper counts all Hénon initial states lying in a
  finite-rank torus through a fixed window.
- Status: **PRIMARY BOUNDARY SOURCES; NO THEOREM IMPORTED**.

## V5. Ostafe--Sha--Shparlinski--Zannier

**Source.** Alina Ostafe, Min Sha, Igor E. Shparlinski, and Umberto Zannier,
“On multiplicative dependence of values of rational functions and a
generalisation of the Northcott theorem.”

- Primary link: https://arxiv.org/abs/1706.05874
- Range locked: Corollary 4.9 concerns multiplicative dependence among
  consecutive univariate iterates, while Theorem 4.11 gives finiteness for
  two distinct iterates under its squarefreeness hypotheses.
- Boundary: univariate value dependence is not coordinatewise subgroup
  survival and is not a Hénon survival theorem.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V6. Bérczes--Ostafe--Shparlinski--Silverman

**Source.** Attila Bérczes, Alina Ostafe, Igor E. Shparlinski, and
Joseph H. Silverman, “Multiplicative dependence among iterated values of
rational functions modulo finitely generated groups.”

- Primary link: https://arxiv.org/abs/1811.04971
- Range locked: Theorems 1.2--1.4 classify the relevant exceptional behavior
  for iterated values of univariate rational functions modulo a finitely
  generated multiplicative group. Theorem 1.7 gives, under its hypotheses,
  finiteness for two polynomial iterates that are multiplicatively dependent
  modulo such a group.
- Boundary: multiplicative dependence modulo a group is not coordinatewise
  membership in that group and does not count all initial states of a
  two-dimensional Hénon map; there is no four-step threshold or
  coefficient-uniform \(d,r\) count.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V7. Bell--Chen--Hossain

**Source.** Jason P. Bell, Shaoshi Chen, and Ehsaan Hossain, “Rational
dynamical systems, S-units, and D-finite power series,” Algebra & Number
Theory 15 (2021), 1699--1728.

- Primary link: https://arxiv.org/abs/2005.04281
- Journal DOI: https://doi.org/10.2140/ant.2021.15.1699
- Range locked: Theorem 1.1 concerns a fixed dynamical sequence
  \(a_n=f(\varphi^n(x_0))\) and says that its membership-time set for a
  finitely generated multiplicative group is a finite union of arithmetic
  progressions plus a Banach-density-zero set. Theorem 1.2 gives a
  torus-factor conclusion for a fixed Zariski-dense orbit under its
  hypotheses.
- Boundary: structure of hitting times for one fixed orbit, not a uniform
  count of all initial points and not a finite-window cardinality theorem.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V7A. Bell--Ghioca

**Source.** Jason P. Bell and Dragos Ghioca, “Intersections of orbits of
self-maps with subgroups in semiabelian varieties,” Bulletin of the London
Mathematical Society 56 (2024), 783--795.

- Journal DOI: https://doi.org/10.1112/blms.12964
- Primary preprint: https://arxiv.org/abs/2210.03152
- Range locked: Theorem 1.1(i) says that, for one fixed orbit of a rational
  self-map of a semiabelian variety and a finitely generated subgroup, the
  return-time set is a finite union of arithmetic progressions plus a
  Banach-density-zero set. Under the regular-self-map hypothesis, Theorem
  1.1(ii) makes only that residual set finite; it does not say that the whole
  return-time set is finite.
- Applicability boundary: \(H|_{\mathbb G_m^2}\) is generally rational rather
  than regular as a torus self-map, because \(b x^d+a y+c\) can vanish.
  In either clause the initial point is fixed and the subgroup is finitely
  generated. There is no all-initial-state count, prescribed finite-window
  cutoff, or rank-only cardinality bound.
- Status: **CLOSE PRIMARY WHOLE-STATE BOUNDARY; NO THEOREM IMPORTED**.

## V8. Grieve--Noytaptim

**Source.** Nathan Grieve and Chatchai Noytaptim, “On non-Zariski density of
\((D,S)\)-integral points in forward orbits and the Subspace Theorem.”

- Primary link: https://arxiv.org/abs/2407.08614
- Range locked: Theorem 1.2 and Corollary 1.5 give sufficient conditions for
  non-Zariski density of integral points in one fixed forward orbit of a
  regular surjective projective self-map, using divisor dynamics and the
  Subspace Theorem.
- Boundary: qualitative non-density for a fixed orbit, not a uniform finite
  count of all Hénon initial states.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V9. Noytaptim--Zhong

**Source.** Chatchai Noytaptim and Xiao Zhong, “Towards Common Zeros of
Iterated Morphisms.”

- Primary link: https://arxiv.org/abs/2412.15141
- Range locked: Theorem 1.2 concerns non-Zariski density of a common-iterate
  locus for two compositionally independent Hénon-type maps and a third
  morphism.
- Boundary: common-zero unlikely intersections; no finite-rank torus,
  four-step survivor set, or explicit \(d,r\) bound.
- Status: **PRIMARY BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V10. Kim--Krieger--Postolache--Szeto

**Source.** Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and
Vivian Szeto, “Hénon maps with many rational periodic points.”

- Primary link: https://arxiv.org/abs/2412.01668
- Version locked: v2, 2025-07-08.
- Range locked: Theorem A constructs, for every odd \(d>2\), a rational
  polynomial \(s_d\) of degree at most \(d\) for which
  \[
  h_d(x,y)=(y,-x+s_d(y))
  \]
  has at least \((d-4)^2\) rational periodic points. Theorem B, for
  \(d\equiv1\pmod6\), gives an integer cycle of length \((8d+10)/3\).
- Boundary: after a coordinate swap this remains a general-polynomial Hénon
  family, not the present monomial-plus-constant family. It is a
  degree-dependent periodic-point lower-bound boundary, not a collision with
  fixed-rank \(T_4\) finiteness or \(T_3\) sharpness.
- Required nonclaim: Paper 14 does not assert a general rational or integral
  periodic-point bound.
- Status: **PRIMARY HÉNON BOUNDARY SOURCE; NO THEOREM IMPORTED**.

## V11. Ji--Xie--Zhang

**Source.** Zhuchao Ji, Junyi Xie, and Geng-Rui Zhang, “Cyclotomic integral
points for affine dynamics.”

- Primary link: https://arxiv.org/abs/2511.13443
- Version locked: v2, 2026-01-20.
- Exact range locked: Theorem 1.8 states that periodic points over the maximal
  cyclotomic extension for a Hénon-type polynomial automorphism over a number
  field are not Zariski dense; Corollary 1.9 specializes this to plane
  polynomial automorphisms of positive entropy.
- Boundary: non-Zariski-density is not finiteness; maximal cyclotomic
  extensions are not arbitrary fixed finite-rank groups; there is no explicit
  \(d,r\) count.
- Status: **CLOSE PRIMARY HÉNON BOUNDARY; NO THEOREM IMPORTED**.

## V12. Mello--Yasufuku

**Source.** Jorge Mello and Yu Yasufuku, “On higher dimensional integrality
and multiplicative dependence in semigroup algebraic dynamics.”

- Primary link: https://arxiv.org/abs/2604.03745
- Version locked: v1, 2026-04-04.
- Range locked: Theorems 1.1--1.2 and Corollary 1.3 concern semigroups of
  projective endomorphisms over number fields and finitely generated
  subgroups, conditional on \(\mathrm{Hyp}_\epsilon\); the main results
  require \(\epsilon\ge(1+c)/2\). Theorem 4.2, under additional divisor
  hypotheses and Vojta's Main Conjecture, supplies the relevant non-density
  only for sufficiently small \(\epsilon\), so it does not verify the general
  hypothesis required by the main theorems.
- Boundary: this is a conditional projective-semigroup result, not an
  unconditional Hénon or fixed-window count over every characteristic-zero
  field.
- Status: **CLOSEST 2026 GENERAL BOUNDARY; NO THEOREM IMPORTED**.

## V13. Arithmetic Hénon height and parameter context

**Sources.**

1. Patrick Ingram, “Canonical heights for Hénon maps.”
   https://arxiv.org/abs/1111.3609
2. Liang-Chung Hsia and Shu Kawaguchi, “Heights and periodic points for
   one-parameter families of Hénon maps.”
   https://arxiv.org/abs/1810.03841

- Range locked: canonical heights, specialization, periodic parameters, and
  unlikely intersections in Hénon families.
- Boundary: no finite-rank torus-survival count.
- Status: **PRIMARY CONTEXT SOURCES; NO THEOREM IMPORTED**.

## Collision conclusion

A targeted primary-source search through 2026-08-16 located no theorem
combining this three-coefficient Hénon family, arbitrary finite-rank
multiplicative groups, a coefficient-uniform four-transition cardinality
bound, and a rank-one sharp three-transition failure. This conclusion is a
bounded search statement, not an assertion that no unpublished or unindexed
result exists.

## Citation nonclaims

- No theorem is inferred from an abstract beyond its stated scope.
- No secondary source is used to extend a theorem.
- No recent non-density theorem is paraphrased as a finiteness theorem.
- No \(\mathbb P^1\) result is treated as a Hénon result.
- No finite-generation hypothesis from one source is silently replaced by
  finite rank.
- No Paper 15 quartic source is part of this bibliography.
