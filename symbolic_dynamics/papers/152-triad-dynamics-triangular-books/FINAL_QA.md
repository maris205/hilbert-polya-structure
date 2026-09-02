# Final internal QA — P152

**Date:** 2026-09-02 UTC.  
**Status:** ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.  
**Surviving severity:** 0 Critical / 0 Major / 0 Minor.

This is the consolidated proof/source/evidence/build/visual audit after both
internal reviews.  Review A returned `REVISE — 0 Critical / 0 Major / 2
Minor`, and Review B returned `REVISE — 0 Critical / 0 Major / 1 Minor`.
Every finding is closed in source and itemized in `IMPROVEMENT_LOG.md`.  No
external model or review service was used.

## Review-A closure

1. **m1, incomplete manifest — closed.**  The Round-1 manifest excludes
   itself and covers all 27 other retained paper-local files, including both
   historical PDFs, the raw review, improvement log, ledgers, sources,
   verifier/transcript, and retained LaTeX products/logs.  A cold checksum
   replay and an independent filename-set comparison both pass 27/27.
2. **m2, narrow inverse/certificate lane — closed by expansion.**  The new
   exact verifier compares the inverse criterion with a complete bounded
   literal image on 7,335 Fraction candidate pairs (69 accepted and 7,266
   rejected), tests 12 gate-specific infeasible pairs and both printed scalar
   collisions, recovers the exact all-private block probability from 8,190
   weighted type words, and checks 546 finite tail inequalities.

The finite audit is still counterexample pressure.  The symbolic converse and
Markov block iteration remain the proof of the all-parameter statements.

## Review-B closure

1. **m1, arbitrary-candidate domain — closed.**  The theorem now declares
   every candidate with `m<=0` or `q` outside `(0,1)` infeasible before
   forming `R`.  The proof, proof package, claims ledger, and control ledger
   use the same order.  The integer-square, `R>=3`, integral-count, and
   admissible-count iff conditions are unchanged.
2. The verifier and transcript did not require modification: their negative-
   mean sentinel already rejects the candidate before any real square root.

## Contract and proof audit

The manuscript remains inside the frozen P152 ceiling and proves each
permitted interface for arbitrary `r>=1` and `1<=k<=r`.

1. **Literal process and clock.**  The triangular book is explicitly
   `B(3,r)=K_{1,1,r}` with a common edge.  `T` counts active imbalanced-triad
   update epochs and `J` counts only spine flips.  The AKR 2005 all-triad clock
   and its no-op holds are separated.
2. **Strong quotient.**  Either private choice clears one selected bit, while
   the spine complements all bits.  Coincident targets are explicitly merged.
3. **Joint transform.**  The reflection is eliminated without dividing by
   `u`; the terminal Bellman equation determines `F_1`; removable boundaries
   are taken from the Bellman system.
4. **Boundary cases.**  `r=1`, the `r=2,k=1` self-loop and `(3+zu)`
   cancellation, `z=0`, coincident arrows, `q=1/2`, the friendship carrier,
   uniform weights, and the active clock all remain visible.
5. **Mean and extrema.**  The reflected mean system reduces to second
   difference `-1`; the terminal condition fixes the quadratic, and the exact
   endpoint/vertex comparison gives all equality cases.
6. **Parity and inverse.**  The affine signed-Bellman solution is justified by
   almost-sure absorption.  The feasible image contains both iff directions,
   exact integer tests, uniqueness, and both single-statistic collisions.
7. **Absorption.**  An `r`-long private-type block forces absorption;
   conditional block iteration gives the exponential tail.

No full sign-state recovery, noisy stability, nonuniform dynamics, arbitrary
graph theorem, generic convergence theorem, or friendship/windmill result is
claimed.

## Owner and citation audit

- The manuscript subtracts both Antal--Krapivsky--Redner primary records,
  Istrate's same-kernel/XOR record, the Istrate--Bonchis--Marin hypergraph
  descendant, and the Sehrawat--Bhattacharjya signed-book record.
- All 5 bibliography entries are primary/author-hosted, cited, and resolved.
- Kernel, representation, carrier, static class count, generic finite-chain
  tools, and generic convergence language receive zero credit.
- The bounded source non-hit is not presented as novelty, priority, ownership
  completeness, or external clearance.

## Exact-control QA

- A fresh process matched `verification_output.txt` byte for byte.
- Result: PASS, 199,581 exact integer/rational assertions.
- Transcript SHA-256:
  `da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083`.
- Lane accounting:
  `4,416 + 7,655 + 180,600 + 2,026 + 3,958 + 648 + 278 = 199,581`.
- No floating-point arithmetic, randomness, network access, or third-party
  package occurs in the verifier.

## Build and visual QA

| Check | Accepted Round-2 value |
|---|---|
| Current / Round-2 freeze | `main.pdf` / `main_round2.pdf`, byte-identical |
| Pages / size | 5 A4 pages / 338,933 bytes |
| SHA-256 | `6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6` |
| Historical Round 1 | `main_round1.pdf`, 339,258 bytes, SHA-256 `2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9` |
| Historical Round 0 | `main_round0_original.pdf`, 338,268 bytes, SHA-256 `f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57` |
| References | 5/5 cited and resolved |
| Isolated builds | two source-only builds, mutually identical and equal to current |
| Settled log | no unresolved citation/reference, rerun request, error, overfull, or underfull box |
| PDF | A4, unencrypted, no forms/JavaScript, blank identifying metadata |
| Fonts | 25/25 reported rows embedded, subsetted, Unicode mapped |
| Visual inspection | 5/5 pages accepted |

Visual inspection covered the ownership table; complete theorem; `r=1`,
`r=2`, and `z=0` display; equations (13)--(18); inverse collisions; repaired
candidate-domain gate; expanded exact-audit table; declarations; and
bibliography.  No clipping, overlap, blank page, corrupt glyph, unresolved
marker, or identifying leak was found.

## Author decision

Both Review-A Minors and the Review-B Minor are repaired in source and
evidence rather than merely marked closed.  The Round-2 package passes the
proof, owner-boundary, exact-control, reproducibility, and visual gates with
zero unresolved severity and is accepted internally.  Scoped repository
synchronization is governed by the standing batch authorization; posting,
submission, circulation, author contact, novelty/priority statements, and
external release remain unauthorized.  External status stays `HOLD_EXTERNAL`.
