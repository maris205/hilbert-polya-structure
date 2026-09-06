# C404 manuscript citation and source verification

Date: 2026-09-06. This audit applies to the actual initial manuscript,
whose eleven TeX/BibTeX inputs are listed in SOURCE_INPUTS.sha256.
It supplements, and does not rewrite, the frozen ../SOURCE_AUDIT.md.
The four bibliography entries have five actual citation contexts. A
source-text scan found no missing citation key, uncited entry, missing
reference label, or duplicate label. This is not a full-literature or
global-priority certificate.

## Actual citation contexts

| Key | Actual TeX location | Claim and source locator | Scope retained |
|---|---|---|---|
| bch2024groups | sections/1_introduction.tex:83 | Algebraic-group endomorphisms, finite-adelic distortion, and zeta dichotomies; arXiv v2 Theorems A and C, §5.2 | Prior mechanism ownership, not a theorem for arbitrary nonlinear affine-plane maps |
| bch2024groups | sections/6_boundaries.tex:30 | Direct vector-group setting; arXiv v2 Theorem 5.2.5 | The manuscript's own finite-subgroup proof excludes direct vector-group conjugacy only |
| bridy2012transcendence | sections/1_introduction.tex:94 | One-variable derivative-zero rationality and transcendental examples; arXiv v2 Theorems 1–2, printed page 3 | No inference from the affine line to this two-dimensional map |
| bch2020affine | sections/1_introduction.tex:100 | Dynamically affine maps on P¹, specified Kummer varieties, and a separate higher-dimensional framework; arXiv v1 definitions and Theorems A–B, printed page 7 | No unverified application of hypotheses (H1)–(H4), and no blanket quotient exclusion |
| cox2015ideals | sections/4_exact_count.tex:15 | Classical coprime-leading-monomial criterion and standard-monomial basis | Book metadata and chapter listing verified; complete official chapter text was not obtained, so no exact-page full-text attestation is made |

The fourth citation is only a classical ownership pointer. The actual
two-generator S-polynomial representation and the quotient's standard
monomial rectangle are written explicitly in the manuscript. None of
these citations replaces the nonlinear leading-term proof or its
all-period quantifiers.

## Metadata and access record

1. Byszewski, Cornelissen, and Houben, *Dynamics of endomorphisms of
   algebraic groups*. The [official arXiv v2 record](https://arxiv.org/abs/2209.00085v2)
   confirms all three authors, the title, first posting in 2022, and the
   19 April 2024 revision. The [v2 author HTML](https://arxiv.org/html/2209.00085v2)
   was the primary theorem text in the frozen source audit. The manuscript
   cites that exact version. No journal metadata is invented.

2. Bridy, *Transcendence of the Artin-Mazur Zeta Function for Polynomial
   Maps of A¹(F̄_p)*. The [author's publication list](https://campuspress.yale.edu/andrewbridy/)
   and official publisher metadata confirm Acta Arithmetica 156 (2012),
   no. 3, 293–300. DOI content negotiation for
   [10.4064/aa156-3-6](https://doi.org/10.4064/aa156-3-6)
   succeeded during manuscript preparation. The returned title contains
   HTML mathematical markup, normalized to TeX without changing the
   mathematical title. The theorem text was actually read in the
   [author preprint](https://arxiv.org/pdf/1202.0362), v2, 14 May 2012,
   as recorded in the frozen audit. Publisher full-text attempts timed
   out; they are not represented as successful access.

3. Byszewski, Cornelissen, and Houben, *Dynamically affine maps in positive
   characteristic*. During manuscript preparation, DOI content negotiation
   for [10.1090/conm/744/14982](https://doi.org/10.1090/conm/744/14982)
   successfully returned the authors, title, book title, publisher, year
   2020, and pages 125–156. The
   [Jagiellonian University bibliographic record](https://ruj.uj.edu.pl/entities/publication/74d03e37-ea09-45ba-b1ee-ad590ef1b4ed)
   independently confirms Contemporary Mathematics 744, the four editors,
   and the Appendix B contribution by Lois van der Meijden with the
   three main authors. The verified record permits a proper incollection
   entry even though the DOI service exported a generic misc type.
   No unverified ISBN or publication address is included.
   The theorem text and numbering were read from the
   [official arXiv v1 preprint](https://arxiv.org/abs/1904.04942v1)
   in the frozen audit, and the bibliography explicitly says that the
   manuscript's theorem locators refer to this version. A new attempt
   to open the versioned PDF timed out; an institutional published-PDF
   link returned 403. We do not claim to have verified that published
   full text or its pagination. The published metadata is an addition
   to the manuscript bibliography, not a mutation of the frozen audit.

4. Cox, Little, and O'Shea, *Ideals, Varieties, and Algorithms: An
   Introduction to Computational Algebraic Geometry and Commutative
   Algebra*, fourth edition, Springer, 2015. The
   [official book record](https://link.springer.com/book/10.1007/978-3-319-16721-3)
   and successful DOI content negotiation verify the title, authors,
   edition, publisher, year, and DOI. The official metadata/chapter
   listing is the access level; a complete official chapter was not
   read. Third-party scans are not used as authoritative evidence.

The bibliography was created from these checked records and the
version-specific source audit, not from memory. All four entries are
actually cited. The selected amsplain style does not print its doi or
url fields; the checked identifiers remain in references.bib and this audit.

## Claim and notation cross-check

The main theorem is Theorem 1.1, with the count (1.3) and actual leading
terms (1.4). Its complete proof comprises the operator setup in §2,
Lemmas 3.1–3.2 and Proposition 3.3, followed by quotient length and
reducedness in §4. Corollary 1.2 is proved in §5, including local uniform
convergence, exact radial order, density for every fixed positive power,
and the algebraicity obstruction. Proposition 6.1 is the narrow direct
vector-group conjugacy obstruction. Example 6.2 contains a direct
expansion proving the p-divisible-degree failure; it does not claim a
classification. Table 1 matches the five frozen exact records.

The manuscript keeps the following distinctions explicit:

- linear pullbacks versus nonlinear point-map subtraction;
- integer degrees versus coefficients reduced modulo p;
- scheme length versus ordinary geometric count;
- radicial function-field degree versus geometric fiber cardinality;
- fixed dynamics of S versus ordinary H-periodicity or Hasse–Weil counting;
- exclusion of a direct vector group versus unclassified finite quotients;
- an exact source-system zeta versus any absent target-arithmetic bridge.

This author-side audit does not replace the independent reading of the
actual manuscript. No external human review, external model call,
manuscript upload, paid service, or venue-integrity certification is claimed.
