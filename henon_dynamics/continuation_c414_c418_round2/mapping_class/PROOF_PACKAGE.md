# Proof Package: all positive two-twist words on the integer trace lattice

## Claim

Let
$$
A(x,y,z)=(x,z,xz-y),\qquad B(x,y,z)=(z,y,yz-x),
\qquad K(x,y,z)=x^2+y^2+z^2-xyz.
$$
A positive two-letter word means a finite chronological string
$w=\ell_1\cdots\ell_s$, with every $\ell_i\in\{A,B\}$ and with both
letters occurring. Its actual map and its ordinary clock are
$$
W=\ell_s\circ\cdots\circ\ell_1,\qquad P,W(P),W^2(P),\ldots.
$$
This chronological convention is used by all scripts here; in particular,
the string $AB$ represents $B\circ A$, not $A\circ B$.

Put $C=\{-1,0,1\}$ and define the following union of 39 distinct affine
lines, with integer parameters:
$$
\begin{aligned}
\mathcal D_0&=\{(t,a,b),(a,t,b),(a,b,t):t\in\mathbb Z,\ a,b\in C\},\\
\mathcal D_x&=\{(c,t,ct+b):t\in\mathbb Z,\ c\in\{-1,1\},\ b\in C\},\\
\mathcal D_y&=\{(t,c,ct+b):t\in\mathbb Z,\ c\in\{-1,1\},\ b\in C\},\\
\mathcal D&=\mathcal D_0\cup\mathcal D_x\cup\mathcal D_y,\\
\mathcal E&=\{(2\epsilon,2\eta,2\epsilon\eta):\epsilon,\eta\in\{-1,1\}\}.
\end{aligned}
$$
For an integer $k$, set $X_k=(\mathcal D\cup\mathcal E)\cap\{K=k\}$.

The claims are:

1. For every positive two-letter word $w$, every integer periodic point
   of $W$ lies in $\mathcal D\cup\mathcal E$. More precisely, every
   intermediate letter phase of a periodic orbit lies there.
2. Conversely, every point of $\mathcal D\cup\mathcal E$ is fixed by
   some positive two-letter word, which may depend on its line. Thus
   $$
   \bigcup_w\operatorname{Fix}(W;\mathbb Z^3)
   =\bigcup_w\operatorname{Per}(W;\mathbb Z^3)
   =\mathcal D\cup\mathcal E.
   $$
   This is an existential union over words, not the set periodic under
   every group element.
3. The finite set $X_k$ has at most 40 points, independently of $k$ and
   of the word. It is empty unless
   $$k\in\{m^2,\ m^2+1,\ m^2-m+2:m\in\mathbb Z\}.$$
   Both $X_k$ and every word's complete periodic structure are obtained
   by the exact quadratic-root/partial-permutation construction below.
   Every ordinary $W$-period is at most 40.
4. For each word, every integer point is either periodic or tends to
   infinity in both ordinary forward and ordinary backward time.

The upper bound 40 is for the universal candidate set. We do not assert
that some one word has 40 periodic points or a 40-cycle, or that this is
the optimal period bound. No claim about rational nonintegral points,
complex periodic schemes, finite-field point counts or multiplicity is
included.

## Status

PROVABLE AS STATED, subject to independent proof review. The proposed
full positive-word family, all integer levels, all integer points and
ordinary word clock have not been narrowed. This is an author proof
package, not an admission decision or an independently reviewed result.

## Assumptions

- The initial coordinates are integers.
- The word is positive in the two displayed maps and contains both.
- Periods refer to iterations of that word's map, not individual
  letter phases, substitution lengths or whole-group orbits.

## Notation

Write $\|P\|=\max(|x|,|y|,|z|)$ for $P=(x,y,z)$, and
$$
\begin{aligned}
\mathcal S&=\{P\in\mathbb Z^3:\min(|x|,|y|,|z|)\le1\},\\
\mathcal C_+&=\{P\in\mathbb Z^3: |x|,|y|\ge2,\
|z|\ge\max(|x|,|y|),\ |z|>2,\ xyz>0\}.
\end{aligned}
$$
The coordinate swap $J(x,y,z)=(y,x,z)$ satisfies $JAJ=B$ and
$JBJ=A$. It preserves $K,\mathcal S,\mathcal C_+$ and exchanges
$\mathcal D_x$ with $\mathcal D_y$. Whenever a statement for the
$y$ coordinate is deduced by $J$, this exact conjugacy is the reason.

## Proof Strategy

Use the integrality gap between absolute values at most one and at
least two. A positive escape cone is invariant under both letters.
Outside it, all-large triples must descend to a small coordinate.
Small-coordinate rotation orders and the next occurrence of the other
letter then force a periodic orbit onto 39 affine lines. The converse
uses positive words that are the identity on small-coordinate planes.
The level equations on those lines are just three quadratic forms.

The escape mechanism and trace-map/matrix structure are classical;
they are re-proved here for a self-contained arithmetic argument and
are fully deducted in [SOURCE_AUDIT.md](SOURCE_AUDIT.md). The proposed
increment is the integer all-word exhaustion and its uniform finite
periodic classifier, not the existence of escape regions.

## Dependency Map

1. Coordinate invertibility and the invariant give a bijective integer
   dynamical system on every level.
2. The cone lemma and all-large descent use positivity of the letters,
   integrality and the occurrence of both letters.
3. The small-coordinate lemma and a predecessor constraint give the
   39-line exhaustion at every periodic letter phase.
4. Finite-order small-coordinate planes give the existential converse.
5. Three exact quadratic level forms give the 40-state bound.
6. Restriction to finite partial permutations gives every word cycle,
   fixed-point count and finite dynamical zeta function.
7. The cone-free forward argument plus a common reverser gives the
   two-sided periodic/escape dichotomy.

## Proof

### Step 1. Inverses, invariant and matrix convention

Direct substitution gives
$$
A^{-1}(x,y,z)=(x,xy-z,y),\qquad
B^{-1}(x,y,z)=(xy-z,y,x),
$$
and
$$
K(A(x,y,z))=x^2+z^2+(xz-y)^2-xz(xz-y)=K(x,y,z).
$$
The equality for $B$ follows by conjugating this identity with $J$.
Thus both maps are bijections of $\mathbb Z^3$ and preserve each level.

For the trace interpretation let $x=\operatorname{tr}X$,
$y=\operatorname{tr}Y$, $z=\operatorname{tr}(XY)$, for determinant-one
matrices. Cayley--Hamilton gives
$\operatorname{tr}(X^2Y)=xz-y$ and
$\operatorname{tr}(XY^2)=yz-x$. The pair substitutions are consequently
$(X,Y)\mapsto(X,XY)$ for $A$ and $(X,Y)\mapsto(XY,Y)$ for $B$.
Using rows for the exponent vectors of the new pair gives
$$
R_A=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
R_B=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R_w=R_{\ell_s}\cdots R_{\ell_1}.
$$
This convention can also be checked directly on diagonal commuting
matrices, where the two angle coordinates transform by these matrices.
Column exponent conventions transpose the matrices and reverse the
corresponding substitution convention; no such alternative is mixed
into this proof.

Every factor is an elementary nonnegative unipotent of determinant
one. A product containing both has an adjacent $R_AR_B$ or $R_BR_A$,
of trace three. Multiplication on either side by either elementary
unipotent cannot decrease any entry of a nonnegative matrix. Hence
$\operatorname{tr}R_w\ge3$ and $\det R_w=1$, so its two eigenvalues
are positive reciprocal numbers with one greater than one. This is
the hyperbolic matrix convention, not a claim of uniform hyperbolicity
of the entire real character surface.

### Step 2. A common forward escape cone

Let $P\in\mathcal C_+$ and put $(a,b,c)=(|x|,|y|,|z|)$.
Because $xyz>0$, $xz$ and $y$ have the same sign. The new third
absolute value under $A$ is $ac-b$, which is positive and satisfies
$$ac-b\ge ac-c=(a-1)c\ge c.$$
The new first two absolute values are $a,c$, and the new product is
positive. Thus $A(P)\in\mathcal C_+$. Equality of the old and new
third absolute values holds exactly when $a=2$ and $b=c$.
Conjugation by $J$ proves the corresponding statement for $B$, whose
equality condition is $b=2$ and $a=c$.

Follow any infinite letter sequence in which both letters occur
infinitely often. The third absolute values are nondecreasing positive
integers. If bounded, they must eventually be constant. At any late
$A$ step equality forces the absolute triple to be $(2,c,c)$ and
leaves that absolute triple unchanged. At the next $B$ step the new
third absolute value is $c^2-2>c$, because $c>2$. This contradicts
eventual constancy. There are late $A$ steps and subsequent $B$ steps
by the assumption on the sequence. Therefore the third absolute value
tends to infinity. In particular, a periodic repetition of any word
under consideration escapes in $\mathcal C_+$.

### Step 3. All-large triples either descend or enter the cone

Consider $P\notin\mathcal S\cup\mathcal E$, so $a,b,c\ge2$.
If $xyz<0$, an $A$ step has third absolute value $ac+b$ and a $B$
step has third absolute value $bc+a$. Either image is in
$\mathcal C_+$. There is no zero-product case here.

Suppose $xyz>0$. If $c\ge\max(a,b)$, either $P\in\mathcal C_+$
or $a=b=c=2$; the latter was excluded by $P\notin\mathcal E$.
It remains that $c<\max(a,b)$.

If $a=b$, then $a=b>c\ge2$. Either letter produces third absolute
value $a(c-1)\ge a>2$, with positive product, and therefore enters
$\mathcal C_+$.

If $a>\max(b,c)$, an $A$ step produces
$ac-b>a(c-1)\ge a$ and enters $\mathcal C_+$. A $B$ step has
signed new magnitude $d=bc-a$ relative to the sign of $x$:

- If $d\le-2$, its image has all absolute values at least two and
  negative product, so the following letter enters $\mathcal C_+$.
- If $-1\le d\le1$, its image lies in $\mathcal S$.
- If $d\ge\max(b,c)$, its image lies in $\mathcal C_+$ unless
  $b=c=d=2$. That exceptional output would be in $\mathcal E$.
  Both $A$ and $B$ permute $\mathcal E$ (verified in Step 6), so
  by injectivity it has no preimage outside $\mathcal E$.
- In the remaining case, $2\le d<\max(b,c)<a$, the new maximum
  is strictly smaller than the old maximum $a$.

The case $b>\max(a,c)$ is the image of this exhaustive list under
$J$, which interchanges the two letters and the first two absolute
values. Thus a forward orbit avoiding $\mathcal C_+$ and
$\mathcal E$, while outside $\mathcal S$, has strictly decreasing
integer maxima at every step; the negative-product case cannot
persist for even one more step. Such a trajectory reaches
$\mathcal S$ after finitely many steps.

### Step 4. A periodic letter orbit has a small coordinate at every phase

If $P\in\mathcal S$ but $A(P)\notin\mathcal S$, then
$|x|,|z|\ge2$ and $|y|\le1$. The product $xz$ dominates $y$,
and
$$|xz-y|\ge |x||z|-1>\max(|x|,|z|),\qquad |xz-y|\ge3.$$
The product of the coordinates of $A(P)$ is positive. Hence this
exit from $\mathcal S$ enters $\mathcal C_+$. Conjugation by $J$
proves the same fact for a $B$ exit.

Expand an ordinary periodic $W$-orbit into all its chronological
letter phases. That expanded trajectory is finite and repeats, and
its letter schedule contains both letters. It cannot enter
$\mathcal C_+$ by Step 2. If a phase is in $\mathcal E$, all phases
are in $\mathcal E$, because both letters permute that set and are
injective. Otherwise Step 3 says that any phase outside
$\mathcal S$ must eventually reach $\mathcal S$. Step 4 says it
cannot leave $\mathcal S$ without entering the cone, contradicting
return to that phase. Therefore every phase is in $\mathcal S$.

There is an extra directional constraint. A triple $P=(x,y,z)$
with $|x|,|y|\ge2$ and $|z|\le1$ has both possible preceding
letter phases outside $\mathcal S$, since
$$
A^{-1}P=(x,xy-z,y),\quad B^{-1}P=(xy-z,y,x),
\quad |xy-z|\ge3.
$$
Such a triple cannot appear in a periodic expanded orbit. This is
why six possible lines with only a small third coordinate are not
part of $\mathcal D$.

### Step 5. Small-coordinate rotations force the 39-line cover

If two coordinates have absolute value at most one, the point is
in $\mathcal D_0$. Consider a periodic phase with exactly one
small coordinate. Step 4 excludes the third coordinate as that
coordinate. Suppose it is $x=c\in C$, so $|y|,|z|\ge2$.
While only $A$ is applied, the pair $(y,z)$ transforms by
$$M_c=\begin{pmatrix}0&1\\-1&c\end{pmatrix}.$$
Multiplication gives
$$M_0^4=I,\qquad M_1^3=-I,\qquad M_1^6=I,
\qquad M_{-1}^3=I.$$
In the $c=0$ case the coordinate absolute values encountered are
just $|y|,|z|$. In the $c=1$ case they belong to
$\{|y|,|z|,|y-z|\}$; in the $c=-1$ case they belong to
$\{|y|,|z|,|y+z|\}$. These lists follow by applying the displayed
$2\times2$ matrices for four, six or three steps, respectively.

If $c=0$, or if $c\in\{-1,1\}$ and $|y-cz|\ge2$, both
other coordinates therefore remain large through every $A$ step.
At the next $B$ step, which exists because both letters occur in
the repeated word, the only small coordinate is removed. Step 4
then puts the image in $\mathcal C_+$, a contradiction. Consequently
$c=\pm1$ and $|y-cz|\le1$. This is equivalent to
$z=cy+b$ with $b\in C$, and hence the phase belongs to
$\mathcal D_x$. The case of a sole small $y$ is obtained under the
explicit conjugacy $J$ and belongs to $\mathcal D_y$.

This proves the entire periodic cover, including intermediate phases.

### Step 6. Every displayed line consists of fixed points of a positive word

The matrix identities in Step 5 imply that $A^{12}$ is the identity
on each plane $x=c$, $c\in C$, and $B^{12}$ is the identity on
each plane $y=c$, $c\in C$. Put $F=B^{12}\circ A^{12}$.
It fixes every point with $x,y\in C$.

For every line $L$ of $\mathcal D$ choose $G\in\{A,B\}$ and
$r\in\{0,1,2\}$ as follows:

| Line | Choice | Image under $G^r$ |
|---|---|---|
| $(a,b,t)$, $a,b\in C$ | $G=A$, $r=0$ | $(a,b,t)$ |
| $(a,t,b)$, $a,b\in C$ | $G=A$, $r=1$ | $(a,b,ab-t)$ |
| $(t,a,b)$, $a,b\in C$ | $G=B$, $r=1$ | $(b,a,ab-t)$ |
| $(c,t,ct+b)$, $c=\pm1$, $b\in C$ | $G=A$, $r=2$ | $(c,cb,-ct)$ |
| $(t,c,ct+b)$, $c=\pm1$, $b\in C$ | $G=B$, $r=2$ | $(cb,c,-ct)$ |

The image always has its first two coordinates in $C$. The coordinate
preserved by $G$ is a fixed member of $C$ on the original line.
Therefore the positive word map
$$W_L=G^{12-r}\circ F\circ G^r$$
fixes every point of $L$: the middle map fixes $G^r(P)$, and
$G^{12-r}G^r(P)=G^{12}(P)=P$. It contains both letters, even when
$r=0$. This argument is symbolic in $t$, not an interpolation from
sample parameter values.

Writing a point of $\mathcal E$ as $(2\epsilon,2\eta,2\epsilon\eta)$,
$A$ changes its sign pair to $(\epsilon,\epsilon\eta)$, and $B$
changes it to $(\epsilon\eta,\eta)$. Both therefore permute
$\mathcal E$ and have square equal to the identity there.
$B^2\circ A^2$ fixes the whole set. The existential converse and
the equality of the two unions over words follow.

### Step 7. Exact level sets and the uniform 40-state bound

There are 27 axis-parallel lines in $\mathcal D_0$, six lines in
each of $\mathcal D_x$ and $\mathcal D_y$, and no line in one
collection coincides with a line in another: their varying-coordinate
directions distinguish the collections, and the fixed coordinate or
intercept distinguishes lines within each collection.

For an axis-parallel line with fixed coordinates $a,b\in C$,
$$K=t^2-abt+a^2+b^2.$$
For $\mathcal D_x$ or $\mathcal D_y$ with parameters $c=\pm1$,
$b\in C$,
$$K=t^2+cbt+b^2+1.$$
The line forms and their multiplicities are thus

| Quadratic form, allowing $t\mapsto-t$ | Number of lines |
|---|---:|
| $t^2$ | $3$ |
| $t^2+1$ | $12+4=16$ |
| $t^2-t+2$ | $12+8=20$ |

Each quadratic has at most two integer roots for a fixed $k$.
The three level families have no common values greater than four.
For the first two families, $u^2=v^2+1$ implies
$(u-v)(u+v)=1$, so the only common level is one. For the first
and third, $u^2=v^2-v+2$ implies
$$((2v-1)-2u)((2v-1)+2u)=-7;$$
the integer factor pairs of $-7$ give only $u^2=4$.
For the second and third, $u^2+1=v^2-v+2$ implies the same
factorization with right side $-3$, and only level two results.
These factor-pair arguments allow negative $u,v$ as well.

For $k>4$, consequently, $|X_k|$ is at most $6$, $32$ or $40$
according to its one possible level family. There are no points of
$\mathcal E$ at those levels. The possible levels at most four
are $0,1,2,4$. Their exact sets follow by substituting the possible
quadratic roots; an explicit description also removes line overlaps:

- $X_0=\{(0,0,0)\}$, of size one.
- $X_1$ consists of the six signed unit-axis points.
- $X_2$ consists of the 12 triples with absolute coordinates
  $(1,1,0)$ in arbitrary coordinate positions, and the four triples
  with all absolute coordinates one and positive product.
- $X_4$ consists of the six signed axis points of height two, the
  four all-unit triples of negative product, the 12 triples with
  absolute coordinates $(2,1,1)$ and positive product, and
  $\mathcal E$. Its size is $6+4+12+4=26$.

All negative levels and level three have empty candidate set. This
proves $|X_k|\le40$ for every integer $k$.

To construct $X_k$ exactly on a line whose form is $t^2+bt+c$,
compute $\Delta=b^2-4(c-k)$. There are no roots unless $\Delta$
is a nonnegative integer square; for its integer square root $d$,
the roots are $(-b\pm d)/2$ when integral. Substitute all such
roots on the 39 lines, deduplicate coordinate triples, and add
$\mathcal E$ when $k=4$. This is a finite algebraic prescription
with no chosen coordinate bound or period cutoff.

### Step 8. Complete ordinary cycle structure for every word

Index $X_k$ once, and for $L\in\{A,B\}$ define its matrix $T_L$
by
$$
(T_L)_{P,Q}=\begin{cases}1&L(P)=Q\in X_k,\\0&\text{otherwise.}\end{cases}
$$
Rows and columns each have at most one nonzero entry, because $L$
is a bijection on the full lattice. Thus these are partial-permutation
matrices, not stochastic matrices with an added absorbing state.
Use the chronological row-action product
$$T_w=T_{\ell_1}\cdots T_{\ell_s}.$$
Its nonzero arrows are exactly the word transitions all of whose
intermediate letter phases stay in $X_k$.

Every genuine periodic point and each of its letter phases belongs
to $X_k$, by Step 5, so its ordinary cycle is retained by this
partial matrix. Conversely, every directed cycle of $T_w$ is an
actual $W$-cycle, by its definition. This proves a necessary and
sufficient classification for every word and every level.
In particular, there is no need to assume that arbitrary points of
$X_k$ remain there under the word, and no whole-group finiteness
result has been substituted for this cyclic criterion.

Let $c_d(w,k)$ be the number of directed cycles of length $d$ in
$T_w$. The complete ordinary fixed-point and zeta formulas are
$$
\#\operatorname{Fix}(W^n;\{K=k\}(\mathbb Z))
=\operatorname{tr}(T_w^n)
=\sum_{d\mid n}d\,c_d(w,k),
$$
$$
\zeta_{w,k}(u)=\prod_{d=1}^{40}(1-u^d)^{-c_d(w,k)}
=\det(I-uT_w)^{-1}.
$$
For the determinant equality, each finite partial-injective component
is a directed cycle or a directed chain. A chain has nilpotent
adjacency matrix and contributes determinant one. A $d$-cycle
contributes $1-u^d$. This also proves that every period is at most
$|X_k|\le40$. These finite-graph consequences are classical
deductions once the arithmetic cover is proved.

### Step 9. Complete forward escape alternative

Fix a point whose repeated-word forward letter trajectory never
enters $\mathcal C_+$. If a phase lies in $\mathcal E$, bijectivity
and the invariance of that finite set make the initial point periodic.
Otherwise, Step 3 forces entry into $\mathcal S$, and Step 4
forces the trajectory to remain in $\mathcal S$ forever.
After one more letter, no point can have only a small third
coordinate: both possible predecessors of such a point are outside
$\mathcal S$, as computed in Step 4.

At any later phase with only a small first coordinate, Step 5's
rotation argument says that a point outside $\mathcal D_x$ enters
$\mathcal C_+$ by the next occurrence of $B$. That occurrence is
guaranteed by the repeated word. Conjugation by $J$ gives the same
conclusion for a sole small second coordinate. Every sufficiently
late phase is consequently in $\mathcal D$, and all such phases
have the fixed level $k=K(P)$. They lie in the finite set $X_k$.

In particular the ordinary forward $W$-orbit is eventually finite.
Some $W^i(P)=W^j(P)$ with $0\le i<j$; applying the inverse of
$W^i$ gives $P=W^{j-i}(P)$. Thus a cone-free forward trajectory
is periodic. Every nonperiodic point therefore enters the cone,
and Step 2 proves $\|W^n(P)\|\to\infty$.

### Step 10. Backward escape via the common reverser

Define $R(x,y,z)=(x,y,xy-z)$. It is an involutive polynomial
automorphism of the lattice. Substitution gives
$$RAR=A^{-1},\qquad RBR=B^{-1}.$$
If $U=\ell_1\circ\cdots\circ\ell_s$ is the positive map with
reversed chronological word, then $W^{-1}=RUR$.
If $P$ is nonperiodic for $W$, $R(P)$ is nonperiodic for $U$:
any positive power of $U$ fixing $R(P)$ would, after conjugation,
give a power of $W^{-1}$ fixing $P$.
Step 9 gives $\|U^n(R(P))\|\to\infty$.

A polynomial automorphism and its inverse take bounded sets to
bounded sets. More quantitatively, if $\|R(Q)\|\le M$, then
$Q=R(R(Q))$ satisfies $\|Q\|\le\max(M,M^2+M)$.
Hence escape of $U^n(R(P))$ implies escape of its image under $R$.
Since $W^{-n}(P)=R(U^n(R(P)))$, this proves the backward assertion.
All four claims follow. $\square$

## Quantifier and old-family counterexamples

The conventional composition $A^6\circ B^6$ fixes $(1,1,m)$ for
every integer $m$, because each sixth power is the identity on
its corresponding trace-one plane. Its matrix is
$R_A^6R_B^6=\left(\begin{smallmatrix}1&6\\6&37\end{smallmatrix}\right)$,
of trace 38. But
$$
(A\circ B)(1,1,m)=(m,m-1,m^2-m-1)
$$
lies in $\mathcal C_+$ for $m\ge3$. Those fixed points have
infinite whole-group orbits. Thus neither finite full-group orbit
classification nor the compact core plus axes gives the requested
single-word answer.

For the chronological word $ABB$, namely $B^2\circ A$, and
every nonzero integer $m$, the four points
$$
(1,m,m),\quad(-1,m,-m),\quad(1,-m,-m),\quad(-1,-m,m)
$$
form a four-cycle, by direct application of its three letters.
Their level is $m^2+1$, an entire level family absent from the
previous Fibonacci-map integer-periodic classification when $|m|\ge2$.
The associated matrix has trace four, so this is not a positive
even power of the Fibonacci matrix (whose positive even powers
have traces $3,7,18,\ldots$); odd powers have determinant minus
one. The theorem itself treats all positive two-letter words, not
just this separating example.

## Corrections or Missing Assumptions

- An exploratory 45-line superset included six lines with a small
  third coordinate only. Step 4 removes them. Neither the theorem
  nor the exact classifier uses that larger set.
- The 45-line symbolic graph in `line_automaton.py` is retained as
  a diagnostic derivation aid. Its first 39 lines are exactly the
  theorem's cover. Generic line transitions do not by themselves
  handle line intersections at small integer parameters; the exact
  point-level classifier in `classify_word.py` does.
- No smaller universal period list inferred from finite word
  probes is asserted. The proof only claims the proved bound 40.

## Verification and Open Risks

`classify_word.py` uses exact integer square roots and exact point
transitions. Its self-test checks the displayed low-level counts,
independent direct membership on a small box, and explicit cycle
closure for six words over levels $-20\le k\le100$.
`probe_positive_words.py` checks 178,605 point-word pairs from a
small box and 245 words, including the fixed-line counterexample;
it finds no violation of the 39-line cover. It also tests the two
one-step cone implications in a separate box. These are finite
falsification checks, not premises of the proof.
An independent symbolic substitution check additionally verifies all
39 line-realizing words, both common-reverser identities and the
displayed $m^2+1$ fourth-iterate identity, identically in the free
parameter. The displayed algebra remains the proof of those facts.

The remaining gate is independent verification of this proof and
the source-bounded assessment of the incremental theorem. General
trace-map escape, low-trace rotations, the trace/matrix correspondence
and finite-permutation zeta formulas are all classical and are not
claimed as new. There is no claim of exhaustive global literature
novelty and no manuscript admission in this document.
