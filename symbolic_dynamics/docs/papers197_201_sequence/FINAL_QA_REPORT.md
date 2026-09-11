# Route A: completed five-paper batch after P196

2026-09-05 UTC. **TERMINAL_PASS / FIVE_PAPERS_COMPLETE_INTERNAL /
OWNER_AMBER / HOLD_EXTERNAL**.

The completed set is **P197 / P199 / P200 / P202 / P203**. These are the
five retained notes of the original P197--P201 batch, after the documented
P198/P201 withdrawals. Every note has a complete anonymous four-page
manuscript, two actual accepted paper reviews, a physical accepted Round2,
two terminal source-only builds and actual viewing of every final page.
ROUND2_REPORT.md records each theorem-level advance and accepted delta.

## Actual complete terminal audit

Root executed qa/audit_batch.py in a fresh process (session30736), starting
by09:19:46 UTC and observing successful completion at09:29:14 UTC. These
are observation timestamps, not benchmark runtimes. The process exited0
and its verbatim stdout is qa/FINAL_TERMINAL_AUDIT.txt, SHA-256
5c2a1eb7190b81709bce847e9b7fa56f98a2818b71fa389af8fb5d0355d5edad.

| Actual final audit item | Result |
|---|---:|
| Retained papers / complete manuscript review packages | 5 / 10 |
| Final PDF pages, each actually viewed at180dpi | 20 |
| Separate physical terminal source-only cold builds | 10 |
| Resolved bibliography records | 16 |
| Fresh author verifier executions in this audit | 10 |
| Fresh Review A/B verifier executions in this audit | 20 |
| Mechanical full-audit checks | 14,607 |
| Current retained-paper open Critical / Major / Minor findings | 0 / 0 / 0 |

Every author/A/B implementation was run twice and both complete output
strings equalled its own frozen canonical. The per-canonical check sums are
13,428,016 author,24,838,472 A and19,844,609 B, totaling58,111,097.
Each canonical was executed twice in the full audit; these counters are
finite check counts, not theorem, system-subclass or independent-review
counts. Earlier scout, author, individual-paper and root-gate runs are not
silently added to these totals.

| Paper | Author checks/run | A checks/run | B checks/run | Accepted Round2 PDF SHA-256 |
|---|---:|---:|---:|---|
| P197 | 3,998,247 | 4,814,623 | 4,833,354 | 42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a |
| P199 | 1,496,779 | 1,926,465 | 1,026,386 | b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0 |
| P200 | 3,595,488 | 3,823,696 | 4,026,047 | 7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea |
| P202 | 3,962,690 | 12,775,204 | 8,456,463 | e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a |
| P203 | 374,812 | 1,498,484 | 1,502,359 | 0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d |

All five live PDFs equal their accepted Round2 and both new terminal cold
outputs. All fifteen physical frozen rounds, all original/Round1/Round2
PDF roles, complete paper and nested QA coverage, ten complete review
trees,195 current input pins, source citations, anonymity, visible current
HOLD declarations, fonts, clean final logs and exact five-target global
manifests passed. Original legacy four-file freezes are honestly preserved
as such; modern full freezes are not retroactively invented for them.

## Final lifecycle refresh, clearly not another mathematical replay

After the successful full audit, root changed only P203's current README,
PAPER_IMPROVEMENT_STATE and IMPROVEMENT_LOG to record completed status.
Its current package manifest and the corresponding global manifest row
were refreshed. The old manifest bytes are preserved under qa/ as
P203_PACKAGE_BEFORE_LIFECYCLE_REFRESH.sha256 and
PACKAGE_MANIFESTS_BEFORE_LIFECYCLE_REFRESH.sha256.

The separate qa/audit_final_hash_refresh.py actually exited0 (session57089),
passing15,301 mechanical checks. Its verbatim output is
qa/FINAL_HASH_REFRESH_AUDIT.txt, SHA-256
7171f5d3335722df6fbf2bc71e114e5f5bb0d807004594a2b53fef5501737b47.
Its status is explicitly HASH_REFRESH_PASS_NOT_A_NEW_REPLAY. It checks
57 exact unchanged scientific inputs, every refreshed package and frozen
version, complete review coverage/pins, all PDF/build structures, final
lifecycle labels and both five-target globals. It executes zero new
mathematical verifiers, builds or visual inspections. No second full
numerical audit is fabricated for a status-text-only edit.

The final five paper trees contain785 files, the ten review trees340;
final build/image files are already included in those counts. P203's final
paper manifest has259 nonself entries and SHA-256
447459ff4e8c7e54b24a9cf3086565b9ca1906a7752c5b0dffc74906a211c78d.
Each of the five qa_final manifests covers32 nonself payload files.
CANONICAL_PDF_MANIFEST.sha256 and PACKAGE_MANIFESTS.sha256 bind exactly
the five retained final PDFs and five current paper manifests respectively.
qa/TERMINAL_SCIENTIFIC_INPUTS.sha256 additionally binds all ten sealed
review manifests and all five final-QA manifests, source/code/canonical/
PDF inputs and the actual full-audit/build code versions.

## Honest review, presentation and archive boundaries

The ten paper reviews were performed by processes distinct from the
respective mathematical authors, with materially different implementations.
Their earlier candidate familiarity and code reuse are disclosed in
reviews/PROCESS_SEPARATION_LEDGER.md. This is not blind, model-diverse,
external-specialist or human review. No outside review API, paper upload,
notification or external release was performed. The proof-writing and
paper-compile workflows supplied full theorem/counterexample separation,
two real rounds and actual source-only/page QA; unavailable external-model
and optional pypdf-reader steps are not falsely reported as successful.

Only P203 changed its main manuscript between original Round0 and Round1:
A-M1 added the required visible release-hold paragraph. The original
617cea5d PDF is preserved; its exact historical role/path/hash has a
HOLD-marker-only exception. Current/Round1/Round2 have no such exception.
All mathematical statements, proofs, bibliography, author code and canonical
remained unchanged. B accepted the repair version unchanged. The two
rejected P198/P201 drafts did not receive manufactured accepted rounds.

P203's separate historical Stage1 intermediate-code archival Minor1 remains
unrepaired; its old pin list still yields3PASS/1FAIL. That old outcome is
preserved rather than hidden by the current-paper zero-open census. The
present all-size proof and physical runtime inputs do not depend on the
unavailable bytes. The global gate follows current input snapshots, not
obsolete targets embedded inside a historical document.

The fixed-Git-object preflight separately verified that all195 current
review input references (150 distinct files) already matched actual Git
blobs at9a394ee2;31 references use16 explicitly mapped historical paths
under symbolic_dynamics/. No additional old evidence rescue was needed.
The later79e8729b checkpoint was actually pushed with all five Round2
packages, ten reviews and terminal builds before the global audit finished;
it is a pre-completion checkpoint, not mislabelled the completion commit.
The final completion/state synchronization is recorded in GIT_SYNC_RECEIPT.md
after its actual push. Split Git layout and unrelated parallel henon work
are preserved; no force push or history rewrite is authorized.

## Scientific ceiling and next-batch boundary

The corrected ledger has57 current attempts (5 selected,3 reserve,49 killed),
plus18 historical controls and8 code-only WIP. It does not certify57 distinct
validated dynamical subclasses. P200's narrow/square sharp clock remains
unproved. Existing primitive/method owners are deducted in every paper;
MCT does not claim a new Johnson bound, and OR does not claim a new parking
mechanism. Bounded source searches, missing P51--P56 and historical Git
gaps remain explicit. No global novelty/priority or Hilbert--Polya A4
completion is implied. The route is still A; all five papers remain
OWNER_AMBER / HOLD_EXTERNAL. The next ordinary five-paper batch begins
with fresh scouting and numbering after P203, without recycling rejected
systems or automatically promoting reserves.
