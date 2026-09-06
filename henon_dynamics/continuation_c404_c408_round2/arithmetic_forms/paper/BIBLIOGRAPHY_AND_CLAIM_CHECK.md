# C405 initial manuscript: bibliography and claim check

2026-09-06. This is the manuscript preparer's check, not the pending
independent manuscript review. Six works are cited. The bibliography contains
only those six works, with no unverified placeholder or fabricated author.

## Bibliographic metadata and actual consultation

### Aistleitner, Berkes and Seip (2015)

*GCD sums from Poisson integrals and systems of dilated functions*,
Journal of the European Mathematical Society **17**(6), 1517–1546.
DOI: [10.4171/JEMS/537](https://doi.org/10.4171/JEMS/537).

- Fresh metadata checks: [EMS publisher record](https://ems.press/journals/jems/articles/12412),
  its original published PDF header, the arXiv version record, and successful
  DOI BibTeX content negotiation. The verified print year is 2015.
- Fresh mathematical passage: [arXiv:1210.0741v3](https://arxiv.org/html/1210.0741v3),
  introduction's prime-square threshold discussion and Section 3, Lemma 1,
  including the finite Poisson formula and attribution immediately afterward.
- The manuscript explicitly credits the finite product kernel, positivity and
  finite GCD norm context. The bibliography identifies the consulted preprint
  for the precise lemma locator. No current open-problem claim is copied from
  the old preprint, and its generated HTML date is not its publication year.

### Bingham, Goldie and Teugels (1987)

*Regular Variation*, Cambridge University Press.
DOI: [10.1017/CBO9780511721434](https://doi.org/10.1017/CBO9780511721434).

- Metadata was reused from the already checked C403 bibliography and its
  [verification record](../../../continuation_c399_c403_round2/spectral_regular_variation/paper/BIBLIOGRAPHY_CHECK.md),
  which records the publisher and successful DOI export. The existing BibTeX
  was read and its fields copied without inventing a new edition or locator.
- This writing task did not read the book in full. The exact measurable
  slow-variation uniform convergence statement used is displayed as (4.1).
  The finite-block and floor arguments are proved in Lemma 4.1, not attributed
  to an uninspected book page. No Potter estimate is invoked in this paper.

### Hilberdink (2017)

*Singular values of multiplicative Toeplitz matrices*, Linear and
Multilinear Algebra **65**(4), 813–829.
DOI: [10.1080/03081087.2016.1204978](https://doi.org/10.1080/03081087.2016.1204978).

- Print metadata was reused from the verified C403 BibTeX and its record
  linked above, and cross-checked against the current supplied source audit.
  The DOI export's online year 2016 is not confused with the print year 2017.
- The current [source audit](../SOURCE_AUDIT.md) records actual access to the
  accepted manuscript at the University of Reading and Proposition 2.1.
  This writer did not claim a fresh complete reading of that paper.
- The arbitrary-coefficient Gram identity is expressly prior-owned. Lemma 4.2
  derives the required specialization directly, so no inaccessible proof is
  substituted for the manuscript's argument.

### Hilberdink and Pushnitski (2023)

*Spectral asymptotics for a family of LCM matrices*, St. Petersburg
Mathematical Journal **34**(3), 463–481.
DOI: [10.1090/spmj/1764](https://doi.org/10.1090/spmj/1764).

- English-edition metadata was reused from the verified C403 record and
  BibTeX. That record separates it from the Russian 2022 edition and pages.
- Fresh mathematical access: [arXiv:2110.14323v1](https://arxiv.org/html/2110.14323v1),
  introductory compact-operator statement and Sections 2.2–2.3, including
  Theorem 2.1. The consulted Gram theorem assumes sigma below 1/2 and even
  Schatten exponent q with q(1−2 sigma)>1.
- The manuscript says only convergence in the source's stated Schatten
  range; it neither silently drops the evenness restriction nor presents
  an old conjecture as currently open. The bibliography marks the consulted
  preprint version. No new LCM diagonalization or norm asymptotic is claimed.

### Simon (1978)

*A canonical decomposition for quadratic forms with applications to monotone
convergence theorems*, Journal of Functional Analysis **28**(3), 377–385.
DOI: [10.1016/0022-1236(78)90094-0](https://doi.org/10.1016/0022-1236(78)90094-0).

- Fresh metadata checks: [author bibliography, item 81](https://math.caltech.edu/simon/biblio.html)
  and successful DOI BibTeX content negotiation.
- Fresh original text: [author-hosted PDF](https://math.caltech.edu/SimonPapers/81.pdf),
  Section 2, Theorems 2.1–2.2 and their largest-closable-minorant consequence;
  Section 3, the monotone hypotheses and statements of Theorems 3.1–3.2.
  No full-paper reading or complete rereading of the differential-operator
  applications is claimed, and the external PDF is not redistributed.
- Sections 1–3 of the manuscript credit this framework explicitly. The
  arbitrary-positive-entrywise-approximant result is proved by recovery
  vectors and minimization, not asserted to be Simon's monotone theorem.

### Yafaev (2017)

*On semibounded Toeplitz operators*, Journal of Operator Theory **77**(1),
205–216. DOI: [10.7900/jot.2016mar20.2095](https://doi.org/10.7900/jot.2016mar20.2095).

- Fresh metadata checks: the [journal's original PDF header](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf),
  journal issue listing, arXiv record, and successful DOI BibTeX export.
- Fresh mathematical text: [arXiv:1603.06229v1](https://arxiv.org/html/1603.06229v1),
  Section 2.1, including the nonnegative symmetric-operator closability
  observation and closed-form representation. The surrounding one-circle
  criterion is used only for positioning, not transferred to an infinite
  product without proof.
- The bibliography records this consulted preprint. No claim depends on an
  unverified equality of every later-version theorem or page number.

## Claim-to-manuscript and proof-package coverage

| Accepted claim | Manuscript location | Check performed by preparer |
|---|---|---|
| Both critical summability branches | Theorem 1.1; proofs in Sections 4–5 | Fixed space, positive L, finite normalization and all-vector/all-lambda quantifiers retained |
| Exact prime-product closability criterion | Proposition 2.3 | Finite positivity credited; explicit tail identities and converse column-square sum included |
| Every closable minorant vanishes | Proposition 2.3 proof | Argument starts with arbitrary finite f and arbitrary closable b; not just a single nonclosability witness |
| Positive entrywise approximants have zero resolvent limit | Proposition 3.1 | Each finite-vector limit precedes the increasing-index diagonal; positivity and minimizer estimate explicit |
| Norms actually tend to infinity | End of Proposition 3.1 | A fixed test vector is selected for each M and the bound holds eventually for all N |
| Full measurable slow-variation family | Lemma 4.1 and divergent-branch proof | UCT version, fixed-block order of limits, negligible initial segment, and floors included |
| Nonzero maximal-convolution limit | Lemmas 5.1–5.2 and summable-branch proof | Closed/dense maximal domain, fixed-row weak lower bound, recovery at true minimizer, strong convexity included |
| Nonmultiplicative examples | Section 6 | Elementary beta threshold and explicit 2,3,6 nonmultiplicativity test |
| Finite sentinels and failure control only | Sections 6–7 | Values transcribed from frozen receipts; no numerical rerun or asymptotic numerical claim |
| Source-only fixed-space scope | Section 6 and conclusion | No general form-theory priority, target arithmetic or all-renormalization exclusion |

The branch-comparison table's summable entrywise description follows from
(5.3) by polarization, since each coordinate vector belongs to D(C). Its
caption expressly avoids assuming the coordinates belong to D(C*C).

The preparer's reverse-outline pass follows a single dependency chain:
fixed-space endpoint question → prime-product form → explicit singular
recovery → positive-approximant resolvents → critical Gram identification →
maximal-domain alternative → finite checks and scope. All eight section
files are included by main.tex. The six BibTeX keys are exactly the six
distinct keys in main.aux; every citation resolves in the completed build.

## Remaining gate

No unresolved bibliography placeholder or claimed theorem correction is
identified by this writing pass. A different agent must still read the
actual manuscript and assess its prose, claim/citation contexts and proof
presentation. The earlier independent review was of the proof package,
not this newly written text. Final deterministic double builds and all-page
release QA are reserved for the coordinator after that review.
