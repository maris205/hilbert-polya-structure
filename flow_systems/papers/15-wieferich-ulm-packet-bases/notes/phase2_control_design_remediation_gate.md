# Replacement Paper 15 Phase-2 control-design remediation gate

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT — C0/M3/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)

This gate authorizes one design-only amendment.  It authorizes no generator,
test suite, README, CSV, manifest, implementation, reproduction run, Route,
composition, manuscript, figure, release, archive, Git action, or public
synchronization.

## 1. Exact authority

```text
post-proof control-design gate
  path: notes/phase2_control_design_gate.md
  sha256:0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3

frozen base control design
  path: notes/phase2_control_design_lock.md
  sha256:db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
  lines:1183
  bytes:62887

independent exact-byte design review
  path: notes/phase2_control_design_peer_review.md
  sha256:3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec
  lines:488
  bytes:22894
  verdict:REVISE_C0_M3_m0
```

All three records were read in full and rehashed on their final bytes.  The
review independently passed every arithmetic model, schema, row count,
authority binding, and manifest edge, but found three experiment-integrity
acceptance surfaces.  Those findings are binding until a versioned amendment
and an independent exact-byte re-review close them.

## 2. Sole authorized target

One file may be created at exactly:

```text
notes/phase2_control_design_amendment_v1.md
```

The amendment must bind the three exact records above and may supersede only
the effective design clauses needed to close M1--M3.  All other base-design
bytes and semantics remain binding.  The amendment must not embed its own
digest.

## 3. M1 repair — causal semantic negatives

For each `S01` through `S35`, the amendment must freeze an exact causal test
chain:

```text
primitive valid seed
  -> independent valid evaluation PASS
  -> one exact substantive mutation
  -> canonical serialize
  -> independent reparse
  -> semantic projection excluding row_id, case_kind,
     mutation_id, negative_reason, oracle, status and detector receipts
  -> arithmetic recomputation or closed typed policy predicate
  -> rejection decision
  -> detector comparison only after rejection
  -> exact inverse/correction
  -> independent acceptance.
```

The amendment must provide a complete `S01..S35` seed/mutation/predicate
registry.  Policy families must use parsed owner/operator/quantifier/state
transitions, not row IDs, reason tokens, membership in a negative list,
substrings, or a supplied expected detector.  The oracle may emit the frozen
detector only after its substantive predicate has failed.  Counts remain
exactly 35 semantic rows and 35 semantic methods.

## 4. M2 repair — observable verify-only immutability

The amendment must freeze one recursive, nonserialized, before/after `lstat`
receipt over the complete isolated repository read set, including every
participating directory.  Each relative-path record must contain at least:

```text
relative path, entry type, mode, size, SHA-256 for regular files,
mtime_ns, ctime_ns, link count, device, inode.
```

The exact inventory and every recorded field must be identical after both a
valid and a malformed `--verify-only` call.  Access time is excluded.  The
receipt must operate under uid 0 and may not expose or serialize an absolute
root.  Directory metadata must participate so create-and-unlink behavior is
observable.  An existing `test_rep_*` method must be assigned an explicit
method-owned falsifier that proves the receipt detects mode-only,
timestamp-only, and transient-sidecar mutations; serial subfixtures may share
that single registered metadata-integrity class.  The total method count
remains 173.

## 5. M3 repair — root capability and lock/cleanup state machine

The amendment must freeze one exact, operational-only capability handoff from
the wrapper to every authorized generation root.  It must specify:

- who creates the root, its ownership, nonsymlink and mode checks;
- the exact environment/descriptor/token used as the capability;
- validation order before nonempty-root classification;
- which root `P25` uses and how it contains exactly `occupied` while remaining
  authorized, so `E_NONEMPTY_OUTPUT` is not masked by outside-root rejection;
- why mutation roots are excluded from the canonical two fresh generations
  and three identity copies; and
- cleanup and nonserialization of every capability artifact.

The external-lock state machine must separately freeze:

```text
UNOWNED
  -> acquisition attempt
  -> OWNED with an independently verifiable ownership token
  -> CLEANING
  -> ABSENT,
```

including trap installation, signal deferral/handling across acquisition,
the ownership transition, success cleanup, failure cleanup, and final absence
checks.  A process may remove only a lock whose exact ownership token it
created.  A pre-existing lock remains untouched and produces the frozen
concurrent-entry class.  Operational tokens and paths are never serialized or
printed.  `P24` must cover the owned failure path and an existing method must
cover the acquisition/signal boundary without changing the 28-class or
173-method totals.

## 6. Frozen invariants

The amendment must preserve exactly:

```text
schema versions
8 CSV paths and headers
9 generated artifacts including manifest
120 body rows
35 negative rows
35 semantic mutation classes
28 package mutation classes
173 unittest methods
14 authority bindings
2 fresh generations
3 byte-identical copies
exact-zero tolerance
universal recover-p = OPEN_NOT_AUTHORIZED
Route B = false
manifest no-self / no-future-result / no-concurrent-proof DAG.
```

If closing M1--M3 requires any count, schema, path, authority, theorem, or
owner change, the amendment must stop and report a new design finding rather
than silently widen scope.

## 7. Mandatory re-review and downstream stop

After the amendment is frozen, an independent reviewer must read the
effective `base + amendment` tuple and append a closure addendum to
`notes/phase2_control_design_peer_review.md`, preserving the complete current
22,894-byte prefix exactly.  The addendum must independently attack each
causal negative, metadata receipt, root capability, and lock state transition.
Only a final `PASS C0/M0/m0` digest can support a later implementation gate.

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE=PASS_TO_ONE_AMENDMENT
OPEN_FINDINGS=C0_M3_m0
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v1.md

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
INDEPENDENT_REREVIEW_REQUIRED=true

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

This gate does not embed its own SHA-256.  The amendment and later re-review
must bind its final digest externally.
