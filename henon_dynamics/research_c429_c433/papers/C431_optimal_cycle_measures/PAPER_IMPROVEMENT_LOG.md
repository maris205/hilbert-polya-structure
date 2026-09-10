# C431 paper improvement log

Article: *Haar limits of optimal wild cycles*.
Current status: **round1_revised_pending_second_review**.
This is the actual author revision following one manuscript review and
a separate citation audit. There is no round-2 review or release claim.

## Scope and intact raw review records

The coordinator accepted the complete reports below and authorized
only the fixes recorded here. The author read both reports in full and
independently checked the hashes before changing sources. These links
point to the **full original reports**, not excerpts, paraphrases or
reconstructed reviews; the files remain unchanged.

| Complete immutable raw record | Lines | SHA256 |
| --- | ---: | --- |
| [E7 actual manuscript pass 1](reviews/round1/REVIEW.md) | 382 | `78964f384e3b1b4c822448a787c57bbb09a56fe5cc0d0cbe6ae0f8cf90ca0703` |
| [X1 bounded citation audit](reviews/citations/REPORT.md) | 266 | `289e6d4e48726877f6231b0c49f11ca2902d4eb1579c916f9ab3bfaed27723e4` |

E7 found the main theorem provable as stated, with no critical or major
mathematical defect; its requested change concerns background scope.
X1 is a citation audit, not a second manuscript-review verdict. Earlier
research-proof reviews are not counted as reviews of this manuscript.
No numerical reviewer score has been assigned or inferred.

The paper-write and paper-compile instructions governed source clarity,
verified bibliography edits and actual output checks. The improvement
loop's original-version preservation, full raw-review retention and
state-record principles were used. The coordinator's explicit scope
overrides external-model uploads, generic ML scoring/format defaults,
automatic additional rounds and final-release defaults. No external
review API or new agent was used.

## Round 1 dispositions

| Finding | Actual authorized change | Author acceptance check |
| --- | --- | --- |
| E7 R1 / C431-CIT-2 | The introduction now attributes the finite-quotient inverse-limit background to **minimal equicontinuous Cantor systems**. The next sentence still supplies this paper's own cyclic-partition proof, including the finite alternative. | Read the revised source and PDF page 3. The unrestricted compact-system phrase is gone; no theorem or proof is modified. |
| C431-CIT-1 | Added each of the four existing exact journal DOI URLs to its BibTeX `note`, retaining `plain` alphabetical numbering and all five version URLs. | All four DOI URLs and five original URLs were recovered exactly from the PDF text after whitespace normalization and visually checked on pages 11–12. |
| C431-CIT-3 | Retained Baker's 2007 lecture-notes entry and explained that the linked PDF records first publication in University Lecture Series 45 (2008). | Directly reopened the actual author PDF, read its opening paragraph and first-page footnote, and checked the revised rendered entry. No notes DOI or PDF revision date was invented. |
| E7 O1, accepted optional | Defined `v_p(a)` as the exponent of `p` dividing a positive integer, distinct from the field valuation, and defined `Z_p` by its usual inverse-limit topology. | Read the definitions on PDF page 1. The conjugacy remains topological, not metric or analytic. |
| E7 O2, accepted optional | Repeated the LRL Theorem C / `q=1` citation immediately after equation (2.2). | Read the source and rendered citation on page 3. The reduction identity remains explicitly source-owned. |
| C431-CIT-4, status limitation | No additional retraction-database or complete article-update pass was authorized or performed in this revision. | Retraction and full update-status clearance stay **UNCHECKED**, not “zero retractions.” |

For the Baker clarification, the primary object actually reopened was
[the same author notes PDF](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf).
The lecture year and first-publication statement are separate facts.
The four journal DOI suffixes were already verified in the original
source record and independently checked by X1; this revision changes
their rendering, not their metadata or theorem version bindings.

Only `references.bib`, `sections/1_introduction.tex` and
`sections/2_coefficients.tex` differ from the original source snapshot.
The complete source diffs were read. All proof text, Theorem 1.1, its
name and label, and every substantive field/prime/multiplier/sequence
quantifier are unchanged. The C430 interface remains one-way, and no
operator-lifting or A4 target claim has been added.

## Actual revision build and checks

The absence of `revision1/` was checked with `test ! -e revision1`.
It was then created with `mkdir revision1`, and the nine current
TeX/BibTeX files were copied into it, with the same section structure.
No old build directory or baseline was cleaned, reused or overwritten.
All prerequisite executables were found under `/usr/bin`.

The following command was actually executed in `revision1/`:

```sh
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

One invocation succeeded, performing three automatic pdfLaTeX passes
and two BibTeX passes. Initial-pass unresolved references resolved
normally within that invocation. No compiler failure or repair rerun
occurred. The authoritative build outputs and logs remain in
`revision1/`. `main.pdf`, `main_round1.pdf`, and the current top-level
`main.log`, `main.blg`, and `main.bbl` are direct copies of those
revision outputs; this was not an additional compilation.

Actual post-build commands included:

```sh
rg -n 'Warning|Overfull|Underfull|undefined|Missing character|^!' main.log main.blg
pdfinfo -rawdates main.pdf
pdffonts main.pdf
pdftotext -f 1 -l 4 -layout main.pdf -
pdftotext -f 11 -l 12 -layout main.pdf -
pdftotext -layout main.pdf main.txt
pdftoppm -r 100 -png main.pdf inspection/page
```

The warning scan returned no matches. The PDF has **12 pages,
384227 bytes**, US Letter, PDF 1.5; both raw timestamps are
`D:20260909000000Z`. All 22 listed fonts are embedded subset Type 1
with Unicode mappings, and no Type 3 font is present. The changed
source passages and affected PDF text were read in full. All 12 pages
were freshly rendered; pages 1–3 and 11–12 were actually opened for
visual inspection and showed no clipping, colliding equations, missing
glyphs or unreadable links. The actual renders remain in
`revision1/inspection/`.

The nine exact links in the bibliography were also checked by applying
`tr -d '[:space:]'` to the extracted `main.txt` and matching each
expected URL with fixed-string `rg`. Results: four journal DOI links,
five original version links. There are eight citation occurrences
after the repeated source citation, still using the same five entries
in the same alphabetical order.

The fresh `revision1/` TeX/BibTeX sources equal the current corresponding
sources byte for byte; `diff -qr sections revision1/sections` returned
no differences, and both master/bibliography hashes agree. The original
baseline and raw-review hashes were rechecked after the revision.

## Frozen version bindings

| Actual PDF version | SHA256 |
| --- | --- |
| `main_round0_original.pdf` = `baseline/main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `main_round1.pdf` = `main.pdf` = `revision1/main.pdf` | `dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915` |

Round-1 source and build hashes below are relative to `revision1/`.
The current top-level source copies have the same hashes.

| File | SHA256 |
| --- | --- |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `references.bib` | `67164b9f8489c3d99cc3219ae13372659dd2aac1b618d2f572e1950375e00da5` |
| `sections/1_introduction.tex` | `40d85d94398f31bb838c5a9779f7533f22523b7de141763b4e73506b524e1308` |
| `sections/2_coefficients.tex` | `8359d9a98f5bd1da20fca07e2ab4c59074e9b36dcab7e29f04a8b99701468432` |
| `sections/3_displacements.tex` | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `main.log` | `78319d8176d8e383bc5f1d883117fc7811bf9b5c7ec2bf224125f83680336aec` |
| `main.blg` | `2869df80311b1a366eafb1f3521178afc6dcc628264e742964e979b9cb9e66e2` |
| `main.txt` | `dd24807e31a05470e0ad35d1dd3f08b39694b1af5b5bbb6985c20478b59ab417` |

The updated current `SOURCE_BUILD_RECORD.md` has SHA256
`0fa72b6c86386f28e3f8af11fb3434794010ecc5ba417d1ba438323ef0023d50`.
Its unchanged baseline counterpart retains
`a6559476e391193f64454fff0d016299b0259723fbc30530bbf6eecb915065af`.

## Handoff boundary

Freeze these round-1 sources and PDF for the coordinator to assign the
same E7 reviewer the actual second manuscript pass. The sole live state
file is `PAPER_IMPROVEMENT_STATE.json`. No `main_round2.pdf`, second-pass
verdict, final-release clean build, Git operation, formal evaluation,
mathematical run or release seal is represented as completed. Raw
reviews, the original baseline, and prior research remain untouched.
