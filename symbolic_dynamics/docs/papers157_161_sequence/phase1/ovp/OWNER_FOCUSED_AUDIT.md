# Owner and collision audit — parallel odd-vertex pruning

Verdict: **PASS_NARROW / HOLD_EXTERNAL**.  The search is bounded and supplies
neither a novelty claim nor a priority certificate.

## External subtraction

The following neighbouring literatures were treated as owned input.

| source | owned material | residual here |
|---|---|---|
| R. J. Nowakowski and P. Ottaway, *Vertex Deletion Games with Parity Rules*, Integers 5(2) (2005), A15 ([author copy](https://www.mathstat.dal.ca/~ottaway/VDel.pdf)) | sequential parity-constrained vertex deletion as a combinatorial game | no game, choices, or Grundy claim; the deterministic simultaneous update and inverse transfer are not supplied |
| O. Krüger, *Analysis of Odd/odd vertex removal games on special graphs*, arXiv:1304.7997 / Integers 14 (2014), G07 ([arXiv](https://arxiv.org/abs/1304.7997)) | sequential odd/odd game, especially bipartite Grundy values | zero credit for parity-deletion vocabulary; no parallel orbit/fibre atlas |
| M. Cygan et al., *Parameterized Complexity of Eulerian Deletion Problems*, Algorithmica 68 (2014), 41–61 ([DOI](https://doi.org/10.1007/s00453-012-9667-x)) | optimization problems asking for vertex/edge deletions that produce connected all-even graphs | no optimization or complexity claim; their chosen deletion set is not the current odd-degree set iterated synchronously |
| standard handshaking, binary incidence-rank, and cycle-space theory | even cardinality of the odd set, rank `v-c`, and the number of even graphs | all receive zero contribution credit; the residual begins with the target-uniform strict inverse system and its exact iteration |

Queries included exact-phrase and mechanism variants of `delete all
odd-degree vertices simultaneously`, `parallel odd-degree vertex deletion`,
`iterated odd vertex pruning`, and `graph dynamics odd-degree deletion`.
The returned primary literature concerned sequential games, prescribed
Eulerian deletion, edge deletion, or unrelated parallel knockout schemes.  No
record located in this bounded search stated the literal simultaneous map or
the `B_n` every-time fibre theorem.

## Internal collision firewall through P156

| occupied paper | apparent overlap | decisive separation |
|---|---|---|
| P114 rooted-forest leaf peeling | a labelled carrier on subsets and simultaneous vertex deletion | P114 deletes nonroot leaves and its clock is forest height; OVP acts on every simple graph, deletes a global parity class, and its inverse is one connected binary incidence system with target-independent rank transfer |
| P123 odd-component complementation | parity language on labelled graphs | P123 preserves vertices and complements selected components; OVP changes the vertex set and never complements an edge |
| P141 random threshold MIS | graph vertex removal | P141 is random greedy threshold selection; OVP is deterministic and its full inverse tower is linear parity algebra |
| P146 random ear deletion | iterative deletion from graphs | P146 works on maximal outerplanar graphs and probabilistic ears; OVP has unrestricted graphs, deterministic simultaneous epochs, and even-graph endpoints |
| P148 even-level tree contraction | simultaneous contraction and all-time fibres | P148 promotes ordered grandchildren with a Catalan/tree grammar; OVP deletes vertices outright and uses incidence-rank transfer powers |

The permanent “another pruning process” exclusion does not automatically
kill OVP because the main theorem does not transfer from a pruning depth or a
tree grammar: its central axis is the exact, target-uniform parity-extension
space and the nilpotent matrix that counts every iterate.  The temporal bound
alone would be below paper scale and must not be presented independently.

## Claim ceiling

Retain only the conjunction of sharp clock, strict inverse incidence theorem,
all-time every-target fibres, exact image layers, and temporal census.  Do not
claim the handshaking lemma, parity games, even-graph enumeration, Eulerian
deletion, generic pruning, matrix powers, or zeta conversion.  External
release remains on hold pending later hostile review.
