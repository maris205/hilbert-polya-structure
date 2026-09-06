# Finite exact checks, 2026-09-06

Command (repository root):

```text
python3 henon_dynamics/continuation_c404_c408_round2/arithmetic_forms/exact_checks.py
```

Final execution used Python 3.12.3 and exited 0. It evaluated real rational
vectors in the coordinates `x(m)=b(m)*sqrt(m)`, with
`b={1:1, 2:-1, 3:1/2, 6:1/3}`. This eliminates floating-point error in the
critical GCD form. It is not a finite substitute for the infinite proof.

For prime tails `{5,7,11}` and `{5,7,11,13,17,19}`, all three exact identities
in proof equation (2) and its preceding display held. The respective tail
sums were `167/385` and `1005768/1616615`; the form residuals were
`148819/27889` and `2593654958521/674379513216`. The first residual need not
be small: this test checks the identity, not an observed asymptotic regime.

The deliberate invalid tail `{2,3,5}`, which overlaps primes in the support,
violates both the asserted disjoint-support Hilbert-norm identity and the
mixed-form identity. For `N=12,31,100`, direct rowwise Gram evaluation agreed
exactly with the separate pairwise harmonic-number/GCD formula. Their values
were respectively:

```text
374167/172042
1321717003419479/581548514594714
1721085726856021822903933653118020525696637/723331813976017558011075902155206572385550
```

An earlier execution exited 1 in the intended invalid-hypothesis control:
the first chosen support `{1,2,6}` and tail `{2,5,7}` still had disjoint
shifted supports, so the norm identity did not fail. This was a defective
negative-control choice, not a counterexample to the theorem. The final
support includes both 2 and 3 and the invalid tail includes both primes,
creating an actual collision at index 6. No failed run is reported as PASS.

The code does not evaluate resolvents, certify slow-variation limits, or
numerically establish pure singularity. Those conclusions depend on the
complete mathematical proof and its substantive non-author review.
