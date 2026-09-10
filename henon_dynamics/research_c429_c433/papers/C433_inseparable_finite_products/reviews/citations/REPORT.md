# C433 citation audit: frozen first-manuscript baseline

## 1. Disposition and role boundary

**No Critical or Major citation finding. One Minor metadata-normalization
recommendation is recorded below. Public retraction screening is incomplete:
the database lookup was unavailable, not negative.**

This is the allocated independent citation audit of the actual C433 manuscript,
not a mathematical review, novelty review, publication decision, or clean
integrity certificate. Observations were made on 2026-09-09 UTC, using the
actual tool clock, after the first baseline was frozen.

I fully read the relevant repository AGENTS files, SCOUT_PLAN, BATCH_PLAN,
the ARS router, academic-paper WORKFLOW, citation_compliance_agent, and
citation_format_switcher. ARS was used only in its bounded citation role.
The explicit format is an anonymous English mathematics article with a plain,
alphabetically ordered, numbered bibliography. No APA/IEEE conversion,
literature-age quota, full intake, Material Passport, or pipeline gate was run.
The freeze overrides the role's generic auto-correction instruction: all
proposals go to the coordinator/author; no manuscript bytes were edited.

I previously performed the R10 source/substance comparison and had already
read the underlying proof. This audit is not blind to that history. Its
claims below nevertheless come from a new comparison against the actual
manuscript, generated bibliography, and accessible primary records.

## 2. Exact input and actual read extent

Fully read: main.tex (63 lines), all eight section files (54, 107, 114, 95,
146, 115, 61, and 33 lines), references.bib (31), SOURCE_AUDIT.md (91), and
BUILD_RECORD.md (115): **1,025 source/record lines in total**.

Also inspected: the complete generated build/third/main.bbl; all citation and
bibliography mappings in main.aux; the PDF's four rendered citation passages,
References text, and development/ownership passage; its three external URI
annotations; and pdfinfo. The PDF is 11 pages and 374,341 bytes. This was not
an independent all-page visual or full PDF-proof review. Findings use source
file/line locators, not certified local-PDF page anchors; no structural
preflight or all-page visual PASS is claimed.

Every file listed below was hashed, and each current file was compared with
its exact snapshots/v1_baseline counterpart by cmp. All **14 comparisons
returned exit 0**, including both PDF names. The two PDFs have the same hash.

| Current file, matched to the same baseline-relative path | SHA-256 |
| --- | --- |
| main.tex | a8bc69d20c0e71385fbaed7e3a9c16987226af49b49d60142a407cbe5ee16dbf |
| sections/01_introduction.tex | 057a027bfd646613a80dcdd9f1375f7ffa061d39d9664ddec2486dddae10f682 |
| sections/02_statement.tex | 3d6d5d65a715adb9a0c98f6257ab4f122491f02e81d9ff6e7458c8a0217b9f2a |
| sections/03_cycles.tex | 49bccc2a0ba02bb8634b78cdc69cd38fa217691db0df7df27ea4ab47e6f2486c |
| sections/04_extractor.tex | 20fc9ff6342288314cd71efcbdc1f9388455245b8186bf749809c103e662cb69 |
| sections/05_transfer.tex | d56317d4ec6ad9375b564472a48564fbeef60c314e4e533d2671fc94d891769e |
| sections/06_rank.tex | 53141c1b73f968333b4af2c180c678a50967df211c78f8190d95935b254fcc88 |
| sections/07_decision.tex | 88b84763f2ab5919de79d8d31b73ff40f6cfd06664b03e308dfb01c6b9477f4c |
| sections/08_conclusion.tex | d3b4d85628883a31ada3e68e211528cdf70ac9350f3d453128e3195a178d8ffb |
| references.bib | 89c47eaeca9645bc2579504a9edb789f5ef6225d67b868da13b07ece4f44d128 |
| SOURCE_AUDIT.md | fc5a379ed7889cb256aa0195e4b95988f3445a6446ad5c9238a3c8c77687104c |
| BUILD_RECORD.md | e1e865cb14033b81014b0c93281cc3c4c65e0f0eff347580ab30022dc21069bc |
| main.pdf and main_round0_original.pdf, separately compared | 8e58c361b89fe132183451f08b4817699ac02164e224a8cc6589d62e3bdb99f7 |

## 3. Complete citation index and rendered identifiers

The full-source scan found four cite commands, no nocite command, and exactly
two bibliography entries. The auxiliary file maps CDS1996 to [1] and
Kiefer2013 to [2]. Both entries occur twice; there are zero orphan citations,
zero uncited bibliography entries, and zero unresolved citation keys.

| Source location | Citation/mention | Attributed role | Result |
| --- | --- | --- | --- |
| sections/01_introduction.tex:26–29 | Cattani, Dickenstein, Sturmfels; CDS1996 | Classical normal forms/residues; specifically Section 4 of the preprint | Matches the named source and version |
| sections/01_introduction.tex:32–36 | Kiefer et al.; Kiefer2013 | Arbitrary-field Section 3/Proposition 3.1; no Gram or complexity import | Matches the actual proposition |
| sections/04_extractor.tex:92–95 | CDS1996, Section 4 of the preprint version | Context for a directly proved algebraic extractor | Scope boundary is explicit |
| sections/05_transfer.tex:127–130 | Kiefer2013, Proposition 3.1 | Classical finite-word principle behind the included span proof | No attribution of the dynamics-specific cutoff to Kiefer |

The generated References text prints the two correct titles, author sequences,
years, venues, and identifiers, subject to the minor accents issue below.
The Q in the second title remains mathematically typeset. Numbering follows
the selected plain alphabetical style, not an inferred IEEE style. Ordinary
bibliographic punctuation after a linked DOI is not treated as an APA error.

The PDF annotations contain exactly these three external targets:

1. https://doi.org/10.1007/978-3-0348-9104-2_8
2. https://arxiv.org/abs/alg-geom/9404011
3. https://doi.org/10.2168/LMCS-9(1:8)2013

The displayed DOI strings match those targets; the first underscore is
correctly rendered. The explicit note fields make the identifiers visible
even though plain.bst does not itself render arbitrary doi/url fields.
Both cited publications have their publication DOI included. A separate
DataCite DOI for an already identified arXiv version is not a missing
publication DOI or an additional orphan reference.

## 4. Primary metadata, versions, and attributed content

### 4.1. CDS1996

The [Springer chapter record](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8)
confirms the three authors, title, 1996 publication, book title, Progress in
Mathematics 143, pages 135–164, Birkhäuser Basel, editors Laureano
González-Vega and Tomás Recio, and DOI 10.1007/978-3-0348-9104-2_8.
The manuscript matches except for the two editor accents. The direct DOI
resolver retrieval failed, but the publisher's DOI-bearing chapter page was
read successfully; DOI identity is verified, live resolver success is not.

The [arXiv record](https://arxiv.org/abs/alg-geom/9404011) identifies v1,
submitted 27 April 1994. The accessible [primary preprint](https://arxiv.org/pdf/alg-geom/9404011)
was reread for its setup, Lemma 1.5/proof, Remark 1.6(iii), and all of Section 4
through Theorem 4.9/proof. Section 4 explicitly connects top normal-form
coefficients, residue pairings, and finite quotient traces. The initial field
is a subfield of C; the remark discusses extending that section to other
fields via deformation methods. The manuscript correctly gives its own
positive-characteristic argument and uses this source as context. Its
locators say preprint Section 4, not an unverified published section/page.

The paywalled publisher PDF was not read. The arXiv abstract's historical
27-page comment differs from the current PDF parser's 30-page count; neither
count is misrepresented as the published chapter's pagination in C433.
No claim of byte identity between the preprint and chapter is made.

### 4.2. Kiefer2013

The [LMCS record](https://lmcs.episciences.org/908) and actual
[publisher BibTeX export](https://lmcs.episciences.org/908/bibtex) confirm the
five authors, title, journal, volume 9, issue 1, article 8, 2013, and DOI
10.2168/LMCS-9(1:8)2013. The DOI resolves to that record. The exported volume
string was appropriately normalized in the manuscript to 9(1:8); this is not
a fabricated issue. The article's title page confirms pages 1–22.

The [arXiv record](https://arxiv.org/abs/1302.2818) identifies v2 dated
1 March 2013 and links the same journal publication. After the LMCS download
timed out and the older author-PDF host failed, the current
[arXiv v2 primary PDF](https://arxiv.org/pdf/1302.2818v2) was read directly:
title page, Section 3 setup and Proposition 3.1, and Section 4.1 including
the complete Theorem 4.2 proof. Proposition 3.1 is explicitly over any field:
short reachable words span the reachable space, with a nonzero witness of
length at most n−1 for an n-state representation. It credits its own
reference [28]; C433 does not assert that Kiefer originated the principle.
The later Gram-kernel step is rational-field specific. C433 instead proves
its matrix-span step and evaluation-rank arguments directly, so the field
distinction is accurately retained.

The primary cover prints article 08, while the publisher's registered DOI
and export use article 8. Keep the verified DOI already in C433; do not
replace it by an unverified zero-padded DOI spelling.

## 5. Raw findings, severity, and proposed correction log

**Applied corrections: zero.** All files and baseline copies remain frozen.

| ID / severity | Exact observation | Proposed action and consequence |
| --- | --- | --- |
| CIT-M01 / Minor metadata normalization | references.bib:5 and the generated [1] print Gonzalez-Vega and Tomas; the publisher records González-Vega and Tomás | At an authorized revision, restore the two accents. This does not change source identity, theorem applicability, DOI, ordering, or mathematics. |
| CIT-I01 / Informational name variant | The primary Kiefer title page and its same-author precursor use Joël; current LMCS metadata/export use Joel, as does C433 | Joël may be restored for full-name typography consistency, but the publisher itself supplies Joel. This is not a wrong-author or misattribution finding. |
| CIT-I02 / Screening limitation | No successful Retraction Watch database query was obtained | Preserve the incomplete-screening disclosure in Section 6; do not label the bibliography retraction-free. |

For CIT-M01, the proposed BibTeX field is:

```bibtex
editor = {Gonz{\'a}lez-Vega, Laureano and Recio, Tom{\'a}s},
```

If the author chooses the optional CIT-I01 normalization, use
`Ouaknine, Jo{\"e}l`. No other bibliographic field or citation wording needs
correction on the evidence inspected here. These are recommendations to the
coordinator, not permission for this auditor to unfreeze the manuscript.

Both sources are foundational mathematics/automata literature; no recency
quota is applicable. Author identities for the anonymous C433 manuscript are
not supplied, so a self-citation ratio or self-plagiarism clearance cannot be
determined. No plagiarism service, proprietary database, or external upload
was used. The proof's own deductions do not require a citation on every line.

## 6. Retraction, correction, and public-status screening

The [Retraction Watch user guide](https://retractionwatch.com/retraction-watch-database-user-guide/)
was read, and both its database link and the direct RetractionSearch.aspx
entry were attempted. The direct entry returned a redirect loop; the linked
entry also failed. Therefore **RWDB screening is unavailable**, not a
successful zero-result database search. The guide also warns that its
corrections/expressions-of-concern coverage is not comprehensive. No database
dump was downloaded and no bibliographic API was called.

Supplementary bounded public screening consisted of the two current
publisher pages, the two arXiv records, and one four-query notice batch:

- Each exact publication DOI with retraction/retracted/corrigendum/erratum/
  expression-of-concern terms.
- Each exact title with a Retraction Watch site restriction.

The returned results did not identify a relevant notice for either cited
publication. Neither parsed publisher record displayed a retraction notice.
This observation is not a complete correction/retraction clearance.

Two apparent signals were examined rather than silently discarded:

1. The LMCS text extractor displays “Detected problematic reference”. Raw
   public HTML inspection located it inside the element
   `id="biblio-ref-legend-public" hidden`, a bibliography legend. It is not
   an article-level status notice. No dynamic citation API was queried.
   [Actual publisher page](https://lmcs.episciences.org/908)
2. The arXiv/LMCS record carries a same-author text-overlap note. The linked
   [2011/2012 precursor record](https://arxiv.org/abs/1112.4644) identifies
   a FoSSaCS technical report, and the 2013 primary title-page footnote
   explicitly discloses the expanded conference-version relationship.
   This is not a retraction finding or a basis for alleging misconduct.
   [2013 version and disclosure](https://arxiv.org/pdf/1302.2818v2)

Transient access failures are not concealed: the LMCS BibTeX direct open
initially failed but succeeded by the publisher's actual export link; the
LMCS PDF timed out; the older author PDF failed; an attempted public-PDF
screenshot failed. Primary text was recovered through arXiv, not by claiming
those failed reads succeeded. The Springer chapter's full paywalled PDF and
a successful Retraction Watch database result remain unchecked.

## 7. Ownership and final handoff

The source citations are bounded to classical context. The manuscript's
Sections 4–7 contain its own extractor, state contraction, word-span proof,
split evaluation rank, persistence argument, and final finite decision.
The development paragraph in sections/08_conclusion.tex:22–33 explicitly
credits the preceding internal work and coordinator's sketch/constants.
No unpublished working-note ID is passed off as published literature, and
no new theorem is delegated to an untyped external dependency.

This audit therefore finds no citation-based reason to reject the manuscript's
stated source/field/ownership boundaries. It does not replace the two assigned
manuscript reviews, adjudicate mathematical correctness, guarantee novelty,
or certify readiness, external peer review, acceptance, or release.

Only this assigned report was created. No source, bibliography, PDF, snapshot,
build, shared record, evaluator, Git state, or external publication was changed.
No mathematical computation, new agent, model/API call, credential action, or
manuscript upload was performed. The raw observations and optional correction
proposal are handed back to the coordinator with the baseline preserved.
