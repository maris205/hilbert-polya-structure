# Paper 12 Phase-3 v3 exact-byte methodology re-lock

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent methodology / category / reproducibility lane**  
Review mode: **read-only exact-byte re-lock**  
Verdict: **REVISE — C0/M0/m2; exact-byte re-lock not granted**

## 1. Scope and independence

This review applies the ARS academic-pipeline, methodology-reviewer, peer-
review, and integrity disciplines to the v3 standalone-strength amendment.
It audits only whether the amended design is sufficiently typed and frozen to
authorize the later targeted source audit, proof, control, and standalone
review lanes. It does not prove the v3 theorem, execute controls, decide
novelty, evaluate Route A, draft the manuscript, or modify an active lock.

The stable v2 proofs and the two conflicting v2 reviews were used only as
evidence for the inherited mathematical baseline and the exact prior Major.
No conclusion in this report withdraws or reinterprets a v2 proof or review.
The only file written by this lane is this report.

## 2. Exact-byte input receipt

The following hashes were independently recomputed both before the audit and
immediately before this report was written.

### 2.1 Active v3 tuple

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `0c8301de2d98c7d07b067b54d49657a5c63ef8f5f93e333f3034697972bfda2f` |
| `notes/candidate_lock.md` | `dae1ae4bf8c54aabc6bf3ccc8a8aebe0377563d09512689b62792ab0b6ff0972` |
| `notes/pipeline_state.md` | `e69d253718d2994fa4a4ea34f3926033566d97caaacdef8b7c8b3445f91f778b` |
| `notes/phase3_disposition_gate.md` | `cc0a9578d187f5dad443b7dc37870e7c24278fca5f02ad532523aeee76ceefa8` |
| `notes/phase3_standalone_amendment_v3.md` | `3751971dd4f2803f8144526f2ad0acefa1e76c5ac8173d3ab6401d316cd7fcf6` |

### 2.2 V2 evidence only

| Artifact | SHA-256 | Evidentiary use |
|---|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | passed `P12-1`--`P12-5` baseline |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | passed `P12-6`--`P12-8` baseline |
| `notes/phase3_peer_review.md` | `12abc205f2e599035ac8fa64346d25672bcadcbea55bca98b88151e5a13022b9` | mathematical PASS and positive standalone judgment |
| `notes/phase3_standalone_review.md` | `a05139142f24b75b682561c732045787923d5c9d6a6d619657880919ba9a39ec` | mathematical PASS, prior routine-reduction M1, and proposed flip point |

## 3. Methodology audit

### 3.1 Category and object domains

The amended object domains are coherent. `C_str` remains the groupoid of
normalized transitive coordinate-marked indiscrete action groupoids with
lattice stabilizer `H=LZ`, while `Hom_R^std` removes the basepoint and keeps
standard Hausdorff transitive right `R`-homogeneous spaces and strictly
equivariant homeomorphisms. The arithmetic orbit and packet owners remain
applications rather than generic hypotheses. No full-suspension, cross-prime,
separated-reflection, completion, trace, or determinant object is imported.

The target word `standard` is operationally constrained by the required
usual quotient topology. At proof time the orbit map must be factored through
`R/H`, and the compact-to-Hausdorff argument (or the quotient universal
property at exactly the frozen domain) must be displayed rather than assumed.
This is already a proof obligation, not an open design defect.

### 3.2 Basepoint-independent topology

The proposed independence calculation has the correct direction. If
`x'=x dot u`, then

```text
q_(x')(t)=x dot (u+t)=(q_x o T_u)(t).
```

Precomposition by the real translation homeomorphism `T_u` leaves the
quotient topology on the same set `X` unchanged. Since `H=LZ` is closed, the
standard quotient is Hausdorff. The frozen topology direction is also
correct: the identity from the standardization to the actual indiscrete unit
space is continuous, while the reverse identity is noncontinuous for a
nontrivial object. The design never retypes this new topology as inherited or
as the Paper-10 Hausdorff/completely-regular reflection.

### 3.3 `Std`, `Indisc`, fullness, and faithfulness

The strict mark fixes the complete arrow coordinate. A strict isomorphism
must have

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t.
```

Thus descent to an equivariant unit homeomorphism and the converse lift are
correctly frozen, and range plus `c` give uniqueness. The indiscrete arrow
topologies make the lifted map and its inverse continuous; the standard
quotient diagrams make the descended unit map and its inverse continuous.
These obligations are sufficient to prove that `Std` is full and faithful.

`Indisc` retains the underlying set and action, indiscretizes only the unit
topology, and forms the same range-first marked groupoid. Consequently the
two composites can be strict inverses under the stated concrete-object
convention, or an equivalence under explicitly displayed natural
isomorphisms. No variance or functor-domain mismatch was found.

### 3.4 Automorphisms and the pointed shadow

For a transitive right `R`-space, an equivariant automorphism is determined by
the image of one unit. Commutativity makes every translation admissible, and
the kernel of `u |-> (x |-> x dot u)` is exactly `H`. Therefore the frozen
classification

```text
Aut_Cstr(G,c) ~= Aut_R(Std(G,c)) ~= R/H
```

has the correct domain and composition law. The existing pointed functor `S`
is correctly retained as a nonfaithful shadow: it sends the distinct strict
unit translations to the unique basepoint-preserving target arrow. It is not
called an equivalence, and scaled dilations remain outside the strict target.

### 3.5 Integration, ownership, and prior M1

The new theorem is integrated into `P12-8`, the standalone conjunction, the
delta matrix, the standard-period Route owner, and the release stops. It adds
no new Route owner and does not alter the pre-existing A-coordinate ceilings.

The amendment genuinely addresses the structural defect identified in the
prior M1: the central target now retains all strict morphisms and admits an
inverse construction, instead of collapsing them through a pointed rigid
target. This is not yet closure of the semantic M1. The amendment correctly
keeps that decision conditional on the targeted primary/authoritative
precedent audit, the v3 proof and controls, and an independent standalone
re-review. Methodology re-lock therefore must not be confused with a novelty
or standalone verdict.

## 4. Findings

### m1 — stale Phase-1 PASS wording conflicts with the active v3 pending state

`notes/candidate_lock.md` Section 9 says that the current bytes are
“Phase-1-PASS design bytes” and that `phase1_final_gate.md` binds their exact
tuple. The displayed v3 candidate hash is not the hash bound by that old
gate, while the file header, `pipeline_state.md`, the disposition gate, and
the v3 amendment all correctly say exact-byte re-lock is pending.

This does not accidentally authorize proof or Route because the controlling
pipeline and amendment are fail-closed, so the finding is Minor rather than
Major. It nevertheless prevents an exact-byte PASS: a later reader cannot
treat the same current file simultaneously as already Phase-1-gated and
awaiting v3 re-lock.

Required repair: rephrase Section 9 so that the old gate is explicitly the
v2 historical gate and the current v3 tuple remains unpassed until the new
three-reviewer re-lock and gate are recorded.

### m2 — the new deterministic finite control carrier is not completely frozen

`STD-EQUIV-L` freezes the properties to check and the four `PER-L` labels,
but the active tuple does not freeze the finite cyclic carrier order(s), the
exact new CSV artifact name, or the deterministic row-count construction.
The protocol simultaneously says the control package is fixed before proof
work and contains no post-hoc choice. The missing carrier/artifact metadata
therefore leaves a small discretionary surface between re-lock and control
implementation.

The issue cannot falsify the universal theorem because controls are expressly
finite witnesses, not proofs, so it is Minor. It is still material to this
reproducibility re-lock.

Required repair: freeze a nontrivial cyclic order (or an exact finite list of
orders), the output filename, and the deterministic row/schema rule before
proof/control implementation. The later manifest may serialize the resulting
hash and exact row count as usual.

## 5. Finding register and disposition

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 2 | stale gate wording; underfrozen finite-control metadata |

```text
V3_METHODOLOGY_RELOCK=REVISE
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=2
CATEGORY_DOMAINS=COHERENT
BASEPOINT_INDEPENDENCE=CORRECTLY_TYPED
STD_FULL_FAITHFUL_EQUIVALENCE=PROOF_ELIGIBLE_AFTER_RELOCK
AUTOMORPHISM_CLASSIFICATION=CORRECTLY_TYPED
PRIOR_M1_STRUCTURAL_DEFECT=ADDRESSED_BUT_NOT_YET_CLOSED
TARGETED_SOURCE_NOVELTY_AUDIT=STILL_REQUIRED
ROUTE_OR_MANUSCRIPT_AUTHORIZED=false
```

**Final verdict: REVISE (`C0/M0/m2`).** The mathematical design of the v3
equivalence is methodology-ready, but exact-byte re-lock is withheld until
the two bounded metadata/status findings are repaired and the amended tuple
is reviewed again.
