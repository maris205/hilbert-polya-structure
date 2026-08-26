# P22 Stage 4 chain-start integrity audit

Date: **2026-08-25**

Verdict: **PASS**

The Stage-2.5 integrity gate closed with zero open issues for
`paper/manuscript.tex` at SHA-256
`5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc`.
For the Stage 4 patch chain, the official ARS anchorizer was replayed on a
temporary byte-copy of that exact manuscript.  The replay produced 102 blocks
and was byte-identical to both chain-start artifacts:

- anchored draft `notes/stage3_revision_base.tex`, SHA-256
  `32f7bea67f6c837a7e8b26b35aeb0297a13ec2c7f910abc09617dcb817c4a4a8`;
- block manifest `notes/stage3_revision_base.block-manifest.json`, SHA-256
  `b21625abd194fc2f0cfdba0eb0193da5915bc81e4a7d26056a770c58f767cc91`.

The anchorizer is content-neutral: removing its marker lines reproduces the
integrity-PASS manuscript bytes.  No manuscript text was rewritten between
the closed integrity gate and this exact chain start.  The anchored draft
therefore carries the same zero-open-issue integrity state for purposes of
the continuous revision-evidence chain.

This receipt does not pre-approve any Stage 4 edit.  Each edit remains bound
to the immutable roadmap, explicit author adjudication, claim-surface
boundary, patch, apply report, and later E6 semantic review.
