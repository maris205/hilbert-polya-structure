# Literal family and proof boundary

Author: `/root/round211_functional_surgery_residual`, 2026-09-09 UTC.
This is a source-aware exclusion proof, not a candidate theorem contract.
No program, finite table search or scientific pilot was executed.

## 1. Carrier and simultaneous update

Let A be a finite alphabet. For n >= 1 and a count vector c with sum n,
let W(n,c) consist of words indexed by Z/nZ in which each letter a occurs
c_a times. A single local rule h:A^3 -> A acts by

    (F_h(w))_i = h(w_(i-1), w_i, w_(i+1)),

with all inputs read from the old word. We require this same h to preserve
W(n,c) for every n and c. This is a family-level assumption; preserving one
chosen content sector or one chosen ring size alone is weaker.

The carrier has labelled cyclic positions, not rotation classes. Length
never changes. There is no schedule, cursor, marker, asynchronous choice,
erasure, quotient, prescribed pair of involutions or alternating partition.

## 2. Binary radius-one closure — independent elementary proof

For A={0,1}, every such h is one of the five rules with Wolfram codes
170, 184, 204, 226 and 240, when the table is ordered 111 down to 000.

Proof. Constant words force h(000)=0 and h(111)=1. Write

    a=h(001), b=h(010), c=h(011),
    d=h(100), e=h(101), g=h(110).

Conservation on the three cyclic test words 001, 011 and 0011 gives,
respectively,

    a+b+d=1,     c+e+g=2,     a+c+d+g=2.

These are symbolic necessary identities, not a numerical experiment.
They imply a+d=1-b, c+g=1+b and e=1-b. Since all six variables are bits,
if b=1 there is only (a,b,c,d,e,g)=(0,1,1,0,0,1), the identity rule.
If b=0, independently choose a+d=1 and c+g=1, while e=1. The four
possibilities are

| a | c | h(x,y,z) | rule |
|---|---|---|---|
| 1 | 1 | z | 170 |
| 0 | 0 | x | 240 |
| 0 | 1 | x(1-y)+yz | 184 |
| 1 | 0 | z(1-y)+xy | 226 |

Each displayed map does preserve every content sector. This is immediate
for identity and shifts. For Rule 184 use the exact conservation identity

    h(x,y,z) = y + x(1-y) - y(1-z).

Summing over a ring telescopes. Its reflection does likewise. These
formulas remain valid for n=1 and n=2, so no small-ring convention is
missing. Necessity plus sufficiency proves the assertion. QED.

The local rule of existing P90 is exactly x(1-y)+yz. Reflection conjugates
184 and 226 on the entire labelled-ring carrier. Thus the only nontrivial non-shift
binary law in this entrance is the old Rule 184 family, not a new proposal.

## 3. Exact unambiguous pair-swap subclass

For any alphabet A, choose R contained in {(a,b): a != b}. The intended
rule swaps every adjacent occurrence ab with (a,b) in R, simultaneously.
Require those swapped edges to be disjoint on every cyclic word. This
holds if and only if R has no directed path a -> b -> c of length two,
where a=c is allowed in the forbidden path.

Proof. A shared vertex of two selected consecutive edges gives exactly
such a path. Conversely, a path appears at the middle of the cyclic word
abc (including aba when a=c), and the two selected edges share a vertex.
Thus it violates the required disjointness. QED.

Under this condition the literal local rule is

    h_R(x,y,z) = z, if (y,z) in R;
                 x, if (x,y) in R;
                 y, otherwise.

The first two cases cannot occur together. This is a deterministic
radius-one map and a product of disjoint swaps chosen from the old word,
so it preserves every count. It is not defined here as a fixed product
of globally prescribed involutions. For n=1 there are no nontrivial
selected edges; for n=2 the two directed edges cannot both be selected.

If |A|=3, each non-isolated vertex is either a source or a sink. Source
and sink sets are disjoint, so R has at most two edges. A nonempty R is
therefore either one ordered pair, two pairs with a common source, or
two pairs with a common sink. There are six of each of the following
two types: six one-pair relations, and six two-pair relations (three
common-source plus three common-sink). Together with R empty this gives
thirteen distinct local rules. Distinctness follows because for a != b,
h_R(a,a,b)=b exactly when (a,b) belongs to R. Neither global shift can
be one of these h_R: the appropriate aab/baa triples would require every
ordered pair to lie in R, violating the no-path condition.

This is an exhaustive proof only for the disjoint adjacent-swap
specification. Arbitrary radius-one local rules were not assumed to
have a swap representation.

## 4. Primary ternary classification and exact identification

Nishida, Watanabe, Fukuda and Watanabe, arXiv:2002.02653v2, section 4
and Appendices A--C, classify complete number conservation for three
states and three neighbours. Their result lists fifteen local rules.
Its literal hypotheses match section 1, as their definition tracks each
letter separately. Their proof derives the coordinate constraints,
solves nine cases per coordinate and selects compatible pairs. The
published case enumeration is source-owned; this desk did not perform
an independent audit of all 81 compatibility pairs.

Two nontrivial representatives in Appendix C, Table 3 are:

    7469071910973:
    ( y1,
      x2*y3 + y2*z1 + y2*z2,
      x1*y3 + x3*y3 + y2*z3 )

    6213370633533:
    ( x1*y2 + x1*y3 + y1*z1,
      x2*y2 + x3*y2 + y1*z2,
      x2*y3 + x3*y3 + y1*z3 ).

Inputs x,y,z are the standard basis vectors e1,e2,e3. Direct substitution
shows that these rules swap 23 only, and swap 12 and 13, respectively.
In the first rule e1 is stationary and separates traffic segments. In
the second, e1 moves right across either passive colour e2 or e3.
Their relabellings and spatial reflections supply exactly the twelve
nontrivial R-rules above. Table 3 also lists identity and both shifts.
Consequently our thirteen swap/identity forms plus two shifts identify
all fifteen source-listed forms. The broader exhaustiveness conclusion
depends on the cited primary classification, not just our subclass lemma.

The same representatives are equations (3) and (2), respectively, of
Nishida et al., JSIAM Letters 14 (2022), 143--146. They are already
published finite-state local laws before any fuzzy-state extension is
considered. No continuum fuzzy dynamics is proposed as a finite system.

For clarity, the discrete-to-vector conservation bridge can also be
proved directly. Extend h multilinearly to probability vectors at each
site. For n >= 3, independent random letters with those distributions
have distinct input sites in each neighbourhood. The output vector
at a site is the expectation of its discrete output basis vector.
Expected total counts therefore remain unchanged whenever the original
discrete map preserves them pointwise. For n=1 or n=2, periodically
repeat the probability-vector configuration on a ring of length 3 or 4,
respectively; the same local polynomial output repeats, so conservation
on that larger ring yields conservation on the smaller one. The reverse
implication is restriction to basis vectors. This justifies the match
of conservation notions without treating correlated repeated random
variables as independent. It does not itself prove the fifteen-rule count.

## 5. Value and limitation

All of these literal laws have an exact prior owner. On the one-pair
three-letter law, fixing a word with at least one barrier decomposes
the moving letters into independent binary traffic segments; with no
barrier it is the binary ring rule. On the two-pair law, forgetting the
passive colours gives Rule 184 (or its reflected/complementary form),
while their relative cyclic order is preserved because they never swap
with each other. A factor and an invariant order are not a whole-map
conjugacy, nor a new full-state temporal theorem or evaluated fibre law.

No claim is made that every coloured statistic is already known, nor
that a future rigorous residual theorem is impossible. None was proved
here, so this is a zero-new-literal desk. Higher radius, larger alphabets,
constraints on the carrier and different deterministic rewrite semantics
remain outside this bounded conclusion. Numeric mass conservation for
ternary symbols is strictly weaker than fixed-content preservation.
