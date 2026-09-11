# Suffix-array feedback: complete elementary negative certificate

## Claim

Fix $n\ge1$. On $X_n=[n]^n$, let $T$ replace a word by its ordinary
suffix-array permutation, with positions and output letters both labelled
by $[n]=\{1,\ldots,n\}$. Then:

1. $T(X_n)=S_n$, $T(p)=p^{-1}$ for every $p\in S_n$, and $T^3=T$.
   The recurrent set is exactly $S_n$. Its fixed points are the
   involutions; all other recurrent points have period two.
2. Every permutation has entry time zero, and every other word has entry
   time one. The maximum is zero for $n=1$ and one for $n\ge2$.
3. Every target fibre is described by the decoder in Step 3 and counted
   in Step 4. The unique maximum-fibre target is the decreasing permutation.

This is a bounded author certificate for a negative admission decision,
not a statement of new theorem priority.

## Status

**PROVABLE AS STATED.**

A materially new two-axis paper is **NOT CURRENTLY JUSTIFIED**:
the temporal mechanism is first-image inversion and the inverse mechanism
is the directly owned suffix-array decoder/count.

## Assumptions

Words are finite sequences of integer letters with their ordinary total
order. Suffixes are ordered lexicographically, with a proper prefix
smaller than the longer word. All $n$ nonempty suffixes are used. There
is no appended sentinel in the update, cyclic rotation sorting, alphabet
standardization between steps, or tie-breaking ambiguity: two different
suffixes have different lengths and cannot be identical words.

## Notation

For $w=w_1\cdots w_n$, the permutation $p=T(w)$ satisfies
$$
w_{p_1}\cdots w_n < w_{p_2}\cdots w_n < \cdots <
w_{p_n}\cdots w_n.
$$
Permutations are identified with their one-line words in $X_n$.
For a target $p\in S_n$, define $r(i)=p^{-1}(i)$ for $1\le i\le n$
and add the convention $r(n+1)=0$. Define the set of forced strict gaps
$$
D(p)=\{j\in\{1,\ldots,n-1\}:r(p_j+1)>r(p_{j+1}+1)\},
\qquad d(p)=|D(p)|.
$$
The added rank zero belongs only to the empty suffix; it is a proof
device, not a state letter or an extra evolving coordinate.

## Proof strategy

First use the distinct first letters on a permutation word. Separately,
reconstruct an arbitrary source by assigning its letters in the target's
prescribed suffix order. Equal letters must be followed by tails in that
same order, giving the forced strict gaps and a weak-composition count.

## Dependency map

1. Distinct first letters prove the permutation inverse identity and image.
2. That identity proves recurrence, periods and entry times.
3. Recursive lexicographic comparison proves the complete target decoder.
4. Removing forced rises gives the fibre count; the unary-word case gives
   the unique extremal target.
5. The primary characterization and old standardization control subtract
   the inverse mechanism without asserting equal forward dynamics.

## Proof

### Step 1. Image and dynamics on the image

Every output is a permutation by definition. If the input $p$ is already
a permutation word, the first letters of its suffixes are distinct.
Their lexicographic ordering is therefore determined at the first letter:
the $i$-th smallest suffix starts at the position containing the letter $i$.
That position is $p^{-1}(i)$, so $T(p)=p^{-1}$.

For every target permutation $p$, the source word $p^{-1}$ maps to $p$.
Thus the image is all of $S_n$, not a proper subset. Writing $p=T(w)$
for an arbitrary input gives
$$
T(w)=p,\qquad T^2(w)=p^{-1},\qquad T^3(w)=p.
$$
Hence $T^3=T$ on the entire carrier.

### Step 2. Recurrent set and exact clock

Every recurrent point of a self-map belongs to its image, so here it
belongs to $S_n$. Every point of $S_n$ is recurrent by Step 1.
A permutation is fixed precisely when it equals its inverse, equivalently
when its square is the identity. Every remaining permutation is exchanged
with its distinct inverse and has period two.

A nonpermutation cannot be recurrent and enters $S_n$ after exactly one
step. This proves the pointwise entry-time statement. For $n=1$ there is
only one word. For $n\ge2$, the word $1^n$ is not a permutation, proving
that the maximum entry time one is attained. For $n\ge3$, the two
permutations $(2,3,1,4,\ldots,n)$ and $(3,1,2,4,\ldots,n)$ provide a
symbolic strict two-cycle; no finite computation is being reported.

### Step 3. Complete every-target decoder

A nonpermutation target has empty fibre by Step 1. Fix $p\in S_n$.
Given a proposed source $w$, write $a_j=w_{p_j}$.
The following conditions are necessary and sufficient for $T(w)=p$:
$$
1\le a_1\le a_2\le\cdots\le a_n\le n,\qquad
a_j<a_{j+1}\quad\text{for every }j\in D(p). \tag{1}
$$
The decoder chooses exactly such a sequence and assigns $w_{p_j}=a_j$.

Necessity follows by comparing successive suffixes in their asserted
order. Their first letters must be nondecreasing. If two adjacent first
letters are equal, the order is decided by their remaining tails,
including the empty tail when the starting position is $n$.
Thus equal adjacent letters require
$r(p_j+1)<r(p_{j+1}+1)$, which forbids equality at a forced gap.

For sufficiency, first note a consequence of (1). If $j<k$ and $a_j=a_k$,
all intermediate $a$-values are equal. None of the intermediate gaps
can belong to $D(p)$, so
$$
r(p_j+1)<r(p_{j+1}+1)<\cdots<r(p_k+1).
$$
These tail ranks are distinct because the positions $p_j+1$ are distinct.

Now consider any two suffix starts $u,v\in\{1,\ldots,n+1\}$ with
$r(u)<r(v)$, allowing the empty suffix at $n+1$.
We prove the same strict lexicographic order by induction on the maximum
of their two suffix lengths. If one suffix is empty, its rank zero is
smaller and the assertion follows from the lexicographic convention.
Otherwise the first letters are ordered according to (1). If they differ,
the desired suffix comparison is decided. If they are equal, the
preceding consequence gives $r(u+1)<r(v+1)$. Both tail lengths are
smaller, so induction compares the tails in the desired order.
This proves the ordering of every pair and hence $T(w)=p$.

The construction is bijective: a chosen sequence determines one source,
and its letters in the prescribed order recover that sequence. No
predecessor outside (1) is omitted.

### Step 4. Fibre count and all maximizers

Let $e_j$ count the members of $D(p)$ strictly smaller than $j$ and put
$b_j=a_j-e_j$. Conditions (1) are equivalent to
$$
1\le b_1\le b_2\le\cdots\le b_n\le n-d(p).
$$
Indeed subtraction removes exactly the prescribed unit rises, and
addition restores them. Since $0\le d(p)\le n-1$, the upper alphabet
size is positive. Recording the multiplicity of each allowed $b$-value
is a weak composition of $n$ into $n-d(p)$ parts. A separator encoding
therefore gives
$$
\#T^{-1}(y)=
\begin{cases}
\displaystyle\binom{2n-1-d(p)}n,&y=p\in S_n,\\
0,&y\notin S_n.
\end{cases} \tag{2}
$$

This count is largest exactly when $d(p)=0$: for fixed positive $n$,
$\binom{m}{n}$ strictly increases over integers $m\ge n$.
If $d(p)=0$, the decoder permits $a_1=\cdots=a_n=1$.
The corresponding constant source has suffix array
$p=(n,n-1,\ldots,1)$ because shorter constant suffixes come first.
Conversely that constant source and the necessity of (1) show that its
suffix array has no forced strict gap. Hence the decreasing permutation
is the unique target with $d(p)=0$, and the exact maximum fibre is
$\binom{2n-1}{n}$. This includes $n=1$ and its single target.

## Source and internal subtraction

The literal static suffix-array definition is
[Kucherov–Tóthmérész–Vialette, Definition 1](https://arxiv.org/pdf/1206.3877).
Their Theorem 9 gives precisely (2), with alphabet size specialized to
$n$. To match their notation, prepend $n+1$ to $p$, obtaining $p'$,
and let $\Phi(p')=(p')^{-1}(p'+1)$, with addition cyclic on $[n+1]$.
For $1\le j\le n$,
$$
\Phi(p')(j+1)=r(p_j+1)+1.
$$
Thus their descent set outside position one has size exactly $d(p)$.
Theorem 4 supplies the equivalent prescribed-letter-multiplicity decoder;
Theorem 9 and its separator proof were actually read. The primary paper
itself attributes that counting result to Schürmann–Stoye. No oldest-
priority claim or unread original proof is inferred from that attribution.

Steps 3–4 are supplied self-contained for orientation and scope, but receive
zero contribution credit. Their maximum is an immediate unary-case
consequence of the same already-owned inverse characterization, not an
independent extremal mechanism.

The exact old
[D04_STW control](../../../papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md)
on $[n]^n$ replaces each letter by its stable rank among
$(\text{letter},\text{position})$. It is idempotent on permutations.
This is not the present map: for example, the three-cycle word in Step 2
is fixed by stable standardization but exchanged with its inverse by $T$.
For $n\ge3$, the different existence of strict two-cycles also rules out
a dynamical conjugacy of those same-parameter carriers.
The shared weak-order/forced-strictness fibre mechanism remains subtracted.

[P139's actual manuscript](../../../../papers/139-lyndon-factor-start-feedback/main.tex)
uses a binary mask of Lyndon factor starts, not the whole suffix-array
permutation. Its suffix-rank characterization is an owned interface, not
a proof that the two autonomous maps are equal or conjugate.
No retained P211/P212/P213 map is reopened.

## Corrections or missing assumptions

Changing the alphabet independently of $n$ would require a different
closed carrier: a suffix-array position may exceed that alphabet.
No such alteration is made. No cyclic BWT ordering or output inversion
is silently substituted for the stated suffix-array update.

There is no missing lemma in the limited author classification, but
there is also no materially separate new inverse axis after the direct
source subtraction. Additional numerical boxes would not change that
decision. No second literal is proposed to fill the unused allowance.

## Open risks

This is not independently reviewed and is not a novelty-clearance
certificate. The search does not prove that the iterative packaging is
absent from the literature. Disposition: **NO_NOMINATION**.
