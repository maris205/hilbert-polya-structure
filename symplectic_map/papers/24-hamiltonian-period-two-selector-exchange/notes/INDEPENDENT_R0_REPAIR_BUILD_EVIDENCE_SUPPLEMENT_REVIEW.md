# Independent R0 Repair-Build Evidence-Supplement Review

## Verdict and role separation

I am the prior independent R1 build reviewer who issued the zero-write
`R1_BUILD_REVIEW_BLOCKED` finding. I did not author
`paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json`, did not perform either repair
build, and did not author the immutable original metadata or receipt. This
review treats every assertion in the supplement as unproved.

All four prior findings are **CLOSED** at the explicitly retrospective
supplement layer. The supplement does not pretend that its evidence was
present in the original builder records or contemporaneous with the build.
It instead freezes the retained raw evidence and a reproducible governance
history while truthfully preserving the original receipt's missing
top-level status. No new required, major, minor, or cosmetic finding remains.

This verdict is only an evidence-supplement review. It is not an R1 build
PASS, does not reopen an R1 review or build by itself, and grants no source,
build, revision, release, Paper 25, or external authority.

## Review-opening state

The opening governance state was exact:

| Object | SHA-256 | Bytes | LF |
|---|---:|---:|---:|
| `BATCH_06_STATUS.md` | `18199d5d32038c580e4ccec49cdee89fb2c13cbd32de9fe5806239d2312a3932` | 157,094 | 2,284 |
| `BATCH_06_IDEA_REPORT.md` | `59e97d2df82bd4af0e5c98ea9e59616ff2e933d3b98e77aaac4031b9819ee707` | 264,645 | 5,137 |

The live gate was
`PAPER24_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW_OPEN`, and the Paper 24
queue was
`R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_AUTHORED_PENDING_INDEPENDENT_REVIEW`.
Both roots were ordinary mode-0644, root-owned, one-link files.

The Paper 24 project contained exactly 35 regular files, four child
directories, zero symlinks, and zero other objects. Its sorted
`SHA256<TAB>bytes<TAB>LF<TAB>relative-path<LF>` manifest was SHA-256
`108803b392fac0cd985c00924ac5f346e5c1ce069a087ec7c3d773d8b149a476`,
3,622 bytes and 35 LF. The four directories were `experiments`, `notes`,
`paper`, and `refine-logs`. The conditional review path
`notes/INDEPENDENT_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW.md` was absent.
The original conditional R1 PASS path and the repair-blocker path were also
absent.

## Supplement identity, complete value tree, and strict canonical form

The reviewed object was exactly:

| Path | SHA-256 | Bytes | LF | Mode/owner/link |
|---|---:|---:|---:|---|
| `paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json` | `3a54b0667937df9c06720528c88d8bb904fbb2c2b177b132fb58c607b21815b7` | 35,512 | 1 | regular `0644`, `root:root`, link 1 |

I read the complete one-line value tree. Its 21 top-level keys, in canonical
order, are `aggregate_algorithm`, `artifact_path`, `authority_and_absence`,
`bound_build_objects`, `contemporaneous_with_build`,
`cross_root_and_project_equality`, `format_contract`,
`governance_histories`, `history_rewrite`, `immutable_original_records`,
`operations_boundary`, `original_receipt_top_level_status_present`,
`project_universes`, `purpose`, `raw_pass_statuses`, `retrospective`,
`root_inventories`, `schema_version`, `self_identity`, `status`, and
`status_closure`.

Two independent strict implementations reproduced the exact 35,512 bytes:

- A duplicate-aware Python parse with arbitrary-precision integers and an
  independently written recursive literal-UTF-8 encoder counted 162 objects,
  22 arrays, 475 integers, 1,620 strings including object keys, 93 booleans,
  two nulls, and 1,118 keys. It found zero unsorted objects and rejected all
  22 adversarial records.
- A handwritten Node recursive-descent parser using explicit `BigInt`, with
  no `JSON.parse` or `JSON.stringify`, and its own Unicode-code-point encoder
  obtained the same counts, zero unsorted objects, byte-exact output, and
  rejected all 23 independent adversarial records.

Both implementations rejected duplicate and escape-equivalent names,
nonfinite values, floats and exponents, leading and negative zero, malformed
UTF-8, BOM, CR, NUL, raw controls, lone surrogates, noncanonical escapes,
noncanonical whitespace or key order, missing or extra terminal LF, trailing
or multiple records, and nonobject roots. The live record is literal UTF-8,
BOM/CR/NUL-free, compact, recursively Unicode-code-point sorted, one physical
line, one object record, and terminated by exactly one LF.

The semantic control values are exact:

- schema: `paper24.build_evidence_supplement_r0_repair.v1`;
- supplement status: `BUILD_R0_REPAIR_PASS_EVIDENCE_SUPPLEMENTED`;
- `self_identity.bytes = null` and `self_identity.sha256 = null`;
- `retrospective = true`;
- `contemporaneous_with_build = false`;
- `history_rewrite = false`;
- `original_receipt_top_level_status_present = false`.

The null self identity is transparent self-reference exclusion. The record's
purpose is expressly to bind omitted retained evidence without rewriting the
immutable original build history.

## Immutable original records and build objects

The supplement binds, and live bytes independently match:

| Object | SHA-256 | Bytes | LF | Inode |
|---|---:|---:|---:|---:|
| `paper/BUILD_METADATA_R0.json` | `0d91c80183c9532bd4b3f0353277af9c2f5bcc5efdf7a9bd427ee45de3eed2a7` | 12,124 | 1 | 12,351,219,449 |
| `paper/BUILD_RECEIPT_R0.json` | `7d34e1e952af185920f78736c71dd03c7c8242dd3f18a4360abfffbfbe7e8a57` | 3,360 | 1 | 12,351,219,450 |
| `notes/BUILD_R0_BLOCKER.md` | `4b5f88b9f31fb60366d3f294917be43cb466a44946ea0c9c9a89e70e4f14de5e` | 3,447 | 59 | 8,057,685,675 |

All are regular mode-0644, one-link files with the recorded inodes. Metadata
has top-level status `BUILD_R0_REPAIR_PASS`. The receipt has no top-level
`status`; its exact nested value is
`this_repair_build.status = BUILD_R0_REPAIR_PASS`. The supplement states both
facts correctly, and
`supplement_level_closure_does_not_claim_original_receipt_had_top_level_status`
is true. The receipt's metadata external identity matches the immutable
metadata record.

The three sources, six final outputs, and round-zero comparator also match all
embedded SHA-256, byte, LF, mode, inode, and link-count values. Principal
identities are:

| Object | SHA-256 | Bytes | LF |
|---|---:|---:|---:|
| `paper/main.tex` | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 |
| `paper/math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `paper/references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |
| `paper/main.aux` | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 |
| `paper/main.bbl` | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 |
| `paper/main.blg` | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 |
| `paper/main.log` | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 |
| `paper/main.out` | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 |
| `paper/main.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |
| `paper/main_round0.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |

No original JSON, source, output, blocker, root, or governance object was
mutated by supplement authoring or this review.

## Eight raw status bindings and command linkage

All eight retained status files are independently bound and live-exact. Each
is regular mode-0644, one link, one byte, zero LF, raw byte `0`, decoded value
zero, and SHA-256
`5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9`.

| Root | Pass | Inode | Command | Bound merged log SHA-256 / bytes / LF |
|---|---:|---:|---|---|
| A | 1 | 11,825,668,797 | `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | `bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29` / 19,722 / 662 |
| B | 1 | 12,351,200,857 | same | `bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29` / 19,722 / 662 |
| A | 2 | 11,825,672,119 | `bibtex main` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` / 158 / 4 |
| B | 2 | 12,351,200,861 | same | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` / 158 / 4 |
| A | 3 | 11,825,672,121 | `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | `c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59` / 8,971 / 174 |
| B | 3 | 12,351,200,869 | same | `c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59` / 8,971 / 174 |
| A | 4 | 11,825,678,360 | `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | `f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b` / 7,837 / 130 |
| B | 4 | 12,351,219,448 | same | `f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b` / 7,837 / 130 |

Every command equals the corresponding immutable metadata command. Every
merged-log path and identity equals the metadata binding, the root-inventory
entry, and its live file. The independently reconstructed exit vectors are
exactly `[0,0,0,0]` for both A and B, matching metadata, both root inventories,
and `status_closure`.

## Exact project universes and u64be aggregates

I independently implemented the declared frame

`u64be(path_utf8_length) || path_utf8 || u64be(content_length) || raw_content`

with paths ordered lexicographically by UTF-8 bytes. Project frames use safe
project-relative POSIX paths; root frames use basenames. The three project
universe claims replay exactly:

| Universe | Entries | Framed bytes | SHA-256 |
|---|---:|---:|---:|
| Retrospectively reconstructed opening set | 25 | 475,261 | `05bb3276fcf370c4e8791059dd1e6b010b9b1a02b635ad34672452068cfe1b30` |
| Exact authorized success delta | 9 | embedded individually | disjoint from the opening 25 |
| Opening 25 plus success 9 | 34 | 1,556,510 | `3e6dd57462806de2bb61d958933472e8418e2074e3959fac06487e8c46fc6fba` |

All 25 embedded opening entries match their current path, SHA-256, bytes, LF,
mode, inode, and link count. They comprise four experiment/lock files,
fourteen pre-build notes, the paper plan and source trio, and three refine-log
files. All nine success entries likewise match their current identities:
metadata, receipt, AUX, BBL, BLG, LOG, OUT, PDF, and round-zero PDF. The two
sets are unique and disjoint. Their union is exactly the pre-supplement
34-file project universe.

At review opening, the only path outside that exact 34-file union was
`paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json`. Thus the supplement is the sole
35th-file delta. No retrospective claim relies only on counts: every opening
and success path is individually embedded and the content-framed aggregates
were recomputed from live raw bytes.

## Complete retained-root audit

The retained build roots are:

| Root | Directory inode | Mode/link | Inventory | Aggregate SHA-256 / framed bytes |
|---|---:|---|---|---|
| `/tmp/paper24-r0-repair-A.F4nzXg` | 11,825,646,800 | `0700`, link 2 | 17 regular / 0 directories / 0 symlinks / 0 other | `ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145` / 677,746 |
| `/tmp/paper24-r0-repair-B.k4LK3V` | 12,351,200,848 | `0700`, link 2 | 17 regular / 0 directories / 0 symlinks / 0 other | `ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145` / 677,746 |

For each root, the exact 17 basenames are the three source copies, four
`passN.merge` logs, four `passN.status` files, and six final outputs. Every
embedded path, role, SHA-256, bytes, LF, mode, inode, and link count matches
live evidence. Independent u64be framing gives 17 entries and exactly the
claimed aggregate in each root.

The following equalities were independently byte-compared and are true:

- all three source copies: A = B = current project source;
- all six final outputs: A = B = project comparator;
- all four merged logs: A = B;
- all four raw status files: A = B;
- root A PDF = project `main_round0.pdf`;
- both root aggregates are equal.

## Governance-history reconstruction

The supplement-author opening identities are exactly:

| Stop | Status SHA-256 / bytes / LF | Idea-report SHA-256 / bytes / LF |
|---|---|---|
| Supplement-author opening | `6d5ee61df1e1c0746e7cf45ec787b94bf319ce5f621f4c6d26febb371b61184c` / 154,809 / 2,252 | `59cffa564d09c2be63083984bfea837e4ba9ad5d1172dcd172dfcfa99782dd9e` / 261,766 / 5,085 |
| R1-review opening | `90d26e127a441a62892e69c8a0bef50fde5b0a795f24d1e2280e38bb8e674ab8` / 151,769 / 2,211 | `2605da86f5188cb3d42bcff820f4f1b91743cbdd5dc81ac92f675e74016c05d1` / 258,117 / 5,019 |
| Build-time stop | `bb3aae0ec08cfaafae0036615be4a845c3b50aef739fc29adb0f49791b201d9f` / 148,830 / 2,169 | `170e7b99755a26b37ed67b63e79e24183e86248a71d2382e42405a5fe9bc6c4d` / 254,437 / 4,953 |

I first independently reversed the current review-opening governance bytes to
the supplement-author opening. In STATUS this required the unique gate and
queue reversals plus removal of the unique supplement-author activity segment
SHA-256 `3322b11969391f79f343e3f20124ab99693c44474979ec62f10f808d81d8f071`,
2,295 bytes / 32 LF. In IDEA_REPORT it required removing the unique author-stop
addendum SHA-256
`ec78ee7d5ddff2fa2b91a9171ec230c0b233dc0d7a2412d9d7ed252bc186b089`,
2,879 bytes / 52 LF. The results equal the two author-opening identities above.

I then replayed every operation named inside the supplement:

1. Author opening to R1-review opening: the two exact STATUS line replacements
   each occurred once, followed by removal of the unique activity segment
   `052621366bf40cf31ef8bb14d9c9c32ac6759867f59905a204f6fae1248a4043`,
   3,018 bytes / 41 LF. The IDEA_REPORT removal was the unique addendum
   `2391cb87784579fe3ee9d6aa6911fdd27b8001f5a2d93b2c7a394f596ca5deb4`,
   3,649 bytes / 66 LF. Results are exactly `90d26...` and `2605da...`.
2. R1-review opening to build-time stop: the two exact STATUS line replacements
   each occurred once, followed by removal of the unique builder activity
   segment
   `030a8d33a778a839ce5167785bbbd75f111e2a2bc64eb9715dc96cf181f874f7`,
   2,943 bytes / 42 LF. The IDEA_REPORT removal was the unique addendum
   `90351b22fa71f034e1b7436a4ed178c3b37346c1d183e74f465b832e2952ea45`,
   3,680 bytes / 66 LF. Results are exactly the full `bb3aae...` and
   `170e7b...` identities.

Reattaching each exact removed segment and reversing each exact line
replacement reproduced its source bytes. Every marker was unique, all
embedded intermediate and result identities agree, and both
`result_matches_frozen_identity` and
`reversible_against_bound_current_bytes` are truthful. The build-time and
R1-open records are explicitly historical; the supplement is explicitly a
retrospective reconstruction backed by earlier parent observation. It does
not call those historical byte strings current files and does not claim that
the supplement existed at build time.

## Closure of the four prior findings

| Prior finding | Verdict | Independent reason |
|---|---|---|
| Eight raw `passN.status` identities absent from original JSON | **CLOSED** | The supplement now persistently binds every path, raw byte, digest, LF, mode, inode, link count, decoded value, command index, command, and merged log; both exit vectors replay from raw bytes. Its retrospective timing is explicit. |
| Full build-time governance identities absent | **CLOSED** | Both full identities and all intermediate stops are embedded, and every uniquely named reverse and forward transition reproduces exact bytes. No current/historical conflation or contemporaneous overclaim remains. |
| Opening metadata had counts but no exact 25-file manifest | **CLOSED** | All 25 paths and identities are embedded, independently live-matched, u64be-framed to `05bb3276...`, disjoint from the exact nine success paths, and united to the exact pre-supplement 34-file aggregate `3e6dd574...`. |
| Original receipt lacked a top-level status | **CLOSED** | The immutable receipt remains unmodified and its absence is stated repeatedly and truthfully. The supplement supplies its own top-level status and an explicit `status_closure` tying metadata status, receipt nested status, both raw exit vectors, and supplement status without pretending to alter history. |

A retrospective supplement cannot make itself contemporaneous with the
build, and this one does not try. It is sufficient because its role is to
freeze retained raw evidence and exact deterministic reconstructions for all
future consumers, while the immutable originals and the historical absence
remain visible. That is the precise closure the parent transition authorized.

## Permission boundary, sole write, and findings

The supplement grants no R1 authorization, release authority, revision
authority, source/build mutation authority, or subsequent-build authority.
This review likewise performed no compilation, BibTeX execution, retry,
cleanup, network action, source or output edit, original-JSON edit, root edit,
governance edit, R1 build review, revision, release, or external effect.

The sole conditional project write is this review artifact. Before writing,
the project was 35 regular files / four child directories / zero symlinks /
zero other objects, and this path was absent. The expected and required
postwrite universe is 36 regular files / four child directories / zero
symlinks / zero other objects, with this file as the sole delta. Its own final
SHA-256, byte count, and LF count are necessarily external postwrite facts.
No R1 PASS artifact or repair blocker is created by this review.

Finding counts:

- prior blocker subfindings closed: 4 of 4;
- required findings: 0;
- major findings: 0;
- minor findings: 0;
- cosmetic findings: 0;
- authority expansions: 0.

R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_PASS
