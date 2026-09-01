# Improvement log — P143

## Round 1

Hostile review A returned REVISE without a theorem counterexample.

Closed findings:

1. Replaced the incorrect Katona--Nagy DOI with the official Springer
   identifier ending 9342-8 and rebuilt the printed bibliography.
2. Added exact Schmidt section/figure/page and orientation locators.
3. Added Botts's classical principal-upper-set representation as the closest
   powerset-embedding control and sharpened the zero-credit boundary.
4. Replaced ambiguous “copies/embeddings” language by “labelled induced
   order-embedding maps” and stated that automorphisms are not divided out.
5. Added verify_p143_embeddings.py, an independent bijection lane that does
   not call the inclusion--exclusion formula.  It compares every direct fibre
   set through n=4 and adds an all-poset B5 pressure lane.
6. Froze both verifier transcripts and documented byte-comparison commands.
7. Recorded the current and historical PDFs separately and reproduced the
   current PDF byte-for-byte in an isolated build.

No theorem was broadened.  The paper remains owner-thin and HOLD_EXTERNAL.

## Round 2

An independent hostile reviewer accepted the repaired package with zero
critical, major, or minor findings.  The reviewer re-derived the preorder
transpose law and quotient-poset fibre bijection, attacked collapsed classes
and labelled-versus-unlabelled embeddings, reran both canonical verifiers,
performed a source-only isolated build, and inspected all four PDF pages.
Both verifier transcripts and the rebuilt PDF matched byte for byte.  No
additional theorem or ownership change was required.  The accepted artifact
is frozen as `main_round2.pdf`; external status remains `HOLD_EXTERNAL`.
