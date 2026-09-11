# Conditional exclusion proofs for adjacent swaps

## Claim and status

**PROVABLE AS STATED** for the three elementary statements below.
These are deductions about already excluded primitives, not a proposed new
literal and not a residual two-axis theorem contract. No chooser or new
finite system is instantiated. They explain precisely which arguments
cannot supply a new paper merely by changing names or phase notation.

## Assumptions and notation

Let $X$ be a finite nonempty set. Function composition acts right-to-left.
An involution $s:X\to X$ satisfies $s^2=\mathrm{id}_X$.
For $n\ge1$, let $S_n$ be the permutations of $[n]$ in one-line notation,
let $s_i$ exchange positions $i,i+1$, and let $\iota=12\cdots n$.
Write
$$
 \mathrm{Inv}(w)=|\{(a,b):1\le a<b\le n,\ w_a>w_b\}|,\qquad
 D(w)=\{i:w_i>w_{i+1}\}.
$$

In Statement 2 only, $p$ is any deterministic selector satisfying
$p(w)\in D(w)$ for every $w\ne\iota$. We discuss this known scheduler
class conditionally; this desk does not nominate any particular $p$.

## Strategy and dependency map

1. Invariant guards let the same involution undo itself.
2. One adjacent inversion swap removes exactly one inversion; involutivity
   of the local swap separately identifies every possible predecessor.
3. Finiteness converts surjectivity of a factor into invertibility, while
   cycle decomposition handles restrictions and return sections.
No finite enumeration, source operator theorem, KIP proof or pointer orbit
formula is a premise of these arguments.

## Proof

### 1. Fixed guarded swaps, fixed products and explicit phase lifts

Suppose $a:X\to\{0,1\}$ satisfies $a(sx)=a(x)$ for all $x$ and define
$\tau(x)=s(x)$ if $a(x)=1$, and $\tau(x)=x$ otherwise.
If $a(x)=0$, both applications of $\tau$ fix $x$.
If $a(x)=1$, the guard remains one at $sx$, so
$\tau^2(x)=s^2(x)=x$. Hence $\tau$ is an involution.

For any finite collection of such guarded involutions, cancellation shows
that every fixed word
$U=\tau_{i_m}\circ\cdots\circ\tau_{i_1}$ is bijective, with inverse
$\tau_{i_1}\circ\cdots\circ\tau_{i_m}$. Every immediate fibre is singleton.

More generally, for bijections $U_0,\ldots,U_{m-1}$ of $X$ and $m\ge1$,
the ordinary autonomous phase lift
$$
 \widehat U(x,j)=(U_jx,j+1\bmod m)
$$
has inverse
$$
 \widehat U^{-1}(y,k)=(U_{k-1\bmod m}^{-1}y,k-1\bmod m).
$$
Substitution verifies both compositions, including $m=1$.

The guard assumption matters. On $S_2$, “swap only if descending” sends
both $12$ and $21$ to $12$. It is not swap-invariant and is not bijective.
Nor does a state-dependent choice among involutions satisfy the fixed-word
hypothesis automatically. No such overgeneralization is used.

### 2. One-descent-swap clocks and generic full-target inversion

For the already standard selector class, write
$F_p(\iota)=\iota$ and $F_p(w)=s_{p(w)}w$ otherwise.
If $i\in D(w)$, swapping positions $i,i+1$ removes their one mutual
inversion. For any third position, the sum of its inversion indicators
with these two entries is unchanged, because both entries remain on the
same side of that third position. All other indicators are unchanged.
Therefore
$$
 \mathrm{Inv}(F_p(w))=\mathrm{Inv}(w)-1\quad(w\ne\iota).
$$
A permutation with no adjacent descent is strictly increasing, hence
equals $\iota$. Repeated application consequently reaches $\iota$ at
exactly $\mathrm{Inv}(w)$ steps. The worst-case clock is
$\binom n2$, attained exactly by the decreasing permutation; for $n=1$
the only state is already fixed.

Independently of the temporal argument, all target predecessors are
$$
 F_p^{-1}(y)=
 \begin{cases}\{\iota\},&y=\iota,\\ \varnothing,&y\ne\iota\end{cases}
 \ \cup\
 \{s_i y:1\le i<n,\ y_i<y_{i+1},\ p(s_i y)=i\}. \tag{1}
$$
Indeed, every nonidentity predecessor must have swapped some descent $i$;
undoing the involution gives $s_i y$, and the old descent is exactly the
displayed target ascent. The selector condition is necessary.
Conversely, each displayed candidate has descent $i$, is nonidentity and
is sent to $y$ by its prescribed selector. Distinct indices give distinct
permutations, since permutations have distinct entries and different
position transpositions act differently. None equals $\iota$ when
$y=\iota$.

For $y=\iota$, each $s_i\iota$ has its unique descent at $i$, so every
selector must choose $i$. Thus $|F_p^{-1}(\iota)|=n$.
Every other target has at most $n-1$ predecessors by (1). Hence the
unique largest fibre is the identity fibre, also covering $n=1$.

The clock, inverse candidate set and extremum follow for *every* selector
in this primitive class. They therefore do not establish a selector-specific
residual; writing a new priority rule without a further mechanism would
not evade the historical standard-sorting deduction. This does not prove
that every selector lacks a further independent enumerative theorem.
The assertion is
about one adjacent swap per update, not a parallel or whole-pass clock.

### 3. Finite permutation factors, restrictions and return sections

Let $P:X\to X$ be a permutation, let $Y$ be finite, let $T:Y\to Y$, and let
$q:X\to Y$ be surjective with $qP=Tq$. Given $y\in Y$, choose $x$ with
$q(x)=y$, then put $z=P^{-1}x$. The identity $T(qz)=q(Pz)=y$ proves
that $T$ is surjective. Since $Y$ is finite, it is bijective.
Thus a genuine deterministic finite factor has singleton immediate fibres.

If $\varnothing\ne A\subseteq X$ and $P(A)\subseteq A$, then $P|_A$ is
injective. Finiteness gives $|P(A)|=|A|$, hence $P(A)=A$ and the restriction
is again a permutation. For any nonempty section $B\subseteq X$, intersect
$B$ with the cycles of $P$. On each nonempty intersection, the first positive
return follows the cyclic order of those marked states and is a cyclic
permutation. The union of these return maps is a permutation of $B$.

These statements do not exclude independent orbit enumeration. They do not
identify arbitrary permutation dynamics with rotations, nor identify
the mutable-function pointer residual with a fixed toggle word.
They also do not apply to nonautonomous observation rules for which no
well-defined semiconjugate $T$ exists.

## Corrections, boundaries and open risks

The general claim “adjacent swaps are automatically bijective” is false;
Statement 1 states its missing guard/fixed-word assumptions. Statement 2
does not apply to promotion sorting merely because it has local swaps:
that operator makes a full sweep, and its state space and comparison
predicate must be matched literally.

The three proofs are self-contained author deductions and were manually
checked without executing a mathematical program. They are elementary
mechanism exclusions, not an independent review or a novelty theorem.
A new all-parameter temporal/orbit theorem plus a materially independent
inverse/enumeration theorem outside these specific old entrances has
**NOT BEEN ESTABLISHED BY THIS DESK**. This is a bounded failure to nominate,
not a proof that all finite permutation systems are exhausted.
