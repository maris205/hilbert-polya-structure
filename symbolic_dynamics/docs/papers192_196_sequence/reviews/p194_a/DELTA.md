# P194 Review-A delta

**Decision:** `ORIGINAL_A_ACCEPTED_NO_CHANGE +
POST_B_REPAIR_ACCEPTED_NONREGRESSION`  
**Round-0 mathematical delta:** none.  
**Round-0 source/owner delta:** none.  
**Round-0 build/presentation delta:** none.  
**Post-B mathematical/control delta:** none.  
**Post-B source delta:** accepted nearest-owner citation and zero-credit repair.  
**Post-B build delta:** expected four-to-five-page reflow; clean and deterministic.  
**Open findings:** `0 Critical / 0 Major / 0 Minor`.

| ID | Severity | Surface | Required change | State |
|---|---|---|---|---|
| — | — | — | No change requested. | ACCEPTED |

## Accepted post-B source-only delta

The original Reviewer-A decision remains an exact no-change acceptance of the
preserved Round-0 inputs.  Review B subsequently found the nearer
Defant--Williams crystal pop-stack surface.  Relative to the exact old source
copies used for Review A, the accepted repair changes only:

- the abstract, to zero-credit existing crystal pop-stack sorting;
- one comparison paragraph, which cites and describes that map and separates
  it from the literal P194 update;
- the closing subtraction paragraph, to repeat the zero-credit boundary; and
- `references.bib`, by adding the `DefantWilliams2022` record.

The Round-0/current manuscript source hashes are respectively
`c0e4c3291fc5d3f5de1df64094c89bc7325b2372a279f09a430f39697957bfcf`
and
`d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9`;
the bibliography hashes are respectively
`b4649d9e22a34a005706625be2472204b1275a722a085dfd19a0b04abd471a54`
and
`b8ab897d271bd4225dc71c4619fb5cbe6843afdc3d6a529705a927d37ce38faa`.
All six theorem-like statement environments are byte-identical before and
after the repair.  The map, proofs, 16 numbered-equation labels, author
verifier, reviewer verifier, and both canonical transcripts are unchanged.

The current PDF is necessarily different because the added source occupies a
fifth page.  Two cold builds reproduce the live five-page PDF at
`682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b`.
The original and Round-1 four-page snapshots remain byte-identical at
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.
This accepted repair is not a mathematical amendment and creates no finding.

The acceptance preserves the manuscript's limiting declarations:

- Kashiwara operators, type-A word crystals, highest-weight components,
  tensor signatures, reverse RSK, Schur/principal specialization, hook
  formulas, tableaux, and the involution correspondence receive zero
  contribution credit;
- a generic least/leftmost scheduler, monotone rank, and generic finite-map
  fibre bookkeeping receive no separation credit;
- the bounded external-owner non-hit is not evidence of novelty, priority,
  completeness, independence, or freedom to operate; and
- the binding release state remains `OWNER_AMBER / HOLD_EXTERNAL`.

Any later edit to a pinned source, control, or PDF invalidates this combined
original acceptance and post-B nonregression acceptance until Reviewer A
checks the exact new delta and fresh pins.
