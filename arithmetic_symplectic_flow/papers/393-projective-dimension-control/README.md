# 393 — External projective dimension control

Candidate: `ANG-CONTROL-20260922-PDC01`.  
Batch: `NONUNIT-RETURN-20260922-I`, round 4/5, 2026-09-22.  
Outcome: `EXTERNAL DIMENSION CONTROL ESTABLISHED; MAIN-CANDIDATE ADMISSION STOP`

This is an EXTERNAL CONTROL, not a lineage-admitted main candidate. [Paper](paper.md) supplies the exact proofs; [frozen card](candidate-card.md) fixes all four full RP³ owners; [claim ledger](claim-ledger.md) separates established results from nonclaims.

## Complete result

For each owner independently, the round-volume IMAGE Jacobian is
`J_A([v])=|det A| ||v||⁴/||Av||⁴`, valid at every point and for every Borel transport set. Its integer-power cocycle is `c_A(k,[v])=−log J_(A^k)([v])`. All integer labels remain, including when projective maps coincide. All real heights, both directions and every projective point are retained.

| Full owner | Complete positive primitive physical ledger | Other points / adverse findings |
| --- | --- | --- |
| MAIN: `diag(B,I₂)`, B=((0,2),(1,0)) | Two irrational eigenline packets AND every point of a complementary RP¹ have least log 2; every other orbit in the first RP¹ is a two-cycle with least log 4 | Both positive packet families are continua; all mixed points are nonperiodic with H={0} |
| S: `2I₄` | None | Every point is fixed, c=0, source/extension isotropy Z, H={0} |
| D: `diag(2,1,1,1)` | One log-8 axis packet plus an entire complementary RP² of distinct log-2 packets | Every mixed point is nonperiodic; its nonunit zero-clock arrows are not isotropy |
| B-control: `diag(B₂,B₂)` | None | Two fixed RP¹s and all remaining two-cycles; retained isotropy Z or 2Z survives in the extension, H={0} everywhere |

For every positive primitive physical time L, the full stabilizer is exactly LZ and repetitions are rL, within the same packet. Equal times never merge different packets. The complete clock kernels, including nonperiodic-source arrows and B's larger zero-clock quadric, are derived in the paper; all lag kernels consist only of unit arrows. These are set-level height actions, not positive-roof suspension claims.

MAIN's irrational eigenlines have rational multiplier exp(L)=2 because the full RP³ Jacobian uses the fourth power of the eigenvalue. The corresponding one-dimensional invariant-line metric has a different Jacobian and zero return clock there. A self-contained rational RP¹ restriction is proved for comparison. No minimum dimension, universal higher-dimensional theorem, novelty or symbolic lineage is inferred.

## Gate and decision

External T0/T1/T2 ownership, clock and orbit bookkeeping is established. Strong arithmetic naturalness is NOT ESTABLISHED; classical A0/A1/A2 are NOT APPLICABLE; T3 NOT AUDITED; formal Route coordinates UNASSIGNED; B NOT INVOKED. The coefficient 2 was explicitly assigned and no prime-symbolic mechanism exists.

STOP main-candidate admission and retain the bounded dimension control for future screening. Do not attach symbolic labels afterwards or use the rational multiplier as target credit. Root owns CP2/CP3 and the card outcome append; this author handoff does not assert their completion.

## Reproduction and disclosure

Original 74-line card SHA-256: `42b57df25ae79aa9deb72de31997f96497361b0db4a24e43c733485f97cf9ecc`. Proof methods: polar integration, full Borel change of variables, exact matrix algebra and complete period classification. No scientific numerical run, cutoff, fitted roof, external source, PDF, publication or Git write was used.

Mechanical checks: `head -n 74 candidate-card.md | sha256sum`, `wc -l paper.md`, and local Node reads comparing IDs, exact Outcome strings and relative-link existence. These check document integrity only. The author read the whole frozen card, not other new manuscripts or raw/peer reports. Same-card author helper work checked the controls and is not independent review. Shared-history internal work is NOT_CALIBRATED; ARS claim-boundary discipline is disclosed in the paper.
