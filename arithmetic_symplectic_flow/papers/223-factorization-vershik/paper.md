# A divisor-cover factorization path has no two-sided Vershik homeomorphism

**Paper ID:** 223-factorization-vershik  
**Candidate ID:** ANG-20260918-FVP01  
**Date / status:** 2026-09-18; PRE-P0 STOP — CANONICAL VERSHIK SUCCESSOR NOT A BIJECTION  
**Route state:** Owner-level T0–T3 not entered; formal Route coordinates
UNASSIGNED; Route B NOT INVOKED.

## Abstract

This screen tests a new broadened carrier built directly from divisor-cover
edges, rather than borrowing a prime alphabet or the shift action from an
earlier candidate.  Positive-rational divisibility covers derive prime edge
labels.  All normalized two-sided cover paths are retained, and their
outgoing edges are ordered by ordinary integer size.  The proposed action is
the canonical lexicographic successor with carry, with a multiplicative
scale cocycle given by the edge ratio.

The source carrier is well defined and is homeomorphic to the full
two-sided prime-label path space.  Every vertex has infinitely many outgoing
edges and the ordinary order has no maximal edge.  Consequently the stated
scan for the first non-maximal edge stops immediately at index \(0\), so the
frozen successor is the everywhere-defined next-prime update at that index.
It is not onto because no prime precedes 2.  Thus the frozen action is not a
homeomorphism and cannot supply the required two-sided integer action, scale
quotient, or closed-orbit ledger.  This is an exact early stop, not a
numerical search or a claim about all Bratteli–Vershik systems.

## 1. Candidate identity and same-object ledger

The [frozen card](candidate-card.md) fixes the carrier before this audit.
For \(x,y\in\mathbb Q_{>0}\), write \(x<_{D}y\) if \(y/x\in\mathbb N\) and
\(y/x\ge2\).  A strict cover \(x\prec_{\rm cov}y\) means that there is no
positive rational \(z\) with \(x<_{D}z<_{D}y\).  The graph and normalized
path space are

\[
 \mathcal G_{\rm FVP}:\quad x\longrightarrow xp\quad(p\in\mathcal P),
 \qquad
 X_{\rm FVP}=\{x_0=1,\ x_j\prec_{\rm cov}x_{j+1}\ (j\in\mathbb Z)\}.
\tag{1}
\]

The coordinates carry the product topology inherited from the discrete
positive-rational space.  The edge labels are
\[
 p_j(x)=x_{j+1}/x_j.
\tag{2}
\]
At a fixed vertex \(x\), the order of edges is the ordinary order of the
integer labels \(p\).  The proposed action \(V\) is the two-sided
lexicographic successor/carry described in the card: scan a fixed carry ray
from index \(0\) toward negative indices, replace the first non-maximal
edge by its next edge, and reset all earlier scanned edges to the minimal
edge 2.  The proposed scale owner would be
\[
 \kappa(x)=p_0(x),\qquad G(x,r)=(Vx,r/\kappa(x)),\quad r>0.
\tag{3}
\]
Equation (3) is a declaration to be tested, not a valid action by
assumption.

| Ledger item | Frozen owner | Result |
| --- | --- | --- |
| Arithmetic source | Positive-rational divisibility covers | Exact source derivation below |
| Symbolic carrier | Full normalized two-sided paths in (1) | Well defined; equivalent to \(\mathcal P^{\mathbb Z}\) |
| Proposed action | Ordinary-order lexicographic successor with carry | \(V\) is defined forward, injective, and non-surjective |
| Clock / scale | \(\kappa=p_0\), prospective \(\log\kappa\) cocycle | No two-sided flow because \(V^{-1}\) is absent |
| Primitive packets | All actual periodic \(V\)-orbits, if a two-sided action existed | Not testable |
| Transfer operator / zeta | Same-object owner only | Not supplied |
| Finite-dimensional symplectic base | None | NOT APPLICABLE |

No shift, unit roof, determinant, or orbit result from
[148](../148-saturated-divisibility-chain-shift/paper.md) or the ordered
scale carrier [163](../163-ordered-cover-scale-suspension/paper.md) is
transferred.  Replacing \(V\) by either earlier action would be a new card.

## 2. Lineage and question

The retained prior-work arrow is

~~~text
prime/composite divisor observable
  -> divisor-cover irreducibility
  -> factorization-path coding
  -> lexicographic/carry return attempt.
~~~

The screen asks one decisive question: does the stated ordinary order turn
the full two-sided factorization carrier into a bijective recurrent action?
Only after that question could an endogenous multiplicative scale cocycle
become a roof, and only after a roofed action could primitive packets or a
same-object zeta be audited.

## 3. Exact source carrier

### Proposition 1 — Cover edges derive prime labels

For positive rationals \(x<_{D}y\), the relation
\(x\prec_{\rm cov}y\) holds exactly when \(y/x\) is prime.

**Proof.** Put \(n=y/x\in\mathbb N\), \(n\ge 2\).  If
\(n=ab\) with \(a,b\ge 2\), then \(z=ax\) is a positive rational with
\(x<_{D}z<_{D}y\).  Conversely, an intermediate \(z\) gives
\(a=z/x\ge2\) and \(b=y/z\ge2\) in \(\mathbb N\), so \(n=ab\) is
composite.  Hence absence of an intermediate is equivalent to primality.
\(\square\)

### Proposition 2 — All two-sided factorization paths are retained

The ratio map
\[
 R:X_{\rm FVP}\longrightarrow\mathcal P^{\mathbb Z},\qquad
 R(x)_j=p_j(x)
\tag{4}
\]
is a homeomorphism.  Its inverse sends \(p=(p_j)_{j\in\mathbb Z}\) to
\[
 x_j=
 \begin{cases}
 \prod_{i=0}^{j-1}p_i,&j>0,\\
 1,&j=0,\\
 \left(\prod_{i=j}^{-1}p_i\right)^{-1},&j<0.
 \end{cases}
\tag{5}
\]

**Proof.** Proposition 1 gives the cover condition for every ratio in
\(\mathcal P\).  Formula (5) is the unique normalized chain with those
ratios.  Each coordinate of (5) depends on finitely many coordinates of
the prime word, and (4) is coordinatewise, so both maps are continuous
for the product topologies.  They are inverse by telescoping. \(\square\)

In particular, the all-2 path, a path alternating 2 and 3, and every
other mixed path are members of the frozen carrier.  No periodic subset is
selected before the action is tested.

## 4. The canonical successor/carry obstruction

### Proposition 3 — Ordinary edge order has no maximal digit, so the scan
stops at index 0

At each vertex \(x\), the outgoing edge set
\(\{x\to xp:p\in\mathcal P\}\) is countably infinite and has no maximal
element in the ordinary integer order.

**Proof.** There are infinitely many primes.  Given any prime \(p\), the
integer \(p!+1\) has a prime divisor \(q>p\); otherwise all its prime
divisors would divide \(p!\), which is impossible.  Thus an outgoing edge
larger than \(xp\) always exists. \(\square\)

Because every digit is non-maximal, the stated scan for the first
non-maximal edge stops at index \(0\) on every path.  No earlier digit is
reset.  Thus the frozen action is explicitly
\[
 V(p)_0=s(p_0),\qquad V(p)_j=p_j\ (j\ne0),
\tag{6}
\]
where \(s(p)\) is the next prime after \(p\).  The absence of a maximal edge
does not make \(V\) undefined; it removes any later carry branch.

### Proposition 4 — The actual successor is not surjective

Under the actual frozen scan, the distinguished label is incremented to its
next prime \(s(p_0)\) while all other labels are fixed:
\[
 V(p)_0=s(p_0),\qquad V(p)_j=p_j\ (j\ne0).
\tag{7}
\]
Then \(V\) is not surjective.

**Proof.** Every prime has a next prime, so (7) is defined.  But no prime has
predecessor 2.  Hence a path \(q\) with \(q_0=2\), such as the all-2 path,
cannot equal \(V(p)\) for any \(p\).  Therefore \(V\) is not onto and cannot
be the base of an integer action or a scale quotient. \(\square\)

Any alternative that sends a putative maximal edge back to 2 must first add
a maximal symbol or a wrap convention.  The prime order has no such symbol.
A finite prime cutoff, a one-sided boundary, or a selected compactification
would be new carrier data and is outside ANG-20260918-FVP01.

The next-prime formula also shows that \(p_0(V^m p)\) is strictly increasing
with \(m\).  Hence this frozen semigroup map has no periodic point.  This is
secondary to the non-surjectivity stop: no inverse \(V^{-1}\) exists on the
full carrier, so no two-sided integer action can be formed.

## 5. Scale cocycle and periodic packets

The multiplicative cocycle \(\kappa(x)=p_0(x)\) is a well-defined positive
observable on the carrier.  For the forward iterates of the actual
everywhere-defined map, one has the formal semigroup identity
\[
G^m(x,r)=\left(V^m x,\,
 r\Big/\prod_{j=0}^{m-1}\kappa(V^j x)\right)
\quad(m>0),
\tag{8}
\]
and a periodic \(V\)-orbit could acquire a scale return
\(\log\prod_j\kappa(V^j x)\).  In the frozen candidate, Propositions 3 and
4 show that \(V\) is not invertible.  Therefore (8) does not define a full
flow, roof, primitive orbit, or repetition law.  In particular, no prime-log
packet is credited merely
because the pointwise observable \(\log p_0\) is available.

## 6. Gate assessment and controls

| Gate | Evidence for ANG-20260918-FVP01 | Status | Limitation / decision |
| --- | --- | --- | --- |
| T0 / carrier owner | Exact divisor-cover path carrier and topology | SCOPED ESTABLISHED | The proposed action is not an automorphism |
| T1 / endogenous arithmetic and clock | Cover labels are prime-derived; \(\kappa=p_0\) is a positive observable | SCOPED FAIL for action/clock | \(V\) is defined forward but not invertible; no integer action or realized roof |
| T2 / primitive packets and repetition | Conditional formula only | NOT TESTABLE | No periodic ledger can belong to the absent action |
| T3 / same-object trace/zeta/operator | None | NOT EVALUATED | Downstream owner never instantiated |
| Classical A0/A1/A2 | No finite-dimensional symplectic base or suspension | NOT APPLICABLE | This is a broadened ANG screen, not a Route candidate |
| Route B | No Route-A readiness | NOT INVOKED | No coordinate or rescue audit permitted |

Controls preserved in the stop:

- **Unbounded-order control:** every outgoing edge has a larger edge, so the
  first non-maximal scan position is always index 0.
- **Minimal-preimage control:** the all-2 path has no preimage under the
  actual next-prime update.
- **Mixed-path control:** alternating 2 and 3 remains in the full carrier; it
  cannot be removed to manufacture a periodic sector.
- **Finite-cutoff control:** imposing a largest prime or wrap is explicitly a
  changed candidate, not a repair of this one.
- **Ownership control:** replacing the proposed successor by the shift would
  reproduce another carrier/action contract and receives no credit here.

## 7. Decision

**PRE-P0 STOP / FORK.**  The source carrier is mathematically clear, and the
frozen scan is the everywhere-defined next-prime update at index \(0\).
However, it is not surjective: states with \(p_0=2\) have no preimage.  The
multiplicative cocycle therefore has no same-object two-sided flow owner, and
no primitive orbit or analytic gate can be advanced.

A future candidate may investigate a finite ordered divisor diagram, an
explicit compactification, or a different recurrent local rule, but each
must receive a new ID and a fresh card.  Such a candidate may not inherit
ANG-20260918-FVP01's proposed scale, packet, or Route status.

## Reproducibility / evidence index

The exact definitions and decision are in this paper and the
[candidate card](candidate-card.md).  The claim ledger and the bounded
readback receipt, including the logical correction, are in
[evidence/README.md](evidence/README.md).  No
computation, prime table, numerical search, external literature claim, or
Route evaluation was used.
