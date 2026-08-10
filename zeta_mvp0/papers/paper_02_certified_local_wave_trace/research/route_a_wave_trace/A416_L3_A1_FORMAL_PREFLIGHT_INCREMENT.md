# A4.16 L3-A1 formal control-plane preflight increment

Date: 2026-08-10 (UTC)

Protocol family: `R401-VAL-L3-A1`

Authority: **implementation candidate / non-licensing / no dispatch / no
canonical publication**

## Outcome

The formal preflight and control-plane implementation received the following
independent engineering verdict on its stable bytes:

```text
formal_control_plane_implementation_review = ACCEPT
P0 = 0
P1 = 0
P2 = 0
scientific_licensing_enabled = false
production_authorized = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

This verdict closes the current implementation increment only.  It is not an
independent pre-freeze scientific review, does not finalize the prospective
machine/main freeze schemas, and grants no evaluator authority.  No
representative, held-out, or all-slab scientific evaluator was dispatched by
the formal preflight.

## Implemented control-plane surfaces

### Same-byte 53-role handshake

The scheduler captures the exact ordered 53-role candidate table as pinned
raw bytes, SHA-256 values, lexical paths, and inode/stat identities.  It then
checks the provisional machine and main semantic envelopes, requires the main
object to reproduce the complete ordered role list, and replays every role and
the main object before returning an immutable snapshot.

The machine/main validators deliberately recognize only the currently
unambiguous subset of the prospective contracts.  Their output is labelled a
non-authorizing implementation snapshot; unknown fields acquire no authority.
The exact production schemas remain a required next-stage deliverable.

### Temporary initialize-only publication

Given a disposable authority fixture and an explicit output outside the
repository and all canonical result namespaces, initialize-only constructs one
`FORMAL_PREFLIGHT_RUN_CONFIG_CANDIDATE`.  It is visibly:

- `preflight_only = true`;
- `promotable = false`;
- `production_authorized = false`;
- `scientific_licensing_enabled = false`; and
- null at component, milestone, theorem, and final status.

Publication writes canonical-JSON bytes as `run_config.json` inside a
same-filesystem temporary directory, flushes the file and directory, uses atomic
`renameat2(RENAME_NOREPLACE)`, verifies the published directory inode, and
flushes the parent.  Injected failures before publication leave neither the
output nor a staging directory.  A successful candidate cannot be resumed or
promoted, creates no operational sibling, and is not the future canonical
production run config.

### Pure formal transaction plans

The static builder produces, but cannot execute, an exact 26-string evaluator
argument vector.  Its semantic hash substitutes only the staging proof path,
and its validation re-hashes the frozen evaluator before reaching the locked
dispatch surface.

The branch builder revalidates the frozen runtime, source, persistent-binary
role, L1 plan, and accepted L1 summary before lazy-loading the runtime and
constructing the exact cell task.  In tests this uses only a disposable fixture
binary.  The canonical persistent A1 binary does not exist.

Both dispatch functions validate their pure plan and then unconditionally
reject.  Injected executor and transaction-runner callbacks are never called.
The component aggregate helpers are likewise pure, non-publishable schema
candidates and require the exact 102-cell order and exact per-cell manifest
paths.

## Test and independent review evidence

| Evidence | Result | Scope boundary |
|---|---:|---|
| formal scheduler focused suite | 79/79 pass | formal preflight plus existing mock scheduler tests |
| owned L3-A1 implementation suite | 194/194 pass | implementation surfaces only |
| complete Paper 02 regression | 710/710 pass | no scientific dispatch |
| independent adversarial review | ACCEPT; P0=0, P1=0, P2=0 | control plane only |

The adversarial review covered ordered raw-byte replay, verdict-token and
entity smuggling, strict JSON types, lexical paths, links, same-byte inode
replacement, mutable-snapshot attempts, L1 mutation after capture, atomic
failure cleanup, lazy runtime ordering, static evaluator re-hashing, exact
aggregate paths, and proof that neither dispatcher calls its supplied runner.

Stable implementation hashes:

| Object | SHA-256 |
|---|---|
| scheduler | `e39caaed78468be1dc7791efde5b85f97668e07ef7117a7c2560decfea7d06bf` |
| scheduler tests | `41655000a7904547f80aadf1726c01f1392239c1e1dea94394df6931e41ad508` |

## Formal-source peak-RSS calibration on public S0 inputs

A separately authorized resource calibration ran the six already-public S0
branch inputs only, using a temporary binary compiled from the formal A1
source.  It did not select, inspect, or dispatch a held-out or all-slab cell.
The exact bindings were:

| Binding | Exact value |
|---|---|
| `validated/capd_r401_phase_branch_tube_mp_a1.cpp` SHA-256 | `66588bf25ae777c854f60a747af4299e3166efdd51db2659e33a28194abc59c5` |
| temporary calibration binary SHA-256 | `25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521` |
| CAPD commit | `731079217a9254ea2948d742df2b170895effe7f` |
| `capd-config` SHA-256 | `c758bc9101beb9c633817b0402df9168c6dea9f652d36833101af3273c50338a` |
| ordered compiler/link flags SHA-256 | `f55b78c25c899b2a8040719240dc309e58f65f99468479e47260acb1cc4315de` |
| `libcapd.a` SHA-256 | `970088d4ba5024c1b59124299d5e46df41f19936ba53446a5a40a0671968b086` |
| `libfilib.a` SHA-256 | `51c40a22a2405faec793d97a0396022212d7a32f4cca4bf38b994adacaf9be85` |
| temporary calibration JSON SHA-256 | `2cd389315867cff7598c2977543a8e1f3d0a3dc60d99b51f1e7826f9f95af99a` |

The worst observed peak RSS was `202428 KiB`.  The conservative six-worker
candidate admission calculation is

```text
baseline 14505582592
+ 6 * peak_rss 207286272
+ reserve 8589934592
= 24339234816 < 51539607552 bytes
headroom = 27200372736 bytes
```

This supports a candidate six-worker resource setting only.  It neither
freezes that setting nor adds scientific evidence to the representative S0
archive.  The calibration binary was not installed, and the calibration JSON
was retained only as a temporary byte image; no canonical calibration object
exists.

## Exact absence boundary

At completion of this increment, all of the following canonical objects are
absent:

- `research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json`;
- `research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json`;
- `research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json`;
- `validated/bin/capd_r401_phase_branch_tube_mp_a1`;
- `results/r401_val_l3_all_slabs/`; and
- `results/r401_val_l3_all_slabs.operational/`.

No canonical run config, cell, aggregate, checker, postcheck, report, or
release object was created.

## Remaining gate and next authorized work

The next engineering stage is to freeze the exact machine/main, run-config,
formal cell/manifest, aggregate, checker, postcheck, report, and release
schemas in the prospective contracts; build and hash the persistent A1 CAPD
binary; and construct the exact non-dispatching machine record.  Only after
those artifacts, the canonical S0 compatibility replay, complete pre-freeze
tests, and a separate independent pre-freeze review may the main freeze be
considered.

Until then, canonical initialize-only and every scientific dispatch remain
prohibited.  This increment asserts no A4.16 theorem, global tube routing,
trace formula, Hilbert--Polya operator, zeta-zero reconstruction, or RH
conclusion.
