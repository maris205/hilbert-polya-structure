# Fixed-Jacobian trace proof: V1.1 clarification

Date: 2026-09-05. This clarification is read together with the unchanged
[author V1](PAPER29_FIXED_JACOBIAN_TRACE_PROOF_V1_20260905.md), SHA256
`8307ce9e82a8066b91c9f7a751299d32941c93e45cc9cb7df164dbae840afd1e`.
It changes no main theorem, bound, parameter region or selected word.

In Section 2, replace the unrestricted sentence about two symbolic words
not related by cyclic shift by the following precise version:

> Two **primitive** cyclic words not related by cyclic shift produce
> disjoint actual cycles. Each has exact period equal to its length;
> if the two cycles coincided, those lengths would agree and their
> root-disc itineraries would then differ by a cyclic shift.

For unrestricted words of different lengths the original sentence is
false: $(a)$ and $(a,a)$ yield the same fixed orbit. Every word selected
in V1 Section 4 is primitive, as proved there, so this auxiliary wording
error does not change the claimed tuple or the main proof. Both
independent readers checked this distinction.

In Section 3 the trace-correction estimate can be made more explicit by
taking
$$q(\epsilon)=B|\epsilon|^2/\mu^2.$$
Then $|\theta|\le q(\epsilon)^n$ on $|b|\le B$, and after decreasing
the common radius so that $q(\epsilon)<1/4$, the scalar factor in
equation (9) differs from one by $O(|\epsilon|^2)$ uniformly in $n$.
This records the dependence already used by the proof; it is not a
new assumption or a weakening.

The limiting occupancy matrix in Section 4 is right-multiplied by the
column-diagonal matrix with entries $-(d-1-j)/d$. This fixes the order
in the phrase “product of a column-diagonal matrix with a matrix”;
the displayed determinant formulas are unchanged.

Mathematical status of V1 together with this clarification:
**PROVABLE AS STATED**. This is not a candidate-fit or publication PASS.
