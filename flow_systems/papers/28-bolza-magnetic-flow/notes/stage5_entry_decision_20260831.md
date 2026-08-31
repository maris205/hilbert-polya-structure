# Paper 28 Stage-5 entry decision — 2026-08-31

Status: **Stage 5 in progress; awaiting one in-stage content confirmation**.

## Scholar decision

Exact response:

> 确认

This response confirms the immediately preceding mandatory Stage-5 entry
prompt.  It also retains the already specified current citation profile:
`natbib[numbers,sort&compress]` with `\bibliographystyle{plainnat}`.  It does
not supply the separate in-stage confirmation of the content proof; that one
content confirmation remains pending before the final PDF build.

## Accepted authority

- The accepted manuscript is
  `notes/stage4_prime_revision_round1.tex`, SHA-256
  `126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e`.
- The accepted bibliography is `paper/references.bib`, SHA-256
  `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e`.
- The Stage-4.5 Round-2 integrity verdict is `PASS`; its final report has
  SHA-256
  `9ce7de406d5f28e6a5efcfa1320c653296d2b7f639ed278507e78e1deafd6fa7`.
- The batch input lock is
  `BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json`, SHA-256
  `bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30`.
- The scholar-authorized citation profile remains
  `natbib[numbers,sort&compress]` with `\bibliographystyle{plainnat}`.

## Authorized preflight operation

The formatter may remove only standalone ARS block-marker lines matching
`^[ \t]*<!--block:B[0-9]{4}-->[ \t]*$` from the accepted manuscript.  The
operation removed 127 marker lines and no manuscript-content line.  The
resulting Stage-5 source is `stage5_finalization/manuscript.tex`, SHA-256
`14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22`.

`stage5_finalization/references.bib` is a byte-identical copy of the accepted
bibliography.  `stage5_finalization/content_proof.pdf` is a byte-identical copy
of the 14-page Stage-4.5 preview, SHA-256
`253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382`.

The Stage-5 entry #660 and #672 advisory carriers are orchestrator-owned and
remain nonblocking.  This Paper-28 formatter preflight did not create, replace,
or reinterpret either carrier.

## Preserved boundaries

No scientific, declaration, Route, subtype, canonical source, result, or
bibliography content is changed.  No submission, public release, external
contact, Git action, Route promotion, A2 evaluation, or Route-B invocation is
authorized.  `stage5_finalization/paper.pdf` is intentionally absent.

## Next required action

The scholar must review `stage5_finalization/content_proof.pdf` and provide one
explicit content confirmation before a final `paper.pdf` may be built.  Until
that confirmation, Stage 5 remains `in_progress`.
