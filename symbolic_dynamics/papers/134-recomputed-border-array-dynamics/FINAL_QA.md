# Final QA — P134 whole-array border recomputation

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- Final `main.tex` SHA-256:
  `4fac43a74db22838e1595975c73972360cc3aa54e79530feaa3a22e5bc3153b6`.
- `main.pdf` and `main_round2.pdf`: 323,103 bytes, five A4 pages, SHA-256
  `7d69a1e9338e9421ef31ac3e265a35317e0d11c836f1a652a76a69c36b923962`.
- `main_round1.pdf` remains immutable at
  `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525`;
  `main_round0_original.pdf` remains immutable at
  `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`.
- Exact paper-local assertions: **1,694,506**.

## 2. Fresh verifier replay

The terminal run in `/tmp/p132-136-terminal-verifiers.TCvHXQ` reproduced the
989-byte canonical stdout byte for byte (`cmp=0`), with SHA-256
`cce8c343276f5a299cb2c723e8b1957020749f74ff36a9aeb8462253c4b34d3e`
and terminal line `STATUS=PASS`.  The verifier source SHA-256 is
`3aec6dd12c1e9472e1734061ba4c006d94e2e94a6d255f7dede25464cb7d162d`.
Enumeration through `n=9` and larger sharp witnesses are falsification only.

## 3. Isolated build

Only the source and bibliography were copied to
`/tmp/p132-136-final-builds.RetOwU/134-recomputed-border-array-dynamics`.
The four-stage build exited zero and reproduced `main.pdf` and
`main_round2.pdf` byte for byte.  Settled logs have no error, warning,
undefined citation/reference, multiply defined label, bad box, or rerun
request.

## 4. PDF, bibliography, and anonymity

The PDF is version 1.5, A4, rotation zero, unencrypted, form-free,
JavaScript-free, and has no metadata stream, raster image, or attachment.
Identifying metadata is blank and the visible author is `Anonymous`.  All
**24/24** font rows pass embedding, subsetting, and Unicode mapping.  All
**4/4** references are cited and resolved.  Every page has searchable text;
marker and identity-leak scans are clean.

## 5. Five-page visual audit

- Page 1: whole-array definition, failure-link firewall, and image theorem are
  clean.
- Page 2: canonical cycles and indexed mismatch cases fit without collision.
- Page 3: the corrected `preceding A_r-case` pointer, recurrent atlas, and
  sharp trajectories are visibly correct.
- Page 4: small boundaries, factorial fibre proof, exact controls, limitations,
  and first reference are complete.
- Page 5: the remaining three references are legible; the large residual
  whitespace is intentional page flow, not an empty or broken page.

## 6. Review closure and decision

Both Review-A clarifications are closed.  Review B plus a separate secondary
audit found only the stale paragraph pointer and package-index state; both are
closed, and the original reviewer confirmed the distinct Round-2 build.
Final severity is critical 0, major 0, minor 0.

**PASS / GO_INTERNAL.**  The anonymous internal theorem package is coherent
and reproducible.  **HOLD_EXTERNAL.**  Bounded owner search does not establish
novelty, priority, or permission for any external action.
