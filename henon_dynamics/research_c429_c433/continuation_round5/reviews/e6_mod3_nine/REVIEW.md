# E6: modulo-three constraints on invariant reversible nine-cycles

2026-09-10 UTC. Separately allocated, current-team nonauthor mathematical
review. The reviewed material is the new Section 12 of
[C2 REPORT.md](../../c2_composition_exact_spectrum/REPORT.md), together with
the staircase definition and involution action in its Section 11.1.

## Verdict and precise scope

**PASS: zero open mathematical must-fixes.**

All three new hand arguments are valid with their stated integral domains
and additional hypotheses:

1. For every polynomial map $T:\mathbb Z_3^2\to\mathbb Z_3^2$ with
   coefficients in $\mathbb Z_3$ and constant Jacobian determinant $+1$
   or $-1$, there is no orbit of ordinary least period nine whose nine
   integral points have the same reduction in $\mathbb F_3^2$.
2. For arbitrary $p,q\in\mathbb Z[t]$, put
   $I(x,y)=(x,q(x)-y)$, $J(x,y)=(p(y)-x,y)$ and $F=JI$.
   If an integer least-nine orbit $C$ additionally satisfies $I(C)=C$,
   its reduced native orbit modulo three has least period exactly three.
3. The nine-vertex staircase of Section 11.1 cannot be realized by such
   integer polynomials when each coordinate alphabet is an arbitrarily
   ordered five-term integer arithmetic progression with nonzero step.
   Both starting integers, both nonzero steps, both permutations, and
   all polynomial degrees and coefficients are unrestricted.

The first lemma concerns points of $\mathbb Z_3^2$, as required by its
integral polynomial-map setting and by every application here. Its proof
does not assert a result for nonintegral points in $\mathbb Q_3^2$, points
over arbitrary residue extensions, or higher-dimensional maps.

The second and third statements are not a universal integer-nine exclusion
for Hénon words. The additional invariant-orbit hypothesis in statement 2
and the specific graph and alphabets in statement 3 are essential to the
arguments actually given.

## 1. Actual-file binding and independence

The final 796-line report has SHA-256

$$
\texttt{772c669813033b0d09acd6ca09776f7bb69a610b1a22231709e1cad501cbacba}.
$$

Its new Section 12, lines 692--796, was read in full after the author
corrected the stray comma in the matrix-power exponent. Section 11.1
was read directly for the vertex definitions, both involution
permutations and the actual native order of the nine vertices.
The original integer-orbit domain in Section 1 was also inspected.

The historical E4 report-prefix binding is not evidence that Section 12
had already been reviewed. The period-sixteen proof, previous diagnostics,
their source programs and their numerical counts are not re-reviewed or
rerun here. No step below uses the old no-hit output as a mathematical
premise. The whole-report hash identifies the bytes; this verdict covers
only the newly allocated sections and interfaces.

## 2. Local nine exclusion: normalization is valid

Start with a hypothetical least-nine orbit in $\mathbb Z_3^2$ contained
in one residue class. If $\det DT=-1$, replacing $T$ by $T^2$ makes its
constant determinant $+1$. Since multiplication by two permutes
$\mathbb Z/9\mathbb Z$, the same points still form one least-nine orbit.
This is a valid contradiction reduction, not a claim that changing the
native clock preserves every possible period.

Write the reordered orbit as $z_0,\ldots,z_8$, with indices modulo nine,
and use

$$
\nu(z)=\min\{v_3(z_1),v_3(z_2)\},\qquad \nu(0)=+\infty.
$$

An integral polynomial map preserves every coordinatewise congruence:
each coordinate difference $T(x)-T(y)$ belongs to the ideal generated
by $x_1-y_1,x_2-y_2$ after evaluation at integral points. Therefore

$$
\nu(z_{i+2}-z_{i+1})\ge\nu(z_{i+1}-z_i).
$$

Going once around the orbit forces equality at every step. The common
value is a finite integer $d\ge1$, since consecutive orbit points are
distinct and all points are congruent modulo three. Telescoping also gives
$z_i-z_0\in3^d\mathbb Z_3^2$ for every $i$.

Set $a=3^{d-1}$ and

$$
g(X)=a^{-1}\bigl(T(z_0+aX)-z_0\bigr).
\tag{R1}
$$

Translation of a polynomial at the integral point $z_0$ has integral
coefficients. Each positive-degree coefficient of total degree $k$
in (R1) has a factor $a^{k-1}$, which is integral even at the boundary
$d=1$. Its constant term

$$
v=g(0)=a^{-1}(z_1-z_0)
$$

has vector valuation exactly one. Thus $g$ is an integral polynomial
map, its transformed orbit starts at zero and lies in $3\mathbb Z_3^2$,
and the transformed least period is still nine.

The scalar changes in the derivative cancel:

$$
Dg(X)=DT(z_0+aX),\qquad \det Dg=1.
$$

No inverse polynomial for $T$ is required; the argument uses only its
integral coefficients, the actual finite orbit and the constant determinant.

## 3. The first Taylor congruence forces the required matrix type

Let $A=Dg(0)$ and $u=(v/3)\bmod3\ne0$. Since all nonlinear monomials
are divisible by nine on $3\mathbb Z_3^2$,

$$
g(z)\equiv v+Az\pmod9
$$

holds at every point used in the nine successive iterates. Induction gives

$$
g^9(0)\equiv\sum_{i=0}^8A^iv\pmod9.
$$

The exact return $g^9(0)=0$, followed by division of this congruence by
three, implies

$$
\left(\sum_{i=0}^8\overline A^i\right)u=0.
\tag{R2}
$$

In $\mathbb F_3[X]$, $X^9-1=(X-1)^9$, so division by the monic
polynomial $X-1$ gives $\sum_{i=0}^8X^i=(X-1)^8$. Substituting the
matrix in this polynomial identity is legitimate. Thus
$(\overline A-I)^8u=0$. An invertible matrix has invertible eighth
power; the nonzero $u$ proves that $\overline A-I$ is singular.

Because $\det\overline A=1$ and the matrix is two-dimensional,

$$
0=\det(\overline A-I)=2-\operatorname{tr}\overline A.
$$

Its characteristic polynomial is therefore $(X-1)^2$, and
Cayley--Hamilton gives $N^2=0$ for $N=\overline A-I$. It follows that

$$
\overline A^3=I,\qquad
I+\overline A+\overline A^2=0.
\tag{R3}
$$

This includes $\overline A=I$; a nontrivial Jordan block is not assumed.
Neither the identity matrix case nor a determinant-sign case has been
discarded. The two-dimensional determinant information is used exactly
at the trace/characteristic-polynomial step.

## 4. The second displacement has a noncancelling leading term

Put $h=g^3$ and $w=h(0)$. The same first Taylor congruence and (R3)
give $w\equiv0\pmod9$. Least period nine gives $w\ne0$, so

$$
e=\nu(w)\quad\text{is finite and }e\ge2.
$$

The points $0,g(0),g^2(0)$ lie in $3\mathbb Z_3^2$, where
$Dg(z)\equiv A\pmod3$. The chain rule therefore gives

$$
B=Dh(0)\equiv\overline A^3=I\pmod3.
$$

Write $B=I+3C$ with $C\in M_2(\mathbb Z_3)$. To audit the Taylor
remainder explicitly, write

$$
h(z)=w+Bz+Q(z),
$$

where every monomial of $Q$ has total degree at least two and integral
coefficient. No division by a Taylor factorial is involved.
For $z\in3^e\mathbb Z_3^2$, $Q(z)\in3^{2e}\mathbb Z_3^2$ and
$h(z)\in3^e\mathbb Z_3^2$. Hence

$$
\begin{aligned}
h^2(0)&=(I+B)w+Q(w),\\
h^3(0)&=(I+B+B^2)w+R,\\
R&=BQ(w)+Q(h^2(0))\in3^{2e}\mathbb Z_3^2.
\end{aligned}
\tag{R4}
$$

Ordinary matrix multiplication gives

$$
I+B+B^2=3I+9C+9C^2.
$$

Since $2e\ge e+2$, (R4) proves

$$
h^3(0)\equiv3w\pmod{3^{e+2}}.
\tag{R5}
$$

At least one coordinate of $3w$ has valuation exactly $e+1$.
Every error coordinate has valuation at least $e+2$, including the
boundary case $e=2$. Thus $h^3(0)\ne0$, contradicting
$h^3(0)=g^9(0)=0$. This closes the local lemma without a finite search,
coefficient bound, degree bound, or unproved local-period theorem.

## 5. The invariant reversible orbit has reduced least period three

For the two triangular maps in the report, $I^2=J^2=1$,
$F=JI$, $\det DF=1$, and $IFI=F^{-1}$ hold as polynomial identities.
If $I(C)=C$, then $J(C)=FI(C)=C$ as well.

Choose $P\in C$ and let $I(P)=F^kP$. The reversal identity gives

$$
I(F^jP)=F^{k-j}P.
$$

Because the nine native orbit points are distinct, a fixed point of
$I|_C$ is equivalent to $2j=k$ in $\mathbb Z/9\mathbb Z$.
There is exactly one such index. The existence of $k$ uses $I(C)=C$;
it is not a consequence of reversibility alone.

Reduction commutes with $F$. The reduced native least period $m$
divides nine, so $m=1,3,$ or $9$.

If $m=9$, reduction is a bijection from $C$ to all nine points of
$\mathbb F_3^2$. It intertwines $I|_C$ with $\overline I$.
Fixed points correspond in both directions: if a reduction is fixed,
then $I(P')$ is another point of $C$ with the same reduction as $P'$;
injectivity forces $I(P')=P'$. On the other hand,

$$
\overline I(x,y)=(x,\overline q(x)-y)
$$

has exactly three fixed points, because each $x\in\mathbb F_3$
allows exactly one solution of $2y=\overline q(x)$.
This contradicts the single fixed point on $C$.

If $m=1$, the nine integral points are all congruent modulo three.
The local lemma applies to $F$, whose determinant is the constant one,
and excludes this alternative. Therefore $m=3$ exactly.

In this remaining case the reduced orbit has three distinct residue
points and each is occupied three times. The action of $F^3$ in each
occupied residue class is a least-three cycle. The local least-nine
lemma does not exclude it. Without $I(C)=C$, the fixed-point
comparison above is unavailable; the argument does not establish
nonexistence, or existence, of the residue-nine branch for general words.

## 6. Every pair of five-term AP alphabets is excluded for this graph

The actual Section 11.1 vertices are

$$
v_{2i}=(x_i,y_i),\quad v_{2i+1}=(x_i,y_{i+1})\quad(0\le i<4),
\qquad v_8=(x_4,y_4).
\tag{R6}
$$

The specified interpolation values make $I$ exchange the pairs
$(v_0,v_1),(v_2,v_3),(v_4,v_5),(v_6,v_7)$ and fix $v_8$.
They make $J$ fix $v_0$ and exchange the adjacent complementary pairs.
Directly composing these permutations gives the nine-cycle

$$
v_0,v_2,v_4,v_6,v_8,v_7,v_5,v_3,v_1.
$$

Distinct coordinate alphabets make all nine vertices distinct, with no
requirement that either ordering be increasing. Thus any realization
really has least period nine and satisfies $I(C)=C$.

Section 5 then implies that the count of vertices with any fixed
first-coordinate residue, and likewise with any fixed second-coordinate
residue, is a multiple of three: each such set is a union of occupied
residue-point fibers, each of cardinality three.

In (R6), $x_0,x_1,x_2,x_3$ each occur twice and $x_4$ once.
If a five-term arithmetic progression has step not divisible by three,
its residues have multiplicities $2,2,1$ regardless of its starting
integer, step sign or permutation. Of the two residues occurring twice,
at least one contains no exceptional value $x_4$. That residue therefore
occurs in exactly four vertices, contradicting divisibility by three.
The first-coordinate step must be divisible by three.

For the second coordinate, the exceptional value is $y_0$, occurring
once; $y_1,\ldots,y_4$ each occur twice. The identical argument forces
the second-coordinate step to be divisible by three.
Both coordinate alphabets are now constant modulo three, so all nine
vertices have the same residue pair. The local lemma gives the final
contradiction.

This covers arbitrary integer starts, arbitrary nonzero positive or
negative steps, arbitrary independent orderings, and integer polynomials
of every degree. It uses no bounded interpolation census.
It does not cover arbitrary five-element alphabets, repeated coordinate
values, another involution graph, non-invariant orbits, or longer words.

## 7. Disposition and execution boundary

The new section is a complete elementary hand proof of these three
bounded statements. Its only general ingredients are polynomial
congruence preservation, integral polynomial expansion, finite-cycle
arithmetic and the two-dimensional Cayley--Hamilton identity, with
their required uses checked explicitly above. No literature-priority
search or novelty conclusion is part of this allocation.

The corrected final report hash was checked before finalization.
No additional author repair is required. The first lemma's integral
$\mathbb Z_3^2$ domain, the additional $I(C)=C$ hypothesis and the
special AP staircase scope must remain attached to subsequent uses.

Research-review guidance supplied the independent argument and
quantifier audit. The current-team, proof-only assignment excludes the
generic external-model workflow. Only this new review was written:
zero mathematical executions, new agents, API calls, previous-review
edits, author/shared-file edits, Git actions or manuscript/PDF work.

**Final disposition: accept Section 12 at the stated scope.**
The full integer-period-nine question for arbitrary integral Hénon
words remains outside this result, as do the other missing lengths
in the exact universal spectrum. No new paper admission follows.

NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
