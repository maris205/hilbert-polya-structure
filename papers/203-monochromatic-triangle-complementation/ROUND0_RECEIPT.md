# P203 physical Round0 freeze

Date: 2026-09-05 UTC. Physical payload frozen by08:13:09 UTC.
**ROUND0_AUTHOR_READY / REVIEW_A_AND_B_PENDING / HOLD_EXTERNAL**.
This receipt authorizes handoff of the supplied version, not review acceptance.

## Exact bearing inputs

| Artifact | SHA-256 |
|---|---|
| main.tex | a08983002caf08109c6a6406183149343aaa5ecd9a6d08af7f521f8ca85480b0 |
| references.bib | 2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a |
| main.pdf = main_round0_original.pdf = frozen_round0/main.pdf | 617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167 |
| verify_p203.py | 77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d |
| CANONICAL.txt = AUTHOR_RUN1.txt = AUTHOR_RUN2.txt | 6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00 |
| PROOF_PACKAGE.md | 04d28178f630a1b0c404bfc26c0d9cd561c2898e4f585f0168d43ef93d2ec9b7 |
| temporal_author_audit.md | f150027508bcdfcc0f22706754fee3b6e645e9027cda3e56eba0e6c0d5a91a56 |

## Physical manifests and their scope

- frozen_round0/SHA256SUMS:
  `4bd31b8f118d7508db30c99145c69aed508ef0efb33d815a37f8722b37ed1f8b`.
  Covers all36 nonself frozen files: standalone text/bibliography/code/PDF,
  actual replay outputs, author memos, eleven physical current-input
  snapshots and primary-source files/manifest. This is not a symlink freeze.
- CURRENT_INPUTS_SHA256SUMS:
  `1327f9bd0177b5e20d29944bfa702b31a81ba481a37e068210fdaa1fdbbe8fdc`.
  Covers all11 supplied current snapshots, relative to the paper directory.
- qa/SHA256SUMS:
  `c62d833d42d8a3cd4f08bdefdbc04c92b8b466aa24a0cce37bd6b4023db98974`.
  Covers all47 nonself QA artifacts: retained draft and both final source-only
  builds, logs/recorders and draft/final page renders.
- sources/SHA256SUMS:
  `7084b547be15e60998373ee19a42897cf9d1ab511cf1986f39673e53b08880fe`.
  Covers both actual primary downloads.

The top SHA256SUMS covers the complete current author artifact tree except
itself, including this receipt and each nested manifest. frozen_round0 does
not contain this post-freeze receipt or the later top manifest; those are
external identity records, avoiding circular digest claims. No new file or
edit is to be placed inside frozen_round0 after this receipt.

## Actual execution and visual evidence

Paper-local Replay1 completion7456f6 and Replay2 completion6d26da each
reported374,812 assertions on33,868 states across n=0,…,6; the raw outputs
were directly compared and physically saved. No independent-review count
is claimed. BUILD.sh launched two final new source-only builds, completion
receipts9c45bb and f89023; actual PDF cmp returned0 in4bbeff. Both produce
the four-page286,868-byte PDF pinned above. All21 font entries are embedded,
the metadata is anonymized, and neither final log has warning/bad-box/
undefined-reference/citation matches. All four final pages were actually
viewed at120dpi; complete extracted text was also read. BUILD.md and
SELF_QA.md provide page-specific observations.

The temporal coauthor's exact Section2 compression check is additional
author checking, not paper A/B. Its main.tex digest equals this freeze.
No FOSP optional vertex-zero lemma was adopted. The manuscript retains
the original complete initial-retired proof and uniform witness.

## Historical finding remains unrepaired

Stage1 admitted internally amber with Critical0/Major0/Minor1: authentic
intermediate author probe bytes are missing. The original external pin
continues to fail. Its list is supplied as an immutable historical document,
not executed as the new paper's runtime/input requirement. Passing its
containing-file hash does not repair the old missing program. PROVENANCE.md
and the physical Stage1 delta disclose the exact version boundary.

The current paper has complete physical inputs and standalone proof/code;
paper A/B must still independently assess those actual inputs and reach
their own findings under the project zero-open-finding rule. No reviewer
scores, accepted deltas, Round1/2 PDFs, FINAL_QA or external release are
manufactured in this author freeze. Root controls the next two rounds.
