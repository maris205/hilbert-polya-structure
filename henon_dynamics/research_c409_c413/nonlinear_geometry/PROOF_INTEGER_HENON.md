# Rational cycles for every integral parameter of the conservative quadratic Hénon map

## Claim and current status

**Object.** For each $a\in\mathbb Z$, let
$$
H_a:\mathbb Q^2\longrightarrow\mathbb Q^2,
\qquad H_a(x,y)=(y,y^2+a-x).
$$
The Jacobian determinant is $+1$. The sign in front of $x$ is part of
the object and must not be replaced with $+x$ when comparing sources.

**Proof status: PROVABLE AS STATED.** The infinite-parameter reduction and
symbol classification below are direct proofs. Thirteen remaining small
parameters have an explicit exact finite-graph certificate in Section 6,
with the complete finite algorithm specified there and implemented in
`integer_henon_check.py`. This draft has not yet passed independent review
or the prior-work/substantiality admission gates. No C number is assigned.

**Classification theorem.** Every rational periodic orbit of $H_a$ is
integral. Up to cyclic rotation of the coordinate word, the following
table is the complete list, including all periods and all $a\in\mathbb Z$.
A word $(u_0,\ldots,u_{\ell-1})$ denotes the orbit of pairs
$(u_i,u_{i+1})$, with indices modulo $\ell$.

| Parameter | Coordinate words | Range and exact periods |
|---|---|---|
| $a=1-k^2$ | $(1-k)$ and $(1+k)$ | $k\geq0$; period $1$; the two words coincide when $k=0$ |
| $a=-k^2-3$ | $(-k-1,k-1)$ | $k\geq1$; period $2$ |
| $a=-k^2-1$ | $(-k-1,k,k)$ and $(k-1,-k,-k)$ | $k\geq0$; period $3$; the two words coincide when $k=0$ |
| $a=-k^2$ | $(-k,-k,k,k)$ | $k\geq1$; period $4$ |

If a parameter lies in two rows, the union is intended. There are exactly
two overlaps between nondegenerate rows: $a=-1$ has one orbit of period
$3$ and one of period $4$; $a=-4$ has one orbit of period $2$ and one of
period $4$. In particular,
$$
\#\operatorname{Per}(H_a,\mathbb Q)\leq 7,
$$
with equality exactly when $a=-1$. No rational periodic point has exact
period outside $\{1,2,3,4\}$.

The theorem concerns rational points of this fixed determinant-$+1$
integer-parameter family. It makes no claim about all rational parameters,
all Hénon maps, algebraic periodic points of unbounded degree, or the
determinant-$-1$ family.

## Assumptions, notation, and dependency map

Only $a\in\mathbb Z$ and periodicity over $\mathbb Q$ are assumed. For a
periodic coordinate sequence $(x_i)_{i\in\mathbb Z/n\mathbb Z}$ the defining
equations are
$$
x_{i-1}+x_{i+1}=x_i^2+a. \tag{1}
$$
No upper bound on $n$ is imposed. Repeated coordinates are allowed. The
map is an automorphism, with inverse $(x,y)\mapsto(x^2+a-y,x)$.

The proof has the following dependencies:

1. A nonarchimedean maximum in (1) proves integrality.
2. A real maximum bounds every periodic coordinate.
3. For $c=-a\geq13$, the nearest-square decomposition bounds each coordinate
   by six symbols; the parity of a leading coefficient separates two exact
   local equations.
4. A direct local classification of those equations gives all large-parameter
   cycles, without a numerical period cutoff or graph enumeration.
5. Thirteen small parameters are exhausted by a finite partial permutation
   graph, with a reproducible exact pruning table.
6. Direct substitution proves existence and exact periods; square-difference
   arithmetic gives the overlaps and sharp total bound.

No analytic height theorem, symbolic conjugacy theorem, or source counting
asymptotic is used as an unproved input. Prior-work attribution is a
separate admission gate currently being investigated by the coordinator.

## 1. Rational periodic points are integral

Fix a prime $p$ and write $M=\max_i|x_i|_p$. If $M>1$, choose $j$ with
$|x_j|_p=M$. Because $a\in\mathbb Z$, one has $|a|_p\leq1<M^2$ and hence
$$
|x_j^2+a|_p=M^2.
$$
But (1) and the nonarchimedean triangle inequality give
$$
|x_j^2+a|_p=|x_{j-1}+x_{j+1}|_p\leq M,
$$
a contradiction. Thus $|x_i|_p\leq1$ for every prime $p$ and every $i$.
Since $x_i$ is rational, this means $x_i\in\mathbb Z$.

## 2. Real bounds and the nonnegative parameter cases

Summing (1) around a period yields
$$
\sum_i(x_i-1)^2=n(1-a). \tag{2}
$$
Consequently $a>1$ has no real periodic orbit, and $a=1$ has just the
fixed point $(1,1)$.

It remains to treat $a\leq0$. Set $c=-a\geq0$ and
$R=\max_i|x_i|$, an integer. At an index attaining $R$,
$$
R^2-c=x_{i-1}+x_{i+1}\leq2R.
$$
Thus
$$
R\leq1+\sqrt{1+c},\qquad
|x_i^2-c|\leq2R\quad\hbox{for every }i. \tag{3}
$$
The latter bound follows from (1) at each index, not just at the maximum.

## 3. Uniform six-symbol reduction for every $c\geq13$

There is a unique integer $r\geq4$ with
$$
r^2-r+1\leq c\leq r^2+r.
$$
These intervals partition the integers beginning at $13$: the next lower
endpoint is $(r+1)^2-(r+1)+1=r^2+r+1$. Put
$$
s=c-r^2,\qquad 1-r\leq s\leq r. \tag{4}
$$

If $s\leq-2$, then $c+1<r^2$, so (3) and integrality imply $R\leq r$.
If $s\geq-1$, then $c+1\leq r^2+r+1<(r+1)^2$, so $R\leq r+1$.

We next exclude $|x_i|\leq r-2$. In the first case such a coordinate would
satisfy
$$
x_i^2-c\leq-4r+4-s\leq-3r+3<-2r\leq-2R,
$$
where the strict inequality uses $r\geq4$. In the second case it would
satisfy
$$
x_i^2-c\leq-4r+5<-2r-2\leq-2R.
$$
Both conclusions contradict (3). We have proved
$$
r-1\leq|x_i|\leq r+1.
$$
There are consequently unique symbols
$$
x_i=\varepsilon_i r+\delta_i,
\qquad \varepsilon_i\in\{-1,1\},\quad
\delta_i\in\{-1,0,1\}. \tag{5}
$$

Substituting (5) into (1) gives the exact identity
$$
r\bigl(\varepsilon_{i-1}+\varepsilon_{i+1}
       -2\varepsilon_i\delta_i\bigr)
=\delta_i^2-\delta_{i-1}-\delta_{i+1}-s. \tag{6}
$$
The coefficient multiplying $r$ is an even integer. By (4), the right
side lies in $[-r-2,r+2]$, whose absolute values are strictly less than
$2r$. Both sides of (6) must therefore vanish. We obtain
$$
\varepsilon_{i-1}+\varepsilon_{i+1}
   =2\varepsilon_i\delta_i, \tag{7}
$$
$$
\delta_{i-1}+\delta_{i+1}=\delta_i^2-s. \tag{8}
$$
In particular $s=\delta_i^2-\delta_{i-1}-\delta_{i+1}\in\{-2,-1,0,1,2,3\}$.
Every other value of $s$ admits no periodic orbit.

## 4. Complete periodic classification of the local symbol equations

Equation (7) has three consequences:

- If $\delta_i=1$, both neighboring signs equal $\varepsilon_i$.
- If $\delta_i=-1$, both neighboring signs equal $-\varepsilon_i$.
- If $\delta_i=0$, the two neighboring signs are opposite.

In particular, adjacent offsets $1$ and $-1$ are impossible: the first
offset would require the two adjacent signs to be equal, whereas the
second would require them to be opposite. This also applies across the
cyclic boundary and for periods $1$ and $2$.

### $s=-2$: no solution

Equation (8) requires $\delta_i^2+2\leq2$ for every $i$, so every offset
is zero. Substitution back into (8) gives $0=2$, a contradiction.

### $s=-1$: two fixed points

An offset $-1$ would require both neighboring offsets to be $1$, which
is forbidden. If an offset $0$ occurs, its two neighbors sum to $1$,
so one of them is $1$. At that neighboring $1$, equation (8) requires
both adjacent offsets to be $1$, contradicting the original $0$.
Thus all offsets are $1$. Equation (7) makes all signs equal. The only
coordinate words are $(1-r)$ and $(1+r)$.

### $s=0$: one four-cycle

An offset $-1$ would require neighboring offsets $0$ and $1$, again
forbidden. Among the remaining offsets $0,1$, a $0$ can only neighbor
$0$, whereas a $1$ requires one neighbor $0$ and one neighbor $1$.
Thus a $1$ cannot occur either. All offsets vanish, and (7) becomes
$\varepsilon_{i+1}=-\varepsilon_{i-1}$. Every sign sequence is therefore
$$
(u,v,-u,-v,u,v,-u,-v,\ldots),\qquad u,v\in\{-1,1\}.
$$
The four choices are cyclic rotations of $(-1,-1,1,1)$. The resulting
coordinate word is $(-r,-r,r,r)$, with exact period $4$.

### $s=1$: two three-cycles

If an offset $1$ occurs, its neighbors sum to zero. A neighboring $-1$
is forbidden, so both neighbors must be $0$. But a $0$ adjacent to $1$
would, by (8), require its other neighbor to be $-2$, impossible. Hence
all offsets lie in $\{-1,0\}$. Each $-1$ has two zero neighbors; each $0$
has one neighbor $-1$ and one neighbor $0$. Thus the offset sequence is
the repetition of $(-1,0,0)$.

Starting with $\varepsilon_i=u$ at an offset $-1$, the sign rules force
the next two signs to be $-u,-u$ and the following sign to be $u$.
The sign sequence has the same period $3$. For $u=-1$ and $u=1$ the two
coordinate words are respectively
$$
(-r-1,r,r),\qquad(r-1,-r,-r).
$$
Both have exact period $3$ and are distinct up to cyclic rotation.

### $s=2$: no solution

An offset $1$ would require neighboring offsets $-1$ and $0$, forbidden
by the sign rule. A zero offset would have two neighbors $-1$. Their
sign rules force both neighboring signs to be the negative of the
center sign, whereas the zero offset requires these signs to be
opposite. Thus neither $1$ nor $0$ can occur. If all offsets were $-1$,
equation (8) would read $-2=-1$, also impossible.

### $s=3$: one two-cycle

A zero offset would require its neighbors to sum to $-3$, impossible.
Each remaining offset has two neighbors $-1$. Offset $1$ is therefore
forbidden, and all offsets are $-1$. The signs alternate, giving
$(-r-1,r-1)$ with exact period $2$.

This completes the classification for every $c\geq13$. It is not a
classification of arbitrary real symbolic itineraries: equations
(5)--(8) were derived from exact integral coordinates.

## 5. Existence and nondegeneracy of all listed families

For the fixed word $x=1\pm k$ and $a=1-k^2$, one has $x^2+a=2x$.
For the period-two word at $a=-k^2-3$,
$$
(-k-1)^2+a=2(k-1),\qquad (k-1)^2+a=2(-k-1).
$$
For the first period-three word at $a=-k^2-1$,
$$
(-k-1)^2+a=2k,\qquad k^2+a=-1=(-k-1)+k.
$$
For the second word, $(k-1)^2+a=-2k$ and
$(-k)^2+a=-1=(k-1)+(-k)$. Finally, for the period-four word at $a=-k^2$,
each coordinate square plus $a$ vanishes, as does the sum of its two
neighbors. These computations verify (1) for every word in the table.

For $k\geq1$ the two coordinates of the period-two word are distinct.
The period-three words have unequal first and second entries for every
integer $k\geq0$, so have exact period $3$; they coincide only at $k=0$.
For $k\geq1$, the period-four word has neither period $1$ nor period $2$.
The fixed words coincide only at $k=0$. These observations explain every
range and degeneracy recorded in the theorem.

## 6. Exact finite certificate for $0\leq c\leq12$

For a specified $c$, define, using integer arithmetic only,
$$
B_c=1+\lfloor\sqrt{1+c}\rfloor,\qquad
S_c=\{u\in\mathbb Z:|u|\leq B_c, |u^2-c|\leq2B_c\}.
$$
By (3), every periodic pair lies in $V_0=S_c\times S_c$. Define
$$
V_{j+1}=\{(x,y)\in V_j:(y,y^2-c-x)\in V_j\}. \tag{9}
$$
Every periodic pair lies in every $V_j$. The sets decrease and are finite,
so eventually stabilize. On the stable set $V_*$ the injective map $H_{-c}$
is a permutation, hence every point of $V_*$ is periodic. Thus $V_*$ is
exactly the complete periodic set; this argument does not impose a
maximum period. It is enough to perform the finite integer tests in (9).

The following table gives every cardinality up to stabilization and the
resulting cycles. A terminal zero means the stable set is empty. The
last entry in a cardinality list is unchanged by one more application
of (9). The initial sets are specified above, so no choices or numerical
tolerances enter this certificate.

| $c$ | $B_c$ | $|V_0|,|V_1|,\ldots,|V_*|$ | Stable coordinate words |
|---|---|---|---|
| $0$ | $2$ | $25,15,10,8,7,6,5,4,3,2$ | $(0)$; $(2)$ |
| $1$ | $2$ | $25,18,14,12,10,9,8,7$ | $(-1,0,0)$; $(-1,-1,1,1)$ |
| $2$ | $2$ | $25,17,12,8,7,6$ | $(-2,1,1)$; $(-1,-1,0)$ |
| $3$ | $3$ | $49,28,18,11,8,6,4,2$ | $(-1)$; $(3)$ |
| $4$ | $3$ | $49,29,18,14,12,10,8,6$ | $(-2,0)$; $(-2,-2,2,2)$ |
| $5$ | $3$ | $49,26,16,9,8,7,6$ | $(-3,2,2)$; $(-2,-2,1)$ |
| $6$ | $3$ | $49,23,12,6,2,0$ | none |
| $7$ | $3$ | $36,12,6,3,2$ | $(-3,1)$ |
| $8$ | $4$ | $81,33,14,6,2$ | $(-2)$; $(4)$ |
| $9$ | $4$ | $64,30,14,12,10,8,6,4$ | $(-3,-3,3,3)$ |
| $10$ | $4$ | $36,20,12,6$ | $(-4,3,3)$; $(-3,-3,2)$ |
| $11$ | $4$ | $36,12,6,4,2,0$ | none |
| $12$ | $4$ | $36,4,2$ | $(-4,2)$ |

All these words occur in the theorem's families. Together with Sections
1--5 and the case $a=1$ in Section 2, this proves completeness for every
integer parameter. The accompanying exact checker verifies the full sets,
not only the cardinalities in the table. It also compares this pruning
method with a separate orbit-path enumeration.

## 7. Parameter overlaps, the sharp bound, and a native zeta corollary

For $c\geq0$ the four families have the forms $k^2-1$, $k^2+3$,
$k^2+1$, and $k^2$, with the ranges already stated. Equality between two
forms reduces to a difference of squares equal to $1$, $2$, $3$, or $4$.
The difference $2$ is impossible for integer squares. Factoring the
other differences gives, after excluding the degenerate $k=0$ two- and
four-cycle words, only $c=1$ and $c=4$ as intersections of distinct rows.
The fixed family is disjoint from every other nondegenerate row.

Thus ordinary three-cycle parameters have six rational periodic points;
$a=-1$ has $3+4=7$, and $a=-4$ has $2+4=6$. Every remaining parameter
has at most four. The sharp bound and its equality case follow.

For completeness, let $F(a),T(a),C(a),Q(a)$ be respectively the numbers
of exact cycles of lengths $1,2,3,4$ in the classification table, with
coincident words counted only once. For every native integer time $n\geq1$,
$$
\#\operatorname{Fix}(H_a^n,\mathbb Q)
=F(a)+2T(a)\mathbf1_{2\mid n}
       +3C(a)\mathbf1_{3\mid n}+4Q(a)\mathbf1_{4\mid n}.
$$
The rational-point Artin--Mazur series is therefore
$$
\exp\left(\sum_{n\geq1}\frac{z^n}{n}
                    \#\operatorname{Fix}(H_a^n,\mathbb Q)\right)
=\frac{1}{(1-z)^{F(a)}(1-z^2)^{T(a)}(1-z^3)^{C(a)}(1-z^4)^{Q(a)}}.
$$
This is a finite-orbit source identity, not a target arithmetic Euler
product, automorphy statement, zero correspondence, or Hilbert--Pólya
realization. It is a corollary of the classification and is not a second
paper contract.

## Open risks and admission boundary

- A non-author must independently check the six-symbol proof and the full
  finite sets in Section 6. The present status is the author's proof claim.
- Exact prior ownership of this determinant-$+1$, integer-parameter,
  all-rational-periods classification remains under independent search.
- Proving a bounded-height census for a finite parameter sample would not
  suffice; the claimed infinite-parameter part is specifically Sections
  3--4. Conversely, this result says nothing about nonintegral rational
  parameters without a new argument.
- A complete proof does not itself decide the batch's substantiality gate.
  The standalone question here is the full parameter-and-period
  classification, not the near-square four-cycle pilot or its zeta alone.
