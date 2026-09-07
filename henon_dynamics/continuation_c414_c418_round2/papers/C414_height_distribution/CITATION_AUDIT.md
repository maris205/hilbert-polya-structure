# C414 manuscript citations and source-access boundary

All four entries in `references.bib` are cited in the introduction.
The manuscript has no selected venue or claimed external submission.
Bibliographic existence is distinguished from actual text access.

## Record verification

1. `ingram2014canonical`: the previously primary-verified C412 bibliography
   and accepted height source audit agree on Patrick Ingram, *Canonical
   heights for Hénon maps*, Proc. London Math. Soc. 108(3) (2014), 780–808,
   DOI `10.1112/plms/pdt026`. Actual source-text comparison is the
   introduction and §2 of arXiv:1111.3609v1. Its arXiv header is
   15 November 2011 and served manuscript-internal date 21 August 2017;
   these are not silently identified with the 2014 journal issue or
   online-first 2013 date. No final journal proof reread is claimed.
2. `kawaguchi2013local`: fresh direct DOI BibTeX request on 2026-09-07
   failed with curl exit 35 (SSL connection to api.crossref.org).
   Browser open of the official MSP XHTML record was unsupported, then
   read-only curl to <https://msp.org/ant/2013/7-5/p08.xhtml> succeeded,
   exit 0. Its metadata/title/volume block confirms Shu Kawaguchi,
   *Local and global canonical height functions for affine space regular
   automorphisms*, Algebra & Number Theory 7(5) (2013), 1225–1252,
   DOI `10.2140/ant.2013.7.1225`. Only relevant metadata/abstract blocks
   of that fresh request were inspected; unrelated page navigation is
   not a new source audit. The original accepted source review read the
   official PDF introduction and Theorems A/B, Corollaries C/D as recorded.
3. `takehira2025number`: fresh DOI content negotiation on 2026-09-07,
   `curl -fsSL --max-time 25 -H 'Accept: application/x-bibtex'
   https://doi.org/10.1016/j.jnt.2024.11.007`, exit 0, returned Kohei
   Takehira, *On the number of points with bounded dynamical canonical
   height*, Journal of Number Theory 271 (2025), 216–245.
   The bibliography transcribes those returned fields. Actual proof-text
   comparison remains arXiv:2404.00955v1, introduction, §2.2,
   Condition 3.1, Theorem 3.4 and opening of §4. Its header date
   1 April 2024 and manuscript-internal date 2 April 2024 are distinct.
   Failed v2 HTML and later publisher full-text access are not reported
   as successful final-version reading.
4. `hsia1997dynamical`: fresh DOI BibTeX request with the same command
   pattern for `10.1006/jnth.1997.2076`, exit 0, returned Liang-chung
   Hsia, *On the Dynamical Height Zeta Functions*, Journal of Number
   Theory 63(1) (1997), 146–169. This confirms the prior NTNU
   institutional metadata. **Original full text not read.** The article
   cites Hsia's published program as contextual attribution through
   Takehira, not as an invoked theorem or a fully excluded prior result.

The unpublished Silverman 1994 talk is mentioned only as Takehira's
secondary attribution of the definition via Hsia. The talk was not
accessed and has no invented bibliography entry. DOI metadata success
for Hsia is not full-text success. All source comparisons remain
bounded, with no worldwide-priority claim.

## Proof dependencies and deducted ownership

The canonical-height construction, scaling and good-reduction escape
are credited to the established framework. The required specialization
is proved from degrees. Kawaguchi's one-orbit naive-height count and
Takehira's one-variable finite local-discrepancy partition are not used
outside their hypotheses. At equal-degree edges, hhat = 2m while h = m,
so the latter finite-discrepancy shortcut does not hold on the full domain.

Accepted input files (read fully before writing) are
`../../../research_c414_c418/spectral/HEIGHT_PROOF_PACKAGE.md`,
`../../../research_c414_c418/spectral/HEIGHT_SOURCE_AUDIT.md`,
`../../../research_c414_c418/arithmetic/REVIEW_HEIGHT_PROOF.md`, and
the exact diagnostic receipt
`../../../research_c414_c418/spectral/HEIGHT_EXACT_CHECK_REPORT.md`.
The original review's source-precision requests are closed in its final
section. No old source, proof or check was changed or rerun here.
