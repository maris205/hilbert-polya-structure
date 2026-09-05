# P200 Review B: independent all-parameter proof audit

2026-09-05 UTC. Status: PROVABLE AS STATED. The frozen Round1 claims
survive unchanged. The reviewer is neither manuscript author nor Review A.
The verifier was written before reading either earlier verifier source;
neither earlier verifier source was needed or imported.

## Claim, assumptions and proof devices

Assume integer dimensions $r,s\ge2$, labelled rows and columns, and the
exact lexicographic order $(i,k,a,b)$ with the row pair first. The state is
an arbitrary binary matrix; there are no fixed-margin restrictions on the
carrier, though each individual orbit preserves its starting margins.
The map flips its first alternating rectangle, or holds if none exists.
Tail means the distance to a directed cycle, not to a fixed point.

For an independent implementation, write a matrix as column-incidence
sets $C_0,\ldots,C_{s-1}\subseteq[r]$. For $a<b$, put
$L=C_a\setminus C_b$ and $R=C_b\setminus C_a$. The alternating
rectangles on these columns are exactly the crossings between $L$ and $R$.
If both are nonempty, the first row of the least crossing is
$i=\min(L\cup R)$ and its partner is the minimum of the opposite class.
Taking the least such event over column pairs gives the printed scheduler.
This is not scanning packed column-major scalar bits or row bit masks.

For the proof, a pair-sign word lists only columns at which rows $i,k$
differ, writing $+$ when row $i$ contains the column and $-$ otherwise.
It is a proof device equivalent to the row exclusive sets, not an added
state variable or a stronger hypothesis.

Dependency map: containment sandwich implies pivot invariance; pivot
invariance and pair-sign evolution imply recurrence and the two-visits
bound; a singleton-pivot itinerary attains the wide bound. Reversing a
pair-sign word plus the same sandwich safety gives the exact inverse;
saturating its two independent finite capacities gives all maximizers.
The fixed census and generic selector descent are not new ingredients.

## 1. Sandwich safety and the invariant pivot

Let $P,Q$ be incomparable row supports. A third set $H$ comparable with
both must obey $H\subseteq P\cap Q$ or $H\supseteq P\cup Q$.
There are only four choices of the directions of the two containments;
each mixed choice would imply $P\subseteq Q$ or $Q\subseteq P$.
An interchange preserves both $P\cap Q$ and $P\cup Q$, so this safety
statement holds in both forward and reverse directions.

If $(i,k)$ is the first incomparable pair, every row $h<i$ is comparable
with every other row. Otherwise an incomparable pair would begin before
$i$, regardless of whether its second index lies before or after $i$.
The safety statement preserves these comparisons after a switch. The
changed pair itself stays incomparable because the same rectangle is
still alternating. Hence the first pivot remains $i$, the least partner
cannot rise beyond $k$, and a nonfixed state cannot enter the fixed class.
This validates Lemma2.1 without assuming that intervening rows are
comparable with every other row; only the rows strictly before $i$ have
that stronger property.

## 2. Every recurrent point and the exact cycle support

The active event remains available after its involutive flip. Thus its
lexicographic index never increases. Equality means the next flip reverses
the same rectangle and returns to the initial matrix; the two matrices
are distinct. A strict decrease cannot occur on a cycle. Therefore
nonfixed recurrence is equivalent to equality of two consecutive selectors,
and every nonfixed cycle has length exactly two.

The least event in a pair-sign word uses its first sign and its first
opposite sign. If that opposite sign is at the second position, flipping
the two signs leaves that pair's selected columns unchanged. If it is
later, the old second sign stays unflipped and becomes opposite to the
new first sign, causing a strict column decrease. Hence the printed
opposite-first-two-differences condition is necessary and sufficient for
column equality. By sandwich safety, no earlier pivot can appear. The
remaining obstruction is exactly that the reconstructed pivot becomes
incomparable with some $i<h<k$. This is the printed row-containment test.
There is no omitted check for $h=k$ or $h>k$: the old pair stays active,
and later partners cannot defeat it.

Fixed points are precisely matrices with pairwise comparable row supports,
equivalently no alternating rectangle. No switch can land at one, so a
fixed target has exactly its self-predecessor. This last assertion is
stronger than merely being fixed and was checked separately.

## 3. Two visits, an off-by-one audit and the width boundary

Follow one partner during its consecutive visit. After at most one switch
its first two signs are opposite if it is still selected. With opposite
first two signs, either the next state changes to a smaller partner or
the present state is already recurrent. Thus no partner appears more
than twice among selector states at times $0,\ldots,\tau$, including
the first recurrent state. Since departed partners never return, for
$p$ distinct partners,

$$\tau+1\le2p\le2(r-i-1),\qquad \tau\le2r-3.$$

The inclusion of the first recurrent state is essential for the minus
one. Fixed states have $\tau=0$ and satisfy the bound independently.

For $s\ge r+1$, use the printed singleton pivot and companion rows.
At the start of stage $k$ the pivot is $\{k+1\}$. All earlier partner
rows contain this singleton, whereas row $k$ lacks it and first differs
in the opposite direction at column0. The first event is
$(0,k,0,k+1)$; the resulting pivot is $\{0\}$ and changed row is
$\{k,\ldots,r\}$. The next event is $(0,k,0,k)$, giving pivot
$\{k\}$ and row $\{0,k+1,\ldots,r\}$. If $k>1$, the first newly
incomparable row is $k-1$. This proves the entire itinerary by induction.
For $k=1$, the second selector is the first recurrent state. Every earlier
selector strictly decreases at its next step. There are $2r-2$ listed
selector states, hence tail $2r-3$. Appended all-zero columns cannot
create an earlier rectangle, proving the same witness for every wider box.

At $r=s=2$, all sixteen matrices are already recurrent, so the general
bound1 is not sharp there. This does not contradict the width restriction.
No equality formula for all $s\le r$ is asserted. Transposition changes
selector priority; the independently verified image counts3292 for
$3\times4$ and3290 for $4\times3$ preclude transposition conjugacy.
The square/narrow observations in the table remain finite data.

## 4. Independent sign-word derivation of the complete inverse

Fix a nonfixed target $Y$. Every predecessor has the same first pivot
$i$ by Step1. Suppose it switched with row $k$. The target pair remains
incomparable. Let its ordered nonzero signs be
$\epsilon_1,\ldots,\epsilon_m$ at positions $j_1<\cdots<j_m$.
Reverse a switch involving target positions $j_a,j_b$ with opposite signs.
The source differs only by reversing those two signs.

For the reversed switch to be first within this row pair, its smaller
column must equal $j_1$: otherwise the earlier differing column persists
and belongs to one of the two exclusive sides, creating an earlier pair.
Write the other column as $j_b$. After reversing $\epsilon_1$ and
$\epsilon_b$, the first source sign is $-\epsilon_1$. Its first opposite
sign must occur at $j_b$, not earlier. Hence every sign between positions
1 and $b$ must equal $-\epsilon_1$ in the target. Equivalently, $j_b$
ranges over the initial run of opposite-type differences after $j_1$,
stopping at the next same-type difference. This gives exactly the strict
inequality $\ell<b_k$ with the sentinel $b_k=s$ when no next sign exists.

Now use sandwich safety in reverse. Every row before $i$ stays comparable
with both changed rows. For a possible earlier partner $i<h<k$, the
row itself is unchanged, so the sole test is comparability of its support
with the pivot after the two toggles. This test is both necessary and
sufficient; no full selector run on the proposed source is required.
These are precisely the target-only candidates in Theorem4.1.

Different $k$ change different nonpivot rows; at fixed $k$, different
$\ell$ change different columns of the pivot. Thus the reconstruction
has no duplicates. A target with no candidate is absent from the image,
and fixed targets contribute the separate unique self-source. The verifier
compares actual sets of source matrices, not only cardinalities, on every
target of every complete box, including zero-source and fixed cases.

## 5. Fibre extremum and every equality target

For a nonfixed target, there are at most $r-i-1$ partner terms and at most
$s-1$ sign positions in each. Therefore the fibre is at most
$(r-1)(s-1)$; fixed fibres equal1 and obey the same bound.
The printed target with pivot $\{0\}$ and all other rows its complement
admits every partner and every column other than0: the reversed pivot
is a singleton contained in each intervening row. It attains the bound.
Entrywise complement commutes with the exact selector and gives another.

If the bound exceeds1 and equality holds, the target is nonfixed and
both capacity inequalities must saturate: $i=0$, every later row is a
partner, and each contributes $s-1$ columns. Consequently the first sign's
side has one column, the opposite side has the remaining $s-1$, and no
column can be shared or absent from both supports. The first column is0.
The common pivot therefore forces one of the same two orientations for
every partner. There are no further equality targets. When the product
equals1, necessarily $(r,s)=(2,2)$; the sole interchange exchanges two
states and the other fourteen hold, giving all sixteen maximizing fibres.

## Corrections, assumptions and open risks

No correction or added hypothesis is needed. The proof-writing skill
guided the quantifier, sentinel, inverse distinctness and off-by-one
checks. The large witness checks support but do not replace the induction.
Square/narrow sharpness, an all-time inverse atlas, and unrestricted source
originality remain outside the accepted claims. OWNER_AMBER / HOLD_EXTERNAL.
