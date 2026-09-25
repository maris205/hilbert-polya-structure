# Claim ledger — reversible divisor-scan control

**Scope ID:** `ASFS-SCOUT-20260918-NCF01`  
**Candidate ID:** `ANG-20260918-RDS01`  
**Status:** `FULL REVERSIBLE OWNER; PRIME SCAN CLOCK — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

| Claim | Evidence in the paper | Boundary |
| --- | --- | --- |
| h is bijective on all integers at least 2 | Lemma 1, disjoint exhaustive image classes and formula (3) | All branches, including 3→2 and inverse 2→3 |
| C and R are bijections of the entire X | Lemma 1, complete divisor-hit fibres and predecessor scan | No hit/non-hit image collision or missing states |
| F has inverse R⁻¹∘C⁻¹ | Lemma 1 | Composition order matters; no extra register |
| The source integer actually changes | Proposition 2, F(4,1)=(8,2) with exact inverse | A source-change witness only, not global escape or prime generation |
| Each prime fibre and the whole composite sector are invariant | Section 3 after Proposition 2: hit outputs and inverse outputs remain composite | Source updates occur among composites; no dynamically generated prime labels |
| S is Hausdorff and φ is a complete two-sided flow | Theorem 3, open-and-closed orbit components and formula (4) | Entire discrete carrier retained; unit roof never changed |
| Every finite F-cycle of least length m gives physical time m | Theorem 3, return subgroup mZ | Generic owner statement; composite finite cycles not classified |
| Each prime fibre gives one primitive circle | Theorem 4 | All p−1 phases are one packet; no auxiliary counter multiplicity |
| Prime least physical times are p−1 and repeats r(p−1) | Theorem 4, actual unit suspension | p=2 base fixed point gives a nonstationary circle of time 1 |
| The frozen prime clock equals log p | FALSE; Theorem 4, strict inequality (5) | Target-clock scoped FAIL for every prime |
| A fixed time-unit multiplier restores logarithmic scale | FALSE; Theorem 4, (p−1)/log p≥(√p+1)/2→∞ | Same unit-clock discriminator; no changed roof is installed |
| Removing C supplies prime selection | FALSE on the separate C=id control | Every n-fibre then returns with time n−1 |
| h alone excludes composite F-cycles | NOT ESTABLISHED; invalid inference | F=C∘R requires its own recurrence analysis |
| All composite cycles / full packet multiplicity | OPEN / NOT CLASSIFIED | Not required after this clock stop |
| Source and clock naturalness | OPEN | Declared cyclic scan and parity transport are designs |
| Same-object trace / zeta / determinant / quantum owner | NOT SUPPLIED | No later owner rescues the clock |
| BFT01 or the NCF01 scope receives RDS01 results | NOT CLAIMED | Distinct owner and search scope remain separate |

T0 is established; T1 has a source-update result and target-clock scoped FAIL;
T2 is established only for the prime fibres and the general repetition
convention. T3 is NOT SUPPLIED. Classical A0/A1/A2 are NOT APPLICABLE.
The [card](candidate-card.md) is unchanged in its mathematical inputs;
the [paper](paper.md) supplies exact proofs; the
[evidence record](evidence/README.md) separates actual checks from claims.
