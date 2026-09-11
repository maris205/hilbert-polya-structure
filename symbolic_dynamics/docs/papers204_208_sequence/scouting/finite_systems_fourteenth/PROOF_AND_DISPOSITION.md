# Fourteenth proof boundary and author deductions

Author: `batch197_fifth_scout`. These are mathematical author notes, not
independent candidate or manuscript review. The immutable intake owns the
six definitions. Its three desk proofs remain the original pre-pilot
deductions. Nothing below alters a literal or enlarges a pilot box.

## 1. SNC: evaluated sink extremum, but no retained temporal axis

### Claim, assumptions and status

Assume $c\ge2$, $p$ is odd and $p\nmid 2c$. Use exactly the intake SNC map
on $2\times c$ matrices plus its fixed sink. The sink is the **unique**
largest one-step fibre and has size

$$
E_{c,p}=p^{2c}+1-(p-1)^2p^{c-2}\bigl((p-1)^c-(-1)^c\bigr).
\tag{S1}
$$

For a nonsink target $Y$, its fibre is zero unless every column sum is 2.
If all column sums are 2, then

$$
|F^{-1}(Y)|=(p-1)^2
\#\{v\in(\mathbb F_p^*)^c:Yv=c\mathbf1_2\}.
\tag{S2}
$$

Status: `PROVABLE AS STATED` for (S1), unique maximality and the exact
constraint formula (S2). The latter is **not** advertised as an evaluated
all-target atlas: its remaining torus-linear-system count is classical
static work. The whole inverse calculation deducts diagonal scaling,
prescribed margins and finite-field nonzero-sum enumeration.

### Strategy and dependency map

Row normalization has uniform $(p-1)^2$ fibres. Reverse column scaling is
a linear margin equation. Count successful intermediate matrices by their
nonzero column sums; bound every nonsink inverse by the dimension of that
same linear system. No orbit classification is used.

### Proof

1. Every row-normalized intermediate matrix $B$ has both row sums $c\ne0$.
   Its original matrices are obtained by multiplying its two rows by
   arbitrary nonzero field scalars. These $(p-1)^2$ choices are distinct,
   since neither row is zero, and all normalize back to $B$.
2. A nonsink target has column sums 2. A column-normalized $Y$ has precisely
   the intermediates $B=Y\operatorname{diag}(v)$ with $v_j\ne0$ and
   $Yv=c\mathbf1_2$. Indeed column $j$ of $B$ then sums to $2v_j\ne0$,
   so its normalization returns column $j$ of $Y$. Conversely every
   successful predecessor has this form with $v_j$ its old column sum
   divided by 2. The column scalars are unique because every column of $Y$
   is nonzero. Step 1 now proves (S2).
3. To count all successful $B$, choose their nonzero column sums
   $w_1,\ldots,w_c$, which must satisfy $\sum w_j=2c\ne0$. Then choose
   the first row with sum $c$ in $p^{c-1}$ ways; the second row is uniquely
   $w$ minus the first and automatically has sum $c$.
   For a specified nonzero $s$, the elementary nonzero-sum count is

   $$N_c(s)=\frac{(p-1)^c-(-1)^c}{p}.$$

   For completeness, all nonzero target sums have the same count by
   scalar multiplication. If $A_c$ counts sum zero and $B_c$ counts one
   specified nonzero sum, then $A_c+(p-1)B_c=(p-1)^c$ and
   $A_{c+1}=(p-1)B_c$, starting with $A_1=0,B_1=1$. Substitution proves
   the displayed formula by induction. Therefore the successful original
   sources number $(p-1)^2p^{c-1}N_c(2c)$. Subtract this from all
   $p^{2c}+1$ states, including the sink itself, to obtain (S1).
4. Every $Y$ eligible for (S2) has rank at least one, because its column
   sums are nonzero. Thus its full affine solution set has size at most
   $p^{c-1}$, giving $|F^{-1}(Y)|\le(p-1)^2p^{c-1}$.
   Already the original matrices whose **first** row sum is zero give
   $p^{2c-1}$ sink predecessors. Since $c\ge2$,

   $$p^{2c-1}>(p-1)^2p^{c-1}.$$

   This proves strict maximality of the sink, including unreachable
   targets with zero fibre. No generic-rank assumption on $Y$ was made.

The case $c=1$ is deliberately outside this claim: its large nonsink fibre
can beat the sink. This is an explicit hypothesis of the theorem, not a
change to the original map or its two fixed $c=3$ pilot boxes.

### Temporal deduction and unresolved obligation

The classical diagonal-scaling chart in intake gives
$t'=cP(t)/P'(t)-t$. On a fixed two-row scaling orbit every nonsink
column-normalized state is represented by $t\in\mathbb F_p^*$, with some
parameters deleted by zero denominators. Thus the generic quotient-size
argument gives entrance at most $p$ and nonsink periods at most $p-1$.
This is a finite scalar-chart bound, not a classification or a new clock.

The original $p=5$ box has only fixed recurrence and maximum tail three;
$p=7$ already has 15 two-cycles and maximum tail four. The latter includes
the exact two-cycle $3541\leftrightarrow9404$ in row-major base-seven
encoding. No prime-uniform recurrent classification or untransferred sharp
temporal theorem is proved. Static (S1) does not repair that deficit.
Disposition: `NO_PROMOTION / KILL_INCOMPLETE_OR_TRANSFERRED_CONJUNCTION`.

## 2. RCI: all-parameter empty-fibre extremum under anisotropy

### Claim, assumptions and status

Use the exact intake RCI rule. Assume either $d=0$, or $d=1$ and $p$ is
any odd prime, or $d=2$ and $p\equiv3\pmod4$. Put $v=p^d$. Then empty
is the **unique** largest one-step fibre, of evaluated size

$$
E_{v,p}=v+\sum_{\substack{0\le j\le v\\p\mid j}}\binom vj.
\tag{I1}
$$

In particular $E_{p,p}=p+2$ on the line. For nonempty $Y$, put $k=|Y|$
and

$$
b_p(k)=\mathbf1_{p\nmid k}+\mathbf1_{p\nmid k+1}.
$$

Its exact inverse constraint is

$$
|I^{-1}(Y)|=b_p(k)\#\left\{g\in V\setminus Y:
 \sum_{y\in Y}\frac{y-g}{Q(y-g)}=0\right\}.
\tag{I2}
$$

On the line, if $P_Y(X)=\prod_{y\in Y}(X-y)$, this becomes

$$
|I^{-1}(Y)|=b_p(k)\#\{g\in\mathbb F_p:P_Y'(g)=0\}.
\tag{I3}
$$

Status: `PROVABLE AS STATED` for these inverse constraints and the evaluated
global maximum. An unevaluated derivative-root count is not labelled a
closed all-target enumeration. Ordinary inversion, centroid equations and
the logarithmic-derivative identity receive zero novelty credit. General
isotropic forms are not covered by this inverse theorem.

### Strategy and dependency map

Anisotropy makes inversion an involution off its center. Reconstruct each
source from its uniquely determined centroid and the optional center point.
This proves (I2); a polynomial degree bound on the line and a binomial
lower bound in the plane establish strict maximality. No temporal statement
beyond fixed-center inversion is used.

### Proof

1. In dimension one $Q(z)=0$ forces $z=0$. In the stated planes a nonzero
   isotropic $(a,b)$ would give $(a/b)^2=-1$ when $b\ne0$, impossible for
   $p\equiv3\pmod4$; when $b=0$ one has $a=0$. Thus in every stated
   positive dimension the only omitted vector is zero. For fixed $g$, the
   map $J_g(x)=g+(x-g)/Q(x-g)$ is an involution on $V\setminus\{g\}$:
   $Q((x-g)/Q(x-g))=Q(x-g)^{-1}$. It is therefore injective there.
2. Every source whose cardinality is divisible by $p$ maps to empty by
   definition. A nonempty source of other cardinality can map to empty only
   if it is contained in its singleton center, hence is a singleton. These
   $v$ singleton sources are disjoint from the cardinal-divisible sources.
   This proves (I1).
3. Let $Y\ne\varnothing$. Every predecessor $S$ has cardinality not
   divisible by $p$, so it has a unique centroid $g$. Injectivity implies
   $g\notin Y$ and forces exactly the two candidate sets

   $$S_0=J_g(Y),\qquad S_1=J_g(Y)\cup\{g\}.$$

   Their sizes are $k$ and $k+1$. For either allowed size, the condition
   that its centroid be $g$ is precisely
   $\sum_{y\in Y}(y-g)/Q(y-g)=0$; the optional center contributes zero.
   A size divisible by $p$ is disallowed because it would map to empty.
   Different centroids cannot describe the same allowed source, and the
   two choices at one centroid have different sizes. This proves (I2).
4. On the line, $(y-g)/Q(y-g)=1/(y-g)$. For $g\notin Y$ the usual product
   differentiation gives

   $$\frac{P_Y'(g)}{P_Y(g)}=\sum_{y\in Y}\frac1{g-y}.$$

   No root of $P_Y$ is a root of $P_Y'$, since the roots in $Y$ are distinct.
   Thus (I2) is equivalent to (I3). For $1\le k<p$, the derivative has
   degree $k-1$, so its root count is at most $\min(k-1,p-k)$. For $k=p$,
   $P_Y=X^p-X$ has derivative $-1$ and no roots. In all cases a nonempty
   fibre is at most $2\min(k-1,p-k)\le p-1$ (with the $k=p$ case zero),
   strictly less than the empty fibre $p+2$.
5. In the plane, (I2) gives at most $2(v-k)\le2(v-1)$ predecessors for
   any nonempty target. Since $v=p^2$ and $1\le p<v$, one has
   $\binom vp\ge v$: for example the $v$ cyclic intervals of length $p$
   in a fixed cyclic ordering are distinct subsets. Hence (I1) is at least
   $v+\binom vp+1\ge2v+1$, proving strict maximality. In dimension zero
   both available subsets map to empty, giving its unique maximum two.

### Actual obstruction to the naive temporal claim

Fixed-center involutivity was deducted before pilot, but the centroid is
not fixed during the full feedback. In the original line over $\mathbb F_{11}$
the following 22 distinct subset masks form a cycle:

```
95, 429, 190, 858, 380, 1716, 760, 1385, 1520, 723, 993,
1446, 1986, 845, 1925, 1690, 1803, 1333, 1559, 619, 1071, 1238.
```

After the last mask the map returns to 95. A mask selects point $i$ by its
$i$th binary bit. The same full box has eleven 20-cycles. This refutes an
unqualified period-at-most-two statement. Maximum tail two in that box
does not prove a height-two theorem for other primes. No all-parameter
core classification or untransferred clock is established.
Disposition: `NO_PROMOTION / HOLD_GLOBAL_TEMPORAL_PROOF`.

## 3. RRM: short-box periods do not close the all-n problem

The complete $n=3$ box has 174 fixed points and 41 two-cycles, maximum
tail six and a unique maximum fibre 136 at the left-projection table
$\mu(x,y)=x$ (encoding 377). The two-cycle $1053\leftrightarrow1066$
and the entrance path

```
1882 -> 1959 -> 1217 -> 1472 -> 731 -> 14 -> 2
```

are finite witnesses, not a proof of the general spectrum or height.

There is already an analytic all-n obstruction to extrapolating periods
one and two. On $X=\mathbb Z/5\mathbb Z$, the tables
$\mu_a(x,y)=x+a$ satisfy $F(\mu_a)=\mu_{2a}$. Consequently

$$\mu_1\longmapsto\mu_2\longmapsto\mu_4\longmapsto\mu_3
\longmapsto\mu_1$$

is an exact four-cycle. This is a deductive witness in the **already
deducted leftoid slice**, not an added $n=5$ pilot or an untransferred
discovery. More generally a leftoid with unary permutation $f$ obeys
$F^t(\mu)(x,y)=f^{2^t}(x)$.

The maximum-fibre target in the two nontrivial original boxes is left
projection, whose predecessors satisfy the familiar return identity
$(x*y)*x=x$. Their finite counts do not evaluate the all-n fibre or prove
its global maximality. General tables need not satisfy an associative law,
so no semigroup multiplication simplification may be inserted into RRM.
Disposition: `NO_PROMOTION / KILL_INCOMPLETE_GLOBAL_CONJUNCTION`.

## 4. Unexecuted desks and final boundary

DCS, TLS and DPM have complete analytic adapters in intake and remain
`DESK_KILL_GENERIC_DERIVED_SERIES`, `DESK_KILL_LINEAR_SUMMARY_ERASURE` and
`DESK_KILL_UNARY_POWER_PULLBACK`, respectively. No numerical result is
claimed on their carriers. The tempting P175 and crossed-Bin(X)-square
rules remain excluded before intake, not extra executed candidates.

The SNC and RCI inverse claims are pressure-checked by a new author
verification pair in the **same original boxes**, preserving the initial
pilot/pair. They do not constitute an admission conjunction, independent
review or a source-completeness certificate. All six literals close
`NO_PROMOTION`; no reserve, number, manuscript or next slate is created.
