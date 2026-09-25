# 228 — GCD-defect cocycle on a countable symplectic carrier

**Candidate:** ASFS-20260918-GDC01  
**Status:** P0 FROZEN; A0 SCOPED POSITIVE FOR THE GCD SOURCE; A1 SCOPED FAIL
(UNIT CLOCK AND INFINITE K-MULTIPLICITY); A2 NOT EVALUATED

Candidate 228 freezes one genuinely same-object finite-dimensional symplectic
map on the countable carrier

\[
(n,d,k,z),\qquad n\ge2,\quad 1\le d<n,\quad k\in\mathbb Z,\quad z\in\mathbb R^2.
\]

The phase moves cyclically, the integer register updates by the endogenous
gcd defect \(\delta(n,d)=\gcd(n,d)-1\), and the same defect selects
\(A_\delta=\begin{psmallmatrix}2+\delta&1+\delta\\1&1\end{psmallmatrix}\).
The map is globally invertible and symplectic. Prime fibres have exactly one
origin packet for every \(k\in\mathbb Z\), with \(p-1\) phases and unit-roof
period \(p-1\); composite fibres have positive \(k\)-drift and no periodic
states. Thus the full prime packet family is countably infinite and the clock
is not \(\log p\). These are decisive A1 stops, not a Route result.

- [Full paper and exact audit](paper.md)
- [Frozen candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and verification record](evidence/README.md)

**Portfolio position:** stop / fork. Keep the complete geometric theorem as a
control; do not project away \(k\), tune the roof, or import an analytic owner.
Route B is NOT INVOKED.
