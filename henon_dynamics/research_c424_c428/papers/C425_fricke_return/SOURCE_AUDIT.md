# C425 manuscript: source and citation receipt

2026-09-09 UTC. Author-side manuscript preparation, not a new independent
review, an exhaustive priority search, or a citation-integrity certificate.
Only this manuscript directory was written. No unpublished material was
uploaded to a third party or another model.

## Frozen mathematical inputs

The following files were read completely; paths are relative to this
manuscript directory. They remain unchanged.

| Input | SHA-256 |
| --- | --- |
| `../../BATCH_PLAN.md` | `0ddf87bd678ec967cbcaa054ce56aac0f1d2fe9af97b9ff9074d9c44e8a061e2` |
| `../../continuation_round3/nonlinear_geometry/PROOF_PACKAGE.md` | `4672ce2e12a3e6584cb2bc4df815ea9c4110806d2d96d05a0506cdf79ed10b9c` |
| `../../continuation_round3/nonlinear_geometry/SOURCE_AUDIT.md` | `e1e7f6ce47027eec07069e53eac99506de249e8a4726409daac5227a3ab7f0f8` |
| `../../continuation_round3/nonlinear_geometry_review/REVIEW.md` | `9c7cea3c7b425141744103ed7cf66546659f3c1bb9d25daae813099259d5c8b5` |
| `../../../research_c419_c423/continuation_round2/integral_return/IR1_PROOF.md` | `5dcc9c6a84e4219a24fa177399ee1e7292e7217d8b83ab3dda4a90ceebd17e5d` |

The C421 manuscript title/date were read from its actual `main.tex`.
Its existing PDF was located and hashed, not rebuilt or claimed newly
reviewed in full:

`../../../research_c419_c423/papers/C421_integral_return/main.pdf`

SHA-256: `13fece76ec21d56eacbdcb43303f3acef017e9f9b7f1e0e228f5438cd6761d0c`.
This is an unpublished local source with no public archival identifier
or DOI. Its author identities are not invented. The bibliography's
relative link resolves from the delivered `main.pdf` directory; it is
not a promise of public availability outside this repository.

## Public source access performed for this manuscript

The source-ownership discussion is in article Section 1.1 and Table 1.
The locators below identify what was actually inspected, not a claim
to have read every source's full body. All primary bodies were read
through remote HTML/PDF retrieval; no local primary-PDF structure
preflight or human-read attestation is asserted.

| Citation key | Primary body and actual reading scope | Metadata verification |
| --- | --- | --- |
| `shin2026character` | [v3 HTML](https://arxiv.org/html/2308.16614v3): Theorems 1.1–1.3, §2.1 definitions, §2.2 low-coordinate identities and Lemma 2.2 with proof, selected adjacent discussion, §§3.2–3.3 including Remark 3.1. Embedded figures were not separately inspected. | [arXiv record](https://arxiv.org/abs/2308.16614v3) plus successful Crossref DOI-to-BibTeX response for `10.1090/proc/17770`: 154(10), 4091–4106 (2026). |
| `cantat2009bers` | [v2 PDF](https://arxiv.org/pdf/0711.1727v2): coefficient-family scope, Proposition 2.2, Theorem 3.1, Proposition 3.2, Corollaries 3.3–3.4 and their visible proofs. | [arXiv record](https://arxiv.org/abs/0711.1727) and successful Crossref response for `10.1215/00127094-2009-042`; page range supplied by arXiv's journal reference. |
| `vishkautsan2016residual` | [v2 PDF](https://arxiv.org/pdf/1504.07099v2): abstract, §1.1, opening §1.2 and displayed Theorems A–B. Later proofs were not read for this manuscript. | [arXiv record](https://arxiv.org/abs/1504.07099) confirms author, title, 27 (2016), 25–35 and DOI `10.4171/RLM/720`; identity also checked against the PDF front page. Independent publisher metadata retrieval was unavailable. |
| `abboud2025rigidity` | [v3 HTML](https://arxiv.org/html/2406.11510v3): abstract and §§1.1–1.3, including Theorem A and the torus comparison. No later effective-height estimate is imported. | [arXiv record](https://arxiv.org/abs/2406.11510) and HTML header agree on author and version date, 23 April 2025; arXiv DOI `10.48550/arXiv.2406.11510`. A journal publication is not asserted. |
| `planat2024dynamics` | [Publisher PDF](https://mdpi-res.com/d_attachment/dynamics/dynamics-04-00001/article_deploy/dynamics-04-00001.pdf?version=1704184938): front-page metadata, abstract and opening introduction. Later sections were not screened for every possible overlap. | Publisher front page and successful Crossref response for `10.3390/dynamics4010001`: 4(1), 1–13, published 2 January 2024. |

The public references are ownership comparators or context, not missing
steps in the self-contained new proof. Most importantly, the manuscript
contains the approved explicit Shin subtraction; it does not treat
independent coefficients alone as the surviving increment. The C421
equal-forcing result is likewise credited, without reusing its certificate
as evidence for the unequal-forcing theorem.

## Retrieval failures and limits

- Direct browser DOI opens for Shin, Cantat and Vishkautsan returned
  non-retryable retrieval errors. They were not counted as successful
  publisher reads, and denied access was not bypassed.
- Four public DOI metadata requests used the Crossref
  `/works/<DOI>/transform/application/x-bibtex` endpoint with a 20-second
  timeout. Shin, Cantat and Planat succeeded. Vishkautsan returned curl
  exit 35 (`SSL_ERROR_SYSCALL`); his verified arXiv/PDF metadata was used
  instead, with the lack of an independent publisher lookup disclosed.
- No fresh novelty-search query was issued in this writing phase. The
  frozen author and independent-review source audits retain their own
  bounded search records; those queries are not relabelled as new work.
- Retraction/Expression-of-Concern databases, indexing completeness,
  plagiarism services, venue policies and conflicts of interest were not
  checked. None is reported as passed. Primary-source version numbers,
  not search-engine relative ages, determine the locators.

## Citation checks and corrections

The compiled auxiliary file contains nine citation commands referring to
six distinct keys. The bibliography has precisely those six entries:
zero orphan citations, zero uncited entries, and zero duplicate keys.
The established numbered, alphabetically sorted mathematical bibliography
is used; neither APA nor a conference-specific citation format was imposed.

All five public references have a DOI in `references.bib`. All five
DOIs are visible in the stable PDF. Because `plainnat` does not print
the `doi` field of a miscellaneous entry, Abboud's DOI was also placed
in its note after inspecting the actual `.bbl`; this is a documented
typesetting correction, not invented metadata. C421 has no DOI and is
explicitly labelled local/unpublished. A duplicated C421 year in the
rendered bibliography was removed during the same correction.

There is one local project reference among six entries (16.7%), above
the skill's 15% self-citation alert if used as a project-reference proxy.
Actual human authorship and hence a literal self-citation ratio are
unassessed. The reference is necessary to disclose prior ownership.
Four entries have a recorded year in 2021–2026; Cantat (2009) is a
foundational comparison, and Vishkautsan (2016) is retained for its
specific adjacent observable, not as current-news evidence.

The complete `paper-write` and `paper-compile` entry instructions and
selected writing/venue/citation references were read. ARS was restricted
to source/citation checks using its router, academic-paper workflow,
citation-compliance prompt and citation-format reference. Their generic
external-model, full-pipeline, venue, bilingual and mandatory-boilerplate
defaults were not substituted for the approved manuscript contract.
No external model or mathematical program was called.
