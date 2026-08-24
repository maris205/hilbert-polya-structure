# Hostile audit — C121

Sixteen independent changes are applied to deep copies of the canonical
evidence.  The audit passes only if the independent checker rejects every one:

1. replace the scope literal;
2. change the frozen parameter;
3. change the affine formula;
4. corrupt the inverse formula;
5. exchange the forward base point;
6. negate the algebraic-stability verdict;
7. change the eighth projective degree from 256 to 255;
8. corrupt the fourth recurrence-DAG hash;
9. alter a cycle point;
10. corrupt a monodromy entry;
11. mark a negative control as preserving the cycle;
12. introduce an unsupported entropy claim;
13. upgrade A1 despite the absent prime-like target correspondence;
14. upgrade A2 without a determinant or transfer owner;
15. soften missing A3 structure to a noncanonical “not addressed” label;
16. remove a required nonclaim.

Result: `16/16` rejected.  The canonical evidence file is never overwritten
by the audit.
