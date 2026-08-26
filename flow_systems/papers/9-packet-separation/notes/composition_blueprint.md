# Paper 9 composition blueprint

Blueprint date: **2026-08-14 (Asia/Shanghai)**  
Status: **READY FOR MANUSCRIPT DRAFTING**  
Composition scope: one theorem paper plus an explicit Paper-8 corrigendum; no
new theorem, experiment, Route verdict, or historical-file mutation is
authorized by this blueprint.

## 1. Exact evidence lock

The manuscript must be composed from the following exact bytes.

| Artifact | SHA-256 | Ownership |
|---|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` | scope and stop rules |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` | frozen object and targets |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` | corrected exact design |
| `notes/phase1_amended_relock.md` | `0e18c1de19a56c988ae17a88859493a238291a2264c012dc09d4e77db688e346` | independent amended re-lock |
| `notes/phase1_methodology_relock.md` | `936b17eb465697414371dd95b691ee9179d2706496e6303b868e366ab97cb88b` | methodology re-lock |
| `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | source locators and ownership ceilings |
| `notes/sources/paper9_source_manifest.md` | `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906` | retained-source ledger |
| `notes/sources/paper9_sources.sha256` | `6413af8f2d0afec7158aec123f32a641776edcef0a9a9e747fd0ebc5c5f697e4` | 14/14 source checksum lock |
| `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | final `CONFIRM_STRONG`, 0 C / 0 M / 0 m |
| `notes/phase3_peer_review.md` | `447a6d575a27c87e3874591dfa3eae5f71ea1714819ada43263ffac44c53a678` | independent `PASS`, 0 C / 0 M / 0 m; drafting authorized |
| `results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` | 20/20 tests, 8 CSVs, 240 rows |
| `notes/route_audit.md` | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` | final eight-object Route-A audit |

Any later mathematical change requires a new proof review and a new blueprint
hash. Cosmetic prose edits may not enlarge the claim ledger below.

## 2. Title, contribution, and abstract contract

### Recommended title

**Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous
Approximation and a Topological Corrigendum**

Short alternative: **Simultaneous Approximation and Indiscrete Deninger Prime
Packets**.

### One-sentence contribution

For each rational prime `p`, constructive simultaneous real/profinite
approximation and fixed-stage finite-kernel character convergence show that
every point of Deninger's genuine rational-Witt `E_f` prime packet specializes
to every other point, so the packet, each inherited orbit, and its orbit
quotient are nontrivial indiscrete spaces and the restricted orbit relation is
not closed; this forces an exact retyping of Paper 8's Hausdorff-circle claims.

### Abstract order

1. State the topology gap: Deninger's coordinates are equivariant set
   bijections, not inherited-topology homeomorphisms in general.
2. Freeze the exact fixed-prime `E_f` packet and its restricted quotient
   topology.
3. State the constructive diagonal density theorem in
   `R_{>0} x A_p` and the fixed-stage convergence lemma.
4. State the universal constant-class convergence theorem and its three
   indiscreteness consequences.
5. State nonclosedness of the restricted relation and the corrected
   naive-adelic/Morishita comparison.
6. Give the precise ceiling: the intrinsic scaling-topos circle and an
   explicitly retopologized standard-circle proxy remain different objects;
   no general non-Hausdorff groupoid or spectral no-go is proved.

Suggested keywords: arithmetic dynamics; rational Witt vectors; suspension
quotient; simultaneous approximation; indiscrete topology; nonclosed orbit
relation; Deninger flow; arithmetic site.

## 3. Claim ledger

Only the following claims may appear as results of Paper 9.

| ID | Claim | Status / owner |
|---|---|---|
| C-01 | The global suspension quotient is open, and restriction to the saturated fixed-prime prepacket gives exactly the inherited quotient topology on `Gamma_p`. | proved, actual source |
| C-02 | `D_p=Z[1/p]_{>0}` is dense diagonally in `R_{>0} x A_p`, with an explicit positive CRT sequence. | proved |
| C-03 | For unit endpoints, the associated finite-kernel characters converge pointwise inside one fixed raw `E_f` fibre, then through the named Galois quotient and initial colimit inclusion. | proved on exact domain |
| C-04 | Every packet class has a unit-exponent representative. | proved; set/action input only |
| C-05 | Normalized representatives are equivalent exactly modulo `H_p=p^{Zhat}` and `p^Z`; hence the displayed product is a set model, not a topological product theorem. | proved |
| C-06 | For arbitrary ordered `x,y in Gamma_p`, the constant sequence at `x` converges to `y`. | main theorem |
| C-07 | `Gamma_p` is nontrivial indiscrete, hence non-`T0`, non-`T1`, and non-Hausdorff. | main corollary |
| C-08 | Every actual inherited periodic orbit is a nontrivial indiscrete subspace, despite its set period `log p`. | main corollary |
| C-09 | `Q_p=Gamma_p/K_p` is nontrivial indiscrete and set-theoretically `U_p/H_p`; it is not thereby the standard topological group `B_p`. | main corollary |
| C-10 | The exact restricted orbit relation `R_p` is not closed, by an explicit convergent sequence of related pairs. | proved |
| C-11 | Deninger's product/circle coordinate maps remain valid as set/action parametrizations but are not homeomorphisms to the standard Hausdorff models. | consequence |
| C-12 | The naive inherited adelic prime orbit in `Q^x\A_Q/Zhat^x`, with the exact double-quotient subspace topology, is nontrivial indiscrete. | proved on named naive object |
| C-13 | After finite-kernel nonvanishing and unit normalization are repaired, Morishita's actual-to-actual orbit map is a homeomorphism between indiscrete spaces, not Hausdorff circles. | proved on exact `E_f` domain |
| C-14 | Connes--Consani's intrinsic scaling-topos `C_p` remains an ordinary Hausdorff circle on its own topology; no topology is transported through the canonical set bijection to the naive quotient. | source-owned distinction |
| C-15 | The actual packet/orbit standard LCH-Hausdorff transformation-groupoid branches fail at the Hausdorff unit-space prerequisite. | proved scoped no-go |
| C-16 | No universal impossibility result is claimed for future non-Hausdorff groupoids, Haar systems, completions, or traces. | mandatory limit |
| C-17 | Paper 8's standard-circle algebraic/Floquet/FNS/character calculations survive only on newly typed proxy owners; actual-source transport is withdrawn. | corrigendum |
| C-18 | The coefficient-one positive-time scalar ledger is unchanged and cannot be spliced into any topology/proxy owner. | preservation boundary |
| C-19 | The finite controls reproduce all recorded residues, convergence, sign, distinctness, and negative controls, but do not prove the infinite topological theorems. | reproducibility boundary |
| C-20 | All eight Stage-9 Route objects remain `ROUTE_A_EXPLORATORY`; all have `A2_FAIL`, `A3_FAIL`, `A4_FAIL`, and Route B is not invoked. | Route ceiling |

Forbidden promotions include: full global-suspension indiscreteness; an
intrinsic topology on `B_p`; a principal bundle or transverse measure; an
actual-source Haar system/completion/trace; a determinant, continuation,
functional equation, quantization, or Hilbert--Polya claim.

## 4. Frozen objects and owner map

Use these types literally and never shorten two different rows to the same
symbol without an immediate qualifier.

| Object | Definition / topology owner | Permitted statement |
|---|---|---|
| `Xcheck=Xcheck_0(C)_{E_f}` | Deninger's finite-kernel rational-Witt pre-suspension space | named source topology and Frobenius action |
| `Y=Xcheck x R_{>0}` | product prequotient | global open quotient argument |
| `Z_p=C_p^{E_f} x R_{>0}` | saturated fixed-prime prepacket | exact restricted relation `R_p` |
| `Gamma_p=rho(Z_p)` | subspace inherited from `Y/Q_{>0}`; equivalently `Z_p/R_p` by C-01 | actual packet theorem |
| actual inherited orbit | orbit subset of `Gamma_p` with subspace topology | indiscrete; set stabilizer `p^Z`, clock `log p` |
| `K_p=R_{>0}/p^Z` | set/action time quotient acting on `Gamma_p` | formation of `Q_p`; not an inherited Hausdorff circle |
| `Q_p=Gamma_p/K_p` | quotient topology | nontrivial indiscrete; set model `U_p/H_p` |
| `C_p^{naive}` | prime orbit subspace of `Q^x\A_Q/Zhat^x` with double-quotient topology | actual naive-adelic indiscreteness |
| `CC-SCALING-Cp` | intrinsic scaling-topos point subspace | source-owned Hausdorff circle only |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | ordinary Hausdorff circle introduced by modeling choice | proxy groupoid/Floquet calculations only |
| proxy regular trace | fixed regular completion on the standard-circle proxy | `Tau_L(a_f)=L f(0)`; nonzero returns erased |
| proxy trivial-character trace | fixed character completion on the standard-circle proxy | `tau_0(a_f)=L sum_{r in Z} f(rL)`; proxy comb only |

Notation to freeze in Section 2 of the manuscript:

```text
A_p = product_{ell != p} Z_ell,   U_p=A_p^x,
H_p=p^{Zhat} subset U_p,          D_p=Z[1/p]_{>0},
(P,u)q=(F_qP,q^{-1}u),            rho_p:Z_p -> Gamma_p.
```

Keep raw character points `Ptilde_a`, Galois-orbit points `P_a`, and colimit
points `j(P_a)` distinct. The equality for `F_{m/p^k}` at the Galois/packet
level must never be printed as an equality of raw characters.

## 5. Theorem order and proof dependencies

The manuscript should present the shortest dependency chain below.

1. **Restricted quotient lemma.** Prove openness of `rho`, saturation of
   `Z_p`, and the homeomorphism `Z_p/R_p -> Gamma_p`.
2. **Simultaneous approximation theorem.** Construct
   `q_j=m_j/p^{k_j}` using cofinal prime-to-`p` moduli `M_j`; impose the
   residue on `q_j`, not merely on `m_j`.
3. **Fixed-stage convergence lemma.** Prove finite kernels of all
   approximants, eventual equality on each finite-order element, and legal
   passage through the continuous quotient/inclusion maps.
4. **Normalization and equivalence lemmas.** Exhaust the packet by unit
   exponents and identify equality exactly modulo `H_p` and `p^Z`.
5. **Universal specialization theorem.** Given
   `x=[j(P_b),u]`, `y=[j(P_a),v]`, choose real target `u/v` and profinite
   target `ab^{-1}`; a single orbit-class sequence in `Z_p` converges to a
   representative of `y`.
6. **Indiscreteness corollaries.** Treat `Gamma_p`, every inherited orbit,
   and `Q_p`; prove nontriviality separately before asserting separation
   failures.
7. **Nonclosed-relation theorem.** Use profinite target `1` and
   `u/v notin p^Z` to exhibit a limit outside `R_p`.
8. **Comparison theorem.** Separate Deninger set coordinates, naive adelic
   `C_p`, intrinsic scaling `C_p`, and the standard-circle proxy; then repair
   the Morishita map on the exact `E_f` domain.
9. **Scoped groupoid corollary and corrigendum.** Refute only the frozen
   standard LCH-Hausdorff branch and retype Paper-8 computations.

The universal-specialization proof is the center of the paper. Source review,
controls, and Route evaluation support it but must not interrupt that proof
chain.

## 6. Manuscript architecture

Target length: **7,500--9,000 words**, excluding references and appendices.

| Section | Purpose | Main content |
|---|---|---|
| 1. Introduction | state gap, result, novelty, and limits | no literature chronology longer than needed |
| 2. Exact source object and quotient topology | freeze notation and C-01 | distinguish set bijection from homeomorphism |
| 3. Simultaneous approximation in the fixed-prime channel | prove C-02 | constructive CRT proof plus negative control |
| 4. Finite-kernel convergence and normalization | prove C-03--C-05 | fixed-stage and quotient-level discipline |
| 5. Indiscrete packets and nonclosed relations | prove C-06--C-10 | main theorem, corollaries, separation ledger |
| 6. Adelic comparison and topology ownership | prove/clarify C-11--C-14 | Deninger/Morishita/Connes--Consani split |
| 7. Consequences for Paper 8 and Route A | C-15--C-18 and exact retyping | no historical bytes edited |
| 8. Reproducibility, controls, and limitations | C-19--C-20 | finite-control boundary and Route ceiling |
| 9. Conclusion | one theorem, one correction, one future direction | no new claim |

Put long hash ledgers, full control tables, and the versioned corrigendum in
appendices or supplementary material if journal length requires it. Keep the
main proof self-contained.

## 7. Paper-8 corrigendum matrix

Historical Paper-8 files remain immutable. Cite the failed premise at
`phase2_source_topology_audit.md:203-239` (especially `:232-239`) and its
propagation at `phase3_topology_ownership_proofs.md:65-70,82-102` and
`proof_audit.md:74-80,84-99,464-473`.

| Paper-8 statement/branch | Paper-9 correction | What survives |
|---|---|---|
| actual inherited orbit is a compact Hausdorff standard circle | **REFUTED**: it is nontrivial indiscrete | orbit set, `p^Z`, action sign, label `(p)`, clock `log p` |
| actual one-orbit standard LCH-Hausdorff groupoid | **REFUTED at topology prerequisite** | abstract formulas only after explicit proxy retyping |
| P8-2--P8-6 owned by the actual orbit | **OWNER ATTRIBUTION SUPERSEDED** | internal standard-circle theorems on `DEN-EF-ORBIT-STD-CIRCLE-PROXY` |
| regular trace on actual orbit | **RETYPED TO PROXY** | FNS formula `L f(0)`; actual-source transport withheld |
| trivial-character trace on actual orbit | **RETYPED TO PROXY** | shifted-Poisson comb on fixed proxy only |
| proxy no-normal-extension theorem | **PRESERVED ON PROXY** | exact proxy corner/representation statement only |
| packet standard LCH-Hausdorff groupoid | **REFUTED at topology gate** | no universal non-Hausdorff no-go |
| `Q_p` quotient properties | **PRESERVED AND SHARPENED** | exact quotient is nontrivial indiscrete; no `B_p` promotion |
| actual packet normal extension | **REMAINS NOT_TESTABLE** | no analytic refutation inferred |
| positive-time scalar Radon ledger | **UNCHANGED; NO REISSUE** | independent typed scalar statement only |

Use “corrigendum” for the topology/owner attribution and “retyping” for the
surviving proxy calculations. Do not say Paper 8's internal circle algebra
was disproved.

## 8. Route tuples and immutable Stage-9 records

All rows have overall verdict `ROUTE_A_EXPLORATORY`, `A2_FAIL`, `A3_FAIL`,
`A4_FAIL`, and Boolean `route_b_invocation_allowed: false`.

| Candidate | Exact `(A0,A1,A2,A3,A4)` tuple | YAML SHA-256 |
|---|---|---|
| `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `e28e139acd07c5b10b689741b7f3c2980b818bcf0932efc85efa92f12b57e42b` |
| `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `fe873616f6370539b7b7ce594127a0c8b4925ffc5981c621cc6e91c0d431d291` |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `e527a694e6e767beb7739239dbdcda75204d14e2c9699d95103ff6be9a7e1c11` |
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `05f3331835a85ba786aaa1e4178f9f6d49e8e588c0c5038453a9bda5758c7422` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `3e563c5c5a4540df490ab5f3f06091adfd4d04f9fab742339a4d2d9dcdbe91c8` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `8e6652a1c0c817033b61c0e11e27fb0b310f3ffb7912eb30d749d7770b338285` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `5b4f69ffbf961b5b1a7e3f0e5d55a08d9d99f017c7cb25e4b0b3cc516a944f71` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `877988ac4ae361480eae2b89687ef39f13e957ac2f20ded52f01a212c62c8caa` |

There is no Stage-9 Route-B YAML. The Stage-8 positive-time scalar record is
not reissued. The manuscript must not splice actual-source A0, proxy A1, and
the scalar ledger into a synthetic stronger candidate.

## 9. Source and citation plan

Use primary sources for mathematical ownership; the exact retained files and
locators are in `source_audit.md` and its 14/14 checksum ledger.

| Source | Required use | Exact locator / restriction |
|---|---|---|
| C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4 | primary source for finite-kernel parametrization, action, stabilizer, and topology | p. 32 Eqs. (35),(38); p. 33 Eq. (39); pp. 38--39 Thm. 6.1; p. 43 Prop. 7.4; pp. 44--47 Props./Cors. 7.6--7.9 and Thm. 7.10 + Remark 2; do not promote bijections to homeomorphisms |
| C. Deninger, survey, arXiv:2301.11643v1 | compactness and explicit inverse-continuity warning | pp. 11--13; “compact” is not “compact Hausdorff” |
| M. Morishita, arXiv:2508.15971v5 | adelic target, continuity, anti-equivariance, orbitwise surjectivity after repair | p. 5 Eq. (1.1.5); pp. 23--25 Lemmas 3.4--3.5, Thm. 3.6; disclose full-character/finite-kernel mismatch |
| A. Connes and C. Consani, *The scaling site* (2016) | intrinsic scaling-topos circle | Lemma 6.3(i); ownership stays intrinsic |
| Connes--Consani, arXiv:2501.06560v1 | natural adelic quotient and mapping-torus context | p. 9 and pp. 11--12 Prop. 3.4; canonical bijection is not a global topology-transfer theorem |
| L. Le Bruyn, *The sieve topology on the arithmetic site*, J. Algebra Appl. 15 (2016), 1650020 | unrelated coarse-but-nonindiscrete negative control | Thm. 1; cite DOI `10.1142/S0219498816500201`; exclude corrected arXiv claim |
| D. Jüstel, *The Zak transform on strongly proper G-spaces and its applications*, arXiv:1605.05168v2 | conditional lcH/proper disintegration ceiling | Def. 2.1, Lemma 2.3, Thm. 2.4; hypotheses fail for actual packet |

Novelty wording: “No verified primary source in the bounded search states the
non-`T0`/indiscrete theorem for this exact fixed-prime `E_f` packet.” Do not
claim exhaustive global priority.

## 10. Controls and reproducibility

Bind the reproducibility statement to manifest
`52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`:

- unit suite: **20/20**;
- artifacts: **8 CSV files / 240 data rows**;
- verify-only: all hashes, sizes, row counts, metrics, active-lock hashes, and
  implementation hashes pass, and no artifact is rewritten;
- recorded maxima: real error `6.5383536556262208e-06`, finite-character
  error `0`, correct-time error `7.7964676432670538e-05`.

| CSV | Rows | SHA-256 |
|---|---:|---|
| simultaneous approximation | 25 | `78828e25c9480ebfa30913e4498763d2d5ae63dce9c51a305978cccca6d9d4c4` |
| finite characters | 75 | `2887308b486f6f4286d6ea66d97725df7acf758bfed7d8c1efe7f8918b5965a8` |
| action/sign | 25 | `f2244a35f6c1509c61fe1ace0230f35300e7e0638891d64ae811ae1ba64ac508` |
| `p^Z` circle negative control | 5 | `d9d71d4a811c2809ec74dadebf1d6a6440d901c70c3d6e2054ebafc667cb07a3` |
| unit normalization | 20 | `4432d72b5651b34e42bdc82ead24718cce5cc1a9004686693682ad493ca542a7` |
| distinctness | 15 | `467e15bce32904b94afa73c574a08e3fc98daf934b2b9830d4a478b14eccf844` |
| illegal-kernel/domain controls | 70 | `e9765f4bdb86ff1b21b5cb9aaa9912e70968bbefa2666239d6ed2b4d98264d35` |
| prime summary | 5 | `2560752144246a4580518f3cd1f76b97b173eb0bffeb258d0aa539778ec243a6` |

Explicitly state that the generator is implementation support and
`--verify-only` is a tamper/regression check. Neither mode proves density,
quotient topology, indiscreteness, nonclosedness, corrigendum ownership, or a
Route verdict; those are symbolic results.

## 11. Figures and tables

Use no decorative figure. Two compact vector figures materially clarify the
argument:

1. **Constant-class convergence mechanism** (TikZ): display one fixed orbit
   class `[(P_b,u)]`, representatives
   `(F_{q_j}P_b,q_j^{-1}u)`, the two simultaneous limits
   `q_j -> u/v` and `q_j -> ab^{-1}`, and endpoint `(P_a,v)`.
2. **Topology-owner split** (TikZ): branch the actual Deninger inherited
   orbit to indiscrete `C_p^{naive}`, while keeping `CC-SCALING-Cp` and the
   standard-circle proxy in separate boxes; label bridges as set bijection,
   actual homeomorphism, or forbidden topology transport.

Required tables are: main theorem ledger, object/owner map, Paper-8
corrigendum matrix, controls ledger, and eight Route tuples. Avoid screenshots
of code or source PDFs.

## 12. Terminology and integrity guardrails

| Use | Avoid |
|---|---|
| “actual inherited orbit is indiscrete” | “the periodic orbit is not a circle” without specifying topology |
| “ordinary Hausdorff-circle proxy” | “the orbit circle” for both actual and proxy objects |
| “set/action parametrization” | “coordinate homeomorphism” |
| “naive double-quotient subspace” | unqualified “Connes--Consani `C_p`” |
| “standard LCH-Hausdorff branch fails at its prerequisite” | “no groupoid/C*-algebra can exist” |
| “bounded source search found no direct theorem” | “first proof ever” |
| “finite regression controls” | “numerical proof” |

Integrity disclosures required in the manuscript or supplement:

- exact source manifestations and access cutoff;
- no source PDF is modified or licensed for redistribution merely by access;
- no Riemann-zero data, fitted parameter, or external model upload was used;
- no human-subject, animal, clinical, or personal data were used;
- code/data availability must point to the versioned repository artifact and
  exact manifest, not promise an uncreated archive;
- authorship, CRediT roles, conflicts, funding, and acknowledgments require
  human confirmation before submission;
- AI assistance must be disclosed as exact-byte comparison, proof drafting,
  deterministic-control generation, and adversarial review; authors retain
  responsibility for every theorem and citation.

## 13. Release checklist

- [ ] Draft uses the exact object and notation lock in Sections 1 and 4.
- [ ] Every theorem maps to C-01--C-20; no new claim appears in abstract or
      conclusion.
- [ ] The restricted-quotient lemma precedes all packet-topology claims.
- [ ] The CRT congruence is imposed on `q_j=m_j/p^{k_j}`.
- [ ] Fixed-stage, `E_f`, raw/Galois/colimit, action-sign, and stabilizer
      distinctions are explicit.
- [ ] Nontriviality is proved separately for packet, orbit, and `Q_p`.
- [ ] `C_p^{naive}`, `CC-SCALING-Cp`, and the standard-circle proxy are never
      merged.
- [ ] Paper-8 correction uses `REFUTED`, `RETYPED`, `PRESERVED`, and
      `UNCHANGED` exactly as in the matrix.
- [ ] Historical Paper-8 and Stage-8 files remain unedited.
- [ ] All eight Stage-9 YAML hashes and tuples verify; no Route-B YAML exists.
- [ ] Controls are identified as finite regression evidence, not proof.
- [ ] All citations are checked against retained primary-source locators.
- [ ] Figures and tables carry explicit object owners in captions.
- [ ] Abstract, title, conclusion, and any press-style summary repeat the
      scoped no-go and no-spectral-claim boundary.
- [ ] Phase-3 peer-review hash remains stable; final manuscript and
      citation/integrity review reports no unresolved Critical or Major
      finding.
- [ ] Repository release, DOI/archive, license, authorship, conflicts, and
      funding statements receive human approval.

## 14. Manuscript handoff

The drafting agent should read, in order:

1. this blueprint;
2. `notes/phase3_peer_review.md` for the independent claim-envelope gate;
3. `notes/proof_audit.md` for theorem text and all countercontrols;
4. `notes/source_audit.md` plus the source manifest for exact citations;
5. `notes/route_audit.md` for typed Route language;
6. `results/packet_separation_manifest.json` for reproducibility statements;
7. Paper 8's locked proof and topology audits only when writing the
   corrigendum matrix.

Draft the main proof from the proof audit rather than paraphrasing the Route
YAMLs. Keep citations adjacent to source-owned inputs and label new arguments
as Paper-9 proofs. Manuscript drafting may begin from this blueprint; public
release remains conditioned on the checklist above and any later independent
review artifact must be added by a versioned re-lock, not silently inserted.

## 15. Composition disclosure

This blueprint was AI-assisted under the ARS research-integrity workflow. It
binds claims to exact-byte proof, source, control, and Route audits; creates no
new mathematical evidence; edits no active lock, source artifact, historical
Paper-8 record, Route YAML, or manuscript; and transfers final scientific and
publication responsibility to the human authors.
