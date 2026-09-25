# Natural path-groupoid suspension of the affine greatest-prime-factor recurrence

**Paper ID:** 087-affine-gpf-path-groupoid-flow  
**Candidate ID:** ANG-20260914-AGPF01  
**Date / status:** 2026-09-14; BROADENED T0–T3 ESTABLISHED  
**Route state:** Broadened audit only; formal Route A unassigned; Route B NOT INVOKED.

## Abstract

This paper freezes a separate arithmetic-groupoid flow built from the natural
two-sided paths of (H(n)=\operatorname{gpf}(n+1)).  Unlike its noninvertible
integer source map, the path shift is invertible.  The complete periodic-path
ledger follows from the exact 084 classification: one oriented prime-only
two-packet has two cyclic phases, unit-roof time (2), and repetitions (2r).
Its same-object orbit zeta is ((1-e^{-2s})^{-1}).  The construction is not a
classical symplectic map, has no per-prime logarithmic clock, and supplies no
formal Route coordinate.

## 1. Frozen object and same-object ownership

Define

\[
X_H=\{z=(z_j)_{j\in\mathbb Z}:z_j\in\mathbb N_{>0},\quad
z_{j+1}=\operatorname{gpf}(z_j+1)\},
\]

with (sigma z=(z_{j+1})_j), and take the transformation groupoid
(X_H\rtimes_\sigma\mathbb Z).  Since (sigma^{-1}z=(z_{j-1})_j), this
action is invertible even though (H) is not.  Its suspension has the fixed
unit roof in the candidate card.

| Item | Same-object owner | Status |
| --- | --- | --- |
| Carrier and action | (X_H,sigma,X_H\rtimes\mathbb Z) | frozen |
| Arithmetic source | edge equation (z_{j+1}=\operatorname{gpf}(z_j+1)) | frozen |
| Symbolic lineage | prime-factor recurrence and its natural extension | direct partial lineage |
| Closed packets / repetitions | (sigma)-periodic paths with cyclic phases | frozen |
| Roof / flow | (	au=1), its suspension | frozen |
| Zeta | orbit product from that same ledger and roof | frozen |
| Classical symplectic map / quantum owner | none | NOT APPLICABLE / DEFERRED |

No object from 079 is used: the source map, path space, packet, and roof are
all defined anew here.

## 2. Complete periodic packet ledger

If (z\in\operatorname{Fix}(\sigma^n)), its zeroth coordinate is periodic
for (H) with period dividing (n). Conversely, each periodic (H)-cycle
defines its periodic bi-infinite path.  Record 084 proves exactly one
oriented primitive (H)-cycle, (2\mapsto3\mapsto2). Hence

\[
\#\operatorname{Fix}(\sigma^n)=
\begin{cases}
2,&2\mid n,\\
0,&2\nmid n.
\end{cases}
\]

The two points are merely the two marked phases of one oriented primitive
packet, not two primitive orbits. With (	au=1), its primitive suspension
length is (T_\gamma=2), while an (r)-fold traversal satisfies
(T_{\gamma^r}=2r).

## 3. Same-object zeta

Using the primitive-oriented convention just stated,

\[
\log\zeta_H(s)=\sum_{r\ge1}\frac{e^{-2rs}}{r},
\qquad
\zeta_H(s)=\frac1{1-e^{-2s}},\qquad \operatorname{Re}s>0.
\]

The convergence region follows from the geometric series. This is an orbit
zeta of the exact unit-roof groupoid suspension; it is neither the Riemann
zeta function nor a transfer operator/determinant imported from another
carrier.

## 4. Broadened audit and boundaries

| Audit | Evidence | Status |
| --- | --- | --- |
| T0 carrier/type and ownership | path space, shift, groupoid, and roof are all frozen here | established |
| T1 endogenous arithmetic/clock | GPF edge rule is internal; unit clock only | established, no prime-log claim |
| T2 packets/repetitions | complete two-phase primitive packet and (2r) repetitions | established |
| T3 same-object trace/zeta | displayed orbit zeta uses that packet and roof | established |
| Classical P0/A0–A2 | no positive-dimensional symplectic base | NOT APPLICABLE / unassigned |
| Route B | no Route-A readiness | NOT INVOKED |

The natural extension changes the carrier, so it is a new candidate rather
than a repair of 084. It does not cure the missing Hénon/conservative lineage
arrows or manufacture a one-prime-one-orbit clock.

## 5. Decision

**Portfolio position: advance within the broadened track; fork for classical
ASFS.**  This is the second exact factor-recurrence path-flow control with a
same-object zeta, but its single small packet remains too sparse and too
nonclassical for the original mission. A future classical candidate must own a
positive-dimensional symplectic base without borrowing this groupoid ledger.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [084 source-map classification](../084-affine-gpf-two-cycle-control/paper.md)
- [079 distinct GPF-Fibonacci path-flow control](../079-gpf-path-groupoid-flow/paper.md)
