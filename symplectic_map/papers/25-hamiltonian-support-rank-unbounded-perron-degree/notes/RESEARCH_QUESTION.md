# Research Question

## Primary question

For degree dynamics selected from Hamiltonian position and momentum
gradient shears, does the row rank of the active supports impose a sharp
upper bound on nonunit spectral complexity, and can that bound be attained
in arbitrarily large rank by explicit maps whose ordinary total degrees are
proved exactly rather than approximated tropically?

## Precise mathematical formulation

The question separates into an abstract bound and a realizability problem.

### RQ-A: abstract support-rank bound

Given

$$
A=-I_n+\mathsf P\mathsf Q,\qquad
B=-I_n+\mathsf R\mathsf S,\qquad C=BA,
$$

and

$$
r=\operatorname{rank}\binom{\mathsf Q}{\mathsf S},
$$

must $\chi_C(t)$ have a factor $(t-1)^{n-r}$? If so, the degree of the
remaining characteristic factor is at most $r$. The question asks for this
factorization only; it does not ask rank data to determine the exact
multiplicity of one.

### RQ-B: sharp Hamiltonian realization

For every integer $d\ge2$, is there an explicit positive
integer-coefficient polynomial symplectomorphism of the form
$F=T_W\circ S_V$ on $2d$ affine coordinates such that:

1. its literal selected gradient rows have stacked rank $d$;
2. the selected degree matrix is a strictly positive $d\times d$ matrix;
3. one fixed coordinate realizes the ordinary degree of every positive
   iterate;
4. the Perron root has algebraic degree $d$; and
5. the visible scalar sequence has minimal rational recurrence order $d$?

## Proposed answer

Yes, within the explicit positive characteristic-zero family

$$
V(q)=\prod_jq_j^2+\sum_iq_i^{a_i+1},\qquad
W(p)=\prod_jp_j^b.
$$

The selected matrix is

$$
C=b\mathbf1a^{\mathsf T}-D.
$$

A row-basis factorization proves the abstract bound. A prescribed
finite-field residue construction makes $\chi_C$ irreducible of degree $d$.
A broad coordinate-ratio cone proves uniform spike selection and
cross-phase domination, while a nested weighted chamber makes $q_1$ the
fixed visible coordinate. Positivity closes the gap between selected matrix
degrees and polynomial degrees. Irreducibility makes the state and
observation cyclic, forcing scalar recurrence order $d$.

## Why the question is not already answered by the local lineage

| Predecessor | Occupied result | Residual question answered here |
|---|---|---|
| Paper 20 | A stationary two-mode matrix and quadratic Perron formula | No support-rank law or unbounded degree |
| Paper 21 | A three-mode visible cubic recurrence and cubic subfamilies | No arbitrary-rank sharpness |
| Paper 22 | An arbitrary-mode endpoint-spike family with a forced common unit sector and cubic collapse | Supplies the closest kernel intuition but not a general row-basis factorization with sharp examples in every $d$ |
| Paper 23 | A fixed four-mode full-profile quartic family | Occupies $d=4$ but not the uniform all-$d$ arithmetic and scalar-minimality theorem |
| Paper 24 | A two-mode period-two selector exchange and parity monodromy | Uses a nonstationary selector mechanism, not the stationary strict-face rank law |

The residual question is not “what happens in five modes?” An isolated
$d=5$ answer would be incremental. The contribution must remain the
uniform rank law and all-$d$ sharp realization.

## Dependency questions

1. Can $C-I_n$ be factored through exactly the stacked selected row space?
2. Can parameters be chosen in a fixed quantifier order without using a
   search?
3. Which inequalities require only the broad ratio cone, and which require
   the finer weighted chamber?
4. Do fresh gradient terms beat every carried coordinate at both
   half-steps?
5. Why can no selected top form cancel over an arbitrary
   characteristic-zero field?
6. Does the modular reduction satisfy every condition of the irreducible
   binomial theorem?
7. Why does a matrix recurrence of dimension $d$ remain minimal after the
   scalar observation $e_1^{\mathsf T}$?
8. Does the selected support presentation actually have rank $d$?

Each question is a hard dependency. A negative answer to any one of
questions 2--8 destroys the all-$d$ exact-visibility theorem; a negative
answer to question 1 destroys the structural framing and sharpness claim.

## Falsifiers

The proposed answer is falsified as stated by any of the following:

- a matrix dimension error in the Sylvester factorization;
- an extra unit root being incorrectly ruled out by rank alone;
- a parameter choice that must be made after seeing an orbit;
- a selector tie on either cone or at the ordinary seed;
- a carried $p$ or $q$ coordinate matching or exceeding a fresh term;
- a possible leading-form cancellation in characteristic zero;
- failure of the binomial criterion for $d=2$ or $4\mid d$;
- a noncyclic state or observation that lowers the Hankel rank;
- a stacked selected-row rank below $d$;
- dependence of the headline on a fixed-dimensional example or a
  computational certificate.

## Scope boundaries

The question is existential and construction-specific. It does not ask for
arbitrary signs, supports, exponents, coefficients, or shear words. It does
not ask to realize all weak Perron numbers, minimize dimension or sparsity,
compare forward and inverse growth, determine higher dynamical degrees,
construct a compactification, identify entropy, prove integrability, classify
selector dynamics, or establish genericity or nonconjugacy. It does not ask
for positive-characteristic validity or exact unit multiplicity. It carries
no absolute priority claim.

## Success criterion

Success requires a self-contained proof of the abstract factorization and
the complete all-$d$ realization, including exact ordinary-degree visibility
and exact scalar minimality, plus bounded and honest positioning. Anything
less is a lemma, example, or partial construction rather than the proposed
Paper 25.
