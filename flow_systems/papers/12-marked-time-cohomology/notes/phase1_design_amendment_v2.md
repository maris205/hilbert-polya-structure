# Paper 12 Phase-1 design amendment v2

Amendment date: **2026-08-15 (Asia/Shanghai)**  
Status: **NARROW EXACTNESS CORRECTION — INDEPENDENT v2 RE-LOCK PENDING**

## 1. Immutable v1 history

Amendment v1 submitted this exact content tuple:

| Artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `a923bfcf5fbae2d3136632794f0eb68ce4b7e48f217f0a071295e9fe4a85dda5` |
| `candidate_lock.md` | `0932d8a388ce732a3ad0702f3703cc91088d2fa73cc02f0a8063d240d70f5a42` |
| `pipeline_state.md` | `9cb7c51c534fd26f68fb66853312b022202c1d58b0ff2d74910c4deb3b32059b` |
| `phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` |

The v1 re-lock outcomes were:

| Review | Verdict | Final report SHA-256 |
|---|---|---|
| methodology/nonredundancy | `REVISE C0/M0/m2` | `ba9e54f81847a4184463a206b0424177e4436702569b8dd39a995d7bf965382d` |
| devil's advocate/domain | `REVISE C0/M1/m0` | `8dce153cb25760729237d264fbe74f5cbf3403e553627526f47f78d9d70413c7` |
| source/scope feasibility | `PASS C0/M0/m0` | `7f5778d7be3843eb238d7192000b93fe1f04cc0dbdd24007600578e0406f74e3` |

All initial mathematical, coefficient, owner, category, quotient, control,
source, novelty, and release findings were closed on v1. The remaining issues
were bounded contract exactness only.

## 2. Packet-branch correction

V1 inconsistently allowed a documented unavailable packet corollary in one
standalone sentence while requiring the corollary elsewhere. V2 makes one
decision everywhere:

```text
PACKET_COROLLARY is mandatory for STANDALONE_PASS.
ORBIT_ONLY forces NOTE_OR_MERGE.
```

This changes no packet theorem or source gate. It only makes the failure
branch executable and fail-closed.

## 3. Complete Route-A intake

V1 omitted six mandatory evaluator fields and used a pending code provenance
placeholder. V2 freezes seven exact candidate records. Every record now has:

```text
candidate_id
candidate_definition
family
phase_space
dynamics
parameters
parameter_provenance
arithmetic_origin
clock
normalization
determinant_convention
orbit_cutoff
precision
training_data
forbidden_data
code_commit
artifact_paths
```

The seven IDs are:

```text
GEN-INDISC-R-ACTION-CNV
DEN-EF-ACTUAL-ORBIT-CNV-P-A
DEN-EF-ACTUAL-PACKET-CNV-P
DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A
DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P
DEN-EF-STANDARD-PERIOD-QUOTIENT-P
UNMARKED-PERIOD-SCALING-CONTROL
```

Each receives the exact Stage-12 path
`evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml` plus exact
Paper-12 proof, manifest, peer-review, and route-audit paths. `P12-10` cannot
execute until those paths exist and their final SHA-256 values are serialized.

The code provenance value is now the resolved state

```text
unavailable-no-git-content-sha256-lock-required
```

rather than a pending future commit. Exact implementation/content hashes are
mandatory mechanical substitutes. The negative determinant convention and
A1/A2/A3/A4/Route-B ceilings are unchanged.

## 4. v2 tuple submitted for re-lock

| Active artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `9c4947880f894dabb0648e9434fdf6e3a28cf2d9bf6434f86579370d8da80087` |
| `candidate_lock.md` | `1893cb74a5fc1a004873d5d027faf58bb384c3419699675dd37f33ee7b13c14f` |
| `pipeline_state.md` | `971489c1208ef32082bf936bf6c8b45661740d9b867857250a02798e02fafb62` |
| `phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` |

Reviewers must also bind the final SHA-256 of this v2 amendment. The v1
amendment and the existing review prefixes/addenda remain untouched.

## 5. Non-claim

V2 is a two-item design correction. It proves no `P12-*` target, changes no
mathematical verdict, performs no Phase-2 search, creates no Route YAML, and
does not authorize downstream work until all three independent reviewers
return `PASS C0/M0/m0` on the exact v2 tuple.
