# Paper 28 Stage 4 draft-writer emission receipt

Status: **PASS — EMITTED, NOT APPLIED**

Emitter: `draft_writer_agent`  
Revision round: 1  
Executed at: `2026-08-30T07:39:23Z`

## Emitted artifacts

| Artifact | SHA-256 |
|---|---|
| `notes/stage4_revision_patch_round1.json` | `37f8ac948f1d8a6aab65f16f10d916d89629208d341871e22f0710cb1fe4ef12` |
| `notes/stage4_response_to_reviewers_provisional.json` | `97b305e6956c01a81cee266869640c3e8a4f52146d747b9f307cb6905dea13d0` |

The patch uses `revision_patch` format 1.1 with
`authorization_context=review_roadmap`. It was emitted as a sidecar only.
No patch-application command was run, no revised manuscript was emitted, and
no apply report was created.

## Frozen authority bindings

| Authority artifact | SHA-256 |
|---|---|
| Anchored base `notes/stage3_revision_base.tex` | `743a047cbe5f6227fbfaa5fef3169029b339af5790218df4ddf8f7cac2987f59` |
| Block manifest | `e70d9d74f0e1396938b75e7908e2f86008a5934cb635f8393bc7f5595c9774c0` |
| Stage-3 roadmap | `721a659d16f7f0c07d0cf8bca6bac298067855c8a19aa643179e0825c5a74bcf` |
| Author adjudication | `52483b12b49eb8220a183889f71f231dabfa525b2bb417c483a9897ec8082e14` |
| Author decision digest | `f752e376c82da8bab1030184a6d04053c0220097d3ee2890afe08298ce1a206d` |
| Claim-surface manifest | `269a55d6e2590dc2e0bac8c9b98f5e10f63def23e31f2c7871526fc583f5c5e2` |
| Batch authorization request | `174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63` |
| Author event | `5e5ad1b6ff2a62060368877016ad4b14f869f22a3e38f9a703672ea52ecd067f` |
| Writer handoff | `95d62f1985827519c5f5dd12008330351ad3bc27dd82a57d3ca5c16a0978d4e2` |
| Writer brief | `258c56f66078edbcfdc2b0c2b64c2308d89b3e3f0b6c7a8979e02d5e6af2ef1e` |

The patch binds the base by hash12 `743a047cbe5f` and carries the exact
roadmap, author-adjudication, author-decision, and claim-manifest digests above.

## Authorized operation log

| Item | Emitted operation | Resolution |
|---|---|---|
| `REV-01` | `B0099/replace_block`, old hash `081f62863008` | Corrected the replay order: isolated proof guards and finite traversal/reconstruction precede `build_validation`; validation checks the freeze, upstream locks, source matrix, theorem fields, and output bindings; verify-only comparison remains temporary and read-only; canonical change requires validation PASS and the explicit refresh path. |
| `REV-02` | `B0048/replace_block`, old hash `af8144e37c5a` | Retained the original invariant account byte-for-byte as the replacement prefix and added the executed direct coverage for repeated Delta cancellation, global-negation idempotence, both generator/inverse orders, and sampled collisions. The text discloses that the tests import the audited builder and do not independently implement the eight-transition closure checker. |
| `REV-03` | `B0106/insert_after`, old hash `c61d4c8ac144` | Added a non-ranking A0–A4 obligation legend. The full P28 tuple remains unassigned; the historical proxy `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` remains unpromoted; the exact systole/cutoff remains A0–A1 infrastructure only; 144 remains an element count; all matched, owner, magnetic, A2, determinant, A3/A4, spectral, and Route-B work is recorded as not run. |
| `REV-04` | `B0037/insert_after`, old hash `774b4aee8097` | Added the typed present map from the fixed control surface, exact PSU(1,1) element state, and target-blind cutoff to geodesic length and the retained cutoff. Magnetic Hamiltonian/flow, clock/action, owner quotient, multiplicities, determinant weights, analytic continuation, and spectral realization remain separately typed and unconstructed, with no A2/A3/A4 or Route-B inference. |

There is exactly one operation per target block and exactly one roadmap item
per operation. Every `claim_strength_changes` and
`collateral_authorization_ids` array is empty. No reference command or
bibliography entry was added.

## Patch and surface validation

The current ARS schema and parser were loaded from the installed
academic-research-suite. A non-writing in-memory preflight called
`validate_patch` and the splice function without emitting the hypothetical
draft.

- revision-patch 1.1 schema: **PASS**
- canonical emitter identity `draft_writer_agent`: **PASS**
- base hash and four target old hashes: **PASS**
- author target/operation authority: **PASS**
- duplicate target check: **PASS** (4 distinct targets)
- fragment parsing: **PASS** (one text segment per operation)
- structural checkpoint: **PASS**, no flag
  (`section_count_delta=0`, `touched_ratio=0.0161`,
  threshold `0.6`)
- hypothetical block count: 124 to 126, solely from the two authorized
  `insert_after` operations
- registered ClaimIntent surfaces: **PASS**, all 14 occur exactly once and
  byte-identically in the in-memory hypothetical result
- unregistered-drift guard: the complete original B0048 text is retained
  byte-for-byte as the replacement prefix; B0099 changes only the authorized
  replay-sequencing account; all other base blocks are untouched
- new references: 0
- claim-strength replacements: 0
- collateral authorizations used: 0

The provisional response contains four resolved items in completed or
present-perfect wording. Its only provisional status is top-level; it records
`apply_status=NOT_APPLIED` and omits post-application mechanical fields as
required.

## Executed scientific regression and replay evidence

Command:

```text
cd code && PYTHONDONTWRITEBYTECODE=1 python -m unittest -v \
  test_stage4_round8_invariants.py \
  test_round8_control_systole_certificate.py
```

Result: **PASS, 28/28 tests** (4 direct Stage-4 tests and 24 legacy Round-8
tests).

Direct properties confirmed:

- two consecutive common Delta factors cancel to the exact identity fixed
  point;
- global-negation normalization returns the same canonical state and is
  idempotent;
- all four `g_j g_j^{-1}` and all four `g_j^{-1} g_j` products close
  exactly;
- all 585 words through length three yield 457 canonical states and nine
  collision buckets, including nine distinct sampled words normalizing to
  identity.

Assurance boundary: `code/test_stage4_round8_invariants.py` imports the
audited Round-8 builder. It is a direct same-builder regression suite, not an
independently implemented eight-transition closure checker, and the patch
makes no independence claim.

Command:

```text
bash experiments/reproduce_round8.sh
```

Result: **PASS**. The script passed its 24 tests, ran two fresh temporary
builds, and reported:

```text
run1_tree_sha256=c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac
run2_tree_sha256=c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac
byte_identical=true
```

The temporary trees matched the checked-in products. The canonical
`results/round8_*` tree retained SHA-256
`6a7738fea6f06f3b77f7c74744421263fcf2d1461207fed9c764184614638d83`.
No canonical result was refreshed and no scientific value changed.

Supporting evidence remained bound to:

- `notes/stage4_round8_invariant_localization.md`:
  `02ea386526347f18da221fe408deb4aee4519c67e019fb308b090ad96fbe113b`
- `experiments/stage4_round8_invariant_receipt.json`:
  `f235c254dcbad3930556ca0142255ae23d7da904c5fa3395cf3605bc11bb0b11`
- `code/test_stage4_round8_invariants.py`:
  `a584f2a2143b2b0aa44a58095014cd2c5791851461fe1ca7edc60e085b06fb89`

## Scope firewall

The formal P28 tuple is unassigned. The historical proxy remains
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` without
promotion. No matched Bolza/control census, owner quotient, magnetic
comparison, signed-field A2 evaluation, determinant or analytic-continuation
construction, A3/A4 or spectral result, or Route-B work was executed. The
canonical manuscript SHA-256 remained
`864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7`;
the anchored base remained
`743a047cbe5f6227fbfaa5fef3169029b339af5790218df4ddf8f7cac2987f59`.

Final writer disposition: **PASS — patch and response emitted; patch not
applied.**
