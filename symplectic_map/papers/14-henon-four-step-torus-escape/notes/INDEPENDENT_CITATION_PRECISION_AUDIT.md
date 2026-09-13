# Independent Citation Precision Audit

## Audit identity and canonical verdict

- Audit date and literature freeze: **2026-08-16**.
- Audit type: fresh independent, primary-source, citation-precision and
  collision audit.
- Frozen input: the eleven files and SHA-256 values recorded below.
- Mathematical execution: none.  No numerical, parameter, prime, modulus,
  finite-field, CAS, or symbolic science scan was run.
- Imported proof theorem: only Evertse--Schlickewei--Schmidt, exactly as in
  the current source package.

The canonical verdict is

> **`CITATION_REPAIR_REQUIRED`**

This is a citation-state verdict, not a mathematical rejection.  The
fixed-coefficient ESS reduction, rank \(3r\), four local equations, the
\(4dE(3,3r)\) term, the degeneracy analysis, and the \(81d^2\) term require
**no mathematical repair** in this audit.  No direct prior-art collision with
the combined theorem was located.  The existing \(7.0/10\) novelty score may
be retained after the mandatory repairs below.

This later audit supersedes only the citation-pass component of
`INDEPENDENT_SOURCE_DESIGN_REVIEW.md`; it does not reverse that file's proof
replay or alter any theorem-bearing file.

## Mandatory correction of the window convention

The project convention is

\[
T_m(H,\Gamma)=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2\text{ for every }0\le j\le m\}.
\]

Thus “four-step” means **four transitions**, not four states:

\[
P,H(P),H^2(P),H^3(P),H^4(P)\in\Gamma^2.
\]

Writing \(H^j(P)=(x_j,x_{j-1})\), a point of \(T_4\) supplies the four local
equations indexed by \(i=0,1,2,3\).  Correspondingly, \(T_3\) contains four
states and supplies three local equations.  The rank-one construction in the
source package shows that this three-transition window can be infinite.

An earlier external checkpoint suggested \(0\le j\le m-1\).  That suggestion
is expressly withdrawn here.  Under that shifted convention the symbol
\(T_4\) would denote the project's \(T_3\), precisely the window for which the
package constructs infinitely many points.  All eleven frozen project files
already use the correct \(0\le j\le m\) convention, so this correction creates
no source-file repair item.

The current fixed-coefficient equation is also already correct:

\[
\frac1c x_{i+1}-\frac bc x_i^d-\frac ac x_{i-1}=1.
\]

Its variables \((x_{i+1},x_i^d,x_{i-1})\) lie in \(\Gamma^3\), of rank at
most \(3r\); \(c^{-1},-b/c,-a/c\) are fixed nonzero coefficients and need
not lie in \(\Gamma\).  No coefficient-enlarged group should be introduced.

## Frozen eleven-file source state

The audit is bound to the following pre-audit manifest.  Sizes are in bytes.

| Frozen file | Bytes | SHA-256 |
|---|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5,522 | `709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95` |
| `experiments/EXPERIMENT_TRACKER.md` | 2,139 | `da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97` |
| `notes/CITATION_VERIFICATION.md` | 10,732 | `ccd48de4e4c96a2b207cf9da911fda427fe8e79c35320779dc02dc2ab694b87c` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 5,902 | `d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 18,618 | `e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c` |
| `notes/NOVELTY_ASSESSMENT.md` | 7,550 | `eed574ca465683985dfb329f7a494b6f7862ff6cc60ef07550796be8046c845f` |
| `notes/PROOF_PACKAGE.md` | 13,728 | `c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa` |
| `notes/RESEARCH_QUESTION.md` | 6,371 | `782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c` |
| `refine-logs/FINAL_PROPOSAL.md` | 6,431 | `af46eae7ef8cc4e8872bcc2ce33ee80c82ff354c7e52346aa575c8018b14db33` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,045 | `ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22` |
| `refine-logs/REVIEW_SUMMARY.md` | 6,383 | `ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f` |

The eleven files total **87,421 bytes**.  The SHA-256 of the lexicographically
sorted `sha256sum` manifest using `./`-prefixed relative paths is

`18e8a542d9b345165f9ebdecf6693266be6f078a8cef9cfec970228077f94bbe`.

This digest excludes the present audit file.

## Collision conclusion

Targeted searches for finite-rank multiplicative subgroups, \(S\)-units,
integral points, torus/subgroup survival, Hénon maps, consecutive orbit
states, and fixed finite windows located no theorem having all of the
following scope:

1. \(H(x,y)=(b x^d+a y+c,x)\) with \(abc\ne0\);
2. an arbitrary characteristic-zero base field;
3. a prescribed finite-rank \(\Gamma\le K^\ast\), not necessarily finitely
   generated;
4. a coefficient-uniform cardinality bound for all initial points in \(T_4\);
5. dependence only on \(d\) and \(r\); and
6. sharp failure at the immediately shorter \(T_3\) window.

The strongest direct Hénon near-collision is Ji--Xie--Zhang's non-Zariski-
density theorem for cyclotomic periodic points.  The strongest omitted
whole-state subgroup near-neighbor is Bell--Ghioca's fixed-orbit return-time
theorem.  Neither supplies finiteness or a uniform count of all initial
states in a fixed finite window.

The safe novelty statement remains:

> A targeted primary-source search through 2026-08-16 located no theorem
> combining this three-coefficient Hénon family, arbitrary finite-rank
> multiplicative groups, a coefficient-uniform four-transition cardinality
> bound, and a rank-one sharp three-transition failure.

This is a bounded search report, not an absolute priority claim.

## Primary-source precision matrix

### 1. Evertse--Schlickewei--Schmidt: proof input, already correct

J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt,
“Linear equations in variables which lie in a multiplicative group,”
*Annals of Mathematics* 155 (2002), 807--836
([journal](https://annals.math.princeton.edu/2002/155-3/p04),
[arXiv](https://arxiv.org/abs/math/0409604)).

- The imported result is published **Theorem 1.1**; the arXiv HTML
  conversion displays it as Theorem 0.1.
- It applies over a characteristic-zero field to a finite-rank subgroup of
  \((K^\ast)^n\), with arbitrary fixed nonzero coefficients, and counts only
  nondegenerate solutions.
- Its bound is
  \(\exp((6n)^{3n}(R+1))\).  Here \(n=3\) and \(R\le3r\), giving
  \(\exp(18^9(3r+1))\).
- It supplies neither the four-index union bound nor any degenerate branch.

**Audit disposition:** no change to V1, the proof formula, or the theorem.

### 2. One-dimensional \(S\)-unit and multiplicative-dependence boundary

- Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve,
  “Uniform Boundedness of S-Units in Arithmetic Dynamics,” *Pacific Journal
  of Mathematics* 274 (2015), 97--106
  ([journal PDF](https://msp.org/pjm/2015/274-1/pjm-v274-n1-p05-s.pdf),
  [arXiv](https://arxiv.org/abs/1406.1990)).  **Theorem 1.7** gives an image
  \(S\)-unit bound for the stated class of monic \(S\)-integral polynomials;
  **Theorem 1.8** is a special one-bad-coefficient orbit result.  These are
  number-field, \(S\)-unit, one-dimensional results, not finite-rank Hénon
  window counts.
- Ostafe--Sha--Shparlinski--Zannier, “On multiplicative dependence of values
  of rational functions and a generalisation of the Northcott theorem”
  ([arXiv](https://arxiv.org/abs/1706.05874)).  **Corollary 4.9** concerns
  multiplicative dependence among consecutive univariate iterates, while
  **Theorem 4.11** gives finiteness for two distinct iterates under its
  squarefreeness hypotheses.  Neither is coordinatewise subgroup survival.
- Bérczes--Ostafe--Shparlinski--Silverman, “Multiplicative dependence among
  iterated values of rational functions modulo finitely generated groups”
  ([arXiv](https://arxiv.org/abs/1811.04971)).  **Theorems 1.2--1.4** classify
  relevant exceptional behavior; **Theorem 1.7** gives a finiteness result
  for two polynomial iterates modulo a finitely generated group under its
  hypotheses.  Multiplicative dependence modulo a group is not the condition
  that every orbit coordinate belongs to that group.
- Bérczes--Bugeaud--Győry--Mello--Ostafe--Sha, “Multiplicative dependence of
  rational values modulo approximate finitely generated groups”
  ([arXiv](https://arxiv.org/abs/2107.05371)).  **Corollary 1.4** treats
  consecutive univariate iterates modulo an approximate division group.
  It is a useful near-neighbor but is not currently required in the Paper 14
  bibliography.

### 3. Fixed-orbit torus and subgroup return times

Jason P. Bell, Shaoshi Chen, and Ehsaan Hossain, “Rational dynamical
systems, \(S\)-units, and \(D\)-finite power series,” *Algebra & Number Theory*
15 (2021), 1699--1728
([journal](https://doi.org/10.2140/ant.2021.15.1699),
[arXiv](https://arxiv.org/abs/2005.04281)).

- **Theorem 1.1** concerns one fixed orbit and one rational observable; the
  membership-time set is finitely many arithmetic progressions plus a
  Banach-density-zero set, which can be infinite.
- **Theorem 1.2** is the torus-factor conclusion for a fixed Zariski-dense
  orbit whose observable always lies in a finitely generated group.
- Neither theorem gives a uniform count over all starting points.

Jason P. Bell and Dragos Ghioca, “Intersections of orbits of self-maps with
subgroups in semiabelian varieties,” *Bulletin of the London Mathematical
Society* 56 (2024), 783--795
([journal](https://doi.org/10.1112/blms.12964),
[arXiv](https://arxiv.org/abs/2210.03152)).

- **Theorem 1.1(i)** says that, for one fixed orbit of a rational self-map of
  a semiabelian variety and a finitely generated subgroup, the return-time
  set is finitely many arithmetic progressions plus a Banach-density-zero
  set.
- **Theorem 1.1(ii)** makes only the residual set finite when the self-map is
  regular; it does not assert that the entire return-time set is finite.
- Restricting \(H\) to \(\mathbb G_m^2\) gives a rational self-map in general,
  not a regular self-map of the torus, because
  \(b x^d+a y+c\) can vanish.
- This is the most direct omitted near-neighbor because it treats whole-state
  subgroup membership.  It still assumes a fixed initial point and a
  finitely generated subgroup, and gives no all-initial-point cardinality,
  fixed-window cutoff, or rank-only bound.

### 4. Higher-dimensional integrality and Hénon boundaries

- Grieve--Noytaptim, “On non-Zariski density of \((D,S)\)-integral points in
  forward orbits and the Subspace Theorem”
  ([arXiv](https://arxiv.org/abs/2407.08614)).  **Theorem 1.2** and
  **Corollary 1.5** concern non-Zariski-density in one fixed orbit of a
  regular surjective projective self-map under divisor hypotheses.  A Hénon
  map is not a regular self-map of \(\mathbb P^2\).
- Noytaptim--Zhong, “Towards Common Zeros of Iterated Morphisms”
  ([arXiv](https://arxiv.org/abs/2412.15141)).  **Theorem 1.2** concerns the
  non-Zariski-density of a common-iterate locus for two compositionally
  independent Hénon-type maps and a third morphism.  It has no multiplicative
  subgroup or one-map window conclusion.
- Ji--Xie--Zhang, “Cyclotomic integral points for affine dynamics”
  ([arXiv](https://arxiv.org/abs/2511.13443)).  **Theorem 1.8** says that
  periodic points over the maximal cyclotomic extension for a Hénon-type
  polynomial automorphism over a number field are not Zariski dense;
  **Corollary 1.9** treats plane positive-entropy polynomial automorphisms.
  Non-density is not finiteness, and the maximal cyclotomic extension is not
  a prescribed finite-rank group.

### 5. Kim--Krieger--Postolache--Szeto: V10 precision repair

Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and Vivian Szeto,
“Hénon maps with many rational periodic points”
([arXiv:2412.01668v2](https://arxiv.org/abs/2412.01668)).

- **Theorem A** is for every odd \(d>2\), not “every odd \(d\ge2\).”  It
  constructs a rational polynomial \(s_d\) of degree at most \(d\) such that
  \[
  h_d(x,y)=(y,-x+s_d(y))
  \]
  has at least \((d-4)^2\) rational periodic points.  The construction yields
  integral points, but the theorem statement should be cited in its stated
  rational form.
- **Theorem B** applies when \(d\equiv1\pmod6\) and gives an integer cycle of
  length \((8d+10)/3\).
- After swapping coordinates this is a general-polynomial Hénon family.  The
  polynomial \(s_d\) is not restricted to a monomial plus a constant, so the
  family is outside \(b x^d+a y+c\).

This source establishes degree-dependent lower-bound context for general
Hénon maps.  It neither collides with a fixed-rank subgroup bound nor proves
the Paper 14 \(T_3\) sharpness construction.

### 6. Mello--Yasufuku: V12 precision repair

Jorge Mello and Yu Yasufuku, “On higher dimensional integrality and
multiplicative dependence in semigroup algebraic dynamics”
([arXiv:2604.03745v1](https://arxiv.org/abs/2604.03745)).

- **Theorem 1.1** works over a number field, with a finitely generated
  subgroup of \(\mathbb G_m^N(k)\), for a semigroup generated by degree-at-
  least-two endomorphisms of \(\mathbb P^N\).  For \(c<1\), it assumes
  \(\mathrm{Hyp}_\epsilon\) for some
  \(\epsilon\ge(1+c)/2\) and obtains containment in a proper closed set plus
  finitely many semigroup orbits.
- **Theorem 1.2** gives a finiteness conclusion outside the exceptional
  closed set for fixed exponents in the post-composition setting, and
  **Corollary 1.3** is the single-map specialization.
- The paper states that \(\mathrm{Hyp}_\epsilon\) is open in dimension at
  least two.
- **Theorem 4.2**, under its additional divisor hypotheses and assuming
  Vojta's Main Conjecture, proves the needed type of non-density only for
  sufficiently small \(\epsilon\).  Theorems 1.1--1.2 require sufficiently
  large \(\epsilon\ge(1+c)/2\); the paper expressly notes that Theorem 4.2 is
  not enough to verify the general main hypothesis.

It is therefore incorrect to say without qualification that Vojta verifies
the hypothesis needed for the main theorems.  The source is a conditional,
projective, finitely-generated-group near-neighbor, not an unconditional
Hénon fixed-window result.

## Mandatory source-package repair ledger

Only the following citation repairs are required.  No theorem, proof,
constant, or experiment file is to be changed on account of this audit.

### R1. Replace the V12 range statement

**Location:** `notes/CITATION_VERIFICATION.md`, frozen lines 198--211.

Replace the current suggestion that the paper records a general
“Vojta-conjectural route to the needed non-density” by text with the following
content:

> Theorems 1.1--1.2 and Corollary 1.3 concern projective endomorphism
> semigroups over number fields and finitely generated subgroups, conditional
> on \(\mathrm{Hyp}_\epsilon\); the main results require
> \(\epsilon\ge(1+c)/2\).  Theorem 4.2, under additional divisor hypotheses
> and Vojta's Main Conjecture, supplies only sufficiently small \(\epsilon\),
> and therefore does not verify the general hypothesis required by the main
> theorems.  This is not an unconditional Hénon or fixed-window result.

### R2. Replace the V10 range statement

**Location:** `notes/CITATION_VERIFICATION.md`, frozen lines 165--180.

Use the following precise content:

> Theorem A constructs, for every odd \(d>2\), a rational polynomial \(s_d\)
> of degree at most \(d\) for which
> \(h_d(x,y)=(y,-x+s_d(y))\) has at least \((d-4)^2\) rational periodic
> points.  Theorem B, for \(d\equiv1\pmod6\), gives an integer cycle of length
> \((8d+10)/3\).  After a coordinate swap this remains a general-polynomial
> Hénon family, not the monomial-plus-constant Paper 14 family.  It is a
> degree-dependent periodic-point lower-bound boundary, not a collision with
> fixed-rank \(T_4\) finiteness or \(T_3\) sharpness.

### R3. Add Bell--Ghioca 2024 without renumbering existing entries

**Location:** `notes/CITATION_VERIFICATION.md`, immediately after V7.

For a minimal diff, label it `V7A` rather than renumbering V8--V13.  Record
**Theorem 1.1(i)--(ii)** and the exact fixed-orbit/finitely-generated-group
scope stated above.  In particular, say that the regular clause makes the
Banach-density-zero residual set finite, not necessarily the whole
return-time set.  State explicitly that \(H|_{\mathbb G_m^2}\) is generally
rational rather than regular and that no all-initial-state count follows.

### R4. Add the theorem numbers that carry each boundary statement

**Location:** `notes/CITATION_VERIFICATION.md`.

- V2: retain Theorems 1.7--1.8; no change beyond preserving their different
  image/orbit roles.
- V5: add Corollary 4.9 and Theorem 4.11.
- V6: add Theorems 1.2--1.4 for exceptional-map scope and Theorem 1.7 for the
  closest polynomial-iterate finiteness statement.
- V7: add Theorem 1.1 for membership-time structure and Theorem 1.2 for the
  torus-factor conclusion.
- New V7A: add Theorem 1.1(i)--(ii).
- V8: add Theorem 1.2 and Corollary 1.5.
- V9: add Theorem 1.2.
- V10: add Theorems A and B.
- V11: Theorem 1.8 and Corollary 1.9 are already precise.
- V12: add Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2.

The bibliography need not import any of these results into the proof.  The
numbers lock the comparison scope only.

### R5. Record Bell--Ghioca and the corrected V10/V12 roles in novelty/refine

**Locations:**

- `notes/NOVELTY_ASSESSMENT.md`, especially frozen lines 92--117;
- `refine-logs/FINAL_PROPOSAL.md`, especially frozen lines 167--186.

The minimal replacement paragraph for the group-intersection discussion is:

> Bell--Chen--Hossain treat a fixed orbit through one observable, while
> Bell--Ghioca Theorem 1.1 treats return times of one fixed orbit of a
> rational self-map of a semiabelian variety to a finitely generated
> subgroup.  Both are qualitative return-time structure results; neither
> bounds all initial states surviving a prescribed four-transition Hénon
> window, and neither yields a rank-only cardinality bound.

The Hénon/higher-dimensional bullet list must identify Kim et al. as the
general-polynomial Theorem A/B lower-bound construction and Mello--Yasufuku
as conditional on \(\mathrm{Hyp}_\epsilon\), with Theorem 4.2's small-
\(\epsilon\) Vojta range distinguished from the main theorems' large-
\(\epsilon\) requirement.

These edits do not reduce the novelty score.  They make the residual novelty
delta more exact: the Paper 14 result concerns **all initial states**, a
**fixed four-transition window**, an **explicit rank-and-degree-only
cardinality**, **finite-rank rather than finitely generated groups**, and an
exact **T4/T3 threshold**.

## Files not requiring repair

- `notes/PROOF_PACKAGE.md` and `notes/RESEARCH_QUESTION.md` already use
  \(0\le j\le m\), five states for \(T_4\), four local equations, the correct
  fixed-coefficient ESS equation, and the rank-\(3r\) group.
- `notes/CLAIMS_EVIDENCE_MATRIX.md` correctly classifies the no-collision
  statement as a bounded search claim and the novelty score as advisory.
- The two experiment-design files contain no scientific result and require
  no citation-driven change.
- `refine-logs/INITIAL_PROPOSAL.md` is a historical record and need not be
  retroactively rewritten.
- `refine-logs/REVIEW_SUMMARY.md` already describes fixed-orbit hitting-time
  structure generically.  Naming Bell--Ghioca there is optional; it is not
  needed for the minimal repair once the citation, novelty, and final-refine
  records are corrected.
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` remains an immutable earlier
  review artifact.  The present later audit supplies the controlling
  citation verdict.

## Terminology and nonclaim controls

1. A finite-rank subgroup need not be finitely generated.  Results assuming
   a finitely generated group or an \(S\)-unit group may not be promoted to
   the Paper 14 scope.
2. \(\Gamma^2\) is a subgroup of \(\mathbb G_m^2(K)\), not itself necessarily
   an algebraic torus.  If “torus survival” is used, it must be defined as
   the coordinatewise membership condition above.
3. A periodic point \(P\in\Gamma^2\) need not have its entire orbit in
   \(\Gamma^2\).  The periodic corollary must continue to require whole-orbit
   containment.
4. Non-Zariski-density is not finiteness, and return-time sparsity is not a
   uniform cardinality bound.
5. The \(T_3\) sharpness claim is existential: for every \(d\ge2\) there are
   admissible \(K,H,\Gamma\) with \(T_3\) infinite.  It is not a claim that
   every \(H,\Gamma\) has infinite \(T_3\).
6. No claim should say “first Hénon arithmetic sparsity,” “first torus
   control,” or “first uniform arithmetic result for Hénon maps.”  The safe
   priority axis is the combined four-transition, all-initial-state,
   finite-rank, coefficient-uniform bound plus three-transition sharpness.

## Final assessment

- Direct collision: **none located**.
- Closest omitted near-neighbor: **Bell--Ghioca, Theorem 1.1 (2024)**.
- Most important scope correction: **Mello--Yasufuku's
  \(\mathrm{Hyp}_\epsilon\)/Vojta boundary**.
- Most important bibliographic-range correction: **Kim et al., Theorems
  A/B**.
- Novelty after repair: **7.0/10**, unchanged.
- Standalone-size and proof-confidence scores: unaffected by this
  citation-only audit.
- Canonical disposition: **`CITATION_REPAIR_REQUIRED`**, followed by a
  line-level citation recheck after R1--R5 are implemented.

No source-package theorem or proof change is authorized or requested by this
audit.
