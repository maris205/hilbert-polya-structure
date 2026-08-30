# Paper 26 Stage 4 Round 1 writer receipt

Status: **RE-EMITTED (SECOND LAYOUT-ONLY CORRECTION) — NOT APPLIED**

## Role and authority boundary

This receipt records an independent draft-writer emission under the current ARS
revision-patch protocol.  The writer emitted the patch and provisional response
sidecars only.  It did not run `ars_apply_revision_patch.py`, create a revised
manuscript, refresh a canonical result, or enter a later pipeline stage.

The copied authority bindings are:

- anchored base: `notes/stage3_revision_base.tex`, SHA-256
  `af61f7b9a80b95bbc15c937ff0af3eed1ecc327965679324c51c376ad9dbb836`;
- block manifest: SHA-256
  `29f3d9fecdc8c11273a15298310ff58b27641d58d592d0f7d49d773a65e932a4`;
- revision roadmap: SHA-256
  `e58163c3796bde9eb524c972e44023c6afaf4f7885f1d55b2859886cc7216438`;
- author adjudication: SHA-256
  `62dcc634fb7c3305588033edd65ef8556b6b62d510d4cc3cae4aa34173bd68e5`;
- author decision digest:
  `a4b991894e2591586abb73209b3e100bbbd794e4afad8fb970dabe80f68ce7ee`;
- claim-surface manifest: SHA-256
  `d1ad38e0b7e71949abc0bc22a35bfce5ff6e1f5133067d8f8bcf8c4b4f52309e`;
- batch authorization request: SHA-256
  `174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63`;
- author event: SHA-256
  `5e5ad1b6ff2a62060368877016ad4b14f869f22a3e38f9a703672ea52ecd067f`.

All nine roadmap items are `will_address`.  There is no declined item,
collateral authorization, registered claim-strength replacement, structural
acknowledgement, canonical refresh authority, Route-B authority, or later-stage
authority.

## Emitted artifacts

- `notes/stage4_revision_patch_round1.json`
  - contract: `revision_patch` 1.1;
  - authorization context: `review_roadmap`;
  - revision round: 1;
  - SHA-256:
    `c885289ecbd8ac53b2d676657b3193778f1dd04536c80db56bbdfaa5f84f5ec5`.
- `notes/stage4_response_to_reviewers_provisional.json`
  - top-level status: `PROVISIONAL_WRITER_EMISSION_NOT_APPLIED`;
  - SHA-256:
    `8719844261d43bf285eef03a7eff6fa417704303071cf63c29d1022504a90646`.

The response items describe the emitted revisions in completed or
present-perfect terms.  Only the artifact-level status is provisional.
`change_block_ids`, inserted fresh block IDs, the apply-report path, and
`word_count_delta` remain explicitly assigned to the post-apply
orchestrator.

## First layout-only re-emission (historical receipt)

The prior writer-emitted patch had SHA-256
`9530a88c2662a4887d8cf87ce71470754a027c7e128118b477f23f6f4bfd1f2e`.
After the marker-stripped preview localized seven overfull boxes to appended
text in B0081, B0090, and B0093, the writer re-emitted the same Round-1 patch
with only those three operations' `new_text` values changed. Long supplemental
paths and SHA-256 strings now use breakable LaTeX `\path{...}` notation, and
the single overflowing sentence in B0090 is split without changing its
evidence domain. Registered ClaimIntent C-014 remains byte-identical and
occurs exactly once at the start of B0081. Counts, hashes, roadmap IDs,
authorized operations, scientific meaning, citations, Route boundaries, and
all other patch content are unchanged. This re-emission has not been applied.

## Second layout-only re-emission (current receipt)

The independent marker-stripped preview bound to patch SHA-256
`9c2224621511806b558fdf9f98e00c22da4c3987a9e9e6a9134da8b99c1a2f25`
reported exactly one remaining overfull hbox, `10.45026 pt`, localized to the
B0090 phrase `correspondence-component families`. The writer re-emitted the
entire patch and changed only that phrase to the equivalent, more breakable
wording `families of correspondence components`.

The other 24 operations remain byte-exact as JSON values. B0090's operation,
target, old hash, roadmap ID, explicit authorization arrays, every number,
scope limitation, Route boundary, and all text outside the one phrase are
unchanged. Replacing the new phrase with the old phrase in the re-emitted raw
patch bytes reconstructs SHA-256
`9c2224621511806b558fdf9f98e00c22da4c3987a9e9e6a9134da8b99c1a2f25`
exactly. The provisional response's nine item objects remain byte-exact; only
its top-level patch SHA-256 binding was updated.

A non-landed synthetic marker-stripped layout preflight reused the exact prior
Stage-4 revised source, made only this B0090 wording substitution, and ran
`lualatex`, `bibtex`, `lualatex`, `lualatex`. It produced 15 pages with zero
overfull hboxes, undefined citations, undefined references, missing glyphs, or
fatal errors. The synthetic PDF SHA-256 was
`8c124fe6001007af9ad7f41fd359cd121b5289708f463d318a30c153ffad14e9`;
the final synthetic log SHA-256 was
`04acbbb93728d8f4d146202a989040d76b86b691c4abbaec7763eb0436d4099d`.
These are preview-only receipts, not applied manuscript, canonical, or Stage-5
artifacts.

## Operation coverage

The patch contains 25 operations on 25 unique anchored blocks.  Under the ARS
structural preflight, the 22 replacement targets count as touched while the
three `insert_after` anchors do not, so the touched ratio is
`22/100 = 0.22`, below the default strict `>0.6` trigger.  It emits no block
marker and changes no section heading or section count.

| Item | Obligation | Emitted block operations |
|---|---|---|
| `REV-01` | should_fix | `B0004/replace_block` |
| `REV-02` | must_fix | `B0029/replace_block`, `B0030/replace_block`, `B0031/replace_block`, `B0092/replace_block` |
| `REV-03` | should_fix | `B0041/insert_after`, `B0076/replace_block` |
| `REV-04` | should_fix | `B0080/replace_block`, `B0081/replace_block`, `B0082/replace_block`, `B0083/replace_block`, `B0093/replace_block` |
| `REV-05` | should_fix | `B0042/insert_after` |
| `REV-06` | should_fix | `B0062/insert_after` |
| `REV-07` | must_fix | `B0013/replace_block`, `B0014/replace_block`, `B0076/replace_block`, `B0089/replace_block`, `B0090/replace_block`, `B0092/replace_block` |
| `REV-08` | must_fix | `B0014/replace_block`, `B0015/replace_block`, `B0031/replace_block`, `B0075/replace_block`, `B0077/replace_block`, `B0087/replace_block`, `B0092/replace_block` |
| `REV-09` | must_fix | `B0040/replace_block`, `B0046/replace_block`, `B0071/replace_block`, `B0080/replace_block`, `B0082/replace_block` |

Where several items use one block, the patch has one operation whose
`roadmap_item_ids` are authorized for that same block and operation.  In
particular, B0041 has exactly one `insert_after` operation for REV-03;
REV-07 is carried by its other authorized blocks.  B0040 has exactly one
`replace_block` operation containing the local bounded-root lemma and proof.

Every operation explicitly carries empty `claim_strength_changes` and
`collateral_authorization_ids` arrays.

## Registered ClaimIntent preservation

All 17 registered surfaces replay exactly once in their original blocks.
The ten untouched registered surfaces remain in the anchored base.  The seven
registered surfaces inside replacement blocks were loaded directly from the
claim-surface manifest and embedded byte-for-byte exactly once:

| Claim | Block | Exact surface SHA-256 |
|---|---|---|
| `C-007` | `B0071` | `f773479e036608633d87d68ed3b9cc9be2acb297c9fef089e40696721f053d86` |
| `C-011` | `B0076` | `8b1597f3c4f3f5a712d72f4ba261b9885da78bc4adb2d875ce23ec554f07037c` |
| `C-013` | `B0080` | `97fb98bd819b36ffa1946650356eb4c0b88d307baa24328e74aefe77e81f1711` |
| `C-014` | `B0081` | `4ff58540898e853ce624276fecc043c9b2ff5a95e56d861ccd97727744c750e6` |
| `C-015` | `B0082` | `f8102ee0e41aa2473ecc71cc1ba621468b8cecae029501d43120e23b64f0d91c` |
| `C-016` | `B0083` | `0565e1f60da79924aa2b7b4f0cfb222be42577b785611f0b54a9838ccf2400cb` |
| `C-017` | `B0089` | `66c5b2a6e62d00a9d09fd0d4170c572cbca93292b702ade59dd27185883318f3` |

The registered Round-8 sentence therefore still says **Eighteen Round-8 unit
tests**.  The ten Stage-4 support tests are identified separately and are not
folded into that registered count.

## Bounded scientific use of Stage-4 support

The emitted prose consumes, but does not regenerate, these already completed
support artifacts:

- dependency manifest:
  `notes/stage4_round8_dependency_manifest.json`,
  SHA-256
  `04544ef268f8b41e526b013bc77d52bb6faf96495e0b88e435dc0d6dd7f3e0dc`;
- matched-control ledger:
  `results/stage4_matched_exact_control_decomposition.csv`,
  SHA-256
  `6681e1c34f260b7b29ccfd7b24c7d31c204036a7a481e74fc3d40fff9e507e9a`;
- matched-control summary:
  `results/stage4_matched_exact_control_summary.json`,
  SHA-256
  `bcb6484321a6064100e8e7ed5b7dd64d75416a31e8097115afc41022d7f3991f`;
- support receipt:
  `experiments/stage4_round8_support_receipt.json`,
  SHA-256
  `70f3b2acabeca6327a98cd4fe5f5b8910b104a1cc6a4171fe7dea91997cf7c10`.

The population remains 138 registered instances, 55 groups, and 165 group-law
rows.  The target-blind controls are `y-z` and `y-2z`.  Their
both-control overlaps among studied-coordinate failures are 51, 44, and 55;
the `a_p^2` row has seven exactly-one-control failures; every
both-controls-pass residue count is zero.  Diagnostic flag counts are reported
as overlapping, not additive.  The interpretation is explicitly limited to
this two-control panel and is not a universal closed-one-form theorem or a
newform-uniqueness result.

The Route-A tuple remains
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.
No target data, formal A2 evaluation, determinant, global-owner
canonicalization, canonical result refresh, or Route-B operation is claimed.

## Literature-scope disposition

No new reference or citation key is introduced.  REV-02 has a provisional
`DELIBERATE_LIMITATION` judgment: the emitted blocks now compare the exact
objects, owner levels, and result types of the already verified Manin, Merel,
Ruelle, and Fried sources with the present finite result, and they state that
the five-entry source frame is not exhaustive modern-literature coverage.
The exact authority contains no bibliography target, so the writer did not
create an unbound modern citation or silently widen the patch scope.

## Read-only validation

The following checks passed without applying the patch:

1. JSON parsing for both emitted JSON artifacts.
2. Current Draft 2020-12 `revision_patch` 1.1 schema validation.
3. ARS `revision_roadmap.py validate-adjudication` against the exact base,
   block manifest, roadmap, author adjudication, claim-surface manifest, and
   artifact root.
4. Exact old-hash replay for 25/25 operations.
5. Unique-block and one-op-per-block checks: 25/25.
6. Exact target/operation authority for every cited roadmap item: 9/9 items.
7. Registered ClaimIntent conservation: 17/17 surfaces exactly once, with no
   replacement or movement.
8. Explicit empty claim-strength and collateral arrays: 25/25 operations.
9. Citation-key comparison: only existing keys `merel1991`, `ruelle1976`,
   and `fried1986` appear in emitted replacement text; zero new keys.
10. No `<!--block:` marker in any emitted `new_text`.
11. All 24 non-B0090 operations remain byte-exact as JSON values; B0090's
    metadata, numbers, scope limits, and Route language remain exact.
12. The second non-landed marker-stripped layout preflight has `0` overfull
    hboxes and no citation, reference, glyph, or fatal-build error.

For the first layout-only re-emission, restoring exactly the three prior
`new_text` values reconstructs the earlier patch SHA-256
`9530a88c2662a4887d8cf87ce71470754a027c7e128118b477f23f6f4bfd1f2e`.
For this second re-emission, restoring the one B0090 phrase reconstructs the
immediately preceding patch SHA-256
`9c2224621511806b558fdf9f98e00c22da4c3987a9e9e6a9134da8b99c1a2f25`.
Together these receipts confirm the bounded byte changes at both layout-only
steps. The current ARS Phase-1 parser, old-hash, structural,
roadmap-authority, and claim-surface preflight also passes with zero structural
flags and touched ratio `0.22`.

Post-emission protected hashes remain:

- anchored base:
  `af61f7b9a80b95bbc15c937ff0af3eed1ecc327965679324c51c376ad9dbb836`;
- canonical manuscript:
  `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe`;
- bibliography:
  `9b061c02006f07f1c93df68d8577d44906122f55db71e6f529f43cf3f6483ed8`;
- previously applied Stage-4 anchored preview source:
  `fd94e65a33473838086f2419ec7e69589628e20fef3a08801f7869eebb12ac29`;
- previously built Stage-4 preview PDF:
  `f389f22e71daa755acd0165f71d43e20467a2acc8ba7482ea166b7a1f779b5d4`;
- prior preview-build receipt:
  `d23cab7426914829bfbb7f4eb5855f8967ca3ceeb10891361344159f36730706`;
- Round-8 canonical manifest:
  `e017b412d46f34d151c178934e3ca7408089ed062baba39dacfaaa806839bd48`;
- Round-8 instance ledger:
  `beb363e4080b794e33ec6bc729b1f3e4dd7ef322be63fc59755e18fdf6bc889f`;
- Round-8 group ledger:
  `532e799686dd8afefa3a7529717208305fedede3f3e74e14ccf761ab35d74f69`;
- Round-8 summary:
  `4ba5de801dfd06c8b03bfe5fc07297b8c4e074bcf26c70ec6566de401ae2384d`;
- legacy Round-8 receipt:
  `08e0faf089e5f203ba61fe09a0f979759b8d5a90a49f47b8a291ccb0dc8d7072`.

No apply report exists at this writer boundary.  Deterministic apply,
mechanical Schema-8 completion, revision-evidence bundling, re-review, and
Stage 4.5 remain separate later actions.
