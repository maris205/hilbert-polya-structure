# Hostile mathematical audit

This audit was applied before the paper skeleton and repeated against the
round-two manuscript.

## Attacks and resolutions

1. **Can a primitive divisor divide \(ab\)?**  No.  Coprimality makes
   \(a^n-b^n\) nonzero modulo every prime dividing \(ab\).
2. **Is divisibility merely a return, not a first return?**  Primitive means
   absence from every earlier difference, exactly the least-order condition.
3. **Can 2 be a primitive return at \(n\geq2\)?**  No.  It either divides
   \(a-b\) at time one or divides no difference.
4. **Was Zsigmondy's theorem relabeled as new dynamics?**  No.  Its existence
   and exception clause is explicitly external and attributed; only the
   package synthesis is claimed.
5. **Are both exception forms complete?**  Yes: \((2,1,6)\), and \(n=2\)
   with \(a+b\) a power of two.
6. **Could \(p\mid n\) invalidate the lift?**  No.  Primitive return gives
   \(n=\operatorname{ord}_p(q)\mid p-1\).
7. **Does the valuation formula silently assume \(k>e\)?**  No.  The maximum
   formula retains order \(n\) for every \(k\leq e\).
8. **Could different points on one fiber have different periods?**  No.
   Translation returns \(x\) iff its multiplier is the identity, independent
   of \(x\).
9. **Is the finite determinant ordinary and legal?**  Yes.  It is the
   determinant of a finite permutation matrix, not a regularized infinite
   determinant.
10. **Is inversion really a reversor for composite \(N\)?**  Yes.  The unit
    group is abelian and \((qx^{-1})^{-1}=xq^{-1}\).
11. **Does the disjoint union have infinitely many fixed points at fixed
    time?**  No.  Only divisors of the finite nonzero integer
    \(a^n-b^n\) contribute.
12. **Why include \(N=1\)?**  Its singleton supplies the divisor 1 term in
    \(\sum_{N\mid m}\varphi(N)=m\); it is stated explicitly.
13. **Are all contributing divisors admissible?**  Yes.
    \((a^n-b^n,ab)=1\) when \((a,b)=1\).
14. **Can the profinite map have a fixed point without \(q^n=1\)?**  No.
    Translation in any group has a fixed point only for identity translator.
15. **Does the inverse-limit nonfixing proof require a prime table?**  No.
    Euclid supplies a prime outside the finite divisor set
    \(ab(a^n-b^n)\); no target list enters computation or proof.
16. **Do incompatible globalizations prove absolute no-owner existence?**
    No.  They prove nonselection by the finite-fiber data alone.  The weaker,
    rigorous conclusion is used everywhere.
17. **Does “prime return modulus” mean “prime-labeled primitive orbit”?**
    No.  The prime indexes a finite fiber; this distinction keeps A0 and A1
    weak.
18. **Could finite checks prove the all-parameter theorem?**  No.  They are
    deterministic drift sentinels only.
19. **Can A4 repair A2?**  No.  Finite permutation and profinite Haar Koopman
    unitaries provide a natural same-clock lift but no target divisor match.
20. **Did scope leak through the rational zeta?**  No.  It is one unweighted
    source fixed-count zeta, not a product weighted by primes and not an
    arithmetic local factor.
21. **Can an attribution status be changed to `NEW_THEOREM_CLAIMED` while
    preserving a permissive keyword?**  No.  Every complete attribution entry,
    including status, must exactly match its frozen map.
22. **Can A0 retain its expected prefix and append a log-(p) clock claim?**
    No.  The entire Route-A map is matched exactly; appended semantics fail.
23. **Can A4 retain `SAME_CLOCK_UNITARIES` and append a target-operator
    identification?**  No.  Exact qualification matching rejects the repaired-
    hash payload.
24. **Can the owner theorem preserve “incompatible fixed ledgers” but infer
    absolute impossibility of every enlarged owner?**  No.  The whole theorem
    ledger is frozen exactly to nonselection by the finite fibers alone.

## Verdict

The four-theorem chain survives.  C179 is a substantial arithmetic-origin
and primitive-return advance with a precise global-owner obstruction, but it
does not pass the target determinant or analytic-structure gates.  The release
checker now enforces these ownership and scope boundaries by exact maps, not
by claim-bearing substring tests.
