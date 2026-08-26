# Paper 17 Phase-2 deterministic-control design exact-byte review

Status: **REVISE — C0 / M1 / m0**  
Version: `P17-P2-CONTROL-DESIGN-REVIEW-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Review mode: independent exact-byte adversarial design review  
Publication disposition: **Technical Note path retained; implementation remains blocked**  
Standalone disposition: **false**

No control implementation, generated result, manifest, generator, test suite,
reproduction script, control run, Route A/B, composition, manuscript, figure,
release, archive, Git, or public synchronization was created or executed in
this review.

## Material Passport

- Origin Skill: ARS academic-research-suite, using experiment-design,
  reproducibility, integrity, methodology-reviewer, and devil's-advocate
  boundaries
- Origin Mode: read-only independent control-design review
- Origin Date: 2026-08-16
- Verification Status: `REVISE`
- Version Label: `p17_phase2_control_design_review_v1`
- Reviewed Gate:
  `notes/phase2_control_design_gate.md`
- Reviewed Gate SHA-256:
  `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647`
- Reviewed Design:
  `notes/phase2_control_design_lock.md`
- Reviewed Design SHA-256:
  `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa`
- Scope: final design bytes only; no executable control was used to repair or
  reinterpret an ambiguity

## 1. Exact-byte intake and authority receipts

The two authorized inputs were re-hashed before review:

| Artifact | Lines | Bytes | SHA-256 | Intake |
|---|---:|---:|---|---|
| `notes/phase2_control_design_gate.md` | 201 | 8,455 | `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647` | exact match |
| `notes/phase2_control_design_lock.md` | 2,103 | 98,350 | `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa` | exact match |

The authority tuple quoted by the design was also checked against the current
local bytes. All thirteen Paper-14--18/Paper-17 digests agree with Section 1,
and the fixed-prime source binding agrees with the current Paper-9 manuscript:

```text
papers/9-packet-separation/paper/manuscript.tex
sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
```

This establishes byte identity only. It does not independently re-prove the
symbolic theorem or convert any finite control into mathematical evidence.

## 2. Independent schema and row arithmetic

### 2.1 Nine CSV headers

Each header was recounted directly from its comma-delimited token sequence.
The widths are:

| Order | CSV | Recounted columns | Frozen columns | Result |
|---:|---|---:|---:|---|
| 1 | `range_first_handedness_controls.csv` | 17 | 17 | match |
| 2 | `action_blind_open_records.csv` | 16 | 16 | match |
| 3 | `connected_disconnected_firewall.csv` | 16 | 16 | match |
| 4 | `domain_guard_controls.csv` | 15 | 15 | match |
| 5 | `quantale_localic_firewall.csv` | 18 | 18 | match |
| 6 | `actual_standard_owner_controls.csv` | 17 | 17 | match |
| 7 | `dilation_strict_marker_controls.csv` | 19 | 19 | match |
| 8 | `fixed_prime_provenance_controls.csv` | 17 | 17 | match |
| 9 | `target_summary.csv` | 12 | 12 | match |

Thus the ordered header-width vector is exactly

```text
17,16,16,15,18,17,19,17,12.
```

### 2.2 Family counts, endpoints, and negatives

The family arithmetic was recomputed from the frozen fixture cardinalities,
not copied from the self-audit:

| CSV | Independent family arithmetic | Body rows | ID endpoint | Negative rows | Nonnegative rows |
|---|---|---:|---|---:|---:|
| C17-1 | `36+6+36+1296+36+216+18+18` | 1,662 | `GH-1662` | 36 | 1,626 |
| C17-2 | `48+48+768+48+32+32+512+32` | 1,520 | `AO-1520` | 0 | 1,520 |
| C17-3 | `3+9+3+4` | 19 | `CZ-0019` | 4 | 15 |
| C17-4 | `3+12+10` | 25 | `DG-0025` | 10 | 15 |
| C17-5 | `3+8+7+3` | 21 | `QL-0021` | 7 | 14 |
| C17-6 | `2+5+11` | 18 | `AS-0018` | 11 | 7 |
| C17-7 | `2+4+16+16+16+16+64+4+2` | 140 | `DM-0140` | 5 | 135 |
| C17-8 | `1+3+6+11` | 21 | `FP-0021` | 11 | 10 |
| summary | `9+1` | 10 | `TS-0010` | 0 | 10 |

The two nonabelian C17-1 counts also close independently: `D3` has 36
ordered pairs and 18 ordered noncommuting pairs, while the full arrow-pair
matrix has `36*36=1296` rows and exactly `36*6=216` composable rows. The
C17-2 counts close as `3*16`, `3*16*16`, `2*16`, and `2*16*16` in their
respective per-action and cross-action families.

The package sums are therefore:

```text
CSV_BODY_ROWS
  = 1662+1520+19+25+21+18+140+21+10
  = 3436

EXPLICIT_NEGATIVE_ROWS
  = 36+0+4+10+7+11+5+11+0
  = 84

NONNEGATIVE_CSV_ROWS
  = 3436-84
  = 3352.
```

All per-file targets, the package row, and the self-row count of ten summary
body rows agree with these independent totals.

### 2.3 Negative-reason ledger

The closed semantic-reason registry contains 48 classes:

```text
C17-1  2 classes, multiplicities 18 and 18          -> 36 rows
C17-3  4 classes, each once                         ->  4 rows
C17-4 10 classes, each once                         -> 10 rows
C17-5  7 classes, each once                         ->  7 rows
C17-6 11 classes, each once                         -> 11 rows
C17-7  3 classes, multiplicities 3, 1, and 1        ->  5 rows
C17-8 11 classes, each once                         -> 11 rows
                                                     --------
semantic classes = 48; explicit negative rows = 84.
```

The repeated C17-7 strict-marker reason is one semantic class with three
frozen nonunit witnesses; it is not three silently bundled reason classes.

## 3. Independent method and inventory recount

### 3.1 Explicit `unittest` methods

The source-level names frozen in Sections 8.1--8.3 were extracted as names,
deduplicated, and recounted. They comprise 180 distinct names with no
duplicate:

| Method group | Recounted |
|---|---:|
| Eight C17 conformance groups | `10+10+6+6+6+6+8+6 = 58` |
| Summary/package schema | 8 |
| Manifest/provenance | 10 |
| Reproduction/read-only | 8 |
| Oracle independence | 6 |
| Other nonmutation subtotal | `8+10+8+6 = 32` |
| Semantic mutation registry `S001..S048` | 48 |
| Package mutation registry `P001..P042` | 42 |
| **Total** | **`58+32+48+42 = 180`** |

The mutation-method subtotal is independently `48+42=90`. P033 and P034
restart from pristine state for each explicitly declared equivalent cache
representative; they do not accumulate multiple deltas or stand in for two
registered semantic reason classes.

### 3.2 Generated, implementation, binding, and manifest inventories

The inventories close as follows:

- generated package: nine ordered CSVs plus one final manifest = 10 artifacts;
- manifest `artifacts`: the nine CSVs only, in Section-2 order;
- future implementation: exactly three `code/` paths and two `experiments/`
  paths = five hashed implementation entries;
- authority bindings: design gate, Paper-9 manuscript, final design lock,
  independent design review, and later implementation gate = five entries;
- fresh generation roots: A and B = two independent generator processes;
- byte-identity copies: checked-in, A, and B = three complete copies, each
  covering all nine CSVs and the manifest.

The manifest is absent from `bindings`, `implementation`, and `artifacts`,
and has no self-byte-count or self-digest. Direct P17 proof and proof-review
paths/digests are prohibited; the design gate is the indirect authority.
Every implementation path and CSV has both byte count and SHA-256. The
resulting dependency graph is acyclic on the frozen specification.

## 4. Required adversarial attacks

### 4.1 Invalid fixture plus supplied detector or PASS receipt

**Result: closed by design.** Persisted `status`, `detected`,
`negative_reason`, `subject_value`, `oracle_value`, composability, open,
equality, licensing, and inverse receipts are quarantined before semantic
derivation. Artifact path and canonical row family select the oracle; a
supplied reason or oracle token cannot select a permissive branch. Exact row
order, family cardinality, reason multiplicity, and negative/nonnegative
field rules prevent relabelling an arbitrary row as an expected negative.

### 4.2 Hard-coded PASS, summary, or manifest totals

**Result: closed by design.** Raw CSV semantics precede summary and manifest
validation. The nine raw CSV widths/counts/negative registries are recomputed;
the summary is then compared with those raw rows, and the manifest is checked
last against the files and recomputed aggregates. Neither summary nor
manifest can validate the other circularly, and persisted PASS values have no
oracle authority.

### 4.3 Same-formula oracle attack

**Result: closed by design.** The frozen alternatives are materially distinct:
pair law versus vertex permutations; explicit action relations versus bitmask
set arithmetic; modular table versus a three-cycle permutation; emitted
owner/claim records versus a closed owner-domain policy; emitted gate bits
versus independent conjunction; emitted packets versus an immutable packet
registry; rational maps versus cleared-denominator integer congruences; and
emitted fixed-prime records versus a two-input allowlist plus direct source
hash. The verifier may not import or call generator helpers. Policy receipts
remain policy receipts and do not masquerade as independent mathematical
proofs.

### 4.4 Finite-proxy and owner-splice attacks

**Result: closed by design.** C17-3 separates the symbolic connected-real
receipt from the executable `Z/3Z` falsifier. C17-4 rejects discrete evidence
for usual-real non-etaleness/nonunitality. C17-5 requires bare quantale,
`q_H`, and local-compactness receipts separately and rejects all seven
incomplete bit triples. C17-6 freezes distinct actual/standard owner,
topology, topos, quantale, and base fields and isolates eleven splice
mutations. No finite row is licensed to establish a real, topos, or localic
theorem.

### 4.5 Mutation-class isolation and provenance promotions

**Result: closed except for M1 below.** The 48 semantic method names map
one-for-one to the 48 registered semantic reason classes. In particular,
wrong product order, opposite sheet handedness, wrong owner/domain, bare-
quantale promotion, each owner splice, strict nonunit scale, and the separate
C-star/Haar/measure/trace/determinant/Route-B/priority promotions have
isolated methods. The Paper-9 hash and two-input post-generic allowlist are
separate from the reason token.

### 4.6 Manifest self/proof/unhashed-path attacks

**Result: closed by design.** P023, P024, and P031 isolate self binding,
direct P17 proof binding, and an unlisted implementation path. The exact
manifest key/array shapes, five bindings, five implementation entries, nine
artifact entries, and digest/byte recomputation prevent an injected path or
digest from becoming authority.

### 4.7 Verify-only and package fail-closed matrix

The frozen registry explicitly covers:

| Surface | Frozen methods | Static result |
|---|---|---|
| content/header/order/ID/row tamper | P001--P008 | closed |
| stale file/package counts | P009--P013 | closed |
| missing/extra file or directory | P014--P018 | closed |
| malformed/drifted/self/proof manifest | P019--P030 | closed |
| unhashed implementation path | P031 | closed |
| bytecode/tool cache | P032--P034 | closed |
| recursive entry | P035 | closed |
| concurrent entry | P036 | **internally contradictory; see M1** |
| CRLF plus no rewrite | P037 | closed |
| nonempty generation root | P038 | closed |
| result symlink/hardlink | P039--P040 | closed |
| stale manifest method/copy totals | P041--P042 | closed |

The verify-only contract itself forbids every mutating operation and surrounds
the checked-in validation with ordered byte/hash/mode/mtime/link receipts.
The design therefore supplies a static no-rewrite specification; no runtime
claim is made in this review because implementation and execution remain
unauthorized.

## 5. Blocking finding

### M1 — The pre-run residue scan consumes P036 before the concurrency gate

**Severity: Major.** This is a localized, repairable orchestration defect,
not a symbolic mathematical error; however, it makes one mandatory isolated
package mutation and its promised exit class impossible under the frozen
sequence.

**Evidence anchors:**

- Section 8.3, lines 1578--1581, requires P036 to pre-create the exact lock
  directory and reach the concurrency gate.
- Section 10.2 step 4, lines 1845--1849, first rejects every pre-existing
  cache/residue class and only afterwards attempts the atomic lock `mkdir`.
- The closed residue vocabulary, lines 1871--1876, includes every
  `.p17-control-*` entry except an active lock *while owned*.
- Lines 1884--1885 state that only the currently owned lock is exempt.
- Section 10.4 assigns recursive/concurrent entry to exit 3 and residue to
  exit 5.

P036's pre-created directory is not yet owned by the child. Under the stated
order, it is therefore a pre-existing `.p17-control-*` residue and must be
rejected before the `mkdir` concurrency branch is reached. A conforming
implementation cannot simultaneously obey the scan order, the owned-lock
exception, and P036's required concurrency classification. Treating the
directory as already exempt would silently broaden “currently owned” and
leave the order ambiguous, which Section 11.3 itself declares blocking.

**Impact:**

- P036 cannot deterministically exercise its registered concurrent-entry
  class;
- exit-3 versus exit-5 classification is not frozen;
- the claim that all 42 package mutation classes have one executable isolated
  method is not yet implementable; and
- implementation cannot be authorized from this design digest.

**Minimum versioned repair:** amend step 4, P036, and the residue-exemption
wording together to freeze this exact order:

1. after recursion and root validation, inspect the exact lock path
   separately; if an entry already exists there, reject it as concurrent with
   exit 3;
2. scan all other subtree entries for the closed cache/residue classes while
   excluding only that exact lock pathname from the generic residue scan;
   reject any other residue with exit 5;
3. perform the one atomic `mkdir` for the exact lock; an intervening
   existence race is also exit 3; and
4. only after successful `mkdir` call the lock “currently owned” and exempt
   it during later owned-lock scans and cleanup.

The repair must be a versioned design amendment or a newly frozen design
digest. It must not be supplied informally by implementation code. The
amended exact bytes require another independent design review.

## 6. Findings ledger and disposition

```text
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=0

M1=PRE_RUN_RESIDUE_SCAN_PREEMPTS_P036_CONCURRENCY_GATE
```

All independent recounts requested by the design gate agree:

```text
CSV_HEADERS=9
CSV_HEADER_WIDTHS=17,16,16,15,18,17,19,17,12
CSV_BODY_ROWS=3436
EXPLICIT_NEGATIVE_ROWS=84
NONNEGATIVE_CSV_ROWS=3352
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=10
UNIQUE_EXPLICIT_UNITTEST_METHODS=180
SEMANTIC_MUTATION_METHODS=48
PACKAGE_MUTATION_METHODS=42
ISOLATED_MUTATION_METHODS=90
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
```

The exact-byte verdict is therefore:

```text
CONTROL_DESIGN_REVIEW_PERFORMED=true
CONTROL_DESIGN_REVIEW_VERDICT=REVISE_C0_M1_m0
CONTROL_DESIGN_REVIEW_PASS=false
TECHNICAL_NOTE_CANDIDATE=true
STANDALONE_PASS=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Paper 17's symbolic proof and Technical Note candidacy are unaffected. The
control-design pipeline stops at this review until M1 is repaired on new,
versioned exact bytes and the replacement design receives an independent
`C0/M0/m0` review.

---

## Closure addendum v1 — amendment exact-byte re-review

Closure status: **PASS — effective C0 / M0 / m0**  
Closure version: `P17-P2-CONTROL-DESIGN-CLOSURE-REVIEW-v1.0`  
Closure date: 2026-08-16 (Asia/Shanghai)  
Effective design: frozen base design plus narrow amendment v1

This addendum is append-only. The 382-line, 15,885-byte review above remains
an exact historical prefix with SHA-256

```text
a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342.
```

Its `REVISE_C0_M1_m0` verdict remains the correct verdict on the unamended
base bytes alone. This addendum records the independent closure verdict on
the effective `base + amendment v1` design; it does not rewrite or erase the
original finding.

### A. Closure input receipts

The three closure inputs were re-hashed on their complete current bytes
before adjudication:

| Closure input | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| base `notes/phase2_control_design_lock.md` | 2,103 | 98,350 | `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa` | exact match |
| original review prefix | 382 | 15,885 | `a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342` | exact match |
| `notes/phase2_control_design_amendment_v1.md` | 219 | 8,737 | `83c8effb2dc4e79f90ef4c72cf5b8f4b20974dc21af8a02e074e19a231b0970d` | exact match |

No base-design or amendment byte was edited. No generator, verifier, test,
manifest, result, implementation file, or reproduction entry was created or
run for this closure review.

### B. M1 closure trace

The amendment supplies one non-overlapping classification path for every
state that M1 left ambiguous:

| State | Effective ordered rule | Required class | Closure result |
|---|---|---:|---|
| `P17_REPRO_ACTIVE` nonempty | recursive guard before any filesystem inspection or mutation | exit 3 | closed |
| exact lock path already occupied by any entry type | no-follow exact-path check before generic scan; do not mutate entry | exit 3 | closed |
| any other closed `.p17-control-*` or cache/residue entry | full-subtree no-follow scan excluding only the already handled exact lock pathname | exit 5 | closed |
| exact lock appears after the dedicated check but before atomic acquisition | the one atomic `mkdir` fails on existence; losing invocation does not remove entry | exit 3 | closed |
| atomic `mkdir` succeeds | ownership begins only at this successful call | continue | closed |
| later owned-lock scan and cleanup | exempt/remove only the exact lock acquired by this invocation | owned-only | closed |

The precedence is now deterministic:

```text
recursive guard
  -> root/environment validation
  -> exact pre-existing-lock check
  -> all-other-residue scan
  -> atomic mkdir
  -> owned-lock state.
```

The exact-path exclusion in the generic scan is not a name-prefix exemption.
It excludes no sibling, alternate spelling, descendant, or other task-residue
entry. Before successful `mkdir`, the invocation owns no lock and therefore
has no cleanup authority over a pre-existing or raced entry.

### C. P035 and P036 independent reapplication

**P035 remains fully addressed.** Its precondition is a nonempty
`P17_REPRO_ACTIVE`; the first effective rule returns recursive/concurrent
class exit 3 before root, lock, residue, temporary-root, or cleanup activity.
The amendment does not move or weaken that guard.

**P036 is now fully addressed.** Starting from a pristine isolated copy with
the recursion variable absent and only the exact lock directory pre-created,
the dedicated no-follow path check fires before the generic residue scan. It
returns exit 3, cannot accept exit 5, and cannot remove, rename, touch, chmod,
enter, or otherwise mutate the unowned directory. Test cleanup remains owner
of only the enclosing isolated root.

The check-to-`mkdir` race is separately closed in the same concurrency class:
an entry appearing in that interval makes atomic acquisition fail with exit 3.
This race rule neither adds a 43rd package mutation class nor substitutes for
P036's mandatory pre-created-lock witness.

### D. Count, schema, mutation, and DAG regression audit

The amendment supersedes only the named orchestration-order clauses. It
changes no CSV schema/header, row family, reason registry, oracle, source
binding, method name, generated inventory, or reproducibility cardinality.
The previously independent recount therefore remains effective without
change:

```text
CSV_HEADER_WIDTHS=17,16,16,15,18,17,19,17,12
CSV_BODY_ROWS=3436
EXPLICIT_NEGATIVE_ROWS=84
NONNEGATIVE_CSV_ROWS=3352
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=10
UNIQUE_EXPLICIT_UNITTEST_METHODS=180
SEMANTIC_MUTATION_METHODS=48
PACKAGE_MUTATION_METHODS=42
ISOLATED_MUTATION_METHODS=90
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
```

The effective authority chain is acyclic:

```text
base design
  -> original exact-byte review prefix
  -> narrow amendment v1
  -> this append-only closure addendum
  -> possible later implementation gate
  -> possible later implementation/artifacts/manifest.
```

The amendment adds no manifest self hash, direct P17 proof/proof-review
binding, generated artifact, or unhashed implementation path. The base
five-binding/nine-artifact manifest shape and all aggregate totals remain
unchanged. Any later implementation gate must carry the amendment and this
final closure receipt as authority; this addendum itself authorizes neither
implementation nor execution.

### E. Effective closure verdict

M1 is closed on the effective amended design, and the narrow repair introduces
no new Critical, Major, or Minor finding:

```text
HISTORICAL_BASE_ONLY_VERDICT=REVISE_C0_M1_m0
HISTORICAL_M1=PRE_RUN_RESIDUE_SCAN_PREEMPTS_P036_CONCURRENCY_GATE
M1_EFFECTIVE_STATUS=CLOSED_BY_AMENDMENT_V1

EFFECTIVE_DESIGN=BASE_abdc4239_PLUS_AMENDMENT_83c8effb
EFFECTIVE_CRITICAL_OPEN=0
EFFECTIVE_MAJOR_OPEN=0
EFFECTIVE_MINOR_OPEN=0
EFFECTIVE_CONTROL_DESIGN_REVIEW_VERDICT=PASS_C0_M0_m0
AMENDED_DESIGN_REVIEW_PASS=true

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
STANDALONE_PASS=false
TECHNICAL_NOTE_CANDIDATE=true
```

The control-design review gate is closed at `C0/M0/m0` for the effective
base-plus-amendment design. A separate owner may now consider an implementation
gate; no such gate is issued or implied here.
