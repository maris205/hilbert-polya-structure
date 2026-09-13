# Paper 23 — Initial Proposal and Correction Log

## Starting idea

The initial candidate asked whether the endpoint-spike cubic-collapse
mechanism could be escaped by placing two pure-power competitors in each
phase of a four-mode Hamiltonian product shear.  The proposed potentials were

$$
V_g=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},\qquad
W_g=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g.
$$

The hoped-for outcome was not merely a formal $4\times4$ matrix.  It required
an actual-degree theorem: four persistent support selectors, temporal carry,
noncancellation, one fixed visible coordinate, and an irreducible quartic
Perron subfamily.

The candidate gate accepted that direction with a narrow novelty margin
because Papers 20--22 already own most of the selector/matrix/Perron proof
grammar.

## Corrections imposed by the candidate gates

### 1. Freeze positive signs

The original R1 artifact printed a negative first shear and included an
unsupported sign-generalization sentence.  The immutable R1 correction
withdraws both points as theorem authority.  The only accepted family is

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p).
$$

No claim survives for subtraction or arbitrary signs without a new proof.

### 2. Freeze the phase order

The composition is exactly

$$
F_g=T_g^+\circ S_g^+.
$$

Thus the intermediate vector is $v=A_gu$ and the complete matrix is
$C_g=B_gA_g$.  Reversing the factors changes the proof object.

### 3. Restrict the field

Characteristic zero is a theorem assumption, not a cosmetic convention.
Positive integer leading coefficients remain nonzero only under that
assumption.  No positive-characteristic extension is proposed.

### 4. Restrict the parameter range

The ordinary seed margins are

$$
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.
$$

At $g=9$ they are $(1,0,-2,5)$, so the stated four-face itinerary already
fails at iteration zero.  The theorem therefore begins at integer $g=10$.
This is sharp only for this seed and itinerary, not globally.

### 5. Replace heuristic selector persistence by an explicit cone

Finite degree iterates cannot prove persistence.  The source design uses the
simple sufficient ratio cone

$$
1\le x\le\frac{g-1}{g-2},\qquad
1\le y\le z\le\frac{g-1}{g-2}y,\qquad
y+z<\frac{g-5}{2}.
$$

This is a separate hand-closed sufficient cone.  It is not claimed maximal,
necessary, or equivalent to every alternative sufficient cone appearing in
the adversarial candidate record.  All six target faces are proved locally.

### 6. Keep selector choice separate from carry

The four internal pure-versus-product comparisons do not by themselves show
that a fresh gradient row beats an inherited coordinate.  The source design
adds the base inequality $A_g\mathbf1>\mathbf1$, full-step monotonicity from
$C_g-I_4>0$, and the later first-phase margin
$A_g(u_n-u_{n-1})>0$.

### 7. Replace sign folklore by positive-semiring survival

Every forward coordinate polynomial has nonnegative integer coefficients.
Selected coefficient paths add rather than cancel, and characteristic zero
keeps their positive sums nonzero.  This is the only no-cancellation argument
used.

### 8. Prove visibility rather than guess it

The fourth row must beat the other three complete $q$ rows on the cone, and
$C_g-A_g>0$ must then compare complete $q$ rows to final $p$ rows.  Strict
visibility starts at $n=1$; the identity seed is tied.

### 9. Derive the quartic coefficient by coefficient

The quartic is not accepted from interpolation or CAS.  The source design
lists the trace, six second-order principal minors, four third-order principal
minors, and determinant factorization.

### 10. Expand the modular argument

For $g\equiv3\pmod5$, root testing alone excludes only linear factors.  The
proposal now also enumerates all four possibilities for the constant terms of
two monic quadratic factors.

### 11. Demote support rank to explanation

The common-kernel lemma is standard linear algebra and direct Paper 22
infrastructure.  Paper 23 may use it to explain why the old unit sector is
absent, but not as a novelty headline or classification theorem.

### 12. Impose bounded novelty language

The R1 search found no direct collision with the complete package, but it was
bounded and some neighbors were accessed only at abstract/metadata level.
Absolute-priority language is prohibited.

## Rejected expansions

- arbitrary signs or subtraction shears;
- positive characteristic;
- arbitrary nonzero coefficients or added monomials;
- the opposite phase order;
- $g\le9$ branch analysis;
- maximal-cone or all-chamber classification;
- irreducibility for every parameter;
- every-full-rank-profile-implies-quartic claims;
- general weak-Perron realization, minimal dimension, optimal sparsity,
  non-conjugacy, entropy, integrability, genericity, or periodic conclusions;
- numerical or CAS certification;
- global priority.

## Initial-gate outcome

The corrected candidate survived as a proof-first, fixed-family theorem.  The
source-design task is to make every dependency auditable without enlarging
that theorem.  No independent source-design verdict is asserted here.
