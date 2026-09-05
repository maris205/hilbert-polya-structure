# Three literal contracts and bounded admission audit

These are AI-assisted scouting notes, **not papers**, not an independent gate,
and not a novelty claim. Definitions are frozen in INTAKE.md. The complete
proofs below are separated from unproved extrapolations.

## 1. ND1: an incomplete but real small-box signal

### Claim, assumptions and status

Let $G$ be any finite simple undirected graph on the fixed vertex set $[n]$,
including $n=0$. Write $N_G(u)$ for its open neighborhood and define

$$uv\in E(N(G))\iff |N_G(u)\triangle N_G(v)|=1.$$

The following four statements are **PROVABLE AS STATED**:

1. $E(N(G))\cap E(G)=\varnothing$; consequently the edgeless graph is the
   unique fixed point.
2. $N(G)$ is bipartite, with parts determined by the parity of old degrees.
3. Equal open-neighborhood classes can merge under iteration but never split.
4. For $n\ge4$, let $S(c,z)$ have center $c$, isolated vertex $z$, and edges
   from $c$ to every other vertex except $z$. Then
   $N(S(c,z))=S(z,c)$. These give $\binom n2$ distinct two-cycles.

The stronger claims that these are **all** recurrent states, that every
trajectory reaches them within four steps, and that the empty target uniquely
maximizes fibre size for every $n$ are **NOT CURRENTLY JUSTIFIED**. The full
boxes $n\le6$ establish these assertions only in those boxes (with smaller
size exceptions to the two-cycle family). We do not promote them to theorems.

### Strategy and dependency map

Open-neighborhood symmetry proves edge disjointness and persistent twins;
parity of a symmetric difference gives bipartiteness; four pair types give
the explicit recurrent family. None of these lemmas bounds how long a twin
partition can remain unchanged before a later merger. Therefore a bound on
the number of strict mergers is not an orbit clock.

### Proof

If $uv$ is an edge of $G$, then $v$ belongs to $N_G(u)$ but not $N_G(v)$,
while $u$ belongs to $N_G(v)$ but not $N_G(u)$. Thus their symmetric
difference has at least two elements. This proves (1); the edgeless graph
maps to itself, while no nonempty edge set can equal a disjoint edge set.

For any two finite sets, the parity of their symmetric-difference size is
the sum of their cardinalities modulo two. An output edge thus joins old
degrees of opposite parity. This proves (2), including graphs with empty
parity classes.

Suppose $N_G(u)=N_G(v)$. They cannot be adjacent, because the two diagonal
coordinates would disagree. For every $w\notin\{u,v\}$, the two tests
$|N_G(u)\triangle N_G(w)|=1$ and
$|N_G(v)\triangle N_G(w)|=1$ agree. The output pair $uv$ is absent because
the difference has size zero. Hence $N_{N(G)}(u)=N_{N(G)}(v)$. Applying the
same argument at successive epochs proves (3).

For (4), put $L=[n]\setminus\{c,z\}$, so $|L|=n-2\ge2$. The input
neighborhoods are $L$ at $c$, the empty set at $z$, and $\{c\}$ at each
leaf. Leaf pairs have difference zero; $c,z$ have difference $n-2\ne1$;
$c,\ell$ have difference $n-1\ne1$; and $z,\ell$ have difference one.
Exactly the edges of $S(z,c)$ result. Swapping the distinct center and
isolated vertex changes the graph, and determines a two-cycle uniquely.

### Separate inverse attempt and exact obstruction

The direct row-distance constraints merely restate the forward definition;
they are not a separate inverse theorem. A possible injection of a prescribed
fibre into the empty fibre, $G\mapsto G\cup N(G)$, fails already on five
vertices. With vertices $0,\ldots,4$ and lexicographically ordered edge bits,
take code $21$, or edges $01,03,12$. Its image has code $802$, edges
$02,13,24,34$; their union has image code $72$, edges $04,14$, which is not
empty. The verifier checks all three codes. This invalidates that proposed
max-fibre proof, not the bounded observed maximum itself.

**Disposition: RESERVE_BOUNDED_SIGNAL / NO_ADMISSION.** A future re-entry
must bring an actual all-size recurrence/attraction proof and a substantive
inverse atlas; re-running a larger graph box alone is insufficient.

## 2. D2G: exactly an occupied external operator

### Literal map and mathematical status

For every labelled simple graph, define $M(G)$ by

$$uv\in E(M(G))\iff d_G(u,v)=2.$$

Equivalently, $uv\notin E(G)$ and $N_G(u)\cap N_G(v)\ne\varnothing$.
This equivalence is **PROVABLE AS STATED**, by the definition of a length-two
path, and holds also for disconnected graphs. It is literally the metamour
operator in Erickson et al., Definition 2.1, on distinguishable vertices.
No conjugacy or encoding is needed.

One basic inverse check is $M(G)=\overline K_n$ exactly when every connected
component of $G$ is complete. In one direction, vertices in a clique are at
distance one and vertices in different components are disconnected. In the
other direction, a noncomplete connected component contains a shortest path
between nonadjacent vertices; its first three vertices exhibit a pair at
distance two. Sources of the empty target are therefore in bijection with
set partitions and number $B_n$, the Bell number, including $B_0=1$.
This elementary special fibre does not constitute a new inverse atlas.

The named owner studies the same iterates, periods and image question. All
claimed finite-map dynamics here is a control of that old operator.
**Disposition: KILL_EXACT_EXTERNAL_METAMOUR_OPERATOR.**

## 3. CCW: complete elementary finite-field branch, no fresh operator

### Claim, assumptions and status

Fix an odd prime $p$ and $Q(x,y)=x^2+y^2$ on $\mathbb F_p^2$. On every
ordered point triple $X=(A,B,C)$, let $T(X)=X$ if the points are collinear
(including repeated points); otherwise let $T(X)=(B,C,O)$, where $O$ is the
unique point equidistant from $A,B,C$ in squared distance. Put
$\epsilon=1$ for $p\equiv1\pmod4$ and $\epsilon=-1$ for
$p\equiv3\pmod4$.

The following statements are **PROVABLE AS STATED**. They are not claimed
new relative to the classical circumcenter-window, finite-circle and
singular-totalization mechanisms.

- Fixed points are exactly the collinear triples, of cardinality
  $F=p^5+p^4-p^3$.
- Besides those fixed points, the recurrent states are exactly noncollinear
  triples with $Q(A-C)=Q(B-C)\ne0$. Their number is
  $S=p^2(p-1)(p-\epsilon)(p-\epsilon-2)$.
- The maximum tail is one when $\epsilon=-1$, and two when $\epsilon=1$.
  Put $Z=0$ in the former case and $Z=2p^2(p-1)^2$ in the latter. The
  depth populations and image size are

  $$D_0=F+S,\quad D_2=Z(2p-3),\quad D_1=p^6-D_0-D_2,
  \qquad |\operatorname{im}T|=F+S+Z.$$

- There is a complete every-target one-step inverse below. The maximum
  fibre is $p$ if $\epsilon=-1$, attained exactly at nonzero antipodal
  targets about their third coordinate, and is $2p-3$ if $\epsilon=1$,
  attained exactly when the first two points are nonzero vectors on the two
  different isotropic lines through the third point. Numbers of maximizing
  targets are respectively $p^2(p^2-1)$ and $2p^2(p-1)^2$.

No formula for each eventual period is asserted here. The real Euclidean
period-eight assertion must **not** be transported to finite fields: the
full $p=5$ box has nontrivial period twenty.

### Strategy and dependency map

1. An invertible linear system defines the center; this proves closure.
2. Reflection supplies the inverse restricted to the nonnull isosceles core.
3. A null-radius special triangle maps directly to a held collinear triple.
4. Circle/line intersections give every full-carrier target fibre.
5. Elementary circle counts give populations, maxima and equality cases.

### Step 1: closure and fixed points

For a noncollinear triple, the center equations are

$$2(B-A)\cdot O=Q(B)-Q(A),\qquad
  2(C-A)\cdot O=Q(C)-Q(A).$$

The coefficient determinant is nonzero because $p$ is odd and the two
differences are independent. Expanding squared distances proves that their
unique solution is the required center. A moving state cannot be fixed:
equality of $(A,B,C)$ with $(B,C,O)$ would force $A=B=C$.

The number of noncollinear triples is
$p^2(p^2-1)(p^2-p)$, by choosing $A$, then $B\ne A$, then $C$ off $AB$.
Subtracting from $p^6$ gives $F$.

### Step 2: a recurrent core with an explicit restricted inverse

Every moving output $(B,C,O)$ satisfies $Q(B-O)=Q(C-O)$. Consider a
noncollinear isosceles target with this common value $r\ne0$. Translate so
$O=0$, and write $b=B-O$, $c=C-O$. If $Q(c-b)=0$, then equality of their
norms gives $(c-b)\cdot b=0$. A nonzero isotropic vector in a nondegenerate
two-dimensional dot space has its own line as perpendicular line. This
would put $b,c$ on the same isotropic line, contradicting noncollinearity.
Thus $Q(c-b)\ne0$.

Reflect $b$ across the nonisotropic line spanned by $c$:

$$a=\frac{2(b\cdot c)}r c-b.$$

Then $Q(a)=r$ and $Q(a-c)=Q(b-c)\ne0$. The vectors $a,b$ lie on the
line $x\cdot c=b\cdot c$ and are distinct, because otherwise $b$ would
be parallel to $c$. This line does not contain $c$: otherwise
$b\cdot c=r$ and $Q(b-c)=0$. Consequently $(a,b,c)$ is noncollinear,
isosceles at $c$ with nonzero squared radius, and has circumcenter zero.
It is a predecessor in the same proposed core.

This is the only such predecessor. Its first point must lie both on
$Q(x)=r$ and $Q(x-c)=Q(b-c)$, hence on the displayed line. The line's
direction is perpendicular to nonisotropic $c$, so restricting $Q$ gives
a genuine quadratic polynomial. Its two distinct solutions are $a,b$;
the solution $b$ repeats a point and is invalid. Thus the finite proposed core
has one predecessor per state within itself. These incoming edges already
use every source in that finite set, so no source in it can map outside.
Its restriction is a permutation,
so every state in this core is recurrent.

### Step 3: the complete temporal classification

The remaining noncollinear isosceles states have squared radius zero.
They do not exist when $\epsilon=-1$, since then $Q$ is anisotropic.
When $\epsilon=1$, their two vectors about the apex are nonzero and on
different isotropic lines. The apex itself is equidistant from all three
points with squared radius zero, so it is the circumcenter. The next
triple repeats the apex and is held forever. Such states have exact tail
one. Every state moves in one step to a collinear or an isosceles state;
this proves the upper bounds, the recurrent exhaustion, and the claim that
there are no other types of transient states.

The inverse below shows that all $Z=2p^2(p-1)^2$ noncollinear null-radius
isosceles targets have $2p-3$ predecessors. All those predecessors have
depth two: an isosceles null target is not recurrent, and no noncollinear
isosceles source can map to one (nonnull sources stay in the core and
null sources become collinear). Hence $D_2=Z(2p-3)>0$ for
$p\equiv1\pmod4$. For $p\equiv3\pmod4$, the noncore noncollinear
population is

$$p^6-F-S=p^2(p^2-1)(p-1)^2>0,$$

which gives sharp tail one. Finally, every collinear target supplies its
own source, every nonnull core target has its reflected core predecessor,
and every null isosceles target has the counted circle predecessors. No
other target lies in the image. This gives the stated image law.

### Step 4: every-target inverse, including the hold branch

For a target $Y=(B,C,O)$, let $h$ be one if $Y$ is collinear and zero
otherwise. The hold-branch predecessor is $Y$ itself exactly when $h=1$.
Moving predecessors are precisely

$$\{(A,B,C):\ Q(A-O)=Q(B-O)=Q(C-O),\quad A\notin\operatorname{line}(B,C)\},$$

with this set empty if $B=C$. The linear center equations prove both
necessity and sufficiency, and the moving and hold sets are disjoint.

For a cardinality formula, set $r=Q(B-O)$. If $B=C$ or
$Q(C-O)\ne r$, the fibre size is $h$. Otherwise:

$$\#T^{-1}(Y)=h+
\begin{cases}
p-\epsilon-2,&r\ne0,\\
p-1,&r=0,\ Q(C-B)=0,\\
2p-3,&r=0,\ Q(C-B)\ne0.
\end{cases}$$

The two zero-radius branches require $\epsilon=1$; with $\epsilon=-1$,
equal zero-radius points would coincide and were already handled.

For $r\ne0$, the circle has $p-\epsilon$ points. A line through two
distinct circle points cannot be contained in that circle; its intersection
consists exactly of $B,C$, which must be excluded. For $r=0$ the circle
is the union of two isotropic lines, with $2p-1$ points. If the chord is
isotropic, it is one entire component, so deleting it leaves $p-1$ points.
Otherwise the chord meets the two lines exactly at $B,C$, leaving $2p-3$.

For completeness the circle count uses no unproved conic estimate. Let
$\chi$ be the quadratic character, extended by $\chi(0)=0$. For $r\ne0$,
the equation $y^2=x^2-r$ has $p-1$ solutions, because
$(x-y)(x+y)=r$ and $2$ is invertible. Hence
$\sum_x\chi(x^2-r)=-1$. Therefore

$$\#\{(x,y):x^2+y^2=r\}
=p+\sum_x\chi(r-x^2)=p-\epsilon.$$

The zero circle has one point if $-1$ is nonsquare; if $i^2=-1$ it is
the union of $x+iy=0$ and $x-iy=0$. These arguments also give
$(p-1)(p-\epsilon)$ vectors of nonzero norm. Choosing an apex, such a
vector, and another equal-norm vector excluding its two collinear choices
proves $S=p^2(p-1)(p-\epsilon)(p-\epsilon-2)$.

### Step 5: maximum and all equality cases

If $\epsilon=-1$, nonzero-radius fibres have size $p-1+h$. Thus the
maximum is $p$, requiring collinearity with two distinct equal-radius
points. On their line, those points are antipodal about $O$; conversely
all such antipodal targets work. Choose $O$ arbitrarily and $B-O\ne0$,
then $C=2O-B$, giving $p^2(p^2-1)$ maximizing targets.

If $\epsilon=1$, nonzero-radius fibres have size at most $p-2$; a
zero-radius isotropic chord has $h=1$ and fibre $p$; a nonisotropic
zero-radius chord has $h=0$ and fibre $2p-3$. Since such primes satisfy
$p\ge5$, the last is strictly largest. Equality requires one nonzero
point on each of the two isotropic lines through $O$, and that condition
is sufficient. Choose the ordered lines, the two nonzero vectors and
$O$, giving $2p^2(p-1)^2$ targets. This exhausts all equality cases.

### Source subtraction and final status

Kanda–Koizumi define the same circumcenter window over the reals and own
the special-isosceles reduction and regular-core similarity mechanism.
They do **not** state the finite-field hold map or its arithmetic periods.
We therefore make no claim of a global conjugacy or whole-theorem transfer.
The field change and hold totalization do not make the classical window a
new operator class under this batch's admission rule. The special/null split
and finite-circle fibre arithmetic above are preserved as honest deductions,
not silently represented as a new selected system. The nearby internal
P161 already occupies finite-field triangle windows with singular branches;
P180 occupies finite-field scalar/similarity lifts. Neither is asserted to
be literally CCW.

**Disposition: KILL_CLASSICAL_WINDOW_FINITE_FIELD_SPECIALIZATION.**
No manuscript, paper number, accepted gate or positive novelty rating follows.
