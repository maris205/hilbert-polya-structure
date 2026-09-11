# Proof Package — previous-smaller distances (NS)

Author: root, 2026-09-05. P204 author theorem contract; candidate gate passed, manuscript reviews pending.

## Claim and status

**PROVABLE AS STATED** for the contract below. The independent candidate
proof/source/value gate passed narrowly; formal manuscript reviews remain due. No originality or external release is asserted.

For $n\ge1$, let $E_n=\{x:x_0=0,\ 0\le x_i\le i\ (1\le i<n)\}$.
Define the synchronous map
$$P(x)_i=\begin{cases}
i-\max\{h<i:x_h<x_i\},&\text{if the set is nonempty},\\
0,&\text{otherwise}.
\end{cases}$$

The zero positions of $x$ are fixed under $P$. Write each maximal positive
block as positions $r+1,\ldots,r+m$, immediately following a zero at $r$.
Define the core $\mathcal C_n$ to consist of words whose entries in every
such block are one at its first position and belong to $\{1,j\}$ at its
$j$-th position, for $2\le j\le m$.

1. $P^2(E_n)=\mathcal C_n$, and on the core $P$ interchanges $1$ and $j$
   independently at every local index $j\ge2$, keeping all zeros and
   block starts fixed. Thus $P^4=P^2$, the core is exactly the recurrent
   set, and every period divides two. The maximum entrance time is zero
   for $n\le2$, one for $n=3$, and two for $n\ge4$.
2. With Fibonacci numbers $F_0=0,F_1=1$, the recurrent count is
   $F_{2n-1}$ and the fixed count is $F_{n+1}$. The number of strict
   two-cycles is $(F_{2n-1}-F_{n+1})/2$.
3. Every target fibre at every time $t\ge2$ is given by the explicit
   alternating-cut product below. Noncore targets have zero fibre.

For a core target $y$ and a positive block at $r+1,\ldots,r+m$, put
$$A_t(y;r,m)=\begin{cases}
\{j\in\{2,\ldots,m\}:y_{r+j}=j\},&t\text{ even},\\
\{j\in\{2,\ldots,m\}:y_{r+j}=1\},&t\text{ odd}.
\end{cases}$$
For $A\subseteq\{2,\ldots,m\}$ define
$$D_{r,m}(A)=
\sum_{B\subseteq A}(-1)^{|A|-|B|}
\prod_{[a,b]\in\operatorname{Seg}(B)}
\binom{r+b}{b-a+1},$$
where $\operatorname{Seg}(B)$ is the partition of $\{1,\ldots,m\}$
cut immediately before each $j\in B$. An empty product is one.
Then
$$|(P^t)^{-1}(y)|=
\prod_{\text{positive blocks }(r,m)\text{ of }y}D_{r,m}(A_t(y;r,m)).$$

## Assumptions and notation

The entries are compared by their usual integer order. Distances are
recomputed from the previous entire word, not followed as pointers. The
carrier is the standard inversion-sequence box; this statement does not
silently extend to arbitrary words with a nonzero first letter.
For $x$ with a fixed positive block, its internal ascent set is
$\{j\ge2:x_{r+j-1}<x_{r+j}\}$. Core coordinates use the local index $j$,
whereas the initial upper bound at that position is the global index $r+j$.

## Strategy and dependency map

Zero barriers split the dynamics into blocks. A previous-smaller index
lemma forces every first-image block entry to be either one or larger than
its predecessor. Its next image is therefore a Boolean choice between one
and its local index. The inverse axis decodes that choice as the original
ascent set, and counts bounded source words using an alternating sum of
weakly decreasing segments.

1. Zero barriers and the nearest-smaller inequality imply the two-step core.
2. The core involution gives recurrence and the sharp small-size clock.
3. A weighted two-state word count gives the recurrent census.
4. The original ascent mask determines the even-time endpoint.
5. Inclusion--exclusion over missing required ascents evaluates each fibre.

## Proof

### 1. Barriers and a first-image inequality

If $x_i=0$, there is no smaller nonnegative entry and $P(x)_i=0$.
If $x_i>0$, the entry $x_0=0$ is smaller, so $P(x)_i>0$.
Thus the zero set is invariant. In a positive block following position $r$,
the nearest smaller predecessor is at least $r$, so its output distance at
position $r+j$ lies in $\{1,\ldots,j\}$. Earlier blocks have no influence.

Let $b_j=P(x)_{r+j}$ and let $p_j$ be the nearest smaller predecessor of
$x_{r+j}$. At $j\ge2$, if $b_j>1$, then
$x_{r+j}\le x_{r+j-1}$. Every position after $p_{j-1}$ and before $r+j-1$
has value at least $x_{r+j-1}$, hence at least $x_{r+j}$; the position
$r+j-1$ also is not smaller than $x_{r+j}$. Consequently
$p_j\le p_{j-1}$ and
$$b_j=(r+j)-p_j\ge(r+j)-p_{j-1}=b_{j-1}+1.$$
Every first-image entry therefore is either one or strictly exceeds its
predecessor.

### 2. The second image and the core action

If $b_j=1$, the only smaller value in its block and left barrier is zero,
so $P(b)_{r+j}=j$. If $b_j>1$, Step 1 gives $b_{j-1}<b_j$, so the
nearest smaller predecessor is immediately adjacent and $P(b)_{r+j}=1$.
The first block entry always remains one. This proves $P^2(x)\in\mathcal C_n$.

Conversely, at a core coordinate with value $j\ge2$, every preceding
core entry in the block is at most $j-1$, so the nearest smaller predecessor
is adjacent and the next value is one. At a core coordinate with value one,
the nearest smaller predecessor is the left zero barrier and the next value
is $j$. Hence $P$ acts as the claimed involution $J$ on $\mathcal C_n$.
Every core word is its own two-step preimage, giving
$P^2(E_n)=\mathcal C_n$ and $P^4=P^2$. A periodic state must lie in the
second image, so this is exactly the recurrent set.

The carriers at $n=1,2$ consist only of fixed core words. At $n=3$, the
six carrier states are $000,001,002,010,011,012$. Only $002$ lies outside
the core, and it maps to $001$, proving height one.
For $n\ge4$, prepend $n-4$ zeros to $(0,1,2,2)$. Its first-image positive
block is $(1,1,2)$, whose last entry is neither one nor three, so that
image is not recurrent. Its second image is core. Thus height two is sharp.

### 3. Exact recurrent and fixed counts

For the $N=n-1$ positions after the initial zero, let $a_N$ and $b_N$
count core words ending in zero and a positive entry respectively, with
$(a_0,b_0)=(1,0)$. Appending a zero has one choice from either state.
Starting a positive block after a zero has one choice, namely one.
Continuing a positive block has two distinct choices, one and its new
local index. Therefore
$$a_{N+1}=a_N+b_N,\qquad b_{N+1}=a_N+2b_N.$$
By induction $(a_N,b_N)=(F_{2N-1},F_{2N})$ for $N\ge1$, or directly
the total has initial values $1,2$ and recurrence
$r_{N+2}=3r_{N+1}-r_N$. Thus $r_N=F_{2N+1}=F_{2n-1}$.

A core word is fixed exactly when it has no positive block of length at
least two. All its positive values then equal one. Binary words of length
$N$ avoiding consecutive ones have $F_{N+2}=F_{n+1}$ possibilities,
by conditioning on whether they start with zero or with $10$ (and checking
$N=0,1$). Every other recurrent point is paired by $J$, proving the
cycle census.

### 4. The even endpoint records exactly the original ascent mask

For $j\ge2$ in a positive source block, $b_j=1$ if and only if
$x_{r+j-1}<x_{r+j}$. Step 2 therefore gives
$$P^2(x)_{r+j}=\begin{cases}
j,&x_{r+j-1}<x_{r+j},\\
1,&x_{r+j-1}\ge x_{r+j}.
\end{cases}$$
At every time $t\ge2$, $P^t(x)=J^{t-2}P^2(x)$.
The zero set is preserved, so a source of a fixed target $y$ must have
exactly its zero set. The internal source ascent set in a target block
must be $A_t(y;r,m)$, and this condition is also sufficient.

### 5. Count all bounded words with an exact internal ascent set

Fix a positive block and an exact required ascent set $A$. Its source
entries obey $1\le x_{r+j}\le r+j$. Initially impose nonascent on all
internal edges outside $A$. Inclusion--exclusion over the failures of
the required ascents says that the count is the alternating sum, over
$B\subseteq A$, of words allowed to ascend only at edges in $B$.
Those words split into independent weakly decreasing segments
$[a,b]\in\operatorname{Seg}(B)$.

In such a segment, every entry is at most its first entry, which is at
most $r+a$. Conversely, any weakly decreasing sequence of length
$b-a+1$ drawn from $\{1,\ldots,r+a\}$ satisfies all position bounds,
since subsequent bounds only increase. Its count by multiplicities is
$$\binom{(r+a)+(b-a+1)-1}{b-a+1}
=\binom{r+b}{b-a+1}.$$
Multiplying over segments and applying the indicated signs yields
$D_{r,m}(A)$. Positive blocks are independent and all intervening source
zeros are forced, proving the complete time-$t$ formula. The all-zero
target has exactly one source at every positive time, as the empty product
also records.

## Corrections or missing assumptions

An initial Fibonacci component indexing slip was corrected before
verification: at $N=1$ both components must be one.
There is no claim here that the first image equals all arrays satisfying
the one-or-rise inequality; only necessity is needed and proved.
No exact formula for the one-step fibre, no first-image census, and no
largest-fibre classification is asserted.

## Open risks

The candidate-stage primary-source and collision audit is complete in the
linked batch's NS_GATE report and is developed in SOURCE_AUDIT.md here.
Those static ingredients receive zero credit. The independent candidate
decision retained the narrow two-step endpoint/ascent interface and flagged
fibre conjunction after the P134/P185 subtractions. Global ownership remains
uncertified and any located exact owner reopens the affected gate. This is
an author proof package, not either accepted manuscript review.
