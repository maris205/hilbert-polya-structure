# P96 — Finite-subset circle expansion

Status: **internal Stage 2 final QA PASS / external HOLD**.

For integers `d >= 2` and `k >= 1`, this note studies the map induced by
`x -> d*x mod 1` on the compact space of nonempty circle subsets with at most
`k` points.  The system is a `k`-dimensional, cardinality-collapsing
configuration-space quotient; it is not an SFT, cellular automaton, tree
shift, substitution system, or linear group shift.

The frozen theorem package is:

1. a finite invariant set is uniquely a disjoint union of complete periodic
   orbits of the base circle map;
2. for `Q=d^n`, the exact-cardinality fixed counts have binary Euler series
   `prod_l (1+u^l)^O_l(Q) = (1-Q*u^2)/((1-Q*u)(1+u))` and
   `E_j(Q)=(Q-1)(Q^j-(-1)^j)/(Q+1)`;
3. total fixed counts split by parity of `k`, producing a complete
   alternating linear-factor formula for the Artin–Mazur zeta function;
4. Möbius inversion gives every least-temporal-period orbit count and the
   prime-orbit estimate `d^(k*m)/m + O(d^((k-1)*m)/m)`;
5. as a standard Bowen-factor control, the uniformly finite-to-one cover
   `(S^1)^k -> exp_k(S^1)` gives exact entropy `k*log(d)`; and
6. the two outermost zeta factors recover `(d,k)`, yielding parameter rigidity
   inside the family.

The paper explicitly separates its unsigned Artin–Mazur ledger from
Tuffley’s topological/degree results, general qualitative hyperspace
dynamics, rotational-subset enumeration, and fixed-index/Lefschetz symmetric
power formulas.  A multiplicity-preserving `SP^k(S^1)` computation is included
as a control, not as a novelty claim.

Run the exact control with:

```bash
python3 code/verify_finite_subset_circle.py
```

Build the manuscript with the four-stage command in [BUILD.md](BUILD.md).
The frozen eight-page PDF, final mechanical checks, and package hashes are
recorded in [FINAL_QA.md](FINAL_QA.md) and [SHA256SUMS](SHA256SUMS).  No
public release, submission, or absolute priority claim is authorized.
