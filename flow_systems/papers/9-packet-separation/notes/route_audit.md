# Paper 9 formal Route-A audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Evaluator: `route-a-evaluator` v0.2.0, with the Route-B same-object entry rule
applied  
Decision: **eight object-specific `ROUTE_A_EXPLORATORY` evaluations; Route B
not invoked**

## 1. Executive decision

Paper 9 closes the topology question without closing an analytic Route-A
layer.  For every rational prime `p`, the actual inherited packet `Gamma_p`,
every actual inherited orbit, and the intrinsic quotient `Q_p` are nontrivial
indiscrete spaces.  The restricted packet orbit relation is not closed.

That result has four different Route consequences which must remain typed:

1. The actual packet and actual inherited-orbit **topology owners** retain
   genuine source arithmetic and an exact set-level clock/repetition relation,
   but only `A1_WEAK`.
2. The frozen actual packet and actual-orbit **standard LCH-Hausdorff
   groupoid branches** are `A1_FAIL`: their Hausdorff unit-space prerequisite
   is refuted before Haar, completion, representation, or trace transport.
3. The bare quotient `Q_p=Gamma_p/K_p` has only
   `A0_WEAK_ARITHMETIC_RELATION` and `A1_FAIL`.  It is source-derived, but it
   has divided out the time orbit and owns no primitive-period ledger.
4. Paper 8's circle-groupoid, regular-trace, and trivial-character-trace
   calculations survive only after explicit retyping to standard-circle
   proxy owners.  The proxy trivial-character trace retains
   `A1_PASS_ANALYTIC`; the proxy regular trace remains `A1_FAIL` because it
   cancels every nonzero return.

All eight records have `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`, overall
`ROUTE_A_EXPLORATORY`, and Boolean
`route_b_invocation_allowed: false`.  No Route-B YAML is created.

The independent positive-time scalar record
`DEN-EF-GRPD-TIME-RETURN-POS` is unchanged.  Its immutable Stage-8 YAML is not
reissued at Stage 9 and lends no topology, groupoid, trace, determinant, or
Route coordinate to these eight records.

## 2. Exact evidence lock

The Route decision is bound to the following final Paper-9 evidence:

| Artifact | SHA-256 | Audit use |
|---|---|---|
| `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | final `CONFIRM_STRONG` proof, correction matrix, and Route ceiling |
| `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | exact source ownership and no-topology-promotion boundary |
| `results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` | deterministic control and implementation lock |

The final proof audit reports `0 Critical / 0 Major / 0 Minor`.  The control
manifest contains eight CSV artifacts and 240 data rows.  During this Route
audit, the non-writing verification path passed all recorded hashes, sizes,
row counts, metrics, active-lock hashes, and implementation hashes.  The unit
suite passed `20/20`.  These finite executions are regression evidence only;
the topology and ownership verdicts come from the symbolic proof audit.

The affected immutable Stage-8 Route records are:

| Historical YAML | SHA-256 |
|---|---|
| `evaluations/route_a/DEN-EF-PACKET-ACTION-GRPD-P/2026-08-14-stage8.yaml` | `28da284cd0f1be601ded15a24281a5b07937df1fd29ba8551cbf2ab9f6f9d0ee` |
| `evaluations/route_a/DEN-EF-ORBIT-ACTION-GRPD/2026-08-14-stage8.yaml` | `17defc7c1ec088e4aab5b256ec4ee19a6df126d1d3c76b86f191d3c76f5b77b9` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-REG-TRACE/2026-08-14-stage8.yaml` | `51903590ba183daa54029c7977c1a0ba5c2550cf6e685d18ec2a9bb64d5fa333` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE/2026-08-14-stage8.yaml` | `ddade81079ca04fcb652b0fe2810e081775afdb674c83d72c5c0844e61077e1d` |
| `evaluations/route_a/DEN-EF-GRPD-TIME-RETURN-POS/2026-08-14-stage8.yaml` | `d42df1d6dd699665e918efac61d24a38b500c4d7a3e771ef87761fd89616c22a` |

Paper 8's internal proxy mathematics is additionally pinned by
`papers/8-isotropy-trace/notes/phase3_operator_proofs.md`, SHA-256
`5e8fd6cd400c7300da5c80e8991b3770ad03c9026a236caab04642cd96314a26`.
Paper 9 changes its owner attribution, not its internal standard-circle
calculations.

## 3. Exact Route-A tuples

| Candidate | Exact tuple `(A0,A1,A2,A3,A4)` | Overall |
|---|---|---|
| `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |

## 4. Typed verdict rationale

### Actual topology owners

`DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P` owns the exact inherited topology of
`Gamma_p`.  Its source closed point `(p)`, packet, stabilizer `p^Z`, clock
`log p`, and repetitions are intrinsic, so A0 remains analytic and A1 remains
weak.  The inherited topology is nevertheless indiscrete and supplies no
separated primitive circles, stability, multiplicity, phase, or amplitude.

`DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` owns the corresponding subspace theorem
for each actual orbit.  The orbit set is `R_{>0}/p^Z` with exact set period
`log p`, but its inherited topology is nontrivial indiscrete, not the ordinary
Hausdorff-circle topology.  No circle Haar measure or completion travels from
the standard proxy to this owner.

### Bare quotient owner

`DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P` owns the intrinsic quotient topology and
the set model `U_p/H_p`.  Its arithmetic relation is real but weak: after the
`K_p` quotient, all time orbits are trivial.  A1 therefore fails for this
bare quotient.  The proof refutes a topological identification with the
standard compact-Hausdorff `B_p` model; it does not deny the proved bare set
description.

### Actual standard-LCH branches

`DEN-EF-PACKET-ACTION-GRPD-P` and `DEN-EF-ORBIT-ACTION-GRPD` retain their
source labels, action sign, stabilizer, and clock at A0.  They receive
`A1_FAIL` because the unit spaces are non-Hausdorff, so the frozen standard
LCH-Hausdorff action-groupoid route fails at its prerequisite.  This is not a
universal no-go for every future non-Hausdorff groupoid or completion theory;
such a construction would require a new lock and evaluation.

### Standard-circle proxy owners

The bare `DEN-EF-ORBIT-STD-CIRCLE-PROXY` is a modeling-choice Hausdorff circle
with copied label `p` and clock `log p`.  Its generic circle orbit/groupoid
theorem gives only A0 weak and A1 weak.

On its fixed regular completion, the proxy FNS trace satisfies

```text
Tau_L(a_f)=L f(0).
```

It erases every nonzero return, so the separately typed regular-trace owner
has `A1_FAIL`.

For the proxy trivial-character owner, shifted Poisson summation proves

```text
tau_0(a_f)=L sum_(r in Z) f(rL).
```

That exact proxy repetition comb earns `A1_PASS_ANALYTIC`.  It does not
restore actual inherited topology or establish an actual-source completion,
trace, or normal-extension claim.

## 5. Supersession and retyping ledger

| Stage-8 statement/record | Stage-9 action | Exact boundary |
|---|---|---|
| actual packet standard-LCH branch, `DEN-EF-PACKET-ACTION-GRPD-P` | **SUPERSEDES** with the same ID | A1 changes from weak/open to fail at the proved topology prerequisite; source packet/action/clock survive |
| actual orbit standard-LCH branch, `DEN-EF-ORBIT-ACTION-GRPD` | **SUPERSEDES** with the same ID | inherited Hausdorff-circle/LCH ownership is refuted; the set action and clock survive |
| bare actual-orbit circle/groupoid calculations | **RETYPES** to `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | standard-circle LCH/Haar/completion mathematics survives on a modeling proxy only |
| Stage-8 regular trace `DEN-EF-ORBIT-GRPD-REG-TRACE` | **RETYPES** to `DEN-EF-ORBIT-STD-CIRCLE-PROXY-REG-TRACE` | FNS formula survives; Stage-8 actual-owner attribution is refuted; future non-Hausdorff transport remains untested |
| Stage-8 trivial-character trace `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | **RETYPES** to `DEN-EF-ORBIT-STD-CIRCLE-PROXY-TRIVCHAR-TRACE` | Poisson/trace and fixed-proxy-map obstruction survive; no actual-source trace or normal-extension statement survives |
| coefficient-one positive-time scalar `DEN-EF-GRPD-TIME-RETURN-POS` | **UNCHANGED; NO REISSUE** | its typed scalar A0/A1 theorem remains Stage 8 and cannot be spliced into a packet/proxy analytic owner |

The two new topology-owner records isolate what Paper 9 actually proves from
the failed standard-LCH branches.  Historical Stage-8 bytes are not edited.

## 6. A2--A4 and Route-B ceiling

No Stage-9 object defines a dynamical zeta function, Fredholm determinant,
trace-log determinant, divisor comparison, or train/validation/test zero
protocol.  Every A2 verdict is therefore `A2_FAIL`, with all nine mandatory
metrics explicitly marked not applicable rather than populated with invented
numbers.

No object supplies analytic continuation, functional equation, Gamma factor,
completed divisor, Riemann--von Mangoldt law, or intrinsic Weil compression;
every A3 verdict is `A3_FAIL`.  No object supplies a natural quantization,
self-adjoint generator/domain, scattering completion, or spectral-parameter
map; every A4 verdict is `A4_FAIL`.

Accordingly:

```text
Route B invocation: false
Route-B YAML: absent by design
Hilbert--Polya claim: forbidden
```

## 7. Adversarial and anti-splice gate

The decisive controls are the exact actual/proxy owner split, the ordinary
`p^Z` Hausdorff-circle negative control, simultaneous real/profinite
approximation with finite-kernel endpoint checks, the frozen inverse action
sign, distinctness modulo `p^Z` and `H_p`, unrelated quotient controls,
arbitrary/composite clocks, regular-versus-trivial-character comparison, and
zero-time exposure.

The verdict is `STOP_SCOPED`: the indiscreteness theorem is specific to the
frozen rational-Witt `E_f` packet and exact diagonal channel, while the proxy
circle/trace compilers work for generic positive clocks.  Neither mechanism
establishes a Riemann determinant.  Coordinates may not be combined as

```text
actual-source A0 + proxy trivial-character A1 + scalar Theta_+ A1.
```

Those coordinates have different typed owners.

## 8. Stage-9 YAML artifacts and hashes

| YAML | SHA-256 |
|---|---|
| `evaluations/route_a/DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P/2026-08-14-stage9.yaml` | `e28e139acd07c5b10b689741b7f3c2980b818bcf0932efc85efa92f12b57e42b` |
| `evaluations/route_a/DEN-EF-ORBIT-INHERITED-TOPOLOGY-P/2026-08-14-stage9.yaml` | `fe873616f6370539b7b7ce594127a0c8b4925ffc5981c621cc6e91c0d431d291` |
| `evaluations/route_a/DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P/2026-08-14-stage9.yaml` | `e527a694e6e767beb7739239dbdcda75204d14e2c9699d95103ff6be9a7e1c11` |
| `evaluations/route_a/DEN-EF-PACKET-ACTION-GRPD-P/2026-08-14-stage9.yaml` | `05f3331835a85ba786aaa1e4178f9f6d49e8e588c0c5038453a9bda5758c7422` |
| `evaluations/route_a/DEN-EF-ORBIT-ACTION-GRPD/2026-08-14-stage9.yaml` | `3e563c5c5a4540df490ab5f3f06091adfd4d04f9fab742339a4d2d9dcdbe91c8` |
| `evaluations/route_a/DEN-EF-ORBIT-STD-CIRCLE-PROXY/2026-08-14-stage9.yaml` | `8e6652a1c0c817033b61c0e11e27fb0b310f3ffb7912eb30d749d7770b338285` |
| `evaluations/route_a/DEN-EF-ORBIT-STD-CIRCLE-PROXY-REG-TRACE/2026-08-14-stage9.yaml` | `5b4f69ffbf961b5b1a7e3f0e5d55a08d9d99f017c7cb25e4b0b3cc516a944f71` |
| `evaluations/route_a/DEN-EF-ORBIT-STD-CIRCLE-PROXY-TRIVCHAR-TRACE/2026-08-14-stage9.yaml` | `877988ac4ae361480eae2b89687ef39f13e957ac2f20ded52f01a212c62c8caa` |

## 9. Mechanical validation gate

All eight YAML files parse with PyYAML.  Their top-level and nested keys match
the Route-A v0.2.0/Stage-8 output schema exactly.  Every A0--A4,
evidence-status, adversarial-control, and overall enum is legal.  Each
candidate ID matches its directory; each A2 block contains all nine mandatory
metrics; all A2--A4 verdicts are the exact `FAIL` enums; all overall verdicts
are `ROUTE_A_EXPLORATORY`; and every `route_b_invocation_allowed` value is the
Boolean `false`.  Exactly eight Stage-9 Route-A YAMLs and no Stage-9 Route-B
YAML are present.
