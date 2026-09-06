# C412 citation metadata and claim boundaries

Checked on 2026-09-06. This is a bounded citation audit for the
article, not a new global-priority search. The sealed
[non-author source review](../../../research_c409_c413/REVIEW_INTEGER_HENON_ROOT.md)
remains the research-admission input. No sealed file was edited or tested.
All five entries in `references.bib` are now cited in the Introduction
or scope discussion. The author-side structural check found five cited
keys, five entries, and no missing or unused entry.

## Verified records and permitted uses

### `silverman1994geometric`

Joseph H. Silverman, *Geometric and arithmetic properties of the Hénon
map*, Mathematische Zeitschrift **215** (1994), no. 1, 237–250.
DOI: [10.1007/BF02571713](https://doi.org/10.1007/BF02571713).
The [publisher record](https://link.springer.com/article/10.1007/BF02571713)
and DOI-negotiated BibTeX agree on these fields.

Permitted role: acknowledge the classical arithmetic-height/finiteness
background, corroborated explicitly by the actually read Ingram and
Kim–Krieger–Postolache–Szeto introductions. Do not claim to have read this
subscription full text, attach an unverified theorem number, or assert
that its unread examples exclude our classification. The article's
elementary proof does not depend on a height theorem from this paper.

### `ingram2014canonical`

Patrick Ingram, *Canonical heights for Hénon maps*, Proceedings of the
London Mathematical Society **108** (2014), no. 3, 780–808.
DOI: [10.1112/plms/pdt026](https://doi.org/10.1112/plms/pdt026).
[Publisher issue metadata](https://academic.oup.com/plms/article-abstract/108/3/780/1571741)
gives March 2014; online publication was 22 July 2013. The DOI BibTeX
returns 2013 from online-first metadata, whereas Crossref's
`published-print` and `journal-issue` fields give 2014. Use the issue year
2014 in the article bibliography, not an unexamined conversion output.

The actual proof-source version is
[arXiv:1111.3609v1](https://arxiv.org/pdf/1111.3609v1), submitted
15 November 2011, the sole listed arXiv version. The opening theorems and
Conjecture 1.5 on printed page 4, plus the relevant computational section,
were read in the admitted source audit; the conjecture and its exact map
were checked again while planning. It concerns
\((y,x+y^2+b)\), determinant \(-1\), not the present determinant \(+1\)
family. Cite the published article with the actual arXiv access version
recorded; do not imply a final-text theorem-number comparison.

### `pezda2002cycles`

Tadeusz Pezda, *On cycles and orbits of polynomial mappings
\(\mathbb Z^2\mapsto\mathbb Z^2\)*, Acta Mathematica et Informatica
Universitatis Ostraviensis **10** (2002), no. 1, 95–102.
The [DML-CZ original-journal record](https://dml.cz/handle/10338.dmlcz/120574)
verifies volume, issue, pages, and title. The linked original PDF cover
verifies the full given name. No DOI was found or invented for this entry.

The PDF was retrieved into a read-only stream and its beginning extracted
with `pdftotext`; no local copy was written. Printed pages 95–96 give the
definitions and Theorem 2.1, with all allowed cycle lengths for arbitrary
integral polynomial maps of the plane and maximum 24. This supplies
background, not an owner for the exact Hénon-family point tables. The
article will not describe the mere existence of a uniform integral
period bound as new.

### `dehenon2024problems`

Julia Xénelkis de Hénon, *Hénon Maps: A List of Open Problems*, Arnold
Mathematical Journal **10** (2024), no. 4, 585–620.
DOI: [10.1007/s40598-024-00252-x](https://doi.org/10.1007/s40598-024-00252-x).
The publisher record and DOI BibTeX verify the collective author form and
metadata; do not replace that published attribution with a guessed list
of authors or editors.

The [journal-hosted full HTML](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html)
was read at Section 11, which credits Patrick Ingram. Its general
number-field questions are broader than this article. Conjecture 3 uses
the opposite determinant sign. Conjecture 4 allows finitely many
exceptional Jacobians, so results at the fixed Jacobian one do not prove
or refute it. Cite this as context, not a claim that the article settles
an open conjecture stated there.

### `kim2025many`

Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and Vivian Szeto,
*Hénon maps with many rational periodic points*, arXiv:2412.01668v2,
8 July 2025. Initial submission was 2 December 2024.
DOI: [10.48550/arXiv.2412.01668](https://doi.org/10.48550/arXiv.2412.01668).
The [arXiv version record](https://arxiv.org/abs/2412.01668v2) verifies all
four names and the version dates. The DOI record uses the initial year
2024; our explicit v2 entry uses 2025 and records the initial year in its
note. The regenerated HTML's displayed 2026 date is not the version date.

The [v2 full HTML](https://arxiv.org/html/2412.01668v2) introduction and
Theorems A–B were read. Their maps have determinant \(+1\); their
polynomials are rational-coefficient integer-valued examples of growing
odd degree. This is relevant contrasting context, not evidence against
the fixed monic quadratic integral-coefficient theorem. No journal
publication is listed in the checked version record, so none is invented.

## Audit method and omissions

Metadata was checked against the primary publisher/arXiv/DML-CZ records,
with real DOI content negotiation for the four DOI entries. The Ingram
date discrepancy was resolved against both the publisher and the raw
Crossref record, not silently normalized from memory. The DML-CZ scan
required a `curl`/`pdftotext` read-only fallback after the browser PDF
parser returned an internal error.

The earlier review also consulted Pezda 2003 and mentioned a 2015 lead.
Neither is needed for this article's precise background comparison, so
neither is padded into its bibliography. Silverman 1994 full text remains
unavailable. This audit did not upload drafts, purchase access, change
external records, or re-run the sealed mathematical checkers. It provides
no global priority guarantee.
