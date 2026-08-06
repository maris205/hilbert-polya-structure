# Experiment Tracker

| Run | Purpose | Status | Decision |
|---|---|---|---|
| R000 | classical warp screen | complete | \(a=1.02,n=1,2\) retained; radial rejected; stiff high-iterate \(a=6\) branches recorded |
| R001 | duration convergence | complete | all frozen gates passed |
| R100 | first quantum mesh comparison | complete | failed 1% level gate; no RMT claim |
| R101 | add \(h=0.0225\) | complete | level gates passed; \(a=6\) spacing extrapolation failed |
| R102 | fourth core grid | complete | \(a=1.02,B=0,1\) core passed |
| R103 | frozen six-field scan | complete | resolved nonmonotone response; no optimum selected |
| R104 | second-grid field check | complete | all gates passed |
| R105 | numerical integrity audit | complete | residual, orthogonality, gauge, sign, rerun passed |
| R106 | adaptive classical replication | complete | all four preregistered gates passed |
| R107 | fourth-order FD check | complete | physical gates passed; maximum residual failed |
| R107A | guard-mode remediation | complete | all unchanged R107 gates passed |
| Window audit v2 | recompute R100--R104 aggregates on the declared 25/15 discard | complete | historical summaries retained; manuscript/figures use corrected 140-level aggregates; no gate reversal |
| R200-S | common-grid relative-trace implementation smoke | complete | 8/8 cells and independent checker passed; production/scientific gates not evaluated; grid convergence failed production scale |
| R200 | relative trace production | frozen parent protocol only | not executed; B/C remain blocked by grid and certified-tail requirements |
| R108-S | independent polygonal-domain P1 FEM smoke | complete | implementation/checker passed, but frozen coarse/fine medians failed: 2.712% at B=0 and 2.883% at B=1 versus <2%; no promotion |
| R108-C0 | same-mesh complex P2 order-isolation remediation | terminated: `INVALID_OR_INCOMPLETE` | M0 and four P1 controls passed; first P2 all-96 solve failed equation and mass-dual residual gates only at mode 96 and was quarantined; formal C0=`NOT_EVALUATED`; no P2 convergence claim |
| R108-C1 | constrained quality-mesh three-grid continuation | blocked; not authorized | C0 did not pass; R108-P and R200 production remain blocked under this branch |
| R400 | near-bottom fast Lyapunov period/action/stability certificate | complete | 6/6 cells, analytic intercept/slope gates, and 66-check independent postcheck passed; local classical certificate only |
| R401-SC | fixed-energy eigenvalue-only \(\hbar\)-ladder | complete / PASS | 8/8 cells from \(4\times10^{-4}\) to \(4\times10^{-5}\), all integrity gates, 58 independent recomputation checks, and 74 current tests passed; finest \(Z_\hbar=1.006523+0.013300i\), \(|Z-1|=0.01481\), phase \(0.0132135\) rad, \(|Z-Z_{\rm har}|=0.00205\); fixed-energy support only |
| A4.11a | quantitative radial theorem-domain component | complete / PROVED | explicit vector-Wirtinger/Hessian bound gives \(T>0.99\) for all radial periodic orbits with \(0<\delta\le0.010201\), hence \(\bar\delta(0.75)\ge0.010201\); A4.13 later closes local-branch \(D>3\), while warped \(\delta_*\) and the protocol-level independent \(\delta_{\rm nd}\) cross-check remain |
| A4.11b | quantitative warped period floor | complete / PROVED / independently accepted | convex-box outward Hessian bound \(\|\nabla^2V_a\|<103\) gives \(T>0.60\) throughout \(0<\delta\le0.010201\); remaining validated cover is only \([0.60,0.75]\) |
| R401-VAL-V2 | validated theorem-domain protocol | composite FROZEN / two-round independent review ACCEPT / implementation active | base SHA-256 `d00d95f32...a20d82`, amendment `a163be880...e62aa`; V2 replaces an impossible raw determinant-range width gate by a shared-parameter exact-rational Taylor-model remainder/residual gate without weakening \(D>3\), coverage, or replay obligations |
| R401-VAL-A0 | Arb analytic/shell implementation smoke | complete / PASS_IMPLEMENTATION_SMOKE | 128/256-bit runs, 60 shell identities per precision, all analytic/special-function gates, protocol/proof hashes, and 15-check independent recomputation pass; no validated ODE claim |
| R401-VAL-L0 | original CAPD endpoint local-slab attempt | **INVALIDATED; audit archive only** | midpoint energy gradient in the first Krawczyk Jacobian row failed to enclose the exact derivative over the root box; no L0 margin, checker status, or pass claim may be cited |
| R401-VAL-L1-V2 | corrected contiguous local fast branch | complete / **PASS_CONTIGUOUS_LOCAL_BRANCH** | 51 primary slabs + 50 guarded bridge hulls at each of 128/256 MPFR bits, 202/202 jobs; exact-rational checker replays all 202 certificates and passes 3973 aggregate checks; cover \(\epsilon\in[0,0.101]\), analytic fast anchor, recovered full \(Q_+\) return, and primitive connected branch; 128/256 minimum margins \(9.323437\times10^{-6}\)/\(9.328825\times10^{-6}\), maximum contractions \(0.0339894\)/\(0.0290133\), minimum phase slope \(8.95504\); uniqueness is local to frozen boxes, so root complement, global cover, \(\delta_{\rm tr}\), and P0 remain open |
| R401-VAL-L1-MG V1 | first derived monodromy-gap release | **SUPERSEDED / NON-LICENSING DISPLAY** | exact-fraction \(D>3\) core remains valid and preserved, but nearest-float Markdown bounds were not directionally rigorous; archived under `r401_val_l1_monodromy_gap.attempt1-superseded-nondirected-display`; V2 is authoritative |
| R401-VAL-L1-MG-V2 / A4.13 | uniform transverse gap on the accepted local branch | complete / **PASS_LOCAL_MONODROMY_GAP** | invariant quotient proves \(\det(I-D\Pi)=4-\operatorname{tr}M\); 202 determinant plus 202 phase-slope replays, 815 directed-decimal payloads, and 8302 aggregate checks pass; 128/256 rigorous minimum lower endpoints are 3.835992606647717183/3.850741968945794693; local branch only, so independent event-projected \(D\Pi\), Taylor residual, root complement, phase/global cover, \(\delta_{\rm tr}\), and P0 remain open; `final_status` is null |

## Current evidence labels

- Q/W: theorem.
- Active geometry: proved identity/lemma.
- Classical S: sampled numerical support at the frozen states.
- Quantum symmetry response: converged finite-window support with an
  independent-order FD check.
- Relative container C: proved admissibility, not a P pass.
- Observable-localized interface \(P^*_{\rm loc,obs}\): proved intermediate
  route, but it contains eigenfunction matrix elements.
- Eigenvalue-only local periodic-orbit interface \(P^*_{\rm loc}\): proved
  for each sufficiently small fixed energy excess as \(\hbar\downarrow0\),
  using whole-shell uniqueness and the finite-time CRR formula.
- Numerical \(P^*_{\rm loc}\) audit: R401-SC passed at \(\delta=0.01\) down
  to \(\hbar=4\times10^{-5}\), including the absolute (1/(2\pi)\)
  normalization and complex phase.  The proof threshold in \(\delta\) is
  still unknown, so this does not quantify the theorem's domain.
- Validated local-domain branch: R401-VAL-L1-V2 connects the analytic fast
  endpoint across \(\epsilon\in[0,0.101]\) and recovers the primitive full
  return, but only within its frozen primary boxes and guarded bridge hulls;
  it does not close the root complement or global cover and does not promote
  \(\delta_{\rm tr}\) or P0.
- Validated local transverse gap: A4.13/R401-VAL-L1-MG-V2 proves
  \(\det(I-D\Pi)>3\) uniformly on that branch.  It does not replace the
  independent event-projected/Taylor-identity gate or extend the claim to
  roots outside the certified boxes.
- Periodic-orbit arithmetic P: open.
- Individual zeta zeros/RH: excluded.
