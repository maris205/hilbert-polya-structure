# Exact control results — P96

Command:

```text
python3 code/verify_finite_subset_circle.py
```

Result on 2026-08-28 UTC:

```text
finite-subset circle exact control: PASS
assertions=7000
literal_subsets=189245
cycle Q=2 k=5 L=3255 orbits={1: 1, 2: 1, 3: 2, 4: 3, 5: 6} exact=[1, 1, 3, 5, 11] total=21
cycle Q=3 k=4 L=1040 orbits={1: 2, 2: 3, 3: 8, 4: 18} exact=[2, 4, 14, 40] total=60
cycle Q=4 k=4 L=5355 orbits={1: 3, 2: 6, 3: 20, 4: 60} exact=[3, 9, 39, 153] total=204
cycle Q=5 k=3 L=744 orbits={1: 4, 2: 10, 3: 40} exact=[4, 16, 84] total=104
cycle Q=8 k=3 L=4599 orbits={1: 7, 2: 28, 3: 168} exact=[7, 49, 399] total=455
subset Q=2 k=3 L=21 exact=[1, 1, 3] total=5
subset Q=3 k=3 L=104 exact=[2, 4, 14] total=20
subset Q=4 k=2 L=15 exact=[3, 9] total=12
temporal d=2 k=3 P_1..P_8=[5, 23, 150, 951, 6354, 42935, 297270, 2088510]
```

The 7,000 registered assertions cover:

- base-orbit Möbius divisibility and nonnegativity;
- binary Euler coefficients and the exact-cardinality formula for
  `2 <= Q <= 8`, through degree 9;
- all parity-split partial sums and their alternating-polynomial form;
- formal Artin--Mazur factor signs, logarithmic coefficients, and outer
  pole/zero parameter recovery for `2 <= d <= 7`, `1 <= k <= 9`, and
  iterates through 15;
- the multiplicity-preserving symmetric-power control;
- five literal rational-circle cycle decompositions, including exact cycle
  lengths and 0/1 cycle-selection counts;
- direct image-equality tests on 189,245 individually enumerated subsets;
  and
- induced temporal Möbius divisibility, nonnegativity, and reconstruction for
  `2 <= d <= 5`, `1 <= k <= 7`, through period 12.

All evidence-bearing arithmetic is integer arithmetic.  No floating-point
comparison, random seed, optimization solver, or symbolic simplifier enters
an assertion.
