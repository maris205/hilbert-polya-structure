# Addendum: all monic integral conservative quadratic Hénon maps

## Claim, status, and relation to the main proof

This addendum extends the **same classification question**, not a second
paper contract. Its main-proof input is Section 4 of
`PROOF_INTEGER_HENON.md`: the exact periodic classification of the two
local symbol equations (7)--(8). That finite-symbol argument is independent
of whether the positive center $r$ is integral or half-integral.

**Proof status: PROVABLE AS STATED, pending non-author review.** The
infinite-parameter odd branch is proved in Sections 2--3 below. All
seventeen small odd-branch parameters have a specified finite-graph
certificate in Section 4. No prior-work or batch-admission verdict is
inferred from this proof status.

**Full classification theorem.** For arbitrary $a,b\in\mathbb Z$, consider
$$
H_{a,b}(x,y)=(y,y^2+by+a-x).
$$
Write uniquely $b=2q+e$ with $q\in\mathbb Z$, $e\in\{0,1\}$, and put
$$
A=a-q^2+(2-e)q. \tag{A1}
$$
Under the integer translation $T_q(x,y)=(x+q,y+q)$ one has
$$
T_q\circ H_{a,b}\circ T_q^{-1}=H_{A,e}. \tag{A2}
$$
If $e=0$, the table in `PROOF_INTEGER_HENON.md` is the complete list of
rational cycles of $H_{A,0}$. If $e=1$, the following table is the complete
list of rational cycles of $H_{A,1}$, with the same coordinate-word
convention as in that proof:

| Parameter | Coordinate words | Ranges and exact periods |
|---|---|---|
| $A=-k(k+1)$ | $(-k)$ and $(k+1)$ | $k\geq0$; two distinct fixed points |
| $A=-k(k+1)-4$ | $(-k-2,k-1)$ | $k\geq0$; period $2$ |
| $A=-k(k+1)-2$ | $(-k-2,k,k)$ | $k\geq0$; period $3$ |
| same parameter | $(k-1,-k-1,-k-1)$ | $k\geq1$; a second period-$3$ orbit |
| $A=-k(k+1)-1$ | $(-k-1,-k-1,k,k)$ | $k\geq0$; period $4$ |

Every coordinate in these normalized words is translated back by $-q$
to obtain the cycles of $H_{a,b}$. At overlapping parameters the union
of the rows is intended. In the odd branch the overlaps are exactly
$A=-2,-4,-6$, with respectively $5,8,4$ rational periodic points. In
particular, for the entire two-parameter integral family,
$$
\#\operatorname{Per}(H_{a,b},\mathbb Q)\leq8,
$$
with equality if and only if $b=2q+1$ and $a-q^2+q=-4$. Every rational
periodic point is integral and has exact period $1$, $2$, $3$, or $4$.

This is a classification for the displayed maps with integral $a,b$ and
coefficient of $y^2$ exactly $1$. It is not a statement for arbitrary
quadratic polynomial automorphisms, arbitrary leading coefficients,
nonintegral rational coefficients, or Jacobian determinant $-1$.

## 1. Normalization and elementary reductions

Substitution of $x=u-q$, $y=v-q$ gives the second coordinate of (A2) as
$$
v^2+(b-2q)v+a+q^2-bq+2q-u
=v^2+ev+A-u,
$$
which proves (A1)--(A2). The translation preserves both $\mathbb Q^2$
and $\mathbb Z^2$ and preserves exact periods.

For a rational periodic coordinate sequence of $H_{a,b}$, the equation is
$$
x_{i-1}+x_{i+1}=x_i^2+bx_i+a.
$$
At a $p$-adic maximum $M>1$, the quadratic term has norm $M^2$ and the
remaining two terms have norms at most $M$ and $1$. The right side has
norm $M^2$, whereas the left side has norm at most $M$. This contradiction
proves integrality for every $a,b\in\mathbb Z$.

The even branch is now precisely the main proof. In the odd branch set
$b=1$ and retain $A$ for its constant parameter. Summation around a
period gives
$$
\sum_i(x_i-\tfrac12)^2=n(\tfrac14-A). \tag{A3}
$$
For integer $x_i$, every summand is at least $1/4$. Thus $A>0$ is
impossible. If $A=0$, every coordinate is $0$ or $1$. The recurrence
forces both neighbors of a $0$ to be $0$, and both neighbors of a $1$
to be $1$, so the only orbits are the fixed points $(0,0)$ and $(1,1)$.

For $A\leq-1$ use the half-integer coordinates
$$
u_i=x_i+\tfrac12\in\mathbb Z+\tfrac12,
\qquad c=-A-\tfrac34.
$$
Their recurrence is
$$
u_{i-1}+u_{i+1}=u_i^2-c. \tag{A4}
$$
Writing $R=\max_i|u_i|\in\mathbb Z+\tfrac12$ gives exactly as in the
main proof
$$
R\leq1+\sqrt{1+c},\qquad |u_i^2-c|\leq2R. \tag{A5}
$$

## 2. Uniform half-integer reduction for every $A\leq-17$

Since $c=N+1/4$ for the nonnegative integer $N=-A-1$, there is a unique
$k\geq0$ with
$$
k^2\leq N\leq k^2+2k.
$$
These integer intervals are adjacent and disjoint. Put
$$
r=k+\tfrac12,\qquad s=c-r^2=N-k(k+1).
$$
Then $s\in\mathbb Z$ and
$$
-k\leq s\leq k,
\quad\hbox{equivalently}\quad -r+\tfrac12\leq s\leq r-\tfrac12. \tag{A6}
$$
If $A\leq-17$, then $N\geq16$ and $k\geq4$, so $r\geq9/2$.

For $s\leq-2$, equation (A5) gives $R<r+1$. Since $R$ and $r$ are
half-integers, $R\leq r$. For $s\geq-1$, the upper bound in (A6) gives
$c+1<(r+1)^2$, hence $R<r+2$ and $R\leq r+1$.

If $|u_i|\leq r-2$ and $s\leq-2$, then
$$
u_i^2-c\leq-4r+4-s\leq-3r+\tfrac72<-2r\leq-2R.
$$
If $|u_i|\leq r-2$ and $s\geq-1$, then
$$
u_i^2-c\leq-4r+5<-2r-2\leq-2R.
$$
Both strict inequalities use $r\geq9/2$ and contradict (A5). Absolute
values of the coordinates have the same half-integral parity as $r$.
It follows that there are unique symbols
$$
u_i=\varepsilon_i r+\delta_i,
\quad\varepsilon_i\in\{-1,1\},\quad\delta_i\in\{-1,0,1\}. \tag{A7}
$$

Substitution into (A4) yields
$$
r(\varepsilon_{i-1}+\varepsilon_{i+1}-2\varepsilon_i\delta_i)
=\delta_i^2-\delta_{i-1}-\delta_{i+1}-s. \tag{A8}
$$
The coefficient on the left is an even integer. The right side is an
integer in $[-r-3/2,r+5/2]$, strictly between $-2r$ and $2r$. Therefore
the even coefficient vanishes even though $r$ is a half-integer. We
obtain the **same two local equations** as in the main proof:
$$
\varepsilon_{i-1}+\varepsilon_{i+1}=2\varepsilon_i\delta_i,
\qquad\delta_{i-1}+\delta_{i+1}=\delta_i^2-s. \tag{A9}
$$
Thus $s\in\{-2,-1,0,1,2,3\}$, and the direct classification in its
Section 4 applies without alteration. The cases $s=-2,2$ are empty;
$s=-1,0,1,3$ give fixed, four-, three-, and two-cycles, respectively.

## 3. Translating the local classification and checking existence

Since $r=k+1/2$ and $x_i=u_i-1/2$, the parameter identity is
$$
A=-k(k+1)-1-s. \tag{A10}
$$
The four allowed $s$ values and their local words therefore give exactly
the table at the beginning of this addendum for all $A\leq-17$.

Existence for the entire stated ranges, including small $k$, can be
checked before imposing the large-parameter bounds: the centered words
from Section 5 of the main proof satisfy (A4) algebraically for every
positive real $r$. Substituting $r=k+1/2$ and translating by $-1/2$
proves (A4) and hence the original recurrence for each displayed word.
The first and second entries in a period-two word differ by $2k+1$,
so its exact period is $2$ for all $k\geq0$. The first period-three word
has unequal entries for every $k\geq0$. The second period-three word
is constant when $k=0$ and nonconstant for $k\geq1$: this is why the
second word has the different range in the table. At $k=0$, it is the
fixed word $(-1)$ for $A=-2$, already counted in the fixed-point row
at $k=1$. The four-cycle has neither period $1$ nor period $2$, since
$-k-1\ne k$ for every $k\geq0$.

## 4. Complete exact certificate for $-16\leq A\leq0$

Set $z_i=2u_i=2x_i+1$, which is odd. For $A\leq0$ define the integer
bound and alphabet
$$
B_A=2+\lfloor\sqrt{1-4A}\rfloor,
$$
$$
S_A=\{z\in\mathbb Z:z\text{ odd},\ |z|\leq B_A,
               \ |z^2+4A+3|\leq4B_A\}.
$$
Equation (A5) proves the bound. The doubled recurrence is
$$
2(z_{i-1}+z_{i+1})=z_i^2+4A+3,
$$
so on pairs of odd integers the map is
$$
G_A(z,w)=\left(w,\frac{w^2+4A+3}{2}-z\right). \tag{A11}
$$
The fraction is an even integer, hence the output coordinate is odd.
This map is injective, with inverse obtained by solving (A11) for $z$.
Starting with $V_0=S_A\times S_A$, use the finite pruning recurrence
$$
V_{j+1}=\{p\in V_j:G_A(p)\in V_j\}. \tag{A12}
$$
The proof in Section 6 of the main document shows that its stable set
is exactly the complete periodic set, with no imposed maximum period.
The following table records all seventeen cases. The words are in the
original integer coordinates $x=(z-1)/2$, not in doubled coordinates.

| $A$ | $B_A$ | Successive sizes through stabilization | Stable coordinate words |
|---|---|---|---|
| $0$ | $3$ | $16,8,5,3,2$ | $(0)$; $(1)$ |
| $-1$ | $4$ | $16,12,9,8,7,6,5,4$ | $(-1,-1,0,0)$ |
| $-2$ | $5$ | $36,22,17,13,10,8,7,6,5$ | $(-1)$; $(2)$; $(-2,0,0)$ |
| $-3$ | $5$ | $36,24,17,14,12,10,8,6,5,4$ | $(-2,-2,1,1)$ |
| $-4$ | $6$ | $36,22,14,8$ | $(-2,-1)$; $(-3,1,1)$; $(-2,-2,0)$ |
| $-5$ | $6$ | $36,20,12,8,5,2,1,0$ | none |
| $-6$ | $7$ | $64,32,18,11,8,5,4$ | $(-2)$; $(3)$; $(-3,0)$ |
| $-7$ | $7$ | $64,32,18,14,10,8,6,4$ | $(-3,-3,2,2)$ |
| $-8$ | $7$ | $64,28,14,7,6$ | $(-4,2,2)$; $(-3,-3,1)$ |
| $-9$ | $8$ | $64,24,10,4,2,0$ | none |
| $-10$ | $8$ | $36,6,2$ | $(-4,1)$ |
| $-11$ | $8$ | $36,8,2,0$ | none |
| $-12$ | $9$ | $64,22,10,4,2$ | $(-3)$; $(4)$ |
| $-13$ | $9$ | $36,20,14,12,10,8,6,4$ | $(-4,-4,3,3)$ |
| $-14$ | $9$ | $36,20,12,6$ | $(-5,3,3)$; $(-4,-4,2)$ |
| $-15$ | $9$ | $36,12,6,4,2,0$ | none |
| $-16$ | $10$ | $36,4,2$ | $(-5,2)$ |

`integer_henon_odd_check.py` specifies these expected sets and verifies
them by (A12), including the point sets rather than just their sizes.
It separately enumerates the partial functional graph by path following
and verifies the cycle words. The all-parameter assertion, however,
depends on Sections 2--3, not on extrapolation of any finite computation.

## 5. All overlaps and the sharp eight-point bound

Let $P(k)=k(k+1)$ for $k\geq0$. It is even and strictly increasing.
Thus the four-cycle row, whose offset is odd, cannot intersect the fixed,
two-, or three-cycle rows, whose offsets are even. Intersections of the
remaining rows reduce to a difference of two pronic numbers equal to
$2$ or $4$. For $k>\ell\geq0$,
$$
P(k)-P(\ell)=(k-\ell)(k+\ell+1). \tag{A13}
$$
The only solution of difference $2$ is $(k,\ell)=(1,0)$, and the only
solution of difference $4$ is $(2,1)$: these follow by listing the
positive factor pairs of $2$ and $4$ in (A13).

Fixed and three-cycle rows therefore intersect only at $A=-2$, where
there are two fixed points and one nonconstant three-cycle. Fixed and
two-cycle rows intersect only at $A=-6$, with two fixed points and one
two-cycle. Three- and two-cycle rows intersect only at $A=-4$, with two
three-cycles and one two-cycle. There is no triple intersection.
Outside these cases there are at most six periodic points, and at
$A=-4$ there are exactly eight. The even-branch maximum is seven by the
main proof. Translation (A2) now proves the complete sharp bound and its
equality locus for all $a,b\in\mathbb Z$.

The finite-orbit native-time counting and rational-point zeta corollary
in the main proof applies with the cycle multiplicities in these tables.
No target arithmetic identification or additional paper contract follows.

## Open risks

The half-integer bounds, exact small point sets, and parameter overlaps
require independent review. Full-family prior ownership remains a
separate gate, including results stated in differently normalized
integral coordinates. The coefficient-$1$, determinant-$+1$ hypotheses
must not be dropped merely because the affine translation is elementary.
