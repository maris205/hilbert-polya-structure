# A4.16 L3-A1 machine-binding and formal-schema engineering increment

Date: 2026-08-10 (UTC)

Protocol family: `R401-VAL-L3-A1`

Authority: **NON_LICENSING / engineering implementation candidate / no
machine freeze / no main freeze / no scientific dispatch / no canonical
results**

## Outcome

The exact-schema, machine-validation, serializer, and persistent-binary
engineering surface received the following independent cross-review verdict
on the current candidate bytes:

```text
machine_binding_and_formal_schema_review = ACCEPT
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

This closes an engineering increment only.  `ACCEPT` is not
`ACCEPT_FOR_FREEZE`, does not create either freeze, does not authorize an
initialize-only production run config, and does not authorize representative,
held-out, or all-slab scientific dispatch.

## Exact formal-schema and machine-validation surface

The scheduler now implements closed exact schemas for the prospective machine
record, main freeze, final run config, formal static and branch cell surfaces,
102-cell component aggregates, independent checker/postcheck objects, and
release provenance.  The ordered 53-role same-byte handshake remains the
authority entry boundary.  Every formal production execution path remains
fail-closed because the canonical machine freeze, accepted pre-freeze review,
and main freeze do not exist.

The prospective machine object has exact authority
`MACHINE_ADMISSION_ONLY`.  Its required state is
`scientific_licensing_enabled=true` only as a machine-admission capability,
`production_authorized=false`, and null component, milestone, theorem, and
final statuses.  It does not itself authorize production or assign a
scientific result.  Independent validation
recomputes and cross-binds:

- the capture-tool, boot, CPU, cgroup-memory, filesystem, and storage facts;
- the Python executable and complete version string, the live Conda installed
  manifest, the raw `python-flint` RECORD, the installed `python-flint`
  manifest, Arb/FLINT extension images, and bundled runtime libraries;
- the CAPD checkout/commit/tree, cache, `capd-config`, raw ordered flags,
  `libcapd.a`, `libfilib.a`, compiler, deterministic build receipt, source,
  persistent ELF, build ID, direct `DT_NEEDED` set, and resolved runtime
  libraries; and
- embedded byte-exact public-only static and branch resource payloads, their
  ABI/whitelist checks, peak-RSS arithmetic, and the persistent-binary transfer
  binding.

The validator is no-import with respect to the producer implementation.  It
parses live ELF metadata itself and recomputes the documented live-manifest
roots instead of accepting copied digest strings.  These capabilities validate
a future candidate machine receipt; they have not generated one.

## Strict static and branch byte surfaces

The formal static cell surface is exactly four files:

```text
proof.json
stdout.txt
stderr.txt
record.json
```

The evaluator and independent checker enforce exact 26-string invocation
semantics, strict duplicate/nonfinite/type rejection, `CJ_COMPACT_V1` JSON,
closed evaluator/scheduler classifications, byte budgets, file bindings, and a
nonempty `STATIC_PROOF_ABSENT` sentinel whenever no evaluator proof exists.  A
nonpass cell is never component-eligible.

The branch runtime, branch checker, composite checker, scheduler schema, and
release replay now share millisecond fields exactly:

```text
timeout_ms = 600000
term_grace_ms = 2000
pipe_close_grace_ms = 1000
```

Conversion to seconds occurs only at the process-wait boundary.  Branch task,
argument, record, and manifest hashes use the strict sorted indent-2
`CJ_PRETTY_2_V1` byte image with one trailing LF; compact formal control and
aggregate objects use `CJ_COMPACT_V1`.  The branch checker independently
recomputes the pretty-byte invocation and task digests and binds them into the
manifest replay.

## Persistent CAPD binary

A deterministic clean rebuild reproduced the public-calibration binary and
installed the same bytes at
`validated/bin/capd_r401_phase_branch_tube_mp_a1` without replacing an existing
file.

| Binding | Exact value |
|---|---|
| formal C++ source SHA-256 | `66588bf25ae777c854f60a747af4299e3166efdd51db2659e33a28194abc59c5` |
| persistent binary SHA-256 | `25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521` |
| size | `2419064` bytes |
| mode | `0755` |
| GNU build ID | `3cff449e0a265fe63d1fa1d1350ea48f324ba386` |
| direct `DT_NEEDED` | `libc.so.6`, `libgcc_s.so.1`, `libm.so.6`, `libmpfr.so.6`, `libstdc++.so.6` |
| RPATH / RUNPATH | absent |

The fresh-build image, installed image, and binary named by the public branch
calibration all have the same SHA-256.  This is a byte-transfer binding, not a
machine freeze or scientific result.

## Public-only resource evidence

### Final static calibration

The final static calibration used only the already-public
`S000/S025/S050 x 128/256` matrix.  It ran six sequential cells and one
eight-worker stress schedule made only from those public cells, including the
documented `256/S025` and `256/S050` repeats.

| Binding | Exact value |
|---|---|
| temporary payload | `/tmp/a416-l3a1-static-rss-final.4CBiaA/static_calibration.json` |
| payload SHA-256 | `8afc8a0a0929da077a1a1ad19ddc0c19e754c49646c4b3d806f3f4cf5522de92` |
| payload size | `30030` bytes |
| serializer | `CJ_COMPACT_V1` |
| final evaluator SHA-256 | `23bc6672016b40abbaec378c7b3d2d09b202eb169f5724920d5d2553e95fbb1f` |
| completed runs | `14/14` return code zero, exact status line, empty stderr |
| ABI | exactly `26` strings per invocation |
| worst peak RSS | `58544 KiB = 59949056` bytes |

The exact eight-worker candidate calculation is

```text
idle baseline 24891273216
+ 8 * representative peak RSS 59949056
+ reserve 8589934592
= 33960800256 < 51539607552 bytes
headroom = 17578807296 bytes
```

The payload remains under `/tmp` until the deterministic canonical machine
receipt capture/builder exists.  It is not a repository result, freeze, run
config, or scientific certificate.

### Branch calibration and persistent-byte transfer

The existing branch resource payload likewise covers only the six public S0
cells.  Its byte image remains
`/tmp/a416-l3a1-rss.jzXoy2/calibration.json`, has size `7402` bytes, and has
SHA-256
`2cd389315867cff7598c2977543a8e1f3d0a3dc60d99b51f1e7826f9f95af99a`.
All `6/6` jobs returned zero with the exact 12-string ABI and empty stderr; the
worst peak RSS was `202428 KiB`.  Its `binary_sha256` is
`25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521`,
which is exactly the installed persistent binary SHA-256.  The original
indent-2 branch payload bytes are preserved for future embedding rather than
rewritten into compact JSON.

## Current byte ledger

### Contract bytes

| Object | SHA-256 |
|---|---|
| protocol | `4dc4830e61959ca8b3ee62f9fa0c6b2cb6eecb90642b178df133403aebd4ba60` |
| scheduler contract | `87279d8772257678a01974951ed8a44138f4491cb987ab3a0781e971bba842c2` |
| checker contract | `6147ce766d277308d8f5818cfb4cf86e85872b99fd76fbda23b01d551efc472a` |
| release-provenance contract | `1647fbf0cdb9fcd881028fdb032f90610779e26d04903709d560b3076cf23265` |
| pre-freeze design | `705d269c05ad4df39adb3ab149499a20d7032fe87c085eb846446304cf87e1d2` |

### Implementation source bytes

| Object | SHA-256 |
|---|---|
| formal scheduler | `f55c98b7b431aad022490f32ae0ae3039c0806557d0e3732dbc6633cb579aa6e` |
| static evaluator | `23bc6672016b40abbaec378c7b3d2d09b202eb169f5724920d5d2553e95fbb1f` |
| static checker | `9bb37583be4f778333e349262265baa2dbbfdace286bdec557f262104c92e427` |
| branch runtime | `e885ea0f8067cd5d0169e7c4bd34723edac6e7fd86929b17378464cd3073161e` |
| branch checker | `a8cb6755876fc58c5fa33d6ebacfbd9438fd3994e17ad7150aad32c3e4727e1c` |
| composite checker | `e2a8106bfe7423f9a37995b09edf0ca095ade1ce916c52fca67a23754d086f22` |
| release builder / independent machine validator | `a74b7d6673a517594a27f14ebe0d984d9cbd988c1e6b51fa5db06af0d69754b5` |

### Test source bytes

| Object | SHA-256 |
|---|---|
| static scheduler tests | `4931d0daf5a21f238fe31bb5de9d433f11ab4dade9fa7f8184dd86e12c49206e` |
| static evaluator tests | `0a8b1973a1863eec6249d36d5d869d8a1090d51dbb0d51d293489c2aa9fdc410` |
| static checker tests | `26130ed8feeb1b54ea23ee84d3af4de3959d931decbff704ae8c2bc26638e8b3` |
| branch scheduler tests | `7856c05fb520ddd8619a4f0f0221c8193843bc6e58eae9bd673594d354650f65` |
| branch checker tests | `7fc887c3a258d09eb56e8a4ffd7b99ceab5aa8ebaec2ea81c6ca46a9654e98d0` |
| composite checker tests | `63672e696d035124b8550a16c0c7a8e6677cf27421e5589bf0d8aba334137c8a` |
| release/machine-validator tests | `5291a4dc06de144aa2c03fbcd21b544c7ca4052e6132010ef8b8434b37dfd95f` |

## Verification scope

The core command immediately before the final embedded branch resource
binary-digest/persistent-binary binding passed `419/419` tests.  After that
binding and all documentation corrections, the complete latest-byte Paper 02
regression passed `814/814`.  Neither command dispatched a scientific
evaluator.

The independent machine-binding/formal-schema cross-review returned `ACCEPT`
with `P0=0`, `P1=0`, and `P2=0`.  Its scope was implementation correctness and
claim-boundary preservation, not scientific freeze authorization.

## Exact absence and claim boundary

At completion of this increment:

- no canonical `R401_VAL_L3_A1_MACHINE_FREEZE.json` exists;
- no canonical `R401_VAL_L3_A1_FREEZE.json` exists;
- no canonical S0 compatibility replay exists;
- no canonical production run config or operational generation exists;
- no canonical A4.16 all-slab result, checker, postcheck, report, or release
  exists; and
- no evaluator was dispatched under scientific authority; the only evaluator
  executions were the explicitly bounded public-S0 resource calibrations.

The persistent binary is an implementation input only.  The public-only
calibrations are resource telemetry only.  Neither assigns a component,
milestone, theorem, or final status.  This increment asserts no A4.16 all-slab
theorem, global tube routing, trace formula, Hilbert--Polya operator, zeta-zero
reconstruction, or RH conclusion.

## Next blocker

The next authorized engineering unit is a deterministic machine-freeze
capture/builder that embeds the final static and branch payload bytes and
recomputes every live environment, toolchain, ELF, resource, and filesystem
binding.  Its candidate output must then pass the producer-independent machine
verifier, the complete pre-freeze regression chain, and a separate independent
review whose sole authorizing line is exactly `Verdict: ACCEPT_FOR_FREEZE`.

Only after that chain may the main freeze be generated last.  Scientific
initialize-only and every representative, held-out, or all-slab dispatch remain
prohibited until separately authorized.
