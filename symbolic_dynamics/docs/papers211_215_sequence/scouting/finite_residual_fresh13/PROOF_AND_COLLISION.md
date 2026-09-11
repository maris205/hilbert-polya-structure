# fresh13: exact old-control certificate, not a fresh theorem nomination

## Claim and status

The research target is a genuinely different finite autonomous map with a
rigid all-parameter temporal theorem and a materially separate residual
inverse or enumeration theorem after the recorded historical subtraction.
Status of that target in this desk: **NOT CURRENTLY JUSTIFIED**.

The elementary statements below are **PROVABLE AS STATED**. They concern
already-defined controls. No new carrier/update entrance is being admitted
or counted. In particular an ambient-group restriction of old G01 is not
renamed a fresh system.

## Assumptions and notation

Let $E$ be a finite set of size $n\ge0$. Families are arbitrary subsets of
$2^E$, including the empty family and families containing the empty set.
Write $\min\mathcal H$ for the inclusion-minimal members of $\mathcal H$,
and $\uparrow\mathcal K=\{S\subseteq E:\exists K\in\mathcal K,\ K\subseteq S\}$.
A clutter is an inclusion antichain, including both $\varnothing$ and
$\{\varnothing\}$. Define $b(\mathcal H)$ to consist of the
inclusion-minimal sets meeting every member of $\mathcal H$.

For a group $G$, write $Z(G)$ for its center, $[G,G]$ for its commutator
subgroup, $\operatorname{Sub}(G)$ for its subgroups and
$N_G(H)=\{g\in G:gHg^{-1}=H\}$. All groups considered as dynamical carriers
are finite. "Class at most two" means $[G,G]\subseteq Z(G)$, including
abelian groups.

The blocker rule is exactly old HBN and D3. The normalizer rule on every
finite $G$ is exactly old G01. These identifications are by the displayed
carrier and update, not by shared terminology.

## Strategy and dependency map

1. Finite minimal-element selection identifies blocker fibres with minimal
   cores; complement separation proves the double-blocker identity.
2. First-image and involution arguments give the complete recurrent locus.
3. Redundant supersets are independent optional members, giving the
   one-step fibre and its maximum. This is the existing D3 proof mechanism.
4. Central containment makes a subgroup of a class-two group normal;
   applied to its normalizer, this supplies a short old-G01 specialization.
   It does not classify all normalizer fibres or all finite group towers.

## 1. The entire blocker result is already old D3

Step 1. A set $S$ meets every member of $\mathcal H$ if and only if it meets
every member of $\mathcal K=\min\mathcal H$. One direction follows from
$\mathcal K\subseteq\mathcal H$. For the other, each $H\in\mathcal H$
contains a minimal member: repeatedly choose a proper contained member
while possible, which terminates because the family is finite. Hence
$b(\mathcal H)=b(\mathcal K)$.

Step 2. For every clutter $\mathcal K$ and every $S\subseteq E$,
$$
S\text{ meets every member of }b(\mathcal K)
\quad\Longleftrightarrow\quad S\in\uparrow\mathcal K.
$$
If $K\in\mathcal K$ lies in $S$, every transversal meets $K$ and therefore
meets $S$. Conversely, suppose no $K\in\mathcal K$ lies in $S$.
Then $E\setminus S$ meets each $K$ and contains a minimal transversal by
finite descending selection. That transversal is disjoint from $S$, so
the left condition fails. This argument also treats $\mathcal K=\varnothing$:
the chosen minimal transversal is then $\varnothing$. When
$\mathcal K=\{\varnothing\}$ the left condition is vacuous and both sides
hold for every $S$.

Taking minimal members in the equivalence proves $b^2(\mathcal K)=\mathcal K$.
Consequently, for every family,
$$
b^2(\mathcal H)=\min\mathcal H,\qquad b^3(\mathcal H)=b(\mathcal H).
$$
The definition itself yields $b(\varnothing)=\{\varnothing\}$ and
$b(\{\varnothing\})=\varnothing$; no undefined "minimum of an empty
collection" of numbers is used.

Step 3. Every output is a clutter, and every clutter lies in the image
because $\mathcal C=b(b(\mathcal C))$. Thus both the image and the
recurrent set are exactly the clutters. A clutter is fixed when
$b(\mathcal C)=\mathcal C$ and otherwise has least period two.
A nonclutter cannot be recurrent and reaches a clutter in one step.
Hence its entry time is exactly one. At $n=0$ both families are clutters;
at $n\ge1$ the family $\{\varnothing,\{e\}\}$ is a nonclutter for any
$e\in E$. The sharp maximum entry time is respectively zero and one.

Step 4. A nonclutter target has no predecessor. For a clutter target
$\mathcal C$, put $\mathcal K=b(\mathcal C)$. Then
$$
b(\mathcal H)=\mathcal C
\Longleftrightarrow \min\mathcal H=\mathcal K
\Longleftrightarrow \mathcal K\subseteq\mathcal H\subseteq\uparrow\mathcal K.
$$
For the first equivalence apply $b$ and the double-blocker identity in one
direction, and use Step 1 and $b(\mathcal K)=\mathcal C$ in the other.
For the second, every minimal member must be included and every other
member must contain one. Conversely, the containments force every added
member to contain a member of $\mathcal K$; antichainhood prevents any
member of $\mathcal K$ from being displaced as a minimum.
There are therefore exactly
$$
|b^{-1}(\mathcal C)|
=2^{|\uparrow b(\mathcal C)|-|b(\mathcal C)|}
$$
predecessors, obtained by independently selecting the redundant supersets.

Step 5. For $n\ge1$, the target $\mathcal C=\varnothing$ has
$\mathcal K=\{\varnothing\}$ and fibre $2^{2^n-1}$. If
$\mathcal K=\varnothing$ the exponent is zero. Every other nonempty
$\mathcal K$ omits $\varnothing$, its upward closure omits $\varnothing$,
and its exponent is at most $(2^n-1)-1=2^n-2$. Thus the empty target
is the unique maximum. For $n=0$, the two families form a two-cycle and
both target fibres have size one.

All five steps reproduce the directly read old D3, Section 3. The original
Edmonds--Fulkerson article owns the blocker definition and clutter
double-blocker theorem; the optional-superset fibre and sharp maximum are
already explicit in D3, not newly attributed to the article. A present
self-contained proof does not confer a new research axis.

## 2. Class-two normalizers do not form a new entrance

Consider the existing G01 map $T(H)=N_G(H)$ on $\operatorname{Sub}(G)$,
with the additional assumption $[G,G]\subseteq Z(G)$.

Step 1. Every central element normalizes every subgroup, so
$Z(G)\subseteq N_G(H)$.

Step 2. Any subgroup $K$ containing $Z(G)$ is normal in $G$. Indeed, for
$g\in G$ and $k\in K$, the element $gkg^{-1}k^{-1}$ is a commutator,
hence lies in $Z(G)\subseteq K$. It follows that $gkg^{-1}\in K$.
This gives $gKg^{-1}\subseteq K$; applying it to $g^{-1}$ gives the reverse
containment.

Step 3. Apply Step 2 to $K=N_G(H)$. Then
$$
T^2(H)=N_G(N_G(H))=G
$$
for every $H$. The sole fixed point is $G$: if $T(H)=H$, then
$H=T^2(H)=G$. The pointwise entry time is zero for $H=G$, one for a
proper normal subgroup, and two for a nonnormal subgroup. The last case
follows because $T(H)\ne G$ by nonnormality, whereas $T^2(H)=G$.

The maximum is zero for the trivial group, one for a nontrivial group
all of whose subgroups are normal, and two otherwise. Class two alone
does not guarantee a nonnormal subgroup; no such claim is made.

This elementary statement has no new literal carrier: the old G01 family
already quantifies over all finite groups. It does not yield a complete
all-target inverse or an independently valuable fibre/extremal residual.
No extraspecial, exponent, field-size or dimension family is separately
fixed as a candidate, and no subgroup enumeration is executed.

Importantly, this is not a theorem that every use of a normalizer map is
below value threshold. Existing P154 explicitly goes beyond its source-owned
dihedral one-step rule by a full inverse-forest and unlabelled-signature
analysis. That historical retained result is preserved, not overturned by
the short class-two observation.

## 3. Exact incidence adapter, not a new geometry rule

The original D4 supplies the following already-used identity. For a finite
incidence relation $I\subseteq X\times Y$, define
$A'=\{y\in Y:\forall a\in A,\ (a,y)\in I\}$ and
$B'=\{x\in X:\forall b\in B,\ (x,b)\in I\}$.
The old update is $T(A,B)=(B',A')$.

Form the bipartite graph on disjoint tagged copies of $X$ and $Y$ whose
cross edges are exactly the nonincidences. The bijection
$h(A,B)=A\sqcup B$ sends a pair to a vertex subset. At a vertex $x\in X$,
having no selected neighbor is equivalent to incidence with every element
of $B$, and the corresponding calculation on $Y$ gives $A'$.
Therefore the graph NOR map $F$ satisfies
$$
F\circ h=h\circ T.
$$
This is a full-carrier conjugacy, including empty sides, not a quotient
or an assertion that arbitrary geometric local moves are polarity maps.
D4 already relates it to P106. The entire D4 adapter, including its static
inverse inclusion-exclusion, was read; no fresh incidence map is offered.

## Corrections, open risks and disposition

No new scientific claim is supported by a pilot, review or experimental
transcript. These deductions require only the stated finite definitions;
there is no gap hidden behind untested examples.

The broader nomination target remains unproved in this bounded screen.
This certificate does not prove that all finite geometry, nonlinear
algebra, resource dynamics, nonabelian groups or incidence maps are
exhausted. It does not establish novelty, priority or external ownership
clearance for any potential later proposal.

Disposition: **ZERO_NEW_LITERAL / NO_NOMINATION / NO_PILOT**.
