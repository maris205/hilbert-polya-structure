# Classical candidate card — ASFS-20260918-GDC01

**Version:** 1, 2026-09-18; frozen before the mathematical audit.  
**Initial status:** P0 FROZEN; A0 SCOPED POSITIVE FOR THE GCD SOURCE; A1
SCOPED FAIL (UNIT CLOCK AND INFINITE K-MULTIPLICITY); A2 NOT EVALUATED.

## Frozen object

For each integer \(n\ge 2\), let

\[
D_n=\{1,\ldots,n-1\},\qquad d^+=
\begin{cases}d+1,&d<n-1,\\1,&d=n-1.\end{cases}
\]

For \(n=2\), this convention means \(D_2=\{1\}\) and \(1^+=1\). The
arithmetic defect at a phase is

\[
\delta(n,d)=\gcd(n,d)-1\in\mathbb Z_{\ge0}.
\]

The carrier is the countable disjoint union

\[
M=\coprod_{n\ge2}\coprod_{d\in D_n}\coprod_{k\in\mathbb Z}\mathbb R^2_{n,d,k},
\qquad \omega|_{\mathbb R^2_{n,d,k}}=dq\wedge dp.
\]

Write \(z=(q,p)^T\), and freeze the integral matrix

\[
A_\delta=\begin{pmatrix}2+\delta&1+\delta\\1&1\end{pmatrix},\qquad
\det A_\delta=1.
\]

The one map owned by this candidate is

\[
F(n,d,k,z)=\bigl(n,d^+,k+\delta(n,d),A_{\delta(n,d)}z\bigr).
\tag{1}
\]

The roof is the unit function \(\tau\equiv1\), and the suspension is the
endpoint-glued quotient

\[
M_\tau=\{(x,t):x\in M,\ 0\le t\le1\}/((x,1)\sim(Fx,0)),
\]

with translation flow. No prime table, manually assigned \(\log p\),
von Mangoldt weight, zero data, or per-prime parameter is permitted.

## P0 ownership ledger

| P0 field | Frozen definition / obligation |
| --- | --- |
| Candidate relation | New gcd-defect cocycle construction; no theorem, roof, map, or Route credit is inherited from another package |
| Source lineage | Prime/composite gcd observable \(\to\) sequential phase scan \(\to\) positive-dimensional area-preserving linear Hénon/cat-type lift |
| Phase space | Every \(n\ge2\), every \(1\le d<n\), every \(k\in\mathbb Z\), and all \(z\in\mathbb R^2\) |
| Symplectic map | (1), with the displayed \(A_\delta\) and no parameter fitting |
| Arithmetic action | The same gcd defect increments the integer register and selects the matrix at each phase |
| Roof / flow | Unit roof on the same map and the endpoint-glued suspension above it |
| Clock hypothesis | A prime packet has exactly \(p-1\) unit sections, so \(T_{p,k}=p-1\); the candidate does not derive \(T_{p,k}=\log p\) |
| Periodic convention | All least-period full states in the complete countable carrier, with phase and \(k\) retained and no \(z\)-slice selected |
| Repetition law | The \(r\)-fold traversal of a primitive flow orbit has time \(r(p-1)\); no repeat is reclassified as a new primitive packet |
| Non-Zeno obligation | \(\inf\tau=1\), so the suspension is complete in both time directions |
| Analytic owner | No transfer operator, zeta, trace, or determinant is frozen; any future owner must use this exact \(F,\tau\), and full ledger |
| Controls | Indicator-divisor defect, single-cycle shuffled phase order, projection forgetting \(k\), and \(A_0\)-decoupled geometry |
| Future lift owner | Hamiltonian/contact/quantum DEFERRED |
| Route state | A0/A1 owner-level audit below; formal Route-A coordinates UNASSIGNED; Route B NOT INVOKED |

The lineage arrows are frozen as follows: the gcd defect is zero on every
phase exactly for prime \(n\) and positive somewhere for composite \(n\);
the cyclic scan is the symbolic/sequential admissibility carrier and its
reversible accumulated record is \(k\); and the same defect selects the
positive-dimensional area-preserving matrix \(A_\delta\). This is a direct
conservative lift of the declared prime/composite observable, not a
conjugacy claim about a prior map.

## Immediate boundaries and stop rules

The integer \(n\), phase \(d\), and register \(k\) are part of the frozen
state. Forgetting \(k\) is a many-to-one projection to a different carrier;
it cannot be used to remove the countably many packets while retaining the
same periodic ledger. Likewise, replacing the unit roof by
\(\log((d+1)/d)\), \(\log p\), or any physical roof creates a new candidate ID.

The expected exact audit is that prime fibres have a packet for every
\(k\in\mathbb Z\), while a composite fibre drifts in \(k\) by a positive amount
on each phase cycle. The same proof exposes two A1 stops: the unit clock is
\(p-1\), not logarithmic, and the complete ledger has infinite multiplicity at
each prime period. If the map is changed, the phase order is made
non-bijective, or a determinant is imported, stop and fork rather than
transferring credit.

The card makes no claim of a natural A0 target relation, an A1 pass, an A2
operator, a Route result, a quantum object, or a Riemann-zero statement.
