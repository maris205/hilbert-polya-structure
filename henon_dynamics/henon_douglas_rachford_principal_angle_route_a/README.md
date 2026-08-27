# HCS-C197 — relaxed Douglas--Rachford principal-angle dynamics

C197 treats the relaxed Douglas--Rachford update for **every pair of linear
subspaces in finite-dimensional real Hilbert space and every real relaxation
parameter**.  The principal-angle decomposition gives the entire dynamics:
fixed spaces, mismatch signs, generic rotation-contraction blocks, the sharp
convergence interval and rate, the optimal relaxation, trace/determinant
factors, shadow convergence, and the orthogonal endpoint at `lambda=2`.

This is one complete algorithmic-dynamics paper, not a numerical study of a
single feasibility instance.  The finite rational-angle ledger is an exact
regression certificate for signs and conventions; the all-subspace statement
is proved in `THEOREM_PACKAGE.md` and the paper.

## Strict result

The same principal-angle theorem also closes the Route-A question.  The source
has no intrinsic rational-prime carrier or logarithmic clock.  Its endpoint
reflection product is a natural same-clock orthogonal map, but that is only an
A4 formal hint and cannot repair A0--A3:

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

Route B remains false under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python code/c197_douglas_rachford_producer.py
python code/c197_douglas_rachford_checker.py
python code/c197_douglas_rachford_sympy_crosscheck.py
python code/c197_douglas_rachford_replay.py
python code/c197_douglas_rachford_mutation.py
python code/c197_release_manifest.py
```

The final paper is `paper/main.pdf`.  Three content-distinct revision PDFs and
the fixed-epoch double-build audit are release payloads.
