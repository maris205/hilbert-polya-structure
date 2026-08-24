# C125 — exact Anosov orbit zeta and Koopman obstruction

This package freezes the toral automorphism

\[
T_A([x])=[Ax],\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

It proves for every \(n\ge1\) that

\[
\#\operatorname{Fix}(T_A^n)=|\det(A^n-I)|,
\]

performs exact Möbius inversion, and obtains

\[
\zeta_T(z)=\frac{(1-z)^2}{1-3z+z^2}.
\]

The natural Koopman action on \(L^2(\mathbb T^2)\) is unitary, but its
Fourier-basis action is an infinite permutation.  An explicit orthonormal
sequence proves it is noncompact, hence not Schatten or trace class.  The
orbit zeta is therefore not promoted to an ordinary Koopman Fredholm
determinant.

## Reproduce

```bash
python code/c125_anosov_producer.py
python code/c125_anosov_checker.py
python code/c125_sympy_crosscheck.py
python code/c125_replay.py
python code/c125_mutation.py
(cd paper && SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
python code/c125_release_manifest.py
```

The checker imports no producer code.  All arithmetic is exact; no tolerance,
random seed, fitted parameter, prime table, or target-zero table is used.

## Progress over prior gate

- relative to C121, the package upgrades an all-order degree law plus one
  two-cycle to a complete all-order fixed/primitive orbit census and exact
  orbit zeta;
- relative to C119, it puts rich recurrent dynamics and a natural global
  Hilbert action in one model, then proves the natural action is not
  determinant class.

## Route-A status

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall = ROUTE_A_EXPLORATORY
route_b_invocation_allowed = false
```

The complete intrinsic orbit census has no prime-like target correspondence,
so A1 remains weak.  The exact internal zeta has no target-divisor comparison
and the Koopman unitary is not determinant class, so strict A2 fails.  Target
analytic structure is absent, and the natural unitary supplies only an A4
formal hint.

The paper is [paper/main.pdf](paper/main.pdf), canonical evidence is
[results/c125_anosov_evidence.json](results/c125_anosov_evidence.json), the
package evaluation is [route_a_evaluation.yaml](route_a_evaluation.yaml), and
the release ledger is [C125_RELEASE_MANIFEST.json](C125_RELEASE_MANIFEST.json).
Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
