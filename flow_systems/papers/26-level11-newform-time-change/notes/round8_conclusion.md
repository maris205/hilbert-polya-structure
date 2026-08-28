# Paper 26 Round-8 conclusion

Round 8 delivers a significant exact closure of the finite second-variation
audit.  The four Round-7 survivors are no longer a special-case analysis: the
same rational Schreier-homology classifier now covers all 138 frozen Hecke
cycle-owner instances and all 55 word/prime groups.

The decisive coordinate is `k(x,y,z)=2y+z` on the one-dimensional compact
real `+1` eigenspace.  Every normalized real period is exactly
`k(owner)/k(source)`, so each quadratic degree moment is a rational sum of
squares.  The complete instance split is 2 full complex kernels, 2 nonzero
real-projection-only kernels, 134 true nonkernels, and 0 degenerate or
unresolved cases.

This converts the Round-6 tolerance-based summary into an exact theorem.  The
primary laws `a_p` and `a_p^2` each fail 51/55 groups and survive in exactly
four `p=5` groups; the secondary `a_p^2-p` control fails 55/55.  Every one of
the 51 primary failures contains nonzero quadratic mass at a nonunit Hecke
cycle degree.  Hence those failures cannot be removed by tightening numerical
precision.  The four positives are exactly the topological/parity kernels
already identified in Round 7.

The result is deliberately finite and negative for the proposed primitive
Euler interpretation.  It completes the frozen multiset taxonomy, not the
global primitive-orbit census.  Cross-instance `Gamma_0(11)` conjugacy
deduplication, cutoff enlargement, a global dynamical determinant, analytic
continuation, and Route-A A2 root validation remain absent.

Formal status remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
```

with overall `ROUTE_A_EXPLORATORY`.  Route B was not run and remains
disallowed.  The next smallest lawful step is exact cross-instance conjugacy
canonicalization of the 138 frozen owners, followed by restating the taxonomy
on the unique-owner/multiplicity ledger.
