# Paper 22 Independent Finalization-Stage Review

Date: 2026-08-24 UTC

Project: `papers/22-hamiltonian-cubic-spectral-collapse`

Public title: **Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian
Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number**

## 1. Reviewer role and disposition

This is the fresh replacement independent finalization-stage review required
after the bounded same-path recovery of the finalization governance pair. The
reviewer is distinct from the original governance author, the zero-write
failed reviewer, and the recovery author, and authored none of the frozen
`F45` inputs or recovered `G47` governance pair.

The review was read-only until every gate below passed. It did not invoke
TeX, BibTeX, `latexmk`, CAS, numerical or scientific execution, rendering,
network access, cleanup, release copying, manifest or receipt authoring, or
any external action. It did not alter root ledgers, source, bibliography,
build artifacts, PDFs, temporary evidence, or a later-stage path. Its sole
conditional write is this review.

## 2. Exact opening fences

The two live root ledgers matched the replacement-review opening state:

| Ledger | SHA-256 | Bytes | LF | Required state |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `00881cd1494725eb091c1bf2f175ef98c4b774755892f39946850a03722df719` | 42,894 | 657 | gate `PAPER22_INDEPENDENT_FINALIZATION_STAGE_REVIEW_OPEN`; Paper 22 queue `FINALIZATION_GOVERNANCE_RECOVERED_PENDING_FRESH_INDEPENDENT_REVIEW` |
| `BATCH_06_IDEA_REPORT.md` | `dd07e13dc5d969cc8cc22043a457ef7366887c370c1d2d46faa1e21fdeb9a185` | 53,988 | 1,041 | append-only through the same-path finalization-governance recovery addendum |

The recovered governance pair was exactly:

| Artifact | SHA-256 | Bytes | LF | Terminal/schema state |
|---|---|---:|---:|---|
| `notes/FINALIZATION_STAGE_SCOPE.md` | `09462316380cf1c958aaf06c6a1d0e3a93ba7fcb8060e177420fafff22de268f` | 27,385 | 447 | `FINALIZATION GOVERNANCE SCOPE AUTHOR STOP` |
| `experiments/finalization_lock.json` | `6df9730752823fce76571ff690aab3c6213038d80ae9ba6e94e4f3c7de3d3e33` | 102,689 | 1 | schema `paper22-finalization-lock-v1`; state/status `FINALIZATION_STAGE_LOCKED_PENDING_INDEPENDENT_FINALIZATION_REVIEW` |

The lock externally binds the recovered scope at the first identity above.
Its own safe path is recorded with null SHA-256 and byte count, one terminal
LF, and an explicit self-exclusion reason. No circular self-identity is
claimed.

## 3. Exact project-universe audit

A fresh no-follow traversal found exactly 47 regular files, the four child
directories `experiments`, `notes`, `paper`, and `refine-logs`, zero
symlinks, and zero other entry types. Safe project-relative paths were unique
and byte-lexicographically ordered where the lock requires ordering.

All 45 `F45` bindings were independently opened with no-follow semantics and
rehash-checked for SHA-256, byte count, and LF count. The recomputed framed
manifest was exactly SHA-256
`7d28756acc975090708d582130fb2f69ca4d07ac8b61e60ed906da67254173dc`,
4,719 bytes and 45 LF. The remaining two paths were exactly the recovered
scope and lock above. Thus recovered `G47` is exactly `F45` plus those two
same paths; recovery added no path and changed no `F45` byte.

The review, release candidate, release manifest, terminal receipt,
`paper/reviews`, and final-integrity review paths were all absent. No
unlisted project artifact existed.

## 4. Corrected chronology and recovery record

The recovered normative chronology is internally and externally consistent,
in this exact order:

1. `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, terminal
   `SOURCE_DESIGN_PASS`;
2. `experiments/source_lock.json`;
3. `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`, terminal
   `SOURCE_LOCK_PASS`;
4. `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`, terminal `PAPER_PLAN_PASS`;
5. `notes/PUBLICATION_STAGE_SCOPE.md`;
6. `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`, terminal
   `PUBLICATION_STAGE_PASS`;
7. `experiments/publication_lock.json`;
8. `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`, terminal
   `PUBLICATION_LOCK_PASS`.

In particular, `PAPER_PLAN_PASS` now correctly precedes publication scope.
The publication scope binds that completed plan review, and publication-stage
PASS is the predecessor of publication-lock authoring. The sole contradiction
reported by the failed reviewer is removed rather than waived.

The recovery record exactly preserves the superseded scope at SHA-256
`999b121be5cf83c6f19d2c61fd595f7a3314cc8d3f834861a516638418471b0f`,
23,825 bytes and 386 LF, and superseded lock at SHA-256
`97fb27d9df15af822159484b03e4a05d8f30e145f6b0b7226594672714a547b0`,
99,054 bytes and one LF. It records the failed review's exact
`WRITE_NOTHING` disposition, zero project writes, absent review path, one
sole defect, and no downstream authority.

It also records the exact recovery-start ledgers: `BATCH_06_STATUS.md` at
SHA-256
`7831ecdbd66ebba735f321aa43e051c0fd321936ef0ccf85782be60e381f40e6`,
41,433 bytes and 635 LF, and `BATCH_06_IDEA_REPORT.md` at SHA-256
`0907031ca8c6e026dc729fa60bf1c5f7b498317558756bc2cf282c85689a4b1b`,
52,317 bytes and 1,013 LF. Those are explicitly recovery-opening provenance,
not false requirements on later live ledgers.

The recovery fields affirm, and the independent hashes confirm, no drift in
`F45`, `E216`, science or proof, source or bibliography, build or PDF,
roles or stage counts, cleanup permission, or external-effect permission.

## 5. Strict-canonical lock and JSON audit

A duplicate-aware Python decoder rejected duplicate keys at every object
depth and nonfinite constants, decoded UTF-8 strictly, and reproduced the
lock byte for byte using recursive Unicode code-point key order, compact
separators, no insignificant whitespace, and exactly one terminal LF.

A genuinely separate handwritten Node parser performed tokenization, string
and number decoding, duplicate detection, trailing-content rejection, and
recursive encoding without `JSON.parse`. Its encoder independently sorted
object keys by Unicode code point and reproduced the same 102,689-byte lock
exactly.

For unambiguous counting, the recovered document contains 394 JSON object
nodes and 3,730 object-member values (the sum of key/value members over those
objects), plus 70 array nodes, 555 array values, and 3,822 scalar values.
These explicitly framed quantities are different notions and were not
conflated with file counts or binding counts.

Each implementation rejected ten adversarial cases: a duplicate key, `NaN`,
infinity, trailing content, a UTF-8 BOM, CRLF, a second terminal LF,
insignificant leading object whitespace, noncanonical key order, and trailing
space before the LF. All eight live project JSON artifacts also passed the
duplicate-aware Python strict recursive-canonical byte round trip. Required
schemas, statuses, and null self-exclusions matched their frozen records.

## 6. Exact temporary-evidence audit

A new no-follow `/tmp` scan found exactly the ten locked top-level
`paper22*` objects: eight ordinary directories and two ordinary files. Every
locked node was revalidated for literal and relative path, type, permission
mode, numeric UID/GID, device, inode, link count, stat size, and, for regular
files, SHA-256, byte count, and LF count. Directory descriptors and file
descriptors were opened with no-follow semantics; no evidence was modified.

The result was exactly `E216`: 216 nodes comprising 201 regular files and 15
directories, zero symlinks, zero special entries, and 72,033,301 regular-file
bytes. All 201 regular files had unique device/inode pairs and link count one.
The independently regenerated 216-record framing was SHA-256
`fb727a475a90e52857700b90b914b448954c8e0aba821b016d1d26ba337e9b39`,
34,161 bytes and 216 LF.

All 16 must-remain-absent assertions were absent, including the removed R2
review scratch, four removed R1 staging/render descendants, nine literal
legacy templates, and two literal future terminal-root templates. Literal
`XXXXXX` names were treated only as absence assertions, never as objects or
cleanup targets.

## 7. Authoritative source and build lineage

All 23 ordered authoritative-chain records were rehashed against live `F45`
bytes. Every Markdown terminal and every JSON schema/status matched. The
historical initial build blocker still ends exactly `R0_BLOCKED` and remains
incident evidence, not a pass. The bounded repair ledger and two independent
repaired-source reviews remain the only authority for the repaired source.

The frozen source trio remains:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

The current, round-zero, and round-one PDFs remain byte-identical at SHA-256
`5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`,
471,647 bytes and 2,649 LF. The accepted four command-log identities and six
output identities match the retained R0-repair and R1 roots and the current
project outputs. This review relies on the frozen independent build/PDF
evidence and rehashes; it correctly did not build or render at this stage.

The frozen theorem and anti-claim contract, four citation commands, six
unique bibliography keys, contextual-only citation role, visible
`Anonymous` identity, PDF metadata/security expectations, and prohibition on
scientific or provenance leakage are unchanged by exact source and PDF
identity.

## 8. Downstream stage and permission audit

The only monotone sequence is exact:

- `G47` to `P48`: add only this review;
- `P48` to `R50`: add only the raw byte-copy release candidate and strict
  final-release manifest;
- `R50` to `Q51`: add only the strict terminal rebuild receipt;
- `Q51` to `T52`: only after every terminal audit and bounded cleanup passes,
  create `paper/reviews` and the final-integrity review.

The corresponding file/directory counts are 47/4, 48/4, 50/4, 51/4, and
52/5. The five roles are distinct and temporally fenced; no role may review
or repair its own output.

Binding-count language is consistent: completed `R50` has 50 files, while
its manifest's own null self-exclusion leaves 49 completed non-self file
bindings; the later terminal receipt binds all 50 completed `R50` input
files and separately excludes its own `Q51` identity. These are project-file
binding counts, not JSON object-node or document-wording counts.

The candidate contract requires an exclusive ordinary raw byte copy of
`paper/main_round1.pdf`, forbids a hard link and every transformation, and
preserves the frozen PDF identity. The terminal build contract requires two
independently created root-owned mode-0700 roots under `/tmp`, a cleared
environment containing exactly `PATH=/usr/bin:/bin`,
`SOURCE_DATE_EPOCH=1787529600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
`LC_ALL=C`, and `LANG=C`, followed exactly once in each root by
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex` with the frozen arguments and
exit vector `0,0,0,0`. It requires terminal A/B equality to every accepted
command log and output and the stated six-way PDF equality. Retry, cleanup
build, fifth pass, engine substitution, shell escape, project overwrite, and
external effect remain forbidden.

Cleanup remains reserved exclusively to the sole terminal-integrity
reviewer, only after every `Q51`, live-root, evidence, source, PDF, visual,
security, and governance audit passes. Its possible targets are exactly the
ten locked legacy top-level objects plus the two literal roots later recorded
by the terminal receipt. It must use the bounded no-follow per-entry unlink
and deepest-first `rmdir` method. Recursive deletion, globs, discovery-based
deletion, partial cleanup, template deletion, and any project deletion are
forbidden.

Submission, upload, public hosting, repository push, network transport,
external messaging, identity disclosure, and all other external effects are
false. Before the final integrity review the effect is `NO_RELEASE_EFFECT`;
the only possible terminal effect afterward is
`LOCAL_ANONYMOUS_RELEASE_ONLY`.

## 9. Verdict and exact effect

No blocker or cosmetic governance defect remains. Recovered `G47`, both live
root ledgers, all 216 live evidence nodes, all 16 absences, the authoritative
chain, canonical contracts, stage arithmetic, role fences, raw-copy and
terminal-build requirements, cleanup bounds, and external-effect denial all
pass.

This file is the sole project write and advances the project to exactly
`P48`: 48 regular files, four child directories, zero symlinks, and zero
other entry types. Its effect is only to make the distinct release-candidate
author role eligible after the parent lifecycle ledger transition. It does
not itself release, build, clean, unlock Paper 23, or authorize any external
effect.

FINALIZATION_STAGE_PASS
