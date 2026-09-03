# Hostile Review B — P181 first-descent prefix reversal

**Reviewer process:** root, independent of the stochastic author lane and
Reviewer A's algebra/factoradic process.  
**Reviewed `main.tex`:**
`95909031cae2c75f09399452a472597e72a1bf3a91d10cf4286df54e54e2fb82`.  
**Reviewed Round-1 PDF:**
`57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

## Independent construction

I represented permutations as digit strings and constructed the first-descent
update, incoming sets, and orbit coordinates directly.  This differs from the
author's tuple/permutation-table organization and Reviewer A's factoradic
rank arrays with indegree peeling.  Complete string-state graphs through
`S_8`, direct predecessor-set equality, tail/period traversal, and an explicit
follower-to-front negative-control map make **377,591 exact assertions**.
Two fresh processes reproduce `CANONICAL.txt` byte for byte.

## Claim audit

- Every nonfixed output begins with the reversed descent pair and therefore
  lies in the ascent half.  Reversing the first two entries gives a source for
  every ascent target, proving the exact half-image.
- A position-two peak invokes `rho_3`, remains a peak, and returns after the
  second reversal.  Every other nonidentity image state has its first descent
  later and maps into this peak core.  This gives exactly one fixed point and
  the claimed two-cycles.
- For each target, I compared the *full set* of incoming strings with all
  reversals indexed by its decreasing run, adding the identity predecessor
  exactly once.  This confirms the inverse formula, not merely fibre sizes.
- Direct orbit traversal reproduces every depth population and confirms no
  tail exceeds two.  Full-run targets have the stated maximum fibres and the
  computed maximizer set agrees exactly through `S_8`.
- The repaired `S_1` atlas is now complete: its one state is fixed, is the
  whole image/recurrent core, has depth zero, and has one predecessor.  The
  `S_2` and `S_3` exceptional atlases also match their literal arrows.

## First Sort and ownership firewall

The Project Euler follower-to-front operation is not this map.  The reviewer
implements both literal rules and confirms the manuscript witness
`1324 -> 2314` versus `1324 -> 2134`.  Prefix-reversal operations, pancake
distance, longest-increasing-prefix selection, descent/peak counts, and
generic finite-map bookkeeping receive zero contribution credit.  P122,
P117, killed FDF, and conjugate FAR are subtracted consistently.

The three bibliography records and their limited roles agree with the source
ledger.  No bounded non-hit is used as novelty or clearance.  A direct owner,
a change from prefix length `d+1`, or conflation with First Sort remains a kill
switch.  None fired; `OWNER_AMBER / HOLD_EXTERNAL` is mandatory.

## Artifact and disposition audit

The author verifier replays to its 6,273,070-assertion transcript, and the
paper manifest passes 16/16 entries.  The live PDF equals
`main_round1.pdf`, differs from the preserved Round-0 PDF, has three A4 pages,
blank identifying metadata, and embedded/subsetted fonts.  The repaired
proposition does not invoke `rho_2` at `n=1`.  There are no open Reviewer-B
findings.
