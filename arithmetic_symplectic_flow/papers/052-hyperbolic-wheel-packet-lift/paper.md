# A hyperbolic transverse symplectic lift gives a full wheel-packet ledger but not endogenous A0

**Paper ID:** 052-hyperbolic-wheel-packet-lift  
**Candidate ID:** ASFS-20260914-HWL01  
**Date / status:** 2026-09-14; P0 FROZEN; A1 + SAME-OBJECT ZETA CONTROL ESTABLISHED; A0 SCOPED FAIL — STATIC WHEEL FAMILY DOES NOT DRIVE THE MAP  
**Route state:** A0 scoped FAIL; owner-level A1 and zeta only; formal Route A not evaluated; Route B NOT INVOKED

## Abstract

Record 033 stopped a direct disk thickening of the primorial wheel packets:
after a packet period, every point of a disk returned, so the desired finite
ledger became a continuum. This paper tests a different positive-dimensional
symplectic realization. It couples each wheel successor cycle to the hyperbolic
area-preserving map H_lambda(x,y)=(lambda x,lambda^(-1)y). H_lambda has exactly
one periodic point, the origin. The result is an exact full periodic ledger:
one primitive orbit O_k of period phi(P_k) for every wheel packet, with a
same-object unit-roof product. But this improvement exposes an independent A0
failure. F never takes the actual sieve arrow from wheel k to wheel k+1; all
wheels are simply placed side by side before the map starts. It is geometric
control, not an arithmetic suspension candidate.

## 1. Frozen same-object construction

Let P_k=p_k# and W_k=(Z/P_k Z)^times. Let R_k be the cyclic successor
permutation on W_k. Set

M = disjoint union_{k>=1} (W_k x R^2),     omega|_{W_k x R^2}=dx wedge dy.

For a fixed lambda>1 define H_lambda(x,y)=(lambda x,lambda^(-1)y) and

F(k,a,x,y)=(k,R_k(a),lambda x,lambda^(-1)y).

Each component is a symplectic plane and F permutes planes while preserving
their form, so F is a symplectic diffeomorphism of M. The positive roof is
tau=1. This is one frozen base, roof, suspension, primitive convention, and
zeta; no object is borrowed from 032, 033, or 035.

The direct lineage retained is:

prime/composite sieve -> primorial reduced-residue symbolic cycle -> wheel
successor packet -> positive-dimensional symplectic lift.

The inter-stage recursion is present only as source data, not as an action of
F; that distinction controls A0 below.

## 2. Complete periodic-orbit ledger

The cycle R_k has least period |W_k|=phi(P_k). For n>0,

H_lambda^n(x,y)=(lambda^n x,lambda^(-n)y)

equals (x,y) only at (0,0). Thus F^n(k,a,z)=(k,a,z) precisely when z=0 and n
is a multiple of phi(P_k). The points (k,a,0), as a runs through W_k, are
cyclic phase representatives of exactly one primitive orbit O_k. There are no
other periodic points.

The unit-roof suspension has primitive length phi(P_k), and the r-fold
traversal has length r phi(P_k). Unlike 033, no positive-dimensional periodic
family remains.

## 3. Same-object zeta

The full primitive ledger defines

zeta_HWL(s)=product_{k>=1}(1-exp(-s phi(P_k)))^(-1).

Since phi(P_k) is a strictly increasing sequence of positive integers and in
fact grows at least exponentially after the first stages, sum_k exp(-sigma
phi(P_k)) converges for every sigma=Re(s)>0. The Euler product therefore
converges absolutely there. This is an owner-level local analytic statement;
it has no target/divisor or formal Route-A claim.

## 4. Decisive A0 control

The source recursion in 028 reads the next sieve prime and maps from W_k to
W_(k+1). The frozen F preserves k and acts only through R_k. Consequently the
transition that carries the endogenous prime reading is never executed by the
same symplectic map. Replacing the family of wheels by any preselected family
of finite cycles of lengths N_k yields the identical symplectic construction
and a product with N_k in place of phi(P_k).

Therefore the primorial family is static input to the carrier. The construction
retains a visible prior-work deformation but fails the stronger requirement
that the base dynamics itself owns its arithmetic mechanism. Adding inter-stage
arrows would make k nonreturning, reintroducing the 018/025 obstruction.

## 5. Gate assessment

| Gate | Evidence for this exact candidate | Status | Limitation |
| --- | --- | --- | --- |
| P0 | M, omega, F, tau, orbit/repetition convention, and product frozen | frozen | disconnected noncompact control |
| A0 | F preserves k and never reads/updates the sieve state | scoped FAIL | wheel family preassembled |
| A1 | complete periodic set and repetitions exactly computed | exact positive control | periods are phi(P_k), not a prime-time mechanism |
| A2 | same-object product for Re(s)>0 | owner-level control only | no formal target/divisor evidence |
| Route B | no A0 / Route-A readiness | NOT INVOKED | prohibited |

## 6. Decision

**Stop/fork after A0.** Retain this construction as proof that the 033
continuum objection is not a universal geometric obstruction: a positive
dimensional symplectic lift can have an exact finite packet ledger. The next
candidate must solve the separate and harder issue of letting the same
recurrent symplectic map read the sieve transition, rather than merely carry
all frozen wheel packets.

## Reproducibility / evidence index

All definitions and elementary periodic-orbit calculations are in this paper.
The source wheel mechanism is [028](../../028-primorial-wheel-fibre-carrier/paper.md).
No computation, external prime table, prime logarithm, or zero data is used.

