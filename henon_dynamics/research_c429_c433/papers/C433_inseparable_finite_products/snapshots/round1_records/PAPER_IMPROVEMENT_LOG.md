# C433 manuscript improvement log

Status: **round1_revised_pending_second_review**.
Author revision 1 was explicitly authorized by the coordinator after full
adjudication of the actual pass-1 manuscript review and citation audit.
The changes below are implemented and author-checked; nonauthor pass-2
confirmation and later release gates remain pending. No numerical score
was requested, assigned, inferred, or copied from a workflow example.

## Immutable full raw review records

The complete raw reports are retained, without editing, summarizing in
place, or truncating them:

- [E8 full manuscript pass-1 review](reviews/round1/REVIEW.md), 443 lines,
  SHA256 `23b397bae79f137c323f37405024537995b64375d4ffd201558a5ececcc071a9`.
- [X2 full citation audit](reviews/citations/REPORT.md), 236 lines,
  SHA256 `aa5fdfa7b9d2b635f25a6e9ac5d267529fa0ed879e3f1c54a0fab6c570551fbf`.

Both full records were read by the author before applying any revision,
and their hashes were checked before and after the changes. These links
bind the full original reports, not selected excerpts. The review is the
actual current-team internal nonauthor manuscript pass 1, not external
peer review and not a relabeling of the earlier research-proof review.
The same E8 reviewer is intended for the coordinator-assigned pass 2.

E8 found zero Critical, zero Major, and three required Minor items, with
no repair to the body theorem or proof. X2 recommended the one Minor
editor-accent normalization and identified the optional author-name
accent variant. Its unavailable Retraction Watch database check remains
an explicit screening limitation, not a negative result or clearance.

## Adjudicated responses

| Item | Implemented response | Actual verification | Current status |
| --- | --- | --- | --- |
| M1: missing explicit condition in summary | Defined the cofinite product condition as (CP) in the abstract and made the visible-period conclusion start “Whenever (CP) holds.” The introduction now says “Under the cofinite product condition (CP).” | Revised source and PDF page 1 read; the formal theorem and Proposition 6.2 are unchanged. | Implemented; awaiting pass 2 |
| M2: two bare diagonal names | Replaced exactly the two `diag` occurrences in equation (5.7) by the existing `\diag` operator. | Source readback and actual revised PDF page 7 show both upright operators. | Implemented; awaiting pass 2 |
| M3: internal review disclosure | Added the truthful sentence that the underlying argument underwent current-team internal nonauthor mathematical review, explicitly not external peer review or publication acceptance. | Revised source and PDF pages 10–11 read; existing AI/shared-development attribution retained. | Implemented; awaiting pass 2 |
| CIT-M01 | Restored editor names González-Vega and Tomás in the CDS entry. | Generated `.bbl` and actual PDF page 11 read. | Implemented; awaiting pass 2 |
| CIT-I01, optional | Chose the documented primary-source spelling Joël Ouaknine. | Generated `.bbl` and actual PDF page 11 read. | Implemented; no identity/DOI change |
| CIT-I02 | Preserved the audit's incomplete public-retraction-screening qualification. | Full immutable audit linked above; no retraction-free claim added. | Limitation retained |

No theorem, proof step, coefficient, return bound, native-clock convention,
support distinction, source identity, or DOI was changed. No new example,
experiment, reference, or mathematical claim was added. Only five source
files changed: `main.tex`, sections 1, 5, 8, and `references.bib`.

## Exact substantive source delta

The following is the complete changed-line content against the frozen
`snapshots/v1_baseline/` source, omitting only unchanged diff context:

```diff
--- main.tex
-the zeros and poles of $g$ and have product one. Put
+the zeros and poles of $g$ and have product one (condition $\CP$). Put
-arbitrarily long returns. In particular, each product-visible
+arbitrarily long returns. Whenever $\CP$ holds, each product-visible
--- sections/01_introduction.tex
-a fixed annihilator. A separate rank argument bounds the native
-period of each visible exceptional cycle, making a universal
+a fixed annihilator. Under the cofinite product condition $\CP$,
+a separate rank argument bounds the native period of each visible
+exceptional cycle, making a universal
--- sections/05_transfer.tex
- \mathsf M_\epsilon=diag(T_{X^\epsilon A},T_{X^\epsilon B}),
+ \mathsf M_\epsilon=\diag(T_{X^\epsilon A},T_{X^\epsilon B}),
- \mathsf B_\epsilon=diag(T_{SX^\epsilon A},-T_{SX^\epsilon B}).
+ \mathsf B_\epsilon=\diag(T_{SX^\epsilon A},-T_{SX^\epsilon B}).
--- sections/08_conclusion.tex
+The underlying argument also underwent current-team internal
+nonauthor mathematical review; this was not external peer review
+or publication acceptance.
--- references.bib
-  editor = {Gonzalez-Vega, Laureano and Recio, Tomas},
+  editor = {Gonz{\'a}lez-Vega, Laureano and Recio, Tom{\'a}s},
-  author = {Kiefer, Stefan and Murawski, Andrzej S. and Ouaknine, Joel
+  author = {Kiefer, Stefan and Murawski, Andrzej S. and Ouaknine, Jo{\"e}l
```

The actual `diff -u` output was read for all five files. `diff -qr`
confirmed that only sections 1, 5, and 8 differ among the section files.
The baseline source, original PDF, and frozen audit/build records were
not edited; their original hashes still match.

## Actual revision build and checks

The directory `build/revision1_20260909/` was explicitly checked not to
exist before creation. Exactly one revision build was run, with the
following command from the C433 paper directory, shell `pipefail` enabled:

```sh
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/revision1_20260909 main.tex 2>&1 | tee build/revision1_20260909/compile.log
```

It exited 0 and produced the revised 11-page, 374934-byte PDF. Actual
author verification was completed by the tool-clock reading
2026-09-09 21:17:14 UTC. The fixed PDF epoch is a build setting, not that
execution time. No old build directory was cleaned or overwritten.

The final `main.log` and `main.blg` have zero warnings, overfull/underfull
boxes, undefined references/citations, or errors. The cumulative
`compile.log` retains the ordinary early multipass reference warnings,
which resolved. All 22 font entries are embedded, subsetted, and have
Unicode mappings. The generated text has no unresolved-reference or
verification-placeholder markers; the two numbered citations and
bibliography entries still resolve.

All 11 revised pages were rendered by
`pdftoppm -r 95 -png main.pdf build/revision1_20260909/visuals/page`.
The author individually viewed the actual affected pages 1, 2, 7, 10,
and 11. Both (CP) qualifiers, both diagonal operators, the internal-review
disclosure, and all normalized accents print correctly, with no clipping
or overlap observed on those pages. This affected-page author check is
not represented as a new independent all-page manuscript review.

An initial text-inspection probe occurred while the separate extraction
command was still running and found no text file yet; it was repeated
after successful completion. The final results above use the completed
actual extraction, not that premature probe. The `.bbl`, changed source
passages, revised abstract/introduction, and ending PDF text were read.

`main.pdf`, `main_round1.pdf`, and the actual build PDF are byte-identical.
An exact source/bibliography/PDF snapshot is stored in
`snapshots/v2_round1/`; it does not replace `snapshots/v1_baseline/`.
The original `main_round0_original.pdf` remains unchanged. This is an
author revision build, not either of the two later clean release builds.

## Revised source/PDF identity

| File | SHA256 |
| --- | --- |
| `main.pdf` / `main_round1.pdf` | `489a1038a9e6f27f589e63b2be6dfe69485a6bd2ab6672360d4407b3ea49a7fa` |
| `main.tex` | `f5bade84a98663c6c2db3acede6b56810c1bbb04aeff192f98db9334d28c9cd3` |
| `references.bib` | `318f239a9934e4e9cd1e0467db8b989b0fd47911bda7ef58d3b85c74be93ef41` |
| `sections/01_introduction.tex` | `e9bebaea42b583d9842a2286bc2ace1df96233272019ca90ab9714eae0a37c4a` |
| `sections/02_statement.tex` | `3d6d5d65a715adb9a0c98f6257ab4f122491f02e81d9ff6e7458c8a0217b9f2a` |
| `sections/03_cycles.tex` | `49bccc2a0ba02bb8634b78cdc69cd38fa217691db0df7df27ea4ab47e6f2486c` |
| `sections/04_extractor.tex` | `20fc9ff6342288314cd71efcbdc1f9388455245b8186bf749809c103e662cb69` |
| `sections/05_transfer.tex` | `ef6e465ea6cd9fc2e70e09a9bdc504e811c3f2fe831c2aef2ed073b302d0927e` |
| `sections/06_rank.tex` | `53141c1b73f968333b4af2c180c678a50967df211c78f8190d95935b254fcc88` |
| `sections/07_decision.tex` | `88b84763f2ab5919de79d8d31b73ff40f6cfd06664b03e308dfb01c6b9477f4c` |
| `sections/08_conclusion.tex` | `f0929e8cca3d7eba6519755f71cdee503f6798de1dbd7472159cf8b9b25310c3` |
| Frozen `main_round0_original.pdf` | `8e58c361b89fe132183451f08b4817699ac02164e224a8cc6589d62e3bdb99f7` |

## Next gate and authority boundary

The revised live sources, bibliography, PDF, and round-1 snapshot are
frozen for the same E8 reviewer's coordinator-assigned pass 2. No pass-2
verdict, final release, external acceptance, or clean retraction screening
is claimed. No mathematical run, new agent, external-model/API review,
notification, package installation, Git, formal evaluator, final clean
build, shared manifest/seal, or external submission was performed.

The improvement skill supplied the review-response/rebuild/version-record
structure. The live state uses the skill's exact filename
`PAPER_IMPROVEMENT_STATE.json`; the coordinator clarified that the earlier
`STATE.json` wording was shorthand, and that initial file was moved rather
than leaving duplicate live state. The actual current-team reviewer,
immutable full-report links, absence of numeric scores, and pause before
pass 2 follow the coordinator's explicit assignment, overriding the
skill's legacy external-model and automatic-next-round examples.
