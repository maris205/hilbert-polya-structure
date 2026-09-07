# Every rational cycle of the nonconstant quadratic Hénon family

## Claim

Let $k$ be any field with $\operatorname{char}k\ne2$. Let $t$ be
transcendental over $k$, let $a\in k^*$, and let $c\in k[t]\setminus k$.
Consider the single polynomial automorphism

$$
H_{a,c}(x,y)=(y,y^2+c-a x)
$$

on the entire set $k(t)^2$, with ordinary positive iteration. A periodic
point has its usual least positive period; points are not identified under
a sign involution. All counts below are ordinary points and ordinary cycles.

**Theorem 1 (parameter rigidity and exhaustive cycle atlas).** If
$H_{a,c}$ has a $k(t)$-rational periodic point, then

$$
c=-P^2+C,\qquad P\in k[t]\setminus k,\quad C\in k.                 \tag{1}
$$

When (1) exists, $C$ is unique and $P$ is unique up to sign. Set

$$
K_a=\frac{(a+1)^2}{4}.
$$

Every rational cycle is given by the following table and the exact
reconstruction rule below. A row contributes if and only if all its
conditions hold in $k$. Simultaneously applicable rows are **added**;
their point sets are disjoint.

| Transition word | Conditions | $C$ | Number of ordinary cycles | Least period |
|---|---|---:|---:|---:|
| $0$ | Every $a\ne0$ | $K_a$ | $2$ | $1$ |
| $1$ | Every $a\ne0$ | $-3K_a$ | $1$ | $2$ |
| $01$ | $a^2=1$ | $K_a-1$ | $1$ | $4$ |
| $001$ | $a^2=-1$ | $K_a$ | $1$ | $6$ |
| $011$ | $a=1$ | $-1$ | $2$ | $3$ |
| $00011$ | $\operatorname{char}k=3$ and $a=-1$ | $-1$ | $2$ | $5$ |
| $0111$ | $\operatorname{char}k=3$ and $a=-1$ | $1$ | $1$ | $8$ |

If no representation (1) exists, there are no rational periodic points.
If (1) exists but no row applies, there are again no such points. Thus the
table is both necessary and sufficient, not just a list of available cycles.

For a row with binary word $w$, repeat $w$ periodically as a transition
sequence $(\delta_i)$. Choose $\sigma_0=1$ or $-1$, and propagate
$\sigma_{i+1}=\sigma_i(-1)^{\delta_i}$ in both directions. Define

$$
y_i=\sigma_iP+\frac{(-1)^{\delta_i}+a(-1)^{\delta_{i-1}}}{2}.        \tag{2}
$$

The points $(y_i,y_{i+1})$ are precisely the row's cycles. An even number
of ones in $w$ gives two distinct cycles, one from each initial sign. An
odd number gives one cycle of twice the word length. Formula (2) provides
all labels over $k(t)$ itself; no field extension or root choice beyond
the required $P$ is inserted.

**Theorem 2 (sharp bounds and the determinant exception).** For every
field and map in Theorem 1 there are at most $14$ rational periodic
points. Equality holds exactly when

$$
\operatorname{char}k=3,\quad a=-1,\quad c=-P^2-1
\quad\text{for some }P\in k[t]\setminus k.                         \tag{3}
$$

These maps have one four-cycle and two five-cycles. When
$\operatorname{char}k\notin\{2,3\}$, the sharp field-dependent bound is
$8$ if $-1$ is a square in $k$, and $6$ otherwise. The bound $8$ is attained
exactly at $a^2=-1$ and $C=K_a$, by two fixed points and a six-cycle.
The bound $6$ in the nonsquare case is attained at $a=1$, $C=-1$.
For every characteristic different from two, a point of period greater
than two requires $a^4=1$.

**Corollary 3 (the same native return ledger).** Let $m_j$ be the number
of cycles of length $j$ obtained by adding the applicable rows of the
table. Then for every $n\ge1$,

$$
\#\operatorname{Fix}(H_{a,c}^n)(k(t))
 =\sum_{j\mid n}j m_j,\qquad
\zeta_{H,k(t)}(z)=\prod_j(1-z^j)^{-m_j}.                           \tag{4}
$$

The empty product is one. This is a finite rational-periodic-point zeta,
not a Frobenius zeta of a variety or a target Euler factor. The return
formula is a consequence of the atlas, not another paper contract.

## Status

**PROVABLE AS STATED**, by the self-contained proof below. This is an
author-side proof status. Independent mathematical/source review, the
coordinator's admission judgment and all manuscript gates are separate.
No paper number or new formal Route A evaluation has been assigned.

## Assumptions and notation

The parameter $c$ is polynomial and nonconstant. The determinant $a$ is
a nonzero constant in $k$, not an arbitrary rational function. The
characteristic-two family and the constant-$c$ family are not claimed.
No perfection, algebraic closure, finite cardinality, ordering or local
compactness of $k$ is assumed. Degree always means degree in $t$; the
degree of zero can be regarded as $-\infty$ in degree inequalities.

A periodic orbit is written as consecutive coordinates $(y_i,y_{i+1})$,
where indices are taken cyclically. Its recurrence is

$$
y_i^2+c=y_{i+1}+a y_{i-1}.                                        \tag{5}
$$

For a polynomial prime $\pi\in k[t]$, $v_\pi$ is its usual discrete
valuation on $k(t)$, normalized by $v_\pi(\pi)=1$. Every nonzero constant
has valuation zero. Binary bits are elements of the set $\{0,1\}$;
when used in field equations their images in $k$ are intended. They
remain distinct in every field under consideration.

## Proof strategy and dependency map

1. The maximum-pole argument in (5) gives polynomial integrality. This is
   classical non-Archimedean escape reasoning, stated explicitly here.
2. A degree comparison at the unique pole of $c$ gives a common degree
   and a global two-branch, constant-offset rigidity statement.
3. Completion of the square fixes the parameter form (1). Coefficient
   comparison in the two linearly independent polynomials $P$ and $1$
   gives an exact binary constraint.
4. An eight-state partial permutation with a two-sheet sign lift encodes
   every actual rational point injectively. It is not the unrestricted
   two-symbol local horseshoe.
5. Direct case analysis of the least state in a cycle exhausts the graph
   over every allowed field. No finite prime or determinant sample is
   promoted to a theorem.
6. The sign product determines ordinary, rather than sign-quotiented,
   periods. The table's overlaps give the sharp total bounds.

The closest-source deductions and prior-repository ownership are recorded
separately in `SOURCE_AUDIT.md` when completed. In particular, C412 already
owns an integral conservative quadratic sign/offset encoding, and Ingram
owns function-field finiteness and bad-place height bounds in his stated
normalization. Neither classical integrality nor symbolic coding as a
general method is claimed as a new discovery here.

## Proof

### Step 1. No rational periodic coordinate has a finite pole

Fix a periodic orbit satisfying (5). If some coordinate has a pole at
$\pi$, let $M>0$ be the largest pole order among the finitely many
coordinates, and choose $i$ with $v_\pi(y_i)=-M$. Since $c$ is polynomial,
$y_i^2+c$ has valuation exactly $-2M$. The right side of (5) has valuation
at least $-M$, since $a$ is a nonzero constant. This is a contradiction.
Every $y_i$ therefore has no pole at any polynomial prime. A rational
function over $k$ with this property is in $k[t]$: in a coprime fraction,
every irreducible factor of a nonconstant denominator would give a pole.

The inverse map is
$H_{a,c}^{-1}(x,y)=((x^2+c-y)/a,x)$. Thus the cyclic use of (5) is valid
also for periods one and two; no separate noninvertible preperiodic tail
is being counted.

### Step 2. Every periodic coordinate has the same positive degree

Let $m$ be the largest degree among one periodic orbit's coordinates.
If $m\le0$, the right side of (5) is constant for every $i$, whereas the
left side contains nonconstant $c$. Thus $m>0$.

Choose a coordinate of degree $m$. The right side of (5) has degree at
most $m$. If $\deg c<2m$, its left side has degree $2m$; if $\deg c>2m$,
it has degree $\deg c$. Both contradict $m>0$. Consequently
$\deg c=2m$, and the leading terms must cancel. If any other coordinate
had degree smaller than $m$, its square could not cancel the degree
$2m$ term of $c$, giving the same contradiction. All coordinates have
degree $m=\deg(c)/2$.

This value of $m$ depends only on $c$. The conclusion applies separately
to every periodic orbit, even if the complete periodic set has not yet
been shown finite. In particular, odd degree of $c$ precludes all rational
periodic points.

### Step 3. Two branches and the unique centered parameter

Suppose at least one periodic point exists, and fix one of its coordinates
$P_0$. For any coordinate $y$ in any periodic orbit, subtract the two
instances of (5). The resulting identity gives

$$
\deg(y^2-P_0^2)\le m.                                             \tag{6}
$$

Both coordinates have degree $m$. Their leading coefficient ratio has
square one, and hence equals a unique sign $\sigma\in\{1,-1\}$.
Because $2\ne0$, the polynomial $y+\sigma P_0$ has degree $m$. Factoring
(6) as

$$
(y-\sigma P_0)(y+\sigma P_0)
$$

shows that $y-\sigma P_0$ is constant, including the possibility that it
is zero. Thus every periodic coordinate has the form
$\sigma P_0+b$ with $b\in k$.

Apply (5) at the chosen coordinate $P_0$. Both its neighbors have this
form, so there are constants $U,V\in k$ such that

$$
c=-P_0^2+U P_0+V.
$$

Setting $P=P_0-U/2$ and $C=V+U^2/4$ gives (1). This is a proof
normalization, not a change of the map or the domain. Every coordinate
can now be written uniquely as $\sigma_iP+b_i$ with $b_i\in k$.

If also $c=-Q^2+D$ with nonconstant $Q$ and constants $C,D$, then
$(P-Q)(P+Q)=C-D$. If the right side were nonzero, both factors would be
nonzero constants, implying that $2P$ is constant. This is impossible.
Therefore $C=D$ and $Q=P$ or $Q=-P$. This proves the asserted uniqueness.

### Step 4. The exact local constraint

Substitute $y_i=\sigma_iP+b_i$ and (1) into (5). Since $P$ is
nonconstant, its coefficient and the constant term can be compared
separately. They give

$$
2\sigma_i b_i=\sigma_{i+1}+a\sigma_{i-1},\qquad
b_i^2+C=b_{i+1}+a b_{i-1}.                                      \tag{7}
$$

Define $\delta_i\in\{0,1\}$ by
$\sigma_{i+1}=\sigma_i(-1)^{\delta_i}$. The first identity in (7)
is precisely the offset formula in (2). Put

$$
\Lambda=K_a-C.
$$

After substituting the offsets into the second identity in (7), it is
equivalent, at index $i+1$, to

$$
\boxed{\Lambda=a^2\delta_{i-1}
             +2a\delta_i\delta_{i+1}+\delta_{i+2}.}               \tag{8}
$$

For an explicit expansion check, at index $i$ the same identity reads

$$
4C=(2\sigma_{i+1}\sigma_{i+2}-1)
 +\bigl(2\sigma_i(\sigma_{i-1}+\sigma_{i+1})
              -2\sigma_{i-1}\sigma_{i+1}\bigr)a
 +(2\sigma_{i-1}\sigma_{i-2}-1)a^2.
$$

Here $\sigma_j\sigma_{j+1}=1-2\delta_j$, and the middle coefficient
is $2-8\delta_{i-1}\delta_i$. This gives (8) upon shifting the index.
Every identity takes place over $\mathbb Z[1/2]$ before specialization,
so it remains valid in all the allowed positive characteristics.

### Step 5. An exact partial permutation, with injective point labels

Let $V=\{0,1\}^3$. A state $uvw\in V$ has an edge to $vwz$ precisely
when

$$
\Lambda=a^2u+2avw+z.                                             \tag{9}
$$

The complete edge table is below. The entries are the required value of
$\Lambda$; an edge exists only if that entry equals the fixed parameter.

| State | Successor with $z=0$: label | Successor with $z=1$: label |
|---|---|---|
| $000$ | $000$: $0$ | $001$: $1$ |
| $001$ | $010$: $0$ | $011$: $1$ |
| $010$ | $100$: $0$ | $101$: $1$ |
| $011$ | $110$: $2a$ | $111$: $2a+1$ |
| $100$ | $000$: $a^2$ | $001$: $a^2+1$ |
| $101$ | $010$: $a^2$ | $011$: $a^2+1$ |
| $110$ | $100$: $a^2$ | $101$: $a^2+1$ |
| $111$ | $110$: $a^2+2a$ | $111$: $(a+1)^2$ |

The two outgoing labels of a state differ by one. The two incoming
labels at a prescribed successor differ by $a^2$. Both differences are
nonzero. The graph therefore has indegree and outdegree at most one:
its recurrent part is a disjoint union of simple directed cycles.

For $\varepsilon\in\{1,-1\}$ define the point reconstruction

$$
E(\varepsilon;u,v,w)=\left(
 \varepsilon P+\frac{(-1)^v+a(-1)^u}{2},\quad
 \varepsilon(-1)^vP+\frac{(-1)^w+a(-1)^v}{2}\right).              \tag{10}
$$

This labels all $16$ signed states injectively. Indeed, the leading
coefficient of the first coordinate determines $\varepsilon$ relative
to $P$. The leading coefficient ratio of the two coordinates determines
$v$. The first constant offset then determines $u$, using $a\ne0$ and
the distinctness of $1,-1$. The second offset determines $w$.

Direct substitution, or (7)–(9), proves that an edge has the exact lift

$$
H_{a,c}\bigl(E(\varepsilon;u,v,w)\bigr)
 =E\bigl(\varepsilon(-1)^v;v,w,z\bigr).                          \tag{11}
$$

Conversely, suppose the image is $E(\varepsilon';u',v',w')$.
The two leading coefficients first give
$\varepsilon'=\varepsilon(-1)^v$ and $v'=w$. Comparing the first
constant offset then gives $u'=v$, since $a\ne0$. Setting $z=w'$,
the remaining constant equation forces (9). Thus (11) is an if-and-only-if
description of the restriction to these $16$ points. Steps 1–4 prove
that every rational periodic point occurs here. A directed cycle in
this graph gives actual points of the original map by (11), proving
sufficiency as well as necessity.

### Step 6. Exhaustion of cycles over every allowed field

Order the eight states lexicographically and choose the least state of
a directed cycle. This gives the following exhaustive case analysis.
It uses the edge table, not a sample of parameter values.

**Least state $000$.** A self-loop has $\Lambda=0$, giving transition
word $0$. Otherwise the cycle leaves along $000\to001$, so
$\Lambda=1$. The next state must be $011$, because the other edge from
$001$ has label zero. From $011$, an edge to $111$ would require
$2a+1=1$, which would force $a=0$. Hence it goes to $110$ and
$2a=1$. An edge from $110$ to $101$ would require $a^2+1=1$, again
forcing $a=0$. Thus it goes to $100$, with $a^2=1$, and then to $000$.
The equations $2a=1$, $a^2=1$ are equivalent to
$\operatorname{char}k=3$ and $a=-1$: squaring the first gives
$4a^2=1$, so $3=0$, after which $1/2=-1$. The resulting cycle is
$000\to001\to011\to110\to100\to000$, with word $00011$.

**Least state $001$.** An edge to $011$ would have $\Lambda=1$ and
would follow the just-derived path through $000$, contradicting
minimality. The edge is therefore $001\to010$, with $\Lambda=0$,
then $010\to100$. The edge from $100$ to $000$ would require $a=0$;
the other closes at $001$ exactly when $a^2+1=0$. This is word $001$.

**Least state $010$.** The label-zero edge leads to $100$, whose
successors are both less than $010$, so it cannot belong to this cycle.
The other edge has $\Lambda=1$ and leads to $101$. An edge from there
to $011$ would force $a^2+1=1$, contradicting $a\ne0$. Therefore it
returns to $010$, exactly when $a^2=1$. This is word $01$.

**Least state $011$, first edge to $110$.** Here $\Lambda=2a$.
The edge from $110$ to $100$ cannot belong to such a cycle, since
the successors of $100$ are below $011$. The edge to $101$ thus
requires $a^2+1=2a$, equivalently $(a-1)^2=0$ and hence $a=1$.
The next edge closes at $011$. This is word $011$ and $\Lambda=2$.

**Least state $011$, first edge to $111$.** Here $\Lambda=2a+1$.
The self-loop at $111$ cannot close the cycle containing $011$ and,
in any event, equality of its label with $2a+1$ would force $a=0$.
The next edge is $111\to110$, requiring $a^2=1$. The edge from
$110$ to $100$ is excluded by the same smaller-successor argument.
Thus $110\to101$ requires $a^2+1=2a+1$, giving $2a=1$.
These equations again force characteristic three and $a=-1$.
The edge $101\to011$ closes the cycle. Its word is $0111$ and
$\Lambda=2$ in characteristic three.

**Remaining least states.** State $100$ has only smaller successors,
and $101$ does also. State $110$ has successors $100,101$, so it
cannot be least in a cycle either. State $111$ can only occur as its
self-loop if it is least. This gives word $1$ and
$\Lambda=(a+1)^2$.

This is the complete list of seven types. Substituting
$C=K_a-\Lambda$ gives exactly the parameter entries in Theorem 1.
The proof has explicitly retained the characteristic-three solutions
of the otherwise inconsistent equations; no characteristic-zero gcd
criterion has been used to discard them.

### Step 7. Ordinary periods and completeness of the point counts

Let a graph cycle have length $\ell$ and transition word $w$. Returning
to its first bit state multiplies $\varepsilon$ in (11) by

$$
(-1)^{\sum_{j=0}^{\ell-1}w_j}.
$$

If this sign is positive, the two initial signs give two disjoint
cycles of length $\ell$. If it is negative, they join into one cycle
of length $2\ell$. These periods are least: an earlier return would
return first to the same graph state, so its time must be a multiple
of $\ell$, and then it must also restore the sign. Injectivity of
(10) rules out any shorter collision of actual points.

The words $0,011,00011$ have even parity; the other four words have
odd parity. Their lengths give the ordinary periods and cycle
multiplicities in the table. Different graph cycles have disjoint
states and hence, by (10), disjoint actual point sets. This proves
the additivity instruction even when parameter rows overlap.

Every point reconstructed from the table satisfies (11) around a
closed signed cycle. Every rational periodic point was proved to
lie on such a cycle. Theorem 1 follows in both directions.

### Step 8. Sharp bounds, with all row overlaps retained

First suppose $a\notin\{1,-1\}$. The only possible extra row beyond
fixed and two-cycles is $001$, and it requires $a^2=-1$.
The fixed and two-cycle parameters $K_a$ and $-3K_a$ are distinct,
because equality would give $(a+1)^2=0$. If $a^2=-1$, the parameter
$C=K_a$ therefore contributes exactly two fixed points and one
six-cycle, for a total of eight. In all other such cases the total
is at most two.

If $a=1$, the possibly nonempty rows have

$$
(C,\text{point contribution})=(1,2),\ (-3,2),\ (0,4),\ (-1,6).
$$

In characteristic different from two, these constants are distinct
except that $-3=0$ in characteristic three. That sole collision
combines the two- and four-cycles, giving six points; it does not
meet the six-point three-cycle parameter. Hence the maximum for
$a=1$ is exactly six in every allowed characteristic.

If $a=-1$, then $K_a=0$. At $C=0$ there are two fixed points and
one two-cycle, totaling four. The word $01$ gives four points at
$C=-1$. Outside characteristic three there are no other rows for
this determinant. In characteristic three, $00011$ adds ten points
at the same $C=-1$, while $0111$ gives eight points at $C=1$.
The constants $0,-1,1$ are distinct in characteristic three.
Consequently the maximum is fourteen, precisely as in (3).

These cases exhaust every $a\ne0$. Theorem 2's total bounds and
equality locus follow. Each stated maximum is attained for $P=t$
over the indicated field, since the table gives actual cycles there.
The field-dependent bound outside characteristics two and three
follows because the eight-point case exists exactly when $-1$ has
a square root in $k$; otherwise $a=1,C=-1$ attains six.
Finally, every row of period greater than two has $a=1$, $a=-1$
or $a^2=-1$. Each condition implies $a^4=1$.

### Step 9. Return counts and native zeta

A cycle of least period $j$ contributes its $j$ distinct points to
$\operatorname{Fix}(H^n)$ exactly when $j$ divides $n$. Summing this
identity over the finitely many cycles gives the first formula in
(4). As a formal power series at zero,

$$
\sum_{n\ge1}\frac{z^n}{n}\sum_{j\mid n}j m_j
 =-\sum_j m_j\log(1-z^j),
$$

so exponentiation gives the second. This finishes the proof. $\square$

## Corrections or missing assumptions

The initial scouting bound of $16$ states is a valid coarse bound,
not the sharp result. The exhaustive graph proof sharpens it to $14$
and retains the characteristic-three five- and eight-cycle branches.
The early conservative specialization with only periods one through
four was explicitly a diagnostic, not a claim for arbitrary $a$.

## Open risks and evidence scope

No mathematical implication above relies on a numerical experiment.
The companion script `certify_symbol_graph.py` independently enumerates
all $19$ simple cycles of the unrestricted eight-state graph, derives
their exact integer polynomial labels, checks all $16$ reconstruction
identities over $\mathbb Q[a]$, and verifies the sharp example directly
in $\mathbb F_3[t]$. The seven surviving types are proved over all
fields in Step 6, not inferred from that finite computation.

The script does not check finite-prime valuations or the global degree
reduction. Independent review of those proofs and closest-source
ownership remains required. The result does not classify maps with
nonconstant determinant, rational parameters with additional poles,
constant parameters, characteristic two, or points over arbitrary
finite extensions of $k(t)$. In particular it does not solve the
number-field uniform boundedness conjecture. Source arithmetic and
the finite zeta do not imply target Euler factors, root numbers,
automorphy, a target divisor or a Hilbert–Pólya realization.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
