# Paper 24 — Deterministic R1 Build Blocker

Date: 2026-08-25 UTC  
Stage: unchanged-source deterministic R1 build  
Disposition: terminal one-shot failure; no R1 success artifact is admissible

## Controlling failure

The one-shot authority in `notes/BUILD_AUTHORIZATION_R1.md` was consumed when
the builder created the first authorized R1 temporary root. Both prescribed
four-command build sequences subsequently returned the exact exit vector
`0,0,0,0`, and their products reproduce the accepted R0 content identities.
Nevertheless, the invocation cannot pass the authorization's conjunctive
acceptance rule.

Before command 1, the builder recorded each root's exact three-file flat
inventory, file types, modes, and link counts and copied the files directly
from the already-hashed frozen project source trio. The builder did **not**
execute and record a cryptographic hash checkpoint of each root source trio
before command 1. Section 5, “Execution, immutability, and determinism,” item
3 requires each root trio to be hashed before command 1, after command 4, and
after all validation. A post-command hash or an inference from the copy
operation cannot retroactively create the missing pre-command observation.

This is a missing, unrecorded acceptance conjunct. The authorization forbids
a retry, repair, replacement root pair, continuation under reused authority,
or evidentiary history rewrite. Accordingly, none of
`paper/BUILD_METADATA_R1.json`, `paper/BUILD_RECEIPT_R1.json`, or
`paper/main_round1.pdf` was created.

## Exact build invocation facts

- Build-time `BATCH_06_STATUS.md`: SHA-256
  `1ab13affdac8d4da5b5482392a0875f796e1cfe8804fb12636924f3fabc6b52d`,
  166,169 bytes / 2,414 LF; gate
  `PAPER24_DETERMINISTIC_R1_BUILD_OPEN`.
- Build-time `BATCH_06_IDEA_REPORT.md`: SHA-256
  `eddc11dda739326f2149e4827640c276ba91e57e63c5c4f5d5c365e22718c8f8`,
  274,286 bytes / 5,308 LF.
- Paper 24 build-open queue: `R1_BUILD_AUTHORIZED`.
- Authorization: SHA-256
  `50a1bfae5c54f720ba69b8d5600fb3ef5e74bb1244d2dcc83ad44b686cd2f99c`,
  29,739 bytes / 478 LF, exact terminal line
  `BUILD_AUTHORIZATION_R1`.
- Exact 40-file opening manifest identity: SHA-256
  `0855db474540aaa35353599101c970a187c1540490f18f061e5e489ac913d3bc`,
  4,211 bytes / 40 LF.
- Exact 40-file u64-framed content aggregate: SHA-256
  `21b05981c7ee115a68afde7fbe1c0fc9f24acce9b963b5b107f4f5c6c207571c`,
  1,681,187 framed bytes; source contents totaled 1,679,343 bytes / 17,796
  LF.
- Root A: `/tmp/paper24-r1-A.ZUdJFJ`, ordinary private directory, mode
  `0700`, device 149, inode 7,517,478,163.
- Root B: `/tmp/paper24-r1-B.LEqGfX`, ordinary private directory, mode
  `0700`, device 149, inode 8,059,960,473.
- Both roots initially contained exactly independent mode-`0644`, link-count-
  one copies named `main.tex`, `math_commands.tex`, and `references.bib`.
- In each root the builder ran exactly once and in order: `pdflatex
  -interaction=nonstopmode -halt-on-error main.tex`; `bibtex main`;
  `pdflatex -interaction=nonstopmode -halt-on-error main.tex`; `pdflatex
  -interaction=nonstopmode -halt-on-error main.tex`.
- Every build child received an empty inherited environment populated with
  exactly `PATH=/usr/bin:/bin`, `SOURCE_DATE_EPOCH=1787616000`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, and `LANG=C`.
- Root A exit vector: `0,0,0,0`. Root B exit vector: `0,0,0,0`.
- All eight raw status files contain the single ASCII byte `0`, zero LF, and
  SHA-256
  `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9`.
- There was no preliminary command, retry, fifth pass, alternate pair,
  source edit, cleanup, package action, or network action.

The private-root umask caused the fourteen generated output, stream, and
status files in each root to be created as mode `0600`. Before the final
evidence checkpoint, the builder normalized only those files to the required
final mode `0644`. This changed permissions only, not content. No TeX command
was rerun.

## Final retained-root evidence

At the final failure checkpoint each root is a flat inventory of exactly 17
ordinary mode-`0644`, link-count-one files, with zero child directories,
symlinks, or other objects. Corresponding A/B files are byte-identical and
inode-distinct. Every one of the 17 file identities matches the frozen R0
contract. The basename/content u64-framed aggregate in each root is exactly
677,746 bytes with SHA-256
`ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145`.

The six final output identities in both roots are:

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.aux` | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 |
| `main.bbl` | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 |
| `main.blg` | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 |
| `main.log` | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 |
| `main.out` | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 |
| `main.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |

The four merged-stream identities in both roots are:

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `pass1.merge` | `bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29` | 19,722 | 662 |
| `pass2.merge` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `pass3.merge` | `c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59` | 8,971 | 174 |
| `pass4.merge` | `f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b` | 7,837 | 130 |

The final root source identities are the frozen project identities:

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.tex` | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 |
| `math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |

Both exact roots are retained privately and must not be retried, continued,
cleaned, or mutated. They remain terminal failure evidence only. No claim is
made that a pre-command root-source hash observation exists.

## Project and authority stop

Immediately before this blocker was written, both build-time root ledgers
still had their exact opening identities; all 40 project-opening files were
unchanged; the three R1 success paths and the future R2 review path were
absent. This blocker is the sole project write of the failed invocation.

The builder performed no source, bibliography, pre-existing output, evidence,
or governance edit; no self-review or R2 action; no release, finalization,
Paper 25, repository, upload, external messaging, package, or network action. The
one-shot R1 authority is terminally consumed and grants no retry or repair.

R1_BUILD_BLOCKED
