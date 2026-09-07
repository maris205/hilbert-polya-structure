# C415 citation and source-ownership audit

Date: 7 September 2026. Scope: the actual C415 manuscript and its five
bibliography entries. This is an AI-assisted author audit, not independent
human peer review, an indexing search, a publication certificate, or a
worldwide novelty guarantee. The coordinator owns manuscript-level
nonauthor review and final release.

## Actual source access and allowed uses

| Key | Primary source and verified metadata | Access actually used | Manuscript use and boundary |
|---|---|---|---|
| `Bridy2016` | Andrew Bridy, *The Artin-Mazur Zeta Function of a Dynamically Affine Rational Map in Positive Characteristic*, JTNB 28(2) (2016), 301–324; DOI 10.5802/jtnb.941. [Numdam article record](https://numdam.org/articles/10.5802/jtnb.941/) | Fresh primary metadata, abstract, and displayed BibTeX were read in this author turn. The earlier accepted source audit also records selected PDF introduction and preliminary sections; this is not a claim to have freshly reread the entire paper. | Section 1.1 attributes the dynamically affine projective-line rationality/transcendence scope. No theorem for arbitrary nonlinear Hénon maps, no all-rational-map dichotomy, and no current status claim about a conjecture is attributed to it. The journal year is 2016; the record's online date in 2017 is not substituted for that year. |
| `BCH2024` | Jakub Byszewski, Gunther Cornelissen, Marc Houben, *Dynamics of endomorphisms of algebraic groups*, [arXiv:2209.00085v2](https://arxiv.org/abs/2209.00085v2), revised 19 April 2024. | Fresh official arXiv metadata and abstract only. The 176-page body was not read for this manuscript. | Section 1.1 identifies the smooth algebraic-group and finite-adelically distorted sequence frameworks. No numbered result, unseen hypothesis, or automatic membership of the present family is asserted. The entry is a versioned preprint, not an invented journal citation. |
| `CLO2015` | David A. Cox, John Little, Donal O'Shea, *Ideals, Varieties, and Algorithms*, fourth edition, Undergraduate Texts in Mathematics, Springer, Cham, 2015; DOI 10.1007/978-3-319-16721-3. [Publisher record](https://link.springer.com/book/10.1007/978-3-319-16721-3) | Fresh publisher metadata, table of contents, and bibliographic-information block; not a full-text read of the textbook. | Section 3 cites the standard Gröbner/Buchberger framework without an unverified page or theorem number. The particular two-generator S-polynomial representation and rectangle basis are given in the body, not delegated to a possibly unseen result. |
| `StacksFrobenius` | The Stacks Project Authors, Lemma 33.36.3, [Tag 0CC8](https://stacks.math.columbia.edu/tag/0CC8). | Fresh full lemma statement and short proof/reference were read. The statement concerns absolute Frobenius as an integral universal homeomorphism with purely inseparable residue extensions. | Section 2 attributes the standard universal-homeomorphism fact. Finiteness for coordinatewise Frobenius on affine two-space is an elementary property of this explicit polynomial map; no assertion that arbitrary absolute Frobenius is finite is attributed to the tag. The subsequent reduced fixed-scheme calculation is independently proved in Section 3. |
| `C404` | Anonymous Authors, *All-period resonant counts for nonlinear Hénon–Frobenius maps*, Internal research series C404, 6 September 2026. | Actual local `henon_resonance/paper/main.tex`, its zeta section, complete `henon_resonance/PROOF_PACKAGE.md`, and source audit were read during preparation. The manuscript title, date, and anonymous author line were checked against the actual source again in this author turn. | Sections 1.1 and 7 credit the commuting-pullback conversion and positive-tail natural-boundary mechanism. It is explicitly an internal repository manuscript, not a journal publication or external peer-review result. The needed proof is reproduced in C415. |

No source text is quoted verbatim in the manuscript. Bibliographic titles
are identifiers. Abstract-level source summaries are short and confined
to their verified scope; the new algebraic calculations are the author's
proofs, not paraphrases of those abstracts.

## Exact contribution subtraction

The accepted mathematical input is
`research_c414_c418/positive_characteristic/FULL_DEGREE_2P_PROOF.md`
(SHA256 `683f4212a1f405fc4d2d5c67ba88e00a34595fb4172a25f1cdad9604841317f5`),
with the full integral strict-gap proof in `PROOF_NOTE.md` and its final
independent internal review in `arithmetic/REVIEW_CHARP_PROOF.md`.
Those frozen files were read; no old mathematical certificate or census
was rerun and no frozen file was edited.

The manuscript subtracts the following ownership explicitly:

- Perfection, coefficient Frobenius, the first nonzero binomial index,
  coprime leading monomials, and Jacobian reducedness are algebraic
  mechanisms, not separately claimed discoveries.
- C404 already owns the commuting-operator conversion and analytic
  positive-tail argument within this repository stream. Both are fully
  reproduced for readability, without claiming a new analytic mechanism.
- The high-support two-term strict-gap calculation was an existing
  restricted companion. It is proved in full and its inequalities are
  checked uniformly for the present family; it is not another paper.
- The degree-six instance and the pure pth-power face are special cases,
  not independent contracts. The admitted increment is the entire
  degree-2p coefficient family for every odd p and every q=p^e, e>=3,
  especially the low-support semilinear state with mixed fractional tails
  and actual ordinary-polynomial descent.

The frozen outline's citation line mentions “applicable C404/C405” results.
The actual current C405 is a critical-divisor/Gram/strong-resolvent paper,
not an input to this count. This mismatch was reported to the coordinator.
Only the actually relevant C404 is cited; an unrelated reference has not
been inserted to match an identifier string.

## Manuscript claim-to-evidence map

| Actual manuscript location | Claim | Complete typeset evidence |
|---|---|---|
| Theorem 1.1 and (1.3)–(1.4) | Every coefficient, every positive S-iterate, ordinary geometric points | Propositions 3.1, 4.2, 6.3 and the proof of Theorem 1.1 |
| Section 3 | Equalizer length becomes an ordinary count | Commuting factorization, explicit coprime S-polynomial argument, finite quotient basis, and local Jacobian/Nakayama argument |
| Section 4 | High-support block never receives a hidden lower-support tie | First-index lemma, both uniform strict inequalities, retained two terms, and entire remainder estimate |
| Sections 5–6 | Low support including c=0 and non-prime-field coefficients | Concrete finite perfected ring, sigma-semilinearity, arbitrary mixed-monomial bound, integer/fractional expansions, induction, denominator-level descent, and coefficient recurrence |
| Theorem 7.1 | Product and natural boundary of each positive integral power | Absolute interchange, positive tail exponents, primitive p^r roots with r>=1, dominated radial order, and dense nonintegral orders |
| Example 8.1 | q=27 support sensitivity | Direct arithmetic substitution into the proved formula; not a new experimental run |

## Bibliography closure and status

All five keys are actually cited in the TeX body. No `nocite` expansion,
uncited padding, placeholder DOI, invented author, or unrelated source is
used. DOI/primary-URL locators are preserved in `references.bib` and in
rendered bibliography notes where the chosen `amsplain` style would
otherwise suppress those fields.

The source comparison is bounded to these accesses and the already
reviewed repository collision audit. No fresh comprehensive literature
search, Scopus/Web of Science indexing check, conflict-of-interest
clearance, human sign-off, or external model review is represented as
performed. The manuscript's ordinary count, map, domain, and clock remain
those of the frozen admitted C415 contract.
