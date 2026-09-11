# FRI: author proof package, not an admission verdict

## Claim, assumptions and status

Fix $q,n\ge1$ and let $W_{q,n}=\{0,\ldots,q-1\}^n$. Positions start at
zero. If $w=a u a v$ and $u$ avoids $a$, define $F(w)=u a a v$.
If the first letter $a$ has no other occurrence, define $F(a u)=u a$.
In particular every length-one word is fixed. No relabelling or quotient
is made; length and every letter multiplicity are preserved.

The exact pointwise entrance clock, recurrent set and period, every-target
one-step decoder, and sharp maximum fibre below are
**PROVABLE AS STATED** by the author. They are not independent review,
novelty or sufficient residual-value findings. The prospective broader
fibre polynomial was deliberately not developed after root's scope decision.

For a finite self-map, $\tau(w)$ is the least $t\ge0$ such that $F^t(w)$
belongs to a cycle. Let $r(w)$ be the least index $r\ge1$ with
$w_r\in\{w_0,\ldots,w_{r-1}\}$, when there is one.

## Strategy and dependency map

1. Track individually distinguishable original occurrences until the first
   repeated-letter position; previously processed letters cannot re-enter
   the unprocessed distinct prefix. This proves the pointwise clock.
2. Use the clock and the direct rotation rule on all-distinct words to
   identify every recurrent state and its exact period.
3. Independently remove a first occurrence of an adjacent equal pair in the
   target, or remove its unique last letter. These are all and only parents.
4. Count the disjoint letter resources consumed by the decoder and exhibit
   words attaining the resource bound. No temporal theorem is used in steps
   3–4. Mathematical independence of these proofs does not establish two
   residual contributions after known primitives have been deducted.

## 1. Pointwise clock and complete recurrence

**Theorem.** If all $n$ letters of $w$ are distinct, then $\tau(w)=0$ and
the exact period is $n$. Otherwise $n\ge2$, $r=r(w)$ exists, and

$$
\tau(w)=\begin{cases}
r-1,&w_{r-1}=w_r,\\
r,&w_{r-1}\ne w_r.
\end{cases}
$$

Every word with a repeated letter ends at a fixed word whose first two
letters agree. Conversely every such word is fixed. Thus for $n\ge2$ the
recurrent set is precisely the disjoint union of the all-distinct words
and the first-two-equal words. At $n=1$ all $q$ words are fixed.

**Proof.** If every letter occurs once, every update is left rotation by
one. Distinct letters give $n$ different rotations, including the
length-one boundary. This proves the first assertion.

Now suppose $r$ exists. The original occurrences in positions
$0,\ldots,r-1$ have pairwise distinct labels. Any one of these occurrences,
when processed at the front, is either moved to immediately before an
original occurrence at position at least $r$, or, if its label is globally
unique, to the end. An occurrence with the same label cannot have been
inserted earlier: all previously processed labels are different. Therefore,
after $t$ updates for $0\le t\le r-1$, the front original occurrence is
$w_t$ and the still-unprocessed original occurrences
$w_t,\ldots,w_{r-1}$ retain their consecutive order in front of all inserted
occurrences. In particular for $t\le r-2$, the first two letters are
$w_t\ne w_{t+1}$, so the word is not fixed.

If $w_{r-1}=w_r=a$, no previously processed prefix letter is $a$.
At time $r-1$ the original pair $w_{r-1}w_r=aa$ is at the front with
no inserted occurrence between it. Hence the state is fixed at that time.
If $w_{r-1}\ne w_r=a$, the first occurrence of $a$ lies in positions
$0,\ldots,r-2$ and has already been inserted immediately before old $w_r$.
At time $r-1$ the front consists of $w_{r-1}aa$. The next update removes
$w_{r-1}$ and places it later, since its label is not $a$, exposing $aa$.
The state first becomes fixed at time $r$.

For $n\ge2$, the rule fixes exactly the first-two-equal words: when the
first two letters differ, the output first letter is the old second
letter and therefore differs from the old first letter. We have proved
finite convergence to that fixed set for every word with any repetition,
so there are no other cycles in that part of the carrier. This proves the
claimed entrance times as well as recurrence. $\square$

**Sharp height.** If $q=1$ or $n\le2$, every state is recurrent and the
height is zero. For $q\ge2$ and $n\ge3$ the height is

$$H(q,n)=\min\{q,n-1\}.$$

Indeed $r\le q$ and $r\le n-1$ prove the upper bound. Put
$h=\min(q,n-1)\ge2$ and take a word beginning
$0,1,\ldots,h-1,0$, completing its length arbitrarily. Its first repeat is
at index $h$ and is not an adjacent repeat, so its clock is $h$.

## 2. Every-target inverse decoder

For a target $y=y_0\cdots y_{n-1}$ and an occurring label $a$, let
$j_a=\min\{j:y_j=a\}$. Define

$$D(y)=\{a:j_a<n-1\ \text{and}\ y_{j_a+1}=a\},\qquad
s(y)=\mathbf1\{|\{j:y_j=y_{n-1}\}|=1\}.$$

For each $a\in D(y)$, delete occurrence $y_{j_a}$ and prepend $a$;
denote the resulting word by $p_a(y)$. If $s(y)=1$, also delete the final
letter and prepend it; denote that word by $p_*(y)$.

**Theorem.** These words are pairwise distinct and are exactly $F^{-1}(y)$.
In particular

$$|F^{-1}(y)|=|D(y)|+s(y),$$

including zero fibres and the length-one boundary.

**Proof.** Let a parent begin with $a$. If it has a second $a$, write it
$a u a v$ with $u$ avoiding $a$. Its image is $u a a v$. Therefore the
first target occurrence of $a$ begins a double, and deleting that first
occurrence and prepending it recovers the parent. If the parent has no
second $a$, its image ends in its only $a$, and the second decoder branch
recovers it. These cases prove necessity and exhaust all parents.

Conversely, for $a\in D(y)$ the word preceding $y_{j_a}$ avoids $a$.
Consequently $p_a(y)$ has the prescribed first-return factorization and
maps back to $y$. If $s(y)=1$, the singleton first letter of $p_*(y)$
rotates to the end and also gives $y$. Different double-decoder labels
give different first letters, hence different parents. The singleton
branch has a globally unique first letter and is disjoint from them.
For $n=1$ there is no double branch and the singleton branch returns the
same one-letter word. $\square$

## 3. Sharp fibre maximum

**Theorem.** For all $q,n\ge1$,

$$\max_{y\in W_{q,n}}|F^{-1}(y)|=\min\{q,\lceil n/2\rceil\}.$$

**Proof.** Write $c=|D(y)|$ and $s=s(y)$. Each of the $c$ double-decoder
labels uses at least two positions. If $s=1$, its label is distinct and
uses another position. Thus $2c+s\le n$ and $c+s\le q$. Since
$s\in\{0,1\}$, these inequalities imply
$c+s\le\min(q,\lceil n/2\rceil)$.

Let $m=\min(q,\lceil n/2\rceil)$. If $2m\le n$, take a word beginning
with $m$ different doubled labels and fill every remaining position with
the first of these labels. All $m$ labels lie in $D(y)$, so the upper
bound is attained. Otherwise $n=2m-1$. Take $m-1$ different doubled labels
followed by one further, singleton label. This has $c=m-1$, $s=1$ and
attains $m$. This construction also covers $n=1$, where the doubled
prefix is empty. $\square$

## 4. Exact direct-owner adapter

Let $J$ reverse a word, $a=z_{n-1}$ and $m_a$ be the total number of $a$'s
in $z$. Ayyer–Schilling–Steinberg–Thiéry define $\partial_{a,j}$ in
Section 6.1, equation (6.1), of [arXiv:1401.4250v4](https://arxiv.org/pdf/1401.4250v4):
it moves the $j$th $a$ next to its previous copy, or to the front when
$j=1$. On every fixed-content class,

$$J F J(z)=\partial_{a,m_a}(z),\qquad a=z_{n-1}.$$

To check the identity, write $z=v^{\rm rev}a u^{\rm rev}a$ where $u$
avoids $a$. Both sides yield $v^{\rm rev}aa u^{\rm rev}$. If $a$ is
unique, both put it at the front. Thus this is an exact state-selected
known-generator representation, including the singleton branch, not
merely similar notation. The selection of the current last letter is
state-dependent; no fixed probability vector or fixed generator is asserted
to equal the full FRI map. The local movement earns zero credit.

Brualdi–Dahl's [2024 primary article](https://link.springer.com/article/10.1007/s00373-024-02751-2),
immediately before Theorem 8, separately defines right-joins on
2-permutations. On a first-letter pair this is exactly $a u a v\mapsto
u a a v$; the placement before/after the identical copy gives the same
unlabelled-letter word. That primitive is also already subtracted in P199.

## Verification scope and open risks

The single pilot checks the pointwise clock, exact period, full parent sets,
height and maximum fibre on all 24 boxes $1\le q\le4$, $1\le n\le6$:
6,684 states and 20,124 assertions. It is one author run, not independent
review or strict terminal reuse. Proofs above do not depend on those boxes.

The outstanding gate is residual value and historical/source subtraction,
not an asserted unproved global clock. P185 already uses the all-distinct
prefix statistic; P192 already uses a strictly advancing first-collision
schedule; P199 and the two direct sources own join primitives. The decoder
is a short reversal of those primitives. Root expressly suspects that
first-repeat stopping plus this local inverse is too thin for two residual
axes. No extra polynomial, larger experiment or numbered manuscript is
used to compensate. The appropriate next action is a fresh noncontributor's
bounded value judgment, or closure, not admission by the author.
