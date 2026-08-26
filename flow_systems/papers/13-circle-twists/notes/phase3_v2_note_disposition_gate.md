# Paper 13 Phase-3 v2 technical-note disposition gate

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent integrated technical-note disposition adjudicator**  
Disposition verdict: **`PASS_TO_TECHNICAL_NOTE`**  
Current mathematical findings: **C0 / M0 / m0**  
Retained standalone findings: **C0 / M1 / m0**

## 1. Decision and non-overriding effect

The frozen Paper-13 v2 mathematical package is coherent for the technical-note
branch of the active `NOTE_OR_MERGE` disposition.  The exact core, support,
and corona proof packages have independent mathematical PASS reviews, and the
replacement finite-controls tuple has an effective PASS review.  No proof,
typing, source-owner, or control-integrity defect was found in this disposition
audit.

This verdict does **not** close, downgrade, or supersede the binding Major
finding in `notes/phase3_v2_standalone_review.md`.  That review establishes
that P13-8B/C reduce, after the required ownership subtraction, to a generic
constant-diagonal `c0`/multiplier/corona lemma once the component isometries
are available.  The result is correct and useful, but it does not have the
owner-specific central weight required for a standalone article.  Therefore:

```text
STANDALONE_PASS=false
NOTE_OR_MERGE=true
NOTE_BRANCH_SELECTED=true
MERGE_BRANCH_SELECTED=false
```

The present zero-finding count is only the count for mathematical coherence
and technical-note disposition.  It is not a second standalone review and
must never be used to rewrite the retained standalone count `C0/M1/m0` as
zero.

## 2. Active-lock compatibility

The active protocol does not forbid a technical note.  It sends a routine or
noncentral P13-8 to `NOTE_OR_MERGE`; the final independent v2 standalone
review expressly states that the proved material is suitable for a technical
note or a merge.  The NOTE branch is therefore an authorized disposition,
not a workaround for `STANDALONE_PASS=false`.

The technical-note branch preserves every active firewall:

- Arm A, including the continuous real-line multiplier collapse and the
  standard twisted-convolution/gauge/completion package, receives no
  standalone novelty credit;
- the hard fixed-prime continuum lower bound remains Paper-2-owned;
- actual-packet, actual-collapse, standardization, and companion-paper results
  remain with their exact prior owners;
- finite controls remain regression, falsification, and owner-ledger evidence,
  never proof of an arbitrary-index or continuum theorem;
- `SUPPORTED_WITHIN_SEARCH` is the maximum novelty language and is neither an
  absence proof nor a priority finding; and
- Route B, standalone-article positioning, release, Git action, and public
  synchronization remain false.

## 3. Exact-byte evidence binding

All hashes below were recomputed from the local bytes immediately before this
gate was written.

### 3.1 Active locks and Phase-2 source/novelty authority

| Artifact | SHA-256 | Bound use |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | active question, standalone rule, Route ceiling, and release boundary |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | active candidate lock |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | active phase state read as a stop ledger, not an authorization override |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | author-delta matrix, fail-closed disposition, and exact ten-owner registry |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` | Phase-1 lock acceptance and downstream stops |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | framework/source applicability ceilings |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` | retained framework-source locator manifest |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` | retained source-byte ledger |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | signs, conventions, names, and owner ceilings |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | bounded exact-package search; no priority conclusion |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | Phase-2 PASS and retained `NOTE_OR_MERGE` branch |

### 3.2 Stable mathematical proof and peer-review tuple

| Artifact | SHA-256 | Verdict/use |
|---|---|---|
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | frozen P13-1--P13-5 proof input |
| `notes/phase3_core_peer_review.md` | `a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665` | independent core PASS, C0/M0/m0 |
| `notes/phase3_support_retention_proofs.md` | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | frozen P13-6--P13-8 support input |
| `notes/phase3_support_peer_review.md` | `ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed` | independent support PASS, C0/M0/m0 |
| `notes/phase3_standalone_amendment_v2.md` | `99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82` | P13-8A--C v2 candidate boundary |
| `notes/phase3_standalone_amendment_v2_ownership_addendum.md` | `d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f` | Paper-2 subtraction and max/reduced owner condition |
| `notes/phase3_v2_methodology_review.md` | `96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74` | v2 methodology closure |
| `notes/phase3_v2_devils_advocate.md` | `1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110` | v2 design-stage adversarial closure |
| `notes/phase3_v2_source_feasibility.md` | `3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320` | v2 source PASS; maximum `SUPPORTED_WITHIN_SEARCH` |
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | exact v2 proof/design authorization boundary |
| `notes/phase3_v2_corona_proofs.md` | `81b0f8aaa1cf6277323452c55107cf33d8ad69783eb80998cc0f4f0d9d636858` | final P13-8A--C proof |
| `notes/phase3_v2_corona_peer_review.md` | `0ae271fd99f3290d7d18486cfc98ad8ccf95aa1421619ccd4fdf72865deb28c8` | independent proof PASS, C0/M0/m0 |

### 3.3 Replacement controls and binding standalone disposition

| Artifact | SHA-256 | Verdict/use |
|---|---|---|
| `results/manifest.json` | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` | stable replacement finite-controls manifest |
| `notes/phase3_v2_controls_review.md` | `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789` | effective controls PASS, C0/M0/m0, with the original oracle-integrity Major closed |
| `notes/phase3_v2_standalone_review.md` | `ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e` | binding `NOTE_OR_MERGE`, C0/M1/m0; M1 retained |

No superseded first-run controls tuple is a downstream evidence input to this
gate.  In particular, this gate binds only the stable replacement manifest
and its final review.  It did not rerun or reproduce the controls.

### 3.4 Mandatory internal owner subtraction

| Owner artifact | SHA-256 | Result that remains with that owner |
|---|---|---|
| Paper 2 `papers/2-flow-zeta/paper/manuscript.tex` | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | typed sign subgroup, procyclic intersection, continuum lower bound, and bare-set packet transfer in Proposition `prop:uncountable` |
| Paper 2 `papers/2-flow-zeta/notes/proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | accepted lower-bound proof and topology ceiling |
| Paper 8 `papers/8-isotropy-trace/paper/manuscript.tex` | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` | one-orbit standard-circle action-groupoid completion/trace formulas and the scoped positive-time scalar ledger |
| Paper 8 `papers/8-isotropy-trace/notes/proof_audit.md` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` | exact local-versus-packet owner firewall and scalar-domain limits |
| Paper 9 `papers/9-packet-separation/paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | actual fixed-prime packet, globally indiscrete topology, stabilizer `p^Z`, period `log p`, and bare orbit quotient `U_p/H_p` |
| Paper 9 `papers/9-packet-separation/notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact topology and quotient-owner audit |
| Paper 11 `papers/11-indiscrete-convolution/paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | actual globally-indiscrete time-only collapse, author convolution algebra, and transported full/reduced time-group records |
| Paper 11 `papers/11-indiscrete-convolution/notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | exact collapse/completion owner audit and naming boundary |
| Paper 12 `papers/12-marked-time-cohomology/paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | same-carrier orbitwise standardization, compact open orbit torsors, owner firewall, and `J:G_std -> G_actual` |
| Paper 12 `papers/12-marked-time-cohomology/notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | standardized cohomology and intrinsic invariant-diagonal proof comparator |
| Paper 12 `papers/12-marked-time-cohomology/notes/phase3_standalone_review.md` | `a05139142f24b75b682561c732045787923d5c9d6a6d619657880919ba9a39ec` | prior nonredundancy comparator; not Paper-13 novelty evidence |

## 4. Technical-note coherence adjudication

The NOTE branch is mathematically coherent for four reasons.

1. The normalized continuous circle-multiplier reduction, typed twisted
   convolution and involution, gauge-star isomorphisms, and transported
   maximal/reduced records are exact at the frozen signs and domains.  Their
   being standard or prior-covered reduces publication weight but does not
   invalidate them.
2. The action/period-retention and fixed-prime statements preserve their
   literal owners and negative ceilings.  They do not manufacture arithmetic
   selectivity, a determinant, or a spectral invariant from gauge-equivalent
   time data.
3. P13-8A is unconditional and correctly typed, but the hard lower bound is
   subtracted to Paper 2, the packet carrier to Paper 9, and standardization
   to Paper 12.  It therefore supplies context, not standalone credit.
4. P13-8B/C give an exact maximal/reduced component norm chain, an
   origin-free arbitrary-index diagonal, the finite/infinite membership
   dichotomy, exact corona norm, gauge covariance, and an unconditional
   fixed-prime specialization.  After component isometries, however, the
   corona theorem is precisely the generic constant-diagonal theorem for a
   `c0` sum.  This is a sound technical result and exposition package, while
   remaining insufficient for standalone centrality.

Thus the package has a stable, honest technical-note purpose: to record one
carefully typed synthesis, exact direct verification, owner-preserving
comparison diagram, and sharp nonselectivity boundary.  The NOTE label is
essential because the same reduction that defeats standalone status is part
of the note's correct mathematical positioning.

## 5. Mandatory title/abstract/introduction positioning contract

Any later manuscript that passes its own gates must be explicitly and visibly
positioned as a **technical note**.  Its title must include “Technical Note”
or an equally unambiguous technical-note label.  Its abstract and introduction
must perform all of the following subtractions before stating the Paper-13
delta:

1. credit Sorkin for the continuous real-line multiplier-collapse result at
   the audited strength, and identify twisted convolution, gauge
   trivialization, group-crossed-product, amenability, `c0`-sum, multiplier,
   and corona facts as standard prior mathematics where applicable;
2. state that Paper 2 owns the nontrivial continuum lower bound, including
   the sign/procyclic argument, and that Paper 13 receives no novelty or Route
   credit for reusing it;
3. state the exact Paper-8 subtraction: its one-orbit standard-circle proxy,
   trace/return formulas, local-versus-packet firewall, and positive-time
   scalar ledger are not Paper-13 results;
4. state the exact Paper-9 subtraction: the actual fixed-prime packet,
   actual indiscrete topology, stabilizer/period data, and bare quotient
   `U_p/H_p` are inherited;
5. state the exact Paper-11 subtraction: the actual globally-indiscrete
   time-only collapse, author convolution algebra, and transported untwisted
   full/reduced time-group records are inherited;
6. state the exact Paper-12 subtraction: the same-carrier orbitwise
   standardization, its compact open orbit components and owner firewall, the
   comparison map `J`, and its intrinsic invariant-diagonal theorem are
   inherited/comparator results; and
7. state affirmatively that the Paper-13 corona theorem is the instantiation
   of a **generic constant-diagonal `c0`/multiplier/corona lemma after the
   component maps have been proved isometric**.  It must not be described as
   a new owner-specific corona obstruction or a prime-sensitive invariant.

The title, abstract, introduction, theorem statements, conclusion, metadata,
cover letter, and any publicity must contain no “first”, “new classification”,
“novel obstruction”, priority, or standalone-breakthrough claim.  The maximum
external-novelty formulation is the dated and bounded
`SUPPORTED_WITHIN_SEARCH`; no direct exact-package hit was found within that
search, which does not prove priority or absence.

The note must also retain these negative boundaries: no topology transfer
from an actual packet to the standardized owner, no unaudited global twisted
groupoid `C*` naming, no proof-by-control claim, no determinant/A3/A4
promotion, and no assertion that the unconditional fixed-prime corona remnant
is a prime-selective analytic invariant.

Only the exact proved v2 package bound above may enter this technical-note
lane.  Later unproved candidate material is outside this disposition.

## 6. Exact Route-A registry and bounded authorization

This gate authorizes the **Route-A evaluation only** as the next executable
stage.  Exactly the following ten Stage-13 owner-local records may be created
and evaluated, using the existing Stage-9--12 schema and the date-stamped path
shown.  No eleventh record, owner splice, or Route-B record is permitted.

| # | Owner ID | Authorized path | Frozen ceiling |
|---:|---|---|---|
| 1 | `TIME-R-CONT-TWIST` | `evaluations/route_a/TIME-R-CONT-TWIST/2026-08-15-stage13.yaml` | time-group/generic source only; no arithmetic credit |
| 2 | `GEN-INDISC-R-ACTION-CONT-TWIST` | `evaluations/route_a/GEN-INDISC-R-ACTION-CONT-TWIST/2026-08-15-stage13.yaml` | generic; A0 ceiling fail |
| 3 | `GEN-INDISC-R-ACTION-TWISTED-GLOB-QC` | `evaluations/route_a/GEN-INDISC-R-ACTION-TWISTED-GLOB-QC/2026-08-15-stage13.yaml` | generic actual-author test algebra; no cross-owner credit |
| 4 | `GEN-INDISC-R-ACTION-TW-FULL` | `evaluations/route_a/GEN-INDISC-R-ACTION-TW-FULL/2026-08-15-stage13.yaml` | author full transport; generic only |
| 5 | `GEN-INDISC-R-ACTION-TW-RED` | `evaluations/route_a/GEN-INDISC-R-ACTION-TW-RED/2026-08-15-stage13.yaml` | author reduced transport; generic only |
| 6 | `DEN-EF-ACTUAL-PACKET-CONT-TWIST-P` | `evaluations/route_a/DEN-EF-ACTUAL-PACKET-CONT-TWIST-P/2026-08-15-stage13.yaml` | source-origin arithmetic ceiling only |
| 7 | `DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P` | `evaluations/route_a/DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P/2026-08-15-stage13.yaml` | source-origin ceiling; no donated A2--A4 |
| 8 | `GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER` | `evaluations/route_a/GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER/2026-08-15-stage13.yaml` | generic support/component-diagonal/corona relation; A0 fail; no arithmetic credit |
| 9 | `DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P` | `evaluations/route_a/DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P/2026-08-15-stage13.yaml` | inherited Paper-2 cardinality; source-origin relation only; no A2--A4 promotion |
| 10 | `TWIST-DOMAIN-NONSELECTIVITY-CONTROL` | `evaluations/route_a/TWIST-DOMAIN-NONSELECTIVITY-CONTROL/2026-08-15-stage13.yaml` | control only; no transferable Route credit |

Owners 8--9 may quantify both `epsilon in {max,r}` within their single owner
records only if the two completions have identical evidence status and final
Route verdict.  If they differ, evaluation must stop before serialization and
a versioned pre-Route owner/count amendment plus independent review is
mandatory.  The count of ten may not be preserved by conflating unequal
owners or outcomes.

Every YAML must evaluate A0--A4 locally, preserve acyclic provenance, omit its
own digest, and set `route_b_invocation_allowed: false`.  Route B cannot rescue
a negative classical fit.

## 7. Downstream staged boundary

The authorized sequence is fail-closed:

```text
this exact gate
  -> exactly ten owner-local Stage-13 Route-A evaluations
  -> independent Route audit binding the ten exact YAML hashes
  -> separately audited composition blueprint for the NOTE branch
  -> manuscript drafting explicitly as a technical note
  -> independent manuscript, citation, and peer-review audits
  -> separate release audit
```

This gate selects the technical-note destination for that sequence, but it
does not substitute for any intervening audit.  At the moment this gate is
frozen:

- Route-A evaluation of the exact ten owners: **authorized**;
- Route audit: **required after YAML creation; not performed here**;
- composition: **blocked pending its own post-Route authorization/audit**;
- technical-note manuscript drafting: **conditionally eligible only after
  the Route audit and composition gate; not performed here**;
- manuscript review, citation audit, peer review, and release audit:
  **separately required and not performed here**;
- Route B: **false**;
- standalone-article manuscript: **false**;
- release, Git action, and public synchronization: **false**.

No Route YAML, composition artifact, manuscript, citation package, peer
review, release artifact, Git action, or public synchronization is created or
authorized as completed by this file.

## 8. Machine-readable receipt

```text
PHASE3_V2_NOTE_DISPOSITION=PASS_TO_TECHNICAL_NOTE
CURRENT_MATHEMATICAL_FINDINGS=C0/M0/m0
STANDALONE_FINDINGS=C0/M1/m0
STANDALONE_M1_CLOSED=false
STANDALONE_M1_DOWNGRADED=false
STANDALONE_PASS=false
NOTE_OR_MERGE=true
NOTE_BRANCH_SELECTED=true
MERGE_BRANCH_SELECTED=false
TECHNICAL_NOTE_LABEL_REQUIRED=true
CORONA_THEOREM_GENERIC_CONSTANT_DIAGONAL_AFTER_COMPONENT_ISOMETRIES=true
PRIORITY_CLAIM_ALLOWED=false
NOVELTY_CEILING=SUPPORTED_WITHIN_SEARCH
ROUTE_A_OWNER_COUNT=10
ROUTE_A_EVALUATION_AUTHORIZED=true
ROUTE_AUDIT_REQUIRED=true
ROUTE_B_INVOCATION_ALLOWED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
STANDALONE_ARTICLE_AUTHORIZED=false
CITATION_AUDIT_REQUIRED=true
PEER_REVIEW_REQUIRED=true
RELEASE_AUTHORIZED=false
GIT_ACTION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
CONTROLS_RERUN_BY_THIS_GATE=false
SUPERSEDED_FIRST_RUN_CONTROLS_BOUND=false
LATER_UNPROVED_CANDIDATES_INCLUDED=false
```

**Final verdict: `PASS_TO_TECHNICAL_NOTE`.**  The exact v2 mathematics may
advance through the frozen ten-owner Route-A evaluation toward an explicitly
positioned technical note, while the binding standalone verdict remains
`NOTE_OR_MERGE`, `C0/M1/m0`, with `STANDALONE_PASS=false`.
