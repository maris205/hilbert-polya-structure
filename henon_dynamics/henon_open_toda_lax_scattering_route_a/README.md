# HCS-C230 — finite open Toda Lax flow and scattering

This package takes a large Route-A dynamics step into a finite open Hamiltonian
lattice.  For
\[
H=\frac12\sum p_j^2+\sum_{j=1}^{N-1}e^{q_j-q_{j+1}},
\]
the Flaschka variables \(a_j=\frac12e^{(q_j-q_{j+1})/2}\) and
\(b_j=-p_j/2\) form a Jacobi matrix with
\(\dot L=[B,L]\).  The theorem package closes global existence and positive
edges, all trace/Hamiltonian invariants, simple spectrum, Moser sorting
scattering, and the exact norming-weight softmax law.  The \(N=2\) flow is
given in closed sech/tanh form.  A singular \(a_j=0\) block boundary exposes
the repeated-root case \(x^2(x-1)\).

Run from this directory:

\`\`\`text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_release_manifest.py
\`\`\`

The strict tuple is
\`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)\`
with \`ROUTE_A_REJECTED\`; Route B remains disabled.  The positive result is
source-local Hamiltonian/Lax/scattering integrability, not arithmetic spectral
data.  The physical positive isospectral leaf is a noncompact scattering
chamber; torus angles are mentioned only for a phase-compactified extension.

Scope: \`NO_BAD_EULER_OR_ROOT_NUMBER\`.

