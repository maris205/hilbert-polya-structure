# Paper 22 — Deterministic R1 No-Op Build Authorization

Date: 2026-08-24 UTC  
Stage: unchanged-source deterministic R1 build  
Disposition: exactly one distinct build-author invocation authorized; all
source and all pre-existing project artifacts are frozen

## Controlling scope and issuance provenance

This note authorizes exactly one distinct R1 build author to perform one
one-shot invocation comprising two fresh independent builds, local read-only
acceptance validation, construction of the two success JSONs, and one
success-or-failure persistence decision. Authority is consumed when that
author first creates either R1 temporary root. It cannot be split between
authors, resumed, retried, or reused after success or failure. A false or
unproved precondition grants no build authority.

The following values are **authorization-author opening/issuance
provenance**. They identify the root state in which this final authorization
was authored. They are historical bindings and are explicitly **not future
build-time preconditions**:

| Issuance artifact or field | Opening/issuance value |
|---|---|
| `BATCH_06_STATUS.md` | SHA-256 `c529e88eb473ca0f2fc528b67dfb2e51921d4e937bf85d10de9460d563d30c03`; 33,827 bytes; 527 LF |
| issuance gate | `PAPER22_R1_BUILD_AUTHORIZATION_OPEN` |
| issuance Paper 22 queue | `R1_NO_OP_REVISION_PASS_PENDING_BUILD_AUTHORIZATION` |
| `BATCH_06_IDEA_REPORT.md` | SHA-256 `c9368d590b626ae65b467d1f53a51e35f97bf8d15d3ba7945d83d36746fa0da4`; 43,752 bytes; 869 LF |
| Paper 22 issuance inventory | 40 regular files; four child directories; zero symlinks |

At issuance, this authorization, `paper/BUILD_METADATA_R1.json`,
`paper/BUILD_RECEIPT_R1.json`, `paper/main_round1.pdf`, and
`notes/BUILD_R1_BLOCKER.md` are all absent. No temporary R1 root has been
created.

Before any R1 builder may act, a later parent consumption transition must:

1. append this authorization's exact path, SHA-256, byte count, LF count,
   and exact terminal line to both `BATCH_06_STATUS.md` and
   `BATCH_06_IDEA_REPORT.md`;
2. set the current gate exactly to
   `PAPER22_DETERMINISTIC_R1_BUILD_OPEN`; and
3. set the Paper 22 queue exactly to `R1_BUILD_AUTHORIZED`.

The authorization path is
`papers/22-hamiltonian-cubic-spectral-collapse/notes/BUILD_AUTHORIZATION_R1.md`.
That parent transition necessarily changes both issuance-time root-ledger
identities above. It is not a build-author action. The R1 builder must hash
and bind the actual post-consumption bytes, byte/LF counts, and terminal lines
of both ledgers; verify the exact gate, queue, and authorization binding; and
freeze those actual ledger bytes throughout the invocation. The opening
hashes in the table above must never be substituted for those build-time
identities.

At build invocation start the Paper 22 project must contain exactly 41
regular files, four child directories, and zero symlinks. The forty-first
file is this authorization, ending exactly `BUILD_AUTHORIZATION_R1`; the
other 40 are the unchanged issuance files. The three success paths and the
optional blocker must still be absent. All 41 project files and, separately,
the actual post-consumption ledger snapshots are immutable to the builder.

## Frozen source and no-op evidence

The only build source is this exact unchanged trio:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

The following no-op evidence is also frozen and must be rebound exactly:

| Evidence | SHA-256 | Bytes | LF | Required status/terminal |
|---|---|---:|---:|---|
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md` | `cc1d6f222ab500c10040c28f24bf3207fe5b0d645dc7a695e1406eb997e5f868` | 24,176 | 195 | `BUILD_R1_R0_REPAIR_PASS` |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | `4da8ff908be280bb9140eaf23ab60a726794ca9d6e2b95a4b2356fda8d350df3` | 2,729 | 68 | `R1_REVISION_WINDOW_NO_CHANGE` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `a77154a2150e74af115cb2ced4767f9617bafdb22267373b8128ebed09c3208d` | 3,967 | 1 | schema `PAPER22_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1`; status `R1_NO_OP_REVISION_PASS` |

The source receipt records one authorized window, one consumed window, zero
remaining windows, zero changed paths/hunks/bytes, and identical before/after
source identities. These facts are hard build preconditions; this
authorization opens no further revision window.

## Frozen R0 comparator evidence

The accepted R0 evidence is immutable:

| Evidence | SHA-256 | Bytes | LF | Required status/terminal |
|---|---|---:|---:|---|
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `8095586065f3f997125b29231ffcff28be1d099ecd01bedc22eb75b7809ee6ca` | 21,642 | 389 | `BUILD_AUTHORIZATION_R0_REPAIR` |
| `paper/BUILD_METADATA_R0.json` | `10797a9079fea64629a852dbf6644302a35ef2a96e8b05573eae9799f865345c` | 65,981 | 1 | `BUILD_METADATA_R0_REPAIR` |
| `paper/BUILD_RECEIPT_R0.json` | `4e7810b9ac2ad628503634539f0997a418aa4f583c9557ef6a5c41146b95dcec` | 66,318 | 1 | `BUILD_R0_REPAIR_PASS` |

The R0 receipt binds accepted roots
`/tmp/paper22-r0-repair-A.0zGVu9` and
`/tmp/paper22-r0-repair-B.FwYPpz`. Their paired accepted command-log
identities are:

| Log | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `command-1.log` | `1775b04cad10c07ae781f497ffea53bb3e1a8d03dfaacf9ee2f313300fc5fe41` | 16,779 | 552 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `command-3.log` | `7418c3d6b43f0c109246fe2bfdd39ec19e07a6c93e43ce55924f93bb44b2f9b7` | 8,372 | 156 |
| `command-4.log` | `0de737419e403fbfcca1c53d69ac98dbe55297e63de51697d8bca064d4c198c6` | 7,642 | 123 |

The current six outputs match the R0 receipt and both accepted R0 roots:

| Output | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.aux` | `22a3bcd35b0aa9b87d6a4e40fe9f0cdc422fee366cf72e848be149486e5bcfb2` | 17,245 | 191 |
| `paper/main.bbl` | `13faf55051bd94bf0cacdf4cae3b6476b77c417657bd8184b6f2446b1c28c3aa` | 1,738 | 45 |
| `paper/main.blg` | `911285900fa9c373c657edd562d9cc284cd702194ab99094be5870613ef15f92` | 896 | 46 |
| `paper/main.log` | `3f8a5951bda82725d0731f0fd17d4e6b506ed2084e48bb7a9663b69ab5924cb0` | 27,869 | 712 |
| `paper/main.out` | `c732b3ddb9511976c30b5b00e10709c77c022636e419de173c10db9ce172093a` | 8,604 | 36 |
| `paper/main.pdf` | `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7` | 471,647 | 2,649 |

`paper/main_round0.pdf` has the same SHA-256 and 471,647-byte identity as
`paper/main.pdf`, and direct byte comparison must pass. These current
outputs and both R0 JSONs are pre-existing evidence: the R1 builder may read
them but must not write, replace, relink, chmod, or otherwise change them.

## Exactly two fresh independent builds

Create exactly two distinct, brand-new private temporary directories,
designated R1 root A and R1 root B. Each must be created independently, have
mode `0700`, have a unique canonical absolute path that did not previously
exist, not be a symlink, and share no artifact with the other root by symlink
or hard link. Before command 1, each root contains exactly three regular
files and nothing else: independent byte copies named `main.tex`,
`math_commands.tex`, and `references.bib`, matching the frozen trio.

Neither R1 root nor any build command may reuse, copy from, cache from, write,
or otherwise touch the old diagnostic roots `/tmp/paper22-r0-A.PIwA2V` and
`/tmp/paper22-r0-B.xwtGZQ`, the accepted R0 repair roots named above, or
`/tmp/paper22-r0-repair-validation.Y4OsGc`. A validation harness may perform
read-only direct comparisons against retained accepted R0 files only after
both R1 command sequences have completed; those R0 paths remain immutable
and are never build inputs.

Every child build process receives an empty inherited environment populated
with exactly these six variables and no others:

| Name | Exact value |
|---|---|
| `PATH` | `/usr/bin:/bin` |
| `SOURCE_DATE_EPOCH` | `1787529600` |
| `FORCE_SOURCE_DATE` | `1` |
| `TZ` | `UTC` |
| `LC_ALL` | `C` |
| `LANG` | `C` |

With each root as its exact working directory, run this sequence exactly
once, in order:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

The resolved executables must remain `/usr/bin/pdftex`, SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`,
and `/usr/bin/bibtex.original`, SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.
Capture each merged stdout/stderr stream as `command-1.log` through
`command-4.log` in its own root without changing arguments, environment,
working directory, bytes, or exit status. There is no retry, fifth pass,
cleanup build, `latexmk`, engine substitution, shell escape, package
installation, source generation, or correction after failure.

## Conjunctive acceptance contract

Success requires every final-R0 acceptance check to be repeated at least as
strictly and every condition below to pass. No waiver or aggregate judgment
can compensate for one false, missing, ambiguous, or unrecorded conjunct.

### Execution, immutability, and cross-round determinism

1. Both exit vectors are exactly `0,0,0,0`.
2. Hash the project trio before copying and after all work, and each root trio
   before command 1 and after command 4 and validation. Every identity remains
   exactly frozen; all source copies are independent.
3. Each root has readable, nonempty final `main.aux`, `main.bbl`, `main.blg`,
   `main.log`, `main.out`, and `main.pdf`, with stable start/end-validation
   identities.
4. All six outputs and all four corresponding command logs are directly
   byte-identical between R1 roots A and B.
5. Because the revision was a no-op, every one of those six outputs and four
   command logs in each R1 root is also byte-identical to its accepted R0
   counterpart and therefore has exactly the SHA-256, byte count, and LF
   count in the comparator tables above. Each R1 PDF is byte-identical to
   current `paper/main.pdf` and `paper/main_round0.pdf`, SHA-256
   `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`.
6. Record both canonical root paths, creation/freshness evidence, mode,
   ownership, device/inode/link evidence, exact initial inventories, working
   directories, commands, environments, exits, logs, outputs, source copies,
   cross-root comparisons, cross-round comparisons, and identity-stability
   checkpoints.

### Closure and diagnostics

1. Final AUX is closed under `plainnat`/`references`; all citations and
   references resolve. BBL contains exactly six unique items, BLG and both
   command-2 logs have zero BibTeX error and warning, and no seventh item
   exists.
2. The four bounded citation commands use exactly the six distinct keys
   `BlancVanSanten2021`, `ShaoSun2025`, `Deserti2016`, `DangFavre2021`,
   `Rangarajan2002`, and `FujiokaKogawaLiShudo2023`. Every key is defined and
   cited, and no citation is used as proof of a gradient, selector, cone,
   carry, leading-form, visibility, matrix, cubic, multiplicity, boundary,
   coefficient, or threshold claim.
3. Final OUT is syntactically readable with exactly 36 resolved bookmarks,
   including plain repaired bookmark text `g=2r`, and no raw failed
   PDF-string math, unresolved token, or private provenance.
4. Each final `main.log` and each `command-4.log` has zero fatal error, zero
   LaTeX/package warning, zero hyperref PDF-string warning, zero undefined
   citation/reference, zero multiply-defined label, zero changed-label or
   rerun event, and zero overfull box. The only permissible final diagnostics
   are exactly three underfull boxes, all at source line 944, with badness
   sequence `6316, 10000, 6316`; visual inspection must confirm Table 2 is
   complete and legible.
5. All first-pass convergence diagnostics are counted and recorded and are
   absent from the final state. Source, AUX/BBL/BLG/LOG/OUT, command logs,
   extracted text, metadata, bookmarks, and PDF objects contain zero TODO,
   TBD, FIXME, VERIFY, placeholder, citation-needed, unresolved citation or
   reference marker, double question mark, or private build provenance.

### PDF safety, identity, pagination, and visual review

1. Both root PDFs are structurally valid, fully readable on all pages,
   unencrypted, and byte-identical. They contain no JavaScript, dangerous
   action, attachment, embedded file, form, AcroForm, XFA, signature,
   multimedia, image object, or image; all physical pages are US Letter
   `612 x 792` points with rotation zero.
2. Exactly 28 reported fonts are present; every font is embedded, subsetted,
   and Unicode mapped. A zero-font result cannot pass.
3. The decoded title is exactly “Cubic Spectral Collapse for Endpoint-Spiked
   Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode
   Number”. Visible author is exactly `Anonymous`; PDF Author, Creator, and
   Producer are each empty.
4. Epoch `1787529600` is `2026-08-24T00:00:00Z`. Raw CreationDate and ModDate
   are each exactly `D:20260824000000Z`; there is no visible source date or
   conflicting metadata date.
5. There are exactly 26 physical, nonblank, readable pages. Abstract begins
   on page 1; Section 8 begins on page 24; Limitations and Conclusion begin
   on page 26; Conclusion ends before References; References begins and ends
   on page 26; there is no appendix. The recorded body boundary must preserve
   the 26.5-page target, preferred 24–28 band, and hard 22–30 band under the
   R0 convention.
6. Read-only structural, text, metadata, bookmark, action/link, font,
   security, geometry, page-boundary, citation, and private-text checks must
   reproduce the accepted R0 observations. Render and visually inspect all
   26 pages, including Tables 1–3 and detailed boundary pages, and record zero
   blank, corrupt, clipped, cropped, overlapping, or table-overflow page.
   Rendered content, metadata, bookmarks, annotations, and objects disclose
   no project/root path, hash, ledger gate/queue, review/build history,
   permission record, agent/tool identity, or other private governance text.

## Strict R1 JSON contract

`paper/BUILD_METADATA_R1.json` and `paper/BUILD_RECEIPT_R1.json` must each be
strict recursive-canonical, compact, one-line UTF-8 JSON with exactly one
terminal LF and no other line break. Each must have zero BOM, CR, NUL,
invalid UTF-8, insignificant whitespace, duplicate key at any depth,
nonfinite number, or trailing content. Every object, including `checks` and
all objects nested beneath it, is ordered recursively by increasing Unicode
code point; arrays retain semantic order and finite numbers use one canonical
form. Each `self_identity` has `bytes:null` and `sha256:null`; neither file
may claim a circular non-null self identity.

The required top-level schema and status pairs are:

| Artifact | `schema` | `status` |
|---|---|---|
| `BUILD_METADATA_R1.json` | `PAPER22_BUILD_METADATA_R1_NO_OP_V1` | `BUILD_METADATA_R1_NO_OP` |
| `BUILD_RECEIPT_R1.json` | `PAPER22_BUILD_RECEIPT_R1_NO_OP_V1` | `BUILD_R1_NO_OP_PASS` |

Before persistence, each exact candidate byte string must independently pass
two genuinely independent strict parser/canonical-encoder implementations.
Each implementation must reject duplicates at every depth, nonfinite values,
invalid text and trailing content; verify recursive Unicode-code-point order
including all nested checks; re-encode with compact separators and one LF;
and reproduce the candidate bytes exactly. The two value trees must agree.
Native `JSON.parse`/`JSON.stringify` alone is insufficient. Record parser
names/versions, adversarial rejection results, nested-object counts/order
checks, byte-exact round-trip results, and round-trip SHA-256 values.

Together the JSONs must bind, without an unrecorded side ledger:

- this authorization's final path/SHA-256/bytes/LF/terminal, the historical
  issuance table, both actual post-consumption root-ledger identities and
  terminals, both authorization bindings, exact build-open gate/queue, and
  the one-shot invocation identity;
- the source trio before/after in the project and both roots; the R1 build
  review, no-change ledger, no-op source receipt and schema/status/window
  facts; the R0 authorization, metadata, receipt, accepted roots, current
  outputs, and both existing equal PDFs;
- both fresh R1 roots, creation/permissions/initial inventories, executable
  identities, exact environments/commands/exits, all source/log/output
  identities and stability checks, all A/B comparisons, and every direct
  cross-round comparison;
- every closure, warning/box, marker/private-text, PDF safety/font/metadata/
  date/page/boundary/visual, citation/bibliography, and JSON-parser check with
  observed evidence and counts; and
- the actual effective filesystem permissions, the complete granted and
  denied authority, persistence transaction, and zero external effects.

The receipt must bind the finalized external byte identity of the metadata.
Canonicality is a byte-level acceptance fact, not a claim inside the JSON.

## Success-only persistence, failure, and handoff

No success path may exist in the project until every conjunct and both JSON
candidates pass. Temporary candidate staging, if needed, stays inside an
authorized private R1 root after its build-output checkpoint and never in the
project. Persistence is exclusive-create, all-or-nothing, and no-overwrite.

On success, create exactly these three new regular project paths and no
others:

1. `paper/BUILD_METADATA_R1.json`
2. `paper/BUILD_RECEIPT_R1.json`
3. `paper/main_round1.pdf`

`main_round1.pdf` is a byte copy of an accepted R1 root PDF. The six current
outputs `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, and
`main.pdf` remain byte-identical to both R1 roots and the R0 comparators, but
their existing content must not be written or changed. `main.pdf`,
`main_round0.pdf`, and `main_round1.pdf` must be directly byte-identical and
share SHA-256 `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`.
Success inventory is exactly 44 regular files, four child directories, and
zero symlinks. All 41 pre-build paths and both root-ledger checkpoints remain
content-identical to invocation start; no blocker exists.

Any false, missing, ambiguous, drifting, or unrecorded conjunct is failure.
Failure creates none of the three success paths; any partial path created by
a failed persistence transaction is rolled back. The only optional project
write on failure is `notes/BUILD_R1_BLOCKER.md`, a standalone factual record
whose exact final nonempty line is `R1_BUILD_BLOCKED`. Whether or not that
blocker is written, the authority is consumed. There is no repair, source
edit, second root pair, replacement invocation, retry, or self-review.

Retain both fresh R1 roots privately and unchanged after the final identity
checkpoint for a fresh, separately authorized independent R2 review. The R1
builder must report the complete bound identities, counts, comparisons,
parser results, inventories, success artifacts or blocker, and then stop.

This note authorizes no manuscript or bibliography edit, further revision
window, release, finalization, publication, submission, upload, transport,
repository action, messaging, identity disclosure, Paper 23 work, network
access, CAS/scientific execution, or external effect.

BUILD_AUTHORIZATION_R1
