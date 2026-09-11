# P203 B: two actual final verifier replays

Both commands were run from /root/autodl-tmp/symbolic_dynamics:

~~~
python docs/papers197_201_sequence/reviews/p203_b/verify_independent.py
~~~

Final verifier SHA-256:
6e0520553738cf546578facf25f59f91c7b80f85b2bb7bfd69cb6729a20c9907.

## Replay 1

Fresh execution session 45998, launch receipt 8e092a, completion b4f30c.
A clock observation immediately before launch was 2026-09-05 08:54:39 UTC;
the completion was observed by 08:57:09 UTC. Exit code 0.
Actual stdout is RUN1.txt.

## Replay 2

Fresh execution session 13516, launch receipt df5bc3, completion fa74ef.
A clock observation immediately before launch was 2026-09-05 08:57:09 UTC;
the completion was observed by 08:58:27 UTC. Exit code 0.
Actual stdout is RUN2.txt.

These are execution-observation intervals, not claimed benchmark runtimes.
The two stored output strings were actually byte-compared in the
orchestration tool, and the written RUN1.txt/RUN2.txt were additionally
compared by cmp with exit 0. Each is byte-identical to CANONICAL.txt, SHA:

bc66ce4a667adaf4e31faffc1342223fa39b0fe26e217f051394e86da421feb5

Both independently execute the final unchanged program and report
assertions=1502359 and status=PASS. Scope: all 33,868 MCT states on n=0..6;
uniform sharp traces n=3..80; both-colour star/top witnesses n=4..24;
and separate historical Q01 controls n=3..6.

An earlier successful run used the provisional footer and is deliberately
not counted as either final replay. The final footer was simplified before
Replay 1 to give one assertions counter and status=PASS, without a
programmatic "review findings" verdict. The mathematical assertion set
was not weakened. Review findings are adjudicated in REVIEW_B.md, not
in the finite control's output.

No author or Review-A code was read, imported, executed or copied for this
implementation. Its row-string/Kosaraju/reverse-BFS engine transparently
adapts this reviewer's pinned Stage1 control; paper-specific image,
recurrent and trace checks were added. It is not a fresh-from-zero claim
and the old Stage1 runs are not substituted for these actual B executions.
