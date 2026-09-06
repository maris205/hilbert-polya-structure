# Primary-source and repository ownership audit

Date: 2026-09-05. Bounded source check for one proposed spectral contract,
not a systematic literature review or a priority certificate.

## Accessed closest sources

| Work | What was actually accessed | Owned result and remaining distinction |
|---|---|---|
| T. Hilberdink, *Singular values of multiplicative Toeplitz matrices*, Linear and Multilinear Algebra 65(4) (2017), 813--829, DOI [10.1080/03081087.2016.1204978](https://doi.org/10.1080/03081087.2016.1204978) | [Official university record](https://centaur.reading.ac.uk/66059/) and the complete [accepted manuscript](https://centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf), downloaded from that URL by curl and read via text extraction, including sections 0--4 and Appendix A1. | Proposition 2.1 owns the general Gram identity. Theorem 2.2/Corollary 2.3 give Hilbert--Schmidt and trace-class convergence for completely multiplicative coefficients under regular variation of their cumulative square sum. Theorems 3.1/3.2 address multiplicative coefficients with further local/correlation conditions. Section 4(a) identifies the power-coefficient LCM limit. Our assumption is pointwise regular variation with no multiplicativity, and our conclusion covers every admissible real Schatten exponent. The two coefficient classes are complementary; neither is described as containing all of the other. |
| T. Hilberdink and A. Pushnitski, *Spectral asymptotics for a family of LCM matrices*, [arXiv:2110.14323v1](https://arxiv.org/html/2110.14323v1), 27 October 2021; published in Algebra i Analiz 34(3) (2022), 207--231, with English translation in St. Petersburg Mathematical Journal 34(3) (2023), 463--481 | Author HTML: introduction, Theorem 1.1, all of section 2 including the proof of Theorem 2.1; additional parts of sections 3 and 4 were consulted, not claimed fully audited. Journal identity was checked against official MathNet metadata. | Theorem 1.1 owns positivity, compactness, injectivity, eigenvalue asymptotics, and the exact S_q threshold of E(sigma,tau). Theorem 2.1 proves normalized power-coefficient Gram convergence for even integer q with q rho>1; the following paragraph explicitly raises lifting that restriction. The proposed theorem both treats nonmultiplicative slowly-varying coefficients and supplies all real q in the sharp range. Neither the LCM spectrum nor its prime tensor decomposition is claimed new. |

The 2017 PDF has 16 physical pages (repository cover plus 15 numbered
manuscript pages), 421253 bytes, SHA256
`d040bf0f3df4da2d72b1f7728b80c6e3fed3d1214ed1e3a895e8dde81f71b518`.
It was fetched into a temporary source cache, not copied into this repository.
The browser open returned an anti-bot error, whereas a normal curl request
to the same public official URL returned the actual PDF successfully.
The repository cover/PDF metadata carry 2026 processing dates; these are not
the paper's publication date. The accepted manuscript title, authorship,
theorem statements and printed numbering were checked in the extracted text.
No screenshot/page-anchor annotation artifact is claimed.

The 2021 HTML version identifier and date are explicit in the source.
Its even-integer remark is evidence of what that version says, not evidence
that an open question remained unresolved through September 2026. No such
current-open-problem or global-priority claim is made.

## Classical proof dependencies

Potter's estimate is stated explicitly in Hilberdink 2017, section 1.1,
and credited there to Bingham--Goldie--Teugels, *Regular Variation* (1987).
The uniform convergence theorem for measurable slowly-varying functions
is also a standard input to our proof. The original Bingham--Goldie--Teugels
book has not been fully inspected in this scan; do not attach an invented
book page or theorem number. The needed statements and their hypotheses
are written explicitly in the proof package. The required discrete
averaging argument is proved there from these statements.

Min--max, operator ideal linearity, and the singular-value sum inequality
are classical inputs. The proof's entrywise majorant is used ONLY for an
operator-norm estimate of a positive diagonal congruence; it does not invoke
a false general Schatten entrywise-majorant principle.

## Search record and limits

No Zotero or Obsidian connector was available in the tool catalog. A
filename scan of the repository `papers/` and relevant PDF names found no
Hilberdink/LCM/Toeplitz source copy; `literature/` is absent. No project
`tools/arxiv_fetch.py` or skill-local fetch script was present. The arXiv
metadata/source step therefore used the browser fallback. No arXiv PDF was
downloaded under the research-lit default; the sole downloaded original
here is the public university accepted manuscript linked above.

Queries included the exact titles and identifiers, `Hilberdink slowly
varying Toeplitz`, `site:arxiv.org Toeplitz slowly varying`, `LCM matrices
Schatten`, and `Hilberdink Pushnitski even convergence`. Most additional
slow-variation results concern additive Toeplitz or stochastic models,
not this divisibility Gram limit, and were not promoted to relevant sources.
No inspected follow-up supplied the stated nonmultiplicative full-range
theorem. This is search-bounded, not exhaustive.

The report uses primary theorem statements, not citation-count rankings,
venue-quartile scores, or an experimental evidence hierarchy inapplicable to
pure operator theory. No external model, journal submission, paid retrieval,
or human peer review was used.

## Repository collision and discarded entrances

The targeted repository scan used LCM/Toeplitz/Hilberdink and
regular-variation/Schatten terms. The important neighboring rejection is
[P44--P48 replacement-candidate ledger](../../../symbolic_dynamics/docs/papers44_48_sequence/phase2/REPLACEMENT_CANDIDATES.md).
Its perfect-power product operator was stopped after subtraction of
Hilberdink's prime tensor, norm product and Schatten machinery. That
rejection remains valid; it is not reopened here. The present theorem is
about a family of nonmultiplicative finite divisibility Grams and a
limit in a sharp ideal topology, not diagonalizing another prime product.
Only the relevant portions of that other stream were read; nothing was edited.

A preceding Helson-matrix spectral-asymptotic entrance was also abandoned
after the inspected Miheisi/Pushnitski work already supplied the contemplated
power-law mechanism. No new contract, proof, or paper is claimed for it.
Likewise, the LCM limit spectrum by itself is discarded as prior-owned.
One contract survives provisionally: nonmultiplicative regular-variation
universality with full-range Schatten convergence.

## Admission boundary

The complete theorem, rather than just the L=1 even-q improvement, is the
object submitted for independent internal proof/admission review. All
corollaries remain in that same proposed paper. The source kernel has
intrinsic divisibility arithmetic, but no target Euler factors, root number,
automorphy, zero/divisor identification, or Hilbert--Polya correspondence
follows. In particular, carrying a zeta-derived classical source kernel
does not establish the repository's target A2/A3 requirements.
