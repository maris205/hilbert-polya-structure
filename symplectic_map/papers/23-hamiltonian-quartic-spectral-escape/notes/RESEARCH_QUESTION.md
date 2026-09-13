# Paper 23 — Research Question and Scope Lock

## Working title

**Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree
Growth and Quartic Perron Subfamilies**

## Principal research question

Can one give a completely explicit four-mode positive-sign Hamiltonian
product-shear family whose actual iterate degrees are governed by a genuinely
four-dimensional matrix, rather than by the common unit sector and cubic
quotient occurring in the endpoint-spiked predecessor, and can one certify an
infinite algebraic-degree-four Perron subfamily without computation?

The question is answered only for

$$
V_g=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},\qquad
W_g=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g,
$$

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),\qquad
F_g=T_g^+\circ S_g^+,
$$

over a characteristic-zero field and for integers $g\ge10$.

## Formal input/output contract

### Inputs

- a characteristic-zero field $K$;
- an integer $g\ge10$;
- the displayed positive integer coefficient potentials;
- ordinary total degree on $K[q_1,\ldots,q_4,p_1,\ldots,p_4]$;
- the ordinary degree seed $\mathbf1=(1,1,1,1)^{\mathsf T}$.

### Outputs

1. polynomial symplecticity and explicit inverses;
2. the literal eight-row gradient-support ledger;
3. four strict support selectors and the selected matrices $A_g,B_g$;
4. one explicit sufficient invariant ratio cone containing $\mathbf1$;
5. the exact phase recurrence
   $$
   v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n,
   \qquad C_g=B_gA_g;
   $$
6. characteristic-zero positive-leading-form survival;
7. strict $q_4$ visibility for $n\ge1$ and
   $$
   \deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1;
   $$
8. the exact quartic characteristic polynomial and order-four recurrence;
9. $\lambda_1(F_g)=\rho(C_g)$;
10. an infinite quartic Perron subfamily for $g\equiv3\pmod5$;
11. an explanatory, explicitly nonnovel support-profile kernel lemma.

## Exact subquestions

1. Which four gradient rows contain a genuine pure-versus-product choice?
2. Why must the second two choices be evaluated at $v=A_gu$?
3. Which homogeneous inequalities keep all four choices strict forever?
4. Does the proposed cone return under every face of $C_g$?
5. Why do newly selected rows beat coordinates carried from the preceding
   phase?
6. Why can no selected leading form vanish over a characteristic-zero field?
7. Which fixed coordinate sees the maximum among all eight coordinate
   degrees?
8. How is every coefficient of $\chi_{C_g}$ obtained by hand?
9. Why does $g\equiv3\pmod5$ exclude both linear and quadratic factors?
10. Which part of the cubic-collapse explanation is reused infrastructure,
    and which concrete four-spike conclusion is the Paper 23 delta?

## Falsification tests

The research question receives a negative or narrowed answer if any of the
following occurs:

- the matrices read from the supports differ from the displayed matrices;
- a selector is non-strict anywhere in the declared cone;
- the seed is outside the cone for a claimed parameter;
- any target cone face fails;
- an inherited coordinate reaches a selected fresh degree;
- a selected coefficient can vanish in the stated field;
- $q_4$ fails to dominate one of the other seven coordinates;
- a principal minor changes the quartic;
- the reduction modulo five admits a root or quadratic factor;
- a checked primary source states the same complete theorem package.

Finite iteration tables, approximate spectra, and computer factorization do
not answer any of these falsification tests.

## In-scope boundaries

- one four-mode family with the displayed supports and coefficients;
- positive signs in both shears and the exact order $T_g^+\circ S_g^+$;
- characteristic zero and integer $g\ge10$;
- ordinary total degree and first dynamical degree;
- a sufficient, not maximal, selector cone;
- a quartic conclusion only for the certified congruence subfamily;
- a bounded comparison with Papers 20--22 and checked public neighbors.

## Out-of-scope boundaries

The project does not claim:

- validity for $g\le9$ or survival of the same itinerary at the $g=9$ tie;
- a globally optimal threshold or classification of selector chambers;
- subtraction shears, arbitrary signs, arbitrary coefficients, added
  supports, reversed phase order, or positive characteristic;
- irreducibility or algebraic degree four for every $g\ge10$;
- that every full-rank support profile produces quartic growth;
- novelty of gradient shears, weighted supports, matrix recurrences,
  Perron--Frobenius, Cayley--Hamilton, modular reduction, or the abstract
  common-kernel lemma;
- general weak-Perron realization, minimal dimension, optimal sparsity,
  non-conjugacy, entropy equality, integrability, genericity, periodic-point,
  or other arithmetic-dynamical conclusions;
- absolute priority from a bounded public search.

## Predecessor and permission lock

Papers 20 and 21 own the two- and three-mode selector-to-matrix proof
architecture.  Paper 22 owns the arbitrary-mode endpoint-spike cubic-collapse
theorem and its common unit-sector explanation.  Paper 23 must reproduce all
definitions and theorem-critical proofs locally while presenting only the
four-spike removal of that unit sector, exact visible quartic matrix, and
infinite irreducible quartic subfamily as its bounded portfolio delta.

This source-design package authorizes no source lock, paper plan, manuscript,
bibliography, build, PDF, release, registry change, or external action.
