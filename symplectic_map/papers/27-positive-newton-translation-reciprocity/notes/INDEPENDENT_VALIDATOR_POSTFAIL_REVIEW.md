# Independent static review of the Paper 27 post-failure validator

## 1. Authority, exact targets, and separation

This is the sole mechanical aggregate authorized by
`B07-E0290-P27-POSTFAIL-VALIDATOR-DUAL-STATIC-REVIEW-PASS-CONSUMPTION-AND-AGGREGATE-AUTHORIZATION`.
The aggregate-path no-follow preflight returned absent.  The E0290 authority
ledger then had 1,471,059 bytes, 17,440 LF, mode 0644, link one, SHA-256
`9ade0aaefc47d19b142fa97d5ccefff52db2c40f3785218fd0d704812320419f`,
ending in
`BATCH07_P27_POSTFAIL_VALIDATOR_AGGREGATE_ARTIFACT_AUTHORIZED`.

Both required reviewers independently bound the E0289 opening ledger at
1,465,196 bytes, 17,381 LF, mode 0644, link one, SHA-256
`fb7b55c393009f00985b2c48d5400821c05d277143e067efebc14c375931364a`,
ending in
`BATCH07_P27_POSTFAIL_VALIDATOR_DUAL_ZERO_WRITE_STATIC_REVIEW_AUTHORIZED`.
Their exact reviewed files were:

| Artifact | Bytes | LF | Mode | nlink | SHA-256 | Terminal |
|---|---:|---:|---:|---:|---|---|
| `notes/BUILD_VALIDATOR_POSTFAIL.py` | 398,307 | 9,366 | 0644 | 1 | `6103a9df0c3d3fec652b9b39e0407b6a35eb369a7950d1b1724c8918fbe57693` | `# BATCH07_P27_BUILD_VALIDATOR_POSTFAIL_AUTHOR_STOP` |
| `notes/VALIDATOR_LOCK_POSTFAIL.md` | 63,861 | 1,168 | 0644 | 1 | `72d3bf2175c983f91b2cbe39c05271638bbcc23409dd7ed42a0acc6133501d63` | `BATCH07_P27_VALIDATOR_LOCK_POSTFAIL_AUTHOR_STOP` |

Both are regular strict UTF-8/LF files with no BOM, CR, or NUL and exactly
one terminal LF.  Source and lock terminals are each unique standalone final
lines.

Reviewer V1 and Reviewer V2 worked from separated contexts and did not read
one another's report.  The additional parser-matrix auditor was also
separated.  All three were zero-write and did not import, compile, AST-parse,
byte-compile, or execute the validator; invoke a compiler, BibTeX, or PDF
tool; or probe, list, stat, or read any Paper 27 `build/*` entity.  This
aggregate author records their substantive reports without adding a review
conclusion.

## 2. Reviewer V1 report

### 2.1 Identities, controls, and exact delta

V1 reproduced the status, source, lock, encoding, and terminal identities
above at both review boundaries.  It also reproduced the immutable
predecessor identities:

- `BUILD_VALIDATOR_SUCCESSOR.py`: 398,248 bytes, 9,360 LF, SHA-256
  `27c8f1e6535602f3cdc734eb8bf89ad28889493532d9628c31d9d95e78faffc1`;
- `VALIDATOR_LOCK_SUCCESSOR.md`: 57,684 bytes, 1,061 LF, SHA-256
  `c770bdba165b60953253c50b0050537b00ea2c4bbd7322140cb372f319f37d65`.

The five physical runtime controls exactly match the source and lock:

| Control | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| corrected post-failure profile | 53,878 | 963 | `f4829e21e4626b372a05e646f34d29f0ea306b653d23d6dd924d1fc54161687e` |
| inherited dependency lock | 30,145 | 215 | `66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17` |
| inherited dependency review | 12,687 | 231 | `b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35` |
| aggregate post-failure profile review | 13,492 | 248 | `b1bbdf96dc68ae1ee4e6ce984616c106931c5f2d462117808f8747f6496d887b` |
| inherited static-source review | 31,760 | 704 | `7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae` |

The source trio likewise matches its frozen 55,063/1,681, 601/17, and
6,610/217 identities and three exact digests.

The complete predecessor/new source diff has exactly twelve hunks, old side
41 changed lines, new side 47 changed lines, +59 bytes and +6 LF.  V1
classified every hunk as authorized:

1. deterministic post-failure docstring;
2. EVIDENCE/ROOT0/ROOT1, source/copy/lock, terminals, profile and profile
   review paths;
3. the two new profile control tuples;
4. final and both ABSENT evidence exact sets;
5. evidence validator cap basename;
6. evidence validator mode basename;
7. the six symbolic total name-dispatch structures;
8. final evidence read/cap/cache/report;
9. final evidence census/rebind;
10. terminal evidence rebind;
11. ultimate evidence rebind; and
12. final source terminal.

No handler, I/O operation, security predicate, failure tag, or seventh parser
grammar changed.

### 2.2 Namespace, basename, identity, and structure censuses

The new source has zero active old build namespace, validator/source/lock,
profile/profile-review, or author-terminal token.  The inherited dependency
lock/review and static-source review names each remain once intentionally.
`BUILD_VALIDATOR_POSTFAIL.py` occurs seventeen times and covers the exact
source/copy constants, three evidence sets, cap/mode functions, final
read/cap/cache/row/census/rebind, terminal rebind, and ultimate rebind.
The lock's only predecessor validator source and lock tokens occur in its
explicit immutable E0282 history.  The external launcher argv0 deliberately
retains `batch07-p27-successor-liveness-fd-scrub-launcher` and is not the
validator child argv0.

The one-way machine frame is exactly BEGIN, six ordered fields, END.  Its
bytes, LF, mode, link count, digest, and terminal equal the physical source.
The source does not hard-code its own or the lock/review digest, so there is
no identity cycle.

Pure sorted `basename<LF>` recomputation gives exactly:

| Frame | Names | Bytes | SHA-256 |
|---|---:|---:|---|
| final evidence root | 16 | 189 | `9639e752796288d63d4c5758974f40e7cdc959d5667cd9970e2722c8f5d97a98` |
| root0 ABSENT | 8 | 103 | `57929c3873fcfbda205572e06aa834199d37707a06aee2df430a09bcb78ed766` |
| root1 ABSENT | 12 | 142 | `6db034e938d75bd8cb26c513f875715786b78c62684d1c55a8939aa7e4caa2bb` |

`MODE_ARITY`, `MODE_HANDLERS`, and `VALIDATOR_RESULT_FIELDS` have the same 15
keys.  The frozen comprehensions expand to 74 unique argv rows.  The result
table has 90 ordered field occurrences and 52 distinct names: 29 decimal,
six symbolic, one warning-hex, and sixteen SHA-bearing names.  The latter are
one recorder structure, one mode-sensitive manifest name, and fourteen
generic-only names.  Each symbolic branch is total exactly once and each old
invalid-only form has zero occurrences.

### 2.3 Positive vectors and negative counterexamples

V1 expanded every lock `H` into 64 lowercase zero digits, `R` into the exact
mirrored R023/R043/R053 list, and `M` into the exact mirrored
R009/R024/R033/R044/R054 list.  All fifteen frames are printable ASCII,
single-LF, exact `PASS MODE` lines whose field counts, names, order, and values
pass their unique branches.  Both r0/r1 values, all eight checkpoint keys, and
all sixteen frozen IDs were checked.

V1 found no counterexample in the required negatives:

- r2 root/stage, R020 checkpoint/ID, 86/86 dependencies, and shortened
  disposition reach `_ROOT`, `_STAGE`, `_CHECKPOINT`, `_ID`,
  `_DEPENDENCIES`, and `_DISPOSITION` respectively;
- noncanonical decimal and generic digest widths/case reach exact decimal/hash
  tags;
- warning hex admits only `-` or nonempty even lowercase hex;
- recorder and CROSS manifest lists reject missing/reordered IDs, unequal
  mirrors, wrong count, and single digests;
- missing/extra/duplicate/reordered/empty fields, wrong prefix/mode, control or
  high bytes, and missing/extra LF fail at framing/prefix/position gates; and
- a grammar-valid caller expected-subset mismatch reaches the exact
  `EXPECTED_field` tag.

Because the 52-name partition is exhaustive, there is no seventh valid field
that can reach `UNVALIDATED`.

V1 exact findings: none.

`Blocker=0; Major=0; Minor=0; Ambiguity=0`

`PASS`

`VALIDATOR_REVIEW_V1_PASS`

## 3. Reviewer V2 report

### 3.1 Identity, delta, namespace, and parser agreement

V2 independently reproduced every target/predecessor/control/source identity,
the twelve-hunk authorized delta, seventeen-basename census, five-control
set, one-way identity frame, three evidence frames, 15-mode/74-row/90-field/
52-name structure, fifteen expanded positives, and every required negative.
It confirmed source has no self-hash or future-review cycle and lock has no
stale active namespace or false predecessor-review claim.

V2 separately recomputed all unchanged name frames, including root-stage
pre-I066 166/2,188, I066 inflight 168/2,212, post-I066 169/2,224; cross
X001--X008 24/288, X009 inflight 26/312, X009 complete 27/324, X010 inflight
29/348, and X010 complete 30/360.  Every digest matches the lock.

### 3.2 Complete preserved security baseline

V2 independently passed the following predecessor predicates, which are
unchanged outside the exact namespace/parser delta:

- held per-component no-follow paths, leaf stat/open identity, mode/link/size,
  EOF probe, full digest, FD/path rebinding, exact-name universes, and no path
  derived from enumeration;
- exact Python environment/runtime/image/imports/argv, `/proc/self/fd`
  census, finite soft `RLIMIT_NOFILE` 1024--4096, `/proc/self/exe` binding,
  and honest external pre-main/cross-process trust premises;
- the literal 87-row/23,408-byte dependency frame, 87 logical paths, 86 final
  targets, two raw symlink hops, held no-follow final reads, tool identities,
  ABSENT/REPLAY rebinds, and no prospective extra dependency;
- exact 74-row argv membership, stdout/stderr/status guard, held receipt FDs,
  offsets, fsync/readback, exact stage/evidence sets, and exclusive
  `O_CREAT|O_EXCL|O_NOFOLLOW` snapshot/manifest writes with no overwrite,
  retry, rename, unlink, truncate, or repair;
- closed AUX/BBL/BLG grammars, exact twenty cite keys/items, warning/log
  disposition, PDFINFO and PDFTEXT schemas, sentinel/pages/headings/fixtures/
  boundaries/conclusion/reference/anonymity closure;
- PDFRAW header/object/stream/length/token/depth limits, bounded ObjStm,
  conventional xref or XRef-stream closure, offsets/free chain/startxref/EOF,
  Catalog/Info/Page tree, `/Contents`, resources/fonts, stream-role and inbound
  multiplicity, bounded content decoding, inline-image and rolling semantic
  token checks;
- Type1 PFA/PFB and Length1/2/3 closure, eexec/CharString/Subr decoding,
  clear/private/macro/OtherSubrs grammar, bounded stack/call/steps, concrete
  glyph and reachable-Subr execution, unreachable inert-Subr abstract
  contract, and honest external font-provenance boundary;
- SOURCEFINAL, STAGEINV cached receipt/snapshot/manifest/semantic checks,
  CROSS raw/normalized/projected equality, EVIDENCE initial/terminal/ultimate
  inventories, and no on-disk projection; and
- terminal recomputation, detail equality, PASS self-parse, short-write loop,
  fsync/readback, post-emission runtime/control/dependency/hold checks, and the
  required conjunction of status 0, exact stdout, empty stderr, and receipts.

V2 found no unsafe operation, omitted predicate, source/lock mismatch,
trust-boundary overclaim, path ambiguity, or semantic regression.

V2 exact findings: none.

`Blocker=0; Major=0; Minor=0; Ambiguity=0`

`PASS`

`VALIDATOR_REVIEW_V2_PASS`

## 4. Additional separated parser-matrix audit

The additional auditor independently confirmed all 15 field/emitter schemas,
90 occurrences, the complete 52-name partition, six total symbolic branches,
mode-sensitive manifest ordering, all fifteen expanded lock vectors, every
symbolic/decimal/hash/warning/structured/framing/expected negative tag, and
the absence of a seventh unvalidated field or lock-vector error.

Its exact findings were none.

`Blocker=0; Major=0; Minor=0; Ambiguity=0`

`PASS`

## 5. Aggregate conjunction and scope

| Report | Blocker | Major | Minor | Ambiguity | Result |
|---|---:|---:|---:|---:|---|
| Reviewer V1 | 0 | 0 | 0 | 0 | PASS |
| Reviewer V2 | 0 | 0 | 0 | 0 | PASS |
| Parser-matrix audit | 0 | 0 | 0 | 0 | PASS |
| Conjunction | 0 | 0 | 0 | 0 | PASS |

This artifact certifies only the exact frozen post-failure validator source
and lock through static analysis.  It is not a runtime microtest, build,
evidence, release-integrity, or external-effect authorization.  No validator
byte was imported, compiled, or executed and no build path was probed during
these reviews.

BATCH07_P27_VALIDATOR_POSTFAIL_REVIEW_PASS
