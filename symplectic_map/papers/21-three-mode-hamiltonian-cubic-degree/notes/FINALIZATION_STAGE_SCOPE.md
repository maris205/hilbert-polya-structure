# Paper 21 Finalization Stage Scope

Date: 2026-08-22 UTC

Project: `papers/21-three-mode-hamiltonian-cubic-degree`

Public title: **Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies**

## 1. Authority and present state

The fresh independent build R2 review is stable and ends exactly
`BUILD_R2_R1_PASS`. This scope freezes the exact after-R2 project universe and
defines a local-only finalization protocol. Its creation does not copy a PDF,
compile a source, create a release manifest or terminal receipt, perform a
terminal review, or produce any external effect.

The governance author may write exactly this file and then
`experiments/finalization_lock.json`, in that order, and must stop. The stable
identity of this scope is computed before the lock is written. This scope can
bind the future lock only by path, role, order, strict-canonical contract, and
self-exclusion rule; it cannot bind bytes that do not yet exist. The lock may
record its own safe path and schema but must exclude its own hash and byte
count.

Source and bibliography edits, manuscript revision, build commands, release
candidate copying, manifest or receipt authoring, scientific execution,
network access, submission, upload, public hosting, repository push, external
messaging, and identity disclosure are unauthorized in this role.

## 2. Exact frozen input universe F51

`F51` is the complete project universe immediately before this scope was
created: 51 regular non-symlink files, exactly four directories
(`experiments`, `notes`, `paper`, `refine-logs`), zero symlinks, and zero other
filesystem entry types. Paths are unique, safe project-relative paths in
lexicographic byte order. LF is the count of byte `0a`, including for PDFs.

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `844268240ac6230d215623a58b77f12fbe2da83a58456c0adc70168a8f444474` | 3238 | 73 |
| `experiments/EXPERIMENT_TRACKER.md` | `8f56ee7483ef087a4539cf842b7fc1dc41ead3fa442949171751b80ccf2fa251` | 2097 | 37 |
| `experiments/publication_lock.json` | `14966ffc04e0ce68eed83688bfaf871aa02422ba2564532d0f6fff5a7071e114` | 6704 | 1 |
| `experiments/source_lock.json` | `41f350ca31fc06cf0eae3412419fa6d4615f9670a5d2150b04d7e59f9986b202` | 19857 | 1 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `9425a79546d7c95742920fe2bbd208771a0fdf2d83288b0c8bc27fe2f2361fce` | 2082 | 46 |
| `notes/BUILD_AUTHORIZATION_R1.md` | `3c295e8cf890b5309baf8c2be6fcd026507b5132562425a4ec93f6f13e005284` | 1652 | 37 |
| `notes/BUILD_R0_BLOCKER.md` | `6b97f1203541b254cd1b0a60c7ed29978e2a500286c0ba1b72dad0712276fada` | 3145 | 79 |
| `notes/BUILD_RECEIPT_R0_CANONICAL_REPAIR.md` | `fefe63317ca10890ba6763bc1fc0dcd3a8c92497caed3ebc454d2704f841e510` | 2168 | 60 |
| `notes/CITATION_VERIFICATION.md` | `0b7586368ced09d13f6e0d43d9493080bae18a78ec1fe36374434aea46612355` | 1338 | 17 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `44151f219d87c3c9ca662e360b248d60bc1262a87fcc01a91c24add5aff9dc16` | 3266 | 55 |
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REPLACEMENT_REVIEW.md` | `62511dd572fa14bdea670df85eb6a48fc54e081a916af5935fdca8f870531bdd` | 5005 | 41 |
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md` | `90d4c0ac6aa682dbd1ca0df5d1a3d75c42ba56d2a4df341643db888bf753be1c` | 7319 | 148 |
| `notes/INDEPENDENT_BUILD_R2_R1_REVIEW.md` | `69f0c560443edbf3f718e47507081525ddd1f2caa383f6bfbd1ec9378cf6070a` | 11252 | 202 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `d92d3fa956c54d5336aed9b699cdc8c61bcf45fccf9342d05548b70ff37585dc` | 2366 | 31 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md` | `e2a0298dddb21d6874edc21f4ad03290f0397e4bb87705f0485f6684a4b96f5f` | 2629 | 46 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `07114e0da0eb41ed827f86064186639ffed49c2be2db97bf3e016d7390fface0` | 6040 | 110 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REPLACEMENT_REVIEW.md` | `135657999f99081f4eb92a35f3b017b87349c0a85de4e75526f48e52a287c6e5` | 7470 | 152 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `c2c8a1327e9f40b5756cfcf0fd5ada4669bf035a41a1529d0daa5f5dc5f8a8b6` | 4177 | 77 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md` | `3516bb3fb81d455233442e63e01905e0f39779f77fb2e2577e2e1d6c0cca1d32` | 1486 | 29 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `3b606a9481811d795dd7fe5ebb16bf280898f56748e61045f8b802de0b063a3a` | 10290 | 299 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_REVIEW.md` | `0aca263b6836f899c134e887f9cc4979f93ab966132eb7d5c74bb1157cf501f6` | 5565 | 105 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `2f82e647a90fb70a2d598d738033085d01546bd76787841f32c2e7378e3f3858` | 2775 | 42 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `1dc6f622048c9737bed40aa92dd5da8f53be9437e5f8e4005a63b3d451260979` | 2060 | 36 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `1dc32c47d06b06657b9ed810df3ad6b2c4365d3b32aa5a49a5e93da1c410eaac` | 6091 | 125 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `5fedcaf69d5e90a4bf9c3ad2eafa83965b1954601adc9e0b8bb2ac89be8abc45` | 4670 | 77 |
| `notes/NOVELTY_ASSESSMENT.md` | `a8c3c93e828ad86c940d038cf347630def5b3a58fdecd606357b2813e1c14941` | 3014 | 58 |
| `notes/PROOF_PACKAGE.md` | `599c9da5e5d4ca0e0b78c7b8683cdd2d63da50e555d9d6984bf1cf09f55e21d6` | 16199 | 427 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `94c185559e9ecb0c0680aa4c58b2fb725e80128bea465b6d4b6e26cbe0decccd` | 4653 | 104 |
| `notes/R0_PROOF_FIRST_SOURCE_REPAIR.md` | `4c8ec1258876305cd447bdf175b5a88fe801f69fdfd78d0ee956ae7463171a12` | 4373 | 102 |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | `0d8e1eed4feb45bd20f90907eb1bddaae42ea7fedd9e34869f24395b20aeaf5f` | 1571 | 35 |
| `notes/RESEARCH_QUESTION.md` | `185c276bac0c10b011b2077154103c7cb305550a60469b28b748cc4370e1577d` | 2362 | 49 |
| `paper/BUILD_METADATA_R0.json` | `69c67c1485ec95465e522a0d92fea8dcc8ce4d91ed406c39bf57d19563df5e2c` | 2378 | 1 |
| `paper/BUILD_METADATA_R1.json` | `8653c6d500998b9f915958eaa78d818feeb9e93d581c37f9fce86e49aa97b2ab` | 1782 | 1 |
| `paper/BUILD_RECEIPT_R0.json` | `3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96` | 7339 | 1 |
| `paper/BUILD_RECEIPT_R1.json` | `fa0a511a3391135db75b6eaef03e83fa90930219ddacb8aeaf4713d2aff0bada` | 5380 | 1 |
| `paper/PAPER_PLAN.md` | `63a7de8600af40648bb4ab94903bd4331bf4dc4265aabe8b88392a595b60a620` | 15765 | 245 |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `441c1cc5e7b3372bbe1d7f05e34ac19461f109bcb0de1e9f7cd4e23db6ba8d42` | 2126 | 1 |
| `paper/main.aux` | `f203a377a6752a16ae22b61dd9c241a638081da2b7d54141ac62a2ab785d18c6` | 12760 | 113 |
| `paper/main.bbl` | `1be6c9b14cae6da54ed8ab04d9739d0bb02ccc363f52ac6ad69b2c2dcf19a1de` | 731 | 20 |
| `paper/main.blg` | `4ef0e5c28c45d31e9cd0f4459679b0a06bfaa2555498a2f87c6b6e68f588d804` | 885 | 46 |
| `paper/main.log` | `ac51e35e84d6cb610ccdb79c57cf79a64da91019656c61167fa65fd1e9e33233` | 29049 | 740 |
| `paper/main.out` | `25820119b32d0994e23555952047c4fe7ddce7a140420b21a1817b9e9141208c` | 4090 | 16 |
| `paper/main.pdf` | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` | 465922 | 2539 |
| `paper/main.tex` | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` | 84917 | 1990 |
| `paper/main_round0.pdf` | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` | 465922 | 2539 |
| `paper/main_round1.pdf` | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` | 465922 | 2539 |
| `paper/math_commands.tex` | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` | 981 | 33 |
| `paper/references.bib` | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` | 675 | 19 |
| `refine-logs/FINAL_PROPOSAL.md` | `c39affe93a6a515c84303caa266733dde0a77df293b4410da92b486a11153fc0` | 2794 | 67 |
| `refine-logs/INITIAL_PROPOSAL.md` | `d38dae672970d3baf032a4ed6540134691e1c138e607a1a8dd8dc471eebb988e` | 1543 | 44 |
| `refine-logs/REVIEW_SUMMARY.md` | `f60a63a75ce6933b97a6b3f143f8f647ea861f1a7e83ce62437184f1b8b077e7` | 1392 | 28 |

## 3. Authoritative chain and retained non-authority

The authoritative terminal source is exactly the trio
`paper/main.tex` / `paper/math_commands.tex` / `paper/references.bib` at
`34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2`,
`05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`,
and `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`.
Its fresh source repair reviews are `07114e0d...` and `3b606a94...`.

The build chain retains, in order: the 21-page R0 blocker; the proof-first
repair ledger and authorization; repaired R0 metadata and current canonical
receipt `3899ee59...`; the first build review's canonical-order block; the
receipt-only repair ledger; replacement build R1 pass `62511dd5...`; explicit
no-op revision ledger and receipt `441c1cc5...`; R1 authorization, metadata,
receipt `fa0a511a...`, and round PDF; and final independent build R2 pass
`69f0c560...`. The three persisted PDFs are byte-identical at
`b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`,
465922 bytes and 2539 LF.

The stale initial/replacement source reviews and the two PAGEFIX reviews are
retained historical evidence but are non-authoritative because they bind
superseded source identities or failed independence. The first build R1 review
is an authoritative blocker in the incident lineage, not a build pass. No
later object may promote a historical final line over these explicit roles.

## 4. Monotone stage universes and future paths

At every gate, the live inventory must be re-enumerated rather than inferred.
The expected monotone universes are:

- `F51`: the 51 frozen inputs above;
- `G53 = F51 + {notes/FINALIZATION_STAGE_SCOPE.md,
  experiments/finalization_lock.json}`;
- `P54 = G53 + {notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md}`;
- `R56 = P54 + {paper/main_release_candidate.pdf,
  paper/FINAL_RELEASE_MANIFEST.json}`;
- `Q57 = R56 + {paper/TERMINAL_REBUILD_RECEIPT.json}`;
- `T58 = Q57 + {paper/reviews/final_integrity_review.md}`.

`paper/reviews` is the only expected new directory and may not exist until all
terminal checks and cleanup have passed. No stage may pre-create a later path,
skip a predecessor, modify an earlier path, retain an unlisted project
artifact, or follow a symlink.

## 5. Five closed temporal roles

1. **Finalization-governance author.** Reads `F51`; writes this scope and the
   lock in order; validates read-only; stops.
2. **Independent finalization reviewer.** Is distinct from the governance
   author and authored none of `F51` or the governance pair. Reads exact
   `G53`; on success writes only
   `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, ending exactly
   `FINALIZATION_STAGE_PASS`; on blocker writes nothing.
3. **Release-candidate author.** Is distinct from the first two roles. Reads
   and rehashes exact `P54`; first creates `paper/main_release_candidate.pdf`
   as an exclusive raw byte copy of `paper/main_round1.pdf`, with no compile,
   transform, metadata rewrite, rendering, signing, or optimization; then
   writes strict-canonical `paper/FINAL_RELEASE_MANIFEST.json`; stops.
4. **Terminal-build evidence author.** Is distinct from the preceding roles.
   Reads exact `R56`; builds only in two fresh root-owned mode-0700 roots
   matching `/tmp/paper21-terminal-[ab].XXXXXX`; copies only the frozen source
   trio; runs exactly `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` under
   `SOURCE_DATE_EPOCH=1787356800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
   `LC_ALL=C`, `LANG=C`, `PATH=/usr/bin:/bin`; then writes only strict-
   canonical `paper/TERMINAL_REBUILD_RECEIPT.json`. The two roots remain live
   for independent inspection.
5. **Sole terminal-integrity reviewer.** Is fresh, distinct from all four
   roles, and authored none of `Q57`. Reads exact `Q57`, both live terminal
   roots, and the eight explicitly governed temporary roots. It independently
   verifies every binding, build output, diagnostic, PDF property, theorem,
   citation, anonymity, and visual gate. Only after all checks pass does it
   clean each exact validated root without wildcard, recursive broad target,
   unresolved variable, or symlink traversal. It then creates `paper/reviews`
   and writes only `paper/reviews/final_integrity_review.md`, whose last two
   nonempty lines are exactly `FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`.

The roles are temporally fenced; a later role starts only after its predecessor
has stopped and the complete predecessor universe has been rehashed.

## 6. Candidate, manifest, terminal build, and cleanup contract

The candidate PDF must equal `paper/main_round1.pdf`, `paper/main_round0.pdf`,
and existing build output `paper/main.pdf` byte for byte at SHA-256
`b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`.
The manifest binds every non-self file in exact `R56`, records raw-copy
provenance and the complete dependency DAG, excludes its own hash and byte
count, and leaves every external effect false.

The terminal receipt records the two literal roots, environment, eight zero
exit codes, four command-stream identities per root, complete root snapshots,
A/B correspondence, and six-way PDF equality
`A = B = main_round0 = main_round1 = main.pdf = main_release_candidate`.
It records 27 pages; body through conclusion page 27 within the 24--29
contract; zero fatal, undefined, marker, warning, and overfull diagnostics;
exactly seven nonblocking underfull hboxes; 25/25 embedded, subsetted, Unicode
fonts; no raster images, attachments, JavaScript, forms, encryption, or
identity leak. Its status before terminal review is exactly
`TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT`.

The terminal roots plus these six historical roots must remain until the sole
terminal reviewer has checked them directly:

- `/tmp/paper21-r0-a.pDEi2V`
- `/tmp/paper21-r0-b.QB6qsy`
- `/tmp/paper21-r0-repair-a.rai5wu`
- `/tmp/paper21-r0-repair-b.WlpPpd`
- `/tmp/paper21-r1-a.cMLvZF`
- `/tmp/paper21-r1-b.2D6a87`

For each root, the terminal reviewer must revalidate the literal path, real
parent `/tmp`, directory type, owner, mode, no symlinks/subdirectories, and
exact direct-child inventory, then unlink each named non-symlink file and use
`rmdir` on the empty root. Cleanup may not alter any project byte.

## 7. Canonical JSON and terminal effect

The lock, manifest, and terminal receipt use UTF-8 strict canonical JSON:
recursive Unicode key order, compact separators, no BOM/CR/NUL, no duplicate
keys or nonfinite numbers, exactly one terminal LF, and byte-identical strict
decode/re-encode round trip. Each self-referential artifact declares its own
safe path and self-exclusion; no circular hash claim is permitted.

Final PDF metadata must retain the exact title, `Anonymous Authors`, empty
subject and keywords, deterministic creation/modification time, and benign
toolchain `Creator`/`Producer` values. Those toolchain fields are not author
identity. The theorem, characteristic-zero and `g >= 8` assumptions, exact
matrices and cubic, mod-five residue classes, anti-claims, and two-entry
bibliography remain frozen.

The only possible terminal effect is `LOCAL_ANONYMOUS_RELEASE_ONLY` after the
sole terminal review passes. Submission, upload, public hosting, repository
push, external message, and identity disclosure remain false and unauthorized.

## 8. Zero-write independent-review block and governance recovery

The first independent finalization-stage review attempt rehashed all of exact
`G53`, passed 72 checks, found one lock-only blocker, and wrote no project
file. The first lock identity was
`7f5473d849dcf7179432395dd32be257b43942ca0d4aca7661686bf8add8682e`.
Its `authoritative_chain` assigned terminal `BUILD_R0_BLOCKED` to
`notes/BUILD_R0_BLOCKER.md`, whereas that bound file's exact state and final
nonempty line are `R0_BLOCKED`.

This same-path governance recovery changes that one terminal value to
`R0_BLOCKED`, updates the lock's binding to this amended scope, and records the
superseded scope/lock identities. It changes no `F51` path or byte, source,
bibliography, PDF, receipt, metadata, review, theorem, build output, stage
path, role fence, cleanup rule, or external-effect rule. The failed review
attempt grants no authority. A fresh independent reviewer must rehash the
complete recovered `G53` and may pass only the new identities.

FINALIZATION GOVERNANCE SCOPE AUTHOR STOP
