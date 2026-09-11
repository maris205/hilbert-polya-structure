# Fresh 54 — mutual-minimum matching deletion

2026-09-11, bounded author desk. **NO NOMINATION**: one literal inspected, zero surviving unoccupied candidates. No scientific execution, pilot, larger parameter box, child agent, paper assignment, central edit or Git operation. Fresh52's preserved construction is not reopened.

## Literal and elementary temporal feasibility

Fix a finite simple graph $G=(V,E)$ and a strict total order $\prec$ on its edges. The finite autonomous carrier is $2^V$. For $S\subseteq V$, let $M(S)$ be the edges of $G[S]$ that precede every other edge incident with either endpoint in $G[S]$. Update

$$T(S)=S\setminus V(M(S)).$$

The strict order implies that distinct edges in $M(S)$ cannot share an endpoint, so this is simultaneous matching deletion. It has no changing priorities, external clock or random update. The phrase “mutual minimum” refers to being the least remaining incident edge at both endpoints.

**Provable elementary statement.** A state is fixed precisely when $S$ is independent in $G$. Every orbit stabilizes and has entrance time at most $\lfloor|S|/2\rfloor$. This bound is attained on a path with edges ordered increasingly from one end, starting with every vertex present.

**Proof.** If $G[S]$ has an edge, its globally least edge belongs to $M(S)$, so at least two vertices disappear. If $G[S]$ has no edge, $M(S)$ is empty and $S$ is fixed. No nontrivial cycle is possible under strict set decrease. On the ordered path, the first remaining edge is the sole local minimum; each other edge has a smaller edge immediately to its left. The update removes the first two vertices of the remaining path. Repeating gives exactly $\lfloor|S|/2\rfloor$ rounds. Empty and singleton states have time zero.

The inverse axis was not closed: the definition $T(Y\cup A)=Y$ is only a preimage test, not an evaluated fibre theorem. No generic subset enumeration is substituted for the missing independent mechanism. The elementary extremal path argument also uses the same greedy-deletion mechanism, not a separate axis.

## Exact archive subtraction before further development

Actual originals read:

- `docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md`, the B01 literal and substantive clock/basin/disposition section, lines 166–228. That map sequentially completes the least unmatched left vertex with the least unused right vertex. It is not this synchronous local-minimum deletion. Its historical `KILL_PORTFOLIO` restriction on further greedy matching is recorded as historical context, not silently promoted into a new blanket prohibition overriding the current scouting instruction.
- `docs/papers211_215_sequence/scouting/finite_ordered_interaction_fresh_desk/REPORT.md`, completely read. GBPR is a best-blocking-pair repair on perfect matchings, with a displaced-partner repair and a fixed-target flip-distance clock. It is not identified with the present subset-deletion rule merely because both use a strict edge order.

The broad initial text search also returned historical copies and was partly truncated in combined display. Only the explicitly read original sections above support these detailed local comparisons; no exhaustive archive-absence claim is made.

## Direct primary owner and deterministic boundary

The actual primary PDF [Fischer and Noever, *Tight Analysis of Parallel Randomized Greedy MIS*](https://arxiv.org/pdf/1707.05124), arXiv v3 dated 16 May 2019, was opened. Printed pp. 10–11, Section 3.1, defines parallel greedy maximal matching by choosing an edge order once, then repeatedly deleting all locally minimal edges and their incident edges. Its proof identifies this with greedy MIS on the line graph. Printed p. 1 also explains that the chosen order remains fixed throughout. These selected passages were read; no full-paper review is claimed.

For exact subtraction, write $R(S)=E(G[S])$. If $D$ is the source's residual-edge update with the fixed order, then

$$R(T(S))=D(R(S)).$$

Indeed, an edge remains after deleting the endpoints of $M(S)$ exactly when it meets none of the selected edges. Those are exactly the residual edges in the source rule. Moreover $T(S)=S$ if and only if $R(S)$ is empty, and any nonempty edge set loses at least its least edge under $D$. Thus the number of rounds to our fixed state is exactly the source process's edge-exhaustion time. Retained isolated vertices do not introduce a temporal residual.

Fixing one sampled priority order makes that already-defined process deterministic; it does not create a new update. The paper's high-probability logarithmic bound is **not** asserted for every fixed order: the path example above has a linear worst-case clock. No probability claim is used in this desk.

## Disposition

**NO NOMINATION / DIRECT OWNED TEMPORAL FACTOR.** The surviving subset labels can affect inverse fibres, but the entire temporal axis is already the fixed-priority greedy-matching process. No independently substantial inverse/extremal theorem was found before that subtraction. This bounded attempt therefore stops without a second literal, a special-case enlargement or a pilot request. This is an author source-and-value assessment, not global novelty clearance or an independent review PASS.

The project research skill directed early literal/source subtraction; proof-writer supplied explicit assumptions, the short deductive check and its boundary. Native source/read calls are available in the conversation, but no immutable raw-source package is claimed here.
