# R6-C2 — Exact tame stabilizer of one frozen nine-point lattice set

2026-09-09 UTC. Coordinator-authorized follow-up to the still unresolved full native integer spectrum question. This is a **construction mechanism**, not a replacement theorem, a new period convention, or a claimed ninth-period witness. Work here is hand-only unless the coordinator separately reviews and releases a precise new diagnostic. No R5 file is modified.

## 1. Frozen set, labels, maps and target

Work over $\mathbb Z^2$. Freeze the following ordered nine-point set $C$; these labels remain fixed in all permutations below.

| Label | Point | $A$ image label | $I$ image label |
| --- | --- | --- | --- |
| 1 | $(0,0)$ | 2 | 5 |
| 2 | $(1,0)$ | 3 | 2 |
| 3 | $(1,1)$ | 1 | 8 |
| 4 | $(3,1)$ | 5 | 4 |
| 5 | $(0,2)$ | 6 | 1 |
| 6 | $(-1,-2)$ | 4 | 7 |
| 7 | $(-1,0)$ | 8 | 6 |
| 8 | $(1,-1)$ | 9 | 3 |
| 9 | $(2,2)$ | 7 | 9 |

The exact polynomial maps are

$$
A(x,y)=(1-y,x-y),\qquad
I(x,y)=(x,q(x)-y),
$$

where

$$
q(t)=-t^4+4t^3-2t^2-3t+2\in\mathbb Z[t].
$$

Both maps are integral tame automorphisms: $A$ is affine with determinant one, and $I$ is a vertical integral shear composed with $(x,y)\mapsto(x,-y)$. Direct calculation gives

$$
A^2(x,y)=(1-x+y,1-x),\quad A^3=\operatorname{id},\quad I^2=\operatorname{id}.
$$

Their restrictions to $C$, with permutation composition acting from right to left, are

$$
a=(1\ 2\ 3)(4\ 5\ 6)(7\ 8\ 9),
\qquad i=(1\ 5)(3\ 8)(6\ 7).
$$

**Exact target.** Find another explicit integral tame automorphism preserving this same $C$, or an explicitly given finite integral tame word, such that the induced subgroup contains a nine-cycle; ultimately exhibit one complete word $T$ and all nine exact transitions of a native least-period-nine orbit. One entire $T$ remains one tick. A set of nine points merely preserved by a group is not a nine-cycle.

If such a word is found, the already proved R5 finite-support padding reduction converts its action on $C$ into a finite word of Hénon factors of degree at least two, preserving the whole native permutation. That reduction is only an interface, not a substitute for first producing the missing nine-cycle. See [the R5 proof supplement](../../continuation_round5/c2_composition_exact_spectrum/PROOF_SUPPLEMENT.md), Sections 1–4. Periods $12,18,24$ would still need their own resolution before the complete spectrum question is settled.

## 2. Direct exact substitution evidence

For $I$, the only required polynomial values are

$$
(q(-1),q(0),q(1),q(2),q(3))=(-2,2,0,4,2).
$$

At $x=-1$, the two heights $-2,0$ are interchanged. At $x=0$, the heights $0,2$ are interchanged. At $x=1$, the heights $-1,0,1$ are reflected about zero. At $x=2$, height $2$ is fixed. At $x=3$, height $1$ is fixed. These observations verify every $I$ transition in the table. The $A$ transitions follow by substituting each displayed point into $(1-y,x-y)$.

For an independent way to recover the integral polynomial, its Newton form on the five consecutive nodes $-1,0,1,2,3$ is

$$
q(t)=-2+4(t+1)-3(t+1)t+2(t+1)t(t-1)
 -(t+1)t(t-1)(t-2).
$$

Expanding this expression gives the frozen quartic above. No interpolating denominator or integer-valued-only polynomial is used.

The horizontal reflection obtained from this set is not a new generator. In fact, with

$$
p(t)=q(t+1)=-t^4+4t^2+t,
\qquad J(x,y)=(p(y)-x,y),
$$

one has the **global identity** $J=A^{-1}IA$: direct substitution gives the first coordinate $q(1-y)+2y-x$, and $q(1-y)+2y=q(y+1)$. Its restriction is

$$
j=(2\ 7)(3\ 4)(5\ 9).
$$

Thus adding $J$ cannot enlarge the currently generated group.

## 3. The current restricted group is exactly $S_3\times C_3$, not a ninth-period witness

The three nonempty residue fibers modulo two are

$$
B_0=\{1,5,9\},\qquad B_1=\{2,6,7\},\qquad B_2=\{3,4,8\},
$$

corresponding respectively to $(0,0),(1,0),(1,1)$. The missing residue class is $(0,1)$. The map $a$ cycles $B_0\to B_1\to B_2\to B_0$. In each fiber use the ordered labels

$$
(\alpha,\beta,\gamma)=(1,5,9),\quad(2,6,7),\quad(3,4,8),
$$

respectively. The map $a$ preserves the internal label when moving to the next fiber, whereas $i$ acts internally by

$$
((\alpha\ \beta),(\beta\ \gamma),(\alpha\ \gamma)).
$$

Put $r=i a i a^{-1}$. Multiplying the displayed finite permutations gives

$$
r=(1\ 9\ 5)(2\ 7\ 6)(3\ 8\ 4).
$$

Consequently

$$
r^3=i^2=a^3=1,\qquad
ara^{-1}=r,\qquad iri=r^{-1},\qquad aia^{-1}=r^{-1}i.
$$

The last identity also follows directly from the definition of $r$. These are assertions about restrictions to $C$, not assertions that the corresponding global polynomial commutator has finite order.

Define $z=ar^2$. Since $a$ commutes with $r$, one has $z^3=1$. Moreover

$$
ziz^{-1}=a r^2 i r^{-2}a^{-1}
=a(ri)a^{-1}=r(r^{-1}i)=i.
$$

Thus $z$ centralizes both $i$ and $r$. The permutations $r,i$ generate exactly a copy of $S_3$: on each fiber they are a three-cycle and an involution conjugating it to its inverse. They act trivially on the set of fibers. In contrast, $z$ induces the same nontrivial three-cycle of fibers as $a$, so $\langle z\rangle\cap\langle r,i\rangle=\{1\}$. As $a=zr$, the original group is exactly

$$
\boxed{\langle a,i\rangle=\langle r,i\rangle\times\langle z\rangle\cong S_3\times C_3.}
$$

Every element has order dividing six. In particular, this group contains no nine-cycle. For example, direct multiplication gives

$$
ia=(1\ 2\ 8\ 9\ 6\ 4)(3\ 5\ 7),
$$

which has a six-cycle and a separate three-cycle, not one nine-cycle.

## 4. Arithmetic compatibility and the genuinely missing step

Modulo two, the set has exactly three fibers of size three, as shown above. Modulo three, its points are all distinct: the listed residue pairs are

$$
(0,0),(1,0),(1,1),(0,1),(0,2),(2,1),(2,0),(1,2),(2,2),
$$

which exhaust $\mathbb F_3^2$. Thus this set does not already violate the two basic residue multiplicity requirements for a hypothetical native nine-cycle. This compatibility is only necessary, not sufficient. In particular, it does not overcome integer interpolation or establish that the full tame stabilizer acts transitively as a cyclic group of order nine.

Any integral tame automorphism preserving $C$ must permute its three modulo-two fibers. Therefore its restriction lies in the imprimitive permutation group $S_3\wr S_3$ of order $(3!)^3\,3!=1296$. This follows solely from congruence preservation and the integral inverse. It does not identify which elements of that finite overgroup lift to integral tame automorphisms preserving the exact points.

The coordinator assigned E2 the complementary **hand-only** problem of classifying single triangular reflections in unimodular affine coordinates that preserve this fixed $C$. A nontrivial such reflection must exchange at least one pair of points along its reflection direction, so the possible primitive directions, up to sign, come from the at most 36 point-pair differences. The report for that complementary task is [E2's direction report](../e2_nine_reflection_directions/REPORT.md). A classification of those reflections will not automatically classify all tame words in the stabilizer.

The present author's task is the broader stabilizer construction mechanism. No new program, expanded coordinate set, coefficient window, external-model API or old checker has been run. No nine-cycle has yet been produced. R5's reviewed period-16 proof and all its frozen report prefixes remain unchanged.

## 5. Hand-only closure of one nonlinear-coordinate bridge

This section tests a precise larger class than affine-coordinate reflections, without changing $C$ or executing a program. It still does not exhaust nonlinear tame coordinates or the full tame stabilizer.

### 5.1 Exact class and the three-pair necessity

For any $b\in\mathbb Z$ let

$$
V_b(x,y)=(x,y+b x^2).
$$

It is an integral tame automorphism with inverse $(x,y)\mapsto(x,y-bx^2)$. Consider a triangular reflection after **any unimodular affine coordinate change following this $V_b$**. Thus the reflection is conjugated by $M=L\circ V_b$, where $L$ is any affine map with integral coefficients and linear determinant one. Allowing determinant minus one gives the same class, by changing the sign of a complementary coordinate.

An elementary reflection $(u,v)\mapsto(u,Q(u)-v)$ has exactly three fixed points on $\mathbb F_3^2$: for each $u$, the equation $2v=Q(u)$ has one solution. The same is true of any integral tame conjugate, because its reduction is a polynomial automorphism. Since $C\to\mathbb F_3^2$ is bijective, a reflection preserving $C$ must therefore have exactly three fixed points and **three disjoint exchanged pairs** in $C$.

Ignoring a constant translation, its invariant coordinate has the form

$$
\ell(x,y)=a x+d(y+b x^2),\qquad \gcd(a,d)=1.
$$

Changing its sign does not change its fibers, so take $d\ge0$. If $d=0$, then $a=\pm1$ and the fibers are precisely the original $x$ fibers. Their reflection permutation is forced to be $i$, as in Section 2; the extra quadratic term in a complementary coordinate only changes the center polynomial by an integral polynomial. Hence this case gives no new restriction.

For $d>0$, put $r=a/d$. Two distinct points $(x_j,y_j),(x_k,y_k)$ can be exchanged only if they have the same $\ell$ value. Such a pair must have $x_j\ne x_k$, and the equality is exactly

$$
r=-b(x_j+x_k)-\frac{y_j-y_k}{x_j-x_k}.
$$

There are five pairs with equal $x$ and 31 remaining pairs. The possible reduced denominators of the displayed slopes are $1,2,3,4$, because the nonzero $x$ differences have absolute value at most four. Since $b(x_j+x_k)$ is integral, an exchanged pair forces $d$ to equal that reduced denominator. All pairs exchanged by one reflection must use the same resulting rational $r$.

### 5.2 Fractional-slope cases

The following is the complete list of pairs with nonintegral slope, obtained by substituting the nine frozen points. A pair label is unordered.

| Reduced denominator | Required $r$ | Point pairs |
| --- | --- | --- |
| 2 | $-3/2$ | $(3,6)$ |
| 2 | $-1/2$ | $(6,8),(3,7)$ |
| 2 | $1/2$ | $(7,8)$ |
| 2 | $-4b-1/2$ | $(2,4)$ |
| 3 | $-b-4/3$ | $(6,9)$ |
| 3 | $-b-2/3$ | $(7,9)$ |
| 3 | $-3b-1/3$ | $(1,4)$ |
| 3 | $-3b+1/3$ | $(4,5)$ |
| 4 | $-2b-3/4$ | $(4,6)$ |
| 4 | $-2b-1/4$ | $(4,7)$ |

For denominator two, the only value supported by two pairs is $r=-1/2$. Obtaining a third pair at that value forces $-4b-1/2=-1/2$, hence $b=0$. Neither $r=-3/2$ nor $r=1/2$ can support three pairs. For denominator three, each fractional residue class modulo $\mathbb Z$ contains only two listed pairs, so it cannot supply three exchanged pairs. For denominator four, each fractional residue class has only one pair. Consequently **for $b\ne0$, none of $d=2,3,4$ can preserve $C$ by such a reflection**.

### 5.3 Complete integer-slope table

It remains to take $d=1$, so $r=c\in\mathbb Z$ and the invariant coordinate is

$$
\ell=y+b x^2+c x.
$$

The 20 integral-slope pairs give exactly the following 18 distinct affine expressions for $c$. Each expression has the pair multiplicity displayed; there are no other pairs with a common $\ell$ value.

| Required $c$ | Point pairs |
| --- | --- |
| $b-4$ | $(5,6)$ |
| $b-2$ | $(1,6),(5,7)$ |
| $b$ | $(1,7)$ |
| $-1$ | $(2,6)$ |
| $0$ | $(2,7)$ |
| $-b-1$ | $(1,3)$ |
| $-b$ | $(1,2)$ |
| $-b+1$ | $(1,8),(3,5)$ |
| $-b+2$ | $(2,5)$ |
| $-b+3$ | $(5,8)$ |
| $-2b-1$ | $(1,9)$ |
| $-2b$ | $(5,9)$ |
| $-3b-3$ | $(8,9)$ |
| $-3b-2$ | $(2,9)$ |
| $-3b-1$ | $(3,9)$ |
| $-4b-1$ | $(4,8)$ |
| $-4b$ | $(3,4)$ |
| $-5b+1$ | $(4,9)$ |

The rows may coincide for special $b$. When several rows coincide, pairs sharing endpoints must be assembled into one fiber: for instance, a three-point fiber supports at most one exchanged pair, not three. For a fiber of size $s$, any reflection supports at most $\lfloor s/2\rfloor$ exchanged pairs. Comparing the displayed expressions gives the following complete hand table for $b\ne0$.

| $b$ | Values of $c$ that can support at least three disjoint exchanged pairs | Bound at every other $c$ |
| --- | --- | --- |
| $b\le-4$ | none | at most two pairs |
| $-3$ | none | at most two pairs |
| $-2$ | none | at most two pairs |
| $-1$ | $0$ | at most two pairs |
| $1$ | $0$ | at most two pairs |
| $2$ | $-1$ | at most two pairs |
| $3$ | none | at most two pairs |
| $b\ge4$ | none | at most two pairs |

For completeness, the unbounded rows do not involve extrapolation. For $b\ge4$, group the possible values into

$$
\{b-4,b-2,b\},\ \{-1,0\},\ [-b-1,-b+3],\
[-2b-1,-2b],\ [-3b-3,-3b-1],\ [-4b-1,-4b],\ \{-5b+1\}.
$$

The last five groups are disjoint from each other, except that at $b=4$ the upper endpoint of the third group can meet $-1$ in the second. The first group can meet the second only at $b=4$, at zero. Each such meeting has just two listed single-pair rows; the internal double-pair rows meet nothing else. Thus no value supports three disjoint exchanged pairs. For $b=-k\le-4$, the first two groups are negative or zero, while the remaining groups are

$$
[k-1,k+3],\ [2k-1,2k],\ [3k-3,3k-1],\
[4k-1,4k],\ \{5k+1\}.
$$

These are mutually disjoint, except that the first two meet at $k=4$, again through two single-pair rows. This proves the other unbounded row. The six nonzero integers $-3,-2,-1,1,2,3$ are direct substitutions into the 18-row table, with shared endpoints grouped into fibers before counting pairs.

### 5.4 The three nonlinear cases fail integral interpolation

For $d=1$, choose coordinates $(x,\ell)$, which are integral unimodular polynomial coordinates with inverse $(u,v)\mapsto(u,v-bu^2-cu)$. A reflection preserving $\ell$ must be of the form

$$
(x,\ell)\longmapsto(P(\ell)-x,\ell),\qquad P\in\mathbb Z[t].
$$

Any other unimodular complementary coordinate differs by its sign and an integral affine function of $\ell$. That only changes $P$ by a sign and an integral affine function, so cannot repair a failure of integer value-difference divisibility. Constant affine coordinate translations likewise leave this obstruction unchanged.

The required fiber centers for the three surviving cases give:

| $(b,c)$ | Two forced polynomial values | Failed necessary divisibility |
| --- | --- | --- |
| $(-1,0)$ | $P(-8)=6$, $P(2)=0$ | $10\nmid -6$ |
| $(1,0)$ | $P(0)=1$, $P(6)=4$ | $6\nmid3$ |
| $(2,-1)$ | $P(0)=1$, $P(8)=4$ | $8\nmid3$ |

The first row comes from the singleton points 4 and 5 after the coordinate change. In the second and third rows, points 1 and 8 form the fiber at $\ell=0$, so their first-coordinate sum is one; point 9 is the singleton at $\ell=6$ or $8$, respectively, so its reflected center value is four. These are exact values at the original points, not numerical approximations.

Every integral polynomial satisfies $s-t\mid P(s)-P(t)$, so all three cases are impossible. Combining Sections 5.1–5.4 shows: **if $b\ne0$, every reflection from this entire post-affine quadratic-shear class that preserves $C$ induces only the already known vertical permutation $i$**. The case $b=0$ is the affine-coordinate subclass assigned to E2. In particular, this specific nonlinear bridge produces no new generator beyond that subclass.

The proof covers arbitrary integer $b$ and arbitrary unimodular affine changes **after this specified vertical quadratic shear**. It does not cover arbitrary affine changes before the shear, higher-degree shears, general compositions of coordinate changes, or all elements of the tame stabilizer. No search or mathematical program was executed to obtain the tables above.

## 6. Arbitrary-degree triangular conjugates of $A$ give no new restriction

This is a different precise bridge: the intermediate map is allowed to send $C$ to a different nine-point set. The conclusion still concerns only the specified one-conjugator class, not arbitrary longer tame words.

**Proposition.** Let

$$
E(x,y)=(\alpha x+c,\beta y+f(x)),\qquad
\alpha,\beta\in\{1,-1\},\quad c\in\mathbb Z,\quad f\in\mathbb Z[t],
$$

with no degree or coefficient bound. If $E^{-1}AE$ preserves $C$, then its restriction is one of

$$
a,\quad iai,\quad a^{-1},\quad ia^{-1}i.
$$

In particular, adjoining any number of these conjugates cannot enlarge $\langle a,i\rangle$.

**Proof: the intermediate set and its centroid.** Put $C'=E(C)$. The hypothesis is equivalent to $A(C')=C'$. The centroid of any finite nonempty $A$-invariant set is an $A$-fixed point over $\mathbb Q$. Solving $A(x,y)=(x,y)$ gives the unique point $(2/3,1/3)$. Direct summation of the frozen $C$ also gives this centroid. Therefore the first-coordinate mean of $E(C)$ satisfies

$$
\alpha\frac23+c=\frac23.
$$

The alternative $\alpha=-1$ would require $c=4/3\notin\mathbb Z$. Hence $\alpha=1,c=0$, and $C'$ has precisely the same first-coordinate multiplicities as $C$:

$$
\begin{array}{c|ccccc}
x&-1&0&1&2&3\\\hline
\text{multiplicity}&2&2&3&1&1.
\end{array}
$$

**All possible intermediate sets.** For $(x,y)\in C'$, the first coordinates of $A(x,y)$ and $A^2(x,y)$ must also lie between $-1$ and $3$. This forces

$$
-1\le x\le3,\qquad -2\le y\le2,\qquad |x-y|\le2.
$$

These conditions describe exactly 18 lattice points. They split into the following six three-cycles of the actual affine map $A$:

$$
\begin{aligned}
O_1&=\{(0,0),(1,0),(1,1)\},\\
O_2&=\{(3,1),(0,2),(-1,-2)\},\\
O_3&=\{(-1,0),(1,-1),(2,2)\},\\
O_4&=\{(-1,-1),(2,0),(1,2)\},\\
O_5&=\{(-1,1),(0,-2),(3,2)\},\\
O_6&=\{(0,-1),(2,1),(0,1)\}.
\end{aligned}
$$

The list is exhaustive by its rows: for $x=-1,0,1,2,3$, the allowed height intervals contain respectively $4,5,4,3,2$ points, totaling 18; every listed point satisfies the inequalities and the 18 points are distinct. There is no integral $A$-fixed point, so $C'$ is a union of three of these orbits.

The multiplicity one at $x=3$ requires exactly one of $O_2,O_5$. The multiplicity two at $x=-1$ then requires exactly one of $O_3,O_4$. To obtain multiplicity three at $x=1$, the third orbit must be $O_1$, not $O_6$. Thus there are only four possible $C'$:

$$
O_1\cup O_s\cup O_t,
\qquad s\in\{2,5\},\quad t\in\{3,4\}.
$$

On each fixed $x$ fiber, $E$ acts as $y\mapsto\beta y+f(x)$ and preserves all height gaps. At $x=-1$, the original heights are $\{-2,0\}$, with gap two. The two mixed choices $(s,t)=(2,4)$ and $(5,3)$ give respectively $\{-2,-1\}$ and $\{0,1\}$, each with gap one, so both are impossible. The remaining choices are $C'=C$ and

$$
C'=D:=O_1\cup O_5\cup O_4=R(C),\qquad R(x,y)=(x,x-y).
$$

The displayed equality follows by applying $R$ to each of the three original orbits. The map $R$ is a global integral affine involution, and direct substitution gives the global identity $RAR=A^{-1}$.

**Restrictions of the conjugates.** If $C'=C$ and $\beta=1$, a translation preserving each finite nonempty height fiber is trivial, so $E|_C=1$. If $C'=C$ and $\beta=-1$, the unique reflection centers of those fibers are $q(x)$, so $E|_C=i$.

If $C'=D$ and $\beta=-1$, the unique fiberwise reflection mapping $C$ to $D$ is $R|_C$. If $C'=D$ and $\beta=1$, the unique fiberwise translation mapping $C$ to $D$ is $(RI)|_C$; it has translation polynomial $x-q(x)$, because $I$ preserves the original fibers. Thus the four possible restrictions of $E:C\to C'$ are precisely

$$
1,\quad I|_C,\quad R|_C,\quad (RI)|_C.
$$

Since $A$ preserves the relevant intermediate set and the inverse restrictions are forced, $E^{-1}AE|_C$ is respectively

$$
a,\quad iai,\quad (RAR)|_C=a^{-1},\quad (IRARI)|_C=ia^{-1}i.
$$

This proves the proposition. No assertion was made that every $E$ agreeing with one of these maps on $C$ equals that map globally. All degrees and coefficients of $f$ were covered through its exact restrictions, not through a coefficient search. $\square$

The entire tame stabilizer remains unclassified: a general returning word can pass through several intermediate sets using different triangular directions, and need not be one of the conjugates in this proposition. No integer nine-cycle has been produced or excluded in that larger class.
