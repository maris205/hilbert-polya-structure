# Frozen candidate card — ALF-20260918-FDC01

**Paper ID:** 220-finite-defect-cover-flow  
**Candidate ID:** ALF-20260918-FDC01  
**Date:** 2026-09-18  
**Version:** 1; frozen before theorem claims or computations.  
**Status at freeze:** FROZEN — FINITE-DEFECT PERIODICITY, SCALE-QUOTIENT, AND TOPOLOGY AUDIT PENDING.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Exact carrier and action

Let \(\mathbb P\) be the positive prime integers.  For positive rationals,
write \(x\prec_{\rm cov}z\) when \(z/x\) is a prime (equivalently, when
\(x<_{D}z\) is a cover in the positive-rational divisibility order).  Freeze
the normalized two-sided cover-chain carrier

\[
X_{\rm fd}=\left\{y\in(\mathbb Q_{>0})^{\mathbb Z}:y_0=1,\quad
 a_j(y):=\frac{y_{j+1}}{y_j}\in\mathbb P\ \text{for every }j,\quad
 \operatorname{TV}(a(y)):=\sum_{j\in\mathbb Z}|a_{j+1}(y)-a_j(y)|<\infty\right\}.
\]

Thus the admissibility rule is finite total variation, equivalently a finite
domain-wall energy on the prime cover-ratio word.  It allows arbitrary finite
nonmonotone walls and does not impose the numerical order used by Candidate
ANG-20260915-OCS01 (163).  Define

\[
 F_{\rm fd}(y)_j=\frac{y_{j+1}}{y_1},\qquad
 G_{\rm fd}(y,r)=\left(F_{\rm fd}y,\frac r{y_1}\right),
\]

on \(X_{\rm fd}\times\mathbb R_{>0}\), with the full integer action generated
by \(G_{\rm fd}\).  The proposed same-object scale quotient and flow are

\[
 Q_{\rm fd}=(X_{\rm fd}\times\mathbb R_{>0})/\langle G_{\rm fd}\rangle,
 \qquad
 \Phi_{\rm fd}^{t}[y,r]=[y,e^t r].
\]

The proposed section is \(r=1\), and the proposed return roof is
\(\tau(y)=\log y_1\).  These are audit obligations of this candidate, not
transferred facts from 163.

## Frozen field contract

| Field | Frozen scope and owner |
| --- | --- |
| Carrier type | Arithmetic laminated / symbolic scale quotient with a finite-defect transverse carrier; standard finite-dimensional symplectic fields are `NOT APPLICABLE` at freeze. |
| Phase space and symplectic map | `NOT APPLICABLE`; no positive-dimensional symplectic lift is silently assumed. |
| Arithmetic input | Positive rationals, the divisibility cover relation, prime cover ratios, and the endogenous finite-variation/domain-wall admissibility rule. No prime table, per-prime parameter, von Mangoldt weight, or zero data. |
| Prior-work lineage | Prime/composite divisor observable -> cover-atom symbolic coding -> finite-defect deformation retaining arbitrary walls -> scale quotient. This is a new admissibility carrier, not a generic arithmetic space. |
| Evolution | The shift-normalization \(F_{\rm fd}\) and its scale cocycle \(y_1\), owned by this card. |
| Clock | Universal multiplicative scale law \(r\mapsto e^t r\), with proposed return time \(\log y_1\); arithmetic naturalness is `OPEN`. |
| Closed packets | All intrinsic primitive oriented closed \(\Phi_{\rm fd}\)-orbits of the full finite-defect carrier, including every admissible wall state; no centres or selected sector may be discarded. |
| Repetitions | Positive integer traversals of each actual primitive orbit, with time exactly multiplied by the traversal number if the quotient calculation supports it. |
| Symbolic owner | The prime cover-ratio word \(a(y)\), with finite total variation as the sole new admissibility condition. |
| Analytic owner | `OPEN`; if the complete orbit ledger is obtained, an ordinary orbit product may be defined only for this quotient and its actual roof. No operator or determinant is borrowed. |
| Topology | Product-subspace topology inherited from \((\mathbb Q_{>0})^{\mathbb Z}\) with discrete coordinate topology; local compactness and Hausdorff quotient properties are explicit audit obligations. |
| Hamiltonian/contact/quantum lift | `DEFERRED`; no such lift is implied by this card. |
| Owner-level labels | T0--T3 only if the broadened-carrier audit is later justified; formal Route coordinates remain `UNASSIGNED`, and Route B is `NOT INVOKED`. |

## Distinction from prior candidates

Candidate 163 uses weak numerical monotonicity
\(a_j\leq a_{j+1}\), which removes every nonconstant two-sided periodic
word before the scale quotient is studied.  Candidate 220 instead retains all
finite nonmonotone walls, including words such as
\(\ldots,2,3,5,3,2,\ldots\) when they have finite total variation, and uses
the global energy bound as the only carrier restriction.  No theorem, topology,
clock, or orbit statement from 163 is inherited.  Candidate 169's leafwise
symplectic thickening is likewise a separate control, not part of this object.

## Precommitted discriminators and controls

1. Prove that \(\operatorname{TV}(a)<\infty\) gives only finitely many
   domain walls and permits arbitrary finite nonmonotone wall patterns.
2. Prove shift invariance and invertibility of \(F_{\rm fd}\), including both
   directions, before discussing any periodic packet.
3. Prove or refute the periodic-rigidity statement: every periodic finite-
   variation prime word is constant, hence has one prime label.
4. Derive the full scale quotient, its section, first-return roof, non-Zeno
   completeness and all primitive/repeated packets from \(G_{\rm fd}\); no
   symbolic return formula alone is sufficient.
5. Classify the product-subspace topology, local compactness, and quotient
   Hausdorffness.  A hidden collapse of far-away walls is an ownership failure.
6. Compare the finite-defect carrier with (a) the monotone 163 carrier, (b)
   the unrestricted all-word cover carrier, and (c) a fixed wall-count carrier.
   These are controls with separate owners, not parameter tuning of 220.
7. Remove the prime-cover condition while retaining finite variation as a
   composite-increment control; any surviving packets are a `PROVES_TOO_MUCH`
   warning, not positive evidence.
8. Replace \(e^t\) by \(e^{ct}\), \(c>0\), only as a universal changed-clock
   control.  Per-prime clocks, hand-inserted \(\log p\), prime tables and
   target-zero fitting are forbidden.
9. If a finite-segment approximation is used, record that it may introduce a
   full finite shift and cannot certify the two-sided carrier or its intrinsic
   packet multiplicity.

## Stop/fork contract

Stop before the owner-level T0/T1/T2 audit if the finite-defect rule is not shift-invariant, if the
quotient is not a well-defined same-object flow, or if finite walls create
extra primitive packets not owned by the stated carrier.  Fork rather than
altering the energy, scale cocycle, topology, or orbit convention in place.
If the periodic ledger is prime-only but the finite-defect rule and scale law
remain declared design choices, the strongest allowed result is a scoped
owner-level construction with naturalness `OPEN`; it is not a formal Route
pass.

## Appended version-1 audit outcome

**Current status:** `ADVANCE — COMPLETE FINITE-DEFECT PRIME-ONLY LEDGER;
T1 NATURALNESS OPEN; CLASSICAL SYMPLECTIC FIELDS NOT APPLICABLE.`

The frozen definitions are unchanged.  The paper proves finite-variation
equivalence to finitely many domain walls, full shift invariance and inverse,
free/proper scale action, a Hausdorff complete quotient, and the complete
primitive ledger: one oriented circle of length \(\log p\) per prime with all
integer repeats.  The finite-defect carrier retains arbitrary nonmonotone walls
and is topologically distinct from 163's weak-order carrier.  The carrier and
quotient are nowhere locally compact in the stated product/local-cover model;
this remains a broadened-carrier topology, not a classical symplectic manifold.

Finite variation and universal exponential scale are declared designs, so
arithmetic naturalness remains `OPEN`.  No transfer operator, trace, Fredholm
determinant, Hamiltonian/contact/quantum lift, or formal Route coordinate is
supplied.  Route B remains `NOT INVOKED`.
