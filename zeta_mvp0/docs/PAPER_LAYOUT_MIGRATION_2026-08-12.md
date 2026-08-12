# Paper layout migration — 2026-08-12

This repository now stores each paper as an immediate child of `zeta_mvp0/`:

```text
zeta_mvp0/papers/paper_01_clock_preserving_henon/
  -> zeta_mvp0/paper_01_clock_preserving_henon/

zeta_mvp0/papers/paper_02_certified_local_wave_trace/
  -> zeta_mvp0/paper_02_certified_local_wave_trace/
```

The redundant `zeta_mvp0/papers/` container and its duplicate index were
removed.  Each paper remains a self-contained package: manuscript, source,
tests, protocols, compact results, and historical evidence move together.

## Historical evidence boundary

This is a repository-layout change, not a replay of past experiments or a
new scientific release.  Frozen JSON, manifests, receipts, exact historical
commands, and source files already bound by published evidence retain their
original bytes.  Absolute paths in those records continue to name the
environment in which the evidence was captured.

Paper 02's pre-migration V2 role-5 publication identity is:

```text
reviewed commit C:
  81a4d56df7dd66bb1d296187915d5b5ddc48be22
artifact SHA-256 H:
  e551a9e3d703041240f35e255fb30e94d8cfc4b27bbdfe038dd784d1d45fc237
original destination D:
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json
publication authority A:
  ROLE19_DESIGN_REVIEW_PUBLICATION_ONLY
publication commit P:
  8f4e006ab5997201115ee14fa0477555edd67a20
```

The byte-identical file carried to the new paper directory is a relocated
historical artifact.  It does not retroactively change `D`, does not count as
a second publication, and is not active authority for the new repository
path.  The move also changes the Git paths under which reviewed inputs live.

Consequently, Paper 02's path-bound control chain is fail-closed at the new
root.  No role 10 or later control object, run initialization, production
authorization, or scientific dispatch may rely on the old role-5 review.
A future control generation must use a distinct generation identity and
canonical path, bind the relocated inputs and their new commit, and pass a
fresh independent review before downstream work resumes.

The mathematical status is unchanged.  In particular, this migration adds
no theorem, no zeta-zero correspondence, and no result toward the Riemann
hypothesis.
