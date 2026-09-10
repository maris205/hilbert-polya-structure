# C431 bounded citation-compliance report

Article: *Haar limits of optimal wild cycles*.
Audit date: 2026-09-09 UTC. Audit target: frozen first-draft source and PDF.
Role: independent citation audit only, not a mathematical manuscript verdict.

## 1. Scope, method, and limits

The applicable repository instructions and batch plan were read. The ARS
academic-paper workflow was used only for its bounded citation-compliance
phase, with its citation-compliance instructions and format-switching
reference read in full. No other persona, intake, or full pipeline was run.
The declared format is an anonymous English mathematics article with a
plain, numbered, alphabetically ordered bibliography. APA/IEEE rules and
generic venue-age quotas were not substituted for that format.

All of `main.tex`, the seven included sections, `references.bib`, and
`SOURCE_BUILD_RECORD.md` were read: 1,059 source/record lines in total.
Every citation occurrence and every bibliography entry was checked.
The author's earlier access record was used as a pointer, not as a
substitute for the primary-source checks described below. Public queries
contained only published titles, identifiers, or public database names;
no private manuscript text was uploaded. No external model API, Git
operation, mathematical program, build, or new agent was used.

The ARS PDF-structure preflight was attempted on the exact frozen PDF.
It returned `UNAVAILABLE` with reason `pypdf-not-installed`, not PASS or
a diagnosis of PDF corruption. Its declared, enumerated, and reader page
counts were null. No package was installed. Separately, `pdfinfo` reported
12 pages, 382,004 bytes, PDF 1.5; `pdftotext -layout` produced 12 page
separators and readable citation/bibliography text. Existing author-created
`inspection/page-11.png` and `inspection/page-12.png` were visually read.
They are supporting renders, not a new structural-integrity certificate.
Accordingly, the primary audit locators below are source file/line and
bibliography label, not certified PDF page anchors.

Per the freeze instruction, only this report was written. All proposed
corrections remain for the coordinator/author. No paper, bibliography,
PDF, baseline, shared record, or evaluation file was edited.

## 2. Summary and zero-versus-unchecked ledger

| Check | Result |
| --- | --- |
| Actual citation commands / reference occurrences | 7 / 7; all are single-key citations |
| Distinct cited keys / bibliography entries | 5 / 5 |
| In-text orphans / uncited bibliography entries | 0 / 0, checked |
| Duplicate bibliography keys / unresolved citation keys | 0 / 0, checked |
| Numbered alphabetical order | Correct: Baker, Hurder–Lukina, Jacobs, Lindahl–Rivera-Letelier, Nordqvist–Rivera-Letelier |
| Version-specific URLs in source and rendered text | 5 / 5 present; all five destinations were accessed |
| Journal DOI fields in source | 4 / 4 present, matching the primary records available below |
| Journal DOIs visible in rendered PDF | 0 / 4; four omissions, finding C431-CIT-1 |
| Major theorem/measure misattributions found in inspected passages | 0; this is not a proof-correctness or worldwide-priority certificate |
| Narrow citation-scope wording correction | 1, C431-CIT-2 |
| Ambiguous lecture-date versus linked-version publication metadata | 1 flag, C431-CIT-3 |
| Full journal retraction-database clearance | UNCHECKED for all 4 journal entries; not a count of zero retractions |
| Identified retraction notices in successfully retrieved article material | 0 observed; materially narrower than clearance |
| Self-citation ratio | UNKNOWN: anonymous authorship prevents attribution; not 0% |
| Self-plagiarism / external similarity corpus | UNCHECKED; no corpus or similarity-service upload used |
| Automatic manuscript corrections | 0, required by the freeze |

Citation-format completion is not certified: the DOI-rendering issue is
open, and the identified wording/metadata flags require author disposition.
No acceptance/rejection recommendation for the manuscript is made.

## 3. Complete citation-occurrence map

All locations are relative to the article directory. The label column is
the rendered bibliography label, not an order-of-first-citation scheme.

| Source locator | Label / key | Claim or locator checked | Disposition |
| --- | --- | --- | --- |
| `sections/1_introduction.tex:28` | [4] `lindahl2016optimal` | Theorem C and its q=1 paragraph: the unique small cycle of each p-power least period, hence distinct orbit points; the optimal-radius formula is in the same introduction | Supported in the pinned v3; see §4 |
| `sections/1_introduction.tex:80` | [4] `lindahl2016optimal` | Problem 1.3, explicitly dated 26 May 2015 | Correct question number, measure family, and stated field/multiplier range |
| `sections/1_introduction.tex:99` | [3] `jacobs2017crucial` | Theorem 2 and introduction's crucial-measure definition | Supported; type-II weighted measures are not uniform selected classical cycles |
| `sections/1_introduction.tex:104` | [5] `nordqvist2020residue` | Theorem 3, periodic-point lower bound | Supported bounded comparison; no broad claim about all later work is inferred |
| `sections/1_introduction.tex:107` | [1] `baker2007berkovich` | Classical seminorm topology | Supported by §1.2 and §§2.3–2.4 of the linked notes |
| `sections/1_introduction.tex:110` | [2] `hurder2025essential` | Author-version §§2.2–2.3, inverse-limit coding and invariant measure | Relevant for minimal equicontinuous Cantor actions; qualify preceding wording as in C431-CIT-2 |
| `sections/5_compact_limit.tex:143` | [1] `baker2007berkovich` | §§2.3–2.4, seminorm topology and Hausdorff analytification | Supported; these are background for the local continuity argument, not a claimed theorem proving the paper's measure limit |

There are no multi-key citations, `nocite` additions, or bibliography
entries serving only as uncited padding. Original argument paragraphs
are not treated as citation-density errors. No sentence contains more
than five citation commands.

## 4. Primary metadata and cited-scope verification

### [1] Baker

The [linked author notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf)
identify Matthew Baker and the bibliography's title. Their opening text
identifies the 2007 Arizona Winter School lectures, while its first-page
footnote records first publication in University Lecture Series 45 (2008).
Thus 2007 is a verified lecture date, not a verified date of the particular
revised PDF; see C431-CIT-3. No DOI for this notes manifestation was
verified. A DOI belonging to a published chapter must not be silently
assigned to this version.

Actually inspected: title/opening footnote, §1.2, §2.3.2 and Theorem 2.3.2,
and §2.4. These supply evaluation-seminorm topology, compact Hausdorff
spectra under the stated Banach-ring hypothesis, and the classical-point
embedding/Hausdorff analytification used at the two citation sites.
The surrounding lecture exposition was not re-proved.

### [2] Hurder–Lukina

The [publisher issue index](https://www.mathsoc.jp/publication/JMSJ/onlineindex/77-1.htm)
confirms *Essential holonomy of Cantor actions*, Hurder and Lukina,
JMSJ 77(1), January 2025, 57–74; its article link is
[10.2969/jmsj/90779077](https://doi.org/10.2969/jmsj/90779077).
The [arXiv version record](https://arxiv.org/abs/2205.06285v2) confirms
Steven Hurder, Olga Lukina, and v2 dated 20 January 2023. Omission of a
middle initial is not treated as a different author.

Actually read in the [v2 text](https://arxiv.org/html/2205.06285v2):
the standing minimal equicontinuous Cantor-action setting, §2.2's finite
coset inverse limit/coding homeomorphism, and §2.3's uniform finite-level
probabilities and Haar pushforward. This supports the relevant classical
background, but not the wording's unqualified extension to every compact
minimal equicontinuous system; see C431-CIT-2. The finite alternative is
proved in the manuscript and is not falsely attributed to this source.
The Project Euclid redirect returned no substantive article text; no
publisher full-proof or publisher-status clearance is claimed.

### [3] Jacobs

The [publisher's indexed article record](https://www.sciencedirect.com/science/article/pii/S0022314X17301312)
gives Kenneth Jacobs, *Equidistribution of the crucial measures in
non-Archimedean dynamics*, JNT 180, November 2017, 86–138, and
[10.1016/j.jnt.2017.02.018](https://doi.org/10.1016/j.jnt.2017.02.018).
This metadata was visible in primary-domain search output; direct article
and accepted-manuscript fetches returned 403. The evidence depth is
therefore narrower than a successfully opened publisher article.

The [actual v2 PDF](https://arxiv.org/pdf/1409.4808v2), dated 28 April 2017,
has the cited title. Its introduction defines the crucial weights to vanish
on types I, III, and IV and depend on reduction at type II; Theorem 2
asserts their weak convergence to the canonical measure. The field setup
does not impose characteristic zero. Both manuscript distinctions are
supported. The [abstract record](https://arxiv.org/abs/1409.4808v2)
retains a different older title; keeping the actual PDF title and explicit
PDF version link is the correct version-aware choice, not a metadata error.

### [4] Lindahl–Rivera-Letelier

The [Cambridge article record](https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/optimal-cycles-in-ultrametric-dynamics-and-minimally-ramified-power-series/83B7D75267327F3D0B76E9E6B47BE8F7)
confirms Karl-Olof Lindahl and Juan Rivera-Letelier, the cited title,
Compositio Mathematica 152(1), January 2016, 187–222, and
[10.1112/S0010437X15007575](https://doi.org/10.1112/S0010437X15007575).
The issue year 2016 is correct; online/copyright dating in 2015 does not
require changing it. The [version record](https://arxiv.org/abs/1311.4478v3)
confirms v3 dated 26 May 2015.

Actually inspected in the [v3 text](https://arxiv.org/html/1311.4478v3):
§1.2's bound (1.4) and its characteristic-p simplification, Problem 1.3,
Theorem C and the following q=1 paragraph. They give the cited optimal
geometry and the exact selected-cycle convergence question over all
complete algebraically closed ultrametric fields of odd characteristic
with 0 < |lambda−1| < 1. The characteristic-zero transcendence condition
in Theorem C is not transferred to this characteristic-p manuscript.
This checks the identity of the problem answered, not the correctness or
priority of the manuscript's answer.

### [5] Nordqvist–Rivera-Letelier

The [LMS/Wiley article record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12325)
confirms Jonas Nordqvist and Juan Rivera-Letelier, the cited title,
JLMS 102(2), October 2020, 470–497, and
[10.1112/jlms.12325](https://doi.org/10.1112/jlms.12325), with first
online publication on 6 May 2020. The [version record](https://arxiv.org/abs/1904.04494v3)
confirms v3 dated 3 February 2020.

Actually inspected in the [v3 text](https://arxiv.org/html/1904.04494v3):
Theorem 3 and its immediate context. Its scope is odd characteristic p,
1 ≤ q ≤ p−1, integral multiplier-one series with first nonlinear
coefficient a nonzero; it bounds norms of nonzero periodic points using
a and the iterative residue. That statement is not a cross-level
selected-cycle contact or measure-convergence theorem. The manuscript's
bounded contrast is accurate; no exhaustive absence claim is verified.

## 5. Proposed correction and flagged-item log

No correction below has been applied to the frozen manuscript.

| ID / priority | Location and original | Proposed author action | Basis / acceptance check |
| --- | --- | --- | --- |
| C431-CIT-1 / required presentation fix | `main.tex:63`; `references.bib:9`, `:20`, `:32`, `:44`; rendered [2]–[5] omit the four declared DOI strings | Keep the required plain alphabetical numbering. Add each journal DOI as a visible `\url{https://doi.org/...}` in its note, or deliberately use a DOI-aware style that preserves this format. Retain all version-specific author URLs. | `plain` does not print these DOI fields. After an author-authorized rebuild, verify all four exact DOI strings and all five existing URLs in extracted and rendered bibliography. Do not claim 4/4 PDF completeness from the `.bib` alone. |
| C431-CIT-2 / minor citation-scope wording | `sections/1_introduction.tex:108`: “compact minimal equicontinuous systems” in the inverse-limit/background sentence | Insert “zero-dimensional” before “minimal,” or explicitly say “minimal equicontinuous Cantor systems” and keep the next sentence's independently proved finite alternative. | The cited Hurder–Lukina sections assume Cantor actions. This is a local attribution qualification; it neither calls for a new theorem nor disputes the paper's included cyclic-partition proof. |
| C431-CIT-3 / metadata ambiguity, author disposition | `references.bib:48` onward; [1] labels the notes only “2007” | Retain the lecture-notes manifestation if intended, but clarify in the note that these are 2007 AWS lectures and the linked PDF records first publication in ULS 45 (2008). If switching to the published chapter, verify its own complete metadata and section numbering before changing entry type/year/DOI. | The actual linked PDF contains both dates with different meanings. This is not an instruction to replace 2007 blindly or to invent chapter metadata. |
| C431-CIT-4 / incomplete external-status check | Journal entries [2]–[5] | Before a claim of retraction clearance, query an accessible current Retraction Watch dataset by each original DOI and title, and inspect any returned notice or publisher update record. | Current bounded access did not yield a searchable database; details in §6. Preserve UNCHECKED unless that follow-up is actually performed. |

The four DOI suffixes for C431-CIT-1 are respectively
`10.2969/jmsj/90779077` [2], `10.1016/j.jnt.2017.02.018` [3],
`10.1112/S0010437X15007575` [4], and `10.1112/jlms.12325` [5].
Plain-style URL punctuation/line wrapping, full author names, and
alphabetical numbering are not APA or IEEE violations to be corrected.

## 6. Retraction/status access and informative ethics checks

The [Retraction Watch search interface](https://retractiondatabase.org/RetractionSearch.aspx)
failed with a redirect loop. [Crossref's public access documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/)
identifies its full public CSV route; the
[dataset repository](https://gitlab.com/crossref/retraction-watch-data)
loaded only its project shell. The
[raw CSV](https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv)
fetch failed because its reported content length, 66,466,306 bytes,
exceeded the browser limit. The prohibited API route was not used.
Search-engine non-hits were not converted into database-negative results.

| Journal reference | Successfully retrieved primary status material | Exact disposition |
| --- | --- | --- |
| [2] Hurder–Lukina | Publisher issue listing and DOI redirect; article body/status unavailable | Retraction database and article-status clearance UNCHECKED |
| [3] Jacobs | Primary-domain indexed metadata; direct article/accepted-manuscript pages 403 | Retraction database and article-status clearance UNCHECKED |
| [4] Lindahl–Rivera-Letelier | Cambridge article metadata/abstract; no article-specific retraction notice observed in retrieved text; no actionable article-status certificate exposed | Retraction database and complete update-status clearance UNCHECKED |
| [5] Nordqvist–Rivera-Letelier | LMS/Wiley article metadata/abstract; no retraction notice observed in retrieved text; no Crossmark status supplied | Retraction database and complete update-status clearance UNCHECKED |

Baker is a notes entry, not one of the four journal entries requested
for this protocol; no global withdrawal-status clearance is inferred.
The statement “0 retracted references” is not warranted by this audit.

Source currency is descriptive only. Using the declared bibliography
years and the 2021–2026 calendar-year window, 1/5 entries (20%) is recent;
the 2007 notes and January 2016 original problem article are more than
ten years old at audit time. Both are foundational/original-source uses,
not age-policy failures. A date clarification for [1] does not change
that conclusion. No modernity quota or speculative reference padding
is recommended.

Anonymous authorship leaves the numerator for self-citation unknown.
No author-identifying self-citation language or unpublished companion
bibliography entry was found, but this cannot establish a 0% self-citation
ratio. No author identity was sought. No prior-publication corpus was
provided for self-plagiarism screening. The local preparation statement
does not present internal team review as external peer review or
publication. The scope statement expressly avoids worldwide-firstness.

## 7. Frozen input identity and handoff

SHA256 values were independently computed from the actual files, not
merely copied from the build record. All nine source files equal their
`baseline/src/` counterparts byte for byte. The source/build record
equals `baseline/SOURCE_BUILD_RECORD.md`. All three PDF copies have the
same required hash. Source hashes were rechecked before handoff.

| Input relative path | SHA256 |
| --- | --- |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `sections/1_introduction.tex` | `d9e36e1bb5239457a6a8e3c32a47217ce8b25b8f340505000718c191198f1c34` |
| `sections/2_coefficients.tex` | `b5eb44fc34ee02d951855ae51989d0b329f85e4ead8b79bd100b67eeeaaa34f8` |
| `sections/3_displacements.tex` | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `references.bib` | `5e0975227644cc458dbf3d40e011f4a11cb9c0d76819f3043cc39f6bcc730bf2` |
| `SOURCE_BUILD_RECORD.md` | `a6559476e391193f64454fff0d016299b0259723fbc30530bbf6eecb915065af` |
| `main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `baseline/main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `main_round0_original.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `inspection/page-11.png` | `e50d947ae6f6a7e92ad2eb5b8c76591150f5389a654be94760971c08ab586965` |
| `inspection/page-12.png` | `7bc0b91097da061b5125b909144978dfa06136844b96afd5eebf3a1abfe7a792` |

The bounded citation audit is complete and this report is frozen for
coordinator/author disposition. Completion refers to the performed
audit, not resolution of the listed corrections, retraction clearance,
structural PDF certification, or manuscript-review acceptance.
