# A genuine contact complex, and what its traces do not imply

**Audit:** `ANG-AUDIT-20260921-CDC01`; **flow:** `ANG-20260921-RCF01`.  
**Batch:** `RCF01-BATCH-20260921-A`, round2/5; 2026-09-21.  
**Status:** `CONTACT COMPLEX ESTABLISHED; ORDINARY SUPERTRACE ZERO`.

## Abstract

On the complete unchanged RCF01 contact quotient, naive horizontal exterior
differentiation is not square-zero. The explicitly frozen middle-degree
correction does give a local, flow-equivariant differential complex,
on both smooth and compactly supported sections. Direct representative
arguments identify its cohomology with the corresponding de Rham cohomology.
Its actual positive-time ordinary supertrace is zero. The separately
predeclared degree-weighted trace is the ordinary orbit measure minus the
scalar flat measure, not the pure orbit measure. A genuine complex alone
therefore does not confer a Fredholm or cohomological determinant identity.

## 1. Candidate identity and same-object ledger

The [101-line P0](candidate-card.md) binds the full RCF01 source, retained
G, Q, beta, R, Phi and nu, without removing states or changing clock.
Only the classical analytic complex is new. On every full component,

```text
Phi^t(u,v,z)=(u+t,exp(t)v,exp(-t)z), nu=du dv dz;
R=partial_u+v partial_v-z partial_z;
alpha=dv-v du, eta=dz+z du;
beta=du+(v eta-z alpha)/2, Omega=d beta=alpha wedge eta.
```

The u coordinate is real on the terminal component and circular of
derived length log p on each atom component. These are348's full quotient
coordinates, not a selected section. Lineage remains the proper-divisor
word source and its contact lift. All same-flow349/350 scalar/form kernel
inputs match these equations. Strong arithmetic naturalness remains OPEN.

## 2. Question and boundary

Can350's transverse form algebra carry a genuine differential complex
with the unchanged flow? The naive differential fails; the explicitly
corrected four-degree complex succeeds. Its cochain flat traces and its
algebraic cohomology are separate constructions. No ordinary cohomology
trace, Hilbert metric, Laplacian, analytic torsion or Fredholm determinant
is silently supplied here.

## 3. Frozen definitions and attribution

Write A^q=Lambda^q ann(R), pi_H=1-beta wedge i_R, and d_H=pi_H d on
horizontal forms. The corrected bundles are
C^0=A^0, C^1=A^1, C^2=beta wedge A^1, C^3=beta wedge A^2.
Use either smooth sections everywhere or compactly supported smooth
sections, consistently through each complex. Its proposed differentials
are delta_0=d_H, delta_1 a=d(a+b beta) where pi_H d(a+b beta)=0,
and delta_2=d. The correction b must be determined, not assumed to exist.

This is the three-dimensional contact-complex construction associated
with Rumin, not a newly invented general complex. The primary attribution
is [Rumin's 1990 note](https://www.imo.universite-paris-saclay.fr/~michel.rumin/recherche/CRAS1990.pdf),
Section1, on contact-form quotients, the middle lift and differential.
That note introduces its discussion for a compact manifold. We do NOT
import compact spectral, Hodge or trace theorems to this noncompact owner;
the required claims are proved directly below. Source access/limits are
recorded in [source provenance](evidence/source-record.md).

For each C^j take its actual (Phi^(-t))* and derive Theta_C,j by the
joint positive-time kernel. The two PREDECLARED combinations are
Theta_C=sum(-1)^j Theta_C,j and Theta_W=sum(-1)^j j Theta_C,j.
Their exponential /t flat functions use the card's negative sign and
normalization1. W is just degree-weighted, not named analytic torsion.

## 4. Proof of the full complex

### C1. Naive horizontal curvature

For horizontal a, Cartan's formula gives i_R da=L_R a, hence
da=d_H a+beta wedge L_R a. For a function f, df=d_H f+(Rf)beta.
Taking d and then the horizontal projection yields

```text
d_H^2 f=-(Rf)Omega.
```

Omega never vanishes on the contact plane. A smooth local function with
Rf nonzero, multiplied by a compact cutoff equal to1 near that point,
therefore refutes d_H^2=0 even on compactly supported sections. This is
the contact nonintegrability obstruction, not an omitted sign convention.

### C2. Unique middle lift, compositions and covariance

Every horizontal two-form has a unique scalar coefficient c in c Omega.
Write d_H a=c(a)Omega. Since pi_H d(b beta)=b Omega, the unique smooth
correction is b=-c(a). It is a local first-order expression in a.
Then d(a+b beta) has zero horizontal part, so lies in beta wedge A^1.
Explicitly it equals beta wedge(L_R a-d_H b); delta_1 has order at most2.
For beta wedge gamma in C^2, d(beta wedge gamma)=-beta wedge d_H gamma
because Omega wedge gamma is a horizontal three-form and thus zero.
This belongs to C^3. All maps preserve compact supports and are global:
source/chart translations preserve beta, R and Omega.

For a=d_H f, C1 gives b=Rf. Its unique lift is df, hence
delta_1 delta_0 f=d^2 f=0. Also delta_2 delta_1 a=d^2(a+b beta)=0.
Thus both full smooth and compact-support sequences are actual complexes.

The physical flow preserves beta, R and d, so commutes with pi_H and
d_H. Uniqueness of b implies that its lift operation also commutes with
pullback. All differentials therefore intertwine the SAME physical action.
This is a genuine equivariant complex, not merely a character assignment.

### C3. Explicit de Rham comparison, with supports preserved

The following representative arguments work separately in the smooth
and compact-support domains; all corrections are local differentials.

- Degree0: d_H f=0 implies df=(Rf)beta. Its horizontal exterior derivative
  forces (Rf)Omega=0, hence df=0. Kernels agree.
- Degree1: a with delta_1 a=0 lifts uniquely to the closed de Rham form
  a-c(a)beta. Conversely any closed one-form has this unique lift from
  its horizontal part. Exact df corresponds exactly to delta_0 f.
- Degree2: any closed de Rham omega can be written c Omega+beta wedge gamma.
  Replace it by omega-d(c beta), which is in C^2, remains closed and
  differs by an exact form. If a C^2 form is de Rham exact d(a+b beta),
  its zero horizontal part forces b=-c(a), so it is delta_1-exact.
  Conversely every delta_1-exact form is de Rham exact. This also shows
  that changing the original representative changes the corrected one
  by a delta_1-exact form.
- Degree3: every top form already lies in C^3. For any two-form primitive
  omega of an exact top form, replace omega by omega-d(c beta) as above.
  Its derivative is unchanged and the new primitive lies in C^2.
  Thus the exact top-form subspaces agree.

These prove cohomology isomorphisms, with no compactness assumption or
infinite-component summation. They are natural for Phi because each
representative operation is. They do not identify smooth cohomology
with compact-support cohomology, nor assign a trace to either one.

## 5. Actual cochain traces and functions

The global C-degree frames are(1), (alpha,eta),
(beta wedge alpha,beta wedge eta), (beta wedge alpha wedge eta).
Their backward fiber characters are respectively

```text
1, exp(-t)+exp(t), exp(-t)+exp(t), 1.
```

These are actual bundle pullbacks, independent of the differential's
order. Each matrix kernel is its smooth fiber matrix times the scalar
joint kernel of349;350's rank3 restriction and finite compact-time
fixed-circle support prove every degree trace exists on the FULL Q.
Write S=Theta_0 of349 and A=Theta_orb+2S as proved in350. Then

```text
(Theta_C,0,Theta_C,1,Theta_C,2,Theta_C,3)=(S,A,A,S),
Theta_C=0,
Theta_W=-A+2A-3S=A-3S=Theta_orb-S.
```

Thus D_C=1, with its zero defining integral absolutely convergent for
all complex s. Individual degrees0,3 have exact initial domain Re s>0,
while1,2 have Re s>1. At t=k log p, put a=p^k+p^(-k)-2. The weighted
coefficient is(log p)(1-1/a). It is negative at log2 and positive at
log3, so no positive scalar interpretation is implied.

The weighted measure has exact absolute log-integral/Laplace domain
Re s>1. Sufficiency follows from349's majorants. For necessity, already
the k=1 terms with p>=3 have1-1/a>=1/4, and their reciprocal-prime
sum diverges at sigma<=1. Discarding the single exceptional p=2 term
does not alter that bound. Local uniform convergence justifies
differentiation and the factorization

```text
D_W(s)=D_orb(s)/D_0(s)=1/(zeta(s)D_0(s)), Re s>1.
```

It normalizes to1 and continues meromorphically by349's owned functions.
This is not D_orb: S is nonzero. No post-result degree weight was changed.

## 6. Controls and strongest adverse finding

The naive horizontal sequence fails by C1. The unchanged full de Rham
complex has zero positive-time supertrace by350's invariant beta factor;
the corrected contact complex now has the SAME zero, by its actual ranks
and pullbacks. A square-zero differential did not preserve the purely
transverse nonzero supertrace.

For FACTOR-OFF, all C1–C3 local arguments hold on its OWN full contact
quotient, with its empty-terminal and fixed-unit real components plus
all integer circles. Its degree traces are(S_F,A_F,A_F,S_F), where
A_F=Theta_orb,F+2S_F, so Theta_C,F=0 and
Theta_W,F=Theta_orb,F-S_F. D_W,F=D_orb,F/D_0,F on Re s>1; no global
continuation is claimed for this control. Composite primitives and
coincident lengths are all retained. This is a PROVES_TOO_MUCH warning
against attributing arithmetic selection to complex geometry.

For UNIT-HOLONOMY, all own components have real u. The same complex is
well-defined but all positive-time degree kernels have empty diagonal
support, so both traces are zero and both functions1, entirely.
Source isotropy has not been mistaken for a physical orbit. DRIFT is
not a Reeb action for beta and lies outside this explicitly Reeb-based
test; its previous undefined-degreewise result is not erased.

## 7. Gates and limitations

Full complex/covariance and explicit de Rham comparison: ESTABLISHED.
Ordinary cochain supertrace: ZERO. Degree-weighted pure-orbit identity:
FALSE for the frozen weights. Ordinary cohomology trace, Laplacian,
analytic torsion and Fredholm determinant: NOT SUPPLIED. These statements
concern owner-level T3 only. Strong naturalness OPEN; classical A0/A1/A2
NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED. No spectral/zero claim.

## 8. Decision and next round

Portfolio **advance** the genuine same-flow contact complex; **stop**
promoting its zero or degree-weighted flat traces into a cohomological
determinant. The next warranted audit asks whether the contact differential's
intrinsic order grading supplies a principled alternative flat functional,
and whether that functional has an actual cohomological interpretation on
this noncompact, countably disconnected full owner. These require a fresh
card: neither weights nor cohomology topology may be changed silently.
No further user confirmation is required before that in-scope third round.

## Evidence and integrity

[P0](candidate-card.md) · [Scope review](evidence/scope-review.md) ·
[Independent derivation](evidence/independent.md) ·
[Source provenance](evidence/source-record.md).
Exact proofs replace finite experiments; no numerical cutoff is used.
AI root/internal collaborators performed the work. No human verification,
external peer review, novelty or calibrated proof assurance is claimed.

EOF — round2 author proof; independent analysis/final review pending.

## Final terminology clarification

The original232-line analysis input is preserved. In the title status,
abstract and conclusions, "ordinary supertrace" means the standard-parity
COCHAIN FLAT supertrace Theta_C, whose construction is Section5. It never
means an ordinary Hilbert-space or cohomological operator trace. The latter
remains NOT SUPPLIED, as the question boundary and gate table require.
No mathematical formula or scope changes in this clarification.

EOF — final terminology fixed; no stronger trace assertion.
