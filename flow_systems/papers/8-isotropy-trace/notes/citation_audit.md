# Paper 8 independent citation and integrity audit

**Audit date:** 2026-08-14 (Asia/Shanghai)  
**Audit role:** independent ARS citation/source/integrity reviewer  
**Final verdict:** **ACCEPT**, conditional only on the public-release path check in
Section 8 showing that no retained source PDF is tracked or staged.

This audit was read-only with respect to the manuscript, bibliography, compiled
paper, retained sources, manifests, and preflight sidecars.  It distinguishes
three separate questions: whether the manuscript cites the right source, whether
the exact retained manifestation supports the stated claim at the stated
locator, and whether those source bytes may be redistributed.

## 1. Exact candidate lock

The verdict attaches only to these bytes:

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` |
| `paper/references.bib` | `a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e` |
| `paper/paper.pdf` | `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a` |

The released PDF is 19 A4 pages and exposes the expected title, author, subject,
and keywords.  A clean independent XeLaTeX--BibTeX--XeLaTeX--XeLaTeX rebuild in
a temporary directory produced no undefined citation, undefined reference,
BibTeX warning, missing glyph, overfull box, or compilation error.  The only
layout diagnostics were two harmless underfull boxes.  The released and rebuilt
PDFs have the same `pdftotext -layout` SHA-256,
`333a501f499b42d141269bee7048f350a5f8442b65dd27921af7fa4ad7433e91`;
their visible/textual content therefore agrees despite timestamp-dependent PDF
container bytes.  Visual checks of the title/abstract page, the ERS locator and
character-filter page, declarations, and both bibliography pages found no
truncation, overlap, broken formula, or broken citation rendering.

## 2. Citation closure

The manuscript contains 30 citation commands and 14 unique cited keys.  The
bibliography contains exactly the same 14 keys:

```text
AnantharamanDelaroche2002  BourneRennie2018
BrownGreenRieffel1977      CombesZettl1983
Deninger2023               Deninger2026
ElliottRobertSantiago2011  Green1978
Jones2009                  Laugesen2017
Morishita2026              MuhlyRenaultWilliams1987
Renault2021                Williams2007
```

- cited but absent from the bibliography: **0**;
- bibliography entries never cited: **0**;
- duplicate bibliography keys: **0**; and
- undefined citations in the final independent build: **0**.

Every bibliography entry is a primary paper, book/author manuscript, or primary
course-note source used for a mathematical statement.  No search-result page,
secondary summary, or unverified DOI is used as proof authority.

## 3. Load-bearing manifestation and locator audit

| Key | Exact manifestation used for technical locators | Independently checked support | Result |
|---|---|---|---|
| `Deninger2026` | arXiv `1807.06400v4` | equation (35), p. 32; Section 6 and Theorem 6.1, pp. 38--39; Propositions 7.4, 7.6, 7.7, Corollaries 7.8--7.9, Theorem 7.10 and cautions, pp. 43--47 | PASS |
| `Deninger2023` | arXiv `2301.11643v1` | Theorem 4.2, pp. 11--12, including compact packets/orbit fibres | PASS |
| `Morishita2026` | arXiv `2508.15971v5` | equation (1.1.5), p. 5; Remark 2.1.13, p. 13; Lemmas 3.4--3.5, pp. 23--24; Theorem 3.6 discussion, pp. 24--25 | PASS |
| `Green1978` | published article | Proposition 3, printed p. 203 | PASS |
| `MuhlyRenaultWilliams1987` | published JOT PDF | Theorem 2.8, printed p. 10; Theorem 3.1, printed p. 16 | PASS (image fallback included) |
| `BrownGreenRieffel1977` | published article | Theorem 1.2, printed pp. 351--352, with its strictly-positive-element hypothesis | PASS |
| `AnantharamanDelaroche2002` | author-hosted primary article PDF | Examples 2.7(2) and Theorem 5.3 | PASS |
| `Williams2007` | author manuscript version 3.1, 6 September 2006 | equation (4.63) and Theorem 4.30, p. 138; Theorem 5.12, p. 161 | PASS |
| `BourneRennie2018` | published article PDF | Proposition 3.2 and Lemma 7.4 | PASS |
| `Renault2021` | published article PDF | printed pp. 416--418, Plancherel weight and dual-Haar normalization | PASS |
| `ElliottRobertSantiago2011` | arXiv `0805.3122v2` | Section 3.3 and Theorem 3.11, **arXiv-v2 physical p. 12** | PASS |
| `CombesZettl1983` | published article PDF | Proposition 2.2, printed pp. 72--73 | PASS (image fallback included) |
| `Jones2009` | 1 October 2009 Berkeley course notes | pp. 15--16 for `vN(Z)=L^infinity(T)` and the trace; Definition 7.1.2 and Theorem 7.1.3, pp. 43--44, for normal order continuity | PASS |
| `Laugesen2017` | arXiv `0903.3845v2` | Definition 14.1, p. 79; Theorems 14.10--14.11, pp. 84--85; Theorem 23.5, p. 137 | PASS |

The two scanned/image-heavy sources were additionally rendered at their cited
pages.  MRW physical pages 8 and 14 correspond to printed pp. 10 and 16;
Combes--Zettl physical pp. 7--8 correspond to printed pp. 72--73.  The locators
are not inferred from OCR alone.

## 4. Bibliographic metadata and DOI checks

The DOI-bearing entries were checked against their primary/Crossref records.
Titles, author lists, venues, years, volumes, issues, and page/article ranges
agree, and no correction/retraction relation was present in those records.
The material metadata points that required special attention are now correct:

- Deninger is bound to *Indagationes Mathematicae* **37**(1) (2026), 25--136,
  DOI `10.1016/j.indag.2024.05.007`, while technical locators explicitly remain
  on arXiv v4.
- The Deninger chapter is in *Colloquium De Giorgi 2021 and 2022* (2024),
  pp. 177--196.  The range was checked against the publisher's official table
  of contents (the chapter starts at 177 and the next contribution starts at
  197), rather than guessed from the 16-page arXiv pagination.
- Bourne--Rennie is volume 21, **issue 3**, article 16; the rendered bibliography
  correctly shows `21(3):16`.
- Combes--Zettl is volume 265, **issue 1**, pp. 67--81.
- Elliott--Robert--Santiago retains the journal metadata and DOI, but its URL,
  note, and manuscript citation all bind the technical locator to exact arXiv
  version 2.  Thus “physical p. 12” cannot be mistaken for journal p. 12.
- Morishita remains a versioned arXiv-v5 `@misc` record with “to appear” status;
  no unpublished final volume or page range is invented.
- Williams's published book metadata is retained while every technical locator
  is explicitly attached to author manuscript version 3.1.

## 5. Retained-source integrity

There are 19 named local PDFs and 19 same-stem preflight sidecars (17 unique PDF
byte streams because the Deninger-v4 and Renault PDFs occur in two audit
collections).  A fresh SHA-256 comparison established that every sidecar's
recorded PDF hash equals the current local file.

- 14 sidecars report `PASS`; in every case declared, enumerated, and reader page
  counts are identical and the warning list is empty.
- The five groupoid sidecars truthfully report `UNAVAILABLE` because `pypdf` was
  absent in that earlier audit environment.  They do not falsely claim a pass.
  Fresh `pdfinfo` counts are 28 pages (Anantharaman-Delaroche), 19 (BGR), 60
  (Green), 20 (MRW), and 540 (Williams); text extraction and representative
  image checks supplied the recorded fallback.
- Both checked checksum ledgers (`phase2_topology_sources.sha256` and
  `trace_source_checksums.sha256`) pass in full, covering both PDFs and
  sidecars.  The five novelty PDFs and their sidecars also match the hashes in
  `phase2_novelty_search.md`.  The five groupoid PDF hashes match
  `phase2_groupoid_source_audit.md` and their sidecars.

The manuscript's source-integrity declaration accurately distinguishes the 14
successful ARS preflights from the five disclosed fallback cases.  It does not
overstate the fallback files as ARS preflight passes.

## 6. Claim strength, ownership, and novelty boundary

The cited sources support the source facts and standard machinery at the level
claimed.  The manuscript does not transfer proof ownership improperly:

- Deninger supplies the finite-kernel parametrization, packet/clock/isotropy,
  topology cautions, and compactness facts; the choice of one actual orbit and
  the corrected restricted-topology argument are visibly manuscript-level
  derivations.
- Morishita's anti-equivariant map is used with the printed limitations of
  Remark 2.1.13 and the Theorem 3.6 proof, rather than promoted to a stronger
  ambient theorem.
- Morita equivalence, stable isomorphism, and the stronger unstabilized
  homogeneous-space isomorphism are kept logically distinct.  Stable
  cancellation is never asserted.
- Amenability/full--reduced equality is kept separate from faithfulness,
  Plancherel normalization, and normality.
- ERS is cited only for lower semicontinuity/traciality under pullback; density,
  semifiniteness, nonfaithfulness, and unboundedness are proved or attributed
  separately.
- The fixed one-orbit result is `REFUTED`; it is not promoted to the inherited
  packet.  The packet claim remains `NOT_TESTABLE` because the topology and
  same-map bridge are absent.  The positive-time scalar Radon measure is a
  separately typed `PASS`, not an all-prime operator construction.

The novelty sentence reproduces the bounded 2026-08-14 search conclusion and
uses “to our knowledge”/“did not locate.”  It does not claim universal
nonexistence, priority, or novelty for generic imprimitivity, Plancherel,
Poisson, or point-evaluation singularity.  This is the strongest wording the
retained exclusion audit supports.

## 7. Abstract and declaration agreement

The English and Chinese abstracts agree on all load-bearing facts: the selected
single orbit and `L=log p`; the unstabilized algebra; the character/Floquet
return comb; the regular FNS trace `Lf(0)`; the fixed-map normality obstruction;
local `REFUTED`, packet `NOT_TESTABLE`, and scalar `PASS`; and the explicit
nonclaims.  The Chinese abstract adds the harmless detail that the trivial
character retains all two-sided repeated returns, while the English abstract
displays the full phase formula.  There is no contradiction or scope inflation.

The declarations cover data/code availability, ethics/consent, author
contributions, competing interests, funding, generative-AI use, source/citation
integrity, and acknowledgments.  The AI disclosure does not claim human reading
or cross-model review and places final verification and responsibility on the
human author.

## 8. Copyright and public-release boundary

Reproducible citation does not imply permission to redistribute the retained
PDF bytes.  The corpus contains a mixture of open licences, arXiv-hosted copies
whose arXiv licence is not a blanket downstream redistribution grant,
author-hosted copies, and publisher-copyrighted manifestations.  A single
repository-wide redistribution claim would therefore be unsafe without an
exact-manifestation, file-by-file licence ledger.

The accepted conservative release policy is:

1. retain all 19 source PDFs locally for verification;
2. exclude every `papers/8-isotropy-trace/notes/sources/*.pdf` from public
   GitHub;
3. publish the manifests, checksum ledgers, exact URLs/versions/locators,
   sidecars, audits, and `sources/README.md`; and
4. preserve `notes/sources/.gitignore`, whose default rule is `*.pdf`.

This audit environment is not itself a Git worktree, so it cannot inspect the
eventual index.  The release acceptance condition is that the final repository
check returns no tracked or staged path matching
`papers/8-isotropy-trace/notes/sources/*.pdf` (in particular, the root release
audit must confirm zero such paths in `git diff --cached --name-only`, and
should also confirm zero with `git ls-files`).  If any retained source PDF is
present, the public-release verdict automatically changes to **REVISE** until
that file is removed from the release or its exact-manifestation licence is
documented.

## 9. Closed findings and decision

| Earlier mandatory issue | Final disposition |
|---|---|
| Wrong Bourne--Rennie issue | fixed to issue 3 |
| Missing Deninger chapter range | fixed to pp. 177--196 and publisher-TOC checked |
| Missing Combes--Zettl issue | fixed to issue 1 |
| Ambiguous ERS page manifestation | fixed to “arXiv-v2 physical p. 12” with v2 URL/note |
| Overbroad preflight declaration | fixed to disclose 14 PASS and five `UNAVAILABLE` fallbacks accurately |
| Unlicensed blanket PDF synchronization | fixed by local-only `*.pdf` policy, conditional on the final staged/tracked-path check |

**Manuscript/bibliography/source-claim verdict: ACCEPT.**  No citation,
metadata, locator, manifestation, claim-strength, bibliography-closure,
bilingual-abstract, build, or declaration blocker remains on the exact candidate
lock.

**Public GitHub package verdict: ACCEPT conditional on the Section 8 zero-PDF
index check.**  That is an external packaging verification, not a request to
alter the accepted manuscript or bibliography.
