# C117 — Markov-switching Hénon tangent moment operators

C117 freezes two dissipative Hénon maps sharing the origin,

\[
F_0(x,y)=(x^2+x/2-y/3,x),\qquad
F_1(x,y)=(x^2-x-y/2,x),
\]

and the exact transition matrix

\[
P=\begin{pmatrix}2/3&1/3\\1/4&3/4\end{pmatrix}.
\]

The convention is explicit: after `s_n=i -> s_(n+1)=j`, the new map `F_j`
is applied.  The package constructs source-owned 4-dimensional first-moment
and 6-dimensional symmetric second-moment operators for the tangent cocycle at
the common fixed point.  It also proves that stationary averaging and taking a
symmetric square do not commute: their exact difference has rank one.

This is a finite tangent/moment certificate, not a global transfer operator for
the nonlinear random system.  It claims no complete random-orbit atlas,
Fredholm or nuclear owner, arithmetic data, Euler factors, root numbers,
automorphy, Hilbert–Pólya operator, or Route B.  The scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python3 code/c117_markov_producer.py
python3 code/c117_markov_checker.py
python3 code/c117_sympy_crosscheck.py
python3 code/c117_replay.py
python3 code/c117_mutation.py
python3 code/c117_release_manifest.py
```

The final paper is [paper/main.pdf](paper/main.pdf), the evidence receipt is
`results/c117_markov_evidence.json`, and the package ledger is
`C117_PREFREEZE_MANIFEST.json`.
