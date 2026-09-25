# An endogenous aggregate-log roof for the Alladi–Erdős path-groupoid flow

**Paper ID:** `124-alladi-erdos-log-roof-path-flow`  
**Candidate ID:** `ANG-20260914-AE02`  
**Date / status:** `2026-09-14; EXTERNAL BROADENED T0–T3 POSITIVE CONTROL — ENDOGENOUS AGGREGATE-LOG ROOF ON THE PRIME-CARRYING TWO-PACKET`  
**Route state:** `Broadened audit only; formal Route A UNASSIGNED; Route B NOT INVOKED`

## Frozen object and roof distinction

Use the two-sided \(B_1\)-path carrier and shift defined in 123, but freeze the
different roof

\[
\tau(z)=\log B_1(z_0)=\log z_1.
\]

The equality follows from the path equation; it makes the clock an observable
of the same arithmetic edge rule. On \(X_{B_1}\), every edge target is at least
\(2\), so \(\tau\ge\log2>0\), giving the stated non-Zeno condition. The
suspension and the orbit product below belong to this roof, not to 123's unit
roof.

| Item | Same-object owner | Status |
| --- | --- | --- |
| Carrier/action/groupoid | \(X_{B_1},\sigma,X_{B_1}\rtimes\mathbb Z\) | frozen |
| Arithmetic source | \(B_1\) on every edge | frozen |
| Roof / flow | \(\log B_1(z_0)\) and its suspension | frozen |
| Packet/repetition ledger | 123's complete source-derived \(4\) and \(5,6\) cycles | frozen for this object |
| Zeta | this roof applied to precisely that ledger | frozen |
| Symplectic/Hénon owner | none | `NOT APPLICABLE` |

## Packet lengths and same-object zeta

On the alternating prime-carrying packet, the consecutive values of the
source action are

\[
B_1(5)=6,\qquad B_1(6)=5.
\]

Thus the two edge roofs sum to

\[
T_\gamma=\log6+\log5=\log30,
\qquad T_{\gamma^r}=r\log30.
\]

The other primitive packet is the fixed path at \(4\), with length \(\log4\).
Using the complete periodic ledger from 123 yields

\[
\zeta_\gamma(s)=\prod_{r\ge1}\exp\!\left(\frac{30^{-rs}}r\right)
=\frac1{1-30^{-s}},
\]

and

\[
\zeta_{B_1,\tau}(s)=\frac1{(1-4^{-s})(1-30^{-s})},
\qquad\operatorname{Re}s>0.
\]

This is a finite packet product, not a Riemann zeta identity or an imported
operator/determinant.

## Broadened audit and boundary

| Audit | Evidence | Status |
| --- | --- | --- |
| T0 carrier/type and ownership | frozen path groupoid and distinct roof | established |
| T1 endogenous arithmetic/clock | roof is \(\log\) of the same edge action | established, aggregate only |
| T2 packets/repetitions | complete two-packet ledger and \(r\log30\) law | established |
| T3 same-object zeta | displayed product uses exact roof and ledger | established |
| Classical P0/A0–A2 | no finite-dimensional symplectic base | `NOT APPLICABLE` |
| Route B | no Route-A-ready candidate | `NOT INVOKED` |

The roof does not make a one-prime-one-orbit clock: the prime state \(5\) and
the composite state \(6\) jointly give the aggregate \(\log30\). The direct
prior-work lineage remains absent; this factorisation path groupoid neither
deforms the sieve-symbolic source nor supplies a Logistic/Hénon/conservative
realization.

**Portfolio position: advance as a broadened analytic control; fork for
classical ASFS.** Any future classical branch must establish an explicit
source-level bridge before reusing neither this roof nor its zeta.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence](evidence/README.md)
- [123 distinct unit-roof object](../123-alladi-erdos-path-groupoid-flow/paper.md)
