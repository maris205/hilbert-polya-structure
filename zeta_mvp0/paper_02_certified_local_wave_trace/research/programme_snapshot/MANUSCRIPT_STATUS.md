# Paper 7 Manuscript Status

## Current analytic-v3 artifact

- Title: *Clock-Preserving Hénon Warps of an Exponential Schrödinger
  Operator: Strict One-Step Ground-State Ordering and Relative Heat
  Asymptotics*
- Author: Liang Wang, School of Artificial Intelligence and Automation,
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China
- Corresponding author: `wangliang.f@gmail.com`
- Final PDF: `paper_analytic_v3/paper7_analytic_v3_round2_final.pdf`
- Pages: 45
- SHA-256:
  `e961e1b65963b2b769d7454e27913bbfa57c60d9e46849b4c8f5834a900ab0ff`

This separately versioned manuscript has completed two independent
review--revision rounds.  Three final read-only audits accepted the strict
ground-state proof, the uniform relative heat proof and figure, and the
whole-paper scope/citation/layout ledger.

## Immutable Round-2 baseline

- Title: *Clock-Preserving Hénon Warps of an Exponential Schrödinger
  Operator: Two Growing Riemann--von Mangoldt Terms and Finite-Window
  Diagnostics*
- Author: Liang Wang, School of Artificial Intelligence and Automation,
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China
- PDF: `paper/paper7_round2_final.pdf`
- Pages: 35
- SHA-256:
  `8ad75ae285244bef380d6474b7e1a4ecb943b6fe96d03fa99c9efd44192a3339`

The PDF above remains an immutable Round-2 baseline.  It was not overwritten
while analytic-v3 was developed.

## Post-freeze analytic addendum

Two stronger spectral-activity results are now proved and independently
reviewed:

\[
\lambda_1(\mathsf H_{a,\hbar})>\lambda_1(\mathsf H_{0,\hbar}),
\qquad a>-1,\ a\ne0,\ \hbar>0,
\]

and, for one fixed warp,

\[
\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
=-\frac{a^2}{24\pi}
\left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
+O_{a,\hbar}(tL^4).
\]

The complete manuscript proofs are in
`paper_analytic_v3/sections/appendix_analytic_activity.tex`; the two-round
audit is in `paper_analytic_v3/reviews/`.  These results upgrade operator
spectral activity, not the rational-prime P or explicit-zero Z gates.

## Evidence ledger

The immutable analytic-v3 manuscript itself freezes the pre-Route-A4 ledger
printed in that PDF.  The current post-freeze research ledger is stronger but
still stops strictly before arithmetic:

\[
\boxed{\text{Q/W and S}_{\rm op}\text{ proved; C admissible; }
P^*_{\rm loc}\text{ proved; }P^*_{\rm loc,num}\text{ passed; }
P_0\text{ open; Z unauthorized; RH not claimed.}}
\]

The exact classical count is

\[
\mathcal N_{\rm cl}(E)
=\frac{E}{2\pi}\log\frac{E}{2\pi}
-\frac{E}{2\pi}+1.
\]

For every fixed \(a>-1\), \(a\ne0\), fixed iterate \(n\), and fixed field
\(B\), the proved quantum count is

\[
N_{a,n,B}(E)
=\frac{E}{2\pi}\log\frac{E}{2\pi}
-\frac{E}{2\pi}
+O_{a,n,B}\!\left(E^{3/4}(\log E)^{1+2^{n-1}}\right).
\]

The quantum theorem does not resolve \(+1\), \(7/8\), \(S(E)\), or
individual zeta ordinates.

## Analytic-v3 reproducibility

- 58 tests pass.
- Eight figures regenerate; the new relative-heat figure uses a
  cancellation-free lower-tail integral and agrees with an independent
  60-digit calculation to maximum absolute error \(1.25\times10^{-14}\).
- 77 BibTeX entries are audited and 67 distinct references are printed.
- The final four-pass build has no undefined citation/reference, no rerun
  warning, and no overfull box; all fonts are embedded.
- The Hénon prior-work citation points to the exact 17-page PDF at fixed Git
  commit `f86bf21a32ad5bcb21ba81d312cc68e91bcc7db0`, not to the different
  21-page Zenodo expansion.

## Frozen baseline reproducibility

- 13 tests pass.
- Seven figures regenerate from frozen JSON/NPZ/CSV data.
- The shared production window has 140 levels, 139 gaps, and 138 adjacent
  ratios.
- Historical level-change summary fields are preserved; the authoritative
  modes-25--164 correction is versioned in
  `results/QUANTUM_WINDOW_AUDIT.json`.
- 59 distinct references are printed; no citation key is missing.

## Research mode

RH remains a breadth-first unknown-object search: generate distinct
structures, apply cheap death tests, and promote only analytic survivors.
Once a survivor exists, Route A switches to theorem engineering: write the
shortest conditional chain and attack the minimum missing bridges.  The
current family has crossed Q/W, the centered one-step scalar
\(S_{\mathrm{op}}\) gate, and the local eigenvalue-only periodic-orbit
interface \(P^*_{\rm loc}\), but not the arithmetic gate \(P_0\).

R200-S and the genuinely independent R108-S/R108-C0 discretization branch have
now been exercised without earning promotion: R200-S remains grid-sensitive,
R108-S failed its frozen P1 refinement gates, and R108-C0 terminated
`INVALID_OR_INCOMPLETE` before a P2 comparison could be evaluated.  The
analytic-v3 upgrade is now frozen.  For this candidate, that next
theorem-engineering target has now been obtained in the post-freeze Route A4
package: A4.8 proves whole-shell short-period uniqueness near the bottom and
A4.9 gives an eigenvalue-only fixed-energy relative wave-trace term.  These
results are not yet incorporated into either immutable manuscript PDF.  The
CRR positive-time phase has since been fixed to \(+i\), and the separate
R401-SC decreasing-\(\hbar\) audit has passed down to
\(\hbar=4\times10^{-5}\).  Its finest absolute complex error is
\(1.48\%\), its phase error is \(0.0132135\) rad, and its separation from
the identically windowed harmonic oracle is \(0.21\%\).  The 58-check
independent recomputation and all 74 current repository regression tests
pass.  In parallel, breadth-first generation
of fixed multiscale or endogenous symbolic-roof candidates may continue.  A
zero comparison remains unauthorized until an endogenous prime-power carrier
passes an independent P-gate audit.

## Post-manuscript Route A4 advance

The next theorem-engineering step has now produced a separate, non-manuscript
research package under `research/route_a_wave_trace/`.  At \(a=1.02\), the
unique well-bottom Hessian yields an exact fast normal-mode period

\[
 T_+^0=0.6638439766792985
\]

and nonzero limiting stability determinant

\[
 D_+^0=3.8627220445155035.
\]

The first nonlinear period slope is explicitly derived, and R400 certified
period, action, and monodromy over six near-bottom energies with an
independent no-package checker.  A4.8 then proves whole-shell uniqueness
through time \(0.75\), and A4.9 invokes the finite-time CRR formula with
observable symbol \(A_{\rm obs}\equiv1\), producing the eigenvalue-only
fixed-energy relative Gutzwiller term

\[
 i\,\widehat g(T)\frac{T}{2\pi\sqrt D}e^{iS/\hbar}.
\]

A4.10 fixes its positive-time phase and the project-normalized coefficient.
R401-SC then recovered that complex coefficient at its finest cell:

\[
 \rho_{\rm rel}/\rho_{\rm pred}
 =1.0065230645+0.0133004473i.
\]

This post-manuscript result does not modify the frozen analytic-v3 PDF.  Its
selected \(\delta=0.01\) is not yet certified against the full theorem
threshold, although A4.11a now proves the radial component
\(\bar\delta(0.75)\ge0.010201\).  The quantitative complement/global and
independent determinant-identity thresholds remain open; A4.11b nevertheless
removes the complete warped
short-time range \(T\le0.60\) analytically, leaving the prospective
R401-VAL cover on \([0.60,0.75]\).  Its initial 128/256-bit Arb
analytic/shell smoke and 15-check independent checker pass.  The original
R401-VAL-L0 endpoint certificate was subsequently invalidated because its
first Krawczyk Jacobian row used the midpoint energy gradient and failed to
enclose the exact derivative over the root box.

The corrected R401-VAL-L1-V2 production now certifies 51 primary slabs and
50 guarded bridge hulls at both 128 and 256 MPFR bits, with all 202/202 jobs
passing.  An independent checker replays all 202 Krawczyk certificates using
exact rational decimal endpoints and passes 3973 aggregate checks.  The
primary slabs cover \(\epsilon\in[0,0.101]\): the analytic fast orbit anchors
the endpoint, the guarded bridges identify one connected branch, exact energy
conservation plus a minimum positive phase slope of \(8.95504\) recover the
full \(Q_+\) return, and the existing short-period exclusion makes the branch
primitive.  The 128/256-bit minimum margins are
\(9.323437\times10^{-6}\)/\(9.328825\times10^{-6}\), and the corresponding
maximum contraction bounds are \(0.0339894\)/\(0.0290133\).  This is
uniqueness only inside the frozen local boxes and bridge hulls.  The root
complement, global cover, \(\delta_{\rm tr}\), and P0 remain open; the result
does not pass the high-energy prime-power P gate.

The companion A4.13/R401-VAL-L1-MG-V2 release now proves a uniform local
transverse gap on that branch.  The positive phase-slope gate supplies
regularity and event transversality, and the invariant quotient
\(\ker(dK)/\operatorname{span}(X_K)\) gives the exact identity

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3.
\]

Its no-analyzer-import checker passes 202 determinant and 202 phase-slope
replays, all 815 directed-decimal payloads, and 8302 aggregate checks.  The
rigorous 128/256-bit minimum lower endpoints are
`3.835992606647717183`/`3.850741968945794693`.  This local result retains
`final_status: null`: an independent event-projected \(D\Pi\), the frozen
Taylor-model identity residual, root complement, phase/global cover,
\(\delta_{\rm tr}\), and P0 remain open.  Like the other Route A4 advances,
it is not yet incorporated into either immutable manuscript PDF.
