# Independent Hostile Gate A: Hamming-weight diagonal translation

Decision: **`GREEN`**  
Findings: **0 Critical / 0 Major / 2 minor scope guards**  
External lifecycle: **`HOLD_EXTERNAL`**  
Date: 2026-09-03

## 1. Input isolation and review posture

I did not inspect or cite any `p160` author output for this candidate.  The
review starts only from the literal definition supplied to the gate:

$$
H_n=(\mathbb Z/n\mathbb Z)^n,\qquad
T_n(x)=x+\operatorname{wt}(x)\mathbf 1,qquad n\ge2,
$$

where $\operatorname{wt}(x)$ is the integer number of nonzero coordinates.
All arithmetic in the state update is modulo $n$.

The derivation status is `COHERENT AS STATED`; every theorem below is
`PROVABLE AS STATED`.  Exact enumeration is used for hostile falsification,
not as a replacement for proof.

## 2. Invariant object and strict diagonal reduction

The organizing invariant is the free diagonal-translation orbit

$$
\mathcal O(x)=\{x-c\mathbf1:c\in\mathbb Z/n\mathbb Z\}.
$$

Every orbit has exactly $n$ elements, because $x-c\mathbf1=x$ forces
$c=0$.  The update adds a diagonal vector, so it preserves every coordinate
difference $x_i-x_1$ and never leaves $\mathcal O(x)$.  Thus the reduction is
strict, not merely a lumping that forgets possible transitions.

Fix a target/anchor $y$ and put

$$
m_j(y)=\#\{i:y_i=j\},\qquad j\in\mathbb Z/n\mathbb Z.
$$

Then $m=(m_0,\ldots,m_{n-1})$ is a weak composition of $n$.  Write
$X_j=y-j\mathbf1$.  Since $X_j$ has $m_j$ zero coordinates,

$$
T_n(X_j)=y-j\mathbf1+(n-m_j)\mathbf1
        =X_{j+m_j}.
$$

Therefore the literal restriction of $T_n$ to this orbit is conjugate to

$$
g_m(j)=j+m_j\pmod n.                                    \tag{2.1}
$$

Changing the anchor cyclically rotates the profile and conjugates the phase
map.  No coordinate-label information is needed for dynamics inside one
diagonal orbit; label multiplicities re-enter global enumeration through the
multinomial $n!/\prod_jm_j!$.

## 3. Complete recurrent structure

### Lemma 3.1: cycles of a composition phase map

Let $C$ be a nontrivial directed cycle of (2.1).  Every $j\in C$ has
$m_j>0$.  Adding the clockwise increments around the cycle gives a positive
multiple of $n$, while

$$
\sum_{j\in C}m_j\le\sum_{j=0}^{n-1}m_j=n.
$$

Hence the sum is exactly $n$ and $m_j=0$ off $C$.  The lifted path winds once,
so it visits the positive support in clockwise order, and $m_j$ is exactly the
clockwise gap from $j$ to the next support point.  Conversely every support
subset with those gap labels produces one nontrivial cycle.

A phase is fixed precisely when $m_j=0$ or $m_j=n$.  Thus every phase graph
has zero positions as fixed points, may have at most one nontrivial cycle,
and cannot have a transient tree feeding a nontrivial cycle.

### Theorem 3.2: exact-period points and cycles

The fixed points of $T_n$ are the all-zero vector and all vectors with no
zero coordinate.  Therefore

$$
P_{n,1}=1+(n-1)^n.                                      \tag{3.1}
$$

For $2\le\ell\le n$, a period-$\ell$ state has an anchored positive support
containing phase zero.  Its clockwise gaps form a positive composition
$d_1+\cdots+d_\ell=n$, and the number of labelled states with that profile is
$n!/(d_1!\cdots d_\ell!)$.  Hence

$$
P_{n,\ell}
=\sum_{d_1+\cdots+d_\ell=n\atop d_i\ge1}
  \frac{n!}{d_1!\cdots d_\ell!}
=\ell!\,\left\{\begin{matrix}n\\\ell\end{matrix}\right\}. \tag{3.2}
$$

Every point counted in (3.2) has exact period $\ell$, not merely period
dividing $\ell$.  The exact numbers of cycles are

$$
C_{n,1}=1+(n-1)^n,\qquad
C_{n,\ell}=(\ell-1)!
\left\{\begin{matrix}n\\\ell\end{matrix}\right\}
\quad(2\le\ell\le n).                                  \tag{3.3}
$$

There are no other periods.

If $F_n=\sum_{\ell=1}^n\ell!\left\{\begin{smallmatrix}n\\\ell\end{smallmatrix}\right\}$
is the ordered Bell/Fubini number, then the recurrent-point census is

$$
|\operatorname{Rec}(T_n)|=(n-1)^n+F_n.                  \tag{3.4}
$$

The Stirling/surjection identity and ordered Bell terminology receive zero
credit; the residual statement is their forced occurrence in the literal
phase dynamics.

## 4. Sharp transient tail

Every transient phase eventually reaches a zero position.  Suppose a tail
contains $d$ positive positions before reaching that fixed point.  It cannot
contain every positive position: if it did, the sum of its increments would
be $n$, returning modulo $n$ to its start rather than reaching a distinct
zero.  Since a transient profile has at least one zero, it has at most $n-1$
positive positions.  Therefore

$$
\operatorname{depth}(x)\le n-2.                         \tag{4.1}
$$

For $n\ge3$, take the anchored profile

$$
(1,\ldots,1,2,1,0),
$$

with the $2$ in position $n-3$.  Starting at phase zero gives
$0\to1\to\cdots\to n-3\to n-1$, a tail of length $n-2$.
Every such profile is realized by labelled vectors.  For $n=2$ every point
is recurrent.  Thus the sharp maximum tail is

$$
\max_x\operatorname{depth}(x)=n-2\qquad(n\ge2).         \tag{4.2}
$$

## 5. Every-target one-step fibre

Fix $y\in H_n$ with profile $m_j=m_j(y)$.  A preimage must have the form
$x=y-k\mathbf1$, because coordinate differences are invariant.  Its weight
is $n-m_k$.  The equation $T_n(x)=y$ is therefore:

- $k=0$: possible exactly for $y=0$;
- $k=n$ (the same residue shift, but the distinct integer weight branch):
  possible exactly when $m_0=0$;
- $1\le k\le n-1$: possible exactly when $m_k=n-k$.

The $k=0$ and $k=n$ cases never hold simultaneously, so there is no duplicate
source.  The exact fibre is

$$
|T_n^{-1}(y)|=mathbf1_{y=0}+\mathbf1_{m_0=0}
+\sum_{k=1}^{n-1}\mathbf1_{m_k=n-k}.                    \tag{5.1}
$$

This includes every zero fibre and the exceptional $n=2$ system.

## 6. Global indegree enumerator and maximum fibre

Let

$$
I_n(u)=\sum_{y\in H_n}u^{|T_n^{-1}(y)|}.
$$

Multinomially marking $m_0=0$ and each event $m_k=n-k$ in (5.1) gives the
formal coefficient identity

$$
I_n(u)=(u-1)+n![z^n](e^z+u-1)
\prod_{r=1}^{n-1}\left(e^z+(u-1)\frac{z^r}{r!}\right). \tag{6.1}
$$

The correction $(u-1)$ changes the otherwise unmarked all-zero target from
degree zero to its special degree one.

Put

$$
h_n=\max\{h:h(h+1)/2\le n\}
=\left\lfloor\frac{\sqrt{8n+1}-1}{2}\right\rfloor.
$$

Every middle branch in (5.1) prescribes a distinct positive multiplicity.
If $h$ middle branches hold, their required counts have total at least
$1+\cdots+h$, so $h\le h_n$.  The full-support branch contributes at most one
more.  For $n\ge3$, impose the middle conditions of sizes $1,\ldots,h_n$ and
put the leftover $n-h_n(h_n+1)/2$ into the nonhit symbol $1$; this keeps
$m_0=0$ and realizes $1+h_n$ branches.  At $n=2$ the only nonzero symbol must
absorb the leftover and the two conditions cannot coexist.  Hence

$$
\max_y|T_n^{-1}(y)|=
\begin{cases}
1,&n=2,\\
1+h_n,&n\ge3.
\end{cases}                                             \tag{6.2}
$$

Formula (6.1) also gives the exact number of targets attaining the maximum,
not just the maximum value.

## 7. All-time target oracle: exact but supporting only

For fixed $y$, every possible source of a $t$-step preimage remains among the
$n$ states $X_j=y-j\mathbf1$.  From (2.1),

$$
|(T_n^t)^{-1}(y)|
=\#\{j\in\mathbb Z/n\mathbb Z:g_m^t(j)=0\}.             \tag{7.1}
$$

This is a genuine every-target, every-time oracle reducing an exponential
state search to an $n$-vertex functional graph.  Its generating series is
also explicit once that graph is traversed:

- if phase zero is transient, sum $z^{h(j)}$ over phases whose first hit of
  zero occurs at time $h(j)$;
- if phase zero has period $\ell$, sum
  $z^{h(j)}/(1-z^\ell)$ over its entire weak component.

This is exact, but it is not a closed global all-time fibre census: it still
requires traversing the target's phase graph.  Gate A therefore counts
(7.1) as a useful interface/supporting theorem, not as an independent third
contribution.  The independent second axis is instead the closed one-step
atlas (5.1), global enumerator (6.1), and extremum (6.2).

## 8. Hostile findings and mandatory scope guards

### Critical: none

No counterexample was found to the normalized contract above.

### Major: none

The temporal and inverse axes remain independent after the owner and
portfolio subtractions recorded separately.

### Minor 1: binary special case must be subtracted

Meyer--Pommersheim define, on binary words, the transform that keeps an
even-weight word and complements an odd-weight word.  Algebraically this is
$x+(\operatorname{wt}(x)\bmod2)\mathbf1$.  It directly owns the binary
weight-controlled diagonal translation mechanism.  In the coupled family
here, alphabet modulus and word length are both $n$, so that owner covers only
the degenerate $n=2$ member, not the $n\ge3$ composition phase theory.  A
future artifact must say this visibly and give $n=2$ no novelty credit.

### Minor 2: do not advertise (7.1) as a closed fibre formula

Equation (7.1) is a target-local oracle.  Calling it a closed all-time
enumerator would overstate the result.  It may be presented as a reduction or
algorithmic interface only.

## 9. Exact evidence

The independent verifier:

- exhausts every literal state for $2\le n\le7$;
- verifies the diagonal invariant, all periods/depths, every one-step fibre,
  and every $t$-step target fibre for $0\le t\le2n$;
- independently enumerates all weak compositions through $n=11$ with
  multinomial label weights;
- independently expands (6.1) through $n=30$;
- checks sharp-tail and maximum-fibre witnesses through $n=64$.

The frozen transcript reports `34,932,126` assertions and `RESULT=PASS`.
Two fresh invocations must byte-match `CANONICAL.txt` before this gate is
considered frozen.

## 10. Verdict

**`GREEN`**, with the two scope guards above.  The literal $n\ge3$ system has
a structurally specific occupancy-composition quotient, a full exact-period
and recurrent census, a sharp linear tail, and a closed target-resolved
one-step inverse distribution.  No internal map inspected has the same
carrier/update/inverse mechanism, and the bounded public search found no
direct owner for the coupled family.  This is not an absolute novelty claim;
external status remains `HOLD_EXTERNAL`.

