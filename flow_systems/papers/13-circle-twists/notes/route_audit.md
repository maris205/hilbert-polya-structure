# Paper 13 formal Route-A audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Evaluator: **typed Route-A / Route-B gate reviewer**  
Result: **three `ROUTE_A_EXPLORATORY`, seven `ROUTE_A_REJECTED`; Route B false**

## 1. Exact authorization and evidence tuple

The technical-note disposition gate authorizes exactly the ten frozen
Stage-13 owners below.  This audit treats the selected technical-note
destination as a publication status only.  It is not an A-axis coordinate,
does not promote any owner, and supplies no arithmetic, determinant,
analytic, or operator evidence.

This audit binds the following stable upstream bytes:

| Artifact | SHA-256 | Role |
|---|---|---|
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` | v0.2.0 schema and A0--A4 vocabulary |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` | no-rescue and Route-B entry boundary |
| `papers/13-circle-twists/notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | active protocol |
| `papers/13-circle-twists/notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | active candidate and owner lock |
| `papers/13-circle-twists/notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | unchanged pre-Route state receipt |
| `papers/13-circle-twists/notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | exact ten-owner registry and ceilings |
| `papers/13-circle-twists/notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` | Phase-1 authorization boundary |
| `papers/13-circle-twists/notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | final framework/source ceiling |
| `papers/13-circle-twists/notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` | source-manifest receipt |
| `papers/13-circle-twists/notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` | source checksum ledger |
| `papers/13-circle-twists/notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | signs, conventions, and ownership firewalls |
| `papers/13-circle-twists/notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | bounded novelty ceiling |
| `papers/13-circle-twists/notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | Phase-3 authorization receipt |
| `papers/13-circle-twists/notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | final P13-1--P13-5 proof |
| `papers/13-circle-twists/notes/phase3_core_peer_review.md` | `a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665` | independent core-proof PASS |
| `papers/13-circle-twists/notes/phase3_support_retention_proofs.md` | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | final P13-6--P13-8 support proof |
| `papers/13-circle-twists/notes/phase3_support_peer_review.md` | `ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed` | independent support-proof PASS |
| `papers/13-circle-twists/notes/phase3_v2_corona_proofs.md` | `81b0f8aaa1cf6277323452c55107cf33d8ad69783eb80998cc0f4f0d9d636858` | final bounded P13-8A--C proof |
| `papers/13-circle-twists/notes/phase3_v2_corona_peer_review.md` | `0ae271fd99f3290d7d18486cfc98ad8ccf95aa1421619ccd4fdf72865deb28c8` | independent corona-proof PASS |
| `papers/13-circle-twists/results/manifest.json` | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` | replacement controls manifest |
| `papers/13-circle-twists/notes/phase3_v2_controls_review.md` | `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789` | replacement-manifest review and closure addendum |
| `papers/13-circle-twists/notes/phase3_v2_standalone_review.md` | `ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e` | binding `NOTE_OR_MERGE`, C0/M1/m0 |
| `papers/13-circle-twists/notes/phase3_v2_note_disposition_gate.md` | `b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e` | exact Route authorization and technical-note destination |

The following ownership tuple is also frozen.  It is used only to subtract
inherited premises and prevent credit transfer:

| Ownership artifact | SHA-256 | Route boundary |
|---|---|---|
| `papers/2-flow-zeta/paper/manuscript.tex` | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | Paper 2 owns the fixed-prime continuum lower bound |
| `papers/2-flow-zeta/notes/proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | sign-subgroup/procyclic proof and its ceiling |
| `papers/8-isotropy-trace/paper/manuscript.tex` | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` | no trace/scalar or amplitude transfer |
| `papers/8-isotropy-trace/notes/proof_audit.md` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` | Paper-8 ownership receipt |
| `papers/9-packet-separation/paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | exact packet/bare-set premise only |
| `papers/9-packet-separation/notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | Paper-9 ownership receipt |
| `papers/11-indiscrete-convolution/paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | author global-QC premise only |
| `papers/11-indiscrete-convolution/notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | Paper-11 ownership receipt |
| `papers/12-marked-time-cohomology/paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | factorization/standardization premise only |
| `papers/12-marked-time-cohomology/notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | standard-owner proof and ceiling |
| `papers/12-marked-time-cohomology/notes/phase3_standalone_review.md` | `a05139142f24b75b682561c732045787923d5c9d6a6d619657880919ba9a39ec` | Paper-12 disposition boundary |

## 2. Typed coordinate adjudication

| # | Candidate | Exact tuple | Overall verdict |
|---:|---|---|---|
| 1 | `TIME-R-CONT-TWIST` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 2 | `GEN-INDISC-R-ACTION-CONT-TWIST` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 3 | `GEN-INDISC-R-ACTION-TWISTED-GLOB-QC` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 4 | `GEN-INDISC-R-ACTION-TW-FULL` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 5 | `GEN-INDISC-R-ACTION-TW-RED` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 6 | `DEN-EF-ACTUAL-PACKET-CONT-TWIST-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| 7 | `DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| 8 | `GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER` | `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |
| 9 | `DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| 10 | `TWIST-DOMAIN-NONSELECTIVITY-CONTROL` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` |

The evaluation is owner-local.  The time-group and four generic actual-author
twist/completion owners have no arithmetic source and retain no primitive
return ledger, so they are rejected.  The exact fixed-prime packet supplies
the only limited same-owner source relation: owner 6 retains direct packet
origin and weak period evidence; owner 7 retains only weak fixed-domain
relation; owner 9 retains weak fixed-prime relation and weak exact
period/cardinality/corona structure.  None of these relations supplies a
prime-power amplitude, determinant, global analytic divisor, Weil
compression, or operator lift.

Owner 8 is a generic topology/completion theorem.  Its common period and
finite/infinite support/corona split earn only `A1_WEAK`; arbitrary-period,
arbitrary-index, and nonarithmetic controls force A0 to fail.  Owners 8 and 9
quantify both `epsilon in {max,r}` only because the maximal and reduced
records have identical evidence status, coordinate tuple, and final Route
verdict.  They remain one registry owner each; no count amendment is needed.

Owner 10 is `CONTROL_ONLY`.  Frozen diagnostic outcomes are not proof and
cannot transfer positive Route credit.  Likewise, the generic constant
diagonal/corona lemma, Paper-8 trace/scalar results, Paper-9--12 conclusions,
and Paper-2 infinity remain with their original owners.  In particular,
Paper-2's fixed-prime lower bound and sign/procyclic proof receive zero
Paper-13 novelty, standalone, or Route credit.

Every owner freezes `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`.  All ten A2
records therefore fail with exactly nine mandatory metrics; all A3 and A4
records fail for lack of a same-owner global analytic object and natural
spectral lift.  The technical-note disposition does not alter this
adjudication.

## 3. Stage-13 hash ledger

| Candidate YAML | SHA-256 |
|---|---|
| `evaluations/route_a/TIME-R-CONT-TWIST/2026-08-15-stage13.yaml` | `e10c099de4a3468aee163efaff28d817ae55e2af505b3f88fccc8b160587c4f1` |
| `evaluations/route_a/GEN-INDISC-R-ACTION-CONT-TWIST/2026-08-15-stage13.yaml` | `e8b3c85a8d08554130cae1c44183262de908bff27315a2f7cdb6098527e2ef3c` |
| `evaluations/route_a/GEN-INDISC-R-ACTION-TWISTED-GLOB-QC/2026-08-15-stage13.yaml` | `24596827430fb6c77fb349379b13ed17ad3a0b95cbd85f21e183f6c4bf1767bb` |
| `evaluations/route_a/GEN-INDISC-R-ACTION-TW-FULL/2026-08-15-stage13.yaml` | `27307b7b331deafdcc1cecbd37b0466e1fcdd853be9c3ce0451a136eded0abd2` |
| `evaluations/route_a/GEN-INDISC-R-ACTION-TW-RED/2026-08-15-stage13.yaml` | `2154fdc83553b6a35496379f2cc38572de4c042fae3f73e5197856fd23dead17` |
| `evaluations/route_a/DEN-EF-ACTUAL-PACKET-CONT-TWIST-P/2026-08-15-stage13.yaml` | `9cd6ead9e63266e64aee8942c2482b028b9aba947f3479d6f6e08eac249a4a49` |
| `evaluations/route_a/DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P/2026-08-15-stage13.yaml` | `bd0f38f9613c4593f76c336f119818c11fb2875ba2987a938bc4e148e9a91eb1` |
| `evaluations/route_a/GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER/2026-08-15-stage13.yaml` | `b65d21a61e615b771c0e0a83095df806b7e4317cb03568a52aa409713a33c6ea` |
| `evaluations/route_a/DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P/2026-08-15-stage13.yaml` | `6b2d998303351f922b3e53f9f6c512741cfd5576b761e47df1252e8c2cc78a8d` |
| `evaluations/route_a/TWIST-DOMAIN-NONSELECTIVITY-CONTROL/2026-08-15-stage13.yaml` | `835b530233e9b416bcf34a2a55ff4ab472ecf2e7121f4c8453d1211648b3b94d` |

The YAMLs bind only stable upstream hashes.  Their own paths and this audit
path are locator-only; no YAML embeds its own hash or this audit's hash.  This
audit binds the ten final YAML hashes but deliberately does not embed its own
hash.  A downstream composition or release artifact may bind the final
`route_audit.md` digest.

## 4. Mechanical closure and Route-B decision

Read-only validation returned PASS for:

- exactly ten authorized Stage-13 Route-A YAMLs and zero Stage-13 Route-B
  YAMLs;
- PyYAML parsing and the exact ordered canonical v0.2.0 top-level and nested
  schema;
- exact candidate-ID/directory/path identity against the ten-owner registry;
- all A0--A4 and overall-verdict enums and the frozen ten adjudication tuples;
- exactly the nine mandatory ordered A2 metric keys in every record;
- all 151 hash-qualified artifact paths and digests;
- Boolean `route_b_invocation_allowed: false` in all ten records;
- identical maximal/reduced evidence status and final outcome in owners 8--9;
  and
- the acyclic locator-only output graph and no self-digest.

No reproduction, generator, deterministic-control, test-control, or
verify-only entry point was run in this Route lane.  The replacement manifest
and review are stable upstream evidence, not a fresh execution result.

No owner reaches `A4_ROUTE_B_READY`, and the disposition gate forbids Route B.
No Stage-13 Route-B YAML exists.

```text
P13_STAGE13_ROUTE_A_COMPLETE=true
ROUTE_A_OWNER_COUNT=10
ROUTE_A_EXPLORATORY_COUNT=3
ROUTE_A_REJECTED_COUNT=7
A2_A3_A4_POSITIVE_COUNT=0
ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_FILE_COUNT=0
HASH_GRAPH_ACYCLIC=true
SCHEMA_VALIDATION=PASS
ARTIFACT_HASH_VALIDATION=PASS
NOTE_BRANCH_SELECTED=true
TECHNICAL_NOTE_STATUS_IS_NOT_A_AXIS=true
STANDALONE_ARTICLE_AUTHORIZED=false
REPRODUCE_EXECUTED_BY_ROUTE_LANE=false
CONTROLS_EXECUTED_BY_ROUTE_LANE=false
```

**Final Route conclusion:** Paper 13 proves a bounded exact twist/gauge and
support/component/corona package suitable for the selected technical-note
lane, but no frozen owner supplies a dynamical determinant, global analytic
divisor, Weil compression, or natural operator lift.  Three source-related
owners remain exploratory; seven generic/control owners are rejected.  Route
B remains closed.
