# HCS-C193: Markoff--Vieta descent tree

C193 freezes the normalized positive integer solutions of

\[
x^2+y^2+z^2=3xyz,\qquad x\le y\le z,
\]

and turns largest-coordinate Vieta descent into a complete dynamical theorem.
Every non-root triple has a unique strictly smaller parent, every path
terminates at `(1,1,1)`, reversing the edges generates all positive solutions,
and the permutation quotient is a rooted tree.  This is one all-solution
classification, not five low-height examples.

The Diophantine phase space earns the round's only
`A0_WEAK_ARITHMETIC_RELATION`, but it has no rational-prime primitive carrier,
prime-power repetition or `log p` clock.  Strict descent also destroys every
non-root periodic orbit.  The final verdict is

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

The Frobenius uniqueness conjecture for Markoff numbers and every mod-prime
Markoff graph are explicitly outside scope.  See `THEOREM_PACKAGE.md`,
`SOURCE_AUDIT.md`, `results/TEST_REPORT.md`, and `paper/main.pdf`.

Run from the repository root:

```bash
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_markoff_producer.py
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_markoff_checker.py
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_sympy_crosscheck.py
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_replay.py
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_mutation.py
python3 henon_dynamics/henon_markoff_vieta_descent_tree_route_a/code/c193_release_manifest.py
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route B is false.
