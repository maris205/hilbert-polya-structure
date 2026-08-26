# Paper 12 Phase-3 controls and reproducibility review

Review date: **2026-08-15 (Asia/Shanghai)**  
Scope: **independent audit of `P12-9` only**  
Verification status: **VERIFIED / REPRODUCIBLE**  
Verdict: **PASS — C0/M0/m0**

## 1. Material Passport and independence statement

```text
artifact_type: deterministic-control validation report
paper: 12-marked-time-cohomology
target: P12-9
determinism_class: deterministic
reproduction_verdict: REPRODUCIBLE
statistical_content: none; exact finite enumeration and frozen float displays only
source_upload: none
external_network: none
reviewer_write_scope: notes/phase3_controls_review.md only
```

This review was conducted from the frozen protocol, candidate lock, Phase-1
and Phase-2 gates, implementation, checked results, and the two Phase-3 proof
lanes. It did not use the controls producer's verdict as evidence. The
reviewer did not edit code, results, locks, gates, proofs, Route records, or a
manuscript.

The complete ARS experiment-validation, statistical-interpretation, and
integrity instructions were applied. The control package contains no
inferential statistics, so significance, effect-size, confidence-interval,
assumption, and multiple-comparison interpretation are not applicable. The
eleven-item statistical fallacy scan was completed `11/11`; every item is
not applicable to this deterministic enumeration package, and no causal or
population inference is drawn from it.

## 2. Frozen authority and exact-byte binding

The following active lock and authorization bytes were independently
rehashed after all validation runs:

| Artifact | Observed SHA-256 | Manifest-bound |
|---|---|---|
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` | yes |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` | yes |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | yes |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` | yes |
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` | yes |
| `notes/phase1_status_relock.md` | `a7a9875c810ea98f5a5563c8f243612b006c20f397aaa8ebae533d8b8c6c61d6` | yes |
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` | yes |
| `notes/phase2_status_relock.md` | `c6fb9d3a04171bc68ed6239e1a91cee8f9987cd75d8516967d3ded5de6b89eea` | yes |
| `notes/pipeline_state.md` | `24c226e35d69c6aab68df19d495957469ec761551680696b20cff865604fe62d` | yes |

The Phase-2 gate authorizes direct Phase-3 proofs and deterministic `P12-9`
controls, records `PACKET_COROLLARY_ELIGIBLE`, and records
`ORBIT_ONLY=false`. The current pipeline state retains Route and manuscript
work as blocked. The live bytes exactly match the generator constants and
the manifest.

Implementation and receipt hashes are:

| Artifact | SHA-256 |
|---|---|
| `code/generate_controls.py` | `fe557d3296e2fd841e313c9e0708a144acfc9da616616f82de30b00f873ec6e7` |
| `code/test_controls.py` | `719e492a1fe07033c8b25edc7dd46aa589f3c6e21d50b14573bef955f638fde6` |
| `experiments/reproduce.sh` | `b3e85a593b1910683ed7545e9ccca9d482f94d8ebf7a7da94d0337fc0e577828` |
| `code/README.md` | `b14b1cc5001db756f058da086af4489632409041ef03cb9c64dcb919e6779dd8` |
| `experiments/README.md` | `ddfefbdaa31fb2ae89ce22fd3ae2231f2dfb58a24aa1a7d71185ee2c9a97f609` |
| `results/README.md` | `9edcfb77529bb8bed32ff97373875edeb47658e3764c9e6fd393421b6d4a96b8` |
| `results/manifest.json` | `5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a` |

The controls manifest deliberately does not bind a changing Phase-3 proof
hash. For snapshot context only, the reviewed proof-lane hashes were
`9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd`
for `phase3_core_proofs.md` and
`3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49`
for `phase3_marked_packet_proofs.md`. Neither filename nor hash occurs in
`manifest.json`. Thus the control tuple has no proof-hash race; a later
integration gate can bind stable proof and control receipts separately.

## 3. Reproduction and fail-closed verification

This reviewer invoked the sole top-level entry point
`./experiments/reproduce.sh` exactly once. The review then independently
checked each part of its contract instead of treating its terminal `PASS`
line as evidence:

- a direct test-module run exited `0` with `Ran 88 tests in 80.106s` and
  `OK`;
- strict verification of checked-in results exited `0` and preserved every
  result file's SHA-256 and nanosecond modification time;
- two independently generated fresh directories each passed strict
  verification;
- all ten CSVs plus `manifest.json` were byte-identical across fresh copy 1,
  fresh copy 2, and the checked-in result directory;
- the two fresh copies reproduced manifest SHA-256
  `5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a`;
  and
- all temporary directories were automatically removed.

An independent mutation audit obtained nonzero exits for each of the
following seven classes:

| Injected condition | Fail-closed result |
|---|---|
| altered CSV bytes | `artifact content/schema/row drift` |
| unexpected output file | output filename contract rejected `extra.csv` |
| missing required CSV | output filename contract rejected the missing artifact |
| candidate-lock byte drift | active-lock SHA-256 drift |
| Phase-2-gate byte drift | phase-gate/status SHA-256 drift |
| implementation byte drift | manifest/hash/lock/gate/implementation drift |
| manifest metric drift | manifest/hash/lock/gate/implementation drift |

The implementation also directly covers row drift, schema drift, unexpected
directories, missing output directories, missing implementation files,
manifest schema/hash drift, invalid JSON, and pre-existing extra output.
`--verify-only` is therefore read-only and fail-closed over filenames,
schemas, parsed rows, bytes, hashes, locks, gates, implementations, and the
full manifest object.

Final hygiene inspection found zero `__pycache__` directories, zero `.pyc`
or `.pyo` files under the authorized control paths, zero Paper-12
reproduction/audit temporary directories under `/tmp`, and zero surviving
`reproduce.sh`, `test_controls.py`, or `generate_controls.py` processes.

## 4. Artifact ledger

Every CSV uses UTF-8, LF line endings, a terminal newline, its exact declared
header, and no extra column. Counts below exclude the header row.

| CSV | Rows | Bytes | SHA-256 |
|---|---:|---:|---|
| `control_summary.csv` | 9 | 716 | `61fc4f8cb46f15710886a8f4f4bd6e65559ebd78367fc50cd3653b98f5ea6370` |
| `degree1_cohomology_controls.csv` | 125 | 18710 | `ebd3bb8062e1c4acec70f5b28d3dca90fc9aabdb92fd90592c0f2bb0dafb6b51` |
| `factorization_controls.csv` | 6 | 711 | `888b2a95f23a80ef9eb06ef008ee9f81344612a01bce19e0ff1f88993213fce0` |
| `label_boundary_controls.csv` | 24 | 7432 | `b3f82c3af8382b1d890cd25e1d496cc2b93be90104c036c15d6159ae2af91e90` |
| `morphism_controls.csv` | 20 | 4360 | `00dbe2ff0e918682cfc75db6e5893631537d77111fcf60c9eff6d21c915a6d2d` |
| `negative_controls.csv` | 12 | 1535 | `0a3a5c2333a0d5d2620b0f54c22e1dfeba9a8eacc336a61d6de45d9ca2736493` |
| `nerve_face_controls.csv` | 12 | 1506 | `c50500cc4775abf20c96de55caf6c62330abfa79177bc7dec6eee76b20c52672` |
| `packet_period_controls.csv` | 12 | 2445 | `3f13dbbbe464522d92e3e33c5b55528be6fd55e92d26b295d74c87ab83c9932e` |
| `period_controls.csv` | 10 | 1122 | `b7f2450441514b87bd15f9da3598d5c05f4f11cb948679536c0af05433de5d33` |
| `quotient_topology_controls.csv` | 4 | 904 | `0bc8338ca42a3a617638c25d3a89309c0388c376fd7208cb592d020bcd9ff5df` |

The totals are exactly **10 CSVs, 234 body rows, and 39,441 CSV bytes**.
All artifact counts, sizes, columns, row counts, and hashes agree with the
manifest.

## 5. Independent semantic recomputation

The reviewer parsed the checked CSVs without importing
`generate_controls.py` and independently recomputed their semantics.

### 5.1 Nerve, faces, and differential

- The 12 rows are exactly four finite right actions crossed with degrees
  `1,2,3`.
- Independent coordinate and composable-arrow enumeration checked **817**
  nerve coordinates; every `Psi` image equals the independently enumerated
  composable nerve.
- Independent face composition checked **161,659** simplicial face
  identities with **0 failures**.
- Independent alternating double-differential collection checked **102,171**
  basis coefficients. Every coefficient is zero, and an all-positive-sign
  mutation produces a nonzero coefficient.
- The CSV scope correctly says `finite exact witness; not an all-degree
  proof`.

### 5.2 `T0` factorization and degree-one profiles

- The six factorization rows exhaust every binary map on the two-unit finite
  sources in degrees `0,1,2`.
- Discrete `T0` targets have **0** continuous nonfactor maps; indiscrete
  non-`T0` targets have **254** across the three degrees, with valid explicit
  first witnesses.
- The degree-one ledger is exactly the `5^3=125` frozen polynomial profiles
  `(a,b,c) in {-2,-1,0,1,2}^3`, with all 25 Cauchy pairs recomputed per row.
  Exactly **5** linear profiles pass and **120** nonlinear or affine profiles
  are rejected.
- These rows are finite profile probes only. They do not replace the direct
  continuous-Cauchy or degree-zero constancy proofs.

### 5.3 Period, morphism, topology, packet, and labels

- The period ledger has 10 exact/symbolic rows: 6 positive lattice rows and
  4 nonlattice boundary rows. The four frozen printed real values agree with
  `log(2)`, `log(4)`, `sqrt(2)`, and `37/29` within the sole `1e-12`
  absolute float boundary.
- The morphism ledger has 4 strict identities, 4 orientation reversals, and
  all 12 ordered unequal-period positive dilations. Every scale is
  `alpha=M/L`; the largest covariance error is
  `2.22044604925031e-16`, and the largest well-definedness error is
  `8.88178419700125e-16`. All 12 identity-scale and reciprocal-direction
  negatives are detected.
- The four topology rows independently reproduce the three-point proxy's 8
  standard opens versus 2 indiscrete opens: standard-to-actual is
  continuous, its inverse is not, and equivariance/basepoint direction is
  correct. The rows explicitly remain a finite topology proxy.
- The packet ledger contains exactly 12 rows (`p in {2,3,5,7}` times three
  schematic units). Every row binds the actual Phase-2 gate hash, states
  `schematic_only=true`, and states `replaces_source_proof=false`. The rows
  therefore compile the already source-gated schema; they do not manufacture
  packet membership, a common stabilizer, or source evidence.
- The label ledger contains every one of the 24 permutations exactly once.
  All have the same frozen generic/Route-boundary signature
  `4cae673ad7c09d77dd2bf40dd57d5bca5fd919ecb4b794227ea87bc872b4c939`,
  set `arithmetic_specificity_selected=false`, and set
  `proves_too_much=true`.
- All 12 explicit negative controls are detected.

## 6. Target-free and noncircular boundary

The generator imports only Python standard-library modules. Code inspection
and execution found no network use, external dataset, randomness, timestamp,
fitting, target-zero value, zeta-zero table, trace, determinant, Paper-8
coefficient, or Paper-11 completion input. The reserved seed `120012` is
serialized and unused. Exact combinatorial, integer, set, schema, symbolic,
and string checks use zero tolerance; the `1e-12` tolerance is confined to
the frozen displayed real/scale comparisons.

The two Phase-3 proof lanes prove their universal and source-dependent
statements analytically and explicitly state that no finite control is used
as a universal proof. Conversely, the controls manifest does not depend on
either proof file. Static symbolic boundary fields in the period, quotient,
packet, label, and summary ledgers were audited as typed declarations, not
laundered as computed universal results. In particular:

- `control_summary.csv` sets `universal_proof=false` and
  `arithmetic_specificity_proved=false` on every preregistered control;
- packet rows disclaim source-proof replacement;
- topology rows say they are finite direction proxies; and
- label rows deliberately record `PROVES_TOO_MUCH`.

The package is therefore target-free and noncircular at its declared scope.
It validates regressions, counterexamples, schema boundaries, and
reproducibility; it does not certify P12-1--P12-8, source truth, arithmetic
specificity, Route coordinates, or standalone release.

## 7. Finding register and gate decision

| Severity | Count | Open finding |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P12-9_controls_review: PASS
critical_open: 0
major_open: 0
minor_open: 0
tests: 88/88
csv_artifacts: 10
csv_body_rows: 234
negative_controls: 12/12
fresh_generation_identity: exact
strict_verify_fail_closed: true
packet_source_evidence_manufactured: false
finite_controls_promoted_to_universal_proof: false
proof_hash_race: false
cache_temp_process_residue: false
reproduction_verdict: REPRODUCIBLE
```

**Final verdict: PASS (`C0/M0/m0`).** The `P12-9` control tuple is eligible
for binding into the independent Phase-3 integration gate. This report does
not authorize Route evaluation, manuscript drafting, or release.

The detached SHA-256 of this report is computed after the final byte is
written and is supplied as the authoritative post-write receipt; embedding
that value here would change the hashed file.
