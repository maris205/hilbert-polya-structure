# Paper 24 — Independent Terminal R1 Build-Blocker Review

Date: 2026-08-25 UTC

## Verdict, scope, and role disclosure

The terminal failure disposition is accurate. The retained products reproduce
the accepted R0 bytes, but the R1 invocation cannot satisfy its conjunctive
authorization because neither root-source trio received a recorded
cryptographic hash checkpoint before command 1. The one-shot authority is
consumed and cannot be retried, replaced, repaired, or retrospectively
completed. This review certifies that terminal blocker only. It does **not**
certify R1 build success, create success evidence, or open a downstream gate.

I previously authored the two no-op revision artifacts
`notes/R1_REVISION_WINDOW_NO_CHANGE.md` and
`paper/SOURCE_REVISION_RECEIPT_R1.json`. I disclose that role explicitly.
For this review I used those artifacts only as frozen byte-identity inputs and
did not self-certify their substantive claims. I am distinct from both the R1
builder and the author of `notes/BUILD_AUTHORIZATION_R1.md`, exactly as the
current review gate requires. The terminal defect arose later, inside the
build protocol, and is independent of the no-op artifacts' substance.

This was a bounded protocol-evidence review. I did not recompile, invoke TeX
or BibTeX, rerun the manuscript/PDF visual review, mutate or clean evidence,
create a temporary root, use the network, touch Paper 25, or cause an external
effect.

## Review-opening authority and universe

The exact opening governance was:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `4efbc79431ead7e07dbd188addf83b637a28e065e16613665cb83972d7ad3b40` | 169,208 | 2,456 |
| `BATCH_06_IDEA_REPORT.md` | `546c496b625042d4a50662f606452dabe7c88126dfbc51b3468d6a029a4c0bdd` | 277,397 | 5,360 |

The gate was exactly `PAPER24_R1_BUILD_BLOCKER_REVIEW_OPEN`; the Paper 24
queue was exactly `R1_BUILD_BLOCKED_PENDING_INDEPENDENT_TERMINAL_REVIEW`.
The target review path and all R1-success, R2-review, finalization, and release
paths were absent. The project contained exactly 41 regular files, four
descendant directories, zero symlinks, and zero other objects. Every opening
file was mode `0644` with link count one.

For a byte-sorted project manifest, I serialized each row as
`sha256<TAB>bytes<TAB>LF<TAB>relative-path<LF>`. Excluding the blocker, the
40-row opening-build manifest independently reproduced:

- SHA-256 `0855db474540aaa35353599101c970a187c1540490f18f061e5e489ac913d3bc`;
- 4,211 bytes / 40 LF;
- 1,679,343 content bytes / 17,796 content LF; and
- under `u64be(path length)||path||u64be(content length)||content`, SHA-256
  `21b05981c7ee115a68afde7fbe1c0fc9f24acce9b963b5b107f4f5c6c207571c`
  over 1,681,187 framed bytes.

The sole added row was:

`eaa41f85cc28a551fec9240913ccf4483095df98f62545f3d118a6afa9d052de<TAB>6985<TAB>132<TAB>notes/BUILD_R1_BLOCKER.md<LF>`

Thus the exact 41-row review-opening manifest had SHA-256
`5b8c6e18b69a3b48b126aded2e49ddb4d82d2e7f4c43d4a400383619003d381d`,
4,311 bytes / 41 LF, 1,686,328 content bytes / 17,928 content LF, and u64
aggregate SHA-256
`6a37648d9709ded6183f7fab3b72166a1ee2ff6a9da39c69cde479d47e7265b0`
over 1,688,213 framed bytes.

The exact postwrite path manifest is the byte-sorted opening path list plus
only `notes/INDEPENDENT_R1_BUILD_BLOCKER_REVIEW.md`, one path per LF. It has
42 rows, 1,315 bytes / 42 LF, and SHA-256
`a4873c90b0be1ed992cd40f85862c39501fa25c04e91f2f8a94293bbbb36f089`.
The review file's own content identity is necessarily an external postwrite
fact; it cannot be embedded circularly. All 41 opening content rows must
remain the exact manifest above.

## Authorization, blocker, and historical ledgers

I read all 478 lines of `notes/BUILD_AUTHORIZATION_R1.md` and all 132 lines
of `notes/BUILD_R1_BLOCKER.md`, treating their assertions as unproved. Their
external identities independently reproduced:

| Record | SHA-256 | Bytes | LF | Mode / links | Unique terminal |
|---|---|---:|---:|---|---|
| `notes/BUILD_AUTHORIZATION_R1.md` | `50a1bfae5c54f720ba69b8d5600fb3ef5e74bb1244d2dcc83ad44b686cd2f99c` | 29,739 | 478 | `0644` / 1 | `BUILD_AUTHORIZATION_R1` |
| `notes/BUILD_R1_BLOCKER.md` | `eaa41f85cc28a551fec9240913ccf4483095df98f62545f3d118a6afa9d052de` | 6,985 | 132 | `0644` / 1 | `R1_BUILD_BLOCKED` |

The historical build-open ledgers were independently recovered from the
current ledgers, rather than accepted from the blocker. For the idea report I
removed the single separator LF and final blocker-review addendum. For the
status ledger I removed the final 42-LF builder record, restored gate
`PAPER24_DETERMINISTIC_R1_BUILD_OPEN`, and restored the exact Paper 24 row
whose status is `R1_BUILD_AUTHORIZED`. Those reversible operations produced:

| Historical record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `1ab13affdac8d4da5b5482392a0875f796e1cfe8804fb12636924f3fabc6b52d` | 166,169 | 2,414 |
| `BATCH_06_IDEA_REPORT.md` | `eddc11dda739326f2149e4827640c276ba91e57e63c5c4f5d5c365e22718c8f8` | 274,286 | 5,308 |

The source trio, controlling R1 review, no-op identities, and authorization
all match the frozen authorization inputs. In particular the source hashes
remain `0e15bba5...` for `main.tex`, `8c3f90e...` for
`math_commands.tex`, and `4acd9cad...` for `references.bib`. My earlier
no-op-author role is not used as evidence for anything beyond the externally
remeasured identities `1bf7c2a5...` / 3,768 / 87 and `c07b387e...` /
3,335 / 1.

## Independent retained-root audit

I accessed only the two authorized retained roots:

| Root | Directory mode | Device | Directory inode |
|---|---:|---:|---:|
| `/tmp/paper24-r1-A.ZUdJFJ` | `0700` | 149 | 7,517,478,163 |
| `/tmp/paper24-r1-B.LEqGfX` | `0700` | 149 | 8,059,960,473 |

Each is an ordinary private directory with exactly 17 flat ordinary files,
zero child directories, zero symlinks, and zero other objects. Every file is
mode `0644`, link count one. All corresponding A/B files are byte-identical
and inode-distinct. The complete common content identities are:

| Basename | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.aux` | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 |
| `main.bbl` | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 |
| `main.blg` | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 |
| `main.log` | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 |
| `main.out` | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 |
| `main.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |
| `main.tex` | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 |
| `math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `pass1.merge` | `bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29` | 19,722 | 662 |
| `pass1.status` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 |
| `pass2.merge` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `pass2.status` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 |
| `pass3.merge` | `c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59` | 8,971 | 174 |
| `pass3.status` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 |
| `pass4.merge` | `f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b` | 7,837 | 130 |
| `pass4.status` | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 |
| `references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |

All eight status bytes are exactly raw ASCII `0`; hence both vectors are
`(0,0,0,0)`. The four log hashes agree with the persisted R0 supplement,
where each occurs in both raw-status/log bindings and both R0 root manifests.
The three source and six output files directly equal their current project
comparators. Both roots reproduce the basename/content u64 aggregate SHA-256
`ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145`
over 677,746 framed bytes. No extra, retry, fifth-pass, candidate-JSON,
rendering, validation, or checkpoint artifact exists in either root.

The prescribed command sequence and six-variable environment are stated
identically in the authorization and blocker. The four exact merged streams
show pdfTeX, BibTeX, pdfTeX, pdfTeX on `main.tex`/`main.aux`; their four raw
statuses and final products corroborate that record. No contradictory command
or environment evidence exists. This blocker review does not convert those
facts into a success certificate.

## Missing time-indexed checkpoint and terminality

Authorization Section 5, execution item 3, requires the builder to hash each
root source trio at three distinct times: before command 1, after command 4,
and after validation. This is an observation requirement, not merely a final
content-equality requirement.

The two roots contain only the exact 17 files above. The 40-file build-opening
project contains no checkpoint ledger, and the sole later project evidence is
the blocker itself. The success metadata and receipt are absent. Searches of
the allowed evidence found no contemporaneous pre-command root-source hash
record; the only unrelated root occurrence of the word `hash` is BibTeX's
`hash_size` capacity line in `main.blg`.

The final root hashes prove what bytes exist now. The project-source hashes
and copy provenance prove the intended copy source. Neither proves that a
cryptographic observation of the root copies was actually made before the
first command. A later calculation cannot reconstruct that time-indexed
event without rewriting history. Root A's creation consumed the one-shot
authority; Sections 1, 4, and 6 forbid continuation, retry, replacement root
pair, evidence repair, or recovery after any missing conjunct. The three
success paths are therefore inadmissible and correctly absent.

This is a protocol/evidence failure only. The direct byte comparisons reveal
zero scientific-content corruption and zero output corruption. No claim of
manuscript or PDF damage is made.

## Transparent same-path blocker finalization

The final blocker contains exactly one occurrence of `external messaging`.
Removing only the nine ASCII bytes `external ` at byte offset 6,839 produces
the observed intermediate identity
`8ef469683274d490601bdc5946943cac26181faeaf551e89c8f2dabe0d44dcd4`,
6,976 bytes / 132 LF. Reinserting those nine bytes produces the final
`eaa41f85...`, 6,985-byte / 132-LF file; all other bytes are identical.

The correction is truthful: internal team status reporting occurred, while
external messaging did not. It narrows an overbroad factual sentence without
changing the blocker reason, evidence, terminal, path set, roots, or
authority. It was finalized on the single authorized failure path while the
builder remained active; the failure branch does not impose the success
branch's three-file no-overwrite transaction. The disclosed correction adds
no second project path and has no effect on the terminal disposition.

## Findings, permission boundary, and conditional sole write

- confirmed terminal acceptance defects: 1 — the missing pre-command
  root-source cryptographic observation;
- blocker factual inaccuracies: 0;
- scientific-content corruption findings: 0;
- output-corruption findings: 0;
- same-path-finalization findings: 0;
- role or authority findings: 0; and
- build-success certifications: 0.

Immediately before this conditional write, the opening governance, exact
41-row project manifest, both root directory identities, both 17-row root
manifests, and both `ceb33e75...` aggregates remained unchanged. This file is
the only authorized and only performed write. It makes the project exactly
42 regular files / four descendant directories / zero symlinks / zero other
objects while preserving all 41 opening files. Its external SHA-256 and
byte/LF counts must be measured after creation.

This PASS means only that the terminal blocker is independently verified. It
does not mean `BUILD_R1_NO_OP_PASS`, does not authorize or infer success,
does not reopen compilation or recovery, and opens no R2, release,
finalization, Paper 25, network, or external-effect authority by itself.

R1_BUILD_BLOCKER_REVIEW_PASS
