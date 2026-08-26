# Replacement Paper 15: independent exact-byte deterministic-control design review

Status: **COMPLETE — INDEPENDENT FINAL-FROZEN-BYTE DESIGN REVIEW**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Verdict: **REVISE — C0/M3/m0**  
Control implementation or execution performed: **no**

## 1. Review object, method, and independence

I reviewed the complete current bytes of

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_lock.md
```

and independently recomputed its schemas, row registries, arithmetic,
finite-group models, mutation registries, method budget, package inventory,
authority bindings, manifest graph, reproduction identities, and failure
surfaces.  Its exact receipt is

```text
SHA-256: db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
lines:   1183
bytes:   62887
```

The authorizing gate was also read in full and re-hashed:

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_gate.md
SHA-256: 0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3
lines:   272
bytes:   10820
```

Both digests match the review instruction and the design's own bindings.  I
did not contact the design author and did not read author conversations.  I
treated the design self-audit, every persisted `PASS`, every expected reason
or detector, every summary total, and every copied digest as untrusted.

Before reviewing, I read the complete ARS academic-research-suite skill and
the complete experiment workflow, experiment reproducibility protocol,
code-runner integrity instructions, academic-pipeline workflow, integrity
review protocol, reproducibility audit, integrity-verification agent,
academic-paper-reviewer workflow, methodology reviewer, domain reviewer,
devil's-advocate reviewer, peer-reviewer, review template, and review-quality
instructions.  This report applies their exact-match, evidence/provenance,
independent-oracle, reproducibility, hostile-counterexample, and no-evidence-
gap standards.

No project generator, verifier, test suite, or reproduction wrapper was run.
The calculations below were independent read-only scratch calculations from
the primitive parameters, not execution or implementation of the proposed
controls.  No design, gate, proof, pipeline, Route, manuscript, release, or
Git artifact was edited.  This review is the only file written.

## 2. Complete stable-authority receipt

All fourteen manifest-authority records required by the gate and design were
read in full and independently hashed.  The indices are continuous, the
paths are distinct, and all fourteen current-byte digests match.

| # | Lines | Bytes | Recomputed SHA-256 | Result |
|---:|---:|---:|---|---|
| 1 | 196 | 9136 | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | MATCH |
| 2 | 325 | 15807 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | MATCH |
| 3 | 239 | 10192 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` | MATCH |
| 4 | 643 | 21817 | `02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb` | MATCH |
| 5 | 339 | 11832 | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | MATCH |
| 6 | 47 | 1705 | `811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722` | MATCH |
| 7 | 152 | 5441 | `2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc` | MATCH |
| 8 | 263 | 7745 | `386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80` | MATCH |
| 9 | 994 | 39122 | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | MATCH |
| 10 | 698 | 33279 | `5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae` | MATCH |
| 11 | 312 | 11102 | `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd` | MATCH |
| 12 | 1127 | 44868 | `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355` | MATCH |
| 13 | 712 | 32599 | `2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7` | MATCH |
| 14 | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | MATCH |

The tuple totals are 6,319 lines and 255,465 bytes.  In particular, the
symbolic proof and its independent peer review are stable upstream members;
neither is a concurrent output of the future control package.

## 3. Independent schema, row, mutation, and method reconciliation

I split each literal header on commas rather than trusting the stated width.
Every header token is unique.  I separately enumerated the defining row IDs,
the negative-row-to-mutation bijection, and both mutation registries.

| CSV | Recomputed columns | Recomputed body rows | Negative rows | Semantic classes |
|---|---:|---:|---:|---:|
| `valuation_normalization_controls.csv` | 18 | 16 | 4 | 4 |
| `exponent_order_branch_controls.csv` | 19 | 14 | 2 | 2 |
| `finite_kernel_truncation_controls.csv` | 22 | 18 | 4 | 4 |
| `torsion_closure_type_controls.csv` | 17 | 10 | 3 | 3 |
| `signature_nonpromotion_controls.csv` | 16 | 12 | 4 | 4 |
| `owner_firewall_controls.csv` | 19 | 15 | 9 | 9 |
| `proof_ceiling_controls.csv` | 13 | 26 | 9 | 9 |
| `target_summary.csv` | 10 | 9 | 0 | 0 |
| **Total** | mixed | **120** | **35** | **35** |

The independent arithmetic is

```text
body rows = 16+14+18+10+12+15+26+9 = 120
negatives = 4+2+4+3+4+9+9+0 = 35
header widths = 18,19,22,17,16,19,13,10
```

The row registries are exactly the continuous sets `VC-001..016`,
`EO-001..014`, `FK-001..018`, `TC-001..010`, `SG-001..012`,
`OF-001..015`, `PC-001..026`, and `TS-001..009`.  The 35 `S01..S35`
entries have 35 distinct negative rows, 35 distinct reason tokens, and 35
distinct method names.  The 28 `P01..P28` entries have 28 distinct method
names and 28 registered detector tokens.  Repeated semantic detector classes
such as `E_ROOT_NOT_IN_KERNEL` and `E_RECOVERY_CEILING` do not collapse the
distinct mutation inputs.

The ten fixed nonmutation method families contribute

```text
10+10+14+9+10+12+12+5+18+10 = 110 methods.
```

Adding the 35 semantic and 28 package methods gives exactly

```text
110+35+28 = 173 independently named test_* methods.
```

All 173 names are distinct, and `test_pkg_018` is itself included in that
set.  No loop or subtest was counted as more than one method.

The Section-3 path inventory independently yields eight CSVs plus one
manifest, hence nine generated artifacts, and six separate implementation
paths.  The reproduction contract names exactly two canonical fresh roots,
three copies (checked-in, A, B), three pairwise relations, and 27 file-level
comparisons across the nine generated artifacts.  Mutation-fixture copies
are explicitly outside those canonical identity counts.

The completion rule in Section 6 makes every still-unassigned CSV field
empty, so the eight CSV schemas do not leave a competing byte serialization.
The manifest's future lifecycle and implementation digests are deliberately
parameters supplied only after their stable files exist; its key set, path
values, value types, array order, and canonical JSON serialization are
otherwise determined.  I found no generated-byte ambiguity or stale count.

## 4. Independent arithmetic and finite-model recomputation

### 4.1 Valuations and factorizations

Starting only from the primitive `(p,r)` pairs and the three branch formulas,
repeated division and independent trial factorization give, in `VC-001`--
`VC-012` order:

```text
3       = 3                  v_3=1, kappa=0
24      = 2^3*3              v_3=1, kappa=0
2400    = 2^5*3*5^2          v_5=2, kappa=1
2808    = 2^3*3^3*13         v_3=3, kappa=2
1023    = 3*11*31            v_11=1, kappa=0
59048   = 2^3*11^2*61        v_11=2, kappa=1
8       = 2^3                v_2=3, kappa=0, sign=-1
24      = 2^3*3              v_2=3, kappa=0, sign=1
48      = 2^4*3              v_2=4, kappa=1, sign=-1
288     = 2^5*3^2            v_2=5, kappa=2, sign=1
diagonal (2,2): kappa=0
diagonal (3,3): kappa=0
```

The four negative rows independently fail, respectively, the branch-domain,
odd-minus-one, two-minus-three, and local-two-sign predicates.  The displayed
factorizations and all positive depths are correct.

### 4.2 Multiplicative orders and the withdrawn diagonal route

Independent repeated modular multiplication gives the nonempty orders

```text
EO-001,003..014:
2,2,4,3,3,18,10,100,6,4,8,8,18.
```

Factoring `ell-1` and minimizing the candidate order by its prime factors
reproduces every displayed value and both exact valuations.  In particular,

```text
ord_17(2)=8, v_2(17-1)=4, v_2(ord_17(2))=3.
```

Characters of `C_16` of order at most eight are indexed by the eight even
residues modulo 16.  Their restrictions to the displayed `C_8` subgroup have
only the four even residues modulo 8.  The bounded image therefore has order
four, not eight, so `S05` correctly rejects the withdrawn surjectivity route.
For `S06`, `(p,r,m,ell)=(2,3,1,19)` has both valuations equal to two, not
one; divisibility does not imply the claimed exact depth.

### 4.3 Kernels, heights, tails, and internal roots

I exhaustively enumerated each finite source group and recomputed the kernel
and every set `r^d K`, without using the displayed kernel or height values.

| Row | Kernel order | Recomputed `|r^d K|`, `d=0..N` |
|---|---:|---|
| `FK-001` | 4 | `[4;1;1;1]` |
| `FK-002` | 81 | `[81;9;1;1]` |
| `FK-003` | 16 | `[16;2;1;1]` |
| `FK-004` | 81 | `[81;3;1;1]` |
| `FK-005` | 64 | `[64;8;2;1]` |
| `FK-006` | 128 | `[128;16;4;2]` |
| `FK-007` | 256 | `[256;32;8;4]` |
| `FK-008` | 27 | `[27;3;1]` |
| `FK-009` | 81 | `[81;9;3]` |
| `FK-010` | 243 | `[243;27;9]` |

Thus the six Phi tails have orders `1,2,4,1,3,9`, exactly `r^kappa`.
Direct coordinate arithmetic gives

```text
FK-011..014: Phi(root)=0 and r^depth*root=tail;
FK-015..018: Phi(root)=4,2,3,1 respectively, all nonzero.
```

All four positive roots are internal to the kernel, and all four ambient-only
roots fail the kernel equation even though their scalar multiple is the tail.
No finite row implies an infinite-height or Ulm theorem.

### 4.4 Signatures, finite dual orders, and owner swaps

Direct branchwise valuation on the frozen prefix `[2;3;5;7;11;13]` gives

```text
p=2:  [0;0;0;0;0;0]
p=3:  [0;0;0;0;1;0]
p=5:  [0;0;0;0;0;0]
p=7:  [1;0;1;0;0;0]
p=11: [0;0;0;0;0;0]
p=13: [0;0;0;0;0;0].
```

At `r=11`, the independently recomputed pair is `(0,1)`, so only the stated
`B_2`/`B_3` separation is licensed.  The `p=2`/`p=5` finite-prefix collision
has no global consequence.

Finite annihilator duality reproduces the six tail/quotient order pairs
`1,2,4,1,3,9`.  The symbolic closure identity remains a proof-bound type
receipt, not a result of the finite models.  Raw torsion, torsion closure,
the discrete infinite-height tail, and its compact annihilator-side owner
remain distinct.

Exhaustive enumeration of the two swap matrices on `C_25^2` and `C_9^2`
gives 625/625 and 81/81 distinct images, preserves addition and every element
order, and swaps the two labelled basis elements.  The determinants are
`-1 mod 5=4` and `-1 mod 3=2`.  The bare finite blocks are unchanged while
the labels move, so no marked, ambient, actual, measured, trace, operator, or
determinant owner promotion follows.

## 5. Manifest and lifecycle audit

The canonical manifest has twelve top-level keys, fourteen ordered authority
objects, three separate lifecycle bindings, six ordered implementation
objects, eight ordered CSV artifact objects, sixteen aggregate keys, and no
manifest object in its own artifact array.  All paths are typed as either
repository-relative authority paths or package-relative lifecycle/package
paths according to the frozen rule.

Reconstructing the lifecycle as a simple directed graph gives eight nodes
and twelve distinct edges:

```text
A->D, D->R, R->G, G->I, I->C, C->M, M->V,
A->M, D->M, R->M, G->M, I->M.
```

The separately printed `C->M` binding is the same edge already present in
the chain, not a second semantic edge.  The unique topological order is

```text
A,D,R,G,I,C,M,V.
```

There is no `M->M`, no `V->M`, no unknown node, and no cycle.  The stable
symbolic proof is authority node `A`; it is neither generated concurrently
nor back-filled.  The future result review binds `M`, while `M` does not bind
that review.  The summary self-row carries counts only.  Manifest self-hash,
summary self-hash, concurrent-proof hash, and future-result edges are absent.

## 6. Hostile oracle and package attacks

The independent arithmetic representations are materially different from
the proposed subject representations: direct factorization versus fresh
factor-and-multiply-back; repeated orders versus factor-reduced orders;
elimination versus exhaustive group enumeration; multiplication of a subject
kernel versus fresh-set enumeration; determinant calculation versus full
finite-block bijection/group-law enumeration; and subject counters/hashes
versus parsed inventory and independent byte reads.  The oracle is forbidden
to import the subject or a shared helper.  These positive-oracle surfaces are
adequately independent.

Raw CSV semantics precede summary and manifest validation.  Persisted row
`status`, `mutation_id`, `negative_reason`, and `oracle` are explicitly
falsified in semantic methods; artifact hashes, summaries, manifest totals,
and manifest `status=PASS` cannot validate raw arithmetic.  The finite-to-
infinite, all-prime, owner, Route-B, source-receipt, and proof ceilings are
separate exact negative classes.  Package mutations cover structural tamper,
missing/extra/order/count, bindings, links, caches, recursion, concurrency,
repair, cleanup, future edges, metadata, and canonical-byte failures.  The
serial variants inside `P27` and `P28` share one declared class and detector
and do not change the 28-class count.

Three blocking acceptance surfaces nevertheless remain.  They are detailed
below.

## 7. Findings and minimum repair contracts

### M1 — Semantic-negative causality can be satisfied by row-token lookup

**Location:** Sections 1, 5, and 7, especially lines 54--56, 221--226, and
680--724; the policy negatives in Sections 6.4--6.7.

The design correctly says that expected fields are not roots of trust, but
the frozen negative-test procedure falsifies only `mutation_id`,
`negative_reason`, `oracle`, and `status`.  It leaves `row_id` and
`case_kind=NEGATIVE` available, explicitly gives the oracle its own hard-
coded mutation registry, and does not require a valid seed to pass before the
substantive mutation, canonical serialization and reparse after mutation, or
acceptance after correction.

Consequently, the frozen test procedure cannot distinguish a substantive
oracle from the following prohibited implementation shape:

```text
if case_kind == NEGATIVE:
    return detector_by_row_id[row_id]
```

That implementation ignores all four falsified fields, returns the detector
expected by the independent method registry, detects each row exactly once,
and can make all 35 methods pass without the invalid arithmetic, root,
closure/type, signature, owner, or proof-ceiling predicate being the cause.
The broad prose command to recompute would prohibit this implementation, but
the locked construction/test sequence does not discriminate it.  For the
policy families in particular, no typed parser/predicate is frozen in place
of token membership.  This is exactly the supplied-detector/token-lookup
acceptance surface that the gate requires the design review to attack.

**Minimum repair contract:** issue a versioned design amendment which, for
each `S01..S35`, freezes (1) a primitive valid seed independent of the
negative row label; (2) successful independent evaluation of that seed; (3)
one exact substantive mutation; (4) canonical serialization and independent
reparse; (5) an oracle projection which excludes `row_id`, `case_kind`, all
expected/detector fields, and all persisted receipts from the semantic
decision; (6) arithmetic recomputation or a closed typed policy predicate;
(7) rejection before detector emission; and (8) acceptance after undoing the
mutation.  The method registry may compare the returned detector only after
that decision.  The torsion/type, signature, owner, and proof-ceiling
families need exact parsed operator/owner/quantifier transition rules, not
substring, reason-token, or row-ID lookup.  This repair can retain 35 rows,
35 semantic methods, and the total of 173 methods.

### M2 — The verify-only proof does not observe prohibited metadata writes

**Location:** Section 12, especially lines 989--990 and 1041--1046; package
mutation `P23` and the reproduction method budget.

`--verify-only` is expressly forbidden to chmod or touch an input, yet its
read-only test snapshots only bytes before and after.  Modes `0444` and
`0555` do not close this surface: the file owner may change mode and
timestamps, and uid 0 may write despite the permission bits.  A verifier can
therefore chmod a result, touch a result or directory, or create and remove a
sidecar, leave every sampled byte identical, and satisfy the frozen test.
`P23` proves only that the reserved `--repair` flag is rejected; it does not
exercise ordinary verify-only metadata behavior.  Thus
`verify_only_read_only=true` can be accepted while the promised state
invariant is false.

**Minimum repair contract:** freeze an operational, nonserialized, recursive
before/after `lstat` receipt for the complete isolated repository read set,
including the input directory itself.  At minimum it must bind relative path,
entry type, mode, size, byte digest, `mtime_ns`, `ctime_ns`, link count,
device, and inode; inventory and receipt must match exactly after both valid
and malformed verify-only calls.  Directory metadata must participate so a
transient create/unlink is visible.  The receipt must be used even under uid
0, and detector output must not expose its absolute root.  Assign an existing
`test_rep_*` method to an explicit metadata-mutation falsifier or otherwise
freeze an equally strong write-observation mechanism.  No method-count or
generated-byte change is required.

### M3 — The output-root and lock-cleanup state machine is not closed

**Location:** Sections 10 and 12, especially lines 793--799, 827, 845,
981--1002, 1027--1033, 1048--1060, and 1068--1095.

Generation mode must refuse every path outside a wrapper-created temporary
root.  Yet its only frozen input is `--output-dir`; no exact capability or
environment handoff tells the generator which dynamic roots the wrapper
created.  At the same time `P25` must pre-create `occupied` in a method-owned
synthetic output directory and reach `E_NONEMPTY_OUTPUT`.  That directory is
not one of canonical A/B, and A/B are passed to the test suite read-only.
Using A or B would violate the three-root contract; using the method-owned
root must be rejected as outside the wrapper roots before its nonempty state
can supply the promised detector.  The design also says mutation-fixture
generations exist outside the exact two canonical generations without
freezing their root authorization channel.

The same state machine promises cleanup on every catchable signal but does
not freeze when an ownership-aware trap is armed relative to atomic `mkdir`.
Arming an unconditional trap before acquisition can remove another process's
pre-existing lock; arming it only after acquisition leaves a signal window
that can strand the owned lock.  `P24` tests one later forced-failure point,
not this acquisition/ownership transition.

**Minimum repair contract:** freeze one exact nonserialized root-capability
handoff and its validation order.  Either add a third, fully validated test-
context injection in which a copied wrapper creates an authorized root,
creates exactly `occupied`, invokes generation, obtains
`E_NONEMPTY_OUTPUT`, and cleans up, or define an equivalent exact capability
for a uid-owned nonsymlink mode-`0700` method root.  State which root and
which validation phase `P25` uses; outside-root rejection must not mask its
nonempty detector.  Separately freeze the lock state variables, trap arming,
successful-acquisition ownership transition, signal deferral/handling,
explicit success cleanup and absence checks, and failure fallback so that a
process removes only a lock it acquired.  All temporary capabilities and
paths remain operational only and must never be serialized or printed.  The
28 package classes and 173 methods may remain unchanged.

## 8. Severity register and gate consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no arithmetic, finite-group, source-binding, owner, or manifest-cycle collapse found |
| Major (`M`) | 3 | all three acceptance surfaces require a versioned design amendment and independent re-review before implementation |
| Minor (`m`) | 0 | none |

The exact arithmetic, schemas, counts, stable authority tuple, finite versus
infinite ceilings, owner firewalls, and acyclic manifest are coherent.  They
do not cure the three experiment-integrity gaps above.  Under the gate's own
rule that an acceptance surface or ambiguity is blocking, the current digest
is not implementation-ready.

```text
REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v1.0
REVIEW_INDEPENDENT_OF_DESIGN_AUTHOR_DIALOGUE=true
ARS_METHODS_READ_IN_FULL=true
REVIEWED_GATE_SHA256=0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3
REVIEWED_DESIGN_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
ARITHMETIC_AND_FINITE_MODELS=PASS
GENERATED_BYTE_CONTRACT=PASS
SEMANTIC_NEGATIVE_CAUSALITY=REVISE
VERIFY_ONLY_METADATA_INTEGRITY=REVISE
OUTPUT_ROOT_LOCK_CLEANUP_STATE_MACHINE=REVISE
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=3
MINOR_FINDINGS=0
OVERALL_REVIEW_VERDICT=REVISE_C0_M3_m0
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Final disposition on the specified frozen design bytes: **REVISE — C0/M3/m0**.
No implementation or execution is authorized on this digest.  A bounded,
versioned amendment satisfying M1--M3 must be re-hashed and independently
reviewed from scratch before an implementation gate may be considered.

---

# Closure addendum: independent exact-byte re-review of amendment v1

Status: **COMPLETE — APPEND-ONLY AMENDED-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v1.1`  
Date: 2026-08-16 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M4/m0**  
Control implementation or execution performed: **no**

## A1. Append-only scope, exact tuple, and independence

Before this addendum was written, the complete original review was still
exactly 488 lines and 22,894 bytes with SHA-256
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
The complete 22,894-byte prefix is historical evidence and is not superseded,
rewritten, or normalized by this addendum.

I independently re-read the complete bytes of the effective-design tuple:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| original review prefix `notes/phase2_control_design_peer_review.md` | 488 | 22894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` | MATCH |
| remediation gate `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` | MATCH |
| amendment v1 `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |

The amendment's three embedded authority receipts match the first three
records exactly.  I did not contact the amendment author, did not inspect an
author dialogue, and did not use the amendment self-audit as evidence.  I
treated every `CLOSED_BY_DESIGN`, count, expected detector, typed-class label,
and transitive-binding assertion as an untrusted claim to be attacked.

Before the re-review, I again read in full the ARS academic-research-suite
skill; experiment workflow, reproducibility protocol, and code-runner
integrity instructions; academic-pipeline workflow, integrity protocol,
reproducibility audit, and integrity-verification instructions; and the
academic-paper-reviewer workflow, methodology, domain, devil's-advocate,
peer-reviewer, report-template, and review-quality instructions.  This
closure applies their independent-oracle, causal-falsifier, exact-byte,
provenance, hostile-counterexample, and pressure-resistant severity rules.

No project generator, verifier, wrapper, test suite, or control was
implemented or executed.  The calculations below were read-only independent
scratch recomputations from the printed primitives.  No base design,
amendment, gate, pipeline, implementation, proof, Route, manuscript, release,
or Git artifact was changed.

## A2. Independent invariant and arithmetic reconciliation

### A2.1 Stable bindings, schemas, rows, and methods

I reparsed the base Section-2 table rather than copying its totals, read all
fourteen current paths, and hashed their complete bytes.  The indices are
exactly `1..14`, all paths are distinct, all fourteen digests match, and the
tuple totals remain 6,319 lines and 255,465 bytes.

Splitting the eight literal headers on commas again gives:

| CSV family | Columns | Body rows | Negative rows | Semantic classes |
|---|---:|---:|---:|---:|
| `VC` | 18 | 16 | 4 | 4 |
| `EO` | 19 | 14 | 2 | 2 |
| `FK` | 22 | 18 | 4 | 4 |
| `TC` | 17 | 10 | 3 | 3 |
| `SG` | 16 | 12 | 4 | 4 |
| `OF` | 19 | 15 | 9 | 9 |
| `PC` | 13 | 26 | 9 | 9 |
| `TS` | 10 | 9 | 0 | 0 |
| **Total** | mixed | **120** | **35** | **35** |

Every header token is unique.  The row sets are exactly the continuous
registries `VC-001..016`, `EO-001..014`, `FK-001..018`, `TC-001..010`,
`SG-001..012`, `OF-001..015`, `PC-001..026`, and `TS-001..009`.

The base semantic registry and the amendment registry each contain exactly
`S01..S35`; the 35 persisted-row bindings are distinct and agree pairwise,
and every amendment detector agrees with its base detector.  Repeated typed
detectors for the four root failures and the two recovery ceilings do not
collapse the 35 distinct methods.  The package registry remains exactly
`P01..P28`, with 28 distinct method names and 28 registered P-detectors.

The method arithmetic independently remains

```text
fixed families = 10+10+14+9+10+12+12+5+18+10 = 110
all methods    = 110+35+28 = 173
```

The generated inventory is still eight CSVs plus `manifest.json`, or nine
generated artifacts.  The canonical reproduction identities are still two
fresh generations A/B and three copies checked-in/A/B.  The amendment's
method-owned mutation roots are excluded from both counts by purpose and are
never accepted as `fresh-a` or `fresh-b`.

### A2.2 Fresh mathematical recomputation

Repeated division gives the ten non-diagonal valuation/depth pairs, in base
row order,

```text
(v_r,kappa) = (1,0),(1,0),(2,1),(3,2),(1,0),(2,1),
              (3,0),(3,0),(4,1),(5,2).
```

The recomputed factorizations remain

```text
3; 2^3*3; 2^5*3*5^2; 2^3*3^3*13; 3*11*31;
2^3*11^2*61; 2^3; 2^3*3; 2^4*3; 2^5*3^2.
```

Independent modular multiplication gives the thirteen nonempty base orders

```text
2,2,4,3,3,18,10,100,6,4,8,8,18.
```

In particular, `ord_17(2)=8` and `v_2(16)=4`.  Enumerating the eight
order-at-most-eight characters of `C_16` and restricting them to the printed
`C_8` gives four images, not eight.

Exhaustive enumeration of the ten finite maps again gives:

| Model | Kernel order | `|r^d K|`, `d=0..N` |
|---|---:|---|
| `FK-001` | 4 | `[4;1;1;1]` |
| `FK-002` | 81 | `[81;9;1;1]` |
| `FK-003` | 16 | `[16;2;1;1]` |
| `FK-004` | 81 | `[81;3;1;1]` |
| `FK-005` | 64 | `[64;8;2;1]` |
| `FK-006` | 128 | `[128;16;4;2]` |
| `FK-007` | 256 | `[256;32;8;4]` |
| `FK-008` | 27 | `[27;3;1]` |
| `FK-009` | 81 | `[81;9;3]` |
| `FK-010` | 243 | `[243;27;9]` |

The four amended valid root seeds have `Phi(root)=0` and scalar multiple
equal to the tail.  Their sole post-images keep the scalar equality but have
`Phi(root)=4,2,3,1`, respectively.  Direct recomputation of the six signature
prefixes remains

```text
p=2  [0;0;0;0;0;0]
p=3  [0;0;0;0;1;0]
p=5  [0;0;0;0;0;0]
p=7  [1;0;1;0;0;0]
p=11 [0;0;0;0;0;0]
p=13 [0;0;0;0;0;0].
```

Full enumeration of the swaps on `C_25^2` and `C_9^2` gives 625 and 81
distinct images, preserves addition and element order, swaps the labels, and
has determinant `4 mod 5` and `2 mod 3`.  These recomputations reveal no new
arithmetic, finite-model, owner, or theorem-ceiling error.

### A2.3 Manifest graph and Route ceiling

Deduplicating the separately printed `C->M` occurrence again gives eight
nodes and twelve edges:

```text
A->D, D->R, R->G, G->I, I->C, C->M, M->V,
A->M, D->M, R->M, G->M, I->M.
```

The unique topological order is `A,D,R,G,I,C,M,V`; no self edge, `V->M`,
unknown node, concurrent-proof edge, or cycle appears in that printed graph.
The schemas, aggregate keys, generated paths, and manifest no-self and
no-future-result rules are unchanged.  `UNIVERSAL_RECOVER_P` remains
`OPEN_NOT_AUTHORIZED`, Route B remains false, and no control result can
authorize Route A, composition, or manuscript work.  Section A6 identifies
a separate missing effective-design byte dependency; it does not turn the
printed graph cyclic.

## A3. M1 causal-negative re-review

### A3.1 Complete 35-chain ledger

I independently applied every printed forward operation to its seed, checked
the changed-field footprint and persisted-row projection, evaluated the
closed rule from the printed primitive data, and applied the printed inverse.
The ledger is:

| ID | Independent seed result | Sole post-image result | Inverse result |
|---|---|---|---|
| `S01` | diagonal domain accepts `(3,3)` | off-local branch at `p=r` rejects | exact diagonal seed accepts |
| `S02` | `v_5(2400)=2`, normalizer 1 gives 1 | normalizer 0 / `kappa=2` rejects | normalizer 1 / `kappa=1` accepts |
| `S03` | `v_2(48)=4`, normalizer 3 gives 1 | normalizer 2 / `kappa=2` rejects | normalizer 3 / `kappa=1` accepts |
| `S04` | `(p,r)=(3,2)` requires sign `-1` | empty sign rejects | `-1` accepts |
| `S05` | bounded restriction image has order 4 | `SURJECTIVE` rejects | `NOT_SURJECTIVE` accepts |
| `S06` | both valuations at `(2,3,1,19)` equal 2 | `IMPLIES exact m=1` rejects | `DOES_NOT_IMPLY` accepts |
| `S07` | internal root has scalar tail and `Phi=0` | ambient root has `Phi=4` | exact internal root accepts |
| `S08` | internal root has scalar tail and `Phi=0` | ambient root has `Phi=2` | exact internal root accepts |
| `S09` | internal root has scalar tail and `Phi=0` | ambient root has `Phi=3` | exact internal root accepts |
| `S10` | internal root has scalar tail and `Phi=0` | ambient root has `Phi=1` | exact internal root accepts |
| `S11` | parsed `ann(closure(Tor(...)))` has correct types | removing `closure` gives invalid operand | exact AST restoration accepts |
| `S12` | finite model `DOES_NOT_PROVE` infinite theorem | `PROVES` contradicts authority | polarity inverse accepts |
| `S13` | reversed correct annihilator equality type-checks | deleting `ann` equates discrete and compact types | exact AST inverse accepts |
| `S14` | recomputed `p=2,5` prefixes collide finitely | group-isomorphism promotion rejects | `NO_GLOBAL_CONCLUSION` accepts |
| `S15` | recomputed pair separates only at printed finite coordinate | universal recovery rejects | exact pair conclusion accepts |
| `S16` | six-by-six recomputation is a finite range only | global injectivity rejects | `FINITE_RANGE_ONLY` accepts |
| `S17` | no infinite evidence leaves map open | known-injective declaration rejects | `OPEN_NOT_AUTHORIZED` accepts |
| `S18` | marked-to-marked owner identity accepts | marked-to-bare transfer rejects | identity accepts |
| `S19` | ambient-to-ambient owner identity accepts | ambient-to-bare transfer rejects | identity accepts |
| `S20` | actual-to-actual owner identity accepts | actual-to-bare transfer rejects | identity accepts |
| `S21` | flow-to-flow owner identity accepts | flow-to-bare transfer rejects | identity accepts |
| `S22` | bare-to-bare owner identity accepts | unlicensed Haar-owner transfer rejects | identity accepts |
| `S23` | bare-to-bare owner identity accepts | unlicensed measured-owner transfer rejects | identity accepts |
| `S24` | bare-to-bare owner identity accepts | unlicensed trace-owner transfer rejects | identity accepts |
| `S25` | bare-to-bare owner identity accepts | unlicensed operator-owner transfer rejects | identity accepts |
| `S26` | bare-to-bare owner identity accepts | unlicensed determinant-owner transfer rejects | identity accepts |
| `S27` | `GRH_NONPROMOTION` agrees with authority | `GRH_PROMOTION` rejects | exact polarity inverse accepts |
| `S28` | `DENSITY_NONPROMOTION` agrees with authority | `DENSITY_PROMOTION` rejects | exact polarity inverse accepts |
| `S29` | `ABSOLUTE_PRIORITY_NONPROMOTION` agrees | promotion rejects | exact polarity inverse accepts |
| `S30` | `ROUTE_B_NONPROMOTION` agrees with `false` | promotion rejects | exact polarity inverse accepts |
| `S31` | recovery nonpromotion agrees with open state | promotion rejects | exact polarity inverse accepts |
| `S32` | finite control is not symbolic proof | `AS` relation rejects | `NOT_AS` inverse accepts |
| `S33` | source receipt is not executed theorem | `AS` relation rejects | `NOT_AS` inverse accepts |
| `S34` | finite control is not Chebotarev proof | `AS` relation rejects | `NOT_AS` inverse accepts |
| `S35` | finite control is not Ulm proof | `AS` relation rejects | `NOT_AS` inverse accepts |

All 35 rows print a seed, one declared forward operator, an exact
changed-field set, an inverse, and the base detector.  The common projection
excludes `row_id`, `case_kind`, `mutation_id`, reason, oracle, status,
detector, and receipts; schema-specific receipt exclusions are also explicit.
The chain requires independent CSV reparse before the predicate, rejection
before detector translation, byte-identical recovery, and inverse acceptance.
The `row_id` and `case_kind` counterfactuals therefore close the original
literal row-ID and `case_kind=NEGATIVE` lookup example.

One different supplied-class bypass remains.

### A-M1 — `SG_SCOPE` is parameterized by the evidence class it is required to derive

**Severity:** Major  
**Evidence anchor:** text: amendment lines 297--320 and 407--410
"`SG_SCOPE` recomputes every supplied prefix" / "`SG_SCOPE(FINITE_COLLISION)`"  
**Confidence:** 5/5 — direct deterministic predicate-interface analysis

Section 4.5 defines unparameterized `SG_SCOPE` as recomputing prefixes and
*classifying* the evidence.  The exact registry's predicate column instead
names `SG_SCOPE(FINITE_COLLISION)`,
`SG_SCOPE(FINITE_PAIR_SEPARATION)`, `SG_SCOPE(FINITE_RANGE)`, and
`SG_SCOPE(NO_INFINITE_EVIDENCE)`.  Under Section 3.1, `P_i` is the predicate
"named in the same registry row"; the parenthesized value is therefore an
implementation input or, at minimum, an unresolved exact-interface
ambiguity, not a harmless prose heading.

The following prohibited oracle passes all four printed seed/post/inverse
chains and every receipt-field falsifier:

```text
take the registry-supplied evidence class;
select that class's licensed conclusion;
accept the seed conclusion, reject the post conclusion;
never recompute p, q, either prefix, the six-by-six matrix, or the witness.
```

The persisted projection-equality check does not cure this: it proves which
bytes were supplied, not that `SG_SCOPE` used them.  This is a derived
expected-class lookup outside the excluded CSV fields.  Four of 35 causal
predicates can therefore go green without the promised primitive
recomputation, so original M1 is not closed.

**Minimum repair contract:** make the registry predicate exactly the
unparameterized `SG_SCOPE` for `S14..S17`.  The evidence class must be an
output derived solely from the typed projection.  If an expected class is
retained as a test assertion, compare it only after recomputation, alongside
the post-rejection detector.  Add a same-method counterfactual which changes
a primitive prefix/witness while keeping any method metadata fixed and
requires the recomputed class to change or the seed to reject.  Counts and
generated bytes need not change.

## A4. M2 recursive receipt re-review

The amendment does freeze a whole-synthetic-root walk starting at `.`, with
unsigned-UTF-8 relative-path order and the exact record

```text
(path,type,mode,size,sha256-or-empty,mtime_ns,ctime_ns,
 nlink,dev,ino).
```

It includes all intermediate directories, rejects non-regular/non-directory
types, compares exact path sets and every tuple field after either exit
status, excludes only access time, keeps the receipt in memory, covers uid 0,
and forbids absolute-root diagnostics.  The valid and malformed calls are
separate and the malformed fixture is byte-exact.  Those clauses repair the
base byte-only snapshot itself.

The five falsifiers, however, do not prove the comparator is sensitive to
the selected fields.

### A-M2 — mode and mtime falsifiers are causally confounded by `ctime_ns`

**Severity:** Major  
**Evidence anchor:** text: amendment lines 504--524
"exactly the stated non-byte surface is changed" / "falsifies mode-only, timestamp-only"  
**Confidence:** 5/5 — filesystem metadata and mutation-test causality

Changing mode `0444 -> 0644` also changes inode `ctime_ns`.  Setting
`mtime_ns` also changes `ctime_ns`.  The amendment's separate ctime variant
requires the comparator to notice `ctime_ns`; the root chmod and transient
create/unlink variants likewise normally change ctime.  Consequently, this
defective implementation satisfies the valid/malformed checks and all five
falsifiers:

```text
compare inventory and ctime_ns;
ignore mode and mtime_ns completely.
```

Each selected field did change, as lines 518--520 require, but `ctime_ns`
alone supplies every rejection.  Thus the action called "mode" does not
falsify an omitted-mode comparator, and the action called "mtime" does not
falsify an omitted-mtime comparator.  This directly misses the remediation
gate's selected-field mode-only and timestamp-only proof.  Original M2 is
not closed.

**Minimum repair contract:** retain the real-filesystem variants to test
receipt collection, and within the same `test_rep_010` add comparator-level
counterfactuals from one actual captured receipt: clone it, change exactly
the `mode` coordinate in one record and no other tuple member, and require
rejection; repeat for exactly `mtime_ns`.  Keep the existing ctime,
transient-sidecar, and root variants.  The method, class, artifact, and byte
counts remain unchanged.

## A5. M3 capability, P25, signal, and cleanup re-review

The generation preflight is substantially stronger than the base design.
It requires the directory FD plus canonical uid/device/inode/purpose receipt,
checks FD and path identity before emptiness, enumerates and writes relative
to the held descriptor, and gives P25 an authorized
`MUTATION_P25_V1` root containing exactly the zero-byte mode-0600
`occupied`.  The purpose grammar expands to P01--P26 variant 1, five P27
variants, and two P28 variants, while A/B alone remain canonical.  P25
therefore reaches `E_NONEMPTY_OUTPUT` after capability validation rather than
being masked by outside-root rejection.

The acquisition half of the lock protocol also installs traps before
`ACQUIRING`, gives the helper the token before `mkdir`, blocks handled signals
through durable `.owner` creation, distinguishes `PREEXISTING` from
`CREATED`, and assigns `test_rep_009` both the first observable signal
boundary and a pre-existing foreign-lock fixture.  These clauses close the
original tokenless acquisition window.  The cleanup half is not equivalently
capability-bound.

### A-M3 — cleanup drops the held capability and separates identity check from pathname deletion

**Severity:** Major  
**Evidence anchor:** text: amendment lines 618--650 and 711--761
"closes the generation descriptor" / "unlink exactly `.owner`, `rmdir` exactly the validated lock directory"  
**Confidence:** 5/5 — directory-FD and concurrent cleanup state analysis

For generation roots, the creator closes the descriptor after the child and
later performs path validation followed by path removal; P25 expressly
closes the descriptor before unlinking `occupied`.  For the external lock,
the helper closes the owner and lock-directory descriptors, the handler
validates token/device/inode in `ACQUIRING` or `OWNED`, changes state to
`CLEANING`, and only then performs pathname `unlink` and `rmdir`.

There is no held directory capability across either check/delete sequence.
For the lock, a same-UID process can deterministically exercise the gap:

1. let the owner validate the original lock and enter `CLEANING`;
2. rename the owned directory away and install a foreign directory at the
   frozen lock path with one `.owner` member; and
3. let the handler unlink the foreign `.owner`, remove the foreign directory,
   observe `ENOENT`, and declare `ABSENT`, while the actual owned lock remains
   at the renamed path.

Mode `0700`/`0600` does not separate processes sharing the same UID, and the
lock is intentionally UID-scoped.  `test_rep_009` attacks a foreign lock
*before* acquisition and the post-helper signal boundary, but not replacement
after validation or after the `OWNED -> CLEANING` transition.  P24 likewise
has no replacement.  An implementation following the printed path sequence
can therefore delete foreign state and leave owned residue while all frozen
methods pass.  This violates the remediation gate's rule that a process may
remove only the lock token it created.  Original M3 is not closed.

**Minimum repair contract:** retain the child-root and private-parent FDs
through generation-root cleanup, and perform member deletion relative to the
held child FD.  Retain an independently verified lock-directory FD through
lock cleanup, unlink `.owner` relative to that FD, and fail closed if the
fixed parent entry no longer resolves to the saved lock inode; never unlink a
replacement reached only by pathname.  Extend `test_rep_009`, as serial
subfixtures of its single state-machine class, with controlled replacement
immediately before ACQUIRING cleanup and after `OWNED -> CLEANING`; foreign
replacement bytes/inodes must remain unchanged and the run must not report
`ABSENT` for a displaced owned lock.  Apply the same retained-capability rule
to P25 before closing its FD.  No method or package-class count need change.

## A6. New effective-design provenance finding

### A-M4 — the manifest authenticates an amendment digest string but never dereferences the amendment bytes

**Severity:** Major  
**Evidence anchor:** text: amendment lines 50--56
"not a fifteenth authority binding or a new manifest node" / "authenticates ... transitively"  
**Confidence:** 5/5 — exact hash-DAG and verifier dependency analysis

The effective design is `base + amendment`, but the amendment explicitly
keeps itself out of the fourteen authority bindings and manifest graph.  The
base manifest schema contains only `design_lock={path,sha256}` and
`design_review={path,sha256}`.  The base verifier is required to reconstruct
the printed eight-node adjacency list; neither base nor amendment freezes a
rule that parses the closure addendum for the amendment path/digest and then
re-hashes the current amendment file.

Hashing the final review authenticates the *pointer string* this addendum
contains.  It does not authenticate the current bytes at that pointer unless
the verifier dereferences and hashes them.  A concrete false-accept is:

```text
leave the final review, base design, gate, manifest, and implementation fixed;
change or remove phase2_control_design_amendment_v1.md;
run the frozen base binding and DAG checks.
```

No registered scan includes `notes/`, no manifest member names the amendment,
and no frozen transitive-dereference rule observes the change.  Every printed
binding and DAG check can pass although the current effective-design bytes no
longer match the reviewed tuple.  This also conflicts with the base rule that
a copied source hash is not a root of trust and applicable bytes must be
recomputed.

**Minimum repair contract:** without trusting this review as an oracle,
freeze one deterministic verifier rule that extracts exactly one canonical
amendment path/SHA receipt from the final review, rejects duplicates or
missing fields, independently reads and hashes that amendment path, and
incorporates the successful dereference into lifecycle adjacency validation.
If doing so changes a frozen manifest key, path, authority count, schema, or
DAG node/edge, the remediation gate requires stopping and issuing a new
design finding/gate rather than silently widening this amendment.  Merely
copying the digest into a later gate or review is not a byte check.

## A7. Closure severity and downstream consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem, arithmetic, schema, count, owner, or printed-DAG collapse |
| Major (`M`) | 4 | one M1 supplied-class bypass, one M2 confounded falsifier, one M3 cleanup race, and one effective-design binding gap |
| Minor (`m`) | 0 | none |

The amendment preserves the frozen numeric invariants and repairs large
parts of all three original findings, but the four counterexamples above are
acceptance/provenance surfaces, not wording preferences.  Under the
remediation gate, any one prevents `PASS C0/M0/m0`.  This addendum therefore
closes neither the implementation gate nor any downstream Route.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v1.1
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=22894
PRESERVED_PREFIX_LINES=488
PRESERVED_PREFIX_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_ORIGINAL_REVIEW_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec
REVIEWED_REMEDIATION_GATE_SHA256=98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16
REVIEWED_AMENDMENT_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AMENDMENT_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

M1_REGISTRY_ROWS_RECOMPUTED=35
M1_SEED_ACCEPTS_RECOMPUTED=35
M1_POST_REJECTIONS_BY_STATED_RULE=35
M1_INVERSE_ACCEPTS_RECOMPUTED=35
M1_PERSISTED_ROW_BINDING_MISMATCHES=0
M1_DETECTOR_BINDING_MISMATCHES=0
M1_SUPPLIED_SG_CLASS_BYPASS=OPEN_MAJOR

M2_WHOLE_ROOT_RECEIPT_FIELDS_PRESENT=true
M2_VALID_AND_MALFORMED_RECEIPTS_PRESENT=true
M2_FALSIFIER_METHOD=test_rep_010
M2_MODE_MTIME_FALSIFIER_INDEPENDENT=false

M3_DIRECTORY_FD_GENERATION_WRITES=PASS_BY_DESIGN
M3_P25_VALIDATION_ORDER=PASS_BY_DESIGN
M3_CANONICAL_MUTATION_ROOT_SEPARATION=PASS_BY_DESIGN
M3_ACQUISITION_TOKEN_SIGNAL_BOUNDARY=PASS_BY_DESIGN
M3_FOREIGN_REPLACEMENT_CLEANUP=OPEN_MAJOR

EFFECTIVE_AMENDMENT_REHASH_RULE_FROZEN=false
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=4
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M4_m0

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Final disposition on the exact effective `base + amendment` tuple:
**REVISE — C0/M4/m0**.  The original 22,894-byte review prefix remains
historically intact.  No implementation or control execution is authorized;
the minimum contracts in A-M1 through A-M4 require a new frozen repair and
another independent exact-byte closure review.

---

# Closure addendum v2: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V2 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v2.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M3/m0**  
Control implementation or execution performed: **no**

## B1. Preserved prefix, exact review object, and independence

Immediately before this addendum, the complete review was exactly 1,017
lines and 49,358 bytes with SHA-256
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`.
That complete byte string is the unmodified prefix of this addendum.  It in
turn still contains the original 488-line / 22,894-byte prefix at SHA-256
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.

I independently read the complete current bytes of every record in the
effective design chain and recomputed each digest:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| remediation gate v1 `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` | MATCH |
| amendment v1 `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| complete pre-v2 review prefix `notes/phase2_control_design_peer_review.md` | 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` | MATCH |
| remediation gate v2 `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` | MATCH |
| amendment v2 `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |

The v2 amendment's five authority rows match the first five applicable
records above.  I also re-read the complete original post-proof design gate
at SHA-256
`0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3`.

I reparsed the base authority table and independently opened and hashed all
fourteen paths.  Their indices are exactly `1..14`, all paths are distinct,
there are zero digest mismatches, and their current-byte totals remain 6,319
lines and 255,465 bytes.  The source/proof ceiling and owner therefore remain
stable; byte receipt is not treated as theorem execution.

Before starting this fresh review, I again read in full the applicable ARS
academic-research-suite root instructions; experiment workflow,
reproducibility protocol, and code-runner integrity instructions;
academic-pipeline workflow, integrity-review protocol, reproducibility
audit, and integrity-verification instructions; and the complete reviewer,
methodology, domain, devil's-advocate, peer-reviewer, report-template, and
review-quality instructions.  I applied their exact-byte, independent-
oracle, causal-falsifier, provenance, reproducibility, and hostile-
counterexample rules.

I did not contact an amendment author, inspect an author conversation, or
use either amendment self-audit as evidence.  No generator, verifier,
wrapper, test suite, namespace launcher, or control was implemented or run.
The read-only calculations in this addendum are independent recomputations
from the frozen text and primitive values.  No design, gate, pipeline,
implementation, proof, Route, manuscript, release, or Git record was
changed.

## B2. Independent invariant reconciliation

Splitting each literal CSV header on commas and independently enumerating
the row ranges gives:

| CSV family | Columns | Body rows | Negative rows | Semantic classes |
|---|---:|---:|---:|---:|
| `VC` | 18 | 16 | 4 | 4 |
| `EO` | 19 | 14 | 2 | 2 |
| `FK` | 22 | 18 | 4 | 4 |
| `TC` | 17 | 10 | 3 | 3 |
| `SG` | 16 | 12 | 4 | 4 |
| `OF` | 19 | 15 | 9 | 9 |
| `PC` | 13 | 26 | 9 | 9 |
| `TS` | 10 | 9 | 0 | 0 |
| **Total** | mixed | **120** | **35** | **35** |

Every header token is unique.  The eight row registries remain continuous
from their `001` member through `016,014,018,010,012,015,026,009`,
respectively.  The independent sums are

```text
body rows = 16+14+18+10+12+15+26+9 = 120
negatives = 4+2+4+3+4+9+9+0 = 35
header widths = 18,19,22,17,16,19,13,10
```

The base registry has exactly `S01..S35`; its persisted rows, reason tokens,
and method names are each 35 distinct values.  The v1 causal registry is the
same continuous 35-entry set, and all detector bindings agree with the base.
The package registry is exactly `P01..P28`, with 28 distinct methods and 28
distinct registered P-detectors.  The method arithmetic is independently

```text
fixed method families = 10+10+14+9+10+12+12+5+18+10 = 110
complete suite         = 110+35+28 = 173
```

There remain eight CSVs, nine generated artifacts including the manifest,
six implementation paths, fourteen authority bindings, two canonical fresh
generations, and three canonical copies.  The five new replacement triggers
are operational serial subfixtures and add no row, package class, method,
artifact, or copy.

The printed lifecycle graph still has the eight nodes
`A,D,R,G,I,C,M,V` and the twelve distinct edges

```text
A->D, D->R, R->G, G->I, I->C, C->M, M->V,
A->M, D->M, R->M, G->M, I->M.
```

Its unique topological order remains `A,D,R,G,I,C,M,V`.  There is no
manifest self-hash, `V->M`, concurrent-proof back edge, unknown node, or
cycle.  Exact-zero tolerance, the bare `B_p` owner,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and Route B false are unchanged.

## B3. A-M1 causal-predicate re-review

### B3.1 The complete 35-method chain

I independently replayed the printed typed seed, sole changed-field set,
post-image predicate, detector-after-rejection, exact inverse, and recovered
seed rule for all 35 entries.  The arithmetic families again give:

```text
S01..S04: branch, odd normalizer, two normalizer, and sign reject exactly;
S05: ord_17(2)=8 and the bounded restriction image has order 4;
S06: both displayed 3-adic valuations at ell=19 are 2, not m=1;
S07..S10: valid roots have Phi=0; post roots have Phi=4,2,3,1;
S11..S13: closure, finite/infinite, and discrete/compact AST types reject;
S18..S26: only nominal owner identity transitions accept;
S27..S35: all nine closed nonpromotion/NOT_AS seeds accept and promotions reject.
```

For each method, the registered persisted negative projection equals the
sole post-image only after the post-image is constructed.  `row_id`,
`case_kind`, reason, oracle, status, expected detector, and receipts remain
noncausal.  Each seed accepts, each post-image rejects by the stated typed
rule, each detector is inspected only after rejection, and each exact
inverse accepts.  I found zero seed, footprint, persisted-row, detector, or
inverse mismatches.

### B3.2 The four repaired signature methods

The callable and dispatch identity is now exactly the unparameterized
`SG_SCOPE`.  Expected class, expected detector, persisted prefixes, and
persisted witness are excluded from the decision.  Direct repeated-division
recomputation on `[2;3;5;7;11;13]` gives

```text
p=2  [0;0;0;0;0;0]
p=3  [0;0;0;0;1;0]
p=5  [0;0;0;0;0;0]
p=7  [1;0;1;0;0;0]
p=11 [0;0;0;0;0;0]
p=13 [0;0;0;0;0;0].
```

The same-method primitive attacks behave causally while metadata remains
fixed:

| Method | Independent counterfactual result |
|---|---|
| `S14`, `q:5 -> 3` | the recomputed pair differs only at 11 and derives `FINITE_PAIR_SEPARATION`; stale collision metadata cannot preserve the class |
| `S15`, coordinate `11 -> 13` | both recomputed values at 13 are zero; the witness rejects before expected-class comparison |
| `S16`, registry to `[]` | no nonempty finite matrix exists and the class becomes `NO_INFINITE_EVIDENCE` |
| `S17`, registry to `[2]` | the recomputed one-by-one matrix is `[[0]]` and the class becomes `FINITE_RANGE` |

Changing an expected class cannot satisfy any of these observations.  The
specific supplied-class false accept in `A-M1` is therefore closed by the
v2 bytes.

## B4. A-M2 receipt-comparator re-review

The retained live receipt walks the complete synthetic root from `.`,
including every directory, and compares the exact tuple

```text
(relative_path,type,mode,size,regular_sha256_or_empty,
 mtime_ns,ctime_ns,nlink,device,inode).
```

It remains mandatory around separately valid and malformed verify-only
calls, under uid 0, with relative-only diagnostics.  The malformed package
stays malformed.  The ctime, transient-sidecar, and root live variants
remain independent collection attacks.

The two v2 pure comparator probes start from one actually captured valid
receipt.  An independent tuple-difference routine first proves that their
complete differences are exactly

```text
{(selected_path,mode,0444,0644)}
{(selected_path,mtime_ns,t,t+1000000000)}.
```

Every other record and coordinate, including `ctime_ns`, is identical.
Therefore a comparator that checks only ctime cannot satisfy either probe;
one that omits mode or mtime fails its corresponding probe.  No filesystem
side effect, detector lookup, or shared clone supplies rejection.  The
confounding counterexample in `A-M2` is closed without changing the method,
class, schema, or generated bytes.

## B5. A-M3 possession, cgroup, RPC, and lifecycle audit

### B5.1 The original foreign-deletion counterexample is closed

The two user-namespace maps are ordered and asymmetric: U1 maps only
`65534 -> 65534`, L irreversibly becomes outer uid/gid 65534 and drops its
capabilities, and U2 maps inner `0 -> 65534`.  G becomes PID 1 only after the
second map and private mount/PID namespace creation.  Initial-user-namespace
root and equivalent ancestor capabilities are explicitly trusted; outer
uid 65534 alone receives neither namespace ownership nor proc-root access.

P retains the cgroup parent/session/guardian/workers identities and the
root-only freeze/events/kill controls.  L is atomically born in guardian;
every later workflow child is atomically born in workers.  Only the common-
ancestor and destination `cgroup.procs` write authority is delegated to
outer uid 65534.  Workers receive the destination cgroup FD only in the
trusted first-instruction stub, close it before subject action, see no
cgroup2 mount, and are forbidden to clone, unshare, setns, or send ancillary
FDs.

The seccomp order is correct for the sole supported ABI: an architecture
mismatch is killed first, an x32-number bit is killed second, and only then
does the native x86_64 deny table run.  The table rejects process creation,
namespace changes, legacy AIO, io_uring, `sendmsg`, and `sendmmsg`; the final
allow branch cannot bypass either architecture gate.  No x32 alias can reach
a native allow.

Per-worker RPC uses a fresh `SOCK_SEQPACKET` pair, G-side `SO_PASSCRED`, a
pidfd/start-time/cgroup/session/role mapping, plain worker send/write, and
exactly one kernel-supplied `SCM_CREDENTIALS`.  An endpoint is never shared
or sent.  PID reuse, an explicit credential cmsg, `SCM_RIGHTS`, truncation,
wrong endpoint, or wrong session fails closed.

For a method cleanup, P freezes workers and waits for a fresh `frozen 1`
events parse; frozen membership and both ledgers are then reconciled, and P
audits every worker FD/cwd/root/executable/mapping before issuing
`FROZEN_NOREFS`.  G is then the sole runnable private-path actor.  For final
cleanup, P instead freezes, writes `cgroup.kill`, requires G's wait-to-
`ECHILD` receipt and its own fresh `populated 0`, and only then allows G to
delete private objects.  A method failure before no-reference proof falls to
the final kill path without pathname deletion.

G retains each generation parent/root and lock parent/directory FD.  Members
are deleted only relative to the held child FD.  A fixed entry is removed
only after exclusive-namespace quiescence and an exact parent/name-to-held-
inode check.  In a controlled exchange the fixed foreign entry is never a
deletion target; the owned object is deleted through its held FD and known
internal exchange name.  `DISPLACED_CLEANED/E_CLEANUP` never becomes
`ABSENT`.  EOF, guardian/coordinator death, timeout, STOP/KILL, or identity
failure yields containment or `CRASH_TEARDOWN`, not a successful absence
receipt.  These clauses defeat the original check-then-path-delete attack.

### B5.2 Old-seven and new-five falsifier reconciliation

The seven existing package lifecycle classes `P19..P25` remain distinct and
reachable at their stated boundaries:

| Class | Frozen v2 observation |
|---|---|
| `P19` | pre-entry cache is rejected by the recursive entry scan before bootstrap or project write |
| `P20` | its old post-cache trigger remains a delegated copied-session trigger and the residue check precedes success |
| `P21` | the inherited active marker rejects recursive entry before delegated-session selection |
| `P22` | a contender binds the already-held ordinary abstract address, receives `EADDRINUSE`/74, and gains no filesystem authority |
| `P23` | the fixed verify-only template retains the reserved `--repair` rejection and cannot repair |
| `P24` | abort-after-fresh-A remains owned by its old trigger and reaches retained-capability failure cleanup |
| `P25` | the authorized `MUTATION_P25_V1` root reaches `E_NONEMPTY_OUTPUT`; `occupied` is deleted only through its retained root FD |

The five new environment triggers are unique, literal-1, pairwise exclusive,
test-context-only, and owned by the exact existing method/purpose.  They
cover, respectively, canonical root, empty mutation root, occupied P25 root,
lock `ACQUIRING` after `CREATED`, and lock `OWNED -> CLEANING`.  Their actors
are independently spawned, capability-empty, single-exchange workers and
are reaped before cleanup.  The five serial fixtures do not change 28
package classes, 173 methods, two canonical generations, or three copies.

That reconciliation does not cure the following three independent closed-
protocol defects.

### B-M1 — the closed `OWNER` enum has no value for ordinary pre-suite workers

**Severity:** Major  
**Evidence anchor:** text: amendment-v2 lines 726--728 and 1382--1391
"OWNER is exactly `SUITE_173` for the one top-level test runner" / "TOP_TEST_CONTROLS is used once by G before the runner endpoint exists"  
**Confidence:** 5/5 — direct closed-enum and unchanged-order reachability analysis

The unchanged reproduction order must run checked-in verify-only and the two
canonical A/B generator calls before it invokes the top-level 173-test
runner.  Section 5.5 requires every generator to be a registered direct G
child, and `CHILD_REGISTERED` requires an `owner=OWNER`.  The closed owner
grammar permits `SUITE_173` only for the single top-level test runner; every
other child must use one of the 173 method names.  None of the three ordinary
pre-suite calls is owned by a unittest method, and the runner does not yet
exist to issue an RPC request.

Thus a conforming implementation has no legal owner value for at least
`VERIFY_ONLY_GENERATOR`, `GENERATE_CANONICAL_A`, and
`GENERATE_CANONICAL_B`.  Reusing an arbitrary method token falsifies method
ownership; reusing `SUITE_173` violates the frozen singleton meaning; adding
a token is outside the enum.  The ordinary workflow cannot reach
`CHILD_ADMITTED` without an implementation-time grammar change.

**Minimum repair contract:** freeze one exact operational-only owner for the
top-level reproduction coordinator, or explicitly redefine `SUITE_173` with
a closed cardinality/role matrix.  Bind the three pre-suite targets to that
owner, session, role, purposes, direct-G spawn order, and admission records;
keep the one actual test runner separately identifiable.  No unittest,
artifact, binding, or generated-byte count need change.

### B-M2 — the four `FDSET` tokens do not define the mandatory admission barrier or phase lifetimes

**Severity:** Major  
**Evidence anchor:** text: amendment-v2 lines 824--849 and 856--864
"closes ... every descriptor outside its role whitelist" / "blocks at a one-use barrier" / "the only FDSET values are"  
**Confidence:** 5/5 — direct descriptor-lifetime and independent-attestation analysis

Every child must retain a one-use barrier after the stub closes all
nonwhitelisted descriptors, because P checks the descriptor table before it
authorizes G to release that same barrier.  Yet the complete `FDSET` enum is
only `STDIO`, `STDIO_RPC`, `STDIO_SOURCE_RPC`, and
`STDIO_GENERATION_ROOT`.  The amendment never expands any token into an
exact pre-admission descriptor set, never assigns the barrier a slot/type,
and never freezes its close transition.  It likewise does not give P a
phase-specific mapping for stdout/stderr pipes, the optional source FD, RPC
endpoint, or descriptor 9.

P receives only the `fdset=FDSET` token in `CHILD_REGISTERED` and is supposed
to independently reject every unexpected descriptor.  With no exact token-
to-set mapping, it cannot distinguish the required live barrier from a
leaked namespace, cgroup, parent, root, lock, or socket FD by the frozen
grammar.  Closing the barrier as "nonwhitelisted" deadlocks admission;
silently treating it and other dynamic descriptors as implicit weakens the
independent no-reference proof.

**Minimum repair contract:** freeze a phase-indexed descriptor table for
every role/target.  For each slot specify number or dynamically bound
identity, type/peer, CLOEXEC state, whether P expects it before admission,
and the exact close event.  Include the one-use barrier explicitly; close it
after admission; freeze source-FD closure before subject action, RPC endpoint
lifetime, generator descriptor-9 lifetime, pipe lifetime, and the empty
post-reap set.  No public field, method, or artifact need be added.

### B-M3 — `ROOT_MEMBER` registration is ordered before the inode can exist

**Severity:** Major  
**Evidence anchor:** text: amendment-v2 lines 868--884 and 1069--1074
"OBJECT_REGISTERED precedes any child access" / "descriptor-relative member creation" / "only the child duplicate closes"  
**Confidence:** 5/5 — direct creator/ledger causality analysis

The retained generator contract creates each generated member in the
generator child with descriptor-relative `O_CREAT|O_EXCL`.  A
`ROOT_MEMBER` device/inode receipt therefore does not exist until that child
performs the creating access.  G cannot report the identity before the
access.  The generator receives the root descriptor but no RPC endpoint or
P--G control channel, and the closed FD grammar supplies no private member-
registration channel.

Registering members when G enumerates the root after the generator is reaped
would be safe for later cleanup, but it violates the exact statement that
registration precedes *any* child access.  Omitting them instead triggers
the frozen fatal condition for a live member absent from the registry and
leaves P's later no-reference audit incomplete.  Precreating them in G is
not an alternative because it violates the retained empty-root and
`O_CREAT|O_EXCL` generator contract.

**Minimum repair contract:** freeze a creator-specific ledger transition.
The smallest repair is: register parent/root before generator admission;
after `CHILD_REAPED`, have G enumerate and validate every fixed generated
member, send one exact `OBJECT_REGISTERED` per identity, receive P's ledger
acknowledgment, and only then admit any later child.  State explicitly that
the pre-access rule applies to parent/root and to all post-creator access,
while the creating generator is the sole bounded exception.  Preserve one
matching release per member.  Alternatively, a new trusted registration
channel requires a complete versioned FD/protocol contract rather than an
implementation-time invention.

## B6. Canonical effective-design amendment receipt

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block above contains no blank or commentary line, has count two, uses
the sole canonical order v1 then v2, and records both independently
recomputed complete-file digests.

## B7. A-M4 dereference and manifest re-review

The v2 verifier order no longer trusts the receipt above as a digest oracle.
It first opens and hashes the manifest-bound complete final review, parses
the same authenticated FD bytes, requires one correctly ordered canonical
receipt, and then independently opens both amendment paths beneath the held
package-root capability.  Regular-file, nlink-one, no-symlink, canonical-
path, complete-read, and SHA-256 checks are mandatory for each.  Only after
both current-byte hashes match may the existing review node acquire the
internal resolved-amendment obligation and permit adjacency validation.

This closes the original false accept in which an amendment was changed or
removed while its copied digest string remained in a stable review.  The
obligation stays internal to `R`; it adds no manifest key, authority binding,
generated artifact, graph node, or graph edge.  The manifest surface remains
fourteen bindings, eight nodes, twelve distinct edges, and no review/manifest
self-cycle.  Original `A-M4` is closed by design.  The three findings in
Section B5 independently prevent an effective PASS.

## B8. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no arithmetic, theorem-owner, source-binding, manifest-cycle, or foreign-deletion collapse |
| Major (`M`) | 3 | one missing ordinary-worker owner class, one undefined admission FD-set/lifetime contract, and one impossible pre-creation member registration order |
| Minor (`m`) | 0 | none |

The v2 bytes close the exact supplied-class, ctime-confounding,
replacement-delete, false-ABSENT, and amendment-dereference attacks that
produced `A-M1..A-M4`.  They also preserve all frozen numeric and graph
invariants.  The three new protocol defects are not style requests: each
forces a later implementer either to violate a closed enum/order or to invent
an admission/ledger transition on which the cgroup no-reference proof
depends.  Under the original gate's ambiguity rule and the v2 gate's
zero-finding requirement, any one is blocking.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v2.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=49358
PRESERVED_PREFIX_LINES=1017
PRESERVED_PREFIX_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_PRE_V2_REVIEW_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
REVIEWED_REMEDIATION_GATE_V2_SHA256=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_ORIGINAL_FINDING=CLOSED_BY_V2_DESIGN
A_M1_SG_SCOPE_PARAMETERIZED=false
A_M1_PRIMITIVE_COUNTERFACTUALS_RECOMPUTED=4
A_M2_ORIGINAL_FINDING=CLOSED_BY_V2_DESIGN
A_M2_SINGLETON_COORDINATE_PROBES_RECOMPUTED=2
A_M3_ORIGINAL_FOREIGN_DELETE_FINDING=CLOSED_BY_V2_DESIGN
A_M3_OLD_P19_P25_CLASSES_RECONCILED=7
A_M3_NEW_REPLACEMENT_TRIGGERS_RECONCILED=5
A_M3_OWNER_ENUM_COMPLETE=false
A_M3_FDSET_PHASE_LIFETIMES_COMPLETE=false
A_M3_ROOT_MEMBER_REGISTRATION_ORDER_IMPLEMENTABLE=false
A_M4_ORIGINAL_FINDING=CLOSED_BY_V2_DESIGN
A_M4_INDEPENDENT_AMENDMENT_REHASH_RULE_FROZEN=true

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=3
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M3_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2` effective tuple:
**REVISE — C0/M3/m0**.  The complete 49,358-byte historical review remains
the exact prefix.  No implementation, control execution, Route,
composition, manuscript, release, or Git action is authorized; the three
minimum contracts above require a further versioned design repair and
another fresh independent exact-byte closure review.

# Closure addendum v3: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V3 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v3.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M2/m0**  
Control implementation or execution performed: **no**

## C1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 1,524 lines and
74,876 bytes with SHA-256
`ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested 49,358-byte and 22,894-byte prefixes remain respectively
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`
and
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.

I independently read the complete current bytes of the effective-design
chain and recomputed the following receipts:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| pre-v3 review prefix `notes/phase2_control_design_peer_review.md` | 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` | MATCH |
| remediation gate v3 `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` | MATCH |
| amendment v3 `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |

I also reparsed the base authority table and independently rehashed its
fourteen distinct, continuously indexed paths.  All fourteen match and the
authority tuple remains 6,319 lines / 255,465 bytes.  Proof and peer-review
sources therefore remain stable inputs, not concurrent outputs.

Before this fresh review I reread in full the applicable ARS academic-
research-suite root instructions; experiment-integrity, reproducibility,
and code-runner instructions; academic-pipeline integrity and
reproducibility protocols; and reviewer, methodology, domain,
devil's-advocate, peer-review, report-template, and review-quality
instructions.  I applied their independent-oracle, exact-byte,
counterfactual, provenance, causal-falsifier, and evidence-gap standards.

I did not contact the amendment author, read an author conversation, or use
the amendment's self-audit as evidence.  I did not implement or run a
generator, verifier, test, wrapper, namespace/cgroup controller, or any
other control.  The work was a read-only reconstruction and hostile design
audit.  No design, gate, implementation, pipeline, proof, Route,
manuscript, release, archive, or Git record was changed.  This append-only
review is the sole file written.

## C2. Frozen invariant and v2-regression reconciliation

Independent enumeration retains the exact invariant vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The eight row ranges remain continuous through
`016,014,018,010,012,015,026,009`; their row sum is 120 and their negative
partition is `4+2+4+3+4+9+9+0=35`.  The method arithmetic remains
`110+35+28=173`, with distinct names.  No v3 operational token is a CSV
field, generated member, authority binding, method, or manifest node.

The graph remains `A,D,R,G,I,C,M,V` with the same twelve edges and unique
topological order.  There is no manifest self-hash, future-result edge,
proof/review concurrent cycle, or new review node.  Exact-zero tolerance,
the bare compact group `B_p` theorem owner,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and Route B false are unchanged.

The v2 closures also survive regression:

- `A-M1`: all 35 valid primitive seeds, single substantive mutations,
  independent canonical reparses, receipt-free typed predicates,
  post-rejection detectors, and exact inverses retain their order.  The four
  signature counterfactuals still derive class from primitives through the
  unparameterized `SG_SCOPE`; no expected class is an input.
- `A-M2`: the whole-root live receipt still covers root, directories, files,
  type/mode/size/hash/mtime/ctime/nlink/device/inode.  The five live
  filesystem variants and the two pure exact-one-coordinate mode/mtime
  clones remain selected-field-specific; ctime covariation cannot stand in
  for either selected comparator.
- `A-M3`: the two user-namespace layers, atomic workers-cgroup placement,
  root-owned freeze/kill controls, pidfd and PASSCRED checks, architecture-
  first plus x32-first seccomp gates, retained root/lock capabilities,
  no-false-`ABSENT`, EOF/crash/signal containment, seven old `P19..P25`
  classes, and five controlled replacement triggers remain distinct.  The
  seven old and five new fixtures add no package class or method.
- `A-M4`: complete-review authentication still precedes parsing and
  capability-relative amendment dereference; the active three-file list is
  internal to `R` and adds no binding, node, edge, or cycle.

## C3. Twelve hostile contract challenges

I tested the effective text by seeking pairs of operational worlds that the
claimed independent oracle could not distinguish.  A `PASS` below means no
counterexample was found for that bounded contract, not that controls were
executed.

| # | Hostile contract challenge | Independent result |
|---:|---|---|
| 1 | exact current-byte chain, nested prefix preservation, and fourteen authority rehashes | PASS |
| 2 | eight CSVs / 120 rows / 35 negatives / 35 semantic mutations / 28 package mutations / 173 methods / 9 artifacts / 14 bindings / 2 fresh / 3 copies | PASS |
| 3 | six session-zero children: two probes, verify-only, canonical A/B, and separately owned top runner, each cardinality one | PASS |
| 4 | closed post-suite admission grammar, canonical decimals, method/session/request/child fields, global single-use and reuse rejection | PASS for syntax and uniqueness only |
| 5 | P's claimed independent binding of that admission to the actually accepted RPC request, target, trigger, and method | **REVISE: C-M1** |
| 6 | exact child slots 0/1/2/3/4/8/9 and all four phase-indexed `FDSET` rows | PASS |
| 7 | fixed `SANITIZED -> ADMIT -> SOURCE_READY -> START` order, packet cardinality, source closure, barrier closure, pipe drain, reap, and empty post-reap process | PASS |
| 8 | first P descriptor audit and second pre-START audit against actual number/type/mode/CLOEXEC/file/pipe/root/cwd facts rather than an `FDSET` token | PASS for non-socket coordinates |
| 9 | independent exact pairing of child socket FDs 4/8 with the corresponding G endpoints, including a two-pair cross-wire | **REVISE: C-M2** |
| 10 | every G-created object exists, is no-follow validated, registered, independently matched in G's live FD table, and ACKed before child access | PASS |
| 11 | creator-only future-inode exception, `CHILD_REAPED_ACK`, dirfd-relative set partition, canonical nine-member registration, ledger ACK, P25 count zero, and partial/unexpected prohibitions | PASS |
| 12 | all four v2 regressions plus immutable historical receipt, unique active count-three receipt, independent v1/v2/v3 reads/hashes, and manifest/DAG ceiling | PASS |

Challenges 5 and 9 are independent: the first concerns which authenticated
request authorized a child; the second concerns which kernel socket
endpoint is paired with that child.  Fixing one does not provide the missing
observation for the other.

## C4. B-M1 repair review

The v3 bytes close the reported enum/cardinality defect.  The amended owner
domain has exactly two bootstrap children, three reproduction-coordinator
children, one suite runner, and one of 173 exact method owners thereafter.
The six session-zero rows and their literal admissions are complete.  The
post-suite production is canonical and single use, and the two child records
echo identical bytes.  Thus the original `B-M1` counterexample is closed.

### C-M1 — P cannot independently derive request-bound admission from an RPC it cannot observe

**Severity:** Major  
**Evidence anchors:** amendment-v3 lines 200--225 and 251--273;
amendment-v2 lines 652--761 and 1287--1329; amendment-v3 lines 82--126  
**Confidence:** 5/5 — closed-channel information-flow counterexample

Amendment v3 requires G to construct
`METHOD_V1:<METHOD>:S<SESSION>:R<REQUEST>:C<CHILD>` from its authenticated
per-endpoint mapping and accepted request, while P "independently derives"
the expected bytes and verifies the accepted request id plus request target,
purpose, trigger, role, and session.  But the retained v2 topology gives the
requester endpoint only to G.  G alone stores the endpoint mapping, G alone
receives the request and its `SCM_CREDENTIALS`, and the RPC channel is
explicitly separate from and never shared with P's control connection.

The amended `CHILD_REGISTERED` payload contains only session, child,
inner_pid, role, owner, purpose, admission, fdset, cwd_dev, and cwd_ino.  It
contains no endpoint identity, accepted-request transcript, target, or
trigger.  The exhaustive v3 operational delta adds no independent
request-witness record or P-held requester endpoint.  Every value from which
P could reconstruct `METHOD`, `SESSION`, `REQUEST`, or `CHILD` is therefore
either parsed from the admission itself or supplied by G in the same record.

Counterexample: hold the actual child PID, descriptors, cwd, cgroup,
credentials, source category, target template, and purpose constant.  In
world A, G receives the authorized method/session request printed in the
registration.  In world B, the accepted endpoint request has a different
request id or method-session owner, while G submits the same unused,
canonical, internally consistent admission and registration as world A.
P's complete frozen observation is byte-for-byte identical in both worlds.
Canonical reserialization and reuse checks pass, yet only world A satisfies
the stated accepted-request predicate.  Parsing and regenerating G's copy
is not independent derivation.

This is not a demand that P distrust every act of trusted G.  It is a direct
failure of the stronger independent oracle that the v3 bytes themselves
make a mandatory pre-admission condition.  An implementer must either omit
that check or invent an unversioned authority path.

**Minimum repair contract:** before `CHILD_REGISTERED`, freeze one
P-observable, kernel-authenticated, single-use request-authorization event
whose exact fields bind requester endpoint identity, session, request,
method, target, purpose, trigger, role, and the future admission production.
Freeze its channel ownership, wire bytes, credentials/capability check,
direction, cardinality, state transition, reuse rule, EOF/failure behavior,
and how P joins it to the later pidfd/child.  A second unverified G assertion
does not repair independence.  If the intended model instead makes G the
sole oracle for request provenance, the design must remove the contradictory
independent-derivation claim and state the resulting trusted boundary; that
is a substantive versioned choice, not an implementation note.

## C5. B-M2 repair review

The v3 bytes close the reported undefined-FDSET defect.  They freeze the
seven possible child slots, four exact target rows at registered,
source-ready, and running phases, fixed four-frame barrier, two P audits,
source/root/RPC lifetimes, orderly drain/reap, and fatal close behavior.
The original `B-M2` counterexample is closed.

### C-M2 — exact socketpair peer identity has no frozen observable relation

**Severity:** Major  
**Evidence anchors:** amendment-v3 lines 283--303, 334--363, and 448--470;
amendment-v2 lines 438--478 and 1294--1329  
**Confidence:** 5/5 — two-pair indistinguishability and missing-primitive analysis

At each audit P must use the child's `/proc/PID/fd` and `fdinfo` table to
check "socket family/type and exact peer identity" and the corresponding
G-held peer.  The text freezes neither a canonical peer-identity value nor a
relation that connects the two distinct endpoint identities of an anonymous
Unix socketpair.  The listed v2 runtime surface contains `SO_PEERCRED` and
`SO_PASSCRED/SCM_CREDENTIALS`, but no peer-inode query, Unix diagnostic
request/response grammar, or other endpoint-correlation primitive.  Proc FD
and fdinfo enumeration exposes each local socket object; equality cannot
pair the endpoints because the two endpoint objects have different socket
identities.  Peer credentials also do not distinguish multiple pairs made
by the same G, and FD 8's fixed packets explicitly contain no credentials,
rights, child id, or admission bytes.

Counterexample: create two otherwise valid simultaneous child-unique barrier
pairs, preserve every child's exact FD number/type/CLOEXEC state and every
G-held endpoint, but cross-associate the two G endpoints.  P still observes
the correct child socket count and local identities and the correct G socket
count and local identities.  All frozen proc/fdinfo and table predicates are
the same.  Because the bare `ADMIT` and `START` payloads carry no child
binding, paired cross-delivery can advance both children while the purported
corresponding-peer assertion is false.  A conforming independent checker
needs an extra relation that the frozen observation contract never defines.

The sentence requiring exact peer identity is a goal, not an implementable
oracle: different later choices can accept or reject the same endpoint set,
and the stipulated fail-closed branch cannot decide whether the coordinate
was observable until the missing primitive is chosen.

**Minimum repair contract:** freeze one exact independent peer-correlation
mechanism.  For example, specify the precise Unix diagnostic request and
response ABI that maps each endpoint inode to exactly one reciprocal peer
inode, including namespace, privilege, byte order, attribute parsing,
duplicate/missing handling, runtime preflight, and fail-closed behavior; then
require reciprocal one-to-one matching for FDs 4 and 8 and add a two-pair
cross-wire falsifier.  An alternative capability/nonce design must freeze
equally exact endpoint-bound bytes and must not rely on G's mapping or the
unbound fixed barrier tokens.

## C6. B-M3 and A-M4 closure review

The v3 creator ordering closes the original `B-M3` counterexample without a
future inode.  G-created parent/root/member/lock objects have actual retained
validation FDs and receive P ACK before access.  A creation-capable generator
instead receives one exact target/purpose/root/basename/primitive
authorization before admission.  After reap, `CHILD_REAPED_ACK` precedes
root enumeration; G partitions already ACKed pre-created members, ignores
filesystem enumeration order, compares a typed set, and registers actual
authorized members in the fixed nine-name order.

Canonical success requires nine ACKed generated members.  Nonempty P25 has
one separately ACKed `occupied` and generated count zero.  A partial failure
registers every actual authorized regular member but cannot become success;
an all-nine non-success status remains failure.  An unexpected basename,
type, symlink, special object, or duplicate blocks ledger close and cannot be
registered, released, normalized, or deleted.  No later admission,
reference audit, exchange, cleanup, or release occurs before ledger ACK.
I found no remaining B-M3 counterexample.

The immutable historical effective-amendment receipt remains byte-for-byte
inside the preserved prefix.  The following is the sole active successor
receipt and is intentionally outside that prefix:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v2]
count=3
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The successor has count three, exact order v1/v2/v3, no internal blank or
commentary line, and all three independently recomputed current-byte hashes.
The final verifier must authenticate this complete post-v3 review from the
manifest-bound path first, parse these same bytes, require the one immutable
historical receipt and this one active receipt with no other tag, then
capability-open and hash all three amendment paths before setting
`R.effective_amendments=[v1,v2,v3]`.  The receipt is not its own digest
oracle.  `A-M4` remains closed.

## C7. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, arithmetic, authority-binding, manifest-cycle, or foreign-deletion collapse |
| Major (`M`) | 2 | missing independent request witness; undefined Unix-socket peer-correlation oracle |
| Minor (`m`) | 0 | none |

The v3 bytes close the three reported v2 findings as written: owner
cardinality is closed, descriptor slots and phases are closed, and creator
ordering is realizable.  The fresh hostile review nevertheless finds two
new information-flow defects in mandatory independent checks.  Each permits
two operational worlds with identical P-visible frozen facts but different
truth of the required predicate.  They are not cured by a token lookup,
canonical reserialization, copied `FDSET`, or hard-coded pass, and either one
blocks an exact design PASS under the gate's zero-finding rule.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v3.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=74876
PRESERVED_PREFIX_LINES=1524
PRESERVED_PREFIX_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_PRE_V3_REVIEW_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
REVIEWED_REMEDIATION_GATE_V3_SHA256=e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M3_OLD_P19_P25_CLASSES_RECONCILED=7
A_M3_NEW_REPLACEMENT_TRIGGERS_RECONCILED=5
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V2_SUCCESSOR
B_M1_ORIGINAL_FINDING=CLOSED_BY_V3_DESIGN
B_M2_ORIGINAL_FINDING=CLOSED_BY_V3_DESIGN
B_M3_ORIGINAL_FINDING=CLOSED_BY_V3_DESIGN
C_M1_INDEPENDENT_REQUEST_WITNESS_COMPLETE=false
C_M2_INDEPENDENT_SOCKET_PEER_ORACLE_COMPLETE=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M2_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c` effective tuple:
**REVISE — C0/M2/m0**.  The complete 74,876-byte historical review remains
the exact prefix.  No implementation gate, control execution, Route,
composition, manuscript, release, archive, or Git action is supported.  The
two minimum contracts above require a further versioned design repair and a
fresh independent exact-byte closure review.

# Closure addendum v4: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V4 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v4.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M2/m0**  
Control implementation or execution performed: **no**

## D1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 1,910 lines and
96,524 bytes with SHA-256
`ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested 74,876-byte, 49,358-byte, and 22,894-byte prefixes remain respectively
`ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725`,
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`,
and
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.

I independently read the complete current bytes of the effective-design
chain and recomputed the following receipts:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| pre-v4 review prefix `notes/phase2_control_design_peer_review.md` | 1910 | 96524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` | MATCH |
| remediation gate v4 `notes/phase2_control_design_remediation_gate_v4.md` | 645 | 30174 | `df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647` | MATCH |
| amendment v4 `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |

I reparsed the base authority table and independently read and hashed all
fourteen distinct, continuously indexed paths.  Every digest matches.  Their
aggregate remains 6,319 lines / 255,465 bytes.  Proof, proof review, control
gate, and peer-review records remain stable upstream inputs rather than
concurrent outputs.

Before this re-review I reread in full the applicable ARS academic-research-
suite root instructions; experiment-integrity, reproducibility, and code-
runner instructions; academic-pipeline integrity and reproducibility
protocols; and reviewer, methodology, domain, devil's-advocate, peer-review,
report-template, and review-quality instructions.  I applied their exact-byte,
independent-oracle, counterfactual, provenance, causal-falsifier, and evidence-
gap standards.

I did not contact the amendment author, read an author conversation, or rely
on the amendment's completeness table.  I did not implement or run a
generator, verifier, test, wrapper, namespace/cgroup controller, or any other
control.  This was a read-only reconstruction and hostile design audit until
this sole append.  No design, amendment, gate, implementation, pipeline,
proof, Route, manuscript, release, archive, or Git record was changed.

## D2. Frozen invariant, regression, and DAG reconciliation

Independent enumeration retains this exact vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The eight continuous row ranges still terminate at
`016,014,018,010,012,015,026,009`; their sum is 120.  The independently
counted negative partition is `4+2+4+3+4+9+9+0=35`.  The eight literal
headers independently split to `18,19,22,17,16,19,13,10` fields.  The
method arithmetic remains
`10+10+14+9+10+12+12+5+18+10+35+28=173`, with the thirty-five `S01..S35`
and twenty-eight `P01..P28` names distinct.  V4 adds operational frames,
records, FD 5, and a local query primitive, but no CSV field, row, semantic
class, package class, method, path, artifact, binding, or public detector.

The graph remains the eight nodes `A,D,R,G,I,C,M,V`, the seven chain edges,
and the five additional edges `A,D,R,G,I -> M`: twelve distinct edges and
the same unique topological order.  The manifest has no self-hash, no
future-result edge, no proof/review concurrent cycle, and no amendment node.
Complete-review authentication precedes parsing; active amendment paths are
then capability-opened and hashed.  This internal dereference adds no edge.

The prior closures also survive regression:

- `A-M1`: all 35 valid primitive seeds, one substantive mutation each,
  independent canonical reparses, receipt-free typed rejection predicates,
  post-reject detectors, and inverse acceptance remain ordered.  Row id,
  `case_kind`, expected reason/oracle/status, and the four signature expected-
  class fields do not become inputs.
- `A-M2`: the whole-root recursive `lstat` receipt still includes root,
  directories, files, type/mode/size/hash/mtime/ctime/nlink/device/inode.
  Valid and malformed roots, all five live metadata falsifiers, and the two
  pure exact-one-coordinate mode/mtime clones remain selected-field-specific;
  ctime covariation cannot stand in for mode or mtime coverage.
- `A-M3`: the two user-namespace layers; root-owned cgroup membership,
  freeze, kill, reap, and populated-zero proof; per-worker PASSCRED/pidfd/RPC/
  lock state; descriptor and EOF lifetime; architecture-first plus x32-first
  seccomp gates; signal/crash/foreign-lock cleanup; and no-false-`ABSENT`
  behavior remain.  The seven old `P19..P25` classes and five new replacement
  triggers remain distinct operational fixtures and add no class or method.
- `B-M1..B-M3`: the six fixed session-zero rows, exact phase-indexed FD sets,
  four-frame start barrier, G-created pre-access registration/ACK, generator-
  created post-reap registration/ACK, canonical set/order, P25 count zero,
  and unexpected/partial prohibitions remain intact.
- `A-M4`: both immutable historical blocks remain byte-exact in the prefix;
  the active successor below has four independently rehashed amendment paths.

Exact-zero tolerance, the bare compact group `B_p` theorem owner,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, Route B false, verify-only
read-only behavior, two fresh roots, three-way identity, recursive residue
checks, cleanup traps, and package-lock ordering are unchanged.

## D3. Hostile v4 contract challenges

I sought pairs of operational worlds for which the required predicate differs
but P's frozen observations do not.  `PASS` here means that no counterexample
was found for the bounded design clause; it is not an execution result.

| # | Hostile contract challenge | Independent result |
|---:|---|---|
| 1 | exact base/v1/v2/v3/v4 chain, v4 gate, full prefix, nested prefixes, and fourteen authority hashes | PASS |
| 2 | all frozen counts, headers, rows, mutations, methods, artifacts, identities, and the 8/12 manifest DAG ceiling | PASS |
| 3 | P-created child-unique FD 5, exact fourth FDSET row, sole retained peer, bounded G transit, pre-admission absence, and close/EOF/reap order | PASS |
| 4 | four FD-5 frames, PASSCRED provenance, canonical serial, P-issued one-use nonce, digest, raw outer bytes, receipt, replay and endpoint-exchange rejection | PASS |
| 5 | FD-5 direct bytes versus the actual FD-4 accepted bytes, credential tuple, confirmation, one clone, audited registration, and deterministic admission production | PASS conditional on a valid pre-receipt session authorization |
| 6 | P's pre-receipt knowledge that a top-runner opaque session is bound to the claimed method and trigger | **REVISE: D-M1** |
| 7 | exact 40-byte Unix-diag request, sequence/port/cookie fields, single outstanding request, timeout, and no fallback | PASS |
| 8 | exact 48-byte reply, family/type/state/inode, peer then shutdown attributes, source, cardinality, and second-datagram rejection | PASS |
| 9 | true reciprocal pairs, simultaneous crossed A/B preflight, post-close B requery, and FD-8/FD-4/FD-5 owner matrices | PASS conditional on an independently acquired child endpoint inode |
| 10 | exact P-side acquisition of the child endpoint's asserted second `fstat` inode observation | **REVISE: D-M2** |
| 11 | endpoint close phases, pre-START fail-closed behavior, post-START containment, kill/reap/cleanup, and foreign preservation | PASS |
| 12 | A-M1--A-M4 and B-M1--B-M3 regressions, historical blocks, unique active count-four block, four dereferences, and no schema/path/Route widening | PASS |

The two findings are independent.  D-M1 is an authorization-state visibility
gap before any actual FD-4 acceptance.  D-M2 is a missing exact acquisition
operation for one input to an otherwise sufficient reciprocal kernel oracle.

## D4. C-M1 repair review

V4 closes the prior absence of requester-authored evidence for the request
bytes themselves.  P creates and retains the audit peer, authenticates both
requester packets with kernel credentials, issues a non-reused audit/serial
nonce, decodes and hashes the exact core, retains the exact outer bytes, and
compares those bytes with G's actual FD-4 transcript.  A changed request id,
method, primitive target, trigger, purpose, core byte, digest, credential,
nonce, endpoint, or G report is distinguishable before clone.  Confirmation
is single-use, and the later audited registration carries enough fields for P
to derive the admission bytes from the confirmed direct transcript rather
than from G's admission token.  Those parts of C-M1 are closed.

### D-M1 — P has no pre-receipt registration of the top runner's opaque method session

**Severity:** Major  
**Evidence anchors:** amendment-v2 lines 1331--1368 and 1434--1459;
amendment-v4 lines 221--247, 314--345, and 350--394  
**Confidence:** 5/5 — closed-channel state counterexample

The top runner's audit endpoint is allocated under the fixed
`session=0, owner=SUITE_173` tuple.  Under retained v2 semantics, however,
that endpoint may make child-creating requests using only the opaque method-
session handles returned on its own `SESSION_CREATE` requests.  G alone owns
the session record containing handle, method, and trigger.  `SESSION_CREATE`
and `SESSION_CREATED` remain non-child RPC frames on the separate requester--G
endpoint, and v4 expressly leaves non-child RPCs unchanged.  None of v4's
five new P--G records tells P that session `s` was allocated for method `M`
and trigger `T`.

Nevertheless, P must validate the direct `AUDITED_SPAWN` against the
"existing closed method/session/target/purpose/trigger authorization" and
send `AUDIT_RECEIPT` before the requester sends those same bytes on FD 4.
At that decision point P has not observed either the session-creation request
or G's returned opaque handle.  Static knowledge of the 173 method names and
target policy cannot establish the dynamic relation `s -> (M,T)`.
`OBJECT_REGISTERED` records may expose the decimal session later, but carry
neither method nor trigger and therefore do not repair that relation.

Counterexample: preserve the same top-runner pidfd, child id, audit endpoint,
credential, audit/serial/nonce, object receipts, session decimal `s`, and
direct `AUDITED_SPAWN` bytes claiming `(s,M,T)`.  In world A G's private
session record binds `s` to `(M,T)`; in world B it binds the same `s` to a
different method or trigger.  P's complete state before `AUDIT_RECEIPT` is
identical, while the mandatory authorization predicate differs.  Reading
`s`, `M`, and `T` back from the direct payload makes the comparison
tautological.  Waiting for `AUDITED_RPC_ACCEPTED` would let G reject world B,
but contradicts the frozen receipt-before-FD-4 order and does not implement
P's stated pre-receipt check.

This does not show that G would clone an unauthorized world after all later
checks; it shows that the exact mandatory P transition cannot be implemented
without inventing a state-mirroring rule or weakening its stated predicate.
That is material under this gate's deterministic exact-design standard.

**Minimum repair contract:** choose and freeze one of two coherent models.
Either add a canonical P-visible session-allocation/authorization record and
ACK before `SESSION_CREATED`, binding creator requester, creation request id,
opaque session, method, trigger, owner, lifetime, single-use/close state,
direction, cardinality, malformed/reuse behavior, and crash cleanup; then use
that state at `AUDIT_RECEIPT`.  Or explicitly limit P's pre-receipt decision
to requester provenance, raw bytes, and static tuple syntax, move dynamic
session authorization to G's separately named confirmed predicate, and
remove every claim that P independently knows the existing method-session
binding.  Either choice requires a versioned amendment; a token lookup from
the same direct payload is not a repair.

## D5. C-M2 repair review

The selected Unix-diag relation is capable of distinguishing the v3 crossed-
pair worlds.  Independent UAPI reconstruction gives a 16-byte `nlmsghdr`
plus 24-byte `unix_diag_req` request.  Exact-inode handling invokes the
non-dump path and returns a 16-byte header plus 16-byte `unix_diag_msg`.
With `udiag_show=4`, the peer attribute is one aligned 8-byte attribute; the
kernel then emits the one-byte shutdown attribute unconditionally, aligned to
8 bytes.  Thus the required 40-byte request, 48-byte response, `flags=0`,
requester port id, peer-then-shutdown order, and shutdown zero are mutually
consistent for a live connected `SOCK_SEQPACKET` pair.  Cookie does not
become identity.  The two simultaneous pairs, reciprocal queries, crossed
inequalities, post-close requery, no-extra-datagram rule, and live owner
cardinalities reject the original cross-wire attack.  The platform preflight
correctly turns kernel/version/LSM/module differences into pre-write failure.

### D-M2 — the child endpoint's "no-follow actual-descriptor fstat" has no frozen acquisition operation

**Severity:** Major  
**Evidence anchors:** remediation-gate-v4 lines 399--409; amendment-v4 lines
675--688; amendment-v2 lines 438--464  
**Confidence:** 5/5 — syscall-object mismatch

V4 requires two child-inode observations: canonical
`/proc/<child-PID>/fd/<slot> -> socket:[INODE]` text and a matching
"no-follow actual-descriptor fstat" inode.  P does not hold the child endpoint
FD; for FD 4 and FD 8 G holds only the opposite peer, and for FD 5 P holds
only the opposite audit peer.  P's pidfd names the process, not one of that
process's numbered descriptors, so `fstat(pidfd)` cannot return the socket
endpoint inode.

No Linux `fstat` call has a no-follow flag.  Applying
`AT_SYMLINK_NOFOLLOW` to `/proc/PID/fd/N` observes the proc magic symlink,
not the socket object.  Following the magic link with `stat`/`fstatat` can
observe the socket object, but contradicts the literal no-follow clause.
Duplicating the actual child descriptor first with `pidfd_getfd` would make
`fstat` meaningful, but neither the syscall/number and flags nor its
permission/LSM preflight, returned-FD identity/CLOEXEC rule, close lifetime,
and failure behavior appear in the frozen platform or v4 ABI.  The design
therefore specifies a desired second inode equality without specifying an
operation that produces its left-hand value.

This gap is upstream of the otherwise valid Unix-diag mapping.  An
implementation that trusts only the proc link omits a mandatory independent
check; one that follows the link violates no-follow; one that invents
`pidfd_getfd` adds an unfrozen platform primitive.  Fail-closed behavior does
not select among them.

**Minimum repair contract:** freeze one exact mechanism.  For example,
replace the phrase with an exact proc-dirfd-relative following
`fstatat`/`statx` operation, including flags, stable blocked/frozen child
state, expected `S_IFSOCK`, device/inode fields, race recheck, and failure
handling.  Alternatively freeze x86_64 `pidfd_getfd` (syscall 438, flags
zero), its required permission/LSM preflight and target-slot state, returned-
FD type/inode/CLOEXEC checks, immediate close and error/ambiguity behavior.
Then require its inode to equal both canonical proc text and the exact-inode
Unix-diag query.  Merely renaming readlink output as `fstat` is insufficient.

## D6. A-M4 successor receipt

The immutable historical `v1` count-two and `v2` count-three receipts remain
inside the preserved 96,524-byte prefix.  The following is the sole active
successor receipt and is intentionally outside that prefix:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v3]
count=4
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The successor has count four, exact v1/v2/v3/v4 order, no internal blank or
commentary line, and four independently recomputed current-byte hashes.  The
final verifier must authenticate this complete post-v4 review from the
manifest-bound path first, parse the same bytes, require the two historical
blocks plus this unique active block and no other tag, then capability-open
and hash the four amendment paths before setting
`R.effective_amendments=[v1,v2,v3,v4]`.  The receipt contains no review digest
and is not its own oracle.  A-M4 remains closed without a self/proof/future
cycle.

## D7. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, authority-binding, arithmetic, manifest-cycle, foreign-deletion, or containment collapse |
| Major (`M`) | 2 | missing P-visible top-runner method-session authorization; unspecified child-endpoint `fstat` acquisition primitive |
| Minor (`m`) | 0 | none |

V4 supplies a genuine direct requester byte witness and a genuine reciprocal
Unix-socket peer relation; neither new finding disputes those repaired
subcomponents.  The remaining gaps occur at two mandatory inputs to those
components.  Each forces an implementer either to omit a frozen check, make a
tautological comparison, or invent a new operational primitive/state event.
Under the v4 gate's zero-finding rule, the exact effective tuple remains
REVISE.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v4.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=96524
PRESERVED_PREFIX_LINES=1910
PRESERVED_PREFIX_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
PRESERVED_NESTED_PREFIX_74876_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_PRE_V4_REVIEW_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
REVIEWED_REMEDIATION_GATE_V4_SHA256=df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M3_OLD_P19_P25_CLASSES_RECONCILED=7
A_M3_NEW_REPLACEMENT_TRIGGERS_RECONCILED=5
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V3_SUCCESSOR
B_M1_REGRESSION=CLOSED
B_M2_REGRESSION=CLOSED
B_M3_REGRESSION=CLOSED
C_M1_DIRECT_REQUEST_PROVENANCE_AND_RAW_BYTE_JOIN_COMPLETE=true
C_M1_PRE_RECEIPT_TOP_SESSION_AUTHORIZATION_COMPLETE=false
C_M2_NETLINK_UNIX_DIAG_RECIPROCAL_ABI_COMPLETE=true
C_M2_CHILD_ENDPOINT_INODE_ACQUISITION_COMPLETE=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M2_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c + v4 f5547926`
effective tuple: **REVISE — C0/M2/m0**.  The complete 96,524-byte historical
review remains the exact prefix.  No implementation gate, control execution,
Route, composition, manuscript, release, archive, or Git action is supported.
The two minimum contracts above require a further versioned design repair and
another fresh independent exact-byte closure review.

# Closure addendum v5: fresh independent exact-byte blocked-amendment re-review

Status: **COMPLETE — APPEND-ONLY V5 BLOCKED-EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v5.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M2/m0**  
Control implementation or execution performed: **no**

## E1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 2,308 lines and
119,250 bytes with SHA-256
`cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested prefix receipts remain:

| Prefix lines | Prefix bytes | Independently recomputed SHA-256 |
|---:|---:|---|
| 1,910 | 96,524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1,524 | 74,876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1,017 | 49,358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22,894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

I freshly read the complete frozen chain and independently recomputed these
current-byte receipts:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| remediation gate v1 `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` | MATCH |
| amendment v1 `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| remediation gate v2 `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` | MATCH |
| amendment v2 `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| remediation gate v3 `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` | MATCH |
| amendment v3 `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| remediation gate v4 `notes/phase2_control_design_remediation_gate_v4.md` | 645 | 30174 | `df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647` | MATCH |
| amendment v4 `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| remediation gate v5 `notes/phase2_control_design_remediation_gate_v5.md` | 839 | 41734 | `55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7` | MATCH |
| blocked amendment v5 `notes/phase2_control_design_amendment_v5.md` | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| complete pre-v5 review prefix `notes/phase2_control_design_peer_review.md` | 2308 | 119250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` | MATCH |

I reparsed the base authority table and independently hashed all fourteen
distinct, continuously indexed authority paths.  All fourteen match; their
aggregate remains 6,319 lines and 255,465 bytes.  The post-proof design gate
is still
`0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3`.
The proof and proof-review records remain stable upstream inputs, never
concurrent outputs or evidence manufactured by this review.

Before this re-review I reread in full the applicable ARS academic-research-
suite root instructions; experiment-integrity, reproducibility, and code-
runner instructions; academic-pipeline integrity and reproducibility
protocols; and the reviewer, methodology, domain, devil's-advocate, peer-
review, review-quality, and report-template instructions.  I applied their
exact-byte provenance, independent-oracle, counterfactual, information-flow,
causal-falsifier, and evidence-gap rules.

I did not contact the amendment author, inspect author dialogue, or treat the
v5 blocker analysis or self-classification as evidence.  I independently
reconstructed each counterexample from the frozen gate and effective-design
bytes.  I did not implement or run a generator, verifier, test, wrapper,
namespace/cgroup controller, pidfd operation, Unix-diag query, or any other
control.  Until this sole append, the audit was read-only.  No base design,
amendment, gate, pipeline, proof, Route, manuscript, release, archive, or Git
record was changed.

## E2. Blocked-v5 semantics, invariants, and DAG reconciliation

The final v5 bytes are an explicit stopped amendment, not an unsuccessful
repair silently presented as effective.  Lines 3--10 classify the record as
`FROZEN_BLOCKED`, retain `REVISE_C0_M2_m0`, and state that no effective
repair was added.  Lines 59--74 make any transient earlier bytes nonauthority
and state that v5 supersedes no base/v1/v2/v3/v4 clause.  Therefore the
operative protocol remains base plus v1--v4; v5 joins the versioned chain
only as an exact stop/provenance record.  Its hash is not evidence that either
finding closed, and the proposed v5-gate repair clauses are not installed by
this no-op amendment.

Independent enumeration retains the exact frozen vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The body-row endpoints remain
`016,014,018,010,012,015,026,009`, totaling 120.  The independently
reconciled negative partition is `4+2+4+3+4+9+9+0=35`; the method arithmetic
is `10+10+14+9+10+12+12+5+18+10+35+28=173`.  The 35 `S01..S35` and 28
`P01..P28` identities remain distinct.  V5 adds no row, header, method,
mutation class, path, artifact, binding, manifest key, public detector, or
exit class.

The graph remains the eight nodes `A,D,R,G,I,C,M,V`, seven chain edges and
five additional `A,D,R,G,I -> M` edges: twelve distinct edges and the same
topological order.  There is no manifest self-hash, future-result edge,
concurrent proof hash, or amendment node.  The count-five receipt below is an
authenticated internal review-node provenance list.  It adds no manifest
edge and does not transform the blocked v5 record into an operational repair.

All earlier closed subcontracts remain unchanged because v5 installs no
operational delta: the 35 primitive semantic chains and four `SG_SCOPE`
counterfactuals; whole-root metadata receipts and selected-field mode/mtime
probes; private possession/cgroup/cleanup protocol; six pre-suite rows,
phase-indexed descriptor sets and barriers; object creation/registration
ledgers; direct requester raw-byte witness; and reciprocal Unix-diag ABI.
The two inputs still missing from those last two subcontracts are exactly the
open `D-M1` and `D-M2` findings reviewed below.

## E3. Hostile blocked-amendment challenges

I sought worlds whose required predicates differ while all observations
available to the named decision owner are held fixed.  `PASS` in this table
means only that no contradiction was found in the bounded record; it is not
an execution result.

| # | Hostile challenge | Independent result |
|---:|---|---|
| 1 | complete chain, v5 gate/amendment, full prefix, nested prefixes, and fourteen authority hashes | PASS |
| 2 | v5 final-byte precedence, no-op status, no supersession, and blocked provenance | PASS |
| 3 | grant/receipt before actual `SESSION_CREATE` across independent P--G and requester--G sockets | **REVISE: D-M1 remains open** |
| 4 | actual `SESSION_CREATED` before activation and P active receipt before any G-side mutation | **REVISE: D-M1 remains open** |
| 5 | every grant/receipt/accepted/commit/activation send-failure and object/session unwind | **REVISE: D-M1 remains open** |
| 6 | v4 FD-5 no-duplicate/exclusive-holder rule versus mandatory `pidfd_getfd(child_pidfd,5,0)` | **REVISE: D-M2 remains open** |
| 7 | unconditional duplicate, proc-directory FD, and pidfd disposal on every partial/error edge | **REVISE: D-M2 remains open** |
| 8 | G descriptor-table quiescence across two snapshots and all candidate acquisitions | **REVISE: D-M2 remains open** |
| 9 | 6/8/120/35/35/28/173/9/14/2/3 counts, prior closures, exact-zero ceiling, and 8/12 DAG | PASS |
| 10 | three immutable historical amendment blocks, one active count-five successor, five path dereferences, and no schema/Route widening | PASS as blocked provenance only |

The supporting counterexamples do not create extra counted findings.  They
expose independent missing edges inside the same two mandatory contracts
already named `D-M1` and `D-M2`.  Neither finding is closed or downgraded.

## E4. D-M1 independent causal-capability audit

### D-M1 remains Major — an early byte-identical FD-4 request is not observable

**Severity:** Major  
**Evidence anchors:** remediation-gate-v5 lines 128--175, 218--298, and
331--388; blocked-amendment-v5 lines 112--212; current-review lines
2071--2123  
**Confidence:** 5/5 — closed two-queue indistinguishability construction

The gate gives the requester `auth`, `session`, `nonce`, request, method,
trigger, owner, digest, and complete future `SESSION_CREATE` bytes before P
sends `SESSION_AUTH_RECEIPT`.  That receipt contains no new one-use value.
The P--G control socket and requester--G FD 4 are independent seqpacket
queues.  Compare:

```text
compliant world:
  P enqueues SESSION_AUTH_GRANTED to G
  P sends SESSION_AUTH_RECEIPT to requester
  requester enqueues the registered SESSION_CREATE on FD 4

early world:
  requester enqueues the same registered SESSION_CREATE on FD 4
  P later enqueues the same SESSION_AUTH_GRANTED to G
  P later sends the same SESSION_AUTH_RECEIPT to requester
```

Let G remain unscheduled until both queues contain their packets.  G then
observes byte-identical grant and FD-4 packets, identical kernel credentials,
pidfd/start-time identity, request/session tuple, and registered raw-byte
join in the two worlds.  P never observes the FD-4 enqueue edge.  Draining
the control queue first does not recover cross-socket send order.  Conversely,
rejecting merely because FD 4 is ready before G dequeues the grant would also
reject a compliant world in which the grant was sent first but both queues
became ready before G ran.  Holding the early packet until a grant exists
merges the worlds rather than distinguishing them.

The same problem recurs at activation.  Because the unchanged
`SESSION_CREATED request=DEC session=DEC` bytes are fully predictable from
already known values, the requester can enqueue byte-identical
`SESSION_AUTH_ACTIVATED` before receiving G's actual reply.  P cannot infer
its send edge after the queues converge.  `SESSION_AUTH_ACTIVE_RECEIPT` is
P-to-requester only; G receives no P-active capability or gate.  Thus after
commit G can receive a state-changing session operation while P is not yet in
`REGISTERED_ACTIVE`, contradicting the gate's required active-receipt-before-
operation order.

This is not repaired by trusting the requester, comparing the registered
bytes again, looking up the same tuple, choosing a poll priority, or adding a
record whose value the requester already knows.  Those operations preserve
the hostile pair.  The fixed four P--G record set also leaves no total causal
cancel/unwind table when a grant succeeds but its requester receipt fails,
the requester dies after receipt, an accepted report fails, commit creates
private state before a later send failure, or active/close receipts fail.

There is also a retained lifetime conflict: v4's exact requester lifecycle
closes FD 5 after its terminal FD-4 reply, whereas the v5-gate ordering puts
`SESSION_AUTH_CLOSED` and its receipt after `SESSION_CLOSED`.  The exhaustive
v5 supersession list does not authorize replacement of the v4 FD-5 lifetime
clauses.  The blocked amendment correctly installs neither contradictory
sequence.  `D-M1` therefore remains open at Major severity.

## E5. D-M2 independent acquisition, unwind, and quiescence audit

### D-M2 remains Major — the proposed acquisition is authority-inconsistent and not total

**Severity:** Major  
**Evidence anchors:** remediation-gate-v5 lines 94--115, 390--578;
amendment-v4 lines 185--195, 675--743, and 784--785;
blocked-amendment-v5 lines 214--284; current-review lines 2141--2181  
**Confidence:** 5/5 — direct holder contradiction plus partial-acquisition
and descriptor-ABA counterexamples

`pidfd_getfd(pidfd,targetfd,0)` supplies the missing actual-object operation:
on success it creates a new P-local descriptor referring to the target's
same open file description, which P can `fstat`.  But that very operation
conflicts with retained v4 authority for FD 5.  V4 states that requester FD 5
is never duplicated and freezes the child endpoint and P peer as exclusive
holders.  Gate v5 mandates `pidfd_getfd(child_pidfd,5,0)` while the child
original is live.  Its exhaustive supersession list replaces only v4
Section 4.5's phrase “no-follow actual-descriptor fstat” and the v2 syscall/
preflight inventory; it does not supersede v4 Section 3.1's no-duplicate rule
or holder cardinality.  Both clauses cannot be implemented simultaneously.

Even after that authority conflict were corrected, the proposed error
contract is not total.  Gate v5 defines normal duplicate disposal only after
both fstat values and both reciprocal Unix-diag results are fixed.  Consider
a first successful child or G-candidate `pidfd_getfd`, followed by failure of
the CLOEXEC check, `fstat`, proc comparison, Unix-diag query, a later
acquisition, or the zero/exactly-one/two-candidate test.  A P-local socket
duplicate now exists, but the normal-close precondition was never reached.
Jumping to the generic fatal kill/reap path lets that duplicate cross the
original endpoint close, keeps the Unix socket alive, and invalidates EOF,
peer-close, and absence evidence.  A successful `pidfd_open` followed by a
live-poll, identity, namespace, cgroup, start-time, or CLOEXEC failure has the
same unenumerated allocated-FD edge.

The two numeric G-descriptor snapshots are also insufficient without a
frozen quiescence capability.  “Single-threaded G” is not “G cannot mutate
its descriptor table.”  The gate names a corresponding frozen control state
but gives no exact P--G enter/acknowledge/exit records spanning the first
snapshot, every candidate `pidfd_getfd` and `fstat`, the second snapshot,
reciprocal comparison, duplicate disposal, and restored-holder proof.  G can
close descriptor number `N` and open a different socket at `N` between the
snapshots; the ordered numeric sets remain byte-identical.  Child barriers
and workers-cgroup freeze do not freeze G's own table.  Per-slot proc-
directory capability counts, flags, reset behavior, identity join, normal
close, every error close, and immediate EBADF proof are likewise not frozen.

These are operational inputs to the same actual-descriptor acquisition
contract, not optional implementation refinements.  The blocked amendment
truthfully refuses to install the contradictory/partial contract, so `D-M2`
remains open at Major severity.

## E6. Minimum corrected-gate and v6 contract

This is a repair threshold, not an authorization or a completed v6 design.
A later corrected gate must first authorize the exact narrow supersessions
that its operations require.

For `D-M1`, the minimum contract must provide a causal capability unavailable
before the predecessor event, not another copy of precommitted bytes:

1. a P-issued single-use create capability first revealed by the post-grant
   requester receipt, bound to the complete requester/session/request/method/
   trigger/owner/raw-byte tuple, and required by G on the actual FD-4 create;
   or one equally exact single causally ordered forwarding channel;
2. an actual-reply-dependent activation capability which cannot be computed
   or sent before the real `SESSION_CREATED`, plus an exact P-to-G ACTIVE
   gate required before every G-side state-changing session operation;
3. exact issuer, direction, bytes, cardinality, endpoint, credential, state,
   one-use, replay, tombstone, cancel, and close rules; and
4. a total send-failure/object/session unwind table for every partial grant,
   receipt, accept, commit, reply, activation, operation, and close state.

A fifth record name alone is insufficient: an already queued byte-identical
packet can wait until that record arrives unless it must carry a capability
that was genuinely unavailable when queued.

For `D-M2`, the minimum contract must:

1. explicitly supersede the exact v4 FD-5 no-duplicate, temporary-holder,
   and affected lifetime clauses only for the bounded P audit duplicate;
2. freeze each child/G pidfd and proc-directory capability count, open flags,
   CLOEXEC, process/start-time/namespace binding, reset, and lifetime;
3. add an exact G-quiesce enter/ACK/exit protocol covering both snapshots,
   every acquisition and comparison, all duplicate disposal, and restored-
   holder proof, while prohibiting close, dup, reopen, rights receipt, fork,
   signal-handler allocation, and every other G FD-table mutation;
4. enter one unconditional unwind after the first successful acquisition,
   close every obtained duplicate/proc FD exactly once on every normal or
   error edge, and require immediate `F_GETFD=-1/EBADF` without intervening
   allocation before any barrier release, original close, thaw, kill, or
   reap; and
5. freeze pidfd close/EBADF behavior both after failed post-open validation
   and after normal post-reap reconciliation.

Any later proposal still requires a fresh two-world attack and another
append-only independent review.  It cannot weaken the retained semantic,
metadata, possession, descriptor, ledger, manifest, theorem-owner, or Route
ceilings.

## E7. A-M4 count-five blocked-provenance successor

The immutable historical `v1` count-two, `v2` count-three, and `v3`
count-four receipts remain inside the preserved 119,250-byte prefix.  The
following is the sole active successor authorized by remediation-gate-v5
Section 7.  It records v5's exact no-op provenance and does not report repair
closure:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v4]
count=5
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The active block has count five, exact v1/v2/v3/v4/v5 order, no internal
blank or commentary line, and five independently recomputed current-byte
hashes.  A final verifier must authenticate this complete post-v5 review
before parsing, require the three immutable historical blocks plus this one
unique active block and no other tag, then capability-open and hash all five
paths before setting `R.effective_amendments=[v1,v2,v3,v4,v5]`.  V5's entry
is explicitly a failed/no-op chain member.  It cannot be used as an oracle
for either finding or as permission to implement.

## E8. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, arithmetic, authority-binding, manifest-cycle, foreign-deletion, or containment collapse |
| Major (`M`) | 2 | D-M1 causal capability absent; D-M2 acquisition authority/unwind/quiescence incomplete |
| Minor (`m`) | 0 | none |

V5 is a precise blocked record: it preserves the real counterexamples,
declines unauthorized widening, and adds no deceptive repair claim.  That is
sound provenance, not design closure.  Both operational worlds remain
under-determined by the effective bytes, and either one independently blocks
PASS.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v5.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=119250
PRESERVED_PREFIX_LINES=2308
PRESERVED_PREFIX_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
PRESERVED_NESTED_PREFIX_96524_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
PRESERVED_NESTED_PREFIX_74876_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
REVIEWED_PRE_V5_REVIEW_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
REVIEWED_REMEDIATION_GATE_V5_SHA256=55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7
REVIEWED_AMENDMENT_V5_SHA256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
V5_BLOCKED_NO_OP_PROVENANCE_BOUND=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V4_BLOCKED_SUCCESSOR
B_M1_REGRESSION=CLOSED
B_M2_REGRESSION=CLOSED
B_M3_REGRESSION=CLOSED
C_M1_DIRECT_REQUEST_PROVENANCE_AND_RAW_BYTE_JOIN_COMPLETE=true
C_M2_NETLINK_UNIX_DIAG_RECIPROCAL_ABI_COMPLETE=true
D_M1_CAUSAL_CAPABILITY_COMPLETE=false
D_M2_ACQUISITION_AUTHORITY_AND_TOTAL_UNWIND_COMPLETE=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M2_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c + v4 f5547926
+ blocked-v5 2204471c` versioned tuple: **REVISE — C0/M2/m0**.  The complete
119,250-byte historical review remains the exact prefix.  No implementation
gate, control execution, reproduction run, Route, composition, manuscript,
release, archive, or Git action is supported.  A corrected gate and a later
versioned repair must satisfy the minimum causal-capability, bounded-
supersession, total-unwind, and G-quiescence contracts above before another
fresh independent exact-byte closure review can consider PASS.

# Closure addendum v6: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V6 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v6.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M1/m0**  
Control implementation or execution performed: **no**

## F1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 2,746 lines and
143,812 bytes with SHA-256
`30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested prefix receipts remain:

| Prefix lines | Prefix bytes | Independently recomputed SHA-256 |
|---:|---:|---|
| 2,308 | 119,250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |
| 1,910 | 96,524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1,524 | 74,876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1,017 | 49,358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22,894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

I freshly read the complete effective-design chain, corrected v6 gate, and
review prefix, and independently recomputed these current-byte receipts:

| Record | Lines | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| corrected remediation gate v6 | 1252 | 62896 | `a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| complete pre-v6 review prefix | 2746 | 143812 | `30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb` | MATCH |

The v1--v5 remediation-gate lineage was also rehashed at its frozen digests.
I reparsed the base authority table and independently rehashed all fourteen
distinct, continuously indexed authority paths.  Every digest matches; the
aggregate remains 6,319 lines and 255,465 bytes.  The post-proof design gate
is still
`0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3`.

Before this review I reread in full the applicable ARS academic-research-
suite root, reviewer, methodology, domain, devil's-advocate, peer-review,
review-quality, report-template, experiment-integrity, reproducibility,
code-runner, academic-pipeline integrity, and reproducibility instructions.
I applied their exact-byte, independent-oracle, information-flow,
counterfactual, causal-falsifier, provenance, and evidence-gap standards.

I did not contact the author, read author dialogue, or use the v6 self-audit
as evidence.  I did not implement or run a generator, verifier, test,
wrapper, namespace/cgroup controller, entropy call, pidfd operation,
Unix-diag query, or other control.  Until this sole append the audit was
read-only.  No design, amendment, gate, implementation, pipeline, proof,
Route, manuscript, figure, release, archive, or Git record was changed.

## F2. Frozen invariants, prior closures, and DAG

Independent enumeration retains the exact vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The continuous body ranges still terminate at
`016,014,018,010,012,015,026,009`, totaling 120.  The negative partition is
`4+2+4+3+4+9+9+0=35`; literal header widths are
`18,19,22,17,16,19,13,10`; method arithmetic is
`10+10+14+9+10+12+12+5+18+10+35+28=173`, with distinct `S01..S35` and
`P01..P28`.  V6 values are operational and nonserialized; they add no schema
field, row, method, path, artifact, binding, detector, or exit class.

The DAG remains nodes `A,D,R,G,I,C,M,V`, seven chain edges, and five
additional `A,D,R,G,I -> M` edges: twelve distinct edges and the same unique
topological order.  There is no manifest self-hash, future-result edge,
concurrent proof hash, amendment node, or review/amendment digest cycle.

The prior closures survive regression:

- `A-M1`: all 35 primitive seeds retain one substantive mutation,
  independent canonical reparse, receipt-free typed rejection, post-reject
  detector, and inverse acceptance.  Expected fields and signature class are
  not oracle inputs; `SG_SCOPE` remains unparameterized.
- `A-M2`: whole-root recursive receipts retain root/directories/type/mode/
  size/hash/mtime/ctime/nlink/device/inode, valid/malformed roots, five live
  falsifiers, and pure selected-coordinate mode/mtime probes without ctime
  substitution.
- `A-M3`: both user namespaces, cgroup membership/freeze/kill, pidfd/
  PASSCRED/RPC/lock lifetimes, arch+x32 seccomp, residue/recursive/concurrent
  cleanup, and capability-relative foreign preservation remain closed.  The
  old seven `P19..P25` and new five replacement fixtures remain distinct.
- `B-M1..B-M3`: six pre-suite rows, closed owner/admission grammar, exact FD
  slots and FDSET rows, SANITIZED/ADMIT/SOURCE_READY/START barriers, two P
  audits, pre-access and post-reap registration/ACK, canonical set/order,
  `CHILD_REAPED_ACK`, P25 count zero, and partial/unexpected prohibitions
  remain exact.
- `C-M1/C-M2`: the v4 child-request direct audit and exact reciprocal
  40-byte/48-byte Unix-diag ABI remain present.
- `A-M4`: all four historical blocks remain byte-exact in the prefix; the
  active count-six successor below adds no manifest edge.

Exact-zero tolerance, bare compact group `B_p` theorem ownership,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and Route B false are unchanged.

## F3. Hostile v6 challenges

I sought worlds whose required predicates differ while the named decision
owner receives the same frozen observation.  `PASS` below is a bounded
design result, not a control-execution result.

| # | Hostile challenge | Independent result |
|---:|---|---|
| 1 | full chain/prefix/nested-prefix and fourteen authority hashes | PASS |
| 2 | all counts, headers, exact-zero ceiling, and 8/12 DAG | PASS |
| 3 | syscall 318, exact fills, collision/no-redraw, P-only retention, and three disclosure edges | PASS |
| 4 | early create lacks `create_cap`; early activation lacks `reply_nonce`; early operation lacks `active_cap` | PASS for requester early-queue causality |
| 5 | exact ten requester--P and ten P--G forms, closed enums, states, replay, and cleanup table | PASS for grammar; **REVISE for actual-evidence/terminal joins** |
| 6 | `CREATE_ACCEPTED` proving an actual requester FD-4 packet without G-only assertion | **REVISE: F-M1** |
| 7 | successful versus failed terminal-reply send after P's CLOSE_ACK | **REVISE: F-M1** |
| 8 | syscalls 434/438, flags zero, actual permission, bounded holder supersession, no fallback | PASS |
| 9 | four slot/kind rows, pidfds, proc FDs, identity/open/lifetime joins | PASS |
| 10 | four-record quiescence, two snapshots, every acquisition/fstat/diag, restored holders | PASS |
| 11 | partial returns, common reverse unwind, EBADF, pidfd close, and both ABA worlds | PASS |
| 12 | all prior closures, five blocks, six dereferences, no schema/path/Route widening | PASS |

Challenges 6 and 7 are counterexamples inside the one named D-M1 causal-
authorization and total-send-state contract.  They do not inflate the
finding count.  D-M2 closes independently.

## F4. D-M1 causal-capability review

The unpredictable values repair the v5 early-byte-identical queue attack.
A pre-receipt packet cannot contain `create_cap`; a pre-reply activation
cannot contain `reply_nonce`; and a pre-reply operation cannot contain
`active_cap`.  Exact fill, collision, disclosure, endpoint, state, request,
replay, and tombstone rules are sufficient for those requester worlds.

### F-M1 — two mandatory success predicates remain G-only or unobservable

**Severity:** Major  
**Evidence anchors:** corrected-gate-v6 lines 59--60, 282--342, 367--372,
478, 528--545, 1066--1072, and 1100; amendment-v6 lines 335--357,
438--505, 543--564, 589--590, and 605--635  
**Confidence:** 5/5 — two closed information-flow counterexamples

#### F-M1.a — G receives every byte needed to synthesize “actual” acceptance

`SESSION_AUTH_CREATE_GRANTED` gives G raw `create_cap` and hex of the complete
capability-bearing create payload.  `SESSION_AUTH_CREATE_ACCEPTED` later
contains only grant-available values: tuple coordinates, registration digest,
a deterministic hash of that raw capability, and the same payload.  P's
success edge compares this G record with its own grant and registration.

Compare two worlds after the identical grant and requester receipt:

```text
actual world:
  requester sends final SESSION_CREATE on FD 4
  G receives it and sends CREATE_ACCEPTED

false-accept world:
  requester sends no FD-4 create packet
  G sends byte-identical CREATE_ACCEPTED from its grant
```

P's observations, state, tuple, capability, payload, digest, endpoint table,
and accepted record are identical, but only the first world contains the
required actual requester packet and consumption.  The false world can
continue after P sends COMMIT because G then receives the future created
bytes and reply nonce.  Direct registration proves only the requester's
pre-capability proposal, not later secret-bearing FD-4 consumption.

This is the corrected gate's explicitly excluded G-self-report case.  Naming
the G payload “actual,” reserializing it, or hashing a capability G already
knows is tautological.  The rule that G must first receive a packet states the
desired operation but gives P no independent observation of it.

#### F-M1.b — P cannot distinguish terminal-reply send success from failure

Normal close is G close report, P CLOSE_ACK, then G's terminal FD-4
`SESSION_CLOSED` send.  P has no observation after its ACK: there is neither
a post-send G-to-P record nor a post-terminal requester-to-P FD-5 form.
Nevertheless, both ledgers are said to enter `CLOSED_TOMBSTONE` after the
terminal send, while the failure table requires a terminal-send failure to
make both ledgers failed tombstones.

Hold every pre-ACK byte and state fixed.  In world A G's terminal send returns
the complete length; in world B it fails or is incomplete.  Only G observes
that return.  If P enters successful close after its ACK, it falsely succeeds
in B; if it waits, A has no legal advancing event.  EOF cannot repair this
because the amendment forbids EOF from synthesizing a receipt or success.
The total failure table and P state machine therefore cannot both be
implemented.

These are not liveness or logging preferences.  Each forces a forbidden
same-party assertion, hard-coded success edge, or invented wire event.  They
are two manifestations of the same open D-M1 contract and count as one Major.

**Minimum repair contract:** version both D-M1 joins.  For create acceptance,
G must not receive raw `create_cap` or an equivalent forgeable complete
payload before the actual FD-4 packet.  Freeze a non-disclosing verifier,
require the actual packet to supply the secret, and give P a non-G-only,
kernel-authenticated observation or capability proof of exact consumption.
Bind its bytes/domain/direction/endpoint/credentials/cardinality/one-use/
wrong-first-attempt/replay/abort/tombstone behavior; a second G copy of grant-
derived bytes is insufficient.

For close, add a post-terminal-success observation before P enters
`CLOSED_TOMBSTONE`, such as a versioned requester-direct terminal receipt on
FD 5 joined to exact P--G finalization.  Freeze the changed form counts,
order, complete-send cardinality, requester close edge, EOF/crash behavior,
and every partial-send cleanup branch.  Moving existing records is adequate
only if the resulting P observation genuinely distinguishes the two worlds.

## F5. D-M2 repair review

D-M2 closes.  V6 narrowly supersedes v4's no-duplicate rule only for one
audit-local P duplicate of selected child FD 4/5/8 and each proc-selected G
candidate inside a quiesced interval.  Original ownership and FD5's terminal
lifetime remain exact outside it.

The sole calls are native x86_64 `pidfd_open=434` and `pidfd_getfd=438`, flags
zero.  A returned FD is ledgered before fallible validation, must have exact
CLOEXEC, and supplies actual-fstat evidence; proc text is comparison-only.
Actual successful `pidfd_getfd`, not inferred uid/capability/LSM state,
establishes permission, and every error is terminal without fallback.

The four kind/slot rows cover preflight FD8 and runtime FD8/FD4/FD5, binding
child/guardian pidfds, four fresh proc FDs, process identity, start time,
NSpid/credentials/cgroup, and any P-held FD5 peer.  The long-lived proc root
is separately named.  Child pidfds close/EBADF after reap; failed post-open
validation closes/EBADF on that error edge.

ENTER/ACK closes G work admission before snapshot 1 and prohibits every FD
allocation, replacement, close, rights receipt, fork, lazy open, and handler
allocation through EXIT_ACK.  The child stays at its barrier.  P's allocation
barrier confines its row opens/acquisitions.  Equal number sets therefore
cannot hide G ABA, and retaining acquired duplicates OPEN until common unwind
prevents P-local reuse.

P acquires/fstats the child endpoint then every increasing G candidate,
performs reciprocal Unix-diag, repeats both snapshots, and requires identity
and generation equality.  FD4/FD8 require one reciprocal G peer; FD5 requires
the child/P pair and zero matching G holders.  Transcript tags and failure/
missing markers bind observations rather than copied PASS tokens.

After the first row FD, success and every error enter one reverse unwind.
Every OPEN entry is closed once and immediately proved absent by same-number
`F_GETFD=-1/EBADF` without allocation.  Other closes continue after error.
Ambiguous absence forbids EXIT, thaw, START, original close, kill/reap
advancement, PASS, or ABSENT and falls to crash containment.  Clean unwind
requeries originals and restores permanent holders before EXIT/ACK.  This
closes partial acquisition, G quiescence, holder/proc/pidfd lifetime, and
dual-ABA counterexamples.

## F6. A-M4 count-six successor

The historical v1 count-two, v2 count-three, v3 count-four, and v4 count-five
blocks remain in the preserved prefix.  This is the sole active successor:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v5]
count=6
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block has count six, exact v1/v2/v3/v4/v5/v6 order, no internal blank or
commentary, and six recomputed hashes.  The verifier authenticates the
complete post-v6 review before parsing, requires four historical blocks plus
this unique active block, then capability-opens and hashes all six amendments
before setting `R.effective_amendments=[v1,v2,v3,v4,v5,v6]`.  Blocked v5
remains no-op provenance; this receipt is not its own oracle and adds no
manifest key, node, edge, self-hash, future-result edge, or proof cycle.

## F7. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, arithmetic, authority, manifest-cycle, foreign-deletion, or containment collapse |
| Major (`M`) | 1 | D-M1 actual-create evidence and terminal-reply success join remain incomplete |
| Minor (`m`) | 0 | none |

V6 genuinely closes the predictable early-queue attack and D-M2.  It does
not close full D-M1: one P success edge uses only values G already got in its
grant, and terminal send occurs after P's last success observation.  Either
counterexample blocks PASS under the gate's zero-finding rule.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v6.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=143812
PRESERVED_PREFIX_LINES=2746
PRESERVED_PREFIX_SHA256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
PRESERVED_NESTED_PREFIX_119250_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
PRESERVED_NESTED_PREFIX_96524_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
PRESERVED_NESTED_PREFIX_74876_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
REVIEWED_BLOCKED_AMENDMENT_V5_SHA256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
REVIEWED_PRE_V6_REVIEW_SHA256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
REVIEWED_CORRECTED_GATE_V6_SHA256=a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00
REVIEWED_AMENDMENT_V6_SHA256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V5_SUCCESSOR
B_M1_REGRESSION=CLOSED
B_M2_REGRESSION=CLOSED
B_M3_REGRESSION=CLOSED
C_M1_CHILD_REQUEST_DIRECT_AUDIT_REGRESSION=CLOSED
C_M2_UNIX_DIAG_ABI_REGRESSION=CLOSED
D_M1_EARLY_QUEUE_CAPABILITIES_COMPLETE=true
D_M1_ACTUAL_FD4_CREATE_EVIDENCE_INDEPENDENT_OF_G=false
D_M1_TERMINAL_REPLY_SUCCESS_JOIN_TOTAL=false
D_M2_BOUNDED_SUPERSESSION_COMPLETE=true
D_M2_PIDFD_PROC_IDENTITY_AND_PERMISSION_COMPLETE=true
D_M2_G_QUIESCENCE_AND_TWO_SNAPSHOTS_COMPLETE=true
D_M2_COMMON_UNWIND_EBADF_AND_DUAL_ABA_COMPLETE=true

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M1_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c + v4 f5547926
+ blocked-v5 2204471c + v6 0e8a90cf` tuple: **REVISE — C0/M1/m0**.  The
complete 143,812-byte historical review remains the exact prefix.  No
implementation gate, control execution, reproduction run, Route,
composition, manuscript, release, archive, or Git action is supported.
D-M1 requires a versioned repair and fresh independent append-only review.

# Closure addendum v7: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V7 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v7.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **REVISE — C0/M1/m0**  
Control implementation or execution performed: **no**

## G1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 3,149 lines and
165,177 bytes with SHA-256
`075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested prefix receipts were independently recomputed as:

| Prefix lines | Prefix bytes | Recomputed SHA-256 |
|---:|---:|---|
| 2,746 | 143,812 | `30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb` |
| 2,308 | 119,250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |
| 1,910 | 96,524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1,524 | 74,876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1,017 | 49,358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22,894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

I freshly read the complete effective-design chain, the v7 remediation
gate, and the full review prefix, and independently recomputed these exact
current-byte receipts:

| Record | Lines | Bytes | Recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| remediation gate v7 | 776 | 38865 | `a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576` | MATCH |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | MATCH |
| complete pre-v7 review prefix | 3149 | 165177 | `075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c` | MATCH |

The earlier remediation gates were also rehashed at their frozen digests.  I
reparsed the base authority registry and independently rehashed all fourteen
distinct paths.  Every digest matches; their aggregate remains 6,319 lines
and 255,465 bytes.  The original post-proof control-design gate remains
`0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3`.

Before this review I reread in full the applicable ARS academic-research-
suite root; reviewer, methodology, domain, devil's-advocate, peer-review,
review-quality, and report-template instructions; experiment-integrity,
reproducibility, and code-runner instructions; and academic-pipeline
integrity and reproducibility protocols.  I applied their exact-byte,
independent-oracle, information-flow, counterfactual, causal-falsifier,
provenance, and evidence-gap standards.

I did not contact the amendment author, inspect author dialogue, or use the
v7 self-audit as evidence.  I did not implement or run a generator,
verifier, test, wrapper, namespace/cgroup controller, entropy call, pidfd
operation, Unix-diag query, or any other control.  Until this sole append the
audit was read-only.  No design, amendment, gate, implementation, pipeline,
proof, Route, manuscript, figure, release, archive, or Git record was
changed.

## G2. Frozen invariants, prior closures, and DAG

Independent enumeration retains the exact invariant vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The eight continuous row ranges still terminate at
`016,014,018,010,012,015,026,009`, totaling 120.  The negative partition is
`4+2+4+3+4+9+9+0=35`; the literal headers split to
`18,19,22,17,16,19,13,10`; and the method arithmetic remains
`10+10+14+9+10+12+12+5+18+10+35+28=173`, with distinct `S01..S35` and
`P01..P28`.  V7 adds operational forms and receipts but no schema field,
row, method, path, artifact, authority binding, detector, or exit class.

The DAG remains nodes `A,D,R,G,I,C,M,V`, seven chain edges, and five
additional `A,D,R,G,I -> M` edges: twelve distinct edges and the same unique
topological order.  There is no manifest self-hash, future-result edge,
concurrent proof hash, amendment node, or review/amendment digest cycle.

The prior closures survive regression:

- `A-M1`: all 35 primitive seeds retain one substantive mutation,
  independent canonical reparse, receipt-free typed rejection, post-reject
  detector, and inverse acceptance; `SG_SCOPE` remains unparameterized.
- `A-M2`: whole-root recursive receipts retain root, directories, mode,
  size, hash, mtime, ctime, nlink, device, and inode; valid/malformed roots,
  five live falsifiers, and selected-coordinate mode/mtime probes remain.
- `A-M3`: both user namespaces, cgroup membership/freeze/kill, pidfd,
  PASSCRED, RPC, lock, residue, recursive/concurrent, signal/crash, and
  capability-relative foreign-preservation rules remain closed.
- `B-M1..B-M3`: the six fixed session-zero rows, exact owner/admission
  grammar, slots and phase FD sets, four start barriers, two P audits,
  pre-access and post-reap object ledgers, P25 count zero, and partial or
  unexpected-object containment remain exact.
- `C-M1/C-M2`: the requester-direct child-request witness and exact native
  40-byte/48-byte reciprocal Unix-diag ABI remain present.
- `D-M2`: the v6 bounded duplicate supersession, native pidfd permission,
  per-row proc capabilities, exact G quiescence, two snapshots, actual
  fstats, reciprocal diag, reverse unwind, EBADF proof, holder restoration,
  and both ABA exclusions remain byte-semantic invariants.  V7 redirects
  only FD-5's terminal close edge; no temporary duplicate crosses FINALIZE,
  ACK, receipt, EOF, reap, or peer close.
- `A-M4`: all five historical effective-amendment blocks remain byte-exact
  in the prefix, and the count-seven successor below adds no manifest edge.

Exact-zero tolerance, the bare compact group `B_p` theorem owner,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, Route B false, verify-only
read-only behavior, two fresh roots, three-way identity, recursive residue
checks, and no-cache/cleanup rules remain unchanged.

## G3. Hostile v7 contract challenges

I sought worlds whose required predicate differs while the named decision
owner receives the same frozen observation.  `PASS` here is a bounded design
result, not a control-execution result.

| # | Hostile challenge | Independent result |
|---:|---|---|
| 1 | complete base/v1--v7 chain, v7 gate, full and nested prefixes, and fourteen authority hashes | PASS |
| 2 | 6/8/120/35/35/28/173/9/14/2/3 counts, header widths, exact-zero ceiling, and 8/12 DAG | PASS |
| 3 | create grant discloses only template and commitment; actual raw cap/frame comes from one immutable first FD-4 receive | PASS under the explicit byte-bound trusted-G ceiling |
| 4 | wrong first create datagram consumes the attempt; no reparse, synthetic replacement, later packet, or retry | PASS under the same ceiling |
| 5 | ACTIVE records disclose only a commitment; first non-child operation supplies raw equality before mutation | PASS |
| 6 | no per-operation requester-provenance claim after G learns the session-scoped active cap | PASS; the evidence ceiling is explicit |
| 7 | complete requester--P FD-5 closed enum | PASS: exactly 12 forms |
| 8 | complete D-M1 P--G session closed enum | PASS: exactly 12 forms; four D-M2 forms remain separate |
| 9 | terminal full FD-4 seqpacket send, requester-direct same-buffer FD-5 observation, G full-send flag, FINALIZE, and FINALIZED_ACK join | PASS |
| 10 | terminal receipt, clean FD-5 EOF, requester exit/reap, inherited `CHILD_REAPED`, and P-peer absence | **REVISE: G-M1** |
| 11 | v6 D-M2 syscall/permission/identity/quiescence/unwind/ABA contract under the redirected FD-5 lifetime | PASS |
| 12 | prior closures, historical blocks, active count-seven block, seven dereferences, no schema/path/Route widening | PASS |

The core `F-M1.a` and `F-M1.b` information-flow counterexamples are closed
inside the gate's expressly bounded threat model.  The remaining finding is
a later lifecycle contradiction: it does not dispute the commitment or
terminal-send joins and does not add a second finding count.

## G4. D-M1 create, active, and terminal evidence review

The create grant contains neither raw `create_cap` nor the final frame.  Its
commitment covers the exact full frame and immutable identity with explicit
length separation.  A uniformly drawn 256-bit preimage is first disclosed
to the requester in the complete receipt.  G captures the first complete
FD-4 seqpacket before parsing and must return the raw slice and whole buffer
from that same object.  P compares those values with its independently held
secret/frame/identity ledger before COMMIT.  A rejected first packet cannot
be repaired or replaced.  This defeats v6's grant-derived synthetic-accept
world, subject to v7's explicit trusted, byte-bound, non-Byzantine G boundary.

The ACTIVE pair similarly carries only `active_cap_commitment`.  G cannot
accept the first later non-child mutation until the packet itself supplies a
matching raw value.  Once it learns the session-scoped value, v7 correctly
does not promote later repetitions into independent requester provenance.
The retained direct `AUDITED_SPAWN` witness and fresh terminal observation
remain the only claimed direct lanes; no ungranted per-operation theorem is
smuggled into the design.

For terminal completion, P draws a fourth, collision-checked
`terminal_cap` only after PREPARED and discloses it first to G in GRANTED.
G's exact full-datagram return and local flag are necessary but not
sufficient.  The requester must receive the exact FD-4 immutable frame and
send its raw capability and same bytes over the P-owned FD-5 peer.  P joins
that direct record before FINALIZE; G joins FINALIZE with its local full-send
flag before ACK.  Neither party's assertion alone satisfies the combined
predicate.  The complete enums are:

```text
FD5: OPEN, CHALLENGE, REGISTERED, RECEIPT, ACTIVATED, ACTIVE_RECEIPT,
     TERMINAL_OBSERVED, TERMINAL_RECEIPT,
     AUDIT_OPEN, AUDIT_CHALLENGE, AUDITED_SPAWN, AUDIT_RECEIPT

D-M1 P--G: CREATE_GRANTED, CREATE_ACCEPTED, COMMIT, COMMITTED,
           ACTIVE, ACTIVE_ACK, ABORT, ABORTED,
           TERMINAL_PREPARED, TERMINAL_GRANTED, FINALIZE, FINALIZED_ACK
```

No thirteenth form, compatibility alias, G-only terminal proof, or hard-coded
`PASS` is needed for those joins.

## G5. Finding and minimum repair contract

### G-M1 — post-FINALIZED_ACK control closure makes mandatory requester-reap reconciliation unreachable

**Severity:** Major  
**Evidence anchors:** amendment-v7 lines 584--594, 608--632, 844--878, and
934--940; inherited amendment-v2 lines 703, 740--742, and 844--850  
**Confidence:** 5/5 — deterministic normal-path and crash-path state
counterexample

V7 fixes an unavoidable order after G's complete `FINALIZED_ACK`:

```text
P validates FINALIZED_ACK
-> P completely sends TERMINAL_RECEIPT
-> requester receives the receipt and only then closes original FD 5
-> P observes clean FD-5 EOF
-> requester exits
-> G waitid-reaps that registered child
-> G sends inherited CHILD_REAPED to P
-> P reconciles reap, closes its retained peer, proves absence, and only then
   enters CLOSED_TOMBSTONE
```

The inherited control protocol makes `CHILD_REAPED` a G-to-P record and
requires G to send it for each registered direct child; P mirrors that
closed ledger.  Therefore this record necessarily occurs after
`FINALIZED_ACK`: the requester is forbidden to close FD 5 or exit before it
receives P's later TERMINAL_RECEIPT.

The same v7 bytes instead permit G to enter `CLOSED_TOMBSTONE` on its
complete ACK send, permit its later orderly P--G control close after P
validates that ACK, and state categorically that no post-ACK P--G message
exists.  They classify P--G EOF/crash as failure only before the final ACK.
These clauses cannot coexist with the required later G-to-P reap receipt.

A concrete compliant-prefix counterexample is:

1. G completely sends `FINALIZED_ACK` and enters its printed
   `CLOSED_TOMBSTONE`.
2. P validates the ACK; G takes the expressly permitted orderly control
   close, or crashes at the same post-ACK boundary.
3. P sends TERMINAL_RECEIPT; the requester receives it, closes FD 5, and
   exits.
4. G either cannot reap/send because it is gone, or can reap locally but has
   no legal post-ACK P--G message with which to deliver `CHILD_REAPED`.

If P nevertheless enters `CLOSED_TOMBSTONE`, it has fabricated the mandatory
reap reconciliation.  If it waits, an expressly permitted normal world has
no terminal transition.  EOF cannot supply the missing record because the
design forbids EOF from synthesizing receipts.  A post-ACK G crash is also
under-specified rather than distinguishable from the permitted orderly
close.

The failure totality has the same boundary defect.  A requester can queue
two `TERMINAL_OBSERVED` datagrams.  P may accept the first, send FINALIZE,
validate ACK, and only encounter the duplicate while draining toward clean
EOF.  The frozen duplicate row says “send no FINALIZE,” which is no longer
possible, and there is no post-ACK abort/control-crash transition.  This is
additional evidence for the same post-ACK lifecycle finding, not a second
counted Major.

**Minimum repair contract:** issue a bounded versioned correction which:

1. changes “no post-ACK P--G message” to “no post-ACK D-M1 session form” and
   explicitly preserves the inherited global control records;
2. keeps G, its control connection, child pidfd/ledger, and reap authority
   live until requester FD-4/FD-5 closure, G `waitid` reap, exact
   `CHILD_REAPED` delivery, any inherited applicable acknowledgment, P
   reconciliation, and retained-peer close/absence proof all finish;
3. distinguishes D-M1 authentication finalization from guardian/control
   lifecycle completion, so G's ACK may close the auth session without
   authorizing an early global-control close; and
4. freezes post-ACK control EOF/crash, queued-extra-frame, terminal-receipt,
   EOF, and reap failure transitions.  None may yield P success or false
   `ABSENT`; every already-sent FINALIZE/ACK remains an immutable fact rather
   than being retroactively described as unsent.

This repair needs no thirteenth FD-5 form, no thirteenth D-M1 session form,
no new CSV/method/path, and no weakening of D-M2.  It closes the lifetime of
the already inherited `CHILD_REAPED` control record instead of inventing a
new provenance channel.

## G6. A-M4 count-seven successor

The historical v1 count-two, v2 count-three, v3 count-four, v4 count-five,
and v5 count-six blocks remain in the preserved prefix.  This is the sole
active successor:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v6]
count=7
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block has count seven, exact v1/v2/v3/v4/v5/v6/v7 order, no internal
blank or commentary line, and seven independently recomputed hashes.  A
final verifier must authenticate the complete post-v7 review before parsing,
require five byte-identical historical blocks plus this unique active block
and no other tag, then capability-open and hash all seven amendment paths
before setting `R.effective_amendments=[v1,v2,v3,v4,v5,v6,v7]`.  Blocked v5
remains no-op provenance.  This receipt is not its own oracle and adds no
manifest key, node, edge, self-hash, future-result edge, or proof cycle.

## G7. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, arithmetic, authority, manifest-cycle, foreign-deletion, or containment collapse |
| Major (`M`) | 1 | post-ACK global-control/reap lifecycle is contradictory and its failure branches are not total |
| Minor (`m`) | 0 | none |

V7 genuinely closes v6's grant-derived create false accept and terminal-
send observability defect within its explicit trusted-G ceiling.  D-M2 and
all earlier semantic, metadata, possession, descriptor, object-ledger, and
manifest closures remain intact.  The mandatory requester-reap receipt is
nevertheless unreachable under another expressly permitted v7 edge.  Under
the zero-finding gate, that one deterministic counterexample blocks PASS.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v7.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=165177
PRESERVED_PREFIX_LINES=3149
PRESERVED_PREFIX_SHA256=075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c
PRESERVED_NESTED_PREFIX_143812_SHA256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
PRESERVED_NESTED_PREFIX_119250_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
PRESERVED_NESTED_PREFIX_96524_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
PRESERVED_NESTED_PREFIX_74876_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
REVIEWED_BLOCKED_AMENDMENT_V5_SHA256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
REVIEWED_AMENDMENT_V6_SHA256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
REVIEWED_PRE_V7_REVIEW_SHA256=075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c
REVIEWED_REMEDIATION_GATE_V7_SHA256=a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576
REVIEWED_AMENDMENT_V7_SHA256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V6_SUCCESSOR
B_M1_REGRESSION=CLOSED
B_M2_REGRESSION=CLOSED
B_M3_REGRESSION=CLOSED
C_M1_CHILD_REQUEST_DIRECT_AUDIT_REGRESSION=CLOSED
C_M2_UNIX_DIAG_ABI_REGRESSION=CLOSED
D_M2_BOUNDED_PIDFD_QUIESCENCE_UNWIND_REGRESSION=CLOSED
F_M1_CREATE_ACTUAL_FIRST_BUFFER_JOIN=CLOSED_WITHIN_TRUSTED_G_CEILING
F_M1_ACTIVE_COMMITMENT_AND_PROVENANCE_CEILING=CLOSED
F_M1_TERMINAL_DIRECT_SEND_JOIN=CLOSED
G_M1_POST_ACK_REAP_LIFECYCLE_TOTAL=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M1_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c + v4 f5547926
+ blocked-v5 2204471c + v6 0e8a90cf + v7 bbdd30c3` tuple:
**REVISE — C0/M1/m0**.  The complete 165,177-byte historical review remains
the exact prefix.  No implementation gate, control execution, reproduction
run, Route, composition, manuscript, release, archive, or Git action is
supported.  G-M1 requires a bounded versioned lifecycle repair and another
fresh independent append-only exact-byte review.

# Closure addendum v8: fresh independent exact-byte re-review

Status: **COMPLETE — APPEND-ONLY V8 EFFECTIVE-TUPLE RE-REVIEW**  
Closure review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v8.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Effective verdict: **PASS — C0/M0/m0**  
Control implementation or execution performed: **no**

## H1. Preserved prefix, exact authority, and independence

Immediately before this addendum, the review was exactly 3,567 lines and
187,634 bytes with SHA-256
`cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73`.
That complete byte string is the unmodified prefix of this addendum.  Its
nested prefix receipts were independently recomputed as:

| Prefix lines | Prefix bytes | Recomputed SHA-256 |
|---:|---:|---|
| 3,149 | 165,177 | `075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c` |
| 2,746 | 143,812 | `30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb` |
| 2,308 | 119,250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |
| 1,910 | 96,524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1,524 | 74,876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1,017 | 49,358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22,894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

I freshly read the complete base, all eight amendments, the complete review
prefix, and the corrected v8 remediation gate, and independently recomputed
these current-byte receipts:

| Record | Lines | Bytes | Recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | MATCH |
| corrected remediation gate v8 | 852 | 43684 | `342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8` | MATCH |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | MATCH |
| complete pre-v8 review prefix | 3567 | 187634 | `cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73` | MATCH |

The corrected v8 gate's first 599 lines / 31,194 bytes independently retain
SHA-256
`f8397076858012c13c657108cf7903f674d4bb0e880b127d477b2af7c8c3976d`.
All earlier remediation gates were rehashed at their frozen digests.  I also
reparsed the base authority registry and independently rehashed all fourteen
distinct paths.  Every digest matches; their aggregate remains 6,319 lines
and 255,465 bytes.  The original post-proof design gate remains
`0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3`.

Before this review I reread in full the applicable ARS academic-research-
suite root; reviewer, methodology, domain, devil's-advocate, peer-review,
review-quality, and report-template instructions; experiment-integrity,
reproducibility, and code-runner instructions; and academic-pipeline
integrity and reproducibility protocols.  I applied their exact-byte,
independent-oracle, information-flow, counterfactual, causal-falsifier,
provenance, reproducibility, and no-evidence-gap standards.

I did not contact the amendment author, inspect author dialogue, or use the
v8 author-side audit as evidence.  I did not implement or run a generator,
verifier, test, wrapper, namespace/cgroup controller, entropy call, pidfd
operation, Unix-diag query, or any other control.  Until this sole append the
audit was read-only.  No design, amendment, gate, implementation, pipeline,
proof, Route, manuscript, figure, release, archive, or Git record was
changed.

## H2. Frozen invariants, prior closures, and DAG

Independent enumeration retains the exact invariant vector:

```text
implementation paths                         6
CSV artifacts                                8
CSV body rows                              120
header widths                18,19,22,17,16,19,13,10
explicit negative rows                      35
semantic mutation classes                   35
package mutation classes                    28
unittest methods                           173
generated artifacts including manifest       9
authority bindings                          14
fresh canonical generations                  2
byte-identical canonical copies              3
manifest nodes / distinct edges           8 / 12
```

The eight continuous row ranges still terminate at
`016,014,018,010,012,015,026,009`, totaling 120.  The negative partition is
`4+2+4+3+4+9+9+0=35`; the eight literal headers split to
`18,19,22,17,16,19,13,10`; and the method arithmetic remains
`10+10+14+9+10+12+12+5+18+10+35+28=173`, with distinct `S01..S35` and
`P01..P28`.  V8 adds only operational states, guards, ledgers, and retained
lifetime edges.  It adds no schema field, CSV row, method, path, artifact,
authority binding, detector, public exit class, or generated byte.

The DAG remains nodes `A,D,R,G,I,C,M,V`, seven chain edges, and the five
additional `A,D,R,G,I -> M` edges: twelve distinct edges and the same unique
topological order.  There is no manifest self-hash, future-result edge,
concurrent proof hash, amendment node, or review/amendment digest cycle.

The prior closures survive regression:

- `A-M1`: all 35 primitive seeds retain one substantive mutation,
  independent canonical reparse, receipt-free typed rejection, post-reject
  detector, and inverse acceptance; `SG_SCOPE` remains unparameterized.
- `A-M2`: whole-root recursive receipts retain root, directories, type,
  mode, size, hash, mtime, ctime, nlink, device, and inode; valid/malformed
  roots, five live falsifiers, and selected-coordinate mode/mtime probes
  remain exact without ctime substitution.
- `A-M3`: both user namespaces, atomic cgroup placement, membership/freeze/
  kill/reap, pidfd, PASSCRED, RPC, lock, residue, recursive/concurrent,
  signal/crash, retained capability, foreign-preservation, and no-false-
  `ABSENT` rules remain closed.  The old seven `P19..P25` and new five
  replacement fixtures remain distinct.
- `B-M1..B-M3`: the six pre-suite rows, exact owner/admission grammar,
  phase-indexed descriptor sets, four start barriers, two P audits,
  pre-access and post-reap object registration/ACK/ledger ordering, P25
  count zero, and partial/unexpected-object containment remain exact.
- `C-M1/C-M2`: the requester-direct child-request witness and exact native
  40-byte/48-byte reciprocal Unix-diag ABI remain present.
- `D-M2`: the bounded temporary-holder supersession, exact syscall and
  runtime-permission checks, child/guardian pidfd and per-row proc
  capabilities, G quiescence, two snapshots, actual fstats, reciprocal
  diag, common reverse unwind, immediate EBADF, holder restoration, and both
  ABA exclusions remain exact.  No audit-local FD crosses its `EXIT_ACK` or
  the validated-global-`EXIT` disposal edge.
- V7's create, active, and terminal joins remain closed within its explicit
  byte-bound trusted, non-Byzantine G ceiling.  The exact twelve FD-5 and
  exact twelve D-M1 session forms remain unchanged.
- `A-M4`: all six historical effective-amendment blocks remain byte-exact in
  the preserved prefix, and the count-eight successor below adds no
  manifest edge.

Exact-zero tolerance, the bare compact group `B_p` theorem owner,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, Route B false, verify-only
read-only behavior, two fresh roots, three-way identity, recursive residue
checks, no-cache/cleanup rules, and foreign-object preservation remain
unchanged.

## H3. Hostile v8 contract challenges

I sought pairs of worlds whose required predicate differs while the named
decision owner receives the same frozen observations.  `PASS` below is a
bounded design result, not a control-execution result.

| # | Hostile challenge | Independent result |
|---:|---|---|
| 1 | complete base/v1--v8 chain, corrected gate, full/nested prefixes, and fourteen authority hashes | PASS |
| 2 | 6/8/120/35/35/28/173/9/14/2/3 counts, widths, exact-zero ceiling, and 8/12 DAG | PASS |
| 3 | `FINALIZED_ACK` closes only D-M1 auth while G, its control endpoint, requester pidfd, identity, ledger, and reap authority stay live | PASS |
| 4 | complete terminal receipt, FD-5 no-extra clean EOF, FD-4 anomaly-free drain, requester exit, exact waitid/status/process-gone join | PASS |
| 5 | inherited `CHILD_REAPED` followed by mandatory inherited `CHILD_REAPED_ACK`, exact field repetition, state guards, and single attempts | PASS |
| 6 | direct-child session versus opaque auth-session mapping, pidfd/credential/cgroup identity, and terminal-ledger joins | PASS within the retained byte-bound trusted-G ceiling |
| 7 | auth-reap ACK closes only the auth reap join; same control remains live for inherited global `FINAL` | PASS |
| 8 | exact `FREEZE_REQUEST/FROZEN_FINAL/KILL_REQUEST/KILL_ISSUED/REAPED/CGROUP_EMPTY/CLEANUP_RESULT*/SIGNAL_CLEANED?/EXIT` order | PASS |
| 9 | validated `EXIT` before any permitted EOF, followed by G exit, exact P pidfd reap, populated-zero, and ordered cgroup removal | PASS |
| 10 | partial/missing/duplicate reap or ACK, early EOF/crash, duplicate FD-5, late FD-4, malformed/out-of-order global record, and cleanup-proof failures | PASS: every world fails closed or makes no progress |
| 11 | exact 12 FD-5 / 12 D-M1 form counts, no new wire form, and no D-M2 regression | PASS |
| 12 | six historical blocks, unique active count-eight block, eight independent dereferences, and no schema/path/Route widening | PASS |

No challenge produced a false-success world, unreachable specified normal
terminal state, tautological comparison, hard-coded `PASS`, token-lookup
acceptance, or under-determined exact byte.

## H4. G-M1 post-ACK lifecycle closure

V8 closes the exact v7 counterexample.  A complete `FINALIZED_ACK` now moves
G to `FINALIZED_AWAITING_REAP`, not global `CLOSED_TOMBSTONE`.  G is forbidden
to close or half-close the control endpoint or discard requester identity,
pidfd, ledger, or reap authority.  The D-M1 session is sealed, but inherited
global records remain legal on the same authenticated connection.

The independently reconstructed clean suffix is:

```text
G complete FINALIZED_ACK -> FINALIZED_AWAITING_REAP
P validates ACK -> complete TERMINAL_RECEIPT
requester closes FD 5 -> P observes identity-valid clean FD-5 EOF
requester closes FD 4 after terminal observation
G drains FD 4 to clean EOF, rejects every queued/late byte, closes peer,
  fixes holder absence, then waitid-reaps the exact requester
G complete CHILD_REAPED
P joins registered child/status, auth mapping, identity, FD4/FD5 ledgers,
  closes/proves child pidfd and FD-5 peer absent
P complete CHILD_REAPED_ACK
G validates ACK -> AUTH_REAP_RECONCILED
same live control executes inherited global FINAL through complete EXIT
G exits
P pidfd-reaps exact G, proves guardian/session populated zero, and removes
  empty workers/guardian/session cgroups in order
```

Each send advances state only on its complete return; each receive advances
state only after exact validation.  P's complete reap-ACK send alone is not
G's acceptance.  `AUTH_REAP_ACK_SENT` and `AUTH_REAP_RECONCILED` close only
the auth-session reap join and cannot authorize a result, endpoint close, or
skip any global `FINAL` record.

The earlier v7 early-close world is therefore no longer conforming.  If G
closes immediately after `FINALIZED_ACK`, if P closes after the auth-reap
ACK, or if either endpoint reaches EOF before P validates `EXIT`, the exact
v8 rule is failure.  Earlier terminal, receipt, reap, or ACK facts stay
immutable but cannot upgrade that failed global lifecycle.  After validated
`EXIT`, EOF remains only a consequence: it does not replace exact G reap,
identity, populated-zero, cgroup-removal, or final-ledger proof.

The late-byte worlds are also closed.  G must complete the FD-4 drain and
holder-removal predicate before `REQUESTER_REAPED` and before constructing a
success-valid `CHILD_REAPED`.  A queued extra FD-4 datagram, partial frame,
ancillary item, duplicate close, capability-bearing operation, wrong status,
or identity drift prevents that record.  P therefore sends no ACK.  The same
canonical reap bytes cannot be relabelled as failure evidence.  On FD 5, P
requires no queued duplicate or extra datagram before accepting EOF; a
duplicate discovered after already completed FINALIZE/ACK is retained as
history plus failure, never rewritten into the impossible claim that those
sends did not occur.

The complete failure table distinguishes terminal-receipt failure, FD-5
early EOF/extra input, FD-4 extra input, post-ACK D-M1 input, identity and
waitid defects, wrong/duplicate reap, nonempty post-reap state, both reap
record send/validation failures, every global-FINAL record or proof defect,
invalid/missing EXIT, either crash direction, premature control disposal,
post-EXIT disposal failure, G-reap failure, cgroup-final failure, pidfd/peer
absence failure, and final-ledger failure.  A living side preserves only its
reachable containment evidence; a dead peer receives no fabricated state.
Physical cleanup or clean-looking EOF never erases the first cause or yields
false `ABSENT` or PASS.

The FD-4 ledger join is not a new Byzantine-G provenance claim.  Under the
unchanged v7 byte-bound trusted-G ceiling, the inherited `CHILD_REAPED` state
guard is emitted only after G's actual anomaly-free drain, exact requester
reap, and retained ledger are fixed.  P joins that authenticated receipt to
its independent direct terminal observation, FD-5 EOF, immutable child/auth
mapping, pidfd/credential/cgroup identity, and expected status.  A Byzantine
G that forges its state remains explicitly outside the theorem; within the
claimed model there is no same-observation counterexample or tautological
oracle.

G-M1 is therefore closed by the v8 bytes.  No minimum repair contract
remains.

## H5. A-M4 count-eight successor

The historical v1 count-two, v2 count-three, v3 count-four, v4 count-five,
v5 count-six, and v6 count-seven blocks remain in the preserved prefix.  This
is the sole active successor:

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v7]
count=8
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block has count eight, exact v1/v2/v3/v4/v5/v6/v7/v8 order, no internal
blank or commentary line, and eight independently recomputed hashes.  The
final verifier must authenticate the complete post-v8 review before parsing,
require six byte-identical historical blocks plus this unique active block
and no other tag, then capability-open and independently hash all eight
amendment paths before setting
`R.effective_amendments=[v1,v2,v3,v4,v5,v6,v7,v8]`.  Blocked v5 remains
no-op provenance.  This receipt is not its own oracle and adds no manifest
key, node, edge, self-hash, future-result edge, or proof cycle.

## H6. Effective verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, arithmetic, authority, manifest-cycle, foreign-deletion, or containment collapse |
| Major (`M`) | 0 | G-M1 is closed; no remaining design acceptance, observability, lifecycle, or totality finding |
| Minor (`m`) | 0 | none |

V8 supplies the missing post-`FINALIZED_ACK` lifecycle without changing a
wire-form count: it preserves the inherited requester reap and ACK, keeps the
same control alive through the inherited global `FINAL`, rejects every early
EOF/crash/duplicate/late-byte world, and requires validated `EXIT` followed
by the already frozen G-reap and cgroup proofs.  V7, D-M2, all earlier
semantic/metadata/possession/descriptor/object-ledger closures, exact counts,
and A-M4 remain intact.  Under the zero-finding gate, the effective design
therefore passes exact-byte review.

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v8.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_BYTES=187634
PRESERVED_PREFIX_LINES=3567
PRESERVED_PREFIX_SHA256=cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73
PRESERVED_NESTED_PREFIX_165177_SHA256=075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c
PRESERVED_NESTED_PREFIX_143812_SHA256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
PRESERVED_NESTED_PREFIX_119250_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
PRESERVED_NESTED_PREFIX_96524_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
PRESERVED_NESTED_PREFIX_74876_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
PRESERVED_NESTED_PREFIX_49358_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
PRESERVED_NESTED_PREFIX_22894_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec

REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
REVIEWED_BLOCKED_AMENDMENT_V5_SHA256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
REVIEWED_AMENDMENT_V6_SHA256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
REVIEWED_AMENDMENT_V7_SHA256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
REVIEWED_PRE_V8_REVIEW_SHA256=cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73
REVIEWED_CORRECTED_GATE_V8_SHA256=342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8
REVIEWED_CORRECTED_GATE_V8_PREFIX_SHA256=f8397076858012c13c657108cf7903f674d4bb0e880b127d477b2af7c8c3976d
REVIEWED_AMENDMENT_V8_SHA256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
ARS_METHODS_REREAD_IN_FULL=true
REVIEW_INDEPENDENT_OF_AUTHOR_DIALOGUE=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false

AUTHORITY_BINDINGS_REHASHED=14
AUTHORITY_BINDING_MISMATCHES=0
CSV_ARTIFACTS_RECOMPUTED=8
GENERATED_ARTIFACTS_RECOMPUTED=9
HEADER_WIDTHS_RECOMPUTED=18,19,22,17,16,19,13,10
CSV_BODY_ROWS_RECOMPUTED=120
EXPLICIT_NEGATIVE_ROWS_RECOMPUTED=35
SEMANTIC_MUTATION_CLASSES_RECOMPUTED=35
PACKAGE_MUTATION_CLASSES_RECOMPUTED=28
UNITTEST_METHODS_RECOMPUTED=173
FRESH_GENERATIONS_RECOMPUTED=2
BYTE_IDENTICAL_COPIES_RECOMPUTED=3
MANIFEST_NODES_RECOMPUTED=8
MANIFEST_DISTINCT_EDGES_RECOMPUTED=12
MANIFEST_SELF_HASH_PRESENT=false
MANIFEST_FUTURE_RESULT_EDGE_PRESENT=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

A_M1_REGRESSION=CLOSED
A_M2_REGRESSION=CLOSED
A_M3_REGRESSION=CLOSED
A_M4_REGRESSION=CLOSED_WITH_ACTIVE_V7_SUCCESSOR
B_M1_REGRESSION=CLOSED
B_M2_REGRESSION=CLOSED
B_M3_REGRESSION=CLOSED
C_M1_CHILD_REQUEST_DIRECT_AUDIT_REGRESSION=CLOSED
C_M2_UNIX_DIAG_ABI_REGRESSION=CLOSED
D_M2_BOUNDED_PIDFD_QUIESCENCE_UNWIND_REGRESSION=CLOSED
V7_CREATE_ACTUAL_FIRST_BUFFER_JOIN_REGRESSION=CLOSED
V7_ACTIVE_COMMITMENT_AND_PROVENANCE_CEILING_REGRESSION=CLOSED
V7_TERMINAL_DIRECT_SEND_JOIN_REGRESSION=CLOSED
G_M1_POST_ACK_REAP_LIFECYCLE=CLOSED_BY_V8_DESIGN
V8_CONTROL_EOF_SUCCESS_STATE_PRESENT=false
V8_VALIDATED_EXIT_BEFORE_EOF_REQUIRED=true
V8_G_REAP_AND_CGROUP_FINAL_REQUIRED=true

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=PASS_C0_M0_m0

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

Final disposition on the exact
`base db590ae2 + v1 cd0b4ab2 + v2 c1d104d2 + v3 f6a0af9c + v4 f5547926
+ blocked-v5 2204471c + v6 0e8a90cf + v7 bbdd30c3 + v8 e3d66503`
tuple: **PASS — C0/M0/m0** for deterministic-control design only.  The
complete 187,634-byte historical review remains the exact prefix.  This does
not implement or execute the controls and does not authorize a reproduction
run, Route, composition, manuscript, release, archive, or Git action.  A
separate implementation gate remains the appropriate next step.

# Fresh design-reopen review: post-attestation P-to-G release

Status: **REVISE — C0/M1/m0**  
Review ID: `P15R-P2-CONTROL-DESIGN-REOPEN-REVIEW-v1.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static design audit  
Finding under adjudication: missing post-`PRIVILEGE_DROP_ATTESTED`
P-to-G release before `GUARDIAN_READY` and lock-state mutation  
Implementation, execution, amendment, and source authority: **none**

## Scope, independence, and evidence boundary

I freshly read in full the ARS academic-research-suite root and the applicable
academic reviewer, methodology, domain, devil's-advocate,
experiment-integrity, and reproducibility instructions before adjudicating
this question.  I then freshly read and re-hashed the complete reopen gate,
base design, amendments v1 through v8, the blocked/no-op v5 provenance
record, this review's complete existing prefix, both implementation gates,
and the six current provisional source files.  I did not import, source,
compile, parse as an AST, or execute project code; invoke a generator,
verifier, unittest, wrapper, platform probe, or reproduction path; or create
any generated, temporary, cache, result, or manifest member.

The finding below is derived from the frozen design chain.  The current
source tuple is used only for static corroboration and cannot define, amend,
or rescue design meaning.  Neither the reopen gate's proposed
classification nor the replacement author's reported result was treated as
an oracle.

The immutable pre-append review prefix was independently verified
immediately before this append:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=3961
PRESERVED_PREFIX_BYTES=209656
PRESERVED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PRESERVED_PREFIX_VERDICT=PASS_C0_M0_m0
PREFIX_REWRITE_PERFORMED=false
```

That historical PASS remains a byte-identical prefix.  This addendum
supersedes its current adjudicative result only for the newly reviewed exact
effective tuple; it does not rewrite any historical text.

## Independent reconstruction of the operative boundary

Amendment v2 Section 5.3 is the operative bootstrap authority.  Its state
sequence contains, in order,
`CGROUP_PREFLIGHTED -> LAUNCHER_REAPED -> PRIVILEGE_DROP_ATTESTED ->
GUARDIAN_READY -> BOOTSTRAP_FAILED`, and it says that only
`GUARDIAN_READY` may enter lock state.  Creation step 10 has P reap L,
verify that the guardian contains exactly G, and send
`LAUNCHER_REAPED outer_pid=DEC`.  G may not bind the package lock, create a
generation root, or advertise READY before receiving that record.

Creation step 11 then assigns different work to the two principals.  G
hides cgroup2, closes setup-only descriptors, drops and locks its capability
and securebits state, sets `no_new_privs=1` and dumpable zero, and revalidates
the source boundary.  P alone creates the disposable initial-user-namespace
uid/gid-65534 probe, observes the required denials against G's proc
fd/root/namespace entries, kills and reaps the probe, and independently
re-reads G's status and cgroup membership.  The design names completion of
those P-owned observations `PRIVILEGE_DROP_ATTESTED` and requires that only
then may G send `GUARDIAN_READY`.

The inherited bootstrap channel cannot carry that result: it contains only
the exact U1/U2 mapping sequence and closes after
`CONTROL_AUTHENTICATED`.  On the authenticated P--G channel, every legal
P-to-G observation before this boundary is already exhausted by
`WORKERS_CGROUP_FD`, the applicable `CGROUP_PROBE_FROZEN`,
`CGROUP_PROBE_THAWED`, and `CGROUP_PROBE_KILLED` records, and finally
`LAUNCHER_REAPED`.  All of them precede P's step-11 denial probe and status
re-read, so none can encode its result.

The next closed-enum record is
`GUARDIAN_READY outer_pid=DEC inner_pid=1`, but it is G-to-P.  The direction
and cardinality paragraph makes `LAUNCHER_REAPED` P-to-G and
`GUARDIAN_READY` G-to-P, each once in that order.  It defines no legal
P-to-G record, ACK, one-use capability, ancillary object, or other positive
fact after P's attestation and before G's READY decision.  Later P-to-G
records such as `CHILD_ADMITTED`, freeze/kill/empty receipts, or
`SIGNAL_PENDING` have later transaction state guards and cannot be moved to
or reinterpreted at bootstrap under the closed-enum and wrong-state rules.
`LOCK_BOUND` is G-to-P and occurs only after a successful bind and complete
CREATED receipt, so it is downstream rather than a release.

Unknown, duplicate, reordered, wrong-direction, wrong-state, partial, and
EOF cases are fail-closed.  That containment does not communicate a
successful P observation.  A control close or failure that P causes after a
failed probe is only negative evidence and can race a G action; absence of
such a close is not positive attestation.

## Fixed-observation two-world attack

I tested both required schedules while fixing every byte and fact available
to G at the decision point.

**PASS schedule.** P has sent the one exact `LAUNCHER_REAPED` record; G
performs its local drop; P's disposable probe receives every required
denial, is killed and reaped, and P's status/cgroup re-reads match.  P may
therefore enter its local `PRIVILEGE_DROP_ATTESTED` state.

**FAIL schedule.** The P-to-G bytes, G-local actions, G-visible kernel facts,
and scheduler prefix available to G are identical.  One P-only required
observation differs: for example, the probe unexpectedly opens one governed
proc entry, or the independent status/cgroup re-read mismatches.  P must
enter `BOOTSTRAP_FAILED` and may not enter
`PRIVILEGE_DROP_ATTESTED`.

Because no post-observation P-to-G event exists, G has the same complete
observation in the two worlds.  A deterministic G rule that sends
`GUARDIAN_READY` sends it in both worlds and violates “only then” in FAIL.
A rule that waits in both worlds has no legal advancing event in PASS and
cannot implement the specified success path.  Randomization cannot turn an
unobserved P fact into a safety proof.  Time, polling order, scheduler
priority, absence of failure, copied state names, G's own local drop check,
transport write completion, EOF, or an implementation convention likewise
does not distinguish the two worlds.

The mutation consequence is reachable, not merely terminological.  Once G
prematurely advertises READY, the state rule permits lock-state entry.
Amendment v2 Section 5.7 then permits G, before `ACQUIRING`, to create the
private candidate through `tmp_fd`, create/fsync/re-read its exact `.owner`,
then transition `UNOWNED -> ACQUIRING` and call bind; a generation root is
also prohibited only before the earlier launcher/READY gates.  Schedule G
through any of those permitted actions before P's failed observation is
delivered as a close or otherwise noticed, and FAIL contains a forbidden
post-bootstrap mutation.  Fail-closed handling after the fact cannot supply
the missing causal precondition.

## Supersession and alleged-equivalent audit

The complete authority chain supplies no existing-semantic substitute:

- The relevant v2 bootstrap, exact wire enum, direction/cardinality,
  state-order, and lock-mutation clauses are not expressly superseded at
  this boundary.
- V3's child/source/start/reap and object-ledger refinements are later
  admission and transaction records, not a privilege-drop bootstrap
  release.
- V4's peer-oracle preflight and requester audit additions occur either
  before U1 mapping or in later request handling; its new audit records do
  not carry P's step-11 observation to G.
- V5 is explicitly blocked/no-op provenance and supersedes no operative
  clause.
- V6's authentication-session and descriptor-audit records and v7's
  create/active/terminal commitments govern later requester sessions.  No
  such record is legal at this bootstrap boundary.
- V8 is expressly confined to the post-`FINALIZED_ACK` global-control,
  EOF, exit, reap, and final-cgroup lifecycle.  It changes no pre-ACK or
  bootstrap semantics.
- The two implementation gates are governance records, expressly not
  design amendments, and therefore cannot add the missing edge.

Consequently there is no existing record to reinterpret and no express
supersession that defeats the fixed-observation counterexample.

## Static provisional-source corroboration and evidentiary ceiling

The six-file provisional tuple remains quarantined, stopped, unfrozen, and
unaccepted.  Its complete static read corroborates rather than closes the
design finding.  In `experiments/reproduce.sh`, `BASE_CONTROL_FORMS`
(lines 145--147) and `WIRE_SPECS` (lines 347--357) include P-to-G
`LAUNCHER_REAPED` and G-to-P `GUARDIAN_READY` but no post-attestation
P-to-G form.  `guardian_bootstrap` receives `LAUNCHER_REAPED` at lines
4232--4233 and sends `GUARDIAN_READY` at line 4237 without awaiting a P
attestation release.  P sends `LAUNCHER_REAPED` and then waits for READY at
lines 4395--4396; the READY handler calls
`attest_guardian_privilege_drop` only afterward at line 2413.  Thus these
bytes reverse the required causal order rather than establish an implicit
edge.  The following `run_after_preflight` can bind at line 3727 and create
the candidate and `.owner` at lines 3731--3735 while P's P-only attestation
is still pending.

These observations are not an implementation review, do not add another
finding, and cannot modify the design verdict.  No source path is accepted
or admitted by this review.

## Adjudicated finding and minimum closure obligation

**P15R-REOPEN-M1 — G has no causal evidence that P completed
`PRIVILEGE_DROP_ATTESTED` before READY and lock mutation.**

Severity is **Major** with high confidence.  The omission defeats an
implementable success path and a required safety precondition, but it is
locally repairable without evidence here of an unrecoverable research-wide
failure.  The adjudicated count is therefore exactly C0/M1/m0.

A future, separately authorized design amendment can close this finding
minimally by adding one authenticated exact record, for example
`PRIVILEGE_DROP_RELEASE outer_pid=DEC`, with all of the following normative
properties:

1. P sends it exactly once only after its disposable denial probe has passed
   completely, the probe is killed/reaped, and its independent G
   status/cgroup re-reads pass; P emits no release in any failure world.
2. G accepts it exactly once, on the existing authenticated P--G channel,
   only after receiving `LAUNCHER_REAPED` and completing its own local drop;
   `outer_pid` is joined to the retained G identity.
3. Before complete canonical receipt and validation, G may not send
   `GUARDIAN_READY`, enter any lock state, create the candidate or `.owner`,
   call bind, or create a generation root.
4. Missing, duplicate, reordered, malformed, wrong-direction, wrong-state,
   partial, EOF, timeout, P/G crash, and transport-error cases remain total
   fail-closed paths with no prohibited mutation and no inference from
   silence.
5. The future amendment must expressly supersede the affected v2 bootstrap
   sequence, closed enum, exact payload, direction/cardinality, transition,
   and failure-containment clauses and must prove both fixed-observation
   worlds.  Only a later, separately authorized source attempt may then
   implement the amended bytes.

This is a nonauthorizing minimum closure obligation, not an amendment,
reserved name, source instruction, or permission to create v9.  No design
amendment path is written or authorized here.

## Final disposition and authority matrix

```text
REOPEN_REVIEW_ID=P15R-P2-CONTROL-DESIGN-REOPEN-REVIEW-v1.0
REOPEN_GATE_SHA256=8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973
REVIEWED_BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEWED_AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
REVIEWED_AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
REVIEWED_AMENDMENT_V3_SHA256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
REVIEWED_AMENDMENT_V4_SHA256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
REVIEWED_BLOCKED_NOOP_V5_SHA256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
REVIEWED_AMENDMENT_V6_SHA256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
REVIEWED_AMENDMENT_V7_SHA256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
REVIEWED_AMENDMENT_V8_SHA256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
ORIGINAL_IMPLEMENTATION_GATE_SHA256=e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8
IMPLEMENTATION_REMEDIATION_GATE_V1_SHA256=52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f

FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
SOURCE_USED_AS_DESIGN_AUTHORITY=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
REOPEN_REVIEW_VERDICT=REVISE_C0_M1_m0
FINDING_ID=P15R-REOPEN-M1
FINDING_STATUS=OPEN_REQUIRES_SEPARATE_DESIGN_REMEDIATION_AUTHORITY

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
DESIGN_AMENDMENT_AUTHORIZED=false
DESIGN_V9_AUTHORIZED=false
SOURCE_EDIT_OR_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact frozen effective design tuple is
**REVISE — C0/M1/m0**.  The missing post-attestation P-to-G causal release
is confirmed.  This single append changes no design, source, implementation,
gate, generated artifact, DAG, proof, Route, manuscript, release, archive,
or Git authority.  The complete post-append path/line/byte/SHA-256 receipt
and the preserved-prefix receipt are issued externally immediately after
this write, because including a digest inside the bytes it digests would
change that digest.

# Fresh v9 design re-review: post-attestation release totality

Status: **REVISE — C0/M1/m1**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v9.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static design audit  
Finding under adjudication: `P15R-REOPEN-M1`  
Implementation, execution, amendment, and source authority: **none**

## I1. Independence, exact prefix, and evidence boundary

I freshly read in full the ARS academic-research-suite root, academic-paper
review workflow, methodology reviewer, domain reviewer, devil's-advocate
reviewer, experiment workflow, integrity-verification agent, integrity review
protocol, both reproducibility protocols, and artifact-reproducibility
pattern.  I applied their independent-oracle, evidence-gap, exact-byte,
causal-counterexample, reproducibility, and no-fabricated-evidence rules.
I did not treat the remediation gate, the amendment's author-side audit, a
source assertion, or another reviewer's conclusion as an oracle.

Immediately before this append, the complete review was independently
re-read and re-hashed as:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=4236
PRESERVED_PREFIX_BYTES=223999
PRESERVED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_NESTED_PREFIX_LINES=3961
PRESERVED_NESTED_PREFIX_BYTES=209656
PRESERVED_NESTED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PREFIX_REWRITE_PERFORMED=false
```

Those 223,999 bytes, including the nested historical PASS and the later
reopen finding, remain the exact prefix of this addendum.  The later review
continues to supersede the historical PASS as the adjudicative result; no
historical text is rewritten or reclassified.

The complete design and governance authority was freshly read and re-hashed
immediately before this append:

| Record | Lines | Bytes | Recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | MATCH |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | MATCH |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` | MATCH |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` | MATCH |
| frozen amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` | MATCH |
| original implementation gate | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` | MATCH |
| implementation remediation gate v1 | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` | MATCH |

The six provisional implementation paths were also completely read and
re-hashed only to verify the quarantine boundary:

| Quarantined path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

Their aggregate remains 7,001 lines and 482,555 bytes.  They are not design
authority, implementation evidence, an acceptance oracle, or a way to
repair an under-specified design.  I did not import, source, compile, parse
as an AST, or execute project code; run a shell syntax check, generator,
verifier, unittest, wrapper, preflight, platform probe, or reproduction; or
create a generated, cache, temporary, result, lock, receipt, or manifest
file.  This addendum is the sole repository write.

## I2. Independently reconstructed v9 release contract

The sole new wire payload is one canonical no-LF/no-NUL ASCII record, on the
existing authenticated framed P--G `SOCK_SEQPACKET` control connection:

```text
PRIVILEGE_DROP_RELEASE session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC attestation_sha256=LOWERHEX64
```

The inherited four-byte unsigned big-endian payload length, 4096-byte
ceiling, exact length, field order, canonical decimal/lowercase-hex grammar,
peer and endpoint identity, complete send/receive, closed-state rules, and
zero ancillary items are explicit.  The direction is P to G.  Its sole
success location is after complete `LAUNCHER_REAPED` and both independent
prerequisite branches, and before any `GUARDIAN_READY` attempt.

The six non-digest fields join the already accepted bootstrap/global session,
G outer PID/inner PID 1/starttime, and retained guardian cgroup device/inode.
The session is not a D-M1 auth-session coordinate.  The G PID/starttime and
cgroup pair are checked against retained identity rather than a pathname,
wall clock, or copied expected token.  V2 did not separately state whether
the `outer_pid` payload in its P--G `LAUNCHER_REAPED` record named reaped L
or surviving G; v9's express G binding is therefore treated here as resolving
that under-defined field, not as an independently counted contradiction.
No quarantined source convention was used to decide that question.

The attestation preimage is domain-separated and independently parseable:

```text
ASCII("P15R-PRIVILEGE-DROP-ATTESTATION-v9") ||
U32BE(7) ||
ITEM(1,binding_ascii) ||
ITEM(2,probe_identity_ascii) ||
ITEM(3,denial_ledger_binary) ||
ITEM(4,probe_reap_ascii) ||
ITEM(5,status_raw) ||
ITEM(6,cgroup_raw) ||
ITEM(7,pass_vector_ascii)

ITEM(tag,value) = U16BE(tag) || U64BE(byte_length(value)) || value
```

Independent boundary attack found no concatenation ambiguity.  Item 1 binds
the ordered release fields; item 2 binds the retained disposable probe PID,
starttime, four uid and gid values, literal empty groups, and five zero
capability sets; item 3 carries a counted fd/root/complete raw-sorted
namespace denial ledger with tagged names, lengths, and exact EPERM/EACCES
numbers; item 4 binds exact pidfd SIGKILL, waitid CLD_KILLED/status, reap, and
process-gone evidence; items 5 and 6 are fresh complete read-to-EOF kernel
bytes with natural final LF and no normalization; and item 7 is the literal
four-predicate pass vector.  P must recompute, canonicalize, and reparse the
complete payload against retained values before its sole send attempt.

G receives one complete record only in `G_LOCAL_DROP_COMPLETE`, validates
every locally knowable frame, field, session, G identity, cgroup, endpoint,
one-use, and local-drop predicate, and then enters
`PRIVILEGE_DROP_RELEASE_VALIDATED`.  The explicit theorem ceiling is a
trusted, non-Byzantine P: G cannot recompute the P-only probe observations,
and the digest is not misrepresented as Byzantine-P resistance.  Within that
ceiling the authenticated release is a genuine causal event, not a copied
flag or G-local substitute.

The successful causal suffix is exact:

```text
P: LAUNCHER_REAPED_SENT
   -> PRIVILEGE_DROP_ATTESTED
   -> PRIVILEGE_DROP_RELEASE_SENT
   -> GUARDIAN_READY_RECEIVED

G: LAUNCHER_REAPED_RECEIVED
   -> G_LOCAL_DROP_COMPLETE
   -> PRIVILEGE_DROP_RELEASE_VALIDATED
   -> GUARDIAN_READY_SENT
```

Before `PRIVILEGE_DROP_RELEASE_VALIDATED`, the fence forbids the lock
candidate and `.owner`, `ACQUIRING`, bind, possession, every generation,
method, subject, package-copy, result, generated, manifest, and staging
object, every subject or worker admission/start, every session/root/spawn/
audit/object/cleanup/exchange operation, and every governed project write.
The cgroup/private-mount setup exception is confined to setup and failure
containment and cannot create a governed artifact.

These features close the original two-world observability gap in the clean
success-versus-failed-P-attestation pair: PASS has the authenticated release;
FAIL has no release, so identical G-local drop facts cannot authorize READY
or a governed mutation.  The review nevertheless cannot PASS because the
same v9 bytes make their broader failure trace algebra contradictory and
their exact retained first-cause label non-deterministic.

## I3. P15R-V9-M1 — failure cardinality contradicts retained failure traces

**Severity: Major.  Confidence: high.**

Section 3.5 says without a phase qualifier that the release "occurs zero
times on every failure path."  The gate repeats that rule in Section 4.5 and
as `AUTHORIZED_FORM_CARDINALITY_FAILURE=ZERO`.  This is stronger than the
coherent Section-3.8 subset rule that a *failed P attestation* emits no
release.

The same amendment separately requires:

1. P enters `PRIVILEGE_DROP_RELEASE_SENT` after a complete framed send;
2. G then completely receives and validates the record;
3. only afterward may G attempt `GUARDIAN_READY`;
4. `P_CRASH`, `G_CRASH`, and `TRANSPORT_ERROR` are release-boundary failure
   causes without a pre-send restriction;
5. `DUPLICATE` and same-bootstrap byte-identical replay are terminal failure
   cases; and
6. a failure tombstone retains every completed predecessor fact, including
   exact release bytes and send result.

The following conforming environmental schedule is therefore a direct
counterexample to failure cardinality zero:

```text
P completes attestation and completely sends the one release
G completely receives and validates it
G crashes before GUARDIAN_READY completes
```

The trace must be `G_CRASH -> PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE ->
BOOTSTRAP_FAILED`, and the tombstone must retain the completed release.  Its
release cardinality is one, not zero.  The same contradiction occurs if the
READY send itself returns a transport error.  It cannot be repaired by
reading "occurs" as "accepted": the same-bootstrap hostile duplicate defined
by v9 necessarily follows a prior current/accepted release, yet the resulting
trace is a failure.  Nor may the tombstone erase the first send; v9 and the
retained v7/v8 rules explicitly preserve completed predecessor history.

This is a design-totality defect, not an implementation preference.  A
future authorized repair must phase-separate at least send attempts,
complete frames emitted/observed, G accepted transitions, successful-
bootstrap cardinality, and failures before versus after an accepted release.
It must permit the actual completed predecessor history while still allowing
at most one successful acceptance and rejecting every additional frame.
Changing prose only in an implementation cannot reconcile the two normative
requirements.

This finding keeps `P15R-REOPEN-M1` open at Major severity.  The new clean
causal edge is present, but the gate requires a zero-finding review of the
complete release/failure contract before closure; that condition is not met.

## I4. P15R-V9-m1 — exact first-cause retention has no tie-break rule

**Severity: Minor.  Confidence: high.**

The set of seventeen names is present exactly:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

All of them lead fail-closed to the same immutable tombstone and inherited
containment, with no retry, reconnect, fallback, correction, record reuse, or
success inferred from EOF/silence.  Safety therefore does not depend on the
label.  Reproducible exact first-cause retention does.

One offending observation can match multiple enum members: a cross-bootstrap
replay normally also has `WRONG_SESSION`; a duplicate after validation is
also `WRONG_STATE`; early READY is expressly called a reordered/wrong-state
failure; malformed digest syntax matches both `MALFORMED` and
`WRONG_ATTESTATION`; and a partial transport operation followed by EOF or
peer death can expose `PARTIAL`, `EOF`, `TRANSPORT_ERROR`, and a crash label
on different owners.  Neither the numbered validation checks nor the failure
rules define precedence, side ownership, a tie break, or a merge rule.  Two
otherwise conforming implementations can therefore retain different "exact
first cause" for the same trace.

A future authorized repair must define a total deterministic classification
function or precedence table keyed by owner, current state, operation result,
observed bytes, peer-liveness evidence, and timeout event.  This is Minor
because every overlapping case already fails before a governed write and the
label is operational/nonserialized, but exact reproducibility remains
under-specified.

## I5. Mandatory hostile-pair and regression audit

| # | Required pair or preservation attack | Independent disposition |
|---:|---|---|
| 1 | exact release versus no release with identical G-local drop | PASS: validation edge exists only in the release world |
| 2 | complete record versus partial send followed by EOF | PASS for safety; partial/EOF cause label precedence remains I4 |
| 3 | exact current record versus byte-identical duplicate | REVISE: fail-closed handling is stated, but failure-zero cardinality contradicts the retained prior record |
| 4 | current record versus replay under another session | PASS for safety; replay/session cause label precedence remains I4 |
| 5 | correct session with wrong G PID/starttime | PASS: exact retained G identity mismatch |
| 6 | correct G identity with wrong guardian device/inode | PASS: exact retained cgroup receipt mismatch |
| 7 | exact bindings with malformed/recomputed-wrong digest | PASS for safety; malformed/attestation label precedence remains I4 |
| 8 | valid record before local drop completion | PASS: wrong state/reorder before validation |
| 9 | valid record after an early READY attempt | PASS: early READY is terminal before any later repair |
| 10 | failed P attestation followed by no failure message | PASS: absence/silence never validates or authorizes a write |

Independent enumeration also confirms that v9 adds exactly one form only to
the inherited global bootstrap P--G enum.  It adds no requester FD-5 form,
D-M1 P--G session form, D-M2 quiescence form, v8 post-finalization form,
ancillary item, descriptor, channel, path, method, detector, result, schema
field, authority binding, generated byte, DAG node, or edge.  The exact
D-M1/D-M1/D-M2 counts remain 12/12/4, and blocked v5 remains no-op
provenance.

The scientific/package vector remains 6 implementation paths, 8 CSVs, 120
body rows, widths `18,19,22,17,16,19,13,10`, 35 negative rows, 35 semantic
mutation classes, 28 package mutation classes, 173 tests, 9 generated paths,
14 authority bindings, 2 fresh generations, 3 byte-identical copies, and an
8-node/12-edge DAG.  Exact-zero tolerance, no network, no manifest self-hash,
no future-result edge, no concurrent proof cycle,
`UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and Route B false remain frozen.
No v1--v8 closure was traded to address the reopened finding.

## I6. Exact count-nine successor authentication

Every historical successor block remains byte-identical in the preserved
prefix.  The following is the sole active count-nine successor.  Its nine
paths were independently read and hashed in printed order.  It authenticates
the exact v9 tuple reviewed here; it does not convert the REVISE verdict into
acceptance or close either finding.

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v8]
count=9
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block contains no blank or commentary line, changes only the effective
amendment count to nine, and adds no manifest key, authority binding,
implementation path, generated member, DAG node, or edge.

## I7. Verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no theorem-owner, evidence-integrity, containment, foreign-deletion, or research-wide collapse |
| Major (`M`) | 1 | `P15R-V9-M1`: failure-zero cardinality contradicts completed release predecessors on enumerated failure traces |
| Minor (`m`) | 1 | `P15R-V9-m1`: overlapping exact first-cause names have no deterministic classification rule |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v9.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_LINES=4236
PRESERVED_PREFIX_BYTES=223999
PRESERVED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_NESTED_PREFIX_LINES=3961
PRESERVED_NESTED_PREFIX_BYTES=209656
PRESERVED_NESTED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

REVIEWED_REMEDIATION_GATE_V9_SHA256=c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90
REVIEWED_AMENDMENT_V9_SHA256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
SOURCE_USED_AS_DESIGN_AUTHORITY=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=1
OVERALL_CLOSURE_VERDICT=REVISE_C0_M1_m1
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN_REQUIRES_SEPARATE_REMEDIATION_AUTHORITY
P15R_V9_m1_STATUS=OPEN_REQUIRES_SEPARATE_REMEDIATION_AUTHORITY

GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT=9
ALL_PRIOR_CLOSURES_REGRESSION=NONE_FOUND

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
NEW_SUCCESSOR_IMPLEMENTATION_GOVERNANCE_GATE_CURRENTLY_AUTHORIZED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact base-plus-v1-through-v9 tuple is
**REVISE — C0/M1/m1**.  The authenticated P-to-G event closes the clean
PASS/failed-attestation observation gap, but the total cardinality and exact
first-cause obligations are not simultaneously reproducible.  Therefore
`P15R-REOPEN-M1` is not closed, neither historical implementation gate is
revived, and no source, implementation, execution, generated artifact,
proof, Route, manuscript, release, archive, or Git action is authorized.
The complete post-append full-path line/byte/SHA-256 receipt and both exact
preserved-prefix receipts are issued externally immediately after this sole
write, because a file cannot contain its own final digest without changing
that digest.

# Fresh v10 design re-review: boundary-seal totality and classifier receipt

Status: **REVISE — C0/M1/m1**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v10.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static design audit  
Findings under adjudication: `P15R-REOPEN-M1`, `P15R-V9-M1`,
`P15R-V9-m1`  
Implementation, execution, amendment, and source authority: **none**

## J1. Independence, complete intake, and exact append boundary

I freshly read in full the ARS academic-research-suite root, academic-paper
review workflow, methodology reviewer, domain reviewer, devil's-advocate
reviewer, experiment workflow, code-runner agent, reproducibility protocol,
integrity-verification agent, integrity review protocol, reproducibility
audit, and artifact-reproducibility pattern. I applied their independent-
oracle, hostile-counterexample, evidence-gap, exact-byte, reproducibility,
and no-fabricated-evidence rules. I did not adopt the v10 gate's requested
shape, the amendment's author-side determination, quarantined source, or any
historical PASS as an adjudicative oracle.

The complete applicable ARS rule set was re-hashed immediately before this
append:

| Complete ARS rule | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| methodology_reviewer_agent.md | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| domain_reviewer_agent.md | 397 | 31829 | `f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052` |
| devils_advocate_reviewer_agent.md | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |
| experiment-agent/WORKFLOW.md | 215 | 11555 | `c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef` |
| code_runner_agent.md | 117 | 4921 | `54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de` |
| reproducibility_protocol.md | 79 | 4150 | `49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |
| reproducibility_audit.md | 54 | 2388 | `a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b` |
| artifact_reproducibility_pattern.md | 173 | 9053 | `661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3` |

The complete current review was re-read and re-hashed immediately before
this append. Its exact current and nested prefixes were:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=4634
PRESERVED_PREFIX_BYTES=245023
PRESERVED_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_NESTED_PREFIX_LINES=4236
PRESERVED_NESTED_PREFIX_BYTES=223999
PRESERVED_NESTED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_OLDER_NESTED_PREFIX_LINES=3961
PRESERVED_OLDER_NESTED_PREFIX_BYTES=209656
PRESERVED_OLDER_NESTED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PREFIX_REWRITE_PERFORMED=false
```

Those 245,023 bytes remain a byte-identical prefix. The nested historical
PASS and the later v9 REVISE remain evidence in their original order; neither
is rewritten or silently reclassified.

The complete design/governance authority was freshly read and re-hashed:

| Record | Lines | Bytes | Recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| remediation gate v10 | 1002 | 45658 | `48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5` | MATCH |
| frozen amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` | MATCH |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` | MATCH |
| frozen amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` | MATCH |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` | MATCH |
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | MATCH |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | MATCH |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | MATCH |
| original implementation gate | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` | MATCH |
| implementation remediation gate v1 | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` | MATCH |

The v10 amendment was a regular mode-0644, nlink-one file at its frozen
receipt. No extra design-amendment successor was present.

The six provisional implementation paths were also completely read and
re-hashed only to verify their quarantine boundary:

| Quarantined path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

The quarantine aggregate is exactly 7,001 lines and 482,555 bytes. Source
was not used as design authority or accepted as implementation evidence. I
did not import, source, compile, AST-parse, syntax-check, or execute project
code; run a generator, verifier, unittest, wrapper, reproduction, preflight,
or platform probe; or create a cache, temporary, generated, result, lock,
receipt, or manifest file. This addendum is the sole repository write.

## J2. Independent reconstruction and attacks that do close

V10 defines the exact binary expected-slot tuple

```text
C=(SA,SC,VA,X,RA,RC,RV)
```

where the first three coordinates count only the sole authorized release
attempt, exact complete send, and exact validated acceptance; the final three
count only the sole authorized READY attempt, exact complete send, and exact
validated receive; and X is set only by an actually observed out-of-slot
boundary frame. Receive attempts, silence, timeout, EOF, crash, errno, poll
readiness, and inferred or merely queued packets do not set X. The first
actual out-of-slot frame sets X once and terminalizes; it is not a second
expected-slot acceptance and cannot erase a predecessor.

Independent enumeration gives exactly these fourteen algebraic vectors:

| # | Release | X | READY | Outcome |
|---:|---|---:|---|---|
| 1 | 000 | 0 | 000 | PRE_SEND_FAILURE |
| 2 | 000 | 1 | 000 | PRE_SEND_FAILURE |
| 3 | 100 | 0 | 000 | PARTIAL_SEND_FAILURE |
| 4 | 100 | 1 | 000 | PARTIAL_SEND_FAILURE |
| 5 | 110 | 0 | 000 | POST_SEND_PRE_VALIDATE_FAILURE |
| 6 | 110 | 1 | 000 | POST_SEND_PRE_VALIDATE_FAILURE |
| 7 | 111 | 0 | 000 | POST_VALIDATE_PRE_READY_FAILURE |
| 8 | 111 | 1 | 000 | POST_VALIDATE_PRE_READY_FAILURE |
| 9 | 111 | 0 | 100 | READY_PARTIAL_SEND_FAILURE |
| 10 | 111 | 1 | 100 | READY_PARTIAL_SEND_FAILURE |
| 11 | 111 | 0 | 110 | READY_POST_SEND_PRE_VALIDATE_FAILURE |
| 12 | 111 | 1 | 110 | READY_POST_SEND_PRE_VALIDATE_FAILURE |
| 13 | 111 | 1 | 111 | POST_READY_BOUNDARY_EXTRA_FAILURE |
| 14 | 111 | 0 | 111 | BOOTSTRAP_BOUNDARY_SUCCESS |

The prefix inequalities exclude every other binary tuple. Rows 1--12 are
mutually exclusive and operationally feasible under their stated retained
receipts. Their X=1 variants require actual hostile frame evidence; X is not
deduced from the six expected-slot bits. Complete release validation followed
by G crash retains `(1,1,1,0,0,0,0)`; partial READY retains
`(1,1,1,0,1,0,0)`; complete READY followed by receive-side failure retains
`(1,1,1,0,1,1,0)`; and a later duplicate changes only X while preserving the
valid predecessor. This repairs v9's history-erasing failure-zero sentence
for those schedules.

V10 also gives the six fixed earliest-first causal phases
`PRE_SEND`, `RELEASE_SEND`, `POST_SEND_PRE_VALIDATE`,
`POST_VALIDATE_PRE_READY`, `READY_SEND`, and `POST_READY_BOUNDARY`. Phase
selection is based on retained send/receive, validation, state-predecessor,
pidfd/reap, deadline, and receipt joins, not wall time, scheduler order,
poll-list order, filesystem time, enumeration order, or cleanup order.
Causally incomparable P/G failure facts in the same phase are unioned, and
the primary-owner tie is P before G for an otherwise identical same-label
tie.

The primary-label order is exact and complete:

```text
PARTIAL > DUPLICATE > REPLAY > WRONG_DIRECTION > REORDERED > WRONG_STATE
> MALFORMED > WRONG_SESSION > WRONG_G_IDENTITY > WRONG_CGROUP
> WRONG_ATTESTATION > TRANSPORT_ERROR > EOF > P_CRASH > G_CRASH
> TIMEOUT > MISSING
```

That order deterministically selects the primary label for the printed
partial/EOF/error/crash, duplicate/wrong-state, replay/wrong-session,
reordered/wrong-state, wrong-direction/reordered, grammar/attestation,
transport/EOF, P-crash/G-crash, and timeout/missing overlaps. Unknown complete
bytes, no-byte transport errors, clean EOF, proved process death, deadline
expiry, and remaining deterministic absence cover the terminal residual
classes. The primary selection itself therefore repairs v9's missing
precedence. The separately required bitmap receipt still has the defect in
J4 below.

The L/G binder is unambiguous. `LAUNCHER_REAPED.outer_pid` equals separately
retained `launcher_outer_pid` for reaped L. `PID1_READY.outer_pid`,
`GUARDIAN_READY.outer_pid`, and `PRIVILEGE_DROP_RELEASE.g_outer_pid` equal
`g_outer_pid` for surviving inner-PID-1 G, and the two outer PIDs must differ.
L remains excluded from `binding_ascii` and the exact seven-item v9 preimage;
its exact pidfd-bound reap receipt is retained separately. No eighth item,
alternate digest, alias, or source-derived identity is introduced.

The sole v9 release payload, framing, direction, seven-item preimage,
trusted-non-Byzantine-P ceiling, fail-before-write fence, and no retry,
fallback, reconnect, correction, or reuse rules remain unchanged. V10 adds
zero forms; v9 remains the sole scoped global-bootstrap plus-one. The exact
12 FD-5 D-M1, 12 P--G session D-M1, and 4 D-M2 forms are unchanged.

## J3. P15R-V10-M1 — no deterministic positive close for the global X window

**Severity: Major. Confidence: high.**

Rows 13 and 14 are declared distinct at the same six completed expected-slot
coordinates. Their only difference is whether an actual out-of-slot frame is
retained before the success receipt is sealed. V10 says the success receipt
is sealed after P fully receives, parses, validates, and G-identity-joins the
READY and the "still-open boundary close" has no retained actual extra. It
does not define an operation, retained receipt, causal join, or positive
closing transition that ends that still-open window.

This omission has a direct two-conforming-implementation counterexample:

```text
common retained predecessor:
  P completely sends the sole valid release
  G completely receives and validates it
  G completely sends the first exact READY
  P completely receives, parses, validates, and G-identity-joins that READY

hostile continuation already available on the same authenticated endpoint:
  a second byte-identical READY is delivered as the next SOCK_SEQPACKET frame

implementation A:
  atomically seals X=0 success when the first READY handler sets RV=1
  only afterward performs another receive and treats the second frame as later

implementation B:
  leaves POST_READY_BOUNDARY open after RV=1
  performs the next receive, retains the actual second frame, sets X=1,
  and seals vector 13 failure
```

Both implementations honor the rule that a queued or inferred frame does not
set X: A has not actually observed the second frame when it seals, while B
has. Both also honor the stated necessary prerequisites for sealing. Nothing
in v10 says whether another receive must occur, how many actual receives form
the close, or which existing positive receipt closes it. A nonblocking empty
queue, poll result, silence, timeout, EOF, or errno cannot supply the missing
causal join: those facts either are expressly excluded from X and passing
fixed observations or leave an arrival race immediately after the check.

The same gap appears cross-owner. G can retain an actual out-of-slot release
observation in `POST_READY_BOUNDARY` while P has received only the first exact
READY. P has no existing success-seal acknowledgment or other G-to-P receipt
that joins G's X fact before it locally admits X=0 success. The Section-5.1
failure-union rule tells a later audit how to order incomparable failure facts;
it does not provide a positive runtime join by which P can know that the
global X window is closed.

Consequently vector 13 is either unreachable under an immediate READY seal,
or the duration and contents of the open window are implementation/scheduler
choices. The same authenticated frame history can be admitted as vector 13
failure or vector 14 success. Once A seals success, v10's no-backflow rule
forbids the later actual extra from correcting C, so that rule does not repair
the ambiguity. Conversely, keeping the boundary open indefinitely cannot
produce positive success without using a forbidden absence/time inference.

This is Major because the unique bootstrap-success boundary, the feasibility
and exclusivity of the thirteenth failure vector and fourteenth success
vector, and the fail-before-write admission decision are not reproducible.
The gate itself says that if the repair needs another form or retained join
outside the frozen v9 envelope, authoring must stop as BLOCKED; v10 may not
silently invent an acknowledgment. A future authorized design must define an
existing-fact positive close that every implementation uses and prove how
both owners' pre-close X evidence is joined, or obtain broader governance for
a new close/acknowledgment mechanism.

## J4. P15R-V10-m1 — immutable candidate-bitmap membership is not total

**Severity: Minor. Confidence: high.**

The linear order in J2 makes the primary label deterministic, and every
overlap still fails closed. The new immutable seventeen-bit candidate bitmap,
however, lacks a deterministic raw-membership function.

Section 5.2 says to evaluate predicates in precedence order and choose the
first true label. Several lower predicates incorporate the precedence into
their own truth conditions: `WRONG_DIRECTION` applies after duplicate/replay
are excluded; `REORDERED` applies after all prior cases are excluded; and the
transport, EOF, crash, timeout, and missing predicates require no higher
evidence. Section 5.3 simultaneously requires lower losing candidates such
as `WRONG_STATE` with `DUPLICATE`, `WRONG_SESSION` with `REPLAY`,
`WRONG_STATE` with `REORDERED`, and `REORDERED` with `WRONG_DIRECTION` to be
retained. It finally permits losing candidate facts to remain in the bitmap
**or** the secondary-fact ledger.

For one canonical READY frame observed from the wrong owner before release
validation, the mandated winner is `WRONG_DIRECTION` and the evidence also
satisfies the printed early-order fact. One conforming implementation can set
both `WRONG_DIRECTION` and `REORDERED` bits before applying precedence.
Another can apply the literal "after prior cases are excluded" predicate,
set only `WRONG_DIRECTION`, and retain early-order evidence in the permitted
secondary ledger. Both select the same required primary and fail closed, but
their supposedly immutable classification receipts have different bitmaps.

The enum declaration order specifies bit positions, not bit membership. The
overlap examples do not define all raw predicate intersections, and the
bitmap-or-secondary alternative prevents them from serving as a total rule.
A reproducible repair must first define each grammar-gated, side-effect-free
raw predicate independently of priority, freeze every true bit into the
bitmap, and only then choose the first set bit under the separate precedence
permutation. This is Minor because primary cause and safety are already
deterministic; exact receipt reproducibility is not.

## J5. Mandatory regression and closure audit

| Required attack | Independent disposition |
|---|---|
| 13 failure plus 1 success vectors; all other tuples excluded | REVISE: algebraic enumeration is exact, but vector-13/vector-14 operational separation fails J3 |
| expected-slot binary semantics and retained predecessor history | PASS for rows 1--12: no counter reaches two and no valid predecessor is erased |
| X actual-frame-only, duplicate, and replay evidence | PASS: no silence/EOF/crash/errno/poll/inferred-queue substitution; success-window closure remains J3 |
| unique success and no downstream backflow | REVISE: post-seal no-backflow is explicit, but the seal's global positive close is absent in J3 |
| six causal phases from retained receipts | PASS for failure phase selection; the positive close is not one of those receipts |
| seventeen primary labels, overlaps, races, and owner tie | PASS for primary selection; immutable losing-candidate bitmap remains J4 |
| immutable tombstone receipt | PASS for fields and post-seal immutability; exact bitmap value remains J4 |
| L/G owner binder and preimage exclusion | PASS: L and G are distinct, exact joins are stated, and L stays outside the seven-item preimage |
| sole global plus-one and closed enums | PASS: v10 adds zero forms and the inherited counts remain 12/12/4 |
| base plus v1--v9, including v5 no-op | PASS: no independent regression found outside the two new findings |
| frozen scientific/package vector | PASS: 6 paths, 8 CSVs, 120 rows, widths 18/19/22/17/16/19/13/10, 35/35/28 classes, 173 methods, 9 generated paths, 14 bindings, 2 generations, and 3 copies remain exact |
| frozen DAG | PASS: nodes A/D/R/G/I/C/M/V and the 7 chain plus 5 additional edges remain exactly 8/12 |

No new record, field, descriptor, ancillary item, socket, channel, preimage
item, digest domain, implementation path, generated artifact, authority
binding, or DAG coordinate was found in the amendment bytes. Exact-zero
tolerance, no network, no manifest self-hash, no future-result edge, no
concurrent proof hash cycle, `UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and
Route B false remain frozen.

The v9 counter algebra and primary-label precedence are materially improved,
but the gate permits closure only on a complete zero-finding review. J3 and
J4 therefore leave `P15R-V9-M1`, `P15R-V9-m1`, and consequently
`P15R-REOPEN-M1` open. Neither historical implementation gate is revived.

## J6. Exact count-ten successor authentication

Every historical successor block remains byte-identical in the preserved
prefix. The following is the sole active count-ten successor. All ten files
were independently read and hashed in printed order. This block authenticates
the exact base-plus-v1-through-v10 tuple reviewed here; it does not convert
the REVISE verdict into acceptance.

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v9]
count=10
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
10.path=notes/phase2_control_design_amendment_v10.md
10.sha256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block has no blank or commentary line inside. It changes only the
governance successor count to ten and adds no manifest key, authority binding,
implementation path, generated member, DAG node, or edge.

## J7. Verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no research-wide theorem/evidence collapse independently found |
| Major (`M`) | 1 | `P15R-V10-M1`: vector-13/vector-14 success-seal cut lacks a deterministic positive close and cross-owner X join |
| Minor (`m`) | 1 | `P15R-V10-m1`: raw membership of the immutable candidate-label bitmap is under-specified |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v10.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_LINES=4634
PRESERVED_PREFIX_BYTES=245023
PRESERVED_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_NESTED_PREFIX_LINES=4236
PRESERVED_NESTED_PREFIX_BYTES=223999
PRESERVED_NESTED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_OLDER_NESTED_PREFIX_LINES=3961
PRESERVED_OLDER_NESTED_PREFIX_BYTES=209656
PRESERVED_OLDER_NESTED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

REVIEWED_REMEDIATION_GATE_V10_SHA256=48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5
REVIEWED_AMENDMENT_V10_SHA256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
SOURCE_USED_AS_DESIGN_AUTHORITY=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=1
OVERALL_CLOSURE_VERDICT=REVISE_C0_M1_m1
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V9_m1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V10_M1_STATUS=OPEN_REQUIRES_SEPARATE_REMEDIATION_AUTHORITY
P15R_V10_m1_STATUS=OPEN_REQUIRES_SEPARATE_REMEDIATION_AUTHORITY

GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
V10_NEW_WIRE_FORM_COUNT=0
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT=10
ALL_PRIOR_CLOSURES_REGRESSION=NONE_FOUND_OUTSIDE_REVIEW_FINDINGS

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
NEW_SUCCESSOR_IMPLEMENTATION_GOVERNANCE_GATE_CURRENTLY_AUTHORIZED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
PLATFORM_PRECHECK_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact base-plus-v1-through-v10 tuple is
**REVISE — C0/M1/m1**. V10 supplies a coherent binary prefix algebra,
retained-predecessor repair, primary-label precedence, and exact L/G binder,
but it does not define a reproducible positive close for the global X window
or a total raw-membership rule for the immutable candidate bitmap. Therefore
none of the three inherited findings closes, no implementation governance is
current, and no source, implementation, run, precheck, generated artifact,
proof, Route, manuscript, release, archive, or Git action is authorized. The
complete post-append path/line/byte/SHA-256 receipt and all three exact prefix
receipts are issued externally immediately after this sole write because a
file cannot contain its own final digest without changing that digest.

# Fresh v11 design re-review after exact path recovery: ACK/seal commit totality

Status: **REVISE — C0/M1/m0**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v11.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static design audit after committed
path recovery  
Findings under adjudication: `P15R-REOPEN-M1`, `P15R-V9-M1`,
`P15R-V9-m1`, `P15R-V10-M1`, and `P15R-V10-m1`  
Implementation, execution, amendment, source, and Git authority: **none**

## K1. Independence, recovery provenance, and exact intake

I freshly read in full the ARS academic-research-suite root, academic-paper
review workflow, methodology reviewer, domain reviewer, devil's-advocate
reviewer, experiment workflow, code-runner agent, reproducibility protocol,
integrity-verification agent, integrity review protocol, reproducibility
audit, and artifact-reproducibility pattern. I applied their independent-
oracle, hostile-counterexample, exact-evidence, experiment-integrity,
reproducibility, and no-fabricated-evidence rules. Neither the v11 gate's
requested result nor the amendment's author-side determination was used as
an adjudicative oracle.

The complete applicable ARS rule set was re-hashed immediately before this
append:

| Complete ARS rule | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| methodology_reviewer_agent.md | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| domain_reviewer_agent.md | 397 | 31829 | `f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052` |
| devils_advocate_reviewer_agent.md | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |
| experiment-agent/WORKFLOW.md | 215 | 11555 | `c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef` |
| code_runner_agent.md | 117 | 4921 | `54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de` |
| reproducibility_protocol.md | 79 | 4150 | `49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |
| reproducibility_audit.md | 54 | 2388 | `a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b` |
| artifact_reproducibility_pattern.md | 173 | 9053 | `661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3` |

The complete current review was re-read and re-hashed immediately before
this append. Its exact append boundary and nested historical boundaries were:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=5080
PRESERVED_PREFIX_BYTES=270649
PRESERVED_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_NESTED_PREFIX_LINES=4634
PRESERVED_NESTED_PREFIX_BYTES=245023
PRESERVED_NESTED_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_OLDER_NESTED_PREFIX_LINES=4236
PRESERVED_OLDER_NESTED_PREFIX_BYTES=223999
PRESERVED_OLDER_NESTED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PREFIX_REWRITE_PERFORMED=false
```

All 270,649 input bytes remain a byte-identical prefix. The historical PASS,
later v9 REVISE, and v10 REVISE remain evidence in their original order;
none is rewritten or silently reclassified.

The path-recovery transaction had committed before review intake. The
correct paper-package target was a regular mode-0644, nlink-one file with
1,072 lines, 49,086 bytes, and SHA-256
`7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269`.
The workspace-root stray `notes/phase2_control_design_amendment_v11.md` was
absent under both ordinary-existence and lstat-path reasoning, and the
correct target was the sole named v11 amendment in the workspace. Recovery
changed path provenance only; it supplied no design claim or review result.

The complete design/governance authority was freshly read and re-hashed:

| Record | Lines | Bytes | Recomputed SHA-256 | Result |
|---|---:|---:|---|---|
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | MATCH |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | MATCH |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | MATCH |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | MATCH |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | MATCH |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | MATCH |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | MATCH |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | MATCH |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | MATCH |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | MATCH |
| amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` | MATCH |
| amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` | MATCH |
| amendment v11, recovered target | 1072 | 49086 | `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269` | MATCH |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` | MATCH |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` | MATCH |
| remediation gate v10 | 1002 | 45658 | `48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5` | MATCH |
| remediation gate v11 | 1221 | 54839 | `d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e` | MATCH |
| amendment-v11 path-recovery gate | 528 | 21386 | `41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888` | MATCH |
| original implementation gate | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` | MATCH |
| implementation remediation gate v1 | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` | MATCH |

The six provisional implementation paths were completely byte-read and
re-hashed only to freeze their quarantine boundary:

| Quarantined path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

The quarantine aggregate remains exactly 7,001 lines and 482,555 bytes.
Source was not used as design authority or accepted as implementation
evidence. I did not import, source, compile, AST-parse, shell-syntax-check,
or execute project code; run a generator, verifier, unittest, wrapper,
reproduction, preflight, or platform probe; or create a cache, temporary,
generated, result, lock, receipt, or manifest path. This append is the sole
repository write.

## K2. Independent reconstruction and hostile attacks that do close

The sole new record has the exact canonical P-to-G form
`GUARDIAN_READY_ACK`, the inherited four-byte U32BE framed-length prefix,
4096-byte ceiling, canonical ASCII grammar, zero ancillary items, one P send
attempt, and one G receive/validation slot. Every printed session, G PID,
starttime, guardian device/inode, release-frame digest, release-attestation
digest, READY-frame digest, four P count fields, `x_p=0`, and P-seal field is
necessary. Wrong-first, partial, malformed, duplicate, replay, wrong-state,
wrong-direction, or wrong binding consumes the sole slot and terminalizes;
there is no correction, retry, reconnect, or fallback.

The nine-item `P15R-GUARDIAN-READY-ACK-SEAL-v11` preimage is reconstructible
at G without trusting normalized fields. Its raw release and READY frames,
separate release-attestation value, P count string, exact two-entry P emit
ledger, exact one-entry P observation ledger, P freeze string, and owner/
one-use/no-entropy string bind every success-shaped P fact. The launcher is
joined through the exact P emit ledger; release and READY are joined through
their raw framed bytes. The digest is correctly limited to a receipt rather
than a secret or capability. `ACK_UNSEEN -> ACK_CONSUMED` on the first
complete slot observation, authenticated endpoint identity, current session
and G/cgroup/frame joins, and no reuse make same-session duplicate and prior-
session replay distinct terminal failures. No independent field, seal-item,
channel, or cardinality counterexample was found.

The old-form set remains exactly `LAUNCHER_REAPED`,
`PRIVILEGE_DROP_RELEASE`, and `GUARDIAN_READY`. P freezes its exact two-emission/
one-observation ledgers only after complete READY validation and before its
sole ACK attempt. G freezes its READY emission ledger after the sole complete
READY send and before ACK receipt, while its observation side remains open
for that expected slot. FIFO on the same authenticated `SOCK_SEQPACKET`
endpoint therefore places every earlier P old-form emission before P's ACK
at G. G knows its own emission history; the ACK binds P's history. P remains
`GUARDIAN_READY_ACK_SENT_PENDING_G_SEAL` and owns neither positive success
nor the first governed write. Within the explicit trusted, authenticated,
non-Byzantine-owner ceiling, no ACK-of-ACK adds a prerequisite at G and an
infinite positive handshake is unnecessary.

The ceiling is material. A trusted conforming owner performs no post-freeze
old-form emission. An actual pre-freeze or pre-seal old-form event sets the
applicable owner-local bit; silence, timeout, EOF, errno, poll readiness,
expected behavior, or inferred queue contents do not. An actual frame after
a sealed success is a downstream violation and cannot flow backward. No
Byzantine-owner detection claim was silently inferred from the P seal or
frozen ledgers.

Independent algebraic enumeration of

```text
C11=(SA,SC,VA,X_P,X_G,RA,RC,RV,AA,AC,AV)
```

does produce the printed 33 coordinate patterns before considering the
separate success-seal state. There are seven release/READY prefix positions
through `RV=1,AA=0`, each with four local-X combinations, then two
`AA=1,AC=0` rows with `X_P=0`, two `AC=1,AV=0` rows with `X_P=0`, and one
`AV=1` coordinate with both X bits zero: `28+2+2+1=33`. The prefix
inequalities exclude all other binary coordinate patterns, ACK-stage
`X_P=1` is forbidden by P's freeze, and AV admits no nonzero X bit. Every
completed predecessor is retained and the v10 projection is exactly
`X=X_P|X_G`. The coordinate arithmetic is correct; the extra success-seal
condition creates the counterexample in K3.

V11 repairs the v10 bitmap-membership defect at the design-clause level.
All seventeen raw predicates are defined from the frozen causal evidence
without mentioning priority or another label. Every true bit is first
retained in the immutable existing-enum-order bitmap. Only afterward is the
winner selected under the separate exact permutation

```text
PARTIAL > DUPLICATE > REPLAY > WRONG_DIRECTION > REORDERED > WRONG_STATE
> MALFORMED > WRONG_SESSION > WRONG_G_IDENTITY > WRONG_CGROUP
> WRONG_ATTESTATION > TRANSPORT_ERROR > EOF > P_CRASH > G_CRASH
> TIMEOUT > MISSING
```

and all losing true bits remain set. Field-parseability is evidence-domain
gating, not hidden precedence, and P-before-G affects only an otherwise
identical same-label owner tie. No residual two-bitmap counterexample was
found.

The v10 nonzero failure cardinalities, monotone predecessor history, L/G PID
binder and launcher exclusion from the v9 preimage remain exact. The v9
release payload, seven-item preimage, raw-byte boundary, one-use/no-retry
rules, and strict pre-write intent remain unchanged. Base plus v1--v8,
including v5's blocked/no-op provenance, retain their effective clauses.
The ACK is the sole v11 new form and the global v2-derived delta is exactly
plus two; it is not a D-M1, D-M2, or requester form, so the exact 12/12/4
closed enums do not change.

## K3. P15R-V11-M1 — ACK validation and the success seal are not one total commit

**Severity: Major. Confidence: high.**

V11 defines three successive G suffix states, including the distinct states
`GUARDIAN_READY_ACK_VALIDATED` and
`BOOTSTRAP_BOUNDARY_SUCCESS_SEALED`. Section 3.5 says complete validation
enters the former **and then** the immutable seal receipt. `AV` is separately
defined only as the ACK validated-accept count at G. No invariant says
`AV==1` iff the success seal is already retained, and no clause makes the AV
increment and seal creation one indivisible, crash-atomic logical commit.

That leaves this exact model-admitted execution:

```text
common retained predecessor:
  release and READY complete and validate
  P freezes both old-form ledgers with X_P=0
  P attempts and completely sends its sole exact ACK
  G receives the ACK, freezes its observation ledger, obtains X_G=0,
    recomputes and validates every ACK/seal binding
  C11=(1,1,1,0,0,1,1,1,1,1,0)

G validation transition:
  AV changes 0 -> 1
  G enters GUARDIAN_READY_ACK_VALIDATED
  C11=(1,1,1,0,0,1,1,1,1,1,1)

continuation A:
  G creates BOOTSTRAP_BOUNDARY_SUCCESS_SEALED
  row 33 is SUCCESS and may cross the fence

continuation B:
  G crashes after AV=1 but before creating the success seal
  or remains in the distinct validated-only state until terminal failure
  P remains pending; no governed write occurs; G_CRASH or TIMEOUT is true
```

Continuation B is inside the declared evidence model. Trusted and
non-Byzantine does not mean crash-free or permanently scheduled; `G_CRASH`
and `TIMEOUT` are two of v11's exact raw failure predicates. The pre-write
fence keeps B safe, but safety is not the disputed coordinate claim.

V11's own success biconditional correctly requires both exact freeze
receipts **and** G ownership of `BOOTSTRAP_BOUNDARY_SUCCESS_SEALED`, so B is
not success. Monotone tombstone history forbids resetting its already
completed AV coordinate from one to zero. B therefore has the exact same
eleven coordinates as row 33, while the supposedly complete and mutually
exclusive table labels that coordinate only `BOOTSTRAP_BOUNDARY_SUCCESS`.
It is an unlisted failure at the claimed sole-success coordinate, not one of
the 32 printed failure vectors.

The classifier phase extension ends at
`POST_ACK_SEND_PRE_VALIDATE`; it has no post-validation/pre-seal phase for B.
The no-backflow sentence for a later crash applies after an immutable success
seal exists and cannot classify this earlier crash. The assertion that a
conforming implementation cannot leave success open indefinitely is a
desired result, not an operational commit rule that makes the two named
states indivisible.

Thus the printed `32 FAILURE + 1 SUCCESS` outcome totality, classification by
exact eleven-coordinate mutual exclusion, and retained-history claim are
false. The new ACK supplies the missing cross-owner evidence, and G's sole
seal still protects the write fence, but the validation-to-seal cut itself
is not modeled totally. This is Major because the exact terminal algebra and
the reproducible positive boundary are mandatory closure conditions for
`P15R-V10-M1`, not optional receipt decoration.

A bounded repair need not add a second wire form. To retain 33 rows, the
design can define one indivisible logical commit in which `AV:0->1` occurs
iff the immutable G success seal is simultaneously retained, make the
validated-only state unobservable/nonterminal, and require every precommit
crash to retain `AV=0` in row 31 or 32. Alternatively, it can add an explicit
seal coordinate/phase and a distinct `AV=1,seal=0` failure row, updating the
vector count. This review grants authority for neither repair.

## K4. Mandatory attack and regression matrix

| Required hostile audit | Independent disposition |
|---|---|
| sole ACK exact fields, framing, direction, channel, and one-attempt/one-slot cardinality | PASS: no independent ambiguity or extra form found |
| exact P seal preimage, ledger bytes, raw-frame joins, owner/use/no-entropy, recomputation, and replay | PASS within the explicit authenticated non-Byzantine ceiling |
| G and P old-form freezes, P-to-G FIFO, owner-local evidence, and `X=X_P|X_G` | PASS for the stated pre-freeze/pre-seal scope; no Byzantine claim inferred |
| one ACK, P pending, G-only authorization, and no ACK-of-ACK | PASS for cross-owner evidence sufficiency; REVISE for the local AV-to-seal commit in K3 |
| 33 coordinate patterns, exact 32 failure plus 1 success, mutual exclusion, feasibility, and tombstones | REVISE: K3 produces row-33 coordinates without the separately required seal |
| actual-evidence X bits, later violation, and no downstream backflow | PASS under the stated ceiling; post-seal facts remain downstream |
| seventeen raw predicates before separate priority, all loser bits retained | PASS at the design-clause level; no v10 two-bitmap counterexample remains |
| v10 cardinality, PID binder, v9 release/preimage/fence, and base/v1--v8 including v5 no-op | PASS: no independent regression found outside K3 |
| strict no-lock/no-object/no-generation/no-write fence through G's success seal | PASS: the K3 failure is safe precisely because the seal is absent |
| global plus two and exact 12/12/4 scoped enums | PASS |
| frozen schemas, 6/8/120/widths/35/35/28/173/9/14/2/3 counts | PASS |
| nodes A/D/R/G/I/C/M/V and 7 chain plus 5 additional edges | PASS: exactly 8 nodes and 12 distinct edges |
| path recovery, sole correct v11 target, and workspace-root stray absence | PASS as provenance only; recovery supplies no merits presumption |

The frozen scientific/package vector remains 6 implementation paths, 8 CSV
artifacts, 120 body rows, widths 18/19/22/17/16/19/13/10, 35 explicit
negative rows, 35 semantic and 28 package mutation classes, 173 unittest
methods, 9 generated artifacts including the manifest, 14 authority
bindings, 2 fresh generations, and 3 byte-identical copies. Exact-zero
tolerance, no network, no manifest self-hash, no future-result edge, no
concurrent proof hash cycle, `UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED`, and
Route B false remain frozen.

V11 materially repairs the v10 cross-owner join and raw predicate definitions,
but the gate permits finding closure only after a complete zero-finding
review. K3 therefore leaves all five named findings open. Neither historical
implementation gate is revived, and the path-recovery gate is spent path
provenance rather than downstream authority.

## K5. Exact count-eleven successor authentication

Every historical successor block remains byte-identical in the preserved
prefix. The following is the sole active count-eleven successor. All eleven
files were independently read and hashed in printed order. This block
authenticates the exact base-plus-v1-through-v11 tuple reviewed here; it does
not convert the REVISE verdict into acceptance.

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v10]
count=11
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
10.path=notes/phase2_control_design_amendment_v10.md
10.sha256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
11.path=notes/phase2_control_design_amendment_v11.md
11.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block contains no blank or commentary line. It changes only the active
governance successor count to eleven and adds no schema field, authority
binding, implementation path, generated member, DAG node, or edge.

## K6. Verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no research-wide theorem/evidence collapse independently found |
| Major (`M`) | 1 | `P15R-V11-M1`: AV=1 can precede the separately required G success seal, leaving an unlisted row-33 failure |
| Minor (`m`) | 0 | no additional bounded defect independently found |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v11.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_LINES=5080
PRESERVED_PREFIX_BYTES=270649
PRESERVED_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_NESTED_PREFIX_LINES=4634
PRESERVED_NESTED_PREFIX_BYTES=245023
PRESERVED_NESTED_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_OLDER_NESTED_PREFIX_LINES=4236
PRESERVED_OLDER_NESTED_PREFIX_BYTES=223999
PRESERVED_OLDER_NESTED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

REVIEWED_REMEDIATION_GATE_V11_SHA256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
REVIEWED_PATH_RECOVERY_GATE_SHA256=41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888
REVIEWED_AMENDMENT_V11_SHA256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
V11_PATH_RECOVERY_COMMITTED=true
WORKSPACE_ROOT_STRAY_V11_PATH_ABSENT=true
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
SOURCE_USED_AS_DESIGN_AUTHORITY=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M1_m0
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V9_m1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V10_M1_STATUS=OPEN_REMEDIATION_INCOMPLETE_BY_P15R_V11_M1
P15R_V10_m1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V11_M1_STATUS=OPEN_REQUIRES_SEPARATE_REMEDIATION_AUTHORITY

GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_TWO
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=2
V11_NEW_WIRE_FORM_COUNT=1
THIRD_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT=11
ALL_PRIOR_CLOSURES_REGRESSION=NONE_FOUND_OUTSIDE_REVIEW_FINDING

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
NEW_SUCCESSOR_IMPLEMENTATION_GOVERNANCE_GATE_CURRENTLY_AUTHORIZED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
PLATFORM_PRECHECK_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact recovered base-plus-v1-through-v11 tuple is
**REVISE — C0/M1/m0**. The one ACK, exact cross-owner frame/ledger joins,
owner freezes, G-only write fence, and independent raw bitmap materially
repair v10, but `AV=1` and the separately required immutable success seal
are not defined as one indivisible commit. A trusted G crash in that gap has
row-33 coordinates without success, contradicting the claimed exact
32-failure/one-success totality. Therefore none of the five inherited
findings closes, `P15R-V11-M1` is open, no implementation governance is
current, and no source, implementation, run, precheck, generated artifact,
proof, Route, manuscript, release, archive, or Git action is authorized. The
complete post-append path/line/byte/SHA-256 receipt and all exact prefix
receipts are issued externally immediately after this sole write because a
file cannot contain its own final digest without changing that digest.

# Fresh v13 independent hostile design re-review: survivor audit and actual-endpoint enqueue

Status: **REVISE — C0/M2/m0**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v13.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static hostile design audit  
Finding posture: no prior verdict, gate conclusion, amendment conclusion, or
source convention was used as an adjudicative oracle  
Implementation, execution, source-edit, artifact, and Git authority: **none**

## L1. Independent intake, method, and append boundary

I freshly read in full the complete applicable ARS-Codex 0.1.25 academic-
research-suite rule set, including the academic-paper-review workflow,
methodology reviewer, domain reviewer, devil's-advocate reviewer, experiment
workflow, code-runner agent, reproducibility protocol, integrity-verification
agent, integrity-review protocol, reproducibility audit, and artifact-
reproducibility pattern. I applied their independent-oracle, hostile fixed-
observation, exact-evidence, no-fabrication, read-only-review, integrity, and
reproducibility rules. The v13 gate and amendment were treated as claims to
attack, not as verdict authority.

The complete ARS rules were re-hashed immediately before this append:

| Complete ARS rule | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| methodology_reviewer_agent.md | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| domain_reviewer_agent.md | 397 | 31829 | `f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052` |
| devils_advocate_reviewer_agent.md | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |
| experiment-agent/WORKFLOW.md | 215 | 11555 | `c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef` |
| code_runner_agent.md | 117 | 4921 | `54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de` |
| reproducibility_protocol.md | 79 | 4150 | `49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |
| reproducibility_audit.md | 54 | 2388 | `a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b` |
| artifact_reproducibility_pattern.md | 173 | 9053 | `661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3` |

The then-current review was completely re-read and authenticated at the sole
append boundary. Every historical PASS/REVISE block remains byte-identical
evidence in its original order:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=5527
PRESERVED_PREFIX_BYTES=296651
PRESERVED_PREFIX_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c
PRESERVED_V11_INPUT_PREFIX_LINES=5080
PRESERVED_V11_INPUT_PREFIX_BYTES=270649
PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_V10_INPUT_PREFIX_LINES=4634
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PREFIX_REWRITE_PERFORMED=false
```

The frozen v13 inputs remained regular mode-0644, nlink-1 files and matched
the external freeze exactly:

| Frozen v13 input | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_design_remediation_gate_v13.md` | 1324 | 61873 | `5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca` |
| `notes/phase2_control_design_amendment_v13.md` | 1057 | 48820 | `4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27` |

`notes/phase2_control_design_amendment_v12.md` was absent under ordinary
existence and path-list checks. Only amendment v13 occupied the v12/v13
successor-name slice.

## L2. Complete design, governance, implementation-gate, and quarantine tuple

Every applicable design/governance record was freshly read in full and
re-hashed. V5 remains blocked/no-op provenance; v12 remains a BLOCKED gate
with no amendment; the two historical implementation gates remain consumed,
nonauthorizing provenance.

| Record | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` |
| amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` |
| amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` |
| amendment v11 | 1072 | 49086 | `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269` |
| amendment v13 | 1057 | 48820 | `4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27` |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` |
| remediation gate v10 | 1002 | 45658 | `48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5` |
| remediation gate v11 | 1221 | 54839 | `d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e` |
| amendment-v11 path-recovery gate | 528 | 21386 | `41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888` |
| remediation gate v12, BLOCKED | 789 | 37732 | `ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999` |
| remediation gate v13 | 1324 | 61873 | `5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca` |
| historical implementation gate | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| historical implementation remediation gate v1 | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` |

The six provisional implementation paths were also freshly read in full and
re-hashed only to confirm their quarantine boundary. They supplied no design
meaning and were neither imported nor executed:

| Quarantined path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

```text
QUARANTINED_SOURCE_PATHS=6
QUARANTINED_SOURCE_LINES=7001
QUARANTINED_SOURCE_BYTES=482555
SOURCE_USED_AS_DESIGN_AUTHORITY=false
SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false
```

## L3. Major finding P15R-V13-M1: inherited VA/RA coordinates do not survive G death

**Severity:** Major. **Confidence:** high. **Scope:** exact terminal C13
classification, monotone tombstones, and survivor-mechanical auditability.

V13 repairs the v11 ACK-validation/seal gap by removing `AV`, but it leaves
two older G-local lifecycle coordinates, release validation `VA` and READY
send attempt `RA`, as stable binary history. Amendment v13 lines 579--591
retain both coordinates; lines 651--675 require distinct rows for their
values; lines 693--720 require exact externally retained, monotone history.
The v13 gate lines 38--41 independently requires every pre-seal failure to be
classified from exact available evidence and forbids reconstructing a
vanished G-local fact.

The first fixed-observation pair sets `X_P=X_G=0` and holds every P-surviving
fact constant:

```text
common P evidence:
  SA=1, SC=1 from P's sole complete release send
  no READY frame or bytes observed
  same authenticated G identity and pidfd/wait death receipt
  same exact drain-then-EOF and containment evidence

E0 — pre-validation death:
  G dies before complete release receive/validation
  true suffix VA=0, RA=RC=RV=AA=AC=SS=0
  required C13 row 9

E1 — post-validation/pre-READY death:
  G completely receives and validates the release, so VA=1
  G dies before beginning its READY send, so RA=0
  required C13 row 13
```

P cannot distinguish E0 from E1. Amendment v9 lines 584--618 assigns P the
release-send and READY-receive facts but assigns G the release-receive and
validation facts, expressly retaining them only in volatile, nonserialized
memory. Amendment v10 lines 563--570 defines `VA` and `RA`; lines 649--669
expressly require `VA=1` to survive a G crash before READY. V11 lines
583--584 and 667--674 preserve completed predecessors but add no cross-owner
carrier. V12 gate lines 408--431 and 476--503 already prove that a dead
G-local tombstone, G death, EOF, pidfd/wait, or sender-side complete send is
not evidence of G receive/validation. V13's only new G-to-P form occurs much
later, after READY and ACK, so it cannot distinguish this pair.

Collapsing both worlds to `VA=0` erases E1's completed monotone predecessor;
collapsing both to `VA=1` fabricates E0; an unknown value violates the exact
binary 33-row table. Thus the 33 vectors are a valid abstract enumeration of
binary prefixes but not an admissible exact-evidence terminal algebra.

A second fixed pair confirms the same defect for `RA`: hold `VA=1`, observe
no completed READY frame, and kill the same G either immediately before the
READY attempt (`RA=0`, row 13) or after the attempt begins but before complete
enqueue (`RA=1,RC=0`, row 17). The P evidence is again identical. V13 itself
recognizes the general rule at lines 547--550 by omitting a seal-attempt
coordinate because a dead G-local attempt receipt must never be guessed, yet
it preserves the older `RA` coordinate. This is one underlying cross-owner
survivor-audit defect, not a second counted finding.

**Required repair:** either make every pre-carrier G-local `VA`/`RA` step
ephemeral and rederive the complete terminal algebra, or publish an exact
authenticated crash-surviving cross-owner receipt before retaining each
coordinate. A repair may not infer, reset, fabricate, or silently label an
unknown value, and must re-prove feasibility, exhaustiveness, and monotone
tombstone auditability.

## L4. Major finding P15R-V13-M2: full send return is not an actual-endpoint enqueue receipt

**Severity:** Major. **Confidence:** high. **Scope:** sole positive commit,
first governed-write release, preflight sufficiency, and post-crash audit.

Amendment v13 lines 199--220, especially lines 209--211, assumes that a
full-length AF_UNIX `SOCK_SEQPACKET` send atomically enqueues exactly the same
record. Lines 228--267 claim that a disposable pair-A test establishes this
invariant, and lines 499--520 make the full return/enqueue event the sole
`SS=1` and first-write release. That equivalence is not unconditional Linux
v5.15 behavior.

The primary Linux v5.15 source gives a counterexample:

- `unix_seqpacket_sendmsg` delegates to `unix_dgram_sendmsg` at
  `net/unix/af_unix.c` lines 2242--2258.
- The delegated path runs `sk_filter(other, skb)` at lines 1842--1845. If it
  rejects the packet, the packet is discarded while the sender result is set
  to `len`; actual `skb_queue_tail` occurs only later at line 1939, followed
  by the ordinary `return len` at line 1944.
- `net/core/filter.c` lines 109--156 shows that this receive-side path can run
  cgroup ingress, security/LSM, and socket-filter logic, and can reject or
  trim the skb. Linux `socket(7)` likewise documents that
  `SO_ATTACH_FILTER`/`SO_ATTACH_BPF` can drop or truncate incoming packets.

Primary source locators:

- <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/net/unix/af_unix.c?h=v5.15>
- <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/net/core/filter.c?h=v5.15>
- <https://man7.org/linux/man-pages/man7/socket.7.html>

A fixed counterexample therefore gives the actual retained P endpoint a
receive filter or security/cgroup receive decision that drops or trims the
canonical seal. G's exact send returns the frame length, so the design sets
`SS=1` and releases the first governed write, but P later receives no exact
seal or a noncanonical truncated record. The disposable pair-A endpoint is a
different socket and uses a different fixed payload; it can pass while the
actual retained endpoint/seal path fails. No clause in the complete design
tuple freezes and mechanically proves the actual endpoint's absence of
socket filters or the acceptance/byte-preservation of cgroup/LSM receive
hooks. A full-tuple search found no `SO_ATTACH_FILTER`, `SO_ATTACH_BPF`,
`SO_LOCK_FILTER`, `sk_filter`, or endpoint-bound equivalent contract.

Amendment line 566's trusted non-Byzantine and byte-preserving transport
ceiling is a conclusory mismatch-handling premise, not the actual-endpoint-
bound mechanical establishment demanded by gate lines 45--50 and amendment
lines 262--267. If no-drop/no-trim behavior were expressly adopted as an
external model axiom, this counterexample would be outside that narrower
model; the current text instead asserts concrete Linux send/enqueue semantics
and says the disposable preflight establishes them. Under the stated
mechanical gate, the unsupported scope expansion is safety-relevant rather
than a documentation caveat.

**Required repair:** bind an exact, auditable no-drop/no-trim/no-receive-
rejection guarantee to the actual retained P endpoint and canonical seal
path, including socket filter, cgroup, and security-hook state, or move write
release to a crash-surviving actual-receipt mechanism such as a P receipt,
ACK, or shared persistence. A one-sample test on another socket/payload is
not a proof of that invariant. Any extra form or persistence mechanism needs
new remediation authority and a rederived commit/failure algebra.

## L5. Hostile attacks with no additional finding

The mandatory hostile surface was attacked independently. These checks do
not cure L3 or L4:

1. Excluding the L4 receive-filter/security counterexample, the v5.15
   enqueue path has no later sender-visible error branch before its full
   return. A crash after actual enqueue but before userspace return leaves the
   record queued; a pre-enqueue crash leaves no record. The design's P-side
   exact packet can therefore evidence the former without inventing a second
   transition.
2. Closing or losing the sole G endpoint does not purge P's peer receive
   queue. With the stated sole-holder/no-drain rules, P drains an already
   queued record before observing EOF. Complete, positive-short, and terminal-
   errno branches are exclusive under the narrowed no-filter/no-drop premise.
3. V13 genuinely removes the v11 `AV` coordinate and stable
   `ACK_VALIDATED` state. `SS` is the only newly committed seal coordinate;
   P's later validation is audit-only, sends no response, creates no second
   transition, and does not create an ACK chain.
4. The exact `BOOTSTRAP_SEALED` grammar, G-to-P direction, one-use slot,
   frame/digest joins, P three-item freeze receipt, G ten-item freeze receipt,
   eight-item seal preimage, concrete substitutions, and no-self-hash rule in
   amendment lines 290--473 are cardinality-complete and unambiguous.
5. The C13 list contains exactly 33 syntactically distinct vectors, 32
   failures and one success, with the printed prefix inequalities. Its defect
   is survivor-mechanical classification in L3, not an arithmetic duplicate
   or a second success row.
6. The seventeen raw predicates remain independent, are recorded before the
   separate priority permutation, retain every true losing bit and owner tie,
   and add no unauthorized label. No blocker was found in the raw17/priority
   text itself.
7. The fail-before-write fence text, owner freezes, PID binder, v9 seven-item
   release preimage, no retry/fallback, and post-success no-backflow rule are
   textually preserved. L4 supplies a concrete way the asserted success bit
   can lack its promised P-side carrier; no separate backflow finding is
   counted.
8. Global bootstrap form accounting is exactly plus three, with one v13 form;
   the scoped form counts remain 12/12/4. Base plus v1--v11 preservation,
   v5 no-op posture, v12 skip, schema, rows, 173 methods, nine generated
   members, 14 authority bindings, eight DAG nodes, and twelve DAG edges show
   no additional regression.

## L6. Exact active count-twelve successor authentication

Every historical amendment block remains byte-identical in the preserved
prefix. The following is the sole active count-twelve successor block. All
twelve listed files were independently read and hashed in printed order; the
v12 amendment is deliberately absent.

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v11]
count=12
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
10.path=notes/phase2_control_design_amendment_v10.md
10.sha256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
11.path=notes/phase2_control_design_amendment_v11.md
11.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
12.path=notes/phase2_control_design_amendment_v13.md
12.sha256=4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The block contains no blank or commentary line and no v12 entry. It adds no
schema field, authority binding, implementation path, generated member, DAG
node, or edge.

## L7. Verdict and authorization consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no research-wide theorem/evidence collapse independently found |
| Major (`M`) | 2 | `P15R-V13-M1` survivor-audit failure; `P15R-V13-M2` actual-endpoint enqueue overclaim |
| Minor (`m`) | 0 | no additional bounded defect independently found |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v13.0
CLOSURE_APPEND_ONLY=true
PRESERVED_PREFIX_LINES=5527
PRESERVED_PREFIX_BYTES=296651
PRESERVED_PREFIX_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c
PRESERVED_V11_INPUT_PREFIX_LINES=5080
PRESERVED_V11_INPUT_PREFIX_BYTES=270649
PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_V10_INPUT_PREFIX_LINES=4634
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

REVIEWED_REMEDIATION_GATE_V13_SHA256=5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca
REVIEWED_AMENDMENT_V13_SHA256=4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
REVIEWED_REMEDIATION_GATE_V12_SHA256=ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999
AMENDMENT_V12_PRESENT=false
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
SOURCE_USED_AS_DESIGN_AUTHORITY=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false
EXTERNAL_PRIMARY_SOURCE_STATIC_READ=true

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=REVISE_C0_M2_m0
P15R_V13_M1_STATUS=OPEN_REQUIRES_REMEDIATION_AUTHORITY
P15R_V13_M2_STATUS=OPEN_REQUIRES_REMEDIATION_AUTHORITY
P15R_V11_M1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
ALL_INHERITED_FINDINGS_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET

V13_SS_SOLE_COMMITTED_SEAL_COORDINATE=true
V13_HIDDEN_AV_FOUND=false
V13_C13_PRINTED_VECTOR_COUNT=33
V13_C13_SURVIVOR_MECHANICALLY_AUDITABLE=false
AF_UNIX_DISPOSABLE_PREFLIGHT_ACTUAL_ENDPOINT_BOUND=false
AF_UNIX_FULL_RETURN_IFF_EXACT_ENQUEUE_ESTABLISHED=false
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT=12
EFFECTIVE_AMENDMENTS=v1-v11-plus-v13

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
NEW_SUCCESSOR_IMPLEMENTATION_GOVERNANCE_GATE_CURRENTLY_AUTHORIZED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
PLATFORM_PRECHECK_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact base-plus-v1-through-v11-plus-v13 tuple is
**REVISE — C0/M2/m0**. V13's removal of stable ACK validation and addition of
one queued `BOOTSTRAP_SEALED` carrier materially addresses the narrow v11
AV/seal gap. It does not make the inherited G-local `VA`/`RA` coordinates
auditable after G death, and its full-return/actual-enqueue equivalence is not
mechanically established for the retained endpoint. The required zero-finding
closure condition is therefore unmet: inherited findings remain open, both
new Major findings require separate remediation authority, historical
implementation authority is not revived, and no source edit, implementation
review, platform precheck, execution, generated artifact, proof, Route,
manuscript, release, archive, or Git action is authorized. The complete
post-append path/line/byte/SHA-256 receipt and all exact prefix receipts are
issued externally immediately after this sole write because a file cannot
contain its own final digest without changing that digest.

# Fresh v14 independent static design re-review: carrier totality and endpoint-contract evidence

Status: **PASS — C0/M0/m0**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v14.0`  
Date: 2026-08-18 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static academic-design consistency,
reproducibility, and evidence-chain review  
Finding posture: the v14 gate, amendment, author-side conclusion, prior review,
and two auxiliary narrow reviews were treated as evidence inputs, not verdict
oracles  
Implementation, execution, source-edit, platform, artifact, Route,
manuscript, release, archive, and Git authority: **none**

## M1. Independent intake, preserved append boundary, and method

Before adjudication I freshly read in full the ARS-Codex 0.1.25 academic-
research-suite router and every reviewer, methodology, domain,
devil's-advocate, experiment-integrity, and reproducibility rule named by
the v14 gate. I applied their independence, fixed-observation, exact-
evidence, fail-closed, no-fabrication, and read-only-review requirements.
The complete rules re-hashed as follows:

| Complete ARS rule | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| methodology_reviewer_agent.md | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| domain_reviewer_agent.md | 397 | 31829 | `f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052` |
| devils_advocate_reviewer_agent.md | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |
| experiment-agent/WORKFLOW.md | 215 | 11555 | `c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef` |
| code_runner_agent.md | 117 | 4921 | `54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de` |
| reproducibility_protocol.md | 79 | 4150 | `49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |
| reproducibility_audit.md | 54 | 2388 | `a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b` |
| artifact_reproducibility_pattern.md | 173 | 9053 | `661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3` |

The sole append target remained a regular mode-0644, nlink-1 file. Its
complete 5,962-line, 321,362-byte pre-append body was read from beginning to
end and authenticated immediately before this append. Every historical
PASS/REVISE block and nested prefix receipt remains byte-identical:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=5962
PRESERVED_PREFIX_BYTES=321362
PRESERVED_PREFIX_SHA256=3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f
PRESERVED_HEAD_BYTES=296651
PRESERVED_HEAD_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c
PRESERVED_TAIL_BYTES=24711
PRESERVED_TAIL_SHA256=fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1
PRESERVED_V11_INPUT_PREFIX_BYTES=270649
PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
PREFIX_REWRITE_PERFORMED=false
```

The externally frozen v14 tuple matched exactly, including regular type,
mode 0644, nlink 1, line/byte counts, terminal LF, and SHA-256:

| Frozen v14 input | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_design_remediation_gate_v14.md` | 1665 | 84029 | `cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292` |
| `notes/phase2_control_design_amendment_v14.md` | 1414 | 65752 | `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c` |

`notes/phase2_control_design_amendment_v12.md` was absent under ordinary,
symlink-aware, and path-list checks. Only the frozen v14 amendment occupied
the v12/v14 successor-name slice. No alternate v14 amendment, temporary,
lock, cache, generated, or recovery path was used.

## M2. Complete design, governance, and quarantine authentication

I freshly read and re-hashed the base and every amendment record in the
operative chain. V5 remains a blocked/no-op provenance record. V12 remains
skipped and has no amendment:

| Design record | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` |
| amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` |
| amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` |
| amendment v11 | 1072 | 49086 | `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269` |
| amendment v13 | 1057 | 48820 | `4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27` |
| amendment v14 | 1414 | 65752 | `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c` |

The complete reopen/remediation/recovery chain and both historical
implementation gates were also read in full. Their re-hashed governance
sequence was:

```text
DESIGN_REOPEN_GATE_SHA256=8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973
REMEDIATION_GATE_V1_SHA256=98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16
REMEDIATION_GATE_V2_SHA256=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705
REMEDIATION_GATE_V3_SHA256=e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac
REMEDIATION_GATE_V4_SHA256=df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647
REMEDIATION_GATE_V5_SHA256=55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7
REMEDIATION_GATE_V6_SHA256=a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00
REMEDIATION_GATE_V7_SHA256=a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576
REMEDIATION_GATE_V8_SHA256=342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8
REMEDIATION_GATE_V9_SHA256=c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90
REMEDIATION_GATE_V10_SHA256=48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5
REMEDIATION_GATE_V11_SHA256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
REMEDIATION_GATE_V12_SHA256=ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999
REMEDIATION_GATE_V13_SHA256=5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca
REMEDIATION_GATE_V14_SHA256=cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292
AMENDMENT_V11_PATH_RECOVERY_GATE_SHA256=41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888
V13_REVIEW_APPEND_RECOVERY_GATE_SHA256=2a0ac6ea868fd5b37b77d21df5c4375123942b5f3ef50926a7609307e048de16
HISTORICAL_IMPLEMENTATION_GATE_SHA256=e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8
HISTORICAL_IMPLEMENTATION_REMEDIATION_GATE_SHA256=52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f
V12_GATE_VERDICT=BLOCKED
AMENDMENT_V12_PRESENT=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
```

The six quarantined paths were read only as static nonauthority evidence.
They remain the old implementation tuple and cannot define, validate, or
rescue v14 design meaning:

| Quarantined path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

```text
QUARANTINED_SOURCE_PATHS=6
QUARANTINED_SOURCE_LINES=7001
QUARANTINED_SOURCE_BYTES=482555
SOURCE_USED_AS_DESIGN_AUTHORITY=false
SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false
```

## M3. P15R-V13-M1 closure: carrier-only C14 is total within its stated scope

The operative tuple is exactly
`C14=(RE,YE,AE,SS,E_PG,E_GP)`. RE, YE, AE, and SS are actual enqueue
events on the sole state-qualified real endpoint slots; E_PG and E_GP are
complete recognizable pre-directional-cut out-of-slot enqueue facts. Send
entry, partial send, userspace return, receive invocation, parsing,
validation, hash construction, freeze, and staging create no coordinate.
The former volatile owner-local VA/RA/AV-style history therefore cannot
split two worlds that have the same surviving carrier evidence.

Independent enumeration under
`YE<=RE`, `AE<=YE`, `SS<=AE`, `AE=>E_PG=0`, and
`SS=>(E_PG,E_GP)=(0,0)` gives exactly these fifteen distinct vectors in the
printed row order:

```text
000000 000010 000001 000011
100000 100010 100001 100011
110000 110010 110001 110011
111000 111001
111100
```

The prefix multiplicities are `4+4+4+2+1=15`. Rows 1--14 are failures;
row 15 alone is success. Row 14 is the admissible asymmetric clean-P/
pre-seal-extra-G vector `111001`; its forbidden mirror is excluded by AE's
published P-to-G clean cut. Row 15 is `111100`. No duplicate, missing,
second-success, unreachable printed vector, or local-coordinate alias was
found.

Failure classification is not frozen at timeout, errno, death, or missing
successor. It first stops all future in-scope enqueue, establishes the
holder/profile/no-reader ceiling, retains exactly one authenticated owner
survivor, drains the survivor inbound actual queue through exact EOF,
reconciles outbound endpoint-bound receipts, counts pre-cut extras once,
and only then freezes C14, raw17, winner, and tombstone. For each carrier
enqueue under the accepted profile, single-owner loss leaves either the
surviving receiver's exact queued frame or the surviving sender's exact
endpoint-bound full-return receipt. Duplicate evidence names one enqueue.
When those prerequisites cannot be established, no exact row is claimed;
double-owner loss remains expressly outside `UNIVERSAL_RECOVER_P`.

The fixed-observation collapse is consequently honest: vanished private
validation, attempt timing, or detection does not survive as a bit. A
complete actual carrier does. A partial/no-enqueue attempt and no attempt
remain the same carrier state. No post-cut or downstream receipt can flow
back into C14, raw17, or a frozen tombstone.

SS changes at exact canonical Seal enqueue and immediately finalizes the
bilateral clean-cut success. A live G's exact complete Seal send return is a
separate execution fence, not a C14 coordinate. If SS enqueues and G dies
before observing return, P's exact queued Seal before EOF audits already-
final row 15; G has no governed-write or normal-clone authority. P's later
receipt/validation is audit and live-window closure only. This preserves
success finality without inventing an ACK-of-Seal or post-success backflow.

The raw classifier remains exactly seventeen independent predicates:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

Its printed priority is a permutation of the same set, every bit is computed
before winner selection, and all supported losing bits and owner ties are
retained. PARTIAL requires a surviving positive proper-prefix/truncation
receipt; MISSING is available only at the reconciled checkpoint. No
unobservable local detection is reconstructed.

Therefore `P15R-V13-M1` is closed by the exact v14 carrier algebra and its
single-survivor reconciliation, within the expressly stated model ceiling.

## M4. P15R-V13-M2 closure: actual endpoints, exact timing, and honest model ceiling

The endpoint identity is no longer inferred from a disposable pair:
`EP_P` is P's accepted actual endpoint receiving G-to-P, and `EP_G` is G's
connected actual endpoint receiving P-to-G. There is no FD handoff,
`pidfd_getfd`, or hidden third owner in the design. Each owner constructs a
seven-item local HP/HG receipt on its own receive endpoint, including the
locked accept-all classic-BPF transcript and two exact readbacks. P also
constructs the reciprocal four-item HM holder/Unix-diag matrix; MECH has
exactly five dense items binding HP, HG, and HM.

The asymmetric F12 happens-before order is exact: G completes its local
drop and HG; G enqueues epoch-2 REAPED; P validates it and completes L reap/
sole-G proof; the denial child performs only the required first-instruction
endpoint closes and is killed/reaped/gone; P completes denial evidence,
HP, and HM; only then may LAUNCHER_REAPED and revised RELEASE occur. The
same pre-LAUNCHER cut token is used by HP/HG/HM and the downstream binding.
There is no backdated HP, HG, H, or RELEASE observation.

The item-30/31/38 F13 surface freezes each endpoint at its respective time.
EP_P admits no additional reference through the complete window. EP_G
admits none before live G observes exact Seal full return and afterward only
the trusted child's transient alias, whose fixed first instruction closes
it before any non-close endpoint action or barrier. The live window ends
only after both G's exact return and P's exact Seal receipt/validation; all
other paths use terminal drain/classification, no future scoped send, and
both endpoint closes. SS-enqueue/pre-return G death therefore does not end
the window early. No hidden post-Seal alias, reader, drain, or post-cut
backflow is admitted.

F14 is not self-contradictory: the general endpoint-operation prohibition
has one explicit close-only exception for the denial child and post-return
trusted child. The required close calls are permitted; read, send, receive,
peek, drain, shutdown, duplication, transfer, registration, and barrier
passage remain forbidden.

HC has exactly 41 dense items. Its exact 2,928-byte preimage re-hashes to
`1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1`.
The profile binds the real endpoints, locked accept-all receive filters,
holder/reference policy, hook/cgroup/LSM/custody conditions, carrier scope,
and both window ends. This closes the v13 disposable-endpoint scope gap only
conditionally: HC explicitly says its hash is not evidence, no current run
or runtime attestation is accepted, and no current platform or execution
authority exists. A separate future execution-governance gate must accept
the exact static HC and one execution-window class before the profile window
begins; failure yields only `E_POSSESSION_UNAVAILABLE` with no fallback.

Under that explicit external static axiom and trusted non-Byzantine P/G
ceiling, the stated Linux-v5.15 full-return-to-enqueue implication is scoped
to the actual locked endpoints and canonical in-window frames. Outside that
accepted ceiling the design makes no mechanical or current-platform claim.
The conditional statement is therefore honest and does not promote HC,
root identity, a disposable sample, or a hash into runtime evidence.

The contract hash H is over exactly five US-ASCII lines with exactly five
LF bytes, including the terminal LF: sole domain, session, carrier-scope ID,
MECH hash, and HC hash. The release bundle has three dense items; the outer
release attestation has eight; ACK chain has five; Seal chain has six.
RELEASE binds HP/HM/HC but no future HG/MECH/H. READY first publishes
HG/MECH/H. ACK binds Launcher/RELEASE/READY, and Seal binds
Launcher/RELEASE/READY/ACK. No preimage includes its own digest, its future
carrier, a carrier bit, terminal drain fact, or a backward edge. The hash
dependency graph is acyclic and has no field/preimage circularity.

Therefore `P15R-V13-M2` is closed by the actual-endpoint receipts plus the
explicitly conditional, static, non-evidentiary HC ceiling. This closure is
design-only and is not platform acceptance or implementation evidence.

## M5. Frozen counts, inherited semantics, and authority boundary

V14 adds zero wire forms and revises only RELEASE, READY, ACK, and Seal.
The global bootstrap delta versus v2 remains exactly plus three: v9 RELEASE,
v11 ACK, and v13 Seal. No ACK-of-Seal, ACK-of-ACK, retry, fallback,
reconnect, record reuse, shared persistence, or endpoint self-test is added.
The inherited exact form counts remain `12/12/4`.

The complete scientific/package vector remains unchanged:

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
CSV_HEADER_WIDTHS=18,19,22,17,16,19,13,10
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
TOLERANCE_POLICY=EXACT_ZERO
NETWORK_USED=false
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The graph remains nodes `A D R G I C M V`, chain edges
`A->D->R->G->I->C->M->V`, and the five additional edges
`A->M,D->M,R->M,G->M,I->M`: eight nodes and twelve distinct edges.
No row, schema, method, artifact, generated member, authority binding, DAG
node, or edge changed. Base plus v1--v11 and v13 semantics remain in force
except where v14 expressly supersedes the lifecycle, actual-endpoint, and
timing surfaces reviewed above.

## M6. Exact active count-thirteen design and final closure

All thirteen records below were independently read and hashed in printed
order. This is the sole new active successor marker. V12 is deliberately
absent and skipped; the marker version is the next append-sequence version,
not an amendment-v12 revival.

[P15R-EFFECTIVE-DESIGN-AMENDMENTS v12]
count=13
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
10.path=notes/phase2_control_design_amendment_v10.md
10.sha256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
11.path=notes/phase2_control_design_amendment_v11.md
11.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
12.path=notes/phase2_control_design_amendment_v13.md
12.sha256=4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
13.path=notes/phase2_control_design_amendment_v14.md
13.sha256=b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

The independent severity disposition is:

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no research-wide theorem/evidence collapse found |
| Major (`M`) | 0 | both v13 Majors closed by v14 within its exact conditional ceiling |
| Minor (`m`) | 0 | no bounded consistency or reproducibility defect found |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v14.0
CLOSURE_APPEND_ONLY=true
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OVERALL_CLOSURE_VERDICT=PASS_C0_M0_m0

P15R_V13_M1_STATUS=CLOSED_BY_V14_FRESH_ZERO_FINDING_REREVIEW
P15R_V13_M2_STATUS=CLOSED_BY_V14_FRESH_ZERO_FINDING_REREVIEW
P15R_V11_M1_STATUS=CLOSED_BY_V14_FRESH_ZERO_FINDING_REREVIEW
ALL_INHERITED_DESIGN_FINDINGS_STATUS=CLOSED_BY_V14_FRESH_ZERO_FINDING_REREVIEW

C14_COORDINATES=RE,YE,AE,SS,E_PG,E_GP
C14_VECTOR_COUNT=15
C14_FAILURE_VECTOR_COUNT=14
C14_SUCCESS_VECTOR_COUNT=1
C14_SUCCESS_VECTOR=111100
C14_ROW14_VECTOR=111001
C14_SURVIVOR_MECHANICALLY_AUDITABLE_UNDER_STATED_CEILING=true
SS_ENQUEUE_PRE_RETURN_G_DEATH_CLASS=ROW15_NONLIVE_SUCCESS_AUDIT
LIVE_G_FULL_RETURN_IS_C14_COORDINATE=false
P_SEAL_RECEIPT_VALIDATION_IS_SUCCESS_OR_WRITE_AUTHORITY=false
RAW_CLASSIFIER_PREDICATE_COUNT=17
RAW_BITS_COMPUTED_BEFORE_WINNER=true
ALL_TRUE_LOSER_BITS_RETAINED=true

HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
ACTUAL_ENDPOINT_CONTRACT_LINE_COUNT=5
ACTUAL_ENDPOINT_CONTRACT_LF_COUNT=5
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_RUN_PROFILE_ACCEPTED=false
CURRENT_RUNTIME_ATTESTATION_PRESENT=false
CURRENT_EXECUTION_AUTHORITY=false
CURRENT_PLATFORM_AVAILABILITY_CLAIM=false

V14_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT=13
EFFECTIVE_AMENDMENTS=v1-v11-plus-v13-plus-v14
AMENDMENT_V12_PRESENT=false
AMENDMENT_V12_SKIPPED=true

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
PLATFORM_PRECHECK_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
PROOF_MODIFICATION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact
`base + v1--v11 + v13 + v14` tuple is **PASS — C0/M0/m0** for static
deterministic-control design only, under the exact conditional unverified
deployment-model ceiling stated by v14. `P15R-V13-M1`, `P15R-V13-M2`, and
all inherited design findings are closed. This review does not accept HC for
any deployment, validate a platform or current run, implement or execute the
controls, revive either historical implementation gate, or authorize any
source edit, implementation review, preflight, generated artifact, proof,
Route, composition, manuscript, release, archive, or Git action. A separate
successor governance gate remains necessary before any such work. The final
post-append path/line/byte/SHA-256 and preserved-prefix receipts are issued
externally after this sole append because this file cannot contain its own
final digest without changing that digest.

# Fresh v15 independent hostile design re-review: P-lifetime capability closure

Status: **REVISE — C0/M5/m1**  
Review ID: `P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v15.0`  
Date: 2026-08-18 (Asia/Shanghai)  
Review mode: fresh independent exact-byte static academic-design,
evidence-chain, Linux-5.15-semantics, and hostile-counterexample review  
Finding posture: the v15 gate, amendment, author-side conclusion, prior
reviews, implementation review, and auxiliary audits were treated as claims
or evidence inputs, never as verdict oracles  
Implementation, execution, source-edit, artifact, Route, manuscript, release,
archive, and Git authority: **none**

## N1. Intake, independence, exact prefix, and frozen authority

I freshly read in full the applicable ARS-Codex 0.1.25
academic-research-suite skill, academic-paper-reviewer workflow, methodology
reviewer prompt, and devil's-advocate reviewer prompt. I applied their
independent-oracle, fixed-observation-pair, evidence-strength, hostile-audit,
anti-bundling, no-fabrication, and read-only-review requirements. The complete
method records used by this review were:

| Complete ARS record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `academic-research-suite/SKILL.md` | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| `academic-paper-reviewer/WORKFLOW.md` | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| `methodology_reviewer_agent.md` | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| `devils_advocate_reviewer_agent.md` | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |

The v15 review intake was byte 0 through EOF, not a delta-only read. It
included the v15 gate and amendment; this complete review prefix; the original
gate and base; every active amendment v1--v11, v13, and v14; blocked/no-op v5;
the ATTEMPT_3 implementation review; the controlling implementation v5 STOP;
and the relevant Linux 5.15 primary source. Amendment v12 remains absent and
skipped.

Immediately before this sole append, the review target and both frozen v15
inputs were regular mode-0644, nlink-1 files. Their exact receipts were:

| Frozen input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| preserved review prefix | 6431 | 346453 | `2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19` |
| v15 remediation gate | 1085 | 48390 | `c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a` |
| v15 amendment | 1132 | 52502 | `158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239` |

The preserved prefix was authenticated before adjudication and again at the
write boundary. Every historical review block and the effective v14 PASS
marker remains evidence in its original byte order:

```text
PRESERVED_PREFIX_PATH=notes/phase2_control_design_peer_review.md
PRESERVED_PREFIX_LINES=6431
PRESERVED_PREFIX_BYTES=346453
PRESERVED_PREFIX_SHA256=2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19
PRESERVED_PREFIX_MODE=0644
PRESERVED_PREFIX_NLINK=1
PREFIX_REWRITE_PERFORMED=false
```

The exact effective predecessor tuple was also fully read and authenticated:

| Record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| amendment v5, blocked/no-op | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` |
| amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` |
| amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` |
| amendment v11 | 1072 | 49086 | `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269` |
| amendment v13 | 1057 | 48820 | `4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27` |
| amendment v14 | 1414 | 65752 | `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c` |
| consumed v14 remediation gate | 1665 | 84029 | `cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292` |

The controlling implementation boundary was read in full and remains:

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| ATTEMPT_3 implementation peer review | 643 | 37947 | `637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88` | `REVISE_C0_M12_m0` |
| implementation remediation gate v5 | 733 | 31304 | `411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7` | `STOP_DESIGN_REOPEN_REQUIRED` |

ATTEMPT_4 is unconsumed but suspended and unavailable. Neither the v15 gate,
the v15 amendment, nor this review spends it or authorizes source mutation.

The six frozen implementation paths were checked only as immutable
quarantine:

| Frozen path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1133 | 60497 | `4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020` |
| `code/test_controls.py` | 1655 | 129574 | `c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac` |
| `code/README.md` | 95 | 5267 | `96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee` |
| `experiments/reproduce.sh` | 6270 | 469357 | `dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59` |
| `experiments/README.md` | 226 | 14697 | `ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6` |
| `results/README.md` | 76 | 3221 | `03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c` |

They total exactly 9455 lines and 682613 bytes. No project module was
imported or executed; no test, reproduction script, probe, platform precheck,
syntax check, Git operation, or source write was performed.

## N2. Primary Linux 5.15 semantic baseline and bounded positive results

The primary-source baseline was checked at the exact v5.15 tag:

- `kernel/pid.c` `pidfd_create()` obtains a pidfd with
  `anon_inode_getfd("[pidfd]", &pidfd_fops, ..., O_RDWR|O_CLOEXEC)`;
- `fs/anon_inodes.c` documents and implements the ordinary
  `anon_inode_getfd()` path with the shared singleton anonymous inode;
- `kernel/fork.c` `pidfd_show_fdinfo()` permits `Pid: 0` when the target is
  outside the reader's descendant PID-namespace view;
- `kernel/fork.c` `pidfd_poll()` returns `EPOLLIN|EPOLLRDNORM` only once the
  target whole thread group has exited; and
- `kernel/fork.c` `copy_files()` calls `dup_fd()` when `CLONE_FILES` is
  absent, producing separate FD tables but no parent-close/child-progress
  synchronization edge.

Primary locators:

- <https://raw.githubusercontent.com/torvalds/linux/v5.15/kernel/pid.c>
- <https://raw.githubusercontent.com/torvalds/linux/v5.15/fs/anon_inodes.c>
- <https://raw.githubusercontent.com/torvalds/linux/v5.15/kernel/fork.c>

Those semantics support several v15 decisions. Requiring `(revents & POLLIN)
!= 0`, rejecting `POLLNVAL|POLLERR`, not requiring `POLLHUP`, and not demanding
exact `revents` equality is correct for Linux 5.15. A G-side fdinfo `Pid:0`
is not a mismatch or death observation. Pidfd readiness proves whole-thread-
group exit, not signal, status, core, cause, or reap. The v15 normal-success
non-backflow rule and the full v14 P_CRASH guard correctly keep readiness
necessary but insufficient. EOF alone, signal 0, wait/ECHILD, and an old
procdir fstat are correctly rejected as substitute death evidence.

No additional finding was found in the exact G-child trusted close-only stub:
ordinary fork transiently copies FD12, EP_G is closed first when present,
FD12 is then closed and proved EBADF, and SANITIZED/registration/non-close
work follows. The four worker FDSET values remain unchanged. The numerical
C14, raw17, D-M1, D-M2, FDSET, HC, package, scientific, and DAG vectors also
recompute to their printed values. These positive results do not cure the
five independent defects below.

## N3. Major finding P15R-V15-M1: unclassified target occupants can be silently destroyed

**Severity:** Major. **Confidence:** high. **Scope:** possession safety,
retained-capability continuity, four-source transaction totality, and
pre-clone fail-closed behavior.

Amendment v15 Section 3.2 lines 211--221 excludes concurrent or interleaved
allocation, and Section 3.3 lines 237--269 records R10--R13 and their high
stages. It never classifies the current occupants of destination integers
10--13 before `dup3`. Linux `dup3(oldfd,newfd,...)` atomically closes an
already-open `newfd`. The special rule at lines 260--263 protects only a raw
R10--R13 reference whose integer is itself displaced.

That is not a closed destination set. Active v6 Section 4.2 lines 875--888
requires P to retain exactly one `LONG_LIVED_PROC_ROOT` through final endpoint
audit. V15 Section 3.2 line 215 expressly says P still owns the trusted outer
proc-root at acquisition. P can also hold control, cgroup, signalfd, and other
pre-existing descriptors. If any such nontransaction descriptor occupies 12
or 13, the high-stage sequence succeeds and the later `dup3(H12,12,...)` or
`dup3(H13,13,...)` silently closes it. It has no R-serial, no unwind entry,
and no restoration rule; the algorithm can still claim `SLOTS_INSTALLED`.
The same defect exists in the gate's Sections 3.2--3.3. Hostile item 1 covers
collision with a retained *raw/source* reference, not this third-party target
occupant.

**Minimum v16 repair obligation:** inside the same allocation barrier and
before the first staging duplicate, classify the occupant of each target
10--13 by acquisition serial and object identity. Each target must be either
vacant with exact `EBADF` evidence or exactly one of R10--R13. Any unrelated
occupant must yield `E_POSSESSION_UNAVAILABLE`/STOP before any `dup3`.
Preserving an unrelated occupant instead would require adding it, a new
destination, and a complete unwind to the transaction and would therefore
reopen the frozen four-source scope; fail-closed rejection is the minimal
repair.

## N4. Major finding P15R-V15-M2: the single closed ledger cannot encode its required references or displacement

**Severity:** Major. **Confidence:** high. **Scope:** exact failure tombstones,
unwind evidence, reference liveness, and monotone state closure.

V15 Section 2 line 173 says all references and transitions reside in one
`P_LIFETIME_LEDGER`. Section 3.3 requires entries for all four raw references,
H10--H13, installed targets, and each displaced raw serial. Yet Section 6
lines 498--508 closes `kind` to only
`P_SELF_PIDFD|P_INITIAL_PROC_PID_DIR`. It cannot name repository/package
roots R10/R11, H10/H11, or their installed targets, and it has no independent
raw/stage/target reference-role field.

The closed state enum at lines 482--496 also omits the mandatory
`DISPLACED_BY_TARGET` disposition from lines 260--263. `CLOSED_PROVED` cannot
stand in for it: Sections 5.2 and 6 require an actual live `close()` return
plus immediate `EBADF`. `OWNER_DIED_RELEASED` requires owner death. A raw
reference atomically displaced by `dup3` satisfies neither predicate. The
gate repeats the same closed enum and two-kind schema.

This is a schema contradiction, not editorial shorthand. In a partial install
or unwind the prescribed single ledger cannot truthfully retain every actual
reference and completed prefix, so its exact tombstone and ABA claims are not
mechanically representable.

**Minimum v16 repair obligation:** define a closed entry algebra that
separately binds transaction, per-object kind (repository root, package root,
P pidfd, P procdir), reference role (raw, high stage, fixed target, inherited
actor copy), local integer, object identity, and liveness/disposition. Add an
explicit `DISPLACED_BY_TARGET` terminal reference disposition distinct from
the transaction phase and from live-close/death outcomes. Recheck every
success and reverse-unwind transition against that algebra.

## N5. Major finding P15R-V15-M3: the receipt has no unique transaction/per-reference serial grammar

**Severity:** Major. **Confidence:** high. **Scope:** immutable receipt
grammar, FD12/FD13 cross-binding, ABA exclusion, and independent G validation.

Section 3.3 lines 246--249 creates one transaction acquisition serial **and**
a distinct serial for each reference. The exact receipt field list in Section
4.1 lines 319--333 contains only singular `acquisition_serial`. Section 4.3
lines 374--377 then requires G to validate FD12 and FD13 `acquisition serials`
in the plural. Section 6 gives each ledger entry another singular
`acquisition_serial` but never defines how it joins the receipt scalar.

Consequently the exact grammar has no unique interpretation: the receipt
scalar can be the transaction serial, R12's serial, or R13's serial, and one
scalar cannot independently bind both capability references if the serials
are distinct. A trusted implementation author could choose one reading, but
an independent verifier cannot mechanically decide which reading is
normative. This defect survives a repair of the ledger kind/state enum and is
therefore counted separately.

**Minimum v16 repair obligation:** name distinct immutable fields, at least
`transaction_serial`, `pidfd_acquisition_serial`, and
`procdir_acquisition_serial`, or an exactly equivalent closed tuple. Each
ledger entry must carry the transaction serial plus its own per-reference
serial, and G must join slot 12 and slot 13 to the corresponding receipt field
independently before any identity transition.

## N6. Major finding P15R-V15-M4: pidfd fstat is class evidence, not exact target or OFD identity

**Severity:** Major. **Confidence:** high. **Scope:** P/G identity binding,
FD12 substitution resistance, D-M2 identity-drift claims, and terminal
classification soundness.

Section 4.1 lines 323--344 records `pidfd_type_and_fstat_identity` and calls
the later join exact. Section 4.3 lines 374--381 requires G to verify the exact
inherited P_SELF_PIDFD OFD/fstat identities. Section 7.1 lines 547--554 says
D-M2 rejects FD12 replacement or identity drift.

On Linux 5.15 `pidfd_create()` uses the ordinary `anon_inode_getfd()` path,
and ordinary anonymous-inode files share the singleton anon inode. Therefore
pidfd `fstat` device/inode/mode is useful class/type sanity, but it neither
identifies the target process nor proves that two descriptors reference the
same open file description. G-side fdinfo is expressly permitted to show
`Pid:0`; the zero-time nonready poll is shared by every still-live target.
The specified G observations thus have no independent OFD comparator. The
fixed D-M2 snapshot/readlink operations likewise cannot distinguish a
replacement live pidfd having the same anon-inode class and `Pid:0`.

Ordinary fork/COW plus a gapless trusted-program rule can establish same-OFD
lineage as a static invariant. It is not a mechanically unique fstat identity,
and the current text conflates those evidence strengths. A wrong replacement
pidfd can later become readable for a different process and make an exact
P_CRASH classification unsound if the advertised substitution detection is
relied upon.

**Minimum v16 repair obligation:** state that pidfd fstat is class/type sanity
only and never unique target/OFD identity. Define the authoritative binding
as the P-side fdinfo PID, procdir field-22 starttime/object join, explicit
per-reference serial, and a gapless ordinary-fork/no-`CLONE_FILES`/no-exec/
no-replacement lineage. Narrow D-M2's claim to the observable slot, set,
type/class, flags, generation, and trusted-lineage invariants. If independent
exact OFD comparison is still required, v16 must authorize a feasible
comparator, holder timing, and permission model; prose naming fstat `exact`
is not that comparator.

## N7. Major finding P15R-V15-M5: local close order does not establish the global P--L--G holder cuts

**Severity:** Major. **Confidence:** high. **Scope:** FD12/13 holder ceiling,
pre-PID1_READY FD13 absence, identity-transition guard, HC non-reopening, and
normal/P_CRASH evidence ownership.

The Section 5.1 matrix claims that after P's successful clone branch only L
holds 12/13, after L's successful fork branch only G holds them, and after G
identity binding nobody holds FD13. Lines 411--419 specify only each process's
local program order. Separate FD tables from omitting `CLONE_FILES` prevent a
close in one process from affecting another; they do not order the L parent
branch before the G child branch.

A legal schedule is:

```text
L forks G, creating separate L and G references to FD12 and FD13
G runs first, validates its own slots, closes its own FD13, and proves EBADF
G connects and sends PID1_READY
L parent has not yet run and still holds both FD12 and FD13
```

That trace satisfies every stated local G close but contradicts the holder
matrix, Section 7's claim that FD13 is gone before PID1_READY, and the HC/no-
extra-holder reasoning. `LAUNCHER_REAPED` occurs later and therefore cannot
prove the claimed pre-PID1_READY cut.

The P side is also under-specified. Lines 411--414 require P to close before
its much later denial child, but do not order P's close receipts before P
processes `U1_CREATED`, writes the maps, and sends `U1_MAPS_COMMITTED`. Without
that explicit order, the existing L block does not establish that P has
released 12/13 before L can eventually fork G.

**Minimum v16 repair obligation:** freeze the P order as

```text
P clone3 parent return
-> close(13)/EBADF
-> close(12)/EBADF
-> only then process U1_CREATED, write/re-read maps, and send U1_MAPS_COMMITTED
```

The existing U1 handshake then provides the P-to-later-L/G happens-before
edge with no new form. For L-to-G, add a real one-use local release barrier:
G may not perform identity validation, connect, or send PID1_READY until an
event causally generated only after L completes both close/EBADF receipts has
been consumed. A fully specified stop/wait/continue barrier or equivalent
can in principle avoid a new P--G wire form, but it is a new governed local
transition requiring v16 authority and hostile review. Merely saying `parent
branch first` is not synchronization. If the pre-send deadline is weakened to
a P-side acceptance proof instead, every affected matrix, PID1_READY, HC, and
ledger claim must be rewritten and mechanically re-proved. Under the current
v15 prohibition on any such new synchronization delta, this finding is not
repairable by interpretation.

## N8. Minor finding P15R-V15-m1: the parent/child direction is reversed

**Severity:** Minor. **Confidence:** high. **Scope:** normative explanation of
the wait prohibition; no separate unsafe wait is authorized.

Amendment and gate Section 8.2 say `G is not P's child`. Active v2 has P call
`PR_SET_CHILD_SUBREAPER`; L forks G; P later reaps L. In the normal carrier
topology G is then P's descendant/adopted child in the outer namespace. The
relevant reason G cannot wait or reap P is the reverse: **P is not G's
child**. The explicit wait/waitid prohibition and rejection of ECHILD as
death evidence remain safe, so this is a bounded normative inconsistency
rather than a sixth Major.

**Minimum v16 repair obligation:** in both gate-quality normative text and
the amendment, replace the sentence with `P is not G's child; after L is
reaped, G is normally P's descendant/adopted child in the outer namespace`,
while retaining every existing wait/reap prohibition.

## N9. Twenty-five hostile pairs, counts, and no-wire audit

All twenty-five mandatory v15 attacks were independently exercised as static
fixed-observation counterexamples. `CLOSED` below means no additional finding;
it does not override another row's open root cause.

| # | Independent disposition |
|---:|---|
| 1 | **OPEN M1:** the four-source algorithm handles raw/source collisions but not an unrelated pre-existing target-10--13 occupant. |
| 2 | **OPEN M2 (evidence closure):** reverse unwind prose exists, but the closed ledger cannot represent every R10/R11/stage/displaced reference. |
| 3 | **CLOSED:** `CLONE_FILES` and exec are explicitly outside the topology. |
| 4 | **OPEN M3/M4 at the inherited join:** P-side PID/starttime mismatch checks are sound, but G's exact per-capability serial/OFD rejoin is not uniquely specified or independently observable. |
| 5 | **CLOSED:** procdir field-22 starttime rejects numeric-PID reuse at acquisition. |
| 6 | **CLOSED:** G-side fdinfo `Pid:0` is correctly accepted without a death inference. |
| 7 | **CLOSED:** EOF with nonready FD12 cannot become P_CRASH. |
| 8 | **CLOSED:** finalized row-15 success cannot backflow when FD12 later becomes ready. |
| 9 | **CLOSED operationally; m1 rationale:** wait is forbidden and ECHILD is rejected, but the printed parent/child explanation is reversed. |
| 10 | **CLOSED:** signal-0 EINVAL/EPERM/success is forbidden as death evidence. |
| 11 | **CLOSED:** old procdir fstat is not life evidence and conforming G closes FD13 pre-ready. |
| 12 | **CLOSED:** hidepid/permission proc failure is not death evidence. |
| 13 | **CLOSED:** POLLIN is required; POLLHUP and exact revents equality are not. |
| 14 | **CLOSED:** pidfd readiness waits for whole-thread-group exit. |
| 15 | **CLOSED:** the trusted child stub removes FD12 before SANITIZED/registration/non-close work. |
| 16 | **OPEN M4:** numeric/type snapshot classification cannot provide the advertised exact pidfd OFD/target identity-drift rejection. |
| 17 | **OPEN M5:** G can send PID1_READY while L still holds FD13; G's local close does not prove global absence. |
| 18 | **OPEN M2/M3:** displacement is absent from the closed state algebra and transaction/per-reference serials are not uniquely joined. |
| 19 | **CLOSED:** ready FD12 without holder ceiling, exact EOF/drain, and reconciliation remains exit-only evidence. |
| 20 | **CLOSED:** pre-carrier P death remains bootstrap failure, not a forced C14 row. |
| 21 | **CLOSED:** poll cannot prove signal/status/core and v15 refuses to invent them. |
| 22 | **CLOSED:** v15 correctly admits only the unavoidable kernel-instant child copy followed by the trusted close-only stub. |
| 23 | **CLOSED:** the receipt bearer is ordinary immutable fork/COW state, not env/wire/shared persistence. |
| 24 | **CLOSED:** no new wire form/field, SCM_RIGHTS item, endpoint handoff, reconnect, or second ancillary is added. |
| 25 | **COUNTS CLOSED; SEMANTIC HC CLAIM OPEN M5:** printed constants are unchanged and arithmetically exact, but the asserted holder cut supporting unchanged HC is false on the schedule in N7. |

Independent count recomputation gives:

```text
C14_COORDINATES=RE,YE,AE,SS,E_PG,E_GP
C14_VECTOR_COUNT=15
C14_FAILURE_VECTOR_COUNT=14
C14_SUCCESS_VECTOR_COUNT=1
C14_SUCCESS_VECTOR=111100
C14_ROW14_VECTOR=111001
RAW_CLASSIFIER_PREDICATE_COUNT=17
RAW_BITS_COMPUTED_BEFORE_WINNER=true
ALL_TRUE_LOSER_BITS_RETAINED=true

HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1

WORKER_FDSET_VALUE_COUNT=4
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
ADMIT_FORM_COUNT=1
V15_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3

DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
CSV_HEADER_WIDTHS=18,19,22,17,16,19,13,10
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
TOLERANCE_POLICY=EXACT_ZERO
```

`AUTHORITY_BINDINGS=14` remains the package binding count, not an amendment
count. No v15 public coordinate, C14 row, raw bit, endpoint, wire field, form,
SCM_RIGHTS item, D-M2 tag, artifact, manifest member, or DAG edge was found.
The defects are private design/evidence-closure defects; fixing them may not
silently change these frozen public counts.

## N10. Effective chain, severity, verdict, and authority consequence

Because acceptance requires exactly `PASS_C0_M0_m0`, v15 is not effective.
This REVISE append deliberately publishes no new effective-amendment marker.
The sole active latest marker remains the preserved v14-review marker version
v12 with count 13 for v1--v11 plus v13 and v14; amendment v12 remains
absent/skipped.

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no research-wide theorem/evidence collapse found |
| Major (`M`) | 5 | target occupant destruction; ledger nonclosure; serial grammar ambiguity; pidfd identity overclaim; missing holder happens-before |
| Minor (`m`) | 1 | reversed P/G parent-child explanation |

```text
CLOSURE_REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v15.0
CLOSURE_APPEND_ONLY=true
THIS_APPEND_IS_SOLE_WRITE=true
PRESERVED_PREFIX_LINES=6431
PRESERVED_PREFIX_BYTES=346453
PRESERVED_PREFIX_SHA256=2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19
REVIEWED_REMEDIATION_GATE_V15_SHA256=c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a
REVIEWED_AMENDMENT_V15_SHA256=158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
FRESH_FULL_READ_COMPLETE=true
AUTHORITY_BINDING_MISMATCHES=0
PROJECT_CODE_IMPORT_OR_EXECUTION_PERFORMED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_PERFORMED=false
PLATFORM_OR_RUNTIME_PROBE_PERFORMED=false
EXTERNAL_PRIMARY_SOURCE_STATIC_READ=true

CRITICAL_FINDINGS=0
MAJOR_FINDINGS=5
MINOR_FINDINGS=1
OVERALL_CLOSURE_VERDICT=REVISE_C0_M5_m1
P15R_V15_M1_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY
P15R_V15_M2_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY
P15R_V15_M3_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY
P15R_V15_M4_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY
P15R_V15_M5_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY
P15R_V15_m1_STATUS=OPEN_REQUIRES_SUCCESSOR_REMEDIATION_AUTHORITY

V15_EFFECTIVE=false
EFFECTIVE_AMENDMENT_COUNT=13
EFFECTIVE_AMENDMENTS=v1-v11-plus-v13-plus-v14
CANDIDATE_V13_EFFECTIVE_MARKER_APPENDED=false
AMENDMENT_V12_PRESENT=false
AMENDMENT_V12_SKIPPED=true
V15_NEW_WIRE_FORM_COUNT=0

ATTEMPT3_IMPLEMENTATION_REVIEW_VERDICT=REVISE_C0_M12_m0
CONTROLLING_IMPLEMENTATION_GATE_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
IMPLEMENTATION_GATE_V5_REMAINS_CONTROLLING=true
ATTEMPT4_UNCONSUMED=true
ATTEMPT4_SUSPENDED=true
ATTEMPT4_AVAILABLE=false
ALL_ATTEMPT3_IMPLEMENTATION_FINDINGS_STATUS=OPEN

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false
SOURCE_USED_AS_DESIGN_AUTHORITY=false
HISTORICAL_IMPLEMENTATION_AUTHORITY_REVIVED=false
SUCCESSOR_DESIGN_REMEDIATION_AUTHORITY_REQUIRED=true
CONTROL_SOURCE_EDIT_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
CONTROL_OR_REPRODUCTION_EXECUTION_AUTHORIZED=false
PLATFORM_PRECHECK_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
PROOF_MODIFICATION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_OR_ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final adjudication on the exact
`base + v1--v11 + v13 + v14 + candidate v15` tuple is **REVISE — C0/M5/m1**.
V15 correctly chooses a persistent G pidfd, a validation-only procdir, a
P_CRASH guard, and Linux-5.15 poll semantics without changing the public wire
or classifier arithmetic. It does not close destination ownership before
destructive remap, cannot represent its promised all-reference ledger, does
not uniquely bind transaction and per-reference serials, overstates singleton
anon-inode fstat as exact pidfd identity, and lacks the happens-before edges
needed for its global P--L--G holder matrix. The bounded parent/child rationale
is also reversed. Therefore the zero-finding acceptance condition is unmet,
v15 is not effective, the implementation v5 STOP remains controlling,
ATTEMPT_4 remains unconsumed but unavailable, and no implementation or source
work is authorized. A separately authorized, frozen successor design must
satisfy every minimum repair obligation above and receive another full
independent zero-finding review. The final post-append path/line/byte/SHA-256,
new-append digest, and preserved-prefix reauthentication are issued externally
after this sole append because this file cannot contain its own final digest
without changing that digest.
