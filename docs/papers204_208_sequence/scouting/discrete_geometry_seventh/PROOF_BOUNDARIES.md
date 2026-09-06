# Seventh geometry scout — deductive boundaries and full adapters

Author: `batch197_fifth_scout`, 2026-09-06 UTC. This is author scout
work, not an independent gate, manuscript or accepted theorem contract.
The six literal carriers, schedules, tie rules and fixed pilot cutoffs
are in [INTAKE](INTAKE.md). Every result below refers to those exact
rules. No cutoff was enlarged. Every disposition is `NO_PROMOTION`.

## Claim, status, assumptions and notation

For a finite self-map $F$, the tail $h(s)$ is the number of updates
before the first recurrent state, and $H=\max_s h(s)$. Image size,
recurrent-state count and number of cycles are different quantities.
The statements explicitly proved below are `PROVABLE AS STATED`;
the stronger admission conjunctions identified under open risks are
`NOT CURRENTLY JUSTIFIED`. A displayed finite census is not a proof
of an arbitrary-parameter conclusion.

All dimensions and population sizes are positive integers unless the
OLS half-widths are explicitly allowed to be zero. States include all
empty subsets where a subset carrier is used. All arithmetic, tie
choices and labelled coordinates are those fixed in the intake.

## Strategy and dependency map

1. QHK: exact rounding inequalities give an acyclic directed map of
   occupied cohorts; a collision at every nonfixed step gives a generic
   support-loss bound. Histogram pushforward and multinomial allocation
   give the complete labelled one-step inverse adapter.
2. OLS: one common strict rank potential proves convergence under both
   compressions. Row occupancies, independent row subset choices and
   diagonal occupancies reconstruct every source fibre.
3. MER: maximal empty rectangle existence and centre containment prove
   disjointness, the empty-target fibre and absence of fixed states.
   They do not bound general periods or reconstruct sources.
4. NTL: unique distance-zero sites prove the only fixed state. On a
   line, consecutive-site midpoint geometry proves an erosion clock.
   This line argument is not extended to two dimensions.
5. NSV: the literal four-bit test gives complement invariance. Two
   diagonal stripe families are verified by residue arithmetic; one
   has period equal to the torus side and one is fixed.
6. LVC: the selected cell-count vector is a subgradient. A quadratic
   identity proves strict potential increase and identifies the exact
   DCA adapter. Ordered sites give a unique assignment for each target
   volume vector and hence a complete difference-constraint inverse.

The elementary deductions are written out rather than inferred from
the external sources. [Source boundaries](SOURCE_AND_REPLAY.md) records
what was actually read and which classical interfaces are deducted.

## 1. QHK — cohort merger and labelled histogram inverse

### Exact claim and proof

For all $L,k\geq1$, every orbit becomes fixed, with
$h(x)\leq |\operatorname{supp}(x)|-1\leq\min(L,k)-1$.
The following formula counts the one-step fibre of every labelled target.

**Step 1 — literal rounding.** Let $c_z$ count source particles at
position $z$, extending $c_z=0$ outside $0\leq z<L$. If $c_z>0$,
all labels at $z$ move together to a position $a_c(z)$. Their mean is

$$
z+\frac{c_{z+1}-c_{z-1}}{c_{z-1}+c_z+c_{z+1}}.
$$

The fraction lies strictly between $-1$ and $1$, since $c_z>0$.
The specified half-down rule therefore gives

$$
a_c(z)=
\begin{cases}
z+1,&c_{z+1}>c_z+3c_{z-1},\\
z-1,&c_{z-1}\geq c_z+3c_{z+1},\\
z,&\text{otherwise}.
\end{cases}
$$

The first inequality cannot hold at $z=L-1$ and the second cannot
hold at $z=0$. Each nonstationary destination is occupied in the old
state. Thus $a_c$ is a self-map of the old occupied-position set.

**Step 2 — a merger on each nonfixed step.** Give occupied position
$z$ the lexicographic priority $(c_z,-z)$. Every nonself arrow of
$a_c$ increases this priority strictly: a right move has greater
destination mass, while a left move has at least the original mass
and a smaller position. Hence the directed graph of $a_c$ has no
nontrivial cycle. Starting with a nonself arrow and following arrows
ends at a fixed vertex. The last nonself arrow and that vertex itself
have the same image, so $a_c$ is not injective. All labels at an old
position remain a cohort, and no destination is new. Consequently
every nonfixed update strictly reduces the number of occupied
positions. That positive integer can fall at most its initial value
minus one times. This proves convergence and the stated bound.

**Step 3 — complete inverse.** Fix a labelled target
$y=(y_1,\ldots,y_k)$ and let $d_z=\#\{i:y_i=z\}$. For any weak
composition $c=(c_0,\ldots,c_{L-1})$ of $k$, define

$$
(a_*c)_z=\sum_{u:c_u>0,\ a_c(u)=z}c_u.
$$

Then

$$
|F^{-1}(y)|=
\sum_{\substack{c_0+\cdots+c_{L-1}=k\\a_*c=d}}
\frac{\prod_{z=0}^{L-1}d_z!}{\prod_{u=0}^{L-1}c_u!}.
$$

To prove this, first fix $c$ with $a_*c=d$. For each output position
$z$, partition the $d_z$ distinct labels whose target is $z$ among
old positions $u$ satisfying $a_c(u)=z$, assigning exactly $c_u$
labels to each. There are $d_z!/\prod_{u:a_c(u)=z}c_u!$ choices.
Choices for distinct $z$ use disjoint labels and are independent.
They determine every coordinate of one source and every such source
arises exactly once. Multiplying and then summing over distinct
source histograms proves the formula, including zero fibres and the
convention $0!=1$.

### Deduction and open risks

Both mechanisms are complete generic adapters: acyclic cohort merging
and labelled occupancy allocation. The displayed inverse is an exact
finite histogram sum, not a new closed all-parameter maximum-fibre
law. The observed $H\leq2$ in the original boxes is **not** proved
for all $L,k$ and is not used for admission. An independent residual
sharp clock/extremal conjunction is absent. Old IAV uses fixed cyclic
neighbours and floor averaging, so it is not falsely called this
literal rule; the shared quantized-consensus primitive is still deducted.

## 2. OLS — common compression potential and full row-choice adapter

### Exact claim and proof

For all $a,b\geq0$, all recurrent states are exactly subsets
compressed along both prescribed line families. A state of
cardinality $k$ has tail at most $k(M-k)$, where
$M=(2a+1)(2b+1)$. Every fibre has the formula below.

**Step 1 — rank potential.** Rank all ambient points from $0$ to
$M-1$ by the common strict order $(x^2+y^2,x,y)$. Set
$\Phi(S)=\sum_{p\in S}\operatorname{rank}(p)$. On a line containing
$r$ occupied points, the unique minimum rank sum among its $r$-subsets
is the first $r$ points in that same order. Thus each line compression
preserves cardinality and decreases $\Phi$ strictly unless it changes
nothing. Distinct lines within a family partition the ambient set,
so these statements add over a compression stage.

**Step 2 — full update and clock.** If either stage changes its
input, the full update strictly lowers $\Phi$; the other stage cannot
increase it. Equality across a full update forces both stages to be
stationary, so the source is compressed in both directions. A finite
orbit cannot make strict decreases forever and has no nontrivial
cycle. For fixed cardinality $k$, the least possible rank sum is
$k(k-1)/2$ and the greatest is $k(2M-k-1)/2$. Their difference is
$k(M-k)$, and each nonfixed update lowers an integer by at least one.
This proves the bound, including $k=0,M$.

**Step 3 — inverse as row counts and choices.** Let horizontal lines
be $H_1,\ldots,H_r$ and diagonals be $D_1,\ldots,D_s$, with each
listed in the common priority order. For row counts
$u_i\in\{0,\ldots,|H_i|\}$ write
$A(u)=\bigcup_i\operatorname{prefix}_{u_i}(H_i)$ and
$v_j(u)=|A(u)\cap D_j|$. If target $Y$ is not compressed on every
diagonal, its fibre is empty. Otherwise put $v_j=|Y\cap D_j|$; then

$$
|F^{-1}(Y)|=
\sum_{u:v(u)=v}\prod_{i=1}^r\binom{|H_i|}{u_i}.
$$

For a fixed $u$, choosing an arbitrary $u_i$-subset independently
on each horizontal line determines a unique source. All those
sources first become $A(u)$, whose second compression is completely
determined by $v(u)$. A diagonally compressed target with those counts
is unique. Different source row-count vectors are disjoint cases,
which proves necessity, sufficiency and multiplicity in the formula.

### Deduction and open risks

The argument holds for any two partitions of a finite totally ordered
set; Euclidean lines are only one instance. Thus the entire proved
time statement and the entire source-fibre reconstruction are
deducted as a generic compression/occupancy adapter. No sharp
all-grid clock or evaluated uniform extremal residual was obtained.
Continuous Steiner symmetrization sources are neighbours, not a
licence to apply convex-body limit theorems to these finite subsets.

## 3. MER — nonfixedness is not a temporal classification

### Exact claim and proof

On every nonempty finite pixel grid, $F(S)\cap S=\varnothing$,
$F(S)=\varnothing$ holds precisely for the full source, and there
are no fixed states.

**Step 1 — existence and enumeration.** Every proper source misses
some pixel; its singleton rectangle is empty. A finite inclusion
poset of empty rectangles has a maximal rectangle above it. A
rectangle is maximal exactly when none of its legal one-side
one-pixel expansions is empty: if a strictly larger containing
rectangle is empty, at least one such immediate expansion lies
inside it and is also empty. This justifies the pilot's maximality
test without omitting rectangles.

**Step 2 — centres and fixed points.** Nearest lattice pixels to a
rectangle's Euclidean midpoint lie inside that rectangle (choose
floor or ceiling independently in both coordinates). They are
therefore outside $S$. The full source has no empty rectangle and
maps to empty; a proper source has at least one maximal rectangle
and at least one output centre. Finally $F(S)=S$ and disjointness
would force $S=\varnothing$, but the empty source outputs the
nonempty centre set of the full grid. Hence there are no fixed states.

### Missing claim and explicit boundary

The original $3\times3$ full carrier has genuine four-cycles; an
explicit ordered witness is recorded in [the deduction canonical](PROOF_CANONICAL.json).
Thus an all-grid “period at most two” claim is false. Disjoint
successive sets do not even prove that all periods are even. A list
of maximal empty rectangles reconstructs the empty background by
union, but the centre-only list discards rectangle sizes and that
full-rectangle inverse cannot be transferred without proof. No
all-grid core/clock theorem or evaluated centre-set fibre formula
was obtained. `NO_PROMOTION / INCOMPLETE_CONJUNCTION`.

## 4. NTL — sharp one-dimensional erosion, not a two-dimensional atlas

### Exact claim and proof

For every finite grid the only fixed state is empty. On the line
$X=\{0,\ldots,N-1\}$ every orbit reaches empty and the maximum
tail is $\lceil N/2\rceil$.

**Step 1 — fixed states.** Each occupied point has itself as its
unique distance-zero nearest site, so $F(S)\cap S=\varnothing$.
Empty maps to empty. A fixed state is disjoint from itself and thus
must be empty.

**Step 2 — exact line rule.** Write a nonempty source in increasing
order $s_1<\cdots<s_k$. A tie between two nearest sites on a line
can only occur between consecutive sites, at their midpoint. A site
strictly between a putative tied pair would be closer to that
midpoint and exclude that pair. Conversely the midpoint of a
consecutive pair has no closer source site. The midpoint is an
ambient integer exactly when the gap is even. Therefore

$$
F(S)=\{(s_i+s_{i+1})/2:1\leq i<k,\ s_{i+1}-s_i\text{ even}\}.
$$

Each nonempty image has minimum at least $\min S+1$ and maximum
at most $\max S-1$. Also $|F(S)|\leq |S|-1$; singleton sources
map to empty.

**Step 3 — upper bound and equality.** If the initial diameter is
$d=\max S-\min S$, after $t$ updates a nonempty state has diameter
at most $d-2t$. At time $\lfloor d/2\rfloor$, any surviving
state has diameter at most one. Such a state is a singleton or
two adjacent sites and its next image is empty by the midpoint
rule. This gives
$h(S)\leq\lfloor d/2\rfloor+1\leq\lceil N/2\rceil$.
For equality choose $S=\{0,2,\ldots,2r\}$ with
$r=\lfloor(N-1)/2\rfloor$. At time $t\leq r$ the exact midpoint
rule gives $\{t,t+2,\ldots,2r-t\}$; the next update after the
singleton at time $r$ is empty. Its tail is $r+1=\lceil N/2\rceil$.
For $N=1$ this is the singleton-to-empty orbit. Empty has tail zero.

### Deduction and open risks

This sharp line clock is completely boundary erosion and receives
zero independent value credit. It cannot prove global nilpotence:
on the original $2\times2$ grid the two diagonal pairs alternate
(row-major masks $9\leftrightarrow6$). General two-dimensional
recurrent structure, sharp tail and independently evaluated fibres
remain unproved. `NO_PROMOTION / INCOMPLETE_CONJUNCTION`.

## 5. NSV — translation cores and complement-paired fibres

### Exact claim and proof

The full rule obeys $F(X\setminus S)=F(S)$, so every nonempty fibre
has even size. On every $g\times g$ torus with $g\geq3$ there are
states of exact period $g$ as well as the fixed stripes below.

**Step 1 — complement pairing.** Complementing all four bits of a
checkerboard gives a checkerboard; complementing a noncheckerboard
does not give one. Thus the output is unchanged at each vertex.
No subset of a nonempty ambient set equals its complement. Each
source in a fibre pairs with a distinct complementary source.

**Step 2 — moving diagonal stripes.** For residues modulo $g$, put
$S_t=\{(i,j):i+j=t\pmod g\}$. At a vertex with $i+j=k$, the
four incident faces have residues $k,k-1,k-1,k-2$. The middle
diagonal pair is occupied and the other pair absent exactly when
$k-1=t$. The other diagonal cannot have both faces occupied since
$k$ and $k-2$ differ for $g\geq3$. Hence $F(S_t)=S_{t+1}$.
The $g$ stripe sets are distinct, proving exact period $g$.

**Step 3 — fixed opposite stripes.** Let
$D_t=\{(i,j):i-j=t\pmod g\}$. The incident residues are now
$k,k-1,k+1,k$. If $k=t$, exactly the first and last face are
occupied. If $k\ne t$, the other diagonal cannot both be occupied
because $k-1\ne k+1$ for $g\geq3$. Thus $F(D_t)=D_t$.

### Deduction and open risks

These are ordinary translation-action cores and a local
complement symmetry, not a full all-torus orbit classification.
The moving stripes forbid any universal period bound independent
of torus size. A prescribed output merely gives coupled local
plaquette constraints; no independent evaluated inverse count or
sharp full-carrier temporal theorem has been proved.
The checkerboard cubical singularity test is itself classical.
`NO_PROMOTION / INCOMPLETE_CONJUNCTION`.

## 6. LVC — exact nonsmooth DCA and ordered-cell inverse

### Exact claim and proof

For every declared $N,m$, all recurrent states are fixed. Every
target fibre is exactly the bounded integer difference-constraint
set below. These conclusions do not provide a new sharp clock or
an evaluated arbitrary-parameter maximum-fibre formula.

**Step 1 — subgradient representation.** Let
$c_{qi}=(q-i)^2$ and define, on all of $\mathbb R^m$,

$$
G(w)=\sum_{q=0}^{N-1}\max_{0\leq i<m}(w_i-c_{qi}),
\qquad \Phi(w)=G(w)-\tfrac12\|w\|^2.
$$

For each $q$, choose the maximizing index by the prescribed least
index tie rule. Its unit coordinate vector is a subgradient of
that maximum: the selected affine function equals the maximum
at $w$ and is at most the maximum at every other point. Adding
these supporting inequalities proves $F(w)\in\partial G(w)$,
because $F(w)$ counts the selected indices.

**Step 2 — strict increase and the full temporal adapter.** Put
$v=F(w)$. The supporting inequality gives
$G(v)-G(w)\geq v\cdot(v-w)$. Subtracting the quadratic difference
and expanding yields

$$
\Phi(F(w))-\Phi(w)\geq\tfrac12\|F(w)-w\|^2.
$$

The finite integer carrier is invariant, and every nonfixed step
strictly increases $\Phi$. Therefore all orbits eventually become
fixed. More strongly, this is literally simplified DCA for
$g(w)-h(w)$ with $g(w)=\|w\|^2/2$ and $h(w)=G(w)$:
choose $y=F(w)\in\partial h(w)$ and update
$w'=\nabla g^*(y)=y$. The quadratic minimizer is unique and
already lies in the original integer carrier. Both components
are finite proper convex functions, and $g-h$ is bounded below
because the quadratic dominates the finite maximum of affine
functions. The selected-subgradient algorithm and strict-descent
interface are treated by Pham Dinh Tao–Le Thi Hoai An (1997),
§§3.1–3.2; the exact nonsmooth specialization is proved here.
No differentiability of $G$ is assumed. Thus the full temporal
argument is deducted as the DCA adapter, not credited as a new
geometric convergence theorem.

**Step 3 — monotone assignment.** For $i<j$,
$c_{qi}-c_{qj}=2q(j-i)+i^2-j^2$ is strictly increasing in $q$.
Suppose $q_1<q_2$ but $q_1$ selects $j$ and $q_2$ selects $i$.
The first selection implies
$w_i-w_j<c_{q_1i}-c_{q_1j}$, since equality would select the
smaller index $i$. The second implies
$w_i-w_j\geq c_{q_2i}-c_{q_2j}$, a contradiction. Hence the
selected site indices are nondecreasing along the line.

**Step 4 — complete target chamber.** A target $v$ can only have
nonnegative entries summing to $N$. For such $v$ there is exactly
one possible nondecreasing assignment: the first $v_0$ demands
go to site $0$, the next $v_1$ to site $1$, and so on. Write
$Q_i(v)$ for the resulting (possibly empty) demand block. If
$Q_i(v)\ne\varnothing$, define for each $j\ne i$

$$
B_{ij}(v)=\max_{q\in Q_i(v)}
\left(c_{qi}-c_{qj}+\mathbf1_{j<i}\right).
$$

Then

$$
F^{-1}(v)=\{w\in\{0,\ldots,N\}^m:
w_i-w_j\geq B_{ij}(v)
\text{ for all active }i\text{ and all }j\ne i\}.
$$

Necessity follows by comparing the chosen site's score with every
competitor. Strict superiority over a smaller-index competitor
becomes the extra integer $1$. Conversely these inequalities
force precisely the unique block assignment, including all tie
choices, and hence the target volumes. The affine cost difference
attains its maximum at an endpoint of the block, so two endpoints
suffice to compute each bound. An empty block contributes no
own inequalities, but that site remains a competitor in other
blocks. Invalid total volume gives an empty fibre.

**Step 5 — translation multiplicity.** Adding the same constant
to every weight leaves all score comparisons unchanged. Every
weight has a unique representation $w=u+t\mathbf1$ with
$\min_i u_i=0$ and $0\leq t\leq N-\max_i u_i$. A normalized
chamber point therefore represents exactly $N-\max_i u_i+1$
sources. This is an ordinary difference-coordinate flat direction,
not an additional theorem axis.

### Deduction and open risks

The inverse is a full static cell-assignment chamber adapter,
not merely “some inverse relation exists.” Its bounded integer
counts were evaluated exhaustively on the original 22 boxes.
No closed all-$N,m$ chamber-volume extremum or equality-class
classification was derived. The entire time argument already
transfers from DCA. `NO_PROMOTION / DCA_AND_STATIC_CHAMBER`.

## Verification and final boundary

[pilot.py](pilot.py) is the unchanged initial six-rule forward census.
[proof_checks.py](proof_checks.py) imports those literal forward maps
and independently implements the histogram, row-choice and chamber
descriptions as an **author** deduction audit. It verifies every
target in the corresponding original full carriers; it is not
process-independent review. The two actual fresh replay pairs and
raw canonical comparisons are documented in
[SOURCE_AND_REPLAY](SOURCE_AND_REPLAY.md). No proof here claims an
all-parameter result merely because its bounded checks passed.

No manuscript was written, no candidate gate was passed, no reserve
was retained and no paper number was assigned. All external release
remains held. The six negative systems remain archived as evidence.
