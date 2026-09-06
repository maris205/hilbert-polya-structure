# OFS bounded recursive follow-up declaration

2026-09-06 UTC, after the unchanged two pilot executions and before the
new checker. Use only the original complete n=3,...,10 triangulations.
This is an author deduction/probe, not another candidate or an expanded box.

The pilot suggests one two-cycle, height n-2 for n>=5, and maximum fibre
2^(n-4). Those all-n statements remain conjectures. The first-image counts
match OEIS A105633, but sequence matching is not an objectwise adapter.
The desk's preliminary unrestricted right-spine grammar was already
discarded: it gives 58 rather than 57 in the original n=8 box. Preserve
that failure; do not revise the raw census.

## Proposed exact binary-tree dictionary to test

Use the usual full binary tree rooted at boundary edge (0,n-1), whose leaves
are the successive boundary intervals. The leaf is e. Write LS(T)=[B1,...,Bk]
for T=leftcomb(e,B1,...,Bk), the successive right subtrees on its left spine.
Let first(S,A) substitute tree A for the leftmost leaf of S. Define G(B)=F(e,B).
For a list of length at least two put

    P(B1,B2)=F(B1,B2),
    P(B1,...,Bk)=first(G(Bk),P(B1,...,B(k-1)))  (k>=3).

The proposed recursion is:

    F(e)=e,
    F(e,e)=(e,e),
    F(T)=(e,P(LS(T)))                         if |LS(T)|>=2,
    F(e,B)=first(G(C1),(e,e))                 if LS(B)=[C1],
    F(e,B)=((e,e),P(LS(B)))                   if |LS(B)|>=2.

All recursive calls use fewer leaves. The proof route partitions the
remaining old diagonals by the protected new fan diagonals after the first
active vertex sweep. The initial 0-fan branch makes vertex 0 an ear; the
initial 0-ear branch processes the 1-fan and creates ear 1. No all-n
acceptance precedes the protected-cell proof and exact original-box check.

## Additional explicit hypotheses, allowed to fail

1. Ear 0 toggles at every step for n>=4; the output has ear 0 or ear 1.
2. Under the standard tree word W(L,R)=U W(L) D W(R), the image might be
   exactly UUDU-avoiding. This is only a count-driven guess, not a fact.
3. A possible fibre exponent is the number of left-child internal edges
   outside the root's all-left spine. This is only a proposed statistic.

Record actual successes and first counterexamples separately. In particular,
a mismatch to hypotheses 2 or 3 must not be disguised by choosing a new
bijection without a new declared adapter. The checker may report these
failures without exiting nonzero, because it is explicitly a falsification
probe. Literal carrier equivalence, the proposed recursive dictionary, and
the proved ear statement are assertions and must actually pass.
