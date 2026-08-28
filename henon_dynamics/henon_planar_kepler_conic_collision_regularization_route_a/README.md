# HCS-C216 — Planar Kepler conics, collision boundary, and Levi–Civita regularization

This package is a self-contained Route-A certificate for the planar Coulomb/Kepler Hamiltonian

\[
 H(q,p)=\frac{|p|^2}{2}-\frac{\mu}{|q|},\qquad \mu>0,
\]

on \((\mathbb R^2\setminus\{0\})\times\mathbb R^2\).  It takes one theorem-scale step: all three conic energy signs, the exact negative-energy period and radial action, hyperbolic scattering, the finite-time radial collision boundary, and the fixed-energy Levi–Civita configuration regularization are locked to one convention and checked independently.

The finite receipt is deliberately a regression ledger, not a numerical substitute for the quantified theorem.  It contains 10 exact orbit probes, 4 radial collision probes, 12 Levi–Civita probes (including 3 collision points), and 5 fixed-set/strobe probes.  All rational identities are exact; displayed quadratures use 68 significant decimal digits.

The package is source-attributed to Levi–Civita (1920), Moser (1970), and Ligon–Schaaf (1976).  It does not claim priority or reproduce a global Ligon–Schaaf symplectomorphism.  The collision statement is only a smooth continuation of the configuration variable in the regularized \(\tau\)-equation.

The strict evaluator result is

\[
 (A0,A1,A2,A3,A4)=(\texttt{A0\_FAIL},\texttt{A1\_WEAK},
 \texttt{A2\_FAIL},\texttt{A3\_FAIL},
 \texttt{A4\_NATURAL\_QUANTIZATION}),
\]

with `ROUTE_A_REJECTED` and Route B disabled.  No prime/zero table, arithmetic local datum, Euler factor, root number, automorphy assertion, target functional equation, or Hilbert–Pólya operator is present.

## Reproduce

From this directory:

```text
python3 code/c216_kepler_producer.py
python3 code/c216_kepler_checker.py
python3 code/c216_kepler_sympy_crosscheck.py
python3 code/c216_kepler_replay.py
python3 code/c216_kepler_mutation.py
python3 code/c216_release_manifest.py
```

The release manifest is content-addressed and excludes itself plus LaTeX sidecars and Python bytecode.  The fixed build epoch used for the three manuscript revisions is recorded in `paper/COMPILE_REPORT.md`.
