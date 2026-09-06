# LUB proof and disposition

2026-09-05 UTC. Proof contributor: batch197_fifth_scout.
Disposition: **NO_PROMOTION / COMPLETE_STATIC_INVERSE_ADAPTER**.
No paper number or reserve is assigned.

## Claim

The requested all-parameter temporal/recurrent theorem plus an independent
inverse/geometry theorem has not been established. The corrected, weaker
claim proved here keeps the original full carrier and all positive lengths:

1. Every output of LUB is exactly a fixed point of the sublevel-component
   area operator, and conversely every such fixed point is an output.
2. LUB's output recovers the entire original upper-component tree,
   including its vertex supports, not merely a list of subtree sizes.
3. Every one-step fibre is in explicit bijection with strict height
   labellings of that fixed rooted tree. Its size is exactly the classical
   rooted-tree strict order polynomial evaluated at the original alphabet
   size.
4. Adjacent equalities are preserved and adjacent strict inequalities
   reverse. Consequently the sole fixed point is the constant word with
   value equal to the length.

The inverse result is a complete old-mechanism adapter and gets zero
independent contribution credit. No universal period-two or sharp-height
statement is asserted.

## Status

**PROVABLE AFTER WEAKENING.** The four statements above are proved for
every original length. The requested two-axis research claim remains
unjustified; finite periods and heights do not fill that gap. There is no
extra assumption and no restricted replacement carrier.

## Assumptions and notation

Fix $n\ge1$ and the labelled cycle on $V=\mathbb Z/n\mathbb Z$ (the usual
connected one-vertex/two-vertex degeneracies are included). A word is
$x\in[n]^V$. Let $C_x^+(i)$ be the connected component containing $i$ in
the induced graph on $\{j:x_j\ge x_i\}$; let $C_x^-(i)$ use
$\{j:x_j\le x_i\}$. Define
$$
 F(x)_i=|C_x^+(i)|,\qquad L(x)_i=|C_x^-(i)|,\qquad
 (Jx)_i=n+1-x_i.
$$
Thus $F$ is exactly root's LUB, $L$ is an auxiliary operator and
$F=LJ$. All global minima of $x$ have output $n$. Strictly smaller values,
not weakly smaller ones, stop an upper component.

For a rooted tree $T$, orient the ancestry order from its root to its
descendants. Write $\bar\Omega_T(m)$ for the number of maps
$h:T\to[m]$ with $h(v)<h(w)$ whenever $w$ is a proper descendant of $v$.

## Proof strategy and dependency map

1. Nested threshold components and their boundary vertices recover an old
   upper component as a new lower component.
2. The same argument for lower components proves $L^2=L$; complementation
   supplies the reverse image inclusion.
3. The complete recovered component family determines its inclusion tree
   and nonempty node atoms. Strict height labellings reconstruct all and
   only the original words.
4. Adjacent component containment proves the fixed-state statement.
5. An optional static counting corollary follows by decomposing linear
   gaps between root atoms; it carries no dynamical or separate novelty
   credit.

No finite computation is a premise of these deductions.

## Proof

### Step 1. Component supports survive exactly

Put $y=F(x)$ and fix $i$. Let $C=C_x^+(i)$ and $s=|C|=y_i$.
For each $j\in C$, its threshold satisfies $x_j\ge x_i$, so every path
above $x_j$ is also above $x_i$. Hence $C_x^+(j)\subseteq C$ and
$y_j\le s$.

If $k\notin C$ is adjacent to a vertex of $C$, then $x_k<x_i$;
otherwise it would join $C$ at threshold $x_i$. At threshold $x_k$ the
entire connected set $C\cup\{k\}$ is present. Therefore
$C\cup\{k\}\subseteq C_x^+(k)$ and $y_k>s$.

The set $C$ is connected, contains $i$, lies inside $\{j:y_j\le y_i\}$,
and every external neighbour has larger $y$-value. It is consequently
exactly the lower component of $y$ at $i$:
$$
 C_{F(x)}^-(i)=C_x^+(i).
 \tag{1}
$$
This also covers $C=V$, when there is no external neighbour. Taking
cardinalities gives $L(F(x))=F(x)$.

Apply the same containment-and-boundary argument to a lower component
$C_x^-(i)$: vertices inside it have lower-component sizes at most its
size, while an external neighbour has a larger original value and its
lower component properly contains it. Hence
$$
 C_{L(x)}^-(i)=C_x^-(i),\qquad L^2=L.
 \tag{2}
$$
The two statements do not imply $F^2=F$ or $F^3=F$.

### Step 2. Exact first image

Equation (1) proves $\operatorname{im}F\subseteq\operatorname{Fix}L$.
If $L(y)=y$, then $F(Jy)=L(y)=y$, because reversing all values turns
upper into lower thresholds without changing the cycle. Thus
$$
 \operatorname{im}F=\operatorname{Fix}L,\qquad
 y\in\operatorname{im}F\Longrightarrow J(y)\in F^{-1}(y).
 \tag{3}
$$
This is a complete membership test and a source witness, not a second
image or recurrent-set description.

### Step 3. Build the exact target tree and atoms

For an image target $y$, let
$$
 \mathcal T_y=\{C_y^-(i):i\in V\},
$$
with duplicates removed. Threshold components either are disjoint or one
contains the other. The full set $V$ occurs and is the unique root.
Every nonroot component has a unique smallest strict superset in this
finite laminar family; it is its parent. The children of a node $C$ are
its maximal proper subcomponents.

Define its atom
$$
 A_C=C\setminus\bigcup_{\substack{D\text{ child}\\\text{of }C}}D.
$$
To identify it, choose $i$ such that $C=C_y^-(i)$ and write $s=y_i$.
Since $L(y)=y$, $s=|C|$. Every $j\in C$ has $y_j\le s$.
Those with $y_j<s$ lie in proper lower components inside $C$ and hence
in a maximal proper one; those with $y_j=s$ have lower component $C$
and lie in no proper subcomponent. Consequently
$$
 A_C=\{j\in C:y_j=|C|\}\ne\varnothing.
 \tag{4}
$$
The atoms partition $V$.

By (1), any source $x$ with $F(x)=y$ has upper-component family exactly
$\mathcal T_y$, with these same geometric supports. There is no unknown
Cartesian tree left to sum over after the target is given.

### Step 4. Full inverse bijection, necessity

In an upper-component tree, the atom of a component consists precisely
of its minimum-valued vertices. Removing these minimum vertices leaves
the maximal proper upper components as the connected pieces. This
description follows by raising the threshold above the component
minimum: every remaining vertex lies in some maximal proper upper
component, and an atom vertex cannot lie in any component with higher
minimum.

It follows that a source $x$ is constant on $A_C$, with common value
$h(C)$, and that
$$
 h(C)<h(D)\quad\text{for each child }D\text{ of }C.
 \tag{5}
$$
All these values lie in $[n]$. Thus each source determines one strict
height labelling $h:\mathcal T_y\to[n]$.

### Step 5. Full inverse bijection, sufficiency

Conversely, choose any labelling satisfying (5) and put
$x_i=h(C)$ for the unique atom $A_C$ containing $i$.

Every vertex of a node $C$ belongs to its own atom or a descendant atom,
so all of $C$ has $x$-value at least $h(C)$. The set $C$ is connected.
If $k\notin C$ is adjacent to $C$, its old target value satisfies
$y_k>|C|$, by the definition of the lower component $C$ of $y$.
The lower component $D=C_y^-(k)$ contains $C\cup\{k\}$: all of $C$
has $y$-value at most $|C|<y_k$. By (4), $k\in A_D$, and $D$ is a
proper ancestor of $C$. Hence $x_k=h(D)<h(C)$.

Therefore for every $i\in A_C$ the upper component of the reconstructed
word at $i$ is exactly $C$. Its output is $|C|=y_i$. This proves
$F(x)=y$. Reconstruction and extraction of atom heights are inverse
operations, giving the exact formula
$$
 |F^{-1}(y)|=
 \begin{cases}
  \bar\Omega_{\mathcal T_y}(n),&L(y)=y,\\
  0,&L(y)\ne y.
 \end{cases}
 \tag{6}
$$
Atom cardinalities affect the recovered geometric tree but do not add
independent colour choices: a whole atom has one height. Sibling
heights may agree. Only ancestor inequalities are strict.

If a tree root has child trees $T_1,\ldots,T_r$, splitting by its height
$a$ gives
$$
 \bar\Omega_T(m)=
 \sum_{a=1}^{m}\prod_{j=1}^{r}\bar\Omega_{T_j}(m-a).
 \tag{7}
$$
For a leaf this is $m$; a nonempty tree has value zero at $m=0$.
Equation (7) is exactly the classical strict order-polynomial recursion.
The source report identifies a primary source that explicitly proves
its finite-difference form.

Thus the adapter is not merely an analogy between LUB and trees. It
specifies the uniquely decoded tree, all geometric atoms, every source,
the exact counting substitution, and all tie/boundary conventions.

### Step 6. Adjacent signs and the unique fixed point

If adjacent vertices satisfy $x_i=x_j$, their upper components at that
level coincide, so $F(x)_i=F(x)_j$. If $x_i<x_j$, the component at $j$
is contained in that at $i$, and the latter also contains $i$, which is
not above threshold $x_j$. Containment is strict, so $F(x)_i>F(x)_j$.
The case $x_i>x_j$ reverses this relation.

A fixed word cannot have unequal adjacent values. The cycle is connected,
so it must be constant. Every constant word maps to $(n,\ldots,n)$,
which is itself fixed. Hence this is the unique fixed point for all
$n\ge1$. This does not preclude two-cycles or longer cycles.

### Step 7. Optional static first-image census

This corollary is included to close the observed image sequence, not as
an independent dynamical contribution. Let $a_m$ count the analogous
lower-area fixed arrays on a line of $m$ positions, with $a_0=1$. This
line is only a counting device for gaps in the original cycle, not a
new research carrier.

For a nonempty line array the maximum is $m$. Its nonempty set of
maximum positions, say $k$ positions, cuts it into $k+1$ gaps. Each gap
is an independent lower-area fixed array of its own length: every
sublevel component below $m$ is confined to that gap. Conversely these
gap arrays and maximum positions reconstruct the line array.
For $A(z)=\sum_{m\ge0}a_mz^m$ this proves
$$
 A(z)=1+\sum_{k\ge1}z^kA(z)^{k+1}
     =1+\frac{zA(z)^2}{1-zA(z)},
 \qquad
 A(z)=\frac{1+z-\sqrt{1-6z+z^2}}{4z}.
 \tag{8}
$$

Let $b_n=|\operatorname{im}F|$. In a cycle image the maximum is $n$.
For exactly $k$ maximum positions, mark one of them. There are $n$
choices for its labelled location and the ordered cyclic gaps contribute
$[z^{n-k}]A(z)^k$. Each unmarked array is counted $k$ times. Thus
$$
 b_n=\sum_{k=1}^{n}\frac nk[z^{n-k}]A(z)^k
     =n[z^n]\bigl[-\log(1-zA(z))\bigr].
 \tag{9}
$$
Differentiating (8)'s explicit expression yields
$$
 \sum_{n\ge1}b_nz^n=\frac{z}{\sqrt{1-6z+z^2}}.
 \tag{10}
$$
These are the central Delannoy numbers shifted by one index. For an
explicit algebraic coefficient check, the binomial-sum generating
function
$$
 \sum_{m\ge0}\sum_{k=0}^{m}
 \binom{m}{k}\binom{m+k}{k}z^m
 =
 \frac1{1-z}
 \sum_{k\ge0}\binom{2k}{k}
       \left(\frac z{(1-z)^2}\right)^k
 =\frac1{\sqrt{1-6z+z^2}}
$$
uses $\binom m k\binom{m+k}k=\binom{2k}k\binom{m+k}{2k}$.
This gives
$$
 b_n=\sum_{k=0}^{n-1}\binom{n-1}{k}\binom{n-1+k}{k}.
 \tag{11}
$$
The classical rooted-component decomposition and arithmetic are fully
subtracted. Equations (8)–(11) say nothing about which image states recur.

## Corrections and failed proof direction

The two-step coordinate comparison is false in both directions, already
within the original pilot bounds:
$$
 (1,3,2,3)\mapsto(4,1,3,1)\mapsto(1,4,1,4)\mapsto(4,1,4,1),
$$
so $F^3(x)\nleq F(x)$. Also
$$
 (1,1,2,1,2)\mapsto(5,5,1,5,1)
 \mapsto(2,2,5,1,5)\mapsto(4,4,1,5,1),
$$
so $F^3(x)\ngeq F(x)$. These are preserved counterexamples to an
exploratory route, not counterexamples to the still-unproved universal
period-two signal.

The finite graph has recurrent-state counts
$1,3,13,59,261,1107$ and heights $0,1,1,2,2,3$ for $n=1,\ldots,6$.
First-image counts are instead $1,3,13,63,321,1683$; image and core
must not be conflated.

## Open risks and closure

No all-parameter recurrent atlas, period bound, sharp clock or uniform
maximum-fibre/equality theorem was completed. The scalar output is the
old upper-component area encoding and its complete inverse is (6).
A future stronger temporal result might still exist, but it would not
restore a materially independent inverse axis by relabelling this same
static tree count.

Accordingly the candidate is closed NO_PROMOTION at the unchanged
$n\le6$ pressure boundary. The original carrier was not restricted,
root's files were not edited, and no manuscript review or independent
candidate gate is claimed. This author would be ineligible to review a
paper using these deductions.
