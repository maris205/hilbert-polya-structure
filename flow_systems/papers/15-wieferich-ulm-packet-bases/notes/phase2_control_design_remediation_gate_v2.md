# Replacement Paper 15 Phase-2 control-design remediation gate v2

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v2 — C0/M4/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v2.0`  
Date: 2026-08-16 (Asia/Shanghai)

This is a design-remediation authorization, not a finding closure.  All four
major findings in the final append-only design review remain open.  This gate
authorizes one design-only amendment and, only after that amendment is frozen,
one fresh independent append-only re-review.  It authorizes no generator,
verifier, test suite, README, CSV, manifest, implementation, reproduction run,
Route, composition, manuscript, figure, release, archive, Git action, or public
synchronization.

## 1. Exact authority and current effective verdict

The following records were read on their complete current bytes and re-hashed
before this gate was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| final append-only design review | `notes/phase2_control_design_peer_review.md` | 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |

The final review preserves its original 488-line / 22,894-byte prefix exactly.
An independent byte read of that prefix gives SHA-256
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
Its current effective verdict is **REVISE — C0/M4/m0**, with the four open
findings `A-M1`, `A-M2`, `A-M3`, and `A-M4`.  The amendment-v1 self-audit is
not evidence against those findings.

The active proof/source ceiling was also re-locked on current bytes:

| Authority | Package-relative path | Lines | Bytes | SHA-256 | Effective state |
|---|---|---:|---:|---|---|
| Phase-1 source/precedent audit with v2 closure | `notes/phase1_source_precedent_audit.md` | 994 | 39122 | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | source-feasible, final closure `PASS C0/M0/m0` |
| integrated Phase-1 proof gate | `notes/phase1_final_gate.md` | 312 | 11102 | `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd` | proof authorization only |
| Phase-2 symbolic proof | `notes/phase2_wieferich_ulm_proofs.md` | 1127 | 44868 | `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355` | proof self-verdict `PASS C0/M0/m0` |
| independent proof review | `notes/phase2_wieferich_ulm_peer_review.md` | 712 | 32599 | `2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7` | `PASS C0/M0/m0`; Full Paper plausible |
| post-proof control-design gate | `notes/phase2_control_design_gate.md` | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | design authority only |

These proof/source records are boundary authority, not an authorization to
change a theorem, source claim, owner, Route, or publication state.  The
theorem owner remains the bare compact group `B_p`; universal prime recovery
remains `OPEN_NOT_AUTHORIZED`; Route B remains false.

## 2. Sole authorized amendment target and precedence

Exactly one new file may be created:

```text
notes/phase2_control_design_amendment_v2.md
```

It must bind the four exact current design records in the first table,
including the complete current review digest `b085df...`, and it must record
the proof/source ceiling without changing it.  The effective design after it
is frozen is:

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 at its externally computed final digest.
```

Amendment v2 may supersede only the clauses necessary to close `A-M1` through
`A-M4`.  It must identify each superseded base/v1 clause precisely.  Every
omitted base or v1 clause remains binding.  Amendment v2 must not embed its
own digest, claim that a finding is independently closed, or authorize any
implementation or execution.

## 3. A-M1 repair — unparameterized signature predicate and causal class derivation

For `S14`, `S15`, `S16`, and `S17`, the predicate name and callable interface
must be exactly the unparameterized symbol

```text
SG_SCOPE
```

The forms `SG_SCOPE(FINITE_COLLISION)`,
`SG_SCOPE(FINITE_PAIR_SEPARATION)`, `SG_SCOPE(FINITE_RANGE)`,
`SG_SCOPE(NO_INFINITE_EVIDENCE)`, or any equivalent supplied-class argument,
dispatch key, closure variable, registry field, or method metadata are
forbidden inputs to the semantic decision.

### 3.1 Primitive-only projection and output order

The amendment must freeze one exact typed primitive projection for each of
the four existing methods.  `SG_SCOPE` must, in this order:

1. parse only that projection;
2. independently recompute every `kappa_r(p)` used by the projection from
   the primitive primes and the frozen branch formulas;
3. validate any claimed distinguishing coordinate against the recomputed
   prefixes;
4. derive exactly one evidence class, or reject malformed/inconsistent
   primitive evidence before classification;
5. parse the proposed conclusion and decide whether that conclusion is
   licensed by the derived class; and
6. only after those computations compare the derived class with a
   method-owned expected-class assertion and, after substantive rejection,
   compare the derived detector with the expected detector.

The expected evidence class is therefore a post-computation assertion only.
It may not select a branch, supply a witness, license a conclusion, or select
a detector.  Persisted `kappa_prefix_p`, `kappa_prefix_q`,
`distinguishing_prime`, row IDs, row kinds, expected class, expected detector,
reason, oracle, status, and prior receipts cannot be roots of trust.  Any
persisted prefix or witness retained by the frozen CSV schema is checked
against the independently recomputed value only after recomputation.

The four derived-class rules remain exactly:

```text
recomputed equal prefixes for one named pair       -> FINITE_COLLISION
recomputed unequal prefixes with a valid coordinate -> FINITE_PAIR_SEPARATION
recomputed finite matrix over the finite registry  -> FINITE_RANGE
empty finite registry and no typed infinite witness -> NO_INFINITE_EVIDENCE
```

None is a global injectivity or universal-recovery conclusion.

### 3.2 Same-method primitive counterfactuals

Each of the same four existing semantic methods must run, after its ordinary
seed/mutation/inverse chain, one counterfactual while all expected-class,
detector, receipt, and method metadata remain byte-identical:

| Method | Exact primitive counterfactual | Required causal observation |
|---|---|---|
| `S14` | change only the primitive pair member `q:5 -> 3`; recompute both prefixes on `[2;3;5;7;11;13]` | the derived class changes from `FINITE_COLLISION` to `FINITE_PAIR_SEPARATION`, or the old collision conclusion rejects |
| `S15` | change only the proposed distinguishing coordinate `11 -> 13` while keeping primitive `p=2,q=3` | recomputation shows that 13 does not distinguish the pair and the seed rejects before any expected-class comparison |
| `S16` | change only the finite primitive registry `[2;3;5;7;11;13] -> []` | the finite-matrix class cannot remain `FINITE_RANGE`; the old finite-range seed rejects or derives `NO_INFINITE_EVIDENCE` |
| `S17` | change only the empty finite registry `[] -> [2]` | the class cannot remain `NO_INFINITE_EVIDENCE`; the old open-state seed rejects or derives `FINITE_RANGE` |

These are serial subfixtures inside the existing methods, not new semantic
rows, mutation classes, or test methods.  The amendment must make clear that
changing a supplied expected class cannot satisfy any of them.

## 4. A-M2 repair — independently sensitive receipt comparator

The real-filesystem receipt collection tests in amendment v1 remain binding:
the valid and malformed calls, recursive `lstat` walk including `.`, complete
path inventory, directories, type, mode, size, regular-file digest,
`mtime_ns`, `ctime_ns`, link count, device, and inode must all remain.
The ctime, transient-sidecar, and root variants also remain.

Within the existing `test_rep_010`, amendment v2 must additionally freeze two
pure comparator probes derived from one actually collected valid receipt:

1. deep-clone the complete receipt, change exactly one regular-file record's
   `mode` coordinate from its captured value to a distinct valid mode, leave
   every other coordinate of that record and every other record bit-for-bit
   identical, and require `E_VERIFY_ONLY_METADATA`;
2. independently deep-clone the same captured receipt, change exactly that
   record's `mtime_ns` by `+1000000000`, leave its `ctime_ns`, mode, size,
   digest, identity fields, and every other record exactly unchanged, and
   require `E_VERIFY_ONLY_METADATA`.

Before invoking the comparator, each probe must assert that the two receipt
objects differ in exactly the named `(relative_path, coordinate)` pair.  No
filesystem mutation, expected detector, or `ctime_ns` change may be used to
cause these two rejections.  A comparator which ignores `mode` or `mtime_ns`
must therefore fail `test_rep_010` even if it checks `ctime_ns`.  No method,
class, schema, artifact, or generated byte is added.

## 5. A-M3 repair — capability-retaining, replacement-safe cleanup

Amendment v2 must eliminate every identity-check-to-pathname-delete window.
Checking a pathname's inode and later unlinking or removing that pathname is
not an ownership proof, even if the interval is short, the mode is `0700`, or
the competing process has the same uid.

### 5.1 Mandatory cleanup property

For canonical generation roots, mutation generation roots, the exact P25
root and `occupied` member, the lock in `ACQUIRING`, and the lock transition
`OWNED -> CLEANING`, the amendment must freeze all of the following:

- the cleanup owner retains an independently verified directory capability
  from acquisition/creation through the final cleanup decision;
- deletion of a member is relative to the held owned directory capability,
  never by joining or reopening the external pathname;
- the fixed parent entry is resolved through a retained parent capability;
- replacement, disappearance, inode drift, token drift, or a parent-entry
  mismatch is fail-closed;
- a foreign replacement at the fixed name is never unlinked, removed,
  truncated, rewritten, chmodded, or otherwise treated as the owned object;
- the run never reports `ABSENT` merely because the fixed pathname is absent
  while the owned object survives at a displaced name; and
- success requires proof that the owned object and its owned members are
  gone and that no foreign object was deleted.

Closing a child FD before deleting its members, or retaining an FD while
performing the destructive operation through the pathname, does not satisfy
this property.  P25 must delete `occupied` relative to its still-held child
capability before that capability is released.  Lock `.owner` deletion must
be relative to the still-held verified lock capability.

### 5.2 Exact replacement falsifiers within existing methods

Without changing the 173-method or 28-package-class totals, amendment v2
must assign serial controlled-replacement subfixtures to existing lifecycle
methods and freeze their timing and expected state:

1. replace a canonical/mutation generation-root fixed parent entry after
   capability validation and before cleanup; the foreign replacement remains
   byte- and inode-identical, cleanup fails closed, and displaced owned state
   is reported rather than falsely declared absent;
2. in `test_package_p25_nonempty_generation_root`, replace the P25 fixed
   parent entry before cleanup; `occupied` is removed only from the held owned
   root, the foreign replacement is untouched, and fixed-entry drift is
   fail-closed;
3. in the existing acquisition-boundary lifecycle method, replace the lock
   fixed entry after the token-complete `CREATED` receipt while the wrapper is
   still `ACQUIRING`; the foreign replacement is untouched and the handler
   cannot report owned-lock absence while the owned directory survives; and
4. in that same state-machine class, replace the fixed entry immediately
   after `OWNED -> CLEANING`; the foreign `.owner` and directory remain
   byte- and inode-identical, no foreign deletion occurs, and the run fails
   closed with displaced owned state visible.

The two lock replacement timings are distinct mandatory subfixtures.  A
pre-existing-lock test before acquisition does not substitute for either.

### 5.3 Permitted atomic-possession alternative and disclosure rule

If the amendment demonstrates that the v1 path-based primitive cannot meet
the property above on the supported platform, it may supersede that primitive
with an equivalent atomic-possession mechanism.  The replacement must make
ownership transfer and the destructive right one indivisible operation, or
make all later destructive operations capability-relative inside an
exclusively possessed namespace.  It must never guess ownership from a token
read followed by pathname deletion.

Any such change must list completely:

```text
superseded v1 operations and state transitions
new acquisition/possession primitive and platform preconditions
creator, owner, capability/descriptor lifetime and inheritance
fixed-parent and child-member operation sequence
signal deferral and trap behavior in every state
success, ordinary-failure, injected-failure and replacement behavior
all detector/exit-class changes, if any
all new or removed operational-only environment/descriptor fields
cleanup, final-absence/displaced-state proof and nonserialization rules.
```

An unlisted operational-contract change is a new design finding.  The
alternative may not change any CSV, schema, generated path, manifest field,
aggregate, test-method name/count, package-class count, authority binding,
printed DAG node/edge, theorem, owner, Route, or publication boundary.

## 6. A-M4 repair — manifest-bound effective-amendment dereference

The final verifier must not trust a digest string copied into a review.  The
manifest-bound final review is the review file at the exact path and SHA-256
stored in the unchanged `design_review={path,sha256}` block after the v2
closure addendum has been appended.  Only after independently reading and
hashing that file may the verifier parse its amendment receipt.

The fresh v2 closure addendum must contain exactly one canonical block:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=<exact final v1 SHA-256>
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=<exact final v2 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

The final verifier must reject, before accepting lifecycle adjacency:

- a missing or second block;
- a count other than two;
- malformed, extra, duplicate, or unknown entries;
- either path appearing more than once;
- order other than v1 then v2;
- any path or digest differing from the canonical values recorded by the
  final closure review; or
- any read, regular-file, link, canonical-path, or SHA-256 mismatch when it
  independently opens and hashes both amendment files.

Parsing a copied digest without dereferencing both files is failure.  The
successful dereference becomes a mandatory internal validation obligation of
the existing review node `R`: adjacency validation stops unless
`R.effective_amendments=[v1,v2]` has been resolved on current bytes.  It does
not create an authority binding, generated artifact, manifest key, graph
node, or graph edge.  The manifest schema, authority-binding count 14, printed
eight lifecycle nodes, twelve distinct edges, and topological order
`A,D,R,G,I,C,M,V` remain unchanged.  If implementation of this rule would
change any of those frozen surfaces, amendment v2 must stop and report a new
design finding rather than silently widening the graph or schema.

## 7. Frozen invariants

Amendment v2 and its re-review must preserve exactly:

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TOLERANCE_POLICY=EXACT_ZERO
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The eight CSV paths and headers, all row values and row order, nine generated
paths, six implementation paths, 14 authority paths, manifest key set and
schema, 35 S-method names, 28 P-method names, 173 total method names, and all
theorem/owner ceilings remain binding.  No repair may manufacture a fifteenth
binding or a sixth lifecycle amendment node.

## 8. Mandatory fresh append-only re-review

After amendment v2 is frozen and externally hashed, a fresh independent
reviewer must read the complete effective tuple and append one closure
addendum to

```text
notes/phase2_control_design_peer_review.md
```

The complete current 49,358-byte / 1,017-line file at SHA-256
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`
must remain the exact prefix of that append.  This also preserves the nested
22,894-byte historical prefix at SHA-256 `3e180598...`.

The reviewer must independently attack, rather than restate:

1. all four unparameterized `SG_SCOPE` computations and their primitive
   counterfactuals;
2. the two exact-one-coordinate receipt-comparator probes, proving that
   `ctime_ns` cannot mask omitted mode or mtime comparison;
3. generation-root, P25, ACQUIRING, and `OWNED -> CLEANING` replacement
   subfixtures, including proof that foreign replacements are never deleted;
4. every operation changed by any atomic-possession alternative; and
5. the manifest-bound final-review parser, unique ordered v1/v2 list,
   independent amendment re-hashes, and unchanged 14-binding/8-node/12-edge
   lifecycle surface.

The fresh reviewer must include the canonical effective-amendment block in
Section 6 with both externally computed digests.  Only a final effective
verdict `PASS C0/M0/m0` can support consideration of a later implementation
gate.  A self-audit, partial closure, wording clarification, or unchanged
counterexample remains `REVISE`.

## 9. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V2=PASS_TO_ONE_AMENDMENT_V2
CURRENT_OPEN_FINDINGS=C0_M4_m0
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v2.md
AMENDMENT_V2_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V2_FROZEN=true
CURRENT_REVIEW_PREFIX_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
CURRENT_REVIEW_PREFIX_BYTES=49358

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
MANIFEST_SCHEMA_MUST_REMAIN_UNCHANGED=true
AUTHORITY_BINDING_COUNT_MUST_REMAIN_14=true
PRINTED_DAG_MUST_REMAIN_8_NODES_12_EDGES=true
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

This gate does not embed its own SHA-256.  Amendment v2 and the later fresh
independent re-review must bind this file's externally computed final digest.
No finding is closed by this authorization.
