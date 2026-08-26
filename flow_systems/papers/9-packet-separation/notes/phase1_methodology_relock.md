# Paper 9 Phase-1 amended methodology and same-object re-lock

Review date: 2026-08-14 (Asia/Shanghai)  
Review type: narrow independent ARS methodology/reviewer/integrity re-lock  
Decision: **PASS — EXACT-BYTE PHASE-1 RE-LOCK CLOSED**  
Open findings: **0 Critical / 0 Major / 0 Minor**

## 1. Exact amended-byte lock and independence boundary

This review tests only whether the amended Phase-1 design closes the prior
methodology and same-object findings.  It performs no new source search, proof
audit, computation, manuscript work, or Route evaluation.  It does not edit an
active lock, Paper-8 artifact, source, manuscript, registry, or YAML.

| Exact input | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` |
| `notes/pipeline_state.md` | `8e2b5d26b138f7fb5052b720ddbda6a868aa71351429f8863b8b144d395513c8` |
| prior `notes/phase1_methodology_review.md` | `8279006415439886b7a8769cc1885b5dcefdd21c1c7dfd35488a8cc5a22aedd6` |
| prior `notes/phase1_devils_advocate.md` | `9fc9026a3abc78f2f17cf808cd6e816631c84744b8726f914545ed9664c5f35a` |

The verdict attaches only to this tuple.  During review an intermediate tuple
(`bc62...`, `ea0e...`, `2bbf...`) was found to leave `Q_p` conditional and
untyped.  That tuple received an intermediate `REVISE`; the active tuple above
supersedes it and was reread after the narrow repair.  This report does not
transfer the verdict across any future byte change.

## 2. Narrow closure matrix

| Required closure | Verdict | Exact amended evidence and boundary |
|---|---|---|
| congruence of `q_j=m_jp^{-k_j}` itself | **PASS** | `phase1_design_amendment.md` freezes `m_j=a_jp^{k_j} (mod M_j)` plus an independent real-error bound and forbids inferring rational profinite convergence from numerator convergence alone. |
| raw/Galois/colimit three-level gauge | **PASS** | Protocol Section 2 and candidate Sections 2/5 distinguish `Ptilde_a`, `P_a`, and `j(P_a)`, require raw pointwise convergence first, and permit `F_{m/p^k}(P_a)=F_m(P_a)` only at the quotient point with `p^Z` stabilizer. |
| unit-exponent exhaustiveness | **PASS** | Protocol P9-3 and candidate Section 5 require the set-level normalization of every packet point to `[P_a,u]`, `a in U_p`, before universal packet closure; `CONFIRM_ORBIT` blocks orbit-to-packet promotion. |
| Morishita inherited/proxy split | **PASS** | `MOR-CC-Cp-INHERITED` and `MOR-CC-Cp-STD-CIRCLE-PROXY` are separate typed objects in both locks; “isomorphic” supplies no homeomorphism. |
| Paper-8 actual `REFUTED` versus downstream `NOT_TESTABLE` | **PASS** | Protocol Section 9 refutes/supersedes the actual Hausdorff/LCH premise, retypes surviving formulas to the circle proxy, explicitly makes actual-source normal-extension claims `NOT_TESTABLE` when their completion gate is lost, and preserves the scalar ledger separately. |
| intrinsic quotient `Q_p` | **PASS after narrow repair** | Both locks now type `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P`, define `K_p=R_{>0}/p^Z`, freeze the quotient topology as always meaningful, separate it from `B_p`, make its indiscreteness conditional on `CONFIRM_STRONG`, and deny `CONFIRM_ORBIT` any transverse conclusion. |
| Route-A/Route-B ceiling | **PASS** | Source A0 is bounded; A1 is at most weak and may fail for the frozen LCH-Hausdorff branch; A2--A4 fail; Route B and Route-B YAML are forbidden.  The bare `Q_p` receives no automatic T3--T7 or analytic Route credit. |

All requested closures are now explicit without moving a theorem result into
Phase 1 or changing the actual topology after observing an outcome.

## 3. Exact map and topology checks

### 3.1 CRT and finite-kernel route

The amended design distinguishes two statements:

1. density of `Z[1/p]_{>0}` in `R_{>0} x A_p` is an arithmetic theorem; and
2. source convergence uses a target in `U_p`, so the limiting character stays
   inside `E_f`.

For each finite modulus the witness must check the residue of
`m_jp^{-k_j}`, not merely `m_j`, and must separately bound
`|m_j/p^{k_j}-c|`.  At the source level, `chi^{bq_j}` is a legal finite-kernel
character and converges in the initial fibre before the continuous Galois
quotient and named open colimit-stage inclusion are applied.  The
quotient-level stabilizer identity cannot be back-propagated into an equality
of raw characters.  These rules close the denominator/gauge defect without
assuming the topology theorem.

### 3.2 Universal scope

The unit-exponent exhaustiveness lemma is a separate set theorem.  Until it is
proved, the strongest licensed universal result is `CONFIRM_ORBIT`.  Only its
closure permits `CONFIRM_STRONG` on all ordered packet-point pairs.  The exact
equivalence modulo `p^{Zhat}`, time stabilizer `p^Z`, and distinctness witness
remain independent obligations; set parametrization supplies no topology.

### 3.3 Restricted quotient ownership

The active source object is now

```text
Z_p=C_p^{E_f} x R_{>0},
R_p={((P,u),(F_qP,q^{-1}u)):q in Q_{>0}},
Gamma_p=Z_p/R_p.
```

The saturated open-quotient lemma equating this quotient topology with the
inherited packet subspace topology is preregistered before the coordinate
argument.  Thus a later nonclosed-relation witness belongs to the actual
packet, not merely to a coordinate quotient.

## 4. `C_p`, `Q_p`, Paper 8, and Route boundaries

Morishita's actual adelic quotient subspace and the ordinary Hausdorff circle
are now different IDs.  A continuous map into the former cannot borrow the
topology of the latter from the word “circle.”

The intrinsic quotient

```text
Q_p=Gamma_p/K_p,  K_p=R_{>0}/p^Z,
```

is always a meaningful topological quotient.  If `CONFIRM_STRONG` proves
`Gamma_p` indiscrete, the quotient definition forces `Q_p` indiscrete; its
`T0` status still requires the set-cardinality check demanded by P9-4.
`CONFIRM_ORBIT` alone says nothing transverse.  No outcome identifies `Q_p`
with `B_p` or gives it a Hausdorff base, local trivialization, Radon
disintegration, groupoid, trace, determinant, or Route coordinate.

The Paper-8 correction is correctly claim-specific:

- the actual standard-circle/Hausdorff/LCH premise is `REFUTED` if the
  obstruction theorem closes;
- actual-source completion-dependent representation, trace, and
  normal-extension claims become `NOT_TESTABLE`;
- Poisson/Floquet, regular FNS, finite-corner, and proxy no-normal-extension
  mathematics may survive only after retyping to
  `DEN-EF-ORBIT-STD-CIRCLE-PROXY`; and
- the positive-time coefficient-one scalar ledger remains independently
  typed and supplies no packet topology or completion.

For Route evaluation, the source topology theorem may retain at most the
locked A0/A1 ceiling, while failure of the frozen standard LCH-Hausdorff
groupoid branch may receive `A1_FAIL` only on that exact versioned owner.
Every record remains `A2_FAIL/A3_FAIL/A4_FAIL`; Route B remains false.  No
coordinate may be maximized across the packet, quotient, proxy trace, and
scalar rows.

## 5. Controls and non-promotions

The `p^Z`-only suspension remains the decisive Hausdorff-circle control.  The
wrong-sign action is an orientation control, not a guaranteed negative
topology control: simultaneous density can persist after inversion.  An
infinite-kernel limit is admissible only in the ambient arithmetic density
test, never as an `E_f` endpoint.  Finite CRT/character tables remain
regression evidence and cannot prove density, indiscreteness, or relation
nonclosedness.

A negative separation theorem stops the standard analytic branch.  It does
not construct or exclude every possible non-Hausdorff groupoid algebra, Haar
system, trace, or determinant.  Any such replacement would require a new
candidate and lock.

## 6. Exact-lock verdict

**PASS — 0 Critical / 0 Major / 0 Minor.**  The exact tuple in Section 1
closes the `q_j` congruence, three-level gauge, unit-exhaustiveness,
Morishita-topology, Paper-8 status, intrinsic-`Q_p`, and Route-boundary gates.
The design is falsifiable, same-object safe, and authorized to enter Phase 2
source verification.  No theorem, Paper-8 supersession, Stage-9 Route result,
or proxy-to-source transport is granted by this Phase-1 verdict.
