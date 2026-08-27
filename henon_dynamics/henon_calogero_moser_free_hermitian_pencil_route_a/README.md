# HCS-C196: free rational Calogero--Moser Hermitian-pencil route

This release treats one complete all-parameter dynamical system, not a slice
of a later paper.  For every `N>=2`, `g>0`, strictly ordered real initial
positions, and real momenta, it closes the repulsive rational
Calogero--Moser flow through the Hermitian pencil

\[
X(t)=Q_0+tL_0,\qquad
(L_0)_{jk}=p_j\delta_{jk}+\frac{ig(1-\delta_{jk})}{q_j-q_k}.
\]

Its ordered eigenvalues are the physical particle positions for all real
time.  The package proves all-time simple spectrum, no collisions, global
completeness, every trace integral, both scattering ends, incoming/outgoing
rank reversal, preservation of each spectral-line intercept, a global inverse
scattering atlas, and absence of bounded nonconstant periodic motion.

## Exact theorem increment

The commutator

\[
[Q_0,L_0]=ig(J-I)
\]

has the decisive rank-one form.  Compressing it to a repeated eigenspace of
`Q_0+tL_0` or `L_0` is impossible.  If
`lambda_1<...<lambda_N` are the eigenvalues of `L_0`, normalized eigenvectors
are gauged by `e^*v_a=1`, and `a_a=v_a^*Q_0v_a`, then

\[
x_j(t)=t\lambda_j+a_j+O(t^{-1})\quad(t\to+\infty),
\]

\[
x_j(t)=t\lambda_{N+1-j}+a_{N+1-j}+O(|t|^{-1})
\quad(t\to-\infty).
\]

Conversely, ordered `lambda` and arbitrary real `a` reconstruct the Hermitian
matrix

\[
\widetilde Q_{aa}=a_a,\qquad
\widetilde Q_{ab}=\frac{ig}{\lambda_b-\lambda_a},
\]

and hence a unique ordered Calogero--Moser phase point.

## Reproduce

Run from the repository root:

```bash
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_calogero_moser_producer.py
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_calogero_moser_checker.py
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_sympy_crosscheck.py
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_replay.py
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_mutation.py
python henon_dynamics/henon_calogero_moser_free_hermitian_pencil_route_a/code/c196_release_manifest.py
```

The finite regression contains 18 deterministic rational systems,
`N=2,...,7`, three positive couplings, and 126 pencil-time rows.  It records
417 exact Hermitian checks, 417 exact commutator checks, and 99 exact
trace/energy checks.  The independent checker passes 2,210 assertions using
realified Jacobi spectra, polynomial projectors, and centered differences;
the separate SymPy path passes 1,200 checks; replay is byte exact; and the
hostile suite rejects 135 repaired-hash mutations plus one stale-hash attack.

## Ownership, boundary, and verdict

Calogero 1969 and Moser 1975 retain ownership of the classical model and
isospectral/scattering solution.  The package contribution is a convention-
locked, proof-complete synthesis with executable regression, not a priority
claim.  The finite `N<=7` oracle does not prove the all-`N` theorem.

The main theorem excludes `g=0`, coincident positions, `N=1`, and confining,
trigonometric, hyperbolic, elliptic, spin, complex, and quantum spectral
variants.  It does not manufacture a periodic-orbit zeta for an unbounded
continuous scattering flow.

Route tuple:
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_REJECTED`; Route B is false.  Scope literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
