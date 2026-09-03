# Hostile stochastic/graph review — P178

**Reviewer process:** stochastic/graph lane, delta-closed against author Round 1.  
**Review mode:** read-only; no author file was modified.  
**Reviewed `main.tex` SHA-256:**
`d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603`.  
**Reviewed PDF SHA-256:**
`b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 OPEN /
HOLD_EXTERNAL`.

## Independent representation and evidence

The reviewer rebuilt every function as its coefficient vector in the
falling-binomial basis.  This is neither the author's table-of-values carrier
nor the discovery lane's integer encoding.  Vandermonde translation gives

\[
 (D_a c)_k=\sum_{j>k}\binom{a}{j-k}c_j,
 \qquad f(0)=c_0,
\]

so the state-selected update and the anchored inverse can be evaluated
without converting to value tables.  Exact functional graphs for
`p=2,3,5`, full augmented anchor maps for the same boxes, and modular
factor/rank checks through `p=31` produced **53,524 assertions**.  The
reviewer also enumerated all functions on the additive group of
`GF(4)`: its image profile is `256/40/4/1`, not the putative prime-field
profile `256/64/16/4`.  This is a positive scope guard: the manuscript's
prime-only quantifier is necessary.

The canonical transcript fixes the coefficient-coordinate edge digest as
`ad8784d9d6a096cd64b7ed79b5cacb81caab8c48c487a2bb8cd4f40584ba5a85`.
Two fresh-process replays after canonicalization matched `CANONICAL.txt`
byte for byte (`PASS/PASS`).  After the author Round-1 documentation repair,
two further fresh reviewer processes again matched it (`PASS/PASS`).

## Claim-by-claim proof audit

| claim under attack | independent derivation | result |
|---|---|---|
| prime scope and difference flag | in binomial coordinates `N` is the single shift `c_j -> c_{j-1}`; the `GF(4)` counterprofile blocks an extension-field reading | pass |
| nonzero-direction layer map | `D_a=N U_a(N)` was reconstructed as a matrix identity for every nonzero `a`, with `U_a(0)=a` and full rank | pass |
| anchored lift | appending the row `c -> c_0` to `D_a:J^i->J^(i+1)` gives a square full-rank matrix; every augmented value was also enumerated for `p<=5` | pass |
| image and every target fibre | each nonzero direction word has one lift and is recovered from its forward orbit; the zero fibre is the remaining source mass | pass |
| sharp rooted clock | the all-one coefficient vector retains anchor one for exactly `p` steps; every enumerated state reaches zero within the proved bound | pass |
| Jordan inventory | `E=P^p` has singleton image and `P^(p+1)=P^p`; on `ker E` the ranks are `p^(p-t)-1`, whose second differences reproduce every stated block count | pass |

The potentially fragile cyclic wrap is harmless: the binomial polynomials
have degree below `p`, and Pascal/Vandermonde identities are polynomial
identities over `F_p`.  The reverse lift is genuinely performed inside
`J^i`; constants lie in every nonterminal layer and evaluation at zero is
bijective on that one-dimensional kernel.  No missing Jordan block or
unproved semisimple component remains.

## Resolved finding

### `P178-S-M1` — Minor — author-verifier provenance terminology — `CLOSED`

The Round-0 package called `verify_p178.py` “independent” in the README and
program docstring.  Round 1 now calls it a “paper-local author-side” verifier
in `README.md:41` and in the docstring; `BUILD.md`, `SELF_QA.md`, and
`PAPER_PLAN.md` use the same process-aware distinction.  The repair is
complete and introduces no theorem or evidentiary overclaim.

## Delta-closeout evidence

- `main.tex` remains
  `d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603`;
  the prime-only quantifiers and all theorem/proof source are unchanged.
- `main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf` are all
  byte-identical at
  `b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce`.
- The paper manifest passes all **16/16** entries.
- Two fresh author-verifier processes reproduce `verification_output.txt`
  exactly: **44,689 assertions**, **3,156 literal arrows**, `RESULT=PASS`.
- Two fresh reviewer-verifier processes reproduce `CANONICAL.txt` exactly:
  **53,524 assertions**, `RESULT=PASS`.

The delta disposition is therefore `CLOSED / 0 OPEN FINDINGS`.

## Ownership and remaining kill switches

The manuscript explicitly subtracts fixed differences, augmentation flags,
linear nilpotent systems, affine kernel counts, and generic rank-to-Jordan
conversion.  The retained conjunction is repeated state selection plus an
observable anchor word and its unique reverse lift.  Direct ownership of that
literal conjunction, loss of the anchored bijection, or any attempt to extend
the theorem from prime fields to arbitrary finite fields would reopen a kill
switch.  The evidence here is not novelty clearance; `OWNER_THIN` and
`HOLD_EXTERNAL` remain mandatory.
