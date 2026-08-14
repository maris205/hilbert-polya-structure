# HCS-C51 source and novelty audit

Status: **PASS; primary-source locators and the frozen release bibliography were checked**

## 1. Source policy

HCS-C51 uses primary papers, official publisher metadata, and predecessor
artifacts.  It does not infer theorems from search snippets or finite-prime
patterns.  Every external source below has a narrow assigned role.

## 2. Theorem-bearing sources

### Deligne purity

- P. Deligne, “La conjecture de Weil. I,” *Publications Mathématiques de
  l'IHÉS* **43** (1974), 273--308,
  DOI 10.1007/BF02684373.
- Exact locator: Theorem 1.6, pp. 275--277.
- Use: purity and the absolute-value bounds for Frobenius eigenvalues on
  the smooth cubic and complete intersection.
- Firewall: this source does not give a number-field Hasse--Weil functional
  equation for \(O_3\) or \(O_4\).

### Weak Lefschetz

- A. Grothendieck, with M. Raynaud, *Cohomologie locale des faisceaux
  cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, North
  Holland, 1968; revised Société Mathématique de France edition, 2005.
- Exact locator: Exposé XIV, Corollaire 4.6.
- Use: projective-space cohomology away from the middle degree for smooth
  complete intersections.
- Firewall: smoothness is an input and is not supplied by weak Lefschetz.

### Primitive cohomology of hypersurfaces

- P. A. Griffiths, “On the periods of certain rational integrals. II,”
  *Annals of Mathematics* **90** (1969), 496--541,
  DOI 10.2307/1970747.
- Exact locator: §10, especially Theorem 10.8, for the hypersurface
  residue/Jacobian-ring description of primitive Hodge pieces.
- Use: the primitive Hodge/Betti calculation for the Fermat cubic.
- Firewall: HCS-C51 independently evaluates the finite Hilbert series
  \((1+t)^{2n}\); it does not claim the Jacobian-ring method as new.

### \(\chi_y\), Chern classes, and Euler characteristic

- F. Hirzebruch, *Topological Methods in Algebraic Geometry*, third edition,
  second corrected printing, Springer, 1995,
  DOI 10.1007/978-3-642-62018-8.
- Exact locator: the chapters on the generalized Todd genus and
  Riemann--Roch; the released coefficient formula is expanded explicitly in
  DERIVATION_PACKAGE.md.
- Use: Hirzebruch--Riemann--Roch and the \(\chi_y\) characteristic series.
- Firewall: the polynomial
  \(1-82y^2+82y^3-y^5\) is independently obtained by finite expansion.

### Chebotarev and semisimple character identity

- J.-P. Serre, “Quelques applications du théorème de densité de
  Chebotarev,” *Publications Mathématiques de l'IHÉS* **54** (1981),
  123--201, DOI 10.1007/BF02698692.
- Exact locator: §2.1, Théorème 1, for Chebotarev density.  Equality of
  traces on the resulting dense Frobenius set is promoted to equality in
  the semisimple representation ring by the standard Brauer--Nesbitt
  character argument.
- Use: density-one Frobenius character comparison in the semisimple
  direct-\(K\) compatible-system obstruction.
- Firewall: the argument assumes the candidate retains the \(E_n/O_n\)
  weight decomposition and unchanged split-prime trace.  It does not apply
  unchanged after restriction of scalars or Galois-orbit reorganization.

## 3. Fermat/Jacobi refinement

- A. Weil, “Jacobi sums as ‘Grössencharaktere’,” *Transactions of the
  American Mathematical Society* **73** (1952), 487--495,
  DOI 10.1090/S0002-9947-1952-0051263-0.
- L. Brünjes, “On the zeta function of forms of Fermat equations,”
  arXiv:math/0301186.
- Exact Brünjes locators: Definition 4.4, Proposition 4.5, Theorem 4.6,
  and Example 4.7.
- Use: classical Jacobi-sum decomposition of Fermat cohomology and the
  interpretation of its one-dimensional packets by Hecke characters.
- Firewall: the \(n=3\) statement is twenty normalized Tate lines plus one
  rank-two non-Tate Jacobi packet inside \(E_3\), not a Tate decomposition
  of all \(H^4_{\mathrm{prim}}(S_3)\).

## 4. Functional-equation sources and limits

### Proved \(n=2\) factors

- A. Caraiani and J. Newton, “On the modularity of elliptic curves over
  imaginary quadratic fields,” arXiv:2301.10509, version 3 (2025),
  Theorem 1.1, p. 2.
- R. Godement and H. Jacquet, *Zeta Functions of Simple Algebras*,
  Lecture Notes in Mathematics **260**, Springer, 1972,
  DOI 10.1007/BFb0070263; “Global Theory,” pp. 136--184.
- Use: inherited modularity of the C50 elliptic factors over
  \(K=\mathbf Q(\sqrt{-3})\), followed by the standard automorphic
  continuation and functional equation.
- Firewall: Caraiani--Newton is used for elliptic curves, not the high-rank
  \(O_3\) or \(O_4\) systems.  Godement--Jacquet supplies the standard
  automorphic analytic package after modularity; it does not make an
  arbitrary geometric compatible system automorphic.

### Expected motivic centers and archimedean factors

- J.-P. Serre, “Facteurs locaux des fonctions zêta des variétés
  algébriques (définitions et conjectures),” *Séminaire
  Delange--Pisot--Poitou* **11** (1969--1970), Exposé 19, 1--15.
- Exact locators: §1.3 (pp. 3--4) for the conjectural global reflection
  \(s\mapsto m+1-s\); §§3.1--3.3 (pp. 9--11) for the Hodge-theoretic
  archimedean factors; and §4.1 (pp. 11--13) for completion and
  functional-equation data.
- P. Deligne, “Valeurs de fonctions \(L\) et périodes d'intégrales,”
  *Proceedings of Symposia in Pure Mathematics* **33**, part 2 (1979),
  313--346.
- Exact Deligne locators: §0.1(c,d) for the Tate object and weight
  bookkeeping; §1.2, equation (1.2.3), for the completed functional
  equation
  \(\Lambda(M,s)=\varepsilon(M,s)\Lambda(M^\vee,1-s)\);
  §3.1, equation (3.1.2), for the Tate shift
  \(L(M(n),s)=L(M,n+s)\); and §5.2 with Table 5.3 for the expected
  archimedean factors and functional-equation convention.
- Use: the standard local-factor convention, Tate-shift rule, pure-motive
  center, and expected Gamma ledger.
- Firewall: Serre and Deligne state the motivic analytic package
  conjecturally in the required generality.  They are not cited as theorems
  proving the Hasse--Weil functional equations of \(O_3\) or \(O_4\).

### Motivic versus unitary normalization

- P. Sarnak, S. W. Shin, and N. Templier, “Families of \(L\)-functions and
  their symmetry,” arXiv:1401.5507, normalization appendix, pp. 34--35.
- K. Buzzard and T. Gee, “The conjectural connections between automorphic
  representations and Galois representations,” arXiv:1009.0785;
  Introduction, §2.2, and §§3.4 and 5.3.
- Use: distinguish motivic from unitary normalization and record the
  \(C\)-algebraic/\(L\)-algebraic half-sum shift.
- Firewall: a half shift is legitimate in automorphic or \(C\)-group
  normalization.  It is not an ordinary half Tate motive and, when the
  Hénon clock is frozen, it cannot be applied while leaving local
  coefficients unchanged.  C51's invariance statement concerns a
  consistent simultaneous change of weight and \(L\)-variable.

### Infinite products and regularized Gamma factors

- J. R. Quine, S. H. Heydari, and R. Y. Song, “Zeta regularized products,”
  *Transactions of the American Mathematical Society* **338** (1993),
  213--231; opening definition.
- C. Deninger, “On the \(\Gamma\)-factors attached to motives,”
  *Inventiones Mathematicae* **104** (1991), 245--261.
- C. Deninger, “Local \(L\)-factors of motives and regularized
  determinants,” *Inventiones Mathematicae* **107** (1992), 135--150,
  DOI 10.1007/BF01231885.
- Use: prior art for expressing archimedean or local factors through
  zeta-regularized products/determinants.
- Firewall: an infinite product is not defined by a formal list of Hodge
  shifts alone.  A released construction would need a spectral zeta
  function with meromorphic continuation at the regularization point,
  together with branch and multiplicity data.  C51 constructs no such
  full Hénon Gamma determinant.

## 5. Operator-theoretic inheritance

- B. Simon, *Trace Ideals and Their Applications*, second edition,
  Mathematical Surveys and Monographs **120**, American Mathematical
  Society, 2005; Chapter 9.
- Use: background for regularized determinants inherited through C47--C50.
- Firewall: C51 proves no new Schatten theorem.  It inherits the
  normalized-semifinite \(\operatorname{Det}_{10}\) realization on
  \(\Re s>1/5\), which is not a classical Fredholm determinant.

## 6. Internal prior-work firewall

| Project | Already established | C51 does not duplicate | New C51 delta |
|---|---|---|---|
| C32 | finite-field Artin--Schreier/Hénon local gate | local Morse/Hill recovery | none |
| C43--C47 | full kernel, Galois normalization, branch obstruction, normalized-trace operator | local determinant and operator construction | source-weight completion audit |
| C48 | \(n=2\) genus-four trace and \(\Re s>1/3\) | second-moment geometry | common weight--clock comparison |
| C49 | \(n=3\) Fermat/Fano trace and \(\Re s>1/4\) | third-moment point-count theorem | uniform packet/rank formula |
| C50 | elliptic \(n=2\) resummation, \(n=4\) trace, \(\Re s>1/5\), \(\operatorname{Det}_{10}\) | continuation or operator threshold | center bifurcation, direct-system no-go, \(O_4\) projector gate |

The rank formulas, standard weight centers, Tate-twist rule, Jacobian-ring
method, Jacobi-sum decomposition, and \(\chi_y\) genus are classical.
HCS-C51 makes no novelty claim for them individually.

The proposed delta is the **source-locked synthesis**:

1. the exact Hénon normalization forces a uniform \(E_n/O_n\) two-weight
   trace with total rank \(4^n-1\);
2. the same normalization forces exponent \(2/n\) and the tower
   \(u=ns+j\);
3. those data prove a factorwise weight--clock bifurcation and a scoped
   direct-\(K\) rank obstruction;
4. the \(O_4\) Hodge ledger identifies one precise algebraic-projector gate.

## 7. External novelty neighbors

- Serre and Deligne already provide the standard conjectural language of
  motivic local factors, weights, Tate shifts, Gamma factors, and functional
  equations.
- Buzzard--Gee and the automorphic-normalization literature already explain
  half-sum shifts via \(C\)- and \(L\)-algebraicity.
- Deninger and Quine--Heydari--Song already connect Gamma/local factors with
  zeta-regularized determinants and infinite products.
- F. Heinloth, “A note on functional equations for zeta functions with
  values in Chow motives,” *Annales de l'Institut Fourier* **57** (2007),
  1927--1945, DOI 10.5802/aif.2318, Proposition 6.1, proves a product
  stability result in a Chow-motive \(\lambda\)-ring setting.
- Classical Selberg and Ruelle programs obtain dynamical completions when a
  trace formula or geometric spectral identity supplies the missing
  archimedean data.  C51 has no analogous trace formula.

A targeted search found no predecessor that starts from the same
field-degree-normalized chronological Hénon kernel and proves this precise
weight--clock bifurcation.  The search is non-exhaustive, so the paper
claims only the explicit source-locked delta above, not absolute priority.

## 8. Claims explicitly forbidden

The paper must not claim:

- source smoothness for all \(n\);
- a proved \(n=3\) or \(n=4\) Hasse--Weil functional equation;
- a full Hénon Gamma factor or functional equation;
- a common factorwise standard pure-motive center beyond the leading odd
  \(j=1\) rail;
- that a fractional \(\operatorname{Log}_0\) germ is a meromorphic root;
- a universal no-go for restriction of scalars, Galois counterpackets, or
  normalized-semifinite realizations;
- an algebraic \(O_4\) projector before it is constructed;
- a Riemann divisor or self-adjoint Hilbert--Pólya operator.

The numerical value \(s=0\) is not itself an obstruction to an RH-type
normalization.  The NIST Digital Library of Mathematical Functions,
§25.4, equations (25.4.3)--(25.4.4), gives
\(\xi(s)=\xi(1-s)\); after recentering
\(\Xi(z)=\xi(1/2+z)\), the center is \(z=0\), and RH is the corresponding
imaginary-axis statement (§25.10).  C51 obstructs **mismatched factorwise
centers under the frozen source clock**, not center zero.

## 9. Metadata verification note

The publisher/author records checked for this package agree on the following
metadata used in the bibliography:

- Griffiths II: *Annals of Mathematics* 90 (1969), 496--541,
  DOI 10.2307/1970747;
- Deligne, Weil I: *Publ. Math. IHÉS* 43 (1974), 273--308,
  DOI 10.1007/BF02684373;
- Hirzebruch: Springer DOI 10.1007/978-3-642-62018-8;
- Weil: *Trans. AMS* 73 (1952), 487--495,
  DOI 10.1090/S0002-9947-1952-0051263-0;
- Godement--Jacquet: LNM 260 (1972), Global Theory pp. 136--184,
  DOI 10.1007/BFb0070263;
- Simon: AMS Mathematical Surveys and Monographs 120 (2005), Chapter 9.
- Serre, Chebotarev: *Publ. Math. IHÉS* 54 (1981), 123--201,
  DOI 10.1007/BF02698692.
