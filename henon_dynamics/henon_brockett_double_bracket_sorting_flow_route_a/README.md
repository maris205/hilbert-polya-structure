# HCS-C185 — Brockett double-bracket sorting flow

This package closes the real symmetric simple-spectrum Brockett family

\[
\dot H=[H,[H,N]],\qquad N=\operatorname{diag}(\nu_1<\cdots<\nu_n),
\]

for every `n>=2`.  It proves global existence on the compact orthogonal orbit,
isospectrality, the exact strict Lyapunov identity, all `n!` permutation
equilibria, the complete pair-mode linearization, the Morse/inversion index,
generic sorting convergence, and the absence of nonconstant recurrent or
periodic trajectories.  Repeated source or target spectra are recorded only as
a separate degenerate boundary; target repetition supplies the genuine
Morse--Bott component.

The double-bracket equation, its gradient interpretation, and its sorting and
diagonalization role are classical results of Brockett.  This package claims no
priority for them.  Its contribution is a content-addressed all-size proof and
validation ledger plus a strict Route-A evaluation.

The final tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`;

overall `ROUTE_A_REJECTED`, Route B false, under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduction

Run from this directory:

```bash
python code/c185_brockett_producer.py
python code/c185_brockett_checker.py
python code/c185_sympy_crosscheck.py
python code/c185_replay.py
python code/c185_mutation.py
python code/c185_release_manifest.py
```

The paper is `paper/main.pdf`; the exact evidence is
`results/c185_brockett_evidence.json`.  Finite regression through `n=7` is not
the proof of the all-size theorem; the proof is in `THEOREM_PACKAGE.md` and
`paper/main.tex`.

## Scope

No target zero or prime table, arithmetic local datum, Euler factor, root
number, automorphy claim, target divisor, Weil compression, Hilbert--Polya
operator, or Route-B input is used.  Internal drafting and hostile checks are
not external peer review or independent error processes.
