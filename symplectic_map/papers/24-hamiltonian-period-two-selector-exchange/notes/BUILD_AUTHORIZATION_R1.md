# Paper 24 — Deterministic R1 No-Op Build Authorization

Date: 2026-08-25 UTC  
Stage: unchanged-source deterministic R1 build authorization  
Disposition: exactly one distinct build-author invocation is authorized; the
source and every pre-existing project artifact are frozen

## 1. Controlling scope, role separation, and issuance provenance

This note authorizes exactly one future R1 builder to perform one indivisible
invocation comprising two fresh independent builds, read-only acceptance
validation, preparation and strict validation of two success JSON records,
and one success-or-failure persistence decision. The authorization is
consumed when that builder first creates either new R1 root. It may not be
split between actors, paused, resumed, retried, repaired, or reused after
success or failure. A false, drifting, missing, or unproved precondition
grants no build authority.

The authorization author is distinct from the no-op revision author, the
fresh full R1 reviewer, and the future R1 builder. The future R1 builder must
also be distinct from all three of those roles. The builder may not review its
own work at R2; any later R2 reviewer must be separately authorized and
distinct from the builder.

The following are exact authorization-author opening identities:

| Issuance fact | Exact opening value |
|---|---|
| BATCH_06_STATUS.md | SHA-256 de709a9982fe57e54f3b7e2c29c1cfa8bf6d5c3c5dd43d74a6135029ee2bd76c; 163,595 bytes; 2,378 LF |
| issuance gate | PAPER24_R1_BUILD_AUTHORIZATION_OPEN |
| Paper 24 issuance queue | R1_NO_OP_REVISION_PASS_PENDING_BUILD_AUTHORIZATION |
| BATCH_06_IDEA_REPORT.md | SHA-256 e7c110f1cf3d572c031dde5aeb1a84e05e88ee0d2ac7310d84ac55f0943eabbe; 271,774 bytes; 5,265 LF |
| Paper 24 issuance inventory | 39 regular files; four descendant directories; zero symlinks; zero other objects |

At issuance, this note, paper/BUILD_METADATA_R1.json,
paper/BUILD_RECEIPT_R1.json, paper/main_round1.pdf,
notes/BUILD_R1_BLOCKER.md, notes/INDEPENDENT_BUILD_R2_R1_REVIEW.md, and all
release/finalization artifacts are absent. No R1 temporary root has been
created.

These ledger identities are historical issuance provenance, not future
build-time identities. Before the R1 builder may act, the parent must:

1. read this note through EOF and bind its external path, SHA-256, byte count,
   LF count, mode, link count, and exact final line in both root ledgers;
2. set the gate exactly to PAPER24_DETERMINISTIC_R1_BUILD_OPEN;
3. set the Paper 24 queue exactly to R1_BUILD_AUTHORIZED; and
4. open exactly one builder distinct from this authorization author, the
   no-op revision author, and the fresh full R1 reviewer.

That parent transition necessarily changes both root-ledger byte identities.
The builder must hash and bind the actual post-consumption ledgers, their
byte/LF counts, the exact build-open gate and queue, and the authorization's
external identity. It must freeze those actual ledger bytes throughout its
invocation. The issuance hashes above must never be substituted for the
build-time hashes.

At builder opening the project must contain exactly 40 regular files, four
descendant directories, zero symlinks, and zero other objects. The fortieth
file is this note; the other 39 are the issuance files below. The three
success paths and the failure blocker must still be absent. The builder must
record a complete exact 40-file opening manifest, not merely counts or an
aggregate, and must prove all 40 opening files unchanged at its final
checkpoint.

### Complete exact 39-file issuance manifest

Paths are relative to
papers/24-hamiltonian-period-two-selector-exchange and are byte-sorted by
their UTF-8 POSIX path bytes.

| Relative path | SHA-256 | Bytes | LF | Mode | Links |
|---|---|---:|---:|---:|---:|
| experiments/EXPERIMENT_PLAN.md | bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94 | 7,098 | 186 | 0644 | 1 |
| experiments/EXPERIMENT_TRACKER.md | 61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0 | 3,459 | 59 | 0644 | 1 |
| experiments/publication_lock.json | a2f3a4e0a005972b60f8c5b2241889ec5fffc1841b83ada69d5b8b7582fcdb6a | 57,325 | 1 | 0644 | 1 |
| experiments/source_lock.json | 45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232 | 45,607 | 1 | 0644 | 1 |
| notes/BUILD_R0_BLOCKER.md | 4b5f88b9f31fb60366d3f294917be43cb466a44946ea0c9c9a89e70e4f14de5e | 3,447 | 59 | 0644 | 1 |
| notes/CITATION_VERIFICATION.md | 66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9 | 6,694 | 93 | 0644 | 1 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5 | 7,040 | 114 | 0644 | 1 |
| notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md | d2118f0a4cf5fc9d61fa8af55a5299f904da7ea1789c6a7e4253eab3a81e0bcf | 34,208 | 530 | 0644 | 1 |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68 | 20,521 | 483 | 0644 | 1 |
| notes/INDEPENDENT_PAPER_SOURCE_R1_R0_BUILD_REPAIR_REVIEW.md | ea520dea141a3334231bf0c3d577bb1d7fb13c833432b1f49892d3336171c8b6 | 19,297 | 472 | 0644 | 1 |
| notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md | c95698f426f9237eaabc44ff20c6961d09ed4c21bd69d6e077d292de94481e89 | 23,203 | 567 | 0644 | 1 |
| notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md | e91bcda341469dfbb877d70fe0daeace876570b3696ef6fc0b881851fe7c9075 | 21,751 | 435 | 0644 | 1 |
| notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md | c11b139759e7951ee5e13617537f60caaad04124638c9c64b95e5071af334972 | 10,735 | 240 | 0644 | 1 |
| notes/INDEPENDENT_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW.md | 8a7771c3a19c35a785bc6aa279bf2675fb6b6fe184c6341a29ef07b496fbaa30 | 17,766 | 302 | 0644 | 1 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8 | 16,630 | 490 | 0644 | 1 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea | 24,533 | 754 | 0644 | 1 |
| notes/NOVELTY_ASSESSMENT.md | e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c | 5,532 | 119 | 0644 | 1 |
| notes/PROOF_PACKAGE.md | b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf | 18,290 | 1,048 | 0644 | 1 |
| notes/PUBLICATION_STAGE_SCOPE.md | c0354c4621afcdfe79d5bddad035b378f6a4917e4c69a570971419ef5e80f762 | 46,832 | 1,331 | 0644 | 1 |
| notes/R1_REVISION_WINDOW_NO_CHANGE.md | 1bf7c2a528c736809ac4f34244e868a5904d4ed420dd9da364efa350a0f81ce0 | 3,768 | 87 | 0644 | 1 |
| notes/RESEARCH_QUESTION.md | 5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d | 5,052 | 132 | 0644 | 1 |
| paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json | 3a54b0667937df9c06720528c88d8bb904fbb2c2b177b132fb58c607b21815b7 | 35,512 | 1 | 0644 | 1 |
| paper/BUILD_METADATA_R0.json | 0d91c80183c9532bd4b3f0353277af9c2f5bcc5efdf7a9bd427ee45de3eed2a7 | 12,124 | 1 | 0644 | 1 |
| paper/BUILD_RECEIPT_R0.json | 7d34e1e952af185920f78736c71dd03c7c8242dd3f18a4360abfffbfbe7e8a57 | 3,360 | 1 | 0644 | 1 |
| paper/PAPER_PLAN.md | ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad | 36,690 | 586 | 0644 | 1 |
| paper/SOURCE_REVISION_RECEIPT_R1.json | c07b387e25b5b173fdd927aabc2841774f5343dce21d8441342a09139000528e | 3,335 | 1 | 0644 | 1 |
| paper/main.aux | d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf | 13,965 | 138 | 0644 | 1 |
| paper/main.bbl | b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855 | 3,371 | 78 | 0644 | 1 |
| paper/main.blg | 04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535 | 900 | 46 | 0644 | 1 |
| paper/main.log | ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08 | 28,421 | 733 | 0644 | 1 |
| paper/main.out | 02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d | 6,374 | 23 | 0644 | 1 |
| paper/main.pdf | 27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22 | 506,215 | 2,820 | 0644 | 1 |
| paper/main.tex | 0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f | 77,196 | 2,004 | 0644 | 1 |
| paper/main_round0.pdf | 27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22 | 506,215 | 2,820 | 0644 | 1 |
| paper/math_commands.tex | 8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e | 605 | 20 | 0644 | 1 |
| paper/references.bib | 4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b | 3,556 | 118 | 0644 | 1 |
| refine-logs/FINAL_PROPOSAL.md | bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf | 4,773 | 175 | 0644 | 1 |
| refine-logs/INITIAL_PROPOSAL.md | 7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc | 3,971 | 148 | 0644 | 1 |
| refine-logs/REVIEW_SUMMARY.md | b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82 | 4,233 | 102 | 0644 | 1 |

The 39 contents total 1,649,604 bytes and 17,318 LF. Their issuance
aggregate uses this exact framing: for each byte-sorted relative path,
concatenate
uint64_be(path-byte-length), path UTF-8 bytes,
uint64_be(content-byte-length), and raw content bytes, with no separator or
terminal record. The framed stream is 1,651,401 bytes and has SHA-256
0e60a332f4507a95a7ac569f5cc1121d6177652b9a50e92bf58045d79992af33.

## 2. Frozen source, full R1 verdict, and no-op revision evidence

The only build source is this unchanged trio:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| paper/main.tex | 0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f | 77,196 | 2,004 |
| paper/math_commands.tex | 8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e | 605 | 20 |
| paper/references.bib | 4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b | 3,556 | 118 |

The controlling full review is
notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md, SHA-256
d2118f0a4cf5fc9d61fa8af55a5299f904da7ea1789c6a7e4253eab3a81e0bcf,
34,208 bytes / 530 LF, ending exactly BUILD_R1_R0_REPAIR_PASS. It reports
zero required/critical, major, minor, cosmetic, and authority findings and
closes all four earlier provenance subfindings.

The mandatory R1 revision window was consumed as an explicit no-op:

| Evidence | SHA-256 | Bytes | LF | Required value |
|---|---|---:|---:|---|
| notes/R1_REVISION_WINDOW_NO_CHANGE.md | 1bf7c2a528c736809ac4f34244e868a5904d4ed420dd9da364efa350a0f81ce0 | 3,768 | 87 | final line R1_REVISION_WINDOW_NO_CHANGE |
| paper/SOURCE_REVISION_RECEIPT_R1.json | c07b387e25b5b173fdd927aabc2841774f5343dce21d8441342a09139000528e | 3,335 | 1 | schema PAPER24_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1; status R1_NO_OP_REVISION_PASS |

The receipt is strict recursive-canonical JSON with null self bytes and
SHA-256. It binds identical before/after source identities, zero changed
paths, zero source deltas, and revision windows
authorized/consumed/remaining = 1/1/0. These are hard preconditions. This
authorization opens no source edit and no further revision window.

## 3. Frozen R0 evidence, exact comparators, and public-output contract

The accepted R0 evidence remains immutable:

| Evidence | SHA-256 | Bytes | LF | Exact status fact |
|---|---|---:|---:|---|
| paper/BUILD_METADATA_R0.json | 0d91c80183c9532bd4b3f0353277af9c2f5bcc5efdf7a9bd427ee45de3eed2a7 | 12,124 | 1 | top-level status BUILD_R0_REPAIR_PASS |
| paper/BUILD_RECEIPT_R0.json | 7d34e1e952af185920f78736c71dd03c7c8242dd3f18a4360abfffbfbe7e8a57 | 3,360 | 1 | top-level status is absent; this_repair_build.status is BUILD_R0_REPAIR_PASS |
| paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json | 3a54b0667937df9c06720528c88d8bb904fbb2c2b177b132fb58c607b21815b7 | 35,512 | 1 | retrospective=true; contemporaneous_with_build=false; history_rewrite=false; status BUILD_R0_REPAIR_PASS_EVIDENCE_SUPPLEMENTED |
| notes/INDEPENDENT_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW.md | 8a7771c3a19c35a785bc6aa279bf2675fb6b6fe184c6341a29ef07b496fbaa30 | 17,766 | 302 | final line R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_PASS |
| notes/BUILD_R0_BLOCKER.md | 4b5f88b9f31fb60366d3f294917be43cb466a44946ea0c9c9a89e70e4f14de5e | 3,447 | 59 | immutable historical blocker ending R0_BLOCKED |

The original R0 receipt's absent top-level status is an immutable historical
fact. Neither this note nor any R1 JSON may assert that the original receipt
had that field. The supplement closes the evidence layer without rewriting
the original.

The following table is the complete 17-name cross-round content contract for
each new R1 root. Project source/output files provide the direct
cross-round comparators. For pass logs and raw statuses, the exact comparator
identities are bound by the persisted project supplement and its independent
reviews. No pre-existing temporary root may be consulted.

| Root name | Role | SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| main.aux | final output | d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf | 13,965 | 138 |
| main.bbl | final output | b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855 | 3,371 | 78 |
| main.blg | final output | 04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535 | 900 | 46 |
| main.log | final output | ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08 | 28,421 | 733 |
| main.out | final output | 02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d | 6,374 | 23 |
| main.pdf | final output | 27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22 | 506,215 | 2,820 |
| main.tex | source copy | 0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f | 77,196 | 2,004 |
| math_commands.tex | source copy | 8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e | 605 | 20 |
| pass1.merge | merged command stream | bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29 | 19,722 | 662 |
| pass1.status | raw exit status | 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9 | 1 | 0 |
| pass2.merge | merged command stream | 7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9 | 158 | 4 |
| pass2.status | raw exit status | 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9 | 1 | 0 |
| pass3.merge | merged command stream | c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59 | 8,971 | 174 |
| pass3.status | raw exit status | 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9 | 1 | 0 |
| pass4.merge | merged command stream | f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b | 7,837 | 130 |
| pass4.status | raw exit status | 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9 | 1 | 0 |
| references.bib | source copy | 4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b | 3,556 | 118 |

Project paper/main.pdf and paper/main_round0.pdf are direct byte-equal
comparators at the common PDF identity above. They and the other five current
outputs are read-only evidence; the builder may not overwrite, relink,
chmod, touch, or otherwise change them.

The controlling public-output policy is frozen by
experiments/publication_lock.json, SHA-256
a2f3a4e0a005972b60f8c5b2241889ec5fffc1841b83ada69d5b8b7582fcdb6a,
57,325 bytes / one LF, and
notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md, SHA-256
e91bcda341469dfbb877d70fe0daeace876570b3696ef6fc0b881851fe7c9075,
21,751 bytes / 435 LF, ending PUBLICATION_LOCK_PASS. The R1 build must
preserve the exact title
“Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears”,
visible author Anonymous, empty visible date, and empty PDF Author, Creator,
Producer, Subject, and Keywords. It must preserve exactly nine bibliography
items, three mathematical tables, zero figures/images/assets, and the full
public/private firewall.

## 4. Exactly two fresh independent four-command builds

The builder must create exactly two distinct, brand-new private directories
whose fresh templates are:

- /tmp/paper24-r1-A.XXXXXX
- /tmp/paper24-r1-B.XXXXXX

Each actual root must have a unique canonical absolute path that did not
previously exist, mode 0700, ordinary directory type, and no symlink or
shared-file relationship with the other root. Before command 1, each root
contains exactly three ordinary mode-0644, link-count-one files and nothing
else: independent byte copies named main.tex, math_commands.tex, and
references.bib matching the frozen trio. The two roots and all corresponding
files must be inode-distinct.

The builder must not name, enumerate, resolve, stat, open, read, compare,
write, chmod, relink, clean, or delete any pre-existing temporary root from
Paper 24, Paper 23, or another stage. Historical root path strings embedded
inside persisted project evidence must not be resolved. Cross-round
comparison uses only the current project files and the exact content
identities in persisted project evidence.

Every child build process receives an empty inherited environment populated
with exactly these six variables and no others:

| Variable | Exact value |
|---|---|
| PATH | /usr/bin:/bin |
| SOURCE_DATE_EPOCH | 1787616000 |
| FORCE_SOURCE_DATE | 1 |
| TZ | UTC |
| LC_ALL | C |
| LANG | C |

The epoch is 2026-08-25T00:00:00Z. With each fresh root as its exact working
directory, the builder runs this sequence exactly once and in order:

1. pdflatex -interaction=nonstopmode -halt-on-error main.tex
2. bibtex main
3. pdflatex -interaction=nonstopmode -halt-on-error main.tex
4. pdflatex -interaction=nonstopmode -halt-on-error main.tex

The resolved executables must be /usr/bin/pdftex, SHA-256
01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9,
and /usr/bin/bibtex.original, SHA-256
c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f.

For command index N, capture its exact merged stdout/stderr byte stream as
passN.merge and its raw decimal exit status without LF as passN.status. The
capture must not change the command arguments, environment, working
directory, stream ordering, stream bytes, or exit value.

There is no latexmk, preliminary build, diagnostic build, clean, fifth pass,
retry, second root pair, engine substitution, shell escape, package
installation, source generation, correction, cache import, or network
action. A nonzero command still consumes the authorization; no later command
may be used to repair or replace a failed sequence. Neither root may be
cleaned after its first creation.

## 5. Conjunctive execution, diagnostic, PDF, visual, and firewall acceptance

Success requires every condition below. No waiver, aggregate score, visual
impression, or later repair can compensate for a false, missing, ambiguous,
drifting, or unrecorded conjunct.

### Execution, immutability, and determinism

1. Both exit vectors are exactly 0,0,0,0.
2. All eight status files contain exactly the single ASCII byte 0, zero LF,
   and the status identity in Section 3.
3. Hash the project source trio at build opening and final checkpoint; hash
   each root trio before command 1, after command 4, and after all validation.
   Every identity remains frozen and all copies remain independent.
4. Each root ends as a flat inventory of exactly the 17 ordinary files in
   Section 3, zero child directories, zero symlinks, and zero other objects.
   Every file is mode 0644 and link count one.
5. Every corresponding A/B file is directly byte-identical and inode-
   distinct. The basename/content aggregate under the R0 supplement's
   declared uint64-be framing is 677,746 bytes with SHA-256
   ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145
   in both new roots.
6. Every new-root source and output is directly byte-identical to its current
   project comparator. Every pass log and status reproduces the exact project-
   evidence identity in Section 3. Thus all 17 content identities reproduce
   the accepted R0 round without accessing any pre-existing temporary root.
7. Record actual root paths, freshness, mode, ownership, device/inode/link
   evidence, exact initial and final inventories, working directories,
   commands, environments, exits, source/log/status/output identities,
   start/end stability, A/B comparisons, and cross-round comparisons.
8. The exact 40-file project opening manifest, both actual build-time root
   ledgers, and every pre-existing project file remain content-identical
   through final validation.

### TeX, bibliography, and diagnostics

1. Final AUX is closed under plainnat/references; every label, reference,
   citation, and bibliography reference resolves.
2. Source citations, AUX citation keys, AUX bibcite keys, BBL bibitem keys,
   and the nine source definitions have the same exact nine-element set:
   BellonVialletAlgebraicEntropy,
   HasselblattProppMonomialDegreeGrowth,
   DangFavreSpectralInterpretations,
   JaneczkoJelonekPolynomialSymplectomorphisms,
   FordyHoneSymplecticCluster, FordyHoneClusterPoisson,
   IshibashiKanoSignStableEntropy, BlancVanSantenAffineTriangular, and
   ShaoSunDimensionFour. There is no tenth item or duplicate.
3. BLG and pass2.merge have zero BibTeX error and warning.
4. Final OUT is syntactically readable and contains no raw PDF-string math,
   unresolved bookmark token, or private provenance.
5. Final main.log and pass4.merge contain zero fatal error, TeX or package
   warning, undefined citation/reference, multiply-defined label,
   changed-label/rerun event, missing glyph, and overfull box.
6. The only permissible final box diagnostics are exactly five underfull
   hboxes in the Table 2 construction around source line 730, corresponding
   to Carried momentum degrees, two Negative chamber labels, Positive
   chamber, and Negative visibility equality. Visual review must prove them
   harmless, complete, and legible.
7. Source, outputs, command streams, extracted PDF text, metadata,
   bookmarks, annotations, and PDF objects contain zero TODO, TBD, FIXME,
   VERIFY, placeholder, citation-needed, unresolved marker, double question
   mark, private path, root name, hash, ledger token, reviewer token, or
   build-history disclosure.

### PDF structure, pagination, identity, and every-page visual review

1. Both PDFs are nonempty, structurally valid, fully readable, unencrypted,
   and byte-identical. They contain no JavaScript, open action, additional
   action, form, AcroForm, XFA, attachment, embedded file, FileSpec,
   signature, multimedia, raster image, or other image object.
2. Every physical page is US Letter 612 by 792 points with rotation zero.
3. Exactly 27 reported font resources are present; every font is embedded and
   subset. A zero-font or partially embedded result cannot pass.
4. The decoded and normalized visible title is exactly “Forced Period-Two
   Selector Exchange in Two-Mode Hamiltonian Product Shears”. Visible author
   is exactly Anonymous. PDF Author, Creator, Producer, Subject, and Keywords
   are empty. CreationDate and ModDate are absent; no visible source date or
   conflicting metadata date exists.
5. There are exactly 27 nonblank readable physical pages. Pages 1 through 26
   are substantive article content; page 26 contains the complete conclusion;
   References is the first heading at the top of page 27; all nine entries end
   on page 27; there is no appendix.
6. Text/layout extraction confirms exactly three tables, zero figures,
   exactly nine bibliography items, one abstract, and eight numbered main
   sections.
7. Render all 27 pages in a fresh validation-only location inside one
   authorized R1 root after its build-output checkpoint and visually inspect
   every page. Give particular attention to the first-page title/author,
   Table 2 on page 9, later formula/table pages, the complete conclusion on
   page 26, and all references on page 27. Record zero blank, corrupt,
   clipped, cropped, overlapping, missing-symbol, unreadable, or table-
   overflow page.
8. Rendered content, metadata, bookmarks, links, annotations, and objects
   disclose no local/project/root path, username, machine marker, Paper or
   Batch number, hash, byte/LF count, gate, queue, review/build history,
   permission record, tool/agent identity, or other private governance text.

## 6. Strict R1 JSON contract, success-only persistence, and failure

The success JSONs must have these exact schema/status pairs:

| Artifact | Schema | Status |
|---|---|---|
| paper/BUILD_METADATA_R1.json | PAPER24_BUILD_METADATA_R1_NO_OP_V1 | BUILD_METADATA_R1_NO_OP |
| paper/BUILD_RECEIPT_R1.json | PAPER24_BUILD_RECEIPT_R1_NO_OP_V1 | BUILD_R1_NO_OP_PASS |

Each JSON must be one strict recursive-canonical compact UTF-8 object on one
physical line followed by exactly one terminal LF. It must contain no BOM,
CR, NUL, invalid UTF-8, lone surrogate, insignificant whitespace, duplicate
key at any depth, nonfinite value, float/exponent/negative-zero ambiguity, or
trailing content. Every object is ordered recursively by increasing Unicode
code point; arrays retain semantic order. Each self_identity has its own
path and null bytes and SHA-256 fields; neither artifact may claim a circular
non-null self identity.

Before project persistence, each exact candidate byte string must pass two
genuinely independent duplicate-aware strict parser/canonical-encoder
implementations, including adversarial rejection cases and byte-exact
round-trip. Record parser identities, negative-suite results, object-order
checks, round-trip bytes, and SHA-256 values. Native JSON parsing without
duplicate detection is insufficient.

Together the JSONs must bind, without an unrecorded side ledger:

- this authorization's final external identity and the exact issuance
  ledgers, gate, queue, 39-file manifest, aggregate, and author-stop
  inventory;
- both actual post-consumption build-time ledger identities, exact build-open
  gate/queue, exact 40-file opening manifest and aggregate, and one-shot
  invocation identity;
- the full R1 review, no-change note, no-op receipt and schema/status/window
  facts, and unchanged source before/after in the project and both roots;
- original R0 metadata, the original receipt with top-level status explicitly
  absent, the retrospective supplement, its independent review, the
  historical blocker, and every current source/output/PDF comparator;
- both fresh roots, their complete 17-file manifests, modes/inodes/links,
  exact commands/environments/executables/exits, all eight raw status bytes,
  all four streams, all six outputs, every stability checkpoint, both root
  aggregates, every A/B comparison, and all 17 cross-round comparisons;
- every TeX/BibTeX, citation, warning/box, marker/private-text, PDF security,
  font, metadata, date, geometry, page-boundary, table/figure, every-page
  visual, firewall, and parser/canonicality observation with exact counts;
  and
- effective filesystem permissions, complete granted and denied authority,
  success/failure persistence semantics, retained-root disposition, and zero
  external effects.

The receipt must bind the finalized external byte identity of metadata.
Canonicality is a byte-level acceptance fact, not merely a claim inside the
JSON.

No success path may exist in the project until every acceptance conjunct and
both exact JSON candidates pass. Candidate staging must stay inside an
authorized private R1 root after its build-output checkpoint. Project
persistence is exclusive-create, no-overwrite, and all-or-nothing. If that
cannot be guaranteed before the first project write, the builder must take
the failure branch without creating a success path.

On success, create exactly these three new ordinary project files and no
others:

1. paper/BUILD_METADATA_R1.json
2. paper/BUILD_RECEIPT_R1.json
3. paper/main_round1.pdf

paper/main_round1.pdf is an independent byte copy of an accepted new-root
PDF. It, paper/main.pdf, and paper/main_round0.pdf must be directly
byte-identical at SHA-256
27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22
and 506,215 bytes. The six current outputs are not rewritten. The successful
project inventory is exactly 43 regular files, four descendant directories,
zero symlinks, and zero other objects. All 40 opening files and both
build-time ledgers remain unchanged; notes/BUILD_R1_BLOCKER.md is absent.

Any false, missing, ambiguous, drifting, or unrecorded conjunct is failure.
Failure creates none of the three success paths. The only optional project
write on failure is notes/BUILD_R1_BLOCKER.md, an ordinary factual record
whose exact final nonempty line is R1_BUILD_BLOCKED. Whether or not that
blocker is written, authority is consumed. There is no source edit, repair,
replacement root pair, retry, continuation, or cleanup.

Retain both fresh R1 roots privately, completely, and unchanged after the
final identity checkpoint on both success and failure. They are evidence for
a future separately authorized independent R2 review. The builder must
report actual identities, counts, commands, comparisons, parser results,
inventories, success artifacts or blocker, and then stop.

## 7. Authority boundary and author stop

This note authorizes no manuscript or bibliography edit, no further revision
window, no mutation of any issuance file or root governance ledger by the
builder, no self-review, no R2 artifact, no release or finalization, no
publication or submission, no upload or transport, no repository action, no
messaging or identity disclosure, no Paper 25 work, no scientific or CAS
execution, no network access, no package installation, and no external
effect.

The authorization author performed no compilation, TeX/BibTeX invocation,
temporary-root creation or access, source/evidence/output/governance edit,
network action, Paper 25 action, or external effect. This note is the sole
authorized project write at author stop. It opens nothing by itself; only the
separate parent consumption transition specified in Section 1 can open the
one future builder.

BUILD_AUTHORIZATION_R1
