# Round 10 Papers 29–33 — Stage 1 Phase-2 metadata correction manifest

Date: **2026-09-02 UTC**  
Scope: **authorized Phase-2 source-integrity corrections only**  
Status: **PATCH APPLIED / INDEPENDENT POST-PATCH RECHECK REQUIRED**

## Authority and boundary

The scholar's exact Phase-2 authorization is stored in
`BATCH_ROUND10_STAGE1_PHASE2_AUTHORIZATION_20260902.txt`, SHA-256
`b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85`.
The bounded corrections below were required by the independent verification
seats and are within the authorized source-verification scope. They do not
change a research question, source count, peer-review count, dynamical object,
clock, primitive/repetition convention, owner type, scientific result, claim,
Route tuple, or execution permission.

## Independent findings that triggered the patch

| Paper | Initial verification report SHA-256 | Finding IDs |
|---|---|---|
| P29 | `fc14da5e0d10947d5e39744bf3921187324d27f2a840aa5da8c17c579d8f026a` | `ERR-P29-01` |
| P30 | `6771d4c5e46c1ba45b98793fcd20a168da892f7eedfa2dd8fdf9f7af343d204d` | `CORR-P30-01`, `CORR-P30-02`, `CORR-P30-03` |
| P31 | `076b3ba2a07175d7ae413b9426f348770b0b25c683ad884014592c74ff2a45a0` | `P31-ERR-01` |
| P32 | `95ad09ca0258b315a25fc7d3cb711e0bffa6b801225ee3c328a849a84074fe29` | `P32-ERR-01` |
| P33 | `3f8aeb32dd82ce900ca43631c6f142939353b7cee6085eaf0ddeee36bb8e7e65` | `ERR-P33-PH2-S12-01` |

## Exact correction operations

| Correction ID | Paper/source | Path | Field/block | Authorized operation | Before | After |
|---|---|---|---|---|---|---|
| `R10PH2-C01` | P29-S09 | `papers/29-bianchi-ideal-owner-refinement/notes/stage1_phase2_annotated_bibliography.md` and `stage1_phase2_source_inventory.tsv` | title | exact text replacement | title omitted initial `On the` | official arXiv title begins `On the symmetric square large sieve ...` |
| `R10PH2-C02` | P30-S01/S02 | `papers/30-three-disk-nonconstant-roof-determinant/notes/stage1_phase2_annotated_bibliography.md` | claim-use correction companion | append bounded correction binding | no binding | bind JCP 91(5), 3279, DOI `10.1063/1.457669` without increasing corpus count |
| `R10PH2-C03` | P30-S03 | `papers/30-three-disk-nonconstant-roof-determinant/notes/stage1_phase2_annotated_bibliography.md` | claim-use correction companion | append bounded correction binding | no binding | bind JCP 91(5), 3280, DOI `10.1063/1.457670` without increasing corpus count |
| `R10PH2-C04` | P31-S16 | `papers/31-level11-conjugacy-owner-ledger/notes/stage1_phase2_annotated_bibliography.md` and `stage1_phase2_source_inventory.tsv` | page range | exact text replacement | `287–306` / `287-306` | `287–305` / `287-305` |
| `R10PH2-C05` | P32-S02 | `papers/32-homology-cover-renormalization-uniformity/notes/stage1_phase2_annotated_bibliography.md` and `stage1_phase2_source_inventory.tsv` | page range | exact text replacement | `287–306` / `287-306` | `287–305` / `287-305` |
| `R10PH2-C06` | P33-S12 | `papers/33-bolza-control-matched-census/notes/stage1_phase2_annotated_bibliography.md` and `stage1_phase2_source_inventory.tsv` | page range | exact text replacement | `287--306` / `287-306` | `287--305` / `287-305` |

No DOI, author list, source ID, peer-review flag, support class, or scientific
value was changed. The P30 correction notices are companion bindings, not two
additional independent source rows.

## Byte-level patch manifest

| Path | Field scope | Pre-patch SHA-256 | Post-patch SHA-256 |
|---|---|---|---|
| `papers/29-bianchi-ideal-owner-refinement/notes/stage1_phase2_annotated_bibliography.md` | P29-S09 title | `cd4ddfe1deee545a6212105a1d66fcce90c1fe265262d10e2f861ef79bd13c51` | `c4d71637e5676337326d2eb78dcdd64d78b4b116a397c50c54a081d7c5e2650b` |
| `papers/29-bianchi-ideal-owner-refinement/notes/stage1_phase2_source_inventory.tsv` | P29-S09 title | `b6ae9947fa3bf71dfea8c4d2dc28c46c22eadb0440580366ff53caefbaae9f60` | `67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8` |
| `papers/30-three-disk-nonconstant-roof-determinant/notes/stage1_phase2_annotated_bibliography.md` | P30-S01/S02/S03 correction bindings and limitation renumbering | `67fd941099205718e203025e92f78fcb976f58951b24cb4aacf1f48615a9e4c0` | `efa7a8b33fa37995f3345f46b232efd4515033d73e2a03f9e5919f59d2977e31` |
| `papers/31-level11-conjugacy-owner-ledger/notes/stage1_phase2_annotated_bibliography.md` | P31-S16 pages | `e2bd432bc655a607898b9c0d74c7acc899c94695bf9dc23b471a124c4f0e46ec` | `c4655ba9c039dc27a1a7fc05347b79f834454423ca80aa1c0dc19fb13f968976` |
| `papers/31-level11-conjugacy-owner-ledger/notes/stage1_phase2_source_inventory.tsv` | P31-S16 pages | `36f0af561157620b57c7d5ceaca616990ddedd3ab64921857fc44e23bbbbad74` | `cf4eef7d626ebc5d217d1597dc1f5e2ba0c5c8dc33b108a86b9be19d60536132` |
| `papers/32-homology-cover-renormalization-uniformity/notes/stage1_phase2_annotated_bibliography.md` | P32-S02 pages | `435056bfd8fa7cfdd279a25079105025ab349c65604515fcc43fbe8e14bc9dfa` | `2480eb3c3fce30fd9535cf7004c99f3cbc0babfc80b81bc1966827fac621a2a7` |
| `papers/32-homology-cover-renormalization-uniformity/notes/stage1_phase2_source_inventory.tsv` | P32-S02 pages | `fa875cbe05a2a73957fb80c6276d981540334d0efca76e74ce595b775ae1ad5c` | `c375c1e7e8310d6d5a1aa4509147a2d4b61b75fe3283b6d148fd0c61f2e76d8e` |
| `papers/33-bolza-control-matched-census/notes/stage1_phase2_annotated_bibliography.md` | P33-S12 pages | `42247115b3a96bd90b4d46f1864195217856054f6bdfc3e45d460ecf7038831c` | `38e98f66c21e61b448aef8184600d8a46550ad58b4fa69f0a30bd51b24474792` |
| `papers/33-bolza-control-matched-census/notes/stage1_phase2_source_inventory.tsv` | P33-S12 pages | `a01ee3d4056e3a27396a4de8411e9825720dbc186e157c2778993f957f156409` | `b1934dba37ff62c263bc33d617425fd85aba1d45efa204ef7ce315651e427b87` |

## Invariants after the patch

```text
SOURCE_ROWS=116/116
PEER_REVIEWED_ROWS=100/116
SOURCE_IDS_ADDED=0
SOURCE_IDS_REMOVED=0
SCIENTIFIC_COMPUTATION=NOT_RUN
NOVELTY_ASSESSMENT=NOT_RUN
CLAIM_REGISTRATION=0/5
FORMAL_ROUTE_A_TUPLES=0/5
POSITIVE_ARITHMETIC_A2=0/5
ROUTE_B_INVOCATIONS=0/5
```

The original verification seats must now re-read the post-patch files, update
only their verification artifacts to record `RESOLVED_POST_VERIFICATION`, and
confirm that the five Phase-2 dispositions remain valid. Phase-2 completion
cannot be issued until those independent rechecks are recorded.
