# Paper 9 Phase-1 amended exact-byte re-lock

Review date: 2026-08-14 (Asia/Shanghai)  
Review type: independent ARS reviewer/integrity re-lock of amendment `P9-DES-01`  
Verdict: **PASS TO PHASE 2 — C0 / M0 / m0**  
Scope: research design and exact-lock consistency only; no theorem is credited

## 1. Exact bytes reviewed

The re-lock applies only to the following three exact artifacts:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` |

The adversarial findings being re-adjudicated are in
`notes/phase1_devils_advocate.md`, SHA-256
`9fc9026a3abc78f2f17cf808cd6e816631c84744b8726f914545ed9664c5f35a`.
The methodology stress tests were checked in
`notes/phase1_methodology_review.md`, SHA-256
`8279006415439886b7a8769cc1885b5dcefdd21c1c7dfd35488a8cc5a22aedd6`.
That methodology review records the earlier lock hashes and is therefore an
advisory input, not the re-lock of the amended bytes.  This document supplies
the independent exact-byte decision required by `P9-DES-01`.

No active lock, prior review, source artifact, manuscript, pipeline record, or
Route record is modified by this review.

## 2. Re-lock decision

All five Major and two Minor design findings from the Devil's Advocate review
are closed on the amended bytes.  “Closed” here means that the exact object,
theorem obligation, decision boundary, and stop rule are now frozen well
enough for Phase 2 to test them.  It does **not** mean that the saturated
quotient lemma, CRT density, fixed-stage character convergence, universal
packet normalization, nonclosedness, or indiscreteness has already been
proved.

Phase 2 is authorized on these exact bytes.  Any byte change to one of the
three reviewed inputs invalidates this PASS and requires a new hash lock and
independent review.

## 3. Closure of the original findings

| Finding | Amended locators | Re-lock adjudication |
|---|---|---|
| M1 — restricted relation not frozen | `research_protocol.md:49-70`; `candidate_lock.md:58-70`; `phase1_design_amendment.md:12-15` | **CLOSED.** `C_p^{E_f}`, `Z_p`, `R_p`, and `Gamma_p=Z_p/R_p` are frozen on the source object. Saturation, openness of the global orbit quotient, and equality of the restricted quotient topology with the inherited packet topology are explicit theorem obligations before coordinate use. |
| M2 — arbitrary `A_p` endpoint overreaches `E_f` | `research_protocol.md:117-148`; `candidate_lock.md:72-86`; `phase1_design_amendment.md:15` | **CLOSED.** Full `A_p` density is arithmetic-only. Source-topology credit is restricted to unit targets in `U_p`; infinite-kernel endpoints are explicit negative controls outside `E_f`. |
| M3 — raw/Galois/colimit levels conflated | `research_protocol.md:72-90,134-148`; `candidate_lock.md:47-56,112-120`; `phase1_design_amendment.md:16` | **CLOSED.** `Ptilde_a`, `P_a`, and `j(P_a)` are distinct. Raw exponent convergence precedes the continuous Galois quotient and named colimit inclusion. `F_{m/p^k}(P_a)=F_m(P_a)` is quotient-only; raw-character equality is forbidden. |
| M4 — no universal packet bridge or orbit-only tier | `research_protocol.md:150-162,232-261`; `candidate_lock.md:120-123,161-168`; `phase1_design_amendment.md:17` | **CLOSED.** Unit-exponent exhaustiveness and the exact set-equivalence condition are preregistered before universalization. `CONFIRM_ORBIT` prevents promotion of an orbit theorem to full-packet indiscreteness. |
| M5 — Paper-8 correction boundary underspecified | `research_protocol.md:225-230,316-333`; `candidate_lock.md:164-175,198-207`; `phase1_design_amendment.md:18` | **CLOSED.** Actual inherited topology, retopologized circle proxy, frozen standard packet LCH-Hausdorff route, and independent scalar ledger are separate correction branches. Historical Stage-8 bytes remain immutable and Stage-9 records require explicit supersession/retyping. |
| m1 — denominator convention | `candidate_lock.md:28-44`; `phase1_design_amendment.md:19` | **CLOSED.** `N={1,2,...}` and `k in Z_{>=0}` are explicit. |
| m2 — ambiguous use of LCH | `research_protocol.md:174-186,202-207`; `candidate_lock.md:194-196`; `phase1_design_amendment.md:20` | **CLOSED.** The refutation target is the standard second-countable LCH-Hausdorff framework. Non-Hausdorff local quasi-compactness and possible replacement theories are not ruled out without separate proofs. |
| Methodology `Q_p` gate | `research_protocol.md:103-105,166-186`; `candidate_lock.md:133,140-143`; `phase1_design_amendment.md:21` | **CLOSED.** `Q_p=Gamma_p/K_p` is an intrinsic quotient that remains defined without Hausdorffness and is never identified with `B_p`. Full-packet indiscreteness descends to `Q_p`; `CONFIRM_ORBIT` alone yields no transverse classification or T3--T7/Route credit. |

## 4. Methodology stress-point audit

### 4.1 Correct residue belongs to `q_j`, not merely to `m_j`

`phase1_design_amendment.md:25-34` freezes the direct rational-residue gauge:

```text
q_j = m_j p^{-k_j},
m_j = a_j p^{k_j} (mod M_j),
```

with independent control of `|m_j/p^{k_j}-c|`.  Together with
`research_protocol.md:119-132`, this requires a cofinal finite-modulus proof
and forbids inferring profinite convergence of `q_j` from numerator convergence.
This closes the residue/gauge design defect.  In Phase 2, `a_j` must be
instantiated as the residue of the chosen target in `A_p` modulo `M_j`.

A numerator-only gauge is not silently available.  If execution instead uses
`m_j -> a`, it must additionally record a condition such as
`p^{k_j}=1 (mod M_j)` that makes that gauge equivalent.  The frozen direct
`q_j` gauge is sufficient, so the alternative is not a new lock obligation.

### 4.2 Stabilizer equality and fixed-stage topology

The amended design correctly separates two legal routes and freezes the raw
route as primary:

1. interpret `chi^{bq_j}` elementwise in the initial `p`-fibre;
2. prove every approximant is in `E_f` and prove pointwise convergence in that
   one fixed stage;
3. apply the continuous Galois quotient;
4. apply the named open colimit-stage inclusion; and
5. only then apply the suspension quotient.

The denominator may be discarded via the exact `p^Z` stabilizer only at the
quotient-point level.  The locks do not equate `chi^{bmp^{-k}}` with
`chi^{bm}`.  Relevant locators are `research_protocol.md:78-90,134-148` and
`candidate_lock.md:47-56,112-120`.

This is a PASS on proof architecture, not proof of continuity or convergence.
Failure to source any named arrow in Phase 2 triggers the stop rule at
`research_protocol.md:350-352`.

### 4.3 Unit normalization and universal scope

The universal packet claim is now conditional on a separate set-level lemma:
every finite-kernel exponent is normalized, using the diagonal action, to a
unit exponent while its nonunit factor is transferred to the positive real
coordinate.  The exact packet equivalence modulo `p^{Zhat}` and time
stabilizer `p^Z` must then be proved.  See
`phase1_design_amendment.md:34-36`, `research_protocol.md:157-162`, and
`candidate_lock.md:120-123`.

This prevents the chosen-chart calculation from being reported as full packet
indiscreteness.  If only the same-exponent/orbit specialization closes,
`CONFIRM_ORBIT` is the ceiling; if only one distinct specialization closes,
`CONFIRM_MINIMAL` is the ceiling.  `CONFIRM_STRONG` requires arbitrary ordered
packet points after normalization and distinctness checks.

### 4.4 Morishita inherited/proxy split

The namespace now distinguishes:

```text
MOR-CC-Cp-INHERITED
MOR-CC-Cp-STD-CIRCLE-PROXY
```

The first carries only the subspace topology inherited from the exact adelic
quotient; the second carries the separately imposed ordinary circle topology.
No occurrence of “circle,” “isomorphic,” or a continuous set bijection can
transport Hausdorffness between them.  See
`research_protocol.md:92-110,188-194`, `candidate_lock.md:125-138`, and
`phase1_design_amendment.md:38-40`.

Accordingly, a Phase-2 theorem may find the actual Deninger and actual
Morishita inherited orbits compatible while refuting their identification
with the Hausdorff standard-circle proxy.  It may not infer the Morishita
topology from the expected approximation mechanism; that topology still
requires a direct source/quotient audit.

### 4.5 Intrinsic orbit quotient `Q_p`

The amended tuple removes the earlier ambiguity around “when meaningful.”
`Q_p=Gamma_p/K_p`, with `K_p=R_{>0}/p^Z`, is frozen as an always-defined
topological quotient of the continuous source-flow action and as an object
distinct from `B_p`.  This is coherent without a Hausdorff hypothesis.

The result boundary is also correct: a quotient of an indiscrete
`Gamma_p` is indiscrete, whereas indiscreteness of each individual orbit does
not determine the topology transverse to those orbits.  Thus
`CONFIRM_STRONG` licenses the stated `Q_p` conclusion and `CONFIRM_ORBIT` does
not.  Neither conclusion supplies a measure, product chart, completion, or
analytic Route coordinate.  See `research_protocol.md:103-105,166-186` and
`candidate_lock.md:133,140-143`.

## 5. Exact Phase-2 acceptance and stop boundary

The PASS opens only the bounded source/topology audit.  Phase 2 must still
close, with exact source locators:

1. the source definition and `Q_{>0}`-invariance/saturation of `C_p^{E_f}`;
2. the open restricted-quotient lemma and equality with the inherited
   `Gamma_p` subspace topology;
3. the constructive `q_j` congruence and real-error estimates for a cofinal
   modulus system;
4. legality in `E_f` and convergence in one fixed character stage;
5. continuity and order of the Galois quotient, colimit inclusion, and
   suspension quotient maps;
6. exact `p^Z` isotropy, `p^{Zhat}` transverse equivalence, and distinctness;
7. the unit-normalization/exhaustiveness lemma before a universal packet
   statement; and
8. the topology of Morishita's actual adelic quotient independently of the
   ordinary circle proxy; and
9. the source continuity/kernel statement for the `K_p` action defining
   `Q_p`, without importing the topology of `B_p`.

If any load-bearing arrow is merely set-theoretic, unavailable on the retained
source manifestation, or valid only after importing a proxy topology, the
project must stop at the corresponding named arrow and assign the strongest
licensed tier, including `NOT_TESTABLE` where appropriate.  Finite CRT or
finite-character controls remain regression checks, not theorem evidence.

No Phase-2 result may yet edit Paper-8 historical bytes, issue Stage-9
supersession records, begin a non-Hausdorff completion theory, promote A2--A4,
or create Route-B YAML.  Those actions remain conditional on later proof and
evaluation gates.

## 6. Final checkpoint

```text
Critical: 0
Major:    0
Minor:    0
Verdict:  PASS TO PHASE 2 ON THE THREE EXACT HASHES IN SECTION 1
```

The amendment resolves the design-level objections without converting any
conjectured topology conclusion into a result.  The next legitimate step is
the exact source and topology audit under P9-1--P9-9.

AI-assisted review disclosure: this independent re-lock used AI-assisted local
exact-byte comparison and adversarial mathematical analysis.  It used no web
search, external model upload, Riemann-zero data, fitted parameter, manuscript
claim, or modification of the active artifacts.
