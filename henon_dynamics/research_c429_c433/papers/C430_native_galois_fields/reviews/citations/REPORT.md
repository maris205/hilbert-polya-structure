# C430 frozen-manuscript citation audit

Audit date: 2026-09-09 UTC (actual session clock; public sources accessed
during this audit). Scope: bounded, independent ARS `citation-check`,
academic-paper Phase 5a. This is a citation report, not a mathematical
peer-review verdict, originality guarantee, release seal, or ARS full-pipeline
certification.

## Result

The frozen manuscript has **nine references, fourteen citation occurrences,
and zero citation orphans in either direction**. Its numbered, alphabetically
ordered mathematical bibliography is consistent with the author-confirmed
`plain` style. No source/result mismatch was found in the cited statements
and selected proof passages checked below.

**Four entries require metadata or rendered-identifier repairs:** [3], [4],
[5], and [7]. In particular, Elder--Keating now has a published journal
version, and `plain.bst` does not print the DOI fields already present in the
BibTeX database. No correction has been applied to the frozen manuscript.
All proposals below are for the coordinator/author to adjudicate and apply.
Retraction-database verification remains unavailable; partial primary-page
status checks are not represented as comprehensive clearance.

## Authority, inputs, and actual reading

The repository and Hénon/batch `AGENTS.md`, relevant current-state entry,
`SCOUT_PLAN.md`, and complete `BATCH_PLAN.md` were read. The full ARS router,
academic-paper workflow, citation-compliance role, and citation-format
switcher were read. The explicit citation-only/frozen-source assignment
overrides the role's default automatic draft correction. The selected style
is mathematical numbered/alphabetical `plain`, not IEEE or APA. No
machine-learning reference-age quota or external-model workflow applies.

The complete actual C430 sources were read: `main.tex`, `math_commands.tex`,
all nine section files, and all of `references.bib` (1,462 lines in total),
plus the complete 171-line `SOURCE_BUILD_RECORD.md`. The source files compare
byte-for-byte with `baseline/src/`; `main.pdf` compares with
`baseline/main.pdf`. The supplied frozen PDF and build-record hashes match.

The corrected author-build `main.bbl` and all citation/bibliography records
in its `main.aux` were checked against the source. Fresh read-only
`pdftotext -layout` output from the actual frozen PDF confirms all nine
rendered bibliography entries and the identifier omissions. The two existing
bibliography-bearing JPEG renders were also viewed; identifiers are legible,
and the missing DOIs are genuinely absent rather than extraction artifacts.
The PDF is 18 pages and 404,880 bytes. This audit did not rebuild, perform
all-page visual QA, or validate a new PDF-reading preflight sidecar. Findings
therefore use source locators and reference numbers, not certified PDF page
anchors. The author's all-page/build claims remain the author's receipt.

### Frozen input binding

Paths below are relative to the C430 manuscript directory.

| Input | SHA256 |
| --- | --- |
| `main.pdf` | `54bc61f0d9c89405047fdf116bbcaf38d9e658c6d401b70862b22659f2574c8e` |
| `SOURCE_BUILD_RECORD.md` | `5f022836036b81e2e79b2cf4bc3100e9ae8891ef1b53e4df3c9700ff652a0957` |
| `main.tex` | `64726ac4156c5f58f7012373b0e00497bf36ea3465c7f664d46292749ca39669` |
| `math_commands.tex` | `09ce6cb709b396eef06067e872ed648bc5f4f4295c2c80200e2f4ccc4b298cdd` |
| `references.bib` | `9bb44aae6ffbd524fd24c6567df1bc7ab671fd7f11ea5a62031c35496f1bfcaa` |
| `sections/00_abstract.tex` | `4190fecbf742de602c4a6a1f9add60df97350f4922fe77a0c0bce5e8a63c8189` |
| `sections/01_introduction.tex` | `83859269616b6fc2d58ab8b22729b862c1cb9bbe49ab87ece564567086d2eefb` |
| `sections/02_local_setup.tex` | `6072b59c61c9583e035b9363c63e7889858b9ba127a8fa33024c036672f57ff6` |
| `sections/03_second_layer.tex` | `f65985674292b57f6cbe52ea2c407394e785fb1d9224dbe8829d9990a811204f` |
| `sections/04_full_inertia.tex` | `9f40a4775383c07dd4a4ecc8733f9ffbb235f1215ab26f02be60a62099fd298c` |
| `sections/05_oriented_quotients.tex` | `8cc49232529207fcbec1ff90f73ef9fe5cd5ca8a9e7049785355f47e7034d284` |
| `sections/06_ramification.tex` | `28d77c6548a8e8780ed56750cdea277b536cd2bbb3147a3abc6ef8c0fe3ea77c` |
| `sections/07_eventual_tower.tex` | `4873ac52d5dedee20ec4443d480d86bfdaf306e2dbcbef3d365c5e88a4a19b43` |
| `sections/08_scope.tex` | `026bdee1dd9bc96e3835c6ec038495cbbd4854ed3e178b95f5ee31ba37e999f2` |
| `qa/author_build_02/source/main.bbl` | `b3adc564b36ad0aff98b7c6f0524202ec5ecb2073e79facc5c94f94d9e9027cf` |
| `qa/author_build_02/source/main.aux` | `560e717157b8d5bcd4ec95b1b41fed6dd598fc8d4525b92f18ebcc69422cc11d` |
| `qa/author_build_02/pages/page-17.jpg` | `d2b853698a87d6fd0533d0b698ee3f0ccd1c9b38ac4ce369195222bf9986e5d2` |
| `qa/author_build_02/pages/page-18.jpg` | `412fcfb684fb9a7d0affb2696ff52d135e2dc5dcab069b641ac987c0ca5ea9b5` |

The build-source PDF itself has the same hash as the frozen `main.pdf`.
No old mathematical proof/review file was changed or reclassified as a
review of this manuscript.

## Complete citation inventory

Locations use section-source basenames and line numbers in the frozen input.
The occurrence count is of citation commands, not repeated PDF hyperlinks.

| Ref. / key | Occurrences | Actual locations | Cross-check |
| --- | ---: | --- | --- |
| [1] `companion2026haar` | 3 | `01_introduction:108`; `07_eventual_tower:35–36`; `08_scope:33` | Present in BibTeX, BBL, AUX and rendered references |
| [2] `conradcompletion` | 1 | `07_eventual_tower:11` | Present in all four |
| [3] `debaisieux2026lubin` | 1 | `01_introduction:146` | Present in all four |
| [4] `elder2025artin` | 2 | `01_introduction:150`; `02_local_setup:139` | Present in all four |
| [5] `keating2006extensions` | 1 | `01_introduction:128`; the following prose also names Proposition 5.1 | Present in all four; narrative mention belongs to this entry |
| [6] `keating2009wintenberger` | 1 | `01_introduction:140` | Present in all four |
| [7] `lindahl2016optimal` | 3 | `01_introduction:27,121`; `02_local_setup:21` | Present in all four |
| [8] `stacksgalois` | 1 | `07_eventual_tower:215` | Present in all four |
| [9] `stacksdifferent` | 1 | `06_ramification:290` | Present in all four |

No uncited reference, missing key, duplicate bibliography record, or
unmatched named-source mention was found. The inline named classical
constructions are either covered by the cited background or proved locally;
original proof paragraphs do not require decorative citations. No sentence
contains an excessive multi-source citation list.

## Primary-source metadata and scope audit

The following are **this audit's actual accesses**, not inherited assertions
that a different worker read a paper. Metadata verification establishes
identity/status; the separate scope column identifies the mathematical text
actually inspected. It does not certify every proof in those publications.

| Ref. | Primary identity/status evidence | Actual cited-scope check and limit |
| --- | --- | --- |
| [1] C431 | Actual local anonymous manuscript *Haar limits of optimal wild cycles*, 2026; genuine `main.tex` and PDF, with Theorem 1.1 labelled `thm:compact-adding-machine`. No venue or DOI is claimed. | Read its complete main/introduction and Sections 5–6. The theorem supplies compact classical closure, full-sequence Hausdorff limit, and native conjugacy to addition by one on the infinite `Z_p`, exactly the C430 Section 7 interface. The finite-contact proof excludes a finite cycle. This is not weak convergence alone. Earlier coefficient/contact sections were not independently re-proved in this citation audit. |
| [2] Conrad | The [Stanford course page](https://math.stanford.edu/~conrad/248APage/) identifies Brian Conrad and Math 248A; the [actual handout](https://math.stanford.edu/~conrad/248APage/handouts/algclosurecomp.pdf) has the cited title and Theorem 1.1. No printed date/DOI was established. | Read introduction, Theorem 1.1 and adjoining action paragraph. Completion of an algebraic closure is algebraically closed for the stated complete nonarchimedean base. The isometric action extends. C430 does not improperly import the separate characteristic-zero fixed-field statement discussed there. |
| [3] Debaisieux | [arXiv:2603.03873v2](https://arxiv.org/abs/2603.03873v2) confirms Martin Debaisieux, the **cyclo-tame** title, 22 April 2026 version, and arXiv DOI `10.48550/arXiv.2603.03873`. The [author's page](https://martindbx.github.io/) lists this work as a preprint. | Read the [v2 Section 2.1 setup and Propositions 2.1–2.3](https://arxiv.org/html/2603.03873v2): consistent roots, Galois transitivity, the simply transitive iterate action on a cell, and character extraction over the restricted base. C430 calls this an antecedent for a mixed-characteristic commuting pair, not its own fixed-base theorem. Do not substitute the differently titled v1 or the author's separate July preprint. |
| [4] Elder--Keating | [arXiv v1](https://arxiv.org/abs/2503.16830v1) confirms both authors, title and 21 March 2025 date. The [Springer article](https://link.springer.com/article/10.1007/s00013-026-02234-1) and [issue page](https://link.springer.com/journal/13/volumes-and-issues/126-5) establish *Archiv der Mathematik* **126(5)** (2026), 461–469, DOI `10.1007/s00013-026-02234-1`, published 24 April 2026. | Read [v1 Section 2 statements and selected proof passages](https://arxiv.org/html/2503.16830v1): definitions, quotient compatibility, Lemmas 2.1–2.2 and Theorem 2.3. Perfect residue field is explicit and covers C430's algebraically closed residue field. The upper-break inequality follows from the stated Witt formula. The subscription VOR proof/numbering was **not** accessed; preserve the author-version locator. |
| [5] Keating 2006 | [Publisher-indexed metadata](https://www.sciencedirect.com/science/article/pii/S0022314X05000831) gives Kevin Keating, *Journal of Number Theory* **116(1)** (January 2006), 69–101, DOI `10.1016/j.jnt.2005.03.003`. Direct publisher-page open returned 403; this is explicitly search-indexed primary metadata. [arXiv v2](https://arxiv.org/abs/math/0312391v2) confirms title/author and 16 March 2005 author version. | Read [author-version Theorem 6.1 and its degree passage, plus Proposition 5.1 and proof](https://arxiv.org/html/math/0312391v2). The hypotheses include `p>3`, finite `K/Q_p`, bounded ramification and a tame extension; the degree argument really uses a prime-to-`p` numerator over `p^n`. Proposition 5.1 already assumes cyclic extensions and allows a base automorphism. C430's stated distinction is accurate. Journal full text was not read. |
| [6] Keating 2009 | [Publisher metadata](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.693/) confirms title, author, *Journal de Théorie des Nombres de Bordeaux* **21(3)** (2009), 665–678 and DOI `10.5802/jtnb.693`. Its 2010 online date does not invalidate the 2009 issue year. The DOI string is already visible inside the printed publisher URL. | Read [arXiv:0805.2932v1](https://arxiv.org/html/0805.2932v1), category definitions, Theorem 1.1 and selected Section 3 norm-compatibility/compactness passages. Finite residue field and varying base objects are explicit. This is not equality of prescribed C430 characters over its original infinite-residue base. Publisher-PDF retrieval attempts failed; no new published-PDF read or line-by-line full-proof verification is claimed. |
| [7] Lindahl--Rivera-Letelier | [Cambridge metadata](https://doi.org/10.1112/S0010437X15007575) confirms both authors, title, *Compositio Mathematica* **152(1)** (January 2016), 187–222, and the DOI already stored in `.bib`. [arXiv v3](https://arxiv.org/abs/1311.4478v3) is dated 26 May 2015 and records the same journal metadata. | Read [v3 Theorem C, its `q=1` discussion, minimal-ramification definition and Proposition 4.4 with relevant proof passage](https://arxiv.org/html/1311.4478v3). For odd `p`, `z+z^2` satisfies the criterion. The unique optimal cycles and reduction order therefore match C430's geometric premise. C430 correctly derives its own Hensel-factor arithmetic and does not attribute degree `p^e` to the radius denominator. |
| [8] Stacks Galois | The [live tag 0BMI](https://stacks.math.columbia.edu/tag/0BMI) is Section 9.22, *Infinite Galois theory*, as cited. The September 2026 access month is compatible with this audit. No DOI was identified. | Read Lemmas 9.22.1–9.22.3 and Theorem 9.22.4 with relevant proofs: profiniteness, inverse limits, finite/open and Galois/normal correspondences. C430 applies this inside the separable closure to open character kernels, not to possibly transcendental coordinates in the completion. |
| [9] Stacks different | [0BWD](https://stacks.math.columbia.edu/tag/0BWD) and [0BWG](https://stacks.math.columbia.edu/tag/0BWG) are Lemmas 49.12.2–49.12.3 in Section 49.12, *A formula for the different*. Both printed tags/URLs are correct. No DOI was identified. | Read both statements and the applicable proof passages. The first computes the Noether different by a Jacobian determinant; the second identifies the different in the relevant complete-intersection setting. Their monogenic specialization supports the derivative formula. C430 itself derives the lower-group sum and distinguishes the maximal integer ring from the root order. |

### The companion is real, unpublished, and dependency-limited

The local companion inputs directly inspected have these hashes:

| C431 input | SHA256 |
| --- | --- |
| `main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `sections/1_introduction.tex` | `d9e36e1bb5239457a6a8e3c32a47217ce8b25b8f340505000718c191198f1c34` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |

C430's two relative targets point to existing C431 source/PDF files in the
shared `papers/` layout. The source/PDF bibliography says unpublished, not
accepted or externally reviewed. Its anonymous author label is not a claim
to know an author's identity. The companion must accompany any package in
which these relative links are retained; an isolated C430 PDF is not a
complete source distribution for its dependent tower claim. Browser/PDF
viewers may impose local-link restrictions; a universal click-through
guarantee was not tested.

C430 Theorem 1.3/Section 7 expressly depends on this input. Its core field
and ramification theorems do not. The checked C431 theorem and compact-limit
proof do not use C430's inertia/class-stabilization conclusions. This is a
checked citation interface, not completion of C431's independent manuscript
review or an external publication claim.

## Required corrections proposed to the author

These four numbered items are metadata/identifier repairs, not mathematical
objections. All remain **OPEN ON THE FROZEN INPUT** until an authorized
revision and affected-output check occur.

| ID | Location and exact defect | Required scoped correction |
| --- | --- | --- |
| C430-CIT-01 | `references.bib:34–41`, rendered [4]: only the 2025 preprint is listed; the verified 2026 journal version/DOI is omitted. | Add the journal metadata in the primary-source row above, while explicitly retaining arXiv:2503.16830v1 as the version used for Section 2 numbering. Render `https://doi.org/10.1007/s00013-026-02234-1`. Do not imply that the VOR proof was newly read. |
| C430-CIT-02 | `references.bib:12–22`, rendered [5]: available journal DOI absent from both database and PDF. | Add and actually render `https://doi.org/10.1016/j.jnt.2005.03.003`; retain the already accurate author-version URL. Preserve the qualification that direct publisher access here was 403. |
| C430-CIT-03 | `references.bib:1–11`, rendered [7]: DOI exists in the database but `plain.bst` suppresses it. | Render `https://doi.org/10.1112/S0010437X15007575`, preserving the v3 theorem-numbering note. Adding another invisible `doi` field does not repair the PDF. |
| C430-CIT-04 | `references.bib:42–49`, rendered [3]: the available arXiv-issued DOI is omitted. | Render `https://doi.org/10.48550/arXiv.2603.03873` while keeping the version-specific v2 URL and date. This is an arXiv DOI, not a fabricated journal DOI. |

With `plain`, the smallest compatible implementation is a rendered
`note`/`howpublished` DOI URL in each affected entry, rather than changing
the bibliography's ordering convention. Alternatively, an author-approved
DOI-aware mathematical style must preserve the selected format. All added
identifiers must be checked in the rebuilt BBL **and PDF**, not only `.bib`.
An Elder--Keating article entry may retain its existing key; its note should
state explicitly that citation numbering follows the March 2025 author
version. No separate orphan reference should be added for that version.

Optional, nonblocking consistency improvements:

- Add issue `1` to [7]; it is directly verified, although omission is not
  ambiguous with this continuous page range and the selected math style.
- Give [6] a canonical `https://doi.org/10.5802/jtnb.693` display alongside
  or instead of its existing publisher URL. Its identifier is already
  present and recoverable, so it is not counted as a missing DOI.
- If journal/author-version theorem-numbering equivalence is not checked
  separately for [6], explicitly identify the consulted author version
  arXiv:0805.2932v1. The existing theorem scope is matched there; this audit
  did not certify equality of every version's pagination/numbering.

## Retraction, access, and inherited-evidence limits

The [Retraction Watch search endpoint](https://retractiondatabase.org/RetractionSearch.aspx)
failed with a redirect loop. Its [user guide](https://retractionwatch.com/retraction-watch-database-user-guide/)
was accessible, but reading that guide is not a database search result.
No RW dataset was downloaded or searched, and no Crossref API request was
made. Status is **RETRACTION_DATABASE_UNCHECKED / ACCESS_UNAVAILABLE**, not
zero retractions certified.

Primary metadata pages for [4], [6], and [7] were inspected. They identify
ordinary publications; no article-specific retraction notice was observed
in the inspected records. Targeted primary-domain searches for the exact
[5] title plus retraction, [7] title plus correction, and [4] DOI plus
retracted returned no results. These are partial checks, not exhaustive
negative evidence. [5]'s direct publisher page was inaccessible; its
primary-page retraction status is therefore unverified. No article-specific
CrossMark status record was obtained; a generic publisher CrossMark policy
link is not clearance. The two preprint version pages display the claimed
versions, but no universal withdrawal/correction search is claimed.

The author's `SOURCE_BUILD_RECORD.md` describes earlier source audits and
their read extent. Those historical records were not independently
re-enacted here. This report's primary-source table replaces neither their
mathematical reasoning nor the separate manuscript reviewers. In
particular, an arXiv HTML read is not a paid publisher-PDF read; indexed
publisher metadata is not successful direct publisher access; and a valid
DOI is not evidence that a theorem's proof is correct.

The manuscript is anonymous, so a genuine author self-citation percentage
cannot be established. The known same-batch companion is one of nine
distinct entries, cited three times; that does not license inferring
authorship for the other references. Of six entries bearing a publication
or manuscript year, three are from 2021–2026; the other three are the
directly relevant classical/antecedent papers. The three undated course/
Stacks records are not assigned publication years from access dates.
These counts are descriptive, not a recency threshold for pure mathematics.
No plagiarism detector, proprietary citation database, exhaustive
forward-citation review, or worldwide novelty search was performed.

## Handoff

No manuscript, baseline, old source audit, shared index, evaluator, Git
state, or external service was written by this audit. Only this report was
created. No mathematical program, new agent, external-model upload, API
client, package installation, or compilation was run.

The coordinator/author has been notified of all four repairs. After
adjudication, check only the changed reference metadata and actual rendered
identifiers, rebind the affected hashes, and preserve the frozen input and
this original finding. The present result is **citation cross-reference
complete; bounded cited-scope check complete; four metadata/identifier
repairs open; retraction coverage partial**.
