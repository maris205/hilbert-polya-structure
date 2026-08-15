# Citation Verification

Verification date: 2026-08-14.  Scope: sources needed for the Paper-7 plan and
its safe claim boundary.  Metadata were checked against publisher DOI pages,
official journal records, or official arXiv records.  Published versions are
preferred when a stable journal DOI is available.  The corresponding BibTeX
file contains no memory-only entry.

## Verification rules

- `METADATA` means author, title, year, venue, and DOI/arXiv identifier were
  checked against a primary bibliographic endpoint.
- `CLAIM` means the cited use is no stronger than the theorem statement,
  abstract, or scope visible in the primary paper.
- A citation establishes context or attribution; it never substitutes for the
  self-contained local proof in Paper 7.
- A 2026 source discovered during this audit is labeled contemporary context
  or an independent cross-check, not retroactive prior motivation.
- The internal Batch-01 Paper-2 artifact is recorded separately because it has
  no public DOI or arXiv identifier.  No identifier is invented for it.

## External bibliography ledger

### `riveraletelier2026critical`

- **Record:** Juan Rivera--Letelier, “Locating critical points attracted to
  p-adic attracting cycles,” arXiv:2601.12163 (2026),
  DOI [10.48550/arXiv.2601.12163](https://doi.org/10.48550/arXiv.2601.12163).
- **Primary source:** [official arXiv record](https://arxiv.org/abs/2601.12163).
- **METADATA:** PASS.  Submitted 17 January 2026; primary class `math.DS`.
- **CLAIM:** PASS for the following narrow use: Theorem A uses the strict
  inequality
  \(|\lambda|<\lambda(d)^{\#\mathcal O}\) to force attraction of a critical
  point, and the paper states sharpness when \(\lambda(d)>0\).  At degree two
  in residue characteristic two the threshold is \(|2|^n\).
- **Boundary:** equality is not covered by the strict theorem.  Paper 7 cites
  this as a contemporary independent cross-check after giving its elementary
  contraction proof; it must not be described as the origin of that proof.

### `benedettoetal2014attracting`

- **Record:** Robert L. Benedetto, Patrick Ingram, Rafe Jones, and Alon Levy,
  “Attracting cycles in p-adic dynamics and height bounds for post-critically
  finite maps,” *Duke Mathematical Journal* 163(13) (2014), 2325--2356.
- **Identifiers:** DOI
  [10.1215/00127094-2804674](https://doi.org/10.1215/00127094-2804674),
  [arXiv:1201.1605](https://arxiv.org/abs/1201.1605).
- **METADATA:** PASS from the official arXiv journal reference and DOI link.
- **CLAIM:** PASS for earlier PCF/non-Archimedean attracting-cycle and height
  background.
- **Boundary:** do not attribute Paper 7's exact equality-boundary valuation
  or frozen Frobenius norm formula to this paper.

### `hutz2009good`

- **Record:** Benjamin Hutz, “Good reduction of periodic points on projective
  varieties,” *Illinois Journal of Mathematics* 53(4) (2009), 1109--1126.
- **Identifier:** [arXiv:0801.3645](https://arxiv.org/abs/0801.3645), arXiv
  DOI [10.48550/arXiv.0801.3645](https://doi.org/10.48550/arXiv.0801.3645).
- **METADATA:** PASS.  The official arXiv record verifies the author/preprint;
  the published title, volume, issue, and pages were cross-checked against the
  Illinois journal bibliography.  No journal DOI was found, so none is placed
  in the BibTeX `doi` field.
- **CLAIM:** PASS for primitive period versus reduced period under good
  reduction.
- **Boundary:** it does not by itself prove the unique Hensel lift, exact norm,
  or the two-coefficient obstruction specialized to the frozen cubic.

### `rajagopalzhang2025uniform`

- **Record:** Isaac Rajagopal and Robin Zhang, “Uniform bounds on periodic
  points of polynomials with good reduction,” arXiv:2510.26119 (submitted
  2025; version 2, 2026).
- **Identifiers:** arXiv DOI
  [10.48550/arXiv.2510.26119](https://doi.org/10.48550/arXiv.2510.26119);
  the official record also links related DOI
  [10.1007/s00605-026-02196-0](https://doi.org/10.1007/s00605-026-02196-0).
- **Primary source:** [official arXiv record](https://arxiv.org/abs/2510.26119).
- **METADATA:** PASS.  The BibTeX deliberately cites the stable arXiv version
  because the arXiv record does not yet provide full journal pagination.
- **CLAIM:** PASS for recent bounds on periodic points of good-reduction
  polynomials.
- **Boundary:** current context only; no result from this paper is a premise of
  the local contraction or norm proof.

### `morton1994rational`

- **Record:** Patrick Morton and Joseph H. Silverman, “Rational periodic
  points of rational functions,” *International Mathematics Research Notices*
  1994(2) (1994), 97--110.
- **Identifier:** DOI
  [10.1155/S1073792894000127](https://doi.org/10.1155/S1073792894000127).
- **METADATA:** PASS from the Oxford Academic article and issue records.
- **CLAIM:** PASS for dynatomic/formal-period background and arithmetic
  periodic-point context.
- **Boundary:** formal dynatomic roots must not be equated with least-period
  points without the source-locked exact-period saturation.

### `buffgauthier2015quadratic`

- **Record:** Xavier Buff and Thomas Gauthier, “Quadratic polynomials,
  multipliers and equidistribution,” *Proceedings of the American Mathematical
  Society* 143(7) (2015), 3011--3017.
- **Identifiers:** DOI
  [10.1090/S0002-9939-2015-12506-3](https://doi.org/10.1090/S0002-9939-2015-12506-3),
  [arXiv:1306.2736](https://arxiv.org/abs/1306.2736).
- **METADATA:** PASS from the official arXiv record and AMS volume/issue
  record.
- **CLAIM:** PASS for prescribed-multiplier loci and their parameter-space
  asymptotics.
- **Boundary:** the occurrence of the scale \(2^n\) in parameter-space work
  does not settle a multiplier value at the frozen PCF parameter.

### `jixiezhang2026space`

- **Record:** Zhuchao Ji, Junyi Xie, and Geng-Rui Zhang, “Space spanned by
  characteristic exponents,” *Mathematische Annalen* 394, article 62 (2026).
- **Identifiers:** DOI
  [10.1007/s00208-026-03361-4](https://doi.org/10.1007/s00208-026-03361-4),
  [arXiv:2308.00289](https://arxiv.org/abs/2308.00289).
- **METADATA:** PASS from the official arXiv journal reference and DOI link.
- **CLAIM:** PASS for characteristic-exponent terminology and global
  multiplier/length-spectrum context.
- **Boundary:** infinite-dimensional span or rigidity does not imply absence
  of one exact value.  The 2026 journal version is current positioning, not a
  logical prior for Paper 7.

### `murakami2024arithmetic`

- **Record:** Yuya Murakami, Kaoru Sano, and Kohei Takehira, “Arithmetic
  properties of multiplier polynomials for certain polynomial maps,”
  arXiv:2403.17315 (2024; version 3, 2025).
- **Identifier:** arXiv DOI
  [10.48550/arXiv.2403.17315](https://doi.org/10.48550/arXiv.2403.17315).
- **Primary source:** [official arXiv record](https://arxiv.org/abs/2403.17315).
- **METADATA:** PASS; no journal DOI is listed on the official record.
- **CLAIM:** PASS for integrality results concerning multiplier polynomials in
  unicritical and related families.
- **Boundary:** no all-period \(B_C=\pm1\) exclusion for this frozen parameter
  may be inferred from the general multiplier-polynomial framework.

### `benedettogoksel2023part1`

- **Record:** Robert L. Benedetto and Vefa Goksel, “Misiurewicz polynomials and
  dynamical units, Part I,” *International Journal of Number Theory* 19(6)
  (2023), 1249--1267.
- **Identifiers:** DOI
  [10.1142/S1793042123500616](https://doi.org/10.1142/S1793042123500616),
  [arXiv:2201.07868](https://arxiv.org/abs/2201.07868).
- **METADATA:** PASS from the official arXiv record and publisher DOI metadata.
- **CLAIM:** PASS for arithmetic of Misiurewicz parameters, their defining
  polynomials, and dynamical-unit questions.
- **Boundary:** parameter-polynomial evaluations are not automatically
  normalized products of arbitrary primitive cycles of the frozen map.

### `benedettogoksel2024part2`

- **Record:** Robert L. Benedetto and Vefa Goksel, “Misiurewicz polynomials and
  dynamical units, Part II,” *Research in Number Theory* 10, article 58 (2024).
- **Identifiers:** DOI
  [10.1007/s40993-024-00539-0](https://doi.org/10.1007/s40993-024-00539-0),
  [arXiv:2203.14431](https://arxiv.org/abs/2203.14431).
- **METADATA:** PASS from the official arXiv record and publisher DOI metadata.
- **CLAIM:** PASS for the stated connection between difficult parameter-
  polynomial evaluations and multipliers of associated periodic points.
- **Boundary:** “associated” does not mean every primitive cycle at the frozen
  type-\((3,1)\) map; no transfer to Paper 7's equality question is allowed
  without a new proof.

### `wang2026prime`

- **Record:** Liang Wang, “The emergence of prime distribution from
  low-dimensional deterministic chaos,” *Research in Mathematics* 13(1),
  article 2684334 (2026).
- **Identifier:** DOI
  [10.1080/27684830.2026.2684334](https://doi.org/10.1080/27684830.2026.2684334).
- **Primary source:** [publisher article page](https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2684334).
- **METADATA:** PASS; publisher issue record lists online publication on
  5 June 2026.
- **CLAIM:** PASS only for author/project genealogy and the origin of the broad
  motivation.
- **Boundary:** no prime table, Riemann-zero data, empirical fit, conjectural
  identification, or latest conclusion from this article is a Paper-7 prior,
  assumption, control, or validation source.

### `silverman2007arithmetic`

- **Record:** Joseph H. Silverman, *The Arithmetic of Dynamical Systems*,
  Graduate Texts in Mathematics 241, Springer, New York (2007).
- **Identifier:** DOI
  [10.1007/978-0-387-69904-2](https://doi.org/10.1007/978-0-387-69904-2).
- **METADATA:** PASS from the official Springer book record.
- **CLAIM:** PASS for standard definitions and general local/global arithmetic-
  dynamics background.
- **Boundary:** use as a textbook source, not as attribution for Paper 7's
  frozen calculation.

## Project genealogy without a fabricated citation

The immediate predecessor is the local artifact
`papers/3-prime-multiplier-obstruction/paper/paper_final.pdf`:

- **Title in the final PDF:** *Raw Rational-Prime Multipliers at a Frozen PCF
  Quadratic: Divisibility Obstruction and Exact Audit*.
- **Author/date:** Liang Wang, 2026-08-13.
- **Final PDF SHA-256:**
  `160e9c6fa12c35f500fbae39d9316fc55e8c9b4f1b044ef3deda6037e0b5b1c3`.
- **Bound source-lock SHA-256:**
  `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842`.
- **Inherited result:** the derivative-content theorem and the rational
  divisibility \(\Lambda_C\in2^n\mathbb Z\); the predecessor explicitly left
  \(|\Lambda_C|=2^n\) open for \(n\ge2\).
- **Paper-7 use:** provenance and project genealogy only.  Paper 7 should
  restate the short integrality step needed for its corollary, so an
  unpublished local artifact is not the sole support of a theorem.

There is intentionally no `@unpublished` entry for this artifact in
`references.bib`: it has no public DOI, arXiv record, or stable repository
identifier.  If one is assigned before release, add it only after a new
metadata check and update this ledger.

## Chronology and no-prior-leakage audit

1. Rivera--Letelier (2026) was located during the current source audit.  It is
   a sharp independent comparison and optional second proof check.  Paper 7's
   primary proof remains the elementary local contraction argument.
2. Ji--Xie--Zhang appeared first as a 2023 arXiv preprint and as a 2026 journal
   article.  It is used for standard semantics/current landscape, not for a
   value-specific inference.
3. Rajagopal--Zhang's 2026 revision is current good-reduction context only.
4. Wang (2026) is genealogy only.  No external prime or zero dataset was
   accessed or transferred, consistent with source-lock v2.
5. The pre-lock period-1--8 observations and the repeated period-4--7 benchmark
   are not literature evidence and must not appear as prospective validation.

## BibTeX completeness check

The bibliography contains twelve external entries.  Every entry has at least
one verified official DOI or arXiv identifier; every published item uses the
journal DOI where available.  Hutz is the only published article without a
located journal DOI, and its official arXiv identifier is retained.  There are
no placeholder keys, guessed page ranges, or invented project citations.

