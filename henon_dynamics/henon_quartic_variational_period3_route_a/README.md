# C120 — Quartic variational primitive period-three certificate

C120 freezes the exact area-preserving map

\[
F(q,p)=(q^3-2q-p,q),\qquad V(q)=q^4/4-q^2,
\]

with type-1 generating function `S(q,Q)=qQ-V(q)` under the convention
`p=-partial_q S`, `P=partial_Q S`. The map has determinant one, inverse
`F^{-1}(Q,P)=(P,P^3-2P-Q)`, and reversor `R(q,p)=(p,q)`.

The exact primitive cycle

```text
(0,-1) -> (1,0) -> (-1,1) -> (0,-1)
```

has chronological monodromy `B(-1)B(1)B(0)=[[-1,0],[-3,-1]]`. Its cyclic
action is `1/2`; the action Hessian has determinant `4`, characteristic
polynomial `(lambda+2)(lambda^2-2lambda-2)`, and Morse index two. Nearby-
parameter, deleted-cubic, and noncyclic-word controls all reject the frozen
cycle.

This is one exact low-period structural witness. Under the repository's
canonical Route-A evaluator its tuple is
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, with overall status
`ROUTE_A_EXPLORATORY`. There is no target prime correspondence or log-prime
clock, no source-owned dynamical zeta/Fredholm object, and no target divisor.
No complete orbit atlas, global analytic match, arithmetic, Euler-factor,
root-number, automorphy, Hilbert–Pólya, or Route-B claim is made. The literal
firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python3 code/c120_variational_period3_producer.py
python3 code/c120_variational_period3_checker.py
python3 code/c120_sympy_crosscheck.py
python3 code/c120_replay.py
python3 code/c120_mutation.py
python3 code/c120_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf).
