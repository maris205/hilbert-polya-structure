# HCS-C249 — Van der Pol/Liénard limit-cycle certificate (Route A)

This package freezes the smooth polynomial oscillator
\[
 \dot x=y,\qquad \dot y=\mu(1-x^2)y-x,
 \qquad\text{equivalently}\qquad
 \ddot x+\mu(x^2-1)\dot x+x=0 .
\]
The theorem-scale advance is a complete sign and boundary atlas: for
\(\mu>0\), the classical Liénard hypotheses give exactly one hyperbolic
attracting cycle surrounding the origin; \(\mu<0\) is its time reversal and
has one repelling cycle; and \(\mu=0\) is a center with a continuum of
harmonic ovals.  The receipt also records the energy balance, divergence
formula, Poincaré fixed section, and transverse Floquet multiplier.

Five positive-parameter return-map rows are finite regression probes, not a
numerical replacement for the all-parameter theorem.  The producer,
independent checker, SymPy reconstruction, clean-process replay, and hostile
mutation suite are all source-local and deterministic.  No period formula is
claimed in elementary closed form for every \(\mu\).

The package is deliberately distinct from the Lorenz flow (C227), the
Hamiltonian Duffing separatrix (C232), the harmonic strobe (C178), stochastic
Kramers dynamics (C237), and hybrid integrate-and-fire dynamics (C245): those
models do not provide this smooth Liénard uniqueness/Floquet boundary.

Locked metadata: source baseline
3ff451e904f8f063e88c40ef87f4697a6586b1a5, evaluator authority SHA
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c, fixed
epoch 1788048000, scope `NO_BAD_EULER_OR_ROOT_NUMBER`, date 2026-08-30.
The Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the overall
verdict is `ROUTE_A_REJECTED`; Route B is disabled.

Run from this directory:

    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_vdp_producer.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_vdp_checker.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_vdp_sympy_crosscheck.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_vdp_replay.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_vdp_mutation.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c249_release_manifest.py
