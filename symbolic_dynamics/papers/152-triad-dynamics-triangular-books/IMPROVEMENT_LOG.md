# P152 improvement log — Reviews A and B through Round 2

**Date:** 2026-09-02 UTC.  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.  
**Review input:** `HOSTILE_REVIEW_A.md` returned `REVISE — 0 Critical / 0
Major / 2 Minor`.

This ledger records the author disposition of every Review-A and Review-B
item.  It is not a novelty statement, ownership certificate, or release gate.
No external model or service was used during review or repair.  Scoped
repository synchronization is recorded separately at the batch level.

## m1 — complete paper-local checksum coverage

**Review finding.**  The Round-0 `SHA256SUMS` listed only six core files and
omitted the stable author ledgers.

**Disposition: FIXED.**  After the verifier, transcript, manuscript, ledgers,
build products, historical Round-0 PDF, and new Round-1 PDF were settled,
`SHA256SUMS` was regenerated over every retained paper-local file except the
manifest itself.  It includes the raw Review A, this improvement log, all
source/evidence/build ledgers, verifier/transcript, LaTeX products and logs,
`main_round0_original.pdf`, `main_round1.pdf`, and the Round-1 working
`main.pdf` at that checkpoint.

**Evidence.**

- `main_round0_original.pdf` remains unchanged at 338,268 bytes with SHA-256
  `f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57`.
- The new manifest has 27 entries and a cold
  `sha256sum -c SHA256SUMS` pass.
- That 27-entry manifest is retained as the Round-1 checkpoint; the final
  manifest is regenerated after the Review-B/Round-2 artifacts and ledgers
  settle.

## m2 — inverse-rejection and probabilistic-certificate pressure

**Review finding.**  The largest verifier lane tested only genuine states and
deterministic private clearing.  It did not pressure infeasible exact
`(m,q)` candidates, the two printed scalar collisions, exact block
probabilities, or finite instances of the tail inequality.

**Disposition: FIXED BY EXPANDING THE VERIFIER.**

1. `inverse_criterion()` implements the theorem's exact feasible-image test
   with `Fraction` and integer square roots only.
2. The verifier independently enumerates the literal two-statistic image
   through `r=24` and compares it with the criterion on 7,335 bounded exact
   candidate pairs.  Of these, 69 are accepted and 7,266 rejected.  The grid
   has `m<=20` and minimum `q(1-q)=11/144`, so every feasible scale satisfies
   `R^2<=5760/11<24^2`; the literal search envelope is complete for the grid.
3. Twelve explicit infeasible pairs separately exercise `q` outside `(0,1)`,
   negative and zero scale, nonsquare scale, rational nonintegral scale,
   `R<3`, nonintegral `k=qR`, and `k>R-2`.
4. The two manuscript collision pairs are asserted as genuine one-statistic
   collisions: equal selected statistic, unequal complementary statistic,
   and distinct source states.
5. The verifier sums exact `Fraction` masses over all 8,190 private/spine type
   words through length 12 and recovers `(2/3)^r` for the all-private event.
6. Exact quotient-mass propagation checks 546 instances of
   `P_k(T>nr)<=[1-(2/3)^r]^n` for every start through `r=12` and
   `n=0,...,6`, including equality at `n=0`.

The new lanes contain 7,655 inverse-iff/collision assertions and 648
private-block probability/tail assertions.  The complete frozen run contains
199,581 assertions.  These finite checks remain counterexample pressure; the
symbolic proof, not enumeration, carries the all-parameter iff and tail law.

## Round-1 reproducibility closure

- Fresh verifier stdout is byte-identical to `verification_output.txt`.
- Transcript SHA-256:
  `da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083`.
- The settled local build and two independent source-only builds are
  byte-identical.
- The Round-1 working `main.pdf` and `main_round1.pdf` were byte-identical at
  that checkpoint: 5 A4 pages, 339,258 bytes, SHA-256
  `2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9`.
- All rendered pages, blank identifying metadata, font embedding, references,
  and build logs were checked again; details are frozen in `BUILD.md` and
  `FINAL_QA.md`.
- `main_round0_original.pdf` was preserved and was not overwritten.

The two Review-A Minors were closed at author Round 1.  At that historical
checkpoint, Review B had not yet been performed; external status remained
`HOLD_EXTERNAL`.

## Review B -> Round 2

Review B returned `REVISE — 0 Critical / 0 Major / 1 Minor`.  The raw report
is retained in `HOSTILE_REVIEW_B.md`.

**Finding.**  The arbitrary-candidate inverse statement formed
`R=sqrt(2m/[q(1-q)])` after requiring only `0<q<1`; it did not first require
positive mean or define a negative scale as infeasible, although the verifier
already rejects that boundary.

**Disposition: FIXED.**  The theorem now declares every candidate with
`m<=0` or `q` outside `(0,1)` infeasible before forming `R`. The inverse proof,
proof package, claims ledger, and control ledger state the same gate. The
integer-square, `R>=3`, integral-`k`, and admissible-count iff conditions are
unchanged, as are the verifier and transcript.

## Round-2 execution evidence and acceptance

- A fresh replay remains byte-identical to `verification_output.txt`: 199,581
  exact assertions, transcript SHA-256
  `da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083`.
- Two independent source-only builds reproduce `main.pdf` and
  `main_round2.pdf` byte for byte: 5 A4 pages, 338,933 bytes, SHA-256
  `6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6`.
- The settled log, 25 embedded/subsetted/Unicode-mapped font rows, blank
  identifying metadata, and all five rendered pages pass the final gate.
- `main_round0_original.pdf` and `main_round1.pdf` remain unchanged at their
  recorded Round-0 and Round-1 hashes.

The Review-B Minor is closed in source.  Together with the two previously
closed Review-A Minors, surviving severity is 0 Critical / 0 Major / 0 Minor.
P152 is accepted internally at Round 2 and remains `HOLD_EXTERNAL`.
