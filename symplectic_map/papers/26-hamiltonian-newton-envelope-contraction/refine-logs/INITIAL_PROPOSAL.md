# Initial problem-anchored proposal

## Frozen identity

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

## Starting observation

A product of a lower position Hamiltonian shear and an upper momentum Hamiltonian shear often admits a tropical degree description. In the planar separated-pure-power case, the position support enters only through its Newton support function
\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2).
\]
This suggests a piecewise-linear recurrence
\[
u_{n+1}=B
\begin{pmatrix}H(u_n)-u_{n,1}\\H(u_n)-u_{n,2}\end{pmatrix},
\qquad B=\operatorname{diag}(e,f).
\]

The initial proposal was to determine whether this recurrence has only low-period selector tails and then convert its selector matrices into algebraic-degree bounds for \(\lambda_1\). A parallel inverse recurrence appeared to have the factors in the opposite order, suggesting a relationship between forward and inverse growth.

## Initial conjectural package

The first formulation contained four hypotheses:

1. \(E\) is a finite subset of the positive interior lattice;
2. all support coefficients are nonzero after collection;
3. both coordinates of every support point are at least two;
4. the momentum Hamiltonian is a sum of two separated pure powers.

It aimed for:

- exact tropical degree transport;
- an eventual selector word of period at most two;
- an algebraic-degree bound obtained from one- or two-step matrices;
- equality of forward and inverse exponential rates.

At this stage, “period at most two” was only a selector hypothesis, not a proved projective statement, and a coarse quartic wall bound looked possible from a two-step \(2\times2\) monodromy. Both points required refinement.

## Immediate proof risks

### Cancellation on a tied face

The max-plus recurrence is merely an upper bound unless the leading forms survive substitution. A Newton wall is the decisive case: several monomials of \(V\) have the same weighted degree, and their gradient contributions can interact.

Initial kill question:

> Is the gradient of every positive exposed face algebraically independent for every choice of nonzero collected coefficients?

Without a coefficient-uniform yes, the candidate would collapse to a generic-coefficient result or a special support family.

### Visibility versus vector degree

Even a correct fresh-gradient degree vector does not automatically equal the total degree of the full four-coordinate map. Each shear carries an old block. Both forward and inverse phase orders require strict inequalities naming the final visible block.

Initial kill question:

> Do exponents at least two force every fresh coordinate degree to dominate all carried coordinate degrees at every half-step?

### Selector cycle versus numerical cycle

A decreasing projective map can alternate sides of a fixed point. The selector labels may therefore alternate while the numerical ratios converge. Calling this a two-cycle would be false.

Initial kill question:

> Is there a global contraction strong enough to distinguish selector alternation from a nontrivial projective periodic orbit?

### Forward versus inverse indexing

The forward recurrence has \(B\mathcal A\), while the inverse recurrence has \(\mathcal A B\). Equality of spectral radii for fixed matrices does not by itself handle a changing selector.

Initial kill question:

> Is there an exact state identity, including its seed and shift, rather than only an analogy between \(AB\) and \(BA\)?

## Candidate proof route

The initial proof route was organized as follows.

1. Prove symplecticity from symmetric Hessian blocks and write the inverse phases explicitly.
2. For an exposed face polynomial \(P\), search for one monomial coefficient in \(\det\operatorname{Hess}P\) that cannot cancel.
3. Apply the characteristic-zero Jacobian criterion to \(P_X,P_Y\).
4. Propagate algebraic independence through face-gradient substitution and separated pure powers.
5. Derive strict carry inequalities from \(x,y,e,f\ge2\).
6. Projectivize the forward recurrence and inspect its chamber derivatives.
7. Compare the inverse projective map to the forward map by scaling.
8. Classify the fixed ray as interior or wall and compute the tail spectrum.

## Early face calculation

For a positive exposed face, choose its point \((x_0,y_0)\) with minimal \(x\). Positivity of the exposing normal makes it unique. The target coefficient
\[
X^{2x_0-2}Y^{2y_0-2}
\]
in
\[
P_{XX}P_{YY}-P_{XY}^2
\]
can only come from the self-pair of that monomial. Its value is
\[
c_{x_0,y_0}^{\,2}x_0y_0(1-x_0-y_0).
\]
This is nonzero in characteristic zero. This calculation removed the largest cancellation risk and upgraded the candidate from a generic tropical heuristic to a coefficient-uniform theorem prospect.

## Early projective calculation

In ratio \(r=u_1/u_2\), an active support point \((x,y)\) gives
\[
\phi_{x,y}(r)=\frac ef
\frac{(x-1)r+y}{xr+y-1}.
\]
Its logarithmic slope magnitude is
\[
\eta_{x,y}(r)
=
\frac{r(x+y-1)}
{((x-1)r+y)(xr+y-1)}.
\]
The denominator gap is
\[
x(x-1)r^2+2(x-1)(y-1)r+y(y-1)>0.
\]
The pointwise strict gap suggested contraction, but the initial proposal still had to establish a single constant below one over all \(r\), all active branches, and all walls.

## Provisional examples

Two examples were selected for different purposes.

1. \(E=\{(2,2)\}\), \(B=\operatorname{diag}(3,2)\), to certify a genuinely quadratic interior Perron value.
2. \(E=\{(2,8),(4,5),(5,3)\}\), \(B=\operatorname{diag}(24,11)\), to exhibit a nontrivial transient followed by selector alternation toward a wall.

The second example was required to report exact chamber ratios and the two-step monodromy, not a floating-point simulation.

## Initial anti-claims

The proposal never intended to establish:

- arbitrary mixed momentum Hamiltonians;
- supports touching axes or containing exponent one;
- positive-characteristic analogues;
- dimension-three selector classification;
- entropy, integrability, higher dynamical degrees, or orbit arithmetic;
- recurrence minimality;
- global novelty.

## Refinement decisions requested

The initial proposal asked the review stage to decide:

1. whether the face-Hessian coefficient really handles every tied face;
2. whether forward and inverse leading-form induction can be made fully symmetric;
3. whether pointwise log contraction is uniform;
4. whether a wall tail has an integer per-step Perron value, improving the coarse quartic expectation;
5. whether a literal state bridge replaces a separate inverse asymptotic proof;
6. how to separate the result from Papers 24 and 25.

The final proposal records the resolved form of each item.
