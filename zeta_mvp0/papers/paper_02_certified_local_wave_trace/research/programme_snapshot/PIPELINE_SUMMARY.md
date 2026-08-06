# Paper-7 Pipeline Summary

## Outcome

The research-refinement and experiment-planning stages produced an explicit,
claim-bounded Paper-7 project:

> a clock-preserving Hénon-warped exponential Schrödinger family with a
> fixed magnetic symmetry deformation.

The mathematical backbone and completed experiments support a full manuscript
draft. The project is framed as a Hilbert--Pólya-motivated testbed for
separating a prescribed mean count from geometric and antiunitary-symmetry
diagnostics, not as a zeta-zero construction.

## Core outputs

- RH_DISCOVERY_PROTOCOL.md: breadth-first RH search and Route A/B policy.
- RH_CANDIDATE_PORTFOLIO.md: ranked post-Paper-7 candidate queue.
- PAPER7_FOUNDATION.md and PAPER_PLAN.md: thesis and manuscript plan.
- DERIVATION_PACKAGE.md, PROOF_PACKAGE.md, and MAGNETIC_EXTENSION.md:
  analytic Q/W backbone.
- P_GATE_RELATIVE_SPECTRAL_SHIFT_AUDIT.md: pre-P C-admissibility audit and
  first-resolvent/prime-time boundary; it is not a P pass.
- EXPERIMENT_PLAN.md and EXPERIMENT_TRACKER.md: claim-driven run chain.
- results/: complete success, failure, and remediation reports.
- paper/: LaTeX manuscript, figures, bibliography, and compiled PDF.
- paper_analytic_v3/: separately versioned analytic theorem upgrade, full
  proofs, two-round reviews, and final PDF.

The frozen round-2 PDF is `paper/paper7_round2_final.pdf` (35 pages,
SHA-256
`8ad75ae285244bef380d6474b7e1a4ecb943b6fe96d03fa99c9efd44192a3339`).
Its baseline regression was 13 tests, seven regenerated figures, no undefined
references/citations, no overfull box, and 59 printed references.

The current analytic-v3 PDF is
`paper_analytic_v3/paper7_analytic_v3_round2_final.pdf` (45 pages, SHA-256
`e961e1b65963b2b769d7454e27913bbfa57c60d9e46849b4c8f5834a900ab0ff`).
Its final regression is 58 tests, eight regenerated figures, 77 database
entries/67 printed references, no undefined reference/citation, no overfull
box, and all fonts embedded.  The old Round-2 artifact remains unchanged.

## Current bottom line

\[
\boxed{\text{Q/W and S}_{\rm op}\text{ proved; C admissible; }
P^*_{\rm loc}\text{ proved; }P^*_{\rm loc,num}\text{ passed; }
P_0\text{ open; Z unauthorized; RH not claimed.}}
\]

R200-S and the independent R108-S/R108-C0 discretization branch were later
executed but did not earn promotion. R200-S remains grid-sensitive; R108-S
failed its frozen refinement gates; and R108-C0 stopped incomplete at its
first P2 all-96 integrity gate, leaving formal C0 `NOT_EVALUATED`. For the
surviving Paper-7 candidate, A4.8--A4.10 have now supplied the
energy-localized relative wave-trace theorem with explicit
period/action/stability and absolute phase; R401-SC subsequently completed
the frozen eigenvalue-only numerical audit.  The next strict bridge is a
quantitative certification of the remaining global warped components and
the independent determinant identity of the theorem
threshold \(\delta_{\rm tr}\).  A4.11a already proves
\(\bar\delta(0.75)\ge0.010201\); \(\delta_*\) and the protocol-level
independent \(\delta_{\rm nd}\) cross-check remain, although A4.13 now proves
the local branch's strict \(D>3\) inequality.  A4.11b additionally excludes every warped
period \(T\le0.60\) by a convex-box Hessian bound, so the prospective
R401-VAL computer-assisted cover is restricted to \([0.60,0.75]\).  The
non-claiming R401-VAL-A0 Arb smoke now passes at 128/256 bits with all 60
shell identities per precision and a 15-check independent recomputation.
The original R401-VAL-L0 endpoint result has been invalidated: its first
Krawczyk Jacobian row used a midpoint energy gradient and did not enclose the
exact box derivative.  The corrected R401-VAL-L1-V2 production instead
certifies 51 primary slabs and 50 guarded bridge hulls at both 128 and 256
MPFR bits.  All 202/202 jobs pass, and an independent exact-rational checker
replays all 202 certificates with 3973 aggregate checks.  The primary slabs
cover \(\epsilon\in[0,0.101]\); the analytic fast orbit anchors the zero
endpoint, the bridge certificates identify one connected branch, exact
energy conservation plus the phase gate recover the full \(Q_+\) return, and
the short-period exclusion makes the branch primitive.  The 128/256-bit
minimum Krawczyk margins are \(9.323437\times10^{-6}\)/
\(9.328825\times10^{-6}\), the maximum contraction bounds are
\(0.0339894\)/\(0.0290133\), and the minimum phase slope is \(8.95504\).
This is local-box uniqueness only.  A4.13 and R401-VAL-L1-MG-V2 now
additionally prove on this branch that

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3.
\]

The invariant-quotient proof covers unit-multiplier Jordan blocks, and the
checker passes 202 determinant plus 202 phase-slope replays, 815
directed-decimal payloads, and 8302 aggregate checks.  Its rigorous minimum
lower endpoints are `3.835992606647717183`/`3.850741968945794693` at
128/256 bits.  Both local statuses retain `final_status: null`: the
independent event-projected \(D\Pi\), Taylor residual, root complement,
phase/global cover, \(\delta_{\rm tr}\), and P0 remain open.  This is followed
separately by the
fixed-operator high-energy problem.  A zero
comparison remains unauthorized until an endogenous prime-power carrier is
specified and independently audited.

## Route A4 addendum

The proposed energy-localized trace bridge has been reframed and advanced in
`research/route_a_wave_trace/`.  Rather than interpreting unstable R200
peaks, the new route begins at the exact bottom normal form of the one-step
\(a=1.02\) Hamiltonian.  It identifies a fast Lyapunov family with explicit
limiting period, action slope, transverse determinant, and first nonlinear
period correction, together with a time interval excluding radial returns
near the bottom.

R400 then continued this branch at six energy excesses and passed every
frozen numerical/asymptotic gate plus a separate implementation check.  The
current promotion is therefore

\[
 C\text{ proved},\qquad
 P^*_{\rm loc}\text{ proved at fixed energy},\qquad
 P^*_{\rm loc,num}\text{ passed at }\delta=0.01,\qquad
 P_0\text{ open},\qquad Z\text{ unauthorized}.
\]

Here \(P^*_{\rm loc}\) denotes a genuine eigenvalue-only local periodic-orbit
trace bridge, not a rational-prime carrier.  A4.10 fixes the positive-time
CRR phase to \(+i\), and the prospectively specified R401-SC audit was
subsequently executed and passed on eight \(\hbar\) values.  Its finest
normalized complex trace is

\[
 1.0065230645+0.0133004473i,
\]

with \(1.48\%\) error and \(0.0132135\) rad phase error against the absolute
\(T/(2\pi\sqrt D)\) coefficient, and only \(0.21\%\) separation from the
identically windowed exact harmonic baseline.  All numerical gates, the
58-check independent recomputation, and all 74 current regression tests
passed.  The result is fixed-energy
semiclassical support only: A4.11a certifies the radial part of
\(\delta_{\rm tr}\) through \(0.01\), and A4.12--A4.13 certify the local
branch and its transverse gap, but the complement/global and independent
identity thresholds remain open.  The separate high-energy
\(\hbar=1\) and prime-time problems remain open.
