# Paper 22 — R0 Hyperref Source Repair Receipt

Date: 2026-08-24 UTC  
Role: bounded R0 hyperref source-repair author  
Disposition: exact source delta frozen; no build performed

## Controlling gate and hard preconditions

Immediately before either authorized write, the root batch ledger recorded the
current gate exactly as `PAPER22_R0_HYPERREF_SOURCE_REPAIR_OPEN`.

The governing failed-build blocker was rehashed and read through its terminal
line:

| Path | SHA-256 | Bytes | LF | Terminal line |
|---|---|---:|---:|---|
| `notes/BUILD_R0_BLOCKER.md` | `5242052c625add4ba084d5542faae221e6b1a1cb6d81b773b9295d968afbc7fd` | 5,873 | 145 | `R0_BLOCKED` |

The frozen pre-repair source was also rehashed immediately before writing:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e` | 69,218 | 1,921 |

The target old heading occurred exactly once and was exactly line 1754. This
receipt path was absent. The project contained exactly 24 regular files, four
child directories, zero symlinks, and zero other filesystem entries.

## Exact authorized source delta

Exactly one existing path was modified: `paper/main.tex`. Its sole content
change is the following one-line replacement:

```diff
-\subsection{The \(g=2r\) seed/selected-face boundary}
+\subsection{The \texorpdfstring{\(g=2r\)}{g=2r} seed/selected-face boundary}
```

The visible subsection title remains `The g=2r seed/selected-face boundary`;
the added second argument supplies the PDF-safe bookmark text `g=2r`. No
prose, mathematics, claim, label, citation, command definition, layout
setting, bibliography entry, or other line was changed.

The exact source transition is:

| State | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| reviewed old `paper/main.tex` | `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e` | 69,218 | 1,921 |
| repaired `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |

Thus the complete file delta is exactly +23 bytes and 0 LF. Replacing the new
line by the old line in a read-only byte stream reconstructs the reviewed old
identity exactly; a unified comparison contains one deletion and one addition
at line 1754 and no other hunk.

## Unchanged companion source bindings

The two other frozen public-source files remain byte-identical:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

Both remain mode `0644`, UTF-8, LF-only, BOM-free, CR-free, NUL-free, and
terminated by exactly one LF. The repaired `paper/main.tex` also remains mode
`0644` with the same hygiene properties.

## Frozen structural, citation, and hygiene counts

Static read-only counts are unchanged across the exact replacement:

| Check | Old | Repaired |
|---|---:|---:|
| abstract environments | 1 | 1 |
| numbered sections | 8 | 8 |
| subsections | 28 | 28 |
| table environments | 3 | 3 |
| figure environments | 0 | 0 |
| appendix commands | 0 | 0 |
| labels | 121 | 121 |
| cross-references | 98 (`70` `\eqref`, `28` `\ref`) | 98 (`70` `\eqref`, `28` `\ref`) |
| citation commands | 4 | 4 |
| cited-key occurrences | 6 | 6 |
| distinct cited keys | 6 | 6 |
| bibliography entries | 6 | 6 |
| comments / percent bytes | 0 | 0 |
| forbidden markers | 0 | 0 |
| `\includegraphics` commands | 0 | 0 |
| `\include{...}` commands | 0 | 0 |
| external `\input{...}` commands | 1 (`math_commands`) | 1 (`math_commands`) |
| `\write18` commands | 0 | 0 |

The exact six-key citation set remains
`BlancVanSanten2021`, `DangFavre2021`, `Deserti2016`,
`FujiokaKogawaLiShudo2023`, `Rangarajan2002`, and `ShaoSun2025`.

The repaired source remains UTF-8, LF-only, BOM-free, CR-free, NUL-free, and
has exactly one terminal LF. Environment and brace balance, unique-label
closure, reference closure, zero-comment status, and the one permitted
`\input{math_commands}` dependency are unaffected by the one-line markup
repair.

## Project inventory transition

The exact pre-write project inventory was 24 regular files, four child
directories, zero symlinks, and zero other entries. The child directories were
exactly `experiments`, `notes`, `paper`, and `refine-logs`.

The pre-write regular-file universe was:

- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- `experiments/publication_lock.json`
- `experiments/source_lock.json`
- `notes/BUILD_R0_BLOCKER.md`
- `notes/CITATION_VERIFICATION.md`
- `notes/CLAIMS_EVIDENCE_MATRIX.md`
- `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`
- `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`
- `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`
- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
- `notes/NOVELTY_ASSESSMENT.md`
- `notes/PROOF_PACKAGE.md`
- `notes/PUBLICATION_STAGE_SCOPE.md`
- `notes/RESEARCH_QUESTION.md`
- `paper/PAPER_PLAN.md`
- `paper/main.tex`
- `paper/math_commands.tex`
- `paper/references.bib`
- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/INITIAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`

The exact post-write inventory is 25 regular files, the same four child
directories, zero symlinks, and zero other entries. It differs only by this
new regular file, `notes/R0_HYPERREF_SOURCE_REPAIR.md`, while the one existing
path `paper/main.tex` has the exact delta above. All other 23 pre-existing
regular files remain byte-identical.

## Build-output absence

No TeX or BibTeX command was run. The following success-only build paths were
absent before the repair and remain absent after it:

- `paper/BUILD_METADATA_R0.json`
- `paper/BUILD_RECEIPT_R0.json`
- `paper/main.aux`
- `paper/main.bbl`
- `paper/main.blg`
- `paper/main.log`
- `paper/main.out`
- `paper/main.pdf`
- `paper/main_round0.pdf`

The retained historical build roots named in the blocker were not accessed or
modified.

## Permission and lifecycle boundary

This invocation exercised exactly the two authorized writes:

1. replace the single specified heading in `paper/main.tex`; and
2. create only `notes/R0_HYPERREF_SOURCE_REPAIR.md` as this receipt.

It did not compile, invoke TeX or BibTeX, build, browse, use network access,
run science, experiments, numerical work, or CAS, touch a temporary build
root, update a batch ledger, create a build output, modify another source or
project path, open Paper 23, release, upload, transport, message externally,
or produce any other external effect. This receipt grants none of those
permissions and does not itself advance the root gate.

The old formal review
`notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`, SHA-256
`d38343539db88d1eeda555c464657e408df6ab58aa6ad7a811cd262f53038750`,
17,056 bytes and 424 LF, ending exactly `PAPER_SOURCE_R1_PASS`, binds the old
`paper/main.tex` bytes with SHA-256
`9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e`.
It is immutable historical evidence and does not review, approve, or transfer
PASS status to the repaired bytes.

Before any rebuild, two fresh, mutually independent repaired-source reviews
must each inspect and bind the repaired `paper/main.tex` identity together
with the unchanged `paper/math_commands.tex` and `paper/references.bib`
identities. No previous source review may substitute for either fresh review.

SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED
