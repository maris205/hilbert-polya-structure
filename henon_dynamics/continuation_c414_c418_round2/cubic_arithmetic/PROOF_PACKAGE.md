# Proof package: the full integral conservative cubic

## Claim

Let $a,b,c\in\mathbb Z$, put $f(t)=t^3+bt^2+ct+a$, and let
$$H_f(x,y)=(y,f(y)-x).$$
All rational periodic points are integral. Their complete list of cycles
is the seven-row template list below. In particular:

1. Every cycle uses at most three distinct coordinate values.
2. Every least period belongs to $\{1,2,3,4,6\}$, and all five periods
   occur somewhere in this full family.
3. There are at most eleven rational periodic points in total.
4. Equality holds if and only if, for some $h\in\mathbb Z$,
   $$f(t)=(t-h)^3-5(t-h)+2h.$$

The word $(v_0,\ldots,v_{n-1})$ denotes the cycle of points
$(v_i,v_{i+1})$, with indices modulo $n$. Words are identified under
cyclic rotation, not reversal. A listed polynomial identity is required
as an identity in $\mathbb Z[t]$, not just at sampled points. Take the
union of all rows that apply to the given polynomial.

| Least period | Coordinate word(s) and integer ranges | Exact condition on $f$ |
|---|---|---|
| $1$ | $(u)$, $u\in\mathbb Z$ | $f(u)=2u$ |
| $2$ | $(u,v)$, $u<v$ | With $S=u+v$, $f(t)=-2t+2S+(t-u)(t-v)(t+S+b)$ |
| $3$ | $(u,u,v)$, $u\ne v$ | With $S=u+v$, $f(t)=-t+(2u+v)+(t-u)(t-v)(t+S+b)$ |
| $3$ | $(u,v,w)$ and $(u,w,v)$, $u<v<w$ | With $S=u+v+w$, $f(t)=-t+S+(t-u)(t-v)(t-w)$ |
| $4$ | $(u,u,v,v)$, $u<v$ | With $S=u+v$, $f(t)=S+(t-u)(t-v)(t+S+b)$ |
| $4$ | $(h-k,h,h+k,h)$, $h\in\mathbb Z$, $k\ge1$ | $f(t)=2h+(t-h)((t-h)^2-k^2)$ |
| $6$ | $(h-k,h-k,h,h+k,h+k,h)$, $h\in\mathbb Z$, $k\ge1$ | $f(t)=t+h+(t-h)((t-h)^2-k^2)$ |

All parameters in each row are integers. In the three-distinct-symbol
period-three row the identity includes $b=-(u+v+w)$; no additional free
quadratic coefficient is hidden. The displayed inequalities prevent
degeneration to lower periods. Different rows of the same period have
different numbers of symbols and cannot describe the same orbit.

## Status

`PROVABLE AS STATED — exact finite graph certificate is part of the proof`.
This is the author's proof package, pending independent mathematical and
source review. It is not an admission, manuscript or formal evaluation.

The global reduction and the cycle-template derivation are analytic.
One explicitly bounded finite lemma is proved by complete integer graph
enumeration, implemented in [certify_cubic.py](certify_cubic.py). The
script computes extrema of all admitted graph counts, rather than taking
eleven as a prefilled assertion. It performs no floating-point test or
period cutoff. The earlier coefficient scout is not used in this proof.

## Assumptions, notation and boundaries

The coefficient of $t^3$ is exactly $+1$, every coefficient is integral,
and the Jacobian determinant of $H_f$ is $+1$. The domain is all
$\mathbb Q^2$; time is ordinary iteration by $H_f$. Points have unit
weight. Neither scheme lengths nor any quotient by orientation is used.
The inverse is $(x,y)\mapsto(f(x)-y,x)$, so there are no strictly
preperiodic points.

Let $\mathcal P$ be the set of all rational periodic points of this one
map. When nonempty, let $E$ be the union of **all coordinates of all
points in $\mathcal P$**. The extrema below are not chosen separately
for one cycle. This distinction is essential for the total-point bound.

The integer translation used in the proof is an internal device; it does
not restrict $b$ to a chosen residue class or shrink the original family.
No assertion is made for nonmonic cubics, rational nonintegral
coefficients, determinant $-1$, arbitrary degree, number fields, or
positive characteristic.

## Proof strategy and dependency map

1. An ultrametric maximum proves integrality; a real maximum proves that
   $\mathcal P$ is finite.
2. Its global extrema give a cubic with two known integer secant roots
   and therefore an integer third root. The error from the secant is at
   most twice the global diameter.
3. For large diameter this leaves either the three roots, where the
   recurrence is affine, or five bounded endpoint cases. Their graphs
   are computed over $\mathbb Z[D]$, uniformly for every $D\ge16$.
4. The same inequality bounds the remaining small-diameter parameter
   set. A complete finite graph lemma gives the sharp maximum and
   three-symbol/period restrictions.
5. Elementary word combinatorics and an integer reciprocal lemma turn
   those restrictions into the exact cycle-template list.
6. The unique finite equality certificate gives the unique translated
   eleven-point polynomial; explicit cycles prove sufficiency.

No theorem from an unread source is a dependency. Classical arithmetic
finiteness, period bounds and interpolation are deducted in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## Proof

### 1. Integrality and a finite global periodic set

A periodic orbit has a cyclic coordinate sequence $(x_i)$ satisfying
$$x_{i-1}+x_{i+1}=f(x_i). \tag{1}$$
For a prime $p$, suppose $T=\max_i|x_i|_p>1$. Choose $i$ attaining
$T$. Integrality of the coefficients implies that $x_i^3$ has
$p$-adic absolute value $T^3$, strictly larger than the absolute values
of all lower terms. Hence $|f(x_i)|_p=T^3$, whereas the left side of
(1) has absolute value at most $T$. This contradiction holds for every
$p$. Thus each rational $x_i$ is integral.

At the real absolute value, $M=\max_i|x_i|$ satisfies
$$M^3\le |b|M^2+(|c|+2)M+|a|.$$
For $M\ge1$ the right side is at most
$(|a|+|b|+|c|+2)M^2$. Thus every such orbit has
$$M\le R:=|a|+|b|+|c|+2.$$
Consequently $\mathcal P\subseteq([-R,R]\cap\mathbb Z)^2$ and is
finite. This establishes the legitimacy of taking extrema over the
whole periodic set. Empty $\mathcal P$ satisfies all bounds. If $E$
has one element, $\mathcal P$ consists of its one diagonal fixed point.

### 2. The global secant identity

Now suppose $E$ has at least two elements. Put $m=\min E$,
$D=\max E-m\ge1$, and translate every coordinate by $-m$. The new
polynomial and map are
$$g(t)=f(t+m)-2m,\qquad H_g=T_{-m}H_fT_m,$$
where $T_m(x,y)=(x+m,y+m)$. The translated global coordinate set
$E'=E-m$ has extrema $0,D$ and lies in $\{0,\ldots,D\}$.

For every $t\in E'$, its occurrence in a cycle gives
$$0\le g(t)\le2D.$$
Set
$$A=g(0),\qquad q=\frac{g(D)-g(0)}D.$$
Since $g\in\mathbb Z[t]$, $q\in\mathbb Z$. The endpoint inequalities
give
$$-2\le q\le2,\quad 0\le A\le2D,\quad0\le A+qD\le2D. \tag{2}$$
The monic cubic $g(t)-A-qt$ vanishes at $0$ and $D$. Its third root
is an integer $r$: if $B$ is the quadratic coefficient of $g$, then
$r=-B-D$. Thus
$$g(t)=A+qt+t(t-D)(t-r). \tag{3}$$
The line $A+qt$ interpolates the two endpoint values, so it belongs
to $[0,2D]$ for every real $t\in[0,D]$. Subtracting two numbers in
this interval yields the decisive inequality
$$|t(t-D)(t-r)|\le2D\qquad(t\in E'). \tag{4}$$
This estimate uses the entire periodic set. In particular, every
coexisting cycle is represented in the same $D,r,A,q$ graph.

### 3. Affine-root cases and the smallest diameters

If $E'\subseteq\{0,D,r\}$, equation (3) restricts to
$$x_{i+1}=A+qx_i-x_{i-1}. \tag{5}$$
There are at most nine possible ordered coordinate pairs.

For $q\ne2$, subtract the stationary value $A/(2-q)$. The homogeneous
matrix is
$$L_q=\begin{pmatrix}0&1\\-1&q\end{pmatrix}.$$
For $q=-1,0,1$, direct multiplication gives respectively
$L_q^3=I$, $L_q^4=I$ and $L_q^6=I$. For $q=-2$, every homogeneous
solution is $(\alpha+\beta i)(-1)^i$, and periodicity forces
$\beta=0$, giving period one or two. For $q=2$, summing (5) around
a cycle forces $A=0$; its first differences are then constant and
periodicity forces the sequence itself to be constant. Hence every
least period in (5) lies in $\{1,2,3,4,6\}$.

This also treats any case in which $E'$ has only the two endpoints,
regardless of $r$. In particular $D=1$ has at most four points and
no missing boundary case. The earlier one-symbol case treats $D=0$.

### 4. The complete large-diameter alphabet

Suppose $D\ge10$ and $t\in E'\setminus\{0,D,r\}$. All factors in
(4) are integers, so $|t-r|\ge1$. If $3\le t\le D-3$, then
$$t(D-t)\ge3(D-3)>2D,$$
contradicting (4). Thus the only possible extra symbols are
$1,2,D-2,D-1$. At the lower endpoint (4) gives
$$|1-r|\le\left\lfloor\frac{2D}{D-1}\right\rfloor=2,
\qquad
|2-r|\le\left\lfloor\frac D{D-2}\right\rfloor=1.$$
Therefore lower extras require $r\in\{-1,0,1,2,3\}$; upper extras
require $D-r\in\{-1,0,1,2,3\}$. These two ranges are disjoint for
$D\ge10$.

The reflection $t=D-z$ conjugates the map to the polynomial
$$\widetilde g(z)=2D-g(D-z)
=\widetilde A+qz+z(z-D)(z-\widetilde r),$$
where
$$\widetilde r=D-r,\qquad \widetilde A=(2-q)D-A.$$
It preserves integrality, least periods and point counts. It is
therefore enough to treat the lower range. If neither range occurs,
Section 3 applies. In the lower range every possible symbol lies in
$S_r=T_r\cup\{D\}$, where

| $r$ | $T_r$ |
|---|---|
| $-1$ | $\{0,1\}$ |
| $0$ | $\{0,1\}$ |
| $1$ | $\{0,1,2\}$ |
| $2$ | $\{0,1,2\}$ |
| $3$ | $\{0,1,2,3\}$ |

This list retains all allowed $\pm1$ and $\pm2$ deviations; it does not
assume that every symbol equals a secant root.

### 5. A genuinely uniform graph over $\mathbb Z[D]$

Assume $D\ge16$ in one of these five cases. Since $0$ and $D$ are
actual coordinates, their images are sums of two symbols in $S_r$.
Write each such sum uniquely as $kD+s$, where $k\in\{0,1,2\}$ and
$0\le s\le6$. Let $\Sigma_r$ be the set of coefficient pairs
$(k,s)$ arising from these sums. We must have
$$A=kD+s,\qquad(k,s)\in\Sigma_r,
\qquad(k+q,s)\in\Sigma_r. \tag{6}$$
The last condition follows from $g(D)=A+qD\in S_r+S_r$:
different constant terms differ by at most six, less than $D$.

For a small symbol $t\in T_r$, equation (3) reads
$$g(t)=[k-t(t-r)]D+[s+qt+t^2(t-r)], \tag{7}$$
and $g(D)=(k+q)D+s$. An edge $(x,t)\mapsto(t,z)$ exists precisely
when $g(t)=x+z$. For $x,z\in S_r$, the constant term of their sum
lies between zero and $2\max T_r$. In (7), the absolute discrepancy
between the two constant terms is at most $14$ for all five cases.
This can be checked without the graph computation: for $r=-1,0,1,2,3$
the bounds obtained from $s,u\in[0,2\max T_r]$, $q\in[-2,2]$ and
$t\in T_r$ are respectively $6,5,12,8,14$. For $t=D$ the bound is
at most six. Thus a numeric edge equality for $D\ge16$ is equivalent
to equality of both integer coefficients of $D$ and $1$.

Consequently these are literal finite graphs over $\mathbb Z[D]$,
not graphs checked at a large representative value. Every map with
any $D\ge16$ is covered by exactly the applicable symbolic case or
the affine-root case. The threshold sixteen is a convenient sufficient
cutoff; it is not asserted to be optimal.

The endpoint-compatible symbolic graphs have the following exhaustive
certificate. Maxima in this table include all graph cycles, even in
parameter cases whose resulting graph does not use both extrema.

| $r$ | Pairs $(A,q)$ from (6) | Graph cases using $0,D$ | Maximum points | Least periods appearing | Maximum symbols per cycle |
|---|---:|---:|---:|---|---:|
| $-1$ | $14$ | $5$ | $4$ | $1,2,3,4$ | $2$ |
| $0$ | $14$ | $5$ | $4$ | $1,2,3,4$ | $2$ |
| $1$ | $19$ | $6$ | $6$ | $1,2,3,4$ | $3$ |
| $2$ | $19$ | $7$ | $8$ | $1,2,3,4$ | $3$ |
| $3$ | $24$ | $6$ | $6$ | $1,2,3,4$ | $3$ |

There are ninety symbolic cases in total. Here is a compact full list
of the graphs using both extrema, which also permits manual checking
of the reported maxima. In every row $r\in\{-1,0,1,2,3\}$ the five
baseline cases are

| $A$ | $q$ | All graph cycles |
|---|---:|---|
| $0$ | $2$ | $(0),(D)$, and $(r)$ when $r=1,2,3$ |
| $D$ | $-1$ | $(0,0,D)$ |
| $D$ | $0$ | $(0,0,D,D)$ |
| $2D$ | $-2$ | $(0,D)$ |
| $2D$ | $-1$ | $(0,D,D)$ |

There are only these additional cases:

| $r$ | $A$ | $q$ | All graph cycles |
|---|---|---:|---|
| $1$ | $D+1$ | $-1$ | $(0,1,D),(0,D,1)$ |
| $2$ | $2$ | $0$ | $(1,1,D),(0,0,2,2)$ |
| $2$ | $D+2$ | $-1$ | $(1,D),(0,2,D),(0,D,2)$ |
| $3$ | $D+3$ | $-1$ | $(0,3,D),(0,D,3)$ |

In particular the $r=2,A=2,q=0$ row supplies four coordinate values
in the full periodic set. It would be lost by the incorrect claim
that the full periodic set has at most three symbols. These displayed
cycles already give seven points, distributed among a three-cycle
and a four-cycle. Calling $0,D$ the graph endpoints does not certify
the absence of other cycles outside the displayed interval; this is
only a necessary filter. When applying the bounds to the original
map, $0,D$ were chosen from its entire periodic set in Section 2,
so all of its cycles are inside the applicable graph.

### 6. The complete small-diameter complement

It remains to treat $2\le D\le15$ outside the two-symbol case. At
least one $t\in E'\cap\{1,\ldots,D-1\}$ exists. Equation (4) gives
$$|t-r|\le\frac{2D}{t(D-t)}\le\frac{2D}{D-1}\le4,$$
so
$$-3\le r\le D+3. \tag{8}$$
This is why the remaining integer parameter set is finite. The exact
ranges are
$$2\le D\le15,\quad -3\le r\le D+3,\quad0\le A\le2D,
\quad q\in\{-2,-1,0,1,2\},\quad0\le A+qD\le2D. \tag{9}$$
For each tuple use the symbol set
$$S=\{0\le t\le D:t\in\mathbb Z,
\ |t(t-D)(t-r)|\le2D\}$$
and the partial graph
$$ (x,y)\longmapsto(y,A+qy+y(y-D)(y-r)-x) \quad\hbox{on }S^2. \tag{10}$$
Every actual periodic point is a vertex of a cycle of this graph.
Conversely every graph cycle is an actual cycle of the polynomial map.
Only tuples for which the union of graph cycles contains both $0$
and $D$ need be retained: all actual global-extrema tuples satisfy
this condition. This filter cannot discard an actual periodic set.

The complete certificate is:

| $D$ | Endpoint-compatible tuples | Tuples with both graph endpoints | Maximum graph-periodic points | Least periods appearing |
|---|---:|---:|---:|---|
| $2$ | $117$ | $51$ | $9$ | $1,2,3,4,6$ |
| $3$ | $170$ | $56$ | $9$ | $1,2,3,4$ |
| $4$ | $231$ | $63$ | $11$ | $1,2,3,4,6$ |
| $5$ | $300$ | $68$ | $8$ | $1,2,3,4$ |
| $6$ | $377$ | $75$ | $9$ | $1,2,3,4,6$ |
| $7$ | $462$ | $78$ | $8$ | $1,2,3,4$ |
| $8$ | $555$ | $85$ | $9$ | $1,2,3,4,6$ |
| $9$ | $656$ | $90$ | $8$ | $1,2,3,4$ |
| $10$ | $765$ | $97$ | $9$ | $1,2,3,4,6$ |
| $11$ | $882$ | $102$ | $8$ | $1,2,3,4$ |
| $12$ | $1007$ | $109$ | $9$ | $1,2,3,4,6$ |
| $13$ | $1140$ | $114$ | $8$ | $1,2,3,4$ |
| $14$ | $1281$ | $121$ | $9$ | $1,2,3,4,6$ |
| $15$ | $1430$ | $126$ | $8$ | $1,2,3,4$ |

There are $9373$ tuples before, and $1235$ after, the graph-endpoint
filter. The maximum number of symbols in any single cycle is three
in each diameter row. The **only** tuple at the overall maximum is
$$ (D,r,A,q)=(4,2,6,-1), \tag{11}$$
whose cycles are
$$ (2),\quad(0,3),\quad(1,4),\quad(0,2,4),\quad(0,4,2). \tag{12}$$

### 7. Why the finite certificate is exhaustive

[certify_cubic.py](certify_cubic.py) contains the full finite arithmetic
specification for Sections 5–6, with no extra coefficient or orbit
height cutoff. Its `small_certificate` loops exactly over (9), builds
(10), computes all cycles, and reports the maximum, every maximizing
tuple, every observed least period and maximum symbols per cycle.
Its `symbolic_certificate` represents $kD+s$ as the pair $(k,s)$,
enumerates (6), and builds edges using equality of integer coefficient
pairs. It also recomputes the constant-term discrepancy bound.

For clarity, the cycle extraction used there is specified fully here:

1. Enumerate every ordered pair of allowed symbols.
2. Starting from any pair not visited in a previous traversal, repeatedly
   apply the exact partial map, recording the current path and the index
   of each vertex's first appearance.
3. If the image leaves the symbol square, stop this traversal. If it
   meets a previously completed traversal, stop: any reachable cycle
   was already found. If a vertex repeats on the current path, the
   segment between its first and second occurrences is one whole cycle.
4. Mark the entire traversed path visited and continue the outer loop.

The graph is finite, so every traversal stops. Any graph cycle has a
vertex considered in the outer loop; when that cycle is first reached
it is recorded by Step 3. Distinct cycles cannot intersect in a
functional graph. Therefore all and only the graph cycles are counted,
each once. A recorded cycle has pairwise distinct vertices, so its
length is its least period. Its canonical coordinate word is obtained
by cyclic rotation only. No reversal identification enters the count.

This proves the finite-check procedure. The preceding two tables are
its exact integer output; the script is an explicit finite certificate
for their arithmetic evaluation. All bounds defining its inputs were
proved before the enumeration. The separate coefficient scan in
[scan_cubic.py](scan_cubic.py) is neither required nor invoked here.

Combining Sections 1–7 proves the total eleven-point bound, the
three-symbol restriction for each cycle and the universal period set.

### 8. From short cycles to complete parameter templates

A point on a least-period-$n$ orbit visits $n$ distinct ordered
coordinate pairs. A one-symbol cycle is fixed. With two symbols there
are only four ordered pairs, so a cycle using only two symbols cannot
have least period six. The period-two word is $(u,v)$ with $u\ne v$.
A two-symbol period-three word has the form $(u,u,v)$ with $u\ne v$.
A two-symbol period-four word must be $(u,u,v,v)$ up to rotation:
$(u,v,u,v)$ has period two, and $(u,u,u,v)$ would give both
$f(u)=2u$ and $f(u)=u+v$, forcing $u=v$.

Their recurrence equations immediately give the three corresponding
polynomial identities in the main table. For example in period two,
$f(u)=2v$ and $f(v)=2u$, so the monic polynomial
$f(t)+2t-2(u+v)$ vanishes at $u,v$; its third factor is forced by
the quadratic coefficient to be $t+u+v+b$. Period three and period
four are obtained respectively from the vanishing polynomials
$f(t)+t-(2u+v)$ and $f(t)-(u+v)$, giving exactly the displayed rows.

For three distinct symbols in period three, write them as $u<v<w$.
Each symbol's two neighbors are the other two. Thus $f(t)+t-S$
vanishes at all three, where $S=u+v+w$; monicity gives the displayed
identity. Both orientations are valid, and they are distinct cycles.

We use the following elementary integer fact for periods four and six:
if $p,q$ are distinct nonzero integers and
$$\frac1p+\frac1q\in\mathbb Z,$$
then $p+q=0$. For opposite signs the absolute value of the sum is
strictly less than one, so it must be zero. For the same sign, after
changing both signs if necessary, take $0<p<q$. If $p=1$, the sum
lies strictly between one and two; if $p\ge2$, it lies strictly
between zero and one. Neither is an integer.

For a three-symbol period-four word, the repeated symbol cannot occur
adjacently: in $(h,h,u,v)$ the two occurrences of $h$ would force
$h+v=h+u$. Thus the word is $(h,u,h,v)$ with $h,u,v$ distinct, and
$$f(h)=u+v,\quad f(u)=f(v)=2h.$$
Let $Q(t)$ be the quadratic interpolant to these three values. Since
$f(t)-Q(t)=(t-h)(t-u)(t-v)$, the leading coefficient of $Q$ is an
integer. That coefficient is
$$\frac{u+v-2h}{(h-u)(h-v)}
=\frac1{u-h}+\frac1{v-h}.$$
The integer fact forces $u+v=2h$. Writing the two endpoints as
$h-k,h+k$, with $k\ge1$, the interpolant is the constant $2h$.
This gives the centered period-four row.

For a three-symbol period-six word, first suppose no equal letters
are adjacent. The six distinct visited ordered pairs must then be
all six off-diagonal pairs on the three symbols. Each symbol occurs
twice. At a given symbol its two neighbor sums are equal; since its
neighbors use only the other two distinct symbols, equality forces
the same unordered neighbor pair at both occurrences. As each other
symbol occurs once as predecessor and once as successor, the word
must follow the same three-symbol order repeatedly, giving period
three, a contradiction.

There is therefore an adjacent pair $p,p$. Equality of the two values
of $f(p)$ forces the predecessor and successor of this pair to be
the same symbol, say $h$. A triple $p,p,p$ would force further equal
letters and hence a constant cycle, so $h\ne p$. Rotate the word to
$(h,p,p,h,\ast,\ast)$. The third symbol, say $q$, must occur in the
two remaining positions. If these two positions are $(p,q)$ or
$(q,p)$, comparing the repeated $p$ neighbor sums forces $q=p$.
If they are $(h,q)$ or $(q,h)$, comparing the repeated $h$ neighbor
sums forces $q=h$. Thus they must be $(q,q)$, and the word has form
$$(p,p,h,q,q,h).$$
Its equations are
$$f(p)=p+h,\quad f(q)=q+h,\quad f(h)=p+q.$$
Apply quadratic interpolation to $f(t)-(t+h)$. Its quadratic
coefficient is the same integer reciprocal sum
$1/(p-h)+1/(q-h)$, so $p+q=2h$. Hence $p=h-k,q=h+k$ after swapping
the endpoints, and monicity gives the centered period-six row.

These arguments exhaust the already proved possible least periods
and symbol counts. Conversely, direct substitution of every listed
polynomial identity into (1) verifies each word. The listed ranges
make all ordered pairs distinct within that cycle, so its asserted
least period is exact. For period six, the six pairs are
$(-k,-k),(-k,0),(0,k),(k,k),(k,0),(0,-k)$ after subtracting $h$;
they are distinct for $k\ge1$. The other rows have the stated least
period by the same distinct-pair criterion or their shorter displayed
words. This proves the full template classification without a bound
on the original coefficients.

All five periods occur: $f(t)=t^3$ has a fixed point and the $k=1$
six-cycle; $f(t)=t^3-3t$ has the two-cycle $(-1,1)$;
$f(t)=t^3-2t$ has the three-cycle $(-1,0,1)$; and
$f(t)=t^3-t$ has the four-cycle $(-1,0,1,0)$.

### 9. Sharpness and the entire equality locus

All large-diameter cases have at most nine points. The two-symbol
case has at most four. Thus equality in the eleven-point bound must
come from (11). Its normalized polynomial is
$$g(t)=6-t+t(t-4)(t-2)=t^3-6t^2+7t+6.$$
Equivalently,
$$g(t)=(t-2)^3-5(t-2)+4.$$
Undo the translation $g(t)=f(t+m)-2m$ and set $h=m+2$. This gives
exactly
$$f(t)=(t-h)^3-5(t-h)+2h,$$
with $h\in\mathbb Z$. In original coefficients this is
$$b=-3h,\quad c=3h^2-5,\quad a=-h^3+7h.$$

Conversely $f_0(t)=t^3-5t$ has the cycles
$$ (0),\quad(-2,1),\quad(-1,2),
\quad(-2,0,2),\quad(-2,2,0),$$
of lengths $1,2,2,3,3$. They are disjoint and supply eleven points.
The proved upper bound excludes any further periodic points.
Conjugating by $T_h$ proves equality for every stated integer
translation. This also proves that the equality locus has no omitted
coefficient or small-parameter branch. $\square$

## Corrections, validation and open risks

The original full-family contract survived unchanged; the integer
translation is only a proof device. An early possible shortcut,
“the full coordinate alphabet always has at most three symbols,” is
false and is not used. Section 5 gives an infinite family witnessing
the failure. The proof instead establishes three symbols separately
for each cycle and controls the sum of coexisting cycles globally.

The author-side [second implementation](crosscheck_cubic.py) instead
starts from the full square $\{0,\ldots,D\}^2$, without the secant
symbol filter, and removes vertices whose forward orbits leave it by
propagating backwards. It agreed with the path-traversal code in all
$9373$ small cases and verified the exact polynomial templates for
all $3474$ individual cycles encountered, including graph cases not
retained by the endpoint filter. This is a same-author cross-check,
not an independent review and not a substitute for the global lemmas.

The finite arithmetic tables and their code still require independent
reconstruction before admission. The author has not represented an
internal model review as human review or a proof assistant certificate.
The narrow exact source comparison remains subject to nonauthor
verification; no global novelty guarantee is made. None of these
arithmetic results identifies rational-prime primitive owners, target
Euler factors, root numbers, an automorphic object, target zeros or a
Hilbert–Pólya operator. `NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.
