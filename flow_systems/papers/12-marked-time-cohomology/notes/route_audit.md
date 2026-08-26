# Paper 12 formal Route-A audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Evaluator: **typed Route-A / Route-B gate reviewer**  
Result: **six `ROUTE_A_EXPLORATORY`, two `ROUTE_A_REJECTED`; Route B false**

## 1. Exact authorization and evidence tuple

The final integrated gate authorizes exactly the eight frozen Stage-12 owners.
This audit binds the following stable bytes:

| Artifact | SHA-256 | Role |
|---|---|---|
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` | v0.2.0 schema and A0--A4 vocabulary |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` | no-rescue and Route-B entry boundary |
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` | active protocol and eight owners |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` | typed owner and verdict ceilings |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` | unchanged active state tuple |
| `notes/phase3_v4_route_provenance_amendment.md` | `db1fe49108ab3697596847571bcdadbed1e6df251cc941b7d51b6c15780372a7` | acyclic output-provenance rule |
| `notes/phase3_v4_route_provenance_relock.md` | `20c67ace45b81523400053b388923e4a01c725b0bfdd528f2c391803ded0cb4d` | provenance PASS C0/M0/m0 |
| `notes/phase3_v4_integrated_gate.md` | `2b23ecc9462431dbebd12a6af5994a09a7f7d7e37bad10f1f11d118aa3ecc9c4` | exact eight-owner authorization |
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | generic/orbit complex proof |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | marked orbit/packet and morphism proof |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | final v4 standardization/H1 proof |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | pre-Route PASS C0/M0/m0 |
| `notes/phase3_peer_review.md` | `7d3ddb6d28d425695696965b73caeaa109f5a5cc27c1c52fd8fb826138818f36` | integrated Phase-3 PASS C0/M0/m0 |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | frozen 122-test/11-CSV control receipt |
| `results/period_controls.csv` | `b7f2450441514b87bd15f9da3598d5c05f4f11cb948679536c0af05433de5d33` | marked-period controls |
| `results/packet_period_controls.csv` | `3f13dbbbe464522d92e3e33c5b55528be6fd55e92d26b295d74c87ab83c9932e` | every-unit packet controls |
| `results/morphism_controls.csv` | `00dbe2ff0e918682cfc75db6e5893631537d77111fcf60c9eff6d21c915a6d2d` | scaled/unmarked controls |
| `results/label_boundary_controls.csv` | `b3f82c3af8382b1d890cd25e1d496cc2b93be90104c036c15d6159ae2af91e90` | arithmetic-selectivity controls |
| `results/quotient_topology_controls.csv` | `0bc8338ca42a3a617638c25d3a89309c0388c376fd7208cb592d020bcd9ff5df` | standard/actual topology controls |
| `results/orbitwise_standardization_h1_controls.csv` | `54498a635f255472b7e7687049a25a23e394408f4adc4d43dc459c2b952943a6` | v4 comparison/H1 controls |

Paths in this table below `notes/` or `results/` are relative to
`papers/12-marked-time-cohomology/`; the two skill paths are repository-relative.

## 2. Typed coordinate adjudication

| Candidate | Exact tuple | Overall verdict |
|---|---|---|
| `GEN-INDISC-R-ACTION-CNV` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| `DEN-EF-ACTUAL-ORBIT-CNV-P-A` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ACTUAL-PACKET-CNV-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-STANDARD-PERIOD-QUOTIENT-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `UNMARKED-PERIOD-SCALING-CONTROL` | `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |

The actual orbit and packet owners receive direct source A0 because the same
Deninger objects own `p` and the unfitted common lattice `(log p)Z`. Their
period/repetition evidence remains only `A1_WEAK`: no record owns the required
phase, multiplicity, stability, amplitude, or global prime enumeration.

The standard-circle and standardized-packet records copy the source lattice
into constructed proxies and therefore receive only weak A0. Their exact
component periods earn `A1_WEAK`, but no actual topology, `Q_p` topology/count,
or arithmetic selectivity is imported. The generic complex fails both A0 and
A1. The unmarked control fails A0; its individual exact periods earn only
`A1_WEAK` because unequal-period dilation destroys owner-level selection.

Every owner explicitly freezes
`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`. Consequently all A2 records fail with
exactly nine `not_applicable`/negative metrics; all A3 and A4 records fail for
lack of a same-owner analytic divisor/Weil compression and natural lift.

## 3. Stage-12 hash ledger

| Candidate YAML | SHA-256 |
|---|---|
| `evaluations/route_a/GEN-INDISC-R-ACTION-CNV/2026-08-15-stage12.yaml` | `b098a29644094b021a1784a560f3429dd547c94f5c898c47922ec1deb3e3a616` |
| `evaluations/route_a/DEN-EF-ACTUAL-ORBIT-CNV-P-A/2026-08-15-stage12.yaml` | `72e7f6a13c42f1a66cf518bad2a9c5891609afb7dc78e4bf472638dfee39b5a5` |
| `evaluations/route_a/DEN-EF-ACTUAL-PACKET-CNV-P/2026-08-15-stage12.yaml` | `f3580335a7592ce9aabb25494da401b5b1ff29821b7631094be46304793dae9f` |
| `evaluations/route_a/DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A/2026-08-15-stage12.yaml` | `2af304786ee062cf623fe30c4c868775b6c3fafbfc6c29c1e76385ea128dace6` |
| `evaluations/route_a/DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P/2026-08-15-stage12.yaml` | `fbc8968768ce171634d8a0320f9a28eaa54c3db2d3aefcd28c82a7caaa1c2ee7` |
| `evaluations/route_a/DEN-EF-STANDARD-PERIOD-QUOTIENT-P/2026-08-15-stage12.yaml` | `52be219e27d51042844b91bcd7a79c1315a8153282595b60c656964daac09302` |
| `evaluations/route_a/DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P/2026-08-15-stage12.yaml` | `98859e9f84926fb6900f03e137fa2e3905a6cd0332eddb30de955d094c9de347` |
| `evaluations/route_a/UNMARKED-PERIOD-SCALING-CONTROL/2026-08-15-stage12.yaml` | `950524f41c60c6f2b556f10aebdbbcb8c48d9edc3021e7d966dc612e92f1a647` |

The YAMLs bind only stable upstream hashes. Their own paths and this audit path
are locator-only; no YAML embeds its own hash or this audit's hash. This audit
binds the final YAML hashes but not its own hash. Downstream composition and
release artifacts alone may bind the final `route_audit.md` digest.

## 4. Mechanical closure and Route-B decision

Read-only validation returned PASS for:

- exactly eight Stage-12 Route-A YAMLs and zero Stage-12 Route-B YAMLs;
- PyYAML parsing and the exact ordered v0.2.0 top-level/nested schema;
- candidate-ID/directory identity and the resolved no-Git receipt;
- all A0--A4, evidence-status, adversarial, and overall-verdict enums;
- exactly the nine mandatory A2 metric keys in every record;
- every hash-qualified artifact path and digest;
- the active tuple, amendment, relock, integrated gate, proof audit, peer
  review, final proof, and controls manifest in every record;
- exact locator-only output paths; and
- Boolean `route_b_invocation_allowed: false` in all eight records.

No reproduction, generator, test-control, or verify-only entry point was run
in this Route lane. The already audited manifest is upstream evidence, not a
fresh execution result.

No owner reaches `A4_ROUTE_B_READY`, and the integrated gate forbids Route B.
No Stage-12 Route-B YAML exists.

```text
P12_10_ROUTE_A_COMPLETE=true
ROUTE_A_OWNER_COUNT=8
ROUTE_A_EXPLORATORY_COUNT=6
ROUTE_A_REJECTED_COUNT=2
A2_A3_A4_POSITIVE_COUNT=0
ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_FILE_COUNT=0
HASH_GRAPH_ACYCLIC=true
SCHEMA_VALIDATION=PASS
ARTIFACT_HASH_VALIDATION=PASS
REPRODUCE_EXECUTED_BY_ROUTE_LANE=false
```

**Final Route conclusion:** Paper 12 proves exact cohomological and marked-
period boundary theorems, but no frozen owner supplies a dynamical determinant,
global analytic divisor, Weil compression, or natural operator lift. The six
source/proxy-related records remain exploratory; the generic and unmarked
controls are rejected. Route B remains closed.
