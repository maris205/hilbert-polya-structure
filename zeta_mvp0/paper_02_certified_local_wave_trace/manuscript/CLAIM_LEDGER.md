# Paper 02 manuscript claim ledger

Last updated: 2026-08-09.

This ledger controls what may enter the abstract, theorem statements, figures,
and conclusion.  “Accepted” means that the named analytic proof or release
chain exists; it does not enlarge the domain stated in that source.

| ID | Statement | Authority | Status | Non-negotiable boundary |
|---|---|---|---|---|
| P02-C1 | The energy-localized relative propagator trace is a finite-rank, eigenvalue-only spectral object. | A4.3 and the exact staircase/Fourier identities | accepted identity | no first-resolvent trace-class assertion |
| P02-C2 | The fast normal mode at (a=1.02) has explicit limiting period, action slope, transverse determinant, and first nonlinear period coefficient. | A4.4--A4.5 and the independent derivation audit | accepted proposition | near-bottom local statement, not a global orbit classification |
| P02-C3 | For every sufficiently small fixed positive energy excess, one primitive warped return gives the positive-time relative Gutzwiller term. | A4.8--A4.10 plus the finite-time CRR hypothesis audit | accepted with (0<\delta<\delta_{\rm tr}) | (delta_{\rm tr}>0) is not yet quantitative |
| P02-C4 | One real-analytic primitive branch exists and is unique inside the frozen local boxes for (0\le\epsilon\le0.101). | A4.12 / `R401-VAL-L1-V2` | `PASS_CONTIGUOUS_LOCAL_BRANCH` | no root-complement, phase-cover, or global uniqueness claim |
| P02-C5 | On the P02-C4 branch, (det(I-D\Pi_\epsilon)>3). | A4.13 / `R401-VAL-L1-MG-V2` | `PASS_LOCAL_MONODROMY_GAP` | not the final independent event-projected/Taylor-width cross-check |
| P02-C6 | At (delta=0.01), the frozen eight-point (hbar) computation approaches the A4.10 coefficient. | `R401-SC` and its 58-check independent recomputation | numerical diagnostic | does not establish (0.01<\delta_{\rm tr}) |
| P02-C7 | The L2 complement engine closes six representative `(precision, slab)` trees. | frozen `R401-VAL-L2-S0` producer/checker, postcheck, and release provenance | `PASS_IMPLEMENTATION_SMOKE`; 3,016 nodes and 89,962 zero-failure checker gates | implementation certificate on S000/S025/S050 only, not the other 48 slabs |
| P02-C8 | For every frozen slab and parameter value, the reduced return map has exactly the accepted L1 root in the declared local box. | A4.15 / `R401-VAL-L2-A1`, combined with the accepted L1 release | `PASS_LOCAL_COMPLEMENT_ALL_SLABS`; 102 trees, 52,790 nodes, and 158,782 zero-failure checker gates | local `P_+=0` reduced chart only; no phase/global cover or quantitative trace-radius promotion |
| P02-C9 | The construction supplies rational-prime times or von-Mangoldt amplitudes. | none | open / unauthorized | required before any zeta-zero comparison |
| P02-C10 | The operator spectrum equals the nontrivial zeta-zero ordinates or proves RH. | none | not claimed | full Hilbert--Pólya and arithmetic chain remains incomplete |

## Promotion rule

P02-C7 was promoted from “pending” to `PASS_IMPLEMENTATION_SMOKE` only after
the frozen six-tree producer, independent exact-decimal checker, postcheck,
and release provenance agreed with zero failures.  This promotion does not
change P02-C3's theorem domain or any status below P02-C7.

P02-C8 was promoted only after the prospectively frozen 102-tree archive,
the independent exact-rational checker, postcheck, A4.15 certificate, and
write-once 19-role release agreed with zero failures.  The promotion closes
the local root complement, but it does not close the phase/flow-box or global
return covers and does not imply that \(0.01<\delta_{\rm tr}\).

Any later global-cover result receives a new claim ID and a new frozen
protocol; it may not silently reuse the representative-smoke label.
