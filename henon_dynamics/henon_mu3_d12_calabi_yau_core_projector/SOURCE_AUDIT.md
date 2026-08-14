# HCS-C52 source and novelty audit

Status: **PASS; primary locators, claim contexts, bibliography, and machine
scope checked**

## 1. Source policy

The mathematical claims in C52 are separated into three layers:

1. exact identities proved directly for the frozen H\'enon source;
2. standard results invoked with exact primary locators; and
3. interpretations or successor questions that are explicitly not
   promoted to theorems.

The literature search is targeted and non-exhaustive.  C52 does not claim
absolute novelty.  Its narrow proposed delta is the explicit
\(K\)-rational order-\(24\) projective monomial source action, its
rank-\(10\) Chow summand for this H\'enon-derived fivefold, and the sharp
rank-\(10\) obstruction inside the associated rational graph algebra.

## 2. Cayley ring and Hodge numbers

Favero, Iliev, and Katzarkov, *On the Griffiths groups of Fano manifolds
of Calabi--Yau Hodge type*, arXiv:1212.2608:

- Section 5.1, equation (6), printed page 16, records for a smooth
  \((2,3)\) complete-intersection fivefold in \(\mathbf P^7\)
  \[
  h^{4,1}=h^{1,4}=1,\qquad h^{3,2}=h^{2,3}=83.
  \]
- Section 5.4, equation (8), printed pages 18--19, uses the Cayley
  polynomial \(F=yf+zq\), the bidegrees
  \(\deg y=(1,-3)\), \(\deg z=(1,-2)\),
  \(\deg x_i=(0,1)\), and the identification
  \(H_{\mathrm{prim}}^{5-p,p}=R_{p,-3}\).
- Lemma 5.5 on printed page 22 concerns a special diagonal model.  C52
  does not import its explicit basis into the non-diagonal H\'enon
  quadric.
- Theorem 5.10 on printed page 27 concerns an infinite Griffiths group.
  It is not a Chow-projector theorem.
- Lemma 7.8, Proposition 7.9, and Theorem 7.10 on printed pages 34--35
  concern noncommutative Calabi--Yau/Griffiths-group structures.  They do
  not construct the projector used in C52 and do not realize its
  rank-\(10\) summand by a Calabi--Yau threefold.

The Hodge dimensions in C52 agree with this primary source.  The group
character and invariant dimensions are new exact calculations for the
frozen source, not quotations from Favero--Iliev--Katzarkov.

Primary locator:
[arXiv:1212.2608](https://arxiv.org/abs/1212.2608),
DOI [10.48550/arXiv.1212.2608](https://doi.org/10.48550/arXiv.1212.2608).

## 3. Ordinary Chow--Künneth projectors versus MCK

Laterveer, *Algebraic cycles and intersections of a quadric and a cubic*,
arXiv:2105.02224:

- the proof of Theorem 4.1, printed pages 8--9, writes the ordinary
  nonmiddle projectors for a degree-six complete intersection in the
  form
  \[
  \pi_Y^{2j}=\frac{1}{6}h^{n-2-j}\times h^j
  \]
  and takes the middle complement;
- Theorem 4.1 proves a multiplicative Chow--Künneth decomposition only
  when the ambient projective dimension \(n\) is even;
- the introduction states that the odd-\(n\), \(n>3\), MCK case remains
  open.

Our source lies in \(\mathbf P^7\), so the MCK theorem does not apply.
C52 uses only the elementary ordinary projectors
\(\pi_{2i}=\frac16h^{5-i}\times h^i\), verifies their compositions
directly, and then composes the middle complement with graph averages.
No MCK multiplicativity is asserted.

Primary locator:
[arXiv:2105.02224](https://arxiv.org/abs/2105.02224),
DOI [10.48550/arXiv.2105.02224](https://doi.org/10.48550/arXiv.2105.02224).

## 4. Graph-character projectors and the hypothesis firewall

Laterveer, Nagel, and Peters, *On complete intersections in varieties
with finite-dimensional motive*, arXiv:1709.10259:

- Section 6, equation (4), printed pages 19--20, gives the standard
  graph-character projector;
- Theorems 6.4 and 6.5, printed pages 20--21, impose additional
  hypotheses involving \(B(M)\), orbit separation, linear independence,
  finite-dimensionality of motives, and coniveau/niveau.

C52 uses only the finite-group averaging identity and exact graph
composition.  It has not checked the hypotheses of Theorems 6.4--6.5.
Accordingly, C52 does not infer coniveau, niveau, finite-dimensionality,
abelian type, or any description of the rank-\(158\) complement by an
abelian variety.

Primary locator:
[arXiv:1709.10259](https://arxiv.org/abs/1709.10259),
DOI [10.48550/arXiv.1709.10259](https://doi.org/10.48550/arXiv.1709.10259).

## 5. Exact claims proved internally

The following statements are established by finite calculation plus
elementary correspondence identities, rather than imported from the
literature:

- completeness of the \(24\)-element projective monomial source
  stabilizer;
- the presentation
  \(G=\operatorname{Dih}(C_{12})=C_{12}\rtimes C_2\), with order \(24\);
- the residue action with the mandatory multiplier
  \(\det(M_g)/\det(A_g)\);
- the exact character rows on \(R_{2,-3}\);
- the invariant multiplicity \(4\) in \(H^{3,2}\);
- the rank-\(10\)/rank-\(158\) Hodge decomposition; and
- the augmentation lower bound for idempotents in \(\mathbf Q[G]\).

The Chow identities use only
\(\int_Xh^5=6\), the composition rule for decomposable
correspondences, graph multiplication, and group averaging.  At release,
the finite enumeration and linear algebra must be accompanied by an
exact producer artifact and a genuinely independent fail-closed checker.

## 6. Relation to internal prior work

- C43--C47 concern coefficient fields, Galois norm roots, branching, and
  operator ideals.  They do not construct this fivefold projector.
- C48 identifies the genus-four curve controlling the second moment.
- C49 identifies the \((2,3)\) threefold controlling the third moment.
- C50 resums the second moment through elliptic factors and controls the
  fourth-moment geometry.
- C51 derives the weight--clock bifurcation and isolates the fourth
  odd packet \(O_4=H^5(X)(2)\) as a projector gate.

C52 answers that gate only partially: it constructs a rank-\(10\)
extreme-Hodge summand and proves that the obvious rational graph algebra
cannot reduce it to rank \(2\).

## 7. External barriers and closest neighbors

Argüz, Bousseau, Pandharipande, and Zvonkine,
*Gromov--Witten theory of complete intersections via nodal invariants*,
arXiv:2109.13323, Section 4.1, Proposition 4.1, printed page 57, reviews
Deligne's full-symplectic-monodromy theorem for the primitive cohomology
of the universal odd-dimensional complete-intersection family.  It is
not an original ABPZ calculation and is not used as theorem-bearing
evidence in C52.  The reviewed very-general-family statement does not
exclude a proper algebraic sub-Hodge structure on the present special
\(\operatorname{Dih}(C_{12})\) fiber.

Cattani, Deligne, and Kaplan, *On the locus of Hodge classes*,
J. Amer. Math. Soc. **8** (1995), Theorem 1.1 and Corollary 1.4, prove
algebraicity results for Hodge/sub-Hodge loci.  These results explain why
a special symmetric locus is a legitimate target; they do not construct
the C52 projector.

Achter, Casalaina-Martin, and Vial, *Distinguished models of intermediate
Jacobians*, J. Inst. Math. Jussieu **19** (2020), introduction, printed
pages 2--3, emphasize that arithmetic descent of the relevant abelian
variety is not automatic, even over \(\mathbf Q\).  Their Theorem A and
Section 6, Theorem 6.1, give sufficient realizations under additional
geometric hypotheses, including coniveau or the full middle cohomology
of a level-one odd complete intersection.  They do not apply
automatically to the present projected rank-\(158\) summand.  Therefore
its level-one ledger does not justify an \(A_{79}/K\) claim.

Ciurca, Tanimoto, and Tschinkel, *Intermediate Jacobians and
linearizability*, arXiv:2403.06047v2, Sections 2--3 and Theorem 3.3,
develop an equivariant intermediate-Jacobian torsor formalism for
threefold rationality and linearizability.  Their setting is not a Chow
splitting of this fivefold.

Ze Xu, *Motivic multiplicativity of complete intersections*,
arXiv:2511.01362v2, revised 30 July 2026, Theorems 1.4 and 4.19, studies
natural Chow--K\"unneth decompositions and multiplicativity defects for
smooth Fano and Calabi--Yau complete intersections in weighted
projective space.  It does not supply the present
\(\operatorname{Dih}(C_{12})\) middle split, coniveau, or an abelian
realization.

Iliev and Roulleau, *On the \(\mathrm{PSL}(2,19)\)-invariant cubic
sevenfold*, arXiv:1301.1142, abstract, Theorem 1, and Corollary 10, prove that the
underlying \(85\)-dimensional intermediate-Jacobian torus is abelian and
identify a symmetry-invariant abelian ninefold.  This is the closest
conceptual warning against claiming that the strategy “high symmetry
plus Calabi--Yau-type Fano cohomology” is new.  Their variety is a cubic
sevenfold, their group is different, and their result is not a
\(K\)-rational Chow projector for the frozen H\'enon \((2,3)\)
fivefold.

Primary locators:

- [arXiv:2109.13323](https://arxiv.org/abs/2109.13323);
- [Cattani--Deligne--Kaplan, DOI
  10.1090/S0894-0347-1995-1273413-7](https://doi.org/10.1090/S0894-0347-1995-1273413-7);
- [Achter--Casalaina-Martin--Vial, DOI
  10.1017/S1474748018000245](https://doi.org/10.1017/S1474748018000245);
- [arXiv:2403.06047](https://arxiv.org/abs/2403.06047);
- [arXiv:2511.01362](https://arxiv.org/abs/2511.01362); and
- [arXiv:1301.1142](https://arxiv.org/abs/1301.1142).

## 8. Novelty statement and nonclaims

A targeted search located general Cayley-ring formulas, ordinary/MCK
projector results for \((2,3)\) complete intersections, and
graph-character projectors under stronger motivic hypotheses.  It did
not locate the exact frozen H\'enon source, the order-\(24\) projective
monomial source action, or this rank-\(10\) graph-average calculation.
That statement is a search report, not an absolute novelty claim.

C52 must not claim any of the following:

- \(G\) is the full automorphism group of \(X\);
- the rank-\(10\) Hodge structure comes from an actual Calabi--Yau
  threefold;
- the rank-\(158\) complement has coniveau one or equals
  \(H^1(A)(-2)\) for an abelian variety \(A/K\);
- the graph-algebra obstruction excludes correspondences outside
  \(\mathbf Q[G]\);
- the same Chow projector has already been proved to form a strict
  compatible system with computed common Frobenius polynomials;
- automorphy or a Hasse--Weil functional equation;
- a new analytic half-plane for the normalized H\'enon Euler germ;
- a Riemann divisor or a self-adjoint Hilbert--P\'olya operator.

The safe realization statement is narrower: one \(K\)-rational Chow
projector induces idempotents in every Weil realization, and the
\(\ell\)-adic idempotents are \(G_K\)-equivariant.  C52 does not compute
or certify strict \(\ell\)-compatibility of the resulting local
polynomials.
