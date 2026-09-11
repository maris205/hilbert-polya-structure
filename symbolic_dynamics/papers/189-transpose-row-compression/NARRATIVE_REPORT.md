# P189 narrative report

**Round:** `ROUND0_AUTHOR_FREEZE`  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

The state is a labelled binary square matrix.  One epoch left-compresses each
source row and then transposes, so the output remembers the labelled row-sum
vector as column heights.  The second epoch applies threshold counting to
those heights.  Threshold counting is partition conjugation after sorting,
and applying it twice sorts an arbitrary vector.  This gives the complete
temporal normal form

```text
F(A)=D(r),  F^2(A)=D(r*),  F^3(A)=D(r_down),  F^4(A)=F^2(A).
```

The paper develops two independent axes.

1. The normal form identifies every recurrent matrix, fixed point, strict
   two-cycle, and exact depth layer.  The recurrent core consists of Ferrers
   matrices and conjugation is the recurrent action.
2. The inverse atlas keeps labels rather than quotienting them away.  At time
   one, row supports are chosen independently at prescribed row sums.  At
   time two, the required row-sum multiset is assigned to labelled rows and
   then each support is chosen independently.

The first and second images have `(n+1)^n` and `binom(2n,n)` states.  The
fixed and strict two-cycle counts are `2^n` and
`(binom(2n,n)-2^n)/2`.  The exact depth-at-most-one population is a weighted
partition sum, equivalently a coefficient of a finite product.

Ferrers matrices, conjugate partitions, diagonal hooks, line sums, and
generic functional-graph bookkeeping receive zero contribution credit.  A
bounded primary/authoritative search did not locate the literal repeated map
together with both inverse laws; this non-hit is not novelty or priority
evidence.  External circulation remains unauthorized.
