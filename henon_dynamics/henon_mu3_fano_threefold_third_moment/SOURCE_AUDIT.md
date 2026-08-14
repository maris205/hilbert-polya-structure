# Primary-source audit

Only primary or official archival sources support theorem-level external
claims.  The C49-specific identities and smoothness elimination are new
derivations and must be certified internally.

## Diagonal equations and Jacobi sums

André Weil, **“Numbers of solutions of equations in finite fields,”**
*Bulletin of the American Mathematical Society* 55 (1949), 497--508,
DOI [10.1090/S0002-9904-1949-09219-4](https://doi.org/10.1090/S0002-9904-1949-09219-4).

Official PDF:
[American Mathematical Society scan](https://www.ams.org/bull/1949-55-05/S0002-9904-1949-09219-4/S0002-9904-1949-09219-4.pdf).

Relevant locators:

* pp. 499--502, especially equations (3) and (4): character expansion,
  Jacobi sums, Gauss products, and absolute values;
* pp. 505--506, equations (7) and (8): projective diagonal hypersurfaces
  and their zeta factors.

C49 rederives the six-variable cubic specialization explicitly, including
the sign and the multiplicity twenty.

Lars Br\"unjes, **“On the zeta function of forms of Fermat equations,”**
arXiv:math/0301186 [math.NT] (2003),
DOI [10.48550/arXiv.math/0301186](https://doi.org/10.48550/arXiv.math/0301186).

Primary PDF:
[arXiv](https://arxiv.org/pdf/math/0301186).

Relevant locators: Definition 4.4 defines the Jacobi sums used in the
cohomological description; Proposition 4.5 records their Weil-size and
symmetry properties; Theorem 4.6 gives the Frobenius eigenspace
decomposition; and Example 4.7 specializes to a cubic Fermat example.  C49
uses this only as cohomological context: its coefficient twenty, sign, and
six-variable specialization are derived internally.

## Frobenius weights

Pierre Deligne, **“La conjecture de Weil. I,”** *Publications
Mathématiques de l'IHÉS* 43 (1974), 273--307.

Official IAS record and PDF:
[IAS Publications](https://publications.ias.edu/node/368).

Relevant locator: Théorème (1.6), pp. 275--277, which gives absolute value
\(q^{i/2}\) for Frobenius eigenvalues on \(H^i\) of a smooth projective
variety.  C49 applies it to primitive \(H^4(S)\) and \(H^3(X)\).

## Fano \((2,3)\) threefold classification context

V. A. Iskovskikh, **“Fano 3-folds. I,”** *Math. USSR-Izvestiya* 11
(1977), 485--527.  The official archival scan explicitly lists
\(V_{2,3}\subset\mathbf P^5\) as the complete intersection of a quadric and
a cubic:
[MathNet English PDF](https://www.mathnet.ru/links/bc3ede047cb8944de593c14a35a54dcd/im1823_eng.pdf).

V. A. Iskovskikh, **“Fano 3-folds. II,”** *Math. USSR-Izvestiya* 12
(1978), 469--506,
DOI [10.1070/IM1978v012n03ABEH001994](https://doi.org/10.1070/IM1978v012n03ABEH001994),
[MathNet record](https://www.mathnet.ru/eng/im1778).

C49 does not rely on classification for its numerical invariants: adjunction,
the Chern-class expansion, and weak Lefschetz are written out.

S. Bloch and J. P. Murre, **“On the Chow group of certain types of Fano
threefolds,”** *Compositio Mathematica* 39 (1979), 47--105.

Official NUMDAM record and PDF:
[NUMDAM](https://www.numdam.org/item/CM_1979__39_1_47_0/).

Relevant locator: the opening setup on p. 47 explicitly includes the smooth
intersection of a quadric and a cubic in \(\mathbf P^5\).  It is cited only
for classical context, not for the C49 trace formula or the internally
derived value \(b_3=40\).

## Lefschetz framework

A. Grothendieck et al., **SGA 2: Cohomologie locale des faisceaux
cohérents et théorèmes de Lefschetz locaux et globaux**, North-Holland
(1968), official recomposed text:
[SGA 2 PDF](https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2original.pdf).

Exact locators: Exposé XII, Corollaire 3.7 (recomposed-text p. 115;
original-edition p. 153; physical PDF file p. 123) gives the Picard group of
a projective complete intersection of dimension at least three.  Exposé
XIV, Corollaire 4.6 (recomposed-text p. 184; original-edition p. 267;
physical PDF file p. 192) is the global cohomological Lefschetz theorem used
for the non-middle comparison.  C49 invokes these only for the standard
non-middle cohomology/Picard ledger; the remaining Betti number is derived
from the displayed Chern-class calculation.

## Regularized-determinant background

Barry Simon, **Trace Ideals and Their Applications**, second edition,
Mathematical Surveys and Monographs 120, American Mathematical Society
(2005), ISBN 978-0-8218-4988-0.

Official publisher record and table of contents:
[American Mathematical Society](https://bookstore.ams.org/SURV/120).

Relevant locator: Chapter 9, “Regularized determinants and renormalization
in quantum field theory.”  This citation supports classical background
only.  The normalized faithful semifinite trace, the graded quotient, the
seven chronological counterterms, and the C49 \(\operatorname{Det}_8\)
identity are defined and proved inside the repository; Simon is not cited
as a source for those new constructions.

## Chevalley--Warning provenance

Ewald Warning, **“Bemerkung zur vorstehenden Arbeit,”** *Abhandlungen aus
dem Mathematischen Seminar der Universität Hamburg* 11 (1935), 76--83,
DOI [10.1007/BF02940715](https://doi.org/10.1007/BF02940715).

The exact divisibility needed here is also proved directly in
`PROOF_PACKAGE.md`, so no black-box strengthening is used.

## Internal claims requiring repository certificates

The following are not delegated to literature and are derived internally:

* the frozen Hénon phase and trace normalization;
* radial direction formula (4);
* the twisted split-quadric matrix (5);
* the characteristic-zero and candidate all-split smoothness elimination;
* the exact \(C_{p,3},c_{p,3}\) substitutions;
* the \(\Re s>1/4\) and \(\tau\)-Det8 conclusions.

The phase, direction count, moment identities, convergence improvement, and
determinant conclusion are replayed by the producer/checker and cannot be
promoted from a citation or finite pilot alone.  The released smoothness
theorem uses the characteristic-zero certificate and therefore permits a
finite exceptional set.  For the optional all-split strengthening, the
checker recomputes the exact resultant and factorization from frozen
elimination coefficients, but it does not rederive the triangular
eliminants or every modular Gröbner basis from the original ideal.  That
coverage boundary is recorded in `results/RESULTS.md`; the all-split claim is
not used in the released theorem.
