# Round 9 Papers 24–28 — Stage 3′ Round 2 Completion Report

## Outcome

Stage 3′ Round 2 completed all three evidence-before-persuasion gates for Papers 24–28 and passed the official ARS checker for all five papers. The fresh round used new round ids and manifests; all Attempt-1 artifacts remain immutable and were excluded from the reviewing threads.

- Phase-1 precommitments: **32** (15 must-fix + 17 should-fix; P27's one consider item had no precommitment).
- Phase-2A/2B matrix rows: **33**.
- Final verdicts: **23 `FULLY_ADDRESSED` + 5 `PARTIALLY_ADDRESSED` + 5 `CANNOT_VERIFY`**.
- `NOT_ADDRESSED` / `MADE_WORSE`: **0 / 0**.
- Phase-2B adjustments: **0**.
- New issues / dissents / escalation exceptions: **0 / 0 / 0**.
- Decisions: **4 Major Revision + 1 Minor Revision**.
- Checker: **5/5 PASS**, apply-chain witness **5/5 `pass`**.
- Canonical manuscript/PDF/results changes: **none**.
- Route-A tuple changes / Route-B invocations: **none / none**.

## Per-paper results

| Paper | Fully | Partially | Cannot verify | Adjustments | Decision | Rule | Next legal stage | Report |
|---|---:|---:|---:|---:|---|---|---|---|
| P24 | 6 | 2 | 0 | 0 | Major Revision | B4 | Stage 4′ | [report](papers/24-bianchi-holonomy-flow/notes/stage3_prime_round2_verification_report.md) |
| P25 | 2 | 1 | 3 | 0 | Minor Revision | B5 | Stage 4.5 | [report](papers/25-three-disk-scattering-flow/notes/stage3_prime_round2_verification_report.md) |
| P26 | 7 | 1 | 1 | 0 | Major Revision | B4 | Stage 4′ | [report](papers/26-level11-newform-time-change/notes/stage3_prime_round2_verification_report.md) |
| P27 | 5 | 1 | 0 | 0 | Major Revision | B4 | Stage 4′ | [report](papers/27-congruence-inverse-limit-no-go/notes/stage3_prime_round2_verification_report.md) |
| P28 | 3 | 0 | 1 | 0 | Major Revision | B3 | Stage 4′ | [report](papers/28-bolza-magnetic-flow/notes/stage3_prime_round2_verification_report.md) |

P25's Minor Revision is driven by the should-fix addressed-rate rule (B5): both must-fix items are fully addressed, while three support-dependent should-fix items remain fail-closed. P24, P26 and P27 trigger B4 because a partial row retains a must-fix residual; P28 triggers B3 because a must-fix row remains `CANNOT_VERIFY`.

## Residual evidence ledger

| Paper | Item | Status | Residual class | Frozen reason |
|---|---|---|---|---|
| P24 | REV-001 | PARTIALLY_ADDRESSED | must_fix | The nearest-work and antecedent verification remains unverified within the hash-bound Round-2 evidence set: the revised manuscript delegates exact source locators to notes/stage4_rev001_008_support_provenance.md, which is not a manifest-bound input, and the permitted manuscript, bundle, patch, and apply-report surfaces do not independently identify and verify those comparisons. |
| P24 | REV-003 | PARTIALLY_ADDRESSED | must_fix | The matrix-versus-owner scope repair is visible, but the exact loxodromic classification and bucket counts cannot be independently verified from the allowed bound inputs because the named Stage-4 loxodromic profile manifest, reproducer, tests, and result ledger are not carried by the Round-2 manifest. |
| P25 | REV-002 | PARTIALLY_ADDRESSED | should_fix | The four-object map and scope guards are present, but avoidable duplication remains across the introductory hierarchy, the text immediately surrounding the map, the Route-A interpretation, and the conclusion, so the committed consolidation component is incomplete. |
| P25 | REV-004 | CANNOT_VERIFY | should_fix | The revised manuscript identifies experiments/stage4_reproducibility_lock.json and lists runtime, package, and platform pins, but that lock or any equivalent bound environment artifact is not in the permitted Phase-2A evidence set, so machine-readable recoverability and the actual pins cannot be verified from manuscript text alone. |
| P25 | REV-005 | CANNOT_VERIFY | should_fix | B0109 replaces the stale pointer with experiments/stage4_reproducibility_lock.json, but the pointed-to lock and Stage-2.5 integrity record are not permitted Phase-2A evidence inputs, so the pointer cannot be replayed to verify that its bibliography digest matches the frozen Stage-2.5 digest. |
| P25 | REV-006 | CANNOT_VERIFY | should_fix | The revised manuscript says that experiments/stage4_reproducibility_lock.json contains a closed 68-file Round-2-through-Round-8 inventory, but the manifest itself is outside and unbound to the permitted Phase-2A evidence set, so its claimed source, test, input, output, receipt, and command bindings cannot be inspected or verified. |
| P26 | REV-02 | PARTIALLY_ADDRESSED | must_fix | The comparison remains restricted to five classical ingredient sources and does not supply the required source-verified nearest-neighbor treatment of modern geodesic-period work or other closest contemporary operator or taxonomy work. |
| P26 | REV-04 | CANNOT_VERIFY | should_fix | The permitted Phase 2A input set contains only the revised manuscript's descriptions and hashes, not the referenced supplemental dependency manifest, support receipt, transitive source graph, or test outputs, so enumeration of every imported project source, fail-closed drift behavior, and preservation of the checked-in output tree cannot be verified from bound evidence. |
| P27 | REV-03 | PARTIALLY_ADDRESSED | must_fix | The permitted bound inputs do not carry the asserted Stage-4 fixture, test output, or replay receipt, so execution of the -I path cannot be verified; additionally, block B0040 still describes the factor-reduction strategy as independent without the shared-kernel qualification supplied later. |
| P28 | REV-02 | CANNOT_VERIFY | must_fix | B0048 now states that Stage-4 direct tests exercise repeated Delta cancellation, global-sign normalization idempotence, both inverse orders, and sampled canonical collisions, but the actual test record and exact replay artifact are outside and unbound to the permitted Phase-2A evidence set, so the manuscript's execution claim cannot be verified independently of its own text. |

These fail-closed statuses are input-bound. In particular, an unbound project receipt, replay fixture, dependency graph or test log cannot be imported merely because the response letter says it exists. They do not mean that a separately stored Stage-4 test failed.

## Hash chain

| Paper | Manifest JCS | Precommitment JCS | Verdict JCS | Phase-2B integration JCS | Traceability JCS |
|---|---|---|---|---|---|
| P24 | `89e8b16af6986df6ebd74225863114d0134ae83c3960fe2509c275996b33d724` | `78923104d92fff86885029d50e75b8b0bbd4de2f3c859bcd3d85df5db47e289c` | `ad0e1241bd014b6377242cda7f5c96e2b8e9bbbaf3f3c143d6ce2c30a5326904` | `51a6b303a371816d5bf80b5aa2e7f4e0a548a26e0d5defb98f582383aafd89a7` | `ded28a1b03142950a13a210f6aa5913f96b4fdd962e140b55444c517ff8547e7` |
| P25 | `18fe79ca40d7057515104501122070013068dcc3f01d2311b6255ba5d9d1213c` | `622f8df870c6dc308bcdb84731e84f590bddaea068f93086f57379d3c77f1474` | `30fdd19b07f4be67e572d36970be39df832cd5f1692916880eada2d50f48d13f` | `027b3454c353877a067a145d727548af06bc70a7217b81fdcb5a0e8b6ad8553f` | `a0c4fb1638707b7a8158ef520a368762a67e2cba8827060b7b44a933292c5d9e` |
| P26 | `e1b4f33681f82d2a45277e0b9e2a8e66b5f7b1755154b94fad0a153688cd56f4` | `f3e919c201f39ff32cfa2eedcf0134b98c9991bb91d36ed8b3d51316171993e6` | `0fa4427cef0ab8cf63af6eec2e0c86b2c12723f0c7baeb93ee683ab3570236a9` | `be8450d2fd26ae6b60f389d31699a82f8e32730e49d59fd71582f24baedbd663` | `19c709770645dc1bec5ec336544c0ff5477c23f78b1a90f493da5ac6d49f1b73` |
| P27 | `38f1caab09ecb50b47a18407f47ff33a9a238ed9061f9c14f77471a4a7ca7682` | `86df53e74d0b63425a2e81f8aae485ad9d130cb03613db51e999d0d1a8f94112` | `39e2160089dea4a562d0f370dedeb25308883b7b6b0e31d65ce10b19d6bc2c78` | `cfdeba0a5c8d6ebb0284e5022a19e59e14e3cf32a34549b791ac62d170954e2b` | `9ff51dd55f221f6cbb5f65bce8459ed2a5438de1358144b8925d41a6792a5e8c` |
| P28 | `c8267e6bab5df01ff599d8fd4f5f0c4c1b0af55f78665bf9036d134cce9088d5` | `7af9511ee1a4bbcfe22d93bc2410b21d2d6cbf228da93972813b0e8e1fc34bea` | `b421165b03a7de0e0edda4cee9c77110fbc24e079ac7b176cba54551de032c0c` | `b0df09e967a7edce188fd5ab5854de8539e012c516816583013e4ff54b2ae3e5` | `7978d8f03ed7a47e21dd55b31ce79545b01cffeb73c713593b906de7fc4d50ef` |

Each manifest hash-binds exactly eleven artifact keys. The five continuous `revision-evidence-bundle/1.0` chains replayed successfully, and every trace row exactly copies the checker-only author triage, authorized targets and claim-strength authorizations.

## Attempt-1 comparison and immutability

Attempt 1 remains an auditable `phase2b_lint_failed` abort with its frozen 24/3/6 evidence split. Round 2 did not repair or overwrite those files; it restarted at Phase 1 under new round ids. The Round-2 split is 23/5/5: the fresh judge was stricter on P24's bound derivative evidence and more granular on P27's partial manuscript fix. This inter-attempt variation is reported, not normalized away.

## Provenance and limitations

All Round-1 panel provenance carriers replay-validated. The verification used the same model family as the revision process and no cross-model pass was configured.

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

All five checker runs emitted the same advisory: the old decision letters are present but contain no parseable `Required Item Details` / `R<n>` acceptance-criteria blocks, so the level-2 criterion layer is empty. The immutable roadmap criteria remained the controlling level-1 yardstick; this advisory did not invalidate any run.

## Route-map correspondence

The Round-2 decisions concern manuscript revision fidelity only. They do not change the Route-A evaluator records in `skills/route-a-evaluator.md`, do not create positive arithmetic A2 credit, and do not invoke Route B. The five initial dynamical-system restrictions remain the Stage-4 frozen baseline: Bianchi marked-word proxy, three-disk physical/symbolic split, Level-11 positive time change, congruence/homology-cover candidates, and Bolza geodesic/magnetic precursor.

## Mandatory user checkpoint

This report does not authorize the next stage.

- P25 may enter **Stage 4.5** only after explicit user confirmation.
- P24, P26, P27 and P28 may enter **Stage 4′** only after explicit user confirmation and a new scoped revision authorization.
- No Stage 5, canonical promotion, submission, Route advancement or new science round has begun.

Checked at `2026-08-30T10:41:10Z`.
