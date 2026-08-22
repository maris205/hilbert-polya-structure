# C111 — Three-site variational/symplectic Hénon ring

This package is a finite, exact Route-A pilot for a three-site coupled Hénon
map. The coupling graph is the 3-cycle with rational parameters `a=7`,
`kappa=1/5`. The potential map

\[
 F(q,p)=(\nabla U(q)-p,q),\qquad
 U(q)=\sum_i(7q_i^2/2-q_i^3/3)-\frac{1}{10}\sum_{\{i,j\}}(q_i-q_j)^2
\]

is checked over `Q`. The evidence certifies two synchronous fixed points, a
genuine synchronous primitive period-two orbit, exact symplectic/reversor
identities, and the longitudinal/transverse Fourier-mode factorisation of the
period-two monodromy. The transverse Laplacian eigenvalue is `3` with
multiplicity two, so the three-site geometry is not reduced to the two-site
package C106.

## Deliverables

- `results/c111_three_site_evidence.json`: canonical exact evidence ledger.
- `code/c111_three_site_producer.py`: deterministic producer.
- `code/c111_three_site_checker.py`: independent semantic checker.
- `code/c111_sympy_crosscheck.py`: symbolic identity and polynomial check.
- `code/c111_replay.py`: canonical-byte replay check.
- `code/c111_mutation.py`: hostile mutation audit.
- `code/c111_release_manifest.py`: deterministic file-ledger generator.
- `paper/main.tex` and `paper/main.pdf`: paper output and source.

Run from this directory:

```bash
python3 code/c111_three_site_producer.py
python3 code/c111_three_site_checker.py
python3 code/c111_sympy_crosscheck.py
python3 code/c111_replay.py
python3 code/c111_mutation.py
```

The package is deliberately conservative. `A1` is only a certified low-period
witness and `A2` remains open because no analytic/Fredholm operator owner is
constructed. It makes no claim about a complete primitive-orbit atlas,
analytic continuation, Euler factors, root numbers, automorphy, or a
Hilbert–Pólya operator. The literal scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
