# HXC and excluded algebra: proof/value boundary

## HXC cardinality clock is sharp but generic

The bound $\operatorname{depth}(H)\le |H|-1$ for nonempty families proved
in `PRECODE_PROOFS.md` is sharp as a bound in the number of edges with the
ground set allowed to vary. For every $r\ge1$ on $[r]$, take
$$H_r=\{\{0\},\{0,1\},\ldots,\{0,1,\ldots,r-1\}\}.$$
Every two members intersect, and their binary-code order is their inclusion
order. Each edge other than $\{0\}$ chooses $\{0\}$; the latter chooses
$\{0,1\}$ when $r\ge2$. The new family consists of
$\{1\},\{1,2\},\ldots,\{1,\ldots,r-1\}$. The same argument repeats
after shifting the first available vertex. At time $r-1$ the family is the
single edge $\{r-1\}$, and every earlier nonterminal family has at least
two intersecting nested edges. Its entrance time is exactly $r-1$.
For $r=1$ it is fixed at time zero. This is a symbolic all-$r$ construction,
not an extra numerical box or an experiment beyond the declared cutoff.

This attainment does not upgrade generic cardinality loss into the required
nontrivial temporal contribution, and it does not give the sharp maximum
over all families on a fixed $n$-element ground set. The original boxes
$n=0,1,2,3,4$ have observed maximum entries $0,0,1,3,6$. No all-$n$ formula
for that maximum is proved. The $n=4$ largest fibre, of size 318, occurs at
edge codes $\{1,2,4,8,10,12\}$ and was evaluated from all 32768 sources.
It is not a recurrent disjoint family. No independent full-target decoder
or all-parameter maximum theorem was derived. Status: NO_PROMOTION.

## Why the algebra desk was excluded before any pilot

A considered description was $T(A,B)=([A,B],A+B)$ on pairs in the strictly
upper-triangular algebra $L_n(\mathbb F_q)$, for $n\ge1$ and prime powers
$q$. This is the same operation already present in the old CS scout, on
a different matrix carrier. It is not counted as a fresh third candidate.
For clarity the proposed all-size facts can be deducted completely.

Let $L_n^k$ consist of matrices supported at least $k$ diagonals above the
main diagonal. Matrix multiplication gives
$[L_n^a,L_n^b]\subseteq L_n^{a+b}$ and $L_n^n=0$. If
$(A_t,B_t)=T^t(A,B)$, induction gives $A_t\in L_n^{t+1}$, whereas
$B_t\in L_n$. Hence $A_{n-1}=0$ and the state is fixed thereafter.
Conversely every fixed state has $A=0$, from its second-coordinate equation.
Every recurrent state must already lie on that fixed locus: iterating it
$n-1$ steps yields a fixed state and periodicity identifies the original
with it. The maximal entrance is $n-1$ for $n\ge2$.

For attainment let $J=\sum_{i=1}^{n-1}E_{i,i+1}$,
$A_0=E_{12}$ and $B_0=J-E_{12}$. The first coordinates satisfy
$A_t=E_{1,t+2}$ for $0\le t\le n-2$. Indeed $B_t$ differs from $J$ only
by a linear combination of first-row matrix units, which commute with
$E_{1,t+2}$, and $[E_{1,t+2},J]=E_{1,t+3}$ until the last column, where
it vanishes. Thus the first coordinate first becomes zero at $n-1$.
For $n=1$ there is only $(0,0)$, of depth zero.

For any target $(C,S)$, the source equation is precisely
$$[A,S]=C,\qquad B=S-A.$$
It is a linear system in $A$. Each nonempty fibre is an affine coset of
$\ker(\operatorname{ad}_S|_{L_n})$, of cardinality
$q^{\dim\ker(\operatorname{ad}_S|_{L_n})}$. The maximum $q^{\dim L_n}$
is attained exactly at $C=0$ and $S$ central in $L_n$. This follows because
the kernel has full dimension exactly when the operator vanishes.
These are the same affine-centralizer source mechanism already explicitly
deducted by the CS gate, coupled to ordinary nilpotent filtration descent.
No numerical execution or independent proof class is claimed for them.

## Source distinction from P117 and H04

The actual P117 opening/update and boundary lemma were read (original TeX
lines 1--165). P117 flips bit values on odd constant cyclic binary runs;
it does not reverse entries of increasing permutation runs. That literal
distinction does not turn generic run parity into new credit. H04's old
span-closure operation adjoins and retains XORs; HXC replaces and merges
selected outputs. Its explicit nonidentity example is recorded in the
source document, without claiming nonconjugacy or source completeness.
