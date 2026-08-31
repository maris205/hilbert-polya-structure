# Totient-complement dynamics on squarefree divisor lattices

**Stage:** repaired proof spike after the independent algebraic hostile gate.  
**Disposition:** internal Stage-2 lead; no paper number is assigned.  
**External status:** `HOLD_EXTERNAL`.

## 1. Literal arithmetic map and support conjugacy

Let `P` be a nonempty finite set of primes, put

```text
n = product_(p in P) p,
F_n(d) = gcd(n, (n/d) phi(d))          (d | n),
```

and identify a divisor `d` with its support `S subseteq P`.  Give `P` the
directed Pratt relation

```text
q -> p  iff  p | q-1.
```

There are no loops, and every edge strictly decreases the prime, so this is a
DAG.  Write

```text
N(S) = {p in P : q -> p for some q in S}.
```

Squarefreeness and Euler's product formula give, prime by prime,

```text
p | (n/d)phi(d)
    iff p notin S or p | q-1 for some q in S.
```

Consequently the literal divisor map is conjugate to

```text
F(S) = (P \ S) union N(S).                              (1.1)
```

This identity is statewise; it is not an analogy with a Boolean network.

## 2. Explicit phase decoder and recurrent census

Let `x_p=1[p in S]` and use complemented bits `y_p=1-x_p`.  If
`Par(p)={q:q->p}`, then (1.1) is exactly

```text
y_p(t+1) = (1-y_p(t)) product_(q in Par(p)) y_q(t),      (2.1)
```

with the empty product equal to one.  In particular,

```text
y_p(t)y_p(t+1)=0                                        (2.2)
```

for every vertex and every time.

Let `Src` be the vertices with no incoming edge and put `s=|Src|`.  At a
source, (2.1) is simple toggling, so choose an arbitrary phase bit
`eta_r in {0,1}` and set

```text
y_r^0=eta_r,       y_r^1=1-eta_r.                       (2.3)
```

Process the remaining vertices in any topological order.  Once the two
parent phases are known, put

```text
A_p^epsilon = product_(q in Par(p)) y_q^epsilon,
y_p^0=A_p^1,       y_p^1=A_p^0.                         (2.4)
```

Because `Par(p)` is nonempty, (2.2) for any one parent implies
`A_p^0 A_p^1=0`.  Hence (2.4) satisfies both phase equations from (2.1):

```text
y_p^1=A_p^0(1-y_p^0),
y_p^0=A_p^1(1-y_p^1).
```

It is also the unique solution of those two equations when
`A_p^0 A_p^1=0`.  Thus every assignment of the `s` source phases has one and
only one extension to a recurrent two-phase state, and different assignments
remain different on the sources.

Every finite nonempty DAG has a source.  Its coordinate toggles, so no global
state is fixed.  Therefore the recurrent set consists of exactly

```text
2^s recurrent states = 2^(s-1) cycles of exact period two.              (2.5)
```

Equations (2.3)--(2.4) are the promised explicit phase decoder; the census
does not rely only on an existence induction.

## 3. The `h+1` entry bound

For a nonsource `p`, abbreviate

```text
A_p(t)=product_(q in Par(p)) y_q(t).
```

By (2.2), `A_p(t)A_p(t+1)=0`.  Expanding (2.1) twice therefore removes the
initial value of the coordinate:

```text
y_p(t+2)
  = A_p(t+1)(1-A_p(t)(1-y_p(t)))
  = A_p(t+1)                                             (3.1)
```

for every `t>=0`.  Indeed, if `A_p(t+1)=0` both sides vanish; if it is one,
then `A_p(t)=0` and both sides are one.  This two-step erasure identity is the
missing ingredient in the earlier proof sketch.

Let `delta(p)` be the maximum length of a directed path from a source to
`p`; sources have depth zero.  Source coordinates are two-periodic from time
zero.  Inductively assume every parent `q` is two-periodic from time
`delta(q)+1` onward.  For `t>=delta(p)+1`, both instances of (3.1) are valid
and

```text
y_p(t+2) = product_q y_q(t+1)
           = product_q y_q(t-1)
           = y_p(t).
```

The middle equality holds because
`t-1>=max_(q in Par(p))(delta(q)+1)`.  Hence `p` is two-periodic from time
`delta(p)+1`.  If `h=max_p delta(p)` is the longest directed-path length,
then the whole state satisfies `F^(t+2)=F^t` for every `t>=h+1`.  Thus every
orbit enters its two-cycle by time at most

```text
h+1.                                                     (3.2)
```

For `|P|=1`, `h=0` and the unique coordinate already toggles from time zero,
so (3.2) remains valid.  The argument is componentwise and therefore also
covers disconnected induced Pratt DAGs.  No sharpness claim is made for the
bound.

## 4. Every-target one-step fibres

Fix a target support `B subseteq P` and set `Z=P\B`.  For
`U subseteq P`, define the parent union

```text
Par(U) = {q in P : q -> p for some p in U}.
```

A target zero at `p in Z` forces the source bit `x_p=1` and every parent bit
`x_q=0`.  Thus all target-zero constraints jointly force `Z` to one and
`Par(Z)` to zero.  For `p in B`, the sole bad event is

```text
E_p = {x_p=1 and x_q=0 for every q in Par(p)}.
```

Apply inclusion--exclusion to these bad events.  An intersection indexed by
`T subseteq B` forces `Z union T` to one and `Par(Z union T)` to zero.  It is
empty when those forced sets intersect; otherwise all remaining coordinates
are free.  Consequently, for every target, including targets outside the
image,

```text
|F_n^(-1)(B)| =
  sum_(T subseteq B,
       (Z union T) intersect Par(Z union T)=empty)
    (-1)^|T| 2^(|P|-|Z union T|-|Par(Z union T)|).       (4.1)
```

This proves the formula and explicitly checks the forced-one/forced-zero
compatibility in every surviving summand.  When the target is not in the
image, (4.1) evaluates to zero by the same inclusion--exclusion identity; no
separate image assumption is hidden in the statement.

## 5. Exact audit and validity boundary

[`../scouting/algebraic/verify_algebraic_scout.py`](../scouting/algebraic/verify_algebraic_scout.py)
compares the integer divisor update with (1.1) at every state in three prime
sets of sizes five, six, and seven.  For `A02` it checks 224 states and 1,132
exact assertions, including the recurrent census, the `h+1` bound, and (4.1)
for every target.  Its frozen transcript is
[`../scouting/algebraic/CANONICAL.txt`](../scouting/algebraic/CANONICAL.txt).

The three profiles are

```text
(sources,recurrent,max tail,image,max fibre)
  (1,2,3,8,10), (2,4,4,17,8), (4,16,2,25,8).
```

Finite enumeration is falsification evidence only.  The all-parameter
results are proved by the statewise arithmetic factorisation, the explicit
phase decoder, the two-step erasure identity, and target-wise
inclusion--exclusion above.

## 6. Owner and portfolio boundary

Prime-chain and Pratt-height theory, Euler's product formula, signed Boolean
networks, topological propagation on a DAG, inclusion--exclusion, and generic
finite-map cycle/zeta conversion receive zero contribution credit.  The
bounded owner search recorded in
[`../phase1/HOSTILE_GATE_ALGEBRAIC_ROOT.md`](../phase1/HOSTILE_GATE_ALGEBRAIC_ROOT.md)
did not locate the literal arithmetic map or this combined theorem package;
that non-hit is not novelty or priority evidence.

The admissible residual is the specified divisor self-map together with its
literal support conjugacy, source-phase recurrent decoder, `h+1` entry bound,
and all-target fibre formula.  It is separated from P97, P100, P107, P128,
and P131 by both carrier and update, but remains a deliberately low-ceiling
short-paper candidate until the final five-way portfolio gate.
