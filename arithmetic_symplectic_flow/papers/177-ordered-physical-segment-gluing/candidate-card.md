# Frozen physical-segment composition card

**Candidate ID:** ALF-20260915-PSG01  
**Paper ID:** 177-ordered-physical-segment-gluing  
**Version:** 1, frozen 2026-09-15 before this candidate's proofs.  
**Status:** ADVANCE — COMPLETE PHYSICAL RETURN-BLOCK COMPOSITION; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

This is the G lane in the [180 scope](../180-constructive-coupling-frontier/candidate-card.md).
The selected input is the full return-block transport construction, not
the preliminary centre-oval-only proposal. All assertions about validity
below were proof obligations at this freeze, not inherited results.
The initial frozen workflow state was FROZEN — FULL RETURN-BLOCK
TRANSPORT AND SEAMS UNDER AUDIT. The final status records the subsequent
proofs in [paper.md](paper.md), without changing any defining input.

## 1. Full source and carrier category

For positive rationals write x <=_D z when z/x is a positive integer,
and x prec z for a strict cover in that order. Let Y contain every
bilateral normalized chain y_0=1, y_j prec y_(j+1), whose ratios
a_j=y_(j+1)/y_j are weakly nondecreasing in the ordinary numerical order.
Use discrete rational coordinates and the product-subspace topology.
F(y)_j=y_(j+1)/y_1. No chain or negative-time history is removed.

The source is the precise admissibility deformation of the
[163 source](../163-ordered-cover-scale-suspension/paper.md).
Its lineage is divisor indecomposability -> symbolic cover admissibility
-> genuine sequential physical segments -> conservative section geometry.
No claim of a chronological primality enumerator or a Logistic/Henon
conjugacy is supplied. Source topology must not be replaced by a discrete
topology or assumed locally compact.

The candidate category is a topological-transverse, smooth-leafwise,
event-glued physical flow with a two-dimensional symplectic return base.
It is not declared a classical finite-dimensional manifold, standard
locally compact lamination, global Hamiltonian energy surface, or contact
flow. Those classical fields are NOT APPLICABLE / NOT SUPPLIED here.

## 2. Uniform section transport, fixed before proof

For every integer n>=2, put c_n=1+n^-2 and
W(q)=4q^2/(1+q^2)^2. On the reference section use all
U*={(Q,P) in R^2: -1<QP<1}, with area dQ wedge dP.
The physical section domain is all U_n={-n^-2<QP<1}.
These entire open strips, not selected axes or centres, are the contract.
Points outside them are not silently claimed as part of this owner.

Fix eta(t)=exp(-1/t) for t>0 and zero otherwise, and
chi(t)=eta(t)/(eta(t)+eta(1-t)). For all n use exactly

    delta_n = 1/(4 n^2),       epsilon_n = 5/(8 n^2-3),
    g_n(u) = epsilon_n + (1-epsilon_n) chi((u+2 delta_n)/delta_n),
    f_n(I) = integral from 0 to I of g_n(u) du.

The obligations are that f_n maps (-1,1) smoothly increasingly onto
(-n^-2,1), and equals I near zero. On Q!=0, set I=QP and define

    Q' = sign(Q) exp(log(abs(Q))/f_n'(I)),
    P' = f_n(I)/Q',            S_n(Q,P) = (Q',P').

At Q=0 define S_n(0,P)=(0,P). Prove this is a global smooth
symplectomorphism U* -> U_n, including both axes and all quadrants.
No parameter, cutoff or function may be retuned after the audit.

## 3. Declared physical blocks, not the full old energy surface

For each n use the actual equations of the Hamiltonian building block

    H_n(q,p,Q,P) = p^2/2 + c_n W(q) + QP,
    Omega = dq wedge dp + dQ wedge dP,
    qdot=p, pdot=-c_n W'(q), Qdot=Q, Pdot=-P.

The building block is its entire inner return-saturation on H_n=1:
0<E=p^2/2+c_n W(q)<c_n and abs(q)<1, with all compatible Q,P.
Cut this saturation at q=0,p>0. Its entrance map is
iota_n(Q,P)=(0,sqrt(2(1-QP)),Q,P), on every point of U_n.
The physical segment runs from this entrance to its first same-oriented
return. Write A_n(E) in (0,1) for c_n W(A_n(E))=E and freeze

    T_n(E) = 4 integral_0^A_n(E) dq/sqrt(2(E-c_n W(q))),
    t_n(w) = T_n(1-QP),
    R_n(Q,P) = (exp(t_n) Q, exp(-t_n) P).

These are proposed actual return quantities to be proved from the displayed
equations. They agree as building-block formulas with the zero-witness
well in [171](../171-separatrix-witness-hamiltonian-clock/paper.md),
but 171's complete energy carrier and its composite exclusion are not
imported. All n are used for the uniform design rule; which n occur in
this candidate is determined by the cover source itself.

## 4. Complete seam and flow owner

Over y, put n=a_0(y), b=a_1(y), and include each physical segment
starting from iota_n(S_n z), for every z in U*. At its physical endpoint
w_end=R_n S_n z in the outgoing section, reset to the next entrance

    (y, iota_n(w_end)) -> (Fy, iota_b(S_b S_n^-1 w_end)).

Thus the whole physical section is transported, including its scalar
entrance momentum; this is not the identity between unequal U_n.
The inverse must use F^-1 and the inverse section transport, with all
negative-time states retained. No elapsed time is added at a seam.

The proposed derived base and actual elapsed roof are

    B(y,z) = (Fy, S_n^-1 R_n S_n z),
    tau(y,z) = t_n(S_n z).

Construct the physical quotient first with both cut faces present and the
displayed seam. Its equivalent elapsed-coordinate quotient is
{(y,z,u):0<=u<=tau(y,z)}/((y,z,tau)~(B(y,z),0)).
Use the induced physical flow-box topology and smooth leaf charts,
not a half-open interval as a gluing space. Prove Hausdorffness, local
flow charts, continuity, leafwise smoothness, positive roof and two-sided
non-Zeno completeness. Preserve physical time without rescaling.

The section has leafwise area dQ wedge dP; section-time volume is the
only proposed invariant leafwise volume. No transverse measure or finite
probability measure is chosen. A global Hamiltonian across event resets
is NOT SUPPLIED; a global time-coordinate simplification, if present,
must be disclosed rather than called irreducible feedback.

## 5. Output obligations and stops

Classify every actual closed orbit in the full quotient, not only
invariant-axis solutions. Primitive means least positive return of the
oriented flow, counted modulo time phase; positive repeats belong to the
same orbit. Derive all multiplicities, least periods and transverse
Poincare monodromy. The anticipated logarithmic-size period is an
obligation from the integral, not an assigned roof or exact log n claim.

The optional sole analytic object is the ordinary unweighted full-orbit
product Z(s)=product_gamma (1-exp(-s T_gamma))^-1, with its positive
repeat logarithm. Its region must be proved. Operator, trace, Fredholm
determinant, continuation, zeros and quantum owner are NOT SUPPLIED.
No operator from 169, 171, 174 or a concurrent lane is borrowed.

Stop on a failed whole-strip transport, invalid seam/inverse, finite-time
accumulation, lost histories, or unaccounted continuous/composite periodic
families. Controls include identity-seam failure, removal of ordering,
removal of cover indecomposability, transverse identity dynamics, and
changing the barrier rule. These are separate comparisons, not repairs.

The construction is deliberate engineering. Arithmetic-source naturalness,
uniqueness of the rule and a stronger global geometric realization remain
OPEN even if all local owner-level claims succeed. A successful explicit
composition is not, by itself, a natural A0 or formal Route pass.
