# Combinatorial lane — bounded initial slate

Date: 2026-09-08 UTC. Author/proof contributor: `round211_combinatorial_scout`.
Status: scouting only; no candidate admission, manuscript number, independent
review, Git action or external model upload. This author cannot review any
resulting paper. Project SKILL, WORKFLOW, current root state, batch state,
PROBLEM_ANCHOR and inherited promotion criteria were read before execution.
`research-lit` / ARS source verification and `proof-writer` are used in the
project's narrower scope; optional API clients and generic pipeline panels
are off. Current-process work is not an external GPT-5.4 review.

## Four literal definitions, before the only pilot

1. **FRI — first-return insertion.** On words of fixed length $n\ge1$ over
   $[q]=\{0,\ldots,q-1\}$, remove the first letter $a$ and insert it
   immediately before the next occurrence of $a$ in the remaining word.
   If there is no other $a$, append it at the end. Equivalently,
   $a u a v\mapsto u a a v$ when $u$ avoids $a$; a singleton first letter
   moves to the end. This preserves every multiplicity, not just the
   equality partition. The only pilot is the complete boxes $1\le q\le4$,
   $1\le n\le6$, with no later cutoff enlargement. Candidate claims under
   pressure: first-repeat pointwise clock, complete recurrence and a
   first-double / final-singleton inverse decoder. Risks: elementary
   stopping/first-collision mechanism, P185 prefix-diversity clock, P176
   pointed rotations, P199 one-root insertion, P209 next-occurrence syntax,
   and public self-organizing-list / word-transform ownership. No claim of
   novelty or residual value is made before subtraction.
2. **OSC — odd sum-component complement.** On $S_n$, split a permutation
   at every proper prefix whose values are that initial interval. Within
   each odd-length resulting direct-sum block, complement its values inside
   its interval; retain every even block. Its inversion graph undergoes
   exactly P123 odd-component complementation. Immediate mechanism kill;
   no pilot, no new temporal credit, and no claim that permutation graphs
   exhaust all P123 graph inputs.
3. **RCS — rectangular row-column sorting.** On bijective fillings of an
   $h\times w$ rectangle by $1,\ldots,hw$, first sort each row increasingly,
   then each column increasingly, using the result of the row pass.
   Column order statistics preserve all row inequalities, so the image is
   the row-and-column-increasing fillings and the map is idempotent.
   The potentially difficult static inverse does not create a temporal
   axis. Immediate one-step retraction kill; no pilot.
4. **OIH — overlap-interval hull propagation.** Fix labelled nonempty
   closed integer intervals $I_1,\ldots,I_m\subseteq[1,N]$. Simultaneously
   replace $I_i$ by the hull of all old $I_j$ intersecting old $I_i$.
   With $G$ the old intersection graph, each new interval is exactly the
   union over its closed $G$-neighbourhood, and the new graph is $G^3$.
   Its iterate is the union of original intervals at distance at most
   $(3^t-1)/2$. Thus the appealing logarithmic clock is a lifted graph-power
   / semilattice-union mechanism, not a fresh temporal axis. Kill that
   mechanism before any inverse work; no pilot.

## Additional preliminary exclusions, not four more candidates

Decreasing-run right rotation was considered by name but is already literal
old C01_DRF. RSK row-word transposition and first Knuth scheduling are also
explicit old kills. They are not fresh slate entries or new executions.

## Pilot execution boundary

One standalone source, no imported project code or data, zero GPU, no random
seed. `/usr/bin/python3.10 -I -S -B` is used with an explicitly empty
environment plus `PATH` and `LC_ALL`; a 60-second external timeout bounds
the single science invocation. The script prints every box summary,
independent orbit/decoder assertion totals, loaded module paths and loaded
native-library paths. Native command return and full combined output are
retained without claiming separately captured stdout/stderr. Relevant
runtime paths and the source are pinned; no host-wide map or historical
file copy is made. A fail remains a fail and does not trigger a larger box.

Storage observation before the pilot: 417,107,968 available workspace bytes;
15,472,173,056 under `/root`. These were observations, not reservations.
