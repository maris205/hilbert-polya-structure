# C104 — Polynomial Hénon with a Three-Branch Route-A Pilot

This package is a conservative candidate-system paper for Route A. The
geometric candidate is the area-preserving polynomial Hénon map

\[
 H_a(x,y)=(x^3-3x+a-y,x),\qquad a=1/7.
\]

The cubic has three monotonicity intervals, so its natural next experiment is
a three-branch coding. **This package does not assert that the candidate has a
complete Markov partition.** Instead it freezes the full one-sided
three-letter branch-word pilot and representative Jacobian samples
\(\xi=(-2,0,3)\), giving branch matrices
\(B_j=\begin{psmallmatrix}P'(\xi_j)&-1\\1&0\end{psmallmatrix}\).

The exact certificate contains:

* all 196 primitive necklaces of lengths 1–6 (counts 3, 3, 8, 18, 48, 116);
* their branch-count vectors and integer representative monodromies;
* the exact \(6\times6\) matrix-valued finite transfer prefix;
* \(\operatorname{Tr}(A^n)\) for \(1\le n\le6\), its primitive trace decomposition,
  and \(\det(I-zA)\) coefficients;
* independent checker, SymPy/Newton cross-check, canonical replay, and nine
  hostile semantic mutations.

The transfer determinant is explicitly a finite-dimensional **screening
object**, not a Fredholm determinant for the polynomial map. The route status
is therefore

```text
A1 = A1_OPEN (qualification: SYMBOLIC_PILOT_ONLY)
A2 = A2_CERTIFIED_PREFIX (qualification: DISCRETE_TRANSFER_PREFIX_ONLY)
A3 = A3_NOT_ADDRESSED
A4 = A4_FAIL
```

No arithmetic/local data, Euler factors, root numbers, automorphy, actual
Hénon periodic-orbit completeness, Hilbert–Pólya operator, or Route-B claim is
made. The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From this directory:

```bash
python3 code/c104_multibranch_producer.py
python3 code/c104_multibranch_checker.py
python3 code/c104_sympy_crosscheck.py
python3 code/c104_replay_checker.py
python3 code/c104_mutation_test.py
```

The first command writes the canonical evidence file under `results/`; all
following commands must pass before the paper is treated as a complete pilot.
The release ledger is generated with:

```bash
python3 code/c104_release_manifest.py
```

The short paper is `paper/main.tex` and the compiled artifact is
`paper/main.pdf`.
