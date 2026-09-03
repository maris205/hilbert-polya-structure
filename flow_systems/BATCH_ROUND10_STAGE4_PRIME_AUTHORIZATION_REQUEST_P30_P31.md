# Round 10 Papers 30--31 -- Stage 4′ Exact Authorization Request

Date: **2026-09-03 UTC**

Status: `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`

This request is preparation-only. Its creation changed no manuscript, bibliography, PDF, result, experiment, registered claim, initial system, or Route state. A later exact confirmation is required before any listed operation is executed.

Machine-readable request: `BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json` (SHA-256 `a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688`).

## Frozen authority bindings

| Paper | Stage 3′ verdict | Traceability | Checker | Stage 4′ base draft | Block manifest | Bibliography |
|---|---|---|---|---|---|---|
| P30 | `a9cca59829836a027b8211b6de9e17150056a1f0689456f0b6372c91a1de4fc3` | `79d665653d3aa43f469355d48b1b315de4601e8062af33595acb7c0e29c8e548` | `254caf1613906cd493040d87c03ee054c339cc1be43d4ecf22192fffb3fe5dd3` | `9d8c7201420d182154796ed714e34de466cc683a7910f9830825ec4ea8efd3e7` | `a3eaa92d60149c9f4facf43be4b5357ea64608188a44e9768c3a472566b86dab` | `1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f` |
| P31 | `2d2a4397bdca26c0b30b697cebc0f4dcdf47e3b0e4115c3f28213815792129a9` | `5291239aa6fef478516512a5f3b0162703c97ff59e2fbebf255877802c1fdb7e` | `d9b8c92502648dcc94463aaef4e16e453753bd4d372c5f31aafd9122190142d6` | `03304330e06f2af77a9311908ab0bbc4d350dd9e5b54a47744cd1e3367a6f6d5` | `8bd7801b604aedd1227185730b370f01d279aece6b83c7777d9db3bc685f0fb5` | `b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958` |

## P30 -- 5 residual items

| Item | Residual class | Exact proposed target/operation set |
|---|---|---|
| `REV-EIC-W2-R1-W3` | `must_fix` | `B0059/replace_block`, `B0062/replace_block`, `B0098/replace_block`, `B0098/insert_after`, `B0123/replace_block` |
| `REV-EIC-W3-R2-W2` | `must_fix` | `B0060/replace_block`, `B0106/replace_block`, `B0123/replace_block` |
| `REV-EIC-W4` | `should_fix` | `B0061/replace_block`, `B0064/replace_block`, `B0067/replace_block`, `B0100/replace_block` |
| `REV-R1-W2-R3-W2` | `must_fix` | `B0084/replace_block`, `B0084/insert_after`, `B0103/replace_block` |
| `REV-R3-W1-DA-N1` | `must_fix` | `B0088/replace_block`, `B0088/insert_after`, `B0090/replace_block` |

Implementation branches:

- `REV-EIC-W2-R1-W3`: Run a dated, bounded replay of the already frozen search strings; publish a row-level retrieval/screening ledger and a claim-to-passage matrix. Preserve unavailable original-session rows as unavailable and never backfill them as historical observations.
- `REV-EIC-W3-R2-W2`: Add exactly two independently citable correction records, keys P30-C01 and P30-C02, for DOI 10.1063/1.457669 and 10.1063/1.457670, then bind P30-S01/P30-S02 and P30-S03 to the matching keys and remove only the now-resolved publication-incomplete wording.
- `REV-EIC-W4`: Replace internal Stage/review vocabulary with a standalone evidence-method description. Rename the B0067 heading only; keep section order and section count unchanged. Describe same-family fresh-context assessments as role-separated, not independent.
- `REV-R1-W2-R3-W2`: Freeze a=1 scale, c0=1, the order-three cyclic disk-label automorphism phi, delta=1/10 giving d=61a/10, Omega={1/2<=Re(s)<=2, |Im(s)|<=50}, and eta_c=1/100. Reclassify phi as a symmetry/invariance control and state preserved/broken properties for every control. Do not execute a comparison.
- `REV-R3-W1-DA-N1`: Insert one six-row gate table that explicitly lists each gate's inputs, output, receipt, hash, uncertainty channel, downstream consumer, permission and stop state, including the Gate-6 output. No gate state is promoted.

## P31 -- 8 residual items

| Item | Residual class | Exact proposed target/operation set |
|---|---|---|
| `REV-P31-001` | `must_fix` | `B0016/replace_block`, `B0033/insert_after` |
| `REV-P31-002` | `must_fix` | `B0079/replace_block`, `B0105/replace_block` |
| `REV-P31-004` | `must_fix` | `B0046/replace_block`, `B0050/replace_block`, `B0051/replace_block` |
| `REV-P31-005` | `must_fix` | `B0015/replace_block`, `B0062/replace_block` |
| `REV-P31-007` | `must_fix` | `B0036/replace_block`, `B0037/replace_block`, `B0038/replace_block`, `B0039/replace_block`, `B0079/insert_after`, `B0089/replace_block` |
| `REV-P31-008` | `should_fix` | `B0012/replace_block`, `B0049/replace_block`, `B0054/replace_block` |
| `REV-P31-009` | `should_fix` | `B0067/replace_block`, `B0072/insert_after` |
| `REV-P31-011` | `must_fix` | `B0015/replace_block`, `B0061/replace_block` |

Implementation branches:

- `REV-P31-001`: Run a bounded closest-work search for proof-carrying-data and ledger-verification methods, add only source-verified records, distinguish inherited components from the project synthesis, and retain the no-priority/no-exhaustive-novelty boundary.
- `REV-P31-002`: Use the conservative branch: remove reader-recovery claims for materials not listed, and give every retained entry its schema/version, digest and explicit repository-relative access state; make no persistent-archive claim.
- `REV-P31-004`: Reserve totality for delta:X->OwnerDisposition; define kappa only on X_res and make every owner-map theorem require X_res=X. Keep the biconditional and G/I/C materialization under the same zero-unresolved stop condition.
- `REV-P31-005`: Restrict the all-pairs surface to byte-level and bookkeeping consequences. Assign reflexivity to self fixtures, direction sensitivity to ordered reversals, transitivity to triples, and semantic merge/split detection only to an independent target-blind route.
- `REV-P31-007`: Run and publish a dated row-level retrieval/screening ledger from frozen queries plus a method-component passage/hypothesis/transfer-boundary table. Preserve every unresolved passage as unresolved; do not fabricate historical screening rows.
- `REV-P31-008`: Add the typed self-reciprocal branch: if subgroup self-reciprocity is certified, retain one owner_bytes value and emit inverse_relation=self_reciprocal with the witness; otherwise retain inverse-separated or unresolved dispositions. Do not assert an exclusion theorem.
- `REV-P31-009`: Add one consolidated G/I/C relational-schema table with keys, cardinalities, materialization gate, allowed I-to-G/C projections and prohibited G/C-to-I reconstruction; retain the prose only as interpretation.
- `REV-P31-011`: Remove the remaining semantic false-merge/false-split and nontransitivity capability claim from the introduction and bind the limitation to the absence of an independent target-blind adjudicator.

## Supporting and exceptional scopes requested

- P30 literature replay: dated retrieval/screening ledger plus claim-to-passage matrix; historical gaps remain visibly unavailable.
- P30 bibliography: append only `P30-C01` / DOI `10.1063/1.457669` and `P30-C02` / DOI `10.1063/1.457670`, after metadata verification.
- P31 closest-work search: at most four source-verified bibliography additions for the two missing method families; no priority claim.
- P31 literature replay: dated row-level ledger and passage/hypothesis/transfer matrix; no fabricated historical rows.
- P30 structural acknowledgment: `B0067/replace_block` is limited to heading text; section order and section count must remain unchanged.

## Boundaries

- Proposed disposition is `will_address` for all 13 residual items, in `source_traceability` order.
- No declined item, no collateral authorization, and no registered-claim replacement; both claim-surface manifests contain zero registered surfaces.
- The later patch may use a subset of an authorized target/operation set but may not broaden it.
- No scientific execution or canonical-result refresh. P30's control values are frozen modeling choices only; no comparison result is produced.
- Any source-verification failure, test failure, scientific-value change, unregistered semantic drift requiring disposition, extra bibliography record, target expansion, broader structural change, Route change, or later-stage transition stops for a new checkpoint.
- Route-A tuples and the five initial dynamical systems stay unchanged; Route B and Stages 4.5--6 remain unauthorized.

## Short confirmation

Reply `确认` to approve this exact request and its SHA-256; any change to the request bytes requires a new confirmation.
