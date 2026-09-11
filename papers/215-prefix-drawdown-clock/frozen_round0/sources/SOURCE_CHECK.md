# P215 primary passages and bibliography verification

2026-09-11 UTC. These are direct author lookups, separate from the earlier
candidate gate's source check. Only the two cited works were included.
No manuscript was uploaded and no external review or contact was requested.

## Bibliographic resolution

| Citation key | Primary metadata checked | Resolved entry |
| --- | --- | --- |
| goldberg2017drawdown | [Springer article landing page](https://link.springer.com/article/10.1007/s11579-016-0181-9), title/authors, volume/pages and Cite this article/Issue date | Lisa R. Goldberg and Ola Mahmoud; Mathematics and Financial Economics 11(3), 275–297, 2017; DOI 10.1007/s11579-016-0181-9 |
| pemantle2009barrier | [EJC article page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r60), authors, publication date, How to Cite and article number | Robin Pemantle and Herbert S. Wilf; The Electronic Journal of Combinatorics 16(1), R60, 2009; DOI 10.37236/149 |

Actual DOI content-negotiation requests used `Accept: application/x-bibtex`
for the two exact DOIs. They returned bibliographic records, not scientific
program output. The returned fields agreed on names, titles, journal,
volume, issue and DOI. The drawdown response uses `year={2016}` and
`month=Sept`, while Springer explicitly states online publication on
28 September 2016, volume 11/pages 275–297 (2017), and issue date June
2017. references.bib uses the journal-issue year 2017 and omits the online
month. The EJC response has no pages/article-number field; R60 is added
from the journal's own How to Cite field. Only these disclosed
normalizations, citation-key naming and ordinary BibTeX formatting were
applied. No field was guessed.

Source observations: native bibliographic response chunks e70ffe and
7df372 both exited zero. Web views turn11141view0 and turn11140view1
supplied the publisher/journal metadata. These identifiers locate actual
conversation observations; this document is an author record, not a
byte-exact capture of the HTTP bodies. No full source PDF is bundled.

## Exact passage scope

- [Goldberg–Mahmoud arXiv PDF](https://arxiv.org/pdf/1404.7493), printed
  p. 5, Definition 2.2: one-step drawdown definition only. The selected
  passage was directly read during author proof preparation; the root
  separately reread it at admission. The article's stochastic/financial
  conclusions are not used in the proofs.
- [Pemantle–Wilf arXiv PDF](https://arxiv.org/pdf/0905.0609), printed
  pp. 1–5, definitions and Theorem 1/combinatorial proof: attribution for
  upper-barrier counting. Our first-violation recurrence is proved locally,
  not attributed as a verbatim formula from that source. No priority
  statement about all possible recurrences is made.

The selected bodies, not merely abstracts or metadata, support those
attributions. These are bounded passage reads; neither complete-paper
reading nor a frozen source archive is claimed. The manuscript contains
no direct quotations or empirical borrowing from either work.

## Retrieval limitations preserved

The web DOI opening for the drawdown item returned a non-retryable safety
fetch error. Opening the explicit Springer article URL succeeded.
The EJC BibTeX download through the web tool was refused as an unsupported
application/x-bibtex response. The separate explicit DOI content-negotiation
requests succeeded. The earlier Berkeley 2015-04.pdf HTTP 502 failure is
disclosed in the author scout; the arXiv source body had succeeded.
None of these failures is represented as a source read.

The lookup process used the paper-writing skill's verified DOI fallback,
with published metadata resolving its ambiguous online/issue year.
No automatic reference client, scientific import, JSON parser, bibliography
engine or LaTeX engine ran. Bibliography resolution is not a PDF build.
