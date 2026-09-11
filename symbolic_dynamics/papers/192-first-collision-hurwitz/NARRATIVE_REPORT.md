# Narrative Report

Status: `OWNER_RED_AMBER/HOLD_EXTERNAL`. This report explains the internal mathematical case; it makes no novelty claim.

## The object in one paragraph

A minimal factorization of the long cycle is a word of (n-1) transpositions. Each transposition has a lower endpoint. Read the word from left to right, find the first adjacent equality among those lower endpoints, and perform the classical right Hurwitz move at that position. If there is no equality, stop. The local move is standard; the deterministic, state-selected scheduler is the only new object under analysis.

The key local calculation is unusually rigid. A collision has the form

\[
(a,b),(a,c)\longmapsto(a,c),(b,c),\qquad a<b,c.
\]

Its first lower endpoint stays (a), while the second becomes \(\min(b,c)>a\). Earlier comparisons do not change, and the active comparison ceases to be equal. Hence the next active position, if any, lies strictly to the right. That observation drives the temporal theorem package without introducing a quotient or canonicalization map.

## The four proved axes

### Temporal normal form

Every update history is a strictly increasing subset of ([n-2]). No nontrivial cycle can occur, every state reaches a fixed point, and the tail is at most (n-2). The factorization

\[
((1,n),(1,2),(2,3),\ldots,(n-2,n-1))
\]

executes at (1,2,\ldots,n-2), so the bound is sharp.

### Fixed census

Fixed states are precisely those whose lower-endpoint word has unequal adjacent entries. The classical lower-endpoint bijection sends minimal long-cycle factorizations to parking functions of length (N=n-1). Pollak's circular parking model counts the adjacent-unequal parking functions: there are ((N+1)N^{N-1}) circular preference words before quotienting by translation, and therefore (N^{N-1}=(n-1)^{n-2}) fixed states.

### Every-target inverse atlas

For a labelled target (y=(\sigma_1,\ldots,\sigma_{n-1})), let (j(y)) be its first lower-endpoint collision, or (n-1) if it is fixed. For (i<j(y)), write \(\sigma_i=(a,b)\) with (a<b). The index (i) contributes exactly one nonself predecessor precisely when \(\sigma_{i+1}\) contains (b) and its other endpoint is greater than (a). This is an exact target-resolved test, not a fibre average.

### Extremal fibre

A fixed target has at most its self-predecessor plus one inverse at each of (n-2) positions, while a nonfixed target has fewer eligible positions. The adjacent chain

\[
((1,2),(2,3),\ldots,(n-1,n))
\]

attains indegree (n-1). Equality forces strictly increasing lower endpoints; the parking inequalities then force the word ((1,2,\ldots,n-1)), whose factorization is unique under the classical bijection. Thus the maximizer is unique.

## The tempting fifth axis is not closed

For every subset (I\subseteq[n-2]), computation suggests

\[
\#\{f:\operatorname{Hist}(f)=I\}=(n-1)^{n-2-|I|}.
\]

The Python verifier exhausts (2\le n\le8); an independent C++ program streams every Prüfer word at (n=9). These are exact finite checks. They do not furnish the missing all-(n) bijection. In particular, the ordinary factorization-tree correspondence does not automatically identify scheduler execution positions with occurrences of a distinguished Prüfer symbol. The manuscript therefore labels the formula, its binomial depth sum, and the general unique-deepest-state consequence as conjectural.

## Contribution subtraction

The following ingredients are classical and receive zero credit:

- the right Hurwitz action itself;
- Cayley's count of minimal long-cycle factorizations;
- factorization-to-tree and factorization-to-parking-function correspondences;
- Pollak's circular parking argument;
- ordinary Prüfer coding and its occurrence statistics.

The surviving internal package is the conjunction of a state-selected first-collision scheduler, the strict rightward history theorem, the sharp tail witness, the adjacent-unequal fixed census, and the every-target inverse atlas with a unique extremal fibre.

## Risk posture

The ordinary Hurwitz and parking-function surfaces have strong direct owners. The internal collision audit found no literal prior P1--P191 system with the full scheduler-plus-atlas package, but this is not external clearance. The manuscript's bounded non-hit is not evidence of novelty. Before any circulation, an external search must target priority/first-collision Hurwitz schedulers, greedy braid dynamics on minimal factorizations, and target-resolved reverse Hurwitz fibres. Until that is done, the status remains `OWNER_RED_AMBER/HOLD_EXTERNAL`.
