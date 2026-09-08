# Proof Package: LY4 short-period atlas and the remaining exhaustion lemma

## Claim

For every integer $a$, classify, up to cyclic rotation, every periodic
sequence $(x_i)_{i\in\mathbb Z}$ of nonzero integers satisfying
$$x_i x_{i+3}=a+x_{i+1}+x_{i+2}.\tag{1}$$
The classification must be necessary and sufficient, include all
exceptional parameters and ordinary-domain conditions, and specify
native least periods. This is the unchanged
[original LY4 contract](../../continuation_round4/third_order_lyness/FROZEN_CONTRACT.md).

## Status

**NOT CURRENTLY JUSTIFIED for the full claim.**

The following complete strata are proved below:

1. Every ordinary integral orbit of least period at most six.
2. Every ordinary integral orbit at $a=1$, including the entire locus
   meeting $-1$ and the entire positive locus.
3. There is no least-period-eight ordinary integral orbit at $a\ne1$.

These are **PROVABLE AS STATED** auxiliary results. They do not exclude
least periods $7,9,10,\ldots$ at $a\ne1$. In particular the frozen
closing lemma E, asserting that all periods outside $a=1$ are at most
six, remains unproved. The results here are not a fourth admission.

## Assumptions and notation

All coordinates are nonzero integers, and every forward and backward
step is an ordinary evaluation of (1). No canceled singular expression
is interpreted as a continuation through zero. A cyclic word represents
the two-sided sequence obtained by repeating it. Equivalence is by
rotation only; reversal is used as a proof device, not an orbit quotient.

The scalar least period equals the least period of consecutive triples.
We use the already independently checked identities
$$x_{i+1}(x_{i+4}+1)=x_{i+3}(x_i+1),\qquad
\kappa_i=\frac{(x_i+1)(x_{i+2}+1)}{x_{i+1}},\qquad
\kappa_{i+2}=\kappa_i.\tag{2}$$
If the least period exceeds two and no coordinate is $-1$, both
alternating values of $\kappa_i$ are nonzero integers. The proof and
its precise hypotheses are in the fourth-pass
[Step 2](../../continuation_round4/third_order_lyness/PROOF_PACKAGE.md)
and [independent helper review](../../continuation_round4/third_order_lyness/INDEPENDENT_HELPER_REVIEW.md).
This proof is reused, not rerun or represented as new fifth-pass work.

## Proof strategy and dependency map

1. Periods one/two are direct substitutions. Period six is a complete
   factorization of the cyclic equations into linear branches.
2. Period five uses the constant value of the classical two-integral,
   a direct fifth-iterate identity for the second-order Lyness map,
   signs, and an integer divisibility argument.
3. At $a=1$, a direct identity gives the eight-step law. The $-1$
   stratum is treated without dividing by a zero plus-factor. Off that
   stratum, signs force positivity. A divisor atlas then has an exact
   analytic bound and is completed by hand cases, not by a census.
4. The period-eight exclusion for $a\ne1$ uses only an exact two-step
   recurrence and the already checked $-1$ stratum.
5. Full LY4 additionally requires lemma E in Section 7. No statement in
   Sections 1–6 proves E. No rational-torsion or elliptic-curve source
   theorem is used in these elementary proofs.

## 1. Complete words of periods dividing two and six

### 1.1 Periods dividing two

For $p,q\in\mathbb Z\setminus\{0\}$, the word $(p,q)$ satisfies (1)
exactly when
$$a=pq-p-q.\tag{3}$$
Its least period is one if $p=q$ and two otherwise. This includes every
constant word, whose parameter is $a=p^2-2p$.

### 1.2 Six-period classification

Every ordinary integral word whose period divides six is either a word
from (3), or a rotation of
$$W(r,s)=(r,-r-1,r,s,-s-1,s),\qquad
a=rs+1,\qquad r,s\in\mathbb Z\setminus\{0,-1\}.\tag{4}$$
For (4), the least period is three if $s=r$, two if $s=-r-1$, and six
in every other case. The two exceptional equalities cannot both hold
for integral $r$.

**Proof.** Write a six-word as $(p,q,r,d,e,f)$. Equations (1) at
opposite positions have equal left sides; hence
$$q+r=e+f,\qquad r+d=f+p,\qquad d+e=p+q.$$
Putting $t=d-p$ gives
$$d=p+t,\qquad e=q-t,\qquad f=r+t.\tag{5}$$
The first three cyclic equations become
$$p^2+pt=a+q+r,\qquad
q^2-qt=a+r+p+t,\qquad r^2+rt=a+p+q.$$
Subtracting in pairs gives the exact products
$$\begin{aligned}
(p-r)(p+r+t+1)&=0,\\
(p+q+1)(p-q+t)&=0,\\
(q+r+1)(q-r-t)&=0.
\end{aligned}\tag{6}$$

If $p=r$, the last two equations coincide. The branch $q=p+t$ in
(5) gives $(p,q,p,q,p,q)$, of period dividing two. The other branch
$q=-p-1$ gives $W(p,p+t)$.

If $p\ne r$, the first equation forces $t=-p-r-1$. If $p+q+1=0$,
then $q=-p-1$, and (5) gives
$$(p,-p-1,r,-r-1,r,-p-1).$$
Its rotation starting at the third coordinate is $W(r,-p-1)$.
If instead $p-q+t=0$, then $q=-r-1$ and (5) gives
$$(p,-r-1,r,-r-1,p,-p-1).$$
Its rotation starting at the second coordinate is $W(-r-1,p)$.
These branches exhaust (6), including intersections. Nonzero entries
in (4) are equivalent to the two exclusions on $r,s$.

For sufficiency, the first, second and third parameter expressions
$x_i x_{i+3}-x_{i+1}-x_{i+2}$ for (4) are respectively
$$rs-(-r-1)-r,
\quad(-r-1)(-s-1)-r-s,
\quad rs-s-(-s-1),$$
all equal to $rs+1$. The remaining three expressions exchange $r$
and $s$ in these same displayed expressions and therefore also equal
$rs+1$. The word has period three exactly when $s=r$. It has period
two exactly when $s=-r-1$: equality of its even positions already
requires this condition. It cannot be constant because $r=-r-1$ has
no integer solution. Every proper least period dividing six is one,
two or three, proving the assertion. $\square$

Thus the fourth-pass unbounded family is the subfamily $r=1,s=M-1$,
followed by a rotation. It is not the only six-period channel: (4)
classifies the entire channel. In particular all genuine six-cycles
avoid $-1$, and all least-three words are rotations of
$(r,r,-r-1)$ at $a=r^2+1$.

## 2. Complete period-five stratum

There is exactly one oriented integral orbit of least period five:
$$(-2,-2,-3,-4,-3),\qquad a=13.\tag{7}$$
Reversing this particular word gives a rotation, but reversal is not
imposed as an equivalence in the classification.

**Proof.** If one coordinate were $-1$, (2) would propagate $-1$
every four positions. Since four is relatively prime to five, every
coordinate would be $-1$, contradicting least period five. Thus no
coordinate equals $-1$.

Since $\kappa_i$ has periods two and five, it is constant. Write
$A=-\kappa_i\ne0$, put $z_i=-x_i-1$, and set $y_i=z_i/A$. Then
$$y_i y_{i+2}=y_{i+1}+c,\qquad c=1/A\ne0.\tag{8}$$
All $y_i$ are nonzero. For the second-order recurrence (8) starting at
$(y_0,y_1)=(v,w)$, direct successive substitution gives
$$y_5-v=
\frac{v(c-1)\bigl(w^2+(c-1)w-cv-c\bigr)}
{(c+w)(cv+c+w)}.\tag{9}$$
The factors $c+w$ and $cv+c+w$ are nonzero on the ordinary orbit:
they are $v y_2$ and $vw y_3$, respectively.

Suppose $c\ne1$. The fifth-period condition and (9), applied at every
cyclic position, imply
$$y_i^2+(c-1)y_i-cy_{i-1}-c=0.\tag{10}$$
The reversed sequence also satisfies (8) and is an ordinary
five-periodic sequence. Applying the same explicitly stated identity
to that sequence gives
$$y_i^2+(c-1)y_i-cy_{i+1}-c=0.$$
Subtracting and using $c\ne0$ gives $y_{i-1}=y_{i+1}$ for every $i$.
The sequence then has periods two and five and is constant, a
contradiction. Therefore $c=1$ and $A=1$.

Now $z_i z_{i+2}=z_{i+1}+1$ with
$z_i\in\mathbb Z\setminus\{0,-1\}$. On this integer domain $z_i+1$
has the same sign as $z_i$. If $\epsilon_i$ denotes the sign of $z_i$,
then $\epsilon_i\epsilon_{i+1}\epsilon_{i+2}=1$, so
$\epsilon_{i+3}=\epsilon_i$. Combining this with period five makes
the sign constant, and its triple product makes that sign positive.
All $z_i$ are positive integers.

Multiplying the five recurrence equations and dividing by the
nonzero product of the coordinates gives
$$\prod_{i=0}^4 z_i=\prod_{i=0}^4(1+1/z_i).\tag{11}$$
If every $z_i\ge2$, the left side is at least $2^5$ and the right
side at most $(3/2)^5$, which is impossible. Rotate to $z_0=1$ and
write $z_1=b\ge1$. The next coordinates are
$$z_2=b+1,\qquad z_3=1+2/b.$$
Thus $b$ divides two, so $b=1$ or $b=2$. Both choices give rotations
of $(1,1,2,3,2)$. Converting back gives (7). Direct substitution of
(7) in (1) gives $a=13$ at all five positions. It is nonconstant
and five is prime, so its least period is five. $\square$

## 3. Period four and the known $-1$ stratum outside $a=1$

If a word has period four, (2) reads
$$(x_i+1)(x_{i+1}-x_{i+3})=0.$$
If no coordinate equals $-1$, each parity is constant and the period
divides two. Thus every genuine four-cycle meets $-1$.

The fourth-pass complete proof establishes that, for $a\ne1$, every
ordinary integral periodic word meeting $-1$ is a rotation of
$$(-1,b,-1,d),\qquad d=1-a-b,\qquad b,d\ne0.\tag{12}$$
The least period is four if $b\ne d$, two if $b=d\ne-1$, and one if
$b=d=-1$. We use that exact previously reviewed stratum unchanged.
Section 4 below treats its exceptional parameter $a=1$, rather than
extending the excluded Möbius argument to it.

Together Sections 1–4 account for every least period at most six.

## 4. The entire exceptional parameter $a=1$

At $a=1$, every ordinary integral periodic orbit is a rotation of one
of the following words:

| Word or family | Restrictions | Least period |
| --- | --- | --- |
| $(2,3)$ | none | $2$ |
| $(-1,b,-1,-b)$ | $b\in\mathbb Z\setminus\{0\}$ | $4$ |
| $(-1,b,1,-b-2,-1,-b-2,1,b)$ | $b\in\mathbb Z\setminus\{-2,-1,0\}$ | $8$ |
| $(1,4,1,6,2,9,2,6)$ | none | $8$ |
| $(1,2,1,4,3,8,3,4)$ | none | $8$ |
| $(1,2,2,5,4,5,2,2)$ | none | $8$ |
| $(1,1,1,3,5,9,5,3)$ | none | $8$ |

The parameterizations may name the same rotated orbit more than once:
$b$ and $-b$ do so in the four-family, and $b$ and $-b-2$ do so in
the eight-family. No quotient by an unrelated symmetry is intended.

### 4.1 A direct eight-step identity

For $a=1$, put $(X,Y,Z)=(x_i,x_{i+1},x_{i+2})$ and $u=\kappa_i$.
Two substitutions in (1) give
$$x_{i+4}
=\frac{X(1+Z)+(1+Y+Z)}{XY}
=\frac{(X+1)(Z+1)+Y}{XY}
=\frac{u+1}{X}.\tag{13}$$
This identity divides only by the nonzero ordinary coordinates $X,Y$.
In particular $u+1\ne0$ on an ordinary orbit. Since $\kappa_{i+4}=u$,
applying (13) twice yields $x_{i+8}=x_i$. This recovers the classical
order-eight law directly on the actual ordinary domain. It is not
by itself an integral classification.

### 4.2 The locus meeting $-1$

Suppose $x_0=-1$. Propagation in (2) permits an eight-word in blocks
$$(-1,b_j,c_j,d_j),\qquad d_j=-1-b_j-c_j,$$
where the block index is periodic. The exact relation between blocks is
$$c_j(b_{j+1}+1)=-(b_j+1).\tag{14}$$

If no $b_j=-1$, multiply (14) over all blocks. Its canceled factors
are nonzero, so the product of the nonzero integers $c_j$ is $1$ or
$-1$, and each $c_j$ equals $1$ or $-1$. If one $c_j=-1$, four-step
propagation makes all of them $-1$. Then (14) makes $b_j$ constant,
and the word is $(-1,b,-1,-b)$. If none is $-1$, all are $1$;
(14) gives $b_{j+1}=-b_j-2=d_j$. This is exactly
$$(-1,b,1,-b-2,-1,-b-2,1,b).\tag{15}$$
Nonzero coordinates require $b\ne0,-2$. The present branch excludes
$b=-1$; allowing it in (15) gives a four-family word already listed.

If some $b_j=-1$, (14) and periodicity force every $b_j=-1$. Now
$$d_j=-c_j,\qquad c_{j+1}=1/c_j,$$
by (1). Integrality and nonzero coordinates force $c_j=1$ or $-1$.
The resulting words are rotations of $(-1,-1,-1,1)$, already in the
four-family. This exhausts the block branches.

Every displayed four-family word has least period four: a two-period
word would require $b=-b$, which is excluded. For (15), a period-four
word requires $b=-b-2$, or $b=-1$; periods one/two would also require
$-1=1$ at its first and third positions. Thus the permitted parameters
in the table give least period eight. For sufficiency, the eight values
$x_i x_{i+3}-x_{i+1}-x_{i+2}$ in (15) reduce in order to
$$1,\ 1,\ 1,\ 1,\ 1,\ 1,\ 1,\ 1,$$
using $(-b-2)(-1)=b+2$ and $b+(-b-2)=-2$; direct four-position
substitution gives the same parameter for the four-family. All listed
denominators remain nonzero by the parameter exclusions.

### 4.3 Off the $-1$ locus, positivity is forced

Let $z_i=-x_i-1$, and let $\epsilon_i$ be its sign. All $z_i$ and
$z_i+1$ are nonzero integers of the same sign. Let
$\alpha_i$ be the sign of $-\kappa_i$; it has period two. The
transformed recurrence gives
$$\epsilon_i\epsilon_{i+1}\epsilon_{i+2}=\alpha_i.$$
Dividing two consecutive equations shows
$$\epsilon_{i+3}=\rho\epsilon_i,
\qquad \rho=\alpha_{i+1}/\alpha_i\in\{1,-1\},$$
where $\rho$ does not depend on $i$. Hence the signs have period six.
By (13) they also have period eight, and therefore have period two.
On each parity the $x_i$ are consequently either all positive or all
at most $-2$.

Both parities cannot be negative: the left side of (1) would be
positive and the right side at most $1-2-2=-3$. If exactly one parity
is negative, rotate to write
$$x_{2j}=-E_j,\qquad E_j\ge2,\qquad
x_{2j+1}=P_j,\qquad P_j\ge1.$$
Equation (1) at the even position gives
$$E_{j+1}=1+P_j+E_jP_{j+1}>E_j.$$
This strict increase contradicts periodicity. Thus all coordinates
are positive integers.

For a word of period dividing two, (3) at $a=1$ is
$$(p-1)(q-1)=2.$$
Its integer solutions in the nonzero ordinary domain are exactly
$(p,q)=(2,3),(3,2)$. The negative factor pairs would give a zero
coordinate, and the equation has no constant integer solution.
It remains to classify positive words of period greater than two;
for these $u=\kappa_0$ is a positive integer by the reused integrality
lemma. Put $K=u+1\ge2$.

### 4.4 Exact divisor atlas for the positive locus

From (13), four successive even coordinates have the form
$$p,\ q,\ K/p,\ K/q,\qquad p,q\text{ positive divisors of }K.$$
The odd coordinates are forced by (2), giving the full word
$$\begin{aligned}
(&p,\ \frac{(p+1)(q+1)}{K-1},\ q,
\ \frac{(q+1)(K/p+1)}{K-1},\\
 &K/p,\ \frac{(K/p+1)(K/q+1)}{K-1},\ K/q,
\ \frac{(K/q+1)(p+1)}{K-1}).
\end{aligned}\tag{16}$$
All four displayed quotients must be positive integers. Conversely,
whenever they are, (16) satisfies (1) at $a=1$. To verify both parity
types, for its first four entries $X,Y,Z,W$ one has
$$XW-Y-Z
=\frac{(q+1)(K+p)-(p+1)(q+1)}{K-1}-q=1,$$
and
$$Y(K/p)-Z-W
=\frac{(q+1)\{K(p+1)/p-(K/p+1)\}}{K-1}-q=1.$$
Rotating the four even coordinates replaces $(p,q)$ successively by
$(q,K/p)$, $(K/p,K/q)$ and $(K/q,p)$, so these two verified identities
cover all eight positions.

Suppose first every coordinate is at least two. Among the opposite
pair $p,K/p$ one is at most $\sqrt K$, and among $q,K/q$ one is at
most $\sqrt K$. Chosen entries from these two pairs are adjacent in
the cyclic even-coordinate list. Rotate to make them the first two
entries. Then $2\le p,q\le\sqrt K$, and the first odd quotient is
at least two, so
$$2(K-1)\le(p+1)(q+1)\le(\sqrt K+1)^2.$$
This is equivalent to $(\sqrt K-3)(\sqrt K+1)\le0$, giving $K\le9$.
Since both factors of $K=p(K/p)$ are at least two, $K\ge4$.
The complete hand cases are:

| $K$ | Possible $p,q$ in $[2,\sqrt K]$ | First odd quotient |
| --- | --- | --- |
| $4$ | $p=q=2$ | $3$ |
| $5$ | none | — |
| $6$ | $p=q=2$ | $9/5$ |
| $7$ | none | — |
| $8$ | $p=q=2$ | $9/7$ |
| $9$ | $p=q=3$ | $2$ |

The two integral cases give only rotations of $(2,3)$. Thus every
remaining positive orbit contains a coordinate one.

Rotate such an orbit to $p=1$ in (16). The first and last odd
coordinates being at least one give
$$K-1\le2(q+1),\qquad
K-1\le2(K/q+1).\tag{17}$$
If $K\ge10$, the second inequality gives
$$q\le\frac{2K}{K-3}\le\frac{20}{7}<3.$$
Thus $q\le2$, and the first inequality would give $K-1\le6$, a
contradiction. Hence $2\le K\le9$. With $q$ a positive divisor of
$K$, every remaining case is the following hand divisor table:

| $K$ | Divisors $q$ making $2(q+1)/(K-1)$ integral | Remaining odd quotients |
| --- | --- | --- |
| $2$ | $1,2$ | integral for both |
| $3$ | $1,3$ | integral for both |
| $4$ | $2$ | integral |
| $5$ | $1,5$ | integral for both |
| $6$ | none | — |
| $7$ | none | — |
| $8$ | none | — |
| $9$ | $3$ | integral |

The first four rows give the four positive eight-words in the theorem;
the row $K=9,q=3$ is a rotation of the last of them. The multiple
choices of $q$ in the other rows give rotations, not extra orbits.
Formula (16) proves sufficiency without any numerical orbit test.
Each of these four words has a coordinate value occurring exactly
once ($9,8,4,9$, respectively). Consequently none can have a proper
period dividing eight. Their distinct multisets show they are four
different oriented orbits. This completes the $a=1$ atlas. $\square$

## 5. Explicit atlas for every least period at most six

Sections 1–4 give the following necessary-and-sufficient union:

1. $(p,q)$ with nonzero integer $p,q$ and $a=pq-p-q$; least period
   one or two as specified in (3).
2. $(-1,b,-1,1-a-b)$, where $b$ and $1-a-b$ are nonzero; it is a
   genuine four-cycle exactly when $b\ne1-a-b$.
3. $W(r,s)$ from (4), with least periods two, three or six as stated.
4. The unique five-cycle (7), at $a=13$.

The overlaps of items 1–3 at their lower periods are intentional and
fully labeled; they are not distinct admissions or duplicate counts.
To obtain a disjoint description, retain item 1 for periods one/two,
retain only genuine four-cycles in item 2, and retain only periods
three/six in item 3. All formulas allow every integer parameter for
which their explicit equations and domain exclusions hold.

## 6. No genuine eight-cycle outside $a=1$

Assume a periodic ordinary integral word has period eight and $a\ne1$.
If it meets $-1$, (12) already makes its least period at most four.
Otherwise let $u=\kappa_0\ne0$ and put $e_j=x_{2j}$. Two direct
substitutions in (1), followed by (2), give
$$e_j e_{j+2}=u+1+\frac{u(a-1)}{e_{j+1}+1}.\tag{18}$$
All denominators in this formula are nonzero by the present stratum.
For completeness, the numerator before this division is
$$aX+XZ+a+Y+Z$$
when $(X,Y,Z)=(x_i,x_{i+1},x_{i+2})$. Using
$(X+1)(Z+1)=uY$ reduces the numerator to
$(u+1)Y+(a-1)(X+1)$, which gives (18).

Write the four-periodic even list as $(p,q,r,s)$. Its equations at
positions zero and two have the same left side $pr$. Because
$u(a-1)\ne0$, subtracting them gives
$$\frac1{q+1}=\frac1{s+1},\qquad q=s.$$
The equations at positions one and three give $p=r$. The odd
coordinates, equal to $(e_j+1)(e_{j+1}+1)/u$, are then constant.
Thus the scalar period divides four. Section 3 now makes it divide
two because the word avoids $-1$. In particular no such word has
least period eight. $\square$

## 7. Exact unclosed lemma and the full-contract boundary

The frozen closing lemma is:

> **E.** For every integer $a\ne1$, every ordinary periodic sequence
> of nonzero integers satisfying (1) has least period at most six.

If E were proved, the union in Section 5 together with the extra
$a=1$ eight-cycles in Section 4 would be an explicit complete answer
to the original LY4 question. Conversely, that proposed complete union
would imply E. Thus the remaining obstruction has not been obscured
by a weaker substitute theorem.

The present arguments prove E on the $-1$ locus, on all periods at
most six, and rule out the candidate period eight. They do **not**
rule out ordinary integral cycles of least period seven, nine, ten,
or higher. The exact remaining implication would be
$$\begin{gathered}
A_{i+2}=A_i\in\mathbb Z\setminus\{0\},\quad
z_i\in\mathbb Z\setminus\{0,-1\},\quad
z_i z_{i+2}=A_i(z_{i+1}+1),\quad (z_i)\text{ periodic},\\
a=x_i x_{i+3}-x_{i+1}-x_{i+2}\ne1,
\quad x_i=-z_i-1
\quad\Longrightarrow\quad\operatorname{per}(z)\le6.
\end{gathered}\tag{19}$$
The value of $a$ is an invariant integer for such an ordinary cyclic
word. Integrality of the coefficients and the period-six sign law do
not prove the implication. The recurrence (18) also yields divisibility
by $u(a-1)$, but it leaves unbounded coefficient pairs; it is not a
uniform exhaustion.

An external rational-torsion bound on smooth invariant curves would
still need its singular/reducible strata justified and its remaining
integral torsion channels explicitly solved. A bounded list of possible
rational periods is not a proof of (19), and a parameter-dependent
height search is not the frozen classification contract. No such
substitution is made here.

## Execution receipt and open risks

No mathematical program was written, imported or executed in this lane.
Both finite tables in Section 4 are hand proofs after an analytic
bound, with every divisor case displayed. The old height-eight census
and IR1 were not rerun, enlarged or used as proof dependencies.

The owned files were created with `apply_patch`. Source/contract reads,
file-status reads and later integrity checks are not mathematical
executions. The coordinator owns the separate primary-source audit;
this proof author does not claim to have independently opened its web
sources. The classical recurrence, two-integrals, QRT mechanism and
order-eight phenomenon are deducted from any proposed increment.

The full claim is still unclosed. The new elementary strata have not
yet received a non-author proof review in this file. No priority,
paper-level novelty, fourth admission, C-number, manuscript, formal
evaluation, target Euler factor, root number, automorphy, zero matching
or Hilbert–Pólya realization follows. `NO_BAD_EULER_OR_ROOT_NUMBER`
remains in force.
