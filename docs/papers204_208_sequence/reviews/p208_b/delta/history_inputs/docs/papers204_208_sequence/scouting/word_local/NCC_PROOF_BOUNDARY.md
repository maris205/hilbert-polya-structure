# NCC — partial static closure, temporal hold

Root author scout, 2026-09-06 UTC. **HOLD_PROOF / NO_ADMISSION**.
This is one unnumbered literal, not a reserve or a paper. The original
[intake](NCC_INTAKE.md) and [complete pilot stdout](NCC_CANONICAL.jsonl)
fix the full boxes $1\le n\le6$; no cutoff is enlarged here.

## Claim, status and assumptions

Let $n\ge1$, $X_n=\{1,\ldots,n\}^n$, and
$C(x)_i=\#\{j:|x_j-x_i|\le1\}$, with self included. Coordinates
are labelled particles, not cyclic sites. Write $m_a=\#\{i:x_i=a\}$,
with $m_0=m_{n+1}=0$ and $d_m(a)=m_{a-1}+m_a+m_{a+1}$.

The following fixed-point and constant-target fibre formulas are
`PROVABLE AS STATED`. A global entrance clock, a full recurrent
classification and the all-target maximum fibre are
`NOT CURRENTLY JUSTIFIED`. No finite census closes those claims.

## Strategy and dependency map

1. Equal old positions remain together; self inclusion proves invariance.
2. Subtract the equations at the upper end of an occupied run to
   exclude adjacent occupied positions at a fixed point.
3. Subtract equations at the lower end of an occupied run in a
   constant-target fibre to bound that run's length by two.
4. Ordered components, labelled allocations and integer gap counts
   enumerate those fibres. The arbitrary-target histogram sum is the
   previously used generic cohort adapter, with zero separate credit.

## Proof

### 1. Cohorts and fixed points

Self inclusion gives $1\le C(x)_i\le n$. If $x_i=x_j$, the two
neighbour sets agree, so $C(x)_i=C(x)_j$. Cohorts never split, but
the occupied positions need not be old positions; the old QHK
acyclic occupied-position proof therefore does not transfer.

Suppose $C(x)=x$. On every occupied position $a$ we have $d_m(a)=a$.
If a maximal occupied run ends at $b$ and has length at least two,
the equations at $b$ and $b-1$ give respectively

$$m_{b-1}+m_b=b,\qquad m_{b-2}+m_{b-1}+m_b=b-1.$$

Here $m_{b+1}=0$, including when $b=n$. Subtraction forces
$m_{b-2}=-1$, impossible. Thus occupied positions have pairwise
distance at least two. Their equations now reduce to $m_a=a$.
Conversely these conditions give $d_m(a)=a$ at every occupied
position and hence a fixed word. Consequently

$$|\operatorname{Fix}(C)|=
\sum_{\substack{S\subseteq\{1,\ldots,n\}\\
|a-b|\ge2\ (a\ne b\in S)\\\sum_{a\in S}a=n}}
\frac{n!}{\prod_{a\in S}a!}.$$

This is a separated-parts partition sum followed by labelled
multinomial allocation, not a distinct novelty axis.

### 2. Every constant-target fibre

Fix $q\in\{1,\ldots,n\}$. A source maps to $q^n$ exactly when
$d_m(a)=q$ at every occupied $a$. An occupied run of length at least
three, starting at $a$, would give

$$m_a+m_{a+1}=q,\qquad m_a+m_{a+1}+m_{a+2}=q,$$

forcing $m_{a+2}=0$. Hence each maximal occupied run has length one
or two, and its total mass is $q$. Conversely any collection of such
runs, separated by a zero site and each of mass $q$, maps to $q^n$.
In particular the fibre is empty unless $q\mid n$.

When $q\mid n$, put $k=n/q$. There are $k$ ordered components.
Choose $r$ to have length two in $\binom{k}{r}$ ways. They occupy
$k+r$ sites and require $k-1$ intervening zero sites. Distributing
the remaining $n-2k-r+1$ zeros among the two end gaps and the $k-1$
internal gaps gives $\binom{n-k-r+1}{k}$ placements. An impossible
placement contributes zero. Partition the $n$ labels among the
ordered components, each with $q$ labels, in $n!/(q!)^k$ ways.
In a two-site component the left site receives a nonempty proper
subset of its $q$ labels, giving $2^q-2$ choices independently.
These choices reconstruct every source uniquely. Therefore

$$|C^{-1}(q^n)|=\frac{n!}{(q!)^k}
\sum_{r=0}^{k}\binom{k}{r}\binom{n-k-r+1}{k}(2^q-2)^r,
\qquad k=n/q.$$

The convention is that $\binom{u}{k}=0$ for integer $u<k$ and
$0^0=1$. This includes $n=q=1$. Taking $q=n$ gives
$|C^{-1}(n^n)|=(n-1)2^n-n+2$: those sources have diameter at most
one. This target is **not** always a global maximizer. At the original
box $n=6$, its fibre is $316$, while $3^6$ has fibre $3800$.

### 3. Generic full-target decoder, deducted

For a target $y$, write $e_b=\#\{i:y_i=b\}$ and
$(d_*m)_b=\sum_{a:m_a>0,\ d_m(a)=b}m_a$. Then

$$|C^{-1}(y)|=
\sum_{\substack{m_1+\cdots+m_n=n\\m_a\ge0\\d_*m=e}}
\frac{\prod_b e_b!}{\prod_a m_a!}.$$

For each compatible histogram, partition the labels in each output
cohort among its old positions with the prescribed sizes. These
independent multinomial choices reconstruct each source exactly once;
different old histograms are disjoint cases. This is exactly the
QHK occupancy-pushforward adapter with $a_c$ replaced by $d_m$.
The complete original QHK proof, including its inverse and value
deduction, was read before making this deduction. The formula does
not evaluate the all-target maximum.

## Temporal evidence and open risks

The original complete pilots have maximum tails $0,1,2,3,4,4$ for
$n=1,\ldots,6$. Genuine labelled two-cycles already occur at $n=5$:

$$ (4,4,5,5,3)\longleftrightarrow(5,5,4,4,3). $$

Both states have the same histogram; the two mass-two cohorts swap.
At $n=6$ append a coordinate $1$ to obtain another two-cycle.
Thus histogram convergence, even if proved, would not establish
labelled convergence. No all-size period-two claim is made. Cohort
coarsening alone does not bound the time between mergers.

Bounded literal/source queries for neighbourhood-cardinality feedback,
unit-interval degree dynamics and count-based bounded confidence
returned nearby averaging/visibility/graph-rewiring literature, but
no exact primary body was established as this rule's owner. Those
queries are not a novelty clearance. The actual local QHK proof and
prior inventory/degree descriptions were read; their generic static
adapters are deducted here. No external contact or upload was made.
The missing temporal/extremal conjunction is sufficient for this hold;
a larger pilot or a new rule disguised as a guard is not a repair.
