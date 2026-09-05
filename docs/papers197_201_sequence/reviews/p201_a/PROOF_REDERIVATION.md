# P201 Review A — independent deductions

Status: `PROVABLE_AS_STATED` for the stated mathematical package, but
`REJECT_ADMISSION_EXACT_HISTORICAL_CONJUGACY` for the new-system slot.
This file does not infer global novelty from valid mathematics.

## 1. Rank cost and the clock ceiling

Every weak component of an endofunction has one directed cycle. Let L be the
set of distinct cycle lengths. Every component contributes its length minus
one to the feedback image; hence the next rank is |L|. Choosing one cycle
of every length gives disjoint subsets of the old image, so
`rank(f)>=sum(L)>=Q(|L|)`, where `Q(s)=s(s+1)/2`.
For a next rank at least two, this decreases rank strictly. At rank one the
current function is constant; its sole cycle is a loop and its feedback is
zero. Zero stays zero. This proves convergence and uniqueness of the
recurrent state without assuming rank satisfies an equality recurrence.

A rank-one state has height at most one. Inductively, height at least h+1
implies that its feedback has height at least h, rank at least N_h, and the
old rank at least Q(N_h)=N_(h+1). Start at N_2=2. Thus N_h is a necessary
rank threshold, not just a necessary carrier size. On one label there is
only zero, so H(1)=0. This addresses the otherwise exceptional rank-one
case before deriving the n>=2 ceiling.

## 2. Core extension and attainment

Suppose g sends all n labels into the first k and u is its restriction to
those k. Its cycles are exactly u's cycles. Feedback still has values in
the first k; its restriction is the feedback of u. Repeating this proves
the restriction identity at every epoch. A feedback vector is zero exactly
when all cycles of its input are loops. Since extension and restriction
have the same cycles at every epoch, zero equivalence holds for every
positive epoch. It need not hold at epoch zero: if u=0 but g is not zero,
g has height one. Otherwise positive height is preserved exactly.

The transposition on two labels has feedback (1,1), then (0,0), and height
two. Given a height-h permutation u on k=N_h labels, associate to each
j in 0,...,k-1 a cycle of length j+1 containing the unique old label
u^{-1}(j) and j fresh labels. These disjoint cycles cover Q(k) labels.
The feedback maps into the first k labels and restricts there to u.
The positive-height core lemma makes the lifted permutation's height h+1.
This proves exact attainment, not just arbitrarily long examples.

For rank r>=2 choose the largest critical size k<=r and its critical
permutation. Pad with fixed points to a permutation on r labels. Its first
feedback is zero outside k and is the old feedback inside k, whose height
is at least one; hence the new permutation has the same height H(r).
Pad the carrier further to n>=r by sending all new labels to zero. The
image rank remains exactly r and the core lemma preserves height. Thus the
ceiling is attained at every rank and carrier. At rank one the maximum is
one when n>=2, attained by any nonzero constant, and zero when n=1.

## 3. Critical iff and factorial count

At n=N_h, height h forces rank n, so the state is a permutation. For h>=3,
put k=N_(h-1). In the chain
`n >= sum(L) >= Q(rank(P f)) >= Q(k)=n`
every inequality is an equality. Strict increase of Q forces next rank k;
the distinct-length sum equality forces L={1,...,k}; and its total cost n
leaves no room for any additional cycle. The first feedback therefore maps
into [k]. Its restriction has height h-1 by the core lemma, and the rank
threshold on that critical carrier makes it a permutation. This proves
necessity of both listed conditions. Conversely those conditions give a
core extension of a height-(h-1) map, so the original permutation has
height h. No condition is silently used in only one direction.

Fix such a restriction u. Its unique preimage of j fixes one old label in
the j+1 cycle. Distribute n-k fresh labels into the distinguished blocks in
`(n-k)! / product(j!)` ways. Once a block and its distinguished old label
are fixed, the number of directed cycles on it is j!. Multiplying cancels
the denominator. Distinct allocations or cycle orders give distinct
permutations, while the critical iff recovers each allocation from its
permutation. The factor per u is exactly `(n-k)!`. Since only the two-label
transposition has height two, D_2=1 and
`D_h=D_(h-1)*(N_h-N_(h-1))!`. No unlabelled quotient or division by k! is
allowed. This classification is asserted only at critical sizes.

## 4. Forest coding and all target sources

For a prescribed nonempty root set R of size s on k labels, orient forest
edges toward R and repeatedly erase the least nonroot leaf, recording its
parent. There are k-s entries, the final one a root. To decode any sequence
of this length ending in a root, choose the least remaining nonroot absent
from the remaining sequence and connect it to its first symbol. Such a
label exists: the sequence contains a root and cannot contain every
remaining nonroot. A previously deleted vertex never appears later, so
every edge goes to a still-present vertex; no cycle is introduced. When
only roots remain the decoder stops and reverses every encoding step.
This proves `s*k^(k-s-1)` when s<k; for s=k the empty code gives one forest.
The verifier checks both roundtrip directions and surjectivity at k<=5.

Let a_d(k) count functions whose cycles all have length d. Select dc cycle
labels, partition them into c directed d-cycles, and attach a forest rooted
at those labels. This yields the manuscript sum over c and proves
nonemptiness exactly when k=0 or k>=d. This is classical enumeration,
not residual novelty. For an independent numerical route, decompose at the
connected component containing the least label:

```
a_d(0)=1,
a_d(k)=sum_{m=1}^k C(k-1,m-1) c_d(m) a_d(k-m),
c_d(m)=C(m,d)(d-1)! R(m,d).
```

If a target g labels a source vertex i by j, then its old successor must
have the same eventual cycle length. Hence every block g^{-1}(j) is
invariant under an inverse source f. Every cycle in that block must have
length j+1. Conversely these block conditions force P f=g at every label.
They are independent on different prescribed blocks. This proves the
product fibre formula, including empty fibres, and reconstructs actual
inverse source sets. An occupied block must have size at least j+1.
Choosing labels for all admissible block sizes gives the stated image sum.
The independent verifier compares all target counts through n=7 and full
incoming source sets through n=5, not merely total mass or a histogram.

## 5. The strict maximum

For a connected m-label component of cycle length d,
`c_d(m)=(m)_d*m^(m-d-1)`, interpreted as `(d-1)!` at m=d.
For d=1 this is `m^(m-1)`. For d>=2 and m>=d the ratio to the rooted-tree
count is `(m)_d/m^d<1`. For m<d the connected count is zero. Expanding SET
as a sum over labelled component partitions preserves coefficientwise
inequality. Strictness for any occupied admissible block follows already
from its single-component summand. Thus a_d(k)<=a_1(k), strictly if d>=2
and k>=d.

For at least two occupied target blocks, disjoint union injects their rooted
forests into all rooted forests on the union, but misses a forest with an
edge joining two distinct blocks (take one cross edge and all other
vertices roots). Thus that product is strictly smaller than a_1(n). For a
single occupied block, equality requires d=1, namely the zero target. Its
forest count is `(n+1)^(n-1)` by adjoining a distinguished extra root and
joining every component root to it. At n=1 this count is one and there is
only one target. Unsupported targets cannot maximize a positive fibre.

## 6. Exact historical conjugacy — all sizes, not a finite signature

The historical OCL implementation uses `O(f)(i)=ell_f(i) mod n`.
For `sigma(i)=i+1 mod n` and `H(f)=sigma f sigma^{-1}`, every old orbit is
relabeled by sigma, whence `ell_(H f)(i)=ell_f(sigma^{-1}(i))`. Since
`sigma(d-1)=d mod n` for every possible period d in {1,...,n},
`O(H f)=H(P f)`. H is invertible, with inverse conjugation by sigma^{-1}.
This is valid even for n=1.

Induction gives `O^t H=H P^t` for every t>=0. Consequently
`H(P^{-t}(g))=O^{-t}(H g)`, and H preserves rank as well. The critical
thresholds and counts are therefore theorems about the previously killed
OCL dynamical system under this explicit coding. It would be false to say
that the old scout already proved them; it is equally false to count this
as a new map beyond that old killed map under the current central anchor.
