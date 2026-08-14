# Paper 8 Phase-3 composition blueprint

Date: 2026-08-14 (Asia/Shanghai)  
Status: **MANUSCRIPT BLUEPRINT — PROOF/CONTROLS/INTEGRITY/ROUTE SYNCHRONIZED; READY FOR DRAFTING**  
Paper type: theorem, obstruction, and typed-ownership audit  
Main language: English, with an independently written Simplified-Chinese abstract  
Route ceiling: Route A only; A2/A3/A4 failed and Route B closed

This file plans the manuscript.  It does not restate the proofs as a substitute
for `phase3_operator_proofs.md` or
`phase3_topology_ownership_proofs.md`, and it does not alter any lock, Route
record, result, or registry.  Drafting is authorized by
`phase3_peer_review.md`, SHA-256
`572e7852de08ded264f87bb245aff181ae032ed8a8bfdf831fcd4ed5d1f921c3`,
with 0 Critical / 0 Major / 0 Minor findings.

## 1. Paper identity

### 1.1 Recommended working title

> **Isotropy Averaging Erases Returns: Character Traces and a Fixed-Map
> Normality Obstruction on Deninger Prime Orbits**

Shorter alternative:

> **Isotropy Characters and Return Traces on Deninger Prime Orbits**

Avoid “packet trace” in the title: the packet completion is not testable under
the frozen standard LCH hypotheses.  Avoid “singular trace” unless the text
immediately says that Paper 8 proves nonnormality of the full character trace
and constructs singular extensions only for a finite corner state.

### 1.2 Author metadata

Use the established project metadata, subject to final human confirmation:

```text
Liang Wang
School of Artificial Intelligence and Automation
Huazhong University of Science and Technology
Wuhan 430074, P.R. China
wangliang.f@gmail.com
```

### 1.3 Central thesis

The manuscript should lead with this three-level result:

> On every already chosen actual periodic orbit in Deninger's finite-kernel
> `E_f` system, the continuous-time action groupoid has an exact
> isotropy-character decomposition.  Dual-Haar averaging produces a normal
> FNS trace that retains only time zero, whereas each character fibre carries
> a lower-semicontinuous semifinite C*-trace and the trivial fibre retains the
> full repetition comb.  The character trace has no normal extension along
> the fixed regular completion.  This refutes the fixed one-orbit analogue,
> but the packet-level primary question remains `NOT_TESTABLE` because packet
> Hausdorff/LCH topology and the packet same-map bridge are open.  Separately,
> closed-point counting yields an exact locally finite positive-time scalar
> ledger; it is not a packet trace or a global operator.

The first sentence states the positive operator theorem, the second states
the exact negative theorem, and the third prevents the local and scalar
results from being spliced into a packet conclusion.

### 1.4 Proposed abstract claim order

Draft the English and Chinese abstracts independently but preserve this order:

1. **Problem.**  Deninger's `E_f` flow supplies prime packets, exact periods
   `log p`, and common isotropy, but does not supply a packet trace or
   completion-level normality theorem.
2. **Object.**  Restrict to one already chosen actual source orbit
   `O\cong R/(LZ)`, `L=log p`, and construct its action groupoid with the
   frozen Lebesgue Haar convention.
3. **Completion.**  Prove
   `C^*(O\rtimes R)=C_r^*(O\rtimes R)\cong C(T)\otimes K` and identify the
   fixed regular bicommutant by a Zak transform.
4. **Trace dichotomy.**  State exactly
   `T_theta(f)=L sum_r f(rL)e^{ir theta}`,
   the normal dual-Haar value `L f(0)`, and the trivial-character value
   `L sum_r f(rL)`.
5. **Obstruction.**  State that a full finite rank-one corner rules out every
   normal extended-positive extension of the character trace along the fixed
   local map.
6. **Packet boundary.**  State explicitly that the packet-level primary
   outcome is `NOT_TESTABLE`, not refuted.
7. **Scalar result.**  State that positive-time closed-point counting defines
   a locally finite scalar Radon measure with coefficient one per rational
   closed point.
8. **Falsification.**  State that arbitrary and composite clocks preserve the
   analytic compiler, so arithmetic ownership comes from the source labels
   and clocks rather than the local mechanism alone.
9. **Limit.**  State that the paper constructs no packet completion, global
   all-prime operator, determinant, A3 structure, quantization, or Route-B
   object.

Do not put an unbounded novelty statement in the abstract.  If novelty is
mentioned, use the dated search-bound wording in Section 9.4 below.

### 1.5 Keywords

Recommended English keywords:

```text
transformation groupoid; isotropy character; Plancherel trace;
lower-semicontinuous trace; normal extension; Poisson summation;
arithmetic dynamics
```

Recommended Simplified-Chinese keywords should express the same concepts, not
mechanically transliterate the English list.

## 2. Contribution hierarchy and non-contributions

### 2.1 Contributions, in decreasing order of strength

1. **Fixed-map normality obstruction.**  On the represented one-orbit
   completion, the full character trace admits no normal extended-positive
   extension; the proof uses the same finite projection and the same regular
   map.
2. **Exact normal-versus-character trace split.**  The normal regular trace
   erases every nonzero return, while the character fibre retains a
   phase-weighted comb at the same Haar scale.
3. **Concrete representation theorem.**  The locked groupoid convolution,
   unstabilized `C(T) tensor K` completion, induced representations, Zak
   decomposition, bicommutant, and FNS domains are connected on one fixed
   object.
4. **Source-topology split.**  Every actual orbit closes, but the inherited
   packet does not yet close the standard Hausdorff/LCH gate.  This is a
   rigorous `NOT_TESTABLE` boundary rather than a silent proxy replacement.
5. **Typed positive-time scalar ledger.**  Closed-point counting and
   `L_p=log p` give a locally finite Radon measure on `(0,infinity)` without
   asserting an all-prime trace.
6. **Falsification and ownership audit.**  Character, transverse, copy,
   arbitrary-clock, composite-clock, normalization, finite-corner, and domain
   controls show exactly which parts are generic.

### 2.2 Non-contributions to say explicitly

The paper does not prove:

- packet Hausdorffness, packet LCH, or `Q_p` Hausdorffness;
- a packet groupoid C*-completion or packet regular von Neumann algebra;
- a packet Radon-measure disintegration, source-selected transverse
  probability, or packet trace;
- transport of the local finite corner or local obstruction to a packet map;
- one primitive orbit per packet or a source-owned packet-orbit
  multiplicity;
- a global all-prime C*- or `L1` operator;
- any zeta/dynamical/Fredholm/semifinite determinant;
- analytic continuation, functional equation, Gamma factor, completed
  divisor, Weil compression, or zero counting;
- a natural quantization or Hilbert--Polya operator; or
- a universal theorem excluding future packet, cohomological, or groupoid
  repairs.

## 3. Typed object roster

| Candidate ID | Manuscript role | Strongest proved statement | Stop condition |
|---|---|---|---|
| `DEN-WITT-Z-FIN` | source owner | rational closed points, packets, periods, repetitions, finite-kernel topology facts | Deninger does not source-own Paper-8's groupoid or trace |
| `DEN-EF-ORBIT-ACTION-GRPD` | main operator owner | P8-1--P8-6 on one actual chosen orbit | no canonical orbit selection or packet promotion |
| `DEN-EF-PACKET-ACTION-GRPD-P` | primary-question owner | partial topology/action fields only | analytic branch `NOT_TESTABLE` until packet LCH closes |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q` | intrinsic quotient owner | free compact action; open quasi-compact second-countable quotient; continuous-function averaging | not `B_p`; Hausdorff/local-trivial/Radon gates open |
| `DEN-PACKET-PROD-ISO-GRPD` | control proxy only | calculational comparison if used | no source or packet transport |
| `DEN-EF-GRPD-REG-TRACE-FAM` | normal trace owner | local one-orbit FNS trace with value `Lf(0)` | packet branch absent; return-blind away from zero |
| `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` | return-sensitive trace owner | local l.s.c. semifinite nonfaithful C*-trace; no normal extension | no full singular extension or packet trace claimed |
| `DEN-EF-GRPD-TIME-RETURN-LOCAL` | local formula owner | actual-orbit restriction `tau_0(a_f)=R_p(f)` | not a packet trace restriction without packet algebra |
| `DEN-EF-GRPD-TIME-RETURN-FIN` | finite scalar assembly | finite sum over actual prime labels | no global operator |
| `DEN-EF-GRPD-TIME-RETURN-POS` | all-prime scalar owner | locally finite positive-time Radon measure with closed-point coefficient one | not a star-algebra trace or determinant |

Changing the orbit, packet topology, Haar normalization, representation,
completion, character, transverse measure, prime masses, or test domain
creates a new version or candidate.

## 4. Pre-drafting claim manifest

The following list should be treated as the one-shot claim-intent baseline.
New substantive claims introduced during drafting must be added visibly and
reviewed rather than retroactively hidden in this list.

| Claim ID | Intended claim | Evidence kind and owner | Strength | Negative constraint |
|---|---|---|---|---|
| C-01 | Every already chosen actual `E_f` prime orbit is homeomorphic to `R/(log p)Z`. | source-specialized/new topology lemma | proved, one orbit | never call this a packet chart |
| C-02 | Its action groupoid is LCH, second countable, has Lebesgue Haar, is amenable, and has full/reduced equality. | P8-1 local theorem | proved | never borrow packet LCH |
| C-03 | The one-orbit algebra is actually `C(T) tensor K`, not merely Morita equivalent. | Williams theorem plus locked specialization | proved, noncanonical trivialization | do not cancel `K` from stable isomorphism |
| C-04 | The induced sign is `(2pi n-theta)/L` with return phase `exp(+ir theta)`. | P8-2/P8-3 new specialization | proved | frequency and phase signs move together |
| C-05 | `pi_theta(a_f)` is trace class and satisfies shifted Poisson summation. | P8-3 | proved on `C_c^infinity(R)` | controls do not prove it |
| C-06 | The fixed regular bicommutant is `L-infinity(T) bar_tensor B(H_0)`. | Zak/fixed-map P8-4 theorem | proved | not an abstract or packet completion |
| C-07 | The regular trace is FNS and returns `Lf(0)`. | P8-4 | proved at length scale | divide the whole trace by `L` for probability scale |
| C-08 | `tau_theta` is l.s.c., densely defined, semifinite, nonfaithful, unbounded, and gives the phase-weighted comb. | P8-5 | proved C*-trace | do not call it normal in `M_L^reg` |
| C-09 | No normal extended-positive weight on `M_L^reg` extends `tau_theta`. | P8-6 fixed-map corner theorem | proved | local only; no packet refutation |
| C-10 | Distinct singular corner states extend point evaluation. | P8-6.2 | proved for the finite corner | do not call them full trace extensions |
| C-11 | Packet and `Q_p` Hausdorff/LCH and packet same-map transport remain open/not testable. | Phase-2 source gate and P8-1/P8-7 | adjudicated limitation | do not convert to nonexistence |
| C-12 | `Theta_+` is a locally finite positive-time scalar Radon measure. | P8-7 scalar theorem | proved | no global C*/L1 owner |
| C-13 | Coefficient one comes from rational closed-point counting. | T7 scalar ownership | proved for declared scalar assembly | not packet-orbit multiplicity |
| C-14 | Arbitrary/composite clocks preserve the analytic mechanism but fail arithmetic provenance when not source-derived. | P8-8 controls | proved/genericity control | do not infer that actual prime provenance fails |
| C-15 | No direct Deninger-`E_f` fixed-object bridge was located in the documented search. | dated novelty search | `SUPPORTED_WITHIN_SEARCH` | never “first” or “no prior work” absolutely |
| C-16 | All Route conclusions are object-specific and exploratory. | independent Route audit | evaluator-owned | no coordinate splice; no Route B |

## 5. Manuscript architecture

Recommended body length: **9,000--10,500 words**, excluding bibliography,
appendices, and declarations.  A shorter version risks hiding the map/domain
distinctions that make the theorem correct.

| Section | Target words | Purpose | Main claim IDs | Required stop sentence |
|---|---:|---|---|---|
| Title, abstracts, keywords | 250--300 EN plus 300--500 Chinese characters | state the local theorem, packet boundary, and scalar result in parallel | C-01, C-06--C-15 | packet outcome is `NOT_TESTABLE` |
| 1. Introduction | 850 | formulate the source-selected packet question, outcome trichotomy, contribution hierarchy, and non-contributions | C-09, C-11--C-15 | local refutation is not packet refutation |
| 2. Source object and topology split | 1,000 | define `E_f`, `Gamma_p`, actual orbit, `K_p`, `Q_p`; prove/cite the exact orbit bridge and list packet-open gates | C-01, C-02, C-11 | `Q_p` is not `B_p` |
| 3. Locked groupoid and exact completion | 1,200 | state arrows, Haar, convolution, crossed-product conversion, amenability, Williams isomorphism, induced representations | C-02--C-04 | isomorphism/trivialization is one-orbit and choice-dependent |
| 4. Character traces and shifted Poisson formula | 1,000 | diagonalization, trace class, uniform summability, modulation, phase-weighted comb | C-04, C-05, C-08 | C*-trace domain precedes formula |
| 5. Fixed regular trace and isotropy cancellation | 1,150 | Zak unitary, faithfulness, bicommutant, FNS domains, bounded `L1`, Haar cancellation | C-06, C-07 | dual Haar and orbit Haar are not the same measure |
| 6. Finite-corner normality obstruction | 1,050 | centre/corner correction, same projection in fixed map, peak contradiction, separate corner-state extensions | C-09, C-10 | no full singular trace extension is constructed |
| 7. Packet and quotient boundary | 750 | free compact action, quotient properties, continuous-function averaging, unavailable Radon/trace steps | C-11 | primary packet outcome remains not testable |
| 8. Scalar ledgers and falsification controls | 900 | local/finite/positive domains; local finiteness; coefficient ownership; character/transverse/copy/clock/composite controls | C-12--C-14 | positive-time object is scalar, not operator |
| 9. Same-object and Route audit | 650 | T0--T7 table, typed Route table, anti-splice argument | C-13, C-16 | A2/A3/A4 fail; Route B closed |
| 10. Limitations and conclusion | 600 | repeat the outcome hierarchy and identify the next hard gate | all | do not end with a determinant or HP speculation |

### 5.1 Appendix plan

- **Appendix A:** locked-to-standard crossed-product calculation and arrow
  convention.
- **Appendix B:** dense-core kernel, Zak Parseval/intertwining, and
  Hilbert--Schmidt identity.
- **Appendix C:** exact FNS positive, square-integrable, trace-ideal, and
  bounded-`L1` domains.
- **Appendix D:** l.s.c./semifiniteness details and finite-corner projection
  independence.
- **Appendix E:** deterministic control inventory, artifact hashes, and
  reproduction command.
- **Appendix F:** expanded T0--T7 ownership certificate and full Route tuples.

Do not move a load-bearing domain qualification exclusively to an appendix.
The main text must still state the exact owner and stop condition.

## 6. Theorem placement and dependency graph

The manuscript theorem order should be:

```text
source actual-orbit topology
        -> one-orbit Haar + amenability
        -> locked crossed-product identification
        -> unstabilized C(T) tensor K completion
        -> induced-character sign and trace class
        -> shifted Poisson trace
        -> Zak decomposition of the same regular map
        -> FNS trace and dual-Haar cancellation
        -> l.s.c. character traces
        -> full finite-corner no-normal-extension theorem
        -> packet NOT_TESTABLE boundary
        -> local/finite/positive scalar ledger
        -> controls, T0--T7, and Route audit
```

The packet boundary appears after the local obstruction so readers cannot
mistake a missing packet theorem for a premise.  The scalar ledger appears
after the packet boundary so its separate owner is visible.

### 6.1 Suggested named results

1. **Proposition 2.1 (actual-orbit topology).**  Exact genuine-`E_f`
   orbit-circle homeomorphism.
2. **Theorem 3.1 (one-orbit groupoid completion).**  Haar, amenability,
   full/reduced equality, and actual `C(T) tensor K` isomorphism.
3. **Theorem 4.1 (character-fibre Poisson trace).**  Equation for
   `T_theta(f)` with exact domain/sign.
4. **Theorem 5.1 (fixed regular FNS trace).**  Zak decomposition,
   bicommutant, domains, and `Lf(0)`.
5. **Theorem 6.1 (fixed-map no-normal-extension).**  Finite-corner
   contradiction for every `theta`.
6. **Proposition 6.2 (singular corner states).**  Existence and
   nonuniqueness, expressly corner-only.
7. **Proposition 7.1 (intrinsic quotient boundary).**  Free action, open
   quotient, exact closed and open properties.
8. **Theorem 8.1 (positive-time scalar ledger).**  Local finiteness and
   closed-point coefficient ownership.
9. **Proposition 8.2 (generic-clock control).**  Proper clock families and
   composite provenance failure.

Avoid calling P8-7's continuous-function functional a measure theorem.

## 7. Figures and tables

Use visualizations only for the two relationships that prose alone makes easy
to splice incorrectly.  All schematic figures should be native TikZ.  A
numerical control figure may be generated deterministically from the checked
CSV files and should be placed in an appendix or control subsection.

### Figure 1 — typed owner and stop-map diagram

Show:

```text
Deninger E_f packet Gamma_p
   | choose one actual orbit (not canonical)
   v
O ~= R/(LZ) -> A_L -> M_L^reg
                |        |
                |        +-- dual-Haar FNS: L f(0)
                +-- fibre theta: L sum_r f(rL)e^(irtheta)
                            |
                            +-- no normal extension to M_L^reg

Gamma_p -- dotted/blocked --> packet completion -- dotted --> packet trace
closed points + clocks ------> scalar Theta_+ only
```

`figure_table_trace` plan:

| Field | Value |
|---|---|
| `artifact_id` | `fig-owner-map` |
| `source_data` | `phase3_operator_proofs.md`, `phase3_topology_ownership_proofs.md`, and `phase3_peer_review.md` at their locked hashes |
| `transformation` | manual TikZ transcription of the typed maps and stop arrows; compare every node/arrow against Sections 2, 5, and 8 of this blueprint |
| `caption_claim` | the local regular and character traces share `A_L` but have different completion-level normality; packet and scalar promotions are blocked typed arrows |
| `supported_manuscript_claims` | C-06--C-13, Sections 1, 6, 7, and 9 |
| `limitations` | diagram suppresses representation-choice details and does not assert existence of a packet completion |

### Figure 2 — character coefficient filter

Plot or schematically show the coefficient of the `r`-th return as
`e^{ir theta}` around the character circle, with its Haar average zero for
`r!=0` and the `theta=0` value one.  Pair it with the same-scale formulas
`Lf(0)` and `L sum_r f(rL)`.

`figure_table_trace` plan:

| Field | Value |
|---|---|
| `artifact_id` | `fig-character-filter` |
| `source_data` | symbolic equations (4.1), (4.4), and (4.6) in `proof_audit.md`; optional finite-grid data `results/finite_character_grid.csv` |
| `transformation` | TikZ unit-circle diagram; optional plotted points generated by the locked controls script SHA `524884ef...` |
| `caption_claim` | dual-Haar averaging removes all nonzero repetition coefficients while the trivial character retains them |
| `supported_manuscript_claims` | C-04--C-08 |
| `limitations` | finite grids are regression witnesses only; the theorem uses Haar integration and absolute summability |

### Optional Appendix Figure A1 — sign and finite-corner controls

Use two small panels: correct-versus-wrong shifted-Poisson residual and peak
Haar integral versus `n`.  Source only
`shifted_poisson_convention.csv` and `rank_one_corner_peaks.csv`; include the
manifest hash in the caption note.  State that the panels do not prove the
representation or normality theorem.

### Required manuscript tables

| Table | Content | Canonical source |
|---|---|---|
| Table 1 | P8-1--P8-9 verdicts and scope | `proof_audit.md` Section 3 |
| Table 2 | regular versus character trace owner, cone/domain, normality, and time-kernel value | operator proofs Sections 7--9 |
| Table 3 | packet/quotient proved properties versus open gates | topology proofs Sections 4--5 |
| Table 4 | local, finite, and positive-time domain split | topology proofs Section 6 |
| Table 5 | target-free controls and interpretation | controls review Sections 4--5 |
| Table 6 | typed T0--T7 and Route-A status | final `route_audit.md` plus `proof_audit.md` Section 8 |

Every table caption must say whether it reports a theorem, a status audit, or
a finite control.  Do not let a blank or `N/A` cell look like a pass.

## 8. Mathematical notation and terminology lock

Use these formulas without alteration:

```text
fhat(xi)=integral_R f(t)exp(-itxi)dt,
chi_theta(rL)=exp(irtheta),
eta(u+rL)=exp(-irtheta)eta(u),
k_(n,theta)=(2pi n-theta)/L,
T_theta(f)=L sum_r f(rL)exp(+irtheta),
dm(theta)=dtheta/(2pi),
Tau_L(a_f)=Lf(0),
tau_0(a_f)=L sum_r f(rL).
```

Terminology:

- “compact” for `Gamma_p` means compact/quasi-compact in the open-cover
  sense unless Hausdorffness is explicitly established.
- “regular trace” means the FNS trace on the fixed represented bicommutant.
- “character trace” means the l.s.c. extended-positive C*-trace on `A_L`.
- “nonnormal” means no normal extended-positive extension along the fixed
  local map.
- “singular extension” is used only for the finite corner states constructed
  in P8-6.2.
- “return ledger” is qualified as local trace restriction, finite scalar sum,
  or positive-time scalar measure every time the domain could be ambiguous.
- “source-selected” retains every clause from the protocol; algebraic
  distinction of `theta=0` alone is insufficient.

## 9. Source and citation plan

### 9.1 Load-bearing source locator matrix

| Citation key / source | Exact locator to cite | Licensed claim | Claim ceiling |
|---|---|---|---|
| `TOP-DEN-DYN-v4` — Deninger, *Dynamical Systems for Arithmetic Schemes*, arXiv:1807.06400v4; journal DOI `10.1016/j.indag.2024.05.007` | equation (35), physical p. 32; Theorem 6.1, pp. 38--39; Propositions 7.4/7.6/7.7, Corollaries 7.8/7.9, Theorem 7.10 and following remarks, pp. 43--47 | finite-kernel fibres, packet/clock/isotropy, pre-suspension topology and coproduct warning | no source-authored groupoid, packet Hausdorffness, or trace |
| `TOP-DEN-SUR-v1` — Deninger, arXiv:2301.11643v1 | Theorem 4.2, physical pp. 11--12 | compact packets and compact orbits | compact does not silently mean packet Hausdorff |
| `TOP-MOR-v5` — Morishita, arXiv:2508.15971v5 | equation (1.1.5), p. 5; Remark 2.1.13, p. 13; Lemmas 3.4--3.5, pp. 23--24; Theorem 3.6 discussion, pp. 24--25 | target circle and continuity/anti-equivariance used in the restricted orbit lemma | printed enlarged-object homeomorphism is not imported into `E_f` |
| Williams, *Crossed Products of C*-Algebras*, author draft v3.1 | equation (4.63), Theorem 4.30, p. 138; Proposition 5.4, p. 153; Theorem 5.12, p. 161; Theorem 7.13, p. 199 | quotient Haar, actual homogeneous-space isomorphism, induced convention, amenability full/reduced equality | no canonical trace transport or packet tensor product |
| Green (1978), DOI `10.1007/BF02392308` | Proposition 3, printed p. 203 | historical imprimitivity corroboration | not authority for the stronger actual isomorphism |
| Muhly--Renault--Williams (1987) | Theorems 2.8 and 3.1, printed pp. 10 and 16 | groupoid equivalence and transitive-groupoid isomorphism corroboration | full algebra only; reduced equality separate |
| Brown--Green--Rieffel (1977), DOI `10.2140/pjm.1977.71.349` | Theorem 1.2, printed p. 351 | stable-isomorphism evidence ladder | do not cancel stabilization |
| Anantharaman-Delaroche (2002), DOI `10.1090/S0002-9947-02-02978-1` | Examples 2.7(2), manuscript p. 6; Theorem 5.3, p. 14 | amenability of every `R` action and full/reduced equality | one-orbit hypotheses must be stated |
| `TR-BR18` — Bourne--Rennie (2018), DOI `10.1007/s11040-018-9274-4` | Proposition 3.2, pp. 8--9; Lemma 7.4, p. 36 | invariant-measure continuous-crossed-product trace template | does not identify Paper-8's fixed representation |
| `TR-REN21` — Renault (2021), DOI `10.5802/crmath.183` | physical pp. 3--4 | Plancherel weight and Fourier-isometric dual Haar normalization | no packet trace selection |
| `TR-ERS11` — Elliott--Robert--Santiago (2011), DOI `10.1353/AJM.2011.0027` | Theorem 3.11, physical p. 12 | pullback of l.s.c. traces | dense semifiniteness and faithfulness remain separate |
| `TR-CZ83` — Combes--Zettl (1983), DOI `10.1007/BF01456936` | Proposition 2.2, physical pp. 7--8 | Morita induction of l.s.c. traces | no algebra isomorphism or selected completion |
| `OP-JON09` — Jones, *Von Neumann Algebras* | physical pp. 15--16; Definition 7.1.2 and Theorem 7.1.3, pp. 43--44 | `vN(Z)=L-infinity(T)`, Haar trace, normality criterion | no source credit for Paper-8's new peak lemma |
| `HA-LAU17` — Laugesen, arXiv:0903.3845v2 | Definition 14.1, p. 79; Theorems 14.10--14.11, pp. 84--85; Theorem 23.5, p. 137 | Fourier sign, decay, unshifted Poisson | shifted arbitrary-`L` formula is Paper-8's specialization |

### 9.2 Citation integrity rules

1. Cite source theorems only for the precise general result they state; label
   each locked specialization and new lemma as Paper-8 work.
2. Include every DOI above in the bibliography; do not invent a DOI for a
   source whose audited manifestation is arXiv or author-hosted only.
3. Use exact theorem/equation/section locators.  The topology and trace PDFs
   have passing read-integrity preflights.  The older groupoid corpus has
   environmental `UNAVAILABLE` preflights; use independently checked printed
   theorem locators and do not represent those page anchors as preflight PASS.
4. Verify reference existence and all bibliographic fields again at final
   integrity, even though the Phase-2 manifests already record them.
5. Maintain zero citation orphans and zero dangling citations.
6. Use direct quotation sparingly and keep any source-specific quotation
   within the ARS word limit; theorem paraphrase is preferred.
7. Do not cite generic literature as evidence that the Deninger packet bridge
   exists.  Generic results become applicable only after their stated
   hypotheses close.

### 9.3 Source redistribution boundary

Before GitHub or public-paper release, check the redistribution licence of
every retained PDF.  If a licence is not explicit, publish the manifest,
hash, primary URL, and locator, but omit the PDF bytes.  This packaging choice
must not remove the bibliography entry or the verification ledger.

### 9.4 Search-bounded novelty sentence

The only permitted novelty form is:

> To our knowledge, based on the arXiv, OpenAlex, Crossref-metadata,
> publisher/author-page, exact-web, and retained-full-text searches documented
> through 14 August 2026, we did not locate a primary paper that connects
> Deninger's rational-Witt finite-kernel prime packets to the continuous-`R`
> transformation-groupoid C*/Plancherel construction or formulates the same
> fixed-object trivial-isotropy-character normality obstruction.

Immediately add that generic groupoid imprimitivity, Plancherel theory,
Poisson summation, and diffuse-`L-infinity` point-evaluation singularity are
prior mathematics.  Classification: `SUPPORTED_WITHIN_SEARCH`, never global
priority.

## 10. Route typed-owner table

The final independent audit is `route_audit.md`, SHA-256
`355cf28868a1c9beaa30924a87d8cfc34214b5160c2ca4ca21d72824f5f37b4e`.
The manuscript must reproduce these record-specific tuples exactly; it may
not compute or narrate a coordinatewise maximum across them.

| Candidate ID | Exact tuple `(A0,A1,A2,A3,A4)` | Overall | Typed owner and ceiling |
|---|---|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | source packet and clock only; analytic packet completion and the primary extension question remain `NOT_TESTABLE` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | the already chosen actual orbit owns the local LCH groupoid/completion, but no source-selected packet orbit, trace amplitude, or multiplicity |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | fixed normal/FNS trace; A1 fails for this owner because dual Haar erases every nonzero return |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact local phase-weighted repetition ledger; the no-normal-extension result is only for the fixed local map |
| `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | source-indexed, coefficient-one, positive-time scalar Radon ledger; no local trace or packet completion is inherited |

Exact Route-A YAML locks:

| YAML | SHA-256 |
|---|---|
| `evaluations/route_a/DEN-EF-PACKET-ACTION-GRPD-P/2026-08-14-stage8.yaml` | `28da284cd0f1be601ded15a24281a5b07937df1fd29ba8551cbf2ab9f6f9d0ee` |
| `evaluations/route_a/DEN-EF-ORBIT-ACTION-GRPD/2026-08-14-stage8.yaml` | `17defc7c1ec088e4aab5b256ec4ee19a6df126d1d3c76b86f191d3c76f5b77b9` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-REG-TRACE/2026-08-14-stage8.yaml` | `51903590ba183daa54029c7977c1a0ba5c2550cf6e685d18ec2a9bb64d5fa333` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE/2026-08-14-stage8.yaml` | `ddade81079ca04fcb652b0fe2810e081775afdb674c83d72c5c0844e61077e1d` |
| `evaluations/route_a/DEN-EF-GRPD-TIME-RETURN-POS/2026-08-14-stage8.yaml` | `d42df1d6dd699665e918efac61d24a38b500c4d7a3e771ef87761fd89616c22a` |

The anti-splice rule is part of the result: the packet and bare-orbit records
cannot inherit a trace A1 coordinate; the regular trace cannot borrow the
character trace's return ledger; the character trace cannot borrow the
regular trace's normality; and the scalar record cannot borrow a local trace
or packet completion.  All five records have `A2_FAIL`, `A3_FAIL`, and
`A4_FAIL`, all have Boolean `route_b_invocation_allowed=false`, and no
Route-B YAML exists or is permitted.

## 11. Declarations package

Include all declarations required by the ARS academic-paper workflow.

### Source and citation integrity

State that locally read primary/authoritative source manifestations are
enumerated in the source manifests with hashes, retrieval endpoints,
preflight status, and exact locators.  Distinguish PASS preflights from the
older groupoid files whose preflight status was environmentally unavailable
but whose printed theorem locators were independently checked.

### Data and code availability

Suggested wording:

> No external empirical dataset was used.  The accompanying Paper-8 directory
> contains the standard-library Python implementation, unit tests,
> reproduction script, nine deterministic CSV control tables, and a hash
> manifest.  Running `./experiments/reproduce.sh` regenerates and verifies the
> package.  These artifacts are finite convention, falsification, and domain
> regression witnesses; they are not proofs of the infinite theorems or of a
> packet transport claim.

### Ethics statement

> This mathematical study involved no human participants, animals, clinical
> records, or personal data.  Institutional review and informed consent are
> not applicable.

### Author contributions (CRediT)

Subject to final human confirmation:

> Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation,
> Software, Validation, Data curation, Visualization, Writing--original draft,
> and Writing--review and editing.

### Competing interests

> The author declares no financial or non-financial conflict of interest.

### Funding

Use the established project declaration only after human confirmation:

> No project-specific external funding source was declared.

### AI-use disclosure

Suggested wording:

> Generative AI assisted source triage, proof and domain cross-checking,
> deterministic-code drafting, adversarial review, manuscript drafting, and
> formatting.  The workflow retained exact source manifestations, locators,
> hashes, typed amendments, independent review records, and target-free
> controls.  No unpublished manuscript was uploaded to a secondary model, and
> no cross-model review is claimed.  The human author directed the research
> question and acceptance criteria, must verify every mathematical statement
> and citation before submission, and takes responsibility for the final
> manuscript.  An AI system is not an author.

### Acknowledgments

Use “No personal acknowledgments are declared” unless the author supplies a
different statement.

## 12. Forbidden wording and safe replacements

| Forbidden or unsafe wording | Required replacement |
|---|---|
| “The packet-level primary hypothesis is refuted.” | “The fixed one-orbit analogue is refuted; the packet-level primary outcome remains `NOT_TESTABLE`.” |
| “The packet groupoid C*-algebra is …” | “Conditional on packet Hausdorff/LCH …”; otherwise discuss only the one-orbit algebra. |
| “`Q_p` is `B_p`” or “the packet is a product” | “`Q_p` is an intrinsic open quasi-compact second-countable quotient; Hausdorffness and product identification remain open.” |
| “`C(T)` is the centre of `C(T) tensor K`” | “The algebraic centre is zero; `C(T)` appears in a full finite rank-one corner or the multiplier centre.” |
| “Point evaluation is a functional on `L-infinity(T)`” | “A hypothetical normal extension compresses to a functional agreeing with point evaluation on the continuous corner.” |
| “A singular trace extending `tau_theta` exists” | “Distinct singular states extend the finite-corner point state; no full unbounded trace extension is claimed.” |
| “Full equals reduced, so the character trace is normal” | State full/reduced equality and completion-level normality as separate theorems. |
| “The Haar system selects the trace/measure” | Separate arrow Haar, invariant orbit measure, transverse probability, and FNS trace. |
| “There is one orbit per prime packet” | “There is one rational closed point `(p)` and one scalar ledger component per prime under closed-point counting.” |
| “`Theta_+` is the groupoid trace/global trace” | “`Theta_+` is a locally finite scalar Radon measure on positive time.” |
| “The mechanism is arithmetic because it reproduces prime powers” | “The local mechanism is generic; arithmetic ownership comes from source-derived `(p)` and `log p`.” |
| “The first/new obstruction” | Use only the dated `SUPPORTED_WITHIN_SEARCH` sentence. |
| “Morita equivalence gives the isomorphism” | Cite Williams Theorem 4.30 for the actual unstabilized isomorphism. |
| “The controls prove the theorem” | “The symbolic proof establishes the theorem; controls detect sign, normalization, and ownership regressions.” |
| “zeta determinant,” “completed function,” or “Hilbert--Polya operator” | Omit; these objects are outside the frozen Paper-8 scope. |

## 13. Writing and formatting specification

- Use formal mathematical English with direct claim openings and varied
  paragraph length.  Avoid throat-clearing, excessive em dashes, and generic
  claims of importance.
- Keep notation stable: `L`, `du`, `du/L`, `dm`, `Tau_L`, and `tau_theta`
  must never exchange roles.
- State the domain before applying a trace to a complex kernel.
- Every theorem begins with its typed owner and ends with its stop boundary.
- Put the three-outcome hierarchy in the introduction, abstract, limitations,
  and conclusion; repetition here is protective rather than stylistic.
- Use `SOURCE_THEOREM`, `DERIVABLE_NEW_LEMMA/THEOREM`, `OPEN`, and
  `NOT_TESTABLE` consistently in notes; translate them into readable prose in
  the main manuscript without weakening their meaning.
- Produce the paper in LaTeX, compile with XeLaTeX/BibTeX, and use native TikZ
  for schematics.  Do not use HTML-to-PDF conversion.
- The English and Simplified-Chinese abstracts cover the same result order but
  are independently composed rather than mechanically translated.
- Keep all citation anchors/source locators in a claim-source audit ledger
  during drafting.  Do not fabricate a locator when the corpus context lacks
  one.

## 14. Release checklist

### Mathematical and typed-owner gate

- [ ] The abstract says packet `NOT_TESTABLE`, local `REFUTED`, scalar
  positive ledger `PASS`.
- [ ] Every occurrence of the no-normal theorem names the fixed one-orbit map.
- [ ] The regular trace is FNS/normal and return-blind away from zero.
- [ ] The character trace is l.s.c., densely defined, semifinite,
  nonfaithful, unbounded, and nonnormal relative to the fixed regular map.
- [ ] Singular extensions are described as corner-state extensions only.
- [ ] The packet topology and same-map bridge remain open/not testable.
- [ ] Local, finite, and positive-time domains are visibly separate.
- [ ] Coefficient one is attributed only to rational closed-point counting.
- [ ] No determinant, A3, A4, Route B, zero-data, or Hilbert--Polya claim is
  present.

### Source and claim-integrity gate

- [ ] Every reference exists and all authors, title, year, venue, pages, DOI,
  and manifestation fields are freshly verified.
- [ ] Every source-backed claim has an exact theorem/equation/section locator.
- [ ] All source claims respect the source/new-specialization distinction.
- [ ] No citation orphan or dangling citation remains.
- [ ] All novelty language is bounded to the documented search through
  2026-08-14 and classified `SUPPORTED_WITHIN_SEARCH`.
- [ ] Locally read PDF page anchors respect their preflight status; no
  environmental `UNAVAILABLE` result is relabelled PASS.
- [ ] Source-PDF redistribution licences are checked; restricted bytes are
  omitted while manifests, URLs, hashes, and locators remain.

### Reproducibility gate

- [ ] `./experiments/reproduce.sh` passes 18/18 tests.
- [ ] All nine CSVs and the JSON manifest regenerate byte-identically in two
  fresh directories.
- [ ] Manifest SHA-256 is
  `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`
  unless an intentional, independently reviewed implementation version is
  created.
- [ ] No `__pycache__`, `*.pyc`, `*.pyo`, backup, or temporary file is present
  in the release subtree.
- [ ] Every figure/table trace names source data, transformation, caption
  claim, supported manuscript claims, and limitations.
- [ ] The manuscript calls the controls finite witnesses, not proofs.

### Route and exact-byte gate

- [ ] Confirm Section 10 still matches independent `route_audit.md` SHA
  `355cf288...` and the five exact YAML hashes at final release.
- [ ] Every Route tuple is record-specific and matches its YAML byte for byte.
- [ ] No coordinatewise maximum is taken across source, orbit, trace, and
  scalar records.
- [ ] No Route-B YAML exists; every record has
  `route_b_invocation_allowed=false`.
- [ ] Current mechanical Phase-2 authority is
  `phase2_final_relock.md` SHA `b1ed0c68...`, not the historical self-version
  sentence it supersedes.
- [ ] Final Phase-3 peer-review authority is
  `phase3_peer_review.md` SHA `572e7852...`.
- [ ] Recompute and record the final hashes of `proof_audit.md`, this
  blueprint, the manuscript, bibliography, PDF, integrity review, and release
  audit.

### Manuscript and PDF gate

- [ ] English and Simplified-Chinese abstracts align structurally and preserve
  all three outcome levels.
- [ ] All required declarations in Section 11 are included and human-confirmed.
- [ ] XeLaTeX/BibTeX compiles without unresolved references, missing glyphs,
  or overfull material text.
- [ ] PDF title/author metadata, page count, bookmarks, equation references,
  tables, and TikZ figures are visually inspected.
- [ ] A fresh final integrity audit verifies 100% of references and
  high-impact claims before release.
- [ ] An independent post-draft peer review confirms that no local result was
  promoted to the packet.

## 15. Drafting handoff

The draft writer should receive, at minimum, the following exact inputs:

```text
research_protocol.md
candidate_lock.md
phase2_domain_amendment.md
phase2_final_relock.md
phase2_source_topology_audit.md
phase2_groupoid_source_audit.md
phase2_trace_source_audit.md
phase2_novelty_search.md
phase3_topology_ownership_proofs.md
phase3_operator_proofs.md
phase3_controls_review.md
phase3_peer_review.md
proof_audit.md
final route_audit.md and Route-A YAMLs
results/isotropy_trace_manifest.json
source manifests and checksum ledgers
```

The writer may compress exposition but may not strengthen a claim, remove a
scope qualifier, change an owner, merge a trace domain, or fill an open packet
gate from general model knowledge.  Any such change requires a new explicit
review before release.
