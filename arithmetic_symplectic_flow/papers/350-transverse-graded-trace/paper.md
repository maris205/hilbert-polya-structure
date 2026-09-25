# The owned transverse supertrace and its fixed sign

**Audit:** `ANG-AUDIT-20260921-TGT01`; **flow:** `ANG-20260921-RCF01`.  
**Batch:** `RCF01-BATCH-20260921-A`, round1/5; 2026-09-21.  
**Status:** `SIGNED GRADED FLAT IDENTITY ESTABLISHED; COHOMOLOGICAL OWNER OPEN`.

## Abstract

The unchanged RCF01 Reeb flow acts on its actual transverse exterior
algebra. Its positive-time supertrace equals MINUS the ordinary length
measure. With the frozen exponential convention its graded flat-determinant
function is therefore the ordinary orbit zeta, not its reciprocal. The
sign is derived from the return matrix and is not repaired. The full
cotangent supertrace instead vanishes. Individual full-L2 transverse
operators are bounded and invertible but never trace class. This is an
owned signed flat identity, not a cohomological or Fredholm realization.

## 1. Candidate identity and same-object ledger

The [100-line P0](candidate-card.md) freezes the new analytic owner and
restates the complete source, G, Q, beta, Phi and nu. The physical owner
is unchanged348, with349 supplying the verified scalar joint kernel and
ordinary orbit zeta. Their exact proof locks are in the card; root measured
both before analysis. The full quotient is

```text
Q=R^3 disjoint-union coproduct_(p atom) (R/(log p)Z)xR^2,
Phi^t(u,v,z)=(u+t,exp(t)v,exp(-t)z), nu=du dv dz,
beta=(1+vz)du+(v dz-z dv)/2, R=partial_u+v partial_v-z partial_z.
```

The prime-symbolic lineage and ALL states/incoming arrows remain. No new
roof, prime table, selected periodic subsystem or physical time is used.
Classical symplectic-base/roof fields are NOT APPLICABLE. Quantum ownership
is not proposed. Strong arithmetic naturalness remains OPEN.

## 2. Question and boundary

Does the ACTUAL induced action on transverse forms remove the scalar
Jacobian, with the predetermined exterior parity? Yes, with a minus sign.
Does this establish an ordinary trace-class determinant or a differential
complex? No. Neither is implied by an exterior algebra or its signed trace.

## 3. Definitions and provenance

Let B_q=Lambda^q ann(R), q=0,1,2, with frame
alpha=dv-v du, eta=dz+z du orthonormal, and H_q=L2(Q,nu;B_q).
The operator U_t^(q) is the actual (Phi^(-t))* on full compactly supported
smooth sections, subsequently extended when bounded. Each Theta_q is
obtained by diagonal restriction of its JOINT kernel, fiber trace and
integration over the full spatial owner, all at t>0.

Freeze Theta_perp=Theta_0-Theta_1+Theta_2 and
D_perp=exp(-integral exp(-s t)Theta_perp(dt)/t). No parity reversal.
The ordinary Theta_orb, Z_orb=zeta and scalar D_0 are precisely349's
objects, not imported operators. Classical zeta continuation is the
previously verified [DLMF25.2](https://dlmf.nist.gov/25.2) property; no
other external trace theorem is invoked. New facts below are direct proofs.

## 4. Proof

### G1. Full bundle and bounded operator

Beta(R)=1, so TQ=span(R) direct-sum ker beta everywhere, including vz=-1.
Restriction identifies ann(R) with (ker beta)* without discarding any
fiber. Alpha(R)=eta(R)=0, and (du,alpha,eta) is a coframe of determinant1.
All are global on circular as well as real-u charts. Source arrows are
translations of u and preserve these forms. The bundles therefore belong
to the FULL quotient, not only its closed circles.

Direct pullback gives

```text
(Phi^(-t))*alpha=exp(-t)alpha,
(Phi^(-t))*eta=exp(t)eta,
(Phi^(-t))*beta=beta.
```

Thus ann(R) is invariant. In the frozen frame the fiber matrices are
A_0=1, A_1=diag(exp(-t),exp(t)), A_2=1, times the scalar base pullback.
Volume preservation makes the scalar part unitary. Consequently U^(0),
U^(2) have norm1, while U^(1) has norm exp(abs(t)); their inverses are
U^q_(-t). Each H_q is infinite dimensional, so a bounded invertible
operator on it cannot be compact: otherwise its bounded inverse would
make the identity compact. None is trace class, at any real time.

### G2. Joint kernels and the sign

The actual matrix kernel is A_q(t) times349's scalar kernel, since
integration against a section gives exactly the displayed form pullback.
Near t=kL_p its diagonal constraints remain
(t-kL_p,(1-exp(-t))v,(1-exp(t))z). The derivative in(t,v,z) has rank3.
Multiplication by the smooth finite-dimensional A_q does not alter the
well-defined delta pullback. For every compact positive-time window,
only finitely many p^k occur and the restricted spatial support is a
finite union of compact phase circles. The full pushforward is proper
on this support. No fixed-time ordinary trace has been assumed.

Put x=p^k and a=x+x^(-1)-2>0. Fiber traces and integration over the
primitive phase circle of length L_p, not kL_p, give

```text
Theta_0=Theta_2=sum_(p,k) L_p/a delta_(kL_p),
Theta_1=sum_(p,k) L_p(x+x^(-1))/a delta_(kL_p),
Theta_perp=sum_(p,k) L_p(2-x-x^(-1))/a delta_(kL_p)
          =-Theta_orb.
```

The numerator is det(I-diag(x^(-1),x))=-a. The inverse absolute
Jacobian in the scalar kernel cancels its MAGNITUDE, not its sign.
This is actual exterior linear algebra, not an inserted compensating
weight. In particular Theta_perp({log2})=-log2; the frozen parity
does not give +Theta_orb.

### G3. Exact analytic domains and function identity

Theta_0 and Theta_2 have the previously proved absolute Laplace/log-
integral domain Re s>0. Since x+x^(-1)=a+2,

```text
Theta_1=Theta_orb+2Theta_0.
```

Its positive measure has exact absolute domain Re s>1; necessity follows
from the divergent prime reciprocal sum at the boundary, already proved
in349. Theta_perp=-Theta_orb has the same total-variation domain. All
local uniform convergence and differentiation estimates are those of
these exact owned measures; no cancellation outside a convergence region
is used to define an ordinary trace.

With D_q=exp(-integral exp(-s t)Theta_q(dt)/t), on Re s>1,

```text
D_2=D_0, D_1=D_orb D_0^2,
D_perp=D_0 D_2/D_1=1/D_orb=Z_orb=zeta.
```

All normalize to1 at large real part. Each continues meromorphically
using349's proved D_0 and the verified classical zeta continuation;
the displayed quotient is interpreted meromorphically at shared zeros
or poles. It is a flat-function factorization, not a Fredholm theorem.
No extra normalization or reversal of standard degree parity occurs.

## 5. Results

The same full flow owns a signed transverse flat trace whose determinant
FUNCTION is exactly its ordinary orbit zeta. The scalar mismatch in349
remains valid. This new analytic owner supplies more than a scalar
counting identity, but less than an ordinary trace or cohomological
determinant. In particular no differential with square zero has yet been
specified on these transverse sections.

## 6. Controls and adverse findings

The FULL cotangent bundle splits as span(beta) plus ann(R), with beta
fixed. For every positive-time kernel the exterior trace polynomial is
(1+y)(1+exp(-t)y)(1+exp(t)y). At y=-1 it vanishes. All four individual
diagonal restrictions exist by G2, so their genuine full-cotangent
supertrace is zero, and its flat function is1. Removing the invariant
flow direction is therefore mathematically substantive, not harmless
notation. No additional control Hilbert metric or ordinary norm claim
is inferred beyond the P0's prescribed kernel comparison.

FACTOR-OFF has its own two real-u components (empty-terminal and fixed
singleton-1 basin), plus one log n circle component for EACH n>=2.
Its own alpha,eta pullbacks give the same numerator -a(n,k). Thus its
transverse supertrace is minus its complete INTEGER length measure and
D_perp,F=Z_F=product_(n>=2)(1-n^(-s))^(-1) on Re s>1. Composite
primitives and length collisions remain: at log4 both n=4,k=1 and
n=2,k=2 contribute. Grading does not select primes.

UNIT-HOLONOMY has only real-u components and no positive-time kernel
intersection with the diagonal. Every degree trace and supertrace is
zero; D_perp,U=1. Its retained source lag is not physical periodicity.

DRIFT-ONLY uses its OWN V=partial_u and ann(V)=span(dv,dz). The induced
fiber action is identity, but its base diagonal constraints have rank1,
not3. Each degree contains the transverse identity delta; pairing a
positive local mollification with a compact test diverges as epsilon^(-2),
times the nonzero rank1,2,1. Under the frozen degreewise definition the
Theta_q are undefined, hence Theta_perp and D_perp are undefined.
One could instead sum fiber traces of kernels BEFORE restriction and
obtain zero from1-2+1; that is a different prescription and cannot assign
values to the undefined individual traces required by this card.

The strongest PROVES_TOO_MUCH test is FACTOR-OFF: the same grading
recovers an integer-primitive zeta just as readily. The arithmetic source,
not exterior algebra, selects primes. Strong naturalness stays OPEN.

## 7. Gate assessment

Owner-level T3 bundle/kernel/signed-function claims are ESTABLISHED.
Positive-sign equality under the frozen parity is FALSE. Ordinary trace
class is FALSE for each specified H_q. A differential/cohomological owner
is OPEN, not supplied by this paper. Classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. No quantum or zero-location claim.

## 8. Decision and next round

Portfolio **advance** the owned signed graded flat identity, **stop**
its promotion to an ordinary or cohomological Fredholm determinant.
The decisive remaining issue is whether the transverse forms form a
genuine flow-equivariant differential complex, rather than merely an
exterior bundle. The next warranted round is to audit the naive horizontal
differential and a precisely defined contact-corrected complex if needed,
including the resulting degree traces. A new analytic P0 must come first.
This is within the user's five-round authority, not an invitation to alter
this frozen parity or quietly count a new complex as the same operator.

## Evidence and integrity

- [Frozen card](candidate-card.md), [batch record](batch-log.md).
- [Scope/analysis/final review](evidence/review.md).
- [Independent MAIN calculation](evidence/independent.md).

All displayed results are exact symbolic arguments, not finite experiments.
Root and internal AI collaborators performed the work; no human proof
verification, external peer review, blind/cross-model independence or
calibrated assurance is claimed. No new source search supports novelty.

EOF — round1 author proof; checkpoint2 and final surfaces to be reviewed.
