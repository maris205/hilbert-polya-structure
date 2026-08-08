# HCS-C21 source and novelty audit

**Audit date:** 2026-08-08

## 1. Evidence labels

- **P1 -- primary/full-text verified:** metadata and the relevant primary
  passage or formula were inspected.
- **P2 -- primary/metadata verified:** publisher or DOI metadata and abstract
  were checked, but no new C21 formula is taken from an uninspected passage.
- **L -- local source:** a repository manuscript was inspected directly and
  is not represented as peer-reviewed literature.
- **R -- repository theorem:** an earlier reproducible repository result used
  as an input.
- **N -- negative targeted search:** no matching result was found in a finite
  search; this is provisional novelty evidence, never proof of priority.

## 2. Foundational model and byte lock

The foundational local source is Liang Wang's repository manuscript,
[*An Area-Preserving Hénon-Map Model for the Riemann Zeros: A
Deterministic-Dynamics Approach with Quantum and Dissipative
Solvers*](../docs/prior_work/papers/5-An%20Area-Preserving%20Henon-Map%20Model.pdf)
(2026).  No DOI or journal publication was verified.  Its frozen SHA-256 is

`23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9`.

It supplies the recurrence

\[
q_{t+1}=1-Aq_t^2-q_{t-1}.
\]

For $A\ne0$, $x_t=Aq_t$ gives exactly

\[
x_{t+1}=A-x_t^2-x_{t-1}.
\]

C21 inherits only this reversible area-preserving family.  It does not use
the manuscript's continuum approximation, quartic regularization, selected
near-critical parameter, fitted zero comparison, or Hilbert--Pólya
interpretation as evidence.  The scaling is singular at $A=0$; C21's
algebraic statements at exceptional parameters are derived directly rather
than transferred through the scaling.  **Evidence: L.**

A local PDF read-integrity preflight was unavailable because the optional
PDF parser was not installed.  The file bytes are locked, but this audit does
not use unverified page anchors from that PDF.

## 3. Primary low-period Hénon program

| Key | Source | Precise support | Boundary | Evidence |
|---|---|---|---|---|
| `endlergallas2002` | A. Endler and J. A. C. Gallas, [*Arithmetical Signatures of the Dynamics of the Hénon Map*](https://doi.org/10.1103/PhysRevE.65.036231), *Physical Review E* **65** (2002), 036231; [author PDF](https://inaesp.org/PublicJG/pre_EG02.pdf). | Develops the parameter-dependent orbital-sum method and a fourth-degree polynomial parametrizing period-four orbits. | Does not construct the period-six ordered-edge normalization or its chronological cohomology. | P2 |
| `endlergallas2004` | A. Endler and J. A. C. Gallas, [*Existence and Characterization of Stable Ghost Orbits in the Hénon Map*](https://doi.org/10.1016/j.physa.2004.06.019), *Physica A* **344** (2004), 491--497; [author PDF](https://inaesp.org/PublicJG/PHYSA_Endler_Gallas_2004.pdf). | Gives the general two-parameter period-six coordinate, orbit-sum, and stability polynomials. | Studies ghost-orbit stability, not the normalization, branch divisor, genus, or $H^1$-representation of the Hamiltonian chiral ordered cover. | P1 |
| `endlergallas2006sums` | A. Endler and J. A. C. Gallas, [*Reductions and Simplifications of Orbital Sums in a Hamiltonian Repeller*](https://doi.org/10.1016/j.physleta.2006.01.031), *Physics Letters A* **352** (2006), 124--128; [author PDF](https://inaesp.org/PublicJG/endler_gallas_orbital_sums_PLA2006.pdf). | Uses both $y_{t+1}=1-ay_t^2-y_{t-1}$ and the scaled Hamiltonian recurrence; gives exact period-five/six sums, factorization, and algebraic-number structure. | Does not identify the generic twelve-state period-six splitting cover or compute its chronology on $H^1$. | P1 |
| `endlergallas2006chiral` | A. Endler and J. A. C. Gallas, [*Conjugacy Classes and Chiral Doublets in the Hénon Hamiltonian Repeller*](https://doi.org/10.1016/j.physleta.2006.04.042), *Physics Letters A* **356** (2006), 1--7; [author PDF](https://inaesp.org/PublicJG/conjugacy_classes_PLA_356_1_2006.pdf). | Equations (11)--(15) give the class factorization, $C^{\mathrm{mark}}_6=\sigma-2$, $D^{\mathrm{mark}}_6=\sigma^2+4\sigma-4a$, and the factorization $P_6=f_r f_{-r}$, $r^2=a-3$.  The text identifies the two cycles via in-phase root combinations. | Does not define or normalize the parameter-varying twelve-state ordered-pair scheme; no connectedness, $D_6$ function field, complete branch data, genus, or chronological $H^1$ theorem was found. | P1 |
| `gallas2007` | J. A. C. Gallas, [*Counting Orbits in Conjugacy Classes of the Hénon Hamiltonian Repeller*](https://doi.org/10.1016/j.physleta.2006.08.065), *Physics Letters A* **360** (2007), 512--514; [author PDF](https://inaesp.org/PublicJG/counting_PLA360_512_2007.pdf). | Gives all-period Möbius formulas for diagonal, non-diagonal, and chiral cycle classes; in particular, one chiral doublet at $n=6$ and two at $n=7$. | Counts classes but does not determine the parameter-cover geometry or time-character cohomology.  Any C21 first-occurrence statement must concern nontrivial weight-one chronology, not chirality itself. | P1 |

The period-14 table inconsistency already recorded by HCS-C12C is irrelevant
to C21.  The exact formulas and unambiguous $n=6,7$ rows are the only count
inputs used here.

## 4. Decisive period-six prior formula

The central source boundary is Endler--Gallas (2006), equations (11)--(15):

\[
S_6(\sigma)
=(C^{\mathrm{mark}}_6(\sigma))^2
D^{\mathrm{mark}}_6(\sigma)N^{\mathrm{mark}}_6(\sigma),
\]

and

\[
C^{\mathrm{mark}}_6(\sigma)=\sigma-2,
\qquad
D^{\mathrm{mark}}_6(\sigma)=\sigma^2+4\sigma-4A.
\]

At the chiral value $\sigma=2$, their equation (15) is

\[
\begin{aligned}
P_6(x)={}&
[x^3-(1+r)x^2-Ax+A(1+r)-1]\\
&\times[x^3-(1-r)x^2-Ax+A(1-r)-1],
\qquad r^2=A-3.
\end{aligned}
\]

C21 writes the historical radical $r$ as $\eta$.  It claims no novelty
for the marker, the first chiral doublet, the six-coordinate polynomial, the
quadratic base extension, or the cubic factorization.

## 5. General polynomial-automorphism boundary

| Key | Source | Precise support | Applicability boundary | Evidence |
|---|---|---|---|---|
| `friedlandmilnor1989` | S. Friedland and J. Milnor, [*Dynamical Properties of Plane Polynomial Automorphisms*](https://doi.org/10.1017/S014338570000482X), *Ergodic Theory and Dynamical Systems* **9** (1989), 67--99. | Theorem 2.6 gives generalized-Hénon normal form; Theorem 3.1 gives total fixed-point multiplicity (d^n) for the (n)-th iterate, with special-fiber collision caveats. | Multiplicity (2^n) is not a primitive-period component theorem and gives no ordered-edge monodromy, genus, or cohomology. | P1 |
| `hutz2010` | B. Hutz, [*Dynatomic Cycles for Morphisms of Projective Varieties*](https://nyjm.albany.edu/j/2010/16-8.html), *New York Journal of Mathematics* **16** (2010), 125--159; [full text](https://nyjm.albany.edu/j/2010/16-8p.pdf), arXiv:0801.3643. | Proves effectivity and multiplicity results for formal-period dynatomic zero-cycles of projective morphisms. | Hutz's hypotheses concern everywhere-defined projective morphisms.  C21 does not invoke those theorems for the affine Hénon family; its exact-period and normalization statements are proved directly. | P1 |

## 6. Repository prior work

| Key | Project | Frozen result | C21 boundary | Evidence |
|---|---|---|---|---|
| `hcsc12a` | HCS-C12A, `henon_frobenius_scheme_obstruction` | At fixed $n$, the reduced finite-field Frobenius zeta is a finite permutation determinant and is cyclotomic/nilpotent-blind. | Fixed-period rationality is not a new arithmetic signal. | R |
| `hcsc12c` | [HCS-C12C](../henon_dihedral_chronology_obstruction/) | Coarse $C^{\mathrm{mark}}_6,D^{\mathrm{mark}}_6,N^{\mathrm{mark}}_6$ quotient normalizations have genus zero; constant-coefficient quotient cohomology retains only invariant sectors. | These are coarse orbit-sum markers, not the six-coordinate carrier or twelve-state ordered-edge normalization. | R |
| `hcsc19` | [HCS-C19](../henon_period7_frobenius_curve/) | For an adopted correction of the printed period-seven equation: exact neighbor reconstruction, scalar genus three, and a degree-14 oriented lift. | C21 may compare but not reclaim these results.  No publisher erratum or full saturated (P_7) classification is asserted. | R |
| `hcsc20` | [HCS-C20](../henon_period7_dihedral_cover/) | The adopted period-seven ordered-edge component is a connected genus-eight (D_7) splitting curve with rotation quotient genus two, RM, and selected-prime local factors. | C21's period-seven dimension is a byte-locked dependency, not a new derivation. | R |

The certificate freezes HCS-C12C at SHA-256
`964b8c98abc850493529b8e939a9c8ff96c832300ad2b1629b1cff807f0e8020`
and HCS-C20 at
`7ee43e3253aff15ec00d78b9633c3d3362e71cd5a880cd3e928e7f322abb2681`.

## 7. Defensible C21 theorem delta

The defensible contribution is restricted to:

1. the precise twelve-state ordered-edge function field attached to the
   published period-six chiral doublet;
2. its geometric connectedness, group (D_6) of order twelve, complete
   compactified branch calculation, and genus one;
3. its exact rotation fixed field and trivial order-six action on
   weight-one cohomology;
4. the scoped comparison with the certified HCS-C20 component; and
5. the proof that the apparent $D^{\mathrm{mark}}_6/C^{\mathrm{mark}}_7$
   field match is a period-one marker shadow, together with the restricted
   clock-divisibility obstruction.

The phrase "first occurrence" is permitted only in the form:

> Among source-identified and repository-certified chiral ordered components
> with $n\le7$, the smallest period at which at least one certified
> component has nontrivial weight-one time characters is seven.

It does not mean first chirality, first nonzero $H^1$, classification of all
exact-period components, or first Hilbert--Pólya structure.

## 8. Finite novelty search and limitation

The audit used repository-wide searches; the complete local Paper-5
manuscript; primary Endler--Gallas/Gallas PDFs; APS, Cambridge, and NYJM
records; and targeted searches for combinations of
`Hénon`, `period 6`, `chiral`, `D6 cover`, `genus`, `cohomology`,
`ordered-edge`, `dynatomic curve`, the exact cubic, and its discriminant.

No inspected source computed the normalization, complete branch data, genus,
or chronological $H^1$-representation of this specific period-six
twelve-state ordered cover.  The safe provisional novelty statement is:

> Starting from the published period-six scalar polynomial, C21 determines
> the normalized ordered-edge cover geometry and chronological cohomology,
> then compares it with the repository-certified period-seven component.

This was a targeted search, not a complete MathSciNet, zbMATH, Web of Science,
or Scopus cited-reference audit.  It cannot prove priority or exclude an
unindexed paper, thesis, or differently worded treatment.  The manuscript
must avoid unqualified phrases such as "previously unknown" or "no prior
work."
