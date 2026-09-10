# C429 frozen-baseline citation audit

## Result and scope

**Bounded citation check complete: no open citation must-fix.** The six actual references, their six occurrences, the cited passages and their ownership, and the rendered bibliography are consistent with the manuscript's expressly limited comparison. The source-access and publication-status qualifications below are part of this result, not silently cleared checks.

This is an independent citation audit of the anonymous English article *Polynomial periodic-data rigidity for unicritical maps in finite characteristic*. It is not a mathematical proof review, admission decision, worldwide novelty search, external peer review, publication acceptance, or final-release approval. The manuscript remains the frozen author baseline.

The applicable repository/batch instructions, complete approved `BATCH_PLAN.md`, ARS router, academic-paper workflow, citation-compliance instructions, and citation-format reference were read. ARS guided the occurrence-to-reference cross-check, primary-source verification, access/status disclosure, and rendered-output check. The task's numbered alphabetical BibTeX `plain` style overrides APA/IEEE ordering and age/self-citation quotas; the freeze overrides citation auto-correction. Only this report was written.

| Check | Actual result |
|---|---|
| Bibliography entries / distinct cited keys | 6 / 6 |
| Citation commands / key occurrences | 6 / 6; each key occurs once |
| Cited keys missing from bibliography | 0 |
| Uncited bibliography entries / duplicate entries | 0 / 0 |
| Incorrect author/title/publication/DOI fields identified | 0 |
| Relevant full-text passages directly inspected | 5 sources; extent and version specified below |
| Original full text unavailable | Levin–Sodin–Yuditskii (1994); metadata and abstract only |
| Open must-fixes / corrections made | 0 / 0 |
| Optional layout item | One existing, readable underfull bibliography paragraph |
| Public status screen | No matching retraction/correction notice located; database and publisher-access limitations retained |

External checks were conducted on 2026-09-09 UTC. No external model, bibliographic API, upload, mathematical computation, new agent, Git operation, source edit, PDF edit, or recompilation was performed.

## Actual inputs and read extent

The complete `main.tex`, `math_commands.tex`, all seven active section files, `references.bib`, and `AUTHOR_RECORD.md` were read, not just the introduction or author's source table. The read of the proof sections was for citation/dependency coverage, not an independent correctness verdict. All seven sections are included by the entry point. All external citation commands are in Section 1.1; no `nocite` or other external citation appears elsewhere. The general named apparatus elsewhere, including Hasse derivatives, Frobenius, and Jacobians, is defined or developed locally rather than presented as an unnamed imported theorem.

The complete generated `main.bbl` was read. The six `citation` entries and six `bibcite` mappings in `main.aux` were independently checked. The final LaTeX/BibTeX logs were screened for citation/reference errors and bibliography warnings. The author's stated source reads were not counted as this auditor's independent reads.

The current PDF, attempt-02 PDF, and frozen-snapshot PDF share SHA-256:

```text
118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02
```

`sha256sum -c BASELINE_FILES.sha256` returned OK for all 23 frozen snapshot files, both before and after the external-source checks. The active source hashes were also rechecked and agree with the recorded baseline:

```text
e8af703473b863355e39c809650f1a0d7da98432747ea8d5a1474775895b6b27  main.tex
08d91e8041f21be8f5f08a273468daef71a75262e65efc0d6508b7b818b4e40d  math_commands.tex
2572ac5a6b6be971085d89df647042ea43f62df451b8c65962f31466db22f04b  references.bib
4261b94f9cdb2ee8f8344240657e61593066e916fd02bb56fca7de57acede495  sections/01_introduction.tex
5eda56a89a9d279180b42e0289ce5d57f315d0e87e374b9e148d4d54154fd1f2  sections/02_periodic_algebra.tex
0c10b30eac8d3cbf3b34b8d6f133a009cd27b9b1c3f9c6d8b0c70141006146e3  sections/03_carry_stabilization.tex
3ebb7dd19724c1cedfa0d3e1c158ce65a7f8c4bc04268b85b90f0c4ff283367a  sections/04_jacobian_regimes.tex
8891ca9a50f08062be10d4ccc2d9cec62603f4ed144b4b89971a63d6469a2386  sections/05_hasse_paths.tex
8e041a4fce45ff486c4718409a065984ddb2c7c8ca7d0104ed3698a7eb9d8226  sections/06_marked_insertion.tex
bb55c5c3603fb1ab1b942c1da7beb10816fcb9dfed7cdfa5eb4cd9ee8a37ce1b  sections/07_consequences.tex
4a1b11611b2b9ec2279e85ff023ce3601d178a1b87a27e72e6deed3dc785cfd6  AUTHOR_RECORD.md
7922a4deb30d1ab568b3cf819d4be641de580f250c58f696660091feab81ce0c  main.bbl
987ae013746b8997de76815026f1042e309b5f04417750f38d991ed9012f7bbd  main.aux
20bca8523c7d303fa6f4b64711a411b855490d840533c950901e8c492019dbb0  main.log
0d46ceeed5552269472c4c37e857b260623c0bd062bf82214ee26ec868da493f  main.blg
225084568d2c0def64a3171248306d29fe688a24616fba55c3ee73f33c3f974d  BASELINE_FILES.sha256
a8e2f53824cd91e9c6b71ebdd96944715de06ec6514bc0c7ac5d28fa42b20a14  SOURCE_AND_PDF.sha256
```

This does not re-audit every upstream proof/provenance file or every compiler dependency. It binds this audit to the actual complete manuscript and its frozen output.

## Occurrence, numbering, and rendered display

All source locations below are in `sections/01_introduction.tex`. The page locations were corroborated by extraction from the actual PDF and the existing attempt-02 page images; the structural-preflight qualification in the next section applies.

| Rendered number / key | Source line and locator | Visible occurrence | Bibliography page |
|---|---|---|---|
| [1] `cattani1996residues` | 138, Section 4 | Section 1.1, p. 3 | 15 |
| [2] `cvitanovic1998beyond` | 141, Section 4 | Section 1.1, p. 3 | 15 |
| [3] `kalinin2011livsic` | 119, Theorem 1.1 | Section 1.1, p. 2 | 16 |
| [4] `levin1994ruelle` | 143, historical attribution without theorem locator | Section 1.1, p. 3 | 16 |
| [5] `li2025ground` | 124, Theorem 1.1 | Section 1.1, p. 2 | 16 |
| [6] `zou2025finite` | 130, Theorem 1.1 | Section 1.1, p. 3 | 16 |

The alphabetical sequence Cattani, Cvitanović, Kalinin, Levin, Li, Zou is correct for `plain`; the nonmonotone order of first citation is therefore intentional. The bibliography contains five journal articles and one correctly typed edited-volume chapter. It is not erroneously forced into order-of-first-appearance IEEE style.

I visually inspected the existing `build_attempts/02/visual/page-02.png`, `page-03.png`, `page-15.png`, and `page-16.png`. Citation numerals and locators, names with accents, titles, page ranges, DOI strings, and accessible-text labels are readable and inside the margins. No missing-glyph or clipped-reference defect was seen. The references begin after the disclosure on p. 15 and continue on p. 16; no entry is lost at the break.

`pdfinfo -url main.pdf` confirms all 11 intended distinct external URLs: six DOI links and five accessible-text alternatives. Its 16 annotation rows arise from wrapped links occupying multiple rectangles, not extra references or changed destinations. Each target matches the corresponding source `url` text, including the chapter DOI underscore, author's tilde path, and explicit arXiv v2 suffixes. The `doi` fields are repeated in `note` as clickable DOI URLs because `plain` does not itself print the DOI field; the output displays each DOI once.

The final logs contain no undefined citation/reference, missing database entry, or BibTeX error. The one `Underfull hbox (badness 2173)` at `main.bbl` lines 33–38 belongs to [5]. Its mildly stretched line is visible but readable in the inspected image. This is optional typography, not a citation correctness blocker, and was not altered in a frozen baseline.

## PDF-read preflight qualification

The mandatory ARS preflight was run before relying on local PDF page anchors. Its actual stdout sidecar is preserved here because this report is the only authorized new file:

```json
{
  "schema": "pdf_read_preflight/1",
  "verdict": "UNAVAILABLE",
  "file": "main.pdf",
  "sha256": "118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02",
  "declared_page_count": null,
  "enumerated_page_count": null,
  "reader_page_count": null,
  "warnings": [
    "pypdf-not-installed: preflight cannot parse the document"
  ],
  "generated_at": "2026-09-09T20:56:01.234285+00:00",
  "tool": "pdf_read_preflight/1.0.0"
}
```

No package was installed and this is not reported as PASS. Independent `pdfinfo` reports 16 letter-size pages, 423862 bytes, no encryption, and anonymous author metadata. `pdftotext -f 15 -l 16 -layout main.pdf -` reproduced all six references. Those checks and the four existing rendered images support the limited visible-citation assessment; they do not replace a successful structural page-tree preflight or an all-pages manuscript-layout review. Source line anchors remain the primary local locators.

## Primary-source records and applicability

The records below preserve the existing reference list; no corrected replacement list is necessary. Full-text inspection means the specified passage was actually inspected, not that the source's entire proof was independently reviewed.

### [1] Cattani–Dickenstein–Sturmfels

**Metadata:** Eduardo Cattani, Alicia Dickenstein, Bernd Sturmfels, “Computing multidimensional residues,” in *Algorithms in Algebraic Geometry and Applications*, edited by Laureano González-Vega and Tomás Recio, *Progress in Mathematics* 143, Birkhäuser Basel, 1996, pp. 135–164. DOI `10.1007/978-3-0348-9104-2_8`. The [publisher chapter record](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8) confirms the publication fields; the [arXiv record](https://arxiv.org/abs/alg-geom/9404011) confirms full author names and the sole v1 submission of 27 April 1994.

**Passage:** The accessible [author preprint, Section 4](https://arxiv.org/html/alg-geom/9404011v1), was read in full: the pure-power initial-form setup, Lemma (4.2), Theorem (4.3), and trace formulas (4.6)–(4.8) substantiate the manuscript's coefficient/residue/Jacobian-trace comparison. The text itself acknowledges earlier trace identities. The manuscript says these authors relate the classical objects, not that they invented all of them.

**Boundary:** The published chapter's complete text was not available from its landing page; the actual mathematical check used the explicitly labeled preprint, not a claimed byte-identical published PDF. No complex-analytic theorem is applied to the characteristic-p proof. Citation supported within this historical-comparison role.

### [2] Cvitanović–Hansen–Rolf–Vattay

**Metadata:** Predrag Cvitanović, Kim Hansen, Juri Rolf, Gábor Vattay, “Beyond the periodic orbit theory,” *Nonlinearity* 11(5) (1998), 1209–1232. The [author-hosted published-format PDF](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf) confirms authors, title, volume, year, and pagination; its issue imprint and the [arXiv record's related DOI](https://arxiv.org/abs/chao-dyn/9712002) corroborate `10.1088/0951-7715/11/5/003`. The separate arXiv v1 is dated 2 December 1997; the manuscript correctly labels its linked 1998 text as author-hosted.

**Passage:** Section 4, especially equations (24)–(28), was read directly. It develops the quadratic-map successive-trace recurrence and finite binomial matrices. The sentence following (28), together with reference [8], explicitly attributes the earlier matrix construction to the 1994 Levin–Sodin–Yuditskii article.

**Boundary:** The source emphasizes the quadratic map's special form and uses complex contour methods. The manuscript credits this precedent but proves its own all-degree finite-characteristic identities. This is not an imported arbitrary-degree theorem. The DOI open failed and IOP's site was robots-blocked; neither failure invalidates the independently corroborated DOI or constitutes publisher full-text access.

### [3] Kalinin

**Metadata:** Boris Kalinin, “Livšic theorem for matrix cocycles,” *Annals of Mathematics* 173(2) (2011), 1025–1042, DOI `10.4007/annals.2011.173.2.11`; confirmed by the [publisher record](https://annals.math.princeton.edu/2011/173-2/p11) and [publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n2-p11-p.pdf). The linked [arXiv v2 record](https://arxiv.org/abs/0808.0350v2) is dated 15 March 2010 and is identified as the selected version, not misdated as a 2011 preprint.

**Passage:** Theorem 1.1 and the preceding closing-property definition were checked in both the [v2 text](https://arxiv.org/html/0808.0350v2) and the published PDF, pp. 1026–1027. The compact metric space, topologically transitive homeomorphism, closing property, Hölder matrix cocycle, trivial periodic products, and Hölder transfer conclusion agree with the manuscript's summary.

**Boundary:** This is a classical antecedent, not a polynomial-regularity or finite-characteristic specialization. The manuscript's “for example” formulation does not attribute invention of the classical Livšic problem to Kalinin. The direct DOI open failed during this audit, while the canonical publisher record and published PDF were accessible.

### [4] Levin–Sodin–Yuditskii

**Metadata:** G. Levin, M. Sodin, P. Yuditskii, “Ruelle operators with rational weights for Julia sets,” *Journal d'Analyse Mathématique* 63 (1994), 303–331, DOI `10.1007/BF03008428`; all confirmed by the [publisher record](https://link.springer.com/article/10.1007/BF03008428). The initials agree with that record; unverified expansions were not substituted.

**Access:** Only publisher metadata and abstract were accessible. The abstract concerns rationally weighted Ruelle operators on Julia sets; it was not used to infer an unread theorem's hypotheses or conclusion. The direct DOI open failed, but the canonical publisher page was readable and showed subscription-only full text.

**Attribution:** The manuscript's claim is that the 1998 authors credit these earlier authors. That claim is directly established by the inspected 1998 text, not by pretending to have read the 1994 article. The current manuscript then expressly discloses abstract-only access and states that no unread theorem is invoked below.

**Disposition:** Preserve this disclosure. The full manuscript contains no stated proof dependency on a theorem from this article, so unavailable full text is a registered limitation, not an unresolved premise requiring deletion of the historical citation. A stronger future assertion about its results would require actual full-text inspection.

### [5] Li–Zhang

**Metadata:** Zhiqiang Li, Yiwei Zhang, “Ground states and periodic orbits for expanding Thurston maps,” *Mathematische Annalen* 391 (2025), 3913–3985, DOI `10.1007/s00208-024-03018-0`; confirmed by the [publisher record](https://link.springer.com/article/10.1007/s00208-024-03018-0) and [arXiv v2 record](https://arxiv.org/abs/2303.00514v2). Online publication was 18 October 2024; the volume year 2025 is correct. The v2 date is 28 December 2024 and its record identifies a polished published version.

**Passage:** [Theorem 1.1 in v2](https://arxiv.org/html/2303.00514v2) was directly inspected. It treats expanding Thurston maps with visual metrics, or postcritically finite rational maps without periodic critical points with chordal/spherical metrics, and real Hölder observables and transfers. These are precisely the two settings summarized in the manuscript.

**Boundary/status:** No reduction to the manuscript's polynomial setting is claimed, nor exclusive priority over earlier Livšic work. The publisher landing page is not full-text access; the selected v2 supplies the theorem check. The arXiv record contains an administrative text-overlap note naming arXiv:1804.08221; record this neutrally. It is not labeled a retraction or expression of concern and does not establish misconduct. The DOI resolved successfully.

### [6] Zou–Wei

**Metadata:** Rui Zou, Hua Wei, “A finite approximate Livšic theorem for Anosov diffeomorphisms,” *Journal of Applied Analysis and Computation* 15(4) (2025), 2185–2194, DOI `10.11948/20240420`; confirmed by the [publisher record](https://www.jaac-online.com/article/doi/10.11948/20240420) and [published PDF](https://www.jaac-online.com/data/article/jaac/preview/pdf/jaac-15-4-2185.pdf). “And” in the journal title follows the PDF masthead; the site's ampersand is not a different journal. The URL's `preview/pdf` path serves the actual ten-page article, not merely an abstract.

**Passage:** Theorem 1.1, p. 2186, was directly inspected, including transitive Anosov/compact-manifold hypotheses, bounded Hölder norm, finite small periodic data, and a Hölder coboundary plus a controlled error. The manuscript's qualitative summary is supported; it does not quote a precise indexing convention or transfer a numerical error bound.

**Boundary:** The manuscript distinguishes approximate Hölder recovery from its exact degree-controlled polynomial conclusion and does not claim to have introduced finite Livšic questions. This theorem is not a premise of the proof. Both the DOI redirect and the full publisher PDF were accessible in this audit, notwithstanding the earlier author's unsuccessful DOI attempt.

## Public correction, retraction, and source-status screen

The status check was explicit, not inferred from bibliographic existence. For each of the six exact titles I searched with the terms `retraction OR retracted OR correction OR erratum OR withdrawn`; the 1994 DOI also received an identifier-based status search. No result matching a correction/retraction notice for one of the six works was located. Broad search results and incidental words in unrelated papers were not counted as notices.

The readable primary landing pages were also inspected for status notices, including targeted `retract` and `correct` checks. The sources and limits are:

| Reference | Primary public status material inspected | Recorded status and limitation |
|---|---|---|
| [1] | [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8), [arXiv v1 record](https://arxiv.org/abs/alg-geom/9404011) | No matching notice found on inspected records; not a full-text or database clearance. |
| [2] | [arXiv record](https://arxiv.org/abs/chao-dyn/9712002), author-hosted published text | No matching notice found there. Current IOP publisher status could not be inspected because the publisher site was robots-blocked. |
| [3] | [Annals publication record](https://annals.math.princeton.edu/2011/173-2/p11), publisher PDF, [v2 history](https://arxiv.org/abs/0808.0350v2) | No matching notice found; v2 remains available. |
| [4] | [Springer article](https://link.springer.com/article/10.1007/BF03008428) | No matching notice found on the public page; complete original article unavailable. |
| [5] | [Springer article](https://link.springer.com/article/10.1007/s00208-024-03018-0), [v2 record/history](https://arxiv.org/abs/2303.00514v2) | No matching retraction/correction notice found. The separate arXiv administrative overlap note is preserved above without further inference. |
| [6] | [JAAC publication record](https://www.jaac-online.com/article/doi/10.11948/20240420), publisher PDF | No matching notice found on inspected public materials. |

The public [Retraction Watch database interface](https://retractiondatabase.org/) was attempted. It redirected to a cookie-support URL and returned zero readable lines. No usable database query was completed: **Retraction Watch database screening is UNAVAILABLE**, not “zero database matches.” No bibliographic API was called to bypass the assigned boundary. A machine-verifiable Crossmark status clearance was not obtained either.

Accordingly, the defensible statement is “no relevant notice located in this bounded public screen,” not “all six sources are guaranteed unretracted.” Public absence of a notice is not a scientific-validity or originality certificate. This audit did not run plagiarism-similarity software, inspect a private author corpus, or infer self-citation rates from anonymous authorship.

## Remaining items and handoff

There are no source/PDF corrections requested for the frozen baseline. The existing bibliography is the verified list; no duplicate revised bibliography is created in this audit.

| Item | Classification | Action / closure condition |
|---|---|---|
| Original 1994 article unavailable | Disclosed access limitation, not a current proof premise | Keep Section 1.1's explicit disclosure and secondary attribution. Obtain and inspect full text before making stronger direct claims. |
| DOI opens failed for [1]–[4] | Access-result qualification, not identified wrong DOI | Retain primary-confirmed DOI strings and the working alternatives already printed for [1]–[3]. Do not call the failed resolver attempts successful. |
| IOP current publisher status unavailable | Status-screen limitation | If comprehensive publisher-status clearance is required, repeat from an authorized accessible interface. |
| Retraction Watch interface unavailable | Status-screen limitation | Repeat an actual database check if that stronger gate is required; do not substitute the present search result for it. |
| Li–Zhang arXiv administrative note | Public source-status observation | Retain the neutral observation in the audit; no unsupported misconduct or priority inference. |
| PDF structural preflight unavailable | Tooling limitation | A successful preflight requires the missing parser in an authorized later environment. This report claims only the documented source/display checks. |
| Underfull [5] bibliography paragraph | Optional cosmetic polish | May be adjusted by the author in a genuine authorized revision; no current readability/citation defect requires unfreezing. |

The source comparison keeps theorem ownership and applicability separate: prior Livšic results motivate the obstruction question; residue and finite-matrix work supplies credited antecedents; no inspected source is claimed to prove the manuscript's characteristic-p rigidity theorem. All six references have an actual purpose and no reference is padding. The manuscript expressly disclaims a worldwide-priority guarantee and represents internal preparation checks as distinct from external peer review.

This report closes only the assigned bounded citation phase. Any later manuscript revision must receive a new hash-bound check of changed citation text and rendered output; the present result does not silently transfer to a different PDF.
