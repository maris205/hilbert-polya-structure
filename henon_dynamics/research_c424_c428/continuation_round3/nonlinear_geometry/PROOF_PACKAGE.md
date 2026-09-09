# R3-NG-F: all-level integral Fricke exhaustion

2026-09-08 UTC. Coordinator's author proof, frozen for nonauthor review.
This is a proposed completion of the original full question, not an
admission, manuscript, numerical census, or priority claim. No mathematical
program was used. The earlier difference route is replaced by a direct
maximum-height argument; the object and quantifiers are unchanged.

## 1. Full object and effective classification theorem

Fix **any** ordered triple $(A,B,C)\in\mathbb Z^3$. Put
$a_0=A,a_1=B,a_2=C$, with subscripts modulo three, and
$$
K=x^2+y^2+z^2-xyz-Ax-By-Cz.
$$
The native map is $T=s_zs_ys_x$, rightmost first, with
$s_x(x,y,z)=(A+yz-x,y,z)$ and the analogous $s_y,s_z$.
All ordinary integral points, including zeros and singular fibre points,
remain in the domain. Set
$$
H=\max(|A|,|B|,|C|),\quad B_0=H+1,\quad R=100B_0,
\quad Q_R=([-R,R]\cap\mathbb Z)^3,\quad N_R=(2R+1)^3.
$$

**Theorem.** The complete integral periodic locus of $T$ is the union of:

1. at most 27 explicitly constructed affine integer lines, each consisting
   entirely of periodic points of a proved return time at most 54;
2. the cyclic vertices of the exact partial map $T:Q_R\dashrightarrow Q_R$.

The line construction is the 27-state graph in Section 3, with its stated
affine-return test. It contains all unbounded periodic families. A finite
parameterwise procedure removes coincidences/intersections and determines
exact least periods on every line and every remaining point. Thus it
determines all coexistence and every fibre's ordinary period counts, not
only a membership semidecision. There is no parameter or period cutoff.
The bound $\max(54,N_R)$ on native least periods is valid but not asserted
sharp; $R$ is also deliberately nonoptimal.

On each fixed level $K=D\in\mathbb Z$, each constructed line contributes
at most two points before de-duplication. All fibre period counts are
finite and effectively determined. No ordinary zeta on all of $\mathbb
Z^3$ is asserted when a whole line of fixed-iterate points exists.

## 2. Phase lift and the maximum-height entry

Use the auxiliary phase lift, not a replacement native clock:
$$
F(i;x,y,z)=(i+1;y,z,yz+a_i-x),\qquad i\in\mathbb Z/3\mathbb Z.
$$
Its inverse is $(i;x,y,z)\mapsto(i-1;xy+a_{i-1}-z,x,y)$.
The restriction of $F^3$ to phase zero is exactly $T$. A native periodic
point therefore gives a periodic scalar sequence
$$
x_{j+3}+x_j=x_{j+1}x_{j+2}+a_j.                 \tag{1}
$$
The maximum $M=\max_j|x_j|$ exists. It is also the maximum coordinate
height over its native $T$-orbit, since the native triples partition
the scalar indices into consecutive blocks of three.

Suppose $M>H+2$ and $|x_j|=M$. Applying (1) immediately to the left and
right of this coordinate gives
$$
|x_{j-1}|,|x_{j+1}|\le 2+H/M<3,
$$
so both neighbours have absolute value at most two by integrality.
If $|x_{j+1}|=2$, then
$|x_{j+2}|\ge2M-|x_{j-1}|-H\ge2M-2-H>M$, impossible.
The reverse inequality excludes $|x_{j-1}|=2$ in exactly the same way,
using $x_{j-2}=x_{j-1}x_j+a_{j-2}-x_{j+1}$.
Thus every periodic orbit with $M>H+2$ has a phase on a line
$$
L_{i,u,v}(t)=(i;u,t,v),\qquad u,v\in S:=\{-1,0,1\},\ t\in\mathbb Z,
                                                               \tag{2}
$$
and the parameter at that phase has absolute value $M$. There are 27
labelled lines. Phases are retained; reversing the ordered coefficient
triple is neither assumed nor used.

## 3. Exact 27-state line-return graph

A state is $s=(i,u,v)\in(\mathbb Z/3\mathbb Z)\times S^2$.
Each state has at most one outgoing edge, as follows.

**Type I, $v=\pm1$.** Put $b=a_i-u$ and $c=vb+a_{i+1}$.
There is an edge precisely when $c\in S$, to
$$
(i+2,v,c),\qquad h_s=2,\qquad t\longmapsto vt+b.       \tag{3}
$$
Indeed the next scalar entries are $vt+b$ and $v(vt+b)+a_{i+1}-t=c$.
Consequently (3) is the exact identity $F^2L_s(t)=L_{s'}(vt+b)$
for **every** integer $t$, not only large ones.

**Type II, $v=0$.** There is an edge precisely when
$a_i=u$ and $a_{i+2}\in S$, to
$$
(i,0,a_{i+2}),\qquad h_s=3,\qquad t\longmapsto-t+a_{i+1}. \tag{4}
$$
The next three entries are $0,-t+a_{i+1},a_{i+2}$, proving
$F^3L_s(t)=L_{s'}(-t+a_{i+1})$ identically.

Each existing edge has slope $\pm1$ and translation of absolute value
at most $B_0$. Its intervening images $F^rL_s(\mathbb Z)$,
$0\le r<h_s$, are injectively parametrized affine integer lines.
For Type I the only additional triple is $(t,v,vt+b)$;
for Type II they are $(t,0,0)$ and $(0,0,-t+a_{i+1})$.
No degree growth, numerical extrapolation, or undefined rational map
is hidden in these edges.

## 4. Uniform forcing of 27 successive transitions

Consider a periodic orbit with $M>R=100B_0$. Suppose that its current
state has the form (2), with
$$
|t|\ge M-jB_0,\qquad 0\le j\le27.                 \tag{5}
$$
Every scalar coordinate of this orbit still has absolute value at most
$M$. We show the outgoing edge must exist. Its new parameter then has
absolute value at least $M-(j+1)B_0$.

For Type I, put $t'=vt+b$; then $|t'|\ge M-28B_0$.
If $|c|\ge2$, the next scalar coordinate after the triple $(v,t',c)$
has magnitude at least
$$
2(M-28B_0)-1-H\ge2M-57B_0>M,
$$
a contradiction. Hence $c\in S$ and the edge exists.

For $v=0$, first put $b=a_i-u$ and $t'=-t+a_{i+1}$.
The next entries are $b,t',bt'+a_{i+2}$, followed by
$$
t'(bt'+a_{i+2})-b+a_i.                            \tag{6}
$$
Again $|t'|\ge M-28B_0$. If $|b|\ge2$, the third displayed entry
already has magnitude at least $2M-56B_0-H>M$.
If $|b|=1$, its magnitude is at least $M-29B_0$, and (6) has magnitude
at least
$$
(M-28B_0)(M-29B_0)-B_0>M.
$$
For clarity, both factors exceed $M/2$, while $M>100B_0\ge100$;
$M^2/4-B_0>M$ follows directly. Thus $b=0$ is necessary.
If now $|a_{i+2}|\ge2$, (6) has magnitude at least
$2(M-28B_0)-H>M$. Therefore $a_i=u$ and $a_{i+2}\in S$,
which are exactly the Type II conditions.

Starting from the maximum-height entry in Section 2, induction therefore
gives 27 graph transitions, all exact, before a height assumption can
be exhausted. Among the 28 visited states two agree. Since the graph is
deterministic, the path has reached a directed cycle. This argument does
not assume that an arbitrary high coordinate is itself globally maximal.

## 5. Cycle test and entire periodic lines

For a directed graph cycle $C$, let
$\ell_C=\sum_{s\in C}h_s$. Returning to the same phase implies
$3\mid\ell_C$. Compose its affine parameter maps to obtain
$$
F^{\ell_C}L_s(t)=L_s(\epsilon_Ct+\beta_C),
\qquad\epsilon_C\in\{1,-1\},\quad\beta_C\in\mathbb Z. \tag{7}
$$
Call the cycle **retained** iff $\epsilon_C=-1$, or
$\epsilon_C=1$ and $\beta_C=0$. This property is unchanged on moving
the base state around the cycle, since the affine maps are bijections.

If a cycle is not retained, (7) is a nonzero translation. Its iterates
are unbounded on every integer parameter, so no point on that cycle's
lines can be periodic under $F$.
For a retained cycle, (7) has order at most two. Every point on all its
lines and intermediate images is periodic under $F$, with a return
time dividing $\ell_C$ or $2\ell_C$, respectively.

Let $\widetilde{\mathcal L}$ be the union of these intermediate line
images for all retained cycles, and let $\mathcal L$ be its phase-zero
part with the phase label removed. The identities (3)--(4), with their
bijective integer parameter maps, show
$F\widetilde{\mathcal L}=\widetilde{\mathcal L}$; thus inverse images
remain in the same union as well. A periodic orbit reaching a graph
cycle must reach a retained one, and its entire preceding orbit is
therefore in $\widetilde{\mathcal L}$. Section 4 proves:
$$
\text{every native periodic orbit with height }M>R
\text{ is contained in }\mathcal L.                 \tag{8}
$$
Cycles use disjoint subsets of at most 27 states, each edge has length
at most three, and each lifted cycle has $\ell_C/3$ phase-zero
intermediate positions. Hence $\mathcal L$ is a union of at most 27
affine integer lines. Since $\ell_C\le81$, each such line has a native
return time $r_C=\ell_C/3$ or $2\ell_C/3\le54$.
These are proved return times, not claims of exact least period.

## 6. Complete residual rule and exact least periods

Compute the exact integer partial map on $Q_R$: put an arrow
$P\to T(P)$ precisely when $T(P)\in Q_R$. Its directed cycles are
computable by finite integer arithmetic. They are exactly the native
periodic orbits entirely contained in $Q_R$. Equivalently, a seed either
exits, or repeats within at most $N_R+1$ visited vertices; injectivity
ensures its first repeated vertex is its initial vertex. No arbitrary
time cutoff or unproved escape conjecture is needed.

Every periodic orbit outside $\mathcal L$ has height at most $R$ by
(8), and hence occurs here. Conversely all retained lines and all
finite-graph cycles consist of genuine periodic points. This proves
the asserted exhaustive union. The graph is an explicit terminating
residual rule for each ordered coefficient triple, not a performed
census of infinitely many coefficient triples.

For exact disjoint output, deduplicate coincident affine lines and
solve their pairwise linear intersection equations over the integers.
Each parametrization is injective and includes a coordinate of slope
$1$ or $-1$, as Section 3's formulas show. It therefore parametrizes
all integer points on its rational affine line; coincident line sets
really coincide on integers. Distinct lines meet at most once.

On a line $P(t)$ with certified native return $r\le54$, compute for
each positive divisor $d\mid r$ the three integer polynomials in
$T^dP(t)-P(t)$. Their common integer zero set is either all integers
(all three polynomials zero), or the finite common integer roots of
their nonzero gcd over $\mathbb Q[t]$. This is effective, for instance
by exact polynomial gcd and the rational-root theorem after removing
any factor of $t$. Assign each parameter the smallest such divisor.
This yields a generic least period and finitely many exact exceptions
on each line. Take the actual disjoint set union, also deleting line
points from the finite cyclic-vertex output. Periods and coexistence
are thus determined without overlap counting. A finite-graph cycle
has exact least period equal to its number of vertices, at most $N_R$.

## 7. Every level and its ordinary counts

Define the phase-labelled invariant
$$
K_i(x,y,z)=x^2+y^2+z^2-xyz-a_ix-a_{i+1}y-a_{i+2}z.
$$
Direct substitution gives $K_{i+1}(F_i(x,y,z))=K_i(x,y,z)$;
in particular $K_0\circ T=K_0$. On a state line (2),
$$
K_i(u,t,v)=t^2-(uv+a_{i+1})t+
u^2+v^2-a_iu-a_{i+2}v.                            \tag{9}
$$
It is monic quadratic. Every intermediate phase-zero image has the
same invariant polynomial in its transported integer parameter.
Thus a prescribed level $D$ has at most two points from each line,
before intersections, and at most $54+N_R$ periodic points in total.
Solve these quadratic integer equations and combine with the finite
core at level $D$, using Section 6's exact least periods and de-duplication.
Writing $c_d(A,B,C,D)$ for the resulting number of primitive native
cycles of length $d$, the actual ordinary fibre zeta is
$$
\zeta_{A,B,C,D}(z)=\prod_d(1-z^d)^{-c_d(A,B,C,D)}.
$$
This is a finite product with nonnegative integer exponents; ordinary
fixed-point counts are $\sum_{d\mid n}d\,c_d$. No multiplicity,
weight change, changed clock, target Euler factor or root number is
inferred. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## 8. Ownership and execution boundary

The Fricke object, Vieta involutions, invariant, and finite-graph
bookkeeping are not new. C421 owns the equal-forcing sharp scalar
classification and its certified universal core. Second-round helpers
and Cantat's fixed-fibre finiteness are already deducted. The proposed
increment here is the all-unequal-forcing, all-level global exhaustion
(8), with its explicit exceptional line family and effective residual
bound. Whether this is sufficiently independent remains for a
nonauthor source/increment review; mathematical closure does not
automatically admit a paper.

All statements above were derived by hand. Mathematical program runs:
**zero**. No finite-core graph was evaluated, no source PDF was newly
built or modified, no old certification was rerun, and no formal Route-A
evaluation, manuscript, or Git integration is represented by this proof.
