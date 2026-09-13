# Paper 22 — Initial Proposal and Correction Log

This is an author design-history record, not an independent review.

## Starting idea

The initial high-dimensional extension asked whether adding a fourth
Hamiltonian mode to the Paper 21 endpoint-spiked product family could produce
a quartic Perron number. The tentative family was

$$
V(q)=\prod_{i=1}^r q_i^2+q_1^g,\qquad
W(p)=\prod_{i=1}^r p_i^2+p_r^g,
$$

with $F=T\circ S$ and $r\ge4$.

The literal quartic expectation failed. Middle-coordinate permutation
symmetry creates difference directions on which both phase matrices act by
$-I$, so the complete-step matrix acts by $I$. The nontrivial dynamics
remain three-dimensional no matter how large $r$ becomes.

That failure changed the proposal from “one more mode gives a higher-degree
Perron root” to “arbitrary mode number produces a stable cubic spectral
collapse.”

## Corrections imposed by the candidate gates

### 1. Fixed public range

The new theorem begins at $r\ge4$. The $r=3$ specialization is Paper 21 and
is retained only as a consistency test. The $r=2$ mechanism belongs to Paper
20.

### 2. Exact normalization

The normalized variables are

$$
x_i=u_i/u_1\quad(2\le i\le r),
$$

and

$$
\sigma=\sum_{i=2}^r x_i.
$$

Including a fictitious $x_1$ in this sum would invalidate threshold seed
containment.

### 3. Cone terminology

The region

$$
x_i\ge1,\qquad \sigma<\frac{g-2}{2}
$$

is an explicit sufficient invariant selector cone. The initial phrase “exact
selector cone” was removed because maximality, necessity, uniqueness, and
classification are not proved.

### 4. Separate second-phase proof

The last-row $W$ selector acts on $v=Au$, not directly on $u$. Its strict
margin must be expanded and checked in two coefficient cases. Treating $B$ as
an arbitrary second matrix or inferring its selector from samples is
prohibited.

### 5. Full cone-wall proof

Every lower face $x_i=1$ is allowed. The output lower faces and the open
height inequality require separate formulas. The least rank $r=4$, least
parameter $g=2r+1$, and approach to the open height boundary must remain
visible.

### 6. Carries and leading forms

Degree inequalities alone do not prove polynomial survival. The final design
uses a phase-labelled carry induction and a highest-homogeneous-form argument
in a polynomial domain. This also permits arbitrary nonzero signs or phases
for exactly four coefficients on the same supports.

### 7. Visibility indexing

The last $q$-coordinate is strictly maximal only for $n\ge1$. At $n=0$ all
degrees tie, although the matrix formula still equals one.

### 8. Cubic wording

The stable three-dimensional quotient gives a cubic characteristic factor and
a cubic annihilating recurrence. It does not imply that every Perron root has
algebraic degree exactly three or that the recurrence is always minimal.

### 9. Sharpness wording

At $g=2r$ the first seed scores tie and the seed reaches the open cone
boundary. This is sharpness for the selected face and seed only, not a theorem
that all possible degree descriptions fail.

### 10. Portfolio boundary

Paper 20 and Paper 21 must be disclosed as direct predecessors. The preferred
local treatment is a separated successor beginning at $r\ge4$. Any future
public overlap requires a separately authorized disclosure review.

## Rejected expansions

- a quartic Perron headline for $r=4$;
- a theorem for arbitrary supports or Hamiltonian potentials;
- maximal cone or Newton-fan classification;
- positive characteristic;
- generic entropy, periodic-point, integrability, or non-conjugacy claims;
- an unconditional rank-three extension or correction;
- proof by finite ranks, CAS determinants, or numerical eigenvalues; and
- literature priority from a bounded search.

## Initial-gate outcome

The corrected theorem passed the two candidate gates. That pass authorized
only the ten-file source-design package. It did not authorize an independent
source-design PASS, source lock, manuscript, build, release, Paper 23, or
external effect.
