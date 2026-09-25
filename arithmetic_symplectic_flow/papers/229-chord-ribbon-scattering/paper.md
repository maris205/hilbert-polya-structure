# Chord-ribbon scattering: an exact groupoid orbit screen

**Paper ID:** `229-chord-ribbon-scattering`
**Candidate ID:** `ANG-20260918-CRS01`
**Date / status:** 2026-09-18; `NEGATIVE` (scoped T1/T2 stop)
**Carrier:** broadened arithmetic noncommutative/groupoid carrier; classical
symplectic fields are `NOT APPLICABLE` in this version.
**Route state:** owner-level T0 established; T1 arithmetic source/clock
selectivity fails; T2 finite primitive/repetition ledger established but the
prime-packet target fails; T3 not supplied. Classical A0/A1/A2 are
`NOT APPLICABLE`; formal Route-A is `UNASSIGNED`; Route B is `NOT INVOKED`.

## Abstract

We audit one frozen arithmetic groupoid carrier built from labelled integer
graphs.  For each \(n\ge 2\), the vertices \(1,\ldots,n\) are joined by the
backbone \(j\leftrightarrow j+1\) and by divisor chords \(d\leftrightarrow n/d\)
for \(d\mid n\), \(d<\sqrt n\), with duplicate edges removed.  Oriented edges
are scattered by the increasing cyclic successor at the arrival vertex.  The
result is a permutation \(\sigma\) on a countable disjoint union of finite dart
sets, hence it owns a transformation groupoid and an orbitwise complete
roofed suspension for

\[
  \tau(u,v)=\frac12\left|\log(v/u)\right|.
\]

The exact \(n=8\) ledger has primitive dart lengths \([3,8,7]\) and roof times
\([\log 2,\log 8,\log 8]\).  The \(n=10\) control has lengths \([4,8,10]\) and
times \([\log(5/2),\log 10,\log 10]\).  A composite \(n=4\) already has a
primitive time-\(\log4\) cycle, not a repetition of the prime \(2\) component.
Therefore the same carrier owns composite primitives and equal-time collisions;
the divisibility source does not select a prime-only packet dictionary.  This
is a decisive broadened T1/T2 stop.  No positive-dimensional symplectic lift,
operator, determinant, Route-A coordinate or Route-B evaluation is asserted.

## 1. Candidate identity and same-object ledger

### 1.1 Exact carrier

For each \(n\ge 2\), let

\[
 V_n=\{1,\ldots,n\},
\]

and let \(E_n\) be the simple edge set

\[
 E_n=\Bigl\{\{j,j+1\}:1\le j<n\Bigr\}
 \cup
 \Bigl\{\{d,n/d\}:d\mid n,\ d<\sqrt n\Bigr\}.
\]

The first family is the backbone.  In the second family an edge equal to a
backbone edge is inserted only once; \(d=\sqrt n\) is excluded, so no loop is
created.  The integer \(n\) remains a component label.  Put

\[
 D_n=\{(u,v):\{u,v\}\in E_n\},\qquad
 X=\bigsqcup_{n\ge2}D_n.
\]

For \(v\in V_n\), denote the increasing list of its neighbours by

\[
 N_n(v)=(w_1<\cdots<w_{d_n(v)}).
\]

If \(u=w_i\), define \(c_{n,v}(u)=w_{i+1}\) for \(i<d_n(v)\) and
\(c_{n,v}(w_{d_n(v)})=w_1\).  If \(d_n(v)=1\), this is the one-neighbour
reflection.  The frozen local map is

\[
 \sigma_n(u,v)=(v,c_{n,v}(u)),
 \qquad \sigma=\bigsqcup_{n\ge2}\sigma_n.
\]

The owner-level groupoid is the transformation groupoid

\[
 \mathcal G=X\rtimes_\sigma\mathbb Z,
\]

whose arrows can be written \((x,k)\) with source \(x\), range
\(\sigma^k x\), and product
\((\sigma^k x,\ell)(x,k)=(x,k+\ell)\).  The
arrow space is discrete.  This is a broadened `ANG` carrier, not a claim that
the dart set is a symplectic manifold.

### 1.2 Roofed suspension and clock

The same \((X,\sigma)\) owns the suspension relation

\[
 (x,\tau(x))\sim(\sigma x,0),
 \qquad
 \tau((u,v))=\frac12\left|\log\frac vu\right|.
\]

Translation in the second coordinate defines the suspension flow on the
resulting disjoint union of circles.  The roof is positive because every edge
has \(u\ne v\).  It is not uniformly bounded below over all components:

\[
 \inf_{n\ge2,(u,v)\in D_n}\tau(u,v)=0,
\]

as shown by the backbone darts \((j,j+1)\).  This does not produce Zeno motion
for a fixed state: \(\sigma\) preserves \(n\), \(D_n\) is finite, every dart is
periodic, and the finite cycle has strictly positive total time.  Thus every
individual forward and backward orbit is complete.  We do not claim a uniform
global roof bound.

The owner table is therefore:

| object | owner and status |
| --- | --- |
| arithmetic graph | the integer-divisibility rule defining the same \(E_n\) |
| symbolic action | the same local successor map \(\sigma\) on \(X\) |
| clock | the same edge roof \(\tau\) in the suspension relation |
| primitive orbits | least-period cycles of this \(\sigma\), with component label \(n\) retained |
| repetitions | \(r\)-fold traversal of one primitive suspension circle, time \(rT\) |
| analytic owner | not supplied; no determinant or trace is claimed |
| symplectic/Hamiltonian/quantum lift | not supplied and not inferred |

No row is imported from papers 136, 217, 225 or any other candidate.

## 2. Question and claim boundary

### Question

Does the frozen divisibility-chord scatter produce a same-object closed-orbit
packet that is selective for prime labels and has a nonarbitrary logarithmic
clock, or does the full groupoid ledger immediately retain decisive composite
controls?

### Strongest supported claim

The local scatter is a bijection and the full finite orbit ledger is exact.
The canonical \(n=8\) and \(n=10\) ledgers contain composite primitive cycles
with the times stated above, and \(n=8\) produces a composite cycle with the
same time \(\log 2\) as the prime \(p=2\) component.  Hence the frozen carrier
fails prime-packet source selectivity at the broadened T1 screen while
retaining an owner-level T2 orbit/repetition convention. Classical A0/A1/A2
are NOT APPLICABLE for this nonclassical carrier.

### Explicit nonclaims

- The graph family is not a positive-dimensional symplectic map or Hamiltonian
  flow.  No such lift has been built.
- The logarithmic roof is not a proven endogenous prime clock; its source
  selectivity is refuted by the full ledger.
- No transfer operator, trace, zeta, Fredholm determinant, analytic
  continuation, Hilbert space, quantum spectrum or target-divisor result is
  supplied.
- Classical A0/A1/A2 are NOT APPLICABLE; formal Route-A is UNASSIGNED and
  Route B is NOT INVOKED.
- Finite \(n=8,10\) checks do not prove a classification for all composite
  labels; they are decisive counterexamples to the prime-only packet claim.

## 3. Definitions, provenance and lineage

### 3.1 Permitted arithmetic mechanism

The only arithmetic test is \(d\mid n\) in the chord rule.  The construction
does not query a prime table.  For a prime \(p\), the only divisor with
\(d<\sqrt p\) is \(d=1\), so the chord \(\{1,p\}\) closes the backbone into a
cycle (for \(p=2\) it duplicates the sole backbone edge).  For a composite
\(n\), additional chords may occur, but the \(d=1\) chord is still present.
The distinction between prime and composite labels is therefore generated by
the same local divisibility predicate on every component; it is not a stored
prime bit.

The lineage arrow is deliberately narrow:

```text
prime/composite observables
  -> divisibility-admissible symbolic graph
  -> finite ribbon/dart scattering
  -> groupoid suspension.
```

This is a broadened carrier continuation of the project's symbolic seed.  It
does not claim the Logistic-to-Hénon bridge, a sequential deformation, or a
classical geometric lift.  Those fields remain unavailable rather than being
silently satisfied by the groupoid terminology.

### 3.2 Primitive convention

For \(x\in D_n\), let \(L(x)\) be the least positive integer with
\(\sigma^{L(x)}x=x\).  The finite cycle

\[
 [x]=\{x,\sigma x,\ldots,\sigma^{L(x)-1}x\}
\]

is one oriented primitive dart cycle.  Its suspension period is

\[
 T([x])=\sum_{j=0}^{L(x)-1}\tau(\sigma^jx).
\]

Different \(n\)-labels, different cycles, and opposite orientations are not
identified merely because their \(L\) or \(T\) agree.  The \(r\)-fold
repetition has length \(rL\) as a dart traversal and elapsed time \(rT\);
it does not create a new primitive cycle.

## 4. Exact map and groupoid proof

### Proposition 1 (finite graph and local bijection)

For every \(n\ge 2\), \(E_n\) is finite, \(D_n\) is finite, and

\[
 \sigma_n^{-1}(v,w)=\bigl(c_{n,v}^{-1}(w),v\bigr).
\]

Consequently \(\sigma_n\) and \(\sigma\) are bijections.

**Proof.**  There are only \(n-1\) backbone candidates and at most
\(\lfloor\sqrt n\rfloor\) chord candidates, after duplicate removal.  If
\((u,v)\in D_n\), then \(u\in N_n(v)\) and \(c_{n,v}(u)\in N_n(v)\), so
\((v,c_{n,v}(u))\in D_n\).  For a fixed arrival vertex \(v\), the cyclic
successor is a permutation of the finite neighbour list, including the
one-neighbour identity.  Applying its inverse to the second coordinate gives
the displayed inverse.  The component label \(n\) is unchanged, hence the
disjoint union is bijective. \(\square\)

### Proposition 2 (same-object suspension completeness)

Every \(\sigma\)-orbit is a finite cycle with positive suspension period.  The
roofed suspension is complete along every orbit and has no finite-time Zeno
accumulation.

**Proof.**  Proposition 1 makes \(\sigma_n\) a permutation of finite \(D_n\),
so \(L(x)<\infty\).  Each summand of \(T([x])\) is positive, so \(T([x])>0\).
After each cycle the flow has advanced exactly \(T([x])\), and after \(r\)
cycles it has advanced \(rT([x])\to\infty\).  The same argument applies in
negative time using the inverse permutation.  The infimum of roof values over
all components may be zero, but a single trajectory never changes its finite
component. \(\square\)

### Corollary 3 (exact owner-level T2 ledger)

The candidate has an intrinsic primitive/repetition convention owned by the
same \((X,\sigma,\tau)\).  This establishes the general broadened T2 ledger,
but does not establish prime-only arithmetic selectivity.

## 5. Exact \(n=8\) ledger

For \(n=8\), the edges are

\[
 \{1,2\},\{2,3\},\{3,4\},\{4,5\},\{5,6\},\{6,7\},\{7,8\},
 \{1,8\},\{2,4\}.
\]

The increasing neighbour lists are

\[
\begin{array}{c|c}
v&N_8(v)\\ \hline
1&[2,8]\\
2&[1,3,4]\\
3&[2,4]\\
4&[2,3,5]\\
5&[4,6]\\
6&[5,7]\\
7&[6,8]\\
8&[1,7].
\end{array}
\]

There are \(18\) darts.  The following three cycles are disjoint and contain
all \(18\) darts, so the list is complete:

### Cycle (C_{8,3}): the divisor chord cycle

\[
 (2,4)\to(4,3)\to(3,2)\to(2,4).
\]

Its edge-ratio product (where
\(\rho(u,v)=\max(u,v)/\min(u,v)\) is

\[
 \rho(2,4)\rho(4,3)\rho(3,2)
 =2\cdot\frac43\cdot\frac32=4,
\]

and hence

\[
 L(C_{8,3})=3,qquad T(C_{8,3})=\frac12\log4=\log2.
\]

### Cycle (C_{8,8}): the forward backbone cycle

\[
 (1,2)\to(2,3)\to(3,4)\to(4,5)\to(5,6)\to(6,7)
 \to(7,8)\to(8,1)\to(1,2).
\]

The ratio product is

\[
 \left(\prod_{j=1}^{7}\frac{j+1}{j}\right)\frac81=8\cdot8=64,
\]

so \(L=8\) and \(T=\frac12\log64=\log8\).

### Cycle (C_{8,7}): the mixed chord/backbone cycle

\[
 (2,1)\to(1,8)\to(8,7)\to(7,6)\to(6,5)\to(5,4)
 \to(4,2)\to(2,1).
\]

Here

\[
 \rho(2,1)\rho(1,8)\rho(8,7)\rho(7,6)\rho(6,5)
 \rho(5,4)\rho(4,2)
 =2\cdot8\cdot\frac87\cdot\frac76\cdot\frac65\cdot\frac54\cdot\frac42
 =64,
\]

so \(L=7\) and \(T=\log8\).  Thus the canonical \(n=8\) ledger, in the
requested chord/forward/mixed order, is exactly

\[
 \boxed{[3,8,7]\quad\text{with}\quad[\log 2,\log 8,\log 8].}
\]

The two \(\log 8\) values are not repetitions of one another: they belong to
different primitive dart cycles of lengths \(8\) and \(7\).

## 6. Exact \(n=10\) control

For \(n=10\), the extra chords are \(\{1,10\}\) and \(\{2,5\}\), giving \(22\)
darts.  The increasing neighbour lists needed below are

\[
\begin{array}{c|c@{\quad}c|c}
1&[2,10]&2&[1,3,5]\\
3&[2,4]&4&[3,5]\\
5&[2,4,6]&6&[5,7]\\
7&[6,8]&8&[7,9]\\
9&[8,10]&10&[1,9].
\end{array}
\]

The \(22\) darts split into the following disjoint cycles:

\[
\begin{aligned}
 C_{10,4}:& (4,3)\to(3,2)\to(2,5)\to(5,4)\to(4,3),\\
 C_{10,10}:& (1,2)\to(2,3)\to(3,4)\to(4,5)\to(5,6)\to(6,7)\\
 &\qquad\to(7,8)\to(8,9)\to(9,10)\to(10,1)\to(1,2),\\
 C_{10,8}:& (2,1)\to(1,10)\to(10,9)\to(9,8)\to(8,7)\to(7,6)\\
 &\qquad\to(6,5)\to(5,2)\to(2,1).
\end{aligned}
\]

The first ratio product is

\[
 \frac43\frac32\frac52\frac54=\frac{25}{4},
 \quad T(C_{10,4})=\frac12\log\frac{25}{4}=\log\frac52.
\]

For the forward \(10\)-cycle the product is \(10\cdot10=100\), and for the
mixed \(8\)-cycle it is

\[
 2\cdot10\cdot\frac{10}{9}\frac98\frac87\frac76\frac65\frac52=100.
\]

Therefore

\[
 \boxed{[4,8,10]\quad\text{with}\quad
 [\log(5/2),\log10,\log10].}
\]

This is a control, not a second candidate or a parameter fit.

## 7. Composite-versus-prime obstruction

The smallest decisive collision already occurs at \(n=4\).  Its chord
\(\{1,4\}\) closes the backbone into a 4-cycle, and canonical scattering has
two oriented primitive dart cycles of length \(4\), each with roof time

\[
 \frac12\log\left(\frac21\frac32\frac43\frac41\right)=\log4.
\]

The prime \(p=2\) component has one degree-one-reflection cycle
 \((1,2)\to(2,1)\to(1,2)\) of time \(\log 2\).  The \(n=4\) cycle is not its
repetition: the least dart period in component \(4\) is \(4\), the component
label is invariant, and no orbit identification across \(n\) is part of the
carrier.  Calling it a second traversal of the \(p=2\) circle would violate
the frozen owner and primitive convention.

At \(n=8\), the cycle \(C_{8,3}\) has the same time \(\log 2\) as the prime
component but is again a distinct primitive in a distinct component.  The
additional \(\log 8\) cycle and the \(n=10\) \(\log(5/2)\) cycle show that the
obstruction is not only an accidental equal-time collision.

For a prime \(p\ge3\), the chord set has only \(\{1,p\}\), so the component is
the \(p\)-cycle and the scatter owns its two orientations.  Composite
components retain the same \(d=1\) closure and may have extra chords and
extra primitive cycles.  Thus “one orbit per prime” is not an invariant of the
full carrier; it would require deleting composite components or selecting
cycles, both forbidden repairs under this card.

## 8. Controls and adverse findings

### 8.1 Chord deletion

Delete every divisibility chord while retaining the backbone and increasing
local order.  The graph is the path \(1-2-\cdots-n\), and the scatter has one
cycle of dart length \(2(n-1)\) for \(n\ge3\) (one 2-cycle for \(n=2\)); its
time is \(\log n\).  Hence the visually appealing logarithmic time is already
generated by the backbone metric without divisibility.  This is a negative
source-selectivity control, not a modification of `CRS01`.

### 8.2 Label shuffle

Keep the unlabelled graph and its incidence/scatter, but replace the numerical
label entering the roof by an independent permutation \(\pi_n:V_n\to V_n\):

\[
 \tau_{\pi}((u,v))=\frac12\left|\log\frac{\pi_n(v)}{\pi_n(u)}\right|.
\]

The chord incidence is held fixed while the numerical clock is decorrelated
from the divisibility labels.  Any purported packet relation that survives
arbitrary such shuffles is not evidence for the declared arithmetic clock.
This control is not used to alter the exact \(n=8\) or \(n=10\) ledger.

### 8.3 Relation to prior controls 136, 217 and 225

* 136 uses factorization words and a nonbacktracking carrier; `CRS01` uses
  all interval vertices and local ribbon scattering.  No word orbit or clock
  is imported.
* 217 uses divisor-cover graphs on the divisor set of one integer and already
  stops because composite components have primitive returns.  `CRS01` retains
  the same integer component label but has a different graph and successor
  rule; the 217 theorem is a motivating negative control only.
* 225 uses Euclid/split-merge word graphs plus an engineered positive-
  dimensional terminal completion.  `CRS01` has no terminal completion,
  momentum fibre, or symplectic map; its groupoid carrier must not be called a
  lift of 225.

These comparisons reinforce, rather than repair, the present stop: changing
the graph architecture does not remove the full-carrier composite primitive
obligation.

### 8.4 Ownership and `PROVES_TOO_MUCH` controls

The finite permutation proof establishes only a combinatorial/groupoid owner.
It does not prove a natural arithmetic source, a target divisor, a trace
formula, or a quantum spectrum.  A unit-roof variant would erase the only
declared clock and is a separate control.  Selecting one dart phase, one
cycle per \(n\), or only prime-labelled components would make the result
depend on an external filter and is disallowed.

## 9. Gate assessment and decision

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| T0 | Same labelled graph family, σ, roof, groupoid and suspension relation; inverse proved | **ESTABLISHED** | No classical symplectic fields apply |
| T1 source / selectivity | Divisibility generates chords, but backbone-only and shuffled-label controls retain the clock; composites own primitives | **SCOPED FAIL / NOT ESTABLISHED** | No prime-selective endogenous mechanism survives the exact controls |
| T2 orbit/repetition | Every finite component is a permutation; \(n=8,10\) ledgers and \(rT\) repetition are exact | **ESTABLISHED, TARGET SELECTIVITY FAILS** | Full packet cannot be prime-only without forbidden filtering |
| T3 analytic owner | No same-object transfer operator, trace or determinant supplied | **NOT EVALUATED** | Do not start analytic construction after the T1/T2 stop |
| Classical A0/A1/A2 | No finite-dimensional symplectic base map or Route-A evidence contract is supplied | **NOT APPLICABLE** | Formal Route-A remains UNASSIGNED |
| Route B | No Route-A readiness or separate authorization | **NOT INVOKED** | Formal coordinates remain unassigned |

**Decision: stop / fork.**  Retain `CRS01` as a reusable negative control for
groupoid scattering.  Do not tune the cyclic order, delete composite cycles,
swap in a unit roof, or attach a symplectic fibre under this ID.  A genuinely
different arithmetic recurrence or a separately justified carrier must receive
a fresh candidate card before any further gate work.

## Reproducibility / evidence index

- [Frozen card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Exact checks and commands](evidence/README.md)

The evidence check is a finite exact enumeration at \(n=8,10\), with all
integer edge and dart lists generated from the displayed rules.  It is not a
global classification of every \(n\), and no external data are used.
