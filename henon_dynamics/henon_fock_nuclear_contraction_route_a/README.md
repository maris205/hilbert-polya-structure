# C119 — Nuclear bosonic-Fock owner for a linear Hénon-type contraction

C119 freezes

\[
\Phi(x,y)=(3x/4-y/4,x/2),\qquad
A=\begin{pmatrix}3/4&-1/4\\1/2&0\end{pmatrix}.
\]

The eigenvalues are `1/2,1/4`, while the squared Euclidean singular values are
`(7±3*sqrt(5))/16`, both strictly below one. On the standard bosonic Fock
space, the source-defined operator

```text
Gamma(A) = direct_sum_{m>=0} Sym^m(A)
```

is trace class. Its traces, Fredholm product, Taylor coefficients through
degree eight, and complete zero divisor are certified exactly. This is an
analytic determinant for this expressly defined Fock owner; no target-divisor
matching is claimed. The contraction has only the origin as a periodic point,
so the nontrivial orbit route fails here. Under the canonical labels in
`skills/route-a-evaluator.md`, the strict tuple is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`: the exact Fock theorem is retained as
structural evidence, but it is neither primitive-orbit-owned nor
target-divisor-validated.

The literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`. No arithmetic local
data, Euler factor, root number, automorphy, Hilbert–Pólya, or Route-B claim is
made.

## Reproduce

```bash
python3 code/c119_fock_producer.py
python3 code/c119_fock_checker.py
python3 code/c119_sympy_crosscheck.py
python3 code/c119_replay.py
python3 code/c119_mutation.py
python3 code/c119_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf).
