# Local novelty and collision assessment

## Assessment scope

This assessment is limited to the audited local project corpus through Paper 25 and the locally frozen primary-source metadata listed in notes/CITATION_VERIFICATION.md. No web search, database query, or external novelty review has been performed for this source-design stage. The assessment can justify separation from the local portfolio; it cannot establish global priority.

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

## Claim-level novelty center

The project is not “another matrix degree-growth example.” Its proposed contribution is the conjunction of five proof mechanisms:

1. a coefficient-uniform Hessian certificate for every positive exposed face of an arbitrary finite planar Newton support;
2. a bidirectional leading-form induction that makes the Newton-envelope degree transports exact, including at walls;
3. a global strict contraction of the projective Newton-envelope map in logarithmic distance;
4. a complete selector-tail classification into interior stationarity and wall-fixed/alternating behavior; and
5. an exact shifted bridge between forward and inverse degree sequences, yielding equal exponential rates and a uniform quadratic algebraic-degree cap.

Removing any one of these changes the result materially. In particular, projective contraction without the face-Hessian lemma gives only a tropical prediction, while the face lemma without contraction gives no selector classification.

## Local portfolio collision map

### Paper 20: stationary two-mode quadratic regime

Collision: both projects can end in a positive \(2\times2\) integer matrix and a quadratic Perron root.

Separation: Paper 20 begins with a fixed stationary selector. Paper 26 derives eventual stationarity or wall alternation from an arbitrary finite interior support, proves wall-safe top-form survival, and treats inverse degree growth through an exact bridge.

Wording discipline: do not claim novelty for the bare quadratic Perron formula or for Cayley–Hamilton in dimension two.

### Paper 21: three-mode cubic recurrence

Collision: both projects expose finite-dimensional linear recurrences in degree data.

Separation: Paper 21 owns a fixed three-mode cubic visible recurrence. Paper 26 owns a nonlinear Newton-envelope transient, a contraction theorem that selects the tail, and a planar arithmetic cap. Its recurrence is a consequence, not the headline.

Wording discipline: do not market the existence of a recurrence alone.

### Paper 22: arbitrary-mode cubic endpoint collapse

Collision: both allow a larger support before reducing to a small asymptotic description.

Separation: Paper 22 uses endpoint-spike cubic collapse and a common unit sector. Paper 26 allows arbitrary finite positive interior planar support and uses log contraction plus exposed-face algebraic independence. No endpoint-collapse claim is imported.

Wording discipline: distinguish “arbitrary finite interior support” from “arbitrary modes” without implying broader dimensionality.

### Paper 23: fixed four-mode quartic escape

Collision: both use exact tropical transport to discuss Perron algebra.

Separation: Paper 23 fixes four modes to obtain quartic escape. Paper 26 proves that its much more structured planar separated-pure-power family cannot escape beyond quadratic degree. These are complementary arithmetic regimes.

Wording discipline: no claim that Paper 26 improves a quartic bound for the Paper 23 class; the hypotheses differ.

### Paper 24: two-term wall and selector period two

This is the strongest direct collision.

Collision:

- Newton walls and adjacent selector matrices;
- a two-step monodromy;
- parity recurrences;
- explicit selector alternation.

Separation:

- Paper 24 studies a special two-term wall criterion and a forced selector word; its general finite-period mechanism is conditional.
- Paper 26 derives a global decreasing contraction for arbitrary finite positive interior support.
- Paper 26 excludes nontrivial numerical projective cycles and proves that apparent period-two selector behavior converges to a single wall ray.
- Paper 26 treats the full face polynomial on a wall, not one selected tied monomial.
- Paper 26 proves the wall per-step Perron value is an integer and couples the forward result to an exact inverse bridge.

Wording discipline: always call the tail “selector alternation converging to a wall,” not “a two-cycle.” Present Paper 24-style monodromy only after the contraction classification.

### Paper 25: support rank and unbounded Perron degree

This is the second strongest collision.

Collision:

- support-dependent tropical degree transports;
- Hamiltonian shear compositions;
- algebraic degrees of Perron values;
- forward/inverse degree considerations.

Separation:

- Paper 25 establishes support-rank upper bounds, stationary sharp constructions, unbounded Perron degree as support dimension grows, and scalar minimality.
- Paper 26 fixes planar support but allows arbitrary finite Newton polygons, then proves contraction-driven selector rigidity and a uniform quadratic cap.
- Paper 26's key face-Hessian certificate and exact projective forward/inverse conjugacy are not the support-rank construction of Paper 25.

Wording discipline: do not describe the quadratic cap as contradicting unboundedness; it is a rigidity theorem for a narrower planar separated family.

## Nearest prior-art threats from local metadata

The local bibliography indicates four collision zones that require eventual external verification.

### Algebraic entropy and degree growth

Bellon–Viallet and subsequent dynamical-degree literature establish the general importance and birational invariance context of exponential degree growth. Threat: a known theorem may already equate forward and inverse rates under broader birational hypotheses. Response: Paper 26 should claim novelty only for its exact sequence bridge and elementary cancellation-free derivation, not for abstract equality if that equality is already known.

### Cluster and tropical recurrences

Fordy–Hone and Ishibashi–Kano connect symplectic or mutation dynamics to tropical degree recurrences and entropy. Threat: a sign-stability or tropical contraction result may resemble selector stabilization. Response: specify the Newton-envelope formula, coefficient-uniform face proof, and wall classification; avoid generic claims about tropical dynamics.

### Polynomial symplectomorphisms and triangular dynamics

Janeczko–Jelonek, Blanc–van Santen, Berger–Turaev, and Koch–Lomelí provide structural context for polynomial symplectic or triangular maps. Threat: broader classifications may subsume special product shears. Response: present the result as an explicit theorem inside one family and verify later whether the exact family is already normal-formed or classified.

### Spectral interpretations of dynamical degree

Dang–Favre and related work offer general spectral frameworks. Threat: the Perron description itself is standard. Response: attribute the spectral viewpoint as context and claim only the derivation of the particular selector matrices, contraction, and arithmetic cap.

## Strongest locally defensible statements

Safe abstract language:

> For a finite planar Newton support contained in \(\mathbf Z_{\ge2}^2\) and a separated pure-power momentum Hamiltonian, we prove a coefficient-uniform exposed-face Hessian lemma that makes the tropical degree transport exact in both time directions. The induced projective envelope map is a global log contraction, forcing a stationary or wall-alternating selector tail and bounding the first dynamical degree by a quadratic algebraic number; on a wall it is integral.

Safe local novelty language:

> Relative to the audited Papers 1–25 corpus, the new ingredient is the combined arbitrary-face cancellation certificate, global selector contraction, and exact forward–inverse transport.

Unsafe until external verification:

- “This is the first contraction theorem for Newton-envelope degree dynamics.”
- “No previous work treats arbitrary finite support.”
- “We completely classify degree growth of planar polynomial symplectomorphisms.”
- “The equality \(\lambda_1(F)=\lambda_1(F^{-1})\) is new.”
- “Our quadratic cap is optimal among all Hamiltonian product shears.”

## Proof novelty versus example novelty

The one-face fixture \(E=\{(2,2)\}\) is not novel as a matrix calculation. Its role is to witness a genuinely quadratic interior Perron value and to check the shifted bridge.

The three-support fixture is also not the primary novelty. Its exact monodromy demonstrates the wall branch of the theorem:
\[
E=\{(2,8),(4,5),(5,3)\},\quad
B=\operatorname{diag}(24,11),\quad
\lambda_1=132.
\]
Its selector word has a transient low–high prefix and then alternates middle–high while the projective ratios converge to the wall \(r=2\). The contribution is the theorem explaining this behavior for every support in scope, not the isolated integers.

## Collision-driven manuscript architecture

To minimize overlap:

1. lead with the arbitrary exposed-face Hessian coefficient, not a selector matrix;
2. put the forward and inverse leading-form inductions before all examples;
3. derive global log contraction before introducing two-step monodromy;
4. label wall alternation as convergence to a fixed ray;
5. use the exact bridge to integrate inverse growth into the main theorem;
6. compare the uniform quadratic cap explicitly with the different-hypothesis unbounded constructions of Paper 25.

The related-work section should be short until an external novelty search is complete. Mathematical limitations should remain in the theorem section rather than being softened in prose.

## External verification requirements

Before submission, an independent literature pass must search at claim level for:

- polynomial Hamiltonian shears with arbitrary Newton polygons;
- Hessian nonvanishing or algebraic independence for positive exposed faces;
- projective contractions of max-plus or Newton-envelope maps;
- selector stabilization and wall alternation in tropical degree recurrences;
- exact forward/inverse degree-sequence relations for polynomial automorphisms;
- algebraic-degree bounds for dynamical degrees of planar-support symplectic maps.

It must also verify every bibliographic field in the citation file against a primary record. If any source contains the same conjunction of mechanisms, the novelty center must be narrowed before drafting a paper.

## Kill criteria

The candidate is not publication-worthy in its present form if any of the following is found:

1. an in-scope exposed face with identically zero Hessian determinant;
2. a forward or inverse wall cancellation invalidating exact degree transport;
3. failure of a support-uniform log contraction constant;
4. an in-scope selector tail outside interior stationarity or wall alternation;
5. an in-scope Perron value of algebraic degree above two;
6. a prior source proving the same arbitrary-support, wall-safe, bidirectional contraction theorem;
7. unavoidable dependence on generic coefficients.

No such mathematical killer appears in the current symbolic audit. The literature killer remains untested externally and is therefore explicitly open.
