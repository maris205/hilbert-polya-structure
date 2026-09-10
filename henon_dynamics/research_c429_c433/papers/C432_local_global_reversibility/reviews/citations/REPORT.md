# C432 independent citation audit

Audit date: 2026-09-09 UTC; actual clock checkpoint during verification:
20:58:38 UTC. Scope: the frozen eight-page author baseline, not a new
outline, proof, novelty, or peer-review assessment.

## Result

**No identified citation must-fixes.** All four references exist, their
included metadata and DOIs match primary records, all eight formal
citations resolve to the correct entries, and no bibliography entry is
orphaned. The cited passages support their stated roles and the paper
explicitly deducts the classical mechanisms it uses.

**Separate limitations remain:** live retraction/Crossmark verification
is incomplete; two IOP landing pages were inaccessible; the published
Song Wang full text was not obtained; and the ARS local-PDF structural
preflight returned `UNAVAILABLE` because `pypdf` is absent. None of these
access limitations is relabeled as a clean-status certificate or a
demonstrated citation error. No source or manuscript correction was made.

## Scope, instructions, and frozen inputs

I read the actual repository, Hénon, and batch `AGENTS.md` instructions,
the complete current 388-line `BATCH_PLAN.md`, the ARS router, the complete
542-line academic-paper workflow, the complete 422-line citation-compliance
role, and the complete 228-line citation-format reference. Only ARS's
bounded `citation-check` role is active. Its automatic-edit, APA/IEEE,
age-ratio, intake, passport, and whole-pipeline defaults do not override
this assignment's frozen-source, anonymous mathematical-article contract.

The selected bibliography style is `amsplain`: numerical brackets with
alphabetical reference ordering, not IEEE order of first appearance.
There is no arbitrary recency quota or inferred author self-citation test.
An anonymous author identity makes an actual self-citation ratio
**not determinable**, not zero.

All current inputs were read in full: `main.tex` (53 lines), all seven
section files (615 lines total), the sole table (21 lines),
`references.bib` (46 lines), `SOURCES.md` (102 lines), and
`BUILD_RECORD.md` (173 lines). I also read the generated bibliography,
all eight pages of extracted PDF text, the actual citation/number mapping
in the build auxiliary file, and the existing final-page rendering.
The source notes supplied pointers; the primary accesses below were
performed independently for this audit.

Actually recomputed input SHA256 values:

| Artifact, relative to the manuscript directory | SHA256 |
| --- | --- |
| `main.pdf` and `baseline/main.pdf` | `d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa` |
| `main.tex` | `e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8` |
| `references.bib` | `a4ce6daf2a069c51bece1a08c45ad8f241c8cfca74b20fede1d6e5cac8b564b7` |
| `SOURCES.md` | `04813dc535c7d6fc4d10140f7bd5f3a4483db05dbd240c2609422239128ef5d1` |
| `BUILD_RECORD.md` | `343d6c01c11989d514c0bb760aca7dfbc840afc3418dc66bc0a8acfb0ee1f0dc` |
| `sections/00_abstract.tex` | `ef3ccceef4dedb08c052bf56563f6976100ac9d38b8a87419c71c543760d3ed8` |
| `sections/01_introduction.tex` | `68852fd93b21c6c7322bd9230170db19f142281d3d7d6dd4c5419d51b80dafc9` |
| `sections/02_axis.tex` | `f49282b52048a15046c3bb2be8644f252ef77e8f6e0df3b48f6e5eac41acecb0` |
| `sections/03_centralizer.tex` | `a5eb22a9144d4893e896aae6f222e917d5f337a2315a5d7b8f2a4af99f0fad56` |
| `sections/04_descent.tex` | `15e6b2f06402a64c62e4c2bb7cd787b47f4acb4a80cb26f4c92a9a85da1cb930` |
| `sections/05_places.tex` | `da4035fc48b59bad0e1a4f64f9c79bab2f05400f5e85496449f15c800eaf7ed7` |
| `sections/06_control.tex` | `7bc226b0cfab97680f02b82e5e26efa648ce1d2ee3f4c4ae98e2fa3b2beca21f` |
| `figures/TABLE_local_places.tex` | `102a0dac97aff1519c20e53122b731543ff0380f9a9ffa7568a42c33a1bcc7fb` |
| `build/attempt_01/main.bbl` | `b90a25d59d957abba4d4b8061baf27926daf6213e221745a0c018e093acd44df` |

Read-only comparisons confirmed that current and baseline main source,
bibliography, source notes, section trees, and table trees are identical.
The PDF hash agrees with the assigned freeze. No rebuild was performed.

## Citation index and rendered identifiers

| Printed reference | Citation key | Actual source locations | Occurrences |
| --- | --- | --- | ---: |
| [1] Baake–Roberts | `baake2005symmetries` | `01_introduction.tex:98`, `:102`; `02_axis.tex:21` | 3 |
| [2] Cantat–Dujardin | `cantat2024holomorphically` | `01_introduction.tex:111` | 1 |
| [3] Gómez–Meiss | `gomez2004reversors` | `01_introduction.tex:97`; `02_axis.tex:20` | 2 |
| [4] Song Wang | `wang2015grunwald` | `01_introduction.tex:108`; `05_places.tex:6` | 2 |

There are eight single-key citation commands, four distinct cited keys,
four generated bibliography items, zero undefined keys, zero uncited
entries, and no `nocite` expansion. The auxiliary `bibcite` mapping,
generated `main.bbl`, and PDF text agree on [1]–[4]. Narrative names
agree with the corresponding references; `Rev` is explicitly defined
in the manuscript to avoid inheriting a source's different convention.

The final-page rendering shows all four DOI strings and both arXiv
links legibly, without clipped identifiers. `pdfinfo -url` returns six
distinct external destinations, exactly the four DOIs and two preprints.
There are nine URI annotations because some long links span lines;
these are not extra references. The annotation destinations do not
include the punctuation printed after the links. The `doi` fields are
also printed through URL notes, so `amsplain` ignoring a nonstandard
field does not cause missing rendered DOIs.

Jung–van der Kulk and Hensel are named classical theorems, not dangling
formal citation keys. The amalgam is attributed through explicitly
identified accounts in [1] and [3]. The basic Hensel hypotheses used
are written in the proof. No unread original Wang article is inserted
merely because the historical obstruction bears Wang's name.

## Independent primary-record and applicability checks

### [1] Baake–Roberts

The [author-submitted arXiv record](https://arxiv.org/abs/math/0501151)
confirms Michael Baake and John A. G. Roberts, the title in the current
bibliography, *Nonlinearity* **18** (2005), 791–816, and
DOI `10.1088/0951-7715/18/2/017`. It lists only version v1, submitted
11 January 2005. The manuscript correctly uses the journal year rather
than a secondary site's inconsistent year.

I read [v1, Section 2](https://arxiv.org/pdf/math/0501151v1), including
Facts 1–2 and Proposition 1 with its proof, and the actual statements
of Theorem 2 and Corollary 1. The whole-group amalgam and reduced-word
input has the required general-field scope. The later centralizer
restriction requires characteristic zero and roots of unity only
$\{\pm1\}$; the manuscript correctly does **not** apply it over
$\mathbb C$. Its specific finite kernel is calculated internally.

Both the DOI route and direct IOP article route returned retrieval
errors. Thus identifier/metadata and the actual cited preprint passages
are verified, but live IOP delivery and final-publisher text were not.

### [2] Cantat–Dujardin

The [publisher's full article](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164)
confirms Serge Cantat and Romain Dujardin, the current title with
$\mathbb C^2$, *Bulletin of the London Mathematical Society* **56**
(2024), 3745–3751, DOI `10.1112/blms.13164`; its record identifies
issue 12 and first online publication on 26 September 2024.
Omitting issue/day is consistent with the approved volume-page style.

I read the final example of Section 2.2 and its full-centralizer
explanation. It supplies the scalar-root field-of-conjugacy mechanism
credited at `01_introduction.tex:109–119`. The manuscript labels the
all-place two-map consequence as a combination with Wang, not as a
quoted theorem of this source. That is a properly separated inference;
the source does not itself supply the constrained inverse-pair theorem.
The manuscript does not import the analytic rigidity argument as a
premise of its own construction.

### [3] Gómez–Meiss

The first page of the [published author-hosted PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf)
confirms A. Gómez and J. D. Meiss, the current title,
*Nonlinearity* **17** (2004), 975–1000, and
DOI `10.1088/0951-7715/17/3/012`. The initials and Gómez accent
are preserved correctly; no unverified name expansion is needed.

I read Section 2.1's full complex polynomial group, reduced-word
formulation and Theorem 3, plus the adjacent symmetry/reversor scope.
They support `02_axis.tex:12–24`. The manuscript credits a classical
group-structure account and proves its own exhaustive centralizer;
it does not upgrade the source's commuting-subgroup inclusion to the
equality needed here. The paper's reversed-map notation is separately
defined rather than silently copied.

The DOI and direct IOP routes returned retrieval errors. The accessible
PDF is the typeset published article, not merely an unidentified draft;
this supports the bibliographic record, not current retraction status.

### [4] Song Wang

The [Springer publisher record](https://link.springer.com/article/10.1007/s11425-015-4977-5)
confirms Song Wang, *Grunwald-Wang theorem, an effective version*,
*Science China Mathematics* **58** (2015), 1589–1606, and
DOI `10.1007/s11425-015-4977-5`. The [author's arXiv record](https://arxiv.org/abs/1401.0389)
links that same DOI and lists only v1, submitted 2 January 2014.
The bibliography correctly distinguishes the 2015 publication from
the accessible 2014 preprint rather than treating them as two works.

I read [v1, Section 2.1](https://arxiv.org/pdf/1401.0389v1), Proposition
2.1 and its following remarks. The remark on printed page 7 gives the
exact field $\mathbb Q(\sqrt7)$, exponent eight and class 16.
`05_places.tex:3–6` explicitly identifies this as the accessible
preprint locator. The manuscript then proves the all-place statement
directly, so a damaged extracted exceptional-set glyph is not used
to justify an omitted-place assertion.

Springer exposed metadata and a subscription preview. The Sciengine
published-PDF endpoint returned HTTP 403. No published full-text read
or direct reading of the original 1948/1950 Wang papers is claimed.

## Retraction and primary-status boundary

| Reference | Status evidence actually obtained | Remaining unchecked status |
| --- | --- | --- |
| [1] | Author record has no withdrawal marker; journal linkage verified | IOP article delivery unavailable; authoritative current correction/retraction status unverified |
| [2] | Publisher article and metadata available; no retraction/correction notice found in retrieved page text | Dedicated Crossmark/database result unavailable |
| [3] | Published author-hosted PDF available | IOP article delivery unavailable; authoritative current correction/retraction status unverified |
| [4] | Publisher metadata and linked preprint available; no publisher-page retraction/correction notice or arXiv withdrawal marker found | Published full text and dedicated Crossmark/database result unavailable |

I performed one bounded search batch: each of the four exact journal
DOIs combined with `(retraction OR correction OR "expression of concern")`.
No relevant notice was located. Search hits from aggregators were not
used to override primary metadata, and no-result searching is not proof
of absence. The [Retraction Watch database](https://retractiondatabase.org/)
returned an empty readable page, so no completed database cross-check
is claimed. Four DOI-specific public Crossmark-dialog openings were
rejected by the browsing tool as unavailable/non-retryable. No API
client, credential, paywall bypass, or alternate transport was used.

The honest disposition for all four is **RETRACTION STATUS UNVERIFIED
BEYOND THE OBSERVED PRIMARY-PAGE SIGNALS**, not “not retracted.”
`SOURCES.md` already discloses that its author-stage work was not a
dedicated retraction audit, so that record needs no integrity correction.

## Local PDF reading limitation

The ARS structural preflight was run once, read-only, with JSON sent
to stdout and Python bytecode writing disabled. Its sidecar result,
bound to the assigned PDF hash, was:

```json
{
  "schema": "pdf_read_preflight/1",
  "verdict": "UNAVAILABLE",
  "file": "papers/C432_local_global_reversibility/main.pdf",
  "sha256": "d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa",
  "declared_page_count": null,
  "enumerated_page_count": null,
  "reader_page_count": null,
  "warnings": ["pypdf-not-installed: preflight cannot parse the document"],
  "generated_at": "2026-09-09T20:56:04.708908+00:00",
  "tool": "pdf_read_preflight/1.0.0"
}
```

Accordingly, this report uses source-section/line locators for its
manuscript findings and does not award ARS-certified PDF page anchors.
The successful Poppler extraction, URL inspection, and existing image
read establish observed rendering, not a replacement structural PASS.
No dependency was installed and no PDF or auxiliary sidecar was written.

## Corrections, handoff, and exclusions

- Mandatory reference/citation corrections: **0**.
- Automatically applied corrections: **0**, because the baseline is frozen.
- Known wrong identifiers, author/year mismatches, orphans, or source-role
  misrepresentations: **0 identified**.
- Access limitations requiring honest retention: those listed above.

There is no reason from this bounded audit to replace a reference,
invent an original-source read, or revise the four existing entries.
Retraction-status completion may be checked later through an available
authorized service; it is not silently satisfied here. Any stricter
release policy is for the coordinator to adjudicate, not for this role
to invent.

This report is the only file written. Source, bibliography, baseline,
PDF, shared state, Git, evaluation files and other review tracks were
not changed. No mathematical program, nested agent, external model/API,
full-manuscript upload, compilation, or new literature/novelty survey
was performed. The structural preflight and read-only text/hash/URL
checks are document diagnostics, not mathematical experiments. The
two actual manuscript reviews remain distinct. No peer-review,
global-priority, submission-readiness, or target-arithmetic verdict is
issued; `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
