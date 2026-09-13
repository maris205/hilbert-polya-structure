# Novelty Assessment

## Decision

**PROVISIONAL NOVELTY GO, SUBJECT TO INDEPENDENT SOURCE REVIEW AND A SEARCH
REFRESH AT ANY FUTURE SOURCE LOCK.**

The bounded primary-source search through 2026-08-17 found no direct collision
with the combined theorem package. This is not a global priority assertion.

## What is being assessed

The novelty object is not Laurent's theorem, the standard fact that characters
form a group-algebra basis, or the known shift-like map definition. It is the
following integrated package:

1. for every dimension `k`, every standard type `nu`, and every
   `0<=m<=k`, the exact torus-coset deficit

   `dim H<=k-m`

   in the anchored sparse survivor variety;
2. an explicit saturated equality subtorus for every window and rank-one
   sharpness at `T_{k-1}`;
3. an exact planar classification of what replaces the anchored singleton step
   when `c=0`;
4. the unique nonlinear two-step survivor support `{1,d}`, the exact locus
   `a=-beta^2`, and the exact coset `C_d`; and
5. proof that the exceptional coset closes at the third recurrence, followed by
   qualitative finite-rank arithmetic corollaries for arbitrary torsion.

The conceptual contribution is the **constant-anchor mechanism**: a constant
plus at least two nonconstant powers forces one trivial middle character per
equation; deleting the constant leaves one and only one low/high pair
alternation in the planar nonlinear phase.

## Paper16 portfolio penalty

Paper16 already proves substantially more at the planar anchored endpoint:

- for `k=2,c!=0,s>=2`, an explicit `T_2` cardinality bound and sharp
  infinite `T_1` examples; and
- for `k=2,c!=0,s=1`, the fully absorbed explicit `T_4` bound and `T_3`
  sharpness theorem.

Accordingly, Paper17 receives no novelty credit for the bare implication
“`k=2,c!=0,s>=2` gives finite `T_2`.” Its Laurent-based specialization is a
weaker qualitative shadow. It also receives no credit for support-one anchored
phenomena.

After that deduction, the surviving novelty is still material:

- the exact all-window dimension profile is new on the portfolio axes `k`,
  `nu`, and `m`;
- the proof gives an integral `2m` relation law, not merely terminal
  finiteness;
- equality is attained by a saturated subtorus at every `m`;
- the no-gcd result and correct residue translation are genuinely
  higher-dimensional bookkeeping;
- the `c=0` phase is outside Paper16's hypotheses and is classified exactly;
  and
- the resonance has an exact coefficient locus, exact geometric coset, and
  exact closing window.

Paper17 therefore does not absorb Paper16, and Paper16 remains a separate
terminal predecessor. Paper14 is already fully absorbed inside Paper16 and is
not revived or separately reabsorbed by Paper17.

## Closest-work collision table

| Work | Closest point of contact | Material difference after theorem-level check | Collision judgment |
|---|---|---|---|
| Laurent 1984 | Finite-rank/division-group intersections with torus subvarieties | Supplies only the qualitative conversion from no coset to finiteness; does not analyze these recurrence varieties. | Foundational input, not collision. |
| Bedford--Pambuccian 1998 | Standard higher-dimensional type-`nu` shift-like maps | Complex filtration and potential theory, not finite-rank survivor varieties or character deficits. | Provenance only. |
| Bera 2018; Bera--Verma 2013 | Shift-like complex dynamics in `C^k` | Degeneration, Fatou components, entire maps, unstable manifolds; no arithmetic support phase. | No collision. |
| Bell--Ghioca 2022 | Orbit intersections with subgroups | One fixed orbit and time-index structure in a finitely generated subgroup; not all initial states or finite-window coset geometry. | Adjacent but distinct. |
| Ji--Xie--Zhang 2025/26 | Cyclotomic points and Hénon-type periodic applications | Zariski-density rigidity for cyclotomic preperiodic/periodic points; not finite-rank window finiteness or sparse-support resonance. | Adjacent but distinct. |
| Mello--Yasufuku 2026 | Higher-dimensional multiplicative dependence in semigroup dynamics | Orbit density/dependence, partly conditional; not survivor-variety coset classification. | Adjacent but distinct. |
| Karimov et al. 2024/25 | Multiple reachability and a torus-subvariety method for a linear rotation case | Real linear systems and algorithmic reachability, not polynomial shift-like recurrences. | Methodological neighbor only. |
| Kaur 2026 | Current shift-like maps | Transcendental complex dynamics, no arithmetic or sparse-recurrence theorem. | No collision. |
| Paper16 | Planar anchored finite-rank windows | Explicit quantitative theorem at `k=2,c!=0`; Paper17's novelty is all-dimensional geometry and exact `c=0` boundary. | Portfolio overlap disclosed and deducted. |

## Candidate-by-candidate novelty disposition

The Batch05 idea search considered more directions than the final package. The
following are explicitly stopped rather than repackaged:

| Candidate | Disposition | Reason |
|---|---|---|
| Reprove planar anchored finiteness via Laurent | **STOP** | Strictly dominated by Paper16's explicit bound. |
| Extend only the terminal `T_k` finiteness to higher dimension | **STOP as standalone** | Too thin without the full `k-m` profile, equality, and sharpness. |
| Claim a general gcd-dependent type phase | **STOP** | Bookkeeping is a residue translation; gcd does not occur. |
| Classify all maximal/equality cosets in Part A | **STOP** | Only the upper bound and a sharp family are proved. |
| Give effective finite-window cardinalities from Laurent | **STOP** | Laurent input is qualitative. |
| Extend to arbitrary Laurent/rational support | **STOP** | Negative exponents and poles change the singleton and survivor geometry. |
| Treat arbitrary mixed multiplicative cosets | **STOP** | No complete compatible-coset classification is proved. |
| Extend to arbitrary shift-like polynomial automorphisms | **STOP** | The scalar one-middle-coordinate recurrence is essential. |
| Anchored all-window profile plus exact zero-anchor plane | **GO** | One mechanism, two exact phases, complete author proof, and portfolio-distinct contribution. |

## Adversarial theorem tests

### Coefficient cancellation

The Part A proof does not assume `P(xi)!=0`. The zero branch retains the future
copy relation and the nonzero branch is stronger. In Part B, every
trivial-middle equation is split explicitly into nonroot killing and root-copy
branches.

### Torsion and disconnected cosets

The character proof runs on the connected identity component, whose character
lattice is torsion-free. Disconnected components are finite translates with
the same dimension. Arbitrary arithmetic torsion, including `mu_infinity`, is
placed inside a division group elementwise; it is not assumed finitely
generated or bounded.

### Rotation bookkeeping

The forced initial residues are

`{n-nu mod k:0<=n<m}`.

This is a translation of consecutive indices. It is not the orbit
`{-j nu mod k}`. Thus a gcd phase would be an artifact and has been removed.

### Exceptional-locus completeness

For a binomial `{p,q}`, the local nontrivial branches have two orientations.
The four two-label words force respectively `pq=1`, `q^2=1`, `p^2=1`, and
`pq=1`. Only the third is possible, forcing `p=1`. Its scalar equations force
exactly `a=-beta^2`; no other coefficient locus remains.

### Orientation correction

The nonlinear monomial sharp tuple is

`(x_0,x_1,x_2)=(t^e,t,2t^e)`

because `x_2=P(x_1)+a x_0`. The transposed tuple from an early idea note is not
carried into the theorem package.

## Unified-article test

The package passes the unity test for an article of about 22 substantive pages:

- both parts use the same `V_m` formalism and character restrictions;
- Part B is obtained by deleting exactly the constant character used in Part
  A's singleton step;
- the local partition calculus explains why the anchored theorem is robust and
  why one exceptional zero-anchor phase exists;
- Laurent is invoked once, after both geometric classifications; and
- Paper16 is handled in one common boundary section.

The 22-page budget in `RESEARCH_QUESTION.md` assigns 19.5 pages to definitions
and proofs and only 2.5 pages to overlap, related work, and limitations. No
padding, computational appendix, or catalogue of examples is needed.

## Portfolio-adjusted scores

Scores use a ten-point scale and already deduct the planar anchored overlap
with Paper16.

| Axis | Score | Basis |
|---|---:|---|
| Novelty | **8.0/10** | Exact all-`k,nu,m` geometry and exact `c=0` resonance survive the Paper16 penalty; no direct collision found. |
| Standalone value | **8.2/10** | Two main theorems, saturated equality, sharp arithmetic examples, and one coherent anchor-loss story support ~22 pages. |
| Proof confidence | **9.3/10** | All character partitions, scalar branches, integral independence, field reduction, torsion, and closure are explicit; only independent rereading remains. |

These exceed the required gates `7.5/7.5/9.0`.

## Fifteen nonclaim audit

All fifteen locked anti-claims from the idea report remain excluded:

1. no dimension claim about `T_m` itself;
2. no universal `Gamma`-infinitude claim at resonance;
3. no necessity claim for `a=1,P(1)=0`;
4. no gcd phase;
5. no iterated-rotation killed set;
6. no no-finite-window claim for nonlinear monomials;
7. no effective Laurent bound;
8. no novelty claim for the standard character partition alone;
9. no positive characteristic, `a=0`, rational, or arbitrary-automorphism
   extension;
10. no affine-conjugacy invariance of support;
11. no finite-generation or bounded-torsion substitution;
12. no improvement claim over Paper16's explicit bound;
13. no global priority claim;
14. no classification of all maximal/equality cosets; and
15. no height, periodic, or effective-enumeration claim.

## Final novelty judgment

The merged package is more than the sum of two notes because Part B classifies
the exact failure of Part A's defining constant-anchor move. After the full
Paper16 portfolio penalty, novelty, standalone value, and proof confidence all
remain above gate.

**GO: retain the unified Paper17 package. STOP every incremental or dominated
variant listed above.**
