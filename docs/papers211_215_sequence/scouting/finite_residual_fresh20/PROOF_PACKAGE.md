# Fresh20 proof package — rank-defect powering closes at desk

Author deductions by `/root/round211_functional_surgery_residual`, not an
independent review. The parent supplied routing and gate reminders only;
it did not contribute a theorem proof or accept this package. No scientific
execution is a dependency.

## Claim and status

**PROVABLE AS STATED:** the exact nilpotent quotient factor in Section 2;
the separated pointwise time formula and sharp tree-tail bound in Section 3;
the restricted inverse descriptions in Section 4.

**NOT CURRENTLY JUSTIFIED:** an independent new two-axis contribution;
an evaluated all-target rank-constrained inverse; a sharp maximum of the
full operator's fibre sizes; a sharp maximum of its full transient over
all functions. No such statement is asserted below.

Disposition: `KILL_OLD_NULLITY_FACTOR_NO_SECOND_RESIDUAL`. RDP is one
literal desk attempt, not a paper, reserve, pilot or zero-entry slate.

## 1. Assumptions, notation and proof dependencies

Fix $n\geq1$, keep all labels, and let $\mathcal T_n$ be the functions
$f:[n]\to[n]$. Composition powers have positive integer exponents. Set

$$
r(f)=|\operatorname{im}f|,\qquad
\mathcal N(f)=f^{\,n-r(f)+1}.
\tag{1}
$$

Let $C=C_f$ be the cyclic vertex set of the original function, $c=|C|$,
and $h$ its greatest distance to $C$. Thus $h=0$ exactly for permutations.
Let $m$ be the least common multiple of its cycle lengths and put
$d=n-c+1$. Define

$$
\delta(e)=n-r(f^e),\quad E_0=1,\quad
E_{t+1}=E_t(1+\delta(E_t))\qquad(e\geq1).
\tag{2}
$$

All maxima over an empty set are zero. The multiplicative order modulo
one is defined to be one. A tree leaf below means a nonroot vertex with
no children; the loop at a functional-graph root is retained and does not
create an additional leaf.

The proof strategy is to expose, not conceal, the occupied factor:

1. Linearize the literal labelled function and quotient by its cyclic
   coordinate space. Rank loss becomes exactly nilpotent nullity.
2. Identify the quotient update with the previously rejected nullity
   feedback map, using its original proof rather than an owner summary.
3. Separate its tail-collapse time from the subsequent cyclic-group
   powering. Prime valuations give the latter's exact remaining time.
4. Inspect inverse slices. Their static reconstructions are not promoted
   to the unresolved all-target or maximum-fibre theorem.

## 2. Exact old nilpotent factor, not a full conjugacy

Take any field $K$ and the vector space $V=K^{[n]}$ with basis $e_v$.
Let $L_f e_v=e_{f(v)}$ and let $W_C$ be the span of $e_v$ for $v\in C$.
The space $W_C$ is invariant, and $L_f|_{W_C}$ is a permutation matrix,
hence invertible in every characteristic. Let $Q_f$ be the induced
operator on $V/W_C$.

The cyclic vertex set of every positive power $f^e$ is exactly $C$.
Indeed a vertex on an original cycle remains on a cycle after powering.
Conversely $(f^e)^a(v)=v$ implies $f^{ea}(v)=v$, so an originally
noncyclic vertex cannot become cyclic. Consequently the same quotient
space is used throughout the trajectory of (1).

Distinct image labels give independent basis vectors, so
$\operatorname{rank}L_f^e=r(f^e)$. Also
$W_C\subseteq\operatorname{im}L_f^e$ because the restriction to $W_C$
is invertible. Passing the image to the quotient therefore gives

$$
\operatorname{rank}Q_f^e=r(f^e)-c,
\qquad
\dim\ker Q_f^e=(n-c)-(r(f^e)-c)=\delta(e).
\tag{3}
$$

In the quotient basis indexed by noncyclic vertices, $Q_f$ sends a vertex
to its parent if that parent is noncyclic, and to zero otherwise. It is
nilpotent. If $h\geq1$, then $Q_f^h=0$ and a vertex at distance $h$
shows $Q_f^{h-1}\ne0$; thus its nilpotency index is exactly $h$.
For $h=0$ the quotient has dimension zero.

Linearization respects composition, and taking a quotient respects
powers. Equations (1) and (3) imply the exact identity

$$
Q_{\mathcal N(f)}=Q_f^{\,1+\dim\ker Q_f}.
\tag{4}
$$

After taking nilpotent similarity classes, (4) is the literal old map
$[A]\mapsto[A^{1+\dim\ker A}]$, on dimension $n-c$, in
`docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power`.
Its original `PROOF_PACKAGE.md`, Propositions 1--4, and
`DERIVATION_PACKAGE.md`, Sections 2--4, already establish the cumulative
exponent, exact nilpotent clock, sharp Sylvester threshold and a stronger
deepest-type boundary. In particular, if $\lambda$ is the Jordan type
of $Q_f$, then (2) becomes exactly its old recurrence

$$
E_{t+1}=E_t\left(1+\sum_i\min(E_t,\lambda_i)\right).
\tag{5}
$$

This is a genuine factor, not just a shared title. For any prescribed
cyclic set $C$ with $c\geq1$ and any partition of $n-c$, realize its
parts by disjoint off-cycle chains of those lengths, attaching each
chain to a chosen point of $C$. Any permutation on $C$ completes a
function whose quotient has exactly that nilpotent type. Thus every
old type of the relevant dimension occurs in this factor.

It is not a conjugacy of the full labelled carriers. Quotient type loses
cyclic permutations, attachment information and labels, and many distinct
functions have the same type. In particular it cannot transfer the old
similarity-class inverse counts into labelled function fibres. The full
linearization is injective, but its nilpotent quotient-type map is not.

## 3. Exact temporal ceiling and its subtraction

### 3.1 Accumulated powers and tail collapse

Induction directly in (1) gives

$$\mathcal N^t(f)=f^{E_t}.\tag{6}$$

The greatest vertex distance to the cyclic set in $f^e$ is
$\lceil h/e\rceil$, with value zero for $h=0$. A positive power moves
each vertex forward $e$ original steps until it first reaches the
unchanged cyclic set. Therefore

$$
s=\min\{t\geq0:E_t\geq h\}
\tag{7}
$$

is the first epoch with all noncyclic vertices at distance at most one;
for $h\leq1$ it is zero. Equivalently it is the first epoch when
$Q_f^{E_t}=0$. It is exactly the already occupied nilpotent clock.

Put $a_0=1$ and $a_{t+1}=a_t(a_t+1)$, and let
$S(h)=\min\{t:a_t\geq h\}$. For $1\leq e\leq h$, the $e$ vertices
of a deepest path at distances $h-e+1,\ldots,h$ cannot lie in
$\operatorname{im}f^e$: an $e$-step predecessor of any of them would
have distance greater than $h$. Hence $\delta(e)\geq e$ in this range.
While $E_t<h$, equation (2) gives $E_{t+1}\geq E_t(E_t+1)$, and
induction up to the stopping epoch proves

$$s\leq S(h).\tag{8}$$

For one off-cycle chain of length $h$, with all remaining vertices
cyclic, $\delta(e)=\min(e,h)$. Equality holds in the recurrence before
the stopping epoch, so (8) is sharp for every feasible
$1\leq h\leq n-1$. The sharp all-function *tail-collapse* maximum is
therefore $S(n-1)$ for $n\geq2$, and zero for $n=1$.
This is the chain realization of the old single-Jordan-block witness,
not an independent new time theorem.

### 3.2 The later cyclic clock

Permutations have $\delta(e)=0$, so (1) fixes every permutation.
Now suppose $h\geq1$. Then $c<n$, $d\geq2$, and from epoch $s$
onwards the image is exactly $C$. Thus

$$E_{s+u}=E_s d^u\qquad(u\geq0).\tag{9}$$

For positive integers $a,b\geq h$, one has $f^a=f^b$ if and only if
$a\equiv b\pmod m$. Necessity follows by restriction to each cycle.
For sufficiency, every vertex has entered a cycle by either exponent;
subsequent positions agree because every cycle length divides $m$.

Write

$$
M=\frac{m}{\gcd(m,E_s)},\qquad
M_{\perp}=\prod_{p\nmid d}p^{v_p(M)},\qquad
J=\max_{p\mid d}\left\lceil\frac{v_p(M)}{v_p(d)}\right\rceil.
\tag{10}
$$

Here $v_p$ denotes the exponent of a prime in a positive integer.
At epoch $s+u$, a return after $q\geq1$ further epochs is equivalent to
$M\mid d^u(d^q-1)$. For $p\mid d$, the number $d^q-1$ is not
divisible by $p$, so return is impossible until $u\geq J$.
For primes not dividing $d$, multiplication by $d^u$ is invertible,
and return is equivalent to $d^q\equiv1\pmod{M_{\perp}}$.
This proves the exact full pointwise transient and period

$$
\tau_{\mathcal N}(f)=s+J,\qquad
\operatorname{per}_{\mathcal N}(f)=\operatorname{ord}_{M_{\perp}}(d).
\tag{11}
$$

No epoch before $s$ is recurrent: its graph has a vertex at distance
at least two, whereas all later epochs from $s$ have height one.
This also proves the lower bound implicit in (11).

Consequently the recurrent functions are exactly those with $h\leq1$
and $\gcd(m,n-c+1)=1$, including all permutations. The fixed functions
are exactly those with $h\leq1$ and $m\mid n-c$; divisibility into
zero includes every permutation. These conclusions also cover $n=1$.

Equation (11) couples the old cumulative exponent to a cyclic-group
power map. The prime-power/coprime decomposition and multiplicative-order
period are credited as ordinary power-map theory; they are not a new
inverse or structural axis. The original source comparison and exact
read bounds are in `SOURCE_READS.md`.

### 3.3 Two hand-checkable scope controls, not a pilot

On $[13]$, take the cycle $(1\ 2\ \cdots\ 8)$ and arrows
$13\to12\to11\to10\to9\to1$. Here $h=5$, $c=8$, $d=6$,
and $m=8$. The first cumulative exponents are $1,2,6,36,216$.
Thus $s=2$, $M=4$, $J=2$, and the full transient is four. In contrast
the sharp tail bound at this carrier is $S(12)=3$. The latter is not
a full-transient bound.

On $[4]$, the function with value list $(2,3,1,1)$ has $h=1$, $c=3$,
$d=2$ and $m=3$. It is already recurrent with period two, with other
state $(3,1,2,2)$. The full system does not always converge to a fixed
function. Both examples follow from the displayed arrows and (2), not
from enumerated experimental output.

## 4. Inverse information and the missing axis

### 4.1 A general identity is not an evaluated inverse

For an arbitrary target $g$, the disjoint union

$$
\mathcal N^{-1}(g)=
\bigsqcup_{k=1}^{n}
\{f\in\mathcal T_n:f^k=g,\ r(f)=n-k+1\}
\tag{12}
$$

is exact, but only rewrites the question as rank-constrained iterative
roots. No independent inverse theorem is claimed from it. If $g$ is
a permutation, every root $f$ is a permutation, hence $k=1$, and its
fibre is the singleton $\{g\}$.

### 4.2 Constant targets: exact height--leaf condition, unevaluated extremum

Fix a label $v$ and let $g$ be the constant function with value $v$.
The cyclic set of a predecessor is exactly $\{v\}$. Its graph is
therefore a labelled tree oriented to $v$ together with the loop at
$v$. Let $H$ be its height and $L$ its number of nonroot leaves.
The missing image labels are exactly those leaves, so the selected
exponent is $L+1$. All vertices map to $v$ after that power if and
only if

$$H\leq L+1.\tag{13}$$

Conversely every such rooted tree supplies one predecessor. At $n=1$
there is one predecessor with $H=L=0$. For $n\geq2$ this is a
nonempty labelled-tree class, not an evaluated sharp global fibre
maximum. A recurrence marking tree height and leaf number followed
by the inequality filter in (13) remains ordinary static enumeration.
No asymptotic equivalence or extremal comparison is asserted.

### 4.3 Targets of defect one reduce to ordinary permutation square roots

Suppose $r(g)=n-1$. Any predecessor is singular and has rank at least
$n-1$, so it has rank exactly $n-1$ and selected exponent two.
A singular functional graph with exactly one missing image vertex
has exactly one noncyclic leaf. Its off-cycle vertices consequently
form one chain: branching or a second nonempty attached tree would
give another leaf. If the chain has length $H$, its squared graph
has defect $\min(2,H)$. Thus $H=1$ is necessary here.

It follows that if $g$ has height greater than one, its fibre is
empty. Otherwise let $z$ be its sole noncyclic vertex, let
$C=[n]\setminus\{z\}$, let $\gamma=g|_C$ and let $y=g(z)$.
For each permutation $\sigma$ of $C$ with $\sigma^2=\gamma$, define

$$f|_C=\sigma,\qquad f(z)=\sigma^{-1}(y).\tag{14}$$

This is the unique predecessor with that cyclic restriction, and
every predecessor has this form. The count is exactly the ordinary
number of square roots of $\gamma$. Its published evaluated formula
is already covered by Leaños--Moreno--Rivera-Martínez, Theorem 1
and its proof; the attachment in (14) contributes no additional
choice or non-generic counting mechanism.

## 5. Disposition and open risks

The promising tail clock is exactly the old nilpotent quotient clock.
The additional cyclic motion is an ordinary power-map lift, while
the labelled inverse has not been evaluated beyond the static slices
above. The old nilpotent inverse is not transplanted to this different
labelled carrier. These are affirmative limitations, not a claim that
the complete RDP literal has a published owner.

Close this one literal attempt with no candidate nomination. A bounded
public non-hit does not establish novelty. No global maximum time or
fibre, all-target root atlas, paper-scale residual, independent PASS,
pilot, science execution or manuscript gate is inferred. All earlier
failed lookups, overly broad discovery returns and the initial routing
lead remain historical evidence, not corrected successful reads.
