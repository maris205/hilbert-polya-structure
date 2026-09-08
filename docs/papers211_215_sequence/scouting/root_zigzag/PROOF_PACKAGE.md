# Greedy zigzag factor reversal — author proof package

2026-09-08 UTC. Author/proof contributor: root. This is not independent
review, admission, a paper or a novelty certificate.

## Claim and status

**PROVABLE AS STATED**, for the bounded claims explicitly stated below:
complete recurrent classification, a nonsharp Fibonacci transient bound,
and a bijection/finite dynamic program for every one-step target fibre.
The observed global maximum-fibre formula and any sharp transient formula
are **NOT CURRENTLY JUSTIFIED** and are not part of this contract.

## Assumptions and notation

Let $n\ge0$ and $x=x_1\cdots x_n\in S_n$. All entries are distinct. An
interval word is zigzag if consecutive comparison signs alternate; lengths
zero, one and two satisfy this condition. Factor $x$ from the left into
the longest available nonoverlapping zigzag prefixes $B_1,\ldots,B_k$.
Let $Z(x)$ reverse each $B_i$ and concatenate. This is the literal map in
INTAKE.md and pilot.py. Write $C(x)=(|B_1|,\ldots,|B_k|)$.
All nonfinal parts have length at least two; the final part is positive.
The empty factorization is reserved for $n=0$.

For distinct real numbers, define
$$\operatorname{Bet}(a;b,c)=[b<a<c\ \text{or}\ c<a<b].$$
Let $A_y(a,b)$ be the indicator that $y_a\cdots y_b$ is zigzag, for
$1\le a\le b\le n$. Let $F_1=F_2=1$ and
$F_n=F_{n-1}+F_{n-2}$ for $n\ge3$.

## Strategy and dependency map

1. Reversal preserves the zigzag language. The first changed greedy factor
   can only get longer, giving a lexicographic composition potential.
2. Unchanged cuts imply that the next reversal returns the entire word.
   This identifies all cycles without extrapolating the pilot.
3. A three-entry boundary test identifies precisely when cuts remain fixed.
4. The same explicit boundary calculation, now applied to arbitrary target
   cuts, reconstructs every source and proves uniqueness of its decoder.
5. A last-block recurrence counts these decoders. No source-permutation
   enumeration is used in the recurrence.

## Proof

### 1. Composition monotonicity

If $C(Zx)\ne C(x)$, then $C(Zx)>_{\rm lex} C(x)$.
Indeed, compare the first factors until their lengths first differ. All
earlier factors have equal lengths, so the next factor begins at the same
position in the old and new words. The reversal of the complete old factor
starting there is still zigzag and remains a prefix of the new unprocessed
suffix. The longest zigzag prefix chosen by the new algorithm is therefore
at least that long. At the first difference it is strictly longer. The two
compositions have the same sum, so neither can be a proper prefix of the
other. This proves the asserted lexicographic inequality.

If $C(Zx)=C(x)$, the exact same disjoint position intervals are reversed
twice. Hence $Z^2x=x$.

### 2. Complete recurrence and a nonsharp bound

A word $x$ is recurrent if and only if $C(Zx)=C(x)$. If the compositions
agree, the preceding involution identity makes it recurrent. Conversely,
along any periodic orbit the composition cannot increase strictly, because
it is nondecreasing in a finite total order. It is therefore constant and
in particular agrees in the first two epochs.

For $n\ge2$, the first factor has length at least two. Its reversal changes
the first entry, so $Zx\ne x$. Every recurrent point then has exact period
two. For $n=0,1$, the unique state is fixed.

Let $c_n$ be the number of compositions of $n$ whose nonfinal parts are at
least two. For $n\ge1$ the one-part composition contributes one, and
choosing a nonfinal first part gives
$$c_n=1+\sum_{j=2}^{n-1}c_{n-j}.$$
Thus $c_1=c_2=1$ and subtracting the formulas at $n$ and $n-1$ gives
$c_n=c_{n-1}+c_{n-2}$ for $n\ge3$. Hence $c_n=F_n$.
Every step before the first recurrent state strictly increases $C$.
The entrance time therefore satisfies $\tau(x)\le F_n-1$ for $n\ge1$;
it is zero for $n=0$. This bound is not claimed sharp. In particular, the
small-box height at $n=8$ is four, whereas this bound is twenty.

### 3. A local test for the recurrent core

Take the greedy factors of $x$. Suppose one factor occupies $[a,b]$ and
the next occupies $[b+1,c]$. The first has length at least two. After both
are reversed, the last two letters of the left factor are
$x_{a+1},x_a$, and the first letter of the right factor is $x_c$.
Extending the left factor by that letter fails the zigzag condition exactly
when these three letters are monotone, that is,
$$\operatorname{Bet}(x_a;x_{a+1},x_c)=1. \tag{R}$$
Every reversed factor remains zigzag. If (R) holds at every boundary,
greedy scanning ends each reversed factor at exactly its old endpoint,
in left-to-right order; hence the cuts agree. If the cuts agree, maximality
at each nonfinal factor forces (R). Together with Step 2 this is a complete
explicit recurrent membership test, including the one-factor case where
there are no boundary conditions.

### 4. Every one-step inverse

For a target $y\in S_n$, call cuts
$0=i_0<i_1<\cdots<i_k=n$ admissible if every segment is zigzag, every
nonfinal segment has length at least two, and for $1\le r<k$,
$$\operatorname{Bet}(y_{i_{r-1}+1};y_{i_{r-1}+2},y_{i_{r+1}})=1. \tag{I}$$
There is a bijection from these cuts to $Z^{-1}(y)$: reverse each target
segment and concatenate the resulting source.

For necessity, start with any source and its unique greedy factorization.
The target segments obtained by reversing its factors remain zigzag. At a
source boundary the last two letters of the left source factor and the
first of the next source factor are exactly the three target letters in
(I). The first pair has the same comparison sign as the boundary pair,
since the greedy source factor cannot extend. This proves (I).

For sufficiency, reconstruct the source from any admissible cuts. Each
source segment is zigzag by reversal invariance. Condition (I) makes its
extension by the first letter of the next segment fail. Consequently its
greedy factorization has exactly the chosen cuts, successively from left
to right. One update restores $y$. Distinct cut sequences cannot produce
the same source, since the greedy factorization of a source is unique.
The constructions are inverse, proving the bijection. At $n=0$ the empty
cut sequence gives the unique empty source.

### 5. A cubic-arithmetic every-target dynamic program

For $n\ge1$ define $D_y(a,b)$ on $1\le a\le b\le n$ by
$$D_y(1,b)=A_y(1,b),$$
and, when $a>1$,
$$D_y(a,b)=A_y(a,b)\sum_{h=1}^{a-2}
 D_y(h,a-1)\operatorname{Bet}(y_h;y_{h+1},y_b). \tag{D}$$
An empty sum is zero. Then
$$|Z^{-1}(y)|=\sum_{a=1}^n D_y(a,n). \tag{F}$$

To prove this, interpret $D_y(a,b)$ as the number of cut sequences ending
with the target block $[a,b]$, where all preceding blocks are nonfinal and
satisfy their boundary tests. A first block has one choice exactly when it
is zigzag. For a later block the preceding block is $[h,a-1]$ with
$h\le a-2$, which enforces its minimum length two. Its last boundary test
is precisely the indicator in (D). These choices are disjoint according to
$h$, proving the recurrence by induction in $b$. A length-one current block
may occur in this table, but it cannot be used as a preceding block in any
later transition. Thus it is admitted only as the final block, as required.
Summing over that block's start proves (F). The tests $A_y$ can be
precomputed by the positions of equal consecutive comparison signs. There
are $O(n^2)$ table entries and at most $n$ summands each, so the arithmetic
operation count is $O(n^3)$. No unit-cost integer bit-complexity claim is made.

## Corrections, subtraction and open risks

The temporal argument uses only the prefix-hereditary, reversal-invariant
language of legal factors and all-factor reversal. It does not use the
particular zigzag inequalities until the boundary test. It therefore gives
a general mechanism, and its mere short-period conclusion must not be
presented as unexplained rule-specific novelty. The inverse cut-bijection
framework is also generic; only the explicit three-letter constraints and
their compatibility structure can be considered as possible residual work.
There is currently no proof that these residuals meet the batch's value bar.

The all-target decoder and boundary tests have not yet received a new
bounded verifier or an independent proof check; the original pilot measured
literal graphs/indegrees but did not implement these later claims. The pilot
cannot be cited as having tested (R), (D) or (F). Affected bounded checks
are required if this contract survives desk subtraction.

The empirical maximum-fibre values are $1,1,1,2,3,5,7,11,15$ for
$n=0,\ldots,8$. The attractive proposed formulas for larger $n$ are not
proved, and neither is a sharp all-size clock. Source ownership and old
mechanism collision checks remain bounded, with external release held.
