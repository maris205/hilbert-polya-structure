# Paper 22 — Deterministic R0 Repair-Build Authorization

Date: 2026-08-24 UTC  
Stage: repaired-source deterministic R0 build  
Disposition: exactly one build-author invocation authorized; all source is frozen

## Controlling scope

This note authorizes exactly one distinct, one-shot build-author invocation
for Paper 22. That invocation comprises the two fresh builds, local
acceptance inspection, success-receipt construction, and the single
success-or-failure persistence decision specified below. Authority is
consumed when the build author first creates either temporary root. It cannot
be split between authors, resumed as a second invocation, retried, or reused
after either success or failure. A precondition mismatch grants no authority:
the build author must write nothing, report the mismatch, and stop.

The following table is immutable authorization-author opening/issuance
provenance. It records the root state in which this final authorization was
authored and issued; it is historical provenance, explicitly not the future
build-invocation root state.

| Authorization-author opening/issuance artifact or field | Issuance value |
|---|---|
| BATCH_06_STATUS.md SHA-256 | 84d3da0a87a2da2e7bc980af4f233e7f2121594cdd3950e61f26d77a344d482c |
| BATCH_06_STATUS.md gate | PAPER22_R0_REPAIR_BUILD_AUTHORIZATION_OPEN |
| Paper 22 queue | R0_REPAIRED_SOURCE_DUAL_PASS_PENDING_BUILD_AUTHORIZATION |
| BATCH_06_IDEA_REPORT.md SHA-256 | 2c07ac86da333aae6a911e01cae7c1013ad94b6fdbc0ba3addccf155b8cbbdc7 |

Before any build author can act, the parent must consume this final
authorization. That consumption must update BATCH_06_STATUS.md so that its
current gate is exactly PAPER22_DETERMINISTIC_R0_REPAIR_BUILD_OPEN and its
Paper 22 queue is exactly R0_REPAIR_BUILD_AUTHORIZED, and must append this
final authorization's path, SHA-256, byte count, LF count, and terminal line
to both root ledgers, BATCH_06_STATUS.md and BATCH_06_IDEA_REPORT.md. The
authorization path is
papers/22-hamiltonian-cubic-spectral-collapse/notes/BUILD_AUTHORIZATION_R0_REPAIR.md.
This required consumption changes the issuance-time root hashes above and is
not a build-author action.

At the start of the authorized invocation, the project must contain exactly
28 regular files, four child directories, and zero symlinks. The twenty-eighth
file must be this authorization note, whose final nonempty line must be
BUILD_AUTHORIZATION_R0_REPAIR; the other 27 files must be the unchanged
opening project files. The nine success-only paths and
notes/BUILD_R0_REPAIR_BLOCKER.md must all be absent. The build author must
hash this note before acting and bind its path, SHA-256, byte count, LF count,
and terminal line into both success JSON artifacts. The build author must
also hash and bind both then-current root ledgers, verify the exact
build-open gate and queue above, verify that both ledgers name and bind this
final authorization identity, and freeze those then-current root-ledger bytes
throughout the invocation. The issuance-time root hashes are not build-time
preconditions.

## Frozen input identities

The build source is exactly this trio and no other source or asset:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| paper/main.tex | 926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1 | 69,241 | 1,921 |
| paper/math_commands.tex | 544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c | 330 | 11 |
| paper/references.bib | 50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d | 1,928 | 55 |

The immutable provenance and two fresh repaired-source PASS reviews are:

| Role and path | SHA-256 | Bytes | LF | Exact terminal line |
|---|---|---:|---:|---|
| old blocker, notes/BUILD_R0_BLOCKER.md | 5242052c625add4ba084d5542faae221e6b1a1cb6d81b773b9295d968afbc7fd | 5,873 | 145 | R0_BLOCKED |
| repair receipt, notes/R0_HYPERREF_SOURCE_REPAIR.md | 0587269d6e5fcd4461a4749b6846d459c096d698dd460d2f4abf291463934ed5 | 7,553 | 189 | SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED |
| R1 source review, notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md | 6c02368dd361192628d4b79898b0a5fd9b273344d56e60179f52cb66dcc6d925 | 21,489 | 582 | PAPER_SOURCE_R1_R0_REPAIR_PASS |
| R2 source review, notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md | 8699472ce07744617c7407d051f84c2cca577c4d5e4ad4f9a0aa6f911ca1b0d5 | 26,796 | 891 | PAPER_SOURCE_R2_R0_REPAIR_PASS |

Every identity, size, LF count, and required terminal line in the frozen
source and provenance tables is a hard precondition and must be verified
again immediately before root creation. The issuance table remains bound as
historical provenance but its old root hashes are not required at build time.
All 27 opening project files, this authorization, the old blocker, the repair
receipt, and both source reviews are immutable throughout the invocation.
The actual post-consumption, build-open bytes of both root ledgers, as hashed
at invocation start, are likewise immutable throughout the invocation.

The prior diagnostic roots /tmp/paper22-r0-A.PIwA2V and
/tmp/paper22-r0-B.xwtGZQ are excluded inputs. They must never be reused,
written, copied from, used as a cache, or treated as either fresh root.

## Exactly two independent local builds

The invocation must create exactly two distinct, brand-new local temporary
directories, designated root A and root B. Each directory must not have
existed before this invocation, must have a unique canonical absolute path,
must be created independently rather than cloned from the other root, and
must be private with directory mode 0700. Neither root may be a symlink or
share a build artifact with the other through a symlink or hard link.

Before any build command, each root must contain exactly three regular files:
main.tex, math_commands.tex, and references.bib. Each must be an independent
byte copy from the corresponding frozen paper source and must match the
identity table above. No directory, figure, asset, prior AUX state, cache,
format file, command log, or other project file may be copied into either
root.

Every one of the eight child build processes must receive an empty inherited
environment populated with exactly these six name/value pairs and no others:

| Name | Exact value |
|---|---|
| PATH | /usr/bin:/bin |
| SOURCE_DATE_EPOCH | 1787529600 |
| FORCE_SOURCE_DATE | 1 |
| TZ | UTC |
| LC_ALL | C |
| LANG | C |

In each root, with that root as the exact working directory, run exactly this
ordered sequence once:

1. pdflatex -interaction=nonstopmode -halt-on-error main.tex
2. bibtex main
3. pdflatex -interaction=nonstopmode -halt-on-error main.tex
4. pdflatex -interaction=nonstopmode -halt-on-error main.tex

There is no fifth TeX or BibTeX command, cleanup pass, retry, latexmk call, or
engine substitution. A supervising harness may capture each process's merged
stdout/stderr byte stream as command-1.log through command-4.log inside its
own root, but capture plumbing must not alter the executable, arguments,
environment, working directory, exit status, or stream bytes. Corresponding
logs in roots A and B must have the same names.

No source edit, source generation, network access, package installation,
shell-escape option or executed shell command, CAS or scientific
computation, figure or asset input, external cache, remote service, or
external effect is authorized. Local read-only hashing, strict JSON
validation, and PDF/log inspection needed solely for this contract are
allowed. They must not alter a source, build output, command log, root
ledger, or pre-existing project artifact.

## Conjunctive acceptance contract

Success exists only if every condition in every subsection below is true.
The conditions are conjunctive: no otherwise good PDF, waiver, diagnostic
history, or reviewer judgment can compensate for one false or unproved
condition.

### Execution, source immutability, and two-root determinism

1. All eight commands exit zero. The exact exit vector is 0,0,0,0 in root A
   and 0,0,0,0 in root B.
2. The canonical project source trio is hashed immediately before copying
   and again after all build and validation work. Each root's copied trio is
   hashed before command 1 and after command 4 and all validation. Every
   before/after identity remains exactly the frozen identity above.
3. After command 4, each root has readable nonempty final main.aux, main.bbl,
   main.blg, main.log, main.out, and main.pdf. Read-only hashes taken at the
   start and end of validation are stable within each root.
4. Each of those six final generated outputs is byte-identical between root
   A and root B. For each index 1 through 4, command-N.log in root A is
   byte-identical to command-N.log in root B. This is paired equality by
   command index, not an assertion that different build stages have identical
   logs.
5. Exact SHA-256 and byte counts for both copies of all six generated outputs,
   all eight command logs, and all six source copies are recorded. The two
   canonical absolute root paths, creation evidence, modes, ownership,
   initial three-file inventories, working directories, exact command arrays,
   exact environments, and exit vectors are recorded.

### Final AUX, bibliography, OUT, and log closure

1. The final main.aux is closed: all citation and reference data are resolved,
   the plainnat bibliography style and references database are bound, and
   exactly the six frozen bibliography keys below have final bibliography
   labels.
2. The final main.bbl contains exactly six bibliography items for the same
   six keys, with no missing, duplicate, or seventh item. The final main.blg
   and both command-2.log files contain zero BibTeX error and zero BibTeX
   warning.
3. The final main.out is syntactically readable and closed, contains
   resolvable bookmarks, uses the repaired plain bookmark text g=2r for the
   repaired heading, and contains no raw failed PDF-string math, private
   governance text, or unresolved token.
4. Every command log has zero fatal error. The final main.log and both
   command-4.log files have zero LaTeX warning and zero package warning of any
   kind, including exactly zero hyperref PDF-string warning. They also have
   zero undefined citation warning, undefined reference warning, multiply
   defined label warning, changed-label/rerun warning, and overfull box.
   Any ordinary first-pass convergence diagnostic must be recorded and must
   be absent from the final state; it cannot survive as an accepted warning.
5. The source trio, final AUX/BBL/BLG/LOG/OUT, command logs, extracted PDF
   text, metadata, and bookmarks contain zero unresolved marker, including
   TODO, TBD, FIXME, VERIFY, placeholder, citation-needed text, double
   question marks, unresolved citation markers, and unresolved reference
   markers.
6. Every underfull box is counted with its complete log location and recorded
   in both JSON artifacts. Underfull boxes are nonfatal under this contract,
   provided all other conditions hold and the PDF inspection finds no
   clipping or corruption. The prior diagnostic history found three
   underfull boxes in Table 2 near source line 944; the fresh observed count
   and locations, rather than an assumption, control the receipt.

### PDF identity, safety, metadata, fonts, and pagination

1. Both PDFs are structurally valid and fully readable, unencrypted, and
   successfully processable across all pages. They contain no JavaScript,
   action script, attachment, embedded file, form, AcroForm, XFA content, or
   image object. Every physical page is US Letter and has rotation zero.
2. Every reported font is embedded, subsetted, and Unicode mapped. A zero-font
   result is not a pass.
3. The decoded title is exactly “Cubic Spectral Collapse for Endpoint-Spiked
   Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode
   Number”. The visible author is exactly Anonymous. PDF Author, Creator, and
   Producer are each exactly empty.
4. SOURCE_DATE_EPOCH 1787529600 means 2026-08-24T00:00:00Z. Raw CreationDate
   and ModDate are each exactly D:20260824000000Z, with no visible source date
   and no conflicting metadata date.
5. Rendered text, document metadata, outlines/bookmarks, annotations, and PDF
   objects contain no private governance text: no project path, temporary
   path, hash, byte/LF identity, PASS/BLOCKED token, gate or queue value,
   review/build history, permission ledger, invocation identifier, command
   log, reviewer/agent/model/tool identity, source or publication lock,
   submission/release instruction, or other private provenance.
6. The repaired candidate has exactly 26 physical pages, as expected from the
   immutable diagnostic history. The Abstract begins on page 1. The exact
   starting and ending page and position of the substantive
   Abstract-through-end-of-Conclusion body and the exact starting page and
   position of References are freshly inspected and recorded; References are
   excluded from the substantive body. The body must satisfy the target of
   26.5 pages, the preferred 24–28 band, and the hard 22–30 band under that
   boundary convention. The diagnostic expectation is Section 8 on page 24,
   Conclusion beginning and ending on page 26, and References beginning
   later on page 26, but the receipt must record the fresh observation. No
   appendix is permitted.
7. All 26 pages pass readability checks with no blank, corrupt, clipped, or
   table-overflow page.
8. Citation closure is exactly four citation commands in the bounded
   Introduction context and exactly these six distinct keys:
   BlancVanSanten2021, ShaoSun2025, Deserti2016, DangFavre2021,
   Rangarajan2002, and FujiokaKogawaLiShudo2023. The bibliography contains
   exactly those six entries and no seventh; every cited key is defined and
   every bibliography key is cited. The four permitted contexts are
   affine-triangular degree constructions, broader higher-dimensional degree
   growth, general spectral motivation, and neighboring symplectic or
   coupled-Hénon constructions. No citation is used as proof of a gradient,
   selector, cone, carry, leading form, visibility, matrix, cubic,
   multiplicity, boundary, coefficient, or threshold claim.
9. The accepted root-A main.pdf and root-B main.pdf are byte-identical.
   Before persistence, main_round0.pdf is made as a byte copy of that accepted
   main.pdf and is then proven byte-identical to main.pdf by both SHA-256 and
   direct byte comparison.

## Canonical JSON and success-only persistence

No success path may be created in paper/ until every acceptance condition
above has passed and both JSON candidates have passed the independent
canonical checks below. Staging is local to a fresh temporary root, never in
the project.

BUILD_METADATA_R0.json and BUILD_RECEIPT_R0.json must each be strict UTF-8
one-line canonical JSON:

- no BOM, CR, invalid UTF-8, duplicate key at any depth, nonfinite number, or
  trailing non-whitespace content;
- exactly one terminal LF and no other line break;
- compact separators, with no insignificant whitespace;
- object keys ordered recursively by increasing Unicode code point, including
  every key nested under checks and every further nested object;
- arrays retained in semantic order and numbers represented in one canonical
  finite form; and
- a self_identity object whose recursively ordered content is exactly
  bytes:null followed by sha256:null. No artifact may claim a circular
  non-null identity for itself.

The top-level status field in BUILD_METADATA_R0.json is exactly
BUILD_METADATA_R0_REPAIR. The top-level status field in
BUILD_RECEIPT_R0.json is exactly BUILD_R0_REPAIR_PASS.

Each JSON byte string must independently pass a strict Python parser and a
strict Node parser, or two genuinely independent equivalent parser
implementations. Each parser must detect duplicate keys at every depth,
reject nonfinite values and invalid text, recursively sort keys by Unicode
code point rather than native insertion or integer-key order, serialize with
compact separators, append exactly one LF, and reproduce the candidate bytes
exactly. The two parsed value trees must also agree. Native JSON.parse or
JSON.stringify alone is insufficient where it cannot detect duplicates or
guarantee the required recursive ordering. Parser names/versions, pass
results, and canonical round-trip SHA-256 values are recorded before
persistence.

Together, the two JSON artifacts must bind, without relying on an unrecorded
side ledger:

- the exact authorization-note identity and terminal; the historical
  issuance-provenance hashes, gate, and queue; both actual post-consumption
  root-ledger paths, SHA-256 values, byte/LF counts, and terminals; the exact
  build-open gate PAPER22_DETERMINISTIC_R0_REPAIR_BUILD_OPEN and queue
  R0_REPAIR_BUILD_AUTHORIZED; evidence that both ledgers bind the final
  authorization identity; and the one-shot invocation identifier;
- the source trio identities before and after in the project and both roots;
- the old blocker, repair receipt, and both fresh source-review paths,
  SHA-256 values, byte/LF counts, and terminals;
- both exact temporary-root paths, freshness and independence evidence,
  modes/ownership, initial inventories, the exact six-variable environment,
  command arrays, working directories, exits, and command-log identities;
- final per-root output identities, stability checks, cross-root byte
  comparisons, and the main.pdf/main_round0.pdf equality;
- the effective filesystem permissions and the complete granted and denied
  authority of this note; and
- every AUX/BBL/BLG/OUT/log, unresolved-marker, warning, underfull/overfull,
  PDF validity/feature, title/author/date, page/boundary, font, private-text,
  citation-context, bibliography, and JSON-parser check with observed counts
  and evidence.

In particular, the nested checks object is not exempt from canonicalization:
its keys and all nested evidence keys must already appear in increasing
Unicode code-point order in the persisted bytes. Canonicality is a byte-level
acceptance fact, not merely a claim stored inside that object.

Only after all checks pass may the invocation persist exactly these nine new
regular files into paper/ and no others:

1. BUILD_METADATA_R0.json
2. BUILD_RECEIPT_R0.json
3. main.aux
4. main.bbl
5. main.blg
6. main.log
7. main.out
8. main.pdf
9. main_round0.pdf

The six build outputs must be the accepted byte-identical final outputs from
one of the two roots; the receipts must say which root supplied the persisted
copies. Both PDF names must remain byte-identical. Persistence is
all-or-nothing, must not overwrite any pre-existing path, and must preserve
the already verified bytes. If a persistence operation fails, the invocation
must roll back only partial success files that it created so that none of the
nine remains.

On success, the project inventory is exactly 37 regular files, four child
directories, and zero symlinks. The 28 pre-build project files and the actual
post-consumption, build-open bytes of both root ledgers remain
content-identical to their build-invocation-start checkpoints. No repair
blocker exists. The two fresh temporary roots are retained privately and
unchanged after the final identity checkpoint for the separately authorized
independent review; no additional command may be run in them by this build
author.

## Failure rule

Any false, missing, ambiguous, or unrecorded precondition or acceptance
conjunct is failure. Failure persists none of the nine success files. The
only project path that a failed invocation may create is
notes/BUILD_R0_REPAIR_BLOCKER.md, and if created it must be a standalone
factual record ending with the exact final nonempty line
R0_REPAIR_BUILD_BLOCKED. The immutable notes/BUILD_R0_BLOCKER.md must never
be edited, replaced, or deleted. A partial success file is not a permissible
failure record.

Whether or not the optional new blocker is written, the one-shot authority is
consumed. The build author must report the failure identities and counts and
stop. No repair, source edit, second root pair, replacement invocation, or
self-review follows from this note.

## Required handoff and withheld authority

The build author must report and stop after the persistence decision. The
report must include the invocation and authorization identities, all bound
input identities and terminals, the historical issuance provenance, the
actual post-consumption build-open root-ledger identities and exact
gate/queue plus both ledgers' authorization bindings, pre/post project
inventories, exact fresh root paths and permissions, initial root
inventories, environment and command identities, both exit vectors, all
command-log and output SHA-256/byte counts, warning and box counts, closure
counts, PDF/page/body and reference boundaries,
title/date/security/font/image findings, citation and bibliography counts,
both canonical-JSON identities and parser results, the persisted nine-file
identities on success, or the sole blocker identity on failure. The build
author performs no self-review.

A successful R0 repair build requires a fresh independent R1 build review as
the next lifecycle check. This note makes that independent review eligible
after success but does not authorize the build author to conduct it and does
not itself open that review.

This authorization grants no source edit, revision window, R1 build or R1
build-review execution, release, finalization, Paper 23 work, publication,
submission, upload, transport, repository push, messaging, identity
disclosure, or any other external effect.

BUILD_AUTHORIZATION_R0_REPAIR
