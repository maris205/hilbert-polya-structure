# Paper 9 Phase-3 independent mathematical and reproducibility peer review

Review date: **2026-08-14 (Asia/Shanghai)**  
Review role: **independent Phase-3 methodology/domain/reproducibility gate**  
ARS basis: `academic-research-suite` paper-review and reproducibility-audit
workflows  
Write boundary: this review created this file only; it did not edit any lock,
proof, source, control, result, registry, or Route artifact.

## 1. Verdict

**PASS — manuscript drafting is authorized inside the scoped claim envelope.**

Finding count:

```text
Critical: 0
Major:    0
Minor:    0
```

The final proof establishes `CONFIRM_STRONG` for the frozen Paper-9 object:
for every rational prime `p`, the actual inherited packet `Gamma_p`, each of
its actual inherited periodic orbits, and the nontrivial orbit quotient `Q_p`
are indiscrete; the restricted orbit relation is not closed.  The result is
uniform in `p`, but it is not a classification of the global suspension or of
unrelated adelic quotients.

The decisive correction is an object-level one.  The inherited orbit is a
nontrivial indiscrete space, whereas the intrinsic scaling-topos orbit is the
standard Hausdorff circle.  They have the same underlying set model but not
the same topology.  Paper 8's standard-circle operator calculations therefore
survive only as explicitly typed proxy calculations; they do not become
actual-source packet/orbit calculations.

## 2. Exact review snapshot

### 2.1 Active locks and evidence

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` |
| `notes/phase1_amended_relock.md` | `0e18c1de19a56c988ae17a88859493a238291a2264c012dc09d4e77db688e346` |
| `notes/phase1_methodology_relock.md` | `936b17eb465697414371dd95b691ee9179d2706496e6303b868e366ab97cb88b` |
| `notes/phase1_final_gate.md` | `eaa6181f4a4dc3b0ca533a323529bd4c24da237cecf836db9d187726be61bfb1` |
| `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` |
| `notes/sources/paper9_source_manifest.md` | `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906` |
| `notes/sources/paper9_sources.sha256` | `6413af8f2d0afec7158aec123f32a641776edcef0a9a9e747fd0ebc5c5f697e4` |
| `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| `notes/route_audit.md` | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` |

This review binds the final proof-audit SHA beginning `c38c2429`; no
provisional proof version is part of the evidence snapshot.

### 2.2 Control implementation and manifest

| Artifact | SHA-256 |
|---|---|
| `code/README.md` | `de59ced0f408b2b1ec0f8ac088e3aa88dd8290c099a954c1ea53403e1a7801f3` |
| `code/packet_separation_controls.py` | `6a2acfa84c3dbf1b3c8969dfcd2a8cca7fe1db956a80874715c7878ed1d6a6e7` |
| `code/test_packet_separation_controls.py` | `aad1cd822aa2f9febb50794577f6cc71508ad81583601c5d2fe34c7792e29a55` |
| `experiments/README.md` | `78ef60c4daf74e5b48befdb4074fe73b64b7d96636330787e5b382b05d94b965` |
| `experiments/reproduce.sh` | `56520434a8fe450b1e7ea89bb2044a33cb05ba0f77a9545da8dec3b07dd9e14a` |
| `results/README.md` | `b24dc6e429f56e2f482fd0b0ed47fb2828203b22817cde7994ff1f58efd971ea` |
| `results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` |

The eight generated CSVs are bound by the manifest and independently
rehash as follows:

| CSV | SHA-256 |
|---|---|
| `action_sign_controls.csv` | `f2244a35f6c1509c61fe1ace0230f35300e7e0638891d64ae811ae1ba64ac508` |
| `distinctness_controls.csv` | `467e15bce32904b94afa73c574a08e3fc98daf934b2b9830d4a478b14eccf844` |
| `finite_cyclic_characters.csv` | `2887308b486f6f4286d6ea66d97725df7acf758bfed7d8c1efe7f8918b5965a8` |
| `illegal_kernel_proxy.csv` | `e9765f4bdb86ff1b21b5cb9aaa9912e70968bbefa2666239d6ed2b4d98264d35` |
| `prime_uniformity_summary.csv` | `2560752144246a4580518f3cd1f76b97b173eb0bffeb258d0aa539778ec243a6` |
| `pz_circle_controls.csv` | `d9d71d4a811c2809ec74dadebf1d6a6440d901c70c3d6e2054ebafc667cb07a3` |
| `simultaneous_approximation.csv` | `78828e25c9480ebfa30913e4498763d2d5ae63dce9c51a305978cccca6d9d4c4` |
| `unit_normalization_controls.csv` | `4432d72b5651b34e42bdc82ead24718cce5cc1a9004686693682ad493ca542a7` |

## 3. Independent reproducibility receipt

I independently executed `experiments/reproduce.sh` twice from the Paper-9
project, including once after the proof/control binding was final.  Both runs
gave the same receipt:

- unit tests: **20/20 PASS**;
- generated data: **8 CSV files, 240 rows**;
- verify-only gate: hashes, byte sizes, row counts, metrics, active tuple, and
  implementation hashes all passed;
- two independent fresh generations were byte-identical to the checked-in
  artifacts and to one another;
- no cache artifact was left behind;
- source ledger check: **14/14 pinned PDF/preflight entries PASS**.

Recorded finite-control extrema were:

```text
max simultaneous real error       6.5383536556262208e-06
max finite-character value error  0
max correct-action time error      7.7964676432670538e-05
```

These executions establish deterministic regression reproducibility for the
frozen implementation.  They are not statistical inference and are not a
finite proof of density, indiscreteness, nonclosedness, source topology, or
Paper-8 supersession.  Those claims rest on the symbolic proof.

## 4. Independent mathematical adjudication of P9-1--P9-9

| Claim | Independent verdict | Decisive check |
|---|---|---|
| P9-1 | **PROVED** | The positive CRT construction chooses `m_j` in the required residue class modulo `M_j` and nearest to the scaled real target; sufficiently large `p`-power denominator ensures positivity and vanishing real error, while the residue cylinders converge in `A_p`. |
| P9-2 | **PROVED ON THE EXACT DOMAIN** | Each rational approximant has only `p` in its denominator; the numerator's prime-to-`p` part has finite kernel, so every endpoint remains in `E_f`.  Convergence is pointwise in one fixed raw `p`-fibre before passing through the named Galois quotient and colimit inclusion. |
| P9-3 | **PROVED UNIVERSALLY** | For arbitrary `x=[P_b,u]` and `y=[P_a,v]`, the P9-1 sequence targets `(u/v,ab^{-1})`; P9-2 supplies convergence of equivalent representatives to `y`.  No fixed base point is substituted for the universal pair. |
| P9-4 | **CONFIRM_STRONG** | Every singleton closure in `Gamma_p` is the whole packet.  The same holds in every actual inherited orbit and in the quotient `Q_p`; explicit distinctness arguments make all three object types nontrivial. |
| P9-5 | **PROVED WITH THE REQUIRED OBJECT SPLIT** | Deninger product coordinates are set coordinates only; the naive adelic inherited `C_p` is indiscrete, while the intrinsic Connes--Consani/scaling-topos `C_p` is the standard Hausdorff circle.  The corrected Morishita bridge is actual-to-actual on the inherited objects, not a transport to the standard circle. |
| P9-6 | **PROVED NON-CLOSED** | A fixed first coordinate and a sequence of related second coordinates converge to a pair whose time ratio lies outside `p^Z`, giving a limit outside the restricted equivalence relation. |
| P9-7 | **REFUTED AT THE FROZEN PREREQUISITE** | The actual packet and orbit unit spaces are non-Hausdorff, so the frozen standard LCH-Hausdorff groupoid/completion branch cannot start.  The conclusion is not a universal no-go for a newly locked non-Hausdorff theory. |
| P9-8 | **PASS** | Action-sign, finite-kernel, residue, normalization, stabilizer, distinctness, ordinary-circle, proxy, unrelated-object, and prime-uniform controls agree with the analytic proof and expose the intended failure modes. |
| P9-9 | **PASS AS A CORRECTION SPECIFICATION** | Paper 8's exact topology overpromotion is isolated; historical bytes remain immutable; standard-circle/Floquet/FNS/trace/corner results are retyped to proxy owners, while actual-source completion and trace transport remain unproved. |

## 5. Adversarial proof checks

### 5.1 Restricted quotient topology

The global orbit quotient is open because every diagonal action map is a
homeomorphism.  The preimage of the packet is the saturated subspace
`C_p^{E_f} x R_{>0}`.  Restricting the open quotient to this saturated
subspace gives exactly the inherited packet topology.  This closes a common
gap in which a convenient product topology is silently substituted for the
actual quotient topology.

### 5.2 Unit normalization and legal character convergence

Deninger's finite-kernel exponent is normalized by transferring its positive
rational factor to the time coordinate through the exact diagonal action.
After normalization, equality is exhausted by transverse difference in
`H_p=p^{Zhat}` and time ratio in `p^Z`.

The P9-2 convergence argument does not erase a denominator by raw-character
equality.  It first proves that every approximant defines a finite-kernel
character, then checks eventual agreement on each element inside one fixed
raw fibre, and only afterward applies continuous quotient/colimit maps.  This
is the correct order of operations.

### 5.3 Universal quantifier and nontriviality

The proof handles arbitrary `x,y in Gamma_p`; the approximating sequence is
chosen after both points are fixed.  Thus it establishes the universal
specialization statement needed for indiscreteness, rather than only density
of one preferred orbit.

Nontriviality is also separately proved.  Packet/orbit distinctness follows
by choosing a time ratio outside `p^Z`.  For
`Q_p ~= U_p/H_p`, the procyclic group `H_p` has at most one element of order
two, whereas independent sign coordinates at two odd primes give at least
three order-two elements in `U_p`.  Hence `U_p/H_p` is not a singleton.  An
indiscrete quotient is therefore genuinely non-`T0`, non-`T1`, and
non-Hausdorff, not vacuously a one-point space.

### 5.4 Nonclosed relation

With one packet point fixed, choose an unrelated target whose time ratio is
outside `p^Z` and approximate it using the same simultaneous channel.  Every
approximating pair lies in the restricted orbit relation, while the limiting
pair does not.  Both membership and failure of membership use the exhaustive
normalized equivalence criterion, so the nonclosedness conclusion is not a
mere consequence of non-Hausdorffness.

### 5.5 Morishita/Connes--Consani topology split

The naive adelic prime orbit uses the inherited quotient topology.  The
constructed rational rescalings remain in one left `Q^x` class and converge
in the restricted product to the desired unit-normalized target, proving that
this inherited orbit is indiscrete.  Its equality relation is still exactly
the expected set relation modulo `p^Z`.

The intrinsic scaling-topos `C_p` is a different topological object and
retains its standard Hausdorff-circle topology.  Morishita's map, after the
away-from-`p` nonvanishing and stabilizer checks, is a bijection between the
two actual inherited objects; since both are indiscrete it is a homeomorphism
there.  Nothing in that statement identifies either inherited object with
the intrinsic standard circle.

## 6. Paper-8 supersession boundary

The review confirms this exact ledger:

1. The actual packet and actual orbit standard-LCH branches are superseded at
   the Hausdorff unit-space prerequisite.
2. The set action, action sign, stabilizer `p^Z`, primitive clock `log p`, and
   repetitions survive.
3. Standard-circle groupoid, regular-trace, and trivial-character-trace
   calculations survive only under the new proxy-owner IDs.
4. The proxy regular trace still cancels all nonzero returns; the proxy
   trivial-character trace still gives the exact repetition comb on its fixed
   proxy representation.
5. No actual-source completion, Haar system, trace transport, or normal
   extension follows.  Those questions remain `NOT_TESTABLE` under the
   frozen object.
6. The independent positive-time scalar Stage-8 result remains unchanged and
   cannot be coordinate-spliced into an actual packet or proxy analytic
   object.

This is a correction of ownership, not a retroactive alteration of historical
Paper-8 artifacts.

## 7. Route audit

The eight Stage-9 Route-A records and their exact hashes are:

| Candidate | Tuple `(A0,A1,A2,A3,A4)` | SHA-256 |
|---|---|---|
| `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `e28e139acd07c5b10b689741b7f3c2980b818bcf0932efc85efa92f12b57e42b` |
| `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `fe873616f6370539b7b7ce594127a0c8b4925ffc5981c621cc6e91c0d431d291` |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `e527a694e6e767beb7739239dbdcda75204d14e2c9699d95103ff6be9a7e1c11` |
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `05f3331835a85ba786aaa1e4178f9f6d49e8e588c0c5038453a9bda5758c7422` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `3e563c5c5a4540df490ab5f3f06091adfd4d04f9fab742339a4d2d9dcdbe91c8` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `8e6652a1c0c817033b61c0e11e27fb0b310f3ffb7912eb30d749d7770b338285` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `5b4f69ffbf961b5b1a7e3f0e5d55a08d9d99f017c7cb25e4b0b3cc516a944f71` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `877988ac4ae361480eae2b89687ef39f13e957ac2f20ded52f01a212c62c8caa` |

Independent PyYAML validation found **8 Route-A files, 0 validation
errors, and 0 Stage-9 Route-B files**.  The top-level/nested schemas match the
frozen v0.2.0 format; candidate IDs match their directories; A0--A4,
evidence, control, and overall enums are legal; every A2 block has all nine
mandatory metrics; all eight overall verdicts are
`ROUTE_A_EXPLORATORY`; and every `route_b_invocation_allowed` field is the
Boolean `false`.

The `Q_p` record is correctly conservative: the bare quotient has
`A0_WEAK_ARITHMETIC_RELATION`, not an analytic carrier, because quotienting by
the time flow removes the primitive-period ledger.  Its failed topological
identification concerns the standard compact-Hausdorff model; it does not
refute the proved bare set model `U_p/H_p`.

No Stage-9 object supplies a same-object determinant, zero protocol,
continuation/functional equation, completed divisor, Weil compression, or
natural quantization.  Consequently all A2--A4 entries fail and Route B is
correctly not invoked.

## 8. Findings and claim envelope

### Critical findings

None.

### Major findings

None.

### Minor findings

None.

The absence of findings is conditional on retaining the following mandatory
manuscript boundaries:

- say **inherited quotient/subspace topology** whenever discussing
  `Gamma_p`, its actual orbits, `Q_p`, or the naive adelic `C_p`;
- never promote a set bijection, common stabilizer, or common period to a
  homeomorphism with the intrinsic standard circle;
- state the universal quantifier `for every rational prime p` only for the
  frozen rational-Witt `E_f` packet and its exact diagonal channel;
- keep the standard-LCH failure scoped to the frozen actual packet/orbit
  branches; do not claim a universal obstruction to all non-Hausdorff
  groupoid theories;
- describe the deterministic controls as finite regression witnesses, not as
  the proof of the topological theorems;
- retain the actual/proxy/scalar owner split and prohibit cross-object Route
  coordinate splicing;
- make no determinant, Riemann-zero, Route-B, Hilbert--Polya, packet trace, or
  natural spectral-completion claim.

Within those boundaries, the proof, sources, deterministic controls,
Paper-8 correction ledger, and Route records are mutually consistent and
sufficiently reproducible for manuscript drafting.

## 9. Integrity disclosure

This peer review was AI-assisted.  Every mathematical conclusion was checked
against the frozen local proof and primary-source audit; every computational
claim was checked by executing the frozen reproduction entry point; every
reported artifact identifier was independently rehashed; and the Route YAMLs
were parsed and mechanically validated.  No external network data, fitted
target data, or unrecorded numerical evidence was used in the verdict.
