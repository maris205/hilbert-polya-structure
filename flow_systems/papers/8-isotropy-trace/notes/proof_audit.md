# Paper 8 Phase-3 integrated proof audit

Date: 2026-08-14 (Asia/Shanghai)  
Status: **PASS — P8-1--P8-9 integrated with the mandatory scoped split**  
Manuscript gate: **AUTHORIZED by independent Phase-3 review**  
Primary packet outcome: **`NOT_TESTABLE`**  
Fixed one-orbit analogue: **`REFUTED`**  
Positive-time scalar ledger: **`PASS`**

This file is an integrated synthesis, not a new proof and not a manuscript.
It does not replace the theorem proofs, source audits, active locks, Route
records, or independent review.  Its purpose is to state exactly which proved
claims may travel into the manuscript, which typed object owns each claim,
and where the argument must stop.

## 1. Exact authority snapshot

### 1.1 Active locks and Phase-2 authority

| Artifact | SHA-256 | Authority |
|---|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` | normative question, conventions, P8 targets, and stop rules |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` | normative typed-object and trace-domain lock |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` | active finite-corner and simultaneous-sign correction |
| `phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` | source topology, actual-orbit bridge, and packet LCH boundary |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` | one-orbit Haar, amenability, imprimitivity, and exact completion source chain |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` | trace, Plancherel, normality, and Poisson source chain |
| `phase2_novelty_search.md` | `28862717c996b60a7c9e210cae65a78ee1a42d035dafadb8f6f8e59435df0bca` | search-bounded novelty classification through 2026-08-14 |
| `phase2_final_gate.md` | `22fd0376ad8e69e6816b3d005d88f4cde2cc5f4b243749c95aa2f19ab8164a3f` | historical Phase-3 authorization gate |
| `phase2_final_relock.md` | `b1ed0c68e1eac5605d70f0a482f28139f764eff12f7fa87007ad9fd854553619` | current mechanical authority for the Phase-2 hash ledger |

The historical final gate records the pre-addendum content hash
`c22f090f...` for `phase2_domain_da_review.md`; the current complete review
file has SHA-256
`05fecacd1215990ff79a66d69670f0ff57510dc5d7466d68588bb4c4a890c014`.
`phase2_final_relock.md` reconstructs both byte strings and independently
closes this self-versioning artifact.  It is not an open finding and changes
no mathematical claim.

### 1.2 Phase-3 proof, controls, and review authority

| Artifact | SHA-256 | Authority |
|---|---|---|
| `phase3_topology_ownership_proofs.md` | `209989444b48a625777c0c4626b92429ed08b58f3dc4c31b03f7d23b067dca14` | P8-1, scoped P8-7/P8-8, P8-9, and scalar-ledger ownership |
| `phase3_operator_proofs.md` | `5e8fd6cd400c7300da5c80e8991b3770ad03c9026a236caab04642cd96314a26` | P8-2--P8-6 on the fixed actual one-orbit map |
| `phase3_controls_review.md` | `a054265f3fb25ef93270a6e5c5a1db6791f8bbb7b08b78f8e13b7554a93a3f3d` | independent controls audit; final 0/0/0 and release-clean addendum |
| `phase3_peer_review.md` | `572e7852de08ded264f87bb245aff181ae032ed8a8bfdf831fcd4ed5d1f921c3` | independent integrated review; PASS, 0 Critical / 0 Major / 0 Minor |
| `results/isotropy_trace_manifest.json` | `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07` | deterministic controls manifest; finite regression evidence only |

The independent review authorizes manuscript drafting only under its ten-item
claim envelope.  In particular, it does not authorize a packet completion, a
packet-level `REFUTE`, a full singular extension of the character trace, a
global operator, or a determinant.

## 2. Central result hierarchy

The three outcomes below are simultaneous and must be reported at the same
level of prominence.

| Level | Exact conclusion | Status | Typed owner |
|---|---|---|---|
| Packet primary question | The inherited packet has no proved Hausdorff/LCH topology suitable for the frozen standard groupoid completion, and no packet same-map restriction/disintegration/compression theorem is available.  The requested normal source-selected packet extension therefore cannot yet be formulated on the frozen map. | **`NOT_TESTABLE`** | `DEN-EF-PACKET-ACTION-GRPD-P` and conditional packet trace records |
| Fixed actual-orbit analogue | On `A_L -> M_L^reg`, the character trace has no normal extended-positive extension.  The local normal-extension analogue is therefore refuted. | **`REFUTED`** | `DEN-EF-ORBIT-ACTION-GRPD` with `tau_theta` on its exact completion |
| Source-clock scalar record | Counting the rational closed points and their source clocks gives an exact locally finite positive-time Radon measure. | **`PASS`** | scalar aspect of `DEN-EF-GRPD-TIME-RETURN-POS` |

The local refutation cannot be promoted to the packet primary outcome.  The
scalar pass cannot be promoted to a packet trace or a global all-prime
operator.  No coordinatewise maximum may be taken across the three rows.

## 3. Integrated P8-1--P8-9 adjudication

| Target | Final integrated verdict | Exact manuscript-safe result | Mandatory boundary |
|---|---|---|---|
| P8-1 | **SPLIT PASS / `NOT_TESTABLE`** | Every already chosen actual `E_f` orbit is a compact Hausdorff second-countable circle; its action groupoid has explicit Lebesgue Haar, is amenable, and has full/reduced equality.  The packet has a continuous free `K_p` action and an open, quasi-compact, second-countable quotient `Q_p`. | Packet and `Q_p` Hausdorffness, packet LCH, local triviality, `Q_p=B_p`, packet completion, and packet analytic transport remain open or not testable. |
| P8-2 | **CLOSED, one orbit** | `A_L=C^*(O\rtimes R)=C_r^*(O\rtimes R)\cong C(T)\otimes K(H_0)` as an actual unstabilized isomorphism, with the induced-character continuous field. | The displayed trivialization is choice-dependent and is not packet or source data. |
| P8-3 | **CLOSED, one orbit** | Every time kernel is trace class in every character fibre, with frequencies `(2pi n-theta)/L` and return phase `exp(+ir theta)`. | The sign belongs to the frozen Williams induction convention; controls are not its proof. |
| P8-4 | **CLOSED, fixed one-orbit map** | The source-fibre regular representation is faithful, its bicommutant is `L-infinity(T,dm) bar_tensor B(H_0)`, and the exact FNS trace returns `L f(0)`. | Normality and cancellation belong only to this fixed regular owner. |
| P8-5 | **CLOSED, one orbit** | `tau_theta=Tr o ev_theta o Phi` is l.s.c., densely defined, semifinite, nonfaithful, and gives `L sum_r f(rL)exp(ir theta)`; `theta=0` gives the full two-sided comb. | It is a C*-level extended-positive trace and is not normal in the fixed regular completion. |
| P8-6 | **CLOSED, fixed one-orbit map** | A full trace-finite rank-one corner reduces any hypothetical normal extension to a normal extension of point evaluation from `C(T)` to Haar `L-infinity(T)`, contradicted by decreasing peaks.  Distinct singular corner-state extensions exist. | `C(T)` is a noncentral corner, not `Z(A_L)`; the constructed singular states extend only the corner state, not the full unbounded `tau_theta`. |
| P8-7 | **SCOPED PASS** | Section-free orbit averaging is a positive continuous-function functional for each given Borel probability on `Q_p`; local and finite scalar combs and the global positive-time scalar measure are valid on their stated domains. | Packet Radon lifting, exhaustion of invariant measures, full packet traces, and a packet same-owner trace restriction remain not testable. |
| P8-8 | **PASS after proof-stream integration** | All character, scale, corner, transverse, copy, clock, composite, zero-time, and domain controls pass and remain target-free. | Finite tables are regression/falsification witnesses, not proofs of infinite theorems or packet transport. |
| P8-9 | **PASS as typed ownership audit** | T0--T7 fields are evaluated record by record; partial passes and `N/A` preserve their type boundaries. | Scalar T6/T7 cannot repair packet T1/T3/T4/T5; no Route coordinates may be spliced. |

## 4. Exact fixed one-orbit theorem package

### 4.1 Object, topology, and Haar owner

Fix a prime `p`, choose one actual orbit `O` in the source packet, and set

```text
L=log p,              O ~= R/(L Z),
G_O=O rtimes R.
```

The inherited-orbit homeomorphism is a corrected genuine-`E_f`
`DERIVABLE_NEW_LEMMA`; it is not Morishita's printed full-character theorem.
The groupoid arrow `(x,t)` has source `x` and range `x+t`.  Its locked
convolution and involution are

```text
(a*b)(x,t)=integral_R a(x+v,t-v)b(x,v)dv,
a^*(x,t)=conjugate(a(x+t,-t)).
```

Lebesgue `dt` is arrow Haar.  Quotient length Haar `du` on `O` has total mass
`L`; orbit probability Haar is `du/L`.  These are three different measures.
The quotient formula is

```text
integral_R g(t)dt
 =integral_[0,L) sum_(r in Z)g(u+rL)du.
```

The one-orbit action is amenable because `R` is amenable, so the full and
reduced completions agree.  None of these statements chooses an orbit inside
the packet or a transverse packet probability.

### 4.2 Completion and induced-character convention

The proof first converts the locked convolution to the standard crossed
product and only then applies the homogeneous-space theorem.  The exact
completion is

```text
A_L=C^*(O rtimes R)=C_r^*(O rtimes R)
   ~=C^*(L Z) tensor K(H_0)
   ~=C(T) tensor K(H_0),
H_0=L2([0,L),du).
```

This is an actual unstabilized isomorphism from Williams, Theorem 4.30,
specialized to the frozen object; it is not obtained by cancelling a stable
factor from Morita equivalence.

For

```text
chi_theta(rL)=exp(i r theta),
eta(u+rL)=exp(-ir theta)eta(u),
(U_t eta)(u)=eta(u-t),
```

the Floquet basis has frequencies

```text
k_(n,theta)=(2pi n-theta)/L.
```

The integrated representation of a locked kernel is

```text
(pi_theta(a)eta)(y)
 =integral_R a([y-t],t)eta(y-t)dt,
```

and the continuous compact-operator field has dense-core kernel

```text
K_a(theta;y,u)
 =sum_(r in Z)a([u],y-u+rL)exp(i r theta).
```

These formulas fix the sign before any return or Euler comparison.

### 4.3 Character-fibre trace formula

For `f in C_c^infinity(R)`, set `a_f(x,t)=f(t)` and freeze

```text
fhat(xi)=integral_R f(t)exp(-it xi)dt.
```

Schwartz decay gives uniform absolute summability, hence

```text
pi_theta(a_f)e_(n,theta)
 =fhat((2pi n-theta)/L)e_(n,theta),

T_theta(f)=Tr(pi_theta(a_f))
 =sum_(n in Z)fhat((2pi n-theta)/L)
 =L sum_(r in Z)f(rL)exp(+ir theta).                 (4.1)
```

The positive return phase in (4.1) is inseparable from the negative Floquet
shift.  A manuscript must not restore the historical provisional
`+theta/-ir theta` pair or change only one sign.

### 4.4 Fixed regular representation and FNS trace

On `L2(R)`, the source-fibre regular representation is

```text
(lambda_L(a)xi)(s)
 =integral_R a([s-t],t)xi(s-t)dt.
```

The Zak transform

```text
(Zxi)(theta,u)=sum_(r in Z)xi(u+rL)exp(i r theta)
```

is a unitary onto the dual-Haar direct integral and intertwines this same
regular representation with `int_T^oplus pi_theta dm`, where
`dm=dtheta/(2pi)`.  Continuity of the compact fields and full support of Haar
prove faithfulness.  The bicommutant is therefore

```text
M_L^reg=lambda_L(A_L)''
 =L-infinity(T,dm) bar_tensor B(H_0).                (4.2)
```

The FNS trace is defined first on the positive cone:

```text
Tau_L(X)=integral_T Tr_(H_0)(X(theta))dm(theta).      (4.3)
```

Its positive finite domain, square-integrable left ideal, algebraic trace
ideal, and bounded `L1` domain are distinct.  The complex time kernel belongs
to the bounded linear `L1` domain because

```text
integral_T sum_n |fhat((2pi n-theta)/L)|dm(theta)
 =(L/(2pi)) integral_R |fhat(xi)|dxi < infinity.
```

Thus Fubini is licensed, and dual-Haar averaging at the common length scale
gives

```text
Tau_L(lambda_L(a_f))
 =(1/(2pi))integral_0^(2pi)T_theta(f)dtheta
 =L f(0).                                             (4.4)
```

Every `r!=0` return is erased.  At probability orbit scale the entire trace,
not just one displayed value, is divided by `L`.

### 4.5 Character traces and the trivial fibre

On the positive cone of `A_L`, define

```text
tau_theta(a)=Tr_(H_0)(Phi(a)(theta)).                 (4.5)
```

The proof establishes that (4.5) is a norm-lower-semicontinuous, densely
defined, semifinite, nonfaithful, genuinely unbounded C*-trace.  Its linear
trace ideal contains every `a_f`.  On those kernels,

```text
tau_theta(a_f)=L sum_r f(rL)exp(ir theta),
tau_0(a_f)=L sum_r f(rL).                             (4.6)
```

Equations (4.4) and (4.6) have different trace owners.  Their agreement at
time zero does not identify the full traces, and the algebraic distinction of
`theta=0` selects neither a transverse packet measure nor a cross-prime mass.

### 4.6 Full finite corner and no normal extension

Since `H_0` is infinite dimensional,

```text
Z(A_L)=0,
ZM(A_L)=C(T) tensor 1.
```

The character weight is generally infinite on positive multiplier-centre
elements.  The bounded witness instead uses a rank-one `e in K(H_0)` and

```text
p=1 tensor e,
pA_Lp ~= C(T),
pM_L^reg p ~= L-infinity(T,dm),
tau_theta(p)=1.                                      (4.7)
```

If a normal extended-positive weight on `M_L^reg` extended the same
`tau_theta`, compression by `p` would be a bounded normal positive functional
extending `delta_theta`.  The continuous peaks

```text
h_n(z)=max(1-n d(z,theta),0)
```

decrease to zero in Haar `L-infinity`, while `h_n(theta)=1`.  Normality gives
a contradiction.  Hence no normal extended-positive weight, and therefore no
normal trace, extends `tau_theta` along the fixed local map.

Hahn--Banach and shrinking-neighbourhood cluster states separately give
distinct singular states on the measurable corner that extend
`delta_theta`.  They are not extensions of the full unbounded character trace
on all of `M_L^reg`.  The manuscript must retain that distinction.

## 5. Packet branch and quotient boundary

The source audit proves packet compactness only in the open-cover sense and
derives second countability.  It does not prove that the inherited suspension
packet `Gamma_p` is Hausdorff.  Consequently the standard frozen LCH packet
groupoid completion is unavailable.

The common stabilizer does prove that

```text
K_p=R/(L_p Z)
```

acts continuously and freely, and that the quotient map
`q_p:Gamma_p->Q_p` is open.  `Q_p` is quasi-compact and second countable.
The following remain open:

- packet and quotient Hausdorffness;
- packet local compactness in the frozen Hausdorff framework;
- proper/principal-bundle status and local triviality;
- `Q_p=B_p` or any packet product chart;
- Radon lifting or exhaustion of invariant packet measures;
- a packet C*-completion, regular von Neumann algebra, or trace
  disintegration; and
- a same-map transport of the local finite corner and no-normal-extension
  theorem.

For `h in C(Gamma_p)`, the section-free orbit average

```text
(A_p h)(q_p(x))=integral_0^(L_p)h(phi^t(x))dt
```

is a positive map into `C(Q_p)`.  Integrating it against a given Borel
probability on `Q_p` yields a positive invariant continuous-function
functional of mass `L_p`.  Without Hausdorffness, this is not relabelled a
Radon packet measure, an exhaustive disintegration, or a packet trace.

The packet-level primary question therefore remains `NOT_TESTABLE`.  This is
not evidence that packet Hausdorffness, a packet completion, or a normal
extension is impossible.

## 6. Local, finite, and positive-time scalar domains

For each prime define the two-sided local scalar comb

```text
R_p=L_p sum_(r in Z)delta_(rL_p).
```

On any already chosen actual orbit, P8-5 proves
`tau_0(a_f)=R_p(f)`.  This equality is local and does not construct a packet
trace.  For a finite prime set `S`, the scalar sum

```text
R_S=sum_(p in S)R_p
```

is a finite assembly with no global C*- or `L1` owner.

The unweighted all-prime two-sided sum is not locally finite on `R`: every
prime contributes `L_p` at zero.  Restricting the test domain to positive time
instead gives

```text
Theta_+
 =sum_p L_p sum_(r>=1)delta_(rL_p),

Theta_+(f)
 =sum_p L_p sum_(r>=1)f(rL_p),
f in C_c^infinity((0,infinity)).                     (6.1)
```

If `supp(f) subset [a,b]` with `a>0`, only primes `p<=exp(b)` and repetitions
`r<=b/log p` contribute.  Hence (6.1) is a locally finite positive Radon
measure on `(0,infinity)`.

The cross-prime coefficient is one because the scalar assembly uses counting
measure on the one rational closed point `(p)` for each prime.  It is not a
packet-orbit multiplicity, a transverse probability, or a trace-normalization
theorem.  Weighted variants are different candidates.

## 7. Integrated falsification and reproducibility audit

The deterministic package passed 18/18 unit tests and two byte-identical fresh
generations.  Nine CSV artifacts contain 129 data rows; the manifest hash is
listed in Section 1.  The controls establish regression-level agreement with
the frozen formulas and boundaries:

| Control family | Exact checked implication | What it cannot prove |
|---|---|---|
| shifted Poisson and nontrivial phase | identifies `(2pi n-theta)/L` with `exp(+ir theta)`; wrong-sign residual is separated | the compact-support Poisson theorem or representation theorem |
| finite character grids | exact root-of-unity cancellation for the finite repetition window | Haar integration as an infinite theorem |
| regular versus trivial / zero time | regular keeps only `Lf(0)`; trivial keeps the comb; zero is exposed | equality or normality of the two traces |
| common length/probability scale | both compared traces rescale by the same `1/L` | a fitted independent normalization |
| finite-corner peaks and representatives | point values survive while Haar mass vanishes; point evaluation is representative-sensitive | the fixed bicommutant or no-normal theorem, which are proved separately |
| transverse probabilities | time-only values agree while a transverse observable varies | canonical selection or exhaustion of packet measures |
| copied packet | counting copies changes the scalar coefficient additively | source canonicity of an artificial copied candidate |
| arbitrary and composite clocks | the analytic compiler persists for target-free proper clock families | arithmetic provenance; composite labels fail the `Spec Z` closed-point gate |
| local/finite/global domains | preserves the three scalar domains and rejects a global operator claim | any all-prime C*- or `L1` trace |

The code uses only the Python standard library, no network or random input,
no Riemann-zero data, no Euler-target comparison, and no fitted phase, clock,
mass, or transverse probability.  The controls are not theorem owners.

## 8. Integrated T0--T7 ownership audit

`PASS*` below means only the stated subfield passes.  `N/A` is a type barrier,
not a pass.

| Typed record | T0--T2 source/object fields | T3--T5 analytic owner | T6 formula/domain | T7 arithmetic promotion |
|---|---|---|---|---|
| `DEN-EF-ORBIT-ACTION-GRPD` | PASS: actual chosen `E_f` orbit, inherited topology, source clock | PASS locally: Haar, completion, fixed regular and character traces | PASS: equations (4.1)--(4.6) on `C_c^infinity(R)` | PASS*: source `(p)` and `L_p`; no packet multiplicity or cross-prime trace mass |
| `DEN-EF-PACKET-ACTION-GRPD-P` | PASS*: actual packet/flow, compact + second countable, source clock; Hausdorff open | `NOT_TESTABLE` at packet completion and trace levels | `NOT_TESTABLE` as a packet trace | PASS*: prime label and clock only |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q` | PASS*: intrinsic free quotient; not `B_p`; Hausdorff/local chart open | N/A as quotient; continuous-function average only | N/A for a return trace | OPEN: no packet or cross-prime mass selected |
| `DEN-EF-GRPD-REG-TRACE-FAM` | PASS on one orbit / packet branch not testable | PASS locally as FNS; packet owner absent | PASS locally: `Lf(0)` | no return amplitude promotion |
| `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` | PASS on one orbit / packet branch not testable | PASS locally as l.s.c. C*-trace and fixed-map nonnormality | PASS locally: full phase-weighted comb | source clock only; no packet mass |
| `DEN-EF-GRPD-TIME-RETURN-LOCAL` | PASS on an actual chosen orbit; packet trace owner absent | PASS only as local orbit trace restriction | PASS: `R_p` | PASS*: local source clock; no packet-wide trace |
| `DEN-EF-GRPD-TIME-RETURN-FIN` | PASS for a finite actual prime set | N/A as scalar finite assembly | PASS as finite scalar sum | PASS: finite closed-point counting |
| `DEN-EF-GRPD-TIME-RETURN-POS` | PASS for actual source prime/clock fields | N/A by scalar-measure type | PASS: locally finite `Theta_+` | PASS for coefficient-one scalar ledger only |

No row may borrow a completion, trace domain, normality property, determinant,
or Route coordinate from another row.

## 9. Final independent Route audit

The independent formal audit is `route_audit.md`, SHA-256
`355cf28868a1c9beaa30924a87d8cfc34214b5160c2ca4ca21d72824f5f37b4e`.
It creates five records because the bare one-orbit groupoid, its fixed normal
trace, and its return-sensitive character trace have different analytic
owners.

| Candidate ID | Exact tuple `(A0,A1,A2,A3,A4)` | Overall | Exact typed interpretation |
|---|---|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | actual packet and clock are source-related; analytic packet branch and primary extension question remain `NOT_TESTABLE` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | actual chosen orbit owns LCH/Haar/amenability/completion, but no source-selected packet orbit, trace amplitude, or multiplicity |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact fixed FNS trace; A1 is refuted for this owner because dual Haar erases all `r!=0` returns |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact local repetition ledger; normal extension is refuted only on the fixed local map |
| `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | exact source-indexed coefficient-one closed-point/repetition scalar Radon ledger |

The YAML artifacts are:

| YAML | SHA-256 |
|---|---|
| `evaluations/route_a/DEN-EF-PACKET-ACTION-GRPD-P/2026-08-14-stage8.yaml` | `28da284cd0f1be601ded15a24281a5b07937df1fd29ba8551cbf2ab9f6f9d0ee` |
| `evaluations/route_a/DEN-EF-ORBIT-ACTION-GRPD/2026-08-14-stage8.yaml` | `17defc7c1ec088e4aab5b256ec4ee19a6df126d1d3c76b86f191d3c76f5b77b9` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-REG-TRACE/2026-08-14-stage8.yaml` | `51903590ba183daa54029c7977c1a0ba5c2550cf6e685d18ec2a9bb64d5fa333` |
| `evaluations/route_a/DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE/2026-08-14-stage8.yaml` | `ddade81079ca04fcb652b0fe2810e081775afdb674c83d72c5c0844e61077e1d` |
| `evaluations/route_a/DEN-EF-GRPD-TIME-RETURN-POS/2026-08-14-stage8.yaml` | `d42df1d6dd699665e918efac61d24a38b500c4d7a3e771ef87761fd89616c22a` |

All five YAMLs parse under the exact Route-A v0.2.0 schema and enums, their
candidate IDs match their directories, and every
`route_b_invocation_allowed` is Boolean `false`.  No Route-B YAML exists.

The anti-splice conclusions are decisive:

- the packet and bare orbit records cannot inherit either trace's A1 result;
- the regular trace cannot borrow the character trace's return ledger;
- the character trace cannot borrow the regular trace's normality;
- the scalar record cannot borrow either local trace or a packet completion;
- no typed record owns a determinant (`A2_FAIL` for all five);
- no typed record owns continuation, functional equation, Gamma factor,
  completed divisor, or Weil compression (`A3_FAIL` for all five); and
- no typed record owns a natural quantization (`A4_FAIL` for all five).

## 10. Source-versus-new-proof ledger

| Claim class | Source owner and locator | Paper-8 contribution |
|---|---|---|
| source packet, clock, and isotropy | Deninger v4, equation (35), Section 6/Theorem 6.1, and Section 7 locators; survey Theorem 4.2 | corrected topology and ownership audit; no source-authored groupoid attribution |
| actual-orbit bridge | Morishita Lemmas 3.4--3.5 and target circle equation (1.1.5), restricted using Deninger `E_f` data | new corrected genuine-`E_f` compact-to-Hausdorff orbit homeomorphism |
| one-orbit completion | Williams Theorems 4.30, 5.12, and 7.13; Green/MRW/BGR as corroboration | locked-convolution specialization, induced sign, and fixed evaluation field |
| regular trace template and dual Haar | Bourne--Rennie Lemma 7.4; Renault 2021, physical pp. 3--4 | fixed Zak decomposition, faithfulness, bicommutant, FNS domains, and cancellation |
| l.s.c. character trace | Elliott--Robert--Santiago Theorem 3.11; Combes--Zettl Proposition 2.2 | exact pullback domain, dense semifiniteness, nonfaithfulness, and time-kernel value |
| Fourier and Poisson inputs | Laugesen Definition 14.1, Theorems 14.10--14.11 and 23.5 | scaled shifted formula and simultaneous sign on the fixed representation |
| measurable normality background | Jones, physical pp. 15--16 and 43--44 | finite-corner decreasing-peak no-normal-extension theorem and separate singular corner states |
| positive-time ledger | Deninger's source prime/clock ownership | new typed locally finite scalar Radon measure and closed-point coefficient audit |

The bounded novelty statement is only `SUPPORTED_WITHIN_SEARCH` through
2026-08-14.  Generic imprimitivity, Plancherel, point-evaluation singularity,
and Poisson summation are prior mathematics; the search did not locate the
same Deninger-`E_f` fixed-object bridge.

## 11. Proof-use and release constraints

The manuscript may use a theorem only if it preserves all of the following:

1. every local theorem says “one already chosen actual source orbit”;
2. every packet sentence preserves `OPEN`/`NOT_TESTABLE` rather than replacing
   it by failure or nonexistence;
3. the regular and character traces keep different owners and domains;
4. the finite corner is not called central;
5. singular extensions are called corner-state extensions only;
6. the positive-time object is called a scalar Radon measure/distribution,
   not a trace or global operator;
7. coefficient one is attributed to closed-point counting, not packet-orbit
   multiplicity or measure uniqueness;
8. controls are described as finite target-free falsification/regression
   witnesses;
9. novelty is search-bounded and dated; and
10. determinant, A3, A4, Route B, Riemann-zero, and Hilbert--Polya language is
    excluded.

## 12. Integrated verdict

The mathematical package is internally consistent and independently accepted
with no open Critical, Major, or Minor finding.  The strongest theorem is the
fixed-map dichotomy on an actual source orbit: dual-Haar regularization gives a
normal FNS trace that erases all nonzero returns, whereas a character fibre
retains the return comb but admits no normal extension to that regular
completion.  The source-clock scalar ledger remains exact after positive-time
restriction.  The strongest unresolved gate is the inherited packet topology
and packet same-map bridge, so the packet-level primary question remains
`NOT_TESTABLE`.
