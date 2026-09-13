# Paper 24 — Research Question and Scope Lock

## Working title

**Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product
Shears**

## Principal research question

Can one give a completely explicit two-mode Hamiltonian product-shear family
whose actual iterate degrees do not remain in one stationary selector chamber
but instead cross a genuine Newton wall at every step, with strict carry,
arbitrary-nonzero-coefficient no-cancellation, a visible coordinate, and an
exact two-step monodromy law?

The question is answered only for

$$
V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
$$

$$
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S,
$$

over a characteristic-zero field, with integers $m\ge2$, $s\ge1$, and
arbitrary nonzero $A,B,C,D$.

## Formal input/output contract

### Inputs

- a characteristic-zero field $K$;
- integers $m\ge2$ and $s\ge1$;
- nonzero coefficients $A,B,C,D\in K^\times$;
- ordinary total degree on $K[q_1,q_2,p_1,p_2]$;
- the ordinary seed $(1,1)^{\mathsf T}$.

### Outputs

1. polynomial symplecticity and explicit subtraction inverses;
2. the literal four-row gradient-support ledger;
3. the exact selector wall $r=2$ and branch matrices $A_-,A_+,B_m$;
4. the corrected projective branches $h_m$ and $\ell_m$ with strict chamber
   exchange;
5. true-polynomial carry in both phases, not only weighted support selection;
6. top-homogeneous survival for arbitrary nonzero coefficients in
   characteristic zero;
7. strict $q_1$ visibility for every positive iterate;
8. the exact monodromy matrix $P=(B_mA_+)(B_mA_-)$;
9. the exact recurrence, wall gaps, parity closed forms, and
   $\lambda_1(F_{m,s})=sm(2m+1)$;
10. a bounded wall-fixing lemma inside the crossed-binomial /
    diagonal-pure-power ansatz;
11. a conditional period-$k$ selector-to-monodromy lemma stated only as
    technique.

## Exact subquestions

1. Why do both competitive $V$-rows switch at the same wall?
2. Why is the wall exactly $r=2$?
3. Why do the projective branches exchange the two open chambers strictly?
4. Why does the wall remain excluded forever once the seed starts off it?
5. Why do selected first-phase rows beat the carried momentum coordinates?
6. Why do selected second-phase rows beat the carried position coordinates?
7. Why can arbitrary nonzero coefficients not cancel the selected top degree?
8. Which coordinate sees the true total degree, and why only for $n\ge1$?
9. How is the two-step monodromy multiplied and diagonalized by hand?
10. How do the parity subsequences, wall gaps, and integrality laws follow
    from the matrix law rather than from computation?

## Falsification tests

The research question receives a negative or narrowed answer if any of the
following occurs:

- the mixed/pure comparisons do not have the common factor $u_1-2u_2$;
- the corrected formulas for $\ell_m(r)-1$ or $2-\ell_m(r)$ fail;
- any first-phase or second-phase carry inequality fails;
- the top-homogeneous-part argument uses positivity instead of domain logic;
- $q_1$ fails to dominate one of the other three coordinate degrees;
- the product $(B_mA_+)(B_mA_-)$ or its spectrum changes;
- the wall-gap identities fail;
- the structural lemma is asserted beyond the crossed-binomial /
  diagonal-pure-power ansatz;
- the conditional period-$k$ lemma is turned into the headline novelty claim.

Finite iteration tables, approximate spectra, and computer factorization do
not answer these falsification tests.

## In-scope boundaries

- one explicit two-mode family with the displayed supports;
- arbitrary nonzero coefficients in characteristic zero;
- strict period-two chamber exchange off the wall;
- one visible coordinate and one two-step monodromy law;
- one bounded crossed-binomial wall-fixing lemma;
- one conditional period-$k$ technique statement.

## Out-of-scope boundaries

This project does not claim:

- the wall case $r=2$;
- $m=1$ or positive characteristic;
- zero coefficients, changed supports, or reversed phase order;
- classification beyond the crossed-binomial / two-pure-power ansatz;
- arbitrary period or automaton realization;
- maximal or necessary selector fans;
- inverse-degree, entropy, integrability, genericity, periodic-point, or
  nonconjugacy statements;
- novelty of tropical switching, Perron theory, or the abstract period-$k$
  lemma by themselves;
- absolute literature priority.

## Predecessor and permission lock

Paper 20 owns the nearest two-mode selector-to-matrix proof grammar. Papers 21
and 23 own stationary-regime cubic and quartic visible-matrix stories, and
Paper 22 owns the arbitrary-mode cubic-collapse mechanism. Paper 24 must
reproduce all theorem-critical definitions and proofs locally while presenting
only the strict period-two wall exchange, the two-step monodromy, and the
parity degree laws as its bounded delta.

This source-design package authorizes no source lock, paper plan, manuscript,
bibliography, build, PDF, release, registry change, or external action.
