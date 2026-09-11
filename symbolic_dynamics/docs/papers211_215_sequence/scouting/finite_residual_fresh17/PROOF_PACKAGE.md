# Fresh17 proof package

2026-09-10 UTC. Author: /root/round211_functional_surgery_residual.
One literal desk attempt, zero pilots, NO_PROMOTION, HOLD_EXTERNAL.
The deductions below are author reasoning, not independently accepted
theorems or evidence of novelty.

## Claim

On all labelled matroids on one fixed finite ground set, compose duality
with one-rank truncation, in that order. Its even iterates have an explicit
rank-clipping formula; the recurrent matroids, exact entrance times and
sharp rank-conditioned maximum times follow. Its every-target predecessor
problem is exactly nontrivial matroid erection, with a separate rank-zero
boundary. The apparently attractive fibre maximum is already source-owned.

## Status

PROVABLE AS STATED for the author-derived identities and boundary cases
proved below. NO_PROMOTION as a research candidate: the temporal mechanism
is a rank-capped standard Higgs lift, and the separate inverse/extremal
mechanism is established erection theory. A clean pair of formulae is not
a new pair of research contributions.

## Assumptions and notation

Fix an integer $n\geq0$ and $E=[n]$. The carrier $\mathcal M(E)$ consists
of all matroids with exactly this labelled ground set. It is finite because
each independent-set family is a subset of $2^E$. The matroid itself is
the state. It is not a subset of a frozen matroid, a matrix representation,
a graphic-basis state, or a variable-ground minor process.

Write $r_M(A)$ for rank on $A\subseteq E$ and $r=r_M(E)$.
Let $M^*$ be the dual, whose bases are the complements of bases of $M$.
For $0\leq c\leq r$, let $\operatorname{tr}_c M$ have independent sets
the independent sets of $M$ of size at most $c$. Define
$\tau M=\operatorname{tr}_{r-1}M$ for $r>0$, and $\tau M=M$ for $r=0$.
The sole newly instantiated literal in this desk is

$$F(M)=\tau(M^*). \tag{1}$$

Thus the rank-zero convention is explicit. It does not count as a second
candidate. Let $U_{r,n}$ denote the unique uniform matroid with rank
function $u_r(A)=\min(r,|A|)$.

For a rank-$r$ matroid define its uniform-rank defect

$$d(M)=\max_{A\subseteq E}\bigl(u_r(A)-r_M(A)\bigr). \tag{2}$$

This is an integer statistic defined from the input, not a finite-state
enumeration performed here. The entrance time $t(M)$ is the first
nonnegative iterate index at which the state lies on a periodic orbit.

## Proof strategy and dependency map

1. Complementary bases give dual rank; the independent-set exchange axiom
   gives truncation rank.
2. Substitute these two ranks twice to get a pointwise clipping recurrence.
3. Solve that recurrence at each subset, deduce the periodic core and exact
   entrance time, then construct loop/coloop witnesses for sharpness.
4. For inverse fibres, undo the bijective dual first. What remains is
   precisely the defining truncation/erection relation, not a new decoder.
5. Keep the source-owned extremal result separate from the author deduction
   and from any unproved equality-case classification.

## Proof

### Step 1. Closure and the two standard rank formulae

The truncation independent sets are hereditary and contain the empty set.
If $I,J$ are such sets with $|I|<|J|\leq c$, the exchange element supplied
by $M$ gives $I\cup\{e\}$ independent in $M$ and of size at most $c$.
Thus truncation is a matroid and

$$r_{\operatorname{tr}_c M}(A)=\min(c,r_M(A)). \tag{3}$$

Duality preserves the class of matroids. Its rank identity is

$$r_{M^*}(A)=|A|-r+r_M(E\setminus A). \tag{4}$$

Indeed, a dual basis is $E\setminus B$, where $B$ is a primal basis.
The maximum intersection of $A$ with a dual basis is $|A|$ minus the
minimum of $|A\cap B|$. That minimum is $r-r_M(E\setminus A)$:
a basis of $E\setminus A$ can be extended to a basis of $E$, and no basis
contains more than $r_M(E\setminus A)$ elements of the complement.

For $r<n$, put $s=n-r-1\geq0$. Equations (3) and (4) give

$$r_{F(M)}(A)=\min\{s,\ |A|-r+r_M(E\setminus A)\},\qquad
r(F(M))=s. \tag{5}$$

If $r=n$, $M$ is the free matroid $U_{n,n}$, and $F(M)=U_{0,n}$.
For $n=0$ the sole matroid is fixed. These exceptions are not substituted
into the formula for $s$.

### Step 2. The entire even-iterate rank function

Suppose $n>0$ and $r<n$. Apply (5) to the rank-$s$ matroid $F(M)$.
Its next rank is $n-s-1=r$, and for every $A\subseteq E$,

$$
\begin{aligned}
r_{F^2(M)}(A)
&=\min\{r,\ |A|-s+r_{F(M)}(E\setminus A)\}\\
&=\min\{r,\ |A|-s+
       \min(s,n-|A|-r+r_M(A))\}\\
&=\min\{r,\ |A|,\ r_M(A)+1\}.
\end{aligned} \tag{6}
$$

All even states therefore have rank $r$. Induction using (6) yields,
for every integer $k\geq0$,

$$r_{F^{2k}(M)}(A)=\min\{r,\ |A|,\ r_M(A)+k\}. \tag{7}$$

For the induction, applying (6) to the right side takes its minimum
with the same two caps after adding one, which is the expression for
$k+1$. The $k=0$ expression equals $r_M(A)$ by the rank axioms.
Applying (7) with initial state $F(M)$ also gives

$$r_{F^{2k+1}(M)}(A)
=\min\{s,\ |A|,\ r_{F(M)}(A)+k\}. \tag{8}$$

This is a whole-carrier identity, not a fit to small cases.

To identify the standard mechanism precisely: $M$ is a quotient of the
free matroid $U_{n,n}$, whose lattice of flats is all subsets of $E$.
The $k$th Higgs lift toward that free matroid has rank
$\min\{|A|,r_M(A)+k\}$. Hence (7) is its rank-$r$ truncation.
It is NOT asserted to be a Higgs lift directly from $M$ to the
same-rank $U_{r,n}$; that would in general violate the quotient hypothesis.
The relevant primary definition and rank formula are in
[Bonin–Schmitt, §2.3](https://arxiv.org/html/0902.0034v2).

### Step 3. Recurrent states and the exact entrance time

Equation (7) is uniform exactly when $k\geq d(M)$. Before then an
$A$ attaining the maximum in (2) witnesses nonuniformity.

Every uniform state of rank below $n$ satisfies

$$F(U_{r,n})=U_{n-r-1,n}. \tag{9}$$

These states lie on orbits of period dividing two. Conversely, a periodic
state of rank $r<n$ must have the same ranks after arbitrarily large even
iterates; equation (7) forces it to be $U_{r,n}$. The free matroid is not
periodic when $n>0$, because every output has rank at most $n-1$.

The recurrent core is therefore exactly the $n$ uniform matroids of ranks
$0,\ldots,n-1$. There is one fixed state when $n$ is odd, at
$r=(n-1)/2$, and none when $n$ is positive and even. The other states in
this core are paired by (9). The empty-ground case has one fixed state.

Put $e=d(F(M))$. By (7) and (8), the first even uniform iterate occurs
at index $2d(M)$ and the first odd uniform iterate at index $2e+1$.
Once uniform, all later states are uniform by (9). Consequently

$$t(M)=\min\{2d(M),\,2d(F(M))+1\}
\quad\text{for }n>0,\ r<n. \tag{10}$$

For the free matroid on a nonempty ground set, $t(U_{n,n})=1$.
For the empty ground set the entrance time is zero.

### Step 4. Sharp rank-conditioned clocks

For $r<n$ and $s=n-r-1$, the definition gives $d(M)\leq r$ and
$d(F(M))\leq s$. Thus (10) implies

$$t(M)\leq H(n,r):=\min\{2r,\,2(n-r)-1\}. \tag{11}$$

This is attained on every indicated rank stratum. Partition $E=C\sqcup L$
with $|C|=r$, and take the matroid $W$ in which every element of $C$ is a
coloop and every element of $L$ is a loop. Then

$$r_W(A)=|A\cap C|,\qquad
d(W)=\min(r,n-r). \tag{12}$$

For the upper bound in (12), $u_r(A)-|A\cap C|$ is at most both $r$
and $|A\cap L|$; choose a subset of $L$ of size $\min(r,n-r)$ for equality.
The dual has $L$ as coloops and $C$ as loops, so

$$r_{F(W)}(A)=\min(s,|A\cap L|),\qquad
d(F(W))=\min(s,r). \tag{13}$$

The deficiency in (13) is at most both $s$ and $|A\cap C|$; a subset
of $C$ of size $\min(s,r)$ attains it. Substituting into (10) gives
$\min(2r,2s+1)$: if $r\leq s$, this is $2r$; if $r\geq s+1$,
it is $2s+1$. This proves (11) is sharp, including $r=0$.

For $n\geq2$, the maximum over the whole carrier is $n-1$.
If $n=2m$, rank $r=m$ attains $2m-1$; if $n=2m+1$, rank $r=m$
attains $2m$. The free state's time one does not exceed this bound.
For $n=1$ the whole-carrier maximum is one; for $n=0$ it is zero.

No finite run, rank table, pilot or witness execution was used.

### Step 5. Full-target inverse reduction, with the missing boundary isolated

Let $K$ be any target on the same ground set.

If $n=0$, there is exactly one predecessor. Suppose $n>0$.
A rank-$n$ target has no predecessor, because $r(F(M))\leq n-1$.

For $1\leq s=r(K)\leq n-1$, the map $M\mapsto M^*$ gives the
exact bijection

$$
F^{-1}(K)\ \longleftrightarrow\
\{N\in\mathcal M(E):r(N)=s+1,\ \tau N=K\}.
\tag{14}
$$

The forward implication follows by setting $N=M^*$ in (1); the rank
condition follows from $s>0$. The converse takes $M=N^*$.
There is no extra freedom because duality is an involution.
The right side is the set of NONTRIVIAL erections of $K$.
The trivial erection $N=K$, sometimes included in source terminology,
must not be counted here.

For $K=U_{0,n}$, the intermediate dual may instead have rank zero OR
rank one. Rank zero contributes one free source. Every rank-one matroid
is determined by its nonempty set $C$ of nonloops: its nonempty independent
sets are exactly the singletons in $C$. To justify uniqueness, no pair can
be independent in rank one, and all nonloop singletons must be independent.
Every nonempty $C$ gives a matroid by these independent sets. There are
$2^n-1$ choices. Therefore

$$|F^{-1}(U_{0,n})|=2^n. \tag{15}$$

This includes the free source and does not confuse the count with
$2^n-1$ nontrivial erections.

### Step 6. Source-owned maximum, not a new inverse theorem

Write $p(n,k)$ for the number of labelled paving matroids of rank $k$.
For positive target rank $s<n$, (14) imports the established bound
$|F^{-1}(K)|\leq p(n,s+1)$, attained at $K=U_{s,n}$.
A paving matroid has no circuit smaller than its rank, so truncating
a rank-$(s+1)$ paving matroid gives exactly $U_{s,n}$.
The bound and its erection encoding are already in
[Pendavingh–van der Pol, §4.1, following Lemma 20](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i1p8/pdf/).
Their §3 supplies the general reconstruction theory.

In particular, merely writing a whole-carrier maximum as the maximum of
$2^n$ and the already-existing counts $p(n,2),\ldots,p(n,n)$ would only
package source-owned quantities. It does not evaluate those counts or
identify every maximizing target. No uniqueness or full equality-case
classification for the positive-rank bound is asserted here.

## Exact old-map distinctions and subtraction

The following are not claimed to be literal conjugacies with (1):

- Old C10 dualizes only odd-rank matroids and fixes even rank.
- Old ASD simplifies by deleting loops and nonleast parallel representatives,
  then dualizes on its smaller ground set.
- Current CCC varies a subset of a fixed matroid and removes the restriction's
  coloops under a complement. Its complete proof reduces to a fixed closure.

Their actual original rows/proofs were read. The new attempt keeps the
ground set and varies the entire matroid. This distinction avoids a false
literal collision, but does not recover the standard truncation/duality/
Higgs-lift mechanism or the source-owned inverse/extremal axis.

The preliminary TFPL and lattice-polygon directions are already explicit
old entrances. No boundary variant of either was instantiated here.

## Corrections or missing assumptions

The rank-zero truncation convention, the exceptional free matroid, the
empty ground set, and exclusion of trivial erections are essential.
No representability, graphicality or simplicity restriction is imposed;
closure of such subclasses under (1) is not asserted.

## Open risks and disposition

This is an author-only deduction and bounded source desk, not a hostile
review or an exhaustive literature claim. No complete pilot contract was
submitted and no scientific execution occurred. Source text extraction
has the limits recorded in SOURCES_AND_LIMITS.md. In particular, source
erection terminology and a displayed Lemma 20 parameter need care; this
desk does not certify every printed source line free of typographical
or extraction defects.

The candidate is closed at author level as
NO_PROMOTION_SOURCE_OWNED_INVERSE_AND_RANK_CLIPPING_TIME.
One real literal attempt is reported; no manuscript, reserve, independent
acceptance or root count is created. HOLD_EXTERNAL.

