# P215 proof package

## Claim, assumptions and status

**PROVABLE AS STATED.** The exact five claims are C1–C5 in
[CLAIMS.md](CLAIMS.md), matching the root's received theorem contract.
All variables $n,q$ are nonnegative integers; the carrier is
$X_{n,q}=\{0,\ldots,q\}^n$. For $n>0$,
$$F(x)_i=M_i-x_i,\qquad M_i=\max_{1\le j\le i}x_j.$$
The empty word is fixed. No coordinate permutation, wraparound or
postprocessing occurs. All coordinates stay between zero and $q$.

Set $x_0=0$, $d_i=x_i-x_{i-1}$. Delete zero differences, then compress
each same-sign block to one sign. The length of that sign word is $R(x)$.
It is zero exactly at the zero word, and otherwise starts with $+$.
Depth $h$ means first entrance to a recurrent state (a state on a cycle).

## Strategy and dependency map

1. Local prefix-maximum recurrence gives a scalar reflection identity.
2. Exact sign-run survival, including plateaus and saturation, gives C1.
3. The finite difference budget and alternating witness give C2.
4. Zero-started target blocks determine record heights, giving C3.
5. Reverse-complemented heights and first violation give C4.
6. Full-height inverse witnesses and strict multiset comparison give C5.

The temporal proof does not use the inverse enumeration. The inverse proof
does not assume the clock. No scientific observation is used in either.

## Proof

### 1. Reflection identity

Put $y=Fx$, $M_0=0$ and $y_0=0$. Then
$$y_i=\max(M_{i-1},x_i)-x_i
     =\max(y_{i-1}-d_i,0).$$
A zero $d_i$ leaves the output unchanged. A negative $d_i$ strictly
increases the output. A positive $d_i$ strictly decreases it when its
preceding value is positive, and otherwise leaves it zero.

### 2. Exact run decrement

Ignore zero input differences, which add only output plateaus. During
the first positive input run, the output starts and stays at zero.
Every negative input run supplies a nonempty strictly positive output
sign run. Every later positive input run follows a negative input run,
so its initial output value is positive. Its first step strictly
decreases that value. The remaining steps continue to decrease it until
zero, if attained, then leave it zero. Thus it supplies exactly one
nonempty negative output sign run.

Between any two positive output runs is the nonempty negative run from
the intervening positive input run. Between any two negative output runs
is the nonempty positive run from the intervening negative input run.
None can merge across these separators. This proves that the compressed
output sign word is the input sign word with its first $+$ removed and
all later signs reversed. Therefore $R(Fx)=R(x)-1$ for $x\ne0$.

Since $R(x)=0$ detects zero exactly, induction reaches zero after exactly
$R(x)$ steps. Zero is fixed and receives every orbit, excluding every
other recurrent state. This proves C1, including $h(0)=0$.

### 3. Sharp height and full equality set

There are $n$ differences, so $R(x)\le n$. Equality holds exactly when
none is zero and no consecutive signs are compressed, equivalently all
signs alternate. For $q>0$, $(q,0,q,0,\ldots)$ gives such a word.
For $n=0$ or $q=0$, the carrier is a singleton and has depth zero.
These statements prove C2 with every boundary and equality case.

### 4. Source bijection

Take $n>0$. The first coordinate of every output is zero, so a target
$y$ with $y_1\ne0$ has no source. Otherwise write its zero positions as
$1=z_1<\cdots<z_k$, and set $z_{k+1}=n+1$. Put
$$b_j=\max_{z_j\le i<z_{j+1}}y_i,\qquad
  B_j=\max_{r\le j}b_r.$$

If $Fx=y$, its running maximum can increase only when $y_i=0$, since
a new maximum equals $x_i$. It is therefore constant at some $L_j$ on
each displayed block. The heights are nondecreasing, at most $q$, and
$L_j\ge b_j$ by nonnegativity of $x_i$. The forced reconstruction is
$$x_i=L_j-y_i\quad(z_j\le i<z_{j+1}).$$
Nondecreasing heights satisfy $L_j\ge b_j$ exactly when $L_j\ge B_j$.

Conversely, given $0\le L_1\le\cdots\le L_k\le q$ and $L_j\ge B_j$,
the reconstruction lies in the carrier. Its value at $z_j$ is $L_j$;
all earlier values are at most $L_j$, and all other entries in that
block are less than $L_j$. Thus $L_j$ is its actual running maximum
throughout the block, proving $Fx=y$. The actual maxima recover the
heights uniquely. Taking every $L_j=q$ proves existence for every
target starting at zero. This proves C3.

### 5. Explicit evaluation

Set $c_i=q-B_{k+1-i}$ and $a_i=q-L_{k+1-i}$. Both sequences are
nondecreasing, and the source heights correspond exactly to
$0\le a_1\le\cdots\le a_k$ with $a_i\le c_i$.
Let $A_m$ count valid prefixes of length $m$ and $A_0=1$. Then
$$A_m=\binom{c_m+m}{m}
 -\sum_{i=1}^{m-1}A_{i-1}\binom{c_m-c_i+m-i}{m-i+1}.$$
Here $\binom{u}{v}=0$ for integers $v>u\ge0$.

To prove the formula, count first all nondecreasing length-$m$ sequences
in $\{0,\ldots,c_m\}$, giving the first binomial coefficient. Every
invalid sequence has a unique first violation $a_i>c_i$ with $i<m$.
Its valid prefix has $A_{i-1}$ choices and its suffix is any
nondecreasing length-$m-i+1$ sequence in $\{c_i+1,\ldots,c_m\}$.
That suffix has the displayed binomial count. For $i>1$ the prefix
ends at most at $c_{i-1}\le c_i$; for $i=1$ it is empty. Thus every
choice concatenates validly and has first violation exactly $i$.
Subtract the disjoint invalid classes and induct on $m$. This proves
the evaluation and $|F^{-1}(y)|=A_k$, giving C4. This first-violation
enumeration is a classical counting primitive, not a new general method.

### 6. Image and maximal fibre

The source bijection shows that the image is precisely $y_1=0$, so for
$n>0$ its size is $(q+1)^{n-1}$. At zero, $k=n$ and every barrier is
zero. All nondecreasing length-$n$ height sequences in $\{0,\ldots,q\}$
are allowed, giving $\binom{q+n}{n}$ predecessors. A nonzero image
target has $k<n$ and at most $\binom{q+k}{k}$ predecessors. For $q>0$
the latter bound is strictly smaller, since each increment of $k$
multiplies that count by $(q+k+1)/(k+1)>1$. Outside-image targets have
empty fibres. If $n=0$ or $q=0$, the sole state has its unique fibre
of size one. This proves C5.

## Corrections and open risks

No mathematical change to the admitted claims is made. The empty-prefix
case in the counting proof is explicit, so no undefined $c_0$ is needed.
The initial zero is essential in the clock statistic; counting only
differences internal to $x$ would be wrong for nonzero increasing words.

These are author proofs, not independent manuscript reviews or executions.
The source/ownership boundary is in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
Classical drawdown and barrier enumeration are credited. A later exact
clock owner or factor can reopen admission; a bounded non-hit is not a
priority certificate. No extension beyond the stated carrier or all-time
inverse theorem is implied.
