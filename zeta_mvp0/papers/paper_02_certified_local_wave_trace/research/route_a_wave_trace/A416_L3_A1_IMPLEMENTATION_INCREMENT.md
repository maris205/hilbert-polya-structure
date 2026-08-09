# A4.16 L3-A1 formal implementation increment

Date: 2026-08-09 (UTC)

Protocol family: `R401-VAL-L3-A1`

Authority: **engineering implementation evidence / non-licensing / no dispatch**

## Outcome and authority

This increment turns the accepted representative A4.16 smoke into the first
formal all-slab engineering candidates.  It implements and adversarially
tests:

1. a one-cell static phase-anchor evaluator;
2. a 102-cell static mock transaction and aggregate path;
3. a no-import static proof-replay core;
4. a formal CAPD branch-tube source and a hardened one-cell transaction
   runtime; and
5. a read-only S0-to-A1 compatibility adapter.

Independent reviews accepted the static increment and the branch transaction
runtime with

```text
static_review = ACCEPT_FOR_IMPLEMENTATION_INCREMENT
static_P0 = 0
static_P1 = 0
branch_review = ACCEPT
branch_P0 = 0
branch_P1 = 0
scientific_licensing_enabled = false
accept_for_freeze = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

This is not an `ACCEPT_FOR_FREEZE` record.  No representative, held-out, or
all-slab scientific evaluator was run in this increment.

## Implemented surfaces

### Prospective contract set

Four separate prospective contracts now specify the formal protocol,
scheduler transactions, independent checker hierarchy, and release
provenance.  They remain
`PROSPECTIVE_NON_LICENSING / REJECT_FOR_DISPATCH`.  Their candidate DAG has
exactly 53 main-freeze input roles and 68 release roles.

### Static phase-anchor chain

The static evaluator uses the exact four-tree order

```text
ANGLE, SECTION_LOW, SECTION_HIGH, SECTION_WINDOW
```

and binds its slab semantics and final-plan digest to one pinned byte image.
It enforces separate depth, per-tree node, and per-cell node budgets; emits no
wall-clock telemetry in the canonical proof; uses closed evaluator statuses;
and writes the proof once.

The transaction scheduler implements an exact 51-slab by two-precision mock
matrix, manifest-last no-replace commits, resume, retained-staging rejection,
whole-generation quarantine with a durable intent journal, exact namespace
scans, and deterministic aggregate construction.  Its production dispatch
path remains unconditionally fail-closed.

The no-import checker independently reconstructs the interval model and
dyadic tree decisions, replays upstream L1 authority, checks frozen resource
caps, and rejects path, link, type-alias, duplicate-key, nonfinite, and
same-byte provenance mutations.  Its full aggregate entry point remains
fail-closed until the component checker and postcheck are implemented.

### Branch-tube transaction chain

The formal C++ candidate preserves the sealed multiprecision CAPD
`SolutionCurve` branch-tube ABI.  A separate Python transaction runtime now
implements:

- the exact 12-string evaluator argument vector and pinned executable inode;
- bounded 16/1/4/32 MiB stdout, stderr, record, and total-cell budgets;
- timeout, TERM/KILL, process-group, and adopted-descendant cleanup;
- cleanup when the scheduler itself receives `BaseException`, SIGINT, or
  SIGTERM;
- exact current-generation live/interrupted lock and staging ownership;
- atomic no-replace lock and cell publication with same-byte replay;
- caller-visible lock/guard ownership handoff across asynchronous signals;
- replacement-resistant namespace guards and inode revalidation;
- interruptible nonblocking lock contention with a 30-second fail-closed
  operational deadline; and
- manifest-less committed-cell recovery under exact frozen budgets.

The fixed CAPD checkout compiled and linked this source with
`-Wall -Wextra -Wpedantic -Werror`.  The resulting temporary binary was not
executed and was not installed as a persistent production binary.

### S0 compatibility adapter

The adapter replays the sealed representative inventory without modifying it:
six static proof entries, 26 branch manifest roles, 18 composite bindings,
and nine control hashes.  Its canonical A1 compatibility object is
intentionally absent; the replay was performed only in a temporary output.

## Test and review evidence

| Surface | Result | Boundary |
|---|---:|---|
| Static evaluator/checker/scheduler focused suite | 102/102 pass | mock and proof-core only |
| Branch transaction focused suite | 74/74 pass | mock/adversarial runtime only |
| S0 compatibility focused suite | 31/31 pass | read-only accepted S0 archive |
| Combined new L3-A1 focused suite | 207/207 pass | no scientific evaluator |
| Paper 02 complete pytest suite | 602/602 pass | repository regression |
| Branch plus S0/phase-contract combined replay | 133/133 pass | reported by independent branch review |
| CAPD compile/link | pass with warnings as errors | compile/link only; binary not run |

The branch review repeatedly injected failures into signal delivery, process
spawn, pipe setup, lock publication, namespace replacement, guard contention,
staging recovery, and descriptor handoff.  The final independent audit found
no P0 or P1 defect in the implemented one-cell transaction surface.

## Stable source provenance

| Object | SHA-256 |
|---|---|
| Prospective protocol | `88fb0b95762ca80ca2a62a0ce63ae91b927424b1490ec0e7ce8364741b8d4c46` |
| Prospective scheduler contract | `d8bd275a177d5f94c57ea7714d2f2bf30d3dca0f64d702f8be0a4c3e8c5ddb47` |
| Prospective checker contract | `dd8e4ed7e167b789484dda29d6664ac0110faf39b186636754a71688d7eef89d` |
| Prospective release contract | `3599cf9d43bf0ed444c844034715a5520dfd40b8dff1b7358ff9c40f323abb44` |
| Static evaluator | `88a99db70f105dec9fbc0a838b0a3e3faace5851b4ac0be17a7015b38b0c7fc3` |
| Static independent checker | `9c214e8ab6be7609d51861b5ae4f7e3ebe6b2d716c5d7d8f6853f6c64b716e02` |
| Static mock scheduler | `76cca1f45ef4ca55f3233dbb5a4d756f106388db550293e078a305b86a6dfcb3` |
| Branch transaction runtime | `a865078bce2fc1e14fd9dbc15f75a029a2c8bbcf843743fc93d2d9d54933989a` |
| S0 compatibility adapter | `f477ea1210aba36ceda6752bd0ce66db4833135aa8f127586fe7847a37409b3c` |
| Static evaluator tests | `4e10e06985934da8a7855965c2c548a542fcb686ba2c051f26d37235dcffd5fd` |
| Static checker tests | `d0a0e52c83d4729f6c0d387dce1b51bd4b1f39a23f70a17662be2a3c1ab1d167` |
| Static scheduler tests | `5c54ab427b3c9308c5d7a489f88faddf866a431b6c5e923d797538f6850ee608` |
| Branch transaction tests | `0f8d84068784ee47d2170830e3ac222e1477d6c35f314201a4af827a0b203e95` |
| S0 compatibility tests | `4440acc3e6d2abfc4abf9aff18d41f22b9a642b628e36e5dc648007d03844e0d` |
| Formal CAPD branch source | `66588bf25ae777c854f60a747af4299e3166efdd51db2659e33a28194abc59c5` |
| Temporary S0 compatibility replay bytes | `87ca73ca31245d84fd47c6765b206f878edbfd4f560c4a1cfaecccf5f15ddd14` |

## Incomplete production chain

The following remain absent and are required before any freeze review:

- the static 102-cell aggregate checker and static postcheck;
- the 102-cell branch scheduler and aggregate;
- the branch independent checker and branch postcheck;
- the composite checker and composite postcheck;
- the release-provenance builder and verify-only path;
- a complete 102-static plus 102-branch mocked E2E and release fault suite;
- a persistent CAPD binary and exact Python/Arb/CAPD machine binding;
- representative peak-RSS calibration;
- the L3 machine freeze, pre-freeze tests, independent formal pre-freeze
  review, and main freeze.

The canonical compatibility replay, production result root, operational
root, machine freeze, main freeze, and formal pre-freeze review are all
absent at this milestone.

## Mathematical and programme boundary

No A4.16 scientific theorem is asserted here.  The intended later theorem
remains conditional: candidates whose complete periodic trajectories remain
inside the slow tube are to be phase-anchored into the A4.15 local reduced
root box, while the accepted branch is separately enclosed in a smaller
tube.  This increment validates engineering surfaces, not the remaining 51
slabs and not arbitrary-candidate global tube routing.

It supplies no global orbit cover, trace formula, Hilbert--Polya operator,
zeta-zero reconstruction, RH proof, or implication toward RH.

## Next authorized action

The next authorized engineering step is to implement and mock-test the two
component aggregates, independent checkers, and write-once postchecks, then
close the composite and release paths.  Only after that mock chain, runtime
calibration, machine record, and an independent formal pre-freeze review may
a main freeze be considered.  Scientific dispatch remains prohibited until
that separate gate is explicitly accepted.
