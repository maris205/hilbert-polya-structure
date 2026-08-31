# P26 Stage 5 entry decision — 2026-08-31

## Decision

**ENTER STAGE 5 / `in_progress`.** The scholar's 2026-08-31 authorization,
relayed in the current Stage-5 task after the accepted fresh Stage-4.5 Round-2
integrity pass, satisfies the mandatory Stage-5 entry decision. This decision
authorizes format-only finalization preparation. It does not constitute the
separate in-stage content confirmation required before a final PDF may be
created.

The sole remaining Stage-5 gate is therefore **one scholar content
confirmation** of the prepared content proof. Until that confirmation is
recorded, no final `paper.pdf` may be generated or promoted.

## Scholar decision record

The exact scholar response is:

> 确认

It answers the immediately preceding mandatory Stage-5 entry prompt and
retains the already specified current `plainnat` numeric citation profile. It
does **not** answer the distinct in-stage content-confirmation prompt, which
remains pending.

## Locked entry basis

- Root input lock:
  `BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json`, SHA-256
  `bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30`.
- Accepted Stage-4.5 TeX:
  `notes/stage4_prime_revision_round2.tex`, SHA-256
  `345c258b5a1097c67d4f7777167b90eee208d6b2d36b23655990269a4de42203`.
- Accepted bibliography: `paper/references.bib`, SHA-256
  `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f`.
- Accepted content proof: `notes/stage4_5_round2_preview.pdf`, SHA-256
  `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da`.
- Stage-4.5 verdict: `PASS`; Stage 5 is entered without Route advancement.

## Format and scope decisions

- Citation profile stays `natbib` numeric with `sort&compress`, and
  bibliography style stays `plainnat`.
- Stage 5 is format-only. Scientific statements, declarations, authorship,
  initial dynamical-system restriction, subtype, registered claim strength,
  Route tuple, result artifacts, and accepted bibliography bytes are frozen.
- `stage5_finalization/manuscript.tex` may differ from the accepted TeX only
  by removal of standalone ARS `<!--block:B####-->` transport-marker lines.
- The canonical `paper/manuscript.tex`, `paper/paper.pdf`,
  `paper/references.bib`, and `results/` tree remain unchanged.
- The content proof is for confirmation only. It is not the Stage-5 final PDF.

The separately carried cross-document advisories are nonblocking and are not
reinterpreted here: `#660` is `not_checked/SNAPSHOT_NOT_PROVIDED`, and `#672`
is `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.
