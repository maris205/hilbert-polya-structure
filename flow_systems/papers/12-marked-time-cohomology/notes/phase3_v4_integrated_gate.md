# Paper 12 Phase-3 v4 integrated Route-authorization gate

Gate date: **2026-08-15 (Asia/Shanghai)**  
Decision: **PASS — C0/M0/m0; `STANDALONE_PASS`; exactly one eight-owner
Route-A evaluation authorized**

## 1. Scope

This gate closes the Paper-12 v4 proof, deterministic-control,
standalone/nonredundancy, and acyclic Route-provenance branches on their
stable exact bytes. It authorizes `P12-10` for the eight frozen Route-A
owners and no others.

It does not assign an A0--A4 verdict, create a Route result, authorize Route
B, or authorize composition, manuscript drafting, citation/declaration
clearance, release, or public synchronization.

## 2. Unchanged active tuple

The independently reviewed active content/status bytes remain unchanged:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` |

The historical `pipeline_state.md` Route row records the earlier pre-artifact
block. This downstream gate supersedes that row for `P12-10` authorization
only, without mutating the active tuple or invalidating the independently
audited controls manifest.

## 3. Design and source gates

| Artifact | SHA-256 | Final result |
|---|---|---|
| `notes/phase3_v4_methodology_relock.md` | `c31e1c6d6b21eb4d9de0c698fcbd10bbd2516a7e8a3e477eba591e88de7bfb81` | PASS C0/M0/m0 |
| `notes/phase3_v4_devils_advocate.md` | `9a9a87fa621b0d0434fb2f0ece635e45a4b721a2f65c238ef4ca441f69aea190` | PASS C0/M0/m0 |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | PASS C0/M0/m0; `SUPPORTED_WITHIN_SEARCH` |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` | PASS C0/M0/m0 |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | exact source ledger |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | 10/10 checksum closure |

No priority claim is authorized. `DIRECT_EXACT_PACKAGE_PRECEDENT_FOUND=false`
is only the dated bounded-search result.

## 4. Stable proof and control tuple

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | v2 actual-complex core remains valid |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | v2 packet/marked core remains valid |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | final v4 theorem |
| `notes/phase3_v4_math_review.md` | `97dbd63fae6d35ae627520203db98d7c497a927a505599c0855231ac3f3b4e07` | PASS C0/M0/m0 |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | 122 tests; 11 CSV/3486 rows; 14 negatives |
| `code/generate_controls.py` | `0aa35a649a676fdd9c747c3b3ff27f8b815aa1e3ff761315cfdf4ceba906fd99` | frozen generator |
| `code/test_controls.py` | `b9c234d8fa2b104f2358707bfbba5f7e59eaf3603715edff0714f70e9d14b76b` | frozen tests |
| `experiments/reproduce.sh` | `aec1371b249cc564d781980c1aae6fa3209c5ec2ec350962060783d947574090` | frozen entry point |
| `results/orbitwise_standardization_h1_controls.csv` | `54498a635f255472b7e7687049a25a23e394408f4adc4d43dc459c2b952943a6` | 3252 v4 rows |
| `notes/phase3_v4_controls_review.md` | `886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6` | PASS C0/M0/m0 |

The accepted control evidence is the controls auditor's single completed
top-level run and the frozen deterministic tuple. The separately disclosed
duplicate-run orchestration incident contributes no evidence and caused no
byte, process, temporary-directory, or cache residue.

## 5. Standalone and integrated reviews

| Artifact | SHA-256 | Final result |
|---|---|---|
| `notes/phase3_v4_standalone_review.md` | `639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895` | `STANDALONE_PASS`, C0/M0/m0 |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | pre-Route PASS C0/M0/m0 |
| `notes/phase3_peer_review.md` | `7d3ddb6d28d425695696965b73caeaa109f5a5cc27c1c52fd8fb826138818f36` | v4 integrated PASS C0/M0/m0 |

The former v2 routine-reduction Major is closed at the proved v4 strength.
The central nonredundant statement is the same-carrier topology comparison

```text
H_cnv^1(G_actual;R)=R[c]
  --J^*--> H_cnv^1(G_std;R)=R^Q,

image(J^*)=(R^Q)^(Aut_R(G_std))=the constant diagonal.
```

All registered stops remain binding: `R^Q` is the full algebraic product;
standardized coboundaries are generally nonzero; the automorphism extension
is canonical only before a choice-dependent split; `Q_p` is only a bare
nonempty orbit set; and the fixed-prime result is a packet corollary with
common stabilizer `(log p)Z` at every unit.

## 6. Acyclic Route provenance

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase3_v4_route_provenance_amendment.md` | `db1fe49108ab3697596847571bcdadbed1e6df251cc941b7d51b6c15780372a7` | upstream/output hash DAG |
| `notes/phase3_v4_route_provenance_relock.md` | `20c67ace45b81523400053b388923e4a01c725b0bfdd528f2c391803ded0cb4d` | PASS C0/M0/m0 |

The amendment supersedes only the impossible self/cross-hash requirement in
protocol Section 10 and candidate Section 6. It changes no active lock byte,
owner, verdict ceiling, control, or YAML schema.

Each Stage-12 YAML must bind hash-qualified stable upstream evidence through
the existing v0.2.0 fields. Its own path and `notes/route_audit.md` are
locator-only. After the eight YAML files stabilize, `route_audit.md` binds
their final hashes and the upstream tuple. Only downstream composition and
release artifacts bind the final Route-audit hash.

## 7. Exact Route authorization

One and only one Route-A evaluation is authorized for these eight candidate
IDs and exact paths:

1. `GEN-INDISC-R-ACTION-CNV`;
2. `DEN-EF-ACTUAL-ORBIT-CNV-P-A`;
3. `DEN-EF-ACTUAL-PACKET-CNV-P`;
4. `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A`;
5. `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P`;
6. `DEN-EF-STANDARD-PERIOD-QUOTIENT-P`;
7. `DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P`; and
8. `UNMARKED-PERIOD-SCALING-CONTROL`.

Each path is
`evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml`. The exact
candidate definition, family, phase space, dynamics, parameters, provenance,
clock, normalization, determinant convention, no-Git receipt, forbidden
data, and ceiling are those frozen in protocol Section 10 and candidate
Section 6.

The evaluator must use the canonical roadmap meanings of A0--A4, serialize
all nine mandatory A2 metrics, distinguish actual/constructed/proxy/control
owners, and decide A0/A1 without importing credit across owners. All A2,
A3, and A4 ceilings remain FAIL or the exact typed negative enum. Route B is
not invoked and no Stage-12 Route-B YAML may exist.

```text
PHASE3_V4_INTEGRATED_GATE=PASS
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
STANDALONE_PASS=true
P12_1_THROUGH_P12_8=PROVED
P12_9_CONTROLS=PASS
P12_10_ROUTE_A_AUTHORIZED=true
ROUTE_A_OWNER_COUNT=8
ROUTE_B_INVOCATION_ALLOWED=false
ACTIVE_LOCK_BYTES_CHANGED=false
CONTROL_MANIFEST_INVALIDATED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

**Final gate decision: PASS (`C0/M0/m0`) with `STANDALONE_PASS`; exactly
the eight frozen Route-A evaluations are authorized.**
