# Proof Package — all odd-degree discrete-sine Hénon cycle graphs

## Claim

For every odd integer $d=2k+1\ge3$, let

$$
s_d(Y)=\sum_{j=0}^{k}(-1)^{k-j}
 \frac{Y\prod_{i=1}^{j}(Y^2-i^2)}{(2j+1)!},
\qquad h_d(x,y)=(y,-x+s_d(y)).
$$

The state space is all of $\mathbb Q^2$, and the clock is ordinary iteration
of $h_d$. Put $R=(d+1)/2=3q+s$, where $s\in\{0,1,2\}$. Thus $q\ge1$
for $s=0,1$, and $q\ge0$ for $s=2$. Let $C_n(d)$ be the number of primitive
cycles of length $n$, modulo rotation but without identifying opposite or
reverse cycles. The following three **additive** tables give all the cycles.
An absent entry has multiplicity zero.

First add the central cycles:

| Condition | Central cycles, written as period: multiplicity |
|---|---|
| $R$ odd | $1:1,\quad 5:2,\quad 6:1$ |
| $R$ even | $1:1,\quad 3:2,\quad 10:1$ |

Next add the bulk cycles:

| $s$ | Period $4$ | Period $12$ | Period $20$ |
|---:|---:|---:|---:|
| $0$ | $q(q+1)$ | $q(q-1)$ | $q(q-1)$ |
| $1$ | $q(q+1)$ | $q(q+1)$ | $q(q-1)$ |
| $2$ | $q(q+1)$ | $q(q+1)$ | $q(q+1)$ |

Finally add the boundary cycles:

| $s$ | Boundary cycles, written as period: multiplicity |
|---:|---|
| $0$ | $4:2q+2,\quad 14:2$ |
| $1$ | $6:2,\quad 16:2,\quad 36:q-1,\quad (16q+6):1$ |
| $2$ | $4:2,\quad 6:1,\quad 8:2q$ |

In particular, with $P(d)$ the total number of rational periodic points,

$$
P(d)=
\begin{cases}
36q^2-20q+53,&R=3q,\\
36q^2+48q+31,&R=3q+1,\\
36q^2+52q+31,&R=3q+2.
\end{cases}
$$

Equivalently, these totals are $(3d^2-4d+152)/3$, $d^2+6d+24$, and
$d^2+8d/3+14$ in the respective classes $d\equiv5,1,3\pmod6$.
For every $n\ge1$, the exact fixed-point count and source cycle zeta are

$$
N_n(d)=\sum_{\ell\mid n}\ell C_\ell(d),\qquad
Z_d(u)=\exp\!\left(\sum_{n\ge1}\frac{N_n(d)}n u^n\right)
      =\prod_{\ell\ge1}(1-u^\ell)^{-C_\ell(d)}.
$$

The proof below also parametrizes the actual cycle graph: positive-phase
bulk points are the residue rectangles of Appendix A, with the stated
central exceptions; the negative phase is obtained through the exact
$C(Sg)C$ relation in Step 3, not by directly reusing the positive-phase
point labels. Boundary cycles are the first-return families in Steps 5–7, with their
intermediate points recovered by the explicit recurrence. Thus the claim
is not only a count or a finite-box search algorithm.

## Status

**PROVABLE AS STATED — author proof complete, independent review pending.**

No paper number or manuscript is assigned by this document. It is one
all-degree family theorem, not separate results for the three congruence
classes. The requested scope has not been weakened to one degree class or
to sufficiently large degrees.

## Assumptions

- The polynomial, sign, rational state space and ordinary clock are exactly
  those in the claim.
- Arithmetic on residues is modulo $6$ unless another modulus is written.
- A cycle is counted once under rotation only. Sign reversal will be used
  as a proof device, not as a change to this convention.

## Notation

- $\sigma:\mathbb Z\to\{0,1,-1\}$ is the six-periodic sequence with values
  $(0,1,1,0,-1,-1)$ on $0,1,\ldots,5$.
- $p=(-1)^{R-1}$; $g_p(x,y)=(y,-x+p\sigma(y))$ on $\mathbb Z^2$.
- $S(x,y)=(-x,-y)$ and $C(x,y)=(-x,y)$.
- $B=[-R-2,R+2]^2\cap\mathbb Z^2$ is the escape box;
  $B_0=[-R,R]^2\cap\mathbb Z^2$ is the core.
- $A=\{(x,y)\in B:|y|\in\{R+1,R+2\}\}$ is the boundary section.
- $[x,\ell]$ denotes the positive representative $(x,R+\ell)$, for
  $\ell\in\{1,2\}$, of its pair under $S$.
- $L_c=[-R+c,1]$, $U_c=[R+c,1]$, and $V_c=[R+c,2]$.

## Proof Strategy

First reduce rational periodic points to integral points of $B$. Inside
$B_0$, use exact affine residue-cell identities for the periodic map $g_p$.
Every remaining periodic orbit meets $A$. Quotient its first return by $S$,
but retain a sign on every return edge. There are finitely many uniform
strip rules and finitely many endpoint rules. Their cycle decomposition
gives all boundary cycles, including the growing cycle. Reassemble the two
disjoint pieces and sum their cardinalities.

## Dependency Map

1. The main claim uses rational integrality, the integer escape bound, the
   complete core table, and the complete signed boundary-return table.
2. Integrality uses the strict $p$-adic dominance of the highest factorial
   summand, for every prime separately.
3. Escape and the core/boundary values use the elementary central-factorial
   identities in Step 1. The already published escape input is reproved
   here in the odd-degree setting to avoid dependence on real-variable
   numerical monotonicity checks.
4. The core classification uses 36 affine identities, proper-divisor
   linear equations, and exact arithmetic-progression counts.
5. Boundary closure uses 36 affine free-strip identities, 30 endpoint
   rows repeated across the paired residue classes, and a monotone
   translation chain with exactly $q+1$ and $q$ nodes.
6. The checks use the least admissible radius in each residue progression:
   $6,7,2,3,4,5$ for $R\equiv0,1,2,3,4,5\pmod6$. There is no exceptional
   finite-degree census hidden in an asymptotic argument.

## Proof

### Step 1. Exact integer values and escape inputs

Write

$$
c_j(Y)=\frac{Y\prod_{i=1}^j(Y^2-i^2)}{(2j+1)!}.
$$

For an integer $n\ge0$, $c_j(n)=\binom{n+j}{2j+1}$, with the binomial
coefficient zero when $j\ge n$. This proves integrality on nonnegative
integers; oddness proves it on negative integers. As a formal power series,

$$
\sum_{n\ge0}\left(\sum_{j\ge0}(-1)^j
\binom{n+j}{2j+1}\right)z^n
=\sum_{j\ge0}\frac{(-1)^jz^{j+1}}{(1-z)^{2j+2}}
=\frac{z}{1-z+z^2}.
$$

Its coefficients are $\sigma(n)$. Comparing the full finite sum at $n$
with the truncation at $j=R-1$ gives

$$
s_d(n)=p\sigma(n)\quad (|n|\le R),\qquad
s_d(R+1)=a:=(-R)\bmod3,\qquad
s_d(R+2)=2R+t,\quad t:=R\bmod3.
\tag{1}
$$

For the last two identities, the missing tail at $R+1$ consists of the
single binomial coefficient $1$; the missing tail at $R+2$ consists of
$2R+2$ and $1$. Hence the respective values are
$1+p\sigma(R+1)$ and $2R+1+p\sigma(R+2)$, giving (1) in all six residues.
Negative boundary values follow from oddness.

For use outside the box, we prove

$$
s_d(n)\ge3n\qquad(n\in\mathbb Z,\ n\ge R+3).
\tag{2}
$$

Pascal's identity, applied twice, gives
$c_j(n+1)-2c_j(n)+c_j(n-1)=c_{j-1}(n)$ for $j\ge1$; the second
difference of $c_0(n)=n$ vanishes. Consequently

$$
s_d(n+1)-2s_d(n)+s_d(n-1)=s_{d-2}(n).
\tag{3}
$$

For $d=3$, $R=2$ and $s_3(n)=(n^3-7n)/6\ge3n$ for $n\ge5$.
Suppose (2) holds in degree $d-2$, where the core radius is $R-1$, and
$R\ge3$. Put $D(n)=s_d(n)-s_d(n-1)$. By (1),
$D(R+2)=2R+t-a\ge2R-2\ge4$. For $n\ge R+2$, (3) and the induction
hypothesis imply $D(n+1)-D(n)=s_{d-2}(n)\ge3n>0$. In particular all
subsequent increments exceed $3$. Also

$$
s_d(R+3)=2s_d(R+2)-s_d(R+1)+s_{d-2}(R+2)
\ge4R-2+3(R+2)=7R+4\ge3(R+3).
$$

Starting from this inequality and adding the positive increments proves
(2). This completes induction over all odd degrees. Oddness gives
$|s_d(n)|\ge3|n|$ for $|n|\ge R+3$.

Now let a rational periodic orbit have coordinates $y_i$, indexed cyclically,
so that $y_{i-1}+y_{i+1}=s_d(y_i)$. At a prime $v$, if $|y|_v>1$, the
$j$th summand in $s_d(y)$ has norm
$|y|_v^{2j+1}|(2j+1)!|_v^{-1}$. These norms strictly increase with $j$.
The ultrametric inequality and uniqueness of the largest norm therefore give
$|s_d(y)|_v=|y|_v^d|d!|_v^{-1}>|y|_v$. At a coordinate of maximal norm
on the finite orbit this contradicts the recurrence. Every coordinate is
$v$-integral at every prime and hence is an integer.

If a periodic orbit has an integer coordinate of maximal ordinary absolute
value $M\ge R+3$, (2) makes the right side of its recurrence have absolute
value at least $3M$, while the left side has absolute value at most $2M$.
Thus every rational periodic orbit lies in $B$. A trajectory leaving $B$
cannot be periodic. These are the only global arithmetic inputs needed.

### Step 2. Full bulk classification for the positive phase

First use the proof device $g=g_+$ on the full lattice. In one residue cell
$(x,y)\equiv(e,f)$, every iterate is a pair of affine expressions in the
free variables $x,y$. The precise recurrence for a coordinate expression
$ax+by+c$ is obtained by evaluating
$\sigma(ae+bf+c)$; the next point is then

$$
(X,Y)\longmapsto\bigl(Y,-X+\sigma(Y\bmod6)\bigr).
\tag{4}
$$

Appendix A gives all 36 identities. Its row
$(e,f;\ell;L_x,U_x,L_y,U_y)$ asserts two facts:

1. The $\ell$th affine iterate is identically $(x,y)$ throughout that
   residue cell. Its least period is $\ell$ except at the listed central
   points.
2. The full orbit is contained in $B_0$ if and only if
   $-R+L_x\le x\le R+U_x$ and $-R+L_y\le y\le R+U_y$.

Here is how both assertions are verified without restricting the radius.
Iterate (4) until the two affine expressions are $x,y$ again. Every
intermediate coordinate is $\pm x+c$ or $\pm y+c$. Intersecting its exact
inequality $-R\le\pm x+c\le R$, or its $y$ version, produces the displayed
rectangle. To test a smaller period, it is enough to test the proper
divisors of $\ell$. At each such divisor, equality with $(x,y)$ is a pair
of linear equations. Every consistent pair has a unique solution; those
solutions that are integral and in the required residue cell are exactly
the following 17 points, grouped here into actual $g$-cycles:

$$
(0,0);
$$
$$
(0,2)\to(2,1)\to(1,-1)\to(-1,-2)\to(-2,0)\to(0,2)
$$

and its negative, together with

$$
(0,1)\to(1,1)\to(1,0)\to(0,-1)\to(-1,-1)\to(-1,0)\to(0,1).
$$

All 17 points lie in $[-2,2]^2$. The exact linear-equation tests and all
rectangle intersections are implemented in `symbolic_bulk.py`; they use
free affine variables, not sample points or sample degrees. In particular,
the code rejects any consistent rank-one exceptional family instead of
silently discarding it.

It remains to count the rectangles, not to infer a formula from examples.
Write $R=6m+r$. For one coordinate of residue $e$ with offsets $(L,U)$,
the number of admissible integers is exactly

$$
2m+\left\lfloor\frac{r+U-e}{6}\right\rfloor
    -\left\lceil\frac{-r+L-e}{6}\right\rceil+1.
\tag{5}
$$

The two counts are multiplied for each row of Appendix A; its central
exceptions are subtracted; and the result is divided by $\ell$. All
coordinate counts in (5) are nonnegative already at the least admissible
$m$, namely $m=1$ for $r=0,1$ and $m=0$ otherwise. Thus no positive-part
correction has been dropped. The resulting polynomials in $m$ are

| $r$ | Bulk $C_4$ | Bulk $C_{12}$ | Bulk $C_{20}$ |
|---:|---:|---:|---:|
| $0$ | $4m^2+2m$ | $4m^2-2m$ | $4m^2-2m$ |
| $1$ | $4m^2+2m$ | $4m^2+2m$ | $4m^2-2m$ |
| $2$ | $4m^2+2m$ | $4m^2+2m$ | $4m^2+2m$ |
| $3$ | $4m^2+6m+2$ | $4m^2+2m$ | $4m^2+2m$ |
| $4$ | $4m^2+6m+2$ | $4m^2+6m+2$ | $4m^2+2m$ |
| $5$ | $4m^2+6m+2$ | $4m^2+6m+2$ | $4m^2+6m+2$ |

Substitution $q=2m+\lfloor r/3\rfloor$ gives the claim's bulk table.
The central positive-phase cycles are $1:1,5:2,6:1$.

### Step 3. Transfer to the negative phase without changing the clock

The identities $Sg=gS$ and $g_-=C(Sg)C$ hold by direct substitution.
Both $S$ and $C$ preserve $B_0$. Since $(Sg)^n=S^ng^n$, the points whose
entire $Sg$-orbit stays in $B_0$ are exactly the points whose $g$-orbit stays
there. This proves the asserted parametrization after applying $C$.

Let $z$ have $g$-period $\ell\in\{4,12,20\}$. Its $Sg$-period divides
$\ell$. If $(Sg)^nz=z$ with $n$ even, then $g^nz=z$, so $\ell\mid n$.
If $n$ is odd, then $g^nz=-z$, hence $\ell\mid2n$, impossible because
$4\mid\ell$. The least period is therefore unchanged, and the total
number of cycles of each of these lengths is unchanged.

Negation exchanges the two 5-cycles, so $Sg$ joins them into one 10-cycle.
On the 6-cycle displayed above, $S=g^3$, hence $Sg=g^4$ splits that cycle
into two 3-cycles. The origin stays fixed. This proves both central rows
and the bulk table for the actual degree-dependent phase $p$ in (1).

### Step 4. Boundary reduction and exact first-return rules

A periodic orbit not wholly in $B_0$ contains a coordinate with absolute
value $R+1$ or $R+2$, so it meets $A$. A periodic orbit wholly in $B_0$
was already classified: until a coordinate exits $[-R,R]$, (1) makes
$h_d$ and $g_p$ identical. These two classes of periodic orbit are disjoint.

The map $h_d$ commutes with $S$. A return from $[x,\ell]$ will be recorded
as $(\tau,\epsilon;[x',\ell'])$ when
$h_d^\tau(x,R+\ell)=\epsilon(x',R+\ell')$, where
$\epsilon\in\{+1,-1\}$. It is always the **first** return to $A$.
If a normalized return cycle has total time $T$ and sign product $+1$,
it lifts to two primitive $h_d$-cycles of length $T$. If its sign product
is $-1$, it lifts to one primitive cycle of length $2T$. The first-return
property proves primitivity: an earlier return to the starting point would
force an earlier repeat of the normalized section point. The two lifts in
the positive-sign case are distinct because otherwise a negative return
would occur before the normalized cycle closes.

Let $r=R\bmod6$, $\kappa=3\lfloor r/3\rfloor$, and
$e=(x-\kappa)\bmod6$. For $[x,1]$ in the interval
$-R+L\le x\le R+U$, the following table gives the first return. Every
edge in this table has sign $-1$; its normalized target is
$[x+\delta,\ell']$.

| $s$ | $e$ | $L$ | $U$ | $\tau$ | $\delta$ | $\ell'$ |
|---:|---|---:|---:|---:|---:|---:|
| $0$ | $0,3$ | $0$ | $0$ | $2$ | $0$ | $1$ |
| $0$ | $1$ | $2$ | $0$ | $10$ | $-2$ | $1$ |
| $0$ | $2$ | $4$ | $0$ | $14$ | $-4$ | $1$ |
| $0$ | $4,5$ | $0$ | $0$ | $2$ | $0$ | $2$ |
| $1$ | $0$ | $4$ | $2$ | $6$ | $-4$ | $1$ |
| $1$ | $1$ | $3$ | $-1$ | $18$ | $0$ | $1$ |
| $1$ | $2,5$ | $2$ | $2$ | $2$ | $-2$ | $1$ |
| $1$ | $3,4$ | $2$ | $2$ | $2$ | $-2$ | $2$ |
| $2$ | $0,5$ | $1$ | $1$ | $2$ | $-1$ | $2$ |
| $2$ | $1,4$ | $1$ | $1$ | $2$ | $-1$ | $1$ |
| $2$ | $2$ | $1$ | $-3$ | $10$ | $3$ | $1$ |
| $2$ | $3$ | $1$ | $-1$ | $6$ | $1$ | $1$ |

This table is a finite affine calculation with $R,x$ both free. Start at
$(x,R+1)$, use $s_d(R+1)=a$ in the first step, and use
$p\sigma(y)$ at every intermediate step. Record each necessary inequality
$-R\le y\le R$; their intersection is exactly the stated interval in
$x$. Stop at the first coordinate of the form $\pm(R+\ell')$. Thus the
recorded inequalities also prove that no intermediate return was omitted.
All other intermediate coordinates are $\pm R+c$ or constants, and their
bulk inequalities hold for $R\ge2$ in every row. The finite affine
derivation is `symbolic_boundary.py`; its output is checked against this
table by `verify_symbolic_certificate.py`.

For an outer state $[x,2]$, its next coordinate is $2R+s-x$. It leaves
$B$ immediately if $x<R+s-2$. The only other outer states are therefore
$V_c$ with $s-2\le c\le2$. For one inner residue row, the exact
complement of its generic interval in $[-R-2,R+2]$ consists of the left
offsets $-2\le c\le L-1$ and the right offsets $U+1\le c\le2$, filtered
by that row's residue. The generic real interval is nonempty already at
the least radius: $2R+U-L\ge0$. The two complementary intervals are
therefore disjoint. Applying these explicit ranges gives exactly the
$L_c,U_c$ appearing in the next table, six inner exceptional states in
each radius class. This is also checked by subtracting the generic
progression count (5) from the full interval count in every residue.
The table uses
$E$ for escape: in entries having no recorded return target, the orbit
leaves $B$ within the stated or next step. Signs and times on those escape
entries are irrelevant to cycle lifting.

| $s$ | Start | First normalized target | Time | Sign |
|---:|---|---|---:|---:|
| $0$ | $L_{-2}$ | $V_1$ | $1$ | $+$ |
| $0$ | $L_{-1}$ | $U_1$ | $1$ | $+$ |
| $0$ | $L_1$ | $U_{-1}$ | $7$ | $-$ |
| $0$ | $L_2$ | $U_{-2}$ | $9$ | $+$ |
| $0$ | $V_{-2}$ | $V_2$ | $1$ | $+$ |
| $0$ | $V_{-1}$ | $U_2$ | $1$ | $+$ |
| $0$ | $V_0$ | $E$ | — | — |
| $0$ | $U_1$ | $L_{-1}$ | $1$ | $-$ |
| $0$ | $V_1$ | $L_1$ | $2$ | $-$ |
| $0$ | $U_2$ | $E$ | — | — |
| $0$ | $V_2$ | $L_2$ | $2$ | $-$ |
| $1$ | $L_{-2},L_{-1}$ | $E$ | — | — |
| $1$ | $L_0$ | $V_1$ | $1$ | $+$ |
| $1$ | $L_1$ | $U_1$ | $1$ | $+$ |
| $1$ | $L_2$ | $U_0$ | $3$ | $-$ |
| $1$ | $V_{-1}$ | $V_2$ | $1$ | $+$ |
| $1$ | $U_0$ | $L_2$ | $13$ | $-$ |
| $1$ | $V_0$ | $U_2$ | $1$ | $+$ |
| $1$ | $V_1$ | $L_0$ | $2$ | $-$ |
| $1$ | $V_2$ | $E$ | — | — |
| $2$ | $L_{-2}$ | $E$ | — | — |
| $2$ | $L_{-1}$ | $V_1$ | $1$ | $+$ |
| $2$ | $L_0$ | $U_1$ | $1$ | $+$ |
| $2$ | $U_0$ | $L_1$ | $5$ | $-$ |
| $2$ | $V_0$ | $V_2$ | $1$ | $+$ |
| $2$ | $U_1$ | $L_0$ | $3$ | $+$ |
| $2$ | $V_1$ | $U_2$ | $1$ | $+$ |
| $2$ | $U_2$ | $L_{-1}$ | $1$ | $-$ |
| $2$ | $V_2$ | $E$ | — | — |

For precision, the non-immediate escape entries at $s=0$ are
$V_0\mapsto-[-R,2]$ in time $2$ and
$U_2\mapsto-[-R-1,2]$ in time $1$, followed by escape; at $s=1$,
$V_2\mapsto-[-R+1,2]$ in time $2$, followed by escape. At $s=2$,
$V_2$ escapes in time $2$. All $L$ escape entries escape in time $1$.

Every endpoint row follows from (1) and (4) with only one free variable
$R$. For example, at $s=1$, starting from $U_0=(R,R+1)$, the successive
second coordinates through the return are

$$
R+1,-R+2,-R,R-3,R-1,-R+3,-R+2,
R-2,R-3,-R+1,-R+3,R,R-2,-R-1.
$$

The last pair is $-L_2$, the elapsed time is $13$, and all intervening
second coordinates lie in $[-R,R]$ for the least possible radius $R=4$.
The other rows are generated and their interval inequalities checked in
`symbolic_corners.py`, independently retaining $R$ as an indeterminate.
For each residue its least permitted radius is used in every linear
inequality, so all six progressions, including their first members, are
covered.

### Step 5. Close the boundary graph when $R=3q$

The inner strip states with $e=0,3$ are precisely the $2q+1$ integers
$x\equiv0\pmod3$ in $[-R,R]$. Each is a normalized fixed point with
time $2$ and negative sign, hence gives one 4-cycle.

The endpoint cycle $L_{-1}\to U_1\to L_{-1}$ has total time $2$ and
negative sign. It gives one more 4-cycle. The cycle

$$
L_2\longrightarrow U_{-2}\longrightarrow V_{-2}
\longrightarrow V_2\longrightarrow L_2
$$

has respective times $9,2,1,2$ and signs $+,-,+,-$. It gives two
14-cycles. The $U_{-2}$ edge here is the $e=4$ strip row.

To exclude all other cycles, a generic $e=1$ state maps to $e=5$ by
$x\mapsto x-2$, then to the outer layer. Its outer coordinate is at most
$R-7<R-2$, so it escapes. A generic $e=2$ state maps to $e=4$ by
$x\mapsto x-4$, and its outer coordinate is at most $R-8<R-2$.
Of the $e=4,5$ states that immediately return to the outer layer, the only
ones not immediately escaping there are $U_{-2},U_{-1}$. The first lies
on the displayed 14-cycles; the second follows
$U_{-1}\to V_{-1}\to U_2\to E$. The remaining endpoint path is
$L_{-2}\to V_1\to L_1\to U_{-1}$, and $V_0$ escapes. Every section
state has now been assigned to a cycle or an escape path. The boundary
counts are $4:2q+2,14:2$.

### Step 6. Close the boundary graph when $R=3q+1$

The stationary $e=1$ strip has exactly $q-1$ coordinates: they are the
integers congruent to $R$ modulo $6$ from $-R+8$ to $R-6$. For $q=1$
this interval has no such integer, as required. Each stationary state has
time $18$ and negative sign, giving one 36-cycle.

The endpoint cycles $L_0\to V_1\to L_0$ and
$V_0\to U_2\to V_0$ each have time $3$ and negative sign; they give
two 6-cycles. The cycle $L_2\to U_0\to L_2$ has time $16$ and
positive sign, giving two 16-cycles.

The growing cycle is completely specified as follows. Begin with
$L_1\to U_1$, of time $1$ and positive sign. For
$j=0,\ldots,q$, put $a_j=R+1-6j$. These are all generic $e=2$ states,
and $a_q=-R+3$. Their time-2 edges go to $a_j-2$. For $0\le j<q$,
$a_j-2$ is a generic $e=0$ state and its time-6 edge goes to $a_{j+1}$.
For $j=q$, its target is $a_q-2=-R+1$, which is $L_1$ itself. Thus the
normalized cycle has $q+1$ edges of time $2$, $q$ edges of time $6$, and
the single initial edge of time $1$. Its total time is $8q+3$ and its
sign is $(-1)^{2q+1}=-1$. Its lift is therefore one primitive cycle of
length $16q+6$. The strict decrease by $6$ shows that the listed normalized
nodes do not repeat before closing; their residue distinction separates
the two interleaved strings. This proves both existence and uniqueness
within the exhaustive graph, not just long-cycle existence.

For completeness, every generic $e=0,2$ state is on that string: their
respective ranges in the correct residue classes are $-R+7$ through
$R-1$, and $-R+3$ through $R+1$. A generic $e=5$ state maps to $e=3$
then to the outer layer with outer coordinate at most $R-6<R-1$, and
escapes. Among generic $e=3,4$ states going to the outer layer, the only
one reaching an outer coordinate at least $R-1$ is $U_2$, already on the
second 6-cycle. The unused endpoint chain is $V_{-1}\to V_2\to E$;
$L_{-2},L_{-1}$ escape immediately. This exhausts the section. The
boundary counts are $6:2,16:2,36:q-1,(16q+6):1$.

### Step 7. Close the boundary graph when $R=3q+2$

For a generic $e=3$ coordinate $x$, its partner $x+1$ has $e=4$ and
returns to $x$. The two edges have times $6,2$ and signs $-,-$, giving
two 8-cycles per pair. The allowed $e=3$ coordinates run from $-R+5$
through $R-5$ in steps of $6$, giving exactly $q$ pairs. When $q=0$
the list is empty. These are all the generic $e=4$ coordinates as well.

The endpoint cycle $L_{-1}\to V_1\to U_2\to L_{-1}$ has time
$3$ and negative sign, giving one 6-cycle. The cycle
$L_0\to U_1\to L_0$ has time $4$ and positive sign, giving two
4-cycles.

Every generic $e=1$ coordinate maps to $e=0$, then to an outer coordinate
at most $R-3<R$. Every generic $e=2$ coordinate maps to $e=5$, then
to an outer coordinate at most $R-4<R$. The direct outer returns from
$e=0,5$ also have outer coordinates below $R$. All these paths escape
by the threshold in Step 4. The unused endpoint paths are
$U_0\to L_1\to E$, where $L_1$ is a generic $e=5$ state,
$V_0\to V_2\to E$, and $L_{-2}\to E$. This exhausts the section
and yields $4:2,6:1,8:2q$.

### Step 8. Exhaustiveness, small degrees and cardinality closure

Steps 2–3 classify exactly the periodic orbits avoiding $A$. Steps 4–7
classify every periodic orbit meeting $A$: the inner section is the
disjoint union of its residue strips and the listed exceptional endpoints;
all other outer section points escape in one step. Each return rule is
an identity on its entire integer strip, including its finite endpoints,
and every listed normalized cycle was proved primitive. No rational
periodic point is outside $B$ by Step 1. This proves the entire cycle graph.

For the potential small-radius alias issue, the inner exceptional labels
are pairwise distinct already at the least radius. For $s=0$, their largest
left coordinate is $-R+2$ and their smallest right coordinate is $R+1$,
with $R\ge3$. For $s=1$ these coordinates are $-R+2$ and $R$, with
$R\ge4$; for $s=2$ they are $-R$ and $R$, with $R\ge2$. Each gap is
strictly positive. Distinct offsets on the same side differ by nonzero
constants; outer states have a different second coordinate. The strip
complement argument separates these labels from all generic states.
The cycle strings in Steps 5–7 use distinct residues or strictly separated
endpoints; their potentially empty strings at $q=0,1$ were accounted for
explicitly. The certificate also checks the sign of each affine difference
between same-level corner labels at the least radius, which excludes any
zero at a larger admissible radius.

No cycle family in the tables has a negative multiplicity on the allowed
range of $q$. The growing period has $q\ge1$, so it is at least $22$
and never coincides with any other listed period, including $36$.
Repeated appearances of periods $4$ and $6$ across the three additive
tables refer to disjoint core and boundary cycles, so their multiplicities
must be added. All bounds and all exceptional central points were checked
at $R\ge2$ itself or at the least admissible radius in the relevant
residue class. In particular:

- $R=2$ has central cycles $1:1,3:2,10:1$ and boundary cycles $4:2,6:1$,
  giving $31$ points; the bulk and 8-cycle families are empty.
- $R=3$ has central cycles $1:1,5:2,6:1$, bulk $4:2$, and boundary
  $4:4,14:2$, giving $69$ points.
- $R=4$ has central cycles $1:1,3:2,10:1$, bulk $4:2,12:2$, and boundary
  $6:2,16:2,22:1$, giving $115$ points; the 36-cycle family is empty.

These are substitutions into the uniform parametrizations, not separate
degree-graph computations. Since the central part always contains $17$
points, the generic bulk point totals are respectively
$36q^2-28q$, $36q^2-4q$, and $36q^2+36q$. The boundary point totals are
$8q+36$, $52q+14$, and $16q+14$. Adding them gives exactly the three
claimed total cardinalities. Every periodic point belongs to exactly one
counted primitive cycle, and a primitive $\ell$-cycle contributes all
$\ell$ of its points to $\operatorname{Fix}(h_d^n)$ exactly when
$\ell\mid n$. This proves the formulas for $N_n(d)$ and $Z_d(u)$.
Therefore the claim follows. $\square$

## Appendix A. Complete positive-phase bulk affine table

The interval convention and exception test are those of Step 2. Empty
exception entries mean that the row has no point of proper-divisor period.
Every other point in a row has exactly its displayed generic period.

| $(e,f)$ | $\ell$ | $(L_x,U_x)$ | $(L_y,U_y)$ | Exceptional point: period |
|---|---:|---|---|---|
| $(0,0)$ | $4$ | $(0,0)$ | $(0,0)$ | $(0,0):1$ |
| $(0,1)$ | $12$ | $(1,-1)$ | $(2,0)$ | $(0,1):6$ |
| $(0,2)$ | $20$ | $(2,-2)$ | $(4,0)$ | $(0,2):5$ |
| $(0,3)$ | $4$ | $(0,0)$ | $(0,0)$ | — |
| $(0,4)$ | $20$ | $(2,-2)$ | $(0,-4)$ | $(0,-2):5$ |
| $(0,5)$ | $12$ | $(1,-1)$ | $(0,-2)$ | $(0,-1):6$ |
| $(1,0)$ | $12$ | $(2,0)$ | $(1,-1)$ | $(1,0):6$ |
| $(1,1)$ | $12$ | $(2,0)$ | $(2,0)$ | $(1,1):6$ |
| $(1,2)$ | $20$ | $(3,-1)$ | $(4,0)$ | $(1,2):5$ |
| $(1,3)$ | $20$ | $(0,-4)$ | $(2,-2)$ | — |
| $(1,4)$ | $20$ | $(0,-4)$ | $(3,-1)$ | — |
| $(1,5)$ | $20$ | $(3,-1)$ | $(1,-3)$ | $(1,-1):5$ |
| $(2,0)$ | $20$ | $(4,0)$ | $(2,-2)$ | $(2,0):5$ |
| $(2,1)$ | $20$ | $(4,0)$ | $(3,-1)$ | $(2,1):5$ |
| $(2,2)$ | $20$ | $(1,-3)$ | $(1,-3)$ | — |
| $(2,3)$ | $12$ | $(0,-2)$ | $(1,-1)$ | — |
| $(2,4)$ | $12$ | $(0,-2)$ | $(2,0)$ | — |
| $(2,5)$ | $20$ | $(1,-3)$ | $(4,0)$ | — |
| $(3,0)$ | $4$ | $(0,0)$ | $(0,0)$ | — |
| $(3,1)$ | $20$ | $(2,-2)$ | $(0,-4)$ | — |
| $(3,2)$ | $12$ | $(1,-1)$ | $(0,-2)$ | — |
| $(3,3)$ | $4$ | $(0,0)$ | $(0,0)$ | — |
| $(3,4)$ | $12$ | $(1,-1)$ | $(2,0)$ | — |
| $(3,5)$ | $20$ | $(2,-2)$ | $(4,0)$ | — |
| $(4,0)$ | $20$ | $(0,-4)$ | $(2,-2)$ | $(-2,0):5$ |
| $(4,1)$ | $20$ | $(3,-1)$ | $(0,-4)$ | — |
| $(4,2)$ | $12$ | $(2,0)$ | $(0,-2)$ | — |
| $(4,3)$ | $12$ | $(2,0)$ | $(1,-1)$ | — |
| $(4,4)$ | $20$ | $(3,-1)$ | $(3,-1)$ | — |
| $(4,5)$ | $20$ | $(0,-4)$ | $(1,-3)$ | $(-2,-1):5$ |
| $(5,0)$ | $12$ | $(0,-2)$ | $(1,-1)$ | $(-1,0):6$ |
| $(5,1)$ | $20$ | $(1,-3)$ | $(3,-1)$ | $(-1,1):5$ |
| $(5,2)$ | $20$ | $(4,0)$ | $(1,-3)$ | — |
| $(5,3)$ | $20$ | $(4,0)$ | $(2,-2)$ | — |
| $(5,4)$ | $20$ | $(1,-3)$ | $(0,-4)$ | $(-1,-2):5$ |
| $(5,5)$ | $12$ | $(0,-2)$ | $(0,-2)$ | $(-1,-1):6$ |

## Corrections or Missing Assumptions

No extra mathematical assumption or degree restriction was introduced.
The claim is for the frozen factorial-product definition, not for an
implicit phase-normalized family. An independent review is still required
before admission or manuscript work.

## Source Ownership and Exact Caveat

The polynomial family, many-point construction, rational/integer escape
box, and existence of the growing cycle are owned by
Kim–Krieger–Postolache–Szeto. Specifically, Corollary 4.3 owns the rational
integer box, Theorem 5.1 owns long-cycle existence, and Proposition 5.2
already owns the full positive-phase bulk residue/period classification,
including its 17 central exceptional points. Those inputs and their
elementary rederivations here are deducted. The proposed increment is the
all-radius clipped bulk multiplicities together with the exhaustive
boundary endpoint graph and hence every rational cycle multiplicity.
[Primary article, v2](https://arxiv.org/html/2412.01668v2)

The accessed v2 contains conflicting numerical information: its Theorem 4.4
implies at least $225$ points when $d=13$, whereas its later exact-count
remark gives $153$. The complete classification above gives $271$.
The report is version-specific; it does not assert that no corrected
version exists or accuse an unseen journal version of the same issue.
The original bounded audit, including the PDF check, remains in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md).
The served HTML's arXiv header says 8 July 2025, while its internal Date
field says August 24, 2026. These are recorded separately, without inferring
a corrected final publication from that metadata discrepancy.

## Verification and Open Risks

The author ran `python -B verify_symbolic_certificate.py` successfully.
It checks symbolic affine bulk identities and all proper-period equations;
compares all 36 free-strip identities with the compressed table; checks the
exact residue-strip complements, all endpoint return rows and all constant
endpoint cycles with inequalities valid for every admissible radius;
checks corner disjointness and the 17 central points' radius bound; and
derives the boundary point-count polynomials from exact progression counts
and checked cycle lifts. It then verifies the total cardinality polynomials.
It does not enumerate any numerical degree graph.
The long-chain proof and exhaustive escape routing are explicitly given
in Steps 5–7; they are not inferred by that script from a sampled graph.

Remaining review risks are finite-table transcription, sign-lift conventions,
and the scope of worldwide novelty. These are review targets, not missing
lemmas in the stated argument. No target Euler product, root number,
automorphy, target zero divisor or Hilbert–Pólya operator is supplied by
this source-cycle result. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
