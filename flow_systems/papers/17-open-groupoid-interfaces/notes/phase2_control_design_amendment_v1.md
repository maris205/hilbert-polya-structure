# Paper 17 control-design amendment v1: exact lock/concurrency ordering

Status: **FROZEN CANDIDATE — NARROW M1 REPAIR / INDEPENDENT RE-REVIEW REQUIRED**  
Version: `P17-P2-CONTROL-DESIGN-AMENDMENT-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Scope: one orchestration-order finding only

This amendment is design-only.  It creates or authorizes no implementation,
generated result, manifest, test, reproduction run, Route A/B, composition,
manuscript, figure, release, archive, Git, or public synchronization.

## 1. Exact immutable inputs

This amendment binds the following complete frozen bytes:

```text
post-proof control-design gate
  path: papers/17-open-groupoid-interfaces/notes/phase2_control_design_gate.md
  sha256:093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647

base control-design lock
  path: papers/17-open-groupoid-interfaces/notes/phase2_control_design_lock.md
  sha256:abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa
  lines:2103
  bytes:98350

independent exact-byte design review
  path: papers/17-open-groupoid-interfaces/notes/phase2_control_design_review.md
  sha256:a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342
  verdict:REVISE_C0_M1_m0
```

The base design remains immutable.  This file supersedes only the exact
ordering/classification clauses named below.  Every other base-design byte,
fixture, schema, header, family, count, oracle, mutation, manifest and
authorization rule remains binding.

## 2. Finding being repaired

The independent review found one contradiction:

```text
M1=PRE_RUN_RESIDUE_SCAN_PREEMPTS_P036_CONCURRENCY_GATE
```

Base Section 8.3 requires P036 to pre-create the exact reproduction lock and
reach the concurrency class, exit 3.  Base Section 10.2 step 4 instead scans
all pre-existing `.p17-control-*` residue before trying to acquire the lock,
while exempting the lock only after it is owned.  The P036 entry is therefore
forced to exit 5 before the concurrency branch.  This amendment removes that
ordering contradiction without widening the residue exemption.

## 3. Superseding exact top-level order

For the effective design `base + amendment v1`, base Section 10.2 steps 1--4
are read with the following exact precedence:

1. **Recursive guard.**  If `P17_REPRO_ACTIVE` is nonempty, exit 3 before
   any filesystem write, deletion, lock acquisition or cleanup.
2. **Deterministic environment and root validation.**  Set the frozen
   environment and resolve/reject the script/root exactly as in base steps
   2--3.  These checks do not create or remove the lock path.
3. **Exact pre-existing-lock check.**  Inspect, without following links, the
   one pathname

   ```text
   experiments/.p17-control-reproduce.lock
   ```

   before the generic residue scan.  If **any** filesystem entry already
   occupies that exact pathname (directory, regular file, symlink, device,
   FIFO, socket, or other entry), classify the invocation as concurrent and
   exit 3.  Do not remove, rename, chmod, touch, enter, or otherwise mutate
   the unowned entry.
4. **Other cache/residue scan.**  Scan the full Paper-17 subtree, without
   following symlinks, for every closed cache/residue class from base
   Section 10.2.  The generic scan excludes only the exact lock pathname
   already handled in step 3; it does not exclude any sibling, prefix match,
   descendant, alternate spelling or other `.p17-control-*` entry.  Any such
   other cache or residue is exit 5.
5. **Atomic acquisition.**  Execute one atomic `mkdir` for the exact lock
   pathname.  Success is the only event that establishes ownership.  If the
   call fails because another entry appeared after step 3, classify that
   race as concurrent and exit 3 without deleting the other entry.  Any
   unrelated failure maps to the narrowest applicable nonzero class and
   never to success.
6. **Owned-lock state.**  Only after the successful `mkdir` may the process
   call the exact lock “currently owned”, exempt it from later owned-lock
   inventory scans, and register it for its exit trap/explicit cleanup.
   Cleanup may remove only the lock acquired by this invocation and the two
   exact temporary roots it later records.

All later base reproduction steps retain their order.  The explicit final
cleanup must remove the owned lock and verify its absence before success.

## 4. Effective residue vocabulary

The closed base vocabulary remains:

```text
directory basename: __pycache__,.pytest_cache,.mypy_cache,.ruff_cache
file suffix:        .pyc,.pyo
task residue:       .p17-control-* except the exact currently owned lock
```

The effective interpretation is now unambiguous:

- before acquisition, the exact lock pathname is handled only by the
  dedicated step-3 concurrency check;
- every other matching task-residue pathname is handled by the generic
  residue scan and exits 5;
- after successful acquisition, only that exact owned lock is temporarily
  exempt;
- no pre-existing lock is ever deemed owned; and
- no pre-existing or raced lock is removed by a losing invocation.

This is a one-path classification rule, not a general exemption for names
beginning with `.p17-control-`.

## 5. Effective P035/P036 mutation contracts

The base P035 contract is unchanged:

```text
P035: preset P17_REPRO_ACTIVE=1 -> recursive guard -> exit 3,
      before any lock or residue inspection.
```

The superseding P036 contract is:

```text
P036: start from a pristine isolated package copy;
      ensure P17_REPRO_ACTIVE is absent;
      pre-create only
        experiments/.p17-control-reproduce.lock
      as a directory;
      invoke the top-level reproduction once;
      require exit 3 from the exact pre-existing-lock check;
      require the pre-created directory bytes/type/metadata to remain
        untouched by the child;
      remove only the enclosing isolated test root in test cleanup.
```

P036 must not add any second residue or cache mutation.  It cannot pass by
accepting exit 5.  A separate race probe may test atomic acquisition inside
the same concurrency gate class, but it is not a new method or a substitute
for the exact pre-created-lock witness.

## 6. Preserved exact design totals and DAG

This amendment changes no data/test cardinality:

```text
SCHEMA=paper17-open-groupoid-controls/1
MANIFEST_SCHEMA=paper17-open-groupoid-controls-manifest/1
CSV_ARTIFACTS=9
GENERATED_ARTIFACTS=10
CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
EXPLICIT_NEGATIVES=84
TEST_METHODS=180
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
```

All nine headers, all row-family bytes, all 48 semantic methods and every
package method other than the clarified P036 route are unchanged.  The
manifest remains acyclic, without self/proof binding.  A future manifest may
bind the final design amendment and its closure review only under a later
implementation gate; this amendment predicts no such digest.

## 7. Required independent closure review

An independent reviewer must re-hash the base design, original review and
this amendment, then verify:

1. P035 reaches recursion exit 3 before filesystem inspection;
2. P036 reaches concurrency exit 3 rather than residue exit 5;
3. any other `.p17-control-*` entry still reaches residue exit 5;
4. a lock appearing between the dedicated check and `mkdir` is exit 3;
5. no losing invocation deletes or mutates an unowned lock;
6. only a successfully acquired exact lock is exempt and cleaned; and
7. all `3436/84/3352/180/48/42/90/2/3` totals and all other base findings
   remain unchanged.

The reviewer must append or freeze an exact-byte closure receipt.  Until it
returns `C0/M0/m0`, implementation remains blocked.

## 8. Authorization matrix

```text
AMENDMENT_ID=P17-P2-CONTROL-DESIGN-AMENDMENT-v1.0
REPAIRED_FINDING=M1_PRE_RUN_RESIDUE_SCAN_PREEMPTS_P036
BASE_DESIGN_SHA256=abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa
ORIGINAL_REVIEW_SHA256=a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342
ORIGINAL_REVIEW_VERDICT=REVISE_C0_M1_m0
AMENDED_DESIGN_REVIEW_REQUIRED=true
AMENDED_DESIGN_REVIEW_PASS=false
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

This amendment closes no gate by self-assertion.  Its sole purpose is to
make one previously impossible fail-closed mutation and exit classification
mechanically implementable on later authorized bytes.
