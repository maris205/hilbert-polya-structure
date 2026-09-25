# Paper407 — divisor-power digit reassembly

Candidate ID: `ANG-20260923-DPR01`. Version1, 2026-09-23.
Batch `NONLINEAR-PACKET-20260923-L`, round3/5.
Outcome: `OWNED REASSEMBLY CLOCK; COMPOSITE FIXED PRIMITIVES — STOP / FORK`

The full owner is \(X=\mathbb N_0\times[0,1]^2\), with counting memory times planar Lebesgue measure. Geometry selects \(d=1+\lfloor nx\rfloor\); legal MAIN steps require nonzero remainder \(r=nx-(d-1)\) and actual divisibility \(d\mid n\). The quotient \(q=n/d\) sets both the power and the second digit grid. With \(e=1+\lfloor qy\rfloor,\ s=qy-(e-1)\),
\[
T(n,x,y)=\left(d+e,r^q,\frac{d-1+s}{d}\right).
\]
All terminals, units, square faces, digit cuts, and actual incoming are retained. This is not a classical conservative or positive-roof suspension.

Its complete inverse branches own the every-Borel IMAGE
\[
J=q^{-3}u^{1/q-1},\qquad
\kappa=3\log q+(q-1)\log r,
\]
using the prescribed analytic point version, including null faces. Counting memory introduces no invented determinant factor.

MAIN's complete fixed set comprises
\[
\left(q,q^{-q/(q-1)},\frac{q-2}{q-1}\right),\ q\ge2,
\qquad (4,\rho^2,t),\ \rho=(1+\sqrt{17})/8,\ 1/2\le t<1.
\]
Their entire primitive clock groups are respectively \(2\log q\,\mathbb Z\) and \(\log(1+\sqrt{17})\,\mathbb Z\). In particular the actual lower-face fixed point \((2,1/4,0)\) has primitive \(\log4\). MAIN therefore fails the ordinary-prime target on its own; equal-time or continuum packets cannot be merged.

The paper gives all source/extension isotropy, full clock and lag kernels, every checked incoming layer and all real phases, plus a general cycle/remainder identity without higher-period enumeration. Each control has its own inverse IMAGE and complete fixed set: L retains a continuum of \(\log4\) fixed packets; G has MAIN's same fixed set but keeps its extra nondivisible branches; H includes the full zero-clock identity sheet at memory1 and its separately parameterized positive-clock fixed sets. Zero clock does not delete isotropy.

## Record and boundary

- [Frozen card](candidate-card.md).
- [Full proof and disclosures](paper.md).
- [Claim ledger](claim-ledger.md).

T0 owner established; T1 local mechanism and owned clock established, strong naturalness and arbitrary-encoding risks OPEN; T2 necessary target fails. T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED. Same-object ledger intact. STOP / FORK; no new candidate, higher census, operator, global coverage, or invariant-probability claim.

Input: frozen105-line card SHA256 `52ad8cc8d271c49317cf7245aed09ef3d421d2245b3b091c0f6c5054c96b25a1`. Exact proofs only; no scientific code/numerics or external search. The main author read no407 evidence/raw/peer proof. Same-author helper `/root/bilateral_transport_review/direct_controls` checked the draft definition by message, then read only that frozen card to derive H/G; it was not the independent reviewer. Prior design mental algebra and shared-history exposure are disclosed in the paper, not presented as blind preregistration. AI agents supplied derivation, drafting, and internal checks; no human or external verification is certified. Internal review is NOT_CALIBRATED.

EOF — DPR01 package handoff; no higher-period work started.
