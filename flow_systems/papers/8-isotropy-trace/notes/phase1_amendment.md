# Paper 8 Phase-1 amendment crosswalk

Amendment ID: `P8-PH1-AMEND-2026-08-14-v1`  
Date: 2026-08-14  
Status: **APPLIED — INDEPENDENT CONTENT RE-LOCK PASS; FINAL STATUS-BYTE CHECK PENDING**

## 1. Historical and amended locks

| Artifact | Historical reviewed SHA-256 | Amended active SHA-256 |
|---|---|---|
| `research_protocol.md` | `51c85aae8262d6fb8597d49e6c23a1926ebb24ee3c3429d996228565b4d7a547` | `127d80d98532ef150df4c74706c44047c3509c14c3498322d6dee09ed81f98c2` |
| `candidate_lock.md` | `d1d11519bd8661be1a62f5cf7bdc34e14a929a79776c52001b2a0d362082cc8a` | `25c37f5a81ad95640f31e4d7f13b0bb328b4cf5735f31c70ce3e30b0f99a699b` |

Historical reviews remain attached only to the historical bytes:

| Review | Verdict | SHA-256 |
|---|---|---|
| `phase1_methodology_review.md` | `REVISE`, 0 Critical / 3 Major / 4 Minor | `1ff32d208f5083297ed10ad23afc86f02200e6c763bf88a60ef8b30d4214aa18` |
| `phase1_devils_advocate.md` | `REVISE`, 0 Critical / 5 Major / 3 Minor | `3e01928884127fe4b3e268ecabfa9977f97e5aa32331d4a008662416deb52093` |
| `phase1_source_feasibility.md` | `REVISE`, no fatal source obstruction | `112ebfda7a1afa3c090b6acbb5630c217011d11f2540a4a8f4a0c1010d9220e5` |

## 2. Finding-to-change crosswalk

| Finding | Amendment |
|---|---|
| Per-prime and all-prime unit spaces shared one ID | Primary object is now the per-prime family `DEN-EF-PACKET-ACTION-GRPD-P`; the optional topological coproduct has its own ID, and no inherited all-prime groupoid is frozen. |
| Strongest source quotient path was omitted | Added `K_p=R/(L_pZ)` and conditional source quotient `Q_p=Gamma_p/K_p`; compact/Hausdorff/countability/local-triviality gates are separate, and `Q_p=B_p` is forbidden without T0--T7. |
| Primary “or” allowed both clauses to be true | Primary question is now the mutually decidable normal source-selected extension problem, with explicit `CONFIRM`, `REFUTE`, and `NOT_TESTABLE` outcomes.  Regular cancellation and singular return traces are complementary subclaims. |
| `source-selected`/`canonical` was undefined | Added a conjunction of source derivation, flow-automorphism invariance, frozen scale, no free transverse/cross-prime weights, and literal uniqueness. |
| Local and global time domains were mixed | Split `TIME-RETURN-LOCAL`, `TIME-RETURN-FIN`, and `TIME-RETURN-POS`; no global all-prime `C*`/`L1` operator is asserted. |
| Two-sided trace silently became a positive-time ledger | Positive time is obtained only by restricting the test function to `C_c^infinity((0,infinity))`; the result is a Radon distribution/measure, not a trace. |
| Haar/Weil/Plancherel scales were mixed | Froze `dt`, length `du`, probability `du/L`, counting Haar on `LZ`, and dual `dtheta/(2pi)` separately.  Both regular and character traces use the same scale. |
| Completion-level nonnormality lacked a fixed map | Added the explicit `C*(G_p) -> C*_r(G_p) -> M_reg` and fibre-representation diagram; full/reduced equality, factorization, compact image, and extension are independent gates. |
| `L-infinity` point evaluation was conflated with an extension | P8-6 now separates the continuous centre, singular-extension existence/nonuniqueness, and no-normal-extension theorem. |
| Packet measure class was open-ended | P8-7 quantifies over `nu_p in Prob(Q_p)` and preregisters the section-free orbit integral, exhaustion question, and transverse-observable distinction. |
| One-orbit topology credit was too broad | Registered a Paper-8 `DERIVABLE_NEW_LEMMA` using the corrected `E_f` Morishita restriction; it can close only orbit T1/T2, not packet topology or analytic transport. |
| Route ceiling was ambiguous | A1 is the maximum possible positive analytic credit; A2 is fail/not-testable, A3 fails, A4 is closed, and `route_b_invocation_allowed=false`. |
| Controls omitted scale/domain/representative checks | Added common-scale, local/finite/global, and centre-representative controls. |
| Groupoid provenance wording still implied source authorship | Classified the transformation groupoid explicitly as a canonical `DERIVABLE_NEW_DEFINITION` from source-owned packet/flow fields; Deninger's source owns neither the groupoid definition nor its analytic trace. |

## 3. Non-changes

- No theorem is declared proved by this amendment.
- No packet Hausdorffness, source transverse probability, groupoid trace,
  full/reduced equality, Morita strengthening, induced trace, or normality
  conclusion is assumed.
- No Riemann zero, Euler equality, fitted parameter, or Paper-7 proxy result is
  admitted as evidence.
- No determinant or Route-B candidate was added.

## 4. Re-lock gate

Independent methodology and source re-locks passed, and the final
devil's-advocate re-lock closed with `0 Critical / 0 Major / 0 Minor`.  One
mechanical check of the status-only byte update remains before Phase 2.  The
check must confirm that the status edit changed no mathematical content and
that the amended hashes in Section 1 match the active files.
