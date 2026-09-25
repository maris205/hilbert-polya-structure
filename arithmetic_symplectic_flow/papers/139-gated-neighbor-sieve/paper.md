# State-gated sieve feedback: exact source output and a local obstruction to period four

**Paper ID:** 139-gated-neighbor-sieve.  
**Candidate ID:** ANG-20260914-GNS01.  
**Date / status:** 2026-09-14; STOP / FORK — PRIME READOUT AND REVERSIBILITY PROVED; PERIOD 4 EXCLUDED; PERIOD 8 OPEN AT THE SEARCH CAP.  
**Evidence:** elementary proofs and reproducible exact finite constraint enumeration.  
**Route state:** broadened T0--T3 audit only; classical coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We replace unconditional neighbor propagation in a reversible sieve action
with a nonlinear gate, keeping the same divisor-based source and full binary
carrier. The resulting map is a homeomorphism and produces the complete
prime indicator from a uniform zero seed after two steps. The reflected
boundary forces every full temporal period to be divisible by four. Exact
enumeration of the period-four equations through spatial coordinate eight
gives a finite contradiction independent of all higher coordinates. Period
eight is not excluded: its bounded constraint search hits the predeclared
prefix cap. We retain that inconclusive outcome, make no assertion about
global absence of periodic points, and stop this architecture after its
planned checks. No arithmetic-carrying closed packet or analytic owner has
been established.

## 1. Identity, lineage and same-object ledger

The [version-1 card](candidate-card.md) precedes the audit. Set
\(X=\mathbb F_2^{\{2,3,\ldots\}}\) with product topology, use addition in
\(\mathbb F_2\), and define

\[
G(y)_n=\prod_{\substack{2\le d\le\lfloor\sqrt n\rfloor\\d\mid n}}(1-y_d),
\qquad y_1=y_2,
\]
\[
L(y)_n=(y_{n-1}+y_n)(y_{n+1}+y_n),\qquad
R(x,y)=(y,x+G(y)+L(y)).
\]

Empty products equal one. The reflected ghost convention implies
\(L(y)_2=0\). This is one parameter-free action on the full \(X^2\), not
a selected periodic subsystem or a family of adjusted Boolean rules.

The [prior-work lineage](../../docs/prior_work/README.md) is
[050's divisor-based prime/composite exclusion](../050-causal-binary-sieve-fixed-point-screen/paper.md)
to [131's reversible two-register memory](../131-second-order-causal-sieve/paper.md)
to state-gated spatial feedback. Relative to
[138's unconditional additive feedback](../138-reflected-wave-sieve/paper.md),
the higher-neighbor dependence can switch off when the current left
difference vanishes. This changes the spatial recursion assumption, rather
than a numerical parameter. It does not itself establish a geometric lift.

| Owner field | This frozen object | Result / limitation |
| --- | --- | --- |
| Carrier and action | Full compact binary product X squared and R | Homeomorphism |
| Broadened carrier | Transformation groupoid by the full Z action | Same action, with all stabilizers retained |
| Source | G, integer divisibility and integer-coordinate labels | Exact source readout; no supplied prime mask |
| Roof and flow | Unit roof; (z,1) identified with (Rz,0) | Complete suspension |
| Packets | Every full least-period orbit modulo cyclic phase | Period 4 excluded; existence at higher periods OPEN |
| Repetitions | Same unit roof on those same full orbits | If a primitive period m exists, length m and repeat length rm |
| Analytic owner | Ordinary product only if the packet audit warrants it | Not constructed; operator, domain and trace OPEN |
| Classical geometric owner | None | Finite-dimensional symplectic fields NOT APPLICABLE |

No prime list, prime-selected carrier, logarithmic prime roof, Mangoldt
weight, zero data or fitted schedule is used.

## 2. Question and claim boundary

Does replacing unconditional propagation with a state-gated neighbor rule
yield an intrinsic packet that carries the source-derived prime observable?

The positive results are reversibility, continuity and an exact full
arithmetic readout. The negative result is a genuine full-space period-four
exclusion, proved by a finite inconsistent subsystem. Period-eight
satisfiability and all higher full periodic orbits remain OPEN; so does the
return status of the particular zero-seed orbit. No infinite existence claim
is inferred from finitely compatible prefixes, and no infinite absence claim
is inferred from the capped search.

## 3. T0 and source readout

### Proposition 1 — Same-object reversible action

R is a homeomorphism, with

\[
R^{-1}(u,v)=(v+G(u)+L(u),u).
\]

Each coordinate of G and L depends on only finitely many input coordinates,
so R and the displayed inverse are continuous. Direct substitution in either
composition cancels the repeated binary terms. Hence the transformation
groupoid \(X^2\rtimes_R\mathbb Z\) has the stated full action as owner.
Its integer slices give source and range charts, so it is a locally compact
Hausdorff etale groupoid. The unit roof gives a complete suspension: in
either time direction, infinitely many returns require infinitely much time.
No symplectic or Hamiltonian structure is inferred from these facts.

### Proposition 2 — Exact arithmetic output

For the uniform words \(\mathbf0,\mathbf1\) and the prime indicator \(\pi\),

\[
R(\mathbf0,\mathbf0)=(\mathbf0,\mathbf1),\qquad
R^2(\mathbf0,\mathbf0)=(\mathbf1,\pi).
\]

Indeed, both L of a uniform zero word and L of a uniform one word vanish.
Every factor in \(G(\mathbf0)\) is one. A prime n has no divisor in the
displayed product for \(G(\mathbf1)_n\), whereas a composite n has a divisor
between 2 and its square root. Thus \(G(\mathbf1)=\pi\). This proves a
spatial source output at a fixed time; it does not turn the output into an
intrinsic primitive packet or an arithmetic clock.

## 4. Exact temporal constraints

Write a full R-orbit as \((u(t-1),u(t))\). A state fixed by \(R^T\) gives
length-T cyclic temporal words \(u_n(t)\), with

\[
u_n(t+1)+u_n(t-1)+G(u(t))_n
=(u_{n-1}(t)+u_n(t))(u_{n+1}(t)+u_n(t)).
\tag{1}
\]

Conversely, a full infinite collection of cyclic words satisfying (1) gives
a state fixed by \(R^T\). Finite collections alone do not.

### Proposition 3 — Boundary period restriction

At coordinate 2, \(G_2=1\) and \(L_2=0\), so

\[
u_2(t+2)=u_2(t)+1.
\]

Every boundary word has least period four: period two contradicts the
displayed equation, and four is a period. Consequently every full positive
period of R is divisible by four. This restriction already occurs if G is
replaced by the constant-one source, and by itself is not prime-selective
evidence.

### Exact prefix method

Encode a temporal word as an integer with its t-th bit equal to \(u_n(t)\).
Let M=2^T-1, let D be the XOR of the two cyclic shifts, and set

\[
A_n=u_{n-1}+u_n,\qquad E_n=D u_n+G(u)_n.
\]

Equation (1) asks for \(A_n(u_{n+1}+u_n)=E_n\), bitwise. It is solvable
precisely when E has no nonzero bit outside A. On bits where A is one,
the next word is forced to \(u_n+E_n\); on the other bits it is free.
Since every divisor used by G at coordinate n is less than n, its value is
known from the current prefix. This gives an exhaustive spatial extension
algorithm without fixing a higher boundary.

We predeclared a maximum of coordinates 2 through 16 and a 100000-prefix
storage cap, ran T=4 first, and then T=8 because the first check decisively
excluded the boundary's minimal possible period. The exact programs and all
output appear in [the computation record](evidence/computation.md). At
coordinate 16 the algorithm would test existential extendibility without
enumerating coordinate 17; neither run reached that spatial cutoff.

## 5. Results and finite contradiction certificate

### Proposition 4 — No full state is fixed by the fourth iterate

For T=4 the coordinate-2 words are the four integers 3, 6, 9 and 12.
There are 64 unconstrained prefixes through coordinate 3. Completing
equations 3 through 7 gives respectively 132, 52, 36, 4 and 16 prefixes.
Every one of the final 16 fails equation 8, regardless of coordinate 9.

The [independent direct-enumeration check](evidence/computation.md)
scans all sixteen possible next words at each step and confirms both the
counts and the complete residual table. The surviving prefixes have form

\[
(u_2,u_3,u_4,u_5,u_6,u_7,u_8)
=(a,a,15,0,15,a,b),
\]

where \(a\in\{3,6,9,12\}\) and b is any submask of a. For each one,
\(E_8\mathbin{\&}(15\mathbin{\mathrm{XOR}}A_8)\ne0\), as the complete
16-row certificate records. Therefore this finite subsystem is inconsistent
and cannot be a restriction of any full period-four state. This implication
is exact; it does not use a periodic finite-box boundary or numerical
precision. Since fixed points and period-two states were already excluded
at coordinate 2, no full primitive orbit of length at most four exists.

### Period eight — capped and inconclusive

For T=8 the four possible boundary words are 51, 102, 153 and 204.
Completing equation 8 yields 69664 prefixes through coordinate 9. During
equation 9 the algorithm creates its 100001st extension and stops immediately
at the predeclared cap. Only 5250 admissible input prefixes had been processed
at that point, so those last-stage numbers are partial, not complete counts.

The remaining prefixes are not proven extendible to all coordinates.
Conversely, the cap does not rule them out. Thus period eight is OPEN. No
period-twelve or higher search was run, and no Boolean-rule variant was
substituted after the cap.

## 6. Controls and limitations

- The inverse proof applies to any continuous Boolean forcing in the same
  two-register pattern. Reversibility alone therefore proves too much to
  certify an arithmetic packet mechanism.
- Uniform-state cancellation of L preserves the source output by an exact
  elementary proof, rather than by fitted prime data.
- The constant-one source has the same coordinate-2 period-four restriction.
  The boundary restriction alone does not certify arithmetic selectivity.
- The additive-feedback candidate 138 has full-shift periodic data; the
  present local contradiction does not transfer to 138, whose map is different.
  Conversely, no coding or zeta from 138 is imported here.
- The G-removed and full constant-source packet enumerations were not run.
  Their broader packet comparisons remain OPEN; neither is replaced silently
  by the boundary-only control above.
- Free higher boundary variables are essential to the contradiction. There
  is no zero, reflecting or periodic upper cutoff in the temporal search.
- No ordinary orbit product, trace formula or transfer operator was built
  from this incomplete packet information.

## 7. Owner-level gate assessment

| Gate | Exact-candidate result | Scope |
| --- | --- | --- |
| T0 | ESTABLISHED | Full continuous invertible action and complete unit-roof owner |
| T1 | PARTIAL | Exact internally computed prime readout; prime-selective packet clock not established |
| T2 | PARTIAL / OPEN | Full periods must be multiples of four; period four excluded; period eight and higher existence OPEN |
| T3 | OPEN / NOT CONSTRUCTED | No packet-based analytic claim or operator owner |
| Classical A0/A1/A2 | UNASSIGNED | Classical symplectic fields NOT APPLICABLE |
| Route B | NOT INVOKED | No formal Route evaluation |

## 8. Decision

Decision: STOP / FORK after the bounded audit. This is not a global
nonexistence result and not a declaration that the prime observable is
external. The decisive search reason is that the lowest possible packet
period is excluded and the next planned test reaches its finite budget
without establishing an arithmetic-carrying packet. The same-object ledger
remains intact. Further work on a new architecture needs a new frozen card;
this package does not continue by adjusting the local Boolean rule.

## Evidence index

See the [card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence index](evidence/README.md), and
[exact commands and full output](evidence/computation.md).
