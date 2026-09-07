# Twenty-third desk: deductions and exact subtraction

2026-09-07 UTC. This is author/scout work, not an independent candidate
review. The literal carriers are those in INTAKE.md. No scientific pilot was
performed. Every displayed example below is symbolic arithmetic.

## Status and dependency map

**D1 full two-axis contract: NOT CURRENTLY JUSTIFIED.** The fixed-set,
scalar-adapter and invariant-graph inverse statements below are PROVABLE AS
STATED; no full recurrent classification, clock or fibre extremum follows.

**D2 temporal statement: PROVABLE AS STATED, but consumed by an exact old
nerve/strong-core adapter.** A separate inverse/extremal axis is NOT CURRENTLY
JUSTIFIED. Both descriptions close NO_PROMOTION.

Dependencies are explicit: D1 uses only field matrix algebra for the
deductions; the primary matrix-solvent source identifies the old primitive,
not an imported finite-field existence theorem. D2 uses the face/facet
incidence equivalence, then strong domination, then finite vertex loss. Its
source-owned core identification uses Barmak--Minian Theorem 2.11 and §3.

## 1. MSP: complete target representation, missing dynamics

Let $q$ be a prime power, $n\ge1$, and $A,B\in M_n(\mathbb F_q)$.

### 1.1 Closure and fixed set

Addition and multiplication preserve $M_n(\mathbb F_q)$, so the stated map
is total. If $(A+B,AB)=(A,B)$, the first equality gives $B=0$; the second
then holds. Conversely $(A,0)$ is fixed for every $A$. Thus the fixed set
has exactly $q^{n^2}$ elements. This classifies fixed points only.

### 1.2 Exact scalar historical adapter and a strict four-cycle

The map $j(x,y)=(xI_n,yI_n)$ is injective because $n\ge1$. Writing
$v(x,y)=(x+y,xy)$, direct multiplication gives $Tj=jv$. Hence the scalar
map is the exact restriction to the scalar-pair invariant subspace, not a
conjugacy of the full noncommutative matrix carrier. The old C8 entry in
the P122--P126 algebraic scout defines precisely $v$, as does the nearer
SP entry in this batch's second algebra scout over prime fields.

In characteristic five,

$$2+2=4,\quad2\cdot2=4;\qquad4+4=3,\quad4\cdot4=1;$$
$$3+1=4,\quad3\cdot1=3;\qquad4+3=2,\quad4\cdot3=2.$$

The four distinct scalar pairs displayed in INTAKE.md therefore form a
strict four-cycle. Their scalar matrix images give the same period for
every $n\ge1$ over every field of characteristic five. In particular,
universal convergence to the fixed set and a universal period-two ceiling
are false. This does not preclude a richer theorem; no such full theorem
is established here.

### 1.3 Complete one-target source-set bijection

Fix $(S,P)\in M_n(\mathbb F_q)^2$. The equation $T(A,B)=(S,P)$ first
forces $B=S-A$, and its second equation becomes

$$A(S-A)=P\iff A^2-AS+P=0.$$

Consequently,

$$\{X:X^2-XS+P=0\}\longrightarrow T^{-1}(S,P),\qquad
X\longmapsto(X,S-X)$$

is bijective. Surjectivity is the displayed elimination; injectivity follows
from the first source coordinate. No invertibility hypothesis is required.

For an equivalent linear-geometric formulation, let $W=\mathbb F_q^n$ be
row vectors and let

$$C_{S,P}=\begin{pmatrix}0&-P\\ I_n&S\end{pmatrix}$$

act on $W\oplus W$ by right multiplication. For each $X$, its row graph
$G_X=\{(u,uX):u\in W\}$ has dimension $n$, and its first-coordinate
projection to $W$ is an isomorphism. Conversely every $n$-dimensional
subspace with that projection property is $G_X$ for a unique matrix $X$:
the second coordinate of the inverse projection is a linear map on $W$.

Now

$$(u,uX)C_{S,P}=(uX,-uP+uXS).$$

This vector lies in $G_X$ for every $u$ if and only if its second component
is $(uX)X=uX^2$ for every $u$, equivalently $X^2-XS+P=0$. Thus the entire
target fibre is also in bijection with the transverse invariant row graphs
of $C_{S,P}$. This is a representation of all predecessors, not an evaluated
count or an extremum. Enumerating all such invariant subspaces would merely
restage the original inverse problem unless a further structural theorem
were proved.

The matrix equation is precisely the left-solvent form of a quadratic
matrix polynomial. Transposition turns it into the right-solvent form.
Higham--Kim's primary §1 explicitly distinguishes these forms; its complex
analytic existence and spectral counting hypotheses are **not** asserted
over arbitrary finite fields here. The elementary graph calculation above
is valid independently over the stated field.

### 1.4 A noncommutative identity is not a temporal theorem

Write $D=AB-BA$. After one step the new commutator is

$$[A+B,AB]=A^2B+BAB-ABA-AB^2=AD-DB.$$

Although the commuting locus is invariant, the variable coefficients $A,B$
give no filtration loss on all matrix pairs. A restriction to triangular
or nilpotent coefficient algebras would change the current full carrier and
invoke excluded standard filtration mechanisms. No such restriction is
offered as a replacement proof. D1 closes with its two stated gaps.

## 2. MFI: exact square-nerve realization consumes recurrence

Let $K$ be a nonempty-vertex simplicial complex on a subset $V$ of $[n]$.
All facets are nonempty. Define signatures and representatives as in
INTAKE.md. The family of signatures is finite and nonempty, and every
signature lies in a maximal one, so $R(K)$ is nonempty.

### 2.1 Face/facet incidence and the nerve square

The facet nerve $N(K)$ has vertex set $\mathcal F(K)$; a set of facets is a
face exactly when its total intersection is nonempty. A family $\Sigma$ of
facets has nonempty intersection if and only if it is a subset of $S_v$
for some $v\in V$. Therefore its maximal faces are exactly the distinct
inclusion-maximal signatures.

Let $\mathcal M$ be that family. The assignment $\Sigma\mapsto r_\Sigma$,
where $r_\Sigma$ is the least-labelled vertex with signature $\Sigma$, is
a bijection from $\mathcal M$ to $R(K)$. A family
$\Sigma_1,\ldots,\Sigma_k$ is a face of $N^2(K)$ if and only if there is
an old facet $F$ in all the $\Sigma_i$. By definition of the signatures,
this holds if and only if all $r_{\Sigma_i}$ belong to $F$. A finite vertex
set belongs to a common facet if and only if it is a face of $K$. Thus this
bijection and its inverse preserve faces, giving the explicit isomorphism

$$N^2(K)\cong K[R(K)]=T(K).$$

Forgetting labels hence intertwines $T$ with the square of the old nerve
map. This is not a bijective conjugacy of the two entire labelled carriers.

The old C06 uses complexes with at most $N$ vertices and $N$ facets.
If $K$ has $v$ vertices and $f$ facets, the calculation above shows that
$N(K)$ has $f$ vertices and at most $v$ facets. Hence that bounded class is
invariant. Taking $N=2^n$ accommodates the full current carrier and every
nerve iterate. This is an exact symbolic parameter adapter, not a larger
experimental box or a numerical run.

### 2.2 Dominated vertices and the full fixed/recurrent classification

If $v\notin R(K)$, choose a maximal signature $\Sigma\supseteq S_v$ and
its representative $r_\Sigma\in R(K)$. It differs from $v$ and every
facet containing $v$ also contains $r_\Sigma$. More explicitly, for each
face $\sigma$ containing $v$, choose a facet $F\supseteq\sigma$. Then
$r_\Sigma\in F$, so $\sigma\cup\{r_\Sigma\}$ is a face. Thus $v$ is
dominated by a retained vertex.

Delete the unretained vertices one at a time. The same face argument still
works after any subset of those vertices has been removed, since the
dominating representative is retained. Each deletion is a strong collapse;
their composition produces the full induced complex $K[R(K)]$. This is
exactly the construction allowed in Barmak--Minian Proposition 3.4 and
Lemma 3.3, with its choices fixed by labels.

The equality $T(K)=K$ holds if and only if every vertex is retained. This
is equivalent to all signatures being distinct and pairwise incomparable.
Indeed an equality class of size at least two loses a representative, and
a strict inclusion loses its smaller member. Conversely no vertex is
discarded when neither occurs. The same condition says that no vertex is
dominated by another.

Whenever $T(K)\ne K$, at least one vertex is removed. Thus a periodic
orbit cannot have a nonfixed step. All recurrent states are exactly the
fixed complexes just described. Starting with $m\ge1$ vertices, the number
of nonfixed steps is at most $m-1$, because at least one vertex remains.
This coarse upper bound is not claimed sharp. Successive strong collapses
end at a minimal complex, hence at the classical strong core, unique up to
isomorphism by the source theorem. The selected labelled copy may depend on
the label order; no label-independent endpoint is claimed.

### 2.3 Inverse boundary

A source for a target must realize the target as the induced subcomplex on
the selected maximal-signature representatives. The discarded vertices can
have many incidences, and deleting them can merge or change facets. No
evaluated source grammar, target-fibre census or sharp maximum is supplied.
Restating the representative test for all possible sources would not be an
independent inverse theorem. Since the temporal mechanism is already owned
and internally screened, no pilot is warranted.

## 3. Verification and final boundary

The proofs were checked for singular matrix inputs, multiplication order,
all prime powers, nonempty complex closure, label ties, and both directions
of the inverse and nerve equivalences. The incidence helper also mentioned
the harmless fixed vertex-free completion; the final literal here is the
nonempty-vertex carrier declared in INTAKE.md, so no nerve convention for a
vertex-free complex is needed. There was no pilot to amend or rerun.

No full two-axis author contract, sharp temporal maximum, source clearance,
independent review or admission is asserted. This is a closed negative desk,
not evidence that no other useful finite-system direction exists.
