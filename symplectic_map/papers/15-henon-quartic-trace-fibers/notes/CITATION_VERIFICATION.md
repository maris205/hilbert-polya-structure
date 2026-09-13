# Citation Verification

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Verification policy

- Literature freeze date: 2026-08-17.
- Technical evidence is restricted to author PDFs, journal records, and
  arXiv primary records.
- Search snippets and secondary summaries are not theorem evidence.
- Cantat--Dujardin's author PDF dated May 10, 2026 is the controlling
  version for this package.
- Every imported theorem is used only in its verified field, parameter, and
  multiplicity scope.
- “No direct collision located” is a bounded search report, not a priority
  claim.

## V1. Cantat--Dujardin: controlling source and version ledger

**Source.** Serge Cantat and Romain Dujardin, “Multiplier rigidity for
complex Hénon maps.”

- Controlling author PDF:
  https://perso.univ-rennes1.fr/serge.cantat/Articles/Mult.pdf
- Date printed in controlling PDF: May 10, 2026.
- Length: 51 pages.
- SHA-256 of the PDF retrieved on 2026-08-17:
  \(707edeb33d0b5ef4b97fa6c73f2c0c95d73d975f5d119d0e3bc5c10eefbd8cc2\).
- arXiv record: https://arxiv.org/abs/2603.09445
- arXiv DOI: https://doi.org/10.48550/arXiv.2603.09445
- Status at the freeze: preprint; no journal reference is present on the
  arXiv record.

### Version difference that must remain visible

The arXiv record has only v1, submitted March 10, 2026. Its PDF is internally
dated March 11, 2026. The v1 PDF retrieved for comparison has SHA-256

\[
025a6c6351a296476159e75e081e5fe24ec4aae37b087f98b5b8cf43078d1f0e.
\]

The author PDF is later and byte-distinct, so it controls. Direct inspection
of the passages used here found the statements of Theorem 3.7, Theorem 4.2,
and Example 4.3 substantively unchanged between arXiv v1 and the May 10
author version. This limited comparison does not assert that the two
manuscripts are identical elsewhere.

### Exact imported and boundary roles

1. **Formal spectra.** Section 3.1 defines formal-period points through
   closure and intersection multiplicity. Section 3.2 defines
   \(\operatorname{Trace}_n\) as a regular multiset map on the formal
   period-\(n\) cycle. This supports the formal, nonreduced convention.

2. **General finite cutoff.** Theorem 3.7 says that, for each degree, some
   finite period bound and a uniform fiber bound exist. It does not identify
   \(P(4)\), and it does not state \(P(4)=3\).

3. **Fixed-Jacobian low-period finiteness.** Theorem 4.2 is over
   \(\mathbb C\). For a single Hénon map of given degree with Jacobian
   different from \(-1\), it gives finite fibers from
   \[
   \bigl(\operatorname{Jac}(f),
   \operatorname{Trace}_1(f),
   \operatorname{Trace}_2(f)\bigr).
   \]
   In the notation \(f_{a,p}=(ay+p(x),x)\), this means \(a\ne1\). The
   theorem does not remove the Jacobian input.

4. **Direct precedent.** Example 4.3 gives
   \[
   p_\lambda(x)=(x-\lambda)^2(x+\lambda)^2
   =(x^2-\lambda^2)^2
   \]
   at Jacobian \(-1\), with constant period-one and period-two trace data.
   It also gives
   \[
   \operatorname{tr}(Df^2)=p'(x)p'(y)+2
   \]
   on the period-two equations.

### What V1 removes from novelty

- the exceptional family;
- its period-one and period-two blindness;
- the fact that degree four is the first degree for this obstruction;
- general finite trace rigidity;
- existence of some non-effective finite cutoff.

### What V1 does not state

- \(C_f'(1-a)=0\);
- at most \(d-1\) Jacobian candidates from pure fixed traces;
- the exact non-quasi-finite locus of \(\mathfrak T_{\le2}\);
- the explicit period-three moment;
- \(P_{\mathcal H^1}(4)=3\);
- an exact global degree, branch locus, or injectivity theorem.

**Status:** **MANDATORY THEOREM INPUT AND DIRECT PRECEDENT, SCOPE LOCKED.**

## V2. Sugiyama I: finite fixed-multiplier fibers

**Source.** Toshi Sugiyama, “The Moduli Space of Polynomial Maps and Their
Fixed-Point Multipliers,” Advances in Mathematics 322 (2017), 132--185.

- arXiv: https://arxiv.org/abs/0708.2512
- Journal DOI: https://doi.org/10.1016/j.aim.2017.10.013
- Current arXiv version at the freeze: v4, November 19, 2017.

The paper studies the fixed-multiplier map on degree-\(d\) polynomial
moduli. Main Theorem I applies on \(V_d\), the locus where no fixed
multiplier equals \(1\), equivalently where there is no multiple fixed
point. It gives finite fibers; in degree four the cardinality is at most
\((4-2)!=2\) in polynomial moduli.

### Exact use here

For the quartic root partition \([1111]\), put \(h=x+p\). Its fixed points
are the simple roots \(\alpha\) of \(p\), with multipliers

\[
h'(\alpha)=1+p'(\alpha)\ne1.
\]

Thus and only thus the tuple belongs to \(V_4\). Sugiyama yields finiteness
in polynomial moduli, and the residual \(\mu_3\)-normalization leaves only a
finite number of monic-centered representatives.

### Prohibited use

V2 is not used for \([31]\), \([211]\), \([22]\), or \([4]\). It does not
classify the exceptional Hénon curve or prove any Hénon period-three
statement.

**Status:** **THEOREM INPUT ONLY ON \([1111]\).**

## V3. Sugiyama II: monic-centered clarification

**Source.** Toshi Sugiyama, “The Moduli Space of Polynomial Maps and Their
Fixed-Point Multipliers: II. Improvement to the Algorithm and Monic Centered
Polynomials,” Ergodic Theory and Dynamical Systems, online February 3, 2023.

- arXiv: https://arxiv.org/abs/1802.07474
- Journal DOI: https://doi.org/10.1017/etds.2022.120
- Current arXiv version at the freeze: v2, February 23, 2023.

Theorem II gives the fiber count for the monic-centered fixed-multiplier map
on the same no-multiple-fixed-point domain \(V_d\). It clarifies the finite
residual normalization used in V2.

The abstract explicitly excludes parameter values whose fibers contain
polynomials with multiple fixed points from its general explicit formula.
This is another reason it may not be invoked on the four multiple-root
strata.

**Status:** **NORMALIZATION SUPPORT; SAME \([1111]\)-ONLY BOUNDARY.**

## V4. Friedland--Milnor: normalized Hénon structure

**Source.** Shmuel Friedland and John Milnor, “Dynamical properties of plane
polynomial automorphisms,” Ergodic Theory and Dynamical Systems 9(1)
(1989), 67--99.

- Journal DOI: https://doi.org/10.1017/S014338570000482X
- Journal record:
  https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dynamical-properties-of-plane-polynomial-automorphisms/43661938D1C6688699C178D0B47B97C0

This is the structural source for generalized Hénon normal forms and their
finite residual diagonal ambiguity. In this package the diagonal action is
also computed directly.

It does not prove the fixed-algebra derivative identity, the five-partition
quartic analysis, or the period-three moment.

**Status:** **STRUCTURAL BACKGROUND; NO HEADLINE NOVELTY.**

## V5. Cattani--Dickenstein--Sturmfels: residue method

**Source.** Eduardo Cattani, Alicia Dickenstein, and Bernd Sturmfels,
“Computing Multidimensional Residues,” in Algorithms in Algebraic Geometry
and Applications, Progress in Mathematics 143, Birkhäuser (1996), 135--164.

- DOI: https://doi.org/10.1007/978-3-0348-9104-2_8
- Preprint: https://arxiv.org/abs/alg-geom/9404011

This is a method source for multidimensional residues and quotient-algebra
trace identities on zero-dimensional complete intersections. The present
proof uses

\[
\operatorname{Tr}(M_h)=\operatorname{Res}(hJ)
\]

with \(J\) the complete-intersection Jacobian.

The residue formalism, top-coefficient extraction, and quotient traces are
not claimed as new. The Hénon specialization and exact ledger are internal
mathematics.

**Status:** **METHOD INPUT.**

## V6. Hutz: formal-period background

**Source.** Benjamin Hutz, “Dynatomic cycles for morphisms of projective
varieties,” New York Journal of Mathematics 16 (2010), 125--159.

- Journal PDF: https://nyjm.albany.edu/j/2010/16-8p.pdf
- arXiv: https://arxiv.org/abs/0801.3643

This is adjacent background for formal period, dynatomic cycles, and
multiplicity. The exact formal-period convention used in the theorem is
taken directly from Cantat--Dujardin, so no Hutz theorem is imported into
the proof.

**Status:** **BACKGROUND ONLY.**

## V7. Huguin: small-cycle polynomial moduli boundary

**Source.** Valentin Huguin, “Moduli spaces of polynomial maps and
multipliers at small cycles,” arXiv:2412.19335.

- arXiv: https://arxiv.org/abs/2412.19335
- Author PDF: https://vhuguin.com/publications/MPolyMult.pdf

Huguin treats one-variable polynomial moduli using periods one and two.
Cantat--Dujardin use that theorem inside their \(a\ne1\) argument. This
package imports Cantat--Dujardin Theorem 4.2 rather than re-importing or
extending Huguin.

It is not a theorem about Jacobian-\(-1\) automorphisms of \(\mathbb C^2\),
and it does not supply the exceptional-curve period-three formula.

**Status:** **ADJACENT BOUNDARY; NO DIRECT THEOREM IMPORTED.**

## V8. Internal Paper 12 provenance

The frozen local proof artifact is:

papers/12-henon-period3-residue/notes/PROOF_PACKAGE.md

Its SHA-256 at the source-design read was

\[
36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9.
\]

Paper 12 supplied provenance for:

- the classification \(p=(x^2-L)^2\) inside the fixed-trace-zero quartic
  slice;
- formal period-two and period-three subtraction;
- the two period-three slope ledgers;
- the constant ledger;
- the local fixed-branch length;
- pointwise and cyclewise normalization.

All of those steps are reproduced inside the present PROOF_PACKAGE.md.
Paper 12 is not cited as an external theorem and is not a black-box proof
dependency.

Publication policy is frozen: Paper 15 absorbs Paper 12's overlapping
theorem and proof; the two must not be submitted as parallel papers.

**Status:** **INTERNAL PROVENANCE, FULLY ABSORBED.**

## V9. Stacks Project: quasi-finite criterion

**Source.** Stacks Project, Lemma 29.21.10, Tag 02NH.

- Official tag: https://stacks.math.columbia.edu/tag/02NH

The lemma states that a morphism is quasi-finite if and only if it is
locally of finite type, quasi-compact, and has finite fibers. The trace maps
in this package are finite-type morphisms between finite-type complex
varieties, so the finite-geometric-fiber proof in PROOF_PACKAGE Step 14
supplies the required final implication.

Stacks Project Tag 02VI records that quasi-finiteness is fpqc local on the
base. It is not used to widen Parts B--C. Such a descent route would first
require an explicit model of the full trace morphism over a smaller field
and a verified base-change argument; neither is part of this package.

**Status:** **STANDARD FINAL-STEP INPUT; NO FIELD-SCOPE EXPANSION.**

## Bounded collision search

The following primary-source-targeted query families were checked through
2026-08-17:

- quartic Hénon period-three trace cutoff;
- Hénon \(P(4)=3\) trace spectrum;
- quartic Hénon multiplier rigidity through period three;
- the exact integers \(1296000\) and \(1572864\) with Hénon terms;
- forward and citing records around Cantat--Dujardin;
- fixed-multiplier fibers with quartic multiple-root partitions.

The search located Cantat--Dujardin as the direct family and lower-period
precedent, Sugiyama as the simple-root fixed-multiplier input, and the known
residue/formal-cycle methods. It did not locate an indexed primary source
stating the unified three-part package or the exact global cutoff
\(P_{\mathcal H^1}(4)=3\).

This is a bounded negative search result. It does not establish global
priority, does not cover unpublished work, and must be rerun by the fresh
reviewer.

## Citation-to-claim controls

| Claim component | Source role | Safe wording |
|---|---|---|
| formal trace multiset morphisms | Cantat--Dujardin §3.1--3.2 | “using the formal-period trace convention of Cantat--Dujardin” |
| some finite cutoff exists | Cantat--Dujardin Theorem 3.7 | “general Noetherian finiteness is known; its cutoff is not explicit here” |
| fixed \(a\ne1\), periods 1--2 finite | Cantat--Dujardin Theorem 4.2 | “after pure traces finitely enumerate the Jacobian” |
| exceptional quartic family and lower blindness | Cantat--Dujardin Example 4.3 | “following the family exhibited by Cantat--Dujardin” |
| \([1111]\) fixed-multiplier finiteness | Sugiyama | “only on the no-multiple-fixed-point stratum” |
| normalized Hénon finite ambiguity | Friedland--Milnor / direct calculation | “in the single-factor monic-centered normal form” |
| trace--residue identity | Cattani--Dickenstein--Sturmfels | “classical residue input” |
| \(C_f'(s)=0\) and at most \(d-1\) Jacobians | internal proof | do not attribute to external sources |
| exact non-quasi-finite locus | internal proof plus direct lower precedent | do not call the family new |
| period-three moment and cutoff | internal proof, Paper 12 provenance absorbed | “no direct indexed collision located in a bounded search” |

## Mandatory citation audit before exit

A fresh reviewer must:

1. open the May 10 author PDF rather than relying only on arXiv v1;
2. recheck Cantat--Dujardin Theorems 3.7 and 4.2 and Example 4.3;
3. verify that Theorem 4.2 is used over \(\mathbb C\), with fixed Jacobian,
   and only for \(a\ne1\);
4. open Sugiyama's theorem and confirm every \([1111]\) multiplier is in
   \(V_4\);
5. confirm Sugiyama is absent from every multiple-root argument;
6. verify the residue theorem's exponent and nonreduced applicability;
7. verify Tag 02NH applies to the exact finite-type trace morphism;
8. repeat the bounded direct-collision search;
9. reject every absolute priority phrase.
