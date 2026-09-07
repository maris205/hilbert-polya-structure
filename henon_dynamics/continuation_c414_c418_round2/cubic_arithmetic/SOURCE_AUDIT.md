# Bounded primary-source audit: monic integral conservative cubics

Checked 2026-09-06 UTC. ARS contribution: source-verification/fact-check only.
The theorem/proof and admission decisions are separately owned by the batch
workflow. This is neither a systematic review nor a global-priority claim.

## Exact comparison

The scout concerns every $H(x,y)=(y,f(y)-x)$ with
$f(t)=t^3+bt^2+ct+a\in\mathbb Z[t]$, on all $\mathbb Q^2$, in ordinary
time. The proposed independent increment is the complete cycle-template
classification, least periods $1,2,3,4,6$, the sharp eleven-point bound,
and its unique integer-translation equality locus. Existence of some
uniform bound, monic integrality, height finiteness, and word interpolation
are not claimed as new. The cubic secant root and global coexistence
closure must carry the increment.

## Primary sources and actual access

| Source | Verified record / actual text read | Claim fitness and exact boundary |
|---|---|---|
| Tadeusz Pezda, *On cycles and orbits of polynomial mappings $\mathbb Z^2\mapsto\mathbb Z^2$*, Acta Mathematica et Informatica Universitatis Ostraviensis 10 (2002), no. 1, 95–102 | [Original-journal DML-CZ record](https://dml.cz/handle/10338.dmlcz/120574); linked original PDF, cover and printed pp. 95–96, definitions and Theorem 2.1. Browser PDF access timed out; a read-only `curl` → `pdftotext` stream succeeded. No local PDF was written. No article DOI found or invented. | Primary theorem, grade A for the stated general integral-map period bound. It gives the full general set $\{1,2,3,4,6,8,9,12,16,18,24\}$. It is not a sharp total-periodic-point theorem for the fixed cubic Hénon family. The cubic proof below does not use it as an unproved black box. |
| Patrick Ingram, *Canonical heights for Hénon maps*, Proceedings of the London Mathematical Society 108 (2014), no. 3, 780–808 | [Publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/pdt026), [DOI](https://doi.org/10.1112/plms/pdt026), and actual [arXiv:1111.3609v1 PDF](https://arxiv.org/pdf/1111.3609v1), introduction, Theorems 1.1–1.4, Conjecture 1.5, Proposition 1.6, and opening local-height definitions/Lemma 2.1. This is selected-section access, not a full-paper reading. | Primary proof source, grade A for the accessed height/specialization context. Its detailed quadratic conjecture uses $(y,x+y^2+b)$, determinant $-1$. Its introduction explicitly credits earlier boundedness results to Pezda. No new finiteness claim or resolution of its rational-coefficient conjecture is asserted. |
| Julia Xénelkis de Hénon, *Hénon Maps: A List of Open Problems*, Arnold Mathematical Journal 10 (2024), no. 4, 585–620 | [DOI](https://doi.org/10.1007/s40598-024-00252-x) verified by content-negotiated metadata; actual [journal-hosted full HTML](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), Section 11 attributed to P. Ingram, including interpolation, Question 46 and Conjectures 2–5. | Primary statement of the questions, grade A for what those questions say, not evidence that a conjecture is proved. General rational-coefficient uniform boundedness is broader; Conjecture 3 has the opposite determinant sign and Conjecture 4 permits exceptional determinants. |
| Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache and Vivian Szeto, *Hénon maps with many rational periodic points*, arXiv:2412.01668v2, 8 July 2025 | [Version record](https://arxiv.org/abs/2412.01668v2), [DOI](https://doi.org/10.48550/arXiv.2412.01668), and actual [v2 HTML](https://arxiv.org/html/2412.01668v2), introduction/Theorems A–B and Section 2.2 polynomial definitions. Selected sections were read. | Primary preprint, grade B for comparative context; publication beyond arXiv not asserted. Its determinant is also $+1$, but the polynomials are rational-coefficient integer-valued examples of growing odd degree. In degree three its displayed definitions give $s_3(t)=(t^3-7t)/6$, not a monic integral-coefficient polynomial. The old admitted all-odd discrete-sine classification remains separate and frozen. |

Mathematical proof/source fitness replaces the inapplicable clinical
study-design pyramid. Foundational sources are not downgraded merely for
age. These records and actual theorem text provide appropriate evidence
for the exact comparisons. No Scopus/Cabell/COPE subscription check, human
read attestation, exhaustive retraction investigation or formal COI
clearance was performed or implied. No predatory-venue red flag appeared
in the accessed primary records; absence of a flag is not a comprehensive
venue certification. Ingram reports NSERC support and the Kim et al.
acknowledgements name the Cambridge summer/internship support. Funding is
not treated as mathematical proof, disproof or a discovered conflict.

## Existence verification and date cautions

DOI browsing encountered safe-open/redirect errors for three DOI URLs.
Read-only `curl -L` content negotiation returned matching BibTeX with HTTP
200 for all three. The returned Ingram year is online-first 2013; the
publisher explicitly identifies the March 2014 issue. The arXiv DOI year
2024 is initial deposit; the cited v2 date is 2025. Regenerated arXiv HTML
or PDF internal date stamps are not substituted for version dates.

Semantic Scholar was actually queried without sending manuscript text:

| Reference | Result |
|---|---|
| Kim et al. | Two HTTP 429 responses, then a matching title/authors/arXiv-id record, paperId `b48a8897f4e89ff33440402dd2ae0ee8b2053072`, year 2024, consistent with initial deposit. |
| Ingram | DOI lookup returned paperId `317246577ac0b5e8a4ae364909512f10ca173a3d`, matching title/author/arXiv/DOI but year 2011. This is a preprint-year merge, not independent confirmation of the journal issue year. Publisher/DOI metadata resolves the publication record. |
| de Hénon | DOI lookup returned paperId `883d4276fd99386ee1eac5a077aaa9855ac98894`, matching title/collective author/DOI, year 2023 from the associated preprint. The 2024 journal year is independently verified through the publisher DOI record. |
| Pezda | Title-search calls were rate-limited; DML-CZ record and the original scanned article establish existence. No Semantic Scholar identifier or successful API match is invented. |

No journal-year mismatch is silently labeled a complete S2 verification.
The exact statements about the wider uniform-boundedness question are
cross-checked against Ingram, the journal question list and Kim et al.;
Pezda's exact numerical set is attributed to its own primary theorem, not
to secondary summaries. No claim needs fabricated extra sources.

## Search and repository collision record

The installed tool inventory had no Zotero/Obsidian research connector.
The new batch's local filename check found no relevant local paper cache;
unrelated symbolic-stream PDFs were not read. Official-source browsing
was the fallback. Bounded searches included:

1. `"cubic" "Hénon" "rational periodic points"`;
2. `"monic" "integral" "Hénon" "periodic"`;
3. `"Hénon maps" "uniform bound" "integral"`;
4. `Ingram Henon maps integral periodic uniform bound good reduction`;
5. `cubic Henon integer cycles periodic points monic rational arithmetic`;
6. `Pezda "Cycles of polynomial mappings" Z2 24`;
7. `"monic" "cubic" "Hénon" "eleven"` and
   `"conservative" "cubic" "rational periodic"`.

The last exact searches returned no relevant new owner in the accessed
results; that is a bounded search outcome, not proof of global novelty.
Search-result snippets, secondary review sites and unrelated Hénon–Heiles
results do not support the theorem or ownership conclusions.

Targeted local comparisons read the C412 registry/obstruction entries,
its introduction/classification and citation audit, and located the older
odd-cubic finite scout in the C409–C413 nonlinear report. C412 already
owns the complete monic integral conservative *quadratic* classification,
including sharp eight points and its equality locus. Its integrality,
coordinate-word encoding and finite-complement methodology are deducted.
The present cubic reduction instead uses an integer third secant root,
three-branch coexistence, all-parameter short-cycle templates and the
sharp eleven-point equality locus. This difference is a proposed bounded
independent increment subject to nonauthor proof/source review, not an
admission decision. The older odd-cubic finite parameter check was
explicitly deferred and is not recast as an earlier proof.

No old file, theorem check, formal evaluation or PDF build was altered or
rerun. No external model API, paid access, external write, inquiry ledger
or full research-pipeline runtime was activated.
