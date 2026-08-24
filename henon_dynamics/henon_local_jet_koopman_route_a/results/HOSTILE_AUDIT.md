# Hostile audit — C114

Thirteen independent changes are applied to deep copies of the canonical
evidence.  The audit passes only if the independent checker rejects every one:

1. replace the scope literal;
2. alter the frozen map formula;
3. change the quotient dimension;
4. swap basis elements;
5. corrupt a Koopman matrix cell;
6. replace the matrix digest;
7. alter the full trace;
8. alter the determinant;
9. corrupt a characteristic-polynomial coefficient;
10. alter the degree-four block trace;
11. erase the nonlinear-correction count;
12. upgrade A2 to an unsupported global Fredholm claim;
13. remove one required nonclaim.

Result: `13/13` rejected.  The canonical evidence file is never overwritten
by the audit.
