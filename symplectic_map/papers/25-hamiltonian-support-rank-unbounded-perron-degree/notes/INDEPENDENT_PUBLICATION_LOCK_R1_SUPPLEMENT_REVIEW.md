# Paper 25 fresh independent R1 publication-lock supplement review

## Verdict, independence, and authority boundary

This fresh review finds zero blocker, major, minor, or ambiguity in the R1
publication-lock supplement.  The supplement is a strict-canonical,
self-excluding overlay that binds the immutable base lock, the repaired source
trio, the complete pre-supplement L24 universe, the R0 failure evidence, and
exactly seven authorized base-contract deltas.  Independent replay produces the
declared effective-contract digest, and the recursively minimal difference set
contains exactly the seven allowed JSON Pointers.

The reviewer is distinct from the supplement author, the R1 source authors and
source reviewer, the R0 builder and evidence reviewer, and all earlier Paper 25
roles.  The current root ledgers explicitly opened only this review.  This
review did not inspect a build root, execute TeX or BibTeX, use a network, edit
an existing byte, act on Paper 26, or perform a release or repository-facing
operation.  Its only write is this review node, made after all checks below had
passed.

The verdict concerns the supplement and the effective contract.  It is not a
claim about a future PDF, page count, warning stream, resource state, or build
result.  A successful review does not authorize root access or a build.  The
parent must consume the externally measured supplement and review identities
and open a later identity-bound dual-build gate before any first root check.

## Complete input consumption and current gate

Both current ledgers and all twenty-five L25 project files were read through
physical EOF before the review write.  Their current ledger identities were:

| input | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `9a38f4597dde21dcea39ca2bd33aae67381822726a061af709801ea9cb30540c` | 242,064 | 3,452 |
| `BATCH_06_IDEA_REPORT.md` | `00ab7befc1f5f72f6f36cf9bb7a00c45f1949b2b1a842ceebf098e988e70a785` | 412,190 | 7,669 |

Each was regular UTF-8 text with one link and a terminal LF.  Each contained
the current supplement-review-open gate exactly once at review start.  The
supplement's `root_controls` identities are earlier append-only ledger prefixes,
not assertions that the current ledgers stopped there.  Hashing those exact
prefix lengths reproduced both stored predecessor identities, LF counts, and
the one-count author-open gate.  The four bound R0 evidence byte slices also
matched their exact offsets, lengths, LF counts, start/end markers, and digests.

The complete L25 read set and external identities were:

| project-relative path | SHA-256 | bytes / LF |
|---|---|---:|
| `experiments/EXPERIMENT_PLAN.md` | `ab2291ddf6bff7aae632e2b261c58895a9367dc110f15d2c22920cec685a7cc9` | 11,033 / 359 |
| `experiments/EXPERIMENT_TRACKER.md` | `9527dada16fa76c0434e94de028a1635fcab3942cf9bee5a38d5cb577f1a89fb` | 5,405 / 92 |
| `experiments/publication_lock.json` | `414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081` | 69,835 / 1 |
| `experiments/publication_lock_r1_supplement.json` | `d88fa75747247e5fe9553a0a71d05fddeccb7aad0e2fc3ed77bc1ec3401f1728` | 32,374 / 1 |
| `experiments/source_lock.json` | `5aa32ca98f7725b9f627129056250d4c21de0b228b66c8b56644752e5512c5ab` | 34,422 / 1 |
| `notes/CITATION_VERIFICATION.md` | `9538e423e5ba9fedf9e9cac3fd8060800d683a935ffba48b8ada69b3b51697af` | 9,001 / 126 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `abb0b13c83fc32c5dbbecd0de6ce18c6a154177f41955deddcfba3bc308b6e7d` | 8,618 / 87 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `2b55e0068348b377d27b982aea3940211a53194e5d41d26e6712eb1053eebbee` | 26,764 / 506 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_NOTATION_REPAIR_REVIEW.md` | `a52ec699f2f243c8f45aa666c1c4cf09704541329fe17b6fa3a51d160c624d49` | 21,610 / 203 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `599640710e5064226c4c390ad78265d100ce0fb8c01d8f9f0eaf6d527f9fec44` | 29,758 / 500 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `413886a5c5c75ce82f2dd3005571ab70241f3f6e9d0bd4102972954260cabe67` | 34,357 / 734 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `feaeb0b5b6c3c6ecb006349e529fcc92355aaea60a969851e20d86312e6e1e5b` | 26,953 / 793 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `e18007da043a38d6099a0d99a55c83d4f590dba79bfb0fe102fab4b118a6e98b` | 25,132 / 515 |
| `notes/NOVELTY_ASSESSMENT.md` | `ecc57ca4ba68375270b04d5be2eff9884d31f81d3fa1acc36d0bc5cd49f2683d` | 8,496 / 136 |
| `notes/PROOF_PACKAGE.md` | `0b957e5519dff5460d819de335782b9ac2b669f42089e0699d03cf0349f5ab93` | 29,750 / 1,240 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `9a60c44aaa308aefce7d0e4f8ea877b381f37386ee7fe88447850e33aa76fca0` | 43,878 / 800 |
| `notes/RESEARCH_QUESTION.md` | `8641c4160fe74ee3925bc2803c90ef139261f48c844c78856b53989e9a8d7098` | 5,839 / 139 |
| `paper/PAPER_PLAN.md` | `ebcd925470e25d53f85bbce861aee68bbefcf4702128e2338969887bb2039be4` | 54,112 / 1,044 |
| `paper/PAPER_PLAN_R1.md` | `422c4e1d4a7810cc6013e1be6ad611ac7c3f4d6d9b70024d389dfc7a2a87c747` | 54,340 / 1,046 |
| `paper/main.tex` | `e5b2654a71104bfd2bdca52d05a6e4aa95d5f54cae541ab7dd1532f7323ccd2d` | 61,156 / 1,114 |
| `paper/math_commands.tex` | `c748e0cde8aadef85c5de9e1fa20efb7770d07fb3fde58dfe0f4fe738720edf0` | 393 / 11 |
| `paper/references.bib` | `159acd5633b19f3f91c203d4f85375cfe5ddaaee6337fd5297c673ac1b9ad99d` | 3,450 / 118 |
| `refine-logs/FINAL_PROPOSAL.md` | `13bf8d9bc21a1841b24b9d9308558d6807cba5e218685a03795dfd65d75d4f6d` | 7,426 / 220 |
| `refine-logs/INITIAL_PROPOSAL.md` | `06caba1425c68ac387d3ae618bc1ce1edea02cbf4db547adfb3dea136070f6ba` | 5,788 / 126 |
| `refine-logs/REVIEW_SUMMARY.md` | `69408011fd514f8a5ab54fe81253b960e527c58c0da46090f346e076de931fb7` | 6,190 / 122 |

The L25 universe was exactly twenty-five regular one-link files under the four
declared directories, with no symlink or other node.  It totaled 616,080 bytes
and 10,034 LF.  Removing only the self-excluded supplement recovered the exact
twenty-four-file L24 universe at 583,706 bytes and 10,033 LF.

## Strict canonical JSON and self-exclusion

The supplement was measured externally as SHA-256
`d88fa75747247e5fe9553a0a71d05fddeccb7aad0e2fc3ed77bc1ec3401f1728`,
32,374 bytes, and one LF.  It is mode 0644, link count one, regular UTF-8, one
physical JSON line followed by exactly one terminal LF, with no BOM, CR, or
NUL.  A duplicate-rejecting parser rejected floating and nonfinite numeric
tokens.  Recursive Unicode-code-point key sorting, UTF-8 output with
`ensure_ascii=false`, and compact separators reproduced every byte including
the terminal LF.  No duplicate key, noncanonical key order, future review
identity, placeholder sentinel, or copy of the supplement's own digest occurs.

The same strict round trip independently reproduced the immutable base lock at
SHA-256
`414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081`,
69,835 bytes and one LF, under schema `paper25.publication_lock.v1`.  A second
implementation in Node independently reproduced the exact supplement and base
bytes, the effective-contract digest, and the L24 frame digest.  This separates
duplicate-aware lexical adjudication from a second parser/serializer and
replay implementation.

Self-exclusion is coherent.  The supplement binds its exact predecessor but
does not assign its own digest or octet count, and it assigns no unknown future
review identity.  The external supplement identity above is therefore a review
measurement, not a self-referential field.

## Complete L24 manifest and frame reconstruction

Every one of the twenty-four manifest records was checked against the actual
regular file for path, SHA-256, byte count, LF count, mode 0644, link count one,
terminal LF, strict UTF-8, and absence of BOM, CR, and NUL.  Paths are in
ascending bytewise UTF-8 order.  Their path bytes sum to 745 and their content
bytes sum to 583,706.

I independently constructed the frame as the ASCII header
`paper25-publication-r1-presupplement-l24-v1`, one NUL, then for each ordered
record `uint64_be(path length)`, exact UTF-8 path, `uint64_be(content length)`,
and exact content.  The header including NUL is 44 bytes.  The resulting frame
is 584,879 bytes and has SHA-256
`6e6a520ffe60db29e47cdc333f6418f5f9780d88f7436eb655582204bbc3d8ec`.
Both Python and Node reconstructions agreed.  Adding only the supplement gives
the exact L25 set; the future review node was absent at review start.

## Base, evidence, and repaired-source bindings

The base publication-lock review is exactly SHA-256
`599640710e5064226c4c390ad78265d100ce0fb8c01d8f9f0eaf6d527f9fec44`,
29,758 bytes / 500 LF, with its unique base-lock PASS at physical EOF.  The
source lock remains
`5aa32ca98f7725b9f627129056250d4c21de0b228b66c8b56644752e5512c5ab`.
The earlier final source-review precedent remains
`a52ec699f2f243c8f45aa666c1c4cf09704541329fe17b6fa3a51d160c624d49`,
21,610 bytes / 203 LF, with its unique terminal at physical EOF.

The actual repaired source trio exactly matches the supplement:

| staged source | SHA-256 | bytes / LF |
|---|---|---:|
| `paper/main.tex` | `e5b2654a71104bfd2bdca52d05a6e4aa95d5f54cae541ab7dd1532f7323ccd2d` | 61,156 / 1,114 |
| `paper/math_commands.tex` | `c748e0cde8aadef85c5de9e1fa20efb7770d07fb3fde58dfe0f4fe738720edf0` | 393 / 11 |
| `paper/references.bib` | `159acd5633b19f3f91c203d4f85375cfe5ddaaee6337fd5297c673ac1b9ad99d` | 3,450 / 118 |

An independent static census of `main.tex` reproduced 26 citation commands,
32 citation mentions, twelve distinct citation keys, nine unique labels,
twelve closed reference uses, eight sections, thirty-nine subsections, one
table, zero figures or appendices, and exactly three mathematical headings
protected by `texorpdfstring`.  The citation-key set equals the twelve unique
bibliography entries.  The protected plain bookmark fallbacks are exactly
`large-b`, `q1`, and `d`.  The two current ledgers contain the repaired-source
zero-finding verdict twice in aggregate, as bound.

The four R0 evidence slices were verified without visiting their retained
roots.  Their exact status/idea offsets, byte counts, LF counts, digests, and
exclusive end markers reproduce the builder stop and the later evidence
correction.  These ledger bytes justify the R1 changes but grant no permission
to revisit the evidence roots.

## Independent seven-operation replay

The overlay declares seven operations, seven target pointers, and the same
ordered target list.  The operations are six `replace` operations followed by
one `add`; every reason is nonempty; all targets are distinct.  RFC 6901 token
decoding was implemented independently with rejection of malformed tilde
escapes.  Each replacement target existed in the deep-copied base tree, and the
added target did not.

| order | operation and target | adjudication |
|---:|---|---|
| 1 | replace `/build_contract/clean_dual_build/build_A_root` | exact new R1 A string |
| 2 | replace `/build_contract/clean_dual_build/build_B_root` | exact new R1 B string |
| 3 | replace `/build_contract/clean_dual_build/freshness_rule` | first access is gate-bound ENOENT/symlink adjudication |
| 4 | replace `/build_contract/clean_dual_build/historical_root_firewall` | Paper 23/24 prohibitions retained and both R0 evidence roots added permanently |
| 5 | replace `/build_contract/inspection/cross_build_command` | exact direct-PDF comparison under the two new roots |
| 6 | replace `/build_contract/failure_and_warning_policy/earlier_pass_only_allowlist` | event-exact pass-one rules, rerun-only pass two, zero-warning pass three |
| 7 | add `/build_contract/failure_and_warning_policy/hard_failure_pattern_exceptions` | one first-pass complete-event exception only |

Canonical compact serialization of the resulting effective base object is
75,264 bytes and has SHA-256
`8c92a2469a415736de6658ebed4710a19b8f59cedfa1c4dbd60f9a3f9ca15aaa`.
The Node replay returned the same value.  A recursive comparison that stops at
an authorized target found precisely these seven minimal pointers and no
eighth difference.  Recursive object traversal naturally visits the two
failure-policy targets before the inspection target, whereas the semantic
operation array places the inspection target fifth.  The audit therefore
checks exact operation-array order and exact recursive-difference set
separately, as required by the overlay.

The canonical SHA-256 values of all explicitly inherited base subcontracts
also reproduce the supplement:

| inherited base value | canonical SHA-256 |
|---|---|
| allowed root filenames | `d0dac127a6ed18ecfe9cb1cfcb644fe4ad22bd925d8e7e0576e7a378349db55a` |
| execution environment | `9bc9f895741e8bbd50f3d5c9b8ebca982a627874c11a87740c138a4d3bb16d86` |
| per-build inspection commands | `8f88615ed8d1c876fef9a0f9e442df01b18971d153582a5fa70ca01b4a8b338c` |
| four-pass order and commands | `d21eb4297853423daf3fa35a5f66b02063f48363cd8b4e016228d32393402b72` |
| source and input audit | `d6e91f8a9a0230a8d1bfffa6d51e7854399ebda410f18c1ba684b7f73d672967` |
| system TeX resources | `b902e5d3355a329cb65d630e1f1142d01abcd25f924f05b4ac3681c54e6a0a51` |
| toolchain | `a76d23d183dc7eae936c533d159bad51f6d1bbe3689b753af85624328eddd959` |

## Root and command semantics

The two new R1 root paths were treated only as JSON string values.  I performed
no existence check, listing, stat, lstat, glob, hash, read, or other filesystem
operation on either string.  The supplement requires the later parent gate
before the first direct exact-path existence-and-symlink check.  ENOENT is
required independently for both; a live or broken symlink counts as presence
and forces a zero-write build stop.  Only after two valid first checks may the
later builder create each exact root once as an empty mode-0700 directory.

The two retained R0 root strings occur only in the permanent firewall object.
That object forbids access, list, stat, lstat, glob, touch, read, hash, copy,
continue, retry, rename, clean, delete, and reuse.  All exact Paper 23 and Paper
24 strings remain present, the rule continues to cover unnamed Paper 24
temporary roots, and the firewall is explicitly unconditional.  I likewise
performed no filesystem operation on any historical or retained string.

The sole root-qualified command in the effective build contract is the exact
absolute `/usr/bin/cmp -s` comparison of the two new roots' direct `main.pdf`
files.  The four inherited pass commands contain no root path and use relative
source/output names; the inherited working-directory rule makes the applicable
new root the cwd.  The pass sequence remains pdfLaTeX 1, BibTeX, pdfLaTeX 2,
pdfLaTeX 3 under the exact `env -i` map, with HOME and CODEX_HOME unset,
shell escape disabled, and network disabled.  There is no wrapper, retry,
extra pass, postprocessor, or PDF rewrite.

## Warning-event policy

The new event policy is source-closed and complete-event based.  Normalization
collapses only nonempty runs of the six listed ASCII whitespace bytes to one
space and trims boundary spaces; it performs no case fold or other transform.
Substring-wide suppression is false, and every unclassified event is a hard
failure.

Pass one requires exactly one complete `No file main.aux.` event and exactly
one complete `No file main.bbl.` event.  Undefined-citation events must fully
match the twelve source keys, total between zero and 32, and obey per-key
ceilings summing to 32.  Undefined-reference events must fully match the eight
source labels, total between zero and twelve, and obey per-label ceilings
summing to twelve.  Each of the two enumerated rerun events may occur zero or
once.  Boxes, PDF-string warnings, missing characters, duplicate definitions,
unclassified destinations or warnings, errors, and fatal events remain
forbidden even on pass one.

The `references.1` fallback is permitted exactly once only on pdfLaTeX pass
one.  It must be the complete normalized event
`pdfTeX warning (dest): name{references.1} has been referenced but does not
exist, replaced by a fixed one`.  Its policy pointer resolves to the sole added
exception, its count is one, its scope is one complete diagnostic event, and
its count must be zero on passes two and three.  The exception is evaluated
only after exact complete-event matching and cannot suppress the inherited
`referenced but does not exist` hard-failure substring globally.

Pass two permits only the two enumerated rerun events, each at most once, and
requires zero missing aux/bbl, undefined citations/references, destinations,
boxes, PDF-string or other warnings, errors, and fatal events.  Pass three has
an empty allowlist and requires zero warnings, reruns, destinations, boxes,
missing characters, duplicate-definition diagnostics, errors, and fatal
events.  The inherited overfull- and underfull-box hard failures and final-pass
warning rule remain intact.  BibTeX's zero-error/zero-warning and exact-key
requirements are unchanged.

## Inherited publication contract

Nothing in the seven deltas weakens the page or direct-PDF contract.  The
effective object still requires exactly twenty-six nonempty content pages from
Abstract through Conclusion, Conclusion on physical page 26, the first
standalone References heading on physical page 27, no earlier standalone
References heading, and total PDF length at least 27 pages.  The source
boundary remains the sole clearpage and bibliography insertion.

The two final PDFs must have identical SHA-256 values and compare equal
byte-for-byte.  All frozen inspection outputs must also agree.  `main.pdf`
remains the direct third-pdfLaTeX result; Ghostscript is inspection-only and no
normalizer, linearizer, optimizer, metadata editor, or timestamp fixer is
allowed.

The complete environment, pass commands, allowed root inventory, source and
FLS/BibTeX input policy, direct system TeX resources, tool and fitz identities,
metadata/date/ID suppression, title and anonymous-author rules, font and text
extraction checks, links and outline rules, source roles, and public firewall
are inherited without change.  The later builder must stage exactly the three
repaired source byte strings and no other project file.

## Hostile-test matrix

All hostile cases were constructed only in memory and were rejected:

| hostile mutation | required rejection |
|---|---|
| remove one operation | declared/actual delta count and target sequence fail |
| duplicate an operation | count and uniqueness fail |
| append an eighth operation | seven-delta contract fails even if metadata is also altered |
| swap two operations | exact semantic operation order fails |
| change an operation to an unknown verb | allowed verb sequence fails |
| delete a replacement target from a base copy | missing-replace-target failure |
| precreate the add target in a base copy | present-add-target failure |
| alter the bound base title | base canonical identity fails |
| alter one repaired source byte virtually | repaired-source digest fails |
| alter one L24 content byte virtually | manifest digest and frame fail |
| alter a new-root value | effective canonical digest fails |
| enable substring-wide suppression | effective digest and semantic policy fail |
| change a warning-pass label | effective digest and ordered-pass semantics fail |
| change a required event count | effective digest and exact-count semantics fail |
| enable case folding | effective digest and normalization semantics fail |
| insert a future identity placeholder | no-placeholder/future-identity rule fails |
| insert the supplement's digest into itself | self-exclusion rule fails |
| supply a duplicate JSON key | strict parser rejects it |
| serialize keys out of canonical order | byte round trip fails |
| supply a floating numeric token | allowed-value-type rule fails |

Thus missing, duplicate, extra, reordered, conflicting, and semantically
broadened overlays cannot be mistaken for this supplement.  In particular,
the exact effective digest alone rejects value drift, while independent schema,
target-conflict, ordering, event-scope, manifest, and self-exclusion checks
identify why the hostile object is invalid.

## Read-only diagnostic disclosure

The first independent Python run made one overly strict comparison: it required
the recursively sorted difference traversal to equal the semantic operation
order.  It stopped read-only after reporting the same seven pointers in a
different order, because object traversal visits
`failure_and_warning_policy` before `inspection`.  No file or external state
changed.  The corrected audit separately requires exact operation-array order
and exact recursive-difference set, then completed all core and twenty hostile
checks.  The independent Node replay corroborated the corrected result.  This
was a reviewer-script assertion error, not a supplement finding.

## Lifecycle, permissions, and finding ledger

The future transition is coherent: L25 may gain exactly one regular file at
this review path, yielding L26 without changing any existing byte or directory.
The review node is not an eighth overlay delta.  Its identity is deliberately
not predicted inside the supplement or this self-referential review; it must be
measured after creation and frozen by the parent together with the already
external supplement identity.

The supplement's author-stop permissions are all false and correctly describe
the snapshot before parent consumption.  The current ledgers, not an internal
self-open, authorized this review.  This PASS still opens no root access,
command execution, build, PDF finalization, archive, release, upload,
submission, repository mutation, Paper 26 action, or external effect.

Final finding counts are: blocker 0, major 0, minor 0, ambiguity 0.  The review
performed no compilation, no network request, no build-root filesystem
operation, and no measurement of an unbuilt future result.

PUBLICATION_LOCK_R1_SUPPLEMENT_PASS
