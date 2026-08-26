# Paper 12 Phase-3 v4 controls and reproducibility review

Review date: **2026-08-15 (Asia/Shanghai)**  
Review mode: **independent, read-only ARS experiment/integrity/methodology audit**  
Verdict: **PASS — C0/M0/m0**

## 1. Scope and authority

This review audits the frozen `P12-9` deterministic control package, its
reproduction entry point, its exact active locks and gates, and its relation
to the stable v4 proof.  It does not re-prove the real or infinite-`Q`
theorems, re-run the source audit, evaluate Route, or authorize manuscript or
release work.  No code, result, lock, gate, proof, Route artifact, or pipeline
state was edited.  The only file written by this reviewer is this report.

The audit used the ARS experiment validation, integrity, and methodology
review contracts.  In particular, deterministic output requires exact bytes;
finite witnesses remain separate from universal proofs; negative controls are
checked explicitly; and an execution anomaly is not silently converted into
either a pass or a mathematical defect.

## 2. Exact reviewed tuple

All hashes below were independently recomputed before the authorized run,
during the post-run audit, and again after all processes had ended.

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` |

The manifest deliberately records
`proof_binding.concurrent_v4_proof_hash_included=false`: the controls were
frozen while the proof lane was concurrent.  This review therefore binds the
now-stable proof separately.  Its SHA-256 remained
`77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8`
at every observation, including after the unrelated extra reproduction
processes described in Section 8.  There was no proof-hash race.

## 3. Implementation binding and static audit

| Implementation artifact | SHA-256 |
|---|---|
| `code/generate_controls.py` | `0aa35a649a676fdd9c747c3b3ff27f8b815aa1e3ff761315cfdf4ceba906fd99` |
| `code/test_controls.py` | `b9c234d8fa2b104f2358707bfbba5f7e59eaf3603715edff0714f70e9d14b76b` |
| `code/README.md` | `b94c7c85e995df80f487044351ac5beeb6e9eee9d42c956e51d07637ff160547` |
| `experiments/reproduce.sh` | `aec1371b249cc564d781980c1aae6fa3209c5ec2ec350962060783d947574090` |
| `experiments/README.md` | `edeaa4f75754ca6888ee710b8e6c7a49956c1f2c234b29e96e56171b033fcf6d` |
| `results/README.md` | `3f3153b767364595ba455db4f6a8c8716263cc1621e0988a5fc73e68dfa8cac9` |

These are exactly the six implementation hashes serialized by the manifest.
Static inspection found:

- Python-standard-library-only execution, with no network or external-data
  path, no random draw, and no timestamp in generated content;
- `LC_ALL=C`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, and `python3 -B`
  at the reproduction boundary;
- exact integer, rational (`Fraction`), set, permutation, and CSV checks; the
  sole numerical tolerance is the frozen `1e-12` absolute boundary for the
  four displayed `log`/`sqrt` period controls, rendered with `.15g`;
- fail-closed binding of the five active-lock files, all six phase gate/status
  files, all six implementation files, exact artifact names, schemas, rows,
  hashes, and manifest semantics; and
- checked-in results are opened only by `--verify-only`; the two writable
  generations are confined to distinct `mktemp` directories removed by the
  exit trap.

The reserved seed `120012` is serialized and unused.  No zeta-zero table,
fitted target, trace, determinant convention, Paper-8 coefficient, Paper-11
completion, or source-PDF content enters the compiler.

## 4. One authorized top-level reproduction

The preflight scan found zero Paper-12 reproduction/generator/test processes
and zero `__pycache__`, `.pyc`, or `.pyo` artifacts.  This reviewer then
executed exactly once:

```text
./experiments/reproduce.sh
```

from `papers/12-marked-time-cohomology/`.  The command completed with exit
code `0` and reported:

```text
Ran 122 tests in 149.094s
OK
PASS schema=paper12-marked-time-cohomology-controls/2 csv=11 rows=3486 negative=14
7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95  .../results/manifest.json
PASS: >=96 tests, strict verification, 11-CSV/3486-row three-way byte identity, recursive-entry gate, and no-cache scan
```

The source contains exactly `122` `unittest` methods, so the run is
`122/122`, not merely the frozen lower bound of `96`.  The five package-status
lines correspond to checked-in strict verification plus generation and strict
verification of each of the two fresh copies.  Every `cmp` across checked-in,
fresh-one, and fresh-two returned success for all eleven CSV files and
`manifest.json`; no comparison emitted a byte difference.

## 5. Exact artifact package

An independent CSV/JSON parser, not the generator's manifest builder,
recomputed each header, body-row count, byte count, and digest and compared it
with the checked manifest.

| CSV | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `control_summary.csv` | 9 | 6 | `61fc4f8cb46f15710886a8f4f4bd6e65559ebd78367fc50cd3653b98f5ea6370` |
| `degree1_cohomology_controls.csv` | 125 | 14 | `ebd3bb8062e1c4acec70f5b28d3dca90fc9aabdb92fd90592c0f2bb0dafb6b51` |
| `factorization_controls.csv` | 6 | 12 | `888b2a95f23a80ef9eb06ef008ee9f81344612a01bce19e0ff1f88993213fce0` |
| `label_boundary_controls.csv` | 24 | 10 | `b3f82c3af8382b1d890cd25e1d496cc2b93be90104c036c15d6159ae2af91e90` |
| `morphism_controls.csv` | 20 | 21 | `00dbe2ff0e918682cfc75db6e5893631537d77111fcf60c9eff6d21c915a6d2d` |
| `negative_controls.csv` | 12 | 4 | `0a3a5c2333a0d5d2620b0f54c22e1dfeba9a8eacc336a61d6de45d9ca2736493` |
| `nerve_face_controls.csv` | 12 | 12 | `c50500cc4775abf20c96de55caf6c62330abfa79177bc7dec6eee76b20c52672` |
| `orbitwise_standardization_h1_controls.csv` | 3252 | 26 | `54498a635f255472b7e7687049a25a23e394408f4adc4d43dc459c2b952943a6` |
| `packet_period_controls.csv` | 12 | 12 | `3f13dbbbe464522d92e3e33c5b55528be6fd55e92d26b295d74c87ab83c9932e` |
| `period_controls.csv` | 10 | 12 | `b7f2450441514b87bd15f9da3598d5c05f4f11cb948679536c0af05433de5d33` |
| `quotient_topology_controls.csv` | 4 | 16 | `0bc8338ca42a3a617638c25d3a89309c0388c376fd7208cb592d020bcd9ff5df` |

The ten legacy CSVs retain exactly their frozen hashes and contain exactly
`234` body rows.  Adding the new `3252`-row ledger gives exactly eleven CSVs
and `3486` body rows.

## 6. Independent v4 algebra and schema checks

The new ledger has the exact 26-column schema frozen in the v4 amendment.
Its body is ordered as follows, with no missing, duplicated, or out-of-block
row:

| Block | Exact count | Independent check |
|---|---:|---|
| `MODEL` | 9 | lexicographic `(n,m)` in `{3,5,7} x {1,2,3}` |
| `BASEPOINT` | 90 | every `(n,m,orbit,basepoint)` exactly once |
| `AUT` | 3151 | every component permutation and every translation vector exactly once, in frozen lexicographic order |
| `NEGATIVE` | 2 | `MIXED_LENGTHS`, then `WRONG_J_DIRECTION` |

For the automorphism block, the independently parsed total is

```text
(3 + 3^2*2! + 3^3*3!)
+ (5 + 5^2*2! + 5^3*3!)
+ (7 + 7^2*2! + 7^3*3!) = 3151.
```

For every one of the nine models, the audit confirmed:

- actual and standardized open counts `2` and `2^(nm)`;
- actual `H^1` dimension `1` and standardized dimension `m`;
- comparison rank `1` and full-permutation invariant dimension `1`;
- enumerated automorphisms equal `n^m m!`, with exhaustive equivariance and
  two-sided inverse checks;
- exhaustive basepoint transport and the finite joint-action law;
- a nonzero coboundary with zero orbit sums and exact recovery of a
  basepoint-zero potential from the frozen zero-isotropy cocycle; and
- exact recovery of the transitive case for all three `m=1` models.

The two v4 negatives detect mixed cycle lengths and the reversed
standard-to-actual comparison direction.  All `3252` rows retain
`packet_schematic_only=true`, `replaces_source_proof=false`, and `status=PASS`.
An independent pass over the old ledgers also confirmed all twelve legacy
negative controls, zero face-identity and `d^2` failures, zero T0 nonfactor
maps versus `254` non-T0 witnesses, five and only five linear cocycle profiles,
zero nonzero `B^1` probes, all twelve wrong-scale detections, four one-sided
topology rows, zero packet-period mismatches, and the one label-neutral
generic signature across all 24 label permutations.  Thus the package has
`12 + 2 = 14` explicit detected negatives and zero observed negative-control
failure.

## 7. Fail-closed and no-cache assessment

The passing suite exercises clean temporary generation; two-generation byte
identity; checked-in verification; read-only `--verify-only`; content, v4-row,
row-count, and schema tampering; extra file and directory rejection; missing
artifact and output rejection; active-lock, Phase-2 gate, v4 amendment, v4
final-gate, and v4 status-relock drift; implementation drift and absence;
manifest metric, schema, artifact-hash, and invalid-JSON changes; recursive
entry; canonical headers; and absence of Python cache artifacts.

The final post-incident scan found:

```text
Paper-12 reproduce/generator/test processes: 0
/tmp/paper12-marked-time-cohomology.* directories: 0
__pycache__ / *.pyc / *.pyo under code, experiments, results: 0
active-lock, gate, proof, implementation, result, manifest hash drift: 0
```

Accordingly, process residue, temporary-directory residue, Python cache
residue, checked-result mutation, and proof-hash race are all absent in the
final reviewed state.

## 8. Shared-workspace orchestration incident

The incident is recorded because suppressing it would make the reproduction
provenance false.  After the clean preflight and during the audit window, the
first post-run shared-workspace scan found two additional top-level
`reproduce.sh` trees and two `mktemp` directories:

```text
2396066 -> 2396075    /tmp/paper12-marked-time-cohomology.eaufXG
2396146 -> 2396150 -> 2396156
                      /tmp/paper12-marked-time-cohomology.0Dzth0
```

The root orchestrator traced both extra launches to the separate standalone
review lane.  One completed; the second was stopped after provenance was
resolved.  The root then verified zero surviving processes, and both exit
traps/cleanup paths left zero temporary directories.  No further reproduction
was run by this controls reviewer.

This was a real violation of the README's operator rule to serialize
top-level reproductions.  It is not counted as a control finding because it
originated outside this review's single authorized invocation, the script
does not claim a cross-process global lock, each extra process used
checked-in `--verify-only` plus a private `mktemp` root, and every bound byte
and the proof hash remained unchanged.  It therefore neither invalidates the
authorized run's exact comparisons nor changes a mathematical/control
verdict.  Future multi-agent dispatches should nevertheless reserve one
top-level reproduction owner and forbid all other lanes from invoking the
entry point until that owner closes.

## 9. Finding register and verdict

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
V4_CONTROLS_REVIEW=PASS
ACTIVE_LOCKS_EXACT=true
FINAL_GATE_EXACT=true
STATUS_RELOCK_EXACT=true
PROOF_SHA256=77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8
PROOF_HASH_RACE=false
MANIFEST_SHA256=7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95
TESTS_PASSED=122
TESTS_FAILED=0
CSV_ARTIFACTS=11
TOTAL_CSV_ROWS=3486
ORBITWISE_ROWS=3252
ORBITWISE_COLUMNS=26
ORBITWISE_BLOCKS=9/90/3151/2
LEGACY_ROWS_UNCHANGED=234
EXPLICIT_NEGATIVES=14
NEGATIVE_FAILURES=0
THREE_WAY_BYTE_IDENTITY=true
FINAL_PROCESS_RESIDUE=0
FINAL_TEMP_RESIDUE=0
FINAL_CACHE_RESIDUE=0
ORCHESTRATION_INCIDENT_RECORDED=true
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

**Final verdict: PASS (`C0/M0/m0`).**  The stable v4 controls are exact,
deterministic, independently reproducible, fail-closed at the frozen gates,
and correctly bounded as finite witnesses rather than proof or source
substitutes.  This verdict closes the controls lane only; standalone, Route,
composition, manuscript, and release authority remain with their separate
gates.
