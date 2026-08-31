# P27 Stage 5 entry decision — 2026-08-31

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
  `notes/stage4_prime_revision_round1.tex`, SHA-256
  `803d9e7d69c233363d912b4fee25f5915b7f07d48937b794ee11c807ca182ef7`.
- Accepted bibliography: `paper/references.bib`, SHA-256
  `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981`.
- Accepted content proof: `notes/stage4_5_round2_preview.pdf`, SHA-256
  `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208`.
- Stage-4.5 verdict: `PASS`; Stage 5 is entered without Route advancement.

## Format and scope decisions

- Citation profile stays `natbib` numeric with `sort&compress`, and
  bibliography style stays `plainnat`.
- Stage 5 is format-only. Scientific statements, declarations, authorship,
  the frozen coordinatewise geodesic-flow restriction, subtype, registered
  claim strength, both Route tuples, result artifacts, and accepted
  bibliography bytes are frozen.
- `stage5_finalization/manuscript.tex` may differ from the accepted TeX only
  by removal of standalone ARS `<!--block:B####-->` transport-marker lines.
- The canonical `paper/manuscript.tex`, `paper/paper.pdf`,
  `paper/references.bib`, and `results/` tree remain unchanged.
- The content proof is for confirmation only. It is not the Stage-5 final PDF.

The separately carried cross-document advisories are nonblocking and are not
reinterpreted here: `#660` is `not_checked/SNAPSHOT_NOT_PROVIDED`, and `#672`
is `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.
