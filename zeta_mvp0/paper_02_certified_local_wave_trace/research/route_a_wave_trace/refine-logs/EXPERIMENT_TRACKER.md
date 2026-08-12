# Experiment Tracker

| ID | Status | Result | Next action |
|---|---|---|---|
| Route A4 unit tests | COMPLETE | 7 dedicated route tests and 74 full-suite tests pass, including validated-branch/monodromy contracts, phase, transformed-metric, radial-oracle, and harmonic-window checks | retain in full regression |
| R400 six-cell run | COMPLETE / PASS | all numerical and asymptotic gates pass | freeze final archive |
| R400 independent checker | COMPLETE / PASS | all checks and independent \(\delta=0.05\) solve pass | freeze postcheck |
| Normal-form proof audit | COMPLETE / ACCEPT | independent derivation matches every coefficient and constant | retain proof text and R400 audit |
| Lyapunov-centre proof audit | COMPLETE / ACCEPT | exact integer-nonresonance and energy parameterization written | retain Alligood--Yorke Section 4 source lock |
| Radial exclusion | COMPLETE / PROVED | qualitative compactness proof plus A4.11a vector-Wirtinger/Hessian bound: \(T>0.99\) throughout \(0<\delta\le0.010201\), hence \(\bar\delta(0.75)\ge0.010201\) | retain analytic margin; certify warped \(\delta_*\) and \(\delta_{\rm nd}\) |
| Warped period floor | COMPLETE / PROVED / ACCEPT | A4.11b convex-box Hessian estimate gives \(\|\nabla^2V_a\|<103\) and hence \(T>0.60\) throughout \(0<\delta\le0.010201\) | validated cover only \([0.60,0.75]\) |
| CRR phase index | COMPLETE | \(\sigma_+^{\mathrm{CRR}}=1\bmod4\), phase \(+i\); negative time has phase \(-i\) | convention frozen and used successfully in R401 |
| Whole-shell fast-orbit uniqueness | COMPLETE / ACCEPT | A4.8: blow-up, limiting return classification, Poincaré IFT, iterate exclusion, and globalization | retain common small-energy threshold |
| Finite-time CRR specialization | COMPLETE / ACCEPT | A4.9 has observable symbol \(A_{\rm obs}\equiv1\), exact H.1--H.5 map, common threshold, phase convention, and fixed-data remainder | retain independent review record |
| R401 \(\hbar\)-ladder | COMPLETE / PASS | 8/8 integrity cells, all scientific gates, 58 independent checks, and 74 current regression tests pass; finest \(Z=1.006523+0.013300i\) | next strict work is the R401-VAL local-complement/global and independent determinant-identity certificate; reserve R401-FC/R401-ID for optional continuations |
| R401-VAL-V2 protocol | COMPLETE / COMPOSITE FROZEN / ACCEPT | base SHA-256 `d00d95f32...a20d82`, amendment `a163be880...e62aa`; shared-parameter exact-rational Taylor-model determinant gate, analytic/global/local cover identity, interval-Newton and phase-cover trees, independent proof-object replay, and honest namespaced statuses | validated production |
| R401-VAL-A0 analytic smoke | COMPLETE / PASS_IMPLEMENTATION_SMOKE | Arb 128/256-bit exact constants, `exprel`/`log1prel`, normal coordinates, analytic bounds, 60 shell points per precision, frozen hashes, and 15 independent checks pass | retained as analytic implementation oracle |
| R401-VAL-L0 local endpoint slab | INVALIDATED / NON-LICENSING | archived computation used a midpoint energy gradient in the first Krawczyk Jacobian row rather than the full root box; preserved as `r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian` | do not cite as a passed milestone; superseded by L1-V2 |
| R401-VAL-L1 attempt 1 | INVALIDATED / NON-LICENSING | 202 interval jobs and arithmetic replays passed, but separately rounded unpadded bridge hulls failed literal printed-box containment by a terminal decimal ULP; preserved as `r401_val_l1_branch.attempt1-invalid-bridge-rounding` | do not repair with a comparison tolerance; superseded by prospectively frozen guarded hulls |
| [A4.12 / R401-VAL-L1-V2](../A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md) contiguous local branch | COMPLETE / LOCAL-BOX COMPUTER-ASSISTED THEOREM / PASS_CONTIGUOUS_LOCAL_BRANCH | 51 primary plus 50 guarded bridge jobs at each of 128/256 MPFR bits cover \(\epsilon\in[0,0.101]\) (202/202 total); checker PASS with 202 exact-rational Krawczyk replays and 3973 aggregate checks; analytic fast anchor and energy-monotonicity full-state recovery identify one primitive branch, using A4.11b for \(\epsilon>0\) and exact harmonic dynamics at \(\epsilon=0\) | A4.13 separately closes \(D>3\), and A4.15 separately closes the local complement; phase/global covers remain open; `final_status` remains null, with no \(\delta_{\rm tr}\) or \(P_0\) promotion |
| R401-VAL-L1-MG V1 | SUPERSEDED / NON-LICENSING DISPLAY | all exact-fraction determinant inequalities remain preserved, but nearest-float Markdown lower/upper displays lacked directional guarantees | retained as `r401_val_l1_monodromy_gap.attempt1-superseded-nondirected-display`; cite V2 only |
| [A4.13 / R401-VAL-L1-MG-V2](../A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md) local transverse monodromy gap | COMPLETE / LOCAL-BRANCH COMPUTER-ASSISTED THEOREM / PASS_LOCAL_MONODROMY_GAP | invariant quotient plus positive phase slope proves \(\det(I-D\Pi)=4-\operatorname{tr}M\); 202 determinant and 202 phase-slope replays, 815 directed-decimal payloads, and 8302 aggregate checks pass; 128/256 rigorous minimum lower endpoints are 3.835992606647717183/3.850741968945794693 | local branch only; independent event-projected \(D\Pi\), Taylor-model residual, phase/global cover, \(\delta_{\rm tr}\), and P0 remain open; `final_status` remains null |
| [A4.14 / R401-VAL-L2-S0](../A414_REPRESENTATIVE_LOCAL_COMPLEMENT_SMOKE.md) representative complement smoke | COMPLETE / IMPLEMENTATION CERTIFICATE / PASS_IMPLEMENTATION_SMOKE | six trees on S000/S025/S050 contain 3,016 nodes; all 1,532 leaves are exclusions; 89,962 independent checks pass with zero failures | bounded engine certificate used before A1 freeze; no independent theorem-domain promotion |
| [A4.15 / R401-VAL-L2-A1](../A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md) all-slab local complement | COMPLETE / LOCAL-CHART COMPUTER-ASSISTED THEOREM / PASS_LOCAL_COMPLEMENT_ALL_SLABS | 102 trees on all 51 slabs contain 52,790 nodes; all 26,803 leaves are exclusions; every frontier closes; 158,782 independent checks and the 19-role release replay pass with zero failures | frozen local `P_+=0` reduced chart only; phase/global covers, independent event projection, Taylor residual, \(\delta_{\rm tr}\), P0, zeta-zero, and RH gates remain open or unauthorized; `final_status` remains null |
| High-energy Route A2 | OPEN | scaling obstruction identified | separate proposal |
| Prime/zero comparison | UNAUTHORIZED | P gate open | do not run |

## Final R400 artifact

`results/r400_local_period_smoke/`

The final run and independent postcheck both report `PASS`.  Two earlier
serialization/reporting attempts are retained with explicit names and were
not edited into the final archive.

## Final R401 artifact

`results/r401_fixed_energy_trace_smoke/`

The final run and no-production-import checker both report `PASS`.  The
initial JSON serialization attempt and the first guard-gap run are retained
as explicitly named failed archives.  Neither was edited into the final
result.
