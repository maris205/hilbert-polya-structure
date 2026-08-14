# Paper 8 formal Route-A audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Evaluator: `route-a-evaluator` v0.2.0, with the Route-B no-splice rule and
ARS integrity boundary applied  
Decision: **five record-specific `ROUTE_A_EXPLORATORY` evaluations; Route B
not invoked**

## 1. Executive decision

The evidence supports three different statements that must not be collapsed:

1. the packet-level primary normal-extension question remains
   **`NOT_TESTABLE`**, because `Gamma_p` Hausdorff/LCH and the packet same-map
   completion/disintegration bridge are absent;
2. the fixed one-orbit trivial-character trace has no normal extension along
   its proved local regular map, so that **local analogue is `REFUTED`**; and
3. the coefficient-one positive-time scalar record is **`PROVED` as a Radon
   measure/closed-point repetition ledger**, not as a packet trace, global
   operator trace, or determinant.

Every evaluated record has `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`.  No record has
a dynamical/Fredholm determinant, completed analytic structure, natural
quantization, or a Route-B entry.  Every YAML therefore has
`route_b_invocation_allowed: false`; no Route-B YAML is created.

## 2. Exact evidence lock

### Active locks and current Phase-2 authority

| Artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` |
| `phase2_final_relock.md` | `b1ed0c68e1eac5605d70f0a482f28139f764eff12f7fa87007ad9fd854553619` |
| `phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` |
| `phase2_novelty_search.md` | `28862717c996b60a7c9e210cae65a78ee1a42d035dafadb8f6f8e59435df0bca` |

`phase2_final_relock.md` is the current mechanical authority for the Phase-2
ledger.  It preserves the older gate as historical evidence while correctly
distinguishing the pre-addendum `c22f...` content snapshot from the current
`phase2_domain_da_review.md` bytes `05fecacd...c014`.

### Phase-3 proofs, controls, and independent review

| Artifact | SHA-256 |
|---|---|
| `phase3_topology_ownership_proofs.md` | `209989444b48a625777c0c4626b92429ed08b58f3dc4c31b03f7d23b067dca14` |
| `phase3_operator_proofs.md` | `5e8fd6cd400c7300da5c80e8991b3770ad03c9026a236caab04642cd96314a26` |
| `phase3_controls_review.md` | `a054265f3fb25ef93270a6e5c5a1db6791f8bbb7b08b78f8e13b7554a93a3f3d` |
| `phase3_peer_review.md` | `572e7852de08ded264f87bb245aff181ae032ed8a8bfdf831fcd4ed5d1f921c3` |
| `results/isotropy_trace_manifest.json` | `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07` |

The final independent peer review is `PASS`, with `0 Critical / 0 Major / 0
Minor`.  Its narrow addendum independently verifies the Phase-2 mechanical
re-lock and changes no theorem, outcome, T0--T7 field, or Route ceiling.

I independently reran `./papers/8-isotropy-trace/experiments/reproduce.sh`.
All 18 tests passed; the active tuple, six implementation hashes, nine CSV
hashes, and manifest verified; two fresh generations were byte-identical.
The final manifest hash was the value in the table above.

## 3. Why there are five YAML records

Four records would conflate an owner.  The additional
`DEN-EF-ORBIT-ACTION-GRPD` evaluation is **necessary, not redundant**:

- the packet record cannot own the local LCH/Haar/completion theorem because
  its LCH gate is open;
- the regular and character traces cannot own each other's representation or
  return behavior; and
- both local traces depend on the same separately proved one-orbit groupoid
  without turning that groupoid into either trace.

The two exact local trace owners receive new evaluation IDs:

```text
DEN-EF-ORBIT-GRPD-REG-TRACE
DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE
```

This is the conservative implementation of the active lock's rule that a
different completion/representation creates a new candidate or version.  It
prevents local theorems from being written under the packet-level parent IDs
`DEN-EF-GRPD-REG-TRACE-FAM` and
`DEN-EF-GRPD-TRIVCHAR-TRACE-FAM`.  Those packet families receive no
completion-level promotion and remain `NOT_TESTABLE` where they require the
packet map.

## 4. Exact Route-A tuples

| Candidate | Exact tuple `(A0,A1,A2,A3,A4)` | Overall | Typed result |
|---|---|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | actual packet/clock source relation passes; analytic packet branch is `NOT_TESTABLE` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | actual chosen orbit, LCH/Haar/amenability/full=reduced, but no packet selection or trace amplitude |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | fixed FNS trace is proved; exact dual-Haar averaging erases every nonzero return |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact local repetition ledger; normal extension on the fixed local map is `REFUTED` |
| `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact coefficient-one closed-point/repetition scalar Radon ledger |

### Why the two trace A0 verdicts are weak

The actual source orbit and its clock are genuine, but both local trace
mechanisms compile arbitrary positive clocks.  The trivial character selects
neither a transverse packet measure nor a cross-prime coefficient, and the
regular trace retains only time zero.  Their arithmetic relation is therefore
real but local and generic.  The scalar positive-time record receives
`A0_ANALYTIC_ARITHMETIC_ORIGIN` only because it separately proves the missing
T7 field: one coefficient per actual rational closed point, with `log p`
derived from the source rather than inserted or fitted.

### Why the regular trace has `A1_FAIL`

The regular trace is mathematically stronger as a normal/FNS object but weaker
as an orbit ledger.  On its exact bounded `L1` domain,

```text
Tau_L(a_f)=L f(0).
```

Dual Haar kills every `r != 0` coefficient.  Assigning it `A1_PASS` merely
because the underlying groupoid has periodic orbits would import the
groupoid's coordinate into a trace that provably does not see those returns.

## 5. Strongest progress and strongest failures by owner

### Packet action groupoid

Strongest progress: actual source packet/clock ownership, compactness and
second countability, the continuous free `K_p` action, and the intrinsic open
quotient `Q_p` are proved.

Strongest failure: `Gamma_p` Hausdorff/LCH and `Q_p` Hausdorffness are open.
Therefore the frozen standard packet completion, Radon disintegration,
normal packet trace, and local-to-packet same-map bridge cannot yet be
formulated.  This is `NOT_TESTABLE`, not `REFUTED`.

Next smallest test: prove or refute that the restricted diagonal equivalence
relation defining one `Gamma_p` is closed.  Only a positive result reopens the
standard packet LCH/completion branch.

### One-orbit action groupoid

Strongest progress: for every already chosen actual orbit,
`O_x ~= R/(log(p)Z)` is an inherited Hausdorff circle; the groupoid has an
explicit Haar system, is amenable, has full/reduced equality, and satisfies
`A_L ~= C(T) tensor K`.

Strongest failure: the source does not canonically select or aggregate an
orbit inside a packet and the bare groupoid owns no stability/multiplicity
amplitude or determinant.

Next smallest test: classify whether a source-flow-equivariant packet
restriction can aggregate these locally equivalent groupoids without a free
transverse measure or multiplicity.

### Fixed one-orbit regular trace

Strongest progress: the Zak transform identifies the fixed faithful regular
representation and its bicommutant
`L-infinity(T) bar-tensor B(H_0)`; fibrewise operator trace integration is an
exact FNS trace with a proved complex time-kernel domain.

Strongest failure: it is exactly return-blind away from zero, so A1 is
refuted for this owner.

Next smallest test: classify source-flow-equivariant normal tracial weights
on the fixed regular algebra and decide whether return blindness is forced.

### Fixed one-orbit trivial-character trace

Strongest progress: the sourced induction convention, trace-class Floquet
diagonalization, and shifted Poisson formula prove

```text
tau_0(a_f)=L sum_(r in Z) f(rL).
```

The trace is l.s.c., densely defined, semifinite, and nonfaithful.  A full
finite rank-one corner proves that no normal extended-positive extension
exists on the fixed local regular completion.

Strongest failure: the result is local; the singular extensions proved are
corner states only, and packet transport remains unavailable.

Next smallest test: prove or refute a singular extended-positive **tracial**
extension of the full `tau_0` to the fixed `M_L^reg`, separately from the
already proved corner-state extensions.

### Positive-time scalar record

Strongest progress: closed-point counting, source periods, and positive-time
local finiteness prove

```text
Theta_+ = sum_p log(p) sum_(r>=1) delta_(r log(p))
```

as an exact order-zero Radon measure with coefficient one per rational closed
point.

Strongest failure: arbitrary and composite clock controls produce the same
analytic ledger form.  The record is scalar and owns no packet trace, global
operator, determinant, or geometry-sensitive discriminator.

Next smallest test: prove or refute a precisely typed flat/groupoid trace on
the actual source object whose positive-time restriction equals `Theta_+`
without free transverse or cross-prime mass.

## 6. Control and proves-too-much gate

The audit uses the following target-free controls:

- finite character grids and exact modular cancellation;
- nontrivial characters with the active `exp(+ir theta)` phase;
- regular versus trivial-character traces on one common scale;
- zero-time exposure and simultaneous length/probability rescaling;
- trace-finite rank-one-corner peaks and `L-infinity` representative classes;
- singleton and arbitrary transverse probability bases;
- copied components;
- arbitrary proper positive clocks and composite-only clocks; and
- local, finite-prime, and all-prime positive-time domain separation.

The control verdict is `STOP_SCOPED`, not a theorem failure.  It proves that
the isotropy/Poisson and scalar-ledger compilers are generic.  Arithmetic A0
credit survives only where the actual source proves `(p)`, `log p`, and, for
the scalar record, closed-point coefficient one.  The generic mechanism
cannot certify a Riemann determinant or Hilbert--Polya operator.

## 7. YAML artifacts and exact hashes

| YAML | SHA-256 |
|---|---|
| `evaluations/route_a/DEN-EF-PACKET-ACTION-GRPD-P/2026-08-14-stage8.yaml` | `28da284cd0f1be601ded15a24281a5b07937df1fd29ba8551cbf2ab9f6f9d0ee` |
| `evaluations/route_a/DEN-EF-ORBIT-ACTION-GRPD/2026-08-14-stage8.yaml` | `17defc7c1ec088e4aab5b256ec4ee19a6df126d1d3c76b86f191d3c76f5b77b9` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-REG-TRACE/2026-08-14-stage8.yaml` | `51903590ba183daa54029c7977c1a0ba5c2550cf6e685d18ec2a9bb64d5fa333` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE/2026-08-14-stage8.yaml` | `ddade81079ca04fcb652b0fe2810e081775afdb674c83d72c5c0844e61077e1d` |
| `evaluations/route_a/DEN-EF-GRPD-TIME-RETURN-POS/2026-08-14-stage8.yaml` | `d42df1d6dd699665e918efac61d24a38b500c4d7a3e771ef87761fd89616c22a` |

All five files parse with PyYAML.  Their top-level keys match the Route-A
v0.2.0 output schema exactly; all A0--A4, evidence-status, and overall enums
are legal; candidate IDs match their directory names; and every
`route_b_invocation_allowed` value is the Boolean `false`.

## 8. Route-B decision

Route-B entry requires a coherent same-object lift and normally
`ROUTE_A_SUCCESS_ROUTE_B_READY`.  None of the five records has A2, A3, or A4,
and no self-adjoint spectral generator or completed divisor is frozen.
Accordingly:

```text
Route B invocation: false
Route-B YAML: absent by design
Hilbert--Polya claim: forbidden
```

This is not a limited Route-B audit.  It is the formal decision that Route B
must not be used to rescue the present exploratory records.
