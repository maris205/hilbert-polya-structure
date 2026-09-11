# P201 Review A — source and historical owner audit

Date: 2026-09-05 UTC. Bibliography checked: all three frozen records.
Disposition: exact internal prior-map collision; external search remains
bounded. No source non-hit establishes novelty, and no manuscript was sent
to an external model. The records below distinguish inspected primary
material from search leads and inaccessible full documents.

## Decisive internal owner: OCL, previously killed rather than reserved

Read the literal row and surrounding disposition in
`docs/papers162_166_sequence/scouting/replacement_adaptive_maps/SCOUT.md`:
lines 39–42 declare the other 25 proposals killed, with no hidden reserve;
line 81 identifies OCL as `KILL_FUNCTIONAL_GRAPH_SUMMARY_THIN`.
Read the implementation at `verify_scout.py` lines 427–438. It traces the
orbit beginning at i until a repeated label and returns the cycle length,
then writes that length modulo n in output position i. Thus
`O(f)(i)=ell_f(i) mod n` on precisely the same labelled carrier as P201.
This is not the cycle containing i (i may be transient), the output at
f(i), or a component-size statistic. The source and canonical historical
bytes are pinned without modifying the old package.

The n=5 record has image 60, one fixed point, maximal tail 3 and maximal
fibre 1296. These agree with P201, but the decisive evidence is the explicit
all-n conjugacy `O o H=H o P`, `H(f)=sigma f sigma^{-1}`,
`sigma(i)=i+1 mod n`, proved in `PROOF_REDERIVATION.md`. The conjugacy even
preserves rank, so the new rank-threshold/equality theorems do not escape
the prior operator by changing a marked statistic. Their mathematical
proofs were not in the old scout and are not falsely credited to it; they
are new deductions about an old killed map. The batch's central anchor
disallows counting such a map as a new subclass.

The neighboring BAS row 82 uses weak-component size modulo n and is also
explicitly killed. It is a relevant summary-map sibling, but no exact
conjugacy with BAS is claimed or needed. OCL is a strictly stronger
collision than the manuscript's named P137/P167 comparisons.

## Other internal boundaries actually rechecked

- P137: read its group/rank literal and threshold argument. Its map splits
  finite abelian p-group data by image and kernel, with a different rank
  trajectory and a linear triangular clock. No exact EPF operator transfer
  was inferred from those formulas alone.
- P167: read the minimum-preimage update with default self-value, involution
  recurrence, linear tail bound and inverse description. Those are not the
  same update as cycle-period feedback. Again, OCL now supersedes this as
  the nearest exact prior map.
- The current word/poset lane's statistics-writeback exclusion is genuinely
  recorded; the author and Stage-1 record had interpreted it as lane-scoped.
  That interpretation is not used to waive the new collision. The central
  problem anchor independently and explicitly bans conjugates of earlier
  killed maps, so this rejection does not depend on resolving the broader
  statistics-writeback interpretation.
- Historical coverage uses the recovery/index/search surface and the named
  primary files, not a claim that every P1–P196 manuscript was freshly read.
  The known missing P51–P56 manuscript caveat remains in force. The positive
  OCL hit makes that missing coverage immaterial to this rejection, not
  magically complete.

## All frozen bibliography records

| Record | Primary material inspected | Verified attribution and subtraction | Access boundary |
|---|---|---|---|
| Doré, Formenti, Porreca, Riva, arXiv:2208.08310v2 | [Version-2 HTML](https://arxiv.org/html/2208.08310v2), metadata, introduction and §2 definitions | Four authors, version 2 dated 6 September 2022; feedback there is a cyclic vertex's return period and the main operation is a direct product of systems | No assertion that every later result was read; the inspected operation is not numeric cycle-length writeback |
| Flajolet and Sedgewick, *Analytic Combinatorics*, Cambridge 2009 | [Author book site](https://ac.cs.princeton.edu/home/), primary indexed PDF excerpts for mappings/SET/CYC/Cayley trees, and [publisher metadata](https://www.cambridge.org/core/books/analytic-combinatorics/7E37474C43E9B95C90BEDE082CF28708) | Authors, publisher, 2009 print date and DOI 10.1017/CBO9780511801655 verified. Standard functional-graph components and labelled SET/CYC enumeration receive zero novelty credit | No claim of reading the full book. DOI redirect itself failed in the browser; the publisher's indexed record supplied the DOI and distinguishes its 2011 digital date |
| Stephan Wagner, *Enumeration of Highly Balanced Trees*, *Ars Combinatoria* 114 (2014), 15–32 | [Author publication list](https://math.sun.ac.za/swagner/pub.html) and indexed primary [paper §4](https://math.sun.ac.za/swagner/balanced.pdf) excerpt | §4 explicitly gives the triangular recurrence and sequence 2,3,6,21,231,26796,..., identifying A007501. The numerical sequence itself is not new | Direct full-PDF browser retrieval timed out. The exact relevant §4 excerpt was read through primary-domain indexing; no full-PDF read is claimed |

The forest code and target product are independently proved in the
manuscript and review; their correctness does not rest on an inaccessible
book page. The cited standard static enumeration remains fully subtracted.
Likewise, the known sequence may have a new extremal interpretation without
being a new sequence. Neither distinction repairs OCL conjugacy.

## Search receipt and its ceiling

Public searches included the precise triangular values, the title of
Wagner's paper, primary book-domain mapping/CYC terms, and combinations of
eventual period, cycle length, feedback and iteration. Primary arXiv,
author-domain and publisher results were used for support; secondary OEIS
or general-index hits were leads only. We found no separate direct external
owner of the complete stated threshold/equality package in those inspected
results. This is a bounded non-hit, not a positive novelty conclusion.
The already-proved internal equivalence is sufficient for rejection and
does not require an external priority dispute.
