# HCS-C126 — Chebyshev contracting skew product

This package proves an all-period orbit and stability theorem for

\[
F(x,y)=(T_3(x),y/4+x)=(4x^3-3x,y/4+x).
\]

For every \(n\ge1\), the base iterate is \(T_{3^n}\), its fixed polynomial
has exactly \(3^n\) distinct real roots, and every root has one unique closing
fiber coordinate.  Hence

\[
\#\operatorname{Fix}(F^n)=3^n,
\quad
P_n=\frac1n\sum_{d\mid n}\mu(d)3^{n/d},
\quad
\zeta_F(z)=\frac1{1-3z}.
\]

The package also classifies all fixed-point multipliers, positive and negative
unstable orientations, stability determinants, and primitive repetitions.
Changing the fiber multiplier to one destroys isolated fiber closure; changing
the base to \(4x^3-2x\) creates triple roots and a neutral two-cycle at period
two.

## Progress over the prior gate

This is not another finite period table.  The theorem has no orbit cutoff and
puts a complete nontrivial real fixed atlas, primitive/repeated bookkeeping, an
orbit-owned zeta, and all-period stability laws in one source dynamics.  It
therefore advances beyond earlier low-period witnesses and beyond the
trace-class contraction whose base had only one periodic point.

It does not yet supply a weighted global nuclear transfer operator, target
divisor comparison, analytic completion, or natural lift.

## Reproduce

```text
python3 code/c126_chebyshev_skew_producer.py
python3 code/c126_chebyshev_skew_checker.py
python3 code/c126_sympy_crosscheck.py
python3 code/c126_replay.py
python3 code/c126_mutation.py
python3 code/c126_release_manifest.py
```

The complete proof is in [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md), the exact
receipt is in
[results/c126_chebyshev_skew_evidence.json](results/c126_chebyshev_skew_evidence.json),
and the compiled paper is [paper/main.pdf](paper/main.pdf).

## Strict evaluation

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
route_b_invocation_allowed = false
```

The evaluation uses only labels admitted by `skills/route-a-evaluator.md`.
The source Artin–Mazur zeta is not promoted to a target-facing weighted
Fredholm determinant.  The scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic/local data, Euler factors, root
numbers, automorphy, Hilbert–Pólya operator, Riemann-zero result, or Route-B
authorization is claimed.  External novelty and literature standing were not
assessed.
