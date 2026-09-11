# Prefix-period feedback: proof and negative disposition

Author: /root/round211_fresh_residual_scout. Date: 2026-09-09 UTC.
One explicit attempted literal is counted; none is promoted.
This is an author scout, not a manuscript, review, admission or novelty claim.

## Claim

Recomputed shortest-prefix-period-minus-one feedback on $E_n$ has exactly
the fixed points $z_1,\ldots,z_n$, reaches its endpoint within two updates,
and has the exact endpoint/depth and inverse formulas proved below.
Its entire one-step inverse problem is the old P134 border-array inverse
problem under a bijective output recoding. The proposed independent
inverse/extremal axis therefore fails despite different forward dynamics.

## Status

PROVABLE AS STATED for the displayed mathematical claims.
NO_PROMOTION / ONE_COUNTED_LITERAL / ZERO_PILOTS.
A materially independent two-axis paper is NOT CURRENTLY JUSTIFIED.

## Assumptions and notation

Fix any integer $n\geq1$, number positions from zero, and set

$$E_n=\{x\in\mathbb Z_{\geq0}^n:0\leq x_i\leq i\}.$$

Thus $x_0=0$ and $|E_n|=n!$. Letters are integers with their ordinary
equality; no standardization occurs between updates.

For a nonempty word $w$ of length $m$, an ordinary period is an integer
$p\in\{1,\ldots,m\}$ satisfying $w_j=w_{j+p}$ for $0\leq j<m-p$.
Its least period is $\operatorname{per}(w)$. Divisibility $p\mid m$ is
NOT required. Let $\beta_i(x)$ be the longest proper-border length of
$x_0\cdots x_i$, including the empty border of length zero.

The sole attempted literal is

$$F(x)_i=\operatorname{per}(x_0\cdots x_i)-1,\qquad 0\leq i<n.$$

Because $1\leq\operatorname{per}(x_0\cdots x_i)\leq i+1$, this defines
a synchronous finite autonomous deterministic self-map $F:E_n\to E_n$.
It is not descent along a fixed word's failure links.

Let $r(x)\in\{1,\ldots,n\}$ be the initial zero-run length and define

$$(z_r)_i=\begin{cases}0,&i<r,\\i,&i\geq r.\end{cases}$$

The second case is empty for $r=n$. Let
$\tau(x)=\min\{t\geq0:F^t(x)\text{ is recurrent}\}$.
The historical control is $B(x)_i=\beta_i(x)$ on exactly $E_n$, from
P134. The auxiliary recoding $C(y)_i=i-y_i$ is an involutive bijection
of $E_n$, not a second candidate literal.

## Proof strategy and dependency map

1. Ordinary border-period equivalence gives $F=C\circ B$ and every
   one-step fibre identity.
2. Period restriction proves monotonicity of the first image.
3. A nonconstant nondecreasing word is unbordered. This computes the
   second iterate and all recurrent states.
4. No zeros after the initial zero run characterizes direct entry;
   independent coordinate choices give the endpoint/depth distribution.
5. P134's actual fibre proof supplies the inherited extremum.
   Fixed-point counts disprove conjugacy.

## Proof

### 1. Exact output equivalence

For a length-$m$ word, the equalities defining a period $p$ say precisely
that its prefix and suffix of length $m-p$ agree. The empty border
corresponds to $p=m$. Minimizing $p$ gives

$$\operatorname{per}(w)=m-\text{length of the longest proper border of }w.$$

This credited relation also appears as the lemma min_per_len_diff in the
primary CoWBasic source identified in SOURCE_SUBTRACTION.md.
No theorem-prover execution is claimed. Coordinatewise it yields

$$F(x)_i=i-\beta_i(x),\qquad F=C\circ B.$$

Therefore, for EVERY target $y\in E_n$,

$$F^{-1}(y)=B^{-1}(Cy). \tag{1}$$

This is equality of subsets of the same source carrier, including empty
fibres of unrealizable targets. It is not a conjugacy assertion.

### 2. Monotone first image and invariant initial run

Let $a_m$ be the least period of $x_0\cdots x_{m-1}$.
If $a_{m+1}\leq m$, restriction of the period equalities to the first
$m$ letters gives $a_m\leq a_{m+1}$. If $a_{m+1}=m+1$, the inequality
follows from $a_m\leq m$. Thus $F(x)$ is nondecreasing.

A prefix has period one exactly when all its letters agree. Because its
first letter is zero, these are precisely the prefixes within the initial
zero run. Hence

$$r(F(x))=r(x). \tag{2}$$

### 3. Exact second iterate and complete recurrent atlas

If a length-$m$ nondecreasing word has a nonempty proper border, Step 1
gives a period $p<m$. For every $0\leq j<m-p$, equality of the endpoints
$y_j=y_{j+p}$ forces all entries on $[j,j+p]$ equal by monotonicity.
These consecutive overlapping intervals cover $[0,m-1]$, so the whole
word is constant. Conversely, a constant word has least period one.

For nondecreasing $y\in E_n$ with initial zero-run length $r$, the prefixes
inside that run have period one, and every later prefix has full length
as its least period. Thus $F(y)=z_r$. Applying Step 2 gives

$$F^2(x)=z_{r(x)},\quad F(z_r)=z_r,\quad
F^t(x)=z_{r(x)}\quad(t\geq2). \tag{3}$$

The $n$ templates are distinct and fixed. A recurrent state lies on a
cycle, but (3) places it at a fixed point within two updates. That cycle
must be the fixed singleton. Therefore $z_1,\ldots,z_n$ are ALL recurrent
states, with no nontrivial cycles.

### 4. Exact pointwise depth and sharp maximum

Equation (3) gives

$$
\tau(x)=
\begin{cases}
0,&x=z_{r(x)},\\
1,&x\ne z_{r(x)}\text{ and }F(x)=z_{r(x)},\\
2,&F(x)\ne z_{r(x)}.
\end{cases} \tag{4}
$$

The direct-entry condition has a coordinate characterization:

$$F(x)=z_{r(x)}
\Longleftrightarrow x_i\ne0\text{ for all }i\geq r(x). \tag{5}$$

For necessity, a zero at $j\geq r$ makes the prefix ending there have
a length-one border. Then $F(x)_j<j=(z_r)_j$.

For sufficiency, suppose all letters after the initial zero run are
nonzero. Inside the run $\beta_i(x)=i$. Consider a later prefix.
A border of length at most $r$ ends in zero in its prefix copy, whereas
the suffix copy ends in a nonzero letter. A border longer than $r$ has
a suffix copy starting at a positive position $s$. If $s\geq r$, its
first letter disagrees with zero. If $0<s<r$, its initial zero run has
length $r-s$, shorter than the prefix copy's $r$ zeros, so the copies
disagree at the next position within the alleged border. No later prefix
has a nonempty border. This proves (5).

For $n=1$ the sole state is fixed. For $n=2$ both $(0,0)$ and $(0,1)$
are fixed. For every $n\geq3$ the valid state

$$x=(0,1,0,3,4,\ldots,n-1)$$

has a zero after its initial zero run, and (4)-(5) give depth two.
The tail is empty at $n=3$. Hence

$$\max_{x\in E_n}\tau(x)=
\begin{cases}0,&n\leq2,\\2,&n\geq3.\end{cases} \tag{6}$$

### 5. Endpoint-resolved depth counts and every later fibre

For $1\leq r<n$, put

$$a_r=\prod_{i=r}^{n-1}i=\frac{(n-1)!}{(r-1)!},\qquad
b_r=r\prod_{i=r+1}^{n-1}(i+1)=\frac{r\,n!}{(r+1)!}.$$

Set $a_n=b_n=1$. By (2) every source of $z_r$ has initial zero-run
length $r$. By (5), each remaining coordinate $i$ is independently
chosen from $\{1,\ldots,i\}$, so $|F^{-1}(z_r)|=a_r$.

All states ending at $z_r$ have that initial zero-run length. For $r<n$,
coordinate $r$ has $r$ nonzero choices; every later coordinate $i$ has
its full $i+1$ choices. This basin has $b_r$ elements. At $r=n$ it
contains only the all-zero state. There is one depth-zero state,
$a_r-1$ depth-one states and $b_r-a_r$ depth-two states. Consequently

$$\sum_{x:\,r(x)=r}u^{\tau(x)}
=1+(a_r-1)u+(b_r-a_r)u^2. \tag{7}$$

At time zero each target fibre is a singleton. At time one fibres are
exactly (1). At every $t\geq2$, the fibre of $z_r$ is
$\{x:r(x)=r\}$, of size $b_r$, and every other target has empty fibre.
These all-time formulas require no finite enumeration.

### 6. Inherited inverse/extremal mechanism and failure of conjugacy

The actual P134 proof bounds every $B$-fibre by $(n-1)!$ and, for
$n\geq2$, attains equality exactly at $0^n$ and
$A_1=(0,1,0,\ldots,0)$. Its left-to-right source exposure forces at most
one source letter for a positive target border, while a zero border
excludes the source letter zero and leaves at most $i$ choices at position
$i$. Equality permits no positive target after position one; both
remaining targets attain the product. This is already-owned argument
and equality data, not new proof credit.

Because $C(0^n)=z_1$ and $C(A_1)=z_2$, identity (1) transports it:

$$|F^{-1}(y)|\leq(n-1)!,\qquad
|F^{-1}(y)|=(n-1)!\Longleftrightarrow y\in\{z_1,z_2\}
\quad(n\geq2). \tag{8}$$

At $n=1$ the only fibre has size one. More generally (1) transports
every one-step realization, image and inverse-description question,
so a different target statistic does not create an independent inverse
mechanism.

Forward dynamics are different: P134 proves that $B$ has only exact
two-cycles and no fixed points for $n\geq2$, while Step 3 gives $n$ fixed
points for $F$. A conjugacy bijection must preserve fixed points.
Therefore $F$ and $B$ are not conjugate for $n\geq2$, under $C$ or under
any bijection. At $n=1$ both are the singleton identity.
Equations (1)-(8), including all boundaries, complete the proof. ∎

## Corrections or missing assumptions

No correction to the stated literal is needed. Ordinary period must not
be replaced by shortest exact repetition-root length. Output equivalence
must not be rewritten as conjugacy.

## Open risks and disposition

These are author deductions, not an independent review or machine-certified
contract. No scientific program, pilot, exhaustive test, interpreter,
theorem prover, build or PDF viewing was performed.
The source search is bounded and does not establish global novelty.
The exact time spine survives, but all one-step inverse/extremal machinery
is inherited and the later fibres are direct initial-run coordinate counts.
No materially independent second mechanism survives. Reject before pilot;
do not add an artificial second literal or enlarge a cutoff.
