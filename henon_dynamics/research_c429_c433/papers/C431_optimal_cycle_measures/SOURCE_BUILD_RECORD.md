# C431 source and first-build record

Article: **Haar limits of optimal wild cycles**. Anonymous mathematical
article, 11pt, one-inch margins. Exclusive author directory only.
This record does not claim manuscript-review completion, formal route
evaluation, a sealed release, or journal submission.

## Scope and proof inputs actually read

The updated batch outline and complete outline review were read after
the coordinator closed the gate. The article retains all odd primes,
all complete algebraically closed ultrametric fields of characteristic
$p$, and every $0<|\lambda-1|<1$. No formal-field or subsequence
restriction is substituted.

The complete inputs, reports, and relevant reviews were read:

- R4 A1 contact/convergence proof, 470 lines, SHA256
  `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`.
- R4 D1 isometric-limit proof, 286 lines, SHA256
  `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd`.
- Full E2 arithmetic review, E1 topology review, E7 substantiality
  review, admission Section 3, coordinator source synthesis and X1 audit.

These are author inputs, not substitutes for typeset proofs. Sections
2–4 contain the full arbitrary-field realization, small factor,
displacement and contact arguments. Sections 5–6 contain the compact
limit, coupling, minimality, finite cyclic quotients and aperiodicity
arguments. D1's optional countable-Berkovich-closure fallback and
isolation alternative are not needed and are not imported.

Stable companion interface: Theorem 1.1, **Compact adding-machine limit
of the optimal cycles**, label `thm:compact-adding-machine`. C430 was
notified of the full statement and title. The containing closure $C$
and limit $\mathcal A$ are distinct; only the latter is uniquely
ergodic. C431 uses no UL4 inertia/AS theorem. The optional later C430
tower may depend on C431, not conversely.

## Bibliographic and source access on the drafting turn

Access was read-only to public primary material. No manuscript content
was uploaded. DOI BibTeX was obtained with `curl` content negotiation
and used with the primary issue records, not guessed from memory.

| Citation | Actual source access and passage | Metadata disposition |
| --- | --- | --- |
| Lindahl–Rivera-Letelier | arXiv:1311.4478v3 abstract and full HTML, Problem 1.3, Theorem C and $q=1$ paragraph; Cambridge issue record and DOI BibTeX | Journal issue is Compositio 152(1), 187–222 (2016). DOI export's 2015 year is online publication, not the issue year. Bibliography uses 2016 and explicitly pins the 26 May 2015 v3 question/theorem text. |
| Jacobs | Actual PDF arXiv:1409.4808v2, title page, measure definition and Theorem 2; full relevant proof already checked in the frozen source/review inputs; DOI BibTeX retrieved | PDF and DOI title is *Equidistribution of the crucial measures in non-Archimedean dynamics*. The v2 abstract page retains the different title *An Equidistribution Result For Dynamical Systems on the Berkovich Projective Line*. Use the PDF/DOI title and explicit v2 PDF link. JNT 180 (2017), 86–138. |
| Nordqvist–Rivera-Letelier | arXiv:1904.04494v3 metadata and HTML; Theorem 3 scope and proof boundary in the fully read source audit; DOI BibTeX retrieved | JLMS 102(2) (2020), 470–497. The source comparison is periodic norm bounds, not selected-cycle measure convergence. |
| Baker | Actual author PDF, title/2007 Arizona Winter School description, seminorm topology and Theorem 2.3.2 with general Banach-ring hypothesis | Cited as 2007 lecture notes at the exact inspected URL. No unverified book-chapter metadata is inserted. |
| Hurder–Lukina | Author PDF opened; some subsequent line retrievals failed. Read actual arXiv:2205.06285v2 Sections 2.2–2.3 as successful fallback. Publisher's JMSJ 77(1) index and DOI BibTeX both accessed | Publisher index confirms January 2025, pp. 57–74; one author publication-list rendering still says 2024. Use publisher issue 2025, with explicit 20 January 2023 author version for the checked sections. |

Primary URLs used in addition to the version-specific bibliography:

- [LRL publisher record](https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/optimal-cycles-in-ultrametric-dynamics-and-minimally-ramified-power-series/83B7D75267327F3D0B76E9E6B47BE8F7).
- [LRL DOI](https://doi.org/10.1112/S0010437X15007575).
- [Jacobs DOI](https://doi.org/10.1016/j.jnt.2017.02.018).
- [Nordqvist–Rivera-Letelier DOI](https://doi.org/10.1112/jlms.12325).
- [Hurder–Lukina publisher issue](https://www.mathsoc.jp/publication/JMSJ/onlineindex/77-1.htm).
- [Hurder–Lukina DOI](https://doi.org/10.2969/jmsj/90779077).

The browser DOI landing-page requests for Jacobs and
Nordqvist–Rivera-Letelier failed; the DOI BibTeX requests succeeded.
No publisher full-proof read is claimed for those two articles.
No independent retraction-database check or exhaustive forward-citation
search was made on this drafting turn. The frozen bounded-search
limitations remain in force. No theorem premise relies on a missing
source, and no worldwide-firstness claim is made.

## First-build protocol

Prerequisites actually found: `pdflatex`, `latexmk`, `bibtex`, `pdfinfo`,
`pdftotext`, `pdffonts`, and `pdftoppm`, all under `/usr/bin`.
No installation was needed. The paper-compile instructions were read
in full. Their ML page caps and submission defaults are inapplicable
under the approved anonymous-math-article format.

Required environment for every build:

```text
SOURCE_DATE_EPOCH=1788912000
TZ=UTC
LC_ALL=C
```

Actual build command, executed in this directory:

```sh
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The first `latexmk` invocation completed successfully. Its three
automatic pdfLaTeX passes and two BibTeX passes resolved the expected
first-pass references. The final initial-build log contained two
underfull-box notices in the comparison table and no compiler error.
That actual log is retained as `build_initial.log`.

The author then read every source section and bibliography, checked the
entire extracted PDF text, and corrected one transcription error in
equation (2.3): `iota(a)` became `\iota(a)`. The table's paragraph
columns were changed to ragged-right alignment to remove the two
underfull notices. No mathematical statement or proof was changed in
this self-review. A second actual `latexmk` invocation completed
successfully after one pdfLaTeX pass.

Final first-draft PDF: **12 pages, 382004 bytes**, US Letter,
PDF 1.5. The raw creation and modification metadata are both
`D:20260909000000Z`, corresponding to the required source-date epoch.
Title and author metadata are the stated title and `Anonymous Authors`.
The final `main.log` and `main.blg` contain no warning, undefined
reference or citation, missing-character, overfull-box or underfull-box
message. All 22 listed fonts are embedded subset Type 1 fonts with
Unicode mappings; there are no Type 3 fonts.

Every page 1–12 was actually rendered with `pdftoppm -r 100 -png` and
visually inspected. No clipped text, colliding equations, unreadable
table cell or missing glyph was found. The original page renders are
retained in `inspection/`. Theorem 1.1 is visible on page 2; the
all-higher contact proof is on pages 6–7; the full compactness/measure
argument is on pages 7–9; and the adding-machine and separation proofs
are on pages 9–10. The last page contains the continuation of the
bibliography, not missing body text.

## Frozen first-draft baseline

`baseline/src/` contains a direct copy of `main.tex`, all seven section
files, and `references.bib`. `baseline/main.pdf` and `baseline/main.log`
are direct copies of the inspected final first-draft files.
`main_round0_original.pdf` is a further byte-identical copy, created at
the coordinator's explicit round-zero freeze request. This record
is also copied into the baseline. These are the actual first-draft
materials for the two prospective nonauthor manuscript reviews, not
fabricated review rounds or a retrospective version history. The
earlier `build_initial.log` is preserved separately as real build
history; there was no failed compiler attempt.

SHA256 hashes for the first-draft source and output are:

| File | SHA256 |
| --- | --- |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `references.bib` | `5e0975227644cc458dbf3d40e011f4a11cb9c0d76819f3043cc39f6bcc730bf2` |
| `sections/1_introduction.tex` | `d9e36e1bb5239457a6a8e3c32a47217ce8b25b8f340505000718c191198f1c34` |
| `sections/2_coefficients.tex` | `b5eb44fc34ee02d951855ae51989d0b329f85e4ead8b79bd100b67eeeaaa34f8` |
| `sections/3_displacements.tex` | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `main.log` | `6867988ca20316e1b106299fac3d94d96a6b1c996066b0cb019bc12881d26a1f` |
| `build_initial.log` | `ef708a5172e83c90b1d91d5e349ef16276328a602ea57ff5ccf7c7134450242d` |

Status: author drafting, full self-review, actual build and visual
inspection complete; manuscript nonauthor reviews are **not yet
claimed**. The frozen mathematical inputs' earlier internal reviews
are not counted as reviews of this newly typeset manuscript. No old
proof file, Git object, evaluator, shared record, seal or mathematics
program was changed or run, and no material was uploaded to an external
review API.

## Authorized author revision 1 — 2026-09-09 UTC

The first-draft entries above remain a historical record. The coordinator
subsequently accepted the full 382-line E7 pass-1 manuscript review and
the full 266-line X1 citation audit, and authorized their bounded
presentation/source fixes. Both original reports were read in full and
their hashes independently checked before editing. The reports and all
baseline files remain unchanged.

The current revision qualifies the Hurder–Lukina background as minimal
equicontinuous Cantor systems, defines the conventional integer valuation
and inverse-limit notation, repeats the LRL citation at the reduction
formula, and prints the four existing journal DOI URLs in bibliography
notes. All five original version URLs and the alphabetical `plain`
style remain. Baker's 2007 lecture-notes manifestation is retained, now
with an explicit distinction between the 2007 lectures and the linked
PDF's first-publication statement for University Lecture Series 45
(2008). The author directly reopened that same primary PDF and read its
opening paragraph and first-page footnote on this revision turn. No DOI
or separate revision date for the notes is invented. Full retraction
and update-status clearance remains **UNCHECKED**.

`revision1/` did not exist before this revision; its absence was checked
and it was created without a reuse/cleanup step. Its nine TeX/BibTeX
source files are an exact copy of the revised current sources. An actual
`latexmk` invocation there used the same recorded source-date epoch,
UTC and C locale. It succeeded through three automatic pdfLaTeX passes
and two BibTeX passes. No compiler-error repair or second invocation was
needed. Its final `main.log` and `main.blg` have no warning, unresolved
reference/citation, missing-character, overfull or underfull message.

The revised PDF has 12 pages, 384227 bytes, PDF 1.5 and the same raw
source-date timestamps. All 22 fonts are embedded subset Type 1 with
Unicode mappings. Text and sources of all changed passages were read;
all four DOI URLs and all five version URLs were recovered exactly from
the extracted PDF after whitespace normalization. All 12 pages were
rendered into `revision1/inspection/`; affected pages 1–3 and 11–12 were
actually viewed and found legible without clipping or collisions.
Theorem 1.1 remains on page 2, with its name, label and statement
unchanged. All proof text is unchanged.

`main.pdf`, `main_round1.pdf` and `revision1/main.pdf` are byte-identical,
SHA256 `dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915`.
The current top-level build log, BibTeX log and bibliography output are
copies from the authoritative `revision1/` build. The original PDF and
baseline retain their earlier hashes. Detailed fixes, full immutable
review links, commands and source/output hashes are in
`PAPER_IMPROVEMENT_LOG.md`; the sole live state record is
`PAPER_IMPROVEMENT_STATE.json`.

Revision status: **round1_revised_pending_second_review**. This is not
pass-2 acceptance, a final clean release build, a numerical review score,
formal route evaluation or external publication clearance. No new
mathematical claim, mathematical program, external review API, Git
operation, old-research change or release seal was introduced.
