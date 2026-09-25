# Independent contact-complex and MAIN flat-kernel audit

**Audit:** `ANG-AUDIT-20260921-CDC01`; unchanged flow `ANG-20260921-RCF01`.
**Finding:** The corrected complex is owned; the naive horizontal differential
has curvature. The prescribed C and W combinations give different functions.
**Standing:** Internal shared-model/history review; `NOT_CALIBRATED`.

## 1. Authorized input, sequence and limitations

After explicit round2 release I personally read the original351 card,
lines1–101 through EOF, and measured SHA-256
`d7106c33c7113dc3a6a55ef03fe8cdcf31eaea71b1241e63c2d1d1d5cae8ec2b`.
Scientific inputs are this card and retained same-flow348–350 context.
No source manuscripts or dependency hashes were newly inspected or remeasured.
The recently read ARS router and retained workflow/DA/runtime instructions
govern this bounded task; no venue calibration or independent-error claim is made.

I derived the formulas and explicit comparison maps below from the definitions,
then sent the parent their mathematical summary before writing this report.
No root draft, peer result, external source, numerical experiment or auxiliary
agent was used. Only this assigned evidence file was written. The parent's
scope-check release is authorization, not a mathematical result assumed here.
The card itself discloses an expectation of curvature/cancellation; this
review is neither blind nor external peer review. No new physical flow is used.

Conclusions concern MAIN on both smooth and compactly supported smooth
sections. The requested de Rham comparison is proved by explicit maps.
FACTOR-OFF and UNIT-HOLONOMY control owners remain the parent's separate task.
There is no Laplacian, Hilbert completion, quantum object, ordinary cohomology
trace or unprovided Fredholm determinant in this report.

## 2. Full horizontal curvature

On every terminal and circular component, the global frame satisfies

```text
beta(R)=1, alpha(R)=eta(R)=0, d beta=alpha wedge eta;
Omega^q=A^q direct-sum (beta wedge A^(q-1)).                (1)
```

The frame never degenerates; no zero section or exceptional hypersurface
is removed. For horizontal omega, Cartan's identity gives
d omega=d_H omega+beta wedge L_R omega. Taking d again and its horizontal
part, using i_R d beta=0, gives the exact curvature formula

```text
d_H^2 omega = -d beta wedge L_R omega.                     (2)
```

For the globally defined function f=v this is -v alpha wedge eta, not zero.
A compactly supported bump equal to v near a point with v!=0 gives the same
local obstruction on the compact-support domain. Thus the naive sequence
is not a differential complex. The zero of (2) in horizontal degrees>=1
due to rank2 does not repair the failed composition starting at functions.

## 3. The proposed correction: existence, membership and differential

For any smooth two-form theta define H(theta) by
pi_H theta=H(theta) d beta. This is a globally defined zero-order operation,
since d beta is a nowhere-vanishing horizontal two-form. Put h(a)=H(da)
for a in A^1. Then

```text
pi_H d(a+b beta)=(h(a)+b)d beta;
b=-h(a) uniquely;
delta_1 a=d(a-h(a)beta)=beta wedge (L_R a+d_H h(a));
delta_2(beta wedge a)=-h(a) beta wedge d beta.              (3)
```

These formulas prove existence, uniqueness, smoothness and membership in
the frozen C^2 and C^3. The maps have differential orders1,2,1, are local,
and never enlarge support. They therefore define maps on ALL smooth
sections and, separately, on ALL compactly supported smooth sections.

For a=d_H f=df-(Rf)beta, equation(2) says h(a)=-Rf. Its corrected lift
a-h(a)beta equals df, so delta_1 delta_0=0. Also delta_2 delta_1=0 follows
directly from d^2(a-h(a)beta)=0. Thus the exact proposed sequence is a
complex on both domains; no alternative differential has been substituted.

The actual Phi preserves beta, R and d beta. Its pullback commutes with d,
pi_H, H and the resulting maps in(3), proving covariance on the entire Q.
Completeness of the frozen flow preserves compact supports at every fixed t.

## 4. Explicit comparison with de Rham, including domains

Let J:C -> Omega be identity in degrees0, inclusion in degrees2,3, and
J_1 a=a-h(a)beta. Define P:Omega -> C by

```text
P_0=P_3=id, P_1=pi_H,
P_2 theta=theta-d(H(theta)beta).                           (4)
```

P_2 theta has zero horizontal part, so lies in C^2. For a general one-form
lambda=a+b beta, H(d lambda)=h(a)+b. Substitution gives
P_2 d lambda=d(a-h(a)beta)=delta_1 P_1 lambda;
d P_2 theta=d theta. Together with J_1 delta_0 f=df, these identities
verify that both J and P are chain maps, and P J=id_C.

Define K only in degree2 by K theta=H(theta)beta, and zero in other degrees.
On degree1, lambda-JP lambda=(h(a)+b)beta=K d lambda;
on degree2, theta-JP theta=dK theta; the other degrees give zero. Hence

```text
id_Omega-JP=dK+Kd.                                        (5)
```

All these maps are local, preserve support, and commute with Phi pullback.
Equations(4)–(5) give an explicit chain-homotopy equivalence, hence identify
the corresponding smooth cohomologies and, separately, compact-support
cohomologies. They do NOT identify these two support conventions with each
other or create a topology/ordinary trace on either cohomology space.
No general contact-complex theorem was cited in place of these checks.

## 5. Actual degree kernels on the full owner

Use the global frames 1; (alpha,eta); (beta wedge alpha,beta wedge eta);
beta wedge alpha wedge eta. For the actual backward pullback, the matrices are

```text
M_0=M_3=1, M_1=M_2=diag(e^(-t),e^t).                      (6)
```

On Q_p, L_p=log p, the joint kernel in each frame is M_j(t) times
delta_(L_p)(y_u-u+t) delta(y_v-e^(-t)v) delta(y_z-e^t z), relative to nu.
This reproduces the induced form pullback, without added amplitude.
On the joint diagonal the three equations are
t-kL_p=0, (1-e^(-t))v=0, (1-e^t)z=0. For positive time they are transverse,
with absolute determinant Delta(t)=e^t+e^(-t)-2>0 in variables(t,v,z).
Direct change of variables therefore defines every degree restriction.

Spatial integration contributes one full phase circle of length L_p,
not kL_p. On a compact positive time window only finitely many p and k
occur, and their spatial supports are compact circles at v=z=0. Thus the
noncompact/countable spatial pushforward is justified by a compact cutoff
equal to one on this support. The terminal component contributes nothing
for t>0 because its longitudinal diagonal requires t=0; it is not discarded.

Let Theta_s denote the previously owned scalar measure with coefficients
L_p w_p,k, w_p,k=p^(-k)/(1-p^(-k))^2, at kL_p. The independently computed
degree measures from(6) are

```text
Theta_C,0=Theta_C,3=Theta_s;
Theta_C,1=Theta_C,2=Theta_orb+2Theta_s.                     (7)
```

Indeed (p^k+p^(-k))w_p,k=1+2w_p,k. These are individually well-defined
positive locally finite measures before either prescribed combination.

## 6. The two frozen combinations and their functions

The fixed, separately declared C and W weights now give

```text
Theta_C=0, D_C=1;
Theta_W=Theta_C,1-3Theta_C,0=Theta_orb-Theta_s;
D_W=D_orb/D_s
   =zeta(s)^(-1) product_(m>=1) zeta(s+m)^m, Re s>1.        (8)
```

Here D_s is349's scalar flat function, not a new operator. Direct expansion
w_p,k=sum_(m>=1)m p^(-km) and absolute rearrangement reproduce its product
product_(m>=1)zeta(s+m)^(-m), so(8) follows from the present kernels as well.
No parity or weight was changed after inspecting the outcome.

For degrees0,3 the initial absolute domain of the /t integral is Re s>0;
for degrees1,2 it is Re s>1. These follow from(7), geometric bounds and
the divergent prime harmonic subseries at the corresponding boundaries.
The zero C measure has an everywhere-convergent integral. W has coefficient
L_p(1-w_p,k): it is negative only at p^k=2, where it equals -log2.
For every other prime power w_p,k<=3/4. Thus its absolute initial domain
is EXACTLY Re s>1; removing one atom cannot cure prime harmonic divergence.
Both functions tend to1 at large Re s, and
D_W'/D_W=integral e^(-st)Theta_W(dt) on that half-plane.

Using the retained standard meromorphic continuation of zeta, D_W continues
meromorphically to C. For each compact set, sufficiently large m satisfy
|zeta(s+m)-1|<=C 2^(-m); hence sum m log zeta(s+m) converges uniformly
for the tail. Its exponential is holomorphic and nowhere zero; the finite
head is meromorphic. This proves the product implication without a new
classical-zeta proof or personal claim to have checked an external source.
It does not extend the defining integral's absolute domain or grant a
Fredholm interpretation. Zeros/poles of finite factors may cancel.

## 7. Adverse check and exact remaining boundary

Curvature genuinely defeats the naive differential, but not the frozen
corrected complex: uniqueness, locality, chain maps and covariance were
proved on both full section domains. Conversely, a legitimate complex does
not turn its flat traces into ordinary traces on cohomology. The standard
alternating combination is zero, while the predeclared degree weighting
leaves a scalar correction; neither may be renamed analytic torsion.
For example W's coefficient at log3 is (log3)/4, not the unit orbit weight.
This is a concrete owner-level distinction, not a failure of the complex.
All transverse points, terminal components and source clocks remain fixed.
Strong naturalness, Hilbert/quantum refinements and formal Route statements
remain outside the proved scope. No extra control or changed owner is audited.

EOF — bounded MAIN complex/kernel derivation and adverse check complete.
