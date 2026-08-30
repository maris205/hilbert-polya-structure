# P118 exact-control results

The deterministic Python verifier has no random branch and uses only the
standard library.  On fifteen parameter lanes it independently computes:

1. every labelled graph colouring and its literal first image;
2. every inclusion–exclusion fibre;
3. every support/onto fibre;
4. every closed recurrent-target fibre;
5. the complete quotient preimages;
6. the literal transition of every quotient vector, including its
   two-step landing in the displayed recurrent list;
7. all pointwise depths and recurrent states; and
8. every orbit basin and depth layer.

The grid includes \(K_{1,2,3}\) with 46,656 states,
\(K_{2,2,2}\) with 15,625 states, the \(k=1\) boundary, and palettes larger
than \(\Delta+1\).  Fresh command:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

Expected result: PASS with 202,965 exact assertions.  The canonical stdout is
stored in code/verification_output.txt.
