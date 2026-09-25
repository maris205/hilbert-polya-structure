# Independent contact-order, cohomology and trace audit

**Audit:** `ANG-AUDIT-20260921-COG01`; same flow `ANG-20260921-RCF01`.
**Finding:** Intrinsic order weighting gives twice the orbit measure;
full compact-support cohomology carries an identity action, not a trace-class
realization of the positive-time flat measure.
**Standing:** Internal inherited-model/shared-history; `NOT_CALIBRATED`.

## 1. Inputs and sequence

After the explicit round3 release I personally read original352 card lines1–88
through EOF and measured SHA-256
`7335c5cbffe9e3f09e7ba63154b6a565478a7a597dc29c1377e7f35ac3bb1048`.
Scientific inputs are that card and my retained same-flow348–351 work.
No earlier manuscript or quoted dependency lock was newly opened or verified.
The already-read ARS router/workflow/DA/runtime instructions remain applicable.
I derived all results below and sent the parent a mathematical summary before
writing this sole authorized file. No root draft, peer answer, external source,
numerical experiment, auxiliary agent, model change or other file write was used.

The card discloses expectations about order weights and flow isotopy, and
the execution inherits extensive context. It is not blind, cross-model,
external peer review or independent-error evidence. This report covers MAIN,
the algebraic weighting controls and the finite-component control only.
Full FACTOR-OFF/UNIT-HOLONOMY audits are not performed here. No new physical
flow, Hilbert structure on cochains, quantum owner or formal Route claim is added.

## 2. Contact filtration and actual differential orders

Use a LOCAL real lift of u on each circular component and put
X=e^(-u)v, Y=e^u z, tau=u-XY/2. Direct substitution gives

```text
beta=d tau+X dY, R=partial_tau;
A=partial_X, B=partial_Y-X partial_tau, [A,B]=-R.           (1)
```

This is only a coordinate check, not a change of physical flow or its clock.
The horizontal covectors dX,dY have filtration weight1; beta has weight2.
The contact tangent filtration assigns A,B order1 and R order2. Its local
dilation scales (X,Y,tau) by (lambda,lambda,lambda^2); contact changes of frame
preserve the underlying horizontal/contact filtration. Thus the frozen
bundles C^0,A^1,beta wedge A^1,beta wedge A^2 have grades(0,1,3,4).

For a=a_1 dX+a_2 dY, set h=Aa_2-Ba_1. The actual differentials become

```text
delta_0 f=(Af)dX+(Bf)dY;
delta_1 a=beta wedge [(Ra_1+Ah)dX+(Ra_2+Bh)dY];
delta_2(beta wedge a)=-h beta wedge dX wedge dY.            (2)
```

They have contact orders1,2,1, respectively, agreeing with the successive
grade differences. The second-order term is real, e.g. a_2 varying
quadratically in X gives the nonzero AAa_2 term. This proves compatibility
of the proposed grading, not a freely fitted list of time weights.
It does not grant an overall factor1/2 or select the arithmetic components.

## 3. Actual order-weighted flat function

Retain the actual degree kernels proved in351: their backward fiber matrices
are 1, diag(e^(-t),e^t), diag(e^(-t),e^t),1. The common scalar diagonal has
denominator Delta(t)=e^t+e^(-t)-2 and full phase integral L_p=log p.
The joint restriction is transverse for positive t; over a compact time
window its support is finitely many compact circles. Thus the full spatial
pushforward is already justified on every degree, including the noncompact
and countable-component boundary, before any new weighting is applied.

Write S for the scalar measure with coefficients L_p w_p,k at kL_p,
w_p,k=p^(-k)/(1-p^(-k))^2, and O=Theta_orb. The four degree measures are
(S,O+2S,O+2S,S). Therefore the UNNORMALIZED frozen grading gives

```text
Theta_ord=-(O+2S)+3(O+2S)-4S=2O;
D_ord(s)=exp[-2 sum_(p,k>=1)p^(-ks)/k]
        =D_orb(s)^2=zeta(s)^(-2), Re s>1.                  (3)
```

Absolute convergence is exact for Re s>1, by geometric-series bounds and
the divergent k=1 prime harmonic subseries at the boundary. Normalization
to1 at large Re s is inherited from this convergent defining series, not
chosen afterward. The retained standard meromorphic continuation of zeta
gives the meromorphic continuation of(3). No new external verification or
proof of that classical property is claimed here; continuation does not
alter the defining integral's absolute domain.

For arbitrary constant degree weights c=(c_0,c_1,c_2,c_3), direct algebra gives

```text
A=c_2-c_1, B=c_0-c_3+2A;
Theta_c=A O+B S, D_c=D_orb^A D_scalar^B                 (initial domain).
```

If A!=0 the exact absolute half-plane is Re s>1; if A=0,B!=0 it is Re s>0;
if A=B=0 the zero-measure integral converges everywhere. The assertions follow
also for complex constants from |A+B w_p,k| bounded below for large p^k.
Noninteger powers here mean the normalized defining exponential, not an
unproved single-valued meromorphic extension. Ordinary degree weights give
O-S; full parity gives0; order weights give2O. These controls are not tuning.

Taking half the logarithm of(3) would algebraically give D_orb on the initial
half-plane, but it is NOT the frozen functional. A torsion interpretation
would require its own normalization and analytic owner, including operator
domains and legitimate determinant/trace or regularization data in this
noncompact/countable setting. No such structure follows from the grading.

## 4. Explicit compact real-fiber homotopy

The351 chain maps between C and de Rham preserve both smooth and compact
support domains. Thus their corresponding cohomologies may be computed with
de Rham forms, but representatives must be returned by the actual map P.
Here is the needed compact-support computation without a Hodge theorem.

On M x R_x write a compactly supported k-form as omega=a(x)+dx wedge b(x).
Fix rho in C_c^infinity(R) with integral1 and F(x)=integral_(-infinity)^x rho.
Define

```text
I omega=integral_R b(x)dx,     J theta=rho(x)dx wedge theta;
K omega=integral_(-infinity)^x b(t)dt-F(x)I omega.            (4)
```

K is horizontal in x. Its two constant tails cancel, so its support is
compact, as are the supports of I and J on their respective spaces.
Since d omega=d_M a+dx wedge (partial_x a-d_M b), direct differentiation gives

```text
I d=-d_M I, d J=-J d_M, I J=id, dK+Kd=id-JI.               (5)
```

The minus sign is the shifted-complex differential, not a lost orientation.
These explicit formulas prove H_c^k(M x R)=H_c^(k-1)(M). Repeating them
twice over a circle and three times over a point determines every needed
component group. Compactness of each form gives uniform support bounds in
the integration coordinate; no convergence at infinity has been assumed.

## 5. Entire smooth and compact-support cohomology

Smooth contraction of the R^2 fibers onto zero is given by
(u,v,z)->(u,tv,tz), 0<=t<=1; integration of the dt coefficient of its pullback
is the usual explicit homotopy identity. On R^3 use radial contraction.
On a circle, a one-form minus its normalized integral has a periodic
primitive; closed functions are constants. Thus a terminal component has
smooth H^0=C only, and each circle component has smooth H^0=H^1=C only.
Smooth sections on the coproduct form a PRODUCT, giving

```text
H^0(C_smooth)=product_({terminal} union primes) C;
H^1(C_smooth)=product_primes C; higher groups=0.             (6)
```

Compact subsets meet only finitely many open components. Equations(4)–(5)
give a terminal H_c^3=C and, on each circle x R^2, H_c^2=H_c^3=C only.
Consequently

```text
H^2(C_c)=direct-sum_primes C;
H^3(C_c)=C_terminal direct-sum direct-sum_primes C;
H^0(C_c)=H^1(C_c)=0.                                      (7)
```

Explicit normalized de Rham generators on a circle component are 1,du/L_p
for smooth cohomology, and rho(v)rho(z)dv wedge dz and
(du/L_p) wedge rho(v)rho(z)dv wedge dz for compact degrees2,3.
The terminal compact generator is rho(u)rho(v)rho(z)du wedge dv wedge dz.
Use351's P_1=pi_H and P_2 theta=theta-d(H(theta)beta), where
pi_H theta=H(theta)d beta, to obtain actual C representatives. A de Rham
two-form is not silently asserted to belong to C^2 before this projection.
There is no product-to-direct-sum identification between(6) and(7).

## 6. Induced flow and the specified Hilbert owner

For de Rham forms the actual flow gives the explicit homotopy
A_t omega=integral_0^t (Phi^s)* i_R omega ds, with
(Phi^t)*-id=dA_t+A_t d. It is valid for negative t as an oriented integral.
For compact support the union of the transported support over a bounded
s interval is compact, as a continuous image of a compact product. Thus it
is a homotopy on BOTH domains. Conjugating by351's equivariant chain maps
P,J gives the corresponding identity on C. Every induced cohomology action
of the frozen backward flow is therefore the identity for EVERY real t.

With exactly the card's orthonormal component generators, its completion is

```text
K_c^2=ell^2(primes), K_c^3=C direct-sum ell^2(primes);
K_c^0=K_c^1=0.                                           (8)
```

The induced operators on degrees2,3 are the identity on infinite-dimensional
Hilbert spaces. An infinite orthonormal sequence proves they are not compact
and hence not trace class. Degrees0,1 are zero spaces, with zero trace.
No trace on the infinite product spaces(6) was furnished by this card.
Neither infinite-dimensional identity encodes the physical period log p:
cohomological fixedness for every t is not a closed physical orbit.

## 7. Finite-component control and final adverse boundary

Retain the terminal component plus N atom components. Compact cohomology has
dimensions dim H_c^2=N and dim H_c^3=N+1. The induced identity gives
parity trace -1, ordinary-degree weighted trace -N-3, and order-weighted
trace 3N-4(N+1)=-N-4. Each is independent of t and of all component lengths.
More generally the constant-weight trace is c_2 N-c_3(N+1).
For comparison, finite smooth cohomology has dimensions(N+1,N) in degrees0,1,
so its parity trace is1 and order-weighted trace is -N. These are legitimate
finite-dimensional algebraic traces, not the infinite owner in(8).

The finite flat order measure is instead the atomic measure
2 sum_(p retained,k>=1) L_p delta_(kL_p), with actual time information.
Even before taking an infinite union, the time-independent cohomology trace
does not equal this distribution. The constant finite parity value -1
cannot be used to define a difference of two divergent infinite traces.
No cutoff subtraction or determinant regularization was authorized.

The strongest positive result survives: the contact filtration naturally
supplies the tested integer weights and a precisely owned flat function.
Its factor2 is not removed by convention. The strongest proposed bridge to
ordinary full-cohomology traces fails both trace-class and time-information
tests, while the cohomology identification itself remains valid. Strong
naturalness, torsion, quantum and formal Route claims remain unproved.

EOF — bounded MAIN order/cohomology and finite-component audit complete.
