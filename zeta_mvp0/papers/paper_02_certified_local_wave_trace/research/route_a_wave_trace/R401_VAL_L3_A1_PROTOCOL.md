# R401-VAL-L3-A1 all-slab local phase-tube protocol candidate

Protocol identifier: `R401-VAL-L3-A1`

Protocol version: 1 candidate

Prepared: 2026-08-09 UTC

Status: **PROSPECTIVE_NON_LICENSING / REJECT_FOR_DISPATCH**

## 1. Purpose and licensed target after a future freeze

This protocol candidate extends the accepted six-cell A4.16 implementation
smoke to the exact 51-slab parameter cover at two independent precisions.  It
specifies a future computer-assisted theorem, but it is not a freeze and does
not authorize an evaluator invocation.

For fixed epsilon, let

```text
C_tube(epsilon) = {
  (z,T): K_epsilon(z)=1, T in [0.64,0.69], Phi_epsilon^T(z)=z,
         sup_{0<=t<=T} r_minus(Phi_epsilon^t(z)) < 0.06
}.
```

Time translation acts by `s.(z,T)=(Phi_epsilon^s(z),T)`.  After a passing
future frozen run, the intended local conclusion is

```text
C_tube(epsilon) / R = {[(z_epsilon,T_epsilon)]},
```

where the right side is the already accepted A4.12--A4.15 fast branch.  The
same future archive must also prove that this distinguished branch satisfies
`r_minus < 0.04` over its complete period.

The premise that an arbitrary candidate remains in `r_minus < 0.06` for its
whole period is part of the theorem domain.  This protocol does not prove
that premise for a global candidate.

## 2. Exact matrix

The canonical slab sequence is exactly

```text
S000, S001, S002, S003, S004, S005, S006, S007, S008, S009,
S010, S011, S012, S013, S014, S015, S016, S017, S018, S019,
S020, S021, S022, S023, S024, S025, S026, S027, S028, S029,
S030, S031, S032, S033, S034, S035, S036, S037, S038, S039,
S040, S041, S042, S043, S044, S045, S046, S047, S048, S049,
S050.
```

The exact production order is

```text
128 bits x the canonical slab sequence,
then
256 bits x the canonical slab sequence.
```

There are exactly 102 composite cells.  Each composite cell contains one
static component and one branch component, for 204 component evaluations.
The exact epsilon interval and accepted primary root box of every slab are
read from `R401_VAL_L1_FINAL_PLAN_V2.json` and rebound through the accepted L1
five-object release chain.  No command-line subset, reordered matrix,
replacement box, or third precision belongs to this protocol.

The canonical matrix digest is computed from the strict canonical JSON array
of the 102 `{precision_bits, slab_id}` objects.  Its value is deliberately
`PENDING_MAIN_FREEZE_COMPUTATION`; this candidate does not invent a freeze
hash.

## 3. Inherited authority

The future main freeze must bind and independently replay:

1. the exact L1 final plan and accepted L1 summary, manifest, checker,
   postcheck, and release provenance;
2. the accepted A4.15 aggregate summary, aggregate manifest, independent
   checker, postcheck, and release provenance;
3. the A4.16 phase-flowbox derivation;
4. the sealed S0 static, branch, and composite controls; and
5. the exact read-only S0-to-A1 compatibility object.

The L1 chain supplies the distinguished primary boxes.  A4.15 supplies
existence and uniqueness of the positive-turning reduced root in the local
box.  L3-A1 supplies only the phase-anchor and complete-period branch-tube
bridges described below.

The prospective provenance DAG has exactly 53 ordered main-freeze input
roles and 68 ordered release roles: those 53 inputs, the downstream role-54
main freeze generated only after all 53 input bytes are final, and 14
downstream result/control roles.  Role 10 among the 53 inputs is the machine
freeze; the main freeze is not itself one of those inputs.  The exhaustive
path map is owned by
`R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md`.  In particular, the
implementation-design review, static evaluator test, branch runtime, and
S0-compatibility test are direct inputs rather than unbound helpers.  These
candidate counts create neither a main freeze nor dispatch authority.

## 4. Exact model and local domains

The evaluator and every scientific checker reconstruct outward from

```text
a = 51/50,
c = 2*(sqrt(1+a)-1),
```

the algebraic orthogonal normal basis and
`omega_plus/minus = 2*pi*sqrt(lambda_plus/minus)`.  Rounded eigenvectors are
display values only.

With `q=OQ`, `p=OP`,

```text
W_epsilon(q) = (-c*q1-q2-a*epsilon*q1^2, q1),
R = |W_epsilon(q)|^2,
K_epsilon = (P_minus^2+P_plus^2)/2
            + 2*pi^2*R*exprel(pi*epsilon^2*R).
```

The static angle root is the exact product

```text
E_j x [-0.015,0.015] x [-0.18,0.18]
    x [-0.06,0.06] x [-1.415,1.415]
```

in `(epsilon,Q_minus,Q_plus,P_minus,P_plus)`.  The section root is

```text
E_j x [-0.015,0.015] x [0,0.18] x [-0.06,0.06]
```

at `P_plus=0`.  `E_j` is carried unchanged; only state coordinates are split.

## 5. Static component

Each static cell contains exactly four canonical trees in this order:

```text
ANGLE, SECTION_LOW, SECTION_HIGH, SECTION_WINDOW.
```

The outer gates prove

```text
r_minus <= 0.06 => |Q_minus| < 0.015 and |P_minus| <= 0.06,
K=1 => |P_plus| < 1.415,
K=1 and epsilon in [0,0.101] => |Q_plus| < 0.18.
```

On the angle tree, define

```text
D_plus = omega_plus^2*Q_plus^2 + P_plus^2,
N_plus = P_plus^2 + Q_plus*K_Q_plus,
theta_dot = omega_plus*N_plus/D_plus.
```

Every non-excluded terminal leaf must prove

```text
D_plus > 0, N_plus > 0, theta_dot < 18.
```

The checker separately proves `18*0.69 < 4*pi`.  Positivity, periodicity, and
the strict total-angle ceiling give winding one and exactly one positive
oriented crossing `P_plus=0, Q_plus>0`.

The section trees must exclude the forbidden closed shells and retain only

```text
0.12 < Q_plus < 0.17,
|Q_minus| < 0.02,
|P_minus| < 0.08.
```

The terminal classifications are exactly `ENERGY_EXCLUDED`,
`TUBE_EXCLUDED`, `ANGLE_CERTIFIED`, and `LANDING_CLOSED_WINDOW`, with
`UNRESOLVED` reserved for a non-pass.  A box that merely permits a bad gate
does not prove existence of a constrained counterexample and may not receive
a violation status.

## 6. Branch component

For each matrix cell, the exact accepted L1 primary box
`(Q_minus,Q_plus,P_minus,T)` is embedded at `P_plus=0`.  Epsilon and `T` are
constant interval state variables and normalized time satisfies

```text
dZ/ds = T*X_K_epsilon(Z), 0 <= s <= 1.
```

The future persistent CAPD multiprecision binary must use
`SolutionCurve`, Taylor order 24, and the exact 64 closed phase cells
`[k/64,(k+1)/64]`, `k=0,...,63`.  The precision-dependent absolute and
relative tolerances are exactly `1e-30` at 128 bits and `1e-60` at 256 bits.

Every phase cell must prove

```text
(omega_minus*Q_minus)^2 + P_minus^2 < 0.0016.
```

Failure of an upper enclosure to prove the inequality is unresolved.  A
scientific violation may be declared only if a validated phase enclosure has
a lower slow-radius bound at or above `0.0016`.

## 7. Cross-precision contract

For each slab, the 128- and 256-bit cells must bind the same exact rational
epsilon interval, the same exact static roots, and the same exact L1 primary
root domain before any outward serialization.  The printed CAPD and Arb
enclosures may differ by precision.

Both precisions must reach the same final component verdict.  Cross-precision
agreement does not require identical tree topology, node count, CAPD piece
count, outward endpoints, proof bytes, or content hashes.  It requires:

- identical exact input-domain identity;
- complete no-gap component proofs at both precisions;
- the same passing component status; and
- no unresolved, resource, malformed, provenance, or scientific-stop result.

One precision cannot repair or substitute for the other.

## 8. Exact control-plane limits, not yet a production freeze

The following values are exact in the implemented schema.  They do not gain
production authority until accepted machine/main freezes bind the same values:

| item | candidate |
|---|---:|
| static maximum depth per tree | 24 |
| static maximum nodes per tree | 250,000 |
| static maximum nodes per cell | 1,000,000 |
| static cell timeout | 1,800 s |
| static workers | 8 |
| static maximum cell bytes | 512 MiB |
| branch phase cells | 64 |
| branch Taylor order | 24 |
| branch cell timeout | 600 s |
| branch workers | 6 |
| branch stdout / stderr cap | 16 MiB / 1 MiB |
| branch record / total-cell cap | 4 MiB / 32 MiB |
| memory admission pause | 48 GiB cgroup current usage |
| launch free storage | 200 GiB |
| storage warning / pause / recovery-only | 180 / 150 / 120 GiB |
| global scientific budget | `null` |

Any depth, node, byte, timeout, flow, memory, or storage limit is
inconclusive.  Operational memory or disk pause leaves a resumable incomplete
generation and cannot assign a scientific failure.

## 9. Authority and three-checker chain

All evaluators, schedulers, cell records, manifests, aggregates, and composite
producer objects retain

```text
milestone_status = null
theorem_status = null
final_status = null
scientific_licensing_enabled = false.
```

The independent static checker may place
`PASS_STATIC_PHASE_ANCHOR_ALL_SLABS` only in `component_status`.  The
independent branch checker may place `PASS_BRANCH_TUBE_ALL_SLABS` only in
`component_status`.  Their milestone, theorem, and final fields remain null.
Each component checker is followed by its own write-once postcheck.

Only the independently frozen composite checker may set

```text
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status = null.
```

It requires both component checker/postcheck chains over all 102 cells and is
itself followed by a third write-once postcheck.  A producer, packager,
postcheck, report writer, or release builder cannot create or widen this
value.

## 10. Acceptance gate

A future composite pass requires all of the following:

1. exact main-freeze, machine-freeze, run-config, matrix, and immutable-input
   handshakes;
2. 102 static cell manifests and 102 branch cell manifests, with no missing,
   extra, aliased, or symlinked object;
3. zero unresolved, timeout, signal, byte-cap, flow, malformed, invalid, or
   scientific-stop component cell;
4. exact independent scientific replay of every static proof and every
   branch transcript;
5. exact 128/256 input-domain and final-verdict agreement for all 51 slabs;
6. passing static and branch checker/postcheck chains;
7. exact L1, A4.15, S0 compatibility, and acyclic provenance bindings; and
8. a passing independent composite checker and final postcheck.

A passing subset has no all-slab status.

## 11. Explicit nonclaims

Even a future `PASS_LOCAL_PHASE_TUBE_ALL_SLABS` is conditional on complete
tube residence for arbitrary candidates.  It does not prove:

- routing of every energy-shell candidate into the tube;
- full-energy-shell or global phase-space uniqueness;
- a global parameter theorem outside the exact 51 slabs;
- an event-projected determinant or new `delta_tr` bound;
- a trace formula, prime-orbit theorem, Hilbert--Polya operator,
  zeta-zero reconstruction, RH, or an implication toward RH.

These boundaries apply to JSON, reports, README files, figures, abstracts,
and manuscripts.

## 12. Current dispatch decision

```text
protocol_status = PROSPECTIVE_NON_LICENSING
machine_capture_temp_only_implemented = true
machine_verify_only_implemented = true
machine_freeze_exists = false
main_freeze_exists = false
independent_prefreeze_accept = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

No evaluator command is licensed by this protocol candidate.

## 13. Exact-schema and serializer boundary

The prospective main freeze uses a closed schema and an ordered 53-element
`input_roles` array of exact `{role,path,sha256}` objects.  The run config is
downstream of the raw main-freeze hash, repeats that ordered array and all
frozen policy objects, and has producer-only authority with
`dispatch_authorized_by_artifact=false`.  No object contains its own hash.

`CJ_COMPACT_V1` applies to the machine/main/run-config, static proof/record/
manifest, and aggregate domains.  Branch task, argv, record, and manifest
hashes retain `CJ_PRETTY_2_V1`.  The machine freeze stores the original static
compact and branch pretty calibration byte images as UTF-8 strings and hashes
those raw strings before strict parsing and semantic replay.

Every static authoritative cell has exactly four files:
`proof.json`, `stdout.txt`, `stderr.txt`, and `record.json`.  Truly absent
proof bytes are represented by the closed compact `STATIC_PROOF_ABSENT`
sentinel; malformed bytes are retained as raw bytes.  The manifest binds all
four files, while the record binds proof/stdout/stderr.  All bindings are
exact `{path,sha256,size_bytes,serializer,truncated}` objects.

Machine admission binds three pairwise-distinct Python identity roots.  The
Conda root uses `CONDA_META_LIVE_FILES_CJ_COMPACT_V1` plus an exact file
count and terminal live replay.  CAPD uses
`GIT_INDEX_LIVE_TREE_CJ_COMPACT_V1`: its checksum-covered v2 index must
reconstruct the authenticated detached-HEAD Git tree, while `tree_sha256`
separately hashes the live ordered tracked-byte rows.  The persistent branch
ELF binds its one 20-byte GNU build-id, exact sorted `DT_NEEDED`, and absence
of `DT_SONAME`; python-flint module/`RECORD`/Arb/fmpq paths share one exact
site-packages root.

The compiler binding is not one ambiguous build record.  It separates a
declarative `build_recipe`, an executed `fresh_rebuild_receipt` for a private
direct-child `/tmp` output, and `transfer_evidence` proving byte equality with
the persistent role-17 binary without overwriting or changing that binary's
identity.  The recipe uses `@STAGING_BINARY@` instead of a canonical target.
Role 19 alone owns the fresh build and records `shell_used=false`; the role-24
independent verifier performs no write and spawns no subprocess.  The current
capture and verify-only CLIs operate only on a temporary candidate and grant
no role-10 publication, role-54 construction, production authorization, or
scientific status.

The exact static timeout is `1800000` ms.  Exact branch timeout and grace
fields are `600000`, `2000`, and `1000` ms.  The formal branch runtime and
independent checker now preserve those exact integer fields, so
`branch_millisecond_migration_complete=true`.  This representation gate is
not execution authority: all production/scientific execution remains
unconditionally rejected pending the accepted freeze chain and a separate
execution decision.
