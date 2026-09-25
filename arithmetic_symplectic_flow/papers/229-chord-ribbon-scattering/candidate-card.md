# Broadened candidate card — chord-ribbon scattering

**Candidate ID:** `ANG-20260918-CRS01`
**Paper ID:** `229-chord-ribbon-scattering`
**Version:** 1; frozen 2026-09-18 before the exact orbit audit.
**Initial status:** `FROZEN HYPOTHESIS — T0/T1/T2 AUDIT OPEN`.
**Carrier type:** arithmetic noncommutative/groupoid (`ANG`); it is not a
finite-dimensional symplectic map unless a separate lift is actually built.
**Classical A0/A1/A2:** `NOT APPLICABLE`. **Formal Route-A:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## 1. Frozen carrier and arithmetic graph

For each integer \(n\ge 2\), freeze the labelled vertex set

\[
 V_n=\{1,2,\ldots,n\}.
\]

The simple undirected edge set \(E_n\) is the union of

1. backbone edges \(\{j,j+1\}\), \(1\le j<n\);
2. divisibility chords \(\{d,n/d\}\) for every \(d\mid n\) with
   \(d<\sqrt n\).

An edge already present in the backbone is retained only once.  Chords are
not added for \(d=\sqrt n\), so a square contributes no loop.  The component
label \(n\) is part of the carrier and is never quotiented by graph
isomorphism.  Let

\[
 D_n=\{(u,v):\{u,v\}\in E_n\},\qquad
 X=\bigsqcup_{n\ge2}D_n.
\]

At a vertex \(v\), list its neighbours in increasing integer order.  For an
incoming dart \((u,v)\), let \(c_v(u)\) be the cyclic successor of \(u\) in
that list; when \(v\) has degree one, this successor is the sole neighbour
(a reflection).  Freeze

\[
 \sigma_n(u,v)=(v,c_v(u)),\qquad \sigma=\bigsqcup_{n\ge2}\sigma_n.
\]

The owner is the transformation groupoid
\[
 \mathcal G=X\rtimes_\sigma\mathbb Z,
\]
with its discrete arrow structure.  The associated roofed suspension is the
groupoid/suspension object obtained from
\((x,t+\tau(x))\sim(\sigma x,t)\), \(x\in X\), \(t\in\mathbb R\),
using the representative \(0\le t<\tau(x)\).

## 2. Frozen clock and permitted data

The sole roof is

\[
 \tau((u,v))=\frac12\left|\log\frac vu\right|.
\]

Every graph edge has \(u\ne v\), hence \(\tau>0\) pointwise.  The roof is
not replaced by a unit roof in the candidate.  It has no uniform lower bound
over all \(n\), because backbone edges at large \(j\) have
\(\frac12\log(1+1/j)\to0\); nevertheless every σ-orbit stays in one finite
component (D_n), is periodic, and has positive cycle time, so its own
forward/backward suspension trajectory is complete and non-Zeno.

Allowed inputs are integer equality, divisibility, order, the fixed graph
rule, and the natural logarithm in the declared roof.  Prime tables,
von-Mangoldt weights, Riemann-zero data, fitted per-prime parameters and
external labels are prohibited.  A unit roof is a separate control, not a
normalization of this object.

## 3. Lineage and ownership contract

The documented lineage is

```text
prime/composite observables
  -> divisibility admissibility and symbolic darts
  -> deterministic local scattering on a finite ribbon graph
  -> broadened groupoid suspension carrier.
```

This realizes the source-to-symbolic and symbolic-to-broadened-carrier
arrows only.  No sequential deformation, Logistic/Hénon conjugacy,
positive-dimensional symplectic lift, Hamiltonian/contact realization,
transfer operator or determinant is asserted.  The relation to papers 136,
217 and 225 is a control comparison, not an inherited theorem or source lock.

The same frozen object must own the arithmetic graph, σ, the roof, the
primitive dart cycles, and their repetitions.  A later operator or geometric
lift would require a fresh candidate ID if it changed the carrier or clock.

## 4. Orbit convention and precommitted discriminators

Primitivity means least positive period of a dart under σ.  Cyclic phase
choices on one σ-cycle are identified; different \(n\)-labels, orientations,
or cycles of equal roof time are not identified.  A flow repetition traverses
the same primitive cycle \(r\) times and has time \(rT\).  The full finite
ledger, not a selected representative or section, is required.

The first exact tests are:

1. prove the inverse of the local successor scatter and the groupoid owner;
2. compute \(n=8\) and \(n=10\) with the canonical increasing orders;
3. test prime, prime-power and squarefree composite labels;
4. compare 136/217/225, chord deletion, and label-shuffle controls;
5. stop if a composite owns a primitive cycle not forced to be a repeat of a
   prime packet, or if the arithmetic source is indistinguishable from a
   nonarithmetic graph rule.

The expected stop is a T2 packet-selectivity failure.  No route language is
to be issued from the finite audit, and no symplectic lift is to be invented
after the stop.

## 5. Appended exact audit — version-1 object unchanged

**Current status:** **STOP — T2 ORBIT LEDGER ESTABLISHED, BUT T1 SOURCE
SELECTIVITY FAILS.**

For every \(n\), the finite dart map is a permutation with inverse
\[
 \sigma_n^{-1}(v,w)=(c_v^{-1}(w),v).
\]
The \(n=8\) ledger is

| primitive cycle (one phase representative) | dart length | roof time |
| --- | ---: | ---: |
| \((2,4)\to(4,3)\to(3,2)\) | 3 | \(\log 2\) |
| \((1,2)\to(2,3)\to\cdots\to(8,1)\) | 8 | \(\log 8\) |
| \((2,1)\to(1,8)\to(8,7)\to\cdots\to(4,2)\) | 7 | \(\log 8\) |

The \(n=10\) control has lengths \([4,8,10]\) and times

\[
 [\log(5/2),\log 10,\log 10].
\]

Thus a composite component has intrinsic primitive cycles, and the \(n=8\)
cycle of time \(\log 2\) is not the \(p=2\) orbit or its repetition: component
labels are invariant under σ.  T2 is complete as a same-object finite orbit
ledger, but prime-only packet selectivity fails at T1.  T3 is not entered;
classical A0/A1/A2 are NOT APPLICABLE, formal Route-A remains UNASSIGNED, and
Route B remains NOT INVOKED.
