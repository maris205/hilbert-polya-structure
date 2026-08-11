# HCS-C29 Phase-2 annotated bibliography

Search date: **2026-08-11 (UTC)**  
Phase: **2 -- Investigation / bibliography only**  
External sources included: **18**

This document is a retrieval and annotation artifact.  It does not synthesize
the literature into a theorem, assess Route A, or draft manuscript prose.

## 1. Reproducible search strategy

### 1.1 Research frame

The search was restricted to sources that can verify the external framework
around the following HCS-C29 components:

1. natural extensions and group extensions of symbolic systems;
2. Ihara--Hashimoto non-backtracking zeta and determinant identities;
3. representation-twisted or matrix-weighted graph zeta functions;
4. von Neumann/group traces and trace determinants;
5. finite Weil representations and their characters;
6. Rauzy--Veech induction, Zorich acceleration and the AGY coding/roof.

The search did **not** ask the literature to verify the frozen C25/C26 matrix
relations.  Those are repository computations and are separated in Section 4.

### 1.2 Search surfaces

- DOI resolver: `https://doi.org/`
- official publisher/article pages: Springer Nature, Elsevier/ScienceDirect,
  Taylor & Francis, Oxford Academic, AIMS, World Scientific and AMS
- official or discipline archives: Numdam, Annals of Mathematics,
  IMPAN/Acta Arithmetica and arXiv
- Semantic Scholar Graph API, attempted only as an additional deduplication and
  existence check; the batch request returned HTTP 429 and was not treated as
  negative evidence

### 1.3 Query families

The following query families were run in English, with exact-title and DOI
lookups added after candidate identification:

```text
"group extension" AND (subshift OR "countable Markov shift")
  AND (periodic OR cocycle OR "two-sided")

(Ihara OR Hashimoto OR "non-backtracking")
  AND (determinant OR "Artin L-function" OR "matrix-weighted")

("von Neumann" OR groupoid OR trace)
  AND (Ihara OR zeta OR determinant)

"Weil representation" AND ("finite field" OR character)
  AND symplectic

(Rauzy OR "Rauzy--Veech" OR Zorich OR AGY)
  AND (induction OR cocycle OR "Teichmüller flow")
```

Domain-restricted variants used `site:link.springer.com`,
`site:sciencedirect.com`, `site:academic.oup.com`, `site:numdam.org`,
`site:annals.math.princeton.edu`, `site:impan.pl`, and `site:arxiv.org`.

### 1.4 Search limits and eligibility

- **Date range:** no lower bound through 2026-08-11.  Seminal mathematical
  sources were deliberately retained regardless of age.
- **Languages:** English and French.
- **Included:** original peer-reviewed mathematical papers or chapters;
  official corrections; authoritative author/preprint copies only when useful
  for version comparison; sources whose hypotheses or construction directly
  delimit a C29 claim.
- **Excluded:** surveys when an original theorem was available; tertiary pages;
  ResearchGate or similar mirrors as the verification endpoint; duplicate
  preprint/published versions; sources addressing only a remote graph-zeta
  variant; any claimed application to the countable AGY operator whose
  hypotheses were not established.

### 1.5 Screening flow

This is a targeted mathematical source audit, not a PRISMA systematic review.
Search-engine hit totals are unstable, so the counts below refer to manually
captured candidate records only.

```text
Candidate records captured from query results:       27
Duplicate/preprint-published records removed:          5
Unique records screened by title/abstract/metadata:   22
Full records excluded after scope check:               4
External sources included and DOI-verified:           18
```

The four scope exclusions were valid publications but either duplicated a more
direct foundational theorem or addressed an infinite/weighted graph class not
used by the current finite C29 determinant germ.

### 1.6 Distributional coverage advisory

`DISTRIBUTIONAL_SKEW_ADVISORY`

- **Time:** 15/18 included sources (83.3%) were published in 2014 or earlier.
  This is expected because the audited claims are foundational theorem and
  definition claims.  A 2024 correction to Dougall--Sharp was included to
  guard currency and integrity.
- **Method:** 18/18 sources are theoretical mathematics.  This is appropriate
  to the research question and is not a missing empirical-method stratum.
- **Venue:** no single journal or publisher family reaches the 70% threshold.
- **Geography:** not assessed; study-site geography is not a meaningful
  metadata dimension for these theorem claims.

## 2. Evidence notation

The generic intervention-study hierarchy is not meaningful for theorem
sources.  The following claim-fitness scale is used instead:

- **M1-direct / Grade A:** original, peer-reviewed proof or construction that
  directly supports the cited mathematical claim.
- **M1-framework / Grade A:** original, peer-reviewed foundational framework;
  direct for the general theorem but not automatically applicable to C29.
- **M2-integrity / Grade A:** official correction or version-control source.
- **M2-adjacent / Grade B:** rigorous primary result whose hypotheses or object
  only partially overlap the proposed C29 object.

Every source below was verified through its DOI and an official publisher or
archive page.  Detailed verification, conflicts, venue screening and currency
status are recorded in `PHASE2_SOURCE_VERIFICATION.md`.

**Verification-depth disclosure:** no local full-text corpus was acquired for
this Phase-2 pass.  For all 18 entries,
`source_verified_against_original_full_text = false`; the annotations are based
on DOI metadata, official abstracts/article descriptions and authoritative
archive records.  They identify claim fitness for source selection but are not
theorem-by-theorem full-text audits.  A later paper may quote a theorem only
after checking the original text and recording a theorem/page locator.

## 3. Annotated bibliography

### Theme A -- natural extensions and group extensions

1. **Dougall, R., & Sharp, R. (2021). Anosov flows, growth rates on covers and group extensions of subshifts. *Inventiones Mathematicae, 223*, 445--483. https://doi.org/10.1007/s00222-020-00994-3**

   - **Use in C29:** primary source for the forward group-extension convention
     and the identity-cocycle condition attached to periodic points.  It also
     records the correspondence needed when moving between one- and two-sided
     symbolic codings.
   - **Boundary:** the statement that a natural extension does not manufacture
     inverse cocycle letters is a C29 inference from the forward cocycle
     definition, not a quoted theorem of this paper.  The source does not prove
     the frozen C25/C26 no-identity result.
   - **Evidence:** M1-direct / Grade A for the group-extension convention;
     existence and metadata verified on the Springer DOI page.  Use together
     with the 2024 correction below when relying on substantive theorems.

2. **Dougall, R., & Sharp, R. (2024). Correction to “Anosov flows, growth rates on covers and group extensions of subshifts.” *Inventiones Mathematicae, 236*, 1505--1509. https://doi.org/10.1007/s00222-024-01251-7**

   - **Use in C29:** integrity/version-control source for item 1.  The official
     abstract states that the listed main results remain unchanged.
   - **Boundary:** this correction is not independent evidence for a C29
     identity-holonomy theorem.  Any future quotation of an intermediate lemma
     from the 2021 paper must be checked against the correction itself.
   - **Evidence:** M2-integrity / Grade A; existence and metadata verified on
     the Springer DOI page.

3. **Daon, Y. (2013). Bernoullicity of equilibrium measures on countable Markov shifts. *Discrete and Continuous Dynamical Systems, 33*(9), 4003--4015. https://doi.org/10.3934/dcds.2013.33.4003**

   - **Use in C29:** primary countable-Markov reference for passing suitable
     two-sided Walters potentials to cohomologous one-sided potentials while
     preserving periodic sums.
   - **Boundary:** the theorem has regularity and transitivity hypotheses and
     concerns potentials, not formal inverse arrows.  It supports the semantic
     firewall but does not identify the declared symmetric C26 groupoid with an
     AGY natural extension.
   - **Evidence:** M1-direct / Grade A under its stated hypotheses; existence,
     volume, pages and DOI verified on the AIMS article page.

### Theme B -- Ihara, Hashimoto and finite non-backtracking determinants

4. **Hashimoto, K.-i. (1989). Zeta functions of finite graphs and representations of p-adic groups. In *Automorphic forms and geometry of arithmetic varieties* (Advanced Studies in Pure Mathematics, Vol. 15, pp. 211--280). Academic Press. https://doi.org/10.1016/B978-0-12-330580-0.50015-X**

   - **Use in C29:** foundational oriented-edge/non-backtracking operator and
     graph-zeta source; establishes that the finite Hashimoto framework is
     prior art.
   - **Boundary:** it does not contain the frozen Rauzy matrices, the C25/C26
     relations or the finite-Weil limiting argument.
   - **Evidence:** M1-framework / Grade A; chapter existence, pages and DOI
     verified on the official ScienceDirect page.

5. **Bass, H. (1992). The Ihara--Selberg zeta function of a tree lattice. *International Journal of Mathematics, 3*(6), 717--797. https://doi.org/10.1142/S0129167X92000357**

   - **Use in C29:** primary determinant-formula and representation-twisted
     graph (L)-function source.  It prevents claiming the general determinant
     mechanism as novel.
   - **Boundary:** Bass's tree-lattice and finite-graph hypotheses do not yield
     a trace theorem for the countable weighted AGY branch operator.
   - **Evidence:** M1-framework / Grade A; DOI and journal metadata verified.
     The DOI redirect blocks automated retrieval with HTTP 403, but the DOI
     record and publisher-indexed metadata agree.

6. **Stark, H. M., & Terras, A. A. (1996). Zeta functions of finite graphs and coverings. *Advances in Mathematics, 121*(1), 124--165. https://doi.org/10.1006/aima.1996.0050**

   - **Use in C29:** primary finite irregular-graph source for vertex, edge and
     path zeta functions and determinant specializations.
   - **Boundary:** finite scalar/path-variable determinant algebra is prior
     art; it does not establish the project-specific symplectic holonomy
     kernel.
   - **Evidence:** M1-direct / Grade A; title, authors, volume, pages and DOI
     verified on ScienceDirect.

7. **Stark, H. M., & Terras, A. A. (2000). Zeta functions of finite graphs and coverings, Part II. *Advances in Mathematics, 154*(1), 132--195. https://doi.org/10.1006/aima.2000.1917**

   - **Use in C29:** primary Artin--Ihara source for representation-valued
     twists, covering factorization and (L)-functions.
   - **Boundary:** the general Artin factorization is prior art and is not the
     C29 novelty claim.
   - **Evidence:** M1-direct / Grade A; metadata and DOI verified on
     ScienceDirect.

### Theme C -- matrix-weighted and unitary-twisted graph zeta

8. **Sato, I., Mitsuhashi, H., & Morita, H. (2014). A matrix-weighted zeta function of a graph. *Linear and Multilinear Algebra, 62*(1), 114--125. https://doi.org/10.1080/03081087.2013.764496**

   - **Use in C29:** direct primary reference that matrix-valued edge weights
     and their determinant expressions are established graph-zeta machinery.
   - **Boundary:** this paper does not supply the finite-Weil character limit,
     the regular group trace or a countable AGY transfer operator.
   - **Evidence:** M1-direct / Grade A; article metadata verified on the
     Taylor & Francis page.  Automated DOI retrieval ends at an access-control
     HTTP 403, not a missing DOI.

### Theme D -- von Neumann/group traces and determinants

9. **Fuglede, B., & Kadison, R. V. (1952). Determinant theory in finite factors. *Annals of Mathematics, 55*(3), 520--530. https://doi.org/10.2307/1969645**

   - **Use in C29:** foundational source for the Fuglede--Kadison determinant
     in finite factors.
   - **Boundary:** C29 currently defines only a small-disc analytic trace-log
     germ; this source must not be used to promote that germ to a global
     Fuglede--Kadison determinant without the required operator hypotheses.
   - **Evidence:** M1-framework / Grade A; journal, pages and DOI verified in
     the Annals/JSTOR metadata chain.  Automated redirect returns HTTP 403.

10. **de la Harpe, P., & Skandalis, G. (1984). Déterminant associé à une trace sur une algèbre de Banach. *Annales de l'Institut Fourier, 34*(1), 241--260. https://doi.org/10.5802/aif.958**

    - **Use in C29:** primary trace-determinant source supporting careful
      terminology for determinants associated with traces on Banach algebras.
    - **Boundary:** it is not a ready-made theorem for the C26 inverse-branch
      operator; C29 imports terminology, not an unproved global determinant.
    - **Evidence:** M1-framework / Grade A; complete metadata and DOI verified
      in Numdam.

11. **Clair, B., & Mokhtari-Sharghi, S. (2001). Zeta functions of discrete groups acting on trees. *Journal of Algebra, 237*(2), 591--620. https://doi.org/10.1006/jabr.2000.8600**

    - **Use in C29:** primary von Neumann-algebraic Ihara framework for bounded
      degree trees with cocompact or finite-covolume group actions.
    - **Boundary:** its bounded-degree tree/action hypotheses do not directly
      cover the countable analytic AGY operator or its expanding inverses.
    - **Evidence:** M1-framework / Grade A for its theorem, M2-adjacent /
      Grade B for direct C29 applicability; metadata and DOI verified on
      ScienceDirect.

12. **Lenz, D., Pogorzelski, F., & Schmidt, M. (2019). The Ihara zeta function for infinite graphs. *Transactions of the American Mathematical Society, 371*(8), 5687--5729. https://doi.org/10.1090/tran/7508**

    - **Use in C29:** primary measure-graph/groupoid source for canonical traces
      and determinant formulas under uniform bounded-degree conditions.
    - **Boundary:** the scalar measure-graph theorem includes finite unweighted
      graphs as a special case but does not by itself prove the finite-Weil
      block twist or a trace theorem for the countable weighted AGY operator.
    - **Evidence:** M1-framework / Grade A for its theorem, M2-adjacent /
      Grade B for direct C29 applicability; DOI and publication metadata
      verified through AMS-linked records and arXiv:1408.3522.  The automated
      DOI redirect returns HTTP 403.

### Theme E -- finite Weil representations and characters

13. **Gérardin, P. (1977). Weil representations associated to finite fields. *Journal of Algebra, 46*(1), 54--101. https://doi.org/10.1016/0021-8693(77)90394-5**

    - **Use in C29:** foundational construction, decomposition and character
      theory for Weil representations of symplectic groups in odd
      characteristic.
    - **Boundary:** it does not prove the repository's exact fixed-integral-
      matrix normalization or the C28 prime limit without additional
      specialization.
    - **Evidence:** M1-framework / Grade A; title, author, volume, pages and DOI
      verified on ScienceDirect.

14. **Thomas, T. (2008). The character of the Weil representation. *Journal of the London Mathematical Society, 77*(1), 221--239. https://doi.org/10.1112/jlms/jdm098**

    - **Use in C29:** direct primary character-formula source for Weil
      representations over finite or local fields; relevant to checking
      fixed-element character magnitudes.
    - **Boundary:** the C28 assertion
      (p^{-2}\Theta_p(g)\to\mathbf 1_{g=I}) for each fixed integral
      (g\in\operatorname{Sp}_4(\mathbb Z)) remains a repository specialization,
      not a verbatim theorem quoted from Thomas.
    - **Evidence:** M1-direct / Grade A for the character formula; DOI, pages
      and authorship verified on Oxford Academic.  Automated DOI retrieval is
      access-controlled with HTTP 403.

### Theme F -- Rauzy--Veech, Zorich and AGY dynamics

15. **Rauzy, G. (1979). Échanges d'intervalles et transformations induites. *Acta Arithmetica, 34*(4), 315--328. https://doi.org/10.4064/aa-34-4-315-328**

    - **Use in C29:** original induction and combinatorial return framework for
      interval exchanges.
    - **Boundary:** it does not fix the particular seven-state C25 Rauzy class,
      its statewise symplectic trivialization or the C26 branch matrices.
    - **Evidence:** M1-framework / Grade A; complete metadata and DOI verified
      on the official IMPAN journal page.

16. **Veech, W. A. (1982). Gauss measures for transformations on the space of interval exchange maps. *Annals of Mathematics, 115*(2), 201--242. https://doi.org/10.2307/1971391**

    - **Use in C29:** primary source for the measure-theoretic Rauzy--Veech
      induction framework on interval exchanges.
    - **Boundary:** measure and natural-extension structures do not authorize
      formal inverse letters with a newly assigned positive roof.
    - **Evidence:** M1-framework / Grade A; title, author, pages and DOI
      verified on the official Annals page.  Automated DOI retrieval returns
      HTTP 403 after resolution.

17. **Zorich, A. (1996). Finite Gauss measure on the space of interval exchange transformations: Lyapunov exponents. *Annales de l'Institut Fourier, 46*(2), 325--370. https://doi.org/10.5802/aif.1517**

    - **Use in C29:** primary source for the accelerated Rauzy map with finite
      absolutely continuous invariant measure and its cocycle/Lyapunov
      structure.
    - **Boundary:** acceleration does not turn inverse matrix symbols into
      genuine forward AGY branches.
    - **Evidence:** M1-framework / Grade A; complete metadata and DOI verified
      in Numdam.

18. **Avila, A., Gouëzel, S., & Yoccoz, J.-C. (2006). Exponential mixing for the Teichmüller flow. *Publications Mathématiques de l'IHÉS, 104*, 143--211. https://doi.org/10.1007/s10240-006-0001-5**

    - **Use in C29:** primary AGY source for an accelerated symbolic model,
      roofed hyperbolic semiflow and exponential-mixing framework for the
      Teichmüller flow.
    - **Boundary:** it does not make the inverse of a contracting C26
      holomorphic branch contractive, and it does not supply the proposed
      symmetric finite-Weil trace-log determinant.
    - **Evidence:** M1-direct / Grade A for the AGY dynamical framework,
      M2-adjacent / Grade B for the declared symmetric C29 object; complete
      metadata and DOI verified in Numdam and the publisher record.

## 4. Prior-art versus repository-specific boundary

The following are **general prior art**, with primary sources above:

- forward group extensions and identity-cocycle periodic conditions;
- one-/two-sided cohomology of suitable symbolic potentials;
- Hashimoto/Ihara non-backtracking operators and determinant formulas;
- Artin/representation twists and matrix-weighted graph zeta functions;
- determinants associated with finite-factor, Banach-algebra or groupoid
  traces under their respective hypotheses;
- finite-field Weil representations and character formulas;
- Rauzy--Veech induction, Zorich acceleration and the AGY roofed symbolic
  framework.

The following are **repository-specific claims/certificates**, not results
established by the external bibliography:

- the exact C25 positive-monoid freeness/decoding result in
  `../rauzy_metaplectic_obstruction/`;
- the two frozen C25 primitive length-six identity-holonomy cycles;
- the frozen C26 factorization (B=AHA\), (C=AKA), the exact braid relation
  (KYK=YKY) after (Y=H^{-1}KH), and the free cyclically reduced length-24
  identity word in (A,B,C);
- the C26 one-sided holomorphic trace-class construction in
  `../agy_holomorphic_slice_obstruction/`;
- the fixed-matrix finite-Weil normalization and prime limit certified in
  `../agy_finite_weil_determinant/` and
  `../agy_prime_direct_sum_determinant/`;
- the C29 locally uniform normalized determinant limit for the newly declared
  finite symmetric non-backtracking path system.

The bibliography therefore supports the framework and the scope restrictions;
it does not independently certify novelty or correctness of those exact local
matrix computations.

## 5. Search limitations

- This was a bounded, targeted search rather than an exhaustive MathSciNet or
  zbMATH review; global novelty is therefore **search-bounded**, not certified.
- Semantic Scholar batch verification was rate-limited (HTTP 429).  DOI
  resolution and official publisher/archive metadata were used instead.
- Several publisher redirects returned HTTP 403 to automated retrieval after
  the DOI resolved.  These were retained only when an official article page or
  authoritative metadata record independently matched title, authors, venue,
  year and DOI.
- No source found identifies the declared symmetric C26 inverse-arrow system
  as the genuine AGY natural extension or gives it an intrinsic positive AGY
  roof.  That absence is a scope boundary, not an impossibility theorem.
