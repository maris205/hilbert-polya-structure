# Contact-order flat weights and the loss of clocks on full cohomology

**Audit:** `ANG-AUDIT-20260921-COG01`; **flow:** `ANG-20260921-RCF01`.  
**Batch:** `RCF01-BATCH-20260921-A`, round3/5; 2026-09-21.  
**Status:** `ORDER-WEIGHTED FLAT SQUARE; COHOMOLOGICAL TRACE STOP`.

## Abstract

The actual contact filtration gives weights(0,1,3,4) on the owned
three-dimensional contact complex. With the frozen unnormalized convention,
its weighted flat measure is twice the ordinary orbit measure and its
function is zeta to power minus2. This structural cancellation is distinct
from351's ordinary degree weighting. However the complete flow acts as
identity on both smooth and compact-support cohomology. The specified
compact-support cohomology Hilbert completions have non-trace-class identity
actions in their nonzero degrees. Finite-component comparisons lose the
periods as well. Thus the flat identity is not an ordinary cohomological
determinant mechanism for this owner. The next question returns to source
and clock naturalness instead of further local trace repairs.

## 1. Same-object identity

The [88-line card](candidate-card.md) fixes the entire RCF01 contact
quotient, physical flow and351 complex, with their input locks. Q is the
disjoint union of a terminal R3 and Q_p=(R/(log p)Z)xR2 for ALL cover
atoms p. Phi^t(u,v,z)=(u+t,exp(t)v,exp(-t)z), and
beta=(1+vz)du+(v dz-z dv)/2. Every source state and all source lag data
remain; no cohomology calculation changes this physical owner.

The lineage is still the proper-divisor/factor-word source and its full
contact lift. This new analytic audit concerns the contact-order functional
and explicitly specified cohomology owner. It does not change350/351
weights or declare their results to have had this meaning all along.

## 2. Question and nonclaims

Do intrinsic differential orders justify different weights, and does the
resulting flat identity descend to an ordinary cohomological trace?
The first answer is positive at the specified unnormalized convention;
the second is negative for the specified full cohomology Hilbert spaces.
No analytic torsion, Laplacian, generator spectrum, quantization or target
zero claim is supplied. This is not a no-go for every other analytic space.

## 3. Definitions

Use351's C^j and actual degree flat traces Theta_C,j. Freeze
w=(0,1,3,4), Theta_ord=sum(-1)^j w_j Theta_C,j, and
D_ord=exp(-integral exp(-s t)Theta_ord(dt)/t), without a half factor.
The scalar S and orbit measure O are349's same-flow measures.

Compute smooth and compact-support cohomology separately. The latter's
component generators are normalized by constant1 on H^0 of a circle,
integral1 on H^1 of a circle and on real-fiber top classes. Their direct
sum is then completed with these generators orthonormal, as the P0
explicitly specifies, to form K_c^j. This is a NEW classical cohomology
Hilbert owner, not the full cochain L2 owner or a physical state selection.

## 4. Proof

### O1. Order grading from the actual contact geometry

On any local lift of u set theta=u, x=exp(-u)v, y=exp(u)z. Direct
substitution gives beta=dtheta+(x dy-y dx)/2. This is a local chart,
NOT a global clock or quotient change on a circle component.
The contact-coordinate dilation(theta,x,y)->(lambda^2 theta,lambda x,
lambda y) scales beta by lambda^2 and horizontal covectors by lambda.
It describes the associated contact filtration, not the physical flow.
The horizontal fields X=partial_x+(y/2)partial_theta and
Y=partial_y-(x/2)partial_theta satisfy[X,Y]=-partial_theta.
Thus horizontal derivatives have contact order1 and the Reeb derivative
order2, precisely the nonzero Levi bracket structure.

C^0, C^1, C^2=beta wedge A^1 and C^3=beta wedge A^2 therefore have
weights0,1,3,4. Their differential-order increments are1,2,1. They
are actual orders, not only upper bounds: for a=f dx the middle lift
has h(a)=-Yf and delta_1 a=beta wedge[(R f-XYf)dx-Y^2f dy],
which has a nonzero second-horizontal-derivative term. Delta_0 and
delta_2 have nonzero first-horizontal-derivative terms. This justifies
the chosen grading without matching a desired orbit coefficient.

### O2. Actual flat functional and its limits

All four individual kernels already exist on the full Q by351, with
degree traces(S,A,A,S), where A=O+2S. The fixed order weights give

```text
Theta_ord=-A+3A-4S=2O,
D_ord(s)=D_orb(s)^2=zeta(s)^(-2), Re s>1.
```

The exact absolute /t and Laplace domain is Re s>1, by349's orbit
majorants and prime reciprocal divergence. Local uniform convergence
justifies logarithmic differentiation. Normalization is1 at large real
part; meromorphic continuation follows from the already identified
classical zeta, not an independent spectral theorem.

For arbitrary constant degree weights a=(a0,a1,a2,a3), direct algebra gives

```text
Theta_a=(a2-a1)O+[a0-a3+2(a2-a1)]S.
```

Thus ordinary degree weights give O-S, standard parity with all weights1
gives0, and eliminating S alone does not uniquely characterize a grading.
The contact grading has the independent filtration justification in O1;
it still supplies the factor2. A half-log prescription would be a new
normalization, not the present D_ord or an automatically obtained analytic
torsion. No such rescaling is applied. A metric/Laplacian, domains and
regularization would be additional obligations for a torsion claim.

### H1. Smooth cohomology of the entire owner

The explicit351 comparison identifies its smooth cohomology with de Rham.
Contracting the real(v,z) fibers of Q_p to zero gives the circle's
cohomology by the ordinary homotopy formula. The circle has H^0=C,
H^1=C (integration detects the class, zero-integral one-forms have a
periodic primitive), and no higher groups. R3 is contractible.
Smooth forms on a disjoint union form a PRODUCT of component complexes;
with no growth condition imposed, component primitives can also be
assembled in that product. Hence

```text
H^0_smooth=product_(b in {terminal} union P) C,
H^1_smooth=product_(p in P) C,
H^j_smooth=0 for j=2,3.
```

This product is not an unspecified Hilbert space, and no ordinary trace
is assigned to it. P is the full intrinsic atom set, not a cutoff list.

### H2. Compact-support cohomology, proved by fiber integration

For the real line choose rho in C_c^infinity(R) with integral1 and set
F(s)=integral_(-infinity)^s rho. For a compactly supported one-form
g(s)ds define

```text
H(g ds)(s)=integral_(-infinity)^s g(r)dr-F(s) integral_R g(r)dr.
```

This primitive is compactly supported. Its derivative is
g ds-rho ds integral g; on compactly supported functions H(df)=f.
Thus the line complex retracts to its integral1 degree1 class. The same
construction with smooth parameters preserves compact support jointly:
project a compact support onto the parameter space and bound its line
coordinates together with the fixed support of rho. Applying this twice,
with the usual exterior-degree signs, integrates the two real fibers of
S1 x R2, shifting degrees by2. Applying it three times handles R3.
This gives

```text
H_c^2(Q_p)=C, H_c^3(Q_p)=C; all other component H_c^j(Q_p)=0;
H_c^3(R3)=C; other H_c^j(R3)=0.
```

The generators are rho(v)rho(z)dv wedge dz and its product with du/L_p,
and the normalized compact top form on R3. Their stated integrals give
exactly the P0 normalization; the representatives need not be flow-fixed.
A compact subset of the full disjoint union meets only finitely many
open components. Compact-support forms therefore form a DIRECT SUM of
component complexes. With351's support-preserving comparison,

```text
H_c^2=direct-sum_(p in P) C,
H_c^3=C_terminal direct-sum direct-sum_(p in P) C,
H_c^0=H_c^1=0.
```

These results neither discard terminal data nor confuse the two support
conventions. They establish the component generators required to define
K_c^2=ell2(P), K_c^3=ell2({terminal} union P), with K_c^0=K_c^1=0.

### H3. Induced action and the decisive ordinary-trace obstruction

For any fixed real t, integration of the usual Cartan homotopy along
Phi^(-s), 0<=s<=t (with oriented integral if t<0), gives

```text
(Phi^(-t))*-I=d K_t+K_t d,
K_t omega=-integral_0^t (Phi^(-s))* i_R omega ds.
```

On compactly supported forms the union of the transported support over
the bounded time interval is compact, as the continuous image of a
compact set. Thus the homotopy works in BOTH domains. It follows that
every induced cohomology action is the identity. The contact-complex
comparison is flow-equivariant, so the same holds there. The closed-orbit
lengths have genuinely disappeared from this induced action.

There are infinitely many atoms (for example by the prime harmonic
divergence already proved in349). Both nonzero K_c degrees are therefore
infinite dimensional, and their induced action is the identity, not trace
class, at every time. Two divergent identity traces cannot be subtracted
to define an ordinary supertrace or weighted determinant.

Even on a terminal-plus-N-atom FINITE component control, the cohomology
traces are constant in time. Standard compact-support supertrace is
N-(N+1)=-1; contact-order weighted trace is3N-4(N+1)=-N-4.
They are neither the cochain zero supertrace nor the periodic Dirac
measure2O of those same components. The latter has isolated positive-time
support; the former are constant functions of time. The missing equality
cannot be repaired by an unexplained infinite-component cutoff. This is
a noncompact trace/descent obstruction, not a failure of351's complex.

## 5. Results

Contact-order weights give an owned positive flat measure2O and function
zeta^(-2). Full smooth and compact-support cohomologies are now explicit;
their induced action is identity and does not retain physical periods.
The specified nonzero K_c operators are not trace class. These are distinct
positive and negative statements, not a single unqualified determinant pass.

## 6. Own controls and alternative explanations

FACTOR-OFF has the same local order grading but all integer circle
components, plus TWO real components (empty and fixed-unit). Its weighted
flat trace is2O_F and its function Z_F^(-2) on Re s>1. Cohomology action
is again identity; finite N integer components plus both real components
give compact Euler trace-2 and order-weighted trace-N-8. This geometry
therefore does not isolate primes.

UNIT-HOLONOMY has a real R3 per basin and no physical periods. Its flat
trace is zero and flat function1, yet each component contributes a degree3
compact-support cohomology generator acted on by identity. The full K_c^3
is infinite dimensional, and even one component has cohomological
order-weighted trace-4. This sharp control prevents source lag or a
cohomology identity from being counted as a physical orbit trace.

The arbitrary-weight identity in O2 also prevents treating a formally
clean zeta power as unique evidence of a natural operator realization.
The present choice has a contact-filtration reason, but neither arithmetic
selection nor the missing ordinary cohomological trace is thereby solved.

## 7. Gates and scope

Order grading / actual weighted flat identity: ESTABLISHED. Full
cohomology and induced action: ESTABLISHED for the two stated domains.
Ordinary cohomological trace on the specified K_c: STOP, non-trace-class
and no retained clock. Analytic torsion/Fredholm/quantum interpretation:
NOT SUPPLIED. Strong naturalness OPEN; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. No universal other-space no-go.

## 8. Decision and next round

Portfolio **advance** the exact structural flat-function and cohomology
calculations; **stop** the ordinary-cohomological determinant route on
this owner. Three analytic rounds have located the limitation decisively;
do not spend the remaining batch on sign or degree-weight repairs.
Next audit the arithmetic naturalness of the physical logarithmic clock:
does the source/contact mechanism force it, or do equally owned arithmetic
transport deformations preserve the packets while changing their lengths?
Any changed physical transport must have a separate type-labelled control
card, with no RCF01 theorem/Route credit transferred by name.

## Evidence and integrity

[Card](candidate-card.md) · [Scope review](evidence/scope-review.md) ·
[Independent proof](evidence/independent.md).
All arguments are exact; finite N is an algebraic control valid for every
finite set, not an experiment or an infinite trace definition. No new
external theorem is needed beyond the previously documented same-owner
analytic inputs. Internal AI work is not external peer review, human
proof verification or calibrated assurance.

EOF — round3 author proof; analysis/final review pending.

## Final notation clarification

The original265-line analysis input is preserved. In O1, h(a) denotes
the horizontal coefficient c(a) defined by d_H a=c(a)Omega, NOT the
middle-lift correction b. For a=f dx it is c(a)=-Yf; the correction is
b=-c(a)=+Yf, so the lift is a+(Yf)beta. The displayed delta_1 formula
and its nonzero second-order term are unchanged. This explicitly aligns
the local notation with351's unique-lift convention.

EOF — notation clarified without changing weights, owner or conclusions.
