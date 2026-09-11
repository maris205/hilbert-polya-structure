# Fresh41: circular recency ranks — exact inverse, missing time axis

AUTHOR_PARTIAL / HOLD_TEMPORAL / NO_PROMOTION. One literal defined below;
zero pilots, no admission/count change or new-source clearance. Proof author:
current_round_two_seats_scout. This is not an independent review.

## Literal

Fix q,n>=1. The carrier is [q]^n with cyclic positions. For w and position
i, let j be its preceding occurrence of w_i when scanning backwards round
the circle (j=i-n if it occurs only once). Define

    R(w)_i = 1 + number of distinct symbols strictly between j and i.

Thus R is a total finite autonomous map [q]^n -> [q]^n. It is invariant
under renaming input symbols. For q>=2 it is noninjective: the q constant
words all map to 1^n. This is NOT the fixed-initial-list bijective encoder
in Fresh37: the list initialization is the input's own cyclic recency order,
and original symbol names are not retained.

## All-target inverse theorem (author deduction)

For a target r in [q]^n set k=max_i r_i. On a list of k distinct tokens,
perform the positional operation 'move entry r_i to the front' in order
i=1,...,n. Let P_r be the resulting permutation of the initial list.
This permutation is independent of the names of the tokens. Then

    |R^{-1}(r)| = (q)_k = q!/(q-k)!  if P_r is the identity;
                  0                 otherwise.

This is a finite permutation identity test and an evaluated fibre count,
not a transfer-matrix sum over uncomputed compatible predecessors.

Proof. If w uses exactly h symbols, take its recency list just before
position 1, ordered by last occurrences in the preceding cyclic period.
Reading w updates that list by move-to-front, with precisely ranks R(w).
The final list equals the initial list. Every rank is at most h, and rank
h must occur: the initially last token remains last until its first access,
which occurs during the full word. Hence max R(w)=h. Necessity follows.

Conversely suppose P_r is the identity. Start with ANY ordered list L of
k distinct symbols selected from [q]. Decode r by outputting the specified
list entry and moving it to the front. Every token is used. Indeed, choose
the initially first unused token z if any exists. All used tokens lie before z at the end.
Since the final list is the initial list, they lay before z initially too.
That initial used-prefix set stays before z at every step, so every access
rank is at most the number of used tokens, which is <k; this contradicts
max r_i=k. After a period using every token, the final list is uniquely the
recency order of the decoded word. Since it equals L, L is also the cyclic
initial recency list. The decoded word therefore has R(w)=r.

Different L give different words, because the word recovers L uniquely
from its last occurrences. There are exactly (q)_k choices of L. This proves
both directions and the count, including k=1 and n=1.

## Consequences: complete image census and sharp inverse maximum

Two source words have the same R-value exactly when they differ by an
injective renaming of their used symbols. One direction is definition;
the other follows by aligning their initial recency lists and applying
the same decoder. Thus rank targets with maximum k correspond bijectively
to set partitions of [n] into k nonempty blocks. In particular,

    |im R| = sum_{k=1}^{min(q,n)} S(n,k).

Here S(n,k) is the Stirling number of the second kind; this is evaluated
standard set-partition enumeration, not a claimed new Stirling identity.
The largest fibre is (q)_{min(q,n)}. It is attained by the image of any
word using min(q,n) symbols. More precisely all equality targets are the
valid r with (q)_{max r}=(q)_{min(q,n)}. For q>=2 this means max r=n when
n<q-1, and max r in {q-1,q} intersect [1,n] when n>=q-1. For q=1 the
unique target has fibre one. The tie at q-1 and q must not be omitted.

## Temporal facts and the missing obligation

If w uses h symbols, R(w) takes values in [h], so the number of distinct
symbols cannot increase under iteration. Therefore every recurrent orbit
has constant support cardinality. This alone is NOT a clock or recurrent
classification: different partitions can have the same number of blocks.

The binary restriction gives no fresh rescue. Encode letters 1,2 as 0,1.
The recency rank is 1 precisely when consecutive symbols agree, so

    R_binary(x)_i = x_i + x_{i-1} over F_2.

This is ordinary cyclic difference. For n a power of two it is nilpotent
of exact index n: (I+S)^n=0, while (I+S)^{n-1} applied to one coordinate
vector is the nonzero all-one vector. The clock and rank-nullity inverse
are entirely classical linear algebra, not a residual theorem. No
all-q>=3 recurrent-set, period or exact entrance-time theorem is proved.
Consequently the independent inverse result does not justify admission
or a pilot request. No unproved convergence conjecture is promoted.

## Archive/source subtraction and actual evidence

Local-first specific search 1edd33 for reuse distance, stack distance,
recency rank and cyclic-recency expressions returned no hit in the two
recent scouting trees under its exclusions. This is NOT exhaustive novelty
clearance. Earlier parity-switch and sink-reversal leads were rejected on
positive archive hits before defining alternatives; they are not candidates.

Fresh37/DESK.md explicitly proves fixed-initial-list MTF bijectivity;
its map differs as explained above. The original CNL proof in
`docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md`,
lines 1--48, was read (383cb6). It explicitly deducts cyclic characteristic-
two difference/augmentation clocks through P178. No CNL literal identity
is asserted for this circular recency transform.

The direct primary definition/decoder source already read in this desk
session is Bentley--Sleator--Tarjan--Wei,
[A Locally Adaptive Data Compression Scheme](https://www-2.cs.cmu.edu/~sleator/papers/adaptive-data-compression.pdf),
Section 2, pp. 320--321 (turn10961view0). It describes synchronized recency
list encoding/decoding. That primitive, and the permutation closure test
built from it, receive no novelty priority. The source is not claimed to
state the circular transform's iteration or the displayed all-target theorem.
The later Kulkarni-host paper opened as a PDF, but two finds failed; no
new body-read claim is based on that opening or search snippets.

Only this note was written. Native source/read/search returns remain in
the conversation, not an immutable captured package. No scientific code,
external-state changes, children, central edits, numbering, Git or review
PASS. The honest outcome is one partial deductive case with a proved
inverse axis and an unresolved general temporal axis, not a paper contract.
