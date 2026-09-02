# Primary-source verification and subtraction — P159

**Access date:** 2026-09-02 UTC  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

Primary publisher records, bibliographic records, arXiv pages, and
author-hosted manuscripts were used to fix metadata and claim boundaries.
Search results were routing aids only.  A bounded non-hit is not evidence of
novelty, priority, ownership completeness, or release readiness.

## Verified cited sources

| Key | Primary or authoritative record | Owned material subtracted | Relation to P159 |
|---|---|---|---|
| `NowakowskiOttaway2005` | R. J. Nowakowski and P. Ottaway, “Vertex Deletion Games with Parity Rules,” *Integers* 5(2), A15 (2005), [EuDML record](https://eudml.org/doc/129047), [author manuscript](https://www.mathstat.dal.ca/~ottaway/VDel.pdf) | sequential parity-restricted single-vertex deletion games | direct neighbouring rule family; no simultaneous deterministic atlas |
| `Kruger2014` | O. Krüger, “Note on Odd/Odd Vertex Removal Games on Bipartite Graphs,” *Integers* 14, G07 (2014), [journal PDF](https://emis.de/ft/4413), [arXiv:1304.7997](https://arxiv.org/abs/1304.7997) | sequential odd/odd removal, terminal even positions, and Grundy analysis on bipartite graphs | closest odd/odd vocabulary owner; fixed-even observation receives zero credit |
| `CyganEtAl2014` | M. Cygan, D. Marx, M. Pilipczuk, M. Pilipczuk, and I. Schlotter, “Parameterized Complexity of Eulerian Deletion Problems,” *Algorithmica* 68, 41–61 (2014), DOI [10.1007/s00453-012-9667-x](https://doi.org/10.1007/s00453-012-9667-x) | chosen vertex/edge deletions to obtain even or connected Eulerian graphs; complexity results | optimization/decision owner, not the forced current-odd-set update |
| `DabrowskiEtAl2016` | K. K. Dabrowski, P. A. Golovach, P. van 't Hof, and D. Paulusma, “Editing to Eulerian Graphs,” *Journal of Computer and System Sciences* 82(2), 213–228 (2016), DOI [10.1016/j.jcss.2015.10.003](https://doi.org/10.1016/j.jcss.2015.10.003), [arXiv:1410.6863](https://arxiv.org/abs/1410.6863) | prescribed degree-parity editing under selected operations | parity-editing framework, not OVP inverse dynamics |
| `JiangMitzenmacherThaler2014` | J. Jiang, M. Mitzenmacher, and J. Thaler, “Parallel Peeling Algorithms,” SPAA 2014, 319–330, DOI [10.1145/2612669.2612674](https://doi.org/10.1145/2612669.2612674), [arXiv:1302.7014](https://arxiv.org/abs/1302.7014) | simultaneous deletion of all vertices below a degree threshold in random hypergraph peeling | owns generic parallel-peeling vocabulary; not an odd-parity predicate or exact inverse atlas |
| `Diestel2017` | R. Diestel, *Graph Theory*, 5th ed., Graduate Texts in Mathematics 173, Springer (2017), DOI [10.1007/978-3-662-53622-3](https://doi.org/10.1007/978-3-662-53622-3) | standard graph notation, degree parity, incidence and cycle-space background | textbook support only; no contribution credit |

All six bibliography entries are cited in `main.tex`.  No uncited entry is
retained, and the final BibTeX run reports no missing entry or metadata error.

## Direct-owner subtraction

P159 assigns no contribution credit to:

1. parity-constrained vertex-deletion games or their terminal positions;
2. Eulerian/even graph deletion and prescribed-parity editing problems;
3. generic simultaneous or parallel peeling;
4. the handshaking lemma and the even cardinality of the odd-degree set;
5. rank `v-1` of a connected binary incidence matrix;
6. cycle-space enumeration of even graphs;
7. rank–nullity, binomial label selection, matrix powers, absorbing sums, or
   generic finite-state dynamics;
8. the path witness and the sharp rank-loss clock considered by itself.

The retained conjunction is:

```text
target-uniform strict parity-extension count
+ correctly oriented literal transfer powers
+ even/non-even every-time fibre split
+ exact image and temporal CDF consequences
```

## Replayable bounded search ledger

The owner screen used generic terminology rather than repository theorem
phrasing.  Query families included:

```text
"delete all odd-degree vertices" graph simultaneously
"simultaneous odd-degree vertex deletion" graph
"parallel odd-degree vertex deletion" graph
"parallel odd-degree peeling" graph
"odd-degree peeling" graph
"parity peeling" graph vertices
"all vertices of odd degree" removed graph iteration
"odd/odd vertex removal" graph
"odd degree stripping" graph
"Eulerian vertex deletion" graph
"Eulerian core" graph "odd degree" deletion
site:arxiv.org "odd-degree vertex deletion"
```

The bounded returned corpus supplied sequential games, chosen
Eulerian/parity edits, and unrelated threshold-based parallel peeling.  It did
not supply a checked source stating the literal simultaneous map together with
the target-uniform `B_n` and its every-time fibre/image/CDF package.  This is a
scoped search record only.  The direct owner question remains **unresolved,
not cleared**, and any later direct source reopens the claim boundary.

## Terminology firewall

- “Even graph” means all degrees are even; it need not be connected.
- “Eulerian” is used only when describing cited literature with its stated
  connectivity conventions.
- “Parallel peeling” is background vocabulary, not a contribution label.
- No sentence may turn the bounded search into “first,” “novel,” or “no prior
  work.”
