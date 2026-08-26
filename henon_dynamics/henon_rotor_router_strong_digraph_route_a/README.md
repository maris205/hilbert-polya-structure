# HCS-C181 — strong-digraph rotor-router orbit theorem

This package gives one complete classification for the rotor-router permutation on recurrent unicycle states of every finite nonempty strongly connected directed multigraph with distinguished arcs and a cyclic order at each vertex.

For directed in-arborescence counts \(t_v\), it source-locks Pham's Theorem 1, under which \(M=\gcd_vt_v\) is the number of recurrent orbits and

\[
L=\frac1M\sum_v d_v^+t_v
\]

is their common exact length. It then combines that exact length with flow balance and the directed matrix-tree kernel to derive that every orbit visits \(v\) exactly \(d_v^+t_v/M\) times and traverses each distinguished outgoing arc at \(v\) exactly \(t_v/M\) times. It also derives the complete fixed-count, zeta, determinant, spectrum, and Eulerian specialization.

This is rotor-router dynamics on unicycles. It is not formulated as a sandpile translation: the frozen system has no sink, stabilization, recurrent sandpile torsor, or critical-group action. The deleted-basepoint chip-addition quotient in Pham's proof is cited only as the exact-return mechanism.

Run from the repository root:

```bash
python3 henon_dynamics/henon_rotor_router_strong_digraph_route_a/code/c181_rotor_router_producer.py
python3 henon_dynamics/henon_rotor_router_strong_digraph_route_a/code/c181_rotor_router_checker.py
python3 henon_dynamics/henon_rotor_router_strong_digraph_route_a/code/c181_sympy_crosscheck.py
python3 henon_dynamics/henon_rotor_router_strong_digraph_route_a/code/c181_replay.py
python3 henon_dynamics/henon_rotor_router_strong_digraph_route_a/code/c181_mutation.py
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`. Route B is false.
