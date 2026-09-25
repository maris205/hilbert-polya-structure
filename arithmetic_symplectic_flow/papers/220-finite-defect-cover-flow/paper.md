# Finite-defect cover-chain scale flow

**Paper ID:** `220-finite-defect-cover-flow`  
**Candidate ID:** `ALF-20260918-FDC01`  
**Date / status:** `2026-09-18; scoped constructive theorem / owner-level audit`  
**Status:** `ADVANCE — PRIME-ONLY FINITE-DEFECT LEDGER; NATURALNESS OPEN; CLASSICAL SYMPLECTIC FIELDS NOT APPLICABLE.`  
**Audit state:** `T0--T2 scoped owner-level results; T3 ordinary product only; classical A0/A1/A2 NOT APPLICABLE; formal Route-A UNASSIGNED; Route B NOT INVOKED`

## Abstract

This paper audits a new arithmetic laminated carrier built from two-sided
positive-rational divisibility-cover chains.  A chain is admitted when its
prime cover-ratio word has finite total variation, equivalently finitely many
domain walls.  Unlike the weak numerical ordering in Candidate
ANG-20260915-OCS01 (163), this rule keeps arbitrary finite nonmonotone walls.
The shift-normalization and one universal multiplicative scale cocycle are
owned by this candidate.  Exact arguments show that the finite-defect carrier
is shift-invariant, every periodic state is a constant prime chain, and the
full scale quotient has exactly one primitive oriented orbit of length
\(\log p\) for each prime, with repetitions \(r\log p\).  The carrier and
quotient are Hausdorff but nowhere locally compact; no finite-dimensional
symplectic or Hamiltonian object is asserted.  The prime-cover mechanism is
endogenous to the symbolic source, while the finite-variation admissibility
and universal scale normalization remain design choices, so this is not a
formal Route-A pass.

## 1. Candidate identity and same-object ledger

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Carrier | \(X_{\rm fd}\subset(\mathbb Q_{>0})^{\mathbb Z}\), normalized by \(y_0=1\), with every ratio \(a_j=y_{j+1}/y_j\) prime and \(\sum_j|a_{j+1}-a_j|<\infty\) | frozen |
| Evolution | \(F_{\rm fd}(y)_j=y_{j+1}/y_1\) on the full carrier | frozen and proved invariant |
| Scale action | \(G_{\rm fd}(y,r)=(F_{\rm fd}y,r/y_1)\) on \(X_{\rm fd}\times\mathbb R_{>0}\) | frozen and audited |
| Flow | \(Q_{\rm fd}=(X_{\rm fd}\times\mathbb R_{>0})/\langle G_{\rm fd}\rangle\), \(\Phi^t[y,r]=[y,e^tr]\) | same-object owner |
| Arithmetic source | Divisibility cover atoms are exactly prime ratios; finite total variation is the new admissibility deformation | structural result; naturalness open |
| Roof | Section \(r=1\), actual return roof \(\tau(y)=\log y_1=\log a_0(y)\) | derived below |
| Orbit ledger | All primitive oriented flow orbits of the entire quotient, with cyclic phase identified by the flow | derived below |
| Repetitions | Every positive integer traversal of an actual primitive orbit | derived below |
| Analytic owner | The ordinary product formed from this ledger, only in its absolute convergence half-plane | owner-level construction |
| Transfer operator / trace / Fredholm determinant | Not supplied | open / not evaluated |
| Symplectic, Hamiltonian, contact, quantum owner | Not applicable or deferred; no lift is silently used | open |

The quotient has odd-dimensional flow leaves and a non-locally-compact
transverse carrier.  It is therefore not called a finite-dimensional
symplectic suspension.  Every clock and orbit below belongs to this one
candidate; nothing is imported from 163, 169, or a separate operator.

## 2. Question and claim boundary

### Question

Can a finite-domain-wall deformation of the prime-symbolic cover chain retain
arbitrary finite walls while producing a complete, same-object prime-only
closed-orbit ledger under one universal scale law?

### Strongest supported claim

Yes, at the broadened-carrier owner level: the exact carrier is shift
invariant, all and only constant prime words are periodic, and the full scale
quotient has one primitive orbit of time \(\log p\) for every prime \(p\),
with its integer repetitions.  The construction is a scoped theorem about a
declared carrier and clock, not evidence that those design choices are the
unique or natural arithmetic dynamics.

### Explicit nonclaims

- No finite-dimensional symplectic map, Hamiltonian flow, or quantization is
  supplied.
- No chronological sieve generator, prime-distribution theorem, Riemann-zero
  match, transfer operator, Fredholm determinant, analytic continuation, or
  formal Route-A/B result is claimed.
- The finite-variation rule and the scale normalization are not derived from
  a deeper variational principle; their arithmetic naturalness remains OPEN.
- A finite-window computation would not certify this two-sided object and was
  not used.

## 3. Definitions, inputs, and provenance

Let \(\mathbb P\) denote the positive primes.  For positive rationals,
\(x\prec_{\rm cov}z\) means \(z/x\in\mathbb P\).  The ratio map
\(\rho(y)=a(y)\) sends a normalized cover chain to a word in
\(\mathbb P^{\mathbb Z}\).  Define

\[
 X_{\rm fd}=\left\{y:y_0=1,\ a_j(y)\in\mathbb P,\quad
 E(a):=\sum_{j\in\mathbb Z}|a_{j+1}-a_j|<\infty\right\}.
\tag{3.1}
\]

This is a derived prime alphabet, not a prime-table input: if
\(x<_D z\), then \(n=z/x\) is an integer greater than one.  When
\(n=uv\) with \(u,v>1\), the rational \(xu\) lies strictly between
\(x\) and \(z\) in the divisibility order, so the pair is not a cover.
When \(n\) is prime, any intermediate rational \(w\) would give
integers \(w/x>1\) and \(z/w>1\) whose product is \(n\), which is
impossible.  Thus the relational cover definition and prime-ratio formula
in the frozen card are equivalent.

The coordinate topology is inherited from the product of discrete rational
coordinates.  The ratio map and its inverse (finite products of ratios) are
homeomorphisms between this carrier and its ratio-word image.

For all integers \(n\), write \(y_n\) for the coordinate of the chain.  The
normalised shift and scale action are

\[
 F(y)_j=\frac{y_{j+1}}{y_1},\qquad
 G(y,r)=\left(Fy,\frac r{y_1}\right).
 \tag{3.2}
\]

The allowed data are only rational multiplication, divisibility, the cover
relation, and the universal exponential scale parameter.  In particular,
prime tables, per-prime choices, \(\log p\) assignments, von Mangoldt
weights, and target-zero data are not inputs.

## 4. Exact carrier and scale-flow proof

### 4.1 Finite variation is finite domain-wall energy

Since distinct primes differ by at least one,

\[
 E(a)<\infty\quad\Longleftrightarrow\quad
 W(a):=\{j\in\mathbb Z:a_{j+1}\ne a_j\}\text{ is finite}.
 \tag{4.1}
\]

The forward implication follows because every wall contributes at least one
to the sum.  For the reverse implication, a finite wall set gives a finite
sum of finite integer differences.  Thus every admitted word has constant
prime tails at both \(+\infty\) and \(-\infty\), but its finite middle can be
any nonmonotone prime word.  For example, a word with a finite block
\(2,3,5,3,2\) between constant tails is admitted; no ordering condition
removes it.

### 4.2 Shift invariance and invertibility

For \(F\) in (3.2),

\[
 \frac{F(y)_{j+1}}{F(y)_j}=\frac{y_{j+2}}{y_{j+1}}=a_{j+1}(y),
 \tag{4.2}
\]

so \(E(a(Fy))=E(a(y))\).  The inverse is

\[
 F^{-1}(y)_j=\frac{y_{j-1}}{y_{-1}},
 \tag{4.3}
\]

whose ratio word is \(a_{j-1}(y)\).  Hence \(F\) is a bijection of the
entire finite-defect carrier, not a map defined only on its periodic sector.

The cocycle identity, valid for every \(n\in\mathbb Z\), is

\[
 G^n(y,r)=\left(F^ny,\frac r{y_n}\right).
 \tag{4.4}
\]

For positive \(n\), this follows from
\(y_n=\prod_{j=0}^{n-1}a_j\); for negative \(n\), it follows from the
corresponding reciprocal product.  In particular, \(G\) is a free action:
for \(n>0\), \(y_n\ge2^n\), and for \(n<0\), \(0<y_n\le2^n<1\), so no
nonzero power fixes the scale coordinate.

### 4.3 Proper quotient and complete flow

The carrier is Hausdorff.  The \(\mathbb Z\)-action is proper on the product
with \(\mathbb R_{>0}\): if a compact set has scale coordinate in
\([\epsilon,R]\), then simultaneous membership of \((y,r)\) and
\(G^n(y,r)\) implies \(r/y_n\in[\epsilon,R]\).  For \(n\ge0\),
\(y_n\ge2^n\); for \(n<0\), \(y_n\le2^n\).  Therefore
\(|n|\le \log_2(R/\epsilon)+1\).  Only finitely many translates meet a
compact set.  One can also see Hausdorffness directly: in log-scale
coordinates \(u=\log r\), bounded strips have intersections with only
finitely many deck translates.  Each of these finitely many relations is
the graph of a homeomorphism, hence closed.  Two inequivalent points can
therefore be separated by sufficiently small product neighborhoods avoiding
all those relations; their open quotient images separate their classes.
Thus \(Q_{\rm fd}\) is Hausdorff without any local-compactness assumption.

For later use, every strip \(X_{\rm fd}\times(u_0-\epsilon,u_0+\epsilon)\)
with \(2\epsilon<\log2\) is disjoint from each nontrivial deck translate:
the log-scale displacement of \(G^n\) has magnitude at least
\(|n|\log2\).  The quotient map is open and injective on this strip,
so it gives a homeomorphic local chart.  This supplies the precise local
product statement used in the topology argument below.

The flow \(\Phi^t[y,r]=[y,e^tr]\) commutes with the deck action and is thus
well-defined for every \(t\in\mathbb R\).  On the section \(r=1\), the first
positive return satisfies \([y,y_1]=[Fy,1]\) because
\(G(y,y_1)=(Fy,1)\), and has time

\[
 \tau(y)=\log y_1=\log a_0(y)\ge\log2.
 \tag{4.5}
\]

The lower bound gives two-sided non-Zeno completeness: every sequence of
section returns accumulates infinite positive and negative time.  This is an
actual roof of the quotient, not a unit-roof symbolic proxy.

For completeness, put \(S_n(y)=\log y_n\).  Then \(S_0=0\),
\(S_{n+1}-S_n=\log a_n\ge\log2\), and \(S_n\to\pm\infty\) as
\(n\to\pm\infty\).  Hence for every \(u=\log r\) there is a unique integer
\(n\) with \(S_n\le u<S_{n+1}\).  Applying \(G^n\) gives a unique
representative with scale logarithm in
\([0,\log a_0(F^ny))\).  Thus the whole quotient is the semi-open mapping
torus over the complete carrier with the displayed roof; no orbit is lost by
using the section.

## 5. Periodic rigidity and the complete orbit ledger

Suppose a base state has period \(m>0\).  Equation (4.2) gives
\(a_{j+m}=a_j\) for every \(j\).  If a periodic word had a wall, that wall
would repeat at infinitely many translates and make \(E(a)=\infty\).  Thus
\(a_j=p\) for one prime \(p\), and \(y_j=p^j\).  Conversely each such
constant word belongs to the carrier and is fixed by \(F\).

For a flow return at positive time \(T\), (4.4) gives an integer \(n\) with

\[
 F^ny=y,\qquad e^T=1/y_n.
 \tag{5.1}
\]

Positive \(T\) forces \(n=-m<0\).  The periodic-rigidity result then gives
\(y_m=p^m\), so

\[
 T=m\log p. \tag{5.2}
\]

The primitive case is \(m=1\).  For a fixed prime \(p\), the quotient of its
scale coordinate is \(\mathbb R_{>0}/(r\sim r/p)\), an oriented circle of
length \(\log p\).  There is exactly one such circle for each prime: all
points on the circle are flow phase, not separate packets.  Every repeated
traversal has time \(k\log p\), \(k\ge1\), and no finite-wall nonconstant
state contributes an additional closed orbit.

If one forms the ordinary same-object orbit product in its absolute region,
the ledger gives

\[
 Z_{\rm fd}(s)=\prod_{p\in\mathbb P}(1-p^{-s})^{-1},\qquad
 \Re s>1. \tag{5.3}
\]

This is recorded only as an owner-level product associated with (3.1)--(3.2).
It is not a transfer-operator determinant, continuation theorem, or formal
Route-A A2 result.

## 6. Topology and comparison with 163

The ratio-word model identifies the carrier with the finite-wall subspace of
the countable discrete product \(\mathbb P^{\mathbb Z}\).  It is Hausdorff and
zero-dimensional.  It is not locally compact: every basic neighborhood fixes
only finitely many coordinates.  Choose an unfixed coordinate \(j_0\) and,
outside the fixed window, make a single finite wall whose value at \(j_0\)
ranges over distinct primes.  The resulting family lies in the neighborhood
and has no convergent subnet because its \(j_0\)-coordinate is a discrete
infinite set.  Hence no neighborhood has compact closure.  The product with
\(\mathbb R_{>0}\), and the local-homeomorphic proper quotient, are likewise
nowhere locally compact.

Candidate 163 is also a Hausdorff product-subspace carrier with no classical
local compactness; its decisive difference is the weak global numerical order.
That order forbids every nonconstant two-sided periodic ratio word before the
scale action is analysed.  Candidate 220 instead admits all finite
nonmonotone walls and obtains the same periodic rigidity from finite energy.
Thus the carriers have a similar topological warning but a genuinely
different symbolic mechanism and orbit-screening contract.

## 7. Controls and adverse findings

| Control | Result | Interpretation |
| --- | --- | --- |
| 163 weakly monotone carrier | Different carrier; finite walls such as \(2,3,5,3,2\) are admitted here | Confirms this is not a relabelled order constraint |
| Unrestricted all-word cover carrier | Drops finite variation and admits mixed primitive words such as the alternating \((2,3)\) word | `PROVES_TOO_MUCH` control; the finite-energy gate is essential |
| Fixed wall-count truncation | Not used as the candidate; it would be a different carrier with boundary effects | No finite-window credit transferred |
| Composite increments in place of prime covers | Not a positive result; would add composite constant packets | Arithmetic source control exposes overgeneration |
| Universal scale change \(e^{ct}\) | Changed-clock control, \(T_p=(\log p)/c\) | No per-prime tuning allowed |
| Finite-window enumeration | Not run | Cannot certify the two-sided ledger or topology |

The principal adverse finding is naturalness: finite variation is a clean
shift-invariant admissibility mechanism, but no deeper arithmetic principle
currently selects it over other finite-defect energies.  The scale law is
likewise universal but declared.  These are T1 limitations, not hidden
positive evidence.

## 8. Broadened owner-level audit

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| T0 | Full finite-defect carrier, invariant invertible action, Hausdorff scale quotient and complete flow | `ESTABLISHED` in the stated nonclassical category | Nowhere locally compact; no classical symplectic structure |
| T1 | Prime labels arise from the divisibility-cover relation, and actual times arise from the same scale action | `SCOPED CONSTRUCTION; NATURALNESS OPEN` | Finite energy and exponential scale are declared designs, not arithmetically forced |
| T2 | Full quotient return equation, periodic finite-variation rigidity, one primitive circle per prime, and exact repetition law | `ESTABLISHED` at owner level | No theorem is transferred to a different carrier |
| T3 | Same-object ordinary orbit product (5.3) in its absolute region | `ORDINARY PRODUCT ONLY` | No transfer operator, Fredholm determinant, trace, or continuation |
| Classical A0/A1/A2 | No finite-dimensional symplectic base map is supplied | `NOT APPLICABLE` | Formal Route-A coordinates remain `UNASSIGNED` |
| Route B | No Route-A readiness and no separate authorization | `NOT INVOKED` | Remains outside scope |

## 9. Conclusion and decision

`ALF-20260918-FDC01` is a **scoped advance** in the broadened carrier track:
it supplies a distinct finite-defect symbolic architecture, preserves its full
nonperiodic carrier, and proves a complete prime-only scale-flow ledger.  It
does not close naturalness at T1, and it supplies no classical symplectic or analytic
operator realization.  The next decision is therefore `advance/fork`: retain
this result as a control and search for an endogenous principle selecting the
finite-defect energy; fork immediately if that principle requires changing the
carrier, cocycle, clock, or orbit convention.

## Reproducibility / evidence index

- [Frozen candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence index](evidence/README.md)

The result is an exact symbolic/topological derivation.  No numerical run,
GPU job, finite cutoff, external prime table, or target data was used.
