# C6 proof dossier: cross-colon dynamics on rectangular monomial ideals

Audit date: 2026-08-30 UTC. This is an internal proof spike, not a paper,
priority certificate, or authorization for external circulation.

## Claim

Let $k$ be any field, let $a,b\geq 1$, and put

$$
R_{a,b}=k[x,y]/(x^a,y^b).
$$

On the finite set $\mathcal M_{a,b}$ of monomial ideals of $R_{a,b}$,
consider

$$
T(I)=x(I:y)+y(I:x). \tag{1}
$$

Write $m=\min(a,b)$. Then:

1. $T$ has exactly $m$ fixed ideals.
2. It has exactly $m-1$ two-cycles, hence $2(m-1)$ states of exact
   period two.
3. It has no cycles of any other length and therefore

   $$
   \#\operatorname{Rec}(T)=3m-2. \tag{2}
   $$

4. If the depth of a state is its first entrance time into the recurrent
   set, the sharp maximum is

   $$
   D(a,b)=
   \begin{cases}
   m,&a\ne b,\\
   \max(1,m-2),&a=b=m.
   \end{cases} \tag{3}
   $$

The scout stated the result for $a,b\geq2$. The proof below establishes the
slightly stronger $a,b\geq1$ version without changing the claimed formulas.

## Status

**PROVABLE AS STATED.** The all-parameter proof closes, including the square
$m-2$ exception.  The post-repair mathematical recommendation is
**GO_INTERNAL / HOLD_EXTERNAL**.  Theorem 2 below adds an exact basin
partition and a four-state all-parameter counting transfer.  The remaining
risk is external ownership: all generic disjunctive-path mechanics receive
zero credit, and the literal colon operator still requires specialist
clearance before circulation.

## Assumptions and scope

- The state space consists of **monomial ideals only**, not all ideals of
  $R_{a,b}$.
- The update is synchronous: both colons are taken from the same input $I$.
- The variables in (1) mean multiplication by the residue classes of $x$ and
  $y$ in $R_{a,b}$.
- No hypothesis on the characteristic or cardinality of $k$ is used.
- Standard facts about monomial ideals, colon ideals, order filters in a
  rectangle, and Boolean/disjunctive networks receive no novelty credit.

## Notation

The residue classes

$$
\{x^iy^j:0\leq i<a,\ 0\leq j<b\}
$$

form a $k$-basis of $R_{a,b}$. We identify a monomial ideal with its occupied
set in the exponent rectangle

$$
P_{a,b}=\{(i,j):0\leq i<a,\ 0\leq j<b\}.
$$

This occupied set is an upper set in the coordinatewise order. Its staircase
is the nonincreasing tuple

$$
h(I)=(h_0,\ldots,h_{a-1}),\qquad
b\geq h_0\geq\cdots\geq h_{a-1}\geq0, \tag{4}
$$

where $x^iy^j\in I$ exactly when $j\geq h_i$.

For a total degree $d$, let

$$
L_d=\max(0,d-b+1),\qquad U_d=\min(a-1,d),
$$

and let $w^{(d)}(I)$ be the binary word indexed by
$i=L_d,\ldots,U_d$ whose $i$th bit records whether
$x^iy^{d-i}\in I$.

Finally, put $\mathfrak m=(x,y)$. For $1\leq r<m$ and
$\epsilon\in\{0,1\}$, define the checker-boundary ideal

$$
C_r^\epsilon=
\left\langle
x^iy^j: i+j>r\ \text{or}\
(i+j=r\ \text{and}\ i\equiv\epsilon\pmod2)
\right\rangle. \tag{5}
$$

The displayed set is upward closed because every monomial of degree greater
than $r$ is included explicitly.  (The shadow of a checker boundary contains
adjacent occupied positions, but for one endpoint phase it need not cover the
whole degree-$(r+1)$ diagonal; only the adjacent-pair fact is used below.)

## Proof strategy and dependency map

The proof uses no classification theorem from commutative algebra.

1. Literal monomial arithmetic gives the staircase update (7).
2. Regrouping cells by total degree conjugates $T$ to independent path
   networks with the rule “new bit = OR of the two neighboring old bits,”
   with zero, one, or two constant boundary sources.
3. A path lemma classifies all recurrent words and gives sharp path depths.
4. Upper-set compatibility between consecutive diagonals reduces all
   recurrent ideals to $\mathfrak m^r$ and $C_r^\epsilon$.
5. The depth of an ideal is the maximum of its diagonal depths. The middle
   one-source band exists exactly when $a\ne b$; its disappearance on a
   square is the full reason for the $m-2$ exception.
6. The first occupied diagonal and its parity support determine the complete
   attractor basin.
7. Staircase boundary paths and a four-state contact automaton count each
   fixed and checker-cycle basin uniformly in $a,b$.
8. Reflection gives the terminal-basin ballot formula and checks the basin
   partition.

## Proof

### Step 1. Literal colon and multiplication formulas

Fix a staircase $h=h(I)$. Multiplication by $y$ sends the basis monomial
$x^iy^j$ to $x^iy^{j+1}$ if $j<b-1$ and to zero if $j=b-1$. Therefore
$x^iy^j\in(I:y)$ exactly when either $j=b-1$ or $j+1\geq h_i$. The threshold
of $(I:y)$ in row $i$ is consequently

$$
c_i=\max(h_i-1,0). \tag{6}
$$

Multiplication by $x$ shifts this row to row $i+1$. Hence the thresholds of
$x(I:y)$ are $b,c_0,c_1,\ldots,c_{a-2}$.

For the other term, $x^iy^j\in(I:x)$ when $i=a-1$ or
$j\geq h_{i+1}$. Its thresholds are
$h_1,\ldots,h_{a-1},0$. Multiplication by $y$ adds one to each threshold,
with clipping at $b$, so the thresholds of $y(I:x)$ are
$\min(b,h_1+1),\ldots,\min(b,h_{a-1}+1),1$.

The sum of two monomial ideals is the union of their occupied upper sets and
therefore takes the coordinatewise minimum of thresholds. For $a\geq2$ this
gives the exact staircase update $h'=F_{a,b}(h)$:

$$
\begin{aligned}
h'_0&=\min(b,h_1+1),\\
h'_i&=\min\bigl(\max(0,h_{i-1}-1),\ h_{i+1}+1\bigr)
       &&(1\leq i\leq a-2),\\
h'_{a-1}&=\min\bigl(\max(0,h_{a-2}-1),1\bigr).
\end{aligned} \tag{7}
$$

When $a=1$, the class of $x$ is zero, so $(I:x)=R_{1,b}$ and
$T(I)=(y)$ for every $I$; in staircase form, $F_{1,b}(h)=(1)$. This also
covers $a=b=1$, where $(y)$ is the zero ideal.

The derivation proves both that (7) agrees with (1) and that its output is a
nonincreasing staircase. No cancellation issue is hidden here: multiplication
by either variable sends distinct nonannihilated basis monomials to distinct
basis monomials, so each colon condition is checked coefficient by
coefficient.

### Step 2. Diagonal path decomposition

Membership in $T(I)$ can be tested before taking thresholds. For a basis
cell $(i,j)$,

$$
\begin{split}
x^iy^j\in T(I)\quad\Longleftrightarrow\quad
&\bigl[i\geq1\ \text{and}\
  (j=b-1\ \text{or}\ x^{i-1}y^{j+1}\in I)\bigr]\\
&\ \ \text{or}\
\bigl[j\geq1\ \text{and}\
  (i=a-1\ \text{or}\ x^{i+1}y^{j-1}\in I)\bigr].
\end{split} \tag{8}
$$

Both predecessor monomials in (8) have total degree $i+j$. Thus distinct
total-degree diagonals do not interact.

Let $n_d=U_d-L_d+1$. In the word $w^{(d)}$, number positions from left to
right. Equation (8) becomes

$$
(G_{n_d}^{\lambda_d,\rho_d}w)_s
=w_{s-1}\vee w_{s+1}, \tag{9}
$$

where a missing left neighbor is the constant
$\lambda_d=\mathbf1_{d\geq b}$ and a missing right neighbor is
$\rho_d=\mathbf1_{d\geq a}$. The symbol $\vee$ is Boolean OR.

If $M=\max(a,b)$, the diagonal types are therefore

| degree range | length | boundary sources |
|---|---:|---:|
| $0\leq d<m$ | $d+1$ | $00$ |
| $m\leq d<M$ | $m$ | exactly one source |
| $M\leq d\leq a+b-2$ | $a+b-1-d$ | $11$ |

The middle range is empty precisely when $a=b$.

### Step 3. Path lemma

For a binary word of length $n$, let $G_n^{\lambda,\rho}$ be (9).

**Lemma 1 (path recurrence and sharp depth).**

1. For $(\lambda,\rho)=(0,0)$ and $n=1$, the only recurrent word is $0$,
   and the maximum depth is $1$.
2. For $(\lambda,\rho)=(0,0)$ and $n\geq2$, the recurrent words are exactly
   the four words that are constant on each parity class of positions. The
   all-zero and all-one words are fixed, and the two checkerboards form a
   two-cycle. The maximum depth is $n-2$.
3. With exactly one source, the unique recurrent word is $1^n$, it is fixed,
   and the maximum depth is $n$.
4. With two sources, the unique recurrent word is $1^n$, it is fixed, and
   the maximum depth is $\lceil n/2\rceil$.

**Proof.** First take no sources. Let $A$ be the adjacency matrix of the
path $P_n$, with arithmetic in the Boolean semiring. Then
$G_n^{0,0}(w)=Aw$, and the $i$th bit of $A^tw$ is one exactly when some
initial one is joined to $i$ by a walk of length $t$.

Assume $n\geq2$ and $t\geq n-2$. Every length-$t$ walk can be extended by
traversing an edge and immediately returning, so every endpoint reachable
in $t$ steps is reachable in $t+2$ steps. Conversely, if two vertices are
joined by a walk of length $t+2$, their distance has the parity of $t$ and
is at most $n-1$. It cannot equal $t+2$, since $t+2\geq n$; hence it is at
most $t$. A shortest path followed by backtracks gives a walk of length
$t$. Thus

$$
A^{t+2}=A^t\qquad(t\geq n-2). \tag{10}
$$

This proves the upper bound $n-2$. Moreover,

$$
(A^2w)_i=w_i\vee w_{i-2}\vee w_{i+2}, \tag{11}
$$

with nonexistent terms omitted. The equality $A^2w=w$ holds exactly when
all bits in each parity class agree. These four words have the stated fixed
or two-cycle behavior. Starting from the word with a single one at the left
endpoint, at time $t<n-2$ the occupied parity class has reached only through
position $t$ and has not reached position $t+2$. Equation (11) then shows
that the word is not recurrent. At time $n-2$, (10) shows that it is
recurrent. This proves sharpness. For $n=1$, the map sends both words to
zero, proving the exceptional first assertion.

Now add boundary sources. With a left source, unrolling the recurrence shows
that the state at time $t$ contains the Boolean sum

$$
e_0\vee Ae_0\vee\cdots\vee A^{t-1}e_0, \tag{12}
$$

where $e_0$ is the left endpoint. Hence position $i$ is one by time $i+1$.
Every state is $1^n$ by time $n$. A periodic state must remain periodic under
all future iterates, while its future is $1^n$; therefore $1^n$ is the only
recurrent state. From the zero word, the right endpoint stays zero through
time $n-1$, since its distance from the source is $n-1$. The depth is
exactly $n$. A right source gives the reflected argument.

With both sources, position $i$ is reached after
$\min(i,n-1-i)+1$ updates. All positions are therefore one after

$$
1+\max_i\min(i,n-1-i)=\lceil n/2\rceil \tag{13}
$$

updates. The zero word attains this time at a middle position. The same
future-periodicity argument makes $1^n$ the unique recurrent word. This
proves all four assertions. $\square$

The lemma is a path-specialized instance of disjunctive Boolean-network
dynamics. It is included to make the transient constants and boundary-source
convention self-contained, not as a claim of ownership of OR-network theory.

### Step 4. Classification of every recurrent ideal

Because the diagonal projections commute with $T$, an ideal is recurrent
only if every diagonal word is recurrent under its corresponding path map.
The converse also holds: if every diagonal word is recurrent, all component
periods divide two, so the ideal itself has period dividing two.

For $d\geq m$, at least one boundary source is present. Lemma 1 forces every
such recurrent diagonal to be all one. For $d<m$, a recurrent diagonal is
zero, all one, or, when its length is at least two, one of the two
checkerboards. Degree zero has length one and must be zero. If $a=b=1$,
degree zero is the only diagonal, so the zero ideal is the unique recurrent
state; it is $\mathfrak m^1$. We now assume $a+b>2$.

Upper-set compatibility restricts the possible sequence of these types. An
occupied position on degree $d$ forces its two available upward successors
on degree $d+1$. Consequently:

- the upward shadow of an all-one diagonal is all one;
- the upward shadow of a checkerboard contains two adjacent occupied
  positions;
- among the recurrent no-source words, only the all-one word can contain two
  adjacent ones.

It follows that there is a first nonzero recurrent diagonal $r$, every lower
diagonal is zero, and every diagonal above $r$ is all one. Since all
diagonals from $m$ onward are one, $1\leq r\leq m$. At degree $r$ there are
two possibilities:

- it is all one, yielding exactly $\mathfrak m^r$;
- it is a checkerboard, which requires $r<m$ and yields exactly one of
  $C_r^0,C_r^1$.

This proves the exhaustive recurrent-set identity

$$
\operatorname{Rec}(T)
=\{\mathfrak m^r:1\leq r\leq m\}
\ \dot\cup\
\{C_r^0,C_r^1:1\leq r<m\}. \tag{14}
$$

Every zero or all-one path word is fixed, so each $\mathfrak m^r$ is fixed.
The no-source path map swaps its two checkerboards, so

$$
T(C_r^0)=C_r^1,\qquad T(C_r^1)=C_r^0. \tag{15}
$$

Equation (14) now gives $m$ fixed ideals, $m-1$ two-cycles,
$3m-2$ recurrent states, and no other periods.

For reference, the staircases of the recurrent families are

$$
h_i(\mathfrak m^r)=\max(r-i,0), \tag{16}
$$

and, after choosing the two phases suitably,

$$
\begin{aligned}
h_i(C_r^0)&=\max\bigl(r-2\lfloor i/2\rfloor,0\bigr),\\
h_i(C_r^1)&=\max\bigl(r+1-2\lceil i/2\rceil,0\bigr).
\end{aligned} \tag{17}
$$

These formulas also give a direct substitution check of (15) in (7).

### Step 5. Exact maximum transient depth

Let $\delta_d(I)$ be the preperiod of $w^{(d)}(I)$ under its path map. Since
the update is the direct product of the diagonal updates and every component
cycle has period at most two,

$$
\operatorname{depth}(I)=\max_d\delta_d(I). \tag{18}
$$

Indeed, at the right-hand time every component is recurrent, so the product
is recurrent. Before that time at least one projection is nonrecurrent, which
prevents the product state from being recurrent.

Suppose first that $a\ne b$. The one-source band
$m\leq d<M$ is nonempty, and every word there has length $m$. Lemma 1 gives
the universal upper bound $m$. The no-source band contributes at most
$\max(1,m-2)$, and the two-source band has lengths at most $m-1$ and
contributes at most $\lceil(m-1)/2\rceil$. Hence no ideal has depth above
$m$. The zero ideal has the zero word on a one-source diagonal of length
$m$, whose depth is $m$ by Lemma 1. Therefore

$$
D(a,b)=m\qquad(a\ne b). \tag{19}
$$

Now let $a=b=m$. There is no one-source band. In the no-source band, degree
zero contributes at most one; degrees $1,\ldots,m-1$ have lengths
$2,\ldots,m$ and contribute at most $0,1,\ldots,m-2$. The two-source band
has maximum length $m-1$ and contributes at most
$\lceil(m-1)/2\rceil$. For all $m\geq1$,

$$
\left\lceil\frac{m-1}{2}\right\rceil
\leq \max(1,m-2). \tag{20}
$$

Equations (18)--(20) give the square upper bound
$\max(1,m-2)$. It is sharp in each boundary case:

- for $m=1$, the unit ideal has depth one;
- for $m=2$, the zero ideal has depth one;
- for $m\geq3$, the principal ideal $(y^{m-1})$ has on degree $m-1$ a
  no-source word of length $m$ with a single occupied left endpoint. Lemma 1
  gives this word depth $m-2$.

Thus

$$
D(m,m)=\max(1,m-2). \tag{21}
$$

This proves (3) and completes the theorem. $\square$

## Why the square loses two steps

The exceptional depth is structural rather than a cancellation in (7):

$$
\begin{array}{c|c|c}
&a\ne b&a=b=m\\ \hline
\text{longest one-source path}&m&\text{absent}\\
\text{longest no-source depth}&m-2&m-2\\
\text{longest two-source depth}&\lceil(m-1)/2\rceil&
\lceil(m-1)/2\rceil
\end{array}
$$

The unequal rectangle has a flat middle band of total-degree diagonals. One
edge of each such diagonal lies on a truncation wall and injects a one at
every update, while the opposite edge does not. Filling a length-$m$ path
from one side takes $m$ steps. On a square, both walls begin on the same
degree, so that middle band disappears. The slowest surviving mechanism is
free parity propagation on the length-$m$ diagonal, taking $m-2$ steps
(apart from $m=1,2$).

## Value repair: exact basins from the first occupied diagonal

The hostile gate required an all-parameter output that is not obtained by
merely inserting known path heights into the diagonal table.  The following
basin theorem supplies that increment.  It uses the compatibility between a
rectangle upper set and all of its diagonal traces; its counting recurrence
has four contact states and never iterates over the set of monomial ideals.

For a periodic orbit $\mathcal O$, write

$$
\mathcal B(\mathcal O)=
\{I:T^t(I)\in\mathcal O\text{ for some }t\geq0\}.
$$

For a nonzero ideal $I$, define its first occupied degree and its trace there
by

$$
\nu(I)=\min\{i+j:x^iy^j\in I\},\qquad
S_r(I)=\{i:x^iy^{r-i}\in I\}. \tag{22}
$$

Put $\nu(0)=\infty$.  When $r<m$, every point on degree $r$ lies inside the
rectangle, so $S_r(I)\subseteq\{0,1,\ldots,r\}$.

### Theorem 2 (basin partition and four-state transfer)

Let $N=a+b$ and $m=\min(a,b)$.

1. If $m=1$, every monomial ideal belongs to
   $\mathcal B(\{\mathfrak m\})$.

2. Suppose $m\geq2$.  The basin of $\mathfrak m$ consists of the unit ideal
   and the ideals with $\nu(I)=1$ whose trace meets both parities.  For
   $2\leq r<m$,

   $$
   I\in\mathcal B(\{\mathfrak m^r\})
   \quad\Longleftrightarrow\quad
   \nu(I)=r\ \text{ and }S_r(I)\text{ meets both parities}. \tag{23}
   $$

   The last fixed basin is

   $$
   \mathcal B(\{\mathfrak m^m\})
   =\{I:\nu(I)\geq m\}, \tag{24}
   $$

   where $\nu(0)=\infty$ is included.

3. For $1\leq r<m$, the basin of the checker two-cycle is

   $$
   \mathcal B(\{C_r^0,C_r^1\})
   =\{I:\nu(I)=r,\ S_r(I)\ne\varnothing,
     \ S_r(I)\text{ lies in one parity class}\}. \tag{25}
   $$

   More precisely, if every index in $S_r(I)$ has parity $\epsilon$, then
   for all sufficiently large $t$,

   $$
   T^t(I)=C_r^{\epsilon+t\bmod2}. \tag{26}
   $$

4. The basin sizes have the following exact all-parameter transfer.  For
   each $1\leq r<m$, consider monotone paths from $(0,b)$ to $(a,0)$ with
   east and south steps, constrained by $i+j\geq r$.  Record which parities
   of $i$ occur among contacts $(i,j)$ with $i+j=r$.  For
   $Q\subseteq\{E,O\}$, let $F^{(r)}_{i,j}(Q)$ count prefixes ending at
   $(i,j)$ with contact-parity set $Q$.

   Initialize

   $$
   F^{(r)}_{0,b}(\varnothing)=1 \tag{27}
   $$

   and set every out-of-range or below-barrier entry to zero.  At an allowed
   vertex $(i,j)\ne(0,b)$, first form

   $$
   A_{i,j}(Q)=F^{(r)}_{i-1,j}(Q)+F^{(r)}_{i,j+1}(Q). \tag{28}
   $$

   If $i+j>r$, put $F^{(r)}_{i,j}(Q)=A_{i,j}(Q)$.  If $i+j=r$, put

   $$
   F^{(r)}_{i,j}(Q)=
   \sum_{Q':\,Q'\cup\{i\bmod2\}=Q}A_{i,j}(Q'), \tag{29}
   $$

   where parity zero is denoted by $E$ and parity one by $O$.  Define

   $$
   A_r^E=F^{(r)}_{a,0}(\{E\}),\quad
   A_r^O=F^{(r)}_{a,0}(\{O\}),\quad
   A_r^M=F^{(r)}_{a,0}(\{E,O\}). \tag{30}
   $$

   Then, for $m\geq2$,

   $$
   \begin{aligned}
   |\mathcal B(\{\mathfrak m\})|&=1+A_1^M=2,\\
   |\mathcal B(\{\mathfrak m^r\})|&=A_r^M
      &&(2\leq r<m),\\
   |\mathcal B(\{C_r^0,C_r^1\})|&=A_r^E+A_r^O
      &&(1\leq r<m),\\
   |\mathcal B(\{\mathfrak m^m\})|
      &=\binom{N}{a}-\binom{N}{m-1}. \tag{31}
   \end{aligned}
   $$

   For $m=1$, the sole basin has size $\binom{N}{a}$.  The transfer also
   satisfies

   $$
   A_r^E+A_r^O+A_r^M
   =\binom{N}{r}-\binom{N}{r-1}, \tag{32}
   $$

   and the basin sizes in (31) sum to $\binom{N}{a}$.

### Proof of Theorem 2

**Step 1: the first trace determines the attractor.**  Every diagonal below
$\nu(I)$ is zero and remains zero, since it is a no-source path.  Suppose
$1\leq r=\nu(I)<m$.  The degree-$r$ diagonal is a no-source path of length
$r+1$.  The walk formula for its iterates has the following consequence.
If the initial support lies in parity $\epsilon$, then for all sufficiently
large $t$ it is the full parity class $\epsilon+t$; if the initial support
meets both parities, then for all sufficiently large $t$ it is the all-one
word.  Indeed, a sufficiently long walk of the required parity joins any
initial occupied vertex to every target vertex in that parity class.

The recurrent-ideal compatibility proved in Step 4 above now forces every
higher diagonal to be all one.  A one-parity first trace therefore gives
$C_r^0,C_r^1$ with the phase in (26), while a mixed first trace gives the
fixed ideal $\mathfrak m^r$.  This proves (23), (25), and (26).

If $\nu(I)\geq m$, all no-source diagonals are zero.  Every sourced diagonal
eventually fills, so the attractor is $\mathfrak m^m$, proving (24).  If
$\nu(I)=0$, then $I=R_{a,b}$ and
$T(R_{a,b})=(x)+(y)=\mathfrak m$.  These cases give the assertion about
$\mathfrak m$.  When $m=1$ there is no intermediate degree
$1\leq r<m$; the preceding two cases exhaust all ideals and give the unique
fixed basin.

**Step 2: staircase paths encode the coupled upper-set count.**  Let
$h=(h_0,\ldots,h_{a-1})$ be the staircase of $I$.  Encode it by the unique
path which starts at $(0,b)$, descends to $(0,h_0)$, takes an east step,
descends to $(1,h_1)$, takes an east step, and so on, finally descending at
$x=a$ to $(a,0)$.  This is a bijection between monomial ideals and the
$\binom{N}{a}$ east/south paths in the rectangle.

For $r<m$, the condition $\nu(I)\geq r$ is

$$
h_i\geq r-i\qquad(0\leq i\leq r), \tag{33}
$$

which is equivalent to the boundary path staying in $i+j\geq r$.  Moreover,
the path contacts $(i,r-i)$ exactly when $h_i=r-i$, equivalently exactly
when $x^iy^{r-i}\in I$.  Thus its contact-parity set is precisely the set of
parities met by $S_r(I)$.

Equations (27)--(29) are now the ordinary last-step recursion for these
paths.  The union with the new contact parity in (29) is the only state
update, so the four states $\varnothing,\{E\},\{O\},\{E,O\}$ count every
path once.  In particular, (30) counts respectively the even-only,
odd-only, and mixed first traces.  Combining this fact with Step 1 gives the
first three lines of (31).  For $r=1$, the only mixed trace is
$S_1=\{0,1\}$, whose upper closure is $\mathfrak m$, so $A_1^M=1$; adding
the unit ideal gives two.

**Step 3: reflection and the last fixed basin.**  The number of paths from
$(0,b)$ to $(a,0)$ that stay in $i+j\geq r$ is

$$
B_{\geq r}=\binom{N}{a}-\binom{N}{r-1}. \tag{34}
$$

To see this without an unstated ballot convention, write
$z=i+j-r$.  An east step raises $z$ by one and a south step lowers it by one;
the walk starts at $p=b-r\geq0$ and ends at $q=a-r\geq0$.  For a bad walk,
swap east and south steps through its first visit to $-1$.  This reflection
is a bijection from bad walks starting at $p$ to unrestricted walks starting
at $-p-2$ and ending at $q$.  Such a reflected walk has
$N-r+1$ up-steps, equivalently $r-1$ down-steps, and hence there are
$\binom{N}{r-1}$ of them.  The assumptions $r\leq m$ put both original
endpoints on or above the barrier, so the argument also applies at $r=m$.

At $r=m$, (33) is exactly $\nu(I)\geq m$, and (34) proves the last line of
(31).  For $r<m$, paths with first degree exactly $r$ are those which stay
above barrier $r$ but not barrier $r+1$.  Hence their number is

$$
B_{\geq r}-B_{\geq r+1}
=\binom{N}{r}-\binom{N}{r-1}. \tag{35}
$$

The three nonempty contact masks partition these paths, proving (32).
Together with the unit ideal and the terminal class $\nu(I)\geq m$, these
first-degree classes partition all monomial ideals.  This proves the final
sum assertion and completes the theorem. $\square$

### Why this is not an ideal-by-ideal enumeration

For a fixed $r$, (27)--(29) uses exactly $4(a+1)(b+1)$ integer entries and
local additions.  Running it for $1\leq r<m$ takes
$O(abm)$ arithmetic operations and $O(ab)$ reusable storage, while the state
space has size $\binom{a+b}{a}$.  The recurrence counts rectangle boundary
paths by a finite contact automaton; it does not define a basin by iterating
all ideals.  The ballot formulas (32)--(35) provide independent global
checks on the transfer.

## Independent exact verification

The independent verifier is
[`verify_alg_cross_colon.py`](verify_alg_cross_colon.py), with canonical
stdout in
[`ALG_CROSS_COLON_CANONICAL.txt`](ALG_CROSS_COLON_CANONICAL.txt). It imports
nothing from the scout and performs three mutually compared implementations:

1. literal basis-monomial multiplication and colon arithmetic;
2. the staircase formula (7);
3. the diagonal path rule (9).

It exhausts every monomial ideal in all $81$ boxes $1\leq a,b\leq9$, tests
the exact families (14)--(17), all cycles and depths, and the sharp witnesses.
It separately exhausts all binary words through path length $14$ for source
types $00,10,01,11$.

Fresh canonical run:

```text
cross-colon monomial-ideal dynamics independent control: PASS
assertions=1469669
path_words=131064; path_lengths=1..14; source_types=00,10,01,11
rectangles=81; parameter_grid=a,b=1..9; ideals=184736
literal_vs_staircase_vs_diagonal=PASS
fixed_two_cycle_recurrent_classification=PASS
sharp_depth_and_witnesses=PASS
global_depth_hist={0: 693, 1: 8656, 2: 27401, 3: 36536, 4: 39774, 5: 28400, 6: 25472, 7: 13192, 8: 4612}
```

These $1,469,669$ assertions are finite falsification controls, not a proof
of the quantified theorem.

The basin theorem has a separate verifier,
[verify_alg_cross_colon_basins.py](verify_alg_cross_colon_basins.py), and
canonical output
[ALG_CROSS_COLON_BASINS_CANONICAL.txt](ALG_CROSS_COLON_BASINS_CANONICAL.txt).
It does not import the first verifier.  It constructs the operator from
literal colon and multiplication arithmetic, follows every ideal in all
$64$ boxes $1\leq a,b\leq8$, and compares the resulting attractor with the
first-trace characterization.  Independently, it evaluates the four-state
path transfer, compares every basin count with the exhaustive dynamics, and
checks the ballot, partition, and transpose-symmetry identities through
$1\leq a,b\leq30$.

Fresh canonical run:

    cross-colon basin transfer independent control: PASS
    assertions=265987
    literal_rectangles=64; parameter_grid=a,b=1..8; ideals=48602
    literal_attractors_vs_first_trace=PASS
    contact_transfer_vs_exhaustive_basins=PASS
    ballot_partition_and_swap_identities=PASS
    large_transfer_grid=a,b=1..30; nontrivial_triples=8555
    example_a5_b7_orbit_basins=[(('C', 1), 10), (('C', 2), 45), (('C', 3), 116), (('C', 4), 185), (('P', 1), 2), (('P', 2), 9), (('P', 3), 38), (('P', 4), 90), (('P', 5), 297)]
    example_a5_b7_trace_phases=[(1, (4, 6, 1)), (2, (30, 15, 9)), (3, (44, 72, 38)), (4, (139, 46, 90))]

These $265,987$ assertions are an independent finite control for Theorem 2,
not its proof.

## Owner and collision audit

### Direct-map search

Searches run on 2026-08-30 included the exact strings
`"x(I:y)+y(I:x)"`, `"x (I : y)" "y (I : x)"`, `cross-colon ideal
operator`, and combinations of `monomial ideal`, `staircase`, `colon`,
`dynamics`, and `truncated polynomial ring`. No direct occurrence of (1),
its diagonal conjugacy, or the conjunction (2)--(3) was located. This is
only **BOUNDED_NO_DIRECT_HIT**, not a novelty certificate.

The post-repair search additionally combined the literal operator with
`basin`, `attractor`, `monomial ideal`, and `truncated polynomial ring`.  It
did not locate the first-trace basin partition or the contact-parity
transfer.  Generic algebraic methods for Boolean-network basins, such as
[Monomials and Basin Cylinders for Network Dynamics](https://doi.org/10.1137/140975929),
own the general basin concept and computational context, not Theorem 2.

Colon ideals and their monomial structure are established commutative
algebra. For example, Balu and Sengupta study explicit colon representations
for associated primes of monomial ideals
([arXiv:2105.00835](https://arxiv.org/abs/2105.00835)). Their target is
static colon structure, not iteration of (1); nevertheless the colon and
monomial-staircase ingredients here receive zero credit.

### Disjunctive Boolean-network owner pressure

The proof exposes a closer mechanism owner than the scout listed. Jarrah,
Laubenbacher, and Veliz-Cuba study conjunctive and disjunctive Boolean
networks through their dependency graphs and determine long-term cycle
structure
([DOI 10.1007/s11538-010-9501-z](https://doi.org/10.1007/s11538-010-9501-z)).
Gadouleau's invited survey explicitly treats graph, Boolean-matrix, periodic,
image, and fixed-point descriptions of disjunctive networks
([DOI 10.4230/OASIcs.AUTOMATA.2021.1](https://doi.org/10.4230/OASIcs.AUTOMATA.2021.1)).

After (9), the path recurrence and the fact that periods divide two belong to
this established mechanism. A future manuscript must assign the following
items zero novelty credit:

- Boolean-semiring adjacency powers and walk reachability;
- the general relation between graph cyclicity and periods of a disjunctive
  network;
- generic fixed/periodic-point theory for OR networks.

The defensible residual, pending specialist clearance, is narrower: the exact
algebraic-to-diagonal conjugacy for (1), compatibility of path-periodic words
with monomial upper sets, the resulting $3m-2$ census, and the sharp
rectangle-versus-square depth law with explicit witnesses.

### Rowmotion and toggle collision

Monomial ideals in $R_{a,b}$ are upper sets in a product of two chains, so
rowmotion is an unavoidable visual and state-space neighbor. Striker and
Williams study promotion and rowmotion as actions on order ideals and give
equivariant bijections between them
([arXiv:1108.1172](https://arxiv.org/abs/1108.1172)). Einstein and Propp treat
rowmotion/promotion on products of two chains, including order-$a+b$
behavior and file-based descriptions
([arXiv:1310.5294](https://arxiv.org/abs/1310.5294)).

There is no whole-state conjugacy to rowmotion or to a composition of
ordinary toggles:

1. Every toggle is an involution, hence any composition of toggles is a
   bijection. Rowmotion is a permutation of the finite order-ideal set.
2. The map (1) has transient states for every $a,b\geq1$, because (3) is at
   least one. It is therefore not bijective.
3. Rectangle rowmotion has global order tied to $a+b$, whereas every
   recurrent orbit of (1) has length at most two.
4. Formula (9) updates all positions synchronously by neighbor OR. It is not
   a sequential product of membership-flipping involutions.

This defeats literal or conjugacy ownership by classical rowmotion. It does
not permit broad language such as “a new rectangle-lattice action,” “a new
file action,” or “unrelated to toggles”: the state space and diagonal/file
visualization remain adjacent, and the manuscript must give the explicit
bijection-versus-transient firewall.

### Internal P107 collision

P107 studies $I\mapsto\operatorname{Ann}(I)^r$ on ideals of $\mathbb Z/N\mathbb Z$.
Its prime-power coordinate is a clipped expanding reflection, and CRT gives
its product census, depth CDF, and zeta function. C6 shares the high-level
grammar “ideal operator, fixed/two-cycles, exact transient depth,” so it
cannot claim a first ideal-lattice dynamical classification.

The mechanisms are nevertheless different at proof level:

| P107 | C6 |
|---|---|
| all ideals of a residue ring | monomial ideals of $k[x,y]/(x^a,y^b)$ |
| annihilator followed by an ideal power | two crossed variable-colon terms followed by a sum |
| independent prime valuations via CRT | independent total-degree diagonals |
| integer clipped reflection with expanding deviation | synchronous disjunctive Boolean paths |
| logarithmic/arithmetic depth thresholds | linear geometric depth and square-band deletion |

The collision is therefore **adjacent but not fatal**. It does reduce value:
P107 already owns the internal narrative template and has the stronger CRT,
CDF, and zeta package.  Theorem 2 repairs the earlier output asymmetry by
adding every attractor basin and a uniform contact transfer.  Its mechanism
is not a renamed CRT coordinate calculation: the count uses the global
upper-set constraint on the diagonal traces.

## Claim ceiling and paper-value verdict

Allowed internal claim ceiling:

> For the specific synchronous map $I\mapsto x(I:y)+y(I:x)$ on monomial
> ideals of $k[x,y]/(x^a,y^b)$, total-degree diagonals give sourced
> disjunctive path networks. Their compatibility with the monomial upper-set
> condition yields the exact recurrent families (14), $m$ fixed ideals,
> $m-1$ two-cycles, and the sharp depth law (3).  The first occupied
> diagonal and its parity trace determine the complete attractor basin, and
> the four-state contact transfer (27)--(31) gives every basin size uniformly
> in $a,b$.

Not allowed without substantially more owner work:

- “first dynamics of colon ideals”;
- “new Boolean path dynamics” or ownership of the period-two mechanism;
- “new rowmotion/toggle action”;
- novelty or priority assertions based on the bounded exact-string miss;
- extension from monomial ideals to all ideals;
- a claim that C6 has no relation to P107 merely because the rings differ.

**Post-repair verdict: GO_INTERNAL / HOLD_EXTERNAL.**  Theorem 2 supplies the
nonmechanical all-parameter value increment required by the first hostile
gate: basin membership uses upper-set compatibility, while basin cardinality
uses a finite contact automaton rather than ideal enumeration.  No novelty
credit is claimed for the OR-path dynamics, lattice-path bijection, or
reflection principle.  External circulation remains blocked until a
specialist search clears the literal colon operator and the basin theorem.

## Open risks

- The direct-owner search is bounded and English-query dependent.
- Disjunctive-network literature may contain the exact sourced-path height
  formulas as immediate named special cases; those formulas must be treated
  as background even if a verbatim match is not found.
- A specialist in monomial operations may recognize (1) as a standard
  closure/interior composition under different notation.
- The even-only and odd-only checker-basin counts are given by a uniform
  four-state recurrence rather than individual scalar closed forms; a direct
  simplification would strengthen, but is not required for, the present
  internal gate.
