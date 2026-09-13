# Paper 26 Publication Scope

## Status and authority

This artifact freezes the publication-facing scope for a possible future anonymous theory article. It resolves the minimum contextual bibliography against primary records and fixes the manuscript identity, theorem boundary, page architecture, citation uses, source universe, and source-author stop rules.

This artifact is not manuscript source and grants no authority to create or edit TeX, BibTeX, code, data, figures, assets, auxiliary files, a build tree, a PDF, or a release. It grants no authority to compile, compute, submit, upload, message, disclose an identity, create a successor artifact, or open a successor stage. Global claim-level novelty remains unresolved.

## Frozen public identity

- Exact title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth
- Visible author: Anonymous
- Visible date: empty
- PDF Title: exactly the title above
- PDF Author: empty
- PDF Creator: empty
- PDF Producer: empty
- PDF Subject: empty
- PDF Keywords: empty
- Article type: anonymous proof-first theory article
- Venue: unresolved; no venue-specific claim or formatting decision is frozen here

The public firewall applies to rendered text, source comments, bookmarks, links, metadata, attachments, filenames exposed through the PDF, and bibliography fields. The public manuscript may contain no personal identity, affiliation, acknowledgment, grant identifier, identity-bearing link, private or local path, hash, review result, gate language, workflow role, candidate identifier, project paper number, unpublished predecessor identifier, or repository datum. No internal collision label may appear publicly. The bibliography may contain only the canonical public records frozen below.

## Reader promise and contribution order

The article concerns one literal planar family: Hamiltonian product shears with arbitrary finite collected support in \(\mathbf Z_{\ge2}^{2}\), all collected coefficients nonzero over a characteristic-zero field, and a separated pure-power momentum Hamiltonian. Its proof-first center is the conjunction of cancellation-safe Newton-envelope exactness and one global projective contraction, not a claim of global priority.

The Introduction and Abstract preserve this order:

1. coefficient-uniform exposed-face Hessian certification and full-face algebraic independence;
2. cancellation-free forward and inverse half-step carries, visible ordinary-degree blocks, and the shifted vector bridge;
3. a support-uniform logarithmic contraction patched across every Newton wall;
4. the interior/wall selector classification and quadratic-versus-integral arithmetic consequences;
5. separately proved forward and inverse scalar-recurrence upper bounds.

Recurrences, two-step products, and the two exact fixtures are consequences. They do not replace or precede the first four mechanisms.

## Frozen theorem contract

### Hypotheses and notation

Let \(K\) have characteristic zero. Let \(E\subset\mathbf Z_{\ge2}^{2}\) be finite, nonempty, and collected. Every coefficient \(c_{x,y}\), \((x,y)\in E\), is nonzero; signs are arbitrary and no positivity or common-sign hypothesis is permitted. Define

\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y
\]

and

\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,\qquad\alpha\beta\ne0.
\]

With

\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),
\]

set \(F=T\circ S\). Degrees are ordinary total degrees in the four initial coordinates, and both forward and inverse degree seeds are \(\mathbf1=(1,1)^\top\).

For coordinatewise positive \(u\), define

\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),\qquad
\mathcal A(u)=\bigl(H(u)-u_1,H(u)-u_2\bigr)^\top,\qquad
B=\operatorname{diag}(e,f).
\]

### Dependency-ordered conclusions

The formal Main Theorem appears only after the full exposed-face Hessian and algebraic-independence proof in Section 3. Its conclusions occur in this order.

1. Structure and cancellation. The map \(F\) is a polynomial symplectomorphism, \(F^{-1}=S^{-1}\circ T^{-1}\), and every full exposed-face leading pair survives every forward and inverse half-step, including subtraction phases and arbitrary multi-point ties.
2. Exact vector transports and visible degrees. With \(u_0^+=v_0^-=\mathbf1\),
   \[
   u_{n+1}^+=B\mathcal A(u_n^+),\qquad
   v_{n+1}^-=\mathcal A(Bv_n^-),
   \]
   and
   \[
   \deg(F^n)=\lVert u_n^+\rVert_\infty,\qquad
   \deg(F^{-n})=\lVert v_n^-\rVert_\infty.
   \]
3. Shifted vector bridge. With \(c_\star=H(\mathbf1)-1\),
   \[
   u_{n+1}^+=c_\star Bv_n^-\qquad(n\ge0).
   \]
   This yields two-sided constant-factor comparison after one index shift and equality \(\lambda_1(F)=\lambda_1(F^{-1})\). It yields neither termwise equality of the two scalar degree sequences nor transfer of a forward scalar recurrence to the inverse sequence.
4. Uniform projective contraction. The forward ratio map has one global contraction constant strictly below one in logarithmic distance after all chamber and wall patches. The inverse ratio map is its scaling conjugate. Each map has one fixed ray and no nontrivial numerical periodic orbit.
5. Selector and arithmetic classification. An interior fixed ray gives an eventually stationary selector. A wall fixed ray gives the full tied face on the fixed orbit; every strict orbit alternates between adjacent selector chambers while its ratios converge to the single wall ray. Interior values have algebraic degree at most two, wall values are positive integers, and
   \[
   [\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
   \]
6. Scalar recurrence consequences. Forward and inverse interior degree tails have order at most two, strict wall-alternating tails have order at most four, and fixed-ray tails are geometric. The inverse result is derived independently from \(D_\xi\), selection at the Newton coordinate \(\kappa s\), both \(s_\star=1\) and \(s_\star\ne1\), stable visible coordinates, and both parity products.

The proof dependency is one-way: full-face cancellation precedes exact carries; exact forward transport precedes projective contraction; contraction precedes selector classification; classification precedes spectral arithmetic; and Cayley–Hamilton recurrence consequences come last. A fixture proves no general step, the bridge proves no inverse scalar recurrence, and a two-step matrix product proves no global contraction.

## Scope exclusions and anti-claims

The manuscript makes no theorem, implication, or suggestive extension for any of the following:

- support on a coordinate axis or an exponent equal to one;
- zero coefficients, duplicate or uncollected support, or a support list different from the actual collected polynomial;
- mixed terms in \(W\), a nonseparated momentum Hamiltonian, or arbitrary Hamiltonian shears;
- positive characteristic;
- dimension at least three;
- altered phase order, a different ordinary seed, or an arbitrary bridge seed;
- termwise equality of forward and inverse degree sequences;
- transfer of scalar recurrences through the vector bridge;
- a nontrivial numerical two-cycle or any other nontrivial numerical periodic orbit;
- recurrence minimality;
- higher dynamical degrees;
- entropy conclusions beyond contextual discussion of the cited literature;
- compactification;
- integrability or nonintegrability;
- periodic, Diophantine, or other arithmetic conclusions for point orbits;
- classification or nonconjugacy of polynomial symplectomorphisms;
- genericity as a substitute for the coefficient-uniform proof;
- support optimality, support-rank novelty, or global quadratic sharpness for all Hamiltonian shears;
- exhaustive literature coverage, global novelty, priority, firstness, uniqueness, or an assertion that no related theorem exists.

Each boundary is stated next to the theorem step it limits and is collected again in Section 8. Selector-label alternation is always distinguished from a numerical two-cycle: the numerical ratios converge to one wall ray.

## Private collision boundary and required public subtraction

The nearest special two-term predecessor owns its two-term wall criterion, forced selector period two, two-step monodromy and parity mechanics, and interleaved-recurrence framing. This article may use two-step products only as late consequences. Its distinct center is arbitrary finite planar support, full tied-face cancellation, one global logarithmic contraction, exclusion of nontrivial numerical cycles, exact inverse transport, and a common-wall-ray integer multiplier.

The nearest support-rank predecessor owns support-rank bounds, stationary sharp constructions, unbounded higher-dimensional Perron degree, and scalar minimality. This article is a narrower planar rigidity result. It makes no support-rank contribution, no scalar-minimality claim, and no suggestion that the planar quadratic cap contradicts a higher-dimensional result.

The public manuscript expresses those distinctions only as assumption-and-mechanism boundaries. It never names a project number, unpublished local paper, internal title, review, or collision record.

## Exact page and section architecture

The body from front matter through the end of Section 9 is designed at exactly 26.0 pages; references begin afterward and are excluded. The acceptable later rendered range is 22–30 body pages. There is no appendix, supplement, empirical section, or theorem-critical material outside the numbered body.

1. Front matter and Abstract — 0.75 page: title/anonymous empty-date matter 0.10; Abstract 0.65.
2. Section 1, Introduction, local related work, and contributions — 2.25 pages: 1.1 degree growth as an exact polynomial problem 0.45; 1.2 three coupled obstacles 0.45; 1.3 local related-work synthesis 0.70; 1.4 contributions and proof roadmap 0.65.
3. Section 2, Setting, symplecticity, and inverse phases — 1.50 pages: 2.1 map class, collected support, and ordinary degree 0.45; 2.2 symplectic block calculation 0.35; 2.3 subtraction inverses and phase chronology 0.30; 2.4 support function and theorem staging 0.40.
4. Section 3, Full exposed-face Hessian and cancellation — 3.00 pages: 3.1 positive exposed support and full face polynomial 0.30; 3.2 unique minimal first coordinate 0.35; 3.3 isolated face-Hessian coefficient 0.75; 3.4 Jacobian independence 0.40; 3.5 injective substitution and pure-power survival 0.65; 3.6 dependency-ordered Main Theorem 0.55.
5. Section 4, Exact forward/inverse transports and bridge — 4.25 pages: 4.1 weighted gradient transform 0.45; 4.2 lower carry inequalities 0.35; 4.3 cross-coordinate upper carry 0.40; 4.4 forward half-step induction 0.75; 4.5 inverse half-step induction 0.85; 4.6 exact vector states and total degrees 0.45; 4.7 shifted bridge induction 0.55; 4.8 norm comparison and exact boundary 0.45.
6. Section 5, Uniform logarithmic contraction — 3.75 pages: 5.1 projective support function and ratio map 0.45; 5.2 chamber derivative and monotonicity 0.45; 5.3 logarithmic derivative and positive gap 0.65; 5.4 endpoint compactification for one branch 0.55; 5.5 finite-support uniformity 0.35; 5.6 wall patching 0.55; 5.7 inverse map and scaled selector 0.40; 5.8 fixed point and numerical-cycle exclusion 0.35.
7. Section 6, Selector and spectral rigidity — 3.50 pages: 6.1 interior fixed ray 0.45; 6.2 wall fixed and strict trajectories 0.85; 6.3 selector alternation is not a numerical two-cycle 0.30; 6.4 interior selector matrix and spectrum 0.55; 6.5 primitive wall ray and common multiplier 0.75; 6.6 integrality and per-step growth 0.40; 6.7 Structural Table 1 0.20.
8. Section 7, Forward and inverse scalar recurrences — 4.00 pages: 7.1 state-matrix and visibility notation 0.45; 7.2 forward interior tail 0.55; 7.3 forward fixed-wall and strict-wall tails 0.55; 7.4 inverse chamber matrices 0.65; 7.5 inverse interior cases 0.45; 7.6 inverse fixed-wall and strict-wall cases 0.65; 7.7 common coefficients, parity visibility, and indices 0.50; 7.8 consequence and boundary 0.20.
9. Section 8, Exact fixtures, scope, and collision subtraction — 2.50 pages: 8.1 quadratic interior fixture 0.65; 8.2 transient-to-fixed-wall fixture 0.90; 8.3 failure modes tied to assumptions 0.40; 8.4 local collision subtraction in public mechanism language 0.30; 8.5 remaining anti-claims 0.25.
10. Section 9, Conclusion — 0.50 page: 9.1 theorem in one chain 0.35; 9.2 open verification, not new mathematics 0.15.

The exact arithmetic is

\[
0.75+2.25+1.50+3.00+4.25+3.75+3.50+4.00+2.50+0.50=26.00.
\]

The technical core remains

\[
\S4+\S5+\S6+\S7=4.25+3.75+3.50+4.00=15.50
\]

pages. A later PDF check may measure pagination but may not change the theorem, hide proof mass, or use font, margin, spacing, display, or forced-break tricks to hit the range.

## Figure, asset, table, and fixture contract

The manuscript contains exactly zero figures and zero assets. There is no figure directory, raster or vector image, diagram, plot, data file, generated visual, contact sheet, or externally generated table.

The manuscript contains exactly one table: hand-typeset Structural Table 1 in Section 6.7. It has exactly three columns, in this order: Mechanism; Consequence; Boundary. It has exactly five qualitative body rows:

1. full-face Hessian certificate; cancellation-safe leading pair; axes, zero or uncollected coefficients, and positive characteristic;
2. strict carries plus separated powers; exact visible forward and inverse degrees; exponent one or mixed \(W\);
3. finite-envelope logarithmic contraction; unique ray and selector dichotomy; infinite support, mixed \(W\), or higher projective dimension;
4. interior matrix or common primitive wall ray; quadratic-at-most versus integral spectrum; no extension to all Hamiltonian shears or higher dynamical degrees;
5. stable visible coordinate plus Cayley–Hamilton; recurrence upper bounds; no minimality and no scalar transfer from the bridge.

The table contains no numerical result, benchmark, score, page budget, literature survey, claims matrix, fixture values, or notation list. No second table is permitted.

The two examples are exact hand-checkable proof fixtures, not experiments, numerical evidence, CAS output, benchmarks, or datasets:

- Interior fixture: \(E=\{(2,2)\}\), \(B=\operatorname{diag}(3,2)\), \(C=\begin{pmatrix}3&6\\4&2\end{pmatrix}\), characteristic polynomial \(t^2-5t-18\), value \((5+\sqrt{97})/2\), and bridge check \(u_1^+=(9,6)\), \(v_1^-=(7,8)\), \(u_2^+=(63,48)=3Bv_1^-\).
- Wall fixture: \(E=\{(2,8),(4,5),(5,3)\}\), \(B=\operatorname{diag}(24,11)\), walls \(3/2\) and \(2\), ratios \(r_1=24/11\), \(r_2=1548/781\), \(r_3=51294/25619\), common wall direction \((2,1)^\top\), multiplier \(132\), monodromy trace \(17648\), determinant \(3902976\), and eigenvalues \(17424,224\). This is selector alternation converging to \(r=2\), never a numerical two-cycle.

## Primary-record bibliography audit

### Evidence rule

All records below were checked on 2026-08-26. Metadata and claim fit were checked only against official publisher or journal records, DOI landing records, and official arXiv records. Search-result pages and snippets were discovery aids only and are not evidence. No secondary aggregator supplies a field or a claim-fit decision. The URL lists below are exact direct records consulted.

The final bibliography is deliberately minimal: seven admitted and used journal articles. For the published articles, the canonical BibTeX freezes only author, title, journal, year, volume, issue where one exists, pages or article number, and DOI. It contains no URL, access-date, local path, review datum, note, speculative field, unused arXiv duplicate, or identity-bearing field.

### Admitted record 1

- Authors: M. P. Bellon; C.-M. Viallet. The consulted primary records expose initials; the bibliography does not speculate about expanded given names.
- Title: Algebraic Entropy
- Journal: Communications in Mathematical Physics
- Year, volume, issue, pages: 1999; 204; 2; 425–437
- DOI: 10.1007/s002200050652
- Status: published journal article; issue date July 1999
- Final key: BellonViallet1999AlgebraicEntropy
- Claim fit: degree-growth and algebraic-entropy motivation only
- Direct records:
  - https://link.springer.com/article/10.1007/s002200050652
  - https://link.springer.com/journal/220/volumes-and-issues/204-2
  - https://doi.org/10.1007/s002200050652
  - https://arxiv.org/abs/chao-dyn/9805006

### Admitted record 2

- Authors: Nguyen-Bac Dang; Charles Favre
- Title: Spectral interpretations of dynamical degrees and applications
- Journal: Annals of Mathematics
- Year, volume, issue, pages: 2021; 194; 1; 299–359
- DOI: 10.4007/annals.2021.194.1.5
- Status: published journal article; published online 23 June 2021
- Final key: DangFavre2021SpectralInterpretations
- Claim fit: general spectral interpretation of dynamical degrees only; none of its operator machinery is asserted to prove this article
- Direct records:
  - https://annals.math.princeton.edu/2021/194-1/p05
  - https://doi.org/10.4007/annals.2021.194.1.5

### Admitted record 3

- Authors: Allan P. Fordy; Andrew Hone
- Title: Symplectic Maps from Cluster Algebras
- Journal: Symmetry, Integrability and Geometry: Methods and Applications
- Year, volume, article, length: 2011; 7; 091; 12 pages
- Issue: none
- DOI: 10.3842/SIGMA.2011.091
- Status: published refereed journal article; published online 22 September 2011
- Final key: FordyHone2011SymplecticMaps
- Claim fit: a separate cluster-map setting where invariant symplectic structure and tropical degree recurrences coexist; no integrability inference
- Direct records:
  - https://sigma-journal.com/2011/091/
  - https://sigma-journal.com/2011/091/sigma11-091.pdf
  - https://doi.org/10.3842/SIGMA.2011.091
  - https://arxiv.org/abs/1105.2985

### Admitted record 4

- Authors: Tsukasa Ishibashi; Shunsuke Kano
- Title: Algebraic entropy of sign-stable mutation loops
- Journal: Geometriae Dedicata
- Year, volume, issue, pages: 2021; 214; 1; 79–118
- DOI: 10.1007/s10711-021-00606-1
- Status: published Original Paper; version of record 9 February 2021 and assigned to the October 2021 issue
- Final key: IshibashiKano2021AlgebraicEntropy
- Claim fit: stable tropical sign data in mutation loops only; no transfer of a mutation-loop theorem to the present Newton selector
- Direct records:
  - https://link.springer.com/article/10.1007/s10711-021-00606-1
  - https://link.springer.com/journal/10711/volumes-and-issues/214-1
  - https://doi.org/10.1007/s10711-021-00606-1

### Admitted record 5

- Authors: Stanisław Janeczko; Zbigniew Jelonek
- Title: Polynomial symplectomorphisms
- Journal: Bulletin of the London Mathematical Society
- Year, volume, issue, pages: 2008; 40; 1; 108–116
- DOI: 10.1112/blms/bdm112
- Status: published journal article; published 5 February 2008
- Final key: JaneczkoJelonek2008PolynomialSymplectomorphisms
- Claim fit: family-level polynomial-symplectomorphism background only; no classification or exact degree formula for the present family
- Direct records:
  - https://academic.oup.com/blms/article/40/1/108/282016
  - https://academic.oup.com/blms/article-pdf/40/1/108/790484/bdm112.pdf
  - https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/blms/bdm112
  - https://doi.org/10.1112/blms/bdm112

### Admitted record 6

- Authors: Pierre Berger; Dmitry Turaev
- Title: Generators of groups of Hamiltonian maps
- Journal: Israel Journal of Mathematics
- Year, volume, issue, pages: 2025; 267; 1; 237–252
- DOI: 10.1007/s11856-024-2709-7
- arXiv record: 2210.14710
- Status: published Original Paper; version of record 18 December 2024 and assigned to the June 2025 issue. The published 2025 record supersedes the arXiv record’s misspelled title and absent journal reference.
- Final key: BergerTuraev2025GeneratorsHamiltonianMaps
- Claim fit: structural context for position-only and momentum-only nonlinear shear generators; no exact polynomial Newton-support, transport, contraction, or degree result is attributed to it
- Direct records:
  - https://link.springer.com/article/10.1007/s11856-024-2709-7
  - https://link.springer.com/journal/11856/volumes-and-issues/267-1
  - https://doi.org/10.1007/s11856-024-2709-7
  - https://arxiv.org/abs/2210.14710

### Admitted record 7

- Authors: Jérémy Blanc; Immanuel van Santen
- Title: Dynamical degrees of affine-triangular automorphisms of affine spaces
- Journal: Ergodic Theory and Dynamical Systems
- Year, volume, issue, pages: 2022; 42; 12; 3551–3592
- DOI: 10.1017/etds.2021.90
- arXiv record: 1912.01324
- Status: published Original Article; online 1 October 2021 and assigned to the December 2022 issue. The bibliographic year is 2022.
- Final key: BlancVanSanten2022DynamicalDegrees
- Claim fit: adjacent affine-triangular dynamical-degree comparison only; the present family is not asserted to lie in that class
- Direct records:
  - https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dynamical-degrees-of-affinetriangular-automorphisms-of-affine-spaces/AC289A185EFECC01805D09B2ED113D7D
  - https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/issue/DA90CB7B3CB3AAF7DE5F81D7AE458F7E
  - https://doi.org/10.1017/etds.2021.90
  - https://arxiv.org/abs/1912.01324

### Withheld record: redundant cluster-map article

- Authors: Allan P. Fordy; Andrew Hone
- Title: Discrete Integrable Systems and Poisson Algebras From Cluster Maps
- Journal: Communications in Mathematical Physics
- Year, volume, issue, pages: 2014; 325; 2; 527–584
- DOI: 10.1007/s00220-013-1867-y
- Status: published journal article; online 17 December 2013 and assigned to the January 2014 issue
- Direct records:
  - https://link.springer.com/article/10.1007/s00220-013-1867-y
  - https://link.springer.com/journal/220/volumes-and-issues/325-2
  - https://doi.org/10.1007/s00220-013-1867-y
  - https://arxiv.org/abs/1207.6072
- Decision: metadata and narrow contextual fit are complete, but the record is withheld from the minimal manifest because the admitted 2011 SIGMA article already supplies the needed cluster symplectic/tropical context. A second Fordy–Hone entry would be redundant and would increase the risk of an unsupported integrability inference. It receives no final-manifest key and may not enter the future bibliography.

### Excluded record: specialized straight-line Hamiltonian flows

- Authors: Hans Koch; Héctor E. Lomelí
- Title: On Hamiltonian flows whose orbits are straight lines
- Journal: Discrete and Continuous Dynamical Systems
- Year, volume, issue, pages: 2014; 34; 5; 2091–2104
- DOI: 10.3934/dcds.2014.34.2091
- arXiv record: 1304.3377
- Status: published journal article; online October 2013 and assigned to the 2014 volume
- Direct records:
  - https://www.aimsciences.org/article/doi/10.3934/dcds.2014.34.2091
  - https://doi.org/10.3934/dcds.2014.34.2091
  - https://arxiv.org/abs/1304.3377
- Decision: primary metadata is now complete, but claim fit is not. The paper concerns the specialized class of affine-integrable Hamiltonian flows with straight-line orbits, cubic reduction, and higher-degree conjugacy obstructions. The current manuscript makes no matching straight-line or affine-integrable-flow claim, and Berger–Turaev already supplies the narrower useful shear-generator context. The record remains excluded, receives no key, and may not enter the future bibliography.

## Exact citation slots and sentence purposes

Every admitted entry is cited exactly once, only in the slot below. These sentences are frozen in purpose; prose may be grammatically integrated without broadening the claim. None is a proof premise. The Abstract and Sections 2–9 contain no contextual citation.

1. Section 1.1, slot S1.1-D1, key BellonViallet1999AlgebraicEntropy: “Algebraic entropy packages the degree growth of iterates as a complexity invariant for rational dynamics.” Purpose: degree-growth motivation only.
2. Section 1.1, slot S1.1-D2, key DangFavre2021SpectralInterpretations: “In broader birational dynamics, dynamical degrees also admit spectral interpretations.” Purpose: general spectral context only.
3. Section 1.3, slot S1.3-T1, key FordyHone2011SymplecticMaps: “Cluster-generated maps provide a separate setting in which invariant symplectic structures and tropical degree recurrences coexist.” Purpose: symplectic/tropical recurrence context; no integrability inference.
4. Section 1.3, slot S1.3-T2, key IshibashiKano2021AlgebraicEntropy: “For mutation loops, stable tropical sign data can control algebraic entropy.” Purpose: conceptual comparison only; no theorem transfer.
5. Section 1.3, slot S1.3-S1, key JaneczkoJelonek2008PolynomialSymplectomorphisms: “The literature on polynomial symplectomorphisms supplies family-level structural background for the ambient map class.” Purpose: background only; no classification.
6. Section 1.3, slot S1.3-S2, key BergerTuraev2025GeneratorsHamiltonianMaps: “Hamiltonian dynamics may be approximated by compositions of nonlinear shears depending only on position or only on momentum.” Purpose: shear-generator context only.
7. Section 1.3, slot S1.3-A1, key BlancVanSanten2022DynamicalDegrees: “Affine-triangular automorphisms form an adjacent structured class in which dynamical degrees obey arithmetic restrictions.” Purpose: adjacent comparison only; no inclusion of the present family.

No citation appears in a theorem statement, proof step, fixture, collision subtraction, or Conclusion. No citation is used for the Jacobian criterion, contraction theorem, Perron–Frobenius, Cayley–Hamilton, rational algebraic integers, cyclic trace, or a private predecessor. The manuscript proves every theorem-critical step internally. No bibliography entry may be uncited or cited outside its frozen slot.

## Final canonical BibTeX manifest

The future references.bib, if separately authorized, contains exactly the following seven entries and no others. Field names, keys, Unicode, capitalization, years, volume and issue data, pagination or article number, and DOI values are frozen.

    @article{BellonViallet1999AlgebraicEntropy,
      author  = {Bellon, M. P. and Viallet, C.-M.},
      title   = {Algebraic Entropy},
      journal = {Communications in Mathematical Physics},
      year    = {1999},
      volume  = {204},
      number  = {2},
      pages   = {425--437},
      doi     = {10.1007/s002200050652}
    }

    @article{DangFavre2021SpectralInterpretations,
      author  = {Dang, Nguyen-Bac and Favre, Charles},
      title   = {Spectral interpretations of dynamical degrees and applications},
      journal = {Annals of Mathematics},
      year    = {2021},
      volume  = {194},
      number  = {1},
      pages   = {299--359},
      doi     = {10.4007/annals.2021.194.1.5}
    }

    @article{FordyHone2011SymplecticMaps,
      author  = {Fordy, Allan P. and Hone, Andrew},
      title   = {Symplectic Maps from Cluster Algebras},
      journal = {Symmetry, Integrability and Geometry: Methods and Applications},
      year    = {2011},
      volume  = {7},
      pages   = {091},
      doi     = {10.3842/SIGMA.2011.091}
    }

    @article{IshibashiKano2021AlgebraicEntropy,
      author  = {Ishibashi, Tsukasa and Kano, Shunsuke},
      title   = {Algebraic entropy of sign-stable mutation loops},
      journal = {Geometriae Dedicata},
      year    = {2021},
      volume  = {214},
      number  = {1},
      pages   = {79--118},
      doi     = {10.1007/s10711-021-00606-1}
    }

    @article{JaneczkoJelonek2008PolynomialSymplectomorphisms,
      author  = {Janeczko, Stanisław and Jelonek, Zbigniew},
      title   = {Polynomial symplectomorphisms},
      journal = {Bulletin of the London Mathematical Society},
      year    = {2008},
      volume  = {40},
      number  = {1},
      pages   = {108--116},
      doi     = {10.1112/blms/bdm112}
    }

    @article{BergerTuraev2025GeneratorsHamiltonianMaps,
      author  = {Berger, Pierre and Turaev, Dmitry},
      title   = {Generators of groups of {Hamiltonian} maps},
      journal = {Israel Journal of Mathematics},
      year    = {2025},
      volume  = {267},
      number  = {1},
      pages   = {237--252},
      doi     = {10.1007/s11856-024-2709-7}
    }

    @article{BlancVanSanten2022DynamicalDegrees,
      author  = {Blanc, Jérémy and van Santen, Immanuel},
      title   = {Dynamical degrees of affine-triangular automorphisms of affine spaces},
      journal = {Ergodic Theory and Dynamical Systems},
      year    = {2022},
      volume  = {42},
      number  = {12},
      pages   = {3551--3592},
      doi     = {10.1017/etds.2021.90}
    }

The SIGMA article has no issue and uses article number 091 in the plain-BibTeX pages field. The scope record, rather than a speculative BibTeX field, records its 12-page length. The published Berger–Turaev version controls the corrected title and 2025 bibliographic year. The Cambridge issue controls the Blanc–van Santen 2022 bibliographic year.

## Future exact source universe

A later parent authorization may jointly permit exactly three regular UTF-8 text files and no other manuscript source:

1. paper/main.tex: the exact title and public metadata; Abstract and exactly Sections 1–9 in the frozen order; every theorem statement and proof; both hand fixtures; the sole hand-typeset three-column, five-row table; and the bibliography call. It may input only math_commands.tex and use only references.bib. It contains no appendix, figure, external source, local path, code, generated text, hidden identity, or hidden metadata.
2. paper/math_commands.tex: notation and formatting macros only. It contains no prose, theorem, proof, citation, bibliography data, file I/O, executable behavior, identity, external input, or hidden source.
3. paper/references.bib: exactly the seven canonical entries above, each used exactly once in its frozen contextual slot. It contains no unused entry, alternate identifier field, URL, access date, local path, internal predecessor, review record, speculative metadata, or Koch–Lomelí or withheld Fordy–Hone entry.

No section file, class or style file, figure file, asset, data file, code, notebook, script, generated table, auxiliary source, alternate bibliography database, build file, or temporary file belongs to the source universe.

This scope does not itself authorize creation of any member of the trio.

## Future source-author acceptance criteria

A future source author may report successful source authoring only when every condition below is true.

- The exact title, Anonymous visible author, and empty visible date are reproduced without drift.
- PDF Title is exact and PDF Author, Creator, Producer, Subject, and Keywords are demonstrably empty.
- The public firewall holds in rendered content, comments, bookmarks, links, metadata, attachments, filenames, and bibliography.
- The source universe is exactly main.tex, math_commands.tex, and references.bib with the roles above and no other source.
- The body is Abstract plus exactly Sections 1–9, with no appendix or supplement.
- The design ledger is exactly 26.0 pages excluding references, Sections 4–7 retain exactly 15.5 pages, and the later rendered body lies within 22–30 pages without a formatting trick.
- There are exactly zero figures/assets and exactly one hand-typeset qualitative table with the frozen three columns and five rows.
- The full-face Hessian coefficient, algebraic independence, and multi-point tied-face survival are proved before any exact degree transport is claimed.
- The Main Theorem contains every frozen hypothesis and conclusion in dependency order.
- Both forward and both inverse half-step carries are explicit; inverse phase order, subtraction signs, visible blocks, and ordinary total degrees are correct.
- The bridge contains \(c_\star\), \(B\), the one-step shift, and the ordinary seed, and is never promoted to scalar equality or an inverse recurrence proof.
- The global logarithmic contraction includes its branch derivative, positive gap, endpoint control, finite-support maximum, and continuous wall patching.
- The inverse selector is evaluated at \(\kappa s\); wall fixed and strict trajectories, multiple ties, no delayed landing, and numerical-cycle exclusion are explicit.
- Interior quadratic and wall primitive-ray integral conclusions are proved without claiming a broader Hamiltonian result.
- Forward and inverse recurrence arguments remain separate and include \(D_\xi\), both \(s_\star\) cases, fixed and strict walls, both parity products, visible-coordinate stabilization, correct indices, and upper-bound rather than minimality language.
- Both fixtures reproduce every frozen rational and integer exactly and are described only as hand calculations.
- The seven admitted references match the canonical manifest byte-for-byte in substantive fields, are each cited exactly once in the frozen contextual slot, and no other entry or citation appears.
- Every anti-claim and both collision subtractions are present in public mechanism language, with no internal identifier.
- Global claim-level novelty is still described as unresolved; no firstness, exhaustiveness, or global noncollision claim appears.

Successful source authoring means only that the three source texts satisfy this scope. It does not itself authorize or imply compilation, a build tree, PDF creation, release, submission, or any external effect.

## Mandatory source-author stop criteria

The future source stage stops with zero source write, or removes any incomplete unaccepted source within that stage’s own separately granted authority, rather than inventing a repair, if any of the following occurs:

1. an in-scope exposed face can have a zero Hessian determinant, a tied leading form can cancel, or algebraic independence is only generic or assumed;
2. any forward or inverse carry, visible-block comparison, phase order, bridge factor, bridge shift, or base case fails;
3. no single contraction constant strictly below one closes all finite support branches and walls;
4. a selector tail lies outside interior stationarity, fixed-wall behavior, or adjacent-wall alternation converging to one ray;
5. a numerical cycle, nonintegral wall multiplier, or algebraic degree above two appears in scope;
6. the inverse recurrence would have to be inferred from the bridge, use \(C_\xi\) instead of \(D_\xi\), select by \(s\) rather than \(\kappa s\), omit a seed case, reverse a parity product, or skip visibility stabilization;
7. recurrence minimality or any forbidden anti-claim is needed;
8. either fixture fails exact hand reconstruction;
9. an admitted primary record, canonical field, exact citation sentence, or claim fit cannot be maintained;
10. an extra citation, source file, appendix, supplement, second table, figure, asset, computation, generated source, or formatting manipulation is needed;
11. the public firewall or any anonymous and empty-metadata requirement cannot be satisfied;
12. a primary source is found to prove the same complete arbitrary-support, wall-safe, bidirectional contraction theorem and the article’s claim center cannot be narrowed without changing the frozen theorem;
13. a special two-term wall/monodromy headline or a support-rank, higher-dimensional unbounded-degree, or scalar-minimality headline would have to be repackaged as this article’s contribution.

Any needed mathematical, bibliographic, identity, architecture, or source-universe change returns to the parent for a new scope decision. The source author may not silently widen the theorem, weaken a proof obligation, add a reference, add a source, or open a successor.

## Final authority boundary

This publication scope freezes a seven-entry contextual bibliography and a possible future three-file source design. It creates no TeX or BibTeX source, no code or data, no figure or asset, no computation or scientific result, no compilation or build root, no PDF, no release or submission, no external message or account action, and no successor authority.

PAPER26_PUBLICATION_SCOPE_AUTHOR_STOP
